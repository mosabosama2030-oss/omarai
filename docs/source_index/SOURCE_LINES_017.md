# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **017**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L005690 إلى SRC-1AE03B9EC3-L006489
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L005690](../../agents/web_agent.py#L5690) | 5690 | `"        report[\"provider_diagnostics\"] = current_research_diagnostics"` | — |
| [SRC-1AE03B9EC3-L005691](../../agents/web_agent.py#L5691) | 5691 | `"        provider_attempt_observed = any("` | — |
| [SRC-1AE03B9EC3-L005692](../../agents/web_agent.py#L5692) | 5692 | `"            item.get(\"status\") in _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES"` | — |
| [SRC-1AE03B9EC3-L005693](../../agents/web_agent.py#L5693) | 5693 | `"            for item in current_research_diagnostics"` | — |
| [SRC-1AE03B9EC3-L005694](../../agents/web_agent.py#L5694) | 5694 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005695](../../agents/web_agent.py#L5695) | 5695 | `"        raw_attempt_count = report.get(\"queries_attempted\", 0)"` | — |
| [SRC-1AE03B9EC3-L005696](../../agents/web_agent.py#L5696) | 5696 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L005697](../../agents/web_agent.py#L5697) | 5697 | `"            queries_attempted = ("` | — |
| [SRC-1AE03B9EC3-L005698](../../agents/web_agent.py#L5698) | 5698 | `"                None if raw_attempt_count is None"` | — |
| [SRC-1AE03B9EC3-L005699](../../agents/web_agent.py#L5699) | 5699 | `"                else max(0, int(raw_attempt_count or 0))"` | — |
| [SRC-1AE03B9EC3-L005700](../../agents/web_agent.py#L5700) | 5700 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005701](../../agents/web_agent.py#L5701) | 5701 | `"        except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L005702](../../agents/web_agent.py#L5702) | 5702 | `"            queries_attempted = None"` | — |
| [SRC-1AE03B9EC3-L005703](../../agents/web_agent.py#L5703) | 5703 | `"        if queries_attempted is not None:"` | — |
| [SRC-1AE03B9EC3-L005704](../../agents/web_agent.py#L5704) | 5704 | `"            search_attempted = ("` | — |
| [SRC-1AE03B9EC3-L005705](../../agents/web_agent.py#L5705) | 5705 | `"                queries_attempted > 0"` | — |
| [SRC-1AE03B9EC3-L005706](../../agents/web_agent.py#L5706) | 5706 | `"                or provider_attempt_observed"` | — |
| [SRC-1AE03B9EC3-L005707](../../agents/web_agent.py#L5707) | 5707 | `"                or report.get(\"search_attempted\") is True"` | — |
| [SRC-1AE03B9EC3-L005708](../../agents/web_agent.py#L5708) | 5708 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005709](../../agents/web_agent.py#L5709) | 5709 | `"        elif provider_attempt_observed or report.get(\"search_attempted\") is True:"` | — |
| [SRC-1AE03B9EC3-L005710](../../agents/web_agent.py#L5710) | 5710 | `"            search_attempted = True"` | — |
| [SRC-1AE03B9EC3-L005711](../../agents/web_agent.py#L5711) | 5711 | `"        elif isinstance(report.get(\"search_attempted\"), bool):"` | — |
| [SRC-1AE03B9EC3-L005712](../../agents/web_agent.py#L5712) | 5712 | `"            search_attempted = report[\"search_attempted\"]"` | — |
| [SRC-1AE03B9EC3-L005713](../../agents/web_agent.py#L5713) | 5713 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L005714](../../agents/web_agent.py#L5714) | 5714 | `"            search_attempted = None"` | — |
| [SRC-1AE03B9EC3-L005715](../../agents/web_agent.py#L5715) | 5715 | `"        report[\"queries_attempted\"] = queries_attempted"` | — |
| [SRC-1AE03B9EC3-L005716](../../agents/web_agent.py#L5716) | 5716 | `"        report[\"queries_attempted_known\"] = queries_attempted is not None"` | — |
| [SRC-1AE03B9EC3-L005717](../../agents/web_agent.py#L5717) | 5717 | `"        report[\"search_attempted\"] = search_attempted"` | — |
| [SRC-1AE03B9EC3-L005718](../../agents/web_agent.py#L5718) | 5718 | `"        previous_search_outcome = report.get(\"search_outcome\")"` | — |
| [SRC-1AE03B9EC3-L005719](../../agents/web_agent.py#L5719) | 5719 | `"        if previous_search_outcome in _RESEARCH_ERROR_OUTCOMES and not sources:"` | — |
| [SRC-1AE03B9EC3-L005720](../../agents/web_agent.py#L5720) | 5720 | `"            if provider_attempt_observed or search_attempted is True:"` | — |
| [SRC-1AE03B9EC3-L005721](../../agents/web_agent.py#L5721) | 5721 | `"                search_outcome = \"attempted_research_error\""` | — |
| [SRC-1AE03B9EC3-L005722](../../agents/web_agent.py#L5722) | 5722 | `"            elif search_attempted is False:"` | — |
| [SRC-1AE03B9EC3-L005723](../../agents/web_agent.py#L5723) | 5723 | `"                search_outcome = \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L005724](../../agents/web_agent.py#L5724) | 5724 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L005725](../../agents/web_agent.py#L5725) | 5725 | `"                search_outcome = \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L005726](../../agents/web_agent.py#L5726) | 5726 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L005727](../../agents/web_agent.py#L5727) | 5727 | `"            search_outcome = ("` | — |
| [SRC-1AE03B9EC3-L005728](../../agents/web_agent.py#L5728) | 5728 | `"                \"attempted_with_usable_sources\" if search_attempted is True and sources"` | — |
| [SRC-1AE03B9EC3-L005729](../../agents/web_agent.py#L5729) | 5729 | `"                else \"attempted_no_usable_sources\" if search_attempted is True"` | — |
| [SRC-1AE03B9EC3-L005730](../../agents/web_agent.py#L5730) | 5730 | `"                else \"not_attempted\" if search_attempted is False"` | — |
| [SRC-1AE03B9EC3-L005731](../../agents/web_agent.py#L5731) | 5731 | `"                else \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L005732](../../agents/web_agent.py#L5732) | 5732 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005733](../../agents/web_agent.py#L5733) | 5733 | `"        report[\"search_outcome\"] = search_outcome"` | — |
| [SRC-1AE03B9EC3-L005734](../../agents/web_agent.py#L5734) | 5734 | `"        if search_outcome in _RESEARCH_ERROR_OUTCOMES:"` | — |
| [SRC-1AE03B9EC3-L005735](../../agents/web_agent.py#L5735) | 5735 | `"            report[\"usable_sources_after_filtering\"] = None"` | — |
| [SRC-1AE03B9EC3-L005736](../../agents/web_agent.py#L5736) | 5736 | `"            report[\"unique_sources\"] = None"` | — |
| [SRC-1AE03B9EC3-L005737](../../agents/web_agent.py#L5737) | 5737 | `"            report[\"pages_fetched\"] = None"` | — |
| [SRC-1AE03B9EC3-L005738](../../agents/web_agent.py#L5738) | 5738 | `"            report[\"provider_counts\"] = None"` | — |
| [SRC-1AE03B9EC3-L005739](../../agents/web_agent.py#L5739) | 5739 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L005740](../../agents/web_agent.py#L5740) | 5740 | `"            report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005741](../../agents/web_agent.py#L5741) | 5741 | `"            if report.get(\"unique_sources\") is None and sources:"` | — |
| [SRC-1AE03B9EC3-L005742](../../agents/web_agent.py#L5742) | 5742 | `"                report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005743](../../agents/web_agent.py#L5743) | 5743 | `"            if report.get(\"pages_fetched\") is None and sources:"` | — |
| [SRC-1AE03B9EC3-L005744](../../agents/web_agent.py#L5744) | 5744 | `"                report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L005745](../../agents/web_agent.py#L5745) | 5745 | `"        report[\"research_quality_semantics\"] = \"process_coverage_not_factual_probability\""` | — |
| [SRC-1AE03B9EC3-L005746](../../agents/web_agent.py#L5746) | 5746 | `"        report[\"distinct_registrable_domains\"] = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L005747](../../agents/web_agent.py#L5747) | 5747 | `"        report[\"independent_sources\"] = len(independent_domains)  # Legacy alias; not editorial independence."` | — |
| [SRC-1AE03B9EC3-L005748](../../agents/web_agent.py#L5748) | 5748 | `"        report[\"independent_sources_field_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L005749](../../agents/web_agent.py#L5749) | 5749 | `"            \"legacy_compatibility_alias_for_distinct_registrable_domain_count\""` | — |
| [SRC-1AE03B9EC3-L005750](../../agents/web_agent.py#L5750) | 5750 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005751](../../agents/web_agent.py#L5751) | 5751 | `"        report[\"source_diversity_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L005752](../../agents/web_agent.py#L5752) | 5752 | `"            \"distinct_registrable_domains_not_editorial_independence\""` | — |
| [SRC-1AE03B9EC3-L005753](../../agents/web_agent.py#L5753) | 5753 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005754](../../agents/web_agent.py#L5754) | 5754 | `"        report[\"editorial_independence_status\"] = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L005755](../../agents/web_agent.py#L5755) | 5755 | `"        if len(independent_domains) >= 2:"` | — |
| [SRC-1AE03B9EC3-L005756](../../agents/web_agent.py#L5756) | 5756 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005757](../../agents/web_agent.py#L5757) | 5757 | `"                \"تعدد النطاقات المسجلة لا يثبت الاستقلال التحريري؛ قد تنقل المواقع عن المصدر الأصلي نفسه.\""` | — |
| [SRC-1AE03B9EC3-L005758](../../agents/web_agent.py#L5758) | 5758 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005759](../../agents/web_agent.py#L5759) | 5759 | `"        search_warning = \"؛ \".join(dict.fromkeys(search_warnings)) if search_warnings else None"` | — |
| [SRC-1AE03B9EC3-L005760](../../agents/web_agent.py#L5760) | 5760 | `"        if needs_corroboration and single_source_navigation and not single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L005761](../../agents/web_agent.py#L5761) | 5761 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005762](../../agents/web_agent.py#L5762) | 5762 | `"                \"هذه نتيجة مرشحة لطلب العثور على موقع/رابط؛ لم تُثبت رسميتها أو صحتها \""` | — |
| [SRC-1AE03B9EC3-L005763](../../agents/web_agent.py#L5763) | 5763 | `"                \"من مصدر مستقل، لذا راجع الرابط قبل الاعتماد عليه.\""` | — |
| [SRC-1AE03B9EC3-L005764](../../agents/web_agent.py#L5764) | 5764 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005765](../../agents/web_agent.py#L5765) | 5765 | `"        if needs_corroboration and (single_source_social or single_source_lead) and not single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L005766](../../agents/web_agent.py#L5766) | 5766 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005767](../../agents/web_agent.py#L5767) | 5767 | `"                \"هذه إشارات بحث أولية وليست تحققًا مستقلًا من هوية العميل أو نيته؛ \""` | — |
| [SRC-1AE03B9EC3-L005768](../../agents/web_agent.py#L5768) | 5768 | `"                \"راجع المنشور وتاريخه وسياقه قبل التواصل أو اتخاذ قرار.\""` | — |
| [SRC-1AE03B9EC3-L005769](../../agents/web_agent.py#L5769) | 5769 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005770](../../agents/web_agent.py#L5770) | 5770 | `"        if needs_corroboration and single_source_listing and not single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L005771](../../agents/web_agent.py#L5771) | 5771 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005772](../../agents/web_agent.py#L5772) | 5772 | `"                \"هذه إعلانات/قوائم مرشحة فقط. قد تكون منتهية أو غير دقيقة؛ تحقق من السعر \""` | — |
| [SRC-1AE03B9EC3-L005773](../../agents/web_agent.py#L5773) | 5773 | `"                \"والتوافر ومصدر الإعلان واطلب تأكيدًا حديثًا قبل دفع مال أو مشاركة بيانات.\""` | — |
| [SRC-1AE03B9EC3-L005774](../../agents/web_agent.py#L5774) | 5774 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005775](../../agents/web_agent.py#L5775) | 5775 | `"        search_warning = \"؛ \".join(dict.fromkeys(search_warnings)) if search_warnings else None"` | — |
| [SRC-1AE03B9EC3-L005776](../../agents/web_agent.py#L5776) | 5776 | `"        if needs_corroboration and not task_specific_partial_evidence:"` | — |
| [SRC-1AE03B9EC3-L005777](../../agents/web_agent.py#L5777) | 5777 | `"            if search_outcome == \"unknown_after_research_error\":"` | — |
| [SRC-1AE03B9EC3-L005778](../../agents/web_agent.py#L5778) | 5778 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005779](../../agents/web_agent.py#L5779) | 5779 | `"                    \"تعذر إكمال مسار البحث بسبب خطأ، ولا توجد بيانات كافية لتحديد ما إذا \""` | — |
| [SRC-1AE03B9EC3-L005780](../../agents/web_agent.py#L5780) | 5780 | `"                    \"كانت محاولة البحث قد اكتملت أو كم نتيجة جُمعت. لذلك لا أستطيع الجزم \""` | — |
| [SRC-1AE03B9EC3-L005781](../../agents/web_agent.py#L5781) | 5781 | `"                    \"بأن البحث لم يُنفّذ أو أن الإنترنت لم يُعد نتائج. لم أتمكن من تقديم \""` | — |
| [SRC-1AE03B9EC3-L005782](../../agents/web_agent.py#L5782) | 5782 | `"                    \"إجابة مكتملة؛ أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L005783](../../agents/web_agent.py#L5783) | 5783 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005784](../../agents/web_agent.py#L5784) | 5784 | `"            elif search_outcome == \"attempted_research_error\":"` | — |
| [SRC-1AE03B9EC3-L005785](../../agents/web_agent.py#L5785) | 5785 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005786](../../agents/web_agent.py#L5786) | 5786 | `"                    \"توجد قرائن تشغيلية على بدء محاولة بحث، لكن مسار البحث فشل قبل إنتاج \""` | — |
| [SRC-1AE03B9EC3-L005787](../../agents/web_agent.py#L5787) | 5787 | `"                    \"تقرير مكتمل. لا أستطيع تحديد عدد النتائج أو المصادر القابلة للاستخدام، \""` | — |
| [SRC-1AE03B9EC3-L005788](../../agents/web_agent.py#L5788) | 5788 | `"                    \"لذلك لن أخمّن. أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L005789](../../agents/web_agent.py#L5789) | 5789 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005790](../../agents/web_agent.py#L5790) | 5790 | `"            elif search_outcome == \"attempted_no_usable_sources\":"` | — |
| [SRC-1AE03B9EC3-L005791](../../agents/web_agent.py#L5791) | 5791 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005792](../../agents/web_agent.py#L5792) | 5792 | `"                    \"جرت محاولة البحث، لكن لم تتوفر مصادر صالحة وكافية للإجابة بعد تصفية \""` | — |
| [SRC-1AE03B9EC3-L005793](../../agents/web_agent.py#L5793) | 5793 | `"                    \"النتائج. هذا لا يثبت أن جميع المواقع أو الإنترنت غير متاح؛ لن أخمّن \""` | — |
| [SRC-1AE03B9EC3-L005794](../../agents/web_agent.py#L5794) | 5794 | `"                    \"أو أقدّم نتيجة غير مدعومة. جرّب صياغة أدق أو أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L005795](../../agents/web_agent.py#L5795) | 5795 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005796](../../agents/web_agent.py#L5796) | 5796 | `"            elif search_outcome == \"not_attempted\":"` | — |
| [SRC-1AE03B9EC3-L005797](../../agents/web_agent.py#L5797) | 5797 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005798](../../agents/web_agent.py#L5798) | 5798 | `"                    \"لم تبدأ محاولة بحث ويب لهذا الطلب، لذلك لا تتوفر لدي أدلة ويب حالية \""` | — |
| [SRC-1AE03B9EC3-L005799](../../agents/web_agent.py#L5799) | 5799 | `"                    \"كافية للإجابة. لن أقدّم نتيجة غير مدعومة؛ أعد المحاولة أو اطلب بحثًا \""` | — |
| [SRC-1AE03B9EC3-L005800](../../agents/web_agent.py#L5800) | 5800 | `"                    \"صريحًا إذا كان ذلك مناسبًا.\""` | — |
| [SRC-1AE03B9EC3-L005801](../../agents/web_agent.py#L5801) | 5801 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005802](../../agents/web_agent.py#L5802) | 5802 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L005803](../../agents/web_agent.py#L5803) | 5803 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005804](../../agents/web_agent.py#L5804) | 5804 | `"                    \"لم أجد معلومات موثوقة كافية مرتبطة بسؤالك من نطاقين مسجلين مختلفين على الأقل. \""` | — |
| [SRC-1AE03B9EC3-L005805](../../agents/web_agent.py#L5805) | 5805 | `"                    \"اختلاف النطاقات لا يثبت الاستقلال التحريري. لن أخمّن أو أقدّم نتيجة غير مدعومة؛ \""` | — |
| [SRC-1AE03B9EC3-L005806](../../agents/web_agent.py#L5806) | 5806 | `"                    \"جرّب صياغة أدق أو أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L005807](../../agents/web_agent.py#L5807) | 5807 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005808](../../agents/web_agent.py#L5808) | 5808 | `"            public_sources = [{"` | — |
| [SRC-1AE03B9EC3-L005809](../../agents/web_agent.py#L5809) | 5809 | `"                \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L005810](../../agents/web_agent.py#L5810) | 5810 | `"                \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L005811](../../agents/web_agent.py#L5811) | 5811 | `"                \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005812](../../agents/web_agent.py#L5812) | 5812 | `"                \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L005813](../../agents/web_agent.py#L5813) | 5813 | `"                \"readable_page_text_available\": bool(source.get(\"page_fetched\")) and bool(str(source.get(\"page_text\") or \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L005814](../../agents/web_agent.py#L5814) | 5814 | `"                \"page_text_present_without_fetch_flag\": bool(str(source.get(\"page_text\") or \"\").strip()) and not bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L005815](../../agents/web_agent.py#L5815) | 5815 | `"                \"page_fetch_status\": source.get(\"page_fetch_status\", \"unknown\"),"` | — |
| [SRC-1AE03B9EC3-L005816](../../agents/web_agent.py#L5816) | 5816 | `"                \"page_fetch_error_class\": source.get(\"page_fetch_error_class\"),"` | — |
| [SRC-1AE03B9EC3-L005817](../../agents/web_agent.py#L5817) | 5817 | `"                \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L005818](../../agents/web_agent.py#L5818) | 5818 | `"                \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L005819](../../agents/web_agent.py#L5819) | 5819 | `"                \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L005820](../../agents/web_agent.py#L5820) | 5820 | `"                \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005821](../../agents/web_agent.py#L5821) | 5821 | `"                \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L005822](../../agents/web_agent.py#L5822) | 5822 | `"                \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005823](../../agents/web_agent.py#L5823) | 5823 | `"                \"opinion_source_classification\": source.get(\"opinion_source_classification\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005824](../../agents/web_agent.py#L5824) | 5824 | `"                \"opinion_classification_basis\": source.get(\"opinion_classification_basis\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005825](../../agents/web_agent.py#L5825) | 5825 | `"                \"opinion_classification_method\": source.get(\"opinion_classification_method\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005826](../../agents/web_agent.py#L5826) | 5826 | `"                \"current_evidence_assessment\": source.get(\"current_evidence_assessment\", {}),"` | — |
| [SRC-1AE03B9EC3-L005827](../../agents/web_agent.py#L5827) | 5827 | `"                \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005828](../../agents/web_agent.py#L5828) | 5828 | `"                \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005829](../../agents/web_agent.py#L5829) | 5829 | `"                \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L005830](../../agents/web_agent.py#L5830) | 5830 | `"                \"lead_qualification\": source.get(\"lead_qualification\"),"` | — |
| [SRC-1AE03B9EC3-L005831](../../agents/web_agent.py#L5831) | 5831 | `"                \"lead_intent_evidence\": source.get(\"lead_intent_evidence\"),"` | — |
| [SRC-1AE03B9EC3-L005832](../../agents/web_agent.py#L5832) | 5832 | `"            } for source in sources]"` | — |
| [SRC-1AE03B9EC3-L005833](../../agents/web_agent.py#L5833) | 5833 | `"            citation_validation = self._citation_validation_metadata("` | — |
| [SRC-1AE03B9EC3-L005834](../../agents/web_agent.py#L5834) | 5834 | `"                reason, 0, [], \"not_run\""` | — |
| [SRC-1AE03B9EC3-L005835](../../agents/web_agent.py#L5835) | 5835 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005836](../../agents/web_agent.py#L5836) | 5836 | `"            citation_validation[\"status\"] = \"not_applicable_no_generated_answer\""` | — |
| [SRC-1AE03B9EC3-L005837](../../agents/web_agent.py#L5837) | 5837 | `"            coverage_targets = self._question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L005838](../../agents/web_agent.py#L5838) | 5838 | `"            answer_coverage = {"` | — |
| [SRC-1AE03B9EC3-L005839](../../agents/web_agent.py#L5839) | 5839 | `"                \"method\": \"explicit_criteria_heuristic\","` | — |
| [SRC-1AE03B9EC3-L005840](../../agents/web_agent.py#L5840) | 5840 | `"                \"targets\": coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L005841](../../agents/web_agent.py#L5841) | 5841 | `"                \"status\": ("` | — |
| [SRC-1AE03B9EC3-L005842](../../agents/web_agent.py#L5842) | 5842 | `"                    \"not_reviewed_insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L005843](../../agents/web_agent.py#L5843) | 5843 | `"                    if coverage_targets else \"no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L005844](../../agents/web_agent.py#L5844) | 5844 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005845](../../agents/web_agent.py#L5845) | 5845 | `"                \"automatically_graded\": False,"` | — |
| [SRC-1AE03B9EC3-L005846](../../agents/web_agent.py#L5846) | 5846 | `"            }"` | — |
| [SRC-1AE03B9EC3-L005847](../../agents/web_agent.py#L5847) | 5847 | `"            answer_integrity = audit_answer_integrity(working_question, reason, sources, coverage_targets, plan.get(\"requirement_queries\"))"` | — |
| [SRC-1AE03B9EC3-L005848](../../agents/web_agent.py#L5848) | 5848 | `"            answer_coverage[\"target_checks\"] = answer_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L005849](../../agents/web_agent.py#L5849) | 5849 | `"            answer_coverage[\"potentially_missing_target_count\"] = answer_integrity[\"potentially_missing_target_count\"]"` | — |
| [SRC-1AE03B9EC3-L005850](../../agents/web_agent.py#L5850) | 5850 | `"            answer_coverage[\"source_evidence_gap_count\"] = answer_integrity[\"source_evidence_gap_count\"]"` | — |
| [SRC-1AE03B9EC3-L005851](../../agents/web_agent.py#L5851) | 5851 | `"            answer_coverage[\"lexical_screen_method\"] = \"deterministic_lexical_screen_only_not_semantic_grading\""` | — |
| [SRC-1AE03B9EC3-L005852](../../agents/web_agent.py#L5852) | 5852 | `"            task_fulfillment_status = ("` | — |
| [SRC-1AE03B9EC3-L005853](../../agents/web_agent.py#L5853) | 5853 | `"                \"not_assessed_insufficient_evidence\" if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L005854](../../agents/web_agent.py#L5854) | 5854 | `"                else \"not_machine_assessed_no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L005855](../../agents/web_agent.py#L5855) | 5855 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005856](../../agents/web_agent.py#L5856) | 5856 | `"            answer_coverage[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L005857](../../agents/web_agent.py#L5857) | 5857 | `"            research_failed = search_outcome in _RESEARCH_ERROR_OUTCOMES"` | — |
| [SRC-1AE03B9EC3-L005858](../../agents/web_agent.py#L5858) | 5858 | `"            report.update({"` | — |
| [SRC-1AE03B9EC3-L005859](../../agents/web_agent.py#L5859) | 5859 | `"                # When collection failed, an empty local list is not evidence that"` | — |
| [SRC-1AE03B9EC3-L005860](../../agents/web_agent.py#L5860) | 5860 | `"                # the remote search returned zero sources; preserve unknown counts."` | — |
| [SRC-1AE03B9EC3-L005861](../../agents/web_agent.py#L5861) | 5861 | `"                \"unique_sources\": None if research_failed else len(sources),"` | — |
| [SRC-1AE03B9EC3-L005862](../../agents/web_agent.py#L5862) | 5862 | `"                \"independent_sources\": None if research_failed else len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L005863](../../agents/web_agent.py#L5863) | 5863 | `"                \"distinct_registrable_domains\": None if research_failed else len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L005864](../../agents/web_agent.py#L5864) | 5864 | `"                \"pages_fetched\": ("` | — |
| [SRC-1AE03B9EC3-L005865](../../agents/web_agent.py#L5865) | 5865 | `"                    None if research_failed"` | — |
| [SRC-1AE03B9EC3-L005866](../../agents/web_agent.py#L5866) | 5866 | `"                    else sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L005867](../../agents/web_agent.py#L5867) | 5867 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005868](../../agents/web_agent.py#L5868) | 5868 | `"                \"provider_diagnostics\": current_research_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L005869](../../agents/web_agent.py#L5869) | 5869 | `"                \"insufficient_evidence\": True,"` | — |
| [SRC-1AE03B9EC3-L005870](../../agents/web_agent.py#L5870) | 5870 | `"                \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L005871](../../agents/web_agent.py#L5871) | 5871 | `"                \"citation_check\": citation_validation[\"status\"],"` | — |
| [SRC-1AE03B9EC3-L005872](../../agents/web_agent.py#L5872) | 5872 | `"                \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L005873](../../agents/web_agent.py#L5873) | 5873 | `"                \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L005874](../../agents/web_agent.py#L5874) | 5874 | `"                \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L005875](../../agents/web_agent.py#L5875) | 5875 | `"                \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L005876](../../agents/web_agent.py#L5876) | 5876 | `"                \"connector_summary\": report.get(\"connector_summary\") or self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L005877](../../agents/web_agent.py#L5877) | 5877 | `"                    current_research_diagnostics, sources"` | — |
| [SRC-1AE03B9EC3-L005878](../../agents/web_agent.py#L5878) | 5878 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005879](../../agents/web_agent.py#L5879) | 5879 | `"            })"` | — |
| [SRC-1AE03B9EC3-L005880](../../agents/web_agent.py#L5880) | 5880 | `"            return {"` | — |
| [SRC-1AE03B9EC3-L005881](../../agents/web_agent.py#L5881) | 5881 | `"                \"answer\": reason,"` | — |
| [SRC-1AE03B9EC3-L005882](../../agents/web_agent.py#L5882) | 5882 | `"                \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L005883](../../agents/web_agent.py#L5883) | 5883 | `"                \"search_query\": (plan.get(\"queries\") or [\"\"])[0],"` | — |
| [SRC-1AE03B9EC3-L005884](../../agents/web_agent.py#L5884) | 5884 | `"                \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L005885](../../agents/web_agent.py#L5885) | 5885 | `"                \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L005886](../../agents/web_agent.py#L5886) | 5886 | `"                    \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L005887](../../agents/web_agent.py#L5887) | 5887 | `"                    \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L005888](../../agents/web_agent.py#L5888) | 5888 | `"                    \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L005889](../../agents/web_agent.py#L5889) | 5889 | `"                    \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L005890](../../agents/web_agent.py#L5890) | 5890 | `"                    \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L005891](../../agents/web_agent.py#L5891) | 5891 | `"                    \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L005892](../../agents/web_agent.py#L5892) | 5892 | `"                    \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L005893](../../agents/web_agent.py#L5893) | 5893 | `"                    \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L005894](../../agents/web_agent.py#L5894) | 5894 | `"                    \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L005895](../../agents/web_agent.py#L5895) | 5895 | `"                    \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L005896](../../agents/web_agent.py#L5896) | 5896 | `"                },"` | — |
| [SRC-1AE03B9EC3-L005897](../../agents/web_agent.py#L5897) | 5897 | `"                \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L005898](../../agents/web_agent.py#L5898) | 5898 | `"                \"sources\": public_sources,"` | — |
| [SRC-1AE03B9EC3-L005899](../../agents/web_agent.py#L5899) | 5899 | `"                \"used_language_model\": False,"` | — |
| [SRC-1AE03B9EC3-L005900](../../agents/web_agent.py#L5900) | 5900 | `"                \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L005901](../../agents/web_agent.py#L5901) | 5901 | `"                \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L005902](../../agents/web_agent.py#L5902) | 5902 | `"                \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L005903](../../agents/web_agent.py#L5903) | 5903 | `"                \"warnings\": list(dict.fromkeys(search_warnings + [reason])),"` | — |
| [SRC-1AE03B9EC3-L005904](../../agents/web_agent.py#L5904) | 5904 | `"                \"kind\": \"insufficient_evidence\","` | — |
| [SRC-1AE03B9EC3-L005905](../../agents/web_agent.py#L5905) | 5905 | `"                \"final_answer_status\": \"insufficient_evidence_no_generation\","` | — |
| [SRC-1AE03B9EC3-L005906](../../agents/web_agent.py#L5906) | 5906 | `"                \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L005907](../../agents/web_agent.py#L5907) | 5907 | `"                \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L005908](../../agents/web_agent.py#L5908) | 5908 | `"                \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L005909](../../agents/web_agent.py#L5909) | 5909 | `"                \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L005910](../../agents/web_agent.py#L5910) | 5910 | `"                \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L005911](../../agents/web_agent.py#L5911) | 5911 | `"                \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L005912](../../agents/web_agent.py#L5912) | 5912 | `"                \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L005913](../../agents/web_agent.py#L5913) | 5913 | `"            }"` | — |
| [SRC-1AE03B9EC3-L005914](../../agents/web_agent.py#L5914) | 5914 | `""` | — |
| [SRC-1AE03B9EC3-L005915](../../agents/web_agent.py#L5915) | 5915 | `"        answer = \"\""` | — |
| [SRC-1AE03B9EC3-L005916](../../agents/web_agent.py#L5916) | 5916 | `"        used_llm = False"` | — |
| [SRC-1AE03B9EC3-L005917](../../agents/web_agent.py#L5917) | 5917 | `"        llm_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L005918](../../agents/web_agent.py#L5918) | 5918 | `"        generation_budget_exhausted = False"` | — |
| [SRC-1AE03B9EC3-L005919](../../agents/web_agent.py#L5919) | 5919 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L005920](../../agents/web_agent.py#L5920) | 5920 | `"            answer = self._generate("` | — |
| [SRC-1AE03B9EC3-L005921](../../agents/web_agent.py#L5921) | 5921 | `"                working_question,"` | — |
| [SRC-1AE03B9EC3-L005922](../../agents/web_agent.py#L5922) | 5922 | `"                clean_history,"` | — |
| [SRC-1AE03B9EC3-L005923](../../agents/web_agent.py#L5923) | 5923 | `"                sources,"` | — |
| [SRC-1AE03B9EC3-L005924](../../agents/web_agent.py#L5924) | 5924 | `"                search_warning,"` | — |
| [SRC-1AE03B9EC3-L005925](../../agents/web_agent.py#L5925) | 5925 | `"                research_plan=plan,"` | — |
| [SRC-1AE03B9EC3-L005926](../../agents/web_agent.py#L5926) | 5926 | `"                search_report=report,"` | — |
| [SRC-1AE03B9EC3-L005927](../../agents/web_agent.py#L5927) | 5927 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005928](../../agents/web_agent.py#L5928) | 5928 | `"            used_llm = True"` | — |
| [SRC-1AE03B9EC3-L005929](../../agents/web_agent.py#L5929) | 5929 | `"            if self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L005930](../../agents/web_agent.py#L5930) | 5930 | `"                existing_urls = {item.get(\"url\") for item in sources}"` | — |
| [SRC-1AE03B9EC3-L005931](../../agents/web_agent.py#L5931) | 5931 | `"                relevance_queries = []"` | — |
| [SRC-1AE03B9EC3-L005932](../../agents/web_agent.py#L5932) | 5932 | `"                planned_queries = plan.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L005933](../../agents/web_agent.py#L5933) | 5933 | `"                if not isinstance(planned_queries, list):"` | — |
| [SRC-1AE03B9EC3-L005934](../../agents/web_agent.py#L5934) | 5934 | `"                    planned_queries = []"` | — |
| [SRC-1AE03B9EC3-L005935](../../agents/web_agent.py#L5935) | 5935 | `"                for candidate_query in [working_question, *planned_queries]:"` | — |
| [SRC-1AE03B9EC3-L005936](../../agents/web_agent.py#L5936) | 5936 | `"                    if not isinstance(candidate_query, str):"` | — |
| [SRC-1AE03B9EC3-L005937](../../agents/web_agent.py#L5937) | 5937 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L005938](../../agents/web_agent.py#L5938) | 5938 | `"                    compacted_query = compact_search_query(candidate_query)"` | — |
| [SRC-1AE03B9EC3-L005939](../../agents/web_agent.py#L5939) | 5939 | `"                    if compacted_query and compacted_query not in relevance_queries:"` | — |
| [SRC-1AE03B9EC3-L005940](../../agents/web_agent.py#L5940) | 5940 | `"                        relevance_queries.append(compacted_query)"` | — |
| [SRC-1AE03B9EC3-L005941](../../agents/web_agent.py#L5941) | 5941 | `"                for item in self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L005942](../../agents/web_agent.py#L5942) | 5942 | `"                    source_text = \" \".join(("` | — |
| [SRC-1AE03B9EC3-L005943](../../agents/web_agent.py#L5943) | 5943 | `"                        item.get(\"title\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005944](../../agents/web_agent.py#L5944) | 5944 | `"                        item.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005945](../../agents/web_agent.py#L5945) | 5945 | `"                    ))"` | — |
| [SRC-1AE03B9EC3-L005946](../../agents/web_agent.py#L5946) | 5946 | `"                    if ("` | — |
| [SRC-1AE03B9EC3-L005947](../../agents/web_agent.py#L5947) | 5947 | `"                        relevance_queries"` | — |
| [SRC-1AE03B9EC3-L005948](../../agents/web_agent.py#L5948) | 5948 | `"                        and item[\"url\"] not in existing_urls"` | — |
| [SRC-1AE03B9EC3-L005949](../../agents/web_agent.py#L5949) | 5949 | `"                        and not _blocked_source_url(item[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L005950](../../agents/web_agent.py#L5950) | 5950 | `"                        and any("` | — |
| [SRC-1AE03B9EC3-L005951](../../agents/web_agent.py#L5951) | 5951 | `"                            _relevance_ratio(candidate_query, source_text) >= 0.20"` | — |
| [SRC-1AE03B9EC3-L005952](../../agents/web_agent.py#L5952) | 5952 | `"                            for candidate_query in relevance_queries"` | — |
| [SRC-1AE03B9EC3-L005953](../../agents/web_agent.py#L5953) | 5953 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005954](../../agents/web_agent.py#L5954) | 5954 | `"                    ):"` | — |
| [SRC-1AE03B9EC3-L005955](../../agents/web_agent.py#L5955) | 5955 | `"                        sources.append(item)"` | — |
| [SRC-1AE03B9EC3-L005956](../../agents/web_agent.py#L5956) | 5956 | `"                        existing_urls.add(item[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L005957](../../agents/web_agent.py#L5957) | 5957 | `"                report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005958](../../agents/web_agent.py#L5958) | 5958 | `"                provider_counts = dict(report.get(\"provider_counts\", {}))"` | — |
| [SRC-1AE03B9EC3-L005959](../../agents/web_agent.py#L5959) | 5959 | `"                provider_counts[\"openrouter_web_search\"] = len(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L005960](../../agents/web_agent.py#L5960) | 5960 | `"                report[\"provider_counts\"] = provider_counts"` | — |
| [SRC-1AE03B9EC3-L005961](../../agents/web_agent.py#L5961) | 5961 | `"                providers_used = list(report.get(\"providers_used\", []))"` | — |
| [SRC-1AE03B9EC3-L005962](../../agents/web_agent.py#L5962) | 5962 | `"                if \"openrouter_web_search\" not in providers_used:"` | — |
| [SRC-1AE03B9EC3-L005963](../../agents/web_agent.py#L5963) | 5963 | `"                    providers_used.append(\"openrouter_web_search\")"` | — |
| [SRC-1AE03B9EC3-L005964](../../agents/web_agent.py#L5964) | 5964 | `"                report[\"providers_used\"] = providers_used"` | — |
| [SRC-1AE03B9EC3-L005965](../../agents/web_agent.py#L5965) | 5965 | `"                report[\"evidence_signals\"] = evidence_signal_report("` | — |
| [SRC-1AE03B9EC3-L005966](../../agents/web_agent.py#L5966) | 5966 | `"                    sources, plan.get(\"freshness\", \"any\")"` | — |
| [SRC-1AE03B9EC3-L005967](../../agents/web_agent.py#L5967) | 5967 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005968](../../agents/web_agent.py#L5968) | 5968 | `"        except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L005969](../../agents/web_agent.py#L5969) | 5969 | `"            llm_warning = str(exc)"` | — |
| [SRC-1AE03B9EC3-L005970](../../agents/web_agent.py#L5970) | 5970 | `"            generation_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L005971](../../agents/web_agent.py#L5971) | 5971 | `"            if generation_budget_exhausted:"` | — |
| [SRC-1AE03B9EC3-L005972](../../agents/web_agent.py#L5972) | 5972 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005973](../../agents/web_agent.py#L5973) | 5973 | `"                    \"استُنفدت ميزانية محاولات النماذج قبل اكتمال الإجابة التحليلية. \""` | — |
| [SRC-1AE03B9EC3-L005974](../../agents/web_agent.py#L5974) | 5974 | `"                    \"أعرض مقتطفات المصادر المتاحة فقط، ولا أعتبر المهمة مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L005975](../../agents/web_agent.py#L5975) | 5975 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005976](../../agents/web_agent.py#L5976) | 5976 | `"            elif not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L005977](../../agents/web_agent.py#L5977) | 5977 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005978](../../agents/web_agent.py#L5978) | 5978 | `"                    \"تم البحث، لكن الفهم التوليدي غير مفعّل بعد. اضبط OPENROUTER_API_KEY \""` | — |
| [SRC-1AE03B9EC3-L005979](../../agents/web_agent.py#L5979) | 5979 | `"                    \"في Termux لتفعيل تخطيط البحث والإجابة باللغة الطبيعية.\""` | — |
| [SRC-1AE03B9EC3-L005980](../../agents/web_agent.py#L5980) | 5980 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005981](../../agents/web_agent.py#L5981) | 5981 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L005982](../../agents/web_agent.py#L5982) | 5982 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005983](../../agents/web_agent.py#L5983) | 5983 | `"                    \"اكتمل البحث، لكن تعذر توليد إجابة تحليلية. أعرض لك مقتطفات المصادر \""` | — |
| [SRC-1AE03B9EC3-L005984](../../agents/web_agent.py#L5984) | 5984 | `"                    \"المتاحة بدلًا من اختلاق إجابة.\""` | — |
| [SRC-1AE03B9EC3-L005985](../../agents/web_agent.py#L5985) | 5985 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005986](../../agents/web_agent.py#L5986) | 5986 | `"            answer = _fallback_answer(sources, reason)"` | — |
| [SRC-1AE03B9EC3-L005987](../../agents/web_agent.py#L5987) | 5987 | `""` | — |
| [SRC-1AE03B9EC3-L005988](../../agents/web_agent.py#L5988) | 5988 | `"        coverage_targets = self._question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L005989](../../agents/web_agent.py#L5989) | 5989 | `"        coverage_repair_status = \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L005990](../../agents/web_agent.py#L5990) | 5990 | `"        coverage_repair_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L005991](../../agents/web_agent.py#L5991) | 5991 | `"        review_status = \"not_run\""` | — |
| [SRC-1AE03B9EC3-L005992](../../agents/web_agent.py#L5992) | 5992 | `"        review_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L005993](../../agents/web_agent.py#L5993) | 5993 | `"        review_budget_exhausted = False"` | — |
| [SRC-1AE03B9EC3-L005994](../../agents/web_agent.py#L5994) | 5994 | `"        if used_llm and sources:"` | — |
| [SRC-1AE03B9EC3-L005995](../../agents/web_agent.py#L5995) | 5995 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L005996](../../agents/web_agent.py#L5996) | 5996 | `"                answer = self._review_answer(working_question, answer, sources[:MAX_LLM_CITED_SOURCES])"` | — |
| [SRC-1AE03B9EC3-L005997](../../agents/web_agent.py#L5997) | 5997 | `"                review_status = \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005998](../../agents/web_agent.py#L5998) | 5998 | `"            except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L005999](../../agents/web_agent.py#L5999) | 5999 | `"                review_status = \"model_claim_audit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L006000](../../agents/web_agent.py#L6000) | 6000 | `"                review_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L006001](../../agents/web_agent.py#L6001) | 6001 | `"                review_warning = ("` | — |
| [SRC-1AE03B9EC3-L006002](../../agents/web_agent.py#L6002) | 6002 | `"                    \"استُنفدت ميزانية النماذج قبل اكتمال تدقيق الإجابة؛ لذلك لن أعرض المسودة \""` | — |
| [SRC-1AE03B9EC3-L006003](../../agents/web_agent.py#L6003) | 6003 | `"                    \"بوصفها إجابة مكتملة. أرفقت مقتطفات المصادر المتاحة بدل الاعتماد عليها.\""` | — |
| [SRC-1AE03B9EC3-L006004](../../agents/web_agent.py#L6004) | 6004 | `"                    if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L006005](../../agents/web_agent.py#L6005) | 6005 | `"                    else"` | — |
| [SRC-1AE03B9EC3-L006006](../../agents/web_agent.py#L6006) | 6006 | `"                    \"تعذر تدقيق الادعاءات مقابل نصوص المصادر؛ لذلك لن أتعامل مع المسودة \""` | — |
| [SRC-1AE03B9EC3-L006007](../../agents/web_agent.py#L6007) | 6007 | `"                    \"كإجابة مؤكدة. أرفقت مقتطفات المصادر المتاحة بدل الاعتماد على المسودة.\""` | — |
| [SRC-1AE03B9EC3-L006008](../../agents/web_agent.py#L6008) | 6008 | `"                )"` | — |
| [SRC-1AE03B9EC3-L006009](../../agents/web_agent.py#L6009) | 6009 | `"                answer = _fallback_answer(sources, review_warning)"` | — |
| [SRC-1AE03B9EC3-L006010](../../agents/web_agent.py#L6010) | 6010 | `"        criterion_gap_research: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L006011](../../agents/web_agent.py#L6011) | 6011 | `"            \"attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L006012](../../agents/web_agent.py#L6012) | 6012 | `"            \"status\": \"not_needed\","` | — |
| [SRC-1AE03B9EC3-L006013](../../agents/web_agent.py#L6013) | 6013 | `"            \"targets\": [],"` | — |
| [SRC-1AE03B9EC3-L006014](../../agents/web_agent.py#L6014) | 6014 | `"            \"new_sources_added\": 0,"` | — |
| [SRC-1AE03B9EC3-L006015](../../agents/web_agent.py#L6015) | 6015 | `"            \"evidence_sources_enriched\": 0,"` | — |
| [SRC-1AE03B9EC3-L006016](../../agents/web_agent.py#L6016) | 6016 | `"        }"` | — |
| [SRC-1AE03B9EC3-L006017](../../agents/web_agent.py#L6017) | 6017 | `"        # Close the loop from an answer-stage gap back to the source layer. A criterion"` | — |
| [SRC-1AE03B9EC3-L006018](../../agents/web_agent.py#L6018) | 6018 | `"        # that appears in the draft but has no source signal triggers one bounded query"` | — |
| [SRC-1AE03B9EC3-L006019](../../agents/web_agent.py#L6019) | 6019 | `"        # when the reserved request-budget slot remains available."` | — |
| [SRC-1AE03B9EC3-L006020](../../agents/web_agent.py#L6020) | 6020 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L006021](../../agents/web_agent.py#L6021) | 6021 | `"            coverage_targets"` | — |
| [SRC-1AE03B9EC3-L006022](../../agents/web_agent.py#L6022) | 6022 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006023](../../agents/web_agent.py#L6023) | 6023 | `"            and sources"` | — |
| [SRC-1AE03B9EC3-L006024](../../agents/web_agent.py#L6024) | 6024 | `"            and self.api_key"` | — |
| [SRC-1AE03B9EC3-L006025](../../agents/web_agent.py#L6025) | 6025 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L006026](../../agents/web_agent.py#L6026) | 6026 | `"            presearch_integrity = audit_answer_integrity(working_question, answer, sources, coverage_targets, plan.get(\"requirement_queries\"))"` | — |
| [SRC-1AE03B9EC3-L006027](../../agents/web_agent.py#L6027) | 6027 | `"            source_gap_targets = ["` | — |
| [SRC-1AE03B9EC3-L006028](../../agents/web_agent.py#L6028) | 6028 | `"                item[\"target\"]"` | — |
| [SRC-1AE03B9EC3-L006029](../../agents/web_agent.py#L6029) | 6029 | `"                for item in presearch_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L006030](../../agents/web_agent.py#L6030) | 6030 | `"                if item.get(\"source_evidence_status\") == \"no_source_lexical_signal\""` | — |
| [SRC-1AE03B9EC3-L006031](../../agents/web_agent.py#L6031) | 6031 | `"            ][:3]"` | — |
| [SRC-1AE03B9EC3-L006032](../../agents/web_agent.py#L6032) | 6032 | `"            if source_gap_targets:"` | — |
| [SRC-1AE03B9EC3-L006033](../../agents/web_agent.py#L6033) | 6033 | `"                criterion_gap_research[\"targets\"] = source_gap_targets"` | — |
| [SRC-1AE03B9EC3-L006034](../../agents/web_agent.py#L6034) | 6034 | `"                budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L006035](../../agents/web_agent.py#L6035) | 6035 | `"                if not plan.get(\"coverage_gap_repair_slot_reserved\"):"` | — |
| [SRC-1AE03B9EC3-L006036](../../agents/web_agent.py#L6036) | 6036 | `"                    criterion_gap_research[\"status\"] = \"skipped_no_reserved_search_slot\""` | — |
| [SRC-1AE03B9EC3-L006037](../../agents/web_agent.py#L6037) | 6037 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L006038](../../agents/web_agent.py#L6038) | 6038 | `"                        \"رُصدت محاور بلا إشارة لفظية في المصادر، لكن لم تُحجز ميزانية \""` | — |
| [SRC-1AE03B9EC3-L006039](../../agents/web_agent.py#L6039) | 6039 | `"                        \"استعلام إضافي لهذه المهمة؛ لذلك ستظل المحاور غير المحسومة ظاهرة.\""` | — |
| [SRC-1AE03B9EC3-L006040](../../agents/web_agent.py#L6040) | 6040 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L006041](../../agents/web_agent.py#L6041) | 6041 | `"                elif budget is None:"` | — |
| [SRC-1AE03B9EC3-L006042](../../agents/web_agent.py#L6042) | 6042 | `"                    criterion_gap_research[\"status\"] = \"skipped_no_request_budget\""` | — |
| [SRC-1AE03B9EC3-L006043](../../agents/web_agent.py#L6043) | 6043 | `"                elif budget.remaining_units(\"search_queries\") < 1:"` | — |
| [SRC-1AE03B9EC3-L006044](../../agents/web_agent.py#L6044) | 6044 | `"                    criterion_gap_research[\"status\"] = \"skipped_search_budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L006045](../../agents/web_agent.py#L6045) | 6045 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L006046](../../agents/web_agent.py#L6046) | 6046 | `"                        \"رُصدت محاور بلا إشارة لفظية في المصادر، لكن ميزانية البحث لم تترك \""` | — |
| [SRC-1AE03B9EC3-L006047](../../agents/web_agent.py#L6047) | 6047 | `"                        \"استعلامًا إضافيًا للتحقق منها؛ لذلك لا تُعدّ الإجابة مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L006048](../../agents/web_agent.py#L6048) | 6048 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L006049](../../agents/web_agent.py#L6049) | 6049 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L006050](../../agents/web_agent.py#L6050) | 6050 | `"                    fallback_queries = fallback_plan(working_question, clean_history).get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L006051](../../agents/web_agent.py#L6051) | 6051 | `"                    topic_query = compact_search_query("` | — |
| [SRC-1AE03B9EC3-L006052](../../agents/web_agent.py#L6052) | 6052 | `"                        fallback_queries[0] if fallback_queries else working_question"` | — |
| [SRC-1AE03B9EC3-L006053](../../agents/web_agent.py#L6053) | 6053 | `"                    ) or compact_search_query(working_question)"` | — |
| [SRC-1AE03B9EC3-L006054](../../agents/web_agent.py#L6054) | 6054 | `"                    gap_query = compact_search_query("` | — |
| [SRC-1AE03B9EC3-L006055](../../agents/web_agent.py#L6055) | 6055 | `"                        f\"{topic_query} {' '.join(source_gap_targets)} official specific evidence data\""` | — |
| [SRC-1AE03B9EC3-L006056](../../agents/web_agent.py#L6056) | 6056 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L006057](../../agents/web_agent.py#L6057) | 6057 | `"                    known_query_keys = {"` | — |
| [SRC-1AE03B9EC3-L006058](../../agents/web_agent.py#L6058) | 6058 | `"                        _normalize_search_query(item).casefold()"` | — |
| [SRC-1AE03B9EC3-L006059](../../agents/web_agent.py#L6059) | 6059 | `"                        for item in plan.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L006060](../../agents/web_agent.py#L6060) | 6060 | `"                        if isinstance(item, str) and item.strip()"` | — |
| [SRC-1AE03B9EC3-L006061](../../agents/web_agent.py#L6061) | 6061 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L006062](../../agents/web_agent.py#L6062) | 6062 | `"                    if not gap_query or not _relevance_query_tokens(gap_query):"` | — |
| [SRC-1AE03B9EC3-L006063](../../agents/web_agent.py#L6063) | 6063 | `"                        criterion_gap_research[\"status\"] = \"skipped_no_valid_query\""` | — |
| [SRC-1AE03B9EC3-L006064](../../agents/web_agent.py#L6064) | 6064 | `"                    elif _normalize_search_query(gap_query).casefold() in known_query_keys:"` | — |
| [SRC-1AE03B9EC3-L006065](../../agents/web_agent.py#L6065) | 6065 | `"                        criterion_gap_research[\"status\"] = \"skipped_query_not_distinct\""` | — |
| [SRC-1AE03B9EC3-L006066](../../agents/web_agent.py#L6066) | 6066 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L006067](../../agents/web_agent.py#L6067) | 6067 | `"                        criterion_gap_research.update({"` | — |
| [SRC-1AE03B9EC3-L006068](../../agents/web_agent.py#L6068) | 6068 | `"                            \"attempted\": True,"` | — |
| [SRC-1AE03B9EC3-L006069](../../agents/web_agent.py#L6069) | 6069 | `"                            \"status\": \"searching_for_missing_criterion_evidence\","` | — |
| [SRC-1AE03B9EC3-L006070](../../agents/web_agent.py#L6070) | 6070 | `"                            \"query\": gap_query,"` | — |
| [SRC-1AE03B9EC3-L006071](../../agents/web_agent.py#L6071) | 6071 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L006072](../../agents/web_agent.py#L6072) | 6072 | `"                        gap_plan = dict(plan)"` | — |
| [SRC-1AE03B9EC3-L006073](../../agents/web_agent.py#L6073) | 6073 | `"                        gap_plan.update({"` | — |
| [SRC-1AE03B9EC3-L006074](../../agents/web_agent.py#L6074) | 6074 | `"                            \"queries\": [gap_query],"` | — |
| [SRC-1AE03B9EC3-L006075](../../agents/web_agent.py#L6075) | 6075 | `"                            \"query_limit\": 1,"` | — |
| [SRC-1AE03B9EC3-L006076](../../agents/web_agent.py#L6076) | 6076 | `"                            \"depth\": \"standard\","` | — |
| [SRC-1AE03B9EC3-L006077](../../agents/web_agent.py#L6077) | 6077 | `"                            \"social_focus\": False,"` | — |
| [SRC-1AE03B9EC3-L006078](../../agents/web_agent.py#L6078) | 6078 | `"                            \"platforms\": [],"` | — |
| [SRC-1AE03B9EC3-L006079](../../agents/web_agent.py#L6079) | 6079 | `"                            \"direct_urls\": [],"` | — |
| [SRC-1AE03B9EC3-L006080](../../agents/web_agent.py#L6080) | 6080 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L006081](../../agents/web_agent.py#L6081) | 6081 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L006082](../../agents/web_agent.py#L6082) | 6082 | `"                            gap_sources, gap_warnings, gap_report = self._collect_research(gap_plan)"` | — |
| [SRC-1AE03B9EC3-L006083](../../agents/web_agent.py#L6083) | 6083 | `"                        except (RuntimeError, AgentDependencyError, RequestBudgetExceeded, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L006084](../../agents/web_agent.py#L6084) | 6084 | `"                            gap_sources, gap_warnings = [], []"` | — |
| [SRC-1AE03B9EC3-L006085](../../agents/web_agent.py#L6085) | 6085 | `"                            gap_report = {"` | — |
| [SRC-1AE03B9EC3-L006086](../../agents/web_agent.py#L6086) | 6086 | `"                                \"queries_planned\": 1,"` | — |
| [SRC-1AE03B9EC3-L006087](../../agents/web_agent.py#L6087) | 6087 | `"                                \"queries_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L006088](../../agents/web_agent.py#L6088) | 6088 | `"                                \"queries_attempted_known\": False,"` | — |
| [SRC-1AE03B9EC3-L006089](../../agents/web_agent.py#L6089) | 6089 | `"                                \"search_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L006090](../../agents/web_agent.py#L6090) | 6090 | `"                                \"search_outcome\": \"unknown_after_research_error\","` | — |
| [SRC-1AE03B9EC3-L006091](../../agents/web_agent.py#L6091) | 6091 | `"                                \"query_results\": [],"` | — |
| [SRC-1AE03B9EC3-L006092](../../agents/web_agent.py#L6092) | 6092 | `"                            }"` | — |
| [SRC-1AE03B9EC3-L006093](../../agents/web_agent.py#L6093) | 6093 | `"                            criterion_gap_research[\"status\"] = \"search_failed\""` | — |
| [SRC-1AE03B9EC3-L006094](../../agents/web_agent.py#L6094) | 6094 | `"                            criterion_gap_research[\"error_class\"] = type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L006095](../../agents/web_agent.py#L6095) | 6095 | `"                        search_warnings.extend("` | — |
| [SRC-1AE03B9EC3-L006096](../../agents/web_agent.py#L6096) | 6096 | `"                            item for item in gap_warnings if isinstance(item, str)"` | — |
| [SRC-1AE03B9EC3-L006097](../../agents/web_agent.py#L6097) | 6097 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L006098](../../agents/web_agent.py#L6098) | 6098 | `"                        source_indexes: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L006099](../../agents/web_agent.py#L6099) | 6099 | `"                        for source_index, source in enumerate(sources):"` | — |
| [SRC-1AE03B9EC3-L006100](../../agents/web_agent.py#L6100) | 6100 | `"                            source_key = self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L006101](../../agents/web_agent.py#L6101) | 6101 | `"                            if source_key:"` | — |
| [SRC-1AE03B9EC3-L006102](../../agents/web_agent.py#L6102) | 6102 | `"                                source_indexes.setdefault(source_key, source_index)"` | — |
| [SRC-1AE03B9EC3-L006103](../../agents/web_agent.py#L6103) | 6103 | `"                        # A criterion-gap search is a second retrieval path, not a"` | — |
| [SRC-1AE03B9EC3-L006104](../../agents/web_agent.py#L6104) | 6104 | `"                        # trusted bypass. Apply the same task-specific source policy before"` | — |
| [SRC-1AE03B9EC3-L006105](../../agents/web_agent.py#L6105) | 6105 | `"                        # merging candidates into the evidence set or regenerating an answer."` | — |
| [SRC-1AE03B9EC3-L006106](../../agents/web_agent.py#L6106) | 6106 | `"                        pre_gap_source_keys = set(source_indexes)"` | — |
| [SRC-1AE03B9EC3-L006107](../../agents/web_agent.py#L6107) | 6107 | `"                        gap_sources_before_guardrails = len(gap_sources)"` | — |
| [SRC-1AE03B9EC3-L006108](../../agents/web_agent.py#L6108) | 6108 | `"                        gap_sources, gap_guardrail_report = apply_source_guardrails("` | — |
| [SRC-1AE03B9EC3-L006109](../../agents/web_agent.py#L6109) | 6109 | `"                            working_question, clean_mode, plan, gap_sources"` | — |
| [SRC-1AE03B9EC3-L006110](../../agents/web_agent.py#L6110) | 6110 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L006111](../../agents/web_agent.py#L6111) | 6111 | `"                        report.setdefault(\"source_guardrails\", {})["` | — |
| [SRC-1AE03B9EC3-L006112](../../agents/web_agent.py#L6112) | 6112 | `"                            \"criterion_gap_repair\""` | — |
| [SRC-1AE03B9EC3-L006113](../../agents/web_agent.py#L6113) | 6113 | `"                        ] = {"` | — |
| [SRC-1AE03B9EC3-L006114](../../agents/web_agent.py#L6114) | 6114 | `"                            **gap_guardrail_report,"` | — |
| [SRC-1AE03B9EC3-L006115](../../agents/web_agent.py#L6115) | 6115 | `"                            \"candidates_before_filter\": gap_sources_before_guardrails,"` | — |
| [SRC-1AE03B9EC3-L006116](../../agents/web_agent.py#L6116) | 6116 | `"                        }"` | — |
| [SRC-1AE03B9EC3-L006117](../../agents/web_agent.py#L6117) | 6117 | `"                        if gap_guardrail_report[\"rejected_sources\"]:"` | — |
| [SRC-1AE03B9EC3-L006118](../../agents/web_agent.py#L6118) | 6118 | `"                            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L006119](../../agents/web_agent.py#L6119) | 6119 | `"                                \"رُفضت بعض نتائج البحث الإضافي لأنها لم تستوفِ شروط قبول \""` | — |
| [SRC-1AE03B9EC3-L006120](../../agents/web_agent.py#L6120) | 6120 | `"                                \"الأدلة الخاصة بالسؤال.\""` | — |
| [SRC-1AE03B9EC3-L006121](../../agents/web_agent.py#L6121) | 6121 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L006122](../../agents/web_agent.py#L6122) | 6122 | `"                        evidence_updated = False"` | — |
| [SRC-1AE03B9EC3-L006123](../../agents/web_agent.py#L6123) | 6123 | `"                        for candidate in gap_sources:"` | — |
| [SRC-1AE03B9EC3-L006124](../../agents/web_agent.py#L6124) | 6124 | `"                            if not isinstance(candidate, dict):"` | — |
| [SRC-1AE03B9EC3-L006125](../../agents/web_agent.py#L6125) | 6125 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L006126](../../agents/web_agent.py#L6126) | 6126 | `"                            if not self._source_matches_query(gap_query, candidate):"` | — |
| [SRC-1AE03B9EC3-L006127](../../agents/web_agent.py#L6127) | 6127 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L006128](../../agents/web_agent.py#L6128) | 6128 | `"                            source_key = self._normalized_source_url_key(candidate.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L006129](../../agents/web_agent.py#L6129) | 6129 | `"                            if not source_key:"` | — |
| [SRC-1AE03B9EC3-L006130](../../agents/web_agent.py#L6130) | 6130 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L006131](../../agents/web_agent.py#L6131) | 6131 | `"                            existing_index = source_indexes.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L006132](../../agents/web_agent.py#L6132) | 6132 | `"                            if existing_index is None:"` | — |
| [SRC-1AE03B9EC3-L006133](../../agents/web_agent.py#L6133) | 6133 | `"                                source_indexes[source_key] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L006134](../../agents/web_agent.py#L6134) | 6134 | `"                                sources.append(candidate)"` | — |
| [SRC-1AE03B9EC3-L006135](../../agents/web_agent.py#L6135) | 6135 | `"                                criterion_gap_research[\"new_sources_added\"] += 1"` | — |
| [SRC-1AE03B9EC3-L006136](../../agents/web_agent.py#L6136) | 6136 | `"                                evidence_updated = True"` | — |
| [SRC-1AE03B9EC3-L006137](../../agents/web_agent.py#L6137) | 6137 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L006138](../../agents/web_agent.py#L6138) | 6138 | `"                            existing_source = sources[existing_index]"` | — |
| [SRC-1AE03B9EC3-L006139](../../agents/web_agent.py#L6139) | 6139 | `"                            merged = dict(existing_source)"` | — |
| [SRC-1AE03B9EC3-L006140](../../agents/web_agent.py#L6140) | 6140 | `"                            source_enriched = False"` | — |
| [SRC-1AE03B9EC3-L006141](../../agents/web_agent.py#L6141) | 6141 | `"                            for text_key in (\"title\", \"snippet\", \"page_text\"):"` | — |
| [SRC-1AE03B9EC3-L006142](../../agents/web_agent.py#L6142) | 6142 | `"                                old_text = str(merged.get(text_key) or \"\")"` | — |
| [SRC-1AE03B9EC3-L006143](../../agents/web_agent.py#L6143) | 6143 | `"                                new_text = str(candidate.get(text_key) or \"\")"` | — |
| [SRC-1AE03B9EC3-L006144](../../agents/web_agent.py#L6144) | 6144 | `"                                if len(new_text) > len(old_text):"` | — |
| [SRC-1AE03B9EC3-L006145](../../agents/web_agent.py#L6145) | 6145 | `"                                    merged[text_key] = candidate[text_key]"` | — |
| [SRC-1AE03B9EC3-L006146](../../agents/web_agent.py#L6146) | 6146 | `"                                    source_enriched = True"` | — |
| [SRC-1AE03B9EC3-L006147](../../agents/web_agent.py#L6147) | 6147 | `"                            if candidate.get(\"page_fetched\") and not existing_source.get(\"page_fetched\"):"` | — |
| [SRC-1AE03B9EC3-L006148](../../agents/web_agent.py#L6148) | 6148 | `"                                merged[\"page_fetched\"] = True"` | — |
| [SRC-1AE03B9EC3-L006149](../../agents/web_agent.py#L6149) | 6149 | `"                                source_enriched = True"` | — |
| [SRC-1AE03B9EC3-L006150](../../agents/web_agent.py#L6150) | 6150 | `"                            if source_enriched:"` | — |
| [SRC-1AE03B9EC3-L006151](../../agents/web_agent.py#L6151) | 6151 | `"                                evidence_updated = True"` | — |
| [SRC-1AE03B9EC3-L006152](../../agents/web_agent.py#L6152) | 6152 | `"                                criterion_gap_research[\"evidence_sources_enriched\"] += 1"` | — |
| [SRC-1AE03B9EC3-L006153](../../agents/web_agent.py#L6153) | 6153 | `"                            merged[\"providers\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L006154](../../agents/web_agent.py#L6154) | 6154 | `"                                list(existing_source.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L006155](../../agents/web_agent.py#L6155) | 6155 | `"                                + list(candidate.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L006156](../../agents/web_agent.py#L6156) | 6156 | `"                            ))"` | — |
| [SRC-1AE03B9EC3-L006157](../../agents/web_agent.py#L6157) | 6157 | `"                            merged[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L006158](../../agents/web_agent.py#L6158) | 6158 | `"                                list(existing_source.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L006159](../../agents/web_agent.py#L6159) | 6159 | `"                                + list(candidate.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L006160](../../agents/web_agent.py#L6160) | 6160 | `"                                + [gap_query]"` | — |
| [SRC-1AE03B9EC3-L006161](../../agents/web_agent.py#L6161) | 6161 | `"                            ))"` | — |
| [SRC-1AE03B9EC3-L006162](../../agents/web_agent.py#L6162) | 6162 | `"                            sources[existing_index] = merged"` | — |
| [SRC-1AE03B9EC3-L006163](../../agents/web_agent.py#L6163) | 6163 | `"                        # Re-apply the guardrails to the merged set as a final safety"` | — |
| [SRC-1AE03B9EC3-L006164](../../agents/web_agent.py#L6164) | 6164 | `"                        # boundary. Count newly added sources only after this filter."` | — |
| [SRC-1AE03B9EC3-L006165](../../agents/web_agent.py#L6165) | 6165 | `"                        sources, merged_guardrail_report = apply_source_guardrails("` | — |
| [SRC-1AE03B9EC3-L006166](../../agents/web_agent.py#L6166) | 6166 | `"                            working_question, clean_mode, plan, sources"` | — |
| [SRC-1AE03B9EC3-L006167](../../agents/web_agent.py#L6167) | 6167 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L006168](../../agents/web_agent.py#L6168) | 6168 | `"                        report[\"source_guardrails\"][\"after_criterion_gap_repair\"] = ("` | — |
| [SRC-1AE03B9EC3-L006169](../../agents/web_agent.py#L6169) | 6169 | `"                            merged_guardrail_report"` | — |
| [SRC-1AE03B9EC3-L006170](../../agents/web_agent.py#L6170) | 6170 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L006171](../../agents/web_agent.py#L6171) | 6171 | `"                        accepted_source_keys = {"` | — |
| [SRC-1AE03B9EC3-L006172](../../agents/web_agent.py#L6172) | 6172 | `"                            self._normalized_source_url_key(item.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L006173](../../agents/web_agent.py#L6173) | 6173 | `"                            for item in sources"` | — |
| [SRC-1AE03B9EC3-L006174](../../agents/web_agent.py#L6174) | 6174 | `"                            if self._normalized_source_url_key(item.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L006175](../../agents/web_agent.py#L6175) | 6175 | `"                        }"` | — |
| [SRC-1AE03B9EC3-L006176](../../agents/web_agent.py#L6176) | 6176 | `"                        criterion_gap_research[\"new_sources_added\"] = len("` | — |
| [SRC-1AE03B9EC3-L006177](../../agents/web_agent.py#L6177) | 6177 | `"                            accepted_source_keys - pre_gap_source_keys"` | — |
| [SRC-1AE03B9EC3-L006178](../../agents/web_agent.py#L6178) | 6178 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L006179](../../agents/web_agent.py#L6179) | 6179 | `"                        criterion_gap_research[\"source_count_after\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L006180](../../agents/web_agent.py#L6180) | 6180 | `"                        plan[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L006181](../../agents/web_agent.py#L6181) | 6181 | `"                            list(plan.get(\"queries\", [])) + [gap_query]"` | — |
| [SRC-1AE03B9EC3-L006182](../../agents/web_agent.py#L6182) | 6182 | `"                        ))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L006183](../../agents/web_agent.py#L6183) | 6183 | `"                        report[\"criterion_gap_research\"] = dict(criterion_gap_research)"` | — |
| [SRC-1AE03B9EC3-L006184](../../agents/web_agent.py#L6184) | 6184 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L006185](../../agents/web_agent.py#L6185) | 6185 | `"                            report[\"queries_planned\"] = max("` | — |
| [SRC-1AE03B9EC3-L006186](../../agents/web_agent.py#L6186) | 6186 | `"                                0, int(report.get(\"queries_planned\", 0) or 0)"` | — |
| [SRC-1AE03B9EC3-L006187](../../agents/web_agent.py#L6187) | 6187 | `"                            ) + max(0, int(gap_report.get(\"queries_planned\", 1) or 0))"` | — |
| [SRC-1AE03B9EC3-L006188](../../agents/web_agent.py#L6188) | 6188 | `"                        except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-1AE03B9EC3-L006189](../../agents/web_agent.py#L6189) | 6189 | `"                            report[\"queries_planned\"] = None"` | — |
| [SRC-1AE03B9EC3-L006190](../../agents/web_agent.py#L6190) | 6190 | `"                        previous_attempts = report.get(\"queries_attempted\")"` | — |
| [SRC-1AE03B9EC3-L006191](../../agents/web_agent.py#L6191) | 6191 | `"                        extra_attempts = gap_report.get(\"queries_attempted\")"` | — |
| [SRC-1AE03B9EC3-L006192](../../agents/web_agent.py#L6192) | 6192 | `"                        if isinstance(previous_attempts, int) and isinstance(extra_attempts, int):"` | — |
| [SRC-1AE03B9EC3-L006193](../../agents/web_agent.py#L6193) | 6193 | `"                            report[\"queries_attempted\"] = max(0, previous_attempts) + max(0, extra_attempts)"` | — |
| [SRC-1AE03B9EC3-L006194](../../agents/web_agent.py#L6194) | 6194 | `"                            report[\"queries_attempted_known\"] = True"` | — |
| [SRC-1AE03B9EC3-L006195](../../agents/web_agent.py#L6195) | 6195 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L006196](../../agents/web_agent.py#L6196) | 6196 | `"                            report[\"queries_attempted\"] = None"` | — |
| [SRC-1AE03B9EC3-L006197](../../agents/web_agent.py#L6197) | 6197 | `"                            report[\"queries_attempted_known\"] = False"` | — |
| [SRC-1AE03B9EC3-L006198](../../agents/web_agent.py#L6198) | 6198 | `"                        old_query_results = report.get(\"query_results\")"` | — |
| [SRC-1AE03B9EC3-L006199](../../agents/web_agent.py#L6199) | 6199 | `"                        new_query_results = gap_report.get(\"query_results\")"` | — |
| [SRC-1AE03B9EC3-L006200](../../agents/web_agent.py#L6200) | 6200 | `"                        report[\"query_results\"] = ("` | — |
| [SRC-1AE03B9EC3-L006201](../../agents/web_agent.py#L6201) | 6201 | `"                            (old_query_results if isinstance(old_query_results, list) else [])"` | — |
| [SRC-1AE03B9EC3-L006202](../../agents/web_agent.py#L6202) | 6202 | `"                            + (new_query_results if isinstance(new_query_results, list) else [])"` | — |
| [SRC-1AE03B9EC3-L006203](../../agents/web_agent.py#L6203) | 6203 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L006204](../../agents/web_agent.py#L6204) | 6204 | `"                        if evidence_updated:"` | — |
| [SRC-1AE03B9EC3-L006205](../../agents/web_agent.py#L6205) | 6205 | `"                            sources.sort("` | — |
| [SRC-1AE03B9EC3-L006206](../../agents/web_agent.py#L6206) | 6206 | `"                                key=lambda item: float(item.get(\"rank_score\", 0) or 0),"` | — |
| [SRC-1AE03B9EC3-L006207](../../agents/web_agent.py#L6207) | 6207 | `"                                reverse=True,"` | — |
| [SRC-1AE03B9EC3-L006208](../../agents/web_agent.py#L6208) | 6208 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L006209](../../agents/web_agent.py#L6209) | 6209 | `"                            try:"` | — |
| [SRC-1AE03B9EC3-L006210](../../agents/web_agent.py#L6210) | 6210 | `"                                revised_draft = self._generate("` | — |
| [SRC-1AE03B9EC3-L006211](../../agents/web_agent.py#L6211) | 6211 | `"                                    working_question,"` | — |
| [SRC-1AE03B9EC3-L006212](../../agents/web_agent.py#L6212) | 6212 | `"                                    clean_history,"` | — |
| [SRC-1AE03B9EC3-L006213](../../agents/web_agent.py#L6213) | 6213 | `"                                    sources,"` | — |
| [SRC-1AE03B9EC3-L006214](../../agents/web_agent.py#L6214) | 6214 | `"                                    search_warning,"` | — |
| [SRC-1AE03B9EC3-L006215](../../agents/web_agent.py#L6215) | 6215 | `"                                    research_plan=plan,"` | — |
| [SRC-1AE03B9EC3-L006216](../../agents/web_agent.py#L6216) | 6216 | `"                                    search_report=report,"` | — |
| [SRC-1AE03B9EC3-L006217](../../agents/web_agent.py#L6217) | 6217 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L006218](../../agents/web_agent.py#L6218) | 6218 | `"                                revised_answer = self._review_answer("` | — |
| [SRC-1AE03B9EC3-L006219](../../agents/web_agent.py#L6219) | 6219 | `"                                    working_question, revised_draft, sources[:MAX_LLM_CITED_SOURCES]"` | — |
| [SRC-1AE03B9EC3-L006220](../../agents/web_agent.py#L6220) | 6220 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L006221](../../agents/web_agent.py#L6221) | 6221 | `"                                answer = revised_answer"` | — |
| [SRC-1AE03B9EC3-L006222](../../agents/web_agent.py#L6222) | 6222 | `"                                review_status = \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006223](../../agents/web_agent.py#L6223) | 6223 | `"                                criterion_gap_research[\"status\"] = \"evidence_added_and_answer_regenerated\""` | — |
| [SRC-1AE03B9EC3-L006224](../../agents/web_agent.py#L6224) | 6224 | `"                            except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L006225](../../agents/web_agent.py#L6225) | 6225 | `"                                criterion_gap_research[\"status\"] = \"evidence_added_but_regeneration_unavailable\""` | — |
| [SRC-1AE03B9EC3-L006226](../../agents/web_agent.py#L6226) | 6226 | `"                                criterion_gap_research[\"regeneration_error_class\"] = type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L006227](../../agents/web_agent.py#L6227) | 6227 | `"                                coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L006228](../../agents/web_agent.py#L6228) | 6228 | `"                                    \"وصلت أدلة إضافية لمحور مطلوب، لكن تعذرت إعادة توليد الإجابة \""` | — |
| [SRC-1AE03B9EC3-L006229](../../agents/web_agent.py#L6229) | 6229 | `"                                    \"وتدقيقها ضمن الميزانية؛ راجع هذا المحور قبل اعتماد الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L006230](../../agents/web_agent.py#L6230) | 6230 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L006231](../../agents/web_agent.py#L6231) | 6231 | `"                        elif criterion_gap_research.get(\"status\") != \"search_failed\":"` | — |
| [SRC-1AE03B9EC3-L006232](../../agents/web_agent.py#L6232) | 6232 | `"                            criterion_gap_research[\"status\"] = \"search_completed_no_new_criterion_evidence\""` | — |
| [SRC-1AE03B9EC3-L006233](../../agents/web_agent.py#L6233) | 6233 | `"                            coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L006234](../../agents/web_agent.py#L6234) | 6234 | `"                                \"أُجري بحث إضافي لمحاور ناقصة، لكنه لم يضف نص مصدر يمكن تمييزه \""` | — |
| [SRC-1AE03B9EC3-L006235](../../agents/web_agent.py#L6235) | 6235 | `"                                \"كدليل جديد؛ ستظل هذه المحاور غير محسومة.\""` | — |
| [SRC-1AE03B9EC3-L006236](../../agents/web_agent.py#L6236) | 6236 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L006237](../../agents/web_agent.py#L6237) | 6237 | `"                        criterion_gap_research[\"source_count_after\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L006238](../../agents/web_agent.py#L6238) | 6238 | `"                        report[\"criterion_gap_research\"] = dict(criterion_gap_research)"` | — |
| [SRC-1AE03B9EC3-L006239](../../agents/web_agent.py#L6239) | 6239 | `""` | — |
| [SRC-1AE03B9EC3-L006240](../../agents/web_agent.py#L6240) | 6240 | `"        report[\"criterion_gap_research\"] = dict(criterion_gap_research)"` | — |
| [SRC-1AE03B9EC3-L006241](../../agents/web_agent.py#L6241) | 6241 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L006242](../../agents/web_agent.py#L6242) | 6242 | `"            coverage_targets"` | — |
| [SRC-1AE03B9EC3-L006243](../../agents/web_agent.py#L6243) | 6243 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006244](../../agents/web_agent.py#L6244) | 6244 | `"            and sources"` | — |
| [SRC-1AE03B9EC3-L006245](../../agents/web_agent.py#L6245) | 6245 | `"            and self.api_key"` | — |
| [SRC-1AE03B9EC3-L006246](../../agents/web_agent.py#L6246) | 6246 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L006247](../../agents/web_agent.py#L6247) | 6247 | `"            initial_integrity = audit_answer_integrity(working_question, answer, sources, coverage_targets, plan.get(\"requirement_queries\"))"` | — |
| [SRC-1AE03B9EC3-L006248](../../agents/web_agent.py#L6248) | 6248 | `"            missing_targets = ["` | — |
| [SRC-1AE03B9EC3-L006249](../../agents/web_agent.py#L6249) | 6249 | `"                item[\"target\"] for item in initial_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L006250](../../agents/web_agent.py#L6250) | 6250 | `"                if item[\"status\"] == \"possibly_missing\""` | — |
| [SRC-1AE03B9EC3-L006251](../../agents/web_agent.py#L6251) | 6251 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L006252](../../agents/web_agent.py#L6252) | 6252 | `"            remaining_source_gap_targets = ["` | — |
| [SRC-1AE03B9EC3-L006253](../../agents/web_agent.py#L6253) | 6253 | `"                item[\"target\"] for item in initial_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L006254](../../agents/web_agent.py#L6254) | 6254 | `"                if item.get(\"source_evidence_status\") == \"no_source_lexical_signal\""` | — |
| [SRC-1AE03B9EC3-L006255](../../agents/web_agent.py#L6255) | 6255 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L006256](../../agents/web_agent.py#L6256) | 6256 | `"            if not missing_targets and remaining_source_gap_targets:"` | — |
| [SRC-1AE03B9EC3-L006257](../../agents/web_agent.py#L6257) | 6257 | `"                coverage_repair_status = \"source_evidence_gap_unresolved\""` | — |
| [SRC-1AE03B9EC3-L006258](../../agents/web_agent.py#L6258) | 6258 | `"                if not coverage_repair_warning:"` | — |
| [SRC-1AE03B9EC3-L006259](../../agents/web_agent.py#L6259) | 6259 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L006260](../../agents/web_agent.py#L6260) | 6260 | `"                        \"ذُكرت المحاور في الإجابة، لكن لم تظهر لها إشارات لفظية في المصادر؛ \""` | — |
| [SRC-1AE03B9EC3-L006261](../../agents/web_agent.py#L6261) | 6261 | `"                        \"ذكر المحور لا يُعد دليلًا، لذلك تظل المهمة غير مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L006262](../../agents/web_agent.py#L6262) | 6262 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L006263](../../agents/web_agent.py#L6263) | 6263 | `"            elif not missing_targets:"` | — |
| [SRC-1AE03B9EC3-L006264](../../agents/web_agent.py#L6264) | 6264 | `"                coverage_repair_status = \"not_needed_lexical_signals_found\""` | — |
| [SRC-1AE03B9EC3-L006265](../../agents/web_agent.py#L6265) | 6265 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L006266](../../agents/web_agent.py#L6266) | 6266 | `"                coverage_repair_status = \"attempted\""` | — |
| [SRC-1AE03B9EC3-L006267](../../agents/web_agent.py#L6267) | 6267 | `"                try:"` | — |
| [SRC-1AE03B9EC3-L006268](../../agents/web_agent.py#L6268) | 6268 | `"                    repaired_answer = self._repair_answer_coverage("` | — |
| [SRC-1AE03B9EC3-L006269](../../agents/web_agent.py#L6269) | 6269 | `"                        working_question, answer, sources, missing_targets"` | — |
| [SRC-1AE03B9EC3-L006270](../../agents/web_agent.py#L6270) | 6270 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L006271](../../agents/web_agent.py#L6271) | 6271 | `"                    if repaired_answer.strip() != answer.strip():"` | — |
| [SRC-1AE03B9EC3-L006272](../../agents/web_agent.py#L6272) | 6272 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L006273](../../agents/web_agent.py#L6273) | 6273 | `"                            reaudit_answer = self._review_answer("` | — |
| [SRC-1AE03B9EC3-L006274](../../agents/web_agent.py#L6274) | 6274 | `"                                working_question,"` | — |
| [SRC-1AE03B9EC3-L006275](../../agents/web_agent.py#L6275) | 6275 | `"                                repaired_answer,"` | — |
| [SRC-1AE03B9EC3-L006276](../../agents/web_agent.py#L6276) | 6276 | `"                                sources[:MAX_LLM_CITED_SOURCES],"` | — |
| [SRC-1AE03B9EC3-L006277](../../agents/web_agent.py#L6277) | 6277 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L006278](../../agents/web_agent.py#L6278) | 6278 | `"                            answer = reaudit_answer"` | — |
| [SRC-1AE03B9EC3-L006279](../../agents/web_agent.py#L6279) | 6279 | `"                            reaudit_integrity = audit_answer_integrity("` | — |
| [SRC-1AE03B9EC3-L006280](../../agents/web_agent.py#L6280) | 6280 | `"                                question, answer, sources, coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L006281](../../agents/web_agent.py#L6281) | 6281 | `"                                plan.get(\"requirement_queries\"),"` | — |
| [SRC-1AE03B9EC3-L006282](../../agents/web_agent.py#L6282) | 6282 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L006283](../../agents/web_agent.py#L6283) | 6283 | `"                            if reaudit_integrity[\"potentially_missing_target_count\"] > 0:"` | — |
| [SRC-1AE03B9EC3-L006284](../../agents/web_agent.py#L6284) | 6284 | `"                                coverage_repair_status = \"revised_and_reaudited_remaining_gaps\""` | — |
| [SRC-1AE03B9EC3-L006285](../../agents/web_agent.py#L6285) | 6285 | `"                                coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L006286](../../agents/web_agent.py#L6286) | 6286 | `"                                    \"خضعت الإجابة المعدلة لمراجعة ثانية، لكن الفحص اللفظي ما زال يرصد محورًا محتمل النقص؛ \""` | — |
| [SRC-1AE03B9EC3-L006287](../../agents/web_agent.py#L6287) | 6287 | `"                                    \"لا تعتبر المهمة مكتملة دون مراجعة هذا المحور والأدلة الأصلية.\""` | — |
| [SRC-1AE03B9EC3-L006288](../../agents/web_agent.py#L6288) | 6288 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L006289](../../agents/web_agent.py#L6289) | 6289 | `"                            else:"` | — |
| [SRC-1AE03B9EC3-L006290](../../agents/web_agent.py#L6290) | 6290 | `"                                coverage_repair_status = \"revised_and_reaudited\""` | — |
| [SRC-1AE03B9EC3-L006291](../../agents/web_agent.py#L6291) | 6291 | `"                            review_status = \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006292](../../agents/web_agent.py#L6292) | 6292 | `"                        except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L006293](../../agents/web_agent.py#L6293) | 6293 | `"                            review_status = \"model_claim_audit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L006294](../../agents/web_agent.py#L6294) | 6294 | `"                            review_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L006295](../../agents/web_agent.py#L6295) | 6295 | `"                            coverage_repair_status = ("` | — |
| [SRC-1AE03B9EC3-L006296](../../agents/web_agent.py#L6296) | 6296 | `"                                \"reaudit_budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L006297](../../agents/web_agent.py#L6297) | 6297 | `"                                if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L006298](../../agents/web_agent.py#L6298) | 6298 | `"                                else \"reaudit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L006299](../../agents/web_agent.py#L6299) | 6299 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L006300](../../agents/web_agent.py#L6300) | 6300 | `"                            review_warning = ("` | — |
| [SRC-1AE03B9EC3-L006301](../../agents/web_agent.py#L6301) | 6301 | `"                                \"استُنفدت ميزانية النماذج قبل إعادة تدقيق الإجابة المعدلة؛ \""` | — |
| [SRC-1AE03B9EC3-L006302](../../agents/web_agent.py#L6302) | 6302 | `"                                \"لذلك لن أعرض النص المعدل بوصفه إجابة مكتملة، وأعرض مقتطفات المصادر بدلًا منه.\""` | — |
| [SRC-1AE03B9EC3-L006303](../../agents/web_agent.py#L6303) | 6303 | `"                                if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L006304](../../agents/web_agent.py#L6304) | 6304 | `"                                else"` | — |
| [SRC-1AE03B9EC3-L006305](../../agents/web_agent.py#L6305) | 6305 | `"                                \"تعذرت إعادة تدقيق الإجابة المعدلة مقابل الأدلة؛ لذلك لن أعرضها بوصفها إجابة مكتملة، \""` | — |
| [SRC-1AE03B9EC3-L006306](../../agents/web_agent.py#L6306) | 6306 | `"                                \"وأعرض مقتطفات المصادر بدلًا منها.\""` | — |
| [SRC-1AE03B9EC3-L006307](../../agents/web_agent.py#L6307) | 6307 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L006308](../../agents/web_agent.py#L6308) | 6308 | `"                            answer = _fallback_answer(sources, review_warning)"` | — |
| [SRC-1AE03B9EC3-L006309](../../agents/web_agent.py#L6309) | 6309 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L006310](../../agents/web_agent.py#L6310) | 6310 | `"                        coverage_repair_status = \"no_change_gap_unresolved\""` | — |
| [SRC-1AE03B9EC3-L006311](../../agents/web_agent.py#L6311) | 6311 | `"                        coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L006312](../../agents/web_agent.py#L6312) | 6312 | `"                            \"رصد الفحص اللفظي محورًا قد يكون ناقصًا، لكن محاولة الإصلاح لم تغيّر الإجابة؛ \""` | — |
| [SRC-1AE03B9EC3-L006313](../../agents/web_agent.py#L6313) | 6313 | `"                            \"تحقق من تغطية هذا المحور يدويًا.\""` | — |
| [SRC-1AE03B9EC3-L006314](../../agents/web_agent.py#L6314) | 6314 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L006315](../../agents/web_agent.py#L6315) | 6315 | `"                except RequestBudgetExceeded:"` | — |
| [SRC-1AE03B9EC3-L006316](../../agents/web_agent.py#L6316) | 6316 | `"                    coverage_repair_status = \"budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L006317](../../agents/web_agent.py#L6317) | 6317 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L006318](../../agents/web_agent.py#L6318) | 6318 | `"                        \"استُنفدت ميزانية النماذج قبل محاولة إصلاح محور قد يكون ناقصًا؛ \""` | — |
| [SRC-1AE03B9EC3-L006319](../../agents/web_agent.py#L6319) | 6319 | `"                        \"لا تعتبر التغطية مكتملة دون مراجعة المحور المذكور.\""` | — |
| [SRC-1AE03B9EC3-L006320](../../agents/web_agent.py#L6320) | 6320 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L006321](../../agents/web_agent.py#L6321) | 6321 | `"                except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L006322](../../agents/web_agent.py#L6322) | 6322 | `"                    coverage_repair_status = \"unavailable\""` | — |
| [SRC-1AE03B9EC3-L006323](../../agents/web_agent.py#L6323) | 6323 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L006324](../../agents/web_agent.py#L6324) | 6324 | `"                        \"تعذرت محاولة إصلاح محور قد يكون ناقصًا (\""` | — |
| [SRC-1AE03B9EC3-L006325](../../agents/web_agent.py#L6325) | 6325 | `"                        + type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L006326](../../agents/web_agent.py#L6326) | 6326 | `"                        + \")؛ راجع المحاور المطلوبة قبل اعتماد الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L006327](../../agents/web_agent.py#L6327) | 6327 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L006328](../../agents/web_agent.py#L6328) | 6328 | `"        elif coverage_targets and review_status == \"model_claim_audit_completed\" and not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L006329](../../agents/web_agent.py#L6329) | 6329 | `"            coverage_repair_status = \"skipped_no_model_configuration\""` | — |
| [SRC-1AE03B9EC3-L006330](../../agents/web_agent.py#L6330) | 6330 | `"        elif coverage_targets:"` | — |
| [SRC-1AE03B9EC3-L006331](../../agents/web_agent.py#L6331) | 6331 | `"            coverage_repair_status = \"skipped_review_unavailable\""` | — |
| [SRC-1AE03B9EC3-L006332](../../agents/web_agent.py#L6332) | 6332 | `""` | — |
| [SRC-1AE03B9EC3-L006333](../../agents/web_agent.py#L6333) | 6333 | `"        if self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L006334](../../agents/web_agent.py#L6334) | 6334 | `"            answer += \"\\n\\nروابط إضافية من البحث المباشر عبر الويب:\""` | — |
| [SRC-1AE03B9EC3-L006335](../../agents/web_agent.py#L6335) | 6335 | `"            for source in self.server_search_sources[:8]:"` | — |
| [SRC-1AE03B9EC3-L006336](../../agents/web_agent.py#L6336) | 6336 | `"                answer += \"\\n- \" + source[\"title\"] + \" — \" + source[\"url\"]"` | — |
| [SRC-1AE03B9EC3-L006337](../../agents/web_agent.py#L6337) | 6337 | `"        max_citable_sources = min(MAX_LLM_CITED_SOURCES, len(sources))"` | — |
| [SRC-1AE03B9EC3-L006338](../../agents/web_agent.py#L6338) | 6338 | `"        answer, citation_warnings = self._remove_invalid_citations("` | — |
| [SRC-1AE03B9EC3-L006339](../../agents/web_agent.py#L6339) | 6339 | `"            answer, max_citable_sources"` | — |
| [SRC-1AE03B9EC3-L006340](../../agents/web_agent.py#L6340) | 6340 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006341](../../agents/web_agent.py#L6341) | 6341 | `"        citation_validation = self._citation_validation_metadata("` | — |
| [SRC-1AE03B9EC3-L006342](../../agents/web_agent.py#L6342) | 6342 | `"            answer, max_citable_sources, citation_warnings, review_status"` | — |
| [SRC-1AE03B9EC3-L006343](../../agents/web_agent.py#L6343) | 6343 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006344](../../agents/web_agent.py#L6344) | 6344 | `"        report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L006345](../../agents/web_agent.py#L6345) | 6345 | `"        report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L006346](../../agents/web_agent.py#L6346) | 6346 | `"        report[\"second_pass_review\"] = review_status"` | — |
| [SRC-1AE03B9EC3-L006347](../../agents/web_agent.py#L6347) | 6347 | `"        report[\"claim_audit\"] = review_status"` | — |
| [SRC-1AE03B9EC3-L006348](../../agents/web_agent.py#L6348) | 6348 | `"        answer_coverage = {"` | — |
| [SRC-1AE03B9EC3-L006349](../../agents/web_agent.py#L6349) | 6349 | `"            \"method\": \"explicit_criteria_heuristic\","` | — |
| [SRC-1AE03B9EC3-L006350](../../agents/web_agent.py#L6350) | 6350 | `"            \"targets\": coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L006351](../../agents/web_agent.py#L6351) | 6351 | `"            \"review_prompted\": review_status == \"model_claim_audit_completed\","` | — |
| [SRC-1AE03B9EC3-L006352](../../agents/web_agent.py#L6352) | 6352 | `"            \"status\": ("` | — |
| [SRC-1AE03B9EC3-L006353](../../agents/web_agent.py#L6353) | 6353 | `"                \"model_review_requested_not_machine_verified\""` | — |
| [SRC-1AE03B9EC3-L006354](../../agents/web_agent.py#L6354) | 6354 | `"                if coverage_targets and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006355](../../agents/web_agent.py#L6355) | 6355 | `"                else \"review_unavailable\""` | — |
| [SRC-1AE03B9EC3-L006356](../../agents/web_agent.py#L6356) | 6356 | `"                if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L006357](../../agents/web_agent.py#L6357) | 6357 | `"                else \"no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L006358](../../agents/web_agent.py#L6358) | 6358 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L006359](../../agents/web_agent.py#L6359) | 6359 | `"            \"automatically_graded\": False,"` | — |
| [SRC-1AE03B9EC3-L006360](../../agents/web_agent.py#L6360) | 6360 | `"        }"` | — |
| [SRC-1AE03B9EC3-L006361](../../agents/web_agent.py#L6361) | 6361 | `"        report[\"answer_coverage\"] = answer_coverage"` | — |
| [SRC-1AE03B9EC3-L006362](../../agents/web_agent.py#L6362) | 6362 | `"        report[\"coverage_repair_status\"] = coverage_repair_status"` | — |
| [SRC-1AE03B9EC3-L006363](../../agents/web_agent.py#L6363) | 6363 | `"        report[\"coverage_repair_warning\"] = coverage_repair_warning"` | — |
| [SRC-1AE03B9EC3-L006364](../../agents/web_agent.py#L6364) | 6364 | `"        answer_integrity = audit_answer_integrity(working_question, answer, sources, coverage_targets, plan.get(\"requirement_queries\"))"` | — |
| [SRC-1AE03B9EC3-L006365](../../agents/web_agent.py#L6365) | 6365 | `"        answer_coverage[\"target_checks\"] = answer_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L006366](../../agents/web_agent.py#L6366) | 6366 | `"        answer_coverage[\"potentially_missing_target_count\"] = answer_integrity[\"potentially_missing_target_count\"]"` | — |
| [SRC-1AE03B9EC3-L006367](../../agents/web_agent.py#L6367) | 6367 | `"        answer_coverage[\"source_evidence_gap_count\"] = answer_integrity[\"source_evidence_gap_count\"]"` | — |
| [SRC-1AE03B9EC3-L006368](../../agents/web_agent.py#L6368) | 6368 | `"        answer_coverage[\"lexical_screen_method\"] = \"deterministic_lexical_screen_only_not_semantic_grading\""` | — |
| [SRC-1AE03B9EC3-L006369](../../agents/web_agent.py#L6369) | 6369 | `"        requirements_without_candidates = int("` | — |
| [SRC-1AE03B9EC3-L006370](../../agents/web_agent.py#L6370) | 6370 | `"            answer_integrity.get(\"requirements_without_candidate_evidence_count\", 0) or 0"` | — |
| [SRC-1AE03B9EC3-L006371](../../agents/web_agent.py#L6371) | 6371 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006372](../../agents/web_agent.py#L6372) | 6372 | `"        task_fulfillment_status = ("` | — |
| [SRC-1AE03B9EC3-L006373](../../agents/web_agent.py#L6373) | 6373 | `"            \"possible_gap_detected\""` | — |
| [SRC-1AE03B9EC3-L006374](../../agents/web_agent.py#L6374) | 6374 | `"            if ("` | — |
| [SRC-1AE03B9EC3-L006375](../../agents/web_agent.py#L6375) | 6375 | `"                answer_integrity[\"potentially_missing_target_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L006376](../../agents/web_agent.py#L6376) | 6376 | `"                or answer_integrity[\"source_evidence_gap_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L006377](../../agents/web_agent.py#L6377) | 6377 | `"            )"` | — |
| [SRC-1AE03B9EC3-L006378](../../agents/web_agent.py#L6378) | 6378 | `"            else \"candidate_evidence_gaps_or_linkage_unknown\""` | — |
| [SRC-1AE03B9EC3-L006379](../../agents/web_agent.py#L6379) | 6379 | `"            if coverage_targets and requirements_without_candidates > 0"` | — |
| [SRC-1AE03B9EC3-L006380](../../agents/web_agent.py#L6380) | 6380 | `"            else \"lexical_signals_found_not_semantically_verified\" if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L006381](../../agents/web_agent.py#L6381) | 6381 | `"            else \"not_machine_assessed_no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L006382](../../agents/web_agent.py#L6382) | 6382 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006383](../../agents/web_agent.py#L6383) | 6383 | `"        answer_coverage[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L006384](../../agents/web_agent.py#L6384) | 6384 | `"        report[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L006385](../../agents/web_agent.py#L6385) | 6385 | `"        report[\"answer_integrity\"] = answer_integrity"` | — |
| [SRC-1AE03B9EC3-L006386](../../agents/web_agent.py#L6386) | 6386 | `"        report[\"requirement_evidence\"] = answer_integrity.get(\"requirement_evidence\", [])"` | — |
| [SRC-1AE03B9EC3-L006387](../../agents/web_agent.py#L6387) | 6387 | `"        report[\"connector_summary\"] = self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L006388](../../agents/web_agent.py#L6388) | 6388 | `"            list(self._provider_diagnostics), sources"` | — |
| [SRC-1AE03B9EC3-L006389](../../agents/web_agent.py#L6389) | 6389 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006390](../../agents/web_agent.py#L6390) | 6390 | `"        report[\"provider_diagnostics\"] = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L006391](../../agents/web_agent.py#L6391) | 6391 | `"        distinct_providers = {"` | — |
| [SRC-1AE03B9EC3-L006392](../../agents/web_agent.py#L6392) | 6392 | `"            provider for source in sources for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L006393](../../agents/web_agent.py#L6393) | 6393 | `"        }"` | — |
| [SRC-1AE03B9EC3-L006394](../../agents/web_agent.py#L6394) | 6394 | `"        distinct_domains = {"` | — |
| [SRC-1AE03B9EC3-L006395](../../agents/web_agent.py#L6395) | 6395 | `"            registrable_domain("` | — |
| [SRC-1AE03B9EC3-L006396](../../agents/web_agent.py#L6396) | 6396 | `"                source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L006397](../../agents/web_agent.py#L6397) | 6397 | `"                or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L006398](../../agents/web_agent.py#L6398) | 6398 | `"                or \"\""` | — |
| [SRC-1AE03B9EC3-L006399](../../agents/web_agent.py#L6399) | 6399 | `"            )"` | — |
| [SRC-1AE03B9EC3-L006400](../../agents/web_agent.py#L6400) | 6400 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L006401](../../agents/web_agent.py#L6401) | 6401 | `"        }"` | — |
| [SRC-1AE03B9EC3-L006402](../../agents/web_agent.py#L6402) | 6402 | `"        distinct_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L006403](../../agents/web_agent.py#L6403) | 6403 | `"        fetched_pages = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L006404](../../agents/web_agent.py#L6404) | 6404 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L006405](../../agents/web_agent.py#L6405) | 6405 | `"            len(sources) >= 4 and len(distinct_domains) >= 3"` | — |
| [SRC-1AE03B9EC3-L006406](../../agents/web_agent.py#L6406) | 6406 | `"            and len(distinct_providers) >= 2 and fetched_pages >= 1"` | — |
| [SRC-1AE03B9EC3-L006407](../../agents/web_agent.py#L6407) | 6407 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006408](../../agents/web_agent.py#L6408) | 6408 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L006409](../../agents/web_agent.py#L6409) | 6409 | `"            research_quality = \"excellent\""` | — |
| [SRC-1AE03B9EC3-L006410](../../agents/web_agent.py#L6410) | 6410 | `"        elif ("` | — |
| [SRC-1AE03B9EC3-L006411](../../agents/web_agent.py#L6411) | 6411 | `"            len(sources) >= 2 and len(distinct_domains) >= 2"` | — |
| [SRC-1AE03B9EC3-L006412](../../agents/web_agent.py#L6412) | 6412 | `"            and (len(distinct_providers) >= 2 or fetched_pages >= 1)"` | — |
| [SRC-1AE03B9EC3-L006413](../../agents/web_agent.py#L6413) | 6413 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006414](../../agents/web_agent.py#L6414) | 6414 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L006415](../../agents/web_agent.py#L6415) | 6415 | `"            research_quality = \"good\""` | — |
| [SRC-1AE03B9EC3-L006416](../../agents/web_agent.py#L6416) | 6416 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L006417](../../agents/web_agent.py#L6417) | 6417 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L006418](../../agents/web_agent.py#L6418) | 6418 | `""` | — |
| [SRC-1AE03B9EC3-L006419](../../agents/web_agent.py#L6419) | 6419 | `"        # Source breadth and a completed model-assisted review do not justify a"` | — |
| [SRC-1AE03B9EC3-L006420](../../agents/web_agent.py#L6420) | 6420 | `"        # positive research-quality label if the final answer has no valid source"` | — |
| [SRC-1AE03B9EC3-L006421](../../agents/web_agent.py#L6421) | 6421 | `"        # citation markers. This is a deterministic presentation guard, not a"` | — |
| [SRC-1AE03B9EC3-L006422](../../agents/web_agent.py#L6422) | 6422 | `"        # semantic entailment check."` | — |
| [SRC-1AE03B9EC3-L006423](../../agents/web_agent.py#L6423) | 6423 | `"        uncited_reviewed_answer = ("` | — |
| [SRC-1AE03B9EC3-L006424](../../agents/web_agent.py#L6424) | 6424 | `"            used_llm"` | — |
| [SRC-1AE03B9EC3-L006425](../../agents/web_agent.py#L6425) | 6425 | `"            and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L006426](../../agents/web_agent.py#L6426) | 6426 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006427](../../agents/web_agent.py#L6427) | 6427 | `"            and citation_validation[\"valid_citation_count\"] == 0"` | — |
| [SRC-1AE03B9EC3-L006428](../../agents/web_agent.py#L6428) | 6428 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006429](../../agents/web_agent.py#L6429) | 6429 | `"        if uncited_reviewed_answer:"` | — |
| [SRC-1AE03B9EC3-L006430](../../agents/web_agent.py#L6430) | 6430 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L006431](../../agents/web_agent.py#L6431) | 6431 | `"            citation_validation[\"claim_support\"] = \"not_established_no_valid_source_citations\""` | — |
| [SRC-1AE03B9EC3-L006432](../../agents/web_agent.py#L6432) | 6432 | `"            answer_evidence_status = \"reviewed_answer_has_no_valid_citations\""` | — |
| [SRC-1AE03B9EC3-L006433](../../agents/web_agent.py#L6433) | 6433 | `"            uncited_answer_warning = ("` | — |
| [SRC-1AE03B9EC3-L006434](../../agents/web_agent.py#L6434) | 6434 | `"                \"اكتملت مراجعة النموذج، لكن الإجابة النهائية لا تحتوي على إحالات صالحة \""` | — |
| [SRC-1AE03B9EC3-L006435](../../agents/web_agent.py#L6435) | 6435 | `"                \"إلى قائمة المصادر؛ لذلك صُنّفت جودة البحث «جزئية». وجود المصادر أو \""` | — |
| [SRC-1AE03B9EC3-L006436](../../agents/web_agent.py#L6436) | 6436 | `"                \"اكتمال مراجعة النموذج لا يثبت دعم كل ادعاء.\""` | — |
| [SRC-1AE03B9EC3-L006437](../../agents/web_agent.py#L6437) | 6437 | `"            )"` | — |
| [SRC-1AE03B9EC3-L006438](../../agents/web_agent.py#L6438) | 6438 | `"        elif citation_validation[\"valid_citation_count\"] > 0:"` | — |
| [SRC-1AE03B9EC3-L006439](../../agents/web_agent.py#L6439) | 6439 | `"            answer_evidence_status = \"citation_indices_validated_only\""` | — |
| [SRC-1AE03B9EC3-L006440](../../agents/web_agent.py#L6440) | 6440 | `"            uncited_answer_warning = None"` | — |
| [SRC-1AE03B9EC3-L006441](../../agents/web_agent.py#L6441) | 6441 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L006442](../../agents/web_agent.py#L6442) | 6442 | `"            answer_evidence_status = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L006443](../../agents/web_agent.py#L6443) | 6443 | `"            uncited_answer_warning = None"` | — |
| [SRC-1AE03B9EC3-L006444](../../agents/web_agent.py#L6444) | 6444 | `""` | — |
| [SRC-1AE03B9EC3-L006445](../../agents/web_agent.py#L6445) | 6445 | `"        search_attempted = search_attempted or bool(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L006446](../../agents/web_agent.py#L6446) | 6446 | `"        report[\"search_attempted\"] = search_attempted"` | — |
| [SRC-1AE03B9EC3-L006447](../../agents/web_agent.py#L6447) | 6447 | `"        prior_search_outcome = report.get(\"search_outcome\")"` | — |
| [SRC-1AE03B9EC3-L006448](../../agents/web_agent.py#L6448) | 6448 | `"        if prior_search_outcome in _RESEARCH_ERROR_OUTCOMES and not sources:"` | — |
| [SRC-1AE03B9EC3-L006449](../../agents/web_agent.py#L6449) | 6449 | `"            # Preserve a known pipeline failure instead of relabeling it as an ordinary"` | — |
| [SRC-1AE03B9EC3-L006450](../../agents/web_agent.py#L6450) | 6450 | `"            # zero-result search merely because the outer request reached its return path."` | — |
| [SRC-1AE03B9EC3-L006451](../../agents/web_agent.py#L6451) | 6451 | `"            report[\"search_outcome\"] = prior_search_outcome"` | — |
| [SRC-1AE03B9EC3-L006452](../../agents/web_agent.py#L6452) | 6452 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L006453](../../agents/web_agent.py#L6453) | 6453 | `"            report[\"search_outcome\"] = ("` | — |
| [SRC-1AE03B9EC3-L006454](../../agents/web_agent.py#L6454) | 6454 | `"                \"attempted_with_usable_sources\" if search_attempted and sources"` | — |
| [SRC-1AE03B9EC3-L006455](../../agents/web_agent.py#L6455) | 6455 | `"                else \"attempted_no_usable_sources\" if search_attempted"` | — |
| [SRC-1AE03B9EC3-L006456](../../agents/web_agent.py#L6456) | 6456 | `"                else \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L006457](../../agents/web_agent.py#L6457) | 6457 | `"            )"` | — |
| [SRC-1AE03B9EC3-L006458](../../agents/web_agent.py#L6458) | 6458 | `"        report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L006459](../../agents/web_agent.py#L6459) | 6459 | `"        report[\"research_quality\"] = research_quality"` | — |
| [SRC-1AE03B9EC3-L006460](../../agents/web_agent.py#L6460) | 6460 | `"        report[\"research_quality_semantics\"] = \"process_coverage_not_factual_probability\""` | — |
| [SRC-1AE03B9EC3-L006461](../../agents/web_agent.py#L6461) | 6461 | `"        report[\"answer_evidence_status\"] = answer_evidence_status"` | — |
| [SRC-1AE03B9EC3-L006462](../../agents/web_agent.py#L6462) | 6462 | `"        report[\"distinct_registrable_domains\"] = len(distinct_domains)"` | — |
| [SRC-1AE03B9EC3-L006463](../../agents/web_agent.py#L6463) | 6463 | `"        report[\"independent_sources\"] = len(distinct_domains)  # Legacy alias; not editorial independence."` | — |
| [SRC-1AE03B9EC3-L006464](../../agents/web_agent.py#L6464) | 6464 | `"        report[\"independent_sources_field_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L006465](../../agents/web_agent.py#L6465) | 6465 | `"            \"legacy_compatibility_alias_for_distinct_registrable_domain_count\""` | — |
| [SRC-1AE03B9EC3-L006466](../../agents/web_agent.py#L6466) | 6466 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006467](../../agents/web_agent.py#L6467) | 6467 | `"        report[\"source_diversity_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L006468](../../agents/web_agent.py#L6468) | 6468 | `"            \"distinct_registrable_domains_not_editorial_independence\""` | — |
| [SRC-1AE03B9EC3-L006469](../../agents/web_agent.py#L6469) | 6469 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006470](../../agents/web_agent.py#L6470) | 6470 | `"        report[\"editorial_independence_status\"] = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L006471](../../agents/web_agent.py#L6471) | 6471 | `"        report[\"claim_audit_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L006472](../../agents/web_agent.py#L6472) | 6472 | `"            \"model_assisted_not_independent_fact_check\""` | — |
| [SRC-1AE03B9EC3-L006473](../../agents/web_agent.py#L6473) | 6473 | `"            if review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006474](../../agents/web_agent.py#L6474) | 6474 | `"            else \"not_verified\""` | — |
| [SRC-1AE03B9EC3-L006475](../../agents/web_agent.py#L6475) | 6475 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006476](../../agents/web_agent.py#L6476) | 6476 | `"        report[\"insufficient_evidence\"] = bool("` | — |
| [SRC-1AE03B9EC3-L006477](../../agents/web_agent.py#L6477) | 6477 | `"            report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES"` | — |
| [SRC-1AE03B9EC3-L006478](../../agents/web_agent.py#L6478) | 6478 | `"            or not sources"` | — |
| [SRC-1AE03B9EC3-L006479](../../agents/web_agent.py#L6479) | 6479 | `"            or answer_integrity[\"source_evidence_gap_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L006480](../../agents/web_agent.py#L6480) | 6480 | `"            or ("` | — |
| [SRC-1AE03B9EC3-L006481](../../agents/web_agent.py#L6481) | 6481 | `"                bool(coverage_targets)"` | — |
| [SRC-1AE03B9EC3-L006482](../../agents/web_agent.py#L6482) | 6482 | `"                and answer_integrity[\"potentially_missing_target_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L006483](../../agents/web_agent.py#L6483) | 6483 | `"            )"` | — |
| [SRC-1AE03B9EC3-L006484](../../agents/web_agent.py#L6484) | 6484 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006485](../../agents/web_agent.py#L6485) | 6485 | `"        report[\"valid_citation_range\"] = [1, max_citable_sources] if max_citable_sources else []"` | — |
| [SRC-1AE03B9EC3-L006486](../../agents/web_agent.py#L6486) | 6486 | `"        report[\"citation_count\"] = citation_validation[\"valid_citation_count\"]"` | — |
| [SRC-1AE03B9EC3-L006487](../../agents/web_agent.py#L6487) | 6487 | `"        report[\"citation_check\"] = citation_validation[\"status\"]"` | — |
| [SRC-1AE03B9EC3-L006488](../../agents/web_agent.py#L6488) | 6488 | `"        report[\"citation_validation\"] = citation_validation"` | — |
| [SRC-1AE03B9EC3-L006489](../../agents/web_agent.py#L6489) | 6489 | `"        warnings = list(dict.fromkeys("` | — |
