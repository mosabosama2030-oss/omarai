# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **021**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L006995 إلى SRC-EEF2E6447C-L000496
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L006995](../../agents/web_agent.py#L6995) | 6995 | `"            else \"not_machine_assessed_no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L006996](../../agents/web_agent.py#L6996) | 6996 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006997](../../agents/web_agent.py#L6997) | 6997 | `"        if semantic_answer_withheld:"` | — |
| [SRC-1AE03B9EC3-L006998](../../agents/web_agent.py#L6998) | 6998 | `"            task_fulfillment_status = \"not_assessed_insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L006999](../../agents/web_agent.py#L6999) | 6999 | `"        answer_coverage[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L007000](../../agents/web_agent.py#L7000) | 7000 | `"        answer_coverage[\"semantic_verification_status\"] = semantic_claim_verification.get(\"status\")"` | — |
| [SRC-1AE03B9EC3-L007001](../../agents/web_agent.py#L7001) | 7001 | `"        report[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L007002](../../agents/web_agent.py#L7002) | 7002 | `"        report[\"answer_integrity\"] = answer_integrity"` | — |
| [SRC-1AE03B9EC3-L007003](../../agents/web_agent.py#L7003) | 7003 | `"        report[\"requirement_evidence\"] = answer_integrity.get(\"requirement_evidence\", [])"` | — |
| [SRC-1AE03B9EC3-L007004](../../agents/web_agent.py#L7004) | 7004 | `"        report[\"connector_summary\"] = self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L007005](../../agents/web_agent.py#L7005) | 7005 | `"            list(self._provider_diagnostics), sources"` | — |
| [SRC-1AE03B9EC3-L007006](../../agents/web_agent.py#L7006) | 7006 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007007](../../agents/web_agent.py#L7007) | 7007 | `"        report[\"provider_diagnostics\"] = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L007008](../../agents/web_agent.py#L7008) | 7008 | `"        distinct_providers = {"` | — |
| [SRC-1AE03B9EC3-L007009](../../agents/web_agent.py#L7009) | 7009 | `"            provider for source in sources for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L007010](../../agents/web_agent.py#L7010) | 7010 | `"        }"` | — |
| [SRC-1AE03B9EC3-L007011](../../agents/web_agent.py#L7011) | 7011 | `"        distinct_domains = {"` | — |
| [SRC-1AE03B9EC3-L007012](../../agents/web_agent.py#L7012) | 7012 | `"            registrable_domain("` | — |
| [SRC-1AE03B9EC3-L007013](../../agents/web_agent.py#L7013) | 7013 | `"                source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L007014](../../agents/web_agent.py#L7014) | 7014 | `"                or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L007015](../../agents/web_agent.py#L7015) | 7015 | `"                or \"\""` | — |
| [SRC-1AE03B9EC3-L007016](../../agents/web_agent.py#L7016) | 7016 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007017](../../agents/web_agent.py#L7017) | 7017 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L007018](../../agents/web_agent.py#L7018) | 7018 | `"        }"` | — |
| [SRC-1AE03B9EC3-L007019](../../agents/web_agent.py#L7019) | 7019 | `"        distinct_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L007020](../../agents/web_agent.py#L7020) | 7020 | `"        fetched_pages = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L007021](../../agents/web_agent.py#L7021) | 7021 | `"        if semantic_answer_withheld:"` | — |
| [SRC-1AE03B9EC3-L007022](../../agents/web_agent.py#L7022) | 7022 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L007023](../../agents/web_agent.py#L7023) | 7023 | `"        elif ("` | — |
| [SRC-1AE03B9EC3-L007024](../../agents/web_agent.py#L7024) | 7024 | `"            len(sources) >= 4 and len(distinct_domains) >= 3"` | — |
| [SRC-1AE03B9EC3-L007025](../../agents/web_agent.py#L7025) | 7025 | `"            and len(distinct_providers) >= 2 and fetched_pages >= 1"` | — |
| [SRC-1AE03B9EC3-L007026](../../agents/web_agent.py#L7026) | 7026 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L007027](../../agents/web_agent.py#L7027) | 7027 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L007028](../../agents/web_agent.py#L7028) | 7028 | `"            research_quality = \"excellent\""` | — |
| [SRC-1AE03B9EC3-L007029](../../agents/web_agent.py#L7029) | 7029 | `"        elif ("` | — |
| [SRC-1AE03B9EC3-L007030](../../agents/web_agent.py#L7030) | 7030 | `"            len(sources) >= 2 and len(distinct_domains) >= 2"` | — |
| [SRC-1AE03B9EC3-L007031](../../agents/web_agent.py#L7031) | 7031 | `"            and (len(distinct_providers) >= 2 or fetched_pages >= 1)"` | — |
| [SRC-1AE03B9EC3-L007032](../../agents/web_agent.py#L7032) | 7032 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L007033](../../agents/web_agent.py#L7033) | 7033 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L007034](../../agents/web_agent.py#L7034) | 7034 | `"            research_quality = \"good\""` | — |
| [SRC-1AE03B9EC3-L007035](../../agents/web_agent.py#L7035) | 7035 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L007036](../../agents/web_agent.py#L7036) | 7036 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L007037](../../agents/web_agent.py#L7037) | 7037 | `""` | — |
| [SRC-1AE03B9EC3-L007038](../../agents/web_agent.py#L7038) | 7038 | `"        # Source breadth and a completed model-assisted review do not justify a"` | — |
| [SRC-1AE03B9EC3-L007039](../../agents/web_agent.py#L7039) | 7039 | `"        # positive research-quality label if the final answer has no valid source"` | — |
| [SRC-1AE03B9EC3-L007040](../../agents/web_agent.py#L7040) | 7040 | `"        # citation markers. This is a deterministic presentation guard, not a"` | — |
| [SRC-1AE03B9EC3-L007041](../../agents/web_agent.py#L7041) | 7041 | `"        # semantic entailment check."` | — |
| [SRC-1AE03B9EC3-L007042](../../agents/web_agent.py#L7042) | 7042 | `"        uncited_reviewed_answer = ("` | — |
| [SRC-1AE03B9EC3-L007043](../../agents/web_agent.py#L7043) | 7043 | `"            used_llm"` | — |
| [SRC-1AE03B9EC3-L007044](../../agents/web_agent.py#L7044) | 7044 | `"            and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L007045](../../agents/web_agent.py#L7045) | 7045 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L007046](../../agents/web_agent.py#L7046) | 7046 | `"            and citation_validation[\"valid_citation_count\"] == 0"` | — |
| [SRC-1AE03B9EC3-L007047](../../agents/web_agent.py#L7047) | 7047 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007048](../../agents/web_agent.py#L7048) | 7048 | `"        if uncited_reviewed_answer:"` | — |
| [SRC-1AE03B9EC3-L007049](../../agents/web_agent.py#L7049) | 7049 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L007050](../../agents/web_agent.py#L7050) | 7050 | `"            citation_validation[\"claim_support\"] = \"not_established_no_valid_source_citations\""` | — |
| [SRC-1AE03B9EC3-L007051](../../agents/web_agent.py#L7051) | 7051 | `"            answer_evidence_status = \"reviewed_answer_has_no_valid_citations\""` | — |
| [SRC-1AE03B9EC3-L007052](../../agents/web_agent.py#L7052) | 7052 | `"            uncited_answer_warning = ("` | — |
| [SRC-1AE03B9EC3-L007053](../../agents/web_agent.py#L7053) | 7053 | `"                \"اكتملت مراجعة النموذج، لكن الإجابة النهائية لا تحتوي على إحالات صالحة \""` | — |
| [SRC-1AE03B9EC3-L007054](../../agents/web_agent.py#L7054) | 7054 | `"                \"إلى قائمة المصادر؛ لذلك صُنّفت جودة البحث «جزئية». وجود المصادر أو \""` | — |
| [SRC-1AE03B9EC3-L007055](../../agents/web_agent.py#L7055) | 7055 | `"                \"اكتمال مراجعة النموذج لا يثبت دعم كل ادعاء.\""` | — |
| [SRC-1AE03B9EC3-L007056](../../agents/web_agent.py#L7056) | 7056 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007057](../../agents/web_agent.py#L7057) | 7057 | `"        elif citation_validation[\"valid_citation_count\"] > 0:"` | — |
| [SRC-1AE03B9EC3-L007058](../../agents/web_agent.py#L7058) | 7058 | `"            answer_evidence_status = ("` | — |
| [SRC-1AE03B9EC3-L007059](../../agents/web_agent.py#L7059) | 7059 | `"                \"semantic_support_unverified_answer_withheld\""` | — |
| [SRC-1AE03B9EC3-L007060](../../agents/web_agent.py#L7060) | 7060 | `"                if semantic_answer_withheld else \"citation_indices_validated_only\""` | — |
| [SRC-1AE03B9EC3-L007061](../../agents/web_agent.py#L7061) | 7061 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007062](../../agents/web_agent.py#L7062) | 7062 | `"            uncited_answer_warning = None"` | — |
| [SRC-1AE03B9EC3-L007063](../../agents/web_agent.py#L7063) | 7063 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L007064](../../agents/web_agent.py#L7064) | 7064 | `"            answer_evidence_status = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L007065](../../agents/web_agent.py#L7065) | 7065 | `"            uncited_answer_warning = None"` | — |
| [SRC-1AE03B9EC3-L007066](../../agents/web_agent.py#L7066) | 7066 | `""` | — |
| [SRC-1AE03B9EC3-L007067](../../agents/web_agent.py#L7067) | 7067 | `"        search_attempted = search_attempted or bool(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L007068](../../agents/web_agent.py#L7068) | 7068 | `"        report[\"search_attempted\"] = search_attempted"` | — |
| [SRC-1AE03B9EC3-L007069](../../agents/web_agent.py#L7069) | 7069 | `"        prior_search_outcome = report.get(\"search_outcome\")"` | — |
| [SRC-1AE03B9EC3-L007070](../../agents/web_agent.py#L7070) | 7070 | `"        if prior_search_outcome in _RESEARCH_ERROR_OUTCOMES and not sources:"` | — |
| [SRC-1AE03B9EC3-L007071](../../agents/web_agent.py#L7071) | 7071 | `"            # Preserve a known pipeline failure instead of relabeling it as an ordinary"` | — |
| [SRC-1AE03B9EC3-L007072](../../agents/web_agent.py#L7072) | 7072 | `"            # zero-result search merely because the outer request reached its return path."` | — |
| [SRC-1AE03B9EC3-L007073](../../agents/web_agent.py#L7073) | 7073 | `"            report[\"search_outcome\"] = prior_search_outcome"` | — |
| [SRC-1AE03B9EC3-L007074](../../agents/web_agent.py#L7074) | 7074 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L007075](../../agents/web_agent.py#L7075) | 7075 | `"            report[\"search_outcome\"] = ("` | — |
| [SRC-1AE03B9EC3-L007076](../../agents/web_agent.py#L7076) | 7076 | `"                \"attempted_with_usable_sources\" if search_attempted and sources"` | — |
| [SRC-1AE03B9EC3-L007077](../../agents/web_agent.py#L7077) | 7077 | `"                else \"attempted_no_usable_sources\" if search_attempted"` | — |
| [SRC-1AE03B9EC3-L007078](../../agents/web_agent.py#L7078) | 7078 | `"                else \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L007079](../../agents/web_agent.py#L7079) | 7079 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007080](../../agents/web_agent.py#L7080) | 7080 | `"        report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L007081](../../agents/web_agent.py#L7081) | 7081 | `"        report[\"research_quality\"] = research_quality"` | — |
| [SRC-1AE03B9EC3-L007082](../../agents/web_agent.py#L7082) | 7082 | `"        report[\"research_quality_semantics\"] = \"process_coverage_not_factual_probability\""` | — |
| [SRC-1AE03B9EC3-L007083](../../agents/web_agent.py#L7083) | 7083 | `"        report[\"answer_evidence_status\"] = answer_evidence_status"` | — |
| [SRC-1AE03B9EC3-L007084](../../agents/web_agent.py#L7084) | 7084 | `"        report[\"distinct_registrable_domains\"] = len(distinct_domains)"` | — |
| [SRC-1AE03B9EC3-L007085](../../agents/web_agent.py#L7085) | 7085 | `"        report[\"independent_sources\"] = len(distinct_domains)  # Legacy alias; not editorial independence."` | — |
| [SRC-1AE03B9EC3-L007086](../../agents/web_agent.py#L7086) | 7086 | `"        report[\"independent_sources_field_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L007087](../../agents/web_agent.py#L7087) | 7087 | `"            \"legacy_compatibility_alias_for_distinct_registrable_domain_count\""` | — |
| [SRC-1AE03B9EC3-L007088](../../agents/web_agent.py#L7088) | 7088 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007089](../../agents/web_agent.py#L7089) | 7089 | `"        report[\"source_diversity_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L007090](../../agents/web_agent.py#L7090) | 7090 | `"            \"distinct_registrable_domains_not_editorial_independence\""` | — |
| [SRC-1AE03B9EC3-L007091](../../agents/web_agent.py#L7091) | 7091 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007092](../../agents/web_agent.py#L7092) | 7092 | `"        report[\"editorial_independence_status\"] = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L007093](../../agents/web_agent.py#L7093) | 7093 | `"        report[\"claim_audit_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L007094](../../agents/web_agent.py#L7094) | 7094 | `"            \"distinct_model_assessed_source_support_not_ground_truth\""` | — |
| [SRC-1AE03B9EC3-L007095](../../agents/web_agent.py#L7095) | 7095 | `"            if semantic_claim_verification.get(\"status\") in {"` | — |
| [SRC-1AE03B9EC3-L007096](../../agents/web_agent.py#L7096) | 7096 | `"                \"completed_all_claims_supported\", \"completed_no_factual_claims\""` | — |
| [SRC-1AE03B9EC3-L007097](../../agents/web_agent.py#L7097) | 7097 | `"            }"` | — |
| [SRC-1AE03B9EC3-L007098](../../agents/web_agent.py#L7098) | 7098 | `"            else \"not_verified\""` | — |
| [SRC-1AE03B9EC3-L007099](../../agents/web_agent.py#L7099) | 7099 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007100](../../agents/web_agent.py#L7100) | 7100 | `"        report[\"insufficient_evidence\"] = bool("` | — |
| [SRC-1AE03B9EC3-L007101](../../agents/web_agent.py#L7101) | 7101 | `"            report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES"` | — |
| [SRC-1AE03B9EC3-L007102](../../agents/web_agent.py#L7102) | 7102 | `"            or not sources"` | — |
| [SRC-1AE03B9EC3-L007103](../../agents/web_agent.py#L7103) | 7103 | `"            or semantic_answer_withheld"` | — |
| [SRC-1AE03B9EC3-L007104](../../agents/web_agent.py#L7104) | 7104 | `"            or answer_integrity[\"source_evidence_gap_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L007105](../../agents/web_agent.py#L7105) | 7105 | `"            or ("` | — |
| [SRC-1AE03B9EC3-L007106](../../agents/web_agent.py#L7106) | 7106 | `"                bool(coverage_targets)"` | — |
| [SRC-1AE03B9EC3-L007107](../../agents/web_agent.py#L7107) | 7107 | `"                and answer_integrity[\"potentially_missing_target_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L007108](../../agents/web_agent.py#L7108) | 7108 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007109](../../agents/web_agent.py#L7109) | 7109 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007110](../../agents/web_agent.py#L7110) | 7110 | `"        report[\"valid_citation_range\"] = [1, max_citable_sources] if max_citable_sources else []"` | — |
| [SRC-1AE03B9EC3-L007111](../../agents/web_agent.py#L7111) | 7111 | `"        report[\"citation_count\"] = citation_validation[\"valid_citation_count\"]"` | — |
| [SRC-1AE03B9EC3-L007112](../../agents/web_agent.py#L7112) | 7112 | `"        report[\"citation_check\"] = citation_validation[\"status\"]"` | — |
| [SRC-1AE03B9EC3-L007113](../../agents/web_agent.py#L7113) | 7113 | `"        report[\"citation_validation\"] = citation_validation"` | — |
| [SRC-1AE03B9EC3-L007114](../../agents/web_agent.py#L7114) | 7114 | `"        warnings = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L007115](../../agents/web_agent.py#L7115) | 7115 | `"            search_warnings"` | — |
| [SRC-1AE03B9EC3-L007116](../../agents/web_agent.py#L7116) | 7116 | `"            + ([llm_warning] if llm_warning else [])"` | — |
| [SRC-1AE03B9EC3-L007117](../../agents/web_agent.py#L7117) | 7117 | `"            + ([review_warning] if review_warning else [])"` | — |
| [SRC-1AE03B9EC3-L007118](../../agents/web_agent.py#L7118) | 7118 | `"            + ([coverage_repair_warning] if coverage_repair_warning else [])"` | — |
| [SRC-1AE03B9EC3-L007119](../../agents/web_agent.py#L7119) | 7119 | `"            + citation_warnings"` | — |
| [SRC-1AE03B9EC3-L007120](../../agents/web_agent.py#L7120) | 7120 | `"            + ([uncited_answer_warning] if uncited_answer_warning else [])"` | — |
| [SRC-1AE03B9EC3-L007121](../../agents/web_agent.py#L7121) | 7121 | `"            + (["` | — |
| [SRC-1AE03B9EC3-L007122](../../agents/web_agent.py#L7122) | 7122 | `"                \"حُجبت الإجابة المولدة لعدم اكتمال التحقق الدلالي المستقل عن نموذج الصياغة.\""` | — |
| [SRC-1AE03B9EC3-L007123](../../agents/web_agent.py#L7123) | 7123 | `"            ] if semantic_answer_withheld else [])"` | — |
| [SRC-1AE03B9EC3-L007124](../../agents/web_agent.py#L7124) | 7124 | `"        ))"` | — |
| [SRC-1AE03B9EC3-L007125](../../agents/web_agent.py#L7125) | 7125 | `"        report[\"model_calls\"] = list(self.model_usage)"` | — |
| [SRC-1AE03B9EC3-L007126](../../agents/web_agent.py#L7126) | 7126 | `"        report[\"openrouter_web_search_enabled\"] = self.openrouter_web_search_enabled"` | — |
| [SRC-1AE03B9EC3-L007127](../../agents/web_agent.py#L7127) | 7127 | `"        report[\"openrouter_web_search_results\"] = len(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L007128](../../agents/web_agent.py#L7128) | 7128 | `"        if semantic_answer_withheld:"` | — |
| [SRC-1AE03B9EC3-L007129](../../agents/web_agent.py#L7129) | 7129 | `"            final_answer_status = \"semantic_verification_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L007130](../../agents/web_agent.py#L7130) | 7130 | `"        elif generation_budget_exhausted or review_budget_exhausted:"` | — |
| [SRC-1AE03B9EC3-L007131](../../agents/web_agent.py#L7131) | 7131 | `"            final_answer_status = \"budget_exhausted_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L007132](../../agents/web_agent.py#L7132) | 7132 | `"        elif llm_warning:"` | — |
| [SRC-1AE03B9EC3-L007133](../../agents/web_agent.py#L7133) | 7133 | `"            final_answer_status = ("` | — |
| [SRC-1AE03B9EC3-L007134](../../agents/web_agent.py#L7134) | 7134 | `"                \"model_not_configured_fallback\""` | — |
| [SRC-1AE03B9EC3-L007135](../../agents/web_agent.py#L7135) | 7135 | `"                if not self.api_key"` | — |
| [SRC-1AE03B9EC3-L007136](../../agents/web_agent.py#L7136) | 7136 | `"                else \"generation_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L007137](../../agents/web_agent.py#L7137) | 7137 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007138](../../agents/web_agent.py#L7138) | 7138 | `"        elif review_warning:"` | — |
| [SRC-1AE03B9EC3-L007139](../../agents/web_agent.py#L7139) | 7139 | `"            final_answer_status = \"review_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L007140](../../agents/web_agent.py#L7140) | 7140 | `"        elif coverage_repair_status == \"no_change_gap_unresolved\":"` | — |
| [SRC-1AE03B9EC3-L007141](../../agents/web_agent.py#L7141) | 7141 | `"            final_answer_status = \"coverage_repair_left_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L007142](../../agents/web_agent.py#L7142) | 7142 | `"        elif coverage_repair_status == \"budget_exhausted\":"` | — |
| [SRC-1AE03B9EC3-L007143](../../agents/web_agent.py#L7143) | 7143 | `"            final_answer_status = \"coverage_repair_budget_exhausted_with_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L007144](../../agents/web_agent.py#L7144) | 7144 | `"        elif coverage_repair_status == \"unavailable\":"` | — |
| [SRC-1AE03B9EC3-L007145](../../agents/web_agent.py#L7145) | 7145 | `"            final_answer_status = \"coverage_repair_unavailable_with_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L007146](../../agents/web_agent.py#L7146) | 7146 | `"        elif used_llm:"` | — |
| [SRC-1AE03B9EC3-L007147](../../agents/web_agent.py#L7147) | 7147 | `"            final_answer_status = \"model_answer_generated\""` | — |
| [SRC-1AE03B9EC3-L007148](../../agents/web_agent.py#L7148) | 7148 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L007149](../../agents/web_agent.py#L7149) | 7149 | `"            final_answer_status = \"source_fallback\""` | — |
| [SRC-1AE03B9EC3-L007150](../../agents/web_agent.py#L7150) | 7150 | `""` | — |
| [SRC-1AE03B9EC3-L007151](../../agents/web_agent.py#L7151) | 7151 | `"        # Report pipeline completion separately from factual correctness. A successful"` | — |
| [SRC-1AE03B9EC3-L007152](../../agents/web_agent.py#L7152) | 7152 | `"        # retrieval or model review is not an independent semantic fact check."` | — |
| [SRC-1AE03B9EC3-L007153](../../agents/web_agent.py#L7153) | 7153 | `"        if report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES:"` | — |
| [SRC-1AE03B9EC3-L007154](../../agents/web_agent.py#L7154) | 7154 | `"            pipeline_completion_status = \"execution_failed\""` | — |
| [SRC-1AE03B9EC3-L007155](../../agents/web_agent.py#L7155) | 7155 | `"        elif not search_attempted:"` | — |
| [SRC-1AE03B9EC3-L007156](../../agents/web_agent.py#L7156) | 7156 | `"            pipeline_completion_status = \"not_verified\""` | — |
| [SRC-1AE03B9EC3-L007157](../../agents/web_agent.py#L7157) | 7157 | `"        elif not sources:"` | — |
| [SRC-1AE03B9EC3-L007158](../../agents/web_agent.py#L7158) | 7158 | `"            pipeline_completion_status = \"insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L007159](../../agents/web_agent.py#L7159) | 7159 | `"        elif ("` | — |
| [SRC-1AE03B9EC3-L007160](../../agents/web_agent.py#L7160) | 7160 | `"            llm_warning"` | — |
| [SRC-1AE03B9EC3-L007161](../../agents/web_agent.py#L7161) | 7161 | `"            or review_warning"` | — |
| [SRC-1AE03B9EC3-L007162](../../agents/web_agent.py#L7162) | 7162 | `"            or review_status != \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L007163](../../agents/web_agent.py#L7163) | 7163 | `"            or answer_integrity[\"potentially_missing_target_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L007164](../../agents/web_agent.py#L7164) | 7164 | `"            or answer_integrity[\"source_evidence_gap_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L007165](../../agents/web_agent.py#L7165) | 7165 | `"            or citation_validation[\"valid_citation_count\"] == 0"` | — |
| [SRC-1AE03B9EC3-L007166](../../agents/web_agent.py#L7166) | 7166 | `"            or semantic_answer_withheld"` | — |
| [SRC-1AE03B9EC3-L007167](../../agents/web_agent.py#L7167) | 7167 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L007168](../../agents/web_agent.py#L7168) | 7168 | `"            pipeline_completion_status = \"partial\""` | — |
| [SRC-1AE03B9EC3-L007169](../../agents/web_agent.py#L7169) | 7169 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L007170](../../agents/web_agent.py#L7170) | 7170 | `"            pipeline_completion_status = \"completed\""` | — |
| [SRC-1AE03B9EC3-L007171](../../agents/web_agent.py#L7171) | 7171 | `"        completion_stages = {"` | — |
| [SRC-1AE03B9EC3-L007172](../../agents/web_agent.py#L7172) | 7172 | `"            \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L007173](../../agents/web_agent.py#L7173) | 7173 | `"            \"accepted_sources\": len(sources),"` | — |
| [SRC-1AE03B9EC3-L007174](../../agents/web_agent.py#L7174) | 7174 | `"            \"pages_read\": fetched_pages,"` | — |
| [SRC-1AE03B9EC3-L007175](../../agents/web_agent.py#L7175) | 7175 | `"            \"answer_generated_by_model\": bool(used_llm),"` | — |
| [SRC-1AE03B9EC3-L007176](../../agents/web_agent.py#L7176) | 7176 | `"            \"claim_review\": review_status,"` | — |
| [SRC-1AE03B9EC3-L007177](../../agents/web_agent.py#L7177) | 7177 | `"            \"valid_citations\": citation_validation[\"valid_citation_count\"],"` | — |
| [SRC-1AE03B9EC3-L007178](../../agents/web_agent.py#L7178) | 7178 | `"            \"semantic_fact_check\": \"not_performed\","` | — |
| [SRC-1AE03B9EC3-L007179](../../agents/web_agent.py#L7179) | 7179 | `"            \"semantic_claim_support_assessment\": semantic_claim_verification.get(\"status\", \"not_performed\"),"` | — |
| [SRC-1AE03B9EC3-L007180](../../agents/web_agent.py#L7180) | 7180 | `"        }"` | — |
| [SRC-1AE03B9EC3-L007181](../../agents/web_agent.py#L7181) | 7181 | `"        if semantic_answer_withheld:"` | — |
| [SRC-1AE03B9EC3-L007182](../../agents/web_agent.py#L7182) | 7182 | `"            pipeline_completion_status = \"partial\""` | — |
| [SRC-1AE03B9EC3-L007183](../../agents/web_agent.py#L7183) | 7183 | `"        report[\"pipeline_completion_status\"] = pipeline_completion_status"` | — |
| [SRC-1AE03B9EC3-L007184](../../agents/web_agent.py#L7184) | 7184 | `"        report[\"completion_stages\"] = completion_stages"` | — |
| [SRC-1AE03B9EC3-L007185](../../agents/web_agent.py#L7185) | 7185 | `"        report[\"pipeline_completion_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L007186](../../agents/web_agent.py#L7186) | 7186 | `"            \"pipeline stage completion only; not a guarantee of factual correctness\""` | — |
| [SRC-1AE03B9EC3-L007187](../../agents/web_agent.py#L7187) | 7187 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007188](../../agents/web_agent.py#L7188) | 7188 | `""` | — |
| [SRC-1AE03B9EC3-L007189](../../agents/web_agent.py#L7189) | 7189 | `"        public_sources = []"` | — |
| [SRC-1AE03B9EC3-L007190](../../agents/web_agent.py#L7190) | 7190 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L007191](../../agents/web_agent.py#L7191) | 7191 | `"            public_sources.append({"` | — |
| [SRC-1AE03B9EC3-L007192](../../agents/web_agent.py#L7192) | 7192 | `"                \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L007193](../../agents/web_agent.py#L7193) | 7193 | `"                \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L007194](../../agents/web_agent.py#L7194) | 7194 | `"                \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007195](../../agents/web_agent.py#L7195) | 7195 | `"                \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L007196](../../agents/web_agent.py#L7196) | 7196 | `"                \"readable_page_text_available\": bool(source.get(\"page_fetched\")) and bool(str(source.get(\"page_text\") or \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L007197](../../agents/web_agent.py#L7197) | 7197 | `"                \"page_text_present_without_fetch_flag\": bool(str(source.get(\"page_text\") or \"\").strip()) and not bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L007198](../../agents/web_agent.py#L7198) | 7198 | `"                \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L007199](../../agents/web_agent.py#L7199) | 7199 | `"                \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L007200](../../agents/web_agent.py#L7200) | 7200 | `"                \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L007201](../../agents/web_agent.py#L7201) | 7201 | `"                \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007202](../../agents/web_agent.py#L7202) | 7202 | `"                \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L007203](../../agents/web_agent.py#L7203) | 7203 | `"                \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007204](../../agents/web_agent.py#L7204) | 7204 | `"                \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007205](../../agents/web_agent.py#L7205) | 7205 | `"                \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007206](../../agents/web_agent.py#L7206) | 7206 | `"                \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L007207](../../agents/web_agent.py#L7207) | 7207 | `"                \"lead_qualification\": source.get(\"lead_qualification\"),"` | — |
| [SRC-1AE03B9EC3-L007208](../../agents/web_agent.py#L7208) | 7208 | `"                \"lead_intent_evidence\": source.get(\"lead_intent_evidence\"),"` | — |
| [SRC-1AE03B9EC3-L007209](../../agents/web_agent.py#L7209) | 7209 | `"            })"` | — |
| [SRC-1AE03B9EC3-L007210](../../agents/web_agent.py#L7210) | 7210 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L007211](../../agents/web_agent.py#L7211) | 7211 | `"            \"answer\": answer,"` | — |
| [SRC-1AE03B9EC3-L007212](../../agents/web_agent.py#L7212) | 7212 | `"            \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L007213](../../agents/web_agent.py#L7213) | 7213 | `"            \"search_query\": (plan.get(\"queries\") or [\"\"])[0],"` | — |
| [SRC-1AE03B9EC3-L007214](../../agents/web_agent.py#L7214) | 7214 | `"            \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L007215](../../agents/web_agent.py#L7215) | 7215 | `"            \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L007216](../../agents/web_agent.py#L7216) | 7216 | `"                \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L007217](../../agents/web_agent.py#L7217) | 7217 | `"                \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L007218](../../agents/web_agent.py#L7218) | 7218 | `"                \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L007219](../../agents/web_agent.py#L7219) | 7219 | `"                \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L007220](../../agents/web_agent.py#L7220) | 7220 | `"                \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L007221](../../agents/web_agent.py#L7221) | 7221 | `"                \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L007222](../../agents/web_agent.py#L7222) | 7222 | `"                \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L007223](../../agents/web_agent.py#L7223) | 7223 | `"                \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L007224](../../agents/web_agent.py#L7224) | 7224 | `"                \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L007225](../../agents/web_agent.py#L7225) | 7225 | `"                \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L007226](../../agents/web_agent.py#L7226) | 7226 | `"            },"` | — |
| [SRC-1AE03B9EC3-L007227](../../agents/web_agent.py#L7227) | 7227 | `"            \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L007228](../../agents/web_agent.py#L7228) | 7228 | `"            \"sources\": public_sources,"` | — |
| [SRC-1AE03B9EC3-L007229](../../agents/web_agent.py#L7229) | 7229 | `"            \"research_quality\": research_quality,"` | — |
| [SRC-1AE03B9EC3-L007230](../../agents/web_agent.py#L7230) | 7230 | `"            \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L007231](../../agents/web_agent.py#L7231) | 7231 | `"            \"answer_evidence_status\": answer_evidence_status,"` | — |
| [SRC-1AE03B9EC3-L007232](../../agents/web_agent.py#L7232) | 7232 | `"            \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L007233](../../agents/web_agent.py#L7233) | 7233 | `"            \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L007234](../../agents/web_agent.py#L7234) | 7234 | `"            \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L007235](../../agents/web_agent.py#L7235) | 7235 | `"            \"coverage_repair_status\": coverage_repair_status,"` | — |
| [SRC-1AE03B9EC3-L007236](../../agents/web_agent.py#L7236) | 7236 | `"            \"used_language_model\": used_llm,"` | — |
| [SRC-1AE03B9EC3-L007237](../../agents/web_agent.py#L7237) | 7237 | `"            \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L007238](../../agents/web_agent.py#L7238) | 7238 | `"            \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L007239](../../agents/web_agent.py#L7239) | 7239 | `"            \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L007240](../../agents/web_agent.py#L7240) | 7240 | `"            \"warnings\": warnings,"` | — |
| [SRC-1AE03B9EC3-L007241](../../agents/web_agent.py#L7241) | 7241 | `"            \"kind\": \"web_research\" if used_llm else \"web_fallback\","` | — |
| [SRC-1AE03B9EC3-L007242](../../agents/web_agent.py#L7242) | 7242 | `"            \"final_answer_status\": final_answer_status,"` | — |
| [SRC-1AE03B9EC3-L007243](../../agents/web_agent.py#L7243) | 7243 | `"            \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L007244](../../agents/web_agent.py#L7244) | 7244 | `"            \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L007245](../../agents/web_agent.py#L7245) | 7245 | `"        }"` | — |
| [SRC-1AE03B9EC3-L007246](../../agents/web_agent.py#L7246) | 7246 | `""` | — |
| [SRC-1AE03B9EC3-L007247](../../agents/web_agent.py#L7247) | 7247 | `"def _normalized_provider_usage("` | — |
| [SRC-1AE03B9EC3-L007248](../../agents/web_agent.py#L7248) | 7248 | `"    usage: Any, *, provider_base_url: str = \"\""` | — |
| [SRC-1AE03B9EC3-L007249](../../agents/web_agent.py#L7249) | 7249 | `") -> dict[str, int \| float] \| None:"` | — |
| [SRC-1AE03B9EC3-L007250](../../agents/web_agent.py#L7250) | 7250 | `"    \"\"\"Allowlist safe counters; interpret generic 'cost' as USD only for OpenRouter.\"\"\""` | — |
| [SRC-1AE03B9EC3-L007251](../../agents/web_agent.py#L7251) | 7251 | `"    if not isinstance(usage, dict):"` | — |
| [SRC-1AE03B9EC3-L007252](../../agents/web_agent.py#L7252) | 7252 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L007253](../../agents/web_agent.py#L7253) | 7253 | `"    normalized: dict[str, int \| float] = {}"` | — |
| [SRC-1AE03B9EC3-L007254](../../agents/web_agent.py#L7254) | 7254 | `"    for source_key in (\"prompt_tokens\", \"completion_tokens\", \"total_tokens\"):"` | — |
| [SRC-1AE03B9EC3-L007255](../../agents/web_agent.py#L7255) | 7255 | `"        value = usage.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L007256](../../agents/web_agent.py#L7256) | 7256 | `"        if isinstance(value, int) and not isinstance(value, bool) and value >= 0:"` | — |
| [SRC-1AE03B9EC3-L007257](../../agents/web_agent.py#L7257) | 7257 | `"            normalized[source_key] = value"` | — |
| [SRC-1AE03B9EC3-L007258](../../agents/web_agent.py#L7258) | 7258 | `"    cost_keys = [\"cost_usd\"]"` | — |
| [SRC-1AE03B9EC3-L007259](../../agents/web_agent.py#L7259) | 7259 | `"    provider_host = \"\""` | — |
| [SRC-1AE03B9EC3-L007260](../../agents/web_agent.py#L7260) | 7260 | `"    if isinstance(provider_base_url, str):"` | — |
| [SRC-1AE03B9EC3-L007261](../../agents/web_agent.py#L7261) | 7261 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L007262](../../agents/web_agent.py#L7262) | 7262 | `"            provider_host = (urllib.parse.urlsplit(provider_base_url.strip()).hostname or \"\").lower().rstrip(\".\")"` | — |
| [SRC-1AE03B9EC3-L007263](../../agents/web_agent.py#L7263) | 7263 | `"        except ValueError:"` | — |
| [SRC-1AE03B9EC3-L007264](../../agents/web_agent.py#L7264) | 7264 | `"            provider_host = \"\""` | — |
| [SRC-1AE03B9EC3-L007265](../../agents/web_agent.py#L7265) | 7265 | `"    is_openrouter = ("` | — |
| [SRC-1AE03B9EC3-L007266](../../agents/web_agent.py#L7266) | 7266 | `"        provider_host == \"openrouter.ai\""` | — |
| [SRC-1AE03B9EC3-L007267](../../agents/web_agent.py#L7267) | 7267 | `"        or provider_host.endswith(\".openrouter.ai\")"` | — |
| [SRC-1AE03B9EC3-L007268](../../agents/web_agent.py#L7268) | 7268 | `"    )"` | — |
| [SRC-1AE03B9EC3-L007269](../../agents/web_agent.py#L7269) | 7269 | `"    if is_openrouter:"` | — |
| [SRC-1AE03B9EC3-L007270](../../agents/web_agent.py#L7270) | 7270 | `"        cost_keys.extend([\"cost\", \"total_cost\"])"` | — |
| [SRC-1AE03B9EC3-L007271](../../agents/web_agent.py#L7271) | 7271 | `"    for source_key in cost_keys:"` | — |
| [SRC-1AE03B9EC3-L007272](../../agents/web_agent.py#L7272) | 7272 | `"        value = usage.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L007273](../../agents/web_agent.py#L7273) | 7273 | `"        if isinstance(value, (int, float)) and not isinstance(value, bool):"` | — |
| [SRC-1AE03B9EC3-L007274](../../agents/web_agent.py#L7274) | 7274 | `"            number = float(value)"` | — |
| [SRC-1AE03B9EC3-L007275](../../agents/web_agent.py#L7275) | 7275 | `"            if number >= 0 and math.isfinite(number):"` | — |
| [SRC-1AE03B9EC3-L007276](../../agents/web_agent.py#L7276) | 7276 | `"                normalized[\"cost_usd\"] = number"` | — |
| [SRC-1AE03B9EC3-L007277](../../agents/web_agent.py#L7277) | 7277 | `"                break"` | — |
| [SRC-1AE03B9EC3-L007278](../../agents/web_agent.py#L7278) | 7278 | `"    return normalized or None"` | — |
| [SRC-1AE03B9EC3-L007279](../../agents/web_agent.py#L7279) | 7279 | `""` | — |
| [SRC-1AE03B9EC3-L007280](../../agents/web_agent.py#L7280) | 7280 | `"def _model_usage_record("` | — |
| [SRC-1AE03B9EC3-L007281](../../agents/web_agent.py#L7281) | 7281 | `"    requested_model: str,"` | — |
| [SRC-1AE03B9EC3-L007282](../../agents/web_agent.py#L7282) | 7282 | `"    candidate_model: str,"` | — |
| [SRC-1AE03B9EC3-L007283](../../agents/web_agent.py#L7283) | 7283 | `"    response_data: dict[str, Any],"` | — |
| [SRC-1AE03B9EC3-L007284](../../agents/web_agent.py#L7284) | 7284 | `"    provider_base_url: str,"` | — |
| [SRC-1AE03B9EC3-L007285](../../agents/web_agent.py#L7285) | 7285 | `") -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L007286](../../agents/web_agent.py#L7286) | 7286 | `"    \"\"\"Return only allowlisted provider usage metadata, never raw prompts/responses.\"\"\""` | — |
| [SRC-1AE03B9EC3-L007287](../../agents/web_agent.py#L7287) | 7287 | `"    record: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L007288](../../agents/web_agent.py#L7288) | 7288 | `"        \"requested_model\": requested_model,"` | — |
| [SRC-1AE03B9EC3-L007289](../../agents/web_agent.py#L7289) | 7289 | `"        \"used_model\": candidate_model,"` | — |
| [SRC-1AE03B9EC3-L007290](../../agents/web_agent.py#L7290) | 7290 | `"        \"fallback_used\": \"true\" if candidate_model != requested_model else \"false\","` | — |
| [SRC-1AE03B9EC3-L007291](../../agents/web_agent.py#L7291) | 7291 | `"    }"` | — |
| [SRC-1AE03B9EC3-L007292](../../agents/web_agent.py#L7292) | 7292 | `"    provider_usage = _normalized_provider_usage("` | — |
| [SRC-1AE03B9EC3-L007293](../../agents/web_agent.py#L7293) | 7293 | `"        response_data.get(\"usage\"), provider_base_url=provider_base_url"` | — |
| [SRC-1AE03B9EC3-L007294](../../agents/web_agent.py#L7294) | 7294 | `"    )"` | — |
| [SRC-1AE03B9EC3-L007295](../../agents/web_agent.py#L7295) | 7295 | `"    if provider_usage is not None:"` | — |
| [SRC-1AE03B9EC3-L007296](../../agents/web_agent.py#L7296) | 7296 | `"        record[\"provider_usage\"] = provider_usage"` | — |
| [SRC-1AE03B9EC3-L007297](../../agents/web_agent.py#L7297) | 7297 | `"    return record"` | — |
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
| [SRC-EEF2E6447C-L000357](../../api/omarai.py#L357) | 357 | `"                # GET/HEAD/other methods are not allowed to leave unread bytes"` | — |
| [SRC-EEF2E6447C-L000358](../../api/omarai.py#L358) | 358 | `"                # on a persistent connection."` | — |
| [SRC-EEF2E6447C-L000359](../../api/omarai.py#L359) | 359 | `"                self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000360](../../api/omarai.py#L360) | 360 | `"                self.send_error(400, \"Content-Length body is not supported for this method\")"` | — |
| [SRC-EEF2E6447C-L000361](../../api/omarai.py#L361) | 361 | `"                return False"` | — |
| [SRC-EEF2E6447C-L000362](../../api/omarai.py#L362) | 362 | `""` | — |
| [SRC-EEF2E6447C-L000363](../../api/omarai.py#L363) | 363 | `"        return True"` | — |
| [SRC-EEF2E6447C-L000364](../../api/omarai.py#L364) | 364 | `""` | — |
| [SRC-EEF2E6447C-L000365](../../api/omarai.py#L365) | 365 | `"    store = _lead_store_from_environment()"` | — |
| [SRC-EEF2E6447C-L000366](../../api/omarai.py#L366) | 366 | `"    _rate_lock = threading.Lock()"` | — |
| [SRC-EEF2E6447C-L000367](../../api/omarai.py#L367) | 367 | `"    _request_times: ClassVar[dict[str, deque[float]]] = defaultdict(deque)"` | — |
| [SRC-EEF2E6447C-L000368](../../api/omarai.py#L368) | 368 | `"    _rate_last_cleanup: ClassVar[float] = 0.0"` | — |
| [SRC-EEF2E6447C-L000369](../../api/omarai.py#L369) | 369 | `"    RATE_LIMIT_REQUESTS = 20"` | — |
| [SRC-EEF2E6447C-L000370](../../api/omarai.py#L370) | 370 | `"    RATE_LIMIT_WINDOW_SECONDS = 60"` | — |
| [SRC-EEF2E6447C-L000371](../../api/omarai.py#L371) | 371 | `"    RATE_LIMIT_CLEANUP_INTERVAL_SECONDS = 60"` | — |
| [SRC-EEF2E6447C-L000372](../../api/omarai.py#L372) | 372 | `"    # Reserve the final bucket for clients beyond the per-process tracking ceiling."` | — |
| [SRC-EEF2E6447C-L000373](../../api/omarai.py#L373) | 373 | `"    MAX_RATE_LIMIT_CLIENT_BUCKETS = 4096"` | — |
| [SRC-EEF2E6447C-L000374](../../api/omarai.py#L374) | 374 | `"    RATE_LIMIT_OVERFLOW_KEY = \"__omarai_overflow__\""` | — |
| [SRC-EEF2E6447C-L000375](../../api/omarai.py#L375) | 375 | `"    AGENT_CONCURRENCY_LIMIT = _configured_agent_concurrency_limit()"` | — |
| [SRC-EEF2E6447C-L000376](../../api/omarai.py#L376) | 376 | `"    _agent_semaphore = threading.BoundedSemaphore(AGENT_CONCURRENCY_LIMIT)"` | — |
| [SRC-EEF2E6447C-L000377](../../api/omarai.py#L377) | 377 | `""` | — |
| [SRC-EEF2E6447C-L000378](../../api/omarai.py#L378) | 378 | `"    def _run_bounded_agent_operation(self, operation):"` | — |
| [SRC-EEF2E6447C-L000379](../../api/omarai.py#L379) | 379 | `"        \"\"\"Run an expensive operation only when a process-local slot is available.\"\"\""` | — |
| [SRC-EEF2E6447C-L000380](../../api/omarai.py#L380) | 380 | `"        cls = type(self)"` | — |
| [SRC-EEF2E6447C-L000381](../../api/omarai.py#L381) | 381 | `"        if not cls._agent_semaphore.acquire(blocking=False):"` | — |
| [SRC-EEF2E6447C-L000382](../../api/omarai.py#L382) | 382 | `"            return self.respond("` | — |
| [SRC-EEF2E6447C-L000383](../../api/omarai.py#L383) | 383 | `"                503,"` | — |
| [SRC-EEF2E6447C-L000384](../../api/omarai.py#L384) | 384 | `"                {"` | — |
| [SRC-EEF2E6447C-L000385](../../api/omarai.py#L385) | 385 | `"                    \"error\": \"خدمة البحث مشغولة حاليًا؛ أعد المحاولة بعد قليل.\","` | — |
| [SRC-EEF2E6447C-L000386](../../api/omarai.py#L386) | 386 | `"                    \"retry_after_seconds\": 5,"` | — |
| [SRC-EEF2E6447C-L000387](../../api/omarai.py#L387) | 387 | `"                    \"process_concurrency_limit\": cls.AGENT_CONCURRENCY_LIMIT,"` | — |
| [SRC-EEF2E6447C-L000388](../../api/omarai.py#L388) | 388 | `"                },"` | — |
| [SRC-EEF2E6447C-L000389](../../api/omarai.py#L389) | 389 | `"            )"` | — |
| [SRC-EEF2E6447C-L000390](../../api/omarai.py#L390) | 390 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000391](../../api/omarai.py#L391) | 391 | `"            return self.respond(200, operation())"` | — |
| [SRC-EEF2E6447C-L000392](../../api/omarai.py#L392) | 392 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000393](../../api/omarai.py#L393) | 393 | `"            cls._agent_semaphore.release()"` | — |
| [SRC-EEF2E6447C-L000394](../../api/omarai.py#L394) | 394 | `""` | — |
| [SRC-EEF2E6447C-L000395](../../api/omarai.py#L395) | 395 | `"    def _session_cookie_name(self):"` | — |
| [SRC-EEF2E6447C-L000396](../../api/omarai.py#L396) | 396 | `"        \"\"\"Use the __Host- prefix on HTTPS public deployments.\"\"\""` | — |
| [SRC-EEF2E6447C-L000397](../../api/omarai.py#L397) | 397 | `"        if os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() == \"1\":"` | — |
| [SRC-EEF2E6447C-L000398](../../api/omarai.py#L398) | 398 | `"            return \"__Host-omarai_session\""` | — |
| [SRC-EEF2E6447C-L000399](../../api/omarai.py#L399) | 399 | `"        return \"omarai_session\""` | — |
| [SRC-EEF2E6447C-L000400](../../api/omarai.py#L400) | 400 | `""` | — |
| [SRC-EEF2E6447C-L000401](../../api/omarai.py#L401) | 401 | `"    def _session_cookie_header(self, token: str) -> str:"` | — |
| [SRC-EEF2E6447C-L000402](../../api/omarai.py#L402) | 402 | `"        if not BROWSER_SESSION_ID_RE.fullmatch(token):"` | — |
| [SRC-EEF2E6447C-L000403](../../api/omarai.py#L403) | 403 | `"            raise ValueError(\"browser access token has an unsupported format\")"` | — |
| [SRC-EEF2E6447C-L000404](../../api/omarai.py#L404) | 404 | `"        parts = ["` | — |
| [SRC-EEF2E6447C-L000405](../../api/omarai.py#L405) | 405 | `"            f\"{self._session_cookie_name()}={token}\","` | — |
| [SRC-EEF2E6447C-L000406](../../api/omarai.py#L406) | 406 | `"            \"Path=/\","` | — |
| [SRC-EEF2E6447C-L000407](../../api/omarai.py#L407) | 407 | `"            \"HttpOnly\","` | — |
| [SRC-EEF2E6447C-L000408](../../api/omarai.py#L408) | 408 | `"            \"SameSite=Strict\","` | — |
| [SRC-EEF2E6447C-L000409](../../api/omarai.py#L409) | 409 | `"            f\"Max-Age={BROWSER_SESSION_COOKIE_MAX_AGE}\","` | — |
| [SRC-EEF2E6447C-L000410](../../api/omarai.py#L410) | 410 | `"        ]"` | — |
| [SRC-EEF2E6447C-L000411](../../api/omarai.py#L411) | 411 | `"        if os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() == \"1\":"` | — |
| [SRC-EEF2E6447C-L000412](../../api/omarai.py#L412) | 412 | `"            parts.insert(2, \"Secure\")"` | — |
| [SRC-EEF2E6447C-L000413](../../api/omarai.py#L413) | 413 | `"        return \"; \".join(parts)"` | — |
| [SRC-EEF2E6447C-L000414](../../api/omarai.py#L414) | 414 | `""` | — |
| [SRC-EEF2E6447C-L000415](../../api/omarai.py#L415) | 415 | `"    def _clear_session_cookie_header(self) -> str:"` | — |
| [SRC-EEF2E6447C-L000416](../../api/omarai.py#L416) | 416 | `"        parts = ["` | — |
| [SRC-EEF2E6447C-L000417](../../api/omarai.py#L417) | 417 | `"            f\"{self._session_cookie_name()}=\","` | — |
| [SRC-EEF2E6447C-L000418](../../api/omarai.py#L418) | 418 | `"            \"Path=/\","` | — |
| [SRC-EEF2E6447C-L000419](../../api/omarai.py#L419) | 419 | `"            \"HttpOnly\","` | — |
| [SRC-EEF2E6447C-L000420](../../api/omarai.py#L420) | 420 | `"            \"SameSite=Strict\","` | — |
| [SRC-EEF2E6447C-L000421](../../api/omarai.py#L421) | 421 | `"            \"Max-Age=0\","` | — |
| [SRC-EEF2E6447C-L000422](../../api/omarai.py#L422) | 422 | `"        ]"` | — |
| [SRC-EEF2E6447C-L000423](../../api/omarai.py#L423) | 423 | `"        if os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() == \"1\":"` | — |
| [SRC-EEF2E6447C-L000424](../../api/omarai.py#L424) | 424 | `"            parts.insert(2, \"Secure\")"` | — |
| [SRC-EEF2E6447C-L000425](../../api/omarai.py#L425) | 425 | `"        return \"; \".join(parts)"` | — |
| [SRC-EEF2E6447C-L000426](../../api/omarai.py#L426) | 426 | `""` | — |
| [SRC-EEF2E6447C-L000427](../../api/omarai.py#L427) | 427 | `"    def _principal_for_access_token(self, token: str):"` | — |
| [SRC-EEF2E6447C-L000428](../../api/omarai.py#L428) | 428 | `"        expected = os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000429](../../api/omarai.py#L429) | 429 | `"        if expected and hmac.compare_digest(token, expected):"` | — |
| [SRC-EEF2E6447C-L000430](../../api/omarai.py#L430) | 430 | `"            return self.store.default_principal()"` | — |
| [SRC-EEF2E6447C-L000431](../../api/omarai.py#L431) | 431 | `"        return self.store.resolve_api_token(token)"` | — |
| [SRC-EEF2E6447C-L000432](../../api/omarai.py#L432) | 432 | `""` | — |
| [SRC-EEF2E6447C-L000433](../../api/omarai.py#L433) | 433 | `"    _FORWARDING_HEADERS = ("` | — |
| [SRC-EEF2E6447C-L000434](../../api/omarai.py#L434) | 434 | `"        \"X-Forwarded-For\", \"X-Forwarded-Host\", \"X-Forwarded-Proto\","` | — |
| [SRC-EEF2E6447C-L000435](../../api/omarai.py#L435) | 435 | `"        \"X-Real-IP\", \"Forwarded\", \"CF-Connecting-IP\", \"True-Client-IP\","` | — |
| [SRC-EEF2E6447C-L000436](../../api/omarai.py#L436) | 436 | `"    )"` | — |
| [SRC-EEF2E6447C-L000437](../../api/omarai.py#L437) | 437 | `""` | — |
| [SRC-EEF2E6447C-L000438](../../api/omarai.py#L438) | 438 | `"    def _has_forwarding_headers(self) -> bool:"` | — |
| [SRC-EEF2E6447C-L000439](../../api/omarai.py#L439) | 439 | `"        return any(self.headers.get(name) for name in self._FORWARDING_HEADERS)"` | — |
| [SRC-EEF2E6447C-L000440](../../api/omarai.py#L440) | 440 | `""` | — |
| [SRC-EEF2E6447C-L000441](../../api/omarai.py#L441) | 441 | `"    def _authorized(self):"` | — |
| [SRC-EEF2E6447C-L000442](../../api/omarai.py#L442) | 442 | `"        \"\"\"Resolve a verified bearer token or HttpOnly browser cookie."` | — |
| [SRC-EEF2E6447C-L000443](../../api/omarai.py#L443) | 443 | `""` | — |
| [SRC-EEF2E6447C-L000444](../../api/omarai.py#L444) | 444 | `"        Browser cookies are accepted only with same-origin POST requests. Request-body"` | — |
| [SRC-EEF2E6447C-L000445](../../api/omarai.py#L445) | 445 | `"        tenant IDs are never used to establish tenant context."` | — |
| [SRC-EEF2E6447C-L000446](../../api/omarai.py#L446) | 446 | `"        \"\"\""` | — |
| [SRC-EEF2E6447C-L000447](../../api/omarai.py#L447) | 447 | `"        self._authenticated_principal = None"` | — |
| [SRC-EEF2E6447C-L000448](../../api/omarai.py#L448) | 448 | `"        self._cookie_authenticated = False"` | — |
| [SRC-EEF2E6447C-L000449](../../api/omarai.py#L449) | 449 | `"        self._browser_session_id = \"\""` | — |
| [SRC-EEF2E6447C-L000450](../../api/omarai.py#L450) | 450 | `"        supplied = self.headers.get(\"Authorization\", \"\")"` | — |
| [SRC-EEF2E6447C-L000451](../../api/omarai.py#L451) | 451 | `"        if supplied.startswith(\"Bearer \"):"` | — |
| [SRC-EEF2E6447C-L000452](../../api/omarai.py#L452) | 452 | `"            token = supplied[7:].strip()"` | — |
| [SRC-EEF2E6447C-L000453](../../api/omarai.py#L453) | 453 | `"            self._authenticated_principal = self._principal_for_access_token(token)"` | — |
| [SRC-EEF2E6447C-L000454](../../api/omarai.py#L454) | 454 | `"            return bool(self._authenticated_principal)"` | — |
| [SRC-EEF2E6447C-L000455](../../api/omarai.py#L455) | 455 | `""` | — |
| [SRC-EEF2E6447C-L000456](../../api/omarai.py#L456) | 456 | `"        cookie = SimpleCookie()"` | — |
| [SRC-EEF2E6447C-L000457](../../api/omarai.py#L457) | 457 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000458](../../api/omarai.py#L458) | 458 | `"            cookie.load(self.headers.get(\"Cookie\", \"\"))"` | — |
| [SRC-EEF2E6447C-L000459](../../api/omarai.py#L459) | 459 | `"        except Exception:"` | — |
| [SRC-EEF2E6447C-L000460](../../api/omarai.py#L460) | 460 | `"            cookie = SimpleCookie()"` | — |
| [SRC-EEF2E6447C-L000461](../../api/omarai.py#L461) | 461 | `"        morsel = cookie.get(self._session_cookie_name())"` | — |
| [SRC-EEF2E6447C-L000462](../../api/omarai.py#L462) | 462 | `"        if morsel is not None:"` | — |
| [SRC-EEF2E6447C-L000463](../../api/omarai.py#L463) | 463 | `"            token = morsel.value"` | — |
| [SRC-EEF2E6447C-L000464](../../api/omarai.py#L464) | 464 | `"            if BROWSER_SESSION_ID_RE.fullmatch(token):"` | — |
| [SRC-EEF2E6447C-L000465](../../api/omarai.py#L465) | 465 | `"                self._authenticated_principal = self.store.resolve_web_session("` | — |
| [SRC-EEF2E6447C-L000466](../../api/omarai.py#L466) | 466 | `"                    token,"` | — |
| [SRC-EEF2E6447C-L000467](../../api/omarai.py#L467) | 467 | `"                    shared_token=os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip(),"` | — |
| [SRC-EEF2E6447C-L000468](../../api/omarai.py#L468) | 468 | `"                )"` | — |
| [SRC-EEF2E6447C-L000469](../../api/omarai.py#L469) | 469 | `"                self._cookie_authenticated = bool(self._authenticated_principal)"` | — |
| [SRC-EEF2E6447C-L000470](../../api/omarai.py#L470) | 470 | `"                if self._cookie_authenticated:"` | — |
| [SRC-EEF2E6447C-L000471](../../api/omarai.py#L471) | 471 | `"                    self._browser_session_id = token"` | — |
| [SRC-EEF2E6447C-L000472](../../api/omarai.py#L472) | 472 | `"                return self._cookie_authenticated"` | — |
| [SRC-EEF2E6447C-L000473](../../api/omarai.py#L473) | 473 | `""` | — |
| [SRC-EEF2E6447C-L000474](../../api/omarai.py#L474) | 474 | `"        # Loopback is not proof of a human identity: reverse proxies and tunnels"` | — |
| [SRC-EEF2E6447C-L000475](../../api/omarai.py#L475) | 475 | `"        # may connect from 127.0.0.1 while forwarding untrusted remote requests."` | — |
| [SRC-EEF2E6447C-L000476](../../api/omarai.py#L476) | 476 | `"        # Local development must opt in explicitly; public deployments never do."` | — |
| [SRC-EEF2E6447C-L000477](../../api/omarai.py#L477) | 477 | `"        if ("` | — |
| [SRC-EEF2E6447C-L000478](../../api/omarai.py#L478) | 478 | `"            os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() != \"1\""` | — |
| [SRC-EEF2E6447C-L000479](../../api/omarai.py#L479) | 479 | `"            and os.getenv(\"OMARAI_ALLOW_LOOPBACK_AUTH\", \"\").strip() == \"1\""` | — |
| [SRC-EEF2E6447C-L000480](../../api/omarai.py#L480) | 480 | `"            and not self._has_forwarding_headers()"` | — |
| [SRC-EEF2E6447C-L000481](../../api/omarai.py#L481) | 481 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000482](../../api/omarai.py#L482) | 482 | `"            try:"` | — |
| [SRC-EEF2E6447C-L000483](../../api/omarai.py#L483) | 483 | `"                if ipaddress.ip_address(self.client_address[0]).is_loopback:"` | — |
| [SRC-EEF2E6447C-L000484](../../api/omarai.py#L484) | 484 | `"                    self._authenticated_principal = self.store.default_principal()"` | — |
| [SRC-EEF2E6447C-L000485](../../api/omarai.py#L485) | 485 | `"                    return bool(self._authenticated_principal)"` | — |
| [SRC-EEF2E6447C-L000486](../../api/omarai.py#L486) | 486 | `"            except ValueError:"` | — |
| [SRC-EEF2E6447C-L000487](../../api/omarai.py#L487) | 487 | `"                pass"` | — |
| [SRC-EEF2E6447C-L000488](../../api/omarai.py#L488) | 488 | `"        return False"` | — |
| [SRC-EEF2E6447C-L000489](../../api/omarai.py#L489) | 489 | `""` | — |
| [SRC-EEF2E6447C-L000490](../../api/omarai.py#L490) | 490 | `"    def _allowed_origins(self):"` | — |
| [SRC-EEF2E6447C-L000491](../../api/omarai.py#L491) | 491 | `"        \"\"\"Return configured browser origins plus this service’s own origin."` | — |
| [SRC-EEF2E6447C-L000492](../../api/omarai.py#L492) | 492 | `""` | — |
| [SRC-EEF2E6447C-L000493](../../api/omarai.py#L493) | 493 | `"        OMARAI_ALLOWED_ORIGINS is a comma-separated list of trusted origins"` | — |
| [SRC-EEF2E6447C-L000494](../../api/omarai.py#L494) | 494 | `"        (scheme + host + optional port; no path and no wildcard)."` | — |
| [SRC-EEF2E6447C-L000495](../../api/omarai.py#L495) | 495 | `"        \"\"\""` | — |
| [SRC-EEF2E6447C-L000496](../../api/omarai.py#L496) | 496 | `"        configured = os.getenv(\"OMARAI_ALLOWED_ORIGINS\", \"\")"` | — |
