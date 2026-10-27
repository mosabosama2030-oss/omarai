# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **010**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L004815 إلى SRC-EEF2E6447C-L000146
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L004815](../../agents/web_agent.py#L4815) | 4815 | `"            answer_coverage[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L004816](../../agents/web_agent.py#L4816) | 4816 | `"            research_failed = search_outcome in _RESEARCH_ERROR_OUTCOMES"` | — |
| [SRC-1AE03B9EC3-L004817](../../agents/web_agent.py#L4817) | 4817 | `"            report.update({"` | — |
| [SRC-1AE03B9EC3-L004818](../../agents/web_agent.py#L4818) | 4818 | `"                # When collection failed, an empty local list is not evidence that"` | — |
| [SRC-1AE03B9EC3-L004819](../../agents/web_agent.py#L4819) | 4819 | `"                # the remote search returned zero sources; preserve unknown counts."` | — |
| [SRC-1AE03B9EC3-L004820](../../agents/web_agent.py#L4820) | 4820 | `"                \"unique_sources\": None if research_failed else len(sources),"` | — |
| [SRC-1AE03B9EC3-L004821](../../agents/web_agent.py#L4821) | 4821 | `"                \"independent_sources\": None if research_failed else len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L004822](../../agents/web_agent.py#L4822) | 4822 | `"                \"distinct_registrable_domains\": None if research_failed else len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L004823](../../agents/web_agent.py#L4823) | 4823 | `"                \"pages_fetched\": ("` | — |
| [SRC-1AE03B9EC3-L004824](../../agents/web_agent.py#L4824) | 4824 | `"                    None if research_failed"` | — |
| [SRC-1AE03B9EC3-L004825](../../agents/web_agent.py#L4825) | 4825 | `"                    else sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L004826](../../agents/web_agent.py#L4826) | 4826 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L004827](../../agents/web_agent.py#L4827) | 4827 | `"                \"provider_diagnostics\": current_research_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L004828](../../agents/web_agent.py#L4828) | 4828 | `"                \"insufficient_evidence\": True,"` | — |
| [SRC-1AE03B9EC3-L004829](../../agents/web_agent.py#L4829) | 4829 | `"                \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L004830](../../agents/web_agent.py#L4830) | 4830 | `"                \"citation_check\": citation_validation[\"status\"],"` | — |
| [SRC-1AE03B9EC3-L004831](../../agents/web_agent.py#L4831) | 4831 | `"                \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L004832](../../agents/web_agent.py#L4832) | 4832 | `"                \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L004833](../../agents/web_agent.py#L4833) | 4833 | `"                \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L004834](../../agents/web_agent.py#L4834) | 4834 | `"                \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L004835](../../agents/web_agent.py#L4835) | 4835 | `"                \"connector_summary\": report.get(\"connector_summary\") or self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L004836](../../agents/web_agent.py#L4836) | 4836 | `"                    current_research_diagnostics, sources"` | — |
| [SRC-1AE03B9EC3-L004837](../../agents/web_agent.py#L4837) | 4837 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L004838](../../agents/web_agent.py#L4838) | 4838 | `"            })"` | — |
| [SRC-1AE03B9EC3-L004839](../../agents/web_agent.py#L4839) | 4839 | `"            return {"` | — |
| [SRC-1AE03B9EC3-L004840](../../agents/web_agent.py#L4840) | 4840 | `"                \"answer\": reason,"` | — |
| [SRC-1AE03B9EC3-L004841](../../agents/web_agent.py#L4841) | 4841 | `"                \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L004842](../../agents/web_agent.py#L4842) | 4842 | `"                \"search_query\": (plan.get(\"queries\") or [\"\"])[0],"` | — |
| [SRC-1AE03B9EC3-L004843](../../agents/web_agent.py#L4843) | 4843 | `"                \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L004844](../../agents/web_agent.py#L4844) | 4844 | `"                \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L004845](../../agents/web_agent.py#L4845) | 4845 | `"                    \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L004846](../../agents/web_agent.py#L4846) | 4846 | `"                    \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L004847](../../agents/web_agent.py#L4847) | 4847 | `"                    \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L004848](../../agents/web_agent.py#L4848) | 4848 | `"                    \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L004849](../../agents/web_agent.py#L4849) | 4849 | `"                    \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L004850](../../agents/web_agent.py#L4850) | 4850 | `"                    \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L004851](../../agents/web_agent.py#L4851) | 4851 | `"                    \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L004852](../../agents/web_agent.py#L4852) | 4852 | `"                    \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L004853](../../agents/web_agent.py#L4853) | 4853 | `"                    \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L004854](../../agents/web_agent.py#L4854) | 4854 | `"                },"` | — |
| [SRC-1AE03B9EC3-L004855](../../agents/web_agent.py#L4855) | 4855 | `"                \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L004856](../../agents/web_agent.py#L4856) | 4856 | `"                \"sources\": public_sources,"` | — |
| [SRC-1AE03B9EC3-L004857](../../agents/web_agent.py#L4857) | 4857 | `"                \"used_language_model\": False,"` | — |
| [SRC-1AE03B9EC3-L004858](../../agents/web_agent.py#L4858) | 4858 | `"                \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L004859](../../agents/web_agent.py#L4859) | 4859 | `"                \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L004860](../../agents/web_agent.py#L4860) | 4860 | `"                \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L004861](../../agents/web_agent.py#L4861) | 4861 | `"                \"warnings\": list(dict.fromkeys(search_warnings + [reason])),"` | — |
| [SRC-1AE03B9EC3-L004862](../../agents/web_agent.py#L4862) | 4862 | `"                \"kind\": \"insufficient_evidence\","` | — |
| [SRC-1AE03B9EC3-L004863](../../agents/web_agent.py#L4863) | 4863 | `"                \"final_answer_status\": \"insufficient_evidence_no_generation\","` | — |
| [SRC-1AE03B9EC3-L004864](../../agents/web_agent.py#L4864) | 4864 | `"                \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L004865](../../agents/web_agent.py#L4865) | 4865 | `"                \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L004866](../../agents/web_agent.py#L4866) | 4866 | `"                \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L004867](../../agents/web_agent.py#L4867) | 4867 | `"                \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L004868](../../agents/web_agent.py#L4868) | 4868 | `"                \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L004869](../../agents/web_agent.py#L4869) | 4869 | `"                \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L004870](../../agents/web_agent.py#L4870) | 4870 | `"                \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L004871](../../agents/web_agent.py#L4871) | 4871 | `"            }"` | — |
| [SRC-1AE03B9EC3-L004872](../../agents/web_agent.py#L4872) | 4872 | `""` | — |
| [SRC-1AE03B9EC3-L004873](../../agents/web_agent.py#L4873) | 4873 | `"        answer = \"\""` | — |
| [SRC-1AE03B9EC3-L004874](../../agents/web_agent.py#L4874) | 4874 | `"        used_llm = False"` | — |
| [SRC-1AE03B9EC3-L004875](../../agents/web_agent.py#L4875) | 4875 | `"        llm_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L004876](../../agents/web_agent.py#L4876) | 4876 | `"        generation_budget_exhausted = False"` | — |
| [SRC-1AE03B9EC3-L004877](../../agents/web_agent.py#L4877) | 4877 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L004878](../../agents/web_agent.py#L4878) | 4878 | `"            answer = self._generate("` | — |
| [SRC-1AE03B9EC3-L004879](../../agents/web_agent.py#L4879) | 4879 | `"                question,"` | — |
| [SRC-1AE03B9EC3-L004880](../../agents/web_agent.py#L4880) | 4880 | `"                clean_history,"` | — |
| [SRC-1AE03B9EC3-L004881](../../agents/web_agent.py#L4881) | 4881 | `"                sources,"` | — |
| [SRC-1AE03B9EC3-L004882](../../agents/web_agent.py#L4882) | 4882 | `"                search_warning,"` | — |
| [SRC-1AE03B9EC3-L004883](../../agents/web_agent.py#L4883) | 4883 | `"                research_plan=plan,"` | — |
| [SRC-1AE03B9EC3-L004884](../../agents/web_agent.py#L4884) | 4884 | `"                search_report=report,"` | — |
| [SRC-1AE03B9EC3-L004885](../../agents/web_agent.py#L4885) | 4885 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004886](../../agents/web_agent.py#L4886) | 4886 | `"            used_llm = True"` | — |
| [SRC-1AE03B9EC3-L004887](../../agents/web_agent.py#L4887) | 4887 | `"            if self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L004888](../../agents/web_agent.py#L4888) | 4888 | `"                existing_urls = {item.get(\"url\") for item in sources}"` | — |
| [SRC-1AE03B9EC3-L004889](../../agents/web_agent.py#L4889) | 4889 | `"                relevance_queries = []"` | — |
| [SRC-1AE03B9EC3-L004890](../../agents/web_agent.py#L4890) | 4890 | `"                planned_queries = plan.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L004891](../../agents/web_agent.py#L4891) | 4891 | `"                if not isinstance(planned_queries, list):"` | — |
| [SRC-1AE03B9EC3-L004892](../../agents/web_agent.py#L4892) | 4892 | `"                    planned_queries = []"` | — |
| [SRC-1AE03B9EC3-L004893](../../agents/web_agent.py#L4893) | 4893 | `"                for candidate_query in [question, *planned_queries]:"` | — |
| [SRC-1AE03B9EC3-L004894](../../agents/web_agent.py#L4894) | 4894 | `"                    if not isinstance(candidate_query, str):"` | — |
| [SRC-1AE03B9EC3-L004895](../../agents/web_agent.py#L4895) | 4895 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L004896](../../agents/web_agent.py#L4896) | 4896 | `"                    compacted_query = compact_search_query(candidate_query)"` | — |
| [SRC-1AE03B9EC3-L004897](../../agents/web_agent.py#L4897) | 4897 | `"                    if compacted_query and compacted_query not in relevance_queries:"` | — |
| [SRC-1AE03B9EC3-L004898](../../agents/web_agent.py#L4898) | 4898 | `"                        relevance_queries.append(compacted_query)"` | — |
| [SRC-1AE03B9EC3-L004899](../../agents/web_agent.py#L4899) | 4899 | `"                for item in self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L004900](../../agents/web_agent.py#L4900) | 4900 | `"                    source_text = \" \".join(("` | — |
| [SRC-1AE03B9EC3-L004901](../../agents/web_agent.py#L4901) | 4901 | `"                        item.get(\"title\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004902](../../agents/web_agent.py#L4902) | 4902 | `"                        item.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004903](../../agents/web_agent.py#L4903) | 4903 | `"                    ))"` | — |
| [SRC-1AE03B9EC3-L004904](../../agents/web_agent.py#L4904) | 4904 | `"                    if ("` | — |
| [SRC-1AE03B9EC3-L004905](../../agents/web_agent.py#L4905) | 4905 | `"                        relevance_queries"` | — |
| [SRC-1AE03B9EC3-L004906](../../agents/web_agent.py#L4906) | 4906 | `"                        and item[\"url\"] not in existing_urls"` | — |
| [SRC-1AE03B9EC3-L004907](../../agents/web_agent.py#L4907) | 4907 | `"                        and not _blocked_source_url(item[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L004908](../../agents/web_agent.py#L4908) | 4908 | `"                        and any("` | — |
| [SRC-1AE03B9EC3-L004909](../../agents/web_agent.py#L4909) | 4909 | `"                            _relevance_ratio(candidate_query, source_text) >= 0.20"` | — |
| [SRC-1AE03B9EC3-L004910](../../agents/web_agent.py#L4910) | 4910 | `"                            for candidate_query in relevance_queries"` | — |
| [SRC-1AE03B9EC3-L004911](../../agents/web_agent.py#L4911) | 4911 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004912](../../agents/web_agent.py#L4912) | 4912 | `"                    ):"` | — |
| [SRC-1AE03B9EC3-L004913](../../agents/web_agent.py#L4913) | 4913 | `"                        sources.append(item)"` | — |
| [SRC-1AE03B9EC3-L004914](../../agents/web_agent.py#L4914) | 4914 | `"                        existing_urls.add(item[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L004915](../../agents/web_agent.py#L4915) | 4915 | `"                report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004916](../../agents/web_agent.py#L4916) | 4916 | `"                provider_counts = dict(report.get(\"provider_counts\", {}))"` | — |
| [SRC-1AE03B9EC3-L004917](../../agents/web_agent.py#L4917) | 4917 | `"                provider_counts[\"openrouter_web_search\"] = len(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L004918](../../agents/web_agent.py#L4918) | 4918 | `"                report[\"provider_counts\"] = provider_counts"` | — |
| [SRC-1AE03B9EC3-L004919](../../agents/web_agent.py#L4919) | 4919 | `"                providers_used = list(report.get(\"providers_used\", []))"` | — |
| [SRC-1AE03B9EC3-L004920](../../agents/web_agent.py#L4920) | 4920 | `"                if \"openrouter_web_search\" not in providers_used:"` | — |
| [SRC-1AE03B9EC3-L004921](../../agents/web_agent.py#L4921) | 4921 | `"                    providers_used.append(\"openrouter_web_search\")"` | — |
| [SRC-1AE03B9EC3-L004922](../../agents/web_agent.py#L4922) | 4922 | `"                report[\"providers_used\"] = providers_used"` | — |
| [SRC-1AE03B9EC3-L004923](../../agents/web_agent.py#L4923) | 4923 | `"                report[\"evidence_signals\"] = evidence_signal_report("` | — |
| [SRC-1AE03B9EC3-L004924](../../agents/web_agent.py#L4924) | 4924 | `"                    sources, plan.get(\"freshness\", \"any\")"` | — |
| [SRC-1AE03B9EC3-L004925](../../agents/web_agent.py#L4925) | 4925 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004926](../../agents/web_agent.py#L4926) | 4926 | `"        except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L004927](../../agents/web_agent.py#L4927) | 4927 | `"            llm_warning = str(exc)"` | — |
| [SRC-1AE03B9EC3-L004928](../../agents/web_agent.py#L4928) | 4928 | `"            generation_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L004929](../../agents/web_agent.py#L4929) | 4929 | `"            if generation_budget_exhausted:"` | — |
| [SRC-1AE03B9EC3-L004930](../../agents/web_agent.py#L4930) | 4930 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004931](../../agents/web_agent.py#L4931) | 4931 | `"                    \"استُنفدت ميزانية محاولات النماذج قبل اكتمال الإجابة التحليلية. \""` | — |
| [SRC-1AE03B9EC3-L004932](../../agents/web_agent.py#L4932) | 4932 | `"                    \"أعرض مقتطفات المصادر المتاحة فقط، ولا أعتبر المهمة مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L004933](../../agents/web_agent.py#L4933) | 4933 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004934](../../agents/web_agent.py#L4934) | 4934 | `"            elif not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L004935](../../agents/web_agent.py#L4935) | 4935 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004936](../../agents/web_agent.py#L4936) | 4936 | `"                    \"تم البحث، لكن الفهم التوليدي غير مفعّل بعد. اضبط OPENROUTER_API_KEY \""` | — |
| [SRC-1AE03B9EC3-L004937](../../agents/web_agent.py#L4937) | 4937 | `"                    \"في Termux لتفعيل تخطيط البحث والإجابة باللغة الطبيعية.\""` | — |
| [SRC-1AE03B9EC3-L004938](../../agents/web_agent.py#L4938) | 4938 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004939](../../agents/web_agent.py#L4939) | 4939 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L004940](../../agents/web_agent.py#L4940) | 4940 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004941](../../agents/web_agent.py#L4941) | 4941 | `"                    \"اكتمل البحث، لكن تعذر توليد إجابة تحليلية. أعرض لك مقتطفات المصادر \""` | — |
| [SRC-1AE03B9EC3-L004942](../../agents/web_agent.py#L4942) | 4942 | `"                    \"المتاحة بدلًا من اختلاق إجابة.\""` | — |
| [SRC-1AE03B9EC3-L004943](../../agents/web_agent.py#L4943) | 4943 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004944](../../agents/web_agent.py#L4944) | 4944 | `"            answer = _fallback_answer(sources, reason)"` | — |
| [SRC-1AE03B9EC3-L004945](../../agents/web_agent.py#L4945) | 4945 | `""` | — |
| [SRC-1AE03B9EC3-L004946](../../agents/web_agent.py#L4946) | 4946 | `"        coverage_targets = self._question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L004947](../../agents/web_agent.py#L4947) | 4947 | `"        coverage_repair_status = \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L004948](../../agents/web_agent.py#L4948) | 4948 | `"        coverage_repair_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L004949](../../agents/web_agent.py#L4949) | 4949 | `"        review_status = \"not_run\""` | — |
| [SRC-1AE03B9EC3-L004950](../../agents/web_agent.py#L4950) | 4950 | `"        review_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L004951](../../agents/web_agent.py#L4951) | 4951 | `"        review_budget_exhausted = False"` | — |
| [SRC-1AE03B9EC3-L004952](../../agents/web_agent.py#L4952) | 4952 | `"        if used_llm and sources:"` | — |
| [SRC-1AE03B9EC3-L004953](../../agents/web_agent.py#L4953) | 4953 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L004954](../../agents/web_agent.py#L4954) | 4954 | `"                answer = self._review_answer(question, answer, sources[:MAX_LLM_CITED_SOURCES])"` | — |
| [SRC-1AE03B9EC3-L004955](../../agents/web_agent.py#L4955) | 4955 | `"                review_status = \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L004956](../../agents/web_agent.py#L4956) | 4956 | `"            except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L004957](../../agents/web_agent.py#L4957) | 4957 | `"                review_status = \"model_claim_audit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L004958](../../agents/web_agent.py#L4958) | 4958 | `"                review_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L004959](../../agents/web_agent.py#L4959) | 4959 | `"                review_warning = ("` | — |
| [SRC-1AE03B9EC3-L004960](../../agents/web_agent.py#L4960) | 4960 | `"                    \"استُنفدت ميزانية النماذج قبل اكتمال تدقيق الإجابة؛ لذلك لن أعرض المسودة \""` | — |
| [SRC-1AE03B9EC3-L004961](../../agents/web_agent.py#L4961) | 4961 | `"                    \"بوصفها إجابة مكتملة. أرفقت مقتطفات المصادر المتاحة بدل الاعتماد عليها.\""` | — |
| [SRC-1AE03B9EC3-L004962](../../agents/web_agent.py#L4962) | 4962 | `"                    if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L004963](../../agents/web_agent.py#L4963) | 4963 | `"                    else"` | — |
| [SRC-1AE03B9EC3-L004964](../../agents/web_agent.py#L4964) | 4964 | `"                    \"تعذر تدقيق الادعاءات مقابل نصوص المصادر؛ لذلك لن أتعامل مع المسودة \""` | — |
| [SRC-1AE03B9EC3-L004965](../../agents/web_agent.py#L4965) | 4965 | `"                    \"كإجابة مؤكدة. أرفقت مقتطفات المصادر المتاحة بدل الاعتماد على المسودة.\""` | — |
| [SRC-1AE03B9EC3-L004966](../../agents/web_agent.py#L4966) | 4966 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004967](../../agents/web_agent.py#L4967) | 4967 | `"                answer = _fallback_answer(sources, review_warning)"` | — |
| [SRC-1AE03B9EC3-L004968](../../agents/web_agent.py#L4968) | 4968 | `"        criterion_gap_research: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L004969](../../agents/web_agent.py#L4969) | 4969 | `"            \"attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L004970](../../agents/web_agent.py#L4970) | 4970 | `"            \"status\": \"not_needed\","` | — |
| [SRC-1AE03B9EC3-L004971](../../agents/web_agent.py#L4971) | 4971 | `"            \"targets\": [],"` | — |
| [SRC-1AE03B9EC3-L004972](../../agents/web_agent.py#L4972) | 4972 | `"            \"new_sources_added\": 0,"` | — |
| [SRC-1AE03B9EC3-L004973](../../agents/web_agent.py#L4973) | 4973 | `"            \"evidence_sources_enriched\": 0,"` | — |
| [SRC-1AE03B9EC3-L004974](../../agents/web_agent.py#L4974) | 4974 | `"        }"` | — |
| [SRC-1AE03B9EC3-L004975](../../agents/web_agent.py#L4975) | 4975 | `"        # Close the loop from an answer-stage gap back to the source layer. A criterion"` | — |
| [SRC-1AE03B9EC3-L004976](../../agents/web_agent.py#L4976) | 4976 | `"        # that appears in the draft but has no source signal triggers one bounded query"` | — |
| [SRC-1AE03B9EC3-L004977](../../agents/web_agent.py#L4977) | 4977 | `"        # when the reserved request-budget slot remains available."` | — |
| [SRC-1AE03B9EC3-L004978](../../agents/web_agent.py#L4978) | 4978 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L004979](../../agents/web_agent.py#L4979) | 4979 | `"            coverage_targets"` | — |
| [SRC-1AE03B9EC3-L004980](../../agents/web_agent.py#L4980) | 4980 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L004981](../../agents/web_agent.py#L4981) | 4981 | `"            and sources"` | — |
| [SRC-1AE03B9EC3-L004982](../../agents/web_agent.py#L4982) | 4982 | `"            and self.api_key"` | — |
| [SRC-1AE03B9EC3-L004983](../../agents/web_agent.py#L4983) | 4983 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L004984](../../agents/web_agent.py#L4984) | 4984 | `"            presearch_integrity = audit_answer_integrity("` | — |
| [SRC-1AE03B9EC3-L004985](../../agents/web_agent.py#L4985) | 4985 | `"                question, answer, sources, coverage_targets"` | — |
| [SRC-1AE03B9EC3-L004986](../../agents/web_agent.py#L4986) | 4986 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004987](../../agents/web_agent.py#L4987) | 4987 | `"            source_gap_targets = ["` | — |
| [SRC-1AE03B9EC3-L004988](../../agents/web_agent.py#L4988) | 4988 | `"                item[\"target\"]"` | — |
| [SRC-1AE03B9EC3-L004989](../../agents/web_agent.py#L4989) | 4989 | `"                for item in presearch_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L004990](../../agents/web_agent.py#L4990) | 4990 | `"                if item.get(\"source_evidence_status\") == \"no_source_lexical_signal\""` | — |
| [SRC-1AE03B9EC3-L004991](../../agents/web_agent.py#L4991) | 4991 | `"            ][:3]"` | — |
| [SRC-1AE03B9EC3-L004992](../../agents/web_agent.py#L4992) | 4992 | `"            if source_gap_targets:"` | — |
| [SRC-1AE03B9EC3-L004993](../../agents/web_agent.py#L4993) | 4993 | `"                criterion_gap_research[\"targets\"] = source_gap_targets"` | — |
| [SRC-1AE03B9EC3-L004994](../../agents/web_agent.py#L4994) | 4994 | `"                budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L004995](../../agents/web_agent.py#L4995) | 4995 | `"                if not plan.get(\"coverage_gap_repair_slot_reserved\"):"` | — |
| [SRC-1AE03B9EC3-L004996](../../agents/web_agent.py#L4996) | 4996 | `"                    criterion_gap_research[\"status\"] = \"skipped_no_reserved_search_slot\""` | — |
| [SRC-1AE03B9EC3-L004997](../../agents/web_agent.py#L4997) | 4997 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L004998](../../agents/web_agent.py#L4998) | 4998 | `"                        \"رُصدت محاور بلا إشارة لفظية في المصادر، لكن لم تُحجز ميزانية \""` | — |
| [SRC-1AE03B9EC3-L004999](../../agents/web_agent.py#L4999) | 4999 | `"                        \"استعلام إضافي لهذه المهمة؛ لذلك ستظل المحاور غير المحسومة ظاهرة.\""` | — |
| [SRC-1AE03B9EC3-L005000](../../agents/web_agent.py#L5000) | 5000 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005001](../../agents/web_agent.py#L5001) | 5001 | `"                elif budget is None:"` | — |
| [SRC-1AE03B9EC3-L005002](../../agents/web_agent.py#L5002) | 5002 | `"                    criterion_gap_research[\"status\"] = \"skipped_no_request_budget\""` | — |
| [SRC-1AE03B9EC3-L005003](../../agents/web_agent.py#L5003) | 5003 | `"                elif budget.remaining_units(\"search_queries\") < 1:"` | — |
| [SRC-1AE03B9EC3-L005004](../../agents/web_agent.py#L5004) | 5004 | `"                    criterion_gap_research[\"status\"] = \"skipped_search_budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L005005](../../agents/web_agent.py#L5005) | 5005 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L005006](../../agents/web_agent.py#L5006) | 5006 | `"                        \"رُصدت محاور بلا إشارة لفظية في المصادر، لكن ميزانية البحث لم تترك \""` | — |
| [SRC-1AE03B9EC3-L005007](../../agents/web_agent.py#L5007) | 5007 | `"                        \"استعلامًا إضافيًا للتحقق منها؛ لذلك لا تُعدّ الإجابة مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L005008](../../agents/web_agent.py#L5008) | 5008 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005009](../../agents/web_agent.py#L5009) | 5009 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L005010](../../agents/web_agent.py#L5010) | 5010 | `"                    fallback_queries = fallback_plan(question, clean_history).get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L005011](../../agents/web_agent.py#L5011) | 5011 | `"                    topic_query = compact_search_query("` | — |
| [SRC-1AE03B9EC3-L005012](../../agents/web_agent.py#L5012) | 5012 | `"                        fallback_queries[0] if fallback_queries else question"` | — |
| [SRC-1AE03B9EC3-L005013](../../agents/web_agent.py#L5013) | 5013 | `"                    ) or compact_search_query(question)"` | — |
| [SRC-1AE03B9EC3-L005014](../../agents/web_agent.py#L5014) | 5014 | `"                    gap_query = compact_search_query("` | — |
| [SRC-1AE03B9EC3-L005015](../../agents/web_agent.py#L5015) | 5015 | `"                        f\"{topic_query} {' '.join(source_gap_targets)} official specific evidence data\""` | — |
| [SRC-1AE03B9EC3-L005016](../../agents/web_agent.py#L5016) | 5016 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005017](../../agents/web_agent.py#L5017) | 5017 | `"                    known_query_keys = {"` | — |
| [SRC-1AE03B9EC3-L005018](../../agents/web_agent.py#L5018) | 5018 | `"                        _normalize_search_query(item).casefold()"` | — |
| [SRC-1AE03B9EC3-L005019](../../agents/web_agent.py#L5019) | 5019 | `"                        for item in plan.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L005020](../../agents/web_agent.py#L5020) | 5020 | `"                        if isinstance(item, str) and item.strip()"` | — |
| [SRC-1AE03B9EC3-L005021](../../agents/web_agent.py#L5021) | 5021 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L005022](../../agents/web_agent.py#L5022) | 5022 | `"                    if not gap_query or not _relevance_query_tokens(gap_query):"` | — |
| [SRC-1AE03B9EC3-L005023](../../agents/web_agent.py#L5023) | 5023 | `"                        criterion_gap_research[\"status\"] = \"skipped_no_valid_query\""` | — |
| [SRC-1AE03B9EC3-L005024](../../agents/web_agent.py#L5024) | 5024 | `"                    elif _normalize_search_query(gap_query).casefold() in known_query_keys:"` | — |
| [SRC-1AE03B9EC3-L005025](../../agents/web_agent.py#L5025) | 5025 | `"                        criterion_gap_research[\"status\"] = \"skipped_query_not_distinct\""` | — |
| [SRC-1AE03B9EC3-L005026](../../agents/web_agent.py#L5026) | 5026 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L005027](../../agents/web_agent.py#L5027) | 5027 | `"                        criterion_gap_research.update({"` | — |
| [SRC-1AE03B9EC3-L005028](../../agents/web_agent.py#L5028) | 5028 | `"                            \"attempted\": True,"` | — |
| [SRC-1AE03B9EC3-L005029](../../agents/web_agent.py#L5029) | 5029 | `"                            \"status\": \"searching_for_missing_criterion_evidence\","` | — |
| [SRC-1AE03B9EC3-L005030](../../agents/web_agent.py#L5030) | 5030 | `"                            \"query\": gap_query,"` | — |
| [SRC-1AE03B9EC3-L005031](../../agents/web_agent.py#L5031) | 5031 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L005032](../../agents/web_agent.py#L5032) | 5032 | `"                        gap_plan = dict(plan)"` | — |
| [SRC-1AE03B9EC3-L005033](../../agents/web_agent.py#L5033) | 5033 | `"                        gap_plan.update({"` | — |
| [SRC-1AE03B9EC3-L005034](../../agents/web_agent.py#L5034) | 5034 | `"                            \"queries\": [gap_query],"` | — |
| [SRC-1AE03B9EC3-L005035](../../agents/web_agent.py#L5035) | 5035 | `"                            \"query_limit\": 1,"` | — |
| [SRC-1AE03B9EC3-L005036](../../agents/web_agent.py#L5036) | 5036 | `"                            \"depth\": \"standard\","` | — |
| [SRC-1AE03B9EC3-L005037](../../agents/web_agent.py#L5037) | 5037 | `"                            \"social_focus\": False,"` | — |
| [SRC-1AE03B9EC3-L005038](../../agents/web_agent.py#L5038) | 5038 | `"                            \"platforms\": [],"` | — |
| [SRC-1AE03B9EC3-L005039](../../agents/web_agent.py#L5039) | 5039 | `"                            \"direct_urls\": [],"` | — |
| [SRC-1AE03B9EC3-L005040](../../agents/web_agent.py#L5040) | 5040 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L005041](../../agents/web_agent.py#L5041) | 5041 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L005042](../../agents/web_agent.py#L5042) | 5042 | `"                            gap_sources, gap_warnings, gap_report = self._collect_research(gap_plan)"` | — |
| [SRC-1AE03B9EC3-L005043](../../agents/web_agent.py#L5043) | 5043 | `"                        except (RuntimeError, AgentDependencyError, RequestBudgetExceeded, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L005044](../../agents/web_agent.py#L5044) | 5044 | `"                            gap_sources, gap_warnings = [], []"` | — |
| [SRC-1AE03B9EC3-L005045](../../agents/web_agent.py#L5045) | 5045 | `"                            gap_report = {"` | — |
| [SRC-1AE03B9EC3-L005046](../../agents/web_agent.py#L5046) | 5046 | `"                                \"queries_planned\": 1,"` | — |
| [SRC-1AE03B9EC3-L005047](../../agents/web_agent.py#L5047) | 5047 | `"                                \"queries_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L005048](../../agents/web_agent.py#L5048) | 5048 | `"                                \"queries_attempted_known\": False,"` | — |
| [SRC-1AE03B9EC3-L005049](../../agents/web_agent.py#L5049) | 5049 | `"                                \"search_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L005050](../../agents/web_agent.py#L5050) | 5050 | `"                                \"search_outcome\": \"unknown_after_research_error\","` | — |
| [SRC-1AE03B9EC3-L005051](../../agents/web_agent.py#L5051) | 5051 | `"                                \"query_results\": [],"` | — |
| [SRC-1AE03B9EC3-L005052](../../agents/web_agent.py#L5052) | 5052 | `"                            }"` | — |
| [SRC-1AE03B9EC3-L005053](../../agents/web_agent.py#L5053) | 5053 | `"                            criterion_gap_research[\"status\"] = \"search_failed\""` | — |
| [SRC-1AE03B9EC3-L005054](../../agents/web_agent.py#L5054) | 5054 | `"                            criterion_gap_research[\"error_class\"] = type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L005055](../../agents/web_agent.py#L5055) | 5055 | `"                        search_warnings.extend("` | — |
| [SRC-1AE03B9EC3-L005056](../../agents/web_agent.py#L5056) | 5056 | `"                            item for item in gap_warnings if isinstance(item, str)"` | — |
| [SRC-1AE03B9EC3-L005057](../../agents/web_agent.py#L5057) | 5057 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005058](../../agents/web_agent.py#L5058) | 5058 | `"                        source_indexes: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L005059](../../agents/web_agent.py#L5059) | 5059 | `"                        for source_index, source in enumerate(sources):"` | — |
| [SRC-1AE03B9EC3-L005060](../../agents/web_agent.py#L5060) | 5060 | `"                            source_key = self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L005061](../../agents/web_agent.py#L5061) | 5061 | `"                            if source_key:"` | — |
| [SRC-1AE03B9EC3-L005062](../../agents/web_agent.py#L5062) | 5062 | `"                                source_indexes.setdefault(source_key, source_index)"` | — |
| [SRC-1AE03B9EC3-L005063](../../agents/web_agent.py#L5063) | 5063 | `"                        evidence_updated = False"` | — |
| [SRC-1AE03B9EC3-L005064](../../agents/web_agent.py#L5064) | 5064 | `"                        for candidate in gap_sources:"` | — |
| [SRC-1AE03B9EC3-L005065](../../agents/web_agent.py#L5065) | 5065 | `"                            if not isinstance(candidate, dict):"` | — |
| [SRC-1AE03B9EC3-L005066](../../agents/web_agent.py#L5066) | 5066 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L005067](../../agents/web_agent.py#L5067) | 5067 | `"                            if not self._source_matches_query(gap_query, candidate):"` | — |
| [SRC-1AE03B9EC3-L005068](../../agents/web_agent.py#L5068) | 5068 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L005069](../../agents/web_agent.py#L5069) | 5069 | `"                            source_key = self._normalized_source_url_key(candidate.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L005070](../../agents/web_agent.py#L5070) | 5070 | `"                            if not source_key:"` | — |
| [SRC-1AE03B9EC3-L005071](../../agents/web_agent.py#L5071) | 5071 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L005072](../../agents/web_agent.py#L5072) | 5072 | `"                            existing_index = source_indexes.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L005073](../../agents/web_agent.py#L5073) | 5073 | `"                            if existing_index is None:"` | — |
| [SRC-1AE03B9EC3-L005074](../../agents/web_agent.py#L5074) | 5074 | `"                                source_indexes[source_key] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005075](../../agents/web_agent.py#L5075) | 5075 | `"                                sources.append(candidate)"` | — |
| [SRC-1AE03B9EC3-L005076](../../agents/web_agent.py#L5076) | 5076 | `"                                criterion_gap_research[\"new_sources_added\"] += 1"` | — |
| [SRC-1AE03B9EC3-L005077](../../agents/web_agent.py#L5077) | 5077 | `"                                evidence_updated = True"` | — |
| [SRC-1AE03B9EC3-L005078](../../agents/web_agent.py#L5078) | 5078 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L005079](../../agents/web_agent.py#L5079) | 5079 | `"                            existing_source = sources[existing_index]"` | — |
| [SRC-1AE03B9EC3-L005080](../../agents/web_agent.py#L5080) | 5080 | `"                            merged = dict(existing_source)"` | — |
| [SRC-1AE03B9EC3-L005081](../../agents/web_agent.py#L5081) | 5081 | `"                            source_enriched = False"` | — |
| [SRC-1AE03B9EC3-L005082](../../agents/web_agent.py#L5082) | 5082 | `"                            for text_key in (\"title\", \"snippet\", \"page_text\"):"` | — |
| [SRC-1AE03B9EC3-L005083](../../agents/web_agent.py#L5083) | 5083 | `"                                old_text = str(merged.get(text_key) or \"\")"` | — |
| [SRC-1AE03B9EC3-L005084](../../agents/web_agent.py#L5084) | 5084 | `"                                new_text = str(candidate.get(text_key) or \"\")"` | — |
| [SRC-1AE03B9EC3-L005085](../../agents/web_agent.py#L5085) | 5085 | `"                                if len(new_text) > len(old_text):"` | — |
| [SRC-1AE03B9EC3-L005086](../../agents/web_agent.py#L5086) | 5086 | `"                                    merged[text_key] = candidate[text_key]"` | — |
| [SRC-1AE03B9EC3-L005087](../../agents/web_agent.py#L5087) | 5087 | `"                                    source_enriched = True"` | — |
| [SRC-1AE03B9EC3-L005088](../../agents/web_agent.py#L5088) | 5088 | `"                            if candidate.get(\"page_fetched\") and not existing_source.get(\"page_fetched\"):"` | — |
| [SRC-1AE03B9EC3-L005089](../../agents/web_agent.py#L5089) | 5089 | `"                                merged[\"page_fetched\"] = True"` | — |
| [SRC-1AE03B9EC3-L005090](../../agents/web_agent.py#L5090) | 5090 | `"                                source_enriched = True"` | — |
| [SRC-1AE03B9EC3-L005091](../../agents/web_agent.py#L5091) | 5091 | `"                            if source_enriched:"` | — |
| [SRC-1AE03B9EC3-L005092](../../agents/web_agent.py#L5092) | 5092 | `"                                evidence_updated = True"` | — |
| [SRC-1AE03B9EC3-L005093](../../agents/web_agent.py#L5093) | 5093 | `"                                criterion_gap_research[\"evidence_sources_enriched\"] += 1"` | — |
| [SRC-1AE03B9EC3-L005094](../../agents/web_agent.py#L5094) | 5094 | `"                            merged[\"providers\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L005095](../../agents/web_agent.py#L5095) | 5095 | `"                                list(existing_source.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L005096](../../agents/web_agent.py#L5096) | 5096 | `"                                + list(candidate.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L005097](../../agents/web_agent.py#L5097) | 5097 | `"                            ))"` | — |
| [SRC-1AE03B9EC3-L005098](../../agents/web_agent.py#L5098) | 5098 | `"                            merged[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L005099](../../agents/web_agent.py#L5099) | 5099 | `"                                list(existing_source.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L005100](../../agents/web_agent.py#L5100) | 5100 | `"                                + list(candidate.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L005101](../../agents/web_agent.py#L5101) | 5101 | `"                                + [gap_query]"` | — |
| [SRC-1AE03B9EC3-L005102](../../agents/web_agent.py#L5102) | 5102 | `"                            ))"` | — |
| [SRC-1AE03B9EC3-L005103](../../agents/web_agent.py#L5103) | 5103 | `"                            sources[existing_index] = merged"` | — |
| [SRC-1AE03B9EC3-L005104](../../agents/web_agent.py#L5104) | 5104 | `"                        criterion_gap_research[\"source_count_after\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005105](../../agents/web_agent.py#L5105) | 5105 | `"                        plan[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L005106](../../agents/web_agent.py#L5106) | 5106 | `"                            list(plan.get(\"queries\", [])) + [gap_query]"` | — |
| [SRC-1AE03B9EC3-L005107](../../agents/web_agent.py#L5107) | 5107 | `"                        ))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L005108](../../agents/web_agent.py#L5108) | 5108 | `"                        report[\"criterion_gap_research\"] = dict(criterion_gap_research)"` | — |
| [SRC-1AE03B9EC3-L005109](../../agents/web_agent.py#L5109) | 5109 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L005110](../../agents/web_agent.py#L5110) | 5110 | `"                            report[\"queries_planned\"] = max("` | — |
| [SRC-1AE03B9EC3-L005111](../../agents/web_agent.py#L5111) | 5111 | `"                                0, int(report.get(\"queries_planned\", 0) or 0)"` | — |
| [SRC-1AE03B9EC3-L005112](../../agents/web_agent.py#L5112) | 5112 | `"                            ) + max(0, int(gap_report.get(\"queries_planned\", 1) or 0))"` | — |
| [SRC-1AE03B9EC3-L005113](../../agents/web_agent.py#L5113) | 5113 | `"                        except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-1AE03B9EC3-L005114](../../agents/web_agent.py#L5114) | 5114 | `"                            report[\"queries_planned\"] = None"` | — |
| [SRC-1AE03B9EC3-L005115](../../agents/web_agent.py#L5115) | 5115 | `"                        previous_attempts = report.get(\"queries_attempted\")"` | — |
| [SRC-1AE03B9EC3-L005116](../../agents/web_agent.py#L5116) | 5116 | `"                        extra_attempts = gap_report.get(\"queries_attempted\")"` | — |
| [SRC-1AE03B9EC3-L005117](../../agents/web_agent.py#L5117) | 5117 | `"                        if isinstance(previous_attempts, int) and isinstance(extra_attempts, int):"` | — |
| [SRC-1AE03B9EC3-L005118](../../agents/web_agent.py#L5118) | 5118 | `"                            report[\"queries_attempted\"] = max(0, previous_attempts) + max(0, extra_attempts)"` | — |
| [SRC-1AE03B9EC3-L005119](../../agents/web_agent.py#L5119) | 5119 | `"                            report[\"queries_attempted_known\"] = True"` | — |
| [SRC-1AE03B9EC3-L005120](../../agents/web_agent.py#L5120) | 5120 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L005121](../../agents/web_agent.py#L5121) | 5121 | `"                            report[\"queries_attempted\"] = None"` | — |
| [SRC-1AE03B9EC3-L005122](../../agents/web_agent.py#L5122) | 5122 | `"                            report[\"queries_attempted_known\"] = False"` | — |
| [SRC-1AE03B9EC3-L005123](../../agents/web_agent.py#L5123) | 5123 | `"                        old_query_results = report.get(\"query_results\")"` | — |
| [SRC-1AE03B9EC3-L005124](../../agents/web_agent.py#L5124) | 5124 | `"                        new_query_results = gap_report.get(\"query_results\")"` | — |
| [SRC-1AE03B9EC3-L005125](../../agents/web_agent.py#L5125) | 5125 | `"                        report[\"query_results\"] = ("` | — |
| [SRC-1AE03B9EC3-L005126](../../agents/web_agent.py#L5126) | 5126 | `"                            (old_query_results if isinstance(old_query_results, list) else [])"` | — |
| [SRC-1AE03B9EC3-L005127](../../agents/web_agent.py#L5127) | 5127 | `"                            + (new_query_results if isinstance(new_query_results, list) else [])"` | — |
| [SRC-1AE03B9EC3-L005128](../../agents/web_agent.py#L5128) | 5128 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005129](../../agents/web_agent.py#L5129) | 5129 | `"                        if evidence_updated:"` | — |
| [SRC-1AE03B9EC3-L005130](../../agents/web_agent.py#L5130) | 5130 | `"                            sources.sort("` | — |
| [SRC-1AE03B9EC3-L005131](../../agents/web_agent.py#L5131) | 5131 | `"                                key=lambda item: float(item.get(\"rank_score\", 0) or 0),"` | — |
| [SRC-1AE03B9EC3-L005132](../../agents/web_agent.py#L5132) | 5132 | `"                                reverse=True,"` | — |
| [SRC-1AE03B9EC3-L005133](../../agents/web_agent.py#L5133) | 5133 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L005134](../../agents/web_agent.py#L5134) | 5134 | `"                            try:"` | — |
| [SRC-1AE03B9EC3-L005135](../../agents/web_agent.py#L5135) | 5135 | `"                                revised_draft = self._generate("` | — |
| [SRC-1AE03B9EC3-L005136](../../agents/web_agent.py#L5136) | 5136 | `"                                    question,"` | — |
| [SRC-1AE03B9EC3-L005137](../../agents/web_agent.py#L5137) | 5137 | `"                                    clean_history,"` | — |
| [SRC-1AE03B9EC3-L005138](../../agents/web_agent.py#L5138) | 5138 | `"                                    sources,"` | — |
| [SRC-1AE03B9EC3-L005139](../../agents/web_agent.py#L5139) | 5139 | `"                                    search_warning,"` | — |
| [SRC-1AE03B9EC3-L005140](../../agents/web_agent.py#L5140) | 5140 | `"                                    research_plan=plan,"` | — |
| [SRC-1AE03B9EC3-L005141](../../agents/web_agent.py#L5141) | 5141 | `"                                    search_report=report,"` | — |
| [SRC-1AE03B9EC3-L005142](../../agents/web_agent.py#L5142) | 5142 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L005143](../../agents/web_agent.py#L5143) | 5143 | `"                                revised_answer = self._review_answer("` | — |
| [SRC-1AE03B9EC3-L005144](../../agents/web_agent.py#L5144) | 5144 | `"                                    question, revised_draft, sources[:MAX_LLM_CITED_SOURCES]"` | — |
| [SRC-1AE03B9EC3-L005145](../../agents/web_agent.py#L5145) | 5145 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L005146](../../agents/web_agent.py#L5146) | 5146 | `"                                answer = revised_answer"` | — |
| [SRC-1AE03B9EC3-L005147](../../agents/web_agent.py#L5147) | 5147 | `"                                review_status = \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005148](../../agents/web_agent.py#L5148) | 5148 | `"                                criterion_gap_research[\"status\"] = \"evidence_added_and_answer_regenerated\""` | — |
| [SRC-1AE03B9EC3-L005149](../../agents/web_agent.py#L5149) | 5149 | `"                            except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L005150](../../agents/web_agent.py#L5150) | 5150 | `"                                criterion_gap_research[\"status\"] = \"evidence_added_but_regeneration_unavailable\""` | — |
| [SRC-1AE03B9EC3-L005151](../../agents/web_agent.py#L5151) | 5151 | `"                                criterion_gap_research[\"regeneration_error_class\"] = type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L005152](../../agents/web_agent.py#L5152) | 5152 | `"                                coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L005153](../../agents/web_agent.py#L5153) | 5153 | `"                                    \"وصلت أدلة إضافية لمحور مطلوب، لكن تعذرت إعادة توليد الإجابة \""` | — |
| [SRC-1AE03B9EC3-L005154](../../agents/web_agent.py#L5154) | 5154 | `"                                    \"وتدقيقها ضمن الميزانية؛ راجع هذا المحور قبل اعتماد الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L005155](../../agents/web_agent.py#L5155) | 5155 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L005156](../../agents/web_agent.py#L5156) | 5156 | `"                        elif criterion_gap_research.get(\"status\") != \"search_failed\":"` | — |
| [SRC-1AE03B9EC3-L005157](../../agents/web_agent.py#L5157) | 5157 | `"                            criterion_gap_research[\"status\"] = \"search_completed_no_new_criterion_evidence\""` | — |
| [SRC-1AE03B9EC3-L005158](../../agents/web_agent.py#L5158) | 5158 | `"                            coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L005159](../../agents/web_agent.py#L5159) | 5159 | `"                                \"أُجري بحث إضافي لمحاور ناقصة، لكنه لم يضف نص مصدر يمكن تمييزه \""` | — |
| [SRC-1AE03B9EC3-L005160](../../agents/web_agent.py#L5160) | 5160 | `"                                \"كدليل جديد؛ ستظل هذه المحاور غير محسومة.\""` | — |
| [SRC-1AE03B9EC3-L005161](../../agents/web_agent.py#L5161) | 5161 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L005162](../../agents/web_agent.py#L5162) | 5162 | `"                        criterion_gap_research[\"source_count_after\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005163](../../agents/web_agent.py#L5163) | 5163 | `"                        report[\"criterion_gap_research\"] = dict(criterion_gap_research)"` | — |
| [SRC-1AE03B9EC3-L005164](../../agents/web_agent.py#L5164) | 5164 | `""` | — |
| [SRC-1AE03B9EC3-L005165](../../agents/web_agent.py#L5165) | 5165 | `"        report[\"criterion_gap_research\"] = dict(criterion_gap_research)"` | — |
| [SRC-1AE03B9EC3-L005166](../../agents/web_agent.py#L5166) | 5166 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L005167](../../agents/web_agent.py#L5167) | 5167 | `"            coverage_targets"` | — |
| [SRC-1AE03B9EC3-L005168](../../agents/web_agent.py#L5168) | 5168 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005169](../../agents/web_agent.py#L5169) | 5169 | `"            and sources"` | — |
| [SRC-1AE03B9EC3-L005170](../../agents/web_agent.py#L5170) | 5170 | `"            and self.api_key"` | — |
| [SRC-1AE03B9EC3-L005171](../../agents/web_agent.py#L5171) | 5171 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L005172](../../agents/web_agent.py#L5172) | 5172 | `"            initial_integrity = audit_answer_integrity(question, answer, sources, coverage_targets)"` | — |
| [SRC-1AE03B9EC3-L005173](../../agents/web_agent.py#L5173) | 5173 | `"            missing_targets = ["` | — |
| [SRC-1AE03B9EC3-L005174](../../agents/web_agent.py#L5174) | 5174 | `"                item[\"target\"] for item in initial_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L005175](../../agents/web_agent.py#L5175) | 5175 | `"                if item[\"status\"] == \"possibly_missing\""` | — |
| [SRC-1AE03B9EC3-L005176](../../agents/web_agent.py#L5176) | 5176 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L005177](../../agents/web_agent.py#L5177) | 5177 | `"            remaining_source_gap_targets = ["` | — |
| [SRC-1AE03B9EC3-L005178](../../agents/web_agent.py#L5178) | 5178 | `"                item[\"target\"] for item in initial_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L005179](../../agents/web_agent.py#L5179) | 5179 | `"                if item.get(\"source_evidence_status\") == \"no_source_lexical_signal\""` | — |
| [SRC-1AE03B9EC3-L005180](../../agents/web_agent.py#L5180) | 5180 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L005181](../../agents/web_agent.py#L5181) | 5181 | `"            if not missing_targets and remaining_source_gap_targets:"` | — |
| [SRC-1AE03B9EC3-L005182](../../agents/web_agent.py#L5182) | 5182 | `"                coverage_repair_status = \"source_evidence_gap_unresolved\""` | — |
| [SRC-1AE03B9EC3-L005183](../../agents/web_agent.py#L5183) | 5183 | `"                if not coverage_repair_warning:"` | — |
| [SRC-1AE03B9EC3-L005184](../../agents/web_agent.py#L5184) | 5184 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L005185](../../agents/web_agent.py#L5185) | 5185 | `"                        \"ذُكرت المحاور في الإجابة، لكن لم تظهر لها إشارات لفظية في المصادر؛ \""` | — |
| [SRC-1AE03B9EC3-L005186](../../agents/web_agent.py#L5186) | 5186 | `"                        \"ذكر المحور لا يُعد دليلًا، لذلك تظل المهمة غير مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L005187](../../agents/web_agent.py#L5187) | 5187 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005188](../../agents/web_agent.py#L5188) | 5188 | `"            elif not missing_targets:"` | — |
| [SRC-1AE03B9EC3-L005189](../../agents/web_agent.py#L5189) | 5189 | `"                coverage_repair_status = \"not_needed_lexical_signals_found\""` | — |
| [SRC-1AE03B9EC3-L005190](../../agents/web_agent.py#L5190) | 5190 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L005191](../../agents/web_agent.py#L5191) | 5191 | `"                coverage_repair_status = \"attempted\""` | — |
| [SRC-1AE03B9EC3-L005192](../../agents/web_agent.py#L5192) | 5192 | `"                try:"` | — |
| [SRC-1AE03B9EC3-L005193](../../agents/web_agent.py#L5193) | 5193 | `"                    repaired_answer = self._repair_answer_coverage("` | — |
| [SRC-1AE03B9EC3-L005194](../../agents/web_agent.py#L5194) | 5194 | `"                        question, answer, sources, missing_targets"` | — |
| [SRC-1AE03B9EC3-L005195](../../agents/web_agent.py#L5195) | 5195 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005196](../../agents/web_agent.py#L5196) | 5196 | `"                    if repaired_answer.strip() != answer.strip():"` | — |
| [SRC-1AE03B9EC3-L005197](../../agents/web_agent.py#L5197) | 5197 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L005198](../../agents/web_agent.py#L5198) | 5198 | `"                            reaudit_answer = self._review_answer("` | — |
| [SRC-1AE03B9EC3-L005199](../../agents/web_agent.py#L5199) | 5199 | `"                                question,"` | — |
| [SRC-1AE03B9EC3-L005200](../../agents/web_agent.py#L5200) | 5200 | `"                                repaired_answer,"` | — |
| [SRC-1AE03B9EC3-L005201](../../agents/web_agent.py#L5201) | 5201 | `"                                sources[:MAX_LLM_CITED_SOURCES],"` | — |
| [SRC-1AE03B9EC3-L005202](../../agents/web_agent.py#L5202) | 5202 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L005203](../../agents/web_agent.py#L5203) | 5203 | `"                            answer = reaudit_answer"` | — |
| [SRC-1AE03B9EC3-L005204](../../agents/web_agent.py#L5204) | 5204 | `"                            coverage_repair_status = \"revised_and_reaudited\""` | — |
| [SRC-1AE03B9EC3-L005205](../../agents/web_agent.py#L5205) | 5205 | `"                            review_status = \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005206](../../agents/web_agent.py#L5206) | 5206 | `"                        except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L005207](../../agents/web_agent.py#L5207) | 5207 | `"                            review_status = \"model_claim_audit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L005208](../../agents/web_agent.py#L5208) | 5208 | `"                            review_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L005209](../../agents/web_agent.py#L5209) | 5209 | `"                            coverage_repair_status = ("` | — |
| [SRC-1AE03B9EC3-L005210](../../agents/web_agent.py#L5210) | 5210 | `"                                \"reaudit_budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L005211](../../agents/web_agent.py#L5211) | 5211 | `"                                if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L005212](../../agents/web_agent.py#L5212) | 5212 | `"                                else \"reaudit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L005213](../../agents/web_agent.py#L5213) | 5213 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L005214](../../agents/web_agent.py#L5214) | 5214 | `"                            review_warning = ("` | — |
| [SRC-1AE03B9EC3-L005215](../../agents/web_agent.py#L5215) | 5215 | `"                                \"استُنفدت ميزانية النماذج قبل إعادة تدقيق الإجابة المعدلة؛ \""` | — |
| [SRC-1AE03B9EC3-L005216](../../agents/web_agent.py#L5216) | 5216 | `"                                \"لذلك لن أعرض النص المعدل بوصفه إجابة مكتملة، وأعرض مقتطفات المصادر بدلًا منه.\""` | — |
| [SRC-1AE03B9EC3-L005217](../../agents/web_agent.py#L5217) | 5217 | `"                                if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L005218](../../agents/web_agent.py#L5218) | 5218 | `"                                else"` | — |
| [SRC-1AE03B9EC3-L005219](../../agents/web_agent.py#L5219) | 5219 | `"                                \"تعذرت إعادة تدقيق الإجابة المعدلة مقابل الأدلة؛ لذلك لن أعرضها بوصفها إجابة مكتملة، \""` | — |
| [SRC-1AE03B9EC3-L005220](../../agents/web_agent.py#L5220) | 5220 | `"                                \"وأعرض مقتطفات المصادر بدلًا منها.\""` | — |
| [SRC-1AE03B9EC3-L005221](../../agents/web_agent.py#L5221) | 5221 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L005222](../../agents/web_agent.py#L5222) | 5222 | `"                            answer = _fallback_answer(sources, review_warning)"` | — |
| [SRC-1AE03B9EC3-L005223](../../agents/web_agent.py#L5223) | 5223 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L005224](../../agents/web_agent.py#L5224) | 5224 | `"                        coverage_repair_status = \"no_change_gap_unresolved\""` | — |
| [SRC-1AE03B9EC3-L005225](../../agents/web_agent.py#L5225) | 5225 | `"                        coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L005226](../../agents/web_agent.py#L5226) | 5226 | `"                            \"رصد الفحص اللفظي محورًا قد يكون ناقصًا، لكن محاولة الإصلاح لم تغيّر الإجابة؛ \""` | — |
| [SRC-1AE03B9EC3-L005227](../../agents/web_agent.py#L5227) | 5227 | `"                            \"تحقق من تغطية هذا المحور يدويًا.\""` | — |
| [SRC-1AE03B9EC3-L005228](../../agents/web_agent.py#L5228) | 5228 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005229](../../agents/web_agent.py#L5229) | 5229 | `"                except RequestBudgetExceeded:"` | — |
| [SRC-1AE03B9EC3-L005230](../../agents/web_agent.py#L5230) | 5230 | `"                    coverage_repair_status = \"budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L005231](../../agents/web_agent.py#L5231) | 5231 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L005232](../../agents/web_agent.py#L5232) | 5232 | `"                        \"استُنفدت ميزانية النماذج قبل محاولة إصلاح محور قد يكون ناقصًا؛ \""` | — |
| [SRC-1AE03B9EC3-L005233](../../agents/web_agent.py#L5233) | 5233 | `"                        \"لا تعتبر التغطية مكتملة دون مراجعة المحور المذكور.\""` | — |
| [SRC-1AE03B9EC3-L005234](../../agents/web_agent.py#L5234) | 5234 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005235](../../agents/web_agent.py#L5235) | 5235 | `"                except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L005236](../../agents/web_agent.py#L5236) | 5236 | `"                    coverage_repair_status = \"unavailable\""` | — |
| [SRC-1AE03B9EC3-L005237](../../agents/web_agent.py#L5237) | 5237 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L005238](../../agents/web_agent.py#L5238) | 5238 | `"                        \"تعذرت محاولة إصلاح محور قد يكون ناقصًا (\""` | — |
| [SRC-1AE03B9EC3-L005239](../../agents/web_agent.py#L5239) | 5239 | `"                        + type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L005240](../../agents/web_agent.py#L5240) | 5240 | `"                        + \")؛ راجع المحاور المطلوبة قبل اعتماد الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L005241](../../agents/web_agent.py#L5241) | 5241 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005242](../../agents/web_agent.py#L5242) | 5242 | `"        elif coverage_targets and review_status == \"model_claim_audit_completed\" and not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L005243](../../agents/web_agent.py#L5243) | 5243 | `"            coverage_repair_status = \"skipped_no_model_configuration\""` | — |
| [SRC-1AE03B9EC3-L005244](../../agents/web_agent.py#L5244) | 5244 | `"        elif coverage_targets:"` | — |
| [SRC-1AE03B9EC3-L005245](../../agents/web_agent.py#L5245) | 5245 | `"            coverage_repair_status = \"skipped_review_unavailable\""` | — |
| [SRC-1AE03B9EC3-L005246](../../agents/web_agent.py#L5246) | 5246 | `""` | — |
| [SRC-1AE03B9EC3-L005247](../../agents/web_agent.py#L5247) | 5247 | `"        if self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L005248](../../agents/web_agent.py#L5248) | 5248 | `"            answer += \"\\n\\nروابط إضافية من البحث المباشر عبر الويب:\""` | — |
| [SRC-1AE03B9EC3-L005249](../../agents/web_agent.py#L5249) | 5249 | `"            for source in self.server_search_sources[:8]:"` | — |
| [SRC-1AE03B9EC3-L005250](../../agents/web_agent.py#L5250) | 5250 | `"                answer += \"\\n- \" + source[\"title\"] + \" — \" + source[\"url\"]"` | — |
| [SRC-1AE03B9EC3-L005251](../../agents/web_agent.py#L5251) | 5251 | `"        max_citable_sources = min(MAX_LLM_CITED_SOURCES, len(sources))"` | — |
| [SRC-1AE03B9EC3-L005252](../../agents/web_agent.py#L5252) | 5252 | `"        answer, citation_warnings = self._remove_invalid_citations("` | — |
| [SRC-1AE03B9EC3-L005253](../../agents/web_agent.py#L5253) | 5253 | `"            answer, max_citable_sources"` | — |
| [SRC-1AE03B9EC3-L005254](../../agents/web_agent.py#L5254) | 5254 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005255](../../agents/web_agent.py#L5255) | 5255 | `"        citation_validation = self._citation_validation_metadata("` | — |
| [SRC-1AE03B9EC3-L005256](../../agents/web_agent.py#L5256) | 5256 | `"            answer, max_citable_sources, citation_warnings, review_status"` | — |
| [SRC-1AE03B9EC3-L005257](../../agents/web_agent.py#L5257) | 5257 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005258](../../agents/web_agent.py#L5258) | 5258 | `"        report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005259](../../agents/web_agent.py#L5259) | 5259 | `"        report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L005260](../../agents/web_agent.py#L5260) | 5260 | `"        report[\"second_pass_review\"] = review_status"` | — |
| [SRC-1AE03B9EC3-L005261](../../agents/web_agent.py#L5261) | 5261 | `"        report[\"claim_audit\"] = review_status"` | — |
| [SRC-1AE03B9EC3-L005262](../../agents/web_agent.py#L5262) | 5262 | `"        answer_coverage = {"` | — |
| [SRC-1AE03B9EC3-L005263](../../agents/web_agent.py#L5263) | 5263 | `"            \"method\": \"explicit_criteria_heuristic\","` | — |
| [SRC-1AE03B9EC3-L005264](../../agents/web_agent.py#L5264) | 5264 | `"            \"targets\": coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L005265](../../agents/web_agent.py#L5265) | 5265 | `"            \"review_prompted\": review_status == \"model_claim_audit_completed\","` | — |
| [SRC-1AE03B9EC3-L005266](../../agents/web_agent.py#L5266) | 5266 | `"            \"status\": ("` | — |
| [SRC-1AE03B9EC3-L005267](../../agents/web_agent.py#L5267) | 5267 | `"                \"model_review_requested_not_machine_verified\""` | — |
| [SRC-1AE03B9EC3-L005268](../../agents/web_agent.py#L5268) | 5268 | `"                if coverage_targets and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005269](../../agents/web_agent.py#L5269) | 5269 | `"                else \"review_unavailable\""` | — |
| [SRC-1AE03B9EC3-L005270](../../agents/web_agent.py#L5270) | 5270 | `"                if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L005271](../../agents/web_agent.py#L5271) | 5271 | `"                else \"no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L005272](../../agents/web_agent.py#L5272) | 5272 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L005273](../../agents/web_agent.py#L5273) | 5273 | `"            \"automatically_graded\": False,"` | — |
| [SRC-1AE03B9EC3-L005274](../../agents/web_agent.py#L5274) | 5274 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005275](../../agents/web_agent.py#L5275) | 5275 | `"        report[\"answer_coverage\"] = answer_coverage"` | — |
| [SRC-1AE03B9EC3-L005276](../../agents/web_agent.py#L5276) | 5276 | `"        report[\"coverage_repair_status\"] = coverage_repair_status"` | — |
| [SRC-1AE03B9EC3-L005277](../../agents/web_agent.py#L5277) | 5277 | `"        answer_integrity = audit_answer_integrity(question, answer, sources, coverage_targets)"` | — |
| [SRC-1AE03B9EC3-L005278](../../agents/web_agent.py#L5278) | 5278 | `"        answer_coverage[\"target_checks\"] = answer_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L005279](../../agents/web_agent.py#L5279) | 5279 | `"        answer_coverage[\"potentially_missing_target_count\"] = answer_integrity[\"potentially_missing_target_count\"]"` | — |
| [SRC-1AE03B9EC3-L005280](../../agents/web_agent.py#L5280) | 5280 | `"        answer_coverage[\"source_evidence_gap_count\"] = answer_integrity[\"source_evidence_gap_count\"]"` | — |
| [SRC-1AE03B9EC3-L005281](../../agents/web_agent.py#L5281) | 5281 | `"        answer_coverage[\"lexical_screen_method\"] = \"deterministic_lexical_screen_only_not_semantic_grading\""` | — |
| [SRC-1AE03B9EC3-L005282](../../agents/web_agent.py#L5282) | 5282 | `"        task_fulfillment_status = ("` | — |
| [SRC-1AE03B9EC3-L005283](../../agents/web_agent.py#L5283) | 5283 | `"            \"possible_gap_detected\""` | — |
| [SRC-1AE03B9EC3-L005284](../../agents/web_agent.py#L5284) | 5284 | `"            if ("` | — |
| [SRC-1AE03B9EC3-L005285](../../agents/web_agent.py#L5285) | 5285 | `"                answer_integrity[\"potentially_missing_target_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L005286](../../agents/web_agent.py#L5286) | 5286 | `"                or answer_integrity[\"source_evidence_gap_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L005287](../../agents/web_agent.py#L5287) | 5287 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005288](../../agents/web_agent.py#L5288) | 5288 | `"            else \"lexical_signals_found_not_semantically_verified\" if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L005289](../../agents/web_agent.py#L5289) | 5289 | `"            else \"not_machine_assessed_no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L005290](../../agents/web_agent.py#L5290) | 5290 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005291](../../agents/web_agent.py#L5291) | 5291 | `"        answer_coverage[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L005292](../../agents/web_agent.py#L5292) | 5292 | `"        report[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L005293](../../agents/web_agent.py#L5293) | 5293 | `"        report[\"answer_integrity\"] = answer_integrity"` | — |
| [SRC-1AE03B9EC3-L005294](../../agents/web_agent.py#L5294) | 5294 | `"        report[\"connector_summary\"] = self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L005295](../../agents/web_agent.py#L5295) | 5295 | `"            list(self._provider_diagnostics), sources"` | — |
| [SRC-1AE03B9EC3-L005296](../../agents/web_agent.py#L5296) | 5296 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005297](../../agents/web_agent.py#L5297) | 5297 | `"        report[\"provider_diagnostics\"] = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L005298](../../agents/web_agent.py#L5298) | 5298 | `"        distinct_providers = {"` | — |
| [SRC-1AE03B9EC3-L005299](../../agents/web_agent.py#L5299) | 5299 | `"            provider for source in sources for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L005300](../../agents/web_agent.py#L5300) | 5300 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005301](../../agents/web_agent.py#L5301) | 5301 | `"        distinct_domains = {"` | — |
| [SRC-1AE03B9EC3-L005302](../../agents/web_agent.py#L5302) | 5302 | `"            registrable_domain("` | — |
| [SRC-1AE03B9EC3-L005303](../../agents/web_agent.py#L5303) | 5303 | `"                source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L005304](../../agents/web_agent.py#L5304) | 5304 | `"                or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L005305](../../agents/web_agent.py#L5305) | 5305 | `"                or \"\""` | — |
| [SRC-1AE03B9EC3-L005306](../../agents/web_agent.py#L5306) | 5306 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005307](../../agents/web_agent.py#L5307) | 5307 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L005308](../../agents/web_agent.py#L5308) | 5308 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005309](../../agents/web_agent.py#L5309) | 5309 | `"        distinct_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L005310](../../agents/web_agent.py#L5310) | 5310 | `"        fetched_pages = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L005311](../../agents/web_agent.py#L5311) | 5311 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L005312](../../agents/web_agent.py#L5312) | 5312 | `"            len(sources) >= 4 and len(distinct_domains) >= 3"` | — |
| [SRC-1AE03B9EC3-L005313](../../agents/web_agent.py#L5313) | 5313 | `"            and len(distinct_providers) >= 2 and fetched_pages >= 1"` | — |
| [SRC-1AE03B9EC3-L005314](../../agents/web_agent.py#L5314) | 5314 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005315](../../agents/web_agent.py#L5315) | 5315 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L005316](../../agents/web_agent.py#L5316) | 5316 | `"            research_quality = \"excellent\""` | — |
| [SRC-1AE03B9EC3-L005317](../../agents/web_agent.py#L5317) | 5317 | `"        elif ("` | — |
| [SRC-1AE03B9EC3-L005318](../../agents/web_agent.py#L5318) | 5318 | `"            len(sources) >= 2 and len(distinct_domains) >= 2"` | — |
| [SRC-1AE03B9EC3-L005319](../../agents/web_agent.py#L5319) | 5319 | `"            and (len(distinct_providers) >= 2 or fetched_pages >= 1)"` | — |
| [SRC-1AE03B9EC3-L005320](../../agents/web_agent.py#L5320) | 5320 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005321](../../agents/web_agent.py#L5321) | 5321 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L005322](../../agents/web_agent.py#L5322) | 5322 | `"            research_quality = \"good\""` | — |
| [SRC-1AE03B9EC3-L005323](../../agents/web_agent.py#L5323) | 5323 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L005324](../../agents/web_agent.py#L5324) | 5324 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L005325](../../agents/web_agent.py#L5325) | 5325 | `""` | — |
| [SRC-1AE03B9EC3-L005326](../../agents/web_agent.py#L5326) | 5326 | `"        # Source breadth and a completed model-assisted review do not justify a"` | — |
| [SRC-1AE03B9EC3-L005327](../../agents/web_agent.py#L5327) | 5327 | `"        # positive research-quality label if the final answer has no valid source"` | — |
| [SRC-1AE03B9EC3-L005328](../../agents/web_agent.py#L5328) | 5328 | `"        # citation markers. This is a deterministic presentation guard, not a"` | — |
| [SRC-1AE03B9EC3-L005329](../../agents/web_agent.py#L5329) | 5329 | `"        # semantic entailment check."` | — |
| [SRC-1AE03B9EC3-L005330](../../agents/web_agent.py#L5330) | 5330 | `"        uncited_reviewed_answer = ("` | — |
| [SRC-1AE03B9EC3-L005331](../../agents/web_agent.py#L5331) | 5331 | `"            used_llm"` | — |
| [SRC-1AE03B9EC3-L005332](../../agents/web_agent.py#L5332) | 5332 | `"            and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L005333](../../agents/web_agent.py#L5333) | 5333 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005334](../../agents/web_agent.py#L5334) | 5334 | `"            and citation_validation[\"valid_citation_count\"] == 0"` | — |
| [SRC-1AE03B9EC3-L005335](../../agents/web_agent.py#L5335) | 5335 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005336](../../agents/web_agent.py#L5336) | 5336 | `"        if uncited_reviewed_answer:"` | — |
| [SRC-1AE03B9EC3-L005337](../../agents/web_agent.py#L5337) | 5337 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L005338](../../agents/web_agent.py#L5338) | 5338 | `"            citation_validation[\"claim_support\"] = \"not_established_no_valid_source_citations\""` | — |
| [SRC-1AE03B9EC3-L005339](../../agents/web_agent.py#L5339) | 5339 | `"            answer_evidence_status = \"reviewed_answer_has_no_valid_citations\""` | — |
| [SRC-1AE03B9EC3-L005340](../../agents/web_agent.py#L5340) | 5340 | `"            uncited_answer_warning = ("` | — |
| [SRC-1AE03B9EC3-L005341](../../agents/web_agent.py#L5341) | 5341 | `"                \"اكتملت مراجعة النموذج، لكن الإجابة النهائية لا تحتوي على إحالات صالحة \""` | — |
| [SRC-1AE03B9EC3-L005342](../../agents/web_agent.py#L5342) | 5342 | `"                \"إلى قائمة المصادر؛ لذلك صُنّفت جودة البحث «جزئية». وجود المصادر أو \""` | — |
| [SRC-1AE03B9EC3-L005343](../../agents/web_agent.py#L5343) | 5343 | `"                \"اكتمال مراجعة النموذج لا يثبت دعم كل ادعاء.\""` | — |
| [SRC-1AE03B9EC3-L005344](../../agents/web_agent.py#L5344) | 5344 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005345](../../agents/web_agent.py#L5345) | 5345 | `"        elif citation_validation[\"valid_citation_count\"] > 0:"` | — |
| [SRC-1AE03B9EC3-L005346](../../agents/web_agent.py#L5346) | 5346 | `"            answer_evidence_status = \"citation_indices_validated_only\""` | — |
| [SRC-1AE03B9EC3-L005347](../../agents/web_agent.py#L5347) | 5347 | `"            uncited_answer_warning = None"` | — |
| [SRC-1AE03B9EC3-L005348](../../agents/web_agent.py#L5348) | 5348 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L005349](../../agents/web_agent.py#L5349) | 5349 | `"            answer_evidence_status = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L005350](../../agents/web_agent.py#L5350) | 5350 | `"            uncited_answer_warning = None"` | — |
| [SRC-1AE03B9EC3-L005351](../../agents/web_agent.py#L5351) | 5351 | `""` | — |
| [SRC-1AE03B9EC3-L005352](../../agents/web_agent.py#L5352) | 5352 | `"        search_attempted = search_attempted or bool(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L005353](../../agents/web_agent.py#L5353) | 5353 | `"        report[\"search_attempted\"] = search_attempted"` | — |
| [SRC-1AE03B9EC3-L005354](../../agents/web_agent.py#L5354) | 5354 | `"        report[\"search_outcome\"] = ("` | — |
| [SRC-1AE03B9EC3-L005355](../../agents/web_agent.py#L5355) | 5355 | `"            \"attempted_with_usable_sources\" if search_attempted and sources"` | — |
| [SRC-1AE03B9EC3-L005356](../../agents/web_agent.py#L5356) | 5356 | `"            else \"attempted_no_usable_sources\" if search_attempted"` | — |
| [SRC-1AE03B9EC3-L005357](../../agents/web_agent.py#L5357) | 5357 | `"            else \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L005358](../../agents/web_agent.py#L5358) | 5358 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005359](../../agents/web_agent.py#L5359) | 5359 | `"        report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005360](../../agents/web_agent.py#L5360) | 5360 | `"        report[\"research_quality\"] = research_quality"` | — |
| [SRC-1AE03B9EC3-L005361](../../agents/web_agent.py#L5361) | 5361 | `"        report[\"research_quality_semantics\"] = \"process_coverage_not_factual_probability\""` | — |
| [SRC-1AE03B9EC3-L005362](../../agents/web_agent.py#L5362) | 5362 | `"        report[\"answer_evidence_status\"] = answer_evidence_status"` | — |
| [SRC-1AE03B9EC3-L005363](../../agents/web_agent.py#L5363) | 5363 | `"        report[\"distinct_registrable_domains\"] = len(distinct_domains)"` | — |
| [SRC-1AE03B9EC3-L005364](../../agents/web_agent.py#L5364) | 5364 | `"        report[\"independent_sources\"] = len(distinct_domains)  # Legacy alias; not editorial independence."` | — |
| [SRC-1AE03B9EC3-L005365](../../agents/web_agent.py#L5365) | 5365 | `"        report[\"independent_sources_field_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L005366](../../agents/web_agent.py#L5366) | 5366 | `"            \"legacy_compatibility_alias_for_distinct_registrable_domain_count\""` | — |
| [SRC-1AE03B9EC3-L005367](../../agents/web_agent.py#L5367) | 5367 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005368](../../agents/web_agent.py#L5368) | 5368 | `"        report[\"source_diversity_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L005369](../../agents/web_agent.py#L5369) | 5369 | `"            \"distinct_registrable_domains_not_editorial_independence\""` | — |
| [SRC-1AE03B9EC3-L005370](../../agents/web_agent.py#L5370) | 5370 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005371](../../agents/web_agent.py#L5371) | 5371 | `"        report[\"editorial_independence_status\"] = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L005372](../../agents/web_agent.py#L5372) | 5372 | `"        report[\"claim_audit_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L005373](../../agents/web_agent.py#L5373) | 5373 | `"            \"model_assisted_not_independent_fact_check\""` | — |
| [SRC-1AE03B9EC3-L005374](../../agents/web_agent.py#L5374) | 5374 | `"            if review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005375](../../agents/web_agent.py#L5375) | 5375 | `"            else \"not_verified\""` | — |
| [SRC-1AE03B9EC3-L005376](../../agents/web_agent.py#L5376) | 5376 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005377](../../agents/web_agent.py#L5377) | 5377 | `"        report[\"insufficient_evidence\"] = False"` | — |
| [SRC-1AE03B9EC3-L005378](../../agents/web_agent.py#L5378) | 5378 | `"        report[\"valid_citation_range\"] = [1, max_citable_sources] if max_citable_sources else []"` | — |
| [SRC-1AE03B9EC3-L005379](../../agents/web_agent.py#L5379) | 5379 | `"        report[\"citation_count\"] = citation_validation[\"valid_citation_count\"]"` | — |
| [SRC-1AE03B9EC3-L005380](../../agents/web_agent.py#L5380) | 5380 | `"        report[\"citation_check\"] = citation_validation[\"status\"]"` | — |
| [SRC-1AE03B9EC3-L005381](../../agents/web_agent.py#L5381) | 5381 | `"        report[\"citation_validation\"] = citation_validation"` | — |
| [SRC-1AE03B9EC3-L005382](../../agents/web_agent.py#L5382) | 5382 | `"        warnings = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L005383](../../agents/web_agent.py#L5383) | 5383 | `"            search_warnings"` | — |
| [SRC-1AE03B9EC3-L005384](../../agents/web_agent.py#L5384) | 5384 | `"            + ([llm_warning] if llm_warning else [])"` | — |
| [SRC-1AE03B9EC3-L005385](../../agents/web_agent.py#L5385) | 5385 | `"            + ([review_warning] if review_warning else [])"` | — |
| [SRC-1AE03B9EC3-L005386](../../agents/web_agent.py#L5386) | 5386 | `"            + ([coverage_repair_warning] if coverage_repair_warning else [])"` | — |
| [SRC-1AE03B9EC3-L005387](../../agents/web_agent.py#L5387) | 5387 | `"            + citation_warnings"` | — |
| [SRC-1AE03B9EC3-L005388](../../agents/web_agent.py#L5388) | 5388 | `"            + ([uncited_answer_warning] if uncited_answer_warning else [])"` | — |
| [SRC-1AE03B9EC3-L005389](../../agents/web_agent.py#L5389) | 5389 | `"        ))"` | — |
| [SRC-1AE03B9EC3-L005390](../../agents/web_agent.py#L5390) | 5390 | `"        report[\"model_calls\"] = list(self.model_usage)"` | — |
| [SRC-1AE03B9EC3-L005391](../../agents/web_agent.py#L5391) | 5391 | `"        report[\"openrouter_web_search_enabled\"] = self.openrouter_web_search_enabled"` | — |
| [SRC-1AE03B9EC3-L005392](../../agents/web_agent.py#L5392) | 5392 | `"        report[\"openrouter_web_search_results\"] = len(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L005393](../../agents/web_agent.py#L5393) | 5393 | `"        if generation_budget_exhausted or review_budget_exhausted:"` | — |
| [SRC-1AE03B9EC3-L005394](../../agents/web_agent.py#L5394) | 5394 | `"            final_answer_status = \"budget_exhausted_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L005395](../../agents/web_agent.py#L5395) | 5395 | `"        elif llm_warning:"` | — |
| [SRC-1AE03B9EC3-L005396](../../agents/web_agent.py#L5396) | 5396 | `"            final_answer_status = ("` | — |
| [SRC-1AE03B9EC3-L005397](../../agents/web_agent.py#L5397) | 5397 | `"                \"model_not_configured_fallback\""` | — |
| [SRC-1AE03B9EC3-L005398](../../agents/web_agent.py#L5398) | 5398 | `"                if not self.api_key"` | — |
| [SRC-1AE03B9EC3-L005399](../../agents/web_agent.py#L5399) | 5399 | `"                else \"generation_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L005400](../../agents/web_agent.py#L5400) | 5400 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005401](../../agents/web_agent.py#L5401) | 5401 | `"        elif review_warning:"` | — |
| [SRC-1AE03B9EC3-L005402](../../agents/web_agent.py#L5402) | 5402 | `"            final_answer_status = \"review_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L005403](../../agents/web_agent.py#L5403) | 5403 | `"        elif coverage_repair_status == \"no_change_gap_unresolved\":"` | — |
| [SRC-1AE03B9EC3-L005404](../../agents/web_agent.py#L5404) | 5404 | `"            final_answer_status = \"coverage_repair_left_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L005405](../../agents/web_agent.py#L5405) | 5405 | `"        elif coverage_repair_status == \"budget_exhausted\":"` | — |
| [SRC-1AE03B9EC3-L005406](../../agents/web_agent.py#L5406) | 5406 | `"            final_answer_status = \"coverage_repair_budget_exhausted_with_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L005407](../../agents/web_agent.py#L5407) | 5407 | `"        elif coverage_repair_status == \"unavailable\":"` | — |
| [SRC-1AE03B9EC3-L005408](../../agents/web_agent.py#L5408) | 5408 | `"            final_answer_status = \"coverage_repair_unavailable_with_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L005409](../../agents/web_agent.py#L5409) | 5409 | `"        elif used_llm:"` | — |
| [SRC-1AE03B9EC3-L005410](../../agents/web_agent.py#L5410) | 5410 | `"            final_answer_status = \"model_answer_generated\""` | — |
| [SRC-1AE03B9EC3-L005411](../../agents/web_agent.py#L5411) | 5411 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L005412](../../agents/web_agent.py#L5412) | 5412 | `"            final_answer_status = \"source_fallback\""` | — |
| [SRC-1AE03B9EC3-L005413](../../agents/web_agent.py#L5413) | 5413 | `""` | — |
| [SRC-1AE03B9EC3-L005414](../../agents/web_agent.py#L5414) | 5414 | `"        public_sources = []"` | — |
| [SRC-1AE03B9EC3-L005415](../../agents/web_agent.py#L5415) | 5415 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L005416](../../agents/web_agent.py#L5416) | 5416 | `"            public_sources.append({"` | — |
| [SRC-1AE03B9EC3-L005417](../../agents/web_agent.py#L5417) | 5417 | `"                \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L005418](../../agents/web_agent.py#L5418) | 5418 | `"                \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L005419](../../agents/web_agent.py#L5419) | 5419 | `"                \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005420](../../agents/web_agent.py#L5420) | 5420 | `"                \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L005421](../../agents/web_agent.py#L5421) | 5421 | `"                \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L005422](../../agents/web_agent.py#L5422) | 5422 | `"                \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L005423](../../agents/web_agent.py#L5423) | 5423 | `"                \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L005424](../../agents/web_agent.py#L5424) | 5424 | `"                \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005425](../../agents/web_agent.py#L5425) | 5425 | `"                \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L005426](../../agents/web_agent.py#L5426) | 5426 | `"                \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005427](../../agents/web_agent.py#L5427) | 5427 | `"                \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005428](../../agents/web_agent.py#L5428) | 5428 | `"                \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005429](../../agents/web_agent.py#L5429) | 5429 | `"                \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L005430](../../agents/web_agent.py#L5430) | 5430 | `"                \"lead_qualification\": source.get(\"lead_qualification\"),"` | — |
| [SRC-1AE03B9EC3-L005431](../../agents/web_agent.py#L5431) | 5431 | `"                \"lead_intent_evidence\": source.get(\"lead_intent_evidence\"),"` | — |
| [SRC-1AE03B9EC3-L005432](../../agents/web_agent.py#L5432) | 5432 | `"            })"` | — |
| [SRC-1AE03B9EC3-L005433](../../agents/web_agent.py#L5433) | 5433 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L005434](../../agents/web_agent.py#L5434) | 5434 | `"            \"answer\": answer,"` | — |
| [SRC-1AE03B9EC3-L005435](../../agents/web_agent.py#L5435) | 5435 | `"            \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L005436](../../agents/web_agent.py#L5436) | 5436 | `"            \"search_query\": (plan.get(\"queries\") or [\"\"])[0],"` | — |
| [SRC-1AE03B9EC3-L005437](../../agents/web_agent.py#L5437) | 5437 | `"            \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L005438](../../agents/web_agent.py#L5438) | 5438 | `"            \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L005439](../../agents/web_agent.py#L5439) | 5439 | `"                \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L005440](../../agents/web_agent.py#L5440) | 5440 | `"                \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L005441](../../agents/web_agent.py#L5441) | 5441 | `"                \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L005442](../../agents/web_agent.py#L5442) | 5442 | `"                \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L005443](../../agents/web_agent.py#L5443) | 5443 | `"                \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L005444](../../agents/web_agent.py#L5444) | 5444 | `"                \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L005445](../../agents/web_agent.py#L5445) | 5445 | `"                \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L005446](../../agents/web_agent.py#L5446) | 5446 | `"                \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L005447](../../agents/web_agent.py#L5447) | 5447 | `"                \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L005448](../../agents/web_agent.py#L5448) | 5448 | `"            },"` | — |
| [SRC-1AE03B9EC3-L005449](../../agents/web_agent.py#L5449) | 5449 | `"            \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L005450](../../agents/web_agent.py#L5450) | 5450 | `"            \"sources\": public_sources,"` | — |
| [SRC-1AE03B9EC3-L005451](../../agents/web_agent.py#L5451) | 5451 | `"            \"research_quality\": research_quality,"` | — |
| [SRC-1AE03B9EC3-L005452](../../agents/web_agent.py#L5452) | 5452 | `"            \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L005453](../../agents/web_agent.py#L5453) | 5453 | `"            \"answer_evidence_status\": answer_evidence_status,"` | — |
| [SRC-1AE03B9EC3-L005454](../../agents/web_agent.py#L5454) | 5454 | `"            \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L005455](../../agents/web_agent.py#L5455) | 5455 | `"            \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L005456](../../agents/web_agent.py#L5456) | 5456 | `"            \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L005457](../../agents/web_agent.py#L5457) | 5457 | `"            \"coverage_repair_status\": coverage_repair_status,"` | — |
| [SRC-1AE03B9EC3-L005458](../../agents/web_agent.py#L5458) | 5458 | `"            \"used_language_model\": used_llm,"` | — |
| [SRC-1AE03B9EC3-L005459](../../agents/web_agent.py#L5459) | 5459 | `"            \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L005460](../../agents/web_agent.py#L5460) | 5460 | `"            \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L005461](../../agents/web_agent.py#L5461) | 5461 | `"            \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L005462](../../agents/web_agent.py#L5462) | 5462 | `"            \"warnings\": warnings,"` | — |
| [SRC-1AE03B9EC3-L005463](../../agents/web_agent.py#L5463) | 5463 | `"            \"kind\": \"web_research\" if used_llm else \"web_fallback\","` | — |
| [SRC-1AE03B9EC3-L005464](../../agents/web_agent.py#L5464) | 5464 | `"            \"final_answer_status\": final_answer_status,"` | — |
| [SRC-1AE03B9EC3-L005465](../../agents/web_agent.py#L5465) | 5465 | `"            \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L005466](../../agents/web_agent.py#L5466) | 5466 | `"            \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L005467](../../agents/web_agent.py#L5467) | 5467 | `"        }"` | — |
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
| [SRC-EEF2E6447C-L000015](../../api/omarai.py#L15) | 15 | `"from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer"` | — |
| [SRC-EEF2E6447C-L000016](../../api/omarai.py#L16) | 16 | `"from pathlib import Path"` | — |
| [SRC-EEF2E6447C-L000017](../../api/omarai.py#L17) | 17 | `"from typing import ClassVar"` | — |
| [SRC-EEF2E6447C-L000018](../../api/omarai.py#L18) | 18 | `"from urllib.parse import parse_qs, urlparse"` | — |
| [SRC-EEF2E6447C-L000019](../../api/omarai.py#L19) | 19 | `""` | — |
| [SRC-EEF2E6447C-L000020](../../api/omarai.py#L20) | 20 | `"from agents.omarai import LeadStore, analyze, normalize"` | — |
| [SRC-EEF2E6447C-L000021](../../api/omarai.py#L21) | 21 | `"from agents.web_agent import WebAgent"` | — |
| [SRC-EEF2E6447C-L000022](../../api/omarai.py#L22) | 22 | `""` | — |
| [SRC-EEF2E6447C-L000023](../../api/omarai.py#L23) | 23 | `"ROOT = Path(__file__).resolve().parents[1] / \"web\""` | — |
| [SRC-EEF2E6447C-L000024](../../api/omarai.py#L24) | 24 | `"AGENT_DASHBOARD = ROOT / \"agent.html\""` | — |
| [SRC-EEF2E6447C-L000025](../../api/omarai.py#L25) | 25 | `"LEADS_DASHBOARD = ROOT / \"dashboard.html\""` | — |
| [SRC-EEF2E6447C-L000026](../../api/omarai.py#L26) | 26 | `"MAX_REQUEST_BODY_BYTES = 200_000"` | — |
| [SRC-EEF2E6447C-L000027](../../api/omarai.py#L27) | 27 | `""` | — |
| [SRC-EEF2E6447C-L000028](../../api/omarai.py#L28) | 28 | `""` | — |
| [SRC-EEF2E6447C-L000029](../../api/omarai.py#L29) | 29 | `"def _csp_hash_source(value: str) -> str:"` | — |
| [SRC-EEF2E6447C-L000030](../../api/omarai.py#L30) | 30 | `"    digest = base64.b64encode(hashlib.sha256(value.encode(\"utf-8\")).digest()).decode(\"ascii\")"` | — |
| [SRC-EEF2E6447C-L000031](../../api/omarai.py#L31) | 31 | `"    return f\"'sha256-{digest}'\""` | — |
| [SRC-EEF2E6447C-L000032](../../api/omarai.py#L32) | 32 | `""` | — |
| [SRC-EEF2E6447C-L000033](../../api/omarai.py#L33) | 33 | `""` | — |
| [SRC-EEF2E6447C-L000034](../../api/omarai.py#L34) | 34 | `"@lru_cache(maxsize=1)"` | — |
| [SRC-EEF2E6447C-L000035](../../api/omarai.py#L35) | 35 | `"def _content_security_policy() -> str:"` | — |
| [SRC-EEF2E6447C-L000036](../../api/omarai.py#L36) | 36 | `"    \"\"\"Allow only known inline blocks/attributes from the static first-party HTML."` | — |
| [SRC-EEF2E6447C-L000037](../../api/omarai.py#L37) | 37 | `""` | — |
| [SRC-EEF2E6447C-L000038](../../api/omarai.py#L38) | 38 | `"    Hashes deliberately replace unsafe-inline. Updating an inline script/style means its"` | — |
| [SRC-EEF2E6447C-L000039](../../api/omarai.py#L39) | 39 | `"    hash changes automatically with the served source. This is not a sanitizer for"` | — |
| [SRC-EEF2E6447C-L000040](../../api/omarai.py#L40) | 40 | `"    untrusted HTML; callers must never splice untrusted input into these static files."` | — |
| [SRC-EEF2E6447C-L000041](../../api/omarai.py#L41) | 41 | `"    \"\"\""` | — |
| [SRC-EEF2E6447C-L000042](../../api/omarai.py#L42) | 42 | `"    script_hashes: set[str] = set()"` | — |
| [SRC-EEF2E6447C-L000043](../../api/omarai.py#L43) | 43 | `"    style_hashes: set[str] = set()"` | — |
| [SRC-EEF2E6447C-L000044](../../api/omarai.py#L44) | 44 | `"    event_handler_hashes: set[str] = set()"` | — |
| [SRC-EEF2E6447C-L000045](../../api/omarai.py#L45) | 45 | `"    style_attribute_hashes: set[str] = set()"` | — |
| [SRC-EEF2E6447C-L000046](../../api/omarai.py#L46) | 46 | `""` | — |
| [SRC-EEF2E6447C-L000047](../../api/omarai.py#L47) | 47 | `"    for html_path in sorted(ROOT.glob(\"*.html\")):"` | — |
| [SRC-EEF2E6447C-L000048](../../api/omarai.py#L48) | 48 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000049](../../api/omarai.py#L49) | 49 | `"            document = html_path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-EEF2E6447C-L000050](../../api/omarai.py#L50) | 50 | `"        except (OSError, UnicodeError):"` | — |
| [SRC-EEF2E6447C-L000051](../../api/omarai.py#L51) | 51 | `"            continue"` | — |
| [SRC-EEF2E6447C-L000052](../../api/omarai.py#L52) | 52 | `""` | — |
| [SRC-EEF2E6447C-L000053](../../api/omarai.py#L53) | 53 | `"        for match in re.finditer("` | — |
| [SRC-EEF2E6447C-L000054](../../api/omarai.py#L54) | 54 | `"            r\"<script\\b(?P<attrs>[^>]*)>(?P<body>.*?)</script\\s*>\","` | — |
| [SRC-EEF2E6447C-L000055](../../api/omarai.py#L55) | 55 | `"            document,"` | — |
| [SRC-EEF2E6447C-L000056](../../api/omarai.py#L56) | 56 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-EEF2E6447C-L000057](../../api/omarai.py#L57) | 57 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000058](../../api/omarai.py#L58) | 58 | `"            if re.search(r\"\\bsrc\\s*=\", match.group(\"attrs\"), re.IGNORECASE):"` | — |
| [SRC-EEF2E6447C-L000059](../../api/omarai.py#L59) | 59 | `"                continue"` | — |
| [SRC-EEF2E6447C-L000060](../../api/omarai.py#L60) | 60 | `"            script_hashes.add(_csp_hash_source(match.group(\"body\")))"` | — |
| [SRC-EEF2E6447C-L000061](../../api/omarai.py#L61) | 61 | `""` | — |
| [SRC-EEF2E6447C-L000062](../../api/omarai.py#L62) | 62 | `"        for match in re.finditer("` | — |
| [SRC-EEF2E6447C-L000063](../../api/omarai.py#L63) | 63 | `"            r\"<style\\b[^>]*>(?P<body>.*?)</style\\s*>\","` | — |
| [SRC-EEF2E6447C-L000064](../../api/omarai.py#L64) | 64 | `"            document,"` | — |
| [SRC-EEF2E6447C-L000065](../../api/omarai.py#L65) | 65 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-EEF2E6447C-L000066](../../api/omarai.py#L66) | 66 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000067](../../api/omarai.py#L67) | 67 | `"            style_hashes.add(_csp_hash_source(match.group(\"body\")))"` | — |
| [SRC-EEF2E6447C-L000068](../../api/omarai.py#L68) | 68 | `""` | — |
| [SRC-EEF2E6447C-L000069](../../api/omarai.py#L69) | 69 | `"        # This scan intentionally includes style/event attributes embedded in"` | — |
| [SRC-EEF2E6447C-L000070](../../api/omarai.py#L70) | 70 | `"        # trusted first-party HTML templates assembled by inline scripts."` | — |
| [SRC-EEF2E6447C-L000071](../../api/omarai.py#L71) | 71 | `"        for match in re.finditer("` | — |
| [SRC-EEF2E6447C-L000072](../../api/omarai.py#L72) | 72 | `"            r\"\"\"\\bstyle\\s*=\\s*([\"'])(.*?)\\1\"\"\","` | — |
| [SRC-EEF2E6447C-L000073](../../api/omarai.py#L73) | 73 | `"            document,"` | — |
| [SRC-EEF2E6447C-L000074](../../api/omarai.py#L74) | 74 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-EEF2E6447C-L000075](../../api/omarai.py#L75) | 75 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000076](../../api/omarai.py#L76) | 76 | `"            style_attribute_hashes.add(_csp_hash_source(match.group(2).strip()))"` | — |
| [SRC-EEF2E6447C-L000077](../../api/omarai.py#L77) | 77 | `""` | — |
| [SRC-EEF2E6447C-L000078](../../api/omarai.py#L78) | 78 | `"        for match in re.finditer("` | — |
| [SRC-EEF2E6447C-L000079](../../api/omarai.py#L79) | 79 | `"            r\"\"\"\\bon[a-z]+\\s*=\\s*([\"'])(.*?)\\1\"\"\","` | — |
| [SRC-EEF2E6447C-L000080](../../api/omarai.py#L80) | 80 | `"            document,"` | — |
| [SRC-EEF2E6447C-L000081](../../api/omarai.py#L81) | 81 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-EEF2E6447C-L000082](../../api/omarai.py#L82) | 82 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000083](../../api/omarai.py#L83) | 83 | `"            event_handler_hashes.add(_csp_hash_source(match.group(2).strip()))"` | — |
| [SRC-EEF2E6447C-L000084](../../api/omarai.py#L84) | 84 | `""` | — |
| [SRC-EEF2E6447C-L000085](../../api/omarai.py#L85) | 85 | `"    script_sources = [\"'self'\", *sorted(script_hashes)]"` | — |
| [SRC-EEF2E6447C-L000086](../../api/omarai.py#L86) | 86 | `"    style_sources = [\"'self'\", *sorted(style_hashes)]"` | — |
| [SRC-EEF2E6447C-L000087](../../api/omarai.py#L87) | 87 | `"    if event_handler_hashes:"` | — |
| [SRC-EEF2E6447C-L000088](../../api/omarai.py#L88) | 88 | `"        script_sources.extend([\"'unsafe-hashes'\", *sorted(event_handler_hashes)])"` | — |
| [SRC-EEF2E6447C-L000089](../../api/omarai.py#L89) | 89 | `"    if style_attribute_hashes:"` | — |
| [SRC-EEF2E6447C-L000090](../../api/omarai.py#L90) | 90 | `"        style_sources.extend([\"'unsafe-hashes'\", *sorted(style_attribute_hashes)])"` | — |
| [SRC-EEF2E6447C-L000091](../../api/omarai.py#L91) | 91 | `""` | — |
| [SRC-EEF2E6447C-L000092](../../api/omarai.py#L92) | 92 | `"    return ("` | — |
| [SRC-EEF2E6447C-L000093](../../api/omarai.py#L93) | 93 | `"        \"default-src 'self'; base-uri 'self'; object-src 'none'; frame-ancestors 'none'; \""` | — |
| [SRC-EEF2E6447C-L000094](../../api/omarai.py#L94) | 94 | `"        \"form-action 'self'; connect-src 'self'; img-src 'self' data:; \""` | — |
| [SRC-EEF2E6447C-L000095](../../api/omarai.py#L95) | 95 | `"        f\"script-src {' '.join(script_sources)}; \""` | — |
| [SRC-EEF2E6447C-L000096](../../api/omarai.py#L96) | 96 | `"        f\"style-src {' '.join(style_sources)}; font-src 'self' data:\""` | — |
| [SRC-EEF2E6447C-L000097](../../api/omarai.py#L97) | 97 | `"    )"` | — |
| [SRC-EEF2E6447C-L000098](../../api/omarai.py#L98) | 98 | `"# Bound request-line + header parsing before application code or body processing."` | — |
| [SRC-EEF2E6447C-L000099](../../api/omarai.py#L99) | 99 | `"REQUEST_HEADER_READ_TIMEOUT_SECONDS = 8.0"` | — |
| [SRC-EEF2E6447C-L000100](../../api/omarai.py#L100) | 100 | `"REQUEST_HEADER_IDLE_TIMEOUT_SECONDS = 2.0"` | — |
| [SRC-EEF2E6447C-L000101](../../api/omarai.py#L101) | 101 | `"MAX_REQUEST_HEADER_READ_TIMEOUT_SECONDS = 15.0"` | — |
| [SRC-EEF2E6447C-L000102](../../api/omarai.py#L102) | 102 | `"# Absolute deadline for reading the entire body, not merely a per-read idle timeout."` | — |
| [SRC-EEF2E6447C-L000103](../../api/omarai.py#L103) | 103 | `"REQUEST_BODY_READ_TIMEOUT_SECONDS = 10.0"` | — |
| [SRC-EEF2E6447C-L000104](../../api/omarai.py#L104) | 104 | `"REQUEST_BODY_IDLE_TIMEOUT_SECONDS = 2.0"` | — |
| [SRC-EEF2E6447C-L000105](../../api/omarai.py#L105) | 105 | `"MAX_REQUEST_BODY_READ_TIMEOUT_SECONDS = 30.0"` | — |
| [SRC-EEF2E6447C-L000106](../../api/omarai.py#L106) | 106 | `"REQUEST_BODY_READ_CHUNK_BYTES = 8_192"` | — |
| [SRC-EEF2E6447C-L000107](../../api/omarai.py#L107) | 107 | `""` | — |
| [SRC-EEF2E6447C-L000108](../../api/omarai.py#L108) | 108 | `""` | — |
| [SRC-EEF2E6447C-L000109](../../api/omarai.py#L109) | 109 | `""` | — |
| [SRC-EEF2E6447C-L000110](../../api/omarai.py#L110) | 110 | `"def _lead_store_from_environment() -> LeadStore:"` | — |
| [SRC-EEF2E6447C-L000111](../../api/omarai.py#L111) | 111 | `"    \"\"\"Use an operator-configured database path when a persistent volume is available.\"\"\""` | — |
| [SRC-EEF2E6447C-L000112](../../api/omarai.py#L112) | 112 | `"    configured_path = os.getenv(\"OMARAI_DB_PATH\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000113](../../api/omarai.py#L113) | 113 | `"    return LeadStore(configured_path or None)"` | — |
| [SRC-EEF2E6447C-L000114](../../api/omarai.py#L114) | 114 | `""` | — |
| [SRC-EEF2E6447C-L000115](../../api/omarai.py#L115) | 115 | `""` | — |
| [SRC-EEF2E6447C-L000116](../../api/omarai.py#L116) | 116 | `"class _DeadlineRequestReader:"` | — |
| [SRC-EEF2E6447C-L000117](../../api/omarai.py#L117) | 117 | `"    \"\"\"Read HTTP header lines with one absolute deadline across all fragments."` | — |
| [SRC-EEF2E6447C-L000118](../../api/omarai.py#L118) | 118 | `""` | — |
| [SRC-EEF2E6447C-L000119](../../api/omarai.py#L119) | 119 | `"    The standard buffered readline can wait indefinitely for a newline if a"` | — |
| [SRC-EEF2E6447C-L000120](../../api/omarai.py#L120) | 120 | `"    client keeps trickling bytes. This reader checks the same deadline before"` | — |
| [SRC-EEF2E6447C-L000121](../../api/omarai.py#L121) | 121 | `"    every socket read and buffers only bounded look-ahead so request body bytes"` | — |
| [SRC-EEF2E6447C-L000122](../../api/omarai.py#L122) | 122 | `"    received with the headers are preserved for read1()."` | — |
| [SRC-EEF2E6447C-L000123](../../api/omarai.py#L123) | 123 | `"    \"\"\""` | — |
| [SRC-EEF2E6447C-L000124](../../api/omarai.py#L124) | 124 | `""` | — |
| [SRC-EEF2E6447C-L000125](../../api/omarai.py#L125) | 125 | `"    def __init__(self, connection, handler):"` | — |
| [SRC-EEF2E6447C-L000126](../../api/omarai.py#L126) | 126 | `"        self.connection = connection"` | — |
| [SRC-EEF2E6447C-L000127](../../api/omarai.py#L127) | 127 | `"        self.handler = handler"` | — |
| [SRC-EEF2E6447C-L000128](../../api/omarai.py#L128) | 128 | `"        self._buffer = bytearray()"` | — |
| [SRC-EEF2E6447C-L000129](../../api/omarai.py#L129) | 129 | `""` | — |
| [SRC-EEF2E6447C-L000130](../../api/omarai.py#L130) | 130 | `"    def readline(self, limit=-1):"` | — |
| [SRC-EEF2E6447C-L000131](../../api/omarai.py#L131) | 131 | `"        if limit == 0:"` | — |
| [SRC-EEF2E6447C-L000132](../../api/omarai.py#L132) | 132 | `"            return b\"\""` | — |
| [SRC-EEF2E6447C-L000133](../../api/omarai.py#L133) | 133 | `"        max_bytes = int(limit) if limit is not None and limit > 0 else 65_537"` | — |
| [SRC-EEF2E6447C-L000134](../../api/omarai.py#L134) | 134 | `"        previous_timeout = self.connection.gettimeout()"` | — |
| [SRC-EEF2E6447C-L000135](../../api/omarai.py#L135) | 135 | `"        line = bytearray()"` | — |
| [SRC-EEF2E6447C-L000136](../../api/omarai.py#L136) | 136 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000137](../../api/omarai.py#L137) | 137 | `"            while len(line) < max_bytes:"` | — |
| [SRC-EEF2E6447C-L000138](../../api/omarai.py#L138) | 138 | `"                deadline = getattr(self.handler, \"_request_header_deadline\", None)"` | — |
| [SRC-EEF2E6447C-L000139](../../api/omarai.py#L139) | 139 | `"                if deadline is None:"` | — |
| [SRC-EEF2E6447C-L000140](../../api/omarai.py#L140) | 140 | `"                    raise TimeoutError(\"request-header deadline is not active\")"` | — |
| [SRC-EEF2E6447C-L000141](../../api/omarai.py#L141) | 141 | `"                remaining = deadline - time.monotonic()"` | — |
| [SRC-EEF2E6447C-L000142](../../api/omarai.py#L142) | 142 | `"                if remaining <= 0:"` | — |
| [SRC-EEF2E6447C-L000143](../../api/omarai.py#L143) | 143 | `"                    raise TimeoutError(\"absolute request-header deadline exceeded\")"` | — |
| [SRC-EEF2E6447C-L000144](../../api/omarai.py#L144) | 144 | `""` | — |
| [SRC-EEF2E6447C-L000145](../../api/omarai.py#L145) | 145 | `"                newline_index = self._buffer.find(b\"\\n\")"` | — |
| [SRC-EEF2E6447C-L000146](../../api/omarai.py#L146) | 146 | `"                if newline_index >= 0:"` | — |
