# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **060**
- سجلات الأسطر: **800**
- النطاق: SRC-F725E90B2A-L003494 إلى SRC-F725E90B2A-L004293
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-F725E90B2A — [tests/test_web_agent.py](../../tests/test_web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-F725E90B2A-L003494](../../tests/test_web_agent.py#L3494) | 3494 | `"            \"platform\": \"web\","` | — |
| [SRC-F725E90B2A-L003495](../../tests/test_web_agent.py#L3495) | 3495 | `"            \"published_at\": \"\","` | — |
| [SRC-F725E90B2A-L003496](../../tests/test_web_agent.py#L3496) | 3496 | `"        }]"` | — |
| [SRC-F725E90B2A-L003497](../../tests/test_web_agent.py#L3497) | 3497 | `"        return \"إجابة مبدئية [المصدر 1].\""` | — |
| [SRC-F725E90B2A-L003498](../../tests/test_web_agent.py#L3498) | 3498 | `""` | — |
| [SRC-F725E90B2A-L003499](../../tests/test_web_agent.py#L3499) | 3499 | `"    monkeypatch.setattr(agent, \"_generate\", generate)"` | — |
| [SRC-F725E90B2A-L003500](../../tests/test_web_agent.py#L3500) | 3500 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda _question, answer, _sources: answer)"` | — |
| [SRC-F725E90B2A-L003501](../../tests/test_web_agent.py#L3501) | 3501 | `""` | — |
| [SRC-F725E90B2A-L003502](../../tests/test_web_agent.py#L3502) | 3502 | `"    def capture_relevance(query, text):"` | — |
| [SRC-F725E90B2A-L003503](../../tests/test_web_agent.py#L3503) | 3503 | `"        if \"تجارب السيارات الكهربائية المستعملة\" in text:"` | — |
| [SRC-F725E90B2A-L003504](../../tests/test_web_agent.py#L3504) | 3504 | `"            source_queries.append(query)"` | — |
| [SRC-F725E90B2A-L003505](../../tests/test_web_agent.py#L3505) | 3505 | `"            if planned_query and query != compact_search_query(topic_query):"` | — |
| [SRC-F725E90B2A-L003506](../../tests/test_web_agent.py#L3506) | 3506 | `"                return 0.0"` | — |
| [SRC-F725E90B2A-L003507](../../tests/test_web_agent.py#L3507) | 3507 | `"        return 0.25"` | — |
| [SRC-F725E90B2A-L003508](../../tests/test_web_agent.py#L3508) | 3508 | `""` | — |
| [SRC-F725E90B2A-L003509](../../tests/test_web_agent.py#L3509) | 3509 | `"    monkeypatch.setattr(\"agents.web_agent._relevance_ratio\", capture_relevance)"` | — |
| [SRC-F725E90B2A-L003510](../../tests/test_web_agent.py#L3510) | 3510 | `""` | — |
| [SRC-F725E90B2A-L003511](../../tests/test_web_agent.py#L3511) | 3511 | `"    agent.answer(question)"` | — |
| [SRC-F725E90B2A-L003512](../../tests/test_web_agent.py#L3512) | 3512 | `""` | — |
| [SRC-F725E90B2A-L003513](../../tests/test_web_agent.py#L3513) | 3513 | `"    expected_queries = list(dict.fromkeys("` | — |
| [SRC-F725E90B2A-L003514](../../tests/test_web_agent.py#L3514) | 3514 | `"        query for query in ("` | — |
| [SRC-F725E90B2A-L003515](../../tests/test_web_agent.py#L3515) | 3515 | `"            compact_search_query(question),"` | — |
| [SRC-F725E90B2A-L003516](../../tests/test_web_agent.py#L3516) | 3516 | `"            compact_search_query(topic_query),"` | — |
| [SRC-F725E90B2A-L003517](../../tests/test_web_agent.py#L3517) | 3517 | `"        ) if query"` | — |
| [SRC-F725E90B2A-L003518](../../tests/test_web_agent.py#L3518) | 3518 | `"    ))"` | — |
| [SRC-F725E90B2A-L003519](../../tests/test_web_agent.py#L3519) | 3519 | `"    assert source_queries == expected_queries"` | — |
| [SRC-F725E90B2A-L003520](../../tests/test_web_agent.py#L3520) | 3520 | `""` | — |
| [SRC-F725E90B2A-L003521](../../tests/test_web_agent.py#L3521) | 3521 | `""` | — |
| [SRC-F725E90B2A-L003522](../../tests/test_web_agent.py#L3522) | 3522 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L003523](../../tests/test_web_agent.py#L3523) | 3523 | `"    (\"mode\", \"planner_query\"),"` | — |
| [SRC-F725E90B2A-L003524](../../tests/test_web_agent.py#L3524) | 3524 | `"    ["` | — |
| [SRC-F725E90B2A-L003525](../../tests/test_web_agent.py#L3525) | 3525 | `"        (\"auto\", \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\"),"` | — |
| [SRC-F725E90B2A-L003526](../../tests/test_web_agent.py#L3526) | 3526 | `"        (\"auto\", \"site:reddit.com\"),"` | — |
| [SRC-F725E90B2A-L003527](../../tests/test_web_agent.py#L3527) | 3527 | `"        (\"latest\", \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\"),"` | — |
| [SRC-F725E90B2A-L003528](../../tests/test_web_agent.py#L3528) | 3528 | `"        (\"deep\", \"site:reddit.com\"),"` | — |
| [SRC-F725E90B2A-L003529](../../tests/test_web_agent.py#L3529) | 3529 | `"        (\"social\", \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\"),"` | — |
| [SRC-F725E90B2A-L003530](../../tests/test_web_agent.py#L3530) | 3530 | `"    ],"` | — |
| [SRC-F725E90B2A-L003531](../../tests/test_web_agent.py#L3531) | 3531 | `")"` | — |
| [SRC-F725E90B2A-L003532](../../tests/test_web_agent.py#L3532) | 3532 | `"def test_modes_do_not_create_generic_queries_without_topic("` | — |
| [SRC-F725E90B2A-L003533](../../tests/test_web_agent.py#L3533) | 3533 | `"    monkeypatch, mode, planner_query"` | — |
| [SRC-F725E90B2A-L003534](../../tests/test_web_agent.py#L3534) | 3534 | `"):"` | — |
| [SRC-F725E90B2A-L003535](../../tests/test_web_agent.py#L3535) | 3535 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003536](../../tests/test_web_agent.py#L3536) | 3536 | `"    instruction_only = \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\""` | — |
| [SRC-F725E90B2A-L003537](../../tests/test_web_agent.py#L3537) | 3537 | `"    direct_url = \"https://example.com/report\""` | — |
| [SRC-F725E90B2A-L003538](../../tests/test_web_agent.py#L3538) | 3538 | `"    observed_plans = []"` | — |
| [SRC-F725E90B2A-L003539](../../tests/test_web_agent.py#L3539) | 3539 | `""` | — |
| [SRC-F725E90B2A-L003540](../../tests/test_web_agent.py#L3540) | 3540 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003541](../../tests/test_web_agent.py#L3541) | 3541 | `"        \"agents.web_agent.route_intent\","` | — |
| [SRC-F725E90B2A-L003542](../../tests/test_web_agent.py#L3542) | 3542 | `"        lambda *args, **kwargs: {\"route\": \"WEB_DEEP\", \"reason\": \"test\"},"` | — |
| [SRC-F725E90B2A-L003543](../../tests/test_web_agent.py#L3543) | 3543 | `"    )"` | — |
| [SRC-F725E90B2A-L003544](../../tests/test_web_agent.py#L3544) | 3544 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003545](../../tests/test_web_agent.py#L3545) | 3545 | `"        agent, \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003546](../../tests/test_web_agent.py#L3546) | 3546 | `"        lambda _question, _history: {"` | — |
| [SRC-F725E90B2A-L003547](../../tests/test_web_agent.py#L3547) | 3547 | `"            \"queries\": [planner_query],"` | — |
| [SRC-F725E90B2A-L003548](../../tests/test_web_agent.py#L3548) | 3548 | `"            \"direct_urls\": [direct_url],"` | — |
| [SRC-F725E90B2A-L003549](../../tests/test_web_agent.py#L3549) | 3549 | `"            \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003550](../../tests/test_web_agent.py#L3550) | 3550 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003551](../../tests/test_web_agent.py#L3551) | 3551 | `"            \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L003552](../../tests/test_web_agent.py#L3552) | 3552 | `"            \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003553](../../tests/test_web_agent.py#L3553) | 3553 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003554](../../tests/test_web_agent.py#L3554) | 3554 | `"        },"` | — |
| [SRC-F725E90B2A-L003555](../../tests/test_web_agent.py#L3555) | 3555 | `"    )"` | — |
| [SRC-F725E90B2A-L003556](../../tests/test_web_agent.py#L3556) | 3556 | `""` | — |
| [SRC-F725E90B2A-L003557](../../tests/test_web_agent.py#L3557) | 3557 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L003558](../../tests/test_web_agent.py#L3558) | 3558 | `"        observed_plans.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L003559](../../tests/test_web_agent.py#L3559) | 3559 | `"        return [], [], {"` | — |
| [SRC-F725E90B2A-L003560](../../tests/test_web_agent.py#L3560) | 3560 | `"            \"queries_planned\": len(research_plan.get(\"queries\", [])),"` | — |
| [SRC-F725E90B2A-L003561](../../tests/test_web_agent.py#L3561) | 3561 | `"            \"queries_attempted\": 0,"` | — |
| [SRC-F725E90B2A-L003562](../../tests/test_web_agent.py#L3562) | 3562 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L003563](../../tests/test_web_agent.py#L3563) | 3563 | `"            \"unique_sources\": 0,"` | — |
| [SRC-F725E90B2A-L003564](../../tests/test_web_agent.py#L3564) | 3564 | `"            \"pages_fetched\": 0,"` | — |
| [SRC-F725E90B2A-L003565](../../tests/test_web_agent.py#L3565) | 3565 | `"            \"providers_used\": [],"` | — |
| [SRC-F725E90B2A-L003566](../../tests/test_web_agent.py#L3566) | 3566 | `"            \"platform_counts\": {},"` | — |
| [SRC-F725E90B2A-L003567](../../tests/test_web_agent.py#L3567) | 3567 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L003568](../../tests/test_web_agent.py#L3568) | 3568 | `"            \"depth\": research_plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-F725E90B2A-L003569](../../tests/test_web_agent.py#L3569) | 3569 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003570](../../tests/test_web_agent.py#L3570) | 3570 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L003571](../../tests/test_web_agent.py#L3571) | 3571 | `"        }"` | — |
| [SRC-F725E90B2A-L003572](../../tests/test_web_agent.py#L3572) | 3572 | `""` | — |
| [SRC-F725E90B2A-L003573](../../tests/test_web_agent.py#L3573) | 3573 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L003574](../../tests/test_web_agent.py#L3574) | 3574 | `""` | — |
| [SRC-F725E90B2A-L003575](../../tests/test_web_agent.py#L3575) | 3575 | `"    agent.answer(instruction_only, mode=mode)"` | — |
| [SRC-F725E90B2A-L003576](../../tests/test_web_agent.py#L3576) | 3576 | `""` | — |
| [SRC-F725E90B2A-L003577](../../tests/test_web_agent.py#L3577) | 3577 | `"    assert observed_plans"` | — |
| [SRC-F725E90B2A-L003578](../../tests/test_web_agent.py#L3578) | 3578 | `"    assert observed_plans[0][\"queries\"] == []"` | — |
| [SRC-F725E90B2A-L003579](../../tests/test_web_agent.py#L3579) | 3579 | `"    assert observed_plans[0][\"direct_urls\"] == [direct_url]"` | — |
| [SRC-F725E90B2A-L003580](../../tests/test_web_agent.py#L3580) | 3580 | `""` | — |
| [SRC-F725E90B2A-L003581](../../tests/test_web_agent.py#L3581) | 3581 | `""` | — |
| [SRC-F725E90B2A-L003582](../../tests/test_web_agent.py#L3582) | 3582 | `"def test_auto_navigation_strips_arabic_search_verb_without_regex_regression(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003583](../../tests/test_web_agent.py#L3583) | 3583 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003584](../../tests/test_web_agent.py#L3584) | 3584 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L003585](../../tests/test_web_agent.py#L3585) | 3585 | `"    question = \"ابحث عن الموقع الرسمي لشركة النور\""` | — |
| [SRC-F725E90B2A-L003586](../../tests/test_web_agent.py#L3586) | 3586 | `"    observed_plans = []"` | — |
| [SRC-F725E90B2A-L003587](../../tests/test_web_agent.py#L3587) | 3587 | `""` | — |
| [SRC-F725E90B2A-L003588](../../tests/test_web_agent.py#L3588) | 3588 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003589](../../tests/test_web_agent.py#L3589) | 3589 | `"        \"agents.web_agent.route_intent\","` | — |
| [SRC-F725E90B2A-L003590](../../tests/test_web_agent.py#L3590) | 3590 | `"        lambda *args, **kwargs: {\"route\": \"WEB_SIMPLE\", \"reason\": \"test\"},"` | — |
| [SRC-F725E90B2A-L003591](../../tests/test_web_agent.py#L3591) | 3591 | `"    )"` | — |
| [SRC-F725E90B2A-L003592](../../tests/test_web_agent.py#L3592) | 3592 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003593](../../tests/test_web_agent.py#L3593) | 3593 | `"        \"agents.web_agent.compact_search_query\","` | — |
| [SRC-F725E90B2A-L003594](../../tests/test_web_agent.py#L3594) | 3594 | `"        lambda value: value.strip() if isinstance(value, str) else \"\","` | — |
| [SRC-F725E90B2A-L003595](../../tests/test_web_agent.py#L3595) | 3595 | `"    )"` | — |
| [SRC-F725E90B2A-L003596](../../tests/test_web_agent.py#L3596) | 3596 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003597](../../tests/test_web_agent.py#L3597) | 3597 | `"        agent, \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003598](../../tests/test_web_agent.py#L3598) | 3598 | `"        lambda _question, _history: {"` | — |
| [SRC-F725E90B2A-L003599](../../tests/test_web_agent.py#L3599) | 3599 | `"            \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L003600](../../tests/test_web_agent.py#L3600) | 3600 | `"            \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L003601](../../tests/test_web_agent.py#L3601) | 3601 | `"            \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003602](../../tests/test_web_agent.py#L3602) | 3602 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003603](../../tests/test_web_agent.py#L3603) | 3603 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003604](../../tests/test_web_agent.py#L3604) | 3604 | `"            \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003605](../../tests/test_web_agent.py#L3605) | 3605 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003606](../../tests/test_web_agent.py#L3606) | 3606 | `"        },"` | — |
| [SRC-F725E90B2A-L003607](../../tests/test_web_agent.py#L3607) | 3607 | `"    )"` | — |
| [SRC-F725E90B2A-L003608](../../tests/test_web_agent.py#L3608) | 3608 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003609](../../tests/test_web_agent.py#L3609) | 3609 | `"        \"agents.web_agent.fallback_plan\","` | — |
| [SRC-F725E90B2A-L003610](../../tests/test_web_agent.py#L3610) | 3610 | `"        lambda *args, **kwargs: {\"queries\": [question]},"` | — |
| [SRC-F725E90B2A-L003611](../../tests/test_web_agent.py#L3611) | 3611 | `"    )"` | — |
| [SRC-F725E90B2A-L003612](../../tests/test_web_agent.py#L3612) | 3612 | `""` | — |
| [SRC-F725E90B2A-L003613](../../tests/test_web_agent.py#L3613) | 3613 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L003614](../../tests/test_web_agent.py#L3614) | 3614 | `"        observed_plans.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L003615](../../tests/test_web_agent.py#L3615) | 3615 | `"        return [], [], {"` | — |
| [SRC-F725E90B2A-L003616](../../tests/test_web_agent.py#L3616) | 3616 | `"            \"queries_planned\": len(research_plan.get(\"queries\", [])),"` | — |
| [SRC-F725E90B2A-L003617](../../tests/test_web_agent.py#L3617) | 3617 | `"            \"queries_attempted\": 0,"` | — |
| [SRC-F725E90B2A-L003618](../../tests/test_web_agent.py#L3618) | 3618 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L003619](../../tests/test_web_agent.py#L3619) | 3619 | `"            \"unique_sources\": 0,"` | — |
| [SRC-F725E90B2A-L003620](../../tests/test_web_agent.py#L3620) | 3620 | `"            \"pages_fetched\": 0,"` | — |
| [SRC-F725E90B2A-L003621](../../tests/test_web_agent.py#L3621) | 3621 | `"            \"providers_used\": [],"` | — |
| [SRC-F725E90B2A-L003622](../../tests/test_web_agent.py#L3622) | 3622 | `"            \"platform_counts\": {},"` | — |
| [SRC-F725E90B2A-L003623](../../tests/test_web_agent.py#L3623) | 3623 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L003624](../../tests/test_web_agent.py#L3624) | 3624 | `"            \"depth\": research_plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-F725E90B2A-L003625](../../tests/test_web_agent.py#L3625) | 3625 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003626](../../tests/test_web_agent.py#L3626) | 3626 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L003627](../../tests/test_web_agent.py#L3627) | 3627 | `"        }"` | — |
| [SRC-F725E90B2A-L003628](../../tests/test_web_agent.py#L3628) | 3628 | `""` | — |
| [SRC-F725E90B2A-L003629](../../tests/test_web_agent.py#L3629) | 3629 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L003630](../../tests/test_web_agent.py#L3630) | 3630 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"لم أعثر على مصدر.\")"` | — |
| [SRC-F725E90B2A-L003631](../../tests/test_web_agent.py#L3631) | 3631 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda _question, answer, _sources: answer)"` | — |
| [SRC-F725E90B2A-L003632](../../tests/test_web_agent.py#L3632) | 3632 | `""` | — |
| [SRC-F725E90B2A-L003633](../../tests/test_web_agent.py#L3633) | 3633 | `"    agent.answer(question, mode=\"auto\")"` | — |
| [SRC-F725E90B2A-L003634](../../tests/test_web_agent.py#L3634) | 3634 | `""` | — |
| [SRC-F725E90B2A-L003635](../../tests/test_web_agent.py#L3635) | 3635 | `"    assert observed_plans"` | — |
| [SRC-F725E90B2A-L003636](../../tests/test_web_agent.py#L3636) | 3636 | `"    assert observed_plans[0][\"queries\"]"` | — |
| [SRC-F725E90B2A-L003637](../../tests/test_web_agent.py#L3637) | 3637 | `"    assert all(not query.startswith(\"ابحث عن\") for query in observed_plans[0][\"queries\"])"` | — |
| [SRC-F725E90B2A-L003638](../../tests/test_web_agent.py#L3638) | 3638 | `"    assert \"الموقع الرسمي لشركة النور\" in observed_plans[0][\"queries\"][0]"` | — |
| [SRC-F725E90B2A-L003639](../../tests/test_web_agent.py#L3639) | 3639 | `"def test_latest_mode_does_not_generate_answer_from_stale_pages(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003640](../../tests/test_web_agent.py#L3640) | 3640 | `"    \"\"\"Current-mode answers must abstain if only old pages survive retrieval.\"\"\""` | — |
| [SRC-F725E90B2A-L003641](../../tests/test_web_agent.py#L3641) | 3641 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003642](../../tests/test_web_agent.py#L3642) | 3642 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L003643](../../tests/test_web_agent.py#L3643) | 3643 | `"        \"queries\": [\"مواعيد عمل مكتب الجوازات العباسية اليوم\"],"` | — |
| [SRC-F725E90B2A-L003644](../../tests/test_web_agent.py#L3644) | 3644 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L003645](../../tests/test_web_agent.py#L3645) | 3645 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003646](../../tests/test_web_agent.py#L3646) | 3646 | `"        \"freshness\": \"current\","` | — |
| [SRC-F725E90B2A-L003647](../../tests/test_web_agent.py#L3647) | 3647 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003648](../../tests/test_web_agent.py#L3648) | 3648 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003649](../../tests/test_web_agent.py#L3649) | 3649 | `"        \"planning_method\": \"fixture\","` | — |
| [SRC-F725E90B2A-L003650](../../tests/test_web_agent.py#L3650) | 3650 | `"        \"coverage_targets\": [],"` | — |
| [SRC-F725E90B2A-L003651](../../tests/test_web_agent.py#L3651) | 3651 | `"    }"` | — |
| [SRC-F725E90B2A-L003652](../../tests/test_web_agent.py#L3652) | 3652 | `"    collection_calls = []"` | — |
| [SRC-F725E90B2A-L003653](../../tests/test_web_agent.py#L3653) | 3653 | `""` | — |
| [SRC-F725E90B2A-L003654](../../tests/test_web_agent.py#L3654) | 3654 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L003655](../../tests/test_web_agent.py#L3655) | 3655 | `"        collection_calls.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L003656](../../tests/test_web_agent.py#L3656) | 3656 | `"        old_page = sample_source(0)"` | — |
| [SRC-F725E90B2A-L003657](../../tests/test_web_agent.py#L3657) | 3657 | `"        old_page.update({"` | — |
| [SRC-F725E90B2A-L003658](../../tests/test_web_agent.py#L3658) | 3658 | `"            \"url\": \"https://moi.gov.eg/passports\","` | — |
| [SRC-F725E90B2A-L003659](../../tests/test_web_agent.py#L3659) | 3659 | `"            \"domain\": \"moi.gov.eg\","` | — |
| [SRC-F725E90B2A-L003660](../../tests/test_web_agent.py#L3660) | 3660 | `"            \"published_at\": \"2024-01-01T10:00:00Z\","` | — |
| [SRC-F725E90B2A-L003661](../../tests/test_web_agent.py#L3661) | 3661 | `"            \"page_fetched\": True,"` | — |
| [SRC-F725E90B2A-L003662](../../tests/test_web_agent.py#L3662) | 3662 | `"            \"page_text\": \"محتوى قديم عن مواعيد العمل\","` | — |
| [SRC-F725E90B2A-L003663](../../tests/test_web_agent.py#L3663) | 3663 | `"        })"` | — |
| [SRC-F725E90B2A-L003664](../../tests/test_web_agent.py#L3664) | 3664 | `"        return [old_page], [], {"` | — |
| [SRC-F725E90B2A-L003665](../../tests/test_web_agent.py#L3665) | 3665 | `"            \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L003666](../../tests/test_web_agent.py#L3666) | 3666 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L003667](../../tests/test_web_agent.py#L3667) | 3667 | `"            \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L003668](../../tests/test_web_agent.py#L3668) | 3668 | `"            \"pages_fetched\": 1,"` | — |
| [SRC-F725E90B2A-L003669](../../tests/test_web_agent.py#L3669) | 3669 | `"            \"providers_used\": [\"fixture\"],"` | — |
| [SRC-F725E90B2A-L003670](../../tests/test_web_agent.py#L3670) | 3670 | `"            \"provider_counts\": {\"fixture\": 1},"` | — |
| [SRC-F725E90B2A-L003671](../../tests/test_web_agent.py#L3671) | 3671 | `"            \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L003672](../../tests/test_web_agent.py#L3672) | 3672 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L003673](../../tests/test_web_agent.py#L3673) | 3673 | `"            \"expansion_queries\": [],"` | — |
| [SRC-F725E90B2A-L003674](../../tests/test_web_agent.py#L3674) | 3674 | `"            \"provider_diagnostics\": [],"` | — |
| [SRC-F725E90B2A-L003675](../../tests/test_web_agent.py#L3675) | 3675 | `"            \"query_results\": [{\"query\": research_plan[\"queries\"][0], \"results\": 1}],"` | — |
| [SRC-F725E90B2A-L003676](../../tests/test_web_agent.py#L3676) | 3676 | `"        }"` | — |
| [SRC-F725E90B2A-L003677](../../tests/test_web_agent.py#L3677) | 3677 | `""` | — |
| [SRC-F725E90B2A-L003678](../../tests/test_web_agent.py#L3678) | 3678 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda *args, **kwargs: dict(plan))"` | — |
| [SRC-F725E90B2A-L003679](../../tests/test_web_agent.py#L3679) | 3679 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L003680](../../tests/test_web_agent.py#L3680) | 3680 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L003681](../../tests/test_web_agent.py#L3681) | 3681 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003682](../../tests/test_web_agent.py#L3682) | 3682 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003683](../../tests/test_web_agent.py#L3683) | 3683 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L003684](../../tests/test_web_agent.py#L3684) | 3684 | `"        lambda *args, **kwargs: pytest.fail(\"Stale pages must not be passed to generation\"),"` | — |
| [SRC-F725E90B2A-L003685](../../tests/test_web_agent.py#L3685) | 3685 | `"    )"` | — |
| [SRC-F725E90B2A-L003686](../../tests/test_web_agent.py#L3686) | 3686 | `""` | — |
| [SRC-F725E90B2A-L003687](../../tests/test_web_agent.py#L3687) | 3687 | `"    result = agent.answer(\"ما مواعيد عمل مكتب الجوازات اليوم؟\", mode=\"latest\")"` | — |
| [SRC-F725E90B2A-L003688](../../tests/test_web_agent.py#L3688) | 3688 | `""` | — |
| [SRC-F725E90B2A-L003689](../../tests/test_web_agent.py#L3689) | 3689 | `"    assert result[\"kind\"] == \"insufficient_evidence\""` | — |
| [SRC-F725E90B2A-L003690](../../tests/test_web_agent.py#L3690) | 3690 | `"    assert len(collection_calls) >= 1"` | — |
| [SRC-F725E90B2A-L003691](../../tests/test_web_agent.py#L3691) | 3691 | `"    guardrails = result[\"search_report\"][\"source_guardrails\"]"` | — |
| [SRC-F725E90B2A-L003692](../../tests/test_web_agent.py#L3692) | 3692 | `"    assert guardrails[\"initial\"][\"rejection_counts\"][\"stale\"] == 1"` | — |
| [SRC-F725E90B2A-L003693](../../tests/test_web_agent.py#L3693) | 3693 | `"    assert guardrails[\"final\"][\"current_evidence_status\"] == \"no_current_eligible_evidence\""` | — |
| [SRC-F725E90B2A-L003694](../../tests/test_web_agent.py#L3694) | 3694 | `"    assert result[\"search_report\"][\"search_outcome\"] == \"attempted_no_usable_sources\""` | — |
| [SRC-F725E90B2A-L003695](../../tests/test_web_agent.py#L3695) | 3695 | `""` | — |
| [SRC-F725E90B2A-L003696](../../tests/test_web_agent.py#L3696) | 3696 | `"def test_official_government_lookup_never_synthesizes_tourism_result(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003697](../../tests/test_web_agent.py#L3697) | 3697 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003698](../../tests/test_web_agent.py#L3698) | 3698 | `"    question = \"ابحث عن الموقع الرسمي لوزارة الاتصالات وتكنولوجيا المعلومات المصرية\""` | — |
| [SRC-F725E90B2A-L003699](../../tests/test_web_agent.py#L3699) | 3699 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L003700](../../tests/test_web_agent.py#L3700) | 3700 | `"        \"queries\": [\"وزارة الاتصالات وتكنولوجيا المعلومات مصر الموقع الرسمي\"],"` | — |
| [SRC-F725E90B2A-L003701](../../tests/test_web_agent.py#L3701) | 3701 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L003702](../../tests/test_web_agent.py#L3702) | 3702 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003703](../../tests/test_web_agent.py#L3703) | 3703 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003704](../../tests/test_web_agent.py#L3704) | 3704 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003705](../../tests/test_web_agent.py#L3705) | 3705 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003706](../../tests/test_web_agent.py#L3706) | 3706 | `"        \"planning_method\": \"fixture\","` | — |
| [SRC-F725E90B2A-L003707](../../tests/test_web_agent.py#L3707) | 3707 | `"    }"` | — |
| [SRC-F725E90B2A-L003708](../../tests/test_web_agent.py#L3708) | 3708 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L003709](../../tests/test_web_agent.py#L3709) | 3709 | `""` | — |
| [SRC-F725E90B2A-L003710](../../tests/test_web_agent.py#L3710) | 3710 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L003711](../../tests/test_web_agent.py#L3711) | 3711 | `"        calls.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L003712](../../tests/test_web_agent.py#L3712) | 3712 | `"        candidate = sample_source(0)"` | — |
| [SRC-F725E90B2A-L003713](../../tests/test_web_agent.py#L3713) | 3713 | `"        candidate.update({"` | — |
| [SRC-F725E90B2A-L003714](../../tests/test_web_agent.py#L3714) | 3714 | `"            \"title\": \"وزارة الاتصالات في مصر ومعلومات سياحية\","` | — |
| [SRC-F725E90B2A-L003715](../../tests/test_web_agent.py#L3715) | 3715 | `"            \"url\": \"https://visitegypt.com/\","` | — |
| [SRC-F725E90B2A-L003716](../../tests/test_web_agent.py#L3716) | 3716 | `"            \"domain\": \"visitegypt.com\","` | — |
| [SRC-F725E90B2A-L003717](../../tests/test_web_agent.py#L3717) | 3717 | `"            \"snippet\": \"معلومات عن الوزارة ضمن دليل سياحي لمصر\","` | — |
| [SRC-F725E90B2A-L003718](../../tests/test_web_agent.py#L3718) | 3718 | `"            \"page_fetched\": True,"` | — |
| [SRC-F725E90B2A-L003719](../../tests/test_web_agent.py#L3719) | 3719 | `"            \"page_text\": \"معلومات سياحية تذكر وزارة الاتصالات\","` | — |
| [SRC-F725E90B2A-L003720](../../tests/test_web_agent.py#L3720) | 3720 | `"            \"queries\": list(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L003721](../../tests/test_web_agent.py#L3721) | 3721 | `"        })"` | — |
| [SRC-F725E90B2A-L003722](../../tests/test_web_agent.py#L3722) | 3722 | `"        return [candidate], [], {"` | — |
| [SRC-F725E90B2A-L003723](../../tests/test_web_agent.py#L3723) | 3723 | `"            \"queries_planned\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L003724](../../tests/test_web_agent.py#L3724) | 3724 | `"            \"queries_attempted\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L003725](../../tests/test_web_agent.py#L3725) | 3725 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L003726](../../tests/test_web_agent.py#L3726) | 3726 | `"            \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L003727](../../tests/test_web_agent.py#L3727) | 3727 | `"            \"pages_fetched\": 1,"` | — |
| [SRC-F725E90B2A-L003728](../../tests/test_web_agent.py#L3728) | 3728 | `"            \"providers_used\": [\"fixture\"],"` | — |
| [SRC-F725E90B2A-L003729](../../tests/test_web_agent.py#L3729) | 3729 | `"            \"provider_counts\": {\"fixture\": 1},"` | — |
| [SRC-F725E90B2A-L003730](../../tests/test_web_agent.py#L3730) | 3730 | `"            \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L003731](../../tests/test_web_agent.py#L3731) | 3731 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L003732](../../tests/test_web_agent.py#L3732) | 3732 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003733](../../tests/test_web_agent.py#L3733) | 3733 | `"            \"planning_method\": \"fixture\","` | — |
| [SRC-F725E90B2A-L003734](../../tests/test_web_agent.py#L3734) | 3734 | `"            \"provider_diagnostics\": [],"` | — |
| [SRC-F725E90B2A-L003735](../../tests/test_web_agent.py#L3735) | 3735 | `"        }"` | — |
| [SRC-F725E90B2A-L003736](../../tests/test_web_agent.py#L3736) | 3736 | `""` | — |
| [SRC-F725E90B2A-L003737](../../tests/test_web_agent.py#L3737) | 3737 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda *args, **kwargs: dict(plan))"` | — |
| [SRC-F725E90B2A-L003738](../../tests/test_web_agent.py#L3738) | 3738 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L003739](../../tests/test_web_agent.py#L3739) | 3739 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L003740](../../tests/test_web_agent.py#L3740) | 3740 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003741](../../tests/test_web_agent.py#L3741) | 3741 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003742](../../tests/test_web_agent.py#L3742) | 3742 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L003743](../../tests/test_web_agent.py#L3743) | 3743 | `"        lambda *args, **kwargs: pytest.fail("` | — |
| [SRC-F725E90B2A-L003744](../../tests/test_web_agent.py#L3744) | 3744 | `"            \"A tourism result must never be passed to answer generation as the official site\""` | — |
| [SRC-F725E90B2A-L003745](../../tests/test_web_agent.py#L3745) | 3745 | `"        ),"` | — |
| [SRC-F725E90B2A-L003746](../../tests/test_web_agent.py#L3746) | 3746 | `"    )"` | — |
| [SRC-F725E90B2A-L003747](../../tests/test_web_agent.py#L3747) | 3747 | `""` | — |
| [SRC-F725E90B2A-L003748](../../tests/test_web_agent.py#L3748) | 3748 | `"    result = agent.answer(question, mode=\"auto\")"` | — |
| [SRC-F725E90B2A-L003749](../../tests/test_web_agent.py#L3749) | 3749 | `""` | — |
| [SRC-F725E90B2A-L003750](../../tests/test_web_agent.py#L3750) | 3750 | `"    assert calls  # initial research, plus bounded repair where applicable"` | — |
| [SRC-F725E90B2A-L003751](../../tests/test_web_agent.py#L3751) | 3751 | `"    assert result[\"kind\"] == \"insufficient_evidence\""` | — |
| [SRC-F725E90B2A-L003752](../../tests/test_web_agent.py#L3752) | 3752 | `"    assert result[\"sources\"] == []"` | — |
| [SRC-F725E90B2A-L003753](../../tests/test_web_agent.py#L3753) | 3753 | `"    guardrails = result[\"search_report\"][\"source_guardrails\"]"` | — |
| [SRC-F725E90B2A-L003754](../../tests/test_web_agent.py#L3754) | 3754 | `"    assert guardrails[\"initial\"][\"official_government_domain_required\"] is True"` | — |
| [SRC-F725E90B2A-L003755](../../tests/test_web_agent.py#L3755) | 3755 | `"    assert guardrails[\"initial\"][\"rejection_counts\"] == {"` | — |
| [SRC-F725E90B2A-L003756](../../tests/test_web_agent.py#L3756) | 3756 | `"        \"not_an_official_government_domain\": 1"` | — |
| [SRC-F725E90B2A-L003757](../../tests/test_web_agent.py#L3757) | 3757 | `"    }"` | — |
| [SRC-F725E90B2A-L003758](../../tests/test_web_agent.py#L3758) | 3758 | `"    assert guardrails[\"final\"][\"accepted_sources\"] == 0"` | — |
| [SRC-F725E90B2A-L003759](../../tests/test_web_agent.py#L3759) | 3759 | `"    assert result[\"search_report\"][\"usable_sources_after_filtering\"] == 0"` | — |
| [SRC-F725E90B2A-L003760](../../tests/test_web_agent.py#L3760) | 3760 | `""` | — |
| [SRC-F725E90B2A-L003761](../../tests/test_web_agent.py#L3761) | 3761 | `"def test_criterion_gap_repair_cannot_reintroduce_non_social_source(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003762](../../tests/test_web_agent.py#L3762) | 3762 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003763](../../tests/test_web_agent.py#L3763) | 3763 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L003764](../../tests/test_web_agent.py#L3764) | 3764 | `"    question = ("` | — |
| [SRC-F725E90B2A-L003765](../../tests/test_web_agent.py#L3765) | 3765 | `"        \"قارن بين خدمتين من حيث السعر والخصوصية والاعتمادية \""` | — |
| [SRC-F725E90B2A-L003766](../../tests/test_web_agent.py#L3766) | 3766 | `"        \"واعرض آراء وتجارب المستخدمين\""` | — |
| [SRC-F725E90B2A-L003767](../../tests/test_web_agent.py#L3767) | 3767 | `"    )"` | — |
| [SRC-F725E90B2A-L003768](../../tests/test_web_agent.py#L3768) | 3768 | `"    initial_sources = ["` | — |
| [SRC-F725E90B2A-L003769](../../tests/test_web_agent.py#L3769) | 3769 | `"        {"` | — |
| [SRC-F725E90B2A-L003770](../../tests/test_web_agent.py#L3770) | 3770 | `"            **sample_source(0),"` | — |
| [SRC-F725E90B2A-L003771](../../tests/test_web_agent.py#L3771) | 3771 | `"            \"url\": \"https://www.reddit.com/r/example/comments/1\","` | — |
| [SRC-F725E90B2A-L003772](../../tests/test_web_agent.py#L3772) | 3772 | `"            \"domain\": \"reddit.com\","` | — |
| [SRC-F725E90B2A-L003773](../../tests/test_web_agent.py#L3773) | 3773 | `"            \"title\": \"مناقشة تجارب المستخدمين للخدمتين\","` | — |
| [SRC-F725E90B2A-L003774](../../tests/test_web_agent.py#L3774) | 3774 | `"            \"snippet\": \"تجارب وآراء مستخدمين حول الخدمتين\","` | — |
| [SRC-F725E90B2A-L003775](../../tests/test_web_agent.py#L3775) | 3775 | `"            \"page_text\": \"تجارب وآراء مستخدمين حول الخدمتين\","` | — |
| [SRC-F725E90B2A-L003776](../../tests/test_web_agent.py#L3776) | 3776 | `"            \"platform\": \"reddit\","` | — |
| [SRC-F725E90B2A-L003777](../../tests/test_web_agent.py#L3777) | 3777 | `"            \"providers\": [\"reddit\"],"` | — |
| [SRC-F725E90B2A-L003778](../../tests/test_web_agent.py#L3778) | 3778 | `"        },"` | — |
| [SRC-F725E90B2A-L003779](../../tests/test_web_agent.py#L3779) | 3779 | `"        {"` | — |
| [SRC-F725E90B2A-L003780](../../tests/test_web_agent.py#L3780) | 3780 | `"            **sample_source(1),"` | — |
| [SRC-F725E90B2A-L003781](../../tests/test_web_agent.py#L3781) | 3781 | `"            \"url\": \"https://www.reddit.com/r/example/comments/2\","` | — |
| [SRC-F725E90B2A-L003782](../../tests/test_web_agent.py#L3782) | 3782 | `"            \"domain\": \"reddit.com\","` | — |
| [SRC-F725E90B2A-L003783](../../tests/test_web_agent.py#L3783) | 3783 | `"            \"title\": \"مناقشة أخرى عن الخدمتين\","` | — |
| [SRC-F725E90B2A-L003784](../../tests/test_web_agent.py#L3784) | 3784 | `"            \"snippet\": \"مناقشة وتجارب مستخدمين حول الخدمتين\","` | — |
| [SRC-F725E90B2A-L003785](../../tests/test_web_agent.py#L3785) | 3785 | `"            \"page_text\": \"مناقشة وتجارب مستخدمين حول الخدمتين\","` | — |
| [SRC-F725E90B2A-L003786](../../tests/test_web_agent.py#L3786) | 3786 | `"            \"platform\": \"reddit\","` | — |
| [SRC-F725E90B2A-L003787](../../tests/test_web_agent.py#L3787) | 3787 | `"            \"providers\": [\"reddit\"],"` | — |
| [SRC-F725E90B2A-L003788](../../tests/test_web_agent.py#L3788) | 3788 | `"        },"` | — |
| [SRC-F725E90B2A-L003789](../../tests/test_web_agent.py#L3789) | 3789 | `"    ]"` | — |
| [SRC-F725E90B2A-L003790](../../tests/test_web_agent.py#L3790) | 3790 | `"    repair_candidate = {"` | — |
| [SRC-F725E90B2A-L003791](../../tests/test_web_agent.py#L3791) | 3791 | `"        **sample_source(2),"` | — |
| [SRC-F725E90B2A-L003792](../../tests/test_web_agent.py#L3792) | 3792 | `"        \"url\": \"https://example.com/unrelated-repair\","` | — |
| [SRC-F725E90B2A-L003793](../../tests/test_web_agent.py#L3793) | 3793 | `"        \"domain\": \"example.com\","` | — |
| [SRC-F725E90B2A-L003794](../../tests/test_web_agent.py#L3794) | 3794 | `"        \"title\": \"معلومات عن الخدمة\","` | — |
| [SRC-F725E90B2A-L003795](../../tests/test_web_agent.py#L3795) | 3795 | `"        \"snippet\": \"معلومات عامة عن الخدمة\","` | — |
| [SRC-F725E90B2A-L003796](../../tests/test_web_agent.py#L3796) | 3796 | `"        \"page_text\": \"معلومات عامة عن الخدمة\","` | — |
| [SRC-F725E90B2A-L003797](../../tests/test_web_agent.py#L3797) | 3797 | `"        \"providers\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L003798](../../tests/test_web_agent.py#L3798) | 3798 | `"    }"` | — |
| [SRC-F725E90B2A-L003799](../../tests/test_web_agent.py#L3799) | 3799 | `"    collect_calls = []"` | — |
| [SRC-F725E90B2A-L003800](../../tests/test_web_agent.py#L3800) | 3800 | `""` | — |
| [SRC-F725E90B2A-L003801](../../tests/test_web_agent.py#L3801) | 3801 | `"    def plan(_question, _history):"` | — |
| [SRC-F725E90B2A-L003802](../../tests/test_web_agent.py#L3802) | 3802 | `"        return {"` | — |
| [SRC-F725E90B2A-L003803](../../tests/test_web_agent.py#L3803) | 3803 | `"            \"queries\": [_question],"` | — |
| [SRC-F725E90B2A-L003804](../../tests/test_web_agent.py#L3804) | 3804 | `"            \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L003805](../../tests/test_web_agent.py#L3805) | 3805 | `"            \"social_focus\": True,"` | — |
| [SRC-F725E90B2A-L003806](../../tests/test_web_agent.py#L3806) | 3806 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003807](../../tests/test_web_agent.py#L3807) | 3807 | `"            \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L003808](../../tests/test_web_agent.py#L3808) | 3808 | `"            \"platforms\": [\"reddit\"],"` | — |
| [SRC-F725E90B2A-L003809](../../tests/test_web_agent.py#L3809) | 3809 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003810](../../tests/test_web_agent.py#L3810) | 3810 | `"        }"` | — |
| [SRC-F725E90B2A-L003811](../../tests/test_web_agent.py#L3811) | 3811 | `""` | — |
| [SRC-F725E90B2A-L003812](../../tests/test_web_agent.py#L3812) | 3812 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L003813](../../tests/test_web_agent.py#L3813) | 3813 | `"        collect_calls.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L003814](../../tests/test_web_agent.py#L3814) | 3814 | `"        if len(collect_calls) == 1:"` | — |
| [SRC-F725E90B2A-L003815](../../tests/test_web_agent.py#L3815) | 3815 | `"            sources = initial_sources"` | — |
| [SRC-F725E90B2A-L003816](../../tests/test_web_agent.py#L3816) | 3816 | `"        else:"` | — |
| [SRC-F725E90B2A-L003817](../../tests/test_web_agent.py#L3817) | 3817 | `"            sources = [repair_candidate]"` | — |
| [SRC-F725E90B2A-L003818](../../tests/test_web_agent.py#L3818) | 3818 | `"        return sources, [], {"` | — |
| [SRC-F725E90B2A-L003819](../../tests/test_web_agent.py#L3819) | 3819 | `"            \"queries_planned\": len(research_plan.get(\"queries\", [])),"` | — |
| [SRC-F725E90B2A-L003820](../../tests/test_web_agent.py#L3820) | 3820 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L003821](../../tests/test_web_agent.py#L3821) | 3821 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L003822](../../tests/test_web_agent.py#L3822) | 3822 | `"            \"unique_sources\": len(sources),"` | — |
| [SRC-F725E90B2A-L003823](../../tests/test_web_agent.py#L3823) | 3823 | `"            \"pages_fetched\": len(sources),"` | — |
| [SRC-F725E90B2A-L003824](../../tests/test_web_agent.py#L3824) | 3824 | `"            \"providers_used\": [\"reddit\"] if len(collect_calls) == 1 else [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L003825](../../tests/test_web_agent.py#L3825) | 3825 | `"            \"provider_counts\": {},"` | — |
| [SRC-F725E90B2A-L003826](../../tests/test_web_agent.py#L3826) | 3826 | `"            \"platform_counts\": {},"` | — |
| [SRC-F725E90B2A-L003827](../../tests/test_web_agent.py#L3827) | 3827 | `"            \"social_direct_results\": len(sources) if len(collect_calls) == 1 else 0,"` | — |
| [SRC-F725E90B2A-L003828](../../tests/test_web_agent.py#L3828) | 3828 | `"            \"depth\": research_plan.get(\"depth\", \"deep\"),"` | — |
| [SRC-F725E90B2A-L003829](../../tests/test_web_agent.py#L3829) | 3829 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003830](../../tests/test_web_agent.py#L3830) | 3830 | `"        }"` | — |
| [SRC-F725E90B2A-L003831](../../tests/test_web_agent.py#L3831) | 3831 | `""` | — |
| [SRC-F725E90B2A-L003832](../../tests/test_web_agent.py#L3832) | 3832 | `"    monkeypatch.setattr(agent, \"_plan_search\", plan)"` | — |
| [SRC-F725E90B2A-L003833](../../tests/test_web_agent.py#L3833) | 3833 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L003834](../../tests/test_web_agent.py#L3834) | 3834 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda _query, _source: True)"` | — |
| [SRC-F725E90B2A-L003835](../../tests/test_web_agent.py#L3835) | 3835 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003836](../../tests/test_web_agent.py#L3836) | 3836 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003837](../../tests/test_web_agent.py#L3837) | 3837 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L003838](../../tests/test_web_agent.py#L3838) | 3838 | `"        lambda *args, **kwargs: ("` | — |
| [SRC-F725E90B2A-L003839](../../tests/test_web_agent.py#L3839) | 3839 | `"            \"السعر مناسب [المصدر 1]. الخصوصية جيدة [المصدر 2]. \""` | — |
| [SRC-F725E90B2A-L003840](../../tests/test_web_agent.py#L3840) | 3840 | `"            \"الاعتمادية مناسبة [المصدر 1].\""` | — |
| [SRC-F725E90B2A-L003841](../../tests/test_web_agent.py#L3841) | 3841 | `"        ),"` | — |
| [SRC-F725E90B2A-L003842](../../tests/test_web_agent.py#L3842) | 3842 | `"    )"` | — |
| [SRC-F725E90B2A-L003843](../../tests/test_web_agent.py#L3843) | 3843 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003844](../../tests/test_web_agent.py#L3844) | 3844 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003845](../../tests/test_web_agent.py#L3845) | 3845 | `"        \"_review_answer\","` | — |
| [SRC-F725E90B2A-L003846](../../tests/test_web_agent.py#L3846) | 3846 | `"        lambda _question, answer, _sources: answer,"` | — |
| [SRC-F725E90B2A-L003847](../../tests/test_web_agent.py#L3847) | 3847 | `"    )"` | — |
| [SRC-F725E90B2A-L003848](../../tests/test_web_agent.py#L3848) | 3848 | `""` | — |
| [SRC-F725E90B2A-L003849](../../tests/test_web_agent.py#L3849) | 3849 | `"    result = agent.answer(question, mode=\"social\")"` | — |
| [SRC-F725E90B2A-L003850](../../tests/test_web_agent.py#L3850) | 3850 | `"    report = result[\"search_report\"]"` | — |
| [SRC-F725E90B2A-L003851](../../tests/test_web_agent.py#L3851) | 3851 | `"    repair_guardrails = report[\"source_guardrails\"][\"criterion_gap_repair\"]"` | — |
| [SRC-F725E90B2A-L003852](../../tests/test_web_agent.py#L3852) | 3852 | `""` | — |
| [SRC-F725E90B2A-L003853](../../tests/test_web_agent.py#L3853) | 3853 | `"    assert len(collect_calls) >= 2"` | — |
| [SRC-F725E90B2A-L003854](../../tests/test_web_agent.py#L3854) | 3854 | `"    assert repair_guardrails[\"rejected_sources\"] >= 1"` | — |
| [SRC-F725E90B2A-L003855](../../tests/test_web_agent.py#L3855) | 3855 | `"    assert repair_guardrails[\"rejection_counts\"][\"not_a_social_platform_source\"] >= 1"` | — |
| [SRC-F725E90B2A-L003856](../../tests/test_web_agent.py#L3856) | 3856 | `"    assert all(\"reddit.com\" in source[\"url\"] for source in result[\"sources\"])"` | — |
| [SRC-F725E90B2A-L003857](../../tests/test_web_agent.py#L3857) | 3857 | `"    assert \"https://example.com/unrelated-repair\" not in {"` | — |
| [SRC-F725E90B2A-L003858](../../tests/test_web_agent.py#L3858) | 3858 | `"        source[\"url\"] for source in result[\"sources\"]"` | — |
| [SRC-F725E90B2A-L003859](../../tests/test_web_agent.py#L3859) | 3859 | `"    }"` | — |
| [SRC-F725E90B2A-L003860](../../tests/test_web_agent.py#L3860) | 3860 | `""` | — |
| [SRC-F725E90B2A-L003861](../../tests/test_web_agent.py#L3861) | 3861 | `"def test_local_answer_exposes_task_spec_without_claiming_search(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003862](../../tests/test_web_agent.py#L3862) | 3862 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003863](../../tests/test_web_agent.py#L3863) | 3863 | `"    result = agent.answer(\"أهلا\")"` | — |
| [SRC-F725E90B2A-L003864](../../tests/test_web_agent.py#L3864) | 3864 | `""` | — |
| [SRC-F725E90B2A-L003865](../../tests/test_web_agent.py#L3865) | 3865 | `"    task_understanding = result[\"task_understanding\"]"` | — |
| [SRC-F725E90B2A-L003866](../../tests/test_web_agent.py#L3866) | 3866 | `"    assert task_understanding[\"task_spec\"][\"schema\"] == \"omarai.task_spec.v1\""` | — |
| [SRC-F725E90B2A-L003867](../../tests/test_web_agent.py#L3867) | 3867 | `"    assert task_understanding[\"tool_execution\"][\"search_outcome\"] == \"not_assessed\""` | — |
| [SRC-F725E90B2A-L003868](../../tests/test_web_agent.py#L3868) | 3868 | `"    assert task_understanding[\"tool_execution\"][\"required_tools\"] == []"` | — |
| [SRC-F725E90B2A-L003869](../../tests/test_web_agent.py#L3869) | 3869 | `"    assert all("` | — |
| [SRC-F725E90B2A-L003870](../../tests/test_web_agent.py#L3870) | 3870 | `"        row[\"status\"] == \"not_required\""` | — |
| [SRC-F725E90B2A-L003871](../../tests/test_web_agent.py#L3871) | 3871 | `"        for row in task_understanding[\"tool_execution\"][\"tool_status_matrix\"]"` | — |
| [SRC-F725E90B2A-L003872](../../tests/test_web_agent.py#L3872) | 3872 | `"    )"` | — |
| [SRC-F725E90B2A-L003873](../../tests/test_web_agent.py#L3873) | 3873 | `"    assert task_understanding[\"actual_queries\"] == []"` | — |
| [SRC-F725E90B2A-L003874](../../tests/test_web_agent.py#L3874) | 3874 | `"    assert task_understanding[\"query_strategy_matrix\"] == []"` | — |
| [SRC-F725E90B2A-L003875](../../tests/test_web_agent.py#L3875) | 3875 | `"    assert task_understanding[\"search_was_attempted\"] is False"` | — |
| [SRC-F725E90B2A-L003876](../../tests/test_web_agent.py#L3876) | 3876 | `""` | — |
| [SRC-F725E90B2A-L003877](../../tests/test_web_agent.py#L3877) | 3877 | `"def test_official_site_without_target_clarifies_before_planning_or_search(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003878](../../tests/test_web_agent.py#L3878) | 3878 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003879](../../tests/test_web_agent.py#L3879) | 3879 | `""` | — |
| [SRC-F725E90B2A-L003880](../../tests/test_web_agent.py#L3880) | 3880 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003881](../../tests/test_web_agent.py#L3881) | 3881 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003882](../../tests/test_web_agent.py#L3882) | 3882 | `"        \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003883](../../tests/test_web_agent.py#L3883) | 3883 | `"        lambda *args, **kwargs: pytest.fail(\"Missing official-site target must be clarified before planning\"),"` | — |
| [SRC-F725E90B2A-L003884](../../tests/test_web_agent.py#L3884) | 3884 | `"    )"` | — |
| [SRC-F725E90B2A-L003885](../../tests/test_web_agent.py#L3885) | 3885 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003886](../../tests/test_web_agent.py#L3886) | 3886 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003887](../../tests/test_web_agent.py#L3887) | 3887 | `"        \"_collect_research\","` | — |
| [SRC-F725E90B2A-L003888](../../tests/test_web_agent.py#L3888) | 3888 | `"        lambda *args, **kwargs: pytest.fail(\"Missing official-site target must not invoke search\"),"` | — |
| [SRC-F725E90B2A-L003889](../../tests/test_web_agent.py#L3889) | 3889 | `"    )"` | — |
| [SRC-F725E90B2A-L003890](../../tests/test_web_agent.py#L3890) | 3890 | `""` | — |
| [SRC-F725E90B2A-L003891](../../tests/test_web_agent.py#L3891) | 3891 | `"    result = agent.answer(\"هات الموقع الرسمي\")"` | — |
| [SRC-F725E90B2A-L003892](../../tests/test_web_agent.py#L3892) | 3892 | `""` | — |
| [SRC-F725E90B2A-L003893](../../tests/test_web_agent.py#L3893) | 3893 | `"    assert result[\"intent_route\"] == \"CLARIFY\""` | — |
| [SRC-F725E90B2A-L003894](../../tests/test_web_agent.py#L3894) | 3894 | `"    assert result[\"kind\"] == \"clarification_needed\""` | — |
| [SRC-F725E90B2A-L003895](../../tests/test_web_agent.py#L3895) | 3895 | `"    assert \"اسم الجهة أو الشركة\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L003896](../../tests/test_web_agent.py#L3896) | 3896 | `"    assert result[\"search_attempted\"] is False"` | — |
| [SRC-F725E90B2A-L003897](../../tests/test_web_agent.py#L3897) | 3897 | `"    assert \"official_destination_target_entity\" in result[\"task_understanding\"][\"task_spec\"][\"missing_required_inputs\"]"` | — |
| [SRC-F725E90B2A-L003898](../../tests/test_web_agent.py#L3898) | 3898 | `""` | — |
| [SRC-F725E90B2A-L003899](../../tests/test_web_agent.py#L3899) | 3899 | `"def test_summary_without_source_clarifies_before_search(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003900](../../tests/test_web_agent.py#L3900) | 3900 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003901](../../tests/test_web_agent.py#L3901) | 3901 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003902](../../tests/test_web_agent.py#L3902) | 3902 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003903](../../tests/test_web_agent.py#L3903) | 3903 | `"        \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003904](../../tests/test_web_agent.py#L3904) | 3904 | `"        lambda *args, **kwargs: pytest.fail(\"Missing summary source must be clarified before planning\"),"` | — |
| [SRC-F725E90B2A-L003905](../../tests/test_web_agent.py#L3905) | 3905 | `"    )"` | — |
| [SRC-F725E90B2A-L003906](../../tests/test_web_agent.py#L3906) | 3906 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003907](../../tests/test_web_agent.py#L3907) | 3907 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003908](../../tests/test_web_agent.py#L3908) | 3908 | `"        \"_collect_research\","` | — |
| [SRC-F725E90B2A-L003909](../../tests/test_web_agent.py#L3909) | 3909 | `"        lambda *args, **kwargs: pytest.fail(\"Missing summary source must not invoke search\"),"` | — |
| [SRC-F725E90B2A-L003910](../../tests/test_web_agent.py#L3910) | 3910 | `"    )"` | — |
| [SRC-F725E90B2A-L003911](../../tests/test_web_agent.py#L3911) | 3911 | `""` | — |
| [SRC-F725E90B2A-L003912](../../tests/test_web_agent.py#L3912) | 3912 | `"    result = agent.answer(\"لخص\")"` | — |
| [SRC-F725E90B2A-L003913](../../tests/test_web_agent.py#L3913) | 3913 | `""` | — |
| [SRC-F725E90B2A-L003914](../../tests/test_web_agent.py#L3914) | 3914 | `"    assert result[\"intent_route\"] == \"CLARIFY\""` | — |
| [SRC-F725E90B2A-L003915](../../tests/test_web_agent.py#L3915) | 3915 | `"    assert \"أرسل النص\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L003916](../../tests/test_web_agent.py#L3916) | 3916 | `"    assert result[\"search_attempted\"] is False"` | — |
| [SRC-F725E90B2A-L003917](../../tests/test_web_agent.py#L3917) | 3917 | `"    assert \"summary_source_url_or_pasted_text\" in result[\"task_understanding\"][\"task_spec\"][\"missing_required_inputs\"]"` | — |
| [SRC-F725E90B2A-L003918](../../tests/test_web_agent.py#L3918) | 3918 | `""` | — |
| [SRC-F725E90B2A-L003919](../../tests/test_web_agent.py#L3919) | 3919 | `"def test_task_spec_controls_generation_context_without_becoming_evidence(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003920](../../tests/test_web_agent.py#L3920) | 3920 | `"    from agents.task_understanding import build_query_strategy_matrix, build_task_spec"` | — |
| [SRC-F725E90B2A-L003921](../../tests/test_web_agent.py#L3921) | 3921 | `""` | — |
| [SRC-F725E90B2A-L003922](../../tests/test_web_agent.py#L3922) | 3922 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003923](../../tests/test_web_agent.py#L3923) | 3923 | `"    captured = {}"` | — |
| [SRC-F725E90B2A-L003924](../../tests/test_web_agent.py#L3924) | 3924 | `""` | — |
| [SRC-F725E90B2A-L003925](../../tests/test_web_agent.py#L3925) | 3925 | `"    question = ("` | — |
| [SRC-F725E90B2A-L003926](../../tests/test_web_agent.py#L3926) | 3926 | `"        \"قارن السيارات الكهربائية في مصر من حيث السعر والضمان، \""` | — |
| [SRC-F725E90B2A-L003927](../../tests/test_web_agent.py#L3927) | 3927 | `"        \"اشرح ببساطة مع أمثلة وروابط مباشرة\""` | — |
| [SRC-F725E90B2A-L003928](../../tests/test_web_agent.py#L3928) | 3928 | `"    )"` | — |
| [SRC-F725E90B2A-L003929](../../tests/test_web_agent.py#L3929) | 3929 | `"    task_spec = build_task_spec("` | — |
| [SRC-F725E90B2A-L003930](../../tests/test_web_agent.py#L3930) | 3930 | `"        question,"` | — |
| [SRC-F725E90B2A-L003931](../../tests/test_web_agent.py#L3931) | 3931 | `"        mode=\"deep\","` | — |
| [SRC-F725E90B2A-L003932](../../tests/test_web_agent.py#L3932) | 3932 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-F725E90B2A-L003933](../../tests/test_web_agent.py#L3933) | 3933 | `"    )"` | — |
| [SRC-F725E90B2A-L003934](../../tests/test_web_agent.py#L3934) | 3934 | `"    initial_queries = [compact_search_query(question)]"` | — |
| [SRC-F725E90B2A-L003935](../../tests/test_web_agent.py#L3935) | 3935 | `"    matrix = build_query_strategy_matrix("` | — |
| [SRC-F725E90B2A-L003936](../../tests/test_web_agent.py#L3936) | 3936 | `"        question,"` | — |
| [SRC-F725E90B2A-L003937](../../tests/test_web_agent.py#L3937) | 3937 | `"        task_spec,"` | — |
| [SRC-F725E90B2A-L003938](../../tests/test_web_agent.py#L3938) | 3938 | `"        initial_queries,"` | — |
| [SRC-F725E90B2A-L003939](../../tests/test_web_agent.py#L3939) | 3939 | `"        limit=4,"` | — |
| [SRC-F725E90B2A-L003940](../../tests/test_web_agent.py#L3940) | 3940 | `"        compact_fn=compact_search_query,"` | — |
| [SRC-F725E90B2A-L003941](../../tests/test_web_agent.py#L3941) | 3941 | `"    )"` | — |
| [SRC-F725E90B2A-L003942](../../tests/test_web_agent.py#L3942) | 3942 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L003943](../../tests/test_web_agent.py#L3943) | 3943 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L003944](../../tests/test_web_agent.py#L3944) | 3944 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003945](../../tests/test_web_agent.py#L3945) | 3945 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003946](../../tests/test_web_agent.py#L3946) | 3946 | `"        \"queries\": [row[\"query\"] for row in matrix],"` | — |
| [SRC-F725E90B2A-L003947](../../tests/test_web_agent.py#L3947) | 3947 | `"        \"dialogue_context\": {},"` | — |
| [SRC-F725E90B2A-L003948](../../tests/test_web_agent.py#L3948) | 3948 | `"        \"intent_route\": \"WEB_DEEP\","` | — |
| [SRC-F725E90B2A-L003949](../../tests/test_web_agent.py#L3949) | 3949 | `"        \"task_spec\": task_spec,"` | — |
| [SRC-F725E90B2A-L003950](../../tests/test_web_agent.py#L3950) | 3950 | `"        \"query_strategy_matrix\": matrix,"` | — |
| [SRC-F725E90B2A-L003951](../../tests/test_web_agent.py#L3951) | 3951 | `"    }"` | — |
| [SRC-F725E90B2A-L003952](../../tests/test_web_agent.py#L3952) | 3952 | `""` | — |
| [SRC-F725E90B2A-L003953](../../tests/test_web_agent.py#L3953) | 3953 | `"    def fake_completion(messages, **kwargs):"` | — |
| [SRC-F725E90B2A-L003954](../../tests/test_web_agent.py#L3954) | 3954 | `"        captured[\"messages\"] = messages"` | — |
| [SRC-F725E90B2A-L003955](../../tests/test_web_agent.py#L3955) | 3955 | `"        captured[\"kwargs\"] = kwargs"` | — |
| [SRC-F725E90B2A-L003956](../../tests/test_web_agent.py#L3956) | 3956 | `"        return \"إجابة اختبارية مرتبطة بالأدلة.\""` | — |
| [SRC-F725E90B2A-L003957](../../tests/test_web_agent.py#L3957) | 3957 | `""` | — |
| [SRC-F725E90B2A-L003958](../../tests/test_web_agent.py#L3958) | 3958 | `"    monkeypatch.setattr(agent, \"_request_completion\", fake_completion)"` | — |
| [SRC-F725E90B2A-L003959](../../tests/test_web_agent.py#L3959) | 3959 | `""` | — |
| [SRC-F725E90B2A-L003960](../../tests/test_web_agent.py#L3960) | 3960 | `"    answer = agent._generate("` | — |
| [SRC-F725E90B2A-L003961](../../tests/test_web_agent.py#L3961) | 3961 | `"        question,"` | — |
| [SRC-F725E90B2A-L003962](../../tests/test_web_agent.py#L3962) | 3962 | `"        [],"` | — |
| [SRC-F725E90B2A-L003963](../../tests/test_web_agent.py#L3963) | 3963 | `"        [sample_source(0)],"` | — |
| [SRC-F725E90B2A-L003964](../../tests/test_web_agent.py#L3964) | 3964 | `"        None,"` | — |
| [SRC-F725E90B2A-L003965](../../tests/test_web_agent.py#L3965) | 3965 | `"        research_plan=plan,"` | — |
| [SRC-F725E90B2A-L003966](../../tests/test_web_agent.py#L3966) | 3966 | `"        search_report={"` | — |
| [SRC-F725E90B2A-L003967](../../tests/test_web_agent.py#L3967) | 3967 | `"            \"queries_planned\": len(plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L003968](../../tests/test_web_agent.py#L3968) | 3968 | `"            \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L003969](../../tests/test_web_agent.py#L3969) | 3969 | `"            \"pages_fetched\": 1,"` | — |
| [SRC-F725E90B2A-L003970](../../tests/test_web_agent.py#L3970) | 3970 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L003971](../../tests/test_web_agent.py#L3971) | 3971 | `"        },"` | — |
| [SRC-F725E90B2A-L003972](../../tests/test_web_agent.py#L3972) | 3972 | `"    )"` | — |
| [SRC-F725E90B2A-L003973](../../tests/test_web_agent.py#L3973) | 3973 | `""` | — |
| [SRC-F725E90B2A-L003974](../../tests/test_web_agent.py#L3974) | 3974 | `"    prompt = \"\\n\".join("` | — |
| [SRC-F725E90B2A-L003975](../../tests/test_web_agent.py#L3975) | 3975 | `"        message.get(\"content\", \"\")"` | — |
| [SRC-F725E90B2A-L003976](../../tests/test_web_agent.py#L3976) | 3976 | `"        for message in captured[\"messages\"]"` | — |
| [SRC-F725E90B2A-L003977](../../tests/test_web_agent.py#L3977) | 3977 | `"        if isinstance(message, dict)"` | — |
| [SRC-F725E90B2A-L003978](../../tests/test_web_agent.py#L3978) | 3978 | `"    )"` | — |
| [SRC-F725E90B2A-L003979](../../tests/test_web_agent.py#L3979) | 3979 | `"    assert answer == \"إجابة اختبارية مرتبطة بالأدلة.\""` | — |
| [SRC-F725E90B2A-L003980](../../tests/test_web_agent.py#L3980) | 3980 | `"    assert \"task_planning_context\" in prompt"` | — |
| [SRC-F725E90B2A-L003981](../../tests/test_web_agent.py#L3981) | 3981 | `"    assert \"explicit_aspects\" in prompt"` | — |
| [SRC-F725E90B2A-L003982](../../tests/test_web_agent.py#L3982) | 3982 | `"    assert \"output_preferences\" in prompt"` | — |
| [SRC-F725E90B2A-L003983](../../tests/test_web_agent.py#L3983) | 3983 | `"    assert \"beginner_friendly_requested\" in prompt"` | — |
| [SRC-F725E90B2A-L003984](../../tests/test_web_agent.py#L3984) | 3984 | `"    assert \"reasoning_guidance\" in prompt"` | — |
| [SRC-F725E90B2A-L003985](../../tests/test_web_agent.py#L3985) | 3985 | `"    assert \"decision_matrix\" in prompt"` | — |
| [SRC-F725E90B2A-L003986](../../tests/test_web_agent.py#L3986) | 3986 | `"    assert \"قسّم المقارنة إلى كل معيار صريح\" in prompt"` | — |
| [SRC-F725E90B2A-L003987](../../tests/test_web_agent.py#L3987) | 3987 | `"    assert \"وحّد العملة والوحدات\" in prompt"` | — |
| [SRC-F725E90B2A-L003988](../../tests/test_web_agent.py#L3988) | 3988 | `"    assert \"query_strategy_matrix\" in prompt"` | — |
| [SRC-F725E90B2A-L003989](../../tests/test_web_agent.py#L3989) | 3989 | `"    assert \"الأولوية لكلام المستخدم الحالي\" in prompt"` | — |
| [SRC-F725E90B2A-L003990](../../tests/test_web_agent.py#L3990) | 3990 | `"    assert \"الاستعلامات المخططة فقط\" in prompt"` | — |
| [SRC-F725E90B2A-L003991](../../tests/test_web_agent.py#L3991) | 3991 | `""` | — |
| [SRC-F725E90B2A-L003992](../../tests/test_web_agent.py#L3992) | 3992 | `"def test_bilingual_relevance_handles_arabic_attached_clitics_without_lowering_floor():"` | — |
| [SRC-F725E90B2A-L003993](../../tests/test_web_agent.py#L3993) | 3993 | `"    query = \"أهم استخدامات الذكاء الاصطناعي للشركات الصغيرة؟\""` | — |
| [SRC-F725E90B2A-L003994](../../tests/test_web_agent.py#L3994) | 3994 | `"    evidence = \"AI use cases for small businesses\""` | — |
| [SRC-F725E90B2A-L003995](../../tests/test_web_agent.py#L3995) | 3995 | `"    assert _minimum_relevance_ratio(query) == 0.20"` | — |
| [SRC-F725E90B2A-L003996](../../tests/test_web_agent.py#L3996) | 3996 | `"    assert _relevance_ratio(query, evidence) >= 0.80"` | — |
| [SRC-F725E90B2A-L003997](../../tests/test_web_agent.py#L3997) | 3997 | `""` | — |
| [SRC-F725E90B2A-L003998](../../tests/test_web_agent.py#L3998) | 3998 | `"def test_search_evidence_matching_keeps_distinct_concepts_as_the_ratio_denominator():"` | — |
| [SRC-F725E90B2A-L003999](../../tests/test_web_agent.py#L3999) | 3999 | `"    query = \"استخدامات الذكاء الاصطناعي للشركات الصغيرة\""` | — |
| [SRC-F725E90B2A-L004000](../../tests/test_web_agent.py#L4000) | 4000 | `"    on_topic = \"AI use cases for small businesses\""` | — |
| [SRC-F725E90B2A-L004001](../../tests/test_web_agent.py#L4001) | 4001 | `"    weak = \"AI tools for personal photo editing\""` | — |
| [SRC-F725E90B2A-L004002](../../tests/test_web_agent.py#L4002) | 4002 | `"    assert _relevance_ratio(query, on_topic) > _relevance_ratio(query, weak)"` | — |
| [SRC-F725E90B2A-L004003](../../tests/test_web_agent.py#L4003) | 4003 | `"    assert _relevance_ratio(query, weak) < _minimum_relevance_ratio(query)"` | — |
| [SRC-F725E90B2A-L004004](../../tests/test_web_agent.py#L4004) | 4004 | `""` | — |
| [SRC-F725E90B2A-L004005](../../tests/test_web_agent.py#L4005) | 4005 | `"def test_bilingual_relevance_matches_english_queries_to_arabic_source_text():"` | — |
| [SRC-F725E90B2A-L004006](../../tests/test_web_agent.py#L4006) | 4006 | `"    query = \"AI use cases for small businesses in Egypt\""` | — |
| [SRC-F725E90B2A-L004007](../../tests/test_web_agent.py#L4007) | 4007 | `"    evidence = \"استخدامات الذكاء الاصطناعي للشركات الصغيرة في مصر\""` | — |
| [SRC-F725E90B2A-L004008](../../tests/test_web_agent.py#L4008) | 4008 | `"    assert _relevance_ratio(query, evidence) >= 0.80"` | — |
| [SRC-F725E90B2A-L004009](../../tests/test_web_agent.py#L4009) | 4009 | `""` | — |
| [SRC-F725E90B2A-L004010](../../tests/test_web_agent.py#L4010) | 4010 | `""` | — |
| [SRC-F725E90B2A-L004011](../../tests/test_web_agent.py#L4011) | 4011 | `"def test_completion_diagnostics_failure_does_not_break_answer(monkeypatch):"` | — |
| [SRC-F725E90B2A-L004012](../../tests/test_web_agent.py#L4012) | 4012 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L004013](../../tests/test_web_agent.py#L4013) | 4013 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L004014](../../tests/test_web_agent.py#L4014) | 4014 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L004015](../../tests/test_web_agent.py#L4015) | 4015 | `"        agent,"` | — |
| [SRC-F725E90B2A-L004016](../../tests/test_web_agent.py#L4016) | 4016 | `"        \"_plan_search\","` | — |
| [SRC-F725E90B2A-L004017](../../tests/test_web_agent.py#L4017) | 4017 | `"        lambda question, history: {"` | — |
| [SRC-F725E90B2A-L004018](../../tests/test_web_agent.py#L4018) | 4018 | `"            \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L004019](../../tests/test_web_agent.py#L4019) | 4019 | `"            \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L004020](../../tests/test_web_agent.py#L4020) | 4020 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L004021](../../tests/test_web_agent.py#L4021) | 4021 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L004022](../../tests/test_web_agent.py#L4022) | 4022 | `"            \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L004023](../../tests/test_web_agent.py#L4023) | 4023 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L004024](../../tests/test_web_agent.py#L4024) | 4024 | `"            \"coverage_targets\": [],"` | — |
| [SRC-F725E90B2A-L004025](../../tests/test_web_agent.py#L4025) | 4025 | `"        },"` | — |
| [SRC-F725E90B2A-L004026](../../tests/test_web_agent.py#L4026) | 4026 | `"    )"` | — |
| [SRC-F725E90B2A-L004027](../../tests/test_web_agent.py#L4027) | 4027 | `"    monkeypatch.setattr(agent, \"_collect_research\", lambda plan: ("` | — |
| [SRC-F725E90B2A-L004028](../../tests/test_web_agent.py#L4028) | 4028 | `"        [sample_source(0), sample_source(1)], [], {"` | — |
| [SRC-F725E90B2A-L004029](../../tests/test_web_agent.py#L4029) | 4029 | `"            \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L004030](../../tests/test_web_agent.py#L4030) | 4030 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L004031](../../tests/test_web_agent.py#L4031) | 4031 | `"            \"query_results\": [{\"query\": plan[\"queries\"][0], \"results\": 2}],"` | — |
| [SRC-F725E90B2A-L004032](../../tests/test_web_agent.py#L4032) | 4032 | `"            \"unique_sources\": 2,"` | — |
| [SRC-F725E90B2A-L004033](../../tests/test_web_agent.py#L4033) | 4033 | `"            \"pages_fetched\": 2,"` | — |
| [SRC-F725E90B2A-L004034](../../tests/test_web_agent.py#L4034) | 4034 | `"            \"providers_used\": [\"test\"],"` | — |
| [SRC-F725E90B2A-L004035](../../tests/test_web_agent.py#L4035) | 4035 | `"            \"provider_diagnostics\": [],"` | — |
| [SRC-F725E90B2A-L004036](../../tests/test_web_agent.py#L4036) | 4036 | `"        }"` | — |
| [SRC-F725E90B2A-L004037](../../tests/test_web_agent.py#L4037) | 4037 | `"    ))"` | — |
| [SRC-F725E90B2A-L004038](../../tests/test_web_agent.py#L4038) | 4038 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L004039](../../tests/test_web_agent.py#L4039) | 4039 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L004040](../../tests/test_web_agent.py#L4040) | 4040 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"إجابة اختبارية [المصدر 1].\")"` | — |
| [SRC-F725E90B2A-L004041](../../tests/test_web_agent.py#L4041) | 4041 | `""` | — |
| [SRC-F725E90B2A-L004042](../../tests/test_web_agent.py#L4042) | 4042 | `"    def fail_diagnostics(_result):"` | — |
| [SRC-F725E90B2A-L004043](../../tests/test_web_agent.py#L4043) | 4043 | `"        raise RuntimeError(\"diagnostics are optional\")"` | — |
| [SRC-F725E90B2A-L004044](../../tests/test_web_agent.py#L4044) | 4044 | `""` | — |
| [SRC-F725E90B2A-L004045](../../tests/test_web_agent.py#L4045) | 4045 | `"    monkeypatch.setattr(\"agents.web_agent.build_research_completion\", fail_diagnostics)"` | — |
| [SRC-F725E90B2A-L004046](../../tests/test_web_agent.py#L4046) | 4046 | `"    result = agent.answer(\"قارن هذه التقنية\")"` | — |
| [SRC-F725E90B2A-L004047](../../tests/test_web_agent.py#L4047) | 4047 | `"    assert result[\"answer\"] == \"إجابة اختبارية [المصدر 1].\""` | — |
| [SRC-F725E90B2A-L004048](../../tests/test_web_agent.py#L4048) | 4048 | `"    assert result[\"research_completion\"][\"status\"] == \"diagnostics_not_computed\""` | — |
| [SRC-F725E90B2A-L004049](../../tests/test_web_agent.py#L4049) | 4049 | `"    assert any(\"لا يُعد ذلك دليلًا على اكتمال البحث\" in warning for warning in result[\"warnings\"])"` | — |
| [SRC-F725E90B2A-L004050](../../tests/test_web_agent.py#L4050) | 4050 | `""` | — |
| [SRC-F725E90B2A-L004051](../../tests/test_web_agent.py#L4051) | 4051 | `""` | — |
| [SRC-F725E90B2A-L004052](../../tests/test_web_agent.py#L4052) | 4052 | `""` | — |
| [SRC-F725E90B2A-L004053](../../tests/test_web_agent.py#L4053) | 4053 | `"def test_model_request_transport_disables_automatic_redirects(monkeypatch):"` | — |
| [SRC-F725E90B2A-L004054](../../tests/test_web_agent.py#L4054) | 4054 | `"    from agents import web_agent"` | — |
| [SRC-F725E90B2A-L004055](../../tests/test_web_agent.py#L4055) | 4055 | `""` | — |
| [SRC-F725E90B2A-L004056](../../tests/test_web_agent.py#L4056) | 4056 | `"    observed = {}"` | — |
| [SRC-F725E90B2A-L004057](../../tests/test_web_agent.py#L4057) | 4057 | `"    sentinel = object()"` | — |
| [SRC-F725E90B2A-L004058](../../tests/test_web_agent.py#L4058) | 4058 | `""` | — |
| [SRC-F725E90B2A-L004059](../../tests/test_web_agent.py#L4059) | 4059 | `"    class FakeOpener:"` | — |
| [SRC-F725E90B2A-L004060](../../tests/test_web_agent.py#L4060) | 4060 | `"        def open(self, request, *, timeout):"` | — |
| [SRC-F725E90B2A-L004061](../../tests/test_web_agent.py#L4061) | 4061 | `"            observed[\"request\"] = request"` | — |
| [SRC-F725E90B2A-L004062](../../tests/test_web_agent.py#L4062) | 4062 | `"            observed[\"timeout\"] = timeout"` | — |
| [SRC-F725E90B2A-L004063](../../tests/test_web_agent.py#L4063) | 4063 | `"            return sentinel"` | — |
| [SRC-F725E90B2A-L004064](../../tests/test_web_agent.py#L4064) | 4064 | `""` | — |
| [SRC-F725E90B2A-L004065](../../tests/test_web_agent.py#L4065) | 4065 | `"    def fake_build_opener(*handlers):"` | — |
| [SRC-F725E90B2A-L004066](../../tests/test_web_agent.py#L4066) | 4066 | `"        observed[\"handlers\"] = handlers"` | — |
| [SRC-F725E90B2A-L004067](../../tests/test_web_agent.py#L4067) | 4067 | `"        return FakeOpener()"` | — |
| [SRC-F725E90B2A-L004068](../../tests/test_web_agent.py#L4068) | 4068 | `""` | — |
| [SRC-F725E90B2A-L004069](../../tests/test_web_agent.py#L4069) | 4069 | `"    monkeypatch.setattr(web_agent.urllib.request, \"build_opener\", fake_build_opener)"` | — |
| [SRC-F725E90B2A-L004070](../../tests/test_web_agent.py#L4070) | 4070 | `"    request = web_agent.urllib.request.Request("` | — |
| [SRC-F725E90B2A-L004071](../../tests/test_web_agent.py#L4071) | 4071 | `"        \"https://provider.example/v1/chat/completions\","` | — |
| [SRC-F725E90B2A-L004072](../../tests/test_web_agent.py#L4072) | 4072 | `"        data=b\"{}\","` | — |
| [SRC-F725E90B2A-L004073](../../tests/test_web_agent.py#L4073) | 4073 | `"        headers={\"Authorization\": \"Bearer test-only-token\"},"` | — |
| [SRC-F725E90B2A-L004074](../../tests/test_web_agent.py#L4074) | 4074 | `"        method=\"POST\","` | — |
| [SRC-F725E90B2A-L004075](../../tests/test_web_agent.py#L4075) | 4075 | `"    )"` | — |
| [SRC-F725E90B2A-L004076](../../tests/test_web_agent.py#L4076) | 4076 | `""` | — |
| [SRC-F725E90B2A-L004077](../../tests/test_web_agent.py#L4077) | 4077 | `"    assert web_agent._open_model_request(request, timeout=3.5) is sentinel"` | — |
| [SRC-F725E90B2A-L004078](../../tests/test_web_agent.py#L4078) | 4078 | `"    assert observed[\"request\"] is request"` | — |
| [SRC-F725E90B2A-L004079](../../tests/test_web_agent.py#L4079) | 4079 | `"    assert observed[\"timeout\"] == 3.5"` | — |
| [SRC-F725E90B2A-L004080](../../tests/test_web_agent.py#L4080) | 4080 | `"    assert observed[\"handlers\"] == (web_agent._NoRedirectHandler,)"` | — |
| [SRC-F725E90B2A-L004081](../../tests/test_web_agent.py#L4081) | 4081 | `""` | — |
| [SRC-F725E90B2A-L004082](../../tests/test_web_agent.py#L4082) | 4082 | `"    handler = web_agent._NoRedirectHandler()"` | — |
| [SRC-F725E90B2A-L004083](../../tests/test_web_agent.py#L4083) | 4083 | `"    redirected = handler.redirect_request("` | — |
| [SRC-F725E90B2A-L004084](../../tests/test_web_agent.py#L4084) | 4084 | `"        request,"` | — |
| [SRC-F725E90B2A-L004085](../../tests/test_web_agent.py#L4085) | 4085 | `"        None,"` | — |
| [SRC-F725E90B2A-L004086](../../tests/test_web_agent.py#L4086) | 4086 | `"        302,"` | — |
| [SRC-F725E90B2A-L004087](../../tests/test_web_agent.py#L4087) | 4087 | `"        \"Found\","` | — |
| [SRC-F725E90B2A-L004088](../../tests/test_web_agent.py#L4088) | 4088 | `"        {},"` | — |
| [SRC-F725E90B2A-L004089](../../tests/test_web_agent.py#L4089) | 4089 | `"        \"https://attacker.example/collect\","` | — |
| [SRC-F725E90B2A-L004090](../../tests/test_web_agent.py#L4090) | 4090 | `"    )"` | — |
| [SRC-F725E90B2A-L004091](../../tests/test_web_agent.py#L4091) | 4091 | `"    assert redirected is None"` | — |
| [SRC-F725E90B2A-L004092](../../tests/test_web_agent.py#L4092) | 4092 | `""` | — |
| [SRC-F725E90B2A-L004093](../../tests/test_web_agent.py#L4093) | 4093 | `""` | — |
| [SRC-F725E90B2A-L004094](../../tests/test_web_agent.py#L4094) | 4094 | `"def test_openrouter_web_search_does_not_match_spoofed_hostname(monkeypatch):"` | — |
| [SRC-F725E90B2A-L004095](../../tests/test_web_agent.py#L4095) | 4095 | `"    monkeypatch.setenv(\"OMARAI_OPENROUTER_WEB_SEARCH\", \"1\")"` | — |
| [SRC-F725E90B2A-L004096](../../tests/test_web_agent.py#L4096) | 4096 | `"    monkeypatch.setenv("` | — |
| [SRC-F725E90B2A-L004097](../../tests/test_web_agent.py#L4097) | 4097 | `"        \"OMARAI_LLM_BASE_URL\","` | — |
| [SRC-F725E90B2A-L004098](../../tests/test_web_agent.py#L4098) | 4098 | `"        \"https://openrouter.ai.attacker.example/api/v1\","` | — |
| [SRC-F725E90B2A-L004099](../../tests/test_web_agent.py#L4099) | 4099 | `"    )"` | — |
| [SRC-F725E90B2A-L004100](../../tests/test_web_agent.py#L4100) | 4100 | `""` | — |
| [SRC-F725E90B2A-L004101](../../tests/test_web_agent.py#L4101) | 4101 | `"    assert WebAgent().openrouter_web_search_enabled is False"` | — |
| [SRC-F725E90B2A-L004102](../../tests/test_web_agent.py#L4102) | 4102 | `""` | — |
| [SRC-F725E90B2A-L004103](../../tests/test_web_agent.py#L4103) | 4103 | `""` | — |
| [SRC-F725E90B2A-L004104](../../tests/test_web_agent.py#L4104) | 4104 | `""` | — |
| [SRC-F725E90B2A-L004105](../../tests/test_web_agent.py#L4105) | 4105 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L004106](../../tests/test_web_agent.py#L4106) | 4106 | `"    \"address,family\","` | — |
| [SRC-F725E90B2A-L004107](../../tests/test_web_agent.py#L4107) | 4107 | `"    ["` | — |
| [SRC-F725E90B2A-L004108](../../tests/test_web_agent.py#L4108) | 4108 | `"        (\"127.0.0.1\", __import__(\"socket\").AF_INET),"` | — |
| [SRC-F725E90B2A-L004109](../../tests/test_web_agent.py#L4109) | 4109 | `"        (\"169.254.169.254\", __import__(\"socket\").AF_INET),"` | — |
| [SRC-F725E90B2A-L004110](../../tests/test_web_agent.py#L4110) | 4110 | `"        (\"::1\", __import__(\"socket\").AF_INET6),"` | — |
| [SRC-F725E90B2A-L004111](../../tests/test_web_agent.py#L4111) | 4111 | `"        (\"fe80::1\", __import__(\"socket\").AF_INET6),"` | — |
| [SRC-F725E90B2A-L004112](../../tests/test_web_agent.py#L4112) | 4112 | `"        (\"fd00::1\", __import__(\"socket\").AF_INET6),"` | — |
| [SRC-F725E90B2A-L004113](../../tests/test_web_agent.py#L4113) | 4113 | `"    ],"` | — |
| [SRC-F725E90B2A-L004114](../../tests/test_web_agent.py#L4114) | 4114 | `")"` | — |
| [SRC-F725E90B2A-L004115](../../tests/test_web_agent.py#L4115) | 4115 | `"def test_public_ip_literals_rejects_non_global_ipv4_and_ipv6_answers("` | — |
| [SRC-F725E90B2A-L004116](../../tests/test_web_agent.py#L4116) | 4116 | `"    monkeypatch, address, family"` | — |
| [SRC-F725E90B2A-L004117](../../tests/test_web_agent.py#L4117) | 4117 | `"):"` | — |
| [SRC-F725E90B2A-L004118](../../tests/test_web_agent.py#L4118) | 4118 | `"    import socket"` | — |
| [SRC-F725E90B2A-L004119](../../tests/test_web_agent.py#L4119) | 4119 | `""` | — |
| [SRC-F725E90B2A-L004120](../../tests/test_web_agent.py#L4120) | 4120 | `"    from agents import web_agent"` | — |
| [SRC-F725E90B2A-L004121](../../tests/test_web_agent.py#L4121) | 4121 | `""` | — |
| [SRC-F725E90B2A-L004122](../../tests/test_web_agent.py#L4122) | 4122 | `"    answers = ["` | — |
| [SRC-F725E90B2A-L004123](../../tests/test_web_agent.py#L4123) | 4123 | `"        (family, socket.SOCK_STREAM, socket.IPPROTO_TCP, \"\", (address, 80))"` | — |
| [SRC-F725E90B2A-L004124](../../tests/test_web_agent.py#L4124) | 4124 | `"    ]"` | — |
| [SRC-F725E90B2A-L004125](../../tests/test_web_agent.py#L4125) | 4125 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L004126](../../tests/test_web_agent.py#L4126) | 4126 | `"        web_agent.socket,"` | — |
| [SRC-F725E90B2A-L004127](../../tests/test_web_agent.py#L4127) | 4127 | `"        \"getaddrinfo\","` | — |
| [SRC-F725E90B2A-L004128](../../tests/test_web_agent.py#L4128) | 4128 | `"        lambda host, port, type: answers,"` | — |
| [SRC-F725E90B2A-L004129](../../tests/test_web_agent.py#L4129) | 4129 | `"    )"` | — |
| [SRC-F725E90B2A-L004130](../../tests/test_web_agent.py#L4130) | 4130 | `""` | — |
| [SRC-F725E90B2A-L004131](../../tests/test_web_agent.py#L4131) | 4131 | `"    assert web_agent._public_ip_literals(\"untrusted.example\") is None"` | — |
| [SRC-F725E90B2A-L004132](../../tests/test_web_agent.py#L4132) | 4132 | `""` | — |
| [SRC-F725E90B2A-L004133](../../tests/test_web_agent.py#L4133) | 4133 | `""` | — |
| [SRC-F725E90B2A-L004134](../../tests/test_web_agent.py#L4134) | 4134 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L004135](../../tests/test_web_agent.py#L4135) | 4135 | `"    \"url\","` | — |
| [SRC-F725E90B2A-L004136](../../tests/test_web_agent.py#L4136) | 4136 | `"    ["` | — |
| [SRC-F725E90B2A-L004137](../../tests/test_web_agent.py#L4137) | 4137 | `"        \"http://127.0.0.1/private\","` | — |
| [SRC-F725E90B2A-L004138](../../tests/test_web_agent.py#L4138) | 4138 | `"        \"http://169.254.169.254/latest/meta-data/\","` | — |
| [SRC-F725E90B2A-L004139](../../tests/test_web_agent.py#L4139) | 4139 | `"        \"http://[::1]/private\","` | — |
| [SRC-F725E90B2A-L004140](../../tests/test_web_agent.py#L4140) | 4140 | `"        \"http://[fe80::1]/private\","` | — |
| [SRC-F725E90B2A-L004141](../../tests/test_web_agent.py#L4141) | 4141 | `"        \"http://[fd00::1]/private\","` | — |
| [SRC-F725E90B2A-L004142](../../tests/test_web_agent.py#L4142) | 4142 | `"        \"file:///etc/passwd\","` | — |
| [SRC-F725E90B2A-L004143](../../tests/test_web_agent.py#L4143) | 4143 | `"        \"https://user:password@example.com/private\","` | — |
| [SRC-F725E90B2A-L004144](../../tests/test_web_agent.py#L4144) | 4144 | `"        \"https://example.com:8443/private\","` | — |
| [SRC-F725E90B2A-L004145](../../tests/test_web_agent.py#L4145) | 4145 | `"    ],"` | — |
| [SRC-F725E90B2A-L004146](../../tests/test_web_agent.py#L4146) | 4146 | `")"` | — |
| [SRC-F725E90B2A-L004147](../../tests/test_web_agent.py#L4147) | 4147 | `"def test_public_http_url_rejects_non_public_or_unsafe_targets(url):"` | — |
| [SRC-F725E90B2A-L004148](../../tests/test_web_agent.py#L4148) | 4148 | `"    from agents.web_agent import _public_http_url"` | — |
| [SRC-F725E90B2A-L004149](../../tests/test_web_agent.py#L4149) | 4149 | `""` | — |
| [SRC-F725E90B2A-L004150](../../tests/test_web_agent.py#L4150) | 4150 | `"    assert _public_http_url(url) is None"` | — |
| [SRC-F725E90B2A-L004151](../../tests/test_web_agent.py#L4151) | 4151 | `""` | — |
| [SRC-F725E90B2A-L004152](../../tests/test_web_agent.py#L4152) | 4152 | `""` | — |
| [SRC-F725E90B2A-L004153](../../tests/test_web_agent.py#L4153) | 4153 | `"def test_fetch_page_enforces_streamed_byte_limit_when_content_length_lies(monkeypatch):"` | — |
| [SRC-F725E90B2A-L004154](../../tests/test_web_agent.py#L4154) | 4154 | `"    from contextlib import contextmanager"` | — |
| [SRC-F725E90B2A-L004155](../../tests/test_web_agent.py#L4155) | 4155 | `""` | — |
| [SRC-F725E90B2A-L004156](../../tests/test_web_agent.py#L4156) | 4156 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L004157](../../tests/test_web_agent.py#L4157) | 4157 | `""` | — |
| [SRC-F725E90B2A-L004158](../../tests/test_web_agent.py#L4158) | 4158 | `"    from agents import web_agent"` | — |
| [SRC-F725E90B2A-L004159](../../tests/test_web_agent.py#L4159) | 4159 | `""` | — |
| [SRC-F725E90B2A-L004160](../../tests/test_web_agent.py#L4160) | 4160 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L004161](../../tests/test_web_agent.py#L4161) | 4161 | `"        web_agent, \"_public_ip_literals\", lambda _host: [\"93.184.216.34\"]"` | — |
| [SRC-F725E90B2A-L004162](../../tests/test_web_agent.py#L4162) | 4162 | `"    )"` | — |
| [SRC-F725E90B2A-L004163](../../tests/test_web_agent.py#L4163) | 4163 | `"    chunks_yielded = []"` | — |
| [SRC-F725E90B2A-L004164](../../tests/test_web_agent.py#L4164) | 4164 | `""` | — |
| [SRC-F725E90B2A-L004165](../../tests/test_web_agent.py#L4165) | 4165 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L004166](../../tests/test_web_agent.py#L4166) | 4166 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L004167](../../tests/test_web_agent.py#L4167) | 4167 | `"        encoding = \"utf-8\""` | — |
| [SRC-F725E90B2A-L004168](../../tests/test_web_agent.py#L4168) | 4168 | `""` | — |
| [SRC-F725E90B2A-L004169](../../tests/test_web_agent.py#L4169) | 4169 | `"        def __init__(self):"` | — |
| [SRC-F725E90B2A-L004170](../../tests/test_web_agent.py#L4170) | 4170 | `"            self.headers = {"` | — |
| [SRC-F725E90B2A-L004171](../../tests/test_web_agent.py#L4171) | 4171 | `"                \"content-type\": \"text/plain; charset=utf-8\","` | — |
| [SRC-F725E90B2A-L004172](../../tests/test_web_agent.py#L4172) | 4172 | `"                # Deliberately under-reports the actual streamed body length."` | — |
| [SRC-F725E90B2A-L004173](../../tests/test_web_agent.py#L4173) | 4173 | `"                \"content-length\": \"1\","` | — |
| [SRC-F725E90B2A-L004174](../../tests/test_web_agent.py#L4174) | 4174 | `"            }"` | — |
| [SRC-F725E90B2A-L004175](../../tests/test_web_agent.py#L4175) | 4175 | `""` | — |
| [SRC-F725E90B2A-L004176](../../tests/test_web_agent.py#L4176) | 4176 | `"        def iter_bytes(self):"` | — |
| [SRC-F725E90B2A-L004177](../../tests/test_web_agent.py#L4177) | 4177 | `"            chunks = ("` | — |
| [SRC-F725E90B2A-L004178](../../tests/test_web_agent.py#L4178) | 4178 | `"                b\"A\" * web_agent.MAX_PAGE_BYTES,"` | — |
| [SRC-F725E90B2A-L004179](../../tests/test_web_agent.py#L4179) | 4179 | `"                b\"B\" * 32,"` | — |
| [SRC-F725E90B2A-L004180](../../tests/test_web_agent.py#L4180) | 4180 | `"                b\"C\" * 32,"` | — |
| [SRC-F725E90B2A-L004181](../../tests/test_web_agent.py#L4181) | 4181 | `"            )"` | — |
| [SRC-F725E90B2A-L004182](../../tests/test_web_agent.py#L4182) | 4182 | `"            for chunk in chunks:"` | — |
| [SRC-F725E90B2A-L004183](../../tests/test_web_agent.py#L4183) | 4183 | `"                chunks_yielded.append(len(chunk))"` | — |
| [SRC-F725E90B2A-L004184](../../tests/test_web_agent.py#L4184) | 4184 | `"                yield chunk"` | — |
| [SRC-F725E90B2A-L004185](../../tests/test_web_agent.py#L4185) | 4185 | `""` | — |
| [SRC-F725E90B2A-L004186](../../tests/test_web_agent.py#L4186) | 4186 | `"    @contextmanager"` | — |
| [SRC-F725E90B2A-L004187](../../tests/test_web_agent.py#L4187) | 4187 | `"    def fake_stream(self, method, url, **kwargs):"` | — |
| [SRC-F725E90B2A-L004188](../../tests/test_web_agent.py#L4188) | 4188 | `"        assert method == \"GET\""` | — |
| [SRC-F725E90B2A-L004189](../../tests/test_web_agent.py#L4189) | 4189 | `"        assert str(url) == \"https://93.184.216.34/large.txt\""` | — |
| [SRC-F725E90B2A-L004190](../../tests/test_web_agent.py#L4190) | 4190 | `"        yield FakeResponse()"` | — |
| [SRC-F725E90B2A-L004191](../../tests/test_web_agent.py#L4191) | 4191 | `""` | — |
| [SRC-F725E90B2A-L004192](../../tests/test_web_agent.py#L4192) | 4192 | `"    class FakeClient:"` | — |
| [SRC-F725E90B2A-L004193](../../tests/test_web_agent.py#L4193) | 4193 | `"        def __init__(self, **kwargs):"` | — |
| [SRC-F725E90B2A-L004194](../../tests/test_web_agent.py#L4194) | 4194 | `"            self.options = kwargs"` | — |
| [SRC-F725E90B2A-L004195](../../tests/test_web_agent.py#L4195) | 4195 | `""` | — |
| [SRC-F725E90B2A-L004196](../../tests/test_web_agent.py#L4196) | 4196 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L004197](../../tests/test_web_agent.py#L4197) | 4197 | `"            return self"` | — |
| [SRC-F725E90B2A-L004198](../../tests/test_web_agent.py#L4198) | 4198 | `""` | — |
| [SRC-F725E90B2A-L004199](../../tests/test_web_agent.py#L4199) | 4199 | `"        def __exit__(self, *_args):"` | — |
| [SRC-F725E90B2A-L004200](../../tests/test_web_agent.py#L4200) | 4200 | `"            return False"` | — |
| [SRC-F725E90B2A-L004201](../../tests/test_web_agent.py#L4201) | 4201 | `""` | — |
| [SRC-F725E90B2A-L004202](../../tests/test_web_agent.py#L4202) | 4202 | `"        stream = fake_stream"` | — |
| [SRC-F725E90B2A-L004203](../../tests/test_web_agent.py#L4203) | 4203 | `""` | — |
| [SRC-F725E90B2A-L004204](../../tests/test_web_agent.py#L4204) | 4204 | `"    monkeypatch.setattr(httpx, \"Client\", FakeClient)"` | — |
| [SRC-F725E90B2A-L004205](../../tests/test_web_agent.py#L4205) | 4205 | `"    result = web_agent.WebAgent()._fetch_page(\"https://example.com/large.txt\")"` | — |
| [SRC-F725E90B2A-L004206](../../tests/test_web_agent.py#L4206) | 4206 | `""` | — |
| [SRC-F725E90B2A-L004207](../../tests/test_web_agent.py#L4207) | 4207 | `"    assert result.status == \"partial_extraction\""` | — |
| [SRC-F725E90B2A-L004208](../../tests/test_web_agent.py#L4208) | 4208 | `"    assert len(result[1]) <= web_agent.MAX_PAGE_TEXT_CHARS"` | — |
| [SRC-F725E90B2A-L004209](../../tests/test_web_agent.py#L4209) | 4209 | `"    # The reader stops as soon as the byte cap is crossed; it never asks for chunk 3."` | — |
| [SRC-F725E90B2A-L004210](../../tests/test_web_agent.py#L4210) | 4210 | `"    assert chunks_yielded == [web_agent.MAX_PAGE_BYTES, 32]"` | — |
| [SRC-F725E90B2A-L004211](../../tests/test_web_agent.py#L4211) | 4211 | `""` | — |
| [SRC-F725E90B2A-L004212](../../tests/test_web_agent.py#L4212) | 4212 | `""` | — |
| [SRC-F725E90B2A-L004213](../../tests/test_web_agent.py#L4213) | 4213 | `""` | — |
| [SRC-F725E90B2A-L004214](../../tests/test_web_agent.py#L4214) | 4214 | `"@pytest.mark.parametrize(\"field\", [\"title\", \"snippet\", \"page_text\"])"` | — |
| [SRC-F725E90B2A-L004215](../../tests/test_web_agent.py#L4215) | 4215 | `"def test_generate_keeps_title_snippet_and_page_text_untrusted(field, monkeypatch):"` | — |
| [SRC-F725E90B2A-L004216](../../tests/test_web_agent.py#L4216) | 4216 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L004217](../../tests/test_web_agent.py#L4217) | 4217 | `"    source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L004218](../../tests/test_web_agent.py#L4218) | 4218 | `"    injected_text = f\"INJECTED INSTRUCTION FROM UNTRUSTED {field.upper()}\""` | — |
| [SRC-F725E90B2A-L004219](../../tests/test_web_agent.py#L4219) | 4219 | `"    source[field] = injected_text"` | — |
| [SRC-F725E90B2A-L004220](../../tests/test_web_agent.py#L4220) | 4220 | `"    if field == \"snippet\":"` | — |
| [SRC-F725E90B2A-L004221](../../tests/test_web_agent.py#L4221) | 4221 | `"        source[\"page_text\"] = \"\""` | — |
| [SRC-F725E90B2A-L004222](../../tests/test_web_agent.py#L4222) | 4222 | `"    captured = {}"` | — |
| [SRC-F725E90B2A-L004223](../../tests/test_web_agent.py#L4223) | 4223 | `""` | — |
| [SRC-F725E90B2A-L004224](../../tests/test_web_agent.py#L4224) | 4224 | `"    def fake_completion(messages, **kwargs):"` | — |
| [SRC-F725E90B2A-L004225](../../tests/test_web_agent.py#L4225) | 4225 | `"        captured[\"messages\"] = messages"` | — |
| [SRC-F725E90B2A-L004226](../../tests/test_web_agent.py#L4226) | 4226 | `"        return \"إجابة اختبارية.\""` | — |
| [SRC-F725E90B2A-L004227](../../tests/test_web_agent.py#L4227) | 4227 | `""` | — |
| [SRC-F725E90B2A-L004228](../../tests/test_web_agent.py#L4228) | 4228 | `"    monkeypatch.setattr(agent, \"_request_completion\", fake_completion)"` | — |
| [SRC-F725E90B2A-L004229](../../tests/test_web_agent.py#L4229) | 4229 | `"    answer = agent._generate("` | — |
| [SRC-F725E90B2A-L004230](../../tests/test_web_agent.py#L4230) | 4230 | `"        question=\"ما الذي يقوله المصدر؟\","` | — |
| [SRC-F725E90B2A-L004231](../../tests/test_web_agent.py#L4231) | 4231 | `"        history=[],"` | — |
| [SRC-F725E90B2A-L004232](../../tests/test_web_agent.py#L4232) | 4232 | `"        sources=[source],"` | — |
| [SRC-F725E90B2A-L004233](../../tests/test_web_agent.py#L4233) | 4233 | `"        search_warning=None,"` | — |
| [SRC-F725E90B2A-L004234](../../tests/test_web_agent.py#L4234) | 4234 | `"        research_plan={\"depth\": \"standard\", \"queries\": [\"ما الذي يقوله المصدر؟\"]},"` | — |
| [SRC-F725E90B2A-L004235](../../tests/test_web_agent.py#L4235) | 4235 | `"        search_report={},"` | — |
| [SRC-F725E90B2A-L004236](../../tests/test_web_agent.py#L4236) | 4236 | `"    )"` | — |
| [SRC-F725E90B2A-L004237](../../tests/test_web_agent.py#L4237) | 4237 | `""` | — |
| [SRC-F725E90B2A-L004238](../../tests/test_web_agent.py#L4238) | 4238 | `"    messages = captured[\"messages\"]"` | — |
| [SRC-F725E90B2A-L004239](../../tests/test_web_agent.py#L4239) | 4239 | `"    system_content = \"\\n\".join("` | — |
| [SRC-F725E90B2A-L004240](../../tests/test_web_agent.py#L4240) | 4240 | `"        message[\"content\"] for message in messages if message[\"role\"] == \"system\""` | — |
| [SRC-F725E90B2A-L004241](../../tests/test_web_agent.py#L4241) | 4241 | `"    )"` | — |
| [SRC-F725E90B2A-L004242](../../tests/test_web_agent.py#L4242) | 4242 | `"    user_contents = ["` | — |
| [SRC-F725E90B2A-L004243](../../tests/test_web_agent.py#L4243) | 4243 | `"        message[\"content\"] for message in messages if message[\"role\"] == \"user\""` | — |
| [SRC-F725E90B2A-L004244](../../tests/test_web_agent.py#L4244) | 4244 | `"    ]"` | — |
| [SRC-F725E90B2A-L004245](../../tests/test_web_agent.py#L4245) | 4245 | `""` | — |
| [SRC-F725E90B2A-L004246](../../tests/test_web_agent.py#L4246) | 4246 | `"    assert answer == \"إجابة اختبارية.\""` | — |
| [SRC-F725E90B2A-L004247](../../tests/test_web_agent.py#L4247) | 4247 | `"    assert injected_text not in system_content"` | — |
| [SRC-F725E90B2A-L004248](../../tests/test_web_agent.py#L4248) | 4248 | `"    assert any(injected_text in value for value in user_contents)"` | — |
| [SRC-F725E90B2A-L004249](../../tests/test_web_agent.py#L4249) | 4249 | `""` | — |
| [SRC-F725E90B2A-L004250](../../tests/test_web_agent.py#L4250) | 4250 | `""` | — |
| [SRC-F725E90B2A-L004251](../../tests/test_web_agent.py#L4251) | 4251 | `"@pytest.mark.parametrize(\"field\", [\"title\", \"snippet\", \"page_text\"])"` | — |
| [SRC-F725E90B2A-L004252](../../tests/test_web_agent.py#L4252) | 4252 | `"def test_review_keeps_title_snippet_and_page_text_untrusted(field, monkeypatch):"` | — |
| [SRC-F725E90B2A-L004253](../../tests/test_web_agent.py#L4253) | 4253 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L004254](../../tests/test_web_agent.py#L4254) | 4254 | `"    source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L004255](../../tests/test_web_agent.py#L4255) | 4255 | `"    injected_text = f\"INJECTED REVIEW INSTRUCTION FROM UNTRUSTED {field.upper()}\""` | — |
| [SRC-F725E90B2A-L004256](../../tests/test_web_agent.py#L4256) | 4256 | `"    source[field] = injected_text"` | — |
| [SRC-F725E90B2A-L004257](../../tests/test_web_agent.py#L4257) | 4257 | `"    if field == \"snippet\":"` | — |
| [SRC-F725E90B2A-L004258](../../tests/test_web_agent.py#L4258) | 4258 | `"        source[\"page_text\"] = \"\""` | — |
| [SRC-F725E90B2A-L004259](../../tests/test_web_agent.py#L4259) | 4259 | `"    captured = {}"` | — |
| [SRC-F725E90B2A-L004260](../../tests/test_web_agent.py#L4260) | 4260 | `""` | — |
| [SRC-F725E90B2A-L004261](../../tests/test_web_agent.py#L4261) | 4261 | `"    def fake_completion(messages, **kwargs):"` | — |
| [SRC-F725E90B2A-L004262](../../tests/test_web_agent.py#L4262) | 4262 | `"        captured[\"messages\"] = messages"` | — |
| [SRC-F725E90B2A-L004263](../../tests/test_web_agent.py#L4263) | 4263 | `"        return \"<<<OMARAI_FINAL_ANSWER>>>تم تدقيق الإجابة.<<<END_OMARAI_FINAL_ANSWER>>>\""` | — |
| [SRC-F725E90B2A-L004264](../../tests/test_web_agent.py#L4264) | 4264 | `""` | — |
| [SRC-F725E90B2A-L004265](../../tests/test_web_agent.py#L4265) | 4265 | `"    monkeypatch.setattr(agent, \"_request_completion\", fake_completion)"` | — |
| [SRC-F725E90B2A-L004266](../../tests/test_web_agent.py#L4266) | 4266 | `"    answer = agent._review_answer("` | — |
| [SRC-F725E90B2A-L004267](../../tests/test_web_agent.py#L4267) | 4267 | `"        question=\"ما الذي يقوله المصدر؟\","` | — |
| [SRC-F725E90B2A-L004268](../../tests/test_web_agent.py#L4268) | 4268 | `"        answer=\"مسودة إجابة تحتاج التحقق.\","` | — |
| [SRC-F725E90B2A-L004269](../../tests/test_web_agent.py#L4269) | 4269 | `"        sources=[source],"` | — |
| [SRC-F725E90B2A-L004270](../../tests/test_web_agent.py#L4270) | 4270 | `"    )"` | — |
| [SRC-F725E90B2A-L004271](../../tests/test_web_agent.py#L4271) | 4271 | `""` | — |
| [SRC-F725E90B2A-L004272](../../tests/test_web_agent.py#L4272) | 4272 | `"    messages = captured[\"messages\"]"` | — |
| [SRC-F725E90B2A-L004273](../../tests/test_web_agent.py#L4273) | 4273 | `"    system_content = \"\\n\".join("` | — |
| [SRC-F725E90B2A-L004274](../../tests/test_web_agent.py#L4274) | 4274 | `"        message[\"content\"] for message in messages if message[\"role\"] == \"system\""` | — |
| [SRC-F725E90B2A-L004275](../../tests/test_web_agent.py#L4275) | 4275 | `"    )"` | — |
| [SRC-F725E90B2A-L004276](../../tests/test_web_agent.py#L4276) | 4276 | `"    user_contents = ["` | — |
| [SRC-F725E90B2A-L004277](../../tests/test_web_agent.py#L4277) | 4277 | `"        message[\"content\"] for message in messages if message[\"role\"] == \"user\""` | — |
| [SRC-F725E90B2A-L004278](../../tests/test_web_agent.py#L4278) | 4278 | `"    ]"` | — |
| [SRC-F725E90B2A-L004279](../../tests/test_web_agent.py#L4279) | 4279 | `""` | — |
| [SRC-F725E90B2A-L004280](../../tests/test_web_agent.py#L4280) | 4280 | `"    assert answer == \"تم تدقيق الإجابة.\""` | — |
| [SRC-F725E90B2A-L004281](../../tests/test_web_agent.py#L4281) | 4281 | `"    assert injected_text not in system_content"` | — |
| [SRC-F725E90B2A-L004282](../../tests/test_web_agent.py#L4282) | 4282 | `"    assert any(injected_text in value for value in user_contents)"` | — |
| [SRC-F725E90B2A-L004283](../../tests/test_web_agent.py#L4283) | 4283 | `""` | — |
| [SRC-F725E90B2A-L004284](../../tests/test_web_agent.py#L4284) | 4284 | `""` | — |
| [SRC-F725E90B2A-L004285](../../tests/test_web_agent.py#L4285) | 4285 | `""` | — |
| [SRC-F725E90B2A-L004286](../../tests/test_web_agent.py#L4286) | 4286 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L004287](../../tests/test_web_agent.py#L4287) | 4287 | `"    \"url\","` | — |
| [SRC-F725E90B2A-L004288](../../tests/test_web_agent.py#L4288) | 4288 | `"    ["` | — |
| [SRC-F725E90B2A-L004289](../../tests/test_web_agent.py#L4289) | 4289 | `"        \"https://api.example.test/v1\","` | — |
| [SRC-F725E90B2A-L004290](../../tests/test_web_agent.py#L4290) | 4290 | `"        \"http://localhost:11434/v1\","` | — |
| [SRC-F725E90B2A-L004291](../../tests/test_web_agent.py#L4291) | 4291 | `"        \"http://127.0.0.1:8080/v1\","` | — |
| [SRC-F725E90B2A-L004292](../../tests/test_web_agent.py#L4292) | 4292 | `"        \"http://[::1]:8000/v1\","` | — |
| [SRC-F725E90B2A-L004293](../../tests/test_web_agent.py#L4293) | 4293 | `"    ],"` | — |
