# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **013**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L005739 إلى SRC-EEF2E6447C-L000535
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L005739](../../agents/web_agent.py#L5739) | 5739 | `"                            review_status = \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005740](../../agents/web_agent.py#L5740) | 5740 | `"                        except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L005741](../../agents/web_agent.py#L5741) | 5741 | `"                            review_status = \"model_claim_audit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L005742](../../agents/web_agent.py#L5742) | 5742 | `"                            review_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L005743](../../agents/web_agent.py#L5743) | 5743 | `"                            coverage_repair_status = ("` | — |
| [SRC-1AE03B9EC3-L005744](../../agents/web_agent.py#L5744) | 5744 | `"                                \"reaudit_budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L005745](../../agents/web_agent.py#L5745) | 5745 | `"                                if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L005746](../../agents/web_agent.py#L5746) | 5746 | `"                                else \"reaudit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L005747](../../agents/web_agent.py#L5747) | 5747 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L005748](../../agents/web_agent.py#L5748) | 5748 | `"                            review_warning = ("` | — |
| [SRC-1AE03B9EC3-L005749](../../agents/web_agent.py#L5749) | 5749 | `"                                \"استُنفدت ميزانية النماذج قبل إعادة تدقيق الإجابة المعدلة؛ \""` | — |
| [SRC-1AE03B9EC3-L005750](../../agents/web_agent.py#L5750) | 5750 | `"                                \"لذلك لن أعرض النص المعدل بوصفه إجابة مكتملة، وأعرض مقتطفات المصادر بدلًا منه.\""` | — |
| [SRC-1AE03B9EC3-L005751](../../agents/web_agent.py#L5751) | 5751 | `"                                if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L005752](../../agents/web_agent.py#L5752) | 5752 | `"                                else"` | — |
| [SRC-1AE03B9EC3-L005753](../../agents/web_agent.py#L5753) | 5753 | `"                                \"تعذرت إعادة تدقيق الإجابة المعدلة مقابل الأدلة؛ لذلك لن أعرضها بوصفها إجابة مكتملة، \""` | — |
| [SRC-1AE03B9EC3-L005754](../../agents/web_agent.py#L5754) | 5754 | `"                                \"وأعرض مقتطفات المصادر بدلًا منها.\""` | — |
| [SRC-1AE03B9EC3-L005755](../../agents/web_agent.py#L5755) | 5755 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L005756](../../agents/web_agent.py#L5756) | 5756 | `"                            answer = _fallback_answer(sources, review_warning)"` | — |
| [SRC-1AE03B9EC3-L005757](../../agents/web_agent.py#L5757) | 5757 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L005758](../../agents/web_agent.py#L5758) | 5758 | `"                        coverage_repair_status = \"no_change_gap_unresolved\""` | — |
| [SRC-1AE03B9EC3-L005759](../../agents/web_agent.py#L5759) | 5759 | `"                        coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L005760](../../agents/web_agent.py#L5760) | 5760 | `"                            \"رصد الفحص اللفظي محورًا قد يكون ناقصًا، لكن محاولة الإصلاح لم تغيّر الإجابة؛ \""` | — |
| [SRC-1AE03B9EC3-L005761](../../agents/web_agent.py#L5761) | 5761 | `"                            \"تحقق من تغطية هذا المحور يدويًا.\""` | — |
| [SRC-1AE03B9EC3-L005762](../../agents/web_agent.py#L5762) | 5762 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005763](../../agents/web_agent.py#L5763) | 5763 | `"                except RequestBudgetExceeded:"` | — |
| [SRC-1AE03B9EC3-L005764](../../agents/web_agent.py#L5764) | 5764 | `"                    coverage_repair_status = \"budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L005765](../../agents/web_agent.py#L5765) | 5765 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L005766](../../agents/web_agent.py#L5766) | 5766 | `"                        \"استُنفدت ميزانية النماذج قبل محاولة إصلاح محور قد يكون ناقصًا؛ \""` | — |
| [SRC-1AE03B9EC3-L005767](../../agents/web_agent.py#L5767) | 5767 | `"                        \"لا تعتبر التغطية مكتملة دون مراجعة المحور المذكور.\""` | — |
| [SRC-1AE03B9EC3-L005768](../../agents/web_agent.py#L5768) | 5768 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005769](../../agents/web_agent.py#L5769) | 5769 | `"                except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L005770](../../agents/web_agent.py#L5770) | 5770 | `"                    coverage_repair_status = \"unavailable\""` | — |
| [SRC-1AE03B9EC3-L005771](../../agents/web_agent.py#L5771) | 5771 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L005772](../../agents/web_agent.py#L5772) | 5772 | `"                        \"تعذرت محاولة إصلاح محور قد يكون ناقصًا (\""` | — |
| [SRC-1AE03B9EC3-L005773](../../agents/web_agent.py#L5773) | 5773 | `"                        + type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L005774](../../agents/web_agent.py#L5774) | 5774 | `"                        + \")؛ راجع المحاور المطلوبة قبل اعتماد الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L005775](../../agents/web_agent.py#L5775) | 5775 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005776](../../agents/web_agent.py#L5776) | 5776 | `"        elif coverage_targets and review_status == \"model_claim_audit_completed\" and not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L005777](../../agents/web_agent.py#L5777) | 5777 | `"            coverage_repair_status = \"skipped_no_model_configuration\""` | — |
| [SRC-1AE03B9EC3-L005778](../../agents/web_agent.py#L5778) | 5778 | `"        elif coverage_targets:"` | — |
| [SRC-1AE03B9EC3-L005779](../../agents/web_agent.py#L5779) | 5779 | `"            coverage_repair_status = \"skipped_review_unavailable\""` | — |
| [SRC-1AE03B9EC3-L005780](../../agents/web_agent.py#L5780) | 5780 | `""` | — |
| [SRC-1AE03B9EC3-L005781](../../agents/web_agent.py#L5781) | 5781 | `"        if self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L005782](../../agents/web_agent.py#L5782) | 5782 | `"            answer += \"\\n\\nروابط إضافية من البحث المباشر عبر الويب:\""` | — |
| [SRC-1AE03B9EC3-L005783](../../agents/web_agent.py#L5783) | 5783 | `"            for source in self.server_search_sources[:8]:"` | — |
| [SRC-1AE03B9EC3-L005784](../../agents/web_agent.py#L5784) | 5784 | `"                answer += \"\\n- \" + source[\"title\"] + \" — \" + source[\"url\"]"` | — |
| [SRC-1AE03B9EC3-L005785](../../agents/web_agent.py#L5785) | 5785 | `"        max_citable_sources = min(MAX_LLM_CITED_SOURCES, len(sources))"` | — |
| [SRC-1AE03B9EC3-L005786](../../agents/web_agent.py#L5786) | 5786 | `"        answer, citation_warnings = self._remove_invalid_citations("` | — |
| [SRC-1AE03B9EC3-L005787](../../agents/web_agent.py#L5787) | 5787 | `"            answer, max_citable_sources"` | — |
| [SRC-1AE03B9EC3-L005788](../../agents/web_agent.py#L5788) | 5788 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005789](../../agents/web_agent.py#L5789) | 5789 | `"        citation_validation = self._citation_validation_metadata("` | — |
| [SRC-1AE03B9EC3-L005790](../../agents/web_agent.py#L5790) | 5790 | `"            answer, max_citable_sources, citation_warnings, review_status"` | — |
| [SRC-1AE03B9EC3-L005791](../../agents/web_agent.py#L5791) | 5791 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005792](../../agents/web_agent.py#L5792) | 5792 | `"        report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005793](../../agents/web_agent.py#L5793) | 5793 | `"        report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L005794](../../agents/web_agent.py#L5794) | 5794 | `"        report[\"second_pass_review\"] = review_status"` | — |
| [SRC-1AE03B9EC3-L005795](../../agents/web_agent.py#L5795) | 5795 | `"        report[\"claim_audit\"] = review_status"` | — |
| [SRC-1AE03B9EC3-L005796](../../agents/web_agent.py#L5796) | 5796 | `"        answer_coverage = {"` | — |
| [SRC-1AE03B9EC3-L005797](../../agents/web_agent.py#L5797) | 5797 | `"            \"method\": \"explicit_criteria_heuristic\","` | — |
| [SRC-1AE03B9EC3-L005798](../../agents/web_agent.py#L5798) | 5798 | `"            \"targets\": coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L005799](../../agents/web_agent.py#L5799) | 5799 | `"            \"review_prompted\": review_status == \"model_claim_audit_completed\","` | — |
| [SRC-1AE03B9EC3-L005800](../../agents/web_agent.py#L5800) | 5800 | `"            \"status\": ("` | — |
| [SRC-1AE03B9EC3-L005801](../../agents/web_agent.py#L5801) | 5801 | `"                \"model_review_requested_not_machine_verified\""` | — |
| [SRC-1AE03B9EC3-L005802](../../agents/web_agent.py#L5802) | 5802 | `"                if coverage_targets and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005803](../../agents/web_agent.py#L5803) | 5803 | `"                else \"review_unavailable\""` | — |
| [SRC-1AE03B9EC3-L005804](../../agents/web_agent.py#L5804) | 5804 | `"                if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L005805](../../agents/web_agent.py#L5805) | 5805 | `"                else \"no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L005806](../../agents/web_agent.py#L5806) | 5806 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L005807](../../agents/web_agent.py#L5807) | 5807 | `"            \"automatically_graded\": False,"` | — |
| [SRC-1AE03B9EC3-L005808](../../agents/web_agent.py#L5808) | 5808 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005809](../../agents/web_agent.py#L5809) | 5809 | `"        report[\"answer_coverage\"] = answer_coverage"` | — |
| [SRC-1AE03B9EC3-L005810](../../agents/web_agent.py#L5810) | 5810 | `"        report[\"coverage_repair_status\"] = coverage_repair_status"` | — |
| [SRC-1AE03B9EC3-L005811](../../agents/web_agent.py#L5811) | 5811 | `"        answer_integrity = audit_answer_integrity(working_question, answer, sources, coverage_targets)"` | — |
| [SRC-1AE03B9EC3-L005812](../../agents/web_agent.py#L5812) | 5812 | `"        answer_coverage[\"target_checks\"] = answer_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L005813](../../agents/web_agent.py#L5813) | 5813 | `"        answer_coverage[\"potentially_missing_target_count\"] = answer_integrity[\"potentially_missing_target_count\"]"` | — |
| [SRC-1AE03B9EC3-L005814](../../agents/web_agent.py#L5814) | 5814 | `"        answer_coverage[\"source_evidence_gap_count\"] = answer_integrity[\"source_evidence_gap_count\"]"` | — |
| [SRC-1AE03B9EC3-L005815](../../agents/web_agent.py#L5815) | 5815 | `"        answer_coverage[\"lexical_screen_method\"] = \"deterministic_lexical_screen_only_not_semantic_grading\""` | — |
| [SRC-1AE03B9EC3-L005816](../../agents/web_agent.py#L5816) | 5816 | `"        task_fulfillment_status = ("` | — |
| [SRC-1AE03B9EC3-L005817](../../agents/web_agent.py#L5817) | 5817 | `"            \"possible_gap_detected\""` | — |
| [SRC-1AE03B9EC3-L005818](../../agents/web_agent.py#L5818) | 5818 | `"            if ("` | — |
| [SRC-1AE03B9EC3-L005819](../../agents/web_agent.py#L5819) | 5819 | `"                answer_integrity[\"potentially_missing_target_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L005820](../../agents/web_agent.py#L5820) | 5820 | `"                or answer_integrity[\"source_evidence_gap_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L005821](../../agents/web_agent.py#L5821) | 5821 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005822](../../agents/web_agent.py#L5822) | 5822 | `"            else \"lexical_signals_found_not_semantically_verified\" if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L005823](../../agents/web_agent.py#L5823) | 5823 | `"            else \"not_machine_assessed_no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L005824](../../agents/web_agent.py#L5824) | 5824 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005825](../../agents/web_agent.py#L5825) | 5825 | `"        answer_coverage[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L005826](../../agents/web_agent.py#L5826) | 5826 | `"        report[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L005827](../../agents/web_agent.py#L5827) | 5827 | `"        report[\"answer_integrity\"] = answer_integrity"` | — |
| [SRC-1AE03B9EC3-L005828](../../agents/web_agent.py#L5828) | 5828 | `"        report[\"connector_summary\"] = self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L005829](../../agents/web_agent.py#L5829) | 5829 | `"            list(self._provider_diagnostics), sources"` | — |
| [SRC-1AE03B9EC3-L005830](../../agents/web_agent.py#L5830) | 5830 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005831](../../agents/web_agent.py#L5831) | 5831 | `"        report[\"provider_diagnostics\"] = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L005832](../../agents/web_agent.py#L5832) | 5832 | `"        distinct_providers = {"` | — |
| [SRC-1AE03B9EC3-L005833](../../agents/web_agent.py#L5833) | 5833 | `"            provider for source in sources for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L005834](../../agents/web_agent.py#L5834) | 5834 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005835](../../agents/web_agent.py#L5835) | 5835 | `"        distinct_domains = {"` | — |
| [SRC-1AE03B9EC3-L005836](../../agents/web_agent.py#L5836) | 5836 | `"            registrable_domain("` | — |
| [SRC-1AE03B9EC3-L005837](../../agents/web_agent.py#L5837) | 5837 | `"                source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L005838](../../agents/web_agent.py#L5838) | 5838 | `"                or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L005839](../../agents/web_agent.py#L5839) | 5839 | `"                or \"\""` | — |
| [SRC-1AE03B9EC3-L005840](../../agents/web_agent.py#L5840) | 5840 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005841](../../agents/web_agent.py#L5841) | 5841 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L005842](../../agents/web_agent.py#L5842) | 5842 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005843](../../agents/web_agent.py#L5843) | 5843 | `"        distinct_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L005844](../../agents/web_agent.py#L5844) | 5844 | `"        fetched_pages = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L005845](../../agents/web_agent.py#L5845) | 5845 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L005846](../../agents/web_agent.py#L5846) | 5846 | `"            len(sources) >= 4 and len(distinct_domains) >= 3"` | — |
| [SRC-1AE03B9EC3-L005847](../../agents/web_agent.py#L5847) | 5847 | `"            and len(distinct_providers) >= 2 and fetched_pages >= 1"` | — |
| [SRC-1AE03B9EC3-L005848](../../agents/web_agent.py#L5848) | 5848 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005849](../../agents/web_agent.py#L5849) | 5849 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L005850](../../agents/web_agent.py#L5850) | 5850 | `"            research_quality = \"excellent\""` | — |
| [SRC-1AE03B9EC3-L005851](../../agents/web_agent.py#L5851) | 5851 | `"        elif ("` | — |
| [SRC-1AE03B9EC3-L005852](../../agents/web_agent.py#L5852) | 5852 | `"            len(sources) >= 2 and len(distinct_domains) >= 2"` | — |
| [SRC-1AE03B9EC3-L005853](../../agents/web_agent.py#L5853) | 5853 | `"            and (len(distinct_providers) >= 2 or fetched_pages >= 1)"` | — |
| [SRC-1AE03B9EC3-L005854](../../agents/web_agent.py#L5854) | 5854 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005855](../../agents/web_agent.py#L5855) | 5855 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L005856](../../agents/web_agent.py#L5856) | 5856 | `"            research_quality = \"good\""` | — |
| [SRC-1AE03B9EC3-L005857](../../agents/web_agent.py#L5857) | 5857 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L005858](../../agents/web_agent.py#L5858) | 5858 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L005859](../../agents/web_agent.py#L5859) | 5859 | `""` | — |
| [SRC-1AE03B9EC3-L005860](../../agents/web_agent.py#L5860) | 5860 | `"        # Source breadth and a completed model-assisted review do not justify a"` | — |
| [SRC-1AE03B9EC3-L005861](../../agents/web_agent.py#L5861) | 5861 | `"        # positive research-quality label if the final answer has no valid source"` | — |
| [SRC-1AE03B9EC3-L005862](../../agents/web_agent.py#L5862) | 5862 | `"        # citation markers. This is a deterministic presentation guard, not a"` | — |
| [SRC-1AE03B9EC3-L005863](../../agents/web_agent.py#L5863) | 5863 | `"        # semantic entailment check."` | — |
| [SRC-1AE03B9EC3-L005864](../../agents/web_agent.py#L5864) | 5864 | `"        uncited_reviewed_answer = ("` | — |
| [SRC-1AE03B9EC3-L005865](../../agents/web_agent.py#L5865) | 5865 | `"            used_llm"` | — |
| [SRC-1AE03B9EC3-L005866](../../agents/web_agent.py#L5866) | 5866 | `"            and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L005867](../../agents/web_agent.py#L5867) | 5867 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005868](../../agents/web_agent.py#L5868) | 5868 | `"            and citation_validation[\"valid_citation_count\"] == 0"` | — |
| [SRC-1AE03B9EC3-L005869](../../agents/web_agent.py#L5869) | 5869 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005870](../../agents/web_agent.py#L5870) | 5870 | `"        if uncited_reviewed_answer:"` | — |
| [SRC-1AE03B9EC3-L005871](../../agents/web_agent.py#L5871) | 5871 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L005872](../../agents/web_agent.py#L5872) | 5872 | `"            citation_validation[\"claim_support\"] = \"not_established_no_valid_source_citations\""` | — |
| [SRC-1AE03B9EC3-L005873](../../agents/web_agent.py#L5873) | 5873 | `"            answer_evidence_status = \"reviewed_answer_has_no_valid_citations\""` | — |
| [SRC-1AE03B9EC3-L005874](../../agents/web_agent.py#L5874) | 5874 | `"            uncited_answer_warning = ("` | — |
| [SRC-1AE03B9EC3-L005875](../../agents/web_agent.py#L5875) | 5875 | `"                \"اكتملت مراجعة النموذج، لكن الإجابة النهائية لا تحتوي على إحالات صالحة \""` | — |
| [SRC-1AE03B9EC3-L005876](../../agents/web_agent.py#L5876) | 5876 | `"                \"إلى قائمة المصادر؛ لذلك صُنّفت جودة البحث «جزئية». وجود المصادر أو \""` | — |
| [SRC-1AE03B9EC3-L005877](../../agents/web_agent.py#L5877) | 5877 | `"                \"اكتمال مراجعة النموذج لا يثبت دعم كل ادعاء.\""` | — |
| [SRC-1AE03B9EC3-L005878](../../agents/web_agent.py#L5878) | 5878 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005879](../../agents/web_agent.py#L5879) | 5879 | `"        elif citation_validation[\"valid_citation_count\"] > 0:"` | — |
| [SRC-1AE03B9EC3-L005880](../../agents/web_agent.py#L5880) | 5880 | `"            answer_evidence_status = \"citation_indices_validated_only\""` | — |
| [SRC-1AE03B9EC3-L005881](../../agents/web_agent.py#L5881) | 5881 | `"            uncited_answer_warning = None"` | — |
| [SRC-1AE03B9EC3-L005882](../../agents/web_agent.py#L5882) | 5882 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L005883](../../agents/web_agent.py#L5883) | 5883 | `"            answer_evidence_status = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L005884](../../agents/web_agent.py#L5884) | 5884 | `"            uncited_answer_warning = None"` | — |
| [SRC-1AE03B9EC3-L005885](../../agents/web_agent.py#L5885) | 5885 | `""` | — |
| [SRC-1AE03B9EC3-L005886](../../agents/web_agent.py#L5886) | 5886 | `"        search_attempted = search_attempted or bool(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L005887](../../agents/web_agent.py#L5887) | 5887 | `"        report[\"search_attempted\"] = search_attempted"` | — |
| [SRC-1AE03B9EC3-L005888](../../agents/web_agent.py#L5888) | 5888 | `"        report[\"search_outcome\"] = ("` | — |
| [SRC-1AE03B9EC3-L005889](../../agents/web_agent.py#L5889) | 5889 | `"            \"attempted_with_usable_sources\" if search_attempted and sources"` | — |
| [SRC-1AE03B9EC3-L005890](../../agents/web_agent.py#L5890) | 5890 | `"            else \"attempted_no_usable_sources\" if search_attempted"` | — |
| [SRC-1AE03B9EC3-L005891](../../agents/web_agent.py#L5891) | 5891 | `"            else \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L005892](../../agents/web_agent.py#L5892) | 5892 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005893](../../agents/web_agent.py#L5893) | 5893 | `"        report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005894](../../agents/web_agent.py#L5894) | 5894 | `"        report[\"research_quality\"] = research_quality"` | — |
| [SRC-1AE03B9EC3-L005895](../../agents/web_agent.py#L5895) | 5895 | `"        report[\"research_quality_semantics\"] = \"process_coverage_not_factual_probability\""` | — |
| [SRC-1AE03B9EC3-L005896](../../agents/web_agent.py#L5896) | 5896 | `"        report[\"answer_evidence_status\"] = answer_evidence_status"` | — |
| [SRC-1AE03B9EC3-L005897](../../agents/web_agent.py#L5897) | 5897 | `"        report[\"distinct_registrable_domains\"] = len(distinct_domains)"` | — |
| [SRC-1AE03B9EC3-L005898](../../agents/web_agent.py#L5898) | 5898 | `"        report[\"independent_sources\"] = len(distinct_domains)  # Legacy alias; not editorial independence."` | — |
| [SRC-1AE03B9EC3-L005899](../../agents/web_agent.py#L5899) | 5899 | `"        report[\"independent_sources_field_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L005900](../../agents/web_agent.py#L5900) | 5900 | `"            \"legacy_compatibility_alias_for_distinct_registrable_domain_count\""` | — |
| [SRC-1AE03B9EC3-L005901](../../agents/web_agent.py#L5901) | 5901 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005902](../../agents/web_agent.py#L5902) | 5902 | `"        report[\"source_diversity_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L005903](../../agents/web_agent.py#L5903) | 5903 | `"            \"distinct_registrable_domains_not_editorial_independence\""` | — |
| [SRC-1AE03B9EC3-L005904](../../agents/web_agent.py#L5904) | 5904 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005905](../../agents/web_agent.py#L5905) | 5905 | `"        report[\"editorial_independence_status\"] = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L005906](../../agents/web_agent.py#L5906) | 5906 | `"        report[\"claim_audit_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L005907](../../agents/web_agent.py#L5907) | 5907 | `"            \"model_assisted_not_independent_fact_check\""` | — |
| [SRC-1AE03B9EC3-L005908](../../agents/web_agent.py#L5908) | 5908 | `"            if review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005909](../../agents/web_agent.py#L5909) | 5909 | `"            else \"not_verified\""` | — |
| [SRC-1AE03B9EC3-L005910](../../agents/web_agent.py#L5910) | 5910 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005911](../../agents/web_agent.py#L5911) | 5911 | `"        report[\"insufficient_evidence\"] = False"` | — |
| [SRC-1AE03B9EC3-L005912](../../agents/web_agent.py#L5912) | 5912 | `"        report[\"valid_citation_range\"] = [1, max_citable_sources] if max_citable_sources else []"` | — |
| [SRC-1AE03B9EC3-L005913](../../agents/web_agent.py#L5913) | 5913 | `"        report[\"citation_count\"] = citation_validation[\"valid_citation_count\"]"` | — |
| [SRC-1AE03B9EC3-L005914](../../agents/web_agent.py#L5914) | 5914 | `"        report[\"citation_check\"] = citation_validation[\"status\"]"` | — |
| [SRC-1AE03B9EC3-L005915](../../agents/web_agent.py#L5915) | 5915 | `"        report[\"citation_validation\"] = citation_validation"` | — |
| [SRC-1AE03B9EC3-L005916](../../agents/web_agent.py#L5916) | 5916 | `"        warnings = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L005917](../../agents/web_agent.py#L5917) | 5917 | `"            search_warnings"` | — |
| [SRC-1AE03B9EC3-L005918](../../agents/web_agent.py#L5918) | 5918 | `"            + ([llm_warning] if llm_warning else [])"` | — |
| [SRC-1AE03B9EC3-L005919](../../agents/web_agent.py#L5919) | 5919 | `"            + ([review_warning] if review_warning else [])"` | — |
| [SRC-1AE03B9EC3-L005920](../../agents/web_agent.py#L5920) | 5920 | `"            + ([coverage_repair_warning] if coverage_repair_warning else [])"` | — |
| [SRC-1AE03B9EC3-L005921](../../agents/web_agent.py#L5921) | 5921 | `"            + citation_warnings"` | — |
| [SRC-1AE03B9EC3-L005922](../../agents/web_agent.py#L5922) | 5922 | `"            + ([uncited_answer_warning] if uncited_answer_warning else [])"` | — |
| [SRC-1AE03B9EC3-L005923](../../agents/web_agent.py#L5923) | 5923 | `"        ))"` | — |
| [SRC-1AE03B9EC3-L005924](../../agents/web_agent.py#L5924) | 5924 | `"        report[\"model_calls\"] = list(self.model_usage)"` | — |
| [SRC-1AE03B9EC3-L005925](../../agents/web_agent.py#L5925) | 5925 | `"        report[\"openrouter_web_search_enabled\"] = self.openrouter_web_search_enabled"` | — |
| [SRC-1AE03B9EC3-L005926](../../agents/web_agent.py#L5926) | 5926 | `"        report[\"openrouter_web_search_results\"] = len(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L005927](../../agents/web_agent.py#L5927) | 5927 | `"        if generation_budget_exhausted or review_budget_exhausted:"` | — |
| [SRC-1AE03B9EC3-L005928](../../agents/web_agent.py#L5928) | 5928 | `"            final_answer_status = \"budget_exhausted_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L005929](../../agents/web_agent.py#L5929) | 5929 | `"        elif llm_warning:"` | — |
| [SRC-1AE03B9EC3-L005930](../../agents/web_agent.py#L5930) | 5930 | `"            final_answer_status = ("` | — |
| [SRC-1AE03B9EC3-L005931](../../agents/web_agent.py#L5931) | 5931 | `"                \"model_not_configured_fallback\""` | — |
| [SRC-1AE03B9EC3-L005932](../../agents/web_agent.py#L5932) | 5932 | `"                if not self.api_key"` | — |
| [SRC-1AE03B9EC3-L005933](../../agents/web_agent.py#L5933) | 5933 | `"                else \"generation_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L005934](../../agents/web_agent.py#L5934) | 5934 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005935](../../agents/web_agent.py#L5935) | 5935 | `"        elif review_warning:"` | — |
| [SRC-1AE03B9EC3-L005936](../../agents/web_agent.py#L5936) | 5936 | `"            final_answer_status = \"review_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L005937](../../agents/web_agent.py#L5937) | 5937 | `"        elif coverage_repair_status == \"no_change_gap_unresolved\":"` | — |
| [SRC-1AE03B9EC3-L005938](../../agents/web_agent.py#L5938) | 5938 | `"            final_answer_status = \"coverage_repair_left_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L005939](../../agents/web_agent.py#L5939) | 5939 | `"        elif coverage_repair_status == \"budget_exhausted\":"` | — |
| [SRC-1AE03B9EC3-L005940](../../agents/web_agent.py#L5940) | 5940 | `"            final_answer_status = \"coverage_repair_budget_exhausted_with_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L005941](../../agents/web_agent.py#L5941) | 5941 | `"        elif coverage_repair_status == \"unavailable\":"` | — |
| [SRC-1AE03B9EC3-L005942](../../agents/web_agent.py#L5942) | 5942 | `"            final_answer_status = \"coverage_repair_unavailable_with_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L005943](../../agents/web_agent.py#L5943) | 5943 | `"        elif used_llm:"` | — |
| [SRC-1AE03B9EC3-L005944](../../agents/web_agent.py#L5944) | 5944 | `"            final_answer_status = \"model_answer_generated\""` | — |
| [SRC-1AE03B9EC3-L005945](../../agents/web_agent.py#L5945) | 5945 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L005946](../../agents/web_agent.py#L5946) | 5946 | `"            final_answer_status = \"source_fallback\""` | — |
| [SRC-1AE03B9EC3-L005947](../../agents/web_agent.py#L5947) | 5947 | `""` | — |
| [SRC-1AE03B9EC3-L005948](../../agents/web_agent.py#L5948) | 5948 | `"        public_sources = []"` | — |
| [SRC-1AE03B9EC3-L005949](../../agents/web_agent.py#L5949) | 5949 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L005950](../../agents/web_agent.py#L5950) | 5950 | `"            public_sources.append({"` | — |
| [SRC-1AE03B9EC3-L005951](../../agents/web_agent.py#L5951) | 5951 | `"                \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L005952](../../agents/web_agent.py#L5952) | 5952 | `"                \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L005953](../../agents/web_agent.py#L5953) | 5953 | `"                \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005954](../../agents/web_agent.py#L5954) | 5954 | `"                \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L005955](../../agents/web_agent.py#L5955) | 5955 | `"                \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L005956](../../agents/web_agent.py#L5956) | 5956 | `"                \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L005957](../../agents/web_agent.py#L5957) | 5957 | `"                \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L005958](../../agents/web_agent.py#L5958) | 5958 | `"                \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005959](../../agents/web_agent.py#L5959) | 5959 | `"                \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L005960](../../agents/web_agent.py#L5960) | 5960 | `"                \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005961](../../agents/web_agent.py#L5961) | 5961 | `"                \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005962](../../agents/web_agent.py#L5962) | 5962 | `"                \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005963](../../agents/web_agent.py#L5963) | 5963 | `"                \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L005964](../../agents/web_agent.py#L5964) | 5964 | `"                \"lead_qualification\": source.get(\"lead_qualification\"),"` | — |
| [SRC-1AE03B9EC3-L005965](../../agents/web_agent.py#L5965) | 5965 | `"                \"lead_intent_evidence\": source.get(\"lead_intent_evidence\"),"` | — |
| [SRC-1AE03B9EC3-L005966](../../agents/web_agent.py#L5966) | 5966 | `"            })"` | — |
| [SRC-1AE03B9EC3-L005967](../../agents/web_agent.py#L5967) | 5967 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L005968](../../agents/web_agent.py#L5968) | 5968 | `"            \"answer\": answer,"` | — |
| [SRC-1AE03B9EC3-L005969](../../agents/web_agent.py#L5969) | 5969 | `"            \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L005970](../../agents/web_agent.py#L5970) | 5970 | `"            \"search_query\": (plan.get(\"queries\") or [\"\"])[0],"` | — |
| [SRC-1AE03B9EC3-L005971](../../agents/web_agent.py#L5971) | 5971 | `"            \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L005972](../../agents/web_agent.py#L5972) | 5972 | `"            \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L005973](../../agents/web_agent.py#L5973) | 5973 | `"                \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L005974](../../agents/web_agent.py#L5974) | 5974 | `"                \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L005975](../../agents/web_agent.py#L5975) | 5975 | `"                \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L005976](../../agents/web_agent.py#L5976) | 5976 | `"                \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L005977](../../agents/web_agent.py#L5977) | 5977 | `"                \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L005978](../../agents/web_agent.py#L5978) | 5978 | `"                \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L005979](../../agents/web_agent.py#L5979) | 5979 | `"                \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L005980](../../agents/web_agent.py#L5980) | 5980 | `"                \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L005981](../../agents/web_agent.py#L5981) | 5981 | `"                \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L005982](../../agents/web_agent.py#L5982) | 5982 | `"                \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L005983](../../agents/web_agent.py#L5983) | 5983 | `"            },"` | — |
| [SRC-1AE03B9EC3-L005984](../../agents/web_agent.py#L5984) | 5984 | `"            \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L005985](../../agents/web_agent.py#L5985) | 5985 | `"            \"sources\": public_sources,"` | — |
| [SRC-1AE03B9EC3-L005986](../../agents/web_agent.py#L5986) | 5986 | `"            \"research_quality\": research_quality,"` | — |
| [SRC-1AE03B9EC3-L005987](../../agents/web_agent.py#L5987) | 5987 | `"            \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L005988](../../agents/web_agent.py#L5988) | 5988 | `"            \"answer_evidence_status\": answer_evidence_status,"` | — |
| [SRC-1AE03B9EC3-L005989](../../agents/web_agent.py#L5989) | 5989 | `"            \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L005990](../../agents/web_agent.py#L5990) | 5990 | `"            \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L005991](../../agents/web_agent.py#L5991) | 5991 | `"            \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L005992](../../agents/web_agent.py#L5992) | 5992 | `"            \"coverage_repair_status\": coverage_repair_status,"` | — |
| [SRC-1AE03B9EC3-L005993](../../agents/web_agent.py#L5993) | 5993 | `"            \"used_language_model\": used_llm,"` | — |
| [SRC-1AE03B9EC3-L005994](../../agents/web_agent.py#L5994) | 5994 | `"            \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L005995](../../agents/web_agent.py#L5995) | 5995 | `"            \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L005996](../../agents/web_agent.py#L5996) | 5996 | `"            \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L005997](../../agents/web_agent.py#L5997) | 5997 | `"            \"warnings\": warnings,"` | — |
| [SRC-1AE03B9EC3-L005998](../../agents/web_agent.py#L5998) | 5998 | `"            \"kind\": \"web_research\" if used_llm else \"web_fallback\","` | — |
| [SRC-1AE03B9EC3-L005999](../../agents/web_agent.py#L5999) | 5999 | `"            \"final_answer_status\": final_answer_status,"` | — |
| [SRC-1AE03B9EC3-L006000](../../agents/web_agent.py#L6000) | 6000 | `"            \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L006001](../../agents/web_agent.py#L6001) | 6001 | `"            \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L006002](../../agents/web_agent.py#L6002) | 6002 | `"        }"` | — |
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
| [SRC-EEF2E6447C-L000147](../../api/omarai.py#L147) | 147 | `"                    take = min(newline_index + 1, max_bytes - len(line))"` | — |
| [SRC-EEF2E6447C-L000148](../../api/omarai.py#L148) | 148 | `"                    line.extend(self._buffer[:take])"` | — |
| [SRC-EEF2E6447C-L000149](../../api/omarai.py#L149) | 149 | `"                    del self._buffer[:take]"` | — |
| [SRC-EEF2E6447C-L000150](../../api/omarai.py#L150) | 150 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000151](../../api/omarai.py#L151) | 151 | `""` | — |
| [SRC-EEF2E6447C-L000152](../../api/omarai.py#L152) | 152 | `"                if self._buffer:"` | — |
| [SRC-EEF2E6447C-L000153](../../api/omarai.py#L153) | 153 | `"                    take = min(len(self._buffer), max_bytes - len(line))"` | — |
| [SRC-EEF2E6447C-L000154](../../api/omarai.py#L154) | 154 | `"                    line.extend(self._buffer[:take])"` | — |
| [SRC-EEF2E6447C-L000155](../../api/omarai.py#L155) | 155 | `"                    del self._buffer[:take]"` | — |
| [SRC-EEF2E6447C-L000156](../../api/omarai.py#L156) | 156 | `"                    if len(line) >= max_bytes:"` | — |
| [SRC-EEF2E6447C-L000157](../../api/omarai.py#L157) | 157 | `"                        break"` | — |
| [SRC-EEF2E6447C-L000158](../../api/omarai.py#L158) | 158 | `""` | — |
| [SRC-EEF2E6447C-L000159](../../api/omarai.py#L159) | 159 | `"                remaining = deadline - time.monotonic()"` | — |
| [SRC-EEF2E6447C-L000160](../../api/omarai.py#L160) | 160 | `"                if remaining <= 0:"` | — |
| [SRC-EEF2E6447C-L000161](../../api/omarai.py#L161) | 161 | `"                    raise TimeoutError(\"absolute request-header deadline exceeded\")"` | — |
| [SRC-EEF2E6447C-L000162](../../api/omarai.py#L162) | 162 | `"                idle_timeout = max("` | — |
| [SRC-EEF2E6447C-L000163](../../api/omarai.py#L163) | 163 | `"                    0.1,"` | — |
| [SRC-EEF2E6447C-L000164](../../api/omarai.py#L164) | 164 | `"                    min("` | — |
| [SRC-EEF2E6447C-L000165](../../api/omarai.py#L165) | 165 | `"                        float(REQUEST_HEADER_IDLE_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000166](../../api/omarai.py#L166) | 166 | `"                        MAX_REQUEST_HEADER_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000167](../../api/omarai.py#L167) | 167 | `"                    ),"` | — |
| [SRC-EEF2E6447C-L000168](../../api/omarai.py#L168) | 168 | `"                )"` | — |
| [SRC-EEF2E6447C-L000169](../../api/omarai.py#L169) | 169 | `"                self.connection.settimeout(min(idle_timeout, remaining))"` | — |
| [SRC-EEF2E6447C-L000170](../../api/omarai.py#L170) | 170 | `"                chunk = self.connection.recv(min(4_096, max_bytes - len(line)))"` | — |
| [SRC-EEF2E6447C-L000171](../../api/omarai.py#L171) | 171 | `"                if not chunk:"` | — |
| [SRC-EEF2E6447C-L000172](../../api/omarai.py#L172) | 172 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000173](../../api/omarai.py#L173) | 173 | `"                self._buffer.extend(chunk)"` | — |
| [SRC-EEF2E6447C-L000174](../../api/omarai.py#L174) | 174 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000175](../../api/omarai.py#L175) | 175 | `"            try:"` | — |
| [SRC-EEF2E6447C-L000176](../../api/omarai.py#L176) | 176 | `"                self.connection.settimeout(previous_timeout)"` | — |
| [SRC-EEF2E6447C-L000177](../../api/omarai.py#L177) | 177 | `"            except OSError:"` | — |
| [SRC-EEF2E6447C-L000178](../../api/omarai.py#L178) | 178 | `"                pass"` | — |
| [SRC-EEF2E6447C-L000179](../../api/omarai.py#L179) | 179 | `"        return bytes(line)"` | — |
| [SRC-EEF2E6447C-L000180](../../api/omarai.py#L180) | 180 | `""` | — |
| [SRC-EEF2E6447C-L000181](../../api/omarai.py#L181) | 181 | `"    def read1(self, size=-1):"` | — |
| [SRC-EEF2E6447C-L000182](../../api/omarai.py#L182) | 182 | `"        \"\"\"Read one chunk; body code applies its own idle and absolute deadlines.\"\"\""` | — |
| [SRC-EEF2E6447C-L000183](../../api/omarai.py#L183) | 183 | `"        if size == 0:"` | — |
| [SRC-EEF2E6447C-L000184](../../api/omarai.py#L184) | 184 | `"            return b\"\""` | — |
| [SRC-EEF2E6447C-L000185](../../api/omarai.py#L185) | 185 | `"        if size is None or size < 0:"` | — |
| [SRC-EEF2E6447C-L000186](../../api/omarai.py#L186) | 186 | `"            size = 8_192"` | — |
| [SRC-EEF2E6447C-L000187](../../api/omarai.py#L187) | 187 | `"        if self._buffer:"` | — |
| [SRC-EEF2E6447C-L000188](../../api/omarai.py#L188) | 188 | `"            take = min(len(self._buffer), size)"` | — |
| [SRC-EEF2E6447C-L000189](../../api/omarai.py#L189) | 189 | `"            data = bytes(self._buffer[:take])"` | — |
| [SRC-EEF2E6447C-L000190](../../api/omarai.py#L190) | 190 | `"            del self._buffer[:take]"` | — |
| [SRC-EEF2E6447C-L000191](../../api/omarai.py#L191) | 191 | `"            return data"` | — |
| [SRC-EEF2E6447C-L000192](../../api/omarai.py#L192) | 192 | `"        return self.connection.recv(size)"` | — |
| [SRC-EEF2E6447C-L000193](../../api/omarai.py#L193) | 193 | `""` | — |
| [SRC-EEF2E6447C-L000194](../../api/omarai.py#L194) | 194 | `"    def close(self):"` | — |
| [SRC-EEF2E6447C-L000195](../../api/omarai.py#L195) | 195 | `"        # The request handler owns the socket and closes its output stream."` | — |
| [SRC-EEF2E6447C-L000196](../../api/omarai.py#L196) | 196 | `"        return None"` | — |
| [SRC-EEF2E6447C-L000197](../../api/omarai.py#L197) | 197 | `""` | — |
| [SRC-EEF2E6447C-L000198](../../api/omarai.py#L198) | 198 | `""` | — |
| [SRC-EEF2E6447C-L000199](../../api/omarai.py#L199) | 199 | `"def _configured_agent_concurrency_limit() -> int:"` | — |
| [SRC-EEF2E6447C-L000200](../../api/omarai.py#L200) | 200 | `"    \"\"\"Return a process-local cap for expensive research and diagnostics operations.\"\"\""` | — |
| [SRC-EEF2E6447C-L000201](../../api/omarai.py#L201) | 201 | `"    try:"` | — |
| [SRC-EEF2E6447C-L000202](../../api/omarai.py#L202) | 202 | `"        configured = int(os.getenv(\"OMARAI_MAX_CONCURRENT_AGENT_REQUESTS\", \"4\").strip())"` | — |
| [SRC-EEF2E6447C-L000203](../../api/omarai.py#L203) | 203 | `"    except ValueError:"` | — |
| [SRC-EEF2E6447C-L000204](../../api/omarai.py#L204) | 204 | `"        configured = 4"` | — |
| [SRC-EEF2E6447C-L000205](../../api/omarai.py#L205) | 205 | `"    return max(1, min(configured, 8))"` | — |
| [SRC-EEF2E6447C-L000206](../../api/omarai.py#L206) | 206 | `""` | — |
| [SRC-EEF2E6447C-L000207](../../api/omarai.py#L207) | 207 | `""` | — |
| [SRC-EEF2E6447C-L000208](../../api/omarai.py#L208) | 208 | `"BUILD_SHA_FILE = Path(__file__).resolve().parents[1] / \"BUILD_SHA\""` | — |
| [SRC-EEF2E6447C-L000209](../../api/omarai.py#L209) | 209 | `"_PLATFORM_BUILD_SHA_ENVIRONMENTS = ("` | — |
| [SRC-EEF2E6447C-L000210](../../api/omarai.py#L210) | 210 | `"    (\"RAILWAY_GIT_COMMIT_SHA\", \"platform:railway\"),"` | — |
| [SRC-EEF2E6447C-L000211](../../api/omarai.py#L211) | 211 | `"    (\"RENDER_GIT_COMMIT\", \"platform:render\"),"` | — |
| [SRC-EEF2E6447C-L000212](../../api/omarai.py#L212) | 212 | `")"` | — |
| [SRC-EEF2E6447C-L000213](../../api/omarai.py#L213) | 213 | `""` | — |
| [SRC-EEF2E6447C-L000214](../../api/omarai.py#L214) | 214 | `""` | — |
| [SRC-EEF2E6447C-L000215](../../api/omarai.py#L215) | 215 | `"def _valid_build_sha(value: str) -> bool:"` | — |
| [SRC-EEF2E6447C-L000216](../../api/omarai.py#L216) | 216 | `"    candidate = value.strip().lower()"` | — |
| [SRC-EEF2E6447C-L000217](../../api/omarai.py#L217) | 217 | `"    return len(candidate) == 40 and all(char in \"0123456789abcdef\" for char in candidate)"` | — |
| [SRC-EEF2E6447C-L000218](../../api/omarai.py#L218) | 218 | `""` | — |
| [SRC-EEF2E6447C-L000219](../../api/omarai.py#L219) | 219 | `""` | — |
| [SRC-EEF2E6447C-L000220](../../api/omarai.py#L220) | 220 | `"def _build_identity() -> tuple[str, str]:"` | — |
| [SRC-EEF2E6447C-L000221](../../api/omarai.py#L221) | 221 | `"    \"\"\"Prefer immutable image metadata, then documented hosting-provided Git SHAs.\"\"\""` | — |
| [SRC-EEF2E6447C-L000222](../../api/omarai.py#L222) | 222 | `"    try:"` | — |
| [SRC-EEF2E6447C-L000223](../../api/omarai.py#L223) | 223 | `"        baked = BUILD_SHA_FILE.read_text(encoding=\"ascii\").strip().lower()"` | — |
| [SRC-EEF2E6447C-L000224](../../api/omarai.py#L224) | 224 | `"    except (OSError, UnicodeError):"` | — |
| [SRC-EEF2E6447C-L000225](../../api/omarai.py#L225) | 225 | `"        baked = \"\""` | — |
| [SRC-EEF2E6447C-L000226](../../api/omarai.py#L226) | 226 | `"    if _valid_build_sha(baked):"` | — |
| [SRC-EEF2E6447C-L000227](../../api/omarai.py#L227) | 227 | `"        return baked, \"image_baked\""` | — |
| [SRC-EEF2E6447C-L000228](../../api/omarai.py#L228) | 228 | `""` | — |
| [SRC-EEF2E6447C-L000229](../../api/omarai.py#L229) | 229 | `"    for environment_name, source in _PLATFORM_BUILD_SHA_ENVIRONMENTS:"` | — |
| [SRC-EEF2E6447C-L000230](../../api/omarai.py#L230) | 230 | `"        candidate = os.getenv(environment_name, \"\").strip().lower()"` | — |
| [SRC-EEF2E6447C-L000231](../../api/omarai.py#L231) | 231 | `"        if _valid_build_sha(candidate):"` | — |
| [SRC-EEF2E6447C-L000232](../../api/omarai.py#L232) | 232 | `"            return candidate, source"` | — |
| [SRC-EEF2E6447C-L000233](../../api/omarai.py#L233) | 233 | `"    return \"unknown\", \"unknown\""` | — |
| [SRC-EEF2E6447C-L000234](../../api/omarai.py#L234) | 234 | `""` | — |
| [SRC-EEF2E6447C-L000235](../../api/omarai.py#L235) | 235 | `""` | — |
| [SRC-EEF2E6447C-L000236](../../api/omarai.py#L236) | 236 | `"def _build_sha() -> str:"` | — |
| [SRC-EEF2E6447C-L000237](../../api/omarai.py#L237) | 237 | `"    \"\"\"Return a validated source SHA, or 'unknown' when no trusted build evidence exists.\"\"\""` | — |
| [SRC-EEF2E6447C-L000238](../../api/omarai.py#L238) | 238 | `"    return _build_identity()[0]"` | — |
| [SRC-EEF2E6447C-L000239](../../api/omarai.py#L239) | 239 | `""` | — |
| [SRC-EEF2E6447C-L000240](../../api/omarai.py#L240) | 240 | `""` | — |
| [SRC-EEF2E6447C-L000241](../../api/omarai.py#L241) | 241 | `"class Handler(BaseHTTPRequestHandler):"` | — |
| [SRC-EEF2E6447C-L000242](../../api/omarai.py#L242) | 242 | `"    def setup(self):"` | — |
| [SRC-EEF2E6447C-L000243](../../api/omarai.py#L243) | 243 | `"        \"\"\"Install a reader with a strict deadline for the request line and headers.\"\"\""` | — |
| [SRC-EEF2E6447C-L000244](../../api/omarai.py#L244) | 244 | `"        self.connection = self.request"` | — |
| [SRC-EEF2E6447C-L000245](../../api/omarai.py#L245) | 245 | `"        if self.timeout is not None:"` | — |
| [SRC-EEF2E6447C-L000246](../../api/omarai.py#L246) | 246 | `"            self.connection.settimeout(self.timeout)"` | — |
| [SRC-EEF2E6447C-L000247](../../api/omarai.py#L247) | 247 | `"        self._request_header_deadline = None"` | — |
| [SRC-EEF2E6447C-L000248](../../api/omarai.py#L248) | 248 | `"        self.rfile = _DeadlineRequestReader(self.connection, self)"` | — |
| [SRC-EEF2E6447C-L000249](../../api/omarai.py#L249) | 249 | `"        self.wfile = self.connection.makefile(\"wb\", self.wbufsize)"` | — |
| [SRC-EEF2E6447C-L000250](../../api/omarai.py#L250) | 250 | `""` | — |
| [SRC-EEF2E6447C-L000251](../../api/omarai.py#L251) | 251 | `"    def handle_one_request(self):"` | — |
| [SRC-EEF2E6447C-L000252](../../api/omarai.py#L252) | 252 | `"        timeout = max("` | — |
| [SRC-EEF2E6447C-L000253](../../api/omarai.py#L253) | 253 | `"            0.1,"` | — |
| [SRC-EEF2E6447C-L000254](../../api/omarai.py#L254) | 254 | `"            min("` | — |
| [SRC-EEF2E6447C-L000255](../../api/omarai.py#L255) | 255 | `"                float(REQUEST_HEADER_READ_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000256](../../api/omarai.py#L256) | 256 | `"                MAX_REQUEST_HEADER_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000257](../../api/omarai.py#L257) | 257 | `"            ),"` | — |
| [SRC-EEF2E6447C-L000258](../../api/omarai.py#L258) | 258 | `"        )"` | — |
| [SRC-EEF2E6447C-L000259](../../api/omarai.py#L259) | 259 | `"        self._request_header_deadline = time.monotonic() + timeout"` | — |
| [SRC-EEF2E6447C-L000260](../../api/omarai.py#L260) | 260 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000261](../../api/omarai.py#L261) | 261 | `"            super().handle_one_request()"` | — |
| [SRC-EEF2E6447C-L000262](../../api/omarai.py#L262) | 262 | `"        except TimeoutError:"` | — |
| [SRC-EEF2E6447C-L000263](../../api/omarai.py#L263) | 263 | `"            # Incomplete request line/headers are untrusted protocol input;"` | — |
| [SRC-EEF2E6447C-L000264](../../api/omarai.py#L264) | 264 | `"            # close the socket without trying to parse or answer a partial request."` | — |
| [SRC-EEF2E6447C-L000265](../../api/omarai.py#L265) | 265 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000266](../../api/omarai.py#L266) | 266 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000267](../../api/omarai.py#L267) | 267 | `"            self._request_header_deadline = None"` | — |
| [SRC-EEF2E6447C-L000268](../../api/omarai.py#L268) | 268 | `""` | — |
| [SRC-EEF2E6447C-L000269](../../api/omarai.py#L269) | 269 | `"    store = _lead_store_from_environment()"` | — |
| [SRC-EEF2E6447C-L000270](../../api/omarai.py#L270) | 270 | `"    _rate_lock = threading.Lock()"` | — |
| [SRC-EEF2E6447C-L000271](../../api/omarai.py#L271) | 271 | `"    _request_times: ClassVar[dict[str, deque[float]]] = defaultdict(deque)"` | — |
| [SRC-EEF2E6447C-L000272](../../api/omarai.py#L272) | 272 | `"    _rate_last_cleanup: ClassVar[float] = 0.0"` | — |
| [SRC-EEF2E6447C-L000273](../../api/omarai.py#L273) | 273 | `"    RATE_LIMIT_REQUESTS = 20"` | — |
| [SRC-EEF2E6447C-L000274](../../api/omarai.py#L274) | 274 | `"    RATE_LIMIT_WINDOW_SECONDS = 60"` | — |
| [SRC-EEF2E6447C-L000275](../../api/omarai.py#L275) | 275 | `"    RATE_LIMIT_CLEANUP_INTERVAL_SECONDS = 60"` | — |
| [SRC-EEF2E6447C-L000276](../../api/omarai.py#L276) | 276 | `"    AGENT_CONCURRENCY_LIMIT = _configured_agent_concurrency_limit()"` | — |
| [SRC-EEF2E6447C-L000277](../../api/omarai.py#L277) | 277 | `"    _agent_semaphore = threading.BoundedSemaphore(AGENT_CONCURRENCY_LIMIT)"` | — |
| [SRC-EEF2E6447C-L000278](../../api/omarai.py#L278) | 278 | `""` | — |
| [SRC-EEF2E6447C-L000279](../../api/omarai.py#L279) | 279 | `"    def _run_bounded_agent_operation(self, operation):"` | — |
| [SRC-EEF2E6447C-L000280](../../api/omarai.py#L280) | 280 | `"        \"\"\"Run an expensive operation only when a process-local slot is available.\"\"\""` | — |
| [SRC-EEF2E6447C-L000281](../../api/omarai.py#L281) | 281 | `"        cls = type(self)"` | — |
| [SRC-EEF2E6447C-L000282](../../api/omarai.py#L282) | 282 | `"        if not cls._agent_semaphore.acquire(blocking=False):"` | — |
| [SRC-EEF2E6447C-L000283](../../api/omarai.py#L283) | 283 | `"            return self.respond("` | — |
| [SRC-EEF2E6447C-L000284](../../api/omarai.py#L284) | 284 | `"                503,"` | — |
| [SRC-EEF2E6447C-L000285](../../api/omarai.py#L285) | 285 | `"                {"` | — |
| [SRC-EEF2E6447C-L000286](../../api/omarai.py#L286) | 286 | `"                    \"error\": \"خدمة البحث مشغولة حاليًا؛ أعد المحاولة بعد قليل.\","` | — |
| [SRC-EEF2E6447C-L000287](../../api/omarai.py#L287) | 287 | `"                    \"retry_after_seconds\": 5,"` | — |
| [SRC-EEF2E6447C-L000288](../../api/omarai.py#L288) | 288 | `"                    \"process_concurrency_limit\": cls.AGENT_CONCURRENCY_LIMIT,"` | — |
| [SRC-EEF2E6447C-L000289](../../api/omarai.py#L289) | 289 | `"                },"` | — |
| [SRC-EEF2E6447C-L000290](../../api/omarai.py#L290) | 290 | `"            )"` | — |
| [SRC-EEF2E6447C-L000291](../../api/omarai.py#L291) | 291 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000292](../../api/omarai.py#L292) | 292 | `"            return self.respond(200, operation())"` | — |
| [SRC-EEF2E6447C-L000293](../../api/omarai.py#L293) | 293 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000294](../../api/omarai.py#L294) | 294 | `"            cls._agent_semaphore.release()"` | — |
| [SRC-EEF2E6447C-L000295](../../api/omarai.py#L295) | 295 | `""` | — |
| [SRC-EEF2E6447C-L000296](../../api/omarai.py#L296) | 296 | `"    def _authorized(self):"` | — |
| [SRC-EEF2E6447C-L000297](../../api/omarai.py#L297) | 297 | `"        expected = os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000298](../../api/omarai.py#L298) | 298 | `"        if not expected:"` | — |
| [SRC-EEF2E6447C-L000299](../../api/omarai.py#L299) | 299 | `"            return os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() != \"1\""` | — |
| [SRC-EEF2E6447C-L000300](../../api/omarai.py#L300) | 300 | `"        supplied = self.headers.get(\"Authorization\", \"\")"` | — |
| [SRC-EEF2E6447C-L000301](../../api/omarai.py#L301) | 301 | `"        if not supplied.startswith(\"Bearer \"):"` | — |
| [SRC-EEF2E6447C-L000302](../../api/omarai.py#L302) | 302 | `"            return False"` | — |
| [SRC-EEF2E6447C-L000303](../../api/omarai.py#L303) | 303 | `"        return hmac.compare_digest(supplied[7:].strip(), expected)"` | — |
| [SRC-EEF2E6447C-L000304](../../api/omarai.py#L304) | 304 | `""` | — |
| [SRC-EEF2E6447C-L000305](../../api/omarai.py#L305) | 305 | `"    def _allowed_origins(self):"` | — |
| [SRC-EEF2E6447C-L000306](../../api/omarai.py#L306) | 306 | `"        \"\"\"Return configured browser origins plus this service’s own origin."` | — |
| [SRC-EEF2E6447C-L000307](../../api/omarai.py#L307) | 307 | `""` | — |
| [SRC-EEF2E6447C-L000308](../../api/omarai.py#L308) | 308 | `"        OMARAI_ALLOWED_ORIGINS is a comma-separated list of trusted origins"` | — |
| [SRC-EEF2E6447C-L000309](../../api/omarai.py#L309) | 309 | `"        (scheme + host + optional port; no path and no wildcard)."` | — |
| [SRC-EEF2E6447C-L000310](../../api/omarai.py#L310) | 310 | `"        \"\"\""` | — |
| [SRC-EEF2E6447C-L000311](../../api/omarai.py#L311) | 311 | `"        configured = os.getenv(\"OMARAI_ALLOWED_ORIGINS\", \"\")"` | — |
| [SRC-EEF2E6447C-L000312](../../api/omarai.py#L312) | 312 | `"        origins = {"` | — |
| [SRC-EEF2E6447C-L000313](../../api/omarai.py#L313) | 313 | `"            item.strip().rstrip(\"/\")"` | — |
| [SRC-EEF2E6447C-L000314](../../api/omarai.py#L314) | 314 | `"            for item in configured.split(\",\")"` | — |
| [SRC-EEF2E6447C-L000315](../../api/omarai.py#L315) | 315 | `"            if item.strip()"` | — |
| [SRC-EEF2E6447C-L000316](../../api/omarai.py#L316) | 316 | `"        }"` | — |
| [SRC-EEF2E6447C-L000317](../../api/omarai.py#L317) | 317 | `"        if os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() == \"1\":"` | — |
| [SRC-EEF2E6447C-L000318](../../api/omarai.py#L318) | 318 | `"            # Host identifies the requested service origin. Do not derive allowed"` | — |
| [SRC-EEF2E6447C-L000319](../../api/omarai.py#L319) | 319 | `"            # origins from X-Forwarded-Host: direct clients can spoof that header"` | — |
| [SRC-EEF2E6447C-L000320](../../api/omarai.py#L320) | 320 | `"            # unless the reverse proxy is separately configured to overwrite it."` | — |
| [SRC-EEF2E6447C-L000321](../../api/omarai.py#L321) | 321 | `"            scheme = self.headers.get(\"X-Forwarded-Proto\", \"https\").split(\",\", 1)[0].strip().lower()"` | — |
| [SRC-EEF2E6447C-L000322](../../api/omarai.py#L322) | 322 | `"            host = self.headers.get(\"Host\", \"\").split(\",\", 1)[0].strip()"` | — |
| [SRC-EEF2E6447C-L000323](../../api/omarai.py#L323) | 323 | `"            if host:"` | — |
| [SRC-EEF2E6447C-L000324](../../api/omarai.py#L324) | 324 | `"                origins.add(f\"https://{host}\".rstrip(\"/\"))"` | — |
| [SRC-EEF2E6447C-L000325](../../api/omarai.py#L325) | 325 | `"                origins.add(f\"{scheme}://{host}\".rstrip(\"/\"))"` | — |
| [SRC-EEF2E6447C-L000326](../../api/omarai.py#L326) | 326 | `"        else:"` | — |
| [SRC-EEF2E6447C-L000327](../../api/omarai.py#L327) | 327 | `"            port = self.server.server_port"` | — |
| [SRC-EEF2E6447C-L000328](../../api/omarai.py#L328) | 328 | `"            origins.update("` | — |
| [SRC-EEF2E6447C-L000329](../../api/omarai.py#L329) | 329 | `"                {"` | — |
| [SRC-EEF2E6447C-L000330](../../api/omarai.py#L330) | 330 | `"                    f\"http://127.0.0.1:{port}\","` | — |
| [SRC-EEF2E6447C-L000331](../../api/omarai.py#L331) | 331 | `"                    f\"http://localhost:{port}\","` | — |
| [SRC-EEF2E6447C-L000332](../../api/omarai.py#L332) | 332 | `"                    f\"http://[::1]:{port}\","` | — |
| [SRC-EEF2E6447C-L000333](../../api/omarai.py#L333) | 333 | `"                }"` | — |
| [SRC-EEF2E6447C-L000334](../../api/omarai.py#L334) | 334 | `"            )"` | — |
| [SRC-EEF2E6447C-L000335](../../api/omarai.py#L335) | 335 | `"        return origins"` | — |
| [SRC-EEF2E6447C-L000336](../../api/omarai.py#L336) | 336 | `""` | — |
| [SRC-EEF2E6447C-L000337](../../api/omarai.py#L337) | 337 | `"    def _origin_allowed(self, origin):"` | — |
| [SRC-EEF2E6447C-L000338](../../api/omarai.py#L338) | 338 | `"        return bool(origin) and origin.rstrip(\"/\") in self._allowed_origins()"` | — |
| [SRC-EEF2E6447C-L000339](../../api/omarai.py#L339) | 339 | `""` | — |
| [SRC-EEF2E6447C-L000340](../../api/omarai.py#L340) | 340 | `"    def _rate_limit_client_key(self):"` | — |
| [SRC-EEF2E6447C-L000341](../../api/omarai.py#L341) | 341 | `"        \"\"\"Choose a rate-limit identity without trusting spoofable proxy headers by default."` | — |
| [SRC-EEF2E6447C-L000342](../../api/omarai.py#L342) | 342 | `""` | — |
| [SRC-EEF2E6447C-L000343](../../api/omarai.py#L343) | 343 | `"        Set OMARAI_TRUST_PROXY_HEADERS=1 only when the deployment's trusted reverse"` | — |
| [SRC-EEF2E6447C-L000344](../../api/omarai.py#L344) | 344 | `"        proxy appends the actual client IP as the rightmost X-Forwarded-For value."` | — |
| [SRC-EEF2E6447C-L000345](../../api/omarai.py#L345) | 345 | `"        \"\"\""` | — |
| [SRC-EEF2E6447C-L000346](../../api/omarai.py#L346) | 346 | `"        direct_ip = self.client_address[0]"` | — |
| [SRC-EEF2E6447C-L000347](../../api/omarai.py#L347) | 347 | `"        if os.getenv(\"OMARAI_TRUST_PROXY_HEADERS\", \"\").strip() != \"1\":"` | — |
| [SRC-EEF2E6447C-L000348](../../api/omarai.py#L348) | 348 | `"            return direct_ip"` | — |
| [SRC-EEF2E6447C-L000349](../../api/omarai.py#L349) | 349 | `"        forwarded = self.headers.get(\"X-Forwarded-For\", \"\")"` | — |
| [SRC-EEF2E6447C-L000350](../../api/omarai.py#L350) | 350 | `"        candidate = forwarded.rsplit(\",\", 1)[-1].strip() if forwarded else \"\""` | — |
| [SRC-EEF2E6447C-L000351](../../api/omarai.py#L351) | 351 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000352](../../api/omarai.py#L352) | 352 | `"            return str(ipaddress.ip_address(candidate))"` | — |
| [SRC-EEF2E6447C-L000353](../../api/omarai.py#L353) | 353 | `"        except ValueError:"` | — |
| [SRC-EEF2E6447C-L000354](../../api/omarai.py#L354) | 354 | `"            return direct_ip"` | — |
| [SRC-EEF2E6447C-L000355](../../api/omarai.py#L355) | 355 | `""` | — |
| [SRC-EEF2E6447C-L000356](../../api/omarai.py#L356) | 356 | `"    def _rate_limit_ok(self):"` | — |
| [SRC-EEF2E6447C-L000357](../../api/omarai.py#L357) | 357 | `"        client_ip = self._rate_limit_client_key()"` | — |
| [SRC-EEF2E6447C-L000358](../../api/omarai.py#L358) | 358 | `"        now = time.monotonic()"` | — |
| [SRC-EEF2E6447C-L000359](../../api/omarai.py#L359) | 359 | `"        cls = type(self)"` | — |
| [SRC-EEF2E6447C-L000360](../../api/omarai.py#L360) | 360 | `"        with self._rate_lock:"` | — |
| [SRC-EEF2E6447C-L000361](../../api/omarai.py#L361) | 361 | `"            # Periodically remove IP buckets whose entire sliding window has expired."` | — |
| [SRC-EEF2E6447C-L000362](../../api/omarai.py#L362) | 362 | `"            # Without this sweep, a public endpoint could retain one empty deque per"` | — |
| [SRC-EEF2E6447C-L000363](../../api/omarai.py#L363) | 363 | `"            # distinct client IP forever, even though the rate-limit window is 60 sec."` | — |
| [SRC-EEF2E6447C-L000364](../../api/omarai.py#L364) | 364 | `"            if now - cls._rate_last_cleanup >= cls.RATE_LIMIT_CLEANUP_INTERVAL_SECONDS:"` | — |
| [SRC-EEF2E6447C-L000365](../../api/omarai.py#L365) | 365 | `"                cutoff = now - cls.RATE_LIMIT_WINDOW_SECONDS"` | — |
| [SRC-EEF2E6447C-L000366](../../api/omarai.py#L366) | 366 | `"                for key, timestamps in list(cls._request_times.items()):"` | — |
| [SRC-EEF2E6447C-L000367](../../api/omarai.py#L367) | 367 | `"                    while timestamps and timestamps[0] <= cutoff:"` | — |
| [SRC-EEF2E6447C-L000368](../../api/omarai.py#L368) | 368 | `"                        timestamps.popleft()"` | — |
| [SRC-EEF2E6447C-L000369](../../api/omarai.py#L369) | 369 | `"                    if not timestamps:"` | — |
| [SRC-EEF2E6447C-L000370](../../api/omarai.py#L370) | 370 | `"                        cls._request_times.pop(key, None)"` | — |
| [SRC-EEF2E6447C-L000371](../../api/omarai.py#L371) | 371 | `"                cls._rate_last_cleanup = now"` | — |
| [SRC-EEF2E6447C-L000372](../../api/omarai.py#L372) | 372 | `""` | — |
| [SRC-EEF2E6447C-L000373](../../api/omarai.py#L373) | 373 | `"            events = cls._request_times[client_ip]"` | — |
| [SRC-EEF2E6447C-L000374](../../api/omarai.py#L374) | 374 | `"            while events and now - events[0] >= cls.RATE_LIMIT_WINDOW_SECONDS:"` | — |
| [SRC-EEF2E6447C-L000375](../../api/omarai.py#L375) | 375 | `"                events.popleft()"` | — |
| [SRC-EEF2E6447C-L000376](../../api/omarai.py#L376) | 376 | `"            if len(events) >= cls.RATE_LIMIT_REQUESTS:"` | — |
| [SRC-EEF2E6447C-L000377](../../api/omarai.py#L377) | 377 | `"                return False"` | — |
| [SRC-EEF2E6447C-L000378](../../api/omarai.py#L378) | 378 | `"            events.append(now)"` | — |
| [SRC-EEF2E6447C-L000379](../../api/omarai.py#L379) | 379 | `"            return True"` | — |
| [SRC-EEF2E6447C-L000380](../../api/omarai.py#L380) | 380 | `""` | — |
| [SRC-EEF2E6447C-L000381](../../api/omarai.py#L381) | 381 | `"    def _read_request_body(self) -> bytes \| None:"` | — |
| [SRC-EEF2E6447C-L000382](../../api/omarai.py#L382) | 382 | `"        \"\"\"Read a bounded body with both idle and absolute wall-clock deadlines.\"\"\""` | — |
| [SRC-EEF2E6447C-L000383](../../api/omarai.py#L383) | 383 | `"        raw_size = self.headers.get(\"Content-Length\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000384](../../api/omarai.py#L384) | 384 | `"        if not raw_size or not raw_size.isascii() or not raw_size.isdecimal():"` | — |
| [SRC-EEF2E6447C-L000385](../../api/omarai.py#L385) | 385 | `"            self.respond(400, {\"error\": \"valid Content-Length is required\"})"` | — |
| [SRC-EEF2E6447C-L000386](../../api/omarai.py#L386) | 386 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000387](../../api/omarai.py#L387) | 387 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000388](../../api/omarai.py#L388) | 388 | `"            size = int(raw_size)"` | — |
| [SRC-EEF2E6447C-L000389](../../api/omarai.py#L389) | 389 | `"        except ValueError:"` | — |
| [SRC-EEF2E6447C-L000390](../../api/omarai.py#L390) | 390 | `"            self.respond(400, {\"error\": \"valid Content-Length is required\"})"` | — |
| [SRC-EEF2E6447C-L000391](../../api/omarai.py#L391) | 391 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000392](../../api/omarai.py#L392) | 392 | `"        if size <= 0:"` | — |
| [SRC-EEF2E6447C-L000393](../../api/omarai.py#L393) | 393 | `"            self.respond(400, {\"error\": \"request body is required\"})"` | — |
| [SRC-EEF2E6447C-L000394](../../api/omarai.py#L394) | 394 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000395](../../api/omarai.py#L395) | 395 | `"        if size > MAX_REQUEST_BODY_BYTES:"` | — |
| [SRC-EEF2E6447C-L000396](../../api/omarai.py#L396) | 396 | `"            self.respond(413, {\"error\": \"request too large\"})"` | — |
| [SRC-EEF2E6447C-L000397](../../api/omarai.py#L397) | 397 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000398](../../api/omarai.py#L398) | 398 | `""` | — |
| [SRC-EEF2E6447C-L000399](../../api/omarai.py#L399) | 399 | `"        total_timeout = max("` | — |
| [SRC-EEF2E6447C-L000400](../../api/omarai.py#L400) | 400 | `"            0.1,"` | — |
| [SRC-EEF2E6447C-L000401](../../api/omarai.py#L401) | 401 | `"            min("` | — |
| [SRC-EEF2E6447C-L000402](../../api/omarai.py#L402) | 402 | `"                float(REQUEST_BODY_READ_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000403](../../api/omarai.py#L403) | 403 | `"                MAX_REQUEST_BODY_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000404](../../api/omarai.py#L404) | 404 | `"            ),"` | — |
| [SRC-EEF2E6447C-L000405](../../api/omarai.py#L405) | 405 | `"        )"` | — |
| [SRC-EEF2E6447C-L000406](../../api/omarai.py#L406) | 406 | `"        idle_timeout = max("` | — |
| [SRC-EEF2E6447C-L000407](../../api/omarai.py#L407) | 407 | `"            0.1,"` | — |
| [SRC-EEF2E6447C-L000408](../../api/omarai.py#L408) | 408 | `"            min("` | — |
| [SRC-EEF2E6447C-L000409](../../api/omarai.py#L409) | 409 | `"                float(REQUEST_BODY_IDLE_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000410](../../api/omarai.py#L410) | 410 | `"                MAX_REQUEST_BODY_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000411](../../api/omarai.py#L411) | 411 | `"            ),"` | — |
| [SRC-EEF2E6447C-L000412](../../api/omarai.py#L412) | 412 | `"        )"` | — |
| [SRC-EEF2E6447C-L000413](../../api/omarai.py#L413) | 413 | `"        deadline = time.monotonic() + total_timeout"` | — |
| [SRC-EEF2E6447C-L000414](../../api/omarai.py#L414) | 414 | `"        previous_timeout = self.connection.gettimeout()"` | — |
| [SRC-EEF2E6447C-L000415](../../api/omarai.py#L415) | 415 | `"        body = bytearray()"` | — |
| [SRC-EEF2E6447C-L000416](../../api/omarai.py#L416) | 416 | `"        timed_out = False"` | — |
| [SRC-EEF2E6447C-L000417](../../api/omarai.py#L417) | 417 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000418](../../api/omarai.py#L418) | 418 | `"            while len(body) < size:"` | — |
| [SRC-EEF2E6447C-L000419](../../api/omarai.py#L419) | 419 | `"                remaining = deadline - time.monotonic()"` | — |
| [SRC-EEF2E6447C-L000420](../../api/omarai.py#L420) | 420 | `"                if remaining <= 0:"` | — |
| [SRC-EEF2E6447C-L000421](../../api/omarai.py#L421) | 421 | `"                    timed_out = True"` | — |
| [SRC-EEF2E6447C-L000422](../../api/omarai.py#L422) | 422 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000423](../../api/omarai.py#L423) | 423 | `"                self.connection.settimeout(min(idle_timeout, remaining))"` | — |
| [SRC-EEF2E6447C-L000424](../../api/omarai.py#L424) | 424 | `"                try:"` | — |
| [SRC-EEF2E6447C-L000425](../../api/omarai.py#L425) | 425 | `"                    # read1 performs at most one underlying read, letting us re-check"` | — |
| [SRC-EEF2E6447C-L000426](../../api/omarai.py#L426) | 426 | `"                    # the absolute deadline between body fragments."` | — |
| [SRC-EEF2E6447C-L000427](../../api/omarai.py#L427) | 427 | `"                    chunk = self.rfile.read1("` | — |
| [SRC-EEF2E6447C-L000428](../../api/omarai.py#L428) | 428 | `"                        min(size - len(body), REQUEST_BODY_READ_CHUNK_BYTES)"` | — |
| [SRC-EEF2E6447C-L000429](../../api/omarai.py#L429) | 429 | `"                    )"` | — |
| [SRC-EEF2E6447C-L000430](../../api/omarai.py#L430) | 430 | `"                except TimeoutError:"` | — |
| [SRC-EEF2E6447C-L000431](../../api/omarai.py#L431) | 431 | `"                    timed_out = True"` | — |
| [SRC-EEF2E6447C-L000432](../../api/omarai.py#L432) | 432 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000433](../../api/omarai.py#L433) | 433 | `"                if not chunk:"` | — |
| [SRC-EEF2E6447C-L000434](../../api/omarai.py#L434) | 434 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000435](../../api/omarai.py#L435) | 435 | `"                body.extend(chunk)"` | — |
| [SRC-EEF2E6447C-L000436](../../api/omarai.py#L436) | 436 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000437](../../api/omarai.py#L437) | 437 | `"            try:"` | — |
| [SRC-EEF2E6447C-L000438](../../api/omarai.py#L438) | 438 | `"                self.connection.settimeout(previous_timeout)"` | — |
| [SRC-EEF2E6447C-L000439](../../api/omarai.py#L439) | 439 | `"            except OSError:"` | — |
| [SRC-EEF2E6447C-L000440](../../api/omarai.py#L440) | 440 | `"                pass"` | — |
| [SRC-EEF2E6447C-L000441](../../api/omarai.py#L441) | 441 | `""` | — |
| [SRC-EEF2E6447C-L000442](../../api/omarai.py#L442) | 442 | `"        if timed_out:"` | — |
| [SRC-EEF2E6447C-L000443](../../api/omarai.py#L443) | 443 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000444](../../api/omarai.py#L444) | 444 | `"            self.respond(408, {\"error\": \"request body read timed out\"})"` | — |
| [SRC-EEF2E6447C-L000445](../../api/omarai.py#L445) | 445 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000446](../../api/omarai.py#L446) | 446 | `"        if len(body) != size:"` | — |
| [SRC-EEF2E6447C-L000447](../../api/omarai.py#L447) | 447 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000448](../../api/omarai.py#L448) | 448 | `"            self.respond(400, {\"error\": \"incomplete request body\"})"` | — |
| [SRC-EEF2E6447C-L000449](../../api/omarai.py#L449) | 449 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000450](../../api/omarai.py#L450) | 450 | `"        return bytes(body)"` | — |
| [SRC-EEF2E6447C-L000451](../../api/omarai.py#L451) | 451 | `""` | — |
| [SRC-EEF2E6447C-L000452](../../api/omarai.py#L452) | 452 | `"    def end_headers(self):"` | — |
| [SRC-EEF2E6447C-L000453](../../api/omarai.py#L453) | 453 | `"        \"\"\"Apply defensive browser headers to successful and error responses alike.\"\"\""` | — |
| [SRC-EEF2E6447C-L000454](../../api/omarai.py#L454) | 454 | `"        self.send_header(\"X-Content-Type-Options\", \"nosniff\")"` | — |
| [SRC-EEF2E6447C-L000455](../../api/omarai.py#L455) | 455 | `"        self.send_header(\"X-Frame-Options\", \"DENY\")"` | — |
| [SRC-EEF2E6447C-L000456](../../api/omarai.py#L456) | 456 | `"        self.send_header(\"Referrer-Policy\", \"strict-origin-when-cross-origin\")"` | — |
| [SRC-EEF2E6447C-L000457](../../api/omarai.py#L457) | 457 | `"        self.send_header(\"Permissions-Policy\", \"camera=(), microphone=(), geolocation=()\")"` | — |
| [SRC-EEF2E6447C-L000458](../../api/omarai.py#L458) | 458 | `"        self.send_header(\"Content-Security-Policy\", _content_security_policy())"` | — |
| [SRC-EEF2E6447C-L000459](../../api/omarai.py#L459) | 459 | `"        super().end_headers()"` | — |
| [SRC-EEF2E6447C-L000460](../../api/omarai.py#L460) | 460 | `""` | — |
| [SRC-EEF2E6447C-L000461](../../api/omarai.py#L461) | 461 | `"    def respond(self, status, payload, content_type=\"application/json; charset=utf-8\"):"` | — |
| [SRC-EEF2E6447C-L000462](../../api/omarai.py#L462) | 462 | `"        body = payload.encode() if isinstance(payload, str) else json.dumps(payload, ensure_ascii=False).encode()"` | — |
| [SRC-EEF2E6447C-L000463](../../api/omarai.py#L463) | 463 | `"        self.send_response(status)"` | — |
| [SRC-EEF2E6447C-L000464](../../api/omarai.py#L464) | 464 | `"        self.send_header(\"Content-Type\", content_type)"` | — |
| [SRC-EEF2E6447C-L000465](../../api/omarai.py#L465) | 465 | `"        self.send_header(\"Content-Length\", str(len(body)))"` | — |
| [SRC-EEF2E6447C-L000466](../../api/omarai.py#L466) | 466 | `"        self.send_header(\"Cache-Control\", \"no-store\")"` | — |
| [SRC-EEF2E6447C-L000467](../../api/omarai.py#L467) | 467 | `"        origin = self.headers.get(\"Origin\")"` | — |
| [SRC-EEF2E6447C-L000468](../../api/omarai.py#L468) | 468 | `"        if origin and self._origin_allowed(origin):"` | — |
| [SRC-EEF2E6447C-L000469](../../api/omarai.py#L469) | 469 | `"            self.send_header(\"Access-Control-Allow-Origin\", origin)"` | — |
| [SRC-EEF2E6447C-L000470](../../api/omarai.py#L470) | 470 | `"            self.send_header(\"Vary\", \"Origin\")"` | — |
| [SRC-EEF2E6447C-L000471](../../api/omarai.py#L471) | 471 | `"        self.end_headers()"` | — |
| [SRC-EEF2E6447C-L000472](../../api/omarai.py#L472) | 472 | `"        self.wfile.write(body)"` | — |
| [SRC-EEF2E6447C-L000473](../../api/omarai.py#L473) | 473 | `""` | — |
| [SRC-EEF2E6447C-L000474](../../api/omarai.py#L474) | 474 | `"    def do_GET(self):"` | — |
| [SRC-EEF2E6447C-L000475](../../api/omarai.py#L475) | 475 | `"        parsed = urlparse(self.path)"` | — |
| [SRC-EEF2E6447C-L000476](../../api/omarai.py#L476) | 476 | `"        if parsed.path in {\"/\", \"/agent\"}:"` | — |
| [SRC-EEF2E6447C-L000477](../../api/omarai.py#L477) | 477 | `"            if not AGENT_DASHBOARD.exists():"` | — |
| [SRC-EEF2E6447C-L000478](../../api/omarai.py#L478) | 478 | `"                return self.respond(404, {\"error\": \"agent dashboard missing\"})"` | — |
| [SRC-EEF2E6447C-L000479](../../api/omarai.py#L479) | 479 | `"            return self.respond(200, AGENT_DASHBOARD.read_text(encoding=\"utf-8\"), \"text/html; charset=utf-8\")"` | — |
| [SRC-EEF2E6447C-L000480](../../api/omarai.py#L480) | 480 | `"        if parsed.path == \"/leads\":"` | — |
| [SRC-EEF2E6447C-L000481](../../api/omarai.py#L481) | 481 | `"            if not LEADS_DASHBOARD.exists():"` | — |
| [SRC-EEF2E6447C-L000482](../../api/omarai.py#L482) | 482 | `"                return self.respond(404, {\"error\": \"leads dashboard missing\"})"` | — |
| [SRC-EEF2E6447C-L000483](../../api/omarai.py#L483) | 483 | `"            return self.respond(200, LEADS_DASHBOARD.read_text(encoding=\"utf-8\"), \"text/html; charset=utf-8\")"` | — |
| [SRC-EEF2E6447C-L000484](../../api/omarai.py#L484) | 484 | `"        if parsed.path == \"/api/health\":"` | — |
| [SRC-EEF2E6447C-L000485](../../api/omarai.py#L485) | 485 | `"            return self.respond("` | — |
| [SRC-EEF2E6447C-L000486](../../api/omarai.py#L486) | 486 | `"                200,"` | — |
| [SRC-EEF2E6447C-L000487](../../api/omarai.py#L487) | 487 | `"                {"` | — |
| [SRC-EEF2E6447C-L000488](../../api/omarai.py#L488) | 488 | `"                    \"ok\": True,"` | — |
| [SRC-EEF2E6447C-L000489](../../api/omarai.py#L489) | 489 | `"                    \"app\": \"Omarai\","` | — |
| [SRC-EEF2E6447C-L000490](../../api/omarai.py#L490) | 490 | `"                    \"mode\": \"web-research\","` | — |
| [SRC-EEF2E6447C-L000491](../../api/omarai.py#L491) | 491 | `"                    \"agent\": WebAgent.status(),"` | — |
| [SRC-EEF2E6447C-L000492](../../api/omarai.py#L492) | 492 | `"                    \"build\": {"` | — |
| [SRC-EEF2E6447C-L000493](../../api/omarai.py#L493) | 493 | `"                        \"sha\": _build_identity()[0],"` | — |
| [SRC-EEF2E6447C-L000494](../../api/omarai.py#L494) | 494 | `"                        \"sha_status\": ("` | — |
| [SRC-EEF2E6447C-L000495](../../api/omarai.py#L495) | 495 | `"                            \"available\" if _build_identity()[0] != \"unknown\" else \"unknown\""` | — |
| [SRC-EEF2E6447C-L000496](../../api/omarai.py#L496) | 496 | `"                        ),"` | — |
| [SRC-EEF2E6447C-L000497](../../api/omarai.py#L497) | 497 | `"                        \"sha_source\": _build_identity()[1],"` | — |
| [SRC-EEF2E6447C-L000498](../../api/omarai.py#L498) | 498 | `"                    },"` | — |
| [SRC-EEF2E6447C-L000499](../../api/omarai.py#L499) | 499 | `"                },"` | — |
| [SRC-EEF2E6447C-L000500](../../api/omarai.py#L500) | 500 | `"            )"` | — |
| [SRC-EEF2E6447C-L000501](../../api/omarai.py#L501) | 501 | `"        if parsed.path == \"/api/leads\":"` | — |
| [SRC-EEF2E6447C-L000502](../../api/omarai.py#L502) | 502 | `"            if not self._rate_limit_ok():"` | — |
| [SRC-EEF2E6447C-L000503](../../api/omarai.py#L503) | 503 | `"                return self.respond(429, {\"error\": \"تجاوزت حد الطلبات المؤقت؛ حاول بعد دقيقة.\"})"` | — |
| [SRC-EEF2E6447C-L000504](../../api/omarai.py#L504) | 504 | `"            if not self._authorized():"` | — |
| [SRC-EEF2E6447C-L000505](../../api/omarai.py#L505) | 505 | `"                return self.respond(401, {\"error\": \"يلزم رمز الوصول الخاص بالتطبيق.\"})"` | — |
| [SRC-EEF2E6447C-L000506](../../api/omarai.py#L506) | 506 | `"            q = parse_qs(parsed.query)"` | — |
| [SRC-EEF2E6447C-L000507](../../api/omarai.py#L507) | 507 | `"            try:"` | — |
| [SRC-EEF2E6447C-L000508](../../api/omarai.py#L508) | 508 | `"                limit = max(1, min(int(q.get(\"limit\", [\"100\"])[0]), 500))"` | — |
| [SRC-EEF2E6447C-L000509](../../api/omarai.py#L509) | 509 | `"                leads = self.store.list(q.get(\"status\", [None])[0], limit)"` | — |
| [SRC-EEF2E6447C-L000510](../../api/omarai.py#L510) | 510 | `"            except (ValueError, TypeError):"` | — |
| [SRC-EEF2E6447C-L000511](../../api/omarai.py#L511) | 511 | `"                return self.respond(400, {\"error\": \"invalid status or limit\"})"` | — |
| [SRC-EEF2E6447C-L000512](../../api/omarai.py#L512) | 512 | `"            return self.respond(200, {\"leads\": leads, \"count\": len(leads)})"` | — |
| [SRC-EEF2E6447C-L000513](../../api/omarai.py#L513) | 513 | `"        return self.respond(404, {\"error\": \"not found\"})"` | — |
| [SRC-EEF2E6447C-L000514](../../api/omarai.py#L514) | 514 | `""` | — |
| [SRC-EEF2E6447C-L000515](../../api/omarai.py#L515) | 515 | `"    def do_POST(self):"` | — |
| [SRC-EEF2E6447C-L000516](../../api/omarai.py#L516) | 516 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000517](../../api/omarai.py#L517) | 517 | `"            # Count API attempts before origin/content-type/body validation so invalid"` | — |
| [SRC-EEF2E6447C-L000518](../../api/omarai.py#L518) | 518 | `"            # credentials and malformed requests cannot bypass per-client throttling."` | — |
| [SRC-EEF2E6447C-L000519](../../api/omarai.py#L519) | 519 | `"            path = urlparse(self.path).path"` | — |
| [SRC-EEF2E6447C-L000520](../../api/omarai.py#L520) | 520 | `"            if path.startswith(\"/api/\") and not self._rate_limit_ok():"` | — |
| [SRC-EEF2E6447C-L000521](../../api/omarai.py#L521) | 521 | `"                return self.respond(429, {\"error\": \"تجاوزت حد الطلبات المؤقت؛ حاول بعد دقيقة.\"})"` | — |
| [SRC-EEF2E6447C-L000522](../../api/omarai.py#L522) | 522 | `"            if path.startswith(\"/api/\") and not self._authorized():"` | — |
| [SRC-EEF2E6447C-L000523](../../api/omarai.py#L523) | 523 | `"                return self.respond(401, {\"error\": \"يلزم رمز الوصول الخاص بالتطبيق.\"})"` | — |
| [SRC-EEF2E6447C-L000524](../../api/omarai.py#L524) | 524 | `""` | — |
| [SRC-EEF2E6447C-L000525](../../api/omarai.py#L525) | 525 | `"            content_type = self.headers.get(\"Content-Type\", \"\").split(\";\", 1)[0].strip().lower()"` | — |
| [SRC-EEF2E6447C-L000526](../../api/omarai.py#L526) | 526 | `"            if content_type != \"application/json\":"` | — |
| [SRC-EEF2E6447C-L000527](../../api/omarai.py#L527) | 527 | `"                return self.respond(415, {\"error\": \"Content-Type must be application/json\"})"` | — |
| [SRC-EEF2E6447C-L000528](../../api/omarai.py#L528) | 528 | `"            origin = self.headers.get(\"Origin\")"` | — |
| [SRC-EEF2E6447C-L000529](../../api/omarai.py#L529) | 529 | `"            if origin and not self._origin_allowed(origin):"` | — |
| [SRC-EEF2E6447C-L000530](../../api/omarai.py#L530) | 530 | `"                return self.respond(403, {\"error\": \"cross-origin requests are not allowed\"})"` | — |
| [SRC-EEF2E6447C-L000531](../../api/omarai.py#L531) | 531 | `""` | — |
| [SRC-EEF2E6447C-L000532](../../api/omarai.py#L532) | 532 | `"            raw_body = self._read_request_body()"` | — |
| [SRC-EEF2E6447C-L000533](../../api/omarai.py#L533) | 533 | `"            if raw_body is None:"` | — |
| [SRC-EEF2E6447C-L000534](../../api/omarai.py#L534) | 534 | `"                return"` | — |
| [SRC-EEF2E6447C-L000535](../../api/omarai.py#L535) | 535 | `"            data = json.loads(raw_body)"` | — |
