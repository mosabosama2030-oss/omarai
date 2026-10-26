# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **034**
- سجلات الأسطر: **800**
- النطاق: SRC-F725E90B2A-L002827 إلى SRC-DE7EABE998-L000365
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-F725E90B2A — [tests/test_web_agent.py](../../tests/test_web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-F725E90B2A-L002827](../../tests/test_web_agent.py#L2827) | 2827 | `"        \"malformed candidate\","` | — |
| [SRC-F725E90B2A-L002828](../../tests/test_web_agent.py#L2828) | 2828 | `"        {"` | — |
| [SRC-F725E90B2A-L002829](../../tests/test_web_agent.py#L2829) | 2829 | `"            \"title\": \"Unsafe scheme\","` | — |
| [SRC-F725E90B2A-L002830](../../tests/test_web_agent.py#L2830) | 2830 | `"            \"url\": \"javascript:alert(1)\","` | — |
| [SRC-F725E90B2A-L002831](../../tests/test_web_agent.py#L2831) | 2831 | `"            \"snippet\": \"Renewable energy storage report\","` | — |
| [SRC-F725E90B2A-L002832](../../tests/test_web_agent.py#L2832) | 2832 | `"        },"` | — |
| [SRC-F725E90B2A-L002833](../../tests/test_web_agent.py#L2833) | 2833 | `"        {"` | — |
| [SRC-F725E90B2A-L002834](../../tests/test_web_agent.py#L2834) | 2834 | `"            \"title\": \"Translated mirror\","` | — |
| [SRC-F725E90B2A-L002835](../../tests/test_web_agent.py#L2835) | 2835 | `"            \"url\": \"https://translate.google.com/translate?u=https%3A%2F%2Fexample.com\","` | — |
| [SRC-F725E90B2A-L002836](../../tests/test_web_agent.py#L2836) | 2836 | `"            \"snippet\": \"Renewable energy storage\","` | — |
| [SRC-F725E90B2A-L002837](../../tests/test_web_agent.py#L2837) | 2837 | `"        },"` | — |
| [SRC-F725E90B2A-L002838](../../tests/test_web_agent.py#L2838) | 2838 | `"        {"` | — |
| [SRC-F725E90B2A-L002839](../../tests/test_web_agent.py#L2839) | 2839 | `"            \"title\": \"Gardening tips\","` | — |
| [SRC-F725E90B2A-L002840](../../tests/test_web_agent.py#L2840) | 2840 | `"            \"url\": \"https://example.com/gardening\","` | — |
| [SRC-F725E90B2A-L002841](../../tests/test_web_agent.py#L2841) | 2841 | `"            \"snippet\": \"Gardening flowers and house plants\","` | — |
| [SRC-F725E90B2A-L002842](../../tests/test_web_agent.py#L2842) | 2842 | `"        },"` | — |
| [SRC-F725E90B2A-L002843](../../tests/test_web_agent.py#L2843) | 2843 | `"    ]"` | — |
| [SRC-F725E90B2A-L002844](../../tests/test_web_agent.py#L2844) | 2844 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", lambda _q: [dict(x) if isinstance(x, dict) else x for x in candidates])"` | — |
| [SRC-F725E90B2A-L002845](../../tests/test_web_agent.py#L2845) | 2845 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", lambda _q: [dict(x) if isinstance(x, dict) else x for x in candidates])"` | — |
| [SRC-F725E90B2A-L002846](../../tests/test_web_agent.py#L2846) | 2846 | `"    monkeypatch.setattr(agent, \"_search_news\", lambda _q: [])"` | — |
| [SRC-F725E90B2A-L002847](../../tests/test_web_agent.py#L2847) | 2847 | `""` | — |
| [SRC-F725E90B2A-L002848](../../tests/test_web_agent.py#L2848) | 2848 | `"    with pytest.raises(RuntimeError, match=\"لم تُرجع موصلات البحث\"):"` | — |
| [SRC-F725E90B2A-L002849](../../tests/test_web_agent.py#L2849) | 2849 | `"        agent._search_web(query)"` | — |
| [SRC-F725E90B2A-L002850](../../tests/test_web_agent.py#L2850) | 2850 | `""` | — |
| [SRC-F725E90B2A-L002851](../../tests/test_web_agent.py#L2851) | 2851 | `"    diagnostic = next("` | — |
| [SRC-F725E90B2A-L002852](../../tests/test_web_agent.py#L2852) | 2852 | `"        item for item in agent._provider_diagnostics"` | — |
| [SRC-F725E90B2A-L002853](../../tests/test_web_agent.py#L2853) | 2853 | `"        if item.get(\"provider\") == \"duckduckgo_html\""` | — |
| [SRC-F725E90B2A-L002854](../../tests/test_web_agent.py#L2854) | 2854 | `"    )"` | — |
| [SRC-F725E90B2A-L002855](../../tests/test_web_agent.py#L2855) | 2855 | `"    assert diagnostic[\"status\"] == \"filtered_all\""` | — |
| [SRC-F725E90B2A-L002856](../../tests/test_web_agent.py#L2856) | 2856 | `"    assert diagnostic[\"result_count\"] == 4"` | — |
| [SRC-F725E90B2A-L002857](../../tests/test_web_agent.py#L2857) | 2857 | `"    assert diagnostic[\"accepted_count\"] == 0"` | — |
| [SRC-F725E90B2A-L002858](../../tests/test_web_agent.py#L2858) | 2858 | `"    assert diagnostic[\"rejected_count\"] == 4"` | — |
| [SRC-F725E90B2A-L002859](../../tests/test_web_agent.py#L2859) | 2859 | `"    assert diagnostic[\"rejection_counts\"] == {"` | — |
| [SRC-F725E90B2A-L002860](../../tests/test_web_agent.py#L2860) | 2860 | `"        \"malformed_candidate\": 1,"` | — |
| [SRC-F725E90B2A-L002861](../../tests/test_web_agent.py#L2861) | 2861 | `"        \"invalid_url_or_unsafe_target\": 1,"` | — |
| [SRC-F725E90B2A-L002862](../../tests/test_web_agent.py#L2862) | 2862 | `"        \"blocked_domain\": 1,"` | — |
| [SRC-F725E90B2A-L002863](../../tests/test_web_agent.py#L2863) | 2863 | `"        \"relevance_below_threshold\": 1,"` | — |
| [SRC-F725E90B2A-L002864](../../tests/test_web_agent.py#L2864) | 2864 | `"    }"` | — |
| [SRC-F725E90B2A-L002865](../../tests/test_web_agent.py#L2865) | 2865 | `"    assert sum(diagnostic[\"rejection_counts\"].values()) == diagnostic[\"rejected_count\"]"` | — |
| [SRC-F725E90B2A-L002866](../../tests/test_web_agent.py#L2866) | 2866 | `""` | — |
| [SRC-F725E90B2A-L002867](../../tests/test_web_agent.py#L2867) | 2867 | `""` | — |
| [SRC-F725E90B2A-L002868](../../tests/test_web_agent.py#L2868) | 2868 | `"def test_search_web_classifies_http_302_as_degraded_without_following_provider_redirect(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002869](../../tests/test_web_agent.py#L2869) | 2869 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002870](../../tests/test_web_agent.py#L2870) | 2870 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L002871](../../tests/test_web_agent.py#L2871) | 2871 | `""` | — |
| [SRC-F725E90B2A-L002872](../../tests/test_web_agent.py#L2872) | 2872 | `"    def redirect_response(query):"` | — |
| [SRC-F725E90B2A-L002873](../../tests/test_web_agent.py#L2873) | 2873 | `"        calls.append((\"duckduckgo_html\", query))"` | — |
| [SRC-F725E90B2A-L002874](../../tests/test_web_agent.py#L2874) | 2874 | `"        raise RuntimeError(\"HTTP 302\")"` | — |
| [SRC-F725E90B2A-L002875](../../tests/test_web_agent.py#L2875) | 2875 | `""` | — |
| [SRC-F725E90B2A-L002876](../../tests/test_web_agent.py#L2876) | 2876 | `"    def no_results(query):"` | — |
| [SRC-F725E90B2A-L002877](../../tests/test_web_agent.py#L2877) | 2877 | `"        calls.append((\"bing_rss\", query))"` | — |
| [SRC-F725E90B2A-L002878](../../tests/test_web_agent.py#L2878) | 2878 | `"        return []"` | — |
| [SRC-F725E90B2A-L002879](../../tests/test_web_agent.py#L2879) | 2879 | `""` | — |
| [SRC-F725E90B2A-L002880](../../tests/test_web_agent.py#L2880) | 2880 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", redirect_response)"` | — |
| [SRC-F725E90B2A-L002881](../../tests/test_web_agent.py#L2881) | 2881 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", no_results)"` | — |
| [SRC-F725E90B2A-L002882](../../tests/test_web_agent.py#L2882) | 2882 | `"    monkeypatch.setattr(agent, \"_search_news\", lambda _q: [])"` | — |
| [SRC-F725E90B2A-L002883](../../tests/test_web_agent.py#L2883) | 2883 | `""` | — |
| [SRC-F725E90B2A-L002884](../../tests/test_web_agent.py#L2884) | 2884 | `"    with pytest.raises(RuntimeError, match=\"لم تُرجع موصلات البحث\"):"` | — |
| [SRC-F725E90B2A-L002885](../../tests/test_web_agent.py#L2885) | 2885 | `"        agent._search_web(\"renewable energy storage\")"` | — |
| [SRC-F725E90B2A-L002886](../../tests/test_web_agent.py#L2886) | 2886 | `""` | — |
| [SRC-F725E90B2A-L002887](../../tests/test_web_agent.py#L2887) | 2887 | `"    diagnostic = next("` | — |
| [SRC-F725E90B2A-L002888](../../tests/test_web_agent.py#L2888) | 2888 | `"        item for item in agent._provider_diagnostics"` | — |
| [SRC-F725E90B2A-L002889](../../tests/test_web_agent.py#L2889) | 2889 | `"        if item.get(\"provider\") == \"duckduckgo_html\""` | — |
| [SRC-F725E90B2A-L002890](../../tests/test_web_agent.py#L2890) | 2890 | `"    )"` | — |
| [SRC-F725E90B2A-L002891](../../tests/test_web_agent.py#L2891) | 2891 | `"    assert diagnostic[\"status\"] == \"http_error\""` | — |
| [SRC-F725E90B2A-L002892](../../tests/test_web_agent.py#L2892) | 2892 | `"    assert diagnostic[\"error\"] == \"RuntimeError: HTTP 302\""` | — |
| [SRC-F725E90B2A-L002893](../../tests/test_web_agent.py#L2893) | 2893 | `"    assert sum(provider == \"duckduckgo_html\" for provider, _query in calls) == 1"` | — |
| [SRC-F725E90B2A-L002894](../../tests/test_web_agent.py#L2894) | 2894 | `""` | — |
| [SRC-F725E90B2A-L002895](../../tests/test_web_agent.py#L2895) | 2895 | `""` | — |
| [SRC-F725E90B2A-L002896](../../tests/test_web_agent.py#L2896) | 2896 | `"def test_relevance_filter_compacts_prompt_and_rejects_instruction_only_queries():"` | — |
| [SRC-F725E90B2A-L002897](../../tests/test_web_agent.py#L2897) | 2897 | `"    question = \"ما عاصمة مصر؟ اذكر مصدرًا موثوقًا مع رابط مباشر، وأجب بالعربية بإيجاز.\""` | — |
| [SRC-F725E90B2A-L002898](../../tests/test_web_agent.py#L2898) | 2898 | `"    assert _relevance_ratio(question, \"عاصمة مصر القاهرة\") >= 0.20"` | — |
| [SRC-F725E90B2A-L002899](../../tests/test_web_agent.py#L2899) | 2899 | `"    assert _relevance_ratio("` | — |
| [SRC-F725E90B2A-L002900](../../tests/test_web_agent.py#L2900) | 2900 | `"        \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\","` | — |
| [SRC-F725E90B2A-L002901](../../tests/test_web_agent.py#L2901) | 2901 | `"        \"Football results and unrelated match reports\","` | — |
| [SRC-F725E90B2A-L002902](../../tests/test_web_agent.py#L2902) | 2902 | `"    ) == 0.0"` | — |
| [SRC-F725E90B2A-L002903](../../tests/test_web_agent.py#L2903) | 2903 | `""` | — |
| [SRC-F725E90B2A-L002904](../../tests/test_web_agent.py#L2904) | 2904 | `""` | — |
| [SRC-F725E90B2A-L002905](../../tests/test_web_agent.py#L2905) | 2905 | `"def test_relevance_query_tokens_reject_site_only_and_modifier_only_queries():"` | — |
| [SRC-F725E90B2A-L002906](../../tests/test_web_agent.py#L2906) | 2906 | `"    assert _relevance_query_tokens(\"site:reddit.com\") == set()"` | — |
| [SRC-F725E90B2A-L002907](../../tests/test_web_agent.py#L2907) | 2907 | `"    assert _relevance_query_tokens(\"risks limitations alternatives\") == set()"` | — |
| [SRC-F725E90B2A-L002908](../../tests/test_web_agent.py#L2908) | 2908 | `"    assert _relevance_query_tokens(\"السيارات الكهربائية المستعملة في مصر\")"` | — |
| [SRC-F725E90B2A-L002909](../../tests/test_web_agent.py#L2909) | 2909 | `""` | — |
| [SRC-F725E90B2A-L002910](../../tests/test_web_agent.py#L2910) | 2910 | `""` | — |
| [SRC-F725E90B2A-L002911](../../tests/test_web_agent.py#L2911) | 2911 | `"def test_search_web_compacts_request_before_provider_dispatch(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002912](../../tests/test_web_agent.py#L2912) | 2912 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002913](../../tests/test_web_agent.py#L2913) | 2913 | `"    seen = []"` | — |
| [SRC-F725E90B2A-L002914](../../tests/test_web_agent.py#L2914) | 2914 | `""` | — |
| [SRC-F725E90B2A-L002915](../../tests/test_web_agent.py#L2915) | 2915 | `"    def capture(query):"` | — |
| [SRC-F725E90B2A-L002916](../../tests/test_web_agent.py#L2916) | 2916 | `"        seen.append(query)"` | — |
| [SRC-F725E90B2A-L002917](../../tests/test_web_agent.py#L2917) | 2917 | `"        return []"` | — |
| [SRC-F725E90B2A-L002918](../../tests/test_web_agent.py#L2918) | 2918 | `""` | — |
| [SRC-F725E90B2A-L002919](../../tests/test_web_agent.py#L2919) | 2919 | `"    for env_name in ("` | — |
| [SRC-F725E90B2A-L002920](../../tests/test_web_agent.py#L2920) | 2920 | `"        \"DEEPSEEK_SEARCH_API_KEY\","` | — |
| [SRC-F725E90B2A-L002921](../../tests/test_web_agent.py#L2921) | 2921 | `"        \"BRAVE_SEARCH_API_KEY\","` | — |
| [SRC-F725E90B2A-L002922](../../tests/test_web_agent.py#L2922) | 2922 | `"        \"TAVILY_API_KEY\","` | — |
| [SRC-F725E90B2A-L002923](../../tests/test_web_agent.py#L2923) | 2923 | `"    ):"` | — |
| [SRC-F725E90B2A-L002924](../../tests/test_web_agent.py#L2924) | 2924 | `"        monkeypatch.delenv(env_name, raising=False)"` | — |
| [SRC-F725E90B2A-L002925](../../tests/test_web_agent.py#L2925) | 2925 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", capture)"` | — |
| [SRC-F725E90B2A-L002926](../../tests/test_web_agent.py#L2926) | 2926 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", capture)"` | — |
| [SRC-F725E90B2A-L002927](../../tests/test_web_agent.py#L2927) | 2927 | `""` | — |
| [SRC-F725E90B2A-L002928](../../tests/test_web_agent.py#L2928) | 2928 | `"    raw_question = ("` | — |
| [SRC-F725E90B2A-L002929](../../tests/test_web_agent.py#L2929) | 2929 | `"        \"ما عاصمة مصر؟ اذكر مصدرًا موثوقًا مع رابط مباشر، وأجب بالعربية بإيجاز.\""` | — |
| [SRC-F725E90B2A-L002930](../../tests/test_web_agent.py#L2930) | 2930 | `"    )"` | — |
| [SRC-F725E90B2A-L002931](../../tests/test_web_agent.py#L2931) | 2931 | `"    with pytest.raises(RuntimeError, match=\"لم تُرجع موصلات البحث\"):"` | — |
| [SRC-F725E90B2A-L002932](../../tests/test_web_agent.py#L2932) | 2932 | `"        agent._search_web(raw_question)"` | — |
| [SRC-F725E90B2A-L002933](../../tests/test_web_agent.py#L2933) | 2933 | `""` | — |
| [SRC-F725E90B2A-L002934](../../tests/test_web_agent.py#L2934) | 2934 | `"    expected = _normalize_search_query(compact_search_query(raw_question))"` | — |
| [SRC-F725E90B2A-L002935](../../tests/test_web_agent.py#L2935) | 2935 | `"    assert seen"` | — |
| [SRC-F725E90B2A-L002936](../../tests/test_web_agent.py#L2936) | 2936 | `"    assert set(seen) == {expected}"` | — |
| [SRC-F725E90B2A-L002937](../../tests/test_web_agent.py#L2937) | 2937 | `"    assert len(expected) <= 240"` | — |
| [SRC-F725E90B2A-L002938](../../tests/test_web_agent.py#L2938) | 2938 | `"    assert \"رابط مباشر\" not in \" \".join(seen)"` | — |
| [SRC-F725E90B2A-L002939](../../tests/test_web_agent.py#L2939) | 2939 | `""` | — |
| [SRC-F725E90B2A-L002940](../../tests/test_web_agent.py#L2940) | 2940 | `""` | — |
| [SRC-F725E90B2A-L002941](../../tests/test_web_agent.py#L2941) | 2941 | `"def test_search_web_does_not_dispatch_instruction_only_query(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002942](../../tests/test_web_agent.py#L2942) | 2942 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002943](../../tests/test_web_agent.py#L2943) | 2943 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002944](../../tests/test_web_agent.py#L2944) | 2944 | `"        agent, \"_search_duckduckgo_html\","` | — |
| [SRC-F725E90B2A-L002945](../../tests/test_web_agent.py#L2945) | 2945 | `"        lambda query: pytest.fail(f\"provider should not receive {query!r}\"),"` | — |
| [SRC-F725E90B2A-L002946](../../tests/test_web_agent.py#L2946) | 2946 | `"    )"` | — |
| [SRC-F725E90B2A-L002947](../../tests/test_web_agent.py#L2947) | 2947 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002948](../../tests/test_web_agent.py#L2948) | 2948 | `"        agent, \"_search_bing_rss\","` | — |
| [SRC-F725E90B2A-L002949](../../tests/test_web_agent.py#L2949) | 2949 | `"        lambda query: pytest.fail(f\"provider should not receive {query!r}\"),"` | — |
| [SRC-F725E90B2A-L002950](../../tests/test_web_agent.py#L2950) | 2950 | `"    )"` | — |
| [SRC-F725E90B2A-L002951](../../tests/test_web_agent.py#L2951) | 2951 | `"    results = agent._search_web(\"اذكر مصادر موثوقة، روابط مباشرة، باختصار\")"` | — |
| [SRC-F725E90B2A-L002952](../../tests/test_web_agent.py#L2952) | 2952 | `"    assert results == []"` | — |
| [SRC-F725E90B2A-L002953](../../tests/test_web_agent.py#L2953) | 2953 | `""` | — |
| [SRC-F725E90B2A-L002954](../../tests/test_web_agent.py#L2954) | 2954 | `""` | — |
| [SRC-F725E90B2A-L002955](../../tests/test_web_agent.py#L2955) | 2955 | `"def test_plan_search_does_not_call_planner_without_a_topic(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002956](../../tests/test_web_agent.py#L2956) | 2956 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002957](../../tests/test_web_agent.py#L2957) | 2957 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L002958](../../tests/test_web_agent.py#L2958) | 2958 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002959](../../tests/test_web_agent.py#L2959) | 2959 | `"        agent, \"_request_completion\","` | — |
| [SRC-F725E90B2A-L002960](../../tests/test_web_agent.py#L2960) | 2960 | `"        lambda *args, **kwargs: pytest.fail(\"planner should not run without a topic\"),"` | — |
| [SRC-F725E90B2A-L002961](../../tests/test_web_agent.py#L2961) | 2961 | `"    )"` | — |
| [SRC-F725E90B2A-L002962](../../tests/test_web_agent.py#L2962) | 2962 | `"    plan = agent._plan_search("` | — |
| [SRC-F725E90B2A-L002963](../../tests/test_web_agent.py#L2963) | 2963 | `"        \"استخدم مصادر متعددة، واذكر روابط المصادر\","` | — |
| [SRC-F725E90B2A-L002964](../../tests/test_web_agent.py#L2964) | 2964 | `"        [],"` | — |
| [SRC-F725E90B2A-L002965](../../tests/test_web_agent.py#L2965) | 2965 | `"    )"` | — |
| [SRC-F725E90B2A-L002966](../../tests/test_web_agent.py#L2966) | 2966 | `"    assert plan[\"queries\"] == []"` | — |
| [SRC-F725E90B2A-L002967](../../tests/test_web_agent.py#L2967) | 2967 | `""` | — |
| [SRC-F725E90B2A-L002968](../../tests/test_web_agent.py#L2968) | 2968 | `""` | — |
| [SRC-F725E90B2A-L002969](../../tests/test_web_agent.py#L2969) | 2969 | `"def test_plan_search_compacts_followup_query_before_fallback(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002970](../../tests/test_web_agent.py#L2970) | 2970 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002971](../../tests/test_web_agent.py#L2971) | 2971 | `"    agent.api_key = \"\""` | — |
| [SRC-F725E90B2A-L002972](../../tests/test_web_agent.py#L2972) | 2972 | `"    history = ["` | — |
| [SRC-F725E90B2A-L002973](../../tests/test_web_agent.py#L2973) | 2973 | `"        {"` | — |
| [SRC-F725E90B2A-L002974](../../tests/test_web_agent.py#L2974) | 2974 | `"            \"role\": \"user\","` | — |
| [SRC-F725E90B2A-L002975](../../tests/test_web_agent.py#L2975) | 2975 | `"            \"content\": ("` | — |
| [SRC-F725E90B2A-L002976](../../tests/test_web_agent.py#L2976) | 2976 | `"                \"قارن السيارات الكهربائية في مصر. استخدم مصادر متعددة، \""` | — |
| [SRC-F725E90B2A-L002977](../../tests/test_web_agent.py#L2977) | 2977 | `"                \"واذكر روابط المصادر وأجب بإيجاز.\""` | — |
| [SRC-F725E90B2A-L002978](../../tests/test_web_agent.py#L2978) | 2978 | `"            ),"` | — |
| [SRC-F725E90B2A-L002979](../../tests/test_web_agent.py#L2979) | 2979 | `"        },"` | — |
| [SRC-F725E90B2A-L002980](../../tests/test_web_agent.py#L2980) | 2980 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن مقارنة موثقة.\"},"` | — |
| [SRC-F725E90B2A-L002981](../../tests/test_web_agent.py#L2981) | 2981 | `"    ]"` | — |
| [SRC-F725E90B2A-L002982](../../tests/test_web_agent.py#L2982) | 2982 | `"    plan = agent._plan_search(\"وطب الأسعار الحالية؟\", history)"` | — |
| [SRC-F725E90B2A-L002983](../../tests/test_web_agent.py#L2983) | 2983 | `""` | — |
| [SRC-F725E90B2A-L002984](../../tests/test_web_agent.py#L2984) | 2984 | `"    assert plan[\"queries\"]"` | — |
| [SRC-F725E90B2A-L002985](../../tests/test_web_agent.py#L2985) | 2985 | `"    assert all(len(query) <= 240 for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L002986](../../tests/test_web_agent.py#L2986) | 2986 | `"    assert any(\"السيارات الكهربائية\" in query for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L002987](../../tests/test_web_agent.py#L2987) | 2987 | `"    assert all("` | — |
| [SRC-F725E90B2A-L002988](../../tests/test_web_agent.py#L2988) | 2988 | `"        \"روابط المصادر\" not in query and \"أجب بإيجاز\" not in query"` | — |
| [SRC-F725E90B2A-L002989](../../tests/test_web_agent.py#L2989) | 2989 | `"        for query in plan[\"queries\"]"` | — |
| [SRC-F725E90B2A-L002990](../../tests/test_web_agent.py#L2990) | 2990 | `"    )"` | — |
| [SRC-F725E90B2A-L002991](../../tests/test_web_agent.py#L2991) | 2991 | `""` | — |
| [SRC-F725E90B2A-L002992](../../tests/test_web_agent.py#L2992) | 2992 | `""` | — |
| [SRC-F725E90B2A-L002993](../../tests/test_web_agent.py#L2993) | 2993 | `"@pytest.mark.parametrize(\"fallback_queries\", [[], None])"` | — |
| [SRC-F725E90B2A-L002994](../../tests/test_web_agent.py#L2994) | 2994 | `"def test_auto_mode_does_not_reinsert_raw_question_when_fallback_has_no_query("` | — |
| [SRC-F725E90B2A-L002995](../../tests/test_web_agent.py#L2995) | 2995 | `"    monkeypatch, fallback_queries"` | — |
| [SRC-F725E90B2A-L002996](../../tests/test_web_agent.py#L2996) | 2996 | `"):"` | — |
| [SRC-F725E90B2A-L002997](../../tests/test_web_agent.py#L2997) | 2997 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002998](../../tests/test_web_agent.py#L2998) | 2998 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L002999](../../tests/test_web_agent.py#L2999) | 2999 | `"    question = ("` | — |
| [SRC-F725E90B2A-L003000](../../tests/test_web_agent.py#L3000) | 3000 | `"        \"ما عيوب السيارات الكهربائية المستعملة في مصر؟ \""` | — |
| [SRC-F725E90B2A-L003001](../../tests/test_web_agent.py#L3001) | 3001 | `"        \"اذكر مصادر موثوقة وروابط مباشرة وأجب بإيجاز.\""` | — |
| [SRC-F725E90B2A-L003002](../../tests/test_web_agent.py#L3002) | 3002 | `"    )"` | — |
| [SRC-F725E90B2A-L003003](../../tests/test_web_agent.py#L3003) | 3003 | `"    observed_plans = []"` | — |
| [SRC-F725E90B2A-L003004](../../tests/test_web_agent.py#L3004) | 3004 | `""` | — |
| [SRC-F725E90B2A-L003005](../../tests/test_web_agent.py#L3005) | 3005 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003006](../../tests/test_web_agent.py#L3006) | 3006 | `"        \"agents.web_agent.route_intent\","` | — |
| [SRC-F725E90B2A-L003007](../../tests/test_web_agent.py#L3007) | 3007 | `"        lambda *args, **kwargs: {\"route\": \"WEB_SIMPLE\", \"reason\": \"test\"},"` | — |
| [SRC-F725E90B2A-L003008](../../tests/test_web_agent.py#L3008) | 3008 | `"    )"` | — |
| [SRC-F725E90B2A-L003009](../../tests/test_web_agent.py#L3009) | 3009 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003010](../../tests/test_web_agent.py#L3010) | 3010 | `"        agent, \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003011](../../tests/test_web_agent.py#L3011) | 3011 | `"        lambda _question, _history: {"` | — |
| [SRC-F725E90B2A-L003012](../../tests/test_web_agent.py#L3012) | 3012 | `"            \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L003013](../../tests/test_web_agent.py#L3013) | 3013 | `"            \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L003014](../../tests/test_web_agent.py#L3014) | 3014 | `"            \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003015](../../tests/test_web_agent.py#L3015) | 3015 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003016](../../tests/test_web_agent.py#L3016) | 3016 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003017](../../tests/test_web_agent.py#L3017) | 3017 | `"            \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003018](../../tests/test_web_agent.py#L3018) | 3018 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003019](../../tests/test_web_agent.py#L3019) | 3019 | `"        },"` | — |
| [SRC-F725E90B2A-L003020](../../tests/test_web_agent.py#L3020) | 3020 | `"    )"` | — |
| [SRC-F725E90B2A-L003021](../../tests/test_web_agent.py#L3021) | 3021 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003022](../../tests/test_web_agent.py#L3022) | 3022 | `"        \"agents.web_agent.fallback_plan\","` | — |
| [SRC-F725E90B2A-L003023](../../tests/test_web_agent.py#L3023) | 3023 | `"        lambda *args, **kwargs: {\"queries\": fallback_queries},"` | — |
| [SRC-F725E90B2A-L003024](../../tests/test_web_agent.py#L3024) | 3024 | `"    )"` | — |
| [SRC-F725E90B2A-L003025](../../tests/test_web_agent.py#L3025) | 3025 | `""` | — |
| [SRC-F725E90B2A-L003026](../../tests/test_web_agent.py#L3026) | 3026 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L003027](../../tests/test_web_agent.py#L3027) | 3027 | `"        observed_plans.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L003028](../../tests/test_web_agent.py#L3028) | 3028 | `"        return [], [], {"` | — |
| [SRC-F725E90B2A-L003029](../../tests/test_web_agent.py#L3029) | 3029 | `"            \"queries_planned\": len(research_plan.get(\"queries\", [])),"` | — |
| [SRC-F725E90B2A-L003030](../../tests/test_web_agent.py#L3030) | 3030 | `"            \"queries_attempted\": 0,"` | — |
| [SRC-F725E90B2A-L003031](../../tests/test_web_agent.py#L3031) | 3031 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L003032](../../tests/test_web_agent.py#L3032) | 3032 | `"            \"unique_sources\": 0,"` | — |
| [SRC-F725E90B2A-L003033](../../tests/test_web_agent.py#L3033) | 3033 | `"            \"pages_fetched\": 0,"` | — |
| [SRC-F725E90B2A-L003034](../../tests/test_web_agent.py#L3034) | 3034 | `"            \"providers_used\": [],"` | — |
| [SRC-F725E90B2A-L003035](../../tests/test_web_agent.py#L3035) | 3035 | `"            \"platform_counts\": {},"` | — |
| [SRC-F725E90B2A-L003036](../../tests/test_web_agent.py#L3036) | 3036 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L003037](../../tests/test_web_agent.py#L3037) | 3037 | `"            \"depth\": research_plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-F725E90B2A-L003038](../../tests/test_web_agent.py#L3038) | 3038 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003039](../../tests/test_web_agent.py#L3039) | 3039 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L003040](../../tests/test_web_agent.py#L3040) | 3040 | `"        }"` | — |
| [SRC-F725E90B2A-L003041](../../tests/test_web_agent.py#L3041) | 3041 | `""` | — |
| [SRC-F725E90B2A-L003042](../../tests/test_web_agent.py#L3042) | 3042 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L003043](../../tests/test_web_agent.py#L3043) | 3043 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"لا تتوفر مصادر كافية.\")"` | — |
| [SRC-F725E90B2A-L003044](../../tests/test_web_agent.py#L3044) | 3044 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda _question, answer, _sources: answer)"` | — |
| [SRC-F725E90B2A-L003045](../../tests/test_web_agent.py#L3045) | 3045 | `""` | — |
| [SRC-F725E90B2A-L003046](../../tests/test_web_agent.py#L3046) | 3046 | `"    agent.answer(question, mode=\"auto\")"` | — |
| [SRC-F725E90B2A-L003047](../../tests/test_web_agent.py#L3047) | 3047 | `""` | — |
| [SRC-F725E90B2A-L003048](../../tests/test_web_agent.py#L3048) | 3048 | `"    assert observed_plans"` | — |
| [SRC-F725E90B2A-L003049](../../tests/test_web_agent.py#L3049) | 3049 | `"    assert question not in observed_plans[0][\"queries\"]"` | — |
| [SRC-F725E90B2A-L003050](../../tests/test_web_agent.py#L3050) | 3050 | `"    assert observed_plans[0][\"queries\"]"` | — |
| [SRC-F725E90B2A-L003051](../../tests/test_web_agent.py#L3051) | 3051 | `"    assert observed_plans[0][\"queries\"][0] == compact_search_query(question)"` | — |
| [SRC-F725E90B2A-L003052](../../tests/test_web_agent.py#L3052) | 3052 | `""` | — |
| [SRC-F725E90B2A-L003053](../../tests/test_web_agent.py#L3053) | 3053 | `""` | — |
| [SRC-F725E90B2A-L003054](../../tests/test_web_agent.py#L3054) | 3054 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L003055](../../tests/test_web_agent.py#L3055) | 3055 | `"    (\"question\", \"planned_query\"),"` | — |
| [SRC-F725E90B2A-L003056](../../tests/test_web_agent.py#L3056) | 3056 | `"    ["` | — |
| [SRC-F725E90B2A-L003057](../../tests/test_web_agent.py#L3057) | 3057 | `"        ("` | — |
| [SRC-F725E90B2A-L003058](../../tests/test_web_agent.py#L3058) | 3058 | `"            ("` | — |
| [SRC-F725E90B2A-L003059](../../tests/test_web_agent.py#L3059) | 3059 | `"                \"ما عيوب السيارات الكهربائية المستعملة في مصر؟ \""` | — |
| [SRC-F725E90B2A-L003060](../../tests/test_web_agent.py#L3060) | 3060 | `"                \"اذكر مصادر موثوقة وروابط مباشرة وأجب بإيجاز.\""` | — |
| [SRC-F725E90B2A-L003061](../../tests/test_web_agent.py#L3061) | 3061 | `"            ),"` | — |
| [SRC-F725E90B2A-L003062](../../tests/test_web_agent.py#L3062) | 3062 | `"            None,"` | — |
| [SRC-F725E90B2A-L003063](../../tests/test_web_agent.py#L3063) | 3063 | `"        ),"` | — |
| [SRC-F725E90B2A-L003064](../../tests/test_web_agent.py#L3064) | 3064 | `"        ("` | — |
| [SRC-F725E90B2A-L003065](../../tests/test_web_agent.py#L3065) | 3065 | `"            \"كام سعرها؟ اذكر مصادر موثوقة وروابط مباشرة وأجب بإيجاز.\","` | — |
| [SRC-F725E90B2A-L003066](../../tests/test_web_agent.py#L3066) | 3066 | `"            \"أسعار السيارات الكهربائية المستعملة في مصر\","` | — |
| [SRC-F725E90B2A-L003067](../../tests/test_web_agent.py#L3067) | 3067 | `"        ),"` | — |
| [SRC-F725E90B2A-L003068](../../tests/test_web_agent.py#L3068) | 3068 | `"    ],"` | — |
| [SRC-F725E90B2A-L003069](../../tests/test_web_agent.py#L3069) | 3069 | `")"` | — |
| [SRC-F725E90B2A-L003070](../../tests/test_web_agent.py#L3070) | 3070 | `"def test_server_search_sources_use_compact_question_and_topic_plan("` | — |
| [SRC-F725E90B2A-L003071](../../tests/test_web_agent.py#L3071) | 3071 | `"    monkeypatch, question, planned_query"` | — |
| [SRC-F725E90B2A-L003072](../../tests/test_web_agent.py#L3072) | 3072 | `"):"` | — |
| [SRC-F725E90B2A-L003073](../../tests/test_web_agent.py#L3073) | 3073 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003074](../../tests/test_web_agent.py#L3074) | 3074 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L003075](../../tests/test_web_agent.py#L3075) | 3075 | `"    topic_query = planned_query or compact_search_query(question)"` | — |
| [SRC-F725E90B2A-L003076](../../tests/test_web_agent.py#L3076) | 3076 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L003077](../../tests/test_web_agent.py#L3077) | 3077 | `"        \"queries\": [topic_query],"` | — |
| [SRC-F725E90B2A-L003078](../../tests/test_web_agent.py#L3078) | 3078 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L003079](../../tests/test_web_agent.py#L3079) | 3079 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003080](../../tests/test_web_agent.py#L3080) | 3080 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003081](../../tests/test_web_agent.py#L3081) | 3081 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003082](../../tests/test_web_agent.py#L3082) | 3082 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003083](../../tests/test_web_agent.py#L3083) | 3083 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003084](../../tests/test_web_agent.py#L3084) | 3084 | `"    }"` | — |
| [SRC-F725E90B2A-L003085](../../tests/test_web_agent.py#L3085) | 3085 | `"    source_queries = []"` | — |
| [SRC-F725E90B2A-L003086](../../tests/test_web_agent.py#L3086) | 3086 | `""` | — |
| [SRC-F725E90B2A-L003087](../../tests/test_web_agent.py#L3087) | 3087 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda _question, _history: dict(plan))"` | — |
| [SRC-F725E90B2A-L003088](../../tests/test_web_agent.py#L3088) | 3088 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003089](../../tests/test_web_agent.py#L3089) | 3089 | `"        agent, \"_collect_research\","` | — |
| [SRC-F725E90B2A-L003090](../../tests/test_web_agent.py#L3090) | 3090 | `"        lambda research_plan: ([sample_source(0), sample_source(1)], [], {"` | — |
| [SRC-F725E90B2A-L003091](../../tests/test_web_agent.py#L3091) | 3091 | `"            \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L003092](../../tests/test_web_agent.py#L3092) | 3092 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L003093](../../tests/test_web_agent.py#L3093) | 3093 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L003094](../../tests/test_web_agent.py#L3094) | 3094 | `"            \"unique_sources\": 2,"` | — |
| [SRC-F725E90B2A-L003095](../../tests/test_web_agent.py#L3095) | 3095 | `"            \"pages_fetched\": 2,"` | — |
| [SRC-F725E90B2A-L003096](../../tests/test_web_agent.py#L3096) | 3096 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L003097](../../tests/test_web_agent.py#L3097) | 3097 | `"            \"platform_counts\": {\"web\": 2},"` | — |
| [SRC-F725E90B2A-L003098](../../tests/test_web_agent.py#L3098) | 3098 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L003099](../../tests/test_web_agent.py#L3099) | 3099 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003100](../../tests/test_web_agent.py#L3100) | 3100 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003101](../../tests/test_web_agent.py#L3101) | 3101 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L003102](../../tests/test_web_agent.py#L3102) | 3102 | `"        }),"` | — |
| [SRC-F725E90B2A-L003103](../../tests/test_web_agent.py#L3103) | 3103 | `"    )"` | — |
| [SRC-F725E90B2A-L003104](../../tests/test_web_agent.py#L3104) | 3104 | `""` | — |
| [SRC-F725E90B2A-L003105](../../tests/test_web_agent.py#L3105) | 3105 | `"    def generate(*args, **kwargs):"` | — |
| [SRC-F725E90B2A-L003106](../../tests/test_web_agent.py#L3106) | 3106 | `"        agent.server_search_sources = [{"` | — |
| [SRC-F725E90B2A-L003107](../../tests/test_web_agent.py#L3107) | 3107 | `"            \"title\": \"تجارب السيارات الكهربائية المستعملة\","` | — |
| [SRC-F725E90B2A-L003108](../../tests/test_web_agent.py#L3108) | 3108 | `"            \"url\": \"https://example.org/ev-used-cars\","` | — |
| [SRC-F725E90B2A-L003109](../../tests/test_web_agent.py#L3109) | 3109 | `"            \"snippet\": \"تكلفة البطارية والمدى الفعلي للسيارات الكهربائية المستعملة في مصر\","` | — |
| [SRC-F725E90B2A-L003110](../../tests/test_web_agent.py#L3110) | 3110 | `"            \"page_text\": \"تكلفة البطارية والمدى الفعلي للسيارات الكهربائية المستعملة في مصر\","` | — |
| [SRC-F725E90B2A-L003111](../../tests/test_web_agent.py#L3111) | 3111 | `"            \"page_fetched\": False,"` | — |
| [SRC-F725E90B2A-L003112](../../tests/test_web_agent.py#L3112) | 3112 | `"            \"provider\": \"openrouter_web_search\","` | — |
| [SRC-F725E90B2A-L003113](../../tests/test_web_agent.py#L3113) | 3113 | `"            \"providers\": [\"openrouter_web_search\"],"` | — |
| [SRC-F725E90B2A-L003114](../../tests/test_web_agent.py#L3114) | 3114 | `"            \"queries\": [],"` | — |
| [SRC-F725E90B2A-L003115](../../tests/test_web_agent.py#L3115) | 3115 | `"            \"domain\": \"example.org\","` | — |
| [SRC-F725E90B2A-L003116](../../tests/test_web_agent.py#L3116) | 3116 | `"            \"source_class\": \"general\","` | — |
| [SRC-F725E90B2A-L003117](../../tests/test_web_agent.py#L3117) | 3117 | `"            \"platform\": \"web\","` | — |
| [SRC-F725E90B2A-L003118](../../tests/test_web_agent.py#L3118) | 3118 | `"            \"published_at\": \"\","` | — |
| [SRC-F725E90B2A-L003119](../../tests/test_web_agent.py#L3119) | 3119 | `"        }]"` | — |
| [SRC-F725E90B2A-L003120](../../tests/test_web_agent.py#L3120) | 3120 | `"        return \"إجابة مبدئية [المصدر 1].\""` | — |
| [SRC-F725E90B2A-L003121](../../tests/test_web_agent.py#L3121) | 3121 | `""` | — |
| [SRC-F725E90B2A-L003122](../../tests/test_web_agent.py#L3122) | 3122 | `"    monkeypatch.setattr(agent, \"_generate\", generate)"` | — |
| [SRC-F725E90B2A-L003123](../../tests/test_web_agent.py#L3123) | 3123 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda _question, answer, _sources: answer)"` | — |
| [SRC-F725E90B2A-L003124](../../tests/test_web_agent.py#L3124) | 3124 | `""` | — |
| [SRC-F725E90B2A-L003125](../../tests/test_web_agent.py#L3125) | 3125 | `"    def capture_relevance(query, text):"` | — |
| [SRC-F725E90B2A-L003126](../../tests/test_web_agent.py#L3126) | 3126 | `"        if \"تجارب السيارات الكهربائية المستعملة\" in text:"` | — |
| [SRC-F725E90B2A-L003127](../../tests/test_web_agent.py#L3127) | 3127 | `"            source_queries.append(query)"` | — |
| [SRC-F725E90B2A-L003128](../../tests/test_web_agent.py#L3128) | 3128 | `"            if planned_query and query != compact_search_query(topic_query):"` | — |
| [SRC-F725E90B2A-L003129](../../tests/test_web_agent.py#L3129) | 3129 | `"                return 0.0"` | — |
| [SRC-F725E90B2A-L003130](../../tests/test_web_agent.py#L3130) | 3130 | `"        return 0.25"` | — |
| [SRC-F725E90B2A-L003131](../../tests/test_web_agent.py#L3131) | 3131 | `""` | — |
| [SRC-F725E90B2A-L003132](../../tests/test_web_agent.py#L3132) | 3132 | `"    monkeypatch.setattr(\"agents.web_agent._relevance_ratio\", capture_relevance)"` | — |
| [SRC-F725E90B2A-L003133](../../tests/test_web_agent.py#L3133) | 3133 | `""` | — |
| [SRC-F725E90B2A-L003134](../../tests/test_web_agent.py#L3134) | 3134 | `"    agent.answer(question)"` | — |
| [SRC-F725E90B2A-L003135](../../tests/test_web_agent.py#L3135) | 3135 | `""` | — |
| [SRC-F725E90B2A-L003136](../../tests/test_web_agent.py#L3136) | 3136 | `"    expected_queries = list(dict.fromkeys("` | — |
| [SRC-F725E90B2A-L003137](../../tests/test_web_agent.py#L3137) | 3137 | `"        query for query in ("` | — |
| [SRC-F725E90B2A-L003138](../../tests/test_web_agent.py#L3138) | 3138 | `"            compact_search_query(question),"` | — |
| [SRC-F725E90B2A-L003139](../../tests/test_web_agent.py#L3139) | 3139 | `"            compact_search_query(topic_query),"` | — |
| [SRC-F725E90B2A-L003140](../../tests/test_web_agent.py#L3140) | 3140 | `"        ) if query"` | — |
| [SRC-F725E90B2A-L003141](../../tests/test_web_agent.py#L3141) | 3141 | `"    ))"` | — |
| [SRC-F725E90B2A-L003142](../../tests/test_web_agent.py#L3142) | 3142 | `"    assert source_queries == expected_queries"` | — |
| [SRC-F725E90B2A-L003143](../../tests/test_web_agent.py#L3143) | 3143 | `""` | — |
| [SRC-F725E90B2A-L003144](../../tests/test_web_agent.py#L3144) | 3144 | `""` | — |
| [SRC-F725E90B2A-L003145](../../tests/test_web_agent.py#L3145) | 3145 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L003146](../../tests/test_web_agent.py#L3146) | 3146 | `"    (\"mode\", \"planner_query\"),"` | — |
| [SRC-F725E90B2A-L003147](../../tests/test_web_agent.py#L3147) | 3147 | `"    ["` | — |
| [SRC-F725E90B2A-L003148](../../tests/test_web_agent.py#L3148) | 3148 | `"        (\"auto\", \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\"),"` | — |
| [SRC-F725E90B2A-L003149](../../tests/test_web_agent.py#L3149) | 3149 | `"        (\"auto\", \"site:reddit.com\"),"` | — |
| [SRC-F725E90B2A-L003150](../../tests/test_web_agent.py#L3150) | 3150 | `"        (\"latest\", \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\"),"` | — |
| [SRC-F725E90B2A-L003151](../../tests/test_web_agent.py#L3151) | 3151 | `"        (\"deep\", \"site:reddit.com\"),"` | — |
| [SRC-F725E90B2A-L003152](../../tests/test_web_agent.py#L3152) | 3152 | `"        (\"social\", \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\"),"` | — |
| [SRC-F725E90B2A-L003153](../../tests/test_web_agent.py#L3153) | 3153 | `"    ],"` | — |
| [SRC-F725E90B2A-L003154](../../tests/test_web_agent.py#L3154) | 3154 | `")"` | — |
| [SRC-F725E90B2A-L003155](../../tests/test_web_agent.py#L3155) | 3155 | `"def test_modes_do_not_create_generic_queries_without_topic("` | — |
| [SRC-F725E90B2A-L003156](../../tests/test_web_agent.py#L3156) | 3156 | `"    monkeypatch, mode, planner_query"` | — |
| [SRC-F725E90B2A-L003157](../../tests/test_web_agent.py#L3157) | 3157 | `"):"` | — |
| [SRC-F725E90B2A-L003158](../../tests/test_web_agent.py#L3158) | 3158 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003159](../../tests/test_web_agent.py#L3159) | 3159 | `"    instruction_only = \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\""` | — |
| [SRC-F725E90B2A-L003160](../../tests/test_web_agent.py#L3160) | 3160 | `"    direct_url = \"https://example.com/report\""` | — |
| [SRC-F725E90B2A-L003161](../../tests/test_web_agent.py#L3161) | 3161 | `"    observed_plans = []"` | — |
| [SRC-F725E90B2A-L003162](../../tests/test_web_agent.py#L3162) | 3162 | `""` | — |
| [SRC-F725E90B2A-L003163](../../tests/test_web_agent.py#L3163) | 3163 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003164](../../tests/test_web_agent.py#L3164) | 3164 | `"        \"agents.web_agent.route_intent\","` | — |
| [SRC-F725E90B2A-L003165](../../tests/test_web_agent.py#L3165) | 3165 | `"        lambda *args, **kwargs: {\"route\": \"WEB_DEEP\", \"reason\": \"test\"},"` | — |
| [SRC-F725E90B2A-L003166](../../tests/test_web_agent.py#L3166) | 3166 | `"    )"` | — |
| [SRC-F725E90B2A-L003167](../../tests/test_web_agent.py#L3167) | 3167 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003168](../../tests/test_web_agent.py#L3168) | 3168 | `"        agent, \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003169](../../tests/test_web_agent.py#L3169) | 3169 | `"        lambda _question, _history: {"` | — |
| [SRC-F725E90B2A-L003170](../../tests/test_web_agent.py#L3170) | 3170 | `"            \"queries\": [planner_query],"` | — |
| [SRC-F725E90B2A-L003171](../../tests/test_web_agent.py#L3171) | 3171 | `"            \"direct_urls\": [direct_url],"` | — |
| [SRC-F725E90B2A-L003172](../../tests/test_web_agent.py#L3172) | 3172 | `"            \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003173](../../tests/test_web_agent.py#L3173) | 3173 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003174](../../tests/test_web_agent.py#L3174) | 3174 | `"            \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L003175](../../tests/test_web_agent.py#L3175) | 3175 | `"            \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003176](../../tests/test_web_agent.py#L3176) | 3176 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003177](../../tests/test_web_agent.py#L3177) | 3177 | `"        },"` | — |
| [SRC-F725E90B2A-L003178](../../tests/test_web_agent.py#L3178) | 3178 | `"    )"` | — |
| [SRC-F725E90B2A-L003179](../../tests/test_web_agent.py#L3179) | 3179 | `""` | — |
| [SRC-F725E90B2A-L003180](../../tests/test_web_agent.py#L3180) | 3180 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L003181](../../tests/test_web_agent.py#L3181) | 3181 | `"        observed_plans.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L003182](../../tests/test_web_agent.py#L3182) | 3182 | `"        return [], [], {"` | — |
| [SRC-F725E90B2A-L003183](../../tests/test_web_agent.py#L3183) | 3183 | `"            \"queries_planned\": len(research_plan.get(\"queries\", [])),"` | — |
| [SRC-F725E90B2A-L003184](../../tests/test_web_agent.py#L3184) | 3184 | `"            \"queries_attempted\": 0,"` | — |
| [SRC-F725E90B2A-L003185](../../tests/test_web_agent.py#L3185) | 3185 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L003186](../../tests/test_web_agent.py#L3186) | 3186 | `"            \"unique_sources\": 0,"` | — |
| [SRC-F725E90B2A-L003187](../../tests/test_web_agent.py#L3187) | 3187 | `"            \"pages_fetched\": 0,"` | — |
| [SRC-F725E90B2A-L003188](../../tests/test_web_agent.py#L3188) | 3188 | `"            \"providers_used\": [],"` | — |
| [SRC-F725E90B2A-L003189](../../tests/test_web_agent.py#L3189) | 3189 | `"            \"platform_counts\": {},"` | — |
| [SRC-F725E90B2A-L003190](../../tests/test_web_agent.py#L3190) | 3190 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L003191](../../tests/test_web_agent.py#L3191) | 3191 | `"            \"depth\": research_plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-F725E90B2A-L003192](../../tests/test_web_agent.py#L3192) | 3192 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003193](../../tests/test_web_agent.py#L3193) | 3193 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L003194](../../tests/test_web_agent.py#L3194) | 3194 | `"        }"` | — |
| [SRC-F725E90B2A-L003195](../../tests/test_web_agent.py#L3195) | 3195 | `""` | — |
| [SRC-F725E90B2A-L003196](../../tests/test_web_agent.py#L3196) | 3196 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L003197](../../tests/test_web_agent.py#L3197) | 3197 | `""` | — |
| [SRC-F725E90B2A-L003198](../../tests/test_web_agent.py#L3198) | 3198 | `"    agent.answer(instruction_only, mode=mode)"` | — |
| [SRC-F725E90B2A-L003199](../../tests/test_web_agent.py#L3199) | 3199 | `""` | — |
| [SRC-F725E90B2A-L003200](../../tests/test_web_agent.py#L3200) | 3200 | `"    assert observed_plans"` | — |
| [SRC-F725E90B2A-L003201](../../tests/test_web_agent.py#L3201) | 3201 | `"    assert observed_plans[0][\"queries\"] == []"` | — |
| [SRC-F725E90B2A-L003202](../../tests/test_web_agent.py#L3202) | 3202 | `"    assert observed_plans[0][\"direct_urls\"] == [direct_url]"` | — |
| [SRC-F725E90B2A-L003203](../../tests/test_web_agent.py#L3203) | 3203 | `""` | — |
| [SRC-F725E90B2A-L003204](../../tests/test_web_agent.py#L3204) | 3204 | `""` | — |
| [SRC-F725E90B2A-L003205](../../tests/test_web_agent.py#L3205) | 3205 | `"def test_auto_navigation_strips_arabic_search_verb_without_regex_regression(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003206](../../tests/test_web_agent.py#L3206) | 3206 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003207](../../tests/test_web_agent.py#L3207) | 3207 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L003208](../../tests/test_web_agent.py#L3208) | 3208 | `"    question = \"ابحث عن الموقع الرسمي لشركة النور\""` | — |
| [SRC-F725E90B2A-L003209](../../tests/test_web_agent.py#L3209) | 3209 | `"    observed_plans = []"` | — |
| [SRC-F725E90B2A-L003210](../../tests/test_web_agent.py#L3210) | 3210 | `""` | — |
| [SRC-F725E90B2A-L003211](../../tests/test_web_agent.py#L3211) | 3211 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003212](../../tests/test_web_agent.py#L3212) | 3212 | `"        \"agents.web_agent.route_intent\","` | — |
| [SRC-F725E90B2A-L003213](../../tests/test_web_agent.py#L3213) | 3213 | `"        lambda *args, **kwargs: {\"route\": \"WEB_SIMPLE\", \"reason\": \"test\"},"` | — |
| [SRC-F725E90B2A-L003214](../../tests/test_web_agent.py#L3214) | 3214 | `"    )"` | — |
| [SRC-F725E90B2A-L003215](../../tests/test_web_agent.py#L3215) | 3215 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003216](../../tests/test_web_agent.py#L3216) | 3216 | `"        \"agents.web_agent.compact_search_query\","` | — |
| [SRC-F725E90B2A-L003217](../../tests/test_web_agent.py#L3217) | 3217 | `"        lambda value: value.strip() if isinstance(value, str) else \"\","` | — |
| [SRC-F725E90B2A-L003218](../../tests/test_web_agent.py#L3218) | 3218 | `"    )"` | — |
| [SRC-F725E90B2A-L003219](../../tests/test_web_agent.py#L3219) | 3219 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003220](../../tests/test_web_agent.py#L3220) | 3220 | `"        agent, \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003221](../../tests/test_web_agent.py#L3221) | 3221 | `"        lambda _question, _history: {"` | — |
| [SRC-F725E90B2A-L003222](../../tests/test_web_agent.py#L3222) | 3222 | `"            \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L003223](../../tests/test_web_agent.py#L3223) | 3223 | `"            \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L003224](../../tests/test_web_agent.py#L3224) | 3224 | `"            \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003225](../../tests/test_web_agent.py#L3225) | 3225 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003226](../../tests/test_web_agent.py#L3226) | 3226 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003227](../../tests/test_web_agent.py#L3227) | 3227 | `"            \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003228](../../tests/test_web_agent.py#L3228) | 3228 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003229](../../tests/test_web_agent.py#L3229) | 3229 | `"        },"` | — |
| [SRC-F725E90B2A-L003230](../../tests/test_web_agent.py#L3230) | 3230 | `"    )"` | — |
| [SRC-F725E90B2A-L003231](../../tests/test_web_agent.py#L3231) | 3231 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003232](../../tests/test_web_agent.py#L3232) | 3232 | `"        \"agents.web_agent.fallback_plan\","` | — |
| [SRC-F725E90B2A-L003233](../../tests/test_web_agent.py#L3233) | 3233 | `"        lambda *args, **kwargs: {\"queries\": [question]},"` | — |
| [SRC-F725E90B2A-L003234](../../tests/test_web_agent.py#L3234) | 3234 | `"    )"` | — |
| [SRC-F725E90B2A-L003235](../../tests/test_web_agent.py#L3235) | 3235 | `""` | — |
| [SRC-F725E90B2A-L003236](../../tests/test_web_agent.py#L3236) | 3236 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L003237](../../tests/test_web_agent.py#L3237) | 3237 | `"        observed_plans.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L003238](../../tests/test_web_agent.py#L3238) | 3238 | `"        return [], [], {"` | — |
| [SRC-F725E90B2A-L003239](../../tests/test_web_agent.py#L3239) | 3239 | `"            \"queries_planned\": len(research_plan.get(\"queries\", [])),"` | — |
| [SRC-F725E90B2A-L003240](../../tests/test_web_agent.py#L3240) | 3240 | `"            \"queries_attempted\": 0,"` | — |
| [SRC-F725E90B2A-L003241](../../tests/test_web_agent.py#L3241) | 3241 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L003242](../../tests/test_web_agent.py#L3242) | 3242 | `"            \"unique_sources\": 0,"` | — |
| [SRC-F725E90B2A-L003243](../../tests/test_web_agent.py#L3243) | 3243 | `"            \"pages_fetched\": 0,"` | — |
| [SRC-F725E90B2A-L003244](../../tests/test_web_agent.py#L3244) | 3244 | `"            \"providers_used\": [],"` | — |
| [SRC-F725E90B2A-L003245](../../tests/test_web_agent.py#L3245) | 3245 | `"            \"platform_counts\": {},"` | — |
| [SRC-F725E90B2A-L003246](../../tests/test_web_agent.py#L3246) | 3246 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L003247](../../tests/test_web_agent.py#L3247) | 3247 | `"            \"depth\": research_plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-F725E90B2A-L003248](../../tests/test_web_agent.py#L3248) | 3248 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003249](../../tests/test_web_agent.py#L3249) | 3249 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L003250](../../tests/test_web_agent.py#L3250) | 3250 | `"        }"` | — |
| [SRC-F725E90B2A-L003251](../../tests/test_web_agent.py#L3251) | 3251 | `""` | — |
| [SRC-F725E90B2A-L003252](../../tests/test_web_agent.py#L3252) | 3252 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L003253](../../tests/test_web_agent.py#L3253) | 3253 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"لم أعثر على مصدر.\")"` | — |
| [SRC-F725E90B2A-L003254](../../tests/test_web_agent.py#L3254) | 3254 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda _question, answer, _sources: answer)"` | — |
| [SRC-F725E90B2A-L003255](../../tests/test_web_agent.py#L3255) | 3255 | `""` | — |
| [SRC-F725E90B2A-L003256](../../tests/test_web_agent.py#L3256) | 3256 | `"    agent.answer(question, mode=\"auto\")"` | — |
| [SRC-F725E90B2A-L003257](../../tests/test_web_agent.py#L3257) | 3257 | `""` | — |
| [SRC-F725E90B2A-L003258](../../tests/test_web_agent.py#L3258) | 3258 | `"    assert observed_plans"` | — |
| [SRC-F725E90B2A-L003259](../../tests/test_web_agent.py#L3259) | 3259 | `"    assert observed_plans[0][\"queries\"]"` | — |
| [SRC-F725E90B2A-L003260](../../tests/test_web_agent.py#L3260) | 3260 | `"    assert all(not query.startswith(\"ابحث عن\") for query in observed_plans[0][\"queries\"])"` | — |
| [SRC-F725E90B2A-L003261](../../tests/test_web_agent.py#L3261) | 3261 | `"    assert \"الموقع الرسمي لشركة النور\" in observed_plans[0][\"queries\"][0]"` | — |
## واجهة الويب

### FILE-DE7EABE998 — [web/agent.html](../../web/agent.html#L1)

- النوع: **HTML**
- نطاق الفهرسة: جرد الملف + معرفات HTML والرموز داخل script/style

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-DE7EABE998-L000001](../../web/agent.html#L1) | 1 | `"<!doctype html>"` | — |
| [SRC-DE7EABE998-L000002](../../web/agent.html#L2) | 2 | `"<html lang=\"ar\" dir=\"rtl\">"` | — |
| [SRC-DE7EABE998-L000003](../../web/agent.html#L3) | 3 | `"<head>"` | — |
| [SRC-DE7EABE998-L000004](../../web/agent.html#L4) | 4 | `"<meta charset=\"utf-8\">"` | — |
| [SRC-DE7EABE998-L000005](../../web/agent.html#L5) | 5 | `"<meta name=\"viewport\" content=\"width=device-width,initial-scale=1,viewport-fit=cover\">"` | — |
| [SRC-DE7EABE998-L000006](../../web/agent.html#L6) | 6 | `"<meta name=\"theme-color\" content=\"#0a1220\">"` | — |
| [SRC-DE7EABE998-L000007](../../web/agent.html#L7) | 7 | `"<title>Omarai \| وكيل البحث والتحليل</title>"` | — |
| [SRC-DE7EABE998-L000008](../../web/agent.html#L8) | 8 | `"<style>"` | — |
| [SRC-DE7EABE998-L000009](../../web/agent.html#L9) | 9 | `":root{color-scheme:dark;--bg:#0a1220;--panel:#101b2c;--panel2:#132238;--line:#263b55;--text:#f0f5fc;--muted:#9cabc0;--teal:#65e5d0;--blue:#9bbcff;--green:#84e0a9;--amber:#ffd28a;--red:#ff929e;--radius:20px}"` | — |
| [SRC-DE7EABE998-L000010](../../web/agent.html#L10) | 10 | `"*{box-sizing:border-box}"` | — |
| [SRC-DE7EABE998-L000011](../../web/agent.html#L11) | 11 | `"body{margin:0;background:radial-gradient(ellipse at 92% -10%,#173755 0,transparent 38%),radial-gradient(ellipse at 5% 40%,#10273a 0,transparent 32%),var(--bg);color:var(--text);font-family:system-ui,-apple-system,\"Segoe UI\",sans-serif;min-height:100vh}"` | — |
| [SRC-DE7EABE998-L000012](../../web/agent.html#L12) | 12 | `"button,input,textarea{font:inherit}button{cursor:pointer}button:focus-visible,textarea:focus-visible{outline:2px solid var(--teal);outline-offset:2px}"` | — |
| [SRC-DE7EABE998-L000013](../../web/agent.html#L13) | 13 | `".shell{max-width:1240px;margin:auto;padding:18px;min-height:100vh;display:flex;flex-direction:column}"` | — |
| [SRC-DE7EABE998-L000014](../../web/agent.html#L14) | 14 | `".topbar{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:7px 2px 18px;border-bottom:1px solid #26384b}"` | — |
| [SRC-DE7EABE998-L000015](../../web/agent.html#L15) | 15 | `".brand{display:flex;align-items:center;gap:11px;min-width:0}.logo{height:45px;width:45px;border-radius:15px;display:grid;place-items:center;color:#07131e;background:linear-gradient(135deg,#73f0d8,#9bbcff);font-weight:950;font-size:25px;box-shadow:0 8px 30px #67e8df22}"` | — |
| [SRC-DE7EABE998-L000016](../../web/agent.html#L16) | 16 | `".brand h1{font-size:21px;letter-spacing:.2px;margin:0}.brand p{margin:3px 0 0;color:var(--muted);font-size:11px}"` | — |
| [SRC-DE7EABE998-L000017](../../web/agent.html#L17) | 17 | `".top-actions{display:flex;align-items:center;gap:8px}.status{display:flex;gap:8px;align-items:center;padding:8px 11px;border:1px solid var(--line);border-radius:99px;color:var(--muted);font-size:11px}.dot{width:7px;height:7px;border-radius:50%;background:#8394aa;flex:none}.dot.ok{background:var(--green);box-shadow:0 0 11px #84e0a966}.dot.warn{background:var(--amber)}.dot.bad{background:var(--red)}"` | — |
| [SRC-DE7EABE998-L000018](../../web/agent.html#L18) | 18 | `".ghost,.primary{border:1px solid var(--line);border-radius:12px;padding:10px 13px;font-weight:750;font-size:12px}.ghost{color:#d9e6f8;background:#121f32}.ghost:hover{border-color:#50718e}.primary{color:#07131e;border:0;background:linear-gradient(110deg,var(--teal),#acc4ff)}.primary:disabled{opacity:.5;cursor:wait}"` | — |
| [SRC-DE7EABE998-L000019](../../web/agent.html#L19) | 19 | `".hero{display:flex;align-items:flex-end;justify-content:space-between;gap:20px;padding:24px 3px 18px}.eyebrow{color:var(--teal);font-size:11px;font-weight:850;letter-spacing:.55px}.hero h2{font-size:clamp(26px,4vw,37px);line-height:1.35;margin:7px 0 9px;letter-spacing:-.6px}.hero h2 span{color:var(--teal)}.hero p{font-size:13px;line-height:1.9;color:var(--muted);margin:0;max-width:760px}.trust{width:230px;flex:none;border:1px solid #28524f;background:#0c2629;border-radius:16px;padding:13px 15px;color:#b5f7e8;font-size:11px;line-height:1.8}.trust b{display:block;color:#e4fffa;font-size:12px;margin-bottom:3px}"` | — |
| [SRC-DE7EABE998-L000020](../../web/agent.html#L20) | 20 | `".layout{display:grid;grid-template-columns:minmax(0,1fr) 286px;gap:15px;align-items:start;flex:1}"` | — |
| [SRC-DE7EABE998-L000021](../../web/agent.html#L21) | 21 | `".chatpanel,.sidepanel{border:1px solid var(--line);background:linear-gradient(150deg,#111e30f5,#0d1727f5);border-radius:var(--radius);overflow:hidden;box-shadow:0 24px 70px #0002}"` | — |
| [SRC-DE7EABE998-L000022](../../web/agent.html#L22) | 22 | `".chatpanel{display:flex;flex-direction:column;min-height:600px}.chathead{padding:15px 17px;border-bottom:1px solid #24384f;display:flex;align-items:center;justify-content:space-between;gap:12px}.chathead h3{font-size:14px;margin:0}.chathead p{font-size:11px;color:var(--muted);margin:4px 0 0}.live-tag{display:flex;align-items:center;gap:7px;color:#b9fff2;background:#102a2e;border:1px solid #245358;padding:7px 10px;border-radius:99px;font-size:10px;white-space:nowrap}"` | — |
| [SRC-DE7EABE998-L000023](../../web/agent.html#L23) | 23 | `".modebar{display:flex;align-items:center;gap:7px;flex-wrap:wrap;padding:12px 15px;border-bottom:1px solid #24384f;background:#0d1827}.mode-label{color:var(--muted);font-size:11px;margin-left:3px}.mode-btn{color:#c3d3e8;border:1px solid #2b4059;background:#101f32;border-radius:99px;padding:8px 11px;font-size:11px;font-weight:700;transition:.16s}.mode-btn:hover{border-color:#5b86a5}.mode-btn.active{color:#07131e;border-color:transparent;background:linear-gradient(110deg,var(--teal),#a8c1ff)}"` | — |
| [SRC-DE7EABE998-L000024](../../web/agent.html#L24) | 24 | `".messages{padding:18px;display:flex;flex-direction:column;gap:18px;min-height:360px;max-height:calc(100vh - 360px);overflow:auto;scroll-behavior:smooth}.welcome{margin:auto 0;text-align:center;padding:25px 10px}.welcome-icon{width:58px;height:58px;border-radius:19px;display:grid;place-items:center;margin:0 auto 14px;background:#142c3c;border:1px solid #2c5561;color:var(--teal);font-size:26px}.welcome h3{font-size:19px;margin:0 0 8px}.welcome p{font-size:12px;color:var(--muted);line-height:1.9;max-width:470px;margin:0 auto 19px}.suggestions{display:flex;flex-wrap:wrap;justify-content:center;gap:8px}.suggestions button{font-size:11px;line-height:1.65;color:#c4d6ec;border:1px solid #2b4059;background:#101f32;padding:10px 12px;border-radius:12px}.suggestions button:hover{color:white;border-color:var(--teal)}"` | — |
| [SRC-DE7EABE998-L000025](../../web/agent.html#L25) | 25 | `".message{display:flex;flex-direction:column;gap:8px;align-self:stretch;max-width:100%;min-width:0}.message.user{align-self:flex-end;max-width:88%;width:max-content}.who{font-size:10px;color:var(--muted);padding:0 3px;display:flex;align-items:center;gap:7px}.bubble{color:#e6eef9;background:#111f32;border:1px solid #2a405a;border-radius:15px 15px 15px 4px;padding:14px 16px;line-height:1.95;font-size:13px;overflow-wrap:anywhere}.user .bubble{background:#123039;border-color:#2b5759;border-radius:15px 15px 4px 15px;white-space:pre-wrap}.bubble h3{font-size:14px;color:#e8fffb;margin:15px 0 5px}.bubble h4{font-size:13px;color:#dce8fc;margin:12px 0 4px}.bubble strong{color:#f6fbff}.bubble ul{margin:6px 0;padding-inline-start:20px}.bubble li{margin:4px 0}.bubble a{color:#b4d4ff}"` | — |
| [SRC-DE7EABE998-L000026](../../web/agent.html#L26) | 26 | `".pending{display:flex;align-items:center;gap:10px;color:#b5c7dc}.spinner{width:17px;height:17px;border:2px solid #2c485a;border-top-color:var(--teal);border-radius:50%;animation:spin .85s linear infinite;flex:none}@keyframes spin{to{transform:rotate(360deg)}}"` | — |
| [SRC-DE7EABE998-L000027](../../web/agent.html#L27) | 27 | `".report{border:1px solid #30465f;background:#0b1726;border-radius:15px;padding:13px;margin-top:3px}.report-head{display:flex;justify-content:space-between;align-items:center;gap:10px;margin-bottom:10px}.report-head b{font-size:12px}.coverage{border:1px solid #315950;background:#102926;border-radius:99px;padding:5px 9px;color:#b9ffeb;font-size:10px;font-weight:800;white-space:nowrap}"` | — |
| [SRC-DE7EABE998-L000028](../../web/agent.html#L28) | 28 | `".metrics{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px}.metric{background:#111f31;border:1px solid #273c55;padding:10px;border-radius:12px;min-width:0}.metric strong{display:block;font-size:20px;line-height:1.35;color:var(--teal);font-weight:850}.metric span{display:block;font-size:10px;color:var(--muted);margin-top:3px;line-height:1.5}.report-note{font-size:11px;color:#b7c8dc;line-height:1.8;margin:10px 0 0}.providers{display:flex;gap:6px;flex-wrap:wrap;margin-top:10px}.provider{border:1px solid #2d425b;background:#102035;color:#c3d5ea;border-radius:99px;padding:5px 8px;font-size:9px}"` | — |
| [SRC-DE7EABE998-L000029](../../web/agent.html#L29) | 29 | `".details{margin-top:9px;border:1px solid #2b4059;background:#0d1929;border-radius:12px;padding:10px 12px;font-size:11px;color:#c6d5e7;line-height:1.8}.details summary{cursor:pointer;color:#b9f8eb;font-weight:700}.details ol{margin:8px 0 0;padding-inline-start:22px}.details li{overflow-wrap:anywhere;margin:4px 0}"` | — |
| [SRC-DE7EABE998-L000030](../../web/agent.html#L30) | 30 | `".warning{border:1px solid #6c5831;background:#292216;color:#ffdfa2;padding:11px 13px;border-radius:12px;font-size:11px;line-height:1.85}.sources{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:9px;margin-top:4px}.source{border:1px solid #293e56;background:#0b1726;border-radius:13px;padding:12px;min-width:0;display:flex;flex-direction:column;gap:6px}.source a{color:#c2d9ff;text-decoration:none;font-weight:800;font-size:11px;line-height:1.75;overflow-wrap:anywhere}.source a:hover{text-decoration:underline;color:white}.source p{color:#acbdd1;font-size:11px;line-height:1.8;margin:0;overflow-wrap:anywhere}.source-meta{display:flex;gap:5px;flex-wrap:wrap;margin-top:auto;padding-top:4px}.tag{border:1px solid #31435a;background:#132237;border-radius:99px;padding:4px 7px;color:#aabbd0;font-size:9px}.tag.read{border-color:#28574b;background:#102821;color:#9deac6}.tag.social{border-color:#594c37;color:#f0cc8f}.no-sources{font-size:11px;color:var(--muted);margin-top:6px}"` | — |
| [SRC-DE7EABE998-L000031](../../web/agent.html#L31) | 31 | `".composer{padding:14px;border-top:1px solid #24384f;background:#0b1523}.inputwrap{display:flex;align-items:flex-end;gap:9px;padding:8px;border:1px solid #314861;border-radius:16px;background:#07111e}.inputwrap:focus-within{border-color:var(--teal);box-shadow:0 0 0 3px #65e5d00e}.inputwrap textarea{flex:1;min-width:0;max-height:150px;min-height:48px;resize:vertical;color:var(--text);background:transparent;border:0;outline:0;padding:10px;font-size:13px;line-height:1.8}.inputwrap textarea::placeholder{color:#7186a0}.send{min-height:44px;min-width:82px}.hint{color:#7589a2;font-size:10px;line-height:1.8;margin:8px 5px 1px}"` | — |
| [SRC-DE7EABE998-L000032](../../web/agent.html#L32) | 32 | `".sidepanel{padding:16px}.sidepanel h3{font-size:13px;margin:0 0 12px}.sideblock{padding:13px 0;border-bottom:1px solid #24374d}.sideblock:first-child{padding-top:0}.sideblock:last-child{border-bottom:0;padding-bottom:0}.sideblock p{font-size:11px;color:var(--muted);line-height:1.9;margin:0}.sidefeature{display:flex;gap:9px;align-items:flex-start;margin:12px 0}.sideicon{flex:none;width:29px;height:29px;display:grid;place-items:center;background:#142b3c;border:1px solid #2a475d;border-radius:9px;color:var(--teal);font-size:13px}.sidefeature b{display:block;font-size:11px;margin:0 0 3px}.sidefeature span{display:block;color:var(--muted);font-size:10px;line-height:1.7}"` | — |
| [SRC-DE7EABE998-L000033](../../web/agent.html#L33) | 33 | `".checkbutton{width:100%;margin-top:10px}.diag{font-size:10px;line-height:1.8;color:#b7c9de;white-space:pre-wrap;overflow-wrap:anywhere;margin:10px 0 0}.config-label{display:inline-block;color:var(--teal);border:1px solid #27534f;background:#0e2827;border-radius:99px;padding:4px 8px;font-size:9px;margin-top:6px}.foot{text-align:center;font-size:10px;color:#71859c;line-height:1.8;padding:16px 4px}"` | — |
| [SRC-DE7EABE998-L000034](../../web/agent.html#L34) | 34 | `"@media(max-width:950px){.layout{grid-template-columns:minmax(0,1fr) 245px}.trust{width:200px}.metrics{grid-template-columns:repeat(2,minmax(0,1fr))}}"` | — |
| [SRC-DE7EABE998-L000035](../../web/agent.html#L35) | 35 | `"@media(max-width:740px){.shell{padding:10px}.layout{grid-template-columns:1fr}.sidepanel{order:2}.hero{align-items:stretch;flex-direction:column;padding:19px 3px 14px}.trust{width:auto}.hero h2{font-size:28px}.topbar{padding-bottom:13px}.brand h1{font-size:19px}.status{display:none}.chatpanel{min-height:70vh}.messages{max-height:unset;min-height:350px;padding:12px}.sidepanel{padding:14px}.sources{grid-template-columns:1fr}.message.user{max-width:94%}.chathead{padding:13px}.modebar{padding:10px;gap:6px}.mode-btn{padding:8px 10px}.composer{padding:10px}.inputwrap{gap:5px}.send{min-width:65px;padding:9px}.bubble{padding:12px;font-size:12px}}"` | — |
| [SRC-DE7EABE998-L000036](../../web/agent.html#L36) | 36 | `"@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation-duration:.01ms!important;scroll-behavior:auto!important;transition:none!important}}"` | — |
| [SRC-DE7EABE998-L000037](../../web/agent.html#L37) | 37 | `".message-context{margin:0 0 9px;padding:8px 10px;border-inline-start:3px solid var(--teal);border-radius:8px;background:rgba(40,190,170,.07);color:var(--muted);font-size:11px;line-height:1.7;overflow-wrap:anywhere}.retry-row{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}.retry-button{border:1px solid #496780;border-radius:10px;background:#152c40;color:var(--text);font:inherit;font-size:12px;font-weight:700;padding:9px 12px;cursor:pointer}.retry-button:focus-visible{outline:2px solid var(--teal);outline-offset:2px}.retry-button:hover{border-color:var(--teal)}"` | — |
| [SRC-DE7EABE998-L000038](../../web/agent.html#L38) | 38 | `"</style>"` | — |
| [SRC-DE7EABE998-L000039](../../web/agent.html#L39) | 39 | `"</head>"` | — |
| [SRC-DE7EABE998-L000040](../../web/agent.html#L40) | 40 | `"<body>"` | — |
| [SRC-DE7EABE998-L000041](../../web/agent.html#L41) | 41 | `"<div class=\"shell\">"` | — |
| [SRC-DE7EABE998-L000042](../../web/agent.html#L42) | 42 | `"<header class=\"topbar\">"` | — |
| [SRC-DE7EABE998-L000043](../../web/agent.html#L43) | 43 | `"  <div class=\"brand\"><div class=\"logo\" aria-hidden=\"true\">O</div><div><h1>Omarai</h1><p>وكيل البحث الحي والتحليل متعدد المصادر</p></div></div>"` | — |
| [SRC-DE7EABE998-L000044](../../web/agent.html#L44) | 44 | `"  <div class=\"top-actions\"><div class=\"status\" id=\"status\" role=\"status\"><span class=\"dot\"></span><span>يفحص الإعداد...</span></div><button class=\"ghost\" id=\"clear\" type=\"button\">بحث جديد ↻</button></div>"` | — |
| [SRC-DE7EABE998-L000045](../../web/agent.html#L45) | 45 | `"</header>"` | — |
| [SRC-DE7EABE998-L000046](../../web/agent.html#L46) | 46 | `""` | — |
| [SRC-DE7EABE998-L000047](../../web/agent.html#L47) | 47 | `"<section class=\"hero\">"` | — |
| [SRC-DE7EABE998-L000048](../../web/agent.html#L48) | 48 | `"  <div><span class=\"eyebrow\">بحث حي · مصادر قابلة للمراجعة · تحليل واضح</span><h2>من السؤال إلى <span>صورة أوضح مدعومة بالأدلة</span></h2><p>اكتب سؤالك بطريقتك الطبيعية. يبحث Omarai عبر محركات ويب ومصادر عامة متاحة، يقرأ الصفحات التي تسمح بالوصول، ويقارن تنوع المصادر وحداثتها ونوعها قبل صياغة إجابة بروابط واضحة. لا يعتبر عدد النتائج وحده إثباتًا للحقيقة.</p></div>"` | — |
| [SRC-DE7EABE998-L000049](../../web/agent.html#L49) | 49 | `"  <div class=\"trust\"><b>◈ شفافية الأدلة أولًا</b>سترى عدد المصادر والنطاقات والصفحات المقروءة ومحركات البحث المستخدمة، مع التنبيه إلى الفجوات. مؤشرات التغطية تصف البحث ولا تمثل احتمال صحة المعلومة.</div>"` | — |
| [SRC-DE7EABE998-L000050](../../web/agent.html#L50) | 50 | `"</section>"` | — |
| [SRC-DE7EABE998-L000051](../../web/agent.html#L51) | 51 | `""` | — |
| [SRC-DE7EABE998-L000052](../../web/agent.html#L52) | 52 | `"<main class=\"layout\">"` | — |
| [SRC-DE7EABE998-L000053](../../web/agent.html#L53) | 53 | `"  <section class=\"chatpanel\" aria-label=\"واجهة البحث\">"` | — |
| [SRC-DE7EABE998-L000054](../../web/agent.html#L54) | 54 | `"    <div class=\"chathead\"><div><h3>مساحة البحث والتحليل</h3><p>تُرسل أسئلة البحث إلى محركات الإنترنت، وقد تُرسل مقتطفات المصادر إلى مزود نموذج اللغة المضبوط.</p></div><span class=\"live-tag\"><span class=\"dot\"></span> بحث ويب</span></div>"` | — |
| [SRC-DE7EABE998-L000055](../../web/agent.html#L55) | 55 | `"    <div class=\"modebar\" role=\"group\" aria-label=\"نمط البحث\">"` | — |
| [SRC-DE7EABE998-L000056](../../web/agent.html#L56) | 56 | `"      <span class=\"mode-label\">عمق البحث:</span>"` | — |
| [SRC-DE7EABE998-L000057](../../web/agent.html#L57) | 57 | `"      <button class=\"mode-btn\" data-mode=\"auto\" type=\"button\">تلقائي</button>"` | — |
| [SRC-DE7EABE998-L000058](../../web/agent.html#L58) | 58 | `"      <button class=\"mode-btn active\" data-mode=\"deep\" type=\"button\" aria-pressed=\"true\">بحث معمّق</button>"` | — |
| [SRC-DE7EABE998-L000059](../../web/agent.html#L59) | 59 | `"      <button class=\"mode-btn\" data-mode=\"latest\" type=\"button\">الأحدث الآن</button>"` | — |
| [SRC-DE7EABE998-L000060](../../web/agent.html#L60) | 60 | `"      <button class=\"mode-btn\" data-mode=\"social\" type=\"button\">آراء الناس</button>"` | — |
| [SRC-DE7EABE998-L000061](../../web/agent.html#L61) | 61 | `"    </div>"` | — |
| [SRC-DE7EABE998-L000062](../../web/agent.html#L62) | 62 | `"    <div class=\"messages\" id=\"messages\" aria-live=\"polite\">"` | — |
| [SRC-DE7EABE998-L000063](../../web/agent.html#L63) | 63 | `"      <div class=\"welcome\" id=\"welcome\"><div class=\"welcome-icon\">⌕</div><h3>ما الذي تريد أن تبحث عنه؟</h3><p>ابدأ بسؤال أو مهمة بحث. اختر بحثًا معمقًا لتوسيع زوايا البحث، أو «الأحدث الآن» للمعلومات الزمنية، أو «آراء الناس» للمحتوى الاجتماعي العام المتاح.</p><div class=\"suggestions\"><button type=\"button\">حلّل أحدث تطورات وكلاء الذكاء الاصطناعي مع المصادر</button><button type=\"button\">قارن سوق العقارات في التجمع والعاصمة الإدارية بالأدلة</button><button type=\"button\">اجمع آراء وتجارب عامة حول منتج أو خدمة</button></div></div>"` | — |
| [SRC-DE7EABE998-L000064](../../web/agent.html#L64) | 64 | `"    </div>"` | — |
| [SRC-DE7EABE998-L000065](../../web/agent.html#L65) | 65 | `"    <div class=\"composer\"><div class=\"inputwrap\"><textarea id=\"question\" rows=\"2\" maxlength=\"4000\" placeholder=\"اسأل باللهجة المصرية أو العربية الفصحى أو الإنجليزية…\"></textarea><button class=\"primary send\" id=\"send\" type=\"button\">ابحث ←</button></div><div class=\"hint\">Enter للإرسال · Shift + Enter لسطر جديد · لا تضع كلمات مرور أو مفاتيح API أو بيانات شخصية سرية داخل السؤال.</div></div>"` | — |
| [SRC-DE7EABE998-L000066](../../web/agent.html#L66) | 66 | `"  </section>"` | — |
| [SRC-DE7EABE998-L000067](../../web/agent.html#L67) | 67 | `""` | — |
| [SRC-DE7EABE998-L000068](../../web/agent.html#L68) | 68 | `"  <aside class=\"sidepanel\">"` | — |
| [SRC-DE7EABE998-L000069](../../web/agent.html#L69) | 69 | `"    <div class=\"sideblock\">"` | — |
| [SRC-DE7EABE998-L000070](../../web/agent.html#L70) | 70 | `"      <h3>الوصول الآمن إلى النسخة المستضافة</h3>"` | — |
| [SRC-DE7EABE998-L000071](../../web/agent.html#L71) | 71 | `"      <label for=\"accessToken\" style=\"display:block;font-size:11px;color:#b9c9dc;margin:9px 0\">رمز الوصول الخاص بالتطبيق</label>"` | — |
| [SRC-DE7EABE998-L000072](../../web/agent.html#L72) | 72 | `"      <input id=\"accessToken\" type=\"password\" autocomplete=\"off\" spellcheck=\"false\" placeholder=\"أدخل رمز الاستضافة الذي أنشأته\" style=\"width:100%;padding:11px;border:1px solid #314861;border-radius:11px;background:#07111e;color:var(--text);font-size:12px\">"` | — |
| [SRC-DE7EABE998-L000073](../../web/agent.html#L73) | 73 | `"      <button id=\"saveAccessToken\" type=\"button\" class=\"ghost checkbutton\">حفظ الرمز على هذا الجهاز</button>"` | — |
| [SRC-DE7EABE998-L000074](../../web/agent.html#L74) | 74 | `"      <p style=\"font-size:10px;color:var(--muted);line-height:1.8;margin-top:7px\">لا تضع مفتاح OpenRouter هنا. هذا رمز منفصل لحماية تطبيقك المستضاف، ويُحفظ محليًا في متصفحك فقط.</p>"` | — |
| [SRC-DE7EABE998-L000075](../../web/agent.html#L75) | 75 | `"    </div>"` | — |
| [SRC-DE7EABE998-L000076](../../web/agent.html#L76) | 76 | `"    <div class=\"sideblock\">"` | — |
| [SRC-DE7EABE998-L000077](../../web/agent.html#L77) | 77 | `"      <h3>حالة الاتصال الفعلية</h3>"` | — |
| [SRC-DE7EABE998-L000078](../../web/agent.html#L78) | 78 | `"      <p id=\"setupStatus\">جارٍ فحص إعدادات الخادم. إعداد المحرك لا يعني أن البحث الحي نجح بعد؛ استخدم الاختبار أدناه للتحقق من الاتصال الفعلي.</p>"` | — |
| [SRC-DE7EABE998-L000079](../../web/agent.html#L79) | 79 | `"      <label style=\"display:flex;gap:8px;align-items:flex-start;margin:11px 0;font-size:10px;color:#b9c9dc;line-height:1.7\"><input id=\"diagSocial\" type=\"checkbox\" style=\"margin-top:3px\"> اختبار المصادر الاجتماعية العامة والموصلات المهيأة أيضًا</label>"` | — |
| [SRC-DE7EABE998-L000080](../../web/agent.html#L80) | 80 | `"      <button id=\"runDiagnostics\" type=\"button\" class=\"primary checkbutton\">اختبار حي للإنترنت والنموذج</button>"` | — |
| [SRC-DE7EABE998-L000081](../../web/agent.html#L81) | 81 | `"      <p id=\"diagnosticsResult\" class=\"diag\" aria-live=\"polite\"></p>"` | — |
| [SRC-DE7EABE998-L000082](../../web/agent.html#L82) | 82 | `"    </div>"` | — |
| [SRC-DE7EABE998-L000083](../../web/agent.html#L83) | 83 | `"    <div class=\"sideblock\">"` | — |
| [SRC-DE7EABE998-L000084](../../web/agent.html#L84) | 84 | `"      <h3>مصادر البحث</h3>"` | — |
| [SRC-DE7EABE998-L000085](../../web/agent.html#L85) | 85 | `"      <div class=\"sidefeature\"><div class=\"sideicon\">⌕</div><div><b>محركات الويب</b><span>DuckDuckGo وBing؛ ويمكن إضافة Brave وTavily بمفتاح API اختياري.</span></div></div>"` | — |
| [SRC-DE7EABE998-L000086](../../web/agent.html#L86) | 86 | `"      <div class=\"sidefeature\"><div class=\"sideicon\">▤</div><div><b>الأخبار والمصادر العامة</b><span>Google News عند طلب معلومات حديثة، وقراءة الصفحات التي تسمح بالوصول العام.</span></div></div>"` | — |
| [SRC-DE7EABE998-L000087](../../web/agent.html#L87) | 87 | `"      <div class=\"sidefeature\"><div class=\"sideicon\">◎</div><div><b>الشبكات الاجتماعية</b><span>مصادر عامة موصولة فعليًا أو نتائج مفهرسة؛ ليست تغطية كاملة لكل المنصات أو المنشورات.</span></div></div>"` | — |
| [SRC-DE7EABE998-L000088](../../web/agent.html#L88) | 88 | `"      <div id=\"providerSetup\"></div>"` | — |
| [SRC-DE7EABE998-L000089](../../web/agent.html#L89) | 89 | `"    </div>"` | — |
| [SRC-DE7EABE998-L000090](../../web/agent.html#L90) | 90 | `"    <div class=\"sideblock\">"` | — |
| [SRC-DE7EABE998-L000091](../../web/agent.html#L91) | 91 | `"      <h3>كيف تقرأ النتيجة؟</h3>"` | — |
| [SRC-DE7EABE998-L000092](../../web/agent.html#L92) | 92 | `"      <p>تنوع النطاقات ومحركات البحث والصفحات المقروءة وتواريخ النشر إشارات إلى مدى تغطية البحث، لا دليلًا قاطعًا على صحة الادعاء. افتح المصادر المهمة، وانتبه إلى التضارب والمعلومات غير المؤرخة.</p>"` | — |
| [SRC-DE7EABE998-L000093](../../web/agent.html#L93) | 93 | `"    </div>"` | — |
| [SRC-DE7EABE998-L000094](../../web/agent.html#L94) | 94 | `"  </aside>"` | — |
| [SRC-DE7EABE998-L000095](../../web/agent.html#L95) | 95 | `"</main>"` | — |
| [SRC-DE7EABE998-L000096](../../web/agent.html#L96) | 96 | `"<footer class=\"foot\">Omarai · لا يتجاوز تسجيل الدخول أو الصفحات الخاصة أو الحواجز المدفوعة، ولا يرسل رسائل تلقائية. الإتاحة الفعلية تعتمد على اتصال الإنترنت، وحدود محركات البحث، ومفاتيح الخدمات الاختيارية.</footer>"` | — |
| [SRC-DE7EABE998-L000097](../../web/agent.html#L97) | 97 | `"</div>"` | — |
| [SRC-DE7EABE998-L000098](../../web/agent.html#L98) | 98 | `""` | — |
| [SRC-DE7EABE998-L000099](../../web/agent.html#L99) | 99 | `"<script>"` | — |
| [SRC-DE7EABE998-L000100](../../web/agent.html#L100) | 100 | `"const $=id=>document.getElementById(id);"` | — |
| [SRC-DE7EABE998-L000101](../../web/agent.html#L101) | 101 | `"const ACCESS_TOKEN_STORAGE_KEY=\"omarai_access_token\";"` | — |
| [SRC-DE7EABE998-L000102](../../web/agent.html#L102) | 102 | `"function apiHeaders(){const headers={\"Content-Type\":\"application/json\"};const token=($(\"accessToken\")?.value\|\|localStorage.getItem(ACCESS_TOKEN_STORAGE_KEY)\|\|\"\").trim();if(token)headers.Authorization=\"Bearer \"+token;return headers;}"` | — |
| [SRC-DE7EABE998-L000103](../../web/agent.html#L103) | 103 | `"const history=[];"` | — |
| [SRC-DE7EABE998-L000104](../../web/agent.html#L104) | 104 | `"let busy=false;"` | — |
| [SRC-DE7EABE998-L000105](../../web/agent.html#L105) | 105 | `"let activeMode=\"deep\";"` | — |
| [SRC-DE7EABE998-L000106](../../web/agent.html#L106) | 106 | `"const modeLabels={auto:\"تلقائي\",deep:\"بحث معمّق\",latest:\"الأحدث الآن\",social:\"آراء الناس\"};"` | — |
| [SRC-DE7EABE998-L000107](../../web/agent.html#L107) | 107 | `"function escapeHtml(s){return String(s??\"\").replace(/[&<>\"']/g,c=>({\"&\":\"&amp;\",\"<\":\"&lt;\",\">\":\"&gt;\",'\"':\"&quot;\",\"'\":\"&#39;\"}[c]));}"` | — |
| [SRC-DE7EABE998-L000108](../../web/agent.html#L108) | 108 | `"function answerMarkup(text){"` | — |
| [SRC-DE7EABE998-L000109](../../web/agent.html#L109) | 109 | `"  const escaped=escapeHtml(text);"` | — |
| [SRC-DE7EABE998-L000110](../../web/agent.html#L110) | 110 | `"  return escaped"` | — |
| [SRC-DE7EABE998-L000111](../../web/agent.html#L111) | 111 | `"   .replace(/^###\\s+(.+)$/gm,\"<h3>$1</h3>\")"` | — |
| [SRC-DE7EABE998-L000112](../../web/agent.html#L112) | 112 | `"   .replace(/^##\\s+(.+)$/gm,\"<h3>$1</h3>\")"` | — |
| [SRC-DE7EABE998-L000113](../../web/agent.html#L113) | 113 | `"   .replace(/^#\\s+(.+)$/gm,\"<h3>$1</h3>\")"` | — |
| [SRC-DE7EABE998-L000114](../../web/agent.html#L114) | 114 | `"   .replace(/^\\s*[-*]\\s+(.+)$/gm,\"• $1\")"` | — |
| [SRC-DE7EABE998-L000115](../../web/agent.html#L115) | 115 | `"   .replace(/\\*\\*(.+?)\\*\\*/g,\"<strong>$1</strong>\")"` | — |
| [SRC-DE7EABE998-L000116](../../web/agent.html#L116) | 116 | ``"   .replace(/`([^`]+)`/g,\"<code>$1</code>\")"`` | — |
| [SRC-DE7EABE998-L000117](../../web/agent.html#L117) | 117 | `"   .replace(/\\n/g,\"<br>\");"` | — |
| [SRC-DE7EABE998-L000118](../../web/agent.html#L118) | 118 | `"}"` | — |
| [SRC-DE7EABE998-L000119](../../web/agent.html#L119) | 119 | `"function setStatus(text,kind){$(\"status\").innerHTML='<span class=\"dot '+(kind\|\|\"\")+'\"></span><span>'+escapeHtml(text)+'</span>';}"` | — |
| [SRC-DE7EABE998-L000120](../../web/agent.html#L120) | 120 | `"function modeName(mode){return modeLabels[mode]\|\|modeLabels.auto;}"` | — |
| [SRC-DE7EABE998-L000121](../../web/agent.html#L121) | 121 | `"function safeSourceUrl(value){"` | — |
| [SRC-DE7EABE998-L000122](../../web/agent.html#L122) | 122 | `" try{"` | — |
| [SRC-DE7EABE998-L000123](../../web/agent.html#L123) | 123 | `"  const parsed=new URL(String(value??\"\"));"` | — |
| [SRC-DE7EABE998-L000124](../../web/agent.html#L124) | 124 | `"  if(![\"https:\",\"http:\"].includes(parsed.protocol)\|\|!parsed.hostname\|\|parsed.username\|\|parsed.password)return null;"` | — |
| [SRC-DE7EABE998-L000125](../../web/agent.html#L125) | 125 | `"  return parsed.href;"` | — |
| [SRC-DE7EABE998-L000126](../../web/agent.html#L126) | 126 | `" }catch(_error){return null;}"` | — |
| [SRC-DE7EABE998-L000127](../../web/agent.html#L127) | 127 | `"}"` | — |
| [SRC-DE7EABE998-L000128](../../web/agent.html#L128) | 128 | `"function renderSource(s,index){"` | — |
| [SRC-DE7EABE998-L000129](../../web/agent.html#L129) | 129 | `" if(!s\|\|typeof s!==\"object\")return \"\";"` | — |
| [SRC-DE7EABE998-L000130](../../web/agent.html#L130) | 130 | `" const url=safeSourceUrl(s.url);"` | — |
| [SRC-DE7EABE998-L000131](../../web/agent.html#L131) | 131 | `" const title=escapeHtml(s.title\|\|(\"نتيجة ويب \"+(index+1)));"` | — |
| [SRC-DE7EABE998-L000132](../../web/agent.html#L132) | 132 | `" const tags=[];"` | — |
| [SRC-DE7EABE998-L000133](../../web/agent.html#L133) | 133 | `" tags.push('<span class=\"tag\">'+escapeHtml(s.source_class\|\|\"مصدر عام\")+'</span>');"` | — |
| [SRC-DE7EABE998-L000134](../../web/agent.html#L134) | 134 | `" const fetchStatus=s.page_fetch_status\|\|(s.page_fetched?\"content_extracted\":\"not_attempted\");"` | — |
| [SRC-DE7EABE998-L000135](../../web/agent.html#L135) | 135 | `" if(fetchStatus===\"partial_extraction\")tags.push('<span class=\"tag read\">اُستخرج جزء من النص فقط</span>');"` | — |
| [SRC-DE7EABE998-L000136](../../web/agent.html#L136) | 136 | `" else if(fetchStatus===\"content_extracted\"\|\|s.page_fetched)tags.push('<span class=\"tag read\">قُرئت الصفحة واستُخرج نص</span>');"` | — |
| [SRC-DE7EABE998-L000137](../../web/agent.html#L137) | 137 | `" else if(fetchStatus===\"no_text_extracted\"\|\|fetchStatus===\"empty_content\")tags.push('<span class=\"tag\">لم يُستخرج نص؛ قد تكون الصفحة ديناميكية أو محجوبة</span>');"` | — |
| [SRC-DE7EABE998-L000138](../../web/agent.html#L138) | 138 | `" else if(fetchStatus===\"blocked_or_unresolved_host\"\|\|fetchStatus===\"blocked_connection_target\")tags.push('<span class=\"tag\">حُظر العنوان أو تعذّر التحقق الآمن منه</span>');"` | — |
| [SRC-DE7EABE998-L000139](../../web/agent.html#L139) | 139 | `" else if([\"redirect_failed\",\"redirect_rejected\",\"redirect_limit\"].includes(fetchStatus))tags.push('<span class=\"tag\">تعذّر اتباع تحويل الرابط بأمان</span>');"` | — |
| [SRC-DE7EABE998-L000140](../../web/agent.html#L140) | 140 | `" else if(fetchStatus===\"http_error\")tags.push('<span class=\"tag\">الموقع أعاد خطأ HTTP</span>');"` | — |
| [SRC-DE7EABE998-L000141](../../web/agent.html#L141) | 141 | `" else if(fetchStatus===\"unsupported_content_type\")tags.push('<span class=\"tag\">نوع محتوى الصفحة غير مدعوم</span>');"` | — |
| [SRC-DE7EABE998-L000142](../../web/agent.html#L142) | 142 | `" else if(fetchStatus===\"page_too_large\")tags.push('<span class=\"tag\">الصفحة تجاوزت حد الحجم الآمن</span>');"` | — |
| [SRC-DE7EABE998-L000143](../../web/agent.html#L143) | 143 | `" else if(fetchStatus===\"network_error\")tags.push('<span class=\"tag\">تعذّر الاتصال بالصفحة</span>');"` | — |
| [SRC-DE7EABE998-L000144](../../web/agent.html#L144) | 144 | `" else if(fetchStatus===\"budget_exhausted\")tags.push('<span class=\"tag\">توقفت القراءة بسبب حدود الموارد</span>');"` | — |
| [SRC-DE7EABE998-L000145](../../web/agent.html#L145) | 145 | `" else if(fetchStatus===\"rejected_url\")tags.push('<span class=\"tag\">رُفض الرابط لأسباب أمان</span>');"` | — |
| [SRC-DE7EABE998-L000146](../../web/agent.html#L146) | 146 | `" else if(fetchStatus===\"fetch_failed\")tags.push('<span class=\"tag\">تعذّر جلب الصفحة</span>');"` | — |
| [SRC-DE7EABE998-L000147](../../web/agent.html#L147) | 147 | `" else if(fetchStatus===\"attempted\")tags.push('<span class=\"tag\">محاولة جلب الصفحة</span>');"` | — |
| [SRC-DE7EABE998-L000148](../../web/agent.html#L148) | 148 | `" else tags.push('<span class=\"tag\">مقتطف بحث — لم تُحاول قراءة الصفحة</span>');"` | — |
| [SRC-DE7EABE998-L000149](../../web/agent.html#L149) | 149 | `" if(s.platform&&s.platform!==\"web\")tags.push('<span class=\"tag social\">'+escapeHtml(s.platform)+'</span>');"` | — |
| [SRC-DE7EABE998-L000150](../../web/agent.html#L150) | 150 | `" if(s.published_at)tags.push('<span class=\"tag\">تاريخ ظاهر: '+escapeHtml(s.published_at)+'</span>');"` | — |
| [SRC-DE7EABE998-L000151](../../web/agent.html#L151) | 151 | `" const providers=Array.isArray(s.providers)?s.providers.map(escapeHtml):[];"` | — |
| [SRC-DE7EABE998-L000152](../../web/agent.html#L152) | 152 | `" if(s.publisher_name)tags.push('<span class=\"tag\">الناشر: '+escapeHtml(s.publisher_name)+'</span>');"` | — |
| [SRC-DE7EABE998-L000153](../../web/agent.html#L153) | 153 | `" if(s.publisher_url&&safeSourceUrl(s.publisher_url))tags.push('<a class=\"tag\" href=\"'+escapeHtml(s.publisher_url)+'\" target=\"_blank\" rel=\"noopener noreferrer\">صفحة الناشر ↗</a>');"` | — |
| [SRC-DE7EABE998-L000154](../../web/agent.html#L154) | 154 | `" if(providers.length)tags.push('<span class=\"tag\">'+providers.join(\" · \")+'</span>');"` | — |
| [SRC-DE7EABE998-L000155](../../web/agent.html#L155) | 155 | `" if(s.lead_qualification===\"related_result_not_lead\")tags.push('<span class=\"tag social\">نتيجة مرتبطة وليست عميلًا محتملًا</span>');"` | — |
| [SRC-DE7EABE998-L000156](../../web/agent.html#L156) | 156 | `" if(s.lead_qualification===\"public_buyer_intent_signal\")tags.push('<span class=\"tag read\">إشارة علنية محتملة لنية شراء؛ الهوية غير متحققة</span>');"` | — |
| [SRC-DE7EABE998-L000157](../../web/agent.html#L157) | 157 | `" const heading=url?'<a href=\"'+escapeHtml(url)+'\" target=\"_blank\" rel=\"noopener noreferrer\">['+(index+1)+'] '+title+' ↗</a>':'<strong>['+(index+1)+'] '+title+'</strong><p class=\"warning\">لم يُعرض الرابط لأنه غير صالح.</p>';"` | — |
| [SRC-DE7EABE998-L000158](../../web/agent.html#L158) | 158 | `" return '<article class=\"source\">'+heading+'<p>'+escapeHtml(s.snippet\|\|\"لا يتوفر مقتطف نصي من هذه النتيجة.\")+'</p><div class=\"source-meta\">'+tags.join(\"\")+'</div></article>';"` | — |
| [SRC-DE7EABE998-L000159](../../web/agent.html#L159) | 159 | `"}"` | — |
| [SRC-DE7EABE998-L000160](../../web/agent.html#L160) | 160 | `"function renderReport(result){"` | — |
| [SRC-DE7EABE998-L000161](../../web/agent.html#L161) | 161 | `" const r=result&&result.search_report&&typeof result.search_report===\"object\"?result.search_report:{};"` | — |
| [SRC-DE7EABE998-L000162](../../web/agent.html#L162) | 162 | `" const e=r.evidence_signals&&typeof r.evidence_signals===\"object\"?r.evidence_signals:{};"` | — |
| [SRC-DE7EABE998-L000163](../../web/agent.html#L163) | 163 | `" const sources=Array.isArray(result.sources)?result.sources:[];"` | — |
| [SRC-DE7EABE998-L000164](../../web/agent.html#L164) | 164 | `" const researchErrorOutcome=[\"attempted_research_error\",\"unknown_after_research_error\"].includes(r.search_outcome);"` | — |
| [SRC-DE7EABE998-L000165](../../web/agent.html#L165) | 165 | `" const lead=r.lead_generation&&typeof r.lead_generation===\"object\"?r.lead_generation:null;"` | — |
| [SRC-DE7EABE998-L000166](../../web/agent.html#L166) | 166 | `" const leadResearchIncomplete=!!lead&&lead.status===\"research_incomplete\";"` | — |
| [SRC-DE7EABE998-L000167](../../web/agent.html#L167) | 167 | `" const leadSignalCount=lead&&lead.candidate_signal_count!==null&&lead.candidate_signal_count!==undefined&&Number.isFinite(Number(lead.candidate_signal_count))?Number(lead.candidate_signal_count):null;"` | — |
| [SRC-DE7EABE998-L000168](../../web/agent.html#L168) | 168 | `" const noQualifiedLeads=!!lead&&!leadResearchIncomplete&&leadSignalCount===0;"` | — |
| [SRC-DE7EABE998-L000169](../../web/agent.html#L169) | 169 | `" const scoreLabel=lead?(leadResearchIncomplete?\"تعذر حسم البحث عن العملاء\":noQualifiedLeads?\"لم يُثبت وجود عميل محتمل\":\"إشارات نية شراء مرشحة\"):(researchErrorOutcome?\"تعذر تحديد التغطية\":(e.coverage_level\|\|\"تغطية محدودة\"));"` | — |
| [SRC-DE7EABE998-L000170](../../web/agent.html#L170) | 170 | `" const metrics=lead?["` | — |
| [SRC-DE7EABE998-L000171](../../web/agent.html#L171) | 171 | `"  [leadSignalCount??\"غير محدد\",\"إشارة نصية مرشحة لنية شراء\"],"` | — |
| [SRC-DE7EABE998-L000172](../../web/agent.html#L172) | 172 | `"  [lead.related_results_reviewed??\"غير محدد\",\"نتيجة تمت مراجعتها\"],"` | — |
| [SRC-DE7EABE998-L000173](../../web/agent.html#L173) | 173 | `"  [r.pages_fetched??(leadResearchIncomplete?\"غير محدد\":0),\"صفحة قُرئت\"],"` | — |
| [SRC-DE7EABE998-L000174](../../web/agent.html#L174) | 174 | `"  [leadResearchIncomplete?\"غير محدد\":(e.providers_count??(Array.isArray(r.providers_used)?r.providers_used.length:0)),\"واجهة أسهمت بمصدر صالح\"]"` | — |
| [SRC-DE7EABE998-L000175](../../web/agent.html#L175) | 175 | `" ]:["` | — |
| [SRC-DE7EABE998-L000176](../../web/agent.html#L176) | 176 | `"  [researchErrorOutcome?(r.unique_sources??\"غير محدد\"):(r.unique_sources??sources.length),\"مصدرًا فريدًا\"],"` | — |
| [SRC-DE7EABE998-L000177](../../web/agent.html#L177) | 177 | `"  [researchErrorOutcome?\"غير محدد\":(e.unique_domains??\"—\"),\"نطاقًا مختلفًا\"],"` | — |
| [SRC-DE7EABE998-L000178](../../web/agent.html#L178) | 178 | `"  [researchErrorOutcome?(r.pages_fetched??\"غير محدد\"):(r.pages_fetched??e.pages_read??0),\"صفحة قُرئت\"],"` | — |
| [SRC-DE7EABE998-L000179](../../web/agent.html#L179) | 179 | `"  [researchErrorOutcome?\"غير محدد\":(e.providers_count??(Array.isArray(r.providers_used)?r.providers_used.length:0)),\"واجهة أسهمت بمصدر صالح\"]"` | — |
| [SRC-DE7EABE998-L000180](../../web/agent.html#L180) | 180 | `" ];"` | — |
| [SRC-DE7EABE998-L000181](../../web/agent.html#L181) | 181 | `" const metricHtml=metrics.map(([v,l])=>'<div class=\"metric\"><strong>'+escapeHtml(v)+'</strong><span>'+escapeHtml(l)+'</span></div>').join(\"\");"` | — |
| [SRC-DE7EABE998-L000182](../../web/agent.html#L182) | 182 | `" const operationalMetrics=["` | — |
| [SRC-DE7EABE998-L000183](../../web/agent.html#L183) | 183 | `"  [r.provider_candidates_received??\"غير محدد\",\"مرشح أعاده محرك البحث قبل التصفية (قد يتكرر)\"],"` | — |
| [SRC-DE7EABE998-L000184](../../web/agent.html#L184) | 184 | `"  [r.provider_candidates_accepted??\"غير محدد\",\"مرشح اجتاز فحص الموصل قبل الدمج\"],"` | — |
| [SRC-DE7EABE998-L000185](../../web/agent.html#L185) | 185 | `"  [r.provider_candidates_rejected??\"غير محدد\",\"مرشح رُفض بفحص الرابط أو الصلة\"],"` | — |
| [SRC-DE7EABE998-L000186](../../web/agent.html#L186) | 186 | `"  [r.raw_results??\"غير محدد\",\"نتيجة جُمعت قبل دمج التكرارات\"],"` | — |
| [SRC-DE7EABE998-L000187](../../web/agent.html#L187) | 187 | `"  [r.unique_urls??r.unique_sources??sources.length,\"رابط فريد بعد الدمج\"],"` | — |
| [SRC-DE7EABE998-L000188](../../web/agent.html#L188) | 188 | `"  [r.pages_fetch_attempted??\"غير محدد\",\"محاولة جلب صفحة\"],"` | — |
| [SRC-DE7EABE998-L000189](../../web/agent.html#L189) | 189 | `"  [r.pages_content_extracted??r.pages_fetched??\"غير محدد\",\"صفحة استُخرج منها نص\"],"` | — |
| [SRC-DE7EABE998-L000190](../../web/agent.html#L190) | 190 | `"  [r.pages_partial_extracted??\"غير محدد\",\"صفحة استُخرج جزء من نصها\"],"` | — |
| [SRC-DE7EABE998-L000191](../../web/agent.html#L191) | 191 | `"  [r.pages_extract_failed??\"غير محدد\",\"صفحة فشل استخراج نصها\"]"` | — |
| [SRC-DE7EABE998-L000192](../../web/agent.html#L192) | 192 | `" ];"` | — |
| [SRC-DE7EABE998-L000193](../../web/agent.html#L193) | 193 | `" const operationalHtml='<div class=\"metrics\">'+operationalMetrics.map(([v,l])=>'<div class=\"metric\"><strong>'+escapeHtml(v)+'</strong><span>'+escapeHtml(l)+'</span></div>').join(\"\")+'</div>';"` | — |
| [SRC-DE7EABE998-L000194](../../web/agent.html#L194) | 194 | `" const connectors=r.connector_summary&&Array.isArray(r.connector_summary.connectors)?r.connector_summary.connectors:[];"` | — |
| [SRC-DE7EABE998-L000195](../../web/agent.html#L195) | 195 | `" const connectorDetails=connectors.length?'<details class=\"details\"><summary>تشخيص الموصلات في هذا الطلب ('+connectors.length+')</summary><div>'+connectors.map(c=>'<article class=\"source\"><strong>'+escapeHtml(c.name\|\|\"موصل\")+' · '+escapeHtml(c.status\|\|\"unknown\")+'</strong><p>الإعداد: '+escapeHtml(c.configuration_status\|\|\"unknown\")+' · تمت المحاولة: '+escapeHtml(c.attempted===true?\"نعم\":c.attempted===false?\"لا\":\"غير محسوم\")+' · متاح في هذا الطلب: '+escapeHtml(c.available_for_this_request===true?\"نعم\":c.available_for_this_request===false?\"لا\":\"غير محسوم\")+' · استجابة المعالجة مؤكدة: '+escapeHtml(c.verified_for_this_request===true?\"نعم\":c.verified_for_this_request===false?\"لا\":\"غير مختبر/غير محسوم\")+' · إخفاق ملاحظ: '+escapeHtml(c.failure_observed===true?\"نعم\":\"لا\")+' · مرشحون أوليون من الموصل: '+escapeHtml(c.result_count??\"غير محدد\")+' · اجتازوا فحص الموصل: '+escapeHtml(c.accepted_count??\"غير محدد\")+' · مصادر نهائية منسوبة إليه: '+escapeHtml(c.useful_result_count??\"غير محدد\")+' · مرفوض: '+escapeHtml(c.rejected_count??\"غير محدد\")+' · توزيع الرفض: '+escapeHtml(c.rejection_counts_observed===true&&c.rejection_counts?('مرشح مشوّه '+(c.rejection_counts.malformed_candidate??0)+'؛ رابط غير صالح/هدف غير آمن '+(c.rejection_counts.invalid_url_or_unsafe_target??0)+'؛ نطاق محظور '+(c.rejection_counts.blocked_domain??0)+'؛ صلة ضعيفة '+(c.rejection_counts.relevance_below_threshold??0)):'غير مسجل في هذه الجولة')+' · كل المرشحين رُفضوا: '+escapeHtml(c.candidate_rejection_observed===true?\"نعم\":c.candidate_rejection_observed===false?\"لا\":\"غير محسوم\")+'</p>'+((Array.isArray(c.queries)&&c.queries.length)?'<p>استعلامات: '+c.queries.map(escapeHtml).join(\" · \")+'</p>':\"\")+((Array.isArray(c.errors)&&c.errors.length)?'<p class=\"warning\">أخطاء: '+c.errors.map(escapeHtml).join(\" · \")+'</p>':\"\")+'</article>').join(\"\")+'</div></details>':\"\";"` | — |
| [SRC-DE7EABE998-L000196](../../web/agent.html#L196) | 196 | `" const integrity=r.answer_integrity&&typeof r.answer_integrity===\"object\"?r.answer_integrity:null;"` | — |
| [SRC-DE7EABE998-L000197](../../web/agent.html#L197) | 197 | `" const integrityNumbers=integrity&&Array.isArray(integrity.potentially_unsupported_numeric_literals)?integrity.potentially_unsupported_numeric_literals:[];"` | — |
| [SRC-DE7EABE998-L000198](../../web/agent.html#L198) | 198 | `" const integrityTargets=integrity&&Array.isArray(integrity.target_coverage)?integrity.target_coverage:[];"` | — |
| [SRC-DE7EABE998-L000199](../../web/agent.html#L199) | 199 | `" const citationNumericSupport=integrity&&Array.isArray(integrity.citation_numeric_support)?integrity.citation_numeric_support:[];"` | — |
| [SRC-DE7EABE998-L000200](../../web/agent.html#L200) | 200 | `" const citedNumberIssues=citationNumericSupport.filter(item=>item&&Array.isArray(item.potentially_unsupported_numeric_literals)&&item.potentially_unsupported_numeric_literals.length);"` | — |
| [SRC-DE7EABE998-L000201](../../web/agent.html#L201) | 201 | `" const citedNumberHtml=citedNumberIssues.length?'<p class=\"warning\">وجد الفحص أرقامًا قد لا يسندها المصدر المحدد في الاستشهاد؛ راجع المقتطف أو نص الصفحة الأصلي.</p><ul>'+citedNumberIssues.map(item=>'<li>الجملة '+escapeHtml(item.sentence_number??\"غير محدد\")+' · الرقم: '+item.potentially_unsupported_numeric_literals.map(escapeHtml).join(\"، \")+' · الاستشهادات: '+(Array.isArray(item.cited_source_indexes)?item.cited_source_indexes.map(n=>'المصدر '+escapeHtml(n)).join(\"، \"):\"غير محددة\")+'</li>').join(\"\")+'</ul>':\"\";"` | — |
| [SRC-DE7EABE998-L000202](../../web/agent.html#L202) | 202 | `" const valueDiscrepancies=integrity&&Array.isArray(integrity.potential_value_discrepancies)?integrity.potential_value_discrepancies:[];"` | — |
| [SRC-DE7EABE998-L000203](../../web/agent.html#L203) | 203 | `" const valueDimensionLabels={price_or_cost:\"السعر/التكلفة\",area_or_size:\"المساحة/الحجم\",duration:\"المدة\",percentage_or_rate:\"النسبة\",date_or_year:\"التاريخ/السنة\"};"` | — |
| [SRC-DE7EABE998-L000204](../../web/agent.html#L204) | 204 | `" const valueDiscrepancyHtml=valueDiscrepancies.length?'<p class=\"warning\">رُصدت قيم مختلفة في مصادر متعددة. قد يكون الاختلاف بين منتجات أو فترات أو وحدات مختلفة؛ هذه ليست إثباتًا تلقائيًا لوجود تناقض.</p><ul>'+valueDiscrepancies.map(item=>'<li>'+escapeHtml(valueDimensionLabels[item.dimension]\|\|item.dimension\|\|\"قيمة\")+' — '+(Array.isArray(item.values)?item.values.map(value=>escapeHtml(value.value)+' ('+(Array.isArray(value.source_indexes)?value.source_indexes.map(n=>'المصدر '+escapeHtml(n)).join(\"، \"):\"مصدر غير محدد\")+')').join(' مقابل '):\"قِيَم تحتاج مراجعة\")+'</li>').join(\"\")+'</ul>':\"\";"` | — |
| [SRC-DE7EABE998-L000205](../../web/agent.html#L205) | 205 | `" const citationAlignment=integrity&&Array.isArray(integrity.citation_lexical_alignment)?integrity.citation_lexical_alignment:[];"` | — |
| [SRC-DE7EABE998-L000206](../../web/agent.html#L206) | 206 | `" const weakCitationAlignment=citationAlignment.filter(item=>item&&item.status===\"weak_lexical_overlap\");"` | — |
| [SRC-DE7EABE998-L000207](../../web/agent.html#L207) | 207 | `" const citationAlignmentHtml=citationAlignment.length?'<p class=\"report-note\">'+(weakCitationAlignment.length?'لم يظهر تطابق لفظي كافٍ في '+weakCitationAlignment.length+' جملة/جمل مستشهد بها؛ راجع الاستشهادات يدويًا.':'ظهرت إشارات تطابق لفظي لبعض الجمل المستشهد بها، لكنها لا تثبت أن المصدر يسند الادعاء.')+'</p>':\"\";"` | — |
| [SRC-DE7EABE998-L000208](../../web/agent.html#L208) | 208 | `" const integrityScope=integrity?({contains_extracted_page_text_and_or_snippets:\"نص صفحات مستخرج مع مقتطفات بحث\",search_snippets_only:\"مقتطفات بحث فقط — لم يؤكد النظام قراءة نص الصفحات\",no_readable_source_text:\"لا يتوفر نص مصدر قابل للفحص\"}[integrity.source_evidence_scope]\|\|integrity.source_evidence_scope\|\|\"غير محدد\"):\"غير محدد\";"` | — |
| [SRC-DE7EABE998-L000209](../../web/agent.html#L209) | 209 | `" const integritySummary=integrity?'<p class=\"report-note\">عدادات الفحص اللفظي: '+escapeHtml(integrity.potentially_unsupported_numeric_count??0)+' رقم لم يظهر نصيًا في الأدلة؛ '+escapeHtml(integrity.potentially_unsupported_numeric_by_citation_count??0)+' رقم لا يسنده المصدر المشار إليه تحديدًا؛ '+escapeHtml(integrity.potential_value_discrepancy_count??0)+' اختلاف قيمة يحتاج مطابقة؛ '+escapeHtml(integrity.potentially_missing_target_count??0)+' محور محتمل النقص.</p>':\"\";"` | — |
| [SRC-DE7EABE998-L000210](../../web/agent.html#L210) | 210 | `" const taskFulfillmentStatus=r.task_fulfillment_status\|\|result.task_fulfillment_status\|\|\"not_machine_assessed_no_explicit_targets_detected\";"` | — |
| [SRC-DE7EABE998-L000211](../../web/agent.html#L211) | 211 | `" const taskFulfillmentText=({"` | — |
| [SRC-DE7EABE998-L000212](../../web/agent.html#L212) | 212 | `"  possible_gap_detected:\"قد تكون الإجابة أغفلت محورًا من السؤال؛ هذه إشارة لفظية تحتاج مراجعة وليست حكمًا نهائيًا.\","` | — |
| [SRC-DE7EABE998-L000213](../../web/agent.html#L213) | 213 | `"  lexical_signals_found_not_semantically_verified:\"ظهرت إشارات لفظية للمحاور المستخرجة، لكن هذا لا يثبت اكتمال المهمة.\","` | — |
| [SRC-DE7EABE998-L000214](../../web/agent.html#L214) | 214 | `"  not_assessed_insufficient_evidence:\"الأدلة غير كافية؛ لم يتم التحقق من اكتمال المهمة.\","` | — |
| [SRC-DE7EABE998-L000215](../../web/agent.html#L215) | 215 | `"  not_machine_assessed_no_explicit_targets_detected:\"لم تُستخرج محاور صريحة قابلة للفحص؛ اكتمال المهمة لم يُقيّم آليًا.\""` | — |
| [SRC-DE7EABE998-L000216](../../web/agent.html#L216) | 216 | `" })[taskFulfillmentStatus]\|\|\"حالة اكتمال المهمة غير محسومة آليًا.\";"` | — |
| [SRC-DE7EABE998-L000217](../../web/agent.html#L217) | 217 | `" const taskFulfillmentHtml='<p class=\"'+(taskFulfillmentStatus===\"possible_gap_detected\"?\"warning\":\"report-note\")+'\">حالة تنفيذ المطلوب: '+escapeHtml(taskFulfillmentText)+'</p>';"` | — |
| [SRC-DE7EABE998-L000218](../../web/agent.html#L218) | 218 | `" const coverageRepairStatus=r.coverage_repair_status\|\|result.coverage_repair_status\|\|\"\";"` | — |
| [SRC-DE7EABE998-L000219](../../web/agent.html#L219) | 219 | `" const coverageRepairMessages={"` | — |
| [SRC-DE7EABE998-L000220](../../web/agent.html#L220) | 220 | `"  revised_and_reaudited:\"عُدّلت الإجابة بعد رصد محور محتمل النقص ثم خضعت لمراجعة أدلة ثانية؛ تظل المراجعة بمساعدة نموذج وليست تحققًا مستقلًا.\","` | — |
| [SRC-DE7EABE998-L000221](../../web/agent.html#L221) | 221 | `"  reaudit_budget_exhausted:\"انتهت ميزانية النماذج قبل إعادة تدقيق الإجابة المعدلة؛ عُرضت مقتطفات المصادر بدل اعتبار النص المعدل إجابة مكتملة.\","` | — |
| [SRC-DE7EABE998-L000222](../../web/agent.html#L222) | 222 | `"  reaudit_unavailable:\"تعذرت إعادة تدقيق الإجابة المعدلة؛ عُرضت مقتطفات المصادر بدل اعتبار النص المعدل إجابة مكتملة.\","` | — |
| [SRC-DE7EABE998-L000223](../../web/agent.html#L223) | 223 | `"  budget_exhausted:\"انتهت ميزانية النماذج قبل استكمال محور محتمل النقص.\","` | — |
| [SRC-DE7EABE998-L000224](../../web/agent.html#L224) | 224 | `"  unavailable:\"تعذرت محاولة إصلاح محور محتمل النقص.\","` | — |
| [SRC-DE7EABE998-L000225](../../web/agent.html#L225) | 225 | `"  no_change_gap_unresolved:\"لم تغيّر محاولة الإصلاح الإجابة؛ لا يزال احتمال نقص أحد المحاور قائمًا.\""` | — |
| [SRC-DE7EABE998-L000226](../../web/agent.html#L226) | 226 | `" };"` | — |
| [SRC-DE7EABE998-L000227](../../web/agent.html#L227) | 227 | `" const coverageRepairHtml=coverageRepairMessages[coverageRepairStatus]?'<p class=\"warning\">حالة إصلاح التغطية: '+escapeHtml(coverageRepairMessages[coverageRepairStatus])+'</p>':\"\";"` | — |
| [SRC-DE7EABE998-L000228](../../web/agent.html#L228) | 228 | `" const integrityHtml=integrity?'<details class=\"details\"><summary>فحص لفظي أولي: اتساق الإجابة مع الأدلة — ليس تحققًا من الحقيقة</summary><p class=\"report-note\">لا يثبت هذا الفحص صحة الوقائع أو دلالة الاستشهاد. نطاق الأدلة النصية: '+escapeHtml(integrityScope)+'.</p>'+integritySummary+taskFulfillmentHtml+coverageRepairHtml+'<p class=\"report-note\">'+(integrityNumbers.length?'أرقام أو تواريخ تحتاج مراجعة لأنها لم تظهر نصيًا في المواد المتاحة: '+integrityNumbers.map(escapeHtml).join(\"، \")+'.':'لم يرصد الفحص أرقامًا محددة غائبة عن النصوص التي جمعها. هذا لا يثبت أن كل رقم صحيح أو أن المصدر يدعم الادعاء المرتبط به.')+'</p>'+citedNumberHtml+valueDiscrepancyHtml+citationAlignmentHtml+(integrityTargets.length?'<p class=\"report-note\">إشارات التغطية اللفظية لمحاور السؤال:</p><ul>'+integrityTargets.map(t=>'<li>'+escapeHtml(t.target\|\|\"محور\")+' — '+escapeHtml(t.status===\"lexical_signal_found\"?\"وُجد تطابق لفظي؛ ليس إثباتًا لاكتمال الإجابة\":\"قد يكون هذا المحور ناقصًا؛ لم يظهر تطابق لفظي كافٍ\")+'</li>').join(\"\")+'</ul>':\"\")+'<p class=\"report-note\">المنهج: فحص لفظي حتمي محدود. لا يتحقق من معنى الادعاء أو صلة الاستشهاد به أو استقلال المصادر؛ راجع الأدلة الأصلية قبل الاعتماد.</p></details>':\"\";"` | — |
| [SRC-DE7EABE998-L000229](../../web/agent.html#L229) | 229 | `" const providerCounts=r.provider_counts&&typeof r.provider_counts===\"object\"&&!Array.isArray(r.provider_counts)?r.provider_counts:{};"` | — |
| [SRC-DE7EABE998-L000230](../../web/agent.html#L230) | 230 | `" const providerHtml=Object.entries(providerCounts).map(([p,n])=>'<span class=\"provider\">'+escapeHtml(p)+' · '+escapeHtml(n)+'</span>').join(\"\");"` | — |
| [SRC-DE7EABE998-L000231](../../web/agent.html#L231) | 231 | `" const notes=Array.isArray(e.warnings)?e.warnings:[];"` | — |
| [SRC-DE7EABE998-L000232](../../web/agent.html#L232) | 232 | `" const queryList=Array.isArray(result.search_queries)?result.search_queries:[];"` | — |
| [SRC-DE7EABE998-L000233](../../web/agent.html#L233) | 233 | `" const details=queryList.length?'<details class=\"details\"><summary>زوايا البحث المستخدمة ('+queryList.length+')</summary><ol>'+queryList.map(q=>'<li>'+escapeHtml(q)+'</li>').join(\"\")+'</ol></details>':\"\";"` | — |
| [SRC-DE7EABE998-L000234](../../web/agent.html#L234) | 234 | `" const coverageText=lead"` | — |
| [SRC-DE7EABE998-L000235](../../web/agent.html#L235) | 235 | `"  ? (leadResearchIncomplete"` | — |
| [SRC-DE7EABE998-L000236](../../web/agent.html#L236) | 236 | `"     ? \"تعطل البحث أو لم يكتمل التقرير؛ الأعداد غير المتاحة ليست صفرًا، ولا يمكن استنتاج عدم وجود عملاء.\""` | — |
| [SRC-DE7EABE998-L000237](../../web/agent.html#L237) | 237 | `"     : noQualifiedLeads"` | — |
| [SRC-DE7EABE998-L000238](../../web/agent.html#L238) | 238 | `"      ? \"لم تثبت النتائج وجود أي عميل محتمل. عدد صفحات العقارات أو النطاقات ليس عدد المشترين.\""` | — |
| [SRC-DE7EABE998-L000239](../../web/agent.html#L239) | 239 | `"      : \"الإشارات العلنية لا تثبت هوية الشخص أو استمرار رغبته في الشراء؛ راجع نص المصدر وتاريخه يدويًا.\")"` | — |
| [SRC-DE7EABE998-L000240](../../web/agent.html#L240) | 240 | `"  : researchErrorOutcome"` | — |
| [SRC-DE7EABE998-L000241](../../web/agent.html#L241) | 241 | `"   ? \"تعذر تحديد تغطية البحث لأن مسار تجميع الأدلة لم يكتمل؛ الأرقام غير المتاحة ليست صفرًا.\""` | — |
| [SRC-DE7EABE998-L000242](../../web/agent.html#L242) | 242 | `"   : \"تغطية الأدلة: \"+scoreLabel+\" — يصف هذا الوصف اتساع الأدلة المتاحة ولا يمثل احتمال صحة الإجابة.\";"` | — |
| [SRC-DE7EABE998-L000243](../../web/agent.html#L243) | 243 | `" const usableSourceCount=researchErrorOutcome?null:(r.usable_sources_after_filtering??sources.length);"` | — |
| [SRC-DE7EABE998-L000244](../../web/agent.html#L244) | 244 | `" const attemptText=result&&result.search_attempted===true"` | — |
| [SRC-DE7EABE998-L000245](../../web/agent.html#L245) | 245 | `"  ? (r.search_outcome===\"attempted_research_error\""` | — |
| [SRC-DE7EABE998-L000246](../../web/agent.html#L246) | 246 | `"     ? \"بدأت محاولة البحث، لكن تعطل مسار تجميع الأدلة قبل اكتمال التقرير؛ لم يمكن تحديد عدد المصادر القابلة للاستخدام.\""` | — |
| [SRC-DE7EABE998-L000247](../../web/agent.html#L247) | 247 | `"     : \"تمت محاولة البحث في الويب. عدد المصادر القابلة للاستخدام بعد التصفية: \"+(usableSourceCount??\"غير محدد\")+\".\")"` | — |
| [SRC-DE7EABE998-L000248](../../web/agent.html#L248) | 248 | `"  : result&&result.search_attempted===false"` | — |
| [SRC-DE7EABE998-L000249](../../web/agent.html#L249) | 249 | `"   ? \"لم تُنفّذ محاولة بحث ويب في هذه الجولة.\""` | — |
| [SRC-DE7EABE998-L000250](../../web/agent.html#L250) | 250 | `"   : r.search_outcome===\"unknown_after_research_error\""` | — |
| [SRC-DE7EABE998-L000251](../../web/agent.html#L251) | 251 | `"    ? \"تعطل مسار البحث، ولم يمكن تأكيد ما إذا كانت محاولة البحث قد بدأت أو كم مصدرًا كان قابلًا للاستخدام.\""` | — |
| [SRC-DE7EABE998-L000252](../../web/agent.html#L252) | 252 | `"    : \"حالة محاولة البحث غير موضحة في الاستجابة.\";"` | — |
| [SRC-DE7EABE998-L000253](../../web/agent.html#L253) | 253 | `" const qualityText='تصنيف جودة البحث يصف تغطية العملية والأدلة المتاحة، ولا يمثل احتمال صحة الوقائع.';"` | — |
| [SRC-DE7EABE998-L000254](../../web/agent.html#L254) | 254 | `" const reviewText=r.claim_audit_semantics==='model_assisted_not_independent_fact_check'?'مراجعة الادعاءات تمت بمساعدة نموذج لغوي؛ وهي ليست تحققًا مستقلًا من صحة الحقائق.':'لم يثبت إجراء تحقق مستقل من صحة الحقائق.';"` | — |
| [SRC-DE7EABE998-L000255](../../web/agent.html#L255) | 255 | `" const diversityText='اختلاف النطاقات المسجلة لا يثبت الاستقلال التحريري؛ فقد تنقل المواقع عن مصدر أصلي واحد.';"` | — |
| [SRC-DE7EABE998-L000256](../../web/agent.html#L256) | 256 | `" const reportNotes=[coverageText,attemptText,qualityText,reviewText,diversityText,...notes].map(n=>'<p class=\"report-note\">'+escapeHtml(n)+'</p>').join(\"\");"` | — |
| [SRC-DE7EABE998-L000257](../../web/agent.html#L257) | 257 | `" const review=r.second_pass_review===\"model_claim_audit_completed\"?\"مراجعة الادعاءات بمساعدة النموذج تمت (ليست تحققًا مستقلًا)\":r.second_pass_review===\"model_claim_audit_completed_before_coverage_repair\"?\"تمت مراجعة المسودة قبل تعديل التغطية؛ النسخة المعدلة لم تخضع لمراجعة ثانية\":r.second_pass_review===\"model_claim_audit_unavailable\"?\"تعذرت مراجعة الادعاءات بمساعدة النموذج\":\"\";"` | — |
| [SRC-DE7EABE998-L000258](../../web/agent.html#L258) | 258 | `" return '<div class=\"report-head\"><b>ملخص الأدلة وتغطية البحث</b><span class=\"coverage\">'+escapeHtml(scoreLabel)+'</span></div><div class=\"metrics\">'+metricHtml+'</div>'+operationalHtml+connectorDetails+integrityHtml+reportNotes+(providerHtml?'<div class=\"providers\">'+providerHtml+'</div>':\"\")+(review?'<p class=\"report-note\">'+escapeHtml(review)+'</p>':\"\")+details;"` | — |
| [SRC-DE7EABE998-L000259](../../web/agent.html#L259) | 259 | `"}"` | — |
| [SRC-DE7EABE998-L000260](../../web/agent.html#L260) | 260 | `"function addMessage(role,text,result,options={}){"` | — |
| [SRC-DE7EABE998-L000261](../../web/agent.html#L261) | 261 | `" const welcome=$(\"welcome\");if(welcome)welcome.remove();"` | — |
| [SRC-DE7EABE998-L000262](../../web/agent.html#L262) | 262 | `" const box=document.createElement(\"div\");box.className=\"message \"+(role===\"user\"?\"user\":\"assistant\");"` | — |
| [SRC-DE7EABE998-L000263](../../web/agent.html#L263) | 263 | `" const who=document.createElement(\"div\");who.className=\"who\";"` | — |
| [SRC-DE7EABE998-L000264](../../web/agent.html#L264) | 264 | `" who.textContent=role===\"user\"?\"أنت\":(result&&result.used_language_model?\"Omarai · بحث وتحليل توليدي\":\"Omarai · إجابة جزئية أو احتياطية\");"` | — |
| [SRC-DE7EABE998-L000265](../../web/agent.html#L265) | 265 | `" box.appendChild(who);"` | — |
| [SRC-DE7EABE998-L000266](../../web/agent.html#L266) | 266 | `" const linkedQuestion=(options&&options.question)\|\|(result&&result.question);"` | — |
| [SRC-DE7EABE998-L000267](../../web/agent.html#L267) | 267 | `" if(role===\"assistant\"&&linkedQuestion){"` | — |
| [SRC-DE7EABE998-L000268](../../web/agent.html#L268) | 268 | `"  const context=document.createElement(\"div\");context.className=\"message-context\";"` | — |
| [SRC-DE7EABE998-L000269](../../web/agent.html#L269) | 269 | `"  context.textContent=\"ردًا على السؤال: \"+linkedQuestion;box.appendChild(context);"` | — |
| [SRC-DE7EABE998-L000270](../../web/agent.html#L270) | 270 | `" }"` | — |
| [SRC-DE7EABE998-L000271](../../web/agent.html#L271) | 271 | `" const bubble=document.createElement(\"div\");bubble.className=\"bubble\";bubble.innerHTML=answerMarkup(text);box.appendChild(bubble);"` | — |
| [SRC-DE7EABE998-L000272](../../web/agent.html#L272) | 272 | `" if(result&&result.used_web_search!==true&&result.kind!==\"general_answer\"&&result.kind!==\"capability_answer\"){"` | — |
| [SRC-DE7EABE998-L000273](../../web/agent.html#L273) | 273 | `"  const notice=document.createElement(\"div\");notice.className=\"warning\";"` | — |
| [SRC-DE7EABE998-L000274](../../web/agent.html#L274) | 274 | `"  notice.textContent=result.search_attempted===true?\"نُفذت محاولة بحث، لكن لم يؤكد النظام توفر مصادر قابلة للاستخدام؛ تعامل مع الإجابة باعتبارها غير مكتملة حتى مراجعة المصادر.\":result.search_attempted===false?\"لم تُنفذ محاولة بحث ويب في هذه الجولة؛ لا تعتبر الإجابة نتيجة بحث حي.\":\"لم يؤكد النظام نجاح البحث الحي في هذه الجولة؛ تعامل مع الإجابة باعتبارها غير مكتملة حتى مراجعة المصادر.\";"` | — |
| [SRC-DE7EABE998-L000275](../../web/agent.html#L275) | 275 | `"  box.appendChild(notice);"` | — |
| [SRC-DE7EABE998-L000276](../../web/agent.html#L276) | 276 | `" }"` | — |
| [SRC-DE7EABE998-L000277](../../web/agent.html#L277) | 277 | `" if(result&&result.used_language_model!==true&&result.kind!==\"general_answer\"&&result.kind!==\"capability_answer\"){"` | — |
| [SRC-DE7EABE998-L000278](../../web/agent.html#L278) | 278 | `"  const notice=document.createElement(\"div\");notice.className=\"warning\";"` | — |
| [SRC-DE7EABE998-L000279](../../web/agent.html#L279) | 279 | `"  notice.textContent=\"لم تُستخدم استجابة مؤكدة من النموذج اللغوي؛ قد تكون الإجابة مقتطفات أو ردًا احتياطيًا وليست تحليلًا توليديًا كاملًا.\";"` | — |
| [SRC-DE7EABE998-L000280](../../web/agent.html#L280) | 280 | `"  box.appendChild(notice);"` | — |
| [SRC-DE7EABE998-L000281](../../web/agent.html#L281) | 281 | `" }"` | — |
| [SRC-DE7EABE998-L000282](../../web/agent.html#L282) | 282 | `" if(result&&result.search_report){"` | — |
| [SRC-DE7EABE998-L000283](../../web/agent.html#L283) | 283 | `"  const report=document.createElement(\"section\");report.className=\"report\";report.innerHTML=renderReport(result);box.appendChild(report);"` | — |
| [SRC-DE7EABE998-L000284](../../web/agent.html#L284) | 284 | `" }"` | — |
| [SRC-DE7EABE998-L000285](../../web/agent.html#L285) | 285 | `" if(result&&Array.isArray(result.warnings)&&result.warnings.length){"` | — |
| [SRC-DE7EABE998-L000286](../../web/agent.html#L286) | 286 | `"  const warning=document.createElement(\"div\");warning.className=\"warning\";"` | — |
| [SRC-DE7EABE998-L000287](../../web/agent.html#L287) | 287 | `"  warning.textContent=result.warnings.join(\" \");box.appendChild(warning);"` | — |
| [SRC-DE7EABE998-L000288](../../web/agent.html#L288) | 288 | `" }"` | — |
| [SRC-DE7EABE998-L000289](../../web/agent.html#L289) | 289 | `" const rawSources=result&&Array.isArray(result.sources)?result.sources:[];"` | — |
| [SRC-DE7EABE998-L000290](../../web/agent.html#L290) | 290 | `" const usableSources=rawSources.filter(s=>s&&typeof s===\"object\"&&safeSourceUrl(s.url));"` | — |
| [SRC-DE7EABE998-L000291](../../web/agent.html#L291) | 291 | `" if(usableSources.length){"` | — |
| [SRC-DE7EABE998-L000292](../../web/agent.html#L292) | 292 | `"  const sources=document.createElement(\"div\");sources.className=\"sources\";"` | — |
| [SRC-DE7EABE998-L000293](../../web/agent.html#L293) | 293 | `"  sources.innerHTML=usableSources.map((s,i)=>renderSource(s,i)).join(\"\");box.appendChild(sources);"` | — |
| [SRC-DE7EABE998-L000294](../../web/agent.html#L294) | 294 | `" }else if(role===\"assistant\"&&result&&result.kind!==\"general_answer\"&&result.kind!==\"capability_answer\"){"` | — |
| [SRC-DE7EABE998-L000295](../../web/agent.html#L295) | 295 | `"  const no=document.createElement(\"p\");no.className=\"no-sources\";"` | — |
| [SRC-DE7EABE998-L000296](../../web/agent.html#L296) | 296 | `"  no.textContent=\"لم يتم إرجاع مصدر صالح قابل للفتح في هذه الجولة. لا تعتبر الإجابة المدعومة بلا مصادر نتيجة بحث ناجحة.\";"` | — |
| [SRC-DE7EABE998-L000297](../../web/agent.html#L297) | 297 | `"  box.appendChild(no);"` | — |
| [SRC-DE7EABE998-L000298](../../web/agent.html#L298) | 298 | `" }"` | — |
| [SRC-DE7EABE998-L000299](../../web/agent.html#L299) | 299 | `" $(\"messages\").appendChild(box);box.scrollIntoView({behavior:\"smooth\",block:\"end\"});"` | — |
| [SRC-DE7EABE998-L000300](../../web/agent.html#L300) | 300 | `" return box;"` | — |
| [SRC-DE7EABE998-L000301](../../web/agent.html#L301) | 301 | `"}"` | — |
| [SRC-DE7EABE998-L000302](../../web/agent.html#L302) | 302 | `"function setBusy(on){busy=on;$(\"send\").disabled=on;$(\"send\").textContent=on?\"يبحث…\":\"ابحث ←\";$(\"question\").disabled=on;document.querySelectorAll(\".mode-btn\").forEach(b=>b.disabled=on);}"` | — |
| [SRC-DE7EABE998-L000303](../../web/agent.html#L303) | 303 | `"async function ask(value){"` | — |
| [SRC-DE7EABE998-L000304](../../web/agent.html#L304) | 304 | `" const q=(value??$(\"question\").value).trim();if(!q\|\|busy)return;"` | — |
| [SRC-DE7EABE998-L000305](../../web/agent.html#L305) | 305 | `" addMessage(\"user\",q);$(\"question\").value=\"\";setBusy(true);"` | — |
| [SRC-DE7EABE998-L000306](../../web/agent.html#L306) | 306 | `" setStatus(\"جارٍ تنفيذ البحث عن السؤال الحالي…\",\"warn\");"` | — |
| [SRC-DE7EABE998-L000307](../../web/agent.html#L307) | 307 | `" const pending=document.createElement(\"div\");pending.className=\"message assistant\";"` | — |
| [SRC-DE7EABE998-L000308](../../web/agent.html#L308) | 308 | `" pending.innerHTML='<div class=\"who\">Omarai · '+escapeHtml(modeName(activeMode))+'</div><div class=\"bubble\"><div class=\"pending\"><span class=\"spinner\"></span><span>يبحث الآن ويجمع المصادر. ستظهر نتيجة هذه الجولة مرتبطة بسؤالك أدناه.</span></div></div>';"` | — |
| [SRC-DE7EABE998-L000309](../../web/agent.html#L309) | 309 | `" $(\"messages\").appendChild(pending);pending.scrollIntoView({behavior:\"smooth\",block:\"end\"});"` | — |
| [SRC-DE7EABE998-L000310](../../web/agent.html#L310) | 310 | `" try{"` | — |
| [SRC-DE7EABE998-L000311](../../web/agent.html#L311) | 311 | `"  const response=await fetch(\"/api/agent\",{method:\"POST\",headers:apiHeaders(),body:JSON.stringify({question:q,history:history.slice(-8),mode:activeMode})});"` | — |
| [SRC-DE7EABE998-L000312](../../web/agent.html#L312) | 312 | `"  const data=await response.json().catch(()=>({}));"` | — |
| [SRC-DE7EABE998-L000313](../../web/agent.html#L313) | 313 | `"  pending.remove();"` | — |
| [SRC-DE7EABE998-L000314](../../web/agent.html#L314) | 314 | `"  if(!response.ok){"` | — |
| [SRC-DE7EABE998-L000315](../../web/agent.html#L315) | 315 | `"   if(response.status===401)throw Error(\"رمز الوصول غير صحيح أو غير محفوظ. راجع رمز التطبيق المستضاف.\");"` | — |
| [SRC-DE7EABE998-L000316](../../web/agent.html#L316) | 316 | `"   if(response.status===429)throw Error(\"تجاوز حد الطلبات المؤقت. انتظر قليلًا ثم أعد المحاولة.\");"` | — |
| [SRC-DE7EABE998-L000317](../../web/agent.html#L317) | 317 | `"   throw Error(data.error\|\|\"تعذر إكمال البحث. أعد المحاولة بعد التحقق من الاتصال.\");"` | — |
| [SRC-DE7EABE998-L000318](../../web/agent.html#L318) | 318 | `"  }"` | — |
| [SRC-DE7EABE998-L000319](../../web/agent.html#L319) | 319 | `"  addMessage(\"assistant\",data.answer\|\|\"لم يرجع الخادم نص إجابة.\",data);"` | — |
| [SRC-DE7EABE998-L000320](../../web/agent.html#L320) | 320 | `"  history.push({role:\"user\",content:q},{role:\"assistant\",content:String(data.answer\|\|\"\")});"` | — |
| [SRC-DE7EABE998-L000321](../../web/agent.html#L321) | 321 | `"  const sources=Array.isArray(data.sources)?data.sources.filter(s=>s&&safeSourceUrl(s.url)):[];"` | — |
| [SRC-DE7EABE998-L000322](../../web/agent.html#L322) | 322 | `"  if(data.kind===\"general_answer\"){"` | — |
| [SRC-DE7EABE998-L000323](../../web/agent.html#L323) | 323 | `"   setStatus(\"اكتملت إجابة المعرفة العامة دون بحث ويب\",\"ok\");"` | — |
| [SRC-DE7EABE998-L000324](../../web/agent.html#L324) | 324 | `"  }else if(data.kind===\"capability_answer\"){"` | — |
| [SRC-DE7EABE998-L000325](../../web/agent.html#L325) | 325 | `"   setStatus(\"إجابة عن قدرات Omarai وحدوده · لم يُجر بحث حي\",\"ok\");"` | — |
| [SRC-DE7EABE998-L000326](../../web/agent.html#L326) | 326 | `"  }else if(data.used_web_search===true&&data.used_language_model===true&&sources.length>0){"` | — |
| [SRC-DE7EABE998-L000327](../../web/agent.html#L327) | 327 | `"   setStatus(\"اكتمل البحث والتحليل · \"+sources.length+\" مصدرًا صالحًا\",\"ok\");"` | — |
| [SRC-DE7EABE998-L000328](../../web/agent.html#L328) | 328 | `"  }else if(data.used_web_search===true&&sources.length>0){"` | — |
| [SRC-DE7EABE998-L000329](../../web/agent.html#L329) | 329 | `"   setStatus(\"البحث أعاد مصادر، لكن التحليل غير مكتمل\",\"warn\");"` | — |
| [SRC-DE7EABE998-L000330](../../web/agent.html#L330) | 330 | `"  }else{"` | — |
| [SRC-DE7EABE998-L000331](../../web/agent.html#L331) | 331 | `"   setStatus(\"نتيجة جزئية: لا يوجد بحث حي مؤكد مع مصادر كافية\",\"bad\");"` | — |
| [SRC-DE7EABE998-L000332](../../web/agent.html#L332) | 332 | `"  }"` | — |
| [SRC-DE7EABE998-L000333](../../web/agent.html#L333) | 333 | `" }catch(error){"` | — |
| [SRC-DE7EABE998-L000334](../../web/agent.html#L334) | 334 | `"  pending.remove();"` | — |
| [SRC-DE7EABE998-L000335](../../web/agent.html#L335) | 335 | `"  const safeMessage=error&&error.message?error.message:\"تعذر إكمال الطلب.\";"` | — |
| [SRC-DE7EABE998-L000336](../../web/agent.html#L336) | 336 | `"  const box=addMessage(\"assistant\",safeMessage,null,{question:q});"` | — |
| [SRC-DE7EABE998-L000337](../../web/agent.html#L337) | 337 | `"  const actions=document.createElement(\"div\");actions.className=\"retry-row\";"` | — |
| [SRC-DE7EABE998-L000338](../../web/agent.html#L338) | 338 | `"  const retry=document.createElement(\"button\");retry.type=\"button\";retry.className=\"retry-button\";"` | — |
| [SRC-DE7EABE998-L000339](../../web/agent.html#L339) | 339 | `"  retry.textContent=\"إعادة محاولة هذا السؤال\";"` | — |
| [SRC-DE7EABE998-L000340](../../web/agent.html#L340) | 340 | `"  retry.addEventListener(\"click\",()=>ask(q));actions.appendChild(retry);box.appendChild(actions);"` | — |
| [SRC-DE7EABE998-L000341](../../web/agent.html#L341) | 341 | `"  setStatus(\"لم يكتمل الطلب؛ يمكنك إعادة محاولة السؤال نفسه\",\"bad\");"` | — |
| [SRC-DE7EABE998-L000342](../../web/agent.html#L342) | 342 | `" }finally{"` | — |
| [SRC-DE7EABE998-L000343](../../web/agent.html#L343) | 343 | `"  setBusy(false);$(\"question\").focus();"` | — |
| [SRC-DE7EABE998-L000344](../../web/agent.html#L344) | 344 | `" }"` | — |
| [SRC-DE7EABE998-L000345](../../web/agent.html#L345) | 345 | `"}"` | — |
| [SRC-DE7EABE998-L000346](../../web/agent.html#L346) | 346 | `"async function runDiagnostics(){"` | — |
| [SRC-DE7EABE998-L000347](../../web/agent.html#L347) | 347 | `" const button=$(\"runDiagnostics\"),output=$(\"diagnosticsResult\");if(button.disabled)return;"` | — |
| [SRC-DE7EABE998-L000348](../../web/agent.html#L348) | 348 | `" button.disabled=true;button.textContent=\"جارٍ الاختبار الحقيقي…\";output.textContent=\"يُرسل الآن طلب فعلي إلى محركات البحث، وقد يستغرق بضع ثوانٍ.\";"` | — |
| [SRC-DE7EABE998-L000349](../../web/agent.html#L349) | 349 | `" try{"` | — |
| [SRC-DE7EABE998-L000350](../../web/agent.html#L350) | 350 | `"  const response=await fetch(\"/api/diagnostics\",{method:\"POST\",headers:apiHeaders(),body:JSON.stringify({test_model:true,test_social:$(\"diagSocial\").checked})});"` | — |
| [SRC-DE7EABE998-L000351](../../web/agent.html#L351) | 351 | `"  const data=await response.json();if(!response.ok)throw Error(data.error\|\|\"فشل طلب الاختبار\");"` | — |
| [SRC-DE7EABE998-L000352](../../web/agent.html#L352) | 352 | `"  const labels={passed:\"نجح فعليًا\",degraded:\"جزئي أو بلا نتائج كافية\",failed:\"فشل\",skipped:\"لم يُختبر\",not_configured:\"غير مضبوط\"};"` | — |
| [SRC-DE7EABE998-L000353](../../web/agent.html#L353) | 353 | `"  const lines=[\"النتيجة: \"+(labels[data.overall_status]\|\|data.overall_status)];"` | — |
| [SRC-DE7EABE998-L000354](../../web/agent.html#L354) | 354 | `"  for(const [key,label] of [[\"web_search\",\"بحث الإنترنت\"],[\"language_model\",\"النموذج اللغوي\"],[\"social_search\",\"المصادر الاجتماعية\"]]){"` | — |
| [SRC-DE7EABE998-L000355](../../web/agent.html#L355) | 355 | `"   const item=(data.checks\|\|{})[key];if(!item)continue;"` | — |
| [SRC-DE7EABE998-L000356](../../web/agent.html#L356) | 356 | `"   lines.push(label+\": \"+(labels[item.status]\|\|item.status)+(item.result_count!==undefined?\" · \"+item.result_count+\" نتيجة\":\"\"));"` | — |
| [SRC-DE7EABE998-L000357](../../web/agent.html#L357) | 357 | `"   if(item.provider_counts&&Object.keys(item.provider_counts).length)lines.push(\"المصادر التي أعادت نتائج: \"+Object.entries(item.provider_counts).map(([p,n])=>p+\" (\"+n+\")\").join(\"، \"));"` | — |
| [SRC-DE7EABE998-L000358](../../web/agent.html#L358) | 358 | `"   if(item.note)lines.push(item.note);"` | — |
| [SRC-DE7EABE998-L000359](../../web/agent.html#L359) | 359 | `"   if(item.warnings&&item.warnings.length)lines.push(item.warnings.join(\"؛ \"));"` | — |
| [SRC-DE7EABE998-L000360](../../web/agent.html#L360) | 360 | `"  }"` | — |
| [SRC-DE7EABE998-L000361](../../web/agent.html#L361) | 361 | `"  if(data.model_usage&&data.model_usage.length)lines.push(\"النموذج المستخدم: \"+data.model_usage.map(x=>x.used_model).join(\"، \"));"` | — |
| [SRC-DE7EABE998-L000362](../../web/agent.html#L362) | 362 | `"  if(data.elapsed_ms!==undefined)lines.push(\"مدة الاختبار: \"+(data.elapsed_ms/1000).toFixed(1)+\" ثانية\");"` | — |
| [SRC-DE7EABE998-L000363](../../web/agent.html#L363) | 363 | `"  output.textContent=lines.join(\"\\n\");setStatus(data.overall_status===\"passed\"?\"نجح الاختبار الحي\":data.overall_status===\"failed\"?\"فشل الاختبار الحي\":\"نتيجة الاختبار جزئية\",data.overall_status===\"passed\"?\"ok\":data.overall_status===\"failed\"?\"bad\":\"warn\");"` | — |
| [SRC-DE7EABE998-L000364](../../web/agent.html#L364) | 364 | `" }catch(e){output.textContent=\"تعذّر الاختبار الحي: \"+(e&&e.message?e.message:\"خطأ غير معروف\");setStatus(\"فشل الاختبار الحي\",\"bad\");}"` | — |
| [SRC-DE7EABE998-L000365](../../web/agent.html#L365) | 365 | `" finally{button.disabled=false;button.textContent=\"إعادة الاختبار الحي\";}"` | — |
