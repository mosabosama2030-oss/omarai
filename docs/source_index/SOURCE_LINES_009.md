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
| [SRC-1AE03B9EC3-L003845](../../agents/web_agent.py#L3845) | 3845 | `"                    \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L003846](../../agents/web_agent.py#L3846) | 3846 | `"                    \"search_outcome\": ("` | — |
| [SRC-1AE03B9EC3-L003847](../../agents/web_agent.py#L3847) | 3847 | `"                        \"unknown_after_budget_exhaustion\""` | — |
| [SRC-1AE03B9EC3-L003848](../../agents/web_agent.py#L3848) | 3848 | `"                        if search_attempted"` | — |
| [SRC-1AE03B9EC3-L003849](../../agents/web_agent.py#L3849) | 3849 | `"                        else \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L003850](../../agents/web_agent.py#L3850) | 3850 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L003851](../../agents/web_agent.py#L3851) | 3851 | `"                    \"insufficient_evidence\": True,"` | — |
| [SRC-1AE03B9EC3-L003852](../../agents/web_agent.py#L3852) | 3852 | `"                    \"budget_exhausted\": True,"` | — |
| [SRC-1AE03B9EC3-L003853](../../agents/web_agent.py#L3853) | 3853 | `"                    \"warnings\": [str(exc)],"` | — |
| [SRC-1AE03B9EC3-L003854](../../agents/web_agent.py#L3854) | 3854 | `"                },"` | — |
| [SRC-1AE03B9EC3-L003855](../../agents/web_agent.py#L3855) | 3855 | `"                \"sources\": [],"` | — |
| [SRC-1AE03B9EC3-L003856](../../agents/web_agent.py#L3856) | 3856 | `"                \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L003857](../../agents/web_agent.py#L3857) | 3857 | `"                \"citation_validation\": {\"status\": \"not_checked\"},"` | — |
| [SRC-1AE03B9EC3-L003858](../../agents/web_agent.py#L3858) | 3858 | `"                \"answer_coverage\": {},"` | — |
| [SRC-1AE03B9EC3-L003859](../../agents/web_agent.py#L3859) | 3859 | `"                \"used_language_model\": False,"` | — |
| [SRC-1AE03B9EC3-L003860](../../agents/web_agent.py#L3860) | 3860 | `"                \"used_web_search\": False,"` | — |
| [SRC-1AE03B9EC3-L003861](../../agents/web_agent.py#L3861) | 3861 | `"                \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L003862](../../agents/web_agent.py#L3862) | 3862 | `"                \"used_social_search\": False,"` | — |
| [SRC-1AE03B9EC3-L003863](../../agents/web_agent.py#L3863) | 3863 | `"                \"warnings\": [str(exc)],"` | — |
| [SRC-1AE03B9EC3-L003864](../../agents/web_agent.py#L3864) | 3864 | `"                \"kind\": \"web_fallback\","` | — |
| [SRC-1AE03B9EC3-L003865](../../agents/web_agent.py#L3865) | 3865 | `"                \"final_answer_status\": \"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L003866](../../agents/web_agent.py#L3866) | 3866 | `"                \"intent_route\": \"BUDGET_EXHAUSTED\","` | — |
| [SRC-1AE03B9EC3-L003867](../../agents/web_agent.py#L3867) | 3867 | `"                \"intent_route_reason\": \"request_budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L003868](../../agents/web_agent.py#L3868) | 3868 | `"            }"` | — |
| [SRC-1AE03B9EC3-L003869](../../agents/web_agent.py#L3869) | 3869 | `"        finally:"` | — |
| [SRC-1AE03B9EC3-L003870](../../agents/web_agent.py#L3870) | 3870 | `"            budget_summary = budget.snapshot()"` | — |
| [SRC-1AE03B9EC3-L003871](../../agents/web_agent.py#L3871) | 3871 | `"            self._request_budget = previous_budget"` | — |
| [SRC-1AE03B9EC3-L003872](../../agents/web_agent.py#L3872) | 3872 | `""` | — |
| [SRC-1AE03B9EC3-L003873](../../agents/web_agent.py#L3873) | 3873 | `"        result[\"request_budget\"] = budget_summary"` | — |
| [SRC-1AE03B9EC3-L003874](../../agents/web_agent.py#L3874) | 3874 | `"        result[\"generation_diagnostics\"] = list(self.generation_diagnostics[-12:])"` | — |
| [SRC-1AE03B9EC3-L003875](../../agents/web_agent.py#L3875) | 3875 | `""` | — |
| [SRC-1AE03B9EC3-L003876](../../agents/web_agent.py#L3876) | 3876 | `"        # Keep the public result contract resilient if a fallback/alternate result"` | — |
| [SRC-1AE03B9EC3-L003877](../../agents/web_agent.py#L3877) | 3877 | `"        # builder omitted the lexical integrity fields. Normal research results are"` | — |
| [SRC-1AE03B9EC3-L003878](../../agents/web_agent.py#L3878) | 3878 | `"        # already audited inside _answer_with_budget, so do not duplicate that work."` | — |
| [SRC-1AE03B9EC3-L003879](../../agents/web_agent.py#L3879) | 3879 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L003880](../../agents/web_agent.py#L3880) | 3880 | `"            result.get(\"kind\") in {\"web_research\", \"web_fallback\", \"insufficient_evidence\"}"` | — |
| [SRC-1AE03B9EC3-L003881](../../agents/web_agent.py#L3881) | 3881 | `"            and \"answer_integrity\" not in result"` | — |
| [SRC-1AE03B9EC3-L003882](../../agents/web_agent.py#L3882) | 3882 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L003883](../../agents/web_agent.py#L3883) | 3883 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L003884](../../agents/web_agent.py#L3884) | 3884 | `"                coverage_targets = self._question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L003885](../../agents/web_agent.py#L3885) | 3885 | `"                source_rows = result.get(\"sources\")"` | — |
| [SRC-1AE03B9EC3-L003886](../../agents/web_agent.py#L3886) | 3886 | `"                safe_sources = source_rows if isinstance(source_rows, list) else []"` | — |
| [SRC-1AE03B9EC3-L003887](../../agents/web_agent.py#L3887) | 3887 | `"                answer_integrity = audit_answer_integrity("` | — |
| [SRC-1AE03B9EC3-L003888](../../agents/web_agent.py#L3888) | 3888 | `"                    question,"` | — |
| [SRC-1AE03B9EC3-L003889](../../agents/web_agent.py#L3889) | 3889 | `"                    str(result.get(\"answer\") or \"\"),"` | — |
| [SRC-1AE03B9EC3-L003890](../../agents/web_agent.py#L3890) | 3890 | `"                    safe_sources,"` | — |
| [SRC-1AE03B9EC3-L003891](../../agents/web_agent.py#L3891) | 3891 | `"                    coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L003892](../../agents/web_agent.py#L3892) | 3892 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003893](../../agents/web_agent.py#L3893) | 3893 | `"                result[\"answer_integrity\"] = answer_integrity"` | — |
| [SRC-1AE03B9EC3-L003894](../../agents/web_agent.py#L3894) | 3894 | `"                coverage = result.get(\"answer_coverage\")"` | — |
| [SRC-1AE03B9EC3-L003895](../../agents/web_agent.py#L3895) | 3895 | `"                if not isinstance(coverage, dict):"` | — |
| [SRC-1AE03B9EC3-L003896](../../agents/web_agent.py#L3896) | 3896 | `"                    coverage = {}"` | — |
| [SRC-1AE03B9EC3-L003897](../../agents/web_agent.py#L3897) | 3897 | `"                coverage[\"targets\"] = coverage_targets"` | — |
| [SRC-1AE03B9EC3-L003898](../../agents/web_agent.py#L3898) | 3898 | `"                coverage[\"target_checks\"] = answer_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L003899](../../agents/web_agent.py#L3899) | 3899 | `"                coverage[\"potentially_missing_target_count\"] = ("` | — |
| [SRC-1AE03B9EC3-L003900](../../agents/web_agent.py#L3900) | 3900 | `"                    answer_integrity[\"potentially_missing_target_count\"]"` | — |
| [SRC-1AE03B9EC3-L003901](../../agents/web_agent.py#L3901) | 3901 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003902](../../agents/web_agent.py#L3902) | 3902 | `"                coverage[\"lexical_screen_method\"] = ("` | — |
| [SRC-1AE03B9EC3-L003903](../../agents/web_agent.py#L3903) | 3903 | `"                    \"deterministic_lexical_screen_only_not_semantic_grading\""` | — |
| [SRC-1AE03B9EC3-L003904](../../agents/web_agent.py#L3904) | 3904 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003905](../../agents/web_agent.py#L3905) | 3905 | `"                if ("` | — |
| [SRC-1AE03B9EC3-L003906](../../agents/web_agent.py#L3906) | 3906 | `"                    result.get(\"kind\") == \"insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L003907](../../agents/web_agent.py#L3907) | 3907 | `"                    or result.get(\"research_quality\") == \"failed\""` | — |
| [SRC-1AE03B9EC3-L003908](../../agents/web_agent.py#L3908) | 3908 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L003909](../../agents/web_agent.py#L3909) | 3909 | `"                    fulfillment_status = ("` | — |
| [SRC-1AE03B9EC3-L003910](../../agents/web_agent.py#L3910) | 3910 | `"                        \"not_assessed_insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L003911](../../agents/web_agent.py#L3911) | 3911 | `"                        if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L003912](../../agents/web_agent.py#L3912) | 3912 | `"                        else \"not_machine_assessed_no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L003913](../../agents/web_agent.py#L3913) | 3913 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003914](../../agents/web_agent.py#L3914) | 3914 | `"                elif answer_integrity[\"potentially_missing_target_count\"] > 0:"` | — |
| [SRC-1AE03B9EC3-L003915](../../agents/web_agent.py#L3915) | 3915 | `"                    fulfillment_status = \"possible_gap_detected\""` | — |
| [SRC-1AE03B9EC3-L003916](../../agents/web_agent.py#L3916) | 3916 | `"                elif coverage_targets:"` | — |
| [SRC-1AE03B9EC3-L003917](../../agents/web_agent.py#L3917) | 3917 | `"                    fulfillment_status = \"lexical_signals_found_not_semantically_verified\""` | — |
| [SRC-1AE03B9EC3-L003918](../../agents/web_agent.py#L3918) | 3918 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L003919](../../agents/web_agent.py#L3919) | 3919 | `"                    fulfillment_status = \"not_machine_assessed_no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L003920](../../agents/web_agent.py#L3920) | 3920 | `"                coverage[\"task_fulfillment_status\"] = fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L003921](../../agents/web_agent.py#L3921) | 3921 | `"                result[\"answer_coverage\"] = coverage"` | — |
| [SRC-1AE03B9EC3-L003922](../../agents/web_agent.py#L3922) | 3922 | `"                result[\"task_fulfillment_status\"] = fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L003923](../../agents/web_agent.py#L3923) | 3923 | `"                if isinstance(result.get(\"search_report\"), dict):"` | — |
| [SRC-1AE03B9EC3-L003924](../../agents/web_agent.py#L3924) | 3924 | `"                    result[\"search_report\"][\"answer_integrity\"] = answer_integrity"` | — |
| [SRC-1AE03B9EC3-L003925](../../agents/web_agent.py#L3925) | 3925 | `"                    result[\"search_report\"][\"task_fulfillment_status\"] = fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L003926](../../agents/web_agent.py#L3926) | 3926 | `"            except (AttributeError, KeyError, TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L003927](../../agents/web_agent.py#L3927) | 3927 | `"                # Auxiliary integrity screening never replaces the actual answer."` | — |
| [SRC-1AE03B9EC3-L003928](../../agents/web_agent.py#L3928) | 3928 | `"                result[\"answer_integrity\"] = {"` | — |
| [SRC-1AE03B9EC3-L003929](../../agents/web_agent.py#L3929) | 3929 | `"                    \"method\": \"deterministic_lexical_screen_only\","` | — |
| [SRC-1AE03B9EC3-L003930](../../agents/web_agent.py#L3930) | 3930 | `"                    \"status\": \"not_run\","` | — |
| [SRC-1AE03B9EC3-L003931](../../agents/web_agent.py#L3931) | 3931 | `"                    \"semantic_verification\": False,"` | — |
| [SRC-1AE03B9EC3-L003932](../../agents/web_agent.py#L3932) | 3932 | `"                    \"independent_fact_check\": False,"` | — |
| [SRC-1AE03B9EC3-L003933](../../agents/web_agent.py#L3933) | 3933 | `"                    \"error_class\": \"integrity_screen_error\","` | — |
| [SRC-1AE03B9EC3-L003934](../../agents/web_agent.py#L3934) | 3934 | `"                }"` | — |
| [SRC-1AE03B9EC3-L003935](../../agents/web_agent.py#L3935) | 3935 | `"                result.setdefault(\"warnings\", []).append("` | — |
| [SRC-1AE03B9EC3-L003936](../../agents/web_agent.py#L3936) | 3936 | `"                    \"تعذر تشغيل الفحص اللفظي الأولي لسلامة الأدلة؛ لم يُعدّ ذلك إثباتًا أو نفيًا لصحة الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L003937](../../agents/web_agent.py#L3937) | 3937 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003938](../../agents/web_agent.py#L3938) | 3938 | `"        if \"final_answer_status\" not in result:"` | — |
| [SRC-1AE03B9EC3-L003939](../../agents/web_agent.py#L3939) | 3939 | `"            if result.get(\"kind\") in {\"capability_answer\", \"local_conversation\"}:"` | — |
| [SRC-1AE03B9EC3-L003940](../../agents/web_agent.py#L3940) | 3940 | `"                final_answer_status = \"local_response_no_generation\""` | — |
| [SRC-1AE03B9EC3-L003941](../../agents/web_agent.py#L3941) | 3941 | `"            elif result.get(\"kind\") == \"insufficient_evidence\":"` | — |
| [SRC-1AE03B9EC3-L003942](../../agents/web_agent.py#L3942) | 3942 | `"                final_answer_status = \"insufficient_evidence_no_generation\""` | — |
| [SRC-1AE03B9EC3-L003943](../../agents/web_agent.py#L3943) | 3943 | `"            elif result.get(\"used_language_model\") is True:"` | — |
| [SRC-1AE03B9EC3-L003944](../../agents/web_agent.py#L3944) | 3944 | `"                final_answer_status = \"model_answer_generated\""` | — |
| [SRC-1AE03B9EC3-L003945](../../agents/web_agent.py#L3945) | 3945 | `"            elif self.generation_diagnostics:"` | — |
| [SRC-1AE03B9EC3-L003946](../../agents/web_agent.py#L3946) | 3946 | `"                final_answer_status = ("` | — |
| [SRC-1AE03B9EC3-L003947](../../agents/web_agent.py#L3947) | 3947 | `"                    \"generation_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L003948](../../agents/web_agent.py#L3948) | 3948 | `"                    if result.get(\"sources\")"` | — |
| [SRC-1AE03B9EC3-L003949](../../agents/web_agent.py#L3949) | 3949 | `"                    else \"generation_failed\""` | — |
| [SRC-1AE03B9EC3-L003950](../../agents/web_agent.py#L3950) | 3950 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003951](../../agents/web_agent.py#L3951) | 3951 | `"            elif result.get(\"kind\") == \"clarification\":"` | — |
| [SRC-1AE03B9EC3-L003952](../../agents/web_agent.py#L3952) | 3952 | `"                final_answer_status = \"clarification_required\""` | — |
| [SRC-1AE03B9EC3-L003953](../../agents/web_agent.py#L3953) | 3953 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L003954](../../agents/web_agent.py#L3954) | 3954 | `"                final_answer_status = \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L003955](../../agents/web_agent.py#L3955) | 3955 | `"            result[\"final_answer_status\"] = final_answer_status"` | — |
| [SRC-1AE03B9EC3-L003956](../../agents/web_agent.py#L3956) | 3956 | `"        if isinstance(result.get(\"search_report\"), dict):"` | — |
| [SRC-1AE03B9EC3-L003957](../../agents/web_agent.py#L3957) | 3957 | `"            result[\"search_report\"][\"request_budget\"] = budget_summary"` | — |
| [SRC-1AE03B9EC3-L003958](../../agents/web_agent.py#L3958) | 3958 | `"        if budget_summary[\"deadline_exceeded\"]:"` | — |
| [SRC-1AE03B9EC3-L003959](../../agents/web_agent.py#L3959) | 3959 | `"            result.setdefault(\"warnings\", []).append("` | — |
| [SRC-1AE03B9EC3-L003960](../../agents/web_agent.py#L3960) | 3960 | `"                \"انتهت نافذة الوقت المحددة للطلب أو جرى تجاوزها قليلًا أثناء إنهاء اتصال جارٍ.\""` | — |
| [SRC-1AE03B9EC3-L003961](../../agents/web_agent.py#L3961) | 3961 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003962](../../agents/web_agent.py#L3962) | 3962 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L003963](../../agents/web_agent.py#L3963) | 3963 | `""` | — |
| [SRC-1AE03B9EC3-L003964](../../agents/web_agent.py#L3964) | 3964 | `"    def _answer_with_budget("` | — |
| [SRC-1AE03B9EC3-L003965](../../agents/web_agent.py#L3965) | 3965 | `"        self, question: str, history: Any = None, mode: str = \"auto\""` | — |
| [SRC-1AE03B9EC3-L003966](../../agents/web_agent.py#L3966) | 3966 | `"    ) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L003967](../../agents/web_agent.py#L3967) | 3967 | `"        if not isinstance(question, str) or not question.strip():"` | — |
| [SRC-1AE03B9EC3-L003968](../../agents/web_agent.py#L3968) | 3968 | `"            raise ValueError(\"اكتب سؤالًا غير فارغ.\")"` | — |
| [SRC-1AE03B9EC3-L003969](../../agents/web_agent.py#L3969) | 3969 | `"        question = question.strip()"` | — |
| [SRC-1AE03B9EC3-L003970](../../agents/web_agent.py#L3970) | 3970 | `"        if len(question) > MAX_QUESTION_CHARS:"` | — |
| [SRC-1AE03B9EC3-L003971](../../agents/web_agent.py#L3971) | 3971 | `"            raise ValueError(f\"السؤال طويل جدًا؛ الحد الأقصى {MAX_QUESTION_CHARS} حرف.\")"` | — |
| [SRC-1AE03B9EC3-L003972](../../agents/web_agent.py#L3972) | 3972 | `"        clean_history = self._sanitize_history(history)"` | — |
| [SRC-1AE03B9EC3-L003973](../../agents/web_agent.py#L3973) | 3973 | `"        self._reset_deepseek_search_budget()"` | — |
| [SRC-1AE03B9EC3-L003974](../../agents/web_agent.py#L3974) | 3974 | `"        self.server_search_sources = []"` | — |
| [SRC-1AE03B9EC3-L003975](../../agents/web_agent.py#L3975) | 3975 | `"        self.model_usage = []"` | — |
| [SRC-1AE03B9EC3-L003976](../../agents/web_agent.py#L3976) | 3976 | `"        self.generation_diagnostics = []"` | — |
| [SRC-1AE03B9EC3-L003977](../../agents/web_agent.py#L3977) | 3977 | `"        with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L003978](../../agents/web_agent.py#L3978) | 3978 | `"            self._provider_diagnostics = []"` | — |
| [SRC-1AE03B9EC3-L003979](../../agents/web_agent.py#L3979) | 3979 | `"        clean_mode = mode.strip().lower() if isinstance(mode, str) else \"auto\""` | — |
| [SRC-1AE03B9EC3-L003980](../../agents/web_agent.py#L3980) | 3980 | `"        if clean_mode not in {\"auto\", \"deep\", \"latest\", \"social\"}:"` | — |
| [SRC-1AE03B9EC3-L003981](../../agents/web_agent.py#L3981) | 3981 | `"            raise ValueError(\"نمط البحث غير مدعوم. اختر auto أو deep أو latest أو social.\")"` | — |
| [SRC-1AE03B9EC3-L003982](../../agents/web_agent.py#L3982) | 3982 | `"        current_search_status_question = self._is_current_search_status_question(question)"` | — |
| [SRC-1AE03B9EC3-L003983](../../agents/web_agent.py#L3983) | 3983 | `"        # Explicit UI modes control research tasks, but must not turn a status"` | — |
| [SRC-1AE03B9EC3-L003984](../../agents/web_agent.py#L3984) | 3984 | `"        # question about this answer into a new web-search request."` | — |
| [SRC-1AE03B9EC3-L003985](../../agents/web_agent.py#L3985) | 3985 | `"        routing_mode = \"auto\" if current_search_status_question else clean_mode"` | — |
| [SRC-1AE03B9EC3-L003986](../../agents/web_agent.py#L3986) | 3986 | `"        decision = route_intent("` | — |
| [SRC-1AE03B9EC3-L003987](../../agents/web_agent.py#L3987) | 3987 | `"            question,"` | — |
| [SRC-1AE03B9EC3-L003988](../../agents/web_agent.py#L3988) | 3988 | `"            clean_history,"` | — |
| [SRC-1AE03B9EC3-L003989](../../agents/web_agent.py#L3989) | 3989 | `"            routing_mode,"` | — |
| [SRC-1AE03B9EC3-L003990](../../agents/web_agent.py#L3990) | 3990 | `"            capability_question=self._is_self_question(question),"` | — |
| [SRC-1AE03B9EC3-L003991](../../agents/web_agent.py#L3991) | 3991 | `"            requires_web=self._requires_web_research(question, routing_mode),"` | — |
| [SRC-1AE03B9EC3-L003992](../../agents/web_agent.py#L3992) | 3992 | `"        )"` | — |
| [SRC-1AE03B9EC3-L003993](../../agents/web_agent.py#L3993) | 3993 | `"        intent_route = str(decision[\"route\"])"` | — |
| [SRC-1AE03B9EC3-L003994](../../agents/web_agent.py#L3994) | 3994 | `"        intent_reason = str(decision[\"reason\"])"` | — |
| [SRC-1AE03B9EC3-L003995](../../agents/web_agent.py#L3995) | 3995 | `""` | — |
| [SRC-1AE03B9EC3-L003996](../../agents/web_agent.py#L3996) | 3996 | `"        if intent_route == \"LOCAL\":"` | — |
| [SRC-1AE03B9EC3-L003997](../../agents/web_agent.py#L3997) | 3997 | `"            if self._is_self_question(question):"` | — |
| [SRC-1AE03B9EC3-L003998](../../agents/web_agent.py#L3998) | 3998 | `"                local_result = self._self_description_answer(question)"` | — |
| [SRC-1AE03B9EC3-L003999](../../agents/web_agent.py#L3999) | 3999 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L004000](../../agents/web_agent.py#L4000) | 4000 | `"                local_result = self._local_answer_result("` | — |
| [SRC-1AE03B9EC3-L004001](../../agents/web_agent.py#L4001) | 4001 | `"                    question, self._local_conversation_reply(question), \"local_conversation\""` | — |
| [SRC-1AE03B9EC3-L004002](../../agents/web_agent.py#L4002) | 4002 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004003](../../agents/web_agent.py#L4003) | 4003 | `"            return self._annotate_intent_route("` | — |
| [SRC-1AE03B9EC3-L004004](../../agents/web_agent.py#L4004) | 4004 | `"                local_result, intent_route, intent_reason, clean_mode"` | — |
| [SRC-1AE03B9EC3-L004005](../../agents/web_agent.py#L4005) | 4005 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004006](../../agents/web_agent.py#L4006) | 4006 | `""` | — |
| [SRC-1AE03B9EC3-L004007](../../agents/web_agent.py#L4007) | 4007 | `"        if intent_route == \"CLARIFY\":"` | — |
| [SRC-1AE03B9EC3-L004008](../../agents/web_agent.py#L4008) | 4008 | `"            return self._clarification_result(question, clean_mode, decision)"` | — |
| [SRC-1AE03B9EC3-L004009](../../agents/web_agent.py#L4009) | 4009 | `""` | — |
| [SRC-1AE03B9EC3-L004010](../../agents/web_agent.py#L4010) | 4010 | `"        if intent_route == \"MODEL_ONLY\":"` | — |
| [SRC-1AE03B9EC3-L004011](../../agents/web_agent.py#L4011) | 4011 | `"            general_answer = self._answer_without_search(question, clean_history)"` | — |
| [SRC-1AE03B9EC3-L004012](../../agents/web_agent.py#L4012) | 4012 | `"            if general_answer is not None:"` | — |
| [SRC-1AE03B9EC3-L004013](../../agents/web_agent.py#L4013) | 4013 | `"                return self._annotate_intent_route("` | — |
| [SRC-1AE03B9EC3-L004014](../../agents/web_agent.py#L4014) | 4014 | `"                    general_answer, intent_route, intent_reason, clean_mode"` | — |
| [SRC-1AE03B9EC3-L004015](../../agents/web_agent.py#L4015) | 4015 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004016](../../agents/web_agent.py#L4016) | 4016 | `"            # Preserve the existing degraded-mode behavior when generation is unavailable:"` | — |
| [SRC-1AE03B9EC3-L004017](../../agents/web_agent.py#L4017) | 4017 | `"            # run the current web pipeline rather than fabricate a model-only answer."` | — |
| [SRC-1AE03B9EC3-L004018](../../agents/web_agent.py#L4018) | 4018 | `"            intent_route = \"WEB_SIMPLE\""` | — |
| [SRC-1AE03B9EC3-L004019](../../agents/web_agent.py#L4019) | 4019 | `"            intent_reason = \"model_unavailable_fallback_to_existing_web_research\""` | — |
| [SRC-1AE03B9EC3-L004020](../../agents/web_agent.py#L4020) | 4020 | `""` | — |
| [SRC-1AE03B9EC3-L004021](../../agents/web_agent.py#L4021) | 4021 | `"        plan = self._plan_search(question, clean_history)"` | — |
| [SRC-1AE03B9EC3-L004022](../../agents/web_agent.py#L4022) | 4022 | `"        plan[\"mode\"] = clean_mode"` | — |
| [SRC-1AE03B9EC3-L004023](../../agents/web_agent.py#L4023) | 4023 | `"        plan[\"intent_route\"] = intent_route"` | — |
| [SRC-1AE03B9EC3-L004024](../../agents/web_agent.py#L4024) | 4024 | `"        plan[\"intent_route_reason\"] = intent_reason"` | — |
| [SRC-1AE03B9EC3-L004025](../../agents/web_agent.py#L4025) | 4025 | `"        # Normalize planner output before depth/mode expansion so a raw instruction-only"` | — |
| [SRC-1AE03B9EC3-L004026](../../agents/web_agent.py#L4026) | 4026 | `"        # prompt cannot seed synthetic generic queries when the topic is empty."` | — |
| [SRC-1AE03B9EC3-L004027](../../agents/web_agent.py#L4027) | 4027 | `"        raw_plan_queries = plan.get(\"queries\") or []"` | — |
| [SRC-1AE03B9EC3-L004028](../../agents/web_agent.py#L4028) | 4028 | `"        if not isinstance(raw_plan_queries, list):"` | — |
| [SRC-1AE03B9EC3-L004029](../../agents/web_agent.py#L4029) | 4029 | `"            raw_plan_queries = []"` | — |
| [SRC-1AE03B9EC3-L004030](../../agents/web_agent.py#L4030) | 4030 | `"        normalized_plan_queries = []"` | — |
| [SRC-1AE03B9EC3-L004031](../../agents/web_agent.py#L4031) | 4031 | `"        for raw_query in raw_plan_queries:"` | — |
| [SRC-1AE03B9EC3-L004032](../../agents/web_agent.py#L4032) | 4032 | `"            if not isinstance(raw_query, str) or not raw_query.strip():"` | — |
| [SRC-1AE03B9EC3-L004033](../../agents/web_agent.py#L4033) | 4033 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L004034](../../agents/web_agent.py#L4034) | 4034 | `"            compacted_query = compact_search_query(raw_query)"` | — |
| [SRC-1AE03B9EC3-L004035](../../agents/web_agent.py#L4035) | 4035 | `"            if ("` | — |
| [SRC-1AE03B9EC3-L004036](../../agents/web_agent.py#L4036) | 4036 | `"                compacted_query"` | — |
| [SRC-1AE03B9EC3-L004037](../../agents/web_agent.py#L4037) | 4037 | `"                and _relevance_query_tokens(compacted_query)"` | — |
| [SRC-1AE03B9EC3-L004038](../../agents/web_agent.py#L4038) | 4038 | `"                and compacted_query not in normalized_plan_queries"` | — |
| [SRC-1AE03B9EC3-L004039](../../agents/web_agent.py#L4039) | 4039 | `"            ):"` | — |
| [SRC-1AE03B9EC3-L004040](../../agents/web_agent.py#L4040) | 4040 | `"                normalized_plan_queries.append(compacted_query)"` | — |
| [SRC-1AE03B9EC3-L004041](../../agents/web_agent.py#L4041) | 4041 | `"        plan[\"queries\"] = normalized_plan_queries[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004042](../../agents/web_agent.py#L4042) | 4042 | `"        # Preserve the requested mode in diagnostics even when no usable query exists."` | — |
| [SRC-1AE03B9EC3-L004043](../../agents/web_agent.py#L4043) | 4043 | `"        if clean_mode == \"deep\":"` | — |
| [SRC-1AE03B9EC3-L004044](../../agents/web_agent.py#L4044) | 4044 | `"            plan[\"depth\"] = \"deep\""` | — |
| [SRC-1AE03B9EC3-L004045](../../agents/web_agent.py#L4045) | 4045 | `"        elif clean_mode == \"latest\":"` | — |
| [SRC-1AE03B9EC3-L004046](../../agents/web_agent.py#L4046) | 4046 | `"            plan[\"freshness\"] = \"current\""` | — |
| [SRC-1AE03B9EC3-L004047](../../agents/web_agent.py#L4047) | 4047 | `"        elif clean_mode == \"social\":"` | — |
| [SRC-1AE03B9EC3-L004048](../../agents/web_agent.py#L4048) | 4048 | `"            plan[\"social_focus\"] = True"` | — |
| [SRC-1AE03B9EC3-L004049](../../agents/web_agent.py#L4049) | 4049 | `"            if not plan.get(\"platforms\"):"` | — |
| [SRC-1AE03B9EC3-L004050](../../agents/web_agent.py#L4050) | 4050 | `"                plan[\"platforms\"] = [\"reddit\", \"bluesky\", \"youtube\"]"` | — |
| [SRC-1AE03B9EC3-L004051](../../agents/web_agent.py#L4051) | 4051 | `""` | — |
| [SRC-1AE03B9EC3-L004052](../../agents/web_agent.py#L4052) | 4052 | `"        if plan.get(\"queries\"):"` | — |
| [SRC-1AE03B9EC3-L004053](../../agents/web_agent.py#L4053) | 4053 | `"            if clean_mode == \"auto\" and intent_route == \"WEB_DEEP\":"` | — |
| [SRC-1AE03B9EC3-L004054](../../agents/web_agent.py#L4054) | 4054 | `"                plan[\"depth\"] = \"deep\""` | — |
| [SRC-1AE03B9EC3-L004055](../../agents/web_agent.py#L4055) | 4055 | `"            if clean_mode == \"auto\":"` | — |
| [SRC-1AE03B9EC3-L004056](../../agents/web_agent.py#L4056) | 4056 | `"                normalized_question = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L004057](../../agents/web_agent.py#L4057) | 4057 | `"                deep_terms = ("` | — |
| [SRC-1AE03B9EC3-L004058](../../agents/web_agent.py#L4058) | 4058 | `"                    \"بحث عميق\", \"بحث معمق\", \"بحث شامل\", \"بالتفصيل\", \"قارن\", \"مقارنة\","` | — |
| [SRC-1AE03B9EC3-L004059](../../agents/web_agent.py#L4059) | 4059 | `"                    \"تحقق\", \"استقصاء\", \"deep research\", \"comprehensive\", \"in-depth\", \"compare\","` | — |
| [SRC-1AE03B9EC3-L004060](../../agents/web_agent.py#L4060) | 4060 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004061](../../agents/web_agent.py#L4061) | 4061 | `"                explicit_deep = intent_route == \"WEB_DEEP\" or any("` | — |
| [SRC-1AE03B9EC3-L004062](../../agents/web_agent.py#L4062) | 4062 | `"                    term in normalized_question for term in deep_terms"` | — |
| [SRC-1AE03B9EC3-L004063](../../agents/web_agent.py#L4063) | 4063 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004064](../../agents/web_agent.py#L4064) | 4064 | `"                if not explicit_deep:"` | — |
| [SRC-1AE03B9EC3-L004065](../../agents/web_agent.py#L4065) | 4065 | `"                    # The planner may overclassify short lookups as deep research. Preserve"` | — |
| [SRC-1AE03B9EC3-L004066](../../agents/web_agent.py#L4066) | 4066 | `"                    # the user's actual intent first and cap routine searches to three queries."` | — |
| [SRC-1AE03B9EC3-L004067](../../agents/web_agent.py#L4067) | 4067 | `"                    fallback_plan_queries = ("` | — |
| [SRC-1AE03B9EC3-L004068](../../agents/web_agent.py#L4068) | 4068 | `"                        fallback_plan(question, clean_history).get(\"queries\") or []"` | — |
| [SRC-1AE03B9EC3-L004069](../../agents/web_agent.py#L4069) | 4069 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004070](../../agents/web_agent.py#L4070) | 4070 | `"                    fallback_queries = ["` | — |
| [SRC-1AE03B9EC3-L004071](../../agents/web_agent.py#L4071) | 4071 | `"                        compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L004072](../../agents/web_agent.py#L4072) | 4072 | `"                        for query in fallback_plan_queries"` | — |
| [SRC-1AE03B9EC3-L004073](../../agents/web_agent.py#L4073) | 4073 | `"                        if isinstance(query, str)"` | — |
| [SRC-1AE03B9EC3-L004074](../../agents/web_agent.py#L4074) | 4074 | `"                    ]"` | — |
| [SRC-1AE03B9EC3-L004075](../../agents/web_agent.py#L4075) | 4075 | `"                    fallback_queries = [query for query in fallback_queries if query]"` | — |
| [SRC-1AE03B9EC3-L004076](../../agents/web_agent.py#L4076) | 4076 | `"                    model_queries = ["` | — |
| [SRC-1AE03B9EC3-L004077](../../agents/web_agent.py#L4077) | 4077 | `"                        compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L004078](../../agents/web_agent.py#L4078) | 4078 | `"                        for query in (plan.get(\"queries\") or [])"` | — |
| [SRC-1AE03B9EC3-L004079](../../agents/web_agent.py#L4079) | 4079 | `"                        if isinstance(query, str)"` | — |
| [SRC-1AE03B9EC3-L004080](../../agents/web_agent.py#L4080) | 4080 | `"                    ]"` | — |
| [SRC-1AE03B9EC3-L004081](../../agents/web_agent.py#L4081) | 4081 | `"                    model_queries = [query for query in model_queries if query]"` | — |
| [SRC-1AE03B9EC3-L004082](../../agents/web_agent.py#L4082) | 4082 | `"                    if self._is_navigation_request(question):"` | — |
| [SRC-1AE03B9EC3-L004083](../../agents/web_agent.py#L4083) | 4083 | `"                        navigation_seed = ("` | — |
| [SRC-1AE03B9EC3-L004084](../../agents/web_agent.py#L4084) | 4084 | `"                            fallback_queries[0] if fallback_queries"` | — |
| [SRC-1AE03B9EC3-L004085](../../agents/web_agent.py#L4085) | 4085 | `"                            else model_queries[0] if model_queries"` | — |
| [SRC-1AE03B9EC3-L004086](../../agents/web_agent.py#L4086) | 4086 | `"                            else \"\""` | — |
| [SRC-1AE03B9EC3-L004087](../../agents/web_agent.py#L4087) | 4087 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004088](../../agents/web_agent.py#L4088) | 4088 | `"                        subject = re.sub("` | — |
| [SRC-1AE03B9EC3-L004089](../../agents/web_agent.py#L4089) | 4089 | `"                            r\"^(?:ابحث\|بحث\|دور\|اعثر)\\s+(?:عن\|على)?\\s*\","` | — |
| [SRC-1AE03B9EC3-L004090](../../agents/web_agent.py#L4090) | 4090 | `"                            \"\","` | — |
| [SRC-1AE03B9EC3-L004091](../../agents/web_agent.py#L4091) | 4091 | `"                            navigation_seed,"` | — |
| [SRC-1AE03B9EC3-L004092](../../agents/web_agent.py#L4092) | 4092 | `"                        ).strip()"` | — |
| [SRC-1AE03B9EC3-L004093](../../agents/web_agent.py#L4093) | 4093 | `"                        plan_queries = ("` | — |
| [SRC-1AE03B9EC3-L004094](../../agents/web_agent.py#L4094) | 4094 | `"                            ["` | — |
| [SRC-1AE03B9EC3-L004095](../../agents/web_agent.py#L4095) | 4095 | `"                                subject,"` | — |
| [SRC-1AE03B9EC3-L004096](../../agents/web_agent.py#L4096) | 4096 | `"                                subject + \" الموقع الرسمي\","` | — |
| [SRC-1AE03B9EC3-L004097](../../agents/web_agent.py#L4097) | 4097 | `"                                subject + \" official website\","` | — |
| [SRC-1AE03B9EC3-L004098](../../agents/web_agent.py#L4098) | 4098 | `"                            ]"` | — |
| [SRC-1AE03B9EC3-L004099](../../agents/web_agent.py#L4099) | 4099 | `"                            if subject else []"` | — |
| [SRC-1AE03B9EC3-L004100](../../agents/web_agent.py#L4100) | 4100 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004101](../../agents/web_agent.py#L4101) | 4101 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L004102](../../agents/web_agent.py#L4102) | 4102 | `"                        plan_queries = (fallback_queries[:1] or model_queries[:1]) + model_queries"` | — |
| [SRC-1AE03B9EC3-L004103](../../agents/web_agent.py#L4103) | 4103 | `"                    plan[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L004104](../../agents/web_agent.py#L4104) | 4104 | `"                        query.strip() for query in plan_queries if isinstance(query, str) and query.strip()"` | — |
| [SRC-1AE03B9EC3-L004105](../../agents/web_agent.py#L4105) | 4105 | `"                    ))[:3]"` | — |
| [SRC-1AE03B9EC3-L004106](../../agents/web_agent.py#L4106) | 4106 | `"                    plan[\"depth\"] = \"standard\""` | — |
| [SRC-1AE03B9EC3-L004107](../../agents/web_agent.py#L4107) | 4107 | `"            base_query = (plan.get(\"queries\") or [\"\"])[0]"` | — |
| [SRC-1AE03B9EC3-L004108](../../agents/web_agent.py#L4108) | 4108 | `"            if clean_mode == \"auto\" and intent_route == \"WEB_DEEP\" and base_query:"` | — |
| [SRC-1AE03B9EC3-L004109](../../agents/web_agent.py#L4109) | 4109 | `"                deep_candidates = ["` | — |
| [SRC-1AE03B9EC3-L004110](../../agents/web_agent.py#L4110) | 4110 | `"                    f\"{base_query} official sources evidence\","` | — |
| [SRC-1AE03B9EC3-L004111](../../agents/web_agent.py#L4111) | 4111 | `"                    f\"{base_query} risks limitations alternatives\","` | — |
| [SRC-1AE03B9EC3-L004112](../../agents/web_agent.py#L4112) | 4112 | `"                    f\"{base_query} recent data reviews comparison\","` | — |
| [SRC-1AE03B9EC3-L004113](../../agents/web_agent.py#L4113) | 4113 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004114](../../agents/web_agent.py#L4114) | 4114 | `"                normalized_question = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L004115](../../agents/web_agent.py#L4115) | 4115 | `"                property_terms = ("` | — |
| [SRC-1AE03B9EC3-L004116](../../agents/web_agent.py#L4116) | 4116 | `"                    \"شقه\", \"شقق\", \"عقار\", \"عقارات\", \"فيلا\", \"فلل\","` | — |
| [SRC-1AE03B9EC3-L004117](../../agents/web_agent.py#L4117) | 4117 | `"                    \"apartment\", \"apartments\", \"flat\", \"real estate\", \"property\", \"house\", \"villa\","` | — |
| [SRC-1AE03B9EC3-L004118](../../agents/web_agent.py#L4118) | 4118 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004119](../../agents/web_agent.py#L4119) | 4119 | `"                if self._is_listing_discovery(question) and any("` | — |
| [SRC-1AE03B9EC3-L004120](../../agents/web_agent.py#L4120) | 4120 | `"                    term in normalized_question for term in property_terms"` | — |
| [SRC-1AE03B9EC3-L004121](../../agents/web_agent.py#L4121) | 4121 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L004122](../../agents/web_agent.py#L4122) | 4122 | `"                    deep_candidates.extend(["` | — |
| [SRC-1AE03B9EC3-L004123](../../agents/web_agent.py#L4123) | 4123 | `"                        f\"{base_query} إعلانات عقارية ومواقع العقارات\","` | — |
| [SRC-1AE03B9EC3-L004124](../../agents/web_agent.py#L4124) | 4124 | `"                        f\"{base_query} متوسط أسعار السوق للمتر\","` | — |
| [SRC-1AE03B9EC3-L004125](../../agents/web_agent.py#L4125) | 4125 | `"                        f\"{base_query} مواصفات الوحدات والمساحات وطرق السداد\","` | — |
| [SRC-1AE03B9EC3-L004126](../../agents/web_agent.py#L4126) | 4126 | `"                    ])"` | — |
| [SRC-1AE03B9EC3-L004127](../../agents/web_agent.py#L4127) | 4127 | `"                plan[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L004128](../../agents/web_agent.py#L4128) | 4128 | `"                    (plan.get(\"queries\") or [])[:5] + deep_candidates"` | — |
| [SRC-1AE03B9EC3-L004129](../../agents/web_agent.py#L4129) | 4129 | `"                ))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004130](../../agents/web_agent.py#L4130) | 4130 | `"                base_query = (plan.get(\"queries\") or [\"\"])[0]"` | — |
| [SRC-1AE03B9EC3-L004131](../../agents/web_agent.py#L4131) | 4131 | `"            # Explicit user-selected modes are control inputs. They do not bypass source"` | — |
| [SRC-1AE03B9EC3-L004132](../../agents/web_agent.py#L4132) | 4132 | `"            # validation and never permit private-source access."` | — |
| [SRC-1AE03B9EC3-L004133](../../agents/web_agent.py#L4133) | 4133 | `"            if clean_mode == \"deep\":"` | — |
| [SRC-1AE03B9EC3-L004134](../../agents/web_agent.py#L4134) | 4134 | `"                plan[\"depth\"] = \"deep\""` | — |
| [SRC-1AE03B9EC3-L004135](../../agents/web_agent.py#L4135) | 4135 | `"                candidates = ["` | — |
| [SRC-1AE03B9EC3-L004136](../../agents/web_agent.py#L4136) | 4136 | `"                    f\"{base_query} official sources data reports\","` | — |
| [SRC-1AE03B9EC3-L004137](../../agents/web_agent.py#L4137) | 4137 | `"                    f\"{base_query} risks limitations alternatives\","` | — |
| [SRC-1AE03B9EC3-L004138](../../agents/web_agent.py#L4138) | 4138 | `"                    f\"{base_query} case studies recent analysis\","` | — |
| [SRC-1AE03B9EC3-L004139](../../agents/web_agent.py#L4139) | 4139 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004140](../../agents/web_agent.py#L4140) | 4140 | `"                normalized_question = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L004141](../../agents/web_agent.py#L4141) | 4141 | `"                property_terms = ("` | — |
| [SRC-1AE03B9EC3-L004142](../../agents/web_agent.py#L4142) | 4142 | `"                    \"شقه\", \"شقق\", \"عقار\", \"عقارات\", \"فيلا\", \"فلل\","` | — |
| [SRC-1AE03B9EC3-L004143](../../agents/web_agent.py#L4143) | 4143 | `"                    \"apartment\", \"apartments\", \"flat\", \"real estate\", \"property\", \"house\", \"villa\","` | — |
| [SRC-1AE03B9EC3-L004144](../../agents/web_agent.py#L4144) | 4144 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004145](../../agents/web_agent.py#L4145) | 4145 | `"                if self._is_listing_discovery(question) and any("` | — |
| [SRC-1AE03B9EC3-L004146](../../agents/web_agent.py#L4146) | 4146 | `"                    term in normalized_question for term in property_terms"` | — |
| [SRC-1AE03B9EC3-L004147](../../agents/web_agent.py#L4147) | 4147 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L004148](../../agents/web_agent.py#L4148) | 4148 | `"                    candidates.extend(["` | — |
| [SRC-1AE03B9EC3-L004149](../../agents/web_agent.py#L4149) | 4149 | `"                        f\"{base_query} إعلانات عقارية ومواقع العقارات\","` | — |
| [SRC-1AE03B9EC3-L004150](../../agents/web_agent.py#L4150) | 4150 | `"                        f\"{base_query} متوسط أسعار السوق للمتر\","` | — |
| [SRC-1AE03B9EC3-L004151](../../agents/web_agent.py#L4151) | 4151 | `"                        f\"{base_query} مواصفات الوحدات والمساحات وطرق السداد\","` | — |
| [SRC-1AE03B9EC3-L004152](../../agents/web_agent.py#L4152) | 4152 | `"                    ])"` | — |
| [SRC-1AE03B9EC3-L004153](../../agents/web_agent.py#L4153) | 4153 | `"                # Keep query budget for evidence-gap searches if first-round coverage is weak."` | — |
| [SRC-1AE03B9EC3-L004154](../../agents/web_agent.py#L4154) | 4154 | `"                plan[\"queries\"] = list(dict.fromkeys((plan.get(\"queries\") or [])[:3] + candidates))["` | — |
| [SRC-1AE03B9EC3-L004155](../../agents/web_agent.py#L4155) | 4155 | `"                    :MAX_PLAN_QUERIES"` | — |
| [SRC-1AE03B9EC3-L004156](../../agents/web_agent.py#L4156) | 4156 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004157](../../agents/web_agent.py#L4157) | 4157 | `"            elif clean_mode == \"latest\":"` | — |
| [SRC-1AE03B9EC3-L004158](../../agents/web_agent.py#L4158) | 4158 | `"                plan[\"freshness\"] = \"current\""` | — |
| [SRC-1AE03B9EC3-L004159](../../agents/web_agent.py#L4159) | 4159 | `"                if self._is_navigation_request(question):"` | — |
| [SRC-1AE03B9EC3-L004160](../../agents/web_agent.py#L4160) | 4160 | `"                    # Preserve link-finding intent in the latest mode. Appending broad"` | — |
| [SRC-1AE03B9EC3-L004161](../../agents/web_agent.py#L4161) | 4161 | `"                    # news modifiers here can turn \"find the official website\" into"` | — |
| [SRC-1AE03B9EC3-L004162](../../agents/web_agent.py#L4162) | 4162 | `"                    # a news-search task and hide the destination the user requested."` | — |
| [SRC-1AE03B9EC3-L004163](../../agents/web_agent.py#L4163) | 4163 | `"                    candidates = ["` | — |
| [SRC-1AE03B9EC3-L004164](../../agents/web_agent.py#L4164) | 4164 | `"                        base_query,"` | — |
| [SRC-1AE03B9EC3-L004165](../../agents/web_agent.py#L4165) | 4165 | `"                        f\"{base_query} الموقع الرسمي\","` | — |
| [SRC-1AE03B9EC3-L004166](../../agents/web_agent.py#L4166) | 4166 | `"                        f\"{base_query} official website\","` | — |
| [SRC-1AE03B9EC3-L004167](../../agents/web_agent.py#L4167) | 4167 | `"                    ]"` | — |
| [SRC-1AE03B9EC3-L004168](../../agents/web_agent.py#L4168) | 4168 | `"                    plan[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L004169](../../agents/web_agent.py#L4169) | 4169 | `"                        candidates + (plan.get(\"queries\") or [])[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004170](../../agents/web_agent.py#L4170) | 4170 | `"                    ))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004171](../../agents/web_agent.py#L4171) | 4171 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L004172](../../agents/web_agent.py#L4172) | 4172 | `"                    candidates = ["` | — |
| [SRC-1AE03B9EC3-L004173](../../agents/web_agent.py#L4173) | 4173 | `"                        f\"{base_query} latest news updates {dt.datetime.now().year}\","` | — |
| [SRC-1AE03B9EC3-L004174](../../agents/web_agent.py#L4174) | 4174 | `"                        f\"{base_query} recent official announcement\","` | — |
| [SRC-1AE03B9EC3-L004175](../../agents/web_agent.py#L4175) | 4175 | `"                    ]"` | — |
| [SRC-1AE03B9EC3-L004176](../../agents/web_agent.py#L4176) | 4176 | `"                    plan[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L004177](../../agents/web_agent.py#L4177) | 4177 | `"                        (plan.get(\"queries\") or [])[:6] + candidates"` | — |
| [SRC-1AE03B9EC3-L004178](../../agents/web_agent.py#L4178) | 4178 | `"                    ))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004179](../../agents/web_agent.py#L4179) | 4179 | `"            elif clean_mode == \"social\":"` | — |
| [SRC-1AE03B9EC3-L004180](../../agents/web_agent.py#L4180) | 4180 | `"                plan[\"social_focus\"] = True"` | — |
| [SRC-1AE03B9EC3-L004181](../../agents/web_agent.py#L4181) | 4181 | `"                if not plan.get(\"platforms\"):"` | — |
| [SRC-1AE03B9EC3-L004182](../../agents/web_agent.py#L4182) | 4182 | `"                    plan[\"platforms\"] = [\"reddit\", \"bluesky\", \"youtube\"]"` | — |
| [SRC-1AE03B9EC3-L004183](../../agents/web_agent.py#L4183) | 4183 | `"                from agents.research import SOCIAL_DOMAINS"` | — |
| [SRC-1AE03B9EC3-L004184](../../agents/web_agent.py#L4184) | 4184 | `"                candidates = ["` | — |
| [SRC-1AE03B9EC3-L004185](../../agents/web_agent.py#L4185) | 4185 | `"                    f\"site:{SOCIAL_DOMAINS[name]} {base_query}\""` | — |
| [SRC-1AE03B9EC3-L004186](../../agents/web_agent.py#L4186) | 4186 | `"                    for name in plan[\"platforms\"][:3]"` | — |
| [SRC-1AE03B9EC3-L004187](../../agents/web_agent.py#L4187) | 4187 | `"                    if name in SOCIAL_DOMAINS"` | — |
| [SRC-1AE03B9EC3-L004188](../../agents/web_agent.py#L4188) | 4188 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004189](../../agents/web_agent.py#L4189) | 4189 | `"                plan[\"queries\"] = list(dict.fromkeys((plan.get(\"queries\") or [])[:5] + candidates))["` | — |
| [SRC-1AE03B9EC3-L004190](../../agents/web_agent.py#L4190) | 4190 | `"                    :MAX_PLAN_QUERIES"` | — |
| [SRC-1AE03B9EC3-L004191](../../agents/web_agent.py#L4191) | 4191 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004192](../../agents/web_agent.py#L4192) | 4192 | `"            if intent_route == \"LEAD_GENERATION\" and clean_mode == \"auto\":"` | — |
| [SRC-1AE03B9EC3-L004193](../../agents/web_agent.py#L4193) | 4193 | `"                # Prospect discovery needs buyer-intent queries and public social signals,"` | — |
| [SRC-1AE03B9EC3-L004194](../../agents/web_agent.py#L4194) | 4194 | `"                # not just broad pages advertising the requested product."` | — |
| [SRC-1AE03B9EC3-L004195](../../agents/web_agent.py#L4195) | 4195 | `"                plan[\"queries\"] = self._lead_generation_queries(question, plan.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L004196](../../agents/web_agent.py#L4196) | 4196 | `"                plan[\"depth\"] = \"standard\""` | — |
| [SRC-1AE03B9EC3-L004197](../../agents/web_agent.py#L4197) | 4197 | `"                plan[\"freshness\"] = \"current\""` | — |
| [SRC-1AE03B9EC3-L004198](../../agents/web_agent.py#L4198) | 4198 | `"                plan[\"social_focus\"] = True"` | — |
| [SRC-1AE03B9EC3-L004199](../../agents/web_agent.py#L4199) | 4199 | `"                allowed_public_platforms = [\"reddit\", \"bluesky\"]"` | — |
| [SRC-1AE03B9EC3-L004200](../../agents/web_agent.py#L4200) | 4200 | `"                if ("` | — |
| [SRC-1AE03B9EC3-L004201](../../agents/web_agent.py#L4201) | 4201 | `"                    os.getenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L004202](../../agents/web_agent.py#L4202) | 4202 | `"                    and os.getenv(\"FACEBOOK_PAGE_IDS\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L004203](../../agents/web_agent.py#L4203) | 4203 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L004204](../../agents/web_agent.py#L4204) | 4204 | `"                    allowed_public_platforms.append(\"facebook\")"` | — |
| [SRC-1AE03B9EC3-L004205](../../agents/web_agent.py#L4205) | 4205 | `"                if os.getenv(\"X_BEARER_TOKEN\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L004206](../../agents/web_agent.py#L4206) | 4206 | `"                    allowed_public_platforms.append(\"x\")"` | — |
| [SRC-1AE03B9EC3-L004207](../../agents/web_agent.py#L4207) | 4207 | `"                if os.getenv(\"YOUTUBE_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L004208](../../agents/web_agent.py#L4208) | 4208 | `"                    allowed_public_platforms.append(\"youtube\")"` | — |
| [SRC-1AE03B9EC3-L004209](../../agents/web_agent.py#L4209) | 4209 | `"                if ("` | — |
| [SRC-1AE03B9EC3-L004210](../../agents/web_agent.py#L4210) | 4210 | `"                    os.getenv(\"INSTAGRAM_USER_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L004211](../../agents/web_agent.py#L4211) | 4211 | `"                    and os.getenv(\"INSTAGRAM_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L004212](../../agents/web_agent.py#L4212) | 4212 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L004213](../../agents/web_agent.py#L4213) | 4213 | `"                    allowed_public_platforms.append(\"instagram\")"` | — |
| [SRC-1AE03B9EC3-L004214](../../agents/web_agent.py#L4214) | 4214 | `"                plan[\"platforms\"] = list(dict.fromkeys(allowed_public_platforms))"` | — |
| [SRC-1AE03B9EC3-L004215](../../agents/web_agent.py#L4215) | 4215 | `""` | — |
| [SRC-1AE03B9EC3-L004216](../../agents/web_agent.py#L4216) | 4216 | `"        final_topic_queries = []"` | — |
| [SRC-1AE03B9EC3-L004217](../../agents/web_agent.py#L4217) | 4217 | `"        for raw_query in plan.get(\"queries\", []):"` | — |
| [SRC-1AE03B9EC3-L004218](../../agents/web_agent.py#L4218) | 4218 | `"            if not isinstance(raw_query, str) or not raw_query.strip():"` | — |
| [SRC-1AE03B9EC3-L004219](../../agents/web_agent.py#L4219) | 4219 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L004220](../../agents/web_agent.py#L4220) | 4220 | `"            compacted_query = compact_search_query(raw_query)"` | — |
| [SRC-1AE03B9EC3-L004221](../../agents/web_agent.py#L4221) | 4221 | `"            if compacted_query and _relevance_query_tokens(compacted_query):"` | — |
| [SRC-1AE03B9EC3-L004222](../../agents/web_agent.py#L4222) | 4222 | `"                final_topic_queries.append(compacted_query)"` | — |
| [SRC-1AE03B9EC3-L004223](../../agents/web_agent.py#L4223) | 4223 | `"        plan[\"queries\"] = list(dict.fromkeys(final_topic_queries))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004224](../../agents/web_agent.py#L4224) | 4224 | `""` | — |
| [SRC-1AE03B9EC3-L004225](../../agents/web_agent.py#L4225) | 4225 | `"        sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L004226](../../agents/web_agent.py#L4226) | 4226 | `"        search_warnings: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L004227](../../agents/web_agent.py#L4227) | 4227 | `"        report: dict[str, Any] = {}"` | — |
| [SRC-1AE03B9EC3-L004228](../../agents/web_agent.py#L4228) | 4228 | `"        # Scope diagnostic evidence to this research attempt; a reused WebAgent must not"` | — |
| [SRC-1AE03B9EC3-L004229](../../agents/web_agent.py#L4229) | 4229 | `"        # accidentally inherit provider attempts from an earlier question."` | — |
| [SRC-1AE03B9EC3-L004230](../../agents/web_agent.py#L4230) | 4230 | `"        with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L004231](../../agents/web_agent.py#L4231) | 4231 | `"            research_diagnostic_baseline = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L004232](../../agents/web_agent.py#L4232) | 4232 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L004233](../../agents/web_agent.py#L4233) | 4233 | `"            sources, search_warnings, report = self._collect_research(plan)"` | — |
| [SRC-1AE03B9EC3-L004234](../../agents/web_agent.py#L4234) | 4234 | `"        except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L004235](../../agents/web_agent.py#L4235) | 4235 | `"            search_warnings.append(str(exc))"` | — |
| [SRC-1AE03B9EC3-L004236](../../agents/web_agent.py#L4236) | 4236 | `"            baseline_diagnostic_ids = {id(item) for item in research_diagnostic_baseline}"` | — |
| [SRC-1AE03B9EC3-L004237](../../agents/web_agent.py#L4237) | 4237 | `"            with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L004238](../../agents/web_agent.py#L4238) | 4238 | `"                failure_diagnostics = ["` | — |
| [SRC-1AE03B9EC3-L004239](../../agents/web_agent.py#L4239) | 4239 | `"                    item for item in self._provider_diagnostics"` | — |
| [SRC-1AE03B9EC3-L004240](../../agents/web_agent.py#L4240) | 4240 | `"                    if id(item) not in baseline_diagnostic_ids"` | — |
| [SRC-1AE03B9EC3-L004241](../../agents/web_agent.py#L4241) | 4241 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004242](../../agents/web_agent.py#L4242) | 4242 | `"            provider_attempt_observed = any("` | — |
| [SRC-1AE03B9EC3-L004243](../../agents/web_agent.py#L4243) | 4243 | `"                item.get(\"status\") in _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES"` | — |
| [SRC-1AE03B9EC3-L004244](../../agents/web_agent.py#L4244) | 4244 | `"                for item in failure_diagnostics"` | — |
| [SRC-1AE03B9EC3-L004245](../../agents/web_agent.py#L4245) | 4245 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004246](../../agents/web_agent.py#L4246) | 4246 | `"            report = {"` | — |
| [SRC-1AE03B9EC3-L004247](../../agents/web_agent.py#L4247) | 4247 | `"                \"queries_planned\": len(plan.get(\"queries\", [])),"` | — |
| [SRC-1AE03B9EC3-L004248](../../agents/web_agent.py#L4248) | 4248 | `"                # The exact query count is unknowable when the pipeline fails before it"` | — |
| [SRC-1AE03B9EC3-L004249](../../agents/web_agent.py#L4249) | 4249 | `"                # returns its report. A provider diagnostic may still prove an attempt."` | — |
| [SRC-1AE03B9EC3-L004250](../../agents/web_agent.py#L4250) | 4250 | `"                \"queries_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L004251](../../agents/web_agent.py#L4251) | 4251 | `"                \"queries_attempted_known\": False,"` | — |
| [SRC-1AE03B9EC3-L004252](../../agents/web_agent.py#L4252) | 4252 | `"                \"search_attempted\": True if provider_attempt_observed else None,"` | — |
| [SRC-1AE03B9EC3-L004253](../../agents/web_agent.py#L4253) | 4253 | `"                \"search_outcome\": ("` | — |
| [SRC-1AE03B9EC3-L004254](../../agents/web_agent.py#L4254) | 4254 | `"                    \"attempted_research_error\""` | — |
| [SRC-1AE03B9EC3-L004255](../../agents/web_agent.py#L4255) | 4255 | `"                    if provider_attempt_observed"` | — |
| [SRC-1AE03B9EC3-L004256](../../agents/web_agent.py#L4256) | 4256 | `"                    else \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L004257](../../agents/web_agent.py#L4257) | 4257 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L004258](../../agents/web_agent.py#L4258) | 4258 | `"                \"usable_sources_after_filtering\": None,"` | — |
| [SRC-1AE03B9EC3-L004259](../../agents/web_agent.py#L4259) | 4259 | `"                \"unique_sources\": None,"` | — |
| [SRC-1AE03B9EC3-L004260](../../agents/web_agent.py#L4260) | 4260 | `"                \"pages_fetched\": None,"` | — |
| [SRC-1AE03B9EC3-L004261](../../agents/web_agent.py#L4261) | 4261 | `"                \"providers_used\": [],"` | — |
| [SRC-1AE03B9EC3-L004262](../../agents/web_agent.py#L4262) | 4262 | `"                \"provider_counts\": None,"` | — |
| [SRC-1AE03B9EC3-L004263](../../agents/web_agent.py#L4263) | 4263 | `"                \"platform_counts\": {},"` | — |
| [SRC-1AE03B9EC3-L004264](../../agents/web_agent.py#L4264) | 4264 | `"                \"social_direct_results\": None,"` | — |
| [SRC-1AE03B9EC3-L004265](../../agents/web_agent.py#L4265) | 4265 | `"                \"provider_diagnostics\": failure_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L004266](../../agents/web_agent.py#L4266) | 4266 | `"                \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L004267](../../agents/web_agent.py#L4267) | 4267 | `"                \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L004268](../../agents/web_agent.py#L4268) | 4268 | `"                \"evidence_signals\": evidence_signal_report([], plan.get(\"freshness\", \"any\")),"` | — |
| [SRC-1AE03B9EC3-L004269](../../agents/web_agent.py#L4269) | 4269 | `"            }"` | — |
| [SRC-1AE03B9EC3-L004270](../../agents/web_agent.py#L4270) | 4270 | `"        # Final relevance check is intentionally repeated after fusion, before any answer LLM call."` | — |
| [SRC-1AE03B9EC3-L004271](../../agents/web_agent.py#L4271) | 4271 | `"        filtered_sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L004272](../../agents/web_agent.py#L4272) | 4272 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L004273](../../agents/web_agent.py#L4273) | 4273 | `"            if \"user_supplied_url\" in source.get(\"providers\", []):"` | — |
| [SRC-1AE03B9EC3-L004274](../../agents/web_agent.py#L4274) | 4274 | `"                filtered_sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L004275](../../agents/web_agent.py#L4275) | 4275 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L004276](../../agents/web_agent.py#L4276) | 4276 | `"            candidate_queries = ("` | — |
| [SRC-1AE03B9EC3-L004277](../../agents/web_agent.py#L4277) | 4277 | `"                source.get(\"queries\")"` | — |
| [SRC-1AE03B9EC3-L004278](../../agents/web_agent.py#L4278) | 4278 | `"                or plan.get(\"queries\")"` | — |
| [SRC-1AE03B9EC3-L004279](../../agents/web_agent.py#L4279) | 4279 | `"                or [compact_search_query(question)]"` | — |
| [SRC-1AE03B9EC3-L004280](../../agents/web_agent.py#L4280) | 4280 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004281](../../agents/web_agent.py#L4281) | 4281 | `"            if any(self._source_matches_query(str(q), source) for q in candidate_queries):"` | — |
| [SRC-1AE03B9EC3-L004282](../../agents/web_agent.py#L4282) | 4282 | `"                filtered_sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L004283](../../agents/web_agent.py#L4283) | 4283 | `"        sources = filtered_sources"` | — |
| [SRC-1AE03B9EC3-L004284](../../agents/web_agent.py#L4284) | 4284 | `"        search_warning = \"؛ \".join(search_warnings) if search_warnings else None"` | — |
| [SRC-1AE03B9EC3-L004285](../../agents/web_agent.py#L4285) | 4285 | `"        independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L004286](../../agents/web_agent.py#L4286) | 4286 | `"            registrable_domain("` | — |
| [SRC-1AE03B9EC3-L004287](../../agents/web_agent.py#L4287) | 4287 | `"                source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L004288](../../agents/web_agent.py#L4288) | 4288 | `"                or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L004289](../../agents/web_agent.py#L4289) | 4289 | `"                or \"\""` | — |
| [SRC-1AE03B9EC3-L004290](../../agents/web_agent.py#L4290) | 4290 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004291](../../agents/web_agent.py#L4291) | 4291 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L004292](../../agents/web_agent.py#L4292) | 4292 | `"        }"` | — |
| [SRC-1AE03B9EC3-L004293](../../agents/web_agent.py#L4293) | 4293 | `"        independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L004294](../../agents/web_agent.py#L4294) | 4294 | `"        # A user-requested page summary is a different task from open-ended research:"` | — |
| [SRC-1AE03B9EC3-L004295](../../agents/web_agent.py#L4295) | 4295 | `"        # one successfully extracted, explicitly supplied page can support a summary,"` | — |
| [SRC-1AE03B9EC3-L004296](../../agents/web_agent.py#L4296) | 4296 | `"        # but must never be presented as independently corroborated research."` | — |
| [SRC-1AE03B9EC3-L004297](../../agents/web_agent.py#L4297) | 4297 | `"        has_read_user_supplied_page = any("` | — |
| [SRC-1AE03B9EC3-L004298](../../agents/web_agent.py#L4298) | 4298 | `"            \"user_supplied_url\" in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L004299](../../agents/web_agent.py#L4299) | 4299 | `"            and bool(source.get(\"page_fetched\"))"` | — |
| [SRC-1AE03B9EC3-L004300](../../agents/web_agent.py#L4300) | 4300 | `"            and bool(str(source.get(\"page_text\") or \"\").strip())"` | — |
| [SRC-1AE03B9EC3-L004301](../../agents/web_agent.py#L4301) | 4301 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L004302](../../agents/web_agent.py#L4302) | 4302 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004303](../../agents/web_agent.py#L4303) | 4303 | `"        single_source_page_summary = ("` | — |
| [SRC-1AE03B9EC3-L004304](../../agents/web_agent.py#L4304) | 4304 | `"            has_read_user_supplied_page"` | — |
| [SRC-1AE03B9EC3-L004305](../../agents/web_agent.py#L4305) | 4305 | `"            and len(sources) == 1"` | — |
| [SRC-1AE03B9EC3-L004306](../../agents/web_agent.py#L4306) | 4306 | `"            and len(independent_domains) == 1"` | — |
| [SRC-1AE03B9EC3-L004307](../../agents/web_agent.py#L4307) | 4307 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004308](../../agents/web_agent.py#L4308) | 4308 | `"        if single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L004309](../../agents/web_agent.py#L4309) | 4309 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L004310](../../agents/web_agent.py#L4310) | 4310 | `"                \"هذا ملخص للرابط الذي قدمته فقط؛ لم يتم تأكيد محتواه من مصدر مستقل آخر.\""` | — |
| [SRC-1AE03B9EC3-L004311](../../agents/web_agent.py#L4311) | 4311 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004312](../../agents/web_agent.py#L4312) | 4312 | `"            search_warning = \"؛ \".join(search_warnings)"` | — |
| [SRC-1AE03B9EC3-L004313](../../agents/web_agent.py#L4313) | 4313 | `"        # Link-finding and lead-discovery are actionable discovery tasks, not broad"` | — |
| [SRC-1AE03B9EC3-L004314](../../agents/web_agent.py#L4314) | 4314 | `"        # fact-checking. Keep useful candidates visible while explicitly labelling them"` | — |
| [SRC-1AE03B9EC3-L004315](../../agents/web_agent.py#L4315) | 4315 | `"        # as uncorroborated instead of refusing a lone result as if it were no result."` | — |
| [SRC-1AE03B9EC3-L004316](../../agents/web_agent.py#L4316) | 4316 | `"        navigation_request = self._is_navigation_request(question)"` | — |
| [SRC-1AE03B9EC3-L004317](../../agents/web_agent.py#L4317) | 4317 | `"        lead_request = intent_route == \"LEAD_GENERATION\" or self._is_lead_search(question)"` | — |
| [SRC-1AE03B9EC3-L004318](../../agents/web_agent.py#L4318) | 4318 | `"        listing_request = self._is_listing_discovery(question)"` | — |
| [SRC-1AE03B9EC3-L004319](../../agents/web_agent.py#L4319) | 4319 | `"        lead_evidence_sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L004320](../../agents/web_agent.py#L4320) | 4320 | `"        related_lead_results_count = 0"` | — |
| [SRC-1AE03B9EC3-L004321](../../agents/web_agent.py#L4321) | 4321 | `"        if lead_request:"` | — |
| [SRC-1AE03B9EC3-L004322](../../agents/web_agent.py#L4322) | 4322 | `"            related_lead_results_count = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004323](../../agents/web_agent.py#L4323) | 4323 | `"            for source in sources:"` | — |
| [SRC-1AE03B9EC3-L004324](../../agents/web_agent.py#L4324) | 4324 | `"                signal = self._lead_intent_evidence(source)"` | — |
| [SRC-1AE03B9EC3-L004325](../../agents/web_agent.py#L4325) | 4325 | `"                if signal:"` | — |
| [SRC-1AE03B9EC3-L004326](../../agents/web_agent.py#L4326) | 4326 | `"                    source[\"lead_qualification\"] = \"public_buyer_intent_signal\""` | — |
| [SRC-1AE03B9EC3-L004327](../../agents/web_agent.py#L4327) | 4327 | `"                    source[\"lead_intent_evidence\"] = signal"` | — |
| [SRC-1AE03B9EC3-L004328](../../agents/web_agent.py#L4328) | 4328 | `"                    lead_evidence_sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L004329](../../agents/web_agent.py#L4329) | 4329 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L004330](../../agents/web_agent.py#L4330) | 4330 | `"                    source[\"lead_qualification\"] = \"related_result_not_lead\""` | — |
| [SRC-1AE03B9EC3-L004331](../../agents/web_agent.py#L4331) | 4331 | `"            lead_research_incomplete = ("` | — |
| [SRC-1AE03B9EC3-L004332](../../agents/web_agent.py#L4332) | 4332 | `"                not sources"` | — |
| [SRC-1AE03B9EC3-L004333](../../agents/web_agent.py#L4333) | 4333 | `"                and report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES"` | — |
| [SRC-1AE03B9EC3-L004334](../../agents/web_agent.py#L4334) | 4334 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004335](../../agents/web_agent.py#L4335) | 4335 | `"            report[\"lead_generation\"] = {"` | — |
| [SRC-1AE03B9EC3-L004336](../../agents/web_agent.py#L4336) | 4336 | `"                \"status\": ("` | — |
| [SRC-1AE03B9EC3-L004337](../../agents/web_agent.py#L4337) | 4337 | `"                    \"research_incomplete\" if lead_research_incomplete"` | — |
| [SRC-1AE03B9EC3-L004338](../../agents/web_agent.py#L4338) | 4338 | `"                    else \"candidate_signals_found\" if lead_evidence_sources"` | — |
| [SRC-1AE03B9EC3-L004339](../../agents/web_agent.py#L4339) | 4339 | `"                    else \"no_qualified_candidates_found\""` | — |
| [SRC-1AE03B9EC3-L004340](../../agents/web_agent.py#L4340) | 4340 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L004341](../../agents/web_agent.py#L4341) | 4341 | `"                \"candidate_signal_count\": ("` | — |
| [SRC-1AE03B9EC3-L004342](../../agents/web_agent.py#L4342) | 4342 | `"                    None if lead_research_incomplete else len(lead_evidence_sources)"` | — |
| [SRC-1AE03B9EC3-L004343](../../agents/web_agent.py#L4343) | 4343 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L004344](../../agents/web_agent.py#L4344) | 4344 | `"                \"related_results_reviewed\": ("` | — |
| [SRC-1AE03B9EC3-L004345](../../agents/web_agent.py#L4345) | 4345 | `"                    None if lead_research_incomplete else related_lead_results_count"` | — |
| [SRC-1AE03B9EC3-L004346](../../agents/web_agent.py#L4346) | 4346 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L004347](../../agents/web_agent.py#L4347) | 4347 | `"                \"qualification_rule\": \"explicit_public_buyer_intent_phrase\","` | — |
| [SRC-1AE03B9EC3-L004348](../../agents/web_agent.py#L4348) | 4348 | `"                \"identity_verified\": False,"` | — |
| [SRC-1AE03B9EC3-L004349](../../agents/web_agent.py#L4349) | 4349 | `"            }"` | — |
| [SRC-1AE03B9EC3-L004350](../../agents/web_agent.py#L4350) | 4350 | `"            if not lead_evidence_sources:"` | — |
| [SRC-1AE03B9EC3-L004351](../../agents/web_agent.py#L4351) | 4351 | `"                if sources:"` | — |
| [SRC-1AE03B9EC3-L004352](../../agents/web_agent.py#L4352) | 4352 | `"                    lead_answer = ("` | — |
| [SRC-1AE03B9EC3-L004353](../../agents/web_agent.py#L4353) | 4353 | `"                        \"لم أعثر على إشارة نصية واضحة تثبت أن أي نتيجة في هذه الجولة تتعلق بشخص \""` | — |
| [SRC-1AE03B9EC3-L004354](../../agents/web_agent.py#L4354) | 4354 | `"                        \"يريد الشراء. راجعت \""` | — |
| [SRC-1AE03B9EC3-L004355](../../agents/web_agent.py#L4355) | 4355 | `"                        + str(len(sources))"` | — |
| [SRC-1AE03B9EC3-L004356](../../agents/web_agent.py#L4356) | 4356 | `"                        + \" نتيجة مرتبطة بالموضوع، لكنني لم أعتبر إعلانات البيع أو صفحات السوق \""` | — |
| [SRC-1AE03B9EC3-L004357](../../agents/web_agent.py#L4357) | 4357 | `"                        \"عملاء محتملين. الروابط أدناه نتائج مرتبطة بالموضوع فقط وليست عملاء.\""` | — |
| [SRC-1AE03B9EC3-L004358](../../agents/web_agent.py#L4358) | 4358 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004359](../../agents/web_agent.py#L4359) | 4359 | `"                elif report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES:"` | — |
| [SRC-1AE03B9EC3-L004360](../../agents/web_agent.py#L4360) | 4360 | `"                    lead_answer = ("` | — |
| [SRC-1AE03B9EC3-L004361](../../agents/web_agent.py#L4361) | 4361 | `"                        \"تعطل مسار البحث أو لم يمكن تأكيد اكتماله؛ لذلك لا أستطيع تحديد ما إذا \""` | — |
| [SRC-1AE03B9EC3-L004362](../../agents/web_agent.py#L4362) | 4362 | `"                        \"كانت هناك نتائج تصلح كعملاء محتملين في هذه الجولة.\""` | — |
| [SRC-1AE03B9EC3-L004363](../../agents/web_agent.py#L4363) | 4363 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004364](../../agents/web_agent.py#L4364) | 4364 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L004365](../../agents/web_agent.py#L4365) | 4365 | `"                    lead_answer = ("` | — |
| [SRC-1AE03B9EC3-L004366](../../agents/web_agent.py#L4366) | 4366 | `"                        \"لم تظهر نتائج قابلة للاستخدام تثبت نية شراء في هذه الجولة. هذا لا يثبت \""` | — |
| [SRC-1AE03B9EC3-L004367](../../agents/web_agent.py#L4367) | 4367 | `"                        \"عدم وجود عملاء؛ بل يعني أن البحث الحالي لم يعثر على دليل كافٍ.\""` | — |
| [SRC-1AE03B9EC3-L004368](../../agents/web_agent.py#L4368) | 4368 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004369](../../agents/web_agent.py#L4369) | 4369 | `"                report[\"research_quality\"] = \"failed\""` | — |
| [SRC-1AE03B9EC3-L004370](../../agents/web_agent.py#L4370) | 4370 | `"                # Distinguish zero qualified signals from unknown counts after an exception."` | — |
| [SRC-1AE03B9EC3-L004371](../../agents/web_agent.py#L4371) | 4371 | `"                report[\"usable_sources_after_filtering\"] = ("` | — |
| [SRC-1AE03B9EC3-L004372](../../agents/web_agent.py#L4372) | 4372 | `"                    None if lead_research_incomplete else len(sources)"` | — |
| [SRC-1AE03B9EC3-L004373](../../agents/web_agent.py#L4373) | 4373 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004374](../../agents/web_agent.py#L4374) | 4374 | `"                report[\"evidence_signals\"] = ("` | — |
| [SRC-1AE03B9EC3-L004375](../../agents/web_agent.py#L4375) | 4375 | `"                    None if lead_research_incomplete"` | — |
| [SRC-1AE03B9EC3-L004376](../../agents/web_agent.py#L4376) | 4376 | `"                    else evidence_signal_report(sources, plan.get(\"freshness\", \"any\"))"` | — |
| [SRC-1AE03B9EC3-L004377](../../agents/web_agent.py#L4377) | 4377 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004378](../../agents/web_agent.py#L4378) | 4378 | `"                public_related_sources = [{"` | — |
| [SRC-1AE03B9EC3-L004379](../../agents/web_agent.py#L4379) | 4379 | `"                    \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L004380](../../agents/web_agent.py#L4380) | 4380 | `"                    \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L004381](../../agents/web_agent.py#L4381) | 4381 | `"                    \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004382](../../agents/web_agent.py#L4382) | 4382 | `"                    \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L004383](../../agents/web_agent.py#L4383) | 4383 | `"                    \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L004384](../../agents/web_agent.py#L4384) | 4384 | `"                    \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L004385](../../agents/web_agent.py#L4385) | 4385 | `"                    \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L004386](../../agents/web_agent.py#L4386) | 4386 | `"                    \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004387](../../agents/web_agent.py#L4387) | 4387 | `"                    \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L004388](../../agents/web_agent.py#L4388) | 4388 | `"                    \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004389](../../agents/web_agent.py#L4389) | 4389 | `"                    \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004390](../../agents/web_agent.py#L4390) | 4390 | `"                    \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004391](../../agents/web_agent.py#L4391) | 4391 | `"                    \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L004392](../../agents/web_agent.py#L4392) | 4392 | `"                    \"lead_qualification\": \"related_result_not_lead\","` | — |
| [SRC-1AE03B9EC3-L004393](../../agents/web_agent.py#L4393) | 4393 | `"                } for source in sources]"` | — |
| [SRC-1AE03B9EC3-L004394](../../agents/web_agent.py#L4394) | 4394 | `"                return {"` | — |
| [SRC-1AE03B9EC3-L004395](../../agents/web_agent.py#L4395) | 4395 | `"                    \"answer\": lead_answer,"` | — |
| [SRC-1AE03B9EC3-L004396](../../agents/web_agent.py#L4396) | 4396 | `"                    \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L004397](../../agents/web_agent.py#L4397) | 4397 | `"                    \"search_query\": (plan.get(\"queries\") or [\"\"])[0],"` | — |
| [SRC-1AE03B9EC3-L004398](../../agents/web_agent.py#L4398) | 4398 | `"                    \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L004399](../../agents/web_agent.py#L4399) | 4399 | `"                    \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L004400](../../agents/web_agent.py#L4400) | 4400 | `"                        \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L004401](../../agents/web_agent.py#L4401) | 4401 | `"                        \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L004402](../../agents/web_agent.py#L4402) | 4402 | `"                        \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L004403](../../agents/web_agent.py#L4403) | 4403 | `"                        \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L004404](../../agents/web_agent.py#L4404) | 4404 | `"                        \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L004405](../../agents/web_agent.py#L4405) | 4405 | `"                        \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L004406](../../agents/web_agent.py#L4406) | 4406 | `"                        \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L004407](../../agents/web_agent.py#L4407) | 4407 | `"                        \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L004408](../../agents/web_agent.py#L4408) | 4408 | `"                        \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L004409](../../agents/web_agent.py#L4409) | 4409 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L004410](../../agents/web_agent.py#L4410) | 4410 | `"                    \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L004411](../../agents/web_agent.py#L4411) | 4411 | `"                    \"sources\": public_related_sources,"` | — |
| [SRC-1AE03B9EC3-L004412](../../agents/web_agent.py#L4412) | 4412 | `"                    \"used_language_model\": False,"` | — |
| [SRC-1AE03B9EC3-L004413](../../agents/web_agent.py#L4413) | 4413 | `"                    \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L004414](../../agents/web_agent.py#L4414) | 4414 | `"                    \"search_attempted\": report.get("` | — |
| [SRC-1AE03B9EC3-L004415](../../agents/web_agent.py#L4415) | 4415 | `"                        \"search_attempted\","` | — |
| [SRC-1AE03B9EC3-L004416](../../agents/web_agent.py#L4416) | 4416 | `"                        bool(report.get(\"queries_attempted\", 0)),"` | — |
| [SRC-1AE03B9EC3-L004417](../../agents/web_agent.py#L4417) | 4417 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L004418](../../agents/web_agent.py#L4418) | 4418 | `"                    \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L004419](../../agents/web_agent.py#L4419) | 4419 | `"                    \"warnings\": [lead_answer],"` | — |
| [SRC-1AE03B9EC3-L004420](../../agents/web_agent.py#L4420) | 4420 | `"                    \"kind\": \"lead_discovery_no_qualified_candidates\","` | — |
| [SRC-1AE03B9EC3-L004421](../../agents/web_agent.py#L4421) | 4421 | `"                    \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L004422](../../agents/web_agent.py#L4422) | 4422 | `"                    \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L004423](../../agents/web_agent.py#L4423) | 4423 | `"                    \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L004424](../../agents/web_agent.py#L4424) | 4424 | `"                }"` | — |
| [SRC-1AE03B9EC3-L004425](../../agents/web_agent.py#L4425) | 4425 | `"            # Only explicit public buyer-intent signals may be synthesized as lead candidates."` | — |
| [SRC-1AE03B9EC3-L004426](../../agents/web_agent.py#L4426) | 4426 | `"            sources = lead_evidence_sources"` | — |
| [SRC-1AE03B9EC3-L004427](../../agents/web_agent.py#L4427) | 4427 | `"            report[\"evidence_signals\"] = evidence_signal_report(sources, plan.get(\"freshness\", \"any\"))"` | — |
| [SRC-1AE03B9EC3-L004428](../../agents/web_agent.py#L4428) | 4428 | `"            report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004429](../../agents/web_agent.py#L4429) | 4429 | `"            report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004430](../../agents/web_agent.py#L4430) | 4430 | `"            report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L004431](../../agents/web_agent.py#L4431) | 4431 | `"            independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L004432](../../agents/web_agent.py#L4432) | 4432 | `"                registrable_domain("` | — |
| [SRC-1AE03B9EC3-L004433](../../agents/web_agent.py#L4433) | 4433 | `"                    source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L004434](../../agents/web_agent.py#L4434) | 4434 | `"                    or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L004435](../../agents/web_agent.py#L4435) | 4435 | `"                    or \"\""` | — |
| [SRC-1AE03B9EC3-L004436](../../agents/web_agent.py#L4436) | 4436 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004437](../../agents/web_agent.py#L4437) | 4437 | `"                for source in sources"` | — |
| [SRC-1AE03B9EC3-L004438](../../agents/web_agent.py#L4438) | 4438 | `"            }"` | — |
| [SRC-1AE03B9EC3-L004439](../../agents/web_agent.py#L4439) | 4439 | `"            independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L004440](../../agents/web_agent.py#L4440) | 4440 | `"        single_source_navigation = navigation_request and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L004441](../../agents/web_agent.py#L4441) | 4441 | `"        single_source_social = bool(plan.get(\"social_focus\")) and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L004442](../../agents/web_agent.py#L4442) | 4442 | `"        single_source_lead = lead_request and bool(lead_evidence_sources)"` | — |
| [SRC-1AE03B9EC3-L004443](../../agents/web_agent.py#L4443) | 4443 | `"        single_source_listing = listing_request and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L004444](../../agents/web_agent.py#L4444) | 4444 | `"        task_specific_partial_evidence = ("` | — |
| [SRC-1AE03B9EC3-L004445](../../agents/web_agent.py#L4445) | 4445 | `"            single_source_page_summary"` | — |
| [SRC-1AE03B9EC3-L004446](../../agents/web_agent.py#L4446) | 4446 | `"            or single_source_navigation"` | — |
| [SRC-1AE03B9EC3-L004447](../../agents/web_agent.py#L4447) | 4447 | `"            or single_source_social"` | — |
| [SRC-1AE03B9EC3-L004448](../../agents/web_agent.py#L4448) | 4448 | `"            or single_source_lead"` | — |
| [SRC-1AE03B9EC3-L004449](../../agents/web_agent.py#L4449) | 4449 | `"            or single_source_listing"` | — |
| [SRC-1AE03B9EC3-L004450](../../agents/web_agent.py#L4450) | 4450 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004451](../../agents/web_agent.py#L4451) | 4451 | `"        needs_corroboration = len(sources) < 2 or len(independent_domains) < 2"` | — |
| [SRC-1AE03B9EC3-L004452](../../agents/web_agent.py#L4452) | 4452 | `"        evidence_repair: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L004453](../../agents/web_agent.py#L4453) | 4453 | `"            \"attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L004454](../../agents/web_agent.py#L4454) | 4454 | `"            \"max_extra_queries\": 1,"` | — |
| [SRC-1AE03B9EC3-L004455](../../agents/web_agent.py#L4455) | 4455 | `"            \"reason\": \"initial_evidence_gate_satisfied\" if not needs_corroboration else \"not_attempted\","` | — |
| [SRC-1AE03B9EC3-L004456](../../agents/web_agent.py#L4456) | 4456 | `"        }"` | — |
| [SRC-1AE03B9EC3-L004457](../../agents/web_agent.py#L4457) | 4457 | `"        if needs_corroboration and not plan.get(\"queries\"):"` | — |
| [SRC-1AE03B9EC3-L004458](../../agents/web_agent.py#L4458) | 4458 | `"            evidence_repair[\"reason\"] = \"no_topic_query_available\""` | — |
| [SRC-1AE03B9EC3-L004459](../../agents/web_agent.py#L4459) | 4459 | `"        elif needs_corroboration:"` | — |
| [SRC-1AE03B9EC3-L004460](../../agents/web_agent.py#L4460) | 4460 | `"            if task_specific_partial_evidence:"` | — |
| [SRC-1AE03B9EC3-L004461](../../agents/web_agent.py#L4461) | 4461 | `"                evidence_repair[\"reason\"] = \"task_specific_partial_evidence\""` | — |
| [SRC-1AE03B9EC3-L004462](../../agents/web_agent.py#L4462) | 4462 | `"            elif plan.get(\"social_focus\"):"` | — |
| [SRC-1AE03B9EC3-L004463](../../agents/web_agent.py#L4463) | 4463 | `"                evidence_repair[\"reason\"] = \"social_search_not_retried\""` | — |
| [SRC-1AE03B9EC3-L004464](../../agents/web_agent.py#L4464) | 4464 | `"            elif plan.get(\"depth\") == \"deep\" or report.get(\"expansion_queries\"):"` | — |
| [SRC-1AE03B9EC3-L004465](../../agents/web_agent.py#L4465) | 4465 | `"                evidence_repair[\"reason\"] = \"deep_research_already_expanded\""` | — |
| [SRC-1AE03B9EC3-L004466](../../agents/web_agent.py#L4466) | 4466 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L004467](../../agents/web_agent.py#L4467) | 4467 | `"                original_queries = ["` | — |
| [SRC-1AE03B9EC3-L004468](../../agents/web_agent.py#L4468) | 4468 | `"                    str(item).strip()"` | — |
| [SRC-1AE03B9EC3-L004469](../../agents/web_agent.py#L4469) | 4469 | `"                    for item in plan.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L004470](../../agents/web_agent.py#L4470) | 4470 | `"                    if isinstance(item, str) and item.strip()"` | — |
| [SRC-1AE03B9EC3-L004471](../../agents/web_agent.py#L4471) | 4471 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004472](../../agents/web_agent.py#L4472) | 4472 | `"                base_query = ("` | — |
| [SRC-1AE03B9EC3-L004473](../../agents/web_agent.py#L4473) | 4473 | `"                    original_queries[0]"` | — |
| [SRC-1AE03B9EC3-L004474](../../agents/web_agent.py#L4474) | 4474 | `"                    if original_queries"` | — |
| [SRC-1AE03B9EC3-L004475](../../agents/web_agent.py#L4475) | 4475 | `"                    else compact_search_query(question)"` | — |
| [SRC-1AE03B9EC3-L004476](../../agents/web_agent.py#L4476) | 4476 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004477](../../agents/web_agent.py#L4477) | 4477 | `"                suffix = ("` | — |
| [SRC-1AE03B9EC3-L004478](../../agents/web_agent.py#L4478) | 4478 | `"                    \"latest official primary source\""` | — |
| [SRC-1AE03B9EC3-L004479](../../agents/web_agent.py#L4479) | 4479 | `"                    if plan.get(\"freshness\") == \"current\""` | — |
| [SRC-1AE03B9EC3-L004480](../../agents/web_agent.py#L4480) | 4480 | `"                    else \"official primary source data\""` | — |
| [SRC-1AE03B9EC3-L004481](../../agents/web_agent.py#L4481) | 4481 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004482](../../agents/web_agent.py#L4482) | 4482 | `"                repair_query = compact_search_query(f\"{base_query} {suffix}\")"` | — |
| [SRC-1AE03B9EC3-L004483](../../agents/web_agent.py#L4483) | 4483 | `"                if not repair_query or not _relevance_query_tokens(repair_query):"` | — |
| [SRC-1AE03B9EC3-L004484](../../agents/web_agent.py#L4484) | 4484 | `"                    evidence_repair[\"reason\"] = \"no_topic_query_available\""` | — |
| [SRC-1AE03B9EC3-L004485](../../agents/web_agent.py#L4485) | 4485 | `"                    repair_query = \"\""` | — |
| [SRC-1AE03B9EC3-L004486](../../agents/web_agent.py#L4486) | 4486 | `"                known_queries = {"` | — |
| [SRC-1AE03B9EC3-L004487](../../agents/web_agent.py#L4487) | 4487 | `"                    _normalize_search_query(item).casefold()"` | — |
| [SRC-1AE03B9EC3-L004488](../../agents/web_agent.py#L4488) | 4488 | `"                    for item in original_queries"` | — |
| [SRC-1AE03B9EC3-L004489](../../agents/web_agent.py#L4489) | 4489 | `"                }"` | — |
| [SRC-1AE03B9EC3-L004490](../../agents/web_agent.py#L4490) | 4490 | `"                if repair_query and _normalize_search_query(repair_query).casefold() in known_queries:"` | — |
| [SRC-1AE03B9EC3-L004491](../../agents/web_agent.py#L4491) | 4491 | `"                    repair_query = compact_search_query("` | — |
| [SRC-1AE03B9EC3-L004492](../../agents/web_agent.py#L4492) | 4492 | `"                        f\"{base_query} independent corroborating evidence\""` | — |
| [SRC-1AE03B9EC3-L004493](../../agents/web_agent.py#L4493) | 4493 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004494](../../agents/web_agent.py#L4494) | 4494 | `"                if repair_query and _relevance_query_tokens(repair_query) and ("` | — |
| [SRC-1AE03B9EC3-L004495](../../agents/web_agent.py#L4495) | 4495 | `"                    _normalize_search_query(repair_query).casefold() not in known_queries"` | — |
| [SRC-1AE03B9EC3-L004496](../../agents/web_agent.py#L4496) | 4496 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L004497](../../agents/web_agent.py#L4497) | 4497 | `"                    initial_source_count = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004498](../../agents/web_agent.py#L4498) | 4498 | `"                    initial_domain_count = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L004499](../../agents/web_agent.py#L4499) | 4499 | `"                    evidence_repair[\"attempted\"] = True"` | — |
| [SRC-1AE03B9EC3-L004500](../../agents/web_agent.py#L4500) | 4500 | `"                    evidence_repair[\"reason\"] = \"thin_or_unrelated_initial_evidence\""` | — |
| [SRC-1AE03B9EC3-L004501](../../agents/web_agent.py#L4501) | 4501 | `"                    evidence_repair[\"query\"] = repair_query"` | — |
| [SRC-1AE03B9EC3-L004502](../../agents/web_agent.py#L4502) | 4502 | `"                    repair_plan = dict(plan)"` | — |
| [SRC-1AE03B9EC3-L004503](../../agents/web_agent.py#L4503) | 4503 | `"                    repair_plan.update({"` | — |
| [SRC-1AE03B9EC3-L004504](../../agents/web_agent.py#L4504) | 4504 | `"                        \"queries\": [repair_query],"` | — |
| [SRC-1AE03B9EC3-L004505](../../agents/web_agent.py#L4505) | 4505 | `"                        \"depth\": \"standard\","` | — |
| [SRC-1AE03B9EC3-L004506](../../agents/web_agent.py#L4506) | 4506 | `"                        \"social_focus\": False,"` | — |
| [SRC-1AE03B9EC3-L004507](../../agents/web_agent.py#L4507) | 4507 | `"                        \"platforms\": [],"` | — |
| [SRC-1AE03B9EC3-L004508](../../agents/web_agent.py#L4508) | 4508 | `"                        \"direct_urls\": [],"` | — |
| [SRC-1AE03B9EC3-L004509](../../agents/web_agent.py#L4509) | 4509 | `"                    })"` | — |
| [SRC-1AE03B9EC3-L004510](../../agents/web_agent.py#L4510) | 4510 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L004511](../../agents/web_agent.py#L4511) | 4511 | `"                        repair_sources, repair_warnings, repair_report = self._collect_research("` | — |
| [SRC-1AE03B9EC3-L004512](../../agents/web_agent.py#L4512) | 4512 | `"                            repair_plan"` | — |
| [SRC-1AE03B9EC3-L004513](../../agents/web_agent.py#L4513) | 4513 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004514](../../agents/web_agent.py#L4514) | 4514 | `"                    except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L004515](../../agents/web_agent.py#L4515) | 4515 | `"                        repair_sources = []"` | — |
| [SRC-1AE03B9EC3-L004516](../../agents/web_agent.py#L4516) | 4516 | `"                        repair_warnings = []"` | — |
| [SRC-1AE03B9EC3-L004517](../../agents/web_agent.py#L4517) | 4517 | `"                        repair_report = {"` | — |
| [SRC-1AE03B9EC3-L004518](../../agents/web_agent.py#L4518) | 4518 | `"                            \"queries_planned\": 1,"` | — |
| [SRC-1AE03B9EC3-L004519](../../agents/web_agent.py#L4519) | 4519 | `"                            \"queries_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L004520](../../agents/web_agent.py#L4520) | 4520 | `"                            \"queries_attempted_known\": False,"` | — |
| [SRC-1AE03B9EC3-L004521](../../agents/web_agent.py#L4521) | 4521 | `"                            \"search_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L004522](../../agents/web_agent.py#L4522) | 4522 | `"                            \"search_outcome\": \"unknown_after_research_error\","` | — |
| [SRC-1AE03B9EC3-L004523](../../agents/web_agent.py#L4523) | 4523 | `"                            \"usable_sources_after_filtering\": None,"` | — |
| [SRC-1AE03B9EC3-L004524](../../agents/web_agent.py#L4524) | 4524 | `"                        }"` | — |
| [SRC-1AE03B9EC3-L004525](../../agents/web_agent.py#L4525) | 4525 | `"                        search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L004526](../../agents/web_agent.py#L4526) | 4526 | `"                            \"تعذر تنفيذ محاولة البحث الإضافية المحدودة (\""` | — |
| [SRC-1AE03B9EC3-L004527](../../agents/web_agent.py#L4527) | 4527 | `"                            + type(exc).__name__ + \").\""` | — |
| [SRC-1AE03B9EC3-L004528](../../agents/web_agent.py#L4528) | 4528 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004529](../../agents/web_agent.py#L4529) | 4529 | `"                    search_warnings.extend(repair_warnings)"` | — |
| [SRC-1AE03B9EC3-L004530](../../agents/web_agent.py#L4530) | 4530 | `"                    evidence_repair[\"attempted_query_count\"] = 1"` | — |
| [SRC-1AE03B9EC3-L004531](../../agents/web_agent.py#L4531) | 4531 | `"                    evidence_repair[\"initial_source_count\"] = initial_source_count"` | — |
| [SRC-1AE03B9EC3-L004532](../../agents/web_agent.py#L4532) | 4532 | `"                    evidence_repair[\"initial_independent_domain_count\"] = initial_domain_count"` | — |
| [SRC-1AE03B9EC3-L004533](../../agents/web_agent.py#L4533) | 4533 | `"                    evidence_repair[\"new_sources_added\"] = 0"` | — |
| [SRC-1AE03B9EC3-L004534](../../agents/web_agent.py#L4534) | 4534 | `"                    source_indexes: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L004535](../../agents/web_agent.py#L4535) | 4535 | `"                    for source_index, source in enumerate(sources):"` | — |
| [SRC-1AE03B9EC3-L004536](../../agents/web_agent.py#L4536) | 4536 | `"                        source_key = self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L004537](../../agents/web_agent.py#L4537) | 4537 | `"                        if source_key:"` | — |
| [SRC-1AE03B9EC3-L004538](../../agents/web_agent.py#L4538) | 4538 | `"                            source_indexes.setdefault(source_key, source_index)"` | — |
| [SRC-1AE03B9EC3-L004539](../../agents/web_agent.py#L4539) | 4539 | `"                    relevant_queries = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L004540](../../agents/web_agent.py#L4540) | 4540 | `"                        query"` | — |
| [SRC-1AE03B9EC3-L004541](../../agents/web_agent.py#L4541) | 4541 | `"                        for query in ("` | — |
| [SRC-1AE03B9EC3-L004542](../../agents/web_agent.py#L4542) | 4542 | `"                            compact_search_query(question),"` | — |
| [SRC-1AE03B9EC3-L004543](../../agents/web_agent.py#L4543) | 4543 | `"                            *("` | — |
| [SRC-1AE03B9EC3-L004544](../../agents/web_agent.py#L4544) | 4544 | `"                                compact_search_query(candidate)"` | — |
| [SRC-1AE03B9EC3-L004545](../../agents/web_agent.py#L4545) | 4545 | `"                                for candidate in original_queries"` | — |
| [SRC-1AE03B9EC3-L004546](../../agents/web_agent.py#L4546) | 4546 | `"                                if isinstance(candidate, str)"` | — |
| [SRC-1AE03B9EC3-L004547](../../agents/web_agent.py#L4547) | 4547 | `"                            ),"` | — |
| [SRC-1AE03B9EC3-L004548](../../agents/web_agent.py#L4548) | 4548 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004549](../../agents/web_agent.py#L4549) | 4549 | `"                        if query"` | — |
| [SRC-1AE03B9EC3-L004550](../../agents/web_agent.py#L4550) | 4550 | `"                    ))"` | — |
| [SRC-1AE03B9EC3-L004551](../../agents/web_agent.py#L4551) | 4551 | `"                    for source in repair_sources:"` | — |
| [SRC-1AE03B9EC3-L004552](../../agents/web_agent.py#L4552) | 4552 | `"                        if not isinstance(source, dict):"` | — |
| [SRC-1AE03B9EC3-L004553](../../agents/web_agent.py#L4553) | 4553 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L004554](../../agents/web_agent.py#L4554) | 4554 | `"                        if not any("` | — |
| [SRC-1AE03B9EC3-L004555](../../agents/web_agent.py#L4555) | 4555 | `"                            self._source_matches_query(candidate, source)"` | — |
| [SRC-1AE03B9EC3-L004556](../../agents/web_agent.py#L4556) | 4556 | `"                            for candidate in relevant_queries if candidate"` | — |
| [SRC-1AE03B9EC3-L004557](../../agents/web_agent.py#L4557) | 4557 | `"                        ):"` | — |
| [SRC-1AE03B9EC3-L004558](../../agents/web_agent.py#L4558) | 4558 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L004559](../../agents/web_agent.py#L4559) | 4559 | `"                        source_key = self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L004560](../../agents/web_agent.py#L4560) | 4560 | `"                        if not source_key:"` | — |
| [SRC-1AE03B9EC3-L004561](../../agents/web_agent.py#L4561) | 4561 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L004562](../../agents/web_agent.py#L4562) | 4562 | `"                        existing_index = source_indexes.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L004563](../../agents/web_agent.py#L4563) | 4563 | `"                        if existing_index is None:"` | — |
| [SRC-1AE03B9EC3-L004564](../../agents/web_agent.py#L4564) | 4564 | `"                            source_indexes[source_key] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004565](../../agents/web_agent.py#L4565) | 4565 | `"                            sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L004566](../../agents/web_agent.py#L4566) | 4566 | `"                            evidence_repair[\"new_sources_added\"] += 1"` | — |
| [SRC-1AE03B9EC3-L004567](../../agents/web_agent.py#L4567) | 4567 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L004568](../../agents/web_agent.py#L4568) | 4568 | `"                        existing_source = sources[existing_index]"` | — |
| [SRC-1AE03B9EC3-L004569](../../agents/web_agent.py#L4569) | 4569 | `"                        providers = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L004570](../../agents/web_agent.py#L4570) | 4570 | `"                            list(existing_source.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L004571](../../agents/web_agent.py#L4571) | 4571 | `"                            + list(source.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L004572](../../agents/web_agent.py#L4572) | 4572 | `"                        ))"` | — |
| [SRC-1AE03B9EC3-L004573](../../agents/web_agent.py#L4573) | 4573 | `"                        source_queries = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L004574](../../agents/web_agent.py#L4574) | 4574 | `"                            list(existing_source.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L004575](../../agents/web_agent.py#L4575) | 4575 | `"                            + list(source.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L004576](../../agents/web_agent.py#L4576) | 4576 | `"                        ))"` | — |
| [SRC-1AE03B9EC3-L004577](../../agents/web_agent.py#L4577) | 4577 | `"                        if source.get(\"page_fetched\") and not existing_source.get(\"page_fetched\"):"` | — |
| [SRC-1AE03B9EC3-L004578](../../agents/web_agent.py#L4578) | 4578 | `"                            merged_source = dict(existing_source)"` | — |
| [SRC-1AE03B9EC3-L004579](../../agents/web_agent.py#L4579) | 4579 | `"                            merged_source.update(source)"` | — |
| [SRC-1AE03B9EC3-L004580](../../agents/web_agent.py#L4580) | 4580 | `"                            merged_source[\"providers\"] = providers"` | — |
| [SRC-1AE03B9EC3-L004581](../../agents/web_agent.py#L4581) | 4581 | `"                            merged_source[\"queries\"] = source_queries"` | — |
| [SRC-1AE03B9EC3-L004582](../../agents/web_agent.py#L4582) | 4582 | `"                            sources[existing_index] = merged_source"` | — |
| [SRC-1AE03B9EC3-L004583](../../agents/web_agent.py#L4583) | 4583 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L004584](../../agents/web_agent.py#L4584) | 4584 | `"                            existing_source[\"providers\"] = providers"` | — |
| [SRC-1AE03B9EC3-L004585](../../agents/web_agent.py#L4585) | 4585 | `"                            existing_source[\"queries\"] = source_queries"` | — |
| [SRC-1AE03B9EC3-L004586](../../agents/web_agent.py#L4586) | 4586 | `"                    sources.sort("` | — |
| [SRC-1AE03B9EC3-L004587](../../agents/web_agent.py#L4587) | 4587 | `"                        key=lambda item: float(item.get(\"rank_score\", 0) or 0),"` | — |
| [SRC-1AE03B9EC3-L004588](../../agents/web_agent.py#L4588) | 4588 | `"                        reverse=True,"` | — |
| [SRC-1AE03B9EC3-L004589](../../agents/web_agent.py#L4589) | 4589 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004590](../../agents/web_agent.py#L4590) | 4590 | `"                    plan[\"queries\"] = list(dict.fromkeys(original_queries + [repair_query]))"` | — |
| [SRC-1AE03B9EC3-L004591](../../agents/web_agent.py#L4591) | 4591 | `"                    independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L004592](../../agents/web_agent.py#L4592) | 4592 | `"                        registrable_domain("` | — |
| [SRC-1AE03B9EC3-L004593](../../agents/web_agent.py#L4593) | 4593 | `"                            source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L004594](../../agents/web_agent.py#L4594) | 4594 | `"                            or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L004595](../../agents/web_agent.py#L4595) | 4595 | `"                            or \"\""` | — |
| [SRC-1AE03B9EC3-L004596](../../agents/web_agent.py#L4596) | 4596 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004597](../../agents/web_agent.py#L4597) | 4597 | `"                        for source in sources"` | — |
| [SRC-1AE03B9EC3-L004598](../../agents/web_agent.py#L4598) | 4598 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L004599](../../agents/web_agent.py#L4599) | 4599 | `"                    independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L004600](../../agents/web_agent.py#L4600) | 4600 | `"                    needs_corroboration = ("` | — |
| [SRC-1AE03B9EC3-L004601](../../agents/web_agent.py#L4601) | 4601 | `"                        len(sources) < 2 or len(independent_domains) < 2"` | — |
| [SRC-1AE03B9EC3-L004602](../../agents/web_agent.py#L4602) | 4602 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004603](../../agents/web_agent.py#L4603) | 4603 | `"                    evidence_repair.update({"` | — |
| [SRC-1AE03B9EC3-L004604](../../agents/web_agent.py#L4604) | 4604 | `"                        \"final_source_count\": len(sources),"` | — |
| [SRC-1AE03B9EC3-L004605](../../agents/web_agent.py#L4605) | 4605 | `"                        \"final_independent_domain_count\": len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L004606](../../agents/web_agent.py#L4606) | 4606 | `"                        \"recovered\": not needs_corroboration,"` | — |
| [SRC-1AE03B9EC3-L004607](../../agents/web_agent.py#L4607) | 4607 | `"                    })"` | — |
| [SRC-1AE03B9EC3-L004608](../../agents/web_agent.py#L4608) | 4608 | `"                    evidence_repair[\"reason\"] = ("` | — |
| [SRC-1AE03B9EC3-L004609](../../agents/web_agent.py#L4609) | 4609 | `"                        \"single_bounded_retry_still_insufficient\""` | — |
| [SRC-1AE03B9EC3-L004610](../../agents/web_agent.py#L4610) | 4610 | `"                        if needs_corroboration else \"evidence_gate_recovered\""` | — |
| [SRC-1AE03B9EC3-L004611](../../agents/web_agent.py#L4611) | 4611 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004612](../../agents/web_agent.py#L4612) | 4612 | `"                    report[\"queries_planned\"] = int(report.get(\"queries_planned\", 0) or 0) + int("` | — |
| [SRC-1AE03B9EC3-L004613](../../agents/web_agent.py#L4613) | 4613 | `"                        repair_report.get(\"queries_planned\", 1) or 0"` | — |
| [SRC-1AE03B9EC3-L004614](../../agents/web_agent.py#L4614) | 4614 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004615](../../agents/web_agent.py#L4615) | 4615 | `"                    initial_attempt_count = report.get(\"queries_attempted\", 0)"` | — |
| [SRC-1AE03B9EC3-L004616](../../agents/web_agent.py#L4616) | 4616 | `"                    repair_attempt_count = repair_report.get(\"queries_attempted\", 0)"` | — |
| [SRC-1AE03B9EC3-L004617](../../agents/web_agent.py#L4617) | 4617 | `"                    if initial_attempt_count is None or repair_attempt_count is None:"` | — |
| [SRC-1AE03B9EC3-L004618](../../agents/web_agent.py#L4618) | 4618 | `"                        report[\"queries_attempted\"] = None"` | — |
| [SRC-1AE03B9EC3-L004619](../../agents/web_agent.py#L4619) | 4619 | `"                        report[\"queries_attempted_known\"] = False"` | — |
| [SRC-1AE03B9EC3-L004620](../../agents/web_agent.py#L4620) | 4620 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L004621](../../agents/web_agent.py#L4621) | 4621 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L004622](../../agents/web_agent.py#L4622) | 4622 | `"                            report[\"queries_attempted\"] = max(0, int(initial_attempt_count or 0)) + max("` | — |
| [SRC-1AE03B9EC3-L004623](../../agents/web_agent.py#L4623) | 4623 | `"                                0, int(repair_attempt_count or 0)"` | — |
| [SRC-1AE03B9EC3-L004624](../../agents/web_agent.py#L4624) | 4624 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L004625](../../agents/web_agent.py#L4625) | 4625 | `"                            report[\"queries_attempted_known\"] = True"` | — |
| [SRC-1AE03B9EC3-L004626](../../agents/web_agent.py#L4626) | 4626 | `"                        except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L004627](../../agents/web_agent.py#L4627) | 4627 | `"                            report[\"queries_attempted\"] = None"` | — |
| [SRC-1AE03B9EC3-L004628](../../agents/web_agent.py#L4628) | 4628 | `"                            report[\"queries_attempted_known\"] = False"` | — |
| [SRC-1AE03B9EC3-L004629](../../agents/web_agent.py#L4629) | 4629 | `"                    report[\"query_results\"] = list(report.get(\"query_results\", [])) + list("` | — |
| [SRC-1AE03B9EC3-L004630](../../agents/web_agent.py#L4630) | 4630 | `"                        repair_report.get(\"query_results\", [])"` | — |
| [SRC-1AE03B9EC3-L004631](../../agents/web_agent.py#L4631) | 4631 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004632](../../agents/web_agent.py#L4632) | 4632 | `"                    merged_providers = {"` | — |
| [SRC-1AE03B9EC3-L004633](../../agents/web_agent.py#L4633) | 4633 | `"                        provider"` | — |
| [SRC-1AE03B9EC3-L004634](../../agents/web_agent.py#L4634) | 4634 | `"                        for source in sources"` | — |
| [SRC-1AE03B9EC3-L004635](../../agents/web_agent.py#L4635) | 4635 | `"                        for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L004636](../../agents/web_agent.py#L4636) | 4636 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L004637](../../agents/web_agent.py#L4637) | 4637 | `"                    report[\"providers_used\"] = sorted(merged_providers)"` | — |
| [SRC-1AE03B9EC3-L004638](../../agents/web_agent.py#L4638) | 4638 | `"                    report[\"provider_counts\"] = {"` | — |
| [SRC-1AE03B9EC3-L004639](../../agents/web_agent.py#L4639) | 4639 | `"                        provider: sum("` | — |
| [SRC-1AE03B9EC3-L004640](../../agents/web_agent.py#L4640) | 4640 | `"                            provider in source.get(\"providers\", []) for source in sources"` | — |
| [SRC-1AE03B9EC3-L004641](../../agents/web_agent.py#L4641) | 4641 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004642](../../agents/web_agent.py#L4642) | 4642 | `"                        for provider in merged_providers"` | — |
| [SRC-1AE03B9EC3-L004643](../../agents/web_agent.py#L4643) | 4643 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L004644](../../agents/web_agent.py#L4644) | 4644 | `"                    report[\"platform_counts\"] = {"` | — |
