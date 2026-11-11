# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **046**
- سجلات الأسطر: **800**
- النطاق: SRC-3451CC474D-L001005 إلى SRC-DA61479D59-L000067
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-3451CC474D — [tests/test_api.py](../../tests/test_api.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-3451CC474D-L001005](../../tests/test_api.py#L1005) | 1005 | `"    script_blocks = 0"` | — |
| [SRC-3451CC474D-L001006](../../tests/test_api.py#L1006) | 1006 | `"    style_blocks = 0"` | — |
| [SRC-3451CC474D-L001007](../../tests/test_api.py#L1007) | 1007 | `"    style_attributes = 0"` | — |
| [SRC-3451CC474D-L001008](../../tests/test_api.py#L1008) | 1008 | `"    for html_path in api_module.ROOT.glob(\"*.html\"):"` | — |
| [SRC-3451CC474D-L001009](../../tests/test_api.py#L1009) | 1009 | `"        document = html_path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3451CC474D-L001010](../../tests/test_api.py#L1010) | 1010 | `"        for match in re.finditer("` | — |
| [SRC-3451CC474D-L001011](../../tests/test_api.py#L1011) | 1011 | `"            r\"<script\\b(?P<attrs>[^>]*)>(?P<body>.*?)</script\\s*>\","` | — |
| [SRC-3451CC474D-L001012](../../tests/test_api.py#L1012) | 1012 | `"            document,"` | — |
| [SRC-3451CC474D-L001013](../../tests/test_api.py#L1013) | 1013 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-3451CC474D-L001014](../../tests/test_api.py#L1014) | 1014 | `"        ):"` | — |
| [SRC-3451CC474D-L001015](../../tests/test_api.py#L1015) | 1015 | `"            if re.search(r\"\\bsrc\\s*=\", match.group(\"attrs\"), re.IGNORECASE):"` | — |
| [SRC-3451CC474D-L001016](../../tests/test_api.py#L1016) | 1016 | `"                continue"` | — |
| [SRC-3451CC474D-L001017](../../tests/test_api.py#L1017) | 1017 | `"            script_blocks += 1"` | — |
| [SRC-3451CC474D-L001018](../../tests/test_api.py#L1018) | 1018 | `"            assert api_module._csp_hash_source(match.group(\"body\")) in policy"` | — |
| [SRC-3451CC474D-L001019](../../tests/test_api.py#L1019) | 1019 | `"        for match in re.finditer("` | — |
| [SRC-3451CC474D-L001020](../../tests/test_api.py#L1020) | 1020 | `"            r\"<style\\b[^>]*>(?P<body>.*?)</style\\s*>\","` | — |
| [SRC-3451CC474D-L001021](../../tests/test_api.py#L1021) | 1021 | `"            document,"` | — |
| [SRC-3451CC474D-L001022](../../tests/test_api.py#L1022) | 1022 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-3451CC474D-L001023](../../tests/test_api.py#L1023) | 1023 | `"        ):"` | — |
| [SRC-3451CC474D-L001024](../../tests/test_api.py#L1024) | 1024 | `"            style_blocks += 1"` | — |
| [SRC-3451CC474D-L001025](../../tests/test_api.py#L1025) | 1025 | `"            assert api_module._csp_hash_source(match.group(\"body\")) in policy"` | — |
| [SRC-3451CC474D-L001026](../../tests/test_api.py#L1026) | 1026 | `"        for match in re.finditer("` | — |
| [SRC-3451CC474D-L001027](../../tests/test_api.py#L1027) | 1027 | `"            r\"\"\"\\bstyle\\s*=\\s*([\"'])(.*?)\\1\"\"\","` | — |
| [SRC-3451CC474D-L001028](../../tests/test_api.py#L1028) | 1028 | `"            document,"` | — |
| [SRC-3451CC474D-L001029](../../tests/test_api.py#L1029) | 1029 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-3451CC474D-L001030](../../tests/test_api.py#L1030) | 1030 | `"        ):"` | — |
| [SRC-3451CC474D-L001031](../../tests/test_api.py#L1031) | 1031 | `"            style_attributes += 1"` | — |
| [SRC-3451CC474D-L001032](../../tests/test_api.py#L1032) | 1032 | `"            assert api_module._csp_hash_source(match.group(2).strip()) in policy"` | — |
| [SRC-3451CC474D-L001033](../../tests/test_api.py#L1033) | 1033 | `"    assert script_blocks >= 2"` | — |
| [SRC-3451CC474D-L001034](../../tests/test_api.py#L1034) | 1034 | `"    assert style_blocks >= 2"` | — |
| [SRC-3451CC474D-L001035](../../tests/test_api.py#L1035) | 1035 | `"    assert style_attributes >= 10"` | — |
| [SRC-3451CC474D-L001036](../../tests/test_api.py#L1036) | 1036 | `""` | — |
| [SRC-3451CC474D-L001037](../../tests/test_api.py#L1037) | 1037 | `""` | — |
| [SRC-3451CC474D-L001038](../../tests/test_api.py#L1038) | 1038 | `"def test_dashboard_uses_delegated_status_action_not_inline_onclick():"` | — |
| [SRC-3451CC474D-L001039](../../tests/test_api.py#L1039) | 1039 | `"    dashboard = (Path(__file__).resolve().parents[1] / \"web\" / \"dashboard.html\").read_text("` | — |
| [SRC-3451CC474D-L001040](../../tests/test_api.py#L1040) | 1040 | `"        encoding=\"utf-8\""` | — |
| [SRC-3451CC474D-L001041](../../tests/test_api.py#L1041) | 1041 | `"    )"` | — |
| [SRC-3451CC474D-L001042](../../tests/test_api.py#L1042) | 1042 | `"    assert 'data-action=\"save-status\"' in dashboard"` | — |
| [SRC-3451CC474D-L001043](../../tests/test_api.py#L1043) | 1043 | `"    assert 'onclick=\"saveStatus' not in dashboard"` | — |
| [SRC-3451CC474D-L001044](../../tests/test_api.py#L1044) | 1044 | `"    assert \"\"\"data-lead-id=\"'+esc(l.id)+'\">\"\"\" in dashboard"` | — |
| [SRC-3451CC474D-L001045](../../tests/test_api.py#L1045) | 1045 | `""` | — |
| [SRC-3451CC474D-L001046](../../tests/test_api.py#L1046) | 1046 | `"def test_browser_session_uses_http_only_cookie_and_rejects_cross_site_posts(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L001047](../../tests/test_api.py#L1047) | 1047 | `"    from urllib.parse import urlsplit"` | — |
| [SRC-3451CC474D-L001048](../../tests/test_api.py#L1048) | 1048 | `""` | — |
| [SRC-3451CC474D-L001049](../../tests/test_api.py#L1049) | 1049 | `"    token = \"browser-session-test-token-1234567890\""` | — |
| [SRC-3451CC474D-L001050](../../tests/test_api.py#L1050) | 1050 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L001051](../../tests/test_api.py#L1051) | 1051 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", token)"` | — |
| [SRC-3451CC474D-L001052](../../tests/test_api.py#L1052) | 1052 | `"    origin = \"https://\" + urlsplit(local_api).netloc"` | — |
| [SRC-3451CC474D-L001053](../../tests/test_api.py#L1053) | 1053 | `""` | — |
| [SRC-3451CC474D-L001054](../../tests/test_api.py#L1054) | 1054 | `"    status, payload, headers = request_json_with_headers("` | — |
| [SRC-3451CC474D-L001055](../../tests/test_api.py#L1055) | 1055 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001056](../../tests/test_api.py#L1056) | 1056 | `"        \"/api/session\","` | — |
| [SRC-3451CC474D-L001057](../../tests/test_api.py#L1057) | 1057 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001058](../../tests/test_api.py#L1058) | 1058 | `"        payload={\"access_token\": token},"` | — |
| [SRC-3451CC474D-L001059](../../tests/test_api.py#L1059) | 1059 | `"        headers={\"Origin\": origin},"` | — |
| [SRC-3451CC474D-L001060](../../tests/test_api.py#L1060) | 1060 | `"    )"` | — |
| [SRC-3451CC474D-L001061](../../tests/test_api.py#L1061) | 1061 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L001062](../../tests/test_api.py#L1062) | 1062 | `"    assert payload == {\"authenticated\": True, \"role\": \"owner\"}"` | — |
| [SRC-3451CC474D-L001063](../../tests/test_api.py#L1063) | 1063 | `"    assert token not in json.dumps(payload)"` | — |
| [SRC-3451CC474D-L001064](../../tests/test_api.py#L1064) | 1064 | `"    set_cookie = headers.get(\"Set-Cookie\", \"\")"` | — |
| [SRC-3451CC474D-L001065](../../tests/test_api.py#L1065) | 1065 | `"    assert set_cookie.startswith(\"__Host-omarai_session=\")"` | — |
| [SRC-3451CC474D-L001066](../../tests/test_api.py#L1066) | 1066 | `"    assert \"Path=/\" in set_cookie"` | — |
| [SRC-3451CC474D-L001067](../../tests/test_api.py#L1067) | 1067 | `"    assert \"Secure\" in set_cookie"` | — |
| [SRC-3451CC474D-L001068](../../tests/test_api.py#L1068) | 1068 | `"    assert \"HttpOnly\" in set_cookie"` | — |
| [SRC-3451CC474D-L001069](../../tests/test_api.py#L1069) | 1069 | `"    assert \"SameSite=Strict\" in set_cookie"` | — |
| [SRC-3451CC474D-L001070](../../tests/test_api.py#L1070) | 1070 | `"    assert \"Max-Age=28800\" in set_cookie"` | — |
| [SRC-3451CC474D-L001071](../../tests/test_api.py#L1071) | 1071 | `"    assert \"Domain=\" not in set_cookie"` | — |
| [SRC-3451CC474D-L001072](../../tests/test_api.py#L1072) | 1072 | `"    cookie = set_cookie.split(\";\", 1)[0]"` | — |
| [SRC-3451CC474D-L001073](../../tests/test_api.py#L1073) | 1073 | `"    assert token not in cookie"` | — |
| [SRC-3451CC474D-L001074](../../tests/test_api.py#L1074) | 1074 | `"    assert len(cookie.split(\"=\", 1)[1]) >= 32"` | — |
| [SRC-3451CC474D-L001075](../../tests/test_api.py#L1075) | 1075 | `""` | — |
| [SRC-3451CC474D-L001076](../../tests/test_api.py#L1076) | 1076 | `"    status, session = request_json("` | — |
| [SRC-3451CC474D-L001077](../../tests/test_api.py#L1077) | 1077 | `"        local_api, \"/api/session\", headers={\"Cookie\": cookie}"` | — |
| [SRC-3451CC474D-L001078](../../tests/test_api.py#L1078) | 1078 | `"    )"` | — |
| [SRC-3451CC474D-L001079](../../tests/test_api.py#L1079) | 1079 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L001080](../../tests/test_api.py#L1080) | 1080 | `"    assert session == {\"authenticated\": True, \"role\": \"owner\"}"` | — |
| [SRC-3451CC474D-L001081](../../tests/test_api.py#L1081) | 1081 | `""` | — |
| [SRC-3451CC474D-L001082](../../tests/test_api.py#L1082) | 1082 | `"    status, listing = request_json("` | — |
| [SRC-3451CC474D-L001083](../../tests/test_api.py#L1083) | 1083 | `"        local_api, \"/api/leads\", headers={\"Cookie\": cookie}"` | — |
| [SRC-3451CC474D-L001084](../../tests/test_api.py#L1084) | 1084 | `"    )"` | — |
| [SRC-3451CC474D-L001085](../../tests/test_api.py#L1085) | 1085 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L001086](../../tests/test_api.py#L1086) | 1086 | `"    assert listing[\"count\"] == 0"` | — |
| [SRC-3451CC474D-L001087](../../tests/test_api.py#L1087) | 1087 | `""` | — |
| [SRC-3451CC474D-L001088](../../tests/test_api.py#L1088) | 1088 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L001089](../../tests/test_api.py#L1089) | 1089 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001090](../../tests/test_api.py#L1090) | 1090 | `"        \"/api/ask\","` | — |
| [SRC-3451CC474D-L001091](../../tests/test_api.py#L1091) | 1091 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001092](../../tests/test_api.py#L1092) | 1092 | `"        payload={\"question\": \"كم عميل؟\"},"` | — |
| [SRC-3451CC474D-L001093](../../tests/test_api.py#L1093) | 1093 | `"        headers={\"Cookie\": cookie, \"Origin\": \"https://attacker.example\"},"` | — |
| [SRC-3451CC474D-L001094](../../tests/test_api.py#L1094) | 1094 | `"    )"` | — |
| [SRC-3451CC474D-L001095](../../tests/test_api.py#L1095) | 1095 | `"    assert status == 403"` | — |
| [SRC-3451CC474D-L001096](../../tests/test_api.py#L1096) | 1096 | `"    assert \"Origin\" in error[\"error\"] or \"cross-origin\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L001097](../../tests/test_api.py#L1097) | 1097 | `""` | — |
| [SRC-3451CC474D-L001098](../../tests/test_api.py#L1098) | 1098 | `"    status, logged_out, logout_headers = request_json_with_headers("` | — |
| [SRC-3451CC474D-L001099](../../tests/test_api.py#L1099) | 1099 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001100](../../tests/test_api.py#L1100) | 1100 | `"        \"/api/session/logout\","` | — |
| [SRC-3451CC474D-L001101](../../tests/test_api.py#L1101) | 1101 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001102](../../tests/test_api.py#L1102) | 1102 | `"        payload={},"` | — |
| [SRC-3451CC474D-L001103](../../tests/test_api.py#L1103) | 1103 | `"        headers={\"Cookie\": cookie, \"Origin\": origin},"` | — |
| [SRC-3451CC474D-L001104](../../tests/test_api.py#L1104) | 1104 | `"    )"` | — |
| [SRC-3451CC474D-L001105](../../tests/test_api.py#L1105) | 1105 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L001106](../../tests/test_api.py#L1106) | 1106 | `"    assert logged_out[\"logged_out\"] is True"` | — |
| [SRC-3451CC474D-L001107](../../tests/test_api.py#L1107) | 1107 | `"    cleared_cookie = logout_headers.get(\"Set-Cookie\", \"\")"` | — |
| [SRC-3451CC474D-L001108](../../tests/test_api.py#L1108) | 1108 | `"    assert cleared_cookie.startswith(\"__Host-omarai_session=\")"` | — |
| [SRC-3451CC474D-L001109](../../tests/test_api.py#L1109) | 1109 | `"    assert \"Max-Age=0\" in cleared_cookie"` | — |
| [SRC-3451CC474D-L001110](../../tests/test_api.py#L1110) | 1110 | `""` | — |
| [SRC-3451CC474D-L001111](../../tests/test_api.py#L1111) | 1111 | `"    status, error = request_json(local_api, \"/api/leads\")"` | — |
| [SRC-3451CC474D-L001112](../../tests/test_api.py#L1112) | 1112 | `"    assert status == 401"` | — |
| [SRC-3451CC474D-L001113](../../tests/test_api.py#L1113) | 1113 | `""` | — |
| [SRC-3451CC474D-L001114](../../tests/test_api.py#L1114) | 1114 | `""` | — |
| [SRC-3451CC474D-L001115](../../tests/test_api.py#L1115) | 1115 | `"def test_browser_session_login_rejects_untrusted_origin(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L001116](../../tests/test_api.py#L1116) | 1116 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L001117](../../tests/test_api.py#L1117) | 1117 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", \"browser-session-test-token-1234567890\")"` | — |
| [SRC-3451CC474D-L001118](../../tests/test_api.py#L1118) | 1118 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L001119](../../tests/test_api.py#L1119) | 1119 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001120](../../tests/test_api.py#L1120) | 1120 | `"        \"/api/session\","` | — |
| [SRC-3451CC474D-L001121](../../tests/test_api.py#L1121) | 1121 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001122](../../tests/test_api.py#L1122) | 1122 | `"        payload={\"access_token\": \"browser-session-test-token-1234567890\"},"` | — |
| [SRC-3451CC474D-L001123](../../tests/test_api.py#L1123) | 1123 | `"        headers={\"Origin\": \"https://attacker.example\"},"` | — |
| [SRC-3451CC474D-L001124](../../tests/test_api.py#L1124) | 1124 | `"    )"` | — |
| [SRC-3451CC474D-L001125](../../tests/test_api.py#L1125) | 1125 | `"    assert status == 403"` | — |
| [SRC-3451CC474D-L001126](../../tests/test_api.py#L1126) | 1126 | `"    assert \"same-origin\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L001127](../../tests/test_api.py#L1127) | 1127 | `""` | — |
| [SRC-3451CC474D-L001128](../../tests/test_api.py#L1128) | 1128 | `""` | — |
| [SRC-3451CC474D-L001129](../../tests/test_api.py#L1129) | 1129 | `"def test_browser_session_does_not_accept_unsafe_cookie_token_format(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L001130](../../tests/test_api.py#L1130) | 1130 | `"    from urllib.parse import urlsplit"` | — |
| [SRC-3451CC474D-L001131](../../tests/test_api.py#L1131) | 1131 | `""` | — |
| [SRC-3451CC474D-L001132](../../tests/test_api.py#L1132) | 1132 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L001133](../../tests/test_api.py#L1133) | 1133 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", \"browser-session-test-token-1234567890\")"` | — |
| [SRC-3451CC474D-L001134](../../tests/test_api.py#L1134) | 1134 | `"    status, _error = request_json("` | — |
| [SRC-3451CC474D-L001135](../../tests/test_api.py#L1135) | 1135 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001136](../../tests/test_api.py#L1136) | 1136 | `"        \"/api/session\","` | — |
| [SRC-3451CC474D-L001137](../../tests/test_api.py#L1137) | 1137 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001138](../../tests/test_api.py#L1138) | 1138 | `"        payload={\"access_token\": \"unsafe;token\" + \"x\" * 40},"` | — |
| [SRC-3451CC474D-L001139](../../tests/test_api.py#L1139) | 1139 | `"        headers={\"Origin\": \"https://\" + urlsplit(local_api).netloc},"` | — |
| [SRC-3451CC474D-L001140](../../tests/test_api.py#L1140) | 1140 | `"    )"` | — |
| [SRC-3451CC474D-L001141](../../tests/test_api.py#L1141) | 1141 | `"    assert status == 401"` | — |
| [SRC-3451CC474D-L001142](../../tests/test_api.py#L1142) | 1142 | `""` | — |
| [SRC-3451CC474D-L001143](../../tests/test_api.py#L1143) | 1143 | `"def test_expired_browser_session_can_logout_and_clear_cookie(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L001144](../../tests/test_api.py#L1144) | 1144 | `"    from urllib.parse import urlsplit"` | — |
| [SRC-3451CC474D-L001145](../../tests/test_api.py#L1145) | 1145 | `"    from api.omarai import Handler"` | — |
| [SRC-3451CC474D-L001146](../../tests/test_api.py#L1146) | 1146 | `""` | — |
| [SRC-3451CC474D-L001147](../../tests/test_api.py#L1147) | 1147 | `"    token = \"expired-browser-session-token-123456\""` | — |
| [SRC-3451CC474D-L001148](../../tests/test_api.py#L1148) | 1148 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L001149](../../tests/test_api.py#L1149) | 1149 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", token)"` | — |
| [SRC-3451CC474D-L001150](../../tests/test_api.py#L1150) | 1150 | `"    origin = \"https://\" + urlsplit(local_api).netloc"` | — |
| [SRC-3451CC474D-L001151](../../tests/test_api.py#L1151) | 1151 | `""` | — |
| [SRC-3451CC474D-L001152](../../tests/test_api.py#L1152) | 1152 | `"    status, _payload, headers = request_json_with_headers("` | — |
| [SRC-3451CC474D-L001153](../../tests/test_api.py#L1153) | 1153 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001154](../../tests/test_api.py#L1154) | 1154 | `"        \"/api/session\","` | — |
| [SRC-3451CC474D-L001155](../../tests/test_api.py#L1155) | 1155 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001156](../../tests/test_api.py#L1156) | 1156 | `"        payload={\"access_token\": token},"` | — |
| [SRC-3451CC474D-L001157](../../tests/test_api.py#L1157) | 1157 | `"        headers={\"Origin\": origin},"` | — |
| [SRC-3451CC474D-L001158](../../tests/test_api.py#L1158) | 1158 | `"    )"` | — |
| [SRC-3451CC474D-L001159](../../tests/test_api.py#L1159) | 1159 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L001160](../../tests/test_api.py#L1160) | 1160 | `"    cookie = headers.get(\"Set-Cookie\", \"\").split(\";\", 1)[0]"` | — |
| [SRC-3451CC474D-L001161](../../tests/test_api.py#L1161) | 1161 | `"    session_id = cookie.split(\"=\", 1)[1]"` | — |
| [SRC-3451CC474D-L001162](../../tests/test_api.py#L1162) | 1162 | `""` | — |
| [SRC-3451CC474D-L001163](../../tests/test_api.py#L1163) | 1163 | `"    with Handler.store.connect() as db:"` | — |
| [SRC-3451CC474D-L001164](../../tests/test_api.py#L1164) | 1164 | `"        db.execute("` | — |
| [SRC-3451CC474D-L001165](../../tests/test_api.py#L1165) | 1165 | `"            \"UPDATE web_sessions SET expires_at=? WHERE session_hash=?\","` | — |
| [SRC-3451CC474D-L001166](../../tests/test_api.py#L1166) | 1166 | `"            (\"2000-01-01T00:00:00Z\", Handler.store._token_hash(session_id)),"` | — |
| [SRC-3451CC474D-L001167](../../tests/test_api.py#L1167) | 1167 | `"        )"` | — |
| [SRC-3451CC474D-L001168](../../tests/test_api.py#L1168) | 1168 | `""` | — |
| [SRC-3451CC474D-L001169](../../tests/test_api.py#L1169) | 1169 | `"    status, payload, logout_headers = request_json_with_headers("` | — |
| [SRC-3451CC474D-L001170](../../tests/test_api.py#L1170) | 1170 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001171](../../tests/test_api.py#L1171) | 1171 | `"        \"/api/session/logout\","` | — |
| [SRC-3451CC474D-L001172](../../tests/test_api.py#L1172) | 1172 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001173](../../tests/test_api.py#L1173) | 1173 | `"        payload={},"` | — |
| [SRC-3451CC474D-L001174](../../tests/test_api.py#L1174) | 1174 | `"        headers={\"Cookie\": cookie, \"Origin\": origin},"` | — |
| [SRC-3451CC474D-L001175](../../tests/test_api.py#L1175) | 1175 | `"    )"` | — |
| [SRC-3451CC474D-L001176](../../tests/test_api.py#L1176) | 1176 | `""` | — |
| [SRC-3451CC474D-L001177](../../tests/test_api.py#L1177) | 1177 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L001178](../../tests/test_api.py#L1178) | 1178 | `"    assert payload == {\"logged_out\": True}"` | — |
| [SRC-3451CC474D-L001179](../../tests/test_api.py#L1179) | 1179 | `"    cleared_cookie = logout_headers.get(\"Set-Cookie\", \"\")"` | — |
| [SRC-3451CC474D-L001180](../../tests/test_api.py#L1180) | 1180 | `"    assert cleared_cookie.startswith(\"__Host-omarai_session=\")"` | — |
| [SRC-3451CC474D-L001181](../../tests/test_api.py#L1181) | 1181 | `"    assert \"Max-Age=0\" in cleared_cookie"` | — |
| [SRC-3451CC474D-L001182](../../tests/test_api.py#L1182) | 1182 | `""` | — |
| [SRC-3451CC474D-L001183](../../tests/test_api.py#L1183) | 1183 | `"    status, _error = request_json("` | — |
| [SRC-3451CC474D-L001184](../../tests/test_api.py#L1184) | 1184 | `"        local_api, \"/api/session\", headers={\"Cookie\": cookie}"` | — |
| [SRC-3451CC474D-L001185](../../tests/test_api.py#L1185) | 1185 | `"    )"` | — |
| [SRC-3451CC474D-L001186](../../tests/test_api.py#L1186) | 1186 | `"    assert status == 401"` | — |
| [SRC-3451CC474D-L001187](../../tests/test_api.py#L1187) | 1187 | `""` | — |
| [SRC-3451CC474D-L001188](../../tests/test_api.py#L1188) | 1188 | `"def test_browser_session_logout_rejects_untrusted_origin_even_without_valid_cookie("` | — |
| [SRC-3451CC474D-L001189](../../tests/test_api.py#L1189) | 1189 | `"    local_api, monkeypatch"` | — |
| [SRC-3451CC474D-L001190](../../tests/test_api.py#L1190) | 1190 | `"):"` | — |
| [SRC-3451CC474D-L001191](../../tests/test_api.py#L1191) | 1191 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L001192](../../tests/test_api.py#L1192) | 1192 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L001193](../../tests/test_api.py#L1193) | 1193 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001194](../../tests/test_api.py#L1194) | 1194 | `"        \"/api/session/logout\","` | — |
| [SRC-3451CC474D-L001195](../../tests/test_api.py#L1195) | 1195 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001196](../../tests/test_api.py#L1196) | 1196 | `"        payload={},"` | — |
| [SRC-3451CC474D-L001197](../../tests/test_api.py#L1197) | 1197 | `"        headers={\"Origin\": \"https://attacker.example\"},"` | — |
| [SRC-3451CC474D-L001198](../../tests/test_api.py#L1198) | 1198 | `"    )"` | — |
| [SRC-3451CC474D-L001199](../../tests/test_api.py#L1199) | 1199 | `"    assert status == 403"` | — |
| [SRC-3451CC474D-L001200](../../tests/test_api.py#L1200) | 1200 | `"    assert \"same-origin\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L001201](../../tests/test_api.py#L1201) | 1201 | `""` | — |
| [SRC-3451CC474D-L001202](../../tests/test_api.py#L1202) | 1202 | `"@pytest.mark.parametrize("` | — |
| [SRC-3451CC474D-L001203](../../tests/test_api.py#L1203) | 1203 | `"    (\"request_line\", \"framing_headers\", \"body\", \"error_marker\"),"` | — |
| [SRC-3451CC474D-L001204](../../tests/test_api.py#L1204) | 1204 | `"    ["` | — |
| [SRC-3451CC474D-L001205](../../tests/test_api.py#L1205) | 1205 | `"        ("` | — |
| [SRC-3451CC474D-L001206](../../tests/test_api.py#L1206) | 1206 | `"            \"POST /api/analyze HTTP/1.1\","` | — |
| [SRC-3451CC474D-L001207](../../tests/test_api.py#L1207) | 1207 | `"            b\"Transfer-Encoding: chunked\\r\\nContent-Length: 4\\r\\n\","` | — |
| [SRC-3451CC474D-L001208](../../tests/test_api.py#L1208) | 1208 | `"            b\"0\\r\\n\\r\\n\","` | — |
| [SRC-3451CC474D-L001209](../../tests/test_api.py#L1209) | 1209 | `"            b\"Transfer-Encoding\","` | — |
| [SRC-3451CC474D-L001210](../../tests/test_api.py#L1210) | 1210 | `"        ),"` | — |
| [SRC-3451CC474D-L001211](../../tests/test_api.py#L1211) | 1211 | `"        ("` | — |
| [SRC-3451CC474D-L001212](../../tests/test_api.py#L1212) | 1212 | `"            \"POST /api/analyze HTTP/1.1\","` | — |
| [SRC-3451CC474D-L001213](../../tests/test_api.py#L1213) | 1213 | `"            b\"Content-Length: 4\\r\\nContent-Length: 5\\r\\n\","` | — |
| [SRC-3451CC474D-L001214](../../tests/test_api.py#L1214) | 1214 | `"            b\"test\","` | — |
| [SRC-3451CC474D-L001215](../../tests/test_api.py#L1215) | 1215 | `"            b\"Content-Length\","` | — |
| [SRC-3451CC474D-L001216](../../tests/test_api.py#L1216) | 1216 | `"        ),"` | — |
| [SRC-3451CC474D-L001217](../../tests/test_api.py#L1217) | 1217 | `"        ("` | — |
| [SRC-3451CC474D-L001218](../../tests/test_api.py#L1218) | 1218 | `"            \"GET /api/health HTTP/1.1\","` | — |
| [SRC-3451CC474D-L001219](../../tests/test_api.py#L1219) | 1219 | `"            b\"Content-Length: 4\\r\\n\","` | — |
| [SRC-3451CC474D-L001220](../../tests/test_api.py#L1220) | 1220 | `"            b\"test\","` | — |
| [SRC-3451CC474D-L001221](../../tests/test_api.py#L1221) | 1221 | `"            b\"Content-Length\","` | — |
| [SRC-3451CC474D-L001222](../../tests/test_api.py#L1222) | 1222 | `"        ),"` | — |
| [SRC-3451CC474D-L001223](../../tests/test_api.py#L1223) | 1223 | `"    ],"` | — |
| [SRC-3451CC474D-L001224](../../tests/test_api.py#L1224) | 1224 | `")"` | — |
| [SRC-3451CC474D-L001225](../../tests/test_api.py#L1225) | 1225 | `"def test_api_rejects_ambiguous_or_unsupported_http_request_framing("` | — |
| [SRC-3451CC474D-L001226](../../tests/test_api.py#L1226) | 1226 | `"    local_api, request_line, framing_headers, body, error_marker"` | — |
| [SRC-3451CC474D-L001227](../../tests/test_api.py#L1227) | 1227 | `"):"` | — |
| [SRC-3451CC474D-L001228](../../tests/test_api.py#L1228) | 1228 | `"    host_port = local_api.rsplit(\":\", 1)"` | — |
| [SRC-3451CC474D-L001229](../../tests/test_api.py#L1229) | 1229 | `"    with socket.create_connection("` | — |
| [SRC-3451CC474D-L001230](../../tests/test_api.py#L1230) | 1230 | `"        (host_port[0].removeprefix(\"http://\"), int(host_port[1])), timeout=2"` | — |
| [SRC-3451CC474D-L001231](../../tests/test_api.py#L1231) | 1231 | `"    ) as client:"` | — |
| [SRC-3451CC474D-L001232](../../tests/test_api.py#L1232) | 1232 | `"        client.settimeout(2)"` | — |
| [SRC-3451CC474D-L001233](../../tests/test_api.py#L1233) | 1233 | `"        request = ("` | — |
| [SRC-3451CC474D-L001234](../../tests/test_api.py#L1234) | 1234 | `"            request_line.encode(\"ascii\")"` | — |
| [SRC-3451CC474D-L001235](../../tests/test_api.py#L1235) | 1235 | `"            + b\"\\r\\nHost: localhost\\r\\n\""` | — |
| [SRC-3451CC474D-L001236](../../tests/test_api.py#L1236) | 1236 | `"            + b\"Content-Type: application/json\\r\\n\""` | — |
| [SRC-3451CC474D-L001237](../../tests/test_api.py#L1237) | 1237 | `"            + framing_headers"` | — |
| [SRC-3451CC474D-L001238](../../tests/test_api.py#L1238) | 1238 | `"            + b\"Connection: close\\r\\n\\r\\n\""` | — |
| [SRC-3451CC474D-L001239](../../tests/test_api.py#L1239) | 1239 | `"            + body"` | — |
| [SRC-3451CC474D-L001240](../../tests/test_api.py#L1240) | 1240 | `"        )"` | — |
| [SRC-3451CC474D-L001241](../../tests/test_api.py#L1241) | 1241 | `"        client.sendall(request)"` | — |
| [SRC-3451CC474D-L001242](../../tests/test_api.py#L1242) | 1242 | `"        response = b\"\""` | — |
| [SRC-3451CC474D-L001243](../../tests/test_api.py#L1243) | 1243 | `"        while True:"` | — |
| [SRC-3451CC474D-L001244](../../tests/test_api.py#L1244) | 1244 | `"            chunk = client.recv(4096)"` | — |
| [SRC-3451CC474D-L001245](../../tests/test_api.py#L1245) | 1245 | `"            if not chunk:"` | — |
| [SRC-3451CC474D-L001246](../../tests/test_api.py#L1246) | 1246 | `"                break"` | — |
| [SRC-3451CC474D-L001247](../../tests/test_api.py#L1247) | 1247 | `"            response += chunk"` | — |
| [SRC-3451CC474D-L001248](../../tests/test_api.py#L1248) | 1248 | `""` | — |
| [SRC-3451CC474D-L001249](../../tests/test_api.py#L1249) | 1249 | `"    assert response.startswith(b\"HTTP/1.0 400\")"` | — |
| [SRC-3451CC474D-L001250](../../tests/test_api.py#L1250) | 1250 | `"    assert error_marker in response"` | — |
| [SRC-3451CC474D-L001251](../../tests/test_api.py#L1251) | 1251 | `"    assert b\"200 OK\" not in response"` | — |
| [SRC-3451CC474D-L001252](../../tests/test_api.py#L1252) | 1252 | `""` | — |
| [SRC-3451CC474D-L001253](../../tests/test_api.py#L1253) | 1253 | `"def test_api_closes_connection_when_declared_body_exceeds_limit(local_api):"` | — |
| [SRC-3451CC474D-L001254](../../tests/test_api.py#L1254) | 1254 | `"    host_port = local_api.rsplit(\":\", 1)"` | — |
| [SRC-3451CC474D-L001255](../../tests/test_api.py#L1255) | 1255 | `"    with socket.create_connection("` | — |
| [SRC-3451CC474D-L001256](../../tests/test_api.py#L1256) | 1256 | `"        (host_port[0].removeprefix(\"http://\"), int(host_port[1])), timeout=2"` | — |
| [SRC-3451CC474D-L001257](../../tests/test_api.py#L1257) | 1257 | `"    ) as client:"` | — |
| [SRC-3451CC474D-L001258](../../tests/test_api.py#L1258) | 1258 | `"        client.settimeout(2)"` | — |
| [SRC-3451CC474D-L001259](../../tests/test_api.py#L1259) | 1259 | `"        client.sendall("` | — |
| [SRC-3451CC474D-L001260](../../tests/test_api.py#L1260) | 1260 | `"            b\"POST /api/analyze HTTP/1.1\\r\\n\""` | — |
| [SRC-3451CC474D-L001261](../../tests/test_api.py#L1261) | 1261 | `"            b\"Host: localhost\\r\\n\""` | — |
| [SRC-3451CC474D-L001262](../../tests/test_api.py#L1262) | 1262 | `"            b\"Content-Type: application/json\\r\\n\""` | — |
| [SRC-3451CC474D-L001263](../../tests/test_api.py#L1263) | 1263 | `"            b\"Content-Length: 200001\\r\\n\""` | — |
| [SRC-3451CC474D-L001264](../../tests/test_api.py#L1264) | 1264 | `"            b\"\\r\\n\""` | — |
| [SRC-3451CC474D-L001265](../../tests/test_api.py#L1265) | 1265 | `"        )"` | — |
| [SRC-3451CC474D-L001266](../../tests/test_api.py#L1266) | 1266 | `"        response = b\"\""` | — |
| [SRC-3451CC474D-L001267](../../tests/test_api.py#L1267) | 1267 | `"        while True:"` | — |
| [SRC-3451CC474D-L001268](../../tests/test_api.py#L1268) | 1268 | `"            chunk = client.recv(4096)"` | — |
| [SRC-3451CC474D-L001269](../../tests/test_api.py#L1269) | 1269 | `"            if not chunk:"` | — |
| [SRC-3451CC474D-L001270](../../tests/test_api.py#L1270) | 1270 | `"                break"` | — |
| [SRC-3451CC474D-L001271](../../tests/test_api.py#L1271) | 1271 | `"            response += chunk"` | — |
| [SRC-3451CC474D-L001272](../../tests/test_api.py#L1272) | 1272 | `""` | — |
| [SRC-3451CC474D-L001273](../../tests/test_api.py#L1273) | 1273 | `"    assert response.startswith(b\"HTTP/1.0 413\")"` | — |
| [SRC-3451CC474D-L001274](../../tests/test_api.py#L1274) | 1274 | `"    assert b\"request too large\" in response"` | — |
| [SRC-3451CC474D-L001275](../../tests/test_api.py#L1275) | 1275 | `""` | — |
| [SRC-3451CC474D-L001276](../../tests/test_api.py#L1276) | 1276 | `""` | — |
| [SRC-3451CC474D-L001277](../../tests/test_api.py#L1277) | 1277 | `""` | — |
| [SRC-3451CC474D-L001278](../../tests/test_api.py#L1278) | 1278 | `"def test_workspace_route_serves_the_arabic_rtl_workspace_shell(local_api):"` | — |
| [SRC-3451CC474D-L001279](../../tests/test_api.py#L1279) | 1279 | `"    with urlopen(local_api + \"/workspace\", timeout=3) as response:"` | — |
| [SRC-3451CC474D-L001280](../../tests/test_api.py#L1280) | 1280 | `"        html = response.read().decode(\"utf-8\")"` | — |
| [SRC-3451CC474D-L001281](../../tests/test_api.py#L1281) | 1281 | `"        assert response.status == 200"` | — |
| [SRC-3451CC474D-L001282](../../tests/test_api.py#L1282) | 1282 | `"        assert response.headers.get_content_type() == \"text/html\""` | — |
| [SRC-3451CC474D-L001283](../../tests/test_api.py#L1283) | 1283 | `""` | — |
| [SRC-3451CC474D-L001284](../../tests/test_api.py#L1284) | 1284 | `"    assert '<html lang=\"ar\" dir=\"rtl\">' in html"` | — |
| [SRC-3451CC474D-L001285](../../tests/test_api.py#L1285) | 1285 | `"    assert 'api(\"/api/session\")' in html"` | — |
| [SRC-3451CC474D-L001286](../../tests/test_api.py#L1286) | 1286 | `"    assert 'api(\"/api/leads?limit=500\")' in html"` | — |
| [SRC-3451CC474D-L001287](../../tests/test_api.py#L1287) | 1287 | `"    assert \"localStorage\" not in html"` | — |
| [SRC-3451CC474D-L001288](../../tests/test_api.py#L1288) | 1288 | `"    assert \"sessionStorage\" not in html"` | — |
| [SRC-3451CC474D-L001289](../../tests/test_api.py#L1289) | 1289 | `""` | — |
| [SRC-3451CC474D-L001290](../../tests/test_api.py#L1290) | 1290 | `"def test_sales_workspace_is_default_home_and_preserves_agent_and_legacy_leads(local_api):"` | — |
| [SRC-3451CC474D-L001291](../../tests/test_api.py#L1291) | 1291 | `"    with urlopen(local_api + \"/\", timeout=3) as response:"` | — |
| [SRC-3451CC474D-L001292](../../tests/test_api.py#L1292) | 1292 | `"        home = response.read().decode(\"utf-8\")"` | — |
| [SRC-3451CC474D-L001293](../../tests/test_api.py#L1293) | 1293 | `"        assert response.status == 200"` | — |
| [SRC-3451CC474D-L001294](../../tests/test_api.py#L1294) | 1294 | `"        assert '<html lang=\"ar\" dir=\"rtl\">' in home"` | — |
| [SRC-3451CC474D-L001295](../../tests/test_api.py#L1295) | 1295 | `"        assert \"OMARAI SECURE WORKSPACE\" in home"` | — |
| [SRC-3451CC474D-L001296](../../tests/test_api.py#L1296) | 1296 | `""` | — |
| [SRC-3451CC474D-L001297](../../tests/test_api.py#L1297) | 1297 | `"    with urlopen(local_api + \"/workspace\", timeout=3) as response:"` | — |
| [SRC-3451CC474D-L001298](../../tests/test_api.py#L1298) | 1298 | `"        workspace = response.read().decode(\"utf-8\")"` | — |
| [SRC-3451CC474D-L001299](../../tests/test_api.py#L1299) | 1299 | `"        assert response.status == 200"` | — |
| [SRC-3451CC474D-L001300](../../tests/test_api.py#L1300) | 1300 | `"        assert workspace == home"` | — |
| [SRC-3451CC474D-L001301](../../tests/test_api.py#L1301) | 1301 | `""` | — |
| [SRC-3451CC474D-L001302](../../tests/test_api.py#L1302) | 1302 | `"    with urlopen(local_api + \"/agent\", timeout=3) as response:"` | — |
| [SRC-3451CC474D-L001303](../../tests/test_api.py#L1303) | 1303 | `"        agent = response.read().decode(\"utf-8\")"` | — |
| [SRC-3451CC474D-L001304](../../tests/test_api.py#L1304) | 1304 | `"        assert response.status == 200"` | — |
| [SRC-3451CC474D-L001305](../../tests/test_api.py#L1305) | 1305 | `"        assert agent != home"` | — |
| [SRC-3451CC474D-L001306](../../tests/test_api.py#L1306) | 1306 | `"        assert \"وكيل البحث الحي والتحليل متعدد المصادر\" in agent"` | — |
| [SRC-3451CC474D-L001307](../../tests/test_api.py#L1307) | 1307 | `""` | — |
| [SRC-3451CC474D-L001308](../../tests/test_api.py#L1308) | 1308 | `"    with urlopen(local_api + \"/leads\", timeout=3) as response:"` | — |
| [SRC-3451CC474D-L001309](../../tests/test_api.py#L1309) | 1309 | `"        leads = response.read().decode(\"utf-8\")"` | — |
| [SRC-3451CC474D-L001310](../../tests/test_api.py#L1310) | 1310 | `"        assert response.status == 200"` | — |
| [SRC-3451CC474D-L001311](../../tests/test_api.py#L1311) | 1311 | `"        assert \"مساعد اكتشاف العملاء\" in leads"` | — |
| [SRC-3451CC474D-L001312](../../tests/test_api.py#L1312) | 1312 | `""` | — |
| [SRC-3451CC474D-L001313](../../tests/test_api.py#L1313) | 1313 | `""` | — |
| [SRC-3451CC474D-L001314](../../tests/test_api.py#L1314) | 1314 | `"def test_product_profile_and_buyer_discovery_api_persist_evidence_and_save_only_qualified_sources("` | — |
| [SRC-3451CC474D-L001315](../../tests/test_api.py#L1315) | 1315 | `"    local_api, monkeypatch"` | — |
| [SRC-3451CC474D-L001316](../../tests/test_api.py#L1316) | 1316 | `"):"` | — |
| [SRC-3451CC474D-L001317](../../tests/test_api.py#L1317) | 1317 | `"    from api.omarai import WebAgent"` | — |
| [SRC-3451CC474D-L001318](../../tests/test_api.py#L1318) | 1318 | `""` | — |
| [SRC-3451CC474D-L001319](../../tests/test_api.py#L1319) | 1319 | `"    captured = {}"` | — |
| [SRC-3451CC474D-L001320](../../tests/test_api.py#L1320) | 1320 | `""` | — |
| [SRC-3451CC474D-L001321](../../tests/test_api.py#L1321) | 1321 | `"    def fake_answer("` | — |
| [SRC-3451CC474D-L001322](../../tests/test_api.py#L1322) | 1322 | `"        self, question, history=None, mode=\"auto\", *, budget_profile=\"default\", buyer_queries=None"` | — |
| [SRC-3451CC474D-L001323](../../tests/test_api.py#L1323) | 1323 | `"    ):"` | — |
| [SRC-3451CC474D-L001324](../../tests/test_api.py#L1324) | 1324 | `"        captured[\"question\"] = question"` | — |
| [SRC-3451CC474D-L001325](../../tests/test_api.py#L1325) | 1325 | `"        captured[\"buyer_queries\"] = buyer_queries"` | — |
| [SRC-3451CC474D-L001326](../../tests/test_api.py#L1326) | 1326 | `"        captured[\"allow_optional_providers\"] = self.allow_optional_providers"` | — |
| [SRC-3451CC474D-L001327](../../tests/test_api.py#L1327) | 1327 | `"        captured[\"openrouter_web_search_enabled\"] = self.openrouter_web_search_enabled"` | — |
| [SRC-3451CC474D-L001328](../../tests/test_api.py#L1328) | 1328 | `"        return {"` | — |
| [SRC-3451CC474D-L001329](../../tests/test_api.py#L1329) | 1329 | `"            \"answer\": \"عُثر على إشارة طلب واحدة.\","` | — |
| [SRC-3451CC474D-L001330](../../tests/test_api.py#L1330) | 1330 | `"            \"search_queries\": buyer_queries,"` | — |
| [SRC-3451CC474D-L001331](../../tests/test_api.py#L1331) | 1331 | `"            \"search_report\": {"` | — |
| [SRC-3451CC474D-L001332](../../tests/test_api.py#L1332) | 1332 | `"                \"lead_generation\": {"` | — |
| [SRC-3451CC474D-L001333](../../tests/test_api.py#L1333) | 1333 | `"                    \"status\": \"candidate_signals_found\","` | — |
| [SRC-3451CC474D-L001334](../../tests/test_api.py#L1334) | 1334 | `"                    \"candidate_signal_count\": 1,"` | — |
| [SRC-3451CC474D-L001335](../../tests/test_api.py#L1335) | 1335 | `"                    \"related_results_reviewed\": 2,"` | — |
| [SRC-3451CC474D-L001336](../../tests/test_api.py#L1336) | 1336 | `"                    \"qualification_rule\": \"public_demand_signal_phrase_by_type\","` | — |
| [SRC-3451CC474D-L001337](../../tests/test_api.py#L1337) | 1337 | `"                    \"identity_verified\": False,"` | — |
| [SRC-3451CC474D-L001338](../../tests/test_api.py#L1338) | 1338 | `"                },"` | — |
| [SRC-3451CC474D-L001339](../../tests/test_api.py#L1339) | 1339 | `"                \"pipeline_completion_status\": \"completed\","` | — |
| [SRC-3451CC474D-L001340](../../tests/test_api.py#L1340) | 1340 | `"            },"` | — |
| [SRC-3451CC474D-L001341](../../tests/test_api.py#L1341) | 1341 | `"            \"sources\": ["` | — |
| [SRC-3451CC474D-L001342](../../tests/test_api.py#L1342) | 1342 | `"                {"` | — |
| [SRC-3451CC474D-L001343](../../tests/test_api.py#L1343) | 1343 | `"                    \"title\": \"طلب توريد لوحة إنذار\","` | — |
| [SRC-3451CC474D-L001344](../../tests/test_api.py#L1344) | 1344 | `"                    \"url\": \"https://example.org/public-request/1\","` | — |
| [SRC-3451CC474D-L001345](../../tests/test_api.py#L1345) | 1345 | `"                    \"snippet\": \"نبحث عن مورد لتوريد لوحة إنذار حريق لمشروع في القاهرة.\","` | — |
| [SRC-3451CC474D-L001346](../../tests/test_api.py#L1346) | 1346 | `"                    \"platform\": \"web\","` | — |
| [SRC-3451CC474D-L001347](../../tests/test_api.py#L1347) | 1347 | `"                    \"published_at\": None,"` | — |
| [SRC-3451CC474D-L001348](../../tests/test_api.py#L1348) | 1348 | `"                    \"page_fetched\": False,"` | — |
| [SRC-3451CC474D-L001349](../../tests/test_api.py#L1349) | 1349 | `"                    \"lead_qualification\": \"public_demand_signal\","` | — |
| [SRC-3451CC474D-L001350](../../tests/test_api.py#L1350) | 1350 | `"                    \"lead_intent_evidence\": {"` | — |
| [SRC-3451CC474D-L001351](../../tests/test_api.py#L1351) | 1351 | `"                        \"phrase\": \"نبحث عن مورد\","` | — |
| [SRC-3451CC474D-L001352](../../tests/test_api.py#L1352) | 1352 | `"                        \"basis\": \"snippet\","` | — |
| [SRC-3451CC474D-L001353](../../tests/test_api.py#L1353) | 1353 | `"                        \"signal_type\": \"request_for_quotation\","` | — |
| [SRC-3451CC474D-L001354](../../tests/test_api.py#L1354) | 1354 | `"                        \"product_fit\": \"unassessed\","` | — |
| [SRC-3451CC474D-L001355](../../tests/test_api.py#L1355) | 1355 | `"                    },"` | — |
| [SRC-3451CC474D-L001356](../../tests/test_api.py#L1356) | 1356 | `"                },"` | — |
| [SRC-3451CC474D-L001357](../../tests/test_api.py#L1357) | 1357 | `"                {"` | — |
| [SRC-3451CC474D-L001358](../../tests/test_api.py#L1358) | 1358 | `"                    \"title\": \"كتالوج لوحة إنذار\","` | — |
| [SRC-3451CC474D-L001359](../../tests/test_api.py#L1359) | 1359 | `"                    \"url\": \"https://example.net/catalog\","` | — |
| [SRC-3451CC474D-L001360](../../tests/test_api.py#L1360) | 1360 | `"                    \"snippet\": \"كتالوج تعريفي بلوحات إنذار الحريق.\","` | — |
| [SRC-3451CC474D-L001361](../../tests/test_api.py#L1361) | 1361 | `"                    \"platform\": \"web\","` | — |
| [SRC-3451CC474D-L001362](../../tests/test_api.py#L1362) | 1362 | `"                    \"published_at\": None,"` | — |
| [SRC-3451CC474D-L001363](../../tests/test_api.py#L1363) | 1363 | `"                    \"page_fetched\": False,"` | — |
| [SRC-3451CC474D-L001364](../../tests/test_api.py#L1364) | 1364 | `"                    \"lead_qualification\": \"related_result_not_lead\","` | — |
| [SRC-3451CC474D-L001365](../../tests/test_api.py#L1365) | 1365 | `"                    \"lead_intent_evidence\": None,"` | — |
| [SRC-3451CC474D-L001366](../../tests/test_api.py#L1366) | 1366 | `"                },"` | — |
| [SRC-3451CC474D-L001367](../../tests/test_api.py#L1367) | 1367 | `"            ],"` | — |
| [SRC-3451CC474D-L001368](../../tests/test_api.py#L1368) | 1368 | `"        }"` | — |
| [SRC-3451CC474D-L001369](../../tests/test_api.py#L1369) | 1369 | `""` | — |
| [SRC-3451CC474D-L001370](../../tests/test_api.py#L1370) | 1370 | `"    monkeypatch.setenv(\"OMARAI_OPENROUTER_WEB_SEARCH\", \"1\")"` | — |
| [SRC-3451CC474D-L001371](../../tests/test_api.py#L1371) | 1371 | `"    monkeypatch.setattr(WebAgent, \"answer\", fake_answer)"` | — |
| [SRC-3451CC474D-L001372](../../tests/test_api.py#L1372) | 1372 | `"    profile_status, profile = request_json("` | — |
| [SRC-3451CC474D-L001373](../../tests/test_api.py#L1373) | 1373 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001374](../../tests/test_api.py#L1374) | 1374 | `"        \"/api/product-profiles\","` | — |
| [SRC-3451CC474D-L001375](../../tests/test_api.py#L1375) | 1375 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001376](../../tests/test_api.py#L1376) | 1376 | `"        payload={"` | — |
| [SRC-3451CC474D-L001377](../../tests/test_api.py#L1377) | 1377 | `"            \"product\": {"` | — |
| [SRC-3451CC474D-L001378](../../tests/test_api.py#L1378) | 1378 | `"                \"name\": \"لوحة إنذار الحريق\","` | — |
| [SRC-3451CC474D-L001379](../../tests/test_api.py#L1379) | 1379 | `"                \"aliases\": [\"FACP\"],"` | — |
| [SRC-3451CC474D-L001380](../../tests/test_api.py#L1380) | 1380 | `"                \"category_path\": [\"السلامة\", \"إنذار الحريق\"],"` | — |
| [SRC-3451CC474D-L001381](../../tests/test_api.py#L1381) | 1381 | `"                \"use_cases\": [\"حماية المباني\"],"` | — |
| [SRC-3451CC474D-L001382](../../tests/test_api.py#L1382) | 1382 | `"                \"problems_solved\": [\"اكتشاف الحريق مبكرًا\"],"` | — |
| [SRC-3451CC474D-L001383](../../tests/test_api.py#L1383) | 1383 | `"            },"` | — |
| [SRC-3451CC474D-L001384](../../tests/test_api.py#L1384) | 1384 | `"            \"market\": {"` | — |
| [SRC-3451CC474D-L001385](../../tests/test_api.py#L1385) | 1385 | `"                \"locations\": [\"القاهرة\", \"الجيزة\"],"` | — |
| [SRC-3451CC474D-L001386](../../tests/test_api.py#L1386) | 1386 | `"                \"industries\": [\"المقاولات\"],"` | — |
| [SRC-3451CC474D-L001387](../../tests/test_api.py#L1387) | 1387 | `"                \"customer_types\": [\"مقاولون\"],"` | — |
| [SRC-3451CC474D-L001388](../../tests/test_api.py#L1388) | 1388 | `"                \"decision_roles\": [\"مدير مشتريات\"],"` | — |
| [SRC-3451CC474D-L001389](../../tests/test_api.py#L1389) | 1389 | `"                \"exclusions\": [],"` | — |
| [SRC-3451CC474D-L001390](../../tests/test_api.py#L1390) | 1390 | `"            },"` | — |
| [SRC-3451CC474D-L001391](../../tests/test_api.py#L1391) | 1391 | `"            \"locale\": \"ar\","` | — |
| [SRC-3451CC474D-L001392](../../tests/test_api.py#L1392) | 1392 | `"        },"` | — |
| [SRC-3451CC474D-L001393](../../tests/test_api.py#L1393) | 1393 | `"    )"` | — |
| [SRC-3451CC474D-L001394](../../tests/test_api.py#L1394) | 1394 | `"    assert profile_status == 201"` | — |
| [SRC-3451CC474D-L001395](../../tests/test_api.py#L1395) | 1395 | `"    assert profile[\"profile\"][\"product\"][\"name\"] == \"لوحة إنذار الحريق\""` | — |
| [SRC-3451CC474D-L001396](../../tests/test_api.py#L1396) | 1396 | `""` | — |
| [SRC-3451CC474D-L001397](../../tests/test_api.py#L1397) | 1397 | `"    run_status, run = request_json("` | — |
| [SRC-3451CC474D-L001398](../../tests/test_api.py#L1398) | 1398 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001399](../../tests/test_api.py#L1399) | 1399 | `"        \"/api/discoveries\","` | — |
| [SRC-3451CC474D-L001400](../../tests/test_api.py#L1400) | 1400 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001401](../../tests/test_api.py#L1401) | 1401 | `"        payload={\"profile_id\": profile[\"id\"], \"allow_optional_providers\": False},"` | — |
| [SRC-3451CC474D-L001402](../../tests/test_api.py#L1402) | 1402 | `"    )"` | — |
| [SRC-3451CC474D-L001403](../../tests/test_api.py#L1403) | 1403 | `"    assert run_status == 201"` | — |
| [SRC-3451CC474D-L001404](../../tests/test_api.py#L1404) | 1404 | `"    assert run[\"sources\"][0][\"lead_qualification\"] == \"public_demand_signal\""` | — |
| [SRC-3451CC474D-L001405](../../tests/test_api.py#L1405) | 1405 | `"    assert run[\"sources\"][1][\"lead_qualification\"] == \"related_result_not_lead\""` | — |
| [SRC-3451CC474D-L001406](../../tests/test_api.py#L1406) | 1406 | `"    assert captured[\"buyer_queries\"]"` | — |
| [SRC-3451CC474D-L001407](../../tests/test_api.py#L1407) | 1407 | `"    assert all(\"القاهرة\" in query or \"الجيزة\" in query for query in captured[\"buyer_queries\"])"` | — |
| [SRC-3451CC474D-L001408](../../tests/test_api.py#L1408) | 1408 | `"    assert all(\"لوحة إنذار الحريق\" in query or \"FACP\" in query for query in captured[\"buyer_queries\"])"` | — |
| [SRC-3451CC474D-L001409](../../tests/test_api.py#L1409) | 1409 | `"    assert captured[\"allow_optional_providers\"] is False"` | — |
| [SRC-3451CC474D-L001410](../../tests/test_api.py#L1410) | 1410 | `"    assert captured[\"openrouter_web_search_enabled\"] is False"` | — |
| [SRC-3451CC474D-L001411](../../tests/test_api.py#L1411) | 1411 | `""` | — |
| [SRC-3451CC474D-L001412](../../tests/test_api.py#L1412) | 1412 | `"    history_status, history = request_json(local_api, \"/api/discoveries\")"` | — |
| [SRC-3451CC474D-L001413](../../tests/test_api.py#L1413) | 1413 | `"    assert history_status == 200"` | — |
| [SRC-3451CC474D-L001414](../../tests/test_api.py#L1414) | 1414 | `"    assert history[\"count\"] == 1"` | — |
| [SRC-3451CC474D-L001415](../../tests/test_api.py#L1415) | 1415 | `"    assert history[\"runs\"][0][\"id\"] == run[\"id\"]"` | — |
| [SRC-3451CC474D-L001416](../../tests/test_api.py#L1416) | 1416 | `""` | — |
| [SRC-3451CC474D-L001417](../../tests/test_api.py#L1417) | 1417 | `"    rejected_status, rejected = request_json("` | — |
| [SRC-3451CC474D-L001418](../../tests/test_api.py#L1418) | 1418 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001419](../../tests/test_api.py#L1419) | 1419 | `"        f\"/api/discoveries/{run['id']}/signals/1/save\","` | — |
| [SRC-3451CC474D-L001420](../../tests/test_api.py#L1420) | 1420 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001421](../../tests/test_api.py#L1421) | 1421 | `"        payload={},"` | — |
| [SRC-3451CC474D-L001422](../../tests/test_api.py#L1422) | 1422 | `"    )"` | — |
| [SRC-3451CC474D-L001423](../../tests/test_api.py#L1423) | 1423 | `"    assert rejected_status == 409"` | — |
| [SRC-3451CC474D-L001424](../../tests/test_api.py#L1424) | 1424 | `"    assert \"ليست إشارة طلب\" in rejected[\"error\"]"` | — |
| [SRC-3451CC474D-L001425](../../tests/test_api.py#L1425) | 1425 | `""` | — |
| [SRC-3451CC474D-L001426](../../tests/test_api.py#L1426) | 1426 | `"    saved_status, saved = request_json("` | — |
| [SRC-3451CC474D-L001427](../../tests/test_api.py#L1427) | 1427 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001428](../../tests/test_api.py#L1428) | 1428 | `"        f\"/api/discoveries/{run['id']}/signals/0/save\","` | — |
| [SRC-3451CC474D-L001429](../../tests/test_api.py#L1429) | 1429 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001430](../../tests/test_api.py#L1430) | 1430 | `"        payload={},"` | — |
| [SRC-3451CC474D-L001431](../../tests/test_api.py#L1431) | 1431 | `"    )"` | — |
| [SRC-3451CC474D-L001432](../../tests/test_api.py#L1432) | 1432 | `"    assert saved_status == 201"` | — |
| [SRC-3451CC474D-L001433](../../tests/test_api.py#L1433) | 1433 | `"    assert saved[\"lead\"][\"source_url\"] == \"https://example.org/public-request/1\""` | — |
| [SRC-3451CC474D-L001434](../../tests/test_api.py#L1434) | 1434 | `"    assert \"نبحث عن مورد\" in saved[\"lead\"][\"note\"]"` | — |
| [SRC-3451CC474D-L001435](../../tests/test_api.py#L1435) | 1435 | `""` | — |
| [SRC-3451CC474D-L001436](../../tests/test_api.py#L1436) | 1436 | `""` | — |
| [SRC-3451CC474D-L001437](../../tests/test_api.py#L1437) | 1437 | `"def test_discovery_api_denies_optional_provider_usage_to_non_owner(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L001438](../../tests/test_api.py#L1438) | 1438 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L001439](../../tests/test_api.py#L1439) | 1439 | `"    store = Handler.store"` | — |
| [SRC-3451CC474D-L001440](../../tests/test_api.py#L1440) | 1440 | `"    tenant = store.create_tenant(\"Sales Team\", \"sales-team\")"` | — |
| [SRC-3451CC474D-L001441](../../tests/test_api.py#L1441) | 1441 | `"    user = store.create_user(\"sales@example.invalid\", \"Sales Agent\")"` | — |
| [SRC-3451CC474D-L001442](../../tests/test_api.py#L1442) | 1442 | `"    store.add_membership(tenant, user, \"sales_agent\")"` | — |
| [SRC-3451CC474D-L001443](../../tests/test_api.py#L1443) | 1443 | `"    token = \"sales-agent-test-token-1234567890\""` | — |
| [SRC-3451CC474D-L001444](../../tests/test_api.py#L1444) | 1444 | `"    store.create_api_token(token, tenant, user, \"test\")"` | — |
| [SRC-3451CC474D-L001445](../../tests/test_api.py#L1445) | 1445 | `"    headers = {\"Authorization\": \"Bearer \" + token}"` | — |
| [SRC-3451CC474D-L001446](../../tests/test_api.py#L1446) | 1446 | `""` | — |
| [SRC-3451CC474D-L001447](../../tests/test_api.py#L1447) | 1447 | `"    profile_status, profile = request_json("` | — |
| [SRC-3451CC474D-L001448](../../tests/test_api.py#L1448) | 1448 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001449](../../tests/test_api.py#L1449) | 1449 | `"        \"/api/product-profiles\","` | — |
| [SRC-3451CC474D-L001450](../../tests/test_api.py#L1450) | 1450 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001451](../../tests/test_api.py#L1451) | 1451 | `"        payload={"` | — |
| [SRC-3451CC474D-L001452](../../tests/test_api.py#L1452) | 1452 | `"            \"product\": {\"name\": \"FACP\", \"aliases\": [\"لوحة إنذار\"], \"use_cases\": [], \"problems_solved\": []},"` | — |
| [SRC-3451CC474D-L001453](../../tests/test_api.py#L1453) | 1453 | `"            \"market\": {\"locations\": [\"Cairo\"], \"industries\": [], \"customer_types\": [], \"decision_roles\": [], \"exclusions\": []},"` | — |
| [SRC-3451CC474D-L001454](../../tests/test_api.py#L1454) | 1454 | `"            \"locale\": \"en\","` | — |
| [SRC-3451CC474D-L001455](../../tests/test_api.py#L1455) | 1455 | `"        },"` | — |
| [SRC-3451CC474D-L001456](../../tests/test_api.py#L1456) | 1456 | `"        headers=headers,"` | — |
| [SRC-3451CC474D-L001457](../../tests/test_api.py#L1457) | 1457 | `"    )"` | — |
| [SRC-3451CC474D-L001458](../../tests/test_api.py#L1458) | 1458 | `"    assert profile_status == 201"` | — |
| [SRC-3451CC474D-L001459](../../tests/test_api.py#L1459) | 1459 | `""` | — |
| [SRC-3451CC474D-L001460](../../tests/test_api.py#L1460) | 1460 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L001461](../../tests/test_api.py#L1461) | 1461 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001462](../../tests/test_api.py#L1462) | 1462 | `"        \"/api/discoveries\","` | — |
| [SRC-3451CC474D-L001463](../../tests/test_api.py#L1463) | 1463 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001464](../../tests/test_api.py#L1464) | 1464 | `"        payload={\"profile_id\": profile[\"id\"], \"allow_optional_providers\": True},"` | — |
| [SRC-3451CC474D-L001465](../../tests/test_api.py#L1465) | 1465 | `"        headers=headers,"` | — |
| [SRC-3451CC474D-L001466](../../tests/test_api.py#L1466) | 1466 | `"    )"` | — |
| [SRC-3451CC474D-L001467](../../tests/test_api.py#L1467) | 1467 | `"    assert status == 403"` | — |
| [SRC-3451CC474D-L001468](../../tests/test_api.py#L1468) | 1468 | `"    assert \"مالك مساحة العمل\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L001469](../../tests/test_api.py#L1469) | 1469 | `""` | — |
| [SRC-3451CC474D-L001470](../../tests/test_api.py#L1470) | 1470 | `""` | — |
| [SRC-3451CC474D-L001471](../../tests/test_api.py#L1471) | 1471 | `"@pytest.mark.parametrize("` | — |
| [SRC-3451CC474D-L001472](../../tests/test_api.py#L1472) | 1472 | `"    \"forwarding_header\","` | — |
| [SRC-3451CC474D-L001473](../../tests/test_api.py#L1473) | 1473 | `"    ["` | — |
| [SRC-3451CC474D-L001474](../../tests/test_api.py#L1474) | 1474 | `"        {\"X-Forwarded-For\": \"203.0.113.9\"},"` | — |
| [SRC-3451CC474D-L001475](../../tests/test_api.py#L1475) | 1475 | `"        {\"CF-Connecting-IP\": \"203.0.113.9\"},"` | — |
| [SRC-3451CC474D-L001476](../../tests/test_api.py#L1476) | 1476 | `"        {\"Forwarded\": \"for=203.0.113.9\"},"` | — |
| [SRC-3451CC474D-L001477](../../tests/test_api.py#L1477) | 1477 | `"    ],"` | — |
| [SRC-3451CC474D-L001478](../../tests/test_api.py#L1478) | 1478 | `")"` | — |
| [SRC-3451CC474D-L001479](../../tests/test_api.py#L1479) | 1479 | `"def test_loopback_auth_is_refused_for_forwarded_requests_even_with_local_opt_in("` | — |
| [SRC-3451CC474D-L001480](../../tests/test_api.py#L1480) | 1480 | `"    local_api, forwarding_header"` | — |
| [SRC-3451CC474D-L001481](../../tests/test_api.py#L1481) | 1481 | `"):"` | — |
| [SRC-3451CC474D-L001482](../../tests/test_api.py#L1482) | 1482 | `"    status, _ = request_json(local_api, \"/api/leads\", headers=forwarding_header)"` | — |
| [SRC-3451CC474D-L001483](../../tests/test_api.py#L1483) | 1483 | `"    assert status == 401"` | — |
| [SRC-3451CC474D-L001484](../../tests/test_api.py#L1484) | 1484 | `""` | — |
| [SRC-3451CC474D-L001485](../../tests/test_api.py#L1485) | 1485 | `""` | — |
| [SRC-3451CC474D-L001486](../../tests/test_api.py#L1486) | 1486 | `""` | — |
| [SRC-3451CC474D-L001487](../../tests/test_api.py#L1487) | 1487 | `"def test_lead_store_uses_postgres_database_url_when_configured(monkeypatch):"` | — |
| [SRC-3451CC474D-L001488](../../tests/test_api.py#L1488) | 1488 | `"    import api.omarai as api_module"` | — |
| [SRC-3451CC474D-L001489](../../tests/test_api.py#L1489) | 1489 | `""` | — |
| [SRC-3451CC474D-L001490](../../tests/test_api.py#L1490) | 1490 | `"    monkeypatch.delenv(\"OMARAI_DB_PATH\", raising=False)"` | — |
| [SRC-3451CC474D-L001491](../../tests/test_api.py#L1491) | 1491 | `"    monkeypatch.delenv(\"DATABASE_URL\", raising=False)"` | — |
| [SRC-3451CC474D-L001492](../../tests/test_api.py#L1492) | 1492 | `"    database_url = \"postgresql://user:secret@example.neon.tech/omarai?sslmode=require\""` | — |
| [SRC-3451CC474D-L001493](../../tests/test_api.py#L1493) | 1493 | `"    monkeypatch.setenv(\"OMARAI_DATABASE_URL\", database_url)"` | — |
| [SRC-3451CC474D-L001494](../../tests/test_api.py#L1494) | 1494 | `"    captured = {}"` | — |
| [SRC-3451CC474D-L001495](../../tests/test_api.py#L1495) | 1495 | `""` | — |
| [SRC-3451CC474D-L001496](../../tests/test_api.py#L1496) | 1496 | `"    class Store:"` | — |
| [SRC-3451CC474D-L001497](../../tests/test_api.py#L1497) | 1497 | `"        def __init__(self, path=None, *, database_url=None):"` | — |
| [SRC-3451CC474D-L001498](../../tests/test_api.py#L1498) | 1498 | `"            captured[\"path\"] = path"` | — |
| [SRC-3451CC474D-L001499](../../tests/test_api.py#L1499) | 1499 | `"            captured[\"database_url\"] = database_url"` | — |
| [SRC-3451CC474D-L001500](../../tests/test_api.py#L1500) | 1500 | `""` | — |
| [SRC-3451CC474D-L001501](../../tests/test_api.py#L1501) | 1501 | `"    monkeypatch.setattr(api_module, \"LeadStore\", Store)"` | — |
| [SRC-3451CC474D-L001502](../../tests/test_api.py#L1502) | 1502 | `""` | — |
| [SRC-3451CC474D-L001503](../../tests/test_api.py#L1503) | 1503 | `"    store = api_module._lead_store_from_environment()"` | — |
| [SRC-3451CC474D-L001504](../../tests/test_api.py#L1504) | 1504 | `""` | — |
| [SRC-3451CC474D-L001505](../../tests/test_api.py#L1505) | 1505 | `"    assert isinstance(store, Store)"` | — |
| [SRC-3451CC474D-L001506](../../tests/test_api.py#L1506) | 1506 | `"    assert captured == {\"path\": None, \"database_url\": database_url}"` | — |
| [SRC-3451CC474D-L001507](../../tests/test_api.py#L1507) | 1507 | `""` | — |
| [SRC-3451CC474D-L001508](../../tests/test_api.py#L1508) | 1508 | `""` | — |
| [SRC-3451CC474D-L001509](../../tests/test_api.py#L1509) | 1509 | `"def test_lead_store_rejects_conflicting_postgres_url_and_sqlite_path(monkeypatch, tmp_path):"` | — |
| [SRC-3451CC474D-L001510](../../tests/test_api.py#L1510) | 1510 | `"    import api.omarai as api_module"` | — |
| [SRC-3451CC474D-L001511](../../tests/test_api.py#L1511) | 1511 | `"    import pytest"` | — |
| [SRC-3451CC474D-L001512](../../tests/test_api.py#L1512) | 1512 | `""` | — |
| [SRC-3451CC474D-L001513](../../tests/test_api.py#L1513) | 1513 | `"    monkeypatch.setenv(\"OMARAI_DATABASE_URL\", \"postgresql://user:secret@example.neon.tech/omarai\")"` | — |
| [SRC-3451CC474D-L001514](../../tests/test_api.py#L1514) | 1514 | `"    monkeypatch.setenv(\"OMARAI_DB_PATH\", str(tmp_path / \"omarai.sqlite3\"))"` | — |
| [SRC-3451CC474D-L001515](../../tests/test_api.py#L1515) | 1515 | `""` | — |
| [SRC-3451CC474D-L001516](../../tests/test_api.py#L1516) | 1516 | `"    with pytest.raises(ValueError, match=\"configure either OMARAI_DATABASE_URL\"):"` | — |
| [SRC-3451CC474D-L001517](../../tests/test_api.py#L1517) | 1517 | `"        api_module._lead_store_from_environment()"` | — |
| [SRC-3451CC474D-L001518](../../tests/test_api.py#L1518) | 1518 | `""` | — |
| [SRC-3451CC474D-L001519](../../tests/test_api.py#L1519) | 1519 | `""` | — |
| [SRC-3451CC474D-L001520](../../tests/test_api.py#L1520) | 1520 | `""` | — |
| [SRC-3451CC474D-L001521](../../tests/test_api.py#L1521) | 1521 | `"def test_health_reports_storage_backend_without_exposing_database_credentials(monkeypatch, local_api):"` | — |
| [SRC-3451CC474D-L001522](../../tests/test_api.py#L1522) | 1522 | `"    import json"` | — |
| [SRC-3451CC474D-L001523](../../tests/test_api.py#L1523) | 1523 | `"    from types import SimpleNamespace"` | — |
| [SRC-3451CC474D-L001524](../../tests/test_api.py#L1524) | 1524 | `"    from urllib.request import urlopen"` | — |
| [SRC-3451CC474D-L001525](../../tests/test_api.py#L1525) | 1525 | `""` | — |
| [SRC-3451CC474D-L001526](../../tests/test_api.py#L1526) | 1526 | `"    import api.omarai as api_module"` | — |
| [SRC-3451CC474D-L001527](../../tests/test_api.py#L1527) | 1527 | `""` | — |
| [SRC-3451CC474D-L001528](../../tests/test_api.py#L1528) | 1528 | `"    monkeypatch.setattr(api_module.Handler, \"store\", SimpleNamespace(backend=\"postgresql\"))"` | — |
| [SRC-3451CC474D-L001529](../../tests/test_api.py#L1529) | 1529 | `"    monkeypatch.setenv("` | — |
| [SRC-3451CC474D-L001530](../../tests/test_api.py#L1530) | 1530 | `"        \"OMARAI_DATABASE_URL\","` | — |
| [SRC-3451CC474D-L001531](../../tests/test_api.py#L1531) | 1531 | `"        \"postgresql://health-user:health-password@example.neon.tech/omarai?sslmode=require\","` | — |
| [SRC-3451CC474D-L001532](../../tests/test_api.py#L1532) | 1532 | `"    )"` | — |
| [SRC-3451CC474D-L001533](../../tests/test_api.py#L1533) | 1533 | `""` | — |
| [SRC-3451CC474D-L001534](../../tests/test_api.py#L1534) | 1534 | `"    with urlopen(f\"{local_api}/api/health\", timeout=3) as response:"` | — |
| [SRC-3451CC474D-L001535](../../tests/test_api.py#L1535) | 1535 | `"        payload = json.loads(response.read().decode(\"utf-8\"))"` | — |
| [SRC-3451CC474D-L001536](../../tests/test_api.py#L1536) | 1536 | `""` | — |
| [SRC-3451CC474D-L001537](../../tests/test_api.py#L1537) | 1537 | `"    assert payload[\"storage\"][\"backend\"] == \"postgresql\""` | — |
| [SRC-3451CC474D-L001538](../../tests/test_api.py#L1538) | 1538 | `"    assert payload[\"storage\"][\"database_url_configured\"] is True"` | — |
| [SRC-3451CC474D-L001539](../../tests/test_api.py#L1539) | 1539 | `"    assert payload[\"storage\"][\"durability_status\"] == \"external_database_configured\""` | — |
| [SRC-3451CC474D-L001540](../../tests/test_api.py#L1540) | 1540 | `"    assert \"health-password\" not in json.dumps(payload)"` | — |
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
