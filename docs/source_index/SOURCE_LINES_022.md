# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **022**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L007001 إلى SRC-EEF2E6447C-L000226
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L007001](../../agents/web_agent.py#L7001) | 7001 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L007002](../../agents/web_agent.py#L7002) | 7002 | `"                        accepted_source_keys = {"` | — |
| [SRC-1AE03B9EC3-L007003](../../agents/web_agent.py#L7003) | 7003 | `"                            self._normalized_source_url_key(item.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L007004](../../agents/web_agent.py#L7004) | 7004 | `"                            for item in sources"` | — |
| [SRC-1AE03B9EC3-L007005](../../agents/web_agent.py#L7005) | 7005 | `"                            if self._normalized_source_url_key(item.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L007006](../../agents/web_agent.py#L7006) | 7006 | `"                        }"` | — |
| [SRC-1AE03B9EC3-L007007](../../agents/web_agent.py#L7007) | 7007 | `"                        criterion_gap_research[\"new_sources_added\"] = len("` | — |
| [SRC-1AE03B9EC3-L007008](../../agents/web_agent.py#L7008) | 7008 | `"                            accepted_source_keys - pre_gap_source_keys"` | — |
| [SRC-1AE03B9EC3-L007009](../../agents/web_agent.py#L7009) | 7009 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L007010](../../agents/web_agent.py#L7010) | 7010 | `"                        criterion_gap_research[\"source_count_after\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L007011](../../agents/web_agent.py#L7011) | 7011 | `"                        plan[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L007012](../../agents/web_agent.py#L7012) | 7012 | `"                            list(plan.get(\"queries\", [])) + [gap_query]"` | — |
| [SRC-1AE03B9EC3-L007013](../../agents/web_agent.py#L7013) | 7013 | `"                        ))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L007014](../../agents/web_agent.py#L7014) | 7014 | `"                        report[\"criterion_gap_research\"] = dict(criterion_gap_research)"` | — |
| [SRC-1AE03B9EC3-L007015](../../agents/web_agent.py#L7015) | 7015 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L007016](../../agents/web_agent.py#L7016) | 7016 | `"                            report[\"queries_planned\"] = max("` | — |
| [SRC-1AE03B9EC3-L007017](../../agents/web_agent.py#L7017) | 7017 | `"                                0, int(report.get(\"queries_planned\", 0) or 0)"` | — |
| [SRC-1AE03B9EC3-L007018](../../agents/web_agent.py#L7018) | 7018 | `"                            ) + max(0, int(gap_report.get(\"queries_planned\", 1) or 0))"` | — |
| [SRC-1AE03B9EC3-L007019](../../agents/web_agent.py#L7019) | 7019 | `"                        except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-1AE03B9EC3-L007020](../../agents/web_agent.py#L7020) | 7020 | `"                            report[\"queries_planned\"] = None"` | — |
| [SRC-1AE03B9EC3-L007021](../../agents/web_agent.py#L7021) | 7021 | `"                        previous_attempts = report.get(\"queries_attempted\")"` | — |
| [SRC-1AE03B9EC3-L007022](../../agents/web_agent.py#L7022) | 7022 | `"                        extra_attempts = gap_report.get(\"queries_attempted\")"` | — |
| [SRC-1AE03B9EC3-L007023](../../agents/web_agent.py#L7023) | 7023 | `"                        if isinstance(previous_attempts, int) and isinstance(extra_attempts, int):"` | — |
| [SRC-1AE03B9EC3-L007024](../../agents/web_agent.py#L7024) | 7024 | `"                            report[\"queries_attempted\"] = max(0, previous_attempts) + max(0, extra_attempts)"` | — |
| [SRC-1AE03B9EC3-L007025](../../agents/web_agent.py#L7025) | 7025 | `"                            report[\"queries_attempted_known\"] = True"` | — |
| [SRC-1AE03B9EC3-L007026](../../agents/web_agent.py#L7026) | 7026 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L007027](../../agents/web_agent.py#L7027) | 7027 | `"                            report[\"queries_attempted\"] = None"` | — |
| [SRC-1AE03B9EC3-L007028](../../agents/web_agent.py#L7028) | 7028 | `"                            report[\"queries_attempted_known\"] = False"` | — |
| [SRC-1AE03B9EC3-L007029](../../agents/web_agent.py#L7029) | 7029 | `"                        old_query_results = report.get(\"query_results\")"` | — |
| [SRC-1AE03B9EC3-L007030](../../agents/web_agent.py#L7030) | 7030 | `"                        new_query_results = gap_report.get(\"query_results\")"` | — |
| [SRC-1AE03B9EC3-L007031](../../agents/web_agent.py#L7031) | 7031 | `"                        report[\"query_results\"] = ("` | — |
| [SRC-1AE03B9EC3-L007032](../../agents/web_agent.py#L7032) | 7032 | `"                            (old_query_results if isinstance(old_query_results, list) else [])"` | — |
| [SRC-1AE03B9EC3-L007033](../../agents/web_agent.py#L7033) | 7033 | `"                            + (new_query_results if isinstance(new_query_results, list) else [])"` | — |
| [SRC-1AE03B9EC3-L007034](../../agents/web_agent.py#L7034) | 7034 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L007035](../../agents/web_agent.py#L7035) | 7035 | `"                        if evidence_updated:"` | — |
| [SRC-1AE03B9EC3-L007036](../../agents/web_agent.py#L7036) | 7036 | `"                            sources.sort("` | — |
| [SRC-1AE03B9EC3-L007037](../../agents/web_agent.py#L7037) | 7037 | `"                                key=lambda item: float(item.get(\"rank_score\", 0) or 0),"` | — |
| [SRC-1AE03B9EC3-L007038](../../agents/web_agent.py#L7038) | 7038 | `"                                reverse=True,"` | — |
| [SRC-1AE03B9EC3-L007039](../../agents/web_agent.py#L7039) | 7039 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L007040](../../agents/web_agent.py#L7040) | 7040 | `"                            try:"` | — |
| [SRC-1AE03B9EC3-L007041](../../agents/web_agent.py#L7041) | 7041 | `"                                revised_draft = self._generate("` | — |
| [SRC-1AE03B9EC3-L007042](../../agents/web_agent.py#L7042) | 7042 | `"                                    working_question,"` | — |
| [SRC-1AE03B9EC3-L007043](../../agents/web_agent.py#L7043) | 7043 | `"                                    clean_history,"` | — |
| [SRC-1AE03B9EC3-L007044](../../agents/web_agent.py#L7044) | 7044 | `"                                    sources,"` | — |
| [SRC-1AE03B9EC3-L007045](../../agents/web_agent.py#L7045) | 7045 | `"                                    search_warning,"` | — |
| [SRC-1AE03B9EC3-L007046](../../agents/web_agent.py#L7046) | 7046 | `"                                    research_plan=plan,"` | — |
| [SRC-1AE03B9EC3-L007047](../../agents/web_agent.py#L7047) | 7047 | `"                                    search_report=report,"` | — |
| [SRC-1AE03B9EC3-L007048](../../agents/web_agent.py#L7048) | 7048 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L007049](../../agents/web_agent.py#L7049) | 7049 | `"                                revised_answer = self._review_answer("` | — |
| [SRC-1AE03B9EC3-L007050](../../agents/web_agent.py#L7050) | 7050 | `"                                    working_question, revised_draft, sources[:MAX_LLM_CITED_SOURCES]"` | — |
| [SRC-1AE03B9EC3-L007051](../../agents/web_agent.py#L7051) | 7051 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L007052](../../agents/web_agent.py#L7052) | 7052 | `"                                answer = revised_answer"` | — |
| [SRC-1AE03B9EC3-L007053](../../agents/web_agent.py#L7053) | 7053 | `"                                review_status = \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L007054](../../agents/web_agent.py#L7054) | 7054 | `"                                criterion_gap_research[\"status\"] = \"evidence_added_and_answer_regenerated\""` | — |
| [SRC-1AE03B9EC3-L007055](../../agents/web_agent.py#L7055) | 7055 | `"                            except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L007056](../../agents/web_agent.py#L7056) | 7056 | `"                                criterion_gap_research[\"status\"] = \"evidence_added_but_regeneration_unavailable\""` | — |
| [SRC-1AE03B9EC3-L007057](../../agents/web_agent.py#L7057) | 7057 | `"                                criterion_gap_research[\"regeneration_error_class\"] = type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L007058](../../agents/web_agent.py#L7058) | 7058 | `"                                coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L007059](../../agents/web_agent.py#L7059) | 7059 | `"                                    \"وصلت أدلة إضافية لمحور مطلوب، لكن تعذرت إعادة توليد الإجابة \""` | — |
| [SRC-1AE03B9EC3-L007060](../../agents/web_agent.py#L7060) | 7060 | `"                                    \"وتدقيقها ضمن الميزانية؛ راجع هذا المحور قبل اعتماد الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L007061](../../agents/web_agent.py#L7061) | 7061 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L007062](../../agents/web_agent.py#L7062) | 7062 | `"                        elif criterion_gap_research.get(\"status\") != \"search_failed\":"` | — |
| [SRC-1AE03B9EC3-L007063](../../agents/web_agent.py#L7063) | 7063 | `"                            criterion_gap_research[\"status\"] = \"search_completed_no_new_criterion_evidence\""` | — |
| [SRC-1AE03B9EC3-L007064](../../agents/web_agent.py#L7064) | 7064 | `"                            coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L007065](../../agents/web_agent.py#L7065) | 7065 | `"                                \"أُجري بحث إضافي لمحاور ناقصة، لكنه لم يضف نص مصدر يمكن تمييزه \""` | — |
| [SRC-1AE03B9EC3-L007066](../../agents/web_agent.py#L7066) | 7066 | `"                                \"كدليل جديد؛ ستظل هذه المحاور غير محسومة.\""` | — |
| [SRC-1AE03B9EC3-L007067](../../agents/web_agent.py#L7067) | 7067 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L007068](../../agents/web_agent.py#L7068) | 7068 | `"                        criterion_gap_research[\"source_count_after\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L007069](../../agents/web_agent.py#L7069) | 7069 | `"                        report[\"criterion_gap_research\"] = dict(criterion_gap_research)"` | — |
| [SRC-1AE03B9EC3-L007070](../../agents/web_agent.py#L7070) | 7070 | `""` | — |
| [SRC-1AE03B9EC3-L007071](../../agents/web_agent.py#L7071) | 7071 | `"        report[\"criterion_gap_research\"] = dict(criterion_gap_research)"` | — |
| [SRC-1AE03B9EC3-L007072](../../agents/web_agent.py#L7072) | 7072 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L007073](../../agents/web_agent.py#L7073) | 7073 | `"            coverage_targets"` | — |
| [SRC-1AE03B9EC3-L007074](../../agents/web_agent.py#L7074) | 7074 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L007075](../../agents/web_agent.py#L7075) | 7075 | `"            and sources"` | — |
| [SRC-1AE03B9EC3-L007076](../../agents/web_agent.py#L7076) | 7076 | `"            and self.api_key"` | — |
| [SRC-1AE03B9EC3-L007077](../../agents/web_agent.py#L7077) | 7077 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L007078](../../agents/web_agent.py#L7078) | 7078 | `"            initial_integrity = audit_answer_integrity(working_question, answer, sources, coverage_targets, plan.get(\"requirement_queries\"))"` | — |
| [SRC-1AE03B9EC3-L007079](../../agents/web_agent.py#L7079) | 7079 | `"            missing_targets = ["` | — |
| [SRC-1AE03B9EC3-L007080](../../agents/web_agent.py#L7080) | 7080 | `"                item[\"target\"] for item in initial_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L007081](../../agents/web_agent.py#L7081) | 7081 | `"                if item[\"status\"] == \"possibly_missing\""` | — |
| [SRC-1AE03B9EC3-L007082](../../agents/web_agent.py#L7082) | 7082 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L007083](../../agents/web_agent.py#L7083) | 7083 | `"            remaining_source_gap_targets = ["` | — |
| [SRC-1AE03B9EC3-L007084](../../agents/web_agent.py#L7084) | 7084 | `"                item[\"target\"] for item in initial_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L007085](../../agents/web_agent.py#L7085) | 7085 | `"                if item.get(\"source_evidence_status\") == \"no_source_lexical_signal\""` | — |
| [SRC-1AE03B9EC3-L007086](../../agents/web_agent.py#L7086) | 7086 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L007087](../../agents/web_agent.py#L7087) | 7087 | `"            if not missing_targets and remaining_source_gap_targets:"` | — |
| [SRC-1AE03B9EC3-L007088](../../agents/web_agent.py#L7088) | 7088 | `"                coverage_repair_status = \"source_evidence_gap_unresolved\""` | — |
| [SRC-1AE03B9EC3-L007089](../../agents/web_agent.py#L7089) | 7089 | `"                if not coverage_repair_warning:"` | — |
| [SRC-1AE03B9EC3-L007090](../../agents/web_agent.py#L7090) | 7090 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L007091](../../agents/web_agent.py#L7091) | 7091 | `"                        \"ذُكرت المحاور في الإجابة، لكن لم تظهر لها إشارات لفظية في المصادر؛ \""` | — |
| [SRC-1AE03B9EC3-L007092](../../agents/web_agent.py#L7092) | 7092 | `"                        \"ذكر المحور لا يُعد دليلًا، لذلك تظل المهمة غير مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L007093](../../agents/web_agent.py#L7093) | 7093 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L007094](../../agents/web_agent.py#L7094) | 7094 | `"            elif not missing_targets:"` | — |
| [SRC-1AE03B9EC3-L007095](../../agents/web_agent.py#L7095) | 7095 | `"                coverage_repair_status = \"not_needed_lexical_signals_found\""` | — |
| [SRC-1AE03B9EC3-L007096](../../agents/web_agent.py#L7096) | 7096 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L007097](../../agents/web_agent.py#L7097) | 7097 | `"                coverage_repair_status = \"attempted\""` | — |
| [SRC-1AE03B9EC3-L007098](../../agents/web_agent.py#L7098) | 7098 | `"                try:"` | — |
| [SRC-1AE03B9EC3-L007099](../../agents/web_agent.py#L7099) | 7099 | `"                    repaired_answer = self._repair_answer_coverage("` | — |
| [SRC-1AE03B9EC3-L007100](../../agents/web_agent.py#L7100) | 7100 | `"                        working_question, answer, sources, missing_targets"` | — |
| [SRC-1AE03B9EC3-L007101](../../agents/web_agent.py#L7101) | 7101 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L007102](../../agents/web_agent.py#L7102) | 7102 | `"                    if repaired_answer.strip() != answer.strip():"` | — |
| [SRC-1AE03B9EC3-L007103](../../agents/web_agent.py#L7103) | 7103 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L007104](../../agents/web_agent.py#L7104) | 7104 | `"                            reaudit_answer = self._review_answer("` | — |
| [SRC-1AE03B9EC3-L007105](../../agents/web_agent.py#L7105) | 7105 | `"                                working_question,"` | — |
| [SRC-1AE03B9EC3-L007106](../../agents/web_agent.py#L7106) | 7106 | `"                                repaired_answer,"` | — |
| [SRC-1AE03B9EC3-L007107](../../agents/web_agent.py#L7107) | 7107 | `"                                sources[:MAX_LLM_CITED_SOURCES],"` | — |
| [SRC-1AE03B9EC3-L007108](../../agents/web_agent.py#L7108) | 7108 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L007109](../../agents/web_agent.py#L7109) | 7109 | `"                            answer = reaudit_answer"` | — |
| [SRC-1AE03B9EC3-L007110](../../agents/web_agent.py#L7110) | 7110 | `"                            reaudit_integrity = audit_answer_integrity("` | — |
| [SRC-1AE03B9EC3-L007111](../../agents/web_agent.py#L7111) | 7111 | `"                                question, answer, sources, coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L007112](../../agents/web_agent.py#L7112) | 7112 | `"                                plan.get(\"requirement_queries\"),"` | — |
| [SRC-1AE03B9EC3-L007113](../../agents/web_agent.py#L7113) | 7113 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L007114](../../agents/web_agent.py#L7114) | 7114 | `"                            if reaudit_integrity[\"potentially_missing_target_count\"] > 0:"` | — |
| [SRC-1AE03B9EC3-L007115](../../agents/web_agent.py#L7115) | 7115 | `"                                coverage_repair_status = \"revised_and_reaudited_remaining_gaps\""` | — |
| [SRC-1AE03B9EC3-L007116](../../agents/web_agent.py#L7116) | 7116 | `"                                coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L007117](../../agents/web_agent.py#L7117) | 7117 | `"                                    \"خضعت الإجابة المعدلة لمراجعة ثانية، لكن الفحص اللفظي ما زال يرصد محورًا محتمل النقص؛ \""` | — |
| [SRC-1AE03B9EC3-L007118](../../agents/web_agent.py#L7118) | 7118 | `"                                    \"لا تعتبر المهمة مكتملة دون مراجعة هذا المحور والأدلة الأصلية.\""` | — |
| [SRC-1AE03B9EC3-L007119](../../agents/web_agent.py#L7119) | 7119 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L007120](../../agents/web_agent.py#L7120) | 7120 | `"                            else:"` | — |
| [SRC-1AE03B9EC3-L007121](../../agents/web_agent.py#L7121) | 7121 | `"                                coverage_repair_status = \"revised_and_reaudited\""` | — |
| [SRC-1AE03B9EC3-L007122](../../agents/web_agent.py#L7122) | 7122 | `"                            review_status = \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L007123](../../agents/web_agent.py#L7123) | 7123 | `"                        except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L007124](../../agents/web_agent.py#L7124) | 7124 | `"                            review_status = \"model_claim_audit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L007125](../../agents/web_agent.py#L7125) | 7125 | `"                            review_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L007126](../../agents/web_agent.py#L7126) | 7126 | `"                            coverage_repair_status = ("` | — |
| [SRC-1AE03B9EC3-L007127](../../agents/web_agent.py#L7127) | 7127 | `"                                \"reaudit_budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L007128](../../agents/web_agent.py#L7128) | 7128 | `"                                if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L007129](../../agents/web_agent.py#L7129) | 7129 | `"                                else \"reaudit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L007130](../../agents/web_agent.py#L7130) | 7130 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L007131](../../agents/web_agent.py#L7131) | 7131 | `"                            review_warning = ("` | — |
| [SRC-1AE03B9EC3-L007132](../../agents/web_agent.py#L7132) | 7132 | `"                                \"استُنفدت ميزانية النماذج قبل إعادة تدقيق الإجابة المعدلة؛ \""` | — |
| [SRC-1AE03B9EC3-L007133](../../agents/web_agent.py#L7133) | 7133 | `"                                \"لذلك لن أعرض النص المعدل بوصفه إجابة مكتملة، وأعرض مقتطفات المصادر بدلًا منه.\""` | — |
| [SRC-1AE03B9EC3-L007134](../../agents/web_agent.py#L7134) | 7134 | `"                                if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L007135](../../agents/web_agent.py#L7135) | 7135 | `"                                else"` | — |
| [SRC-1AE03B9EC3-L007136](../../agents/web_agent.py#L7136) | 7136 | `"                                \"تعذرت إعادة تدقيق الإجابة المعدلة مقابل الأدلة؛ لذلك لن أعرضها بوصفها إجابة مكتملة، \""` | — |
| [SRC-1AE03B9EC3-L007137](../../agents/web_agent.py#L7137) | 7137 | `"                                \"وأعرض مقتطفات المصادر بدلًا منها.\""` | — |
| [SRC-1AE03B9EC3-L007138](../../agents/web_agent.py#L7138) | 7138 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L007139](../../agents/web_agent.py#L7139) | 7139 | `"                            answer = ("` | — |
| [SRC-1AE03B9EC3-L007140](../../agents/web_agent.py#L7140) | 7140 | `"                                _fallback_lead_answer(lead_evidence_sources)"` | — |
| [SRC-1AE03B9EC3-L007141](../../agents/web_agent.py#L7141) | 7141 | `"                                if lead_request and lead_evidence_sources"` | — |
| [SRC-1AE03B9EC3-L007142](../../agents/web_agent.py#L7142) | 7142 | `"                                else _fallback_answer(sources, review_warning)"` | — |
| [SRC-1AE03B9EC3-L007143](../../agents/web_agent.py#L7143) | 7143 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L007144](../../agents/web_agent.py#L7144) | 7144 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L007145](../../agents/web_agent.py#L7145) | 7145 | `"                        coverage_repair_status = \"no_change_gap_unresolved\""` | — |
| [SRC-1AE03B9EC3-L007146](../../agents/web_agent.py#L7146) | 7146 | `"                        coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L007147](../../agents/web_agent.py#L7147) | 7147 | `"                            \"رصد الفحص اللفظي محورًا قد يكون ناقصًا، لكن محاولة الإصلاح لم تغيّر الإجابة؛ \""` | — |
| [SRC-1AE03B9EC3-L007148](../../agents/web_agent.py#L7148) | 7148 | `"                            \"تحقق من تغطية هذا المحور يدويًا.\""` | — |
| [SRC-1AE03B9EC3-L007149](../../agents/web_agent.py#L7149) | 7149 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L007150](../../agents/web_agent.py#L7150) | 7150 | `"                except RequestBudgetExceeded:"` | — |
| [SRC-1AE03B9EC3-L007151](../../agents/web_agent.py#L7151) | 7151 | `"                    coverage_repair_status = \"budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L007152](../../agents/web_agent.py#L7152) | 7152 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L007153](../../agents/web_agent.py#L7153) | 7153 | `"                        \"استُنفدت ميزانية النماذج قبل محاولة إصلاح محور قد يكون ناقصًا؛ \""` | — |
| [SRC-1AE03B9EC3-L007154](../../agents/web_agent.py#L7154) | 7154 | `"                        \"لا تعتبر التغطية مكتملة دون مراجعة المحور المذكور.\""` | — |
| [SRC-1AE03B9EC3-L007155](../../agents/web_agent.py#L7155) | 7155 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L007156](../../agents/web_agent.py#L7156) | 7156 | `"                except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L007157](../../agents/web_agent.py#L7157) | 7157 | `"                    coverage_repair_status = \"unavailable\""` | — |
| [SRC-1AE03B9EC3-L007158](../../agents/web_agent.py#L7158) | 7158 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L007159](../../agents/web_agent.py#L7159) | 7159 | `"                        \"تعذرت محاولة إصلاح محور قد يكون ناقصًا (\""` | — |
| [SRC-1AE03B9EC3-L007160](../../agents/web_agent.py#L7160) | 7160 | `"                        + type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L007161](../../agents/web_agent.py#L7161) | 7161 | `"                        + \")؛ راجع المحاور المطلوبة قبل اعتماد الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L007162](../../agents/web_agent.py#L7162) | 7162 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L007163](../../agents/web_agent.py#L7163) | 7163 | `"        elif coverage_targets and review_status == \"model_claim_audit_completed\" and not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L007164](../../agents/web_agent.py#L7164) | 7164 | `"            coverage_repair_status = \"skipped_no_model_configuration\""` | — |
| [SRC-1AE03B9EC3-L007165](../../agents/web_agent.py#L7165) | 7165 | `"        elif coverage_targets:"` | — |
| [SRC-1AE03B9EC3-L007166](../../agents/web_agent.py#L7166) | 7166 | `"            coverage_repair_status = \"skipped_review_unavailable\""` | — |
| [SRC-1AE03B9EC3-L007167](../../agents/web_agent.py#L7167) | 7167 | `""` | — |
| [SRC-1AE03B9EC3-L007168](../../agents/web_agent.py#L7168) | 7168 | `"        if self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L007169](../../agents/web_agent.py#L7169) | 7169 | `"            answer += \"\\n\\nروابط إضافية من البحث المباشر عبر الويب:\""` | — |
| [SRC-1AE03B9EC3-L007170](../../agents/web_agent.py#L7170) | 7170 | `"            for source in self.server_search_sources[:8]:"` | — |
| [SRC-1AE03B9EC3-L007171](../../agents/web_agent.py#L7171) | 7171 | `"                answer += \"\\n- \" + source[\"title\"] + \" — \" + source[\"url\"]"` | — |
| [SRC-1AE03B9EC3-L007172](../../agents/web_agent.py#L7172) | 7172 | `"        max_citable_sources = min(MAX_LLM_CITED_SOURCES, len(sources))"` | — |
| [SRC-1AE03B9EC3-L007173](../../agents/web_agent.py#L7173) | 7173 | `"        answer, citation_warnings = self._remove_invalid_citations("` | — |
| [SRC-1AE03B9EC3-L007174](../../agents/web_agent.py#L7174) | 7174 | `"            answer, max_citable_sources"` | — |
| [SRC-1AE03B9EC3-L007175](../../agents/web_agent.py#L7175) | 7175 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007176](../../agents/web_agent.py#L7176) | 7176 | `"        citation_validation = self._citation_validation_metadata("` | — |
| [SRC-1AE03B9EC3-L007177](../../agents/web_agent.py#L7177) | 7177 | `"            answer, max_citable_sources, citation_warnings, review_status"` | — |
| [SRC-1AE03B9EC3-L007178](../../agents/web_agent.py#L7178) | 7178 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007179](../../agents/web_agent.py#L7179) | 7179 | `"        # Run deterministic numeric/provenance checks before asking the semantic reviewer."` | — |
| [SRC-1AE03B9EC3-L007180](../../agents/web_agent.py#L7180) | 7180 | `"        # Recompute below after a source-only fallback so public diagnostics describe the final text."` | — |
| [SRC-1AE03B9EC3-L007181](../../agents/web_agent.py#L7181) | 7181 | `"        answer_integrity = audit_answer_integrity("` | — |
| [SRC-1AE03B9EC3-L007182](../../agents/web_agent.py#L7182) | 7182 | `"            working_question, answer, sources, coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L007183](../../agents/web_agent.py#L7183) | 7183 | `"            plan.get(\"requirement_queries\")"` | — |
| [SRC-1AE03B9EC3-L007184](../../agents/web_agent.py#L7184) | 7184 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007185](../../agents/web_agent.py#L7185) | 7185 | `"        semantic_claim_verification: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L007186](../../agents/web_agent.py#L7186) | 7186 | `"            \"status\": \"not_run_review_unavailable\","` | — |
| [SRC-1AE03B9EC3-L007187](../../agents/web_agent.py#L7187) | 7187 | `"            \"withhold_answer\": False,"` | — |
| [SRC-1AE03B9EC3-L007188](../../agents/web_agent.py#L7188) | 7188 | `"            \"semantic_verification\": \"not_performed\","` | — |
| [SRC-1AE03B9EC3-L007189](../../agents/web_agent.py#L7189) | 7189 | `"            \"fact_correctness\": \"not_verified\","` | — |
| [SRC-1AE03B9EC3-L007190](../../agents/web_agent.py#L7190) | 7190 | `"        }"` | — |
| [SRC-1AE03B9EC3-L007191](../../agents/web_agent.py#L7191) | 7191 | `"        semantic_answer_withheld = False"` | — |
| [SRC-1AE03B9EC3-L007192](../../agents/web_agent.py#L7192) | 7192 | `"        if used_llm and sources and review_status == \"model_claim_audit_completed\":"` | — |
| [SRC-1AE03B9EC3-L007193](../../agents/web_agent.py#L7193) | 7193 | `"            if citation_warnings:"` | — |
| [SRC-1AE03B9EC3-L007194](../../agents/web_agent.py#L7194) | 7194 | `"                semantic_claim_verification = {"` | — |
| [SRC-1AE03B9EC3-L007195](../../agents/web_agent.py#L7195) | 7195 | `"                    \"status\": \"not_verifiable\","` | — |
| [SRC-1AE03B9EC3-L007196](../../agents/web_agent.py#L7196) | 7196 | `"                    \"withhold_answer\": True,"` | — |
| [SRC-1AE03B9EC3-L007197](../../agents/web_agent.py#L7197) | 7197 | `"                    \"reason\": \"invalid_citation_references_were_removed\","` | — |
| [SRC-1AE03B9EC3-L007198](../../agents/web_agent.py#L7198) | 7198 | `"                    \"semantic_verification\": \"not_completed\","` | — |
| [SRC-1AE03B9EC3-L007199](../../agents/web_agent.py#L7199) | 7199 | `"                    \"fact_correctness\": \"not_verified\","` | — |
| [SRC-1AE03B9EC3-L007200](../../agents/web_agent.py#L7200) | 7200 | `"                }"` | — |
| [SRC-1AE03B9EC3-L007201](../../agents/web_agent.py#L7201) | 7201 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L007202](../../agents/web_agent.py#L7202) | 7202 | `"                semantic_claim_verification = self._verify_semantic_claims("` | — |
| [SRC-1AE03B9EC3-L007203](../../agents/web_agent.py#L7203) | 7203 | `"                    working_question, answer, sources, answer_integrity"` | — |
| [SRC-1AE03B9EC3-L007204](../../agents/web_agent.py#L7204) | 7204 | `"                )"` | — |
| [SRC-1AE03B9EC3-L007205](../../agents/web_agent.py#L7205) | 7205 | `"            if semantic_claim_verification.get(\"status\") not in {"` | — |
| [SRC-1AE03B9EC3-L007206](../../agents/web_agent.py#L7206) | 7206 | `"                \"completed_all_claims_supported\","` | — |
| [SRC-1AE03B9EC3-L007207](../../agents/web_agent.py#L7207) | 7207 | `"                \"completed_no_factual_claims\","` | — |
| [SRC-1AE03B9EC3-L007208](../../agents/web_agent.py#L7208) | 7208 | `"            }:"` | — |
| [SRC-1AE03B9EC3-L007209](../../agents/web_agent.py#L7209) | 7209 | `"                semantic_answer_withheld = True"` | — |
| [SRC-1AE03B9EC3-L007210](../../agents/web_agent.py#L7210) | 7210 | `"                semantic_warning = ("` | — |
| [SRC-1AE03B9EC3-L007211](../../agents/web_agent.py#L7211) | 7211 | `"                    \"حُجبت صياغة النموذج لأن مراجع دعم الادعاءات لم يستطع إثبات دعم \""` | — |
| [SRC-1AE03B9EC3-L007212](../../agents/web_agent.py#L7212) | 7212 | `"                    \"كل ادعاء واقعي بمصدره المحدد دون تعارض. المقتطفات أدناه مواد مصدرية \""` | — |
| [SRC-1AE03B9EC3-L007213](../../agents/web_agent.py#L7213) | 7213 | `"                    \"للمراجعة وليست إجابة متحققة.\""` | — |
| [SRC-1AE03B9EC3-L007214](../../agents/web_agent.py#L7214) | 7214 | `"                )"` | — |
| [SRC-1AE03B9EC3-L007215](../../agents/web_agent.py#L7215) | 7215 | `"                answer = ("` | — |
| [SRC-1AE03B9EC3-L007216](../../agents/web_agent.py#L7216) | 7216 | `"                    _fallback_lead_answer(lead_evidence_sources)"` | — |
| [SRC-1AE03B9EC3-L007217](../../agents/web_agent.py#L7217) | 7217 | `"                    if lead_request and lead_evidence_sources"` | — |
| [SRC-1AE03B9EC3-L007218](../../agents/web_agent.py#L7218) | 7218 | `"                    else _fallback_answer(sources, semantic_warning)"` | — |
| [SRC-1AE03B9EC3-L007219](../../agents/web_agent.py#L7219) | 7219 | `"                )"` | — |
| [SRC-1AE03B9EC3-L007220](../../agents/web_agent.py#L7220) | 7220 | `"                answer, fallback_citation_warnings = self._remove_invalid_citations("` | — |
| [SRC-1AE03B9EC3-L007221](../../agents/web_agent.py#L7221) | 7221 | `"                    answer, max_citable_sources"` | — |
| [SRC-1AE03B9EC3-L007222](../../agents/web_agent.py#L7222) | 7222 | `"                )"` | — |
| [SRC-1AE03B9EC3-L007223](../../agents/web_agent.py#L7223) | 7223 | `"                citation_warnings = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L007224](../../agents/web_agent.py#L7224) | 7224 | `"                    citation_warnings + fallback_citation_warnings"` | — |
| [SRC-1AE03B9EC3-L007225](../../agents/web_agent.py#L7225) | 7225 | `"                ))"` | — |
| [SRC-1AE03B9EC3-L007226](../../agents/web_agent.py#L7226) | 7226 | `"                citation_validation = self._citation_validation_metadata("` | — |
| [SRC-1AE03B9EC3-L007227](../../agents/web_agent.py#L7227) | 7227 | `"                    answer, max_citable_sources, citation_warnings, review_status"` | — |
| [SRC-1AE03B9EC3-L007228](../../agents/web_agent.py#L7228) | 7228 | `"                )"` | — |
| [SRC-1AE03B9EC3-L007229](../../agents/web_agent.py#L7229) | 7229 | `"        report[\"semantic_claim_verification\"] = semantic_claim_verification"` | — |
| [SRC-1AE03B9EC3-L007230](../../agents/web_agent.py#L7230) | 7230 | `"        report[\"answer_was_withheld\"] = semantic_answer_withheld"` | — |
| [SRC-1AE03B9EC3-L007231](../../agents/web_agent.py#L7231) | 7231 | `"        report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L007232](../../agents/web_agent.py#L7232) | 7232 | `"        report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L007233](../../agents/web_agent.py#L7233) | 7233 | `"        report[\"second_pass_review\"] = review_status"` | — |
| [SRC-1AE03B9EC3-L007234](../../agents/web_agent.py#L7234) | 7234 | `"        report[\"claim_audit\"] = review_status"` | — |
| [SRC-1AE03B9EC3-L007235](../../agents/web_agent.py#L7235) | 7235 | `"        answer_coverage = {"` | — |
| [SRC-1AE03B9EC3-L007236](../../agents/web_agent.py#L7236) | 7236 | `"            \"method\": \"explicit_criteria_heuristic\","` | — |
| [SRC-1AE03B9EC3-L007237](../../agents/web_agent.py#L7237) | 7237 | `"            \"targets\": coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L007238](../../agents/web_agent.py#L7238) | 7238 | `"            \"review_prompted\": review_status == \"model_claim_audit_completed\","` | — |
| [SRC-1AE03B9EC3-L007239](../../agents/web_agent.py#L7239) | 7239 | `"            \"status\": ("` | — |
| [SRC-1AE03B9EC3-L007240](../../agents/web_agent.py#L7240) | 7240 | `"                \"model_review_requested_not_machine_verified\""` | — |
| [SRC-1AE03B9EC3-L007241](../../agents/web_agent.py#L7241) | 7241 | `"                if coverage_targets and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L007242](../../agents/web_agent.py#L7242) | 7242 | `"                else \"review_unavailable\""` | — |
| [SRC-1AE03B9EC3-L007243](../../agents/web_agent.py#L7243) | 7243 | `"                if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L007244](../../agents/web_agent.py#L7244) | 7244 | `"                else \"no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L007245](../../agents/web_agent.py#L7245) | 7245 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L007246](../../agents/web_agent.py#L7246) | 7246 | `"            \"automatically_graded\": False,"` | — |
| [SRC-1AE03B9EC3-L007247](../../agents/web_agent.py#L7247) | 7247 | `"        }"` | — |
| [SRC-1AE03B9EC3-L007248](../../agents/web_agent.py#L7248) | 7248 | `"        report[\"answer_coverage\"] = answer_coverage"` | — |
| [SRC-1AE03B9EC3-L007249](../../agents/web_agent.py#L7249) | 7249 | `"        report[\"coverage_repair_status\"] = coverage_repair_status"` | — |
| [SRC-1AE03B9EC3-L007250](../../agents/web_agent.py#L7250) | 7250 | `"        report[\"coverage_repair_warning\"] = coverage_repair_warning"` | — |
| [SRC-1AE03B9EC3-L007251](../../agents/web_agent.py#L7251) | 7251 | `"        answer_integrity = audit_answer_integrity(working_question, answer, sources, coverage_targets, plan.get(\"requirement_queries\"))"` | — |
| [SRC-1AE03B9EC3-L007252](../../agents/web_agent.py#L7252) | 7252 | `"        if semantic_answer_withheld:"` | — |
| [SRC-1AE03B9EC3-L007253](../../agents/web_agent.py#L7253) | 7253 | `"            answer_coverage[\"status\"] = \"semantic_support_unverified_answer_withheld\""` | — |
| [SRC-1AE03B9EC3-L007254](../../agents/web_agent.py#L7254) | 7254 | `"            answer_coverage[\"semantic_verification_status\"] = semantic_claim_verification.get(\"status\")"` | — |
| [SRC-1AE03B9EC3-L007255](../../agents/web_agent.py#L7255) | 7255 | `"        answer_coverage[\"target_checks\"] = answer_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L007256](../../agents/web_agent.py#L7256) | 7256 | `"        answer_coverage[\"potentially_missing_target_count\"] = answer_integrity[\"potentially_missing_target_count\"]"` | — |
| [SRC-1AE03B9EC3-L007257](../../agents/web_agent.py#L7257) | 7257 | `"        answer_coverage[\"source_evidence_gap_count\"] = answer_integrity[\"source_evidence_gap_count\"]"` | — |
| [SRC-1AE03B9EC3-L007258](../../agents/web_agent.py#L7258) | 7258 | `"        answer_coverage[\"lexical_screen_method\"] = \"deterministic_lexical_screen_only_not_semantic_grading\""` | — |
| [SRC-1AE03B9EC3-L007259](../../agents/web_agent.py#L7259) | 7259 | `"        requirements_without_candidates = int("` | — |
| [SRC-1AE03B9EC3-L007260](../../agents/web_agent.py#L7260) | 7260 | `"            answer_integrity.get(\"requirements_without_candidate_evidence_count\", 0) or 0"` | — |
| [SRC-1AE03B9EC3-L007261](../../agents/web_agent.py#L7261) | 7261 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007262](../../agents/web_agent.py#L7262) | 7262 | `"        task_fulfillment_status = ("` | — |
| [SRC-1AE03B9EC3-L007263](../../agents/web_agent.py#L7263) | 7263 | `"            \"possible_gap_detected\""` | — |
| [SRC-1AE03B9EC3-L007264](../../agents/web_agent.py#L7264) | 7264 | `"            if ("` | — |
| [SRC-1AE03B9EC3-L007265](../../agents/web_agent.py#L7265) | 7265 | `"                answer_integrity[\"potentially_missing_target_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L007266](../../agents/web_agent.py#L7266) | 7266 | `"                or answer_integrity[\"source_evidence_gap_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L007267](../../agents/web_agent.py#L7267) | 7267 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007268](../../agents/web_agent.py#L7268) | 7268 | `"            else \"candidate_evidence_gaps_or_linkage_unknown\""` | — |
| [SRC-1AE03B9EC3-L007269](../../agents/web_agent.py#L7269) | 7269 | `"            if coverage_targets and requirements_without_candidates > 0"` | — |
| [SRC-1AE03B9EC3-L007270](../../agents/web_agent.py#L7270) | 7270 | `"            else \"lexical_signals_found_not_semantically_verified\" if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L007271](../../agents/web_agent.py#L7271) | 7271 | `"            else \"not_machine_assessed_no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L007272](../../agents/web_agent.py#L7272) | 7272 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007273](../../agents/web_agent.py#L7273) | 7273 | `"        if semantic_answer_withheld:"` | — |
| [SRC-1AE03B9EC3-L007274](../../agents/web_agent.py#L7274) | 7274 | `"            task_fulfillment_status = \"not_assessed_insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L007275](../../agents/web_agent.py#L7275) | 7275 | `"        answer_coverage[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L007276](../../agents/web_agent.py#L7276) | 7276 | `"        answer_coverage[\"semantic_verification_status\"] = semantic_claim_verification.get(\"status\")"` | — |
| [SRC-1AE03B9EC3-L007277](../../agents/web_agent.py#L7277) | 7277 | `"        report[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L007278](../../agents/web_agent.py#L7278) | 7278 | `"        report[\"answer_integrity\"] = answer_integrity"` | — |
| [SRC-1AE03B9EC3-L007279](../../agents/web_agent.py#L7279) | 7279 | `"        report[\"requirement_evidence\"] = answer_integrity.get(\"requirement_evidence\", [])"` | — |
| [SRC-1AE03B9EC3-L007280](../../agents/web_agent.py#L7280) | 7280 | `"        report[\"connector_summary\"] = self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L007281](../../agents/web_agent.py#L7281) | 7281 | `"            list(self._provider_diagnostics), sources"` | — |
| [SRC-1AE03B9EC3-L007282](../../agents/web_agent.py#L7282) | 7282 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007283](../../agents/web_agent.py#L7283) | 7283 | `"        report[\"provider_diagnostics\"] = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L007284](../../agents/web_agent.py#L7284) | 7284 | `"        distinct_providers = {"` | — |
| [SRC-1AE03B9EC3-L007285](../../agents/web_agent.py#L7285) | 7285 | `"            provider for source in sources for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L007286](../../agents/web_agent.py#L7286) | 7286 | `"        }"` | — |
| [SRC-1AE03B9EC3-L007287](../../agents/web_agent.py#L7287) | 7287 | `"        distinct_domains = {"` | — |
| [SRC-1AE03B9EC3-L007288](../../agents/web_agent.py#L7288) | 7288 | `"            registrable_domain("` | — |
| [SRC-1AE03B9EC3-L007289](../../agents/web_agent.py#L7289) | 7289 | `"                source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L007290](../../agents/web_agent.py#L7290) | 7290 | `"                or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L007291](../../agents/web_agent.py#L7291) | 7291 | `"                or \"\""` | — |
| [SRC-1AE03B9EC3-L007292](../../agents/web_agent.py#L7292) | 7292 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007293](../../agents/web_agent.py#L7293) | 7293 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L007294](../../agents/web_agent.py#L7294) | 7294 | `"        }"` | — |
| [SRC-1AE03B9EC3-L007295](../../agents/web_agent.py#L7295) | 7295 | `"        distinct_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L007296](../../agents/web_agent.py#L7296) | 7296 | `"        fetched_pages = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L007297](../../agents/web_agent.py#L7297) | 7297 | `"        if semantic_answer_withheld:"` | — |
| [SRC-1AE03B9EC3-L007298](../../agents/web_agent.py#L7298) | 7298 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L007299](../../agents/web_agent.py#L7299) | 7299 | `"        elif ("` | — |
| [SRC-1AE03B9EC3-L007300](../../agents/web_agent.py#L7300) | 7300 | `"            len(sources) >= 4 and len(distinct_domains) >= 3"` | — |
| [SRC-1AE03B9EC3-L007301](../../agents/web_agent.py#L7301) | 7301 | `"            and len(distinct_providers) >= 2 and fetched_pages >= 1"` | — |
| [SRC-1AE03B9EC3-L007302](../../agents/web_agent.py#L7302) | 7302 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L007303](../../agents/web_agent.py#L7303) | 7303 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L007304](../../agents/web_agent.py#L7304) | 7304 | `"            research_quality = \"excellent\""` | — |
| [SRC-1AE03B9EC3-L007305](../../agents/web_agent.py#L7305) | 7305 | `"        elif ("` | — |
| [SRC-1AE03B9EC3-L007306](../../agents/web_agent.py#L7306) | 7306 | `"            len(sources) >= 2 and len(distinct_domains) >= 2"` | — |
| [SRC-1AE03B9EC3-L007307](../../agents/web_agent.py#L7307) | 7307 | `"            and (len(distinct_providers) >= 2 or fetched_pages >= 1)"` | — |
| [SRC-1AE03B9EC3-L007308](../../agents/web_agent.py#L7308) | 7308 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L007309](../../agents/web_agent.py#L7309) | 7309 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L007310](../../agents/web_agent.py#L7310) | 7310 | `"            research_quality = \"good\""` | — |
| [SRC-1AE03B9EC3-L007311](../../agents/web_agent.py#L7311) | 7311 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L007312](../../agents/web_agent.py#L7312) | 7312 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L007313](../../agents/web_agent.py#L7313) | 7313 | `""` | — |
| [SRC-1AE03B9EC3-L007314](../../agents/web_agent.py#L7314) | 7314 | `"        # Source breadth and a completed model-assisted review do not justify a"` | — |
| [SRC-1AE03B9EC3-L007315](../../agents/web_agent.py#L7315) | 7315 | `"        # positive research-quality label if the final answer has no valid source"` | — |
| [SRC-1AE03B9EC3-L007316](../../agents/web_agent.py#L7316) | 7316 | `"        # citation markers. This is a deterministic presentation guard, not a"` | — |
| [SRC-1AE03B9EC3-L007317](../../agents/web_agent.py#L7317) | 7317 | `"        # semantic entailment check."` | — |
| [SRC-1AE03B9EC3-L007318](../../agents/web_agent.py#L7318) | 7318 | `"        uncited_reviewed_answer = ("` | — |
| [SRC-1AE03B9EC3-L007319](../../agents/web_agent.py#L7319) | 7319 | `"            used_llm"` | — |
| [SRC-1AE03B9EC3-L007320](../../agents/web_agent.py#L7320) | 7320 | `"            and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L007321](../../agents/web_agent.py#L7321) | 7321 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L007322](../../agents/web_agent.py#L7322) | 7322 | `"            and citation_validation[\"valid_citation_count\"] == 0"` | — |
| [SRC-1AE03B9EC3-L007323](../../agents/web_agent.py#L7323) | 7323 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007324](../../agents/web_agent.py#L7324) | 7324 | `"        if uncited_reviewed_answer:"` | — |
| [SRC-1AE03B9EC3-L007325](../../agents/web_agent.py#L7325) | 7325 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L007326](../../agents/web_agent.py#L7326) | 7326 | `"            citation_validation[\"claim_support\"] = \"not_established_no_valid_source_citations\""` | — |
| [SRC-1AE03B9EC3-L007327](../../agents/web_agent.py#L7327) | 7327 | `"            answer_evidence_status = \"reviewed_answer_has_no_valid_citations\""` | — |
| [SRC-1AE03B9EC3-L007328](../../agents/web_agent.py#L7328) | 7328 | `"            uncited_answer_warning = ("` | — |
| [SRC-1AE03B9EC3-L007329](../../agents/web_agent.py#L7329) | 7329 | `"                \"اكتملت مراجعة النموذج، لكن الإجابة النهائية لا تحتوي على إحالات صالحة \""` | — |
| [SRC-1AE03B9EC3-L007330](../../agents/web_agent.py#L7330) | 7330 | `"                \"إلى قائمة المصادر؛ لذلك صُنّفت جودة البحث «جزئية». وجود المصادر أو \""` | — |
| [SRC-1AE03B9EC3-L007331](../../agents/web_agent.py#L7331) | 7331 | `"                \"اكتمال مراجعة النموذج لا يثبت دعم كل ادعاء.\""` | — |
| [SRC-1AE03B9EC3-L007332](../../agents/web_agent.py#L7332) | 7332 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007333](../../agents/web_agent.py#L7333) | 7333 | `"        elif citation_validation[\"valid_citation_count\"] > 0:"` | — |
| [SRC-1AE03B9EC3-L007334](../../agents/web_agent.py#L7334) | 7334 | `"            answer_evidence_status = ("` | — |
| [SRC-1AE03B9EC3-L007335](../../agents/web_agent.py#L7335) | 7335 | `"                \"semantic_support_unverified_answer_withheld\""` | — |
| [SRC-1AE03B9EC3-L007336](../../agents/web_agent.py#L7336) | 7336 | `"                if semantic_answer_withheld else \"citation_indices_validated_only\""` | — |
| [SRC-1AE03B9EC3-L007337](../../agents/web_agent.py#L7337) | 7337 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007338](../../agents/web_agent.py#L7338) | 7338 | `"            uncited_answer_warning = None"` | — |
| [SRC-1AE03B9EC3-L007339](../../agents/web_agent.py#L7339) | 7339 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L007340](../../agents/web_agent.py#L7340) | 7340 | `"            answer_evidence_status = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L007341](../../agents/web_agent.py#L7341) | 7341 | `"            uncited_answer_warning = None"` | — |
| [SRC-1AE03B9EC3-L007342](../../agents/web_agent.py#L7342) | 7342 | `""` | — |
| [SRC-1AE03B9EC3-L007343](../../agents/web_agent.py#L7343) | 7343 | `"        search_attempted = search_attempted or bool(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L007344](../../agents/web_agent.py#L7344) | 7344 | `"        report[\"search_attempted\"] = search_attempted"` | — |
| [SRC-1AE03B9EC3-L007345](../../agents/web_agent.py#L7345) | 7345 | `"        prior_search_outcome = report.get(\"search_outcome\")"` | — |
| [SRC-1AE03B9EC3-L007346](../../agents/web_agent.py#L7346) | 7346 | `"        if prior_search_outcome in _RESEARCH_ERROR_OUTCOMES and not sources:"` | — |
| [SRC-1AE03B9EC3-L007347](../../agents/web_agent.py#L7347) | 7347 | `"            # Preserve a known pipeline failure instead of relabeling it as an ordinary"` | — |
| [SRC-1AE03B9EC3-L007348](../../agents/web_agent.py#L7348) | 7348 | `"            # zero-result search merely because the outer request reached its return path."` | — |
| [SRC-1AE03B9EC3-L007349](../../agents/web_agent.py#L7349) | 7349 | `"            report[\"search_outcome\"] = prior_search_outcome"` | — |
| [SRC-1AE03B9EC3-L007350](../../agents/web_agent.py#L7350) | 7350 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L007351](../../agents/web_agent.py#L7351) | 7351 | `"            report[\"search_outcome\"] = ("` | — |
| [SRC-1AE03B9EC3-L007352](../../agents/web_agent.py#L7352) | 7352 | `"                \"attempted_with_usable_sources\" if search_attempted and sources"` | — |
| [SRC-1AE03B9EC3-L007353](../../agents/web_agent.py#L7353) | 7353 | `"                else \"attempted_no_usable_sources\" if search_attempted"` | — |
| [SRC-1AE03B9EC3-L007354](../../agents/web_agent.py#L7354) | 7354 | `"                else \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L007355](../../agents/web_agent.py#L7355) | 7355 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007356](../../agents/web_agent.py#L7356) | 7356 | `"        report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L007357](../../agents/web_agent.py#L7357) | 7357 | `"        report[\"research_quality\"] = research_quality"` | — |
| [SRC-1AE03B9EC3-L007358](../../agents/web_agent.py#L7358) | 7358 | `"        report[\"research_quality_semantics\"] = \"process_coverage_not_factual_probability\""` | — |
| [SRC-1AE03B9EC3-L007359](../../agents/web_agent.py#L7359) | 7359 | `"        report[\"answer_evidence_status\"] = answer_evidence_status"` | — |
| [SRC-1AE03B9EC3-L007360](../../agents/web_agent.py#L7360) | 7360 | `"        report[\"distinct_registrable_domains\"] = len(distinct_domains)"` | — |
| [SRC-1AE03B9EC3-L007361](../../agents/web_agent.py#L7361) | 7361 | `"        report[\"independent_sources\"] = len(distinct_domains)  # Legacy alias; not editorial independence."` | — |
| [SRC-1AE03B9EC3-L007362](../../agents/web_agent.py#L7362) | 7362 | `"        report[\"independent_sources_field_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L007363](../../agents/web_agent.py#L7363) | 7363 | `"            \"legacy_compatibility_alias_for_distinct_registrable_domain_count\""` | — |
| [SRC-1AE03B9EC3-L007364](../../agents/web_agent.py#L7364) | 7364 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007365](../../agents/web_agent.py#L7365) | 7365 | `"        report[\"source_diversity_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L007366](../../agents/web_agent.py#L7366) | 7366 | `"            \"distinct_registrable_domains_not_editorial_independence\""` | — |
| [SRC-1AE03B9EC3-L007367](../../agents/web_agent.py#L7367) | 7367 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007368](../../agents/web_agent.py#L7368) | 7368 | `"        report[\"editorial_independence_status\"] = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L007369](../../agents/web_agent.py#L7369) | 7369 | `"        report[\"claim_audit_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L007370](../../agents/web_agent.py#L7370) | 7370 | `"            \"distinct_model_assessed_source_support_not_ground_truth\""` | — |
| [SRC-1AE03B9EC3-L007371](../../agents/web_agent.py#L7371) | 7371 | `"            if semantic_claim_verification.get(\"status\") in {"` | — |
| [SRC-1AE03B9EC3-L007372](../../agents/web_agent.py#L7372) | 7372 | `"                \"completed_all_claims_supported\", \"completed_no_factual_claims\""` | — |
| [SRC-1AE03B9EC3-L007373](../../agents/web_agent.py#L7373) | 7373 | `"            }"` | — |
| [SRC-1AE03B9EC3-L007374](../../agents/web_agent.py#L7374) | 7374 | `"            else \"not_verified\""` | — |
| [SRC-1AE03B9EC3-L007375](../../agents/web_agent.py#L7375) | 7375 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007376](../../agents/web_agent.py#L7376) | 7376 | `"        report[\"insufficient_evidence\"] = bool("` | — |
| [SRC-1AE03B9EC3-L007377](../../agents/web_agent.py#L7377) | 7377 | `"            report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES"` | — |
| [SRC-1AE03B9EC3-L007378](../../agents/web_agent.py#L7378) | 7378 | `"            or not sources"` | — |
| [SRC-1AE03B9EC3-L007379](../../agents/web_agent.py#L7379) | 7379 | `"            or semantic_answer_withheld"` | — |
| [SRC-1AE03B9EC3-L007380](../../agents/web_agent.py#L7380) | 7380 | `"            or answer_integrity[\"source_evidence_gap_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L007381](../../agents/web_agent.py#L7381) | 7381 | `"            or ("` | — |
| [SRC-1AE03B9EC3-L007382](../../agents/web_agent.py#L7382) | 7382 | `"                bool(coverage_targets)"` | — |
| [SRC-1AE03B9EC3-L007383](../../agents/web_agent.py#L7383) | 7383 | `"                and answer_integrity[\"potentially_missing_target_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L007384](../../agents/web_agent.py#L7384) | 7384 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007385](../../agents/web_agent.py#L7385) | 7385 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007386](../../agents/web_agent.py#L7386) | 7386 | `"        report[\"valid_citation_range\"] = [1, max_citable_sources] if max_citable_sources else []"` | — |
| [SRC-1AE03B9EC3-L007387](../../agents/web_agent.py#L7387) | 7387 | `"        report[\"citation_count\"] = citation_validation[\"valid_citation_count\"]"` | — |
| [SRC-1AE03B9EC3-L007388](../../agents/web_agent.py#L7388) | 7388 | `"        report[\"citation_check\"] = citation_validation[\"status\"]"` | — |
| [SRC-1AE03B9EC3-L007389](../../agents/web_agent.py#L7389) | 7389 | `"        report[\"citation_validation\"] = citation_validation"` | — |
| [SRC-1AE03B9EC3-L007390](../../agents/web_agent.py#L7390) | 7390 | `"        warnings = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L007391](../../agents/web_agent.py#L7391) | 7391 | `"            search_warnings"` | — |
| [SRC-1AE03B9EC3-L007392](../../agents/web_agent.py#L7392) | 7392 | `"            + ([llm_warning] if llm_warning else [])"` | — |
| [SRC-1AE03B9EC3-L007393](../../agents/web_agent.py#L7393) | 7393 | `"            + ([review_warning] if review_warning else [])"` | — |
| [SRC-1AE03B9EC3-L007394](../../agents/web_agent.py#L7394) | 7394 | `"            + ([coverage_repair_warning] if coverage_repair_warning else [])"` | — |
| [SRC-1AE03B9EC3-L007395](../../agents/web_agent.py#L7395) | 7395 | `"            + citation_warnings"` | — |
| [SRC-1AE03B9EC3-L007396](../../agents/web_agent.py#L7396) | 7396 | `"            + ([uncited_answer_warning] if uncited_answer_warning else [])"` | — |
| [SRC-1AE03B9EC3-L007397](../../agents/web_agent.py#L7397) | 7397 | `"            + (["` | — |
| [SRC-1AE03B9EC3-L007398](../../agents/web_agent.py#L7398) | 7398 | `"                \"حُجبت الإجابة المولدة لعدم اكتمال التحقق الدلالي المستقل عن نموذج الصياغة.\""` | — |
| [SRC-1AE03B9EC3-L007399](../../agents/web_agent.py#L7399) | 7399 | `"            ] if semantic_answer_withheld else [])"` | — |
| [SRC-1AE03B9EC3-L007400](../../agents/web_agent.py#L7400) | 7400 | `"        ))"` | — |
| [SRC-1AE03B9EC3-L007401](../../agents/web_agent.py#L7401) | 7401 | `"        report[\"model_calls\"] = list(self.model_usage)"` | — |
| [SRC-1AE03B9EC3-L007402](../../agents/web_agent.py#L7402) | 7402 | `"        report[\"openrouter_web_search_enabled\"] = self.openrouter_web_search_enabled"` | — |
| [SRC-1AE03B9EC3-L007403](../../agents/web_agent.py#L7403) | 7403 | `"        report[\"openrouter_web_search_results\"] = len(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L007404](../../agents/web_agent.py#L7404) | 7404 | `"        if semantic_answer_withheld:"` | — |
| [SRC-1AE03B9EC3-L007405](../../agents/web_agent.py#L7405) | 7405 | `"            final_answer_status = \"semantic_verification_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L007406](../../agents/web_agent.py#L7406) | 7406 | `"        elif generation_budget_exhausted or review_budget_exhausted:"` | — |
| [SRC-1AE03B9EC3-L007407](../../agents/web_agent.py#L7407) | 7407 | `"            final_answer_status = \"budget_exhausted_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L007408](../../agents/web_agent.py#L7408) | 7408 | `"        elif llm_warning:"` | — |
| [SRC-1AE03B9EC3-L007409](../../agents/web_agent.py#L7409) | 7409 | `"            final_answer_status = ("` | — |
| [SRC-1AE03B9EC3-L007410](../../agents/web_agent.py#L7410) | 7410 | `"                \"model_not_configured_fallback\""` | — |
| [SRC-1AE03B9EC3-L007411](../../agents/web_agent.py#L7411) | 7411 | `"                if not self.api_key"` | — |
| [SRC-1AE03B9EC3-L007412](../../agents/web_agent.py#L7412) | 7412 | `"                else \"generation_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L007413](../../agents/web_agent.py#L7413) | 7413 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007414](../../agents/web_agent.py#L7414) | 7414 | `"        elif review_warning:"` | — |
| [SRC-1AE03B9EC3-L007415](../../agents/web_agent.py#L7415) | 7415 | `"            final_answer_status = \"review_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L007416](../../agents/web_agent.py#L7416) | 7416 | `"        elif coverage_repair_status == \"no_change_gap_unresolved\":"` | — |
| [SRC-1AE03B9EC3-L007417](../../agents/web_agent.py#L7417) | 7417 | `"            final_answer_status = \"coverage_repair_left_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L007418](../../agents/web_agent.py#L7418) | 7418 | `"        elif coverage_repair_status == \"budget_exhausted\":"` | — |
| [SRC-1AE03B9EC3-L007419](../../agents/web_agent.py#L7419) | 7419 | `"            final_answer_status = \"coverage_repair_budget_exhausted_with_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L007420](../../agents/web_agent.py#L7420) | 7420 | `"        elif coverage_repair_status == \"unavailable\":"` | — |
| [SRC-1AE03B9EC3-L007421](../../agents/web_agent.py#L7421) | 7421 | `"            final_answer_status = \"coverage_repair_unavailable_with_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L007422](../../agents/web_agent.py#L7422) | 7422 | `"        elif used_llm:"` | — |
| [SRC-1AE03B9EC3-L007423](../../agents/web_agent.py#L7423) | 7423 | `"            final_answer_status = \"model_answer_generated\""` | — |
| [SRC-1AE03B9EC3-L007424](../../agents/web_agent.py#L7424) | 7424 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L007425](../../agents/web_agent.py#L7425) | 7425 | `"            final_answer_status = \"source_fallback\""` | — |
| [SRC-1AE03B9EC3-L007426](../../agents/web_agent.py#L7426) | 7426 | `""` | — |
| [SRC-1AE03B9EC3-L007427](../../agents/web_agent.py#L7427) | 7427 | `"        # Report pipeline completion separately from factual correctness. A successful"` | — |
| [SRC-1AE03B9EC3-L007428](../../agents/web_agent.py#L7428) | 7428 | `"        # retrieval or model review is not an independent semantic fact check."` | — |
| [SRC-1AE03B9EC3-L007429](../../agents/web_agent.py#L7429) | 7429 | `"        if report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES:"` | — |
| [SRC-1AE03B9EC3-L007430](../../agents/web_agent.py#L7430) | 7430 | `"            pipeline_completion_status = \"execution_failed\""` | — |
| [SRC-1AE03B9EC3-L007431](../../agents/web_agent.py#L7431) | 7431 | `"        elif not search_attempted:"` | — |
| [SRC-1AE03B9EC3-L007432](../../agents/web_agent.py#L7432) | 7432 | `"            pipeline_completion_status = \"not_verified\""` | — |
| [SRC-1AE03B9EC3-L007433](../../agents/web_agent.py#L7433) | 7433 | `"        elif not sources:"` | — |
| [SRC-1AE03B9EC3-L007434](../../agents/web_agent.py#L7434) | 7434 | `"            pipeline_completion_status = \"insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L007435](../../agents/web_agent.py#L7435) | 7435 | `"        elif ("` | — |
| [SRC-1AE03B9EC3-L007436](../../agents/web_agent.py#L7436) | 7436 | `"            llm_warning"` | — |
| [SRC-1AE03B9EC3-L007437](../../agents/web_agent.py#L7437) | 7437 | `"            or review_warning"` | — |
| [SRC-1AE03B9EC3-L007438](../../agents/web_agent.py#L7438) | 7438 | `"            or review_status != \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L007439](../../agents/web_agent.py#L7439) | 7439 | `"            or answer_integrity[\"potentially_missing_target_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L007440](../../agents/web_agent.py#L7440) | 7440 | `"            or answer_integrity[\"source_evidence_gap_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L007441](../../agents/web_agent.py#L7441) | 7441 | `"            or citation_validation[\"valid_citation_count\"] == 0"` | — |
| [SRC-1AE03B9EC3-L007442](../../agents/web_agent.py#L7442) | 7442 | `"            or semantic_answer_withheld"` | — |
| [SRC-1AE03B9EC3-L007443](../../agents/web_agent.py#L7443) | 7443 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L007444](../../agents/web_agent.py#L7444) | 7444 | `"            pipeline_completion_status = \"partial\""` | — |
| [SRC-1AE03B9EC3-L007445](../../agents/web_agent.py#L7445) | 7445 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L007446](../../agents/web_agent.py#L7446) | 7446 | `"            pipeline_completion_status = \"completed\""` | — |
| [SRC-1AE03B9EC3-L007447](../../agents/web_agent.py#L7447) | 7447 | `"        completion_stages = {"` | — |
| [SRC-1AE03B9EC3-L007448](../../agents/web_agent.py#L7448) | 7448 | `"            \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L007449](../../agents/web_agent.py#L7449) | 7449 | `"            \"accepted_sources\": len(sources),"` | — |
| [SRC-1AE03B9EC3-L007450](../../agents/web_agent.py#L7450) | 7450 | `"            \"pages_read\": fetched_pages,"` | — |
| [SRC-1AE03B9EC3-L007451](../../agents/web_agent.py#L7451) | 7451 | `"            \"answer_generated_by_model\": bool(used_llm),"` | — |
| [SRC-1AE03B9EC3-L007452](../../agents/web_agent.py#L7452) | 7452 | `"            \"claim_review\": review_status,"` | — |
| [SRC-1AE03B9EC3-L007453](../../agents/web_agent.py#L7453) | 7453 | `"            \"valid_citations\": citation_validation[\"valid_citation_count\"],"` | — |
| [SRC-1AE03B9EC3-L007454](../../agents/web_agent.py#L7454) | 7454 | `"            \"semantic_fact_check\": \"not_performed\","` | — |
| [SRC-1AE03B9EC3-L007455](../../agents/web_agent.py#L7455) | 7455 | `"            \"semantic_claim_support_assessment\": semantic_claim_verification.get(\"status\", \"not_performed\"),"` | — |
| [SRC-1AE03B9EC3-L007456](../../agents/web_agent.py#L7456) | 7456 | `"        }"` | — |
| [SRC-1AE03B9EC3-L007457](../../agents/web_agent.py#L7457) | 7457 | `"        if semantic_answer_withheld:"` | — |
| [SRC-1AE03B9EC3-L007458](../../agents/web_agent.py#L7458) | 7458 | `"            pipeline_completion_status = \"partial\""` | — |
| [SRC-1AE03B9EC3-L007459](../../agents/web_agent.py#L7459) | 7459 | `"        report[\"pipeline_completion_status\"] = pipeline_completion_status"` | — |
| [SRC-1AE03B9EC3-L007460](../../agents/web_agent.py#L7460) | 7460 | `"        report[\"completion_stages\"] = completion_stages"` | — |
| [SRC-1AE03B9EC3-L007461](../../agents/web_agent.py#L7461) | 7461 | `"        report[\"pipeline_completion_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L007462](../../agents/web_agent.py#L7462) | 7462 | `"            \"pipeline stage completion only; not a guarantee of factual correctness\""` | — |
| [SRC-1AE03B9EC3-L007463](../../agents/web_agent.py#L7463) | 7463 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007464](../../agents/web_agent.py#L7464) | 7464 | `""` | — |
| [SRC-1AE03B9EC3-L007465](../../agents/web_agent.py#L7465) | 7465 | `"        public_sources = []"` | — |
| [SRC-1AE03B9EC3-L007466](../../agents/web_agent.py#L7466) | 7466 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L007467](../../agents/web_agent.py#L7467) | 7467 | `"            public_sources.append({"` | — |
| [SRC-1AE03B9EC3-L007468](../../agents/web_agent.py#L7468) | 7468 | `"                \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L007469](../../agents/web_agent.py#L7469) | 7469 | `"                \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L007470](../../agents/web_agent.py#L7470) | 7470 | `"                \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007471](../../agents/web_agent.py#L7471) | 7471 | `"                \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L007472](../../agents/web_agent.py#L7472) | 7472 | `"                \"readable_page_text_available\": bool(source.get(\"page_fetched\")) and bool(str(source.get(\"page_text\") or \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L007473](../../agents/web_agent.py#L7473) | 7473 | `"                \"page_text_present_without_fetch_flag\": bool(str(source.get(\"page_text\") or \"\").strip()) and not bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L007474](../../agents/web_agent.py#L7474) | 7474 | `"                \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L007475](../../agents/web_agent.py#L7475) | 7475 | `"                \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L007476](../../agents/web_agent.py#L7476) | 7476 | `"                \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L007477](../../agents/web_agent.py#L7477) | 7477 | `"                \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007478](../../agents/web_agent.py#L7478) | 7478 | `"                \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L007479](../../agents/web_agent.py#L7479) | 7479 | `"                \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007480](../../agents/web_agent.py#L7480) | 7480 | `"                \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007481](../../agents/web_agent.py#L7481) | 7481 | `"                \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007482](../../agents/web_agent.py#L7482) | 7482 | `"                \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L007483](../../agents/web_agent.py#L7483) | 7483 | `"                \"lead_qualification\": source.get(\"lead_qualification\"),"` | — |
| [SRC-1AE03B9EC3-L007484](../../agents/web_agent.py#L7484) | 7484 | `"                \"lead_intent_evidence\": source.get(\"lead_intent_evidence\"),"` | — |
| [SRC-1AE03B9EC3-L007485](../../agents/web_agent.py#L7485) | 7485 | `"            })"` | — |
| [SRC-1AE03B9EC3-L007486](../../agents/web_agent.py#L7486) | 7486 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L007487](../../agents/web_agent.py#L7487) | 7487 | `"            \"answer\": answer,"` | — |
| [SRC-1AE03B9EC3-L007488](../../agents/web_agent.py#L7488) | 7488 | `"            \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L007489](../../agents/web_agent.py#L7489) | 7489 | `"            \"search_query\": (plan.get(\"queries\") or [\"\"])[0],"` | — |
| [SRC-1AE03B9EC3-L007490](../../agents/web_agent.py#L7490) | 7490 | `"            \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L007491](../../agents/web_agent.py#L7491) | 7491 | `"            \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L007492](../../agents/web_agent.py#L7492) | 7492 | `"                \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L007493](../../agents/web_agent.py#L7493) | 7493 | `"                \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L007494](../../agents/web_agent.py#L7494) | 7494 | `"                \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L007495](../../agents/web_agent.py#L7495) | 7495 | `"                \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L007496](../../agents/web_agent.py#L7496) | 7496 | `"                \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L007497](../../agents/web_agent.py#L7497) | 7497 | `"                \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L007498](../../agents/web_agent.py#L7498) | 7498 | `"                \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L007499](../../agents/web_agent.py#L7499) | 7499 | `"                \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L007500](../../agents/web_agent.py#L7500) | 7500 | `"                \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L007501](../../agents/web_agent.py#L7501) | 7501 | `"                \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L007502](../../agents/web_agent.py#L7502) | 7502 | `"            },"` | — |
| [SRC-1AE03B9EC3-L007503](../../agents/web_agent.py#L7503) | 7503 | `"            \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L007504](../../agents/web_agent.py#L7504) | 7504 | `"            \"sources\": public_sources,"` | — |
| [SRC-1AE03B9EC3-L007505](../../agents/web_agent.py#L7505) | 7505 | `"            \"research_quality\": research_quality,"` | — |
| [SRC-1AE03B9EC3-L007506](../../agents/web_agent.py#L7506) | 7506 | `"            \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L007507](../../agents/web_agent.py#L7507) | 7507 | `"            \"answer_evidence_status\": answer_evidence_status,"` | — |
| [SRC-1AE03B9EC3-L007508](../../agents/web_agent.py#L7508) | 7508 | `"            \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L007509](../../agents/web_agent.py#L7509) | 7509 | `"            \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L007510](../../agents/web_agent.py#L7510) | 7510 | `"            \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L007511](../../agents/web_agent.py#L7511) | 7511 | `"            \"coverage_repair_status\": coverage_repair_status,"` | — |
| [SRC-1AE03B9EC3-L007512](../../agents/web_agent.py#L7512) | 7512 | `"            \"used_language_model\": used_llm,"` | — |
| [SRC-1AE03B9EC3-L007513](../../agents/web_agent.py#L7513) | 7513 | `"            \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L007514](../../agents/web_agent.py#L7514) | 7514 | `"            \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L007515](../../agents/web_agent.py#L7515) | 7515 | `"            \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L007516](../../agents/web_agent.py#L7516) | 7516 | `"            \"warnings\": warnings,"` | — |
| [SRC-1AE03B9EC3-L007517](../../agents/web_agent.py#L7517) | 7517 | `"            \"kind\": \"web_research\" if used_llm else \"web_fallback\","` | — |
| [SRC-1AE03B9EC3-L007518](../../agents/web_agent.py#L7518) | 7518 | `"            \"final_answer_status\": final_answer_status,"` | — |
| [SRC-1AE03B9EC3-L007519](../../agents/web_agent.py#L7519) | 7519 | `"            \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L007520](../../agents/web_agent.py#L7520) | 7520 | `"            \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L007521](../../agents/web_agent.py#L7521) | 7521 | `"        }"` | — |
| [SRC-1AE03B9EC3-L007522](../../agents/web_agent.py#L7522) | 7522 | `""` | — |
| [SRC-1AE03B9EC3-L007523](../../agents/web_agent.py#L7523) | 7523 | `"def _normalized_provider_usage("` | — |
| [SRC-1AE03B9EC3-L007524](../../agents/web_agent.py#L7524) | 7524 | `"    usage: Any, *, provider_base_url: str = \"\""` | — |
| [SRC-1AE03B9EC3-L007525](../../agents/web_agent.py#L7525) | 7525 | `") -> dict[str, int \| float] \| None:"` | — |
| [SRC-1AE03B9EC3-L007526](../../agents/web_agent.py#L7526) | 7526 | `"    \"\"\"Allowlist safe counters; interpret generic 'cost' as USD only for OpenRouter.\"\"\""` | — |
| [SRC-1AE03B9EC3-L007527](../../agents/web_agent.py#L7527) | 7527 | `"    if not isinstance(usage, dict):"` | — |
| [SRC-1AE03B9EC3-L007528](../../agents/web_agent.py#L7528) | 7528 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L007529](../../agents/web_agent.py#L7529) | 7529 | `"    normalized: dict[str, int \| float] = {}"` | — |
| [SRC-1AE03B9EC3-L007530](../../agents/web_agent.py#L7530) | 7530 | `"    for source_key in (\"prompt_tokens\", \"completion_tokens\", \"total_tokens\"):"` | — |
| [SRC-1AE03B9EC3-L007531](../../agents/web_agent.py#L7531) | 7531 | `"        value = usage.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L007532](../../agents/web_agent.py#L7532) | 7532 | `"        if isinstance(value, int) and not isinstance(value, bool) and value >= 0:"` | — |
| [SRC-1AE03B9EC3-L007533](../../agents/web_agent.py#L7533) | 7533 | `"            normalized[source_key] = value"` | — |
| [SRC-1AE03B9EC3-L007534](../../agents/web_agent.py#L7534) | 7534 | `"    cost_keys = [\"cost_usd\"]"` | — |
| [SRC-1AE03B9EC3-L007535](../../agents/web_agent.py#L7535) | 7535 | `"    provider_host = \"\""` | — |
| [SRC-1AE03B9EC3-L007536](../../agents/web_agent.py#L7536) | 7536 | `"    if isinstance(provider_base_url, str):"` | — |
| [SRC-1AE03B9EC3-L007537](../../agents/web_agent.py#L7537) | 7537 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L007538](../../agents/web_agent.py#L7538) | 7538 | `"            provider_host = (urllib.parse.urlsplit(provider_base_url.strip()).hostname or \"\").lower().rstrip(\".\")"` | — |
| [SRC-1AE03B9EC3-L007539](../../agents/web_agent.py#L7539) | 7539 | `"        except ValueError:"` | — |
| [SRC-1AE03B9EC3-L007540](../../agents/web_agent.py#L7540) | 7540 | `"            provider_host = \"\""` | — |
| [SRC-1AE03B9EC3-L007541](../../agents/web_agent.py#L7541) | 7541 | `"    is_openrouter = ("` | — |
| [SRC-1AE03B9EC3-L007542](../../agents/web_agent.py#L7542) | 7542 | `"        provider_host == \"openrouter.ai\""` | — |
| [SRC-1AE03B9EC3-L007543](../../agents/web_agent.py#L7543) | 7543 | `"        or provider_host.endswith(\".openrouter.ai\")"` | — |
| [SRC-1AE03B9EC3-L007544](../../agents/web_agent.py#L7544) | 7544 | `"    )"` | — |
| [SRC-1AE03B9EC3-L007545](../../agents/web_agent.py#L7545) | 7545 | `"    if is_openrouter:"` | — |
| [SRC-1AE03B9EC3-L007546](../../agents/web_agent.py#L7546) | 7546 | `"        cost_keys.extend([\"cost\", \"total_cost\"])"` | — |
| [SRC-1AE03B9EC3-L007547](../../agents/web_agent.py#L7547) | 7547 | `"    for source_key in cost_keys:"` | — |
| [SRC-1AE03B9EC3-L007548](../../agents/web_agent.py#L7548) | 7548 | `"        value = usage.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L007549](../../agents/web_agent.py#L7549) | 7549 | `"        if isinstance(value, (int, float)) and not isinstance(value, bool):"` | — |
| [SRC-1AE03B9EC3-L007550](../../agents/web_agent.py#L7550) | 7550 | `"            number = float(value)"` | — |
| [SRC-1AE03B9EC3-L007551](../../agents/web_agent.py#L7551) | 7551 | `"            if number >= 0 and math.isfinite(number):"` | — |
| [SRC-1AE03B9EC3-L007552](../../agents/web_agent.py#L7552) | 7552 | `"                normalized[\"cost_usd\"] = number"` | — |
| [SRC-1AE03B9EC3-L007553](../../agents/web_agent.py#L7553) | 7553 | `"                break"` | — |
| [SRC-1AE03B9EC3-L007554](../../agents/web_agent.py#L7554) | 7554 | `"    return normalized or None"` | — |
| [SRC-1AE03B9EC3-L007555](../../agents/web_agent.py#L7555) | 7555 | `""` | — |
| [SRC-1AE03B9EC3-L007556](../../agents/web_agent.py#L7556) | 7556 | `"def _model_usage_record("` | — |
| [SRC-1AE03B9EC3-L007557](../../agents/web_agent.py#L7557) | 7557 | `"    requested_model: str,"` | — |
| [SRC-1AE03B9EC3-L007558](../../agents/web_agent.py#L7558) | 7558 | `"    candidate_model: str,"` | — |
| [SRC-1AE03B9EC3-L007559](../../agents/web_agent.py#L7559) | 7559 | `"    response_data: dict[str, Any],"` | — |
| [SRC-1AE03B9EC3-L007560](../../agents/web_agent.py#L7560) | 7560 | `"    provider_base_url: str,"` | — |
| [SRC-1AE03B9EC3-L007561](../../agents/web_agent.py#L7561) | 7561 | `") -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L007562](../../agents/web_agent.py#L7562) | 7562 | `"    \"\"\"Return only allowlisted provider usage metadata, never raw prompts/responses.\"\"\""` | — |
| [SRC-1AE03B9EC3-L007563](../../agents/web_agent.py#L7563) | 7563 | `"    record: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L007564](../../agents/web_agent.py#L7564) | 7564 | `"        \"requested_model\": requested_model,"` | — |
| [SRC-1AE03B9EC3-L007565](../../agents/web_agent.py#L7565) | 7565 | `"        \"used_model\": candidate_model,"` | — |
| [SRC-1AE03B9EC3-L007566](../../agents/web_agent.py#L7566) | 7566 | `"        \"fallback_used\": \"true\" if candidate_model != requested_model else \"false\","` | — |
| [SRC-1AE03B9EC3-L007567](../../agents/web_agent.py#L7567) | 7567 | `"    }"` | — |
| [SRC-1AE03B9EC3-L007568](../../agents/web_agent.py#L7568) | 7568 | `"    provider_usage = _normalized_provider_usage("` | — |
| [SRC-1AE03B9EC3-L007569](../../agents/web_agent.py#L7569) | 7569 | `"        response_data.get(\"usage\"), provider_base_url=provider_base_url"` | — |
| [SRC-1AE03B9EC3-L007570](../../agents/web_agent.py#L7570) | 7570 | `"    )"` | — |
| [SRC-1AE03B9EC3-L007571](../../agents/web_agent.py#L7571) | 7571 | `"    if provider_usage is not None:"` | — |
| [SRC-1AE03B9EC3-L007572](../../agents/web_agent.py#L7572) | 7572 | `"        record[\"provider_usage\"] = provider_usage"` | — |
| [SRC-1AE03B9EC3-L007573](../../agents/web_agent.py#L7573) | 7573 | `"    return record"` | — |
## واجهات API

### FILE-D8438CDB65 — [api/__init__.py](../../api/__init__.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-D8438CDB65-L000001](../../api/__init__.py#L1) | 1 | `"\"\"\"Omarai local API package.\"\"\""` | — |
## واجهات API

### FILE-EEF2E6447C — [api/omarai.py](../../api/omarai.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-EEF2E6447C-L000001](../../api/omarai.py#L1) | 1 | `"\"\"\"HTTP API for Omarai's web-research agent and lead workspace.\"\"\""` | — |
| [SRC-EEF2E6447C-L000002](../../api/omarai.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-EEF2E6447C-L000003](../../api/omarai.py#L3) | 3 | `""` | — |
| [SRC-EEF2E6447C-L000004](../../api/omarai.py#L4) | 4 | `"import base64"` | — |
| [SRC-EEF2E6447C-L000005](../../api/omarai.py#L5) | 5 | `"import hashlib"` | — |
| [SRC-EEF2E6447C-L000006](../../api/omarai.py#L6) | 6 | `"import hmac"` | — |
| [SRC-EEF2E6447C-L000007](../../api/omarai.py#L7) | 7 | `"import ipaddress"` | — |
| [SRC-EEF2E6447C-L000008](../../api/omarai.py#L8) | 8 | `"import json"` | — |
| [SRC-EEF2E6447C-L000009](../../api/omarai.py#L9) | 9 | `"import os"` | — |
| [SRC-EEF2E6447C-L000010](../../api/omarai.py#L10) | 10 | `"import re"` | — |
| [SRC-EEF2E6447C-L000011](../../api/omarai.py#L11) | 11 | `"import threading"` | — |
| [SRC-EEF2E6447C-L000012](../../api/omarai.py#L12) | 12 | `"import time"` | — |
| [SRC-EEF2E6447C-L000013](../../api/omarai.py#L13) | 13 | `"from collections import defaultdict, deque"` | — |
| [SRC-EEF2E6447C-L000014](../../api/omarai.py#L14) | 14 | `"from functools import lru_cache"` | — |
| [SRC-EEF2E6447C-L000015](../../api/omarai.py#L15) | 15 | `"from http.cookies import SimpleCookie"` | — |
| [SRC-EEF2E6447C-L000016](../../api/omarai.py#L16) | 16 | `"from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer"` | — |
| [SRC-EEF2E6447C-L000017](../../api/omarai.py#L17) | 17 | `"from pathlib import Path"` | — |
| [SRC-EEF2E6447C-L000018](../../api/omarai.py#L18) | 18 | `"from typing import ClassVar"` | — |
| [SRC-EEF2E6447C-L000019](../../api/omarai.py#L19) | 19 | `"from urllib.parse import parse_qs, urlparse"` | — |
| [SRC-EEF2E6447C-L000020](../../api/omarai.py#L20) | 20 | `""` | — |
| [SRC-EEF2E6447C-L000021](../../api/omarai.py#L21) | 21 | `"from agents.omarai import LeadStore, analyze, normalize"` | — |
| [SRC-EEF2E6447C-L000022](../../api/omarai.py#L22) | 22 | `"from agents.sales_domain import MarketProfile, ProductProfile, build_buyer_queries"` | — |
| [SRC-EEF2E6447C-L000023](../../api/omarai.py#L23) | 23 | `"from agents.web_agent import WebAgent"` | — |
| [SRC-EEF2E6447C-L000024](../../api/omarai.py#L24) | 24 | `""` | — |
| [SRC-EEF2E6447C-L000025](../../api/omarai.py#L25) | 25 | `"ROOT = Path(__file__).resolve().parents[1] / \"web\""` | — |
| [SRC-EEF2E6447C-L000026](../../api/omarai.py#L26) | 26 | `"AGENT_DASHBOARD = ROOT / \"agent.html\""` | — |
| [SRC-EEF2E6447C-L000027](../../api/omarai.py#L27) | 27 | `"LEADS_DASHBOARD = ROOT / \"dashboard.html\""` | — |
| [SRC-EEF2E6447C-L000028](../../api/omarai.py#L28) | 28 | `"WORKSPACE_DASHBOARD = ROOT / \"workspace.html\""` | — |
| [SRC-EEF2E6447C-L000029](../../api/omarai.py#L29) | 29 | `"MAX_REQUEST_BODY_BYTES = 200_000"` | — |
| [SRC-EEF2E6447C-L000030](../../api/omarai.py#L30) | 30 | `"BROWSER_SESSION_COOKIE_MAX_AGE = 8 * 60 * 60"` | — |
| [SRC-EEF2E6447C-L000031](../../api/omarai.py#L31) | 31 | `"BROWSER_SESSION_ID_RE = re.compile(r\"^[A-Za-z0-9_-]{32,128}$\")"` | — |
| [SRC-EEF2E6447C-L000032](../../api/omarai.py#L32) | 32 | `""` | — |
| [SRC-EEF2E6447C-L000033](../../api/omarai.py#L33) | 33 | `""` | — |
| [SRC-EEF2E6447C-L000034](../../api/omarai.py#L34) | 34 | `"def _csp_hash_source(value: str) -> str:"` | — |
| [SRC-EEF2E6447C-L000035](../../api/omarai.py#L35) | 35 | `"    digest = base64.b64encode(hashlib.sha256(value.encode(\"utf-8\")).digest()).decode(\"ascii\")"` | — |
| [SRC-EEF2E6447C-L000036](../../api/omarai.py#L36) | 36 | `"    return f\"'sha256-{digest}'\""` | — |
| [SRC-EEF2E6447C-L000037](../../api/omarai.py#L37) | 37 | `""` | — |
| [SRC-EEF2E6447C-L000038](../../api/omarai.py#L38) | 38 | `""` | — |
| [SRC-EEF2E6447C-L000039](../../api/omarai.py#L39) | 39 | `"@lru_cache(maxsize=1)"` | — |
| [SRC-EEF2E6447C-L000040](../../api/omarai.py#L40) | 40 | `"def _content_security_policy() -> str:"` | — |
| [SRC-EEF2E6447C-L000041](../../api/omarai.py#L41) | 41 | `"    \"\"\"Allow only known inline blocks/attributes from the static first-party HTML."` | — |
| [SRC-EEF2E6447C-L000042](../../api/omarai.py#L42) | 42 | `""` | — |
| [SRC-EEF2E6447C-L000043](../../api/omarai.py#L43) | 43 | `"    Hashes deliberately replace unsafe-inline. Updating an inline script/style means its"` | — |
| [SRC-EEF2E6447C-L000044](../../api/omarai.py#L44) | 44 | `"    hash changes automatically with the served source. This is not a sanitizer for"` | — |
| [SRC-EEF2E6447C-L000045](../../api/omarai.py#L45) | 45 | `"    untrusted HTML; callers must never splice untrusted input into these static files."` | — |
| [SRC-EEF2E6447C-L000046](../../api/omarai.py#L46) | 46 | `"    \"\"\""` | — |
| [SRC-EEF2E6447C-L000047](../../api/omarai.py#L47) | 47 | `"    script_hashes: set[str] = set()"` | — |
| [SRC-EEF2E6447C-L000048](../../api/omarai.py#L48) | 48 | `"    style_hashes: set[str] = set()"` | — |
| [SRC-EEF2E6447C-L000049](../../api/omarai.py#L49) | 49 | `"    event_handler_hashes: set[str] = set()"` | — |
| [SRC-EEF2E6447C-L000050](../../api/omarai.py#L50) | 50 | `"    style_attribute_hashes: set[str] = set()"` | — |
| [SRC-EEF2E6447C-L000051](../../api/omarai.py#L51) | 51 | `""` | — |
| [SRC-EEF2E6447C-L000052](../../api/omarai.py#L52) | 52 | `"    for html_path in sorted(ROOT.glob(\"*.html\")):"` | — |
| [SRC-EEF2E6447C-L000053](../../api/omarai.py#L53) | 53 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000054](../../api/omarai.py#L54) | 54 | `"            document = html_path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-EEF2E6447C-L000055](../../api/omarai.py#L55) | 55 | `"        except (OSError, UnicodeError):"` | — |
| [SRC-EEF2E6447C-L000056](../../api/omarai.py#L56) | 56 | `"            continue"` | — |
| [SRC-EEF2E6447C-L000057](../../api/omarai.py#L57) | 57 | `""` | — |
| [SRC-EEF2E6447C-L000058](../../api/omarai.py#L58) | 58 | `"        for match in re.finditer("` | — |
| [SRC-EEF2E6447C-L000059](../../api/omarai.py#L59) | 59 | `"            r\"<script\\b(?P<attrs>[^>]*)>(?P<body>.*?)</script\\s*>\","` | — |
| [SRC-EEF2E6447C-L000060](../../api/omarai.py#L60) | 60 | `"            document,"` | — |
| [SRC-EEF2E6447C-L000061](../../api/omarai.py#L61) | 61 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-EEF2E6447C-L000062](../../api/omarai.py#L62) | 62 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000063](../../api/omarai.py#L63) | 63 | `"            if re.search(r\"\\bsrc\\s*=\", match.group(\"attrs\"), re.IGNORECASE):"` | — |
| [SRC-EEF2E6447C-L000064](../../api/omarai.py#L64) | 64 | `"                continue"` | — |
| [SRC-EEF2E6447C-L000065](../../api/omarai.py#L65) | 65 | `"            script_hashes.add(_csp_hash_source(match.group(\"body\")))"` | — |
| [SRC-EEF2E6447C-L000066](../../api/omarai.py#L66) | 66 | `""` | — |
| [SRC-EEF2E6447C-L000067](../../api/omarai.py#L67) | 67 | `"        for match in re.finditer("` | — |
| [SRC-EEF2E6447C-L000068](../../api/omarai.py#L68) | 68 | `"            r\"<style\\b[^>]*>(?P<body>.*?)</style\\s*>\","` | — |
| [SRC-EEF2E6447C-L000069](../../api/omarai.py#L69) | 69 | `"            document,"` | — |
| [SRC-EEF2E6447C-L000070](../../api/omarai.py#L70) | 70 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-EEF2E6447C-L000071](../../api/omarai.py#L71) | 71 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000072](../../api/omarai.py#L72) | 72 | `"            style_hashes.add(_csp_hash_source(match.group(\"body\")))"` | — |
| [SRC-EEF2E6447C-L000073](../../api/omarai.py#L73) | 73 | `""` | — |
| [SRC-EEF2E6447C-L000074](../../api/omarai.py#L74) | 74 | `"        # This scan intentionally includes style/event attributes embedded in"` | — |
| [SRC-EEF2E6447C-L000075](../../api/omarai.py#L75) | 75 | `"        # trusted first-party HTML templates assembled by inline scripts."` | — |
| [SRC-EEF2E6447C-L000076](../../api/omarai.py#L76) | 76 | `"        for match in re.finditer("` | — |
| [SRC-EEF2E6447C-L000077](../../api/omarai.py#L77) | 77 | `"            r\"\"\"\\bstyle\\s*=\\s*([\"'])(.*?)\\1\"\"\","` | — |
| [SRC-EEF2E6447C-L000078](../../api/omarai.py#L78) | 78 | `"            document,"` | — |
| [SRC-EEF2E6447C-L000079](../../api/omarai.py#L79) | 79 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-EEF2E6447C-L000080](../../api/omarai.py#L80) | 80 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000081](../../api/omarai.py#L81) | 81 | `"            style_attribute_hashes.add(_csp_hash_source(match.group(2).strip()))"` | — |
| [SRC-EEF2E6447C-L000082](../../api/omarai.py#L82) | 82 | `""` | — |
| [SRC-EEF2E6447C-L000083](../../api/omarai.py#L83) | 83 | `"        for match in re.finditer("` | — |
| [SRC-EEF2E6447C-L000084](../../api/omarai.py#L84) | 84 | `"            r\"\"\"\\bon[a-z]+\\s*=\\s*([\"'])(.*?)\\1\"\"\","` | — |
| [SRC-EEF2E6447C-L000085](../../api/omarai.py#L85) | 85 | `"            document,"` | — |
| [SRC-EEF2E6447C-L000086](../../api/omarai.py#L86) | 86 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-EEF2E6447C-L000087](../../api/omarai.py#L87) | 87 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000088](../../api/omarai.py#L88) | 88 | `"            event_handler_hashes.add(_csp_hash_source(match.group(2).strip()))"` | — |
| [SRC-EEF2E6447C-L000089](../../api/omarai.py#L89) | 89 | `""` | — |
| [SRC-EEF2E6447C-L000090](../../api/omarai.py#L90) | 90 | `"    script_sources = [\"'self'\", *sorted(script_hashes)]"` | — |
| [SRC-EEF2E6447C-L000091](../../api/omarai.py#L91) | 91 | `"    style_sources = [\"'self'\", *sorted(style_hashes)]"` | — |
| [SRC-EEF2E6447C-L000092](../../api/omarai.py#L92) | 92 | `"    if event_handler_hashes:"` | — |
| [SRC-EEF2E6447C-L000093](../../api/omarai.py#L93) | 93 | `"        script_sources.extend([\"'unsafe-hashes'\", *sorted(event_handler_hashes)])"` | — |
| [SRC-EEF2E6447C-L000094](../../api/omarai.py#L94) | 94 | `"    if style_attribute_hashes:"` | — |
| [SRC-EEF2E6447C-L000095](../../api/omarai.py#L95) | 95 | `"        style_sources.extend([\"'unsafe-hashes'\", *sorted(style_attribute_hashes)])"` | — |
| [SRC-EEF2E6447C-L000096](../../api/omarai.py#L96) | 96 | `""` | — |
| [SRC-EEF2E6447C-L000097](../../api/omarai.py#L97) | 97 | `"    return ("` | — |
| [SRC-EEF2E6447C-L000098](../../api/omarai.py#L98) | 98 | `"        \"default-src 'self'; base-uri 'self'; object-src 'none'; frame-ancestors 'none'; \""` | — |
| [SRC-EEF2E6447C-L000099](../../api/omarai.py#L99) | 99 | `"        \"form-action 'self'; connect-src 'self'; img-src 'self' data:; \""` | — |
| [SRC-EEF2E6447C-L000100](../../api/omarai.py#L100) | 100 | `"        f\"script-src {' '.join(script_sources)}; \""` | — |
| [SRC-EEF2E6447C-L000101](../../api/omarai.py#L101) | 101 | `"        f\"style-src {' '.join(style_sources)}; font-src 'self' data:\""` | — |
| [SRC-EEF2E6447C-L000102](../../api/omarai.py#L102) | 102 | `"    )"` | — |
| [SRC-EEF2E6447C-L000103](../../api/omarai.py#L103) | 103 | `"# Bound request-line + header parsing before application code or body processing."` | — |
| [SRC-EEF2E6447C-L000104](../../api/omarai.py#L104) | 104 | `"REQUEST_HEADER_READ_TIMEOUT_SECONDS = 8.0"` | — |
| [SRC-EEF2E6447C-L000105](../../api/omarai.py#L105) | 105 | `"REQUEST_HEADER_IDLE_TIMEOUT_SECONDS = 2.0"` | — |
| [SRC-EEF2E6447C-L000106](../../api/omarai.py#L106) | 106 | `"MAX_REQUEST_HEADER_READ_TIMEOUT_SECONDS = 15.0"` | — |
| [SRC-EEF2E6447C-L000107](../../api/omarai.py#L107) | 107 | `"# Absolute deadline for reading the entire body, not merely a per-read idle timeout."` | — |
| [SRC-EEF2E6447C-L000108](../../api/omarai.py#L108) | 108 | `"REQUEST_BODY_READ_TIMEOUT_SECONDS = 10.0"` | — |
| [SRC-EEF2E6447C-L000109](../../api/omarai.py#L109) | 109 | `"REQUEST_BODY_IDLE_TIMEOUT_SECONDS = 2.0"` | — |
| [SRC-EEF2E6447C-L000110](../../api/omarai.py#L110) | 110 | `"MAX_REQUEST_BODY_READ_TIMEOUT_SECONDS = 30.0"` | — |
| [SRC-EEF2E6447C-L000111](../../api/omarai.py#L111) | 111 | `"REQUEST_BODY_READ_CHUNK_BYTES = 8_192"` | — |
| [SRC-EEF2E6447C-L000112](../../api/omarai.py#L112) | 112 | `""` | — |
| [SRC-EEF2E6447C-L000113](../../api/omarai.py#L113) | 113 | `""` | — |
| [SRC-EEF2E6447C-L000114](../../api/omarai.py#L114) | 114 | `""` | — |
| [SRC-EEF2E6447C-L000115](../../api/omarai.py#L115) | 115 | `"def _lead_store_from_environment() -> LeadStore:"` | — |
| [SRC-EEF2E6447C-L000116](../../api/omarai.py#L116) | 116 | `"    \"\"\"Select managed PostgreSQL when configured; otherwise retain local SQLite.\"\"\""` | — |
| [SRC-EEF2E6447C-L000117](../../api/omarai.py#L117) | 117 | `"    database_url = ("` | — |
| [SRC-EEF2E6447C-L000118](../../api/omarai.py#L118) | 118 | `"        os.getenv(\"OMARAI_DATABASE_URL\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000119](../../api/omarai.py#L119) | 119 | `"        or os.getenv(\"DATABASE_URL\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000120](../../api/omarai.py#L120) | 120 | `"    )"` | — |
| [SRC-EEF2E6447C-L000121](../../api/omarai.py#L121) | 121 | `"    configured_path = os.getenv(\"OMARAI_DB_PATH\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000122](../../api/omarai.py#L122) | 122 | `"    if database_url and configured_path:"` | — |
| [SRC-EEF2E6447C-L000123](../../api/omarai.py#L123) | 123 | `"        raise ValueError("` | — |
| [SRC-EEF2E6447C-L000124](../../api/omarai.py#L124) | 124 | `"            \"configure either OMARAI_DATABASE_URL/DATABASE_URL or OMARAI_DB_PATH, not both\""` | — |
| [SRC-EEF2E6447C-L000125](../../api/omarai.py#L125) | 125 | `"        )"` | — |
| [SRC-EEF2E6447C-L000126](../../api/omarai.py#L126) | 126 | `"    return LeadStore(configured_path or None, database_url=database_url or None)"` | — |
| [SRC-EEF2E6447C-L000127](../../api/omarai.py#L127) | 127 | `""` | — |
| [SRC-EEF2E6447C-L000128](../../api/omarai.py#L128) | 128 | `""` | — |
| [SRC-EEF2E6447C-L000129](../../api/omarai.py#L129) | 129 | `"def _profile_terms(value, field_name: str) -> tuple[str, ...]:"` | — |
| [SRC-EEF2E6447C-L000130](../../api/omarai.py#L130) | 130 | `"    \"\"\"Validate bounded ProductProfile/MarketProfile string arrays.\"\"\""` | — |
| [SRC-EEF2E6447C-L000131](../../api/omarai.py#L131) | 131 | `"    if value is None:"` | — |
| [SRC-EEF2E6447C-L000132](../../api/omarai.py#L132) | 132 | `"        return ()"` | — |
| [SRC-EEF2E6447C-L000133](../../api/omarai.py#L133) | 133 | `"    if not isinstance(value, list) or len(value) > 40:"` | — |
| [SRC-EEF2E6447C-L000134](../../api/omarai.py#L134) | 134 | `"        raise ValueError(f\"{field_name} must be a list of at most 40 strings\")"` | — |
| [SRC-EEF2E6447C-L000135](../../api/omarai.py#L135) | 135 | `"    if any(not isinstance(item, str) or len(item) > 240 for item in value):"` | — |
| [SRC-EEF2E6447C-L000136](../../api/omarai.py#L136) | 136 | `"        raise ValueError(f\"{field_name} items must be strings of at most 240 characters\")"` | — |
| [SRC-EEF2E6447C-L000137](../../api/omarai.py#L137) | 137 | `"    return tuple(value)"` | — |
| [SRC-EEF2E6447C-L000138](../../api/omarai.py#L138) | 138 | `""` | — |
| [SRC-EEF2E6447C-L000139](../../api/omarai.py#L139) | 139 | `""` | — |
| [SRC-EEF2E6447C-L000140](../../api/omarai.py#L140) | 140 | `"def _product_market_from_payload(data: dict):"` | — |
| [SRC-EEF2E6447C-L000141](../../api/omarai.py#L141) | 141 | `"    product_data = data.get(\"product\")"` | — |
| [SRC-EEF2E6447C-L000142](../../api/omarai.py#L142) | 142 | `"    market_data = data.get(\"market\")"` | — |
| [SRC-EEF2E6447C-L000143](../../api/omarai.py#L143) | 143 | `"    if not isinstance(product_data, dict) or not isinstance(market_data, dict):"` | — |
| [SRC-EEF2E6447C-L000144](../../api/omarai.py#L144) | 144 | `"        raise TypeError(\"product and market objects are required\")"` | — |
| [SRC-EEF2E6447C-L000145](../../api/omarai.py#L145) | 145 | `"    product = ProductProfile("` | — |
| [SRC-EEF2E6447C-L000146](../../api/omarai.py#L146) | 146 | `"        name=product_data.get(\"name\", \"\"),"` | — |
| [SRC-EEF2E6447C-L000147](../../api/omarai.py#L147) | 147 | `"        aliases=_profile_terms(product_data.get(\"aliases\"), \"aliases\"),"` | — |
| [SRC-EEF2E6447C-L000148](../../api/omarai.py#L148) | 148 | `"        category_path=_profile_terms(product_data.get(\"category_path\"), \"category_path\"),"` | — |
| [SRC-EEF2E6447C-L000149](../../api/omarai.py#L149) | 149 | `"        use_cases=_profile_terms(product_data.get(\"use_cases\"), \"use_cases\"),"` | — |
| [SRC-EEF2E6447C-L000150](../../api/omarai.py#L150) | 150 | `"        problems_solved=_profile_terms(product_data.get(\"problems_solved\"), \"problems_solved\"),"` | — |
| [SRC-EEF2E6447C-L000151](../../api/omarai.py#L151) | 151 | `"    )"` | — |
| [SRC-EEF2E6447C-L000152](../../api/omarai.py#L152) | 152 | `"    market = MarketProfile("` | — |
| [SRC-EEF2E6447C-L000153](../../api/omarai.py#L153) | 153 | `"        locations=_profile_terms(market_data.get(\"locations\"), \"locations\"),"` | — |
| [SRC-EEF2E6447C-L000154](../../api/omarai.py#L154) | 154 | `"        industries=_profile_terms(market_data.get(\"industries\"), \"industries\"),"` | — |
| [SRC-EEF2E6447C-L000155](../../api/omarai.py#L155) | 155 | `"        customer_types=_profile_terms(market_data.get(\"customer_types\"), \"customer_types\"),"` | — |
| [SRC-EEF2E6447C-L000156](../../api/omarai.py#L156) | 156 | `"        decision_roles=_profile_terms(market_data.get(\"decision_roles\"), \"decision_roles\"),"` | — |
| [SRC-EEF2E6447C-L000157](../../api/omarai.py#L157) | 157 | `"        exclusions=_profile_terms(market_data.get(\"exclusions\"), \"exclusions\"),"` | — |
| [SRC-EEF2E6447C-L000158](../../api/omarai.py#L158) | 158 | `"    )"` | — |
| [SRC-EEF2E6447C-L000159](../../api/omarai.py#L159) | 159 | `"    locale = data.get(\"locale\", \"auto\")"` | — |
| [SRC-EEF2E6447C-L000160](../../api/omarai.py#L160) | 160 | `"    if not isinstance(locale, str) or locale not in {\"auto\", \"ar\", \"en\", \"mixed\"}:"` | — |
| [SRC-EEF2E6447C-L000161](../../api/omarai.py#L161) | 161 | `"        raise ValueError(\"locale must be auto, ar, en, or mixed\")"` | — |
| [SRC-EEF2E6447C-L000162](../../api/omarai.py#L162) | 162 | `"    return product, market, locale"` | — |
| [SRC-EEF2E6447C-L000163](../../api/omarai.py#L163) | 163 | `""` | — |
| [SRC-EEF2E6447C-L000164](../../api/omarai.py#L164) | 164 | `""` | — |
| [SRC-EEF2E6447C-L000165](../../api/omarai.py#L165) | 165 | `"class _DeadlineRequestReader:"` | — |
| [SRC-EEF2E6447C-L000166](../../api/omarai.py#L166) | 166 | `"    \"\"\"Read HTTP header lines with one absolute deadline across all fragments."` | — |
| [SRC-EEF2E6447C-L000167](../../api/omarai.py#L167) | 167 | `""` | — |
| [SRC-EEF2E6447C-L000168](../../api/omarai.py#L168) | 168 | `"    The standard buffered readline can wait indefinitely for a newline if a"` | — |
| [SRC-EEF2E6447C-L000169](../../api/omarai.py#L169) | 169 | `"    client keeps trickling bytes. This reader checks the same deadline before"` | — |
| [SRC-EEF2E6447C-L000170](../../api/omarai.py#L170) | 170 | `"    every socket read and buffers only bounded look-ahead so request body bytes"` | — |
| [SRC-EEF2E6447C-L000171](../../api/omarai.py#L171) | 171 | `"    received with the headers are preserved for read1()."` | — |
| [SRC-EEF2E6447C-L000172](../../api/omarai.py#L172) | 172 | `"    \"\"\""` | — |
| [SRC-EEF2E6447C-L000173](../../api/omarai.py#L173) | 173 | `""` | — |
| [SRC-EEF2E6447C-L000174](../../api/omarai.py#L174) | 174 | `"    def __init__(self, connection, handler):"` | — |
| [SRC-EEF2E6447C-L000175](../../api/omarai.py#L175) | 175 | `"        self.connection = connection"` | — |
| [SRC-EEF2E6447C-L000176](../../api/omarai.py#L176) | 176 | `"        self.handler = handler"` | — |
| [SRC-EEF2E6447C-L000177](../../api/omarai.py#L177) | 177 | `"        self._buffer = bytearray()"` | — |
| [SRC-EEF2E6447C-L000178](../../api/omarai.py#L178) | 178 | `""` | — |
| [SRC-EEF2E6447C-L000179](../../api/omarai.py#L179) | 179 | `"    def readline(self, limit=-1):"` | — |
| [SRC-EEF2E6447C-L000180](../../api/omarai.py#L180) | 180 | `"        if limit == 0:"` | — |
| [SRC-EEF2E6447C-L000181](../../api/omarai.py#L181) | 181 | `"            return b\"\""` | — |
| [SRC-EEF2E6447C-L000182](../../api/omarai.py#L182) | 182 | `"        max_bytes = int(limit) if limit is not None and limit > 0 else 65_537"` | — |
| [SRC-EEF2E6447C-L000183](../../api/omarai.py#L183) | 183 | `"        previous_timeout = self.connection.gettimeout()"` | — |
| [SRC-EEF2E6447C-L000184](../../api/omarai.py#L184) | 184 | `"        line = bytearray()"` | — |
| [SRC-EEF2E6447C-L000185](../../api/omarai.py#L185) | 185 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000186](../../api/omarai.py#L186) | 186 | `"            while len(line) < max_bytes:"` | — |
| [SRC-EEF2E6447C-L000187](../../api/omarai.py#L187) | 187 | `"                deadline = getattr(self.handler, \"_request_header_deadline\", None)"` | — |
| [SRC-EEF2E6447C-L000188](../../api/omarai.py#L188) | 188 | `"                if deadline is None:"` | — |
| [SRC-EEF2E6447C-L000189](../../api/omarai.py#L189) | 189 | `"                    raise TimeoutError(\"request-header deadline is not active\")"` | — |
| [SRC-EEF2E6447C-L000190](../../api/omarai.py#L190) | 190 | `"                remaining = deadline - time.monotonic()"` | — |
| [SRC-EEF2E6447C-L000191](../../api/omarai.py#L191) | 191 | `"                if remaining <= 0:"` | — |
| [SRC-EEF2E6447C-L000192](../../api/omarai.py#L192) | 192 | `"                    raise TimeoutError(\"absolute request-header deadline exceeded\")"` | — |
| [SRC-EEF2E6447C-L000193](../../api/omarai.py#L193) | 193 | `""` | — |
| [SRC-EEF2E6447C-L000194](../../api/omarai.py#L194) | 194 | `"                newline_index = self._buffer.find(b\"\\n\")"` | — |
| [SRC-EEF2E6447C-L000195](../../api/omarai.py#L195) | 195 | `"                if newline_index >= 0:"` | — |
| [SRC-EEF2E6447C-L000196](../../api/omarai.py#L196) | 196 | `"                    take = min(newline_index + 1, max_bytes - len(line))"` | — |
| [SRC-EEF2E6447C-L000197](../../api/omarai.py#L197) | 197 | `"                    line.extend(self._buffer[:take])"` | — |
| [SRC-EEF2E6447C-L000198](../../api/omarai.py#L198) | 198 | `"                    del self._buffer[:take]"` | — |
| [SRC-EEF2E6447C-L000199](../../api/omarai.py#L199) | 199 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000200](../../api/omarai.py#L200) | 200 | `""` | — |
| [SRC-EEF2E6447C-L000201](../../api/omarai.py#L201) | 201 | `"                if self._buffer:"` | — |
| [SRC-EEF2E6447C-L000202](../../api/omarai.py#L202) | 202 | `"                    take = min(len(self._buffer), max_bytes - len(line))"` | — |
| [SRC-EEF2E6447C-L000203](../../api/omarai.py#L203) | 203 | `"                    line.extend(self._buffer[:take])"` | — |
| [SRC-EEF2E6447C-L000204](../../api/omarai.py#L204) | 204 | `"                    del self._buffer[:take]"` | — |
| [SRC-EEF2E6447C-L000205](../../api/omarai.py#L205) | 205 | `"                    if len(line) >= max_bytes:"` | — |
| [SRC-EEF2E6447C-L000206](../../api/omarai.py#L206) | 206 | `"                        break"` | — |
| [SRC-EEF2E6447C-L000207](../../api/omarai.py#L207) | 207 | `""` | — |
| [SRC-EEF2E6447C-L000208](../../api/omarai.py#L208) | 208 | `"                remaining = deadline - time.monotonic()"` | — |
| [SRC-EEF2E6447C-L000209](../../api/omarai.py#L209) | 209 | `"                if remaining <= 0:"` | — |
| [SRC-EEF2E6447C-L000210](../../api/omarai.py#L210) | 210 | `"                    raise TimeoutError(\"absolute request-header deadline exceeded\")"` | — |
| [SRC-EEF2E6447C-L000211](../../api/omarai.py#L211) | 211 | `"                idle_timeout = max("` | — |
| [SRC-EEF2E6447C-L000212](../../api/omarai.py#L212) | 212 | `"                    0.1,"` | — |
| [SRC-EEF2E6447C-L000213](../../api/omarai.py#L213) | 213 | `"                    min("` | — |
| [SRC-EEF2E6447C-L000214](../../api/omarai.py#L214) | 214 | `"                        float(REQUEST_HEADER_IDLE_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000215](../../api/omarai.py#L215) | 215 | `"                        MAX_REQUEST_HEADER_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000216](../../api/omarai.py#L216) | 216 | `"                    ),"` | — |
| [SRC-EEF2E6447C-L000217](../../api/omarai.py#L217) | 217 | `"                )"` | — |
| [SRC-EEF2E6447C-L000218](../../api/omarai.py#L218) | 218 | `"                self.connection.settimeout(min(idle_timeout, remaining))"` | — |
| [SRC-EEF2E6447C-L000219](../../api/omarai.py#L219) | 219 | `"                chunk = self.connection.recv(min(4_096, max_bytes - len(line)))"` | — |
| [SRC-EEF2E6447C-L000220](../../api/omarai.py#L220) | 220 | `"                if not chunk:"` | — |
| [SRC-EEF2E6447C-L000221](../../api/omarai.py#L221) | 221 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000222](../../api/omarai.py#L222) | 222 | `"                self._buffer.extend(chunk)"` | — |
| [SRC-EEF2E6447C-L000223](../../api/omarai.py#L223) | 223 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000224](../../api/omarai.py#L224) | 224 | `"            try:"` | — |
| [SRC-EEF2E6447C-L000225](../../api/omarai.py#L225) | 225 | `"                self.connection.settimeout(previous_timeout)"` | — |
| [SRC-EEF2E6447C-L000226](../../api/omarai.py#L226) | 226 | `"            except OSError:"` | — |
