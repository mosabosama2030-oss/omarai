# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **066**
- سجلات الأسطر: **800**
- النطاق: SRC-F725E90B2A-L003669 إلى SRC-F725E90B2A-L004468
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-F725E90B2A — [tests/test_web_agent.py](../../tests/test_web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-F725E90B2A-L003669](../../tests/test_web_agent.py#L3669) | 3669 | `"        lambda _question, _history: {"` | — |
| [SRC-F725E90B2A-L003670](../../tests/test_web_agent.py#L3670) | 3670 | `"            \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L003671](../../tests/test_web_agent.py#L3671) | 3671 | `"            \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L003672](../../tests/test_web_agent.py#L3672) | 3672 | `"            \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003673](../../tests/test_web_agent.py#L3673) | 3673 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003674](../../tests/test_web_agent.py#L3674) | 3674 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003675](../../tests/test_web_agent.py#L3675) | 3675 | `"            \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003676](../../tests/test_web_agent.py#L3676) | 3676 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003677](../../tests/test_web_agent.py#L3677) | 3677 | `"        },"` | — |
| [SRC-F725E90B2A-L003678](../../tests/test_web_agent.py#L3678) | 3678 | `"    )"` | — |
| [SRC-F725E90B2A-L003679](../../tests/test_web_agent.py#L3679) | 3679 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003680](../../tests/test_web_agent.py#L3680) | 3680 | `"        \"agents.web_agent.fallback_plan\","` | — |
| [SRC-F725E90B2A-L003681](../../tests/test_web_agent.py#L3681) | 3681 | `"        lambda *args, **kwargs: {\"queries\": [question]},"` | — |
| [SRC-F725E90B2A-L003682](../../tests/test_web_agent.py#L3682) | 3682 | `"    )"` | — |
| [SRC-F725E90B2A-L003683](../../tests/test_web_agent.py#L3683) | 3683 | `""` | — |
| [SRC-F725E90B2A-L003684](../../tests/test_web_agent.py#L3684) | 3684 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L003685](../../tests/test_web_agent.py#L3685) | 3685 | `"        observed_plans.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L003686](../../tests/test_web_agent.py#L3686) | 3686 | `"        return [], [], {"` | — |
| [SRC-F725E90B2A-L003687](../../tests/test_web_agent.py#L3687) | 3687 | `"            \"queries_planned\": len(research_plan.get(\"queries\", [])),"` | — |
| [SRC-F725E90B2A-L003688](../../tests/test_web_agent.py#L3688) | 3688 | `"            \"queries_attempted\": 0,"` | — |
| [SRC-F725E90B2A-L003689](../../tests/test_web_agent.py#L3689) | 3689 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L003690](../../tests/test_web_agent.py#L3690) | 3690 | `"            \"unique_sources\": 0,"` | — |
| [SRC-F725E90B2A-L003691](../../tests/test_web_agent.py#L3691) | 3691 | `"            \"pages_fetched\": 0,"` | — |
| [SRC-F725E90B2A-L003692](../../tests/test_web_agent.py#L3692) | 3692 | `"            \"providers_used\": [],"` | — |
| [SRC-F725E90B2A-L003693](../../tests/test_web_agent.py#L3693) | 3693 | `"            \"platform_counts\": {},"` | — |
| [SRC-F725E90B2A-L003694](../../tests/test_web_agent.py#L3694) | 3694 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L003695](../../tests/test_web_agent.py#L3695) | 3695 | `"            \"depth\": research_plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-F725E90B2A-L003696](../../tests/test_web_agent.py#L3696) | 3696 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003697](../../tests/test_web_agent.py#L3697) | 3697 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L003698](../../tests/test_web_agent.py#L3698) | 3698 | `"        }"` | — |
| [SRC-F725E90B2A-L003699](../../tests/test_web_agent.py#L3699) | 3699 | `""` | — |
| [SRC-F725E90B2A-L003700](../../tests/test_web_agent.py#L3700) | 3700 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L003701](../../tests/test_web_agent.py#L3701) | 3701 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"لم أعثر على مصدر.\")"` | — |
| [SRC-F725E90B2A-L003702](../../tests/test_web_agent.py#L3702) | 3702 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda _question, answer, _sources: answer)"` | — |
| [SRC-F725E90B2A-L003703](../../tests/test_web_agent.py#L3703) | 3703 | `""` | — |
| [SRC-F725E90B2A-L003704](../../tests/test_web_agent.py#L3704) | 3704 | `"    agent.answer(question, mode=\"auto\")"` | — |
| [SRC-F725E90B2A-L003705](../../tests/test_web_agent.py#L3705) | 3705 | `""` | — |
| [SRC-F725E90B2A-L003706](../../tests/test_web_agent.py#L3706) | 3706 | `"    assert observed_plans"` | — |
| [SRC-F725E90B2A-L003707](../../tests/test_web_agent.py#L3707) | 3707 | `"    assert observed_plans[0][\"queries\"]"` | — |
| [SRC-F725E90B2A-L003708](../../tests/test_web_agent.py#L3708) | 3708 | `"    assert all(not query.startswith(\"ابحث عن\") for query in observed_plans[0][\"queries\"])"` | — |
| [SRC-F725E90B2A-L003709](../../tests/test_web_agent.py#L3709) | 3709 | `"    assert \"الموقع الرسمي لشركة النور\" in observed_plans[0][\"queries\"][0]"` | — |
| [SRC-F725E90B2A-L003710](../../tests/test_web_agent.py#L3710) | 3710 | `"def test_latest_mode_does_not_generate_answer_from_stale_pages(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003711](../../tests/test_web_agent.py#L3711) | 3711 | `"    \"\"\"Current-mode answers must abstain if only old pages survive retrieval.\"\"\""` | — |
| [SRC-F725E90B2A-L003712](../../tests/test_web_agent.py#L3712) | 3712 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003713](../../tests/test_web_agent.py#L3713) | 3713 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L003714](../../tests/test_web_agent.py#L3714) | 3714 | `"        \"queries\": [\"مواعيد عمل مكتب الجوازات العباسية اليوم\"],"` | — |
| [SRC-F725E90B2A-L003715](../../tests/test_web_agent.py#L3715) | 3715 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L003716](../../tests/test_web_agent.py#L3716) | 3716 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003717](../../tests/test_web_agent.py#L3717) | 3717 | `"        \"freshness\": \"current\","` | — |
| [SRC-F725E90B2A-L003718](../../tests/test_web_agent.py#L3718) | 3718 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003719](../../tests/test_web_agent.py#L3719) | 3719 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003720](../../tests/test_web_agent.py#L3720) | 3720 | `"        \"planning_method\": \"fixture\","` | — |
| [SRC-F725E90B2A-L003721](../../tests/test_web_agent.py#L3721) | 3721 | `"        \"coverage_targets\": [],"` | — |
| [SRC-F725E90B2A-L003722](../../tests/test_web_agent.py#L3722) | 3722 | `"    }"` | — |
| [SRC-F725E90B2A-L003723](../../tests/test_web_agent.py#L3723) | 3723 | `"    collection_calls = []"` | — |
| [SRC-F725E90B2A-L003724](../../tests/test_web_agent.py#L3724) | 3724 | `""` | — |
| [SRC-F725E90B2A-L003725](../../tests/test_web_agent.py#L3725) | 3725 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L003726](../../tests/test_web_agent.py#L3726) | 3726 | `"        collection_calls.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L003727](../../tests/test_web_agent.py#L3727) | 3727 | `"        old_page = sample_source(0)"` | — |
| [SRC-F725E90B2A-L003728](../../tests/test_web_agent.py#L3728) | 3728 | `"        old_page.update({"` | — |
| [SRC-F725E90B2A-L003729](../../tests/test_web_agent.py#L3729) | 3729 | `"            \"url\": \"https://moi.gov.eg/passports\","` | — |
| [SRC-F725E90B2A-L003730](../../tests/test_web_agent.py#L3730) | 3730 | `"            \"domain\": \"moi.gov.eg\","` | — |
| [SRC-F725E90B2A-L003731](../../tests/test_web_agent.py#L3731) | 3731 | `"            \"published_at\": \"2024-01-01T10:00:00Z\","` | — |
| [SRC-F725E90B2A-L003732](../../tests/test_web_agent.py#L3732) | 3732 | `"            \"page_fetched\": True,"` | — |
| [SRC-F725E90B2A-L003733](../../tests/test_web_agent.py#L3733) | 3733 | `"            \"page_text\": \"محتوى قديم عن مواعيد العمل\","` | — |
| [SRC-F725E90B2A-L003734](../../tests/test_web_agent.py#L3734) | 3734 | `"        })"` | — |
| [SRC-F725E90B2A-L003735](../../tests/test_web_agent.py#L3735) | 3735 | `"        return [old_page], [], {"` | — |
| [SRC-F725E90B2A-L003736](../../tests/test_web_agent.py#L3736) | 3736 | `"            \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L003737](../../tests/test_web_agent.py#L3737) | 3737 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L003738](../../tests/test_web_agent.py#L3738) | 3738 | `"            \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L003739](../../tests/test_web_agent.py#L3739) | 3739 | `"            \"pages_fetched\": 1,"` | — |
| [SRC-F725E90B2A-L003740](../../tests/test_web_agent.py#L3740) | 3740 | `"            \"providers_used\": [\"fixture\"],"` | — |
| [SRC-F725E90B2A-L003741](../../tests/test_web_agent.py#L3741) | 3741 | `"            \"provider_counts\": {\"fixture\": 1},"` | — |
| [SRC-F725E90B2A-L003742](../../tests/test_web_agent.py#L3742) | 3742 | `"            \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L003743](../../tests/test_web_agent.py#L3743) | 3743 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L003744](../../tests/test_web_agent.py#L3744) | 3744 | `"            \"expansion_queries\": [],"` | — |
| [SRC-F725E90B2A-L003745](../../tests/test_web_agent.py#L3745) | 3745 | `"            \"provider_diagnostics\": [],"` | — |
| [SRC-F725E90B2A-L003746](../../tests/test_web_agent.py#L3746) | 3746 | `"            \"query_results\": [{\"query\": research_plan[\"queries\"][0], \"results\": 1}],"` | — |
| [SRC-F725E90B2A-L003747](../../tests/test_web_agent.py#L3747) | 3747 | `"        }"` | — |
| [SRC-F725E90B2A-L003748](../../tests/test_web_agent.py#L3748) | 3748 | `""` | — |
| [SRC-F725E90B2A-L003749](../../tests/test_web_agent.py#L3749) | 3749 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda *args, **kwargs: dict(plan))"` | — |
| [SRC-F725E90B2A-L003750](../../tests/test_web_agent.py#L3750) | 3750 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L003751](../../tests/test_web_agent.py#L3751) | 3751 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L003752](../../tests/test_web_agent.py#L3752) | 3752 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003753](../../tests/test_web_agent.py#L3753) | 3753 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003754](../../tests/test_web_agent.py#L3754) | 3754 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L003755](../../tests/test_web_agent.py#L3755) | 3755 | `"        lambda *args, **kwargs: pytest.fail(\"Stale pages must not be passed to generation\"),"` | — |
| [SRC-F725E90B2A-L003756](../../tests/test_web_agent.py#L3756) | 3756 | `"    )"` | — |
| [SRC-F725E90B2A-L003757](../../tests/test_web_agent.py#L3757) | 3757 | `""` | — |
| [SRC-F725E90B2A-L003758](../../tests/test_web_agent.py#L3758) | 3758 | `"    result = agent.answer(\"ما مواعيد عمل مكتب الجوازات اليوم؟\", mode=\"latest\")"` | — |
| [SRC-F725E90B2A-L003759](../../tests/test_web_agent.py#L3759) | 3759 | `""` | — |
| [SRC-F725E90B2A-L003760](../../tests/test_web_agent.py#L3760) | 3760 | `"    assert result[\"kind\"] == \"insufficient_evidence\""` | — |
| [SRC-F725E90B2A-L003761](../../tests/test_web_agent.py#L3761) | 3761 | `"    assert len(collection_calls) >= 1"` | — |
| [SRC-F725E90B2A-L003762](../../tests/test_web_agent.py#L3762) | 3762 | `"    guardrails = result[\"search_report\"][\"source_guardrails\"]"` | — |
| [SRC-F725E90B2A-L003763](../../tests/test_web_agent.py#L3763) | 3763 | `"    assert guardrails[\"initial\"][\"rejection_counts\"][\"stale\"] == 1"` | — |
| [SRC-F725E90B2A-L003764](../../tests/test_web_agent.py#L3764) | 3764 | `"    assert guardrails[\"final\"][\"current_evidence_status\"] == \"no_current_eligible_evidence\""` | — |
| [SRC-F725E90B2A-L003765](../../tests/test_web_agent.py#L3765) | 3765 | `"    assert result[\"search_report\"][\"search_outcome\"] == \"attempted_no_usable_sources\""` | — |
| [SRC-F725E90B2A-L003766](../../tests/test_web_agent.py#L3766) | 3766 | `""` | — |
| [SRC-F725E90B2A-L003767](../../tests/test_web_agent.py#L3767) | 3767 | `"def test_official_government_lookup_never_synthesizes_tourism_result(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003768](../../tests/test_web_agent.py#L3768) | 3768 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003769](../../tests/test_web_agent.py#L3769) | 3769 | `"    question = \"ابحث عن الموقع الرسمي لوزارة الاتصالات وتكنولوجيا المعلومات المصرية\""` | — |
| [SRC-F725E90B2A-L003770](../../tests/test_web_agent.py#L3770) | 3770 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L003771](../../tests/test_web_agent.py#L3771) | 3771 | `"        \"queries\": [\"وزارة الاتصالات وتكنولوجيا المعلومات مصر الموقع الرسمي\"],"` | — |
| [SRC-F725E90B2A-L003772](../../tests/test_web_agent.py#L3772) | 3772 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L003773](../../tests/test_web_agent.py#L3773) | 3773 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003774](../../tests/test_web_agent.py#L3774) | 3774 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003775](../../tests/test_web_agent.py#L3775) | 3775 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003776](../../tests/test_web_agent.py#L3776) | 3776 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003777](../../tests/test_web_agent.py#L3777) | 3777 | `"        \"planning_method\": \"fixture\","` | — |
| [SRC-F725E90B2A-L003778](../../tests/test_web_agent.py#L3778) | 3778 | `"    }"` | — |
| [SRC-F725E90B2A-L003779](../../tests/test_web_agent.py#L3779) | 3779 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L003780](../../tests/test_web_agent.py#L3780) | 3780 | `""` | — |
| [SRC-F725E90B2A-L003781](../../tests/test_web_agent.py#L3781) | 3781 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L003782](../../tests/test_web_agent.py#L3782) | 3782 | `"        calls.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L003783](../../tests/test_web_agent.py#L3783) | 3783 | `"        candidate = sample_source(0)"` | — |
| [SRC-F725E90B2A-L003784](../../tests/test_web_agent.py#L3784) | 3784 | `"        candidate.update({"` | — |
| [SRC-F725E90B2A-L003785](../../tests/test_web_agent.py#L3785) | 3785 | `"            \"title\": \"وزارة الاتصالات في مصر ومعلومات سياحية\","` | — |
| [SRC-F725E90B2A-L003786](../../tests/test_web_agent.py#L3786) | 3786 | `"            \"url\": \"https://visitegypt.com/\","` | — |
| [SRC-F725E90B2A-L003787](../../tests/test_web_agent.py#L3787) | 3787 | `"            \"domain\": \"visitegypt.com\","` | — |
| [SRC-F725E90B2A-L003788](../../tests/test_web_agent.py#L3788) | 3788 | `"            \"snippet\": \"معلومات عن الوزارة ضمن دليل سياحي لمصر\","` | — |
| [SRC-F725E90B2A-L003789](../../tests/test_web_agent.py#L3789) | 3789 | `"            \"page_fetched\": True,"` | — |
| [SRC-F725E90B2A-L003790](../../tests/test_web_agent.py#L3790) | 3790 | `"            \"page_text\": \"معلومات سياحية تذكر وزارة الاتصالات\","` | — |
| [SRC-F725E90B2A-L003791](../../tests/test_web_agent.py#L3791) | 3791 | `"            \"queries\": list(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L003792](../../tests/test_web_agent.py#L3792) | 3792 | `"        })"` | — |
| [SRC-F725E90B2A-L003793](../../tests/test_web_agent.py#L3793) | 3793 | `"        return [candidate], [], {"` | — |
| [SRC-F725E90B2A-L003794](../../tests/test_web_agent.py#L3794) | 3794 | `"            \"queries_planned\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L003795](../../tests/test_web_agent.py#L3795) | 3795 | `"            \"queries_attempted\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L003796](../../tests/test_web_agent.py#L3796) | 3796 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L003797](../../tests/test_web_agent.py#L3797) | 3797 | `"            \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L003798](../../tests/test_web_agent.py#L3798) | 3798 | `"            \"pages_fetched\": 1,"` | — |
| [SRC-F725E90B2A-L003799](../../tests/test_web_agent.py#L3799) | 3799 | `"            \"providers_used\": [\"fixture\"],"` | — |
| [SRC-F725E90B2A-L003800](../../tests/test_web_agent.py#L3800) | 3800 | `"            \"provider_counts\": {\"fixture\": 1},"` | — |
| [SRC-F725E90B2A-L003801](../../tests/test_web_agent.py#L3801) | 3801 | `"            \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L003802](../../tests/test_web_agent.py#L3802) | 3802 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L003803](../../tests/test_web_agent.py#L3803) | 3803 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003804](../../tests/test_web_agent.py#L3804) | 3804 | `"            \"planning_method\": \"fixture\","` | — |
| [SRC-F725E90B2A-L003805](../../tests/test_web_agent.py#L3805) | 3805 | `"            \"provider_diagnostics\": [],"` | — |
| [SRC-F725E90B2A-L003806](../../tests/test_web_agent.py#L3806) | 3806 | `"        }"` | — |
| [SRC-F725E90B2A-L003807](../../tests/test_web_agent.py#L3807) | 3807 | `""` | — |
| [SRC-F725E90B2A-L003808](../../tests/test_web_agent.py#L3808) | 3808 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda *args, **kwargs: dict(plan))"` | — |
| [SRC-F725E90B2A-L003809](../../tests/test_web_agent.py#L3809) | 3809 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L003810](../../tests/test_web_agent.py#L3810) | 3810 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L003811](../../tests/test_web_agent.py#L3811) | 3811 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003812](../../tests/test_web_agent.py#L3812) | 3812 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003813](../../tests/test_web_agent.py#L3813) | 3813 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L003814](../../tests/test_web_agent.py#L3814) | 3814 | `"        lambda *args, **kwargs: pytest.fail("` | — |
| [SRC-F725E90B2A-L003815](../../tests/test_web_agent.py#L3815) | 3815 | `"            \"A tourism result must never be passed to answer generation as the official site\""` | — |
| [SRC-F725E90B2A-L003816](../../tests/test_web_agent.py#L3816) | 3816 | `"        ),"` | — |
| [SRC-F725E90B2A-L003817](../../tests/test_web_agent.py#L3817) | 3817 | `"    )"` | — |
| [SRC-F725E90B2A-L003818](../../tests/test_web_agent.py#L3818) | 3818 | `""` | — |
| [SRC-F725E90B2A-L003819](../../tests/test_web_agent.py#L3819) | 3819 | `"    result = agent.answer(question, mode=\"auto\")"` | — |
| [SRC-F725E90B2A-L003820](../../tests/test_web_agent.py#L3820) | 3820 | `""` | — |
| [SRC-F725E90B2A-L003821](../../tests/test_web_agent.py#L3821) | 3821 | `"    assert calls  # initial research, plus bounded repair where applicable"` | — |
| [SRC-F725E90B2A-L003822](../../tests/test_web_agent.py#L3822) | 3822 | `"    assert result[\"kind\"] == \"insufficient_evidence\""` | — |
| [SRC-F725E90B2A-L003823](../../tests/test_web_agent.py#L3823) | 3823 | `"    assert result[\"sources\"] == []"` | — |
| [SRC-F725E90B2A-L003824](../../tests/test_web_agent.py#L3824) | 3824 | `"    guardrails = result[\"search_report\"][\"source_guardrails\"]"` | — |
| [SRC-F725E90B2A-L003825](../../tests/test_web_agent.py#L3825) | 3825 | `"    assert guardrails[\"initial\"][\"official_government_domain_required\"] is True"` | — |
| [SRC-F725E90B2A-L003826](../../tests/test_web_agent.py#L3826) | 3826 | `"    assert guardrails[\"initial\"][\"rejection_counts\"] == {"` | — |
| [SRC-F725E90B2A-L003827](../../tests/test_web_agent.py#L3827) | 3827 | `"        \"not_an_official_government_domain\": 1"` | — |
| [SRC-F725E90B2A-L003828](../../tests/test_web_agent.py#L3828) | 3828 | `"    }"` | — |
| [SRC-F725E90B2A-L003829](../../tests/test_web_agent.py#L3829) | 3829 | `"    assert guardrails[\"final\"][\"accepted_sources\"] == 0"` | — |
| [SRC-F725E90B2A-L003830](../../tests/test_web_agent.py#L3830) | 3830 | `"    assert result[\"search_report\"][\"usable_sources_after_filtering\"] == 0"` | — |
| [SRC-F725E90B2A-L003831](../../tests/test_web_agent.py#L3831) | 3831 | `""` | — |
| [SRC-F725E90B2A-L003832](../../tests/test_web_agent.py#L3832) | 3832 | `"def test_criterion_gap_repair_cannot_reintroduce_non_social_source(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003833](../../tests/test_web_agent.py#L3833) | 3833 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003834](../../tests/test_web_agent.py#L3834) | 3834 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L003835](../../tests/test_web_agent.py#L3835) | 3835 | `"    question = ("` | — |
| [SRC-F725E90B2A-L003836](../../tests/test_web_agent.py#L3836) | 3836 | `"        \"قارن بين خدمتين من حيث السعر والخصوصية والاعتمادية \""` | — |
| [SRC-F725E90B2A-L003837](../../tests/test_web_agent.py#L3837) | 3837 | `"        \"واعرض آراء وتجارب المستخدمين\""` | — |
| [SRC-F725E90B2A-L003838](../../tests/test_web_agent.py#L3838) | 3838 | `"    )"` | — |
| [SRC-F725E90B2A-L003839](../../tests/test_web_agent.py#L3839) | 3839 | `"    initial_sources = ["` | — |
| [SRC-F725E90B2A-L003840](../../tests/test_web_agent.py#L3840) | 3840 | `"        {"` | — |
| [SRC-F725E90B2A-L003841](../../tests/test_web_agent.py#L3841) | 3841 | `"            **sample_source(0),"` | — |
| [SRC-F725E90B2A-L003842](../../tests/test_web_agent.py#L3842) | 3842 | `"            \"url\": \"https://www.reddit.com/r/example/comments/1\","` | — |
| [SRC-F725E90B2A-L003843](../../tests/test_web_agent.py#L3843) | 3843 | `"            \"domain\": \"reddit.com\","` | — |
| [SRC-F725E90B2A-L003844](../../tests/test_web_agent.py#L3844) | 3844 | `"            \"title\": \"مناقشة تجارب المستخدمين للخدمتين\","` | — |
| [SRC-F725E90B2A-L003845](../../tests/test_web_agent.py#L3845) | 3845 | `"            \"snippet\": \"تجارب وآراء مستخدمين حول الخدمتين\","` | — |
| [SRC-F725E90B2A-L003846](../../tests/test_web_agent.py#L3846) | 3846 | `"            \"page_text\": \"تجارب وآراء مستخدمين حول الخدمتين\","` | — |
| [SRC-F725E90B2A-L003847](../../tests/test_web_agent.py#L3847) | 3847 | `"            \"platform\": \"reddit\","` | — |
| [SRC-F725E90B2A-L003848](../../tests/test_web_agent.py#L3848) | 3848 | `"            \"providers\": [\"reddit\"],"` | — |
| [SRC-F725E90B2A-L003849](../../tests/test_web_agent.py#L3849) | 3849 | `"        },"` | — |
| [SRC-F725E90B2A-L003850](../../tests/test_web_agent.py#L3850) | 3850 | `"        {"` | — |
| [SRC-F725E90B2A-L003851](../../tests/test_web_agent.py#L3851) | 3851 | `"            **sample_source(1),"` | — |
| [SRC-F725E90B2A-L003852](../../tests/test_web_agent.py#L3852) | 3852 | `"            \"url\": \"https://www.reddit.com/r/example/comments/2\","` | — |
| [SRC-F725E90B2A-L003853](../../tests/test_web_agent.py#L3853) | 3853 | `"            \"domain\": \"reddit.com\","` | — |
| [SRC-F725E90B2A-L003854](../../tests/test_web_agent.py#L3854) | 3854 | `"            \"title\": \"مناقشة أخرى عن الخدمتين\","` | — |
| [SRC-F725E90B2A-L003855](../../tests/test_web_agent.py#L3855) | 3855 | `"            \"snippet\": \"مناقشة وتجارب مستخدمين حول الخدمتين\","` | — |
| [SRC-F725E90B2A-L003856](../../tests/test_web_agent.py#L3856) | 3856 | `"            \"page_text\": \"مناقشة وتجارب مستخدمين حول الخدمتين\","` | — |
| [SRC-F725E90B2A-L003857](../../tests/test_web_agent.py#L3857) | 3857 | `"            \"platform\": \"reddit\","` | — |
| [SRC-F725E90B2A-L003858](../../tests/test_web_agent.py#L3858) | 3858 | `"            \"providers\": [\"reddit\"],"` | — |
| [SRC-F725E90B2A-L003859](../../tests/test_web_agent.py#L3859) | 3859 | `"        },"` | — |
| [SRC-F725E90B2A-L003860](../../tests/test_web_agent.py#L3860) | 3860 | `"    ]"` | — |
| [SRC-F725E90B2A-L003861](../../tests/test_web_agent.py#L3861) | 3861 | `"    repair_candidate = {"` | — |
| [SRC-F725E90B2A-L003862](../../tests/test_web_agent.py#L3862) | 3862 | `"        **sample_source(2),"` | — |
| [SRC-F725E90B2A-L003863](../../tests/test_web_agent.py#L3863) | 3863 | `"        \"url\": \"https://example.com/unrelated-repair\","` | — |
| [SRC-F725E90B2A-L003864](../../tests/test_web_agent.py#L3864) | 3864 | `"        \"domain\": \"example.com\","` | — |
| [SRC-F725E90B2A-L003865](../../tests/test_web_agent.py#L3865) | 3865 | `"        \"title\": \"معلومات عن الخدمة\","` | — |
| [SRC-F725E90B2A-L003866](../../tests/test_web_agent.py#L3866) | 3866 | `"        \"snippet\": \"معلومات عامة عن الخدمة\","` | — |
| [SRC-F725E90B2A-L003867](../../tests/test_web_agent.py#L3867) | 3867 | `"        \"page_text\": \"معلومات عامة عن الخدمة\","` | — |
| [SRC-F725E90B2A-L003868](../../tests/test_web_agent.py#L3868) | 3868 | `"        \"providers\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L003869](../../tests/test_web_agent.py#L3869) | 3869 | `"    }"` | — |
| [SRC-F725E90B2A-L003870](../../tests/test_web_agent.py#L3870) | 3870 | `"    collect_calls = []"` | — |
| [SRC-F725E90B2A-L003871](../../tests/test_web_agent.py#L3871) | 3871 | `""` | — |
| [SRC-F725E90B2A-L003872](../../tests/test_web_agent.py#L3872) | 3872 | `"    def plan(_question, _history):"` | — |
| [SRC-F725E90B2A-L003873](../../tests/test_web_agent.py#L3873) | 3873 | `"        return {"` | — |
| [SRC-F725E90B2A-L003874](../../tests/test_web_agent.py#L3874) | 3874 | `"            \"queries\": [_question],"` | — |
| [SRC-F725E90B2A-L003875](../../tests/test_web_agent.py#L3875) | 3875 | `"            \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L003876](../../tests/test_web_agent.py#L3876) | 3876 | `"            \"social_focus\": True,"` | — |
| [SRC-F725E90B2A-L003877](../../tests/test_web_agent.py#L3877) | 3877 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003878](../../tests/test_web_agent.py#L3878) | 3878 | `"            \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L003879](../../tests/test_web_agent.py#L3879) | 3879 | `"            \"platforms\": [\"reddit\"],"` | — |
| [SRC-F725E90B2A-L003880](../../tests/test_web_agent.py#L3880) | 3880 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003881](../../tests/test_web_agent.py#L3881) | 3881 | `"        }"` | — |
| [SRC-F725E90B2A-L003882](../../tests/test_web_agent.py#L3882) | 3882 | `""` | — |
| [SRC-F725E90B2A-L003883](../../tests/test_web_agent.py#L3883) | 3883 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L003884](../../tests/test_web_agent.py#L3884) | 3884 | `"        collect_calls.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L003885](../../tests/test_web_agent.py#L3885) | 3885 | `"        if len(collect_calls) == 1:"` | — |
| [SRC-F725E90B2A-L003886](../../tests/test_web_agent.py#L3886) | 3886 | `"            sources = initial_sources"` | — |
| [SRC-F725E90B2A-L003887](../../tests/test_web_agent.py#L3887) | 3887 | `"        else:"` | — |
| [SRC-F725E90B2A-L003888](../../tests/test_web_agent.py#L3888) | 3888 | `"            sources = [repair_candidate]"` | — |
| [SRC-F725E90B2A-L003889](../../tests/test_web_agent.py#L3889) | 3889 | `"        return sources, [], {"` | — |
| [SRC-F725E90B2A-L003890](../../tests/test_web_agent.py#L3890) | 3890 | `"            \"queries_planned\": len(research_plan.get(\"queries\", [])),"` | — |
| [SRC-F725E90B2A-L003891](../../tests/test_web_agent.py#L3891) | 3891 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L003892](../../tests/test_web_agent.py#L3892) | 3892 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L003893](../../tests/test_web_agent.py#L3893) | 3893 | `"            \"unique_sources\": len(sources),"` | — |
| [SRC-F725E90B2A-L003894](../../tests/test_web_agent.py#L3894) | 3894 | `"            \"pages_fetched\": len(sources),"` | — |
| [SRC-F725E90B2A-L003895](../../tests/test_web_agent.py#L3895) | 3895 | `"            \"providers_used\": [\"reddit\"] if len(collect_calls) == 1 else [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L003896](../../tests/test_web_agent.py#L3896) | 3896 | `"            \"provider_counts\": {},"` | — |
| [SRC-F725E90B2A-L003897](../../tests/test_web_agent.py#L3897) | 3897 | `"            \"platform_counts\": {},"` | — |
| [SRC-F725E90B2A-L003898](../../tests/test_web_agent.py#L3898) | 3898 | `"            \"social_direct_results\": len(sources) if len(collect_calls) == 1 else 0,"` | — |
| [SRC-F725E90B2A-L003899](../../tests/test_web_agent.py#L3899) | 3899 | `"            \"depth\": research_plan.get(\"depth\", \"deep\"),"` | — |
| [SRC-F725E90B2A-L003900](../../tests/test_web_agent.py#L3900) | 3900 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003901](../../tests/test_web_agent.py#L3901) | 3901 | `"        }"` | — |
| [SRC-F725E90B2A-L003902](../../tests/test_web_agent.py#L3902) | 3902 | `""` | — |
| [SRC-F725E90B2A-L003903](../../tests/test_web_agent.py#L3903) | 3903 | `"    monkeypatch.setattr(agent, \"_plan_search\", plan)"` | — |
| [SRC-F725E90B2A-L003904](../../tests/test_web_agent.py#L3904) | 3904 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L003905](../../tests/test_web_agent.py#L3905) | 3905 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda _query, _source: True)"` | — |
| [SRC-F725E90B2A-L003906](../../tests/test_web_agent.py#L3906) | 3906 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003907](../../tests/test_web_agent.py#L3907) | 3907 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003908](../../tests/test_web_agent.py#L3908) | 3908 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L003909](../../tests/test_web_agent.py#L3909) | 3909 | `"        lambda *args, **kwargs: ("` | — |
| [SRC-F725E90B2A-L003910](../../tests/test_web_agent.py#L3910) | 3910 | `"            \"السعر مناسب [المصدر 1]. الخصوصية جيدة [المصدر 2]. \""` | — |
| [SRC-F725E90B2A-L003911](../../tests/test_web_agent.py#L3911) | 3911 | `"            \"الاعتمادية مناسبة [المصدر 1].\""` | — |
| [SRC-F725E90B2A-L003912](../../tests/test_web_agent.py#L3912) | 3912 | `"        ),"` | — |
| [SRC-F725E90B2A-L003913](../../tests/test_web_agent.py#L3913) | 3913 | `"    )"` | — |
| [SRC-F725E90B2A-L003914](../../tests/test_web_agent.py#L3914) | 3914 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003915](../../tests/test_web_agent.py#L3915) | 3915 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003916](../../tests/test_web_agent.py#L3916) | 3916 | `"        \"_review_answer\","` | — |
| [SRC-F725E90B2A-L003917](../../tests/test_web_agent.py#L3917) | 3917 | `"        lambda _question, answer, _sources: answer,"` | — |
| [SRC-F725E90B2A-L003918](../../tests/test_web_agent.py#L3918) | 3918 | `"    )"` | — |
| [SRC-F725E90B2A-L003919](../../tests/test_web_agent.py#L3919) | 3919 | `""` | — |
| [SRC-F725E90B2A-L003920](../../tests/test_web_agent.py#L3920) | 3920 | `"    result = agent.answer(question, mode=\"social\")"` | — |
| [SRC-F725E90B2A-L003921](../../tests/test_web_agent.py#L3921) | 3921 | `"    report = result[\"search_report\"]"` | — |
| [SRC-F725E90B2A-L003922](../../tests/test_web_agent.py#L3922) | 3922 | `"    repair_guardrails = report[\"source_guardrails\"][\"criterion_gap_repair\"]"` | — |
| [SRC-F725E90B2A-L003923](../../tests/test_web_agent.py#L3923) | 3923 | `""` | — |
| [SRC-F725E90B2A-L003924](../../tests/test_web_agent.py#L3924) | 3924 | `"    assert len(collect_calls) >= 2"` | — |
| [SRC-F725E90B2A-L003925](../../tests/test_web_agent.py#L3925) | 3925 | `"    assert repair_guardrails[\"rejected_sources\"] >= 1"` | — |
| [SRC-F725E90B2A-L003926](../../tests/test_web_agent.py#L3926) | 3926 | `"    assert repair_guardrails[\"rejection_counts\"][\"not_a_social_platform_source\"] >= 1"` | — |
| [SRC-F725E90B2A-L003927](../../tests/test_web_agent.py#L3927) | 3927 | `"    assert all(\"reddit.com\" in source[\"url\"] for source in result[\"sources\"])"` | — |
| [SRC-F725E90B2A-L003928](../../tests/test_web_agent.py#L3928) | 3928 | `"    assert \"https://example.com/unrelated-repair\" not in {"` | — |
| [SRC-F725E90B2A-L003929](../../tests/test_web_agent.py#L3929) | 3929 | `"        source[\"url\"] for source in result[\"sources\"]"` | — |
| [SRC-F725E90B2A-L003930](../../tests/test_web_agent.py#L3930) | 3930 | `"    }"` | — |
| [SRC-F725E90B2A-L003931](../../tests/test_web_agent.py#L3931) | 3931 | `""` | — |
| [SRC-F725E90B2A-L003932](../../tests/test_web_agent.py#L3932) | 3932 | `"def test_local_answer_exposes_task_spec_without_claiming_search(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003933](../../tests/test_web_agent.py#L3933) | 3933 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003934](../../tests/test_web_agent.py#L3934) | 3934 | `"    result = agent.answer(\"أهلا\")"` | — |
| [SRC-F725E90B2A-L003935](../../tests/test_web_agent.py#L3935) | 3935 | `""` | — |
| [SRC-F725E90B2A-L003936](../../tests/test_web_agent.py#L3936) | 3936 | `"    task_understanding = result[\"task_understanding\"]"` | — |
| [SRC-F725E90B2A-L003937](../../tests/test_web_agent.py#L3937) | 3937 | `"    assert task_understanding[\"task_spec\"][\"schema\"] == \"omarai.task_spec.v1\""` | — |
| [SRC-F725E90B2A-L003938](../../tests/test_web_agent.py#L3938) | 3938 | `"    assert task_understanding[\"tool_execution\"][\"search_outcome\"] == \"not_assessed\""` | — |
| [SRC-F725E90B2A-L003939](../../tests/test_web_agent.py#L3939) | 3939 | `"    assert task_understanding[\"tool_execution\"][\"required_tools\"] == []"` | — |
| [SRC-F725E90B2A-L003940](../../tests/test_web_agent.py#L3940) | 3940 | `"    assert all("` | — |
| [SRC-F725E90B2A-L003941](../../tests/test_web_agent.py#L3941) | 3941 | `"        row[\"status\"] == \"not_required\""` | — |
| [SRC-F725E90B2A-L003942](../../tests/test_web_agent.py#L3942) | 3942 | `"        for row in task_understanding[\"tool_execution\"][\"tool_status_matrix\"]"` | — |
| [SRC-F725E90B2A-L003943](../../tests/test_web_agent.py#L3943) | 3943 | `"    )"` | — |
| [SRC-F725E90B2A-L003944](../../tests/test_web_agent.py#L3944) | 3944 | `"    assert task_understanding[\"actual_queries\"] == []"` | — |
| [SRC-F725E90B2A-L003945](../../tests/test_web_agent.py#L3945) | 3945 | `"    assert task_understanding[\"query_strategy_matrix\"] == []"` | — |
| [SRC-F725E90B2A-L003946](../../tests/test_web_agent.py#L3946) | 3946 | `"    assert task_understanding[\"search_was_attempted\"] is False"` | — |
| [SRC-F725E90B2A-L003947](../../tests/test_web_agent.py#L3947) | 3947 | `""` | — |
| [SRC-F725E90B2A-L003948](../../tests/test_web_agent.py#L3948) | 3948 | `"def test_official_site_without_target_clarifies_before_planning_or_search(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003949](../../tests/test_web_agent.py#L3949) | 3949 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003950](../../tests/test_web_agent.py#L3950) | 3950 | `""` | — |
| [SRC-F725E90B2A-L003951](../../tests/test_web_agent.py#L3951) | 3951 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003952](../../tests/test_web_agent.py#L3952) | 3952 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003953](../../tests/test_web_agent.py#L3953) | 3953 | `"        \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003954](../../tests/test_web_agent.py#L3954) | 3954 | `"        lambda *args, **kwargs: pytest.fail(\"Missing official-site target must be clarified before planning\"),"` | — |
| [SRC-F725E90B2A-L003955](../../tests/test_web_agent.py#L3955) | 3955 | `"    )"` | — |
| [SRC-F725E90B2A-L003956](../../tests/test_web_agent.py#L3956) | 3956 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003957](../../tests/test_web_agent.py#L3957) | 3957 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003958](../../tests/test_web_agent.py#L3958) | 3958 | `"        \"_collect_research\","` | — |
| [SRC-F725E90B2A-L003959](../../tests/test_web_agent.py#L3959) | 3959 | `"        lambda *args, **kwargs: pytest.fail(\"Missing official-site target must not invoke search\"),"` | — |
| [SRC-F725E90B2A-L003960](../../tests/test_web_agent.py#L3960) | 3960 | `"    )"` | — |
| [SRC-F725E90B2A-L003961](../../tests/test_web_agent.py#L3961) | 3961 | `""` | — |
| [SRC-F725E90B2A-L003962](../../tests/test_web_agent.py#L3962) | 3962 | `"    result = agent.answer(\"هات الموقع الرسمي\")"` | — |
| [SRC-F725E90B2A-L003963](../../tests/test_web_agent.py#L3963) | 3963 | `""` | — |
| [SRC-F725E90B2A-L003964](../../tests/test_web_agent.py#L3964) | 3964 | `"    assert result[\"intent_route\"] == \"CLARIFY\""` | — |
| [SRC-F725E90B2A-L003965](../../tests/test_web_agent.py#L3965) | 3965 | `"    assert result[\"kind\"] == \"clarification_needed\""` | — |
| [SRC-F725E90B2A-L003966](../../tests/test_web_agent.py#L3966) | 3966 | `"    assert \"اسم الجهة أو الشركة\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L003967](../../tests/test_web_agent.py#L3967) | 3967 | `"    assert result[\"search_attempted\"] is False"` | — |
| [SRC-F725E90B2A-L003968](../../tests/test_web_agent.py#L3968) | 3968 | `"    assert \"official_destination_target_entity\" in result[\"task_understanding\"][\"task_spec\"][\"missing_required_inputs\"]"` | — |
| [SRC-F725E90B2A-L003969](../../tests/test_web_agent.py#L3969) | 3969 | `""` | — |
| [SRC-F725E90B2A-L003970](../../tests/test_web_agent.py#L3970) | 3970 | `"def test_summary_without_source_clarifies_before_search(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003971](../../tests/test_web_agent.py#L3971) | 3971 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003972](../../tests/test_web_agent.py#L3972) | 3972 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003973](../../tests/test_web_agent.py#L3973) | 3973 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003974](../../tests/test_web_agent.py#L3974) | 3974 | `"        \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003975](../../tests/test_web_agent.py#L3975) | 3975 | `"        lambda *args, **kwargs: pytest.fail(\"Missing summary source must be clarified before planning\"),"` | — |
| [SRC-F725E90B2A-L003976](../../tests/test_web_agent.py#L3976) | 3976 | `"    )"` | — |
| [SRC-F725E90B2A-L003977](../../tests/test_web_agent.py#L3977) | 3977 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003978](../../tests/test_web_agent.py#L3978) | 3978 | `"        agent,"` | — |
| [SRC-F725E90B2A-L003979](../../tests/test_web_agent.py#L3979) | 3979 | `"        \"_collect_research\","` | — |
| [SRC-F725E90B2A-L003980](../../tests/test_web_agent.py#L3980) | 3980 | `"        lambda *args, **kwargs: pytest.fail(\"Missing summary source must not invoke search\"),"` | — |
| [SRC-F725E90B2A-L003981](../../tests/test_web_agent.py#L3981) | 3981 | `"    )"` | — |
| [SRC-F725E90B2A-L003982](../../tests/test_web_agent.py#L3982) | 3982 | `""` | — |
| [SRC-F725E90B2A-L003983](../../tests/test_web_agent.py#L3983) | 3983 | `"    result = agent.answer(\"لخص\")"` | — |
| [SRC-F725E90B2A-L003984](../../tests/test_web_agent.py#L3984) | 3984 | `""` | — |
| [SRC-F725E90B2A-L003985](../../tests/test_web_agent.py#L3985) | 3985 | `"    assert result[\"intent_route\"] == \"CLARIFY\""` | — |
| [SRC-F725E90B2A-L003986](../../tests/test_web_agent.py#L3986) | 3986 | `"    assert \"أرسل النص\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L003987](../../tests/test_web_agent.py#L3987) | 3987 | `"    assert result[\"search_attempted\"] is False"` | — |
| [SRC-F725E90B2A-L003988](../../tests/test_web_agent.py#L3988) | 3988 | `"    assert \"summary_source_url_or_pasted_text\" in result[\"task_understanding\"][\"task_spec\"][\"missing_required_inputs\"]"` | — |
| [SRC-F725E90B2A-L003989](../../tests/test_web_agent.py#L3989) | 3989 | `""` | — |
| [SRC-F725E90B2A-L003990](../../tests/test_web_agent.py#L3990) | 3990 | `"def test_task_spec_controls_generation_context_without_becoming_evidence(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003991](../../tests/test_web_agent.py#L3991) | 3991 | `"    from agents.task_understanding import build_query_strategy_matrix, build_task_spec"` | — |
| [SRC-F725E90B2A-L003992](../../tests/test_web_agent.py#L3992) | 3992 | `""` | — |
| [SRC-F725E90B2A-L003993](../../tests/test_web_agent.py#L3993) | 3993 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003994](../../tests/test_web_agent.py#L3994) | 3994 | `"    captured = {}"` | — |
| [SRC-F725E90B2A-L003995](../../tests/test_web_agent.py#L3995) | 3995 | `""` | — |
| [SRC-F725E90B2A-L003996](../../tests/test_web_agent.py#L3996) | 3996 | `"    question = ("` | — |
| [SRC-F725E90B2A-L003997](../../tests/test_web_agent.py#L3997) | 3997 | `"        \"قارن السيارات الكهربائية في مصر من حيث السعر والضمان، \""` | — |
| [SRC-F725E90B2A-L003998](../../tests/test_web_agent.py#L3998) | 3998 | `"        \"اشرح ببساطة مع أمثلة وروابط مباشرة\""` | — |
| [SRC-F725E90B2A-L003999](../../tests/test_web_agent.py#L3999) | 3999 | `"    )"` | — |
| [SRC-F725E90B2A-L004000](../../tests/test_web_agent.py#L4000) | 4000 | `"    task_spec = build_task_spec("` | — |
| [SRC-F725E90B2A-L004001](../../tests/test_web_agent.py#L4001) | 4001 | `"        question,"` | — |
| [SRC-F725E90B2A-L004002](../../tests/test_web_agent.py#L4002) | 4002 | `"        mode=\"deep\","` | — |
| [SRC-F725E90B2A-L004003](../../tests/test_web_agent.py#L4003) | 4003 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-F725E90B2A-L004004](../../tests/test_web_agent.py#L4004) | 4004 | `"    )"` | — |
| [SRC-F725E90B2A-L004005](../../tests/test_web_agent.py#L4005) | 4005 | `"    initial_queries = [compact_search_query(question)]"` | — |
| [SRC-F725E90B2A-L004006](../../tests/test_web_agent.py#L4006) | 4006 | `"    matrix = build_query_strategy_matrix("` | — |
| [SRC-F725E90B2A-L004007](../../tests/test_web_agent.py#L4007) | 4007 | `"        question,"` | — |
| [SRC-F725E90B2A-L004008](../../tests/test_web_agent.py#L4008) | 4008 | `"        task_spec,"` | — |
| [SRC-F725E90B2A-L004009](../../tests/test_web_agent.py#L4009) | 4009 | `"        initial_queries,"` | — |
| [SRC-F725E90B2A-L004010](../../tests/test_web_agent.py#L4010) | 4010 | `"        limit=4,"` | — |
| [SRC-F725E90B2A-L004011](../../tests/test_web_agent.py#L4011) | 4011 | `"        compact_fn=compact_search_query,"` | — |
| [SRC-F725E90B2A-L004012](../../tests/test_web_agent.py#L4012) | 4012 | `"    )"` | — |
| [SRC-F725E90B2A-L004013](../../tests/test_web_agent.py#L4013) | 4013 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L004014](../../tests/test_web_agent.py#L4014) | 4014 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L004015](../../tests/test_web_agent.py#L4015) | 4015 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L004016](../../tests/test_web_agent.py#L4016) | 4016 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L004017](../../tests/test_web_agent.py#L4017) | 4017 | `"        \"queries\": [row[\"query\"] for row in matrix],"` | — |
| [SRC-F725E90B2A-L004018](../../tests/test_web_agent.py#L4018) | 4018 | `"        \"dialogue_context\": {},"` | — |
| [SRC-F725E90B2A-L004019](../../tests/test_web_agent.py#L4019) | 4019 | `"        \"intent_route\": \"WEB_DEEP\","` | — |
| [SRC-F725E90B2A-L004020](../../tests/test_web_agent.py#L4020) | 4020 | `"        \"task_spec\": task_spec,"` | — |
| [SRC-F725E90B2A-L004021](../../tests/test_web_agent.py#L4021) | 4021 | `"        \"query_strategy_matrix\": matrix,"` | — |
| [SRC-F725E90B2A-L004022](../../tests/test_web_agent.py#L4022) | 4022 | `"    }"` | — |
| [SRC-F725E90B2A-L004023](../../tests/test_web_agent.py#L4023) | 4023 | `""` | — |
| [SRC-F725E90B2A-L004024](../../tests/test_web_agent.py#L4024) | 4024 | `"    def fake_completion(messages, **kwargs):"` | — |
| [SRC-F725E90B2A-L004025](../../tests/test_web_agent.py#L4025) | 4025 | `"        captured[\"messages\"] = messages"` | — |
| [SRC-F725E90B2A-L004026](../../tests/test_web_agent.py#L4026) | 4026 | `"        captured[\"kwargs\"] = kwargs"` | — |
| [SRC-F725E90B2A-L004027](../../tests/test_web_agent.py#L4027) | 4027 | `"        return \"إجابة اختبارية مرتبطة بالأدلة.\""` | — |
| [SRC-F725E90B2A-L004028](../../tests/test_web_agent.py#L4028) | 4028 | `""` | — |
| [SRC-F725E90B2A-L004029](../../tests/test_web_agent.py#L4029) | 4029 | `"    monkeypatch.setattr(agent, \"_request_completion\", fake_completion)"` | — |
| [SRC-F725E90B2A-L004030](../../tests/test_web_agent.py#L4030) | 4030 | `""` | — |
| [SRC-F725E90B2A-L004031](../../tests/test_web_agent.py#L4031) | 4031 | `"    answer = agent._generate("` | — |
| [SRC-F725E90B2A-L004032](../../tests/test_web_agent.py#L4032) | 4032 | `"        question,"` | — |
| [SRC-F725E90B2A-L004033](../../tests/test_web_agent.py#L4033) | 4033 | `"        [],"` | — |
| [SRC-F725E90B2A-L004034](../../tests/test_web_agent.py#L4034) | 4034 | `"        [sample_source(0)],"` | — |
| [SRC-F725E90B2A-L004035](../../tests/test_web_agent.py#L4035) | 4035 | `"        None,"` | — |
| [SRC-F725E90B2A-L004036](../../tests/test_web_agent.py#L4036) | 4036 | `"        research_plan=plan,"` | — |
| [SRC-F725E90B2A-L004037](../../tests/test_web_agent.py#L4037) | 4037 | `"        search_report={"` | — |
| [SRC-F725E90B2A-L004038](../../tests/test_web_agent.py#L4038) | 4038 | `"            \"queries_planned\": len(plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L004039](../../tests/test_web_agent.py#L4039) | 4039 | `"            \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L004040](../../tests/test_web_agent.py#L4040) | 4040 | `"            \"pages_fetched\": 1,"` | — |
| [SRC-F725E90B2A-L004041](../../tests/test_web_agent.py#L4041) | 4041 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L004042](../../tests/test_web_agent.py#L4042) | 4042 | `"        },"` | — |
| [SRC-F725E90B2A-L004043](../../tests/test_web_agent.py#L4043) | 4043 | `"    )"` | — |
| [SRC-F725E90B2A-L004044](../../tests/test_web_agent.py#L4044) | 4044 | `""` | — |
| [SRC-F725E90B2A-L004045](../../tests/test_web_agent.py#L4045) | 4045 | `"    prompt = \"\\n\".join("` | — |
| [SRC-F725E90B2A-L004046](../../tests/test_web_agent.py#L4046) | 4046 | `"        message.get(\"content\", \"\")"` | — |
| [SRC-F725E90B2A-L004047](../../tests/test_web_agent.py#L4047) | 4047 | `"        for message in captured[\"messages\"]"` | — |
| [SRC-F725E90B2A-L004048](../../tests/test_web_agent.py#L4048) | 4048 | `"        if isinstance(message, dict)"` | — |
| [SRC-F725E90B2A-L004049](../../tests/test_web_agent.py#L4049) | 4049 | `"    )"` | — |
| [SRC-F725E90B2A-L004050](../../tests/test_web_agent.py#L4050) | 4050 | `"    assert answer == \"إجابة اختبارية مرتبطة بالأدلة.\""` | — |
| [SRC-F725E90B2A-L004051](../../tests/test_web_agent.py#L4051) | 4051 | `"    assert \"task_planning_context\" in prompt"` | — |
| [SRC-F725E90B2A-L004052](../../tests/test_web_agent.py#L4052) | 4052 | `"    assert \"explicit_aspects\" in prompt"` | — |
| [SRC-F725E90B2A-L004053](../../tests/test_web_agent.py#L4053) | 4053 | `"    assert \"output_preferences\" in prompt"` | — |
| [SRC-F725E90B2A-L004054](../../tests/test_web_agent.py#L4054) | 4054 | `"    assert \"beginner_friendly_requested\" in prompt"` | — |
| [SRC-F725E90B2A-L004055](../../tests/test_web_agent.py#L4055) | 4055 | `"    assert \"reasoning_guidance\" in prompt"` | — |
| [SRC-F725E90B2A-L004056](../../tests/test_web_agent.py#L4056) | 4056 | `"    assert \"decision_matrix\" in prompt"` | — |
| [SRC-F725E90B2A-L004057](../../tests/test_web_agent.py#L4057) | 4057 | `"    assert \"قسّم المقارنة إلى كل معيار صريح\" in prompt"` | — |
| [SRC-F725E90B2A-L004058](../../tests/test_web_agent.py#L4058) | 4058 | `"    assert \"وحّد العملة والوحدات\" in prompt"` | — |
| [SRC-F725E90B2A-L004059](../../tests/test_web_agent.py#L4059) | 4059 | `"    assert \"query_strategy_matrix\" in prompt"` | — |
| [SRC-F725E90B2A-L004060](../../tests/test_web_agent.py#L4060) | 4060 | `"    assert \"الأولوية لكلام المستخدم الحالي\" in prompt"` | — |
| [SRC-F725E90B2A-L004061](../../tests/test_web_agent.py#L4061) | 4061 | `"    assert \"الاستعلامات المخططة فقط\" in prompt"` | — |
| [SRC-F725E90B2A-L004062](../../tests/test_web_agent.py#L4062) | 4062 | `""` | — |
| [SRC-F725E90B2A-L004063](../../tests/test_web_agent.py#L4063) | 4063 | `"def test_bilingual_relevance_handles_arabic_attached_clitics_without_lowering_floor():"` | — |
| [SRC-F725E90B2A-L004064](../../tests/test_web_agent.py#L4064) | 4064 | `"    query = \"أهم استخدامات الذكاء الاصطناعي للشركات الصغيرة؟\""` | — |
| [SRC-F725E90B2A-L004065](../../tests/test_web_agent.py#L4065) | 4065 | `"    evidence = \"AI use cases for small businesses\""` | — |
| [SRC-F725E90B2A-L004066](../../tests/test_web_agent.py#L4066) | 4066 | `"    assert _minimum_relevance_ratio(query) == 0.20"` | — |
| [SRC-F725E90B2A-L004067](../../tests/test_web_agent.py#L4067) | 4067 | `"    assert _relevance_ratio(query, evidence) >= 0.80"` | — |
| [SRC-F725E90B2A-L004068](../../tests/test_web_agent.py#L4068) | 4068 | `""` | — |
| [SRC-F725E90B2A-L004069](../../tests/test_web_agent.py#L4069) | 4069 | `"def test_search_evidence_matching_keeps_distinct_concepts_as_the_ratio_denominator():"` | — |
| [SRC-F725E90B2A-L004070](../../tests/test_web_agent.py#L4070) | 4070 | `"    query = \"استخدامات الذكاء الاصطناعي للشركات الصغيرة\""` | — |
| [SRC-F725E90B2A-L004071](../../tests/test_web_agent.py#L4071) | 4071 | `"    on_topic = \"AI use cases for small businesses\""` | — |
| [SRC-F725E90B2A-L004072](../../tests/test_web_agent.py#L4072) | 4072 | `"    weak = \"AI tools for personal photo editing\""` | — |
| [SRC-F725E90B2A-L004073](../../tests/test_web_agent.py#L4073) | 4073 | `"    assert _relevance_ratio(query, on_topic) > _relevance_ratio(query, weak)"` | — |
| [SRC-F725E90B2A-L004074](../../tests/test_web_agent.py#L4074) | 4074 | `"    assert _relevance_ratio(query, weak) < _minimum_relevance_ratio(query)"` | — |
| [SRC-F725E90B2A-L004075](../../tests/test_web_agent.py#L4075) | 4075 | `""` | — |
| [SRC-F725E90B2A-L004076](../../tests/test_web_agent.py#L4076) | 4076 | `"def test_bilingual_relevance_matches_english_queries_to_arabic_source_text():"` | — |
| [SRC-F725E90B2A-L004077](../../tests/test_web_agent.py#L4077) | 4077 | `"    query = \"AI use cases for small businesses in Egypt\""` | — |
| [SRC-F725E90B2A-L004078](../../tests/test_web_agent.py#L4078) | 4078 | `"    evidence = \"استخدامات الذكاء الاصطناعي للشركات الصغيرة في مصر\""` | — |
| [SRC-F725E90B2A-L004079](../../tests/test_web_agent.py#L4079) | 4079 | `"    assert _relevance_ratio(query, evidence) >= 0.80"` | — |
| [SRC-F725E90B2A-L004080](../../tests/test_web_agent.py#L4080) | 4080 | `""` | — |
| [SRC-F725E90B2A-L004081](../../tests/test_web_agent.py#L4081) | 4081 | `""` | — |
| [SRC-F725E90B2A-L004082](../../tests/test_web_agent.py#L4082) | 4082 | `"def test_completion_diagnostics_failure_does_not_break_answer(monkeypatch):"` | — |
| [SRC-F725E90B2A-L004083](../../tests/test_web_agent.py#L4083) | 4083 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L004084](../../tests/test_web_agent.py#L4084) | 4084 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L004085](../../tests/test_web_agent.py#L4085) | 4085 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L004086](../../tests/test_web_agent.py#L4086) | 4086 | `"        agent,"` | — |
| [SRC-F725E90B2A-L004087](../../tests/test_web_agent.py#L4087) | 4087 | `"        \"_plan_search\","` | — |
| [SRC-F725E90B2A-L004088](../../tests/test_web_agent.py#L4088) | 4088 | `"        lambda question, history: {"` | — |
| [SRC-F725E90B2A-L004089](../../tests/test_web_agent.py#L4089) | 4089 | `"            \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L004090](../../tests/test_web_agent.py#L4090) | 4090 | `"            \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L004091](../../tests/test_web_agent.py#L4091) | 4091 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L004092](../../tests/test_web_agent.py#L4092) | 4092 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L004093](../../tests/test_web_agent.py#L4093) | 4093 | `"            \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L004094](../../tests/test_web_agent.py#L4094) | 4094 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L004095](../../tests/test_web_agent.py#L4095) | 4095 | `"            \"coverage_targets\": [],"` | — |
| [SRC-F725E90B2A-L004096](../../tests/test_web_agent.py#L4096) | 4096 | `"        },"` | — |
| [SRC-F725E90B2A-L004097](../../tests/test_web_agent.py#L4097) | 4097 | `"    )"` | — |
| [SRC-F725E90B2A-L004098](../../tests/test_web_agent.py#L4098) | 4098 | `"    monkeypatch.setattr(agent, \"_collect_research\", lambda plan: ("` | — |
| [SRC-F725E90B2A-L004099](../../tests/test_web_agent.py#L4099) | 4099 | `"        [sample_source(0), sample_source(1)], [], {"` | — |
| [SRC-F725E90B2A-L004100](../../tests/test_web_agent.py#L4100) | 4100 | `"            \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L004101](../../tests/test_web_agent.py#L4101) | 4101 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L004102](../../tests/test_web_agent.py#L4102) | 4102 | `"            \"query_results\": [{\"query\": plan[\"queries\"][0], \"results\": 2}],"` | — |
| [SRC-F725E90B2A-L004103](../../tests/test_web_agent.py#L4103) | 4103 | `"            \"unique_sources\": 2,"` | — |
| [SRC-F725E90B2A-L004104](../../tests/test_web_agent.py#L4104) | 4104 | `"            \"pages_fetched\": 2,"` | — |
| [SRC-F725E90B2A-L004105](../../tests/test_web_agent.py#L4105) | 4105 | `"            \"providers_used\": [\"test\"],"` | — |
| [SRC-F725E90B2A-L004106](../../tests/test_web_agent.py#L4106) | 4106 | `"            \"provider_diagnostics\": [],"` | — |
| [SRC-F725E90B2A-L004107](../../tests/test_web_agent.py#L4107) | 4107 | `"        }"` | — |
| [SRC-F725E90B2A-L004108](../../tests/test_web_agent.py#L4108) | 4108 | `"    ))"` | — |
| [SRC-F725E90B2A-L004109](../../tests/test_web_agent.py#L4109) | 4109 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L004110](../../tests/test_web_agent.py#L4110) | 4110 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L004111](../../tests/test_web_agent.py#L4111) | 4111 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"إجابة اختبارية [المصدر 1].\")"` | — |
| [SRC-F725E90B2A-L004112](../../tests/test_web_agent.py#L4112) | 4112 | `""` | — |
| [SRC-F725E90B2A-L004113](../../tests/test_web_agent.py#L4113) | 4113 | `"    def fail_diagnostics(_result):"` | — |
| [SRC-F725E90B2A-L004114](../../tests/test_web_agent.py#L4114) | 4114 | `"        raise RuntimeError(\"diagnostics are optional\")"` | — |
| [SRC-F725E90B2A-L004115](../../tests/test_web_agent.py#L4115) | 4115 | `""` | — |
| [SRC-F725E90B2A-L004116](../../tests/test_web_agent.py#L4116) | 4116 | `"    monkeypatch.setattr(\"agents.web_agent.build_research_completion\", fail_diagnostics)"` | — |
| [SRC-F725E90B2A-L004117](../../tests/test_web_agent.py#L4117) | 4117 | `"    result = agent.answer(\"قارن هذه التقنية\")"` | — |
| [SRC-F725E90B2A-L004118](../../tests/test_web_agent.py#L4118) | 4118 | `"    assert result[\"answer\"] == \"إجابة اختبارية [المصدر 1].\""` | — |
| [SRC-F725E90B2A-L004119](../../tests/test_web_agent.py#L4119) | 4119 | `"    assert result[\"research_completion\"][\"status\"] == \"diagnostics_not_computed\""` | — |
| [SRC-F725E90B2A-L004120](../../tests/test_web_agent.py#L4120) | 4120 | `"    assert any(\"لا يُعد ذلك دليلًا على اكتمال البحث\" in warning for warning in result[\"warnings\"])"` | — |
| [SRC-F725E90B2A-L004121](../../tests/test_web_agent.py#L4121) | 4121 | `""` | — |
| [SRC-F725E90B2A-L004122](../../tests/test_web_agent.py#L4122) | 4122 | `""` | — |
| [SRC-F725E90B2A-L004123](../../tests/test_web_agent.py#L4123) | 4123 | `""` | — |
| [SRC-F725E90B2A-L004124](../../tests/test_web_agent.py#L4124) | 4124 | `"def test_model_request_transport_disables_automatic_redirects(monkeypatch):"` | — |
| [SRC-F725E90B2A-L004125](../../tests/test_web_agent.py#L4125) | 4125 | `"    from agents import web_agent"` | — |
| [SRC-F725E90B2A-L004126](../../tests/test_web_agent.py#L4126) | 4126 | `""` | — |
| [SRC-F725E90B2A-L004127](../../tests/test_web_agent.py#L4127) | 4127 | `"    observed = {}"` | — |
| [SRC-F725E90B2A-L004128](../../tests/test_web_agent.py#L4128) | 4128 | `"    sentinel = object()"` | — |
| [SRC-F725E90B2A-L004129](../../tests/test_web_agent.py#L4129) | 4129 | `""` | — |
| [SRC-F725E90B2A-L004130](../../tests/test_web_agent.py#L4130) | 4130 | `"    class FakeOpener:"` | — |
| [SRC-F725E90B2A-L004131](../../tests/test_web_agent.py#L4131) | 4131 | `"        def open(self, request, *, timeout):"` | — |
| [SRC-F725E90B2A-L004132](../../tests/test_web_agent.py#L4132) | 4132 | `"            observed[\"request\"] = request"` | — |
| [SRC-F725E90B2A-L004133](../../tests/test_web_agent.py#L4133) | 4133 | `"            observed[\"timeout\"] = timeout"` | — |
| [SRC-F725E90B2A-L004134](../../tests/test_web_agent.py#L4134) | 4134 | `"            return sentinel"` | — |
| [SRC-F725E90B2A-L004135](../../tests/test_web_agent.py#L4135) | 4135 | `""` | — |
| [SRC-F725E90B2A-L004136](../../tests/test_web_agent.py#L4136) | 4136 | `"    def fake_build_opener(*handlers):"` | — |
| [SRC-F725E90B2A-L004137](../../tests/test_web_agent.py#L4137) | 4137 | `"        observed[\"handlers\"] = handlers"` | — |
| [SRC-F725E90B2A-L004138](../../tests/test_web_agent.py#L4138) | 4138 | `"        return FakeOpener()"` | — |
| [SRC-F725E90B2A-L004139](../../tests/test_web_agent.py#L4139) | 4139 | `""` | — |
| [SRC-F725E90B2A-L004140](../../tests/test_web_agent.py#L4140) | 4140 | `"    monkeypatch.setattr(web_agent.urllib.request, \"build_opener\", fake_build_opener)"` | — |
| [SRC-F725E90B2A-L004141](../../tests/test_web_agent.py#L4141) | 4141 | `"    request = web_agent.urllib.request.Request("` | — |
| [SRC-F725E90B2A-L004142](../../tests/test_web_agent.py#L4142) | 4142 | `"        \"https://provider.example/v1/chat/completions\","` | — |
| [SRC-F725E90B2A-L004143](../../tests/test_web_agent.py#L4143) | 4143 | `"        data=b\"{}\","` | — |
| [SRC-F725E90B2A-L004144](../../tests/test_web_agent.py#L4144) | 4144 | `"        headers={\"Authorization\": \"Bearer test-only-token\"},"` | — |
| [SRC-F725E90B2A-L004145](../../tests/test_web_agent.py#L4145) | 4145 | `"        method=\"POST\","` | — |
| [SRC-F725E90B2A-L004146](../../tests/test_web_agent.py#L4146) | 4146 | `"    )"` | — |
| [SRC-F725E90B2A-L004147](../../tests/test_web_agent.py#L4147) | 4147 | `""` | — |
| [SRC-F725E90B2A-L004148](../../tests/test_web_agent.py#L4148) | 4148 | `"    assert web_agent._open_model_request(request, timeout=3.5) is sentinel"` | — |
| [SRC-F725E90B2A-L004149](../../tests/test_web_agent.py#L4149) | 4149 | `"    assert observed[\"request\"] is request"` | — |
| [SRC-F725E90B2A-L004150](../../tests/test_web_agent.py#L4150) | 4150 | `"    assert observed[\"timeout\"] == 3.5"` | — |
| [SRC-F725E90B2A-L004151](../../tests/test_web_agent.py#L4151) | 4151 | `"    assert observed[\"handlers\"] == (web_agent._NoRedirectHandler,)"` | — |
| [SRC-F725E90B2A-L004152](../../tests/test_web_agent.py#L4152) | 4152 | `""` | — |
| [SRC-F725E90B2A-L004153](../../tests/test_web_agent.py#L4153) | 4153 | `"    handler = web_agent._NoRedirectHandler()"` | — |
| [SRC-F725E90B2A-L004154](../../tests/test_web_agent.py#L4154) | 4154 | `"    redirected = handler.redirect_request("` | — |
| [SRC-F725E90B2A-L004155](../../tests/test_web_agent.py#L4155) | 4155 | `"        request,"` | — |
| [SRC-F725E90B2A-L004156](../../tests/test_web_agent.py#L4156) | 4156 | `"        None,"` | — |
| [SRC-F725E90B2A-L004157](../../tests/test_web_agent.py#L4157) | 4157 | `"        302,"` | — |
| [SRC-F725E90B2A-L004158](../../tests/test_web_agent.py#L4158) | 4158 | `"        \"Found\","` | — |
| [SRC-F725E90B2A-L004159](../../tests/test_web_agent.py#L4159) | 4159 | `"        {},"` | — |
| [SRC-F725E90B2A-L004160](../../tests/test_web_agent.py#L4160) | 4160 | `"        \"https://attacker.example/collect\","` | — |
| [SRC-F725E90B2A-L004161](../../tests/test_web_agent.py#L4161) | 4161 | `"    )"` | — |
| [SRC-F725E90B2A-L004162](../../tests/test_web_agent.py#L4162) | 4162 | `"    assert redirected is None"` | — |
| [SRC-F725E90B2A-L004163](../../tests/test_web_agent.py#L4163) | 4163 | `""` | — |
| [SRC-F725E90B2A-L004164](../../tests/test_web_agent.py#L4164) | 4164 | `""` | — |
| [SRC-F725E90B2A-L004165](../../tests/test_web_agent.py#L4165) | 4165 | `"def test_openrouter_web_search_does_not_match_spoofed_hostname(monkeypatch):"` | — |
| [SRC-F725E90B2A-L004166](../../tests/test_web_agent.py#L4166) | 4166 | `"    monkeypatch.setenv(\"OMARAI_OPENROUTER_WEB_SEARCH\", \"1\")"` | — |
| [SRC-F725E90B2A-L004167](../../tests/test_web_agent.py#L4167) | 4167 | `"    monkeypatch.setenv("` | — |
| [SRC-F725E90B2A-L004168](../../tests/test_web_agent.py#L4168) | 4168 | `"        \"OMARAI_LLM_BASE_URL\","` | — |
| [SRC-F725E90B2A-L004169](../../tests/test_web_agent.py#L4169) | 4169 | `"        \"https://openrouter.ai.attacker.example/api/v1\","` | — |
| [SRC-F725E90B2A-L004170](../../tests/test_web_agent.py#L4170) | 4170 | `"    )"` | — |
| [SRC-F725E90B2A-L004171](../../tests/test_web_agent.py#L4171) | 4171 | `""` | — |
| [SRC-F725E90B2A-L004172](../../tests/test_web_agent.py#L4172) | 4172 | `"    assert WebAgent().openrouter_web_search_enabled is False"` | — |
| [SRC-F725E90B2A-L004173](../../tests/test_web_agent.py#L4173) | 4173 | `""` | — |
| [SRC-F725E90B2A-L004174](../../tests/test_web_agent.py#L4174) | 4174 | `""` | — |
| [SRC-F725E90B2A-L004175](../../tests/test_web_agent.py#L4175) | 4175 | `""` | — |
| [SRC-F725E90B2A-L004176](../../tests/test_web_agent.py#L4176) | 4176 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L004177](../../tests/test_web_agent.py#L4177) | 4177 | `"    \"address,family\","` | — |
| [SRC-F725E90B2A-L004178](../../tests/test_web_agent.py#L4178) | 4178 | `"    ["` | — |
| [SRC-F725E90B2A-L004179](../../tests/test_web_agent.py#L4179) | 4179 | `"        (\"127.0.0.1\", __import__(\"socket\").AF_INET),"` | — |
| [SRC-F725E90B2A-L004180](../../tests/test_web_agent.py#L4180) | 4180 | `"        (\"169.254.169.254\", __import__(\"socket\").AF_INET),"` | — |
| [SRC-F725E90B2A-L004181](../../tests/test_web_agent.py#L4181) | 4181 | `"        (\"::1\", __import__(\"socket\").AF_INET6),"` | — |
| [SRC-F725E90B2A-L004182](../../tests/test_web_agent.py#L4182) | 4182 | `"        (\"fe80::1\", __import__(\"socket\").AF_INET6),"` | — |
| [SRC-F725E90B2A-L004183](../../tests/test_web_agent.py#L4183) | 4183 | `"        (\"fd00::1\", __import__(\"socket\").AF_INET6),"` | — |
| [SRC-F725E90B2A-L004184](../../tests/test_web_agent.py#L4184) | 4184 | `"    ],"` | — |
| [SRC-F725E90B2A-L004185](../../tests/test_web_agent.py#L4185) | 4185 | `")"` | — |
| [SRC-F725E90B2A-L004186](../../tests/test_web_agent.py#L4186) | 4186 | `"def test_public_ip_literals_rejects_non_global_ipv4_and_ipv6_answers("` | — |
| [SRC-F725E90B2A-L004187](../../tests/test_web_agent.py#L4187) | 4187 | `"    monkeypatch, address, family"` | — |
| [SRC-F725E90B2A-L004188](../../tests/test_web_agent.py#L4188) | 4188 | `"):"` | — |
| [SRC-F725E90B2A-L004189](../../tests/test_web_agent.py#L4189) | 4189 | `"    import socket"` | — |
| [SRC-F725E90B2A-L004190](../../tests/test_web_agent.py#L4190) | 4190 | `""` | — |
| [SRC-F725E90B2A-L004191](../../tests/test_web_agent.py#L4191) | 4191 | `"    from agents import web_agent"` | — |
| [SRC-F725E90B2A-L004192](../../tests/test_web_agent.py#L4192) | 4192 | `""` | — |
| [SRC-F725E90B2A-L004193](../../tests/test_web_agent.py#L4193) | 4193 | `"    answers = ["` | — |
| [SRC-F725E90B2A-L004194](../../tests/test_web_agent.py#L4194) | 4194 | `"        (family, socket.SOCK_STREAM, socket.IPPROTO_TCP, \"\", (address, 80))"` | — |
| [SRC-F725E90B2A-L004195](../../tests/test_web_agent.py#L4195) | 4195 | `"    ]"` | — |
| [SRC-F725E90B2A-L004196](../../tests/test_web_agent.py#L4196) | 4196 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L004197](../../tests/test_web_agent.py#L4197) | 4197 | `"        web_agent.socket,"` | — |
| [SRC-F725E90B2A-L004198](../../tests/test_web_agent.py#L4198) | 4198 | `"        \"getaddrinfo\","` | — |
| [SRC-F725E90B2A-L004199](../../tests/test_web_agent.py#L4199) | 4199 | `"        lambda host, port, type: answers,"` | — |
| [SRC-F725E90B2A-L004200](../../tests/test_web_agent.py#L4200) | 4200 | `"    )"` | — |
| [SRC-F725E90B2A-L004201](../../tests/test_web_agent.py#L4201) | 4201 | `""` | — |
| [SRC-F725E90B2A-L004202](../../tests/test_web_agent.py#L4202) | 4202 | `"    assert web_agent._public_ip_literals(\"untrusted.example\") is None"` | — |
| [SRC-F725E90B2A-L004203](../../tests/test_web_agent.py#L4203) | 4203 | `""` | — |
| [SRC-F725E90B2A-L004204](../../tests/test_web_agent.py#L4204) | 4204 | `""` | — |
| [SRC-F725E90B2A-L004205](../../tests/test_web_agent.py#L4205) | 4205 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L004206](../../tests/test_web_agent.py#L4206) | 4206 | `"    \"url\","` | — |
| [SRC-F725E90B2A-L004207](../../tests/test_web_agent.py#L4207) | 4207 | `"    ["` | — |
| [SRC-F725E90B2A-L004208](../../tests/test_web_agent.py#L4208) | 4208 | `"        \"http://127.0.0.1/private\","` | — |
| [SRC-F725E90B2A-L004209](../../tests/test_web_agent.py#L4209) | 4209 | `"        \"http://169.254.169.254/latest/meta-data/\","` | — |
| [SRC-F725E90B2A-L004210](../../tests/test_web_agent.py#L4210) | 4210 | `"        \"http://[::1]/private\","` | — |
| [SRC-F725E90B2A-L004211](../../tests/test_web_agent.py#L4211) | 4211 | `"        \"http://[fe80::1]/private\","` | — |
| [SRC-F725E90B2A-L004212](../../tests/test_web_agent.py#L4212) | 4212 | `"        \"http://[fd00::1]/private\","` | — |
| [SRC-F725E90B2A-L004213](../../tests/test_web_agent.py#L4213) | 4213 | `"        \"file:///etc/passwd\","` | — |
| [SRC-F725E90B2A-L004214](../../tests/test_web_agent.py#L4214) | 4214 | `"        \"https://user:password@example.com/private\","` | — |
| [SRC-F725E90B2A-L004215](../../tests/test_web_agent.py#L4215) | 4215 | `"        \"https://example.com:8443/private\","` | — |
| [SRC-F725E90B2A-L004216](../../tests/test_web_agent.py#L4216) | 4216 | `"    ],"` | — |
| [SRC-F725E90B2A-L004217](../../tests/test_web_agent.py#L4217) | 4217 | `")"` | — |
| [SRC-F725E90B2A-L004218](../../tests/test_web_agent.py#L4218) | 4218 | `"def test_public_http_url_rejects_non_public_or_unsafe_targets(url):"` | — |
| [SRC-F725E90B2A-L004219](../../tests/test_web_agent.py#L4219) | 4219 | `"    from agents.web_agent import _public_http_url"` | — |
| [SRC-F725E90B2A-L004220](../../tests/test_web_agent.py#L4220) | 4220 | `""` | — |
| [SRC-F725E90B2A-L004221](../../tests/test_web_agent.py#L4221) | 4221 | `"    assert _public_http_url(url) is None"` | — |
| [SRC-F725E90B2A-L004222](../../tests/test_web_agent.py#L4222) | 4222 | `""` | — |
| [SRC-F725E90B2A-L004223](../../tests/test_web_agent.py#L4223) | 4223 | `""` | — |
| [SRC-F725E90B2A-L004224](../../tests/test_web_agent.py#L4224) | 4224 | `"def test_fetch_page_enforces_streamed_byte_limit_when_content_length_lies(monkeypatch):"` | — |
| [SRC-F725E90B2A-L004225](../../tests/test_web_agent.py#L4225) | 4225 | `"    from contextlib import contextmanager"` | — |
| [SRC-F725E90B2A-L004226](../../tests/test_web_agent.py#L4226) | 4226 | `""` | — |
| [SRC-F725E90B2A-L004227](../../tests/test_web_agent.py#L4227) | 4227 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L004228](../../tests/test_web_agent.py#L4228) | 4228 | `""` | — |
| [SRC-F725E90B2A-L004229](../../tests/test_web_agent.py#L4229) | 4229 | `"    from agents import web_agent"` | — |
| [SRC-F725E90B2A-L004230](../../tests/test_web_agent.py#L4230) | 4230 | `""` | — |
| [SRC-F725E90B2A-L004231](../../tests/test_web_agent.py#L4231) | 4231 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L004232](../../tests/test_web_agent.py#L4232) | 4232 | `"        web_agent, \"_public_ip_literals\", lambda _host: [\"93.184.216.34\"]"` | — |
| [SRC-F725E90B2A-L004233](../../tests/test_web_agent.py#L4233) | 4233 | `"    )"` | — |
| [SRC-F725E90B2A-L004234](../../tests/test_web_agent.py#L4234) | 4234 | `"    chunks_yielded = []"` | — |
| [SRC-F725E90B2A-L004235](../../tests/test_web_agent.py#L4235) | 4235 | `""` | — |
| [SRC-F725E90B2A-L004236](../../tests/test_web_agent.py#L4236) | 4236 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L004237](../../tests/test_web_agent.py#L4237) | 4237 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L004238](../../tests/test_web_agent.py#L4238) | 4238 | `"        encoding = \"utf-8\""` | — |
| [SRC-F725E90B2A-L004239](../../tests/test_web_agent.py#L4239) | 4239 | `""` | — |
| [SRC-F725E90B2A-L004240](../../tests/test_web_agent.py#L4240) | 4240 | `"        def __init__(self):"` | — |
| [SRC-F725E90B2A-L004241](../../tests/test_web_agent.py#L4241) | 4241 | `"            self.headers = {"` | — |
| [SRC-F725E90B2A-L004242](../../tests/test_web_agent.py#L4242) | 4242 | `"                \"content-type\": \"text/plain; charset=utf-8\","` | — |
| [SRC-F725E90B2A-L004243](../../tests/test_web_agent.py#L4243) | 4243 | `"                # Deliberately under-reports the actual streamed body length."` | — |
| [SRC-F725E90B2A-L004244](../../tests/test_web_agent.py#L4244) | 4244 | `"                \"content-length\": \"1\","` | — |
| [SRC-F725E90B2A-L004245](../../tests/test_web_agent.py#L4245) | 4245 | `"            }"` | — |
| [SRC-F725E90B2A-L004246](../../tests/test_web_agent.py#L4246) | 4246 | `""` | — |
| [SRC-F725E90B2A-L004247](../../tests/test_web_agent.py#L4247) | 4247 | `"        def iter_bytes(self):"` | — |
| [SRC-F725E90B2A-L004248](../../tests/test_web_agent.py#L4248) | 4248 | `"            chunks = ("` | — |
| [SRC-F725E90B2A-L004249](../../tests/test_web_agent.py#L4249) | 4249 | `"                b\"A\" * web_agent.MAX_PAGE_BYTES,"` | — |
| [SRC-F725E90B2A-L004250](../../tests/test_web_agent.py#L4250) | 4250 | `"                b\"B\" * 32,"` | — |
| [SRC-F725E90B2A-L004251](../../tests/test_web_agent.py#L4251) | 4251 | `"                b\"C\" * 32,"` | — |
| [SRC-F725E90B2A-L004252](../../tests/test_web_agent.py#L4252) | 4252 | `"            )"` | — |
| [SRC-F725E90B2A-L004253](../../tests/test_web_agent.py#L4253) | 4253 | `"            for chunk in chunks:"` | — |
| [SRC-F725E90B2A-L004254](../../tests/test_web_agent.py#L4254) | 4254 | `"                chunks_yielded.append(len(chunk))"` | — |
| [SRC-F725E90B2A-L004255](../../tests/test_web_agent.py#L4255) | 4255 | `"                yield chunk"` | — |
| [SRC-F725E90B2A-L004256](../../tests/test_web_agent.py#L4256) | 4256 | `""` | — |
| [SRC-F725E90B2A-L004257](../../tests/test_web_agent.py#L4257) | 4257 | `"    @contextmanager"` | — |
| [SRC-F725E90B2A-L004258](../../tests/test_web_agent.py#L4258) | 4258 | `"    def fake_stream(self, method, url, **kwargs):"` | — |
| [SRC-F725E90B2A-L004259](../../tests/test_web_agent.py#L4259) | 4259 | `"        assert method == \"GET\""` | — |
| [SRC-F725E90B2A-L004260](../../tests/test_web_agent.py#L4260) | 4260 | `"        assert str(url) == \"https://93.184.216.34/large.txt\""` | — |
| [SRC-F725E90B2A-L004261](../../tests/test_web_agent.py#L4261) | 4261 | `"        yield FakeResponse()"` | — |
| [SRC-F725E90B2A-L004262](../../tests/test_web_agent.py#L4262) | 4262 | `""` | — |
| [SRC-F725E90B2A-L004263](../../tests/test_web_agent.py#L4263) | 4263 | `"    class FakeClient:"` | — |
| [SRC-F725E90B2A-L004264](../../tests/test_web_agent.py#L4264) | 4264 | `"        def __init__(self, **kwargs):"` | — |
| [SRC-F725E90B2A-L004265](../../tests/test_web_agent.py#L4265) | 4265 | `"            self.options = kwargs"` | — |
| [SRC-F725E90B2A-L004266](../../tests/test_web_agent.py#L4266) | 4266 | `""` | — |
| [SRC-F725E90B2A-L004267](../../tests/test_web_agent.py#L4267) | 4267 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L004268](../../tests/test_web_agent.py#L4268) | 4268 | `"            return self"` | — |
| [SRC-F725E90B2A-L004269](../../tests/test_web_agent.py#L4269) | 4269 | `""` | — |
| [SRC-F725E90B2A-L004270](../../tests/test_web_agent.py#L4270) | 4270 | `"        def __exit__(self, *_args):"` | — |
| [SRC-F725E90B2A-L004271](../../tests/test_web_agent.py#L4271) | 4271 | `"            return False"` | — |
| [SRC-F725E90B2A-L004272](../../tests/test_web_agent.py#L4272) | 4272 | `""` | — |
| [SRC-F725E90B2A-L004273](../../tests/test_web_agent.py#L4273) | 4273 | `"        stream = fake_stream"` | — |
| [SRC-F725E90B2A-L004274](../../tests/test_web_agent.py#L4274) | 4274 | `""` | — |
| [SRC-F725E90B2A-L004275](../../tests/test_web_agent.py#L4275) | 4275 | `"    monkeypatch.setattr(httpx, \"Client\", FakeClient)"` | — |
| [SRC-F725E90B2A-L004276](../../tests/test_web_agent.py#L4276) | 4276 | `"    result = web_agent.WebAgent()._fetch_page(\"https://example.com/large.txt\")"` | — |
| [SRC-F725E90B2A-L004277](../../tests/test_web_agent.py#L4277) | 4277 | `""` | — |
| [SRC-F725E90B2A-L004278](../../tests/test_web_agent.py#L4278) | 4278 | `"    assert result.status == \"partial_extraction\""` | — |
| [SRC-F725E90B2A-L004279](../../tests/test_web_agent.py#L4279) | 4279 | `"    assert len(result[1]) <= web_agent.MAX_PAGE_TEXT_CHARS"` | — |
| [SRC-F725E90B2A-L004280](../../tests/test_web_agent.py#L4280) | 4280 | `"    # The reader stops as soon as the byte cap is crossed; it never asks for chunk 3."` | — |
| [SRC-F725E90B2A-L004281](../../tests/test_web_agent.py#L4281) | 4281 | `"    assert chunks_yielded == [web_agent.MAX_PAGE_BYTES, 32]"` | — |
| [SRC-F725E90B2A-L004282](../../tests/test_web_agent.py#L4282) | 4282 | `""` | — |
| [SRC-F725E90B2A-L004283](../../tests/test_web_agent.py#L4283) | 4283 | `""` | — |
| [SRC-F725E90B2A-L004284](../../tests/test_web_agent.py#L4284) | 4284 | `""` | — |
| [SRC-F725E90B2A-L004285](../../tests/test_web_agent.py#L4285) | 4285 | `"@pytest.mark.parametrize(\"field\", [\"title\", \"snippet\", \"page_text\"])"` | — |
| [SRC-F725E90B2A-L004286](../../tests/test_web_agent.py#L4286) | 4286 | `"def test_generate_keeps_title_snippet_and_page_text_untrusted(field, monkeypatch):"` | — |
| [SRC-F725E90B2A-L004287](../../tests/test_web_agent.py#L4287) | 4287 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L004288](../../tests/test_web_agent.py#L4288) | 4288 | `"    source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L004289](../../tests/test_web_agent.py#L4289) | 4289 | `"    injected_text = f\"INJECTED INSTRUCTION FROM UNTRUSTED {field.upper()}\""` | — |
| [SRC-F725E90B2A-L004290](../../tests/test_web_agent.py#L4290) | 4290 | `"    source[field] = injected_text"` | — |
| [SRC-F725E90B2A-L004291](../../tests/test_web_agent.py#L4291) | 4291 | `"    if field == \"snippet\":"` | — |
| [SRC-F725E90B2A-L004292](../../tests/test_web_agent.py#L4292) | 4292 | `"        source[\"page_text\"] = \"\""` | — |
| [SRC-F725E90B2A-L004293](../../tests/test_web_agent.py#L4293) | 4293 | `"    captured = {}"` | — |
| [SRC-F725E90B2A-L004294](../../tests/test_web_agent.py#L4294) | 4294 | `""` | — |
| [SRC-F725E90B2A-L004295](../../tests/test_web_agent.py#L4295) | 4295 | `"    def fake_completion(messages, **kwargs):"` | — |
| [SRC-F725E90B2A-L004296](../../tests/test_web_agent.py#L4296) | 4296 | `"        captured[\"messages\"] = messages"` | — |
| [SRC-F725E90B2A-L004297](../../tests/test_web_agent.py#L4297) | 4297 | `"        return \"إجابة اختبارية.\""` | — |
| [SRC-F725E90B2A-L004298](../../tests/test_web_agent.py#L4298) | 4298 | `""` | — |
| [SRC-F725E90B2A-L004299](../../tests/test_web_agent.py#L4299) | 4299 | `"    monkeypatch.setattr(agent, \"_request_completion\", fake_completion)"` | — |
| [SRC-F725E90B2A-L004300](../../tests/test_web_agent.py#L4300) | 4300 | `"    answer = agent._generate("` | — |
| [SRC-F725E90B2A-L004301](../../tests/test_web_agent.py#L4301) | 4301 | `"        question=\"ما الذي يقوله المصدر؟\","` | — |
| [SRC-F725E90B2A-L004302](../../tests/test_web_agent.py#L4302) | 4302 | `"        history=[],"` | — |
| [SRC-F725E90B2A-L004303](../../tests/test_web_agent.py#L4303) | 4303 | `"        sources=[source],"` | — |
| [SRC-F725E90B2A-L004304](../../tests/test_web_agent.py#L4304) | 4304 | `"        search_warning=None,"` | — |
| [SRC-F725E90B2A-L004305](../../tests/test_web_agent.py#L4305) | 4305 | `"        research_plan={\"depth\": \"standard\", \"queries\": [\"ما الذي يقوله المصدر؟\"]},"` | — |
| [SRC-F725E90B2A-L004306](../../tests/test_web_agent.py#L4306) | 4306 | `"        search_report={},"` | — |
| [SRC-F725E90B2A-L004307](../../tests/test_web_agent.py#L4307) | 4307 | `"    )"` | — |
| [SRC-F725E90B2A-L004308](../../tests/test_web_agent.py#L4308) | 4308 | `""` | — |
| [SRC-F725E90B2A-L004309](../../tests/test_web_agent.py#L4309) | 4309 | `"    messages = captured[\"messages\"]"` | — |
| [SRC-F725E90B2A-L004310](../../tests/test_web_agent.py#L4310) | 4310 | `"    system_content = \"\\n\".join("` | — |
| [SRC-F725E90B2A-L004311](../../tests/test_web_agent.py#L4311) | 4311 | `"        message[\"content\"] for message in messages if message[\"role\"] == \"system\""` | — |
| [SRC-F725E90B2A-L004312](../../tests/test_web_agent.py#L4312) | 4312 | `"    )"` | — |
| [SRC-F725E90B2A-L004313](../../tests/test_web_agent.py#L4313) | 4313 | `"    user_contents = ["` | — |
| [SRC-F725E90B2A-L004314](../../tests/test_web_agent.py#L4314) | 4314 | `"        message[\"content\"] for message in messages if message[\"role\"] == \"user\""` | — |
| [SRC-F725E90B2A-L004315](../../tests/test_web_agent.py#L4315) | 4315 | `"    ]"` | — |
| [SRC-F725E90B2A-L004316](../../tests/test_web_agent.py#L4316) | 4316 | `""` | — |
| [SRC-F725E90B2A-L004317](../../tests/test_web_agent.py#L4317) | 4317 | `"    assert answer == \"إجابة اختبارية.\""` | — |
| [SRC-F725E90B2A-L004318](../../tests/test_web_agent.py#L4318) | 4318 | `"    assert injected_text not in system_content"` | — |
| [SRC-F725E90B2A-L004319](../../tests/test_web_agent.py#L4319) | 4319 | `"    assert any(injected_text in value for value in user_contents)"` | — |
| [SRC-F725E90B2A-L004320](../../tests/test_web_agent.py#L4320) | 4320 | `""` | — |
| [SRC-F725E90B2A-L004321](../../tests/test_web_agent.py#L4321) | 4321 | `""` | — |
| [SRC-F725E90B2A-L004322](../../tests/test_web_agent.py#L4322) | 4322 | `"@pytest.mark.parametrize(\"field\", [\"title\", \"snippet\", \"page_text\"])"` | — |
| [SRC-F725E90B2A-L004323](../../tests/test_web_agent.py#L4323) | 4323 | `"def test_review_keeps_title_snippet_and_page_text_untrusted(field, monkeypatch):"` | — |
| [SRC-F725E90B2A-L004324](../../tests/test_web_agent.py#L4324) | 4324 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L004325](../../tests/test_web_agent.py#L4325) | 4325 | `"    source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L004326](../../tests/test_web_agent.py#L4326) | 4326 | `"    injected_text = f\"INJECTED REVIEW INSTRUCTION FROM UNTRUSTED {field.upper()}\""` | — |
| [SRC-F725E90B2A-L004327](../../tests/test_web_agent.py#L4327) | 4327 | `"    source[field] = injected_text"` | — |
| [SRC-F725E90B2A-L004328](../../tests/test_web_agent.py#L4328) | 4328 | `"    if field == \"snippet\":"` | — |
| [SRC-F725E90B2A-L004329](../../tests/test_web_agent.py#L4329) | 4329 | `"        source[\"page_text\"] = \"\""` | — |
| [SRC-F725E90B2A-L004330](../../tests/test_web_agent.py#L4330) | 4330 | `"    captured = {}"` | — |
| [SRC-F725E90B2A-L004331](../../tests/test_web_agent.py#L4331) | 4331 | `""` | — |
| [SRC-F725E90B2A-L004332](../../tests/test_web_agent.py#L4332) | 4332 | `"    def fake_completion(messages, **kwargs):"` | — |
| [SRC-F725E90B2A-L004333](../../tests/test_web_agent.py#L4333) | 4333 | `"        captured[\"messages\"] = messages"` | — |
| [SRC-F725E90B2A-L004334](../../tests/test_web_agent.py#L4334) | 4334 | `"        return \"<<<OMARAI_FINAL_ANSWER>>>تم تدقيق الإجابة.<<<END_OMARAI_FINAL_ANSWER>>>\""` | — |
| [SRC-F725E90B2A-L004335](../../tests/test_web_agent.py#L4335) | 4335 | `""` | — |
| [SRC-F725E90B2A-L004336](../../tests/test_web_agent.py#L4336) | 4336 | `"    monkeypatch.setattr(agent, \"_request_completion\", fake_completion)"` | — |
| [SRC-F725E90B2A-L004337](../../tests/test_web_agent.py#L4337) | 4337 | `"    answer = agent._review_answer("` | — |
| [SRC-F725E90B2A-L004338](../../tests/test_web_agent.py#L4338) | 4338 | `"        question=\"ما الذي يقوله المصدر؟\","` | — |
| [SRC-F725E90B2A-L004339](../../tests/test_web_agent.py#L4339) | 4339 | `"        answer=\"مسودة إجابة تحتاج التحقق.\","` | — |
| [SRC-F725E90B2A-L004340](../../tests/test_web_agent.py#L4340) | 4340 | `"        sources=[source],"` | — |
| [SRC-F725E90B2A-L004341](../../tests/test_web_agent.py#L4341) | 4341 | `"    )"` | — |
| [SRC-F725E90B2A-L004342](../../tests/test_web_agent.py#L4342) | 4342 | `""` | — |
| [SRC-F725E90B2A-L004343](../../tests/test_web_agent.py#L4343) | 4343 | `"    messages = captured[\"messages\"]"` | — |
| [SRC-F725E90B2A-L004344](../../tests/test_web_agent.py#L4344) | 4344 | `"    system_content = \"\\n\".join("` | — |
| [SRC-F725E90B2A-L004345](../../tests/test_web_agent.py#L4345) | 4345 | `"        message[\"content\"] for message in messages if message[\"role\"] == \"system\""` | — |
| [SRC-F725E90B2A-L004346](../../tests/test_web_agent.py#L4346) | 4346 | `"    )"` | — |
| [SRC-F725E90B2A-L004347](../../tests/test_web_agent.py#L4347) | 4347 | `"    user_contents = ["` | — |
| [SRC-F725E90B2A-L004348](../../tests/test_web_agent.py#L4348) | 4348 | `"        message[\"content\"] for message in messages if message[\"role\"] == \"user\""` | — |
| [SRC-F725E90B2A-L004349](../../tests/test_web_agent.py#L4349) | 4349 | `"    ]"` | — |
| [SRC-F725E90B2A-L004350](../../tests/test_web_agent.py#L4350) | 4350 | `""` | — |
| [SRC-F725E90B2A-L004351](../../tests/test_web_agent.py#L4351) | 4351 | `"    assert answer == \"تم تدقيق الإجابة.\""` | — |
| [SRC-F725E90B2A-L004352](../../tests/test_web_agent.py#L4352) | 4352 | `"    assert injected_text not in system_content"` | — |
| [SRC-F725E90B2A-L004353](../../tests/test_web_agent.py#L4353) | 4353 | `"    assert any(injected_text in value for value in user_contents)"` | — |
| [SRC-F725E90B2A-L004354](../../tests/test_web_agent.py#L4354) | 4354 | `""` | — |
| [SRC-F725E90B2A-L004355](../../tests/test_web_agent.py#L4355) | 4355 | `""` | — |
| [SRC-F725E90B2A-L004356](../../tests/test_web_agent.py#L4356) | 4356 | `""` | — |
| [SRC-F725E90B2A-L004357](../../tests/test_web_agent.py#L4357) | 4357 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L004358](../../tests/test_web_agent.py#L4358) | 4358 | `"    \"url\","` | — |
| [SRC-F725E90B2A-L004359](../../tests/test_web_agent.py#L4359) | 4359 | `"    ["` | — |
| [SRC-F725E90B2A-L004360](../../tests/test_web_agent.py#L4360) | 4360 | `"        \"https://api.example.test/v1\","` | — |
| [SRC-F725E90B2A-L004361](../../tests/test_web_agent.py#L4361) | 4361 | `"        \"http://localhost:11434/v1\","` | — |
| [SRC-F725E90B2A-L004362](../../tests/test_web_agent.py#L4362) | 4362 | `"        \"http://127.0.0.1:8080/v1\","` | — |
| [SRC-F725E90B2A-L004363](../../tests/test_web_agent.py#L4363) | 4363 | `"        \"http://[::1]:8000/v1\","` | — |
| [SRC-F725E90B2A-L004364](../../tests/test_web_agent.py#L4364) | 4364 | `"    ],"` | — |
| [SRC-F725E90B2A-L004365](../../tests/test_web_agent.py#L4365) | 4365 | `")"` | — |
| [SRC-F725E90B2A-L004366](../../tests/test_web_agent.py#L4366) | 4366 | `"def test_model_provider_base_url_allows_https_or_loopback(url):"` | — |
| [SRC-F725E90B2A-L004367](../../tests/test_web_agent.py#L4367) | 4367 | `"    from agents.web_agent import _is_safe_model_base_url"` | — |
| [SRC-F725E90B2A-L004368](../../tests/test_web_agent.py#L4368) | 4368 | `""` | — |
| [SRC-F725E90B2A-L004369](../../tests/test_web_agent.py#L4369) | 4369 | `"    assert _is_safe_model_base_url(url) is True"` | — |
| [SRC-F725E90B2A-L004370](../../tests/test_web_agent.py#L4370) | 4370 | `""` | — |
| [SRC-F725E90B2A-L004371](../../tests/test_web_agent.py#L4371) | 4371 | `""` | — |
| [SRC-F725E90B2A-L004372](../../tests/test_web_agent.py#L4372) | 4372 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L004373](../../tests/test_web_agent.py#L4373) | 4373 | `"    \"url\","` | — |
| [SRC-F725E90B2A-L004374](../../tests/test_web_agent.py#L4374) | 4374 | `"    ["` | — |
| [SRC-F725E90B2A-L004375](../../tests/test_web_agent.py#L4375) | 4375 | `"        \"http://api.example.test/v1\","` | — |
| [SRC-F725E90B2A-L004376](../../tests/test_web_agent.py#L4376) | 4376 | `"        \"ftp://api.example.test/v1\","` | — |
| [SRC-F725E90B2A-L004377](../../tests/test_web_agent.py#L4377) | 4377 | `"        \"https://user:password@api.example.test/v1\","` | — |
| [SRC-F725E90B2A-L004378](../../tests/test_web_agent.py#L4378) | 4378 | `"        \"https://api.example.test/v1?token=secret\","` | — |
| [SRC-F725E90B2A-L004379](../../tests/test_web_agent.py#L4379) | 4379 | `"        \"https://api.example.test/v1#fragment\","` | — |
| [SRC-F725E90B2A-L004380](../../tests/test_web_agent.py#L4380) | 4380 | `"        \"https:///missing-host\","` | — |
| [SRC-F725E90B2A-L004381](../../tests/test_web_agent.py#L4381) | 4381 | `"        \"https://api.example.test:99999/v1\","` | — |
| [SRC-F725E90B2A-L004382](../../tests/test_web_agent.py#L4382) | 4382 | `"    ],"` | — |
| [SRC-F725E90B2A-L004383](../../tests/test_web_agent.py#L4383) | 4383 | `")"` | — |
| [SRC-F725E90B2A-L004384](../../tests/test_web_agent.py#L4384) | 4384 | `"def test_model_provider_base_url_rejects_insecure_or_ambiguous_urls(url):"` | — |
| [SRC-F725E90B2A-L004385](../../tests/test_web_agent.py#L4385) | 4385 | `"    from agents.web_agent import _is_safe_model_base_url"` | — |
| [SRC-F725E90B2A-L004386](../../tests/test_web_agent.py#L4386) | 4386 | `""` | — |
| [SRC-F725E90B2A-L004387](../../tests/test_web_agent.py#L4387) | 4387 | `"    assert _is_safe_model_base_url(url) is False"` | — |
| [SRC-F725E90B2A-L004388](../../tests/test_web_agent.py#L4388) | 4388 | `""` | — |
| [SRC-F725E90B2A-L004389](../../tests/test_web_agent.py#L4389) | 4389 | `""` | — |
| [SRC-F725E90B2A-L004390](../../tests/test_web_agent.py#L4390) | 4390 | `"def test_model_provider_rejects_remote_http_before_sending_bearer_key(monkeypatch):"` | — |
| [SRC-F725E90B2A-L004391](../../tests/test_web_agent.py#L4391) | 4391 | `"    from agents import web_agent"` | — |
| [SRC-F725E90B2A-L004392](../../tests/test_web_agent.py#L4392) | 4392 | `""` | — |
| [SRC-F725E90B2A-L004393](../../tests/test_web_agent.py#L4393) | 4393 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L004394](../../tests/test_web_agent.py#L4394) | 4394 | `"    agent.api_key = \"unit-test-secret\""` | — |
| [SRC-F725E90B2A-L004395](../../tests/test_web_agent.py#L4395) | 4395 | `"    agent.base_url = \"http://provider.example/api/v1\""` | — |
| [SRC-F725E90B2A-L004396](../../tests/test_web_agent.py#L4396) | 4396 | `""` | — |
| [SRC-F725E90B2A-L004397](../../tests/test_web_agent.py#L4397) | 4397 | `"    def unexpected_request(*_args, **_kwargs):"` | — |
| [SRC-F725E90B2A-L004398](../../tests/test_web_agent.py#L4398) | 4398 | `"        pytest.fail(\"bearer credentials must not be sent to a remote HTTP URL\")"` | — |
| [SRC-F725E90B2A-L004399](../../tests/test_web_agent.py#L4399) | 4399 | `""` | — |
| [SRC-F725E90B2A-L004400](../../tests/test_web_agent.py#L4400) | 4400 | `"    monkeypatch.setattr(web_agent, \"_open_model_request\", unexpected_request)"` | — |
| [SRC-F725E90B2A-L004401](../../tests/test_web_agent.py#L4401) | 4401 | `"    with pytest.raises(RuntimeError, match=\"HTTPS\"):"` | — |
| [SRC-F725E90B2A-L004402](../../tests/test_web_agent.py#L4402) | 4402 | `"        agent._request_completion("` | — |
| [SRC-F725E90B2A-L004403](../../tests/test_web_agent.py#L4403) | 4403 | `"            [{\"role\": \"user\", \"content\": \"test\"}],"` | — |
| [SRC-F725E90B2A-L004404](../../tests/test_web_agent.py#L4404) | 4404 | `"            max_tokens=100,"` | — |
| [SRC-F725E90B2A-L004405](../../tests/test_web_agent.py#L4405) | 4405 | `"        )"` | — |
| [SRC-F725E90B2A-L004406](../../tests/test_web_agent.py#L4406) | 4406 | `""` | — |
| [SRC-F725E90B2A-L004407](../../tests/test_web_agent.py#L4407) | 4407 | `"    assert agent.generation_diagnostics[-1][\"status\"] == \"unsafe_provider_url\""` | — |
| [SRC-F725E90B2A-L004408](../../tests/test_web_agent.py#L4408) | 4408 | `"    assert agent.generation_diagnostics[-1][\"request_started\"] is False"` | — |
| [SRC-F725E90B2A-L004409](../../tests/test_web_agent.py#L4409) | 4409 | `""` | — |
| [SRC-F725E90B2A-L004410](../../tests/test_web_agent.py#L4410) | 4410 | `""` | — |
| [SRC-F725E90B2A-L004411](../../tests/test_web_agent.py#L4411) | 4411 | `"def test_health_status_redacts_model_provider_userinfo_path_and_query(monkeypatch):"` | — |
| [SRC-F725E90B2A-L004412](../../tests/test_web_agent.py#L4412) | 4412 | `"    monkeypatch.setenv("` | — |
| [SRC-F725E90B2A-L004413](../../tests/test_web_agent.py#L4413) | 4413 | `"        \"OMARAI_LLM_BASE_URL\","` | — |
| [SRC-F725E90B2A-L004414](../../tests/test_web_agent.py#L4414) | 4414 | `"        \"https://health-user:health-password@provider.example/api/v1?token=health-secret\","` | — |
| [SRC-F725E90B2A-L004415](../../tests/test_web_agent.py#L4415) | 4415 | `"    )"` | — |
| [SRC-F725E90B2A-L004416](../../tests/test_web_agent.py#L4416) | 4416 | `""` | — |
| [SRC-F725E90B2A-L004417](../../tests/test_web_agent.py#L4417) | 4417 | `"    status = WebAgent.status()"` | — |
| [SRC-F725E90B2A-L004418](../../tests/test_web_agent.py#L4418) | 4418 | `"    provider = status[\"language_model_provider\"]"` | — |
| [SRC-F725E90B2A-L004419](../../tests/test_web_agent.py#L4419) | 4419 | `""` | — |
| [SRC-F725E90B2A-L004420](../../tests/test_web_agent.py#L4420) | 4420 | `"    assert provider == \"https://provider.example\""` | — |
| [SRC-F725E90B2A-L004421](../../tests/test_web_agent.py#L4421) | 4421 | `"    assert \"health-user\" not in provider"` | — |
| [SRC-F725E90B2A-L004422](../../tests/test_web_agent.py#L4422) | 4422 | `"    assert \"health-password\" not in provider"` | — |
| [SRC-F725E90B2A-L004423](../../tests/test_web_agent.py#L4423) | 4423 | `"    assert \"health-secret\" not in provider"` | — |
| [SRC-F725E90B2A-L004424](../../tests/test_web_agent.py#L4424) | 4424 | `"    assert \"/api/v1\" not in provider"` | — |
| [SRC-F725E90B2A-L004425](../../tests/test_web_agent.py#L4425) | 4425 | `""` | — |
| [SRC-F725E90B2A-L004426](../../tests/test_web_agent.py#L4426) | 4426 | `""` | — |
| [SRC-F725E90B2A-L004427](../../tests/test_web_agent.py#L4427) | 4427 | `"def test_answer_is_withheld_when_semantic_claim_support_is_not_established(monkeypatch):"` | — |
| [SRC-F725E90B2A-L004428](../../tests/test_web_agent.py#L4428) | 4428 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L004429](../../tests/test_web_agent.py#L4429) | 4429 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L004430](../../tests/test_web_agent.py#L4430) | 4430 | `"    source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L004431](../../tests/test_web_agent.py#L4431) | 4431 | `"    source[\"providers\"] = [\"user_supplied_url\"]"` | — |
| [SRC-F725E90B2A-L004432](../../tests/test_web_agent.py#L4432) | 4432 | `"    source[\"page_fetched\"] = True"` | — |
| [SRC-F725E90B2A-L004433](../../tests/test_web_agent.py#L4433) | 4433 | `"    source[\"page_text\"] = \"النص الكامل المستخرج من الصفحة التي قدمها المستخدم.\""` | — |
| [SRC-F725E90B2A-L004434](../../tests/test_web_agent.py#L4434) | 4434 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L004435](../../tests/test_web_agent.py#L4435) | 4435 | `"        \"queries\": [\"لخص الصفحة\"],"` | — |
| [SRC-F725E90B2A-L004436](../../tests/test_web_agent.py#L4436) | 4436 | `"        \"direct_urls\": [\"https://example.com/research\"],"` | — |
| [SRC-F725E90B2A-L004437](../../tests/test_web_agent.py#L4437) | 4437 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L004438](../../tests/test_web_agent.py#L4438) | 4438 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L004439](../../tests/test_web_agent.py#L4439) | 4439 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L004440](../../tests/test_web_agent.py#L4440) | 4440 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L004441](../../tests/test_web_agent.py#L4441) | 4441 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L004442](../../tests/test_web_agent.py#L4442) | 4442 | `"    }"` | — |
| [SRC-F725E90B2A-L004443](../../tests/test_web_agent.py#L4443) | 4443 | `""` | — |
| [SRC-F725E90B2A-L004444](../../tests/test_web_agent.py#L4444) | 4444 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L004445](../../tests/test_web_agent.py#L4445) | 4445 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L004446](../../tests/test_web_agent.py#L4446) | 4446 | `"        agent,"` | — |
| [SRC-F725E90B2A-L004447](../../tests/test_web_agent.py#L4447) | 4447 | `"        \"_collect_research\","` | — |
| [SRC-F725E90B2A-L004448](../../tests/test_web_agent.py#L4448) | 4448 | `"        lambda research_plan: ("` | — |
| [SRC-F725E90B2A-L004449](../../tests/test_web_agent.py#L4449) | 4449 | `"            [source], [], {"` | — |
| [SRC-F725E90B2A-L004450](../../tests/test_web_agent.py#L4450) | 4450 | `"                \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L004451](../../tests/test_web_agent.py#L4451) | 4451 | `"                \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L004452](../../tests/test_web_agent.py#L4452) | 4452 | `"                \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L004453](../../tests/test_web_agent.py#L4453) | 4453 | `"                \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L004454](../../tests/test_web_agent.py#L4454) | 4454 | `"                \"pages_fetched\": 1,"` | — |
| [SRC-F725E90B2A-L004455](../../tests/test_web_agent.py#L4455) | 4455 | `"                \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L004456](../../tests/test_web_agent.py#L4456) | 4456 | `"                \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L004457](../../tests/test_web_agent.py#L4457) | 4457 | `"                \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L004458](../../tests/test_web_agent.py#L4458) | 4458 | `"                \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L004459](../../tests/test_web_agent.py#L4459) | 4459 | `"                \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L004460](../../tests/test_web_agent.py#L4460) | 4460 | `"            },"` | — |
| [SRC-F725E90B2A-L004461](../../tests/test_web_agent.py#L4461) | 4461 | `"        ),"` | — |
| [SRC-F725E90B2A-L004462](../../tests/test_web_agent.py#L4462) | 4462 | `"    )"` | — |
| [SRC-F725E90B2A-L004463](../../tests/test_web_agent.py#L4463) | 4463 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, item: True)"` | — |
| [SRC-F725E90B2A-L004464](../../tests/test_web_agent.py#L4464) | 4464 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L004465](../../tests/test_web_agent.py#L4465) | 4465 | `"        agent, \"_generate\","` | — |
| [SRC-F725E90B2A-L004466](../../tests/test_web_agent.py#L4466) | 4466 | `"        lambda *args, **kwargs: \"ادعاء واقعي غير مدعوم بما يكفي [المصدر 1].\","` | — |
| [SRC-F725E90B2A-L004467](../../tests/test_web_agent.py#L4467) | 4467 | `"    )"` | — |
| [SRC-F725E90B2A-L004468](../../tests/test_web_agent.py#L4468) | 4468 | `"    monkeypatch.setattr("` | — |
