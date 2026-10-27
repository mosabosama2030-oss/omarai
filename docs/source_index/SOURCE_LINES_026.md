# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **026**
- سجلات الأسطر: **800**
- النطاق: SRC-3451CC474D-L000678 إلى SRC-6BCB799CEC-L000282
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-3451CC474D — [tests/test_api.py](../../tests/test_api.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-3451CC474D-L000678](../../tests/test_api.py#L678) | 678 | `""` | — |
| [SRC-3451CC474D-L000679](../../tests/test_api.py#L679) | 679 | `""` | — |
| [SRC-3451CC474D-L000680](../../tests/test_api.py#L680) | 680 | `"def test_public_origin_still_allows_the_requested_host(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000681](../../tests/test_api.py#L681) | 681 | `"    \"\"\"Same-service public UI remains compatible when the request Host is trusted.\"\"\""` | — |
| [SRC-3451CC474D-L000682](../../tests/test_api.py#L682) | 682 | `"    from types import SimpleNamespace"` | — |
| [SRC-3451CC474D-L000683](../../tests/test_api.py#L683) | 683 | `""` | — |
| [SRC-3451CC474D-L000684](../../tests/test_api.py#L684) | 684 | `"    from api.omarai import Handler"` | — |
| [SRC-3451CC474D-L000685](../../tests/test_api.py#L685) | 685 | `""` | — |
| [SRC-3451CC474D-L000686](../../tests/test_api.py#L686) | 686 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L000687](../../tests/test_api.py#L687) | 687 | `"    monkeypatch.delenv(\"OMARAI_ALLOWED_ORIGINS\", raising=False)"` | — |
| [SRC-3451CC474D-L000688](../../tests/test_api.py#L688) | 688 | `"    handler = SimpleNamespace("` | — |
| [SRC-3451CC474D-L000689](../../tests/test_api.py#L689) | 689 | `"        headers={"` | — |
| [SRC-3451CC474D-L000690](../../tests/test_api.py#L690) | 690 | `"            \"Host\": \"omarai.example\","` | — |
| [SRC-3451CC474D-L000691](../../tests/test_api.py#L691) | 691 | `"            \"X-Forwarded-Proto\": \"https\","` | — |
| [SRC-3451CC474D-L000692](../../tests/test_api.py#L692) | 692 | `"            \"X-Forwarded-Host\": \"attacker.example\","` | — |
| [SRC-3451CC474D-L000693](../../tests/test_api.py#L693) | 693 | `"        }"` | — |
| [SRC-3451CC474D-L000694](../../tests/test_api.py#L694) | 694 | `"    )"` | — |
| [SRC-3451CC474D-L000695](../../tests/test_api.py#L695) | 695 | `"    allowed = Handler._allowed_origins(handler)"` | — |
| [SRC-3451CC474D-L000696](../../tests/test_api.py#L696) | 696 | `"    assert \"https://omarai.example\" in allowed"` | — |
| [SRC-3451CC474D-L000697](../../tests/test_api.py#L697) | 697 | `"    assert \"https://attacker.example\" not in allowed"` | — |
| [SRC-3451CC474D-L000698](../../tests/test_api.py#L698) | 698 | `""` | — |
| [SRC-3451CC474D-L000699](../../tests/test_api.py#L699) | 699 | `""` | — |
| [SRC-3451CC474D-L000700](../../tests/test_api.py#L700) | 700 | `""` | — |
| [SRC-3451CC474D-L000701](../../tests/test_api.py#L701) | 701 | `"def test_security_headers_apply_to_json_and_html_responses(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000702](../../tests/test_api.py#L702) | 702 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000703](../../tests/test_api.py#L703) | 703 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000704](../../tests/test_api.py#L704) | 704 | `"    for path in (\"/api/health\", \"/\"):"` | — |
| [SRC-3451CC474D-L000705](../../tests/test_api.py#L705) | 705 | `"        request = Request(local_api + path)"` | — |
| [SRC-3451CC474D-L000706](../../tests/test_api.py#L706) | 706 | `"        with urlopen(request, timeout=3) as response:"` | — |
| [SRC-3451CC474D-L000707](../../tests/test_api.py#L707) | 707 | `"            headers = {name.lower(): value for name, value in response.headers.items()}"` | — |
| [SRC-3451CC474D-L000708](../../tests/test_api.py#L708) | 708 | `"            assert headers[\"x-content-type-options\"] == \"nosniff\""` | — |
| [SRC-3451CC474D-L000709](../../tests/test_api.py#L709) | 709 | `"            assert headers[\"x-frame-options\"] == \"DENY\""` | — |
| [SRC-3451CC474D-L000710](../../tests/test_api.py#L710) | 710 | `"            assert headers[\"referrer-policy\"] == \"strict-origin-when-cross-origin\""` | — |
| [SRC-3451CC474D-L000711](../../tests/test_api.py#L711) | 711 | `"            assert \"default-src 'self'\" in headers[\"content-security-policy\"]"` | — |
| [SRC-3451CC474D-L000712](../../tests/test_api.py#L712) | 712 | `"            policy = headers[\"content-security-policy\"]"` | — |
| [SRC-3451CC474D-L000713](../../tests/test_api.py#L713) | 713 | `"            assert \"frame-ancestors 'none'\" in policy"` | — |
| [SRC-3451CC474D-L000714](../../tests/test_api.py#L714) | 714 | `"            assert \"'unsafe-inline'\" not in policy"` | — |
| [SRC-3451CC474D-L000715](../../tests/test_api.py#L715) | 715 | `"            assert \"'sha256-\" in policy"` | — |
| [SRC-3451CC474D-L000716](../../tests/test_api.py#L716) | 716 | `"            assert headers[\"permissions-policy\"] == ("` | — |
| [SRC-3451CC474D-L000717](../../tests/test_api.py#L717) | 717 | `"                \"camera=(), microphone=(), geolocation=()\""` | — |
| [SRC-3451CC474D-L000718](../../tests/test_api.py#L718) | 718 | `"            )"` | — |
| [SRC-3451CC474D-L000719](../../tests/test_api.py#L719) | 719 | `""` | — |
| [SRC-3451CC474D-L000720](../../tests/test_api.py#L720) | 720 | `""` | — |
| [SRC-3451CC474D-L000721](../../tests/test_api.py#L721) | 721 | `"def test_health_exposes_only_validated_image_baked_sha(monkeypatch, tmp_path):"` | — |
| [SRC-3451CC474D-L000722](../../tests/test_api.py#L722) | 722 | `"    import api.omarai as api_module"` | — |
| [SRC-3451CC474D-L000723](../../tests/test_api.py#L723) | 723 | `""` | — |
| [SRC-3451CC474D-L000724](../../tests/test_api.py#L724) | 724 | `"    build_sha_file = tmp_path / \"BUILD_SHA\""` | — |
| [SRC-3451CC474D-L000725](../../tests/test_api.py#L725) | 725 | `"    monkeypatch.setattr(api_module, \"BUILD_SHA_FILE\", build_sha_file)"` | — |
| [SRC-3451CC474D-L000726](../../tests/test_api.py#L726) | 726 | `"    assert api_module._build_sha() == \"unknown\""` | — |
| [SRC-3451CC474D-L000727](../../tests/test_api.py#L727) | 727 | `"    build_sha_file.write_text(\"a\" * 40, encoding=\"ascii\")"` | — |
| [SRC-3451CC474D-L000728](../../tests/test_api.py#L728) | 728 | `"    assert api_module._build_sha() == \"a\" * 40"` | — |
| [SRC-3451CC474D-L000729](../../tests/test_api.py#L729) | 729 | `"    build_sha_file.write_text(\"not-a-git-sha\", encoding=\"ascii\")"` | — |
| [SRC-3451CC474D-L000730](../../tests/test_api.py#L730) | 730 | `"    assert api_module._build_sha() == \"unknown\""` | — |
| [SRC-3451CC474D-L000731](../../tests/test_api.py#L731) | 731 | `""` | — |
| [SRC-3451CC474D-L000732](../../tests/test_api.py#L732) | 732 | `""` | — |
| [SRC-3451CC474D-L000733](../../tests/test_api.py#L733) | 733 | `""` | — |
| [SRC-3451CC474D-L000734](../../tests/test_api.py#L734) | 734 | `"@pytest.mark.parametrize("` | — |
| [SRC-3451CC474D-L000735](../../tests/test_api.py#L735) | 735 | `"    (\"variable\", \"source\"),"` | — |
| [SRC-3451CC474D-L000736](../../tests/test_api.py#L736) | 736 | `"    ["` | — |
| [SRC-3451CC474D-L000737](../../tests/test_api.py#L737) | 737 | `"        (\"RAILWAY_GIT_COMMIT_SHA\", \"platform:railway\"),"` | — |
| [SRC-3451CC474D-L000738](../../tests/test_api.py#L738) | 738 | `"        (\"RENDER_GIT_COMMIT\", \"platform:render\"),"` | — |
| [SRC-3451CC474D-L000739](../../tests/test_api.py#L739) | 739 | `"    ],"` | — |
| [SRC-3451CC474D-L000740](../../tests/test_api.py#L740) | 740 | `")"` | — |
| [SRC-3451CC474D-L000741](../../tests/test_api.py#L741) | 741 | `"def test_build_identity_uses_validated_platform_commit_when_image_sha_is_unavailable("` | — |
| [SRC-3451CC474D-L000742](../../tests/test_api.py#L742) | 742 | `"    monkeypatch, tmp_path, variable, source"` | — |
| [SRC-3451CC474D-L000743](../../tests/test_api.py#L743) | 743 | `"):"` | — |
| [SRC-3451CC474D-L000744](../../tests/test_api.py#L744) | 744 | `"    import api.omarai as api_module"` | — |
| [SRC-3451CC474D-L000745](../../tests/test_api.py#L745) | 745 | `""` | — |
| [SRC-3451CC474D-L000746](../../tests/test_api.py#L746) | 746 | `"    build_sha_file = tmp_path / \"BUILD_SHA\""` | — |
| [SRC-3451CC474D-L000747](../../tests/test_api.py#L747) | 747 | `"    monkeypatch.setattr(api_module, \"BUILD_SHA_FILE\", build_sha_file)"` | — |
| [SRC-3451CC474D-L000748](../../tests/test_api.py#L748) | 748 | `"    build_sha_file.write_text(\"unknown\", encoding=\"ascii\")"` | — |
| [SRC-3451CC474D-L000749](../../tests/test_api.py#L749) | 749 | `"    for name, _label in api_module._PLATFORM_BUILD_SHA_ENVIRONMENTS:"` | — |
| [SRC-3451CC474D-L000750](../../tests/test_api.py#L750) | 750 | `"        monkeypatch.delenv(name, raising=False)"` | — |
| [SRC-3451CC474D-L000751](../../tests/test_api.py#L751) | 751 | `"    monkeypatch.setenv(variable, \"b\" * 40)"` | — |
| [SRC-3451CC474D-L000752](../../tests/test_api.py#L752) | 752 | `""` | — |
| [SRC-3451CC474D-L000753](../../tests/test_api.py#L753) | 753 | `"    assert api_module._build_identity() == (\"b\" * 40, source)"` | — |
| [SRC-3451CC474D-L000754](../../tests/test_api.py#L754) | 754 | `""` | — |
| [SRC-3451CC474D-L000755](../../tests/test_api.py#L755) | 755 | `""` | — |
| [SRC-3451CC474D-L000756](../../tests/test_api.py#L756) | 756 | `"def test_invalid_platform_commit_does_not_create_build_identity(monkeypatch, tmp_path):"` | — |
| [SRC-3451CC474D-L000757](../../tests/test_api.py#L757) | 757 | `"    import api.omarai as api_module"` | — |
| [SRC-3451CC474D-L000758](../../tests/test_api.py#L758) | 758 | `""` | — |
| [SRC-3451CC474D-L000759](../../tests/test_api.py#L759) | 759 | `"    monkeypatch.setattr(api_module, \"BUILD_SHA_FILE\", tmp_path / \"BUILD_SHA\")"` | — |
| [SRC-3451CC474D-L000760](../../tests/test_api.py#L760) | 760 | `"    api_module.BUILD_SHA_FILE.write_text(\"unknown\", encoding=\"ascii\")"` | — |
| [SRC-3451CC474D-L000761](../../tests/test_api.py#L761) | 761 | `"    monkeypatch.setenv(\"RAILWAY_GIT_COMMIT_SHA\", \"not-a-sha\")"` | — |
| [SRC-3451CC474D-L000762](../../tests/test_api.py#L762) | 762 | `"    monkeypatch.setenv(\"RENDER_GIT_COMMIT\", \"also-not-a-sha\")"` | — |
| [SRC-3451CC474D-L000763](../../tests/test_api.py#L763) | 763 | `""` | — |
| [SRC-3451CC474D-L000764](../../tests/test_api.py#L764) | 764 | `"    assert api_module._build_identity() == (\"unknown\", \"unknown\")"` | — |
| [SRC-3451CC474D-L000765](../../tests/test_api.py#L765) | 765 | `""` | — |
| [SRC-3451CC474D-L000766](../../tests/test_api.py#L766) | 766 | `""` | — |
| [SRC-3451CC474D-L000767](../../tests/test_api.py#L767) | 767 | `""` | — |
| [SRC-3451CC474D-L000768](../../tests/test_api.py#L768) | 768 | `"def test_lead_store_uses_configured_database_path(monkeypatch, tmp_path):"` | — |
| [SRC-3451CC474D-L000769](../../tests/test_api.py#L769) | 769 | `"    from api.omarai import _lead_store_from_environment"` | — |
| [SRC-3451CC474D-L000770](../../tests/test_api.py#L770) | 770 | `""` | — |
| [SRC-3451CC474D-L000771](../../tests/test_api.py#L771) | 771 | `"    database_path = tmp_path / \"persistent\" / \"omarai.sqlite3\""` | — |
| [SRC-3451CC474D-L000772](../../tests/test_api.py#L772) | 772 | `"    monkeypatch.setenv(\"OMARAI_DB_PATH\", str(database_path))"` | — |
| [SRC-3451CC474D-L000773](../../tests/test_api.py#L773) | 773 | `""` | — |
| [SRC-3451CC474D-L000774](../../tests/test_api.py#L774) | 774 | `"    store = _lead_store_from_environment()"` | — |
| [SRC-3451CC474D-L000775](../../tests/test_api.py#L775) | 775 | `""` | — |
| [SRC-3451CC474D-L000776](../../tests/test_api.py#L776) | 776 | `"    assert store.path == database_path"` | — |
| [SRC-3451CC474D-L000777](../../tests/test_api.py#L777) | 777 | `"    assert database_path.is_file()"` | — |
| [SRC-3451CC474D-L000778](../../tests/test_api.py#L778) | 778 | `""` | — |
| [SRC-3451CC474D-L000779](../../tests/test_api.py#L779) | 779 | `""` | — |
| [SRC-3451CC474D-L000780](../../tests/test_api.py#L780) | 780 | `""` | — |
| [SRC-3451CC474D-L000781](../../tests/test_api.py#L781) | 781 | `"def test_agent_concurrency_slot_released_after_operation_error(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000782](../../tests/test_api.py#L782) | 782 | `"    from api.omarai import WebAgent"` | — |
| [SRC-3451CC474D-L000783](../../tests/test_api.py#L783) | 783 | `""` | — |
| [SRC-3451CC474D-L000784](../../tests/test_api.py#L784) | 784 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000785](../../tests/test_api.py#L785) | 785 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000786](../../tests/test_api.py#L786) | 786 | `"    monkeypatch.setattr(Handler, \"_request_times\", defaultdict(deque))"` | — |
| [SRC-3451CC474D-L000787](../../tests/test_api.py#L787) | 787 | `"    monkeypatch.setattr(Handler, \"_rate_last_cleanup\", 0.0)"` | — |
| [SRC-3451CC474D-L000788](../../tests/test_api.py#L788) | 788 | `"    monkeypatch.setattr(Handler, \"_agent_semaphore\", threading.BoundedSemaphore(1))"` | — |
| [SRC-3451CC474D-L000789](../../tests/test_api.py#L789) | 789 | `"    state = {\"fail\": True}"` | — |
| [SRC-3451CC474D-L000790](../../tests/test_api.py#L790) | 790 | `""` | — |
| [SRC-3451CC474D-L000791](../../tests/test_api.py#L791) | 791 | `"    def answer_with_one_transient_failure(self, question, history=None, mode=\"auto\"):"` | — |
| [SRC-3451CC474D-L000792](../../tests/test_api.py#L792) | 792 | `"        if state[\"fail\"]:"` | — |
| [SRC-3451CC474D-L000793](../../tests/test_api.py#L793) | 793 | `"            raise RuntimeError(\"synthetic operation failure\")"` | — |
| [SRC-3451CC474D-L000794](../../tests/test_api.py#L794) | 794 | `"        return {"` | — |
| [SRC-3451CC474D-L000795](../../tests/test_api.py#L795) | 795 | `"            \"answer\": \"اختبار ناجح\","` | — |
| [SRC-3451CC474D-L000796](../../tests/test_api.py#L796) | 796 | `"            \"question\": question,"` | — |
| [SRC-3451CC474D-L000797](../../tests/test_api.py#L797) | 797 | `"            \"search_query\": question,"` | — |
| [SRC-3451CC474D-L000798](../../tests/test_api.py#L798) | 798 | `"            \"search_queries\": [],"` | — |
| [SRC-3451CC474D-L000799](../../tests/test_api.py#L799) | 799 | `"            \"search_report\": {"` | — |
| [SRC-3451CC474D-L000800](../../tests/test_api.py#L800) | 800 | `"                \"search_attempted\": False,"` | — |
| [SRC-3451CC474D-L000801](../../tests/test_api.py#L801) | 801 | `"                \"search_outcome\": \"not_attempted\","` | — |
| [SRC-3451CC474D-L000802](../../tests/test_api.py#L802) | 802 | `"            },"` | — |
| [SRC-3451CC474D-L000803](../../tests/test_api.py#L803) | 803 | `"            \"sources\": [],"` | — |
| [SRC-3451CC474D-L000804](../../tests/test_api.py#L804) | 804 | `"            \"used_language_model\": False,"` | — |
| [SRC-3451CC474D-L000805](../../tests/test_api.py#L805) | 805 | `"            \"used_web_search\": False,"` | — |
| [SRC-3451CC474D-L000806](../../tests/test_api.py#L806) | 806 | `"            \"search_attempted\": False,"` | — |
| [SRC-3451CC474D-L000807](../../tests/test_api.py#L807) | 807 | `"            \"used_social_search\": False,"` | — |
| [SRC-3451CC474D-L000808](../../tests/test_api.py#L808) | 808 | `"            \"warnings\": [],"` | — |
| [SRC-3451CC474D-L000809](../../tests/test_api.py#L809) | 809 | `"            \"kind\": \"web_fallback\","` | — |
| [SRC-3451CC474D-L000810](../../tests/test_api.py#L810) | 810 | `"        }"` | — |
| [SRC-3451CC474D-L000811](../../tests/test_api.py#L811) | 811 | `""` | — |
| [SRC-3451CC474D-L000812](../../tests/test_api.py#L812) | 812 | `"    monkeypatch.setattr(WebAgent, \"answer\", answer_with_one_transient_failure)"` | — |
| [SRC-3451CC474D-L000813](../../tests/test_api.py#L813) | 813 | `""` | — |
| [SRC-3451CC474D-L000814](../../tests/test_api.py#L814) | 814 | `"    status, payload = request_json("` | — |
| [SRC-3451CC474D-L000815](../../tests/test_api.py#L815) | 815 | `"        local_api, \"/api/agent\", method=\"POST\", payload={\"question\": \"الطلب الأول\"}"` | — |
| [SRC-3451CC474D-L000816](../../tests/test_api.py#L816) | 816 | `"    )"` | — |
| [SRC-3451CC474D-L000817](../../tests/test_api.py#L817) | 817 | `"    assert status == 500"` | — |
| [SRC-3451CC474D-L000818](../../tests/test_api.py#L818) | 818 | `"    assert payload[\"error\"] == \"internal server error\""` | — |
| [SRC-3451CC474D-L000819](../../tests/test_api.py#L819) | 819 | `""` | — |
| [SRC-3451CC474D-L000820](../../tests/test_api.py#L820) | 820 | `"    state[\"fail\"] = False"` | — |
| [SRC-3451CC474D-L000821](../../tests/test_api.py#L821) | 821 | `"    status, payload = request_json("` | — |
| [SRC-3451CC474D-L000822](../../tests/test_api.py#L822) | 822 | `"        local_api, \"/api/agent\", method=\"POST\", payload={\"question\": \"الطلب الثاني\"}"` | — |
| [SRC-3451CC474D-L000823](../../tests/test_api.py#L823) | 823 | `"    )"` | — |
| [SRC-3451CC474D-L000824](../../tests/test_api.py#L824) | 824 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000825](../../tests/test_api.py#L825) | 825 | `"    assert payload[\"answer\"] == \"اختبار ناجح\""` | — |
| [SRC-3451CC474D-L000826](../../tests/test_api.py#L826) | 826 | `""` | — |
| [SRC-3451CC474D-L000827](../../tests/test_api.py#L827) | 827 | `""` | — |
| [SRC-3451CC474D-L000828](../../tests/test_api.py#L828) | 828 | `"def test_csp_hashes_match_all_first_party_inline_content_and_attributes():"` | — |
| [SRC-3451CC474D-L000829](../../tests/test_api.py#L829) | 829 | `"    import api.omarai as api_module"` | — |
| [SRC-3451CC474D-L000830](../../tests/test_api.py#L830) | 830 | `""` | — |
| [SRC-3451CC474D-L000831](../../tests/test_api.py#L831) | 831 | `"    policy = api_module._content_security_policy()"` | — |
| [SRC-3451CC474D-L000832](../../tests/test_api.py#L832) | 832 | `"    assert \"'unsafe-inline'\" not in policy"` | — |
| [SRC-3451CC474D-L000833](../../tests/test_api.py#L833) | 833 | `"    script_blocks = 0"` | — |
| [SRC-3451CC474D-L000834](../../tests/test_api.py#L834) | 834 | `"    style_blocks = 0"` | — |
| [SRC-3451CC474D-L000835](../../tests/test_api.py#L835) | 835 | `"    style_attributes = 0"` | — |
| [SRC-3451CC474D-L000836](../../tests/test_api.py#L836) | 836 | `"    for html_path in api_module.ROOT.glob(\"*.html\"):"` | — |
| [SRC-3451CC474D-L000837](../../tests/test_api.py#L837) | 837 | `"        document = html_path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3451CC474D-L000838](../../tests/test_api.py#L838) | 838 | `"        for match in re.finditer("` | — |
| [SRC-3451CC474D-L000839](../../tests/test_api.py#L839) | 839 | `"            r\"<script\\b(?P<attrs>[^>]*)>(?P<body>.*?)</script\\s*>\","` | — |
| [SRC-3451CC474D-L000840](../../tests/test_api.py#L840) | 840 | `"            document,"` | — |
| [SRC-3451CC474D-L000841](../../tests/test_api.py#L841) | 841 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-3451CC474D-L000842](../../tests/test_api.py#L842) | 842 | `"        ):"` | — |
| [SRC-3451CC474D-L000843](../../tests/test_api.py#L843) | 843 | `"            if re.search(r\"\\bsrc\\s*=\", match.group(\"attrs\"), re.IGNORECASE):"` | — |
| [SRC-3451CC474D-L000844](../../tests/test_api.py#L844) | 844 | `"                continue"` | — |
| [SRC-3451CC474D-L000845](../../tests/test_api.py#L845) | 845 | `"            script_blocks += 1"` | — |
| [SRC-3451CC474D-L000846](../../tests/test_api.py#L846) | 846 | `"            assert api_module._csp_hash_source(match.group(\"body\")) in policy"` | — |
| [SRC-3451CC474D-L000847](../../tests/test_api.py#L847) | 847 | `"        for match in re.finditer("` | — |
| [SRC-3451CC474D-L000848](../../tests/test_api.py#L848) | 848 | `"            r\"<style\\b[^>]*>(?P<body>.*?)</style\\s*>\","` | — |
| [SRC-3451CC474D-L000849](../../tests/test_api.py#L849) | 849 | `"            document,"` | — |
| [SRC-3451CC474D-L000850](../../tests/test_api.py#L850) | 850 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-3451CC474D-L000851](../../tests/test_api.py#L851) | 851 | `"        ):"` | — |
| [SRC-3451CC474D-L000852](../../tests/test_api.py#L852) | 852 | `"            style_blocks += 1"` | — |
| [SRC-3451CC474D-L000853](../../tests/test_api.py#L853) | 853 | `"            assert api_module._csp_hash_source(match.group(\"body\")) in policy"` | — |
| [SRC-3451CC474D-L000854](../../tests/test_api.py#L854) | 854 | `"        for match in re.finditer("` | — |
| [SRC-3451CC474D-L000855](../../tests/test_api.py#L855) | 855 | `"            r\"\"\"\\bstyle\\s*=\\s*([\"'])(.*?)\\1\"\"\","` | — |
| [SRC-3451CC474D-L000856](../../tests/test_api.py#L856) | 856 | `"            document,"` | — |
| [SRC-3451CC474D-L000857](../../tests/test_api.py#L857) | 857 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-3451CC474D-L000858](../../tests/test_api.py#L858) | 858 | `"        ):"` | — |
| [SRC-3451CC474D-L000859](../../tests/test_api.py#L859) | 859 | `"            style_attributes += 1"` | — |
| [SRC-3451CC474D-L000860](../../tests/test_api.py#L860) | 860 | `"            assert api_module._csp_hash_source(match.group(2).strip()) in policy"` | — |
| [SRC-3451CC474D-L000861](../../tests/test_api.py#L861) | 861 | `"    assert script_blocks >= 2"` | — |
| [SRC-3451CC474D-L000862](../../tests/test_api.py#L862) | 862 | `"    assert style_blocks >= 2"` | — |
| [SRC-3451CC474D-L000863](../../tests/test_api.py#L863) | 863 | `"    assert style_attributes >= 10"` | — |
| [SRC-3451CC474D-L000864](../../tests/test_api.py#L864) | 864 | `""` | — |
| [SRC-3451CC474D-L000865](../../tests/test_api.py#L865) | 865 | `""` | — |
| [SRC-3451CC474D-L000866](../../tests/test_api.py#L866) | 866 | `"def test_dashboard_uses_delegated_status_action_not_inline_onclick():"` | — |
| [SRC-3451CC474D-L000867](../../tests/test_api.py#L867) | 867 | `"    dashboard = (Path(__file__).resolve().parents[1] / \"web\" / \"dashboard.html\").read_text("` | — |
| [SRC-3451CC474D-L000868](../../tests/test_api.py#L868) | 868 | `"        encoding=\"utf-8\""` | — |
| [SRC-3451CC474D-L000869](../../tests/test_api.py#L869) | 869 | `"    )"` | — |
| [SRC-3451CC474D-L000870](../../tests/test_api.py#L870) | 870 | `"    assert 'data-action=\"save-status\"' in dashboard"` | — |
| [SRC-3451CC474D-L000871](../../tests/test_api.py#L871) | 871 | `"    assert 'onclick=\"saveStatus' not in dashboard"` | — |
| [SRC-3451CC474D-L000872](../../tests/test_api.py#L872) | 872 | `"    assert \"\"\"data-lead-id=\"'+esc(l.id)+'\">\"\"\" in dashboard"` | — |
## اختبارات

### FILE-DA61479D59 — [tests/test_connector_summary_counters.py](../../tests/test_connector_summary_counters.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-DA61479D59-L000001](../../tests/test_connector_summary_counters.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-DA61479D59-L000002](../../tests/test_connector_summary_counters.py#L2) | 2 | `""` | — |
| [SRC-DA61479D59-L000003](../../tests/test_connector_summary_counters.py#L3) | 3 | `"import json"` | — |
| [SRC-DA61479D59-L000004](../../tests/test_connector_summary_counters.py#L4) | 4 | `""` | — |
| [SRC-DA61479D59-L000005](../../tests/test_connector_summary_counters.py#L5) | 5 | `"from agents.web_agent import PageFetchResult, WebAgent"` | — |
| [SRC-DA61479D59-L000006](../../tests/test_connector_summary_counters.py#L6) | 6 | `""` | — |
| [SRC-DA61479D59-L000007](../../tests/test_connector_summary_counters.py#L7) | 7 | `""` | — |
| [SRC-DA61479D59-L000008](../../tests/test_connector_summary_counters.py#L8) | 8 | `"def test_connector_summary_reports_request_scope_worst_state_and_redacts_secrets(monkeypatch):"` | — |
| [SRC-DA61479D59-L000009](../../tests/test_connector_summary_counters.py#L9) | 9 | `"    agent = WebAgent()"` | — |
| [SRC-DA61479D59-L000010](../../tests/test_connector_summary_counters.py#L10) | 10 | `"    monkeypatch.delenv(\"BRAVE_SEARCH_API_KEY\", raising=False)"` | — |
| [SRC-DA61479D59-L000011](../../tests/test_connector_summary_counters.py#L11) | 11 | `"    diagnostics = ["` | — |
| [SRC-DA61479D59-L000012](../../tests/test_connector_summary_counters.py#L12) | 12 | `"        {"` | — |
| [SRC-DA61479D59-L000013](../../tests/test_connector_summary_counters.py#L13) | 13 | `"            \"provider\": \"duckduckgo_html\","` | — |
| [SRC-DA61479D59-L000014](../../tests/test_connector_summary_counters.py#L14) | 14 | `"            \"query\": \"renewable energy\","` | — |
| [SRC-DA61479D59-L000015](../../tests/test_connector_summary_counters.py#L15) | 15 | `"            \"status\": \"ok\","` | — |
| [SRC-DA61479D59-L000016](../../tests/test_connector_summary_counters.py#L16) | 16 | `"            \"result_count\": 3,"` | — |
| [SRC-DA61479D59-L000017](../../tests/test_connector_summary_counters.py#L17) | 17 | `"            \"rejected_count\": 1,"` | — |
| [SRC-DA61479D59-L000018](../../tests/test_connector_summary_counters.py#L18) | 18 | `"        },"` | — |
| [SRC-DA61479D59-L000019](../../tests/test_connector_summary_counters.py#L19) | 19 | `"        {"` | — |
| [SRC-DA61479D59-L000020](../../tests/test_connector_summary_counters.py#L20) | 20 | `"            \"provider\": \"duckduckgo_html\","` | — |
| [SRC-DA61479D59-L000021](../../tests/test_connector_summary_counters.py#L21) | 21 | `"            \"query\": \"renewable energy\","` | — |
| [SRC-DA61479D59-L000022](../../tests/test_connector_summary_counters.py#L22) | 22 | `"            \"status\": \"failed\","` | — |
| [SRC-DA61479D59-L000023](../../tests/test_connector_summary_counters.py#L23) | 23 | `"            \"result_count\": 0,"` | — |
| [SRC-DA61479D59-L000024](../../tests/test_connector_summary_counters.py#L24) | 24 | `"            \"rejected_count\": 0,"` | — |
| [SRC-DA61479D59-L000025](../../tests/test_connector_summary_counters.py#L25) | 25 | `"            \"error\": \"HTTP 500 token=secret-value\","` | — |
| [SRC-DA61479D59-L000026](../../tests/test_connector_summary_counters.py#L26) | 26 | `"        },"` | — |
| [SRC-DA61479D59-L000027](../../tests/test_connector_summary_counters.py#L27) | 27 | `"    ]"` | — |
| [SRC-DA61479D59-L000028](../../tests/test_connector_summary_counters.py#L28) | 28 | `"    sources = ["` | — |
| [SRC-DA61479D59-L000029](../../tests/test_connector_summary_counters.py#L29) | 29 | `"        {\"url\": \"https://example.com/a\", \"providers\": [\"duckduckgo_html\"]},"` | — |
| [SRC-DA61479D59-L000030](../../tests/test_connector_summary_counters.py#L30) | 30 | `"        {\"url\": \"https://example.org/b\", \"providers\": [\"bing_rss\"]},"` | — |
| [SRC-DA61479D59-L000031](../../tests/test_connector_summary_counters.py#L31) | 31 | `"    ]"` | — |
| [SRC-DA61479D59-L000032](../../tests/test_connector_summary_counters.py#L32) | 32 | `""` | — |
| [SRC-DA61479D59-L000033](../../tests/test_connector_summary_counters.py#L33) | 33 | `"    summary = agent._connector_status_summary(diagnostics, sources)"` | — |
| [SRC-DA61479D59-L000034](../../tests/test_connector_summary_counters.py#L34) | 34 | `""` | — |
| [SRC-DA61479D59-L000035](../../tests/test_connector_summary_counters.py#L35) | 35 | `"    duckduckgo = next(item for item in summary[\"connectors\"] if item[\"name\"] == \"duckduckgo_html\")"` | — |
| [SRC-DA61479D59-L000036](../../tests/test_connector_summary_counters.py#L36) | 36 | `"    brave = next(item for item in summary[\"connectors\"] if item[\"name\"] == \"brave_search_api\")"` | — |
| [SRC-DA61479D59-L000037](../../tests/test_connector_summary_counters.py#L37) | 37 | `"    assert summary[\"scope\"] == \"this_request_only\""` | — |
| [SRC-DA61479D59-L000038](../../tests/test_connector_summary_counters.py#L38) | 38 | `"    assert duckduckgo[\"attempted\"] is True"` | — |
| [SRC-DA61479D59-L000039](../../tests/test_connector_summary_counters.py#L39) | 39 | `"    assert duckduckgo[\"status\"] == \"failed\""` | — |
| [SRC-DA61479D59-L000040](../../tests/test_connector_summary_counters.py#L40) | 40 | `"    assert duckduckgo[\"observed_statuses\"] == [\"ok\", \"failed\"]"` | — |
| [SRC-DA61479D59-L000041](../../tests/test_connector_summary_counters.py#L41) | 41 | `"    assert duckduckgo[\"result_count\"] == 3"` | — |
| [SRC-DA61479D59-L000042](../../tests/test_connector_summary_counters.py#L42) | 42 | `"    assert duckduckgo[\"useful_result_count\"] == 1"` | — |
| [SRC-DA61479D59-L000043](../../tests/test_connector_summary_counters.py#L43) | 43 | `"    assert duckduckgo[\"rejected_count\"] == 1"` | — |
| [SRC-DA61479D59-L000044](../../tests/test_connector_summary_counters.py#L44) | 44 | `"    assert duckduckgo[\"implementation_status\"] == \"implemented_in_code\""` | — |
| [SRC-DA61479D59-L000045](../../tests/test_connector_summary_counters.py#L45) | 45 | `"    assert duckduckgo[\"available_for_this_request\"] is True"` | — |
| [SRC-DA61479D59-L000046](../../tests/test_connector_summary_counters.py#L46) | 46 | `"    assert duckduckgo[\"verified_for_this_request\"] is True"` | — |
| [SRC-DA61479D59-L000047](../../tests/test_connector_summary_counters.py#L47) | 47 | `"    assert duckduckgo[\"failure_observed\"] is True"` | — |
| [SRC-DA61479D59-L000048](../../tests/test_connector_summary_counters.py#L48) | 48 | `"    assert \"secret-value\" not in json.dumps(summary)"` | — |
| [SRC-DA61479D59-L000049](../../tests/test_connector_summary_counters.py#L49) | 49 | `"    assert brave[\"configured\"] is False"` | — |
| [SRC-DA61479D59-L000050](../../tests/test_connector_summary_counters.py#L50) | 50 | `"    assert brave[\"status\"] == \"not_configured\""` | — |
| [SRC-DA61479D59-L000051](../../tests/test_connector_summary_counters.py#L51) | 51 | `"    assert brave[\"available_for_this_request\"] is False"` | — |
| [SRC-DA61479D59-L000052](../../tests/test_connector_summary_counters.py#L52) | 52 | `"    assert brave[\"verified_for_this_request\"] is None"` | — |
| [SRC-DA61479D59-L000053](../../tests/test_connector_summary_counters.py#L53) | 53 | `""` | — |
| [SRC-DA61479D59-L000054](../../tests/test_connector_summary_counters.py#L54) | 54 | `""` | — |
| [SRC-DA61479D59-L000055](../../tests/test_connector_summary_counters.py#L55) | 55 | `"def test_collect_research_distinguishes_raw_rows_unique_urls_and_page_extraction(monkeypatch):"` | — |
| [SRC-DA61479D59-L000056](../../tests/test_connector_summary_counters.py#L56) | 56 | `"    agent = WebAgent()"` | — |
| [SRC-DA61479D59-L000057](../../tests/test_connector_summary_counters.py#L57) | 57 | `"    query = \"renewable energy storage\""` | — |
| [SRC-DA61479D59-L000058](../../tests/test_connector_summary_counters.py#L58) | 58 | `"    results = ["` | — |
| [SRC-DA61479D59-L000059](../../tests/test_connector_summary_counters.py#L59) | 59 | `"        {"` | — |
| [SRC-DA61479D59-L000060](../../tests/test_connector_summary_counters.py#L60) | 60 | `"            \"title\": \"Renewable energy storage report\","` | — |
| [SRC-DA61479D59-L000061](../../tests/test_connector_summary_counters.py#L61) | 61 | `"            \"url\": \"https://example.com/report\","` | — |
| [SRC-DA61479D59-L000062](../../tests/test_connector_summary_counters.py#L62) | 62 | `"            \"snippet\": \"Renewable energy storage data from the report\","` | — |
| [SRC-DA61479D59-L000063](../../tests/test_connector_summary_counters.py#L63) | 63 | `"            \"page_text\": \"\","` | — |
| [SRC-DA61479D59-L000064](../../tests/test_connector_summary_counters.py#L64) | 64 | `"            \"page_fetched\": False,"` | — |
| [SRC-DA61479D59-L000065](../../tests/test_connector_summary_counters.py#L65) | 65 | `"            \"provider\": \"test_search\","` | — |
| [SRC-DA61479D59-L000066](../../tests/test_connector_summary_counters.py#L66) | 66 | `"            \"provider_rank\": 1,"` | — |
| [SRC-DA61479D59-L000067](../../tests/test_connector_summary_counters.py#L67) | 67 | `"            \"search_query\": query,"` | — |
| [SRC-DA61479D59-L000068](../../tests/test_connector_summary_counters.py#L68) | 68 | `"            \"published_at\": \"\","` | — |
| [SRC-DA61479D59-L000069](../../tests/test_connector_summary_counters.py#L69) | 69 | `"        },"` | — |
| [SRC-DA61479D59-L000070](../../tests/test_connector_summary_counters.py#L70) | 70 | `"        {"` | — |
| [SRC-DA61479D59-L000071](../../tests/test_connector_summary_counters.py#L71) | 71 | `"            \"title\": \"Renewable energy storage report (duplicate URL)\","` | — |
| [SRC-DA61479D59-L000072](../../tests/test_connector_summary_counters.py#L72) | 72 | `"            \"url\": \"https://example.com/report?utm_source=test\","` | — |
| [SRC-DA61479D59-L000073](../../tests/test_connector_summary_counters.py#L73) | 73 | `"            \"snippet\": \"Renewable energy storage data from a duplicate result\","` | — |
| [SRC-DA61479D59-L000074](../../tests/test_connector_summary_counters.py#L74) | 74 | `"            \"page_text\": \"\","` | — |
| [SRC-DA61479D59-L000075](../../tests/test_connector_summary_counters.py#L75) | 75 | `"            \"page_fetched\": False,"` | — |
| [SRC-DA61479D59-L000076](../../tests/test_connector_summary_counters.py#L76) | 76 | `"            \"provider\": \"test_search\","` | — |
| [SRC-DA61479D59-L000077](../../tests/test_connector_summary_counters.py#L77) | 77 | `"            \"provider_rank\": 2,"` | — |
| [SRC-DA61479D59-L000078](../../tests/test_connector_summary_counters.py#L78) | 78 | `"            \"search_query\": query,"` | — |
| [SRC-DA61479D59-L000079](../../tests/test_connector_summary_counters.py#L79) | 79 | `"            \"published_at\": \"\","` | — |
| [SRC-DA61479D59-L000080](../../tests/test_connector_summary_counters.py#L80) | 80 | `"        },"` | — |
| [SRC-DA61479D59-L000081](../../tests/test_connector_summary_counters.py#L81) | 81 | `"        {"` | — |
| [SRC-DA61479D59-L000082](../../tests/test_connector_summary_counters.py#L82) | 82 | `"            \"title\": \"Renewable energy storage statistics\","` | — |
| [SRC-DA61479D59-L000083](../../tests/test_connector_summary_counters.py#L83) | 83 | `"            \"url\": \"https://example.org/statistics\","` | — |
| [SRC-DA61479D59-L000084](../../tests/test_connector_summary_counters.py#L84) | 84 | `"            \"snippet\": \"Renewable energy storage statistics\","` | — |
| [SRC-DA61479D59-L000085](../../tests/test_connector_summary_counters.py#L85) | 85 | `"            \"page_text\": \"\","` | — |
| [SRC-DA61479D59-L000086](../../tests/test_connector_summary_counters.py#L86) | 86 | `"            \"page_fetched\": False,"` | — |
| [SRC-DA61479D59-L000087](../../tests/test_connector_summary_counters.py#L87) | 87 | `"            \"provider\": \"test_search\","` | — |
| [SRC-DA61479D59-L000088](../../tests/test_connector_summary_counters.py#L88) | 88 | `"            \"provider_rank\": 3,"` | — |
| [SRC-DA61479D59-L000089](../../tests/test_connector_summary_counters.py#L89) | 89 | `"            \"search_query\": query,"` | — |
| [SRC-DA61479D59-L000090](../../tests/test_connector_summary_counters.py#L90) | 90 | `"            \"published_at\": \"\","` | — |
| [SRC-DA61479D59-L000091](../../tests/test_connector_summary_counters.py#L91) | 91 | `"        },"` | — |
| [SRC-DA61479D59-L000092](../../tests/test_connector_summary_counters.py#L92) | 92 | `"    ]"` | — |
| [SRC-DA61479D59-L000093](../../tests/test_connector_summary_counters.py#L93) | 93 | `""` | — |
| [SRC-DA61479D59-L000094](../../tests/test_connector_summary_counters.py#L94) | 94 | `"    monkeypatch.setattr(agent, \"_search_web\", lambda _query: results)"` | — |
| [SRC-DA61479D59-L000095](../../tests/test_connector_summary_counters.py#L95) | 95 | `"    def fetch(url: str):"` | — |
| [SRC-DA61479D59-L000096](../../tests/test_connector_summary_counters.py#L96) | 96 | `"        if \"example.com\" in url:"` | — |
| [SRC-DA61479D59-L000097](../../tests/test_connector_summary_counters.py#L97) | 97 | `"            return \"Report page\", \"Renewable energy storage page body with extracted text.\""` | — |
| [SRC-DA61479D59-L000098](../../tests/test_connector_summary_counters.py#L98) | 98 | `"        return \"\", \"\""` | — |
| [SRC-DA61479D59-L000099](../../tests/test_connector_summary_counters.py#L99) | 99 | `""` | — |
| [SRC-DA61479D59-L000100](../../tests/test_connector_summary_counters.py#L100) | 100 | `"    monkeypatch.setattr(agent, \"_fetch_page\", fetch)"` | — |
| [SRC-DA61479D59-L000101](../../tests/test_connector_summary_counters.py#L101) | 101 | `"    sources, warnings, report = agent._collect_research({"` | — |
| [SRC-DA61479D59-L000102](../../tests/test_connector_summary_counters.py#L102) | 102 | `"        \"queries\": [query],"` | — |
| [SRC-DA61479D59-L000103](../../tests/test_connector_summary_counters.py#L103) | 103 | `"        \"direct_urls\": [],"` | — |
| [SRC-DA61479D59-L000104](../../tests/test_connector_summary_counters.py#L104) | 104 | `"        \"social_focus\": False,"` | — |
| [SRC-DA61479D59-L000105](../../tests/test_connector_summary_counters.py#L105) | 105 | `"        \"freshness\": \"any\","` | — |
| [SRC-DA61479D59-L000106](../../tests/test_connector_summary_counters.py#L106) | 106 | `"        \"depth\": \"standard\","` | — |
| [SRC-DA61479D59-L000107](../../tests/test_connector_summary_counters.py#L107) | 107 | `"        \"platforms\": [],"` | — |
| [SRC-DA61479D59-L000108](../../tests/test_connector_summary_counters.py#L108) | 108 | `"        \"planning_method\": \"unit_test\","` | — |
| [SRC-DA61479D59-L000109](../../tests/test_connector_summary_counters.py#L109) | 109 | `"    })"` | — |
| [SRC-DA61479D59-L000110](../../tests/test_connector_summary_counters.py#L110) | 110 | `""` | — |
| [SRC-DA61479D59-L000111](../../tests/test_connector_summary_counters.py#L111) | 111 | `"    assert warnings"` | — |
| [SRC-DA61479D59-L000112](../../tests/test_connector_summary_counters.py#L112) | 112 | `"    assert report[\"raw_results\"] == 3"` | — |
| [SRC-DA61479D59-L000113](../../tests/test_connector_summary_counters.py#L113) | 113 | `"    assert report[\"unique_urls\"] == 2"` | — |
| [SRC-DA61479D59-L000114](../../tests/test_connector_summary_counters.py#L114) | 114 | `"    assert report[\"unique_sources\"] == 2"` | — |
| [SRC-DA61479D59-L000115](../../tests/test_connector_summary_counters.py#L115) | 115 | `"    assert report[\"pages_fetch_attempted\"] == 2"` | — |
| [SRC-DA61479D59-L000116](../../tests/test_connector_summary_counters.py#L116) | 116 | `"    assert report[\"pages_content_extracted\"] == 1"` | — |
| [SRC-DA61479D59-L000117](../../tests/test_connector_summary_counters.py#L117) | 117 | `"    assert report[\"pages_extract_failed\"] == 1"` | — |
| [SRC-DA61479D59-L000118](../../tests/test_connector_summary_counters.py#L118) | 118 | `"    assert report[\"page_fetch_status_counts\"][\"content_extracted\"] == 1"` | — |
| [SRC-DA61479D59-L000119](../../tests/test_connector_summary_counters.py#L119) | 119 | `"    assert report[\"page_fetch_status_counts\"][\"no_text_extracted\"] == 1"` | — |
| [SRC-DA61479D59-L000120](../../tests/test_connector_summary_counters.py#L120) | 120 | `"    assert report[\"page_fetch_status_counts\"][\"fetch_failed\"] == 0"` | — |
| [SRC-DA61479D59-L000121](../../tests/test_connector_summary_counters.py#L121) | 121 | `"    assert report[\"page_fetch_status_counts\"][\"partial_extraction\"] == 0"` | — |
| [SRC-DA61479D59-L000122](../../tests/test_connector_summary_counters.py#L122) | 122 | `"    assert report[\"pages_partial_extracted\"] == 0"` | — |
| [SRC-DA61479D59-L000123](../../tests/test_connector_summary_counters.py#L123) | 123 | `"    assert sum(source[\"page_fetch_status\"] == \"content_extracted\" for source in sources) == 1"` | — |
| [SRC-DA61479D59-L000124](../../tests/test_connector_summary_counters.py#L124) | 124 | `"    assert sum(source[\"page_fetch_status\"] == \"no_text_extracted\" for source in sources) == 1"` | — |
| [SRC-DA61479D59-L000125](../../tests/test_connector_summary_counters.py#L125) | 125 | `"    assert report[\"connector_summary\"][\"scope\"] == \"this_request_only\""` | — |
| [SRC-DA61479D59-L000126](../../tests/test_connector_summary_counters.py#L126) | 126 | `""` | — |
| [SRC-DA61479D59-L000127](../../tests/test_connector_summary_counters.py#L127) | 127 | `""` | — |
| [SRC-DA61479D59-L000128](../../tests/test_connector_summary_counters.py#L128) | 128 | `"def test_connector_summary_does_not_claim_timeout_or_budget_exhaustion_was_a_confirmed_attempt(monkeypatch):"` | — |
| [SRC-DA61479D59-L000129](../../tests/test_connector_summary_counters.py#L129) | 129 | `"    agent = WebAgent()"` | — |
| [SRC-DA61479D59-L000130](../../tests/test_connector_summary_counters.py#L130) | 130 | `"    monkeypatch.setenv(\"TAVILY_API_KEY\", \"configured-test-key\")"` | — |
| [SRC-DA61479D59-L000131](../../tests/test_connector_summary_counters.py#L131) | 131 | `"    monkeypatch.setenv(\"DEEPSEEK_SEARCH_API_KEY\", \"configured-test-key\")"` | — |
| [SRC-DA61479D59-L000132](../../tests/test_connector_summary_counters.py#L132) | 132 | `"    timeout = agent._connector_status_summary("` | — |
| [SRC-DA61479D59-L000133](../../tests/test_connector_summary_counters.py#L133) | 133 | `"        [{\"provider\": \"tavily_search_api\", \"query\": \"query\", \"status\": \"timeout\", \"error\": \"request timed out\"}],"` | — |
| [SRC-DA61479D59-L000134](../../tests/test_connector_summary_counters.py#L134) | 134 | `"        [],"` | — |
| [SRC-DA61479D59-L000135](../../tests/test_connector_summary_counters.py#L135) | 135 | `"    )"` | — |
| [SRC-DA61479D59-L000136](../../tests/test_connector_summary_counters.py#L136) | 136 | `"    exhausted = agent._connector_status_summary("` | — |
| [SRC-DA61479D59-L000137](../../tests/test_connector_summary_counters.py#L137) | 137 | `"        [{\"provider\": \"deepseek_search_api\", \"query\": \"query\", \"status\": \"budget_exhausted\"}],"` | — |
| [SRC-DA61479D59-L000138](../../tests/test_connector_summary_counters.py#L138) | 138 | `"        [],"` | — |
| [SRC-DA61479D59-L000139](../../tests/test_connector_summary_counters.py#L139) | 139 | `"    )"` | — |
| [SRC-DA61479D59-L000140](../../tests/test_connector_summary_counters.py#L140) | 140 | `"    tavily = next(item for item in timeout[\"connectors\"] if item[\"name\"] == \"tavily_search_api\")"` | — |
| [SRC-DA61479D59-L000141](../../tests/test_connector_summary_counters.py#L141) | 141 | `"    deepseek = next(item for item in exhausted[\"connectors\"] if item[\"name\"] == \"deepseek_search_api\")"` | — |
| [SRC-DA61479D59-L000142](../../tests/test_connector_summary_counters.py#L142) | 142 | `"    assert tavily[\"configured\"] is True"` | — |
| [SRC-DA61479D59-L000143](../../tests/test_connector_summary_counters.py#L143) | 143 | `"    assert tavily[\"attempted\"] is None"` | — |
| [SRC-DA61479D59-L000144](../../tests/test_connector_summary_counters.py#L144) | 144 | `"    assert tavily[\"status\"] == \"timeout\""` | — |
| [SRC-DA61479D59-L000145](../../tests/test_connector_summary_counters.py#L145) | 145 | `"    assert tavily[\"available_for_this_request\"] is None"` | — |
| [SRC-DA61479D59-L000146](../../tests/test_connector_summary_counters.py#L146) | 146 | `"    assert tavily[\"verified_for_this_request\"] is None"` | — |
| [SRC-DA61479D59-L000147](../../tests/test_connector_summary_counters.py#L147) | 147 | `"    assert tavily[\"failure_observed\"] is True"` | — |
| [SRC-DA61479D59-L000148](../../tests/test_connector_summary_counters.py#L148) | 148 | `"    assert deepseek[\"configured\"] is True"` | — |
| [SRC-DA61479D59-L000149](../../tests/test_connector_summary_counters.py#L149) | 149 | `"    assert deepseek[\"attempted\"] is False"` | — |
| [SRC-DA61479D59-L000150](../../tests/test_connector_summary_counters.py#L150) | 150 | `"    assert deepseek[\"status\"] == \"budget_exhausted\""` | — |
| [SRC-DA61479D59-L000151](../../tests/test_connector_summary_counters.py#L151) | 151 | `"    assert deepseek[\"available_for_this_request\"] is False"` | — |
| [SRC-DA61479D59-L000152](../../tests/test_connector_summary_counters.py#L152) | 152 | `"    assert deepseek[\"verified_for_this_request\"] is None"` | — |
| [SRC-DA61479D59-L000153](../../tests/test_connector_summary_counters.py#L153) | 153 | `""` | — |
| [SRC-DA61479D59-L000154](../../tests/test_connector_summary_counters.py#L154) | 154 | `""` | — |
| [SRC-DA61479D59-L000155](../../tests/test_connector_summary_counters.py#L155) | 155 | `"def test_collect_research_preserves_partial_and_http_failure_page_statuses(monkeypatch):"` | — |
| [SRC-DA61479D59-L000156](../../tests/test_connector_summary_counters.py#L156) | 156 | `"    agent = WebAgent()"` | — |
| [SRC-DA61479D59-L000157](../../tests/test_connector_summary_counters.py#L157) | 157 | `"    query = \"renewable energy storage\""` | — |
| [SRC-DA61479D59-L000158](../../tests/test_connector_summary_counters.py#L158) | 158 | `"    results = ["` | — |
| [SRC-DA61479D59-L000159](../../tests/test_connector_summary_counters.py#L159) | 159 | `"        {"` | — |
| [SRC-DA61479D59-L000160](../../tests/test_connector_summary_counters.py#L160) | 160 | `"            \"title\": \"Renewable energy storage report\","` | — |
| [SRC-DA61479D59-L000161](../../tests/test_connector_summary_counters.py#L161) | 161 | `"            \"url\": \"https://example.com/report\","` | — |
| [SRC-DA61479D59-L000162](../../tests/test_connector_summary_counters.py#L162) | 162 | `"            \"snippet\": \"Renewable energy storage report\","` | — |
| [SRC-DA61479D59-L000163](../../tests/test_connector_summary_counters.py#L163) | 163 | `"            \"page_text\": \"\","` | — |
| [SRC-DA61479D59-L000164](../../tests/test_connector_summary_counters.py#L164) | 164 | `"            \"page_fetched\": False,"` | — |
| [SRC-DA61479D59-L000165](../../tests/test_connector_summary_counters.py#L165) | 165 | `"            \"provider\": \"test_search\","` | — |
| [SRC-DA61479D59-L000166](../../tests/test_connector_summary_counters.py#L166) | 166 | `"            \"provider_rank\": 1,"` | — |
| [SRC-DA61479D59-L000167](../../tests/test_connector_summary_counters.py#L167) | 167 | `"            \"search_query\": query,"` | — |
| [SRC-DA61479D59-L000168](../../tests/test_connector_summary_counters.py#L168) | 168 | `"            \"published_at\": \"\","` | — |
| [SRC-DA61479D59-L000169](../../tests/test_connector_summary_counters.py#L169) | 169 | `"        },"` | — |
| [SRC-DA61479D59-L000170](../../tests/test_connector_summary_counters.py#L170) | 170 | `"        {"` | — |
| [SRC-DA61479D59-L000171](../../tests/test_connector_summary_counters.py#L171) | 171 | `"            \"title\": \"Renewable energy storage statistics\","` | — |
| [SRC-DA61479D59-L000172](../../tests/test_connector_summary_counters.py#L172) | 172 | `"            \"url\": \"https://example.org/statistics\","` | — |
| [SRC-DA61479D59-L000173](../../tests/test_connector_summary_counters.py#L173) | 173 | `"            \"snippet\": \"Renewable energy storage statistics\","` | — |
| [SRC-DA61479D59-L000174](../../tests/test_connector_summary_counters.py#L174) | 174 | `"            \"page_text\": \"\","` | — |
| [SRC-DA61479D59-L000175](../../tests/test_connector_summary_counters.py#L175) | 175 | `"            \"page_fetched\": False,"` | — |
| [SRC-DA61479D59-L000176](../../tests/test_connector_summary_counters.py#L176) | 176 | `"            \"provider\": \"test_search\","` | — |
| [SRC-DA61479D59-L000177](../../tests/test_connector_summary_counters.py#L177) | 177 | `"            \"provider_rank\": 2,"` | — |
| [SRC-DA61479D59-L000178](../../tests/test_connector_summary_counters.py#L178) | 178 | `"            \"search_query\": query,"` | — |
| [SRC-DA61479D59-L000179](../../tests/test_connector_summary_counters.py#L179) | 179 | `"            \"published_at\": \"\","` | — |
| [SRC-DA61479D59-L000180](../../tests/test_connector_summary_counters.py#L180) | 180 | `"        },"` | — |
| [SRC-DA61479D59-L000181](../../tests/test_connector_summary_counters.py#L181) | 181 | `"    ]"` | — |
| [SRC-DA61479D59-L000182](../../tests/test_connector_summary_counters.py#L182) | 182 | `"    monkeypatch.setattr(agent, \"_search_web\", lambda _query: results)"` | — |
| [SRC-DA61479D59-L000183](../../tests/test_connector_summary_counters.py#L183) | 183 | `""` | — |
| [SRC-DA61479D59-L000184](../../tests/test_connector_summary_counters.py#L184) | 184 | `"    def fetch(url: str):"` | — |
| [SRC-DA61479D59-L000185](../../tests/test_connector_summary_counters.py#L185) | 185 | `"        if \"example.com\" in url:"` | — |
| [SRC-DA61479D59-L000186](../../tests/test_connector_summary_counters.py#L186) | 186 | `"            return PageFetchResult("` | — |
| [SRC-DA61479D59-L000187](../../tests/test_connector_summary_counters.py#L187) | 187 | `"                \"Report page\","` | — |
| [SRC-DA61479D59-L000188](../../tests/test_connector_summary_counters.py#L188) | 188 | `"                \"Renewable energy storage body, with an explicit note that extraction was capped.\","` | — |
| [SRC-DA61479D59-L000189](../../tests/test_connector_summary_counters.py#L189) | 189 | `"                \"partial_extraction\","` | — |
| [SRC-DA61479D59-L000190](../../tests/test_connector_summary_counters.py#L190) | 190 | `"            )"` | — |
| [SRC-DA61479D59-L000191](../../tests/test_connector_summary_counters.py#L191) | 191 | `"        return PageFetchResult(\"\", \"\", \"http_error\", \"HTTPStatus\")"` | — |
| [SRC-DA61479D59-L000192](../../tests/test_connector_summary_counters.py#L192) | 192 | `""` | — |
| [SRC-DA61479D59-L000193](../../tests/test_connector_summary_counters.py#L193) | 193 | `"    monkeypatch.setattr(agent, \"_fetch_page\", fetch)"` | — |
| [SRC-DA61479D59-L000194](../../tests/test_connector_summary_counters.py#L194) | 194 | `"    sources, warnings, report = agent._collect_research({"` | — |
| [SRC-DA61479D59-L000195](../../tests/test_connector_summary_counters.py#L195) | 195 | `"        \"queries\": [query],"` | — |
| [SRC-DA61479D59-L000196](../../tests/test_connector_summary_counters.py#L196) | 196 | `"        \"direct_urls\": [],"` | — |
| [SRC-DA61479D59-L000197](../../tests/test_connector_summary_counters.py#L197) | 197 | `"        \"social_focus\": False,"` | — |
| [SRC-DA61479D59-L000198](../../tests/test_connector_summary_counters.py#L198) | 198 | `"        \"freshness\": \"any\","` | — |
| [SRC-DA61479D59-L000199](../../tests/test_connector_summary_counters.py#L199) | 199 | `"        \"depth\": \"standard\","` | — |
| [SRC-DA61479D59-L000200](../../tests/test_connector_summary_counters.py#L200) | 200 | `"        \"platforms\": [],"` | — |
| [SRC-DA61479D59-L000201](../../tests/test_connector_summary_counters.py#L201) | 201 | `"        \"planning_method\": \"unit_test\","` | — |
| [SRC-DA61479D59-L000202](../../tests/test_connector_summary_counters.py#L202) | 202 | `"    })"` | — |
| [SRC-DA61479D59-L000203](../../tests/test_connector_summary_counters.py#L203) | 203 | `""` | — |
| [SRC-DA61479D59-L000204](../../tests/test_connector_summary_counters.py#L204) | 204 | `"    assert warnings"` | — |
| [SRC-DA61479D59-L000205](../../tests/test_connector_summary_counters.py#L205) | 205 | `"    assert report[\"pages_fetch_attempted\"] == 2"` | — |
| [SRC-DA61479D59-L000206](../../tests/test_connector_summary_counters.py#L206) | 206 | `"    assert report[\"pages_content_extracted\"] == 1"` | — |
| [SRC-DA61479D59-L000207](../../tests/test_connector_summary_counters.py#L207) | 207 | `"    assert report[\"pages_partial_extracted\"] == 1"` | — |
| [SRC-DA61479D59-L000208](../../tests/test_connector_summary_counters.py#L208) | 208 | `"    assert report[\"pages_extract_failed\"] == 1"` | — |
| [SRC-DA61479D59-L000209](../../tests/test_connector_summary_counters.py#L209) | 209 | `"    assert report[\"page_fetch_status_counts\"][\"partial_extraction\"] == 1"` | — |
| [SRC-DA61479D59-L000210](../../tests/test_connector_summary_counters.py#L210) | 210 | `"    assert report[\"page_fetch_status_counts\"][\"http_error\"] == 1"` | — |
| [SRC-DA61479D59-L000211](../../tests/test_connector_summary_counters.py#L211) | 211 | `"    assert sum(item[\"page_fetch_status\"] == \"partial_extraction\" for item in sources) == 1"` | — |
| [SRC-DA61479D59-L000212](../../tests/test_connector_summary_counters.py#L212) | 212 | `"    assert sum(item[\"page_fetch_status\"] == \"http_error\" for item in sources) == 1"` | — |
| [SRC-DA61479D59-L000213](../../tests/test_connector_summary_counters.py#L213) | 213 | `"    assert any(\"HTTPStatus\" in str(item.get(\"page_fetch_error_class\")) for item in sources)"` | — |
| [SRC-DA61479D59-L000214](../../tests/test_connector_summary_counters.py#L214) | 214 | `""` | — |
| [SRC-DA61479D59-L000215](../../tests/test_connector_summary_counters.py#L215) | 215 | `""` | — |
| [SRC-DA61479D59-L000216](../../tests/test_connector_summary_counters.py#L216) | 216 | `"def test_raw_provider_diagnostics_redact_credentials_from_queries_and_errors():"` | — |
| [SRC-DA61479D59-L000217](../../tests/test_connector_summary_counters.py#L217) | 217 | `"    agent = WebAgent()"` | — |
| [SRC-DA61479D59-L000218](../../tests/test_connector_summary_counters.py#L218) | 218 | `"    agent._record_provider_diagnostic("` | — |
| [SRC-DA61479D59-L000219](../../tests/test_connector_summary_counters.py#L219) | 219 | `"        provider=\"test_provider\","` | — |
| [SRC-DA61479D59-L000220](../../tests/test_connector_summary_counters.py#L220) | 220 | `"        query=\"research API_KEY=query-secret\","` | — |
| [SRC-DA61479D59-L000221](../../tests/test_connector_summary_counters.py#L221) | 221 | `"        status=\"failed\","` | — |
| [SRC-DA61479D59-L000222](../../tests/test_connector_summary_counters.py#L222) | 222 | `"        error=("` | — |
| [SRC-DA61479D59-L000223](../../tests/test_connector_summary_counters.py#L223) | 223 | `"            \"Authorization: Bearer bearer-secret access_token=access-secret; \""` | — |
| [SRC-DA61479D59-L000224](../../tests/test_connector_summary_counters.py#L224) | 224 | `"            \"URL https://example.test/search?token=url-secret\""` | — |
| [SRC-DA61479D59-L000225](../../tests/test_connector_summary_counters.py#L225) | 225 | `"        ),"` | — |
| [SRC-DA61479D59-L000226](../../tests/test_connector_summary_counters.py#L226) | 226 | `"    )"` | — |
| [SRC-DA61479D59-L000227](../../tests/test_connector_summary_counters.py#L227) | 227 | `""` | — |
| [SRC-DA61479D59-L000228](../../tests/test_connector_summary_counters.py#L228) | 228 | `"    diagnostic_json = json.dumps(agent._provider_diagnostics, ensure_ascii=False)"` | — |
| [SRC-DA61479D59-L000229](../../tests/test_connector_summary_counters.py#L229) | 229 | `"    for secret in (\"query-secret\", \"bearer-secret\", \"access-secret\", \"url-secret\"):"` | — |
| [SRC-DA61479D59-L000230](../../tests/test_connector_summary_counters.py#L230) | 230 | `"        assert secret not in diagnostic_json"` | — |
| [SRC-DA61479D59-L000231](../../tests/test_connector_summary_counters.py#L231) | 231 | `"    assert \"[REDACTED]\" in diagnostic_json"` | — |
| [SRC-DA61479D59-L000232](../../tests/test_connector_summary_counters.py#L232) | 232 | `""` | — |
| [SRC-DA61479D59-L000233](../../tests/test_connector_summary_counters.py#L233) | 233 | `""` | — |
| [SRC-DA61479D59-L000234](../../tests/test_connector_summary_counters.py#L234) | 234 | `"def test_connector_summary_separates_raw_candidates_from_filtered_results():"` | — |
| [SRC-DA61479D59-L000235](../../tests/test_connector_summary_counters.py#L235) | 235 | `"    agent = WebAgent()"` | — |
| [SRC-DA61479D59-L000236](../../tests/test_connector_summary_counters.py#L236) | 236 | `"    summary = agent._connector_status_summary("` | — |
| [SRC-DA61479D59-L000237](../../tests/test_connector_summary_counters.py#L237) | 237 | `"        [{"` | — |
| [SRC-DA61479D59-L000238](../../tests/test_connector_summary_counters.py#L238) | 238 | `"            \"provider\": \"bing_rss\","` | — |
| [SRC-DA61479D59-L000239](../../tests/test_connector_summary_counters.py#L239) | 239 | `"            \"query\": \"Arabic question with source instructions\","` | — |
| [SRC-DA61479D59-L000240](../../tests/test_connector_summary_counters.py#L240) | 240 | `"            \"status\": \"filtered_all\","` | — |
| [SRC-DA61479D59-L000241](../../tests/test_connector_summary_counters.py#L241) | 241 | `"            \"result_count\": 6,"` | — |
| [SRC-DA61479D59-L000242](../../tests/test_connector_summary_counters.py#L242) | 242 | `"            \"accepted_count\": 0,"` | — |
| [SRC-DA61479D59-L000243](../../tests/test_connector_summary_counters.py#L243) | 243 | `"            \"rejected_count\": 6,"` | — |
| [SRC-DA61479D59-L000244](../../tests/test_connector_summary_counters.py#L244) | 244 | `"            \"rejection_counts\": {"` | — |
| [SRC-DA61479D59-L000245](../../tests/test_connector_summary_counters.py#L245) | 245 | `"                \"malformed_candidate\": 0,"` | — |
| [SRC-DA61479D59-L000246](../../tests/test_connector_summary_counters.py#L246) | 246 | `"                \"invalid_url_or_unsafe_target\": 2,"` | — |
| [SRC-DA61479D59-L000247](../../tests/test_connector_summary_counters.py#L247) | 247 | `"                \"blocked_domain\": 1,"` | — |
| [SRC-DA61479D59-L000248](../../tests/test_connector_summary_counters.py#L248) | 248 | `"                \"relevance_below_threshold\": 3,"` | — |
| [SRC-DA61479D59-L000249](../../tests/test_connector_summary_counters.py#L249) | 249 | `"            },"` | — |
| [SRC-DA61479D59-L000250](../../tests/test_connector_summary_counters.py#L250) | 250 | `"            \"error\": \"all candidates rejected; invalid_url_or_unsafe_target=2, blocked_domain=1, relevance_below_threshold=3\","` | — |
| [SRC-DA61479D59-L000251](../../tests/test_connector_summary_counters.py#L251) | 251 | `"        }],"` | — |
| [SRC-DA61479D59-L000252](../../tests/test_connector_summary_counters.py#L252) | 252 | `"        [],"` | — |
| [SRC-DA61479D59-L000253](../../tests/test_connector_summary_counters.py#L253) | 253 | `"    )"` | — |
| [SRC-DA61479D59-L000254](../../tests/test_connector_summary_counters.py#L254) | 254 | `"    bing = next(item for item in summary[\"connectors\"] if item[\"name\"] == \"bing_rss\")"` | — |
| [SRC-DA61479D59-L000255](../../tests/test_connector_summary_counters.py#L255) | 255 | `"    assert bing[\"attempted\"] is True"` | — |
| [SRC-DA61479D59-L000256](../../tests/test_connector_summary_counters.py#L256) | 256 | `"    assert bing[\"result_count\"] == 6"` | — |
| [SRC-DA61479D59-L000257](../../tests/test_connector_summary_counters.py#L257) | 257 | `"    assert bing[\"accepted_count\"] == 0"` | — |
| [SRC-DA61479D59-L000258](../../tests/test_connector_summary_counters.py#L258) | 258 | `"    assert bing[\"rejected_count\"] == 6"` | — |
| [SRC-DA61479D59-L000259](../../tests/test_connector_summary_counters.py#L259) | 259 | `"    assert bing[\"rejection_counts_observed\"] is True"` | — |
| [SRC-DA61479D59-L000260](../../tests/test_connector_summary_counters.py#L260) | 260 | `"    assert bing[\"rejection_counts\"] == {"` | — |
| [SRC-DA61479D59-L000261](../../tests/test_connector_summary_counters.py#L261) | 261 | `"        \"malformed_candidate\": 0,"` | — |
| [SRC-DA61479D59-L000262](../../tests/test_connector_summary_counters.py#L262) | 262 | `"        \"invalid_url_or_unsafe_target\": 2,"` | — |
| [SRC-DA61479D59-L000263](../../tests/test_connector_summary_counters.py#L263) | 263 | `"        \"blocked_domain\": 1,"` | — |
| [SRC-DA61479D59-L000264](../../tests/test_connector_summary_counters.py#L264) | 264 | `"        \"relevance_below_threshold\": 3,"` | — |
| [SRC-DA61479D59-L000265](../../tests/test_connector_summary_counters.py#L265) | 265 | `"    }"` | — |
| [SRC-DA61479D59-L000266](../../tests/test_connector_summary_counters.py#L266) | 266 | `"    assert sum(bing[\"rejection_counts\"].values()) == bing[\"rejected_count\"]"` | — |
| [SRC-DA61479D59-L000267](../../tests/test_connector_summary_counters.py#L267) | 267 | `"    assert bing[\"candidate_rejection_observed\"] is True"` | — |
| [SRC-DA61479D59-L000268](../../tests/test_connector_summary_counters.py#L268) | 268 | `"    assert bing[\"available_for_this_request\"] is True"` | — |
| [SRC-DA61479D59-L000269](../../tests/test_connector_summary_counters.py#L269) | 269 | `"    assert bing[\"verified_for_this_request\"] is True"` | — |
| [SRC-DA61479D59-L000270](../../tests/test_connector_summary_counters.py#L270) | 270 | `""` | — |
| [SRC-DA61479D59-L000271](../../tests/test_connector_summary_counters.py#L271) | 271 | `""` | — |
| [SRC-DA61479D59-L000272](../../tests/test_connector_summary_counters.py#L272) | 272 | `"def test_connector_summary_does_not_present_partial_legacy_rejection_counts_as_complete():"` | — |
| [SRC-DA61479D59-L000273](../../tests/test_connector_summary_counters.py#L273) | 273 | `"    agent = WebAgent()"` | — |
| [SRC-DA61479D59-L000274](../../tests/test_connector_summary_counters.py#L274) | 274 | `"    summary = agent._connector_status_summary("` | — |
| [SRC-DA61479D59-L000275](../../tests/test_connector_summary_counters.py#L275) | 275 | `"        ["` | — |
| [SRC-DA61479D59-L000276](../../tests/test_connector_summary_counters.py#L276) | 276 | `"            {"` | — |
| [SRC-DA61479D59-L000277](../../tests/test_connector_summary_counters.py#L277) | 277 | `"                \"provider\": \"bing_rss\","` | — |
| [SRC-DA61479D59-L000278](../../tests/test_connector_summary_counters.py#L278) | 278 | `"                \"query\": \"first query\","` | — |
| [SRC-DA61479D59-L000279](../../tests/test_connector_summary_counters.py#L279) | 279 | `"                \"status\": \"filtered_all\","` | — |
| [SRC-DA61479D59-L000280](../../tests/test_connector_summary_counters.py#L280) | 280 | `"                \"result_count\": 3,"` | — |
| [SRC-DA61479D59-L000281](../../tests/test_connector_summary_counters.py#L281) | 281 | `"                \"accepted_count\": 0,"` | — |
| [SRC-DA61479D59-L000282](../../tests/test_connector_summary_counters.py#L282) | 282 | `"                \"rejected_count\": 3,"` | — |
| [SRC-DA61479D59-L000283](../../tests/test_connector_summary_counters.py#L283) | 283 | `"            },"` | — |
| [SRC-DA61479D59-L000284](../../tests/test_connector_summary_counters.py#L284) | 284 | `"            {"` | — |
| [SRC-DA61479D59-L000285](../../tests/test_connector_summary_counters.py#L285) | 285 | `"                \"provider\": \"bing_rss\","` | — |
| [SRC-DA61479D59-L000286](../../tests/test_connector_summary_counters.py#L286) | 286 | `"                \"query\": \"second query\","` | — |
| [SRC-DA61479D59-L000287](../../tests/test_connector_summary_counters.py#L287) | 287 | `"                \"status\": \"filtered_all\","` | — |
| [SRC-DA61479D59-L000288](../../tests/test_connector_summary_counters.py#L288) | 288 | `"                \"result_count\": 2,"` | — |
| [SRC-DA61479D59-L000289](../../tests/test_connector_summary_counters.py#L289) | 289 | `"                \"accepted_count\": 0,"` | — |
| [SRC-DA61479D59-L000290](../../tests/test_connector_summary_counters.py#L290) | 290 | `"                \"rejected_count\": 2,"` | — |
| [SRC-DA61479D59-L000291](../../tests/test_connector_summary_counters.py#L291) | 291 | `"                \"rejection_counts\": {"` | — |
| [SRC-DA61479D59-L000292](../../tests/test_connector_summary_counters.py#L292) | 292 | `"                    \"malformed_candidate\": 0,"` | — |
| [SRC-DA61479D59-L000293](../../tests/test_connector_summary_counters.py#L293) | 293 | `"                    \"invalid_url_or_unsafe_target\": 0,"` | — |
| [SRC-DA61479D59-L000294](../../tests/test_connector_summary_counters.py#L294) | 294 | `"                    \"blocked_domain\": 0,"` | — |
| [SRC-DA61479D59-L000295](../../tests/test_connector_summary_counters.py#L295) | 295 | `"                    \"relevance_below_threshold\": 2,"` | — |
| [SRC-DA61479D59-L000296](../../tests/test_connector_summary_counters.py#L296) | 296 | `"                },"` | — |
| [SRC-DA61479D59-L000297](../../tests/test_connector_summary_counters.py#L297) | 297 | `"            },"` | — |
| [SRC-DA61479D59-L000298](../../tests/test_connector_summary_counters.py#L298) | 298 | `"        ],"` | — |
| [SRC-DA61479D59-L000299](../../tests/test_connector_summary_counters.py#L299) | 299 | `"        [],"` | — |
| [SRC-DA61479D59-L000300](../../tests/test_connector_summary_counters.py#L300) | 300 | `"    )"` | — |
| [SRC-DA61479D59-L000301](../../tests/test_connector_summary_counters.py#L301) | 301 | `"    bing = next(item for item in summary[\"connectors\"] if item[\"name\"] == \"bing_rss\")"` | — |
| [SRC-DA61479D59-L000302](../../tests/test_connector_summary_counters.py#L302) | 302 | `"    assert bing[\"rejected_count\"] == 5"` | — |
| [SRC-DA61479D59-L000303](../../tests/test_connector_summary_counters.py#L303) | 303 | `"    assert bing[\"rejection_counts_observed\"] is False"` | — |
| [SRC-DA61479D59-L000304](../../tests/test_connector_summary_counters.py#L304) | 304 | `"    assert bing[\"rejection_counts\"] is None"` | — |
## اختبارات

### FILE-3D0A619359 — [tests/test_dashboard_security.py](../../tests/test_dashboard_security.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-3D0A619359-L000001](../../tests/test_dashboard_security.py#L1) | 1 | `"\"\"\"Static regression checks for sensitive lead-dashboard browser behavior.\"\"\""` | — |
| [SRC-3D0A619359-L000002](../../tests/test_dashboard_security.py#L2) | 2 | `"from pathlib import Path"` | — |
| [SRC-3D0A619359-L000003](../../tests/test_dashboard_security.py#L3) | 3 | `""` | — |
| [SRC-3D0A619359-L000004](../../tests/test_dashboard_security.py#L4) | 4 | `"DASHBOARD = Path(__file__).resolve().parents[1] / \"web\" / \"dashboard.html\""` | — |
| [SRC-3D0A619359-L000005](../../tests/test_dashboard_security.py#L5) | 5 | `""` | — |
| [SRC-3D0A619359-L000006](../../tests/test_dashboard_security.py#L6) | 6 | `""` | — |
| [SRC-3D0A619359-L000007](../../tests/test_dashboard_security.py#L7) | 7 | `"def test_hosted_lead_dashboard_can_send_the_private_access_token():"` | — |
| [SRC-3D0A619359-L000008](../../tests/test_dashboard_security.py#L8) | 8 | `"    html = DASHBOARD.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000009](../../tests/test_dashboard_security.py#L9) | 9 | `"    assert 'const ACCESS_TOKEN_STORAGE_KEY=\"omarai_access_token\"' in html"` | — |
| [SRC-3D0A619359-L000010](../../tests/test_dashboard_security.py#L10) | 10 | `"    assert 'headers.Authorization=\"Bearer \"+token' in html"` | — |
| [SRC-3D0A619359-L000011](../../tests/test_dashboard_security.py#L11) | 11 | `"    assert '$(\"saveAccessToken\").onclick' in html"` | — |
| [SRC-3D0A619359-L000012](../../tests/test_dashboard_security.py#L12) | 12 | `""` | — |
| [SRC-3D0A619359-L000013](../../tests/test_dashboard_security.py#L13) | 13 | `""` | — |
| [SRC-3D0A619359-L000014](../../tests/test_dashboard_security.py#L14) | 14 | `"def test_saved_lead_source_links_reject_non_http_schemes():"` | — |
| [SRC-3D0A619359-L000015](../../tests/test_dashboard_security.py#L15) | 15 | `"    html = DASHBOARD.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000016](../../tests/test_dashboard_security.py#L16) | 16 | `"    assert \"function safeSourceUrl(value)\" in html"` | — |
| [SRC-3D0A619359-L000017](../../tests/test_dashboard_security.py#L17) | 17 | `"    assert '[\"http:\",\"https:\"]' in html"` | — |
| [SRC-3D0A619359-L000018](../../tests/test_dashboard_security.py#L18) | 18 | `"    assert \"const sourceUrl=safeSourceUrl(l.source_url)\" in html"` | — |
| [SRC-3D0A619359-L000019](../../tests/test_dashboard_security.py#L19) | 19 | `"    assert \"const sourceLink=sourceUrl?\" in html"` | — |
## اختبارات

### FILE-6BCB799CEC — [tests/test_evidence_provenance.py](../../tests/test_evidence_provenance.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6BCB799CEC-L000001](../../tests/test_evidence_provenance.py#L1) | 1 | `"\"\"\"Regression tests for evidence provenance and pinned public-page retrieval.\"\"\""` | — |
| [SRC-6BCB799CEC-L000002](../../tests/test_evidence_provenance.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-6BCB799CEC-L000003](../../tests/test_evidence_provenance.py#L3) | 3 | `""` | — |
| [SRC-6BCB799CEC-L000004](../../tests/test_evidence_provenance.py#L4) | 4 | `"import socket"` | — |
| [SRC-6BCB799CEC-L000005](../../tests/test_evidence_provenance.py#L5) | 5 | `""` | — |
| [SRC-6BCB799CEC-L000006](../../tests/test_evidence_provenance.py#L6) | 6 | `"import pytest"` | — |
| [SRC-6BCB799CEC-L000007](../../tests/test_evidence_provenance.py#L7) | 7 | `""` | — |
| [SRC-6BCB799CEC-L000008](../../tests/test_evidence_provenance.py#L8) | 8 | `"from agents.web_agent import WebAgent, _public_ip_literals"` | — |
| [SRC-6BCB799CEC-L000009](../../tests/test_evidence_provenance.py#L9) | 9 | `""` | — |
| [SRC-6BCB799CEC-L000010](../../tests/test_evidence_provenance.py#L10) | 10 | `""` | — |
| [SRC-6BCB799CEC-L000011](../../tests/test_evidence_provenance.py#L11) | 11 | `"def _addrinfo(ip: str):"` | — |
| [SRC-6BCB799CEC-L000012](../../tests/test_evidence_provenance.py#L12) | 12 | `"    family = socket.AF_INET6 if \":\" in ip else socket.AF_INET"` | — |
| [SRC-6BCB799CEC-L000013](../../tests/test_evidence_provenance.py#L13) | 13 | `"    return [(family, socket.SOCK_STREAM, 6, \"\", (ip, 0))]"` | — |
| [SRC-6BCB799CEC-L000014](../../tests/test_evidence_provenance.py#L14) | 14 | `""` | — |
| [SRC-6BCB799CEC-L000015](../../tests/test_evidence_provenance.py#L15) | 15 | `""` | — |
| [SRC-6BCB799CEC-L000016](../../tests/test_evidence_provenance.py#L16) | 16 | `"def test_failed_page_read_is_not_reported_as_fetched(monkeypatch):"` | — |
| [SRC-6BCB799CEC-L000017](../../tests/test_evidence_provenance.py#L17) | 17 | `"    \"\"\"An empty extraction must not set page_fetched through the real collector.\"\"\""` | — |
| [SRC-6BCB799CEC-L000018](../../tests/test_evidence_provenance.py#L18) | 18 | `"    agent = WebAgent()"` | — |
| [SRC-6BCB799CEC-L000019](../../tests/test_evidence_provenance.py#L19) | 19 | `""` | — |
| [SRC-6BCB799CEC-L000020](../../tests/test_evidence_provenance.py#L20) | 20 | `"    def search(query):"` | — |
| [SRC-6BCB799CEC-L000021](../../tests/test_evidence_provenance.py#L21) | 21 | `"        return [{"` | — |
| [SRC-6BCB799CEC-L000022](../../tests/test_evidence_provenance.py#L22) | 22 | `"            \"title\": \"عنوان فقط\","` | — |
| [SRC-6BCB799CEC-L000023](../../tests/test_evidence_provenance.py#L23) | 23 | `"            \"url\": \"https://example.com/unread\","` | — |
| [SRC-6BCB799CEC-L000024](../../tests/test_evidence_provenance.py#L24) | 24 | `"            \"snippet\": \"مقتطف محرك بحث\","` | — |
| [SRC-6BCB799CEC-L000025](../../tests/test_evidence_provenance.py#L25) | 25 | `"            \"provider\": \"duckduckgo_html\","` | — |
| [SRC-6BCB799CEC-L000026](../../tests/test_evidence_provenance.py#L26) | 26 | `"            \"provider_rank\": 1,"` | — |
| [SRC-6BCB799CEC-L000027](../../tests/test_evidence_provenance.py#L27) | 27 | `"            \"search_query\": query,"` | — |
| [SRC-6BCB799CEC-L000028](../../tests/test_evidence_provenance.py#L28) | 28 | `"            \"published_at\": \"\","` | — |
| [SRC-6BCB799CEC-L000029](../../tests/test_evidence_provenance.py#L29) | 29 | `"        }]"` | — |
| [SRC-6BCB799CEC-L000030](../../tests/test_evidence_provenance.py#L30) | 30 | `""` | — |
| [SRC-6BCB799CEC-L000031](../../tests/test_evidence_provenance.py#L31) | 31 | `"    monkeypatch.setattr(agent, \"_search_web\", search)"` | — |
| [SRC-6BCB799CEC-L000032](../../tests/test_evidence_provenance.py#L32) | 32 | `"    monkeypatch.setattr(agent, \"_search_news\", lambda query: [])"` | — |
| [SRC-6BCB799CEC-L000033](../../tests/test_evidence_provenance.py#L33) | 33 | `"    monkeypatch.setattr(agent, \"_search_social\", lambda query, platforms: ([], []))"` | — |
| [SRC-6BCB799CEC-L000034](../../tests/test_evidence_provenance.py#L34) | 34 | `"    monkeypatch.setattr(agent, \"_fetch_page\", lambda url: (\"\", \"\"))"` | — |
| [SRC-6BCB799CEC-L000035](../../tests/test_evidence_provenance.py#L35) | 35 | `""` | — |
| [SRC-6BCB799CEC-L000036](../../tests/test_evidence_provenance.py#L36) | 36 | `"    sources, warnings, report = agent._collect_research({"` | — |
| [SRC-6BCB799CEC-L000037](../../tests/test_evidence_provenance.py#L37) | 37 | `"        \"queries\": [\"سؤال دون قراءة صفحة\"],"` | — |
| [SRC-6BCB799CEC-L000038](../../tests/test_evidence_provenance.py#L38) | 38 | `"        \"direct_urls\": [],"` | — |
| [SRC-6BCB799CEC-L000039](../../tests/test_evidence_provenance.py#L39) | 39 | `"        \"social_focus\": False,"` | — |
| [SRC-6BCB799CEC-L000040](../../tests/test_evidence_provenance.py#L40) | 40 | `"        \"freshness\": \"any\","` | — |
| [SRC-6BCB799CEC-L000041](../../tests/test_evidence_provenance.py#L41) | 41 | `"        \"depth\": \"standard\","` | — |
| [SRC-6BCB799CEC-L000042](../../tests/test_evidence_provenance.py#L42) | 42 | `"        \"platforms\": [],"` | — |
| [SRC-6BCB799CEC-L000043](../../tests/test_evidence_provenance.py#L43) | 43 | `"        \"planning_method\": \"test\","` | — |
| [SRC-6BCB799CEC-L000044](../../tests/test_evidence_provenance.py#L44) | 44 | `"    })"` | — |
| [SRC-6BCB799CEC-L000045](../../tests/test_evidence_provenance.py#L45) | 45 | `""` | — |
| [SRC-6BCB799CEC-L000046](../../tests/test_evidence_provenance.py#L46) | 46 | `"    assert any(\"لم يمكن استخراج نص\" in warning for warning in warnings)"` | — |
| [SRC-6BCB799CEC-L000047](../../tests/test_evidence_provenance.py#L47) | 47 | `"    assert len(sources) == 1"` | — |
| [SRC-6BCB799CEC-L000048](../../tests/test_evidence_provenance.py#L48) | 48 | `"    assert sources[0][\"url\"] == \"https://example.com/unread\""` | — |
| [SRC-6BCB799CEC-L000049](../../tests/test_evidence_provenance.py#L49) | 49 | `"    assert sources[0].get(\"page_fetched\") is not True"` | — |
| [SRC-6BCB799CEC-L000050](../../tests/test_evidence_provenance.py#L50) | 50 | `"    assert report[\"pages_fetched\"] == 0"` | — |
| [SRC-6BCB799CEC-L000051](../../tests/test_evidence_provenance.py#L51) | 51 | `"    assert report[\"queries_attempted\"] == 1"` | — |
| [SRC-6BCB799CEC-L000052](../../tests/test_evidence_provenance.py#L52) | 52 | `"    assert report[\"unique_sources\"] == 1"` | — |
| [SRC-6BCB799CEC-L000053](../../tests/test_evidence_provenance.py#L53) | 53 | `""` | — |
| [SRC-6BCB799CEC-L000054](../../tests/test_evidence_provenance.py#L54) | 54 | `""` | — |
| [SRC-6BCB799CEC-L000055](../../tests/test_evidence_provenance.py#L55) | 55 | `"def test_openrouter_citations_stay_unread_in_public_answer(monkeypatch):"` | — |
| [SRC-6BCB799CEC-L000056](../../tests/test_evidence_provenance.py#L56) | 56 | `"    \"\"\"Server-side citations must not be misreported as direct source-page reads.\"\"\""` | — |
| [SRC-6BCB799CEC-L000057](../../tests/test_evidence_provenance.py#L57) | 57 | `"    agent = WebAgent()"` | — |
| [SRC-6BCB799CEC-L000058](../../tests/test_evidence_provenance.py#L58) | 58 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-6BCB799CEC-L000059](../../tests/test_evidence_provenance.py#L59) | 59 | `"    question = \"ما آخر المعلومات؟\""` | — |
| [SRC-6BCB799CEC-L000060](../../tests/test_evidence_provenance.py#L60) | 60 | `""` | — |
| [SRC-6BCB799CEC-L000061](../../tests/test_evidence_provenance.py#L61) | 61 | `"    def collect(plan):"` | — |
| [SRC-6BCB799CEC-L000062](../../tests/test_evidence_provenance.py#L62) | 62 | `"        sources = ["` | — |
| [SRC-6BCB799CEC-L000063](../../tests/test_evidence_provenance.py#L63) | 63 | `"            {"` | — |
| [SRC-6BCB799CEC-L000064](../../tests/test_evidence_provenance.py#L64) | 64 | `"                \"title\": \"آخر المعلومات عن التقنية\","` | — |
| [SRC-6BCB799CEC-L000065](../../tests/test_evidence_provenance.py#L65) | 65 | `"                \"url\": \"https://alpha.example.com/report\","` | — |
| [SRC-6BCB799CEC-L000066](../../tests/test_evidence_provenance.py#L66) | 66 | `"                \"snippet\": \"معلومات حديثة عن الموضوع\","` | — |
| [SRC-6BCB799CEC-L000067](../../tests/test_evidence_provenance.py#L67) | 67 | `"                \"page_text\": \"\","` | — |
| [SRC-6BCB799CEC-L000068](../../tests/test_evidence_provenance.py#L68) | 68 | `"                \"page_fetched\": False,"` | — |
| [SRC-6BCB799CEC-L000069](../../tests/test_evidence_provenance.py#L69) | 69 | `"                \"provider\": \"bing_rss\","` | — |
| [SRC-6BCB799CEC-L000070](../../tests/test_evidence_provenance.py#L70) | 70 | `"                \"providers\": [\"bing_rss\"],"` | — |
| [SRC-6BCB799CEC-L000071](../../tests/test_evidence_provenance.py#L71) | 71 | `"                \"queries\": [question],"` | — |
| [SRC-6BCB799CEC-L000072](../../tests/test_evidence_provenance.py#L72) | 72 | `"                \"domain\": \"alpha.example.com\","` | — |
| [SRC-6BCB799CEC-L000073](../../tests/test_evidence_provenance.py#L73) | 73 | `"                \"source_class\": \"general\","` | — |
| [SRC-6BCB799CEC-L000074](../../tests/test_evidence_provenance.py#L74) | 74 | `"                \"platform\": \"web\","` | — |
| [SRC-6BCB799CEC-L000075](../../tests/test_evidence_provenance.py#L75) | 75 | `"                \"published_at\": \"\","` | — |
| [SRC-6BCB799CEC-L000076](../../tests/test_evidence_provenance.py#L76) | 76 | `"                \"rank_score\": 0.8,"` | — |
| [SRC-6BCB799CEC-L000077](../../tests/test_evidence_provenance.py#L77) | 77 | `"            },"` | — |
| [SRC-6BCB799CEC-L000078](../../tests/test_evidence_provenance.py#L78) | 78 | `"            {"` | — |
| [SRC-6BCB799CEC-L000079](../../tests/test_evidence_provenance.py#L79) | 79 | `"                \"title\": \"آخر المعلومات من مصدر مستقل\","` | — |
| [SRC-6BCB799CEC-L000080](../../tests/test_evidence_provenance.py#L80) | 80 | `"                \"url\": \"https://beta.example.org/report\","` | — |
| [SRC-6BCB799CEC-L000081](../../tests/test_evidence_provenance.py#L81) | 81 | `"                \"snippet\": \"معلومات موثقة عن الموضوع\","` | — |
| [SRC-6BCB799CEC-L000082](../../tests/test_evidence_provenance.py#L82) | 82 | `"                \"page_text\": \"\","` | — |
| [SRC-6BCB799CEC-L000083](../../tests/test_evidence_provenance.py#L83) | 83 | `"                \"page_fetched\": False,"` | — |
| [SRC-6BCB799CEC-L000084](../../tests/test_evidence_provenance.py#L84) | 84 | `"                \"provider\": \"duckduckgo_html\","` | — |
| [SRC-6BCB799CEC-L000085](../../tests/test_evidence_provenance.py#L85) | 85 | `"                \"providers\": [\"duckduckgo_html\"],"` | — |
| [SRC-6BCB799CEC-L000086](../../tests/test_evidence_provenance.py#L86) | 86 | `"                \"queries\": [question],"` | — |
| [SRC-6BCB799CEC-L000087](../../tests/test_evidence_provenance.py#L87) | 87 | `"                \"domain\": \"beta.example.org\","` | — |
| [SRC-6BCB799CEC-L000088](../../tests/test_evidence_provenance.py#L88) | 88 | `"                \"source_class\": \"general\","` | — |
| [SRC-6BCB799CEC-L000089](../../tests/test_evidence_provenance.py#L89) | 89 | `"                \"platform\": \"web\","` | — |
| [SRC-6BCB799CEC-L000090](../../tests/test_evidence_provenance.py#L90) | 90 | `"                \"published_at\": \"\","` | — |
| [SRC-6BCB799CEC-L000091](../../tests/test_evidence_provenance.py#L91) | 91 | `"                \"rank_score\": 0.7,"` | — |
| [SRC-6BCB799CEC-L000092](../../tests/test_evidence_provenance.py#L92) | 92 | `"            },"` | — |
| [SRC-6BCB799CEC-L000093](../../tests/test_evidence_provenance.py#L93) | 93 | `"        ]"` | — |
| [SRC-6BCB799CEC-L000094](../../tests/test_evidence_provenance.py#L94) | 94 | `"        return sources, [], {"` | — |
| [SRC-6BCB799CEC-L000095](../../tests/test_evidence_provenance.py#L95) | 95 | `"            \"queries_planned\": 1,"` | — |
| [SRC-6BCB799CEC-L000096](../../tests/test_evidence_provenance.py#L96) | 96 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-6BCB799CEC-L000097](../../tests/test_evidence_provenance.py#L97) | 97 | `"            \"query_results\": [{\"query\": question, \"results\": 2}],"` | — |
| [SRC-6BCB799CEC-L000098](../../tests/test_evidence_provenance.py#L98) | 98 | `"            \"unique_sources\": 2,"` | — |
| [SRC-6BCB799CEC-L000099](../../tests/test_evidence_provenance.py#L99) | 99 | `"            \"pages_fetched\": 0,"` | — |
| [SRC-6BCB799CEC-L000100](../../tests/test_evidence_provenance.py#L100) | 100 | `"            \"providers_used\": [\"bing_rss\", \"duckduckgo_html\"],"` | — |
| [SRC-6BCB799CEC-L000101](../../tests/test_evidence_provenance.py#L101) | 101 | `"            \"provider_counts\": {\"bing_rss\": 1, \"duckduckgo_html\": 1},"` | — |
| [SRC-6BCB799CEC-L000102](../../tests/test_evidence_provenance.py#L102) | 102 | `"            \"platform_counts\": {\"web\": 2},"` | — |
| [SRC-6BCB799CEC-L000103](../../tests/test_evidence_provenance.py#L103) | 103 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-6BCB799CEC-L000104](../../tests/test_evidence_provenance.py#L104) | 104 | `"            \"expansion_queries\": [],"` | — |
| [SRC-6BCB799CEC-L000105](../../tests/test_evidence_provenance.py#L105) | 105 | `"            \"evidence_signals\": {},"` | — |
| [SRC-6BCB799CEC-L000106](../../tests/test_evidence_provenance.py#L106) | 106 | `"            \"depth\": \"standard\","` | — |
| [SRC-6BCB799CEC-L000107](../../tests/test_evidence_provenance.py#L107) | 107 | `"            \"planning_method\": \"test\","` | — |
| [SRC-6BCB799CEC-L000108](../../tests/test_evidence_provenance.py#L108) | 108 | `"        }"` | — |
| [SRC-6BCB799CEC-L000109](../../tests/test_evidence_provenance.py#L109) | 109 | `""` | — |
| [SRC-6BCB799CEC-L000110](../../tests/test_evidence_provenance.py#L110) | 110 | `"    def generate(*args, **kwargs):"` | — |
| [SRC-6BCB799CEC-L000111](../../tests/test_evidence_provenance.py#L111) | 111 | `"        agent.server_search_sources.append({"` | — |
| [SRC-6BCB799CEC-L000112](../../tests/test_evidence_provenance.py#L112) | 112 | `"            \"title\": \"آخر المعلومات - نتيجة بحث مباشر\","` | — |
| [SRC-6BCB799CEC-L000113](../../tests/test_evidence_provenance.py#L113) | 113 | `"            \"url\": \"https://research.example.net/live-result\","` | — |
| [SRC-6BCB799CEC-L000114](../../tests/test_evidence_provenance.py#L114) | 114 | `"            \"snippet\": \"معلومات حديثة إضافية عن الموضوع\","` | — |
| [SRC-6BCB799CEC-L000115](../../tests/test_evidence_provenance.py#L115) | 115 | `"            \"page_text\": \"مقتطف أعاده مزود البحث\","` | — |
| [SRC-6BCB799CEC-L000116](../../tests/test_evidence_provenance.py#L116) | 116 | `"            \"page_fetched\": False,"` | — |
| [SRC-6BCB799CEC-L000117](../../tests/test_evidence_provenance.py#L117) | 117 | `"            \"provider\": \"openrouter_web_search\","` | — |
| [SRC-6BCB799CEC-L000118](../../tests/test_evidence_provenance.py#L118) | 118 | `"            \"providers\": [\"openrouter_web_search\"],"` | — |
| [SRC-6BCB799CEC-L000119](../../tests/test_evidence_provenance.py#L119) | 119 | `"            \"queries\": [question],"` | — |
| [SRC-6BCB799CEC-L000120](../../tests/test_evidence_provenance.py#L120) | 120 | `"            \"domain\": \"research.example.net\","` | — |
| [SRC-6BCB799CEC-L000121](../../tests/test_evidence_provenance.py#L121) | 121 | `"            \"source_class\": \"general\","` | — |
| [SRC-6BCB799CEC-L000122](../../tests/test_evidence_provenance.py#L122) | 122 | `"            \"platform\": \"web\","` | — |
| [SRC-6BCB799CEC-L000123](../../tests/test_evidence_provenance.py#L123) | 123 | `"            \"published_at\": \"\","` | — |
| [SRC-6BCB799CEC-L000124](../../tests/test_evidence_provenance.py#L124) | 124 | `"            \"rank_score\": 0.0,"` | — |
| [SRC-6BCB799CEC-L000125](../../tests/test_evidence_provenance.py#L125) | 125 | `"        })"` | — |
| [SRC-6BCB799CEC-L000126](../../tests/test_evidence_provenance.py#L126) | 126 | `"        return \"الخلاصة من المصدرين [المصدر 1] [المصدر 2].\""` | — |
| [SRC-6BCB799CEC-L000127](../../tests/test_evidence_provenance.py#L127) | 127 | `""` | — |
| [SRC-6BCB799CEC-L000128](../../tests/test_evidence_provenance.py#L128) | 128 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: {"` | — |
| [SRC-6BCB799CEC-L000129](../../tests/test_evidence_provenance.py#L129) | 129 | `"        \"queries\": [question],"` | — |
| [SRC-6BCB799CEC-L000130](../../tests/test_evidence_provenance.py#L130) | 130 | `"        \"direct_urls\": [],"` | — |
| [SRC-6BCB799CEC-L000131](../../tests/test_evidence_provenance.py#L131) | 131 | `"        \"social_focus\": False,"` | — |
| [SRC-6BCB799CEC-L000132](../../tests/test_evidence_provenance.py#L132) | 132 | `"        \"freshness\": \"any\","` | — |
| [SRC-6BCB799CEC-L000133](../../tests/test_evidence_provenance.py#L133) | 133 | `"        \"depth\": \"standard\","` | — |
| [SRC-6BCB799CEC-L000134](../../tests/test_evidence_provenance.py#L134) | 134 | `"        \"platforms\": [],"` | — |
| [SRC-6BCB799CEC-L000135](../../tests/test_evidence_provenance.py#L135) | 135 | `"        \"planning_method\": \"test\","` | — |
| [SRC-6BCB799CEC-L000136](../../tests/test_evidence_provenance.py#L136) | 136 | `"    })"` | — |
| [SRC-6BCB799CEC-L000137](../../tests/test_evidence_provenance.py#L137) | 137 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-6BCB799CEC-L000138](../../tests/test_evidence_provenance.py#L138) | 138 | `"    monkeypatch.setattr(agent, \"_generate\", generate)"` | — |
| [SRC-6BCB799CEC-L000139](../../tests/test_evidence_provenance.py#L139) | 139 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-6BCB799CEC-L000140](../../tests/test_evidence_provenance.py#L140) | 140 | `""` | — |
| [SRC-6BCB799CEC-L000141](../../tests/test_evidence_provenance.py#L141) | 141 | `"    result = agent.answer(question, history=[], mode=\"auto\")"` | — |
| [SRC-6BCB799CEC-L000142](../../tests/test_evidence_provenance.py#L142) | 142 | `"    cited = next(source for source in result[\"sources\"] if source[\"url\"] == \"https://research.example.net/live-result\")"` | — |
| [SRC-6BCB799CEC-L000143](../../tests/test_evidence_provenance.py#L143) | 143 | `"    assert cited[\"page_fetched\"] is False"` | — |
| [SRC-6BCB799CEC-L000144](../../tests/test_evidence_provenance.py#L144) | 144 | `"    assert \"openrouter_web_search\" in cited[\"providers\"]"` | — |
| [SRC-6BCB799CEC-L000145](../../tests/test_evidence_provenance.py#L145) | 145 | `"    assert result[\"search_report\"][\"pages_fetched\"] == 0"` | — |
| [SRC-6BCB799CEC-L000146](../../tests/test_evidence_provenance.py#L146) | 146 | `"    assert result[\"search_report\"][\"openrouter_web_search_results\"] == 1"` | — |
| [SRC-6BCB799CEC-L000147](../../tests/test_evidence_provenance.py#L147) | 147 | `""` | — |
| [SRC-6BCB799CEC-L000148](../../tests/test_evidence_provenance.py#L148) | 148 | `"def test_private_resolution_blocks_page_fetch(monkeypatch):"` | — |
| [SRC-6BCB799CEC-L000149](../../tests/test_evidence_provenance.py#L149) | 149 | `"    called = {\"stream\": 0}"` | — |
| [SRC-6BCB799CEC-L000150](../../tests/test_evidence_provenance.py#L150) | 150 | `""` | — |
| [SRC-6BCB799CEC-L000151](../../tests/test_evidence_provenance.py#L151) | 151 | `"    def fake_getaddrinfo(host, port, *args, **kwargs):"` | — |
| [SRC-6BCB799CEC-L000152](../../tests/test_evidence_provenance.py#L152) | 152 | `"        return _addrinfo(\"127.0.0.1\")"` | — |
| [SRC-6BCB799CEC-L000153](../../tests/test_evidence_provenance.py#L153) | 153 | `""` | — |
| [SRC-6BCB799CEC-L000154](../../tests/test_evidence_provenance.py#L154) | 154 | `"    class FakeClient:"` | — |
| [SRC-6BCB799CEC-L000155](../../tests/test_evidence_provenance.py#L155) | 155 | `"        def __init__(self, *args, **kwargs):"` | — |
| [SRC-6BCB799CEC-L000156](../../tests/test_evidence_provenance.py#L156) | 156 | `"            pass"` | — |
| [SRC-6BCB799CEC-L000157](../../tests/test_evidence_provenance.py#L157) | 157 | `""` | — |
| [SRC-6BCB799CEC-L000158](../../tests/test_evidence_provenance.py#L158) | 158 | `"        def __enter__(self):"` | — |
| [SRC-6BCB799CEC-L000159](../../tests/test_evidence_provenance.py#L159) | 159 | `"            return self"` | — |
| [SRC-6BCB799CEC-L000160](../../tests/test_evidence_provenance.py#L160) | 160 | `""` | — |
| [SRC-6BCB799CEC-L000161](../../tests/test_evidence_provenance.py#L161) | 161 | `"        def __exit__(self, *args):"` | — |
| [SRC-6BCB799CEC-L000162](../../tests/test_evidence_provenance.py#L162) | 162 | `"            return False"` | — |
| [SRC-6BCB799CEC-L000163](../../tests/test_evidence_provenance.py#L163) | 163 | `""` | — |
| [SRC-6BCB799CEC-L000164](../../tests/test_evidence_provenance.py#L164) | 164 | `"        def stream(self, *args, **kwargs):"` | — |
| [SRC-6BCB799CEC-L000165](../../tests/test_evidence_provenance.py#L165) | 165 | `"            called[\"stream\"] += 1"` | — |
| [SRC-6BCB799CEC-L000166](../../tests/test_evidence_provenance.py#L166) | 166 | `"            raise AssertionError(\"private destinations must not be connected\")"` | — |
| [SRC-6BCB799CEC-L000167](../../tests/test_evidence_provenance.py#L167) | 167 | `""` | — |
| [SRC-6BCB799CEC-L000168](../../tests/test_evidence_provenance.py#L168) | 168 | `"    monkeypatch.setattr(socket, \"getaddrinfo\", fake_getaddrinfo)"` | — |
| [SRC-6BCB799CEC-L000169](../../tests/test_evidence_provenance.py#L169) | 169 | `"    monkeypatch.setattr(\"httpx.Client\", FakeClient)"` | — |
| [SRC-6BCB799CEC-L000170](../../tests/test_evidence_provenance.py#L170) | 170 | `"    assert _public_ip_literals(\"example.com\") is None"` | — |
| [SRC-6BCB799CEC-L000171](../../tests/test_evidence_provenance.py#L171) | 171 | `"    assert WebAgent()._fetch_page(\"https://example.com/secret\") == (\"\", \"\")"` | — |
| [SRC-6BCB799CEC-L000172](../../tests/test_evidence_provenance.py#L172) | 172 | `"    assert called[\"stream\"] == 0"` | — |
| [SRC-6BCB799CEC-L000173](../../tests/test_evidence_provenance.py#L173) | 173 | `""` | — |
| [SRC-6BCB799CEC-L000174](../../tests/test_evidence_provenance.py#L174) | 174 | `""` | — |
| [SRC-6BCB799CEC-L000175](../../tests/test_evidence_provenance.py#L175) | 175 | `"def test_page_fetch_connects_to_the_validated_public_ip(monkeypatch):"` | — |
| [SRC-6BCB799CEC-L000176](../../tests/test_evidence_provenance.py#L176) | 176 | `"    seen = {}"` | — |
| [SRC-6BCB799CEC-L000177](../../tests/test_evidence_provenance.py#L177) | 177 | `""` | — |
| [SRC-6BCB799CEC-L000178](../../tests/test_evidence_provenance.py#L178) | 178 | `"    def fake_getaddrinfo(host, port, *args, **kwargs):"` | — |
| [SRC-6BCB799CEC-L000179](../../tests/test_evidence_provenance.py#L179) | 179 | `"        assert host == \"example.com\""` | — |
| [SRC-6BCB799CEC-L000180](../../tests/test_evidence_provenance.py#L180) | 180 | `"        return _addrinfo(\"1.1.1.1\")"` | — |
| [SRC-6BCB799CEC-L000181](../../tests/test_evidence_provenance.py#L181) | 181 | `""` | — |
| [SRC-6BCB799CEC-L000182](../../tests/test_evidence_provenance.py#L182) | 182 | `"    class FakeResponse:"` | — |
| [SRC-6BCB799CEC-L000183](../../tests/test_evidence_provenance.py#L183) | 183 | `"        status_code = 200"` | — |
| [SRC-6BCB799CEC-L000184](../../tests/test_evidence_provenance.py#L184) | 184 | `"        encoding = \"utf-8\""` | — |
| [SRC-6BCB799CEC-L000185](../../tests/test_evidence_provenance.py#L185) | 185 | `""` | — |
| [SRC-6BCB799CEC-L000186](../../tests/test_evidence_provenance.py#L186) | 186 | `"        def __init__(self):"` | — |
| [SRC-6BCB799CEC-L000187](../../tests/test_evidence_provenance.py#L187) | 187 | `"            self.headers = {\"content-type\": \"text/plain; charset=utf-8\"}"` | — |
| [SRC-6BCB799CEC-L000188](../../tests/test_evidence_provenance.py#L188) | 188 | `""` | — |
| [SRC-6BCB799CEC-L000189](../../tests/test_evidence_provenance.py#L189) | 189 | `"        def iter_bytes(self):"` | — |
| [SRC-6BCB799CEC-L000190](../../tests/test_evidence_provenance.py#L190) | 190 | `"            yield \"نص عام\".encode()"` | — |
| [SRC-6BCB799CEC-L000191](../../tests/test_evidence_provenance.py#L191) | 191 | `""` | — |
| [SRC-6BCB799CEC-L000192](../../tests/test_evidence_provenance.py#L192) | 192 | `"        def __enter__(self):"` | — |
| [SRC-6BCB799CEC-L000193](../../tests/test_evidence_provenance.py#L193) | 193 | `"            return self"` | — |
| [SRC-6BCB799CEC-L000194](../../tests/test_evidence_provenance.py#L194) | 194 | `""` | — |
| [SRC-6BCB799CEC-L000195](../../tests/test_evidence_provenance.py#L195) | 195 | `"        def __exit__(self, *args):"` | — |
| [SRC-6BCB799CEC-L000196](../../tests/test_evidence_provenance.py#L196) | 196 | `"            return False"` | — |
| [SRC-6BCB799CEC-L000197](../../tests/test_evidence_provenance.py#L197) | 197 | `""` | — |
| [SRC-6BCB799CEC-L000198](../../tests/test_evidence_provenance.py#L198) | 198 | `"    class FakeClient:"` | — |
| [SRC-6BCB799CEC-L000199](../../tests/test_evidence_provenance.py#L199) | 199 | `"        def __init__(self, *args, **kwargs):"` | — |
| [SRC-6BCB799CEC-L000200](../../tests/test_evidence_provenance.py#L200) | 200 | `"            assert kwargs.get(\"verify\") is True"` | — |
| [SRC-6BCB799CEC-L000201](../../tests/test_evidence_provenance.py#L201) | 201 | `"            assert kwargs.get(\"follow_redirects\") is False"` | — |
| [SRC-6BCB799CEC-L000202](../../tests/test_evidence_provenance.py#L202) | 202 | `"            # Do not allow HTTP_PROXY/HTTPS_PROXY to bypass the pinned IP."` | — |
| [SRC-6BCB799CEC-L000203](../../tests/test_evidence_provenance.py#L203) | 203 | `"            assert kwargs.get(\"trust_env\") is False"` | — |
| [SRC-6BCB799CEC-L000204](../../tests/test_evidence_provenance.py#L204) | 204 | `""` | — |
| [SRC-6BCB799CEC-L000205](../../tests/test_evidence_provenance.py#L205) | 205 | `"        def __enter__(self):"` | — |
| [SRC-6BCB799CEC-L000206](../../tests/test_evidence_provenance.py#L206) | 206 | `"            return self"` | — |
| [SRC-6BCB799CEC-L000207](../../tests/test_evidence_provenance.py#L207) | 207 | `""` | — |
| [SRC-6BCB799CEC-L000208](../../tests/test_evidence_provenance.py#L208) | 208 | `"        def __exit__(self, *args):"` | — |
| [SRC-6BCB799CEC-L000209](../../tests/test_evidence_provenance.py#L209) | 209 | `"            return False"` | — |
| [SRC-6BCB799CEC-L000210](../../tests/test_evidence_provenance.py#L210) | 210 | `""` | — |
| [SRC-6BCB799CEC-L000211](../../tests/test_evidence_provenance.py#L211) | 211 | `"        def stream(self, method, url, headers=None, extensions=None):"` | — |
| [SRC-6BCB799CEC-L000212](../../tests/test_evidence_provenance.py#L212) | 212 | `"            seen[\"method\"] = method"` | — |
| [SRC-6BCB799CEC-L000213](../../tests/test_evidence_provenance.py#L213) | 213 | `"            seen[\"url\"] = url"` | — |
| [SRC-6BCB799CEC-L000214](../../tests/test_evidence_provenance.py#L214) | 214 | `"            seen[\"headers\"] = headers"` | — |
| [SRC-6BCB799CEC-L000215](../../tests/test_evidence_provenance.py#L215) | 215 | `"            seen[\"extensions\"] = extensions"` | — |
| [SRC-6BCB799CEC-L000216](../../tests/test_evidence_provenance.py#L216) | 216 | `"            return FakeResponse()"` | — |
| [SRC-6BCB799CEC-L000217](../../tests/test_evidence_provenance.py#L217) | 217 | `""` | — |
| [SRC-6BCB799CEC-L000218](../../tests/test_evidence_provenance.py#L218) | 218 | `"    monkeypatch.setattr(socket, \"getaddrinfo\", fake_getaddrinfo)"` | — |
| [SRC-6BCB799CEC-L000219](../../tests/test_evidence_provenance.py#L219) | 219 | `"    monkeypatch.setattr(\"httpx.Client\", FakeClient)"` | — |
| [SRC-6BCB799CEC-L000220](../../tests/test_evidence_provenance.py#L220) | 220 | `"    title, text = WebAgent()._fetch_page(\"https://example.com/article\")"` | — |
| [SRC-6BCB799CEC-L000221](../../tests/test_evidence_provenance.py#L221) | 221 | `"    assert title == \"\""` | — |
| [SRC-6BCB799CEC-L000222](../../tests/test_evidence_provenance.py#L222) | 222 | `"    assert \"نص عام\" in text"` | — |
| [SRC-6BCB799CEC-L000223](../../tests/test_evidence_provenance.py#L223) | 223 | `"    assert seen[\"url\"].startswith(\"https://1.1.1.1/\")"` | — |
| [SRC-6BCB799CEC-L000224](../../tests/test_evidence_provenance.py#L224) | 224 | `"    assert seen[\"headers\"][\"Host\"] == \"example.com\""` | — |
| [SRC-6BCB799CEC-L000225](../../tests/test_evidence_provenance.py#L225) | 225 | `"    assert seen[\"extensions\"][\"sni_hostname\"] == \"example.com\""` | — |
| [SRC-6BCB799CEC-L000226](../../tests/test_evidence_provenance.py#L226) | 226 | `""` | — |
| [SRC-6BCB799CEC-L000227](../../tests/test_evidence_provenance.py#L227) | 227 | `"def test_mixed_public_and_private_dns_answers_block_page_fetch(monkeypatch):"` | — |
| [SRC-6BCB799CEC-L000228](../../tests/test_evidence_provenance.py#L228) | 228 | `"    \"\"\"A hostname is rejected when even one DNS answer is non-global.\"\"\""` | — |
| [SRC-6BCB799CEC-L000229](../../tests/test_evidence_provenance.py#L229) | 229 | `"    def fake_getaddrinfo(host, port, *args, **kwargs):"` | — |
| [SRC-6BCB799CEC-L000230](../../tests/test_evidence_provenance.py#L230) | 230 | `"        return _addrinfo(\"1.1.1.1\") + _addrinfo(\"127.0.0.1\")"` | — |
| [SRC-6BCB799CEC-L000231](../../tests/test_evidence_provenance.py#L231) | 231 | `""` | — |
| [SRC-6BCB799CEC-L000232](../../tests/test_evidence_provenance.py#L232) | 232 | `"    monkeypatch.setattr(socket, \"getaddrinfo\", fake_getaddrinfo)"` | — |
| [SRC-6BCB799CEC-L000233](../../tests/test_evidence_provenance.py#L233) | 233 | `"    assert _public_ip_literals(\"example.com\") is None"` | — |
| [SRC-6BCB799CEC-L000234](../../tests/test_evidence_provenance.py#L234) | 234 | `""` | — |
| [SRC-6BCB799CEC-L000235](../../tests/test_evidence_provenance.py#L235) | 235 | `""` | — |
| [SRC-6BCB799CEC-L000236](../../tests/test_evidence_provenance.py#L236) | 236 | `"def test_private_redirect_target_is_rejected_before_a_second_connection(monkeypatch):"` | — |
| [SRC-6BCB799CEC-L000237](../../tests/test_evidence_provenance.py#L237) | 237 | `"    \"\"\"Every redirect is validated independently, even after a pinned public request.\"\"\""` | — |
| [SRC-6BCB799CEC-L000238](../../tests/test_evidence_provenance.py#L238) | 238 | `"    resolutions = []"` | — |
| [SRC-6BCB799CEC-L000239](../../tests/test_evidence_provenance.py#L239) | 239 | `"    connections = []"` | — |
| [SRC-6BCB799CEC-L000240](../../tests/test_evidence_provenance.py#L240) | 240 | `""` | — |
| [SRC-6BCB799CEC-L000241](../../tests/test_evidence_provenance.py#L241) | 241 | `"    def fake_getaddrinfo(host, port, *args, **kwargs):"` | — |
| [SRC-6BCB799CEC-L000242](../../tests/test_evidence_provenance.py#L242) | 242 | `"        resolutions.append(host)"` | — |
| [SRC-6BCB799CEC-L000243](../../tests/test_evidence_provenance.py#L243) | 243 | `"        assert host == \"example.com\""` | — |
| [SRC-6BCB799CEC-L000244](../../tests/test_evidence_provenance.py#L244) | 244 | `"        return _addrinfo(\"1.1.1.1\")"` | — |
| [SRC-6BCB799CEC-L000245](../../tests/test_evidence_provenance.py#L245) | 245 | `""` | — |
| [SRC-6BCB799CEC-L000246](../../tests/test_evidence_provenance.py#L246) | 246 | `"    class FakeResponse:"` | — |
| [SRC-6BCB799CEC-L000247](../../tests/test_evidence_provenance.py#L247) | 247 | `"        status_code = 302"` | — |
| [SRC-6BCB799CEC-L000248](../../tests/test_evidence_provenance.py#L248) | 248 | `""` | — |
| [SRC-6BCB799CEC-L000249](../../tests/test_evidence_provenance.py#L249) | 249 | `"        def __init__(self):"` | — |
| [SRC-6BCB799CEC-L000250](../../tests/test_evidence_provenance.py#L250) | 250 | `"            self.headers = {\"location\": \"http://127.0.0.1/latest/meta-data/\"}"` | — |
| [SRC-6BCB799CEC-L000251](../../tests/test_evidence_provenance.py#L251) | 251 | `""` | — |
| [SRC-6BCB799CEC-L000252](../../tests/test_evidence_provenance.py#L252) | 252 | `"        def __enter__(self):"` | — |
| [SRC-6BCB799CEC-L000253](../../tests/test_evidence_provenance.py#L253) | 253 | `"            return self"` | — |
| [SRC-6BCB799CEC-L000254](../../tests/test_evidence_provenance.py#L254) | 254 | `""` | — |
| [SRC-6BCB799CEC-L000255](../../tests/test_evidence_provenance.py#L255) | 255 | `"        def __exit__(self, *args):"` | — |
| [SRC-6BCB799CEC-L000256](../../tests/test_evidence_provenance.py#L256) | 256 | `"            return False"` | — |
| [SRC-6BCB799CEC-L000257](../../tests/test_evidence_provenance.py#L257) | 257 | `""` | — |
| [SRC-6BCB799CEC-L000258](../../tests/test_evidence_provenance.py#L258) | 258 | `"    class FakeClient:"` | — |
| [SRC-6BCB799CEC-L000259](../../tests/test_evidence_provenance.py#L259) | 259 | `"        def __init__(self, *args, **kwargs):"` | — |
| [SRC-6BCB799CEC-L000260](../../tests/test_evidence_provenance.py#L260) | 260 | `"            assert kwargs.get(\"trust_env\") is False"` | — |
| [SRC-6BCB799CEC-L000261](../../tests/test_evidence_provenance.py#L261) | 261 | `"            assert kwargs.get(\"follow_redirects\") is False"` | — |
| [SRC-6BCB799CEC-L000262](../../tests/test_evidence_provenance.py#L262) | 262 | `""` | — |
| [SRC-6BCB799CEC-L000263](../../tests/test_evidence_provenance.py#L263) | 263 | `"        def __enter__(self):"` | — |
| [SRC-6BCB799CEC-L000264](../../tests/test_evidence_provenance.py#L264) | 264 | `"            return self"` | — |
| [SRC-6BCB799CEC-L000265](../../tests/test_evidence_provenance.py#L265) | 265 | `""` | — |
| [SRC-6BCB799CEC-L000266](../../tests/test_evidence_provenance.py#L266) | 266 | `"        def __exit__(self, *args):"` | — |
| [SRC-6BCB799CEC-L000267](../../tests/test_evidence_provenance.py#L267) | 267 | `"            return False"` | — |
| [SRC-6BCB799CEC-L000268](../../tests/test_evidence_provenance.py#L268) | 268 | `""` | — |
| [SRC-6BCB799CEC-L000269](../../tests/test_evidence_provenance.py#L269) | 269 | `"        def stream(self, method, url, **kwargs):"` | — |
| [SRC-6BCB799CEC-L000270](../../tests/test_evidence_provenance.py#L270) | 270 | `"            connections.append(url)"` | — |
| [SRC-6BCB799CEC-L000271](../../tests/test_evidence_provenance.py#L271) | 271 | `"            return FakeResponse()"` | — |
| [SRC-6BCB799CEC-L000272](../../tests/test_evidence_provenance.py#L272) | 272 | `""` | — |
| [SRC-6BCB799CEC-L000273](../../tests/test_evidence_provenance.py#L273) | 273 | `"    monkeypatch.setattr(socket, \"getaddrinfo\", fake_getaddrinfo)"` | — |
| [SRC-6BCB799CEC-L000274](../../tests/test_evidence_provenance.py#L274) | 274 | `"    monkeypatch.setattr(\"httpx.Client\", FakeClient)"` | — |
| [SRC-6BCB799CEC-L000275](../../tests/test_evidence_provenance.py#L275) | 275 | `"    assert WebAgent()._fetch_page(\"https://example.com/article\") == (\"\", \"\")"` | — |
| [SRC-6BCB799CEC-L000276](../../tests/test_evidence_provenance.py#L276) | 276 | `"    assert len(connections) == 1"` | — |
| [SRC-6BCB799CEC-L000277](../../tests/test_evidence_provenance.py#L277) | 277 | `"    assert connections[0].startswith(\"https://1.1.1.1/\")"` | — |
| [SRC-6BCB799CEC-L000278](../../tests/test_evidence_provenance.py#L278) | 278 | `"    assert resolutions == [\"example.com\"]"` | — |
| [SRC-6BCB799CEC-L000279](../../tests/test_evidence_provenance.py#L279) | 279 | `""` | — |
| [SRC-6BCB799CEC-L000280](../../tests/test_evidence_provenance.py#L280) | 280 | `""` | — |
| [SRC-6BCB799CEC-L000281](../../tests/test_evidence_provenance.py#L281) | 281 | `""` | — |
| [SRC-6BCB799CEC-L000282](../../tests/test_evidence_provenance.py#L282) | 282 | `"@pytest.mark.parametrize("` | — |
