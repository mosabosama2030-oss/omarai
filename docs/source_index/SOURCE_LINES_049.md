# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **049**
- سجلات الأسطر: **800**
- النطاق: SRC-F725E90B2A-L003343 إلى SRC-DE7EABE998-L000109
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-F725E90B2A — [tests/test_web_agent.py](../../tests/test_web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-F725E90B2A-L003343](../../tests/test_web_agent.py#L3343) | 3343 | `"    def capture_relevance(query, text):"` | — |
| [SRC-F725E90B2A-L003344](../../tests/test_web_agent.py#L3344) | 3344 | `"        if \"تجارب السيارات الكهربائية المستعملة\" in text:"` | — |
| [SRC-F725E90B2A-L003345](../../tests/test_web_agent.py#L3345) | 3345 | `"            source_queries.append(query)"` | — |
| [SRC-F725E90B2A-L003346](../../tests/test_web_agent.py#L3346) | 3346 | `"            if planned_query and query != compact_search_query(topic_query):"` | — |
| [SRC-F725E90B2A-L003347](../../tests/test_web_agent.py#L3347) | 3347 | `"                return 0.0"` | — |
| [SRC-F725E90B2A-L003348](../../tests/test_web_agent.py#L3348) | 3348 | `"        return 0.25"` | — |
| [SRC-F725E90B2A-L003349](../../tests/test_web_agent.py#L3349) | 3349 | `""` | — |
| [SRC-F725E90B2A-L003350](../../tests/test_web_agent.py#L3350) | 3350 | `"    monkeypatch.setattr(\"agents.web_agent._relevance_ratio\", capture_relevance)"` | — |
| [SRC-F725E90B2A-L003351](../../tests/test_web_agent.py#L3351) | 3351 | `""` | — |
| [SRC-F725E90B2A-L003352](../../tests/test_web_agent.py#L3352) | 3352 | `"    agent.answer(question)"` | — |
| [SRC-F725E90B2A-L003353](../../tests/test_web_agent.py#L3353) | 3353 | `""` | — |
| [SRC-F725E90B2A-L003354](../../tests/test_web_agent.py#L3354) | 3354 | `"    expected_queries = list(dict.fromkeys("` | — |
| [SRC-F725E90B2A-L003355](../../tests/test_web_agent.py#L3355) | 3355 | `"        query for query in ("` | — |
| [SRC-F725E90B2A-L003356](../../tests/test_web_agent.py#L3356) | 3356 | `"            compact_search_query(question),"` | — |
| [SRC-F725E90B2A-L003357](../../tests/test_web_agent.py#L3357) | 3357 | `"            compact_search_query(topic_query),"` | — |
| [SRC-F725E90B2A-L003358](../../tests/test_web_agent.py#L3358) | 3358 | `"        ) if query"` | — |
| [SRC-F725E90B2A-L003359](../../tests/test_web_agent.py#L3359) | 3359 | `"    ))"` | — |
| [SRC-F725E90B2A-L003360](../../tests/test_web_agent.py#L3360) | 3360 | `"    assert source_queries == expected_queries"` | — |
| [SRC-F725E90B2A-L003361](../../tests/test_web_agent.py#L3361) | 3361 | `""` | — |
| [SRC-F725E90B2A-L003362](../../tests/test_web_agent.py#L3362) | 3362 | `""` | — |
| [SRC-F725E90B2A-L003363](../../tests/test_web_agent.py#L3363) | 3363 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L003364](../../tests/test_web_agent.py#L3364) | 3364 | `"    (\"mode\", \"planner_query\"),"` | — |
| [SRC-F725E90B2A-L003365](../../tests/test_web_agent.py#L3365) | 3365 | `"    ["` | — |
| [SRC-F725E90B2A-L003366](../../tests/test_web_agent.py#L3366) | 3366 | `"        (\"auto\", \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\"),"` | — |
| [SRC-F725E90B2A-L003367](../../tests/test_web_agent.py#L3367) | 3367 | `"        (\"auto\", \"site:reddit.com\"),"` | — |
| [SRC-F725E90B2A-L003368](../../tests/test_web_agent.py#L3368) | 3368 | `"        (\"latest\", \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\"),"` | — |
| [SRC-F725E90B2A-L003369](../../tests/test_web_agent.py#L3369) | 3369 | `"        (\"deep\", \"site:reddit.com\"),"` | — |
| [SRC-F725E90B2A-L003370](../../tests/test_web_agent.py#L3370) | 3370 | `"        (\"social\", \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\"),"` | — |
| [SRC-F725E90B2A-L003371](../../tests/test_web_agent.py#L3371) | 3371 | `"    ],"` | — |
| [SRC-F725E90B2A-L003372](../../tests/test_web_agent.py#L3372) | 3372 | `")"` | — |
| [SRC-F725E90B2A-L003373](../../tests/test_web_agent.py#L3373) | 3373 | `"def test_modes_do_not_create_generic_queries_without_topic("` | — |
| [SRC-F725E90B2A-L003374](../../tests/test_web_agent.py#L3374) | 3374 | `"    monkeypatch, mode, planner_query"` | — |
| [SRC-F725E90B2A-L003375](../../tests/test_web_agent.py#L3375) | 3375 | `"):"` | — |
| [SRC-F725E90B2A-L003376](../../tests/test_web_agent.py#L3376) | 3376 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003377](../../tests/test_web_agent.py#L3377) | 3377 | `"    instruction_only = \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\""` | — |
| [SRC-F725E90B2A-L003378](../../tests/test_web_agent.py#L3378) | 3378 | `"    direct_url = \"https://example.com/report\""` | — |
| [SRC-F725E90B2A-L003379](../../tests/test_web_agent.py#L3379) | 3379 | `"    observed_plans = []"` | — |
| [SRC-F725E90B2A-L003380](../../tests/test_web_agent.py#L3380) | 3380 | `""` | — |
| [SRC-F725E90B2A-L003381](../../tests/test_web_agent.py#L3381) | 3381 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003382](../../tests/test_web_agent.py#L3382) | 3382 | `"        \"agents.web_agent.route_intent\","` | — |
| [SRC-F725E90B2A-L003383](../../tests/test_web_agent.py#L3383) | 3383 | `"        lambda *args, **kwargs: {\"route\": \"WEB_DEEP\", \"reason\": \"test\"},"` | — |
| [SRC-F725E90B2A-L003384](../../tests/test_web_agent.py#L3384) | 3384 | `"    )"` | — |
| [SRC-F725E90B2A-L003385](../../tests/test_web_agent.py#L3385) | 3385 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003386](../../tests/test_web_agent.py#L3386) | 3386 | `"        agent, \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003387](../../tests/test_web_agent.py#L3387) | 3387 | `"        lambda _question, _history: {"` | — |
| [SRC-F725E90B2A-L003388](../../tests/test_web_agent.py#L3388) | 3388 | `"            \"queries\": [planner_query],"` | — |
| [SRC-F725E90B2A-L003389](../../tests/test_web_agent.py#L3389) | 3389 | `"            \"direct_urls\": [direct_url],"` | — |
| [SRC-F725E90B2A-L003390](../../tests/test_web_agent.py#L3390) | 3390 | `"            \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003391](../../tests/test_web_agent.py#L3391) | 3391 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003392](../../tests/test_web_agent.py#L3392) | 3392 | `"            \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L003393](../../tests/test_web_agent.py#L3393) | 3393 | `"            \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003394](../../tests/test_web_agent.py#L3394) | 3394 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003395](../../tests/test_web_agent.py#L3395) | 3395 | `"        },"` | — |
| [SRC-F725E90B2A-L003396](../../tests/test_web_agent.py#L3396) | 3396 | `"    )"` | — |
| [SRC-F725E90B2A-L003397](../../tests/test_web_agent.py#L3397) | 3397 | `""` | — |
| [SRC-F725E90B2A-L003398](../../tests/test_web_agent.py#L3398) | 3398 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L003399](../../tests/test_web_agent.py#L3399) | 3399 | `"        observed_plans.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L003400](../../tests/test_web_agent.py#L3400) | 3400 | `"        return [], [], {"` | — |
| [SRC-F725E90B2A-L003401](../../tests/test_web_agent.py#L3401) | 3401 | `"            \"queries_planned\": len(research_plan.get(\"queries\", [])),"` | — |
| [SRC-F725E90B2A-L003402](../../tests/test_web_agent.py#L3402) | 3402 | `"            \"queries_attempted\": 0,"` | — |
| [SRC-F725E90B2A-L003403](../../tests/test_web_agent.py#L3403) | 3403 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L003404](../../tests/test_web_agent.py#L3404) | 3404 | `"            \"unique_sources\": 0,"` | — |
| [SRC-F725E90B2A-L003405](../../tests/test_web_agent.py#L3405) | 3405 | `"            \"pages_fetched\": 0,"` | — |
| [SRC-F725E90B2A-L003406](../../tests/test_web_agent.py#L3406) | 3406 | `"            \"providers_used\": [],"` | — |
| [SRC-F725E90B2A-L003407](../../tests/test_web_agent.py#L3407) | 3407 | `"            \"platform_counts\": {},"` | — |
| [SRC-F725E90B2A-L003408](../../tests/test_web_agent.py#L3408) | 3408 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L003409](../../tests/test_web_agent.py#L3409) | 3409 | `"            \"depth\": research_plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-F725E90B2A-L003410](../../tests/test_web_agent.py#L3410) | 3410 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003411](../../tests/test_web_agent.py#L3411) | 3411 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L003412](../../tests/test_web_agent.py#L3412) | 3412 | `"        }"` | — |
| [SRC-F725E90B2A-L003413](../../tests/test_web_agent.py#L3413) | 3413 | `""` | — |
| [SRC-F725E90B2A-L003414](../../tests/test_web_agent.py#L3414) | 3414 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L003415](../../tests/test_web_agent.py#L3415) | 3415 | `""` | — |
| [SRC-F725E90B2A-L003416](../../tests/test_web_agent.py#L3416) | 3416 | `"    agent.answer(instruction_only, mode=mode)"` | — |
| [SRC-F725E90B2A-L003417](../../tests/test_web_agent.py#L3417) | 3417 | `""` | — |
| [SRC-F725E90B2A-L003418](../../tests/test_web_agent.py#L3418) | 3418 | `"    assert observed_plans"` | — |
| [SRC-F725E90B2A-L003419](../../tests/test_web_agent.py#L3419) | 3419 | `"    assert observed_plans[0][\"queries\"] == []"` | — |
| [SRC-F725E90B2A-L003420](../../tests/test_web_agent.py#L3420) | 3420 | `"    assert observed_plans[0][\"direct_urls\"] == [direct_url]"` | — |
| [SRC-F725E90B2A-L003421](../../tests/test_web_agent.py#L3421) | 3421 | `""` | — |
| [SRC-F725E90B2A-L003422](../../tests/test_web_agent.py#L3422) | 3422 | `""` | — |
| [SRC-F725E90B2A-L003423](../../tests/test_web_agent.py#L3423) | 3423 | `"def test_auto_navigation_strips_arabic_search_verb_without_regex_regression(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003424](../../tests/test_web_agent.py#L3424) | 3424 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003425](../../tests/test_web_agent.py#L3425) | 3425 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L003426](../../tests/test_web_agent.py#L3426) | 3426 | `"    question = \"ابحث عن الموقع الرسمي لشركة النور\""` | — |
| [SRC-F725E90B2A-L003427](../../tests/test_web_agent.py#L3427) | 3427 | `"    observed_plans = []"` | — |
| [SRC-F725E90B2A-L003428](../../tests/test_web_agent.py#L3428) | 3428 | `""` | — |
| [SRC-F725E90B2A-L003429](../../tests/test_web_agent.py#L3429) | 3429 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003430](../../tests/test_web_agent.py#L3430) | 3430 | `"        \"agents.web_agent.route_intent\","` | — |
| [SRC-F725E90B2A-L003431](../../tests/test_web_agent.py#L3431) | 3431 | `"        lambda *args, **kwargs: {\"route\": \"WEB_SIMPLE\", \"reason\": \"test\"},"` | — |
| [SRC-F725E90B2A-L003432](../../tests/test_web_agent.py#L3432) | 3432 | `"    )"` | — |
| [SRC-F725E90B2A-L003433](../../tests/test_web_agent.py#L3433) | 3433 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003434](../../tests/test_web_agent.py#L3434) | 3434 | `"        \"agents.web_agent.compact_search_query\","` | — |
| [SRC-F725E90B2A-L003435](../../tests/test_web_agent.py#L3435) | 3435 | `"        lambda value: value.strip() if isinstance(value, str) else \"\","` | — |
| [SRC-F725E90B2A-L003436](../../tests/test_web_agent.py#L3436) | 3436 | `"    )"` | — |
| [SRC-F725E90B2A-L003437](../../tests/test_web_agent.py#L3437) | 3437 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003438](../../tests/test_web_agent.py#L3438) | 3438 | `"        agent, \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003439](../../tests/test_web_agent.py#L3439) | 3439 | `"        lambda _question, _history: {"` | — |
| [SRC-F725E90B2A-L003440](../../tests/test_web_agent.py#L3440) | 3440 | `"            \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L003441](../../tests/test_web_agent.py#L3441) | 3441 | `"            \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L003442](../../tests/test_web_agent.py#L3442) | 3442 | `"            \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003443](../../tests/test_web_agent.py#L3443) | 3443 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003444](../../tests/test_web_agent.py#L3444) | 3444 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003445](../../tests/test_web_agent.py#L3445) | 3445 | `"            \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003446](../../tests/test_web_agent.py#L3446) | 3446 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003447](../../tests/test_web_agent.py#L3447) | 3447 | `"        },"` | — |
| [SRC-F725E90B2A-L003448](../../tests/test_web_agent.py#L3448) | 3448 | `"    )"` | — |
| [SRC-F725E90B2A-L003449](../../tests/test_web_agent.py#L3449) | 3449 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003450](../../tests/test_web_agent.py#L3450) | 3450 | `"        \"agents.web_agent.fallback_plan\","` | — |
| [SRC-F725E90B2A-L003451](../../tests/test_web_agent.py#L3451) | 3451 | `"        lambda *args, **kwargs: {\"queries\": [question]},"` | — |
| [SRC-F725E90B2A-L003452](../../tests/test_web_agent.py#L3452) | 3452 | `"    )"` | — |
| [SRC-F725E90B2A-L003453](../../tests/test_web_agent.py#L3453) | 3453 | `""` | — |
| [SRC-F725E90B2A-L003454](../../tests/test_web_agent.py#L3454) | 3454 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L003455](../../tests/test_web_agent.py#L3455) | 3455 | `"        observed_plans.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L003456](../../tests/test_web_agent.py#L3456) | 3456 | `"        return [], [], {"` | — |
| [SRC-F725E90B2A-L003457](../../tests/test_web_agent.py#L3457) | 3457 | `"            \"queries_planned\": len(research_plan.get(\"queries\", [])),"` | — |
| [SRC-F725E90B2A-L003458](../../tests/test_web_agent.py#L3458) | 3458 | `"            \"queries_attempted\": 0,"` | — |
| [SRC-F725E90B2A-L003459](../../tests/test_web_agent.py#L3459) | 3459 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L003460](../../tests/test_web_agent.py#L3460) | 3460 | `"            \"unique_sources\": 0,"` | — |
| [SRC-F725E90B2A-L003461](../../tests/test_web_agent.py#L3461) | 3461 | `"            \"pages_fetched\": 0,"` | — |
| [SRC-F725E90B2A-L003462](../../tests/test_web_agent.py#L3462) | 3462 | `"            \"providers_used\": [],"` | — |
| [SRC-F725E90B2A-L003463](../../tests/test_web_agent.py#L3463) | 3463 | `"            \"platform_counts\": {},"` | — |
| [SRC-F725E90B2A-L003464](../../tests/test_web_agent.py#L3464) | 3464 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L003465](../../tests/test_web_agent.py#L3465) | 3465 | `"            \"depth\": research_plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-F725E90B2A-L003466](../../tests/test_web_agent.py#L3466) | 3466 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003467](../../tests/test_web_agent.py#L3467) | 3467 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L003468](../../tests/test_web_agent.py#L3468) | 3468 | `"        }"` | — |
| [SRC-F725E90B2A-L003469](../../tests/test_web_agent.py#L3469) | 3469 | `""` | — |
| [SRC-F725E90B2A-L003470](../../tests/test_web_agent.py#L3470) | 3470 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L003471](../../tests/test_web_agent.py#L3471) | 3471 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"لم أعثر على مصدر.\")"` | — |
| [SRC-F725E90B2A-L003472](../../tests/test_web_agent.py#L3472) | 3472 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda _question, answer, _sources: answer)"` | — |
| [SRC-F725E90B2A-L003473](../../tests/test_web_agent.py#L3473) | 3473 | `""` | — |
| [SRC-F725E90B2A-L003474](../../tests/test_web_agent.py#L3474) | 3474 | `"    agent.answer(question, mode=\"auto\")"` | — |
| [SRC-F725E90B2A-L003475](../../tests/test_web_agent.py#L3475) | 3475 | `""` | — |
| [SRC-F725E90B2A-L003476](../../tests/test_web_agent.py#L3476) | 3476 | `"    assert observed_plans"` | — |
| [SRC-F725E90B2A-L003477](../../tests/test_web_agent.py#L3477) | 3477 | `"    assert observed_plans[0][\"queries\"]"` | — |
| [SRC-F725E90B2A-L003478](../../tests/test_web_agent.py#L3478) | 3478 | `"    assert all(not query.startswith(\"ابحث عن\") for query in observed_plans[0][\"queries\"])"` | — |
| [SRC-F725E90B2A-L003479](../../tests/test_web_agent.py#L3479) | 3479 | `"    assert \"الموقع الرسمي لشركة النور\" in observed_plans[0][\"queries\"][0]"` | — |
| [SRC-F725E90B2A-L003480](../../tests/test_web_agent.py#L3480) | 3480 | `"def test_latest_mode_does_not_generate_answer_from_stale_pages(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003481](../../tests/test_web_agent.py#L3481) | 3481 | `"    \"\"\"Current-mode answers must abstain if only old pages survive retrieval.\"\"\""` | — |
| [SRC-F725E90B2A-L003482](../../tests/test_web_agent.py#L3482) | 3482 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003483](../../tests/test_web_agent.py#L3483) | 3483 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L003484](../../tests/test_web_agent.py#L3484) | 3484 | `"        \"queries\": [\"مواعيد عمل مكتب الجوازات العباسية اليوم\"],"` | — |
| [SRC-F725E90B2A-L003485](../../tests/test_web_agent.py#L3485) | 3485 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L003486](../../tests/test_web_agent.py#L3486) | 3486 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003487](../../tests/test_web_agent.py#L3487) | 3487 | `"        \"freshness\": \"current\","` | — |
| [SRC-F725E90B2A-L003488](../../tests/test_web_agent.py#L3488) | 3488 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003489](../../tests/test_web_agent.py#L3489) | 3489 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003490](../../tests/test_web_agent.py#L3490) | 3490 | `"        \"planning_method\": \"fixture\","` | — |
| [SRC-F725E90B2A-L003491](../../tests/test_web_agent.py#L3491) | 3491 | `"        \"coverage_targets\": [],"` | — |
| [SRC-F725E90B2A-L003492](../../tests/test_web_agent.py#L3492) | 3492 | `"    }"` | — |
| [SRC-F725E90B2A-L003493](../../tests/test_web_agent.py#L3493) | 3493 | `"    collection_calls = []"` | — |
| [SRC-F725E90B2A-L003494](../../tests/test_web_agent.py#L3494) | 3494 | `""` | — |
| [SRC-F725E90B2A-L003495](../../tests/test_web_agent.py#L3495) | 3495 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L003496](../../tests/test_web_agent.py#L3496) | 3496 | `"        collection_calls.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L003497](../../tests/test_web_agent.py#L3497) | 3497 | `"        old_page = sample_source(0)"` | — |
| [SRC-F725E90B2A-L003498](../../tests/test_web_agent.py#L3498) | 3498 | `"        old_page.update({"` | — |
| [SRC-F725E90B2A-L003499](../../tests/test_web_agent.py#L3499) | 3499 | `"            \"url\": \"https://moi.gov.eg/passports\","` | — |
| [SRC-F725E90B2A-L003500](../../tests/test_web_agent.py#L3500) | 3500 | `"            \"domain\": \"moi.gov.eg\","` | — |
| [SRC-F725E90B2A-L003501](../../tests/test_web_agent.py#L3501) | 3501 | `"            \"published_at\": \"2024-01-01T10:00:00Z\","` | — |
| [SRC-F725E90B2A-L003502](../../tests/test_web_agent.py#L3502) | 3502 | `"            \"page_fetched\": True,"` | — |
| [SRC-F725E90B2A-L003503](../../tests/test_web_agent.py#L3503) | 3503 | `"            \"page_text\": \"محتوى قديم عن مواعيد العمل\","` | — |
| [SRC-F725E90B2A-L003504](../../tests/test_web_agent.py#L3504) | 3504 | `"        })"` | — |
| [SRC-F725E90B2A-L003505](../../tests/test_web_agent.py#L3505) | 3505 | `"        return [old_page], [], {"` | — |
| [SRC-F725E90B2A-L003506](../../tests/test_web_agent.py#L3506) | 3506 | `"            \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L003507](../../tests/test_web_agent.py#L3507) | 3507 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L003508](../../tests/test_web_agent.py#L3508) | 3508 | `"            \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L003509](../../tests/test_web_agent.py#L3509) | 3509 | `"            \"pages_fetched\": 1,"` | — |
| [SRC-F725E90B2A-L003510](../../tests/test_web_agent.py#L3510) | 3510 | `"            \"providers_used\": [\"fixture\"],"` | — |
| [SRC-F725E90B2A-L003511](../../tests/test_web_agent.py#L3511) | 3511 | `"            \"provider_counts\": {\"fixture\": 1},"` | — |
| [SRC-F725E90B2A-L003512](../../tests/test_web_agent.py#L3512) | 3512 | `"            \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L003513](../../tests/test_web_agent.py#L3513) | 3513 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L003514](../../tests/test_web_agent.py#L3514) | 3514 | `"            \"expansion_queries\": [],"` | — |
| [SRC-F725E90B2A-L003515](../../tests/test_web_agent.py#L3515) | 3515 | `"            \"provider_diagnostics\": [],"` | — |
| [SRC-F725E90B2A-L003516](../../tests/test_web_agent.py#L3516) | 3516 | `"            \"query_results\": [{\"query\": research_plan[\"queries\"][0], \"results\": 1}],"` | — |
| [SRC-F725E90B2A-L003517](../../tests/test_web_agent.py#L3517) | 3517 | `"        }"` | — |
| [SRC-F725E90B2A-L003518](../../tests/test_web_agent.py#L3518) | 3518 | `""` | — |
| [SRC-F725E90B2A-L003519](../../tests/test_web_agent.py#L3519) | 3519 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda *args, **kwargs: dict(plan))"` | — |
| [SRC-F725E90B2A-L003520](../../tests/test_web_agent.py#L3520) | 3520 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L003521](../../tests/test_web_agent.py#L3521) | 3521 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L003522](../../tests/test_web_agent.py#L3522) | 3522 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003523](../../tests/test_web_agent.py#L3523) | 3523 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003524](../../tests/test_web_agent.py#L3524) | 3524 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L003525](../../tests/test_web_agent.py#L3525) | 3525 | `"        lambda *args, **kwargs: pytest.fail(\"Stale pages must not be passed to generation\"),"` | — |
| [SRC-F725E90B2A-L003526](../../tests/test_web_agent.py#L3526) | 3526 | `"    )"` | — |
| [SRC-F725E90B2A-L003527](../../tests/test_web_agent.py#L3527) | 3527 | `""` | — |
| [SRC-F725E90B2A-L003528](../../tests/test_web_agent.py#L3528) | 3528 | `"    result = agent.answer(\"ما مواعيد عمل مكتب الجوازات اليوم؟\", mode=\"latest\")"` | — |
| [SRC-F725E90B2A-L003529](../../tests/test_web_agent.py#L3529) | 3529 | `""` | — |
| [SRC-F725E90B2A-L003530](../../tests/test_web_agent.py#L3530) | 3530 | `"    assert result[\"kind\"] == \"insufficient_evidence\""` | — |
| [SRC-F725E90B2A-L003531](../../tests/test_web_agent.py#L3531) | 3531 | `"    assert len(collection_calls) >= 1"` | — |
| [SRC-F725E90B2A-L003532](../../tests/test_web_agent.py#L3532) | 3532 | `"    guardrails = result[\"search_report\"][\"source_guardrails\"]"` | — |
| [SRC-F725E90B2A-L003533](../../tests/test_web_agent.py#L3533) | 3533 | `"    assert guardrails[\"initial\"][\"rejection_counts\"][\"stale\"] == 1"` | — |
| [SRC-F725E90B2A-L003534](../../tests/test_web_agent.py#L3534) | 3534 | `"    assert guardrails[\"final\"][\"current_evidence_status\"] == \"no_current_eligible_evidence\""` | — |
| [SRC-F725E90B2A-L003535](../../tests/test_web_agent.py#L3535) | 3535 | `"    assert result[\"search_report\"][\"search_outcome\"] == \"attempted_no_usable_sources\""` | — |
| [SRC-F725E90B2A-L003536](../../tests/test_web_agent.py#L3536) | 3536 | `""` | — |
| [SRC-F725E90B2A-L003537](../../tests/test_web_agent.py#L3537) | 3537 | `"def test_official_government_lookup_never_synthesizes_tourism_result(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003538](../../tests/test_web_agent.py#L3538) | 3538 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003539](../../tests/test_web_agent.py#L3539) | 3539 | `"    question = \"ابحث عن الموقع الرسمي لوزارة الاتصالات وتكنولوجيا المعلومات المصرية\""` | — |
| [SRC-F725E90B2A-L003540](../../tests/test_web_agent.py#L3540) | 3540 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L003541](../../tests/test_web_agent.py#L3541) | 3541 | `"        \"queries\": [\"وزارة الاتصالات وتكنولوجيا المعلومات مصر الموقع الرسمي\"],"` | — |
| [SRC-F725E90B2A-L003542](../../tests/test_web_agent.py#L3542) | 3542 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L003543](../../tests/test_web_agent.py#L3543) | 3543 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003544](../../tests/test_web_agent.py#L3544) | 3544 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003545](../../tests/test_web_agent.py#L3545) | 3545 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003546](../../tests/test_web_agent.py#L3546) | 3546 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003547](../../tests/test_web_agent.py#L3547) | 3547 | `"        \"planning_method\": \"fixture\","` | — |
| [SRC-F725E90B2A-L003548](../../tests/test_web_agent.py#L3548) | 3548 | `"    }"` | — |
| [SRC-F725E90B2A-L003549](../../tests/test_web_agent.py#L3549) | 3549 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L003550](../../tests/test_web_agent.py#L3550) | 3550 | `""` | — |
| [SRC-F725E90B2A-L003551](../../tests/test_web_agent.py#L3551) | 3551 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L003552](../../tests/test_web_agent.py#L3552) | 3552 | `"        calls.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L003553](../../tests/test_web_agent.py#L3553) | 3553 | `"        candidate = sample_source(0)"` | — |
| [SRC-F725E90B2A-L003554](../../tests/test_web_agent.py#L3554) | 3554 | `"        candidate.update({"` | — |
| [SRC-F725E90B2A-L003555](../../tests/test_web_agent.py#L3555) | 3555 | `"            \"title\": \"وزارة الاتصالات في مصر ومعلومات سياحية\","` | — |
| [SRC-F725E90B2A-L003556](../../tests/test_web_agent.py#L3556) | 3556 | `"            \"url\": \"https://visitegypt.com/\","` | — |
| [SRC-F725E90B2A-L003557](../../tests/test_web_agent.py#L3557) | 3557 | `"            \"domain\": \"visitegypt.com\","` | — |
| [SRC-F725E90B2A-L003558](../../tests/test_web_agent.py#L3558) | 3558 | `"            \"snippet\": \"معلومات عن الوزارة ضمن دليل سياحي لمصر\","` | — |
| [SRC-F725E90B2A-L003559](../../tests/test_web_agent.py#L3559) | 3559 | `"            \"page_fetched\": True,"` | — |
| [SRC-F725E90B2A-L003560](../../tests/test_web_agent.py#L3560) | 3560 | `"            \"page_text\": \"معلومات سياحية تذكر وزارة الاتصالات\","` | — |
| [SRC-F725E90B2A-L003561](../../tests/test_web_agent.py#L3561) | 3561 | `"            \"queries\": list(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L003562](../../tests/test_web_agent.py#L3562) | 3562 | `"        })"` | — |
| [SRC-F725E90B2A-L003563](../../tests/test_web_agent.py#L3563) | 3563 | `"        return [candidate], [], {"` | — |
| [SRC-F725E90B2A-L003564](../../tests/test_web_agent.py#L3564) | 3564 | `"            \"queries_planned\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L003565](../../tests/test_web_agent.py#L3565) | 3565 | `"            \"queries_attempted\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L003566](../../tests/test_web_agent.py#L3566) | 3566 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L003567](../../tests/test_web_agent.py#L3567) | 3567 | `"            \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L003568](../../tests/test_web_agent.py#L3568) | 3568 | `"            \"pages_fetched\": 1,"` | — |
| [SRC-F725E90B2A-L003569](../../tests/test_web_agent.py#L3569) | 3569 | `"            \"providers_used\": [\"fixture\"],"` | — |
| [SRC-F725E90B2A-L003570](../../tests/test_web_agent.py#L3570) | 3570 | `"            \"provider_counts\": {\"fixture\": 1},"` | — |
| [SRC-F725E90B2A-L003571](../../tests/test_web_agent.py#L3571) | 3571 | `"            \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L003572](../../tests/test_web_agent.py#L3572) | 3572 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L003573](../../tests/test_web_agent.py#L3573) | 3573 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003574](../../tests/test_web_agent.py#L3574) | 3574 | `"            \"planning_method\": \"fixture\","` | — |
| [SRC-F725E90B2A-L003575](../../tests/test_web_agent.py#L3575) | 3575 | `"            \"provider_diagnostics\": [],"` | — |
| [SRC-F725E90B2A-L003576](../../tests/test_web_agent.py#L3576) | 3576 | `"        }"` | — |
| [SRC-F725E90B2A-L003577](../../tests/test_web_agent.py#L3577) | 3577 | `""` | — |
| [SRC-F725E90B2A-L003578](../../tests/test_web_agent.py#L3578) | 3578 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda *args, **kwargs: dict(plan))"` | — |
| [SRC-F725E90B2A-L003579](../../tests/test_web_agent.py#L3579) | 3579 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L003580](../../tests/test_web_agent.py#L3580) | 3580 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L003581](../../tests/test_web_agent.py#L3581) | 3581 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003582](../../tests/test_web_agent.py#L3582) | 3582 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003583](../../tests/test_web_agent.py#L3583) | 3583 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L003584](../../tests/test_web_agent.py#L3584) | 3584 | `"        lambda *args, **kwargs: pytest.fail("` | — |
| [SRC-F725E90B2A-L003585](../../tests/test_web_agent.py#L3585) | 3585 | `"            \"A tourism result must never be passed to answer generation as the official site\""` | — |
| [SRC-F725E90B2A-L003586](../../tests/test_web_agent.py#L3586) | 3586 | `"        ),"` | — |
| [SRC-F725E90B2A-L003587](../../tests/test_web_agent.py#L3587) | 3587 | `"    )"` | — |
| [SRC-F725E90B2A-L003588](../../tests/test_web_agent.py#L3588) | 3588 | `""` | — |
| [SRC-F725E90B2A-L003589](../../tests/test_web_agent.py#L3589) | 3589 | `"    result = agent.answer(question, mode=\"auto\")"` | — |
| [SRC-F725E90B2A-L003590](../../tests/test_web_agent.py#L3590) | 3590 | `""` | — |
| [SRC-F725E90B2A-L003591](../../tests/test_web_agent.py#L3591) | 3591 | `"    assert calls  # initial research, plus bounded repair where applicable"` | — |
| [SRC-F725E90B2A-L003592](../../tests/test_web_agent.py#L3592) | 3592 | `"    assert result[\"kind\"] == \"insufficient_evidence\""` | — |
| [SRC-F725E90B2A-L003593](../../tests/test_web_agent.py#L3593) | 3593 | `"    assert result[\"sources\"] == []"` | — |
| [SRC-F725E90B2A-L003594](../../tests/test_web_agent.py#L3594) | 3594 | `"    guardrails = result[\"search_report\"][\"source_guardrails\"]"` | — |
| [SRC-F725E90B2A-L003595](../../tests/test_web_agent.py#L3595) | 3595 | `"    assert guardrails[\"initial\"][\"official_government_domain_required\"] is True"` | — |
| [SRC-F725E90B2A-L003596](../../tests/test_web_agent.py#L3596) | 3596 | `"    assert guardrails[\"initial\"][\"rejection_counts\"] == {"` | — |
| [SRC-F725E90B2A-L003597](../../tests/test_web_agent.py#L3597) | 3597 | `"        \"not_an_official_government_domain\": 1"` | — |
| [SRC-F725E90B2A-L003598](../../tests/test_web_agent.py#L3598) | 3598 | `"    }"` | — |
| [SRC-F725E90B2A-L003599](../../tests/test_web_agent.py#L3599) | 3599 | `"    assert guardrails[\"final\"][\"accepted_sources\"] == 0"` | — |
| [SRC-F725E90B2A-L003600](../../tests/test_web_agent.py#L3600) | 3600 | `"    assert result[\"search_report\"][\"usable_sources_after_filtering\"] == 0"` | — |
| [SRC-F725E90B2A-L003601](../../tests/test_web_agent.py#L3601) | 3601 | `""` | — |
| [SRC-F725E90B2A-L003602](../../tests/test_web_agent.py#L3602) | 3602 | `"def test_criterion_gap_repair_cannot_reintroduce_non_social_source(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003603](../../tests/test_web_agent.py#L3603) | 3603 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003604](../../tests/test_web_agent.py#L3604) | 3604 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L003605](../../tests/test_web_agent.py#L3605) | 3605 | `"    question = ("` | — |
| [SRC-F725E90B2A-L003606](../../tests/test_web_agent.py#L3606) | 3606 | `"        \"قارن بين خدمتين من حيث السعر والخصوصية والاعتمادية \""` | — |
| [SRC-F725E90B2A-L003607](../../tests/test_web_agent.py#L3607) | 3607 | `"        \"واعرض آراء وتجارب المستخدمين\""` | — |
| [SRC-F725E90B2A-L003608](../../tests/test_web_agent.py#L3608) | 3608 | `"    )"` | — |
| [SRC-F725E90B2A-L003609](../../tests/test_web_agent.py#L3609) | 3609 | `"    initial_sources = ["` | — |
| [SRC-F725E90B2A-L003610](../../tests/test_web_agent.py#L3610) | 3610 | `"        {"` | — |
| [SRC-F725E90B2A-L003611](../../tests/test_web_agent.py#L3611) | 3611 | `"            **sample_source(0),"` | — |
| [SRC-F725E90B2A-L003612](../../tests/test_web_agent.py#L3612) | 3612 | `"            \"url\": \"https://www.reddit.com/r/example/comments/1\","` | — |
| [SRC-F725E90B2A-L003613](../../tests/test_web_agent.py#L3613) | 3613 | `"            \"domain\": \"reddit.com\","` | — |
| [SRC-F725E90B2A-L003614](../../tests/test_web_agent.py#L3614) | 3614 | `"            \"title\": \"مناقشة تجارب المستخدمين للخدمتين\","` | — |
| [SRC-F725E90B2A-L003615](../../tests/test_web_agent.py#L3615) | 3615 | `"            \"snippet\": \"تجارب وآراء مستخدمين حول الخدمتين\","` | — |
| [SRC-F725E90B2A-L003616](../../tests/test_web_agent.py#L3616) | 3616 | `"            \"page_text\": \"تجارب وآراء مستخدمين حول الخدمتين\","` | — |
| [SRC-F725E90B2A-L003617](../../tests/test_web_agent.py#L3617) | 3617 | `"            \"platform\": \"reddit\","` | — |
| [SRC-F725E90B2A-L003618](../../tests/test_web_agent.py#L3618) | 3618 | `"            \"providers\": [\"reddit\"],"` | — |
| [SRC-F725E90B2A-L003619](../../tests/test_web_agent.py#L3619) | 3619 | `"        },"` | — |
| [SRC-F725E90B2A-L003620](../../tests/test_web_agent.py#L3620) | 3620 | `"        {"` | — |
| [SRC-F725E90B2A-L003621](../../tests/test_web_agent.py#L3621) | 3621 | `"            **sample_source(1),"` | — |
| [SRC-F725E90B2A-L003622](../../tests/test_web_agent.py#L3622) | 3622 | `"            \"url\": \"https://www.reddit.com/r/example/comments/2\","` | — |
| [SRC-F725E90B2A-L003623](../../tests/test_web_agent.py#L3623) | 3623 | `"            \"domain\": \"reddit.com\","` | — |
| [SRC-F725E90B2A-L003624](../../tests/test_web_agent.py#L3624) | 3624 | `"            \"title\": \"مناقشة أخرى عن الخدمتين\","` | — |
| [SRC-F725E90B2A-L003625](../../tests/test_web_agent.py#L3625) | 3625 | `"            \"snippet\": \"مناقشة وتجارب مستخدمين حول الخدمتين\","` | — |
| [SRC-F725E90B2A-L003626](../../tests/test_web_agent.py#L3626) | 3626 | `"            \"page_text\": \"مناقشة وتجارب مستخدمين حول الخدمتين\","` | — |
| [SRC-F725E90B2A-L003627](../../tests/test_web_agent.py#L3627) | 3627 | `"            \"platform\": \"reddit\","` | — |
| [SRC-F725E90B2A-L003628](../../tests/test_web_agent.py#L3628) | 3628 | `"            \"providers\": [\"reddit\"],"` | — |
| [SRC-F725E90B2A-L003629](../../tests/test_web_agent.py#L3629) | 3629 | `"        },"` | — |
| [SRC-F725E90B2A-L003630](../../tests/test_web_agent.py#L3630) | 3630 | `"    ]"` | — |
| [SRC-F725E90B2A-L003631](../../tests/test_web_agent.py#L3631) | 3631 | `"    repair_candidate = {"` | — |
| [SRC-F725E90B2A-L003632](../../tests/test_web_agent.py#L3632) | 3632 | `"        **sample_source(2),"` | — |
| [SRC-F725E90B2A-L003633](../../tests/test_web_agent.py#L3633) | 3633 | `"        \"url\": \"https://example.com/unrelated-repair\","` | — |
| [SRC-F725E90B2A-L003634](../../tests/test_web_agent.py#L3634) | 3634 | `"        \"domain\": \"example.com\","` | — |
| [SRC-F725E90B2A-L003635](../../tests/test_web_agent.py#L3635) | 3635 | `"        \"title\": \"معلومات عن الخدمة\","` | — |
| [SRC-F725E90B2A-L003636](../../tests/test_web_agent.py#L3636) | 3636 | `"        \"snippet\": \"معلومات عامة عن الخدمة\","` | — |
| [SRC-F725E90B2A-L003637](../../tests/test_web_agent.py#L3637) | 3637 | `"        \"page_text\": \"معلومات عامة عن الخدمة\","` | — |
| [SRC-F725E90B2A-L003638](../../tests/test_web_agent.py#L3638) | 3638 | `"        \"providers\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L003639](../../tests/test_web_agent.py#L3639) | 3639 | `"    }"` | — |
| [SRC-F725E90B2A-L003640](../../tests/test_web_agent.py#L3640) | 3640 | `"    collect_calls = []"` | — |
| [SRC-F725E90B2A-L003641](../../tests/test_web_agent.py#L3641) | 3641 | `""` | — |
| [SRC-F725E90B2A-L003642](../../tests/test_web_agent.py#L3642) | 3642 | `"    def plan(_question, _history):"` | — |
| [SRC-F725E90B2A-L003643](../../tests/test_web_agent.py#L3643) | 3643 | `"        return {"` | — |
| [SRC-F725E90B2A-L003644](../../tests/test_web_agent.py#L3644) | 3644 | `"            \"queries\": [_question],"` | — |
| [SRC-F725E90B2A-L003645](../../tests/test_web_agent.py#L3645) | 3645 | `"            \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L003646](../../tests/test_web_agent.py#L3646) | 3646 | `"            \"social_focus\": True,"` | — |
| [SRC-F725E90B2A-L003647](../../tests/test_web_agent.py#L3647) | 3647 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003648](../../tests/test_web_agent.py#L3648) | 3648 | `"            \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L003649](../../tests/test_web_agent.py#L3649) | 3649 | `"            \"platforms\": [\"reddit\"],"` | — |
| [SRC-F725E90B2A-L003650](../../tests/test_web_agent.py#L3650) | 3650 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003651](../../tests/test_web_agent.py#L3651) | 3651 | `"        }"` | — |
| [SRC-F725E90B2A-L003652](../../tests/test_web_agent.py#L3652) | 3652 | `""` | — |
| [SRC-F725E90B2A-L003653](../../tests/test_web_agent.py#L3653) | 3653 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L003654](../../tests/test_web_agent.py#L3654) | 3654 | `"        collect_calls.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L003655](../../tests/test_web_agent.py#L3655) | 3655 | `"        if len(collect_calls) == 1:"` | — |
| [SRC-F725E90B2A-L003656](../../tests/test_web_agent.py#L3656) | 3656 | `"            sources = initial_sources"` | — |
| [SRC-F725E90B2A-L003657](../../tests/test_web_agent.py#L3657) | 3657 | `"        else:"` | — |
| [SRC-F725E90B2A-L003658](../../tests/test_web_agent.py#L3658) | 3658 | `"            sources = [repair_candidate]"` | — |
| [SRC-F725E90B2A-L003659](../../tests/test_web_agent.py#L3659) | 3659 | `"        return sources, [], {"` | — |
| [SRC-F725E90B2A-L003660](../../tests/test_web_agent.py#L3660) | 3660 | `"            \"queries_planned\": len(research_plan.get(\"queries\", [])),"` | — |
| [SRC-F725E90B2A-L003661](../../tests/test_web_agent.py#L3661) | 3661 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L003662](../../tests/test_web_agent.py#L3662) | 3662 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L003663](../../tests/test_web_agent.py#L3663) | 3663 | `"            \"unique_sources\": len(sources),"` | — |
| [SRC-F725E90B2A-L003664](../../tests/test_web_agent.py#L3664) | 3664 | `"            \"pages_fetched\": len(sources),"` | — |
| [SRC-F725E90B2A-L003665](../../tests/test_web_agent.py#L3665) | 3665 | `"            \"providers_used\": [\"reddit\"] if len(collect_calls) == 1 else [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L003666](../../tests/test_web_agent.py#L3666) | 3666 | `"            \"provider_counts\": {},"` | — |
| [SRC-F725E90B2A-L003667](../../tests/test_web_agent.py#L3667) | 3667 | `"            \"platform_counts\": {},"` | — |
| [SRC-F725E90B2A-L003668](../../tests/test_web_agent.py#L3668) | 3668 | `"            \"social_direct_results\": len(sources) if len(collect_calls) == 1 else 0,"` | — |
| [SRC-F725E90B2A-L003669](../../tests/test_web_agent.py#L3669) | 3669 | `"            \"depth\": research_plan.get(\"depth\", \"deep\"),"` | — |
| [SRC-F725E90B2A-L003670](../../tests/test_web_agent.py#L3670) | 3670 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003671](../../tests/test_web_agent.py#L3671) | 3671 | `"        }"` | — |
| [SRC-F725E90B2A-L003672](../../tests/test_web_agent.py#L3672) | 3672 | `""` | — |
| [SRC-F725E90B2A-L003673](../../tests/test_web_agent.py#L3673) | 3673 | `"    monkeypatch.setattr(agent, \"_plan_search\", plan)"` | — |
| [SRC-F725E90B2A-L003674](../../tests/test_web_agent.py#L3674) | 3674 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L003675](../../tests/test_web_agent.py#L3675) | 3675 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda _query, _source: True)"` | — |
| [SRC-F725E90B2A-L003676](../../tests/test_web_agent.py#L3676) | 3676 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003677](../../tests/test_web_agent.py#L3677) | 3677 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003678](../../tests/test_web_agent.py#L3678) | 3678 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L003679](../../tests/test_web_agent.py#L3679) | 3679 | `"        lambda *args, **kwargs: ("` | — |
| [SRC-F725E90B2A-L003680](../../tests/test_web_agent.py#L3680) | 3680 | `"            \"السعر مناسب [المصدر 1]. الخصوصية جيدة [المصدر 2]. \""` | — |
| [SRC-F725E90B2A-L003681](../../tests/test_web_agent.py#L3681) | 3681 | `"            \"الاعتمادية مناسبة [المصدر 1].\""` | — |
| [SRC-F725E90B2A-L003682](../../tests/test_web_agent.py#L3682) | 3682 | `"        ),"` | — |
| [SRC-F725E90B2A-L003683](../../tests/test_web_agent.py#L3683) | 3683 | `"    )"` | — |
| [SRC-F725E90B2A-L003684](../../tests/test_web_agent.py#L3684) | 3684 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003685](../../tests/test_web_agent.py#L3685) | 3685 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003686](../../tests/test_web_agent.py#L3686) | 3686 | `"        \"_review_answer\","` | — |
| [SRC-F725E90B2A-L003687](../../tests/test_web_agent.py#L3687) | 3687 | `"        lambda _question, answer, _sources: answer,"` | — |
| [SRC-F725E90B2A-L003688](../../tests/test_web_agent.py#L3688) | 3688 | `"    )"` | — |
| [SRC-F725E90B2A-L003689](../../tests/test_web_agent.py#L3689) | 3689 | `""` | — |
| [SRC-F725E90B2A-L003690](../../tests/test_web_agent.py#L3690) | 3690 | `"    result = agent.answer(question, mode=\"social\")"` | — |
| [SRC-F725E90B2A-L003691](../../tests/test_web_agent.py#L3691) | 3691 | `"    report = result[\"search_report\"]"` | — |
| [SRC-F725E90B2A-L003692](../../tests/test_web_agent.py#L3692) | 3692 | `"    repair_guardrails = report[\"source_guardrails\"][\"criterion_gap_repair\"]"` | — |
| [SRC-F725E90B2A-L003693](../../tests/test_web_agent.py#L3693) | 3693 | `""` | — |
| [SRC-F725E90B2A-L003694](../../tests/test_web_agent.py#L3694) | 3694 | `"    assert len(collect_calls) >= 2"` | — |
| [SRC-F725E90B2A-L003695](../../tests/test_web_agent.py#L3695) | 3695 | `"    assert repair_guardrails[\"rejected_sources\"] >= 1"` | — |
| [SRC-F725E90B2A-L003696](../../tests/test_web_agent.py#L3696) | 3696 | `"    assert repair_guardrails[\"rejection_counts\"][\"not_a_social_platform_source\"] >= 1"` | — |
| [SRC-F725E90B2A-L003697](../../tests/test_web_agent.py#L3697) | 3697 | `"    assert all(\"reddit.com\" in source[\"url\"] for source in result[\"sources\"])"` | — |
| [SRC-F725E90B2A-L003698](../../tests/test_web_agent.py#L3698) | 3698 | `"    assert \"https://example.com/unrelated-repair\" not in {"` | — |
| [SRC-F725E90B2A-L003699](../../tests/test_web_agent.py#L3699) | 3699 | `"        source[\"url\"] for source in result[\"sources\"]"` | — |
| [SRC-F725E90B2A-L003700](../../tests/test_web_agent.py#L3700) | 3700 | `"    }"` | — |
| [SRC-F725E90B2A-L003701](../../tests/test_web_agent.py#L3701) | 3701 | `""` | — |
| [SRC-F725E90B2A-L003702](../../tests/test_web_agent.py#L3702) | 3702 | `"def test_local_answer_exposes_task_spec_without_claiming_search(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003703](../../tests/test_web_agent.py#L3703) | 3703 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003704](../../tests/test_web_agent.py#L3704) | 3704 | `"    result = agent.answer(\"أهلا\")"` | — |
| [SRC-F725E90B2A-L003705](../../tests/test_web_agent.py#L3705) | 3705 | `""` | — |
| [SRC-F725E90B2A-L003706](../../tests/test_web_agent.py#L3706) | 3706 | `"    task_understanding = result[\"task_understanding\"]"` | — |
| [SRC-F725E90B2A-L003707](../../tests/test_web_agent.py#L3707) | 3707 | `"    assert task_understanding[\"task_spec\"][\"schema\"] == \"omarai.task_spec.v1\""` | — |
| [SRC-F725E90B2A-L003708](../../tests/test_web_agent.py#L3708) | 3708 | `"    assert task_understanding[\"tool_execution\"][\"search_outcome\"] == \"not_assessed\""` | — |
| [SRC-F725E90B2A-L003709](../../tests/test_web_agent.py#L3709) | 3709 | `"    assert task_understanding[\"tool_execution\"][\"required_tools\"] == []"` | — |
| [SRC-F725E90B2A-L003710](../../tests/test_web_agent.py#L3710) | 3710 | `"    assert all("` | — |
| [SRC-F725E90B2A-L003711](../../tests/test_web_agent.py#L3711) | 3711 | `"        row[\"status\"] == \"not_required\""` | — |
| [SRC-F725E90B2A-L003712](../../tests/test_web_agent.py#L3712) | 3712 | `"        for row in task_understanding[\"tool_execution\"][\"tool_status_matrix\"]"` | — |
| [SRC-F725E90B2A-L003713](../../tests/test_web_agent.py#L3713) | 3713 | `"    )"` | — |
| [SRC-F725E90B2A-L003714](../../tests/test_web_agent.py#L3714) | 3714 | `"    assert task_understanding[\"actual_queries\"] == []"` | — |
| [SRC-F725E90B2A-L003715](../../tests/test_web_agent.py#L3715) | 3715 | `"    assert task_understanding[\"query_strategy_matrix\"] == []"` | — |
| [SRC-F725E90B2A-L003716](../../tests/test_web_agent.py#L3716) | 3716 | `"    assert task_understanding[\"search_was_attempted\"] is False"` | — |
| [SRC-F725E90B2A-L003717](../../tests/test_web_agent.py#L3717) | 3717 | `""` | — |
| [SRC-F725E90B2A-L003718](../../tests/test_web_agent.py#L3718) | 3718 | `"def test_official_site_without_target_clarifies_before_planning_or_search(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003719](../../tests/test_web_agent.py#L3719) | 3719 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003720](../../tests/test_web_agent.py#L3720) | 3720 | `""` | — |
| [SRC-F725E90B2A-L003721](../../tests/test_web_agent.py#L3721) | 3721 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003722](../../tests/test_web_agent.py#L3722) | 3722 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003723](../../tests/test_web_agent.py#L3723) | 3723 | `"        \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003724](../../tests/test_web_agent.py#L3724) | 3724 | `"        lambda *args, **kwargs: pytest.fail(\"Missing official-site target must be clarified before planning\"),"` | — |
| [SRC-F725E90B2A-L003725](../../tests/test_web_agent.py#L3725) | 3725 | `"    )"` | — |
| [SRC-F725E90B2A-L003726](../../tests/test_web_agent.py#L3726) | 3726 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003727](../../tests/test_web_agent.py#L3727) | 3727 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003728](../../tests/test_web_agent.py#L3728) | 3728 | `"        \"_collect_research\","` | — |
| [SRC-F725E90B2A-L003729](../../tests/test_web_agent.py#L3729) | 3729 | `"        lambda *args, **kwargs: pytest.fail(\"Missing official-site target must not invoke search\"),"` | — |
| [SRC-F725E90B2A-L003730](../../tests/test_web_agent.py#L3730) | 3730 | `"    )"` | — |
| [SRC-F725E90B2A-L003731](../../tests/test_web_agent.py#L3731) | 3731 | `""` | — |
| [SRC-F725E90B2A-L003732](../../tests/test_web_agent.py#L3732) | 3732 | `"    result = agent.answer(\"هات الموقع الرسمي\")"` | — |
| [SRC-F725E90B2A-L003733](../../tests/test_web_agent.py#L3733) | 3733 | `""` | — |
| [SRC-F725E90B2A-L003734](../../tests/test_web_agent.py#L3734) | 3734 | `"    assert result[\"intent_route\"] == \"CLARIFY\""` | — |
| [SRC-F725E90B2A-L003735](../../tests/test_web_agent.py#L3735) | 3735 | `"    assert result[\"kind\"] == \"clarification_needed\""` | — |
| [SRC-F725E90B2A-L003736](../../tests/test_web_agent.py#L3736) | 3736 | `"    assert \"اسم الجهة أو الشركة\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L003737](../../tests/test_web_agent.py#L3737) | 3737 | `"    assert result[\"search_attempted\"] is False"` | — |
| [SRC-F725E90B2A-L003738](../../tests/test_web_agent.py#L3738) | 3738 | `"    assert \"official_destination_target_entity\" in result[\"task_understanding\"][\"task_spec\"][\"missing_required_inputs\"]"` | — |
| [SRC-F725E90B2A-L003739](../../tests/test_web_agent.py#L3739) | 3739 | `""` | — |
| [SRC-F725E90B2A-L003740](../../tests/test_web_agent.py#L3740) | 3740 | `"def test_summary_without_source_clarifies_before_search(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003741](../../tests/test_web_agent.py#L3741) | 3741 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003742](../../tests/test_web_agent.py#L3742) | 3742 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003743](../../tests/test_web_agent.py#L3743) | 3743 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003744](../../tests/test_web_agent.py#L3744) | 3744 | `"        \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003745](../../tests/test_web_agent.py#L3745) | 3745 | `"        lambda *args, **kwargs: pytest.fail(\"Missing summary source must be clarified before planning\"),"` | — |
| [SRC-F725E90B2A-L003746](../../tests/test_web_agent.py#L3746) | 3746 | `"    )"` | — |
| [SRC-F725E90B2A-L003747](../../tests/test_web_agent.py#L3747) | 3747 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003748](../../tests/test_web_agent.py#L3748) | 3748 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003749](../../tests/test_web_agent.py#L3749) | 3749 | `"        \"_collect_research\","` | — |
| [SRC-F725E90B2A-L003750](../../tests/test_web_agent.py#L3750) | 3750 | `"        lambda *args, **kwargs: pytest.fail(\"Missing summary source must not invoke search\"),"` | — |
| [SRC-F725E90B2A-L003751](../../tests/test_web_agent.py#L3751) | 3751 | `"    )"` | — |
| [SRC-F725E90B2A-L003752](../../tests/test_web_agent.py#L3752) | 3752 | `""` | — |
| [SRC-F725E90B2A-L003753](../../tests/test_web_agent.py#L3753) | 3753 | `"    result = agent.answer(\"لخص\")"` | — |
| [SRC-F725E90B2A-L003754](../../tests/test_web_agent.py#L3754) | 3754 | `""` | — |
| [SRC-F725E90B2A-L003755](../../tests/test_web_agent.py#L3755) | 3755 | `"    assert result[\"intent_route\"] == \"CLARIFY\""` | — |
| [SRC-F725E90B2A-L003756](../../tests/test_web_agent.py#L3756) | 3756 | `"    assert \"أرسل النص\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L003757](../../tests/test_web_agent.py#L3757) | 3757 | `"    assert result[\"search_attempted\"] is False"` | — |
| [SRC-F725E90B2A-L003758](../../tests/test_web_agent.py#L3758) | 3758 | `"    assert \"summary_source_url_or_pasted_text\" in result[\"task_understanding\"][\"task_spec\"][\"missing_required_inputs\"]"` | — |
| [SRC-F725E90B2A-L003759](../../tests/test_web_agent.py#L3759) | 3759 | `""` | — |
| [SRC-F725E90B2A-L003760](../../tests/test_web_agent.py#L3760) | 3760 | `"def test_task_spec_controls_generation_context_without_becoming_evidence(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003761](../../tests/test_web_agent.py#L3761) | 3761 | `"    from agents.task_understanding import build_query_strategy_matrix, build_task_spec"` | — |
| [SRC-F725E90B2A-L003762](../../tests/test_web_agent.py#L3762) | 3762 | `""` | — |
| [SRC-F725E90B2A-L003763](../../tests/test_web_agent.py#L3763) | 3763 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003764](../../tests/test_web_agent.py#L3764) | 3764 | `"    captured = {}"` | — |
| [SRC-F725E90B2A-L003765](../../tests/test_web_agent.py#L3765) | 3765 | `""` | — |
| [SRC-F725E90B2A-L003766](../../tests/test_web_agent.py#L3766) | 3766 | `"    question = ("` | — |
| [SRC-F725E90B2A-L003767](../../tests/test_web_agent.py#L3767) | 3767 | `"        \"قارن السيارات الكهربائية في مصر من حيث السعر والضمان، \""` | — |
| [SRC-F725E90B2A-L003768](../../tests/test_web_agent.py#L3768) | 3768 | `"        \"اشرح ببساطة مع أمثلة وروابط مباشرة\""` | — |
| [SRC-F725E90B2A-L003769](../../tests/test_web_agent.py#L3769) | 3769 | `"    )"` | — |
| [SRC-F725E90B2A-L003770](../../tests/test_web_agent.py#L3770) | 3770 | `"    task_spec = build_task_spec("` | — |
| [SRC-F725E90B2A-L003771](../../tests/test_web_agent.py#L3771) | 3771 | `"        question,"` | — |
| [SRC-F725E90B2A-L003772](../../tests/test_web_agent.py#L3772) | 3772 | `"        mode=\"deep\","` | — |
| [SRC-F725E90B2A-L003773](../../tests/test_web_agent.py#L3773) | 3773 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-F725E90B2A-L003774](../../tests/test_web_agent.py#L3774) | 3774 | `"    )"` | — |
| [SRC-F725E90B2A-L003775](../../tests/test_web_agent.py#L3775) | 3775 | `"    initial_queries = [compact_search_query(question)]"` | — |
| [SRC-F725E90B2A-L003776](../../tests/test_web_agent.py#L3776) | 3776 | `"    matrix = build_query_strategy_matrix("` | — |
| [SRC-F725E90B2A-L003777](../../tests/test_web_agent.py#L3777) | 3777 | `"        question,"` | — |
| [SRC-F725E90B2A-L003778](../../tests/test_web_agent.py#L3778) | 3778 | `"        task_spec,"` | — |
| [SRC-F725E90B2A-L003779](../../tests/test_web_agent.py#L3779) | 3779 | `"        initial_queries,"` | — |
| [SRC-F725E90B2A-L003780](../../tests/test_web_agent.py#L3780) | 3780 | `"        limit=4,"` | — |
| [SRC-F725E90B2A-L003781](../../tests/test_web_agent.py#L3781) | 3781 | `"        compact_fn=compact_search_query,"` | — |
| [SRC-F725E90B2A-L003782](../../tests/test_web_agent.py#L3782) | 3782 | `"    )"` | — |
| [SRC-F725E90B2A-L003783](../../tests/test_web_agent.py#L3783) | 3783 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L003784](../../tests/test_web_agent.py#L3784) | 3784 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L003785](../../tests/test_web_agent.py#L3785) | 3785 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003786](../../tests/test_web_agent.py#L3786) | 3786 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003787](../../tests/test_web_agent.py#L3787) | 3787 | `"        \"queries\": [row[\"query\"] for row in matrix],"` | — |
| [SRC-F725E90B2A-L003788](../../tests/test_web_agent.py#L3788) | 3788 | `"        \"dialogue_context\": {},"` | — |
| [SRC-F725E90B2A-L003789](../../tests/test_web_agent.py#L3789) | 3789 | `"        \"intent_route\": \"WEB_DEEP\","` | — |
| [SRC-F725E90B2A-L003790](../../tests/test_web_agent.py#L3790) | 3790 | `"        \"task_spec\": task_spec,"` | — |
| [SRC-F725E90B2A-L003791](../../tests/test_web_agent.py#L3791) | 3791 | `"        \"query_strategy_matrix\": matrix,"` | — |
| [SRC-F725E90B2A-L003792](../../tests/test_web_agent.py#L3792) | 3792 | `"    }"` | — |
| [SRC-F725E90B2A-L003793](../../tests/test_web_agent.py#L3793) | 3793 | `""` | — |
| [SRC-F725E90B2A-L003794](../../tests/test_web_agent.py#L3794) | 3794 | `"    def fake_completion(messages, **kwargs):"` | — |
| [SRC-F725E90B2A-L003795](../../tests/test_web_agent.py#L3795) | 3795 | `"        captured[\"messages\"] = messages"` | — |
| [SRC-F725E90B2A-L003796](../../tests/test_web_agent.py#L3796) | 3796 | `"        captured[\"kwargs\"] = kwargs"` | — |
| [SRC-F725E90B2A-L003797](../../tests/test_web_agent.py#L3797) | 3797 | `"        return \"إجابة اختبارية مرتبطة بالأدلة.\""` | — |
| [SRC-F725E90B2A-L003798](../../tests/test_web_agent.py#L3798) | 3798 | `""` | — |
| [SRC-F725E90B2A-L003799](../../tests/test_web_agent.py#L3799) | 3799 | `"    monkeypatch.setattr(agent, \"_request_completion\", fake_completion)"` | — |
| [SRC-F725E90B2A-L003800](../../tests/test_web_agent.py#L3800) | 3800 | `""` | — |
| [SRC-F725E90B2A-L003801](../../tests/test_web_agent.py#L3801) | 3801 | `"    answer = agent._generate("` | — |
| [SRC-F725E90B2A-L003802](../../tests/test_web_agent.py#L3802) | 3802 | `"        question,"` | — |
| [SRC-F725E90B2A-L003803](../../tests/test_web_agent.py#L3803) | 3803 | `"        [],"` | — |
| [SRC-F725E90B2A-L003804](../../tests/test_web_agent.py#L3804) | 3804 | `"        [sample_source(0)],"` | — |
| [SRC-F725E90B2A-L003805](../../tests/test_web_agent.py#L3805) | 3805 | `"        None,"` | — |
| [SRC-F725E90B2A-L003806](../../tests/test_web_agent.py#L3806) | 3806 | `"        research_plan=plan,"` | — |
| [SRC-F725E90B2A-L003807](../../tests/test_web_agent.py#L3807) | 3807 | `"        search_report={"` | — |
| [SRC-F725E90B2A-L003808](../../tests/test_web_agent.py#L3808) | 3808 | `"            \"queries_planned\": len(plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L003809](../../tests/test_web_agent.py#L3809) | 3809 | `"            \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L003810](../../tests/test_web_agent.py#L3810) | 3810 | `"            \"pages_fetched\": 1,"` | — |
| [SRC-F725E90B2A-L003811](../../tests/test_web_agent.py#L3811) | 3811 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L003812](../../tests/test_web_agent.py#L3812) | 3812 | `"        },"` | — |
| [SRC-F725E90B2A-L003813](../../tests/test_web_agent.py#L3813) | 3813 | `"    )"` | — |
| [SRC-F725E90B2A-L003814](../../tests/test_web_agent.py#L3814) | 3814 | `""` | — |
| [SRC-F725E90B2A-L003815](../../tests/test_web_agent.py#L3815) | 3815 | `"    prompt = \"\\n\".join("` | — |
| [SRC-F725E90B2A-L003816](../../tests/test_web_agent.py#L3816) | 3816 | `"        message.get(\"content\", \"\")"` | — |
| [SRC-F725E90B2A-L003817](../../tests/test_web_agent.py#L3817) | 3817 | `"        for message in captured[\"messages\"]"` | — |
| [SRC-F725E90B2A-L003818](../../tests/test_web_agent.py#L3818) | 3818 | `"        if isinstance(message, dict)"` | — |
| [SRC-F725E90B2A-L003819](../../tests/test_web_agent.py#L3819) | 3819 | `"    )"` | — |
| [SRC-F725E90B2A-L003820](../../tests/test_web_agent.py#L3820) | 3820 | `"    assert answer == \"إجابة اختبارية مرتبطة بالأدلة.\""` | — |
| [SRC-F725E90B2A-L003821](../../tests/test_web_agent.py#L3821) | 3821 | `"    assert \"task_planning_context\" in prompt"` | — |
| [SRC-F725E90B2A-L003822](../../tests/test_web_agent.py#L3822) | 3822 | `"    assert \"explicit_aspects\" in prompt"` | — |
| [SRC-F725E90B2A-L003823](../../tests/test_web_agent.py#L3823) | 3823 | `"    assert \"output_preferences\" in prompt"` | — |
| [SRC-F725E90B2A-L003824](../../tests/test_web_agent.py#L3824) | 3824 | `"    assert \"beginner_friendly_requested\" in prompt"` | — |
| [SRC-F725E90B2A-L003825](../../tests/test_web_agent.py#L3825) | 3825 | `"    assert \"reasoning_guidance\" in prompt"` | — |
| [SRC-F725E90B2A-L003826](../../tests/test_web_agent.py#L3826) | 3826 | `"    assert \"decision_matrix\" in prompt"` | — |
| [SRC-F725E90B2A-L003827](../../tests/test_web_agent.py#L3827) | 3827 | `"    assert \"قسّم المقارنة إلى كل معيار صريح\" in prompt"` | — |
| [SRC-F725E90B2A-L003828](../../tests/test_web_agent.py#L3828) | 3828 | `"    assert \"وحّد العملة والوحدات\" in prompt"` | — |
| [SRC-F725E90B2A-L003829](../../tests/test_web_agent.py#L3829) | 3829 | `"    assert \"query_strategy_matrix\" in prompt"` | — |
| [SRC-F725E90B2A-L003830](../../tests/test_web_agent.py#L3830) | 3830 | `"    assert \"الأولوية لكلام المستخدم الحالي\" in prompt"` | — |
| [SRC-F725E90B2A-L003831](../../tests/test_web_agent.py#L3831) | 3831 | `"    assert \"الاستعلامات المخططة فقط\" in prompt"` | — |
| [SRC-F725E90B2A-L003832](../../tests/test_web_agent.py#L3832) | 3832 | `""` | — |
| [SRC-F725E90B2A-L003833](../../tests/test_web_agent.py#L3833) | 3833 | `"def test_bilingual_relevance_handles_arabic_attached_clitics_without_lowering_floor():"` | — |
| [SRC-F725E90B2A-L003834](../../tests/test_web_agent.py#L3834) | 3834 | `"    query = \"أهم استخدامات الذكاء الاصطناعي للشركات الصغيرة؟\""` | — |
| [SRC-F725E90B2A-L003835](../../tests/test_web_agent.py#L3835) | 3835 | `"    evidence = \"AI use cases for small businesses\""` | — |
| [SRC-F725E90B2A-L003836](../../tests/test_web_agent.py#L3836) | 3836 | `"    assert _minimum_relevance_ratio(query) == 0.20"` | — |
| [SRC-F725E90B2A-L003837](../../tests/test_web_agent.py#L3837) | 3837 | `"    assert _relevance_ratio(query, evidence) >= 0.80"` | — |
| [SRC-F725E90B2A-L003838](../../tests/test_web_agent.py#L3838) | 3838 | `""` | — |
| [SRC-F725E90B2A-L003839](../../tests/test_web_agent.py#L3839) | 3839 | `"def test_search_evidence_matching_keeps_distinct_concepts_as_the_ratio_denominator():"` | — |
| [SRC-F725E90B2A-L003840](../../tests/test_web_agent.py#L3840) | 3840 | `"    query = \"استخدامات الذكاء الاصطناعي للشركات الصغيرة\""` | — |
| [SRC-F725E90B2A-L003841](../../tests/test_web_agent.py#L3841) | 3841 | `"    on_topic = \"AI use cases for small businesses\""` | — |
| [SRC-F725E90B2A-L003842](../../tests/test_web_agent.py#L3842) | 3842 | `"    weak = \"AI tools for personal photo editing\""` | — |
| [SRC-F725E90B2A-L003843](../../tests/test_web_agent.py#L3843) | 3843 | `"    assert _relevance_ratio(query, on_topic) > _relevance_ratio(query, weak)"` | — |
| [SRC-F725E90B2A-L003844](../../tests/test_web_agent.py#L3844) | 3844 | `"    assert _relevance_ratio(query, weak) < _minimum_relevance_ratio(query)"` | — |
| [SRC-F725E90B2A-L003845](../../tests/test_web_agent.py#L3845) | 3845 | `""` | — |
| [SRC-F725E90B2A-L003846](../../tests/test_web_agent.py#L3846) | 3846 | `"def test_bilingual_relevance_matches_english_queries_to_arabic_source_text():"` | — |
| [SRC-F725E90B2A-L003847](../../tests/test_web_agent.py#L3847) | 3847 | `"    query = \"AI use cases for small businesses in Egypt\""` | — |
| [SRC-F725E90B2A-L003848](../../tests/test_web_agent.py#L3848) | 3848 | `"    evidence = \"استخدامات الذكاء الاصطناعي للشركات الصغيرة في مصر\""` | — |
| [SRC-F725E90B2A-L003849](../../tests/test_web_agent.py#L3849) | 3849 | `"    assert _relevance_ratio(query, evidence) >= 0.80"` | — |
| [SRC-F725E90B2A-L003850](../../tests/test_web_agent.py#L3850) | 3850 | `""` | — |
| [SRC-F725E90B2A-L003851](../../tests/test_web_agent.py#L3851) | 3851 | `""` | — |
| [SRC-F725E90B2A-L003852](../../tests/test_web_agent.py#L3852) | 3852 | `"def test_completion_diagnostics_failure_does_not_break_answer(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003853](../../tests/test_web_agent.py#L3853) | 3853 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003854](../../tests/test_web_agent.py#L3854) | 3854 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L003855](../../tests/test_web_agent.py#L3855) | 3855 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003856](../../tests/test_web_agent.py#L3856) | 3856 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003857](../../tests/test_web_agent.py#L3857) | 3857 | `"        \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003858](../../tests/test_web_agent.py#L3858) | 3858 | `"        lambda question, history: {"` | — |
| [SRC-F725E90B2A-L003859](../../tests/test_web_agent.py#L3859) | 3859 | `"            \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L003860](../../tests/test_web_agent.py#L3860) | 3860 | `"            \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003861](../../tests/test_web_agent.py#L3861) | 3861 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003862](../../tests/test_web_agent.py#L3862) | 3862 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003863](../../tests/test_web_agent.py#L3863) | 3863 | `"            \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003864](../../tests/test_web_agent.py#L3864) | 3864 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003865](../../tests/test_web_agent.py#L3865) | 3865 | `"            \"coverage_targets\": [],"` | — |
| [SRC-F725E90B2A-L003866](../../tests/test_web_agent.py#L3866) | 3866 | `"        },"` | — |
| [SRC-F725E90B2A-L003867](../../tests/test_web_agent.py#L3867) | 3867 | `"    )"` | — |
| [SRC-F725E90B2A-L003868](../../tests/test_web_agent.py#L3868) | 3868 | `"    monkeypatch.setattr(agent, \"_collect_research\", lambda plan: ("` | — |
| [SRC-F725E90B2A-L003869](../../tests/test_web_agent.py#L3869) | 3869 | `"        [sample_source(0), sample_source(1)], [], {"` | — |
| [SRC-F725E90B2A-L003870](../../tests/test_web_agent.py#L3870) | 3870 | `"            \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L003871](../../tests/test_web_agent.py#L3871) | 3871 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L003872](../../tests/test_web_agent.py#L3872) | 3872 | `"            \"query_results\": [{\"query\": plan[\"queries\"][0], \"results\": 2}],"` | — |
| [SRC-F725E90B2A-L003873](../../tests/test_web_agent.py#L3873) | 3873 | `"            \"unique_sources\": 2,"` | — |
| [SRC-F725E90B2A-L003874](../../tests/test_web_agent.py#L3874) | 3874 | `"            \"pages_fetched\": 2,"` | — |
| [SRC-F725E90B2A-L003875](../../tests/test_web_agent.py#L3875) | 3875 | `"            \"providers_used\": [\"test\"],"` | — |
| [SRC-F725E90B2A-L003876](../../tests/test_web_agent.py#L3876) | 3876 | `"            \"provider_diagnostics\": [],"` | — |
| [SRC-F725E90B2A-L003877](../../tests/test_web_agent.py#L3877) | 3877 | `"        }"` | — |
| [SRC-F725E90B2A-L003878](../../tests/test_web_agent.py#L3878) | 3878 | `"    ))"` | — |
| [SRC-F725E90B2A-L003879](../../tests/test_web_agent.py#L3879) | 3879 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L003880](../../tests/test_web_agent.py#L3880) | 3880 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L003881](../../tests/test_web_agent.py#L3881) | 3881 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"إجابة اختبارية [المصدر 1].\")"` | — |
| [SRC-F725E90B2A-L003882](../../tests/test_web_agent.py#L3882) | 3882 | `""` | — |
| [SRC-F725E90B2A-L003883](../../tests/test_web_agent.py#L3883) | 3883 | `"    def fail_diagnostics(_result):"` | — |
| [SRC-F725E90B2A-L003884](../../tests/test_web_agent.py#L3884) | 3884 | `"        raise RuntimeError(\"diagnostics are optional\")"` | — |
| [SRC-F725E90B2A-L003885](../../tests/test_web_agent.py#L3885) | 3885 | `""` | — |
| [SRC-F725E90B2A-L003886](../../tests/test_web_agent.py#L3886) | 3886 | `"    monkeypatch.setattr(\"agents.web_agent.build_research_completion\", fail_diagnostics)"` | — |
| [SRC-F725E90B2A-L003887](../../tests/test_web_agent.py#L3887) | 3887 | `"    result = agent.answer(\"قارن هذه التقنية\")"` | — |
| [SRC-F725E90B2A-L003888](../../tests/test_web_agent.py#L3888) | 3888 | `"    assert result[\"answer\"] == \"إجابة اختبارية [المصدر 1].\""` | — |
| [SRC-F725E90B2A-L003889](../../tests/test_web_agent.py#L3889) | 3889 | `"    assert result[\"research_completion\"][\"status\"] == \"diagnostics_not_computed\""` | — |
| [SRC-F725E90B2A-L003890](../../tests/test_web_agent.py#L3890) | 3890 | `"    assert any(\"لا يُعد ذلك دليلًا على اكتمال البحث\" in warning for warning in result[\"warnings\"])"` | — |
## اختبارات

### FILE-8C13B81AB4 — [tests/test_web_agent_nlu_integration.py](../../tests/test_web_agent_nlu_integration.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-8C13B81AB4-L000001](../../tests/test_web_agent_nlu_integration.py#L1) | 1 | `"\"\"\"Integration regressions for budgeted academic fallback and compound facets.\"\"\""` | — |
| [SRC-8C13B81AB4-L000002](../../tests/test_web_agent_nlu_integration.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-8C13B81AB4-L000003](../../tests/test_web_agent_nlu_integration.py#L3) | 3 | `""` | — |
| [SRC-8C13B81AB4-L000004](../../tests/test_web_agent_nlu_integration.py#L4) | 4 | `"import pytest"` | — |
| [SRC-8C13B81AB4-L000005](../../tests/test_web_agent_nlu_integration.py#L5) | 5 | `""` | — |
| [SRC-8C13B81AB4-L000006](../../tests/test_web_agent_nlu_integration.py#L6) | 6 | `"import agents.web_agent as web_module"` | — |
| [SRC-8C13B81AB4-L000007](../../tests/test_web_agent_nlu_integration.py#L7) | 7 | `"from agents.web_agent import WebAgent"` | — |
| [SRC-8C13B81AB4-L000008](../../tests/test_web_agent_nlu_integration.py#L8) | 8 | `""` | — |
| [SRC-8C13B81AB4-L000009](../../tests/test_web_agent_nlu_integration.py#L9) | 9 | `""` | — |
| [SRC-8C13B81AB4-L000010](../../tests/test_web_agent_nlu_integration.py#L10) | 10 | `"def _academic_result(provider: str, query: str) -> dict:"` | — |
| [SRC-8C13B81AB4-L000011](../../tests/test_web_agent_nlu_integration.py#L11) | 11 | `"    urls = {"` | — |
| [SRC-8C13B81AB4-L000012](../../tests/test_web_agent_nlu_integration.py#L12) | 12 | `"        \"openalex\": \"https://openalex.org/W123\","` | — |
| [SRC-8C13B81AB4-L000013](../../tests/test_web_agent_nlu_integration.py#L13) | 13 | `"        \"arxiv\": \"https://arxiv.org/abs/2401.00001\","` | — |
| [SRC-8C13B81AB4-L000014](../../tests/test_web_agent_nlu_integration.py#L14) | 14 | `"        \"crossref\": \"https://api.crossref.org/works/10.1000/example\","` | — |
| [SRC-8C13B81AB4-L000015](../../tests/test_web_agent_nlu_integration.py#L15) | 15 | `"    }"` | — |
| [SRC-8C13B81AB4-L000016](../../tests/test_web_agent_nlu_integration.py#L16) | 16 | `"    return {"` | — |
| [SRC-8C13B81AB4-L000017](../../tests/test_web_agent_nlu_integration.py#L17) | 17 | `"        \"title\": \"Peer reviewed research on lithium battery degradation\","` | — |
| [SRC-8C13B81AB4-L000018](../../tests/test_web_agent_nlu_integration.py#L18) | 18 | `"        \"url\": urls[provider],"` | — |
| [SRC-8C13B81AB4-L000019](../../tests/test_web_agent_nlu_integration.py#L19) | 19 | `"        \"snippet\": \"Peer reviewed research on lithium battery degradation study.\","` | — |
| [SRC-8C13B81AB4-L000020](../../tests/test_web_agent_nlu_integration.py#L20) | 20 | `"        \"page_fetched\": False,"` | — |
| [SRC-8C13B81AB4-L000021](../../tests/test_web_agent_nlu_integration.py#L21) | 21 | `"        \"provider\": provider,"` | — |
| [SRC-8C13B81AB4-L000022](../../tests/test_web_agent_nlu_integration.py#L22) | 22 | `"        \"provider_rank\": 1,"` | — |
| [SRC-8C13B81AB4-L000023](../../tests/test_web_agent_nlu_integration.py#L23) | 23 | `"        \"search_query\": query,"` | — |
| [SRC-8C13B81AB4-L000024](../../tests/test_web_agent_nlu_integration.py#L24) | 24 | `"        \"published_at\": \"2025\","` | — |
| [SRC-8C13B81AB4-L000025](../../tests/test_web_agent_nlu_integration.py#L25) | 25 | `"        \"source_class\": \"academic\","` | — |
| [SRC-8C13B81AB4-L000026](../../tests/test_web_agent_nlu_integration.py#L26) | 26 | `"    }"` | — |
| [SRC-8C13B81AB4-L000027](../../tests/test_web_agent_nlu_integration.py#L27) | 27 | `""` | — |
| [SRC-8C13B81AB4-L000028](../../tests/test_web_agent_nlu_integration.py#L28) | 28 | `""` | — |
| [SRC-8C13B81AB4-L000029](../../tests/test_web_agent_nlu_integration.py#L29) | 29 | `"def test_sparse_academic_search_uses_budgeted_safe_connectors(monkeypatch) -> None:"` | — |
| [SRC-8C13B81AB4-L000030](../../tests/test_web_agent_nlu_integration.py#L30) | 30 | `"    agent = WebAgent()"` | — |
| [SRC-8C13B81AB4-L000031](../../tests/test_web_agent_nlu_integration.py#L31) | 31 | `"    agent._request_budget = None"` | — |
| [SRC-8C13B81AB4-L000032](../../tests/test_web_agent_nlu_integration.py#L32) | 32 | `"    for key in (\"DEEPSEEK_SEARCH_API_KEY\", \"BRAVE_SEARCH_API_KEY\", \"TAVILY_API_KEY\"):"` | — |
| [SRC-8C13B81AB4-L000033](../../tests/test_web_agent_nlu_integration.py#L33) | 33 | `"        monkeypatch.delenv(key, raising=False)"` | — |
| [SRC-8C13B81AB4-L000034](../../tests/test_web_agent_nlu_integration.py#L34) | 34 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", lambda _q: [])"` | — |
| [SRC-8C13B81AB4-L000035](../../tests/test_web_agent_nlu_integration.py#L35) | 35 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", lambda _q: [])"` | — |
| [SRC-8C13B81AB4-L000036](../../tests/test_web_agent_nlu_integration.py#L36) | 36 | `"    monkeypatch.setattr(web_module, \"_public_http_url\", lambda value: value)"` | — |
| [SRC-8C13B81AB4-L000037](../../tests/test_web_agent_nlu_integration.py#L37) | 37 | `"    monkeypatch.setattr(web_module, \"_blocked_source_url\", lambda _value: False)"` | — |
| [SRC-8C13B81AB4-L000038](../../tests/test_web_agent_nlu_integration.py#L38) | 38 | `"    monkeypatch.setattr(web_module, \"_relevance_ratio\", lambda _q, _text: 1.0)"` | — |
| [SRC-8C13B81AB4-L000039](../../tests/test_web_agent_nlu_integration.py#L39) | 39 | `"    funcs = {\"openalex\": \"search_openalex\", \"arxiv\": \"search_arxiv\", \"crossref\": \"search_crossref\"}"` | — |
| [SRC-8C13B81AB4-L000040](../../tests/test_web_agent_nlu_integration.py#L40) | 40 | `"    for provider, attr in funcs.items():"` | — |
| [SRC-8C13B81AB4-L000041](../../tests/test_web_agent_nlu_integration.py#L41) | 41 | `"        monkeypatch.setattr("` | — |
| [SRC-8C13B81AB4-L000042](../../tests/test_web_agent_nlu_integration.py#L42) | 42 | `"            web_module, attr,"` | — |
| [SRC-8C13B81AB4-L000043](../../tests/test_web_agent_nlu_integration.py#L43) | 43 | `"            lambda query, limit=3, p=provider: [_academic_result(p, query)],"` | — |
| [SRC-8C13B81AB4-L000044](../../tests/test_web_agent_nlu_integration.py#L44) | 44 | `"        )"` | — |
| [SRC-8C13B81AB4-L000045](../../tests/test_web_agent_nlu_integration.py#L45) | 45 | `"    results = agent._search_web(\"peer-reviewed research on lithium battery degradation\")"` | — |
| [SRC-8C13B81AB4-L000046](../../tests/test_web_agent_nlu_integration.py#L46) | 46 | `"    assert {\"openalex\", \"arxiv\", \"crossref\"} <= {row[\"provider\"] for row in results}"` | — |
| [SRC-8C13B81AB4-L000047](../../tests/test_web_agent_nlu_integration.py#L47) | 47 | `""` | — |
| [SRC-8C13B81AB4-L000048](../../tests/test_web_agent_nlu_integration.py#L48) | 48 | `""` | — |
| [SRC-8C13B81AB4-L000049](../../tests/test_web_agent_nlu_integration.py#L49) | 49 | `"def test_academic_connectors_are_not_called_for_ordinary_sparse_queries(monkeypatch) -> None:"` | — |
| [SRC-8C13B81AB4-L000050](../../tests/test_web_agent_nlu_integration.py#L50) | 50 | `"    agent = WebAgent()"` | — |
| [SRC-8C13B81AB4-L000051](../../tests/test_web_agent_nlu_integration.py#L51) | 51 | `"    agent._request_budget = None"` | — |
| [SRC-8C13B81AB4-L000052](../../tests/test_web_agent_nlu_integration.py#L52) | 52 | `"    for key in (\"DEEPSEEK_SEARCH_API_KEY\", \"BRAVE_SEARCH_API_KEY\", \"TAVILY_API_KEY\"):"` | — |
| [SRC-8C13B81AB4-L000053](../../tests/test_web_agent_nlu_integration.py#L53) | 53 | `"        monkeypatch.delenv(key, raising=False)"` | — |
| [SRC-8C13B81AB4-L000054](../../tests/test_web_agent_nlu_integration.py#L54) | 54 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", lambda _q: [{"` | — |
| [SRC-8C13B81AB4-L000055](../../tests/test_web_agent_nlu_integration.py#L55) | 55 | `"        \"title\": \"iPhone 17 price in Egypt\","` | — |
| [SRC-8C13B81AB4-L000056](../../tests/test_web_agent_nlu_integration.py#L56) | 56 | `"        \"url\": \"https://example.com/iphone-price\","` | — |
| [SRC-8C13B81AB4-L000057](../../tests/test_web_agent_nlu_integration.py#L57) | 57 | `"        \"snippet\": \"iPhone 17 price in Egypt.\","` | — |
| [SRC-8C13B81AB4-L000058](../../tests/test_web_agent_nlu_integration.py#L58) | 58 | `"        \"provider\": \"duckduckgo_html\","` | — |
| [SRC-8C13B81AB4-L000059](../../tests/test_web_agent_nlu_integration.py#L59) | 59 | `"        \"provider_rank\": 1,"` | — |
| [SRC-8C13B81AB4-L000060](../../tests/test_web_agent_nlu_integration.py#L60) | 60 | `"    }])"` | — |
| [SRC-8C13B81AB4-L000061](../../tests/test_web_agent_nlu_integration.py#L61) | 61 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", lambda _q: [])"` | — |
| [SRC-8C13B81AB4-L000062](../../tests/test_web_agent_nlu_integration.py#L62) | 62 | `"    monkeypatch.setattr(web_module, \"_public_http_url\", lambda value: value)"` | — |
| [SRC-8C13B81AB4-L000063](../../tests/test_web_agent_nlu_integration.py#L63) | 63 | `"    monkeypatch.setattr(web_module, \"_blocked_source_url\", lambda _value: False)"` | — |
| [SRC-8C13B81AB4-L000064](../../tests/test_web_agent_nlu_integration.py#L64) | 64 | `"    monkeypatch.setattr(web_module, \"_relevance_ratio\", lambda _q, _text: 1.0)"` | — |
| [SRC-8C13B81AB4-L000065](../../tests/test_web_agent_nlu_integration.py#L65) | 65 | `""` | — |
| [SRC-8C13B81AB4-L000066](../../tests/test_web_agent_nlu_integration.py#L66) | 66 | `"    def unexpected(*_args, **_kwargs):"` | — |
| [SRC-8C13B81AB4-L000067](../../tests/test_web_agent_nlu_integration.py#L67) | 67 | `"        pytest.fail(\"Academic connectors must not run for ordinary product-price queries.\")"` | — |
| [SRC-8C13B81AB4-L000068](../../tests/test_web_agent_nlu_integration.py#L68) | 68 | `""` | — |
| [SRC-8C13B81AB4-L000069](../../tests/test_web_agent_nlu_integration.py#L69) | 69 | `"    monkeypatch.setattr(web_module, \"search_openalex\", unexpected)"` | — |
| [SRC-8C13B81AB4-L000070](../../tests/test_web_agent_nlu_integration.py#L70) | 70 | `"    monkeypatch.setattr(web_module, \"search_arxiv\", unexpected)"` | — |
| [SRC-8C13B81AB4-L000071](../../tests/test_web_agent_nlu_integration.py#L71) | 71 | `"    monkeypatch.setattr(web_module, \"search_crossref\", unexpected)"` | — |
| [SRC-8C13B81AB4-L000072](../../tests/test_web_agent_nlu_integration.py#L72) | 72 | `"    results = agent._search_web(\"iPhone 17 price in Egypt\")"` | — |
| [SRC-8C13B81AB4-L000073](../../tests/test_web_agent_nlu_integration.py#L73) | 73 | `"    assert len(results) == 1"` | — |
| [SRC-8C13B81AB4-L000074](../../tests/test_web_agent_nlu_integration.py#L74) | 74 | `"    assert results[0][\"provider\"] == \"duckduckgo_html\""` | — |
| [SRC-8C13B81AB4-L000075](../../tests/test_web_agent_nlu_integration.py#L75) | 75 | `""` | — |
| [SRC-8C13B81AB4-L000076](../../tests/test_web_agent_nlu_integration.py#L76) | 76 | `""` | — |
| [SRC-8C13B81AB4-L000077](../../tests/test_web_agent_nlu_integration.py#L77) | 77 | `"def test_web_agent_extracts_joined_comparison_facets() -> None:"` | — |
| [SRC-8C13B81AB4-L000078](../../tests/test_web_agent_nlu_integration.py#L78) | 78 | `"    targets = WebAgent._question_coverage_targets("` | — |
| [SRC-8C13B81AB4-L000079](../../tests/test_web_agent_nlu_integration.py#L79) | 79 | `"        \"قارن بين الأنظمة: السعر والبطارية، بالإضافة إلى الضمان والصيانة \""` | — |
| [SRC-8C13B81AB4-L000080](../../tests/test_web_agent_nlu_integration.py#L80) | 80 | `"        \"والخصوصية والاعتمادية والدعم والجودة\""` | — |
| [SRC-8C13B81AB4-L000081](../../tests/test_web_agent_nlu_integration.py#L81) | 81 | `"    )"` | — |
| [SRC-8C13B81AB4-L000082](../../tests/test_web_agent_nlu_integration.py#L82) | 82 | `"    joined = \" \".join(targets)"` | — |
| [SRC-8C13B81AB4-L000083](../../tests/test_web_agent_nlu_integration.py#L83) | 83 | `"    for expected in (\"السعر\", \"البطارية\", \"الضمان\", \"الصيانة\", \"الخصوصية\", \"الاعتمادية\", \"الدعم\", \"الجودة\"):"` | — |
| [SRC-8C13B81AB4-L000084](../../tests/test_web_agent_nlu_integration.py#L84) | 84 | `"        assert expected in joined"` | — |
| [SRC-8C13B81AB4-L000085](../../tests/test_web_agent_nlu_integration.py#L85) | 85 | `""` | — |
| [SRC-8C13B81AB4-L000086](../../tests/test_web_agent_nlu_integration.py#L86) | 86 | `""` | — |
| [SRC-8C13B81AB4-L000087](../../tests/test_web_agent_nlu_integration.py#L87) | 87 | `"def test_incomplete_compound_evidence_withholds_final_answer() -> None:"` | — |
| [SRC-8C13B81AB4-L000088](../../tests/test_web_agent_nlu_integration.py#L88) | 88 | `"    from agents.web_agent import enforce_aspect_answer_completeness"` | — |
| [SRC-8C13B81AB4-L000089](../../tests/test_web_agent_nlu_integration.py#L89) | 89 | `""` | — |
| [SRC-8C13B81AB4-L000090](../../tests/test_web_agent_nlu_integration.py#L90) | 90 | `"    payload = {"` | — |
| [SRC-8C13B81AB4-L000091](../../tests/test_web_agent_nlu_integration.py#L91) | 91 | `"        \"answer\": \"PRIVATE DRAFT: claim complete details for price and warranty.\","` | — |
| [SRC-8C13B81AB4-L000092](../../tests/test_web_agent_nlu_integration.py#L92) | 92 | `"        \"sources\": ["` | — |
| [SRC-8C13B81AB4-L000093](../../tests/test_web_agent_nlu_integration.py#L93) | 93 | `"            {"` | — |
| [SRC-8C13B81AB4-L000094](../../tests/test_web_agent_nlu_integration.py#L94) | 94 | `"                \"title\": \"Price list\","` | — |
| [SRC-8C13B81AB4-L000095](../../tests/test_web_agent_nlu_integration.py#L95) | 95 | `"                \"url\": \"https://example.org/prices\","` | — |
| [SRC-8C13B81AB4-L000096](../../tests/test_web_agent_nlu_integration.py#L96) | 96 | `"                \"snippet\": \"price cost prices\","` | — |
| [SRC-8C13B81AB4-L000097](../../tests/test_web_agent_nlu_integration.py#L97) | 97 | `"                \"provider\": \"mock\","` | — |
| [SRC-8C13B81AB4-L000098](../../tests/test_web_agent_nlu_integration.py#L98) | 98 | `"            }"` | — |
| [SRC-8C13B81AB4-L000099](../../tests/test_web_agent_nlu_integration.py#L99) | 99 | `"        ],"` | — |
| [SRC-8C13B81AB4-L000100](../../tests/test_web_agent_nlu_integration.py#L100) | 100 | `"        \"search_report\": {"` | — |
| [SRC-8C13B81AB4-L000101](../../tests/test_web_agent_nlu_integration.py#L101) | 101 | `"            \"evidence_ledger\": {"` | — |
| [SRC-8C13B81AB4-L000102](../../tests/test_web_agent_nlu_integration.py#L102) | 102 | `"                \"aspects\": [\"price\", \"warranty\"],"` | — |
| [SRC-8C13B81AB4-L000103](../../tests/test_web_agent_nlu_integration.py#L103) | 103 | `"                \"covered\": [\"price\"],"` | — |
| [SRC-8C13B81AB4-L000104](../../tests/test_web_agent_nlu_integration.py#L104) | 104 | `"                \"missing\": [\"warranty\"],"` | — |
| [SRC-8C13B81AB4-L000105](../../tests/test_web_agent_nlu_integration.py#L105) | 105 | `"                \"coverage_ratio\": 0.5,"` | — |
| [SRC-8C13B81AB4-L000106](../../tests/test_web_agent_nlu_integration.py#L106) | 106 | `"            },"` | — |
| [SRC-8C13B81AB4-L000107](../../tests/test_web_agent_nlu_integration.py#L107) | 107 | `"            \"aspect_diagnostics_ar\": [],"` | — |
| [SRC-8C13B81AB4-L000108](../../tests/test_web_agent_nlu_integration.py#L108) | 108 | `"        },"` | — |
| [SRC-8C13B81AB4-L000109](../../tests/test_web_agent_nlu_integration.py#L109) | 109 | `"    }"` | — |
| [SRC-8C13B81AB4-L000110](../../tests/test_web_agent_nlu_integration.py#L110) | 110 | `"    result = enforce_aspect_answer_completeness(payload)"` | — |
| [SRC-8C13B81AB4-L000111](../../tests/test_web_agent_nlu_integration.py#L111) | 111 | `"    assert result[\"answer_was_withheld\"] is True"` | — |
| [SRC-8C13B81AB4-L000112](../../tests/test_web_agent_nlu_integration.py#L112) | 112 | `"    assert result[\"answer_completeness_status\"] == \"incomplete_evidence_withheld\""` | — |
| [SRC-8C13B81AB4-L000113](../../tests/test_web_agent_nlu_integration.py#L113) | 113 | `"    assert result[\"aspect_evidence_gaps\"] == [\"warranty\"]"` | — |
| [SRC-8C13B81AB4-L000114](../../tests/test_web_agent_nlu_integration.py#L114) | 114 | `"    assert \"PRIVATE DRAFT\" not in result[\"answer\"]"` | — |
| [SRC-8C13B81AB4-L000115](../../tests/test_web_agent_nlu_integration.py#L115) | 115 | `"    assert \"warranty\" in result[\"answer\"]"` | — |
| [SRC-8C13B81AB4-L000116](../../tests/test_web_agent_nlu_integration.py#L116) | 116 | `"    assert result[\"search_report\"][\"task_fulfillment_status\"] == \"possible_gap_detected\""` | — |
| [SRC-8C13B81AB4-L000117](../../tests/test_web_agent_nlu_integration.py#L117) | 117 | `"    assert result[\"final_answer_status\"] == \"incomplete_evidence_withheld\""` | — |
| [SRC-8C13B81AB4-L000118](../../tests/test_web_agent_nlu_integration.py#L118) | 118 | `""` | — |
| [SRC-8C13B81AB4-L000119](../../tests/test_web_agent_nlu_integration.py#L119) | 119 | `""` | — |
| [SRC-8C13B81AB4-L000120](../../tests/test_web_agent_nlu_integration.py#L120) | 120 | `"def test_no_lexical_gap_is_not_presented_as_semantic_proof() -> None:"` | — |
| [SRC-8C13B81AB4-L000121](../../tests/test_web_agent_nlu_integration.py#L121) | 121 | `"    from agents.web_agent import enforce_aspect_answer_completeness"` | — |
| [SRC-8C13B81AB4-L000122](../../tests/test_web_agent_nlu_integration.py#L122) | 122 | `""` | — |
| [SRC-8C13B81AB4-L000123](../../tests/test_web_agent_nlu_integration.py#L123) | 123 | `"    payload = {"` | — |
| [SRC-8C13B81AB4-L000124](../../tests/test_web_agent_nlu_integration.py#L124) | 124 | `"        \"answer\": \"Supported draft.\","` | — |
| [SRC-8C13B81AB4-L000125](../../tests/test_web_agent_nlu_integration.py#L125) | 125 | `"        \"sources\": ["` | — |
| [SRC-8C13B81AB4-L000126](../../tests/test_web_agent_nlu_integration.py#L126) | 126 | `"            {"` | — |
| [SRC-8C13B81AB4-L000127](../../tests/test_web_agent_nlu_integration.py#L127) | 127 | `"                \"title\": \"Price and warranty terms\","` | — |
| [SRC-8C13B81AB4-L000128](../../tests/test_web_agent_nlu_integration.py#L128) | 128 | `"                \"url\": \"https://example.org/terms\","` | — |
| [SRC-8C13B81AB4-L000129](../../tests/test_web_agent_nlu_integration.py#L129) | 129 | `"                \"snippet\": \"price cost warranty warranty coverage\","` | — |
| [SRC-8C13B81AB4-L000130](../../tests/test_web_agent_nlu_integration.py#L130) | 130 | `"                \"provider\": \"mock\","` | — |
| [SRC-8C13B81AB4-L000131](../../tests/test_web_agent_nlu_integration.py#L131) | 131 | `"            }"` | — |
| [SRC-8C13B81AB4-L000132](../../tests/test_web_agent_nlu_integration.py#L132) | 132 | `"        ],"` | — |
| [SRC-8C13B81AB4-L000133](../../tests/test_web_agent_nlu_integration.py#L133) | 133 | `"        \"search_report\": {"` | — |
| [SRC-8C13B81AB4-L000134](../../tests/test_web_agent_nlu_integration.py#L134) | 134 | `"            \"evidence_ledger\": {\"aspects\": [\"price\", \"warranty\"], \"missing\": []},"` | — |
| [SRC-8C13B81AB4-L000135](../../tests/test_web_agent_nlu_integration.py#L135) | 135 | `"            \"aspect_diagnostics_ar\": [],"` | — |
| [SRC-8C13B81AB4-L000136](../../tests/test_web_agent_nlu_integration.py#L136) | 136 | `"        },"` | — |
| [SRC-8C13B81AB4-L000137](../../tests/test_web_agent_nlu_integration.py#L137) | 137 | `"    }"` | — |
| [SRC-8C13B81AB4-L000138](../../tests/test_web_agent_nlu_integration.py#L138) | 138 | `"    result = enforce_aspect_answer_completeness(payload)"` | — |
| [SRC-8C13B81AB4-L000139](../../tests/test_web_agent_nlu_integration.py#L139) | 139 | `"    assert result[\"answer_was_withheld\"] is False"` | — |
| [SRC-8C13B81AB4-L000140](../../tests/test_web_agent_nlu_integration.py#L140) | 140 | `"    assert result[\"answer_completeness_status\"] == ("` | — |
| [SRC-8C13B81AB4-L000141](../../tests/test_web_agent_nlu_integration.py#L141) | 141 | `"        \"no_lexical_gaps_detected_semantic_completeness_not_proven\""` | — |
| [SRC-8C13B81AB4-L000142](../../tests/test_web_agent_nlu_integration.py#L142) | 142 | `"    )"` | — |
| [SRC-8C13B81AB4-L000143](../../tests/test_web_agent_nlu_integration.py#L143) | 143 | `"    assert result[\"aspect_coverage_is_not_truth_score\"] is True"` | — |
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
