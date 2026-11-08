# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **021**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L006887 إلى SRC-EEF2E6447C-L000356
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L006887](../../agents/web_agent.py#L6887) | 6887 | `"                            review_warning = ("` | — |
| [SRC-1AE03B9EC3-L006888](../../agents/web_agent.py#L6888) | 6888 | `"                                \"استُنفدت ميزانية النماذج قبل إعادة تدقيق الإجابة المعدلة؛ \""` | — |
| [SRC-1AE03B9EC3-L006889](../../agents/web_agent.py#L6889) | 6889 | `"                                \"لذلك لن أعرض النص المعدل بوصفه إجابة مكتملة، وأعرض مقتطفات المصادر بدلًا منه.\""` | — |
| [SRC-1AE03B9EC3-L006890](../../agents/web_agent.py#L6890) | 6890 | `"                                if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L006891](../../agents/web_agent.py#L6891) | 6891 | `"                                else"` | — |
| [SRC-1AE03B9EC3-L006892](../../agents/web_agent.py#L6892) | 6892 | `"                                \"تعذرت إعادة تدقيق الإجابة المعدلة مقابل الأدلة؛ لذلك لن أعرضها بوصفها إجابة مكتملة، \""` | — |
| [SRC-1AE03B9EC3-L006893](../../agents/web_agent.py#L6893) | 6893 | `"                                \"وأعرض مقتطفات المصادر بدلًا منها.\""` | — |
| [SRC-1AE03B9EC3-L006894](../../agents/web_agent.py#L6894) | 6894 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L006895](../../agents/web_agent.py#L6895) | 6895 | `"                            answer = ("` | — |
| [SRC-1AE03B9EC3-L006896](../../agents/web_agent.py#L6896) | 6896 | `"                                _fallback_lead_answer(lead_evidence_sources)"` | — |
| [SRC-1AE03B9EC3-L006897](../../agents/web_agent.py#L6897) | 6897 | `"                                if lead_request and lead_evidence_sources"` | — |
| [SRC-1AE03B9EC3-L006898](../../agents/web_agent.py#L6898) | 6898 | `"                                else _fallback_answer(sources, review_warning)"` | — |
| [SRC-1AE03B9EC3-L006899](../../agents/web_agent.py#L6899) | 6899 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L006900](../../agents/web_agent.py#L6900) | 6900 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L006901](../../agents/web_agent.py#L6901) | 6901 | `"                        coverage_repair_status = \"no_change_gap_unresolved\""` | — |
| [SRC-1AE03B9EC3-L006902](../../agents/web_agent.py#L6902) | 6902 | `"                        coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L006903](../../agents/web_agent.py#L6903) | 6903 | `"                            \"رصد الفحص اللفظي محورًا قد يكون ناقصًا، لكن محاولة الإصلاح لم تغيّر الإجابة؛ \""` | — |
| [SRC-1AE03B9EC3-L006904](../../agents/web_agent.py#L6904) | 6904 | `"                            \"تحقق من تغطية هذا المحور يدويًا.\""` | — |
| [SRC-1AE03B9EC3-L006905](../../agents/web_agent.py#L6905) | 6905 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L006906](../../agents/web_agent.py#L6906) | 6906 | `"                except RequestBudgetExceeded:"` | — |
| [SRC-1AE03B9EC3-L006907](../../agents/web_agent.py#L6907) | 6907 | `"                    coverage_repair_status = \"budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L006908](../../agents/web_agent.py#L6908) | 6908 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L006909](../../agents/web_agent.py#L6909) | 6909 | `"                        \"استُنفدت ميزانية النماذج قبل محاولة إصلاح محور قد يكون ناقصًا؛ \""` | — |
| [SRC-1AE03B9EC3-L006910](../../agents/web_agent.py#L6910) | 6910 | `"                        \"لا تعتبر التغطية مكتملة دون مراجعة المحور المذكور.\""` | — |
| [SRC-1AE03B9EC3-L006911](../../agents/web_agent.py#L6911) | 6911 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L006912](../../agents/web_agent.py#L6912) | 6912 | `"                except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L006913](../../agents/web_agent.py#L6913) | 6913 | `"                    coverage_repair_status = \"unavailable\""` | — |
| [SRC-1AE03B9EC3-L006914](../../agents/web_agent.py#L6914) | 6914 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L006915](../../agents/web_agent.py#L6915) | 6915 | `"                        \"تعذرت محاولة إصلاح محور قد يكون ناقصًا (\""` | — |
| [SRC-1AE03B9EC3-L006916](../../agents/web_agent.py#L6916) | 6916 | `"                        + type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L006917](../../agents/web_agent.py#L6917) | 6917 | `"                        + \")؛ راجع المحاور المطلوبة قبل اعتماد الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L006918](../../agents/web_agent.py#L6918) | 6918 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L006919](../../agents/web_agent.py#L6919) | 6919 | `"        elif coverage_targets and review_status == \"model_claim_audit_completed\" and not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L006920](../../agents/web_agent.py#L6920) | 6920 | `"            coverage_repair_status = \"skipped_no_model_configuration\""` | — |
| [SRC-1AE03B9EC3-L006921](../../agents/web_agent.py#L6921) | 6921 | `"        elif coverage_targets:"` | — |
| [SRC-1AE03B9EC3-L006922](../../agents/web_agent.py#L6922) | 6922 | `"            coverage_repair_status = \"skipped_review_unavailable\""` | — |
| [SRC-1AE03B9EC3-L006923](../../agents/web_agent.py#L6923) | 6923 | `""` | — |
| [SRC-1AE03B9EC3-L006924](../../agents/web_agent.py#L6924) | 6924 | `"        if self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L006925](../../agents/web_agent.py#L6925) | 6925 | `"            answer += \"\\n\\nروابط إضافية من البحث المباشر عبر الويب:\""` | — |
| [SRC-1AE03B9EC3-L006926](../../agents/web_agent.py#L6926) | 6926 | `"            for source in self.server_search_sources[:8]:"` | — |
| [SRC-1AE03B9EC3-L006927](../../agents/web_agent.py#L6927) | 6927 | `"                answer += \"\\n- \" + source[\"title\"] + \" — \" + source[\"url\"]"` | — |
| [SRC-1AE03B9EC3-L006928](../../agents/web_agent.py#L6928) | 6928 | `"        max_citable_sources = min(MAX_LLM_CITED_SOURCES, len(sources))"` | — |
| [SRC-1AE03B9EC3-L006929](../../agents/web_agent.py#L6929) | 6929 | `"        answer, citation_warnings = self._remove_invalid_citations("` | — |
| [SRC-1AE03B9EC3-L006930](../../agents/web_agent.py#L6930) | 6930 | `"            answer, max_citable_sources"` | — |
| [SRC-1AE03B9EC3-L006931](../../agents/web_agent.py#L6931) | 6931 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006932](../../agents/web_agent.py#L6932) | 6932 | `"        citation_validation = self._citation_validation_metadata("` | — |
| [SRC-1AE03B9EC3-L006933](../../agents/web_agent.py#L6933) | 6933 | `"            answer, max_citable_sources, citation_warnings, review_status"` | — |
| [SRC-1AE03B9EC3-L006934](../../agents/web_agent.py#L6934) | 6934 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006935](../../agents/web_agent.py#L6935) | 6935 | `"        # Run deterministic numeric/provenance checks before asking the semantic reviewer."` | — |
| [SRC-1AE03B9EC3-L006936](../../agents/web_agent.py#L6936) | 6936 | `"        # Recompute below after a source-only fallback so public diagnostics describe the final text."` | — |
| [SRC-1AE03B9EC3-L006937](../../agents/web_agent.py#L6937) | 6937 | `"        answer_integrity = audit_answer_integrity("` | — |
| [SRC-1AE03B9EC3-L006938](../../agents/web_agent.py#L6938) | 6938 | `"            working_question, answer, sources, coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L006939](../../agents/web_agent.py#L6939) | 6939 | `"            plan.get(\"requirement_queries\")"` | — |
| [SRC-1AE03B9EC3-L006940](../../agents/web_agent.py#L6940) | 6940 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006941](../../agents/web_agent.py#L6941) | 6941 | `"        semantic_claim_verification: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L006942](../../agents/web_agent.py#L6942) | 6942 | `"            \"status\": \"not_run_review_unavailable\","` | — |
| [SRC-1AE03B9EC3-L006943](../../agents/web_agent.py#L6943) | 6943 | `"            \"withhold_answer\": False,"` | — |
| [SRC-1AE03B9EC3-L006944](../../agents/web_agent.py#L6944) | 6944 | `"            \"semantic_verification\": \"not_performed\","` | — |
| [SRC-1AE03B9EC3-L006945](../../agents/web_agent.py#L6945) | 6945 | `"            \"fact_correctness\": \"not_verified\","` | — |
| [SRC-1AE03B9EC3-L006946](../../agents/web_agent.py#L6946) | 6946 | `"        }"` | — |
| [SRC-1AE03B9EC3-L006947](../../agents/web_agent.py#L6947) | 6947 | `"        semantic_answer_withheld = False"` | — |
| [SRC-1AE03B9EC3-L006948](../../agents/web_agent.py#L6948) | 6948 | `"        if used_llm and sources and review_status == \"model_claim_audit_completed\":"` | — |
| [SRC-1AE03B9EC3-L006949](../../agents/web_agent.py#L6949) | 6949 | `"            if citation_warnings:"` | — |
| [SRC-1AE03B9EC3-L006950](../../agents/web_agent.py#L6950) | 6950 | `"                semantic_claim_verification = {"` | — |
| [SRC-1AE03B9EC3-L006951](../../agents/web_agent.py#L6951) | 6951 | `"                    \"status\": \"not_verifiable\","` | — |
| [SRC-1AE03B9EC3-L006952](../../agents/web_agent.py#L6952) | 6952 | `"                    \"withhold_answer\": True,"` | — |
| [SRC-1AE03B9EC3-L006953](../../agents/web_agent.py#L6953) | 6953 | `"                    \"reason\": \"invalid_citation_references_were_removed\","` | — |
| [SRC-1AE03B9EC3-L006954](../../agents/web_agent.py#L6954) | 6954 | `"                    \"semantic_verification\": \"not_completed\","` | — |
| [SRC-1AE03B9EC3-L006955](../../agents/web_agent.py#L6955) | 6955 | `"                    \"fact_correctness\": \"not_verified\","` | — |
| [SRC-1AE03B9EC3-L006956](../../agents/web_agent.py#L6956) | 6956 | `"                }"` | — |
| [SRC-1AE03B9EC3-L006957](../../agents/web_agent.py#L6957) | 6957 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L006958](../../agents/web_agent.py#L6958) | 6958 | `"                semantic_claim_verification = self._verify_semantic_claims("` | — |
| [SRC-1AE03B9EC3-L006959](../../agents/web_agent.py#L6959) | 6959 | `"                    working_question, answer, sources, answer_integrity"` | — |
| [SRC-1AE03B9EC3-L006960](../../agents/web_agent.py#L6960) | 6960 | `"                )"` | — |
| [SRC-1AE03B9EC3-L006961](../../agents/web_agent.py#L6961) | 6961 | `"            if semantic_claim_verification.get(\"status\") not in {"` | — |
| [SRC-1AE03B9EC3-L006962](../../agents/web_agent.py#L6962) | 6962 | `"                \"completed_all_claims_supported\","` | — |
| [SRC-1AE03B9EC3-L006963](../../agents/web_agent.py#L6963) | 6963 | `"                \"completed_no_factual_claims\","` | — |
| [SRC-1AE03B9EC3-L006964](../../agents/web_agent.py#L6964) | 6964 | `"            }:"` | — |
| [SRC-1AE03B9EC3-L006965](../../agents/web_agent.py#L6965) | 6965 | `"                semantic_answer_withheld = True"` | — |
| [SRC-1AE03B9EC3-L006966](../../agents/web_agent.py#L6966) | 6966 | `"                semantic_warning = ("` | — |
| [SRC-1AE03B9EC3-L006967](../../agents/web_agent.py#L6967) | 6967 | `"                    \"حُجبت صياغة النموذج لأن مراجع دعم الادعاءات لم يستطع إثبات دعم \""` | — |
| [SRC-1AE03B9EC3-L006968](../../agents/web_agent.py#L6968) | 6968 | `"                    \"كل ادعاء واقعي بمصدره المحدد دون تعارض. المقتطفات أدناه مواد مصدرية \""` | — |
| [SRC-1AE03B9EC3-L006969](../../agents/web_agent.py#L6969) | 6969 | `"                    \"للمراجعة وليست إجابة متحققة.\""` | — |
| [SRC-1AE03B9EC3-L006970](../../agents/web_agent.py#L6970) | 6970 | `"                )"` | — |
| [SRC-1AE03B9EC3-L006971](../../agents/web_agent.py#L6971) | 6971 | `"                answer = ("` | — |
| [SRC-1AE03B9EC3-L006972](../../agents/web_agent.py#L6972) | 6972 | `"                    _fallback_lead_answer(lead_evidence_sources)"` | — |
| [SRC-1AE03B9EC3-L006973](../../agents/web_agent.py#L6973) | 6973 | `"                    if lead_request and lead_evidence_sources"` | — |
| [SRC-1AE03B9EC3-L006974](../../agents/web_agent.py#L6974) | 6974 | `"                    else _fallback_answer(sources, semantic_warning)"` | — |
| [SRC-1AE03B9EC3-L006975](../../agents/web_agent.py#L6975) | 6975 | `"                )"` | — |
| [SRC-1AE03B9EC3-L006976](../../agents/web_agent.py#L6976) | 6976 | `"                answer, fallback_citation_warnings = self._remove_invalid_citations("` | — |
| [SRC-1AE03B9EC3-L006977](../../agents/web_agent.py#L6977) | 6977 | `"                    answer, max_citable_sources"` | — |
| [SRC-1AE03B9EC3-L006978](../../agents/web_agent.py#L6978) | 6978 | `"                )"` | — |
| [SRC-1AE03B9EC3-L006979](../../agents/web_agent.py#L6979) | 6979 | `"                citation_warnings = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L006980](../../agents/web_agent.py#L6980) | 6980 | `"                    citation_warnings + fallback_citation_warnings"` | — |
| [SRC-1AE03B9EC3-L006981](../../agents/web_agent.py#L6981) | 6981 | `"                ))"` | — |
| [SRC-1AE03B9EC3-L006982](../../agents/web_agent.py#L6982) | 6982 | `"                citation_validation = self._citation_validation_metadata("` | — |
| [SRC-1AE03B9EC3-L006983](../../agents/web_agent.py#L6983) | 6983 | `"                    answer, max_citable_sources, citation_warnings, review_status"` | — |
| [SRC-1AE03B9EC3-L006984](../../agents/web_agent.py#L6984) | 6984 | `"                )"` | — |
| [SRC-1AE03B9EC3-L006985](../../agents/web_agent.py#L6985) | 6985 | `"        report[\"semantic_claim_verification\"] = semantic_claim_verification"` | — |
| [SRC-1AE03B9EC3-L006986](../../agents/web_agent.py#L6986) | 6986 | `"        report[\"answer_was_withheld\"] = semantic_answer_withheld"` | — |
| [SRC-1AE03B9EC3-L006987](../../agents/web_agent.py#L6987) | 6987 | `"        report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L006988](../../agents/web_agent.py#L6988) | 6988 | `"        report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L006989](../../agents/web_agent.py#L6989) | 6989 | `"        report[\"second_pass_review\"] = review_status"` | — |
| [SRC-1AE03B9EC3-L006990](../../agents/web_agent.py#L6990) | 6990 | `"        report[\"claim_audit\"] = review_status"` | — |
| [SRC-1AE03B9EC3-L006991](../../agents/web_agent.py#L6991) | 6991 | `"        answer_coverage = {"` | — |
| [SRC-1AE03B9EC3-L006992](../../agents/web_agent.py#L6992) | 6992 | `"            \"method\": \"explicit_criteria_heuristic\","` | — |
| [SRC-1AE03B9EC3-L006993](../../agents/web_agent.py#L6993) | 6993 | `"            \"targets\": coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L006994](../../agents/web_agent.py#L6994) | 6994 | `"            \"review_prompted\": review_status == \"model_claim_audit_completed\","` | — |
| [SRC-1AE03B9EC3-L006995](../../agents/web_agent.py#L6995) | 6995 | `"            \"status\": ("` | — |
| [SRC-1AE03B9EC3-L006996](../../agents/web_agent.py#L6996) | 6996 | `"                \"model_review_requested_not_machine_verified\""` | — |
| [SRC-1AE03B9EC3-L006997](../../agents/web_agent.py#L6997) | 6997 | `"                if coverage_targets and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006998](../../agents/web_agent.py#L6998) | 6998 | `"                else \"review_unavailable\""` | — |
| [SRC-1AE03B9EC3-L006999](../../agents/web_agent.py#L6999) | 6999 | `"                if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L007000](../../agents/web_agent.py#L7000) | 7000 | `"                else \"no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L007001](../../agents/web_agent.py#L7001) | 7001 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L007002](../../agents/web_agent.py#L7002) | 7002 | `"            \"automatically_graded\": False,"` | — |
| [SRC-1AE03B9EC3-L007003](../../agents/web_agent.py#L7003) | 7003 | `"        }"` | — |
| [SRC-1AE03B9EC3-L007004](../../agents/web_agent.py#L7004) | 7004 | `"        report[\"answer_coverage\"] = answer_coverage"` | — |
| [SRC-1AE03B9EC3-L007005](../../agents/web_agent.py#L7005) | 7005 | `"        report[\"coverage_repair_status\"] = coverage_repair_status"` | — |
| [SRC-1AE03B9EC3-L007006](../../agents/web_agent.py#L7006) | 7006 | `"        report[\"coverage_repair_warning\"] = coverage_repair_warning"` | — |
| [SRC-1AE03B9EC3-L007007](../../agents/web_agent.py#L7007) | 7007 | `"        answer_integrity = audit_answer_integrity(working_question, answer, sources, coverage_targets, plan.get(\"requirement_queries\"))"` | — |
| [SRC-1AE03B9EC3-L007008](../../agents/web_agent.py#L7008) | 7008 | `"        if semantic_answer_withheld:"` | — |
| [SRC-1AE03B9EC3-L007009](../../agents/web_agent.py#L7009) | 7009 | `"            answer_coverage[\"status\"] = \"semantic_support_unverified_answer_withheld\""` | — |
| [SRC-1AE03B9EC3-L007010](../../agents/web_agent.py#L7010) | 7010 | `"            answer_coverage[\"semantic_verification_status\"] = semantic_claim_verification.get(\"status\")"` | — |
| [SRC-1AE03B9EC3-L007011](../../agents/web_agent.py#L7011) | 7011 | `"        answer_coverage[\"target_checks\"] = answer_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L007012](../../agents/web_agent.py#L7012) | 7012 | `"        answer_coverage[\"potentially_missing_target_count\"] = answer_integrity[\"potentially_missing_target_count\"]"` | — |
| [SRC-1AE03B9EC3-L007013](../../agents/web_agent.py#L7013) | 7013 | `"        answer_coverage[\"source_evidence_gap_count\"] = answer_integrity[\"source_evidence_gap_count\"]"` | — |
| [SRC-1AE03B9EC3-L007014](../../agents/web_agent.py#L7014) | 7014 | `"        answer_coverage[\"lexical_screen_method\"] = \"deterministic_lexical_screen_only_not_semantic_grading\""` | — |
| [SRC-1AE03B9EC3-L007015](../../agents/web_agent.py#L7015) | 7015 | `"        requirements_without_candidates = int("` | — |
| [SRC-1AE03B9EC3-L007016](../../agents/web_agent.py#L7016) | 7016 | `"            answer_integrity.get(\"requirements_without_candidate_evidence_count\", 0) or 0"` | — |
| [SRC-1AE03B9EC3-L007017](../../agents/web_agent.py#L7017) | 7017 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007018](../../agents/web_agent.py#L7018) | 7018 | `"        task_fulfillment_status = ("` | — |
| [SRC-1AE03B9EC3-L007019](../../agents/web_agent.py#L7019) | 7019 | `"            \"possible_gap_detected\""` | — |
| [SRC-1AE03B9EC3-L007020](../../agents/web_agent.py#L7020) | 7020 | `"            if ("` | — |
| [SRC-1AE03B9EC3-L007021](../../agents/web_agent.py#L7021) | 7021 | `"                answer_integrity[\"potentially_missing_target_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L007022](../../agents/web_agent.py#L7022) | 7022 | `"                or answer_integrity[\"source_evidence_gap_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L007023](../../agents/web_agent.py#L7023) | 7023 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007024](../../agents/web_agent.py#L7024) | 7024 | `"            else \"candidate_evidence_gaps_or_linkage_unknown\""` | — |
| [SRC-1AE03B9EC3-L007025](../../agents/web_agent.py#L7025) | 7025 | `"            if coverage_targets and requirements_without_candidates > 0"` | — |
| [SRC-1AE03B9EC3-L007026](../../agents/web_agent.py#L7026) | 7026 | `"            else \"lexical_signals_found_not_semantically_verified\" if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L007027](../../agents/web_agent.py#L7027) | 7027 | `"            else \"not_machine_assessed_no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L007028](../../agents/web_agent.py#L7028) | 7028 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007029](../../agents/web_agent.py#L7029) | 7029 | `"        if semantic_answer_withheld:"` | — |
| [SRC-1AE03B9EC3-L007030](../../agents/web_agent.py#L7030) | 7030 | `"            task_fulfillment_status = \"not_assessed_insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L007031](../../agents/web_agent.py#L7031) | 7031 | `"        answer_coverage[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L007032](../../agents/web_agent.py#L7032) | 7032 | `"        answer_coverage[\"semantic_verification_status\"] = semantic_claim_verification.get(\"status\")"` | — |
| [SRC-1AE03B9EC3-L007033](../../agents/web_agent.py#L7033) | 7033 | `"        report[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L007034](../../agents/web_agent.py#L7034) | 7034 | `"        report[\"answer_integrity\"] = answer_integrity"` | — |
| [SRC-1AE03B9EC3-L007035](../../agents/web_agent.py#L7035) | 7035 | `"        report[\"requirement_evidence\"] = answer_integrity.get(\"requirement_evidence\", [])"` | — |
| [SRC-1AE03B9EC3-L007036](../../agents/web_agent.py#L7036) | 7036 | `"        report[\"connector_summary\"] = self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L007037](../../agents/web_agent.py#L7037) | 7037 | `"            list(self._provider_diagnostics), sources"` | — |
| [SRC-1AE03B9EC3-L007038](../../agents/web_agent.py#L7038) | 7038 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007039](../../agents/web_agent.py#L7039) | 7039 | `"        report[\"provider_diagnostics\"] = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L007040](../../agents/web_agent.py#L7040) | 7040 | `"        distinct_providers = {"` | — |
| [SRC-1AE03B9EC3-L007041](../../agents/web_agent.py#L7041) | 7041 | `"            provider for source in sources for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L007042](../../agents/web_agent.py#L7042) | 7042 | `"        }"` | — |
| [SRC-1AE03B9EC3-L007043](../../agents/web_agent.py#L7043) | 7043 | `"        distinct_domains = {"` | — |
| [SRC-1AE03B9EC3-L007044](../../agents/web_agent.py#L7044) | 7044 | `"            registrable_domain("` | — |
| [SRC-1AE03B9EC3-L007045](../../agents/web_agent.py#L7045) | 7045 | `"                source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L007046](../../agents/web_agent.py#L7046) | 7046 | `"                or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L007047](../../agents/web_agent.py#L7047) | 7047 | `"                or \"\""` | — |
| [SRC-1AE03B9EC3-L007048](../../agents/web_agent.py#L7048) | 7048 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007049](../../agents/web_agent.py#L7049) | 7049 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L007050](../../agents/web_agent.py#L7050) | 7050 | `"        }"` | — |
| [SRC-1AE03B9EC3-L007051](../../agents/web_agent.py#L7051) | 7051 | `"        distinct_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L007052](../../agents/web_agent.py#L7052) | 7052 | `"        fetched_pages = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L007053](../../agents/web_agent.py#L7053) | 7053 | `"        if semantic_answer_withheld:"` | — |
| [SRC-1AE03B9EC3-L007054](../../agents/web_agent.py#L7054) | 7054 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L007055](../../agents/web_agent.py#L7055) | 7055 | `"        elif ("` | — |
| [SRC-1AE03B9EC3-L007056](../../agents/web_agent.py#L7056) | 7056 | `"            len(sources) >= 4 and len(distinct_domains) >= 3"` | — |
| [SRC-1AE03B9EC3-L007057](../../agents/web_agent.py#L7057) | 7057 | `"            and len(distinct_providers) >= 2 and fetched_pages >= 1"` | — |
| [SRC-1AE03B9EC3-L007058](../../agents/web_agent.py#L7058) | 7058 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L007059](../../agents/web_agent.py#L7059) | 7059 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L007060](../../agents/web_agent.py#L7060) | 7060 | `"            research_quality = \"excellent\""` | — |
| [SRC-1AE03B9EC3-L007061](../../agents/web_agent.py#L7061) | 7061 | `"        elif ("` | — |
| [SRC-1AE03B9EC3-L007062](../../agents/web_agent.py#L7062) | 7062 | `"            len(sources) >= 2 and len(distinct_domains) >= 2"` | — |
| [SRC-1AE03B9EC3-L007063](../../agents/web_agent.py#L7063) | 7063 | `"            and (len(distinct_providers) >= 2 or fetched_pages >= 1)"` | — |
| [SRC-1AE03B9EC3-L007064](../../agents/web_agent.py#L7064) | 7064 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L007065](../../agents/web_agent.py#L7065) | 7065 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L007066](../../agents/web_agent.py#L7066) | 7066 | `"            research_quality = \"good\""` | — |
| [SRC-1AE03B9EC3-L007067](../../agents/web_agent.py#L7067) | 7067 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L007068](../../agents/web_agent.py#L7068) | 7068 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L007069](../../agents/web_agent.py#L7069) | 7069 | `""` | — |
| [SRC-1AE03B9EC3-L007070](../../agents/web_agent.py#L7070) | 7070 | `"        # Source breadth and a completed model-assisted review do not justify a"` | — |
| [SRC-1AE03B9EC3-L007071](../../agents/web_agent.py#L7071) | 7071 | `"        # positive research-quality label if the final answer has no valid source"` | — |
| [SRC-1AE03B9EC3-L007072](../../agents/web_agent.py#L7072) | 7072 | `"        # citation markers. This is a deterministic presentation guard, not a"` | — |
| [SRC-1AE03B9EC3-L007073](../../agents/web_agent.py#L7073) | 7073 | `"        # semantic entailment check."` | — |
| [SRC-1AE03B9EC3-L007074](../../agents/web_agent.py#L7074) | 7074 | `"        uncited_reviewed_answer = ("` | — |
| [SRC-1AE03B9EC3-L007075](../../agents/web_agent.py#L7075) | 7075 | `"            used_llm"` | — |
| [SRC-1AE03B9EC3-L007076](../../agents/web_agent.py#L7076) | 7076 | `"            and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L007077](../../agents/web_agent.py#L7077) | 7077 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L007078](../../agents/web_agent.py#L7078) | 7078 | `"            and citation_validation[\"valid_citation_count\"] == 0"` | — |
| [SRC-1AE03B9EC3-L007079](../../agents/web_agent.py#L7079) | 7079 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007080](../../agents/web_agent.py#L7080) | 7080 | `"        if uncited_reviewed_answer:"` | — |
| [SRC-1AE03B9EC3-L007081](../../agents/web_agent.py#L7081) | 7081 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L007082](../../agents/web_agent.py#L7082) | 7082 | `"            citation_validation[\"claim_support\"] = \"not_established_no_valid_source_citations\""` | — |
| [SRC-1AE03B9EC3-L007083](../../agents/web_agent.py#L7083) | 7083 | `"            answer_evidence_status = \"reviewed_answer_has_no_valid_citations\""` | — |
| [SRC-1AE03B9EC3-L007084](../../agents/web_agent.py#L7084) | 7084 | `"            uncited_answer_warning = ("` | — |
| [SRC-1AE03B9EC3-L007085](../../agents/web_agent.py#L7085) | 7085 | `"                \"اكتملت مراجعة النموذج، لكن الإجابة النهائية لا تحتوي على إحالات صالحة \""` | — |
| [SRC-1AE03B9EC3-L007086](../../agents/web_agent.py#L7086) | 7086 | `"                \"إلى قائمة المصادر؛ لذلك صُنّفت جودة البحث «جزئية». وجود المصادر أو \""` | — |
| [SRC-1AE03B9EC3-L007087](../../agents/web_agent.py#L7087) | 7087 | `"                \"اكتمال مراجعة النموذج لا يثبت دعم كل ادعاء.\""` | — |
| [SRC-1AE03B9EC3-L007088](../../agents/web_agent.py#L7088) | 7088 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007089](../../agents/web_agent.py#L7089) | 7089 | `"        elif citation_validation[\"valid_citation_count\"] > 0:"` | — |
| [SRC-1AE03B9EC3-L007090](../../agents/web_agent.py#L7090) | 7090 | `"            answer_evidence_status = ("` | — |
| [SRC-1AE03B9EC3-L007091](../../agents/web_agent.py#L7091) | 7091 | `"                \"semantic_support_unverified_answer_withheld\""` | — |
| [SRC-1AE03B9EC3-L007092](../../agents/web_agent.py#L7092) | 7092 | `"                if semantic_answer_withheld else \"citation_indices_validated_only\""` | — |
| [SRC-1AE03B9EC3-L007093](../../agents/web_agent.py#L7093) | 7093 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007094](../../agents/web_agent.py#L7094) | 7094 | `"            uncited_answer_warning = None"` | — |
| [SRC-1AE03B9EC3-L007095](../../agents/web_agent.py#L7095) | 7095 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L007096](../../agents/web_agent.py#L7096) | 7096 | `"            answer_evidence_status = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L007097](../../agents/web_agent.py#L7097) | 7097 | `"            uncited_answer_warning = None"` | — |
| [SRC-1AE03B9EC3-L007098](../../agents/web_agent.py#L7098) | 7098 | `""` | — |
| [SRC-1AE03B9EC3-L007099](../../agents/web_agent.py#L7099) | 7099 | `"        search_attempted = search_attempted or bool(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L007100](../../agents/web_agent.py#L7100) | 7100 | `"        report[\"search_attempted\"] = search_attempted"` | — |
| [SRC-1AE03B9EC3-L007101](../../agents/web_agent.py#L7101) | 7101 | `"        prior_search_outcome = report.get(\"search_outcome\")"` | — |
| [SRC-1AE03B9EC3-L007102](../../agents/web_agent.py#L7102) | 7102 | `"        if prior_search_outcome in _RESEARCH_ERROR_OUTCOMES and not sources:"` | — |
| [SRC-1AE03B9EC3-L007103](../../agents/web_agent.py#L7103) | 7103 | `"            # Preserve a known pipeline failure instead of relabeling it as an ordinary"` | — |
| [SRC-1AE03B9EC3-L007104](../../agents/web_agent.py#L7104) | 7104 | `"            # zero-result search merely because the outer request reached its return path."` | — |
| [SRC-1AE03B9EC3-L007105](../../agents/web_agent.py#L7105) | 7105 | `"            report[\"search_outcome\"] = prior_search_outcome"` | — |
| [SRC-1AE03B9EC3-L007106](../../agents/web_agent.py#L7106) | 7106 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L007107](../../agents/web_agent.py#L7107) | 7107 | `"            report[\"search_outcome\"] = ("` | — |
| [SRC-1AE03B9EC3-L007108](../../agents/web_agent.py#L7108) | 7108 | `"                \"attempted_with_usable_sources\" if search_attempted and sources"` | — |
| [SRC-1AE03B9EC3-L007109](../../agents/web_agent.py#L7109) | 7109 | `"                else \"attempted_no_usable_sources\" if search_attempted"` | — |
| [SRC-1AE03B9EC3-L007110](../../agents/web_agent.py#L7110) | 7110 | `"                else \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L007111](../../agents/web_agent.py#L7111) | 7111 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007112](../../agents/web_agent.py#L7112) | 7112 | `"        report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L007113](../../agents/web_agent.py#L7113) | 7113 | `"        report[\"research_quality\"] = research_quality"` | — |
| [SRC-1AE03B9EC3-L007114](../../agents/web_agent.py#L7114) | 7114 | `"        report[\"research_quality_semantics\"] = \"process_coverage_not_factual_probability\""` | — |
| [SRC-1AE03B9EC3-L007115](../../agents/web_agent.py#L7115) | 7115 | `"        report[\"answer_evidence_status\"] = answer_evidence_status"` | — |
| [SRC-1AE03B9EC3-L007116](../../agents/web_agent.py#L7116) | 7116 | `"        report[\"distinct_registrable_domains\"] = len(distinct_domains)"` | — |
| [SRC-1AE03B9EC3-L007117](../../agents/web_agent.py#L7117) | 7117 | `"        report[\"independent_sources\"] = len(distinct_domains)  # Legacy alias; not editorial independence."` | — |
| [SRC-1AE03B9EC3-L007118](../../agents/web_agent.py#L7118) | 7118 | `"        report[\"independent_sources_field_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L007119](../../agents/web_agent.py#L7119) | 7119 | `"            \"legacy_compatibility_alias_for_distinct_registrable_domain_count\""` | — |
| [SRC-1AE03B9EC3-L007120](../../agents/web_agent.py#L7120) | 7120 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007121](../../agents/web_agent.py#L7121) | 7121 | `"        report[\"source_diversity_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L007122](../../agents/web_agent.py#L7122) | 7122 | `"            \"distinct_registrable_domains_not_editorial_independence\""` | — |
| [SRC-1AE03B9EC3-L007123](../../agents/web_agent.py#L7123) | 7123 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007124](../../agents/web_agent.py#L7124) | 7124 | `"        report[\"editorial_independence_status\"] = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L007125](../../agents/web_agent.py#L7125) | 7125 | `"        report[\"claim_audit_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L007126](../../agents/web_agent.py#L7126) | 7126 | `"            \"distinct_model_assessed_source_support_not_ground_truth\""` | — |
| [SRC-1AE03B9EC3-L007127](../../agents/web_agent.py#L7127) | 7127 | `"            if semantic_claim_verification.get(\"status\") in {"` | — |
| [SRC-1AE03B9EC3-L007128](../../agents/web_agent.py#L7128) | 7128 | `"                \"completed_all_claims_supported\", \"completed_no_factual_claims\""` | — |
| [SRC-1AE03B9EC3-L007129](../../agents/web_agent.py#L7129) | 7129 | `"            }"` | — |
| [SRC-1AE03B9EC3-L007130](../../agents/web_agent.py#L7130) | 7130 | `"            else \"not_verified\""` | — |
| [SRC-1AE03B9EC3-L007131](../../agents/web_agent.py#L7131) | 7131 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007132](../../agents/web_agent.py#L7132) | 7132 | `"        report[\"insufficient_evidence\"] = bool("` | — |
| [SRC-1AE03B9EC3-L007133](../../agents/web_agent.py#L7133) | 7133 | `"            report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES"` | — |
| [SRC-1AE03B9EC3-L007134](../../agents/web_agent.py#L7134) | 7134 | `"            or not sources"` | — |
| [SRC-1AE03B9EC3-L007135](../../agents/web_agent.py#L7135) | 7135 | `"            or semantic_answer_withheld"` | — |
| [SRC-1AE03B9EC3-L007136](../../agents/web_agent.py#L7136) | 7136 | `"            or answer_integrity[\"source_evidence_gap_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L007137](../../agents/web_agent.py#L7137) | 7137 | `"            or ("` | — |
| [SRC-1AE03B9EC3-L007138](../../agents/web_agent.py#L7138) | 7138 | `"                bool(coverage_targets)"` | — |
| [SRC-1AE03B9EC3-L007139](../../agents/web_agent.py#L7139) | 7139 | `"                and answer_integrity[\"potentially_missing_target_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L007140](../../agents/web_agent.py#L7140) | 7140 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007141](../../agents/web_agent.py#L7141) | 7141 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007142](../../agents/web_agent.py#L7142) | 7142 | `"        report[\"valid_citation_range\"] = [1, max_citable_sources] if max_citable_sources else []"` | — |
| [SRC-1AE03B9EC3-L007143](../../agents/web_agent.py#L7143) | 7143 | `"        report[\"citation_count\"] = citation_validation[\"valid_citation_count\"]"` | — |
| [SRC-1AE03B9EC3-L007144](../../agents/web_agent.py#L7144) | 7144 | `"        report[\"citation_check\"] = citation_validation[\"status\"]"` | — |
| [SRC-1AE03B9EC3-L007145](../../agents/web_agent.py#L7145) | 7145 | `"        report[\"citation_validation\"] = citation_validation"` | — |
| [SRC-1AE03B9EC3-L007146](../../agents/web_agent.py#L7146) | 7146 | `"        warnings = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L007147](../../agents/web_agent.py#L7147) | 7147 | `"            search_warnings"` | — |
| [SRC-1AE03B9EC3-L007148](../../agents/web_agent.py#L7148) | 7148 | `"            + ([llm_warning] if llm_warning else [])"` | — |
| [SRC-1AE03B9EC3-L007149](../../agents/web_agent.py#L7149) | 7149 | `"            + ([review_warning] if review_warning else [])"` | — |
| [SRC-1AE03B9EC3-L007150](../../agents/web_agent.py#L7150) | 7150 | `"            + ([coverage_repair_warning] if coverage_repair_warning else [])"` | — |
| [SRC-1AE03B9EC3-L007151](../../agents/web_agent.py#L7151) | 7151 | `"            + citation_warnings"` | — |
| [SRC-1AE03B9EC3-L007152](../../agents/web_agent.py#L7152) | 7152 | `"            + ([uncited_answer_warning] if uncited_answer_warning else [])"` | — |
| [SRC-1AE03B9EC3-L007153](../../agents/web_agent.py#L7153) | 7153 | `"            + (["` | — |
| [SRC-1AE03B9EC3-L007154](../../agents/web_agent.py#L7154) | 7154 | `"                \"حُجبت الإجابة المولدة لعدم اكتمال التحقق الدلالي المستقل عن نموذج الصياغة.\""` | — |
| [SRC-1AE03B9EC3-L007155](../../agents/web_agent.py#L7155) | 7155 | `"            ] if semantic_answer_withheld else [])"` | — |
| [SRC-1AE03B9EC3-L007156](../../agents/web_agent.py#L7156) | 7156 | `"        ))"` | — |
| [SRC-1AE03B9EC3-L007157](../../agents/web_agent.py#L7157) | 7157 | `"        report[\"model_calls\"] = list(self.model_usage)"` | — |
| [SRC-1AE03B9EC3-L007158](../../agents/web_agent.py#L7158) | 7158 | `"        report[\"openrouter_web_search_enabled\"] = self.openrouter_web_search_enabled"` | — |
| [SRC-1AE03B9EC3-L007159](../../agents/web_agent.py#L7159) | 7159 | `"        report[\"openrouter_web_search_results\"] = len(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L007160](../../agents/web_agent.py#L7160) | 7160 | `"        if semantic_answer_withheld:"` | — |
| [SRC-1AE03B9EC3-L007161](../../agents/web_agent.py#L7161) | 7161 | `"            final_answer_status = \"semantic_verification_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L007162](../../agents/web_agent.py#L7162) | 7162 | `"        elif generation_budget_exhausted or review_budget_exhausted:"` | — |
| [SRC-1AE03B9EC3-L007163](../../agents/web_agent.py#L7163) | 7163 | `"            final_answer_status = \"budget_exhausted_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L007164](../../agents/web_agent.py#L7164) | 7164 | `"        elif llm_warning:"` | — |
| [SRC-1AE03B9EC3-L007165](../../agents/web_agent.py#L7165) | 7165 | `"            final_answer_status = ("` | — |
| [SRC-1AE03B9EC3-L007166](../../agents/web_agent.py#L7166) | 7166 | `"                \"model_not_configured_fallback\""` | — |
| [SRC-1AE03B9EC3-L007167](../../agents/web_agent.py#L7167) | 7167 | `"                if not self.api_key"` | — |
| [SRC-1AE03B9EC3-L007168](../../agents/web_agent.py#L7168) | 7168 | `"                else \"generation_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L007169](../../agents/web_agent.py#L7169) | 7169 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007170](../../agents/web_agent.py#L7170) | 7170 | `"        elif review_warning:"` | — |
| [SRC-1AE03B9EC3-L007171](../../agents/web_agent.py#L7171) | 7171 | `"            final_answer_status = \"review_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L007172](../../agents/web_agent.py#L7172) | 7172 | `"        elif coverage_repair_status == \"no_change_gap_unresolved\":"` | — |
| [SRC-1AE03B9EC3-L007173](../../agents/web_agent.py#L7173) | 7173 | `"            final_answer_status = \"coverage_repair_left_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L007174](../../agents/web_agent.py#L7174) | 7174 | `"        elif coverage_repair_status == \"budget_exhausted\":"` | — |
| [SRC-1AE03B9EC3-L007175](../../agents/web_agent.py#L7175) | 7175 | `"            final_answer_status = \"coverage_repair_budget_exhausted_with_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L007176](../../agents/web_agent.py#L7176) | 7176 | `"        elif coverage_repair_status == \"unavailable\":"` | — |
| [SRC-1AE03B9EC3-L007177](../../agents/web_agent.py#L7177) | 7177 | `"            final_answer_status = \"coverage_repair_unavailable_with_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L007178](../../agents/web_agent.py#L7178) | 7178 | `"        elif used_llm:"` | — |
| [SRC-1AE03B9EC3-L007179](../../agents/web_agent.py#L7179) | 7179 | `"            final_answer_status = \"model_answer_generated\""` | — |
| [SRC-1AE03B9EC3-L007180](../../agents/web_agent.py#L7180) | 7180 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L007181](../../agents/web_agent.py#L7181) | 7181 | `"            final_answer_status = \"source_fallback\""` | — |
| [SRC-1AE03B9EC3-L007182](../../agents/web_agent.py#L7182) | 7182 | `""` | — |
| [SRC-1AE03B9EC3-L007183](../../agents/web_agent.py#L7183) | 7183 | `"        # Report pipeline completion separately from factual correctness. A successful"` | — |
| [SRC-1AE03B9EC3-L007184](../../agents/web_agent.py#L7184) | 7184 | `"        # retrieval or model review is not an independent semantic fact check."` | — |
| [SRC-1AE03B9EC3-L007185](../../agents/web_agent.py#L7185) | 7185 | `"        if report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES:"` | — |
| [SRC-1AE03B9EC3-L007186](../../agents/web_agent.py#L7186) | 7186 | `"            pipeline_completion_status = \"execution_failed\""` | — |
| [SRC-1AE03B9EC3-L007187](../../agents/web_agent.py#L7187) | 7187 | `"        elif not search_attempted:"` | — |
| [SRC-1AE03B9EC3-L007188](../../agents/web_agent.py#L7188) | 7188 | `"            pipeline_completion_status = \"not_verified\""` | — |
| [SRC-1AE03B9EC3-L007189](../../agents/web_agent.py#L7189) | 7189 | `"        elif not sources:"` | — |
| [SRC-1AE03B9EC3-L007190](../../agents/web_agent.py#L7190) | 7190 | `"            pipeline_completion_status = \"insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L007191](../../agents/web_agent.py#L7191) | 7191 | `"        elif ("` | — |
| [SRC-1AE03B9EC3-L007192](../../agents/web_agent.py#L7192) | 7192 | `"            llm_warning"` | — |
| [SRC-1AE03B9EC3-L007193](../../agents/web_agent.py#L7193) | 7193 | `"            or review_warning"` | — |
| [SRC-1AE03B9EC3-L007194](../../agents/web_agent.py#L7194) | 7194 | `"            or review_status != \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L007195](../../agents/web_agent.py#L7195) | 7195 | `"            or answer_integrity[\"potentially_missing_target_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L007196](../../agents/web_agent.py#L7196) | 7196 | `"            or answer_integrity[\"source_evidence_gap_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L007197](../../agents/web_agent.py#L7197) | 7197 | `"            or citation_validation[\"valid_citation_count\"] == 0"` | — |
| [SRC-1AE03B9EC3-L007198](../../agents/web_agent.py#L7198) | 7198 | `"            or semantic_answer_withheld"` | — |
| [SRC-1AE03B9EC3-L007199](../../agents/web_agent.py#L7199) | 7199 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L007200](../../agents/web_agent.py#L7200) | 7200 | `"            pipeline_completion_status = \"partial\""` | — |
| [SRC-1AE03B9EC3-L007201](../../agents/web_agent.py#L7201) | 7201 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L007202](../../agents/web_agent.py#L7202) | 7202 | `"            pipeline_completion_status = \"completed\""` | — |
| [SRC-1AE03B9EC3-L007203](../../agents/web_agent.py#L7203) | 7203 | `"        completion_stages = {"` | — |
| [SRC-1AE03B9EC3-L007204](../../agents/web_agent.py#L7204) | 7204 | `"            \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L007205](../../agents/web_agent.py#L7205) | 7205 | `"            \"accepted_sources\": len(sources),"` | — |
| [SRC-1AE03B9EC3-L007206](../../agents/web_agent.py#L7206) | 7206 | `"            \"pages_read\": fetched_pages,"` | — |
| [SRC-1AE03B9EC3-L007207](../../agents/web_agent.py#L7207) | 7207 | `"            \"answer_generated_by_model\": bool(used_llm),"` | — |
| [SRC-1AE03B9EC3-L007208](../../agents/web_agent.py#L7208) | 7208 | `"            \"claim_review\": review_status,"` | — |
| [SRC-1AE03B9EC3-L007209](../../agents/web_agent.py#L7209) | 7209 | `"            \"valid_citations\": citation_validation[\"valid_citation_count\"],"` | — |
| [SRC-1AE03B9EC3-L007210](../../agents/web_agent.py#L7210) | 7210 | `"            \"semantic_fact_check\": \"not_performed\","` | — |
| [SRC-1AE03B9EC3-L007211](../../agents/web_agent.py#L7211) | 7211 | `"            \"semantic_claim_support_assessment\": semantic_claim_verification.get(\"status\", \"not_performed\"),"` | — |
| [SRC-1AE03B9EC3-L007212](../../agents/web_agent.py#L7212) | 7212 | `"        }"` | — |
| [SRC-1AE03B9EC3-L007213](../../agents/web_agent.py#L7213) | 7213 | `"        if semantic_answer_withheld:"` | — |
| [SRC-1AE03B9EC3-L007214](../../agents/web_agent.py#L7214) | 7214 | `"            pipeline_completion_status = \"partial\""` | — |
| [SRC-1AE03B9EC3-L007215](../../agents/web_agent.py#L7215) | 7215 | `"        report[\"pipeline_completion_status\"] = pipeline_completion_status"` | — |
| [SRC-1AE03B9EC3-L007216](../../agents/web_agent.py#L7216) | 7216 | `"        report[\"completion_stages\"] = completion_stages"` | — |
| [SRC-1AE03B9EC3-L007217](../../agents/web_agent.py#L7217) | 7217 | `"        report[\"pipeline_completion_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L007218](../../agents/web_agent.py#L7218) | 7218 | `"            \"pipeline stage completion only; not a guarantee of factual correctness\""` | — |
| [SRC-1AE03B9EC3-L007219](../../agents/web_agent.py#L7219) | 7219 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007220](../../agents/web_agent.py#L7220) | 7220 | `""` | — |
| [SRC-1AE03B9EC3-L007221](../../agents/web_agent.py#L7221) | 7221 | `"        public_sources = []"` | — |
| [SRC-1AE03B9EC3-L007222](../../agents/web_agent.py#L7222) | 7222 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L007223](../../agents/web_agent.py#L7223) | 7223 | `"            public_sources.append({"` | — |
| [SRC-1AE03B9EC3-L007224](../../agents/web_agent.py#L7224) | 7224 | `"                \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L007225](../../agents/web_agent.py#L7225) | 7225 | `"                \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L007226](../../agents/web_agent.py#L7226) | 7226 | `"                \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007227](../../agents/web_agent.py#L7227) | 7227 | `"                \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L007228](../../agents/web_agent.py#L7228) | 7228 | `"                \"readable_page_text_available\": bool(source.get(\"page_fetched\")) and bool(str(source.get(\"page_text\") or \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L007229](../../agents/web_agent.py#L7229) | 7229 | `"                \"page_text_present_without_fetch_flag\": bool(str(source.get(\"page_text\") or \"\").strip()) and not bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L007230](../../agents/web_agent.py#L7230) | 7230 | `"                \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L007231](../../agents/web_agent.py#L7231) | 7231 | `"                \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L007232](../../agents/web_agent.py#L7232) | 7232 | `"                \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L007233](../../agents/web_agent.py#L7233) | 7233 | `"                \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007234](../../agents/web_agent.py#L7234) | 7234 | `"                \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L007235](../../agents/web_agent.py#L7235) | 7235 | `"                \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007236](../../agents/web_agent.py#L7236) | 7236 | `"                \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007237](../../agents/web_agent.py#L7237) | 7237 | `"                \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007238](../../agents/web_agent.py#L7238) | 7238 | `"                \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L007239](../../agents/web_agent.py#L7239) | 7239 | `"                \"lead_qualification\": source.get(\"lead_qualification\"),"` | — |
| [SRC-1AE03B9EC3-L007240](../../agents/web_agent.py#L7240) | 7240 | `"                \"lead_intent_evidence\": source.get(\"lead_intent_evidence\"),"` | — |
| [SRC-1AE03B9EC3-L007241](../../agents/web_agent.py#L7241) | 7241 | `"            })"` | — |
| [SRC-1AE03B9EC3-L007242](../../agents/web_agent.py#L7242) | 7242 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L007243](../../agents/web_agent.py#L7243) | 7243 | `"            \"answer\": answer,"` | — |
| [SRC-1AE03B9EC3-L007244](../../agents/web_agent.py#L7244) | 7244 | `"            \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L007245](../../agents/web_agent.py#L7245) | 7245 | `"            \"search_query\": (plan.get(\"queries\") or [\"\"])[0],"` | — |
| [SRC-1AE03B9EC3-L007246](../../agents/web_agent.py#L7246) | 7246 | `"            \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L007247](../../agents/web_agent.py#L7247) | 7247 | `"            \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L007248](../../agents/web_agent.py#L7248) | 7248 | `"                \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L007249](../../agents/web_agent.py#L7249) | 7249 | `"                \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L007250](../../agents/web_agent.py#L7250) | 7250 | `"                \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L007251](../../agents/web_agent.py#L7251) | 7251 | `"                \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L007252](../../agents/web_agent.py#L7252) | 7252 | `"                \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L007253](../../agents/web_agent.py#L7253) | 7253 | `"                \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L007254](../../agents/web_agent.py#L7254) | 7254 | `"                \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L007255](../../agents/web_agent.py#L7255) | 7255 | `"                \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L007256](../../agents/web_agent.py#L7256) | 7256 | `"                \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L007257](../../agents/web_agent.py#L7257) | 7257 | `"                \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L007258](../../agents/web_agent.py#L7258) | 7258 | `"            },"` | — |
| [SRC-1AE03B9EC3-L007259](../../agents/web_agent.py#L7259) | 7259 | `"            \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L007260](../../agents/web_agent.py#L7260) | 7260 | `"            \"sources\": public_sources,"` | — |
| [SRC-1AE03B9EC3-L007261](../../agents/web_agent.py#L7261) | 7261 | `"            \"research_quality\": research_quality,"` | — |
| [SRC-1AE03B9EC3-L007262](../../agents/web_agent.py#L7262) | 7262 | `"            \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L007263](../../agents/web_agent.py#L7263) | 7263 | `"            \"answer_evidence_status\": answer_evidence_status,"` | — |
| [SRC-1AE03B9EC3-L007264](../../agents/web_agent.py#L7264) | 7264 | `"            \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L007265](../../agents/web_agent.py#L7265) | 7265 | `"            \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L007266](../../agents/web_agent.py#L7266) | 7266 | `"            \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L007267](../../agents/web_agent.py#L7267) | 7267 | `"            \"coverage_repair_status\": coverage_repair_status,"` | — |
| [SRC-1AE03B9EC3-L007268](../../agents/web_agent.py#L7268) | 7268 | `"            \"used_language_model\": used_llm,"` | — |
| [SRC-1AE03B9EC3-L007269](../../agents/web_agent.py#L7269) | 7269 | `"            \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L007270](../../agents/web_agent.py#L7270) | 7270 | `"            \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L007271](../../agents/web_agent.py#L7271) | 7271 | `"            \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L007272](../../agents/web_agent.py#L7272) | 7272 | `"            \"warnings\": warnings,"` | — |
| [SRC-1AE03B9EC3-L007273](../../agents/web_agent.py#L7273) | 7273 | `"            \"kind\": \"web_research\" if used_llm else \"web_fallback\","` | — |
| [SRC-1AE03B9EC3-L007274](../../agents/web_agent.py#L7274) | 7274 | `"            \"final_answer_status\": final_answer_status,"` | — |
| [SRC-1AE03B9EC3-L007275](../../agents/web_agent.py#L7275) | 7275 | `"            \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L007276](../../agents/web_agent.py#L7276) | 7276 | `"            \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L007277](../../agents/web_agent.py#L7277) | 7277 | `"        }"` | — |
| [SRC-1AE03B9EC3-L007278](../../agents/web_agent.py#L7278) | 7278 | `""` | — |
| [SRC-1AE03B9EC3-L007279](../../agents/web_agent.py#L7279) | 7279 | `"def _normalized_provider_usage("` | — |
| [SRC-1AE03B9EC3-L007280](../../agents/web_agent.py#L7280) | 7280 | `"    usage: Any, *, provider_base_url: str = \"\""` | — |
| [SRC-1AE03B9EC3-L007281](../../agents/web_agent.py#L7281) | 7281 | `") -> dict[str, int \| float] \| None:"` | — |
| [SRC-1AE03B9EC3-L007282](../../agents/web_agent.py#L7282) | 7282 | `"    \"\"\"Allowlist safe counters; interpret generic 'cost' as USD only for OpenRouter.\"\"\""` | — |
| [SRC-1AE03B9EC3-L007283](../../agents/web_agent.py#L7283) | 7283 | `"    if not isinstance(usage, dict):"` | — |
| [SRC-1AE03B9EC3-L007284](../../agents/web_agent.py#L7284) | 7284 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L007285](../../agents/web_agent.py#L7285) | 7285 | `"    normalized: dict[str, int \| float] = {}"` | — |
| [SRC-1AE03B9EC3-L007286](../../agents/web_agent.py#L7286) | 7286 | `"    for source_key in (\"prompt_tokens\", \"completion_tokens\", \"total_tokens\"):"` | — |
| [SRC-1AE03B9EC3-L007287](../../agents/web_agent.py#L7287) | 7287 | `"        value = usage.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L007288](../../agents/web_agent.py#L7288) | 7288 | `"        if isinstance(value, int) and not isinstance(value, bool) and value >= 0:"` | — |
| [SRC-1AE03B9EC3-L007289](../../agents/web_agent.py#L7289) | 7289 | `"            normalized[source_key] = value"` | — |
| [SRC-1AE03B9EC3-L007290](../../agents/web_agent.py#L7290) | 7290 | `"    cost_keys = [\"cost_usd\"]"` | — |
| [SRC-1AE03B9EC3-L007291](../../agents/web_agent.py#L7291) | 7291 | `"    provider_host = \"\""` | — |
| [SRC-1AE03B9EC3-L007292](../../agents/web_agent.py#L7292) | 7292 | `"    if isinstance(provider_base_url, str):"` | — |
| [SRC-1AE03B9EC3-L007293](../../agents/web_agent.py#L7293) | 7293 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L007294](../../agents/web_agent.py#L7294) | 7294 | `"            provider_host = (urllib.parse.urlsplit(provider_base_url.strip()).hostname or \"\").lower().rstrip(\".\")"` | — |
| [SRC-1AE03B9EC3-L007295](../../agents/web_agent.py#L7295) | 7295 | `"        except ValueError:"` | — |
| [SRC-1AE03B9EC3-L007296](../../agents/web_agent.py#L7296) | 7296 | `"            provider_host = \"\""` | — |
| [SRC-1AE03B9EC3-L007297](../../agents/web_agent.py#L7297) | 7297 | `"    is_openrouter = ("` | — |
| [SRC-1AE03B9EC3-L007298](../../agents/web_agent.py#L7298) | 7298 | `"        provider_host == \"openrouter.ai\""` | — |
| [SRC-1AE03B9EC3-L007299](../../agents/web_agent.py#L7299) | 7299 | `"        or provider_host.endswith(\".openrouter.ai\")"` | — |
| [SRC-1AE03B9EC3-L007300](../../agents/web_agent.py#L7300) | 7300 | `"    )"` | — |
| [SRC-1AE03B9EC3-L007301](../../agents/web_agent.py#L7301) | 7301 | `"    if is_openrouter:"` | — |
| [SRC-1AE03B9EC3-L007302](../../agents/web_agent.py#L7302) | 7302 | `"        cost_keys.extend([\"cost\", \"total_cost\"])"` | — |
| [SRC-1AE03B9EC3-L007303](../../agents/web_agent.py#L7303) | 7303 | `"    for source_key in cost_keys:"` | — |
| [SRC-1AE03B9EC3-L007304](../../agents/web_agent.py#L7304) | 7304 | `"        value = usage.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L007305](../../agents/web_agent.py#L7305) | 7305 | `"        if isinstance(value, (int, float)) and not isinstance(value, bool):"` | — |
| [SRC-1AE03B9EC3-L007306](../../agents/web_agent.py#L7306) | 7306 | `"            number = float(value)"` | — |
| [SRC-1AE03B9EC3-L007307](../../agents/web_agent.py#L7307) | 7307 | `"            if number >= 0 and math.isfinite(number):"` | — |
| [SRC-1AE03B9EC3-L007308](../../agents/web_agent.py#L7308) | 7308 | `"                normalized[\"cost_usd\"] = number"` | — |
| [SRC-1AE03B9EC3-L007309](../../agents/web_agent.py#L7309) | 7309 | `"                break"` | — |
| [SRC-1AE03B9EC3-L007310](../../agents/web_agent.py#L7310) | 7310 | `"    return normalized or None"` | — |
| [SRC-1AE03B9EC3-L007311](../../agents/web_agent.py#L7311) | 7311 | `""` | — |
| [SRC-1AE03B9EC3-L007312](../../agents/web_agent.py#L7312) | 7312 | `"def _model_usage_record("` | — |
| [SRC-1AE03B9EC3-L007313](../../agents/web_agent.py#L7313) | 7313 | `"    requested_model: str,"` | — |
| [SRC-1AE03B9EC3-L007314](../../agents/web_agent.py#L7314) | 7314 | `"    candidate_model: str,"` | — |
| [SRC-1AE03B9EC3-L007315](../../agents/web_agent.py#L7315) | 7315 | `"    response_data: dict[str, Any],"` | — |
| [SRC-1AE03B9EC3-L007316](../../agents/web_agent.py#L7316) | 7316 | `"    provider_base_url: str,"` | — |
| [SRC-1AE03B9EC3-L007317](../../agents/web_agent.py#L7317) | 7317 | `") -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L007318](../../agents/web_agent.py#L7318) | 7318 | `"    \"\"\"Return only allowlisted provider usage metadata, never raw prompts/responses.\"\"\""` | — |
| [SRC-1AE03B9EC3-L007319](../../agents/web_agent.py#L7319) | 7319 | `"    record: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L007320](../../agents/web_agent.py#L7320) | 7320 | `"        \"requested_model\": requested_model,"` | — |
| [SRC-1AE03B9EC3-L007321](../../agents/web_agent.py#L7321) | 7321 | `"        \"used_model\": candidate_model,"` | — |
| [SRC-1AE03B9EC3-L007322](../../agents/web_agent.py#L7322) | 7322 | `"        \"fallback_used\": \"true\" if candidate_model != requested_model else \"false\","` | — |
| [SRC-1AE03B9EC3-L007323](../../agents/web_agent.py#L7323) | 7323 | `"    }"` | — |
| [SRC-1AE03B9EC3-L007324](../../agents/web_agent.py#L7324) | 7324 | `"    provider_usage = _normalized_provider_usage("` | — |
| [SRC-1AE03B9EC3-L007325](../../agents/web_agent.py#L7325) | 7325 | `"        response_data.get(\"usage\"), provider_base_url=provider_base_url"` | — |
| [SRC-1AE03B9EC3-L007326](../../agents/web_agent.py#L7326) | 7326 | `"    )"` | — |
| [SRC-1AE03B9EC3-L007327](../../agents/web_agent.py#L7327) | 7327 | `"    if provider_usage is not None:"` | — |
| [SRC-1AE03B9EC3-L007328](../../agents/web_agent.py#L7328) | 7328 | `"        record[\"provider_usage\"] = provider_usage"` | — |
| [SRC-1AE03B9EC3-L007329](../../agents/web_agent.py#L7329) | 7329 | `"    return record"` | — |
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
| [SRC-EEF2E6447C-L000227](../../api/omarai.py#L227) | 227 | `"                pass"` | — |
| [SRC-EEF2E6447C-L000228](../../api/omarai.py#L228) | 228 | `"        return bytes(line)"` | — |
| [SRC-EEF2E6447C-L000229](../../api/omarai.py#L229) | 229 | `""` | — |
| [SRC-EEF2E6447C-L000230](../../api/omarai.py#L230) | 230 | `"    def read1(self, size=-1):"` | — |
| [SRC-EEF2E6447C-L000231](../../api/omarai.py#L231) | 231 | `"        \"\"\"Read one chunk; body code applies its own idle and absolute deadlines.\"\"\""` | — |
| [SRC-EEF2E6447C-L000232](../../api/omarai.py#L232) | 232 | `"        if size == 0:"` | — |
| [SRC-EEF2E6447C-L000233](../../api/omarai.py#L233) | 233 | `"            return b\"\""` | — |
| [SRC-EEF2E6447C-L000234](../../api/omarai.py#L234) | 234 | `"        if size is None or size < 0:"` | — |
| [SRC-EEF2E6447C-L000235](../../api/omarai.py#L235) | 235 | `"            size = 8_192"` | — |
| [SRC-EEF2E6447C-L000236](../../api/omarai.py#L236) | 236 | `"        if self._buffer:"` | — |
| [SRC-EEF2E6447C-L000237](../../api/omarai.py#L237) | 237 | `"            take = min(len(self._buffer), size)"` | — |
| [SRC-EEF2E6447C-L000238](../../api/omarai.py#L238) | 238 | `"            data = bytes(self._buffer[:take])"` | — |
| [SRC-EEF2E6447C-L000239](../../api/omarai.py#L239) | 239 | `"            del self._buffer[:take]"` | — |
| [SRC-EEF2E6447C-L000240](../../api/omarai.py#L240) | 240 | `"            return data"` | — |
| [SRC-EEF2E6447C-L000241](../../api/omarai.py#L241) | 241 | `"        return self.connection.recv(size)"` | — |
| [SRC-EEF2E6447C-L000242](../../api/omarai.py#L242) | 242 | `""` | — |
| [SRC-EEF2E6447C-L000243](../../api/omarai.py#L243) | 243 | `"    def close(self):"` | — |
| [SRC-EEF2E6447C-L000244](../../api/omarai.py#L244) | 244 | `"        # The request handler owns the socket and closes its output stream."` | — |
| [SRC-EEF2E6447C-L000245](../../api/omarai.py#L245) | 245 | `"        return None"` | — |
| [SRC-EEF2E6447C-L000246](../../api/omarai.py#L246) | 246 | `""` | — |
| [SRC-EEF2E6447C-L000247](../../api/omarai.py#L247) | 247 | `""` | — |
| [SRC-EEF2E6447C-L000248](../../api/omarai.py#L248) | 248 | `"def _configured_agent_concurrency_limit() -> int:"` | — |
| [SRC-EEF2E6447C-L000249](../../api/omarai.py#L249) | 249 | `"    \"\"\"Return a process-local cap for expensive research and diagnostics operations.\"\"\""` | — |
| [SRC-EEF2E6447C-L000250](../../api/omarai.py#L250) | 250 | `"    try:"` | — |
| [SRC-EEF2E6447C-L000251](../../api/omarai.py#L251) | 251 | `"        configured = int(os.getenv(\"OMARAI_MAX_CONCURRENT_AGENT_REQUESTS\", \"4\").strip())"` | — |
| [SRC-EEF2E6447C-L000252](../../api/omarai.py#L252) | 252 | `"    except ValueError:"` | — |
| [SRC-EEF2E6447C-L000253](../../api/omarai.py#L253) | 253 | `"        configured = 4"` | — |
| [SRC-EEF2E6447C-L000254](../../api/omarai.py#L254) | 254 | `"    return max(1, min(configured, 8))"` | — |
| [SRC-EEF2E6447C-L000255](../../api/omarai.py#L255) | 255 | `""` | — |
| [SRC-EEF2E6447C-L000256](../../api/omarai.py#L256) | 256 | `""` | — |
| [SRC-EEF2E6447C-L000257](../../api/omarai.py#L257) | 257 | `"DEFAULT_HTTP_CONNECTION_LIMIT = 32"` | — |
| [SRC-EEF2E6447C-L000258](../../api/omarai.py#L258) | 258 | `"MAX_HTTP_CONNECTION_LIMIT = 128"` | — |
| [SRC-EEF2E6447C-L000259](../../api/omarai.py#L259) | 259 | `""` | — |
| [SRC-EEF2E6447C-L000260](../../api/omarai.py#L260) | 260 | `""` | — |
| [SRC-EEF2E6447C-L000261](../../api/omarai.py#L261) | 261 | `"def _configured_http_connection_limit() -> int:"` | — |
| [SRC-EEF2E6447C-L000262](../../api/omarai.py#L262) | 262 | `"    \"\"\"Return the bounded number of live HTTP handler threads for this process.\"\"\""` | — |
| [SRC-EEF2E6447C-L000263](../../api/omarai.py#L263) | 263 | `"    try:"` | — |
| [SRC-EEF2E6447C-L000264](../../api/omarai.py#L264) | 264 | `"        configured = int(os.getenv(\"OMARAI_MAX_CONCURRENT_HTTP_CONNECTIONS\", \"32\").strip())"` | — |
| [SRC-EEF2E6447C-L000265](../../api/omarai.py#L265) | 265 | `"    except ValueError:"` | — |
| [SRC-EEF2E6447C-L000266](../../api/omarai.py#L266) | 266 | `"        configured = DEFAULT_HTTP_CONNECTION_LIMIT"` | — |
| [SRC-EEF2E6447C-L000267](../../api/omarai.py#L267) | 267 | `"    return max(1, min(configured, MAX_HTTP_CONNECTION_LIMIT))"` | — |
| [SRC-EEF2E6447C-L000268](../../api/omarai.py#L268) | 268 | `""` | — |
| [SRC-EEF2E6447C-L000269](../../api/omarai.py#L269) | 269 | `""` | — |
| [SRC-EEF2E6447C-L000270](../../api/omarai.py#L270) | 270 | `"BUILD_SHA_FILE = Path(__file__).resolve().parents[1] / \"BUILD_SHA\""` | — |
| [SRC-EEF2E6447C-L000271](../../api/omarai.py#L271) | 271 | `"_PLATFORM_BUILD_SHA_ENVIRONMENTS = ("` | — |
| [SRC-EEF2E6447C-L000272](../../api/omarai.py#L272) | 272 | `"    (\"RAILWAY_GIT_COMMIT_SHA\", \"platform:railway\"),"` | — |
| [SRC-EEF2E6447C-L000273](../../api/omarai.py#L273) | 273 | `"    (\"RENDER_GIT_COMMIT\", \"platform:render\"),"` | — |
| [SRC-EEF2E6447C-L000274](../../api/omarai.py#L274) | 274 | `")"` | — |
| [SRC-EEF2E6447C-L000275](../../api/omarai.py#L275) | 275 | `""` | — |
| [SRC-EEF2E6447C-L000276](../../api/omarai.py#L276) | 276 | `""` | — |
| [SRC-EEF2E6447C-L000277](../../api/omarai.py#L277) | 277 | `"def _valid_build_sha(value: str) -> bool:"` | — |
| [SRC-EEF2E6447C-L000278](../../api/omarai.py#L278) | 278 | `"    candidate = value.strip().lower()"` | — |
| [SRC-EEF2E6447C-L000279](../../api/omarai.py#L279) | 279 | `"    return len(candidate) == 40 and all(char in \"0123456789abcdef\" for char in candidate)"` | — |
| [SRC-EEF2E6447C-L000280](../../api/omarai.py#L280) | 280 | `""` | — |
| [SRC-EEF2E6447C-L000281](../../api/omarai.py#L281) | 281 | `""` | — |
| [SRC-EEF2E6447C-L000282](../../api/omarai.py#L282) | 282 | `"def _build_identity() -> tuple[str, str]:"` | — |
| [SRC-EEF2E6447C-L000283](../../api/omarai.py#L283) | 283 | `"    \"\"\"Prefer immutable image metadata, then documented hosting-provided Git SHAs.\"\"\""` | — |
| [SRC-EEF2E6447C-L000284](../../api/omarai.py#L284) | 284 | `"    try:"` | — |
| [SRC-EEF2E6447C-L000285](../../api/omarai.py#L285) | 285 | `"        baked = BUILD_SHA_FILE.read_text(encoding=\"ascii\").strip().lower()"` | — |
| [SRC-EEF2E6447C-L000286](../../api/omarai.py#L286) | 286 | `"    except (OSError, UnicodeError):"` | — |
| [SRC-EEF2E6447C-L000287](../../api/omarai.py#L287) | 287 | `"        baked = \"\""` | — |
| [SRC-EEF2E6447C-L000288](../../api/omarai.py#L288) | 288 | `"    if _valid_build_sha(baked):"` | — |
| [SRC-EEF2E6447C-L000289](../../api/omarai.py#L289) | 289 | `"        return baked, \"image_baked\""` | — |
| [SRC-EEF2E6447C-L000290](../../api/omarai.py#L290) | 290 | `""` | — |
| [SRC-EEF2E6447C-L000291](../../api/omarai.py#L291) | 291 | `"    for environment_name, source in _PLATFORM_BUILD_SHA_ENVIRONMENTS:"` | — |
| [SRC-EEF2E6447C-L000292](../../api/omarai.py#L292) | 292 | `"        candidate = os.getenv(environment_name, \"\").strip().lower()"` | — |
| [SRC-EEF2E6447C-L000293](../../api/omarai.py#L293) | 293 | `"        if _valid_build_sha(candidate):"` | — |
| [SRC-EEF2E6447C-L000294](../../api/omarai.py#L294) | 294 | `"            return candidate, source"` | — |
| [SRC-EEF2E6447C-L000295](../../api/omarai.py#L295) | 295 | `"    return \"unknown\", \"unknown\""` | — |
| [SRC-EEF2E6447C-L000296](../../api/omarai.py#L296) | 296 | `""` | — |
| [SRC-EEF2E6447C-L000297](../../api/omarai.py#L297) | 297 | `""` | — |
| [SRC-EEF2E6447C-L000298](../../api/omarai.py#L298) | 298 | `"def _build_sha() -> str:"` | — |
| [SRC-EEF2E6447C-L000299](../../api/omarai.py#L299) | 299 | `"    \"\"\"Return a validated source SHA, or 'unknown' when no trusted build evidence exists.\"\"\""` | — |
| [SRC-EEF2E6447C-L000300](../../api/omarai.py#L300) | 300 | `"    return _build_identity()[0]"` | — |
| [SRC-EEF2E6447C-L000301](../../api/omarai.py#L301) | 301 | `""` | — |
| [SRC-EEF2E6447C-L000302](../../api/omarai.py#L302) | 302 | `""` | — |
| [SRC-EEF2E6447C-L000303](../../api/omarai.py#L303) | 303 | `"class Handler(BaseHTTPRequestHandler):"` | — |
| [SRC-EEF2E6447C-L000304](../../api/omarai.py#L304) | 304 | `"    def setup(self):"` | — |
| [SRC-EEF2E6447C-L000305](../../api/omarai.py#L305) | 305 | `"        \"\"\"Install a reader with a strict deadline for the request line and headers.\"\"\""` | — |
| [SRC-EEF2E6447C-L000306](../../api/omarai.py#L306) | 306 | `"        self.connection = self.request"` | — |
| [SRC-EEF2E6447C-L000307](../../api/omarai.py#L307) | 307 | `"        if self.timeout is not None:"` | — |
| [SRC-EEF2E6447C-L000308](../../api/omarai.py#L308) | 308 | `"            self.connection.settimeout(self.timeout)"` | — |
| [SRC-EEF2E6447C-L000309](../../api/omarai.py#L309) | 309 | `"        self._request_header_deadline = None"` | — |
| [SRC-EEF2E6447C-L000310](../../api/omarai.py#L310) | 310 | `"        self.rfile = _DeadlineRequestReader(self.connection, self)"` | — |
| [SRC-EEF2E6447C-L000311](../../api/omarai.py#L311) | 311 | `"        self.wfile = self.connection.makefile(\"wb\", self.wbufsize)"` | — |
| [SRC-EEF2E6447C-L000312](../../api/omarai.py#L312) | 312 | `""` | — |
| [SRC-EEF2E6447C-L000313](../../api/omarai.py#L313) | 313 | `"    def handle_one_request(self):"` | — |
| [SRC-EEF2E6447C-L000314](../../api/omarai.py#L314) | 314 | `"        timeout = max("` | — |
| [SRC-EEF2E6447C-L000315](../../api/omarai.py#L315) | 315 | `"            0.1,"` | — |
| [SRC-EEF2E6447C-L000316](../../api/omarai.py#L316) | 316 | `"            min("` | — |
| [SRC-EEF2E6447C-L000317](../../api/omarai.py#L317) | 317 | `"                float(REQUEST_HEADER_READ_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000318](../../api/omarai.py#L318) | 318 | `"                MAX_REQUEST_HEADER_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000319](../../api/omarai.py#L319) | 319 | `"            ),"` | — |
| [SRC-EEF2E6447C-L000320](../../api/omarai.py#L320) | 320 | `"        )"` | — |
| [SRC-EEF2E6447C-L000321](../../api/omarai.py#L321) | 321 | `"        self._request_header_deadline = time.monotonic() + timeout"` | — |
| [SRC-EEF2E6447C-L000322](../../api/omarai.py#L322) | 322 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000323](../../api/omarai.py#L323) | 323 | `"            super().handle_one_request()"` | — |
| [SRC-EEF2E6447C-L000324](../../api/omarai.py#L324) | 324 | `"        except TimeoutError:"` | — |
| [SRC-EEF2E6447C-L000325](../../api/omarai.py#L325) | 325 | `"            # Incomplete request line/headers are untrusted protocol input;"` | — |
| [SRC-EEF2E6447C-L000326](../../api/omarai.py#L326) | 326 | `"            # close the socket without trying to parse or answer a partial request."` | — |
| [SRC-EEF2E6447C-L000327](../../api/omarai.py#L327) | 327 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000328](../../api/omarai.py#L328) | 328 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000329](../../api/omarai.py#L329) | 329 | `"            self._request_header_deadline = None"` | — |
| [SRC-EEF2E6447C-L000330](../../api/omarai.py#L330) | 330 | `""` | — |
| [SRC-EEF2E6447C-L000331](../../api/omarai.py#L331) | 331 | `"    def parse_request(self):"` | — |
| [SRC-EEF2E6447C-L000332](../../api/omarai.py#L332) | 332 | `"        \"\"\"Reject ambiguous HTTP message framing before dispatching any handler.\"\"\""` | — |
| [SRC-EEF2E6447C-L000333](../../api/omarai.py#L333) | 333 | `"        if not super().parse_request():"` | — |
| [SRC-EEF2E6447C-L000334](../../api/omarai.py#L334) | 334 | `"            return False"` | — |
| [SRC-EEF2E6447C-L000335](../../api/omarai.py#L335) | 335 | `""` | — |
| [SRC-EEF2E6447C-L000336](../../api/omarai.py#L336) | 336 | `"        transfer_encodings = self.headers.get_all(\"Transfer-Encoding\", [])"` | — |
| [SRC-EEF2E6447C-L000337](../../api/omarai.py#L337) | 337 | `"        if transfer_encodings:"` | — |
| [SRC-EEF2E6447C-L000338](../../api/omarai.py#L338) | 338 | `"            # This API does not implement chunked request decoding. Never let a"` | — |
| [SRC-EEF2E6447C-L000339](../../api/omarai.py#L339) | 339 | `"            # proxy/backend disagree about where the request body ends."` | — |
| [SRC-EEF2E6447C-L000340](../../api/omarai.py#L340) | 340 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000341](../../api/omarai.py#L341) | 341 | `"            self.send_error(400, \"Transfer-Encoding is not supported\")"` | — |
| [SRC-EEF2E6447C-L000342](../../api/omarai.py#L342) | 342 | `"            return False"` | — |
| [SRC-EEF2E6447C-L000343](../../api/omarai.py#L343) | 343 | `""` | — |
| [SRC-EEF2E6447C-L000344](../../api/omarai.py#L344) | 344 | `"        content_lengths = self.headers.get_all(\"Content-Length\", [])"` | — |
| [SRC-EEF2E6447C-L000345](../../api/omarai.py#L345) | 345 | `"        if len(content_lengths) > 1:"` | — |
| [SRC-EEF2E6447C-L000346](../../api/omarai.py#L346) | 346 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000347](../../api/omarai.py#L347) | 347 | `"            self.send_error(400, \"Multiple Content-Length headers are not supported\")"` | — |
| [SRC-EEF2E6447C-L000348](../../api/omarai.py#L348) | 348 | `"            return False"` | — |
| [SRC-EEF2E6447C-L000349](../../api/omarai.py#L349) | 349 | `""` | — |
| [SRC-EEF2E6447C-L000350](../../api/omarai.py#L350) | 350 | `"        if content_lengths:"` | — |
| [SRC-EEF2E6447C-L000351](../../api/omarai.py#L351) | 351 | `"            raw_size = content_lengths[0].strip()"` | — |
| [SRC-EEF2E6447C-L000352](../../api/omarai.py#L352) | 352 | `"            if not raw_size or not raw_size.isascii() or not raw_size.isdecimal():"` | — |
| [SRC-EEF2E6447C-L000353](../../api/omarai.py#L353) | 353 | `"                self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000354](../../api/omarai.py#L354) | 354 | `"                self.send_error(400, \"valid Content-Length is required\")"` | — |
| [SRC-EEF2E6447C-L000355](../../api/omarai.py#L355) | 355 | `"                return False"` | — |
| [SRC-EEF2E6447C-L000356](../../api/omarai.py#L356) | 356 | `"            if self.command != \"POST\" and raw_size.lstrip(\"0\"):"` | — |
