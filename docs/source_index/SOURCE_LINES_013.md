# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **013**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L005017 إلى SRC-1AE03B9EC3-L005816
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L005017](../../agents/web_agent.py#L5017) | 5017 | `"                    \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005018](../../agents/web_agent.py#L5018) | 5018 | `"                    \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L005019](../../agents/web_agent.py#L5019) | 5019 | `"                    \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005020](../../agents/web_agent.py#L5020) | 5020 | `"                    \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005021](../../agents/web_agent.py#L5021) | 5021 | `"                    \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005022](../../agents/web_agent.py#L5022) | 5022 | `"                    \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L005023](../../agents/web_agent.py#L5023) | 5023 | `"                    \"lead_qualification\": \"related_result_not_lead\","` | — |
| [SRC-1AE03B9EC3-L005024](../../agents/web_agent.py#L5024) | 5024 | `"                } for source in sources]"` | — |
| [SRC-1AE03B9EC3-L005025](../../agents/web_agent.py#L5025) | 5025 | `"                return {"` | — |
| [SRC-1AE03B9EC3-L005026](../../agents/web_agent.py#L5026) | 5026 | `"                    \"answer\": lead_answer,"` | — |
| [SRC-1AE03B9EC3-L005027](../../agents/web_agent.py#L5027) | 5027 | `"                    \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L005028](../../agents/web_agent.py#L5028) | 5028 | `"                    \"search_query\": (plan.get(\"queries\") or [\"\"])[0],"` | — |
| [SRC-1AE03B9EC3-L005029](../../agents/web_agent.py#L5029) | 5029 | `"                    \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L005030](../../agents/web_agent.py#L5030) | 5030 | `"                    \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L005031](../../agents/web_agent.py#L5031) | 5031 | `"                        \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L005032](../../agents/web_agent.py#L5032) | 5032 | `"                        \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L005033](../../agents/web_agent.py#L5033) | 5033 | `"                        \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L005034](../../agents/web_agent.py#L5034) | 5034 | `"                        \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L005035](../../agents/web_agent.py#L5035) | 5035 | `"                        \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L005036](../../agents/web_agent.py#L5036) | 5036 | `"                        \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L005037](../../agents/web_agent.py#L5037) | 5037 | `"                        \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L005038](../../agents/web_agent.py#L5038) | 5038 | `"                        \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L005039](../../agents/web_agent.py#L5039) | 5039 | `"                        \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L005040](../../agents/web_agent.py#L5040) | 5040 | `"                        \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L005041](../../agents/web_agent.py#L5041) | 5041 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L005042](../../agents/web_agent.py#L5042) | 5042 | `"                    \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L005043](../../agents/web_agent.py#L5043) | 5043 | `"                    \"sources\": public_related_sources,"` | — |
| [SRC-1AE03B9EC3-L005044](../../agents/web_agent.py#L5044) | 5044 | `"                    \"used_language_model\": False,"` | — |
| [SRC-1AE03B9EC3-L005045](../../agents/web_agent.py#L5045) | 5045 | `"                    \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L005046](../../agents/web_agent.py#L5046) | 5046 | `"                    \"search_attempted\": report.get("` | — |
| [SRC-1AE03B9EC3-L005047](../../agents/web_agent.py#L5047) | 5047 | `"                        \"search_attempted\","` | — |
| [SRC-1AE03B9EC3-L005048](../../agents/web_agent.py#L5048) | 5048 | `"                        bool(report.get(\"queries_attempted\", 0)),"` | — |
| [SRC-1AE03B9EC3-L005049](../../agents/web_agent.py#L5049) | 5049 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L005050](../../agents/web_agent.py#L5050) | 5050 | `"                    \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L005051](../../agents/web_agent.py#L5051) | 5051 | `"                    \"warnings\": [lead_answer],"` | — |
| [SRC-1AE03B9EC3-L005052](../../agents/web_agent.py#L5052) | 5052 | `"                    \"kind\": \"lead_discovery_no_qualified_candidates\","` | — |
| [SRC-1AE03B9EC3-L005053](../../agents/web_agent.py#L5053) | 5053 | `"                    \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L005054](../../agents/web_agent.py#L5054) | 5054 | `"                    \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L005055](../../agents/web_agent.py#L5055) | 5055 | `"                    \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L005056](../../agents/web_agent.py#L5056) | 5056 | `"                }"` | — |
| [SRC-1AE03B9EC3-L005057](../../agents/web_agent.py#L5057) | 5057 | `"            # Only explicit public buyer-intent signals may be synthesized as lead candidates."` | — |
| [SRC-1AE03B9EC3-L005058](../../agents/web_agent.py#L5058) | 5058 | `"            sources = lead_evidence_sources"` | — |
| [SRC-1AE03B9EC3-L005059](../../agents/web_agent.py#L5059) | 5059 | `"            report[\"evidence_signals\"] = evidence_signal_report(sources, plan.get(\"freshness\", \"any\"))"` | — |
| [SRC-1AE03B9EC3-L005060](../../agents/web_agent.py#L5060) | 5060 | `"            report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005061](../../agents/web_agent.py#L5061) | 5061 | `"            report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005062](../../agents/web_agent.py#L5062) | 5062 | `"            report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L005063](../../agents/web_agent.py#L5063) | 5063 | `"            independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L005064](../../agents/web_agent.py#L5064) | 5064 | `"                registrable_domain("` | — |
| [SRC-1AE03B9EC3-L005065](../../agents/web_agent.py#L5065) | 5065 | `"                    source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L005066](../../agents/web_agent.py#L5066) | 5066 | `"                    or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L005067](../../agents/web_agent.py#L5067) | 5067 | `"                    or \"\""` | — |
| [SRC-1AE03B9EC3-L005068](../../agents/web_agent.py#L5068) | 5068 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005069](../../agents/web_agent.py#L5069) | 5069 | `"                for source in sources"` | — |
| [SRC-1AE03B9EC3-L005070](../../agents/web_agent.py#L5070) | 5070 | `"            }"` | — |
| [SRC-1AE03B9EC3-L005071](../../agents/web_agent.py#L5071) | 5071 | `"            independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L005072](../../agents/web_agent.py#L5072) | 5072 | `"        single_source_navigation = navigation_request and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L005073](../../agents/web_agent.py#L5073) | 5073 | `"        single_source_social = bool(plan.get(\"social_focus\")) and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L005074](../../agents/web_agent.py#L5074) | 5074 | `"        single_source_lead = lead_request and bool(lead_evidence_sources)"` | — |
| [SRC-1AE03B9EC3-L005075](../../agents/web_agent.py#L5075) | 5075 | `"        single_source_listing = listing_request and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L005076](../../agents/web_agent.py#L5076) | 5076 | `"        task_specific_partial_evidence = ("` | — |
| [SRC-1AE03B9EC3-L005077](../../agents/web_agent.py#L5077) | 5077 | `"            single_source_page_summary"` | — |
| [SRC-1AE03B9EC3-L005078](../../agents/web_agent.py#L5078) | 5078 | `"            or single_source_navigation"` | — |
| [SRC-1AE03B9EC3-L005079](../../agents/web_agent.py#L5079) | 5079 | `"            or single_source_social"` | — |
| [SRC-1AE03B9EC3-L005080](../../agents/web_agent.py#L5080) | 5080 | `"            or single_source_lead"` | — |
| [SRC-1AE03B9EC3-L005081](../../agents/web_agent.py#L5081) | 5081 | `"            or single_source_listing"` | — |
| [SRC-1AE03B9EC3-L005082](../../agents/web_agent.py#L5082) | 5082 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005083](../../agents/web_agent.py#L5083) | 5083 | `"        needs_corroboration = len(sources) < 2 or len(independent_domains) < 2"` | — |
| [SRC-1AE03B9EC3-L005084](../../agents/web_agent.py#L5084) | 5084 | `"        evidence_repair: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L005085](../../agents/web_agent.py#L5085) | 5085 | `"            \"attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L005086](../../agents/web_agent.py#L5086) | 5086 | `"            \"max_extra_queries\": 1,"` | — |
| [SRC-1AE03B9EC3-L005087](../../agents/web_agent.py#L5087) | 5087 | `"            \"reason\": \"initial_evidence_gate_satisfied\" if not needs_corroboration else \"not_attempted\","` | — |
| [SRC-1AE03B9EC3-L005088](../../agents/web_agent.py#L5088) | 5088 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005089](../../agents/web_agent.py#L5089) | 5089 | `"        if needs_corroboration and not plan.get(\"queries\"):"` | — |
| [SRC-1AE03B9EC3-L005090](../../agents/web_agent.py#L5090) | 5090 | `"            evidence_repair[\"reason\"] = \"no_topic_query_available\""` | — |
| [SRC-1AE03B9EC3-L005091](../../agents/web_agent.py#L5091) | 5091 | `"        elif needs_corroboration:"` | — |
| [SRC-1AE03B9EC3-L005092](../../agents/web_agent.py#L5092) | 5092 | `"            if task_specific_partial_evidence:"` | — |
| [SRC-1AE03B9EC3-L005093](../../agents/web_agent.py#L5093) | 5093 | `"                evidence_repair[\"reason\"] = \"task_specific_partial_evidence\""` | — |
| [SRC-1AE03B9EC3-L005094](../../agents/web_agent.py#L5094) | 5094 | `"            elif plan.get(\"social_focus\"):"` | — |
| [SRC-1AE03B9EC3-L005095](../../agents/web_agent.py#L5095) | 5095 | `"                evidence_repair[\"reason\"] = \"social_search_not_retried\""` | — |
| [SRC-1AE03B9EC3-L005096](../../agents/web_agent.py#L5096) | 5096 | `"            elif plan.get(\"depth\") == \"deep\" or report.get(\"expansion_queries\"):"` | — |
| [SRC-1AE03B9EC3-L005097](../../agents/web_agent.py#L5097) | 5097 | `"                evidence_repair[\"reason\"] = \"deep_research_already_expanded\""` | — |
| [SRC-1AE03B9EC3-L005098](../../agents/web_agent.py#L5098) | 5098 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L005099](../../agents/web_agent.py#L5099) | 5099 | `"                original_queries = ["` | — |
| [SRC-1AE03B9EC3-L005100](../../agents/web_agent.py#L5100) | 5100 | `"                    str(item).strip()"` | — |
| [SRC-1AE03B9EC3-L005101](../../agents/web_agent.py#L5101) | 5101 | `"                    for item in plan.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L005102](../../agents/web_agent.py#L5102) | 5102 | `"                    if isinstance(item, str) and item.strip()"` | — |
| [SRC-1AE03B9EC3-L005103](../../agents/web_agent.py#L5103) | 5103 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L005104](../../agents/web_agent.py#L5104) | 5104 | `"                base_query = ("` | — |
| [SRC-1AE03B9EC3-L005105](../../agents/web_agent.py#L5105) | 5105 | `"                    original_queries[0]"` | — |
| [SRC-1AE03B9EC3-L005106](../../agents/web_agent.py#L5106) | 5106 | `"                    if original_queries"` | — |
| [SRC-1AE03B9EC3-L005107](../../agents/web_agent.py#L5107) | 5107 | `"                    else compact_search_query(working_question)"` | — |
| [SRC-1AE03B9EC3-L005108](../../agents/web_agent.py#L5108) | 5108 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005109](../../agents/web_agent.py#L5109) | 5109 | `"                suffix = ("` | — |
| [SRC-1AE03B9EC3-L005110](../../agents/web_agent.py#L5110) | 5110 | `"                    \"latest official primary source\""` | — |
| [SRC-1AE03B9EC3-L005111](../../agents/web_agent.py#L5111) | 5111 | `"                    if plan.get(\"freshness\") == \"current\""` | — |
| [SRC-1AE03B9EC3-L005112](../../agents/web_agent.py#L5112) | 5112 | `"                    else \"official primary source data\""` | — |
| [SRC-1AE03B9EC3-L005113](../../agents/web_agent.py#L5113) | 5113 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005114](../../agents/web_agent.py#L5114) | 5114 | `"                repair_query = compact_search_query(f\"{base_query} {suffix}\")"` | — |
| [SRC-1AE03B9EC3-L005115](../../agents/web_agent.py#L5115) | 5115 | `"                if not repair_query or not _relevance_query_tokens(repair_query):"` | — |
| [SRC-1AE03B9EC3-L005116](../../agents/web_agent.py#L5116) | 5116 | `"                    evidence_repair[\"reason\"] = \"no_topic_query_available\""` | — |
| [SRC-1AE03B9EC3-L005117](../../agents/web_agent.py#L5117) | 5117 | `"                    repair_query = \"\""` | — |
| [SRC-1AE03B9EC3-L005118](../../agents/web_agent.py#L5118) | 5118 | `"                known_queries = {"` | — |
| [SRC-1AE03B9EC3-L005119](../../agents/web_agent.py#L5119) | 5119 | `"                    _normalize_search_query(item).casefold()"` | — |
| [SRC-1AE03B9EC3-L005120](../../agents/web_agent.py#L5120) | 5120 | `"                    for item in original_queries"` | — |
| [SRC-1AE03B9EC3-L005121](../../agents/web_agent.py#L5121) | 5121 | `"                }"` | — |
| [SRC-1AE03B9EC3-L005122](../../agents/web_agent.py#L5122) | 5122 | `"                if repair_query and _normalize_search_query(repair_query).casefold() in known_queries:"` | — |
| [SRC-1AE03B9EC3-L005123](../../agents/web_agent.py#L5123) | 5123 | `"                    repair_query = compact_search_query("` | — |
| [SRC-1AE03B9EC3-L005124](../../agents/web_agent.py#L5124) | 5124 | `"                        f\"{base_query} independent corroborating evidence\""` | — |
| [SRC-1AE03B9EC3-L005125](../../agents/web_agent.py#L5125) | 5125 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005126](../../agents/web_agent.py#L5126) | 5126 | `"                if repair_query and _relevance_query_tokens(repair_query) and ("` | — |
| [SRC-1AE03B9EC3-L005127](../../agents/web_agent.py#L5127) | 5127 | `"                    _normalize_search_query(repair_query).casefold() not in known_queries"` | — |
| [SRC-1AE03B9EC3-L005128](../../agents/web_agent.py#L5128) | 5128 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L005129](../../agents/web_agent.py#L5129) | 5129 | `"                    initial_source_count = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005130](../../agents/web_agent.py#L5130) | 5130 | `"                    initial_domain_count = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L005131](../../agents/web_agent.py#L5131) | 5131 | `"                    evidence_repair[\"attempted\"] = True"` | — |
| [SRC-1AE03B9EC3-L005132](../../agents/web_agent.py#L5132) | 5132 | `"                    evidence_repair[\"reason\"] = \"thin_or_unrelated_initial_evidence\""` | — |
| [SRC-1AE03B9EC3-L005133](../../agents/web_agent.py#L5133) | 5133 | `"                    evidence_repair[\"query\"] = repair_query"` | — |
| [SRC-1AE03B9EC3-L005134](../../agents/web_agent.py#L5134) | 5134 | `"                    repair_plan = dict(plan)"` | — |
| [SRC-1AE03B9EC3-L005135](../../agents/web_agent.py#L5135) | 5135 | `"                    repair_plan.update({"` | — |
| [SRC-1AE03B9EC3-L005136](../../agents/web_agent.py#L5136) | 5136 | `"                        \"queries\": [repair_query],"` | — |
| [SRC-1AE03B9EC3-L005137](../../agents/web_agent.py#L5137) | 5137 | `"                        \"depth\": \"standard\","` | — |
| [SRC-1AE03B9EC3-L005138](../../agents/web_agent.py#L5138) | 5138 | `"                        \"social_focus\": False,"` | — |
| [SRC-1AE03B9EC3-L005139](../../agents/web_agent.py#L5139) | 5139 | `"                        \"platforms\": [],"` | — |
| [SRC-1AE03B9EC3-L005140](../../agents/web_agent.py#L5140) | 5140 | `"                        \"direct_urls\": [],"` | — |
| [SRC-1AE03B9EC3-L005141](../../agents/web_agent.py#L5141) | 5141 | `"                    })"` | — |
| [SRC-1AE03B9EC3-L005142](../../agents/web_agent.py#L5142) | 5142 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L005143](../../agents/web_agent.py#L5143) | 5143 | `"                        repair_sources, repair_warnings, repair_report = self._collect_research("` | — |
| [SRC-1AE03B9EC3-L005144](../../agents/web_agent.py#L5144) | 5144 | `"                            repair_plan"` | — |
| [SRC-1AE03B9EC3-L005145](../../agents/web_agent.py#L5145) | 5145 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005146](../../agents/web_agent.py#L5146) | 5146 | `"                    except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L005147](../../agents/web_agent.py#L5147) | 5147 | `"                        repair_sources = []"` | — |
| [SRC-1AE03B9EC3-L005148](../../agents/web_agent.py#L5148) | 5148 | `"                        repair_warnings = []"` | — |
| [SRC-1AE03B9EC3-L005149](../../agents/web_agent.py#L5149) | 5149 | `"                        repair_report = {"` | — |
| [SRC-1AE03B9EC3-L005150](../../agents/web_agent.py#L5150) | 5150 | `"                            \"queries_planned\": 1,"` | — |
| [SRC-1AE03B9EC3-L005151](../../agents/web_agent.py#L5151) | 5151 | `"                            \"queries_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L005152](../../agents/web_agent.py#L5152) | 5152 | `"                            \"queries_attempted_known\": False,"` | — |
| [SRC-1AE03B9EC3-L005153](../../agents/web_agent.py#L5153) | 5153 | `"                            \"search_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L005154](../../agents/web_agent.py#L5154) | 5154 | `"                            \"search_outcome\": \"unknown_after_research_error\","` | — |
| [SRC-1AE03B9EC3-L005155](../../agents/web_agent.py#L5155) | 5155 | `"                            \"usable_sources_after_filtering\": None,"` | — |
| [SRC-1AE03B9EC3-L005156](../../agents/web_agent.py#L5156) | 5156 | `"                        }"` | — |
| [SRC-1AE03B9EC3-L005157](../../agents/web_agent.py#L5157) | 5157 | `"                        search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005158](../../agents/web_agent.py#L5158) | 5158 | `"                            \"تعذر تنفيذ محاولة البحث الإضافية المحدودة (\""` | — |
| [SRC-1AE03B9EC3-L005159](../../agents/web_agent.py#L5159) | 5159 | `"                            + type(exc).__name__ + \").\""` | — |
| [SRC-1AE03B9EC3-L005160](../../agents/web_agent.py#L5160) | 5160 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005161](../../agents/web_agent.py#L5161) | 5161 | `"                    search_warnings.extend(repair_warnings)"` | — |
| [SRC-1AE03B9EC3-L005162](../../agents/web_agent.py#L5162) | 5162 | `"                    evidence_repair[\"attempted_query_count\"] = 1"` | — |
| [SRC-1AE03B9EC3-L005163](../../agents/web_agent.py#L5163) | 5163 | `"                    evidence_repair[\"initial_source_count\"] = initial_source_count"` | — |
| [SRC-1AE03B9EC3-L005164](../../agents/web_agent.py#L5164) | 5164 | `"                    evidence_repair[\"initial_independent_domain_count\"] = initial_domain_count"` | — |
| [SRC-1AE03B9EC3-L005165](../../agents/web_agent.py#L5165) | 5165 | `"                    evidence_repair[\"new_sources_added\"] = 0"` | — |
| [SRC-1AE03B9EC3-L005166](../../agents/web_agent.py#L5166) | 5166 | `"                    source_indexes: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L005167](../../agents/web_agent.py#L5167) | 5167 | `"                    for source_index, source in enumerate(sources):"` | — |
| [SRC-1AE03B9EC3-L005168](../../agents/web_agent.py#L5168) | 5168 | `"                        source_key = self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L005169](../../agents/web_agent.py#L5169) | 5169 | `"                        if source_key:"` | — |
| [SRC-1AE03B9EC3-L005170](../../agents/web_agent.py#L5170) | 5170 | `"                            source_indexes.setdefault(source_key, source_index)"` | — |
| [SRC-1AE03B9EC3-L005171](../../agents/web_agent.py#L5171) | 5171 | `"                    relevant_queries = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L005172](../../agents/web_agent.py#L5172) | 5172 | `"                        query"` | — |
| [SRC-1AE03B9EC3-L005173](../../agents/web_agent.py#L5173) | 5173 | `"                        for query in ("` | — |
| [SRC-1AE03B9EC3-L005174](../../agents/web_agent.py#L5174) | 5174 | `"                            compact_search_query(working_question),"` | — |
| [SRC-1AE03B9EC3-L005175](../../agents/web_agent.py#L5175) | 5175 | `"                            *("` | — |
| [SRC-1AE03B9EC3-L005176](../../agents/web_agent.py#L5176) | 5176 | `"                                compact_search_query(candidate)"` | — |
| [SRC-1AE03B9EC3-L005177](../../agents/web_agent.py#L5177) | 5177 | `"                                for candidate in original_queries"` | — |
| [SRC-1AE03B9EC3-L005178](../../agents/web_agent.py#L5178) | 5178 | `"                                if isinstance(candidate, str)"` | — |
| [SRC-1AE03B9EC3-L005179](../../agents/web_agent.py#L5179) | 5179 | `"                            ),"` | — |
| [SRC-1AE03B9EC3-L005180](../../agents/web_agent.py#L5180) | 5180 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005181](../../agents/web_agent.py#L5181) | 5181 | `"                        if query"` | — |
| [SRC-1AE03B9EC3-L005182](../../agents/web_agent.py#L5182) | 5182 | `"                    ))"` | — |
| [SRC-1AE03B9EC3-L005183](../../agents/web_agent.py#L5183) | 5183 | `"                    for source in repair_sources:"` | — |
| [SRC-1AE03B9EC3-L005184](../../agents/web_agent.py#L5184) | 5184 | `"                        if not isinstance(source, dict):"` | — |
| [SRC-1AE03B9EC3-L005185](../../agents/web_agent.py#L5185) | 5185 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L005186](../../agents/web_agent.py#L5186) | 5186 | `"                        if not any("` | — |
| [SRC-1AE03B9EC3-L005187](../../agents/web_agent.py#L5187) | 5187 | `"                            self._source_matches_query(candidate, source)"` | — |
| [SRC-1AE03B9EC3-L005188](../../agents/web_agent.py#L5188) | 5188 | `"                            for candidate in relevant_queries if candidate"` | — |
| [SRC-1AE03B9EC3-L005189](../../agents/web_agent.py#L5189) | 5189 | `"                        ):"` | — |
| [SRC-1AE03B9EC3-L005190](../../agents/web_agent.py#L5190) | 5190 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L005191](../../agents/web_agent.py#L5191) | 5191 | `"                        source_key = self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L005192](../../agents/web_agent.py#L5192) | 5192 | `"                        if not source_key:"` | — |
| [SRC-1AE03B9EC3-L005193](../../agents/web_agent.py#L5193) | 5193 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L005194](../../agents/web_agent.py#L5194) | 5194 | `"                        existing_index = source_indexes.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L005195](../../agents/web_agent.py#L5195) | 5195 | `"                        if existing_index is None:"` | — |
| [SRC-1AE03B9EC3-L005196](../../agents/web_agent.py#L5196) | 5196 | `"                            source_indexes[source_key] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005197](../../agents/web_agent.py#L5197) | 5197 | `"                            sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L005198](../../agents/web_agent.py#L5198) | 5198 | `"                            evidence_repair[\"new_sources_added\"] += 1"` | — |
| [SRC-1AE03B9EC3-L005199](../../agents/web_agent.py#L5199) | 5199 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L005200](../../agents/web_agent.py#L5200) | 5200 | `"                        existing_source = sources[existing_index]"` | — |
| [SRC-1AE03B9EC3-L005201](../../agents/web_agent.py#L5201) | 5201 | `"                        providers = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L005202](../../agents/web_agent.py#L5202) | 5202 | `"                            list(existing_source.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L005203](../../agents/web_agent.py#L5203) | 5203 | `"                            + list(source.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L005204](../../agents/web_agent.py#L5204) | 5204 | `"                        ))"` | — |
| [SRC-1AE03B9EC3-L005205](../../agents/web_agent.py#L5205) | 5205 | `"                        source_queries = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L005206](../../agents/web_agent.py#L5206) | 5206 | `"                            list(existing_source.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L005207](../../agents/web_agent.py#L5207) | 5207 | `"                            + list(source.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L005208](../../agents/web_agent.py#L5208) | 5208 | `"                        ))"` | — |
| [SRC-1AE03B9EC3-L005209](../../agents/web_agent.py#L5209) | 5209 | `"                        if source.get(\"page_fetched\") and not existing_source.get(\"page_fetched\"):"` | — |
| [SRC-1AE03B9EC3-L005210](../../agents/web_agent.py#L5210) | 5210 | `"                            merged_source = dict(existing_source)"` | — |
| [SRC-1AE03B9EC3-L005211](../../agents/web_agent.py#L5211) | 5211 | `"                            merged_source.update(source)"` | — |
| [SRC-1AE03B9EC3-L005212](../../agents/web_agent.py#L5212) | 5212 | `"                            merged_source[\"providers\"] = providers"` | — |
| [SRC-1AE03B9EC3-L005213](../../agents/web_agent.py#L5213) | 5213 | `"                            merged_source[\"queries\"] = source_queries"` | — |
| [SRC-1AE03B9EC3-L005214](../../agents/web_agent.py#L5214) | 5214 | `"                            sources[existing_index] = merged_source"` | — |
| [SRC-1AE03B9EC3-L005215](../../agents/web_agent.py#L5215) | 5215 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L005216](../../agents/web_agent.py#L5216) | 5216 | `"                            existing_source[\"providers\"] = providers"` | — |
| [SRC-1AE03B9EC3-L005217](../../agents/web_agent.py#L5217) | 5217 | `"                            existing_source[\"queries\"] = source_queries"` | — |
| [SRC-1AE03B9EC3-L005218](../../agents/web_agent.py#L5218) | 5218 | `"                    sources.sort("` | — |
| [SRC-1AE03B9EC3-L005219](../../agents/web_agent.py#L5219) | 5219 | `"                        key=lambda item: float(item.get(\"rank_score\", 0) or 0),"` | — |
| [SRC-1AE03B9EC3-L005220](../../agents/web_agent.py#L5220) | 5220 | `"                        reverse=True,"` | — |
| [SRC-1AE03B9EC3-L005221](../../agents/web_agent.py#L5221) | 5221 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005222](../../agents/web_agent.py#L5222) | 5222 | `"                    plan[\"queries\"] = list(dict.fromkeys(original_queries + [repair_query]))"` | — |
| [SRC-1AE03B9EC3-L005223](../../agents/web_agent.py#L5223) | 5223 | `"                    independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L005224](../../agents/web_agent.py#L5224) | 5224 | `"                        registrable_domain("` | — |
| [SRC-1AE03B9EC3-L005225](../../agents/web_agent.py#L5225) | 5225 | `"                            source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L005226](../../agents/web_agent.py#L5226) | 5226 | `"                            or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L005227](../../agents/web_agent.py#L5227) | 5227 | `"                            or \"\""` | — |
| [SRC-1AE03B9EC3-L005228](../../agents/web_agent.py#L5228) | 5228 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005229](../../agents/web_agent.py#L5229) | 5229 | `"                        for source in sources"` | — |
| [SRC-1AE03B9EC3-L005230](../../agents/web_agent.py#L5230) | 5230 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L005231](../../agents/web_agent.py#L5231) | 5231 | `"                    independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L005232](../../agents/web_agent.py#L5232) | 5232 | `"                    needs_corroboration = ("` | — |
| [SRC-1AE03B9EC3-L005233](../../agents/web_agent.py#L5233) | 5233 | `"                        len(sources) < 2 or len(independent_domains) < 2"` | — |
| [SRC-1AE03B9EC3-L005234](../../agents/web_agent.py#L5234) | 5234 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005235](../../agents/web_agent.py#L5235) | 5235 | `"                    evidence_repair.update({"` | — |
| [SRC-1AE03B9EC3-L005236](../../agents/web_agent.py#L5236) | 5236 | `"                        \"final_source_count\": len(sources),"` | — |
| [SRC-1AE03B9EC3-L005237](../../agents/web_agent.py#L5237) | 5237 | `"                        \"final_independent_domain_count\": len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L005238](../../agents/web_agent.py#L5238) | 5238 | `"                        \"recovered\": not needs_corroboration,"` | — |
| [SRC-1AE03B9EC3-L005239](../../agents/web_agent.py#L5239) | 5239 | `"                    })"` | — |
| [SRC-1AE03B9EC3-L005240](../../agents/web_agent.py#L5240) | 5240 | `"                    evidence_repair[\"reason\"] = ("` | — |
| [SRC-1AE03B9EC3-L005241](../../agents/web_agent.py#L5241) | 5241 | `"                        \"single_bounded_retry_still_insufficient\""` | — |
| [SRC-1AE03B9EC3-L005242](../../agents/web_agent.py#L5242) | 5242 | `"                        if needs_corroboration else \"evidence_gate_recovered\""` | — |
| [SRC-1AE03B9EC3-L005243](../../agents/web_agent.py#L5243) | 5243 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005244](../../agents/web_agent.py#L5244) | 5244 | `"                    report[\"queries_planned\"] = int(report.get(\"queries_planned\", 0) or 0) + int("` | — |
| [SRC-1AE03B9EC3-L005245](../../agents/web_agent.py#L5245) | 5245 | `"                        repair_report.get(\"queries_planned\", 1) or 0"` | — |
| [SRC-1AE03B9EC3-L005246](../../agents/web_agent.py#L5246) | 5246 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005247](../../agents/web_agent.py#L5247) | 5247 | `"                    initial_attempt_count = report.get(\"queries_attempted\", 0)"` | — |
| [SRC-1AE03B9EC3-L005248](../../agents/web_agent.py#L5248) | 5248 | `"                    repair_attempt_count = repair_report.get(\"queries_attempted\", 0)"` | — |
| [SRC-1AE03B9EC3-L005249](../../agents/web_agent.py#L5249) | 5249 | `"                    if initial_attempt_count is None or repair_attempt_count is None:"` | — |
| [SRC-1AE03B9EC3-L005250](../../agents/web_agent.py#L5250) | 5250 | `"                        report[\"queries_attempted\"] = None"` | — |
| [SRC-1AE03B9EC3-L005251](../../agents/web_agent.py#L5251) | 5251 | `"                        report[\"queries_attempted_known\"] = False"` | — |
| [SRC-1AE03B9EC3-L005252](../../agents/web_agent.py#L5252) | 5252 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L005253](../../agents/web_agent.py#L5253) | 5253 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L005254](../../agents/web_agent.py#L5254) | 5254 | `"                            report[\"queries_attempted\"] = max(0, int(initial_attempt_count or 0)) + max("` | — |
| [SRC-1AE03B9EC3-L005255](../../agents/web_agent.py#L5255) | 5255 | `"                                0, int(repair_attempt_count or 0)"` | — |
| [SRC-1AE03B9EC3-L005256](../../agents/web_agent.py#L5256) | 5256 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L005257](../../agents/web_agent.py#L5257) | 5257 | `"                            report[\"queries_attempted_known\"] = True"` | — |
| [SRC-1AE03B9EC3-L005258](../../agents/web_agent.py#L5258) | 5258 | `"                        except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L005259](../../agents/web_agent.py#L5259) | 5259 | `"                            report[\"queries_attempted\"] = None"` | — |
| [SRC-1AE03B9EC3-L005260](../../agents/web_agent.py#L5260) | 5260 | `"                            report[\"queries_attempted_known\"] = False"` | — |
| [SRC-1AE03B9EC3-L005261](../../agents/web_agent.py#L5261) | 5261 | `"                    report[\"query_results\"] = list(report.get(\"query_results\", [])) + list("` | — |
| [SRC-1AE03B9EC3-L005262](../../agents/web_agent.py#L5262) | 5262 | `"                        repair_report.get(\"query_results\", [])"` | — |
| [SRC-1AE03B9EC3-L005263](../../agents/web_agent.py#L5263) | 5263 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005264](../../agents/web_agent.py#L5264) | 5264 | `"                    merged_providers = {"` | — |
| [SRC-1AE03B9EC3-L005265](../../agents/web_agent.py#L5265) | 5265 | `"                        provider"` | — |
| [SRC-1AE03B9EC3-L005266](../../agents/web_agent.py#L5266) | 5266 | `"                        for source in sources"` | — |
| [SRC-1AE03B9EC3-L005267](../../agents/web_agent.py#L5267) | 5267 | `"                        for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L005268](../../agents/web_agent.py#L5268) | 5268 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L005269](../../agents/web_agent.py#L5269) | 5269 | `"                    report[\"providers_used\"] = sorted(merged_providers)"` | — |
| [SRC-1AE03B9EC3-L005270](../../agents/web_agent.py#L5270) | 5270 | `"                    report[\"provider_counts\"] = {"` | — |
| [SRC-1AE03B9EC3-L005271](../../agents/web_agent.py#L5271) | 5271 | `"                        provider: sum("` | — |
| [SRC-1AE03B9EC3-L005272](../../agents/web_agent.py#L5272) | 5272 | `"                            provider in source.get(\"providers\", []) for source in sources"` | — |
| [SRC-1AE03B9EC3-L005273](../../agents/web_agent.py#L5273) | 5273 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005274](../../agents/web_agent.py#L5274) | 5274 | `"                        for provider in merged_providers"` | — |
| [SRC-1AE03B9EC3-L005275](../../agents/web_agent.py#L5275) | 5275 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L005276](../../agents/web_agent.py#L5276) | 5276 | `"                    report[\"platform_counts\"] = {"` | — |
| [SRC-1AE03B9EC3-L005277](../../agents/web_agent.py#L5277) | 5277 | `"                        str(source.get(\"platform\", \"web\")): sum("` | — |
| [SRC-1AE03B9EC3-L005278](../../agents/web_agent.py#L5278) | 5278 | `"                            str(other.get(\"platform\", \"web\"))"` | — |
| [SRC-1AE03B9EC3-L005279](../../agents/web_agent.py#L5279) | 5279 | `"                            == str(source.get(\"platform\", \"web\"))"` | — |
| [SRC-1AE03B9EC3-L005280](../../agents/web_agent.py#L5280) | 5280 | `"                            for other in sources"` | — |
| [SRC-1AE03B9EC3-L005281](../../agents/web_agent.py#L5281) | 5281 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005282](../../agents/web_agent.py#L5282) | 5282 | `"                        for source in sources"` | — |
| [SRC-1AE03B9EC3-L005283](../../agents/web_agent.py#L5283) | 5283 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L005284](../../agents/web_agent.py#L5284) | 5284 | `"                    report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005285](../../agents/web_agent.py#L5285) | 5285 | `"                    report[\"pages_fetched\"] = sum("` | — |
| [SRC-1AE03B9EC3-L005286](../../agents/web_agent.py#L5286) | 5286 | `"                        bool(source.get(\"page_fetched\")) for source in sources"` | — |
| [SRC-1AE03B9EC3-L005287](../../agents/web_agent.py#L5287) | 5287 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005288](../../agents/web_agent.py#L5288) | 5288 | `"                    report[\"independent_sources\"] = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L005289](../../agents/web_agent.py#L5289) | 5289 | `"                    report[\"provider_diagnostics\"] = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L005290](../../agents/web_agent.py#L5290) | 5290 | `"                    report[\"evidence_signals\"] = evidence_signal_report("` | — |
| [SRC-1AE03B9EC3-L005291](../../agents/web_agent.py#L5291) | 5291 | `"                        sources, plan.get(\"freshness\", \"any\")"` | — |
| [SRC-1AE03B9EC3-L005292](../../agents/web_agent.py#L5292) | 5292 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005293](../../agents/web_agent.py#L5293) | 5293 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L005294](../../agents/web_agent.py#L5294) | 5294 | `"                    evidence_repair[\"reason\"] = \"repair_query_was_not_distinct\""` | — |
| [SRC-1AE03B9EC3-L005295](../../agents/web_agent.py#L5295) | 5295 | `"        # Re-apply task guardrails after the optional repair query so stale,"` | — |
| [SRC-1AE03B9EC3-L005296](../../agents/web_agent.py#L5296) | 5296 | `"        # non-government, or non-social candidates cannot re-enter the answer."` | — |
| [SRC-1AE03B9EC3-L005297](../../agents/web_agent.py#L5297) | 5297 | `"        pre_final_guardrail_count = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005298](../../agents/web_agent.py#L5298) | 5298 | `"        sources, final_source_guardrails = apply_source_guardrails("` | — |
| [SRC-1AE03B9EC3-L005299](../../agents/web_agent.py#L5299) | 5299 | `"            working_question, clean_mode, plan, sources"` | — |
| [SRC-1AE03B9EC3-L005300](../../agents/web_agent.py#L5300) | 5300 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005301](../../agents/web_agent.py#L5301) | 5301 | `"        report[\"source_guardrails\"][\"final\"] = final_source_guardrails"` | — |
| [SRC-1AE03B9EC3-L005302](../../agents/web_agent.py#L5302) | 5302 | `"        report[\"source_guardrails\"][\"repair_candidates_before_final_filter\"] = ("` | — |
| [SRC-1AE03B9EC3-L005303](../../agents/web_agent.py#L5303) | 5303 | `"            pre_final_guardrail_count"` | — |
| [SRC-1AE03B9EC3-L005304](../../agents/web_agent.py#L5304) | 5304 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005305](../../agents/web_agent.py#L5305) | 5305 | `"        if final_source_guardrails[\"rejected_sources\"]:"` | — |
| [SRC-1AE03B9EC3-L005306](../../agents/web_agent.py#L5306) | 5306 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005307](../../agents/web_agent.py#L5307) | 5307 | `"                \"أُعيد تطبيق شروط قبول الأدلة بعد محاولة الإصلاح؛ لم تُستخدم النتائج \""` | — |
| [SRC-1AE03B9EC3-L005308](../../agents/web_agent.py#L5308) | 5308 | `"                \"التي أخفقت في شروط الرسمية أو الحداثة أو كونها منشورات اجتماعية.\""` | — |
| [SRC-1AE03B9EC3-L005309](../../agents/web_agent.py#L5309) | 5309 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005310](../../agents/web_agent.py#L5310) | 5310 | `"        if evidence_repair.get(\"attempted\") and \"final_source_count\" in evidence_repair:"` | — |
| [SRC-1AE03B9EC3-L005311](../../agents/web_agent.py#L5311) | 5311 | `"            final_domains = {"` | — |
| [SRC-1AE03B9EC3-L005312](../../agents/web_agent.py#L5312) | 5312 | `"                registrable_domain("` | — |
| [SRC-1AE03B9EC3-L005313](../../agents/web_agent.py#L5313) | 5313 | `"                    source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L005314](../../agents/web_agent.py#L5314) | 5314 | `"                    or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L005315](../../agents/web_agent.py#L5315) | 5315 | `"                    or \"\""` | — |
| [SRC-1AE03B9EC3-L005316](../../agents/web_agent.py#L5316) | 5316 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005317](../../agents/web_agent.py#L5317) | 5317 | `"                for source in sources"` | — |
| [SRC-1AE03B9EC3-L005318](../../agents/web_agent.py#L5318) | 5318 | `"            }"` | — |
| [SRC-1AE03B9EC3-L005319](../../agents/web_agent.py#L5319) | 5319 | `"            final_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L005320](../../agents/web_agent.py#L5320) | 5320 | `"            evidence_repair[\"final_source_count\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005321](../../agents/web_agent.py#L5321) | 5321 | `"            evidence_repair[\"final_independent_domain_count\"] = len(final_domains)"` | — |
| [SRC-1AE03B9EC3-L005322](../../agents/web_agent.py#L5322) | 5322 | `"            evidence_repair[\"recovered\"] = ("` | — |
| [SRC-1AE03B9EC3-L005323](../../agents/web_agent.py#L5323) | 5323 | `"                len(sources) >= 2 and len(final_domains) >= 2"` | — |
| [SRC-1AE03B9EC3-L005324](../../agents/web_agent.py#L5324) | 5324 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005325](../../agents/web_agent.py#L5325) | 5325 | `"            evidence_repair[\"new_sources_added\"] = max("` | — |
| [SRC-1AE03B9EC3-L005326](../../agents/web_agent.py#L5326) | 5326 | `"                0,"` | — |
| [SRC-1AE03B9EC3-L005327](../../agents/web_agent.py#L5327) | 5327 | `"                len(sources) - int("` | — |
| [SRC-1AE03B9EC3-L005328](../../agents/web_agent.py#L5328) | 5328 | `"                    report[\"source_guardrails\"].get(\"initial_eligible_source_count\", 0)"` | — |
| [SRC-1AE03B9EC3-L005329](../../agents/web_agent.py#L5329) | 5329 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005330](../../agents/web_agent.py#L5330) | 5330 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005331](../../agents/web_agent.py#L5331) | 5331 | `"        final_independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L005332](../../agents/web_agent.py#L5332) | 5332 | `"            registrable_domain("` | — |
| [SRC-1AE03B9EC3-L005333](../../agents/web_agent.py#L5333) | 5333 | `"                source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L005334](../../agents/web_agent.py#L5334) | 5334 | `"                or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L005335](../../agents/web_agent.py#L5335) | 5335 | `"                or \"\""` | — |
| [SRC-1AE03B9EC3-L005336](../../agents/web_agent.py#L5336) | 5336 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005337](../../agents/web_agent.py#L5337) | 5337 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L005338](../../agents/web_agent.py#L5338) | 5338 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005339](../../agents/web_agent.py#L5339) | 5339 | `"        final_independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L005340](../../agents/web_agent.py#L5340) | 5340 | `"        # All post-filter source metrics describe the sources that remain eligible"` | — |
| [SRC-1AE03B9EC3-L005341](../../agents/web_agent.py#L5341) | 5341 | `"        # for the answer. Connector-level received/accepted/rejected totals remain"` | — |
| [SRC-1AE03B9EC3-L005342](../../agents/web_agent.py#L5342) | 5342 | `"        # available in provider diagnostics and are intentionally separate."` | — |
| [SRC-1AE03B9EC3-L005343](../../agents/web_agent.py#L5343) | 5343 | `"        independent_domains = final_independent_domains"` | — |
| [SRC-1AE03B9EC3-L005344](../../agents/web_agent.py#L5344) | 5344 | `"        report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005345](../../agents/web_agent.py#L5345) | 5345 | `"        report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L005346](../../agents/web_agent.py#L5346) | 5346 | `"        report[\"distinct_registrable_domains\"] = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L005347](../../agents/web_agent.py#L5347) | 5347 | `"        report[\"independent_sources\"] = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L005348](../../agents/web_agent.py#L5348) | 5348 | `"        report[\"providers_used\"] = sorted({"` | — |
| [SRC-1AE03B9EC3-L005349](../../agents/web_agent.py#L5349) | 5349 | `"            str(provider)"` | — |
| [SRC-1AE03B9EC3-L005350](../../agents/web_agent.py#L5350) | 5350 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L005351](../../agents/web_agent.py#L5351) | 5351 | `"            for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L005352](../../agents/web_agent.py#L5352) | 5352 | `"            if provider"` | — |
| [SRC-1AE03B9EC3-L005353](../../agents/web_agent.py#L5353) | 5353 | `"        })"` | — |
| [SRC-1AE03B9EC3-L005354](../../agents/web_agent.py#L5354) | 5354 | `"        report[\"provider_counts\"] = {"` | — |
| [SRC-1AE03B9EC3-L005355](../../agents/web_agent.py#L5355) | 5355 | `"            provider: sum(provider in source.get(\"providers\", []) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L005356](../../agents/web_agent.py#L5356) | 5356 | `"            for provider in report[\"providers_used\"]"` | — |
| [SRC-1AE03B9EC3-L005357](../../agents/web_agent.py#L5357) | 5357 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005358](../../agents/web_agent.py#L5358) | 5358 | `"        report[\"platform_counts\"] = {"` | — |
| [SRC-1AE03B9EC3-L005359](../../agents/web_agent.py#L5359) | 5359 | `"            str(source.get(\"platform\", \"web\")): sum("` | — |
| [SRC-1AE03B9EC3-L005360](../../agents/web_agent.py#L5360) | 5360 | `"                str(other.get(\"platform\", \"web\")) == str(source.get(\"platform\", \"web\"))"` | — |
| [SRC-1AE03B9EC3-L005361](../../agents/web_agent.py#L5361) | 5361 | `"                for other in sources"` | — |
| [SRC-1AE03B9EC3-L005362](../../agents/web_agent.py#L5362) | 5362 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005363](../../agents/web_agent.py#L5363) | 5363 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L005364](../../agents/web_agent.py#L5364) | 5364 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005365](../../agents/web_agent.py#L5365) | 5365 | `"        report[\"evidence_signals\"] = evidence_signal_report("` | — |
| [SRC-1AE03B9EC3-L005366](../../agents/web_agent.py#L5366) | 5366 | `"            sources, plan.get(\"freshness\", \"any\")"` | — |
| [SRC-1AE03B9EC3-L005367](../../agents/web_agent.py#L5367) | 5367 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005368](../../agents/web_agent.py#L5368) | 5368 | `"        needs_corroboration = ("` | — |
| [SRC-1AE03B9EC3-L005369](../../agents/web_agent.py#L5369) | 5369 | `"            len(sources) < 2 or len(independent_domains) < 2"` | — |
| [SRC-1AE03B9EC3-L005370](../../agents/web_agent.py#L5370) | 5370 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005371](../../agents/web_agent.py#L5371) | 5371 | `"        report[\"evidence_repair\"] = evidence_repair"` | — |
| [SRC-1AE03B9EC3-L005372](../../agents/web_agent.py#L5372) | 5372 | `"        baseline_diagnostic_ids = {id(item) for item in research_diagnostic_baseline}"` | — |
| [SRC-1AE03B9EC3-L005373](../../agents/web_agent.py#L5373) | 5373 | `"        with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L005374](../../agents/web_agent.py#L5374) | 5374 | `"            current_research_diagnostics = ["` | — |
| [SRC-1AE03B9EC3-L005375](../../agents/web_agent.py#L5375) | 5375 | `"                item for item in self._provider_diagnostics"` | — |
| [SRC-1AE03B9EC3-L005376](../../agents/web_agent.py#L5376) | 5376 | `"                if id(item) not in baseline_diagnostic_ids"` | — |
| [SRC-1AE03B9EC3-L005377](../../agents/web_agent.py#L5377) | 5377 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L005378](../../agents/web_agent.py#L5378) | 5378 | `"        report[\"provider_diagnostics\"] = current_research_diagnostics"` | — |
| [SRC-1AE03B9EC3-L005379](../../agents/web_agent.py#L5379) | 5379 | `"        provider_attempt_observed = any("` | — |
| [SRC-1AE03B9EC3-L005380](../../agents/web_agent.py#L5380) | 5380 | `"            item.get(\"status\") in _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES"` | — |
| [SRC-1AE03B9EC3-L005381](../../agents/web_agent.py#L5381) | 5381 | `"            for item in current_research_diagnostics"` | — |
| [SRC-1AE03B9EC3-L005382](../../agents/web_agent.py#L5382) | 5382 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005383](../../agents/web_agent.py#L5383) | 5383 | `"        raw_attempt_count = report.get(\"queries_attempted\", 0)"` | — |
| [SRC-1AE03B9EC3-L005384](../../agents/web_agent.py#L5384) | 5384 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L005385](../../agents/web_agent.py#L5385) | 5385 | `"            queries_attempted = ("` | — |
| [SRC-1AE03B9EC3-L005386](../../agents/web_agent.py#L5386) | 5386 | `"                None if raw_attempt_count is None"` | — |
| [SRC-1AE03B9EC3-L005387](../../agents/web_agent.py#L5387) | 5387 | `"                else max(0, int(raw_attempt_count or 0))"` | — |
| [SRC-1AE03B9EC3-L005388](../../agents/web_agent.py#L5388) | 5388 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005389](../../agents/web_agent.py#L5389) | 5389 | `"        except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L005390](../../agents/web_agent.py#L5390) | 5390 | `"            queries_attempted = None"` | — |
| [SRC-1AE03B9EC3-L005391](../../agents/web_agent.py#L5391) | 5391 | `"        if queries_attempted is not None:"` | — |
| [SRC-1AE03B9EC3-L005392](../../agents/web_agent.py#L5392) | 5392 | `"            search_attempted = ("` | — |
| [SRC-1AE03B9EC3-L005393](../../agents/web_agent.py#L5393) | 5393 | `"                queries_attempted > 0"` | — |
| [SRC-1AE03B9EC3-L005394](../../agents/web_agent.py#L5394) | 5394 | `"                or provider_attempt_observed"` | — |
| [SRC-1AE03B9EC3-L005395](../../agents/web_agent.py#L5395) | 5395 | `"                or report.get(\"search_attempted\") is True"` | — |
| [SRC-1AE03B9EC3-L005396](../../agents/web_agent.py#L5396) | 5396 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005397](../../agents/web_agent.py#L5397) | 5397 | `"        elif provider_attempt_observed or report.get(\"search_attempted\") is True:"` | — |
| [SRC-1AE03B9EC3-L005398](../../agents/web_agent.py#L5398) | 5398 | `"            search_attempted = True"` | — |
| [SRC-1AE03B9EC3-L005399](../../agents/web_agent.py#L5399) | 5399 | `"        elif isinstance(report.get(\"search_attempted\"), bool):"` | — |
| [SRC-1AE03B9EC3-L005400](../../agents/web_agent.py#L5400) | 5400 | `"            search_attempted = report[\"search_attempted\"]"` | — |
| [SRC-1AE03B9EC3-L005401](../../agents/web_agent.py#L5401) | 5401 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L005402](../../agents/web_agent.py#L5402) | 5402 | `"            search_attempted = None"` | — |
| [SRC-1AE03B9EC3-L005403](../../agents/web_agent.py#L5403) | 5403 | `"        report[\"queries_attempted\"] = queries_attempted"` | — |
| [SRC-1AE03B9EC3-L005404](../../agents/web_agent.py#L5404) | 5404 | `"        report[\"queries_attempted_known\"] = queries_attempted is not None"` | — |
| [SRC-1AE03B9EC3-L005405](../../agents/web_agent.py#L5405) | 5405 | `"        report[\"search_attempted\"] = search_attempted"` | — |
| [SRC-1AE03B9EC3-L005406](../../agents/web_agent.py#L5406) | 5406 | `"        previous_search_outcome = report.get(\"search_outcome\")"` | — |
| [SRC-1AE03B9EC3-L005407](../../agents/web_agent.py#L5407) | 5407 | `"        if previous_search_outcome in _RESEARCH_ERROR_OUTCOMES and not sources:"` | — |
| [SRC-1AE03B9EC3-L005408](../../agents/web_agent.py#L5408) | 5408 | `"            if provider_attempt_observed or search_attempted is True:"` | — |
| [SRC-1AE03B9EC3-L005409](../../agents/web_agent.py#L5409) | 5409 | `"                search_outcome = \"attempted_research_error\""` | — |
| [SRC-1AE03B9EC3-L005410](../../agents/web_agent.py#L5410) | 5410 | `"            elif search_attempted is False:"` | — |
| [SRC-1AE03B9EC3-L005411](../../agents/web_agent.py#L5411) | 5411 | `"                search_outcome = \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L005412](../../agents/web_agent.py#L5412) | 5412 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L005413](../../agents/web_agent.py#L5413) | 5413 | `"                search_outcome = \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L005414](../../agents/web_agent.py#L5414) | 5414 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L005415](../../agents/web_agent.py#L5415) | 5415 | `"            search_outcome = ("` | — |
| [SRC-1AE03B9EC3-L005416](../../agents/web_agent.py#L5416) | 5416 | `"                \"attempted_with_usable_sources\" if search_attempted is True and sources"` | — |
| [SRC-1AE03B9EC3-L005417](../../agents/web_agent.py#L5417) | 5417 | `"                else \"attempted_no_usable_sources\" if search_attempted is True"` | — |
| [SRC-1AE03B9EC3-L005418](../../agents/web_agent.py#L5418) | 5418 | `"                else \"not_attempted\" if search_attempted is False"` | — |
| [SRC-1AE03B9EC3-L005419](../../agents/web_agent.py#L5419) | 5419 | `"                else \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L005420](../../agents/web_agent.py#L5420) | 5420 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005421](../../agents/web_agent.py#L5421) | 5421 | `"        report[\"search_outcome\"] = search_outcome"` | — |
| [SRC-1AE03B9EC3-L005422](../../agents/web_agent.py#L5422) | 5422 | `"        if search_outcome in _RESEARCH_ERROR_OUTCOMES:"` | — |
| [SRC-1AE03B9EC3-L005423](../../agents/web_agent.py#L5423) | 5423 | `"            report[\"usable_sources_after_filtering\"] = None"` | — |
| [SRC-1AE03B9EC3-L005424](../../agents/web_agent.py#L5424) | 5424 | `"            report[\"unique_sources\"] = None"` | — |
| [SRC-1AE03B9EC3-L005425](../../agents/web_agent.py#L5425) | 5425 | `"            report[\"pages_fetched\"] = None"` | — |
| [SRC-1AE03B9EC3-L005426](../../agents/web_agent.py#L5426) | 5426 | `"            report[\"provider_counts\"] = None"` | — |
| [SRC-1AE03B9EC3-L005427](../../agents/web_agent.py#L5427) | 5427 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L005428](../../agents/web_agent.py#L5428) | 5428 | `"            report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005429](../../agents/web_agent.py#L5429) | 5429 | `"            if report.get(\"unique_sources\") is None and sources:"` | — |
| [SRC-1AE03B9EC3-L005430](../../agents/web_agent.py#L5430) | 5430 | `"                report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005431](../../agents/web_agent.py#L5431) | 5431 | `"            if report.get(\"pages_fetched\") is None and sources:"` | — |
| [SRC-1AE03B9EC3-L005432](../../agents/web_agent.py#L5432) | 5432 | `"                report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L005433](../../agents/web_agent.py#L5433) | 5433 | `"        report[\"research_quality_semantics\"] = \"process_coverage_not_factual_probability\""` | — |
| [SRC-1AE03B9EC3-L005434](../../agents/web_agent.py#L5434) | 5434 | `"        report[\"distinct_registrable_domains\"] = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L005435](../../agents/web_agent.py#L5435) | 5435 | `"        report[\"independent_sources\"] = len(independent_domains)  # Legacy alias; not editorial independence."` | — |
| [SRC-1AE03B9EC3-L005436](../../agents/web_agent.py#L5436) | 5436 | `"        report[\"independent_sources_field_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L005437](../../agents/web_agent.py#L5437) | 5437 | `"            \"legacy_compatibility_alias_for_distinct_registrable_domain_count\""` | — |
| [SRC-1AE03B9EC3-L005438](../../agents/web_agent.py#L5438) | 5438 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005439](../../agents/web_agent.py#L5439) | 5439 | `"        report[\"source_diversity_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L005440](../../agents/web_agent.py#L5440) | 5440 | `"            \"distinct_registrable_domains_not_editorial_independence\""` | — |
| [SRC-1AE03B9EC3-L005441](../../agents/web_agent.py#L5441) | 5441 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005442](../../agents/web_agent.py#L5442) | 5442 | `"        report[\"editorial_independence_status\"] = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L005443](../../agents/web_agent.py#L5443) | 5443 | `"        if len(independent_domains) >= 2:"` | — |
| [SRC-1AE03B9EC3-L005444](../../agents/web_agent.py#L5444) | 5444 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005445](../../agents/web_agent.py#L5445) | 5445 | `"                \"تعدد النطاقات المسجلة لا يثبت الاستقلال التحريري؛ قد تنقل المواقع عن المصدر الأصلي نفسه.\""` | — |
| [SRC-1AE03B9EC3-L005446](../../agents/web_agent.py#L5446) | 5446 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005447](../../agents/web_agent.py#L5447) | 5447 | `"        search_warning = \"؛ \".join(dict.fromkeys(search_warnings)) if search_warnings else None"` | — |
| [SRC-1AE03B9EC3-L005448](../../agents/web_agent.py#L5448) | 5448 | `"        if needs_corroboration and single_source_navigation and not single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L005449](../../agents/web_agent.py#L5449) | 5449 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005450](../../agents/web_agent.py#L5450) | 5450 | `"                \"هذه نتيجة مرشحة لطلب العثور على موقع/رابط؛ لم تُثبت رسميتها أو صحتها \""` | — |
| [SRC-1AE03B9EC3-L005451](../../agents/web_agent.py#L5451) | 5451 | `"                \"من مصدر مستقل، لذا راجع الرابط قبل الاعتماد عليه.\""` | — |
| [SRC-1AE03B9EC3-L005452](../../agents/web_agent.py#L5452) | 5452 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005453](../../agents/web_agent.py#L5453) | 5453 | `"        if needs_corroboration and (single_source_social or single_source_lead) and not single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L005454](../../agents/web_agent.py#L5454) | 5454 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005455](../../agents/web_agent.py#L5455) | 5455 | `"                \"هذه إشارات بحث أولية وليست تحققًا مستقلًا من هوية العميل أو نيته؛ \""` | — |
| [SRC-1AE03B9EC3-L005456](../../agents/web_agent.py#L5456) | 5456 | `"                \"راجع المنشور وتاريخه وسياقه قبل التواصل أو اتخاذ قرار.\""` | — |
| [SRC-1AE03B9EC3-L005457](../../agents/web_agent.py#L5457) | 5457 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005458](../../agents/web_agent.py#L5458) | 5458 | `"        if needs_corroboration and single_source_listing and not single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L005459](../../agents/web_agent.py#L5459) | 5459 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005460](../../agents/web_agent.py#L5460) | 5460 | `"                \"هذه إعلانات/قوائم مرشحة فقط. قد تكون منتهية أو غير دقيقة؛ تحقق من السعر \""` | — |
| [SRC-1AE03B9EC3-L005461](../../agents/web_agent.py#L5461) | 5461 | `"                \"والتوافر ومصدر الإعلان واطلب تأكيدًا حديثًا قبل دفع مال أو مشاركة بيانات.\""` | — |
| [SRC-1AE03B9EC3-L005462](../../agents/web_agent.py#L5462) | 5462 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005463](../../agents/web_agent.py#L5463) | 5463 | `"        search_warning = \"؛ \".join(dict.fromkeys(search_warnings)) if search_warnings else None"` | — |
| [SRC-1AE03B9EC3-L005464](../../agents/web_agent.py#L5464) | 5464 | `"        if needs_corroboration and not task_specific_partial_evidence:"` | — |
| [SRC-1AE03B9EC3-L005465](../../agents/web_agent.py#L5465) | 5465 | `"            if search_outcome == \"unknown_after_research_error\":"` | — |
| [SRC-1AE03B9EC3-L005466](../../agents/web_agent.py#L5466) | 5466 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005467](../../agents/web_agent.py#L5467) | 5467 | `"                    \"تعذر إكمال مسار البحث بسبب خطأ، ولا توجد بيانات كافية لتحديد ما إذا \""` | — |
| [SRC-1AE03B9EC3-L005468](../../agents/web_agent.py#L5468) | 5468 | `"                    \"كانت محاولة البحث قد اكتملت أو كم نتيجة جُمعت. لذلك لا أستطيع الجزم \""` | — |
| [SRC-1AE03B9EC3-L005469](../../agents/web_agent.py#L5469) | 5469 | `"                    \"بأن البحث لم يُنفّذ أو أن الإنترنت لم يُعد نتائج. لم أتمكن من تقديم \""` | — |
| [SRC-1AE03B9EC3-L005470](../../agents/web_agent.py#L5470) | 5470 | `"                    \"إجابة مكتملة؛ أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L005471](../../agents/web_agent.py#L5471) | 5471 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005472](../../agents/web_agent.py#L5472) | 5472 | `"            elif search_outcome == \"attempted_research_error\":"` | — |
| [SRC-1AE03B9EC3-L005473](../../agents/web_agent.py#L5473) | 5473 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005474](../../agents/web_agent.py#L5474) | 5474 | `"                    \"توجد قرائن تشغيلية على بدء محاولة بحث، لكن مسار البحث فشل قبل إنتاج \""` | — |
| [SRC-1AE03B9EC3-L005475](../../agents/web_agent.py#L5475) | 5475 | `"                    \"تقرير مكتمل. لا أستطيع تحديد عدد النتائج أو المصادر القابلة للاستخدام، \""` | — |
| [SRC-1AE03B9EC3-L005476](../../agents/web_agent.py#L5476) | 5476 | `"                    \"لذلك لن أخمّن. أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L005477](../../agents/web_agent.py#L5477) | 5477 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005478](../../agents/web_agent.py#L5478) | 5478 | `"            elif search_outcome == \"attempted_no_usable_sources\":"` | — |
| [SRC-1AE03B9EC3-L005479](../../agents/web_agent.py#L5479) | 5479 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005480](../../agents/web_agent.py#L5480) | 5480 | `"                    \"جرت محاولة البحث، لكن لم تتوفر مصادر صالحة وكافية للإجابة بعد تصفية \""` | — |
| [SRC-1AE03B9EC3-L005481](../../agents/web_agent.py#L5481) | 5481 | `"                    \"النتائج. هذا لا يثبت أن جميع المواقع أو الإنترنت غير متاح؛ لن أخمّن \""` | — |
| [SRC-1AE03B9EC3-L005482](../../agents/web_agent.py#L5482) | 5482 | `"                    \"أو أقدّم نتيجة غير مدعومة. جرّب صياغة أدق أو أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L005483](../../agents/web_agent.py#L5483) | 5483 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005484](../../agents/web_agent.py#L5484) | 5484 | `"            elif search_outcome == \"not_attempted\":"` | — |
| [SRC-1AE03B9EC3-L005485](../../agents/web_agent.py#L5485) | 5485 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005486](../../agents/web_agent.py#L5486) | 5486 | `"                    \"لم تبدأ محاولة بحث ويب لهذا الطلب، لذلك لا تتوفر لدي أدلة ويب حالية \""` | — |
| [SRC-1AE03B9EC3-L005487](../../agents/web_agent.py#L5487) | 5487 | `"                    \"كافية للإجابة. لن أقدّم نتيجة غير مدعومة؛ أعد المحاولة أو اطلب بحثًا \""` | — |
| [SRC-1AE03B9EC3-L005488](../../agents/web_agent.py#L5488) | 5488 | `"                    \"صريحًا إذا كان ذلك مناسبًا.\""` | — |
| [SRC-1AE03B9EC3-L005489](../../agents/web_agent.py#L5489) | 5489 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005490](../../agents/web_agent.py#L5490) | 5490 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L005491](../../agents/web_agent.py#L5491) | 5491 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005492](../../agents/web_agent.py#L5492) | 5492 | `"                    \"لم أجد معلومات موثوقة كافية مرتبطة بسؤالك من نطاقين مسجلين مختلفين على الأقل. \""` | — |
| [SRC-1AE03B9EC3-L005493](../../agents/web_agent.py#L5493) | 5493 | `"                    \"اختلاف النطاقات لا يثبت الاستقلال التحريري. لن أخمّن أو أقدّم نتيجة غير مدعومة؛ \""` | — |
| [SRC-1AE03B9EC3-L005494](../../agents/web_agent.py#L5494) | 5494 | `"                    \"جرّب صياغة أدق أو أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L005495](../../agents/web_agent.py#L5495) | 5495 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005496](../../agents/web_agent.py#L5496) | 5496 | `"            public_sources = [{"` | — |
| [SRC-1AE03B9EC3-L005497](../../agents/web_agent.py#L5497) | 5497 | `"                \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L005498](../../agents/web_agent.py#L5498) | 5498 | `"                \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L005499](../../agents/web_agent.py#L5499) | 5499 | `"                \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005500](../../agents/web_agent.py#L5500) | 5500 | `"                \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L005501](../../agents/web_agent.py#L5501) | 5501 | `"                \"page_fetch_status\": source.get(\"page_fetch_status\", \"unknown\"),"` | — |
| [SRC-1AE03B9EC3-L005502](../../agents/web_agent.py#L5502) | 5502 | `"                \"page_fetch_error_class\": source.get(\"page_fetch_error_class\"),"` | — |
| [SRC-1AE03B9EC3-L005503](../../agents/web_agent.py#L5503) | 5503 | `"                \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L005504](../../agents/web_agent.py#L5504) | 5504 | `"                \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L005505](../../agents/web_agent.py#L5505) | 5505 | `"                \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L005506](../../agents/web_agent.py#L5506) | 5506 | `"                \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005507](../../agents/web_agent.py#L5507) | 5507 | `"                \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L005508](../../agents/web_agent.py#L5508) | 5508 | `"                \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005509](../../agents/web_agent.py#L5509) | 5509 | `"                \"opinion_source_classification\": source.get(\"opinion_source_classification\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005510](../../agents/web_agent.py#L5510) | 5510 | `"                \"opinion_classification_basis\": source.get(\"opinion_classification_basis\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005511](../../agents/web_agent.py#L5511) | 5511 | `"                \"opinion_classification_method\": source.get(\"opinion_classification_method\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005512](../../agents/web_agent.py#L5512) | 5512 | `"                \"current_evidence_assessment\": source.get(\"current_evidence_assessment\", {}),"` | — |
| [SRC-1AE03B9EC3-L005513](../../agents/web_agent.py#L5513) | 5513 | `"                \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005514](../../agents/web_agent.py#L5514) | 5514 | `"                \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005515](../../agents/web_agent.py#L5515) | 5515 | `"                \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L005516](../../agents/web_agent.py#L5516) | 5516 | `"                \"lead_qualification\": source.get(\"lead_qualification\"),"` | — |
| [SRC-1AE03B9EC3-L005517](../../agents/web_agent.py#L5517) | 5517 | `"                \"lead_intent_evidence\": source.get(\"lead_intent_evidence\"),"` | — |
| [SRC-1AE03B9EC3-L005518](../../agents/web_agent.py#L5518) | 5518 | `"            } for source in sources]"` | — |
| [SRC-1AE03B9EC3-L005519](../../agents/web_agent.py#L5519) | 5519 | `"            citation_validation = self._citation_validation_metadata("` | — |
| [SRC-1AE03B9EC3-L005520](../../agents/web_agent.py#L5520) | 5520 | `"                reason, 0, [], \"not_run\""` | — |
| [SRC-1AE03B9EC3-L005521](../../agents/web_agent.py#L5521) | 5521 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005522](../../agents/web_agent.py#L5522) | 5522 | `"            citation_validation[\"status\"] = \"not_applicable_no_generated_answer\""` | — |
| [SRC-1AE03B9EC3-L005523](../../agents/web_agent.py#L5523) | 5523 | `"            coverage_targets = self._question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L005524](../../agents/web_agent.py#L5524) | 5524 | `"            answer_coverage = {"` | — |
| [SRC-1AE03B9EC3-L005525](../../agents/web_agent.py#L5525) | 5525 | `"                \"method\": \"explicit_criteria_heuristic\","` | — |
| [SRC-1AE03B9EC3-L005526](../../agents/web_agent.py#L5526) | 5526 | `"                \"targets\": coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L005527](../../agents/web_agent.py#L5527) | 5527 | `"                \"status\": ("` | — |
| [SRC-1AE03B9EC3-L005528](../../agents/web_agent.py#L5528) | 5528 | `"                    \"not_reviewed_insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L005529](../../agents/web_agent.py#L5529) | 5529 | `"                    if coverage_targets else \"no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L005530](../../agents/web_agent.py#L5530) | 5530 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005531](../../agents/web_agent.py#L5531) | 5531 | `"                \"automatically_graded\": False,"` | — |
| [SRC-1AE03B9EC3-L005532](../../agents/web_agent.py#L5532) | 5532 | `"            }"` | — |
| [SRC-1AE03B9EC3-L005533](../../agents/web_agent.py#L5533) | 5533 | `"            answer_integrity = audit_answer_integrity(working_question, reason, sources, coverage_targets)"` | — |
| [SRC-1AE03B9EC3-L005534](../../agents/web_agent.py#L5534) | 5534 | `"            answer_coverage[\"target_checks\"] = answer_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L005535](../../agents/web_agent.py#L5535) | 5535 | `"            answer_coverage[\"potentially_missing_target_count\"] = answer_integrity[\"potentially_missing_target_count\"]"` | — |
| [SRC-1AE03B9EC3-L005536](../../agents/web_agent.py#L5536) | 5536 | `"            answer_coverage[\"source_evidence_gap_count\"] = answer_integrity[\"source_evidence_gap_count\"]"` | — |
| [SRC-1AE03B9EC3-L005537](../../agents/web_agent.py#L5537) | 5537 | `"            answer_coverage[\"lexical_screen_method\"] = \"deterministic_lexical_screen_only_not_semantic_grading\""` | — |
| [SRC-1AE03B9EC3-L005538](../../agents/web_agent.py#L5538) | 5538 | `"            task_fulfillment_status = ("` | — |
| [SRC-1AE03B9EC3-L005539](../../agents/web_agent.py#L5539) | 5539 | `"                \"not_assessed_insufficient_evidence\" if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L005540](../../agents/web_agent.py#L5540) | 5540 | `"                else \"not_machine_assessed_no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L005541](../../agents/web_agent.py#L5541) | 5541 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005542](../../agents/web_agent.py#L5542) | 5542 | `"            answer_coverage[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L005543](../../agents/web_agent.py#L5543) | 5543 | `"            research_failed = search_outcome in _RESEARCH_ERROR_OUTCOMES"` | — |
| [SRC-1AE03B9EC3-L005544](../../agents/web_agent.py#L5544) | 5544 | `"            report.update({"` | — |
| [SRC-1AE03B9EC3-L005545](../../agents/web_agent.py#L5545) | 5545 | `"                # When collection failed, an empty local list is not evidence that"` | — |
| [SRC-1AE03B9EC3-L005546](../../agents/web_agent.py#L5546) | 5546 | `"                # the remote search returned zero sources; preserve unknown counts."` | — |
| [SRC-1AE03B9EC3-L005547](../../agents/web_agent.py#L5547) | 5547 | `"                \"unique_sources\": None if research_failed else len(sources),"` | — |
| [SRC-1AE03B9EC3-L005548](../../agents/web_agent.py#L5548) | 5548 | `"                \"independent_sources\": None if research_failed else len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L005549](../../agents/web_agent.py#L5549) | 5549 | `"                \"distinct_registrable_domains\": None if research_failed else len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L005550](../../agents/web_agent.py#L5550) | 5550 | `"                \"pages_fetched\": ("` | — |
| [SRC-1AE03B9EC3-L005551](../../agents/web_agent.py#L5551) | 5551 | `"                    None if research_failed"` | — |
| [SRC-1AE03B9EC3-L005552](../../agents/web_agent.py#L5552) | 5552 | `"                    else sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L005553](../../agents/web_agent.py#L5553) | 5553 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005554](../../agents/web_agent.py#L5554) | 5554 | `"                \"provider_diagnostics\": current_research_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L005555](../../agents/web_agent.py#L5555) | 5555 | `"                \"insufficient_evidence\": True,"` | — |
| [SRC-1AE03B9EC3-L005556](../../agents/web_agent.py#L5556) | 5556 | `"                \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L005557](../../agents/web_agent.py#L5557) | 5557 | `"                \"citation_check\": citation_validation[\"status\"],"` | — |
| [SRC-1AE03B9EC3-L005558](../../agents/web_agent.py#L5558) | 5558 | `"                \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L005559](../../agents/web_agent.py#L5559) | 5559 | `"                \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L005560](../../agents/web_agent.py#L5560) | 5560 | `"                \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L005561](../../agents/web_agent.py#L5561) | 5561 | `"                \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L005562](../../agents/web_agent.py#L5562) | 5562 | `"                \"connector_summary\": report.get(\"connector_summary\") or self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L005563](../../agents/web_agent.py#L5563) | 5563 | `"                    current_research_diagnostics, sources"` | — |
| [SRC-1AE03B9EC3-L005564](../../agents/web_agent.py#L5564) | 5564 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005565](../../agents/web_agent.py#L5565) | 5565 | `"            })"` | — |
| [SRC-1AE03B9EC3-L005566](../../agents/web_agent.py#L5566) | 5566 | `"            return {"` | — |
| [SRC-1AE03B9EC3-L005567](../../agents/web_agent.py#L5567) | 5567 | `"                \"answer\": reason,"` | — |
| [SRC-1AE03B9EC3-L005568](../../agents/web_agent.py#L5568) | 5568 | `"                \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L005569](../../agents/web_agent.py#L5569) | 5569 | `"                \"search_query\": (plan.get(\"queries\") or [\"\"])[0],"` | — |
| [SRC-1AE03B9EC3-L005570](../../agents/web_agent.py#L5570) | 5570 | `"                \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L005571](../../agents/web_agent.py#L5571) | 5571 | `"                \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L005572](../../agents/web_agent.py#L5572) | 5572 | `"                    \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L005573](../../agents/web_agent.py#L5573) | 5573 | `"                    \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L005574](../../agents/web_agent.py#L5574) | 5574 | `"                    \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L005575](../../agents/web_agent.py#L5575) | 5575 | `"                    \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L005576](../../agents/web_agent.py#L5576) | 5576 | `"                    \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L005577](../../agents/web_agent.py#L5577) | 5577 | `"                    \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L005578](../../agents/web_agent.py#L5578) | 5578 | `"                    \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L005579](../../agents/web_agent.py#L5579) | 5579 | `"                    \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L005580](../../agents/web_agent.py#L5580) | 5580 | `"                    \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L005581](../../agents/web_agent.py#L5581) | 5581 | `"                    \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L005582](../../agents/web_agent.py#L5582) | 5582 | `"                },"` | — |
| [SRC-1AE03B9EC3-L005583](../../agents/web_agent.py#L5583) | 5583 | `"                \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L005584](../../agents/web_agent.py#L5584) | 5584 | `"                \"sources\": public_sources,"` | — |
| [SRC-1AE03B9EC3-L005585](../../agents/web_agent.py#L5585) | 5585 | `"                \"used_language_model\": False,"` | — |
| [SRC-1AE03B9EC3-L005586](../../agents/web_agent.py#L5586) | 5586 | `"                \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L005587](../../agents/web_agent.py#L5587) | 5587 | `"                \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L005588](../../agents/web_agent.py#L5588) | 5588 | `"                \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L005589](../../agents/web_agent.py#L5589) | 5589 | `"                \"warnings\": list(dict.fromkeys(search_warnings + [reason])),"` | — |
| [SRC-1AE03B9EC3-L005590](../../agents/web_agent.py#L5590) | 5590 | `"                \"kind\": \"insufficient_evidence\","` | — |
| [SRC-1AE03B9EC3-L005591](../../agents/web_agent.py#L5591) | 5591 | `"                \"final_answer_status\": \"insufficient_evidence_no_generation\","` | — |
| [SRC-1AE03B9EC3-L005592](../../agents/web_agent.py#L5592) | 5592 | `"                \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L005593](../../agents/web_agent.py#L5593) | 5593 | `"                \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L005594](../../agents/web_agent.py#L5594) | 5594 | `"                \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L005595](../../agents/web_agent.py#L5595) | 5595 | `"                \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L005596](../../agents/web_agent.py#L5596) | 5596 | `"                \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L005597](../../agents/web_agent.py#L5597) | 5597 | `"                \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L005598](../../agents/web_agent.py#L5598) | 5598 | `"                \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L005599](../../agents/web_agent.py#L5599) | 5599 | `"            }"` | — |
| [SRC-1AE03B9EC3-L005600](../../agents/web_agent.py#L5600) | 5600 | `""` | — |
| [SRC-1AE03B9EC3-L005601](../../agents/web_agent.py#L5601) | 5601 | `"        answer = \"\""` | — |
| [SRC-1AE03B9EC3-L005602](../../agents/web_agent.py#L5602) | 5602 | `"        used_llm = False"` | — |
| [SRC-1AE03B9EC3-L005603](../../agents/web_agent.py#L5603) | 5603 | `"        llm_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L005604](../../agents/web_agent.py#L5604) | 5604 | `"        generation_budget_exhausted = False"` | — |
| [SRC-1AE03B9EC3-L005605](../../agents/web_agent.py#L5605) | 5605 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L005606](../../agents/web_agent.py#L5606) | 5606 | `"            answer = self._generate("` | — |
| [SRC-1AE03B9EC3-L005607](../../agents/web_agent.py#L5607) | 5607 | `"                working_question,"` | — |
| [SRC-1AE03B9EC3-L005608](../../agents/web_agent.py#L5608) | 5608 | `"                clean_history,"` | — |
| [SRC-1AE03B9EC3-L005609](../../agents/web_agent.py#L5609) | 5609 | `"                sources,"` | — |
| [SRC-1AE03B9EC3-L005610](../../agents/web_agent.py#L5610) | 5610 | `"                search_warning,"` | — |
| [SRC-1AE03B9EC3-L005611](../../agents/web_agent.py#L5611) | 5611 | `"                research_plan=plan,"` | — |
| [SRC-1AE03B9EC3-L005612](../../agents/web_agent.py#L5612) | 5612 | `"                search_report=report,"` | — |
| [SRC-1AE03B9EC3-L005613](../../agents/web_agent.py#L5613) | 5613 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005614](../../agents/web_agent.py#L5614) | 5614 | `"            used_llm = True"` | — |
| [SRC-1AE03B9EC3-L005615](../../agents/web_agent.py#L5615) | 5615 | `"            if self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L005616](../../agents/web_agent.py#L5616) | 5616 | `"                existing_urls = {item.get(\"url\") for item in sources}"` | — |
| [SRC-1AE03B9EC3-L005617](../../agents/web_agent.py#L5617) | 5617 | `"                relevance_queries = []"` | — |
| [SRC-1AE03B9EC3-L005618](../../agents/web_agent.py#L5618) | 5618 | `"                planned_queries = plan.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L005619](../../agents/web_agent.py#L5619) | 5619 | `"                if not isinstance(planned_queries, list):"` | — |
| [SRC-1AE03B9EC3-L005620](../../agents/web_agent.py#L5620) | 5620 | `"                    planned_queries = []"` | — |
| [SRC-1AE03B9EC3-L005621](../../agents/web_agent.py#L5621) | 5621 | `"                for candidate_query in [working_question, *planned_queries]:"` | — |
| [SRC-1AE03B9EC3-L005622](../../agents/web_agent.py#L5622) | 5622 | `"                    if not isinstance(candidate_query, str):"` | — |
| [SRC-1AE03B9EC3-L005623](../../agents/web_agent.py#L5623) | 5623 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L005624](../../agents/web_agent.py#L5624) | 5624 | `"                    compacted_query = compact_search_query(candidate_query)"` | — |
| [SRC-1AE03B9EC3-L005625](../../agents/web_agent.py#L5625) | 5625 | `"                    if compacted_query and compacted_query not in relevance_queries:"` | — |
| [SRC-1AE03B9EC3-L005626](../../agents/web_agent.py#L5626) | 5626 | `"                        relevance_queries.append(compacted_query)"` | — |
| [SRC-1AE03B9EC3-L005627](../../agents/web_agent.py#L5627) | 5627 | `"                for item in self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L005628](../../agents/web_agent.py#L5628) | 5628 | `"                    source_text = \" \".join(("` | — |
| [SRC-1AE03B9EC3-L005629](../../agents/web_agent.py#L5629) | 5629 | `"                        item.get(\"title\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005630](../../agents/web_agent.py#L5630) | 5630 | `"                        item.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005631](../../agents/web_agent.py#L5631) | 5631 | `"                    ))"` | — |
| [SRC-1AE03B9EC3-L005632](../../agents/web_agent.py#L5632) | 5632 | `"                    if ("` | — |
| [SRC-1AE03B9EC3-L005633](../../agents/web_agent.py#L5633) | 5633 | `"                        relevance_queries"` | — |
| [SRC-1AE03B9EC3-L005634](../../agents/web_agent.py#L5634) | 5634 | `"                        and item[\"url\"] not in existing_urls"` | — |
| [SRC-1AE03B9EC3-L005635](../../agents/web_agent.py#L5635) | 5635 | `"                        and not _blocked_source_url(item[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L005636](../../agents/web_agent.py#L5636) | 5636 | `"                        and any("` | — |
| [SRC-1AE03B9EC3-L005637](../../agents/web_agent.py#L5637) | 5637 | `"                            _relevance_ratio(candidate_query, source_text) >= 0.20"` | — |
| [SRC-1AE03B9EC3-L005638](../../agents/web_agent.py#L5638) | 5638 | `"                            for candidate_query in relevance_queries"` | — |
| [SRC-1AE03B9EC3-L005639](../../agents/web_agent.py#L5639) | 5639 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005640](../../agents/web_agent.py#L5640) | 5640 | `"                    ):"` | — |
| [SRC-1AE03B9EC3-L005641](../../agents/web_agent.py#L5641) | 5641 | `"                        sources.append(item)"` | — |
| [SRC-1AE03B9EC3-L005642](../../agents/web_agent.py#L5642) | 5642 | `"                        existing_urls.add(item[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L005643](../../agents/web_agent.py#L5643) | 5643 | `"                report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005644](../../agents/web_agent.py#L5644) | 5644 | `"                provider_counts = dict(report.get(\"provider_counts\", {}))"` | — |
| [SRC-1AE03B9EC3-L005645](../../agents/web_agent.py#L5645) | 5645 | `"                provider_counts[\"openrouter_web_search\"] = len(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L005646](../../agents/web_agent.py#L5646) | 5646 | `"                report[\"provider_counts\"] = provider_counts"` | — |
| [SRC-1AE03B9EC3-L005647](../../agents/web_agent.py#L5647) | 5647 | `"                providers_used = list(report.get(\"providers_used\", []))"` | — |
| [SRC-1AE03B9EC3-L005648](../../agents/web_agent.py#L5648) | 5648 | `"                if \"openrouter_web_search\" not in providers_used:"` | — |
| [SRC-1AE03B9EC3-L005649](../../agents/web_agent.py#L5649) | 5649 | `"                    providers_used.append(\"openrouter_web_search\")"` | — |
| [SRC-1AE03B9EC3-L005650](../../agents/web_agent.py#L5650) | 5650 | `"                report[\"providers_used\"] = providers_used"` | — |
| [SRC-1AE03B9EC3-L005651](../../agents/web_agent.py#L5651) | 5651 | `"                report[\"evidence_signals\"] = evidence_signal_report("` | — |
| [SRC-1AE03B9EC3-L005652](../../agents/web_agent.py#L5652) | 5652 | `"                    sources, plan.get(\"freshness\", \"any\")"` | — |
| [SRC-1AE03B9EC3-L005653](../../agents/web_agent.py#L5653) | 5653 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005654](../../agents/web_agent.py#L5654) | 5654 | `"        except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L005655](../../agents/web_agent.py#L5655) | 5655 | `"            llm_warning = str(exc)"` | — |
| [SRC-1AE03B9EC3-L005656](../../agents/web_agent.py#L5656) | 5656 | `"            generation_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L005657](../../agents/web_agent.py#L5657) | 5657 | `"            if generation_budget_exhausted:"` | — |
| [SRC-1AE03B9EC3-L005658](../../agents/web_agent.py#L5658) | 5658 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005659](../../agents/web_agent.py#L5659) | 5659 | `"                    \"استُنفدت ميزانية محاولات النماذج قبل اكتمال الإجابة التحليلية. \""` | — |
| [SRC-1AE03B9EC3-L005660](../../agents/web_agent.py#L5660) | 5660 | `"                    \"أعرض مقتطفات المصادر المتاحة فقط، ولا أعتبر المهمة مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L005661](../../agents/web_agent.py#L5661) | 5661 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005662](../../agents/web_agent.py#L5662) | 5662 | `"            elif not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L005663](../../agents/web_agent.py#L5663) | 5663 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005664](../../agents/web_agent.py#L5664) | 5664 | `"                    \"تم البحث، لكن الفهم التوليدي غير مفعّل بعد. اضبط OPENROUTER_API_KEY \""` | — |
| [SRC-1AE03B9EC3-L005665](../../agents/web_agent.py#L5665) | 5665 | `"                    \"في Termux لتفعيل تخطيط البحث والإجابة باللغة الطبيعية.\""` | — |
| [SRC-1AE03B9EC3-L005666](../../agents/web_agent.py#L5666) | 5666 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005667](../../agents/web_agent.py#L5667) | 5667 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L005668](../../agents/web_agent.py#L5668) | 5668 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005669](../../agents/web_agent.py#L5669) | 5669 | `"                    \"اكتمل البحث، لكن تعذر توليد إجابة تحليلية. أعرض لك مقتطفات المصادر \""` | — |
| [SRC-1AE03B9EC3-L005670](../../agents/web_agent.py#L5670) | 5670 | `"                    \"المتاحة بدلًا من اختلاق إجابة.\""` | — |
| [SRC-1AE03B9EC3-L005671](../../agents/web_agent.py#L5671) | 5671 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005672](../../agents/web_agent.py#L5672) | 5672 | `"            answer = _fallback_answer(sources, reason)"` | — |
| [SRC-1AE03B9EC3-L005673](../../agents/web_agent.py#L5673) | 5673 | `""` | — |
| [SRC-1AE03B9EC3-L005674](../../agents/web_agent.py#L5674) | 5674 | `"        coverage_targets = self._question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L005675](../../agents/web_agent.py#L5675) | 5675 | `"        coverage_repair_status = \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L005676](../../agents/web_agent.py#L5676) | 5676 | `"        coverage_repair_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L005677](../../agents/web_agent.py#L5677) | 5677 | `"        review_status = \"not_run\""` | — |
| [SRC-1AE03B9EC3-L005678](../../agents/web_agent.py#L5678) | 5678 | `"        review_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L005679](../../agents/web_agent.py#L5679) | 5679 | `"        review_budget_exhausted = False"` | — |
| [SRC-1AE03B9EC3-L005680](../../agents/web_agent.py#L5680) | 5680 | `"        if used_llm and sources:"` | — |
| [SRC-1AE03B9EC3-L005681](../../agents/web_agent.py#L5681) | 5681 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L005682](../../agents/web_agent.py#L5682) | 5682 | `"                answer = self._review_answer(working_question, answer, sources[:MAX_LLM_CITED_SOURCES])"` | — |
| [SRC-1AE03B9EC3-L005683](../../agents/web_agent.py#L5683) | 5683 | `"                review_status = \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005684](../../agents/web_agent.py#L5684) | 5684 | `"            except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L005685](../../agents/web_agent.py#L5685) | 5685 | `"                review_status = \"model_claim_audit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L005686](../../agents/web_agent.py#L5686) | 5686 | `"                review_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L005687](../../agents/web_agent.py#L5687) | 5687 | `"                review_warning = ("` | — |
| [SRC-1AE03B9EC3-L005688](../../agents/web_agent.py#L5688) | 5688 | `"                    \"استُنفدت ميزانية النماذج قبل اكتمال تدقيق الإجابة؛ لذلك لن أعرض المسودة \""` | — |
| [SRC-1AE03B9EC3-L005689](../../agents/web_agent.py#L5689) | 5689 | `"                    \"بوصفها إجابة مكتملة. أرفقت مقتطفات المصادر المتاحة بدل الاعتماد عليها.\""` | — |
| [SRC-1AE03B9EC3-L005690](../../agents/web_agent.py#L5690) | 5690 | `"                    if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L005691](../../agents/web_agent.py#L5691) | 5691 | `"                    else"` | — |
| [SRC-1AE03B9EC3-L005692](../../agents/web_agent.py#L5692) | 5692 | `"                    \"تعذر تدقيق الادعاءات مقابل نصوص المصادر؛ لذلك لن أتعامل مع المسودة \""` | — |
| [SRC-1AE03B9EC3-L005693](../../agents/web_agent.py#L5693) | 5693 | `"                    \"كإجابة مؤكدة. أرفقت مقتطفات المصادر المتاحة بدل الاعتماد على المسودة.\""` | — |
| [SRC-1AE03B9EC3-L005694](../../agents/web_agent.py#L5694) | 5694 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005695](../../agents/web_agent.py#L5695) | 5695 | `"                answer = _fallback_answer(sources, review_warning)"` | — |
| [SRC-1AE03B9EC3-L005696](../../agents/web_agent.py#L5696) | 5696 | `"        criterion_gap_research: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L005697](../../agents/web_agent.py#L5697) | 5697 | `"            \"attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L005698](../../agents/web_agent.py#L5698) | 5698 | `"            \"status\": \"not_needed\","` | — |
| [SRC-1AE03B9EC3-L005699](../../agents/web_agent.py#L5699) | 5699 | `"            \"targets\": [],"` | — |
| [SRC-1AE03B9EC3-L005700](../../agents/web_agent.py#L5700) | 5700 | `"            \"new_sources_added\": 0,"` | — |
| [SRC-1AE03B9EC3-L005701](../../agents/web_agent.py#L5701) | 5701 | `"            \"evidence_sources_enriched\": 0,"` | — |
| [SRC-1AE03B9EC3-L005702](../../agents/web_agent.py#L5702) | 5702 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005703](../../agents/web_agent.py#L5703) | 5703 | `"        # Close the loop from an answer-stage gap back to the source layer. A criterion"` | — |
| [SRC-1AE03B9EC3-L005704](../../agents/web_agent.py#L5704) | 5704 | `"        # that appears in the draft but has no source signal triggers one bounded query"` | — |
| [SRC-1AE03B9EC3-L005705](../../agents/web_agent.py#L5705) | 5705 | `"        # when the reserved request-budget slot remains available."` | — |
| [SRC-1AE03B9EC3-L005706](../../agents/web_agent.py#L5706) | 5706 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L005707](../../agents/web_agent.py#L5707) | 5707 | `"            coverage_targets"` | — |
| [SRC-1AE03B9EC3-L005708](../../agents/web_agent.py#L5708) | 5708 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005709](../../agents/web_agent.py#L5709) | 5709 | `"            and sources"` | — |
| [SRC-1AE03B9EC3-L005710](../../agents/web_agent.py#L5710) | 5710 | `"            and self.api_key"` | — |
| [SRC-1AE03B9EC3-L005711](../../agents/web_agent.py#L5711) | 5711 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L005712](../../agents/web_agent.py#L5712) | 5712 | `"            presearch_integrity = audit_answer_integrity("` | — |
| [SRC-1AE03B9EC3-L005713](../../agents/web_agent.py#L5713) | 5713 | `"                working_question, answer, sources, coverage_targets"` | — |
| [SRC-1AE03B9EC3-L005714](../../agents/web_agent.py#L5714) | 5714 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005715](../../agents/web_agent.py#L5715) | 5715 | `"            source_gap_targets = ["` | — |
| [SRC-1AE03B9EC3-L005716](../../agents/web_agent.py#L5716) | 5716 | `"                item[\"target\"]"` | — |
| [SRC-1AE03B9EC3-L005717](../../agents/web_agent.py#L5717) | 5717 | `"                for item in presearch_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L005718](../../agents/web_agent.py#L5718) | 5718 | `"                if item.get(\"source_evidence_status\") == \"no_source_lexical_signal\""` | — |
| [SRC-1AE03B9EC3-L005719](../../agents/web_agent.py#L5719) | 5719 | `"            ][:3]"` | — |
| [SRC-1AE03B9EC3-L005720](../../agents/web_agent.py#L5720) | 5720 | `"            if source_gap_targets:"` | — |
| [SRC-1AE03B9EC3-L005721](../../agents/web_agent.py#L5721) | 5721 | `"                criterion_gap_research[\"targets\"] = source_gap_targets"` | — |
| [SRC-1AE03B9EC3-L005722](../../agents/web_agent.py#L5722) | 5722 | `"                budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L005723](../../agents/web_agent.py#L5723) | 5723 | `"                if not plan.get(\"coverage_gap_repair_slot_reserved\"):"` | — |
| [SRC-1AE03B9EC3-L005724](../../agents/web_agent.py#L5724) | 5724 | `"                    criterion_gap_research[\"status\"] = \"skipped_no_reserved_search_slot\""` | — |
| [SRC-1AE03B9EC3-L005725](../../agents/web_agent.py#L5725) | 5725 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L005726](../../agents/web_agent.py#L5726) | 5726 | `"                        \"رُصدت محاور بلا إشارة لفظية في المصادر، لكن لم تُحجز ميزانية \""` | — |
| [SRC-1AE03B9EC3-L005727](../../agents/web_agent.py#L5727) | 5727 | `"                        \"استعلام إضافي لهذه المهمة؛ لذلك ستظل المحاور غير المحسومة ظاهرة.\""` | — |
| [SRC-1AE03B9EC3-L005728](../../agents/web_agent.py#L5728) | 5728 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005729](../../agents/web_agent.py#L5729) | 5729 | `"                elif budget is None:"` | — |
| [SRC-1AE03B9EC3-L005730](../../agents/web_agent.py#L5730) | 5730 | `"                    criterion_gap_research[\"status\"] = \"skipped_no_request_budget\""` | — |
| [SRC-1AE03B9EC3-L005731](../../agents/web_agent.py#L5731) | 5731 | `"                elif budget.remaining_units(\"search_queries\") < 1:"` | — |
| [SRC-1AE03B9EC3-L005732](../../agents/web_agent.py#L5732) | 5732 | `"                    criterion_gap_research[\"status\"] = \"skipped_search_budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L005733](../../agents/web_agent.py#L5733) | 5733 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L005734](../../agents/web_agent.py#L5734) | 5734 | `"                        \"رُصدت محاور بلا إشارة لفظية في المصادر، لكن ميزانية البحث لم تترك \""` | — |
| [SRC-1AE03B9EC3-L005735](../../agents/web_agent.py#L5735) | 5735 | `"                        \"استعلامًا إضافيًا للتحقق منها؛ لذلك لا تُعدّ الإجابة مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L005736](../../agents/web_agent.py#L5736) | 5736 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005737](../../agents/web_agent.py#L5737) | 5737 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L005738](../../agents/web_agent.py#L5738) | 5738 | `"                    fallback_queries = fallback_plan(working_question, clean_history).get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L005739](../../agents/web_agent.py#L5739) | 5739 | `"                    topic_query = compact_search_query("` | — |
| [SRC-1AE03B9EC3-L005740](../../agents/web_agent.py#L5740) | 5740 | `"                        fallback_queries[0] if fallback_queries else working_question"` | — |
| [SRC-1AE03B9EC3-L005741](../../agents/web_agent.py#L5741) | 5741 | `"                    ) or compact_search_query(working_question)"` | — |
| [SRC-1AE03B9EC3-L005742](../../agents/web_agent.py#L5742) | 5742 | `"                    gap_query = compact_search_query("` | — |
| [SRC-1AE03B9EC3-L005743](../../agents/web_agent.py#L5743) | 5743 | `"                        f\"{topic_query} {' '.join(source_gap_targets)} official specific evidence data\""` | — |
| [SRC-1AE03B9EC3-L005744](../../agents/web_agent.py#L5744) | 5744 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005745](../../agents/web_agent.py#L5745) | 5745 | `"                    known_query_keys = {"` | — |
| [SRC-1AE03B9EC3-L005746](../../agents/web_agent.py#L5746) | 5746 | `"                        _normalize_search_query(item).casefold()"` | — |
| [SRC-1AE03B9EC3-L005747](../../agents/web_agent.py#L5747) | 5747 | `"                        for item in plan.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L005748](../../agents/web_agent.py#L5748) | 5748 | `"                        if isinstance(item, str) and item.strip()"` | — |
| [SRC-1AE03B9EC3-L005749](../../agents/web_agent.py#L5749) | 5749 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L005750](../../agents/web_agent.py#L5750) | 5750 | `"                    if not gap_query or not _relevance_query_tokens(gap_query):"` | — |
| [SRC-1AE03B9EC3-L005751](../../agents/web_agent.py#L5751) | 5751 | `"                        criterion_gap_research[\"status\"] = \"skipped_no_valid_query\""` | — |
| [SRC-1AE03B9EC3-L005752](../../agents/web_agent.py#L5752) | 5752 | `"                    elif _normalize_search_query(gap_query).casefold() in known_query_keys:"` | — |
| [SRC-1AE03B9EC3-L005753](../../agents/web_agent.py#L5753) | 5753 | `"                        criterion_gap_research[\"status\"] = \"skipped_query_not_distinct\""` | — |
| [SRC-1AE03B9EC3-L005754](../../agents/web_agent.py#L5754) | 5754 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L005755](../../agents/web_agent.py#L5755) | 5755 | `"                        criterion_gap_research.update({"` | — |
| [SRC-1AE03B9EC3-L005756](../../agents/web_agent.py#L5756) | 5756 | `"                            \"attempted\": True,"` | — |
| [SRC-1AE03B9EC3-L005757](../../agents/web_agent.py#L5757) | 5757 | `"                            \"status\": \"searching_for_missing_criterion_evidence\","` | — |
| [SRC-1AE03B9EC3-L005758](../../agents/web_agent.py#L5758) | 5758 | `"                            \"query\": gap_query,"` | — |
| [SRC-1AE03B9EC3-L005759](../../agents/web_agent.py#L5759) | 5759 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L005760](../../agents/web_agent.py#L5760) | 5760 | `"                        gap_plan = dict(plan)"` | — |
| [SRC-1AE03B9EC3-L005761](../../agents/web_agent.py#L5761) | 5761 | `"                        gap_plan.update({"` | — |
| [SRC-1AE03B9EC3-L005762](../../agents/web_agent.py#L5762) | 5762 | `"                            \"queries\": [gap_query],"` | — |
| [SRC-1AE03B9EC3-L005763](../../agents/web_agent.py#L5763) | 5763 | `"                            \"query_limit\": 1,"` | — |
| [SRC-1AE03B9EC3-L005764](../../agents/web_agent.py#L5764) | 5764 | `"                            \"depth\": \"standard\","` | — |
| [SRC-1AE03B9EC3-L005765](../../agents/web_agent.py#L5765) | 5765 | `"                            \"social_focus\": False,"` | — |
| [SRC-1AE03B9EC3-L005766](../../agents/web_agent.py#L5766) | 5766 | `"                            \"platforms\": [],"` | — |
| [SRC-1AE03B9EC3-L005767](../../agents/web_agent.py#L5767) | 5767 | `"                            \"direct_urls\": [],"` | — |
| [SRC-1AE03B9EC3-L005768](../../agents/web_agent.py#L5768) | 5768 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L005769](../../agents/web_agent.py#L5769) | 5769 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L005770](../../agents/web_agent.py#L5770) | 5770 | `"                            gap_sources, gap_warnings, gap_report = self._collect_research(gap_plan)"` | — |
| [SRC-1AE03B9EC3-L005771](../../agents/web_agent.py#L5771) | 5771 | `"                        except (RuntimeError, AgentDependencyError, RequestBudgetExceeded, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L005772](../../agents/web_agent.py#L5772) | 5772 | `"                            gap_sources, gap_warnings = [], []"` | — |
| [SRC-1AE03B9EC3-L005773](../../agents/web_agent.py#L5773) | 5773 | `"                            gap_report = {"` | — |
| [SRC-1AE03B9EC3-L005774](../../agents/web_agent.py#L5774) | 5774 | `"                                \"queries_planned\": 1,"` | — |
| [SRC-1AE03B9EC3-L005775](../../agents/web_agent.py#L5775) | 5775 | `"                                \"queries_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L005776](../../agents/web_agent.py#L5776) | 5776 | `"                                \"queries_attempted_known\": False,"` | — |
| [SRC-1AE03B9EC3-L005777](../../agents/web_agent.py#L5777) | 5777 | `"                                \"search_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L005778](../../agents/web_agent.py#L5778) | 5778 | `"                                \"search_outcome\": \"unknown_after_research_error\","` | — |
| [SRC-1AE03B9EC3-L005779](../../agents/web_agent.py#L5779) | 5779 | `"                                \"query_results\": [],"` | — |
| [SRC-1AE03B9EC3-L005780](../../agents/web_agent.py#L5780) | 5780 | `"                            }"` | — |
| [SRC-1AE03B9EC3-L005781](../../agents/web_agent.py#L5781) | 5781 | `"                            criterion_gap_research[\"status\"] = \"search_failed\""` | — |
| [SRC-1AE03B9EC3-L005782](../../agents/web_agent.py#L5782) | 5782 | `"                            criterion_gap_research[\"error_class\"] = type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L005783](../../agents/web_agent.py#L5783) | 5783 | `"                        search_warnings.extend("` | — |
| [SRC-1AE03B9EC3-L005784](../../agents/web_agent.py#L5784) | 5784 | `"                            item for item in gap_warnings if isinstance(item, str)"` | — |
| [SRC-1AE03B9EC3-L005785](../../agents/web_agent.py#L5785) | 5785 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005786](../../agents/web_agent.py#L5786) | 5786 | `"                        source_indexes: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L005787](../../agents/web_agent.py#L5787) | 5787 | `"                        for source_index, source in enumerate(sources):"` | — |
| [SRC-1AE03B9EC3-L005788](../../agents/web_agent.py#L5788) | 5788 | `"                            source_key = self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L005789](../../agents/web_agent.py#L5789) | 5789 | `"                            if source_key:"` | — |
| [SRC-1AE03B9EC3-L005790](../../agents/web_agent.py#L5790) | 5790 | `"                                source_indexes.setdefault(source_key, source_index)"` | — |
| [SRC-1AE03B9EC3-L005791](../../agents/web_agent.py#L5791) | 5791 | `"                        # A criterion-gap search is a second retrieval path, not a"` | — |
| [SRC-1AE03B9EC3-L005792](../../agents/web_agent.py#L5792) | 5792 | `"                        # trusted bypass. Apply the same task-specific source policy before"` | — |
| [SRC-1AE03B9EC3-L005793](../../agents/web_agent.py#L5793) | 5793 | `"                        # merging candidates into the evidence set or regenerating an answer."` | — |
| [SRC-1AE03B9EC3-L005794](../../agents/web_agent.py#L5794) | 5794 | `"                        pre_gap_source_keys = set(source_indexes)"` | — |
| [SRC-1AE03B9EC3-L005795](../../agents/web_agent.py#L5795) | 5795 | `"                        gap_sources_before_guardrails = len(gap_sources)"` | — |
| [SRC-1AE03B9EC3-L005796](../../agents/web_agent.py#L5796) | 5796 | `"                        gap_sources, gap_guardrail_report = apply_source_guardrails("` | — |
| [SRC-1AE03B9EC3-L005797](../../agents/web_agent.py#L5797) | 5797 | `"                            working_question, clean_mode, plan, gap_sources"` | — |
| [SRC-1AE03B9EC3-L005798](../../agents/web_agent.py#L5798) | 5798 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005799](../../agents/web_agent.py#L5799) | 5799 | `"                        report.setdefault(\"source_guardrails\", {})["` | — |
| [SRC-1AE03B9EC3-L005800](../../agents/web_agent.py#L5800) | 5800 | `"                            \"criterion_gap_repair\""` | — |
| [SRC-1AE03B9EC3-L005801](../../agents/web_agent.py#L5801) | 5801 | `"                        ] = {"` | — |
| [SRC-1AE03B9EC3-L005802](../../agents/web_agent.py#L5802) | 5802 | `"                            **gap_guardrail_report,"` | — |
| [SRC-1AE03B9EC3-L005803](../../agents/web_agent.py#L5803) | 5803 | `"                            \"candidates_before_filter\": gap_sources_before_guardrails,"` | — |
| [SRC-1AE03B9EC3-L005804](../../agents/web_agent.py#L5804) | 5804 | `"                        }"` | — |
| [SRC-1AE03B9EC3-L005805](../../agents/web_agent.py#L5805) | 5805 | `"                        if gap_guardrail_report[\"rejected_sources\"]:"` | — |
| [SRC-1AE03B9EC3-L005806](../../agents/web_agent.py#L5806) | 5806 | `"                            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005807](../../agents/web_agent.py#L5807) | 5807 | `"                                \"رُفضت بعض نتائج البحث الإضافي لأنها لم تستوفِ شروط قبول \""` | — |
| [SRC-1AE03B9EC3-L005808](../../agents/web_agent.py#L5808) | 5808 | `"                                \"الأدلة الخاصة بالسؤال.\""` | — |
| [SRC-1AE03B9EC3-L005809](../../agents/web_agent.py#L5809) | 5809 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L005810](../../agents/web_agent.py#L5810) | 5810 | `"                        evidence_updated = False"` | — |
| [SRC-1AE03B9EC3-L005811](../../agents/web_agent.py#L5811) | 5811 | `"                        for candidate in gap_sources:"` | — |
| [SRC-1AE03B9EC3-L005812](../../agents/web_agent.py#L5812) | 5812 | `"                            if not isinstance(candidate, dict):"` | — |
| [SRC-1AE03B9EC3-L005813](../../agents/web_agent.py#L5813) | 5813 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L005814](../../agents/web_agent.py#L5814) | 5814 | `"                            if not self._source_matches_query(gap_query, candidate):"` | — |
| [SRC-1AE03B9EC3-L005815](../../agents/web_agent.py#L5815) | 5815 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L005816](../../agents/web_agent.py#L5816) | 5816 | `"                            source_key = self._normalized_source_url_key(candidate.get(\"url\"))"` | — |
