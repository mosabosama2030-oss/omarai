# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **011**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L000899 إلى SRC-1AE03B9EC3-L001698
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L000899](../../agents/web_agent.py#L899) | 899 | `"            \"not interested in purchasing\", \"no longer looking to buy\","` | — |
| [SRC-1AE03B9EC3-L000900](../../agents/web_agent.py#L900) | 900 | `"            \"do not want to buy\", \"don't want to buy\","` | — |
| [SRC-1AE03B9EC3-L000901](../../agents/web_agent.py#L901) | 901 | `"            \"مش بدور على\", \"مش عايز اشتري\", \"مش عاوز اشتري\","` | — |
| [SRC-1AE03B9EC3-L000902](../../agents/web_agent.py#L902) | 902 | `"            \"لا اريد شراء\", \"لا ارغب في شراء\", \"مش محتاج اشتري\","` | — |
| [SRC-1AE03B9EC3-L000903](../../agents/web_agent.py#L903) | 903 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000904](../../agents/web_agent.py#L904) | 904 | `"        for field, basis in evidence_fields:"` | — |
| [SRC-1AE03B9EC3-L000905](../../agents/web_agent.py#L905) | 905 | `"            raw = source.get(field)"` | — |
| [SRC-1AE03B9EC3-L000906](../../agents/web_agent.py#L906) | 906 | `"            if not isinstance(raw, str) or not raw.strip():"` | — |
| [SRC-1AE03B9EC3-L000907](../../agents/web_agent.py#L907) | 907 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L000908](../../agents/web_agent.py#L908) | 908 | `"            normalized = _normalize_search_query(raw).casefold()"` | — |
| [SRC-1AE03B9EC3-L000909](../../agents/web_agent.py#L909) | 909 | `"            if any(_normalize_search_query(term).casefold() in normalized for term in negations):"` | — |
| [SRC-1AE03B9EC3-L000910](../../agents/web_agent.py#L910) | 910 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L000911](../../agents/web_agent.py#L911) | 911 | `"            for signal_type, phrases in signal_phrases:"` | — |
| [SRC-1AE03B9EC3-L000912](../../agents/web_agent.py#L912) | 912 | `"                for phrase in phrases:"` | — |
| [SRC-1AE03B9EC3-L000913](../../agents/web_agent.py#L913) | 913 | `"                    needle = _normalize_search_query(phrase).casefold()"` | — |
| [SRC-1AE03B9EC3-L000914](../../agents/web_agent.py#L914) | 914 | `"                    if needle and needle in normalized:"` | — |
| [SRC-1AE03B9EC3-L000915](../../agents/web_agent.py#L915) | 915 | `"                        return {"` | — |
| [SRC-1AE03B9EC3-L000916](../../agents/web_agent.py#L916) | 916 | `"                            \"phrase\": phrase,"` | — |
| [SRC-1AE03B9EC3-L000917](../../agents/web_agent.py#L917) | 917 | `"                            \"basis\": basis,"` | — |
| [SRC-1AE03B9EC3-L000918](../../agents/web_agent.py#L918) | 918 | `"                            \"signal_type\": signal_type,"` | — |
| [SRC-1AE03B9EC3-L000919](../../agents/web_agent.py#L919) | 919 | `"                            \"product_fit\": \"unassessed\","` | — |
| [SRC-1AE03B9EC3-L000920](../../agents/web_agent.py#L920) | 920 | `"                        }"` | — |
| [SRC-1AE03B9EC3-L000921](../../agents/web_agent.py#L921) | 921 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000922](../../agents/web_agent.py#L922) | 922 | `""` | — |
| [SRC-1AE03B9EC3-L000923](../../agents/web_agent.py#L923) | 923 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000924](../../agents/web_agent.py#L924) | 924 | `"    def _lead_generation_queries("` | — |
| [SRC-1AE03B9EC3-L000925](../../agents/web_agent.py#L925) | 925 | `"        question: str, existing_queries: list[str] \| None = None"` | — |
| [SRC-1AE03B9EC3-L000926](../../agents/web_agent.py#L926) | 926 | `"    ) -> list[str]:"` | — |
| [SRC-1AE03B9EC3-L000927](../../agents/web_agent.py#L927) | 927 | `"        \"\"\"Build bounded buying-intent queries from the requested product, not a sector template.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000928](../../agents/web_agent.py#L928) | 928 | `"        subject = _normalize_search_query(question).strip()"` | — |
| [SRC-1AE03B9EC3-L000929](../../agents/web_agent.py#L929) | 929 | `"        subject = re.sub("` | — |
| [SRC-1AE03B9EC3-L000930](../../agents/web_agent.py#L930) | 930 | `"            r\"^(?:(?:من فضلك\|لو سمحت)\\s*)?(?:ابحث\|بحث\|دور\|دورلي\|اعثر)\\s+\""` | — |
| [SRC-1AE03B9EC3-L000931](../../agents/web_agent.py#L931) | 931 | `"            r\"(?:عن\|على)\\s+(?:عميل(?:\\s+محتمل)?\|عملاء(?:\\s+محتملين)?\|\""` | — |
| [SRC-1AE03B9EC3-L000932](../../agents/web_agent.py#L932) | 932 | `"            r\"مشتري(?:ن)?\|مشترين)\\s*(?:(?:الذي\|اللي\|الذين)\\s*)?\""` | — |
| [SRC-1AE03B9EC3-L000933](../../agents/web_agent.py#L933) | 933 | `"            r\"(?:(?:يريد\|عايز\|عاوز)\\s*(?:ان\\s*)?(?:يشتري\|شراء))?\\s*\","` | — |
| [SRC-1AE03B9EC3-L000934](../../agents/web_agent.py#L934) | 934 | `"            \"\", subject, flags=re.IGNORECASE,"` | — |
| [SRC-1AE03B9EC3-L000935](../../agents/web_agent.py#L935) | 935 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000936](../../agents/web_agent.py#L936) | 936 | `"        subject = re.sub("` | — |
| [SRC-1AE03B9EC3-L000937](../../agents/web_agent.py#L937) | 937 | `"            r\"^(?:please\\s+)?(?:find\|search for\|look for)\\s+(?:(?:a\|an)\\s+)?\""` | — |
| [SRC-1AE03B9EC3-L000938](../../agents/web_agent.py#L938) | 938 | `"            r\"(?:(?:potential\\s+)?(?:customer\|buyer\|prospect\|lead)s?)\\s*\""` | — |
| [SRC-1AE03B9EC3-L000939](../../agents/web_agent.py#L939) | 939 | `"            r\"(?:(?:who\|that)\\s*)?(?:(?:wants?\|looking to\|seeking to)\\s+\""` | — |
| [SRC-1AE03B9EC3-L000940](../../agents/web_agent.py#L940) | 940 | `"            r\"(?:buy\|purchase)\\s*)?\","` | — |
| [SRC-1AE03B9EC3-L000941](../../agents/web_agent.py#L941) | 941 | `"            \"\", subject, flags=re.IGNORECASE,"` | — |
| [SRC-1AE03B9EC3-L000942](../../agents/web_agent.py#L942) | 942 | `"        ).strip(\" \\t:;,.-\")"` | — |
| [SRC-1AE03B9EC3-L000943](../../agents/web_agent.py#L943) | 943 | `"        if len(_search_tokens(subject)) < 2:"` | — |
| [SRC-1AE03B9EC3-L000944](../../agents/web_agent.py#L944) | 944 | `"            subject = _normalize_search_query(question).strip()"` | — |
| [SRC-1AE03B9EC3-L000945](../../agents/web_agent.py#L945) | 945 | `"        profile = ProductProfile(name=subject[:240])"` | — |
| [SRC-1AE03B9EC3-L000946](../../agents/web_agent.py#L946) | 946 | `"        has_arabic = bool(re.search(r\"[\\u0600-\\u06FF]\", question))"` | — |
| [SRC-1AE03B9EC3-L000947](../../agents/web_agent.py#L947) | 947 | `"        has_latin = bool(re.search(r\"[A-Za-z]\", question))"` | — |
| [SRC-1AE03B9EC3-L000948](../../agents/web_agent.py#L948) | 948 | `"        locale = \"mixed\" if has_arabic and has_latin else \"ar\" if has_arabic else \"en\""` | — |
| [SRC-1AE03B9EC3-L000949](../../agents/web_agent.py#L949) | 949 | `"        return build_buyer_queries("` | — |
| [SRC-1AE03B9EC3-L000950](../../agents/web_agent.py#L950) | 950 | `"            profile,"` | — |
| [SRC-1AE03B9EC3-L000951](../../agents/web_agent.py#L951) | 951 | `"            locale=locale,"` | — |
| [SRC-1AE03B9EC3-L000952](../../agents/web_agent.py#L952) | 952 | `"            existing_queries=existing_queries or (),"` | — |
| [SRC-1AE03B9EC3-L000953](../../agents/web_agent.py#L953) | 953 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000954](../../agents/web_agent.py#L954) | 954 | `""` | — |
| [SRC-1AE03B9EC3-L000955](../../agents/web_agent.py#L955) | 955 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000956](../../agents/web_agent.py#L956) | 956 | `"    def _is_listing_discovery(question: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000957](../../agents/web_agent.py#L957) | 957 | `"        \"\"\"Recognize property/job/product discovery where candidates are useful with caveats.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000958](../../agents/web_agent.py#L958) | 958 | `"        value = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L000959](../../agents/web_agent.py#L959) | 959 | `"        entities = ("` | — |
| [SRC-1AE03B9EC3-L000960](../../agents/web_agent.py#L960) | 960 | `"            \"شقه\", \"شقق\", \"عقار\", \"عقارات\", \"فيلا\", \"فلل\", \"وحده سكنيه\","` | — |
| [SRC-1AE03B9EC3-L000961](../../agents/web_agent.py#L961) | 961 | `"            \"وحدات سكنيه\", \"apartment\", \"apartments\", \"flat\", \"property listing\","` | — |
| [SRC-1AE03B9EC3-L000962](../../agents/web_agent.py#L962) | 962 | `"            \"real estate\", \"house\", \"villa\", \"job opening\", \"وظيفه\", \"وظائف\","` | — |
| [SRC-1AE03B9EC3-L000963](../../agents/web_agent.py#L963) | 963 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000964](../../agents/web_agent.py#L964) | 964 | `"        actions = ("` | — |
| [SRC-1AE03B9EC3-L000965](../../agents/web_agent.py#L965) | 965 | `"            \"ابحث\", \"دور\", \"هات\", \"عايز\", \"عاوز\", \"محتاج\", \"بدور\", \"للبيع\","` | — |
| [SRC-1AE03B9EC3-L000966](../../agents/web_agent.py#L966) | 966 | `"            \"للايجار\", \"ايجار\", \"معاينه\", \"اعلان\", \"اعلانات\", \"find\", \"search\","` | — |
| [SRC-1AE03B9EC3-L000967](../../agents/web_agent.py#L967) | 967 | `"            \"looking for\", \"for sale\", \"for rent\","` | — |
| [SRC-1AE03B9EC3-L000968](../../agents/web_agent.py#L968) | 968 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000969](../../agents/web_agent.py#L969) | 969 | `"        normalized_entities = (_normalize_search_query(term).casefold() for term in entities)"` | — |
| [SRC-1AE03B9EC3-L000970](../../agents/web_agent.py#L970) | 970 | `"        normalized_actions = (_normalize_search_query(term).casefold() for term in actions)"` | — |
| [SRC-1AE03B9EC3-L000971](../../agents/web_agent.py#L971) | 971 | `"        return any(term in value for term in normalized_entities) and any("` | — |
| [SRC-1AE03B9EC3-L000972](../../agents/web_agent.py#L972) | 972 | `"            term in value for term in normalized_actions"` | — |
| [SRC-1AE03B9EC3-L000973](../../agents/web_agent.py#L973) | 973 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000974](../../agents/web_agent.py#L974) | 974 | `""` | — |
| [SRC-1AE03B9EC3-L000975](../../agents/web_agent.py#L975) | 975 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000976](../../agents/web_agent.py#L976) | 976 | `"    def _requires_web_research(question: str, mode: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000977](../../agents/web_agent.py#L977) | 977 | `"        \"\"\"Use the web only when the user requests it or the answer depends on live data.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000978](../../agents/web_agent.py#L978) | 978 | `"        # A question about whether the current answer already searched is a"` | — |
| [SRC-1AE03B9EC3-L000979](../../agents/web_agent.py#L979) | 979 | `"        # status query, not a request to launch fresh research in any UI mode."` | — |
| [SRC-1AE03B9EC3-L000980](../../agents/web_agent.py#L980) | 980 | `"        if WebAgent._is_current_search_status_question(question):"` | — |
| [SRC-1AE03B9EC3-L000981](../../agents/web_agent.py#L981) | 981 | `"            return False"` | — |
| [SRC-1AE03B9EC3-L000982](../../agents/web_agent.py#L982) | 982 | `"        if mode != \"auto\":"` | — |
| [SRC-1AE03B9EC3-L000983](../../agents/web_agent.py#L983) | 983 | `"            return True"` | — |
| [SRC-1AE03B9EC3-L000984](../../agents/web_agent.py#L984) | 984 | `"        value = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L000985](../../agents/web_agent.py#L985) | 985 | `"        dynamic_terms = ("` | — |
| [SRC-1AE03B9EC3-L000986](../../agents/web_agent.py#L986) | 986 | `"            \"ابحث\", \"بحث عن\", \"دور على\", \"دورلي\", \"هات رابط\", \"هاتلي\","` | — |
| [SRC-1AE03B9EC3-L000987](../../agents/web_agent.py#L987) | 987 | `"            \"جيبلي\", \"اعثر على\", \"موقع\", \"رابط\", \"لينك\", \"اخبار\", \"اخر\","` | — |
| [SRC-1AE03B9EC3-L000988](../../agents/web_agent.py#L988) | 988 | `"            \"احدث\", \"اليوم\", \"دلوقتي\", \"حاليا\", \"سعر\", \"اسعار\", \"للبيع\","` | — |
| [SRC-1AE03B9EC3-L000989](../../agents/web_agent.py#L989) | 989 | `"            \"للايجار\", \"ايجار\", \"معاينه\", \"عميل محتمل\", \"عملاء محتملين\","` | — |
| [SRC-1AE03B9EC3-L000990](../../agents/web_agent.py#L990) | 990 | `"            \"وظائف\", \"وظيفه\", \"حجز\", \"موعد\", \"الطقس\", \"سهم\", \"سعر الصرف\","` | — |
| [SRC-1AE03B9EC3-L000991](../../agents/web_agent.py#L991) | 991 | `"            \"search\", \"find\", \"look up\", \"latest\", \"today\", \"current\","` | — |
| [SRC-1AE03B9EC3-L000992](../../agents/web_agent.py#L992) | 992 | `"            \"news\", \"price\", \"for sale\", \"for rent\", \"real estate\", \"job opening\","` | — |
| [SRC-1AE03B9EC3-L000993](../../agents/web_agent.py#L993) | 993 | `"            \"appointment\", \"reservation\", \"weather\", \"stock price\", \"exchange rate\","` | — |
| [SRC-1AE03B9EC3-L000994](../../agents/web_agent.py#L994) | 994 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000995](../../agents/web_agent.py#L995) | 995 | `"        return any(term in value for term in dynamic_terms) or bool("` | — |
| [SRC-1AE03B9EC3-L000996](../../agents/web_agent.py#L996) | 996 | `"            re.search(r\"https?://\", question, flags=re.IGNORECASE)"` | — |
| [SRC-1AE03B9EC3-L000997](../../agents/web_agent.py#L997) | 997 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000998](../../agents/web_agent.py#L998) | 998 | `""` | — |
| [SRC-1AE03B9EC3-L000999](../../agents/web_agent.py#L999) | 999 | `"    def _local_answer_result(self, question: str, answer: str, kind: str) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L001000](../../agents/web_agent.py#L1000) | 1000 | `"        \"\"\"Build a consistently shaped answer for non-research conversational requests.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001001](../../agents/web_agent.py#L1001) | 1001 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L001002](../../agents/web_agent.py#L1002) | 1002 | `"            \"answer\": answer,"` | — |
| [SRC-1AE03B9EC3-L001003](../../agents/web_agent.py#L1003) | 1003 | `"            \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L001004](../../agents/web_agent.py#L1004) | 1004 | `"            \"search_query\": question,"` | — |
| [SRC-1AE03B9EC3-L001005](../../agents/web_agent.py#L1005) | 1005 | `"            \"search_queries\": [],"` | — |
| [SRC-1AE03B9EC3-L001006](../../agents/web_agent.py#L1006) | 1006 | `"            \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L001007](../../agents/web_agent.py#L1007) | 1007 | `"                \"mode\": \"auto\","` | — |
| [SRC-1AE03B9EC3-L001008](../../agents/web_agent.py#L1008) | 1008 | `"                \"planning_method\": \"local_capability_router\","` | — |
| [SRC-1AE03B9EC3-L001009](../../agents/web_agent.py#L1009) | 1009 | `"                \"web_search_skipped\": True,"` | — |
| [SRC-1AE03B9EC3-L001010](../../agents/web_agent.py#L1010) | 1010 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001011](../../agents/web_agent.py#L1011) | 1011 | `"            \"sources\": [],"` | — |
| [SRC-1AE03B9EC3-L001012](../../agents/web_agent.py#L1012) | 1012 | `"            \"used_language_model\": False,"` | — |
| [SRC-1AE03B9EC3-L001013](../../agents/web_agent.py#L1013) | 1013 | `"            \"used_web_search\": False,"` | — |
| [SRC-1AE03B9EC3-L001014](../../agents/web_agent.py#L1014) | 1014 | `"            \"search_attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L001015](../../agents/web_agent.py#L1015) | 1015 | `"            \"used_social_search\": False,"` | — |
| [SRC-1AE03B9EC3-L001016](../../agents/web_agent.py#L1016) | 1016 | `"            \"warnings\": [],"` | — |
| [SRC-1AE03B9EC3-L001017](../../agents/web_agent.py#L1017) | 1017 | `"            \"kind\": kind,"` | — |
| [SRC-1AE03B9EC3-L001018](../../agents/web_agent.py#L1018) | 1018 | `"            \"research_quality\": \"not_applicable\","` | — |
| [SRC-1AE03B9EC3-L001019](../../agents/web_agent.py#L1019) | 1019 | `"        }"` | — |
| [SRC-1AE03B9EC3-L001020](../../agents/web_agent.py#L1020) | 1020 | `""` | — |
| [SRC-1AE03B9EC3-L001021](../../agents/web_agent.py#L1021) | 1021 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L001022](../../agents/web_agent.py#L1022) | 1022 | `"    def _local_conversation_reply(question: str) -> str:"` | — |
| [SRC-1AE03B9EC3-L001023](../../agents/web_agent.py#L1023) | 1023 | `"        \"\"\"Return a short greeting/acknowledgment without a model or web request.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001024](../../agents/web_agent.py#L1024) | 1024 | `"        value = _normalize_search_query(question).casefold().strip(\" \\t\\r\\n؟?!.,،؛;\")"` | — |
| [SRC-1AE03B9EC3-L001025](../../agents/web_agent.py#L1025) | 1025 | `"        if \"السلام عليكم\" in value:"` | — |
| [SRC-1AE03B9EC3-L001026](../../agents/web_agent.py#L1026) | 1026 | `"            return \"وعليكم السلام ورحمة الله وبركاته. أنا معاك؛ أقدر أساعدك في إيه؟\""` | — |
| [SRC-1AE03B9EC3-L001027](../../agents/web_agent.py#L1027) | 1027 | `"        if any(term in value for term in (\"شكرا\", \"متشكر\", \"متشكره\", \"العفو\")):"` | — |
| [SRC-1AE03B9EC3-L001028](../../agents/web_agent.py#L1028) | 1028 | `"            return \"العفو، تحت أمرك.\""` | — |
| [SRC-1AE03B9EC3-L001029](../../agents/web_agent.py#L1029) | 1029 | `"        if re.search(r\"[a-z]\", value):"` | — |
| [SRC-1AE03B9EC3-L001030](../../agents/web_agent.py#L1030) | 1030 | `"            if any(term in value for term in (\"thanks\", \"thank you\", \"got it\")):"` | — |
| [SRC-1AE03B9EC3-L001031](../../agents/web_agent.py#L1031) | 1031 | `"                return \"You're welcome—glad it helped.\""` | — |
| [SRC-1AE03B9EC3-L001032](../../agents/web_agent.py#L1032) | 1032 | `"            return \"Hi! I'm here and ready to help. What would you like to work on?\""` | — |
| [SRC-1AE03B9EC3-L001033](../../agents/web_agent.py#L1033) | 1033 | `"        return \"أهلًا! أنا معاك. أقدر أساعدك في إيه؟\""` | — |
| [SRC-1AE03B9EC3-L001034](../../agents/web_agent.py#L1034) | 1034 | `""` | — |
| [SRC-1AE03B9EC3-L001035](../../agents/web_agent.py#L1035) | 1035 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L001036](../../agents/web_agent.py#L1036) | 1036 | `"    def _annotate_intent_route("` | — |
| [SRC-1AE03B9EC3-L001037](../../agents/web_agent.py#L1037) | 1037 | `"        result: dict[str, Any], route: str, reason: str, mode: str = \"auto\""` | — |
| [SRC-1AE03B9EC3-L001038](../../agents/web_agent.py#L1038) | 1038 | `"    ) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L001039](../../agents/web_agent.py#L1039) | 1039 | `"        \"\"\"Attach route diagnostics to both response and research-plan metadata.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001040](../../agents/web_agent.py#L1040) | 1040 | `"        result[\"intent_route\"] = route"` | — |
| [SRC-1AE03B9EC3-L001041](../../agents/web_agent.py#L1041) | 1041 | `"        result[\"intent_route_reason\"] = reason"` | — |
| [SRC-1AE03B9EC3-L001042](../../agents/web_agent.py#L1042) | 1042 | `"        plan = result.get(\"research_plan\")"` | — |
| [SRC-1AE03B9EC3-L001043](../../agents/web_agent.py#L1043) | 1043 | `"        if not isinstance(plan, dict):"` | — |
| [SRC-1AE03B9EC3-L001044](../../agents/web_agent.py#L1044) | 1044 | `"            plan = {}"` | — |
| [SRC-1AE03B9EC3-L001045](../../agents/web_agent.py#L1045) | 1045 | `"            result[\"research_plan\"] = plan"` | — |
| [SRC-1AE03B9EC3-L001046](../../agents/web_agent.py#L1046) | 1046 | `"        plan[\"intent_route\"] = route"` | — |
| [SRC-1AE03B9EC3-L001047](../../agents/web_agent.py#L1047) | 1047 | `"        plan[\"intent_route_reason\"] = reason"` | — |
| [SRC-1AE03B9EC3-L001048](../../agents/web_agent.py#L1048) | 1048 | `"        plan[\"mode\"] = mode"` | — |
| [SRC-1AE03B9EC3-L001049](../../agents/web_agent.py#L1049) | 1049 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L001050](../../agents/web_agent.py#L1050) | 1050 | `""` | — |
| [SRC-1AE03B9EC3-L001051](../../agents/web_agent.py#L1051) | 1051 | `"    def _clarification_result("` | — |
| [SRC-1AE03B9EC3-L001052](../../agents/web_agent.py#L1052) | 1052 | `"        self, question: str, mode: str, decision: dict[str, Any]"` | — |
| [SRC-1AE03B9EC3-L001053](../../agents/web_agent.py#L1053) | 1053 | `"    ) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L001054](../../agents/web_agent.py#L1054) | 1054 | `"        \"\"\"Return a bounded clarification result without starting web search.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001055](../../agents/web_agent.py#L1055) | 1055 | `"        if re.search(r\"[a-z]\", question.casefold()):"` | — |
| [SRC-1AE03B9EC3-L001056](../../agents/web_agent.py#L1056) | 1056 | `"            answer = ("` | — |
| [SRC-1AE03B9EC3-L001057](../../agents/web_agent.py#L1057) | 1057 | `"                \"What are you referring to? Please name the item or share its link, \""` | — |
| [SRC-1AE03B9EC3-L001058](../../agents/web_agent.py#L1058) | 1058 | `"                \"and I'll continue without guessing.\""` | — |
| [SRC-1AE03B9EC3-L001059](../../agents/web_agent.py#L1059) | 1059 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001060](../../agents/web_agent.py#L1060) | 1060 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L001061](../../agents/web_agent.py#L1061) | 1061 | `"            answer = ("` | — |
| [SRC-1AE03B9EC3-L001062](../../agents/web_agent.py#L1062) | 1062 | `"                \"تقصد إيه تحديدًا؟ اكتب اسم الشيء أو المنتج المقصود، أو ابعت الرابط، \""` | — |
| [SRC-1AE03B9EC3-L001063](../../agents/web_agent.py#L1063) | 1063 | `"                \"وأكمل معاك من غير ما أخمّن.\""` | — |
| [SRC-1AE03B9EC3-L001064](../../agents/web_agent.py#L1064) | 1064 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001065](../../agents/web_agent.py#L1065) | 1065 | `"        result = self._local_answer_result(question, answer, \"clarification_needed\")"` | — |
| [SRC-1AE03B9EC3-L001066](../../agents/web_agent.py#L1066) | 1066 | `"        return self._annotate_intent_route("` | — |
| [SRC-1AE03B9EC3-L001067](../../agents/web_agent.py#L1067) | 1067 | `"            result, \"CLARIFY\", str(decision.get(\"reason\", \"missing_referent\")), mode"` | — |
| [SRC-1AE03B9EC3-L001068](../../agents/web_agent.py#L1068) | 1068 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001069](../../agents/web_agent.py#L1069) | 1069 | `""` | — |
| [SRC-1AE03B9EC3-L001070](../../agents/web_agent.py#L1070) | 1070 | `"    def _dialogue_clarification_result("` | — |
| [SRC-1AE03B9EC3-L001071](../../agents/web_agent.py#L1071) | 1071 | `"        self, question: str, mode: str, context: dict[str, Any], reason: str"` | — |
| [SRC-1AE03B9EC3-L001072](../../agents/web_agent.py#L1072) | 1072 | `"    ) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L001073](../../agents/web_agent.py#L1073) | 1073 | `"        \"\"\"Expose why context resolution stopped and ask instead of guessing.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001074](../../agents/web_agent.py#L1074) | 1074 | `"        context = dict(context)"` | — |
| [SRC-1AE03B9EC3-L001075](../../agents/web_agent.py#L1075) | 1075 | `"        context[\"needs_clarification\"] = True"` | — |
| [SRC-1AE03B9EC3-L001076](../../agents/web_agent.py#L1076) | 1076 | `"        context[\"status\"] = \"needs_clarification\""` | — |
| [SRC-1AE03B9EC3-L001077](../../agents/web_agent.py#L1077) | 1077 | `"        context[\"resolved_question\"] = question[:MAX_QUESTION_CHARS]"` | — |
| [SRC-1AE03B9EC3-L001078](../../agents/web_agent.py#L1078) | 1078 | `"        context[\"resolution_basis\"] = \"insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L001079](../../agents/web_agent.py#L1079) | 1079 | `"        result = self._clarification_result("` | — |
| [SRC-1AE03B9EC3-L001080](../../agents/web_agent.py#L1080) | 1080 | `"            question, mode, {"` | — |
| [SRC-1AE03B9EC3-L001081](../../agents/web_agent.py#L1081) | 1081 | `"                \"reason\": reason,"` | — |
| [SRC-1AE03B9EC3-L001082](../../agents/web_agent.py#L1082) | 1082 | `"                \"needs_clarification\": True,"` | — |
| [SRC-1AE03B9EC3-L001083](../../agents/web_agent.py#L1083) | 1083 | `"                \"context_available\": bool(context.get(\"is_follow_up\")),"` | — |
| [SRC-1AE03B9EC3-L001084](../../agents/web_agent.py#L1084) | 1084 | `"            }"` | — |
| [SRC-1AE03B9EC3-L001085](../../agents/web_agent.py#L1085) | 1085 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001086](../../agents/web_agent.py#L1086) | 1086 | `"        requested_clarification = context.get(\"clarification_question\")"` | — |
| [SRC-1AE03B9EC3-L001087](../../agents/web_agent.py#L1087) | 1087 | `"        if isinstance(requested_clarification, str) and requested_clarification.strip():"` | — |
| [SRC-1AE03B9EC3-L001088](../../agents/web_agent.py#L1088) | 1088 | `"            result[\"answer\"] = requested_clarification[:400]"` | — |
| [SRC-1AE03B9EC3-L001089](../../agents/web_agent.py#L1089) | 1089 | `"        result[\"dialogue_context\"] = context"` | — |
| [SRC-1AE03B9EC3-L001090](../../agents/web_agent.py#L1090) | 1090 | `"        if isinstance(result.get(\"research_plan\"), dict):"` | — |
| [SRC-1AE03B9EC3-L001091](../../agents/web_agent.py#L1091) | 1091 | `"            result[\"research_plan\"][\"dialogue_context\"] = context"` | — |
| [SRC-1AE03B9EC3-L001092](../../agents/web_agent.py#L1092) | 1092 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L001093](../../agents/web_agent.py#L1093) | 1093 | `""` | — |
| [SRC-1AE03B9EC3-L001094](../../agents/web_agent.py#L1094) | 1094 | `"    def _capability_status_snapshot(self) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L001095](../../agents/web_agent.py#L1095) | 1095 | `"        \"\"\"Describe configured capabilities without claiming a live health check.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001096](../../agents/web_agent.py#L1096) | 1096 | `"        status = self.status()"` | — |
| [SRC-1AE03B9EC3-L001097](../../agents/web_agent.py#L1097) | 1097 | `"        not_tested = \"not_tested_in_this_response\""` | — |
| [SRC-1AE03B9EC3-L001098](../../agents/web_agent.py#L1098) | 1098 | `"        providers = ["` | — |
| [SRC-1AE03B9EC3-L001099](../../agents/web_agent.py#L1099) | 1099 | `"            {"` | — |
| [SRC-1AE03B9EC3-L001100](../../agents/web_agent.py#L1100) | 1100 | `"                \"name\": \"duckduckgo_html\","` | — |
| [SRC-1AE03B9EC3-L001101](../../agents/web_agent.py#L1101) | 1101 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L001102](../../agents/web_agent.py#L1102) | 1102 | `"                \"configuration_status\": \"built_in_no_api_key\","` | — |
| [SRC-1AE03B9EC3-L001103](../../agents/web_agent.py#L1103) | 1103 | `"                \"runtime_status\": not_tested,"` | — |
| [SRC-1AE03B9EC3-L001104](../../agents/web_agent.py#L1104) | 1104 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001105](../../agents/web_agent.py#L1105) | 1105 | `"            {"` | — |
| [SRC-1AE03B9EC3-L001106](../../agents/web_agent.py#L1106) | 1106 | `"                \"name\": \"bing_rss\","` | — |
| [SRC-1AE03B9EC3-L001107](../../agents/web_agent.py#L1107) | 1107 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L001108](../../agents/web_agent.py#L1108) | 1108 | `"                \"configuration_status\": \"built_in_no_api_key\","` | — |
| [SRC-1AE03B9EC3-L001109](../../agents/web_agent.py#L1109) | 1109 | `"                \"runtime_status\": not_tested,"` | — |
| [SRC-1AE03B9EC3-L001110](../../agents/web_agent.py#L1110) | 1110 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001111](../../agents/web_agent.py#L1111) | 1111 | `"            {"` | — |
| [SRC-1AE03B9EC3-L001112](../../agents/web_agent.py#L1112) | 1112 | `"                \"name\": \"google_news_rss\","` | — |
| [SRC-1AE03B9EC3-L001113](../../agents/web_agent.py#L1113) | 1113 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L001114](../../agents/web_agent.py#L1114) | 1114 | `"                \"configuration_status\": \"conditional_no_api_key\","` | — |
| [SRC-1AE03B9EC3-L001115](../../agents/web_agent.py#L1115) | 1115 | `"                \"runtime_status\": not_tested,"` | — |
| [SRC-1AE03B9EC3-L001116](../../agents/web_agent.py#L1116) | 1116 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001117](../../agents/web_agent.py#L1117) | 1117 | `"            {"` | — |
| [SRC-1AE03B9EC3-L001118](../../agents/web_agent.py#L1118) | 1118 | `"                \"name\": \"deepseek_search_api\","` | — |
| [SRC-1AE03B9EC3-L001119](../../agents/web_agent.py#L1119) | 1119 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L001120](../../agents/web_agent.py#L1120) | 1120 | `"                \"configuration_status\": ("` | — |
| [SRC-1AE03B9EC3-L001121](../../agents/web_agent.py#L1121) | 1121 | `"                    \"configured\" if status.get(\"deepseek_search_api_configured\")"` | — |
| [SRC-1AE03B9EC3-L001122](../../agents/web_agent.py#L1122) | 1122 | `"                    else \"not_configured\""` | — |
| [SRC-1AE03B9EC3-L001123](../../agents/web_agent.py#L1123) | 1123 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001124](../../agents/web_agent.py#L1124) | 1124 | `"                \"runtime_status\": not_tested if status.get(\"deepseek_search_api_configured\")"` | — |
| [SRC-1AE03B9EC3-L001125](../../agents/web_agent.py#L1125) | 1125 | `"                else \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L001126](../../agents/web_agent.py#L1126) | 1126 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001127](../../agents/web_agent.py#L1127) | 1127 | `"            {"` | — |
| [SRC-1AE03B9EC3-L001128](../../agents/web_agent.py#L1128) | 1128 | `"                \"name\": \"brave_search_api\","` | — |
| [SRC-1AE03B9EC3-L001129](../../agents/web_agent.py#L1129) | 1129 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L001130](../../agents/web_agent.py#L1130) | 1130 | `"                \"configuration_status\": ("` | — |
| [SRC-1AE03B9EC3-L001131](../../agents/web_agent.py#L1131) | 1131 | `"                    \"configured\" if status.get(\"brave_search_api_configured\")"` | — |
| [SRC-1AE03B9EC3-L001132](../../agents/web_agent.py#L1132) | 1132 | `"                    else \"not_configured\""` | — |
| [SRC-1AE03B9EC3-L001133](../../agents/web_agent.py#L1133) | 1133 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001134](../../agents/web_agent.py#L1134) | 1134 | `"                \"runtime_status\": not_tested if status.get(\"brave_search_api_configured\")"` | — |
| [SRC-1AE03B9EC3-L001135](../../agents/web_agent.py#L1135) | 1135 | `"                else \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L001136](../../agents/web_agent.py#L1136) | 1136 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001137](../../agents/web_agent.py#L1137) | 1137 | `"            {"` | — |
| [SRC-1AE03B9EC3-L001138](../../agents/web_agent.py#L1138) | 1138 | `"                \"name\": \"tavily_search_api\","` | — |
| [SRC-1AE03B9EC3-L001139](../../agents/web_agent.py#L1139) | 1139 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L001140](../../agents/web_agent.py#L1140) | 1140 | `"                \"configuration_status\": ("` | — |
| [SRC-1AE03B9EC3-L001141](../../agents/web_agent.py#L1141) | 1141 | `"                    \"configured\" if status.get(\"tavily_search_api_configured\")"` | — |
| [SRC-1AE03B9EC3-L001142](../../agents/web_agent.py#L1142) | 1142 | `"                    else \"not_configured\""` | — |
| [SRC-1AE03B9EC3-L001143](../../agents/web_agent.py#L1143) | 1143 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001144](../../agents/web_agent.py#L1144) | 1144 | `"                \"runtime_status\": not_tested if status.get(\"tavily_search_api_configured\")"` | — |
| [SRC-1AE03B9EC3-L001145](../../agents/web_agent.py#L1145) | 1145 | `"                else \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L001146](../../agents/web_agent.py#L1146) | 1146 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001147](../../agents/web_agent.py#L1147) | 1147 | `"            {"` | — |
| [SRC-1AE03B9EC3-L001148](../../agents/web_agent.py#L1148) | 1148 | `"                \"name\": \"openrouter_web_search\","` | — |
| [SRC-1AE03B9EC3-L001149](../../agents/web_agent.py#L1149) | 1149 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L001150](../../agents/web_agent.py#L1150) | 1150 | `"                \"configuration_status\": ("` | — |
| [SRC-1AE03B9EC3-L001151](../../agents/web_agent.py#L1151) | 1151 | `"                    \"enabled\" if status.get(\"openrouter_web_search_enabled\")"` | — |
| [SRC-1AE03B9EC3-L001152](../../agents/web_agent.py#L1152) | 1152 | `"                    else \"disabled\""` | — |
| [SRC-1AE03B9EC3-L001153](../../agents/web_agent.py#L1153) | 1153 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001154](../../agents/web_agent.py#L1154) | 1154 | `"                \"runtime_status\": not_tested if status.get(\"openrouter_web_search_enabled\")"` | — |
| [SRC-1AE03B9EC3-L001155](../../agents/web_agent.py#L1155) | 1155 | `"                else \"disabled\","` | — |
| [SRC-1AE03B9EC3-L001156](../../agents/web_agent.py#L1156) | 1156 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001157](../../agents/web_agent.py#L1157) | 1157 | `"        ]"` | — |
| [SRC-1AE03B9EC3-L001158](../../agents/web_agent.py#L1158) | 1158 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L001159](../../agents/web_agent.py#L1159) | 1159 | `"            \"web_search\": {"` | — |
| [SRC-1AE03B9EC3-L001160](../../agents/web_agent.py#L1160) | 1160 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L001161](../../agents/web_agent.py#L1161) | 1161 | `"                \"local_dependencies_ready\": bool(status.get(\"web_search_ready\")),"` | — |
| [SRC-1AE03B9EC3-L001162](../../agents/web_agent.py#L1162) | 1162 | `"                \"runtime_status\": not_tested,"` | — |
| [SRC-1AE03B9EC3-L001163](../../agents/web_agent.py#L1163) | 1163 | `"                \"providers\": providers,"` | — |
| [SRC-1AE03B9EC3-L001164](../../agents/web_agent.py#L1164) | 1164 | `"                \"semantics\": ("` | — |
| [SRC-1AE03B9EC3-L001165](../../agents/web_agent.py#L1165) | 1165 | `"                    \"Configuration and installed dependencies do not prove that a live \""` | — |
| [SRC-1AE03B9EC3-L001166](../../agents/web_agent.py#L1166) | 1166 | `"                    \"network request will succeed.\""` | — |
| [SRC-1AE03B9EC3-L001167](../../agents/web_agent.py#L1167) | 1167 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001168](../../agents/web_agent.py#L1168) | 1168 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001169](../../agents/web_agent.py#L1169) | 1169 | `"            \"language_model\": {"` | — |
| [SRC-1AE03B9EC3-L001170](../../agents/web_agent.py#L1170) | 1170 | `"                \"configured\": bool(status.get(\"language_model_configured\")),"` | — |
| [SRC-1AE03B9EC3-L001171](../../agents/web_agent.py#L1171) | 1171 | `"                \"runtime_status\": not_tested,"` | — |
| [SRC-1AE03B9EC3-L001172](../../agents/web_agent.py#L1172) | 1172 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001173](../../agents/web_agent.py#L1173) | 1173 | `"        }"` | — |
| [SRC-1AE03B9EC3-L001174](../../agents/web_agent.py#L1174) | 1174 | `""` | — |
| [SRC-1AE03B9EC3-L001175](../../agents/web_agent.py#L1175) | 1175 | `"    def _self_description_answer(self, question: str) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L001176](../../agents/web_agent.py#L1176) | 1176 | `"        \"\"\"Answer self/capability questions without inventing a live health result.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001177](../../agents/web_agent.py#L1177) | 1177 | `"        value = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L001178](../../agents/web_agent.py#L1178) | 1178 | `"        current_search_question = self._is_current_search_status_question(question)"` | — |
| [SRC-1AE03B9EC3-L001179](../../agents/web_agent.py#L1179) | 1179 | `""` | — |
| [SRC-1AE03B9EC3-L001180](../../agents/web_agent.py#L1180) | 1180 | `"        if current_search_question:"` | — |
| [SRC-1AE03B9EC3-L001181](../../agents/web_agent.py#L1181) | 1181 | `"            answer = ("` | — |
| [SRC-1AE03B9EC3-L001182](../../agents/web_agent.py#L1182) | 1182 | `"                \"لا، لم أنفّذ بحثًا حيًا للإجابة عن هذا السؤال تحديدًا؛ هذا السؤال عن \""` | — |
| [SRC-1AE03B9EC3-L001183](../../agents/web_agent.py#L1183) | 1183 | `"                \"طريقة عملي، ولذلك لم أبدأ بحث ويب في هذه الجولة. هذا لا يعني أن البحث \""` | — |
| [SRC-1AE03B9EC3-L001184](../../agents/web_agent.py#L1184) | 1184 | `"                \"غير متاح؛ عند تنفيذ طلب يحتاج إلى معلومات حديثة سأوضح هل جرت محاولة البحث، \""` | — |
| [SRC-1AE03B9EC3-L001185](../../agents/web_agent.py#L1185) | 1185 | `"                \"وما النتائج التي عادت، وما إذا اكتملت الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L001186](../../agents/web_agent.py#L1186) | 1186 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001187](../../agents/web_agent.py#L1187) | 1187 | `"            result = self._local_answer_result(question, answer, \"capability_answer\")"` | — |
| [SRC-1AE03B9EC3-L001188](../../agents/web_agent.py#L1188) | 1188 | `"            result[\"request_execution_status\"] = {"` | — |
| [SRC-1AE03B9EC3-L001189](../../agents/web_agent.py#L1189) | 1189 | `"                \"search_attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L001190](../../agents/web_agent.py#L1190) | 1190 | `"                \"search_outcome\": \"not_attempted\","` | — |
| [SRC-1AE03B9EC3-L001191](../../agents/web_agent.py#L1191) | 1191 | `"                \"semantics\": \"status_of_this_request_only\","` | — |
| [SRC-1AE03B9EC3-L001192](../../agents/web_agent.py#L1192) | 1192 | `"            }"` | — |
| [SRC-1AE03B9EC3-L001193](../../agents/web_agent.py#L1193) | 1193 | `"            result[\"capability_status\"] = self._capability_status_snapshot()"` | — |
| [SRC-1AE03B9EC3-L001194](../../agents/web_agent.py#L1194) | 1194 | `"            return result"` | — |
| [SRC-1AE03B9EC3-L001195](../../agents/web_agent.py#L1195) | 1195 | `""` | — |
| [SRC-1AE03B9EC3-L001196](../../agents/web_agent.py#L1196) | 1196 | `"        capability_phrases = ("` | — |
| [SRC-1AE03B9EC3-L001197](../../agents/web_agent.py#L1197) | 1197 | `"            \"كيف تستطيع مساعدتي\", \"ازاي تقدر تساعدني\", \"ازاي ممكن تساعدني\","` | — |
| [SRC-1AE03B9EC3-L001198](../../agents/web_agent.py#L1198) | 1198 | `"            \"ماذا تستطيع ان تفعل\", \"ما الذي تستطيع فعله\", \"ايه اللي تقدر تعمله\","` | — |
| [SRC-1AE03B9EC3-L001199](../../agents/web_agent.py#L1199) | 1199 | `"            \"what can you do\", \"how can you help me\","` | — |
| [SRC-1AE03B9EC3-L001200](../../agents/web_agent.py#L1200) | 1200 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001201](../../agents/web_agent.py#L1201) | 1201 | `"        if any(term in value for term in capability_phrases):"` | — |
| [SRC-1AE03B9EC3-L001202](../../agents/web_agent.py#L1202) | 1202 | `"            answer = ("` | — |
| [SRC-1AE03B9EC3-L001203](../../agents/web_agent.py#L1203) | 1203 | `"                \"أقدر أساعدك في شرح الأسئلة ووضع خطط عملية، كما يتضمن Omarai مسارًا \""` | — |
| [SRC-1AE03B9EC3-L001204](../../agents/web_agent.py#L1204) | 1204 | `"                \"للبحث في الويب عند الحاجة إلى معلومات حديثة أو روابط أو مقارنة خيارات. \""` | — |
| [SRC-1AE03B9EC3-L001205](../../agents/web_agent.py#L1205) | 1205 | `"                \"سأوضح في كل مهمة ما إذا نُفذ البحث فعلًا وما المصادر التي أمكن جمعها، \""` | — |
| [SRC-1AE03B9EC3-L001206](../../agents/web_agent.py#L1206) | 1206 | `"                \"وما الذي لم يمكن التحقق منه. قد تعمل بعض الموصلات الاختيارية فقط عند \""` | — |
| [SRC-1AE03B9EC3-L001207](../../agents/web_agent.py#L1207) | 1207 | `"                \"ضبط إعداداتها، ولا أضمن الوصول إلى كل موقع أو إلى المجموعات والمنشورات \""` | — |
| [SRC-1AE03B9EC3-L001208](../../agents/web_agent.py#L1208) | 1208 | `"                \"الخاصة. لم أجرِ اختبار اتصال حي في هذه الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L001209](../../agents/web_agent.py#L1209) | 1209 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001210](../../agents/web_agent.py#L1210) | 1210 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L001211](../../agents/web_agent.py#L1211) | 1211 | `"            status = self.status()"` | — |
| [SRC-1AE03B9EC3-L001212](../../agents/web_agent.py#L1212) | 1212 | `"            providers = [\"DuckDuckGo HTML\", \"Bing RSS\"]"` | — |
| [SRC-1AE03B9EC3-L001213](../../agents/web_agent.py#L1213) | 1213 | `"            providers.append(\"Google News RSS عند ملاءمة السؤال أو الحاجة إلى معلومات حديثة\")"` | — |
| [SRC-1AE03B9EC3-L001214](../../agents/web_agent.py#L1214) | 1214 | `"            if status.get(\"deepseek_search_api_configured\"):"` | — |
| [SRC-1AE03B9EC3-L001215](../../agents/web_agent.py#L1215) | 1215 | `"                providers.append("` | — |
| [SRC-1AE03B9EC3-L001216](../../agents/web_agent.py#L1216) | 1216 | `"                    \"DeepSeek Search API (مفتاحه مضبوط، لكنه غير مختبر في هذه الإجابة \""` | — |
| [SRC-1AE03B9EC3-L001217](../../agents/web_agent.py#L1217) | 1217 | `"                    \"وقد يستهلك استخدامًا مدفوعًا)\""` | — |
| [SRC-1AE03B9EC3-L001218](../../agents/web_agent.py#L1218) | 1218 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001219](../../agents/web_agent.py#L1219) | 1219 | `"            if status.get(\"brave_search_api_configured\"):"` | — |
| [SRC-1AE03B9EC3-L001220](../../agents/web_agent.py#L1220) | 1220 | `"                providers.append(\"Brave Search API (الإعداد موجود، وليس دليلًا على نجاح الاتصال)\")"` | — |
| [SRC-1AE03B9EC3-L001221](../../agents/web_agent.py#L1221) | 1221 | `"            if status.get(\"tavily_search_api_configured\"):"` | — |
| [SRC-1AE03B9EC3-L001222](../../agents/web_agent.py#L1222) | 1222 | `"                providers.append(\"Tavily Search API (الإعداد موجود، وليس دليلًا على نجاح الاتصال)\")"` | — |
| [SRC-1AE03B9EC3-L001223](../../agents/web_agent.py#L1223) | 1223 | `"            if status.get(\"openrouter_web_search_enabled\"):"` | — |
| [SRC-1AE03B9EC3-L001224](../../agents/web_agent.py#L1224) | 1224 | `"                providers.append(\"بحث OpenRouter المباشر (مفعّل بالإعداد، وقد يستهلك رصيدًا)\")"` | — |
| [SRC-1AE03B9EC3-L001225](../../agents/web_agent.py#L1225) | 1225 | `"            answer = ("` | — |
| [SRC-1AE03B9EC3-L001226](../../agents/web_agent.py#L1226) | 1226 | `"                \"بحسب الكود الحالي، يتضمن Omarai مسار بحث ويب يستخدم: \""` | — |
| [SRC-1AE03B9EC3-L001227](../../agents/web_agent.py#L1227) | 1227 | `"                + \"، \".join(providers)"` | — |
| [SRC-1AE03B9EC3-L001228](../../agents/web_agent.py#L1228) | 1228 | `"                + \". هذه قائمة بالموصلات المضمّنة أو المهيأة، وليست إثباتًا بأنها نجحت \""` | — |
| [SRC-1AE03B9EC3-L001229](../../agents/web_agent.py#L1229) | 1229 | `"                \"في هذه اللحظة. لم أنفّذ اختبار اتصال حي في هذه الإجابة، لذلك لا أستطيع \""` | — |
| [SRC-1AE03B9EC3-L001230](../../agents/web_agent.py#L1230) | 1230 | `"                \"تأكيد توافر الشبكة الآن. عند طلب بحث فعلي، ينبغي أن يوضح التقرير ما إذا \""` | — |
| [SRC-1AE03B9EC3-L001231](../../agents/web_agent.py#L1231) | 1231 | `"                \"بدأت المحاولة، وما الموصلات التي أعادت نتائج، وما الصفحات التي أمكن قراءة \""` | — |
| [SRC-1AE03B9EC3-L001232](../../agents/web_agent.py#L1232) | 1232 | `"                \"محتواها. لا يوجد وصول مضمون إلى كل الإنترنت أو إلى المحتوى الخاص.\""` | — |
| [SRC-1AE03B9EC3-L001233](../../agents/web_agent.py#L1233) | 1233 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001234](../../agents/web_agent.py#L1234) | 1234 | `"        result = self._local_answer_result(question, answer, \"capability_answer\")"` | — |
| [SRC-1AE03B9EC3-L001235](../../agents/web_agent.py#L1235) | 1235 | `"        result[\"capability_status\"] = self._capability_status_snapshot()"` | — |
| [SRC-1AE03B9EC3-L001236](../../agents/web_agent.py#L1236) | 1236 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L001237](../../agents/web_agent.py#L1237) | 1237 | `""` | — |
| [SRC-1AE03B9EC3-L001238](../../agents/web_agent.py#L1238) | 1238 | `"    def _answer_without_search("` | — |
| [SRC-1AE03B9EC3-L001239](../../agents/web_agent.py#L1239) | 1239 | `"        self, question: str, history: list[dict[str, str]]"` | — |
| [SRC-1AE03B9EC3-L001240](../../agents/web_agent.py#L1240) | 1240 | `"    ) -> dict[str, Any] \| None:"` | — |
| [SRC-1AE03B9EC3-L001241](../../agents/web_agent.py#L1241) | 1241 | `"        \"\"\"Answer stable informational questions with the configured LLM, without fake citations.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001242](../../agents/web_agent.py#L1242) | 1242 | `"        if not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L001243](../../agents/web_agent.py#L1243) | 1243 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L001244](../../agents/web_agent.py#L1244) | 1244 | `"        messages: list[dict[str, str]] = ["` | — |
| [SRC-1AE03B9EC3-L001245](../../agents/web_agent.py#L1245) | 1245 | `"            {"` | — |
| [SRC-1AE03B9EC3-L001246](../../agents/web_agent.py#L1246) | 1246 | `"                \"role\": \"system\","` | — |
| [SRC-1AE03B9EC3-L001247](../../agents/web_agent.py#L1247) | 1247 | `"                \"content\": ("` | — |
| [SRC-1AE03B9EC3-L001248](../../agents/web_agent.py#L1248) | 1248 | `"                    \"أنت Omarai، مساعد عربي عملي. أجب مباشرة وباللغة التي استخدمها الشخص، \""` | — |
| [SRC-1AE03B9EC3-L001249](../../agents/web_agent.py#L1249) | 1249 | `"                    \"وافهم المقصود حتى لو كان باللهجة المصرية أو به أخطاء كتابية. هذا المسار \""` | — |
| [SRC-1AE03B9EC3-L001250](../../agents/web_agent.py#L1250) | 1250 | `"                    \"للشرح والمعرفة العامة والأسئلة الحوارية غير المعتمدة على معلومات لحظية. \""` | — |
| [SRC-1AE03B9EC3-L001251](../../agents/web_agent.py#L1251) | 1251 | `"                    \"لا تستخدم أدوات الويب ولا تقل إنك بحثت أو تحققت من مصدر. لا تختلق أرقامًا \""` | — |
| [SRC-1AE03B9EC3-L001252](../../agents/web_agent.py#L1252) | 1252 | `"                    \"أو اقتباسات أو روابط. إذا كان جزء من السؤال يتطلب بيانات حديثة أو تحققًا \""` | — |
| [SRC-1AE03B9EC3-L001253](../../agents/web_agent.py#L1253) | 1253 | `"                    \"خارجيًا، صرّح بذلك بدل الجزم. وضّح عدم اليقين بإيجاز، وأعط إجابة مفيدة \""` | — |
| [SRC-1AE03B9EC3-L001254](../../agents/web_agent.py#L1254) | 1254 | `"                    \"من غير إطالة أو سلسلة تفكير داخلية.\""` | — |
| [SRC-1AE03B9EC3-L001255](../../agents/web_agent.py#L1255) | 1255 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001256](../../agents/web_agent.py#L1256) | 1256 | `"            }"` | — |
| [SRC-1AE03B9EC3-L001257](../../agents/web_agent.py#L1257) | 1257 | `"        ]"` | — |
| [SRC-1AE03B9EC3-L001258](../../agents/web_agent.py#L1258) | 1258 | `"        messages.extend(history[-MAX_HISTORY_ITEMS:])"` | — |
| [SRC-1AE03B9EC3-L001259](../../agents/web_agent.py#L1259) | 1259 | `"        messages.append({\"role\": \"user\", \"content\": question})"` | — |
| [SRC-1AE03B9EC3-L001260](../../agents/web_agent.py#L1260) | 1260 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L001261](../../agents/web_agent.py#L1261) | 1261 | `"            answer = self._request_completion("` | — |
| [SRC-1AE03B9EC3-L001262](../../agents/web_agent.py#L1262) | 1262 | `"                messages,"` | — |
| [SRC-1AE03B9EC3-L001263](../../agents/web_agent.py#L1263) | 1263 | `"                max_tokens=1500,"` | — |
| [SRC-1AE03B9EC3-L001264](../../agents/web_agent.py#L1264) | 1264 | `"                temperature=0.2,"` | — |
| [SRC-1AE03B9EC3-L001265](../../agents/web_agent.py#L1265) | 1265 | `"                timeout=self._effective_timeout(min(self.timeout, 28)),"` | — |
| [SRC-1AE03B9EC3-L001266](../../agents/web_agent.py#L1266) | 1266 | `"                model=self.answer_model,"` | — |
| [SRC-1AE03B9EC3-L001267](../../agents/web_agent.py#L1267) | 1267 | `"                enable_web_search=False,"` | — |
| [SRC-1AE03B9EC3-L001268](../../agents/web_agent.py#L1268) | 1268 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001269](../../agents/web_agent.py#L1269) | 1269 | `"        except (RuntimeError, AgentDependencyError):"` | — |
| [SRC-1AE03B9EC3-L001270](../../agents/web_agent.py#L1270) | 1270 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L001271](../../agents/web_agent.py#L1271) | 1271 | `"        # Never turn an overlong completion into a seemingly complete answer by slicing it."` | — |
| [SRC-1AE03B9EC3-L001272](../../agents/web_agent.py#L1272) | 1272 | `"        if len(answer) > 24_000:"` | — |
| [SRC-1AE03B9EC3-L001273](../../agents/web_agent.py#L1273) | 1273 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L001274](../../agents/web_agent.py#L1274) | 1274 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L001275](../../agents/web_agent.py#L1275) | 1275 | `"            \"answer\": answer,"` | — |
| [SRC-1AE03B9EC3-L001276](../../agents/web_agent.py#L1276) | 1276 | `"            \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L001277](../../agents/web_agent.py#L1277) | 1277 | `"            \"search_query\": question,"` | — |
| [SRC-1AE03B9EC3-L001278](../../agents/web_agent.py#L1278) | 1278 | `"            \"search_queries\": [],"` | — |
| [SRC-1AE03B9EC3-L001279](../../agents/web_agent.py#L1279) | 1279 | `"            \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L001280](../../agents/web_agent.py#L1280) | 1280 | `"                \"mode\": \"auto\","` | — |
| [SRC-1AE03B9EC3-L001281](../../agents/web_agent.py#L1281) | 1281 | `"                \"planning_method\": \"general_qa_without_web\","` | — |
| [SRC-1AE03B9EC3-L001282](../../agents/web_agent.py#L1282) | 1282 | `"                \"web_search_skipped\": True,"` | — |
| [SRC-1AE03B9EC3-L001283](../../agents/web_agent.py#L1283) | 1283 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001284](../../agents/web_agent.py#L1284) | 1284 | `"            \"sources\": [],"` | — |
| [SRC-1AE03B9EC3-L001285](../../agents/web_agent.py#L1285) | 1285 | `"            \"used_language_model\": True,"` | — |
| [SRC-1AE03B9EC3-L001286](../../agents/web_agent.py#L1286) | 1286 | `"            \"used_web_search\": False,"` | — |
| [SRC-1AE03B9EC3-L001287](../../agents/web_agent.py#L1287) | 1287 | `"            \"search_attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L001288](../../agents/web_agent.py#L1288) | 1288 | `"            \"used_social_search\": False,"` | — |
| [SRC-1AE03B9EC3-L001289](../../agents/web_agent.py#L1289) | 1289 | `"            \"warnings\": [],"` | — |
| [SRC-1AE03B9EC3-L001290](../../agents/web_agent.py#L1290) | 1290 | `"            \"kind\": \"general_answer\","` | — |
| [SRC-1AE03B9EC3-L001291](../../agents/web_agent.py#L1291) | 1291 | `"            \"research_quality\": \"not_applicable\","` | — |
| [SRC-1AE03B9EC3-L001292](../../agents/web_agent.py#L1292) | 1292 | `"            \"model_calls\": list(self.model_usage),"` | — |
| [SRC-1AE03B9EC3-L001293](../../agents/web_agent.py#L1293) | 1293 | `"        }"` | — |
| [SRC-1AE03B9EC3-L001294](../../agents/web_agent.py#L1294) | 1294 | `""` | — |
| [SRC-1AE03B9EC3-L001295](../../agents/web_agent.py#L1295) | 1295 | `"    def _search_duckduckgo_html(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001296](../../agents/web_agent.py#L1296) | 1296 | `"        import httpx"` | — |
| [SRC-1AE03B9EC3-L001297](../../agents/web_agent.py#L1297) | 1297 | `"        from bs4 import BeautifulSoup"` | — |
| [SRC-1AE03B9EC3-L001298](../../agents/web_agent.py#L1298) | 1298 | `""` | — |
| [SRC-1AE03B9EC3-L001299](../../agents/web_agent.py#L1299) | 1299 | `"        response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001300](../../agents/web_agent.py#L1300) | 1300 | `"            \"https://html.duckduckgo.com/html/\","` | — |
| [SRC-1AE03B9EC3-L001301](../../agents/web_agent.py#L1301) | 1301 | `"            params={\"q\": query},"` | — |
| [SRC-1AE03B9EC3-L001302](../../agents/web_agent.py#L1302) | 1302 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L001303](../../agents/web_agent.py#L1303) | 1303 | `"                \"User-Agent\": ("` | — |
| [SRC-1AE03B9EC3-L001304](../../agents/web_agent.py#L1304) | 1304 | `"                    \"Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 \""` | — |
| [SRC-1AE03B9EC3-L001305](../../agents/web_agent.py#L1305) | 1305 | `"                    \"(KHTML, like Gecko) Chrome/124.0 Mobile Safari/537.36\""` | — |
| [SRC-1AE03B9EC3-L001306](../../agents/web_agent.py#L1306) | 1306 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001307](../../agents/web_agent.py#L1307) | 1307 | `"                \"Accept-Language\": \"ar,en;q=0.9\","` | — |
| [SRC-1AE03B9EC3-L001308](../../agents/web_agent.py#L1308) | 1308 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001309](../../agents/web_agent.py#L1309) | 1309 | `"            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001310](../../agents/web_agent.py#L1310) | 1310 | `"            # Search provider redirects are not followed automatically. A 3xx is"` | — |
| [SRC-1AE03B9EC3-L001311](../../agents/web_agent.py#L1311) | 1311 | `"            # reported as a provider failure so the host never fetches an unchecked target."` | — |
| [SRC-1AE03B9EC3-L001312](../../agents/web_agent.py#L1312) | 1312 | `"            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001313](../../agents/web_agent.py#L1313) | 1313 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001314](../../agents/web_agent.py#L1314) | 1314 | `"        if response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L001315](../../agents/web_agent.py#L1315) | 1315 | `"            raise RuntimeError(f\"HTTP {response.status_code}\")"` | — |
| [SRC-1AE03B9EC3-L001316](../../agents/web_agent.py#L1316) | 1316 | `"        soup = BeautifulSoup(response.text, \"html.parser\")"` | — |
| [SRC-1AE03B9EC3-L001317](../../agents/web_agent.py#L1317) | 1317 | `"        if soup.select_one(\"form#challenge-form, #challenge-form, .anomaly-modal\"):"` | — |
| [SRC-1AE03B9EC3-L001318](../../agents/web_agent.py#L1318) | 1318 | `"            raise RuntimeError(\"anti-bot challenge returned\")"` | — |
| [SRC-1AE03B9EC3-L001319](../../agents/web_agent.py#L1319) | 1319 | `"        rows: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001320](../../agents/web_agent.py#L1320) | 1320 | `"        for card in soup.select(\"div.result\"):"` | — |
| [SRC-1AE03B9EC3-L001321](../../agents/web_agent.py#L1321) | 1321 | `"            link = card.select_one(\"a.result__a\")"` | — |
| [SRC-1AE03B9EC3-L001322](../../agents/web_agent.py#L1322) | 1322 | `"            if not link:"` | — |
| [SRC-1AE03B9EC3-L001323](../../agents/web_agent.py#L1323) | 1323 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001324](../../agents/web_agent.py#L1324) | 1324 | `"            url = _public_http_url(self._unwrap_search_url(str(link.get(\"href\", \"\"))))"` | — |
| [SRC-1AE03B9EC3-L001325](../../agents/web_agent.py#L1325) | 1325 | `"            if not url:"` | — |
| [SRC-1AE03B9EC3-L001326](../../agents/web_agent.py#L1326) | 1326 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001327](../../agents/web_agent.py#L1327) | 1327 | `"            snippet_node = card.select_one(\".result__snippet\")"` | — |
| [SRC-1AE03B9EC3-L001328](../../agents/web_agent.py#L1328) | 1328 | `"            rows.append({"` | — |
| [SRC-1AE03B9EC3-L001329](../../agents/web_agent.py#L1329) | 1329 | `"                \"title\": _clean_text(link.get_text(\" \", strip=True), 300),"` | — |
| [SRC-1AE03B9EC3-L001330](../../agents/web_agent.py#L1330) | 1330 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001331](../../agents/web_agent.py#L1331) | 1331 | `"                \"snippet\": _clean_text("` | — |
| [SRC-1AE03B9EC3-L001332](../../agents/web_agent.py#L1332) | 1332 | `"                    snippet_node.get_text(\" \", strip=True) if snippet_node else \"\", 1200"` | — |
| [SRC-1AE03B9EC3-L001333](../../agents/web_agent.py#L1333) | 1333 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001334](../../agents/web_agent.py#L1334) | 1334 | `"                \"provider\": \"duckduckgo_html\","` | — |
| [SRC-1AE03B9EC3-L001335](../../agents/web_agent.py#L1335) | 1335 | `"                \"provider_rank\": len(rows) + 1,"` | — |
| [SRC-1AE03B9EC3-L001336](../../agents/web_agent.py#L1336) | 1336 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001337](../../agents/web_agent.py#L1337) | 1337 | `"                \"published_at\": \"\","` | — |
| [SRC-1AE03B9EC3-L001338](../../agents/web_agent.py#L1338) | 1338 | `"            })"` | — |
| [SRC-1AE03B9EC3-L001339](../../agents/web_agent.py#L1339) | 1339 | `"            if len(rows) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L001340](../../agents/web_agent.py#L1340) | 1340 | `"                break"` | — |
| [SRC-1AE03B9EC3-L001341](../../agents/web_agent.py#L1341) | 1341 | `"        if not rows and (\"captcha\" in response.text.casefold() or \"anomaly\" in response.text.casefold()):"` | — |
| [SRC-1AE03B9EC3-L001342](../../agents/web_agent.py#L1342) | 1342 | `"            raise RuntimeError(\"anti-bot challenge returned no result cards\")"` | — |
| [SRC-1AE03B9EC3-L001343](../../agents/web_agent.py#L1343) | 1343 | `"        return rows"` | — |
| [SRC-1AE03B9EC3-L001344](../../agents/web_agent.py#L1344) | 1344 | `""` | — |
| [SRC-1AE03B9EC3-L001345](../../agents/web_agent.py#L1345) | 1345 | `"    def _search_bing_rss(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001346](../../agents/web_agent.py#L1346) | 1346 | `"        import xml.etree.ElementTree as ET"` | — |
| [SRC-1AE03B9EC3-L001347](../../agents/web_agent.py#L1347) | 1347 | `""` | — |
| [SRC-1AE03B9EC3-L001348](../../agents/web_agent.py#L1348) | 1348 | `"        import httpx"` | — |
| [SRC-1AE03B9EC3-L001349](../../agents/web_agent.py#L1349) | 1349 | `""` | — |
| [SRC-1AE03B9EC3-L001350](../../agents/web_agent.py#L1350) | 1350 | `"        response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001351](../../agents/web_agent.py#L1351) | 1351 | `"            \"https://www.bing.com/search\","` | — |
| [SRC-1AE03B9EC3-L001352](../../agents/web_agent.py#L1352) | 1352 | `"            params={\"format\": \"rss\", \"q\": query},"` | — |
| [SRC-1AE03B9EC3-L001353](../../agents/web_agent.py#L1353) | 1353 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L001354](../../agents/web_agent.py#L1354) | 1354 | `"                \"User-Agent\": ("` | — |
| [SRC-1AE03B9EC3-L001355](../../agents/web_agent.py#L1355) | 1355 | `"                    \"Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 \""` | — |
| [SRC-1AE03B9EC3-L001356](../../agents/web_agent.py#L1356) | 1356 | `"                    \"(KHTML, like Gecko) Chrome/124.0 Mobile Safari/537.36\""` | — |
| [SRC-1AE03B9EC3-L001357](../../agents/web_agent.py#L1357) | 1357 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001358](../../agents/web_agent.py#L1358) | 1358 | `"                \"Accept-Language\": \"ar,en;q=0.9\","` | — |
| [SRC-1AE03B9EC3-L001359](../../agents/web_agent.py#L1359) | 1359 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001360](../../agents/web_agent.py#L1360) | 1360 | `"            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001361](../../agents/web_agent.py#L1361) | 1361 | `"            # Refuse automatic redirects from public search endpoints; never fetch an"` | — |
| [SRC-1AE03B9EC3-L001362](../../agents/web_agent.py#L1362) | 1362 | `"            # unchecked redirect target as part of a provider search request."` | — |
| [SRC-1AE03B9EC3-L001363](../../agents/web_agent.py#L1363) | 1363 | `"            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001364](../../agents/web_agent.py#L1364) | 1364 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001365](../../agents/web_agent.py#L1365) | 1365 | `"        if response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L001366](../../agents/web_agent.py#L1366) | 1366 | `"            raise RuntimeError(f\"HTTP {response.status_code}\")"` | — |
| [SRC-1AE03B9EC3-L001367](../../agents/web_agent.py#L1367) | 1367 | `"        root = ET.fromstring(response.content)"` | — |
| [SRC-1AE03B9EC3-L001368](../../agents/web_agent.py#L1368) | 1368 | `"        rows: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001369](../../agents/web_agent.py#L1369) | 1369 | `"        for item in root.iter():"` | — |
| [SRC-1AE03B9EC3-L001370](../../agents/web_agent.py#L1370) | 1370 | `"            if item.tag.rsplit(\"}\", 1)[-1] != \"item\":"` | — |
| [SRC-1AE03B9EC3-L001371](../../agents/web_agent.py#L1371) | 1371 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001372](../../agents/web_agent.py#L1372) | 1372 | `"            fields = {"` | — |
| [SRC-1AE03B9EC3-L001373](../../agents/web_agent.py#L1373) | 1373 | `"                child.tag.rsplit(\"}\", 1)[-1]: (child.text or \"\")"` | — |
| [SRC-1AE03B9EC3-L001374](../../agents/web_agent.py#L1374) | 1374 | `"                for child in item"` | — |
| [SRC-1AE03B9EC3-L001375](../../agents/web_agent.py#L1375) | 1375 | `"            }"` | — |
| [SRC-1AE03B9EC3-L001376](../../agents/web_agent.py#L1376) | 1376 | `"            url = _public_http_url(fields.get(\"link\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001377](../../agents/web_agent.py#L1377) | 1377 | `"            if not url:"` | — |
| [SRC-1AE03B9EC3-L001378](../../agents/web_agent.py#L1378) | 1378 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001379](../../agents/web_agent.py#L1379) | 1379 | `"            rows.append({"` | — |
| [SRC-1AE03B9EC3-L001380](../../agents/web_agent.py#L1380) | 1380 | `"                \"title\": _clean_text(fields.get(\"title\", \"\"), 300),"` | — |
| [SRC-1AE03B9EC3-L001381](../../agents/web_agent.py#L1381) | 1381 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001382](../../agents/web_agent.py#L1382) | 1382 | `"                \"snippet\": _clean_text(fields.get(\"description\", \"\"), 1200),"` | — |
| [SRC-1AE03B9EC3-L001383](../../agents/web_agent.py#L1383) | 1383 | `"                \"provider\": \"bing_rss\","` | — |
| [SRC-1AE03B9EC3-L001384](../../agents/web_agent.py#L1384) | 1384 | `"                \"provider_rank\": len(rows) + 1,"` | — |
| [SRC-1AE03B9EC3-L001385](../../agents/web_agent.py#L1385) | 1385 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001386](../../agents/web_agent.py#L1386) | 1386 | `"                \"published_at\": _clean_text(fields.get(\"pubDate\", \"\"), 80),"` | — |
| [SRC-1AE03B9EC3-L001387](../../agents/web_agent.py#L1387) | 1387 | `"            })"` | — |
| [SRC-1AE03B9EC3-L001388](../../agents/web_agent.py#L1388) | 1388 | `"            if len(rows) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L001389](../../agents/web_agent.py#L1389) | 1389 | `"                break"` | — |
| [SRC-1AE03B9EC3-L001390](../../agents/web_agent.py#L1390) | 1390 | `"        return rows"` | — |
| [SRC-1AE03B9EC3-L001391](../../agents/web_agent.py#L1391) | 1391 | `""` | — |
| [SRC-1AE03B9EC3-L001392](../../agents/web_agent.py#L1392) | 1392 | `"    def _search_deepseek_api(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001393](../../agents/web_agent.py#L1393) | 1393 | `"        \"\"\"Use DeepSeek's optional Search API as a comparison provider, never by default.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001394](../../agents/web_agent.py#L1394) | 1394 | `"        api_key = os.getenv(\"DEEPSEEK_SEARCH_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L001395](../../agents/web_agent.py#L1395) | 1395 | `"        if not api_key:"` | — |
| [SRC-1AE03B9EC3-L001396](../../agents/web_agent.py#L1396) | 1396 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L001397](../../agents/web_agent.py#L1397) | 1397 | `"        import httpx"` | — |
| [SRC-1AE03B9EC3-L001398](../../agents/web_agent.py#L1398) | 1398 | `""` | — |
| [SRC-1AE03B9EC3-L001399](../../agents/web_agent.py#L1399) | 1399 | `"        response = httpx.post("` | — |
| [SRC-1AE03B9EC3-L001400](../../agents/web_agent.py#L1400) | 1400 | `"            \"https://api.deepseek.com/v1/tools/search\","` | — |
| [SRC-1AE03B9EC3-L001401](../../agents/web_agent.py#L1401) | 1401 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L001402](../../agents/web_agent.py#L1402) | 1402 | `"                \"Authorization\": \"Bearer \" + api_key,"` | — |
| [SRC-1AE03B9EC3-L001403](../../agents/web_agent.py#L1403) | 1403 | `"                \"Content-Type\": \"application/json\","` | — |
| [SRC-1AE03B9EC3-L001404](../../agents/web_agent.py#L1404) | 1404 | `"                \"Accept\": \"application/json\","` | — |
| [SRC-1AE03B9EC3-L001405](../../agents/web_agent.py#L1405) | 1405 | `"                \"User-Agent\": \"OmaraiResearchAgent/1.0\","` | — |
| [SRC-1AE03B9EC3-L001406](../../agents/web_agent.py#L1406) | 1406 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001407](../../agents/web_agent.py#L1407) | 1407 | `"            json={"` | — |
| [SRC-1AE03B9EC3-L001408](../../agents/web_agent.py#L1408) | 1408 | `"                \"query\": _normalize_search_query(query)[:128] or \"public web search\","` | — |
| [SRC-1AE03B9EC3-L001409](../../agents/web_agent.py#L1409) | 1409 | `"                \"count\": min(MAX_PROVIDER_RESULTS, 10),"` | — |
| [SRC-1AE03B9EC3-L001410](../../agents/web_agent.py#L1410) | 1410 | `"                \"need_content\": False,"` | — |
| [SRC-1AE03B9EC3-L001411](../../agents/web_agent.py#L1411) | 1411 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001412](../../agents/web_agent.py#L1412) | 1412 | `"            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001413](../../agents/web_agent.py#L1413) | 1413 | `"            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001414](../../agents/web_agent.py#L1414) | 1414 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001415](../../agents/web_agent.py#L1415) | 1415 | `"        response.raise_for_status()"` | — |
| [SRC-1AE03B9EC3-L001416](../../agents/web_agent.py#L1416) | 1416 | `"        payload = response.json()"` | — |
| [SRC-1AE03B9EC3-L001417](../../agents/web_agent.py#L1417) | 1417 | `"        results = payload.get(\"results\", []) if isinstance(payload, dict) else []"` | — |
| [SRC-1AE03B9EC3-L001418](../../agents/web_agent.py#L1418) | 1418 | `"        rows: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001419](../../agents/web_agent.py#L1419) | 1419 | `"        for item in results if isinstance(results, list) else []:"` | — |
| [SRC-1AE03B9EC3-L001420](../../agents/web_agent.py#L1420) | 1420 | `"            if not isinstance(item, dict):"` | — |
| [SRC-1AE03B9EC3-L001421](../../agents/web_agent.py#L1421) | 1421 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001422](../../agents/web_agent.py#L1422) | 1422 | `"            url = _public_http_url(item.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001423](../../agents/web_agent.py#L1423) | 1423 | `"            if not url or _blocked_source_url(url):"` | — |
| [SRC-1AE03B9EC3-L001424](../../agents/web_agent.py#L1424) | 1424 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001425](../../agents/web_agent.py#L1425) | 1425 | `"            title = _clean_text(item.get(\"title\", \"\"), 300)"` | — |
| [SRC-1AE03B9EC3-L001426](../../agents/web_agent.py#L1426) | 1426 | `"            summary = item.get(\"summary\", \"\")"` | — |
| [SRC-1AE03B9EC3-L001427](../../agents/web_agent.py#L1427) | 1427 | `"            snippet = item.get(\"snippet\", \"\")"` | — |
| [SRC-1AE03B9EC3-L001428](../../agents/web_agent.py#L1428) | 1428 | `"            if isinstance(summary, str) and summary.strip():"` | — |
| [SRC-1AE03B9EC3-L001429](../../agents/web_agent.py#L1429) | 1429 | `"                snippet = summary"` | — |
| [SRC-1AE03B9EC3-L001430](../../agents/web_agent.py#L1430) | 1430 | `"            if not title or not isinstance(snippet, str) or not snippet.strip():"` | — |
| [SRC-1AE03B9EC3-L001431](../../agents/web_agent.py#L1431) | 1431 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001432](../../agents/web_agent.py#L1432) | 1432 | `"            rows.append({"` | — |
| [SRC-1AE03B9EC3-L001433](../../agents/web_agent.py#L1433) | 1433 | `"                \"title\": title,"` | — |
| [SRC-1AE03B9EC3-L001434](../../agents/web_agent.py#L1434) | 1434 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001435](../../agents/web_agent.py#L1435) | 1435 | `"                \"snippet\": _clean_text(snippet, 1600),"` | — |
| [SRC-1AE03B9EC3-L001436](../../agents/web_agent.py#L1436) | 1436 | `"                \"provider\": \"deepseek_search_api\","` | — |
| [SRC-1AE03B9EC3-L001437](../../agents/web_agent.py#L1437) | 1437 | `"                \"provider_rank\": len(rows) + 1,"` | — |
| [SRC-1AE03B9EC3-L001438](../../agents/web_agent.py#L1438) | 1438 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001439](../../agents/web_agent.py#L1439) | 1439 | `"                \"published_at\": _clean_text(item.get(\"date\", \"\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L001440](../../agents/web_agent.py#L1440) | 1440 | `"                \"publisher_name\": _clean_text(item.get(\"site_name\", \"\") or \"\", 200),"` | — |
| [SRC-1AE03B9EC3-L001441](../../agents/web_agent.py#L1441) | 1441 | `"                \"provider_rerank_score\": item.get(\"rerank_score\"),"` | — |
| [SRC-1AE03B9EC3-L001442](../../agents/web_agent.py#L1442) | 1442 | `"                \"provider_authority_tier\": item.get(\"authority\"),"` | — |
| [SRC-1AE03B9EC3-L001443](../../agents/web_agent.py#L1443) | 1443 | `"            })"` | — |
| [SRC-1AE03B9EC3-L001444](../../agents/web_agent.py#L1444) | 1444 | `"            if len(rows) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L001445](../../agents/web_agent.py#L1445) | 1445 | `"                break"` | — |
| [SRC-1AE03B9EC3-L001446](../../agents/web_agent.py#L1446) | 1446 | `"        return rows"` | — |
| [SRC-1AE03B9EC3-L001447](../../agents/web_agent.py#L1447) | 1447 | `""` | — |
| [SRC-1AE03B9EC3-L001448](../../agents/web_agent.py#L1448) | 1448 | `"    def _reset_deepseek_search_budget(self) -> None:"` | — |
| [SRC-1AE03B9EC3-L001449](../../agents/web_agent.py#L1449) | 1449 | `"        \"\"\"Reset the bounded optional Search API request budget for one operation.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001450](../../agents/web_agent.py#L1450) | 1450 | `"        with self._deepseek_budget_lock:"` | — |
| [SRC-1AE03B9EC3-L001451](../../agents/web_agent.py#L1451) | 1451 | `"            self._deepseek_search_requests_reserved = 0"` | — |
| [SRC-1AE03B9EC3-L001452](../../agents/web_agent.py#L1452) | 1452 | `""` | — |
| [SRC-1AE03B9EC3-L001453](../../agents/web_agent.py#L1453) | 1453 | `"    def _reserve_deepseek_search_request(self) -> bool:"` | — |
| [SRC-1AE03B9EC3-L001454](../../agents/web_agent.py#L1454) | 1454 | `"        \"\"\"Reserve one paid search request before concurrent queries invoke the provider.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001455](../../agents/web_agent.py#L1455) | 1455 | `"        if not os.getenv(\"DEEPSEEK_SEARCH_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L001456](../../agents/web_agent.py#L1456) | 1456 | `"            return False"` | — |
| [SRC-1AE03B9EC3-L001457](../../agents/web_agent.py#L1457) | 1457 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L001458](../../agents/web_agent.py#L1458) | 1458 | `"            configured_budget = int("` | — |
| [SRC-1AE03B9EC3-L001459](../../agents/web_agent.py#L1459) | 1459 | `"                os.getenv(\"OMARAI_DEEPSEEK_SEARCH_REQUEST_BUDGET\", \"1\").strip()"` | — |
| [SRC-1AE03B9EC3-L001460](../../agents/web_agent.py#L1460) | 1460 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001461](../../agents/web_agent.py#L1461) | 1461 | `"        except ValueError:"` | — |
| [SRC-1AE03B9EC3-L001462](../../agents/web_agent.py#L1462) | 1462 | `"            configured_budget = 1"` | — |
| [SRC-1AE03B9EC3-L001463](../../agents/web_agent.py#L1463) | 1463 | `"        budget = max(0, min(configured_budget, 3))"` | — |
| [SRC-1AE03B9EC3-L001464](../../agents/web_agent.py#L1464) | 1464 | `"        with self._deepseek_budget_lock:"` | — |
| [SRC-1AE03B9EC3-L001465](../../agents/web_agent.py#L1465) | 1465 | `"            if self._deepseek_search_requests_reserved >= budget:"` | — |
| [SRC-1AE03B9EC3-L001466](../../agents/web_agent.py#L1466) | 1466 | `"                return False"` | — |
| [SRC-1AE03B9EC3-L001467](../../agents/web_agent.py#L1467) | 1467 | `"            self._deepseek_search_requests_reserved += 1"` | — |
| [SRC-1AE03B9EC3-L001468](../../agents/web_agent.py#L1468) | 1468 | `"            return True"` | — |
| [SRC-1AE03B9EC3-L001469](../../agents/web_agent.py#L1469) | 1469 | `""` | — |
| [SRC-1AE03B9EC3-L001470](../../agents/web_agent.py#L1470) | 1470 | `"    def _search_web(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001471](../../agents/web_agent.py#L1471) | 1471 | `"        \"\"\"Run configured search connectors concurrently with isolated failures and relevance checks.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001472](../../agents/web_agent.py#L1472) | 1472 | `"        from agents.research import detect_freshness"` | — |
| [SRC-1AE03B9EC3-L001473](../../agents/web_agent.py#L1473) | 1473 | `""` | — |
| [SRC-1AE03B9EC3-L001474](../../agents/web_agent.py#L1474) | 1474 | `"        query = compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L001475](../../agents/web_agent.py#L1475) | 1475 | `"        if not query:"` | — |
| [SRC-1AE03B9EC3-L001476](../../agents/web_agent.py#L1476) | 1476 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L001477](../../agents/web_agent.py#L1477) | 1477 | `"        search_query = _normalize_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L001478](../../agents/web_agent.py#L1478) | 1478 | `"        budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L001479](../../agents/web_agent.py#L1479) | 1479 | `"        if budget is not None:"` | — |
| [SRC-1AE03B9EC3-L001480](../../agents/web_agent.py#L1480) | 1480 | `"            budget.reserve(\"search_queries\")"` | — |
| [SRC-1AE03B9EC3-L001481](../../agents/web_agent.py#L1481) | 1481 | `"        adapters: list[tuple[str, Any]] = ["` | — |
| [SRC-1AE03B9EC3-L001482](../../agents/web_agent.py#L1482) | 1482 | `"            (\"duckduckgo_html\", self._search_duckduckgo_html),"` | — |
| [SRC-1AE03B9EC3-L001483](../../agents/web_agent.py#L1483) | 1483 | `"            (\"bing_rss\", self._search_bing_rss),"` | — |
| [SRC-1AE03B9EC3-L001484](../../agents/web_agent.py#L1484) | 1484 | `"        ]"` | — |
| [SRC-1AE03B9EC3-L001485](../../agents/web_agent.py#L1485) | 1485 | `"        # Experimental opt-in only: DeepSeek Search is billed per successful request."` | — |
| [SRC-1AE03B9EC3-L001486](../../agents/web_agent.py#L1486) | 1486 | `"        # Do not promote it to primary without a measured comparison."` | — |
| [SRC-1AE03B9EC3-L001487](../../agents/web_agent.py#L1487) | 1487 | `"        if not os.getenv(\"DEEPSEEK_SEARCH_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L001488](../../agents/web_agent.py#L1488) | 1488 | `"            self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001489](../../agents/web_agent.py#L1489) | 1489 | `"                \"deepseek_search_api\", search_query, \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L001490](../../agents/web_agent.py#L1490) | 1490 | `"                error=\"DEEPSEEK_SEARCH_API_KEY is not set\","` | — |
| [SRC-1AE03B9EC3-L001491](../../agents/web_agent.py#L1491) | 1491 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001492](../../agents/web_agent.py#L1492) | 1492 | `"        elif self._reserve_deepseek_search_request():"` | — |
| [SRC-1AE03B9EC3-L001493](../../agents/web_agent.py#L1493) | 1493 | `"            adapters.append((\"deepseek_search_api\", self._search_deepseek_api))"` | — |
| [SRC-1AE03B9EC3-L001494](../../agents/web_agent.py#L1494) | 1494 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L001495](../../agents/web_agent.py#L1495) | 1495 | `"            self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001496](../../agents/web_agent.py#L1496) | 1496 | `"                \"deepseek_search_api\", search_query, \"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L001497](../../agents/web_agent.py#L1497) | 1497 | `"                error=\"per-operation DeepSeek Search request budget exhausted\","` | — |
| [SRC-1AE03B9EC3-L001498](../../agents/web_agent.py#L1498) | 1498 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001499](../../agents/web_agent.py#L1499) | 1499 | `"        if os.getenv(\"BRAVE_SEARCH_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L001500](../../agents/web_agent.py#L1500) | 1500 | `"            adapters.append((\"brave_search_api\", self._search_brave))"` | — |
| [SRC-1AE03B9EC3-L001501](../../agents/web_agent.py#L1501) | 1501 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L001502](../../agents/web_agent.py#L1502) | 1502 | `"            self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001503](../../agents/web_agent.py#L1503) | 1503 | `"                \"brave_search_api\", search_query, \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L001504](../../agents/web_agent.py#L1504) | 1504 | `"                error=\"BRAVE_SEARCH_API_KEY is not set\","` | — |
| [SRC-1AE03B9EC3-L001505](../../agents/web_agent.py#L1505) | 1505 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001506](../../agents/web_agent.py#L1506) | 1506 | `"        if os.getenv(\"TAVILY_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L001507](../../agents/web_agent.py#L1507) | 1507 | `"            adapters.append((\"tavily_search_api\", self._search_tavily))"` | — |
| [SRC-1AE03B9EC3-L001508](../../agents/web_agent.py#L1508) | 1508 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L001509](../../agents/web_agent.py#L1509) | 1509 | `"            self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001510](../../agents/web_agent.py#L1510) | 1510 | `"                \"tavily_search_api\", search_query, \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L001511](../../agents/web_agent.py#L1511) | 1511 | `"                error=\"TAVILY_API_KEY is not set\","` | — |
| [SRC-1AE03B9EC3-L001512](../../agents/web_agent.py#L1512) | 1512 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001513](../../agents/web_agent.py#L1513) | 1513 | `"        if detect_freshness(search_query):"` | — |
| [SRC-1AE03B9EC3-L001514](../../agents/web_agent.py#L1514) | 1514 | `"            adapters.append((\"google_news_rss\", self._search_news))"` | — |
| [SRC-1AE03B9EC3-L001515](../../agents/web_agent.py#L1515) | 1515 | `""` | — |
| [SRC-1AE03B9EC3-L001516](../../agents/web_agent.py#L1516) | 1516 | `"        async def run_one(name: str, method: Any) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001517](../../agents/web_agent.py#L1517) | 1517 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L001518](../../agents/web_agent.py#L1518) | 1518 | `"                if budget is not None:"` | — |
| [SRC-1AE03B9EC3-L001519](../../agents/web_agent.py#L1519) | 1519 | `"                    budget.reserve(\"search_calls\")"` | — |
| [SRC-1AE03B9EC3-L001520](../../agents/web_agent.py#L1520) | 1520 | `"                provider_timeout = self._effective_timeout(10.0)"` | — |
| [SRC-1AE03B9EC3-L001521](../../agents/web_agent.py#L1521) | 1521 | `"                raw = await asyncio.wait_for("` | — |
| [SRC-1AE03B9EC3-L001522](../../agents/web_agent.py#L1522) | 1522 | `"                    asyncio.to_thread(method, search_query), timeout=provider_timeout"` | — |
| [SRC-1AE03B9EC3-L001523](../../agents/web_agent.py#L1523) | 1523 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001524](../../agents/web_agent.py#L1524) | 1524 | `"                if not isinstance(raw, list):"` | — |
| [SRC-1AE03B9EC3-L001525](../../agents/web_agent.py#L1525) | 1525 | `"                    raise TypeError(\"connector returned a non-list result\")"` | — |
| [SRC-1AE03B9EC3-L001526](../../agents/web_agent.py#L1526) | 1526 | `"                accepted: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001527](../../agents/web_agent.py#L1527) | 1527 | `"                rejected = 0"` | — |
| [SRC-1AE03B9EC3-L001528](../../agents/web_agent.py#L1528) | 1528 | `"                rejection_counts = {reason: 0 for reason in _PROVIDER_REJECTION_REASONS}"` | — |
| [SRC-1AE03B9EC3-L001529](../../agents/web_agent.py#L1529) | 1529 | `"                for item in raw:"` | — |
| [SRC-1AE03B9EC3-L001530](../../agents/web_agent.py#L1530) | 1530 | `"                    if not isinstance(item, dict):"` | — |
| [SRC-1AE03B9EC3-L001531](../../agents/web_agent.py#L1531) | 1531 | `"                        rejected += 1"` | — |
| [SRC-1AE03B9EC3-L001532](../../agents/web_agent.py#L1532) | 1532 | `"                        rejection_counts[\"malformed_candidate\"] += 1"` | — |
| [SRC-1AE03B9EC3-L001533](../../agents/web_agent.py#L1533) | 1533 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L001534](../../agents/web_agent.py#L1534) | 1534 | `"                    safe_url = _public_http_url(item.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001535](../../agents/web_agent.py#L1535) | 1535 | `"                    if not safe_url:"` | — |
| [SRC-1AE03B9EC3-L001536](../../agents/web_agent.py#L1536) | 1536 | `"                        rejected += 1"` | — |
| [SRC-1AE03B9EC3-L001537](../../agents/web_agent.py#L1537) | 1537 | `"                        rejection_counts[\"invalid_url_or_unsafe_target\"] += 1"` | — |
| [SRC-1AE03B9EC3-L001538](../../agents/web_agent.py#L1538) | 1538 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L001539](../../agents/web_agent.py#L1539) | 1539 | `"                    if _blocked_source_url(safe_url):"` | — |
| [SRC-1AE03B9EC3-L001540](../../agents/web_agent.py#L1540) | 1540 | `"                        rejected += 1"` | — |
| [SRC-1AE03B9EC3-L001541](../../agents/web_agent.py#L1541) | 1541 | `"                        rejection_counts[\"blocked_domain\"] += 1"` | — |
| [SRC-1AE03B9EC3-L001542](../../agents/web_agent.py#L1542) | 1542 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L001543](../../agents/web_agent.py#L1543) | 1543 | `"                    normalized_item = dict(item)"` | — |
| [SRC-1AE03B9EC3-L001544](../../agents/web_agent.py#L1544) | 1544 | `"                    normalized_item[\"url\"] = safe_url"` | — |
| [SRC-1AE03B9EC3-L001545](../../agents/web_agent.py#L1545) | 1545 | `"                    normalized_item.setdefault(\"provider\", name)"` | — |
| [SRC-1AE03B9EC3-L001546](../../agents/web_agent.py#L1546) | 1546 | `"                    normalized_item.setdefault(\"search_query\", search_query)"` | — |
| [SRC-1AE03B9EC3-L001547](../../agents/web_agent.py#L1547) | 1547 | `"                    evidence = \" \".join(str(normalized_item.get(k) or \"\") for k in (\"title\", \"snippet\"))"` | — |
| [SRC-1AE03B9EC3-L001548](../../agents/web_agent.py#L1548) | 1548 | `"                    if _relevance_ratio(search_query, evidence) < _minimum_relevance_ratio(search_query):"` | — |
| [SRC-1AE03B9EC3-L001549](../../agents/web_agent.py#L1549) | 1549 | `"                        rejected += 1"` | — |
| [SRC-1AE03B9EC3-L001550](../../agents/web_agent.py#L1550) | 1550 | `"                        rejection_counts[\"relevance_below_threshold\"] += 1"` | — |
| [SRC-1AE03B9EC3-L001551](../../agents/web_agent.py#L1551) | 1551 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L001552](../../agents/web_agent.py#L1552) | 1552 | `"                    accepted.append(normalized_item)"` | — |
| [SRC-1AE03B9EC3-L001553](../../agents/web_agent.py#L1553) | 1553 | `"                if accepted:"` | — |
| [SRC-1AE03B9EC3-L001554](../../agents/web_agent.py#L1554) | 1554 | `"                    status = \"ok\""` | — |
| [SRC-1AE03B9EC3-L001555](../../agents/web_agent.py#L1555) | 1555 | `"                    error = None"` | — |
| [SRC-1AE03B9EC3-L001556](../../agents/web_agent.py#L1556) | 1556 | `"                elif raw:"` | — |
| [SRC-1AE03B9EC3-L001557](../../agents/web_agent.py#L1557) | 1557 | `"                    status = \"filtered_all\""` | — |
| [SRC-1AE03B9EC3-L001558](../../agents/web_agent.py#L1558) | 1558 | `"                    details = \", \".join("` | — |
| [SRC-1AE03B9EC3-L001559](../../agents/web_agent.py#L1559) | 1559 | `"                        f\"{reason}={count}\" for reason, count in rejection_counts.items() if count"` | — |
| [SRC-1AE03B9EC3-L001560](../../agents/web_agent.py#L1560) | 1560 | `"                    ) or \"no reason counters recorded\""` | — |
| [SRC-1AE03B9EC3-L001561](../../agents/web_agent.py#L1561) | 1561 | `"                    error = f\"all candidates rejected; {details}\""` | — |
| [SRC-1AE03B9EC3-L001562](../../agents/web_agent.py#L1562) | 1562 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L001563](../../agents/web_agent.py#L1563) | 1563 | `"                    status = \"no_results\""` | — |
| [SRC-1AE03B9EC3-L001564](../../agents/web_agent.py#L1564) | 1564 | `"                    error = \"connector returned no parseable results\""` | — |
| [SRC-1AE03B9EC3-L001565](../../agents/web_agent.py#L1565) | 1565 | `"                self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001566](../../agents/web_agent.py#L1566) | 1566 | `"                    name, search_query, status, len(raw), rejected, error,"` | — |
| [SRC-1AE03B9EC3-L001567](../../agents/web_agent.py#L1567) | 1567 | `"                    accepted_count=len(accepted), rejection_counts=rejection_counts if raw else None,"` | — |
| [SRC-1AE03B9EC3-L001568](../../agents/web_agent.py#L1568) | 1568 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001569](../../agents/web_agent.py#L1569) | 1569 | `"                return accepted"` | — |
| [SRC-1AE03B9EC3-L001570](../../agents/web_agent.py#L1570) | 1570 | `"            except RequestBudgetExceeded as exc:"` | — |
| [SRC-1AE03B9EC3-L001571](../../agents/web_agent.py#L1571) | 1571 | `"                self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001572](../../agents/web_agent.py#L1572) | 1572 | `"                    name, search_query, \"budget_exhausted\", error=str(exc)"` | — |
| [SRC-1AE03B9EC3-L001573](../../agents/web_agent.py#L1573) | 1573 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001574](../../agents/web_agent.py#L1574) | 1574 | `"            except TimeoutError:"` | — |
| [SRC-1AE03B9EC3-L001575](../../agents/web_agent.py#L1575) | 1575 | `"                self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001576](../../agents/web_agent.py#L1576) | 1576 | `"                    name, search_query, \"timeout\", error=\"provider exceeded its bounded request timeout\""` | — |
| [SRC-1AE03B9EC3-L001577](../../agents/web_agent.py#L1577) | 1577 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001578](../../agents/web_agent.py#L1578) | 1578 | `"            except Exception as exc:  # noqa: BLE001 - isolate a connector without leaking provider bodies/secrets"` | — |
| [SRC-1AE03B9EC3-L001579](../../agents/web_agent.py#L1579) | 1579 | `"                detail = f\"{type(exc).__name__}: {exc}\" if isinstance(exc, RuntimeError) else type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L001580](../../agents/web_agent.py#L1580) | 1580 | `"                status = \"failed\""` | — |
| [SRC-1AE03B9EC3-L001581](../../agents/web_agent.py#L1581) | 1581 | `"                status_match = re.search(r\"(?i)\\bHTTP\\s+(\\d{3})\\b\", str(exc))"` | — |
| [SRC-1AE03B9EC3-L001582](../../agents/web_agent.py#L1582) | 1582 | `"                if status_match:"` | — |
| [SRC-1AE03B9EC3-L001583](../../agents/web_agent.py#L1583) | 1583 | `"                    status_code = int(status_match.group(1))"` | — |
| [SRC-1AE03B9EC3-L001584](../../agents/web_agent.py#L1584) | 1584 | `"                    if status_code == 429:"` | — |
| [SRC-1AE03B9EC3-L001585](../../agents/web_agent.py#L1585) | 1585 | `"                        status = \"rate_limited\""` | — |
| [SRC-1AE03B9EC3-L001586](../../agents/web_agent.py#L1586) | 1586 | `"                    elif status_code in {401, 403}:"` | — |
| [SRC-1AE03B9EC3-L001587](../../agents/web_agent.py#L1587) | 1587 | `"                        status = \"unauthorized\""` | — |
| [SRC-1AE03B9EC3-L001588](../../agents/web_agent.py#L1588) | 1588 | `"                    elif status_code == 202 or 300 <= status_code < 600:"` | — |
| [SRC-1AE03B9EC3-L001589](../../agents/web_agent.py#L1589) | 1589 | `"                        # Do not bypass anti-bot/challenge responses; mark the provider degraded."` | — |
| [SRC-1AE03B9EC3-L001590](../../agents/web_agent.py#L1590) | 1590 | `"                        status = \"http_error\""` | — |
| [SRC-1AE03B9EC3-L001591](../../agents/web_agent.py#L1591) | 1591 | `"                self._record_provider_diagnostic(name, search_query, status, error=detail)"` | — |
| [SRC-1AE03B9EC3-L001592](../../agents/web_agent.py#L1592) | 1592 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L001593](../../agents/web_agent.py#L1593) | 1593 | `""` | — |
| [SRC-1AE03B9EC3-L001594](../../agents/web_agent.py#L1594) | 1594 | `"        async def run_all() -> list[list[dict[str, Any]]]:"` | — |
| [SRC-1AE03B9EC3-L001595](../../agents/web_agent.py#L1595) | 1595 | `"            return await asyncio.gather(*(run_one(name, method) for name, method in adapters))"` | — |
| [SRC-1AE03B9EC3-L001596](../../agents/web_agent.py#L1596) | 1596 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L001597](../../agents/web_agent.py#L1597) | 1597 | `"            provider_batches = asyncio.run(run_all())"` | — |
| [SRC-1AE03B9EC3-L001598](../../agents/web_agent.py#L1598) | 1598 | `"            combined = [item for batch in provider_batches for item in batch]"` | — |
| [SRC-1AE03B9EC3-L001599](../../agents/web_agent.py#L1599) | 1599 | `"            # Scholarly fallback only for explicit research-shaped queries; reuse"` | — |
| [SRC-1AE03B9EC3-L001600](../../agents/web_agent.py#L1600) | 1600 | `"            # run_one so budget, timeouts, public-URL/SSRF, blocklist and relevance"` | — |
| [SRC-1AE03B9EC3-L001601](../../agents/web_agent.py#L1601) | 1601 | `"            # validation are identical to ordinary search connectors."` | — |
| [SRC-1AE03B9EC3-L001602](../../agents/web_agent.py#L1602) | 1602 | `"            academic_markers = ("` | — |
| [SRC-1AE03B9EC3-L001603](../../agents/web_agent.py#L1603) | 1603 | `"                \"دراسة علمية\", \"دراسات\", \"ابحاث\", \"أبحاث\", \"بحث علمي\","` | — |
| [SRC-1AE03B9EC3-L001604](../../agents/web_agent.py#L1604) | 1604 | `"                \"ورقة علمية\", \"أوراق علمية\", \"academic\", \"research\","` | — |
| [SRC-1AE03B9EC3-L001605](../../agents/web_agent.py#L1605) | 1605 | `"                \"scientific study\", \"research paper\", \"peer reviewed\","` | — |
| [SRC-1AE03B9EC3-L001606](../../agents/web_agent.py#L1606) | 1606 | `"                \"peer-reviewed\", \"scholarly\", \"literature review\","` | — |
| [SRC-1AE03B9EC3-L001607](../../agents/web_agent.py#L1607) | 1607 | `"                \"systematic review\", \"arxiv\", \"openalex\", \"crossref\","` | — |
| [SRC-1AE03B9EC3-L001608](../../agents/web_agent.py#L1608) | 1608 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001609](../../agents/web_agent.py#L1609) | 1609 | `"            if len(combined) < 3 and any(marker in search_query.casefold() for marker in academic_markers):"` | — |
| [SRC-1AE03B9EC3-L001610](../../agents/web_agent.py#L1610) | 1610 | `"                academic_adapters: list[tuple[str, Any]] = ["` | — |
| [SRC-1AE03B9EC3-L001611](../../agents/web_agent.py#L1611) | 1611 | `"                    (\"openalex\", lambda q: search_openalex(q, limit=3)),"` | — |
| [SRC-1AE03B9EC3-L001612](../../agents/web_agent.py#L1612) | 1612 | `"                    (\"arxiv\", lambda q: search_arxiv(q, limit=3)),"` | — |
| [SRC-1AE03B9EC3-L001613](../../agents/web_agent.py#L1613) | 1613 | `"                    (\"crossref\", lambda q: search_crossref(q, limit=3)),"` | — |
| [SRC-1AE03B9EC3-L001614](../../agents/web_agent.py#L1614) | 1614 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L001615](../../agents/web_agent.py#L1615) | 1615 | `""` | — |
| [SRC-1AE03B9EC3-L001616](../../agents/web_agent.py#L1616) | 1616 | `"                async def run_academic_all() -> list[list[dict[str, Any]]]:"` | — |
| [SRC-1AE03B9EC3-L001617](../../agents/web_agent.py#L1617) | 1617 | `"                    return await asyncio.gather("` | — |
| [SRC-1AE03B9EC3-L001618](../../agents/web_agent.py#L1618) | 1618 | `"                        *(run_one(name, method) for name, method in academic_adapters)"` | — |
| [SRC-1AE03B9EC3-L001619](../../agents/web_agent.py#L1619) | 1619 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L001620](../../agents/web_agent.py#L1620) | 1620 | `""` | — |
| [SRC-1AE03B9EC3-L001621](../../agents/web_agent.py#L1621) | 1621 | `"                provider_batches.extend(asyncio.run(run_academic_all()))"` | — |
| [SRC-1AE03B9EC3-L001622](../../agents/web_agent.py#L1622) | 1622 | `"        except RuntimeError as exc:"` | — |
| [SRC-1AE03B9EC3-L001623](../../agents/web_agent.py#L1623) | 1623 | `"            # This method is synchronous by contract; the HTTP server invokes it in worker threads."` | — |
| [SRC-1AE03B9EC3-L001624](../../agents/web_agent.py#L1624) | 1624 | `"            raise RuntimeError(\"تعذر تشغيل مجدول موصلات البحث.\") from exc"` | — |
| [SRC-1AE03B9EC3-L001625](../../agents/web_agent.py#L1625) | 1625 | `"        combined = [item for batch in provider_batches for item in batch]"` | — |
| [SRC-1AE03B9EC3-L001626](../../agents/web_agent.py#L1626) | 1626 | `"        # De-duplicate repeated URLs before ranking/fusion."` | — |
| [SRC-1AE03B9EC3-L001627](../../agents/web_agent.py#L1627) | 1627 | `"        unique: dict[str, dict[str, Any]] = {}"` | — |
| [SRC-1AE03B9EC3-L001628](../../agents/web_agent.py#L1628) | 1628 | `"        for item in combined:"` | — |
| [SRC-1AE03B9EC3-L001629](../../agents/web_agent.py#L1629) | 1629 | `"            key = item[\"url\"].split(\"#\", 1)[0].rstrip(\"/\")"` | — |
| [SRC-1AE03B9EC3-L001630](../../agents/web_agent.py#L1630) | 1630 | `"            if key not in unique or len(str(item.get(\"snippet\") or \"\")) > len(str(unique[key].get(\"snippet\") or \"\")):"` | — |
| [SRC-1AE03B9EC3-L001631](../../agents/web_agent.py#L1631) | 1631 | `"                unique[key] = item"` | — |
| [SRC-1AE03B9EC3-L001632](../../agents/web_agent.py#L1632) | 1632 | `"        if not unique:"` | — |
| [SRC-1AE03B9EC3-L001633](../../agents/web_agent.py#L1633) | 1633 | `"            raise RuntimeError(\"لم تُرجع موصلات البحث نتائج مرتبطة وقابلة للاستخدام.\")"` | — |
| [SRC-1AE03B9EC3-L001634](../../agents/web_agent.py#L1634) | 1634 | `"        return list(unique.values())"` | — |
| [SRC-1AE03B9EC3-L001635](../../agents/web_agent.py#L1635) | 1635 | `""` | — |
| [SRC-1AE03B9EC3-L001636](../../agents/web_agent.py#L1636) | 1636 | `"    def _reserve_search_call(self) -> None:"` | — |
| [SRC-1AE03B9EC3-L001637](../../agents/web_agent.py#L1637) | 1637 | `"        \"\"\"Reserve one outbound search/social-provider request before network I/O.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001638](../../agents/web_agent.py#L1638) | 1638 | `"        budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L001639](../../agents/web_agent.py#L1639) | 1639 | `"        if budget is not None:"` | — |
| [SRC-1AE03B9EC3-L001640](../../agents/web_agent.py#L1640) | 1640 | `"            budget.reserve(\"search_calls\")"` | — |
| [SRC-1AE03B9EC3-L001641](../../agents/web_agent.py#L1641) | 1641 | `""` | — |
| [SRC-1AE03B9EC3-L001642](../../agents/web_agent.py#L1642) | 1642 | `"    def _search_brave(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001643](../../agents/web_agent.py#L1643) | 1643 | `"        \"\"\"Use Brave's official web-search API when the operator provides an API key.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001644](../../agents/web_agent.py#L1644) | 1644 | `"        api_key = os.getenv(\"BRAVE_SEARCH_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L001645](../../agents/web_agent.py#L1645) | 1645 | `"        if not api_key:"` | — |
| [SRC-1AE03B9EC3-L001646](../../agents/web_agent.py#L1646) | 1646 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L001647](../../agents/web_agent.py#L1647) | 1647 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L001648](../../agents/web_agent.py#L1648) | 1648 | `"            import httpx"` | — |
| [SRC-1AE03B9EC3-L001649](../../agents/web_agent.py#L1649) | 1649 | `"        except ImportError as exc:"` | — |
| [SRC-1AE03B9EC3-L001650](../../agents/web_agent.py#L1650) | 1650 | `"            raise AgentDependencyError(\"حزمة httpx غير مثبتة.\") from exc"` | — |
| [SRC-1AE03B9EC3-L001651](../../agents/web_agent.py#L1651) | 1651 | `"        is_arabic = bool(re.search(r\"[\\u0600-\\u06FF]\", query))"` | — |
| [SRC-1AE03B9EC3-L001652](../../agents/web_agent.py#L1652) | 1652 | `"        response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001653](../../agents/web_agent.py#L1653) | 1653 | `"            \"https://api.search.brave.com/res/v1/web/search\","` | — |
| [SRC-1AE03B9EC3-L001654](../../agents/web_agent.py#L1654) | 1654 | `"            params={"` | — |
| [SRC-1AE03B9EC3-L001655](../../agents/web_agent.py#L1655) | 1655 | `"                \"q\": query[:600],"` | — |
| [SRC-1AE03B9EC3-L001656](../../agents/web_agent.py#L1656) | 1656 | `"                \"count\": MAX_PROVIDER_RESULTS,"` | — |
| [SRC-1AE03B9EC3-L001657](../../agents/web_agent.py#L1657) | 1657 | `"                \"country\": \"EG\" if is_arabic else \"US\","` | — |
| [SRC-1AE03B9EC3-L001658](../../agents/web_agent.py#L1658) | 1658 | `"                \"search_lang\": \"ar\" if is_arabic else \"en\","` | — |
| [SRC-1AE03B9EC3-L001659](../../agents/web_agent.py#L1659) | 1659 | `"                \"extra_snippets\": \"true\","` | — |
| [SRC-1AE03B9EC3-L001660](../../agents/web_agent.py#L1660) | 1660 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001661](../../agents/web_agent.py#L1661) | 1661 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L001662](../../agents/web_agent.py#L1662) | 1662 | `"                \"Accept\": \"application/json\","` | — |
| [SRC-1AE03B9EC3-L001663](../../agents/web_agent.py#L1663) | 1663 | `"                \"X-Subscription-Token\": api_key,"` | — |
| [SRC-1AE03B9EC3-L001664](../../agents/web_agent.py#L1664) | 1664 | `"                \"User-Agent\": \"OmaraiResearchAgent/1.0\","` | — |
| [SRC-1AE03B9EC3-L001665](../../agents/web_agent.py#L1665) | 1665 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001666](../../agents/web_agent.py#L1666) | 1666 | `"            timeout=self._effective_timeout(8.5),"` | — |
| [SRC-1AE03B9EC3-L001667](../../agents/web_agent.py#L1667) | 1667 | `"            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001668](../../agents/web_agent.py#L1668) | 1668 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001669](../../agents/web_agent.py#L1669) | 1669 | `"        response.raise_for_status()"` | — |
| [SRC-1AE03B9EC3-L001670](../../agents/web_agent.py#L1670) | 1670 | `"        payload = response.json()"` | — |
| [SRC-1AE03B9EC3-L001671](../../agents/web_agent.py#L1671) | 1671 | `"        web_results = payload.get(\"web\", {}).get(\"results\", [])"` | — |
| [SRC-1AE03B9EC3-L001672](../../agents/web_agent.py#L1672) | 1672 | `"        rows: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001673](../../agents/web_agent.py#L1673) | 1673 | `"        for item in web_results if isinstance(web_results, list) else []:"` | — |
| [SRC-1AE03B9EC3-L001674](../../agents/web_agent.py#L1674) | 1674 | `"            if not isinstance(item, dict):"` | — |
| [SRC-1AE03B9EC3-L001675](../../agents/web_agent.py#L1675) | 1675 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001676](../../agents/web_agent.py#L1676) | 1676 | `"            url = _public_http_url(item.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001677](../../agents/web_agent.py#L1677) | 1677 | `"            if not url:"` | — |
| [SRC-1AE03B9EC3-L001678](../../agents/web_agent.py#L1678) | 1678 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001679](../../agents/web_agent.py#L1679) | 1679 | `"            snippets = item.get(\"extra_snippets\", [])"` | — |
| [SRC-1AE03B9EC3-L001680](../../agents/web_agent.py#L1680) | 1680 | `"            extra = \" \".join(x for x in snippets if isinstance(x, str)) if isinstance(snippets, list) else \"\""` | — |
| [SRC-1AE03B9EC3-L001681](../../agents/web_agent.py#L1681) | 1681 | `"            rows.append({"` | — |
| [SRC-1AE03B9EC3-L001682](../../agents/web_agent.py#L1682) | 1682 | `"                \"title\": _clean_text(item.get(\"title\", \"\"), 300),"` | — |
| [SRC-1AE03B9EC3-L001683](../../agents/web_agent.py#L1683) | 1683 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001684](../../agents/web_agent.py#L1684) | 1684 | `"                \"snippet\": _clean_text(item.get(\"description\", \"\") + \" \" + extra, 1600),"` | — |
| [SRC-1AE03B9EC3-L001685](../../agents/web_agent.py#L1685) | 1685 | `"                \"provider\": \"brave_search_api\","` | — |
| [SRC-1AE03B9EC3-L001686](../../agents/web_agent.py#L1686) | 1686 | `"                \"provider_rank\": len(rows) + 1,"` | — |
| [SRC-1AE03B9EC3-L001687](../../agents/web_agent.py#L1687) | 1687 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001688](../../agents/web_agent.py#L1688) | 1688 | `"                \"published_at\": _clean_text(item.get(\"page_age\", \"\") or item.get(\"published_at\", \"\"), 100),"` | — |
| [SRC-1AE03B9EC3-L001689](../../agents/web_agent.py#L1689) | 1689 | `"            })"` | — |
| [SRC-1AE03B9EC3-L001690](../../agents/web_agent.py#L1690) | 1690 | `"            if len(rows) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L001691](../../agents/web_agent.py#L1691) | 1691 | `"                break"` | — |
| [SRC-1AE03B9EC3-L001692](../../agents/web_agent.py#L1692) | 1692 | `"        return rows"` | — |
| [SRC-1AE03B9EC3-L001693](../../agents/web_agent.py#L1693) | 1693 | `""` | — |
| [SRC-1AE03B9EC3-L001694](../../agents/web_agent.py#L1694) | 1694 | `"    def _search_tavily(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001695](../../agents/web_agent.py#L1695) | 1695 | `"        \"\"\"Use Tavily's official search API for structured, extractable live web results.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001696](../../agents/web_agent.py#L1696) | 1696 | `"        api_key = os.getenv(\"TAVILY_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L001697](../../agents/web_agent.py#L1697) | 1697 | `"        if not api_key:"` | — |
| [SRC-1AE03B9EC3-L001698](../../agents/web_agent.py#L1698) | 1698 | `"            return []"` | — |
