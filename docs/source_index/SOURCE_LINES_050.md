# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **050**
- سجلات الأسطر: **800**
- النطاق: SRC-F725E90B2A-L003632 إلى SRC-DE7EABE998-L000064
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-F725E90B2A — [tests/test_web_agent.py](../../tests/test_web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-F725E90B2A-L003632](../../tests/test_web_agent.py#L3632) | 3632 | `"def test_criterion_gap_repair_cannot_reintroduce_non_social_source(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003633](../../tests/test_web_agent.py#L3633) | 3633 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003634](../../tests/test_web_agent.py#L3634) | 3634 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L003635](../../tests/test_web_agent.py#L3635) | 3635 | `"    question = ("` | — |
| [SRC-F725E90B2A-L003636](../../tests/test_web_agent.py#L3636) | 3636 | `"        \"قارن بين خدمتين من حيث السعر والخصوصية والاعتمادية \""` | — |
| [SRC-F725E90B2A-L003637](../../tests/test_web_agent.py#L3637) | 3637 | `"        \"واعرض آراء وتجارب المستخدمين\""` | — |
| [SRC-F725E90B2A-L003638](../../tests/test_web_agent.py#L3638) | 3638 | `"    )"` | — |
| [SRC-F725E90B2A-L003639](../../tests/test_web_agent.py#L3639) | 3639 | `"    initial_sources = ["` | — |
| [SRC-F725E90B2A-L003640](../../tests/test_web_agent.py#L3640) | 3640 | `"        {"` | — |
| [SRC-F725E90B2A-L003641](../../tests/test_web_agent.py#L3641) | 3641 | `"            **sample_source(0),"` | — |
| [SRC-F725E90B2A-L003642](../../tests/test_web_agent.py#L3642) | 3642 | `"            \"url\": \"https://www.reddit.com/r/example/comments/1\","` | — |
| [SRC-F725E90B2A-L003643](../../tests/test_web_agent.py#L3643) | 3643 | `"            \"domain\": \"reddit.com\","` | — |
| [SRC-F725E90B2A-L003644](../../tests/test_web_agent.py#L3644) | 3644 | `"            \"title\": \"مناقشة تجارب المستخدمين للخدمتين\","` | — |
| [SRC-F725E90B2A-L003645](../../tests/test_web_agent.py#L3645) | 3645 | `"            \"snippet\": \"تجارب وآراء مستخدمين حول الخدمتين\","` | — |
| [SRC-F725E90B2A-L003646](../../tests/test_web_agent.py#L3646) | 3646 | `"            \"page_text\": \"تجارب وآراء مستخدمين حول الخدمتين\","` | — |
| [SRC-F725E90B2A-L003647](../../tests/test_web_agent.py#L3647) | 3647 | `"            \"platform\": \"reddit\","` | — |
| [SRC-F725E90B2A-L003648](../../tests/test_web_agent.py#L3648) | 3648 | `"            \"providers\": [\"reddit\"],"` | — |
| [SRC-F725E90B2A-L003649](../../tests/test_web_agent.py#L3649) | 3649 | `"        },"` | — |
| [SRC-F725E90B2A-L003650](../../tests/test_web_agent.py#L3650) | 3650 | `"        {"` | — |
| [SRC-F725E90B2A-L003651](../../tests/test_web_agent.py#L3651) | 3651 | `"            **sample_source(1),"` | — |
| [SRC-F725E90B2A-L003652](../../tests/test_web_agent.py#L3652) | 3652 | `"            \"url\": \"https://www.reddit.com/r/example/comments/2\","` | — |
| [SRC-F725E90B2A-L003653](../../tests/test_web_agent.py#L3653) | 3653 | `"            \"domain\": \"reddit.com\","` | — |
| [SRC-F725E90B2A-L003654](../../tests/test_web_agent.py#L3654) | 3654 | `"            \"title\": \"مناقشة أخرى عن الخدمتين\","` | — |
| [SRC-F725E90B2A-L003655](../../tests/test_web_agent.py#L3655) | 3655 | `"            \"snippet\": \"مناقشة وتجارب مستخدمين حول الخدمتين\","` | — |
| [SRC-F725E90B2A-L003656](../../tests/test_web_agent.py#L3656) | 3656 | `"            \"page_text\": \"مناقشة وتجارب مستخدمين حول الخدمتين\","` | — |
| [SRC-F725E90B2A-L003657](../../tests/test_web_agent.py#L3657) | 3657 | `"            \"platform\": \"reddit\","` | — |
| [SRC-F725E90B2A-L003658](../../tests/test_web_agent.py#L3658) | 3658 | `"            \"providers\": [\"reddit\"],"` | — |
| [SRC-F725E90B2A-L003659](../../tests/test_web_agent.py#L3659) | 3659 | `"        },"` | — |
| [SRC-F725E90B2A-L003660](../../tests/test_web_agent.py#L3660) | 3660 | `"    ]"` | — |
| [SRC-F725E90B2A-L003661](../../tests/test_web_agent.py#L3661) | 3661 | `"    repair_candidate = {"` | — |
| [SRC-F725E90B2A-L003662](../../tests/test_web_agent.py#L3662) | 3662 | `"        **sample_source(2),"` | — |
| [SRC-F725E90B2A-L003663](../../tests/test_web_agent.py#L3663) | 3663 | `"        \"url\": \"https://example.com/unrelated-repair\","` | — |
| [SRC-F725E90B2A-L003664](../../tests/test_web_agent.py#L3664) | 3664 | `"        \"domain\": \"example.com\","` | — |
| [SRC-F725E90B2A-L003665](../../tests/test_web_agent.py#L3665) | 3665 | `"        \"title\": \"معلومات عن الخدمة\","` | — |
| [SRC-F725E90B2A-L003666](../../tests/test_web_agent.py#L3666) | 3666 | `"        \"snippet\": \"معلومات عامة عن الخدمة\","` | — |
| [SRC-F725E90B2A-L003667](../../tests/test_web_agent.py#L3667) | 3667 | `"        \"page_text\": \"معلومات عامة عن الخدمة\","` | — |
| [SRC-F725E90B2A-L003668](../../tests/test_web_agent.py#L3668) | 3668 | `"        \"providers\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L003669](../../tests/test_web_agent.py#L3669) | 3669 | `"    }"` | — |
| [SRC-F725E90B2A-L003670](../../tests/test_web_agent.py#L3670) | 3670 | `"    collect_calls = []"` | — |
| [SRC-F725E90B2A-L003671](../../tests/test_web_agent.py#L3671) | 3671 | `""` | — |
| [SRC-F725E90B2A-L003672](../../tests/test_web_agent.py#L3672) | 3672 | `"    def plan(_question, _history):"` | — |
| [SRC-F725E90B2A-L003673](../../tests/test_web_agent.py#L3673) | 3673 | `"        return {"` | — |
| [SRC-F725E90B2A-L003674](../../tests/test_web_agent.py#L3674) | 3674 | `"            \"queries\": [_question],"` | — |
| [SRC-F725E90B2A-L003675](../../tests/test_web_agent.py#L3675) | 3675 | `"            \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L003676](../../tests/test_web_agent.py#L3676) | 3676 | `"            \"social_focus\": True,"` | — |
| [SRC-F725E90B2A-L003677](../../tests/test_web_agent.py#L3677) | 3677 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003678](../../tests/test_web_agent.py#L3678) | 3678 | `"            \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L003679](../../tests/test_web_agent.py#L3679) | 3679 | `"            \"platforms\": [\"reddit\"],"` | — |
| [SRC-F725E90B2A-L003680](../../tests/test_web_agent.py#L3680) | 3680 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003681](../../tests/test_web_agent.py#L3681) | 3681 | `"        }"` | — |
| [SRC-F725E90B2A-L003682](../../tests/test_web_agent.py#L3682) | 3682 | `""` | — |
| [SRC-F725E90B2A-L003683](../../tests/test_web_agent.py#L3683) | 3683 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L003684](../../tests/test_web_agent.py#L3684) | 3684 | `"        collect_calls.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L003685](../../tests/test_web_agent.py#L3685) | 3685 | `"        if len(collect_calls) == 1:"` | — |
| [SRC-F725E90B2A-L003686](../../tests/test_web_agent.py#L3686) | 3686 | `"            sources = initial_sources"` | — |
| [SRC-F725E90B2A-L003687](../../tests/test_web_agent.py#L3687) | 3687 | `"        else:"` | — |
| [SRC-F725E90B2A-L003688](../../tests/test_web_agent.py#L3688) | 3688 | `"            sources = [repair_candidate]"` | — |
| [SRC-F725E90B2A-L003689](../../tests/test_web_agent.py#L3689) | 3689 | `"        return sources, [], {"` | — |
| [SRC-F725E90B2A-L003690](../../tests/test_web_agent.py#L3690) | 3690 | `"            \"queries_planned\": len(research_plan.get(\"queries\", [])),"` | — |
| [SRC-F725E90B2A-L003691](../../tests/test_web_agent.py#L3691) | 3691 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L003692](../../tests/test_web_agent.py#L3692) | 3692 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L003693](../../tests/test_web_agent.py#L3693) | 3693 | `"            \"unique_sources\": len(sources),"` | — |
| [SRC-F725E90B2A-L003694](../../tests/test_web_agent.py#L3694) | 3694 | `"            \"pages_fetched\": len(sources),"` | — |
| [SRC-F725E90B2A-L003695](../../tests/test_web_agent.py#L3695) | 3695 | `"            \"providers_used\": [\"reddit\"] if len(collect_calls) == 1 else [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L003696](../../tests/test_web_agent.py#L3696) | 3696 | `"            \"provider_counts\": {},"` | — |
| [SRC-F725E90B2A-L003697](../../tests/test_web_agent.py#L3697) | 3697 | `"            \"platform_counts\": {},"` | — |
| [SRC-F725E90B2A-L003698](../../tests/test_web_agent.py#L3698) | 3698 | `"            \"social_direct_results\": len(sources) if len(collect_calls) == 1 else 0,"` | — |
| [SRC-F725E90B2A-L003699](../../tests/test_web_agent.py#L3699) | 3699 | `"            \"depth\": research_plan.get(\"depth\", \"deep\"),"` | — |
| [SRC-F725E90B2A-L003700](../../tests/test_web_agent.py#L3700) | 3700 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003701](../../tests/test_web_agent.py#L3701) | 3701 | `"        }"` | — |
| [SRC-F725E90B2A-L003702](../../tests/test_web_agent.py#L3702) | 3702 | `""` | — |
| [SRC-F725E90B2A-L003703](../../tests/test_web_agent.py#L3703) | 3703 | `"    monkeypatch.setattr(agent, \"_plan_search\", plan)"` | — |
| [SRC-F725E90B2A-L003704](../../tests/test_web_agent.py#L3704) | 3704 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L003705](../../tests/test_web_agent.py#L3705) | 3705 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda _query, _source: True)"` | — |
| [SRC-F725E90B2A-L003706](../../tests/test_web_agent.py#L3706) | 3706 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003707](../../tests/test_web_agent.py#L3707) | 3707 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003708](../../tests/test_web_agent.py#L3708) | 3708 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L003709](../../tests/test_web_agent.py#L3709) | 3709 | `"        lambda *args, **kwargs: ("` | — |
| [SRC-F725E90B2A-L003710](../../tests/test_web_agent.py#L3710) | 3710 | `"            \"السعر مناسب [المصدر 1]. الخصوصية جيدة [المصدر 2]. \""` | — |
| [SRC-F725E90B2A-L003711](../../tests/test_web_agent.py#L3711) | 3711 | `"            \"الاعتمادية مناسبة [المصدر 1].\""` | — |
| [SRC-F725E90B2A-L003712](../../tests/test_web_agent.py#L3712) | 3712 | `"        ),"` | — |
| [SRC-F725E90B2A-L003713](../../tests/test_web_agent.py#L3713) | 3713 | `"    )"` | — |
| [SRC-F725E90B2A-L003714](../../tests/test_web_agent.py#L3714) | 3714 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003715](../../tests/test_web_agent.py#L3715) | 3715 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003716](../../tests/test_web_agent.py#L3716) | 3716 | `"        \"_review_answer\","` | — |
| [SRC-F725E90B2A-L003717](../../tests/test_web_agent.py#L3717) | 3717 | `"        lambda _question, answer, _sources: answer,"` | — |
| [SRC-F725E90B2A-L003718](../../tests/test_web_agent.py#L3718) | 3718 | `"    )"` | — |
| [SRC-F725E90B2A-L003719](../../tests/test_web_agent.py#L3719) | 3719 | `""` | — |
| [SRC-F725E90B2A-L003720](../../tests/test_web_agent.py#L3720) | 3720 | `"    result = agent.answer(question, mode=\"social\")"` | — |
| [SRC-F725E90B2A-L003721](../../tests/test_web_agent.py#L3721) | 3721 | `"    report = result[\"search_report\"]"` | — |
| [SRC-F725E90B2A-L003722](../../tests/test_web_agent.py#L3722) | 3722 | `"    repair_guardrails = report[\"source_guardrails\"][\"criterion_gap_repair\"]"` | — |
| [SRC-F725E90B2A-L003723](../../tests/test_web_agent.py#L3723) | 3723 | `""` | — |
| [SRC-F725E90B2A-L003724](../../tests/test_web_agent.py#L3724) | 3724 | `"    assert len(collect_calls) >= 2"` | — |
| [SRC-F725E90B2A-L003725](../../tests/test_web_agent.py#L3725) | 3725 | `"    assert repair_guardrails[\"rejected_sources\"] >= 1"` | — |
| [SRC-F725E90B2A-L003726](../../tests/test_web_agent.py#L3726) | 3726 | `"    assert repair_guardrails[\"rejection_counts\"][\"not_a_social_platform_source\"] >= 1"` | — |
| [SRC-F725E90B2A-L003727](../../tests/test_web_agent.py#L3727) | 3727 | `"    assert all(\"reddit.com\" in source[\"url\"] for source in result[\"sources\"])"` | — |
| [SRC-F725E90B2A-L003728](../../tests/test_web_agent.py#L3728) | 3728 | `"    assert \"https://example.com/unrelated-repair\" not in {"` | — |
| [SRC-F725E90B2A-L003729](../../tests/test_web_agent.py#L3729) | 3729 | `"        source[\"url\"] for source in result[\"sources\"]"` | — |
| [SRC-F725E90B2A-L003730](../../tests/test_web_agent.py#L3730) | 3730 | `"    }"` | — |
| [SRC-F725E90B2A-L003731](../../tests/test_web_agent.py#L3731) | 3731 | `""` | — |
| [SRC-F725E90B2A-L003732](../../tests/test_web_agent.py#L3732) | 3732 | `"def test_local_answer_exposes_task_spec_without_claiming_search(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003733](../../tests/test_web_agent.py#L3733) | 3733 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003734](../../tests/test_web_agent.py#L3734) | 3734 | `"    result = agent.answer(\"أهلا\")"` | — |
| [SRC-F725E90B2A-L003735](../../tests/test_web_agent.py#L3735) | 3735 | `""` | — |
| [SRC-F725E90B2A-L003736](../../tests/test_web_agent.py#L3736) | 3736 | `"    task_understanding = result[\"task_understanding\"]"` | — |
| [SRC-F725E90B2A-L003737](../../tests/test_web_agent.py#L3737) | 3737 | `"    assert task_understanding[\"task_spec\"][\"schema\"] == \"omarai.task_spec.v1\""` | — |
| [SRC-F725E90B2A-L003738](../../tests/test_web_agent.py#L3738) | 3738 | `"    assert task_understanding[\"tool_execution\"][\"search_outcome\"] == \"not_assessed\""` | — |
| [SRC-F725E90B2A-L003739](../../tests/test_web_agent.py#L3739) | 3739 | `"    assert task_understanding[\"tool_execution\"][\"required_tools\"] == []"` | — |
| [SRC-F725E90B2A-L003740](../../tests/test_web_agent.py#L3740) | 3740 | `"    assert all("` | — |
| [SRC-F725E90B2A-L003741](../../tests/test_web_agent.py#L3741) | 3741 | `"        row[\"status\"] == \"not_required\""` | — |
| [SRC-F725E90B2A-L003742](../../tests/test_web_agent.py#L3742) | 3742 | `"        for row in task_understanding[\"tool_execution\"][\"tool_status_matrix\"]"` | — |
| [SRC-F725E90B2A-L003743](../../tests/test_web_agent.py#L3743) | 3743 | `"    )"` | — |
| [SRC-F725E90B2A-L003744](../../tests/test_web_agent.py#L3744) | 3744 | `"    assert task_understanding[\"actual_queries\"] == []"` | — |
| [SRC-F725E90B2A-L003745](../../tests/test_web_agent.py#L3745) | 3745 | `"    assert task_understanding[\"query_strategy_matrix\"] == []"` | — |
| [SRC-F725E90B2A-L003746](../../tests/test_web_agent.py#L3746) | 3746 | `"    assert task_understanding[\"search_was_attempted\"] is False"` | — |
| [SRC-F725E90B2A-L003747](../../tests/test_web_agent.py#L3747) | 3747 | `""` | — |
| [SRC-F725E90B2A-L003748](../../tests/test_web_agent.py#L3748) | 3748 | `"def test_official_site_without_target_clarifies_before_planning_or_search(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003749](../../tests/test_web_agent.py#L3749) | 3749 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003750](../../tests/test_web_agent.py#L3750) | 3750 | `""` | — |
| [SRC-F725E90B2A-L003751](../../tests/test_web_agent.py#L3751) | 3751 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003752](../../tests/test_web_agent.py#L3752) | 3752 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003753](../../tests/test_web_agent.py#L3753) | 3753 | `"        \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003754](../../tests/test_web_agent.py#L3754) | 3754 | `"        lambda *args, **kwargs: pytest.fail(\"Missing official-site target must be clarified before planning\"),"` | — |
| [SRC-F725E90B2A-L003755](../../tests/test_web_agent.py#L3755) | 3755 | `"    )"` | — |
| [SRC-F725E90B2A-L003756](../../tests/test_web_agent.py#L3756) | 3756 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003757](../../tests/test_web_agent.py#L3757) | 3757 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003758](../../tests/test_web_agent.py#L3758) | 3758 | `"        \"_collect_research\","` | — |
| [SRC-F725E90B2A-L003759](../../tests/test_web_agent.py#L3759) | 3759 | `"        lambda *args, **kwargs: pytest.fail(\"Missing official-site target must not invoke search\"),"` | — |
| [SRC-F725E90B2A-L003760](../../tests/test_web_agent.py#L3760) | 3760 | `"    )"` | — |
| [SRC-F725E90B2A-L003761](../../tests/test_web_agent.py#L3761) | 3761 | `""` | — |
| [SRC-F725E90B2A-L003762](../../tests/test_web_agent.py#L3762) | 3762 | `"    result = agent.answer(\"هات الموقع الرسمي\")"` | — |
| [SRC-F725E90B2A-L003763](../../tests/test_web_agent.py#L3763) | 3763 | `""` | — |
| [SRC-F725E90B2A-L003764](../../tests/test_web_agent.py#L3764) | 3764 | `"    assert result[\"intent_route\"] == \"CLARIFY\""` | — |
| [SRC-F725E90B2A-L003765](../../tests/test_web_agent.py#L3765) | 3765 | `"    assert result[\"kind\"] == \"clarification_needed\""` | — |
| [SRC-F725E90B2A-L003766](../../tests/test_web_agent.py#L3766) | 3766 | `"    assert \"اسم الجهة أو الشركة\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L003767](../../tests/test_web_agent.py#L3767) | 3767 | `"    assert result[\"search_attempted\"] is False"` | — |
| [SRC-F725E90B2A-L003768](../../tests/test_web_agent.py#L3768) | 3768 | `"    assert \"official_destination_target_entity\" in result[\"task_understanding\"][\"task_spec\"][\"missing_required_inputs\"]"` | — |
| [SRC-F725E90B2A-L003769](../../tests/test_web_agent.py#L3769) | 3769 | `""` | — |
| [SRC-F725E90B2A-L003770](../../tests/test_web_agent.py#L3770) | 3770 | `"def test_summary_without_source_clarifies_before_search(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003771](../../tests/test_web_agent.py#L3771) | 3771 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003772](../../tests/test_web_agent.py#L3772) | 3772 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003773](../../tests/test_web_agent.py#L3773) | 3773 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003774](../../tests/test_web_agent.py#L3774) | 3774 | `"        \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003775](../../tests/test_web_agent.py#L3775) | 3775 | `"        lambda *args, **kwargs: pytest.fail(\"Missing summary source must be clarified before planning\"),"` | — |
| [SRC-F725E90B2A-L003776](../../tests/test_web_agent.py#L3776) | 3776 | `"    )"` | — |
| [SRC-F725E90B2A-L003777](../../tests/test_web_agent.py#L3777) | 3777 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003778](../../tests/test_web_agent.py#L3778) | 3778 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003779](../../tests/test_web_agent.py#L3779) | 3779 | `"        \"_collect_research\","` | — |
| [SRC-F725E90B2A-L003780](../../tests/test_web_agent.py#L3780) | 3780 | `"        lambda *args, **kwargs: pytest.fail(\"Missing summary source must not invoke search\"),"` | — |
| [SRC-F725E90B2A-L003781](../../tests/test_web_agent.py#L3781) | 3781 | `"    )"` | — |
| [SRC-F725E90B2A-L003782](../../tests/test_web_agent.py#L3782) | 3782 | `""` | — |
| [SRC-F725E90B2A-L003783](../../tests/test_web_agent.py#L3783) | 3783 | `"    result = agent.answer(\"لخص\")"` | — |
| [SRC-F725E90B2A-L003784](../../tests/test_web_agent.py#L3784) | 3784 | `""` | — |
| [SRC-F725E90B2A-L003785](../../tests/test_web_agent.py#L3785) | 3785 | `"    assert result[\"intent_route\"] == \"CLARIFY\""` | — |
| [SRC-F725E90B2A-L003786](../../tests/test_web_agent.py#L3786) | 3786 | `"    assert \"أرسل النص\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L003787](../../tests/test_web_agent.py#L3787) | 3787 | `"    assert result[\"search_attempted\"] is False"` | — |
| [SRC-F725E90B2A-L003788](../../tests/test_web_agent.py#L3788) | 3788 | `"    assert \"summary_source_url_or_pasted_text\" in result[\"task_understanding\"][\"task_spec\"][\"missing_required_inputs\"]"` | — |
| [SRC-F725E90B2A-L003789](../../tests/test_web_agent.py#L3789) | 3789 | `""` | — |
| [SRC-F725E90B2A-L003790](../../tests/test_web_agent.py#L3790) | 3790 | `"def test_task_spec_controls_generation_context_without_becoming_evidence(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003791](../../tests/test_web_agent.py#L3791) | 3791 | `"    from agents.task_understanding import build_query_strategy_matrix, build_task_spec"` | — |
| [SRC-F725E90B2A-L003792](../../tests/test_web_agent.py#L3792) | 3792 | `""` | — |
| [SRC-F725E90B2A-L003793](../../tests/test_web_agent.py#L3793) | 3793 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003794](../../tests/test_web_agent.py#L3794) | 3794 | `"    captured = {}"` | — |
| [SRC-F725E90B2A-L003795](../../tests/test_web_agent.py#L3795) | 3795 | `""` | — |
| [SRC-F725E90B2A-L003796](../../tests/test_web_agent.py#L3796) | 3796 | `"    question = ("` | — |
| [SRC-F725E90B2A-L003797](../../tests/test_web_agent.py#L3797) | 3797 | `"        \"قارن السيارات الكهربائية في مصر من حيث السعر والضمان، \""` | — |
| [SRC-F725E90B2A-L003798](../../tests/test_web_agent.py#L3798) | 3798 | `"        \"اشرح ببساطة مع أمثلة وروابط مباشرة\""` | — |
| [SRC-F725E90B2A-L003799](../../tests/test_web_agent.py#L3799) | 3799 | `"    )"` | — |
| [SRC-F725E90B2A-L003800](../../tests/test_web_agent.py#L3800) | 3800 | `"    task_spec = build_task_spec("` | — |
| [SRC-F725E90B2A-L003801](../../tests/test_web_agent.py#L3801) | 3801 | `"        question,"` | — |
| [SRC-F725E90B2A-L003802](../../tests/test_web_agent.py#L3802) | 3802 | `"        mode=\"deep\","` | — |
| [SRC-F725E90B2A-L003803](../../tests/test_web_agent.py#L3803) | 3803 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-F725E90B2A-L003804](../../tests/test_web_agent.py#L3804) | 3804 | `"    )"` | — |
| [SRC-F725E90B2A-L003805](../../tests/test_web_agent.py#L3805) | 3805 | `"    initial_queries = [compact_search_query(question)]"` | — |
| [SRC-F725E90B2A-L003806](../../tests/test_web_agent.py#L3806) | 3806 | `"    matrix = build_query_strategy_matrix("` | — |
| [SRC-F725E90B2A-L003807](../../tests/test_web_agent.py#L3807) | 3807 | `"        question,"` | — |
| [SRC-F725E90B2A-L003808](../../tests/test_web_agent.py#L3808) | 3808 | `"        task_spec,"` | — |
| [SRC-F725E90B2A-L003809](../../tests/test_web_agent.py#L3809) | 3809 | `"        initial_queries,"` | — |
| [SRC-F725E90B2A-L003810](../../tests/test_web_agent.py#L3810) | 3810 | `"        limit=4,"` | — |
| [SRC-F725E90B2A-L003811](../../tests/test_web_agent.py#L3811) | 3811 | `"        compact_fn=compact_search_query,"` | — |
| [SRC-F725E90B2A-L003812](../../tests/test_web_agent.py#L3812) | 3812 | `"    )"` | — |
| [SRC-F725E90B2A-L003813](../../tests/test_web_agent.py#L3813) | 3813 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L003814](../../tests/test_web_agent.py#L3814) | 3814 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L003815](../../tests/test_web_agent.py#L3815) | 3815 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003816](../../tests/test_web_agent.py#L3816) | 3816 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003817](../../tests/test_web_agent.py#L3817) | 3817 | `"        \"queries\": [row[\"query\"] for row in matrix],"` | — |
| [SRC-F725E90B2A-L003818](../../tests/test_web_agent.py#L3818) | 3818 | `"        \"dialogue_context\": {},"` | — |
| [SRC-F725E90B2A-L003819](../../tests/test_web_agent.py#L3819) | 3819 | `"        \"intent_route\": \"WEB_DEEP\","` | — |
| [SRC-F725E90B2A-L003820](../../tests/test_web_agent.py#L3820) | 3820 | `"        \"task_spec\": task_spec,"` | — |
| [SRC-F725E90B2A-L003821](../../tests/test_web_agent.py#L3821) | 3821 | `"        \"query_strategy_matrix\": matrix,"` | — |
| [SRC-F725E90B2A-L003822](../../tests/test_web_agent.py#L3822) | 3822 | `"    }"` | — |
| [SRC-F725E90B2A-L003823](../../tests/test_web_agent.py#L3823) | 3823 | `""` | — |
| [SRC-F725E90B2A-L003824](../../tests/test_web_agent.py#L3824) | 3824 | `"    def fake_completion(messages, **kwargs):"` | — |
| [SRC-F725E90B2A-L003825](../../tests/test_web_agent.py#L3825) | 3825 | `"        captured[\"messages\"] = messages"` | — |
| [SRC-F725E90B2A-L003826](../../tests/test_web_agent.py#L3826) | 3826 | `"        captured[\"kwargs\"] = kwargs"` | — |
| [SRC-F725E90B2A-L003827](../../tests/test_web_agent.py#L3827) | 3827 | `"        return \"إجابة اختبارية مرتبطة بالأدلة.\""` | — |
| [SRC-F725E90B2A-L003828](../../tests/test_web_agent.py#L3828) | 3828 | `""` | — |
| [SRC-F725E90B2A-L003829](../../tests/test_web_agent.py#L3829) | 3829 | `"    monkeypatch.setattr(agent, \"_request_completion\", fake_completion)"` | — |
| [SRC-F725E90B2A-L003830](../../tests/test_web_agent.py#L3830) | 3830 | `""` | — |
| [SRC-F725E90B2A-L003831](../../tests/test_web_agent.py#L3831) | 3831 | `"    answer = agent._generate("` | — |
| [SRC-F725E90B2A-L003832](../../tests/test_web_agent.py#L3832) | 3832 | `"        question,"` | — |
| [SRC-F725E90B2A-L003833](../../tests/test_web_agent.py#L3833) | 3833 | `"        [],"` | — |
| [SRC-F725E90B2A-L003834](../../tests/test_web_agent.py#L3834) | 3834 | `"        [sample_source(0)],"` | — |
| [SRC-F725E90B2A-L003835](../../tests/test_web_agent.py#L3835) | 3835 | `"        None,"` | — |
| [SRC-F725E90B2A-L003836](../../tests/test_web_agent.py#L3836) | 3836 | `"        research_plan=plan,"` | — |
| [SRC-F725E90B2A-L003837](../../tests/test_web_agent.py#L3837) | 3837 | `"        search_report={"` | — |
| [SRC-F725E90B2A-L003838](../../tests/test_web_agent.py#L3838) | 3838 | `"            \"queries_planned\": len(plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L003839](../../tests/test_web_agent.py#L3839) | 3839 | `"            \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L003840](../../tests/test_web_agent.py#L3840) | 3840 | `"            \"pages_fetched\": 1,"` | — |
| [SRC-F725E90B2A-L003841](../../tests/test_web_agent.py#L3841) | 3841 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L003842](../../tests/test_web_agent.py#L3842) | 3842 | `"        },"` | — |
| [SRC-F725E90B2A-L003843](../../tests/test_web_agent.py#L3843) | 3843 | `"    )"` | — |
| [SRC-F725E90B2A-L003844](../../tests/test_web_agent.py#L3844) | 3844 | `""` | — |
| [SRC-F725E90B2A-L003845](../../tests/test_web_agent.py#L3845) | 3845 | `"    prompt = \"\\n\".join("` | — |
| [SRC-F725E90B2A-L003846](../../tests/test_web_agent.py#L3846) | 3846 | `"        message.get(\"content\", \"\")"` | — |
| [SRC-F725E90B2A-L003847](../../tests/test_web_agent.py#L3847) | 3847 | `"        for message in captured[\"messages\"]"` | — |
| [SRC-F725E90B2A-L003848](../../tests/test_web_agent.py#L3848) | 3848 | `"        if isinstance(message, dict)"` | — |
| [SRC-F725E90B2A-L003849](../../tests/test_web_agent.py#L3849) | 3849 | `"    )"` | — |
| [SRC-F725E90B2A-L003850](../../tests/test_web_agent.py#L3850) | 3850 | `"    assert answer == \"إجابة اختبارية مرتبطة بالأدلة.\""` | — |
| [SRC-F725E90B2A-L003851](../../tests/test_web_agent.py#L3851) | 3851 | `"    assert \"task_planning_context\" in prompt"` | — |
| [SRC-F725E90B2A-L003852](../../tests/test_web_agent.py#L3852) | 3852 | `"    assert \"explicit_aspects\" in prompt"` | — |
| [SRC-F725E90B2A-L003853](../../tests/test_web_agent.py#L3853) | 3853 | `"    assert \"output_preferences\" in prompt"` | — |
| [SRC-F725E90B2A-L003854](../../tests/test_web_agent.py#L3854) | 3854 | `"    assert \"beginner_friendly_requested\" in prompt"` | — |
| [SRC-F725E90B2A-L003855](../../tests/test_web_agent.py#L3855) | 3855 | `"    assert \"reasoning_guidance\" in prompt"` | — |
| [SRC-F725E90B2A-L003856](../../tests/test_web_agent.py#L3856) | 3856 | `"    assert \"decision_matrix\" in prompt"` | — |
| [SRC-F725E90B2A-L003857](../../tests/test_web_agent.py#L3857) | 3857 | `"    assert \"قسّم المقارنة إلى كل معيار صريح\" in prompt"` | — |
| [SRC-F725E90B2A-L003858](../../tests/test_web_agent.py#L3858) | 3858 | `"    assert \"وحّد العملة والوحدات\" in prompt"` | — |
| [SRC-F725E90B2A-L003859](../../tests/test_web_agent.py#L3859) | 3859 | `"    assert \"query_strategy_matrix\" in prompt"` | — |
| [SRC-F725E90B2A-L003860](../../tests/test_web_agent.py#L3860) | 3860 | `"    assert \"الأولوية لكلام المستخدم الحالي\" in prompt"` | — |
| [SRC-F725E90B2A-L003861](../../tests/test_web_agent.py#L3861) | 3861 | `"    assert \"الاستعلامات المخططة فقط\" in prompt"` | — |
| [SRC-F725E90B2A-L003862](../../tests/test_web_agent.py#L3862) | 3862 | `""` | — |
| [SRC-F725E90B2A-L003863](../../tests/test_web_agent.py#L3863) | 3863 | `"def test_bilingual_relevance_handles_arabic_attached_clitics_without_lowering_floor():"` | — |
| [SRC-F725E90B2A-L003864](../../tests/test_web_agent.py#L3864) | 3864 | `"    query = \"أهم استخدامات الذكاء الاصطناعي للشركات الصغيرة؟\""` | — |
| [SRC-F725E90B2A-L003865](../../tests/test_web_agent.py#L3865) | 3865 | `"    evidence = \"AI use cases for small businesses\""` | — |
| [SRC-F725E90B2A-L003866](../../tests/test_web_agent.py#L3866) | 3866 | `"    assert _minimum_relevance_ratio(query) == 0.20"` | — |
| [SRC-F725E90B2A-L003867](../../tests/test_web_agent.py#L3867) | 3867 | `"    assert _relevance_ratio(query, evidence) >= 0.80"` | — |
| [SRC-F725E90B2A-L003868](../../tests/test_web_agent.py#L3868) | 3868 | `""` | — |
| [SRC-F725E90B2A-L003869](../../tests/test_web_agent.py#L3869) | 3869 | `"def test_search_evidence_matching_keeps_distinct_concepts_as_the_ratio_denominator():"` | — |
| [SRC-F725E90B2A-L003870](../../tests/test_web_agent.py#L3870) | 3870 | `"    query = \"استخدامات الذكاء الاصطناعي للشركات الصغيرة\""` | — |
| [SRC-F725E90B2A-L003871](../../tests/test_web_agent.py#L3871) | 3871 | `"    on_topic = \"AI use cases for small businesses\""` | — |
| [SRC-F725E90B2A-L003872](../../tests/test_web_agent.py#L3872) | 3872 | `"    weak = \"AI tools for personal photo editing\""` | — |
| [SRC-F725E90B2A-L003873](../../tests/test_web_agent.py#L3873) | 3873 | `"    assert _relevance_ratio(query, on_topic) > _relevance_ratio(query, weak)"` | — |
| [SRC-F725E90B2A-L003874](../../tests/test_web_agent.py#L3874) | 3874 | `"    assert _relevance_ratio(query, weak) < _minimum_relevance_ratio(query)"` | — |
| [SRC-F725E90B2A-L003875](../../tests/test_web_agent.py#L3875) | 3875 | `""` | — |
| [SRC-F725E90B2A-L003876](../../tests/test_web_agent.py#L3876) | 3876 | `"def test_bilingual_relevance_matches_english_queries_to_arabic_source_text():"` | — |
| [SRC-F725E90B2A-L003877](../../tests/test_web_agent.py#L3877) | 3877 | `"    query = \"AI use cases for small businesses in Egypt\""` | — |
| [SRC-F725E90B2A-L003878](../../tests/test_web_agent.py#L3878) | 3878 | `"    evidence = \"استخدامات الذكاء الاصطناعي للشركات الصغيرة في مصر\""` | — |
| [SRC-F725E90B2A-L003879](../../tests/test_web_agent.py#L3879) | 3879 | `"    assert _relevance_ratio(query, evidence) >= 0.80"` | — |
| [SRC-F725E90B2A-L003880](../../tests/test_web_agent.py#L3880) | 3880 | `""` | — |
| [SRC-F725E90B2A-L003881](../../tests/test_web_agent.py#L3881) | 3881 | `""` | — |
| [SRC-F725E90B2A-L003882](../../tests/test_web_agent.py#L3882) | 3882 | `"def test_completion_diagnostics_failure_does_not_break_answer(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003883](../../tests/test_web_agent.py#L3883) | 3883 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003884](../../tests/test_web_agent.py#L3884) | 3884 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L003885](../../tests/test_web_agent.py#L3885) | 3885 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003886](../../tests/test_web_agent.py#L3886) | 3886 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003887](../../tests/test_web_agent.py#L3887) | 3887 | `"        \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003888](../../tests/test_web_agent.py#L3888) | 3888 | `"        lambda question, history: {"` | — |
| [SRC-F725E90B2A-L003889](../../tests/test_web_agent.py#L3889) | 3889 | `"            \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L003890](../../tests/test_web_agent.py#L3890) | 3890 | `"            \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003891](../../tests/test_web_agent.py#L3891) | 3891 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003892](../../tests/test_web_agent.py#L3892) | 3892 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003893](../../tests/test_web_agent.py#L3893) | 3893 | `"            \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003894](../../tests/test_web_agent.py#L3894) | 3894 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003895](../../tests/test_web_agent.py#L3895) | 3895 | `"            \"coverage_targets\": [],"` | — |
| [SRC-F725E90B2A-L003896](../../tests/test_web_agent.py#L3896) | 3896 | `"        },"` | — |
| [SRC-F725E90B2A-L003897](../../tests/test_web_agent.py#L3897) | 3897 | `"    )"` | — |
| [SRC-F725E90B2A-L003898](../../tests/test_web_agent.py#L3898) | 3898 | `"    monkeypatch.setattr(agent, \"_collect_research\", lambda plan: ("` | — |
| [SRC-F725E90B2A-L003899](../../tests/test_web_agent.py#L3899) | 3899 | `"        [sample_source(0), sample_source(1)], [], {"` | — |
| [SRC-F725E90B2A-L003900](../../tests/test_web_agent.py#L3900) | 3900 | `"            \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L003901](../../tests/test_web_agent.py#L3901) | 3901 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L003902](../../tests/test_web_agent.py#L3902) | 3902 | `"            \"query_results\": [{\"query\": plan[\"queries\"][0], \"results\": 2}],"` | — |
| [SRC-F725E90B2A-L003903](../../tests/test_web_agent.py#L3903) | 3903 | `"            \"unique_sources\": 2,"` | — |
| [SRC-F725E90B2A-L003904](../../tests/test_web_agent.py#L3904) | 3904 | `"            \"pages_fetched\": 2,"` | — |
| [SRC-F725E90B2A-L003905](../../tests/test_web_agent.py#L3905) | 3905 | `"            \"providers_used\": [\"test\"],"` | — |
| [SRC-F725E90B2A-L003906](../../tests/test_web_agent.py#L3906) | 3906 | `"            \"provider_diagnostics\": [],"` | — |
| [SRC-F725E90B2A-L003907](../../tests/test_web_agent.py#L3907) | 3907 | `"        }"` | — |
| [SRC-F725E90B2A-L003908](../../tests/test_web_agent.py#L3908) | 3908 | `"    ))"` | — |
| [SRC-F725E90B2A-L003909](../../tests/test_web_agent.py#L3909) | 3909 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L003910](../../tests/test_web_agent.py#L3910) | 3910 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L003911](../../tests/test_web_agent.py#L3911) | 3911 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"إجابة اختبارية [المصدر 1].\")"` | — |
| [SRC-F725E90B2A-L003912](../../tests/test_web_agent.py#L3912) | 3912 | `""` | — |
| [SRC-F725E90B2A-L003913](../../tests/test_web_agent.py#L3913) | 3913 | `"    def fail_diagnostics(_result):"` | — |
| [SRC-F725E90B2A-L003914](../../tests/test_web_agent.py#L3914) | 3914 | `"        raise RuntimeError(\"diagnostics are optional\")"` | — |
| [SRC-F725E90B2A-L003915](../../tests/test_web_agent.py#L3915) | 3915 | `""` | — |
| [SRC-F725E90B2A-L003916](../../tests/test_web_agent.py#L3916) | 3916 | `"    monkeypatch.setattr(\"agents.web_agent.build_research_completion\", fail_diagnostics)"` | — |
| [SRC-F725E90B2A-L003917](../../tests/test_web_agent.py#L3917) | 3917 | `"    result = agent.answer(\"قارن هذه التقنية\")"` | — |
| [SRC-F725E90B2A-L003918](../../tests/test_web_agent.py#L3918) | 3918 | `"    assert result[\"answer\"] == \"إجابة اختبارية [المصدر 1].\""` | — |
| [SRC-F725E90B2A-L003919](../../tests/test_web_agent.py#L3919) | 3919 | `"    assert result[\"research_completion\"][\"status\"] == \"diagnostics_not_computed\""` | — |
| [SRC-F725E90B2A-L003920](../../tests/test_web_agent.py#L3920) | 3920 | `"    assert any(\"لا يُعد ذلك دليلًا على اكتمال البحث\" in warning for warning in result[\"warnings\"])"` | — |
| [SRC-F725E90B2A-L003921](../../tests/test_web_agent.py#L3921) | 3921 | `""` | — |
| [SRC-F725E90B2A-L003922](../../tests/test_web_agent.py#L3922) | 3922 | `""` | — |
| [SRC-F725E90B2A-L003923](../../tests/test_web_agent.py#L3923) | 3923 | `""` | — |
| [SRC-F725E90B2A-L003924](../../tests/test_web_agent.py#L3924) | 3924 | `"def test_model_request_transport_disables_automatic_redirects(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003925](../../tests/test_web_agent.py#L3925) | 3925 | `"    from agents import web_agent"` | — |
| [SRC-F725E90B2A-L003926](../../tests/test_web_agent.py#L3926) | 3926 | `""` | — |
| [SRC-F725E90B2A-L003927](../../tests/test_web_agent.py#L3927) | 3927 | `"    observed = {}"` | — |
| [SRC-F725E90B2A-L003928](../../tests/test_web_agent.py#L3928) | 3928 | `"    sentinel = object()"` | — |
| [SRC-F725E90B2A-L003929](../../tests/test_web_agent.py#L3929) | 3929 | `""` | — |
| [SRC-F725E90B2A-L003930](../../tests/test_web_agent.py#L3930) | 3930 | `"    class FakeOpener:"` | — |
| [SRC-F725E90B2A-L003931](../../tests/test_web_agent.py#L3931) | 3931 | `"        def open(self, request, *, timeout):"` | — |
| [SRC-F725E90B2A-L003932](../../tests/test_web_agent.py#L3932) | 3932 | `"            observed[\"request\"] = request"` | — |
| [SRC-F725E90B2A-L003933](../../tests/test_web_agent.py#L3933) | 3933 | `"            observed[\"timeout\"] = timeout"` | — |
| [SRC-F725E90B2A-L003934](../../tests/test_web_agent.py#L3934) | 3934 | `"            return sentinel"` | — |
| [SRC-F725E90B2A-L003935](../../tests/test_web_agent.py#L3935) | 3935 | `""` | — |
| [SRC-F725E90B2A-L003936](../../tests/test_web_agent.py#L3936) | 3936 | `"    def fake_build_opener(*handlers):"` | — |
| [SRC-F725E90B2A-L003937](../../tests/test_web_agent.py#L3937) | 3937 | `"        observed[\"handlers\"] = handlers"` | — |
| [SRC-F725E90B2A-L003938](../../tests/test_web_agent.py#L3938) | 3938 | `"        return FakeOpener()"` | — |
| [SRC-F725E90B2A-L003939](../../tests/test_web_agent.py#L3939) | 3939 | `""` | — |
| [SRC-F725E90B2A-L003940](../../tests/test_web_agent.py#L3940) | 3940 | `"    monkeypatch.setattr(web_agent.urllib.request, \"build_opener\", fake_build_opener)"` | — |
| [SRC-F725E90B2A-L003941](../../tests/test_web_agent.py#L3941) | 3941 | `"    request = web_agent.urllib.request.Request("` | — |
| [SRC-F725E90B2A-L003942](../../tests/test_web_agent.py#L3942) | 3942 | `"        \"https://provider.example/v1/chat/completions\","` | — |
| [SRC-F725E90B2A-L003943](../../tests/test_web_agent.py#L3943) | 3943 | `"        data=b\"{}\","` | — |
| [SRC-F725E90B2A-L003944](../../tests/test_web_agent.py#L3944) | 3944 | `"        headers={\"Authorization\": \"Bearer test-only-token\"},"` | — |
| [SRC-F725E90B2A-L003945](../../tests/test_web_agent.py#L3945) | 3945 | `"        method=\"POST\","` | — |
| [SRC-F725E90B2A-L003946](../../tests/test_web_agent.py#L3946) | 3946 | `"    )"` | — |
| [SRC-F725E90B2A-L003947](../../tests/test_web_agent.py#L3947) | 3947 | `""` | — |
| [SRC-F725E90B2A-L003948](../../tests/test_web_agent.py#L3948) | 3948 | `"    assert web_agent._open_model_request(request, timeout=3.5) is sentinel"` | — |
| [SRC-F725E90B2A-L003949](../../tests/test_web_agent.py#L3949) | 3949 | `"    assert observed[\"request\"] is request"` | — |
| [SRC-F725E90B2A-L003950](../../tests/test_web_agent.py#L3950) | 3950 | `"    assert observed[\"timeout\"] == 3.5"` | — |
| [SRC-F725E90B2A-L003951](../../tests/test_web_agent.py#L3951) | 3951 | `"    assert observed[\"handlers\"] == (web_agent._NoRedirectHandler,)"` | — |
| [SRC-F725E90B2A-L003952](../../tests/test_web_agent.py#L3952) | 3952 | `""` | — |
| [SRC-F725E90B2A-L003953](../../tests/test_web_agent.py#L3953) | 3953 | `"    handler = web_agent._NoRedirectHandler()"` | — |
| [SRC-F725E90B2A-L003954](../../tests/test_web_agent.py#L3954) | 3954 | `"    redirected = handler.redirect_request("` | — |
| [SRC-F725E90B2A-L003955](../../tests/test_web_agent.py#L3955) | 3955 | `"        request,"` | — |
| [SRC-F725E90B2A-L003956](../../tests/test_web_agent.py#L3956) | 3956 | `"        None,"` | — |
| [SRC-F725E90B2A-L003957](../../tests/test_web_agent.py#L3957) | 3957 | `"        302,"` | — |
| [SRC-F725E90B2A-L003958](../../tests/test_web_agent.py#L3958) | 3958 | `"        \"Found\","` | — |
| [SRC-F725E90B2A-L003959](../../tests/test_web_agent.py#L3959) | 3959 | `"        {},"` | — |
| [SRC-F725E90B2A-L003960](../../tests/test_web_agent.py#L3960) | 3960 | `"        \"https://attacker.example/collect\","` | — |
| [SRC-F725E90B2A-L003961](../../tests/test_web_agent.py#L3961) | 3961 | `"    )"` | — |
| [SRC-F725E90B2A-L003962](../../tests/test_web_agent.py#L3962) | 3962 | `"    assert redirected is None"` | — |
| [SRC-F725E90B2A-L003963](../../tests/test_web_agent.py#L3963) | 3963 | `""` | — |
| [SRC-F725E90B2A-L003964](../../tests/test_web_agent.py#L3964) | 3964 | `""` | — |
| [SRC-F725E90B2A-L003965](../../tests/test_web_agent.py#L3965) | 3965 | `"def test_openrouter_web_search_does_not_match_spoofed_hostname(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003966](../../tests/test_web_agent.py#L3966) | 3966 | `"    monkeypatch.setenv(\"OMARAI_OPENROUTER_WEB_SEARCH\", \"1\")"` | — |
| [SRC-F725E90B2A-L003967](../../tests/test_web_agent.py#L3967) | 3967 | `"    monkeypatch.setenv("` | — |
| [SRC-F725E90B2A-L003968](../../tests/test_web_agent.py#L3968) | 3968 | `"        \"OMARAI_LLM_BASE_URL\","` | — |
| [SRC-F725E90B2A-L003969](../../tests/test_web_agent.py#L3969) | 3969 | `"        \"https://openrouter.ai.attacker.example/api/v1\","` | — |
| [SRC-F725E90B2A-L003970](../../tests/test_web_agent.py#L3970) | 3970 | `"    )"` | — |
| [SRC-F725E90B2A-L003971](../../tests/test_web_agent.py#L3971) | 3971 | `""` | — |
| [SRC-F725E90B2A-L003972](../../tests/test_web_agent.py#L3972) | 3972 | `"    assert WebAgent().openrouter_web_search_enabled is False"` | — |
| [SRC-F725E90B2A-L003973](../../tests/test_web_agent.py#L3973) | 3973 | `""` | — |
| [SRC-F725E90B2A-L003974](../../tests/test_web_agent.py#L3974) | 3974 | `""` | — |
| [SRC-F725E90B2A-L003975](../../tests/test_web_agent.py#L3975) | 3975 | `""` | — |
| [SRC-F725E90B2A-L003976](../../tests/test_web_agent.py#L3976) | 3976 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L003977](../../tests/test_web_agent.py#L3977) | 3977 | `"    \"address,family\","` | — |
| [SRC-F725E90B2A-L003978](../../tests/test_web_agent.py#L3978) | 3978 | `"    ["` | — |
| [SRC-F725E90B2A-L003979](../../tests/test_web_agent.py#L3979) | 3979 | `"        (\"127.0.0.1\", __import__(\"socket\").AF_INET),"` | — |
| [SRC-F725E90B2A-L003980](../../tests/test_web_agent.py#L3980) | 3980 | `"        (\"169.254.169.254\", __import__(\"socket\").AF_INET),"` | — |
| [SRC-F725E90B2A-L003981](../../tests/test_web_agent.py#L3981) | 3981 | `"        (\"::1\", __import__(\"socket\").AF_INET6),"` | — |
| [SRC-F725E90B2A-L003982](../../tests/test_web_agent.py#L3982) | 3982 | `"        (\"fe80::1\", __import__(\"socket\").AF_INET6),"` | — |
| [SRC-F725E90B2A-L003983](../../tests/test_web_agent.py#L3983) | 3983 | `"        (\"fd00::1\", __import__(\"socket\").AF_INET6),"` | — |
| [SRC-F725E90B2A-L003984](../../tests/test_web_agent.py#L3984) | 3984 | `"    ],"` | — |
| [SRC-F725E90B2A-L003985](../../tests/test_web_agent.py#L3985) | 3985 | `")"` | — |
| [SRC-F725E90B2A-L003986](../../tests/test_web_agent.py#L3986) | 3986 | `"def test_public_ip_literals_rejects_non_global_ipv4_and_ipv6_answers("` | — |
| [SRC-F725E90B2A-L003987](../../tests/test_web_agent.py#L3987) | 3987 | `"    monkeypatch, address, family"` | — |
| [SRC-F725E90B2A-L003988](../../tests/test_web_agent.py#L3988) | 3988 | `"):"` | — |
| [SRC-F725E90B2A-L003989](../../tests/test_web_agent.py#L3989) | 3989 | `"    import socket"` | — |
| [SRC-F725E90B2A-L003990](../../tests/test_web_agent.py#L3990) | 3990 | `""` | — |
| [SRC-F725E90B2A-L003991](../../tests/test_web_agent.py#L3991) | 3991 | `"    from agents import web_agent"` | — |
| [SRC-F725E90B2A-L003992](../../tests/test_web_agent.py#L3992) | 3992 | `""` | — |
| [SRC-F725E90B2A-L003993](../../tests/test_web_agent.py#L3993) | 3993 | `"    answers = ["` | — |
| [SRC-F725E90B2A-L003994](../../tests/test_web_agent.py#L3994) | 3994 | `"        (family, socket.SOCK_STREAM, socket.IPPROTO_TCP, \"\", (address, 80))"` | — |
| [SRC-F725E90B2A-L003995](../../tests/test_web_agent.py#L3995) | 3995 | `"    ]"` | — |
| [SRC-F725E90B2A-L003996](../../tests/test_web_agent.py#L3996) | 3996 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003997](../../tests/test_web_agent.py#L3997) | 3997 | `"        web_agent.socket,"` | — |
| [SRC-F725E90B2A-L003998](../../tests/test_web_agent.py#L3998) | 3998 | `"        \"getaddrinfo\","` | — |
| [SRC-F725E90B2A-L003999](../../tests/test_web_agent.py#L3999) | 3999 | `"        lambda host, port, type: answers,"` | — |
| [SRC-F725E90B2A-L004000](../../tests/test_web_agent.py#L4000) | 4000 | `"    )"` | — |
| [SRC-F725E90B2A-L004001](../../tests/test_web_agent.py#L4001) | 4001 | `""` | — |
| [SRC-F725E90B2A-L004002](../../tests/test_web_agent.py#L4002) | 4002 | `"    assert web_agent._public_ip_literals(\"untrusted.example\") is None"` | — |
| [SRC-F725E90B2A-L004003](../../tests/test_web_agent.py#L4003) | 4003 | `""` | — |
| [SRC-F725E90B2A-L004004](../../tests/test_web_agent.py#L4004) | 4004 | `""` | — |
| [SRC-F725E90B2A-L004005](../../tests/test_web_agent.py#L4005) | 4005 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L004006](../../tests/test_web_agent.py#L4006) | 4006 | `"    \"url\","` | — |
| [SRC-F725E90B2A-L004007](../../tests/test_web_agent.py#L4007) | 4007 | `"    ["` | — |
| [SRC-F725E90B2A-L004008](../../tests/test_web_agent.py#L4008) | 4008 | `"        \"http://127.0.0.1/private\","` | — |
| [SRC-F725E90B2A-L004009](../../tests/test_web_agent.py#L4009) | 4009 | `"        \"http://169.254.169.254/latest/meta-data/\","` | — |
| [SRC-F725E90B2A-L004010](../../tests/test_web_agent.py#L4010) | 4010 | `"        \"http://[::1]/private\","` | — |
| [SRC-F725E90B2A-L004011](../../tests/test_web_agent.py#L4011) | 4011 | `"        \"http://[fe80::1]/private\","` | — |
| [SRC-F725E90B2A-L004012](../../tests/test_web_agent.py#L4012) | 4012 | `"        \"http://[fd00::1]/private\","` | — |
| [SRC-F725E90B2A-L004013](../../tests/test_web_agent.py#L4013) | 4013 | `"        \"file:///etc/passwd\","` | — |
| [SRC-F725E90B2A-L004014](../../tests/test_web_agent.py#L4014) | 4014 | `"        \"https://user:password@example.com/private\","` | — |
| [SRC-F725E90B2A-L004015](../../tests/test_web_agent.py#L4015) | 4015 | `"        \"https://example.com:8443/private\","` | — |
| [SRC-F725E90B2A-L004016](../../tests/test_web_agent.py#L4016) | 4016 | `"    ],"` | — |
| [SRC-F725E90B2A-L004017](../../tests/test_web_agent.py#L4017) | 4017 | `")"` | — |
| [SRC-F725E90B2A-L004018](../../tests/test_web_agent.py#L4018) | 4018 | `"def test_public_http_url_rejects_non_public_or_unsafe_targets(url):"` | — |
| [SRC-F725E90B2A-L004019](../../tests/test_web_agent.py#L4019) | 4019 | `"    from agents.web_agent import _public_http_url"` | — |
| [SRC-F725E90B2A-L004020](../../tests/test_web_agent.py#L4020) | 4020 | `""` | — |
| [SRC-F725E90B2A-L004021](../../tests/test_web_agent.py#L4021) | 4021 | `"    assert _public_http_url(url) is None"` | — |
| [SRC-F725E90B2A-L004022](../../tests/test_web_agent.py#L4022) | 4022 | `""` | — |
| [SRC-F725E90B2A-L004023](../../tests/test_web_agent.py#L4023) | 4023 | `""` | — |
| [SRC-F725E90B2A-L004024](../../tests/test_web_agent.py#L4024) | 4024 | `"def test_fetch_page_enforces_streamed_byte_limit_when_content_length_lies(monkeypatch):"` | — |
| [SRC-F725E90B2A-L004025](../../tests/test_web_agent.py#L4025) | 4025 | `"    from contextlib import contextmanager"` | — |
| [SRC-F725E90B2A-L004026](../../tests/test_web_agent.py#L4026) | 4026 | `""` | — |
| [SRC-F725E90B2A-L004027](../../tests/test_web_agent.py#L4027) | 4027 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L004028](../../tests/test_web_agent.py#L4028) | 4028 | `""` | — |
| [SRC-F725E90B2A-L004029](../../tests/test_web_agent.py#L4029) | 4029 | `"    from agents import web_agent"` | — |
| [SRC-F725E90B2A-L004030](../../tests/test_web_agent.py#L4030) | 4030 | `""` | — |
| [SRC-F725E90B2A-L004031](../../tests/test_web_agent.py#L4031) | 4031 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L004032](../../tests/test_web_agent.py#L4032) | 4032 | `"        web_agent, \"_public_ip_literals\", lambda _host: [\"93.184.216.34\"]"` | — |
| [SRC-F725E90B2A-L004033](../../tests/test_web_agent.py#L4033) | 4033 | `"    )"` | — |
| [SRC-F725E90B2A-L004034](../../tests/test_web_agent.py#L4034) | 4034 | `"    chunks_yielded = []"` | — |
| [SRC-F725E90B2A-L004035](../../tests/test_web_agent.py#L4035) | 4035 | `""` | — |
| [SRC-F725E90B2A-L004036](../../tests/test_web_agent.py#L4036) | 4036 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L004037](../../tests/test_web_agent.py#L4037) | 4037 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L004038](../../tests/test_web_agent.py#L4038) | 4038 | `"        encoding = \"utf-8\""` | — |
| [SRC-F725E90B2A-L004039](../../tests/test_web_agent.py#L4039) | 4039 | `""` | — |
| [SRC-F725E90B2A-L004040](../../tests/test_web_agent.py#L4040) | 4040 | `"        def __init__(self):"` | — |
| [SRC-F725E90B2A-L004041](../../tests/test_web_agent.py#L4041) | 4041 | `"            self.headers = {"` | — |
| [SRC-F725E90B2A-L004042](../../tests/test_web_agent.py#L4042) | 4042 | `"                \"content-type\": \"text/plain; charset=utf-8\","` | — |
| [SRC-F725E90B2A-L004043](../../tests/test_web_agent.py#L4043) | 4043 | `"                # Deliberately under-reports the actual streamed body length."` | — |
| [SRC-F725E90B2A-L004044](../../tests/test_web_agent.py#L4044) | 4044 | `"                \"content-length\": \"1\","` | — |
| [SRC-F725E90B2A-L004045](../../tests/test_web_agent.py#L4045) | 4045 | `"            }"` | — |
| [SRC-F725E90B2A-L004046](../../tests/test_web_agent.py#L4046) | 4046 | `""` | — |
| [SRC-F725E90B2A-L004047](../../tests/test_web_agent.py#L4047) | 4047 | `"        def iter_bytes(self):"` | — |
| [SRC-F725E90B2A-L004048](../../tests/test_web_agent.py#L4048) | 4048 | `"            chunks = ("` | — |
| [SRC-F725E90B2A-L004049](../../tests/test_web_agent.py#L4049) | 4049 | `"                b\"A\" * web_agent.MAX_PAGE_BYTES,"` | — |
| [SRC-F725E90B2A-L004050](../../tests/test_web_agent.py#L4050) | 4050 | `"                b\"B\" * 32,"` | — |
| [SRC-F725E90B2A-L004051](../../tests/test_web_agent.py#L4051) | 4051 | `"                b\"C\" * 32,"` | — |
| [SRC-F725E90B2A-L004052](../../tests/test_web_agent.py#L4052) | 4052 | `"            )"` | — |
| [SRC-F725E90B2A-L004053](../../tests/test_web_agent.py#L4053) | 4053 | `"            for chunk in chunks:"` | — |
| [SRC-F725E90B2A-L004054](../../tests/test_web_agent.py#L4054) | 4054 | `"                chunks_yielded.append(len(chunk))"` | — |
| [SRC-F725E90B2A-L004055](../../tests/test_web_agent.py#L4055) | 4055 | `"                yield chunk"` | — |
| [SRC-F725E90B2A-L004056](../../tests/test_web_agent.py#L4056) | 4056 | `""` | — |
| [SRC-F725E90B2A-L004057](../../tests/test_web_agent.py#L4057) | 4057 | `"    @contextmanager"` | — |
| [SRC-F725E90B2A-L004058](../../tests/test_web_agent.py#L4058) | 4058 | `"    def fake_stream(self, method, url, **kwargs):"` | — |
| [SRC-F725E90B2A-L004059](../../tests/test_web_agent.py#L4059) | 4059 | `"        assert method == \"GET\""` | — |
| [SRC-F725E90B2A-L004060](../../tests/test_web_agent.py#L4060) | 4060 | `"        assert str(url) == \"https://93.184.216.34/large.txt\""` | — |
| [SRC-F725E90B2A-L004061](../../tests/test_web_agent.py#L4061) | 4061 | `"        yield FakeResponse()"` | — |
| [SRC-F725E90B2A-L004062](../../tests/test_web_agent.py#L4062) | 4062 | `""` | — |
| [SRC-F725E90B2A-L004063](../../tests/test_web_agent.py#L4063) | 4063 | `"    class FakeClient:"` | — |
| [SRC-F725E90B2A-L004064](../../tests/test_web_agent.py#L4064) | 4064 | `"        def __init__(self, **kwargs):"` | — |
| [SRC-F725E90B2A-L004065](../../tests/test_web_agent.py#L4065) | 4065 | `"            self.options = kwargs"` | — |
| [SRC-F725E90B2A-L004066](../../tests/test_web_agent.py#L4066) | 4066 | `""` | — |
| [SRC-F725E90B2A-L004067](../../tests/test_web_agent.py#L4067) | 4067 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L004068](../../tests/test_web_agent.py#L4068) | 4068 | `"            return self"` | — |
| [SRC-F725E90B2A-L004069](../../tests/test_web_agent.py#L4069) | 4069 | `""` | — |
| [SRC-F725E90B2A-L004070](../../tests/test_web_agent.py#L4070) | 4070 | `"        def __exit__(self, *_args):"` | — |
| [SRC-F725E90B2A-L004071](../../tests/test_web_agent.py#L4071) | 4071 | `"            return False"` | — |
| [SRC-F725E90B2A-L004072](../../tests/test_web_agent.py#L4072) | 4072 | `""` | — |
| [SRC-F725E90B2A-L004073](../../tests/test_web_agent.py#L4073) | 4073 | `"        stream = fake_stream"` | — |
| [SRC-F725E90B2A-L004074](../../tests/test_web_agent.py#L4074) | 4074 | `""` | — |
| [SRC-F725E90B2A-L004075](../../tests/test_web_agent.py#L4075) | 4075 | `"    monkeypatch.setattr(httpx, \"Client\", FakeClient)"` | — |
| [SRC-F725E90B2A-L004076](../../tests/test_web_agent.py#L4076) | 4076 | `"    result = web_agent.WebAgent()._fetch_page(\"https://example.com/large.txt\")"` | — |
| [SRC-F725E90B2A-L004077](../../tests/test_web_agent.py#L4077) | 4077 | `""` | — |
| [SRC-F725E90B2A-L004078](../../tests/test_web_agent.py#L4078) | 4078 | `"    assert result.status == \"partial_extraction\""` | — |
| [SRC-F725E90B2A-L004079](../../tests/test_web_agent.py#L4079) | 4079 | `"    assert len(result[1]) <= web_agent.MAX_PAGE_TEXT_CHARS"` | — |
| [SRC-F725E90B2A-L004080](../../tests/test_web_agent.py#L4080) | 4080 | `"    # The reader stops as soon as the byte cap is crossed; it never asks for chunk 3."` | — |
| [SRC-F725E90B2A-L004081](../../tests/test_web_agent.py#L4081) | 4081 | `"    assert chunks_yielded == [web_agent.MAX_PAGE_BYTES, 32]"` | — |
| [SRC-F725E90B2A-L004082](../../tests/test_web_agent.py#L4082) | 4082 | `""` | — |
| [SRC-F725E90B2A-L004083](../../tests/test_web_agent.py#L4083) | 4083 | `""` | — |
| [SRC-F725E90B2A-L004084](../../tests/test_web_agent.py#L4084) | 4084 | `""` | — |
| [SRC-F725E90B2A-L004085](../../tests/test_web_agent.py#L4085) | 4085 | `"@pytest.mark.parametrize(\"field\", [\"title\", \"snippet\", \"page_text\"])"` | — |
| [SRC-F725E90B2A-L004086](../../tests/test_web_agent.py#L4086) | 4086 | `"def test_generate_keeps_title_snippet_and_page_text_untrusted(field, monkeypatch):"` | — |
| [SRC-F725E90B2A-L004087](../../tests/test_web_agent.py#L4087) | 4087 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L004088](../../tests/test_web_agent.py#L4088) | 4088 | `"    source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L004089](../../tests/test_web_agent.py#L4089) | 4089 | `"    injected_text = f\"INJECTED INSTRUCTION FROM UNTRUSTED {field.upper()}\""` | — |
| [SRC-F725E90B2A-L004090](../../tests/test_web_agent.py#L4090) | 4090 | `"    source[field] = injected_text"` | — |
| [SRC-F725E90B2A-L004091](../../tests/test_web_agent.py#L4091) | 4091 | `"    if field == \"snippet\":"` | — |
| [SRC-F725E90B2A-L004092](../../tests/test_web_agent.py#L4092) | 4092 | `"        source[\"page_text\"] = \"\""` | — |
| [SRC-F725E90B2A-L004093](../../tests/test_web_agent.py#L4093) | 4093 | `"    captured = {}"` | — |
| [SRC-F725E90B2A-L004094](../../tests/test_web_agent.py#L4094) | 4094 | `""` | — |
| [SRC-F725E90B2A-L004095](../../tests/test_web_agent.py#L4095) | 4095 | `"    def fake_completion(messages, **kwargs):"` | — |
| [SRC-F725E90B2A-L004096](../../tests/test_web_agent.py#L4096) | 4096 | `"        captured[\"messages\"] = messages"` | — |
| [SRC-F725E90B2A-L004097](../../tests/test_web_agent.py#L4097) | 4097 | `"        return \"إجابة اختبارية.\""` | — |
| [SRC-F725E90B2A-L004098](../../tests/test_web_agent.py#L4098) | 4098 | `""` | — |
| [SRC-F725E90B2A-L004099](../../tests/test_web_agent.py#L4099) | 4099 | `"    monkeypatch.setattr(agent, \"_request_completion\", fake_completion)"` | — |
| [SRC-F725E90B2A-L004100](../../tests/test_web_agent.py#L4100) | 4100 | `"    answer = agent._generate("` | — |
| [SRC-F725E90B2A-L004101](../../tests/test_web_agent.py#L4101) | 4101 | `"        question=\"ما الذي يقوله المصدر؟\","` | — |
| [SRC-F725E90B2A-L004102](../../tests/test_web_agent.py#L4102) | 4102 | `"        history=[],"` | — |
| [SRC-F725E90B2A-L004103](../../tests/test_web_agent.py#L4103) | 4103 | `"        sources=[source],"` | — |
| [SRC-F725E90B2A-L004104](../../tests/test_web_agent.py#L4104) | 4104 | `"        search_warning=None,"` | — |
| [SRC-F725E90B2A-L004105](../../tests/test_web_agent.py#L4105) | 4105 | `"        research_plan={\"depth\": \"standard\", \"queries\": [\"ما الذي يقوله المصدر؟\"]},"` | — |
| [SRC-F725E90B2A-L004106](../../tests/test_web_agent.py#L4106) | 4106 | `"        search_report={},"` | — |
| [SRC-F725E90B2A-L004107](../../tests/test_web_agent.py#L4107) | 4107 | `"    )"` | — |
| [SRC-F725E90B2A-L004108](../../tests/test_web_agent.py#L4108) | 4108 | `""` | — |
| [SRC-F725E90B2A-L004109](../../tests/test_web_agent.py#L4109) | 4109 | `"    messages = captured[\"messages\"]"` | — |
| [SRC-F725E90B2A-L004110](../../tests/test_web_agent.py#L4110) | 4110 | `"    system_content = \"\\n\".join("` | — |
| [SRC-F725E90B2A-L004111](../../tests/test_web_agent.py#L4111) | 4111 | `"        message[\"content\"] for message in messages if message[\"role\"] == \"system\""` | — |
| [SRC-F725E90B2A-L004112](../../tests/test_web_agent.py#L4112) | 4112 | `"    )"` | — |
| [SRC-F725E90B2A-L004113](../../tests/test_web_agent.py#L4113) | 4113 | `"    user_contents = ["` | — |
| [SRC-F725E90B2A-L004114](../../tests/test_web_agent.py#L4114) | 4114 | `"        message[\"content\"] for message in messages if message[\"role\"] == \"user\""` | — |
| [SRC-F725E90B2A-L004115](../../tests/test_web_agent.py#L4115) | 4115 | `"    ]"` | — |
| [SRC-F725E90B2A-L004116](../../tests/test_web_agent.py#L4116) | 4116 | `""` | — |
| [SRC-F725E90B2A-L004117](../../tests/test_web_agent.py#L4117) | 4117 | `"    assert answer == \"إجابة اختبارية.\""` | — |
| [SRC-F725E90B2A-L004118](../../tests/test_web_agent.py#L4118) | 4118 | `"    assert injected_text not in system_content"` | — |
| [SRC-F725E90B2A-L004119](../../tests/test_web_agent.py#L4119) | 4119 | `"    assert any(injected_text in value for value in user_contents)"` | — |
| [SRC-F725E90B2A-L004120](../../tests/test_web_agent.py#L4120) | 4120 | `""` | — |
| [SRC-F725E90B2A-L004121](../../tests/test_web_agent.py#L4121) | 4121 | `""` | — |
| [SRC-F725E90B2A-L004122](../../tests/test_web_agent.py#L4122) | 4122 | `"@pytest.mark.parametrize(\"field\", [\"title\", \"snippet\", \"page_text\"])"` | — |
| [SRC-F725E90B2A-L004123](../../tests/test_web_agent.py#L4123) | 4123 | `"def test_review_keeps_title_snippet_and_page_text_untrusted(field, monkeypatch):"` | — |
| [SRC-F725E90B2A-L004124](../../tests/test_web_agent.py#L4124) | 4124 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L004125](../../tests/test_web_agent.py#L4125) | 4125 | `"    source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L004126](../../tests/test_web_agent.py#L4126) | 4126 | `"    injected_text = f\"INJECTED REVIEW INSTRUCTION FROM UNTRUSTED {field.upper()}\""` | — |
| [SRC-F725E90B2A-L004127](../../tests/test_web_agent.py#L4127) | 4127 | `"    source[field] = injected_text"` | — |
| [SRC-F725E90B2A-L004128](../../tests/test_web_agent.py#L4128) | 4128 | `"    if field == \"snippet\":"` | — |
| [SRC-F725E90B2A-L004129](../../tests/test_web_agent.py#L4129) | 4129 | `"        source[\"page_text\"] = \"\""` | — |
| [SRC-F725E90B2A-L004130](../../tests/test_web_agent.py#L4130) | 4130 | `"    captured = {}"` | — |
| [SRC-F725E90B2A-L004131](../../tests/test_web_agent.py#L4131) | 4131 | `""` | — |
| [SRC-F725E90B2A-L004132](../../tests/test_web_agent.py#L4132) | 4132 | `"    def fake_completion(messages, **kwargs):"` | — |
| [SRC-F725E90B2A-L004133](../../tests/test_web_agent.py#L4133) | 4133 | `"        captured[\"messages\"] = messages"` | — |
| [SRC-F725E90B2A-L004134](../../tests/test_web_agent.py#L4134) | 4134 | `"        return \"<<<OMARAI_FINAL_ANSWER>>>تم تدقيق الإجابة.<<<END_OMARAI_FINAL_ANSWER>>>\""` | — |
| [SRC-F725E90B2A-L004135](../../tests/test_web_agent.py#L4135) | 4135 | `""` | — |
| [SRC-F725E90B2A-L004136](../../tests/test_web_agent.py#L4136) | 4136 | `"    monkeypatch.setattr(agent, \"_request_completion\", fake_completion)"` | — |
| [SRC-F725E90B2A-L004137](../../tests/test_web_agent.py#L4137) | 4137 | `"    answer = agent._review_answer("` | — |
| [SRC-F725E90B2A-L004138](../../tests/test_web_agent.py#L4138) | 4138 | `"        question=\"ما الذي يقوله المصدر؟\","` | — |
| [SRC-F725E90B2A-L004139](../../tests/test_web_agent.py#L4139) | 4139 | `"        answer=\"مسودة إجابة تحتاج التحقق.\","` | — |
| [SRC-F725E90B2A-L004140](../../tests/test_web_agent.py#L4140) | 4140 | `"        sources=[source],"` | — |
| [SRC-F725E90B2A-L004141](../../tests/test_web_agent.py#L4141) | 4141 | `"    )"` | — |
| [SRC-F725E90B2A-L004142](../../tests/test_web_agent.py#L4142) | 4142 | `""` | — |
| [SRC-F725E90B2A-L004143](../../tests/test_web_agent.py#L4143) | 4143 | `"    messages = captured[\"messages\"]"` | — |
| [SRC-F725E90B2A-L004144](../../tests/test_web_agent.py#L4144) | 4144 | `"    system_content = \"\\n\".join("` | — |
| [SRC-F725E90B2A-L004145](../../tests/test_web_agent.py#L4145) | 4145 | `"        message[\"content\"] for message in messages if message[\"role\"] == \"system\""` | — |
| [SRC-F725E90B2A-L004146](../../tests/test_web_agent.py#L4146) | 4146 | `"    )"` | — |
| [SRC-F725E90B2A-L004147](../../tests/test_web_agent.py#L4147) | 4147 | `"    user_contents = ["` | — |
| [SRC-F725E90B2A-L004148](../../tests/test_web_agent.py#L4148) | 4148 | `"        message[\"content\"] for message in messages if message[\"role\"] == \"user\""` | — |
| [SRC-F725E90B2A-L004149](../../tests/test_web_agent.py#L4149) | 4149 | `"    ]"` | — |
| [SRC-F725E90B2A-L004150](../../tests/test_web_agent.py#L4150) | 4150 | `""` | — |
| [SRC-F725E90B2A-L004151](../../tests/test_web_agent.py#L4151) | 4151 | `"    assert answer == \"تم تدقيق الإجابة.\""` | — |
| [SRC-F725E90B2A-L004152](../../tests/test_web_agent.py#L4152) | 4152 | `"    assert injected_text not in system_content"` | — |
| [SRC-F725E90B2A-L004153](../../tests/test_web_agent.py#L4153) | 4153 | `"    assert any(injected_text in value for value in user_contents)"` | — |
| [SRC-F725E90B2A-L004154](../../tests/test_web_agent.py#L4154) | 4154 | `""` | — |
| [SRC-F725E90B2A-L004155](../../tests/test_web_agent.py#L4155) | 4155 | `""` | — |
| [SRC-F725E90B2A-L004156](../../tests/test_web_agent.py#L4156) | 4156 | `""` | — |
| [SRC-F725E90B2A-L004157](../../tests/test_web_agent.py#L4157) | 4157 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L004158](../../tests/test_web_agent.py#L4158) | 4158 | `"    \"url\","` | — |
| [SRC-F725E90B2A-L004159](../../tests/test_web_agent.py#L4159) | 4159 | `"    ["` | — |
| [SRC-F725E90B2A-L004160](../../tests/test_web_agent.py#L4160) | 4160 | `"        \"https://api.example.test/v1\","` | — |
| [SRC-F725E90B2A-L004161](../../tests/test_web_agent.py#L4161) | 4161 | `"        \"http://localhost:11434/v1\","` | — |
| [SRC-F725E90B2A-L004162](../../tests/test_web_agent.py#L4162) | 4162 | `"        \"http://127.0.0.1:8080/v1\","` | — |
| [SRC-F725E90B2A-L004163](../../tests/test_web_agent.py#L4163) | 4163 | `"        \"http://[::1]:8000/v1\","` | — |
| [SRC-F725E90B2A-L004164](../../tests/test_web_agent.py#L4164) | 4164 | `"    ],"` | — |
| [SRC-F725E90B2A-L004165](../../tests/test_web_agent.py#L4165) | 4165 | `")"` | — |
| [SRC-F725E90B2A-L004166](../../tests/test_web_agent.py#L4166) | 4166 | `"def test_model_provider_base_url_allows_https_or_loopback(url):"` | — |
| [SRC-F725E90B2A-L004167](../../tests/test_web_agent.py#L4167) | 4167 | `"    from agents.web_agent import _is_safe_model_base_url"` | — |
| [SRC-F725E90B2A-L004168](../../tests/test_web_agent.py#L4168) | 4168 | `""` | — |
| [SRC-F725E90B2A-L004169](../../tests/test_web_agent.py#L4169) | 4169 | `"    assert _is_safe_model_base_url(url) is True"` | — |
| [SRC-F725E90B2A-L004170](../../tests/test_web_agent.py#L4170) | 4170 | `""` | — |
| [SRC-F725E90B2A-L004171](../../tests/test_web_agent.py#L4171) | 4171 | `""` | — |
| [SRC-F725E90B2A-L004172](../../tests/test_web_agent.py#L4172) | 4172 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L004173](../../tests/test_web_agent.py#L4173) | 4173 | `"    \"url\","` | — |
| [SRC-F725E90B2A-L004174](../../tests/test_web_agent.py#L4174) | 4174 | `"    ["` | — |
| [SRC-F725E90B2A-L004175](../../tests/test_web_agent.py#L4175) | 4175 | `"        \"http://api.example.test/v1\","` | — |
| [SRC-F725E90B2A-L004176](../../tests/test_web_agent.py#L4176) | 4176 | `"        \"ftp://api.example.test/v1\","` | — |
| [SRC-F725E90B2A-L004177](../../tests/test_web_agent.py#L4177) | 4177 | `"        \"https://user:password@api.example.test/v1\","` | — |
| [SRC-F725E90B2A-L004178](../../tests/test_web_agent.py#L4178) | 4178 | `"        \"https://api.example.test/v1?token=secret\","` | — |
| [SRC-F725E90B2A-L004179](../../tests/test_web_agent.py#L4179) | 4179 | `"        \"https://api.example.test/v1#fragment\","` | — |
| [SRC-F725E90B2A-L004180](../../tests/test_web_agent.py#L4180) | 4180 | `"        \"https:///missing-host\","` | — |
| [SRC-F725E90B2A-L004181](../../tests/test_web_agent.py#L4181) | 4181 | `"        \"https://api.example.test:99999/v1\","` | — |
| [SRC-F725E90B2A-L004182](../../tests/test_web_agent.py#L4182) | 4182 | `"    ],"` | — |
| [SRC-F725E90B2A-L004183](../../tests/test_web_agent.py#L4183) | 4183 | `")"` | — |
| [SRC-F725E90B2A-L004184](../../tests/test_web_agent.py#L4184) | 4184 | `"def test_model_provider_base_url_rejects_insecure_or_ambiguous_urls(url):"` | — |
| [SRC-F725E90B2A-L004185](../../tests/test_web_agent.py#L4185) | 4185 | `"    from agents.web_agent import _is_safe_model_base_url"` | — |
| [SRC-F725E90B2A-L004186](../../tests/test_web_agent.py#L4186) | 4186 | `""` | — |
| [SRC-F725E90B2A-L004187](../../tests/test_web_agent.py#L4187) | 4187 | `"    assert _is_safe_model_base_url(url) is False"` | — |
| [SRC-F725E90B2A-L004188](../../tests/test_web_agent.py#L4188) | 4188 | `""` | — |
| [SRC-F725E90B2A-L004189](../../tests/test_web_agent.py#L4189) | 4189 | `""` | — |
| [SRC-F725E90B2A-L004190](../../tests/test_web_agent.py#L4190) | 4190 | `"def test_model_provider_rejects_remote_http_before_sending_bearer_key(monkeypatch):"` | — |
| [SRC-F725E90B2A-L004191](../../tests/test_web_agent.py#L4191) | 4191 | `"    from agents import web_agent"` | — |
| [SRC-F725E90B2A-L004192](../../tests/test_web_agent.py#L4192) | 4192 | `""` | — |
| [SRC-F725E90B2A-L004193](../../tests/test_web_agent.py#L4193) | 4193 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L004194](../../tests/test_web_agent.py#L4194) | 4194 | `"    agent.api_key = \"unit-test-secret\""` | — |
| [SRC-F725E90B2A-L004195](../../tests/test_web_agent.py#L4195) | 4195 | `"    agent.base_url = \"http://provider.example/api/v1\""` | — |
| [SRC-F725E90B2A-L004196](../../tests/test_web_agent.py#L4196) | 4196 | `""` | — |
| [SRC-F725E90B2A-L004197](../../tests/test_web_agent.py#L4197) | 4197 | `"    def unexpected_request(*_args, **_kwargs):"` | — |
| [SRC-F725E90B2A-L004198](../../tests/test_web_agent.py#L4198) | 4198 | `"        pytest.fail(\"bearer credentials must not be sent to a remote HTTP URL\")"` | — |
| [SRC-F725E90B2A-L004199](../../tests/test_web_agent.py#L4199) | 4199 | `""` | — |
| [SRC-F725E90B2A-L004200](../../tests/test_web_agent.py#L4200) | 4200 | `"    monkeypatch.setattr(web_agent, \"_open_model_request\", unexpected_request)"` | — |
| [SRC-F725E90B2A-L004201](../../tests/test_web_agent.py#L4201) | 4201 | `"    with pytest.raises(RuntimeError, match=\"HTTPS\"):"` | — |
| [SRC-F725E90B2A-L004202](../../tests/test_web_agent.py#L4202) | 4202 | `"        agent._request_completion("` | — |
| [SRC-F725E90B2A-L004203](../../tests/test_web_agent.py#L4203) | 4203 | `"            [{\"role\": \"user\", \"content\": \"test\"}],"` | — |
| [SRC-F725E90B2A-L004204](../../tests/test_web_agent.py#L4204) | 4204 | `"            max_tokens=100,"` | — |
| [SRC-F725E90B2A-L004205](../../tests/test_web_agent.py#L4205) | 4205 | `"        )"` | — |
| [SRC-F725E90B2A-L004206](../../tests/test_web_agent.py#L4206) | 4206 | `""` | — |
| [SRC-F725E90B2A-L004207](../../tests/test_web_agent.py#L4207) | 4207 | `"    assert agent.generation_diagnostics[-1][\"status\"] == \"unsafe_provider_url\""` | — |
| [SRC-F725E90B2A-L004208](../../tests/test_web_agent.py#L4208) | 4208 | `"    assert agent.generation_diagnostics[-1][\"request_started\"] == \"false\""` | — |
| [SRC-F725E90B2A-L004209](../../tests/test_web_agent.py#L4209) | 4209 | `""` | — |
| [SRC-F725E90B2A-L004210](../../tests/test_web_agent.py#L4210) | 4210 | `""` | — |
| [SRC-F725E90B2A-L004211](../../tests/test_web_agent.py#L4211) | 4211 | `"def test_health_status_redacts_model_provider_userinfo_path_and_query(monkeypatch):"` | — |
| [SRC-F725E90B2A-L004212](../../tests/test_web_agent.py#L4212) | 4212 | `"    monkeypatch.setenv("` | — |
| [SRC-F725E90B2A-L004213](../../tests/test_web_agent.py#L4213) | 4213 | `"        \"OMARAI_LLM_BASE_URL\","` | — |
| [SRC-F725E90B2A-L004214](../../tests/test_web_agent.py#L4214) | 4214 | `"        \"https://health-user:health-password@provider.example/api/v1?token=health-secret\","` | — |
| [SRC-F725E90B2A-L004215](../../tests/test_web_agent.py#L4215) | 4215 | `"    )"` | — |
| [SRC-F725E90B2A-L004216](../../tests/test_web_agent.py#L4216) | 4216 | `""` | — |
| [SRC-F725E90B2A-L004217](../../tests/test_web_agent.py#L4217) | 4217 | `"    status = WebAgent.status()"` | — |
| [SRC-F725E90B2A-L004218](../../tests/test_web_agent.py#L4218) | 4218 | `"    provider = status[\"language_model_provider\"]"` | — |
| [SRC-F725E90B2A-L004219](../../tests/test_web_agent.py#L4219) | 4219 | `""` | — |
| [SRC-F725E90B2A-L004220](../../tests/test_web_agent.py#L4220) | 4220 | `"    assert provider == \"https://provider.example\""` | — |
| [SRC-F725E90B2A-L004221](../../tests/test_web_agent.py#L4221) | 4221 | `"    assert \"health-user\" not in provider"` | — |
| [SRC-F725E90B2A-L004222](../../tests/test_web_agent.py#L4222) | 4222 | `"    assert \"health-password\" not in provider"` | — |
| [SRC-F725E90B2A-L004223](../../tests/test_web_agent.py#L4223) | 4223 | `"    assert \"health-secret\" not in provider"` | — |
| [SRC-F725E90B2A-L004224](../../tests/test_web_agent.py#L4224) | 4224 | `"    assert \"/api/v1\" not in provider"` | — |
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
