# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **020**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L006931 إلى SRC-EEF2E6447C-L000480
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L006931](../../agents/web_agent.py#L6931) | 6931 | `"        answer_coverage[\"target_checks\"] = answer_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L006932](../../agents/web_agent.py#L6932) | 6932 | `"        answer_coverage[\"potentially_missing_target_count\"] = answer_integrity[\"potentially_missing_target_count\"]"` | — |
| [SRC-1AE03B9EC3-L006933](../../agents/web_agent.py#L6933) | 6933 | `"        answer_coverage[\"source_evidence_gap_count\"] = answer_integrity[\"source_evidence_gap_count\"]"` | — |
| [SRC-1AE03B9EC3-L006934](../../agents/web_agent.py#L6934) | 6934 | `"        answer_coverage[\"lexical_screen_method\"] = \"deterministic_lexical_screen_only_not_semantic_grading\""` | — |
| [SRC-1AE03B9EC3-L006935](../../agents/web_agent.py#L6935) | 6935 | `"        requirements_without_candidates = int("` | — |
| [SRC-1AE03B9EC3-L006936](../../agents/web_agent.py#L6936) | 6936 | `"            answer_integrity.get(\"requirements_without_candidate_evidence_count\", 0) or 0"` | — |
| [SRC-1AE03B9EC3-L006937](../../agents/web_agent.py#L6937) | 6937 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006938](../../agents/web_agent.py#L6938) | 6938 | `"        task_fulfillment_status = ("` | — |
| [SRC-1AE03B9EC3-L006939](../../agents/web_agent.py#L6939) | 6939 | `"            \"possible_gap_detected\""` | — |
| [SRC-1AE03B9EC3-L006940](../../agents/web_agent.py#L6940) | 6940 | `"            if ("` | — |
| [SRC-1AE03B9EC3-L006941](../../agents/web_agent.py#L6941) | 6941 | `"                answer_integrity[\"potentially_missing_target_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L006942](../../agents/web_agent.py#L6942) | 6942 | `"                or answer_integrity[\"source_evidence_gap_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L006943](../../agents/web_agent.py#L6943) | 6943 | `"            )"` | — |
| [SRC-1AE03B9EC3-L006944](../../agents/web_agent.py#L6944) | 6944 | `"            else \"candidate_evidence_gaps_or_linkage_unknown\""` | — |
| [SRC-1AE03B9EC3-L006945](../../agents/web_agent.py#L6945) | 6945 | `"            if coverage_targets and requirements_without_candidates > 0"` | — |
| [SRC-1AE03B9EC3-L006946](../../agents/web_agent.py#L6946) | 6946 | `"            else \"lexical_signals_found_not_semantically_verified\" if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L006947](../../agents/web_agent.py#L6947) | 6947 | `"            else \"not_machine_assessed_no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L006948](../../agents/web_agent.py#L6948) | 6948 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006949](../../agents/web_agent.py#L6949) | 6949 | `"        if semantic_answer_withheld:"` | — |
| [SRC-1AE03B9EC3-L006950](../../agents/web_agent.py#L6950) | 6950 | `"            task_fulfillment_status = \"not_assessed_insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L006951](../../agents/web_agent.py#L6951) | 6951 | `"        answer_coverage[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L006952](../../agents/web_agent.py#L6952) | 6952 | `"        answer_coverage[\"semantic_verification_status\"] = semantic_claim_verification.get(\"status\")"` | — |
| [SRC-1AE03B9EC3-L006953](../../agents/web_agent.py#L6953) | 6953 | `"        report[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L006954](../../agents/web_agent.py#L6954) | 6954 | `"        report[\"answer_integrity\"] = answer_integrity"` | — |
| [SRC-1AE03B9EC3-L006955](../../agents/web_agent.py#L6955) | 6955 | `"        report[\"requirement_evidence\"] = answer_integrity.get(\"requirement_evidence\", [])"` | — |
| [SRC-1AE03B9EC3-L006956](../../agents/web_agent.py#L6956) | 6956 | `"        report[\"connector_summary\"] = self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L006957](../../agents/web_agent.py#L6957) | 6957 | `"            list(self._provider_diagnostics), sources"` | — |
| [SRC-1AE03B9EC3-L006958](../../agents/web_agent.py#L6958) | 6958 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006959](../../agents/web_agent.py#L6959) | 6959 | `"        report[\"provider_diagnostics\"] = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L006960](../../agents/web_agent.py#L6960) | 6960 | `"        distinct_providers = {"` | — |
| [SRC-1AE03B9EC3-L006961](../../agents/web_agent.py#L6961) | 6961 | `"            provider for source in sources for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L006962](../../agents/web_agent.py#L6962) | 6962 | `"        }"` | — |
| [SRC-1AE03B9EC3-L006963](../../agents/web_agent.py#L6963) | 6963 | `"        distinct_domains = {"` | — |
| [SRC-1AE03B9EC3-L006964](../../agents/web_agent.py#L6964) | 6964 | `"            registrable_domain("` | — |
| [SRC-1AE03B9EC3-L006965](../../agents/web_agent.py#L6965) | 6965 | `"                source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L006966](../../agents/web_agent.py#L6966) | 6966 | `"                or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L006967](../../agents/web_agent.py#L6967) | 6967 | `"                or \"\""` | — |
| [SRC-1AE03B9EC3-L006968](../../agents/web_agent.py#L6968) | 6968 | `"            )"` | — |
| [SRC-1AE03B9EC3-L006969](../../agents/web_agent.py#L6969) | 6969 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L006970](../../agents/web_agent.py#L6970) | 6970 | `"        }"` | — |
| [SRC-1AE03B9EC3-L006971](../../agents/web_agent.py#L6971) | 6971 | `"        distinct_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L006972](../../agents/web_agent.py#L6972) | 6972 | `"        fetched_pages = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L006973](../../agents/web_agent.py#L6973) | 6973 | `"        if semantic_answer_withheld:"` | — |
| [SRC-1AE03B9EC3-L006974](../../agents/web_agent.py#L6974) | 6974 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L006975](../../agents/web_agent.py#L6975) | 6975 | `"        elif ("` | — |
| [SRC-1AE03B9EC3-L006976](../../agents/web_agent.py#L6976) | 6976 | `"            len(sources) >= 4 and len(distinct_domains) >= 3"` | — |
| [SRC-1AE03B9EC3-L006977](../../agents/web_agent.py#L6977) | 6977 | `"            and len(distinct_providers) >= 2 and fetched_pages >= 1"` | — |
| [SRC-1AE03B9EC3-L006978](../../agents/web_agent.py#L6978) | 6978 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006979](../../agents/web_agent.py#L6979) | 6979 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L006980](../../agents/web_agent.py#L6980) | 6980 | `"            research_quality = \"excellent\""` | — |
| [SRC-1AE03B9EC3-L006981](../../agents/web_agent.py#L6981) | 6981 | `"        elif ("` | — |
| [SRC-1AE03B9EC3-L006982](../../agents/web_agent.py#L6982) | 6982 | `"            len(sources) >= 2 and len(distinct_domains) >= 2"` | — |
| [SRC-1AE03B9EC3-L006983](../../agents/web_agent.py#L6983) | 6983 | `"            and (len(distinct_providers) >= 2 or fetched_pages >= 1)"` | — |
| [SRC-1AE03B9EC3-L006984](../../agents/web_agent.py#L6984) | 6984 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006985](../../agents/web_agent.py#L6985) | 6985 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L006986](../../agents/web_agent.py#L6986) | 6986 | `"            research_quality = \"good\""` | — |
| [SRC-1AE03B9EC3-L006987](../../agents/web_agent.py#L6987) | 6987 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L006988](../../agents/web_agent.py#L6988) | 6988 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L006989](../../agents/web_agent.py#L6989) | 6989 | `""` | — |
| [SRC-1AE03B9EC3-L006990](../../agents/web_agent.py#L6990) | 6990 | `"        # Source breadth and a completed model-assisted review do not justify a"` | — |
| [SRC-1AE03B9EC3-L006991](../../agents/web_agent.py#L6991) | 6991 | `"        # positive research-quality label if the final answer has no valid source"` | — |
| [SRC-1AE03B9EC3-L006992](../../agents/web_agent.py#L6992) | 6992 | `"        # citation markers. This is a deterministic presentation guard, not a"` | — |
| [SRC-1AE03B9EC3-L006993](../../agents/web_agent.py#L6993) | 6993 | `"        # semantic entailment check."` | — |
| [SRC-1AE03B9EC3-L006994](../../agents/web_agent.py#L6994) | 6994 | `"        uncited_reviewed_answer = ("` | — |
| [SRC-1AE03B9EC3-L006995](../../agents/web_agent.py#L6995) | 6995 | `"            used_llm"` | — |
| [SRC-1AE03B9EC3-L006996](../../agents/web_agent.py#L6996) | 6996 | `"            and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L006997](../../agents/web_agent.py#L6997) | 6997 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006998](../../agents/web_agent.py#L6998) | 6998 | `"            and citation_validation[\"valid_citation_count\"] == 0"` | — |
| [SRC-1AE03B9EC3-L006999](../../agents/web_agent.py#L6999) | 6999 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007000](../../agents/web_agent.py#L7000) | 7000 | `"        if uncited_reviewed_answer:"` | — |
| [SRC-1AE03B9EC3-L007001](../../agents/web_agent.py#L7001) | 7001 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L007002](../../agents/web_agent.py#L7002) | 7002 | `"            citation_validation[\"claim_support\"] = \"not_established_no_valid_source_citations\""` | — |
| [SRC-1AE03B9EC3-L007003](../../agents/web_agent.py#L7003) | 7003 | `"            answer_evidence_status = \"reviewed_answer_has_no_valid_citations\""` | — |
| [SRC-1AE03B9EC3-L007004](../../agents/web_agent.py#L7004) | 7004 | `"            uncited_answer_warning = ("` | — |
| [SRC-1AE03B9EC3-L007005](../../agents/web_agent.py#L7005) | 7005 | `"                \"اكتملت مراجعة النموذج، لكن الإجابة النهائية لا تحتوي على إحالات صالحة \""` | — |
| [SRC-1AE03B9EC3-L007006](../../agents/web_agent.py#L7006) | 7006 | `"                \"إلى قائمة المصادر؛ لذلك صُنّفت جودة البحث «جزئية». وجود المصادر أو \""` | — |
| [SRC-1AE03B9EC3-L007007](../../agents/web_agent.py#L7007) | 7007 | `"                \"اكتمال مراجعة النموذج لا يثبت دعم كل ادعاء.\""` | — |
| [SRC-1AE03B9EC3-L007008](../../agents/web_agent.py#L7008) | 7008 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007009](../../agents/web_agent.py#L7009) | 7009 | `"        elif citation_validation[\"valid_citation_count\"] > 0:"` | — |
| [SRC-1AE03B9EC3-L007010](../../agents/web_agent.py#L7010) | 7010 | `"            answer_evidence_status = ("` | — |
| [SRC-1AE03B9EC3-L007011](../../agents/web_agent.py#L7011) | 7011 | `"                \"semantic_support_unverified_answer_withheld\""` | — |
| [SRC-1AE03B9EC3-L007012](../../agents/web_agent.py#L7012) | 7012 | `"                if semantic_answer_withheld else \"citation_indices_validated_only\""` | — |
| [SRC-1AE03B9EC3-L007013](../../agents/web_agent.py#L7013) | 7013 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007014](../../agents/web_agent.py#L7014) | 7014 | `"            uncited_answer_warning = None"` | — |
| [SRC-1AE03B9EC3-L007015](../../agents/web_agent.py#L7015) | 7015 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L007016](../../agents/web_agent.py#L7016) | 7016 | `"            answer_evidence_status = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L007017](../../agents/web_agent.py#L7017) | 7017 | `"            uncited_answer_warning = None"` | — |
| [SRC-1AE03B9EC3-L007018](../../agents/web_agent.py#L7018) | 7018 | `""` | — |
| [SRC-1AE03B9EC3-L007019](../../agents/web_agent.py#L7019) | 7019 | `"        search_attempted = search_attempted or bool(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L007020](../../agents/web_agent.py#L7020) | 7020 | `"        report[\"search_attempted\"] = search_attempted"` | — |
| [SRC-1AE03B9EC3-L007021](../../agents/web_agent.py#L7021) | 7021 | `"        prior_search_outcome = report.get(\"search_outcome\")"` | — |
| [SRC-1AE03B9EC3-L007022](../../agents/web_agent.py#L7022) | 7022 | `"        if prior_search_outcome in _RESEARCH_ERROR_OUTCOMES and not sources:"` | — |
| [SRC-1AE03B9EC3-L007023](../../agents/web_agent.py#L7023) | 7023 | `"            # Preserve a known pipeline failure instead of relabeling it as an ordinary"` | — |
| [SRC-1AE03B9EC3-L007024](../../agents/web_agent.py#L7024) | 7024 | `"            # zero-result search merely because the outer request reached its return path."` | — |
| [SRC-1AE03B9EC3-L007025](../../agents/web_agent.py#L7025) | 7025 | `"            report[\"search_outcome\"] = prior_search_outcome"` | — |
| [SRC-1AE03B9EC3-L007026](../../agents/web_agent.py#L7026) | 7026 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L007027](../../agents/web_agent.py#L7027) | 7027 | `"            report[\"search_outcome\"] = ("` | — |
| [SRC-1AE03B9EC3-L007028](../../agents/web_agent.py#L7028) | 7028 | `"                \"attempted_with_usable_sources\" if search_attempted and sources"` | — |
| [SRC-1AE03B9EC3-L007029](../../agents/web_agent.py#L7029) | 7029 | `"                else \"attempted_no_usable_sources\" if search_attempted"` | — |
| [SRC-1AE03B9EC3-L007030](../../agents/web_agent.py#L7030) | 7030 | `"                else \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L007031](../../agents/web_agent.py#L7031) | 7031 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007032](../../agents/web_agent.py#L7032) | 7032 | `"        report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L007033](../../agents/web_agent.py#L7033) | 7033 | `"        report[\"research_quality\"] = research_quality"` | — |
| [SRC-1AE03B9EC3-L007034](../../agents/web_agent.py#L7034) | 7034 | `"        report[\"research_quality_semantics\"] = \"process_coverage_not_factual_probability\""` | — |
| [SRC-1AE03B9EC3-L007035](../../agents/web_agent.py#L7035) | 7035 | `"        report[\"answer_evidence_status\"] = answer_evidence_status"` | — |
| [SRC-1AE03B9EC3-L007036](../../agents/web_agent.py#L7036) | 7036 | `"        report[\"distinct_registrable_domains\"] = len(distinct_domains)"` | — |
| [SRC-1AE03B9EC3-L007037](../../agents/web_agent.py#L7037) | 7037 | `"        report[\"independent_sources\"] = len(distinct_domains)  # Legacy alias; not editorial independence."` | — |
| [SRC-1AE03B9EC3-L007038](../../agents/web_agent.py#L7038) | 7038 | `"        report[\"independent_sources_field_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L007039](../../agents/web_agent.py#L7039) | 7039 | `"            \"legacy_compatibility_alias_for_distinct_registrable_domain_count\""` | — |
| [SRC-1AE03B9EC3-L007040](../../agents/web_agent.py#L7040) | 7040 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007041](../../agents/web_agent.py#L7041) | 7041 | `"        report[\"source_diversity_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L007042](../../agents/web_agent.py#L7042) | 7042 | `"            \"distinct_registrable_domains_not_editorial_independence\""` | — |
| [SRC-1AE03B9EC3-L007043](../../agents/web_agent.py#L7043) | 7043 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007044](../../agents/web_agent.py#L7044) | 7044 | `"        report[\"editorial_independence_status\"] = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L007045](../../agents/web_agent.py#L7045) | 7045 | `"        report[\"claim_audit_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L007046](../../agents/web_agent.py#L7046) | 7046 | `"            \"distinct_model_assessed_source_support_not_ground_truth\""` | — |
| [SRC-1AE03B9EC3-L007047](../../agents/web_agent.py#L7047) | 7047 | `"            if semantic_claim_verification.get(\"status\") in {"` | — |
| [SRC-1AE03B9EC3-L007048](../../agents/web_agent.py#L7048) | 7048 | `"                \"completed_all_claims_supported\", \"completed_no_factual_claims\""` | — |
| [SRC-1AE03B9EC3-L007049](../../agents/web_agent.py#L7049) | 7049 | `"            }"` | — |
| [SRC-1AE03B9EC3-L007050](../../agents/web_agent.py#L7050) | 7050 | `"            else \"not_verified\""` | — |
| [SRC-1AE03B9EC3-L007051](../../agents/web_agent.py#L7051) | 7051 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007052](../../agents/web_agent.py#L7052) | 7052 | `"        report[\"insufficient_evidence\"] = bool("` | — |
| [SRC-1AE03B9EC3-L007053](../../agents/web_agent.py#L7053) | 7053 | `"            report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES"` | — |
| [SRC-1AE03B9EC3-L007054](../../agents/web_agent.py#L7054) | 7054 | `"            or not sources"` | — |
| [SRC-1AE03B9EC3-L007055](../../agents/web_agent.py#L7055) | 7055 | `"            or semantic_answer_withheld"` | — |
| [SRC-1AE03B9EC3-L007056](../../agents/web_agent.py#L7056) | 7056 | `"            or answer_integrity[\"source_evidence_gap_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L007057](../../agents/web_agent.py#L7057) | 7057 | `"            or ("` | — |
| [SRC-1AE03B9EC3-L007058](../../agents/web_agent.py#L7058) | 7058 | `"                bool(coverage_targets)"` | — |
| [SRC-1AE03B9EC3-L007059](../../agents/web_agent.py#L7059) | 7059 | `"                and answer_integrity[\"potentially_missing_target_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L007060](../../agents/web_agent.py#L7060) | 7060 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007061](../../agents/web_agent.py#L7061) | 7061 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007062](../../agents/web_agent.py#L7062) | 7062 | `"        report[\"valid_citation_range\"] = [1, max_citable_sources] if max_citable_sources else []"` | — |
| [SRC-1AE03B9EC3-L007063](../../agents/web_agent.py#L7063) | 7063 | `"        report[\"citation_count\"] = citation_validation[\"valid_citation_count\"]"` | — |
| [SRC-1AE03B9EC3-L007064](../../agents/web_agent.py#L7064) | 7064 | `"        report[\"citation_check\"] = citation_validation[\"status\"]"` | — |
| [SRC-1AE03B9EC3-L007065](../../agents/web_agent.py#L7065) | 7065 | `"        report[\"citation_validation\"] = citation_validation"` | — |
| [SRC-1AE03B9EC3-L007066](../../agents/web_agent.py#L7066) | 7066 | `"        warnings = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L007067](../../agents/web_agent.py#L7067) | 7067 | `"            search_warnings"` | — |
| [SRC-1AE03B9EC3-L007068](../../agents/web_agent.py#L7068) | 7068 | `"            + ([llm_warning] if llm_warning else [])"` | — |
| [SRC-1AE03B9EC3-L007069](../../agents/web_agent.py#L7069) | 7069 | `"            + ([review_warning] if review_warning else [])"` | — |
| [SRC-1AE03B9EC3-L007070](../../agents/web_agent.py#L7070) | 7070 | `"            + ([coverage_repair_warning] if coverage_repair_warning else [])"` | — |
| [SRC-1AE03B9EC3-L007071](../../agents/web_agent.py#L7071) | 7071 | `"            + citation_warnings"` | — |
| [SRC-1AE03B9EC3-L007072](../../agents/web_agent.py#L7072) | 7072 | `"            + ([uncited_answer_warning] if uncited_answer_warning else [])"` | — |
| [SRC-1AE03B9EC3-L007073](../../agents/web_agent.py#L7073) | 7073 | `"            + (["` | — |
| [SRC-1AE03B9EC3-L007074](../../agents/web_agent.py#L7074) | 7074 | `"                \"حُجبت الإجابة المولدة لعدم اكتمال التحقق الدلالي المستقل عن نموذج الصياغة.\""` | — |
| [SRC-1AE03B9EC3-L007075](../../agents/web_agent.py#L7075) | 7075 | `"            ] if semantic_answer_withheld else [])"` | — |
| [SRC-1AE03B9EC3-L007076](../../agents/web_agent.py#L7076) | 7076 | `"        ))"` | — |
| [SRC-1AE03B9EC3-L007077](../../agents/web_agent.py#L7077) | 7077 | `"        report[\"model_calls\"] = list(self.model_usage)"` | — |
| [SRC-1AE03B9EC3-L007078](../../agents/web_agent.py#L7078) | 7078 | `"        report[\"openrouter_web_search_enabled\"] = self.openrouter_web_search_enabled"` | — |
| [SRC-1AE03B9EC3-L007079](../../agents/web_agent.py#L7079) | 7079 | `"        report[\"openrouter_web_search_results\"] = len(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L007080](../../agents/web_agent.py#L7080) | 7080 | `"        if semantic_answer_withheld:"` | — |
| [SRC-1AE03B9EC3-L007081](../../agents/web_agent.py#L7081) | 7081 | `"            final_answer_status = \"semantic_verification_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L007082](../../agents/web_agent.py#L7082) | 7082 | `"        elif generation_budget_exhausted or review_budget_exhausted:"` | — |
| [SRC-1AE03B9EC3-L007083](../../agents/web_agent.py#L7083) | 7083 | `"            final_answer_status = \"budget_exhausted_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L007084](../../agents/web_agent.py#L7084) | 7084 | `"        elif llm_warning:"` | — |
| [SRC-1AE03B9EC3-L007085](../../agents/web_agent.py#L7085) | 7085 | `"            final_answer_status = ("` | — |
| [SRC-1AE03B9EC3-L007086](../../agents/web_agent.py#L7086) | 7086 | `"                \"model_not_configured_fallback\""` | — |
| [SRC-1AE03B9EC3-L007087](../../agents/web_agent.py#L7087) | 7087 | `"                if not self.api_key"` | — |
| [SRC-1AE03B9EC3-L007088](../../agents/web_agent.py#L7088) | 7088 | `"                else \"generation_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L007089](../../agents/web_agent.py#L7089) | 7089 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007090](../../agents/web_agent.py#L7090) | 7090 | `"        elif review_warning:"` | — |
| [SRC-1AE03B9EC3-L007091](../../agents/web_agent.py#L7091) | 7091 | `"            final_answer_status = \"review_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L007092](../../agents/web_agent.py#L7092) | 7092 | `"        elif coverage_repair_status == \"no_change_gap_unresolved\":"` | — |
| [SRC-1AE03B9EC3-L007093](../../agents/web_agent.py#L7093) | 7093 | `"            final_answer_status = \"coverage_repair_left_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L007094](../../agents/web_agent.py#L7094) | 7094 | `"        elif coverage_repair_status == \"budget_exhausted\":"` | — |
| [SRC-1AE03B9EC3-L007095](../../agents/web_agent.py#L7095) | 7095 | `"            final_answer_status = \"coverage_repair_budget_exhausted_with_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L007096](../../agents/web_agent.py#L7096) | 7096 | `"        elif coverage_repair_status == \"unavailable\":"` | — |
| [SRC-1AE03B9EC3-L007097](../../agents/web_agent.py#L7097) | 7097 | `"            final_answer_status = \"coverage_repair_unavailable_with_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L007098](../../agents/web_agent.py#L7098) | 7098 | `"        elif used_llm:"` | — |
| [SRC-1AE03B9EC3-L007099](../../agents/web_agent.py#L7099) | 7099 | `"            final_answer_status = \"model_answer_generated\""` | — |
| [SRC-1AE03B9EC3-L007100](../../agents/web_agent.py#L7100) | 7100 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L007101](../../agents/web_agent.py#L7101) | 7101 | `"            final_answer_status = \"source_fallback\""` | — |
| [SRC-1AE03B9EC3-L007102](../../agents/web_agent.py#L7102) | 7102 | `""` | — |
| [SRC-1AE03B9EC3-L007103](../../agents/web_agent.py#L7103) | 7103 | `"        # Report pipeline completion separately from factual correctness. A successful"` | — |
| [SRC-1AE03B9EC3-L007104](../../agents/web_agent.py#L7104) | 7104 | `"        # retrieval or model review is not an independent semantic fact check."` | — |
| [SRC-1AE03B9EC3-L007105](../../agents/web_agent.py#L7105) | 7105 | `"        if report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES:"` | — |
| [SRC-1AE03B9EC3-L007106](../../agents/web_agent.py#L7106) | 7106 | `"            pipeline_completion_status = \"execution_failed\""` | — |
| [SRC-1AE03B9EC3-L007107](../../agents/web_agent.py#L7107) | 7107 | `"        elif not search_attempted:"` | — |
| [SRC-1AE03B9EC3-L007108](../../agents/web_agent.py#L7108) | 7108 | `"            pipeline_completion_status = \"not_verified\""` | — |
| [SRC-1AE03B9EC3-L007109](../../agents/web_agent.py#L7109) | 7109 | `"        elif not sources:"` | — |
| [SRC-1AE03B9EC3-L007110](../../agents/web_agent.py#L7110) | 7110 | `"            pipeline_completion_status = \"insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L007111](../../agents/web_agent.py#L7111) | 7111 | `"        elif ("` | — |
| [SRC-1AE03B9EC3-L007112](../../agents/web_agent.py#L7112) | 7112 | `"            llm_warning"` | — |
| [SRC-1AE03B9EC3-L007113](../../agents/web_agent.py#L7113) | 7113 | `"            or review_warning"` | — |
| [SRC-1AE03B9EC3-L007114](../../agents/web_agent.py#L7114) | 7114 | `"            or review_status != \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L007115](../../agents/web_agent.py#L7115) | 7115 | `"            or answer_integrity[\"potentially_missing_target_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L007116](../../agents/web_agent.py#L7116) | 7116 | `"            or answer_integrity[\"source_evidence_gap_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L007117](../../agents/web_agent.py#L7117) | 7117 | `"            or citation_validation[\"valid_citation_count\"] == 0"` | — |
| [SRC-1AE03B9EC3-L007118](../../agents/web_agent.py#L7118) | 7118 | `"            or semantic_answer_withheld"` | — |
| [SRC-1AE03B9EC3-L007119](../../agents/web_agent.py#L7119) | 7119 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L007120](../../agents/web_agent.py#L7120) | 7120 | `"            pipeline_completion_status = \"partial\""` | — |
| [SRC-1AE03B9EC3-L007121](../../agents/web_agent.py#L7121) | 7121 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L007122](../../agents/web_agent.py#L7122) | 7122 | `"            pipeline_completion_status = \"completed\""` | — |
| [SRC-1AE03B9EC3-L007123](../../agents/web_agent.py#L7123) | 7123 | `"        completion_stages = {"` | — |
| [SRC-1AE03B9EC3-L007124](../../agents/web_agent.py#L7124) | 7124 | `"            \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L007125](../../agents/web_agent.py#L7125) | 7125 | `"            \"accepted_sources\": len(sources),"` | — |
| [SRC-1AE03B9EC3-L007126](../../agents/web_agent.py#L7126) | 7126 | `"            \"pages_read\": fetched_pages,"` | — |
| [SRC-1AE03B9EC3-L007127](../../agents/web_agent.py#L7127) | 7127 | `"            \"answer_generated_by_model\": bool(used_llm),"` | — |
| [SRC-1AE03B9EC3-L007128](../../agents/web_agent.py#L7128) | 7128 | `"            \"claim_review\": review_status,"` | — |
| [SRC-1AE03B9EC3-L007129](../../agents/web_agent.py#L7129) | 7129 | `"            \"valid_citations\": citation_validation[\"valid_citation_count\"],"` | — |
| [SRC-1AE03B9EC3-L007130](../../agents/web_agent.py#L7130) | 7130 | `"            \"semantic_fact_check\": \"not_performed\","` | — |
| [SRC-1AE03B9EC3-L007131](../../agents/web_agent.py#L7131) | 7131 | `"            \"semantic_claim_support_assessment\": semantic_claim_verification.get(\"status\", \"not_performed\"),"` | — |
| [SRC-1AE03B9EC3-L007132](../../agents/web_agent.py#L7132) | 7132 | `"        }"` | — |
| [SRC-1AE03B9EC3-L007133](../../agents/web_agent.py#L7133) | 7133 | `"        if semantic_answer_withheld:"` | — |
| [SRC-1AE03B9EC3-L007134](../../agents/web_agent.py#L7134) | 7134 | `"            pipeline_completion_status = \"partial\""` | — |
| [SRC-1AE03B9EC3-L007135](../../agents/web_agent.py#L7135) | 7135 | `"        report[\"pipeline_completion_status\"] = pipeline_completion_status"` | — |
| [SRC-1AE03B9EC3-L007136](../../agents/web_agent.py#L7136) | 7136 | `"        report[\"completion_stages\"] = completion_stages"` | — |
| [SRC-1AE03B9EC3-L007137](../../agents/web_agent.py#L7137) | 7137 | `"        report[\"pipeline_completion_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L007138](../../agents/web_agent.py#L7138) | 7138 | `"            \"pipeline stage completion only; not a guarantee of factual correctness\""` | — |
| [SRC-1AE03B9EC3-L007139](../../agents/web_agent.py#L7139) | 7139 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007140](../../agents/web_agent.py#L7140) | 7140 | `""` | — |
| [SRC-1AE03B9EC3-L007141](../../agents/web_agent.py#L7141) | 7141 | `"        public_sources = []"` | — |
| [SRC-1AE03B9EC3-L007142](../../agents/web_agent.py#L7142) | 7142 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L007143](../../agents/web_agent.py#L7143) | 7143 | `"            public_sources.append({"` | — |
| [SRC-1AE03B9EC3-L007144](../../agents/web_agent.py#L7144) | 7144 | `"                \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L007145](../../agents/web_agent.py#L7145) | 7145 | `"                \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L007146](../../agents/web_agent.py#L7146) | 7146 | `"                \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007147](../../agents/web_agent.py#L7147) | 7147 | `"                \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L007148](../../agents/web_agent.py#L7148) | 7148 | `"                \"readable_page_text_available\": bool(source.get(\"page_fetched\")) and bool(str(source.get(\"page_text\") or \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L007149](../../agents/web_agent.py#L7149) | 7149 | `"                \"page_text_present_without_fetch_flag\": bool(str(source.get(\"page_text\") or \"\").strip()) and not bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L007150](../../agents/web_agent.py#L7150) | 7150 | `"                \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L007151](../../agents/web_agent.py#L7151) | 7151 | `"                \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L007152](../../agents/web_agent.py#L7152) | 7152 | `"                \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L007153](../../agents/web_agent.py#L7153) | 7153 | `"                \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007154](../../agents/web_agent.py#L7154) | 7154 | `"                \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L007155](../../agents/web_agent.py#L7155) | 7155 | `"                \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007156](../../agents/web_agent.py#L7156) | 7156 | `"                \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007157](../../agents/web_agent.py#L7157) | 7157 | `"                \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007158](../../agents/web_agent.py#L7158) | 7158 | `"                \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L007159](../../agents/web_agent.py#L7159) | 7159 | `"                \"lead_qualification\": source.get(\"lead_qualification\"),"` | — |
| [SRC-1AE03B9EC3-L007160](../../agents/web_agent.py#L7160) | 7160 | `"                \"lead_intent_evidence\": source.get(\"lead_intent_evidence\"),"` | — |
| [SRC-1AE03B9EC3-L007161](../../agents/web_agent.py#L7161) | 7161 | `"            })"` | — |
| [SRC-1AE03B9EC3-L007162](../../agents/web_agent.py#L7162) | 7162 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L007163](../../agents/web_agent.py#L7163) | 7163 | `"            \"answer\": answer,"` | — |
| [SRC-1AE03B9EC3-L007164](../../agents/web_agent.py#L7164) | 7164 | `"            \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L007165](../../agents/web_agent.py#L7165) | 7165 | `"            \"search_query\": (plan.get(\"queries\") or [\"\"])[0],"` | — |
| [SRC-1AE03B9EC3-L007166](../../agents/web_agent.py#L7166) | 7166 | `"            \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L007167](../../agents/web_agent.py#L7167) | 7167 | `"            \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L007168](../../agents/web_agent.py#L7168) | 7168 | `"                \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L007169](../../agents/web_agent.py#L7169) | 7169 | `"                \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L007170](../../agents/web_agent.py#L7170) | 7170 | `"                \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L007171](../../agents/web_agent.py#L7171) | 7171 | `"                \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L007172](../../agents/web_agent.py#L7172) | 7172 | `"                \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L007173](../../agents/web_agent.py#L7173) | 7173 | `"                \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L007174](../../agents/web_agent.py#L7174) | 7174 | `"                \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L007175](../../agents/web_agent.py#L7175) | 7175 | `"                \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L007176](../../agents/web_agent.py#L7176) | 7176 | `"                \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L007177](../../agents/web_agent.py#L7177) | 7177 | `"                \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L007178](../../agents/web_agent.py#L7178) | 7178 | `"            },"` | — |
| [SRC-1AE03B9EC3-L007179](../../agents/web_agent.py#L7179) | 7179 | `"            \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L007180](../../agents/web_agent.py#L7180) | 7180 | `"            \"sources\": public_sources,"` | — |
| [SRC-1AE03B9EC3-L007181](../../agents/web_agent.py#L7181) | 7181 | `"            \"research_quality\": research_quality,"` | — |
| [SRC-1AE03B9EC3-L007182](../../agents/web_agent.py#L7182) | 7182 | `"            \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L007183](../../agents/web_agent.py#L7183) | 7183 | `"            \"answer_evidence_status\": answer_evidence_status,"` | — |
| [SRC-1AE03B9EC3-L007184](../../agents/web_agent.py#L7184) | 7184 | `"            \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L007185](../../agents/web_agent.py#L7185) | 7185 | `"            \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L007186](../../agents/web_agent.py#L7186) | 7186 | `"            \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L007187](../../agents/web_agent.py#L7187) | 7187 | `"            \"coverage_repair_status\": coverage_repair_status,"` | — |
| [SRC-1AE03B9EC3-L007188](../../agents/web_agent.py#L7188) | 7188 | `"            \"used_language_model\": used_llm,"` | — |
| [SRC-1AE03B9EC3-L007189](../../agents/web_agent.py#L7189) | 7189 | `"            \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L007190](../../agents/web_agent.py#L7190) | 7190 | `"            \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L007191](../../agents/web_agent.py#L7191) | 7191 | `"            \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L007192](../../agents/web_agent.py#L7192) | 7192 | `"            \"warnings\": warnings,"` | — |
| [SRC-1AE03B9EC3-L007193](../../agents/web_agent.py#L7193) | 7193 | `"            \"kind\": \"web_research\" if used_llm else \"web_fallback\","` | — |
| [SRC-1AE03B9EC3-L007194](../../agents/web_agent.py#L7194) | 7194 | `"            \"final_answer_status\": final_answer_status,"` | — |
| [SRC-1AE03B9EC3-L007195](../../agents/web_agent.py#L7195) | 7195 | `"            \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L007196](../../agents/web_agent.py#L7196) | 7196 | `"            \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L007197](../../agents/web_agent.py#L7197) | 7197 | `"        }"` | — |
| [SRC-1AE03B9EC3-L007198](../../agents/web_agent.py#L7198) | 7198 | `""` | — |
| [SRC-1AE03B9EC3-L007199](../../agents/web_agent.py#L7199) | 7199 | `"def _normalized_provider_usage("` | — |
| [SRC-1AE03B9EC3-L007200](../../agents/web_agent.py#L7200) | 7200 | `"    usage: Any, *, provider_base_url: str = \"\""` | — |
| [SRC-1AE03B9EC3-L007201](../../agents/web_agent.py#L7201) | 7201 | `") -> dict[str, int \| float] \| None:"` | — |
| [SRC-1AE03B9EC3-L007202](../../agents/web_agent.py#L7202) | 7202 | `"    \"\"\"Allowlist safe counters; interpret generic 'cost' as USD only for OpenRouter.\"\"\""` | — |
| [SRC-1AE03B9EC3-L007203](../../agents/web_agent.py#L7203) | 7203 | `"    if not isinstance(usage, dict):"` | — |
| [SRC-1AE03B9EC3-L007204](../../agents/web_agent.py#L7204) | 7204 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L007205](../../agents/web_agent.py#L7205) | 7205 | `"    normalized: dict[str, int \| float] = {}"` | — |
| [SRC-1AE03B9EC3-L007206](../../agents/web_agent.py#L7206) | 7206 | `"    for source_key in (\"prompt_tokens\", \"completion_tokens\", \"total_tokens\"):"` | — |
| [SRC-1AE03B9EC3-L007207](../../agents/web_agent.py#L7207) | 7207 | `"        value = usage.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L007208](../../agents/web_agent.py#L7208) | 7208 | `"        if isinstance(value, int) and not isinstance(value, bool) and value >= 0:"` | — |
| [SRC-1AE03B9EC3-L007209](../../agents/web_agent.py#L7209) | 7209 | `"            normalized[source_key] = value"` | — |
| [SRC-1AE03B9EC3-L007210](../../agents/web_agent.py#L7210) | 7210 | `"    cost_keys = [\"cost_usd\"]"` | — |
| [SRC-1AE03B9EC3-L007211](../../agents/web_agent.py#L7211) | 7211 | `"    provider_host = \"\""` | — |
| [SRC-1AE03B9EC3-L007212](../../agents/web_agent.py#L7212) | 7212 | `"    if isinstance(provider_base_url, str):"` | — |
| [SRC-1AE03B9EC3-L007213](../../agents/web_agent.py#L7213) | 7213 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L007214](../../agents/web_agent.py#L7214) | 7214 | `"            provider_host = (urllib.parse.urlsplit(provider_base_url.strip()).hostname or \"\").lower().rstrip(\".\")"` | — |
| [SRC-1AE03B9EC3-L007215](../../agents/web_agent.py#L7215) | 7215 | `"        except ValueError:"` | — |
| [SRC-1AE03B9EC3-L007216](../../agents/web_agent.py#L7216) | 7216 | `"            provider_host = \"\""` | — |
| [SRC-1AE03B9EC3-L007217](../../agents/web_agent.py#L7217) | 7217 | `"    is_openrouter = ("` | — |
| [SRC-1AE03B9EC3-L007218](../../agents/web_agent.py#L7218) | 7218 | `"        provider_host == \"openrouter.ai\""` | — |
| [SRC-1AE03B9EC3-L007219](../../agents/web_agent.py#L7219) | 7219 | `"        or provider_host.endswith(\".openrouter.ai\")"` | — |
| [SRC-1AE03B9EC3-L007220](../../agents/web_agent.py#L7220) | 7220 | `"    )"` | — |
| [SRC-1AE03B9EC3-L007221](../../agents/web_agent.py#L7221) | 7221 | `"    if is_openrouter:"` | — |
| [SRC-1AE03B9EC3-L007222](../../agents/web_agent.py#L7222) | 7222 | `"        cost_keys.extend([\"cost\", \"total_cost\"])"` | — |
| [SRC-1AE03B9EC3-L007223](../../agents/web_agent.py#L7223) | 7223 | `"    for source_key in cost_keys:"` | — |
| [SRC-1AE03B9EC3-L007224](../../agents/web_agent.py#L7224) | 7224 | `"        value = usage.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L007225](../../agents/web_agent.py#L7225) | 7225 | `"        if isinstance(value, (int, float)) and not isinstance(value, bool):"` | — |
| [SRC-1AE03B9EC3-L007226](../../agents/web_agent.py#L7226) | 7226 | `"            number = float(value)"` | — |
| [SRC-1AE03B9EC3-L007227](../../agents/web_agent.py#L7227) | 7227 | `"            if number >= 0 and math.isfinite(number):"` | — |
| [SRC-1AE03B9EC3-L007228](../../agents/web_agent.py#L7228) | 7228 | `"                normalized[\"cost_usd\"] = number"` | — |
| [SRC-1AE03B9EC3-L007229](../../agents/web_agent.py#L7229) | 7229 | `"                break"` | — |
| [SRC-1AE03B9EC3-L007230](../../agents/web_agent.py#L7230) | 7230 | `"    return normalized or None"` | — |
| [SRC-1AE03B9EC3-L007231](../../agents/web_agent.py#L7231) | 7231 | `""` | — |
| [SRC-1AE03B9EC3-L007232](../../agents/web_agent.py#L7232) | 7232 | `"def _model_usage_record("` | — |
| [SRC-1AE03B9EC3-L007233](../../agents/web_agent.py#L7233) | 7233 | `"    requested_model: str,"` | — |
| [SRC-1AE03B9EC3-L007234](../../agents/web_agent.py#L7234) | 7234 | `"    candidate_model: str,"` | — |
| [SRC-1AE03B9EC3-L007235](../../agents/web_agent.py#L7235) | 7235 | `"    response_data: dict[str, Any],"` | — |
| [SRC-1AE03B9EC3-L007236](../../agents/web_agent.py#L7236) | 7236 | `"    provider_base_url: str,"` | — |
| [SRC-1AE03B9EC3-L007237](../../agents/web_agent.py#L7237) | 7237 | `") -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L007238](../../agents/web_agent.py#L7238) | 7238 | `"    \"\"\"Return only allowlisted provider usage metadata, never raw prompts/responses.\"\"\""` | — |
| [SRC-1AE03B9EC3-L007239](../../agents/web_agent.py#L7239) | 7239 | `"    record: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L007240](../../agents/web_agent.py#L7240) | 7240 | `"        \"requested_model\": requested_model,"` | — |
| [SRC-1AE03B9EC3-L007241](../../agents/web_agent.py#L7241) | 7241 | `"        \"used_model\": candidate_model,"` | — |
| [SRC-1AE03B9EC3-L007242](../../agents/web_agent.py#L7242) | 7242 | `"        \"fallback_used\": \"true\" if candidate_model != requested_model else \"false\","` | — |
| [SRC-1AE03B9EC3-L007243](../../agents/web_agent.py#L7243) | 7243 | `"    }"` | — |
| [SRC-1AE03B9EC3-L007244](../../agents/web_agent.py#L7244) | 7244 | `"    provider_usage = _normalized_provider_usage("` | — |
| [SRC-1AE03B9EC3-L007245](../../agents/web_agent.py#L7245) | 7245 | `"        response_data.get(\"usage\"), provider_base_url=provider_base_url"` | — |
| [SRC-1AE03B9EC3-L007246](../../agents/web_agent.py#L7246) | 7246 | `"    )"` | — |
| [SRC-1AE03B9EC3-L007247](../../agents/web_agent.py#L7247) | 7247 | `"    if provider_usage is not None:"` | — |
| [SRC-1AE03B9EC3-L007248](../../agents/web_agent.py#L7248) | 7248 | `"        record[\"provider_usage\"] = provider_usage"` | — |
| [SRC-1AE03B9EC3-L007249](../../agents/web_agent.py#L7249) | 7249 | `"    return record"` | — |
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
| [SRC-EEF2E6447C-L000022](../../api/omarai.py#L22) | 22 | `"from agents.web_agent import WebAgent"` | — |
| [SRC-EEF2E6447C-L000023](../../api/omarai.py#L23) | 23 | `""` | — |
| [SRC-EEF2E6447C-L000024](../../api/omarai.py#L24) | 24 | `"ROOT = Path(__file__).resolve().parents[1] / \"web\""` | — |
| [SRC-EEF2E6447C-L000025](../../api/omarai.py#L25) | 25 | `"AGENT_DASHBOARD = ROOT / \"agent.html\""` | — |
| [SRC-EEF2E6447C-L000026](../../api/omarai.py#L26) | 26 | `"LEADS_DASHBOARD = ROOT / \"dashboard.html\""` | — |
| [SRC-EEF2E6447C-L000027](../../api/omarai.py#L27) | 27 | `"MAX_REQUEST_BODY_BYTES = 200_000"` | — |
| [SRC-EEF2E6447C-L000028](../../api/omarai.py#L28) | 28 | `"BROWSER_SESSION_COOKIE_MAX_AGE = 8 * 60 * 60"` | — |
| [SRC-EEF2E6447C-L000029](../../api/omarai.py#L29) | 29 | `"BROWSER_SESSION_ID_RE = re.compile(r\"^[A-Za-z0-9_-]{32,128}$\")"` | — |
| [SRC-EEF2E6447C-L000030](../../api/omarai.py#L30) | 30 | `""` | — |
| [SRC-EEF2E6447C-L000031](../../api/omarai.py#L31) | 31 | `""` | — |
| [SRC-EEF2E6447C-L000032](../../api/omarai.py#L32) | 32 | `"def _csp_hash_source(value: str) -> str:"` | — |
| [SRC-EEF2E6447C-L000033](../../api/omarai.py#L33) | 33 | `"    digest = base64.b64encode(hashlib.sha256(value.encode(\"utf-8\")).digest()).decode(\"ascii\")"` | — |
| [SRC-EEF2E6447C-L000034](../../api/omarai.py#L34) | 34 | `"    return f\"'sha256-{digest}'\""` | — |
| [SRC-EEF2E6447C-L000035](../../api/omarai.py#L35) | 35 | `""` | — |
| [SRC-EEF2E6447C-L000036](../../api/omarai.py#L36) | 36 | `""` | — |
| [SRC-EEF2E6447C-L000037](../../api/omarai.py#L37) | 37 | `"@lru_cache(maxsize=1)"` | — |
| [SRC-EEF2E6447C-L000038](../../api/omarai.py#L38) | 38 | `"def _content_security_policy() -> str:"` | — |
| [SRC-EEF2E6447C-L000039](../../api/omarai.py#L39) | 39 | `"    \"\"\"Allow only known inline blocks/attributes from the static first-party HTML."` | — |
| [SRC-EEF2E6447C-L000040](../../api/omarai.py#L40) | 40 | `""` | — |
| [SRC-EEF2E6447C-L000041](../../api/omarai.py#L41) | 41 | `"    Hashes deliberately replace unsafe-inline. Updating an inline script/style means its"` | — |
| [SRC-EEF2E6447C-L000042](../../api/omarai.py#L42) | 42 | `"    hash changes automatically with the served source. This is not a sanitizer for"` | — |
| [SRC-EEF2E6447C-L000043](../../api/omarai.py#L43) | 43 | `"    untrusted HTML; callers must never splice untrusted input into these static files."` | — |
| [SRC-EEF2E6447C-L000044](../../api/omarai.py#L44) | 44 | `"    \"\"\""` | — |
| [SRC-EEF2E6447C-L000045](../../api/omarai.py#L45) | 45 | `"    script_hashes: set[str] = set()"` | — |
| [SRC-EEF2E6447C-L000046](../../api/omarai.py#L46) | 46 | `"    style_hashes: set[str] = set()"` | — |
| [SRC-EEF2E6447C-L000047](../../api/omarai.py#L47) | 47 | `"    event_handler_hashes: set[str] = set()"` | — |
| [SRC-EEF2E6447C-L000048](../../api/omarai.py#L48) | 48 | `"    style_attribute_hashes: set[str] = set()"` | — |
| [SRC-EEF2E6447C-L000049](../../api/omarai.py#L49) | 49 | `""` | — |
| [SRC-EEF2E6447C-L000050](../../api/omarai.py#L50) | 50 | `"    for html_path in sorted(ROOT.glob(\"*.html\")):"` | — |
| [SRC-EEF2E6447C-L000051](../../api/omarai.py#L51) | 51 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000052](../../api/omarai.py#L52) | 52 | `"            document = html_path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-EEF2E6447C-L000053](../../api/omarai.py#L53) | 53 | `"        except (OSError, UnicodeError):"` | — |
| [SRC-EEF2E6447C-L000054](../../api/omarai.py#L54) | 54 | `"            continue"` | — |
| [SRC-EEF2E6447C-L000055](../../api/omarai.py#L55) | 55 | `""` | — |
| [SRC-EEF2E6447C-L000056](../../api/omarai.py#L56) | 56 | `"        for match in re.finditer("` | — |
| [SRC-EEF2E6447C-L000057](../../api/omarai.py#L57) | 57 | `"            r\"<script\\b(?P<attrs>[^>]*)>(?P<body>.*?)</script\\s*>\","` | — |
| [SRC-EEF2E6447C-L000058](../../api/omarai.py#L58) | 58 | `"            document,"` | — |
| [SRC-EEF2E6447C-L000059](../../api/omarai.py#L59) | 59 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-EEF2E6447C-L000060](../../api/omarai.py#L60) | 60 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000061](../../api/omarai.py#L61) | 61 | `"            if re.search(r\"\\bsrc\\s*=\", match.group(\"attrs\"), re.IGNORECASE):"` | — |
| [SRC-EEF2E6447C-L000062](../../api/omarai.py#L62) | 62 | `"                continue"` | — |
| [SRC-EEF2E6447C-L000063](../../api/omarai.py#L63) | 63 | `"            script_hashes.add(_csp_hash_source(match.group(\"body\")))"` | — |
| [SRC-EEF2E6447C-L000064](../../api/omarai.py#L64) | 64 | `""` | — |
| [SRC-EEF2E6447C-L000065](../../api/omarai.py#L65) | 65 | `"        for match in re.finditer("` | — |
| [SRC-EEF2E6447C-L000066](../../api/omarai.py#L66) | 66 | `"            r\"<style\\b[^>]*>(?P<body>.*?)</style\\s*>\","` | — |
| [SRC-EEF2E6447C-L000067](../../api/omarai.py#L67) | 67 | `"            document,"` | — |
| [SRC-EEF2E6447C-L000068](../../api/omarai.py#L68) | 68 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-EEF2E6447C-L000069](../../api/omarai.py#L69) | 69 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000070](../../api/omarai.py#L70) | 70 | `"            style_hashes.add(_csp_hash_source(match.group(\"body\")))"` | — |
| [SRC-EEF2E6447C-L000071](../../api/omarai.py#L71) | 71 | `""` | — |
| [SRC-EEF2E6447C-L000072](../../api/omarai.py#L72) | 72 | `"        # This scan intentionally includes style/event attributes embedded in"` | — |
| [SRC-EEF2E6447C-L000073](../../api/omarai.py#L73) | 73 | `"        # trusted first-party HTML templates assembled by inline scripts."` | — |
| [SRC-EEF2E6447C-L000074](../../api/omarai.py#L74) | 74 | `"        for match in re.finditer("` | — |
| [SRC-EEF2E6447C-L000075](../../api/omarai.py#L75) | 75 | `"            r\"\"\"\\bstyle\\s*=\\s*([\"'])(.*?)\\1\"\"\","` | — |
| [SRC-EEF2E6447C-L000076](../../api/omarai.py#L76) | 76 | `"            document,"` | — |
| [SRC-EEF2E6447C-L000077](../../api/omarai.py#L77) | 77 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-EEF2E6447C-L000078](../../api/omarai.py#L78) | 78 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000079](../../api/omarai.py#L79) | 79 | `"            style_attribute_hashes.add(_csp_hash_source(match.group(2).strip()))"` | — |
| [SRC-EEF2E6447C-L000080](../../api/omarai.py#L80) | 80 | `""` | — |
| [SRC-EEF2E6447C-L000081](../../api/omarai.py#L81) | 81 | `"        for match in re.finditer("` | — |
| [SRC-EEF2E6447C-L000082](../../api/omarai.py#L82) | 82 | `"            r\"\"\"\\bon[a-z]+\\s*=\\s*([\"'])(.*?)\\1\"\"\","` | — |
| [SRC-EEF2E6447C-L000083](../../api/omarai.py#L83) | 83 | `"            document,"` | — |
| [SRC-EEF2E6447C-L000084](../../api/omarai.py#L84) | 84 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-EEF2E6447C-L000085](../../api/omarai.py#L85) | 85 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000086](../../api/omarai.py#L86) | 86 | `"            event_handler_hashes.add(_csp_hash_source(match.group(2).strip()))"` | — |
| [SRC-EEF2E6447C-L000087](../../api/omarai.py#L87) | 87 | `""` | — |
| [SRC-EEF2E6447C-L000088](../../api/omarai.py#L88) | 88 | `"    script_sources = [\"'self'\", *sorted(script_hashes)]"` | — |
| [SRC-EEF2E6447C-L000089](../../api/omarai.py#L89) | 89 | `"    style_sources = [\"'self'\", *sorted(style_hashes)]"` | — |
| [SRC-EEF2E6447C-L000090](../../api/omarai.py#L90) | 90 | `"    if event_handler_hashes:"` | — |
| [SRC-EEF2E6447C-L000091](../../api/omarai.py#L91) | 91 | `"        script_sources.extend([\"'unsafe-hashes'\", *sorted(event_handler_hashes)])"` | — |
| [SRC-EEF2E6447C-L000092](../../api/omarai.py#L92) | 92 | `"    if style_attribute_hashes:"` | — |
| [SRC-EEF2E6447C-L000093](../../api/omarai.py#L93) | 93 | `"        style_sources.extend([\"'unsafe-hashes'\", *sorted(style_attribute_hashes)])"` | — |
| [SRC-EEF2E6447C-L000094](../../api/omarai.py#L94) | 94 | `""` | — |
| [SRC-EEF2E6447C-L000095](../../api/omarai.py#L95) | 95 | `"    return ("` | — |
| [SRC-EEF2E6447C-L000096](../../api/omarai.py#L96) | 96 | `"        \"default-src 'self'; base-uri 'self'; object-src 'none'; frame-ancestors 'none'; \""` | — |
| [SRC-EEF2E6447C-L000097](../../api/omarai.py#L97) | 97 | `"        \"form-action 'self'; connect-src 'self'; img-src 'self' data:; \""` | — |
| [SRC-EEF2E6447C-L000098](../../api/omarai.py#L98) | 98 | `"        f\"script-src {' '.join(script_sources)}; \""` | — |
| [SRC-EEF2E6447C-L000099](../../api/omarai.py#L99) | 99 | `"        f\"style-src {' '.join(style_sources)}; font-src 'self' data:\""` | — |
| [SRC-EEF2E6447C-L000100](../../api/omarai.py#L100) | 100 | `"    )"` | — |
| [SRC-EEF2E6447C-L000101](../../api/omarai.py#L101) | 101 | `"# Bound request-line + header parsing before application code or body processing."` | — |
| [SRC-EEF2E6447C-L000102](../../api/omarai.py#L102) | 102 | `"REQUEST_HEADER_READ_TIMEOUT_SECONDS = 8.0"` | — |
| [SRC-EEF2E6447C-L000103](../../api/omarai.py#L103) | 103 | `"REQUEST_HEADER_IDLE_TIMEOUT_SECONDS = 2.0"` | — |
| [SRC-EEF2E6447C-L000104](../../api/omarai.py#L104) | 104 | `"MAX_REQUEST_HEADER_READ_TIMEOUT_SECONDS = 15.0"` | — |
| [SRC-EEF2E6447C-L000105](../../api/omarai.py#L105) | 105 | `"# Absolute deadline for reading the entire body, not merely a per-read idle timeout."` | — |
| [SRC-EEF2E6447C-L000106](../../api/omarai.py#L106) | 106 | `"REQUEST_BODY_READ_TIMEOUT_SECONDS = 10.0"` | — |
| [SRC-EEF2E6447C-L000107](../../api/omarai.py#L107) | 107 | `"REQUEST_BODY_IDLE_TIMEOUT_SECONDS = 2.0"` | — |
| [SRC-EEF2E6447C-L000108](../../api/omarai.py#L108) | 108 | `"MAX_REQUEST_BODY_READ_TIMEOUT_SECONDS = 30.0"` | — |
| [SRC-EEF2E6447C-L000109](../../api/omarai.py#L109) | 109 | `"REQUEST_BODY_READ_CHUNK_BYTES = 8_192"` | — |
| [SRC-EEF2E6447C-L000110](../../api/omarai.py#L110) | 110 | `""` | — |
| [SRC-EEF2E6447C-L000111](../../api/omarai.py#L111) | 111 | `""` | — |
| [SRC-EEF2E6447C-L000112](../../api/omarai.py#L112) | 112 | `""` | — |
| [SRC-EEF2E6447C-L000113](../../api/omarai.py#L113) | 113 | `"def _lead_store_from_environment() -> LeadStore:"` | — |
| [SRC-EEF2E6447C-L000114](../../api/omarai.py#L114) | 114 | `"    \"\"\"Use an operator-configured database path when a persistent volume is available.\"\"\""` | — |
| [SRC-EEF2E6447C-L000115](../../api/omarai.py#L115) | 115 | `"    configured_path = os.getenv(\"OMARAI_DB_PATH\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000116](../../api/omarai.py#L116) | 116 | `"    return LeadStore(configured_path or None)"` | — |
| [SRC-EEF2E6447C-L000117](../../api/omarai.py#L117) | 117 | `""` | — |
| [SRC-EEF2E6447C-L000118](../../api/omarai.py#L118) | 118 | `""` | — |
| [SRC-EEF2E6447C-L000119](../../api/omarai.py#L119) | 119 | `"class _DeadlineRequestReader:"` | — |
| [SRC-EEF2E6447C-L000120](../../api/omarai.py#L120) | 120 | `"    \"\"\"Read HTTP header lines with one absolute deadline across all fragments."` | — |
| [SRC-EEF2E6447C-L000121](../../api/omarai.py#L121) | 121 | `""` | — |
| [SRC-EEF2E6447C-L000122](../../api/omarai.py#L122) | 122 | `"    The standard buffered readline can wait indefinitely for a newline if a"` | — |
| [SRC-EEF2E6447C-L000123](../../api/omarai.py#L123) | 123 | `"    client keeps trickling bytes. This reader checks the same deadline before"` | — |
| [SRC-EEF2E6447C-L000124](../../api/omarai.py#L124) | 124 | `"    every socket read and buffers only bounded look-ahead so request body bytes"` | — |
| [SRC-EEF2E6447C-L000125](../../api/omarai.py#L125) | 125 | `"    received with the headers are preserved for read1()."` | — |
| [SRC-EEF2E6447C-L000126](../../api/omarai.py#L126) | 126 | `"    \"\"\""` | — |
| [SRC-EEF2E6447C-L000127](../../api/omarai.py#L127) | 127 | `""` | — |
| [SRC-EEF2E6447C-L000128](../../api/omarai.py#L128) | 128 | `"    def __init__(self, connection, handler):"` | — |
| [SRC-EEF2E6447C-L000129](../../api/omarai.py#L129) | 129 | `"        self.connection = connection"` | — |
| [SRC-EEF2E6447C-L000130](../../api/omarai.py#L130) | 130 | `"        self.handler = handler"` | — |
| [SRC-EEF2E6447C-L000131](../../api/omarai.py#L131) | 131 | `"        self._buffer = bytearray()"` | — |
| [SRC-EEF2E6447C-L000132](../../api/omarai.py#L132) | 132 | `""` | — |
| [SRC-EEF2E6447C-L000133](../../api/omarai.py#L133) | 133 | `"    def readline(self, limit=-1):"` | — |
| [SRC-EEF2E6447C-L000134](../../api/omarai.py#L134) | 134 | `"        if limit == 0:"` | — |
| [SRC-EEF2E6447C-L000135](../../api/omarai.py#L135) | 135 | `"            return b\"\""` | — |
| [SRC-EEF2E6447C-L000136](../../api/omarai.py#L136) | 136 | `"        max_bytes = int(limit) if limit is not None and limit > 0 else 65_537"` | — |
| [SRC-EEF2E6447C-L000137](../../api/omarai.py#L137) | 137 | `"        previous_timeout = self.connection.gettimeout()"` | — |
| [SRC-EEF2E6447C-L000138](../../api/omarai.py#L138) | 138 | `"        line = bytearray()"` | — |
| [SRC-EEF2E6447C-L000139](../../api/omarai.py#L139) | 139 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000140](../../api/omarai.py#L140) | 140 | `"            while len(line) < max_bytes:"` | — |
| [SRC-EEF2E6447C-L000141](../../api/omarai.py#L141) | 141 | `"                deadline = getattr(self.handler, \"_request_header_deadline\", None)"` | — |
| [SRC-EEF2E6447C-L000142](../../api/omarai.py#L142) | 142 | `"                if deadline is None:"` | — |
| [SRC-EEF2E6447C-L000143](../../api/omarai.py#L143) | 143 | `"                    raise TimeoutError(\"request-header deadline is not active\")"` | — |
| [SRC-EEF2E6447C-L000144](../../api/omarai.py#L144) | 144 | `"                remaining = deadline - time.monotonic()"` | — |
| [SRC-EEF2E6447C-L000145](../../api/omarai.py#L145) | 145 | `"                if remaining <= 0:"` | — |
| [SRC-EEF2E6447C-L000146](../../api/omarai.py#L146) | 146 | `"                    raise TimeoutError(\"absolute request-header deadline exceeded\")"` | — |
| [SRC-EEF2E6447C-L000147](../../api/omarai.py#L147) | 147 | `""` | — |
| [SRC-EEF2E6447C-L000148](../../api/omarai.py#L148) | 148 | `"                newline_index = self._buffer.find(b\"\\n\")"` | — |
| [SRC-EEF2E6447C-L000149](../../api/omarai.py#L149) | 149 | `"                if newline_index >= 0:"` | — |
| [SRC-EEF2E6447C-L000150](../../api/omarai.py#L150) | 150 | `"                    take = min(newline_index + 1, max_bytes - len(line))"` | — |
| [SRC-EEF2E6447C-L000151](../../api/omarai.py#L151) | 151 | `"                    line.extend(self._buffer[:take])"` | — |
| [SRC-EEF2E6447C-L000152](../../api/omarai.py#L152) | 152 | `"                    del self._buffer[:take]"` | — |
| [SRC-EEF2E6447C-L000153](../../api/omarai.py#L153) | 153 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000154](../../api/omarai.py#L154) | 154 | `""` | — |
| [SRC-EEF2E6447C-L000155](../../api/omarai.py#L155) | 155 | `"                if self._buffer:"` | — |
| [SRC-EEF2E6447C-L000156](../../api/omarai.py#L156) | 156 | `"                    take = min(len(self._buffer), max_bytes - len(line))"` | — |
| [SRC-EEF2E6447C-L000157](../../api/omarai.py#L157) | 157 | `"                    line.extend(self._buffer[:take])"` | — |
| [SRC-EEF2E6447C-L000158](../../api/omarai.py#L158) | 158 | `"                    del self._buffer[:take]"` | — |
| [SRC-EEF2E6447C-L000159](../../api/omarai.py#L159) | 159 | `"                    if len(line) >= max_bytes:"` | — |
| [SRC-EEF2E6447C-L000160](../../api/omarai.py#L160) | 160 | `"                        break"` | — |
| [SRC-EEF2E6447C-L000161](../../api/omarai.py#L161) | 161 | `""` | — |
| [SRC-EEF2E6447C-L000162](../../api/omarai.py#L162) | 162 | `"                remaining = deadline - time.monotonic()"` | — |
| [SRC-EEF2E6447C-L000163](../../api/omarai.py#L163) | 163 | `"                if remaining <= 0:"` | — |
| [SRC-EEF2E6447C-L000164](../../api/omarai.py#L164) | 164 | `"                    raise TimeoutError(\"absolute request-header deadline exceeded\")"` | — |
| [SRC-EEF2E6447C-L000165](../../api/omarai.py#L165) | 165 | `"                idle_timeout = max("` | — |
| [SRC-EEF2E6447C-L000166](../../api/omarai.py#L166) | 166 | `"                    0.1,"` | — |
| [SRC-EEF2E6447C-L000167](../../api/omarai.py#L167) | 167 | `"                    min("` | — |
| [SRC-EEF2E6447C-L000168](../../api/omarai.py#L168) | 168 | `"                        float(REQUEST_HEADER_IDLE_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000169](../../api/omarai.py#L169) | 169 | `"                        MAX_REQUEST_HEADER_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000170](../../api/omarai.py#L170) | 170 | `"                    ),"` | — |
| [SRC-EEF2E6447C-L000171](../../api/omarai.py#L171) | 171 | `"                )"` | — |
| [SRC-EEF2E6447C-L000172](../../api/omarai.py#L172) | 172 | `"                self.connection.settimeout(min(idle_timeout, remaining))"` | — |
| [SRC-EEF2E6447C-L000173](../../api/omarai.py#L173) | 173 | `"                chunk = self.connection.recv(min(4_096, max_bytes - len(line)))"` | — |
| [SRC-EEF2E6447C-L000174](../../api/omarai.py#L174) | 174 | `"                if not chunk:"` | — |
| [SRC-EEF2E6447C-L000175](../../api/omarai.py#L175) | 175 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000176](../../api/omarai.py#L176) | 176 | `"                self._buffer.extend(chunk)"` | — |
| [SRC-EEF2E6447C-L000177](../../api/omarai.py#L177) | 177 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000178](../../api/omarai.py#L178) | 178 | `"            try:"` | — |
| [SRC-EEF2E6447C-L000179](../../api/omarai.py#L179) | 179 | `"                self.connection.settimeout(previous_timeout)"` | — |
| [SRC-EEF2E6447C-L000180](../../api/omarai.py#L180) | 180 | `"            except OSError:"` | — |
| [SRC-EEF2E6447C-L000181](../../api/omarai.py#L181) | 181 | `"                pass"` | — |
| [SRC-EEF2E6447C-L000182](../../api/omarai.py#L182) | 182 | `"        return bytes(line)"` | — |
| [SRC-EEF2E6447C-L000183](../../api/omarai.py#L183) | 183 | `""` | — |
| [SRC-EEF2E6447C-L000184](../../api/omarai.py#L184) | 184 | `"    def read1(self, size=-1):"` | — |
| [SRC-EEF2E6447C-L000185](../../api/omarai.py#L185) | 185 | `"        \"\"\"Read one chunk; body code applies its own idle and absolute deadlines.\"\"\""` | — |
| [SRC-EEF2E6447C-L000186](../../api/omarai.py#L186) | 186 | `"        if size == 0:"` | — |
| [SRC-EEF2E6447C-L000187](../../api/omarai.py#L187) | 187 | `"            return b\"\""` | — |
| [SRC-EEF2E6447C-L000188](../../api/omarai.py#L188) | 188 | `"        if size is None or size < 0:"` | — |
| [SRC-EEF2E6447C-L000189](../../api/omarai.py#L189) | 189 | `"            size = 8_192"` | — |
| [SRC-EEF2E6447C-L000190](../../api/omarai.py#L190) | 190 | `"        if self._buffer:"` | — |
| [SRC-EEF2E6447C-L000191](../../api/omarai.py#L191) | 191 | `"            take = min(len(self._buffer), size)"` | — |
| [SRC-EEF2E6447C-L000192](../../api/omarai.py#L192) | 192 | `"            data = bytes(self._buffer[:take])"` | — |
| [SRC-EEF2E6447C-L000193](../../api/omarai.py#L193) | 193 | `"            del self._buffer[:take]"` | — |
| [SRC-EEF2E6447C-L000194](../../api/omarai.py#L194) | 194 | `"            return data"` | — |
| [SRC-EEF2E6447C-L000195](../../api/omarai.py#L195) | 195 | `"        return self.connection.recv(size)"` | — |
| [SRC-EEF2E6447C-L000196](../../api/omarai.py#L196) | 196 | `""` | — |
| [SRC-EEF2E6447C-L000197](../../api/omarai.py#L197) | 197 | `"    def close(self):"` | — |
| [SRC-EEF2E6447C-L000198](../../api/omarai.py#L198) | 198 | `"        # The request handler owns the socket and closes its output stream."` | — |
| [SRC-EEF2E6447C-L000199](../../api/omarai.py#L199) | 199 | `"        return None"` | — |
| [SRC-EEF2E6447C-L000200](../../api/omarai.py#L200) | 200 | `""` | — |
| [SRC-EEF2E6447C-L000201](../../api/omarai.py#L201) | 201 | `""` | — |
| [SRC-EEF2E6447C-L000202](../../api/omarai.py#L202) | 202 | `"def _configured_agent_concurrency_limit() -> int:"` | — |
| [SRC-EEF2E6447C-L000203](../../api/omarai.py#L203) | 203 | `"    \"\"\"Return a process-local cap for expensive research and diagnostics operations.\"\"\""` | — |
| [SRC-EEF2E6447C-L000204](../../api/omarai.py#L204) | 204 | `"    try:"` | — |
| [SRC-EEF2E6447C-L000205](../../api/omarai.py#L205) | 205 | `"        configured = int(os.getenv(\"OMARAI_MAX_CONCURRENT_AGENT_REQUESTS\", \"4\").strip())"` | — |
| [SRC-EEF2E6447C-L000206](../../api/omarai.py#L206) | 206 | `"    except ValueError:"` | — |
| [SRC-EEF2E6447C-L000207](../../api/omarai.py#L207) | 207 | `"        configured = 4"` | — |
| [SRC-EEF2E6447C-L000208](../../api/omarai.py#L208) | 208 | `"    return max(1, min(configured, 8))"` | — |
| [SRC-EEF2E6447C-L000209](../../api/omarai.py#L209) | 209 | `""` | — |
| [SRC-EEF2E6447C-L000210](../../api/omarai.py#L210) | 210 | `""` | — |
| [SRC-EEF2E6447C-L000211](../../api/omarai.py#L211) | 211 | `"DEFAULT_HTTP_CONNECTION_LIMIT = 32"` | — |
| [SRC-EEF2E6447C-L000212](../../api/omarai.py#L212) | 212 | `"MAX_HTTP_CONNECTION_LIMIT = 128"` | — |
| [SRC-EEF2E6447C-L000213](../../api/omarai.py#L213) | 213 | `""` | — |
| [SRC-EEF2E6447C-L000214](../../api/omarai.py#L214) | 214 | `""` | — |
| [SRC-EEF2E6447C-L000215](../../api/omarai.py#L215) | 215 | `"def _configured_http_connection_limit() -> int:"` | — |
| [SRC-EEF2E6447C-L000216](../../api/omarai.py#L216) | 216 | `"    \"\"\"Return the bounded number of live HTTP handler threads for this process.\"\"\""` | — |
| [SRC-EEF2E6447C-L000217](../../api/omarai.py#L217) | 217 | `"    try:"` | — |
| [SRC-EEF2E6447C-L000218](../../api/omarai.py#L218) | 218 | `"        configured = int(os.getenv(\"OMARAI_MAX_CONCURRENT_HTTP_CONNECTIONS\", \"32\").strip())"` | — |
| [SRC-EEF2E6447C-L000219](../../api/omarai.py#L219) | 219 | `"    except ValueError:"` | — |
| [SRC-EEF2E6447C-L000220](../../api/omarai.py#L220) | 220 | `"        configured = DEFAULT_HTTP_CONNECTION_LIMIT"` | — |
| [SRC-EEF2E6447C-L000221](../../api/omarai.py#L221) | 221 | `"    return max(1, min(configured, MAX_HTTP_CONNECTION_LIMIT))"` | — |
| [SRC-EEF2E6447C-L000222](../../api/omarai.py#L222) | 222 | `""` | — |
| [SRC-EEF2E6447C-L000223](../../api/omarai.py#L223) | 223 | `""` | — |
| [SRC-EEF2E6447C-L000224](../../api/omarai.py#L224) | 224 | `"BUILD_SHA_FILE = Path(__file__).resolve().parents[1] / \"BUILD_SHA\""` | — |
| [SRC-EEF2E6447C-L000225](../../api/omarai.py#L225) | 225 | `"_PLATFORM_BUILD_SHA_ENVIRONMENTS = ("` | — |
| [SRC-EEF2E6447C-L000226](../../api/omarai.py#L226) | 226 | `"    (\"RAILWAY_GIT_COMMIT_SHA\", \"platform:railway\"),"` | — |
| [SRC-EEF2E6447C-L000227](../../api/omarai.py#L227) | 227 | `"    (\"RENDER_GIT_COMMIT\", \"platform:render\"),"` | — |
| [SRC-EEF2E6447C-L000228](../../api/omarai.py#L228) | 228 | `")"` | — |
| [SRC-EEF2E6447C-L000229](../../api/omarai.py#L229) | 229 | `""` | — |
| [SRC-EEF2E6447C-L000230](../../api/omarai.py#L230) | 230 | `""` | — |
| [SRC-EEF2E6447C-L000231](../../api/omarai.py#L231) | 231 | `"def _valid_build_sha(value: str) -> bool:"` | — |
| [SRC-EEF2E6447C-L000232](../../api/omarai.py#L232) | 232 | `"    candidate = value.strip().lower()"` | — |
| [SRC-EEF2E6447C-L000233](../../api/omarai.py#L233) | 233 | `"    return len(candidate) == 40 and all(char in \"0123456789abcdef\" for char in candidate)"` | — |
| [SRC-EEF2E6447C-L000234](../../api/omarai.py#L234) | 234 | `""` | — |
| [SRC-EEF2E6447C-L000235](../../api/omarai.py#L235) | 235 | `""` | — |
| [SRC-EEF2E6447C-L000236](../../api/omarai.py#L236) | 236 | `"def _build_identity() -> tuple[str, str]:"` | — |
| [SRC-EEF2E6447C-L000237](../../api/omarai.py#L237) | 237 | `"    \"\"\"Prefer immutable image metadata, then documented hosting-provided Git SHAs.\"\"\""` | — |
| [SRC-EEF2E6447C-L000238](../../api/omarai.py#L238) | 238 | `"    try:"` | — |
| [SRC-EEF2E6447C-L000239](../../api/omarai.py#L239) | 239 | `"        baked = BUILD_SHA_FILE.read_text(encoding=\"ascii\").strip().lower()"` | — |
| [SRC-EEF2E6447C-L000240](../../api/omarai.py#L240) | 240 | `"    except (OSError, UnicodeError):"` | — |
| [SRC-EEF2E6447C-L000241](../../api/omarai.py#L241) | 241 | `"        baked = \"\""` | — |
| [SRC-EEF2E6447C-L000242](../../api/omarai.py#L242) | 242 | `"    if _valid_build_sha(baked):"` | — |
| [SRC-EEF2E6447C-L000243](../../api/omarai.py#L243) | 243 | `"        return baked, \"image_baked\""` | — |
| [SRC-EEF2E6447C-L000244](../../api/omarai.py#L244) | 244 | `""` | — |
| [SRC-EEF2E6447C-L000245](../../api/omarai.py#L245) | 245 | `"    for environment_name, source in _PLATFORM_BUILD_SHA_ENVIRONMENTS:"` | — |
| [SRC-EEF2E6447C-L000246](../../api/omarai.py#L246) | 246 | `"        candidate = os.getenv(environment_name, \"\").strip().lower()"` | — |
| [SRC-EEF2E6447C-L000247](../../api/omarai.py#L247) | 247 | `"        if _valid_build_sha(candidate):"` | — |
| [SRC-EEF2E6447C-L000248](../../api/omarai.py#L248) | 248 | `"            return candidate, source"` | — |
| [SRC-EEF2E6447C-L000249](../../api/omarai.py#L249) | 249 | `"    return \"unknown\", \"unknown\""` | — |
| [SRC-EEF2E6447C-L000250](../../api/omarai.py#L250) | 250 | `""` | — |
| [SRC-EEF2E6447C-L000251](../../api/omarai.py#L251) | 251 | `""` | — |
| [SRC-EEF2E6447C-L000252](../../api/omarai.py#L252) | 252 | `"def _build_sha() -> str:"` | — |
| [SRC-EEF2E6447C-L000253](../../api/omarai.py#L253) | 253 | `"    \"\"\"Return a validated source SHA, or 'unknown' when no trusted build evidence exists.\"\"\""` | — |
| [SRC-EEF2E6447C-L000254](../../api/omarai.py#L254) | 254 | `"    return _build_identity()[0]"` | — |
| [SRC-EEF2E6447C-L000255](../../api/omarai.py#L255) | 255 | `""` | — |
| [SRC-EEF2E6447C-L000256](../../api/omarai.py#L256) | 256 | `""` | — |
| [SRC-EEF2E6447C-L000257](../../api/omarai.py#L257) | 257 | `"class Handler(BaseHTTPRequestHandler):"` | — |
| [SRC-EEF2E6447C-L000258](../../api/omarai.py#L258) | 258 | `"    def setup(self):"` | — |
| [SRC-EEF2E6447C-L000259](../../api/omarai.py#L259) | 259 | `"        \"\"\"Install a reader with a strict deadline for the request line and headers.\"\"\""` | — |
| [SRC-EEF2E6447C-L000260](../../api/omarai.py#L260) | 260 | `"        self.connection = self.request"` | — |
| [SRC-EEF2E6447C-L000261](../../api/omarai.py#L261) | 261 | `"        if self.timeout is not None:"` | — |
| [SRC-EEF2E6447C-L000262](../../api/omarai.py#L262) | 262 | `"            self.connection.settimeout(self.timeout)"` | — |
| [SRC-EEF2E6447C-L000263](../../api/omarai.py#L263) | 263 | `"        self._request_header_deadline = None"` | — |
| [SRC-EEF2E6447C-L000264](../../api/omarai.py#L264) | 264 | `"        self.rfile = _DeadlineRequestReader(self.connection, self)"` | — |
| [SRC-EEF2E6447C-L000265](../../api/omarai.py#L265) | 265 | `"        self.wfile = self.connection.makefile(\"wb\", self.wbufsize)"` | — |
| [SRC-EEF2E6447C-L000266](../../api/omarai.py#L266) | 266 | `""` | — |
| [SRC-EEF2E6447C-L000267](../../api/omarai.py#L267) | 267 | `"    def handle_one_request(self):"` | — |
| [SRC-EEF2E6447C-L000268](../../api/omarai.py#L268) | 268 | `"        timeout = max("` | — |
| [SRC-EEF2E6447C-L000269](../../api/omarai.py#L269) | 269 | `"            0.1,"` | — |
| [SRC-EEF2E6447C-L000270](../../api/omarai.py#L270) | 270 | `"            min("` | — |
| [SRC-EEF2E6447C-L000271](../../api/omarai.py#L271) | 271 | `"                float(REQUEST_HEADER_READ_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000272](../../api/omarai.py#L272) | 272 | `"                MAX_REQUEST_HEADER_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000273](../../api/omarai.py#L273) | 273 | `"            ),"` | — |
| [SRC-EEF2E6447C-L000274](../../api/omarai.py#L274) | 274 | `"        )"` | — |
| [SRC-EEF2E6447C-L000275](../../api/omarai.py#L275) | 275 | `"        self._request_header_deadline = time.monotonic() + timeout"` | — |
| [SRC-EEF2E6447C-L000276](../../api/omarai.py#L276) | 276 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000277](../../api/omarai.py#L277) | 277 | `"            super().handle_one_request()"` | — |
| [SRC-EEF2E6447C-L000278](../../api/omarai.py#L278) | 278 | `"        except TimeoutError:"` | — |
| [SRC-EEF2E6447C-L000279](../../api/omarai.py#L279) | 279 | `"            # Incomplete request line/headers are untrusted protocol input;"` | — |
| [SRC-EEF2E6447C-L000280](../../api/omarai.py#L280) | 280 | `"            # close the socket without trying to parse or answer a partial request."` | — |
| [SRC-EEF2E6447C-L000281](../../api/omarai.py#L281) | 281 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000282](../../api/omarai.py#L282) | 282 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000283](../../api/omarai.py#L283) | 283 | `"            self._request_header_deadline = None"` | — |
| [SRC-EEF2E6447C-L000284](../../api/omarai.py#L284) | 284 | `""` | — |
| [SRC-EEF2E6447C-L000285](../../api/omarai.py#L285) | 285 | `"    def parse_request(self):"` | — |
| [SRC-EEF2E6447C-L000286](../../api/omarai.py#L286) | 286 | `"        \"\"\"Reject ambiguous HTTP message framing before dispatching any handler.\"\"\""` | — |
| [SRC-EEF2E6447C-L000287](../../api/omarai.py#L287) | 287 | `"        if not super().parse_request():"` | — |
| [SRC-EEF2E6447C-L000288](../../api/omarai.py#L288) | 288 | `"            return False"` | — |
| [SRC-EEF2E6447C-L000289](../../api/omarai.py#L289) | 289 | `""` | — |
| [SRC-EEF2E6447C-L000290](../../api/omarai.py#L290) | 290 | `"        transfer_encodings = self.headers.get_all(\"Transfer-Encoding\", [])"` | — |
| [SRC-EEF2E6447C-L000291](../../api/omarai.py#L291) | 291 | `"        if transfer_encodings:"` | — |
| [SRC-EEF2E6447C-L000292](../../api/omarai.py#L292) | 292 | `"            # This API does not implement chunked request decoding. Never let a"` | — |
| [SRC-EEF2E6447C-L000293](../../api/omarai.py#L293) | 293 | `"            # proxy/backend disagree about where the request body ends."` | — |
| [SRC-EEF2E6447C-L000294](../../api/omarai.py#L294) | 294 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000295](../../api/omarai.py#L295) | 295 | `"            self.send_error(400, \"Transfer-Encoding is not supported\")"` | — |
| [SRC-EEF2E6447C-L000296](../../api/omarai.py#L296) | 296 | `"            return False"` | — |
| [SRC-EEF2E6447C-L000297](../../api/omarai.py#L297) | 297 | `""` | — |
| [SRC-EEF2E6447C-L000298](../../api/omarai.py#L298) | 298 | `"        content_lengths = self.headers.get_all(\"Content-Length\", [])"` | — |
| [SRC-EEF2E6447C-L000299](../../api/omarai.py#L299) | 299 | `"        if len(content_lengths) > 1:"` | — |
| [SRC-EEF2E6447C-L000300](../../api/omarai.py#L300) | 300 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000301](../../api/omarai.py#L301) | 301 | `"            self.send_error(400, \"Multiple Content-Length headers are not supported\")"` | — |
| [SRC-EEF2E6447C-L000302](../../api/omarai.py#L302) | 302 | `"            return False"` | — |
| [SRC-EEF2E6447C-L000303](../../api/omarai.py#L303) | 303 | `""` | — |
| [SRC-EEF2E6447C-L000304](../../api/omarai.py#L304) | 304 | `"        if content_lengths:"` | — |
| [SRC-EEF2E6447C-L000305](../../api/omarai.py#L305) | 305 | `"            raw_size = content_lengths[0].strip()"` | — |
| [SRC-EEF2E6447C-L000306](../../api/omarai.py#L306) | 306 | `"            if not raw_size or not raw_size.isascii() or not raw_size.isdecimal():"` | — |
| [SRC-EEF2E6447C-L000307](../../api/omarai.py#L307) | 307 | `"                self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000308](../../api/omarai.py#L308) | 308 | `"                self.send_error(400, \"valid Content-Length is required\")"` | — |
| [SRC-EEF2E6447C-L000309](../../api/omarai.py#L309) | 309 | `"                return False"` | — |
| [SRC-EEF2E6447C-L000310](../../api/omarai.py#L310) | 310 | `"            if self.command != \"POST\" and raw_size.lstrip(\"0\"):"` | — |
| [SRC-EEF2E6447C-L000311](../../api/omarai.py#L311) | 311 | `"                # GET/HEAD/other methods are not allowed to leave unread bytes"` | — |
| [SRC-EEF2E6447C-L000312](../../api/omarai.py#L312) | 312 | `"                # on a persistent connection."` | — |
| [SRC-EEF2E6447C-L000313](../../api/omarai.py#L313) | 313 | `"                self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000314](../../api/omarai.py#L314) | 314 | `"                self.send_error(400, \"Content-Length body is not supported for this method\")"` | — |
| [SRC-EEF2E6447C-L000315](../../api/omarai.py#L315) | 315 | `"                return False"` | — |
| [SRC-EEF2E6447C-L000316](../../api/omarai.py#L316) | 316 | `""` | — |
| [SRC-EEF2E6447C-L000317](../../api/omarai.py#L317) | 317 | `"        return True"` | — |
| [SRC-EEF2E6447C-L000318](../../api/omarai.py#L318) | 318 | `""` | — |
| [SRC-EEF2E6447C-L000319](../../api/omarai.py#L319) | 319 | `"    store = _lead_store_from_environment()"` | — |
| [SRC-EEF2E6447C-L000320](../../api/omarai.py#L320) | 320 | `"    _rate_lock = threading.Lock()"` | — |
| [SRC-EEF2E6447C-L000321](../../api/omarai.py#L321) | 321 | `"    _request_times: ClassVar[dict[str, deque[float]]] = defaultdict(deque)"` | — |
| [SRC-EEF2E6447C-L000322](../../api/omarai.py#L322) | 322 | `"    _rate_last_cleanup: ClassVar[float] = 0.0"` | — |
| [SRC-EEF2E6447C-L000323](../../api/omarai.py#L323) | 323 | `"    RATE_LIMIT_REQUESTS = 20"` | — |
| [SRC-EEF2E6447C-L000324](../../api/omarai.py#L324) | 324 | `"    RATE_LIMIT_WINDOW_SECONDS = 60"` | — |
| [SRC-EEF2E6447C-L000325](../../api/omarai.py#L325) | 325 | `"    RATE_LIMIT_CLEANUP_INTERVAL_SECONDS = 60"` | — |
| [SRC-EEF2E6447C-L000326](../../api/omarai.py#L326) | 326 | `"    # Reserve the final bucket for clients beyond the per-process tracking ceiling."` | — |
| [SRC-EEF2E6447C-L000327](../../api/omarai.py#L327) | 327 | `"    MAX_RATE_LIMIT_CLIENT_BUCKETS = 4096"` | — |
| [SRC-EEF2E6447C-L000328](../../api/omarai.py#L328) | 328 | `"    RATE_LIMIT_OVERFLOW_KEY = \"__omarai_overflow__\""` | — |
| [SRC-EEF2E6447C-L000329](../../api/omarai.py#L329) | 329 | `"    AGENT_CONCURRENCY_LIMIT = _configured_agent_concurrency_limit()"` | — |
| [SRC-EEF2E6447C-L000330](../../api/omarai.py#L330) | 330 | `"    _agent_semaphore = threading.BoundedSemaphore(AGENT_CONCURRENCY_LIMIT)"` | — |
| [SRC-EEF2E6447C-L000331](../../api/omarai.py#L331) | 331 | `""` | — |
| [SRC-EEF2E6447C-L000332](../../api/omarai.py#L332) | 332 | `"    def _run_bounded_agent_operation(self, operation):"` | — |
| [SRC-EEF2E6447C-L000333](../../api/omarai.py#L333) | 333 | `"        \"\"\"Run an expensive operation only when a process-local slot is available.\"\"\""` | — |
| [SRC-EEF2E6447C-L000334](../../api/omarai.py#L334) | 334 | `"        cls = type(self)"` | — |
| [SRC-EEF2E6447C-L000335](../../api/omarai.py#L335) | 335 | `"        if not cls._agent_semaphore.acquire(blocking=False):"` | — |
| [SRC-EEF2E6447C-L000336](../../api/omarai.py#L336) | 336 | `"            return self.respond("` | — |
| [SRC-EEF2E6447C-L000337](../../api/omarai.py#L337) | 337 | `"                503,"` | — |
| [SRC-EEF2E6447C-L000338](../../api/omarai.py#L338) | 338 | `"                {"` | — |
| [SRC-EEF2E6447C-L000339](../../api/omarai.py#L339) | 339 | `"                    \"error\": \"خدمة البحث مشغولة حاليًا؛ أعد المحاولة بعد قليل.\","` | — |
| [SRC-EEF2E6447C-L000340](../../api/omarai.py#L340) | 340 | `"                    \"retry_after_seconds\": 5,"` | — |
| [SRC-EEF2E6447C-L000341](../../api/omarai.py#L341) | 341 | `"                    \"process_concurrency_limit\": cls.AGENT_CONCURRENCY_LIMIT,"` | — |
| [SRC-EEF2E6447C-L000342](../../api/omarai.py#L342) | 342 | `"                },"` | — |
| [SRC-EEF2E6447C-L000343](../../api/omarai.py#L343) | 343 | `"            )"` | — |
| [SRC-EEF2E6447C-L000344](../../api/omarai.py#L344) | 344 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000345](../../api/omarai.py#L345) | 345 | `"            return self.respond(200, operation())"` | — |
| [SRC-EEF2E6447C-L000346](../../api/omarai.py#L346) | 346 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000347](../../api/omarai.py#L347) | 347 | `"            cls._agent_semaphore.release()"` | — |
| [SRC-EEF2E6447C-L000348](../../api/omarai.py#L348) | 348 | `""` | — |
| [SRC-EEF2E6447C-L000349](../../api/omarai.py#L349) | 349 | `"    def _session_cookie_name(self):"` | — |
| [SRC-EEF2E6447C-L000350](../../api/omarai.py#L350) | 350 | `"        \"\"\"Use the __Host- prefix on HTTPS public deployments.\"\"\""` | — |
| [SRC-EEF2E6447C-L000351](../../api/omarai.py#L351) | 351 | `"        if os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() == \"1\":"` | — |
| [SRC-EEF2E6447C-L000352](../../api/omarai.py#L352) | 352 | `"            return \"__Host-omarai_session\""` | — |
| [SRC-EEF2E6447C-L000353](../../api/omarai.py#L353) | 353 | `"        return \"omarai_session\""` | — |
| [SRC-EEF2E6447C-L000354](../../api/omarai.py#L354) | 354 | `""` | — |
| [SRC-EEF2E6447C-L000355](../../api/omarai.py#L355) | 355 | `"    def _session_cookie_header(self, token: str) -> str:"` | — |
| [SRC-EEF2E6447C-L000356](../../api/omarai.py#L356) | 356 | `"        if not BROWSER_SESSION_ID_RE.fullmatch(token):"` | — |
| [SRC-EEF2E6447C-L000357](../../api/omarai.py#L357) | 357 | `"            raise ValueError(\"browser access token has an unsupported format\")"` | — |
| [SRC-EEF2E6447C-L000358](../../api/omarai.py#L358) | 358 | `"        parts = ["` | — |
| [SRC-EEF2E6447C-L000359](../../api/omarai.py#L359) | 359 | `"            f\"{self._session_cookie_name()}={token}\","` | — |
| [SRC-EEF2E6447C-L000360](../../api/omarai.py#L360) | 360 | `"            \"Path=/\","` | — |
| [SRC-EEF2E6447C-L000361](../../api/omarai.py#L361) | 361 | `"            \"HttpOnly\","` | — |
| [SRC-EEF2E6447C-L000362](../../api/omarai.py#L362) | 362 | `"            \"SameSite=Strict\","` | — |
| [SRC-EEF2E6447C-L000363](../../api/omarai.py#L363) | 363 | `"            f\"Max-Age={BROWSER_SESSION_COOKIE_MAX_AGE}\","` | — |
| [SRC-EEF2E6447C-L000364](../../api/omarai.py#L364) | 364 | `"        ]"` | — |
| [SRC-EEF2E6447C-L000365](../../api/omarai.py#L365) | 365 | `"        if os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() == \"1\":"` | — |
| [SRC-EEF2E6447C-L000366](../../api/omarai.py#L366) | 366 | `"            parts.insert(2, \"Secure\")"` | — |
| [SRC-EEF2E6447C-L000367](../../api/omarai.py#L367) | 367 | `"        return \"; \".join(parts)"` | — |
| [SRC-EEF2E6447C-L000368](../../api/omarai.py#L368) | 368 | `""` | — |
| [SRC-EEF2E6447C-L000369](../../api/omarai.py#L369) | 369 | `"    def _clear_session_cookie_header(self) -> str:"` | — |
| [SRC-EEF2E6447C-L000370](../../api/omarai.py#L370) | 370 | `"        parts = ["` | — |
| [SRC-EEF2E6447C-L000371](../../api/omarai.py#L371) | 371 | `"            f\"{self._session_cookie_name()}=\","` | — |
| [SRC-EEF2E6447C-L000372](../../api/omarai.py#L372) | 372 | `"            \"Path=/\","` | — |
| [SRC-EEF2E6447C-L000373](../../api/omarai.py#L373) | 373 | `"            \"HttpOnly\","` | — |
| [SRC-EEF2E6447C-L000374](../../api/omarai.py#L374) | 374 | `"            \"SameSite=Strict\","` | — |
| [SRC-EEF2E6447C-L000375](../../api/omarai.py#L375) | 375 | `"            \"Max-Age=0\","` | — |
| [SRC-EEF2E6447C-L000376](../../api/omarai.py#L376) | 376 | `"        ]"` | — |
| [SRC-EEF2E6447C-L000377](../../api/omarai.py#L377) | 377 | `"        if os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() == \"1\":"` | — |
| [SRC-EEF2E6447C-L000378](../../api/omarai.py#L378) | 378 | `"            parts.insert(2, \"Secure\")"` | — |
| [SRC-EEF2E6447C-L000379](../../api/omarai.py#L379) | 379 | `"        return \"; \".join(parts)"` | — |
| [SRC-EEF2E6447C-L000380](../../api/omarai.py#L380) | 380 | `""` | — |
| [SRC-EEF2E6447C-L000381](../../api/omarai.py#L381) | 381 | `"    def _principal_for_access_token(self, token: str):"` | — |
| [SRC-EEF2E6447C-L000382](../../api/omarai.py#L382) | 382 | `"        expected = os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000383](../../api/omarai.py#L383) | 383 | `"        if expected and hmac.compare_digest(token, expected):"` | — |
| [SRC-EEF2E6447C-L000384](../../api/omarai.py#L384) | 384 | `"            return self.store.default_principal()"` | — |
| [SRC-EEF2E6447C-L000385](../../api/omarai.py#L385) | 385 | `"        return self.store.resolve_api_token(token)"` | — |
| [SRC-EEF2E6447C-L000386](../../api/omarai.py#L386) | 386 | `""` | — |
| [SRC-EEF2E6447C-L000387](../../api/omarai.py#L387) | 387 | `"    def _authorized(self):"` | — |
| [SRC-EEF2E6447C-L000388](../../api/omarai.py#L388) | 388 | `"        \"\"\"Resolve a verified bearer token or HttpOnly browser cookie."` | — |
| [SRC-EEF2E6447C-L000389](../../api/omarai.py#L389) | 389 | `""` | — |
| [SRC-EEF2E6447C-L000390](../../api/omarai.py#L390) | 390 | `"        Browser cookies are accepted only with same-origin POST requests. Request-body"` | — |
| [SRC-EEF2E6447C-L000391](../../api/omarai.py#L391) | 391 | `"        tenant IDs are never used to establish tenant context."` | — |
| [SRC-EEF2E6447C-L000392](../../api/omarai.py#L392) | 392 | `"        \"\"\""` | — |
| [SRC-EEF2E6447C-L000393](../../api/omarai.py#L393) | 393 | `"        self._authenticated_principal = None"` | — |
| [SRC-EEF2E6447C-L000394](../../api/omarai.py#L394) | 394 | `"        self._cookie_authenticated = False"` | — |
| [SRC-EEF2E6447C-L000395](../../api/omarai.py#L395) | 395 | `"        self._browser_session_id = \"\""` | — |
| [SRC-EEF2E6447C-L000396](../../api/omarai.py#L396) | 396 | `"        supplied = self.headers.get(\"Authorization\", \"\")"` | — |
| [SRC-EEF2E6447C-L000397](../../api/omarai.py#L397) | 397 | `"        if supplied.startswith(\"Bearer \"):"` | — |
| [SRC-EEF2E6447C-L000398](../../api/omarai.py#L398) | 398 | `"            token = supplied[7:].strip()"` | — |
| [SRC-EEF2E6447C-L000399](../../api/omarai.py#L399) | 399 | `"            self._authenticated_principal = self._principal_for_access_token(token)"` | — |
| [SRC-EEF2E6447C-L000400](../../api/omarai.py#L400) | 400 | `"            return bool(self._authenticated_principal)"` | — |
| [SRC-EEF2E6447C-L000401](../../api/omarai.py#L401) | 401 | `""` | — |
| [SRC-EEF2E6447C-L000402](../../api/omarai.py#L402) | 402 | `"        cookie = SimpleCookie()"` | — |
| [SRC-EEF2E6447C-L000403](../../api/omarai.py#L403) | 403 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000404](../../api/omarai.py#L404) | 404 | `"            cookie.load(self.headers.get(\"Cookie\", \"\"))"` | — |
| [SRC-EEF2E6447C-L000405](../../api/omarai.py#L405) | 405 | `"        except Exception:"` | — |
| [SRC-EEF2E6447C-L000406](../../api/omarai.py#L406) | 406 | `"            cookie = SimpleCookie()"` | — |
| [SRC-EEF2E6447C-L000407](../../api/omarai.py#L407) | 407 | `"        morsel = cookie.get(self._session_cookie_name())"` | — |
| [SRC-EEF2E6447C-L000408](../../api/omarai.py#L408) | 408 | `"        if morsel is not None:"` | — |
| [SRC-EEF2E6447C-L000409](../../api/omarai.py#L409) | 409 | `"            token = morsel.value"` | — |
| [SRC-EEF2E6447C-L000410](../../api/omarai.py#L410) | 410 | `"            if BROWSER_SESSION_ID_RE.fullmatch(token):"` | — |
| [SRC-EEF2E6447C-L000411](../../api/omarai.py#L411) | 411 | `"                self._authenticated_principal = self.store.resolve_web_session("` | — |
| [SRC-EEF2E6447C-L000412](../../api/omarai.py#L412) | 412 | `"                    token,"` | — |
| [SRC-EEF2E6447C-L000413](../../api/omarai.py#L413) | 413 | `"                    shared_token=os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip(),"` | — |
| [SRC-EEF2E6447C-L000414](../../api/omarai.py#L414) | 414 | `"                )"` | — |
| [SRC-EEF2E6447C-L000415](../../api/omarai.py#L415) | 415 | `"                self._cookie_authenticated = bool(self._authenticated_principal)"` | — |
| [SRC-EEF2E6447C-L000416](../../api/omarai.py#L416) | 416 | `"                if self._cookie_authenticated:"` | — |
| [SRC-EEF2E6447C-L000417](../../api/omarai.py#L417) | 417 | `"                    self._browser_session_id = token"` | — |
| [SRC-EEF2E6447C-L000418](../../api/omarai.py#L418) | 418 | `"                return self._cookie_authenticated"` | — |
| [SRC-EEF2E6447C-L000419](../../api/omarai.py#L419) | 419 | `""` | — |
| [SRC-EEF2E6447C-L000420](../../api/omarai.py#L420) | 420 | `"        if os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() != \"1\":"` | — |
| [SRC-EEF2E6447C-L000421](../../api/omarai.py#L421) | 421 | `"            try:"` | — |
| [SRC-EEF2E6447C-L000422](../../api/omarai.py#L422) | 422 | `"                if ipaddress.ip_address(self.client_address[0]).is_loopback:"` | — |
| [SRC-EEF2E6447C-L000423](../../api/omarai.py#L423) | 423 | `"                    self._authenticated_principal = self.store.default_principal()"` | — |
| [SRC-EEF2E6447C-L000424](../../api/omarai.py#L424) | 424 | `"                    return bool(self._authenticated_principal)"` | — |
| [SRC-EEF2E6447C-L000425](../../api/omarai.py#L425) | 425 | `"            except ValueError:"` | — |
| [SRC-EEF2E6447C-L000426](../../api/omarai.py#L426) | 426 | `"                pass"` | — |
| [SRC-EEF2E6447C-L000427](../../api/omarai.py#L427) | 427 | `"        return False"` | — |
| [SRC-EEF2E6447C-L000428](../../api/omarai.py#L428) | 428 | `""` | — |
| [SRC-EEF2E6447C-L000429](../../api/omarai.py#L429) | 429 | `"    def _allowed_origins(self):"` | — |
| [SRC-EEF2E6447C-L000430](../../api/omarai.py#L430) | 430 | `"        \"\"\"Return configured browser origins plus this service’s own origin."` | — |
| [SRC-EEF2E6447C-L000431](../../api/omarai.py#L431) | 431 | `""` | — |
| [SRC-EEF2E6447C-L000432](../../api/omarai.py#L432) | 432 | `"        OMARAI_ALLOWED_ORIGINS is a comma-separated list of trusted origins"` | — |
| [SRC-EEF2E6447C-L000433](../../api/omarai.py#L433) | 433 | `"        (scheme + host + optional port; no path and no wildcard)."` | — |
| [SRC-EEF2E6447C-L000434](../../api/omarai.py#L434) | 434 | `"        \"\"\""` | — |
| [SRC-EEF2E6447C-L000435](../../api/omarai.py#L435) | 435 | `"        configured = os.getenv(\"OMARAI_ALLOWED_ORIGINS\", \"\")"` | — |
| [SRC-EEF2E6447C-L000436](../../api/omarai.py#L436) | 436 | `"        origins = {"` | — |
| [SRC-EEF2E6447C-L000437](../../api/omarai.py#L437) | 437 | `"            item.strip().rstrip(\"/\")"` | — |
| [SRC-EEF2E6447C-L000438](../../api/omarai.py#L438) | 438 | `"            for item in configured.split(\",\")"` | — |
| [SRC-EEF2E6447C-L000439](../../api/omarai.py#L439) | 439 | `"            if item.strip()"` | — |
| [SRC-EEF2E6447C-L000440](../../api/omarai.py#L440) | 440 | `"        }"` | — |
| [SRC-EEF2E6447C-L000441](../../api/omarai.py#L441) | 441 | `"        if os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() == \"1\":"` | — |
| [SRC-EEF2E6447C-L000442](../../api/omarai.py#L442) | 442 | `"            # Host identifies the requested service origin. Do not derive allowed"` | — |
| [SRC-EEF2E6447C-L000443](../../api/omarai.py#L443) | 443 | `"            # origins from X-Forwarded-Host: direct clients can spoof that header"` | — |
| [SRC-EEF2E6447C-L000444](../../api/omarai.py#L444) | 444 | `"            # unless the reverse proxy is separately configured to overwrite it."` | — |
| [SRC-EEF2E6447C-L000445](../../api/omarai.py#L445) | 445 | `"            scheme = self.headers.get(\"X-Forwarded-Proto\", \"https\").split(\",\", 1)[0].strip().lower()"` | — |
| [SRC-EEF2E6447C-L000446](../../api/omarai.py#L446) | 446 | `"            host = self.headers.get(\"Host\", \"\").split(\",\", 1)[0].strip()"` | — |
| [SRC-EEF2E6447C-L000447](../../api/omarai.py#L447) | 447 | `"            if host:"` | — |
| [SRC-EEF2E6447C-L000448](../../api/omarai.py#L448) | 448 | `"                origins.add(f\"https://{host}\".rstrip(\"/\"))"` | — |
| [SRC-EEF2E6447C-L000449](../../api/omarai.py#L449) | 449 | `"                origins.add(f\"{scheme}://{host}\".rstrip(\"/\"))"` | — |
| [SRC-EEF2E6447C-L000450](../../api/omarai.py#L450) | 450 | `"        else:"` | — |
| [SRC-EEF2E6447C-L000451](../../api/omarai.py#L451) | 451 | `"            port = self.server.server_port"` | — |
| [SRC-EEF2E6447C-L000452](../../api/omarai.py#L452) | 452 | `"            origins.update("` | — |
| [SRC-EEF2E6447C-L000453](../../api/omarai.py#L453) | 453 | `"                {"` | — |
| [SRC-EEF2E6447C-L000454](../../api/omarai.py#L454) | 454 | `"                    f\"http://127.0.0.1:{port}\","` | — |
| [SRC-EEF2E6447C-L000455](../../api/omarai.py#L455) | 455 | `"                    f\"http://localhost:{port}\","` | — |
| [SRC-EEF2E6447C-L000456](../../api/omarai.py#L456) | 456 | `"                    f\"http://[::1]:{port}\","` | — |
| [SRC-EEF2E6447C-L000457](../../api/omarai.py#L457) | 457 | `"                }"` | — |
| [SRC-EEF2E6447C-L000458](../../api/omarai.py#L458) | 458 | `"            )"` | — |
| [SRC-EEF2E6447C-L000459](../../api/omarai.py#L459) | 459 | `"        return origins"` | — |
| [SRC-EEF2E6447C-L000460](../../api/omarai.py#L460) | 460 | `""` | — |
| [SRC-EEF2E6447C-L000461](../../api/omarai.py#L461) | 461 | `"    def _origin_allowed(self, origin):"` | — |
| [SRC-EEF2E6447C-L000462](../../api/omarai.py#L462) | 462 | `"        return bool(origin) and origin.rstrip(\"/\") in self._allowed_origins()"` | — |
| [SRC-EEF2E6447C-L000463](../../api/omarai.py#L463) | 463 | `""` | — |
| [SRC-EEF2E6447C-L000464](../../api/omarai.py#L464) | 464 | `"    def _rate_limit_client_key(self):"` | — |
| [SRC-EEF2E6447C-L000465](../../api/omarai.py#L465) | 465 | `"        \"\"\"Choose a rate-limit identity without trusting spoofable proxy headers by default."` | — |
| [SRC-EEF2E6447C-L000466](../../api/omarai.py#L466) | 466 | `""` | — |
| [SRC-EEF2E6447C-L000467](../../api/omarai.py#L467) | 467 | `"        Set OMARAI_TRUST_PROXY_HEADERS=1 only when the deployment's trusted reverse"` | — |
| [SRC-EEF2E6447C-L000468](../../api/omarai.py#L468) | 468 | `"        proxy appends the actual client IP as the rightmost X-Forwarded-For value."` | — |
| [SRC-EEF2E6447C-L000469](../../api/omarai.py#L469) | 469 | `"        \"\"\""` | — |
| [SRC-EEF2E6447C-L000470](../../api/omarai.py#L470) | 470 | `"        direct_ip = self.client_address[0]"` | — |
| [SRC-EEF2E6447C-L000471](../../api/omarai.py#L471) | 471 | `"        if os.getenv(\"OMARAI_TRUST_PROXY_HEADERS\", \"\").strip() != \"1\":"` | — |
| [SRC-EEF2E6447C-L000472](../../api/omarai.py#L472) | 472 | `"            return direct_ip"` | — |
| [SRC-EEF2E6447C-L000473](../../api/omarai.py#L473) | 473 | `"        forwarded = self.headers.get(\"X-Forwarded-For\", \"\")"` | — |
| [SRC-EEF2E6447C-L000474](../../api/omarai.py#L474) | 474 | `"        candidate = forwarded.rsplit(\",\", 1)[-1].strip() if forwarded else \"\""` | — |
| [SRC-EEF2E6447C-L000475](../../api/omarai.py#L475) | 475 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000476](../../api/omarai.py#L476) | 476 | `"            return str(ipaddress.ip_address(candidate))"` | — |
| [SRC-EEF2E6447C-L000477](../../api/omarai.py#L477) | 477 | `"        except ValueError:"` | — |
| [SRC-EEF2E6447C-L000478](../../api/omarai.py#L478) | 478 | `"            return direct_ip"` | — |
| [SRC-EEF2E6447C-L000479](../../api/omarai.py#L479) | 479 | `""` | — |
| [SRC-EEF2E6447C-L000480](../../api/omarai.py#L480) | 480 | `"    def _rate_limit_ok(self):"` | — |
