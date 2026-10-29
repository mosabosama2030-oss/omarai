# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **045**
- سجلات الأسطر: **800**
- النطاق: SRC-F725E90B2A-L002979 إلى SRC-F725E90B2A-L003778
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-F725E90B2A — [tests/test_web_agent.py](../../tests/test_web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-F725E90B2A-L002979](../../tests/test_web_agent.py#L2979) | 2979 | `"            \"ما أحدث التطورات في وكلاء الذكاء الاصطناعي خلال الأيام السبعة الماضية؟ اذكر تواريخ الأخبار وروابط المصادر، ولا تعرض معلومات قديمة باعتبارها جديدة.\","` | — |
| [SRC-F725E90B2A-L002980](../../tests/test_web_agent.py#L2980) | 2980 | `"            \"Recent developments in AI agents\","` | — |
| [SRC-F725E90B2A-L002981](../../tests/test_web_agent.py#L2981) | 2981 | `"            \"New AI agent tools and launches this week.\","` | — |
| [SRC-F725E90B2A-L002982](../../tests/test_web_agent.py#L2982) | 2982 | `"        ),"` | — |
| [SRC-F725E90B2A-L002983](../../tests/test_web_agent.py#L2983) | 2983 | `"        ("` | — |
| [SRC-F725E90B2A-L002984](../../tests/test_web_agent.py#L2984) | 2984 | `"            \"اجمع آراء وتجارب المستخدمين العامة حول السيارات الكهربائية في مصر. اعرض الآراء الإيجابية والسلبية، واذكر روابط المنشورات أو المصادر المتاحة.\","` | — |
| [SRC-F725E90B2A-L002985](../../tests/test_web_agent.py#L2985) | 2985 | `"            \"Reddit users share electric car experiences in Egypt\","` | — |
| [SRC-F725E90B2A-L002986](../../tests/test_web_agent.py#L2986) | 2986 | `"            \"Owners discuss electric vehicles, charging and daily use.\","` | — |
| [SRC-F725E90B2A-L002987](../../tests/test_web_agent.py#L2987) | 2987 | `"        ),"` | — |
| [SRC-F725E90B2A-L002988](../../tests/test_web_agent.py#L2988) | 2988 | `"    ]"` | — |
| [SRC-F725E90B2A-L002989](../../tests/test_web_agent.py#L2989) | 2989 | `"    for index, (query, title, snippet) in enumerate(cases):"` | — |
| [SRC-F725E90B2A-L002990](../../tests/test_web_agent.py#L2990) | 2990 | `"        agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002991](../../tests/test_web_agent.py#L2991) | 2991 | `"        row = {"` | — |
| [SRC-F725E90B2A-L002992](../../tests/test_web_agent.py#L2992) | 2992 | `"            \"title\": title,"` | — |
| [SRC-F725E90B2A-L002993](../../tests/test_web_agent.py#L2993) | 2993 | `"            \"url\": f\"https://example.com/case-{index}\","` | — |
| [SRC-F725E90B2A-L002994](../../tests/test_web_agent.py#L2994) | 2994 | `"            \"snippet\": snippet,"` | — |
| [SRC-F725E90B2A-L002995](../../tests/test_web_agent.py#L2995) | 2995 | `"            \"provider\": \"fake_provider\","` | — |
| [SRC-F725E90B2A-L002996](../../tests/test_web_agent.py#L2996) | 2996 | `"            \"provider_rank\": 1,"` | — |
| [SRC-F725E90B2A-L002997](../../tests/test_web_agent.py#L2997) | 2997 | `"            \"search_query\": query,"` | — |
| [SRC-F725E90B2A-L002998](../../tests/test_web_agent.py#L2998) | 2998 | `"        }"` | — |
| [SRC-F725E90B2A-L002999](../../tests/test_web_agent.py#L2999) | 2999 | `"        monkeypatch.setattr(agent, \"_search_duckduckgo_html\", lambda _q, row=row: [dict(row)])"` | — |
| [SRC-F725E90B2A-L003000](../../tests/test_web_agent.py#L3000) | 3000 | `"        monkeypatch.setattr(agent, \"_search_bing_rss\", lambda _q, row=row: [dict(row)])"` | — |
| [SRC-F725E90B2A-L003001](../../tests/test_web_agent.py#L3001) | 3001 | `"        # Current-news questions normally add Google News RSS; keep this unit test deterministic."` | — |
| [SRC-F725E90B2A-L003002](../../tests/test_web_agent.py#L3002) | 3002 | `"        monkeypatch.setattr(agent, \"_search_news\", lambda _q: [])"` | — |
| [SRC-F725E90B2A-L003003](../../tests/test_web_agent.py#L3003) | 3003 | `"        results = agent._search_web(query)"` | — |
| [SRC-F725E90B2A-L003004](../../tests/test_web_agent.py#L3004) | 3004 | `"        assert results, f\"Search candidates were all filtered for case {index}\""` | — |
| [SRC-F725E90B2A-L003005](../../tests/test_web_agent.py#L3005) | 3005 | `"        diagnostic = next("` | — |
| [SRC-F725E90B2A-L003006](../../tests/test_web_agent.py#L3006) | 3006 | `"            item for item in agent._provider_diagnostics if item.get(\"provider\") == \"duckduckgo_html\""` | — |
| [SRC-F725E90B2A-L003007](../../tests/test_web_agent.py#L3007) | 3007 | `"        )"` | — |
| [SRC-F725E90B2A-L003008](../../tests/test_web_agent.py#L3008) | 3008 | `"        assert diagnostic[\"accepted_count\"] == 1"` | — |
| [SRC-F725E90B2A-L003009](../../tests/test_web_agent.py#L3009) | 3009 | `"        assert diagnostic[\"result_count\"] == 1"` | — |
| [SRC-F725E90B2A-L003010](../../tests/test_web_agent.py#L3010) | 3010 | `""` | — |
| [SRC-F725E90B2A-L003011](../../tests/test_web_agent.py#L3011) | 3011 | `""` | — |
| [SRC-F725E90B2A-L003012](../../tests/test_web_agent.py#L3012) | 3012 | `"def test_search_web_classifies_http_challenge_and_rate_limit_as_provider_degradation(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003013](../../tests/test_web_agent.py#L3013) | 3013 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003014](../../tests/test_web_agent.py#L3014) | 3014 | `""` | — |
| [SRC-F725E90B2A-L003015](../../tests/test_web_agent.py#L3015) | 3015 | `"    def http_202(_query):"` | — |
| [SRC-F725E90B2A-L003016](../../tests/test_web_agent.py#L3016) | 3016 | `"        raise RuntimeError(\"HTTP 202\")"` | — |
| [SRC-F725E90B2A-L003017](../../tests/test_web_agent.py#L3017) | 3017 | `""` | — |
| [SRC-F725E90B2A-L003018](../../tests/test_web_agent.py#L3018) | 3018 | `"    def http_429(_query):"` | — |
| [SRC-F725E90B2A-L003019](../../tests/test_web_agent.py#L3019) | 3019 | `"        raise RuntimeError(\"HTTP 429\")"` | — |
| [SRC-F725E90B2A-L003020](../../tests/test_web_agent.py#L3020) | 3020 | `""` | — |
| [SRC-F725E90B2A-L003021](../../tests/test_web_agent.py#L3021) | 3021 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", http_202)"` | — |
| [SRC-F725E90B2A-L003022](../../tests/test_web_agent.py#L3022) | 3022 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", http_429)"` | — |
| [SRC-F725E90B2A-L003023](../../tests/test_web_agent.py#L3023) | 3023 | `"    with pytest.raises(RuntimeError, match=\"لم تُرجع موصلات البحث\"):"` | — |
| [SRC-F725E90B2A-L003024](../../tests/test_web_agent.py#L3024) | 3024 | `"        agent._search_web(\"renewable energy storage policy\")"` | — |
| [SRC-F725E90B2A-L003025](../../tests/test_web_agent.py#L3025) | 3025 | `""` | — |
| [SRC-F725E90B2A-L003026](../../tests/test_web_agent.py#L3026) | 3026 | `"    statuses = {"` | — |
| [SRC-F725E90B2A-L003027](../../tests/test_web_agent.py#L3027) | 3027 | `"        item[\"provider\"]: item[\"status\"]"` | — |
| [SRC-F725E90B2A-L003028](../../tests/test_web_agent.py#L3028) | 3028 | `"        for item in agent._provider_diagnostics"` | — |
| [SRC-F725E90B2A-L003029](../../tests/test_web_agent.py#L3029) | 3029 | `"        if item[\"provider\"] in {\"duckduckgo_html\", \"bing_rss\"}"` | — |
| [SRC-F725E90B2A-L003030](../../tests/test_web_agent.py#L3030) | 3030 | `"    }"` | — |
| [SRC-F725E90B2A-L003031](../../tests/test_web_agent.py#L3031) | 3031 | `"    assert statuses[\"duckduckgo_html\"] == \"http_error\""` | — |
| [SRC-F725E90B2A-L003032](../../tests/test_web_agent.py#L3032) | 3032 | `"    assert statuses[\"bing_rss\"] == \"rate_limited\""` | — |
| [SRC-F725E90B2A-L003033](../../tests/test_web_agent.py#L3033) | 3033 | `""` | — |
| [SRC-F725E90B2A-L003034](../../tests/test_web_agent.py#L3034) | 3034 | `""` | — |
| [SRC-F725E90B2A-L003035](../../tests/test_web_agent.py#L3035) | 3035 | `"def test_search_web_records_distinct_candidate_rejection_reasons(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003036](../../tests/test_web_agent.py#L3036) | 3036 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003037](../../tests/test_web_agent.py#L3037) | 3037 | `"    query = \"renewable energy storage\""` | — |
| [SRC-F725E90B2A-L003038](../../tests/test_web_agent.py#L3038) | 3038 | `"    candidates = ["` | — |
| [SRC-F725E90B2A-L003039](../../tests/test_web_agent.py#L3039) | 3039 | `"        \"malformed candidate\","` | — |
| [SRC-F725E90B2A-L003040](../../tests/test_web_agent.py#L3040) | 3040 | `"        {"` | — |
| [SRC-F725E90B2A-L003041](../../tests/test_web_agent.py#L3041) | 3041 | `"            \"title\": \"Unsafe scheme\","` | — |
| [SRC-F725E90B2A-L003042](../../tests/test_web_agent.py#L3042) | 3042 | `"            \"url\": \"javascript:alert(1)\","` | — |
| [SRC-F725E90B2A-L003043](../../tests/test_web_agent.py#L3043) | 3043 | `"            \"snippet\": \"Renewable energy storage report\","` | — |
| [SRC-F725E90B2A-L003044](../../tests/test_web_agent.py#L3044) | 3044 | `"        },"` | — |
| [SRC-F725E90B2A-L003045](../../tests/test_web_agent.py#L3045) | 3045 | `"        {"` | — |
| [SRC-F725E90B2A-L003046](../../tests/test_web_agent.py#L3046) | 3046 | `"            \"title\": \"Translated mirror\","` | — |
| [SRC-F725E90B2A-L003047](../../tests/test_web_agent.py#L3047) | 3047 | `"            \"url\": \"https://translate.google.com/translate?u=https%3A%2F%2Fexample.com\","` | — |
| [SRC-F725E90B2A-L003048](../../tests/test_web_agent.py#L3048) | 3048 | `"            \"snippet\": \"Renewable energy storage\","` | — |
| [SRC-F725E90B2A-L003049](../../tests/test_web_agent.py#L3049) | 3049 | `"        },"` | — |
| [SRC-F725E90B2A-L003050](../../tests/test_web_agent.py#L3050) | 3050 | `"        {"` | — |
| [SRC-F725E90B2A-L003051](../../tests/test_web_agent.py#L3051) | 3051 | `"            \"title\": \"Gardening tips\","` | — |
| [SRC-F725E90B2A-L003052](../../tests/test_web_agent.py#L3052) | 3052 | `"            \"url\": \"https://example.com/gardening\","` | — |
| [SRC-F725E90B2A-L003053](../../tests/test_web_agent.py#L3053) | 3053 | `"            \"snippet\": \"Gardening flowers and house plants\","` | — |
| [SRC-F725E90B2A-L003054](../../tests/test_web_agent.py#L3054) | 3054 | `"        },"` | — |
| [SRC-F725E90B2A-L003055](../../tests/test_web_agent.py#L3055) | 3055 | `"    ]"` | — |
| [SRC-F725E90B2A-L003056](../../tests/test_web_agent.py#L3056) | 3056 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", lambda _q: [dict(x) if isinstance(x, dict) else x for x in candidates])"` | — |
| [SRC-F725E90B2A-L003057](../../tests/test_web_agent.py#L3057) | 3057 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", lambda _q: [dict(x) if isinstance(x, dict) else x for x in candidates])"` | — |
| [SRC-F725E90B2A-L003058](../../tests/test_web_agent.py#L3058) | 3058 | `"    monkeypatch.setattr(agent, \"_search_news\", lambda _q: [])"` | — |
| [SRC-F725E90B2A-L003059](../../tests/test_web_agent.py#L3059) | 3059 | `""` | — |
| [SRC-F725E90B2A-L003060](../../tests/test_web_agent.py#L3060) | 3060 | `"    with pytest.raises(RuntimeError, match=\"لم تُرجع موصلات البحث\"):"` | — |
| [SRC-F725E90B2A-L003061](../../tests/test_web_agent.py#L3061) | 3061 | `"        agent._search_web(query)"` | — |
| [SRC-F725E90B2A-L003062](../../tests/test_web_agent.py#L3062) | 3062 | `""` | — |
| [SRC-F725E90B2A-L003063](../../tests/test_web_agent.py#L3063) | 3063 | `"    diagnostic = next("` | — |
| [SRC-F725E90B2A-L003064](../../tests/test_web_agent.py#L3064) | 3064 | `"        item for item in agent._provider_diagnostics"` | — |
| [SRC-F725E90B2A-L003065](../../tests/test_web_agent.py#L3065) | 3065 | `"        if item.get(\"provider\") == \"duckduckgo_html\""` | — |
| [SRC-F725E90B2A-L003066](../../tests/test_web_agent.py#L3066) | 3066 | `"    )"` | — |
| [SRC-F725E90B2A-L003067](../../tests/test_web_agent.py#L3067) | 3067 | `"    assert diagnostic[\"status\"] == \"filtered_all\""` | — |
| [SRC-F725E90B2A-L003068](../../tests/test_web_agent.py#L3068) | 3068 | `"    assert diagnostic[\"result_count\"] == 4"` | — |
| [SRC-F725E90B2A-L003069](../../tests/test_web_agent.py#L3069) | 3069 | `"    assert diagnostic[\"accepted_count\"] == 0"` | — |
| [SRC-F725E90B2A-L003070](../../tests/test_web_agent.py#L3070) | 3070 | `"    assert diagnostic[\"rejected_count\"] == 4"` | — |
| [SRC-F725E90B2A-L003071](../../tests/test_web_agent.py#L3071) | 3071 | `"    assert diagnostic[\"rejection_counts\"] == {"` | — |
| [SRC-F725E90B2A-L003072](../../tests/test_web_agent.py#L3072) | 3072 | `"        \"malformed_candidate\": 1,"` | — |
| [SRC-F725E90B2A-L003073](../../tests/test_web_agent.py#L3073) | 3073 | `"        \"invalid_url_or_unsafe_target\": 1,"` | — |
| [SRC-F725E90B2A-L003074](../../tests/test_web_agent.py#L3074) | 3074 | `"        \"blocked_domain\": 1,"` | — |
| [SRC-F725E90B2A-L003075](../../tests/test_web_agent.py#L3075) | 3075 | `"        \"relevance_below_threshold\": 1,"` | — |
| [SRC-F725E90B2A-L003076](../../tests/test_web_agent.py#L3076) | 3076 | `"    }"` | — |
| [SRC-F725E90B2A-L003077](../../tests/test_web_agent.py#L3077) | 3077 | `"    assert sum(diagnostic[\"rejection_counts\"].values()) == diagnostic[\"rejected_count\"]"` | — |
| [SRC-F725E90B2A-L003078](../../tests/test_web_agent.py#L3078) | 3078 | `""` | — |
| [SRC-F725E90B2A-L003079](../../tests/test_web_agent.py#L3079) | 3079 | `""` | — |
| [SRC-F725E90B2A-L003080](../../tests/test_web_agent.py#L3080) | 3080 | `"def test_search_web_classifies_http_302_as_degraded_without_following_provider_redirect(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003081](../../tests/test_web_agent.py#L3081) | 3081 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003082](../../tests/test_web_agent.py#L3082) | 3082 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L003083](../../tests/test_web_agent.py#L3083) | 3083 | `""` | — |
| [SRC-F725E90B2A-L003084](../../tests/test_web_agent.py#L3084) | 3084 | `"    def redirect_response(query):"` | — |
| [SRC-F725E90B2A-L003085](../../tests/test_web_agent.py#L3085) | 3085 | `"        calls.append((\"duckduckgo_html\", query))"` | — |
| [SRC-F725E90B2A-L003086](../../tests/test_web_agent.py#L3086) | 3086 | `"        raise RuntimeError(\"HTTP 302\")"` | — |
| [SRC-F725E90B2A-L003087](../../tests/test_web_agent.py#L3087) | 3087 | `""` | — |
| [SRC-F725E90B2A-L003088](../../tests/test_web_agent.py#L3088) | 3088 | `"    def no_results(query):"` | — |
| [SRC-F725E90B2A-L003089](../../tests/test_web_agent.py#L3089) | 3089 | `"        calls.append((\"bing_rss\", query))"` | — |
| [SRC-F725E90B2A-L003090](../../tests/test_web_agent.py#L3090) | 3090 | `"        return []"` | — |
| [SRC-F725E90B2A-L003091](../../tests/test_web_agent.py#L3091) | 3091 | `""` | — |
| [SRC-F725E90B2A-L003092](../../tests/test_web_agent.py#L3092) | 3092 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", redirect_response)"` | — |
| [SRC-F725E90B2A-L003093](../../tests/test_web_agent.py#L3093) | 3093 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", no_results)"` | — |
| [SRC-F725E90B2A-L003094](../../tests/test_web_agent.py#L3094) | 3094 | `"    monkeypatch.setattr(agent, \"_search_news\", lambda _q: [])"` | — |
| [SRC-F725E90B2A-L003095](../../tests/test_web_agent.py#L3095) | 3095 | `""` | — |
| [SRC-F725E90B2A-L003096](../../tests/test_web_agent.py#L3096) | 3096 | `"    with pytest.raises(RuntimeError, match=\"لم تُرجع موصلات البحث\"):"` | — |
| [SRC-F725E90B2A-L003097](../../tests/test_web_agent.py#L3097) | 3097 | `"        agent._search_web(\"renewable energy storage\")"` | — |
| [SRC-F725E90B2A-L003098](../../tests/test_web_agent.py#L3098) | 3098 | `""` | — |
| [SRC-F725E90B2A-L003099](../../tests/test_web_agent.py#L3099) | 3099 | `"    diagnostic = next("` | — |
| [SRC-F725E90B2A-L003100](../../tests/test_web_agent.py#L3100) | 3100 | `"        item for item in agent._provider_diagnostics"` | — |
| [SRC-F725E90B2A-L003101](../../tests/test_web_agent.py#L3101) | 3101 | `"        if item.get(\"provider\") == \"duckduckgo_html\""` | — |
| [SRC-F725E90B2A-L003102](../../tests/test_web_agent.py#L3102) | 3102 | `"    )"` | — |
| [SRC-F725E90B2A-L003103](../../tests/test_web_agent.py#L3103) | 3103 | `"    assert diagnostic[\"status\"] == \"http_error\""` | — |
| [SRC-F725E90B2A-L003104](../../tests/test_web_agent.py#L3104) | 3104 | `"    assert diagnostic[\"error\"] == \"RuntimeError: HTTP 302\""` | — |
| [SRC-F725E90B2A-L003105](../../tests/test_web_agent.py#L3105) | 3105 | `"    assert sum(provider == \"duckduckgo_html\" for provider, _query in calls) == 1"` | — |
| [SRC-F725E90B2A-L003106](../../tests/test_web_agent.py#L3106) | 3106 | `""` | — |
| [SRC-F725E90B2A-L003107](../../tests/test_web_agent.py#L3107) | 3107 | `""` | — |
| [SRC-F725E90B2A-L003108](../../tests/test_web_agent.py#L3108) | 3108 | `"def test_relevance_filter_compacts_prompt_and_rejects_instruction_only_queries():"` | — |
| [SRC-F725E90B2A-L003109](../../tests/test_web_agent.py#L3109) | 3109 | `"    question = \"ما عاصمة مصر؟ اذكر مصدرًا موثوقًا مع رابط مباشر، وأجب بالعربية بإيجاز.\""` | — |
| [SRC-F725E90B2A-L003110](../../tests/test_web_agent.py#L3110) | 3110 | `"    assert _relevance_ratio(question, \"عاصمة مصر القاهرة\") >= 0.20"` | — |
| [SRC-F725E90B2A-L003111](../../tests/test_web_agent.py#L3111) | 3111 | `"    assert _relevance_ratio("` | — |
| [SRC-F725E90B2A-L003112](../../tests/test_web_agent.py#L3112) | 3112 | `"        \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\","` | — |
| [SRC-F725E90B2A-L003113](../../tests/test_web_agent.py#L3113) | 3113 | `"        \"Football results and unrelated match reports\","` | — |
| [SRC-F725E90B2A-L003114](../../tests/test_web_agent.py#L3114) | 3114 | `"    ) == 0.0"` | — |
| [SRC-F725E90B2A-L003115](../../tests/test_web_agent.py#L3115) | 3115 | `""` | — |
| [SRC-F725E90B2A-L003116](../../tests/test_web_agent.py#L3116) | 3116 | `""` | — |
| [SRC-F725E90B2A-L003117](../../tests/test_web_agent.py#L3117) | 3117 | `"def test_relevance_query_tokens_reject_site_only_and_modifier_only_queries():"` | — |
| [SRC-F725E90B2A-L003118](../../tests/test_web_agent.py#L3118) | 3118 | `"    assert _relevance_query_tokens(\"site:reddit.com\") == set()"` | — |
| [SRC-F725E90B2A-L003119](../../tests/test_web_agent.py#L3119) | 3119 | `"    assert _relevance_query_tokens(\"risks limitations alternatives\") == set()"` | — |
| [SRC-F725E90B2A-L003120](../../tests/test_web_agent.py#L3120) | 3120 | `"    assert _relevance_query_tokens(\"السيارات الكهربائية المستعملة في مصر\")"` | — |
| [SRC-F725E90B2A-L003121](../../tests/test_web_agent.py#L3121) | 3121 | `""` | — |
| [SRC-F725E90B2A-L003122](../../tests/test_web_agent.py#L3122) | 3122 | `""` | — |
| [SRC-F725E90B2A-L003123](../../tests/test_web_agent.py#L3123) | 3123 | `"def test_search_web_compacts_request_before_provider_dispatch(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003124](../../tests/test_web_agent.py#L3124) | 3124 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003125](../../tests/test_web_agent.py#L3125) | 3125 | `"    seen = []"` | — |
| [SRC-F725E90B2A-L003126](../../tests/test_web_agent.py#L3126) | 3126 | `""` | — |
| [SRC-F725E90B2A-L003127](../../tests/test_web_agent.py#L3127) | 3127 | `"    def capture(query):"` | — |
| [SRC-F725E90B2A-L003128](../../tests/test_web_agent.py#L3128) | 3128 | `"        seen.append(query)"` | — |
| [SRC-F725E90B2A-L003129](../../tests/test_web_agent.py#L3129) | 3129 | `"        return []"` | — |
| [SRC-F725E90B2A-L003130](../../tests/test_web_agent.py#L3130) | 3130 | `""` | — |
| [SRC-F725E90B2A-L003131](../../tests/test_web_agent.py#L3131) | 3131 | `"    for env_name in ("` | — |
| [SRC-F725E90B2A-L003132](../../tests/test_web_agent.py#L3132) | 3132 | `"        \"DEEPSEEK_SEARCH_API_KEY\","` | — |
| [SRC-F725E90B2A-L003133](../../tests/test_web_agent.py#L3133) | 3133 | `"        \"BRAVE_SEARCH_API_KEY\","` | — |
| [SRC-F725E90B2A-L003134](../../tests/test_web_agent.py#L3134) | 3134 | `"        \"TAVILY_API_KEY\","` | — |
| [SRC-F725E90B2A-L003135](../../tests/test_web_agent.py#L3135) | 3135 | `"    ):"` | — |
| [SRC-F725E90B2A-L003136](../../tests/test_web_agent.py#L3136) | 3136 | `"        monkeypatch.delenv(env_name, raising=False)"` | — |
| [SRC-F725E90B2A-L003137](../../tests/test_web_agent.py#L3137) | 3137 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", capture)"` | — |
| [SRC-F725E90B2A-L003138](../../tests/test_web_agent.py#L3138) | 3138 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", capture)"` | — |
| [SRC-F725E90B2A-L003139](../../tests/test_web_agent.py#L3139) | 3139 | `""` | — |
| [SRC-F725E90B2A-L003140](../../tests/test_web_agent.py#L3140) | 3140 | `"    raw_question = ("` | — |
| [SRC-F725E90B2A-L003141](../../tests/test_web_agent.py#L3141) | 3141 | `"        \"ما عاصمة مصر؟ اذكر مصدرًا موثوقًا مع رابط مباشر، وأجب بالعربية بإيجاز.\""` | — |
| [SRC-F725E90B2A-L003142](../../tests/test_web_agent.py#L3142) | 3142 | `"    )"` | — |
| [SRC-F725E90B2A-L003143](../../tests/test_web_agent.py#L3143) | 3143 | `"    with pytest.raises(RuntimeError, match=\"لم تُرجع موصلات البحث\"):"` | — |
| [SRC-F725E90B2A-L003144](../../tests/test_web_agent.py#L3144) | 3144 | `"        agent._search_web(raw_question)"` | — |
| [SRC-F725E90B2A-L003145](../../tests/test_web_agent.py#L3145) | 3145 | `""` | — |
| [SRC-F725E90B2A-L003146](../../tests/test_web_agent.py#L3146) | 3146 | `"    expected = _normalize_search_query(compact_search_query(raw_question))"` | — |
| [SRC-F725E90B2A-L003147](../../tests/test_web_agent.py#L3147) | 3147 | `"    assert seen"` | — |
| [SRC-F725E90B2A-L003148](../../tests/test_web_agent.py#L3148) | 3148 | `"    assert set(seen) == {expected}"` | — |
| [SRC-F725E90B2A-L003149](../../tests/test_web_agent.py#L3149) | 3149 | `"    assert len(expected) <= 240"` | — |
| [SRC-F725E90B2A-L003150](../../tests/test_web_agent.py#L3150) | 3150 | `"    assert \"رابط مباشر\" not in \" \".join(seen)"` | — |
| [SRC-F725E90B2A-L003151](../../tests/test_web_agent.py#L3151) | 3151 | `""` | — |
| [SRC-F725E90B2A-L003152](../../tests/test_web_agent.py#L3152) | 3152 | `""` | — |
| [SRC-F725E90B2A-L003153](../../tests/test_web_agent.py#L3153) | 3153 | `"def test_search_web_does_not_dispatch_instruction_only_query(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003154](../../tests/test_web_agent.py#L3154) | 3154 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003155](../../tests/test_web_agent.py#L3155) | 3155 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003156](../../tests/test_web_agent.py#L3156) | 3156 | `"        agent, \"_search_duckduckgo_html\","` | — |
| [SRC-F725E90B2A-L003157](../../tests/test_web_agent.py#L3157) | 3157 | `"        lambda query: pytest.fail(f\"provider should not receive {query!r}\"),"` | — |
| [SRC-F725E90B2A-L003158](../../tests/test_web_agent.py#L3158) | 3158 | `"    )"` | — |
| [SRC-F725E90B2A-L003159](../../tests/test_web_agent.py#L3159) | 3159 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003160](../../tests/test_web_agent.py#L3160) | 3160 | `"        agent, \"_search_bing_rss\","` | — |
| [SRC-F725E90B2A-L003161](../../tests/test_web_agent.py#L3161) | 3161 | `"        lambda query: pytest.fail(f\"provider should not receive {query!r}\"),"` | — |
| [SRC-F725E90B2A-L003162](../../tests/test_web_agent.py#L3162) | 3162 | `"    )"` | — |
| [SRC-F725E90B2A-L003163](../../tests/test_web_agent.py#L3163) | 3163 | `"    results = agent._search_web(\"اذكر مصادر موثوقة، روابط مباشرة، باختصار\")"` | — |
| [SRC-F725E90B2A-L003164](../../tests/test_web_agent.py#L3164) | 3164 | `"    assert results == []"` | — |
| [SRC-F725E90B2A-L003165](../../tests/test_web_agent.py#L3165) | 3165 | `""` | — |
| [SRC-F725E90B2A-L003166](../../tests/test_web_agent.py#L3166) | 3166 | `""` | — |
| [SRC-F725E90B2A-L003167](../../tests/test_web_agent.py#L3167) | 3167 | `"def test_plan_search_does_not_call_planner_without_a_topic(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003168](../../tests/test_web_agent.py#L3168) | 3168 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003169](../../tests/test_web_agent.py#L3169) | 3169 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L003170](../../tests/test_web_agent.py#L3170) | 3170 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003171](../../tests/test_web_agent.py#L3171) | 3171 | `"        agent, \"_request_completion\","` | — |
| [SRC-F725E90B2A-L003172](../../tests/test_web_agent.py#L3172) | 3172 | `"        lambda *args, **kwargs: pytest.fail(\"planner should not run without a topic\"),"` | — |
| [SRC-F725E90B2A-L003173](../../tests/test_web_agent.py#L3173) | 3173 | `"    )"` | — |
| [SRC-F725E90B2A-L003174](../../tests/test_web_agent.py#L3174) | 3174 | `"    plan = agent._plan_search("` | — |
| [SRC-F725E90B2A-L003175](../../tests/test_web_agent.py#L3175) | 3175 | `"        \"استخدم مصادر متعددة، واذكر روابط المصادر\","` | — |
| [SRC-F725E90B2A-L003176](../../tests/test_web_agent.py#L3176) | 3176 | `"        [],"` | — |
| [SRC-F725E90B2A-L003177](../../tests/test_web_agent.py#L3177) | 3177 | `"    )"` | — |
| [SRC-F725E90B2A-L003178](../../tests/test_web_agent.py#L3178) | 3178 | `"    assert plan[\"queries\"] == []"` | — |
| [SRC-F725E90B2A-L003179](../../tests/test_web_agent.py#L3179) | 3179 | `""` | — |
| [SRC-F725E90B2A-L003180](../../tests/test_web_agent.py#L3180) | 3180 | `""` | — |
| [SRC-F725E90B2A-L003181](../../tests/test_web_agent.py#L3181) | 3181 | `"def test_plan_search_compacts_followup_query_before_fallback(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003182](../../tests/test_web_agent.py#L3182) | 3182 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003183](../../tests/test_web_agent.py#L3183) | 3183 | `"    agent.api_key = \"\""` | — |
| [SRC-F725E90B2A-L003184](../../tests/test_web_agent.py#L3184) | 3184 | `"    history = ["` | — |
| [SRC-F725E90B2A-L003185](../../tests/test_web_agent.py#L3185) | 3185 | `"        {"` | — |
| [SRC-F725E90B2A-L003186](../../tests/test_web_agent.py#L3186) | 3186 | `"            \"role\": \"user\","` | — |
| [SRC-F725E90B2A-L003187](../../tests/test_web_agent.py#L3187) | 3187 | `"            \"content\": ("` | — |
| [SRC-F725E90B2A-L003188](../../tests/test_web_agent.py#L3188) | 3188 | `"                \"قارن السيارات الكهربائية في مصر. استخدم مصادر متعددة، \""` | — |
| [SRC-F725E90B2A-L003189](../../tests/test_web_agent.py#L3189) | 3189 | `"                \"واذكر روابط المصادر وأجب بإيجاز.\""` | — |
| [SRC-F725E90B2A-L003190](../../tests/test_web_agent.py#L3190) | 3190 | `"            ),"` | — |
| [SRC-F725E90B2A-L003191](../../tests/test_web_agent.py#L3191) | 3191 | `"        },"` | — |
| [SRC-F725E90B2A-L003192](../../tests/test_web_agent.py#L3192) | 3192 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن مقارنة موثقة.\"},"` | — |
| [SRC-F725E90B2A-L003193](../../tests/test_web_agent.py#L3193) | 3193 | `"    ]"` | — |
| [SRC-F725E90B2A-L003194](../../tests/test_web_agent.py#L3194) | 3194 | `"    plan = agent._plan_search(\"وطب الأسعار الحالية؟\", history)"` | — |
| [SRC-F725E90B2A-L003195](../../tests/test_web_agent.py#L3195) | 3195 | `""` | — |
| [SRC-F725E90B2A-L003196](../../tests/test_web_agent.py#L3196) | 3196 | `"    assert plan[\"queries\"]"` | — |
| [SRC-F725E90B2A-L003197](../../tests/test_web_agent.py#L3197) | 3197 | `"    assert all(len(query) <= 240 for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L003198](../../tests/test_web_agent.py#L3198) | 3198 | `"    assert any(\"السيارات الكهربائية\" in query for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L003199](../../tests/test_web_agent.py#L3199) | 3199 | `"    assert all("` | — |
| [SRC-F725E90B2A-L003200](../../tests/test_web_agent.py#L3200) | 3200 | `"        \"روابط المصادر\" not in query and \"أجب بإيجاز\" not in query"` | — |
| [SRC-F725E90B2A-L003201](../../tests/test_web_agent.py#L3201) | 3201 | `"        for query in plan[\"queries\"]"` | — |
| [SRC-F725E90B2A-L003202](../../tests/test_web_agent.py#L3202) | 3202 | `"    )"` | — |
| [SRC-F725E90B2A-L003203](../../tests/test_web_agent.py#L3203) | 3203 | `""` | — |
| [SRC-F725E90B2A-L003204](../../tests/test_web_agent.py#L3204) | 3204 | `""` | — |
| [SRC-F725E90B2A-L003205](../../tests/test_web_agent.py#L3205) | 3205 | `"@pytest.mark.parametrize(\"fallback_queries\", [[], None])"` | — |
| [SRC-F725E90B2A-L003206](../../tests/test_web_agent.py#L3206) | 3206 | `"def test_auto_mode_does_not_reinsert_raw_question_when_fallback_has_no_query("` | — |
| [SRC-F725E90B2A-L003207](../../tests/test_web_agent.py#L3207) | 3207 | `"    monkeypatch, fallback_queries"` | — |
| [SRC-F725E90B2A-L003208](../../tests/test_web_agent.py#L3208) | 3208 | `"):"` | — |
| [SRC-F725E90B2A-L003209](../../tests/test_web_agent.py#L3209) | 3209 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003210](../../tests/test_web_agent.py#L3210) | 3210 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L003211](../../tests/test_web_agent.py#L3211) | 3211 | `"    question = ("` | — |
| [SRC-F725E90B2A-L003212](../../tests/test_web_agent.py#L3212) | 3212 | `"        \"ما عيوب السيارات الكهربائية المستعملة في مصر؟ \""` | — |
| [SRC-F725E90B2A-L003213](../../tests/test_web_agent.py#L3213) | 3213 | `"        \"اذكر مصادر موثوقة وروابط مباشرة وأجب بإيجاز.\""` | — |
| [SRC-F725E90B2A-L003214](../../tests/test_web_agent.py#L3214) | 3214 | `"    )"` | — |
| [SRC-F725E90B2A-L003215](../../tests/test_web_agent.py#L3215) | 3215 | `"    observed_plans = []"` | — |
| [SRC-F725E90B2A-L003216](../../tests/test_web_agent.py#L3216) | 3216 | `""` | — |
| [SRC-F725E90B2A-L003217](../../tests/test_web_agent.py#L3217) | 3217 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003218](../../tests/test_web_agent.py#L3218) | 3218 | `"        \"agents.web_agent.route_intent\","` | — |
| [SRC-F725E90B2A-L003219](../../tests/test_web_agent.py#L3219) | 3219 | `"        lambda *args, **kwargs: {\"route\": \"WEB_SIMPLE\", \"reason\": \"test\"},"` | — |
| [SRC-F725E90B2A-L003220](../../tests/test_web_agent.py#L3220) | 3220 | `"    )"` | — |
| [SRC-F725E90B2A-L003221](../../tests/test_web_agent.py#L3221) | 3221 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003222](../../tests/test_web_agent.py#L3222) | 3222 | `"        agent, \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003223](../../tests/test_web_agent.py#L3223) | 3223 | `"        lambda _question, _history: {"` | — |
| [SRC-F725E90B2A-L003224](../../tests/test_web_agent.py#L3224) | 3224 | `"            \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L003225](../../tests/test_web_agent.py#L3225) | 3225 | `"            \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L003226](../../tests/test_web_agent.py#L3226) | 3226 | `"            \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003227](../../tests/test_web_agent.py#L3227) | 3227 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003228](../../tests/test_web_agent.py#L3228) | 3228 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003229](../../tests/test_web_agent.py#L3229) | 3229 | `"            \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003230](../../tests/test_web_agent.py#L3230) | 3230 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003231](../../tests/test_web_agent.py#L3231) | 3231 | `"        },"` | — |
| [SRC-F725E90B2A-L003232](../../tests/test_web_agent.py#L3232) | 3232 | `"    )"` | — |
| [SRC-F725E90B2A-L003233](../../tests/test_web_agent.py#L3233) | 3233 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003234](../../tests/test_web_agent.py#L3234) | 3234 | `"        \"agents.web_agent.fallback_plan\","` | — |
| [SRC-F725E90B2A-L003235](../../tests/test_web_agent.py#L3235) | 3235 | `"        lambda *args, **kwargs: {\"queries\": fallback_queries},"` | — |
| [SRC-F725E90B2A-L003236](../../tests/test_web_agent.py#L3236) | 3236 | `"    )"` | — |
| [SRC-F725E90B2A-L003237](../../tests/test_web_agent.py#L3237) | 3237 | `""` | — |
| [SRC-F725E90B2A-L003238](../../tests/test_web_agent.py#L3238) | 3238 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L003239](../../tests/test_web_agent.py#L3239) | 3239 | `"        observed_plans.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L003240](../../tests/test_web_agent.py#L3240) | 3240 | `"        return [], [], {"` | — |
| [SRC-F725E90B2A-L003241](../../tests/test_web_agent.py#L3241) | 3241 | `"            \"queries_planned\": len(research_plan.get(\"queries\", [])),"` | — |
| [SRC-F725E90B2A-L003242](../../tests/test_web_agent.py#L3242) | 3242 | `"            \"queries_attempted\": 0,"` | — |
| [SRC-F725E90B2A-L003243](../../tests/test_web_agent.py#L3243) | 3243 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L003244](../../tests/test_web_agent.py#L3244) | 3244 | `"            \"unique_sources\": 0,"` | — |
| [SRC-F725E90B2A-L003245](../../tests/test_web_agent.py#L3245) | 3245 | `"            \"pages_fetched\": 0,"` | — |
| [SRC-F725E90B2A-L003246](../../tests/test_web_agent.py#L3246) | 3246 | `"            \"providers_used\": [],"` | — |
| [SRC-F725E90B2A-L003247](../../tests/test_web_agent.py#L3247) | 3247 | `"            \"platform_counts\": {},"` | — |
| [SRC-F725E90B2A-L003248](../../tests/test_web_agent.py#L3248) | 3248 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L003249](../../tests/test_web_agent.py#L3249) | 3249 | `"            \"depth\": research_plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-F725E90B2A-L003250](../../tests/test_web_agent.py#L3250) | 3250 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003251](../../tests/test_web_agent.py#L3251) | 3251 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L003252](../../tests/test_web_agent.py#L3252) | 3252 | `"        }"` | — |
| [SRC-F725E90B2A-L003253](../../tests/test_web_agent.py#L3253) | 3253 | `""` | — |
| [SRC-F725E90B2A-L003254](../../tests/test_web_agent.py#L3254) | 3254 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L003255](../../tests/test_web_agent.py#L3255) | 3255 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"لا تتوفر مصادر كافية.\")"` | — |
| [SRC-F725E90B2A-L003256](../../tests/test_web_agent.py#L3256) | 3256 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda _question, answer, _sources: answer)"` | — |
| [SRC-F725E90B2A-L003257](../../tests/test_web_agent.py#L3257) | 3257 | `""` | — |
| [SRC-F725E90B2A-L003258](../../tests/test_web_agent.py#L3258) | 3258 | `"    agent.answer(question, mode=\"auto\")"` | — |
| [SRC-F725E90B2A-L003259](../../tests/test_web_agent.py#L3259) | 3259 | `""` | — |
| [SRC-F725E90B2A-L003260](../../tests/test_web_agent.py#L3260) | 3260 | `"    assert observed_plans"` | — |
| [SRC-F725E90B2A-L003261](../../tests/test_web_agent.py#L3261) | 3261 | `"    assert question not in observed_plans[0][\"queries\"]"` | — |
| [SRC-F725E90B2A-L003262](../../tests/test_web_agent.py#L3262) | 3262 | `"    assert observed_plans[0][\"queries\"]"` | — |
| [SRC-F725E90B2A-L003263](../../tests/test_web_agent.py#L3263) | 3263 | `"    assert observed_plans[0][\"queries\"][0] == compact_search_query(question)"` | — |
| [SRC-F725E90B2A-L003264](../../tests/test_web_agent.py#L3264) | 3264 | `""` | — |
| [SRC-F725E90B2A-L003265](../../tests/test_web_agent.py#L3265) | 3265 | `""` | — |
| [SRC-F725E90B2A-L003266](../../tests/test_web_agent.py#L3266) | 3266 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L003267](../../tests/test_web_agent.py#L3267) | 3267 | `"    (\"question\", \"planned_query\"),"` | — |
| [SRC-F725E90B2A-L003268](../../tests/test_web_agent.py#L3268) | 3268 | `"    ["` | — |
| [SRC-F725E90B2A-L003269](../../tests/test_web_agent.py#L3269) | 3269 | `"        ("` | — |
| [SRC-F725E90B2A-L003270](../../tests/test_web_agent.py#L3270) | 3270 | `"            ("` | — |
| [SRC-F725E90B2A-L003271](../../tests/test_web_agent.py#L3271) | 3271 | `"                \"ما عيوب السيارات الكهربائية المستعملة في مصر؟ \""` | — |
| [SRC-F725E90B2A-L003272](../../tests/test_web_agent.py#L3272) | 3272 | `"                \"اذكر مصادر موثوقة وروابط مباشرة وأجب بإيجاز.\""` | — |
| [SRC-F725E90B2A-L003273](../../tests/test_web_agent.py#L3273) | 3273 | `"            ),"` | — |
| [SRC-F725E90B2A-L003274](../../tests/test_web_agent.py#L3274) | 3274 | `"            None,"` | — |
| [SRC-F725E90B2A-L003275](../../tests/test_web_agent.py#L3275) | 3275 | `"        ),"` | — |
| [SRC-F725E90B2A-L003276](../../tests/test_web_agent.py#L3276) | 3276 | `"        ("` | — |
| [SRC-F725E90B2A-L003277](../../tests/test_web_agent.py#L3277) | 3277 | `"            \"كام سعرها؟ اذكر مصادر موثوقة وروابط مباشرة وأجب بإيجاز.\","` | — |
| [SRC-F725E90B2A-L003278](../../tests/test_web_agent.py#L3278) | 3278 | `"            \"أسعار السيارات الكهربائية المستعملة في مصر\","` | — |
| [SRC-F725E90B2A-L003279](../../tests/test_web_agent.py#L3279) | 3279 | `"        ),"` | — |
| [SRC-F725E90B2A-L003280](../../tests/test_web_agent.py#L3280) | 3280 | `"    ],"` | — |
| [SRC-F725E90B2A-L003281](../../tests/test_web_agent.py#L3281) | 3281 | `")"` | — |
| [SRC-F725E90B2A-L003282](../../tests/test_web_agent.py#L3282) | 3282 | `"def test_server_search_sources_use_compact_question_and_topic_plan("` | — |
| [SRC-F725E90B2A-L003283](../../tests/test_web_agent.py#L3283) | 3283 | `"    monkeypatch, question, planned_query"` | — |
| [SRC-F725E90B2A-L003284](../../tests/test_web_agent.py#L3284) | 3284 | `"):"` | — |
| [SRC-F725E90B2A-L003285](../../tests/test_web_agent.py#L3285) | 3285 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003286](../../tests/test_web_agent.py#L3286) | 3286 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L003287](../../tests/test_web_agent.py#L3287) | 3287 | `"    topic_query = planned_query or compact_search_query(question)"` | — |
| [SRC-F725E90B2A-L003288](../../tests/test_web_agent.py#L3288) | 3288 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L003289](../../tests/test_web_agent.py#L3289) | 3289 | `"        \"queries\": [topic_query],"` | — |
| [SRC-F725E90B2A-L003290](../../tests/test_web_agent.py#L3290) | 3290 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L003291](../../tests/test_web_agent.py#L3291) | 3291 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003292](../../tests/test_web_agent.py#L3292) | 3292 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003293](../../tests/test_web_agent.py#L3293) | 3293 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003294](../../tests/test_web_agent.py#L3294) | 3294 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003295](../../tests/test_web_agent.py#L3295) | 3295 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003296](../../tests/test_web_agent.py#L3296) | 3296 | `"    }"` | — |
| [SRC-F725E90B2A-L003297](../../tests/test_web_agent.py#L3297) | 3297 | `"    source_queries = []"` | — |
| [SRC-F725E90B2A-L003298](../../tests/test_web_agent.py#L3298) | 3298 | `""` | — |
| [SRC-F725E90B2A-L003299](../../tests/test_web_agent.py#L3299) | 3299 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda _question, _history: dict(plan))"` | — |
| [SRC-F725E90B2A-L003300](../../tests/test_web_agent.py#L3300) | 3300 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003301](../../tests/test_web_agent.py#L3301) | 3301 | `"        agent, \"_collect_research\","` | — |
| [SRC-F725E90B2A-L003302](../../tests/test_web_agent.py#L3302) | 3302 | `"        lambda research_plan: ([sample_source(0), sample_source(1)], [], {"` | — |
| [SRC-F725E90B2A-L003303](../../tests/test_web_agent.py#L3303) | 3303 | `"            \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L003304](../../tests/test_web_agent.py#L3304) | 3304 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L003305](../../tests/test_web_agent.py#L3305) | 3305 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L003306](../../tests/test_web_agent.py#L3306) | 3306 | `"            \"unique_sources\": 2,"` | — |
| [SRC-F725E90B2A-L003307](../../tests/test_web_agent.py#L3307) | 3307 | `"            \"pages_fetched\": 2,"` | — |
| [SRC-F725E90B2A-L003308](../../tests/test_web_agent.py#L3308) | 3308 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L003309](../../tests/test_web_agent.py#L3309) | 3309 | `"            \"platform_counts\": {\"web\": 2},"` | — |
| [SRC-F725E90B2A-L003310](../../tests/test_web_agent.py#L3310) | 3310 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L003311](../../tests/test_web_agent.py#L3311) | 3311 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003312](../../tests/test_web_agent.py#L3312) | 3312 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003313](../../tests/test_web_agent.py#L3313) | 3313 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L003314](../../tests/test_web_agent.py#L3314) | 3314 | `"        }),"` | — |
| [SRC-F725E90B2A-L003315](../../tests/test_web_agent.py#L3315) | 3315 | `"    )"` | — |
| [SRC-F725E90B2A-L003316](../../tests/test_web_agent.py#L3316) | 3316 | `""` | — |
| [SRC-F725E90B2A-L003317](../../tests/test_web_agent.py#L3317) | 3317 | `"    def generate(*args, **kwargs):"` | — |
| [SRC-F725E90B2A-L003318](../../tests/test_web_agent.py#L3318) | 3318 | `"        agent.server_search_sources = [{"` | — |
| [SRC-F725E90B2A-L003319](../../tests/test_web_agent.py#L3319) | 3319 | `"            \"title\": \"تجارب السيارات الكهربائية المستعملة\","` | — |
| [SRC-F725E90B2A-L003320](../../tests/test_web_agent.py#L3320) | 3320 | `"            \"url\": \"https://example.org/ev-used-cars\","` | — |
| [SRC-F725E90B2A-L003321](../../tests/test_web_agent.py#L3321) | 3321 | `"            \"snippet\": \"تكلفة البطارية والمدى الفعلي للسيارات الكهربائية المستعملة في مصر\","` | — |
| [SRC-F725E90B2A-L003322](../../tests/test_web_agent.py#L3322) | 3322 | `"            \"page_text\": \"تكلفة البطارية والمدى الفعلي للسيارات الكهربائية المستعملة في مصر\","` | — |
| [SRC-F725E90B2A-L003323](../../tests/test_web_agent.py#L3323) | 3323 | `"            \"page_fetched\": False,"` | — |
| [SRC-F725E90B2A-L003324](../../tests/test_web_agent.py#L3324) | 3324 | `"            \"provider\": \"openrouter_web_search\","` | — |
| [SRC-F725E90B2A-L003325](../../tests/test_web_agent.py#L3325) | 3325 | `"            \"providers\": [\"openrouter_web_search\"],"` | — |
| [SRC-F725E90B2A-L003326](../../tests/test_web_agent.py#L3326) | 3326 | `"            \"queries\": [],"` | — |
| [SRC-F725E90B2A-L003327](../../tests/test_web_agent.py#L3327) | 3327 | `"            \"domain\": \"example.org\","` | — |
| [SRC-F725E90B2A-L003328](../../tests/test_web_agent.py#L3328) | 3328 | `"            \"source_class\": \"general\","` | — |
| [SRC-F725E90B2A-L003329](../../tests/test_web_agent.py#L3329) | 3329 | `"            \"platform\": \"web\","` | — |
| [SRC-F725E90B2A-L003330](../../tests/test_web_agent.py#L3330) | 3330 | `"            \"published_at\": \"\","` | — |
| [SRC-F725E90B2A-L003331](../../tests/test_web_agent.py#L3331) | 3331 | `"        }]"` | — |
| [SRC-F725E90B2A-L003332](../../tests/test_web_agent.py#L3332) | 3332 | `"        return \"إجابة مبدئية [المصدر 1].\""` | — |
| [SRC-F725E90B2A-L003333](../../tests/test_web_agent.py#L3333) | 3333 | `""` | — |
| [SRC-F725E90B2A-L003334](../../tests/test_web_agent.py#L3334) | 3334 | `"    monkeypatch.setattr(agent, \"_generate\", generate)"` | — |
| [SRC-F725E90B2A-L003335](../../tests/test_web_agent.py#L3335) | 3335 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda _question, answer, _sources: answer)"` | — |
| [SRC-F725E90B2A-L003336](../../tests/test_web_agent.py#L3336) | 3336 | `""` | — |
| [SRC-F725E90B2A-L003337](../../tests/test_web_agent.py#L3337) | 3337 | `"    def capture_relevance(query, text):"` | — |
| [SRC-F725E90B2A-L003338](../../tests/test_web_agent.py#L3338) | 3338 | `"        if \"تجارب السيارات الكهربائية المستعملة\" in text:"` | — |
| [SRC-F725E90B2A-L003339](../../tests/test_web_agent.py#L3339) | 3339 | `"            source_queries.append(query)"` | — |
| [SRC-F725E90B2A-L003340](../../tests/test_web_agent.py#L3340) | 3340 | `"            if planned_query and query != compact_search_query(topic_query):"` | — |
| [SRC-F725E90B2A-L003341](../../tests/test_web_agent.py#L3341) | 3341 | `"                return 0.0"` | — |
| [SRC-F725E90B2A-L003342](../../tests/test_web_agent.py#L3342) | 3342 | `"        return 0.25"` | — |
| [SRC-F725E90B2A-L003343](../../tests/test_web_agent.py#L3343) | 3343 | `""` | — |
| [SRC-F725E90B2A-L003344](../../tests/test_web_agent.py#L3344) | 3344 | `"    monkeypatch.setattr(\"agents.web_agent._relevance_ratio\", capture_relevance)"` | — |
| [SRC-F725E90B2A-L003345](../../tests/test_web_agent.py#L3345) | 3345 | `""` | — |
| [SRC-F725E90B2A-L003346](../../tests/test_web_agent.py#L3346) | 3346 | `"    agent.answer(question)"` | — |
| [SRC-F725E90B2A-L003347](../../tests/test_web_agent.py#L3347) | 3347 | `""` | — |
| [SRC-F725E90B2A-L003348](../../tests/test_web_agent.py#L3348) | 3348 | `"    expected_queries = list(dict.fromkeys("` | — |
| [SRC-F725E90B2A-L003349](../../tests/test_web_agent.py#L3349) | 3349 | `"        query for query in ("` | — |
| [SRC-F725E90B2A-L003350](../../tests/test_web_agent.py#L3350) | 3350 | `"            compact_search_query(question),"` | — |
| [SRC-F725E90B2A-L003351](../../tests/test_web_agent.py#L3351) | 3351 | `"            compact_search_query(topic_query),"` | — |
| [SRC-F725E90B2A-L003352](../../tests/test_web_agent.py#L3352) | 3352 | `"        ) if query"` | — |
| [SRC-F725E90B2A-L003353](../../tests/test_web_agent.py#L3353) | 3353 | `"    ))"` | — |
| [SRC-F725E90B2A-L003354](../../tests/test_web_agent.py#L3354) | 3354 | `"    assert source_queries == expected_queries"` | — |
| [SRC-F725E90B2A-L003355](../../tests/test_web_agent.py#L3355) | 3355 | `""` | — |
| [SRC-F725E90B2A-L003356](../../tests/test_web_agent.py#L3356) | 3356 | `""` | — |
| [SRC-F725E90B2A-L003357](../../tests/test_web_agent.py#L3357) | 3357 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L003358](../../tests/test_web_agent.py#L3358) | 3358 | `"    (\"mode\", \"planner_query\"),"` | — |
| [SRC-F725E90B2A-L003359](../../tests/test_web_agent.py#L3359) | 3359 | `"    ["` | — |
| [SRC-F725E90B2A-L003360](../../tests/test_web_agent.py#L3360) | 3360 | `"        (\"auto\", \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\"),"` | — |
| [SRC-F725E90B2A-L003361](../../tests/test_web_agent.py#L3361) | 3361 | `"        (\"auto\", \"site:reddit.com\"),"` | — |
| [SRC-F725E90B2A-L003362](../../tests/test_web_agent.py#L3362) | 3362 | `"        (\"latest\", \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\"),"` | — |
| [SRC-F725E90B2A-L003363](../../tests/test_web_agent.py#L3363) | 3363 | `"        (\"deep\", \"site:reddit.com\"),"` | — |
| [SRC-F725E90B2A-L003364](../../tests/test_web_agent.py#L3364) | 3364 | `"        (\"social\", \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\"),"` | — |
| [SRC-F725E90B2A-L003365](../../tests/test_web_agent.py#L3365) | 3365 | `"    ],"` | — |
| [SRC-F725E90B2A-L003366](../../tests/test_web_agent.py#L3366) | 3366 | `")"` | — |
| [SRC-F725E90B2A-L003367](../../tests/test_web_agent.py#L3367) | 3367 | `"def test_modes_do_not_create_generic_queries_without_topic("` | — |
| [SRC-F725E90B2A-L003368](../../tests/test_web_agent.py#L3368) | 3368 | `"    monkeypatch, mode, planner_query"` | — |
| [SRC-F725E90B2A-L003369](../../tests/test_web_agent.py#L3369) | 3369 | `"):"` | — |
| [SRC-F725E90B2A-L003370](../../tests/test_web_agent.py#L3370) | 3370 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003371](../../tests/test_web_agent.py#L3371) | 3371 | `"    instruction_only = \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\""` | — |
| [SRC-F725E90B2A-L003372](../../tests/test_web_agent.py#L3372) | 3372 | `"    direct_url = \"https://example.com/report\""` | — |
| [SRC-F725E90B2A-L003373](../../tests/test_web_agent.py#L3373) | 3373 | `"    observed_plans = []"` | — |
| [SRC-F725E90B2A-L003374](../../tests/test_web_agent.py#L3374) | 3374 | `""` | — |
| [SRC-F725E90B2A-L003375](../../tests/test_web_agent.py#L3375) | 3375 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003376](../../tests/test_web_agent.py#L3376) | 3376 | `"        \"agents.web_agent.route_intent\","` | — |
| [SRC-F725E90B2A-L003377](../../tests/test_web_agent.py#L3377) | 3377 | `"        lambda *args, **kwargs: {\"route\": \"WEB_DEEP\", \"reason\": \"test\"},"` | — |
| [SRC-F725E90B2A-L003378](../../tests/test_web_agent.py#L3378) | 3378 | `"    )"` | — |
| [SRC-F725E90B2A-L003379](../../tests/test_web_agent.py#L3379) | 3379 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003380](../../tests/test_web_agent.py#L3380) | 3380 | `"        agent, \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003381](../../tests/test_web_agent.py#L3381) | 3381 | `"        lambda _question, _history: {"` | — |
| [SRC-F725E90B2A-L003382](../../tests/test_web_agent.py#L3382) | 3382 | `"            \"queries\": [planner_query],"` | — |
| [SRC-F725E90B2A-L003383](../../tests/test_web_agent.py#L3383) | 3383 | `"            \"direct_urls\": [direct_url],"` | — |
| [SRC-F725E90B2A-L003384](../../tests/test_web_agent.py#L3384) | 3384 | `"            \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003385](../../tests/test_web_agent.py#L3385) | 3385 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003386](../../tests/test_web_agent.py#L3386) | 3386 | `"            \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L003387](../../tests/test_web_agent.py#L3387) | 3387 | `"            \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003388](../../tests/test_web_agent.py#L3388) | 3388 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003389](../../tests/test_web_agent.py#L3389) | 3389 | `"        },"` | — |
| [SRC-F725E90B2A-L003390](../../tests/test_web_agent.py#L3390) | 3390 | `"    )"` | — |
| [SRC-F725E90B2A-L003391](../../tests/test_web_agent.py#L3391) | 3391 | `""` | — |
| [SRC-F725E90B2A-L003392](../../tests/test_web_agent.py#L3392) | 3392 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L003393](../../tests/test_web_agent.py#L3393) | 3393 | `"        observed_plans.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L003394](../../tests/test_web_agent.py#L3394) | 3394 | `"        return [], [], {"` | — |
| [SRC-F725E90B2A-L003395](../../tests/test_web_agent.py#L3395) | 3395 | `"            \"queries_planned\": len(research_plan.get(\"queries\", [])),"` | — |
| [SRC-F725E90B2A-L003396](../../tests/test_web_agent.py#L3396) | 3396 | `"            \"queries_attempted\": 0,"` | — |
| [SRC-F725E90B2A-L003397](../../tests/test_web_agent.py#L3397) | 3397 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L003398](../../tests/test_web_agent.py#L3398) | 3398 | `"            \"unique_sources\": 0,"` | — |
| [SRC-F725E90B2A-L003399](../../tests/test_web_agent.py#L3399) | 3399 | `"            \"pages_fetched\": 0,"` | — |
| [SRC-F725E90B2A-L003400](../../tests/test_web_agent.py#L3400) | 3400 | `"            \"providers_used\": [],"` | — |
| [SRC-F725E90B2A-L003401](../../tests/test_web_agent.py#L3401) | 3401 | `"            \"platform_counts\": {},"` | — |
| [SRC-F725E90B2A-L003402](../../tests/test_web_agent.py#L3402) | 3402 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L003403](../../tests/test_web_agent.py#L3403) | 3403 | `"            \"depth\": research_plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-F725E90B2A-L003404](../../tests/test_web_agent.py#L3404) | 3404 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003405](../../tests/test_web_agent.py#L3405) | 3405 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L003406](../../tests/test_web_agent.py#L3406) | 3406 | `"        }"` | — |
| [SRC-F725E90B2A-L003407](../../tests/test_web_agent.py#L3407) | 3407 | `""` | — |
| [SRC-F725E90B2A-L003408](../../tests/test_web_agent.py#L3408) | 3408 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L003409](../../tests/test_web_agent.py#L3409) | 3409 | `""` | — |
| [SRC-F725E90B2A-L003410](../../tests/test_web_agent.py#L3410) | 3410 | `"    agent.answer(instruction_only, mode=mode)"` | — |
| [SRC-F725E90B2A-L003411](../../tests/test_web_agent.py#L3411) | 3411 | `""` | — |
| [SRC-F725E90B2A-L003412](../../tests/test_web_agent.py#L3412) | 3412 | `"    assert observed_plans"` | — |
| [SRC-F725E90B2A-L003413](../../tests/test_web_agent.py#L3413) | 3413 | `"    assert observed_plans[0][\"queries\"] == []"` | — |
| [SRC-F725E90B2A-L003414](../../tests/test_web_agent.py#L3414) | 3414 | `"    assert observed_plans[0][\"direct_urls\"] == [direct_url]"` | — |
| [SRC-F725E90B2A-L003415](../../tests/test_web_agent.py#L3415) | 3415 | `""` | — |
| [SRC-F725E90B2A-L003416](../../tests/test_web_agent.py#L3416) | 3416 | `""` | — |
| [SRC-F725E90B2A-L003417](../../tests/test_web_agent.py#L3417) | 3417 | `"def test_auto_navigation_strips_arabic_search_verb_without_regex_regression(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003418](../../tests/test_web_agent.py#L3418) | 3418 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003419](../../tests/test_web_agent.py#L3419) | 3419 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L003420](../../tests/test_web_agent.py#L3420) | 3420 | `"    question = \"ابحث عن الموقع الرسمي لشركة النور\""` | — |
| [SRC-F725E90B2A-L003421](../../tests/test_web_agent.py#L3421) | 3421 | `"    observed_plans = []"` | — |
| [SRC-F725E90B2A-L003422](../../tests/test_web_agent.py#L3422) | 3422 | `""` | — |
| [SRC-F725E90B2A-L003423](../../tests/test_web_agent.py#L3423) | 3423 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003424](../../tests/test_web_agent.py#L3424) | 3424 | `"        \"agents.web_agent.route_intent\","` | — |
| [SRC-F725E90B2A-L003425](../../tests/test_web_agent.py#L3425) | 3425 | `"        lambda *args, **kwargs: {\"route\": \"WEB_SIMPLE\", \"reason\": \"test\"},"` | — |
| [SRC-F725E90B2A-L003426](../../tests/test_web_agent.py#L3426) | 3426 | `"    )"` | — |
| [SRC-F725E90B2A-L003427](../../tests/test_web_agent.py#L3427) | 3427 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003428](../../tests/test_web_agent.py#L3428) | 3428 | `"        \"agents.web_agent.compact_search_query\","` | — |
| [SRC-F725E90B2A-L003429](../../tests/test_web_agent.py#L3429) | 3429 | `"        lambda value: value.strip() if isinstance(value, str) else \"\","` | — |
| [SRC-F725E90B2A-L003430](../../tests/test_web_agent.py#L3430) | 3430 | `"    )"` | — |
| [SRC-F725E90B2A-L003431](../../tests/test_web_agent.py#L3431) | 3431 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003432](../../tests/test_web_agent.py#L3432) | 3432 | `"        agent, \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003433](../../tests/test_web_agent.py#L3433) | 3433 | `"        lambda _question, _history: {"` | — |
| [SRC-F725E90B2A-L003434](../../tests/test_web_agent.py#L3434) | 3434 | `"            \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L003435](../../tests/test_web_agent.py#L3435) | 3435 | `"            \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L003436](../../tests/test_web_agent.py#L3436) | 3436 | `"            \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003437](../../tests/test_web_agent.py#L3437) | 3437 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003438](../../tests/test_web_agent.py#L3438) | 3438 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003439](../../tests/test_web_agent.py#L3439) | 3439 | `"            \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003440](../../tests/test_web_agent.py#L3440) | 3440 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003441](../../tests/test_web_agent.py#L3441) | 3441 | `"        },"` | — |
| [SRC-F725E90B2A-L003442](../../tests/test_web_agent.py#L3442) | 3442 | `"    )"` | — |
| [SRC-F725E90B2A-L003443](../../tests/test_web_agent.py#L3443) | 3443 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003444](../../tests/test_web_agent.py#L3444) | 3444 | `"        \"agents.web_agent.fallback_plan\","` | — |
| [SRC-F725E90B2A-L003445](../../tests/test_web_agent.py#L3445) | 3445 | `"        lambda *args, **kwargs: {\"queries\": [question]},"` | — |
| [SRC-F725E90B2A-L003446](../../tests/test_web_agent.py#L3446) | 3446 | `"    )"` | — |
| [SRC-F725E90B2A-L003447](../../tests/test_web_agent.py#L3447) | 3447 | `""` | — |
| [SRC-F725E90B2A-L003448](../../tests/test_web_agent.py#L3448) | 3448 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L003449](../../tests/test_web_agent.py#L3449) | 3449 | `"        observed_plans.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L003450](../../tests/test_web_agent.py#L3450) | 3450 | `"        return [], [], {"` | — |
| [SRC-F725E90B2A-L003451](../../tests/test_web_agent.py#L3451) | 3451 | `"            \"queries_planned\": len(research_plan.get(\"queries\", [])),"` | — |
| [SRC-F725E90B2A-L003452](../../tests/test_web_agent.py#L3452) | 3452 | `"            \"queries_attempted\": 0,"` | — |
| [SRC-F725E90B2A-L003453](../../tests/test_web_agent.py#L3453) | 3453 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L003454](../../tests/test_web_agent.py#L3454) | 3454 | `"            \"unique_sources\": 0,"` | — |
| [SRC-F725E90B2A-L003455](../../tests/test_web_agent.py#L3455) | 3455 | `"            \"pages_fetched\": 0,"` | — |
| [SRC-F725E90B2A-L003456](../../tests/test_web_agent.py#L3456) | 3456 | `"            \"providers_used\": [],"` | — |
| [SRC-F725E90B2A-L003457](../../tests/test_web_agent.py#L3457) | 3457 | `"            \"platform_counts\": {},"` | — |
| [SRC-F725E90B2A-L003458](../../tests/test_web_agent.py#L3458) | 3458 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L003459](../../tests/test_web_agent.py#L3459) | 3459 | `"            \"depth\": research_plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-F725E90B2A-L003460](../../tests/test_web_agent.py#L3460) | 3460 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003461](../../tests/test_web_agent.py#L3461) | 3461 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L003462](../../tests/test_web_agent.py#L3462) | 3462 | `"        }"` | — |
| [SRC-F725E90B2A-L003463](../../tests/test_web_agent.py#L3463) | 3463 | `""` | — |
| [SRC-F725E90B2A-L003464](../../tests/test_web_agent.py#L3464) | 3464 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L003465](../../tests/test_web_agent.py#L3465) | 3465 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"لم أعثر على مصدر.\")"` | — |
| [SRC-F725E90B2A-L003466](../../tests/test_web_agent.py#L3466) | 3466 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda _question, answer, _sources: answer)"` | — |
| [SRC-F725E90B2A-L003467](../../tests/test_web_agent.py#L3467) | 3467 | `""` | — |
| [SRC-F725E90B2A-L003468](../../tests/test_web_agent.py#L3468) | 3468 | `"    agent.answer(question, mode=\"auto\")"` | — |
| [SRC-F725E90B2A-L003469](../../tests/test_web_agent.py#L3469) | 3469 | `""` | — |
| [SRC-F725E90B2A-L003470](../../tests/test_web_agent.py#L3470) | 3470 | `"    assert observed_plans"` | — |
| [SRC-F725E90B2A-L003471](../../tests/test_web_agent.py#L3471) | 3471 | `"    assert observed_plans[0][\"queries\"]"` | — |
| [SRC-F725E90B2A-L003472](../../tests/test_web_agent.py#L3472) | 3472 | `"    assert all(not query.startswith(\"ابحث عن\") for query in observed_plans[0][\"queries\"])"` | — |
| [SRC-F725E90B2A-L003473](../../tests/test_web_agent.py#L3473) | 3473 | `"    assert \"الموقع الرسمي لشركة النور\" in observed_plans[0][\"queries\"][0]"` | — |
| [SRC-F725E90B2A-L003474](../../tests/test_web_agent.py#L3474) | 3474 | `"def test_latest_mode_does_not_generate_answer_from_stale_pages(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003475](../../tests/test_web_agent.py#L3475) | 3475 | `"    \"\"\"Current-mode answers must abstain if only old pages survive retrieval.\"\"\""` | — |
| [SRC-F725E90B2A-L003476](../../tests/test_web_agent.py#L3476) | 3476 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003477](../../tests/test_web_agent.py#L3477) | 3477 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L003478](../../tests/test_web_agent.py#L3478) | 3478 | `"        \"queries\": [\"مواعيد عمل مكتب الجوازات العباسية اليوم\"],"` | — |
| [SRC-F725E90B2A-L003479](../../tests/test_web_agent.py#L3479) | 3479 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L003480](../../tests/test_web_agent.py#L3480) | 3480 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003481](../../tests/test_web_agent.py#L3481) | 3481 | `"        \"freshness\": \"current\","` | — |
| [SRC-F725E90B2A-L003482](../../tests/test_web_agent.py#L3482) | 3482 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003483](../../tests/test_web_agent.py#L3483) | 3483 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003484](../../tests/test_web_agent.py#L3484) | 3484 | `"        \"planning_method\": \"fixture\","` | — |
| [SRC-F725E90B2A-L003485](../../tests/test_web_agent.py#L3485) | 3485 | `"        \"coverage_targets\": [],"` | — |
| [SRC-F725E90B2A-L003486](../../tests/test_web_agent.py#L3486) | 3486 | `"    }"` | — |
| [SRC-F725E90B2A-L003487](../../tests/test_web_agent.py#L3487) | 3487 | `"    collection_calls = []"` | — |
| [SRC-F725E90B2A-L003488](../../tests/test_web_agent.py#L3488) | 3488 | `""` | — |
| [SRC-F725E90B2A-L003489](../../tests/test_web_agent.py#L3489) | 3489 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L003490](../../tests/test_web_agent.py#L3490) | 3490 | `"        collection_calls.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L003491](../../tests/test_web_agent.py#L3491) | 3491 | `"        old_page = sample_source(0)"` | — |
| [SRC-F725E90B2A-L003492](../../tests/test_web_agent.py#L3492) | 3492 | `"        old_page.update({"` | — |
| [SRC-F725E90B2A-L003493](../../tests/test_web_agent.py#L3493) | 3493 | `"            \"url\": \"https://moi.gov.eg/passports\","` | — |
| [SRC-F725E90B2A-L003494](../../tests/test_web_agent.py#L3494) | 3494 | `"            \"domain\": \"moi.gov.eg\","` | — |
| [SRC-F725E90B2A-L003495](../../tests/test_web_agent.py#L3495) | 3495 | `"            \"published_at\": \"2024-01-01T10:00:00Z\","` | — |
| [SRC-F725E90B2A-L003496](../../tests/test_web_agent.py#L3496) | 3496 | `"            \"page_fetched\": True,"` | — |
| [SRC-F725E90B2A-L003497](../../tests/test_web_agent.py#L3497) | 3497 | `"            \"page_text\": \"محتوى قديم عن مواعيد العمل\","` | — |
| [SRC-F725E90B2A-L003498](../../tests/test_web_agent.py#L3498) | 3498 | `"        })"` | — |
| [SRC-F725E90B2A-L003499](../../tests/test_web_agent.py#L3499) | 3499 | `"        return [old_page], [], {"` | — |
| [SRC-F725E90B2A-L003500](../../tests/test_web_agent.py#L3500) | 3500 | `"            \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L003501](../../tests/test_web_agent.py#L3501) | 3501 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L003502](../../tests/test_web_agent.py#L3502) | 3502 | `"            \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L003503](../../tests/test_web_agent.py#L3503) | 3503 | `"            \"pages_fetched\": 1,"` | — |
| [SRC-F725E90B2A-L003504](../../tests/test_web_agent.py#L3504) | 3504 | `"            \"providers_used\": [\"fixture\"],"` | — |
| [SRC-F725E90B2A-L003505](../../tests/test_web_agent.py#L3505) | 3505 | `"            \"provider_counts\": {\"fixture\": 1},"` | — |
| [SRC-F725E90B2A-L003506](../../tests/test_web_agent.py#L3506) | 3506 | `"            \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L003507](../../tests/test_web_agent.py#L3507) | 3507 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L003508](../../tests/test_web_agent.py#L3508) | 3508 | `"            \"expansion_queries\": [],"` | — |
| [SRC-F725E90B2A-L003509](../../tests/test_web_agent.py#L3509) | 3509 | `"            \"provider_diagnostics\": [],"` | — |
| [SRC-F725E90B2A-L003510](../../tests/test_web_agent.py#L3510) | 3510 | `"            \"query_results\": [{\"query\": research_plan[\"queries\"][0], \"results\": 1}],"` | — |
| [SRC-F725E90B2A-L003511](../../tests/test_web_agent.py#L3511) | 3511 | `"        }"` | — |
| [SRC-F725E90B2A-L003512](../../tests/test_web_agent.py#L3512) | 3512 | `""` | — |
| [SRC-F725E90B2A-L003513](../../tests/test_web_agent.py#L3513) | 3513 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda *args, **kwargs: dict(plan))"` | — |
| [SRC-F725E90B2A-L003514](../../tests/test_web_agent.py#L3514) | 3514 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L003515](../../tests/test_web_agent.py#L3515) | 3515 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L003516](../../tests/test_web_agent.py#L3516) | 3516 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003517](../../tests/test_web_agent.py#L3517) | 3517 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003518](../../tests/test_web_agent.py#L3518) | 3518 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L003519](../../tests/test_web_agent.py#L3519) | 3519 | `"        lambda *args, **kwargs: pytest.fail(\"Stale pages must not be passed to generation\"),"` | — |
| [SRC-F725E90B2A-L003520](../../tests/test_web_agent.py#L3520) | 3520 | `"    )"` | — |
| [SRC-F725E90B2A-L003521](../../tests/test_web_agent.py#L3521) | 3521 | `""` | — |
| [SRC-F725E90B2A-L003522](../../tests/test_web_agent.py#L3522) | 3522 | `"    result = agent.answer(\"ما مواعيد عمل مكتب الجوازات اليوم؟\", mode=\"latest\")"` | — |
| [SRC-F725E90B2A-L003523](../../tests/test_web_agent.py#L3523) | 3523 | `""` | — |
| [SRC-F725E90B2A-L003524](../../tests/test_web_agent.py#L3524) | 3524 | `"    assert result[\"kind\"] == \"insufficient_evidence\""` | — |
| [SRC-F725E90B2A-L003525](../../tests/test_web_agent.py#L3525) | 3525 | `"    assert len(collection_calls) >= 1"` | — |
| [SRC-F725E90B2A-L003526](../../tests/test_web_agent.py#L3526) | 3526 | `"    guardrails = result[\"search_report\"][\"source_guardrails\"]"` | — |
| [SRC-F725E90B2A-L003527](../../tests/test_web_agent.py#L3527) | 3527 | `"    assert guardrails[\"initial\"][\"rejection_counts\"][\"stale\"] == 1"` | — |
| [SRC-F725E90B2A-L003528](../../tests/test_web_agent.py#L3528) | 3528 | `"    assert guardrails[\"final\"][\"current_evidence_status\"] == \"no_current_eligible_evidence\""` | — |
| [SRC-F725E90B2A-L003529](../../tests/test_web_agent.py#L3529) | 3529 | `"    assert result[\"search_report\"][\"search_outcome\"] == \"attempted_no_usable_sources\""` | — |
| [SRC-F725E90B2A-L003530](../../tests/test_web_agent.py#L3530) | 3530 | `""` | — |
| [SRC-F725E90B2A-L003531](../../tests/test_web_agent.py#L3531) | 3531 | `"def test_official_government_lookup_never_synthesizes_tourism_result(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003532](../../tests/test_web_agent.py#L3532) | 3532 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003533](../../tests/test_web_agent.py#L3533) | 3533 | `"    question = \"ابحث عن الموقع الرسمي لوزارة الاتصالات وتكنولوجيا المعلومات المصرية\""` | — |
| [SRC-F725E90B2A-L003534](../../tests/test_web_agent.py#L3534) | 3534 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L003535](../../tests/test_web_agent.py#L3535) | 3535 | `"        \"queries\": [\"وزارة الاتصالات وتكنولوجيا المعلومات مصر الموقع الرسمي\"],"` | — |
| [SRC-F725E90B2A-L003536](../../tests/test_web_agent.py#L3536) | 3536 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L003537](../../tests/test_web_agent.py#L3537) | 3537 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003538](../../tests/test_web_agent.py#L3538) | 3538 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003539](../../tests/test_web_agent.py#L3539) | 3539 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003540](../../tests/test_web_agent.py#L3540) | 3540 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003541](../../tests/test_web_agent.py#L3541) | 3541 | `"        \"planning_method\": \"fixture\","` | — |
| [SRC-F725E90B2A-L003542](../../tests/test_web_agent.py#L3542) | 3542 | `"    }"` | — |
| [SRC-F725E90B2A-L003543](../../tests/test_web_agent.py#L3543) | 3543 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L003544](../../tests/test_web_agent.py#L3544) | 3544 | `""` | — |
| [SRC-F725E90B2A-L003545](../../tests/test_web_agent.py#L3545) | 3545 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L003546](../../tests/test_web_agent.py#L3546) | 3546 | `"        calls.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L003547](../../tests/test_web_agent.py#L3547) | 3547 | `"        candidate = sample_source(0)"` | — |
| [SRC-F725E90B2A-L003548](../../tests/test_web_agent.py#L3548) | 3548 | `"        candidate.update({"` | — |
| [SRC-F725E90B2A-L003549](../../tests/test_web_agent.py#L3549) | 3549 | `"            \"title\": \"وزارة الاتصالات في مصر ومعلومات سياحية\","` | — |
| [SRC-F725E90B2A-L003550](../../tests/test_web_agent.py#L3550) | 3550 | `"            \"url\": \"https://visitegypt.com/\","` | — |
| [SRC-F725E90B2A-L003551](../../tests/test_web_agent.py#L3551) | 3551 | `"            \"domain\": \"visitegypt.com\","` | — |
| [SRC-F725E90B2A-L003552](../../tests/test_web_agent.py#L3552) | 3552 | `"            \"snippet\": \"معلومات عن الوزارة ضمن دليل سياحي لمصر\","` | — |
| [SRC-F725E90B2A-L003553](../../tests/test_web_agent.py#L3553) | 3553 | `"            \"page_fetched\": True,"` | — |
| [SRC-F725E90B2A-L003554](../../tests/test_web_agent.py#L3554) | 3554 | `"            \"page_text\": \"معلومات سياحية تذكر وزارة الاتصالات\","` | — |
| [SRC-F725E90B2A-L003555](../../tests/test_web_agent.py#L3555) | 3555 | `"            \"queries\": list(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L003556](../../tests/test_web_agent.py#L3556) | 3556 | `"        })"` | — |
| [SRC-F725E90B2A-L003557](../../tests/test_web_agent.py#L3557) | 3557 | `"        return [candidate], [], {"` | — |
| [SRC-F725E90B2A-L003558](../../tests/test_web_agent.py#L3558) | 3558 | `"            \"queries_planned\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L003559](../../tests/test_web_agent.py#L3559) | 3559 | `"            \"queries_attempted\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L003560](../../tests/test_web_agent.py#L3560) | 3560 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L003561](../../tests/test_web_agent.py#L3561) | 3561 | `"            \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L003562](../../tests/test_web_agent.py#L3562) | 3562 | `"            \"pages_fetched\": 1,"` | — |
| [SRC-F725E90B2A-L003563](../../tests/test_web_agent.py#L3563) | 3563 | `"            \"providers_used\": [\"fixture\"],"` | — |
| [SRC-F725E90B2A-L003564](../../tests/test_web_agent.py#L3564) | 3564 | `"            \"provider_counts\": {\"fixture\": 1},"` | — |
| [SRC-F725E90B2A-L003565](../../tests/test_web_agent.py#L3565) | 3565 | `"            \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L003566](../../tests/test_web_agent.py#L3566) | 3566 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L003567](../../tests/test_web_agent.py#L3567) | 3567 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003568](../../tests/test_web_agent.py#L3568) | 3568 | `"            \"planning_method\": \"fixture\","` | — |
| [SRC-F725E90B2A-L003569](../../tests/test_web_agent.py#L3569) | 3569 | `"            \"provider_diagnostics\": [],"` | — |
| [SRC-F725E90B2A-L003570](../../tests/test_web_agent.py#L3570) | 3570 | `"        }"` | — |
| [SRC-F725E90B2A-L003571](../../tests/test_web_agent.py#L3571) | 3571 | `""` | — |
| [SRC-F725E90B2A-L003572](../../tests/test_web_agent.py#L3572) | 3572 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda *args, **kwargs: dict(plan))"` | — |
| [SRC-F725E90B2A-L003573](../../tests/test_web_agent.py#L3573) | 3573 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L003574](../../tests/test_web_agent.py#L3574) | 3574 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L003575](../../tests/test_web_agent.py#L3575) | 3575 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003576](../../tests/test_web_agent.py#L3576) | 3576 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003577](../../tests/test_web_agent.py#L3577) | 3577 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L003578](../../tests/test_web_agent.py#L3578) | 3578 | `"        lambda *args, **kwargs: pytest.fail("` | — |
| [SRC-F725E90B2A-L003579](../../tests/test_web_agent.py#L3579) | 3579 | `"            \"A tourism result must never be passed to answer generation as the official site\""` | — |
| [SRC-F725E90B2A-L003580](../../tests/test_web_agent.py#L3580) | 3580 | `"        ),"` | — |
| [SRC-F725E90B2A-L003581](../../tests/test_web_agent.py#L3581) | 3581 | `"    )"` | — |
| [SRC-F725E90B2A-L003582](../../tests/test_web_agent.py#L3582) | 3582 | `""` | — |
| [SRC-F725E90B2A-L003583](../../tests/test_web_agent.py#L3583) | 3583 | `"    result = agent.answer(question, mode=\"auto\")"` | — |
| [SRC-F725E90B2A-L003584](../../tests/test_web_agent.py#L3584) | 3584 | `""` | — |
| [SRC-F725E90B2A-L003585](../../tests/test_web_agent.py#L3585) | 3585 | `"    assert calls  # initial research, plus bounded repair where applicable"` | — |
| [SRC-F725E90B2A-L003586](../../tests/test_web_agent.py#L3586) | 3586 | `"    assert result[\"kind\"] == \"insufficient_evidence\""` | — |
| [SRC-F725E90B2A-L003587](../../tests/test_web_agent.py#L3587) | 3587 | `"    assert result[\"sources\"] == []"` | — |
| [SRC-F725E90B2A-L003588](../../tests/test_web_agent.py#L3588) | 3588 | `"    guardrails = result[\"search_report\"][\"source_guardrails\"]"` | — |
| [SRC-F725E90B2A-L003589](../../tests/test_web_agent.py#L3589) | 3589 | `"    assert guardrails[\"initial\"][\"official_government_domain_required\"] is True"` | — |
| [SRC-F725E90B2A-L003590](../../tests/test_web_agent.py#L3590) | 3590 | `"    assert guardrails[\"initial\"][\"rejection_counts\"] == {"` | — |
| [SRC-F725E90B2A-L003591](../../tests/test_web_agent.py#L3591) | 3591 | `"        \"not_an_official_government_domain\": 1"` | — |
| [SRC-F725E90B2A-L003592](../../tests/test_web_agent.py#L3592) | 3592 | `"    }"` | — |
| [SRC-F725E90B2A-L003593](../../tests/test_web_agent.py#L3593) | 3593 | `"    assert guardrails[\"final\"][\"accepted_sources\"] == 0"` | — |
| [SRC-F725E90B2A-L003594](../../tests/test_web_agent.py#L3594) | 3594 | `"    assert result[\"search_report\"][\"usable_sources_after_filtering\"] == 0"` | — |
| [SRC-F725E90B2A-L003595](../../tests/test_web_agent.py#L3595) | 3595 | `""` | — |
| [SRC-F725E90B2A-L003596](../../tests/test_web_agent.py#L3596) | 3596 | `"def test_criterion_gap_repair_cannot_reintroduce_non_social_source(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003597](../../tests/test_web_agent.py#L3597) | 3597 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003598](../../tests/test_web_agent.py#L3598) | 3598 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L003599](../../tests/test_web_agent.py#L3599) | 3599 | `"    question = ("` | — |
| [SRC-F725E90B2A-L003600](../../tests/test_web_agent.py#L3600) | 3600 | `"        \"قارن بين خدمتين من حيث السعر والخصوصية والاعتمادية \""` | — |
| [SRC-F725E90B2A-L003601](../../tests/test_web_agent.py#L3601) | 3601 | `"        \"واعرض آراء وتجارب المستخدمين\""` | — |
| [SRC-F725E90B2A-L003602](../../tests/test_web_agent.py#L3602) | 3602 | `"    )"` | — |
| [SRC-F725E90B2A-L003603](../../tests/test_web_agent.py#L3603) | 3603 | `"    initial_sources = ["` | — |
| [SRC-F725E90B2A-L003604](../../tests/test_web_agent.py#L3604) | 3604 | `"        {"` | — |
| [SRC-F725E90B2A-L003605](../../tests/test_web_agent.py#L3605) | 3605 | `"            **sample_source(0),"` | — |
| [SRC-F725E90B2A-L003606](../../tests/test_web_agent.py#L3606) | 3606 | `"            \"url\": \"https://www.reddit.com/r/example/comments/1\","` | — |
| [SRC-F725E90B2A-L003607](../../tests/test_web_agent.py#L3607) | 3607 | `"            \"domain\": \"reddit.com\","` | — |
| [SRC-F725E90B2A-L003608](../../tests/test_web_agent.py#L3608) | 3608 | `"            \"title\": \"مناقشة تجارب المستخدمين للخدمتين\","` | — |
| [SRC-F725E90B2A-L003609](../../tests/test_web_agent.py#L3609) | 3609 | `"            \"snippet\": \"تجارب وآراء مستخدمين حول الخدمتين\","` | — |
| [SRC-F725E90B2A-L003610](../../tests/test_web_agent.py#L3610) | 3610 | `"            \"page_text\": \"تجارب وآراء مستخدمين حول الخدمتين\","` | — |
| [SRC-F725E90B2A-L003611](../../tests/test_web_agent.py#L3611) | 3611 | `"            \"platform\": \"reddit\","` | — |
| [SRC-F725E90B2A-L003612](../../tests/test_web_agent.py#L3612) | 3612 | `"            \"providers\": [\"reddit\"],"` | — |
| [SRC-F725E90B2A-L003613](../../tests/test_web_agent.py#L3613) | 3613 | `"        },"` | — |
| [SRC-F725E90B2A-L003614](../../tests/test_web_agent.py#L3614) | 3614 | `"        {"` | — |
| [SRC-F725E90B2A-L003615](../../tests/test_web_agent.py#L3615) | 3615 | `"            **sample_source(1),"` | — |
| [SRC-F725E90B2A-L003616](../../tests/test_web_agent.py#L3616) | 3616 | `"            \"url\": \"https://www.reddit.com/r/example/comments/2\","` | — |
| [SRC-F725E90B2A-L003617](../../tests/test_web_agent.py#L3617) | 3617 | `"            \"domain\": \"reddit.com\","` | — |
| [SRC-F725E90B2A-L003618](../../tests/test_web_agent.py#L3618) | 3618 | `"            \"title\": \"مناقشة أخرى عن الخدمتين\","` | — |
| [SRC-F725E90B2A-L003619](../../tests/test_web_agent.py#L3619) | 3619 | `"            \"snippet\": \"مناقشة وتجارب مستخدمين حول الخدمتين\","` | — |
| [SRC-F725E90B2A-L003620](../../tests/test_web_agent.py#L3620) | 3620 | `"            \"page_text\": \"مناقشة وتجارب مستخدمين حول الخدمتين\","` | — |
| [SRC-F725E90B2A-L003621](../../tests/test_web_agent.py#L3621) | 3621 | `"            \"platform\": \"reddit\","` | — |
| [SRC-F725E90B2A-L003622](../../tests/test_web_agent.py#L3622) | 3622 | `"            \"providers\": [\"reddit\"],"` | — |
| [SRC-F725E90B2A-L003623](../../tests/test_web_agent.py#L3623) | 3623 | `"        },"` | — |
| [SRC-F725E90B2A-L003624](../../tests/test_web_agent.py#L3624) | 3624 | `"    ]"` | — |
| [SRC-F725E90B2A-L003625](../../tests/test_web_agent.py#L3625) | 3625 | `"    repair_candidate = {"` | — |
| [SRC-F725E90B2A-L003626](../../tests/test_web_agent.py#L3626) | 3626 | `"        **sample_source(2),"` | — |
| [SRC-F725E90B2A-L003627](../../tests/test_web_agent.py#L3627) | 3627 | `"        \"url\": \"https://example.com/unrelated-repair\","` | — |
| [SRC-F725E90B2A-L003628](../../tests/test_web_agent.py#L3628) | 3628 | `"        \"domain\": \"example.com\","` | — |
| [SRC-F725E90B2A-L003629](../../tests/test_web_agent.py#L3629) | 3629 | `"        \"title\": \"معلومات عن الخدمة\","` | — |
| [SRC-F725E90B2A-L003630](../../tests/test_web_agent.py#L3630) | 3630 | `"        \"snippet\": \"معلومات عامة عن الخدمة\","` | — |
| [SRC-F725E90B2A-L003631](../../tests/test_web_agent.py#L3631) | 3631 | `"        \"page_text\": \"معلومات عامة عن الخدمة\","` | — |
| [SRC-F725E90B2A-L003632](../../tests/test_web_agent.py#L3632) | 3632 | `"        \"providers\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L003633](../../tests/test_web_agent.py#L3633) | 3633 | `"    }"` | — |
| [SRC-F725E90B2A-L003634](../../tests/test_web_agent.py#L3634) | 3634 | `"    collect_calls = []"` | — |
| [SRC-F725E90B2A-L003635](../../tests/test_web_agent.py#L3635) | 3635 | `""` | — |
| [SRC-F725E90B2A-L003636](../../tests/test_web_agent.py#L3636) | 3636 | `"    def plan(_question, _history):"` | — |
| [SRC-F725E90B2A-L003637](../../tests/test_web_agent.py#L3637) | 3637 | `"        return {"` | — |
| [SRC-F725E90B2A-L003638](../../tests/test_web_agent.py#L3638) | 3638 | `"            \"queries\": [_question],"` | — |
| [SRC-F725E90B2A-L003639](../../tests/test_web_agent.py#L3639) | 3639 | `"            \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L003640](../../tests/test_web_agent.py#L3640) | 3640 | `"            \"social_focus\": True,"` | — |
| [SRC-F725E90B2A-L003641](../../tests/test_web_agent.py#L3641) | 3641 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003642](../../tests/test_web_agent.py#L3642) | 3642 | `"            \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L003643](../../tests/test_web_agent.py#L3643) | 3643 | `"            \"platforms\": [\"reddit\"],"` | — |
| [SRC-F725E90B2A-L003644](../../tests/test_web_agent.py#L3644) | 3644 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003645](../../tests/test_web_agent.py#L3645) | 3645 | `"        }"` | — |
| [SRC-F725E90B2A-L003646](../../tests/test_web_agent.py#L3646) | 3646 | `""` | — |
| [SRC-F725E90B2A-L003647](../../tests/test_web_agent.py#L3647) | 3647 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L003648](../../tests/test_web_agent.py#L3648) | 3648 | `"        collect_calls.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L003649](../../tests/test_web_agent.py#L3649) | 3649 | `"        if len(collect_calls) == 1:"` | — |
| [SRC-F725E90B2A-L003650](../../tests/test_web_agent.py#L3650) | 3650 | `"            sources = initial_sources"` | — |
| [SRC-F725E90B2A-L003651](../../tests/test_web_agent.py#L3651) | 3651 | `"        else:"` | — |
| [SRC-F725E90B2A-L003652](../../tests/test_web_agent.py#L3652) | 3652 | `"            sources = [repair_candidate]"` | — |
| [SRC-F725E90B2A-L003653](../../tests/test_web_agent.py#L3653) | 3653 | `"        return sources, [], {"` | — |
| [SRC-F725E90B2A-L003654](../../tests/test_web_agent.py#L3654) | 3654 | `"            \"queries_planned\": len(research_plan.get(\"queries\", [])),"` | — |
| [SRC-F725E90B2A-L003655](../../tests/test_web_agent.py#L3655) | 3655 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L003656](../../tests/test_web_agent.py#L3656) | 3656 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L003657](../../tests/test_web_agent.py#L3657) | 3657 | `"            \"unique_sources\": len(sources),"` | — |
| [SRC-F725E90B2A-L003658](../../tests/test_web_agent.py#L3658) | 3658 | `"            \"pages_fetched\": len(sources),"` | — |
| [SRC-F725E90B2A-L003659](../../tests/test_web_agent.py#L3659) | 3659 | `"            \"providers_used\": [\"reddit\"] if len(collect_calls) == 1 else [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L003660](../../tests/test_web_agent.py#L3660) | 3660 | `"            \"provider_counts\": {},"` | — |
| [SRC-F725E90B2A-L003661](../../tests/test_web_agent.py#L3661) | 3661 | `"            \"platform_counts\": {},"` | — |
| [SRC-F725E90B2A-L003662](../../tests/test_web_agent.py#L3662) | 3662 | `"            \"social_direct_results\": len(sources) if len(collect_calls) == 1 else 0,"` | — |
| [SRC-F725E90B2A-L003663](../../tests/test_web_agent.py#L3663) | 3663 | `"            \"depth\": research_plan.get(\"depth\", \"deep\"),"` | — |
| [SRC-F725E90B2A-L003664](../../tests/test_web_agent.py#L3664) | 3664 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003665](../../tests/test_web_agent.py#L3665) | 3665 | `"        }"` | — |
| [SRC-F725E90B2A-L003666](../../tests/test_web_agent.py#L3666) | 3666 | `""` | — |
| [SRC-F725E90B2A-L003667](../../tests/test_web_agent.py#L3667) | 3667 | `"    monkeypatch.setattr(agent, \"_plan_search\", plan)"` | — |
| [SRC-F725E90B2A-L003668](../../tests/test_web_agent.py#L3668) | 3668 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L003669](../../tests/test_web_agent.py#L3669) | 3669 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda _query, _source: True)"` | — |
| [SRC-F725E90B2A-L003670](../../tests/test_web_agent.py#L3670) | 3670 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003671](../../tests/test_web_agent.py#L3671) | 3671 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003672](../../tests/test_web_agent.py#L3672) | 3672 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L003673](../../tests/test_web_agent.py#L3673) | 3673 | `"        lambda *args, **kwargs: ("` | — |
| [SRC-F725E90B2A-L003674](../../tests/test_web_agent.py#L3674) | 3674 | `"            \"السعر مناسب [المصدر 1]. الخصوصية جيدة [المصدر 2]. \""` | — |
| [SRC-F725E90B2A-L003675](../../tests/test_web_agent.py#L3675) | 3675 | `"            \"الاعتمادية مناسبة [المصدر 1].\""` | — |
| [SRC-F725E90B2A-L003676](../../tests/test_web_agent.py#L3676) | 3676 | `"        ),"` | — |
| [SRC-F725E90B2A-L003677](../../tests/test_web_agent.py#L3677) | 3677 | `"    )"` | — |
| [SRC-F725E90B2A-L003678](../../tests/test_web_agent.py#L3678) | 3678 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003679](../../tests/test_web_agent.py#L3679) | 3679 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003680](../../tests/test_web_agent.py#L3680) | 3680 | `"        \"_review_answer\","` | — |
| [SRC-F725E90B2A-L003681](../../tests/test_web_agent.py#L3681) | 3681 | `"        lambda _question, answer, _sources: answer,"` | — |
| [SRC-F725E90B2A-L003682](../../tests/test_web_agent.py#L3682) | 3682 | `"    )"` | — |
| [SRC-F725E90B2A-L003683](../../tests/test_web_agent.py#L3683) | 3683 | `""` | — |
| [SRC-F725E90B2A-L003684](../../tests/test_web_agent.py#L3684) | 3684 | `"    result = agent.answer(question, mode=\"social\")"` | — |
| [SRC-F725E90B2A-L003685](../../tests/test_web_agent.py#L3685) | 3685 | `"    report = result[\"search_report\"]"` | — |
| [SRC-F725E90B2A-L003686](../../tests/test_web_agent.py#L3686) | 3686 | `"    repair_guardrails = report[\"source_guardrails\"][\"criterion_gap_repair\"]"` | — |
| [SRC-F725E90B2A-L003687](../../tests/test_web_agent.py#L3687) | 3687 | `""` | — |
| [SRC-F725E90B2A-L003688](../../tests/test_web_agent.py#L3688) | 3688 | `"    assert len(collect_calls) >= 2"` | — |
| [SRC-F725E90B2A-L003689](../../tests/test_web_agent.py#L3689) | 3689 | `"    assert repair_guardrails[\"rejected_sources\"] >= 1"` | — |
| [SRC-F725E90B2A-L003690](../../tests/test_web_agent.py#L3690) | 3690 | `"    assert repair_guardrails[\"rejection_counts\"][\"not_a_social_platform_source\"] >= 1"` | — |
| [SRC-F725E90B2A-L003691](../../tests/test_web_agent.py#L3691) | 3691 | `"    assert all(\"reddit.com\" in source[\"url\"] for source in result[\"sources\"])"` | — |
| [SRC-F725E90B2A-L003692](../../tests/test_web_agent.py#L3692) | 3692 | `"    assert \"https://example.com/unrelated-repair\" not in {"` | — |
| [SRC-F725E90B2A-L003693](../../tests/test_web_agent.py#L3693) | 3693 | `"        source[\"url\"] for source in result[\"sources\"]"` | — |
| [SRC-F725E90B2A-L003694](../../tests/test_web_agent.py#L3694) | 3694 | `"    }"` | — |
| [SRC-F725E90B2A-L003695](../../tests/test_web_agent.py#L3695) | 3695 | `""` | — |
| [SRC-F725E90B2A-L003696](../../tests/test_web_agent.py#L3696) | 3696 | `"def test_local_answer_exposes_task_spec_without_claiming_search(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003697](../../tests/test_web_agent.py#L3697) | 3697 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003698](../../tests/test_web_agent.py#L3698) | 3698 | `"    result = agent.answer(\"أهلا\")"` | — |
| [SRC-F725E90B2A-L003699](../../tests/test_web_agent.py#L3699) | 3699 | `""` | — |
| [SRC-F725E90B2A-L003700](../../tests/test_web_agent.py#L3700) | 3700 | `"    task_understanding = result[\"task_understanding\"]"` | — |
| [SRC-F725E90B2A-L003701](../../tests/test_web_agent.py#L3701) | 3701 | `"    assert task_understanding[\"task_spec\"][\"schema\"] == \"omarai.task_spec.v1\""` | — |
| [SRC-F725E90B2A-L003702](../../tests/test_web_agent.py#L3702) | 3702 | `"    assert task_understanding[\"tool_execution\"][\"search_outcome\"] == \"not_assessed\""` | — |
| [SRC-F725E90B2A-L003703](../../tests/test_web_agent.py#L3703) | 3703 | `"    assert task_understanding[\"tool_execution\"][\"required_tools\"] == []"` | — |
| [SRC-F725E90B2A-L003704](../../tests/test_web_agent.py#L3704) | 3704 | `"    assert all("` | — |
| [SRC-F725E90B2A-L003705](../../tests/test_web_agent.py#L3705) | 3705 | `"        row[\"status\"] == \"not_required\""` | — |
| [SRC-F725E90B2A-L003706](../../tests/test_web_agent.py#L3706) | 3706 | `"        for row in task_understanding[\"tool_execution\"][\"tool_status_matrix\"]"` | — |
| [SRC-F725E90B2A-L003707](../../tests/test_web_agent.py#L3707) | 3707 | `"    )"` | — |
| [SRC-F725E90B2A-L003708](../../tests/test_web_agent.py#L3708) | 3708 | `"    assert task_understanding[\"actual_queries\"] == []"` | — |
| [SRC-F725E90B2A-L003709](../../tests/test_web_agent.py#L3709) | 3709 | `"    assert task_understanding[\"query_strategy_matrix\"] == []"` | — |
| [SRC-F725E90B2A-L003710](../../tests/test_web_agent.py#L3710) | 3710 | `"    assert task_understanding[\"search_was_attempted\"] is False"` | — |
| [SRC-F725E90B2A-L003711](../../tests/test_web_agent.py#L3711) | 3711 | `""` | — |
| [SRC-F725E90B2A-L003712](../../tests/test_web_agent.py#L3712) | 3712 | `"def test_official_site_without_target_clarifies_before_planning_or_search(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003713](../../tests/test_web_agent.py#L3713) | 3713 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003714](../../tests/test_web_agent.py#L3714) | 3714 | `""` | — |
| [SRC-F725E90B2A-L003715](../../tests/test_web_agent.py#L3715) | 3715 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003716](../../tests/test_web_agent.py#L3716) | 3716 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003717](../../tests/test_web_agent.py#L3717) | 3717 | `"        \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003718](../../tests/test_web_agent.py#L3718) | 3718 | `"        lambda *args, **kwargs: pytest.fail(\"Missing official-site target must be clarified before planning\"),"` | — |
| [SRC-F725E90B2A-L003719](../../tests/test_web_agent.py#L3719) | 3719 | `"    )"` | — |
| [SRC-F725E90B2A-L003720](../../tests/test_web_agent.py#L3720) | 3720 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003721](../../tests/test_web_agent.py#L3721) | 3721 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003722](../../tests/test_web_agent.py#L3722) | 3722 | `"        \"_collect_research\","` | — |
| [SRC-F725E90B2A-L003723](../../tests/test_web_agent.py#L3723) | 3723 | `"        lambda *args, **kwargs: pytest.fail(\"Missing official-site target must not invoke search\"),"` | — |
| [SRC-F725E90B2A-L003724](../../tests/test_web_agent.py#L3724) | 3724 | `"    )"` | — |
| [SRC-F725E90B2A-L003725](../../tests/test_web_agent.py#L3725) | 3725 | `""` | — |
| [SRC-F725E90B2A-L003726](../../tests/test_web_agent.py#L3726) | 3726 | `"    result = agent.answer(\"هات الموقع الرسمي\")"` | — |
| [SRC-F725E90B2A-L003727](../../tests/test_web_agent.py#L3727) | 3727 | `""` | — |
| [SRC-F725E90B2A-L003728](../../tests/test_web_agent.py#L3728) | 3728 | `"    assert result[\"intent_route\"] == \"CLARIFY\""` | — |
| [SRC-F725E90B2A-L003729](../../tests/test_web_agent.py#L3729) | 3729 | `"    assert result[\"kind\"] == \"clarification_needed\""` | — |
| [SRC-F725E90B2A-L003730](../../tests/test_web_agent.py#L3730) | 3730 | `"    assert \"اسم الجهة أو الشركة\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L003731](../../tests/test_web_agent.py#L3731) | 3731 | `"    assert result[\"search_attempted\"] is False"` | — |
| [SRC-F725E90B2A-L003732](../../tests/test_web_agent.py#L3732) | 3732 | `"    assert \"official_destination_target_entity\" in result[\"task_understanding\"][\"task_spec\"][\"missing_required_inputs\"]"` | — |
| [SRC-F725E90B2A-L003733](../../tests/test_web_agent.py#L3733) | 3733 | `""` | — |
| [SRC-F725E90B2A-L003734](../../tests/test_web_agent.py#L3734) | 3734 | `"def test_summary_without_source_clarifies_before_search(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003735](../../tests/test_web_agent.py#L3735) | 3735 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003736](../../tests/test_web_agent.py#L3736) | 3736 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003737](../../tests/test_web_agent.py#L3737) | 3737 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003738](../../tests/test_web_agent.py#L3738) | 3738 | `"        \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003739](../../tests/test_web_agent.py#L3739) | 3739 | `"        lambda *args, **kwargs: pytest.fail(\"Missing summary source must be clarified before planning\"),"` | — |
| [SRC-F725E90B2A-L003740](../../tests/test_web_agent.py#L3740) | 3740 | `"    )"` | — |
| [SRC-F725E90B2A-L003741](../../tests/test_web_agent.py#L3741) | 3741 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003742](../../tests/test_web_agent.py#L3742) | 3742 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003743](../../tests/test_web_agent.py#L3743) | 3743 | `"        \"_collect_research\","` | — |
| [SRC-F725E90B2A-L003744](../../tests/test_web_agent.py#L3744) | 3744 | `"        lambda *args, **kwargs: pytest.fail(\"Missing summary source must not invoke search\"),"` | — |
| [SRC-F725E90B2A-L003745](../../tests/test_web_agent.py#L3745) | 3745 | `"    )"` | — |
| [SRC-F725E90B2A-L003746](../../tests/test_web_agent.py#L3746) | 3746 | `""` | — |
| [SRC-F725E90B2A-L003747](../../tests/test_web_agent.py#L3747) | 3747 | `"    result = agent.answer(\"لخص\")"` | — |
| [SRC-F725E90B2A-L003748](../../tests/test_web_agent.py#L3748) | 3748 | `""` | — |
| [SRC-F725E90B2A-L003749](../../tests/test_web_agent.py#L3749) | 3749 | `"    assert result[\"intent_route\"] == \"CLARIFY\""` | — |
| [SRC-F725E90B2A-L003750](../../tests/test_web_agent.py#L3750) | 3750 | `"    assert \"أرسل النص\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L003751](../../tests/test_web_agent.py#L3751) | 3751 | `"    assert result[\"search_attempted\"] is False"` | — |
| [SRC-F725E90B2A-L003752](../../tests/test_web_agent.py#L3752) | 3752 | `"    assert \"summary_source_url_or_pasted_text\" in result[\"task_understanding\"][\"task_spec\"][\"missing_required_inputs\"]"` | — |
| [SRC-F725E90B2A-L003753](../../tests/test_web_agent.py#L3753) | 3753 | `""` | — |
| [SRC-F725E90B2A-L003754](../../tests/test_web_agent.py#L3754) | 3754 | `"def test_task_spec_controls_generation_context_without_becoming_evidence(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003755](../../tests/test_web_agent.py#L3755) | 3755 | `"    from agents.task_understanding import build_query_strategy_matrix, build_task_spec"` | — |
| [SRC-F725E90B2A-L003756](../../tests/test_web_agent.py#L3756) | 3756 | `""` | — |
| [SRC-F725E90B2A-L003757](../../tests/test_web_agent.py#L3757) | 3757 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003758](../../tests/test_web_agent.py#L3758) | 3758 | `"    captured = {}"` | — |
| [SRC-F725E90B2A-L003759](../../tests/test_web_agent.py#L3759) | 3759 | `""` | — |
| [SRC-F725E90B2A-L003760](../../tests/test_web_agent.py#L3760) | 3760 | `"    question = ("` | — |
| [SRC-F725E90B2A-L003761](../../tests/test_web_agent.py#L3761) | 3761 | `"        \"قارن السيارات الكهربائية في مصر من حيث السعر والضمان، \""` | — |
| [SRC-F725E90B2A-L003762](../../tests/test_web_agent.py#L3762) | 3762 | `"        \"اشرح ببساطة مع أمثلة وروابط مباشرة\""` | — |
| [SRC-F725E90B2A-L003763](../../tests/test_web_agent.py#L3763) | 3763 | `"    )"` | — |
| [SRC-F725E90B2A-L003764](../../tests/test_web_agent.py#L3764) | 3764 | `"    task_spec = build_task_spec("` | — |
| [SRC-F725E90B2A-L003765](../../tests/test_web_agent.py#L3765) | 3765 | `"        question,"` | — |
| [SRC-F725E90B2A-L003766](../../tests/test_web_agent.py#L3766) | 3766 | `"        mode=\"deep\","` | — |
| [SRC-F725E90B2A-L003767](../../tests/test_web_agent.py#L3767) | 3767 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-F725E90B2A-L003768](../../tests/test_web_agent.py#L3768) | 3768 | `"    )"` | — |
| [SRC-F725E90B2A-L003769](../../tests/test_web_agent.py#L3769) | 3769 | `"    initial_queries = [compact_search_query(question)]"` | — |
| [SRC-F725E90B2A-L003770](../../tests/test_web_agent.py#L3770) | 3770 | `"    matrix = build_query_strategy_matrix("` | — |
| [SRC-F725E90B2A-L003771](../../tests/test_web_agent.py#L3771) | 3771 | `"        question,"` | — |
| [SRC-F725E90B2A-L003772](../../tests/test_web_agent.py#L3772) | 3772 | `"        task_spec,"` | — |
| [SRC-F725E90B2A-L003773](../../tests/test_web_agent.py#L3773) | 3773 | `"        initial_queries,"` | — |
| [SRC-F725E90B2A-L003774](../../tests/test_web_agent.py#L3774) | 3774 | `"        limit=4,"` | — |
| [SRC-F725E90B2A-L003775](../../tests/test_web_agent.py#L3775) | 3775 | `"        compact_fn=compact_search_query,"` | — |
| [SRC-F725E90B2A-L003776](../../tests/test_web_agent.py#L3776) | 3776 | `"    )"` | — |
| [SRC-F725E90B2A-L003777](../../tests/test_web_agent.py#L3777) | 3777 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L003778](../../tests/test_web_agent.py#L3778) | 3778 | `"        \"depth\": \"deep\","` | — |
