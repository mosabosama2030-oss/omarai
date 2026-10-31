# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **038**
- سجلات الأسطر: **800**
- النطاق: SRC-3451CC474D-L000922 إلى SRC-6BECF5AD00-L000048
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-3451CC474D — [tests/test_api.py](../../tests/test_api.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-3451CC474D-L000922](../../tests/test_api.py#L922) | 922 | `"            \"warnings\": [],"` | — |
| [SRC-3451CC474D-L000923](../../tests/test_api.py#L923) | 923 | `"            \"kind\": \"web_fallback\","` | — |
| [SRC-3451CC474D-L000924](../../tests/test_api.py#L924) | 924 | `"        }"` | — |
| [SRC-3451CC474D-L000925](../../tests/test_api.py#L925) | 925 | `""` | — |
| [SRC-3451CC474D-L000926](../../tests/test_api.py#L926) | 926 | `"    monkeypatch.setattr(WebAgent, \"answer\", answer_with_one_transient_failure)"` | — |
| [SRC-3451CC474D-L000927](../../tests/test_api.py#L927) | 927 | `""` | — |
| [SRC-3451CC474D-L000928](../../tests/test_api.py#L928) | 928 | `"    status, payload = request_json("` | — |
| [SRC-3451CC474D-L000929](../../tests/test_api.py#L929) | 929 | `"        local_api, \"/api/agent\", method=\"POST\", payload={\"question\": \"الطلب الأول\"}"` | — |
| [SRC-3451CC474D-L000930](../../tests/test_api.py#L930) | 930 | `"    )"` | — |
| [SRC-3451CC474D-L000931](../../tests/test_api.py#L931) | 931 | `"    assert status == 500"` | — |
| [SRC-3451CC474D-L000932](../../tests/test_api.py#L932) | 932 | `"    assert payload[\"error\"] == \"internal server error\""` | — |
| [SRC-3451CC474D-L000933](../../tests/test_api.py#L933) | 933 | `""` | — |
| [SRC-3451CC474D-L000934](../../tests/test_api.py#L934) | 934 | `"    state[\"fail\"] = False"` | — |
| [SRC-3451CC474D-L000935](../../tests/test_api.py#L935) | 935 | `"    status, payload = request_json("` | — |
| [SRC-3451CC474D-L000936](../../tests/test_api.py#L936) | 936 | `"        local_api, \"/api/agent\", method=\"POST\", payload={\"question\": \"الطلب الثاني\"}"` | — |
| [SRC-3451CC474D-L000937](../../tests/test_api.py#L937) | 937 | `"    )"` | — |
| [SRC-3451CC474D-L000938](../../tests/test_api.py#L938) | 938 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000939](../../tests/test_api.py#L939) | 939 | `"    assert payload[\"answer\"] == \"اختبار ناجح\""` | — |
| [SRC-3451CC474D-L000940](../../tests/test_api.py#L940) | 940 | `""` | — |
| [SRC-3451CC474D-L000941](../../tests/test_api.py#L941) | 941 | `""` | — |
| [SRC-3451CC474D-L000942](../../tests/test_api.py#L942) | 942 | `"def test_csp_hashes_match_all_first_party_inline_content_and_attributes():"` | — |
| [SRC-3451CC474D-L000943](../../tests/test_api.py#L943) | 943 | `"    import api.omarai as api_module"` | — |
| [SRC-3451CC474D-L000944](../../tests/test_api.py#L944) | 944 | `""` | — |
| [SRC-3451CC474D-L000945](../../tests/test_api.py#L945) | 945 | `"    policy = api_module._content_security_policy()"` | — |
| [SRC-3451CC474D-L000946](../../tests/test_api.py#L946) | 946 | `"    assert \"'unsafe-inline'\" not in policy"` | — |
| [SRC-3451CC474D-L000947](../../tests/test_api.py#L947) | 947 | `"    script_blocks = 0"` | — |
| [SRC-3451CC474D-L000948](../../tests/test_api.py#L948) | 948 | `"    style_blocks = 0"` | — |
| [SRC-3451CC474D-L000949](../../tests/test_api.py#L949) | 949 | `"    style_attributes = 0"` | — |
| [SRC-3451CC474D-L000950](../../tests/test_api.py#L950) | 950 | `"    for html_path in api_module.ROOT.glob(\"*.html\"):"` | — |
| [SRC-3451CC474D-L000951](../../tests/test_api.py#L951) | 951 | `"        document = html_path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3451CC474D-L000952](../../tests/test_api.py#L952) | 952 | `"        for match in re.finditer("` | — |
| [SRC-3451CC474D-L000953](../../tests/test_api.py#L953) | 953 | `"            r\"<script\\b(?P<attrs>[^>]*)>(?P<body>.*?)</script\\s*>\","` | — |
| [SRC-3451CC474D-L000954](../../tests/test_api.py#L954) | 954 | `"            document,"` | — |
| [SRC-3451CC474D-L000955](../../tests/test_api.py#L955) | 955 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-3451CC474D-L000956](../../tests/test_api.py#L956) | 956 | `"        ):"` | — |
| [SRC-3451CC474D-L000957](../../tests/test_api.py#L957) | 957 | `"            if re.search(r\"\\bsrc\\s*=\", match.group(\"attrs\"), re.IGNORECASE):"` | — |
| [SRC-3451CC474D-L000958](../../tests/test_api.py#L958) | 958 | `"                continue"` | — |
| [SRC-3451CC474D-L000959](../../tests/test_api.py#L959) | 959 | `"            script_blocks += 1"` | — |
| [SRC-3451CC474D-L000960](../../tests/test_api.py#L960) | 960 | `"            assert api_module._csp_hash_source(match.group(\"body\")) in policy"` | — |
| [SRC-3451CC474D-L000961](../../tests/test_api.py#L961) | 961 | `"        for match in re.finditer("` | — |
| [SRC-3451CC474D-L000962](../../tests/test_api.py#L962) | 962 | `"            r\"<style\\b[^>]*>(?P<body>.*?)</style\\s*>\","` | — |
| [SRC-3451CC474D-L000963](../../tests/test_api.py#L963) | 963 | `"            document,"` | — |
| [SRC-3451CC474D-L000964](../../tests/test_api.py#L964) | 964 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-3451CC474D-L000965](../../tests/test_api.py#L965) | 965 | `"        ):"` | — |
| [SRC-3451CC474D-L000966](../../tests/test_api.py#L966) | 966 | `"            style_blocks += 1"` | — |
| [SRC-3451CC474D-L000967](../../tests/test_api.py#L967) | 967 | `"            assert api_module._csp_hash_source(match.group(\"body\")) in policy"` | — |
| [SRC-3451CC474D-L000968](../../tests/test_api.py#L968) | 968 | `"        for match in re.finditer("` | — |
| [SRC-3451CC474D-L000969](../../tests/test_api.py#L969) | 969 | `"            r\"\"\"\\bstyle\\s*=\\s*([\"'])(.*?)\\1\"\"\","` | — |
| [SRC-3451CC474D-L000970](../../tests/test_api.py#L970) | 970 | `"            document,"` | — |
| [SRC-3451CC474D-L000971](../../tests/test_api.py#L971) | 971 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-3451CC474D-L000972](../../tests/test_api.py#L972) | 972 | `"        ):"` | — |
| [SRC-3451CC474D-L000973](../../tests/test_api.py#L973) | 973 | `"            style_attributes += 1"` | — |
| [SRC-3451CC474D-L000974](../../tests/test_api.py#L974) | 974 | `"            assert api_module._csp_hash_source(match.group(2).strip()) in policy"` | — |
| [SRC-3451CC474D-L000975](../../tests/test_api.py#L975) | 975 | `"    assert script_blocks >= 2"` | — |
| [SRC-3451CC474D-L000976](../../tests/test_api.py#L976) | 976 | `"    assert style_blocks >= 2"` | — |
| [SRC-3451CC474D-L000977](../../tests/test_api.py#L977) | 977 | `"    assert style_attributes >= 10"` | — |
| [SRC-3451CC474D-L000978](../../tests/test_api.py#L978) | 978 | `""` | — |
| [SRC-3451CC474D-L000979](../../tests/test_api.py#L979) | 979 | `""` | — |
| [SRC-3451CC474D-L000980](../../tests/test_api.py#L980) | 980 | `"def test_dashboard_uses_delegated_status_action_not_inline_onclick():"` | — |
| [SRC-3451CC474D-L000981](../../tests/test_api.py#L981) | 981 | `"    dashboard = (Path(__file__).resolve().parents[1] / \"web\" / \"dashboard.html\").read_text("` | — |
| [SRC-3451CC474D-L000982](../../tests/test_api.py#L982) | 982 | `"        encoding=\"utf-8\""` | — |
| [SRC-3451CC474D-L000983](../../tests/test_api.py#L983) | 983 | `"    )"` | — |
| [SRC-3451CC474D-L000984](../../tests/test_api.py#L984) | 984 | `"    assert 'data-action=\"save-status\"' in dashboard"` | — |
| [SRC-3451CC474D-L000985](../../tests/test_api.py#L985) | 985 | `"    assert 'onclick=\"saveStatus' not in dashboard"` | — |
| [SRC-3451CC474D-L000986](../../tests/test_api.py#L986) | 986 | `"    assert \"\"\"data-lead-id=\"'+esc(l.id)+'\">\"\"\" in dashboard"` | — |
| [SRC-3451CC474D-L000987](../../tests/test_api.py#L987) | 987 | `""` | — |
| [SRC-3451CC474D-L000988](../../tests/test_api.py#L988) | 988 | `"def test_loopback_test_mode_allows_tokenless_local_api_but_not_remote_or_public_clients("` | — |
| [SRC-3451CC474D-L000989](../../tests/test_api.py#L989) | 989 | `"    local_api, monkeypatch"` | — |
| [SRC-3451CC474D-L000990](../../tests/test_api.py#L990) | 990 | `"):"` | — |
| [SRC-3451CC474D-L000991](../../tests/test_api.py#L991) | 991 | `"    status, leads = request_json(local_api, \"/api/leads\")"` | — |
| [SRC-3451CC474D-L000992](../../tests/test_api.py#L992) | 992 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000993](../../tests/test_api.py#L993) | 993 | `"    assert leads[\"count\"] == 0"` | — |
| [SRC-3451CC474D-L000994](../../tests/test_api.py#L994) | 994 | `""` | — |
| [SRC-3451CC474D-L000995](../../tests/test_api.py#L995) | 995 | `"    monkeypatch.delenv(\"OMARAI_TEST_MODE\", raising=False)"` | — |
| [SRC-3451CC474D-L000996](../../tests/test_api.py#L996) | 996 | `"    status, _error = request_json(local_api, \"/api/leads\")"` | — |
| [SRC-3451CC474D-L000997](../../tests/test_api.py#L997) | 997 | `"    assert status == 401"` | — |
| [SRC-3451CC474D-L000998](../../tests/test_api.py#L998) | 998 | `""` | — |
| [SRC-3451CC474D-L000999](../../tests/test_api.py#L999) | 999 | `"    from types import SimpleNamespace"` | — |
| [SRC-3451CC474D-L001000](../../tests/test_api.py#L1000) | 1000 | `""` | — |
| [SRC-3451CC474D-L001001](../../tests/test_api.py#L1001) | 1001 | `"    harness = SimpleNamespace("` | — |
| [SRC-3451CC474D-L001002](../../tests/test_api.py#L1002) | 1002 | `"        client_address=(\"203.0.113.10\", 50000),"` | — |
| [SRC-3451CC474D-L001003](../../tests/test_api.py#L1003) | 1003 | `"        server=SimpleNamespace(server_address=(\"127.0.0.1\", 8765)),"` | — |
| [SRC-3451CC474D-L001004](../../tests/test_api.py#L1004) | 1004 | `"        _is_loopback_address=Handler._is_loopback_address,"` | — |
| [SRC-3451CC474D-L001005](../../tests/test_api.py#L1005) | 1005 | `"    )"` | — |
| [SRC-3451CC474D-L001006](../../tests/test_api.py#L1006) | 1006 | `"    monkeypatch.setenv(\"OMARAI_TEST_MODE\", \"1\")"` | — |
| [SRC-3451CC474D-L001007](../../tests/test_api.py#L1007) | 1007 | `"    assert Handler._is_loopback_test_request(harness) is False"` | — |
| [SRC-3451CC474D-L001008](../../tests/test_api.py#L1008) | 1008 | `"    harness.client_address = (\"127.0.0.1\", 50000)"` | — |
| [SRC-3451CC474D-L001009](../../tests/test_api.py#L1009) | 1009 | `"    assert Handler._is_loopback_test_request(harness) is True"` | — |
| [SRC-3451CC474D-L001010](../../tests/test_api.py#L1010) | 1010 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L001011](../../tests/test_api.py#L1011) | 1011 | `"    assert Handler._is_loopback_test_request(harness) is False"` | — |
| [SRC-3451CC474D-L001012](../../tests/test_api.py#L1012) | 1012 | `""` | — |
| [SRC-3451CC474D-L001013](../../tests/test_api.py#L1013) | 1013 | `""` | — |
| [SRC-3451CC474D-L001014](../../tests/test_api.py#L1014) | 1014 | `"def test_api_rejects_cross_company_list_write_update_and_export(local_api):"` | — |
| [SRC-3451CC474D-L001015](../../tests/test_api.py#L1015) | 1015 | `"    store = Handler.store"` | — |
| [SRC-3451CC474D-L001016](../../tests/test_api.py#L1016) | 1016 | `"    store.create_company(\"company-b\", \"شركة ب\")"` | — |
| [SRC-3451CC474D-L001017](../../tests/test_api.py#L1017) | 1017 | `"    store.create_user(\"user-b\", display_name=\"مسؤول ب\")"` | — |
| [SRC-3451CC474D-L001018](../../tests/test_api.py#L1018) | 1018 | `"    store.add_membership(\"company-b\", \"user-b\", role=\"admin\")"` | — |
| [SRC-3451CC474D-L001019](../../tests/test_api.py#L1019) | 1019 | `"    lead_b, created = store.add("` | — |
| [SRC-3451CC474D-L001020](../../tests/test_api.py#L1020) | 1020 | `"        \"مطلوب شراء منتج\","` | — |
| [SRC-3451CC474D-L001021](../../tests/test_api.py#L1021) | 1021 | `"        \"https://example.com/company-b/request\","` | — |
| [SRC-3451CC474D-L001022](../../tests/test_api.py#L1022) | 1022 | `"        tenant_id=\"company-b\","` | — |
| [SRC-3451CC474D-L001023](../../tests/test_api.py#L1023) | 1023 | `"    )"` | — |
| [SRC-3451CC474D-L001024](../../tests/test_api.py#L1024) | 1024 | `"    assert created is True"` | — |
| [SRC-3451CC474D-L001025](../../tests/test_api.py#L1025) | 1025 | `""` | — |
| [SRC-3451CC474D-L001026](../../tests/test_api.py#L1026) | 1026 | `"    # The default operator has no membership in company B, even if it forges tenant_id."` | — |
| [SRC-3451CC474D-L001027](../../tests/test_api.py#L1027) | 1027 | `"    status, _ = request_json(local_api, \"/api/leads?tenant_id=company-b\")"` | — |
| [SRC-3451CC474D-L001028](../../tests/test_api.py#L1028) | 1028 | `"    assert status == 403"` | — |
| [SRC-3451CC474D-L001029](../../tests/test_api.py#L1029) | 1029 | `"    status, _ = request_json("` | — |
| [SRC-3451CC474D-L001030](../../tests/test_api.py#L1030) | 1030 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001031](../../tests/test_api.py#L1031) | 1031 | `"        \"/api/leads\","` | — |
| [SRC-3451CC474D-L001032](../../tests/test_api.py#L1032) | 1032 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001033](../../tests/test_api.py#L1033) | 1033 | `"        payload={"` | — |
| [SRC-3451CC474D-L001034](../../tests/test_api.py#L1034) | 1034 | `"            \"tenant_id\": \"company-b\","` | — |
| [SRC-3451CC474D-L001035](../../tests/test_api.py#L1035) | 1035 | `"            \"text\": \"مطلوب شراء منتج آخر\","` | — |
| [SRC-3451CC474D-L001036](../../tests/test_api.py#L1036) | 1036 | `"            \"source_url\": \"https://example.com/company-b/forged\","` | — |
| [SRC-3451CC474D-L001037](../../tests/test_api.py#L1037) | 1037 | `"        },"` | — |
| [SRC-3451CC474D-L001038](../../tests/test_api.py#L1038) | 1038 | `"    )"` | — |
| [SRC-3451CC474D-L001039](../../tests/test_api.py#L1039) | 1039 | `"    assert status == 403"` | — |
| [SRC-3451CC474D-L001040](../../tests/test_api.py#L1040) | 1040 | `"    status, _ = request_json("` | — |
| [SRC-3451CC474D-L001041](../../tests/test_api.py#L1041) | 1041 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001042](../../tests/test_api.py#L1042) | 1042 | `"        f\"/api/leads/{lead_b['id']}/status\","` | — |
| [SRC-3451CC474D-L001043](../../tests/test_api.py#L1043) | 1043 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001044](../../tests/test_api.py#L1044) | 1044 | `"        payload={\"tenant_id\": \"company-b\", \"status\": \"qualified\"},"` | — |
| [SRC-3451CC474D-L001045](../../tests/test_api.py#L1045) | 1045 | `"    )"` | — |
| [SRC-3451CC474D-L001046](../../tests/test_api.py#L1046) | 1046 | `"    assert status == 403"` | — |
| [SRC-3451CC474D-L001047](../../tests/test_api.py#L1047) | 1047 | `"    status, _ = request_text(local_api, \"/api/leads/export.csv?tenant_id=company-b\")"` | — |
| [SRC-3451CC474D-L001048](../../tests/test_api.py#L1048) | 1048 | `"    assert status == 403"` | — |
| [SRC-3451CC474D-L001049](../../tests/test_api.py#L1049) | 1049 | `""` | — |
| [SRC-3451CC474D-L001050](../../tests/test_api.py#L1050) | 1050 | `"    headers_b = {\"X-Omarai-Test-User\": \"user-b\"}"` | — |
| [SRC-3451CC474D-L001051](../../tests/test_api.py#L1051) | 1051 | `"    status, leads_b = request_json("` | — |
| [SRC-3451CC474D-L001052](../../tests/test_api.py#L1052) | 1052 | `"        local_api, \"/api/leads?tenant_id=company-b\", headers=headers_b"` | — |
| [SRC-3451CC474D-L001053](../../tests/test_api.py#L1053) | 1053 | `"    )"` | — |
| [SRC-3451CC474D-L001054](../../tests/test_api.py#L1054) | 1054 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L001055](../../tests/test_api.py#L1055) | 1055 | `"    assert [item[\"id\"] for item in leads_b[\"leads\"]] == [lead_b[\"id\"]]"` | — |
| [SRC-3451CC474D-L001056](../../tests/test_api.py#L1056) | 1056 | `""` | — |
| [SRC-3451CC474D-L001057](../../tests/test_api.py#L1057) | 1057 | `"    # Membership in company B does not grant access to the default company."` | — |
| [SRC-3451CC474D-L001058](../../tests/test_api.py#L1058) | 1058 | `"    status, _ = request_json("` | — |
| [SRC-3451CC474D-L001059](../../tests/test_api.py#L1059) | 1059 | `"        local_api, \"/api/leads?tenant_id=default\", headers=headers_b"` | — |
| [SRC-3451CC474D-L001060](../../tests/test_api.py#L1060) | 1060 | `"    )"` | — |
| [SRC-3451CC474D-L001061](../../tests/test_api.py#L1061) | 1061 | `"    assert status == 403"` | — |
| [SRC-3451CC474D-L001062](../../tests/test_api.py#L1062) | 1062 | `""` | — |
| [SRC-3451CC474D-L001063](../../tests/test_api.py#L1063) | 1063 | `"    status, exported_b = request_text("` | — |
| [SRC-3451CC474D-L001064](../../tests/test_api.py#L1064) | 1064 | `"        local_api, \"/api/leads/export.csv?tenant_id=company-b\", headers=headers_b"` | — |
| [SRC-3451CC474D-L001065](../../tests/test_api.py#L1065) | 1065 | `"    )"` | — |
| [SRC-3451CC474D-L001066](../../tests/test_api.py#L1066) | 1066 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L001067](../../tests/test_api.py#L1067) | 1067 | `"    assert lead_b[\"id\"] in exported_b"` | — |
| [SRC-3451CC474D-L001068](../../tests/test_api.py#L1068) | 1068 | `"    assert \"company-b\" in exported_b"` | — |
| [SRC-3451CC474D-L001069](../../tests/test_api.py#L1069) | 1069 | `""` | — |
| [SRC-3451CC474D-L001070](../../tests/test_api.py#L1070) | 1070 | `"    status, updated = request_json("` | — |
| [SRC-3451CC474D-L001071](../../tests/test_api.py#L1071) | 1071 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001072](../../tests/test_api.py#L1072) | 1072 | `"        f\"/api/leads/{lead_b['id']}/status\","` | — |
| [SRC-3451CC474D-L001073](../../tests/test_api.py#L1073) | 1073 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001074](../../tests/test_api.py#L1074) | 1074 | `"        payload={\"tenant_id\": \"company-b\", \"status\": \"qualified\"},"` | — |
| [SRC-3451CC474D-L001075](../../tests/test_api.py#L1075) | 1075 | `"        headers=headers_b,"` | — |
| [SRC-3451CC474D-L001076](../../tests/test_api.py#L1076) | 1076 | `"    )"` | — |
| [SRC-3451CC474D-L001077](../../tests/test_api.py#L1077) | 1077 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L001078](../../tests/test_api.py#L1078) | 1078 | `"    assert updated[\"lead\"][\"tenant_id\"] == \"company-b\""` | — |
| [SRC-3451CC474D-L001079](../../tests/test_api.py#L1079) | 1079 | `"    assert updated[\"lead\"][\"status\"] == \"qualified\""` | — |
| [SRC-3451CC474D-L001080](../../tests/test_api.py#L1080) | 1080 | `""` | — |
| [SRC-3451CC474D-L001081](../../tests/test_api.py#L1081) | 1081 | `"    # A default-company identity cannot mutate a foreign row even by guessing its ID."` | — |
| [SRC-3451CC474D-L001082](../../tests/test_api.py#L1082) | 1082 | `"    status, _ = request_json("` | — |
| [SRC-3451CC474D-L001083](../../tests/test_api.py#L1083) | 1083 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001084](../../tests/test_api.py#L1084) | 1084 | `"        f\"/api/leads/{lead_b['id']}/status\","` | — |
| [SRC-3451CC474D-L001085](../../tests/test_api.py#L1085) | 1085 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001086](../../tests/test_api.py#L1086) | 1086 | `"        payload={\"status\": \"rejected\"},"` | — |
| [SRC-3451CC474D-L001087](../../tests/test_api.py#L1087) | 1087 | `"    )"` | — |
| [SRC-3451CC474D-L001088](../../tests/test_api.py#L1088) | 1088 | `"    assert status == 404"` | — |
| [SRC-3451CC474D-L001089](../../tests/test_api.py#L1089) | 1089 | `""` | — |
| [SRC-3451CC474D-L001090](../../tests/test_api.py#L1090) | 1090 | `""` | — |
| [SRC-3451CC474D-L001091](../../tests/test_api.py#L1091) | 1091 | `"def test_api_tenant_id_header_requires_verified_membership(local_api):"` | — |
| [SRC-3451CC474D-L001092](../../tests/test_api.py#L1092) | 1092 | `"    store = Handler.store"` | — |
| [SRC-3451CC474D-L001093](../../tests/test_api.py#L1093) | 1093 | `"    store.create_company(\"company-c\", \"شركة ج\")"` | — |
| [SRC-3451CC474D-L001094](../../tests/test_api.py#L1094) | 1094 | `"    store.create_user(\"user-c\")"` | — |
| [SRC-3451CC474D-L001095](../../tests/test_api.py#L1095) | 1095 | `"    store.add_membership(\"company-c\", \"user-c\", role=\"viewer\")"` | — |
| [SRC-3451CC474D-L001096](../../tests/test_api.py#L1096) | 1096 | `""` | — |
| [SRC-3451CC474D-L001097](../../tests/test_api.py#L1097) | 1097 | `"    status, _ = request_json("` | — |
| [SRC-3451CC474D-L001098](../../tests/test_api.py#L1098) | 1098 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001099](../../tests/test_api.py#L1099) | 1099 | `"        \"/api/analyze\","` | — |
| [SRC-3451CC474D-L001100](../../tests/test_api.py#L1100) | 1100 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001101](../../tests/test_api.py#L1101) | 1101 | `"        payload={\"text\": \"اختبار\", \"tenant_id\": \"company-c\"},"` | — |
| [SRC-3451CC474D-L001102](../../tests/test_api.py#L1102) | 1102 | `"    )"` | — |
| [SRC-3451CC474D-L001103](../../tests/test_api.py#L1103) | 1103 | `"    assert status == 403"` | — |
| [SRC-3451CC474D-L001104](../../tests/test_api.py#L1104) | 1104 | `""` | — |
| [SRC-3451CC474D-L001105](../../tests/test_api.py#L1105) | 1105 | `"    status, _ = request_json("` | — |
| [SRC-3451CC474D-L001106](../../tests/test_api.py#L1106) | 1106 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001107](../../tests/test_api.py#L1107) | 1107 | `"        \"/api/analyze\","` | — |
| [SRC-3451CC474D-L001108](../../tests/test_api.py#L1108) | 1108 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001109](../../tests/test_api.py#L1109) | 1109 | `"        payload={\"text\": \"اختبار\"},"` | — |
| [SRC-3451CC474D-L001110](../../tests/test_api.py#L1110) | 1110 | `"        headers={\"X-Omarai-Tenant-ID\": \"company-c\"},"` | — |
| [SRC-3451CC474D-L001111](../../tests/test_api.py#L1111) | 1111 | `"    )"` | — |
| [SRC-3451CC474D-L001112](../../tests/test_api.py#L1112) | 1112 | `"    assert status == 403"` | — |
| [SRC-3451CC474D-L001113](../../tests/test_api.py#L1113) | 1113 | `""` | — |
| [SRC-3451CC474D-L001114](../../tests/test_api.py#L1114) | 1114 | `"    status, result = request_json("` | — |
| [SRC-3451CC474D-L001115](../../tests/test_api.py#L1115) | 1115 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001116](../../tests/test_api.py#L1116) | 1116 | `"        \"/api/analyze\","` | — |
| [SRC-3451CC474D-L001117](../../tests/test_api.py#L1117) | 1117 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001118](../../tests/test_api.py#L1118) | 1118 | `"        payload={\"text\": \"اختبار\", \"tenant_id\": \"company-c\"},"` | — |
| [SRC-3451CC474D-L001119](../../tests/test_api.py#L1119) | 1119 | `"        headers={\"X-Omarai-Test-User\": \"user-c\"},"` | — |
| [SRC-3451CC474D-L001120](../../tests/test_api.py#L1120) | 1120 | `"    )"` | — |
| [SRC-3451CC474D-L001121](../../tests/test_api.py#L1121) | 1121 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L001122](../../tests/test_api.py#L1122) | 1122 | `"    assert \"score\" in result"` | — |
| [SRC-3451CC474D-L001123](../../tests/test_api.py#L1123) | 1123 | `""` | — |
| [SRC-3451CC474D-L001124](../../tests/test_api.py#L1124) | 1124 | `"def test_api_ask_statistics_and_recommendations_are_company_scoped(local_api):"` | — |
| [SRC-3451CC474D-L001125](../../tests/test_api.py#L1125) | 1125 | `"    store = Handler.store"` | — |
| [SRC-3451CC474D-L001126](../../tests/test_api.py#L1126) | 1126 | `"    store.create_company(\"company-b\", \"شركة ب\")"` | — |
| [SRC-3451CC474D-L001127](../../tests/test_api.py#L1127) | 1127 | `"    store.create_user(\"user-b\", display_name=\"مسؤول ب\")"` | — |
| [SRC-3451CC474D-L001128](../../tests/test_api.py#L1128) | 1128 | `"    store.add_membership(\"company-b\", \"user-b\", role=\"admin\")"` | — |
| [SRC-3451CC474D-L001129](../../tests/test_api.py#L1129) | 1129 | `"    lead_b, created = store.add("` | — |
| [SRC-3451CC474D-L001130](../../tests/test_api.py#L1130) | 1130 | `"        \"بدور على شقة وممكن معاينة والسعر كام\","` | — |
| [SRC-3451CC474D-L001131](../../tests/test_api.py#L1131) | 1131 | `"        \"https://example.com/company-b/housing\","` | — |
| [SRC-3451CC474D-L001132](../../tests/test_api.py#L1132) | 1132 | `"        tenant_id=\"company-b\","` | — |
| [SRC-3451CC474D-L001133](../../tests/test_api.py#L1133) | 1133 | `"    )"` | — |
| [SRC-3451CC474D-L001134](../../tests/test_api.py#L1134) | 1134 | `"    assert created is True"` | — |
| [SRC-3451CC474D-L001135](../../tests/test_api.py#L1135) | 1135 | `""` | — |
| [SRC-3451CC474D-L001136](../../tests/test_api.py#L1136) | 1136 | `"    status, stats_a = request_json("` | — |
| [SRC-3451CC474D-L001137](../../tests/test_api.py#L1137) | 1137 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001138](../../tests/test_api.py#L1138) | 1138 | `"        \"/api/ask\","` | — |
| [SRC-3451CC474D-L001139](../../tests/test_api.py#L1139) | 1139 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001140](../../tests/test_api.py#L1140) | 1140 | `"        payload={\"question\": \"كام عميل\", \"tenant_id\": \"default\"},"` | — |
| [SRC-3451CC474D-L001141](../../tests/test_api.py#L1141) | 1141 | `"    )"` | — |
| [SRC-3451CC474D-L001142](../../tests/test_api.py#L1142) | 1142 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L001143](../../tests/test_api.py#L1143) | 1143 | `"    assert \"0 إشارة\" in stats_a[\"answer\"]"` | — |
| [SRC-3451CC474D-L001144](../../tests/test_api.py#L1144) | 1144 | `""` | — |
| [SRC-3451CC474D-L001145](../../tests/test_api.py#L1145) | 1145 | `"    status, stats_b = request_json("` | — |
| [SRC-3451CC474D-L001146](../../tests/test_api.py#L1146) | 1146 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001147](../../tests/test_api.py#L1147) | 1147 | `"        \"/api/ask\","` | — |
| [SRC-3451CC474D-L001148](../../tests/test_api.py#L1148) | 1148 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001149](../../tests/test_api.py#L1149) | 1149 | `"        payload={\"question\": \"كام عميل\", \"tenant_id\": \"company-b\"},"` | — |
| [SRC-3451CC474D-L001150](../../tests/test_api.py#L1150) | 1150 | `"        headers={\"X-Omarai-Test-User\": \"user-b\"},"` | — |
| [SRC-3451CC474D-L001151](../../tests/test_api.py#L1151) | 1151 | `"    )"` | — |
| [SRC-3451CC474D-L001152](../../tests/test_api.py#L1152) | 1152 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L001153](../../tests/test_api.py#L1153) | 1153 | `"    assert \"1 إشارة\" in stats_b[\"answer\"]"` | — |
| [SRC-3451CC474D-L001154](../../tests/test_api.py#L1154) | 1154 | `""` | — |
| [SRC-3451CC474D-L001155](../../tests/test_api.py#L1155) | 1155 | `"    status, recommendation_b = request_json("` | — |
| [SRC-3451CC474D-L001156](../../tests/test_api.py#L1156) | 1156 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001157](../../tests/test_api.py#L1157) | 1157 | `"        \"/api/ask\","` | — |
| [SRC-3451CC474D-L001158](../../tests/test_api.py#L1158) | 1158 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001159](../../tests/test_api.py#L1159) | 1159 | `"        payload={\"question\": \"مين افضل عميل\", \"tenant_id\": \"company-b\"},"` | — |
| [SRC-3451CC474D-L001160](../../tests/test_api.py#L1160) | 1160 | `"        headers={\"X-Omarai-Test-User\": \"user-b\"},"` | — |
| [SRC-3451CC474D-L001161](../../tests/test_api.py#L1161) | 1161 | `"    )"` | — |
| [SRC-3451CC474D-L001162](../../tests/test_api.py#L1162) | 1162 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L001163](../../tests/test_api.py#L1163) | 1163 | `"    assert lead_b[\"id\"][:8] in recommendation_b[\"answer\"]"` | — |
| [SRC-3451CC474D-L001164](../../tests/test_api.py#L1164) | 1164 | `""` | — |
| [SRC-3451CC474D-L001165](../../tests/test_api.py#L1165) | 1165 | `"    # The default-company operator cannot select company B for a recommendation."` | — |
| [SRC-3451CC474D-L001166](../../tests/test_api.py#L1166) | 1166 | `"    status, _denied = request_json("` | — |
| [SRC-3451CC474D-L001167](../../tests/test_api.py#L1167) | 1167 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001168](../../tests/test_api.py#L1168) | 1168 | `"        \"/api/ask\","` | — |
| [SRC-3451CC474D-L001169](../../tests/test_api.py#L1169) | 1169 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001170](../../tests/test_api.py#L1170) | 1170 | `"        payload={\"question\": \"مين افضل عميل\", \"tenant_id\": \"company-b\"},"` | — |
| [SRC-3451CC474D-L001171](../../tests/test_api.py#L1171) | 1171 | `"    )"` | — |
| [SRC-3451CC474D-L001172](../../tests/test_api.py#L1172) | 1172 | `"    assert status == 403"` | — |
## اختبارات

### FILE-6CBA87B20C — [tests/test_aspect_planning.py](../../tests/test_aspect_planning.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6CBA87B20C-L000001](../../tests/test_aspect_planning.py#L1) | 1 | `"\"\"\"Unit tests for aspect extraction and evidence ledger (no network).\"\"\""` | — |
| [SRC-6CBA87B20C-L000002](../../tests/test_aspect_planning.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-6CBA87B20C-L000003](../../tests/test_aspect_planning.py#L3) | 3 | `""` | — |
| [SRC-6CBA87B20C-L000004](../../tests/test_aspect_planning.py#L4) | 4 | `"from agents.aspect_planning import ("` | — |
| [SRC-6CBA87B20C-L000005](../../tests/test_aspect_planning.py#L5) | 5 | `"    arabic_aspect_diagnostics,"` | — |
| [SRC-6CBA87B20C-L000006](../../tests/test_aspect_planning.py#L6) | 6 | `"    build_aspect_queries,"` | — |
| [SRC-6CBA87B20C-L000007](../../tests/test_aspect_planning.py#L7) | 7 | `"    build_evidence_ledger,"` | — |
| [SRC-6CBA87B20C-L000008](../../tests/test_aspect_planning.py#L8) | 8 | `"    extract_aspects,"` | — |
| [SRC-6CBA87B20C-L000009](../../tests/test_aspect_planning.py#L9) | 9 | `"    repair_queries_for_missing_aspects,"` | — |
| [SRC-6CBA87B20C-L000010](../../tests/test_aspect_planning.py#L10) | 10 | `")"` | — |
| [SRC-6CBA87B20C-L000011](../../tests/test_aspect_planning.py#L11) | 11 | `""` | — |
| [SRC-6CBA87B20C-L000012](../../tests/test_aspect_planning.py#L12) | 12 | `""` | — |
| [SRC-6CBA87B20C-L000013](../../tests/test_aspect_planning.py#L13) | 13 | `"def test_extract_aspects_from_min_hayth():"` | — |
| [SRC-6CBA87B20C-L000014](../../tests/test_aspect_planning.py#L14) | 14 | `"    q = ("` | — |
| [SRC-6CBA87B20C-L000015](../../tests/test_aspect_planning.py#L15) | 15 | `"        \"حلل السيارات الكهربائية في مصر من حيث السعر، البطارية، والضمان. \""` | — |
| [SRC-6CBA87B20C-L000016](../../tests/test_aspect_planning.py#L16) | 16 | `"        \"اذكر مصادر موثوقة.\""` | — |
| [SRC-6CBA87B20C-L000017](../../tests/test_aspect_planning.py#L17) | 17 | `"    )"` | — |
| [SRC-6CBA87B20C-L000018](../../tests/test_aspect_planning.py#L18) | 18 | `"    aspects = extract_aspects(q)"` | — |
| [SRC-6CBA87B20C-L000019](../../tests/test_aspect_planning.py#L19) | 19 | `"    assert \"السعر\" in aspects or any(\"سعر\" in a for a in aspects)"` | — |
| [SRC-6CBA87B20C-L000020](../../tests/test_aspect_planning.py#L20) | 20 | `"    assert any(\"بطار\" in a for a in aspects)"` | — |
| [SRC-6CBA87B20C-L000021](../../tests/test_aspect_planning.py#L21) | 21 | `"    assert any(\"ضمان\" in a for a in aspects)"` | — |
| [SRC-6CBA87B20C-L000022](../../tests/test_aspect_planning.py#L22) | 22 | `"    assert len(aspects) >= 3"` | — |
| [SRC-6CBA87B20C-L000023](../../tests/test_aspect_planning.py#L23) | 23 | `""` | — |
| [SRC-6CBA87B20C-L000024](../../tests/test_aspect_planning.py#L24) | 24 | `""` | — |
| [SRC-6CBA87B20C-L000025](../../tests/test_aspect_planning.py#L25) | 25 | `"def test_extract_aspects_from_multi_question_marks():"` | — |
| [SRC-6CBA87B20C-L000026](../../tests/test_aspect_planning.py#L26) | 26 | `"    q = \"ما سعر الآيفون في مصر؟ وما مدة الضمان؟ وهل تتوفر صيانة محلية؟\""` | — |
| [SRC-6CBA87B20C-L000027](../../tests/test_aspect_planning.py#L27) | 27 | `"    aspects = extract_aspects(q)"` | — |
| [SRC-6CBA87B20C-L000028](../../tests/test_aspect_planning.py#L28) | 28 | `"    assert len(aspects) >= 2"` | — |
| [SRC-6CBA87B20C-L000029](../../tests/test_aspect_planning.py#L29) | 29 | `""` | — |
| [SRC-6CBA87B20C-L000030](../../tests/test_aspect_planning.py#L30) | 30 | `""` | — |
| [SRC-6CBA87B20C-L000031](../../tests/test_aspect_planning.py#L31) | 31 | `"def test_build_aspect_queries_prioritizes_topic():"` | — |
| [SRC-6CBA87B20C-L000032](../../tests/test_aspect_planning.py#L32) | 32 | `"    queries = build_aspect_queries("` | — |
| [SRC-6CBA87B20C-L000033](../../tests/test_aspect_planning.py#L33) | 33 | `"        \"السيارات الكهربائية في مصر\","` | — |
| [SRC-6CBA87B20C-L000034](../../tests/test_aspect_planning.py#L34) | 34 | `"        [\"السعر\", \"الضمان\"],"` | — |
| [SRC-6CBA87B20C-L000035](../../tests/test_aspect_planning.py#L35) | 35 | `"        limit=5,"` | — |
| [SRC-6CBA87B20C-L000036](../../tests/test_aspect_planning.py#L36) | 36 | `"    )"` | — |
| [SRC-6CBA87B20C-L000037](../../tests/test_aspect_planning.py#L37) | 37 | `"    assert queries[0] == \"السيارات الكهربائية في مصر\""` | — |
| [SRC-6CBA87B20C-L000038](../../tests/test_aspect_planning.py#L38) | 38 | `"    assert any(\"السعر\" in q for q in queries)"` | — |
| [SRC-6CBA87B20C-L000039](../../tests/test_aspect_planning.py#L39) | 39 | `"    assert any(\"الضمان\" in q for q in queries)"` | — |
| [SRC-6CBA87B20C-L000040](../../tests/test_aspect_planning.py#L40) | 40 | `"    assert len(queries) <= 5"` | — |
| [SRC-6CBA87B20C-L000041](../../tests/test_aspect_planning.py#L41) | 41 | `""` | — |
| [SRC-6CBA87B20C-L000042](../../tests/test_aspect_planning.py#L42) | 42 | `""` | — |
| [SRC-6CBA87B20C-L000043](../../tests/test_aspect_planning.py#L43) | 43 | `"def test_evidence_ledger_marks_missing_and_covered():"` | — |
| [SRC-6CBA87B20C-L000044](../../tests/test_aspect_planning.py#L44) | 44 | `"    aspects = [\"السعر\", \"الضمان\"]"` | — |
| [SRC-6CBA87B20C-L000045](../../tests/test_aspect_planning.py#L45) | 45 | `"    sources = ["` | — |
| [SRC-6CBA87B20C-L000046](../../tests/test_aspect_planning.py#L46) | 46 | `"        {"` | — |
| [SRC-6CBA87B20C-L000047](../../tests/test_aspect_planning.py#L47) | 47 | `"            \"title\": \"أسعار السيارات الكهربائية\","` | — |
| [SRC-6CBA87B20C-L000048](../../tests/test_aspect_planning.py#L48) | 48 | `"            \"url\": \"https://example.com/prices\","` | — |
| [SRC-6CBA87B20C-L000049](../../tests/test_aspect_planning.py#L49) | 49 | `"            \"snippet\": \"متوسط السعر في مصر لعام 2026\","` | — |
| [SRC-6CBA87B20C-L000050](../../tests/test_aspect_planning.py#L50) | 50 | `"            \"page_text\": \"\","` | — |
| [SRC-6CBA87B20C-L000051](../../tests/test_aspect_planning.py#L51) | 51 | `"            \"provider\": \"test\","` | — |
| [SRC-6CBA87B20C-L000052](../../tests/test_aspect_planning.py#L52) | 52 | `"        }"` | — |
| [SRC-6CBA87B20C-L000053](../../tests/test_aspect_planning.py#L53) | 53 | `"    ]"` | — |
| [SRC-6CBA87B20C-L000054](../../tests/test_aspect_planning.py#L54) | 54 | `"    ledger = build_evidence_ledger(aspects, sources)"` | — |
| [SRC-6CBA87B20C-L000055](../../tests/test_aspect_planning.py#L55) | 55 | `"    assert \"السعر\" in ledger[\"covered\"] or any("` | — |
| [SRC-6CBA87B20C-L000056](../../tests/test_aspect_planning.py#L56) | 56 | `"        \"سعر\" in c for c in ledger[\"covered\"]"` | — |
| [SRC-6CBA87B20C-L000057](../../tests/test_aspect_planning.py#L57) | 57 | `"    )"` | — |
| [SRC-6CBA87B20C-L000058](../../tests/test_aspect_planning.py#L58) | 58 | `"    assert \"الضمان\" in ledger[\"missing\"]"` | — |
| [SRC-6CBA87B20C-L000059](../../tests/test_aspect_planning.py#L59) | 59 | `"    assert 0 <= ledger[\"coverage_ratio\"] <= 1"` | — |
| [SRC-6CBA87B20C-L000060](../../tests/test_aspect_planning.py#L60) | 60 | `""` | — |
| [SRC-6CBA87B20C-L000061](../../tests/test_aspect_planning.py#L61) | 61 | `""` | — |
| [SRC-6CBA87B20C-L000062](../../tests/test_aspect_planning.py#L62) | 62 | `"def test_repair_queries_for_missing():"` | — |
| [SRC-6CBA87B20C-L000063](../../tests/test_aspect_planning.py#L63) | 63 | `"    qs = repair_queries_for_missing_aspects("` | — |
| [SRC-6CBA87B20C-L000064](../../tests/test_aspect_planning.py#L64) | 64 | `"        \"السيارات الكهربائية مصر\","` | — |
| [SRC-6CBA87B20C-L000065](../../tests/test_aspect_planning.py#L65) | 65 | `"        [\"الضمان\", \"الصيانة\"],"` | — |
| [SRC-6CBA87B20C-L000066](../../tests/test_aspect_planning.py#L66) | 66 | `"        limit=2,"` | — |
| [SRC-6CBA87B20C-L000067](../../tests/test_aspect_planning.py#L67) | 67 | `"    )"` | — |
| [SRC-6CBA87B20C-L000068](../../tests/test_aspect_planning.py#L68) | 68 | `"    assert len(qs) == 2"` | — |
| [SRC-6CBA87B20C-L000069](../../tests/test_aspect_planning.py#L69) | 69 | `"    assert all(\"السيارات\" in q for q in qs)"` | — |
| [SRC-6CBA87B20C-L000070](../../tests/test_aspect_planning.py#L70) | 70 | `""` | — |
| [SRC-6CBA87B20C-L000071](../../tests/test_aspect_planning.py#L71) | 71 | `""` | — |
| [SRC-6CBA87B20C-L000072](../../tests/test_aspect_planning.py#L72) | 72 | `"def test_arabic_diagnostics_not_truth_claim():"` | — |
| [SRC-6CBA87B20C-L000073](../../tests/test_aspect_planning.py#L73) | 73 | `"    ledger = {"` | — |
| [SRC-6CBA87B20C-L000074](../../tests/test_aspect_planning.py#L74) | 74 | `"        \"covered\": [\"السعر\"],"` | — |
| [SRC-6CBA87B20C-L000075](../../tests/test_aspect_planning.py#L75) | 75 | `"        \"missing\": [\"الضمان\"],"` | — |
| [SRC-6CBA87B20C-L000076](../../tests/test_aspect_planning.py#L76) | 76 | `"        \"coverage_ratio\": 0.5,"` | — |
| [SRC-6CBA87B20C-L000077](../../tests/test_aspect_planning.py#L77) | 77 | `"    }"` | — |
| [SRC-6CBA87B20C-L000078](../../tests/test_aspect_planning.py#L78) | 78 | `"    lines = arabic_aspect_diagnostics(ledger)"` | — |
| [SRC-6CBA87B20C-L000079](../../tests/test_aspect_planning.py#L79) | 79 | `"    assert any(\"ضمان\" in line for line in lines)"` | — |
| [SRC-6CBA87B20C-L000080](../../tests/test_aspect_planning.py#L80) | 80 | `"    assert any(\"لا يثبت\" in line for line in lines)"` | — |
| [SRC-6CBA87B20C-L000081](../../tests/test_aspect_planning.py#L81) | 81 | `""` | — |
| [SRC-6CBA87B20C-L000082](../../tests/test_aspect_planning.py#L82) | 82 | `""` | — |
| [SRC-6CBA87B20C-L000083](../../tests/test_aspect_planning.py#L83) | 83 | `"def test_extract_aspects_understands_compound_connectors_without_marker():"` | — |
| [SRC-6CBA87B20C-L000084](../../tests/test_aspect_planning.py#L84) | 84 | `"    question = ("` | — |
| [SRC-6CBA87B20C-L000085](../../tests/test_aspect_planning.py#L85) | 85 | `"        \"قارن بين الأنظمة: السعر والبطارية، بالإضافة إلى الضمان والصيانة \""` | — |
| [SRC-6CBA87B20C-L000086](../../tests/test_aspect_planning.py#L86) | 86 | `"        \"والخصوصية والاعتمادية والدعم والجودة\""` | — |
| [SRC-6CBA87B20C-L000087](../../tests/test_aspect_planning.py#L87) | 87 | `"    )"` | — |
| [SRC-6CBA87B20C-L000088](../../tests/test_aspect_planning.py#L88) | 88 | `"    aspects = extract_aspects(question)"` | — |
| [SRC-6CBA87B20C-L000089](../../tests/test_aspect_planning.py#L89) | 89 | `"    normalized = \" \".join(aspects)"` | — |
| [SRC-6CBA87B20C-L000090](../../tests/test_aspect_planning.py#L90) | 90 | `"    for expected in (\"السعر\", \"البطارية\", \"الضمان\", \"الصيانة\", \"الخصوصية\", \"الاعتمادية\", \"الدعم\", \"الجودة\"):"` | — |
| [SRC-6CBA87B20C-L000091](../../tests/test_aspect_planning.py#L91) | 91 | `"        assert expected in normalized"` | — |
| [SRC-6CBA87B20C-L000092](../../tests/test_aspect_planning.py#L92) | 92 | `"    assert len(aspects) <= 8"` | — |
| [SRC-6CBA87B20C-L000093](../../tests/test_aspect_planning.py#L93) | 93 | `""` | — |
| [SRC-6CBA87B20C-L000094](../../tests/test_aspect_planning.py#L94) | 94 | `""` | — |
| [SRC-6CBA87B20C-L000095](../../tests/test_aspect_planning.py#L95) | 95 | `"def test_extracts_joined_facets_without_formal_comparison_marker():"` | — |
| [SRC-6CBA87B20C-L000096](../../tests/test_aspect_planning.py#L96) | 96 | `"    aspects = extract_aspects(\"ما سعر الهاتف ومدة الضمان والصيانة؟\")"` | — |
| [SRC-6CBA87B20C-L000097](../../tests/test_aspect_planning.py#L97) | 97 | `"    joined = \" \".join(aspects)"` | — |
| [SRC-6CBA87B20C-L000098](../../tests/test_aspect_planning.py#L98) | 98 | `"    assert \"السعر\" in joined"` | — |
| [SRC-6CBA87B20C-L000099](../../tests/test_aspect_planning.py#L99) | 99 | `"    assert \"الضمان\" in joined"` | — |
| [SRC-6CBA87B20C-L000100](../../tests/test_aspect_planning.py#L100) | 100 | `"    assert \"الصيانة\" in joined"` | — |
| [SRC-6CBA87B20C-L000101](../../tests/test_aspect_planning.py#L101) | 101 | `""` | — |
| [SRC-6CBA87B20C-L000102](../../tests/test_aspect_planning.py#L102) | 102 | `""` | — |
| [SRC-6CBA87B20C-L000103](../../tests/test_aspect_planning.py#L103) | 103 | `"def test_extracts_general_factual_aspects_from_compound_arabic_question():"` | — |
| [SRC-6CBA87B20C-L000104](../../tests/test_aspect_planning.py#L104) | 104 | `"    question = \"اذكر عاصمة مصر وعدد سكان القاهرة، مع مصدر وتاريخ لكل معلومة\""` | — |
| [SRC-6CBA87B20C-L000105](../../tests/test_aspect_planning.py#L105) | 105 | `"    aspects = extract_aspects(question)"` | — |
| [SRC-6CBA87B20C-L000106](../../tests/test_aspect_planning.py#L106) | 106 | `"    joined = \" \".join(aspects)"` | — |
| [SRC-6CBA87B20C-L000107](../../tests/test_aspect_planning.py#L107) | 107 | `"    assert \"العاصمة\" in joined"` | — |
| [SRC-6CBA87B20C-L000108](../../tests/test_aspect_planning.py#L108) | 108 | `"    assert \"عدد السكان\" in joined"` | — |
| [SRC-6CBA87B20C-L000109](../../tests/test_aspect_planning.py#L109) | 109 | `"    assert len(aspects) <= 8"` | — |
| [SRC-6CBA87B20C-L000110](../../tests/test_aspect_planning.py#L110) | 110 | `""` | — |
| [SRC-6CBA87B20C-L000111](../../tests/test_aspect_planning.py#L111) | 111 | `""` | — |
| [SRC-6CBA87B20C-L000112](../../tests/test_aspect_planning.py#L112) | 112 | `"def test_builds_separate_queries_for_capital_and_population_aspects():"` | — |
| [SRC-6CBA87B20C-L000113](../../tests/test_aspect_planning.py#L113) | 113 | `"    question = \"اذكر عاصمة مصر وعدد سكان القاهرة\""` | — |
| [SRC-6CBA87B20C-L000114](../../tests/test_aspect_planning.py#L114) | 114 | `"    aspects = extract_aspects(question)"` | — |
| [SRC-6CBA87B20C-L000115](../../tests/test_aspect_planning.py#L115) | 115 | `"    queries = build_aspect_queries(\"مصر القاهرة\", aspects)"` | — |
| [SRC-6CBA87B20C-L000116](../../tests/test_aspect_planning.py#L116) | 116 | `"    assert any(\"العاصمة\" in query for query in queries)"` | — |
| [SRC-6CBA87B20C-L000117](../../tests/test_aspect_planning.py#L117) | 117 | `"    assert any(\"عدد السكان\" in query for query in queries)"` | — |
## اختبارات

### FILE-6B37B7D6D3 — [tests/test_claim_evidence_metadata.py](../../tests/test_claim_evidence_metadata.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6B37B7D6D3-L000001](../../tests/test_claim_evidence_metadata.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-6B37B7D6D3-L000002](../../tests/test_claim_evidence_metadata.py#L2) | 2 | `""` | — |
| [SRC-6B37B7D6D3-L000003](../../tests/test_claim_evidence_metadata.py#L3) | 3 | `"from agents.claim_evidence import audit_source_metadata, build_claim_evidence_ledger"` | — |
| [SRC-6B37B7D6D3-L000004](../../tests/test_claim_evidence_metadata.py#L4) | 4 | `""` | — |
| [SRC-6B37B7D6D3-L000005](../../tests/test_claim_evidence_metadata.py#L5) | 5 | `""` | — |
| [SRC-6B37B7D6D3-L000006](../../tests/test_claim_evidence_metadata.py#L6) | 6 | `"def test_source_metadata_accepts_complete_population_metadata_without_asserting_truth():"` | — |
| [SRC-6B37B7D6D3-L000007](../../tests/test_claim_evidence_metadata.py#L7) | 7 | `"    result = audit_source_metadata("` | — |
| [SRC-6B37B7D6D3-L000008](../../tests/test_claim_evidence_metadata.py#L8) | 8 | `"        {"` | — |
| [SRC-6B37B7D6D3-L000009](../../tests/test_claim_evidence_metadata.py#L9) | 9 | `"            \"url\": \"https://example.org/census\","` | — |
| [SRC-6B37B7D6D3-L000010](../../tests/test_claim_evidence_metadata.py#L10) | 10 | `"            \"title\": \"Population table\","` | — |
| [SRC-6B37B7D6D3-L000011](../../tests/test_claim_evidence_metadata.py#L11) | 11 | `"            \"publisher\": \"Example Statistics Office\","` | — |
| [SRC-6B37B7D6D3-L000012](../../tests/test_claim_evidence_metadata.py#L12) | 12 | `"            \"published_at\": \"2025-06-01\","` | — |
| [SRC-6B37B7D6D3-L000013](../../tests/test_claim_evidence_metadata.py#L13) | 13 | `"            \"data_reference_period\": \"2025 estimate\","` | — |
| [SRC-6B37B7D6D3-L000014](../../tests/test_claim_evidence_metadata.py#L14) | 14 | `"            \"geographic_scope\": \"Cairo Governorate administrative boundaries\","` | — |
| [SRC-6B37B7D6D3-L000015](../../tests/test_claim_evidence_metadata.py#L15) | 15 | `"            \"snippet\": \"Population estimate for the governorate.\","` | — |
| [SRC-6B37B7D6D3-L000016](../../tests/test_claim_evidence_metadata.py#L16) | 16 | `"        },"` | — |
| [SRC-6B37B7D6D3-L000017](../../tests/test_claim_evidence_metadata.py#L17) | 17 | `"        claim_text=\"عدد سكان محافظة القاهرة\","` | — |
| [SRC-6B37B7D6D3-L000018](../../tests/test_claim_evidence_metadata.py#L18) | 18 | `"    )"` | — |
| [SRC-6B37B7D6D3-L000019](../../tests/test_claim_evidence_metadata.py#L19) | 19 | `""` | — |
| [SRC-6B37B7D6D3-L000020](../../tests/test_claim_evidence_metadata.py#L20) | 20 | `"    assert result[\"status\"] == \"metadata_complete\""` | — |
| [SRC-6B37B7D6D3-L000021](../../tests/test_claim_evidence_metadata.py#L21) | 21 | `"    assert result[\"required_fields_missing\"] == []"` | — |
| [SRC-6B37B7D6D3-L000022](../../tests/test_claim_evidence_metadata.py#L22) | 22 | `"    assert result[\"claim_entailment\"] == \"not_checked\""` | — |
| [SRC-6B37B7D6D3-L000023](../../tests/test_claim_evidence_metadata.py#L23) | 23 | `"    assert result[\"fact_correctness\"] == \"not_checked\""` | — |
| [SRC-6B37B7D6D3-L000024](../../tests/test_claim_evidence_metadata.py#L24) | 24 | `"    assert result[\"semantic_verification\"] is False"` | — |
| [SRC-6B37B7D6D3-L000025](../../tests/test_claim_evidence_metadata.py#L25) | 25 | `""` | — |
| [SRC-6B37B7D6D3-L000026](../../tests/test_claim_evidence_metadata.py#L26) | 26 | `""` | — |
| [SRC-6B37B7D6D3-L000027](../../tests/test_claim_evidence_metadata.py#L27) | 27 | `"def test_source_metadata_flags_missing_publication_date_period_and_population_scope():"` | — |
| [SRC-6B37B7D6D3-L000028](../../tests/test_claim_evidence_metadata.py#L28) | 28 | `"    result = audit_source_metadata("` | — |
| [SRC-6B37B7D6D3-L000029](../../tests/test_claim_evidence_metadata.py#L29) | 29 | `"        {"` | — |
| [SRC-6B37B7D6D3-L000030](../../tests/test_claim_evidence_metadata.py#L30) | 30 | `"            \"url\": \"https://example.org/census\","` | — |
| [SRC-6B37B7D6D3-L000031](../../tests/test_claim_evidence_metadata.py#L31) | 31 | `"            \"title\": \"Population table\","` | — |
| [SRC-6B37B7D6D3-L000032](../../tests/test_claim_evidence_metadata.py#L32) | 32 | `"            \"publisher\": \"Example Statistics Office\","` | — |
| [SRC-6B37B7D6D3-L000033](../../tests/test_claim_evidence_metadata.py#L33) | 33 | `"            \"snippet\": \"Population estimate.\","` | — |
| [SRC-6B37B7D6D3-L000034](../../tests/test_claim_evidence_metadata.py#L34) | 34 | `"        },"` | — |
| [SRC-6B37B7D6D3-L000035](../../tests/test_claim_evidence_metadata.py#L35) | 35 | `"        claim_text=\"عدد سكان القاهرة الكبرى\","` | — |
| [SRC-6B37B7D6D3-L000036](../../tests/test_claim_evidence_metadata.py#L36) | 36 | `"    )"` | — |
| [SRC-6B37B7D6D3-L000037](../../tests/test_claim_evidence_metadata.py#L37) | 37 | `""` | — |
| [SRC-6B37B7D6D3-L000038](../../tests/test_claim_evidence_metadata.py#L38) | 38 | `"    assert result[\"status\"] == \"metadata_incomplete\""` | — |
| [SRC-6B37B7D6D3-L000039](../../tests/test_claim_evidence_metadata.py#L39) | 39 | `"    assert \"publication_date\" in result[\"required_fields_missing\"]"` | — |
| [SRC-6B37B7D6D3-L000040](../../tests/test_claim_evidence_metadata.py#L40) | 40 | `"    assert \"data_reference_period_for_population_claim\" in result[\"required_fields_missing\"]"` | — |
| [SRC-6B37B7D6D3-L000041](../../tests/test_claim_evidence_metadata.py#L41) | 41 | `"    assert \"geographic_scope_for_population_claim\" in result[\"required_fields_missing\"]"` | — |
| [SRC-6B37B7D6D3-L000042](../../tests/test_claim_evidence_metadata.py#L42) | 42 | `""` | — |
| [SRC-6B37B7D6D3-L000043](../../tests/test_claim_evidence_metadata.py#L43) | 43 | `""` | — |
| [SRC-6B37B7D6D3-L000044](../../tests/test_claim_evidence_metadata.py#L44) | 44 | `"def test_source_metadata_rejects_non_http_urls_and_urls_with_credentials():"` | — |
| [SRC-6B37B7D6D3-L000045](../../tests/test_claim_evidence_metadata.py#L45) | 45 | `"    for url in (\"javascript:alert(1)\", \"https://user:password@example.org/data\"):"` | — |
| [SRC-6B37B7D6D3-L000046](../../tests/test_claim_evidence_metadata.py#L46) | 46 | `"        result = audit_source_metadata("` | — |
| [SRC-6B37B7D6D3-L000047](../../tests/test_claim_evidence_metadata.py#L47) | 47 | `"            {"` | — |
| [SRC-6B37B7D6D3-L000048](../../tests/test_claim_evidence_metadata.py#L48) | 48 | `"                \"url\": url,"` | — |
| [SRC-6B37B7D6D3-L000049](../../tests/test_claim_evidence_metadata.py#L49) | 49 | `"                \"title\": \"Research report\","` | — |
| [SRC-6B37B7D6D3-L000050](../../tests/test_claim_evidence_metadata.py#L50) | 50 | `"                \"publisher\": \"Example Statistics Office\","` | — |
| [SRC-6B37B7D6D3-L000051](../../tests/test_claim_evidence_metadata.py#L51) | 51 | `"                \"published_at\": \"2025-06-01\","` | — |
| [SRC-6B37B7D6D3-L000052](../../tests/test_claim_evidence_metadata.py#L52) | 52 | `"                \"snippet\": \"A readable summary.\","` | — |
| [SRC-6B37B7D6D3-L000053](../../tests/test_claim_evidence_metadata.py#L53) | 53 | `"            },"` | — |
| [SRC-6B37B7D6D3-L000054](../../tests/test_claim_evidence_metadata.py#L54) | 54 | `"            claim_text=\"general research\","` | — |
| [SRC-6B37B7D6D3-L000055](../../tests/test_claim_evidence_metadata.py#L55) | 55 | `"        )"` | — |
| [SRC-6B37B7D6D3-L000056](../../tests/test_claim_evidence_metadata.py#L56) | 56 | `""` | — |
| [SRC-6B37B7D6D3-L000057](../../tests/test_claim_evidence_metadata.py#L57) | 57 | `"        assert result[\"valid_http_url\"] is False"` | — |
| [SRC-6B37B7D6D3-L000058](../../tests/test_claim_evidence_metadata.py#L58) | 58 | `"        assert \"valid_http_source_url\" in result[\"required_fields_missing\"]"` | — |
| [SRC-6B37B7D6D3-L000059](../../tests/test_claim_evidence_metadata.py#L59) | 59 | `""` | — |
| [SRC-6B37B7D6D3-L000060](../../tests/test_claim_evidence_metadata.py#L60) | 60 | `""` | — |
| [SRC-6B37B7D6D3-L000061](../../tests/test_claim_evidence_metadata.py#L61) | 61 | `"def test_claim_evidence_ledger_uses_question_context_for_population_metadata():"` | — |
| [SRC-6B37B7D6D3-L000062](../../tests/test_claim_evidence_metadata.py#L62) | 62 | `"    ledger = build_claim_evidence_ledger("` | — |
| [SRC-6B37B7D6D3-L000063](../../tests/test_claim_evidence_metadata.py#L63) | 63 | `"        \"The estimate is 9.7 million [source 1].\","` | — |
| [SRC-6B37B7D6D3-L000064](../../tests/test_claim_evidence_metadata.py#L64) | 64 | `"        ["` | — |
| [SRC-6B37B7D6D3-L000065](../../tests/test_claim_evidence_metadata.py#L65) | 65 | `"            {"` | — |
| [SRC-6B37B7D6D3-L000066](../../tests/test_claim_evidence_metadata.py#L66) | 66 | `"                \"url\": \"https://example.org/census\","` | — |
| [SRC-6B37B7D6D3-L000067](../../tests/test_claim_evidence_metadata.py#L67) | 67 | `"                \"title\": \"Population table\","` | — |
| [SRC-6B37B7D6D3-L000068](../../tests/test_claim_evidence_metadata.py#L68) | 68 | `"                \"publisher\": \"Example Statistics Office\","` | — |
| [SRC-6B37B7D6D3-L000069](../../tests/test_claim_evidence_metadata.py#L69) | 69 | `"                \"published_at\": \"2025-06-01\","` | — |
| [SRC-6B37B7D6D3-L000070](../../tests/test_claim_evidence_metadata.py#L70) | 70 | `"                \"snippet\": \"The estimate is 9.7 million.\","` | — |
| [SRC-6B37B7D6D3-L000071](../../tests/test_claim_evidence_metadata.py#L71) | 71 | `"            }"` | — |
| [SRC-6B37B7D6D3-L000072](../../tests/test_claim_evidence_metadata.py#L72) | 72 | `"        ],"` | — |
| [SRC-6B37B7D6D3-L000073](../../tests/test_claim_evidence_metadata.py#L73) | 73 | `"        question_context=\"How many people live in Cairo?\","` | — |
| [SRC-6B37B7D6D3-L000074](../../tests/test_claim_evidence_metadata.py#L74) | 74 | `"    )"` | — |
| [SRC-6B37B7D6D3-L000075](../../tests/test_claim_evidence_metadata.py#L75) | 75 | `""` | — |
| [SRC-6B37B7D6D3-L000076](../../tests/test_claim_evidence_metadata.py#L76) | 76 | `"    audit = ledger[\"segments\"][0][\"sources\"][0][\"metadata_audit\"]"` | — |
| [SRC-6B37B7D6D3-L000077](../../tests/test_claim_evidence_metadata.py#L77) | 77 | `"    assert audit[\"population_scope_required\"] is True"` | — |
| [SRC-6B37B7D6D3-L000078](../../tests/test_claim_evidence_metadata.py#L78) | 78 | `"    assert \"data_reference_period_for_population_claim\" in audit[\"required_fields_missing\"]"` | — |
| [SRC-6B37B7D6D3-L000079](../../tests/test_claim_evidence_metadata.py#L79) | 79 | `"    assert \"geographic_scope_for_population_claim\" in audit[\"required_fields_missing\"]"` | — |
| [SRC-6B37B7D6D3-L000080](../../tests/test_claim_evidence_metadata.py#L80) | 80 | `"    assert ledger[\"fact_correctness\"] == \"not_checked\""` | — |
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

### FILE-6BECF5AD00 — [tests/test_connectors_mocked.py](../../tests/test_connectors_mocked.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6BECF5AD00-L000001](../../tests/test_connectors_mocked.py#L1) | 1 | `"\"\"\"Connector unit tests with mocked HTTP (no live network required).\"\"\""` | — |
| [SRC-6BECF5AD00-L000002](../../tests/test_connectors_mocked.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-6BECF5AD00-L000003](../../tests/test_connectors_mocked.py#L3) | 3 | `""` | — |
| [SRC-6BECF5AD00-L000004](../../tests/test_connectors_mocked.py#L4) | 4 | `""` | — |
| [SRC-6BECF5AD00-L000005](../../tests/test_connectors_mocked.py#L5) | 5 | `"import agents.search_connectors as sc"` | — |
| [SRC-6BECF5AD00-L000006](../../tests/test_connectors_mocked.py#L6) | 6 | `""` | — |
| [SRC-6BECF5AD00-L000007](../../tests/test_connectors_mocked.py#L7) | 7 | `""` | — |
| [SRC-6BECF5AD00-L000008](../../tests/test_connectors_mocked.py#L8) | 8 | `"def test_openalex_parses_mocked_payload(monkeypatch):"` | — |
| [SRC-6BECF5AD00-L000009](../../tests/test_connectors_mocked.py#L9) | 9 | `"    payload = {"` | — |
| [SRC-6BECF5AD00-L000010](../../tests/test_connectors_mocked.py#L10) | 10 | `"        \"results\": ["` | — |
| [SRC-6BECF5AD00-L000011](../../tests/test_connectors_mocked.py#L11) | 11 | `"            {"` | — |
| [SRC-6BECF5AD00-L000012](../../tests/test_connectors_mocked.py#L12) | 12 | `"                \"display_name\": \"Electric Vehicles in Egypt\","` | — |
| [SRC-6BECF5AD00-L000013](../../tests/test_connectors_mocked.py#L13) | 13 | `"                \"id\": \"https://openalex.org/W123\","` | — |
| [SRC-6BECF5AD00-L000014](../../tests/test_connectors_mocked.py#L14) | 14 | `"                \"primary_location\": {\"landing_page_url\": \"https://example.org/paper\"},"` | — |
| [SRC-6BECF5AD00-L000015](../../tests/test_connectors_mocked.py#L15) | 15 | `"                \"concepts\": [{\"display_name\": \"Battery\"}],"` | — |
| [SRC-6BECF5AD00-L000016](../../tests/test_connectors_mocked.py#L16) | 16 | `"                \"publication_date\": \"2024-01-01\","` | — |
| [SRC-6BECF5AD00-L000017](../../tests/test_connectors_mocked.py#L17) | 17 | `"            }"` | — |
| [SRC-6BECF5AD00-L000018](../../tests/test_connectors_mocked.py#L18) | 18 | `"        ]"` | — |
| [SRC-6BECF5AD00-L000019](../../tests/test_connectors_mocked.py#L19) | 19 | `"    }"` | — |
| [SRC-6BECF5AD00-L000020](../../tests/test_connectors_mocked.py#L20) | 20 | `""` | — |
| [SRC-6BECF5AD00-L000021](../../tests/test_connectors_mocked.py#L21) | 21 | `"    def fake_json(url, headers=None, timeout=12):"` | — |
| [SRC-6BECF5AD00-L000022](../../tests/test_connectors_mocked.py#L22) | 22 | `"        return payload"` | — |
| [SRC-6BECF5AD00-L000023](../../tests/test_connectors_mocked.py#L23) | 23 | `""` | — |
| [SRC-6BECF5AD00-L000024](../../tests/test_connectors_mocked.py#L24) | 24 | `"    monkeypatch.setattr(sc, \"_http_get_json\", fake_json)"` | — |
| [SRC-6BECF5AD00-L000025](../../tests/test_connectors_mocked.py#L25) | 25 | `"    rows = sc.search_openalex(\"electric vehicles Egypt\", limit=3)"` | — |
| [SRC-6BECF5AD00-L000026](../../tests/test_connectors_mocked.py#L26) | 26 | `"    assert len(rows) == 1"` | — |
| [SRC-6BECF5AD00-L000027](../../tests/test_connectors_mocked.py#L27) | 27 | `"    assert rows[0][\"provider\"] == \"openalex\""` | — |
| [SRC-6BECF5AD00-L000028](../../tests/test_connectors_mocked.py#L28) | 28 | `"    assert rows[0][\"url\"] == \"https://example.org/paper\""` | — |
| [SRC-6BECF5AD00-L000029](../../tests/test_connectors_mocked.py#L29) | 29 | `"    assert rows[0][\"page_fetched\"] is False"` | — |
| [SRC-6BECF5AD00-L000030](../../tests/test_connectors_mocked.py#L30) | 30 | `""` | — |
| [SRC-6BECF5AD00-L000031](../../tests/test_connectors_mocked.py#L31) | 31 | `""` | — |
| [SRC-6BECF5AD00-L000032](../../tests/test_connectors_mocked.py#L32) | 32 | `"def test_arxiv_parses_atom(monkeypatch):"` | — |
| [SRC-6BECF5AD00-L000033](../../tests/test_connectors_mocked.py#L33) | 33 | `"    xml = \"\"\""` | — |
| [SRC-6BECF5AD00-L000034](../../tests/test_connectors_mocked.py#L34) | 34 | `"    <feed>"` | — |
| [SRC-6BECF5AD00-L000035](../../tests/test_connectors_mocked.py#L35) | 35 | `"      <entry>"` | — |
| [SRC-6BECF5AD00-L000036](../../tests/test_connectors_mocked.py#L36) | 36 | `"        <title>Study of EV Batteries</title>"` | — |
| [SRC-6BECF5AD00-L000037](../../tests/test_connectors_mocked.py#L37) | 37 | `"        <id>http://arxiv.org/abs/2401.00001</id>"` | — |
| [SRC-6BECF5AD00-L000038](../../tests/test_connectors_mocked.py#L38) | 38 | `"        <summary>Battery degradation analysis.</summary>"` | — |
| [SRC-6BECF5AD00-L000039](../../tests/test_connectors_mocked.py#L39) | 39 | `"        <published>2024-01-02T00:00:00Z</published>"` | — |
| [SRC-6BECF5AD00-L000040](../../tests/test_connectors_mocked.py#L40) | 40 | `"      </entry>"` | — |
| [SRC-6BECF5AD00-L000041](../../tests/test_connectors_mocked.py#L41) | 41 | `"    </feed>"` | — |
| [SRC-6BECF5AD00-L000042](../../tests/test_connectors_mocked.py#L42) | 42 | `"    \"\"\""` | — |
| [SRC-6BECF5AD00-L000043](../../tests/test_connectors_mocked.py#L43) | 43 | `""` | — |
| [SRC-6BECF5AD00-L000044](../../tests/test_connectors_mocked.py#L44) | 44 | `"    monkeypatch.setattr(sc, \"_http_get_text\", lambda url, timeout=12: xml)"` | — |
| [SRC-6BECF5AD00-L000045](../../tests/test_connectors_mocked.py#L45) | 45 | `"    rows = sc.search_arxiv(\"battery\", limit=2)"` | — |
| [SRC-6BECF5AD00-L000046](../../tests/test_connectors_mocked.py#L46) | 46 | `"    assert len(rows) == 1"` | — |
| [SRC-6BECF5AD00-L000047](../../tests/test_connectors_mocked.py#L47) | 47 | `"    assert rows[0][\"provider\"] == \"arxiv\""` | — |
| [SRC-6BECF5AD00-L000048](../../tests/test_connectors_mocked.py#L48) | 48 | `"    assert \"arxiv.org\" in rows[0][\"url\"]"` | — |
