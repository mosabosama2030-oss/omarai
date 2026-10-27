# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **010**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L004645 إلى SRC-EEF2E6447C-L000282
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L004645](../../agents/web_agent.py#L4645) | 4645 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L004646](../../agents/web_agent.py#L4646) | 4646 | `"                \"هذه إعلانات/قوائم مرشحة فقط. قد تكون منتهية أو غير دقيقة؛ تحقق من السعر \""` | — |
| [SRC-1AE03B9EC3-L004647](../../agents/web_agent.py#L4647) | 4647 | `"                \"والتوافر ومصدر الإعلان واطلب تأكيدًا حديثًا قبل دفع مال أو مشاركة بيانات.\""` | — |
| [SRC-1AE03B9EC3-L004648](../../agents/web_agent.py#L4648) | 4648 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004649](../../agents/web_agent.py#L4649) | 4649 | `"        search_warning = \"؛ \".join(dict.fromkeys(search_warnings)) if search_warnings else None"` | — |
| [SRC-1AE03B9EC3-L004650](../../agents/web_agent.py#L4650) | 4650 | `"        if needs_corroboration and not task_specific_partial_evidence:"` | — |
| [SRC-1AE03B9EC3-L004651](../../agents/web_agent.py#L4651) | 4651 | `"            if search_outcome == \"unknown_after_research_error\":"` | — |
| [SRC-1AE03B9EC3-L004652](../../agents/web_agent.py#L4652) | 4652 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004653](../../agents/web_agent.py#L4653) | 4653 | `"                    \"تعذر إكمال مسار البحث بسبب خطأ، ولا توجد بيانات كافية لتحديد ما إذا \""` | — |
| [SRC-1AE03B9EC3-L004654](../../agents/web_agent.py#L4654) | 4654 | `"                    \"كانت محاولة البحث قد اكتملت أو كم نتيجة جُمعت. لذلك لا أستطيع الجزم \""` | — |
| [SRC-1AE03B9EC3-L004655](../../agents/web_agent.py#L4655) | 4655 | `"                    \"بأن البحث لم يُنفّذ أو أن الإنترنت لم يُعد نتائج. لم أتمكن من تقديم \""` | — |
| [SRC-1AE03B9EC3-L004656](../../agents/web_agent.py#L4656) | 4656 | `"                    \"إجابة مكتملة؛ أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L004657](../../agents/web_agent.py#L4657) | 4657 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004658](../../agents/web_agent.py#L4658) | 4658 | `"            elif search_outcome == \"attempted_research_error\":"` | — |
| [SRC-1AE03B9EC3-L004659](../../agents/web_agent.py#L4659) | 4659 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004660](../../agents/web_agent.py#L4660) | 4660 | `"                    \"توجد قرائن تشغيلية على بدء محاولة بحث، لكن مسار البحث فشل قبل إنتاج \""` | — |
| [SRC-1AE03B9EC3-L004661](../../agents/web_agent.py#L4661) | 4661 | `"                    \"تقرير مكتمل. لا أستطيع تحديد عدد النتائج أو المصادر القابلة للاستخدام، \""` | — |
| [SRC-1AE03B9EC3-L004662](../../agents/web_agent.py#L4662) | 4662 | `"                    \"لذلك لن أخمّن. أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L004663](../../agents/web_agent.py#L4663) | 4663 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004664](../../agents/web_agent.py#L4664) | 4664 | `"            elif search_outcome == \"attempted_no_usable_sources\":"` | — |
| [SRC-1AE03B9EC3-L004665](../../agents/web_agent.py#L4665) | 4665 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004666](../../agents/web_agent.py#L4666) | 4666 | `"                    \"جرت محاولة البحث، لكن لم تتوفر مصادر صالحة وكافية للإجابة بعد تصفية \""` | — |
| [SRC-1AE03B9EC3-L004667](../../agents/web_agent.py#L4667) | 4667 | `"                    \"النتائج. هذا لا يثبت أن جميع المواقع أو الإنترنت غير متاح؛ لن أخمّن \""` | — |
| [SRC-1AE03B9EC3-L004668](../../agents/web_agent.py#L4668) | 4668 | `"                    \"أو أقدّم نتيجة غير مدعومة. جرّب صياغة أدق أو أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L004669](../../agents/web_agent.py#L4669) | 4669 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004670](../../agents/web_agent.py#L4670) | 4670 | `"            elif search_outcome == \"not_attempted\":"` | — |
| [SRC-1AE03B9EC3-L004671](../../agents/web_agent.py#L4671) | 4671 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004672](../../agents/web_agent.py#L4672) | 4672 | `"                    \"لم تبدأ محاولة بحث ويب لهذا الطلب، لذلك لا تتوفر لدي أدلة ويب حالية \""` | — |
| [SRC-1AE03B9EC3-L004673](../../agents/web_agent.py#L4673) | 4673 | `"                    \"كافية للإجابة. لن أقدّم نتيجة غير مدعومة؛ أعد المحاولة أو اطلب بحثًا \""` | — |
| [SRC-1AE03B9EC3-L004674](../../agents/web_agent.py#L4674) | 4674 | `"                    \"صريحًا إذا كان ذلك مناسبًا.\""` | — |
| [SRC-1AE03B9EC3-L004675](../../agents/web_agent.py#L4675) | 4675 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004676](../../agents/web_agent.py#L4676) | 4676 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L004677](../../agents/web_agent.py#L4677) | 4677 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004678](../../agents/web_agent.py#L4678) | 4678 | `"                    \"لم أجد معلومات موثوقة كافية مرتبطة بسؤالك من نطاقين مسجلين مختلفين على الأقل. \""` | — |
| [SRC-1AE03B9EC3-L004679](../../agents/web_agent.py#L4679) | 4679 | `"                    \"اختلاف النطاقات لا يثبت الاستقلال التحريري. لن أخمّن أو أقدّم نتيجة غير مدعومة؛ \""` | — |
| [SRC-1AE03B9EC3-L004680](../../agents/web_agent.py#L4680) | 4680 | `"                    \"جرّب صياغة أدق أو أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L004681](../../agents/web_agent.py#L4681) | 4681 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004682](../../agents/web_agent.py#L4682) | 4682 | `"            public_sources = [{"` | — |
| [SRC-1AE03B9EC3-L004683](../../agents/web_agent.py#L4683) | 4683 | `"                \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L004684](../../agents/web_agent.py#L4684) | 4684 | `"                \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L004685](../../agents/web_agent.py#L4685) | 4685 | `"                \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004686](../../agents/web_agent.py#L4686) | 4686 | `"                \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L004687](../../agents/web_agent.py#L4687) | 4687 | `"                \"page_fetch_status\": source.get(\"page_fetch_status\", \"unknown\"),"` | — |
| [SRC-1AE03B9EC3-L004688](../../agents/web_agent.py#L4688) | 4688 | `"                \"page_fetch_error_class\": source.get(\"page_fetch_error_class\"),"` | — |
| [SRC-1AE03B9EC3-L004689](../../agents/web_agent.py#L4689) | 4689 | `"                \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L004690](../../agents/web_agent.py#L4690) | 4690 | `"                \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L004691](../../agents/web_agent.py#L4691) | 4691 | `"                \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L004692](../../agents/web_agent.py#L4692) | 4692 | `"                \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004693](../../agents/web_agent.py#L4693) | 4693 | `"                \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L004694](../../agents/web_agent.py#L4694) | 4694 | `"                \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004695](../../agents/web_agent.py#L4695) | 4695 | `"                \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004696](../../agents/web_agent.py#L4696) | 4696 | `"                \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004697](../../agents/web_agent.py#L4697) | 4697 | `"                \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L004698](../../agents/web_agent.py#L4698) | 4698 | `"                \"lead_qualification\": source.get(\"lead_qualification\"),"` | — |
| [SRC-1AE03B9EC3-L004699](../../agents/web_agent.py#L4699) | 4699 | `"                \"lead_intent_evidence\": source.get(\"lead_intent_evidence\"),"` | — |
| [SRC-1AE03B9EC3-L004700](../../agents/web_agent.py#L4700) | 4700 | `"            } for source in sources]"` | — |
| [SRC-1AE03B9EC3-L004701](../../agents/web_agent.py#L4701) | 4701 | `"            citation_validation = self._citation_validation_metadata("` | — |
| [SRC-1AE03B9EC3-L004702](../../agents/web_agent.py#L4702) | 4702 | `"                reason, 0, [], \"not_run\""` | — |
| [SRC-1AE03B9EC3-L004703](../../agents/web_agent.py#L4703) | 4703 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004704](../../agents/web_agent.py#L4704) | 4704 | `"            citation_validation[\"status\"] = \"not_applicable_no_generated_answer\""` | — |
| [SRC-1AE03B9EC3-L004705](../../agents/web_agent.py#L4705) | 4705 | `"            coverage_targets = self._question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L004706](../../agents/web_agent.py#L4706) | 4706 | `"            answer_coverage = {"` | — |
| [SRC-1AE03B9EC3-L004707](../../agents/web_agent.py#L4707) | 4707 | `"                \"method\": \"explicit_criteria_heuristic\","` | — |
| [SRC-1AE03B9EC3-L004708](../../agents/web_agent.py#L4708) | 4708 | `"                \"targets\": coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L004709](../../agents/web_agent.py#L4709) | 4709 | `"                \"status\": ("` | — |
| [SRC-1AE03B9EC3-L004710](../../agents/web_agent.py#L4710) | 4710 | `"                    \"not_reviewed_insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L004711](../../agents/web_agent.py#L4711) | 4711 | `"                    if coverage_targets else \"no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L004712](../../agents/web_agent.py#L4712) | 4712 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L004713](../../agents/web_agent.py#L4713) | 4713 | `"                \"automatically_graded\": False,"` | — |
| [SRC-1AE03B9EC3-L004714](../../agents/web_agent.py#L4714) | 4714 | `"            }"` | — |
| [SRC-1AE03B9EC3-L004715](../../agents/web_agent.py#L4715) | 4715 | `"            answer_integrity = audit_answer_integrity(question, reason, sources, coverage_targets)"` | — |
| [SRC-1AE03B9EC3-L004716](../../agents/web_agent.py#L4716) | 4716 | `"            answer_coverage[\"target_checks\"] = answer_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L004717](../../agents/web_agent.py#L4717) | 4717 | `"            answer_coverage[\"potentially_missing_target_count\"] = answer_integrity[\"potentially_missing_target_count\"]"` | — |
| [SRC-1AE03B9EC3-L004718](../../agents/web_agent.py#L4718) | 4718 | `"            answer_coverage[\"lexical_screen_method\"] = \"deterministic_lexical_screen_only_not_semantic_grading\""` | — |
| [SRC-1AE03B9EC3-L004719](../../agents/web_agent.py#L4719) | 4719 | `"            task_fulfillment_status = ("` | — |
| [SRC-1AE03B9EC3-L004720](../../agents/web_agent.py#L4720) | 4720 | `"                \"not_assessed_insufficient_evidence\" if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L004721](../../agents/web_agent.py#L4721) | 4721 | `"                else \"not_machine_assessed_no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L004722](../../agents/web_agent.py#L4722) | 4722 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004723](../../agents/web_agent.py#L4723) | 4723 | `"            answer_coverage[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L004724](../../agents/web_agent.py#L4724) | 4724 | `"            research_failed = search_outcome in _RESEARCH_ERROR_OUTCOMES"` | — |
| [SRC-1AE03B9EC3-L004725](../../agents/web_agent.py#L4725) | 4725 | `"            report.update({"` | — |
| [SRC-1AE03B9EC3-L004726](../../agents/web_agent.py#L4726) | 4726 | `"                # When collection failed, an empty local list is not evidence that"` | — |
| [SRC-1AE03B9EC3-L004727](../../agents/web_agent.py#L4727) | 4727 | `"                # the remote search returned zero sources; preserve unknown counts."` | — |
| [SRC-1AE03B9EC3-L004728](../../agents/web_agent.py#L4728) | 4728 | `"                \"unique_sources\": None if research_failed else len(sources),"` | — |
| [SRC-1AE03B9EC3-L004729](../../agents/web_agent.py#L4729) | 4729 | `"                \"independent_sources\": None if research_failed else len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L004730](../../agents/web_agent.py#L4730) | 4730 | `"                \"distinct_registrable_domains\": None if research_failed else len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L004731](../../agents/web_agent.py#L4731) | 4731 | `"                \"pages_fetched\": ("` | — |
| [SRC-1AE03B9EC3-L004732](../../agents/web_agent.py#L4732) | 4732 | `"                    None if research_failed"` | — |
| [SRC-1AE03B9EC3-L004733](../../agents/web_agent.py#L4733) | 4733 | `"                    else sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L004734](../../agents/web_agent.py#L4734) | 4734 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L004735](../../agents/web_agent.py#L4735) | 4735 | `"                \"provider_diagnostics\": current_research_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L004736](../../agents/web_agent.py#L4736) | 4736 | `"                \"insufficient_evidence\": True,"` | — |
| [SRC-1AE03B9EC3-L004737](../../agents/web_agent.py#L4737) | 4737 | `"                \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L004738](../../agents/web_agent.py#L4738) | 4738 | `"                \"citation_check\": citation_validation[\"status\"],"` | — |
| [SRC-1AE03B9EC3-L004739](../../agents/web_agent.py#L4739) | 4739 | `"                \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L004740](../../agents/web_agent.py#L4740) | 4740 | `"                \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L004741](../../agents/web_agent.py#L4741) | 4741 | `"                \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L004742](../../agents/web_agent.py#L4742) | 4742 | `"                \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L004743](../../agents/web_agent.py#L4743) | 4743 | `"                \"connector_summary\": report.get(\"connector_summary\") or self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L004744](../../agents/web_agent.py#L4744) | 4744 | `"                    current_research_diagnostics, sources"` | — |
| [SRC-1AE03B9EC3-L004745](../../agents/web_agent.py#L4745) | 4745 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L004746](../../agents/web_agent.py#L4746) | 4746 | `"            })"` | — |
| [SRC-1AE03B9EC3-L004747](../../agents/web_agent.py#L4747) | 4747 | `"            return {"` | — |
| [SRC-1AE03B9EC3-L004748](../../agents/web_agent.py#L4748) | 4748 | `"                \"answer\": reason,"` | — |
| [SRC-1AE03B9EC3-L004749](../../agents/web_agent.py#L4749) | 4749 | `"                \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L004750](../../agents/web_agent.py#L4750) | 4750 | `"                \"search_query\": (plan.get(\"queries\") or [\"\"])[0],"` | — |
| [SRC-1AE03B9EC3-L004751](../../agents/web_agent.py#L4751) | 4751 | `"                \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L004752](../../agents/web_agent.py#L4752) | 4752 | `"                \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L004753](../../agents/web_agent.py#L4753) | 4753 | `"                    \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L004754](../../agents/web_agent.py#L4754) | 4754 | `"                    \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L004755](../../agents/web_agent.py#L4755) | 4755 | `"                    \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L004756](../../agents/web_agent.py#L4756) | 4756 | `"                    \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L004757](../../agents/web_agent.py#L4757) | 4757 | `"                    \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L004758](../../agents/web_agent.py#L4758) | 4758 | `"                    \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L004759](../../agents/web_agent.py#L4759) | 4759 | `"                    \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L004760](../../agents/web_agent.py#L4760) | 4760 | `"                    \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L004761](../../agents/web_agent.py#L4761) | 4761 | `"                    \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L004762](../../agents/web_agent.py#L4762) | 4762 | `"                },"` | — |
| [SRC-1AE03B9EC3-L004763](../../agents/web_agent.py#L4763) | 4763 | `"                \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L004764](../../agents/web_agent.py#L4764) | 4764 | `"                \"sources\": public_sources,"` | — |
| [SRC-1AE03B9EC3-L004765](../../agents/web_agent.py#L4765) | 4765 | `"                \"used_language_model\": False,"` | — |
| [SRC-1AE03B9EC3-L004766](../../agents/web_agent.py#L4766) | 4766 | `"                \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L004767](../../agents/web_agent.py#L4767) | 4767 | `"                \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L004768](../../agents/web_agent.py#L4768) | 4768 | `"                \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L004769](../../agents/web_agent.py#L4769) | 4769 | `"                \"warnings\": list(dict.fromkeys(search_warnings + [reason])),"` | — |
| [SRC-1AE03B9EC3-L004770](../../agents/web_agent.py#L4770) | 4770 | `"                \"kind\": \"insufficient_evidence\","` | — |
| [SRC-1AE03B9EC3-L004771](../../agents/web_agent.py#L4771) | 4771 | `"                \"final_answer_status\": \"insufficient_evidence_no_generation\","` | — |
| [SRC-1AE03B9EC3-L004772](../../agents/web_agent.py#L4772) | 4772 | `"                \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L004773](../../agents/web_agent.py#L4773) | 4773 | `"                \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L004774](../../agents/web_agent.py#L4774) | 4774 | `"                \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L004775](../../agents/web_agent.py#L4775) | 4775 | `"                \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L004776](../../agents/web_agent.py#L4776) | 4776 | `"                \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L004777](../../agents/web_agent.py#L4777) | 4777 | `"                \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L004778](../../agents/web_agent.py#L4778) | 4778 | `"                \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L004779](../../agents/web_agent.py#L4779) | 4779 | `"            }"` | — |
| [SRC-1AE03B9EC3-L004780](../../agents/web_agent.py#L4780) | 4780 | `""` | — |
| [SRC-1AE03B9EC3-L004781](../../agents/web_agent.py#L4781) | 4781 | `"        answer = \"\""` | — |
| [SRC-1AE03B9EC3-L004782](../../agents/web_agent.py#L4782) | 4782 | `"        used_llm = False"` | — |
| [SRC-1AE03B9EC3-L004783](../../agents/web_agent.py#L4783) | 4783 | `"        llm_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L004784](../../agents/web_agent.py#L4784) | 4784 | `"        generation_budget_exhausted = False"` | — |
| [SRC-1AE03B9EC3-L004785](../../agents/web_agent.py#L4785) | 4785 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L004786](../../agents/web_agent.py#L4786) | 4786 | `"            answer = self._generate("` | — |
| [SRC-1AE03B9EC3-L004787](../../agents/web_agent.py#L4787) | 4787 | `"                question,"` | — |
| [SRC-1AE03B9EC3-L004788](../../agents/web_agent.py#L4788) | 4788 | `"                clean_history,"` | — |
| [SRC-1AE03B9EC3-L004789](../../agents/web_agent.py#L4789) | 4789 | `"                sources,"` | — |
| [SRC-1AE03B9EC3-L004790](../../agents/web_agent.py#L4790) | 4790 | `"                search_warning,"` | — |
| [SRC-1AE03B9EC3-L004791](../../agents/web_agent.py#L4791) | 4791 | `"                research_plan=plan,"` | — |
| [SRC-1AE03B9EC3-L004792](../../agents/web_agent.py#L4792) | 4792 | `"                search_report=report,"` | — |
| [SRC-1AE03B9EC3-L004793](../../agents/web_agent.py#L4793) | 4793 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004794](../../agents/web_agent.py#L4794) | 4794 | `"            used_llm = True"` | — |
| [SRC-1AE03B9EC3-L004795](../../agents/web_agent.py#L4795) | 4795 | `"            if self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L004796](../../agents/web_agent.py#L4796) | 4796 | `"                existing_urls = {item.get(\"url\") for item in sources}"` | — |
| [SRC-1AE03B9EC3-L004797](../../agents/web_agent.py#L4797) | 4797 | `"                relevance_queries = []"` | — |
| [SRC-1AE03B9EC3-L004798](../../agents/web_agent.py#L4798) | 4798 | `"                planned_queries = plan.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L004799](../../agents/web_agent.py#L4799) | 4799 | `"                if not isinstance(planned_queries, list):"` | — |
| [SRC-1AE03B9EC3-L004800](../../agents/web_agent.py#L4800) | 4800 | `"                    planned_queries = []"` | — |
| [SRC-1AE03B9EC3-L004801](../../agents/web_agent.py#L4801) | 4801 | `"                for candidate_query in [question, *planned_queries]:"` | — |
| [SRC-1AE03B9EC3-L004802](../../agents/web_agent.py#L4802) | 4802 | `"                    if not isinstance(candidate_query, str):"` | — |
| [SRC-1AE03B9EC3-L004803](../../agents/web_agent.py#L4803) | 4803 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L004804](../../agents/web_agent.py#L4804) | 4804 | `"                    compacted_query = compact_search_query(candidate_query)"` | — |
| [SRC-1AE03B9EC3-L004805](../../agents/web_agent.py#L4805) | 4805 | `"                    if compacted_query and compacted_query not in relevance_queries:"` | — |
| [SRC-1AE03B9EC3-L004806](../../agents/web_agent.py#L4806) | 4806 | `"                        relevance_queries.append(compacted_query)"` | — |
| [SRC-1AE03B9EC3-L004807](../../agents/web_agent.py#L4807) | 4807 | `"                for item in self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L004808](../../agents/web_agent.py#L4808) | 4808 | `"                    source_text = \" \".join(("` | — |
| [SRC-1AE03B9EC3-L004809](../../agents/web_agent.py#L4809) | 4809 | `"                        item.get(\"title\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004810](../../agents/web_agent.py#L4810) | 4810 | `"                        item.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004811](../../agents/web_agent.py#L4811) | 4811 | `"                    ))"` | — |
| [SRC-1AE03B9EC3-L004812](../../agents/web_agent.py#L4812) | 4812 | `"                    if ("` | — |
| [SRC-1AE03B9EC3-L004813](../../agents/web_agent.py#L4813) | 4813 | `"                        relevance_queries"` | — |
| [SRC-1AE03B9EC3-L004814](../../agents/web_agent.py#L4814) | 4814 | `"                        and item[\"url\"] not in existing_urls"` | — |
| [SRC-1AE03B9EC3-L004815](../../agents/web_agent.py#L4815) | 4815 | `"                        and not _blocked_source_url(item[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L004816](../../agents/web_agent.py#L4816) | 4816 | `"                        and any("` | — |
| [SRC-1AE03B9EC3-L004817](../../agents/web_agent.py#L4817) | 4817 | `"                            _relevance_ratio(candidate_query, source_text) >= 0.20"` | — |
| [SRC-1AE03B9EC3-L004818](../../agents/web_agent.py#L4818) | 4818 | `"                            for candidate_query in relevance_queries"` | — |
| [SRC-1AE03B9EC3-L004819](../../agents/web_agent.py#L4819) | 4819 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004820](../../agents/web_agent.py#L4820) | 4820 | `"                    ):"` | — |
| [SRC-1AE03B9EC3-L004821](../../agents/web_agent.py#L4821) | 4821 | `"                        sources.append(item)"` | — |
| [SRC-1AE03B9EC3-L004822](../../agents/web_agent.py#L4822) | 4822 | `"                        existing_urls.add(item[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L004823](../../agents/web_agent.py#L4823) | 4823 | `"                report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004824](../../agents/web_agent.py#L4824) | 4824 | `"                provider_counts = dict(report.get(\"provider_counts\", {}))"` | — |
| [SRC-1AE03B9EC3-L004825](../../agents/web_agent.py#L4825) | 4825 | `"                provider_counts[\"openrouter_web_search\"] = len(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L004826](../../agents/web_agent.py#L4826) | 4826 | `"                report[\"provider_counts\"] = provider_counts"` | — |
| [SRC-1AE03B9EC3-L004827](../../agents/web_agent.py#L4827) | 4827 | `"                providers_used = list(report.get(\"providers_used\", []))"` | — |
| [SRC-1AE03B9EC3-L004828](../../agents/web_agent.py#L4828) | 4828 | `"                if \"openrouter_web_search\" not in providers_used:"` | — |
| [SRC-1AE03B9EC3-L004829](../../agents/web_agent.py#L4829) | 4829 | `"                    providers_used.append(\"openrouter_web_search\")"` | — |
| [SRC-1AE03B9EC3-L004830](../../agents/web_agent.py#L4830) | 4830 | `"                report[\"providers_used\"] = providers_used"` | — |
| [SRC-1AE03B9EC3-L004831](../../agents/web_agent.py#L4831) | 4831 | `"                report[\"evidence_signals\"] = evidence_signal_report("` | — |
| [SRC-1AE03B9EC3-L004832](../../agents/web_agent.py#L4832) | 4832 | `"                    sources, plan.get(\"freshness\", \"any\")"` | — |
| [SRC-1AE03B9EC3-L004833](../../agents/web_agent.py#L4833) | 4833 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004834](../../agents/web_agent.py#L4834) | 4834 | `"        except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L004835](../../agents/web_agent.py#L4835) | 4835 | `"            llm_warning = str(exc)"` | — |
| [SRC-1AE03B9EC3-L004836](../../agents/web_agent.py#L4836) | 4836 | `"            generation_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L004837](../../agents/web_agent.py#L4837) | 4837 | `"            if generation_budget_exhausted:"` | — |
| [SRC-1AE03B9EC3-L004838](../../agents/web_agent.py#L4838) | 4838 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004839](../../agents/web_agent.py#L4839) | 4839 | `"                    \"استُنفدت ميزانية محاولات النماذج قبل اكتمال الإجابة التحليلية. \""` | — |
| [SRC-1AE03B9EC3-L004840](../../agents/web_agent.py#L4840) | 4840 | `"                    \"أعرض مقتطفات المصادر المتاحة فقط، ولا أعتبر المهمة مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L004841](../../agents/web_agent.py#L4841) | 4841 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004842](../../agents/web_agent.py#L4842) | 4842 | `"            elif not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L004843](../../agents/web_agent.py#L4843) | 4843 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004844](../../agents/web_agent.py#L4844) | 4844 | `"                    \"تم البحث، لكن الفهم التوليدي غير مفعّل بعد. اضبط OPENROUTER_API_KEY \""` | — |
| [SRC-1AE03B9EC3-L004845](../../agents/web_agent.py#L4845) | 4845 | `"                    \"في Termux لتفعيل تخطيط البحث والإجابة باللغة الطبيعية.\""` | — |
| [SRC-1AE03B9EC3-L004846](../../agents/web_agent.py#L4846) | 4846 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004847](../../agents/web_agent.py#L4847) | 4847 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L004848](../../agents/web_agent.py#L4848) | 4848 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004849](../../agents/web_agent.py#L4849) | 4849 | `"                    \"اكتمل البحث، لكن تعذر توليد إجابة تحليلية. أعرض لك مقتطفات المصادر \""` | — |
| [SRC-1AE03B9EC3-L004850](../../agents/web_agent.py#L4850) | 4850 | `"                    \"المتاحة بدلًا من اختلاق إجابة.\""` | — |
| [SRC-1AE03B9EC3-L004851](../../agents/web_agent.py#L4851) | 4851 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004852](../../agents/web_agent.py#L4852) | 4852 | `"            answer = _fallback_answer(sources, reason)"` | — |
| [SRC-1AE03B9EC3-L004853](../../agents/web_agent.py#L4853) | 4853 | `""` | — |
| [SRC-1AE03B9EC3-L004854](../../agents/web_agent.py#L4854) | 4854 | `"        coverage_targets = self._question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L004855](../../agents/web_agent.py#L4855) | 4855 | `"        coverage_repair_status = \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L004856](../../agents/web_agent.py#L4856) | 4856 | `"        coverage_repair_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L004857](../../agents/web_agent.py#L4857) | 4857 | `"        review_status = \"not_run\""` | — |
| [SRC-1AE03B9EC3-L004858](../../agents/web_agent.py#L4858) | 4858 | `"        review_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L004859](../../agents/web_agent.py#L4859) | 4859 | `"        review_budget_exhausted = False"` | — |
| [SRC-1AE03B9EC3-L004860](../../agents/web_agent.py#L4860) | 4860 | `"        if used_llm and sources:"` | — |
| [SRC-1AE03B9EC3-L004861](../../agents/web_agent.py#L4861) | 4861 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L004862](../../agents/web_agent.py#L4862) | 4862 | `"                answer = self._review_answer(question, answer, sources[:MAX_LLM_CITED_SOURCES])"` | — |
| [SRC-1AE03B9EC3-L004863](../../agents/web_agent.py#L4863) | 4863 | `"                review_status = \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L004864](../../agents/web_agent.py#L4864) | 4864 | `"            except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L004865](../../agents/web_agent.py#L4865) | 4865 | `"                review_status = \"model_claim_audit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L004866](../../agents/web_agent.py#L4866) | 4866 | `"                review_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L004867](../../agents/web_agent.py#L4867) | 4867 | `"                review_warning = ("` | — |
| [SRC-1AE03B9EC3-L004868](../../agents/web_agent.py#L4868) | 4868 | `"                    \"استُنفدت ميزانية النماذج قبل اكتمال تدقيق الإجابة؛ لذلك لن أعرض المسودة \""` | — |
| [SRC-1AE03B9EC3-L004869](../../agents/web_agent.py#L4869) | 4869 | `"                    \"بوصفها إجابة مكتملة. أرفقت مقتطفات المصادر المتاحة بدل الاعتماد عليها.\""` | — |
| [SRC-1AE03B9EC3-L004870](../../agents/web_agent.py#L4870) | 4870 | `"                    if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L004871](../../agents/web_agent.py#L4871) | 4871 | `"                    else"` | — |
| [SRC-1AE03B9EC3-L004872](../../agents/web_agent.py#L4872) | 4872 | `"                    \"تعذر تدقيق الادعاءات مقابل نصوص المصادر؛ لذلك لن أتعامل مع المسودة \""` | — |
| [SRC-1AE03B9EC3-L004873](../../agents/web_agent.py#L4873) | 4873 | `"                    \"كإجابة مؤكدة. أرفقت مقتطفات المصادر المتاحة بدل الاعتماد على المسودة.\""` | — |
| [SRC-1AE03B9EC3-L004874](../../agents/web_agent.py#L4874) | 4874 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004875](../../agents/web_agent.py#L4875) | 4875 | `"                answer = _fallback_answer(sources, review_warning)"` | — |
| [SRC-1AE03B9EC3-L004876](../../agents/web_agent.py#L4876) | 4876 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L004877](../../agents/web_agent.py#L4877) | 4877 | `"            coverage_targets"` | — |
| [SRC-1AE03B9EC3-L004878](../../agents/web_agent.py#L4878) | 4878 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L004879](../../agents/web_agent.py#L4879) | 4879 | `"            and sources"` | — |
| [SRC-1AE03B9EC3-L004880](../../agents/web_agent.py#L4880) | 4880 | `"            and self.api_key"` | — |
| [SRC-1AE03B9EC3-L004881](../../agents/web_agent.py#L4881) | 4881 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L004882](../../agents/web_agent.py#L4882) | 4882 | `"            initial_integrity = audit_answer_integrity(question, answer, sources, coverage_targets)"` | — |
| [SRC-1AE03B9EC3-L004883](../../agents/web_agent.py#L4883) | 4883 | `"            missing_targets = ["` | — |
| [SRC-1AE03B9EC3-L004884](../../agents/web_agent.py#L4884) | 4884 | `"                item[\"target\"] for item in initial_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L004885](../../agents/web_agent.py#L4885) | 4885 | `"                if item[\"status\"] == \"possibly_missing\""` | — |
| [SRC-1AE03B9EC3-L004886](../../agents/web_agent.py#L4886) | 4886 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L004887](../../agents/web_agent.py#L4887) | 4887 | `"            if not missing_targets:"` | — |
| [SRC-1AE03B9EC3-L004888](../../agents/web_agent.py#L4888) | 4888 | `"                coverage_repair_status = \"not_needed_lexical_signals_found\""` | — |
| [SRC-1AE03B9EC3-L004889](../../agents/web_agent.py#L4889) | 4889 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L004890](../../agents/web_agent.py#L4890) | 4890 | `"                coverage_repair_status = \"attempted\""` | — |
| [SRC-1AE03B9EC3-L004891](../../agents/web_agent.py#L4891) | 4891 | `"                try:"` | — |
| [SRC-1AE03B9EC3-L004892](../../agents/web_agent.py#L4892) | 4892 | `"                    repaired_answer = self._repair_answer_coverage("` | — |
| [SRC-1AE03B9EC3-L004893](../../agents/web_agent.py#L4893) | 4893 | `"                        question, answer, sources, missing_targets"` | — |
| [SRC-1AE03B9EC3-L004894](../../agents/web_agent.py#L4894) | 4894 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004895](../../agents/web_agent.py#L4895) | 4895 | `"                    if repaired_answer.strip() != answer.strip():"` | — |
| [SRC-1AE03B9EC3-L004896](../../agents/web_agent.py#L4896) | 4896 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L004897](../../agents/web_agent.py#L4897) | 4897 | `"                            reaudit_answer = self._review_answer("` | — |
| [SRC-1AE03B9EC3-L004898](../../agents/web_agent.py#L4898) | 4898 | `"                                question,"` | — |
| [SRC-1AE03B9EC3-L004899](../../agents/web_agent.py#L4899) | 4899 | `"                                repaired_answer,"` | — |
| [SRC-1AE03B9EC3-L004900](../../agents/web_agent.py#L4900) | 4900 | `"                                sources[:MAX_LLM_CITED_SOURCES],"` | — |
| [SRC-1AE03B9EC3-L004901](../../agents/web_agent.py#L4901) | 4901 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L004902](../../agents/web_agent.py#L4902) | 4902 | `"                            answer = reaudit_answer"` | — |
| [SRC-1AE03B9EC3-L004903](../../agents/web_agent.py#L4903) | 4903 | `"                            coverage_repair_status = \"revised_and_reaudited\""` | — |
| [SRC-1AE03B9EC3-L004904](../../agents/web_agent.py#L4904) | 4904 | `"                            review_status = \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L004905](../../agents/web_agent.py#L4905) | 4905 | `"                        except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L004906](../../agents/web_agent.py#L4906) | 4906 | `"                            review_status = \"model_claim_audit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L004907](../../agents/web_agent.py#L4907) | 4907 | `"                            review_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L004908](../../agents/web_agent.py#L4908) | 4908 | `"                            coverage_repair_status = ("` | — |
| [SRC-1AE03B9EC3-L004909](../../agents/web_agent.py#L4909) | 4909 | `"                                \"reaudit_budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L004910](../../agents/web_agent.py#L4910) | 4910 | `"                                if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L004911](../../agents/web_agent.py#L4911) | 4911 | `"                                else \"reaudit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L004912](../../agents/web_agent.py#L4912) | 4912 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L004913](../../agents/web_agent.py#L4913) | 4913 | `"                            review_warning = ("` | — |
| [SRC-1AE03B9EC3-L004914](../../agents/web_agent.py#L4914) | 4914 | `"                                \"استُنفدت ميزانية النماذج قبل إعادة تدقيق الإجابة المعدلة؛ \""` | — |
| [SRC-1AE03B9EC3-L004915](../../agents/web_agent.py#L4915) | 4915 | `"                                \"لذلك لن أعرض النص المعدل بوصفه إجابة مكتملة، وأعرض مقتطفات المصادر بدلًا منه.\""` | — |
| [SRC-1AE03B9EC3-L004916](../../agents/web_agent.py#L4916) | 4916 | `"                                if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L004917](../../agents/web_agent.py#L4917) | 4917 | `"                                else"` | — |
| [SRC-1AE03B9EC3-L004918](../../agents/web_agent.py#L4918) | 4918 | `"                                \"تعذرت إعادة تدقيق الإجابة المعدلة مقابل الأدلة؛ لذلك لن أعرضها بوصفها إجابة مكتملة، \""` | — |
| [SRC-1AE03B9EC3-L004919](../../agents/web_agent.py#L4919) | 4919 | `"                                \"وأعرض مقتطفات المصادر بدلًا منها.\""` | — |
| [SRC-1AE03B9EC3-L004920](../../agents/web_agent.py#L4920) | 4920 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L004921](../../agents/web_agent.py#L4921) | 4921 | `"                            answer = _fallback_answer(sources, review_warning)"` | — |
| [SRC-1AE03B9EC3-L004922](../../agents/web_agent.py#L4922) | 4922 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L004923](../../agents/web_agent.py#L4923) | 4923 | `"                        coverage_repair_status = \"no_change_gap_unresolved\""` | — |
| [SRC-1AE03B9EC3-L004924](../../agents/web_agent.py#L4924) | 4924 | `"                        coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L004925](../../agents/web_agent.py#L4925) | 4925 | `"                            \"رصد الفحص اللفظي محورًا قد يكون ناقصًا، لكن محاولة الإصلاح لم تغيّر الإجابة؛ \""` | — |
| [SRC-1AE03B9EC3-L004926](../../agents/web_agent.py#L4926) | 4926 | `"                            \"تحقق من تغطية هذا المحور يدويًا.\""` | — |
| [SRC-1AE03B9EC3-L004927](../../agents/web_agent.py#L4927) | 4927 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004928](../../agents/web_agent.py#L4928) | 4928 | `"                except RequestBudgetExceeded:"` | — |
| [SRC-1AE03B9EC3-L004929](../../agents/web_agent.py#L4929) | 4929 | `"                    coverage_repair_status = \"budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L004930](../../agents/web_agent.py#L4930) | 4930 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L004931](../../agents/web_agent.py#L4931) | 4931 | `"                        \"استُنفدت ميزانية النماذج قبل محاولة إصلاح محور قد يكون ناقصًا؛ \""` | — |
| [SRC-1AE03B9EC3-L004932](../../agents/web_agent.py#L4932) | 4932 | `"                        \"لا تعتبر التغطية مكتملة دون مراجعة المحور المذكور.\""` | — |
| [SRC-1AE03B9EC3-L004933](../../agents/web_agent.py#L4933) | 4933 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004934](../../agents/web_agent.py#L4934) | 4934 | `"                except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L004935](../../agents/web_agent.py#L4935) | 4935 | `"                    coverage_repair_status = \"unavailable\""` | — |
| [SRC-1AE03B9EC3-L004936](../../agents/web_agent.py#L4936) | 4936 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L004937](../../agents/web_agent.py#L4937) | 4937 | `"                        \"تعذرت محاولة إصلاح محور قد يكون ناقصًا (\""` | — |
| [SRC-1AE03B9EC3-L004938](../../agents/web_agent.py#L4938) | 4938 | `"                        + type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L004939](../../agents/web_agent.py#L4939) | 4939 | `"                        + \")؛ راجع المحاور المطلوبة قبل اعتماد الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L004940](../../agents/web_agent.py#L4940) | 4940 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004941](../../agents/web_agent.py#L4941) | 4941 | `"        elif coverage_targets and review_status == \"model_claim_audit_completed\" and not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L004942](../../agents/web_agent.py#L4942) | 4942 | `"            coverage_repair_status = \"skipped_no_model_configuration\""` | — |
| [SRC-1AE03B9EC3-L004943](../../agents/web_agent.py#L4943) | 4943 | `"        elif coverage_targets:"` | — |
| [SRC-1AE03B9EC3-L004944](../../agents/web_agent.py#L4944) | 4944 | `"            coverage_repair_status = \"skipped_review_unavailable\""` | — |
| [SRC-1AE03B9EC3-L004945](../../agents/web_agent.py#L4945) | 4945 | `""` | — |
| [SRC-1AE03B9EC3-L004946](../../agents/web_agent.py#L4946) | 4946 | `"        if self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L004947](../../agents/web_agent.py#L4947) | 4947 | `"            answer += \"\\n\\nروابط إضافية من البحث المباشر عبر الويب:\""` | — |
| [SRC-1AE03B9EC3-L004948](../../agents/web_agent.py#L4948) | 4948 | `"            for source in self.server_search_sources[:8]:"` | — |
| [SRC-1AE03B9EC3-L004949](../../agents/web_agent.py#L4949) | 4949 | `"                answer += \"\\n- \" + source[\"title\"] + \" — \" + source[\"url\"]"` | — |
| [SRC-1AE03B9EC3-L004950](../../agents/web_agent.py#L4950) | 4950 | `"        max_citable_sources = min(MAX_LLM_CITED_SOURCES, len(sources))"` | — |
| [SRC-1AE03B9EC3-L004951](../../agents/web_agent.py#L4951) | 4951 | `"        answer, citation_warnings = self._remove_invalid_citations("` | — |
| [SRC-1AE03B9EC3-L004952](../../agents/web_agent.py#L4952) | 4952 | `"            answer, max_citable_sources"` | — |
| [SRC-1AE03B9EC3-L004953](../../agents/web_agent.py#L4953) | 4953 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004954](../../agents/web_agent.py#L4954) | 4954 | `"        citation_validation = self._citation_validation_metadata("` | — |
| [SRC-1AE03B9EC3-L004955](../../agents/web_agent.py#L4955) | 4955 | `"            answer, max_citable_sources, citation_warnings, review_status"` | — |
| [SRC-1AE03B9EC3-L004956](../../agents/web_agent.py#L4956) | 4956 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004957](../../agents/web_agent.py#L4957) | 4957 | `"        report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004958](../../agents/web_agent.py#L4958) | 4958 | `"        report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L004959](../../agents/web_agent.py#L4959) | 4959 | `"        report[\"second_pass_review\"] = review_status"` | — |
| [SRC-1AE03B9EC3-L004960](../../agents/web_agent.py#L4960) | 4960 | `"        report[\"claim_audit\"] = review_status"` | — |
| [SRC-1AE03B9EC3-L004961](../../agents/web_agent.py#L4961) | 4961 | `"        answer_coverage = {"` | — |
| [SRC-1AE03B9EC3-L004962](../../agents/web_agent.py#L4962) | 4962 | `"            \"method\": \"explicit_criteria_heuristic\","` | — |
| [SRC-1AE03B9EC3-L004963](../../agents/web_agent.py#L4963) | 4963 | `"            \"targets\": coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L004964](../../agents/web_agent.py#L4964) | 4964 | `"            \"review_prompted\": review_status == \"model_claim_audit_completed\","` | — |
| [SRC-1AE03B9EC3-L004965](../../agents/web_agent.py#L4965) | 4965 | `"            \"status\": ("` | — |
| [SRC-1AE03B9EC3-L004966](../../agents/web_agent.py#L4966) | 4966 | `"                \"model_review_requested_not_machine_verified\""` | — |
| [SRC-1AE03B9EC3-L004967](../../agents/web_agent.py#L4967) | 4967 | `"                if coverage_targets and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L004968](../../agents/web_agent.py#L4968) | 4968 | `"                else \"review_unavailable\""` | — |
| [SRC-1AE03B9EC3-L004969](../../agents/web_agent.py#L4969) | 4969 | `"                if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L004970](../../agents/web_agent.py#L4970) | 4970 | `"                else \"no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L004971](../../agents/web_agent.py#L4971) | 4971 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L004972](../../agents/web_agent.py#L4972) | 4972 | `"            \"automatically_graded\": False,"` | — |
| [SRC-1AE03B9EC3-L004973](../../agents/web_agent.py#L4973) | 4973 | `"        }"` | — |
| [SRC-1AE03B9EC3-L004974](../../agents/web_agent.py#L4974) | 4974 | `"        report[\"answer_coverage\"] = answer_coverage"` | — |
| [SRC-1AE03B9EC3-L004975](../../agents/web_agent.py#L4975) | 4975 | `"        report[\"coverage_repair_status\"] = coverage_repair_status"` | — |
| [SRC-1AE03B9EC3-L004976](../../agents/web_agent.py#L4976) | 4976 | `"        answer_integrity = audit_answer_integrity(question, answer, sources, coverage_targets)"` | — |
| [SRC-1AE03B9EC3-L004977](../../agents/web_agent.py#L4977) | 4977 | `"        answer_coverage[\"target_checks\"] = answer_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L004978](../../agents/web_agent.py#L4978) | 4978 | `"        answer_coverage[\"potentially_missing_target_count\"] = answer_integrity[\"potentially_missing_target_count\"]"` | — |
| [SRC-1AE03B9EC3-L004979](../../agents/web_agent.py#L4979) | 4979 | `"        answer_coverage[\"lexical_screen_method\"] = \"deterministic_lexical_screen_only_not_semantic_grading\""` | — |
| [SRC-1AE03B9EC3-L004980](../../agents/web_agent.py#L4980) | 4980 | `"        task_fulfillment_status = ("` | — |
| [SRC-1AE03B9EC3-L004981](../../agents/web_agent.py#L4981) | 4981 | `"            \"possible_gap_detected\" if answer_integrity[\"potentially_missing_target_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L004982](../../agents/web_agent.py#L4982) | 4982 | `"            else \"lexical_signals_found_not_semantically_verified\" if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L004983](../../agents/web_agent.py#L4983) | 4983 | `"            else \"not_machine_assessed_no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L004984](../../agents/web_agent.py#L4984) | 4984 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004985](../../agents/web_agent.py#L4985) | 4985 | `"        answer_coverage[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L004986](../../agents/web_agent.py#L4986) | 4986 | `"        report[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L004987](../../agents/web_agent.py#L4987) | 4987 | `"        report[\"answer_integrity\"] = answer_integrity"` | — |
| [SRC-1AE03B9EC3-L004988](../../agents/web_agent.py#L4988) | 4988 | `"        report[\"connector_summary\"] = self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L004989](../../agents/web_agent.py#L4989) | 4989 | `"            list(self._provider_diagnostics), sources"` | — |
| [SRC-1AE03B9EC3-L004990](../../agents/web_agent.py#L4990) | 4990 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004991](../../agents/web_agent.py#L4991) | 4991 | `"        report[\"provider_diagnostics\"] = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L004992](../../agents/web_agent.py#L4992) | 4992 | `"        distinct_providers = {"` | — |
| [SRC-1AE03B9EC3-L004993](../../agents/web_agent.py#L4993) | 4993 | `"            provider for source in sources for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L004994](../../agents/web_agent.py#L4994) | 4994 | `"        }"` | — |
| [SRC-1AE03B9EC3-L004995](../../agents/web_agent.py#L4995) | 4995 | `"        distinct_domains = {"` | — |
| [SRC-1AE03B9EC3-L004996](../../agents/web_agent.py#L4996) | 4996 | `"            registrable_domain("` | — |
| [SRC-1AE03B9EC3-L004997](../../agents/web_agent.py#L4997) | 4997 | `"                source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L004998](../../agents/web_agent.py#L4998) | 4998 | `"                or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L004999](../../agents/web_agent.py#L4999) | 4999 | `"                or \"\""` | — |
| [SRC-1AE03B9EC3-L005000](../../agents/web_agent.py#L5000) | 5000 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005001](../../agents/web_agent.py#L5001) | 5001 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L005002](../../agents/web_agent.py#L5002) | 5002 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005003](../../agents/web_agent.py#L5003) | 5003 | `"        distinct_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L005004](../../agents/web_agent.py#L5004) | 5004 | `"        fetched_pages = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L005005](../../agents/web_agent.py#L5005) | 5005 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L005006](../../agents/web_agent.py#L5006) | 5006 | `"            len(sources) >= 4 and len(distinct_domains) >= 3"` | — |
| [SRC-1AE03B9EC3-L005007](../../agents/web_agent.py#L5007) | 5007 | `"            and len(distinct_providers) >= 2 and fetched_pages >= 1"` | — |
| [SRC-1AE03B9EC3-L005008](../../agents/web_agent.py#L5008) | 5008 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005009](../../agents/web_agent.py#L5009) | 5009 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L005010](../../agents/web_agent.py#L5010) | 5010 | `"            research_quality = \"excellent\""` | — |
| [SRC-1AE03B9EC3-L005011](../../agents/web_agent.py#L5011) | 5011 | `"        elif ("` | — |
| [SRC-1AE03B9EC3-L005012](../../agents/web_agent.py#L5012) | 5012 | `"            len(sources) >= 2 and len(distinct_domains) >= 2"` | — |
| [SRC-1AE03B9EC3-L005013](../../agents/web_agent.py#L5013) | 5013 | `"            and (len(distinct_providers) >= 2 or fetched_pages >= 1)"` | — |
| [SRC-1AE03B9EC3-L005014](../../agents/web_agent.py#L5014) | 5014 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005015](../../agents/web_agent.py#L5015) | 5015 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L005016](../../agents/web_agent.py#L5016) | 5016 | `"            research_quality = \"good\""` | — |
| [SRC-1AE03B9EC3-L005017](../../agents/web_agent.py#L5017) | 5017 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L005018](../../agents/web_agent.py#L5018) | 5018 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L005019](../../agents/web_agent.py#L5019) | 5019 | `""` | — |
| [SRC-1AE03B9EC3-L005020](../../agents/web_agent.py#L5020) | 5020 | `"        # Source breadth and a completed model-assisted review do not justify a"` | — |
| [SRC-1AE03B9EC3-L005021](../../agents/web_agent.py#L5021) | 5021 | `"        # positive research-quality label if the final answer has no valid source"` | — |
| [SRC-1AE03B9EC3-L005022](../../agents/web_agent.py#L5022) | 5022 | `"        # citation markers. This is a deterministic presentation guard, not a"` | — |
| [SRC-1AE03B9EC3-L005023](../../agents/web_agent.py#L5023) | 5023 | `"        # semantic entailment check."` | — |
| [SRC-1AE03B9EC3-L005024](../../agents/web_agent.py#L5024) | 5024 | `"        uncited_reviewed_answer = ("` | — |
| [SRC-1AE03B9EC3-L005025](../../agents/web_agent.py#L5025) | 5025 | `"            used_llm"` | — |
| [SRC-1AE03B9EC3-L005026](../../agents/web_agent.py#L5026) | 5026 | `"            and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L005027](../../agents/web_agent.py#L5027) | 5027 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005028](../../agents/web_agent.py#L5028) | 5028 | `"            and citation_validation[\"valid_citation_count\"] == 0"` | — |
| [SRC-1AE03B9EC3-L005029](../../agents/web_agent.py#L5029) | 5029 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005030](../../agents/web_agent.py#L5030) | 5030 | `"        if uncited_reviewed_answer:"` | — |
| [SRC-1AE03B9EC3-L005031](../../agents/web_agent.py#L5031) | 5031 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L005032](../../agents/web_agent.py#L5032) | 5032 | `"            citation_validation[\"claim_support\"] = \"not_established_no_valid_source_citations\""` | — |
| [SRC-1AE03B9EC3-L005033](../../agents/web_agent.py#L5033) | 5033 | `"            answer_evidence_status = \"reviewed_answer_has_no_valid_citations\""` | — |
| [SRC-1AE03B9EC3-L005034](../../agents/web_agent.py#L5034) | 5034 | `"            uncited_answer_warning = ("` | — |
| [SRC-1AE03B9EC3-L005035](../../agents/web_agent.py#L5035) | 5035 | `"                \"اكتملت مراجعة النموذج، لكن الإجابة النهائية لا تحتوي على إحالات صالحة \""` | — |
| [SRC-1AE03B9EC3-L005036](../../agents/web_agent.py#L5036) | 5036 | `"                \"إلى قائمة المصادر؛ لذلك صُنّفت جودة البحث «جزئية». وجود المصادر أو \""` | — |
| [SRC-1AE03B9EC3-L005037](../../agents/web_agent.py#L5037) | 5037 | `"                \"اكتمال مراجعة النموذج لا يثبت دعم كل ادعاء.\""` | — |
| [SRC-1AE03B9EC3-L005038](../../agents/web_agent.py#L5038) | 5038 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005039](../../agents/web_agent.py#L5039) | 5039 | `"        elif citation_validation[\"valid_citation_count\"] > 0:"` | — |
| [SRC-1AE03B9EC3-L005040](../../agents/web_agent.py#L5040) | 5040 | `"            answer_evidence_status = \"citation_indices_validated_only\""` | — |
| [SRC-1AE03B9EC3-L005041](../../agents/web_agent.py#L5041) | 5041 | `"            uncited_answer_warning = None"` | — |
| [SRC-1AE03B9EC3-L005042](../../agents/web_agent.py#L5042) | 5042 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L005043](../../agents/web_agent.py#L5043) | 5043 | `"            answer_evidence_status = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L005044](../../agents/web_agent.py#L5044) | 5044 | `"            uncited_answer_warning = None"` | — |
| [SRC-1AE03B9EC3-L005045](../../agents/web_agent.py#L5045) | 5045 | `""` | — |
| [SRC-1AE03B9EC3-L005046](../../agents/web_agent.py#L5046) | 5046 | `"        search_attempted = search_attempted or bool(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L005047](../../agents/web_agent.py#L5047) | 5047 | `"        report[\"search_attempted\"] = search_attempted"` | — |
| [SRC-1AE03B9EC3-L005048](../../agents/web_agent.py#L5048) | 5048 | `"        report[\"search_outcome\"] = ("` | — |
| [SRC-1AE03B9EC3-L005049](../../agents/web_agent.py#L5049) | 5049 | `"            \"attempted_with_usable_sources\" if search_attempted and sources"` | — |
| [SRC-1AE03B9EC3-L005050](../../agents/web_agent.py#L5050) | 5050 | `"            else \"attempted_no_usable_sources\" if search_attempted"` | — |
| [SRC-1AE03B9EC3-L005051](../../agents/web_agent.py#L5051) | 5051 | `"            else \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L005052](../../agents/web_agent.py#L5052) | 5052 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005053](../../agents/web_agent.py#L5053) | 5053 | `"        report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005054](../../agents/web_agent.py#L5054) | 5054 | `"        report[\"research_quality\"] = research_quality"` | — |
| [SRC-1AE03B9EC3-L005055](../../agents/web_agent.py#L5055) | 5055 | `"        report[\"research_quality_semantics\"] = \"process_coverage_not_factual_probability\""` | — |
| [SRC-1AE03B9EC3-L005056](../../agents/web_agent.py#L5056) | 5056 | `"        report[\"answer_evidence_status\"] = answer_evidence_status"` | — |
| [SRC-1AE03B9EC3-L005057](../../agents/web_agent.py#L5057) | 5057 | `"        report[\"distinct_registrable_domains\"] = len(distinct_domains)"` | — |
| [SRC-1AE03B9EC3-L005058](../../agents/web_agent.py#L5058) | 5058 | `"        report[\"independent_sources\"] = len(distinct_domains)  # Legacy alias; not editorial independence."` | — |
| [SRC-1AE03B9EC3-L005059](../../agents/web_agent.py#L5059) | 5059 | `"        report[\"independent_sources_field_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L005060](../../agents/web_agent.py#L5060) | 5060 | `"            \"legacy_compatibility_alias_for_distinct_registrable_domain_count\""` | — |
| [SRC-1AE03B9EC3-L005061](../../agents/web_agent.py#L5061) | 5061 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005062](../../agents/web_agent.py#L5062) | 5062 | `"        report[\"source_diversity_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L005063](../../agents/web_agent.py#L5063) | 5063 | `"            \"distinct_registrable_domains_not_editorial_independence\""` | — |
| [SRC-1AE03B9EC3-L005064](../../agents/web_agent.py#L5064) | 5064 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005065](../../agents/web_agent.py#L5065) | 5065 | `"        report[\"editorial_independence_status\"] = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L005066](../../agents/web_agent.py#L5066) | 5066 | `"        report[\"claim_audit_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L005067](../../agents/web_agent.py#L5067) | 5067 | `"            \"model_assisted_not_independent_fact_check\""` | — |
| [SRC-1AE03B9EC3-L005068](../../agents/web_agent.py#L5068) | 5068 | `"            if review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005069](../../agents/web_agent.py#L5069) | 5069 | `"            else \"not_verified\""` | — |
| [SRC-1AE03B9EC3-L005070](../../agents/web_agent.py#L5070) | 5070 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005071](../../agents/web_agent.py#L5071) | 5071 | `"        report[\"insufficient_evidence\"] = False"` | — |
| [SRC-1AE03B9EC3-L005072](../../agents/web_agent.py#L5072) | 5072 | `"        report[\"valid_citation_range\"] = [1, max_citable_sources] if max_citable_sources else []"` | — |
| [SRC-1AE03B9EC3-L005073](../../agents/web_agent.py#L5073) | 5073 | `"        report[\"citation_count\"] = citation_validation[\"valid_citation_count\"]"` | — |
| [SRC-1AE03B9EC3-L005074](../../agents/web_agent.py#L5074) | 5074 | `"        report[\"citation_check\"] = citation_validation[\"status\"]"` | — |
| [SRC-1AE03B9EC3-L005075](../../agents/web_agent.py#L5075) | 5075 | `"        report[\"citation_validation\"] = citation_validation"` | — |
| [SRC-1AE03B9EC3-L005076](../../agents/web_agent.py#L5076) | 5076 | `"        warnings = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L005077](../../agents/web_agent.py#L5077) | 5077 | `"            search_warnings"` | — |
| [SRC-1AE03B9EC3-L005078](../../agents/web_agent.py#L5078) | 5078 | `"            + ([llm_warning] if llm_warning else [])"` | — |
| [SRC-1AE03B9EC3-L005079](../../agents/web_agent.py#L5079) | 5079 | `"            + ([review_warning] if review_warning else [])"` | — |
| [SRC-1AE03B9EC3-L005080](../../agents/web_agent.py#L5080) | 5080 | `"            + ([coverage_repair_warning] if coverage_repair_warning else [])"` | — |
| [SRC-1AE03B9EC3-L005081](../../agents/web_agent.py#L5081) | 5081 | `"            + citation_warnings"` | — |
| [SRC-1AE03B9EC3-L005082](../../agents/web_agent.py#L5082) | 5082 | `"            + ([uncited_answer_warning] if uncited_answer_warning else [])"` | — |
| [SRC-1AE03B9EC3-L005083](../../agents/web_agent.py#L5083) | 5083 | `"        ))"` | — |
| [SRC-1AE03B9EC3-L005084](../../agents/web_agent.py#L5084) | 5084 | `"        report[\"model_calls\"] = list(self.model_usage)"` | — |
| [SRC-1AE03B9EC3-L005085](../../agents/web_agent.py#L5085) | 5085 | `"        report[\"openrouter_web_search_enabled\"] = self.openrouter_web_search_enabled"` | — |
| [SRC-1AE03B9EC3-L005086](../../agents/web_agent.py#L5086) | 5086 | `"        report[\"openrouter_web_search_results\"] = len(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L005087](../../agents/web_agent.py#L5087) | 5087 | `"        if generation_budget_exhausted or review_budget_exhausted:"` | — |
| [SRC-1AE03B9EC3-L005088](../../agents/web_agent.py#L5088) | 5088 | `"            final_answer_status = \"budget_exhausted_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L005089](../../agents/web_agent.py#L5089) | 5089 | `"        elif llm_warning:"` | — |
| [SRC-1AE03B9EC3-L005090](../../agents/web_agent.py#L5090) | 5090 | `"            final_answer_status = ("` | — |
| [SRC-1AE03B9EC3-L005091](../../agents/web_agent.py#L5091) | 5091 | `"                \"model_not_configured_fallback\""` | — |
| [SRC-1AE03B9EC3-L005092](../../agents/web_agent.py#L5092) | 5092 | `"                if not self.api_key"` | — |
| [SRC-1AE03B9EC3-L005093](../../agents/web_agent.py#L5093) | 5093 | `"                else \"generation_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L005094](../../agents/web_agent.py#L5094) | 5094 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005095](../../agents/web_agent.py#L5095) | 5095 | `"        elif review_warning:"` | — |
| [SRC-1AE03B9EC3-L005096](../../agents/web_agent.py#L5096) | 5096 | `"            final_answer_status = \"review_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L005097](../../agents/web_agent.py#L5097) | 5097 | `"        elif coverage_repair_status == \"no_change_gap_unresolved\":"` | — |
| [SRC-1AE03B9EC3-L005098](../../agents/web_agent.py#L5098) | 5098 | `"            final_answer_status = \"coverage_repair_left_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L005099](../../agents/web_agent.py#L5099) | 5099 | `"        elif coverage_repair_status == \"budget_exhausted\":"` | — |
| [SRC-1AE03B9EC3-L005100](../../agents/web_agent.py#L5100) | 5100 | `"            final_answer_status = \"coverage_repair_budget_exhausted_with_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L005101](../../agents/web_agent.py#L5101) | 5101 | `"        elif coverage_repair_status == \"unavailable\":"` | — |
| [SRC-1AE03B9EC3-L005102](../../agents/web_agent.py#L5102) | 5102 | `"            final_answer_status = \"coverage_repair_unavailable_with_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L005103](../../agents/web_agent.py#L5103) | 5103 | `"        elif used_llm:"` | — |
| [SRC-1AE03B9EC3-L005104](../../agents/web_agent.py#L5104) | 5104 | `"            final_answer_status = \"model_answer_generated\""` | — |
| [SRC-1AE03B9EC3-L005105](../../agents/web_agent.py#L5105) | 5105 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L005106](../../agents/web_agent.py#L5106) | 5106 | `"            final_answer_status = \"source_fallback\""` | — |
| [SRC-1AE03B9EC3-L005107](../../agents/web_agent.py#L5107) | 5107 | `""` | — |
| [SRC-1AE03B9EC3-L005108](../../agents/web_agent.py#L5108) | 5108 | `"        public_sources = []"` | — |
| [SRC-1AE03B9EC3-L005109](../../agents/web_agent.py#L5109) | 5109 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L005110](../../agents/web_agent.py#L5110) | 5110 | `"            public_sources.append({"` | — |
| [SRC-1AE03B9EC3-L005111](../../agents/web_agent.py#L5111) | 5111 | `"                \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L005112](../../agents/web_agent.py#L5112) | 5112 | `"                \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L005113](../../agents/web_agent.py#L5113) | 5113 | `"                \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005114](../../agents/web_agent.py#L5114) | 5114 | `"                \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L005115](../../agents/web_agent.py#L5115) | 5115 | `"                \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L005116](../../agents/web_agent.py#L5116) | 5116 | `"                \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L005117](../../agents/web_agent.py#L5117) | 5117 | `"                \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L005118](../../agents/web_agent.py#L5118) | 5118 | `"                \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005119](../../agents/web_agent.py#L5119) | 5119 | `"                \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L005120](../../agents/web_agent.py#L5120) | 5120 | `"                \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005121](../../agents/web_agent.py#L5121) | 5121 | `"                \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005122](../../agents/web_agent.py#L5122) | 5122 | `"                \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005123](../../agents/web_agent.py#L5123) | 5123 | `"                \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L005124](../../agents/web_agent.py#L5124) | 5124 | `"                \"lead_qualification\": source.get(\"lead_qualification\"),"` | — |
| [SRC-1AE03B9EC3-L005125](../../agents/web_agent.py#L5125) | 5125 | `"                \"lead_intent_evidence\": source.get(\"lead_intent_evidence\"),"` | — |
| [SRC-1AE03B9EC3-L005126](../../agents/web_agent.py#L5126) | 5126 | `"            })"` | — |
| [SRC-1AE03B9EC3-L005127](../../agents/web_agent.py#L5127) | 5127 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L005128](../../agents/web_agent.py#L5128) | 5128 | `"            \"answer\": answer,"` | — |
| [SRC-1AE03B9EC3-L005129](../../agents/web_agent.py#L5129) | 5129 | `"            \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L005130](../../agents/web_agent.py#L5130) | 5130 | `"            \"search_query\": (plan.get(\"queries\") or [\"\"])[0],"` | — |
| [SRC-1AE03B9EC3-L005131](../../agents/web_agent.py#L5131) | 5131 | `"            \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L005132](../../agents/web_agent.py#L5132) | 5132 | `"            \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L005133](../../agents/web_agent.py#L5133) | 5133 | `"                \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L005134](../../agents/web_agent.py#L5134) | 5134 | `"                \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L005135](../../agents/web_agent.py#L5135) | 5135 | `"                \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L005136](../../agents/web_agent.py#L5136) | 5136 | `"                \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L005137](../../agents/web_agent.py#L5137) | 5137 | `"                \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L005138](../../agents/web_agent.py#L5138) | 5138 | `"                \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L005139](../../agents/web_agent.py#L5139) | 5139 | `"                \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L005140](../../agents/web_agent.py#L5140) | 5140 | `"                \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L005141](../../agents/web_agent.py#L5141) | 5141 | `"                \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L005142](../../agents/web_agent.py#L5142) | 5142 | `"            },"` | — |
| [SRC-1AE03B9EC3-L005143](../../agents/web_agent.py#L5143) | 5143 | `"            \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L005144](../../agents/web_agent.py#L5144) | 5144 | `"            \"sources\": public_sources,"` | — |
| [SRC-1AE03B9EC3-L005145](../../agents/web_agent.py#L5145) | 5145 | `"            \"research_quality\": research_quality,"` | — |
| [SRC-1AE03B9EC3-L005146](../../agents/web_agent.py#L5146) | 5146 | `"            \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L005147](../../agents/web_agent.py#L5147) | 5147 | `"            \"answer_evidence_status\": answer_evidence_status,"` | — |
| [SRC-1AE03B9EC3-L005148](../../agents/web_agent.py#L5148) | 5148 | `"            \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L005149](../../agents/web_agent.py#L5149) | 5149 | `"            \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L005150](../../agents/web_agent.py#L5150) | 5150 | `"            \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L005151](../../agents/web_agent.py#L5151) | 5151 | `"            \"coverage_repair_status\": coverage_repair_status,"` | — |
| [SRC-1AE03B9EC3-L005152](../../agents/web_agent.py#L5152) | 5152 | `"            \"used_language_model\": used_llm,"` | — |
| [SRC-1AE03B9EC3-L005153](../../agents/web_agent.py#L5153) | 5153 | `"            \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L005154](../../agents/web_agent.py#L5154) | 5154 | `"            \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L005155](../../agents/web_agent.py#L5155) | 5155 | `"            \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L005156](../../agents/web_agent.py#L5156) | 5156 | `"            \"warnings\": warnings,"` | — |
| [SRC-1AE03B9EC3-L005157](../../agents/web_agent.py#L5157) | 5157 | `"            \"kind\": \"web_research\" if used_llm else \"web_fallback\","` | — |
| [SRC-1AE03B9EC3-L005158](../../agents/web_agent.py#L5158) | 5158 | `"            \"final_answer_status\": final_answer_status,"` | — |
| [SRC-1AE03B9EC3-L005159](../../agents/web_agent.py#L5159) | 5159 | `"            \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L005160](../../agents/web_agent.py#L5160) | 5160 | `"            \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L005161](../../agents/web_agent.py#L5161) | 5161 | `"        }"` | — |
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
