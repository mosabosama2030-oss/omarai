# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **021**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L006840 إلى SRC-EEF2E6447C-L000125
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L006840](../../agents/web_agent.py#L6840) | 6840 | `"                            \"status\": \"searching_for_missing_criterion_evidence\","` | — |
| [SRC-1AE03B9EC3-L006841](../../agents/web_agent.py#L6841) | 6841 | `"                            \"query\": gap_query,"` | — |
| [SRC-1AE03B9EC3-L006842](../../agents/web_agent.py#L6842) | 6842 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L006843](../../agents/web_agent.py#L6843) | 6843 | `"                        gap_plan = dict(plan)"` | — |
| [SRC-1AE03B9EC3-L006844](../../agents/web_agent.py#L6844) | 6844 | `"                        gap_plan.update({"` | — |
| [SRC-1AE03B9EC3-L006845](../../agents/web_agent.py#L6845) | 6845 | `"                            \"queries\": [gap_query],"` | — |
| [SRC-1AE03B9EC3-L006846](../../agents/web_agent.py#L6846) | 6846 | `"                            \"query_limit\": 1,"` | — |
| [SRC-1AE03B9EC3-L006847](../../agents/web_agent.py#L6847) | 6847 | `"                            \"depth\": \"standard\","` | — |
| [SRC-1AE03B9EC3-L006848](../../agents/web_agent.py#L6848) | 6848 | `"                            \"social_focus\": False,"` | — |
| [SRC-1AE03B9EC3-L006849](../../agents/web_agent.py#L6849) | 6849 | `"                            \"platforms\": [],"` | — |
| [SRC-1AE03B9EC3-L006850](../../agents/web_agent.py#L6850) | 6850 | `"                            \"direct_urls\": [],"` | — |
| [SRC-1AE03B9EC3-L006851](../../agents/web_agent.py#L6851) | 6851 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L006852](../../agents/web_agent.py#L6852) | 6852 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L006853](../../agents/web_agent.py#L6853) | 6853 | `"                            gap_sources, gap_warnings, gap_report = self._collect_research(gap_plan)"` | — |
| [SRC-1AE03B9EC3-L006854](../../agents/web_agent.py#L6854) | 6854 | `"                        except (RuntimeError, AgentDependencyError, RequestBudgetExceeded, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L006855](../../agents/web_agent.py#L6855) | 6855 | `"                            gap_sources, gap_warnings = [], []"` | — |
| [SRC-1AE03B9EC3-L006856](../../agents/web_agent.py#L6856) | 6856 | `"                            gap_report = {"` | — |
| [SRC-1AE03B9EC3-L006857](../../agents/web_agent.py#L6857) | 6857 | `"                                \"queries_planned\": 1,"` | — |
| [SRC-1AE03B9EC3-L006858](../../agents/web_agent.py#L6858) | 6858 | `"                                \"queries_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L006859](../../agents/web_agent.py#L6859) | 6859 | `"                                \"queries_attempted_known\": False,"` | — |
| [SRC-1AE03B9EC3-L006860](../../agents/web_agent.py#L6860) | 6860 | `"                                \"search_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L006861](../../agents/web_agent.py#L6861) | 6861 | `"                                \"search_outcome\": \"unknown_after_research_error\","` | — |
| [SRC-1AE03B9EC3-L006862](../../agents/web_agent.py#L6862) | 6862 | `"                                \"query_results\": [],"` | — |
| [SRC-1AE03B9EC3-L006863](../../agents/web_agent.py#L6863) | 6863 | `"                            }"` | — |
| [SRC-1AE03B9EC3-L006864](../../agents/web_agent.py#L6864) | 6864 | `"                            criterion_gap_research[\"status\"] = \"search_failed\""` | — |
| [SRC-1AE03B9EC3-L006865](../../agents/web_agent.py#L6865) | 6865 | `"                            criterion_gap_research[\"error_class\"] = type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L006866](../../agents/web_agent.py#L6866) | 6866 | `"                        search_warnings.extend("` | — |
| [SRC-1AE03B9EC3-L006867](../../agents/web_agent.py#L6867) | 6867 | `"                            item for item in gap_warnings if isinstance(item, str)"` | — |
| [SRC-1AE03B9EC3-L006868](../../agents/web_agent.py#L6868) | 6868 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L006869](../../agents/web_agent.py#L6869) | 6869 | `"                        source_indexes: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L006870](../../agents/web_agent.py#L6870) | 6870 | `"                        for source_index, source in enumerate(sources):"` | — |
| [SRC-1AE03B9EC3-L006871](../../agents/web_agent.py#L6871) | 6871 | `"                            source_key = self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L006872](../../agents/web_agent.py#L6872) | 6872 | `"                            if source_key:"` | — |
| [SRC-1AE03B9EC3-L006873](../../agents/web_agent.py#L6873) | 6873 | `"                                source_indexes.setdefault(source_key, source_index)"` | — |
| [SRC-1AE03B9EC3-L006874](../../agents/web_agent.py#L6874) | 6874 | `"                        # A criterion-gap search is a second retrieval path, not a"` | — |
| [SRC-1AE03B9EC3-L006875](../../agents/web_agent.py#L6875) | 6875 | `"                        # trusted bypass. Apply the same task-specific source policy before"` | — |
| [SRC-1AE03B9EC3-L006876](../../agents/web_agent.py#L6876) | 6876 | `"                        # merging candidates into the evidence set or regenerating an answer."` | — |
| [SRC-1AE03B9EC3-L006877](../../agents/web_agent.py#L6877) | 6877 | `"                        pre_gap_source_keys = set(source_indexes)"` | — |
| [SRC-1AE03B9EC3-L006878](../../agents/web_agent.py#L6878) | 6878 | `"                        gap_sources_before_guardrails = len(gap_sources)"` | — |
| [SRC-1AE03B9EC3-L006879](../../agents/web_agent.py#L6879) | 6879 | `"                        gap_sources, gap_guardrail_report = apply_source_guardrails("` | — |
| [SRC-1AE03B9EC3-L006880](../../agents/web_agent.py#L6880) | 6880 | `"                            working_question, clean_mode, plan, gap_sources"` | — |
| [SRC-1AE03B9EC3-L006881](../../agents/web_agent.py#L6881) | 6881 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L006882](../../agents/web_agent.py#L6882) | 6882 | `"                        report.setdefault(\"source_guardrails\", {})["` | — |
| [SRC-1AE03B9EC3-L006883](../../agents/web_agent.py#L6883) | 6883 | `"                            \"criterion_gap_repair\""` | — |
| [SRC-1AE03B9EC3-L006884](../../agents/web_agent.py#L6884) | 6884 | `"                        ] = {"` | — |
| [SRC-1AE03B9EC3-L006885](../../agents/web_agent.py#L6885) | 6885 | `"                            **gap_guardrail_report,"` | — |
| [SRC-1AE03B9EC3-L006886](../../agents/web_agent.py#L6886) | 6886 | `"                            \"candidates_before_filter\": gap_sources_before_guardrails,"` | — |
| [SRC-1AE03B9EC3-L006887](../../agents/web_agent.py#L6887) | 6887 | `"                        }"` | — |
| [SRC-1AE03B9EC3-L006888](../../agents/web_agent.py#L6888) | 6888 | `"                        if gap_guardrail_report[\"rejected_sources\"]:"` | — |
| [SRC-1AE03B9EC3-L006889](../../agents/web_agent.py#L6889) | 6889 | `"                            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L006890](../../agents/web_agent.py#L6890) | 6890 | `"                                \"رُفضت بعض نتائج البحث الإضافي لأنها لم تستوفِ شروط قبول \""` | — |
| [SRC-1AE03B9EC3-L006891](../../agents/web_agent.py#L6891) | 6891 | `"                                \"الأدلة الخاصة بالسؤال.\""` | — |
| [SRC-1AE03B9EC3-L006892](../../agents/web_agent.py#L6892) | 6892 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L006893](../../agents/web_agent.py#L6893) | 6893 | `"                        evidence_updated = False"` | — |
| [SRC-1AE03B9EC3-L006894](../../agents/web_agent.py#L6894) | 6894 | `"                        for candidate in gap_sources:"` | — |
| [SRC-1AE03B9EC3-L006895](../../agents/web_agent.py#L6895) | 6895 | `"                            if not isinstance(candidate, dict):"` | — |
| [SRC-1AE03B9EC3-L006896](../../agents/web_agent.py#L6896) | 6896 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L006897](../../agents/web_agent.py#L6897) | 6897 | `"                            if not self._source_matches_query(gap_query, candidate):"` | — |
| [SRC-1AE03B9EC3-L006898](../../agents/web_agent.py#L6898) | 6898 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L006899](../../agents/web_agent.py#L6899) | 6899 | `"                            source_key = self._normalized_source_url_key(candidate.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L006900](../../agents/web_agent.py#L6900) | 6900 | `"                            if not source_key:"` | — |
| [SRC-1AE03B9EC3-L006901](../../agents/web_agent.py#L6901) | 6901 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L006902](../../agents/web_agent.py#L6902) | 6902 | `"                            existing_index = source_indexes.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L006903](../../agents/web_agent.py#L6903) | 6903 | `"                            if existing_index is None:"` | — |
| [SRC-1AE03B9EC3-L006904](../../agents/web_agent.py#L6904) | 6904 | `"                                source_indexes[source_key] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L006905](../../agents/web_agent.py#L6905) | 6905 | `"                                sources.append(candidate)"` | — |
| [SRC-1AE03B9EC3-L006906](../../agents/web_agent.py#L6906) | 6906 | `"                                criterion_gap_research[\"new_sources_added\"] += 1"` | — |
| [SRC-1AE03B9EC3-L006907](../../agents/web_agent.py#L6907) | 6907 | `"                                evidence_updated = True"` | — |
| [SRC-1AE03B9EC3-L006908](../../agents/web_agent.py#L6908) | 6908 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L006909](../../agents/web_agent.py#L6909) | 6909 | `"                            existing_source = sources[existing_index]"` | — |
| [SRC-1AE03B9EC3-L006910](../../agents/web_agent.py#L6910) | 6910 | `"                            merged = dict(existing_source)"` | — |
| [SRC-1AE03B9EC3-L006911](../../agents/web_agent.py#L6911) | 6911 | `"                            source_enriched = False"` | — |
| [SRC-1AE03B9EC3-L006912](../../agents/web_agent.py#L6912) | 6912 | `"                            for text_key in (\"title\", \"snippet\", \"page_text\"):"` | — |
| [SRC-1AE03B9EC3-L006913](../../agents/web_agent.py#L6913) | 6913 | `"                                old_text = str(merged.get(text_key) or \"\")"` | — |
| [SRC-1AE03B9EC3-L006914](../../agents/web_agent.py#L6914) | 6914 | `"                                new_text = str(candidate.get(text_key) or \"\")"` | — |
| [SRC-1AE03B9EC3-L006915](../../agents/web_agent.py#L6915) | 6915 | `"                                if len(new_text) > len(old_text):"` | — |
| [SRC-1AE03B9EC3-L006916](../../agents/web_agent.py#L6916) | 6916 | `"                                    merged[text_key] = candidate[text_key]"` | — |
| [SRC-1AE03B9EC3-L006917](../../agents/web_agent.py#L6917) | 6917 | `"                                    source_enriched = True"` | — |
| [SRC-1AE03B9EC3-L006918](../../agents/web_agent.py#L6918) | 6918 | `"                            if candidate.get(\"page_fetched\") and not existing_source.get(\"page_fetched\"):"` | — |
| [SRC-1AE03B9EC3-L006919](../../agents/web_agent.py#L6919) | 6919 | `"                                merged[\"page_fetched\"] = True"` | — |
| [SRC-1AE03B9EC3-L006920](../../agents/web_agent.py#L6920) | 6920 | `"                                source_enriched = True"` | — |
| [SRC-1AE03B9EC3-L006921](../../agents/web_agent.py#L6921) | 6921 | `"                            if source_enriched:"` | — |
| [SRC-1AE03B9EC3-L006922](../../agents/web_agent.py#L6922) | 6922 | `"                                evidence_updated = True"` | — |
| [SRC-1AE03B9EC3-L006923](../../agents/web_agent.py#L6923) | 6923 | `"                                criterion_gap_research[\"evidence_sources_enriched\"] += 1"` | — |
| [SRC-1AE03B9EC3-L006924](../../agents/web_agent.py#L6924) | 6924 | `"                            merged[\"providers\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L006925](../../agents/web_agent.py#L6925) | 6925 | `"                                list(existing_source.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L006926](../../agents/web_agent.py#L6926) | 6926 | `"                                + list(candidate.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L006927](../../agents/web_agent.py#L6927) | 6927 | `"                            ))"` | — |
| [SRC-1AE03B9EC3-L006928](../../agents/web_agent.py#L6928) | 6928 | `"                            merged[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L006929](../../agents/web_agent.py#L6929) | 6929 | `"                                list(existing_source.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L006930](../../agents/web_agent.py#L6930) | 6930 | `"                                + list(candidate.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L006931](../../agents/web_agent.py#L6931) | 6931 | `"                                + [gap_query]"` | — |
| [SRC-1AE03B9EC3-L006932](../../agents/web_agent.py#L6932) | 6932 | `"                            ))"` | — |
| [SRC-1AE03B9EC3-L006933](../../agents/web_agent.py#L6933) | 6933 | `"                            sources[existing_index] = merged"` | — |
| [SRC-1AE03B9EC3-L006934](../../agents/web_agent.py#L6934) | 6934 | `"                        # Re-apply the guardrails to the merged set as a final safety"` | — |
| [SRC-1AE03B9EC3-L006935](../../agents/web_agent.py#L6935) | 6935 | `"                        # boundary. Count newly added sources only after this filter."` | — |
| [SRC-1AE03B9EC3-L006936](../../agents/web_agent.py#L6936) | 6936 | `"                        sources, merged_guardrail_report = apply_source_guardrails("` | — |
| [SRC-1AE03B9EC3-L006937](../../agents/web_agent.py#L6937) | 6937 | `"                            working_question, clean_mode, plan, sources"` | — |
| [SRC-1AE03B9EC3-L006938](../../agents/web_agent.py#L6938) | 6938 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L006939](../../agents/web_agent.py#L6939) | 6939 | `"                        report[\"source_guardrails\"][\"after_criterion_gap_repair\"] = ("` | — |
| [SRC-1AE03B9EC3-L006940](../../agents/web_agent.py#L6940) | 6940 | `"                            merged_guardrail_report"` | — |
| [SRC-1AE03B9EC3-L006941](../../agents/web_agent.py#L6941) | 6941 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L006942](../../agents/web_agent.py#L6942) | 6942 | `"                        accepted_source_keys = {"` | — |
| [SRC-1AE03B9EC3-L006943](../../agents/web_agent.py#L6943) | 6943 | `"                            self._normalized_source_url_key(item.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L006944](../../agents/web_agent.py#L6944) | 6944 | `"                            for item in sources"` | — |
| [SRC-1AE03B9EC3-L006945](../../agents/web_agent.py#L6945) | 6945 | `"                            if self._normalized_source_url_key(item.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L006946](../../agents/web_agent.py#L6946) | 6946 | `"                        }"` | — |
| [SRC-1AE03B9EC3-L006947](../../agents/web_agent.py#L6947) | 6947 | `"                        criterion_gap_research[\"new_sources_added\"] = len("` | — |
| [SRC-1AE03B9EC3-L006948](../../agents/web_agent.py#L6948) | 6948 | `"                            accepted_source_keys - pre_gap_source_keys"` | — |
| [SRC-1AE03B9EC3-L006949](../../agents/web_agent.py#L6949) | 6949 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L006950](../../agents/web_agent.py#L6950) | 6950 | `"                        criterion_gap_research[\"source_count_after\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L006951](../../agents/web_agent.py#L6951) | 6951 | `"                        plan[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L006952](../../agents/web_agent.py#L6952) | 6952 | `"                            list(plan.get(\"queries\", [])) + [gap_query]"` | — |
| [SRC-1AE03B9EC3-L006953](../../agents/web_agent.py#L6953) | 6953 | `"                        ))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L006954](../../agents/web_agent.py#L6954) | 6954 | `"                        report[\"criterion_gap_research\"] = dict(criterion_gap_research)"` | — |
| [SRC-1AE03B9EC3-L006955](../../agents/web_agent.py#L6955) | 6955 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L006956](../../agents/web_agent.py#L6956) | 6956 | `"                            report[\"queries_planned\"] = max("` | — |
| [SRC-1AE03B9EC3-L006957](../../agents/web_agent.py#L6957) | 6957 | `"                                0, int(report.get(\"queries_planned\", 0) or 0)"` | — |
| [SRC-1AE03B9EC3-L006958](../../agents/web_agent.py#L6958) | 6958 | `"                            ) + max(0, int(gap_report.get(\"queries_planned\", 1) or 0))"` | — |
| [SRC-1AE03B9EC3-L006959](../../agents/web_agent.py#L6959) | 6959 | `"                        except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-1AE03B9EC3-L006960](../../agents/web_agent.py#L6960) | 6960 | `"                            report[\"queries_planned\"] = None"` | — |
| [SRC-1AE03B9EC3-L006961](../../agents/web_agent.py#L6961) | 6961 | `"                        previous_attempts = report.get(\"queries_attempted\")"` | — |
| [SRC-1AE03B9EC3-L006962](../../agents/web_agent.py#L6962) | 6962 | `"                        extra_attempts = gap_report.get(\"queries_attempted\")"` | — |
| [SRC-1AE03B9EC3-L006963](../../agents/web_agent.py#L6963) | 6963 | `"                        if isinstance(previous_attempts, int) and isinstance(extra_attempts, int):"` | — |
| [SRC-1AE03B9EC3-L006964](../../agents/web_agent.py#L6964) | 6964 | `"                            report[\"queries_attempted\"] = max(0, previous_attempts) + max(0, extra_attempts)"` | — |
| [SRC-1AE03B9EC3-L006965](../../agents/web_agent.py#L6965) | 6965 | `"                            report[\"queries_attempted_known\"] = True"` | — |
| [SRC-1AE03B9EC3-L006966](../../agents/web_agent.py#L6966) | 6966 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L006967](../../agents/web_agent.py#L6967) | 6967 | `"                            report[\"queries_attempted\"] = None"` | — |
| [SRC-1AE03B9EC3-L006968](../../agents/web_agent.py#L6968) | 6968 | `"                            report[\"queries_attempted_known\"] = False"` | — |
| [SRC-1AE03B9EC3-L006969](../../agents/web_agent.py#L6969) | 6969 | `"                        old_query_results = report.get(\"query_results\")"` | — |
| [SRC-1AE03B9EC3-L006970](../../agents/web_agent.py#L6970) | 6970 | `"                        new_query_results = gap_report.get(\"query_results\")"` | — |
| [SRC-1AE03B9EC3-L006971](../../agents/web_agent.py#L6971) | 6971 | `"                        report[\"query_results\"] = ("` | — |
| [SRC-1AE03B9EC3-L006972](../../agents/web_agent.py#L6972) | 6972 | `"                            (old_query_results if isinstance(old_query_results, list) else [])"` | — |
| [SRC-1AE03B9EC3-L006973](../../agents/web_agent.py#L6973) | 6973 | `"                            + (new_query_results if isinstance(new_query_results, list) else [])"` | — |
| [SRC-1AE03B9EC3-L006974](../../agents/web_agent.py#L6974) | 6974 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L006975](../../agents/web_agent.py#L6975) | 6975 | `"                        if evidence_updated:"` | — |
| [SRC-1AE03B9EC3-L006976](../../agents/web_agent.py#L6976) | 6976 | `"                            sources.sort("` | — |
| [SRC-1AE03B9EC3-L006977](../../agents/web_agent.py#L6977) | 6977 | `"                                key=lambda item: float(item.get(\"rank_score\", 0) or 0),"` | — |
| [SRC-1AE03B9EC3-L006978](../../agents/web_agent.py#L6978) | 6978 | `"                                reverse=True,"` | — |
| [SRC-1AE03B9EC3-L006979](../../agents/web_agent.py#L6979) | 6979 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L006980](../../agents/web_agent.py#L6980) | 6980 | `"                            try:"` | — |
| [SRC-1AE03B9EC3-L006981](../../agents/web_agent.py#L6981) | 6981 | `"                                revised_draft = self._generate("` | — |
| [SRC-1AE03B9EC3-L006982](../../agents/web_agent.py#L6982) | 6982 | `"                                    working_question,"` | — |
| [SRC-1AE03B9EC3-L006983](../../agents/web_agent.py#L6983) | 6983 | `"                                    clean_history,"` | — |
| [SRC-1AE03B9EC3-L006984](../../agents/web_agent.py#L6984) | 6984 | `"                                    sources,"` | — |
| [SRC-1AE03B9EC3-L006985](../../agents/web_agent.py#L6985) | 6985 | `"                                    search_warning,"` | — |
| [SRC-1AE03B9EC3-L006986](../../agents/web_agent.py#L6986) | 6986 | `"                                    research_plan=plan,"` | — |
| [SRC-1AE03B9EC3-L006987](../../agents/web_agent.py#L6987) | 6987 | `"                                    search_report=report,"` | — |
| [SRC-1AE03B9EC3-L006988](../../agents/web_agent.py#L6988) | 6988 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L006989](../../agents/web_agent.py#L6989) | 6989 | `"                                revised_answer = self._review_answer("` | — |
| [SRC-1AE03B9EC3-L006990](../../agents/web_agent.py#L6990) | 6990 | `"                                    working_question, revised_draft, sources[:MAX_LLM_CITED_SOURCES]"` | — |
| [SRC-1AE03B9EC3-L006991](../../agents/web_agent.py#L6991) | 6991 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L006992](../../agents/web_agent.py#L6992) | 6992 | `"                                answer = revised_answer"` | — |
| [SRC-1AE03B9EC3-L006993](../../agents/web_agent.py#L6993) | 6993 | `"                                review_status = \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006994](../../agents/web_agent.py#L6994) | 6994 | `"                                criterion_gap_research[\"status\"] = \"evidence_added_and_answer_regenerated\""` | — |
| [SRC-1AE03B9EC3-L006995](../../agents/web_agent.py#L6995) | 6995 | `"                            except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L006996](../../agents/web_agent.py#L6996) | 6996 | `"                                criterion_gap_research[\"status\"] = \"evidence_added_but_regeneration_unavailable\""` | — |
| [SRC-1AE03B9EC3-L006997](../../agents/web_agent.py#L6997) | 6997 | `"                                criterion_gap_research[\"regeneration_error_class\"] = type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L006998](../../agents/web_agent.py#L6998) | 6998 | `"                                coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L006999](../../agents/web_agent.py#L6999) | 6999 | `"                                    \"وصلت أدلة إضافية لمحور مطلوب، لكن تعذرت إعادة توليد الإجابة \""` | — |
| [SRC-1AE03B9EC3-L007000](../../agents/web_agent.py#L7000) | 7000 | `"                                    \"وتدقيقها ضمن الميزانية؛ راجع هذا المحور قبل اعتماد الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L007001](../../agents/web_agent.py#L7001) | 7001 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L007002](../../agents/web_agent.py#L7002) | 7002 | `"                        elif criterion_gap_research.get(\"status\") != \"search_failed\":"` | — |
| [SRC-1AE03B9EC3-L007003](../../agents/web_agent.py#L7003) | 7003 | `"                            criterion_gap_research[\"status\"] = \"search_completed_no_new_criterion_evidence\""` | — |
| [SRC-1AE03B9EC3-L007004](../../agents/web_agent.py#L7004) | 7004 | `"                            coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L007005](../../agents/web_agent.py#L7005) | 7005 | `"                                \"أُجري بحث إضافي لمحاور ناقصة، لكنه لم يضف نص مصدر يمكن تمييزه \""` | — |
| [SRC-1AE03B9EC3-L007006](../../agents/web_agent.py#L7006) | 7006 | `"                                \"كدليل جديد؛ ستظل هذه المحاور غير محسومة.\""` | — |
| [SRC-1AE03B9EC3-L007007](../../agents/web_agent.py#L7007) | 7007 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L007008](../../agents/web_agent.py#L7008) | 7008 | `"                        criterion_gap_research[\"source_count_after\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L007009](../../agents/web_agent.py#L7009) | 7009 | `"                        report[\"criterion_gap_research\"] = dict(criterion_gap_research)"` | — |
| [SRC-1AE03B9EC3-L007010](../../agents/web_agent.py#L7010) | 7010 | `""` | — |
| [SRC-1AE03B9EC3-L007011](../../agents/web_agent.py#L7011) | 7011 | `"        report[\"criterion_gap_research\"] = dict(criterion_gap_research)"` | — |
| [SRC-1AE03B9EC3-L007012](../../agents/web_agent.py#L7012) | 7012 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L007013](../../agents/web_agent.py#L7013) | 7013 | `"            coverage_targets"` | — |
| [SRC-1AE03B9EC3-L007014](../../agents/web_agent.py#L7014) | 7014 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L007015](../../agents/web_agent.py#L7015) | 7015 | `"            and sources"` | — |
| [SRC-1AE03B9EC3-L007016](../../agents/web_agent.py#L7016) | 7016 | `"            and self.api_key"` | — |
| [SRC-1AE03B9EC3-L007017](../../agents/web_agent.py#L7017) | 7017 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L007018](../../agents/web_agent.py#L7018) | 7018 | `"            initial_integrity = audit_answer_integrity(working_question, answer, sources, coverage_targets, plan.get(\"requirement_queries\"))"` | — |
| [SRC-1AE03B9EC3-L007019](../../agents/web_agent.py#L7019) | 7019 | `"            missing_targets = ["` | — |
| [SRC-1AE03B9EC3-L007020](../../agents/web_agent.py#L7020) | 7020 | `"                item[\"target\"] for item in initial_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L007021](../../agents/web_agent.py#L7021) | 7021 | `"                if item[\"status\"] == \"possibly_missing\""` | — |
| [SRC-1AE03B9EC3-L007022](../../agents/web_agent.py#L7022) | 7022 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L007023](../../agents/web_agent.py#L7023) | 7023 | `"            remaining_source_gap_targets = ["` | — |
| [SRC-1AE03B9EC3-L007024](../../agents/web_agent.py#L7024) | 7024 | `"                item[\"target\"] for item in initial_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L007025](../../agents/web_agent.py#L7025) | 7025 | `"                if item.get(\"source_evidence_status\") == \"no_source_lexical_signal\""` | — |
| [SRC-1AE03B9EC3-L007026](../../agents/web_agent.py#L7026) | 7026 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L007027](../../agents/web_agent.py#L7027) | 7027 | `"            if not missing_targets and remaining_source_gap_targets:"` | — |
| [SRC-1AE03B9EC3-L007028](../../agents/web_agent.py#L7028) | 7028 | `"                coverage_repair_status = \"source_evidence_gap_unresolved\""` | — |
| [SRC-1AE03B9EC3-L007029](../../agents/web_agent.py#L7029) | 7029 | `"                if not coverage_repair_warning:"` | — |
| [SRC-1AE03B9EC3-L007030](../../agents/web_agent.py#L7030) | 7030 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L007031](../../agents/web_agent.py#L7031) | 7031 | `"                        \"ذُكرت المحاور في الإجابة، لكن لم تظهر لها إشارات لفظية في المصادر؛ \""` | — |
| [SRC-1AE03B9EC3-L007032](../../agents/web_agent.py#L7032) | 7032 | `"                        \"ذكر المحور لا يُعد دليلًا، لذلك تظل المهمة غير مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L007033](../../agents/web_agent.py#L7033) | 7033 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L007034](../../agents/web_agent.py#L7034) | 7034 | `"            elif not missing_targets:"` | — |
| [SRC-1AE03B9EC3-L007035](../../agents/web_agent.py#L7035) | 7035 | `"                coverage_repair_status = \"not_needed_lexical_signals_found\""` | — |
| [SRC-1AE03B9EC3-L007036](../../agents/web_agent.py#L7036) | 7036 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L007037](../../agents/web_agent.py#L7037) | 7037 | `"                coverage_repair_status = \"attempted\""` | — |
| [SRC-1AE03B9EC3-L007038](../../agents/web_agent.py#L7038) | 7038 | `"                try:"` | — |
| [SRC-1AE03B9EC3-L007039](../../agents/web_agent.py#L7039) | 7039 | `"                    repaired_answer = self._repair_answer_coverage("` | — |
| [SRC-1AE03B9EC3-L007040](../../agents/web_agent.py#L7040) | 7040 | `"                        working_question, answer, sources, missing_targets"` | — |
| [SRC-1AE03B9EC3-L007041](../../agents/web_agent.py#L7041) | 7041 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L007042](../../agents/web_agent.py#L7042) | 7042 | `"                    if repaired_answer.strip() != answer.strip():"` | — |
| [SRC-1AE03B9EC3-L007043](../../agents/web_agent.py#L7043) | 7043 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L007044](../../agents/web_agent.py#L7044) | 7044 | `"                            reaudit_answer = self._review_answer("` | — |
| [SRC-1AE03B9EC3-L007045](../../agents/web_agent.py#L7045) | 7045 | `"                                working_question,"` | — |
| [SRC-1AE03B9EC3-L007046](../../agents/web_agent.py#L7046) | 7046 | `"                                repaired_answer,"` | — |
| [SRC-1AE03B9EC3-L007047](../../agents/web_agent.py#L7047) | 7047 | `"                                sources[:MAX_LLM_CITED_SOURCES],"` | — |
| [SRC-1AE03B9EC3-L007048](../../agents/web_agent.py#L7048) | 7048 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L007049](../../agents/web_agent.py#L7049) | 7049 | `"                            answer = reaudit_answer"` | — |
| [SRC-1AE03B9EC3-L007050](../../agents/web_agent.py#L7050) | 7050 | `"                            reaudit_integrity = audit_answer_integrity("` | — |
| [SRC-1AE03B9EC3-L007051](../../agents/web_agent.py#L7051) | 7051 | `"                                question, answer, sources, coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L007052](../../agents/web_agent.py#L7052) | 7052 | `"                                plan.get(\"requirement_queries\"),"` | — |
| [SRC-1AE03B9EC3-L007053](../../agents/web_agent.py#L7053) | 7053 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L007054](../../agents/web_agent.py#L7054) | 7054 | `"                            if reaudit_integrity[\"potentially_missing_target_count\"] > 0:"` | — |
| [SRC-1AE03B9EC3-L007055](../../agents/web_agent.py#L7055) | 7055 | `"                                coverage_repair_status = \"revised_and_reaudited_remaining_gaps\""` | — |
| [SRC-1AE03B9EC3-L007056](../../agents/web_agent.py#L7056) | 7056 | `"                                coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L007057](../../agents/web_agent.py#L7057) | 7057 | `"                                    \"خضعت الإجابة المعدلة لمراجعة ثانية، لكن الفحص اللفظي ما زال يرصد محورًا محتمل النقص؛ \""` | — |
| [SRC-1AE03B9EC3-L007058](../../agents/web_agent.py#L7058) | 7058 | `"                                    \"لا تعتبر المهمة مكتملة دون مراجعة هذا المحور والأدلة الأصلية.\""` | — |
| [SRC-1AE03B9EC3-L007059](../../agents/web_agent.py#L7059) | 7059 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L007060](../../agents/web_agent.py#L7060) | 7060 | `"                            else:"` | — |
| [SRC-1AE03B9EC3-L007061](../../agents/web_agent.py#L7061) | 7061 | `"                                coverage_repair_status = \"revised_and_reaudited\""` | — |
| [SRC-1AE03B9EC3-L007062](../../agents/web_agent.py#L7062) | 7062 | `"                            review_status = \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L007063](../../agents/web_agent.py#L7063) | 7063 | `"                        except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L007064](../../agents/web_agent.py#L7064) | 7064 | `"                            review_status = \"model_claim_audit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L007065](../../agents/web_agent.py#L7065) | 7065 | `"                            review_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L007066](../../agents/web_agent.py#L7066) | 7066 | `"                            coverage_repair_status = ("` | — |
| [SRC-1AE03B9EC3-L007067](../../agents/web_agent.py#L7067) | 7067 | `"                                \"reaudit_budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L007068](../../agents/web_agent.py#L7068) | 7068 | `"                                if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L007069](../../agents/web_agent.py#L7069) | 7069 | `"                                else \"reaudit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L007070](../../agents/web_agent.py#L7070) | 7070 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L007071](../../agents/web_agent.py#L7071) | 7071 | `"                            review_warning = ("` | — |
| [SRC-1AE03B9EC3-L007072](../../agents/web_agent.py#L7072) | 7072 | `"                                \"استُنفدت ميزانية النماذج قبل إعادة تدقيق الإجابة المعدلة؛ \""` | — |
| [SRC-1AE03B9EC3-L007073](../../agents/web_agent.py#L7073) | 7073 | `"                                \"لذلك لن أعرض النص المعدل بوصفه إجابة مكتملة، وأعرض مقتطفات المصادر بدلًا منه.\""` | — |
| [SRC-1AE03B9EC3-L007074](../../agents/web_agent.py#L7074) | 7074 | `"                                if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L007075](../../agents/web_agent.py#L7075) | 7075 | `"                                else"` | — |
| [SRC-1AE03B9EC3-L007076](../../agents/web_agent.py#L7076) | 7076 | `"                                \"تعذرت إعادة تدقيق الإجابة المعدلة مقابل الأدلة؛ لذلك لن أعرضها بوصفها إجابة مكتملة، \""` | — |
| [SRC-1AE03B9EC3-L007077](../../agents/web_agent.py#L7077) | 7077 | `"                                \"وأعرض مقتطفات المصادر بدلًا منها.\""` | — |
| [SRC-1AE03B9EC3-L007078](../../agents/web_agent.py#L7078) | 7078 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L007079](../../agents/web_agent.py#L7079) | 7079 | `"                            answer = ("` | — |
| [SRC-1AE03B9EC3-L007080](../../agents/web_agent.py#L7080) | 7080 | `"                                _fallback_lead_answer(lead_evidence_sources)"` | — |
| [SRC-1AE03B9EC3-L007081](../../agents/web_agent.py#L7081) | 7081 | `"                                if lead_request and lead_evidence_sources"` | — |
| [SRC-1AE03B9EC3-L007082](../../agents/web_agent.py#L7082) | 7082 | `"                                else _fallback_answer(sources, review_warning)"` | — |
| [SRC-1AE03B9EC3-L007083](../../agents/web_agent.py#L7083) | 7083 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L007084](../../agents/web_agent.py#L7084) | 7084 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L007085](../../agents/web_agent.py#L7085) | 7085 | `"                        coverage_repair_status = \"no_change_gap_unresolved\""` | — |
| [SRC-1AE03B9EC3-L007086](../../agents/web_agent.py#L7086) | 7086 | `"                        coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L007087](../../agents/web_agent.py#L7087) | 7087 | `"                            \"رصد الفحص اللفظي محورًا قد يكون ناقصًا، لكن محاولة الإصلاح لم تغيّر الإجابة؛ \""` | — |
| [SRC-1AE03B9EC3-L007088](../../agents/web_agent.py#L7088) | 7088 | `"                            \"تحقق من تغطية هذا المحور يدويًا.\""` | — |
| [SRC-1AE03B9EC3-L007089](../../agents/web_agent.py#L7089) | 7089 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L007090](../../agents/web_agent.py#L7090) | 7090 | `"                except RequestBudgetExceeded:"` | — |
| [SRC-1AE03B9EC3-L007091](../../agents/web_agent.py#L7091) | 7091 | `"                    coverage_repair_status = \"budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L007092](../../agents/web_agent.py#L7092) | 7092 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L007093](../../agents/web_agent.py#L7093) | 7093 | `"                        \"استُنفدت ميزانية النماذج قبل محاولة إصلاح محور قد يكون ناقصًا؛ \""` | — |
| [SRC-1AE03B9EC3-L007094](../../agents/web_agent.py#L7094) | 7094 | `"                        \"لا تعتبر التغطية مكتملة دون مراجعة المحور المذكور.\""` | — |
| [SRC-1AE03B9EC3-L007095](../../agents/web_agent.py#L7095) | 7095 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L007096](../../agents/web_agent.py#L7096) | 7096 | `"                except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L007097](../../agents/web_agent.py#L7097) | 7097 | `"                    coverage_repair_status = \"unavailable\""` | — |
| [SRC-1AE03B9EC3-L007098](../../agents/web_agent.py#L7098) | 7098 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L007099](../../agents/web_agent.py#L7099) | 7099 | `"                        \"تعذرت محاولة إصلاح محور قد يكون ناقصًا (\""` | — |
| [SRC-1AE03B9EC3-L007100](../../agents/web_agent.py#L7100) | 7100 | `"                        + type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L007101](../../agents/web_agent.py#L7101) | 7101 | `"                        + \")؛ راجع المحاور المطلوبة قبل اعتماد الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L007102](../../agents/web_agent.py#L7102) | 7102 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L007103](../../agents/web_agent.py#L7103) | 7103 | `"        elif coverage_targets and review_status == \"model_claim_audit_completed\" and not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L007104](../../agents/web_agent.py#L7104) | 7104 | `"            coverage_repair_status = \"skipped_no_model_configuration\""` | — |
| [SRC-1AE03B9EC3-L007105](../../agents/web_agent.py#L7105) | 7105 | `"        elif coverage_targets:"` | — |
| [SRC-1AE03B9EC3-L007106](../../agents/web_agent.py#L7106) | 7106 | `"            coverage_repair_status = \"skipped_review_unavailable\""` | — |
| [SRC-1AE03B9EC3-L007107](../../agents/web_agent.py#L7107) | 7107 | `""` | — |
| [SRC-1AE03B9EC3-L007108](../../agents/web_agent.py#L7108) | 7108 | `"        if self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L007109](../../agents/web_agent.py#L7109) | 7109 | `"            answer += \"\\n\\nروابط إضافية من البحث المباشر عبر الويب:\""` | — |
| [SRC-1AE03B9EC3-L007110](../../agents/web_agent.py#L7110) | 7110 | `"            for source in self.server_search_sources[:8]:"` | — |
| [SRC-1AE03B9EC3-L007111](../../agents/web_agent.py#L7111) | 7111 | `"                answer += \"\\n- \" + source[\"title\"] + \" — \" + source[\"url\"]"` | — |
| [SRC-1AE03B9EC3-L007112](../../agents/web_agent.py#L7112) | 7112 | `"        max_citable_sources = min(MAX_LLM_CITED_SOURCES, len(sources))"` | — |
| [SRC-1AE03B9EC3-L007113](../../agents/web_agent.py#L7113) | 7113 | `"        answer, citation_warnings = self._remove_invalid_citations("` | — |
| [SRC-1AE03B9EC3-L007114](../../agents/web_agent.py#L7114) | 7114 | `"            answer, max_citable_sources"` | — |
| [SRC-1AE03B9EC3-L007115](../../agents/web_agent.py#L7115) | 7115 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007116](../../agents/web_agent.py#L7116) | 7116 | `"        citation_validation = self._citation_validation_metadata("` | — |
| [SRC-1AE03B9EC3-L007117](../../agents/web_agent.py#L7117) | 7117 | `"            answer, max_citable_sources, citation_warnings, review_status"` | — |
| [SRC-1AE03B9EC3-L007118](../../agents/web_agent.py#L7118) | 7118 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007119](../../agents/web_agent.py#L7119) | 7119 | `"        # Run deterministic numeric/provenance checks before asking the semantic reviewer."` | — |
| [SRC-1AE03B9EC3-L007120](../../agents/web_agent.py#L7120) | 7120 | `"        # Recompute below after a source-only fallback so public diagnostics describe the final text."` | — |
| [SRC-1AE03B9EC3-L007121](../../agents/web_agent.py#L7121) | 7121 | `"        answer_integrity = audit_answer_integrity("` | — |
| [SRC-1AE03B9EC3-L007122](../../agents/web_agent.py#L7122) | 7122 | `"            working_question, answer, sources, coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L007123](../../agents/web_agent.py#L7123) | 7123 | `"            plan.get(\"requirement_queries\")"` | — |
| [SRC-1AE03B9EC3-L007124](../../agents/web_agent.py#L7124) | 7124 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007125](../../agents/web_agent.py#L7125) | 7125 | `"        semantic_claim_verification: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L007126](../../agents/web_agent.py#L7126) | 7126 | `"            \"status\": \"not_run_review_unavailable\","` | — |
| [SRC-1AE03B9EC3-L007127](../../agents/web_agent.py#L7127) | 7127 | `"            \"withhold_answer\": False,"` | — |
| [SRC-1AE03B9EC3-L007128](../../agents/web_agent.py#L7128) | 7128 | `"            \"semantic_verification\": \"not_performed\","` | — |
| [SRC-1AE03B9EC3-L007129](../../agents/web_agent.py#L7129) | 7129 | `"            \"fact_correctness\": \"not_verified\","` | — |
| [SRC-1AE03B9EC3-L007130](../../agents/web_agent.py#L7130) | 7130 | `"        }"` | — |
| [SRC-1AE03B9EC3-L007131](../../agents/web_agent.py#L7131) | 7131 | `"        semantic_answer_withheld = False"` | — |
| [SRC-1AE03B9EC3-L007132](../../agents/web_agent.py#L7132) | 7132 | `"        if used_llm and sources and review_status == \"model_claim_audit_completed\":"` | — |
| [SRC-1AE03B9EC3-L007133](../../agents/web_agent.py#L7133) | 7133 | `"            if citation_warnings:"` | — |
| [SRC-1AE03B9EC3-L007134](../../agents/web_agent.py#L7134) | 7134 | `"                semantic_claim_verification = {"` | — |
| [SRC-1AE03B9EC3-L007135](../../agents/web_agent.py#L7135) | 7135 | `"                    \"status\": \"not_verifiable\","` | — |
| [SRC-1AE03B9EC3-L007136](../../agents/web_agent.py#L7136) | 7136 | `"                    \"withhold_answer\": True,"` | — |
| [SRC-1AE03B9EC3-L007137](../../agents/web_agent.py#L7137) | 7137 | `"                    \"reason\": \"invalid_citation_references_were_removed\","` | — |
| [SRC-1AE03B9EC3-L007138](../../agents/web_agent.py#L7138) | 7138 | `"                    \"semantic_verification\": \"not_completed\","` | — |
| [SRC-1AE03B9EC3-L007139](../../agents/web_agent.py#L7139) | 7139 | `"                    \"fact_correctness\": \"not_verified\","` | — |
| [SRC-1AE03B9EC3-L007140](../../agents/web_agent.py#L7140) | 7140 | `"                }"` | — |
| [SRC-1AE03B9EC3-L007141](../../agents/web_agent.py#L7141) | 7141 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L007142](../../agents/web_agent.py#L7142) | 7142 | `"                semantic_claim_verification = self._verify_semantic_claims("` | — |
| [SRC-1AE03B9EC3-L007143](../../agents/web_agent.py#L7143) | 7143 | `"                    working_question, answer, sources, answer_integrity"` | — |
| [SRC-1AE03B9EC3-L007144](../../agents/web_agent.py#L7144) | 7144 | `"                )"` | — |
| [SRC-1AE03B9EC3-L007145](../../agents/web_agent.py#L7145) | 7145 | `"            if semantic_claim_verification.get(\"status\") not in {"` | — |
| [SRC-1AE03B9EC3-L007146](../../agents/web_agent.py#L7146) | 7146 | `"                \"completed_all_claims_supported\","` | — |
| [SRC-1AE03B9EC3-L007147](../../agents/web_agent.py#L7147) | 7147 | `"                \"completed_no_factual_claims\","` | — |
| [SRC-1AE03B9EC3-L007148](../../agents/web_agent.py#L7148) | 7148 | `"            }:"` | — |
| [SRC-1AE03B9EC3-L007149](../../agents/web_agent.py#L7149) | 7149 | `"                semantic_answer_withheld = True"` | — |
| [SRC-1AE03B9EC3-L007150](../../agents/web_agent.py#L7150) | 7150 | `"                semantic_warning = ("` | — |
| [SRC-1AE03B9EC3-L007151](../../agents/web_agent.py#L7151) | 7151 | `"                    \"حُجبت صياغة النموذج لأن مراجع دعم الادعاءات لم يستطع إثبات دعم \""` | — |
| [SRC-1AE03B9EC3-L007152](../../agents/web_agent.py#L7152) | 7152 | `"                    \"كل ادعاء واقعي بمصدره المحدد دون تعارض. المقتطفات أدناه مواد مصدرية \""` | — |
| [SRC-1AE03B9EC3-L007153](../../agents/web_agent.py#L7153) | 7153 | `"                    \"للمراجعة وليست إجابة متحققة.\""` | — |
| [SRC-1AE03B9EC3-L007154](../../agents/web_agent.py#L7154) | 7154 | `"                )"` | — |
| [SRC-1AE03B9EC3-L007155](../../agents/web_agent.py#L7155) | 7155 | `"                answer = ("` | — |
| [SRC-1AE03B9EC3-L007156](../../agents/web_agent.py#L7156) | 7156 | `"                    _fallback_lead_answer(lead_evidence_sources)"` | — |
| [SRC-1AE03B9EC3-L007157](../../agents/web_agent.py#L7157) | 7157 | `"                    if lead_request and lead_evidence_sources"` | — |
| [SRC-1AE03B9EC3-L007158](../../agents/web_agent.py#L7158) | 7158 | `"                    else _fallback_answer(sources, semantic_warning)"` | — |
| [SRC-1AE03B9EC3-L007159](../../agents/web_agent.py#L7159) | 7159 | `"                )"` | — |
| [SRC-1AE03B9EC3-L007160](../../agents/web_agent.py#L7160) | 7160 | `"                answer, fallback_citation_warnings = self._remove_invalid_citations("` | — |
| [SRC-1AE03B9EC3-L007161](../../agents/web_agent.py#L7161) | 7161 | `"                    answer, max_citable_sources"` | — |
| [SRC-1AE03B9EC3-L007162](../../agents/web_agent.py#L7162) | 7162 | `"                )"` | — |
| [SRC-1AE03B9EC3-L007163](../../agents/web_agent.py#L7163) | 7163 | `"                citation_warnings = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L007164](../../agents/web_agent.py#L7164) | 7164 | `"                    citation_warnings + fallback_citation_warnings"` | — |
| [SRC-1AE03B9EC3-L007165](../../agents/web_agent.py#L7165) | 7165 | `"                ))"` | — |
| [SRC-1AE03B9EC3-L007166](../../agents/web_agent.py#L7166) | 7166 | `"                citation_validation = self._citation_validation_metadata("` | — |
| [SRC-1AE03B9EC3-L007167](../../agents/web_agent.py#L7167) | 7167 | `"                    answer, max_citable_sources, citation_warnings, review_status"` | — |
| [SRC-1AE03B9EC3-L007168](../../agents/web_agent.py#L7168) | 7168 | `"                )"` | — |
| [SRC-1AE03B9EC3-L007169](../../agents/web_agent.py#L7169) | 7169 | `"        report[\"semantic_claim_verification\"] = semantic_claim_verification"` | — |
| [SRC-1AE03B9EC3-L007170](../../agents/web_agent.py#L7170) | 7170 | `"        report[\"answer_was_withheld\"] = semantic_answer_withheld"` | — |
| [SRC-1AE03B9EC3-L007171](../../agents/web_agent.py#L7171) | 7171 | `"        report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L007172](../../agents/web_agent.py#L7172) | 7172 | `"        report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L007173](../../agents/web_agent.py#L7173) | 7173 | `"        report[\"second_pass_review\"] = review_status"` | — |
| [SRC-1AE03B9EC3-L007174](../../agents/web_agent.py#L7174) | 7174 | `"        report[\"claim_audit\"] = review_status"` | — |
| [SRC-1AE03B9EC3-L007175](../../agents/web_agent.py#L7175) | 7175 | `"        answer_coverage = {"` | — |
| [SRC-1AE03B9EC3-L007176](../../agents/web_agent.py#L7176) | 7176 | `"            \"method\": \"explicit_criteria_heuristic\","` | — |
| [SRC-1AE03B9EC3-L007177](../../agents/web_agent.py#L7177) | 7177 | `"            \"targets\": coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L007178](../../agents/web_agent.py#L7178) | 7178 | `"            \"review_prompted\": review_status == \"model_claim_audit_completed\","` | — |
| [SRC-1AE03B9EC3-L007179](../../agents/web_agent.py#L7179) | 7179 | `"            \"status\": ("` | — |
| [SRC-1AE03B9EC3-L007180](../../agents/web_agent.py#L7180) | 7180 | `"                \"model_review_requested_not_machine_verified\""` | — |
| [SRC-1AE03B9EC3-L007181](../../agents/web_agent.py#L7181) | 7181 | `"                if coverage_targets and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L007182](../../agents/web_agent.py#L7182) | 7182 | `"                else \"review_unavailable\""` | — |
| [SRC-1AE03B9EC3-L007183](../../agents/web_agent.py#L7183) | 7183 | `"                if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L007184](../../agents/web_agent.py#L7184) | 7184 | `"                else \"no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L007185](../../agents/web_agent.py#L7185) | 7185 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L007186](../../agents/web_agent.py#L7186) | 7186 | `"            \"automatically_graded\": False,"` | — |
| [SRC-1AE03B9EC3-L007187](../../agents/web_agent.py#L7187) | 7187 | `"        }"` | — |
| [SRC-1AE03B9EC3-L007188](../../agents/web_agent.py#L7188) | 7188 | `"        report[\"answer_coverage\"] = answer_coverage"` | — |
| [SRC-1AE03B9EC3-L007189](../../agents/web_agent.py#L7189) | 7189 | `"        report[\"coverage_repair_status\"] = coverage_repair_status"` | — |
| [SRC-1AE03B9EC3-L007190](../../agents/web_agent.py#L7190) | 7190 | `"        report[\"coverage_repair_warning\"] = coverage_repair_warning"` | — |
| [SRC-1AE03B9EC3-L007191](../../agents/web_agent.py#L7191) | 7191 | `"        answer_integrity = audit_answer_integrity(working_question, answer, sources, coverage_targets, plan.get(\"requirement_queries\"))"` | — |
| [SRC-1AE03B9EC3-L007192](../../agents/web_agent.py#L7192) | 7192 | `"        if semantic_answer_withheld:"` | — |
| [SRC-1AE03B9EC3-L007193](../../agents/web_agent.py#L7193) | 7193 | `"            answer_coverage[\"status\"] = \"semantic_support_unverified_answer_withheld\""` | — |
| [SRC-1AE03B9EC3-L007194](../../agents/web_agent.py#L7194) | 7194 | `"            answer_coverage[\"semantic_verification_status\"] = semantic_claim_verification.get(\"status\")"` | — |
| [SRC-1AE03B9EC3-L007195](../../agents/web_agent.py#L7195) | 7195 | `"        answer_coverage[\"target_checks\"] = answer_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L007196](../../agents/web_agent.py#L7196) | 7196 | `"        answer_coverage[\"potentially_missing_target_count\"] = answer_integrity[\"potentially_missing_target_count\"]"` | — |
| [SRC-1AE03B9EC3-L007197](../../agents/web_agent.py#L7197) | 7197 | `"        answer_coverage[\"source_evidence_gap_count\"] = answer_integrity[\"source_evidence_gap_count\"]"` | — |
| [SRC-1AE03B9EC3-L007198](../../agents/web_agent.py#L7198) | 7198 | `"        answer_coverage[\"lexical_screen_method\"] = \"deterministic_lexical_screen_only_not_semantic_grading\""` | — |
| [SRC-1AE03B9EC3-L007199](../../agents/web_agent.py#L7199) | 7199 | `"        requirements_without_candidates = int("` | — |
| [SRC-1AE03B9EC3-L007200](../../agents/web_agent.py#L7200) | 7200 | `"            answer_integrity.get(\"requirements_without_candidate_evidence_count\", 0) or 0"` | — |
| [SRC-1AE03B9EC3-L007201](../../agents/web_agent.py#L7201) | 7201 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007202](../../agents/web_agent.py#L7202) | 7202 | `"        task_fulfillment_status = ("` | — |
| [SRC-1AE03B9EC3-L007203](../../agents/web_agent.py#L7203) | 7203 | `"            \"possible_gap_detected\""` | — |
| [SRC-1AE03B9EC3-L007204](../../agents/web_agent.py#L7204) | 7204 | `"            if ("` | — |
| [SRC-1AE03B9EC3-L007205](../../agents/web_agent.py#L7205) | 7205 | `"                answer_integrity[\"potentially_missing_target_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L007206](../../agents/web_agent.py#L7206) | 7206 | `"                or answer_integrity[\"source_evidence_gap_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L007207](../../agents/web_agent.py#L7207) | 7207 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007208](../../agents/web_agent.py#L7208) | 7208 | `"            else \"candidate_evidence_gaps_or_linkage_unknown\""` | — |
| [SRC-1AE03B9EC3-L007209](../../agents/web_agent.py#L7209) | 7209 | `"            if coverage_targets and requirements_without_candidates > 0"` | — |
| [SRC-1AE03B9EC3-L007210](../../agents/web_agent.py#L7210) | 7210 | `"            else \"lexical_signals_found_not_semantically_verified\" if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L007211](../../agents/web_agent.py#L7211) | 7211 | `"            else \"not_machine_assessed_no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L007212](../../agents/web_agent.py#L7212) | 7212 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007213](../../agents/web_agent.py#L7213) | 7213 | `"        if semantic_answer_withheld:"` | — |
| [SRC-1AE03B9EC3-L007214](../../agents/web_agent.py#L7214) | 7214 | `"            task_fulfillment_status = \"not_assessed_insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L007215](../../agents/web_agent.py#L7215) | 7215 | `"        answer_coverage[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L007216](../../agents/web_agent.py#L7216) | 7216 | `"        answer_coverage[\"semantic_verification_status\"] = semantic_claim_verification.get(\"status\")"` | — |
| [SRC-1AE03B9EC3-L007217](../../agents/web_agent.py#L7217) | 7217 | `"        report[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L007218](../../agents/web_agent.py#L7218) | 7218 | `"        report[\"answer_integrity\"] = answer_integrity"` | — |
| [SRC-1AE03B9EC3-L007219](../../agents/web_agent.py#L7219) | 7219 | `"        report[\"requirement_evidence\"] = answer_integrity.get(\"requirement_evidence\", [])"` | — |
| [SRC-1AE03B9EC3-L007220](../../agents/web_agent.py#L7220) | 7220 | `"        report[\"connector_summary\"] = self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L007221](../../agents/web_agent.py#L7221) | 7221 | `"            list(self._provider_diagnostics), sources"` | — |
| [SRC-1AE03B9EC3-L007222](../../agents/web_agent.py#L7222) | 7222 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007223](../../agents/web_agent.py#L7223) | 7223 | `"        report[\"provider_diagnostics\"] = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L007224](../../agents/web_agent.py#L7224) | 7224 | `"        distinct_providers = {"` | — |
| [SRC-1AE03B9EC3-L007225](../../agents/web_agent.py#L7225) | 7225 | `"            provider for source in sources for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L007226](../../agents/web_agent.py#L7226) | 7226 | `"        }"` | — |
| [SRC-1AE03B9EC3-L007227](../../agents/web_agent.py#L7227) | 7227 | `"        distinct_domains = {"` | — |
| [SRC-1AE03B9EC3-L007228](../../agents/web_agent.py#L7228) | 7228 | `"            registrable_domain("` | — |
| [SRC-1AE03B9EC3-L007229](../../agents/web_agent.py#L7229) | 7229 | `"                source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L007230](../../agents/web_agent.py#L7230) | 7230 | `"                or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L007231](../../agents/web_agent.py#L7231) | 7231 | `"                or \"\""` | — |
| [SRC-1AE03B9EC3-L007232](../../agents/web_agent.py#L7232) | 7232 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007233](../../agents/web_agent.py#L7233) | 7233 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L007234](../../agents/web_agent.py#L7234) | 7234 | `"        }"` | — |
| [SRC-1AE03B9EC3-L007235](../../agents/web_agent.py#L7235) | 7235 | `"        distinct_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L007236](../../agents/web_agent.py#L7236) | 7236 | `"        fetched_pages = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L007237](../../agents/web_agent.py#L7237) | 7237 | `"        if semantic_answer_withheld:"` | — |
| [SRC-1AE03B9EC3-L007238](../../agents/web_agent.py#L7238) | 7238 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L007239](../../agents/web_agent.py#L7239) | 7239 | `"        elif ("` | — |
| [SRC-1AE03B9EC3-L007240](../../agents/web_agent.py#L7240) | 7240 | `"            len(sources) >= 4 and len(distinct_domains) >= 3"` | — |
| [SRC-1AE03B9EC3-L007241](../../agents/web_agent.py#L7241) | 7241 | `"            and len(distinct_providers) >= 2 and fetched_pages >= 1"` | — |
| [SRC-1AE03B9EC3-L007242](../../agents/web_agent.py#L7242) | 7242 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L007243](../../agents/web_agent.py#L7243) | 7243 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L007244](../../agents/web_agent.py#L7244) | 7244 | `"            research_quality = \"excellent\""` | — |
| [SRC-1AE03B9EC3-L007245](../../agents/web_agent.py#L7245) | 7245 | `"        elif ("` | — |
| [SRC-1AE03B9EC3-L007246](../../agents/web_agent.py#L7246) | 7246 | `"            len(sources) >= 2 and len(distinct_domains) >= 2"` | — |
| [SRC-1AE03B9EC3-L007247](../../agents/web_agent.py#L7247) | 7247 | `"            and (len(distinct_providers) >= 2 or fetched_pages >= 1)"` | — |
| [SRC-1AE03B9EC3-L007248](../../agents/web_agent.py#L7248) | 7248 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L007249](../../agents/web_agent.py#L7249) | 7249 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L007250](../../agents/web_agent.py#L7250) | 7250 | `"            research_quality = \"good\""` | — |
| [SRC-1AE03B9EC3-L007251](../../agents/web_agent.py#L7251) | 7251 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L007252](../../agents/web_agent.py#L7252) | 7252 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L007253](../../agents/web_agent.py#L7253) | 7253 | `""` | — |
| [SRC-1AE03B9EC3-L007254](../../agents/web_agent.py#L7254) | 7254 | `"        # Source breadth and a completed model-assisted review do not justify a"` | — |
| [SRC-1AE03B9EC3-L007255](../../agents/web_agent.py#L7255) | 7255 | `"        # positive research-quality label if the final answer has no valid source"` | — |
| [SRC-1AE03B9EC3-L007256](../../agents/web_agent.py#L7256) | 7256 | `"        # citation markers. This is a deterministic presentation guard, not a"` | — |
| [SRC-1AE03B9EC3-L007257](../../agents/web_agent.py#L7257) | 7257 | `"        # semantic entailment check."` | — |
| [SRC-1AE03B9EC3-L007258](../../agents/web_agent.py#L7258) | 7258 | `"        uncited_reviewed_answer = ("` | — |
| [SRC-1AE03B9EC3-L007259](../../agents/web_agent.py#L7259) | 7259 | `"            used_llm"` | — |
| [SRC-1AE03B9EC3-L007260](../../agents/web_agent.py#L7260) | 7260 | `"            and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L007261](../../agents/web_agent.py#L7261) | 7261 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L007262](../../agents/web_agent.py#L7262) | 7262 | `"            and citation_validation[\"valid_citation_count\"] == 0"` | — |
| [SRC-1AE03B9EC3-L007263](../../agents/web_agent.py#L7263) | 7263 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007264](../../agents/web_agent.py#L7264) | 7264 | `"        if uncited_reviewed_answer:"` | — |
| [SRC-1AE03B9EC3-L007265](../../agents/web_agent.py#L7265) | 7265 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L007266](../../agents/web_agent.py#L7266) | 7266 | `"            citation_validation[\"claim_support\"] = \"not_established_no_valid_source_citations\""` | — |
| [SRC-1AE03B9EC3-L007267](../../agents/web_agent.py#L7267) | 7267 | `"            answer_evidence_status = \"reviewed_answer_has_no_valid_citations\""` | — |
| [SRC-1AE03B9EC3-L007268](../../agents/web_agent.py#L7268) | 7268 | `"            uncited_answer_warning = ("` | — |
| [SRC-1AE03B9EC3-L007269](../../agents/web_agent.py#L7269) | 7269 | `"                \"اكتملت مراجعة النموذج، لكن الإجابة النهائية لا تحتوي على إحالات صالحة \""` | — |
| [SRC-1AE03B9EC3-L007270](../../agents/web_agent.py#L7270) | 7270 | `"                \"إلى قائمة المصادر؛ لذلك صُنّفت جودة البحث «جزئية». وجود المصادر أو \""` | — |
| [SRC-1AE03B9EC3-L007271](../../agents/web_agent.py#L7271) | 7271 | `"                \"اكتمال مراجعة النموذج لا يثبت دعم كل ادعاء.\""` | — |
| [SRC-1AE03B9EC3-L007272](../../agents/web_agent.py#L7272) | 7272 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007273](../../agents/web_agent.py#L7273) | 7273 | `"        elif citation_validation[\"valid_citation_count\"] > 0:"` | — |
| [SRC-1AE03B9EC3-L007274](../../agents/web_agent.py#L7274) | 7274 | `"            answer_evidence_status = ("` | — |
| [SRC-1AE03B9EC3-L007275](../../agents/web_agent.py#L7275) | 7275 | `"                \"semantic_support_unverified_answer_withheld\""` | — |
| [SRC-1AE03B9EC3-L007276](../../agents/web_agent.py#L7276) | 7276 | `"                if semantic_answer_withheld else \"citation_indices_validated_only\""` | — |
| [SRC-1AE03B9EC3-L007277](../../agents/web_agent.py#L7277) | 7277 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007278](../../agents/web_agent.py#L7278) | 7278 | `"            uncited_answer_warning = None"` | — |
| [SRC-1AE03B9EC3-L007279](../../agents/web_agent.py#L7279) | 7279 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L007280](../../agents/web_agent.py#L7280) | 7280 | `"            answer_evidence_status = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L007281](../../agents/web_agent.py#L7281) | 7281 | `"            uncited_answer_warning = None"` | — |
| [SRC-1AE03B9EC3-L007282](../../agents/web_agent.py#L7282) | 7282 | `""` | — |
| [SRC-1AE03B9EC3-L007283](../../agents/web_agent.py#L7283) | 7283 | `"        search_attempted = search_attempted or bool(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L007284](../../agents/web_agent.py#L7284) | 7284 | `"        report[\"search_attempted\"] = search_attempted"` | — |
| [SRC-1AE03B9EC3-L007285](../../agents/web_agent.py#L7285) | 7285 | `"        prior_search_outcome = report.get(\"search_outcome\")"` | — |
| [SRC-1AE03B9EC3-L007286](../../agents/web_agent.py#L7286) | 7286 | `"        if prior_search_outcome in _RESEARCH_ERROR_OUTCOMES and not sources:"` | — |
| [SRC-1AE03B9EC3-L007287](../../agents/web_agent.py#L7287) | 7287 | `"            # Preserve a known pipeline failure instead of relabeling it as an ordinary"` | — |
| [SRC-1AE03B9EC3-L007288](../../agents/web_agent.py#L7288) | 7288 | `"            # zero-result search merely because the outer request reached its return path."` | — |
| [SRC-1AE03B9EC3-L007289](../../agents/web_agent.py#L7289) | 7289 | `"            report[\"search_outcome\"] = prior_search_outcome"` | — |
| [SRC-1AE03B9EC3-L007290](../../agents/web_agent.py#L7290) | 7290 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L007291](../../agents/web_agent.py#L7291) | 7291 | `"            report[\"search_outcome\"] = ("` | — |
| [SRC-1AE03B9EC3-L007292](../../agents/web_agent.py#L7292) | 7292 | `"                \"attempted_with_usable_sources\" if search_attempted and sources"` | — |
| [SRC-1AE03B9EC3-L007293](../../agents/web_agent.py#L7293) | 7293 | `"                else \"attempted_no_usable_sources\" if search_attempted"` | — |
| [SRC-1AE03B9EC3-L007294](../../agents/web_agent.py#L7294) | 7294 | `"                else \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L007295](../../agents/web_agent.py#L7295) | 7295 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007296](../../agents/web_agent.py#L7296) | 7296 | `"        report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L007297](../../agents/web_agent.py#L7297) | 7297 | `"        report[\"research_quality\"] = research_quality"` | — |
| [SRC-1AE03B9EC3-L007298](../../agents/web_agent.py#L7298) | 7298 | `"        report[\"research_quality_semantics\"] = \"process_coverage_not_factual_probability\""` | — |
| [SRC-1AE03B9EC3-L007299](../../agents/web_agent.py#L7299) | 7299 | `"        report[\"answer_evidence_status\"] = answer_evidence_status"` | — |
| [SRC-1AE03B9EC3-L007300](../../agents/web_agent.py#L7300) | 7300 | `"        report[\"distinct_registrable_domains\"] = len(distinct_domains)"` | — |
| [SRC-1AE03B9EC3-L007301](../../agents/web_agent.py#L7301) | 7301 | `"        report[\"independent_sources\"] = len(distinct_domains)  # Legacy alias; not editorial independence."` | — |
| [SRC-1AE03B9EC3-L007302](../../agents/web_agent.py#L7302) | 7302 | `"        report[\"independent_sources_field_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L007303](../../agents/web_agent.py#L7303) | 7303 | `"            \"legacy_compatibility_alias_for_distinct_registrable_domain_count\""` | — |
| [SRC-1AE03B9EC3-L007304](../../agents/web_agent.py#L7304) | 7304 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007305](../../agents/web_agent.py#L7305) | 7305 | `"        report[\"source_diversity_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L007306](../../agents/web_agent.py#L7306) | 7306 | `"            \"distinct_registrable_domains_not_editorial_independence\""` | — |
| [SRC-1AE03B9EC3-L007307](../../agents/web_agent.py#L7307) | 7307 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007308](../../agents/web_agent.py#L7308) | 7308 | `"        report[\"editorial_independence_status\"] = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L007309](../../agents/web_agent.py#L7309) | 7309 | `"        report[\"claim_audit_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L007310](../../agents/web_agent.py#L7310) | 7310 | `"            \"distinct_model_assessed_source_support_not_ground_truth\""` | — |
| [SRC-1AE03B9EC3-L007311](../../agents/web_agent.py#L7311) | 7311 | `"            if semantic_claim_verification.get(\"status\") in {"` | — |
| [SRC-1AE03B9EC3-L007312](../../agents/web_agent.py#L7312) | 7312 | `"                \"completed_all_claims_supported\", \"completed_no_factual_claims\""` | — |
| [SRC-1AE03B9EC3-L007313](../../agents/web_agent.py#L7313) | 7313 | `"            }"` | — |
| [SRC-1AE03B9EC3-L007314](../../agents/web_agent.py#L7314) | 7314 | `"            else \"not_verified\""` | — |
| [SRC-1AE03B9EC3-L007315](../../agents/web_agent.py#L7315) | 7315 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007316](../../agents/web_agent.py#L7316) | 7316 | `"        report[\"insufficient_evidence\"] = bool("` | — |
| [SRC-1AE03B9EC3-L007317](../../agents/web_agent.py#L7317) | 7317 | `"            report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES"` | — |
| [SRC-1AE03B9EC3-L007318](../../agents/web_agent.py#L7318) | 7318 | `"            or not sources"` | — |
| [SRC-1AE03B9EC3-L007319](../../agents/web_agent.py#L7319) | 7319 | `"            or semantic_answer_withheld"` | — |
| [SRC-1AE03B9EC3-L007320](../../agents/web_agent.py#L7320) | 7320 | `"            or answer_integrity[\"source_evidence_gap_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L007321](../../agents/web_agent.py#L7321) | 7321 | `"            or ("` | — |
| [SRC-1AE03B9EC3-L007322](../../agents/web_agent.py#L7322) | 7322 | `"                bool(coverage_targets)"` | — |
| [SRC-1AE03B9EC3-L007323](../../agents/web_agent.py#L7323) | 7323 | `"                and answer_integrity[\"potentially_missing_target_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L007324](../../agents/web_agent.py#L7324) | 7324 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007325](../../agents/web_agent.py#L7325) | 7325 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007326](../../agents/web_agent.py#L7326) | 7326 | `"        report[\"valid_citation_range\"] = [1, max_citable_sources] if max_citable_sources else []"` | — |
| [SRC-1AE03B9EC3-L007327](../../agents/web_agent.py#L7327) | 7327 | `"        report[\"citation_count\"] = citation_validation[\"valid_citation_count\"]"` | — |
| [SRC-1AE03B9EC3-L007328](../../agents/web_agent.py#L7328) | 7328 | `"        report[\"citation_check\"] = citation_validation[\"status\"]"` | — |
| [SRC-1AE03B9EC3-L007329](../../agents/web_agent.py#L7329) | 7329 | `"        report[\"citation_validation\"] = citation_validation"` | — |
| [SRC-1AE03B9EC3-L007330](../../agents/web_agent.py#L7330) | 7330 | `"        warnings = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L007331](../../agents/web_agent.py#L7331) | 7331 | `"            search_warnings"` | — |
| [SRC-1AE03B9EC3-L007332](../../agents/web_agent.py#L7332) | 7332 | `"            + ([llm_warning] if llm_warning else [])"` | — |
| [SRC-1AE03B9EC3-L007333](../../agents/web_agent.py#L7333) | 7333 | `"            + ([review_warning] if review_warning else [])"` | — |
| [SRC-1AE03B9EC3-L007334](../../agents/web_agent.py#L7334) | 7334 | `"            + ([coverage_repair_warning] if coverage_repair_warning else [])"` | — |
| [SRC-1AE03B9EC3-L007335](../../agents/web_agent.py#L7335) | 7335 | `"            + citation_warnings"` | — |
| [SRC-1AE03B9EC3-L007336](../../agents/web_agent.py#L7336) | 7336 | `"            + ([uncited_answer_warning] if uncited_answer_warning else [])"` | — |
| [SRC-1AE03B9EC3-L007337](../../agents/web_agent.py#L7337) | 7337 | `"            + (["` | — |
| [SRC-1AE03B9EC3-L007338](../../agents/web_agent.py#L7338) | 7338 | `"                \"حُجبت الإجابة المولدة لعدم اكتمال التحقق الدلالي المستقل عن نموذج الصياغة.\""` | — |
| [SRC-1AE03B9EC3-L007339](../../agents/web_agent.py#L7339) | 7339 | `"            ] if semantic_answer_withheld else [])"` | — |
| [SRC-1AE03B9EC3-L007340](../../agents/web_agent.py#L7340) | 7340 | `"        ))"` | — |
| [SRC-1AE03B9EC3-L007341](../../agents/web_agent.py#L7341) | 7341 | `"        report[\"model_calls\"] = list(self.model_usage)"` | — |
| [SRC-1AE03B9EC3-L007342](../../agents/web_agent.py#L7342) | 7342 | `"        report[\"openrouter_web_search_enabled\"] = self.openrouter_web_search_enabled"` | — |
| [SRC-1AE03B9EC3-L007343](../../agents/web_agent.py#L7343) | 7343 | `"        report[\"openrouter_web_search_results\"] = len(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L007344](../../agents/web_agent.py#L7344) | 7344 | `"        if semantic_answer_withheld:"` | — |
| [SRC-1AE03B9EC3-L007345](../../agents/web_agent.py#L7345) | 7345 | `"            final_answer_status = \"semantic_verification_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L007346](../../agents/web_agent.py#L7346) | 7346 | `"        elif generation_budget_exhausted or review_budget_exhausted:"` | — |
| [SRC-1AE03B9EC3-L007347](../../agents/web_agent.py#L7347) | 7347 | `"            final_answer_status = \"budget_exhausted_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L007348](../../agents/web_agent.py#L7348) | 7348 | `"        elif llm_warning:"` | — |
| [SRC-1AE03B9EC3-L007349](../../agents/web_agent.py#L7349) | 7349 | `"            final_answer_status = ("` | — |
| [SRC-1AE03B9EC3-L007350](../../agents/web_agent.py#L7350) | 7350 | `"                \"model_not_configured_fallback\""` | — |
| [SRC-1AE03B9EC3-L007351](../../agents/web_agent.py#L7351) | 7351 | `"                if not self.api_key"` | — |
| [SRC-1AE03B9EC3-L007352](../../agents/web_agent.py#L7352) | 7352 | `"                else \"generation_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L007353](../../agents/web_agent.py#L7353) | 7353 | `"            )"` | — |
| [SRC-1AE03B9EC3-L007354](../../agents/web_agent.py#L7354) | 7354 | `"        elif review_warning:"` | — |
| [SRC-1AE03B9EC3-L007355](../../agents/web_agent.py#L7355) | 7355 | `"            final_answer_status = \"review_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L007356](../../agents/web_agent.py#L7356) | 7356 | `"        elif coverage_repair_status == \"no_change_gap_unresolved\":"` | — |
| [SRC-1AE03B9EC3-L007357](../../agents/web_agent.py#L7357) | 7357 | `"            final_answer_status = \"coverage_repair_left_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L007358](../../agents/web_agent.py#L7358) | 7358 | `"        elif coverage_repair_status == \"budget_exhausted\":"` | — |
| [SRC-1AE03B9EC3-L007359](../../agents/web_agent.py#L7359) | 7359 | `"            final_answer_status = \"coverage_repair_budget_exhausted_with_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L007360](../../agents/web_agent.py#L7360) | 7360 | `"        elif coverage_repair_status == \"unavailable\":"` | — |
| [SRC-1AE03B9EC3-L007361](../../agents/web_agent.py#L7361) | 7361 | `"            final_answer_status = \"coverage_repair_unavailable_with_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L007362](../../agents/web_agent.py#L7362) | 7362 | `"        elif used_llm:"` | — |
| [SRC-1AE03B9EC3-L007363](../../agents/web_agent.py#L7363) | 7363 | `"            final_answer_status = \"model_answer_generated\""` | — |
| [SRC-1AE03B9EC3-L007364](../../agents/web_agent.py#L7364) | 7364 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L007365](../../agents/web_agent.py#L7365) | 7365 | `"            final_answer_status = \"source_fallback\""` | — |
| [SRC-1AE03B9EC3-L007366](../../agents/web_agent.py#L7366) | 7366 | `""` | — |
| [SRC-1AE03B9EC3-L007367](../../agents/web_agent.py#L7367) | 7367 | `"        # Report pipeline completion separately from factual correctness. A successful"` | — |
| [SRC-1AE03B9EC3-L007368](../../agents/web_agent.py#L7368) | 7368 | `"        # retrieval or model review is not an independent semantic fact check."` | — |
| [SRC-1AE03B9EC3-L007369](../../agents/web_agent.py#L7369) | 7369 | `"        if report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES:"` | — |
| [SRC-1AE03B9EC3-L007370](../../agents/web_agent.py#L7370) | 7370 | `"            pipeline_completion_status = \"execution_failed\""` | — |
| [SRC-1AE03B9EC3-L007371](../../agents/web_agent.py#L7371) | 7371 | `"        elif not search_attempted:"` | — |
| [SRC-1AE03B9EC3-L007372](../../agents/web_agent.py#L7372) | 7372 | `"            pipeline_completion_status = \"not_verified\""` | — |
| [SRC-1AE03B9EC3-L007373](../../agents/web_agent.py#L7373) | 7373 | `"        elif not sources:"` | — |
| [SRC-1AE03B9EC3-L007374](../../agents/web_agent.py#L7374) | 7374 | `"            pipeline_completion_status = \"insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L007375](../../agents/web_agent.py#L7375) | 7375 | `"        elif ("` | — |
| [SRC-1AE03B9EC3-L007376](../../agents/web_agent.py#L7376) | 7376 | `"            llm_warning"` | — |
| [SRC-1AE03B9EC3-L007377](../../agents/web_agent.py#L7377) | 7377 | `"            or review_warning"` | — |
| [SRC-1AE03B9EC3-L007378](../../agents/web_agent.py#L7378) | 7378 | `"            or review_status != \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L007379](../../agents/web_agent.py#L7379) | 7379 | `"            or answer_integrity[\"potentially_missing_target_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L007380](../../agents/web_agent.py#L7380) | 7380 | `"            or answer_integrity[\"source_evidence_gap_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L007381](../../agents/web_agent.py#L7381) | 7381 | `"            or citation_validation[\"valid_citation_count\"] == 0"` | — |
| [SRC-1AE03B9EC3-L007382](../../agents/web_agent.py#L7382) | 7382 | `"            or semantic_answer_withheld"` | — |
| [SRC-1AE03B9EC3-L007383](../../agents/web_agent.py#L7383) | 7383 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L007384](../../agents/web_agent.py#L7384) | 7384 | `"            pipeline_completion_status = \"partial\""` | — |
| [SRC-1AE03B9EC3-L007385](../../agents/web_agent.py#L7385) | 7385 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L007386](../../agents/web_agent.py#L7386) | 7386 | `"            pipeline_completion_status = \"completed\""` | — |
| [SRC-1AE03B9EC3-L007387](../../agents/web_agent.py#L7387) | 7387 | `"        completion_stages = {"` | — |
| [SRC-1AE03B9EC3-L007388](../../agents/web_agent.py#L7388) | 7388 | `"            \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L007389](../../agents/web_agent.py#L7389) | 7389 | `"            \"accepted_sources\": len(sources),"` | — |
| [SRC-1AE03B9EC3-L007390](../../agents/web_agent.py#L7390) | 7390 | `"            \"pages_read\": fetched_pages,"` | — |
| [SRC-1AE03B9EC3-L007391](../../agents/web_agent.py#L7391) | 7391 | `"            \"answer_generated_by_model\": bool(used_llm),"` | — |
| [SRC-1AE03B9EC3-L007392](../../agents/web_agent.py#L7392) | 7392 | `"            \"claim_review\": review_status,"` | — |
| [SRC-1AE03B9EC3-L007393](../../agents/web_agent.py#L7393) | 7393 | `"            \"valid_citations\": citation_validation[\"valid_citation_count\"],"` | — |
| [SRC-1AE03B9EC3-L007394](../../agents/web_agent.py#L7394) | 7394 | `"            \"semantic_fact_check\": \"not_performed\","` | — |
| [SRC-1AE03B9EC3-L007395](../../agents/web_agent.py#L7395) | 7395 | `"            \"semantic_claim_support_assessment\": semantic_claim_verification.get(\"status\", \"not_performed\"),"` | — |
| [SRC-1AE03B9EC3-L007396](../../agents/web_agent.py#L7396) | 7396 | `"        }"` | — |
| [SRC-1AE03B9EC3-L007397](../../agents/web_agent.py#L7397) | 7397 | `"        if semantic_answer_withheld:"` | — |
| [SRC-1AE03B9EC3-L007398](../../agents/web_agent.py#L7398) | 7398 | `"            pipeline_completion_status = \"partial\""` | — |
| [SRC-1AE03B9EC3-L007399](../../agents/web_agent.py#L7399) | 7399 | `"        report[\"pipeline_completion_status\"] = pipeline_completion_status"` | — |
| [SRC-1AE03B9EC3-L007400](../../agents/web_agent.py#L7400) | 7400 | `"        report[\"completion_stages\"] = completion_stages"` | — |
| [SRC-1AE03B9EC3-L007401](../../agents/web_agent.py#L7401) | 7401 | `"        report[\"pipeline_completion_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L007402](../../agents/web_agent.py#L7402) | 7402 | `"            \"pipeline stage completion only; not a guarantee of factual correctness\""` | — |
| [SRC-1AE03B9EC3-L007403](../../agents/web_agent.py#L7403) | 7403 | `"        )"` | — |
| [SRC-1AE03B9EC3-L007404](../../agents/web_agent.py#L7404) | 7404 | `""` | — |
| [SRC-1AE03B9EC3-L007405](../../agents/web_agent.py#L7405) | 7405 | `"        public_sources = []"` | — |
| [SRC-1AE03B9EC3-L007406](../../agents/web_agent.py#L7406) | 7406 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L007407](../../agents/web_agent.py#L7407) | 7407 | `"            public_sources.append({"` | — |
| [SRC-1AE03B9EC3-L007408](../../agents/web_agent.py#L7408) | 7408 | `"                \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L007409](../../agents/web_agent.py#L7409) | 7409 | `"                \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L007410](../../agents/web_agent.py#L7410) | 7410 | `"                \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007411](../../agents/web_agent.py#L7411) | 7411 | `"                \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L007412](../../agents/web_agent.py#L7412) | 7412 | `"                \"readable_page_text_available\": bool(source.get(\"page_fetched\")) and bool(str(source.get(\"page_text\") or \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L007413](../../agents/web_agent.py#L7413) | 7413 | `"                \"page_text_present_without_fetch_flag\": bool(str(source.get(\"page_text\") or \"\").strip()) and not bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L007414](../../agents/web_agent.py#L7414) | 7414 | `"                \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L007415](../../agents/web_agent.py#L7415) | 7415 | `"                \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L007416](../../agents/web_agent.py#L7416) | 7416 | `"                \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L007417](../../agents/web_agent.py#L7417) | 7417 | `"                \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007418](../../agents/web_agent.py#L7418) | 7418 | `"                \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L007419](../../agents/web_agent.py#L7419) | 7419 | `"                \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007420](../../agents/web_agent.py#L7420) | 7420 | `"                \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007421](../../agents/web_agent.py#L7421) | 7421 | `"                \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L007422](../../agents/web_agent.py#L7422) | 7422 | `"                \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L007423](../../agents/web_agent.py#L7423) | 7423 | `"                \"lead_qualification\": source.get(\"lead_qualification\"),"` | — |
| [SRC-1AE03B9EC3-L007424](../../agents/web_agent.py#L7424) | 7424 | `"                \"lead_intent_evidence\": source.get(\"lead_intent_evidence\"),"` | — |
| [SRC-1AE03B9EC3-L007425](../../agents/web_agent.py#L7425) | 7425 | `"            })"` | — |
| [SRC-1AE03B9EC3-L007426](../../agents/web_agent.py#L7426) | 7426 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L007427](../../agents/web_agent.py#L7427) | 7427 | `"            \"answer\": answer,"` | — |
| [SRC-1AE03B9EC3-L007428](../../agents/web_agent.py#L7428) | 7428 | `"            \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L007429](../../agents/web_agent.py#L7429) | 7429 | `"            \"search_query\": (plan.get(\"queries\") or [\"\"])[0],"` | — |
| [SRC-1AE03B9EC3-L007430](../../agents/web_agent.py#L7430) | 7430 | `"            \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L007431](../../agents/web_agent.py#L7431) | 7431 | `"            \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L007432](../../agents/web_agent.py#L7432) | 7432 | `"                \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L007433](../../agents/web_agent.py#L7433) | 7433 | `"                \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L007434](../../agents/web_agent.py#L7434) | 7434 | `"                \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L007435](../../agents/web_agent.py#L7435) | 7435 | `"                \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L007436](../../agents/web_agent.py#L7436) | 7436 | `"                \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L007437](../../agents/web_agent.py#L7437) | 7437 | `"                \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L007438](../../agents/web_agent.py#L7438) | 7438 | `"                \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L007439](../../agents/web_agent.py#L7439) | 7439 | `"                \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L007440](../../agents/web_agent.py#L7440) | 7440 | `"                \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L007441](../../agents/web_agent.py#L7441) | 7441 | `"                \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L007442](../../agents/web_agent.py#L7442) | 7442 | `"            },"` | — |
| [SRC-1AE03B9EC3-L007443](../../agents/web_agent.py#L7443) | 7443 | `"            \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L007444](../../agents/web_agent.py#L7444) | 7444 | `"            \"sources\": public_sources,"` | — |
| [SRC-1AE03B9EC3-L007445](../../agents/web_agent.py#L7445) | 7445 | `"            \"research_quality\": research_quality,"` | — |
| [SRC-1AE03B9EC3-L007446](../../agents/web_agent.py#L7446) | 7446 | `"            \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L007447](../../agents/web_agent.py#L7447) | 7447 | `"            \"answer_evidence_status\": answer_evidence_status,"` | — |
| [SRC-1AE03B9EC3-L007448](../../agents/web_agent.py#L7448) | 7448 | `"            \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L007449](../../agents/web_agent.py#L7449) | 7449 | `"            \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L007450](../../agents/web_agent.py#L7450) | 7450 | `"            \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L007451](../../agents/web_agent.py#L7451) | 7451 | `"            \"coverage_repair_status\": coverage_repair_status,"` | — |
| [SRC-1AE03B9EC3-L007452](../../agents/web_agent.py#L7452) | 7452 | `"            \"used_language_model\": used_llm,"` | — |
| [SRC-1AE03B9EC3-L007453](../../agents/web_agent.py#L7453) | 7453 | `"            \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L007454](../../agents/web_agent.py#L7454) | 7454 | `"            \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L007455](../../agents/web_agent.py#L7455) | 7455 | `"            \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L007456](../../agents/web_agent.py#L7456) | 7456 | `"            \"warnings\": warnings,"` | — |
| [SRC-1AE03B9EC3-L007457](../../agents/web_agent.py#L7457) | 7457 | `"            \"kind\": \"web_research\" if used_llm else \"web_fallback\","` | — |
| [SRC-1AE03B9EC3-L007458](../../agents/web_agent.py#L7458) | 7458 | `"            \"final_answer_status\": final_answer_status,"` | — |
| [SRC-1AE03B9EC3-L007459](../../agents/web_agent.py#L7459) | 7459 | `"            \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L007460](../../agents/web_agent.py#L7460) | 7460 | `"            \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L007461](../../agents/web_agent.py#L7461) | 7461 | `"        }"` | — |
| [SRC-1AE03B9EC3-L007462](../../agents/web_agent.py#L7462) | 7462 | `""` | — |
| [SRC-1AE03B9EC3-L007463](../../agents/web_agent.py#L7463) | 7463 | `"def _normalized_provider_usage("` | — |
| [SRC-1AE03B9EC3-L007464](../../agents/web_agent.py#L7464) | 7464 | `"    usage: Any, *, provider_base_url: str = \"\""` | — |
| [SRC-1AE03B9EC3-L007465](../../agents/web_agent.py#L7465) | 7465 | `") -> dict[str, int \| float] \| None:"` | — |
| [SRC-1AE03B9EC3-L007466](../../agents/web_agent.py#L7466) | 7466 | `"    \"\"\"Allowlist safe counters; interpret generic 'cost' as USD only for OpenRouter.\"\"\""` | — |
| [SRC-1AE03B9EC3-L007467](../../agents/web_agent.py#L7467) | 7467 | `"    if not isinstance(usage, dict):"` | — |
| [SRC-1AE03B9EC3-L007468](../../agents/web_agent.py#L7468) | 7468 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L007469](../../agents/web_agent.py#L7469) | 7469 | `"    normalized: dict[str, int \| float] = {}"` | — |
| [SRC-1AE03B9EC3-L007470](../../agents/web_agent.py#L7470) | 7470 | `"    for source_key in (\"prompt_tokens\", \"completion_tokens\", \"total_tokens\"):"` | — |
| [SRC-1AE03B9EC3-L007471](../../agents/web_agent.py#L7471) | 7471 | `"        value = usage.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L007472](../../agents/web_agent.py#L7472) | 7472 | `"        if isinstance(value, int) and not isinstance(value, bool) and value >= 0:"` | — |
| [SRC-1AE03B9EC3-L007473](../../agents/web_agent.py#L7473) | 7473 | `"            normalized[source_key] = value"` | — |
| [SRC-1AE03B9EC3-L007474](../../agents/web_agent.py#L7474) | 7474 | `"    cost_keys = [\"cost_usd\"]"` | — |
| [SRC-1AE03B9EC3-L007475](../../agents/web_agent.py#L7475) | 7475 | `"    provider_host = \"\""` | — |
| [SRC-1AE03B9EC3-L007476](../../agents/web_agent.py#L7476) | 7476 | `"    if isinstance(provider_base_url, str):"` | — |
| [SRC-1AE03B9EC3-L007477](../../agents/web_agent.py#L7477) | 7477 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L007478](../../agents/web_agent.py#L7478) | 7478 | `"            provider_host = (urllib.parse.urlsplit(provider_base_url.strip()).hostname or \"\").lower().rstrip(\".\")"` | — |
| [SRC-1AE03B9EC3-L007479](../../agents/web_agent.py#L7479) | 7479 | `"        except ValueError:"` | — |
| [SRC-1AE03B9EC3-L007480](../../agents/web_agent.py#L7480) | 7480 | `"            provider_host = \"\""` | — |
| [SRC-1AE03B9EC3-L007481](../../agents/web_agent.py#L7481) | 7481 | `"    is_openrouter = ("` | — |
| [SRC-1AE03B9EC3-L007482](../../agents/web_agent.py#L7482) | 7482 | `"        provider_host == \"openrouter.ai\""` | — |
| [SRC-1AE03B9EC3-L007483](../../agents/web_agent.py#L7483) | 7483 | `"        or provider_host.endswith(\".openrouter.ai\")"` | — |
| [SRC-1AE03B9EC3-L007484](../../agents/web_agent.py#L7484) | 7484 | `"    )"` | — |
| [SRC-1AE03B9EC3-L007485](../../agents/web_agent.py#L7485) | 7485 | `"    if is_openrouter:"` | — |
| [SRC-1AE03B9EC3-L007486](../../agents/web_agent.py#L7486) | 7486 | `"        cost_keys.extend([\"cost\", \"total_cost\"])"` | — |
| [SRC-1AE03B9EC3-L007487](../../agents/web_agent.py#L7487) | 7487 | `"    for source_key in cost_keys:"` | — |
| [SRC-1AE03B9EC3-L007488](../../agents/web_agent.py#L7488) | 7488 | `"        value = usage.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L007489](../../agents/web_agent.py#L7489) | 7489 | `"        if isinstance(value, (int, float)) and not isinstance(value, bool):"` | — |
| [SRC-1AE03B9EC3-L007490](../../agents/web_agent.py#L7490) | 7490 | `"            number = float(value)"` | — |
| [SRC-1AE03B9EC3-L007491](../../agents/web_agent.py#L7491) | 7491 | `"            if number >= 0 and math.isfinite(number):"` | — |
| [SRC-1AE03B9EC3-L007492](../../agents/web_agent.py#L7492) | 7492 | `"                normalized[\"cost_usd\"] = number"` | — |
| [SRC-1AE03B9EC3-L007493](../../agents/web_agent.py#L7493) | 7493 | `"                break"` | — |
| [SRC-1AE03B9EC3-L007494](../../agents/web_agent.py#L7494) | 7494 | `"    return normalized or None"` | — |
| [SRC-1AE03B9EC3-L007495](../../agents/web_agent.py#L7495) | 7495 | `""` | — |
| [SRC-1AE03B9EC3-L007496](../../agents/web_agent.py#L7496) | 7496 | `"def _model_usage_record("` | — |
| [SRC-1AE03B9EC3-L007497](../../agents/web_agent.py#L7497) | 7497 | `"    requested_model: str,"` | — |
| [SRC-1AE03B9EC3-L007498](../../agents/web_agent.py#L7498) | 7498 | `"    candidate_model: str,"` | — |
| [SRC-1AE03B9EC3-L007499](../../agents/web_agent.py#L7499) | 7499 | `"    response_data: dict[str, Any],"` | — |
| [SRC-1AE03B9EC3-L007500](../../agents/web_agent.py#L7500) | 7500 | `"    provider_base_url: str,"` | — |
| [SRC-1AE03B9EC3-L007501](../../agents/web_agent.py#L7501) | 7501 | `") -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L007502](../../agents/web_agent.py#L7502) | 7502 | `"    \"\"\"Return only allowlisted provider usage metadata, never raw prompts/responses.\"\"\""` | — |
| [SRC-1AE03B9EC3-L007503](../../agents/web_agent.py#L7503) | 7503 | `"    record: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L007504](../../agents/web_agent.py#L7504) | 7504 | `"        \"requested_model\": requested_model,"` | — |
| [SRC-1AE03B9EC3-L007505](../../agents/web_agent.py#L7505) | 7505 | `"        \"used_model\": candidate_model,"` | — |
| [SRC-1AE03B9EC3-L007506](../../agents/web_agent.py#L7506) | 7506 | `"        \"fallback_used\": \"true\" if candidate_model != requested_model else \"false\","` | — |
| [SRC-1AE03B9EC3-L007507](../../agents/web_agent.py#L7507) | 7507 | `"    }"` | — |
| [SRC-1AE03B9EC3-L007508](../../agents/web_agent.py#L7508) | 7508 | `"    provider_usage = _normalized_provider_usage("` | — |
| [SRC-1AE03B9EC3-L007509](../../agents/web_agent.py#L7509) | 7509 | `"        response_data.get(\"usage\"), provider_base_url=provider_base_url"` | — |
| [SRC-1AE03B9EC3-L007510](../../agents/web_agent.py#L7510) | 7510 | `"    )"` | — |
| [SRC-1AE03B9EC3-L007511](../../agents/web_agent.py#L7511) | 7511 | `"    if provider_usage is not None:"` | — |
| [SRC-1AE03B9EC3-L007512](../../agents/web_agent.py#L7512) | 7512 | `"        record[\"provider_usage\"] = provider_usage"` | — |
| [SRC-1AE03B9EC3-L007513](../../agents/web_agent.py#L7513) | 7513 | `"    return record"` | — |
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
