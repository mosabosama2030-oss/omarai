# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **010**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L000729 إلى SRC-1AE03B9EC3-L001528
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L000729](../../agents/web_agent.py#L729) | 729 | `"            record[\"rejection_counts\"] = safe_counts"` | — |
| [SRC-1AE03B9EC3-L000730](../../agents/web_agent.py#L730) | 730 | `"        if error:"` | — |
| [SRC-1AE03B9EC3-L000731](../../agents/web_agent.py#L731) | 731 | `"            record[\"error\"] = redact(error, 180)"` | — |
| [SRC-1AE03B9EC3-L000732](../../agents/web_agent.py#L732) | 732 | `"        with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L000733](../../agents/web_agent.py#L733) | 733 | `"            self._provider_diagnostics.append(record)"` | — |
| [SRC-1AE03B9EC3-L000734](../../agents/web_agent.py#L734) | 734 | `"            # Bound memory when the instance serves many user requests."` | — |
| [SRC-1AE03B9EC3-L000735](../../agents/web_agent.py#L735) | 735 | `"            self._provider_diagnostics = self._provider_diagnostics[-160:]"` | — |
| [SRC-1AE03B9EC3-L000736](../../agents/web_agent.py#L736) | 736 | `""` | — |
| [SRC-1AE03B9EC3-L000737](../../agents/web_agent.py#L737) | 737 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000738](../../agents/web_agent.py#L738) | 738 | `"    def _source_matches_query(query: str, source: dict[str, Any]) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000739](../../agents/web_agent.py#L739) | 739 | `"        if \"user_supplied_url\" in source.get(\"providers\", []):"` | — |
| [SRC-1AE03B9EC3-L000740](../../agents/web_agent.py#L740) | 740 | `"            return True"` | — |
| [SRC-1AE03B9EC3-L000741](../../agents/web_agent.py#L741) | 741 | `"        evidence = \" \".join("` | — |
| [SRC-1AE03B9EC3-L000742](../../agents/web_agent.py#L742) | 742 | `"            str(source.get(key) or \"\")"` | — |
| [SRC-1AE03B9EC3-L000743](../../agents/web_agent.py#L743) | 743 | `"            for key in (\"title\", \"snippet\", \"page_text\")"` | — |
| [SRC-1AE03B9EC3-L000744](../../agents/web_agent.py#L744) | 744 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000745](../../agents/web_agent.py#L745) | 745 | `"        return _relevance_ratio(query, evidence) >= 0.20"` | — |
| [SRC-1AE03B9EC3-L000746](../../agents/web_agent.py#L746) | 746 | `""` | — |
| [SRC-1AE03B9EC3-L000747](../../agents/web_agent.py#L747) | 747 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000748](../../agents/web_agent.py#L748) | 748 | `"    def _normalized_source_url_key(value: Any) -> str:"` | — |
| [SRC-1AE03B9EC3-L000749](../../agents/web_agent.py#L749) | 749 | `"        \"\"\"Normalize a public HTTP(S) URL for duplicate detection across search rounds.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000750](../../agents/web_agent.py#L750) | 750 | `"        if not isinstance(value, str) or not value.strip():"` | — |
| [SRC-1AE03B9EC3-L000751](../../agents/web_agent.py#L751) | 751 | `"            return \"\""` | — |
| [SRC-1AE03B9EC3-L000752](../../agents/web_agent.py#L752) | 752 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000753](../../agents/web_agent.py#L753) | 753 | `"            parsed = urllib.parse.urlsplit(value.strip())"` | — |
| [SRC-1AE03B9EC3-L000754](../../agents/web_agent.py#L754) | 754 | `"            scheme = parsed.scheme.lower()"` | — |
| [SRC-1AE03B9EC3-L000755](../../agents/web_agent.py#L755) | 755 | `"            if scheme not in {\"http\", \"https\"} or not parsed.hostname:"` | — |
| [SRC-1AE03B9EC3-L000756](../../agents/web_agent.py#L756) | 756 | `"                return \"\""` | — |
| [SRC-1AE03B9EC3-L000757](../../agents/web_agent.py#L757) | 757 | `"            host = parsed.hostname.lower().rstrip(\".\")"` | — |
| [SRC-1AE03B9EC3-L000758](../../agents/web_agent.py#L758) | 758 | `"            port = parsed.port"` | — |
| [SRC-1AE03B9EC3-L000759](../../agents/web_agent.py#L759) | 759 | `"            if (scheme == \"https\" and port == 443) or (scheme == \"http\" and port == 80):"` | — |
| [SRC-1AE03B9EC3-L000760](../../agents/web_agent.py#L760) | 760 | `"                port = None"` | — |
| [SRC-1AE03B9EC3-L000761](../../agents/web_agent.py#L761) | 761 | `"            host_for_url = f\"[{host}]\" if \":\" in host else host"` | — |
| [SRC-1AE03B9EC3-L000762](../../agents/web_agent.py#L762) | 762 | `"            netloc = host_for_url + (f\":{port}\" if port is not None else \"\")"` | — |
| [SRC-1AE03B9EC3-L000763](../../agents/web_agent.py#L763) | 763 | `"            path = parsed.path.rstrip(\"/\") or \"/\""` | — |
| [SRC-1AE03B9EC3-L000764](../../agents/web_agent.py#L764) | 764 | `"            tracking_keys = {\"fbclid\", \"gclid\", \"ref\", \"source\"}"` | — |
| [SRC-1AE03B9EC3-L000765](../../agents/web_agent.py#L765) | 765 | `"            query_items = ["` | — |
| [SRC-1AE03B9EC3-L000766](../../agents/web_agent.py#L766) | 766 | `"                (key, item)"` | — |
| [SRC-1AE03B9EC3-L000767](../../agents/web_agent.py#L767) | 767 | `"                for key, item in urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)"` | — |
| [SRC-1AE03B9EC3-L000768](../../agents/web_agent.py#L768) | 768 | `"                if not key.lower().startswith(\"utm_\") and key.lower() not in tracking_keys"` | — |
| [SRC-1AE03B9EC3-L000769](../../agents/web_agent.py#L769) | 769 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L000770](../../agents/web_agent.py#L770) | 770 | `"            query = urllib.parse.urlencode(query_items, doseq=True)"` | — |
| [SRC-1AE03B9EC3-L000771](../../agents/web_agent.py#L771) | 771 | `"            return urllib.parse.urlunsplit((scheme, netloc, path, query, \"\"))"` | — |
| [SRC-1AE03B9EC3-L000772](../../agents/web_agent.py#L772) | 772 | `"        except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L000773](../../agents/web_agent.py#L773) | 773 | `"            return \"\""` | — |
| [SRC-1AE03B9EC3-L000774](../../agents/web_agent.py#L774) | 774 | `""` | — |
| [SRC-1AE03B9EC3-L000775](../../agents/web_agent.py#L775) | 775 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000776](../../agents/web_agent.py#L776) | 776 | `"    def _question_coverage_targets(question: str) -> list[str]:"` | — |
| [SRC-1AE03B9EC3-L000777](../../agents/web_agent.py#L777) | 777 | `"        \"\"\"Use the richer aspect parser, then the shared deterministic fallback.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000778](../../agents/web_agent.py#L778) | 778 | `"        enhanced_targets = extract_aspects(question)"` | — |
| [SRC-1AE03B9EC3-L000779](../../agents/web_agent.py#L779) | 779 | `"        if enhanced_targets:"` | — |
| [SRC-1AE03B9EC3-L000780](../../agents/web_agent.py#L780) | 780 | `"            return enhanced_targets[:8]"` | — |
| [SRC-1AE03B9EC3-L000781](../../agents/web_agent.py#L781) | 781 | `"        return extract_question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L000782](../../agents/web_agent.py#L782) | 782 | `""` | — |
| [SRC-1AE03B9EC3-L000783](../../agents/web_agent.py#L783) | 783 | `""` | — |
| [SRC-1AE03B9EC3-L000784](../../agents/web_agent.py#L784) | 784 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000785](../../agents/web_agent.py#L785) | 785 | `"    def _is_current_search_status_question(question: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000786](../../agents/web_agent.py#L786) | 786 | `"        \"\"\"Recognize a question about whether this answer already used web search.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000787](../../agents/web_agent.py#L787) | 787 | `"        value = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L000788](../../agents/web_agent.py#L788) | 788 | `"        asks_if_searched = any("` | — |
| [SRC-1AE03B9EC3-L000789](../../agents/web_agent.py#L789) | 789 | `"            term in value"` | — |
| [SRC-1AE03B9EC3-L000790](../../agents/web_agent.py#L790) | 790 | `"            for term in (\"بحثت\", \"اجريت بحث\", \"قمت بالبحث\", \"عملت بحث\", \"did you search\", \"did you browse\")"` | — |
| [SRC-1AE03B9EC3-L000791](../../agents/web_agent.py#L791) | 791 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000792](../../agents/web_agent.py#L792) | 792 | `"        references_web = any("` | — |
| [SRC-1AE03B9EC3-L000793](../../agents/web_agent.py#L793) | 793 | `"            term in value for term in (\"انترنت\", \"النت\", \"الويب\", \"ويب\", \"the web\", \"online\")"` | — |
| [SRC-1AE03B9EC3-L000794](../../agents/web_agent.py#L794) | 794 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000795](../../agents/web_agent.py#L795) | 795 | `"        references_current_answer = any("` | — |
| [SRC-1AE03B9EC3-L000796](../../agents/web_agent.py#L796) | 796 | `"            term in value"` | — |
| [SRC-1AE03B9EC3-L000797](../../agents/web_agent.py#L797) | 797 | `"            for term in ("` | — |
| [SRC-1AE03B9EC3-L000798](../../agents/web_agent.py#L798) | 798 | `"                \"اجاب\", \"الرد الحالي\", \"هذا السؤال\", \"هذه الاجابه\","` | — |
| [SRC-1AE03B9EC3-L000799](../../agents/web_agent.py#L799) | 799 | `"                \"this answer\", \"this response\","` | — |
| [SRC-1AE03B9EC3-L000800](../../agents/web_agent.py#L800) | 800 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000801](../../agents/web_agent.py#L801) | 801 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000802](../../agents/web_agent.py#L802) | 802 | `"        return asks_if_searched and references_web and references_current_answer"` | — |
| [SRC-1AE03B9EC3-L000803](../../agents/web_agent.py#L803) | 803 | `""` | — |
| [SRC-1AE03B9EC3-L000804](../../agents/web_agent.py#L804) | 804 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000805](../../agents/web_agent.py#L805) | 805 | `"    def _is_self_question(question: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000806](../../agents/web_agent.py#L806) | 806 | `"        \"\"\"Recognize questions about Omarai itself so they do not need web search.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000807](../../agents/web_agent.py#L807) | 807 | `"        value = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L000808](../../agents/web_agent.py#L808) | 808 | `"        capability_phrases = ("` | — |
| [SRC-1AE03B9EC3-L000809](../../agents/web_agent.py#L809) | 809 | `"            \"كيف تستطيع مساعدتي\", \"ازاي تقدر تساعدني\", \"ازاي ممكن تساعدني\","` | — |
| [SRC-1AE03B9EC3-L000810](../../agents/web_agent.py#L810) | 810 | `"            \"ماذا تستطيع ان تفعل\", \"ما الذي تستطيع فعله\", \"ايه اللي تقدر تعمله\","` | — |
| [SRC-1AE03B9EC3-L000811](../../agents/web_agent.py#L811) | 811 | `"            \"what can you do\", \"how can you help me\","` | — |
| [SRC-1AE03B9EC3-L000812](../../agents/web_agent.py#L812) | 812 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000813](../../agents/web_agent.py#L813) | 813 | `"        search_phrases = ("` | — |
| [SRC-1AE03B9EC3-L000814](../../agents/web_agent.py#L814) | 814 | `"            \"كيف تبحث انت\", \"ازاي بتبحث\", \"كيف يعمل البحث عندك\","` | — |
| [SRC-1AE03B9EC3-L000815](../../agents/web_agent.py#L815) | 815 | `"            \"ما المواقع التي تستخدمها\", \"ما محركات البحث التي تستخدمها\","` | — |
| [SRC-1AE03B9EC3-L000816](../../agents/web_agent.py#L816) | 816 | `"            \"ما المواقع التي قدرت\", \"كيف تبحث على الانترنت\","` | — |
| [SRC-1AE03B9EC3-L000817](../../agents/web_agent.py#L817) | 817 | `"            \"هل تستطيع البحث\", \"هل يمكنك البحث\", \"هل تقدر تبحث\","` | — |
| [SRC-1AE03B9EC3-L000818](../../agents/web_agent.py#L818) | 818 | `"            \"هل تستطيع الوصول\", \"هل يمكنك الوصول\","` | — |
| [SRC-1AE03B9EC3-L000819](../../agents/web_agent.py#L819) | 819 | `"            \"هل عندك اتصال بالانترنت\", \"هل عندك اتصال بالانترنيت\","` | — |
| [SRC-1AE03B9EC3-L000820](../../agents/web_agent.py#L820) | 820 | `"            \"هل عندك انترنت\","` | — |
| [SRC-1AE03B9EC3-L000821](../../agents/web_agent.py#L821) | 821 | `"            \"هل بحثت في الانترنت للاجابه الحاليه\","` | — |
| [SRC-1AE03B9EC3-L000822](../../agents/web_agent.py#L822) | 822 | `"            \"هل بحثت علي الانترنت للاجابه الحاليه\","` | — |
| [SRC-1AE03B9EC3-L000823](../../agents/web_agent.py#L823) | 823 | `"            \"هل بحثت في الانترنت لهذا السؤال\","` | — |
| [SRC-1AE03B9EC3-L000824](../../agents/web_agent.py#L824) | 824 | `"            \"هل بحثت في النت للرد ده\","` | — |
| [SRC-1AE03B9EC3-L000825](../../agents/web_agent.py#L825) | 825 | `"            \"did you search the web for this answer\","` | — |
| [SRC-1AE03B9EC3-L000826](../../agents/web_agent.py#L826) | 826 | `"            \"did you browse for this response\","` | — |
| [SRC-1AE03B9EC3-L000827](../../agents/web_agent.py#L827) | 827 | `"            \"how do you search\", \"which search engines\", \"what sites do you use\","` | — |
| [SRC-1AE03B9EC3-L000828](../../agents/web_agent.py#L828) | 828 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000829](../../agents/web_agent.py#L829) | 829 | `"        return ("` | — |
| [SRC-1AE03B9EC3-L000830](../../agents/web_agent.py#L830) | 830 | `"            any(phrase in value for phrase in capability_phrases + search_phrases)"` | — |
| [SRC-1AE03B9EC3-L000831](../../agents/web_agent.py#L831) | 831 | `"            or WebAgent._is_current_search_status_question(question)"` | — |
| [SRC-1AE03B9EC3-L000832](../../agents/web_agent.py#L832) | 832 | `"            or ("` | — |
| [SRC-1AE03B9EC3-L000833](../../agents/web_agent.py#L833) | 833 | `"                \"omarai\" in value"` | — |
| [SRC-1AE03B9EC3-L000834](../../agents/web_agent.py#L834) | 834 | `"                and any(token in value for token in (\"بحث\", \"موقع\", \"تستطيع\", \"تقدر\", \"تعمل\"))"` | — |
| [SRC-1AE03B9EC3-L000835](../../agents/web_agent.py#L835) | 835 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000836](../../agents/web_agent.py#L836) | 836 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000837](../../agents/web_agent.py#L837) | 837 | `""` | — |
| [SRC-1AE03B9EC3-L000838](../../agents/web_agent.py#L838) | 838 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000839](../../agents/web_agent.py#L839) | 839 | `"    def _is_navigation_request(question: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000840](../../agents/web_agent.py#L840) | 840 | `"        \"\"\"A link-finding task can be useful with one clearly labelled candidate result.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000841](../../agents/web_agent.py#L841) | 841 | `"        value = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L000842](../../agents/web_agent.py#L842) | 842 | `"        terms = ("` | — |
| [SRC-1AE03B9EC3-L000843](../../agents/web_agent.py#L843) | 843 | `"            \"موقع\", \"رابط\", \"لينك\", \"الموقع الرسمي\", \"الصفحة الرسمية\","` | — |
| [SRC-1AE03B9EC3-L000844](../../agents/web_agent.py#L844) | 844 | `"            \"official website\", \"website\", \"homepage\", \"link to\","` | — |
| [SRC-1AE03B9EC3-L000845](../../agents/web_agent.py#L845) | 845 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000846](../../agents/web_agent.py#L846) | 846 | `"        return any(term in value for term in terms)"` | — |
| [SRC-1AE03B9EC3-L000847](../../agents/web_agent.py#L847) | 847 | `""` | — |
| [SRC-1AE03B9EC3-L000848](../../agents/web_agent.py#L848) | 848 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000849](../../agents/web_agent.py#L849) | 849 | `"    def _is_lead_search(question: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000850](../../agents/web_agent.py#L850) | 850 | `"        \"\"\"Keep lead discovery distinct from listing searches and generic explanations.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000851](../../agents/web_agent.py#L851) | 851 | `"        return route_intent(question).get(\"route\") == \"LEAD_GENERATION\""` | — |
| [SRC-1AE03B9EC3-L000852](../../agents/web_agent.py#L852) | 852 | `""` | — |
| [SRC-1AE03B9EC3-L000853](../../agents/web_agent.py#L853) | 853 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000854](../../agents/web_agent.py#L854) | 854 | `"    def _lead_intent_evidence(source: dict[str, Any]) -> dict[str, str] \| None:"` | — |
| [SRC-1AE03B9EC3-L000855](../../agents/web_agent.py#L855) | 855 | `"        \"\"\"Return a narrow, inspectable public buyer-intent phrase signal, if present.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000856](../../agents/web_agent.py#L856) | 856 | `"        phrases = ("` | — |
| [SRC-1AE03B9EC3-L000857](../../agents/web_agent.py#L857) | 857 | `"            \"مطلوب شقه تمليك\", \"مطلوب شقه للشراء\", \"مطلوب شراء شقه\","` | — |
| [SRC-1AE03B9EC3-L000858](../../agents/web_agent.py#L858) | 858 | `"            \"مطلوب عقار للشراء\", \"مطلوب فيلا للشراء\","` | — |
| [SRC-1AE03B9EC3-L000859](../../agents/web_agent.py#L859) | 859 | `"            \"بدور على شقه تمليك\", \"بدور على شقه للشراء\","` | — |
| [SRC-1AE03B9EC3-L000860](../../agents/web_agent.py#L860) | 860 | `"            \"ابحث عن شقه للشراء\", \"عايز اشتري شقه\", \"عاوز اشتري شقه\","` | — |
| [SRC-1AE03B9EC3-L000861](../../agents/web_agent.py#L861) | 861 | `"            \"عايز اشتري عقار\", \"عاوز اشتري عقار\", \"اريد شراء شقه\","` | — |
| [SRC-1AE03B9EC3-L000862](../../agents/web_agent.py#L862) | 862 | `"            \"ارغب في شراء شقه\", \"اريد شراء عقار\", \"ارغب في شراء عقار\","` | — |
| [SRC-1AE03B9EC3-L000863](../../agents/web_agent.py#L863) | 863 | `"            \"looking to buy\", \"looking to purchase\", \"want to buy\","` | — |
| [SRC-1AE03B9EC3-L000864](../../agents/web_agent.py#L864) | 864 | `"            \"wants to buy\", \"want to purchase\", \"wants to purchase\","` | — |
| [SRC-1AE03B9EC3-L000865](../../agents/web_agent.py#L865) | 865 | `"            \"seeking to buy\", \"seeking to purchase\", \"interested in buying\","` | — |
| [SRC-1AE03B9EC3-L000866](../../agents/web_agent.py#L866) | 866 | `"            \"interested in purchasing\", \"buyer looking to buy\","` | — |
| [SRC-1AE03B9EC3-L000867](../../agents/web_agent.py#L867) | 867 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000868](../../agents/web_agent.py#L868) | 868 | `"        for field, basis in ((\"page_text\", \"page_text\"), (\"title\", \"title\"), (\"snippet\", \"search_snippet\")):"` | — |
| [SRC-1AE03B9EC3-L000869](../../agents/web_agent.py#L869) | 869 | `"            raw = source.get(field)"` | — |
| [SRC-1AE03B9EC3-L000870](../../agents/web_agent.py#L870) | 870 | `"            if not isinstance(raw, str) or not raw.strip():"` | — |
| [SRC-1AE03B9EC3-L000871](../../agents/web_agent.py#L871) | 871 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L000872](../../agents/web_agent.py#L872) | 872 | `"            normalized = _normalize_search_query(raw).casefold()"` | — |
| [SRC-1AE03B9EC3-L000873](../../agents/web_agent.py#L873) | 873 | `"            negations = ("` | — |
| [SRC-1AE03B9EC3-L000874](../../agents/web_agent.py#L874) | 874 | `"                \"not looking to buy\", \"not interested in buying\","` | — |
| [SRC-1AE03B9EC3-L000875](../../agents/web_agent.py#L875) | 875 | `"                \"not interested in purchasing\", \"no longer looking to buy\","` | — |
| [SRC-1AE03B9EC3-L000876](../../agents/web_agent.py#L876) | 876 | `"                \"مش بدور على\", \"مش عايز اشتري\", \"مش عاوز اشتري\","` | — |
| [SRC-1AE03B9EC3-L000877](../../agents/web_agent.py#L877) | 877 | `"                \"لا اريد شراء\", \"لا ارغب في شراء\", \"مش محتاج اشتري\","` | — |
| [SRC-1AE03B9EC3-L000878](../../agents/web_agent.py#L878) | 878 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000879](../../agents/web_agent.py#L879) | 879 | `"            if any(_normalize_search_query(term).casefold() in normalized for term in negations):"` | — |
| [SRC-1AE03B9EC3-L000880](../../agents/web_agent.py#L880) | 880 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L000881](../../agents/web_agent.py#L881) | 881 | `"            for phrase in phrases:"` | — |
| [SRC-1AE03B9EC3-L000882](../../agents/web_agent.py#L882) | 882 | `"                needle = _normalize_search_query(phrase).casefold()"` | — |
| [SRC-1AE03B9EC3-L000883](../../agents/web_agent.py#L883) | 883 | `"                if needle and needle in normalized:"` | — |
| [SRC-1AE03B9EC3-L000884](../../agents/web_agent.py#L884) | 884 | `"                    return {\"phrase\": phrase, \"basis\": basis}"` | — |
| [SRC-1AE03B9EC3-L000885](../../agents/web_agent.py#L885) | 885 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000886](../../agents/web_agent.py#L886) | 886 | `""` | — |
| [SRC-1AE03B9EC3-L000887](../../agents/web_agent.py#L887) | 887 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000888](../../agents/web_agent.py#L888) | 888 | `"    def _lead_generation_queries("` | — |
| [SRC-1AE03B9EC3-L000889](../../agents/web_agent.py#L889) | 889 | `"        question: str, existing_queries: list[str] \| None = None"` | — |
| [SRC-1AE03B9EC3-L000890](../../agents/web_agent.py#L890) | 890 | `"    ) -> list[str]:"` | — |
| [SRC-1AE03B9EC3-L000891](../../agents/web_agent.py#L891) | 891 | `"        \"\"\"Create high-intent buyer-search variants without changing the product/location.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000892](../../agents/web_agent.py#L892) | 892 | `"        subject = _normalize_search_query(question).strip()"` | — |
| [SRC-1AE03B9EC3-L000893](../../agents/web_agent.py#L893) | 893 | `"        subject = re.sub("` | — |
| [SRC-1AE03B9EC3-L000894](../../agents/web_agent.py#L894) | 894 | `"            r\"^(?:(?:من فضلك\|لو سمحت)\\s*)?(?:ابحث\|بحث\|دور\|دورلي\|اعثر)\\s+\""` | — |
| [SRC-1AE03B9EC3-L000895](../../agents/web_agent.py#L895) | 895 | `"            r\"(?:عن\|على)\\s+(?:عميل(?:\\s+محتمل)?\|عملاء(?:\\s+محتملين)?\|\""` | — |
| [SRC-1AE03B9EC3-L000896](../../agents/web_agent.py#L896) | 896 | `"            r\"مشتري(?:ن)?\|مشترين)\\s*(?:(?:الذي\|اللي\|الذين)\\s*)?\""` | — |
| [SRC-1AE03B9EC3-L000897](../../agents/web_agent.py#L897) | 897 | `"            r\"(?:(?:يريد\|عايز\|عاوز)\\s*(?:ان\\s*)?(?:يشتري\|شراء))?\\s*\","` | — |
| [SRC-1AE03B9EC3-L000898](../../agents/web_agent.py#L898) | 898 | `"            \"\", subject, flags=re.IGNORECASE,"` | — |
| [SRC-1AE03B9EC3-L000899](../../agents/web_agent.py#L899) | 899 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000900](../../agents/web_agent.py#L900) | 900 | `"        subject = re.sub("` | — |
| [SRC-1AE03B9EC3-L000901](../../agents/web_agent.py#L901) | 901 | `"            r\"^(?:please\\s+)?(?:find\|search for\|look for)\\s+(?:(?:a\|an)\\s+)?\""` | — |
| [SRC-1AE03B9EC3-L000902](../../agents/web_agent.py#L902) | 902 | `"            r\"(?:(?:potential\\s+)?(?:customer\|buyer\|prospect\|lead)s?)\\s*\""` | — |
| [SRC-1AE03B9EC3-L000903](../../agents/web_agent.py#L903) | 903 | `"            r\"(?:(?:who\|that)\\s*)?(?:(?:wants?\|looking to\|seeking to)\\s+\""` | — |
| [SRC-1AE03B9EC3-L000904](../../agents/web_agent.py#L904) | 904 | `"            r\"(?:buy\|purchase)\\s*)?\","` | — |
| [SRC-1AE03B9EC3-L000905](../../agents/web_agent.py#L905) | 905 | `"            \"\", subject, flags=re.IGNORECASE,"` | — |
| [SRC-1AE03B9EC3-L000906](../../agents/web_agent.py#L906) | 906 | `"        ).strip(\" \\t:;,.-\")"` | — |
| [SRC-1AE03B9EC3-L000907](../../agents/web_agent.py#L907) | 907 | `"        if len(_search_tokens(subject)) < 2:"` | — |
| [SRC-1AE03B9EC3-L000908](../../agents/web_agent.py#L908) | 908 | `"            subject = _normalize_search_query(question).strip()"` | — |
| [SRC-1AE03B9EC3-L000909](../../agents/web_agent.py#L909) | 909 | `"        arabic = bool(re.search(r\"[\\u0600-\\u06FF]\", question))"` | — |
| [SRC-1AE03B9EC3-L000910](../../agents/web_agent.py#L910) | 910 | `"        if arabic:"` | — |
| [SRC-1AE03B9EC3-L000911](../../agents/web_agent.py#L911) | 911 | `"            targeted = ["` | — |
| [SRC-1AE03B9EC3-L000912](../../agents/web_agent.py#L912) | 912 | `"                f'\"مطلوب شراء\" {subject}',"` | — |
| [SRC-1AE03B9EC3-L000913](../../agents/web_agent.py#L913) | 913 | `"                f'\"مطلوب شقه تمليك\" {subject}',"` | — |
| [SRC-1AE03B9EC3-L000914](../../agents/web_agent.py#L914) | 914 | `"                f'\"بدور على\" {subject} تمليك',"` | — |
| [SRC-1AE03B9EC3-L000915](../../agents/web_agent.py#L915) | 915 | `"                f'\"عايز اشتري\" {subject}',"` | — |
| [SRC-1AE03B9EC3-L000916](../../agents/web_agent.py#L916) | 916 | `"                f'site:facebook.com/groups \"{subject}\" (\"مطلوب\" OR \"تمليك\")',"` | — |
| [SRC-1AE03B9EC3-L000917](../../agents/web_agent.py#L917) | 917 | `"                f'site:linkedin.com/posts \"{subject}\" (\"looking to buy\" OR \"purchase\")',"` | — |
| [SRC-1AE03B9EC3-L000918](../../agents/web_agent.py#L918) | 918 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L000919](../../agents/web_agent.py#L919) | 919 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L000920](../../agents/web_agent.py#L920) | 920 | `"            targeted = ["` | — |
| [SRC-1AE03B9EC3-L000921](../../agents/web_agent.py#L921) | 921 | `"                f'\"looking to buy\" {subject}',"` | — |
| [SRC-1AE03B9EC3-L000922](../../agents/web_agent.py#L922) | 922 | `"                f'\"want to purchase\" {subject}',"` | — |
| [SRC-1AE03B9EC3-L000923](../../agents/web_agent.py#L923) | 923 | `"                f'site:linkedin.com/posts \"{subject}\" (\"looking to buy\" OR \"purchase\")',"` | — |
| [SRC-1AE03B9EC3-L000924](../../agents/web_agent.py#L924) | 924 | `"                f'site:facebook.com/groups \"{subject}\" (\"looking for\" OR \"want to buy\")',"` | — |
| [SRC-1AE03B9EC3-L000925](../../agents/web_agent.py#L925) | 925 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L000926](../../agents/web_agent.py#L926) | 926 | `"        candidates = targeted + [_normalize_search_query(q) for q in (existing_queries or [])]"` | — |
| [SRC-1AE03B9EC3-L000927](../../agents/web_agent.py#L927) | 927 | `"        return list(dict.fromkeys(q[:500] for q in candidates if q and q.strip()))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L000928](../../agents/web_agent.py#L928) | 928 | `""` | — |
| [SRC-1AE03B9EC3-L000929](../../agents/web_agent.py#L929) | 929 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000930](../../agents/web_agent.py#L930) | 930 | `"    def _is_listing_discovery(question: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000931](../../agents/web_agent.py#L931) | 931 | `"        \"\"\"Recognize property/job/product discovery where candidates are useful with caveats.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000932](../../agents/web_agent.py#L932) | 932 | `"        value = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L000933](../../agents/web_agent.py#L933) | 933 | `"        entities = ("` | — |
| [SRC-1AE03B9EC3-L000934](../../agents/web_agent.py#L934) | 934 | `"            \"شقه\", \"شقق\", \"عقار\", \"عقارات\", \"فيلا\", \"فلل\", \"وحده سكنيه\","` | — |
| [SRC-1AE03B9EC3-L000935](../../agents/web_agent.py#L935) | 935 | `"            \"وحدات سكنيه\", \"apartment\", \"apartments\", \"flat\", \"property listing\","` | — |
| [SRC-1AE03B9EC3-L000936](../../agents/web_agent.py#L936) | 936 | `"            \"real estate\", \"house\", \"villa\", \"job opening\", \"وظيفه\", \"وظائف\","` | — |
| [SRC-1AE03B9EC3-L000937](../../agents/web_agent.py#L937) | 937 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000938](../../agents/web_agent.py#L938) | 938 | `"        actions = ("` | — |
| [SRC-1AE03B9EC3-L000939](../../agents/web_agent.py#L939) | 939 | `"            \"ابحث\", \"دور\", \"هات\", \"عايز\", \"عاوز\", \"محتاج\", \"بدور\", \"للبيع\","` | — |
| [SRC-1AE03B9EC3-L000940](../../agents/web_agent.py#L940) | 940 | `"            \"للايجار\", \"ايجار\", \"معاينه\", \"اعلان\", \"اعلانات\", \"find\", \"search\","` | — |
| [SRC-1AE03B9EC3-L000941](../../agents/web_agent.py#L941) | 941 | `"            \"looking for\", \"for sale\", \"for rent\","` | — |
| [SRC-1AE03B9EC3-L000942](../../agents/web_agent.py#L942) | 942 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000943](../../agents/web_agent.py#L943) | 943 | `"        normalized_entities = (_normalize_search_query(term).casefold() for term in entities)"` | — |
| [SRC-1AE03B9EC3-L000944](../../agents/web_agent.py#L944) | 944 | `"        normalized_actions = (_normalize_search_query(term).casefold() for term in actions)"` | — |
| [SRC-1AE03B9EC3-L000945](../../agents/web_agent.py#L945) | 945 | `"        return any(term in value for term in normalized_entities) and any("` | — |
| [SRC-1AE03B9EC3-L000946](../../agents/web_agent.py#L946) | 946 | `"            term in value for term in normalized_actions"` | — |
| [SRC-1AE03B9EC3-L000947](../../agents/web_agent.py#L947) | 947 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000948](../../agents/web_agent.py#L948) | 948 | `""` | — |
| [SRC-1AE03B9EC3-L000949](../../agents/web_agent.py#L949) | 949 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000950](../../agents/web_agent.py#L950) | 950 | `"    def _requires_web_research(question: str, mode: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000951](../../agents/web_agent.py#L951) | 951 | `"        \"\"\"Use the web only when the user requests it or the answer depends on live data.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000952](../../agents/web_agent.py#L952) | 952 | `"        # A question about whether the current answer already searched is a"` | — |
| [SRC-1AE03B9EC3-L000953](../../agents/web_agent.py#L953) | 953 | `"        # status query, not a request to launch fresh research in any UI mode."` | — |
| [SRC-1AE03B9EC3-L000954](../../agents/web_agent.py#L954) | 954 | `"        if WebAgent._is_current_search_status_question(question):"` | — |
| [SRC-1AE03B9EC3-L000955](../../agents/web_agent.py#L955) | 955 | `"            return False"` | — |
| [SRC-1AE03B9EC3-L000956](../../agents/web_agent.py#L956) | 956 | `"        if mode != \"auto\":"` | — |
| [SRC-1AE03B9EC3-L000957](../../agents/web_agent.py#L957) | 957 | `"            return True"` | — |
| [SRC-1AE03B9EC3-L000958](../../agents/web_agent.py#L958) | 958 | `"        value = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L000959](../../agents/web_agent.py#L959) | 959 | `"        dynamic_terms = ("` | — |
| [SRC-1AE03B9EC3-L000960](../../agents/web_agent.py#L960) | 960 | `"            \"ابحث\", \"بحث عن\", \"دور على\", \"دورلي\", \"هات رابط\", \"هاتلي\","` | — |
| [SRC-1AE03B9EC3-L000961](../../agents/web_agent.py#L961) | 961 | `"            \"جيبلي\", \"اعثر على\", \"موقع\", \"رابط\", \"لينك\", \"اخبار\", \"اخر\","` | — |
| [SRC-1AE03B9EC3-L000962](../../agents/web_agent.py#L962) | 962 | `"            \"احدث\", \"اليوم\", \"دلوقتي\", \"حاليا\", \"سعر\", \"اسعار\", \"للبيع\","` | — |
| [SRC-1AE03B9EC3-L000963](../../agents/web_agent.py#L963) | 963 | `"            \"للايجار\", \"ايجار\", \"معاينه\", \"عميل محتمل\", \"عملاء محتملين\","` | — |
| [SRC-1AE03B9EC3-L000964](../../agents/web_agent.py#L964) | 964 | `"            \"وظائف\", \"وظيفه\", \"حجز\", \"موعد\", \"الطقس\", \"سهم\", \"سعر الصرف\","` | — |
| [SRC-1AE03B9EC3-L000965](../../agents/web_agent.py#L965) | 965 | `"            \"search\", \"find\", \"look up\", \"latest\", \"today\", \"current\","` | — |
| [SRC-1AE03B9EC3-L000966](../../agents/web_agent.py#L966) | 966 | `"            \"news\", \"price\", \"for sale\", \"for rent\", \"real estate\", \"job opening\","` | — |
| [SRC-1AE03B9EC3-L000967](../../agents/web_agent.py#L967) | 967 | `"            \"appointment\", \"reservation\", \"weather\", \"stock price\", \"exchange rate\","` | — |
| [SRC-1AE03B9EC3-L000968](../../agents/web_agent.py#L968) | 968 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000969](../../agents/web_agent.py#L969) | 969 | `"        return any(term in value for term in dynamic_terms) or bool("` | — |
| [SRC-1AE03B9EC3-L000970](../../agents/web_agent.py#L970) | 970 | `"            re.search(r\"https?://\", question, flags=re.IGNORECASE)"` | — |
| [SRC-1AE03B9EC3-L000971](../../agents/web_agent.py#L971) | 971 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000972](../../agents/web_agent.py#L972) | 972 | `""` | — |
| [SRC-1AE03B9EC3-L000973](../../agents/web_agent.py#L973) | 973 | `"    def _local_answer_result(self, question: str, answer: str, kind: str) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L000974](../../agents/web_agent.py#L974) | 974 | `"        \"\"\"Build a consistently shaped answer for non-research conversational requests.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000975](../../agents/web_agent.py#L975) | 975 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L000976](../../agents/web_agent.py#L976) | 976 | `"            \"answer\": answer,"` | — |
| [SRC-1AE03B9EC3-L000977](../../agents/web_agent.py#L977) | 977 | `"            \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L000978](../../agents/web_agent.py#L978) | 978 | `"            \"search_query\": question,"` | — |
| [SRC-1AE03B9EC3-L000979](../../agents/web_agent.py#L979) | 979 | `"            \"search_queries\": [],"` | — |
| [SRC-1AE03B9EC3-L000980](../../agents/web_agent.py#L980) | 980 | `"            \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L000981](../../agents/web_agent.py#L981) | 981 | `"                \"mode\": \"auto\","` | — |
| [SRC-1AE03B9EC3-L000982](../../agents/web_agent.py#L982) | 982 | `"                \"planning_method\": \"local_capability_router\","` | — |
| [SRC-1AE03B9EC3-L000983](../../agents/web_agent.py#L983) | 983 | `"                \"web_search_skipped\": True,"` | — |
| [SRC-1AE03B9EC3-L000984](../../agents/web_agent.py#L984) | 984 | `"            },"` | — |
| [SRC-1AE03B9EC3-L000985](../../agents/web_agent.py#L985) | 985 | `"            \"sources\": [],"` | — |
| [SRC-1AE03B9EC3-L000986](../../agents/web_agent.py#L986) | 986 | `"            \"used_language_model\": False,"` | — |
| [SRC-1AE03B9EC3-L000987](../../agents/web_agent.py#L987) | 987 | `"            \"used_web_search\": False,"` | — |
| [SRC-1AE03B9EC3-L000988](../../agents/web_agent.py#L988) | 988 | `"            \"search_attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L000989](../../agents/web_agent.py#L989) | 989 | `"            \"used_social_search\": False,"` | — |
| [SRC-1AE03B9EC3-L000990](../../agents/web_agent.py#L990) | 990 | `"            \"warnings\": [],"` | — |
| [SRC-1AE03B9EC3-L000991](../../agents/web_agent.py#L991) | 991 | `"            \"kind\": kind,"` | — |
| [SRC-1AE03B9EC3-L000992](../../agents/web_agent.py#L992) | 992 | `"            \"research_quality\": \"not_applicable\","` | — |
| [SRC-1AE03B9EC3-L000993](../../agents/web_agent.py#L993) | 993 | `"        }"` | — |
| [SRC-1AE03B9EC3-L000994](../../agents/web_agent.py#L994) | 994 | `""` | — |
| [SRC-1AE03B9EC3-L000995](../../agents/web_agent.py#L995) | 995 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000996](../../agents/web_agent.py#L996) | 996 | `"    def _local_conversation_reply(question: str) -> str:"` | — |
| [SRC-1AE03B9EC3-L000997](../../agents/web_agent.py#L997) | 997 | `"        \"\"\"Return a short greeting/acknowledgment without a model or web request.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000998](../../agents/web_agent.py#L998) | 998 | `"        value = _normalize_search_query(question).casefold().strip(\" \\t\\r\\n؟?!.,،؛;\")"` | — |
| [SRC-1AE03B9EC3-L000999](../../agents/web_agent.py#L999) | 999 | `"        if \"السلام عليكم\" in value:"` | — |
| [SRC-1AE03B9EC3-L001000](../../agents/web_agent.py#L1000) | 1000 | `"            return \"وعليكم السلام ورحمة الله وبركاته. أنا معاك؛ أقدر أساعدك في إيه؟\""` | — |
| [SRC-1AE03B9EC3-L001001](../../agents/web_agent.py#L1001) | 1001 | `"        if any(term in value for term in (\"شكرا\", \"متشكر\", \"متشكره\", \"العفو\")):"` | — |
| [SRC-1AE03B9EC3-L001002](../../agents/web_agent.py#L1002) | 1002 | `"            return \"العفو، تحت أمرك.\""` | — |
| [SRC-1AE03B9EC3-L001003](../../agents/web_agent.py#L1003) | 1003 | `"        if re.search(r\"[a-z]\", value):"` | — |
| [SRC-1AE03B9EC3-L001004](../../agents/web_agent.py#L1004) | 1004 | `"            if any(term in value for term in (\"thanks\", \"thank you\", \"got it\")):"` | — |
| [SRC-1AE03B9EC3-L001005](../../agents/web_agent.py#L1005) | 1005 | `"                return \"You're welcome—glad it helped.\""` | — |
| [SRC-1AE03B9EC3-L001006](../../agents/web_agent.py#L1006) | 1006 | `"            return \"Hi! I'm here and ready to help. What would you like to work on?\""` | — |
| [SRC-1AE03B9EC3-L001007](../../agents/web_agent.py#L1007) | 1007 | `"        return \"أهلًا! أنا معاك. أقدر أساعدك في إيه؟\""` | — |
| [SRC-1AE03B9EC3-L001008](../../agents/web_agent.py#L1008) | 1008 | `""` | — |
| [SRC-1AE03B9EC3-L001009](../../agents/web_agent.py#L1009) | 1009 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L001010](../../agents/web_agent.py#L1010) | 1010 | `"    def _annotate_intent_route("` | — |
| [SRC-1AE03B9EC3-L001011](../../agents/web_agent.py#L1011) | 1011 | `"        result: dict[str, Any], route: str, reason: str, mode: str = \"auto\""` | — |
| [SRC-1AE03B9EC3-L001012](../../agents/web_agent.py#L1012) | 1012 | `"    ) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L001013](../../agents/web_agent.py#L1013) | 1013 | `"        \"\"\"Attach route diagnostics to both response and research-plan metadata.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001014](../../agents/web_agent.py#L1014) | 1014 | `"        result[\"intent_route\"] = route"` | — |
| [SRC-1AE03B9EC3-L001015](../../agents/web_agent.py#L1015) | 1015 | `"        result[\"intent_route_reason\"] = reason"` | — |
| [SRC-1AE03B9EC3-L001016](../../agents/web_agent.py#L1016) | 1016 | `"        plan = result.get(\"research_plan\")"` | — |
| [SRC-1AE03B9EC3-L001017](../../agents/web_agent.py#L1017) | 1017 | `"        if not isinstance(plan, dict):"` | — |
| [SRC-1AE03B9EC3-L001018](../../agents/web_agent.py#L1018) | 1018 | `"            plan = {}"` | — |
| [SRC-1AE03B9EC3-L001019](../../agents/web_agent.py#L1019) | 1019 | `"            result[\"research_plan\"] = plan"` | — |
| [SRC-1AE03B9EC3-L001020](../../agents/web_agent.py#L1020) | 1020 | `"        plan[\"intent_route\"] = route"` | — |
| [SRC-1AE03B9EC3-L001021](../../agents/web_agent.py#L1021) | 1021 | `"        plan[\"intent_route_reason\"] = reason"` | — |
| [SRC-1AE03B9EC3-L001022](../../agents/web_agent.py#L1022) | 1022 | `"        plan[\"mode\"] = mode"` | — |
| [SRC-1AE03B9EC3-L001023](../../agents/web_agent.py#L1023) | 1023 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L001024](../../agents/web_agent.py#L1024) | 1024 | `""` | — |
| [SRC-1AE03B9EC3-L001025](../../agents/web_agent.py#L1025) | 1025 | `"    def _clarification_result("` | — |
| [SRC-1AE03B9EC3-L001026](../../agents/web_agent.py#L1026) | 1026 | `"        self, question: str, mode: str, decision: dict[str, Any]"` | — |
| [SRC-1AE03B9EC3-L001027](../../agents/web_agent.py#L1027) | 1027 | `"    ) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L001028](../../agents/web_agent.py#L1028) | 1028 | `"        \"\"\"Return a bounded clarification result without starting web search.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001029](../../agents/web_agent.py#L1029) | 1029 | `"        if re.search(r\"[a-z]\", question.casefold()):"` | — |
| [SRC-1AE03B9EC3-L001030](../../agents/web_agent.py#L1030) | 1030 | `"            answer = ("` | — |
| [SRC-1AE03B9EC3-L001031](../../agents/web_agent.py#L1031) | 1031 | `"                \"What are you referring to? Please name the item or share its link, \""` | — |
| [SRC-1AE03B9EC3-L001032](../../agents/web_agent.py#L1032) | 1032 | `"                \"and I'll continue without guessing.\""` | — |
| [SRC-1AE03B9EC3-L001033](../../agents/web_agent.py#L1033) | 1033 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001034](../../agents/web_agent.py#L1034) | 1034 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L001035](../../agents/web_agent.py#L1035) | 1035 | `"            answer = ("` | — |
| [SRC-1AE03B9EC3-L001036](../../agents/web_agent.py#L1036) | 1036 | `"                \"تقصد إيه تحديدًا؟ اكتب اسم الشيء أو المنتج المقصود، أو ابعت الرابط، \""` | — |
| [SRC-1AE03B9EC3-L001037](../../agents/web_agent.py#L1037) | 1037 | `"                \"وأكمل معاك من غير ما أخمّن.\""` | — |
| [SRC-1AE03B9EC3-L001038](../../agents/web_agent.py#L1038) | 1038 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001039](../../agents/web_agent.py#L1039) | 1039 | `"        result = self._local_answer_result(question, answer, \"clarification_needed\")"` | — |
| [SRC-1AE03B9EC3-L001040](../../agents/web_agent.py#L1040) | 1040 | `"        return self._annotate_intent_route("` | — |
| [SRC-1AE03B9EC3-L001041](../../agents/web_agent.py#L1041) | 1041 | `"            result, \"CLARIFY\", str(decision.get(\"reason\", \"missing_referent\")), mode"` | — |
| [SRC-1AE03B9EC3-L001042](../../agents/web_agent.py#L1042) | 1042 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001043](../../agents/web_agent.py#L1043) | 1043 | `""` | — |
| [SRC-1AE03B9EC3-L001044](../../agents/web_agent.py#L1044) | 1044 | `"    def _dialogue_clarification_result("` | — |
| [SRC-1AE03B9EC3-L001045](../../agents/web_agent.py#L1045) | 1045 | `"        self, question: str, mode: str, context: dict[str, Any], reason: str"` | — |
| [SRC-1AE03B9EC3-L001046](../../agents/web_agent.py#L1046) | 1046 | `"    ) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L001047](../../agents/web_agent.py#L1047) | 1047 | `"        \"\"\"Expose why context resolution stopped and ask instead of guessing.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001048](../../agents/web_agent.py#L1048) | 1048 | `"        context = dict(context)"` | — |
| [SRC-1AE03B9EC3-L001049](../../agents/web_agent.py#L1049) | 1049 | `"        context[\"needs_clarification\"] = True"` | — |
| [SRC-1AE03B9EC3-L001050](../../agents/web_agent.py#L1050) | 1050 | `"        context[\"status\"] = \"needs_clarification\""` | — |
| [SRC-1AE03B9EC3-L001051](../../agents/web_agent.py#L1051) | 1051 | `"        context[\"resolved_question\"] = question[:MAX_QUESTION_CHARS]"` | — |
| [SRC-1AE03B9EC3-L001052](../../agents/web_agent.py#L1052) | 1052 | `"        context[\"resolution_basis\"] = \"insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L001053](../../agents/web_agent.py#L1053) | 1053 | `"        result = self._clarification_result("` | — |
| [SRC-1AE03B9EC3-L001054](../../agents/web_agent.py#L1054) | 1054 | `"            question, mode, {"` | — |
| [SRC-1AE03B9EC3-L001055](../../agents/web_agent.py#L1055) | 1055 | `"                \"reason\": reason,"` | — |
| [SRC-1AE03B9EC3-L001056](../../agents/web_agent.py#L1056) | 1056 | `"                \"needs_clarification\": True,"` | — |
| [SRC-1AE03B9EC3-L001057](../../agents/web_agent.py#L1057) | 1057 | `"                \"context_available\": bool(context.get(\"is_follow_up\")),"` | — |
| [SRC-1AE03B9EC3-L001058](../../agents/web_agent.py#L1058) | 1058 | `"            }"` | — |
| [SRC-1AE03B9EC3-L001059](../../agents/web_agent.py#L1059) | 1059 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001060](../../agents/web_agent.py#L1060) | 1060 | `"        requested_clarification = context.get(\"clarification_question\")"` | — |
| [SRC-1AE03B9EC3-L001061](../../agents/web_agent.py#L1061) | 1061 | `"        if isinstance(requested_clarification, str) and requested_clarification.strip():"` | — |
| [SRC-1AE03B9EC3-L001062](../../agents/web_agent.py#L1062) | 1062 | `"            result[\"answer\"] = requested_clarification[:400]"` | — |
| [SRC-1AE03B9EC3-L001063](../../agents/web_agent.py#L1063) | 1063 | `"        result[\"dialogue_context\"] = context"` | — |
| [SRC-1AE03B9EC3-L001064](../../agents/web_agent.py#L1064) | 1064 | `"        if isinstance(result.get(\"research_plan\"), dict):"` | — |
| [SRC-1AE03B9EC3-L001065](../../agents/web_agent.py#L1065) | 1065 | `"            result[\"research_plan\"][\"dialogue_context\"] = context"` | — |
| [SRC-1AE03B9EC3-L001066](../../agents/web_agent.py#L1066) | 1066 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L001067](../../agents/web_agent.py#L1067) | 1067 | `""` | — |
| [SRC-1AE03B9EC3-L001068](../../agents/web_agent.py#L1068) | 1068 | `"    def _capability_status_snapshot(self) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L001069](../../agents/web_agent.py#L1069) | 1069 | `"        \"\"\"Describe configured capabilities without claiming a live health check.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001070](../../agents/web_agent.py#L1070) | 1070 | `"        status = self.status()"` | — |
| [SRC-1AE03B9EC3-L001071](../../agents/web_agent.py#L1071) | 1071 | `"        not_tested = \"not_tested_in_this_response\""` | — |
| [SRC-1AE03B9EC3-L001072](../../agents/web_agent.py#L1072) | 1072 | `"        providers = ["` | — |
| [SRC-1AE03B9EC3-L001073](../../agents/web_agent.py#L1073) | 1073 | `"            {"` | — |
| [SRC-1AE03B9EC3-L001074](../../agents/web_agent.py#L1074) | 1074 | `"                \"name\": \"duckduckgo_html\","` | — |
| [SRC-1AE03B9EC3-L001075](../../agents/web_agent.py#L1075) | 1075 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L001076](../../agents/web_agent.py#L1076) | 1076 | `"                \"configuration_status\": \"built_in_no_api_key\","` | — |
| [SRC-1AE03B9EC3-L001077](../../agents/web_agent.py#L1077) | 1077 | `"                \"runtime_status\": not_tested,"` | — |
| [SRC-1AE03B9EC3-L001078](../../agents/web_agent.py#L1078) | 1078 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001079](../../agents/web_agent.py#L1079) | 1079 | `"            {"` | — |
| [SRC-1AE03B9EC3-L001080](../../agents/web_agent.py#L1080) | 1080 | `"                \"name\": \"bing_rss\","` | — |
| [SRC-1AE03B9EC3-L001081](../../agents/web_agent.py#L1081) | 1081 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L001082](../../agents/web_agent.py#L1082) | 1082 | `"                \"configuration_status\": \"built_in_no_api_key\","` | — |
| [SRC-1AE03B9EC3-L001083](../../agents/web_agent.py#L1083) | 1083 | `"                \"runtime_status\": not_tested,"` | — |
| [SRC-1AE03B9EC3-L001084](../../agents/web_agent.py#L1084) | 1084 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001085](../../agents/web_agent.py#L1085) | 1085 | `"            {"` | — |
| [SRC-1AE03B9EC3-L001086](../../agents/web_agent.py#L1086) | 1086 | `"                \"name\": \"google_news_rss\","` | — |
| [SRC-1AE03B9EC3-L001087](../../agents/web_agent.py#L1087) | 1087 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L001088](../../agents/web_agent.py#L1088) | 1088 | `"                \"configuration_status\": \"conditional_no_api_key\","` | — |
| [SRC-1AE03B9EC3-L001089](../../agents/web_agent.py#L1089) | 1089 | `"                \"runtime_status\": not_tested,"` | — |
| [SRC-1AE03B9EC3-L001090](../../agents/web_agent.py#L1090) | 1090 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001091](../../agents/web_agent.py#L1091) | 1091 | `"            {"` | — |
| [SRC-1AE03B9EC3-L001092](../../agents/web_agent.py#L1092) | 1092 | `"                \"name\": \"deepseek_search_api\","` | — |
| [SRC-1AE03B9EC3-L001093](../../agents/web_agent.py#L1093) | 1093 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L001094](../../agents/web_agent.py#L1094) | 1094 | `"                \"configuration_status\": ("` | — |
| [SRC-1AE03B9EC3-L001095](../../agents/web_agent.py#L1095) | 1095 | `"                    \"configured\" if status.get(\"deepseek_search_api_configured\")"` | — |
| [SRC-1AE03B9EC3-L001096](../../agents/web_agent.py#L1096) | 1096 | `"                    else \"not_configured\""` | — |
| [SRC-1AE03B9EC3-L001097](../../agents/web_agent.py#L1097) | 1097 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001098](../../agents/web_agent.py#L1098) | 1098 | `"                \"runtime_status\": not_tested if status.get(\"deepseek_search_api_configured\")"` | — |
| [SRC-1AE03B9EC3-L001099](../../agents/web_agent.py#L1099) | 1099 | `"                else \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L001100](../../agents/web_agent.py#L1100) | 1100 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001101](../../agents/web_agent.py#L1101) | 1101 | `"            {"` | — |
| [SRC-1AE03B9EC3-L001102](../../agents/web_agent.py#L1102) | 1102 | `"                \"name\": \"brave_search_api\","` | — |
| [SRC-1AE03B9EC3-L001103](../../agents/web_agent.py#L1103) | 1103 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L001104](../../agents/web_agent.py#L1104) | 1104 | `"                \"configuration_status\": ("` | — |
| [SRC-1AE03B9EC3-L001105](../../agents/web_agent.py#L1105) | 1105 | `"                    \"configured\" if status.get(\"brave_search_api_configured\")"` | — |
| [SRC-1AE03B9EC3-L001106](../../agents/web_agent.py#L1106) | 1106 | `"                    else \"not_configured\""` | — |
| [SRC-1AE03B9EC3-L001107](../../agents/web_agent.py#L1107) | 1107 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001108](../../agents/web_agent.py#L1108) | 1108 | `"                \"runtime_status\": not_tested if status.get(\"brave_search_api_configured\")"` | — |
| [SRC-1AE03B9EC3-L001109](../../agents/web_agent.py#L1109) | 1109 | `"                else \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L001110](../../agents/web_agent.py#L1110) | 1110 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001111](../../agents/web_agent.py#L1111) | 1111 | `"            {"` | — |
| [SRC-1AE03B9EC3-L001112](../../agents/web_agent.py#L1112) | 1112 | `"                \"name\": \"tavily_search_api\","` | — |
| [SRC-1AE03B9EC3-L001113](../../agents/web_agent.py#L1113) | 1113 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L001114](../../agents/web_agent.py#L1114) | 1114 | `"                \"configuration_status\": ("` | — |
| [SRC-1AE03B9EC3-L001115](../../agents/web_agent.py#L1115) | 1115 | `"                    \"configured\" if status.get(\"tavily_search_api_configured\")"` | — |
| [SRC-1AE03B9EC3-L001116](../../agents/web_agent.py#L1116) | 1116 | `"                    else \"not_configured\""` | — |
| [SRC-1AE03B9EC3-L001117](../../agents/web_agent.py#L1117) | 1117 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001118](../../agents/web_agent.py#L1118) | 1118 | `"                \"runtime_status\": not_tested if status.get(\"tavily_search_api_configured\")"` | — |
| [SRC-1AE03B9EC3-L001119](../../agents/web_agent.py#L1119) | 1119 | `"                else \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L001120](../../agents/web_agent.py#L1120) | 1120 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001121](../../agents/web_agent.py#L1121) | 1121 | `"            {"` | — |
| [SRC-1AE03B9EC3-L001122](../../agents/web_agent.py#L1122) | 1122 | `"                \"name\": \"openrouter_web_search\","` | — |
| [SRC-1AE03B9EC3-L001123](../../agents/web_agent.py#L1123) | 1123 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L001124](../../agents/web_agent.py#L1124) | 1124 | `"                \"configuration_status\": ("` | — |
| [SRC-1AE03B9EC3-L001125](../../agents/web_agent.py#L1125) | 1125 | `"                    \"enabled\" if status.get(\"openrouter_web_search_enabled\")"` | — |
| [SRC-1AE03B9EC3-L001126](../../agents/web_agent.py#L1126) | 1126 | `"                    else \"disabled\""` | — |
| [SRC-1AE03B9EC3-L001127](../../agents/web_agent.py#L1127) | 1127 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001128](../../agents/web_agent.py#L1128) | 1128 | `"                \"runtime_status\": not_tested if status.get(\"openrouter_web_search_enabled\")"` | — |
| [SRC-1AE03B9EC3-L001129](../../agents/web_agent.py#L1129) | 1129 | `"                else \"disabled\","` | — |
| [SRC-1AE03B9EC3-L001130](../../agents/web_agent.py#L1130) | 1130 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001131](../../agents/web_agent.py#L1131) | 1131 | `"        ]"` | — |
| [SRC-1AE03B9EC3-L001132](../../agents/web_agent.py#L1132) | 1132 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L001133](../../agents/web_agent.py#L1133) | 1133 | `"            \"web_search\": {"` | — |
| [SRC-1AE03B9EC3-L001134](../../agents/web_agent.py#L1134) | 1134 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L001135](../../agents/web_agent.py#L1135) | 1135 | `"                \"local_dependencies_ready\": bool(status.get(\"web_search_ready\")),"` | — |
| [SRC-1AE03B9EC3-L001136](../../agents/web_agent.py#L1136) | 1136 | `"                \"runtime_status\": not_tested,"` | — |
| [SRC-1AE03B9EC3-L001137](../../agents/web_agent.py#L1137) | 1137 | `"                \"providers\": providers,"` | — |
| [SRC-1AE03B9EC3-L001138](../../agents/web_agent.py#L1138) | 1138 | `"                \"semantics\": ("` | — |
| [SRC-1AE03B9EC3-L001139](../../agents/web_agent.py#L1139) | 1139 | `"                    \"Configuration and installed dependencies do not prove that a live \""` | — |
| [SRC-1AE03B9EC3-L001140](../../agents/web_agent.py#L1140) | 1140 | `"                    \"network request will succeed.\""` | — |
| [SRC-1AE03B9EC3-L001141](../../agents/web_agent.py#L1141) | 1141 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001142](../../agents/web_agent.py#L1142) | 1142 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001143](../../agents/web_agent.py#L1143) | 1143 | `"            \"language_model\": {"` | — |
| [SRC-1AE03B9EC3-L001144](../../agents/web_agent.py#L1144) | 1144 | `"                \"configured\": bool(status.get(\"language_model_configured\")),"` | — |
| [SRC-1AE03B9EC3-L001145](../../agents/web_agent.py#L1145) | 1145 | `"                \"runtime_status\": not_tested,"` | — |
| [SRC-1AE03B9EC3-L001146](../../agents/web_agent.py#L1146) | 1146 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001147](../../agents/web_agent.py#L1147) | 1147 | `"        }"` | — |
| [SRC-1AE03B9EC3-L001148](../../agents/web_agent.py#L1148) | 1148 | `""` | — |
| [SRC-1AE03B9EC3-L001149](../../agents/web_agent.py#L1149) | 1149 | `"    def _self_description_answer(self, question: str) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L001150](../../agents/web_agent.py#L1150) | 1150 | `"        \"\"\"Answer self/capability questions without inventing a live health result.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001151](../../agents/web_agent.py#L1151) | 1151 | `"        value = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L001152](../../agents/web_agent.py#L1152) | 1152 | `"        current_search_question = self._is_current_search_status_question(question)"` | — |
| [SRC-1AE03B9EC3-L001153](../../agents/web_agent.py#L1153) | 1153 | `""` | — |
| [SRC-1AE03B9EC3-L001154](../../agents/web_agent.py#L1154) | 1154 | `"        if current_search_question:"` | — |
| [SRC-1AE03B9EC3-L001155](../../agents/web_agent.py#L1155) | 1155 | `"            answer = ("` | — |
| [SRC-1AE03B9EC3-L001156](../../agents/web_agent.py#L1156) | 1156 | `"                \"لا، لم أنفّذ بحثًا حيًا للإجابة عن هذا السؤال تحديدًا؛ هذا السؤال عن \""` | — |
| [SRC-1AE03B9EC3-L001157](../../agents/web_agent.py#L1157) | 1157 | `"                \"طريقة عملي، ولذلك لم أبدأ بحث ويب في هذه الجولة. هذا لا يعني أن البحث \""` | — |
| [SRC-1AE03B9EC3-L001158](../../agents/web_agent.py#L1158) | 1158 | `"                \"غير متاح؛ عند تنفيذ طلب يحتاج إلى معلومات حديثة سأوضح هل جرت محاولة البحث، \""` | — |
| [SRC-1AE03B9EC3-L001159](../../agents/web_agent.py#L1159) | 1159 | `"                \"وما النتائج التي عادت، وما إذا اكتملت الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L001160](../../agents/web_agent.py#L1160) | 1160 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001161](../../agents/web_agent.py#L1161) | 1161 | `"            result = self._local_answer_result(question, answer, \"capability_answer\")"` | — |
| [SRC-1AE03B9EC3-L001162](../../agents/web_agent.py#L1162) | 1162 | `"            result[\"request_execution_status\"] = {"` | — |
| [SRC-1AE03B9EC3-L001163](../../agents/web_agent.py#L1163) | 1163 | `"                \"search_attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L001164](../../agents/web_agent.py#L1164) | 1164 | `"                \"search_outcome\": \"not_attempted\","` | — |
| [SRC-1AE03B9EC3-L001165](../../agents/web_agent.py#L1165) | 1165 | `"                \"semantics\": \"status_of_this_request_only\","` | — |
| [SRC-1AE03B9EC3-L001166](../../agents/web_agent.py#L1166) | 1166 | `"            }"` | — |
| [SRC-1AE03B9EC3-L001167](../../agents/web_agent.py#L1167) | 1167 | `"            result[\"capability_status\"] = self._capability_status_snapshot()"` | — |
| [SRC-1AE03B9EC3-L001168](../../agents/web_agent.py#L1168) | 1168 | `"            return result"` | — |
| [SRC-1AE03B9EC3-L001169](../../agents/web_agent.py#L1169) | 1169 | `""` | — |
| [SRC-1AE03B9EC3-L001170](../../agents/web_agent.py#L1170) | 1170 | `"        capability_phrases = ("` | — |
| [SRC-1AE03B9EC3-L001171](../../agents/web_agent.py#L1171) | 1171 | `"            \"كيف تستطيع مساعدتي\", \"ازاي تقدر تساعدني\", \"ازاي ممكن تساعدني\","` | — |
| [SRC-1AE03B9EC3-L001172](../../agents/web_agent.py#L1172) | 1172 | `"            \"ماذا تستطيع ان تفعل\", \"ما الذي تستطيع فعله\", \"ايه اللي تقدر تعمله\","` | — |
| [SRC-1AE03B9EC3-L001173](../../agents/web_agent.py#L1173) | 1173 | `"            \"what can you do\", \"how can you help me\","` | — |
| [SRC-1AE03B9EC3-L001174](../../agents/web_agent.py#L1174) | 1174 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001175](../../agents/web_agent.py#L1175) | 1175 | `"        if any(term in value for term in capability_phrases):"` | — |
| [SRC-1AE03B9EC3-L001176](../../agents/web_agent.py#L1176) | 1176 | `"            answer = ("` | — |
| [SRC-1AE03B9EC3-L001177](../../agents/web_agent.py#L1177) | 1177 | `"                \"أقدر أساعدك في شرح الأسئلة ووضع خطط عملية، كما يتضمن Omarai مسارًا \""` | — |
| [SRC-1AE03B9EC3-L001178](../../agents/web_agent.py#L1178) | 1178 | `"                \"للبحث في الويب عند الحاجة إلى معلومات حديثة أو روابط أو مقارنة خيارات. \""` | — |
| [SRC-1AE03B9EC3-L001179](../../agents/web_agent.py#L1179) | 1179 | `"                \"سأوضح في كل مهمة ما إذا نُفذ البحث فعلًا وما المصادر التي أمكن جمعها، \""` | — |
| [SRC-1AE03B9EC3-L001180](../../agents/web_agent.py#L1180) | 1180 | `"                \"وما الذي لم يمكن التحقق منه. قد تعمل بعض الموصلات الاختيارية فقط عند \""` | — |
| [SRC-1AE03B9EC3-L001181](../../agents/web_agent.py#L1181) | 1181 | `"                \"ضبط إعداداتها، ولا أضمن الوصول إلى كل موقع أو إلى المجموعات والمنشورات \""` | — |
| [SRC-1AE03B9EC3-L001182](../../agents/web_agent.py#L1182) | 1182 | `"                \"الخاصة. لم أجرِ اختبار اتصال حي في هذه الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L001183](../../agents/web_agent.py#L1183) | 1183 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001184](../../agents/web_agent.py#L1184) | 1184 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L001185](../../agents/web_agent.py#L1185) | 1185 | `"            status = self.status()"` | — |
| [SRC-1AE03B9EC3-L001186](../../agents/web_agent.py#L1186) | 1186 | `"            providers = [\"DuckDuckGo HTML\", \"Bing RSS\"]"` | — |
| [SRC-1AE03B9EC3-L001187](../../agents/web_agent.py#L1187) | 1187 | `"            providers.append(\"Google News RSS عند ملاءمة السؤال أو الحاجة إلى معلومات حديثة\")"` | — |
| [SRC-1AE03B9EC3-L001188](../../agents/web_agent.py#L1188) | 1188 | `"            if status.get(\"deepseek_search_api_configured\"):"` | — |
| [SRC-1AE03B9EC3-L001189](../../agents/web_agent.py#L1189) | 1189 | `"                providers.append("` | — |
| [SRC-1AE03B9EC3-L001190](../../agents/web_agent.py#L1190) | 1190 | `"                    \"DeepSeek Search API (مفتاحه مضبوط، لكنه غير مختبر في هذه الإجابة \""` | — |
| [SRC-1AE03B9EC3-L001191](../../agents/web_agent.py#L1191) | 1191 | `"                    \"وقد يستهلك استخدامًا مدفوعًا)\""` | — |
| [SRC-1AE03B9EC3-L001192](../../agents/web_agent.py#L1192) | 1192 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001193](../../agents/web_agent.py#L1193) | 1193 | `"            if status.get(\"brave_search_api_configured\"):"` | — |
| [SRC-1AE03B9EC3-L001194](../../agents/web_agent.py#L1194) | 1194 | `"                providers.append(\"Brave Search API (الإعداد موجود، وليس دليلًا على نجاح الاتصال)\")"` | — |
| [SRC-1AE03B9EC3-L001195](../../agents/web_agent.py#L1195) | 1195 | `"            if status.get(\"tavily_search_api_configured\"):"` | — |
| [SRC-1AE03B9EC3-L001196](../../agents/web_agent.py#L1196) | 1196 | `"                providers.append(\"Tavily Search API (الإعداد موجود، وليس دليلًا على نجاح الاتصال)\")"` | — |
| [SRC-1AE03B9EC3-L001197](../../agents/web_agent.py#L1197) | 1197 | `"            if status.get(\"openrouter_web_search_enabled\"):"` | — |
| [SRC-1AE03B9EC3-L001198](../../agents/web_agent.py#L1198) | 1198 | `"                providers.append(\"بحث OpenRouter المباشر (مفعّل بالإعداد، وقد يستهلك رصيدًا)\")"` | — |
| [SRC-1AE03B9EC3-L001199](../../agents/web_agent.py#L1199) | 1199 | `"            answer = ("` | — |
| [SRC-1AE03B9EC3-L001200](../../agents/web_agent.py#L1200) | 1200 | `"                \"بحسب الكود الحالي، يتضمن Omarai مسار بحث ويب يستخدم: \""` | — |
| [SRC-1AE03B9EC3-L001201](../../agents/web_agent.py#L1201) | 1201 | `"                + \"، \".join(providers)"` | — |
| [SRC-1AE03B9EC3-L001202](../../agents/web_agent.py#L1202) | 1202 | `"                + \". هذه قائمة بالموصلات المضمّنة أو المهيأة، وليست إثباتًا بأنها نجحت \""` | — |
| [SRC-1AE03B9EC3-L001203](../../agents/web_agent.py#L1203) | 1203 | `"                \"في هذه اللحظة. لم أنفّذ اختبار اتصال حي في هذه الإجابة، لذلك لا أستطيع \""` | — |
| [SRC-1AE03B9EC3-L001204](../../agents/web_agent.py#L1204) | 1204 | `"                \"تأكيد توافر الشبكة الآن. عند طلب بحث فعلي، ينبغي أن يوضح التقرير ما إذا \""` | — |
| [SRC-1AE03B9EC3-L001205](../../agents/web_agent.py#L1205) | 1205 | `"                \"بدأت المحاولة، وما الموصلات التي أعادت نتائج، وما الصفحات التي أمكن قراءة \""` | — |
| [SRC-1AE03B9EC3-L001206](../../agents/web_agent.py#L1206) | 1206 | `"                \"محتواها. لا يوجد وصول مضمون إلى كل الإنترنت أو إلى المحتوى الخاص.\""` | — |
| [SRC-1AE03B9EC3-L001207](../../agents/web_agent.py#L1207) | 1207 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001208](../../agents/web_agent.py#L1208) | 1208 | `"        result = self._local_answer_result(question, answer, \"capability_answer\")"` | — |
| [SRC-1AE03B9EC3-L001209](../../agents/web_agent.py#L1209) | 1209 | `"        result[\"capability_status\"] = self._capability_status_snapshot()"` | — |
| [SRC-1AE03B9EC3-L001210](../../agents/web_agent.py#L1210) | 1210 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L001211](../../agents/web_agent.py#L1211) | 1211 | `""` | — |
| [SRC-1AE03B9EC3-L001212](../../agents/web_agent.py#L1212) | 1212 | `"    def _answer_without_search("` | — |
| [SRC-1AE03B9EC3-L001213](../../agents/web_agent.py#L1213) | 1213 | `"        self, question: str, history: list[dict[str, str]]"` | — |
| [SRC-1AE03B9EC3-L001214](../../agents/web_agent.py#L1214) | 1214 | `"    ) -> dict[str, Any] \| None:"` | — |
| [SRC-1AE03B9EC3-L001215](../../agents/web_agent.py#L1215) | 1215 | `"        \"\"\"Answer stable informational questions with the configured LLM, without fake citations.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001216](../../agents/web_agent.py#L1216) | 1216 | `"        if not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L001217](../../agents/web_agent.py#L1217) | 1217 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L001218](../../agents/web_agent.py#L1218) | 1218 | `"        messages: list[dict[str, str]] = ["` | — |
| [SRC-1AE03B9EC3-L001219](../../agents/web_agent.py#L1219) | 1219 | `"            {"` | — |
| [SRC-1AE03B9EC3-L001220](../../agents/web_agent.py#L1220) | 1220 | `"                \"role\": \"system\","` | — |
| [SRC-1AE03B9EC3-L001221](../../agents/web_agent.py#L1221) | 1221 | `"                \"content\": ("` | — |
| [SRC-1AE03B9EC3-L001222](../../agents/web_agent.py#L1222) | 1222 | `"                    \"أنت Omarai، مساعد عربي عملي. أجب مباشرة وباللغة التي استخدمها الشخص، \""` | — |
| [SRC-1AE03B9EC3-L001223](../../agents/web_agent.py#L1223) | 1223 | `"                    \"وافهم المقصود حتى لو كان باللهجة المصرية أو به أخطاء كتابية. هذا المسار \""` | — |
| [SRC-1AE03B9EC3-L001224](../../agents/web_agent.py#L1224) | 1224 | `"                    \"للشرح والمعرفة العامة والأسئلة الحوارية غير المعتمدة على معلومات لحظية. \""` | — |
| [SRC-1AE03B9EC3-L001225](../../agents/web_agent.py#L1225) | 1225 | `"                    \"لا تستخدم أدوات الويب ولا تقل إنك بحثت أو تحققت من مصدر. لا تختلق أرقامًا \""` | — |
| [SRC-1AE03B9EC3-L001226](../../agents/web_agent.py#L1226) | 1226 | `"                    \"أو اقتباسات أو روابط. إذا كان جزء من السؤال يتطلب بيانات حديثة أو تحققًا \""` | — |
| [SRC-1AE03B9EC3-L001227](../../agents/web_agent.py#L1227) | 1227 | `"                    \"خارجيًا، صرّح بذلك بدل الجزم. وضّح عدم اليقين بإيجاز، وأعط إجابة مفيدة \""` | — |
| [SRC-1AE03B9EC3-L001228](../../agents/web_agent.py#L1228) | 1228 | `"                    \"من غير إطالة أو سلسلة تفكير داخلية.\""` | — |
| [SRC-1AE03B9EC3-L001229](../../agents/web_agent.py#L1229) | 1229 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001230](../../agents/web_agent.py#L1230) | 1230 | `"            }"` | — |
| [SRC-1AE03B9EC3-L001231](../../agents/web_agent.py#L1231) | 1231 | `"        ]"` | — |
| [SRC-1AE03B9EC3-L001232](../../agents/web_agent.py#L1232) | 1232 | `"        messages.extend(history[-MAX_HISTORY_ITEMS:])"` | — |
| [SRC-1AE03B9EC3-L001233](../../agents/web_agent.py#L1233) | 1233 | `"        messages.append({\"role\": \"user\", \"content\": question})"` | — |
| [SRC-1AE03B9EC3-L001234](../../agents/web_agent.py#L1234) | 1234 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L001235](../../agents/web_agent.py#L1235) | 1235 | `"            answer = self._request_completion("` | — |
| [SRC-1AE03B9EC3-L001236](../../agents/web_agent.py#L1236) | 1236 | `"                messages,"` | — |
| [SRC-1AE03B9EC3-L001237](../../agents/web_agent.py#L1237) | 1237 | `"                max_tokens=1500,"` | — |
| [SRC-1AE03B9EC3-L001238](../../agents/web_agent.py#L1238) | 1238 | `"                temperature=0.2,"` | — |
| [SRC-1AE03B9EC3-L001239](../../agents/web_agent.py#L1239) | 1239 | `"                timeout=self._effective_timeout(min(self.timeout, 28)),"` | — |
| [SRC-1AE03B9EC3-L001240](../../agents/web_agent.py#L1240) | 1240 | `"                model=self.answer_model,"` | — |
| [SRC-1AE03B9EC3-L001241](../../agents/web_agent.py#L1241) | 1241 | `"                enable_web_search=False,"` | — |
| [SRC-1AE03B9EC3-L001242](../../agents/web_agent.py#L1242) | 1242 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001243](../../agents/web_agent.py#L1243) | 1243 | `"        except (RuntimeError, AgentDependencyError):"` | — |
| [SRC-1AE03B9EC3-L001244](../../agents/web_agent.py#L1244) | 1244 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L001245](../../agents/web_agent.py#L1245) | 1245 | `"        # Never turn an overlong completion into a seemingly complete answer by slicing it."` | — |
| [SRC-1AE03B9EC3-L001246](../../agents/web_agent.py#L1246) | 1246 | `"        if len(answer) > 24_000:"` | — |
| [SRC-1AE03B9EC3-L001247](../../agents/web_agent.py#L1247) | 1247 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L001248](../../agents/web_agent.py#L1248) | 1248 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L001249](../../agents/web_agent.py#L1249) | 1249 | `"            \"answer\": answer,"` | — |
| [SRC-1AE03B9EC3-L001250](../../agents/web_agent.py#L1250) | 1250 | `"            \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L001251](../../agents/web_agent.py#L1251) | 1251 | `"            \"search_query\": question,"` | — |
| [SRC-1AE03B9EC3-L001252](../../agents/web_agent.py#L1252) | 1252 | `"            \"search_queries\": [],"` | — |
| [SRC-1AE03B9EC3-L001253](../../agents/web_agent.py#L1253) | 1253 | `"            \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L001254](../../agents/web_agent.py#L1254) | 1254 | `"                \"mode\": \"auto\","` | — |
| [SRC-1AE03B9EC3-L001255](../../agents/web_agent.py#L1255) | 1255 | `"                \"planning_method\": \"general_qa_without_web\","` | — |
| [SRC-1AE03B9EC3-L001256](../../agents/web_agent.py#L1256) | 1256 | `"                \"web_search_skipped\": True,"` | — |
| [SRC-1AE03B9EC3-L001257](../../agents/web_agent.py#L1257) | 1257 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001258](../../agents/web_agent.py#L1258) | 1258 | `"            \"sources\": [],"` | — |
| [SRC-1AE03B9EC3-L001259](../../agents/web_agent.py#L1259) | 1259 | `"            \"used_language_model\": True,"` | — |
| [SRC-1AE03B9EC3-L001260](../../agents/web_agent.py#L1260) | 1260 | `"            \"used_web_search\": False,"` | — |
| [SRC-1AE03B9EC3-L001261](../../agents/web_agent.py#L1261) | 1261 | `"            \"search_attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L001262](../../agents/web_agent.py#L1262) | 1262 | `"            \"used_social_search\": False,"` | — |
| [SRC-1AE03B9EC3-L001263](../../agents/web_agent.py#L1263) | 1263 | `"            \"warnings\": [],"` | — |
| [SRC-1AE03B9EC3-L001264](../../agents/web_agent.py#L1264) | 1264 | `"            \"kind\": \"general_answer\","` | — |
| [SRC-1AE03B9EC3-L001265](../../agents/web_agent.py#L1265) | 1265 | `"            \"research_quality\": \"not_applicable\","` | — |
| [SRC-1AE03B9EC3-L001266](../../agents/web_agent.py#L1266) | 1266 | `"            \"model_calls\": list(self.model_usage),"` | — |
| [SRC-1AE03B9EC3-L001267](../../agents/web_agent.py#L1267) | 1267 | `"        }"` | — |
| [SRC-1AE03B9EC3-L001268](../../agents/web_agent.py#L1268) | 1268 | `""` | — |
| [SRC-1AE03B9EC3-L001269](../../agents/web_agent.py#L1269) | 1269 | `"    def _search_duckduckgo_html(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001270](../../agents/web_agent.py#L1270) | 1270 | `"        import httpx"` | — |
| [SRC-1AE03B9EC3-L001271](../../agents/web_agent.py#L1271) | 1271 | `"        from bs4 import BeautifulSoup"` | — |
| [SRC-1AE03B9EC3-L001272](../../agents/web_agent.py#L1272) | 1272 | `""` | — |
| [SRC-1AE03B9EC3-L001273](../../agents/web_agent.py#L1273) | 1273 | `"        response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001274](../../agents/web_agent.py#L1274) | 1274 | `"            \"https://html.duckduckgo.com/html/\","` | — |
| [SRC-1AE03B9EC3-L001275](../../agents/web_agent.py#L1275) | 1275 | `"            params={\"q\": query},"` | — |
| [SRC-1AE03B9EC3-L001276](../../agents/web_agent.py#L1276) | 1276 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L001277](../../agents/web_agent.py#L1277) | 1277 | `"                \"User-Agent\": ("` | — |
| [SRC-1AE03B9EC3-L001278](../../agents/web_agent.py#L1278) | 1278 | `"                    \"Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 \""` | — |
| [SRC-1AE03B9EC3-L001279](../../agents/web_agent.py#L1279) | 1279 | `"                    \"(KHTML, like Gecko) Chrome/124.0 Mobile Safari/537.36\""` | — |
| [SRC-1AE03B9EC3-L001280](../../agents/web_agent.py#L1280) | 1280 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001281](../../agents/web_agent.py#L1281) | 1281 | `"                \"Accept-Language\": \"ar,en;q=0.9\","` | — |
| [SRC-1AE03B9EC3-L001282](../../agents/web_agent.py#L1282) | 1282 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001283](../../agents/web_agent.py#L1283) | 1283 | `"            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001284](../../agents/web_agent.py#L1284) | 1284 | `"            # Search provider redirects are not followed automatically. A 3xx is"` | — |
| [SRC-1AE03B9EC3-L001285](../../agents/web_agent.py#L1285) | 1285 | `"            # reported as a provider failure so the host never fetches an unchecked target."` | — |
| [SRC-1AE03B9EC3-L001286](../../agents/web_agent.py#L1286) | 1286 | `"            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001287](../../agents/web_agent.py#L1287) | 1287 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001288](../../agents/web_agent.py#L1288) | 1288 | `"        if response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L001289](../../agents/web_agent.py#L1289) | 1289 | `"            raise RuntimeError(f\"HTTP {response.status_code}\")"` | — |
| [SRC-1AE03B9EC3-L001290](../../agents/web_agent.py#L1290) | 1290 | `"        soup = BeautifulSoup(response.text, \"html.parser\")"` | — |
| [SRC-1AE03B9EC3-L001291](../../agents/web_agent.py#L1291) | 1291 | `"        if soup.select_one(\"form#challenge-form, #challenge-form, .anomaly-modal\"):"` | — |
| [SRC-1AE03B9EC3-L001292](../../agents/web_agent.py#L1292) | 1292 | `"            raise RuntimeError(\"anti-bot challenge returned\")"` | — |
| [SRC-1AE03B9EC3-L001293](../../agents/web_agent.py#L1293) | 1293 | `"        rows: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001294](../../agents/web_agent.py#L1294) | 1294 | `"        for card in soup.select(\"div.result\"):"` | — |
| [SRC-1AE03B9EC3-L001295](../../agents/web_agent.py#L1295) | 1295 | `"            link = card.select_one(\"a.result__a\")"` | — |
| [SRC-1AE03B9EC3-L001296](../../agents/web_agent.py#L1296) | 1296 | `"            if not link:"` | — |
| [SRC-1AE03B9EC3-L001297](../../agents/web_agent.py#L1297) | 1297 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001298](../../agents/web_agent.py#L1298) | 1298 | `"            url = _public_http_url(self._unwrap_search_url(str(link.get(\"href\", \"\"))))"` | — |
| [SRC-1AE03B9EC3-L001299](../../agents/web_agent.py#L1299) | 1299 | `"            if not url:"` | — |
| [SRC-1AE03B9EC3-L001300](../../agents/web_agent.py#L1300) | 1300 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001301](../../agents/web_agent.py#L1301) | 1301 | `"            snippet_node = card.select_one(\".result__snippet\")"` | — |
| [SRC-1AE03B9EC3-L001302](../../agents/web_agent.py#L1302) | 1302 | `"            rows.append({"` | — |
| [SRC-1AE03B9EC3-L001303](../../agents/web_agent.py#L1303) | 1303 | `"                \"title\": _clean_text(link.get_text(\" \", strip=True), 300),"` | — |
| [SRC-1AE03B9EC3-L001304](../../agents/web_agent.py#L1304) | 1304 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001305](../../agents/web_agent.py#L1305) | 1305 | `"                \"snippet\": _clean_text("` | — |
| [SRC-1AE03B9EC3-L001306](../../agents/web_agent.py#L1306) | 1306 | `"                    snippet_node.get_text(\" \", strip=True) if snippet_node else \"\", 1200"` | — |
| [SRC-1AE03B9EC3-L001307](../../agents/web_agent.py#L1307) | 1307 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001308](../../agents/web_agent.py#L1308) | 1308 | `"                \"provider\": \"duckduckgo_html\","` | — |
| [SRC-1AE03B9EC3-L001309](../../agents/web_agent.py#L1309) | 1309 | `"                \"provider_rank\": len(rows) + 1,"` | — |
| [SRC-1AE03B9EC3-L001310](../../agents/web_agent.py#L1310) | 1310 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001311](../../agents/web_agent.py#L1311) | 1311 | `"                \"published_at\": \"\","` | — |
| [SRC-1AE03B9EC3-L001312](../../agents/web_agent.py#L1312) | 1312 | `"            })"` | — |
| [SRC-1AE03B9EC3-L001313](../../agents/web_agent.py#L1313) | 1313 | `"            if len(rows) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L001314](../../agents/web_agent.py#L1314) | 1314 | `"                break"` | — |
| [SRC-1AE03B9EC3-L001315](../../agents/web_agent.py#L1315) | 1315 | `"        if not rows and (\"captcha\" in response.text.casefold() or \"anomaly\" in response.text.casefold()):"` | — |
| [SRC-1AE03B9EC3-L001316](../../agents/web_agent.py#L1316) | 1316 | `"            raise RuntimeError(\"anti-bot challenge returned no result cards\")"` | — |
| [SRC-1AE03B9EC3-L001317](../../agents/web_agent.py#L1317) | 1317 | `"        return rows"` | — |
| [SRC-1AE03B9EC3-L001318](../../agents/web_agent.py#L1318) | 1318 | `""` | — |
| [SRC-1AE03B9EC3-L001319](../../agents/web_agent.py#L1319) | 1319 | `"    def _search_bing_rss(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001320](../../agents/web_agent.py#L1320) | 1320 | `"        import xml.etree.ElementTree as ET"` | — |
| [SRC-1AE03B9EC3-L001321](../../agents/web_agent.py#L1321) | 1321 | `""` | — |
| [SRC-1AE03B9EC3-L001322](../../agents/web_agent.py#L1322) | 1322 | `"        import httpx"` | — |
| [SRC-1AE03B9EC3-L001323](../../agents/web_agent.py#L1323) | 1323 | `""` | — |
| [SRC-1AE03B9EC3-L001324](../../agents/web_agent.py#L1324) | 1324 | `"        response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001325](../../agents/web_agent.py#L1325) | 1325 | `"            \"https://www.bing.com/search\","` | — |
| [SRC-1AE03B9EC3-L001326](../../agents/web_agent.py#L1326) | 1326 | `"            params={\"format\": \"rss\", \"q\": query},"` | — |
| [SRC-1AE03B9EC3-L001327](../../agents/web_agent.py#L1327) | 1327 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L001328](../../agents/web_agent.py#L1328) | 1328 | `"                \"User-Agent\": ("` | — |
| [SRC-1AE03B9EC3-L001329](../../agents/web_agent.py#L1329) | 1329 | `"                    \"Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 \""` | — |
| [SRC-1AE03B9EC3-L001330](../../agents/web_agent.py#L1330) | 1330 | `"                    \"(KHTML, like Gecko) Chrome/124.0 Mobile Safari/537.36\""` | — |
| [SRC-1AE03B9EC3-L001331](../../agents/web_agent.py#L1331) | 1331 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001332](../../agents/web_agent.py#L1332) | 1332 | `"                \"Accept-Language\": \"ar,en;q=0.9\","` | — |
| [SRC-1AE03B9EC3-L001333](../../agents/web_agent.py#L1333) | 1333 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001334](../../agents/web_agent.py#L1334) | 1334 | `"            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001335](../../agents/web_agent.py#L1335) | 1335 | `"            # Refuse automatic redirects from public search endpoints; never fetch an"` | — |
| [SRC-1AE03B9EC3-L001336](../../agents/web_agent.py#L1336) | 1336 | `"            # unchecked redirect target as part of a provider search request."` | — |
| [SRC-1AE03B9EC3-L001337](../../agents/web_agent.py#L1337) | 1337 | `"            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001338](../../agents/web_agent.py#L1338) | 1338 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001339](../../agents/web_agent.py#L1339) | 1339 | `"        if response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L001340](../../agents/web_agent.py#L1340) | 1340 | `"            raise RuntimeError(f\"HTTP {response.status_code}\")"` | — |
| [SRC-1AE03B9EC3-L001341](../../agents/web_agent.py#L1341) | 1341 | `"        root = ET.fromstring(response.content)"` | — |
| [SRC-1AE03B9EC3-L001342](../../agents/web_agent.py#L1342) | 1342 | `"        rows: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001343](../../agents/web_agent.py#L1343) | 1343 | `"        for item in root.iter():"` | — |
| [SRC-1AE03B9EC3-L001344](../../agents/web_agent.py#L1344) | 1344 | `"            if item.tag.rsplit(\"}\", 1)[-1] != \"item\":"` | — |
| [SRC-1AE03B9EC3-L001345](../../agents/web_agent.py#L1345) | 1345 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001346](../../agents/web_agent.py#L1346) | 1346 | `"            fields = {"` | — |
| [SRC-1AE03B9EC3-L001347](../../agents/web_agent.py#L1347) | 1347 | `"                child.tag.rsplit(\"}\", 1)[-1]: (child.text or \"\")"` | — |
| [SRC-1AE03B9EC3-L001348](../../agents/web_agent.py#L1348) | 1348 | `"                for child in item"` | — |
| [SRC-1AE03B9EC3-L001349](../../agents/web_agent.py#L1349) | 1349 | `"            }"` | — |
| [SRC-1AE03B9EC3-L001350](../../agents/web_agent.py#L1350) | 1350 | `"            url = _public_http_url(fields.get(\"link\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001351](../../agents/web_agent.py#L1351) | 1351 | `"            if not url:"` | — |
| [SRC-1AE03B9EC3-L001352](../../agents/web_agent.py#L1352) | 1352 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001353](../../agents/web_agent.py#L1353) | 1353 | `"            rows.append({"` | — |
| [SRC-1AE03B9EC3-L001354](../../agents/web_agent.py#L1354) | 1354 | `"                \"title\": _clean_text(fields.get(\"title\", \"\"), 300),"` | — |
| [SRC-1AE03B9EC3-L001355](../../agents/web_agent.py#L1355) | 1355 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001356](../../agents/web_agent.py#L1356) | 1356 | `"                \"snippet\": _clean_text(fields.get(\"description\", \"\"), 1200),"` | — |
| [SRC-1AE03B9EC3-L001357](../../agents/web_agent.py#L1357) | 1357 | `"                \"provider\": \"bing_rss\","` | — |
| [SRC-1AE03B9EC3-L001358](../../agents/web_agent.py#L1358) | 1358 | `"                \"provider_rank\": len(rows) + 1,"` | — |
| [SRC-1AE03B9EC3-L001359](../../agents/web_agent.py#L1359) | 1359 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001360](../../agents/web_agent.py#L1360) | 1360 | `"                \"published_at\": _clean_text(fields.get(\"pubDate\", \"\"), 80),"` | — |
| [SRC-1AE03B9EC3-L001361](../../agents/web_agent.py#L1361) | 1361 | `"            })"` | — |
| [SRC-1AE03B9EC3-L001362](../../agents/web_agent.py#L1362) | 1362 | `"            if len(rows) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L001363](../../agents/web_agent.py#L1363) | 1363 | `"                break"` | — |
| [SRC-1AE03B9EC3-L001364](../../agents/web_agent.py#L1364) | 1364 | `"        return rows"` | — |
| [SRC-1AE03B9EC3-L001365](../../agents/web_agent.py#L1365) | 1365 | `""` | — |
| [SRC-1AE03B9EC3-L001366](../../agents/web_agent.py#L1366) | 1366 | `"    def _search_deepseek_api(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001367](../../agents/web_agent.py#L1367) | 1367 | `"        \"\"\"Use DeepSeek's optional Search API as a comparison provider, never by default.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001368](../../agents/web_agent.py#L1368) | 1368 | `"        api_key = os.getenv(\"DEEPSEEK_SEARCH_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L001369](../../agents/web_agent.py#L1369) | 1369 | `"        if not api_key:"` | — |
| [SRC-1AE03B9EC3-L001370](../../agents/web_agent.py#L1370) | 1370 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L001371](../../agents/web_agent.py#L1371) | 1371 | `"        import httpx"` | — |
| [SRC-1AE03B9EC3-L001372](../../agents/web_agent.py#L1372) | 1372 | `""` | — |
| [SRC-1AE03B9EC3-L001373](../../agents/web_agent.py#L1373) | 1373 | `"        response = httpx.post("` | — |
| [SRC-1AE03B9EC3-L001374](../../agents/web_agent.py#L1374) | 1374 | `"            \"https://api.deepseek.com/v1/tools/search\","` | — |
| [SRC-1AE03B9EC3-L001375](../../agents/web_agent.py#L1375) | 1375 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L001376](../../agents/web_agent.py#L1376) | 1376 | `"                \"Authorization\": \"Bearer \" + api_key,"` | — |
| [SRC-1AE03B9EC3-L001377](../../agents/web_agent.py#L1377) | 1377 | `"                \"Content-Type\": \"application/json\","` | — |
| [SRC-1AE03B9EC3-L001378](../../agents/web_agent.py#L1378) | 1378 | `"                \"Accept\": \"application/json\","` | — |
| [SRC-1AE03B9EC3-L001379](../../agents/web_agent.py#L1379) | 1379 | `"                \"User-Agent\": \"OmaraiResearchAgent/1.0\","` | — |
| [SRC-1AE03B9EC3-L001380](../../agents/web_agent.py#L1380) | 1380 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001381](../../agents/web_agent.py#L1381) | 1381 | `"            json={"` | — |
| [SRC-1AE03B9EC3-L001382](../../agents/web_agent.py#L1382) | 1382 | `"                \"query\": _normalize_search_query(query)[:128] or \"public web search\","` | — |
| [SRC-1AE03B9EC3-L001383](../../agents/web_agent.py#L1383) | 1383 | `"                \"count\": min(MAX_PROVIDER_RESULTS, 10),"` | — |
| [SRC-1AE03B9EC3-L001384](../../agents/web_agent.py#L1384) | 1384 | `"                \"need_content\": False,"` | — |
| [SRC-1AE03B9EC3-L001385](../../agents/web_agent.py#L1385) | 1385 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001386](../../agents/web_agent.py#L1386) | 1386 | `"            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001387](../../agents/web_agent.py#L1387) | 1387 | `"            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001388](../../agents/web_agent.py#L1388) | 1388 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001389](../../agents/web_agent.py#L1389) | 1389 | `"        response.raise_for_status()"` | — |
| [SRC-1AE03B9EC3-L001390](../../agents/web_agent.py#L1390) | 1390 | `"        payload = response.json()"` | — |
| [SRC-1AE03B9EC3-L001391](../../agents/web_agent.py#L1391) | 1391 | `"        results = payload.get(\"results\", []) if isinstance(payload, dict) else []"` | — |
| [SRC-1AE03B9EC3-L001392](../../agents/web_agent.py#L1392) | 1392 | `"        rows: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001393](../../agents/web_agent.py#L1393) | 1393 | `"        for item in results if isinstance(results, list) else []:"` | — |
| [SRC-1AE03B9EC3-L001394](../../agents/web_agent.py#L1394) | 1394 | `"            if not isinstance(item, dict):"` | — |
| [SRC-1AE03B9EC3-L001395](../../agents/web_agent.py#L1395) | 1395 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001396](../../agents/web_agent.py#L1396) | 1396 | `"            url = _public_http_url(item.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001397](../../agents/web_agent.py#L1397) | 1397 | `"            if not url or _blocked_source_url(url):"` | — |
| [SRC-1AE03B9EC3-L001398](../../agents/web_agent.py#L1398) | 1398 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001399](../../agents/web_agent.py#L1399) | 1399 | `"            title = _clean_text(item.get(\"title\", \"\"), 300)"` | — |
| [SRC-1AE03B9EC3-L001400](../../agents/web_agent.py#L1400) | 1400 | `"            summary = item.get(\"summary\", \"\")"` | — |
| [SRC-1AE03B9EC3-L001401](../../agents/web_agent.py#L1401) | 1401 | `"            snippet = item.get(\"snippet\", \"\")"` | — |
| [SRC-1AE03B9EC3-L001402](../../agents/web_agent.py#L1402) | 1402 | `"            if isinstance(summary, str) and summary.strip():"` | — |
| [SRC-1AE03B9EC3-L001403](../../agents/web_agent.py#L1403) | 1403 | `"                snippet = summary"` | — |
| [SRC-1AE03B9EC3-L001404](../../agents/web_agent.py#L1404) | 1404 | `"            if not title or not isinstance(snippet, str) or not snippet.strip():"` | — |
| [SRC-1AE03B9EC3-L001405](../../agents/web_agent.py#L1405) | 1405 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001406](../../agents/web_agent.py#L1406) | 1406 | `"            rows.append({"` | — |
| [SRC-1AE03B9EC3-L001407](../../agents/web_agent.py#L1407) | 1407 | `"                \"title\": title,"` | — |
| [SRC-1AE03B9EC3-L001408](../../agents/web_agent.py#L1408) | 1408 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001409](../../agents/web_agent.py#L1409) | 1409 | `"                \"snippet\": _clean_text(snippet, 1600),"` | — |
| [SRC-1AE03B9EC3-L001410](../../agents/web_agent.py#L1410) | 1410 | `"                \"provider\": \"deepseek_search_api\","` | — |
| [SRC-1AE03B9EC3-L001411](../../agents/web_agent.py#L1411) | 1411 | `"                \"provider_rank\": len(rows) + 1,"` | — |
| [SRC-1AE03B9EC3-L001412](../../agents/web_agent.py#L1412) | 1412 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001413](../../agents/web_agent.py#L1413) | 1413 | `"                \"published_at\": _clean_text(item.get(\"date\", \"\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L001414](../../agents/web_agent.py#L1414) | 1414 | `"                \"publisher_name\": _clean_text(item.get(\"site_name\", \"\") or \"\", 200),"` | — |
| [SRC-1AE03B9EC3-L001415](../../agents/web_agent.py#L1415) | 1415 | `"                \"provider_rerank_score\": item.get(\"rerank_score\"),"` | — |
| [SRC-1AE03B9EC3-L001416](../../agents/web_agent.py#L1416) | 1416 | `"                \"provider_authority_tier\": item.get(\"authority\"),"` | — |
| [SRC-1AE03B9EC3-L001417](../../agents/web_agent.py#L1417) | 1417 | `"            })"` | — |
| [SRC-1AE03B9EC3-L001418](../../agents/web_agent.py#L1418) | 1418 | `"            if len(rows) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L001419](../../agents/web_agent.py#L1419) | 1419 | `"                break"` | — |
| [SRC-1AE03B9EC3-L001420](../../agents/web_agent.py#L1420) | 1420 | `"        return rows"` | — |
| [SRC-1AE03B9EC3-L001421](../../agents/web_agent.py#L1421) | 1421 | `""` | — |
| [SRC-1AE03B9EC3-L001422](../../agents/web_agent.py#L1422) | 1422 | `"    def _reset_deepseek_search_budget(self) -> None:"` | — |
| [SRC-1AE03B9EC3-L001423](../../agents/web_agent.py#L1423) | 1423 | `"        \"\"\"Reset the bounded optional Search API request budget for one operation.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001424](../../agents/web_agent.py#L1424) | 1424 | `"        with self._deepseek_budget_lock:"` | — |
| [SRC-1AE03B9EC3-L001425](../../agents/web_agent.py#L1425) | 1425 | `"            self._deepseek_search_requests_reserved = 0"` | — |
| [SRC-1AE03B9EC3-L001426](../../agents/web_agent.py#L1426) | 1426 | `""` | — |
| [SRC-1AE03B9EC3-L001427](../../agents/web_agent.py#L1427) | 1427 | `"    def _reserve_deepseek_search_request(self) -> bool:"` | — |
| [SRC-1AE03B9EC3-L001428](../../agents/web_agent.py#L1428) | 1428 | `"        \"\"\"Reserve one paid search request before concurrent queries invoke the provider.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001429](../../agents/web_agent.py#L1429) | 1429 | `"        if not os.getenv(\"DEEPSEEK_SEARCH_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L001430](../../agents/web_agent.py#L1430) | 1430 | `"            return False"` | — |
| [SRC-1AE03B9EC3-L001431](../../agents/web_agent.py#L1431) | 1431 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L001432](../../agents/web_agent.py#L1432) | 1432 | `"            configured_budget = int("` | — |
| [SRC-1AE03B9EC3-L001433](../../agents/web_agent.py#L1433) | 1433 | `"                os.getenv(\"OMARAI_DEEPSEEK_SEARCH_REQUEST_BUDGET\", \"1\").strip()"` | — |
| [SRC-1AE03B9EC3-L001434](../../agents/web_agent.py#L1434) | 1434 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001435](../../agents/web_agent.py#L1435) | 1435 | `"        except ValueError:"` | — |
| [SRC-1AE03B9EC3-L001436](../../agents/web_agent.py#L1436) | 1436 | `"            configured_budget = 1"` | — |
| [SRC-1AE03B9EC3-L001437](../../agents/web_agent.py#L1437) | 1437 | `"        budget = max(0, min(configured_budget, 3))"` | — |
| [SRC-1AE03B9EC3-L001438](../../agents/web_agent.py#L1438) | 1438 | `"        with self._deepseek_budget_lock:"` | — |
| [SRC-1AE03B9EC3-L001439](../../agents/web_agent.py#L1439) | 1439 | `"            if self._deepseek_search_requests_reserved >= budget:"` | — |
| [SRC-1AE03B9EC3-L001440](../../agents/web_agent.py#L1440) | 1440 | `"                return False"` | — |
| [SRC-1AE03B9EC3-L001441](../../agents/web_agent.py#L1441) | 1441 | `"            self._deepseek_search_requests_reserved += 1"` | — |
| [SRC-1AE03B9EC3-L001442](../../agents/web_agent.py#L1442) | 1442 | `"            return True"` | — |
| [SRC-1AE03B9EC3-L001443](../../agents/web_agent.py#L1443) | 1443 | `""` | — |
| [SRC-1AE03B9EC3-L001444](../../agents/web_agent.py#L1444) | 1444 | `"    def _search_web(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001445](../../agents/web_agent.py#L1445) | 1445 | `"        \"\"\"Run configured search connectors concurrently with isolated failures and relevance checks.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001446](../../agents/web_agent.py#L1446) | 1446 | `"        from agents.research import detect_freshness"` | — |
| [SRC-1AE03B9EC3-L001447](../../agents/web_agent.py#L1447) | 1447 | `""` | — |
| [SRC-1AE03B9EC3-L001448](../../agents/web_agent.py#L1448) | 1448 | `"        query = compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L001449](../../agents/web_agent.py#L1449) | 1449 | `"        if not query:"` | — |
| [SRC-1AE03B9EC3-L001450](../../agents/web_agent.py#L1450) | 1450 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L001451](../../agents/web_agent.py#L1451) | 1451 | `"        search_query = _normalize_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L001452](../../agents/web_agent.py#L1452) | 1452 | `"        budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L001453](../../agents/web_agent.py#L1453) | 1453 | `"        if budget is not None:"` | — |
| [SRC-1AE03B9EC3-L001454](../../agents/web_agent.py#L1454) | 1454 | `"            budget.reserve(\"search_queries\")"` | — |
| [SRC-1AE03B9EC3-L001455](../../agents/web_agent.py#L1455) | 1455 | `"        adapters: list[tuple[str, Any]] = ["` | — |
| [SRC-1AE03B9EC3-L001456](../../agents/web_agent.py#L1456) | 1456 | `"            (\"duckduckgo_html\", self._search_duckduckgo_html),"` | — |
| [SRC-1AE03B9EC3-L001457](../../agents/web_agent.py#L1457) | 1457 | `"            (\"bing_rss\", self._search_bing_rss),"` | — |
| [SRC-1AE03B9EC3-L001458](../../agents/web_agent.py#L1458) | 1458 | `"        ]"` | — |
| [SRC-1AE03B9EC3-L001459](../../agents/web_agent.py#L1459) | 1459 | `"        # Experimental opt-in only: DeepSeek Search is billed per successful request."` | — |
| [SRC-1AE03B9EC3-L001460](../../agents/web_agent.py#L1460) | 1460 | `"        # Do not promote it to primary without a measured comparison."` | — |
| [SRC-1AE03B9EC3-L001461](../../agents/web_agent.py#L1461) | 1461 | `"        if not os.getenv(\"DEEPSEEK_SEARCH_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L001462](../../agents/web_agent.py#L1462) | 1462 | `"            self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001463](../../agents/web_agent.py#L1463) | 1463 | `"                \"deepseek_search_api\", search_query, \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L001464](../../agents/web_agent.py#L1464) | 1464 | `"                error=\"DEEPSEEK_SEARCH_API_KEY is not set\","` | — |
| [SRC-1AE03B9EC3-L001465](../../agents/web_agent.py#L1465) | 1465 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001466](../../agents/web_agent.py#L1466) | 1466 | `"        elif self._reserve_deepseek_search_request():"` | — |
| [SRC-1AE03B9EC3-L001467](../../agents/web_agent.py#L1467) | 1467 | `"            adapters.append((\"deepseek_search_api\", self._search_deepseek_api))"` | — |
| [SRC-1AE03B9EC3-L001468](../../agents/web_agent.py#L1468) | 1468 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L001469](../../agents/web_agent.py#L1469) | 1469 | `"            self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001470](../../agents/web_agent.py#L1470) | 1470 | `"                \"deepseek_search_api\", search_query, \"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L001471](../../agents/web_agent.py#L1471) | 1471 | `"                error=\"per-operation DeepSeek Search request budget exhausted\","` | — |
| [SRC-1AE03B9EC3-L001472](../../agents/web_agent.py#L1472) | 1472 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001473](../../agents/web_agent.py#L1473) | 1473 | `"        if os.getenv(\"BRAVE_SEARCH_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L001474](../../agents/web_agent.py#L1474) | 1474 | `"            adapters.append((\"brave_search_api\", self._search_brave))"` | — |
| [SRC-1AE03B9EC3-L001475](../../agents/web_agent.py#L1475) | 1475 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L001476](../../agents/web_agent.py#L1476) | 1476 | `"            self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001477](../../agents/web_agent.py#L1477) | 1477 | `"                \"brave_search_api\", search_query, \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L001478](../../agents/web_agent.py#L1478) | 1478 | `"                error=\"BRAVE_SEARCH_API_KEY is not set\","` | — |
| [SRC-1AE03B9EC3-L001479](../../agents/web_agent.py#L1479) | 1479 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001480](../../agents/web_agent.py#L1480) | 1480 | `"        if os.getenv(\"TAVILY_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L001481](../../agents/web_agent.py#L1481) | 1481 | `"            adapters.append((\"tavily_search_api\", self._search_tavily))"` | — |
| [SRC-1AE03B9EC3-L001482](../../agents/web_agent.py#L1482) | 1482 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L001483](../../agents/web_agent.py#L1483) | 1483 | `"            self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001484](../../agents/web_agent.py#L1484) | 1484 | `"                \"tavily_search_api\", search_query, \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L001485](../../agents/web_agent.py#L1485) | 1485 | `"                error=\"TAVILY_API_KEY is not set\","` | — |
| [SRC-1AE03B9EC3-L001486](../../agents/web_agent.py#L1486) | 1486 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001487](../../agents/web_agent.py#L1487) | 1487 | `"        if detect_freshness(search_query):"` | — |
| [SRC-1AE03B9EC3-L001488](../../agents/web_agent.py#L1488) | 1488 | `"            adapters.append((\"google_news_rss\", self._search_news))"` | — |
| [SRC-1AE03B9EC3-L001489](../../agents/web_agent.py#L1489) | 1489 | `""` | — |
| [SRC-1AE03B9EC3-L001490](../../agents/web_agent.py#L1490) | 1490 | `"        async def run_one(name: str, method: Any) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001491](../../agents/web_agent.py#L1491) | 1491 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L001492](../../agents/web_agent.py#L1492) | 1492 | `"                if budget is not None:"` | — |
| [SRC-1AE03B9EC3-L001493](../../agents/web_agent.py#L1493) | 1493 | `"                    budget.reserve(\"search_calls\")"` | — |
| [SRC-1AE03B9EC3-L001494](../../agents/web_agent.py#L1494) | 1494 | `"                provider_timeout = self._effective_timeout(10.0)"` | — |
| [SRC-1AE03B9EC3-L001495](../../agents/web_agent.py#L1495) | 1495 | `"                raw = await asyncio.wait_for("` | — |
| [SRC-1AE03B9EC3-L001496](../../agents/web_agent.py#L1496) | 1496 | `"                    asyncio.to_thread(method, search_query), timeout=provider_timeout"` | — |
| [SRC-1AE03B9EC3-L001497](../../agents/web_agent.py#L1497) | 1497 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001498](../../agents/web_agent.py#L1498) | 1498 | `"                if not isinstance(raw, list):"` | — |
| [SRC-1AE03B9EC3-L001499](../../agents/web_agent.py#L1499) | 1499 | `"                    raise TypeError(\"connector returned a non-list result\")"` | — |
| [SRC-1AE03B9EC3-L001500](../../agents/web_agent.py#L1500) | 1500 | `"                accepted: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001501](../../agents/web_agent.py#L1501) | 1501 | `"                rejected = 0"` | — |
| [SRC-1AE03B9EC3-L001502](../../agents/web_agent.py#L1502) | 1502 | `"                rejection_counts = {reason: 0 for reason in _PROVIDER_REJECTION_REASONS}"` | — |
| [SRC-1AE03B9EC3-L001503](../../agents/web_agent.py#L1503) | 1503 | `"                for item in raw:"` | — |
| [SRC-1AE03B9EC3-L001504](../../agents/web_agent.py#L1504) | 1504 | `"                    if not isinstance(item, dict):"` | — |
| [SRC-1AE03B9EC3-L001505](../../agents/web_agent.py#L1505) | 1505 | `"                        rejected += 1"` | — |
| [SRC-1AE03B9EC3-L001506](../../agents/web_agent.py#L1506) | 1506 | `"                        rejection_counts[\"malformed_candidate\"] += 1"` | — |
| [SRC-1AE03B9EC3-L001507](../../agents/web_agent.py#L1507) | 1507 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L001508](../../agents/web_agent.py#L1508) | 1508 | `"                    safe_url = _public_http_url(item.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001509](../../agents/web_agent.py#L1509) | 1509 | `"                    if not safe_url:"` | — |
| [SRC-1AE03B9EC3-L001510](../../agents/web_agent.py#L1510) | 1510 | `"                        rejected += 1"` | — |
| [SRC-1AE03B9EC3-L001511](../../agents/web_agent.py#L1511) | 1511 | `"                        rejection_counts[\"invalid_url_or_unsafe_target\"] += 1"` | — |
| [SRC-1AE03B9EC3-L001512](../../agents/web_agent.py#L1512) | 1512 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L001513](../../agents/web_agent.py#L1513) | 1513 | `"                    if _blocked_source_url(safe_url):"` | — |
| [SRC-1AE03B9EC3-L001514](../../agents/web_agent.py#L1514) | 1514 | `"                        rejected += 1"` | — |
| [SRC-1AE03B9EC3-L001515](../../agents/web_agent.py#L1515) | 1515 | `"                        rejection_counts[\"blocked_domain\"] += 1"` | — |
| [SRC-1AE03B9EC3-L001516](../../agents/web_agent.py#L1516) | 1516 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L001517](../../agents/web_agent.py#L1517) | 1517 | `"                    normalized_item = dict(item)"` | — |
| [SRC-1AE03B9EC3-L001518](../../agents/web_agent.py#L1518) | 1518 | `"                    normalized_item[\"url\"] = safe_url"` | — |
| [SRC-1AE03B9EC3-L001519](../../agents/web_agent.py#L1519) | 1519 | `"                    normalized_item.setdefault(\"provider\", name)"` | — |
| [SRC-1AE03B9EC3-L001520](../../agents/web_agent.py#L1520) | 1520 | `"                    normalized_item.setdefault(\"search_query\", search_query)"` | — |
| [SRC-1AE03B9EC3-L001521](../../agents/web_agent.py#L1521) | 1521 | `"                    evidence = \" \".join(str(normalized_item.get(k) or \"\") for k in (\"title\", \"snippet\"))"` | — |
| [SRC-1AE03B9EC3-L001522](../../agents/web_agent.py#L1522) | 1522 | `"                    if _relevance_ratio(search_query, evidence) < _minimum_relevance_ratio(search_query):"` | — |
| [SRC-1AE03B9EC3-L001523](../../agents/web_agent.py#L1523) | 1523 | `"                        rejected += 1"` | — |
| [SRC-1AE03B9EC3-L001524](../../agents/web_agent.py#L1524) | 1524 | `"                        rejection_counts[\"relevance_below_threshold\"] += 1"` | — |
| [SRC-1AE03B9EC3-L001525](../../agents/web_agent.py#L1525) | 1525 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L001526](../../agents/web_agent.py#L1526) | 1526 | `"                    accepted.append(normalized_item)"` | — |
| [SRC-1AE03B9EC3-L001527](../../agents/web_agent.py#L1527) | 1527 | `"                if accepted:"` | — |
| [SRC-1AE03B9EC3-L001528](../../agents/web_agent.py#L1528) | 1528 | `"                    status = \"ok\""` | — |
