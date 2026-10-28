# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **009**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L003676 إلى SRC-1AE03B9EC3-L004475
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L003676](../../agents/web_agent.py#L3676) | 3676 | `"        probe_sources: dict[str, dict[str, Any]] = {}"` | — |
| [SRC-1AE03B9EC3-L003677](../../agents/web_agent.py#L3677) | 3677 | `"        completed_connector_responses = 0"` | — |
| [SRC-1AE03B9EC3-L003678](../../agents/web_agent.py#L3678) | 3678 | `"        probe_errors: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L003679](../../agents/web_agent.py#L3679) | 3679 | `"        probes_attempted = 0"` | — |
| [SRC-1AE03B9EC3-L003680](../../agents/web_agent.py#L3680) | 3680 | `"        for probe_query in probe_queries:"` | — |
| [SRC-1AE03B9EC3-L003681](../../agents/web_agent.py#L3681) | 3681 | `"            probes_attempted += 1"` | — |
| [SRC-1AE03B9EC3-L003682](../../agents/web_agent.py#L3682) | 3682 | `"            with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L003683](../../agents/web_agent.py#L3683) | 3683 | `"                previous_ids = {id(item) for item in self._provider_diagnostics}"` | — |
| [SRC-1AE03B9EC3-L003684](../../agents/web_agent.py#L3684) | 3684 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L003685](../../agents/web_agent.py#L3685) | 3685 | `"                returned = self._search_web(probe_query)"` | — |
| [SRC-1AE03B9EC3-L003686](../../agents/web_agent.py#L3686) | 3686 | `"            except (RuntimeError, AgentDependencyError, ValueError, OSError) as exc:"` | — |
| [SRC-1AE03B9EC3-L003687](../../agents/web_agent.py#L3687) | 3687 | `"                probe_errors.append(type(exc).__name__)"` | — |
| [SRC-1AE03B9EC3-L003688](../../agents/web_agent.py#L3688) | 3688 | `"                with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L003689](../../agents/web_agent.py#L3689) | 3689 | `"                    new_diagnostics = ["` | — |
| [SRC-1AE03B9EC3-L003690](../../agents/web_agent.py#L3690) | 3690 | `"                        item for item in self._provider_diagnostics"` | — |
| [SRC-1AE03B9EC3-L003691](../../agents/web_agent.py#L3691) | 3691 | `"                        if id(item) not in previous_ids"` | — |
| [SRC-1AE03B9EC3-L003692](../../agents/web_agent.py#L3692) | 3692 | `"                    ]"` | — |
| [SRC-1AE03B9EC3-L003693](../../agents/web_agent.py#L3693) | 3693 | `"                completed_connector_responses += sum("` | — |
| [SRC-1AE03B9EC3-L003694](../../agents/web_agent.py#L3694) | 3694 | `"                    item.get(\"status\") in _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES"` | — |
| [SRC-1AE03B9EC3-L003695](../../agents/web_agent.py#L3695) | 3695 | `"                    for item in new_diagnostics"` | — |
| [SRC-1AE03B9EC3-L003696](../../agents/web_agent.py#L3696) | 3696 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003697](../../agents/web_agent.py#L3697) | 3697 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L003698](../../agents/web_agent.py#L3698) | 3698 | `""` | — |
| [SRC-1AE03B9EC3-L003699](../../agents/web_agent.py#L3699) | 3699 | `"            for source in returned:"` | — |
| [SRC-1AE03B9EC3-L003700](../../agents/web_agent.py#L3700) | 3700 | `"                if not isinstance(source, dict):"` | — |
| [SRC-1AE03B9EC3-L003701](../../agents/web_agent.py#L3701) | 3701 | `"                    continue"` | — |
| [SRC-1AE03B9EC3-L003702](../../agents/web_agent.py#L3702) | 3702 | `"                safe_url = _public_http_url(source.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L003703](../../agents/web_agent.py#L3703) | 3703 | `"                if not safe_url or _blocked_source_url(safe_url):"` | — |
| [SRC-1AE03B9EC3-L003704](../../agents/web_agent.py#L3704) | 3704 | `"                    continue"` | — |
| [SRC-1AE03B9EC3-L003705](../../agents/web_agent.py#L3705) | 3705 | `"                probe_sources.setdefault(safe_url.split(\"#\", 1)[0].rstrip(\"/\"), source)"` | — |
| [SRC-1AE03B9EC3-L003706](../../agents/web_agent.py#L3706) | 3706 | `"            if returned:"` | — |
| [SRC-1AE03B9EC3-L003707](../../agents/web_agent.py#L3707) | 3707 | `"                break"` | — |
| [SRC-1AE03B9EC3-L003708](../../agents/web_agent.py#L3708) | 3708 | `""` | — |
| [SRC-1AE03B9EC3-L003709](../../agents/web_agent.py#L3709) | 3709 | `"            with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L003710](../../agents/web_agent.py#L3710) | 3710 | `"                new_diagnostics = ["` | — |
| [SRC-1AE03B9EC3-L003711](../../agents/web_agent.py#L3711) | 3711 | `"                    item for item in self._provider_diagnostics"` | — |
| [SRC-1AE03B9EC3-L003712](../../agents/web_agent.py#L3712) | 3712 | `"                    if id(item) not in previous_ids"` | — |
| [SRC-1AE03B9EC3-L003713](../../agents/web_agent.py#L3713) | 3713 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L003714](../../agents/web_agent.py#L3714) | 3714 | `"            if any(item.get(\"status\") in _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES"` | — |
| [SRC-1AE03B9EC3-L003715](../../agents/web_agent.py#L3715) | 3715 | `"                   for item in new_diagnostics):"` | — |
| [SRC-1AE03B9EC3-L003716](../../agents/web_agent.py#L3716) | 3716 | `"                completed_connector_responses += 1"` | — |
| [SRC-1AE03B9EC3-L003717](../../agents/web_agent.py#L3717) | 3717 | `""` | — |
| [SRC-1AE03B9EC3-L003718](../../agents/web_agent.py#L3718) | 3718 | `"        probe_result_list = list(probe_sources.values())"` | — |
| [SRC-1AE03B9EC3-L003719](../../agents/web_agent.py#L3719) | 3719 | `"        providers: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L003720](../../agents/web_agent.py#L3720) | 3720 | `"        for source in probe_result_list:"` | — |
| [SRC-1AE03B9EC3-L003721](../../agents/web_agent.py#L3721) | 3721 | `"            provider = str(source.get(\"provider\") or \"unknown\")"` | — |
| [SRC-1AE03B9EC3-L003722](../../agents/web_agent.py#L3722) | 3722 | `"            providers[provider] = providers.get(provider, 0) + 1"` | — |
| [SRC-1AE03B9EC3-L003723](../../agents/web_agent.py#L3723) | 3723 | `"        with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L003724](../../agents/web_agent.py#L3724) | 3724 | `"            confirmed_connector_attempts = sum("` | — |
| [SRC-1AE03B9EC3-L003725](../../agents/web_agent.py#L3725) | 3725 | `"                1 for item in self._provider_diagnostics"` | — |
| [SRC-1AE03B9EC3-L003726](../../agents/web_agent.py#L3726) | 3726 | `"                if item.get(\"status\") in _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES"` | — |
| [SRC-1AE03B9EC3-L003727](../../agents/web_agent.py#L3727) | 3727 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003728](../../agents/web_agent.py#L3728) | 3728 | `"            provider_failure_count = sum("` | — |
| [SRC-1AE03B9EC3-L003729](../../agents/web_agent.py#L3729) | 3729 | `"                1 for item in self._provider_diagnostics"` | — |
| [SRC-1AE03B9EC3-L003730](../../agents/web_agent.py#L3730) | 3730 | `"                if item.get(\"status\") in {\"failed\", \"timeout\"}"` | — |
| [SRC-1AE03B9EC3-L003731](../../agents/web_agent.py#L3731) | 3731 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003732](../../agents/web_agent.py#L3732) | 3732 | `"        if probe_result_list:"` | — |
| [SRC-1AE03B9EC3-L003733](../../agents/web_agent.py#L3733) | 3733 | `"            web_status = \"passed\""` | — |
| [SRC-1AE03B9EC3-L003734](../../agents/web_agent.py#L3734) | 3734 | `"            web_note = ("` | — |
| [SRC-1AE03B9EC3-L003735](../../agents/web_agent.py#L3735) | 3735 | `"                \"A public search connector returned a usable result. This confirms a successful \""` | — |
| [SRC-1AE03B9EC3-L003736](../../agents/web_agent.py#L3736) | 3736 | `"                \"probe, not general reachability or answer quality.\""` | — |
| [SRC-1AE03B9EC3-L003737](../../agents/web_agent.py#L3737) | 3737 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003738](../../agents/web_agent.py#L3738) | 3738 | `"        elif completed_connector_responses:"` | — |
| [SRC-1AE03B9EC3-L003739](../../agents/web_agent.py#L3739) | 3739 | `"            web_status = \"degraded\""` | — |
| [SRC-1AE03B9EC3-L003740](../../agents/web_agent.py#L3740) | 3740 | `"            web_note = ("` | — |
| [SRC-1AE03B9EC3-L003741](../../agents/web_agent.py#L3741) | 3741 | `"                \"At least one connector completed a request, but no usable results were returned. \""` | — |
| [SRC-1AE03B9EC3-L003742](../../agents/web_agent.py#L3742) | 3742 | `"                \"This differs from a confirmed connection failure.\""` | — |
| [SRC-1AE03B9EC3-L003743](../../agents/web_agent.py#L3743) | 3743 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003744](../../agents/web_agent.py#L3744) | 3744 | `"        elif probe_errors or provider_failure_count:"` | — |
| [SRC-1AE03B9EC3-L003745](../../agents/web_agent.py#L3745) | 3745 | `"            web_status = \"failed\""` | — |
| [SRC-1AE03B9EC3-L003746](../../agents/web_agent.py#L3746) | 3746 | `"            web_note = \"All probes failed before any completed connector response or usable result was confirmed.\""` | — |
| [SRC-1AE03B9EC3-L003747](../../agents/web_agent.py#L3747) | 3747 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L003748](../../agents/web_agent.py#L3748) | 3748 | `"            web_status = \"degraded\""` | — |
| [SRC-1AE03B9EC3-L003749](../../agents/web_agent.py#L3749) | 3749 | `"            web_note = ("` | — |
| [SRC-1AE03B9EC3-L003750](../../agents/web_agent.py#L3750) | 3750 | `"                \"No usable matches were returned and connector completion could not be confirmed; \""` | — |
| [SRC-1AE03B9EC3-L003751](../../agents/web_agent.py#L3751) | 3751 | `"                \"this is inconclusive, not proof that all search services are offline.\""` | — |
| [SRC-1AE03B9EC3-L003752](../../agents/web_agent.py#L3752) | 3752 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003753](../../agents/web_agent.py#L3753) | 3753 | `"        report[\"checks\"][\"web_search\"] = {"` | — |
| [SRC-1AE03B9EC3-L003754](../../agents/web_agent.py#L3754) | 3754 | `"            \"status\": web_status,"` | — |
| [SRC-1AE03B9EC3-L003755](../../agents/web_agent.py#L3755) | 3755 | `"            \"result_count\": len(probe_result_list),"` | — |
| [SRC-1AE03B9EC3-L003756](../../agents/web_agent.py#L3756) | 3756 | `"            \"provider_counts\": providers,"` | — |
| [SRC-1AE03B9EC3-L003757](../../agents/web_agent.py#L3757) | 3757 | `"            \"probe_count\": probes_attempted,"` | — |
| [SRC-1AE03B9EC3-L003758](../../agents/web_agent.py#L3758) | 3758 | `"            \"completed_connector_responses\": completed_connector_responses,"` | — |
| [SRC-1AE03B9EC3-L003759](../../agents/web_agent.py#L3759) | 3759 | `"            \"confirmed_connector_attempts\": confirmed_connector_attempts,"` | — |
| [SRC-1AE03B9EC3-L003760](../../agents/web_agent.py#L3760) | 3760 | `"            \"note\": _clean_text(web_note, 400),"` | — |
| [SRC-1AE03B9EC3-L003761](../../agents/web_agent.py#L3761) | 3761 | `"        }"` | — |
| [SRC-1AE03B9EC3-L003762](../../agents/web_agent.py#L3762) | 3762 | `""` | — |
| [SRC-1AE03B9EC3-L003763](../../agents/web_agent.py#L3763) | 3763 | `"        # Do not send a provider request unless a model check was explicitly requested."` | — |
| [SRC-1AE03B9EC3-L003764](../../agents/web_agent.py#L3764) | 3764 | `"        if not test_model:"` | — |
| [SRC-1AE03B9EC3-L003765](../../agents/web_agent.py#L3765) | 3765 | `"            report[\"checks\"][\"language_model\"] = {"` | — |
| [SRC-1AE03B9EC3-L003766](../../agents/web_agent.py#L3766) | 3766 | `"                \"status\": \"skipped\","` | — |
| [SRC-1AE03B9EC3-L003767](../../agents/web_agent.py#L3767) | 3767 | `"                \"note\": \"Model request was not requested.\","` | — |
| [SRC-1AE03B9EC3-L003768](../../agents/web_agent.py#L3768) | 3768 | `"            }"` | — |
| [SRC-1AE03B9EC3-L003769](../../agents/web_agent.py#L3769) | 3769 | `"        elif not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L003770](../../agents/web_agent.py#L3770) | 3770 | `"            report[\"checks\"][\"language_model\"] = {"` | — |
| [SRC-1AE03B9EC3-L003771](../../agents/web_agent.py#L3771) | 3771 | `"                \"status\": \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L003772](../../agents/web_agent.py#L3772) | 3772 | `"                \"note\": \"No language-model key is configured in this server session.\","` | — |
| [SRC-1AE03B9EC3-L003773](../../agents/web_agent.py#L3773) | 3773 | `"            }"` | — |
| [SRC-1AE03B9EC3-L003774](../../agents/web_agent.py#L3774) | 3774 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L003775](../../agents/web_agent.py#L3775) | 3775 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L003776](../../agents/web_agent.py#L3776) | 3776 | `"                probe = self._request_completion("` | — |
| [SRC-1AE03B9EC3-L003777](../../agents/web_agent.py#L3777) | 3777 | `"                    ["` | — |
| [SRC-1AE03B9EC3-L003778](../../agents/web_agent.py#L3778) | 3778 | `"                        {"` | — |
| [SRC-1AE03B9EC3-L003779](../../agents/web_agent.py#L3779) | 3779 | `"                            \"role\": \"system\","` | — |
| [SRC-1AE03B9EC3-L003780](../../agents/web_agent.py#L3780) | 3780 | `"                            \"content\": \"Reply with the exact text OK and nothing else.\","` | — |
| [SRC-1AE03B9EC3-L003781](../../agents/web_agent.py#L3781) | 3781 | `"                        },"` | — |
| [SRC-1AE03B9EC3-L003782](../../agents/web_agent.py#L3782) | 3782 | `"                        {"` | — |
| [SRC-1AE03B9EC3-L003783](../../agents/web_agent.py#L3783) | 3783 | `"                            \"role\": \"user\","` | — |
| [SRC-1AE03B9EC3-L003784](../../agents/web_agent.py#L3784) | 3784 | `"                            \"content\": \"Omarai connectivity self-test.\","` | — |
| [SRC-1AE03B9EC3-L003785](../../agents/web_agent.py#L3785) | 3785 | `"                        },"` | — |
| [SRC-1AE03B9EC3-L003786](../../agents/web_agent.py#L3786) | 3786 | `"                    ],"` | — |
| [SRC-1AE03B9EC3-L003787](../../agents/web_agent.py#L3787) | 3787 | `"                    max_tokens=12,"` | — |
| [SRC-1AE03B9EC3-L003788](../../agents/web_agent.py#L3788) | 3788 | `"                    temperature=0.0,"` | — |
| [SRC-1AE03B9EC3-L003789](../../agents/web_agent.py#L3789) | 3789 | `"                    timeout=self._effective_timeout(min(self.timeout, 12)),"` | — |
| [SRC-1AE03B9EC3-L003790](../../agents/web_agent.py#L3790) | 3790 | `"                    model=self.answer_model,"` | — |
| [SRC-1AE03B9EC3-L003791](../../agents/web_agent.py#L3791) | 3791 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003792](../../agents/web_agent.py#L3792) | 3792 | `"                report[\"checks\"][\"language_model\"] = {"` | — |
| [SRC-1AE03B9EC3-L003793](../../agents/web_agent.py#L3793) | 3793 | `"                    \"status\": \"passed\" if probe.strip() else \"failed\","` | — |
| [SRC-1AE03B9EC3-L003794](../../agents/web_agent.py#L3794) | 3794 | `"                    \"note\": \"A real model completion was received; no prompt content was retained.\","` | — |
| [SRC-1AE03B9EC3-L003795](../../agents/web_agent.py#L3795) | 3795 | `"                    \"response_received\": bool(probe.strip()),"` | — |
| [SRC-1AE03B9EC3-L003796](../../agents/web_agent.py#L3796) | 3796 | `"                }"` | — |
| [SRC-1AE03B9EC3-L003797](../../agents/web_agent.py#L3797) | 3797 | `"            except (RuntimeError, AgentDependencyError) as exc:"` | — |
| [SRC-1AE03B9EC3-L003798](../../agents/web_agent.py#L3798) | 3798 | `"                report[\"checks\"][\"language_model\"] = {"` | — |
| [SRC-1AE03B9EC3-L003799](../../agents/web_agent.py#L3799) | 3799 | `"                    \"status\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L003800](../../agents/web_agent.py#L3800) | 3800 | `"                    \"note\": _clean_text(str(exc), 400),"` | — |
| [SRC-1AE03B9EC3-L003801](../../agents/web_agent.py#L3801) | 3801 | `"                }"` | — |
| [SRC-1AE03B9EC3-L003802](../../agents/web_agent.py#L3802) | 3802 | `""` | — |
| [SRC-1AE03B9EC3-L003803](../../agents/web_agent.py#L3803) | 3803 | `"        if not test_social:"` | — |
| [SRC-1AE03B9EC3-L003804](../../agents/web_agent.py#L3804) | 3804 | `"            report[\"checks\"][\"social_search\"] = {"` | — |
| [SRC-1AE03B9EC3-L003805](../../agents/web_agent.py#L3805) | 3805 | `"                \"status\": \"skipped\","` | — |
| [SRC-1AE03B9EC3-L003806](../../agents/web_agent.py#L3806) | 3806 | `"                \"note\": \"Social-source probes were not requested.\","` | — |
| [SRC-1AE03B9EC3-L003807](../../agents/web_agent.py#L3807) | 3807 | `"            }"` | — |
| [SRC-1AE03B9EC3-L003808](../../agents/web_agent.py#L3808) | 3808 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L003809](../../agents/web_agent.py#L3809) | 3809 | `"            configured_platforms = [\"reddit\", \"bluesky\"]"` | — |
| [SRC-1AE03B9EC3-L003810](../../agents/web_agent.py#L3810) | 3810 | `"            optional_connectors = {"` | — |
| [SRC-1AE03B9EC3-L003811](../../agents/web_agent.py#L3811) | 3811 | `"                \"facebook\": bool("` | — |
| [SRC-1AE03B9EC3-L003812](../../agents/web_agent.py#L3812) | 3812 | `"                    os.getenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L003813](../../agents/web_agent.py#L3813) | 3813 | `"                    and os.getenv(\"FACEBOOK_PAGE_IDS\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L003814](../../agents/web_agent.py#L3814) | 3814 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L003815](../../agents/web_agent.py#L3815) | 3815 | `"                \"instagram\": bool("` | — |
| [SRC-1AE03B9EC3-L003816](../../agents/web_agent.py#L3816) | 3816 | `"                    os.getenv(\"INSTAGRAM_USER_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L003817](../../agents/web_agent.py#L3817) | 3817 | `"                    and os.getenv(\"INSTAGRAM_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L003818](../../agents/web_agent.py#L3818) | 3818 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L003819](../../agents/web_agent.py#L3819) | 3819 | `"                \"x\": bool(os.getenv(\"X_BEARER_TOKEN\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L003820](../../agents/web_agent.py#L3820) | 3820 | `"                \"youtube\": bool(os.getenv(\"YOUTUBE_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L003821](../../agents/web_agent.py#L3821) | 3821 | `"            }"` | — |
| [SRC-1AE03B9EC3-L003822](../../agents/web_agent.py#L3822) | 3822 | `"            configured_platforms.extend("` | — |
| [SRC-1AE03B9EC3-L003823](../../agents/web_agent.py#L3823) | 3823 | `"                platform"` | — |
| [SRC-1AE03B9EC3-L003824](../../agents/web_agent.py#L3824) | 3824 | `"                for platform, is_configured in optional_connectors.items()"` | — |
| [SRC-1AE03B9EC3-L003825](../../agents/web_agent.py#L3825) | 3825 | `"                if is_configured"` | — |
| [SRC-1AE03B9EC3-L003826](../../agents/web_agent.py#L3826) | 3826 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003827](../../agents/web_agent.py#L3827) | 3827 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L003828](../../agents/web_agent.py#L3828) | 3828 | `"                social_results, social_warnings = self._search_social("` | — |
| [SRC-1AE03B9EC3-L003829](../../agents/web_agent.py#L3829) | 3829 | `"                    \"Omarai public connectivity test\", configured_platforms"` | — |
| [SRC-1AE03B9EC3-L003830](../../agents/web_agent.py#L3830) | 3830 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003831](../../agents/web_agent.py#L3831) | 3831 | `"                providers: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L003832](../../agents/web_agent.py#L3832) | 3832 | `"                for source in social_results:"` | — |
| [SRC-1AE03B9EC3-L003833](../../agents/web_agent.py#L3833) | 3833 | `"                    provider = str(source.get(\"provider\") or \"unknown\")"` | — |
| [SRC-1AE03B9EC3-L003834](../../agents/web_agent.py#L3834) | 3834 | `"                    providers[provider] = providers.get(provider, 0) + 1"` | — |
| [SRC-1AE03B9EC3-L003835](../../agents/web_agent.py#L3835) | 3835 | `"                report[\"checks\"][\"social_search\"] = {"` | — |
| [SRC-1AE03B9EC3-L003836](../../agents/web_agent.py#L3836) | 3836 | `"                    \"status\": \"passed\" if social_results else \"degraded\","` | — |
| [SRC-1AE03B9EC3-L003837](../../agents/web_agent.py#L3837) | 3837 | `"                    \"platforms_tested\": configured_platforms,"` | — |
| [SRC-1AE03B9EC3-L003838](../../agents/web_agent.py#L3838) | 3838 | `"                    \"result_count\": len(social_results),"` | — |
| [SRC-1AE03B9EC3-L003839](../../agents/web_agent.py#L3839) | 3839 | `"                    \"provider_counts\": providers,"` | — |
| [SRC-1AE03B9EC3-L003840](../../agents/web_agent.py#L3840) | 3840 | `"                    \"warnings\": [_clean_text(item, 300) for item in social_warnings[:8]],"` | — |
| [SRC-1AE03B9EC3-L003841](../../agents/web_agent.py#L3841) | 3841 | `"                    \"note\": ("` | — |
| [SRC-1AE03B9EC3-L003842](../../agents/web_agent.py#L3842) | 3842 | `"                        \"Public-source request(s) returned results.\""` | — |
| [SRC-1AE03B9EC3-L003843](../../agents/web_agent.py#L3843) | 3843 | `"                        if social_results"` | — |
| [SRC-1AE03B9EC3-L003844](../../agents/web_agent.py#L3844) | 3844 | `"                        else \"No parseable public social results were returned. This does not establish that the platform is offline.\""` | — |
| [SRC-1AE03B9EC3-L003845](../../agents/web_agent.py#L3845) | 3845 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L003846](../../agents/web_agent.py#L3846) | 3846 | `"                }"` | — |
| [SRC-1AE03B9EC3-L003847](../../agents/web_agent.py#L3847) | 3847 | `"            except (RuntimeError, AgentDependencyError, ValueError, OSError) as exc:"` | — |
| [SRC-1AE03B9EC3-L003848](../../agents/web_agent.py#L3848) | 3848 | `"                report[\"checks\"][\"social_search\"] = {"` | — |
| [SRC-1AE03B9EC3-L003849](../../agents/web_agent.py#L3849) | 3849 | `"                    \"status\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L003850](../../agents/web_agent.py#L3850) | 3850 | `"                    \"platforms_tested\": configured_platforms,"` | — |
| [SRC-1AE03B9EC3-L003851](../../agents/web_agent.py#L3851) | 3851 | `"                    \"result_count\": 0,"` | — |
| [SRC-1AE03B9EC3-L003852](../../agents/web_agent.py#L3852) | 3852 | `"                    \"note\": _clean_text(str(exc), 400),"` | — |
| [SRC-1AE03B9EC3-L003853](../../agents/web_agent.py#L3853) | 3853 | `"                }"` | — |
| [SRC-1AE03B9EC3-L003854](../../agents/web_agent.py#L3854) | 3854 | `""` | — |
| [SRC-1AE03B9EC3-L003855](../../agents/web_agent.py#L3855) | 3855 | `"        report[\"model_usage\"] = list(self.model_usage)"` | — |
| [SRC-1AE03B9EC3-L003856](../../agents/web_agent.py#L3856) | 3856 | `"        report[\"elapsed_ms\"] = round((time.monotonic() - started) * 1000)"` | — |
| [SRC-1AE03B9EC3-L003857](../../agents/web_agent.py#L3857) | 3857 | `"        statuses = [check.get(\"status\") for check in report[\"checks\"].values()]"` | — |
| [SRC-1AE03B9EC3-L003858](../../agents/web_agent.py#L3858) | 3858 | `"        report[\"overall_status\"] = ("` | — |
| [SRC-1AE03B9EC3-L003859](../../agents/web_agent.py#L3859) | 3859 | `"            \"passed\""` | — |
| [SRC-1AE03B9EC3-L003860](../../agents/web_agent.py#L3860) | 3860 | `"            if all(status in {\"passed\", \"skipped\"} for status in statuses)"` | — |
| [SRC-1AE03B9EC3-L003861](../../agents/web_agent.py#L3861) | 3861 | `"            else \"degraded\""` | — |
| [SRC-1AE03B9EC3-L003862](../../agents/web_agent.py#L3862) | 3862 | `"            if any(status in {\"passed\", \"degraded\"} for status in statuses)"` | — |
| [SRC-1AE03B9EC3-L003863](../../agents/web_agent.py#L3863) | 3863 | `"            else \"failed\""` | — |
| [SRC-1AE03B9EC3-L003864](../../agents/web_agent.py#L3864) | 3864 | `"        )"` | — |
| [SRC-1AE03B9EC3-L003865](../../agents/web_agent.py#L3865) | 3865 | `"        return report"` | — |
| [SRC-1AE03B9EC3-L003866](../../agents/web_agent.py#L3866) | 3866 | `""` | — |
| [SRC-1AE03B9EC3-L003867](../../agents/web_agent.py#L3867) | 3867 | `"    def answer("` | — |
| [SRC-1AE03B9EC3-L003868](../../agents/web_agent.py#L3868) | 3868 | `"        self, question: str, history: Any = None, mode: str = \"auto\""` | — |
| [SRC-1AE03B9EC3-L003869](../../agents/web_agent.py#L3869) | 3869 | `"    ) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L003870](../../agents/web_agent.py#L3870) | 3870 | `"        \"\"\"Run one answer with an isolated, observable resource budget.\"\"\""` | — |
| [SRC-1AE03B9EC3-L003871](../../agents/web_agent.py#L3871) | 3871 | `"        previous_budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L003872](../../agents/web_agent.py#L3872) | 3872 | `"        self.generation_diagnostics = []"` | — |
| [SRC-1AE03B9EC3-L003873](../../agents/web_agent.py#L3873) | 3873 | `"        self._generation_attempt_sequence = 0"` | — |
| [SRC-1AE03B9EC3-L003874](../../agents/web_agent.py#L3874) | 3874 | `"        budget = RequestBudget.from_environment()"` | — |
| [SRC-1AE03B9EC3-L003875](../../agents/web_agent.py#L3875) | 3875 | `"        self._request_budget = budget"` | — |
| [SRC-1AE03B9EC3-L003876](../../agents/web_agent.py#L3876) | 3876 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L003877](../../agents/web_agent.py#L3877) | 3877 | `"            result = self._answer_with_budget(question, history, mode)"` | — |
| [SRC-1AE03B9EC3-L003878](../../agents/web_agent.py#L3878) | 3878 | `"        except RequestBudgetExceeded as exc:"` | — |
| [SRC-1AE03B9EC3-L003879](../../agents/web_agent.py#L3879) | 3879 | `"            safe_question = ("` | — |
| [SRC-1AE03B9EC3-L003880](../../agents/web_agent.py#L3880) | 3880 | `"                question.strip()[:MAX_QUESTION_CHARS]"` | — |
| [SRC-1AE03B9EC3-L003881](../../agents/web_agent.py#L3881) | 3881 | `"                if isinstance(question, str)"` | — |
| [SRC-1AE03B9EC3-L003882](../../agents/web_agent.py#L3882) | 3882 | `"                else \"\""` | — |
| [SRC-1AE03B9EC3-L003883](../../agents/web_agent.py#L3883) | 3883 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003884](../../agents/web_agent.py#L3884) | 3884 | `"            budget_at_failure = budget.snapshot()"` | — |
| [SRC-1AE03B9EC3-L003885](../../agents/web_agent.py#L3885) | 3885 | `"            search_attempted = budget_at_failure[\"counts\"][\"search_calls\"] > 0"` | — |
| [SRC-1AE03B9EC3-L003886](../../agents/web_agent.py#L3886) | 3886 | `"            result = {"` | — |
| [SRC-1AE03B9EC3-L003887](../../agents/web_agent.py#L3887) | 3887 | `"                \"answer\": ("` | — |
| [SRC-1AE03B9EC3-L003888](../../agents/web_agent.py#L3888) | 3888 | `"                    \"توقفت العملية لأن ميزانية الوقت أو الموارد المحددة لهذا الطلب \""` | — |
| [SRC-1AE03B9EC3-L003889](../../agents/web_agent.py#L3889) | 3889 | `"                    \"قد استُنفدت. لم أتمكن من إكمال البحث ضمن الحدود الحالية؛ \""` | — |
| [SRC-1AE03B9EC3-L003890](../../agents/web_agent.py#L3890) | 3890 | `"                    \"لا تعتبر هذه النتيجة بحثًا مكتملًا.\""` | — |
| [SRC-1AE03B9EC3-L003891](../../agents/web_agent.py#L3891) | 3891 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L003892](../../agents/web_agent.py#L3892) | 3892 | `"                \"question\": safe_question,"` | — |
| [SRC-1AE03B9EC3-L003893](../../agents/web_agent.py#L3893) | 3893 | `"                \"search_query\": safe_question,"` | — |
| [SRC-1AE03B9EC3-L003894](../../agents/web_agent.py#L3894) | 3894 | `"                \"search_queries\": [],"` | — |
| [SRC-1AE03B9EC3-L003895](../../agents/web_agent.py#L3895) | 3895 | `"                \"search_report\": {"` | — |
| [SRC-1AE03B9EC3-L003896](../../agents/web_agent.py#L3896) | 3896 | `"                    \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L003897](../../agents/web_agent.py#L3897) | 3897 | `"                    \"search_outcome\": ("` | — |
| [SRC-1AE03B9EC3-L003898](../../agents/web_agent.py#L3898) | 3898 | `"                        \"unknown_after_budget_exhaustion\""` | — |
| [SRC-1AE03B9EC3-L003899](../../agents/web_agent.py#L3899) | 3899 | `"                        if search_attempted"` | — |
| [SRC-1AE03B9EC3-L003900](../../agents/web_agent.py#L3900) | 3900 | `"                        else \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L003901](../../agents/web_agent.py#L3901) | 3901 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L003902](../../agents/web_agent.py#L3902) | 3902 | `"                    \"insufficient_evidence\": True,"` | — |
| [SRC-1AE03B9EC3-L003903](../../agents/web_agent.py#L3903) | 3903 | `"                    \"budget_exhausted\": True,"` | — |
| [SRC-1AE03B9EC3-L003904](../../agents/web_agent.py#L3904) | 3904 | `"                    \"warnings\": [str(exc)],"` | — |
| [SRC-1AE03B9EC3-L003905](../../agents/web_agent.py#L3905) | 3905 | `"                },"` | — |
| [SRC-1AE03B9EC3-L003906](../../agents/web_agent.py#L3906) | 3906 | `"                \"sources\": [],"` | — |
| [SRC-1AE03B9EC3-L003907](../../agents/web_agent.py#L3907) | 3907 | `"                \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L003908](../../agents/web_agent.py#L3908) | 3908 | `"                \"citation_validation\": {\"status\": \"not_checked\"},"` | — |
| [SRC-1AE03B9EC3-L003909](../../agents/web_agent.py#L3909) | 3909 | `"                \"answer_coverage\": {},"` | — |
| [SRC-1AE03B9EC3-L003910](../../agents/web_agent.py#L3910) | 3910 | `"                \"used_language_model\": False,"` | — |
| [SRC-1AE03B9EC3-L003911](../../agents/web_agent.py#L3911) | 3911 | `"                \"used_web_search\": False,"` | — |
| [SRC-1AE03B9EC3-L003912](../../agents/web_agent.py#L3912) | 3912 | `"                \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L003913](../../agents/web_agent.py#L3913) | 3913 | `"                \"used_social_search\": False,"` | — |
| [SRC-1AE03B9EC3-L003914](../../agents/web_agent.py#L3914) | 3914 | `"                \"warnings\": [str(exc)],"` | — |
| [SRC-1AE03B9EC3-L003915](../../agents/web_agent.py#L3915) | 3915 | `"                \"kind\": \"web_fallback\","` | — |
| [SRC-1AE03B9EC3-L003916](../../agents/web_agent.py#L3916) | 3916 | `"                \"final_answer_status\": \"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L003917](../../agents/web_agent.py#L3917) | 3917 | `"                \"intent_route\": \"BUDGET_EXHAUSTED\","` | — |
| [SRC-1AE03B9EC3-L003918](../../agents/web_agent.py#L3918) | 3918 | `"                \"intent_route_reason\": \"request_budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L003919](../../agents/web_agent.py#L3919) | 3919 | `"            }"` | — |
| [SRC-1AE03B9EC3-L003920](../../agents/web_agent.py#L3920) | 3920 | `"        finally:"` | — |
| [SRC-1AE03B9EC3-L003921](../../agents/web_agent.py#L3921) | 3921 | `"            budget_summary = budget.snapshot()"` | — |
| [SRC-1AE03B9EC3-L003922](../../agents/web_agent.py#L3922) | 3922 | `"            self._request_budget = previous_budget"` | — |
| [SRC-1AE03B9EC3-L003923](../../agents/web_agent.py#L3923) | 3923 | `""` | — |
| [SRC-1AE03B9EC3-L003924](../../agents/web_agent.py#L3924) | 3924 | `"        result[\"request_budget\"] = budget_summary"` | — |
| [SRC-1AE03B9EC3-L003925](../../agents/web_agent.py#L3925) | 3925 | `"        result[\"generation_diagnostics\"] = list(self.generation_diagnostics[-12:])"` | — |
| [SRC-1AE03B9EC3-L003926](../../agents/web_agent.py#L3926) | 3926 | `""` | — |
| [SRC-1AE03B9EC3-L003927](../../agents/web_agent.py#L3927) | 3927 | `"        # Keep the public result contract resilient if a fallback/alternate result"` | — |
| [SRC-1AE03B9EC3-L003928](../../agents/web_agent.py#L3928) | 3928 | `"        # builder omitted the lexical integrity fields. Normal research results are"` | — |
| [SRC-1AE03B9EC3-L003929](../../agents/web_agent.py#L3929) | 3929 | `"        # already audited inside _answer_with_budget, so do not duplicate that work."` | — |
| [SRC-1AE03B9EC3-L003930](../../agents/web_agent.py#L3930) | 3930 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L003931](../../agents/web_agent.py#L3931) | 3931 | `"            result.get(\"kind\") in {\"web_research\", \"web_fallback\", \"insufficient_evidence\"}"` | — |
| [SRC-1AE03B9EC3-L003932](../../agents/web_agent.py#L3932) | 3932 | `"            and \"answer_integrity\" not in result"` | — |
| [SRC-1AE03B9EC3-L003933](../../agents/web_agent.py#L3933) | 3933 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L003934](../../agents/web_agent.py#L3934) | 3934 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L003935](../../agents/web_agent.py#L3935) | 3935 | `"                coverage_targets = self._question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L003936](../../agents/web_agent.py#L3936) | 3936 | `"                source_rows = result.get(\"sources\")"` | — |
| [SRC-1AE03B9EC3-L003937](../../agents/web_agent.py#L3937) | 3937 | `"                safe_sources = source_rows if isinstance(source_rows, list) else []"` | — |
| [SRC-1AE03B9EC3-L003938](../../agents/web_agent.py#L3938) | 3938 | `"                answer_integrity = audit_answer_integrity("` | — |
| [SRC-1AE03B9EC3-L003939](../../agents/web_agent.py#L3939) | 3939 | `"                    question,"` | — |
| [SRC-1AE03B9EC3-L003940](../../agents/web_agent.py#L3940) | 3940 | `"                    str(result.get(\"answer\") or \"\"),"` | — |
| [SRC-1AE03B9EC3-L003941](../../agents/web_agent.py#L3941) | 3941 | `"                    safe_sources,"` | — |
| [SRC-1AE03B9EC3-L003942](../../agents/web_agent.py#L3942) | 3942 | `"                    coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L003943](../../agents/web_agent.py#L3943) | 3943 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003944](../../agents/web_agent.py#L3944) | 3944 | `"                result[\"answer_integrity\"] = answer_integrity"` | — |
| [SRC-1AE03B9EC3-L003945](../../agents/web_agent.py#L3945) | 3945 | `"                coverage = result.get(\"answer_coverage\")"` | — |
| [SRC-1AE03B9EC3-L003946](../../agents/web_agent.py#L3946) | 3946 | `"                if not isinstance(coverage, dict):"` | — |
| [SRC-1AE03B9EC3-L003947](../../agents/web_agent.py#L3947) | 3947 | `"                    coverage = {}"` | — |
| [SRC-1AE03B9EC3-L003948](../../agents/web_agent.py#L3948) | 3948 | `"                coverage[\"targets\"] = coverage_targets"` | — |
| [SRC-1AE03B9EC3-L003949](../../agents/web_agent.py#L3949) | 3949 | `"                coverage[\"target_checks\"] = answer_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L003950](../../agents/web_agent.py#L3950) | 3950 | `"                coverage[\"potentially_missing_target_count\"] = ("` | — |
| [SRC-1AE03B9EC3-L003951](../../agents/web_agent.py#L3951) | 3951 | `"                    answer_integrity[\"potentially_missing_target_count\"]"` | — |
| [SRC-1AE03B9EC3-L003952](../../agents/web_agent.py#L3952) | 3952 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003953](../../agents/web_agent.py#L3953) | 3953 | `"                coverage[\"source_evidence_gap_count\"] = answer_integrity[\"source_evidence_gap_count\"]"` | — |
| [SRC-1AE03B9EC3-L003954](../../agents/web_agent.py#L3954) | 3954 | `"                coverage[\"lexical_screen_method\"] = ("` | — |
| [SRC-1AE03B9EC3-L003955](../../agents/web_agent.py#L3955) | 3955 | `"                    \"deterministic_lexical_screen_only_not_semantic_grading\""` | — |
| [SRC-1AE03B9EC3-L003956](../../agents/web_agent.py#L3956) | 3956 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003957](../../agents/web_agent.py#L3957) | 3957 | `"                if ("` | — |
| [SRC-1AE03B9EC3-L003958](../../agents/web_agent.py#L3958) | 3958 | `"                    result.get(\"kind\") == \"insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L003959](../../agents/web_agent.py#L3959) | 3959 | `"                    or result.get(\"research_quality\") == \"failed\""` | — |
| [SRC-1AE03B9EC3-L003960](../../agents/web_agent.py#L3960) | 3960 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L003961](../../agents/web_agent.py#L3961) | 3961 | `"                    fulfillment_status = ("` | — |
| [SRC-1AE03B9EC3-L003962](../../agents/web_agent.py#L3962) | 3962 | `"                        \"not_assessed_insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L003963](../../agents/web_agent.py#L3963) | 3963 | `"                        if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L003964](../../agents/web_agent.py#L3964) | 3964 | `"                        else \"not_machine_assessed_no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L003965](../../agents/web_agent.py#L3965) | 3965 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003966](../../agents/web_agent.py#L3966) | 3966 | `"                elif ("` | — |
| [SRC-1AE03B9EC3-L003967](../../agents/web_agent.py#L3967) | 3967 | `"                    answer_integrity[\"potentially_missing_target_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L003968](../../agents/web_agent.py#L3968) | 3968 | `"                    or answer_integrity[\"source_evidence_gap_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L003969](../../agents/web_agent.py#L3969) | 3969 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L003970](../../agents/web_agent.py#L3970) | 3970 | `"                    fulfillment_status = \"possible_gap_detected\""` | — |
| [SRC-1AE03B9EC3-L003971](../../agents/web_agent.py#L3971) | 3971 | `"                elif coverage_targets:"` | — |
| [SRC-1AE03B9EC3-L003972](../../agents/web_agent.py#L3972) | 3972 | `"                    fulfillment_status = \"lexical_signals_found_not_semantically_verified\""` | — |
| [SRC-1AE03B9EC3-L003973](../../agents/web_agent.py#L3973) | 3973 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L003974](../../agents/web_agent.py#L3974) | 3974 | `"                    fulfillment_status = \"not_machine_assessed_no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L003975](../../agents/web_agent.py#L3975) | 3975 | `"                coverage[\"task_fulfillment_status\"] = fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L003976](../../agents/web_agent.py#L3976) | 3976 | `"                result[\"answer_coverage\"] = coverage"` | — |
| [SRC-1AE03B9EC3-L003977](../../agents/web_agent.py#L3977) | 3977 | `"                result[\"task_fulfillment_status\"] = fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L003978](../../agents/web_agent.py#L3978) | 3978 | `"                if isinstance(result.get(\"search_report\"), dict):"` | — |
| [SRC-1AE03B9EC3-L003979](../../agents/web_agent.py#L3979) | 3979 | `"                    result[\"search_report\"][\"answer_integrity\"] = answer_integrity"` | — |
| [SRC-1AE03B9EC3-L003980](../../agents/web_agent.py#L3980) | 3980 | `"                    result[\"search_report\"][\"task_fulfillment_status\"] = fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L003981](../../agents/web_agent.py#L3981) | 3981 | `"            except (AttributeError, KeyError, TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L003982](../../agents/web_agent.py#L3982) | 3982 | `"                # Auxiliary integrity screening never replaces the actual answer."` | — |
| [SRC-1AE03B9EC3-L003983](../../agents/web_agent.py#L3983) | 3983 | `"                result[\"answer_integrity\"] = {"` | — |
| [SRC-1AE03B9EC3-L003984](../../agents/web_agent.py#L3984) | 3984 | `"                    \"method\": \"deterministic_lexical_screen_only\","` | — |
| [SRC-1AE03B9EC3-L003985](../../agents/web_agent.py#L3985) | 3985 | `"                    \"status\": \"not_run\","` | — |
| [SRC-1AE03B9EC3-L003986](../../agents/web_agent.py#L3986) | 3986 | `"                    \"semantic_verification\": False,"` | — |
| [SRC-1AE03B9EC3-L003987](../../agents/web_agent.py#L3987) | 3987 | `"                    \"independent_fact_check\": False,"` | — |
| [SRC-1AE03B9EC3-L003988](../../agents/web_agent.py#L3988) | 3988 | `"                    \"error_class\": \"integrity_screen_error\","` | — |
| [SRC-1AE03B9EC3-L003989](../../agents/web_agent.py#L3989) | 3989 | `"                }"` | — |
| [SRC-1AE03B9EC3-L003990](../../agents/web_agent.py#L3990) | 3990 | `"                result.setdefault(\"warnings\", []).append("` | — |
| [SRC-1AE03B9EC3-L003991](../../agents/web_agent.py#L3991) | 3991 | `"                    \"تعذر تشغيل الفحص اللفظي الأولي لسلامة الأدلة؛ لم يُعدّ ذلك إثباتًا أو نفيًا لصحة الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L003992](../../agents/web_agent.py#L3992) | 3992 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003993](../../agents/web_agent.py#L3993) | 3993 | `"        if \"final_answer_status\" not in result:"` | — |
| [SRC-1AE03B9EC3-L003994](../../agents/web_agent.py#L3994) | 3994 | `"            if result.get(\"kind\") in {\"capability_answer\", \"local_conversation\"}:"` | — |
| [SRC-1AE03B9EC3-L003995](../../agents/web_agent.py#L3995) | 3995 | `"                final_answer_status = \"local_response_no_generation\""` | — |
| [SRC-1AE03B9EC3-L003996](../../agents/web_agent.py#L3996) | 3996 | `"            elif result.get(\"kind\") == \"insufficient_evidence\":"` | — |
| [SRC-1AE03B9EC3-L003997](../../agents/web_agent.py#L3997) | 3997 | `"                final_answer_status = \"insufficient_evidence_no_generation\""` | — |
| [SRC-1AE03B9EC3-L003998](../../agents/web_agent.py#L3998) | 3998 | `"            elif result.get(\"used_language_model\") is True:"` | — |
| [SRC-1AE03B9EC3-L003999](../../agents/web_agent.py#L3999) | 3999 | `"                final_answer_status = \"model_answer_generated\""` | — |
| [SRC-1AE03B9EC3-L004000](../../agents/web_agent.py#L4000) | 4000 | `"            elif self.generation_diagnostics:"` | — |
| [SRC-1AE03B9EC3-L004001](../../agents/web_agent.py#L4001) | 4001 | `"                final_answer_status = ("` | — |
| [SRC-1AE03B9EC3-L004002](../../agents/web_agent.py#L4002) | 4002 | `"                    \"generation_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L004003](../../agents/web_agent.py#L4003) | 4003 | `"                    if result.get(\"sources\")"` | — |
| [SRC-1AE03B9EC3-L004004](../../agents/web_agent.py#L4004) | 4004 | `"                    else \"generation_failed\""` | — |
| [SRC-1AE03B9EC3-L004005](../../agents/web_agent.py#L4005) | 4005 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004006](../../agents/web_agent.py#L4006) | 4006 | `"            elif result.get(\"kind\") == \"clarification\":"` | — |
| [SRC-1AE03B9EC3-L004007](../../agents/web_agent.py#L4007) | 4007 | `"                final_answer_status = \"clarification_required\""` | — |
| [SRC-1AE03B9EC3-L004008](../../agents/web_agent.py#L4008) | 4008 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L004009](../../agents/web_agent.py#L4009) | 4009 | `"                final_answer_status = \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L004010](../../agents/web_agent.py#L4010) | 4010 | `"            result[\"final_answer_status\"] = final_answer_status"` | — |
| [SRC-1AE03B9EC3-L004011](../../agents/web_agent.py#L4011) | 4011 | `"        if isinstance(result.get(\"search_report\"), dict):"` | — |
| [SRC-1AE03B9EC3-L004012](../../agents/web_agent.py#L4012) | 4012 | `"            result[\"search_report\"][\"request_budget\"] = budget_summary"` | — |
| [SRC-1AE03B9EC3-L004013](../../agents/web_agent.py#L4013) | 4013 | `"        if budget_summary[\"deadline_exceeded\"]:"` | — |
| [SRC-1AE03B9EC3-L004014](../../agents/web_agent.py#L4014) | 4014 | `"            result.setdefault(\"warnings\", []).append("` | — |
| [SRC-1AE03B9EC3-L004015](../../agents/web_agent.py#L4015) | 4015 | `"                \"انتهت نافذة الوقت المحددة للطلب أو جرى تجاوزها قليلًا أثناء إنهاء اتصال جارٍ.\""` | — |
| [SRC-1AE03B9EC3-L004016](../../agents/web_agent.py#L4016) | 4016 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004017](../../agents/web_agent.py#L4017) | 4017 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L004018](../../agents/web_agent.py#L4018) | 4018 | `""` | — |
| [SRC-1AE03B9EC3-L004019](../../agents/web_agent.py#L4019) | 4019 | `"    def _answer_with_budget("` | — |
| [SRC-1AE03B9EC3-L004020](../../agents/web_agent.py#L4020) | 4020 | `"        self, question: str, history: Any = None, mode: str = \"auto\""` | — |
| [SRC-1AE03B9EC3-L004021](../../agents/web_agent.py#L4021) | 4021 | `"    ) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L004022](../../agents/web_agent.py#L4022) | 4022 | `"        if not isinstance(question, str) or not question.strip():"` | — |
| [SRC-1AE03B9EC3-L004023](../../agents/web_agent.py#L4023) | 4023 | `"            raise ValueError(\"اكتب سؤالًا غير فارغ.\")"` | — |
| [SRC-1AE03B9EC3-L004024](../../agents/web_agent.py#L4024) | 4024 | `"        question = question.strip()"` | — |
| [SRC-1AE03B9EC3-L004025](../../agents/web_agent.py#L4025) | 4025 | `"        if len(question) > MAX_QUESTION_CHARS:"` | — |
| [SRC-1AE03B9EC3-L004026](../../agents/web_agent.py#L4026) | 4026 | `"            raise ValueError(f\"السؤال طويل جدًا؛ الحد الأقصى {MAX_QUESTION_CHARS} حرف.\")"` | — |
| [SRC-1AE03B9EC3-L004027](../../agents/web_agent.py#L4027) | 4027 | `"        clean_history = self._sanitize_history(history)"` | — |
| [SRC-1AE03B9EC3-L004028](../../agents/web_agent.py#L4028) | 4028 | `"        # Resolve elliptical follow-ups once and carry the resolved intent through"` | — |
| [SRC-1AE03B9EC3-L004029](../../agents/web_agent.py#L4029) | 4029 | ``"        # planning, generation, review, and evidence checks. Keep `question` intact"`` | — |
| [SRC-1AE03B9EC3-L004030](../../agents/web_agent.py#L4030) | 4030 | `"        # for the public response contract and initial intent routing."` | — |
| [SRC-1AE03B9EC3-L004031](../../agents/web_agent.py#L4031) | 4031 | `"        working_question = self._history_search_query(question, clean_history) or question"` | — |
| [SRC-1AE03B9EC3-L004032](../../agents/web_agent.py#L4032) | 4032 | `"        if not isinstance(working_question, str) or not working_question.strip():"` | — |
| [SRC-1AE03B9EC3-L004033](../../agents/web_agent.py#L4033) | 4033 | `"            working_question = question"` | — |
| [SRC-1AE03B9EC3-L004034](../../agents/web_agent.py#L4034) | 4034 | `"        self._reset_deepseek_search_budget()"` | — |
| [SRC-1AE03B9EC3-L004035](../../agents/web_agent.py#L4035) | 4035 | `"        self.server_search_sources = []"` | — |
| [SRC-1AE03B9EC3-L004036](../../agents/web_agent.py#L4036) | 4036 | `"        self.model_usage = []"` | — |
| [SRC-1AE03B9EC3-L004037](../../agents/web_agent.py#L4037) | 4037 | `"        self.generation_diagnostics = []"` | — |
| [SRC-1AE03B9EC3-L004038](../../agents/web_agent.py#L4038) | 4038 | `"        with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L004039](../../agents/web_agent.py#L4039) | 4039 | `"            self._provider_diagnostics = []"` | — |
| [SRC-1AE03B9EC3-L004040](../../agents/web_agent.py#L4040) | 4040 | `"        clean_mode = mode.strip().lower() if isinstance(mode, str) else \"auto\""` | — |
| [SRC-1AE03B9EC3-L004041](../../agents/web_agent.py#L4041) | 4041 | `"        if clean_mode not in {\"auto\", \"deep\", \"latest\", \"social\"}:"` | — |
| [SRC-1AE03B9EC3-L004042](../../agents/web_agent.py#L4042) | 4042 | `"            raise ValueError(\"نمط البحث غير مدعوم. اختر auto أو deep أو latest أو social.\")"` | — |
| [SRC-1AE03B9EC3-L004043](../../agents/web_agent.py#L4043) | 4043 | `"        current_search_status_question = self._is_current_search_status_question(question)"` | — |
| [SRC-1AE03B9EC3-L004044](../../agents/web_agent.py#L4044) | 4044 | `"        # Explicit UI modes control research tasks, but must not turn a status"` | — |
| [SRC-1AE03B9EC3-L004045](../../agents/web_agent.py#L4045) | 4045 | `"        # question about this answer into a new web-search request."` | — |
| [SRC-1AE03B9EC3-L004046](../../agents/web_agent.py#L4046) | 4046 | `"        routing_mode = \"auto\" if current_search_status_question else clean_mode"` | — |
| [SRC-1AE03B9EC3-L004047](../../agents/web_agent.py#L4047) | 4047 | `"        decision = route_intent("` | — |
| [SRC-1AE03B9EC3-L004048](../../agents/web_agent.py#L4048) | 4048 | `"            question,"` | — |
| [SRC-1AE03B9EC3-L004049](../../agents/web_agent.py#L4049) | 4049 | `"            clean_history,"` | — |
| [SRC-1AE03B9EC3-L004050](../../agents/web_agent.py#L4050) | 4050 | `"            routing_mode,"` | — |
| [SRC-1AE03B9EC3-L004051](../../agents/web_agent.py#L4051) | 4051 | `"            capability_question=self._is_self_question(question),"` | — |
| [SRC-1AE03B9EC3-L004052](../../agents/web_agent.py#L4052) | 4052 | `"            requires_web=self._requires_web_research(question, routing_mode),"` | — |
| [SRC-1AE03B9EC3-L004053](../../agents/web_agent.py#L4053) | 4053 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004054](../../agents/web_agent.py#L4054) | 4054 | `"        intent_route = str(decision[\"route\"])"` | — |
| [SRC-1AE03B9EC3-L004055](../../agents/web_agent.py#L4055) | 4055 | `"        intent_reason = str(decision[\"reason\"])"` | — |
| [SRC-1AE03B9EC3-L004056](../../agents/web_agent.py#L4056) | 4056 | `"        context_override: dict[str, Any] \| None = None"` | — |
| [SRC-1AE03B9EC3-L004057](../../agents/web_agent.py#L4057) | 4057 | `""` | — |
| [SRC-1AE03B9EC3-L004058](../../agents/web_agent.py#L4058) | 4058 | `"        # Rules only decide when a context probe may be needed. The model interprets"` | — |
| [SRC-1AE03B9EC3-L004059](../../agents/web_agent.py#L4059) | 4059 | `"        # meaning only on those turns; it never receives authority to execute tools."` | — |
| [SRC-1AE03B9EC3-L004060](../../agents/web_agent.py#L4060) | 4060 | `"        probe_dialogue = bool(clean_history) and ("` | — |
| [SRC-1AE03B9EC3-L004061](../../agents/web_agent.py#L4061) | 4061 | `"            intent_route == \"CLARIFY\""` | — |
| [SRC-1AE03B9EC3-L004062](../../agents/web_agent.py#L4062) | 4062 | `"            or (intent_route == \"MODEL_ONLY\" and might_be_context_dependent(question))"` | — |
| [SRC-1AE03B9EC3-L004063](../../agents/web_agent.py#L4063) | 4063 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004064](../../agents/web_agent.py#L4064) | 4064 | `"        if probe_dialogue:"` | — |
| [SRC-1AE03B9EC3-L004065](../../agents/web_agent.py#L4065) | 4065 | `"            semantic_context = self._resolve_dialogue_context(question, clean_history)"` | — |
| [SRC-1AE03B9EC3-L004066](../../agents/web_agent.py#L4066) | 4066 | `"            if semantic_context.get(\"method\") == \"llm_semantic_context\":"` | — |
| [SRC-1AE03B9EC3-L004067](../../agents/web_agent.py#L4067) | 4067 | `"                context_override = semantic_context"` | — |
| [SRC-1AE03B9EC3-L004068](../../agents/web_agent.py#L4068) | 4068 | `"                if semantic_context.get(\"needs_clarification\"):"` | — |
| [SRC-1AE03B9EC3-L004069](../../agents/web_agent.py#L4069) | 4069 | `"                    return self._dialogue_clarification_result("` | — |
| [SRC-1AE03B9EC3-L004070](../../agents/web_agent.py#L4070) | 4070 | `"                        question, clean_mode, semantic_context,"` | — |
| [SRC-1AE03B9EC3-L004071](../../agents/web_agent.py#L4071) | 4071 | `"                        \"semantic_context_has_unresolved_referent\","` | — |
| [SRC-1AE03B9EC3-L004072](../../agents/web_agent.py#L4072) | 4072 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004073](../../agents/web_agent.py#L4073) | 4073 | `"                working_question = ("` | — |
| [SRC-1AE03B9EC3-L004074](../../agents/web_agent.py#L4074) | 4074 | `"                    question if semantic_context.get(\"topic_shift\")"` | — |
| [SRC-1AE03B9EC3-L004075](../../agents/web_agent.py#L4075) | 4075 | `"                    else semantic_context.get(\"resolved_question\") or question"` | — |
| [SRC-1AE03B9EC3-L004076](../../agents/web_agent.py#L4076) | 4076 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004077](../../agents/web_agent.py#L4077) | 4077 | `"                semantic_decision = route_intent("` | — |
| [SRC-1AE03B9EC3-L004078](../../agents/web_agent.py#L4078) | 4078 | `"                    working_question,"` | — |
| [SRC-1AE03B9EC3-L004079](../../agents/web_agent.py#L4079) | 4079 | `"                    clean_history,"` | — |
| [SRC-1AE03B9EC3-L004080](../../agents/web_agent.py#L4080) | 4080 | `"                    routing_mode,"` | — |
| [SRC-1AE03B9EC3-L004081](../../agents/web_agent.py#L4081) | 4081 | `"                    capability_question=self._is_self_question(working_question),"` | — |
| [SRC-1AE03B9EC3-L004082](../../agents/web_agent.py#L4082) | 4082 | `"                    requires_web=("` | — |
| [SRC-1AE03B9EC3-L004083](../../agents/web_agent.py#L4083) | 4083 | `"                        bool(semantic_context.get(\"needs_web\"))"` | — |
| [SRC-1AE03B9EC3-L004084](../../agents/web_agent.py#L4084) | 4084 | `"                        or self._requires_web_research(working_question, routing_mode)"` | — |
| [SRC-1AE03B9EC3-L004085](../../agents/web_agent.py#L4085) | 4085 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L004086](../../agents/web_agent.py#L4086) | 4086 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004087](../../agents/web_agent.py#L4087) | 4087 | `"                if semantic_context.get(\"needs_web\") and routing_mode == \"auto\":"` | — |
| [SRC-1AE03B9EC3-L004088](../../agents/web_agent.py#L4088) | 4088 | `"                    deep_intents = {\"compare\", \"social_opinions\", \"lead_generation\"}"` | — |
| [SRC-1AE03B9EC3-L004089](../../agents/web_agent.py#L4089) | 4089 | `"                    intent_route = ("` | — |
| [SRC-1AE03B9EC3-L004090](../../agents/web_agent.py#L4090) | 4090 | `"                        \"WEB_DEEP\""` | — |
| [SRC-1AE03B9EC3-L004091](../../agents/web_agent.py#L4091) | 4091 | `"                        if semantic_context.get(\"research_depth\") == \"deep\""` | — |
| [SRC-1AE03B9EC3-L004092](../../agents/web_agent.py#L4092) | 4092 | `"                        or semantic_context.get(\"intent\") in deep_intents"` | — |
| [SRC-1AE03B9EC3-L004093](../../agents/web_agent.py#L4093) | 4093 | `"                        else \"WEB_SIMPLE\""` | — |
| [SRC-1AE03B9EC3-L004094](../../agents/web_agent.py#L4094) | 4094 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004095](../../agents/web_agent.py#L4095) | 4095 | `"                    intent_reason = \"semantic_dialogue_context_requires_web\""` | — |
| [SRC-1AE03B9EC3-L004096](../../agents/web_agent.py#L4096) | 4096 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L004097](../../agents/web_agent.py#L4097) | 4097 | `"                    intent_route = str(semantic_decision[\"route\"])"` | — |
| [SRC-1AE03B9EC3-L004098](../../agents/web_agent.py#L4098) | 4098 | `"                    intent_reason = \"semantic_dialogue_context_\" + str(semantic_decision[\"reason\"])"` | — |
| [SRC-1AE03B9EC3-L004099](../../agents/web_agent.py#L4099) | 4099 | `"                decision = semantic_decision"` | — |
| [SRC-1AE03B9EC3-L004100](../../agents/web_agent.py#L4100) | 4100 | `""` | — |
| [SRC-1AE03B9EC3-L004101](../../agents/web_agent.py#L4101) | 4101 | `"        if intent_route == \"LOCAL\":"` | — |
| [SRC-1AE03B9EC3-L004102](../../agents/web_agent.py#L4102) | 4102 | `"            if self._is_self_question(question):"` | — |
| [SRC-1AE03B9EC3-L004103](../../agents/web_agent.py#L4103) | 4103 | `"                local_result = self._self_description_answer(question)"` | — |
| [SRC-1AE03B9EC3-L004104](../../agents/web_agent.py#L4104) | 4104 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L004105](../../agents/web_agent.py#L4105) | 4105 | `"                local_result = self._local_answer_result("` | — |
| [SRC-1AE03B9EC3-L004106](../../agents/web_agent.py#L4106) | 4106 | `"                    question, self._local_conversation_reply(question), \"local_conversation\""` | — |
| [SRC-1AE03B9EC3-L004107](../../agents/web_agent.py#L4107) | 4107 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004108](../../agents/web_agent.py#L4108) | 4108 | `"            return self._annotate_intent_route("` | — |
| [SRC-1AE03B9EC3-L004109](../../agents/web_agent.py#L4109) | 4109 | `"                local_result, intent_route, intent_reason, clean_mode"` | — |
| [SRC-1AE03B9EC3-L004110](../../agents/web_agent.py#L4110) | 4110 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004111](../../agents/web_agent.py#L4111) | 4111 | `""` | — |
| [SRC-1AE03B9EC3-L004112](../../agents/web_agent.py#L4112) | 4112 | `"        if intent_route == \"CLARIFY\":"` | — |
| [SRC-1AE03B9EC3-L004113](../../agents/web_agent.py#L4113) | 4113 | `"            if context_override is not None:"` | — |
| [SRC-1AE03B9EC3-L004114](../../agents/web_agent.py#L4114) | 4114 | `"                return self._dialogue_clarification_result("` | — |
| [SRC-1AE03B9EC3-L004115](../../agents/web_agent.py#L4115) | 4115 | `"                    question, clean_mode, context_override, intent_reason"` | — |
| [SRC-1AE03B9EC3-L004116](../../agents/web_agent.py#L4116) | 4116 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004117](../../agents/web_agent.py#L4117) | 4117 | `"            return self._clarification_result(question, clean_mode, decision)"` | — |
| [SRC-1AE03B9EC3-L004118](../../agents/web_agent.py#L4118) | 4118 | `""` | — |
| [SRC-1AE03B9EC3-L004119](../../agents/web_agent.py#L4119) | 4119 | `"        if intent_route == \"MODEL_ONLY\":"` | — |
| [SRC-1AE03B9EC3-L004120](../../agents/web_agent.py#L4120) | 4120 | `"            general_answer = self._answer_without_search(working_question, clean_history)"` | — |
| [SRC-1AE03B9EC3-L004121](../../agents/web_agent.py#L4121) | 4121 | `"            if general_answer is not None:"` | — |
| [SRC-1AE03B9EC3-L004122](../../agents/web_agent.py#L4122) | 4122 | `"                return self._annotate_intent_route("` | — |
| [SRC-1AE03B9EC3-L004123](../../agents/web_agent.py#L4123) | 4123 | `"                    general_answer, intent_route, intent_reason, clean_mode"` | — |
| [SRC-1AE03B9EC3-L004124](../../agents/web_agent.py#L4124) | 4124 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004125](../../agents/web_agent.py#L4125) | 4125 | `"            # Preserve the existing degraded-mode behavior when generation is unavailable:"` | — |
| [SRC-1AE03B9EC3-L004126](../../agents/web_agent.py#L4126) | 4126 | `"            # run the current web pipeline rather than fabricate a model-only answer."` | — |
| [SRC-1AE03B9EC3-L004127](../../agents/web_agent.py#L4127) | 4127 | `"            intent_route = \"WEB_SIMPLE\""` | — |
| [SRC-1AE03B9EC3-L004128](../../agents/web_agent.py#L4128) | 4128 | `"            intent_reason = \"model_unavailable_fallback_to_existing_web_research\""` | — |
| [SRC-1AE03B9EC3-L004129](../../agents/web_agent.py#L4129) | 4129 | `""` | — |
| [SRC-1AE03B9EC3-L004130](../../agents/web_agent.py#L4130) | 4130 | `"        plan = self._plan_search("` | — |
| [SRC-1AE03B9EC3-L004131](../../agents/web_agent.py#L4131) | 4131 | `"            question, clean_history, context_override=context_override"` | — |
| [SRC-1AE03B9EC3-L004132](../../agents/web_agent.py#L4132) | 4132 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004133](../../agents/web_agent.py#L4133) | 4133 | `"        dialogue_context = plan.get(\"dialogue_context\")"` | — |
| [SRC-1AE03B9EC3-L004134](../../agents/web_agent.py#L4134) | 4134 | `"        if isinstance(dialogue_context, dict):"` | — |
| [SRC-1AE03B9EC3-L004135](../../agents/web_agent.py#L4135) | 4135 | `"            if dialogue_context.get(\"needs_clarification\"):"` | — |
| [SRC-1AE03B9EC3-L004136](../../agents/web_agent.py#L4136) | 4136 | `"                return self._dialogue_clarification_result("` | — |
| [SRC-1AE03B9EC3-L004137](../../agents/web_agent.py#L4137) | 4137 | `"                    question, clean_mode, dialogue_context,"` | — |
| [SRC-1AE03B9EC3-L004138](../../agents/web_agent.py#L4138) | 4138 | `"                    \"planner_detected_unresolved_referent\","` | — |
| [SRC-1AE03B9EC3-L004139](../../agents/web_agent.py#L4139) | 4139 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004140](../../agents/web_agent.py#L4140) | 4140 | `"            working_question = ("` | — |
| [SRC-1AE03B9EC3-L004141](../../agents/web_agent.py#L4141) | 4141 | `"                question if dialogue_context.get(\"topic_shift\")"` | — |
| [SRC-1AE03B9EC3-L004142](../../agents/web_agent.py#L4142) | 4142 | `"                else dialogue_context.get(\"resolved_question\") or working_question"` | — |
| [SRC-1AE03B9EC3-L004143](../../agents/web_agent.py#L4143) | 4143 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004144](../../agents/web_agent.py#L4144) | 4144 | `"        plan[\"mode\"] = clean_mode"` | — |
| [SRC-1AE03B9EC3-L004145](../../agents/web_agent.py#L4145) | 4145 | `"        plan[\"intent_route\"] = intent_route"` | — |
| [SRC-1AE03B9EC3-L004146](../../agents/web_agent.py#L4146) | 4146 | `"        plan[\"intent_route_reason\"] = intent_reason"` | — |
| [SRC-1AE03B9EC3-L004147](../../agents/web_agent.py#L4147) | 4147 | `"        # Normalize planner output before depth/mode expansion so a raw instruction-only"` | — |
| [SRC-1AE03B9EC3-L004148](../../agents/web_agent.py#L4148) | 4148 | `"        # prompt cannot seed synthetic generic queries when the topic is empty."` | — |
| [SRC-1AE03B9EC3-L004149](../../agents/web_agent.py#L4149) | 4149 | `"        raw_plan_queries = plan.get(\"queries\") or []"` | — |
| [SRC-1AE03B9EC3-L004150](../../agents/web_agent.py#L4150) | 4150 | `"        if not isinstance(raw_plan_queries, list):"` | — |
| [SRC-1AE03B9EC3-L004151](../../agents/web_agent.py#L4151) | 4151 | `"            raw_plan_queries = []"` | — |
| [SRC-1AE03B9EC3-L004152](../../agents/web_agent.py#L4152) | 4152 | `"        normalized_plan_queries = []"` | — |
| [SRC-1AE03B9EC3-L004153](../../agents/web_agent.py#L4153) | 4153 | `"        for raw_query in raw_plan_queries:"` | — |
| [SRC-1AE03B9EC3-L004154](../../agents/web_agent.py#L4154) | 4154 | `"            if not isinstance(raw_query, str) or not raw_query.strip():"` | — |
| [SRC-1AE03B9EC3-L004155](../../agents/web_agent.py#L4155) | 4155 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L004156](../../agents/web_agent.py#L4156) | 4156 | `"            compacted_query = compact_search_query(raw_query)"` | — |
| [SRC-1AE03B9EC3-L004157](../../agents/web_agent.py#L4157) | 4157 | `"            if ("` | — |
| [SRC-1AE03B9EC3-L004158](../../agents/web_agent.py#L4158) | 4158 | `"                compacted_query"` | — |
| [SRC-1AE03B9EC3-L004159](../../agents/web_agent.py#L4159) | 4159 | `"                and _relevance_query_tokens(compacted_query)"` | — |
| [SRC-1AE03B9EC3-L004160](../../agents/web_agent.py#L4160) | 4160 | `"                and compacted_query not in normalized_plan_queries"` | — |
| [SRC-1AE03B9EC3-L004161](../../agents/web_agent.py#L4161) | 4161 | `"            ):"` | — |
| [SRC-1AE03B9EC3-L004162](../../agents/web_agent.py#L4162) | 4162 | `"                normalized_plan_queries.append(compacted_query)"` | — |
| [SRC-1AE03B9EC3-L004163](../../agents/web_agent.py#L4163) | 4163 | `"        plan[\"queries\"] = normalized_plan_queries[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004164](../../agents/web_agent.py#L4164) | 4164 | `"        # Preserve the requested mode in diagnostics even when no usable query exists."` | — |
| [SRC-1AE03B9EC3-L004165](../../agents/web_agent.py#L4165) | 4165 | `"        if clean_mode == \"deep\":"` | — |
| [SRC-1AE03B9EC3-L004166](../../agents/web_agent.py#L4166) | 4166 | `"            plan[\"depth\"] = \"deep\""` | — |
| [SRC-1AE03B9EC3-L004167](../../agents/web_agent.py#L4167) | 4167 | `"        elif clean_mode == \"latest\":"` | — |
| [SRC-1AE03B9EC3-L004168](../../agents/web_agent.py#L4168) | 4168 | `"            plan[\"freshness\"] = \"current\""` | — |
| [SRC-1AE03B9EC3-L004169](../../agents/web_agent.py#L4169) | 4169 | `"        elif clean_mode == \"social\":"` | — |
| [SRC-1AE03B9EC3-L004170](../../agents/web_agent.py#L4170) | 4170 | `"            plan[\"social_focus\"] = True"` | — |
| [SRC-1AE03B9EC3-L004171](../../agents/web_agent.py#L4171) | 4171 | `"            if not plan.get(\"platforms\"):"` | — |
| [SRC-1AE03B9EC3-L004172](../../agents/web_agent.py#L4172) | 4172 | `"                plan[\"platforms\"] = [\"reddit\", \"bluesky\", \"youtube\"]"` | — |
| [SRC-1AE03B9EC3-L004173](../../agents/web_agent.py#L4173) | 4173 | `""` | — |
| [SRC-1AE03B9EC3-L004174](../../agents/web_agent.py#L4174) | 4174 | `"        if plan.get(\"queries\"):"` | — |
| [SRC-1AE03B9EC3-L004175](../../agents/web_agent.py#L4175) | 4175 | `"            if clean_mode == \"auto\" and intent_route == \"WEB_DEEP\":"` | — |
| [SRC-1AE03B9EC3-L004176](../../agents/web_agent.py#L4176) | 4176 | `"                plan[\"depth\"] = \"deep\""` | — |
| [SRC-1AE03B9EC3-L004177](../../agents/web_agent.py#L4177) | 4177 | `"            if clean_mode == \"auto\":"` | — |
| [SRC-1AE03B9EC3-L004178](../../agents/web_agent.py#L4178) | 4178 | `"                normalized_question = _normalize_search_query(working_question).casefold()"` | — |
| [SRC-1AE03B9EC3-L004179](../../agents/web_agent.py#L4179) | 4179 | `"                deep_terms = ("` | — |
| [SRC-1AE03B9EC3-L004180](../../agents/web_agent.py#L4180) | 4180 | `"                    \"بحث عميق\", \"بحث معمق\", \"بحث شامل\", \"بالتفصيل\", \"قارن\", \"مقارنة\","` | — |
| [SRC-1AE03B9EC3-L004181](../../agents/web_agent.py#L4181) | 4181 | `"                    \"تحقق\", \"استقصاء\", \"deep research\", \"comprehensive\", \"in-depth\", \"compare\","` | — |
| [SRC-1AE03B9EC3-L004182](../../agents/web_agent.py#L4182) | 4182 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004183](../../agents/web_agent.py#L4183) | 4183 | `"                explicit_deep = intent_route == \"WEB_DEEP\" or any("` | — |
| [SRC-1AE03B9EC3-L004184](../../agents/web_agent.py#L4184) | 4184 | `"                    term in normalized_question for term in deep_terms"` | — |
| [SRC-1AE03B9EC3-L004185](../../agents/web_agent.py#L4185) | 4185 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004186](../../agents/web_agent.py#L4186) | 4186 | `"                if not explicit_deep:"` | — |
| [SRC-1AE03B9EC3-L004187](../../agents/web_agent.py#L4187) | 4187 | `"                    # The planner may overclassify short lookups as deep research. Preserve"` | — |
| [SRC-1AE03B9EC3-L004188](../../agents/web_agent.py#L4188) | 4188 | `"                    # the user's actual intent first and cap routine searches to three queries."` | — |
| [SRC-1AE03B9EC3-L004189](../../agents/web_agent.py#L4189) | 4189 | `"                    fallback_plan_queries = ("` | — |
| [SRC-1AE03B9EC3-L004190](../../agents/web_agent.py#L4190) | 4190 | `"                        fallback_plan(working_question, clean_history).get(\"queries\") or []"` | — |
| [SRC-1AE03B9EC3-L004191](../../agents/web_agent.py#L4191) | 4191 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004192](../../agents/web_agent.py#L4192) | 4192 | `"                    fallback_queries = ["` | — |
| [SRC-1AE03B9EC3-L004193](../../agents/web_agent.py#L4193) | 4193 | `"                        compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L004194](../../agents/web_agent.py#L4194) | 4194 | `"                        for query in fallback_plan_queries"` | — |
| [SRC-1AE03B9EC3-L004195](../../agents/web_agent.py#L4195) | 4195 | `"                        if isinstance(query, str)"` | — |
| [SRC-1AE03B9EC3-L004196](../../agents/web_agent.py#L4196) | 4196 | `"                    ]"` | — |
| [SRC-1AE03B9EC3-L004197](../../agents/web_agent.py#L4197) | 4197 | `"                    fallback_queries = [query for query in fallback_queries if query]"` | — |
| [SRC-1AE03B9EC3-L004198](../../agents/web_agent.py#L4198) | 4198 | `"                    model_queries = ["` | — |
| [SRC-1AE03B9EC3-L004199](../../agents/web_agent.py#L4199) | 4199 | `"                        compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L004200](../../agents/web_agent.py#L4200) | 4200 | `"                        for query in (plan.get(\"queries\") or [])"` | — |
| [SRC-1AE03B9EC3-L004201](../../agents/web_agent.py#L4201) | 4201 | `"                        if isinstance(query, str)"` | — |
| [SRC-1AE03B9EC3-L004202](../../agents/web_agent.py#L4202) | 4202 | `"                    ]"` | — |
| [SRC-1AE03B9EC3-L004203](../../agents/web_agent.py#L4203) | 4203 | `"                    model_queries = [query for query in model_queries if query]"` | — |
| [SRC-1AE03B9EC3-L004204](../../agents/web_agent.py#L4204) | 4204 | `"                    if self._is_navigation_request(working_question):"` | — |
| [SRC-1AE03B9EC3-L004205](../../agents/web_agent.py#L4205) | 4205 | `"                        navigation_seed = ("` | — |
| [SRC-1AE03B9EC3-L004206](../../agents/web_agent.py#L4206) | 4206 | `"                            fallback_queries[0] if fallback_queries"` | — |
| [SRC-1AE03B9EC3-L004207](../../agents/web_agent.py#L4207) | 4207 | `"                            else model_queries[0] if model_queries"` | — |
| [SRC-1AE03B9EC3-L004208](../../agents/web_agent.py#L4208) | 4208 | `"                            else \"\""` | — |
| [SRC-1AE03B9EC3-L004209](../../agents/web_agent.py#L4209) | 4209 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004210](../../agents/web_agent.py#L4210) | 4210 | `"                        subject = re.sub("` | — |
| [SRC-1AE03B9EC3-L004211](../../agents/web_agent.py#L4211) | 4211 | `"                            r\"^(?:ابحث\|بحث\|دور\|اعثر)\\s+(?:عن\|على)?\\s*\","` | — |
| [SRC-1AE03B9EC3-L004212](../../agents/web_agent.py#L4212) | 4212 | `"                            \"\","` | — |
| [SRC-1AE03B9EC3-L004213](../../agents/web_agent.py#L4213) | 4213 | `"                            navigation_seed,"` | — |
| [SRC-1AE03B9EC3-L004214](../../agents/web_agent.py#L4214) | 4214 | `"                        ).strip()"` | — |
| [SRC-1AE03B9EC3-L004215](../../agents/web_agent.py#L4215) | 4215 | `"                        plan_queries = ("` | — |
| [SRC-1AE03B9EC3-L004216](../../agents/web_agent.py#L4216) | 4216 | `"                            ["` | — |
| [SRC-1AE03B9EC3-L004217](../../agents/web_agent.py#L4217) | 4217 | `"                                subject,"` | — |
| [SRC-1AE03B9EC3-L004218](../../agents/web_agent.py#L4218) | 4218 | `"                                subject + \" الموقع الرسمي\","` | — |
| [SRC-1AE03B9EC3-L004219](../../agents/web_agent.py#L4219) | 4219 | `"                                subject + \" official website\","` | — |
| [SRC-1AE03B9EC3-L004220](../../agents/web_agent.py#L4220) | 4220 | `"                            ]"` | — |
| [SRC-1AE03B9EC3-L004221](../../agents/web_agent.py#L4221) | 4221 | `"                            if subject else []"` | — |
| [SRC-1AE03B9EC3-L004222](../../agents/web_agent.py#L4222) | 4222 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004223](../../agents/web_agent.py#L4223) | 4223 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L004224](../../agents/web_agent.py#L4224) | 4224 | `"                        plan_queries = (fallback_queries[:1] or model_queries[:1]) + model_queries"` | — |
| [SRC-1AE03B9EC3-L004225](../../agents/web_agent.py#L4225) | 4225 | `"                    plan[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L004226](../../agents/web_agent.py#L4226) | 4226 | `"                        query.strip() for query in plan_queries if isinstance(query, str) and query.strip()"` | — |
| [SRC-1AE03B9EC3-L004227](../../agents/web_agent.py#L4227) | 4227 | `"                    ))[:3]"` | — |
| [SRC-1AE03B9EC3-L004228](../../agents/web_agent.py#L4228) | 4228 | `"                    plan[\"depth\"] = \"standard\""` | — |
| [SRC-1AE03B9EC3-L004229](../../agents/web_agent.py#L4229) | 4229 | `"            base_query = (plan.get(\"queries\") or [\"\"])[0]"` | — |
| [SRC-1AE03B9EC3-L004230](../../agents/web_agent.py#L4230) | 4230 | `"            if clean_mode == \"auto\" and intent_route == \"WEB_DEEP\" and base_query:"` | — |
| [SRC-1AE03B9EC3-L004231](../../agents/web_agent.py#L4231) | 4231 | `"                deep_candidates = ["` | — |
| [SRC-1AE03B9EC3-L004232](../../agents/web_agent.py#L4232) | 4232 | `"                    f\"{base_query} official sources evidence\","` | — |
| [SRC-1AE03B9EC3-L004233](../../agents/web_agent.py#L4233) | 4233 | `"                    f\"{base_query} risks limitations alternatives\","` | — |
| [SRC-1AE03B9EC3-L004234](../../agents/web_agent.py#L4234) | 4234 | `"                    f\"{base_query} recent data reviews comparison\","` | — |
| [SRC-1AE03B9EC3-L004235](../../agents/web_agent.py#L4235) | 4235 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004236](../../agents/web_agent.py#L4236) | 4236 | `"                normalized_question = _normalize_search_query(working_question).casefold()"` | — |
| [SRC-1AE03B9EC3-L004237](../../agents/web_agent.py#L4237) | 4237 | `"                property_terms = ("` | — |
| [SRC-1AE03B9EC3-L004238](../../agents/web_agent.py#L4238) | 4238 | `"                    \"شقه\", \"شقق\", \"عقار\", \"عقارات\", \"فيلا\", \"فلل\","` | — |
| [SRC-1AE03B9EC3-L004239](../../agents/web_agent.py#L4239) | 4239 | `"                    \"apartment\", \"apartments\", \"flat\", \"real estate\", \"property\", \"house\", \"villa\","` | — |
| [SRC-1AE03B9EC3-L004240](../../agents/web_agent.py#L4240) | 4240 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004241](../../agents/web_agent.py#L4241) | 4241 | `"                if self._is_listing_discovery(working_question) and any("` | — |
| [SRC-1AE03B9EC3-L004242](../../agents/web_agent.py#L4242) | 4242 | `"                    term in normalized_question for term in property_terms"` | — |
| [SRC-1AE03B9EC3-L004243](../../agents/web_agent.py#L4243) | 4243 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L004244](../../agents/web_agent.py#L4244) | 4244 | `"                    deep_candidates.extend(["` | — |
| [SRC-1AE03B9EC3-L004245](../../agents/web_agent.py#L4245) | 4245 | `"                        f\"{base_query} إعلانات عقارية ومواقع العقارات\","` | — |
| [SRC-1AE03B9EC3-L004246](../../agents/web_agent.py#L4246) | 4246 | `"                        f\"{base_query} متوسط أسعار السوق للمتر\","` | — |
| [SRC-1AE03B9EC3-L004247](../../agents/web_agent.py#L4247) | 4247 | `"                        f\"{base_query} مواصفات الوحدات والمساحات وطرق السداد\","` | — |
| [SRC-1AE03B9EC3-L004248](../../agents/web_agent.py#L4248) | 4248 | `"                    ])"` | — |
| [SRC-1AE03B9EC3-L004249](../../agents/web_agent.py#L4249) | 4249 | `"                # Close the planning loop: give every explicit user criterion its own"` | — |
| [SRC-1AE03B9EC3-L004250](../../agents/web_agent.py#L4250) | 4250 | `"                # query before generic \"deep research\" queries consume the fixed budget."` | — |
| [SRC-1AE03B9EC3-L004251](../../agents/web_agent.py#L4251) | 4251 | `"                # This is a retrieval heuristic, not a guarantee that evidence exists."` | — |
| [SRC-1AE03B9EC3-L004252](../../agents/web_agent.py#L4252) | 4252 | `"                criterion_queries = ["` | — |
| [SRC-1AE03B9EC3-L004253](../../agents/web_agent.py#L4253) | 4253 | `"                    compact_search_query(f\"{base_query} {target} official data specifications\")"` | — |
| [SRC-1AE03B9EC3-L004254](../../agents/web_agent.py#L4254) | 4254 | `"                    for target in self._question_coverage_targets(working_question)"` | — |
| [SRC-1AE03B9EC3-L004255](../../agents/web_agent.py#L4255) | 4255 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004256](../../agents/web_agent.py#L4256) | 4256 | `"                criterion_queries = ["` | — |
| [SRC-1AE03B9EC3-L004257](../../agents/web_agent.py#L4257) | 4257 | `"                    query for query in criterion_queries"` | — |
| [SRC-1AE03B9EC3-L004258](../../agents/web_agent.py#L4258) | 4258 | `"                    if query and _relevance_query_tokens(query)"` | — |
| [SRC-1AE03B9EC3-L004259](../../agents/web_agent.py#L4259) | 4259 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004260](../../agents/web_agent.py#L4260) | 4260 | `"                original_queries = ["` | — |
| [SRC-1AE03B9EC3-L004261](../../agents/web_agent.py#L4261) | 4261 | `"                    query for query in (plan.get(\"queries\") or [])"` | — |
| [SRC-1AE03B9EC3-L004262](../../agents/web_agent.py#L4262) | 4262 | `"                    if isinstance(query, str) and query.strip()"` | — |
| [SRC-1AE03B9EC3-L004263](../../agents/web_agent.py#L4263) | 4263 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004264](../../agents/web_agent.py#L4264) | 4264 | `"                # Each criterion query already contains the base subject. When the"` | — |
| [SRC-1AE03B9EC3-L004265](../../agents/web_agent.py#L4265) | 4265 | `"                # question has many criteria, spend the full bounded budget on those"` | — |
| [SRC-1AE03B9EC3-L004266](../../agents/web_agent.py#L4266) | 4266 | `"                # queries rather than silently dropping later criteria for a base query."` | — |
| [SRC-1AE03B9EC3-L004267](../../agents/web_agent.py#L4267) | 4267 | `"                prioritized_queries = criterion_queries[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004268](../../agents/web_agent.py#L4268) | 4268 | `"                if len(prioritized_queries) < MAX_PLAN_QUERIES:"` | — |
| [SRC-1AE03B9EC3-L004269](../../agents/web_agent.py#L4269) | 4269 | `"                    prioritized_queries += original_queries[:1] + deep_candidates"` | — |
| [SRC-1AE03B9EC3-L004270](../../agents/web_agent.py#L4270) | 4270 | `"                plan[\"queries\"] = list(dict.fromkeys(prioritized_queries))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004271](../../agents/web_agent.py#L4271) | 4271 | `"                base_query = (plan.get(\"queries\") or [\"\"])[0]"` | — |
| [SRC-1AE03B9EC3-L004272](../../agents/web_agent.py#L4272) | 4272 | `"            # Explicit user-selected modes are control inputs. They do not bypass source"` | — |
| [SRC-1AE03B9EC3-L004273](../../agents/web_agent.py#L4273) | 4273 | `"            # validation and never permit private-source access."` | — |
| [SRC-1AE03B9EC3-L004274](../../agents/web_agent.py#L4274) | 4274 | `"            if clean_mode == \"deep\":"` | — |
| [SRC-1AE03B9EC3-L004275](../../agents/web_agent.py#L4275) | 4275 | `"                plan[\"depth\"] = \"deep\""` | — |
| [SRC-1AE03B9EC3-L004276](../../agents/web_agent.py#L4276) | 4276 | `"                candidates = ["` | — |
| [SRC-1AE03B9EC3-L004277](../../agents/web_agent.py#L4277) | 4277 | `"                    f\"{base_query} official sources data reports\","` | — |
| [SRC-1AE03B9EC3-L004278](../../agents/web_agent.py#L4278) | 4278 | `"                    f\"{base_query} risks limitations alternatives\","` | — |
| [SRC-1AE03B9EC3-L004279](../../agents/web_agent.py#L4279) | 4279 | `"                    f\"{base_query} case studies recent analysis\","` | — |
| [SRC-1AE03B9EC3-L004280](../../agents/web_agent.py#L4280) | 4280 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004281](../../agents/web_agent.py#L4281) | 4281 | `"                normalized_question = _normalize_search_query(working_question).casefold()"` | — |
| [SRC-1AE03B9EC3-L004282](../../agents/web_agent.py#L4282) | 4282 | `"                property_terms = ("` | — |
| [SRC-1AE03B9EC3-L004283](../../agents/web_agent.py#L4283) | 4283 | `"                    \"شقه\", \"شقق\", \"عقار\", \"عقارات\", \"فيلا\", \"فلل\","` | — |
| [SRC-1AE03B9EC3-L004284](../../agents/web_agent.py#L4284) | 4284 | `"                    \"apartment\", \"apartments\", \"flat\", \"real estate\", \"property\", \"house\", \"villa\","` | — |
| [SRC-1AE03B9EC3-L004285](../../agents/web_agent.py#L4285) | 4285 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004286](../../agents/web_agent.py#L4286) | 4286 | `"                if self._is_listing_discovery(working_question) and any("` | — |
| [SRC-1AE03B9EC3-L004287](../../agents/web_agent.py#L4287) | 4287 | `"                    term in normalized_question for term in property_terms"` | — |
| [SRC-1AE03B9EC3-L004288](../../agents/web_agent.py#L4288) | 4288 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L004289](../../agents/web_agent.py#L4289) | 4289 | `"                    candidates.extend(["` | — |
| [SRC-1AE03B9EC3-L004290](../../agents/web_agent.py#L4290) | 4290 | `"                        f\"{base_query} إعلانات عقارية ومواقع العقارات\","` | — |
| [SRC-1AE03B9EC3-L004291](../../agents/web_agent.py#L4291) | 4291 | `"                        f\"{base_query} متوسط أسعار السوق للمتر\","` | — |
| [SRC-1AE03B9EC3-L004292](../../agents/web_agent.py#L4292) | 4292 | `"                        f\"{base_query} مواصفات الوحدات والمساحات وطرق السداد\","` | — |
| [SRC-1AE03B9EC3-L004293](../../agents/web_agent.py#L4293) | 4293 | `"                    ])"` | — |
| [SRC-1AE03B9EC3-L004294](../../agents/web_agent.py#L4294) | 4294 | `"                # Explicit deep mode follows the same criterion-first budget allocation"` | — |
| [SRC-1AE03B9EC3-L004295](../../agents/web_agent.py#L4295) | 4295 | `"                # as automatic deep mode, so generic modifiers cannot crowd out requested"` | — |
| [SRC-1AE03B9EC3-L004296](../../agents/web_agent.py#L4296) | 4296 | `"                # dimensions such as price, battery, camera, privacy, or reliability."` | — |
| [SRC-1AE03B9EC3-L004297](../../agents/web_agent.py#L4297) | 4297 | `"                criterion_queries = ["` | — |
| [SRC-1AE03B9EC3-L004298](../../agents/web_agent.py#L4298) | 4298 | `"                    compact_search_query(f\"{base_query} {target} official data specifications\")"` | — |
| [SRC-1AE03B9EC3-L004299](../../agents/web_agent.py#L4299) | 4299 | `"                    for target in self._question_coverage_targets(working_question)"` | — |
| [SRC-1AE03B9EC3-L004300](../../agents/web_agent.py#L4300) | 4300 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004301](../../agents/web_agent.py#L4301) | 4301 | `"                criterion_queries = ["` | — |
| [SRC-1AE03B9EC3-L004302](../../agents/web_agent.py#L4302) | 4302 | `"                    query for query in criterion_queries"` | — |
| [SRC-1AE03B9EC3-L004303](../../agents/web_agent.py#L4303) | 4303 | `"                    if query and _relevance_query_tokens(query)"` | — |
| [SRC-1AE03B9EC3-L004304](../../agents/web_agent.py#L4304) | 4304 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004305](../../agents/web_agent.py#L4305) | 4305 | `"                # Criterion queries include the subject and take priority; retain a"` | — |
| [SRC-1AE03B9EC3-L004306](../../agents/web_agent.py#L4306) | 4306 | `"                # planner query and generic exploration only when budget remains."` | — |
| [SRC-1AE03B9EC3-L004307](../../agents/web_agent.py#L4307) | 4307 | `"                original_queries = ["` | — |
| [SRC-1AE03B9EC3-L004308](../../agents/web_agent.py#L4308) | 4308 | `"                    query for query in (plan.get(\"queries\") or [])"` | — |
| [SRC-1AE03B9EC3-L004309](../../agents/web_agent.py#L4309) | 4309 | `"                    if isinstance(query, str) and query.strip()"` | — |
| [SRC-1AE03B9EC3-L004310](../../agents/web_agent.py#L4310) | 4310 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004311](../../agents/web_agent.py#L4311) | 4311 | `"                prioritized_queries = criterion_queries[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004312](../../agents/web_agent.py#L4312) | 4312 | `"                if len(prioritized_queries) < MAX_PLAN_QUERIES:"` | — |
| [SRC-1AE03B9EC3-L004313](../../agents/web_agent.py#L4313) | 4313 | `"                    prioritized_queries += original_queries[:1] + candidates"` | — |
| [SRC-1AE03B9EC3-L004314](../../agents/web_agent.py#L4314) | 4314 | `"                plan[\"queries\"] = list(dict.fromkeys(prioritized_queries))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004315](../../agents/web_agent.py#L4315) | 4315 | `"            elif clean_mode == \"latest\":"` | — |
| [SRC-1AE03B9EC3-L004316](../../agents/web_agent.py#L4316) | 4316 | `"                plan[\"freshness\"] = \"current\""` | — |
| [SRC-1AE03B9EC3-L004317](../../agents/web_agent.py#L4317) | 4317 | `"                if self._is_navigation_request(working_question):"` | — |
| [SRC-1AE03B9EC3-L004318](../../agents/web_agent.py#L4318) | 4318 | `"                    # Preserve link-finding intent in the latest mode. Appending broad"` | — |
| [SRC-1AE03B9EC3-L004319](../../agents/web_agent.py#L4319) | 4319 | `"                    # news modifiers here can turn \"find the official website\" into"` | — |
| [SRC-1AE03B9EC3-L004320](../../agents/web_agent.py#L4320) | 4320 | `"                    # a news-search task and hide the destination the user requested."` | — |
| [SRC-1AE03B9EC3-L004321](../../agents/web_agent.py#L4321) | 4321 | `"                    candidates = ["` | — |
| [SRC-1AE03B9EC3-L004322](../../agents/web_agent.py#L4322) | 4322 | `"                        base_query,"` | — |
| [SRC-1AE03B9EC3-L004323](../../agents/web_agent.py#L4323) | 4323 | `"                        f\"{base_query} الموقع الرسمي\","` | — |
| [SRC-1AE03B9EC3-L004324](../../agents/web_agent.py#L4324) | 4324 | `"                        f\"{base_query} official website\","` | — |
| [SRC-1AE03B9EC3-L004325](../../agents/web_agent.py#L4325) | 4325 | `"                    ]"` | — |
| [SRC-1AE03B9EC3-L004326](../../agents/web_agent.py#L4326) | 4326 | `"                    plan[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L004327](../../agents/web_agent.py#L4327) | 4327 | `"                        candidates + (plan.get(\"queries\") or [])[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004328](../../agents/web_agent.py#L4328) | 4328 | `"                    ))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004329](../../agents/web_agent.py#L4329) | 4329 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L004330](../../agents/web_agent.py#L4330) | 4330 | `"                    candidates = ["` | — |
| [SRC-1AE03B9EC3-L004331](../../agents/web_agent.py#L4331) | 4331 | `"                        f\"{base_query} latest news updates {dt.datetime.now().year}\","` | — |
| [SRC-1AE03B9EC3-L004332](../../agents/web_agent.py#L4332) | 4332 | `"                        f\"{base_query} recent official announcement\","` | — |
| [SRC-1AE03B9EC3-L004333](../../agents/web_agent.py#L4333) | 4333 | `"                    ]"` | — |
| [SRC-1AE03B9EC3-L004334](../../agents/web_agent.py#L4334) | 4334 | `"                    plan[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L004335](../../agents/web_agent.py#L4335) | 4335 | `"                        (plan.get(\"queries\") or [])[:6] + candidates"` | — |
| [SRC-1AE03B9EC3-L004336](../../agents/web_agent.py#L4336) | 4336 | `"                    ))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004337](../../agents/web_agent.py#L4337) | 4337 | `"            elif clean_mode == \"social\":"` | — |
| [SRC-1AE03B9EC3-L004338](../../agents/web_agent.py#L4338) | 4338 | `"                plan[\"social_focus\"] = True"` | — |
| [SRC-1AE03B9EC3-L004339](../../agents/web_agent.py#L4339) | 4339 | `"                if not plan.get(\"platforms\"):"` | — |
| [SRC-1AE03B9EC3-L004340](../../agents/web_agent.py#L4340) | 4340 | `"                    plan[\"platforms\"] = [\"reddit\", \"bluesky\", \"youtube\"]"` | — |
| [SRC-1AE03B9EC3-L004341](../../agents/web_agent.py#L4341) | 4341 | `"                from agents.research import SOCIAL_DOMAINS"` | — |
| [SRC-1AE03B9EC3-L004342](../../agents/web_agent.py#L4342) | 4342 | `"                candidates = ["` | — |
| [SRC-1AE03B9EC3-L004343](../../agents/web_agent.py#L4343) | 4343 | `"                    f\"site:{SOCIAL_DOMAINS[name]} {base_query}\""` | — |
| [SRC-1AE03B9EC3-L004344](../../agents/web_agent.py#L4344) | 4344 | `"                    for name in plan[\"platforms\"][:3]"` | — |
| [SRC-1AE03B9EC3-L004345](../../agents/web_agent.py#L4345) | 4345 | `"                    if name in SOCIAL_DOMAINS"` | — |
| [SRC-1AE03B9EC3-L004346](../../agents/web_agent.py#L4346) | 4346 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004347](../../agents/web_agent.py#L4347) | 4347 | `"                plan[\"queries\"] = list(dict.fromkeys((plan.get(\"queries\") or [])[:5] + candidates))["` | — |
| [SRC-1AE03B9EC3-L004348](../../agents/web_agent.py#L4348) | 4348 | `"                    :MAX_PLAN_QUERIES"` | — |
| [SRC-1AE03B9EC3-L004349](../../agents/web_agent.py#L4349) | 4349 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004350](../../agents/web_agent.py#L4350) | 4350 | `"            if intent_route == \"LEAD_GENERATION\" and clean_mode == \"auto\":"` | — |
| [SRC-1AE03B9EC3-L004351](../../agents/web_agent.py#L4351) | 4351 | `"                # Prospect discovery needs buyer-intent queries and public social signals,"` | — |
| [SRC-1AE03B9EC3-L004352](../../agents/web_agent.py#L4352) | 4352 | `"                # not just broad pages advertising the requested product."` | — |
| [SRC-1AE03B9EC3-L004353](../../agents/web_agent.py#L4353) | 4353 | `"                plan[\"queries\"] = self._lead_generation_queries(working_question, plan.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L004354](../../agents/web_agent.py#L4354) | 4354 | `"                plan[\"depth\"] = \"standard\""` | — |
| [SRC-1AE03B9EC3-L004355](../../agents/web_agent.py#L4355) | 4355 | `"                plan[\"freshness\"] = \"current\""` | — |
| [SRC-1AE03B9EC3-L004356](../../agents/web_agent.py#L4356) | 4356 | `"                plan[\"social_focus\"] = True"` | — |
| [SRC-1AE03B9EC3-L004357](../../agents/web_agent.py#L4357) | 4357 | `"                allowed_public_platforms = [\"reddit\", \"bluesky\"]"` | — |
| [SRC-1AE03B9EC3-L004358](../../agents/web_agent.py#L4358) | 4358 | `"                if ("` | — |
| [SRC-1AE03B9EC3-L004359](../../agents/web_agent.py#L4359) | 4359 | `"                    os.getenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L004360](../../agents/web_agent.py#L4360) | 4360 | `"                    and os.getenv(\"FACEBOOK_PAGE_IDS\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L004361](../../agents/web_agent.py#L4361) | 4361 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L004362](../../agents/web_agent.py#L4362) | 4362 | `"                    allowed_public_platforms.append(\"facebook\")"` | — |
| [SRC-1AE03B9EC3-L004363](../../agents/web_agent.py#L4363) | 4363 | `"                if os.getenv(\"X_BEARER_TOKEN\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L004364](../../agents/web_agent.py#L4364) | 4364 | `"                    allowed_public_platforms.append(\"x\")"` | — |
| [SRC-1AE03B9EC3-L004365](../../agents/web_agent.py#L4365) | 4365 | `"                if os.getenv(\"YOUTUBE_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L004366](../../agents/web_agent.py#L4366) | 4366 | `"                    allowed_public_platforms.append(\"youtube\")"` | — |
| [SRC-1AE03B9EC3-L004367](../../agents/web_agent.py#L4367) | 4367 | `"                if ("` | — |
| [SRC-1AE03B9EC3-L004368](../../agents/web_agent.py#L4368) | 4368 | `"                    os.getenv(\"INSTAGRAM_USER_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L004369](../../agents/web_agent.py#L4369) | 4369 | `"                    and os.getenv(\"INSTAGRAM_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L004370](../../agents/web_agent.py#L4370) | 4370 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L004371](../../agents/web_agent.py#L4371) | 4371 | `"                    allowed_public_platforms.append(\"instagram\")"` | — |
| [SRC-1AE03B9EC3-L004372](../../agents/web_agent.py#L4372) | 4372 | `"                plan[\"platforms\"] = list(dict.fromkeys(allowed_public_platforms))"` | — |
| [SRC-1AE03B9EC3-L004373](../../agents/web_agent.py#L4373) | 4373 | `""` | — |
| [SRC-1AE03B9EC3-L004374](../../agents/web_agent.py#L4374) | 4374 | `"        final_topic_queries = []"` | — |
| [SRC-1AE03B9EC3-L004375](../../agents/web_agent.py#L4375) | 4375 | `"        for raw_query in plan.get(\"queries\", []):"` | — |
| [SRC-1AE03B9EC3-L004376](../../agents/web_agent.py#L4376) | 4376 | `"            if not isinstance(raw_query, str) or not raw_query.strip():"` | — |
| [SRC-1AE03B9EC3-L004377](../../agents/web_agent.py#L4377) | 4377 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L004378](../../agents/web_agent.py#L4378) | 4378 | `"            compacted_query = compact_search_query(raw_query)"` | — |
| [SRC-1AE03B9EC3-L004379](../../agents/web_agent.py#L4379) | 4379 | `"            if compacted_query and _relevance_query_tokens(compacted_query):"` | — |
| [SRC-1AE03B9EC3-L004380](../../agents/web_agent.py#L4380) | 4380 | `"                final_topic_queries.append(compacted_query)"` | — |
| [SRC-1AE03B9EC3-L004381](../../agents/web_agent.py#L4381) | 4381 | `"        coverage_targets_for_budget = self._question_coverage_targets(working_question)"` | — |
| [SRC-1AE03B9EC3-L004382](../../agents/web_agent.py#L4382) | 4382 | `"        # Reserve one bounded search slot for a post-review criterion-evidence gap."` | — |
| [SRC-1AE03B9EC3-L004383](../../agents/web_agent.py#L4383) | 4383 | `"        # Keep all explicit criterion queries when there are many dimensions; the"` | — |
| [SRC-1AE03B9EC3-L004384](../../agents/web_agent.py#L4384) | 4384 | `"        # reserve applies only to ordinary compound tasks with up to six targets."` | — |
| [SRC-1AE03B9EC3-L004385](../../agents/web_agent.py#L4385) | 4385 | `"        reserve_coverage_gap_query = ("` | — |
| [SRC-1AE03B9EC3-L004386](../../agents/web_agent.py#L4386) | 4386 | `"            2 <= len(coverage_targets_for_budget) <= 6"` | — |
| [SRC-1AE03B9EC3-L004387](../../agents/web_agent.py#L4387) | 4387 | `"            and plan.get(\"depth\") == \"deep\""` | — |
| [SRC-1AE03B9EC3-L004388](../../agents/web_agent.py#L4388) | 4388 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004389](../../agents/web_agent.py#L4389) | 4389 | `"        query_limit = MAX_PLAN_QUERIES - 1 if reserve_coverage_gap_query else MAX_PLAN_QUERIES"` | — |
| [SRC-1AE03B9EC3-L004390](../../agents/web_agent.py#L4390) | 4390 | `"        plan[\"coverage_gap_repair_slot_reserved\"] = reserve_coverage_gap_query"` | — |
| [SRC-1AE03B9EC3-L004391](../../agents/web_agent.py#L4391) | 4391 | `"        plan[\"query_limit\"] = query_limit"` | — |
| [SRC-1AE03B9EC3-L004392](../../agents/web_agent.py#L4392) | 4392 | `"        plan[\"queries\"] = list(dict.fromkeys(final_topic_queries))[:query_limit]"` | — |
| [SRC-1AE03B9EC3-L004393](../../agents/web_agent.py#L4393) | 4393 | `""` | — |
| [SRC-1AE03B9EC3-L004394](../../agents/web_agent.py#L4394) | 4394 | `"        sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L004395](../../agents/web_agent.py#L4395) | 4395 | `"        search_warnings: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L004396](../../agents/web_agent.py#L4396) | 4396 | `"        report: dict[str, Any] = {}"` | — |
| [SRC-1AE03B9EC3-L004397](../../agents/web_agent.py#L4397) | 4397 | `"        # Scope diagnostic evidence to this research attempt; a reused WebAgent must not"` | — |
| [SRC-1AE03B9EC3-L004398](../../agents/web_agent.py#L4398) | 4398 | `"        # accidentally inherit provider attempts from an earlier question."` | — |
| [SRC-1AE03B9EC3-L004399](../../agents/web_agent.py#L4399) | 4399 | `"        with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L004400](../../agents/web_agent.py#L4400) | 4400 | `"            research_diagnostic_baseline = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L004401](../../agents/web_agent.py#L4401) | 4401 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L004402](../../agents/web_agent.py#L4402) | 4402 | `"            sources, search_warnings, report = self._collect_research(plan)"` | — |
| [SRC-1AE03B9EC3-L004403](../../agents/web_agent.py#L4403) | 4403 | `"        except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L004404](../../agents/web_agent.py#L4404) | 4404 | `"            search_warnings.append(str(exc))"` | — |
| [SRC-1AE03B9EC3-L004405](../../agents/web_agent.py#L4405) | 4405 | `"            baseline_diagnostic_ids = {id(item) for item in research_diagnostic_baseline}"` | — |
| [SRC-1AE03B9EC3-L004406](../../agents/web_agent.py#L4406) | 4406 | `"            with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L004407](../../agents/web_agent.py#L4407) | 4407 | `"                failure_diagnostics = ["` | — |
| [SRC-1AE03B9EC3-L004408](../../agents/web_agent.py#L4408) | 4408 | `"                    item for item in self._provider_diagnostics"` | — |
| [SRC-1AE03B9EC3-L004409](../../agents/web_agent.py#L4409) | 4409 | `"                    if id(item) not in baseline_diagnostic_ids"` | — |
| [SRC-1AE03B9EC3-L004410](../../agents/web_agent.py#L4410) | 4410 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004411](../../agents/web_agent.py#L4411) | 4411 | `"            provider_attempt_observed = any("` | — |
| [SRC-1AE03B9EC3-L004412](../../agents/web_agent.py#L4412) | 4412 | `"                item.get(\"status\") in _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES"` | — |
| [SRC-1AE03B9EC3-L004413](../../agents/web_agent.py#L4413) | 4413 | `"                for item in failure_diagnostics"` | — |
| [SRC-1AE03B9EC3-L004414](../../agents/web_agent.py#L4414) | 4414 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004415](../../agents/web_agent.py#L4415) | 4415 | `"            report = {"` | — |
| [SRC-1AE03B9EC3-L004416](../../agents/web_agent.py#L4416) | 4416 | `"                \"queries_planned\": len(plan.get(\"queries\", [])),"` | — |
| [SRC-1AE03B9EC3-L004417](../../agents/web_agent.py#L4417) | 4417 | `"                # The exact query count is unknowable when the pipeline fails before it"` | — |
| [SRC-1AE03B9EC3-L004418](../../agents/web_agent.py#L4418) | 4418 | `"                # returns its report. A provider diagnostic may still prove an attempt."` | — |
| [SRC-1AE03B9EC3-L004419](../../agents/web_agent.py#L4419) | 4419 | `"                \"queries_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L004420](../../agents/web_agent.py#L4420) | 4420 | `"                \"queries_attempted_known\": False,"` | — |
| [SRC-1AE03B9EC3-L004421](../../agents/web_agent.py#L4421) | 4421 | `"                \"search_attempted\": True if provider_attempt_observed else None,"` | — |
| [SRC-1AE03B9EC3-L004422](../../agents/web_agent.py#L4422) | 4422 | `"                \"search_outcome\": ("` | — |
| [SRC-1AE03B9EC3-L004423](../../agents/web_agent.py#L4423) | 4423 | `"                    \"attempted_research_error\""` | — |
| [SRC-1AE03B9EC3-L004424](../../agents/web_agent.py#L4424) | 4424 | `"                    if provider_attempt_observed"` | — |
| [SRC-1AE03B9EC3-L004425](../../agents/web_agent.py#L4425) | 4425 | `"                    else \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L004426](../../agents/web_agent.py#L4426) | 4426 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L004427](../../agents/web_agent.py#L4427) | 4427 | `"                \"usable_sources_after_filtering\": None,"` | — |
| [SRC-1AE03B9EC3-L004428](../../agents/web_agent.py#L4428) | 4428 | `"                \"unique_sources\": None,"` | — |
| [SRC-1AE03B9EC3-L004429](../../agents/web_agent.py#L4429) | 4429 | `"                \"pages_fetched\": None,"` | — |
| [SRC-1AE03B9EC3-L004430](../../agents/web_agent.py#L4430) | 4430 | `"                \"providers_used\": [],"` | — |
| [SRC-1AE03B9EC3-L004431](../../agents/web_agent.py#L4431) | 4431 | `"                \"provider_counts\": None,"` | — |
| [SRC-1AE03B9EC3-L004432](../../agents/web_agent.py#L4432) | 4432 | `"                \"platform_counts\": {},"` | — |
| [SRC-1AE03B9EC3-L004433](../../agents/web_agent.py#L4433) | 4433 | `"                \"social_direct_results\": None,"` | — |
| [SRC-1AE03B9EC3-L004434](../../agents/web_agent.py#L4434) | 4434 | `"                \"provider_diagnostics\": failure_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L004435](../../agents/web_agent.py#L4435) | 4435 | `"                \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L004436](../../agents/web_agent.py#L4436) | 4436 | `"                \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L004437](../../agents/web_agent.py#L4437) | 4437 | `"                \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L004438](../../agents/web_agent.py#L4438) | 4438 | `"                \"evidence_signals\": evidence_signal_report([], plan.get(\"freshness\", \"any\")),"` | — |
| [SRC-1AE03B9EC3-L004439](../../agents/web_agent.py#L4439) | 4439 | `"            }"` | — |
| [SRC-1AE03B9EC3-L004440](../../agents/web_agent.py#L4440) | 4440 | `"        if isinstance(report, dict):"` | — |
| [SRC-1AE03B9EC3-L004441](../../agents/web_agent.py#L4441) | 4441 | `"            report[\"dialogue_context\"] = plan.get(\"dialogue_context\", {})"` | — |
| [SRC-1AE03B9EC3-L004442](../../agents/web_agent.py#L4442) | 4442 | `"        # Final relevance check is intentionally repeated after fusion, before any answer LLM call."` | — |
| [SRC-1AE03B9EC3-L004443](../../agents/web_agent.py#L4443) | 4443 | `"        filtered_sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L004444](../../agents/web_agent.py#L4444) | 4444 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L004445](../../agents/web_agent.py#L4445) | 4445 | `"            if \"user_supplied_url\" in source.get(\"providers\", []):"` | — |
| [SRC-1AE03B9EC3-L004446](../../agents/web_agent.py#L4446) | 4446 | `"                filtered_sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L004447](../../agents/web_agent.py#L4447) | 4447 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L004448](../../agents/web_agent.py#L4448) | 4448 | `"            candidate_queries = ("` | — |
| [SRC-1AE03B9EC3-L004449](../../agents/web_agent.py#L4449) | 4449 | `"                source.get(\"queries\")"` | — |
| [SRC-1AE03B9EC3-L004450](../../agents/web_agent.py#L4450) | 4450 | `"                or plan.get(\"queries\")"` | — |
| [SRC-1AE03B9EC3-L004451](../../agents/web_agent.py#L4451) | 4451 | `"                or [compact_search_query(working_question)]"` | — |
| [SRC-1AE03B9EC3-L004452](../../agents/web_agent.py#L4452) | 4452 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004453](../../agents/web_agent.py#L4453) | 4453 | `"            if any(self._source_matches_query(str(q), source) for q in candidate_queries):"` | — |
| [SRC-1AE03B9EC3-L004454](../../agents/web_agent.py#L4454) | 4454 | `"                filtered_sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L004455](../../agents/web_agent.py#L4455) | 4455 | `"        sources = filtered_sources"` | — |
| [SRC-1AE03B9EC3-L004456](../../agents/web_agent.py#L4456) | 4456 | `"        search_warning = \"؛ \".join(search_warnings) if search_warnings else None"` | — |
| [SRC-1AE03B9EC3-L004457](../../agents/web_agent.py#L4457) | 4457 | `"        independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L004458](../../agents/web_agent.py#L4458) | 4458 | `"            registrable_domain("` | — |
| [SRC-1AE03B9EC3-L004459](../../agents/web_agent.py#L4459) | 4459 | `"                source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L004460](../../agents/web_agent.py#L4460) | 4460 | `"                or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L004461](../../agents/web_agent.py#L4461) | 4461 | `"                or \"\""` | — |
| [SRC-1AE03B9EC3-L004462](../../agents/web_agent.py#L4462) | 4462 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004463](../../agents/web_agent.py#L4463) | 4463 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L004464](../../agents/web_agent.py#L4464) | 4464 | `"        }"` | — |
| [SRC-1AE03B9EC3-L004465](../../agents/web_agent.py#L4465) | 4465 | `"        independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L004466](../../agents/web_agent.py#L4466) | 4466 | `"        # A user-requested page summary is a different task from open-ended research:"` | — |
| [SRC-1AE03B9EC3-L004467](../../agents/web_agent.py#L4467) | 4467 | `"        # one successfully extracted, explicitly supplied page can support a summary,"` | — |
| [SRC-1AE03B9EC3-L004468](../../agents/web_agent.py#L4468) | 4468 | `"        # but must never be presented as independently corroborated research."` | — |
| [SRC-1AE03B9EC3-L004469](../../agents/web_agent.py#L4469) | 4469 | `"        has_read_user_supplied_page = any("` | — |
| [SRC-1AE03B9EC3-L004470](../../agents/web_agent.py#L4470) | 4470 | `"            \"user_supplied_url\" in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L004471](../../agents/web_agent.py#L4471) | 4471 | `"            and bool(source.get(\"page_fetched\"))"` | — |
| [SRC-1AE03B9EC3-L004472](../../agents/web_agent.py#L4472) | 4472 | `"            and bool(str(source.get(\"page_text\") or \"\").strip())"` | — |
| [SRC-1AE03B9EC3-L004473](../../agents/web_agent.py#L4473) | 4473 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L004474](../../agents/web_agent.py#L4474) | 4474 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004475](../../agents/web_agent.py#L4475) | 4475 | `"        single_source_page_summary = ("` | — |
