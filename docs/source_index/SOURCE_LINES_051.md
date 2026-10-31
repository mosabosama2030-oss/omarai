# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **051**
- سجلات الأسطر: **800**
- النطاق: SRC-F725E90B2A-L003600 إلى SRC-DE7EABE998-L000357
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-F725E90B2A — [tests/test_web_agent.py](../../tests/test_web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-F725E90B2A-L003600](../../tests/test_web_agent.py#L3600) | 3600 | `"    assert calls  # initial research, plus bounded repair where applicable"` | — |
| [SRC-F725E90B2A-L003601](../../tests/test_web_agent.py#L3601) | 3601 | `"    assert result[\"kind\"] == \"insufficient_evidence\""` | — |
| [SRC-F725E90B2A-L003602](../../tests/test_web_agent.py#L3602) | 3602 | `"    assert result[\"sources\"] == []"` | — |
| [SRC-F725E90B2A-L003603](../../tests/test_web_agent.py#L3603) | 3603 | `"    guardrails = result[\"search_report\"][\"source_guardrails\"]"` | — |
| [SRC-F725E90B2A-L003604](../../tests/test_web_agent.py#L3604) | 3604 | `"    assert guardrails[\"initial\"][\"official_government_domain_required\"] is True"` | — |
| [SRC-F725E90B2A-L003605](../../tests/test_web_agent.py#L3605) | 3605 | `"    assert guardrails[\"initial\"][\"rejection_counts\"] == {"` | — |
| [SRC-F725E90B2A-L003606](../../tests/test_web_agent.py#L3606) | 3606 | `"        \"not_an_official_government_domain\": 1"` | — |
| [SRC-F725E90B2A-L003607](../../tests/test_web_agent.py#L3607) | 3607 | `"    }"` | — |
| [SRC-F725E90B2A-L003608](../../tests/test_web_agent.py#L3608) | 3608 | `"    assert guardrails[\"final\"][\"accepted_sources\"] == 0"` | — |
| [SRC-F725E90B2A-L003609](../../tests/test_web_agent.py#L3609) | 3609 | `"    assert result[\"search_report\"][\"usable_sources_after_filtering\"] == 0"` | — |
| [SRC-F725E90B2A-L003610](../../tests/test_web_agent.py#L3610) | 3610 | `""` | — |
| [SRC-F725E90B2A-L003611](../../tests/test_web_agent.py#L3611) | 3611 | `"def test_criterion_gap_repair_cannot_reintroduce_non_social_source(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003612](../../tests/test_web_agent.py#L3612) | 3612 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003613](../../tests/test_web_agent.py#L3613) | 3613 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L003614](../../tests/test_web_agent.py#L3614) | 3614 | `"    question = ("` | — |
| [SRC-F725E90B2A-L003615](../../tests/test_web_agent.py#L3615) | 3615 | `"        \"قارن بين خدمتين من حيث السعر والخصوصية والاعتمادية \""` | — |
| [SRC-F725E90B2A-L003616](../../tests/test_web_agent.py#L3616) | 3616 | `"        \"واعرض آراء وتجارب المستخدمين\""` | — |
| [SRC-F725E90B2A-L003617](../../tests/test_web_agent.py#L3617) | 3617 | `"    )"` | — |
| [SRC-F725E90B2A-L003618](../../tests/test_web_agent.py#L3618) | 3618 | `"    initial_sources = ["` | — |
| [SRC-F725E90B2A-L003619](../../tests/test_web_agent.py#L3619) | 3619 | `"        {"` | — |
| [SRC-F725E90B2A-L003620](../../tests/test_web_agent.py#L3620) | 3620 | `"            **sample_source(0),"` | — |
| [SRC-F725E90B2A-L003621](../../tests/test_web_agent.py#L3621) | 3621 | `"            \"url\": \"https://www.reddit.com/r/example/comments/1\","` | — |
| [SRC-F725E90B2A-L003622](../../tests/test_web_agent.py#L3622) | 3622 | `"            \"domain\": \"reddit.com\","` | — |
| [SRC-F725E90B2A-L003623](../../tests/test_web_agent.py#L3623) | 3623 | `"            \"title\": \"مناقشة تجارب المستخدمين للخدمتين\","` | — |
| [SRC-F725E90B2A-L003624](../../tests/test_web_agent.py#L3624) | 3624 | `"            \"snippet\": \"تجارب وآراء مستخدمين حول الخدمتين\","` | — |
| [SRC-F725E90B2A-L003625](../../tests/test_web_agent.py#L3625) | 3625 | `"            \"page_text\": \"تجارب وآراء مستخدمين حول الخدمتين\","` | — |
| [SRC-F725E90B2A-L003626](../../tests/test_web_agent.py#L3626) | 3626 | `"            \"platform\": \"reddit\","` | — |
| [SRC-F725E90B2A-L003627](../../tests/test_web_agent.py#L3627) | 3627 | `"            \"providers\": [\"reddit\"],"` | — |
| [SRC-F725E90B2A-L003628](../../tests/test_web_agent.py#L3628) | 3628 | `"        },"` | — |
| [SRC-F725E90B2A-L003629](../../tests/test_web_agent.py#L3629) | 3629 | `"        {"` | — |
| [SRC-F725E90B2A-L003630](../../tests/test_web_agent.py#L3630) | 3630 | `"            **sample_source(1),"` | — |
| [SRC-F725E90B2A-L003631](../../tests/test_web_agent.py#L3631) | 3631 | `"            \"url\": \"https://www.reddit.com/r/example/comments/2\","` | — |
| [SRC-F725E90B2A-L003632](../../tests/test_web_agent.py#L3632) | 3632 | `"            \"domain\": \"reddit.com\","` | — |
| [SRC-F725E90B2A-L003633](../../tests/test_web_agent.py#L3633) | 3633 | `"            \"title\": \"مناقشة أخرى عن الخدمتين\","` | — |
| [SRC-F725E90B2A-L003634](../../tests/test_web_agent.py#L3634) | 3634 | `"            \"snippet\": \"مناقشة وتجارب مستخدمين حول الخدمتين\","` | — |
| [SRC-F725E90B2A-L003635](../../tests/test_web_agent.py#L3635) | 3635 | `"            \"page_text\": \"مناقشة وتجارب مستخدمين حول الخدمتين\","` | — |
| [SRC-F725E90B2A-L003636](../../tests/test_web_agent.py#L3636) | 3636 | `"            \"platform\": \"reddit\","` | — |
| [SRC-F725E90B2A-L003637](../../tests/test_web_agent.py#L3637) | 3637 | `"            \"providers\": [\"reddit\"],"` | — |
| [SRC-F725E90B2A-L003638](../../tests/test_web_agent.py#L3638) | 3638 | `"        },"` | — |
| [SRC-F725E90B2A-L003639](../../tests/test_web_agent.py#L3639) | 3639 | `"    ]"` | — |
| [SRC-F725E90B2A-L003640](../../tests/test_web_agent.py#L3640) | 3640 | `"    repair_candidate = {"` | — |
| [SRC-F725E90B2A-L003641](../../tests/test_web_agent.py#L3641) | 3641 | `"        **sample_source(2),"` | — |
| [SRC-F725E90B2A-L003642](../../tests/test_web_agent.py#L3642) | 3642 | `"        \"url\": \"https://example.com/unrelated-repair\","` | — |
| [SRC-F725E90B2A-L003643](../../tests/test_web_agent.py#L3643) | 3643 | `"        \"domain\": \"example.com\","` | — |
| [SRC-F725E90B2A-L003644](../../tests/test_web_agent.py#L3644) | 3644 | `"        \"title\": \"معلومات عن الخدمة\","` | — |
| [SRC-F725E90B2A-L003645](../../tests/test_web_agent.py#L3645) | 3645 | `"        \"snippet\": \"معلومات عامة عن الخدمة\","` | — |
| [SRC-F725E90B2A-L003646](../../tests/test_web_agent.py#L3646) | 3646 | `"        \"page_text\": \"معلومات عامة عن الخدمة\","` | — |
| [SRC-F725E90B2A-L003647](../../tests/test_web_agent.py#L3647) | 3647 | `"        \"providers\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L003648](../../tests/test_web_agent.py#L3648) | 3648 | `"    }"` | — |
| [SRC-F725E90B2A-L003649](../../tests/test_web_agent.py#L3649) | 3649 | `"    collect_calls = []"` | — |
| [SRC-F725E90B2A-L003650](../../tests/test_web_agent.py#L3650) | 3650 | `""` | — |
| [SRC-F725E90B2A-L003651](../../tests/test_web_agent.py#L3651) | 3651 | `"    def plan(_question, _history):"` | — |
| [SRC-F725E90B2A-L003652](../../tests/test_web_agent.py#L3652) | 3652 | `"        return {"` | — |
| [SRC-F725E90B2A-L003653](../../tests/test_web_agent.py#L3653) | 3653 | `"            \"queries\": [_question],"` | — |
| [SRC-F725E90B2A-L003654](../../tests/test_web_agent.py#L3654) | 3654 | `"            \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L003655](../../tests/test_web_agent.py#L3655) | 3655 | `"            \"social_focus\": True,"` | — |
| [SRC-F725E90B2A-L003656](../../tests/test_web_agent.py#L3656) | 3656 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003657](../../tests/test_web_agent.py#L3657) | 3657 | `"            \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L003658](../../tests/test_web_agent.py#L3658) | 3658 | `"            \"platforms\": [\"reddit\"],"` | — |
| [SRC-F725E90B2A-L003659](../../tests/test_web_agent.py#L3659) | 3659 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003660](../../tests/test_web_agent.py#L3660) | 3660 | `"        }"` | — |
| [SRC-F725E90B2A-L003661](../../tests/test_web_agent.py#L3661) | 3661 | `""` | — |
| [SRC-F725E90B2A-L003662](../../tests/test_web_agent.py#L3662) | 3662 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L003663](../../tests/test_web_agent.py#L3663) | 3663 | `"        collect_calls.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L003664](../../tests/test_web_agent.py#L3664) | 3664 | `"        if len(collect_calls) == 1:"` | — |
| [SRC-F725E90B2A-L003665](../../tests/test_web_agent.py#L3665) | 3665 | `"            sources = initial_sources"` | — |
| [SRC-F725E90B2A-L003666](../../tests/test_web_agent.py#L3666) | 3666 | `"        else:"` | — |
| [SRC-F725E90B2A-L003667](../../tests/test_web_agent.py#L3667) | 3667 | `"            sources = [repair_candidate]"` | — |
| [SRC-F725E90B2A-L003668](../../tests/test_web_agent.py#L3668) | 3668 | `"        return sources, [], {"` | — |
| [SRC-F725E90B2A-L003669](../../tests/test_web_agent.py#L3669) | 3669 | `"            \"queries_planned\": len(research_plan.get(\"queries\", [])),"` | — |
| [SRC-F725E90B2A-L003670](../../tests/test_web_agent.py#L3670) | 3670 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L003671](../../tests/test_web_agent.py#L3671) | 3671 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L003672](../../tests/test_web_agent.py#L3672) | 3672 | `"            \"unique_sources\": len(sources),"` | — |
| [SRC-F725E90B2A-L003673](../../tests/test_web_agent.py#L3673) | 3673 | `"            \"pages_fetched\": len(sources),"` | — |
| [SRC-F725E90B2A-L003674](../../tests/test_web_agent.py#L3674) | 3674 | `"            \"providers_used\": [\"reddit\"] if len(collect_calls) == 1 else [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L003675](../../tests/test_web_agent.py#L3675) | 3675 | `"            \"provider_counts\": {},"` | — |
| [SRC-F725E90B2A-L003676](../../tests/test_web_agent.py#L3676) | 3676 | `"            \"platform_counts\": {},"` | — |
| [SRC-F725E90B2A-L003677](../../tests/test_web_agent.py#L3677) | 3677 | `"            \"social_direct_results\": len(sources) if len(collect_calls) == 1 else 0,"` | — |
| [SRC-F725E90B2A-L003678](../../tests/test_web_agent.py#L3678) | 3678 | `"            \"depth\": research_plan.get(\"depth\", \"deep\"),"` | — |
| [SRC-F725E90B2A-L003679](../../tests/test_web_agent.py#L3679) | 3679 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003680](../../tests/test_web_agent.py#L3680) | 3680 | `"        }"` | — |
| [SRC-F725E90B2A-L003681](../../tests/test_web_agent.py#L3681) | 3681 | `""` | — |
| [SRC-F725E90B2A-L003682](../../tests/test_web_agent.py#L3682) | 3682 | `"    monkeypatch.setattr(agent, \"_plan_search\", plan)"` | — |
| [SRC-F725E90B2A-L003683](../../tests/test_web_agent.py#L3683) | 3683 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L003684](../../tests/test_web_agent.py#L3684) | 3684 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda _query, _source: True)"` | — |
| [SRC-F725E90B2A-L003685](../../tests/test_web_agent.py#L3685) | 3685 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003686](../../tests/test_web_agent.py#L3686) | 3686 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003687](../../tests/test_web_agent.py#L3687) | 3687 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L003688](../../tests/test_web_agent.py#L3688) | 3688 | `"        lambda *args, **kwargs: ("` | — |
| [SRC-F725E90B2A-L003689](../../tests/test_web_agent.py#L3689) | 3689 | `"            \"السعر مناسب [المصدر 1]. الخصوصية جيدة [المصدر 2]. \""` | — |
| [SRC-F725E90B2A-L003690](../../tests/test_web_agent.py#L3690) | 3690 | `"            \"الاعتمادية مناسبة [المصدر 1].\""` | — |
| [SRC-F725E90B2A-L003691](../../tests/test_web_agent.py#L3691) | 3691 | `"        ),"` | — |
| [SRC-F725E90B2A-L003692](../../tests/test_web_agent.py#L3692) | 3692 | `"    )"` | — |
| [SRC-F725E90B2A-L003693](../../tests/test_web_agent.py#L3693) | 3693 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003694](../../tests/test_web_agent.py#L3694) | 3694 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003695](../../tests/test_web_agent.py#L3695) | 3695 | `"        \"_review_answer\","` | — |
| [SRC-F725E90B2A-L003696](../../tests/test_web_agent.py#L3696) | 3696 | `"        lambda _question, answer, _sources: answer,"` | — |
| [SRC-F725E90B2A-L003697](../../tests/test_web_agent.py#L3697) | 3697 | `"    )"` | — |
| [SRC-F725E90B2A-L003698](../../tests/test_web_agent.py#L3698) | 3698 | `""` | — |
| [SRC-F725E90B2A-L003699](../../tests/test_web_agent.py#L3699) | 3699 | `"    result = agent.answer(question, mode=\"social\")"` | — |
| [SRC-F725E90B2A-L003700](../../tests/test_web_agent.py#L3700) | 3700 | `"    report = result[\"search_report\"]"` | — |
| [SRC-F725E90B2A-L003701](../../tests/test_web_agent.py#L3701) | 3701 | `"    repair_guardrails = report[\"source_guardrails\"][\"criterion_gap_repair\"]"` | — |
| [SRC-F725E90B2A-L003702](../../tests/test_web_agent.py#L3702) | 3702 | `""` | — |
| [SRC-F725E90B2A-L003703](../../tests/test_web_agent.py#L3703) | 3703 | `"    assert len(collect_calls) >= 2"` | — |
| [SRC-F725E90B2A-L003704](../../tests/test_web_agent.py#L3704) | 3704 | `"    assert repair_guardrails[\"rejected_sources\"] >= 1"` | — |
| [SRC-F725E90B2A-L003705](../../tests/test_web_agent.py#L3705) | 3705 | `"    assert repair_guardrails[\"rejection_counts\"][\"not_a_social_platform_source\"] >= 1"` | — |
| [SRC-F725E90B2A-L003706](../../tests/test_web_agent.py#L3706) | 3706 | `"    assert all(\"reddit.com\" in source[\"url\"] for source in result[\"sources\"])"` | — |
| [SRC-F725E90B2A-L003707](../../tests/test_web_agent.py#L3707) | 3707 | `"    assert \"https://example.com/unrelated-repair\" not in {"` | — |
| [SRC-F725E90B2A-L003708](../../tests/test_web_agent.py#L3708) | 3708 | `"        source[\"url\"] for source in result[\"sources\"]"` | — |
| [SRC-F725E90B2A-L003709](../../tests/test_web_agent.py#L3709) | 3709 | `"    }"` | — |
| [SRC-F725E90B2A-L003710](../../tests/test_web_agent.py#L3710) | 3710 | `""` | — |
| [SRC-F725E90B2A-L003711](../../tests/test_web_agent.py#L3711) | 3711 | `"def test_local_answer_exposes_task_spec_without_claiming_search(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003712](../../tests/test_web_agent.py#L3712) | 3712 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003713](../../tests/test_web_agent.py#L3713) | 3713 | `"    result = agent.answer(\"أهلا\")"` | — |
| [SRC-F725E90B2A-L003714](../../tests/test_web_agent.py#L3714) | 3714 | `""` | — |
| [SRC-F725E90B2A-L003715](../../tests/test_web_agent.py#L3715) | 3715 | `"    task_understanding = result[\"task_understanding\"]"` | — |
| [SRC-F725E90B2A-L003716](../../tests/test_web_agent.py#L3716) | 3716 | `"    assert task_understanding[\"task_spec\"][\"schema\"] == \"omarai.task_spec.v1\""` | — |
| [SRC-F725E90B2A-L003717](../../tests/test_web_agent.py#L3717) | 3717 | `"    assert task_understanding[\"tool_execution\"][\"search_outcome\"] == \"not_assessed\""` | — |
| [SRC-F725E90B2A-L003718](../../tests/test_web_agent.py#L3718) | 3718 | `"    assert task_understanding[\"tool_execution\"][\"required_tools\"] == []"` | — |
| [SRC-F725E90B2A-L003719](../../tests/test_web_agent.py#L3719) | 3719 | `"    assert all("` | — |
| [SRC-F725E90B2A-L003720](../../tests/test_web_agent.py#L3720) | 3720 | `"        row[\"status\"] == \"not_required\""` | — |
| [SRC-F725E90B2A-L003721](../../tests/test_web_agent.py#L3721) | 3721 | `"        for row in task_understanding[\"tool_execution\"][\"tool_status_matrix\"]"` | — |
| [SRC-F725E90B2A-L003722](../../tests/test_web_agent.py#L3722) | 3722 | `"    )"` | — |
| [SRC-F725E90B2A-L003723](../../tests/test_web_agent.py#L3723) | 3723 | `"    assert task_understanding[\"actual_queries\"] == []"` | — |
| [SRC-F725E90B2A-L003724](../../tests/test_web_agent.py#L3724) | 3724 | `"    assert task_understanding[\"query_strategy_matrix\"] == []"` | — |
| [SRC-F725E90B2A-L003725](../../tests/test_web_agent.py#L3725) | 3725 | `"    assert task_understanding[\"search_was_attempted\"] is False"` | — |
| [SRC-F725E90B2A-L003726](../../tests/test_web_agent.py#L3726) | 3726 | `""` | — |
| [SRC-F725E90B2A-L003727](../../tests/test_web_agent.py#L3727) | 3727 | `"def test_official_site_without_target_clarifies_before_planning_or_search(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003728](../../tests/test_web_agent.py#L3728) | 3728 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003729](../../tests/test_web_agent.py#L3729) | 3729 | `""` | — |
| [SRC-F725E90B2A-L003730](../../tests/test_web_agent.py#L3730) | 3730 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003731](../../tests/test_web_agent.py#L3731) | 3731 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003732](../../tests/test_web_agent.py#L3732) | 3732 | `"        \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003733](../../tests/test_web_agent.py#L3733) | 3733 | `"        lambda *args, **kwargs: pytest.fail(\"Missing official-site target must be clarified before planning\"),"` | — |
| [SRC-F725E90B2A-L003734](../../tests/test_web_agent.py#L3734) | 3734 | `"    )"` | — |
| [SRC-F725E90B2A-L003735](../../tests/test_web_agent.py#L3735) | 3735 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003736](../../tests/test_web_agent.py#L3736) | 3736 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003737](../../tests/test_web_agent.py#L3737) | 3737 | `"        \"_collect_research\","` | — |
| [SRC-F725E90B2A-L003738](../../tests/test_web_agent.py#L3738) | 3738 | `"        lambda *args, **kwargs: pytest.fail(\"Missing official-site target must not invoke search\"),"` | — |
| [SRC-F725E90B2A-L003739](../../tests/test_web_agent.py#L3739) | 3739 | `"    )"` | — |
| [SRC-F725E90B2A-L003740](../../tests/test_web_agent.py#L3740) | 3740 | `""` | — |
| [SRC-F725E90B2A-L003741](../../tests/test_web_agent.py#L3741) | 3741 | `"    result = agent.answer(\"هات الموقع الرسمي\")"` | — |
| [SRC-F725E90B2A-L003742](../../tests/test_web_agent.py#L3742) | 3742 | `""` | — |
| [SRC-F725E90B2A-L003743](../../tests/test_web_agent.py#L3743) | 3743 | `"    assert result[\"intent_route\"] == \"CLARIFY\""` | — |
| [SRC-F725E90B2A-L003744](../../tests/test_web_agent.py#L3744) | 3744 | `"    assert result[\"kind\"] == \"clarification_needed\""` | — |
| [SRC-F725E90B2A-L003745](../../tests/test_web_agent.py#L3745) | 3745 | `"    assert \"اسم الجهة أو الشركة\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L003746](../../tests/test_web_agent.py#L3746) | 3746 | `"    assert result[\"search_attempted\"] is False"` | — |
| [SRC-F725E90B2A-L003747](../../tests/test_web_agent.py#L3747) | 3747 | `"    assert \"official_destination_target_entity\" in result[\"task_understanding\"][\"task_spec\"][\"missing_required_inputs\"]"` | — |
| [SRC-F725E90B2A-L003748](../../tests/test_web_agent.py#L3748) | 3748 | `""` | — |
| [SRC-F725E90B2A-L003749](../../tests/test_web_agent.py#L3749) | 3749 | `"def test_summary_without_source_clarifies_before_search(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003750](../../tests/test_web_agent.py#L3750) | 3750 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003751](../../tests/test_web_agent.py#L3751) | 3751 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003752](../../tests/test_web_agent.py#L3752) | 3752 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003753](../../tests/test_web_agent.py#L3753) | 3753 | `"        \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003754](../../tests/test_web_agent.py#L3754) | 3754 | `"        lambda *args, **kwargs: pytest.fail(\"Missing summary source must be clarified before planning\"),"` | — |
| [SRC-F725E90B2A-L003755](../../tests/test_web_agent.py#L3755) | 3755 | `"    )"` | — |
| [SRC-F725E90B2A-L003756](../../tests/test_web_agent.py#L3756) | 3756 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003757](../../tests/test_web_agent.py#L3757) | 3757 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003758](../../tests/test_web_agent.py#L3758) | 3758 | `"        \"_collect_research\","` | — |
| [SRC-F725E90B2A-L003759](../../tests/test_web_agent.py#L3759) | 3759 | `"        lambda *args, **kwargs: pytest.fail(\"Missing summary source must not invoke search\"),"` | — |
| [SRC-F725E90B2A-L003760](../../tests/test_web_agent.py#L3760) | 3760 | `"    )"` | — |
| [SRC-F725E90B2A-L003761](../../tests/test_web_agent.py#L3761) | 3761 | `""` | — |
| [SRC-F725E90B2A-L003762](../../tests/test_web_agent.py#L3762) | 3762 | `"    result = agent.answer(\"لخص\")"` | — |
| [SRC-F725E90B2A-L003763](../../tests/test_web_agent.py#L3763) | 3763 | `""` | — |
| [SRC-F725E90B2A-L003764](../../tests/test_web_agent.py#L3764) | 3764 | `"    assert result[\"intent_route\"] == \"CLARIFY\""` | — |
| [SRC-F725E90B2A-L003765](../../tests/test_web_agent.py#L3765) | 3765 | `"    assert \"أرسل النص\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L003766](../../tests/test_web_agent.py#L3766) | 3766 | `"    assert result[\"search_attempted\"] is False"` | — |
| [SRC-F725E90B2A-L003767](../../tests/test_web_agent.py#L3767) | 3767 | `"    assert \"summary_source_url_or_pasted_text\" in result[\"task_understanding\"][\"task_spec\"][\"missing_required_inputs\"]"` | — |
| [SRC-F725E90B2A-L003768](../../tests/test_web_agent.py#L3768) | 3768 | `""` | — |
| [SRC-F725E90B2A-L003769](../../tests/test_web_agent.py#L3769) | 3769 | `"def test_task_spec_controls_generation_context_without_becoming_evidence(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003770](../../tests/test_web_agent.py#L3770) | 3770 | `"    from agents.task_understanding import build_query_strategy_matrix, build_task_spec"` | — |
| [SRC-F725E90B2A-L003771](../../tests/test_web_agent.py#L3771) | 3771 | `""` | — |
| [SRC-F725E90B2A-L003772](../../tests/test_web_agent.py#L3772) | 3772 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003773](../../tests/test_web_agent.py#L3773) | 3773 | `"    captured = {}"` | — |
| [SRC-F725E90B2A-L003774](../../tests/test_web_agent.py#L3774) | 3774 | `""` | — |
| [SRC-F725E90B2A-L003775](../../tests/test_web_agent.py#L3775) | 3775 | `"    question = ("` | — |
| [SRC-F725E90B2A-L003776](../../tests/test_web_agent.py#L3776) | 3776 | `"        \"قارن السيارات الكهربائية في مصر من حيث السعر والضمان، \""` | — |
| [SRC-F725E90B2A-L003777](../../tests/test_web_agent.py#L3777) | 3777 | `"        \"اشرح ببساطة مع أمثلة وروابط مباشرة\""` | — |
| [SRC-F725E90B2A-L003778](../../tests/test_web_agent.py#L3778) | 3778 | `"    )"` | — |
| [SRC-F725E90B2A-L003779](../../tests/test_web_agent.py#L3779) | 3779 | `"    task_spec = build_task_spec("` | — |
| [SRC-F725E90B2A-L003780](../../tests/test_web_agent.py#L3780) | 3780 | `"        question,"` | — |
| [SRC-F725E90B2A-L003781](../../tests/test_web_agent.py#L3781) | 3781 | `"        mode=\"deep\","` | — |
| [SRC-F725E90B2A-L003782](../../tests/test_web_agent.py#L3782) | 3782 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-F725E90B2A-L003783](../../tests/test_web_agent.py#L3783) | 3783 | `"    )"` | — |
| [SRC-F725E90B2A-L003784](../../tests/test_web_agent.py#L3784) | 3784 | `"    initial_queries = [compact_search_query(question)]"` | — |
| [SRC-F725E90B2A-L003785](../../tests/test_web_agent.py#L3785) | 3785 | `"    matrix = build_query_strategy_matrix("` | — |
| [SRC-F725E90B2A-L003786](../../tests/test_web_agent.py#L3786) | 3786 | `"        question,"` | — |
| [SRC-F725E90B2A-L003787](../../tests/test_web_agent.py#L3787) | 3787 | `"        task_spec,"` | — |
| [SRC-F725E90B2A-L003788](../../tests/test_web_agent.py#L3788) | 3788 | `"        initial_queries,"` | — |
| [SRC-F725E90B2A-L003789](../../tests/test_web_agent.py#L3789) | 3789 | `"        limit=4,"` | — |
| [SRC-F725E90B2A-L003790](../../tests/test_web_agent.py#L3790) | 3790 | `"        compact_fn=compact_search_query,"` | — |
| [SRC-F725E90B2A-L003791](../../tests/test_web_agent.py#L3791) | 3791 | `"    )"` | — |
| [SRC-F725E90B2A-L003792](../../tests/test_web_agent.py#L3792) | 3792 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L003793](../../tests/test_web_agent.py#L3793) | 3793 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L003794](../../tests/test_web_agent.py#L3794) | 3794 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003795](../../tests/test_web_agent.py#L3795) | 3795 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003796](../../tests/test_web_agent.py#L3796) | 3796 | `"        \"queries\": [row[\"query\"] for row in matrix],"` | — |
| [SRC-F725E90B2A-L003797](../../tests/test_web_agent.py#L3797) | 3797 | `"        \"dialogue_context\": {},"` | — |
| [SRC-F725E90B2A-L003798](../../tests/test_web_agent.py#L3798) | 3798 | `"        \"intent_route\": \"WEB_DEEP\","` | — |
| [SRC-F725E90B2A-L003799](../../tests/test_web_agent.py#L3799) | 3799 | `"        \"task_spec\": task_spec,"` | — |
| [SRC-F725E90B2A-L003800](../../tests/test_web_agent.py#L3800) | 3800 | `"        \"query_strategy_matrix\": matrix,"` | — |
| [SRC-F725E90B2A-L003801](../../tests/test_web_agent.py#L3801) | 3801 | `"    }"` | — |
| [SRC-F725E90B2A-L003802](../../tests/test_web_agent.py#L3802) | 3802 | `""` | — |
| [SRC-F725E90B2A-L003803](../../tests/test_web_agent.py#L3803) | 3803 | `"    def fake_completion(messages, **kwargs):"` | — |
| [SRC-F725E90B2A-L003804](../../tests/test_web_agent.py#L3804) | 3804 | `"        captured[\"messages\"] = messages"` | — |
| [SRC-F725E90B2A-L003805](../../tests/test_web_agent.py#L3805) | 3805 | `"        captured[\"kwargs\"] = kwargs"` | — |
| [SRC-F725E90B2A-L003806](../../tests/test_web_agent.py#L3806) | 3806 | `"        return \"إجابة اختبارية مرتبطة بالأدلة.\""` | — |
| [SRC-F725E90B2A-L003807](../../tests/test_web_agent.py#L3807) | 3807 | `""` | — |
| [SRC-F725E90B2A-L003808](../../tests/test_web_agent.py#L3808) | 3808 | `"    monkeypatch.setattr(agent, \"_request_completion\", fake_completion)"` | — |
| [SRC-F725E90B2A-L003809](../../tests/test_web_agent.py#L3809) | 3809 | `""` | — |
| [SRC-F725E90B2A-L003810](../../tests/test_web_agent.py#L3810) | 3810 | `"    answer = agent._generate("` | — |
| [SRC-F725E90B2A-L003811](../../tests/test_web_agent.py#L3811) | 3811 | `"        question,"` | — |
| [SRC-F725E90B2A-L003812](../../tests/test_web_agent.py#L3812) | 3812 | `"        [],"` | — |
| [SRC-F725E90B2A-L003813](../../tests/test_web_agent.py#L3813) | 3813 | `"        [sample_source(0)],"` | — |
| [SRC-F725E90B2A-L003814](../../tests/test_web_agent.py#L3814) | 3814 | `"        None,"` | — |
| [SRC-F725E90B2A-L003815](../../tests/test_web_agent.py#L3815) | 3815 | `"        research_plan=plan,"` | — |
| [SRC-F725E90B2A-L003816](../../tests/test_web_agent.py#L3816) | 3816 | `"        search_report={"` | — |
| [SRC-F725E90B2A-L003817](../../tests/test_web_agent.py#L3817) | 3817 | `"            \"queries_planned\": len(plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L003818](../../tests/test_web_agent.py#L3818) | 3818 | `"            \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L003819](../../tests/test_web_agent.py#L3819) | 3819 | `"            \"pages_fetched\": 1,"` | — |
| [SRC-F725E90B2A-L003820](../../tests/test_web_agent.py#L3820) | 3820 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L003821](../../tests/test_web_agent.py#L3821) | 3821 | `"        },"` | — |
| [SRC-F725E90B2A-L003822](../../tests/test_web_agent.py#L3822) | 3822 | `"    )"` | — |
| [SRC-F725E90B2A-L003823](../../tests/test_web_agent.py#L3823) | 3823 | `""` | — |
| [SRC-F725E90B2A-L003824](../../tests/test_web_agent.py#L3824) | 3824 | `"    prompt = \"\\n\".join("` | — |
| [SRC-F725E90B2A-L003825](../../tests/test_web_agent.py#L3825) | 3825 | `"        message.get(\"content\", \"\")"` | — |
| [SRC-F725E90B2A-L003826](../../tests/test_web_agent.py#L3826) | 3826 | `"        for message in captured[\"messages\"]"` | — |
| [SRC-F725E90B2A-L003827](../../tests/test_web_agent.py#L3827) | 3827 | `"        if isinstance(message, dict)"` | — |
| [SRC-F725E90B2A-L003828](../../tests/test_web_agent.py#L3828) | 3828 | `"    )"` | — |
| [SRC-F725E90B2A-L003829](../../tests/test_web_agent.py#L3829) | 3829 | `"    assert answer == \"إجابة اختبارية مرتبطة بالأدلة.\""` | — |
| [SRC-F725E90B2A-L003830](../../tests/test_web_agent.py#L3830) | 3830 | `"    assert \"task_planning_context\" in prompt"` | — |
| [SRC-F725E90B2A-L003831](../../tests/test_web_agent.py#L3831) | 3831 | `"    assert \"explicit_aspects\" in prompt"` | — |
| [SRC-F725E90B2A-L003832](../../tests/test_web_agent.py#L3832) | 3832 | `"    assert \"output_preferences\" in prompt"` | — |
| [SRC-F725E90B2A-L003833](../../tests/test_web_agent.py#L3833) | 3833 | `"    assert \"beginner_friendly_requested\" in prompt"` | — |
| [SRC-F725E90B2A-L003834](../../tests/test_web_agent.py#L3834) | 3834 | `"    assert \"reasoning_guidance\" in prompt"` | — |
| [SRC-F725E90B2A-L003835](../../tests/test_web_agent.py#L3835) | 3835 | `"    assert \"decision_matrix\" in prompt"` | — |
| [SRC-F725E90B2A-L003836](../../tests/test_web_agent.py#L3836) | 3836 | `"    assert \"قسّم المقارنة إلى كل معيار صريح\" in prompt"` | — |
| [SRC-F725E90B2A-L003837](../../tests/test_web_agent.py#L3837) | 3837 | `"    assert \"وحّد العملة والوحدات\" in prompt"` | — |
| [SRC-F725E90B2A-L003838](../../tests/test_web_agent.py#L3838) | 3838 | `"    assert \"query_strategy_matrix\" in prompt"` | — |
| [SRC-F725E90B2A-L003839](../../tests/test_web_agent.py#L3839) | 3839 | `"    assert \"الأولوية لكلام المستخدم الحالي\" in prompt"` | — |
| [SRC-F725E90B2A-L003840](../../tests/test_web_agent.py#L3840) | 3840 | `"    assert \"الاستعلامات المخططة فقط\" in prompt"` | — |
| [SRC-F725E90B2A-L003841](../../tests/test_web_agent.py#L3841) | 3841 | `""` | — |
| [SRC-F725E90B2A-L003842](../../tests/test_web_agent.py#L3842) | 3842 | `"def test_bilingual_relevance_handles_arabic_attached_clitics_without_lowering_floor():"` | — |
| [SRC-F725E90B2A-L003843](../../tests/test_web_agent.py#L3843) | 3843 | `"    query = \"أهم استخدامات الذكاء الاصطناعي للشركات الصغيرة؟\""` | — |
| [SRC-F725E90B2A-L003844](../../tests/test_web_agent.py#L3844) | 3844 | `"    evidence = \"AI use cases for small businesses\""` | — |
| [SRC-F725E90B2A-L003845](../../tests/test_web_agent.py#L3845) | 3845 | `"    assert _minimum_relevance_ratio(query) == 0.20"` | — |
| [SRC-F725E90B2A-L003846](../../tests/test_web_agent.py#L3846) | 3846 | `"    assert _relevance_ratio(query, evidence) >= 0.80"` | — |
| [SRC-F725E90B2A-L003847](../../tests/test_web_agent.py#L3847) | 3847 | `""` | — |
| [SRC-F725E90B2A-L003848](../../tests/test_web_agent.py#L3848) | 3848 | `"def test_search_evidence_matching_keeps_distinct_concepts_as_the_ratio_denominator():"` | — |
| [SRC-F725E90B2A-L003849](../../tests/test_web_agent.py#L3849) | 3849 | `"    query = \"استخدامات الذكاء الاصطناعي للشركات الصغيرة\""` | — |
| [SRC-F725E90B2A-L003850](../../tests/test_web_agent.py#L3850) | 3850 | `"    on_topic = \"AI use cases for small businesses\""` | — |
| [SRC-F725E90B2A-L003851](../../tests/test_web_agent.py#L3851) | 3851 | `"    weak = \"AI tools for personal photo editing\""` | — |
| [SRC-F725E90B2A-L003852](../../tests/test_web_agent.py#L3852) | 3852 | `"    assert _relevance_ratio(query, on_topic) > _relevance_ratio(query, weak)"` | — |
| [SRC-F725E90B2A-L003853](../../tests/test_web_agent.py#L3853) | 3853 | `"    assert _relevance_ratio(query, weak) < _minimum_relevance_ratio(query)"` | — |
| [SRC-F725E90B2A-L003854](../../tests/test_web_agent.py#L3854) | 3854 | `""` | — |
| [SRC-F725E90B2A-L003855](../../tests/test_web_agent.py#L3855) | 3855 | `"def test_bilingual_relevance_matches_english_queries_to_arabic_source_text():"` | — |
| [SRC-F725E90B2A-L003856](../../tests/test_web_agent.py#L3856) | 3856 | `"    query = \"AI use cases for small businesses in Egypt\""` | — |
| [SRC-F725E90B2A-L003857](../../tests/test_web_agent.py#L3857) | 3857 | `"    evidence = \"استخدامات الذكاء الاصطناعي للشركات الصغيرة في مصر\""` | — |
| [SRC-F725E90B2A-L003858](../../tests/test_web_agent.py#L3858) | 3858 | `"    assert _relevance_ratio(query, evidence) >= 0.80"` | — |
| [SRC-F725E90B2A-L003859](../../tests/test_web_agent.py#L3859) | 3859 | `""` | — |
| [SRC-F725E90B2A-L003860](../../tests/test_web_agent.py#L3860) | 3860 | `""` | — |
| [SRC-F725E90B2A-L003861](../../tests/test_web_agent.py#L3861) | 3861 | `"def test_completion_diagnostics_failure_does_not_break_answer(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003862](../../tests/test_web_agent.py#L3862) | 3862 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003863](../../tests/test_web_agent.py#L3863) | 3863 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L003864](../../tests/test_web_agent.py#L3864) | 3864 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003865](../../tests/test_web_agent.py#L3865) | 3865 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003866](../../tests/test_web_agent.py#L3866) | 3866 | `"        \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003867](../../tests/test_web_agent.py#L3867) | 3867 | `"        lambda question, history: {"` | — |
| [SRC-F725E90B2A-L003868](../../tests/test_web_agent.py#L3868) | 3868 | `"            \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L003869](../../tests/test_web_agent.py#L3869) | 3869 | `"            \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003870](../../tests/test_web_agent.py#L3870) | 3870 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003871](../../tests/test_web_agent.py#L3871) | 3871 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003872](../../tests/test_web_agent.py#L3872) | 3872 | `"            \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003873](../../tests/test_web_agent.py#L3873) | 3873 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003874](../../tests/test_web_agent.py#L3874) | 3874 | `"            \"coverage_targets\": [],"` | — |
| [SRC-F725E90B2A-L003875](../../tests/test_web_agent.py#L3875) | 3875 | `"        },"` | — |
| [SRC-F725E90B2A-L003876](../../tests/test_web_agent.py#L3876) | 3876 | `"    )"` | — |
| [SRC-F725E90B2A-L003877](../../tests/test_web_agent.py#L3877) | 3877 | `"    monkeypatch.setattr(agent, \"_collect_research\", lambda plan: ("` | — |
| [SRC-F725E90B2A-L003878](../../tests/test_web_agent.py#L3878) | 3878 | `"        [sample_source(0), sample_source(1)], [], {"` | — |
| [SRC-F725E90B2A-L003879](../../tests/test_web_agent.py#L3879) | 3879 | `"            \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L003880](../../tests/test_web_agent.py#L3880) | 3880 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L003881](../../tests/test_web_agent.py#L3881) | 3881 | `"            \"query_results\": [{\"query\": plan[\"queries\"][0], \"results\": 2}],"` | — |
| [SRC-F725E90B2A-L003882](../../tests/test_web_agent.py#L3882) | 3882 | `"            \"unique_sources\": 2,"` | — |
| [SRC-F725E90B2A-L003883](../../tests/test_web_agent.py#L3883) | 3883 | `"            \"pages_fetched\": 2,"` | — |
| [SRC-F725E90B2A-L003884](../../tests/test_web_agent.py#L3884) | 3884 | `"            \"providers_used\": [\"test\"],"` | — |
| [SRC-F725E90B2A-L003885](../../tests/test_web_agent.py#L3885) | 3885 | `"            \"provider_diagnostics\": [],"` | — |
| [SRC-F725E90B2A-L003886](../../tests/test_web_agent.py#L3886) | 3886 | `"        }"` | — |
| [SRC-F725E90B2A-L003887](../../tests/test_web_agent.py#L3887) | 3887 | `"    ))"` | — |
| [SRC-F725E90B2A-L003888](../../tests/test_web_agent.py#L3888) | 3888 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L003889](../../tests/test_web_agent.py#L3889) | 3889 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L003890](../../tests/test_web_agent.py#L3890) | 3890 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"إجابة اختبارية [المصدر 1].\")"` | — |
| [SRC-F725E90B2A-L003891](../../tests/test_web_agent.py#L3891) | 3891 | `""` | — |
| [SRC-F725E90B2A-L003892](../../tests/test_web_agent.py#L3892) | 3892 | `"    def fail_diagnostics(_result):"` | — |
| [SRC-F725E90B2A-L003893](../../tests/test_web_agent.py#L3893) | 3893 | `"        raise RuntimeError(\"diagnostics are optional\")"` | — |
| [SRC-F725E90B2A-L003894](../../tests/test_web_agent.py#L3894) | 3894 | `""` | — |
| [SRC-F725E90B2A-L003895](../../tests/test_web_agent.py#L3895) | 3895 | `"    monkeypatch.setattr(\"agents.web_agent.build_research_completion\", fail_diagnostics)"` | — |
| [SRC-F725E90B2A-L003896](../../tests/test_web_agent.py#L3896) | 3896 | `"    result = agent.answer(\"قارن هذه التقنية\")"` | — |
| [SRC-F725E90B2A-L003897](../../tests/test_web_agent.py#L3897) | 3897 | `"    assert result[\"answer\"] == \"إجابة اختبارية [المصدر 1].\""` | — |
| [SRC-F725E90B2A-L003898](../../tests/test_web_agent.py#L3898) | 3898 | `"    assert result[\"research_completion\"][\"status\"] == \"diagnostics_not_computed\""` | — |
| [SRC-F725E90B2A-L003899](../../tests/test_web_agent.py#L3899) | 3899 | `"    assert any(\"لا يُعد ذلك دليلًا على اكتمال البحث\" in warning for warning in result[\"warnings\"])"` | — |
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
| [SRC-DE7EABE998-L000162](../../web/agent.html#L162) | 162 | `" const completion=r.research_completion&&typeof r.research_completion===\"object\"?r.research_completion:"` | — |
| [SRC-DE7EABE998-L000163](../../web/agent.html#L163) | 163 | `"  (result&&result.research_completion&&typeof result.research_completion===\"object\"?result.research_completion:null);"` | — |
| [SRC-DE7EABE998-L000164](../../web/agent.html#L164) | 164 | `" const completionStatusLabels={"` | — |
| [SRC-DE7EABE998-L000165](../../web/agent.html#L165) | 165 | `"  execution_stopped_budget:\"توقفت العملية عند حد الميزانية\","` | — |
| [SRC-DE7EABE998-L000166](../../web/agent.html#L166) | 166 | `"  no_eligible_sources_after_filtering:\"لم يبقَ مصدر مقبول بعد التصفية\","` | — |
| [SRC-DE7EABE998-L000167](../../web/agent.html#L167) | 167 | `"  search_failed_or_incomplete:\"البحث فشل أو لم يكتمل\","` | — |
| [SRC-DE7EABE998-L000168](../../web/agent.html#L168) | 168 | `"  no_results_returned:\"اكتمل البحث دون نتائج\","` | — |
| [SRC-DE7EABE998-L000169](../../web/agent.html#L169) | 169 | `"  search_not_attempted:\"لم تُنفذ محاولة البحث\","` | — |
| [SRC-DE7EABE998-L000170](../../web/agent.html#L170) | 170 | `"  insufficient_evidence:\"الأدلة غير كافية\","` | — |
| [SRC-DE7EABE998-L000171](../../web/agent.html#L171) | 171 | `"  source_snippets_only_generation_not_completed:\"مقتطفات فقط؛ لم تكتمل صياغة الإجابة\","` | — |
| [SRC-DE7EABE998-L000172](../../web/agent.html#L172) | 172 | `"  evidence_collected_generation_not_completed:\"جُمعت أدلة؛ لم تكتمل صياغة الإجابة\","` | — |
| [SRC-DE7EABE998-L000173](../../web/agent.html#L173) | 173 | `"  answer_generation_or_review_failed:\"تعذر توليد الإجابة أو مراجعتها\","` | — |
| [SRC-DE7EABE998-L000174](../../web/agent.html#L174) | 174 | `"  partial_answer_evidence_gaps_detected:\"إجابة جزئية مع فجوات أدلة محتملة\","` | — |
| [SRC-DE7EABE998-L000175](../../web/agent.html#L175) | 175 | `"  answer_generated_citations_range_checked_semantic_support_unverified:\"وُلّدت الإجابة وفُحصت أرقام الإحالات فقط؛ دعم الادعاءات دلاليًا غير متحقق\","` | — |
| [SRC-DE7EABE998-L000176](../../web/agent.html#L176) | 176 | `"  answer_generated_without_valid_citation_markers:\"وُلّدت الإجابة دون علامات إحالة صالحة\""` | — |
| [SRC-DE7EABE998-L000177](../../web/agent.html#L177) | 177 | `" };"` | — |
| [SRC-DE7EABE998-L000178](../../web/agent.html#L178) | 178 | `" const completionPhaseLabels={"` | — |
| [SRC-DE7EABE998-L000179](../../web/agent.html#L179) | 179 | `"  planning:\"التخطيط\",search:\"البحث\",source_filtering:\"تصفية المصادر\","` | — |
| [SRC-DE7EABE998-L000180](../../web/agent.html#L180) | 180 | `"  page_reading:\"قراءة الصفحات\",answer_generation:\"توليد الإجابة\","` | — |
| [SRC-DE7EABE998-L000181](../../web/agent.html#L181) | 181 | `"  citation_validation:\"فحص الإحالات\",semantic_verification:\"التحقق الدلالي\""` | — |
| [SRC-DE7EABE998-L000182](../../web/agent.html#L182) | 182 | `" };"` | — |
| [SRC-DE7EABE998-L000183](../../web/agent.html#L183) | 183 | `" const completionStateLabels={"` | — |
| [SRC-DE7EABE998-L000184](../../web/agent.html#L184) | 184 | `"  completed:\"مكتمل\",unknown:\"غير معلوم\",not_attempted:\"لم يبدأ\","` | — |
| [SRC-DE7EABE998-L000185](../../web/agent.html#L185) | 185 | `"  failed_or_incomplete:\"فشل أو لم يكتمل\",results_received:\"استُلمت نتائج\","` | — |
| [SRC-DE7EABE998-L000186](../../web/agent.html#L186) | 186 | `"  completed_no_results:\"اكتمل دون نتائج\",attempted_no_usable_sources:\"محاولة دون مصادر صالحة\","` | — |
| [SRC-DE7EABE998-L000187](../../web/agent.html#L187) | 187 | `"  not_applicable_no_eligible_sources:\"لا توجد مصادر نهائية\",all_final_sources_read:\"قُرئت كل الصفحات النهائية\","` | — |
| [SRC-DE7EABE998-L000188](../../web/agent.html#L188) | 188 | `"  some_final_sources_read:\"قُرئ بعض الصفحات\",no_final_source_page_read:\"لم تُقرأ صفحات نهائية\","` | — |
| [SRC-DE7EABE998-L000189](../../web/agent.html#L189) | 189 | `"  not_attempted_or_withheld:\"لم تُولد الإجابة أو حُجبت\",answer_generated:\"وُلّدت الإجابة\","` | — |
| [SRC-DE7EABE998-L000190](../../web/agent.html#L190) | 190 | `"  not_completed:\"لم يكتمل\",failed_or_unavailable:\"فشل أو غير متاح\","` | — |
| [SRC-DE7EABE998-L000191](../../web/agent.html#L191) | 191 | `"  not_run:\"لم يُنفذ\",not_performed:\"لم يُنفذ\",sources_retained:\"احتُفظ بمصادر\","` | — |
| [SRC-DE7EABE998-L000192](../../web/agent.html#L192) | 192 | `"  rejected_all_candidates:\"رُفضت كل المرشحات\",no_eligible_sources:\"لا توجد مصادر مقبولة\","` | — |
| [SRC-DE7EABE998-L000193](../../web/agent.html#L193) | 193 | `"  index_range_check_passed:\"فُحص نطاق أرقام الإحالات فقط\","` | — |
| [SRC-DE7EABE998-L000194](../../web/agent.html#L194) | 194 | `"  invalid_index_references_removed:\"حُذفت إحالات خارج النطاق\","` | — |
| [SRC-DE7EABE998-L000195](../../web/agent.html#L195) | 195 | `"  no_citation_markers_present:\"لا توجد علامات إحالة\",diagnostics_not_computed:\"تعذر احتساب التشخيص\""` | — |
| [SRC-DE7EABE998-L000196](../../web/agent.html#L196) | 196 | `" };"` | — |
| [SRC-DE7EABE998-L000197](../../web/agent.html#L197) | 197 | `" const completionSummary=completion&&completion.status"` | — |
| [SRC-DE7EABE998-L000198](../../web/agent.html#L198) | 198 | `"  ?'<p class=\"'+([\"search_failed_or_incomplete\",\"execution_stopped_budget\",\"answer_generation_or_review_failed\",\"no_eligible_sources_after_filtering\",\"partial_answer_evidence_gaps_detected\"].includes(completion.status)?\"warning\":\"report-note\")+'\"><b>حالة إكمال البحث:</b> '+escapeHtml(completionStatusLabels[completion.status]\|\|completion.status)+'. هذه حالة تشغيلية وليست احتمالًا لصحة الإجابة.</p>'"` | — |
| [SRC-DE7EABE998-L000199](../../web/agent.html#L199) | 199 | `"  :\"\";"` | — |
| [SRC-DE7EABE998-L000200](../../web/agent.html#L200) | 200 | `" const completionPhaseRows=completion&&completion.phases&&typeof completion.phases===\"object\""` | — |
| [SRC-DE7EABE998-L000201](../../web/agent.html#L201) | 201 | `"  ?Object.entries(completion.phases).map(([phase,state])=>'<li>'+escapeHtml(completionPhaseLabels[phase]\|\|phase)+': '+escapeHtml(completionStateLabels[state]\|\|state\|\|\"غير محدد\")+'</li>').join(\"\")"` | — |
| [SRC-DE7EABE998-L000202](../../web/agent.html#L202) | 202 | `"  :\"\";"` | — |
| [SRC-DE7EABE998-L000203](../../web/agent.html#L203) | 203 | `" const completionCounters=completion&&completion.counters&&typeof completion.counters===\"object\"?completion.counters:{};"` | — |
| [SRC-DE7EABE998-L000204](../../web/agent.html#L204) | 204 | `" const completionCounterRows=["` | — |
| [SRC-DE7EABE998-L000205](../../web/agent.html#L205) | 205 | `"  [completionCounters.queries_planned,\"استعلامًا مخططًا\"],"` | — |
| [SRC-DE7EABE998-L000206](../../web/agent.html#L206) | 206 | `"  [completionCounters.queries_attempted,\"استعلامًا تمت محاولته\"],"` | — |
| [SRC-DE7EABE998-L000207](../../web/agent.html#L207) | 207 | `"  [completionCounters.per_query_result_count_sum,\"مجموع أعداد النتائج المسجلة لكل استعلام، قبل إزالة التكرار\"],"` | — |
| [SRC-DE7EABE998-L000208](../../web/agent.html#L208) | 208 | `"  [completionCounters.final_source_list_count,\"مصدرًا في القائمة النهائية\"],"` | — |
| [SRC-DE7EABE998-L000209](../../web/agent.html#L209) | 209 | `"  [completionCounters.unique_normalized_url_count,\"رابطًا فريدًا بعد التطبيع\"],"` | — |
| [SRC-DE7EABE998-L000210](../../web/agent.html#L210) | 210 | `"  [completionCounters.duplicate_normalized_url_count,\"رابطًا مكررًا وفق التطبيع\"],"` | — |
| [SRC-DE7EABE998-L000211](../../web/agent.html#L211) | 211 | `"  [completionCounters.distinct_registrable_domain_count,\"نطاقًا مسجلًا مختلفًا\"],"` | — |
| [SRC-DE7EABE998-L000212](../../web/agent.html#L212) | 212 | `"  [completionCounters.pages_fetched_flag_count,\"صفحة تحمل علامة جلب\"],"` | — |
| [SRC-DE7EABE998-L000213](../../web/agent.html#L213) | 213 | `"  [completionCounters.pages_read_with_text_count,\"صفحة توفر نصها المقروء\"],"` | — |
| [SRC-DE7EABE998-L000214](../../web/agent.html#L214) | 214 | `"  [completionCounters.snippet_only_source_count,\"مصدرًا بمقتطف دون صفحة مقروءة\"],"` | — |
| [SRC-DE7EABE998-L000215](../../web/agent.html#L215) | 215 | `"  [completionCounters.connector_success_count,\"استجابة موصل ناجحة/مكتملة\"],"` | — |
| [SRC-DE7EABE998-L000216](../../web/agent.html#L216) | 216 | `"  [completionCounters.connector_failure_count,\"حالة إخفاق موصل مسجلة\"],"` | — |
| [SRC-DE7EABE998-L000217](../../web/agent.html#L217) | 217 | `"  [completionCounters.guardrail_rejected_candidate_count,\"مرشحًا مرفوضًا بحواجز الأدلة\"]"` | — |
| [SRC-DE7EABE998-L000218](../../web/agent.html#L218) | 218 | `" ];"` | — |
| [SRC-DE7EABE998-L000219](../../web/agent.html#L219) | 219 | `" const completionCounterHtml=completionCounterRows.map(([value,label])=>'<div class=\"metric\"><strong>'+escapeHtml(value===null\|\|value===undefined?\"غير محدد\":value)+'</strong><span>'+escapeHtml(label)+'</span></div>').join(\"\");"` | — |
| [SRC-DE7EABE998-L000220](../../web/agent.html#L220) | 220 | `" const consistency=completion&&completion.counter_consistency&&typeof completion.counter_consistency===\"object\"?completion.counter_consistency:null;"` | — |
| [SRC-DE7EABE998-L000221](../../web/agent.html#L221) | 221 | `" const consistencyLabels={matched:\"العدادات المتاحة متطابقة\",mismatch_detected:\"اختلاف بين بعض العدادات والقائمة النهائية\",not_computable:\"لا توجد عدادات كافية للمقارنة\"};"` | — |
| [SRC-DE7EABE998-L000222](../../web/agent.html#L222) | 222 | `" const consistencyHtml=consistency?'<p class=\"'+(consistency.status===\"mismatch_detected\"?\"warning\":\"report-note\")+'\">اتساق العدادات: '+escapeHtml(consistencyLabels[consistency.status]\|\|consistency.status\|\|\"غير محدد\")+(Array.isArray(consistency.issues)&&consistency.issues.length?' — '+consistency.issues.map(escapeHtml).join(\"، \"):\"\")+'</p>':\"\";"` | — |
| [SRC-DE7EABE998-L000223](../../web/agent.html#L223) | 223 | `" const completionDetailsHtml=completion&&completion.status"` | — |
| [SRC-DE7EABE998-L000224](../../web/agent.html#L224) | 224 | `"  ?'<details class=\"details\"><summary>تفاصيل مراحل إكمال البحث والعدادات</summary>'+(completionPhaseRows?'<p class=\"report-note\">مراحل التنفيذ:</p><ul>'+completionPhaseRows+'</ul>':\"\")+'<div class=\"metrics\">'+completionCounterHtml+'</div>'+consistencyHtml+'<p class=\"warning\">التحقق الدلالي من أن كل ادعاء مسنود فعلًا بالمصدر لم يُنفذ في هذا التشخيص. صلاحية رقم الإحالة أو قراءة الصفحة لا تثبت صحة الادعاء.</p></details>'"` | — |
| [SRC-DE7EABE998-L000225](../../web/agent.html#L225) | 225 | `"  :\"\";"` | — |
| [SRC-DE7EABE998-L000226](../../web/agent.html#L226) | 226 | `" const e=r.evidence_signals&&typeof r.evidence_signals===\"object\"?r.evidence_signals:{};"` | — |
| [SRC-DE7EABE998-L000227](../../web/agent.html#L227) | 227 | `" const sources=Array.isArray(result.sources)?result.sources:[];"` | — |
| [SRC-DE7EABE998-L000228](../../web/agent.html#L228) | 228 | `" const researchErrorOutcome=[\"attempted_research_error\",\"unknown_after_research_error\"].includes(r.search_outcome);"` | — |
| [SRC-DE7EABE998-L000229](../../web/agent.html#L229) | 229 | `" const lead=r.lead_generation&&typeof r.lead_generation===\"object\"?r.lead_generation:null;"` | — |
| [SRC-DE7EABE998-L000230](../../web/agent.html#L230) | 230 | `" const leadResearchIncomplete=!!lead&&lead.status===\"research_incomplete\";"` | — |
| [SRC-DE7EABE998-L000231](../../web/agent.html#L231) | 231 | `" const leadSignalCount=lead&&lead.candidate_signal_count!==null&&lead.candidate_signal_count!==undefined&&Number.isFinite(Number(lead.candidate_signal_count))?Number(lead.candidate_signal_count):null;"` | — |
| [SRC-DE7EABE998-L000232](../../web/agent.html#L232) | 232 | `" const noQualifiedLeads=!!lead&&!leadResearchIncomplete&&leadSignalCount===0;"` | — |
| [SRC-DE7EABE998-L000233](../../web/agent.html#L233) | 233 | `" const scoreLabel=lead?(leadResearchIncomplete?\"تعذر حسم البحث عن العملاء\":noQualifiedLeads?\"لم يُثبت وجود عميل محتمل\":\"إشارات نية شراء مرشحة\"):(researchErrorOutcome?\"تعذر تحديد التغطية\":(e.coverage_level\|\|\"تغطية محدودة\"));"` | — |
| [SRC-DE7EABE998-L000234](../../web/agent.html#L234) | 234 | `" const metrics=lead?["` | — |
| [SRC-DE7EABE998-L000235](../../web/agent.html#L235) | 235 | `"  [leadSignalCount??\"غير محدد\",\"إشارة نصية مرشحة لنية شراء\"],"` | — |
| [SRC-DE7EABE998-L000236](../../web/agent.html#L236) | 236 | `"  [lead.related_results_reviewed??\"غير محدد\",\"نتيجة تمت مراجعتها\"],"` | — |
| [SRC-DE7EABE998-L000237](../../web/agent.html#L237) | 237 | `"  [r.pages_fetched??(leadResearchIncomplete?\"غير محدد\":0),\"صفحة قُرئت\"],"` | — |
| [SRC-DE7EABE998-L000238](../../web/agent.html#L238) | 238 | `"  [leadResearchIncomplete?\"غير محدد\":(e.providers_count??(Array.isArray(r.providers_used)?r.providers_used.length:0)),\"واجهة أسهمت بمصدر صالح\"]"` | — |
| [SRC-DE7EABE998-L000239](../../web/agent.html#L239) | 239 | `" ]:["` | — |
| [SRC-DE7EABE998-L000240](../../web/agent.html#L240) | 240 | `"  [researchErrorOutcome?(r.unique_sources??\"غير محدد\"):(r.unique_sources??sources.length),\"مصدرًا فريدًا\"],"` | — |
| [SRC-DE7EABE998-L000241](../../web/agent.html#L241) | 241 | `"  [researchErrorOutcome?\"غير محدد\":(e.unique_domains??\"—\"),\"نطاقًا مختلفًا\"],"` | — |
| [SRC-DE7EABE998-L000242](../../web/agent.html#L242) | 242 | `"  [researchErrorOutcome?(r.pages_fetched??\"غير محدد\"):(r.pages_fetched??e.pages_read??0),\"صفحة قُرئت\"],"` | — |
| [SRC-DE7EABE998-L000243](../../web/agent.html#L243) | 243 | `"  [researchErrorOutcome?\"غير محدد\":(e.providers_count??(Array.isArray(r.providers_used)?r.providers_used.length:0)),\"واجهة أسهمت بمصدر صالح\"]"` | — |
| [SRC-DE7EABE998-L000244](../../web/agent.html#L244) | 244 | `" ];"` | — |
| [SRC-DE7EABE998-L000245](../../web/agent.html#L245) | 245 | `" const metricHtml=metrics.map(([v,l])=>'<div class=\"metric\"><strong>'+escapeHtml(v)+'</strong><span>'+escapeHtml(l)+'</span></div>').join(\"\");"` | — |
| [SRC-DE7EABE998-L000246](../../web/agent.html#L246) | 246 | `" const operationalMetrics=["` | — |
| [SRC-DE7EABE998-L000247](../../web/agent.html#L247) | 247 | `"  [r.provider_candidates_received??\"غير محدد\",\"مرشح أعاده محرك البحث قبل التصفية (قد يتكرر)\"],"` | — |
| [SRC-DE7EABE998-L000248](../../web/agent.html#L248) | 248 | `"  [r.provider_candidates_accepted??\"غير محدد\",\"مرشح اجتاز فحص الموصل قبل الدمج\"],"` | — |
| [SRC-DE7EABE998-L000249](../../web/agent.html#L249) | 249 | `"  [r.provider_candidates_rejected??\"غير محدد\",\"مرشح رُفض بفحص الرابط أو الصلة\"],"` | — |
| [SRC-DE7EABE998-L000250](../../web/agent.html#L250) | 250 | `"  [r.raw_results??\"غير محدد\",\"نتيجة جُمعت قبل دمج التكرارات\"],"` | — |
| [SRC-DE7EABE998-L000251](../../web/agent.html#L251) | 251 | `"  [r.unique_urls??r.unique_sources??sources.length,\"رابط فريد بعد الدمج\"],"` | — |
| [SRC-DE7EABE998-L000252](../../web/agent.html#L252) | 252 | `"  [r.pages_fetch_attempted??\"غير محدد\",\"محاولة جلب صفحة\"],"` | — |
| [SRC-DE7EABE998-L000253](../../web/agent.html#L253) | 253 | `"  [r.pages_content_extracted??r.pages_fetched??\"غير محدد\",\"صفحة استُخرج منها نص\"],"` | — |
| [SRC-DE7EABE998-L000254](../../web/agent.html#L254) | 254 | `"  [r.pages_partial_extracted??\"غير محدد\",\"صفحة استُخرج جزء من نصها\"],"` | — |
| [SRC-DE7EABE998-L000255](../../web/agent.html#L255) | 255 | `"  [r.pages_extract_failed??\"غير محدد\",\"صفحة فشل استخراج نصها\"]"` | — |
| [SRC-DE7EABE998-L000256](../../web/agent.html#L256) | 256 | `" ];"` | — |
| [SRC-DE7EABE998-L000257](../../web/agent.html#L257) | 257 | `" const operationalHtml='<div class=\"metrics\">'+operationalMetrics.map(([v,l])=>'<div class=\"metric\"><strong>'+escapeHtml(v)+'</strong><span>'+escapeHtml(l)+'</span></div>').join(\"\")+'</div>';"` | — |
| [SRC-DE7EABE998-L000258](../../web/agent.html#L258) | 258 | `" const connectors=r.connector_summary&&Array.isArray(r.connector_summary.connectors)?r.connector_summary.connectors:[];"` | — |
| [SRC-DE7EABE998-L000259](../../web/agent.html#L259) | 259 | `" const connectorDetails=connectors.length?'<details class=\"details\"><summary>تشخيص الموصلات في هذا الطلب ('+connectors.length+')</summary><div>'+connectors.map(c=>'<article class=\"source\"><strong>'+escapeHtml(c.name\|\|\"موصل\")+' · '+escapeHtml(c.status\|\|\"unknown\")+'</strong><p>الإعداد: '+escapeHtml(c.configuration_status\|\|\"unknown\")+' · تمت المحاولة: '+escapeHtml(c.attempted===true?\"نعم\":c.attempted===false?\"لا\":\"غير محسوم\")+' · متاح في هذا الطلب: '+escapeHtml(c.available_for_this_request===true?\"نعم\":c.available_for_this_request===false?\"لا\":\"غير محسوم\")+' · استجابة المعالجة مؤكدة: '+escapeHtml(c.verified_for_this_request===true?\"نعم\":c.verified_for_this_request===false?\"لا\":\"غير مختبر/غير محسوم\")+' · إخفاق ملاحظ: '+escapeHtml(c.failure_observed===true?\"نعم\":\"لا\")+' · مرشحون أوليون من الموصل: '+escapeHtml(c.result_count??\"غير محدد\")+' · اجتازوا فحص الموصل: '+escapeHtml(c.accepted_count??\"غير محدد\")+' · مصادر نهائية منسوبة إليه: '+escapeHtml(c.useful_result_count??\"غير محدد\")+' · مرفوض: '+escapeHtml(c.rejected_count??\"غير محدد\")+' · توزيع الرفض: '+escapeHtml(c.rejection_counts_observed===true&&c.rejection_counts?('مرشح مشوّه '+(c.rejection_counts.malformed_candidate??0)+'؛ رابط غير صالح/هدف غير آمن '+(c.rejection_counts.invalid_url_or_unsafe_target??0)+'؛ نطاق محظور '+(c.rejection_counts.blocked_domain??0)+'؛ صلة ضعيفة '+(c.rejection_counts.relevance_below_threshold??0)):'غير مسجل في هذه الجولة')+' · كل المرشحين رُفضوا: '+escapeHtml(c.candidate_rejection_observed===true?\"نعم\":c.candidate_rejection_observed===false?\"لا\":\"غير محسوم\")+'</p>'+((Array.isArray(c.queries)&&c.queries.length)?'<p>استعلامات: '+c.queries.map(escapeHtml).join(\" · \")+'</p>':\"\")+((Array.isArray(c.errors)&&c.errors.length)?'<p class=\"warning\">أخطاء: '+c.errors.map(escapeHtml).join(\" · \")+'</p>':\"\")+'</article>').join(\"\")+'</div></details>':\"\";"` | — |
| [SRC-DE7EABE998-L000260](../../web/agent.html#L260) | 260 | `" const integrity=r.answer_integrity&&typeof r.answer_integrity===\"object\"?r.answer_integrity:null;"` | — |
| [SRC-DE7EABE998-L000261](../../web/agent.html#L261) | 261 | `" const integrityNumbers=integrity&&Array.isArray(integrity.potentially_unsupported_numeric_literals)?integrity.potentially_unsupported_numeric_literals:[];"` | — |
| [SRC-DE7EABE998-L000262](../../web/agent.html#L262) | 262 | `" const integrityTargets=integrity&&Array.isArray(integrity.target_coverage)?integrity.target_coverage:[];"` | — |
| [SRC-DE7EABE998-L000263](../../web/agent.html#L263) | 263 | `" const requirementEvidence=integrity&&Array.isArray(integrity.requirement_evidence)?integrity.requirement_evidence:[];"` | — |
| [SRC-DE7EABE998-L000264](../../web/agent.html#L264) | 264 | `" const requirementEvidenceHtml=requirementEvidence.length?'<p class=\"report-note\">سجل الأدلة لكل محور — إشارات لفظية وربط استعلامات، وليست إثباتًا لصحة الادعاءات:</p><ul>'+requirementEvidence.map(item=>{const statusText=({candidate_evidence_found_not_verified:\"وُجد نص مرشح مطابق لفظيًا؛ لم تُتحقق دلالته.\",query_returned_candidates_no_lexical_signal:\"عاد الاستعلام بمصادر، لكن لم يظهر تطابق لفظي كافٍ داخل النص.\",no_candidate_evidence_found:\"لم تُسجل أدلة مرشحة لهذا المحور في النتائج المتاحة.\",query_result_linkage_unavailable:\"تعذر ربط النتائج بالاستعلام المخصص لهذا المحور.\",query_not_available:\"لا يوجد استعلام مخصص مسجل لهذا المحور.\"})[item.status]\|\|\"الحالة غير محسومة.\";const ids=Array.isArray(item.candidate_source_indexes)?item.candidate_source_indexes:[];const qids=Array.isArray(item.query_result_source_indexes)?item.query_result_source_indexes:[];return '<li><strong>'+escapeHtml(item.target\|\|\"محور\")+':</strong> '+escapeHtml(statusText)+(ids.length?' — مرشحو الدليل: '+ids.map(n=>\"المصدر \"+escapeHtml(n)).join(\"، \"):\"\")+(qids.length?' — نتائج الاستعلام: '+qids.map(n=>\"المصدر \"+escapeHtml(n)).join(\"، \"):\"\")+'</li>';}).join(\"\")+'</ul>':\"\";"` | — |
| [SRC-DE7EABE998-L000265](../../web/agent.html#L265) | 265 | `" const citationNumericSupport=integrity&&Array.isArray(integrity.citation_numeric_support)?integrity.citation_numeric_support:[];"` | — |
| [SRC-DE7EABE998-L000266](../../web/agent.html#L266) | 266 | `" const citedNumberIssues=citationNumericSupport.filter(item=>item&&Array.isArray(item.potentially_unsupported_numeric_literals)&&item.potentially_unsupported_numeric_literals.length);"` | — |
| [SRC-DE7EABE998-L000267](../../web/agent.html#L267) | 267 | `" const citedNumberHtml=citedNumberIssues.length?'<p class=\"warning\">وجد الفحص أرقامًا قد لا يسندها المصدر المحدد في الاستشهاد؛ راجع المقتطف أو نص الصفحة الأصلي.</p><ul>'+citedNumberIssues.map(item=>'<li>الجملة '+escapeHtml(item.sentence_number??\"غير محدد\")+' · الرقم: '+item.potentially_unsupported_numeric_literals.map(escapeHtml).join(\"، \")+' · الاستشهادات: '+(Array.isArray(item.cited_source_indexes)?item.cited_source_indexes.map(n=>'المصدر '+escapeHtml(n)).join(\"، \"):\"غير محددة\")+'</li>').join(\"\")+'</ul>':\"\";"` | — |
| [SRC-DE7EABE998-L000268](../../web/agent.html#L268) | 268 | `" const valueDiscrepancies=integrity&&Array.isArray(integrity.potential_value_discrepancies)?integrity.potential_value_discrepancies:[];"` | — |
| [SRC-DE7EABE998-L000269](../../web/agent.html#L269) | 269 | `" const valueDimensionLabels={price_or_cost:\"السعر/التكلفة\",area_or_size:\"المساحة/الحجم\",duration:\"المدة\",percentage_or_rate:\"النسبة\",date_or_year:\"التاريخ/السنة\"};"` | — |
| [SRC-DE7EABE998-L000270](../../web/agent.html#L270) | 270 | `" const valueDiscrepancyHtml=valueDiscrepancies.length?'<p class=\"warning\">رُصدت قيم مختلفة في مصادر متعددة. قد يكون الاختلاف بين منتجات أو فترات أو وحدات مختلفة؛ هذه ليست إثباتًا تلقائيًا لوجود تناقض.</p><ul>'+valueDiscrepancies.map(item=>'<li>'+escapeHtml(valueDimensionLabels[item.dimension]\|\|item.dimension\|\|\"قيمة\")+' — '+(Array.isArray(item.values)?item.values.map(value=>escapeHtml(value.value)+' ('+(Array.isArray(value.source_indexes)?value.source_indexes.map(n=>'المصدر '+escapeHtml(n)).join(\"، \"):\"مصدر غير محدد\")+')').join(' مقابل '):\"قِيَم تحتاج مراجعة\")+'</li>').join(\"\")+'</ul>':\"\";"` | — |
| [SRC-DE7EABE998-L000271](../../web/agent.html#L271) | 271 | `" const citationAlignment=integrity&&Array.isArray(integrity.citation_lexical_alignment)?integrity.citation_lexical_alignment:[];"` | — |
| [SRC-DE7EABE998-L000272](../../web/agent.html#L272) | 272 | `" const weakCitationAlignment=citationAlignment.filter(item=>item&&item.status===\"weak_lexical_overlap\");"` | — |
| [SRC-DE7EABE998-L000273](../../web/agent.html#L273) | 273 | `" const citationAlignmentHtml=citationAlignment.length?'<p class=\"report-note\">'+(weakCitationAlignment.length?'لم يظهر تطابق لفظي كافٍ في '+weakCitationAlignment.length+' جملة/جمل مستشهد بها؛ راجع الاستشهادات يدويًا.':'ظهرت إشارات تطابق لفظي لبعض الجمل المستشهد بها، لكنها لا تثبت أن المصدر يسند الادعاء.')+'</p>':\"\";"` | — |
| [SRC-DE7EABE998-L000274](../../web/agent.html#L274) | 274 | `" const integrityScope=integrity?({contains_extracted_page_text_and_or_snippets:\"نص صفحات مستخرج مع مقتطفات بحث\",search_snippets_only:\"مقتطفات بحث فقط — لم يؤكد النظام قراءة نص الصفحات\",no_readable_source_text:\"لا يتوفر نص مصدر قابل للفحص\"}[integrity.source_evidence_scope]\|\|integrity.source_evidence_scope\|\|\"غير محدد\"):\"غير محدد\";"` | — |
| [SRC-DE7EABE998-L000275](../../web/agent.html#L275) | 275 | `" const integritySummary=integrity?'<p class=\"report-note\">عدادات الفحص اللفظي: '+escapeHtml(integrity.potentially_unsupported_numeric_count??0)+' رقم لم يظهر نصيًا في الأدلة؛ '+escapeHtml(integrity.potentially_unsupported_numeric_by_citation_count??0)+' رقم لا يسنده المصدر المشار إليه تحديدًا؛ '+escapeHtml(integrity.potential_value_discrepancy_count??0)+' اختلاف قيمة يحتاج مطابقة؛ '+escapeHtml(integrity.potentially_missing_target_count??0)+' محور محتمل النقص؛ '+escapeHtml(integrity.source_evidence_gap_count??0)+' محور بلا إشارة لفظية في المصادر.</p>':\"\";"` | — |
| [SRC-DE7EABE998-L000276](../../web/agent.html#L276) | 276 | `" const taskFulfillmentStatus=r.task_fulfillment_status\|\|result.task_fulfillment_status\|\|\"not_machine_assessed_no_explicit_targets_detected\";"` | — |
| [SRC-DE7EABE998-L000277](../../web/agent.html#L277) | 277 | `" const taskFulfillmentText=({"` | — |
| [SRC-DE7EABE998-L000278](../../web/agent.html#L278) | 278 | `"  possible_gap_detected:\"قد تكون الإجابة أغفلت محورًا من السؤال؛ هذه إشارة لفظية تحتاج مراجعة وليست حكمًا نهائيًا.\","` | — |
| [SRC-DE7EABE998-L000279](../../web/agent.html#L279) | 279 | `"  lexical_signals_found_not_semantically_verified:\"ظهرت إشارات لفظية للمحاور المستخرجة، لكن هذا لا يثبت اكتمال المهمة.\","` | — |
| [SRC-DE7EABE998-L000280](../../web/agent.html#L280) | 280 | `"  candidate_evidence_gaps_or_linkage_unknown:\"لا توجد إشارات نصية كافية لبعض المحاور أو تعذر ربط نتائج البحث بها؛ راجع الاستعلامات والمصادر قبل اعتماد الإجابة.\","` | — |
| [SRC-DE7EABE998-L000281](../../web/agent.html#L281) | 281 | `"  not_assessed_insufficient_evidence:\"الأدلة غير كافية؛ لم يتم التحقق من اكتمال المهمة.\","` | — |
| [SRC-DE7EABE998-L000282](../../web/agent.html#L282) | 282 | `"  not_machine_assessed_no_explicit_targets_detected:\"لم تُستخرج محاور صريحة قابلة للفحص؛ اكتمال المهمة لم يُقيّم آليًا.\""` | — |
| [SRC-DE7EABE998-L000283](../../web/agent.html#L283) | 283 | `" })[taskFulfillmentStatus]\|\|\"حالة اكتمال المهمة غير محسومة آليًا.\";"` | — |
| [SRC-DE7EABE998-L000284](../../web/agent.html#L284) | 284 | `" const taskFulfillmentHtml='<p class=\"'+([\"possible_gap_detected\",\"candidate_evidence_gaps_or_linkage_unknown\"].includes(taskFulfillmentStatus)?\"warning\":\"report-note\")+'\">حالة تنفيذ المطلوب: '+escapeHtml(taskFulfillmentText)+'</p>';"` | — |
| [SRC-DE7EABE998-L000285](../../web/agent.html#L285) | 285 | `" const coverageRepairStatus=r.coverage_repair_status\|\|result.coverage_repair_status\|\|\"\";"` | — |
| [SRC-DE7EABE998-L000286](../../web/agent.html#L286) | 286 | `" const coverageRepairMessages={"` | — |
| [SRC-DE7EABE998-L000287](../../web/agent.html#L287) | 287 | `"  revised_and_reaudited:\"عُدّلت الإجابة بعد رصد محور محتمل النقص ثم خضعت لمراجعة أدلة ثانية؛ تظل المراجعة بمساعدة نموذج وليست تحققًا مستقلًا.\","` | — |
| [SRC-DE7EABE998-L000288](../../web/agent.html#L288) | 288 | `"  revised_and_reaudited_remaining_gaps:\"خضعت الإجابة المعدلة لمراجعة ثانية، لكن بقي محور محتمل النقص؛ لا تعتبر المهمة مكتملة قبل مراجعة الأدلة.\","` | — |
| [SRC-DE7EABE998-L000289](../../web/agent.html#L289) | 289 | `"  reaudit_budget_exhausted:\"انتهت ميزانية النماذج قبل إعادة تدقيق الإجابة المعدلة؛ عُرضت مقتطفات المصادر بدل اعتبار النص المعدل إجابة مكتملة.\","` | — |
| [SRC-DE7EABE998-L000290](../../web/agent.html#L290) | 290 | `"  reaudit_unavailable:\"تعذرت إعادة تدقيق الإجابة المعدلة؛ عُرضت مقتطفات المصادر بدل اعتبار النص المعدل إجابة مكتملة.\","` | — |
| [SRC-DE7EABE998-L000291](../../web/agent.html#L291) | 291 | `"  budget_exhausted:\"انتهت ميزانية النماذج قبل استكمال محور محتمل النقص.\","` | — |
| [SRC-DE7EABE998-L000292](../../web/agent.html#L292) | 292 | `"  unavailable:\"تعذرت محاولة إصلاح محور محتمل النقص.\","` | — |
| [SRC-DE7EABE998-L000293](../../web/agent.html#L293) | 293 | `"  no_change_gap_unresolved:\"لم تغيّر محاولة الإصلاح الإجابة؛ لا يزال احتمال نقص أحد المحاور قائمًا.\","` | — |
| [SRC-DE7EABE998-L000294](../../web/agent.html#L294) | 294 | `"  source_evidence_gap_unresolved:\"ذُكرت المحاور في الإجابة، لكن لم تظهر لها إشارات لفظية في المصادر؛ تظل غير محسومة.\""` | — |
| [SRC-DE7EABE998-L000295](../../web/agent.html#L295) | 295 | `" };"` | — |
| [SRC-DE7EABE998-L000296](../../web/agent.html#L296) | 296 | `" const coverageRepairHtml=coverageRepairMessages[coverageRepairStatus]?'<p class=\"warning\">حالة إصلاح التغطية: '+escapeHtml(coverageRepairMessages[coverageRepairStatus])+'</p>':\"\";"` | — |
| [SRC-DE7EABE998-L000297](../../web/agent.html#L297) | 297 | `" const criterionGapResearch=r.criterion_gap_research\|\|(result.search_report&&result.search_report.criterion_gap_research)\|\|{};"` | — |
| [SRC-DE7EABE998-L000298](../../web/agent.html#L298) | 298 | `" const criterionGapResearchStatus=criterionGapResearch.status\|\|\"\";"` | — |
| [SRC-DE7EABE998-L000299](../../web/agent.html#L299) | 299 | `" const criterionGapResearchMessages={"` | — |
| [SRC-DE7EABE998-L000300](../../web/agent.html#L300) | 300 | `"  not_needed:\"لم يرصد الفحص فجوة مصدر تستدعي بحثًا إضافيًا.\","` | — |
| [SRC-DE7EABE998-L000301](../../web/agent.html#L301) | 301 | `"  evidence_added_and_answer_regenerated:\"أضاف البحث الإضافي نص مصدر جديدًا؛ ثم أُعيد توليد الإجابة ومراجعتها.\","` | — |
| [SRC-DE7EABE998-L000302](../../web/agent.html#L302) | 302 | `"  search_completed_no_new_criterion_evidence:\"أُجري بحث إضافي للمحاور الناقصة، لكنه لم يضف نص مصدر جديدًا يمكن تمييزه.\","` | — |
| [SRC-DE7EABE998-L000303](../../web/agent.html#L303) | 303 | `"  skipped_no_reserved_search_slot:\"لم يُخصّص استعلام إضافي لهذه المهمة؛ ظلت المحاور بلا إشارة مصدر غير محسومة.\","` | — |
| [SRC-DE7EABE998-L000304](../../web/agent.html#L304) | 304 | `"  skipped_search_budget_exhausted:\"انتهت ميزانية البحث قبل إعادة البحث عن المحاور الناقصة؛ لا تُعدّ التغطية مكتملة.\","` | — |
| [SRC-DE7EABE998-L000305](../../web/agent.html#L305) | 305 | `"  search_failed:\"تعذر إكمال البحث الإضافي عن الأدلة المفقودة.\","` | — |
| [SRC-DE7EABE998-L000306](../../web/agent.html#L306) | 306 | `"  skipped_no_request_budget:\"تعذر فحص ميزانية البحث؛ لم يُنفذ بحث إضافي.\","` | — |
| [SRC-DE7EABE998-L000307](../../web/agent.html#L307) | 307 | `"  skipped_query_not_distinct:\"لم يُنفذ بحث إضافي لأن الاستعلام المقترح لم يكن مختلفًا بما يكفي.\","` | — |
| [SRC-DE7EABE998-L000308](../../web/agent.html#L308) | 308 | `"  skipped_no_valid_query:\"لم يتوفر استعلام إضافي صالح للمحاور الناقصة.\","` | — |
| [SRC-DE7EABE998-L000309](../../web/agent.html#L309) | 309 | `"  evidence_added_but_regeneration_unavailable:\"وصل نص مصدر إضافي، لكن تعذرت إعادة توليد الإجابة ومراجعتها؛ يلزم التحقق من المحاور يدويًا.\""` | — |
| [SRC-DE7EABE998-L000310](../../web/agent.html#L310) | 310 | `" };"` | — |
| [SRC-DE7EABE998-L000311](../../web/agent.html#L311) | 311 | `" const criterionGapResearchHtml=criterionGapResearchMessages[criterionGapResearchStatus]?'<p class=\"'+(criterionGapResearchStatus===\"evidence_added_and_answer_regenerated\"?\"report-note\":\"warning\")+'\">بحث فجوة الأدلة: '+escapeHtml(criterionGapResearchMessages[criterionGapResearchStatus])+'</p>':\"\";"` | — |
| [SRC-DE7EABE998-L000312](../../web/agent.html#L312) | 312 | `" const claimLedger=r.claim_evidence_ledger&&typeof r.claim_evidence_ledger===\"object\"?r.claim_evidence_ledger:null;"` | — |
| [SRC-DE7EABE998-L000313](../../web/agent.html#L313) | 313 | `" const claimSegments=claimLedger&&Array.isArray(claimLedger.segments)?claimLedger.segments:[];"` | — |
| [SRC-DE7EABE998-L000314](../../web/agent.html#L314) | 314 | `" const claimSummary=claimLedger&&claimLedger.summary&&typeof claimLedger.summary===\"object\"?claimLedger.summary:{};"` | — |
| [SRC-DE7EABE998-L000315](../../web/agent.html#L315) | 315 | `" const claimEvidenceHtml=claimLedger?'<p class=\"report-note\">سجل تتبع الاستشهادات (لا يثبت صحة الادعاء): '+escapeHtml(claimSummary.segments_with_citations??0)+' مقطعًا يحمل استشهادًا، '+escapeHtml(claimSummary.segments_without_citation_markers??0)+' بلا علامة استشهاد، '+escapeHtml(claimSummary.out_of_range_reference_count??0)+' مرجعًا خارج نطاق المصادر، '+escapeHtml(claimSummary.cited_segments_with_readable_source_evidence??0)+' مقطعًا مستشهدًا به له نص دليل قابل للقراءة.</p>'+(claimSegments.length?'<details class=\"details\"><summary>عرض سجل المقاطع والاستشهادات المرتبطة</summary><ol>'+claimSegments.map(item=>'<li><p>'+escapeHtml(item.text\|\|\"\")+'</p><p class=\"report-note\">الحالة: '+escapeHtml(item.citation_status\|\|\"غير محدد\")+' · الفحص اللفظي: '+escapeHtml(item.lexical_audit_status\|\|\"غير منفذ\")+'</p>'+(Array.isArray(item.sources)&&item.sources.length?'<ul>'+item.sources.map(source=>'<li>المصدر '+escapeHtml(source.source_index)+' · '+escapeHtml(source.title\|\|\"دون عنوان\")+' · '+escapeHtml(source.evidence_basis\|\|\"غير معروف\")+(source.url?' · <a href=\"'+escapeHtml(source.url)+'\" target=\"_blank\" rel=\"noopener noreferrer\">فتح المصدر</a>':\"\")+'</li>').join(\"\")+'</ul>':\"\")+'</li>').join(\"\")+'</ol><p class=\"report-note\">السجل يربط علامات الاستشهاد بقائمة المصادر المتاحة فقط؛ لا يُجري تحققًا دلاليًا أو مستقلًا من الحقيقة.</p></details>':\"\"):\"\";"` | — |
| [SRC-DE7EABE998-L000316](../../web/agent.html#L316) | 316 | `" const integrityHtml=integrity?'<details class=\"details\"><summary>فحص لفظي أولي: اتساق الإجابة مع الأدلة — ليس تحققًا من الحقيقة</summary><p class=\"report-note\">لا يثبت هذا الفحص صحة الوقائع أو دلالة الاستشهاد. نطاق الأدلة النصية: '+escapeHtml(integrityScope)+'.</p>'+integritySummary+taskFulfillmentHtml+claimEvidenceHtml+coverageRepairHtml+requirementEvidenceHtml+criterionGapResearchHtml+'<p class=\"report-note\">'+(integrityNumbers.length?'أرقام أو تواريخ تحتاج مراجعة لأنها لم تظهر نصيًا في المواد المتاحة: '+integrityNumbers.map(escapeHtml).join(\"، \")+'.':'لم يرصد الفحص أرقامًا محددة غائبة عن النصوص التي جمعها. هذا لا يثبت أن كل رقم صحيح أو أن المصدر يدعم الادعاء المرتبط به.')+'</p>'+citedNumberHtml+valueDiscrepancyHtml+citationAlignmentHtml+(integrityTargets.length?'<p class=\"report-note\">إشارات التغطية اللفظية لمحاور السؤال:</p><ul>'+integrityTargets.map(t=>'<li>'+escapeHtml(t.target\|\|\"محور\")+' — '+escapeHtml(t.status===\"lexical_signal_found\"?\"وُجد تطابق لفظي في الإجابة؛ ليس إثباتًا لاكتمالها\":\"قد يكون هذا المحور ناقصًا؛ لم يظهر تطابق لفظي كافٍ في الإجابة\")+' · '+escapeHtml(t.source_evidence_status===\"source_lexical_signal_found\"?\"توجد إشارة لفظية في المصادر\":\"لا توجد إشارة لفظية في المصادر\")+(Array.isArray(t.source_evidence_checks)&&t.source_evidence_checks.length?' ('+t.source_evidence_checks.map(item=>'المصدر '+escapeHtml(item.source_index)).join('، ')+')':'')+'</li>').join(\"\")+'</ul>':\"\")+'<p class=\"report-note\">المنهج: فحص لفظي حتمي محدود. لا يتحقق من معنى الادعاء أو صلة الاستشهاد به أو استقلال المصادر؛ راجع الأدلة الأصلية قبل الاعتماد.</p></details>':\"\";"` | — |
| [SRC-DE7EABE998-L000317](../../web/agent.html#L317) | 317 | `" const providerCounts=r.provider_counts&&typeof r.provider_counts===\"object\"&&!Array.isArray(r.provider_counts)?r.provider_counts:{};"` | — |
| [SRC-DE7EABE998-L000318](../../web/agent.html#L318) | 318 | `" const providerHtml=Object.entries(providerCounts).map(([p,n])=>'<span class=\"provider\">'+escapeHtml(p)+' · '+escapeHtml(n)+'</span>').join(\"\");"` | — |
| [SRC-DE7EABE998-L000319](../../web/agent.html#L319) | 319 | `" const notes=Array.isArray(e.warnings)?e.warnings:[];"` | — |
| [SRC-DE7EABE998-L000320](../../web/agent.html#L320) | 320 | `" const queryList=Array.isArray(result.search_queries)?result.search_queries:[];"` | — |
| [SRC-DE7EABE998-L000321](../../web/agent.html#L321) | 321 | `" const details=queryList.length?'<details class=\"details\"><summary>زوايا البحث المستخدمة ('+queryList.length+')</summary><ol>'+queryList.map(q=>'<li>'+escapeHtml(q)+'</li>').join(\"\")+'</ol></details>':\"\";"` | — |
| [SRC-DE7EABE998-L000322](../../web/agent.html#L322) | 322 | `" const coverageText=lead"` | — |
| [SRC-DE7EABE998-L000323](../../web/agent.html#L323) | 323 | `"  ? (leadResearchIncomplete"` | — |
| [SRC-DE7EABE998-L000324](../../web/agent.html#L324) | 324 | `"     ? \"تعطل البحث أو لم يكتمل التقرير؛ الأعداد غير المتاحة ليست صفرًا، ولا يمكن استنتاج عدم وجود عملاء.\""` | — |
| [SRC-DE7EABE998-L000325](../../web/agent.html#L325) | 325 | `"     : noQualifiedLeads"` | — |
| [SRC-DE7EABE998-L000326](../../web/agent.html#L326) | 326 | `"      ? \"لم تثبت النتائج وجود أي عميل محتمل. عدد صفحات العقارات أو النطاقات ليس عدد المشترين.\""` | — |
| [SRC-DE7EABE998-L000327](../../web/agent.html#L327) | 327 | `"      : \"الإشارات العلنية لا تثبت هوية الشخص أو استمرار رغبته في الشراء؛ راجع نص المصدر وتاريخه يدويًا.\")"` | — |
| [SRC-DE7EABE998-L000328](../../web/agent.html#L328) | 328 | `"  : researchErrorOutcome"` | — |
| [SRC-DE7EABE998-L000329](../../web/agent.html#L329) | 329 | `"   ? \"تعذر تحديد تغطية البحث لأن مسار تجميع الأدلة لم يكتمل؛ الأرقام غير المتاحة ليست صفرًا.\""` | — |
| [SRC-DE7EABE998-L000330](../../web/agent.html#L330) | 330 | `"   : \"تغطية الأدلة: \"+scoreLabel+\" — يصف هذا الوصف اتساع الأدلة المتاحة ولا يمثل احتمال صحة الإجابة.\";"` | — |
| [SRC-DE7EABE998-L000331](../../web/agent.html#L331) | 331 | `" const usableSourceCount=researchErrorOutcome?null:(r.usable_sources_after_filtering??sources.length);"` | — |
| [SRC-DE7EABE998-L000332](../../web/agent.html#L332) | 332 | `" const attemptText=result&&result.search_attempted===true"` | — |
| [SRC-DE7EABE998-L000333](../../web/agent.html#L333) | 333 | `"  ? (r.search_outcome===\"attempted_research_error\""` | — |
| [SRC-DE7EABE998-L000334](../../web/agent.html#L334) | 334 | `"     ? \"بدأت محاولة البحث، لكن تعطل مسار تجميع الأدلة قبل اكتمال التقرير؛ لم يمكن تحديد عدد المصادر القابلة للاستخدام.\""` | — |
| [SRC-DE7EABE998-L000335](../../web/agent.html#L335) | 335 | `"     : \"تمت محاولة البحث في الويب. عدد المصادر القابلة للاستخدام بعد التصفية: \"+(usableSourceCount??\"غير محدد\")+\".\")"` | — |
| [SRC-DE7EABE998-L000336](../../web/agent.html#L336) | 336 | `"  : result&&result.search_attempted===false"` | — |
| [SRC-DE7EABE998-L000337](../../web/agent.html#L337) | 337 | `"   ? \"لم تُنفّذ محاولة بحث ويب في هذه الجولة.\""` | — |
| [SRC-DE7EABE998-L000338](../../web/agent.html#L338) | 338 | `"   : r.search_outcome===\"unknown_after_research_error\""` | — |
| [SRC-DE7EABE998-L000339](../../web/agent.html#L339) | 339 | `"    ? \"تعطل مسار البحث، ولم يمكن تأكيد ما إذا كانت محاولة البحث قد بدأت أو كم مصدرًا كان قابلًا للاستخدام.\""` | — |
| [SRC-DE7EABE998-L000340](../../web/agent.html#L340) | 340 | `"    : \"حالة محاولة البحث غير موضحة في الاستجابة.\";"` | — |
| [SRC-DE7EABE998-L000341](../../web/agent.html#L341) | 341 | `" const qualityText='تصنيف جودة البحث يصف تغطية العملية والأدلة المتاحة، ولا يمثل احتمال صحة الوقائع.';"` | — |
| [SRC-DE7EABE998-L000342](../../web/agent.html#L342) | 342 | `" const reviewText=r.claim_audit_semantics==='model_assisted_not_independent_fact_check'?'مراجعة الادعاءات تمت بمساعدة نموذج لغوي؛ وهي ليست تحققًا مستقلًا من صحة الحقائق.':'لم يثبت إجراء تحقق مستقل من صحة الحقائق.';"` | — |
| [SRC-DE7EABE998-L000343](../../web/agent.html#L343) | 343 | `" const diversityText='اختلاف النطاقات المسجلة لا يثبت الاستقلال التحريري؛ فقد تنقل المواقع عن مصدر أصلي واحد.';"` | — |
| [SRC-DE7EABE998-L000344](../../web/agent.html#L344) | 344 | `" const reportNotes=[coverageText,attemptText,qualityText,reviewText,diversityText,...notes].map(n=>'<p class=\"report-note\">'+escapeHtml(n)+'</p>').join(\"\");"` | — |
| [SRC-DE7EABE998-L000345](../../web/agent.html#L345) | 345 | `" const review=r.second_pass_review===\"model_claim_audit_completed\"?\"مراجعة الادعاءات بمساعدة النموذج تمت (ليست تحققًا مستقلًا)\":r.second_pass_review===\"model_claim_audit_completed_before_coverage_repair\"?\"تمت مراجعة المسودة قبل تعديل التغطية؛ النسخة المعدلة لم تخضع لمراجعة ثانية\":r.second_pass_review===\"model_claim_audit_unavailable\"?\"تعذرت مراجعة الادعاءات بمساعدة النموذج\":\"\";"` | — |
| [SRC-DE7EABE998-L000346](../../web/agent.html#L346) | 346 | `" return '<div class=\"report-head\"><b>ملخص الأدلة وتغطية البحث</b><span class=\"coverage\">'+escapeHtml(scoreLabel)+'</span></div><div class=\"metrics\">'+metricHtml+'</div>'+completionSummary+completionDetailsHtml+operationalHtml+connectorDetails+integrityHtml+reportNotes+(providerHtml?'<div class=\"providers\">'+providerHtml+'</div>':\"\")+(review?'<p class=\"report-note\">'+escapeHtml(review)+'</p>':\"\")+details;"` | — |
| [SRC-DE7EABE998-L000347](../../web/agent.html#L347) | 347 | `"}"` | — |
| [SRC-DE7EABE998-L000348](../../web/agent.html#L348) | 348 | `"function addMessage(role,text,result,options={}){"` | — |
| [SRC-DE7EABE998-L000349](../../web/agent.html#L349) | 349 | `" const welcome=$(\"welcome\");if(welcome)welcome.remove();"` | — |
| [SRC-DE7EABE998-L000350](../../web/agent.html#L350) | 350 | `" const box=document.createElement(\"div\");box.className=\"message \"+(role===\"user\"?\"user\":\"assistant\");"` | — |
| [SRC-DE7EABE998-L000351](../../web/agent.html#L351) | 351 | `" const who=document.createElement(\"div\");who.className=\"who\";"` | — |
| [SRC-DE7EABE998-L000352](../../web/agent.html#L352) | 352 | `" who.textContent=role===\"user\"?\"أنت\":(result&&result.used_language_model?\"Omarai · بحث وتحليل توليدي\":\"Omarai · إجابة جزئية أو احتياطية\");"` | — |
| [SRC-DE7EABE998-L000353](../../web/agent.html#L353) | 353 | `" box.appendChild(who);"` | — |
| [SRC-DE7EABE998-L000354](../../web/agent.html#L354) | 354 | `" const linkedQuestion=(options&&options.question)\|\|(result&&result.question);"` | — |
| [SRC-DE7EABE998-L000355](../../web/agent.html#L355) | 355 | `" if(role===\"assistant\"&&linkedQuestion){"` | — |
| [SRC-DE7EABE998-L000356](../../web/agent.html#L356) | 356 | `"  const context=document.createElement(\"div\");context.className=\"message-context\";"` | — |
| [SRC-DE7EABE998-L000357](../../web/agent.html#L357) | 357 | `"  context.textContent=\"ردًا على السؤال: \"+linkedQuestion;box.appendChild(context);"` | — |
