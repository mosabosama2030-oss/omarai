# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **059**
- سجلات الأسطر: **800**
- النطاق: SRC-F725E90B2A-L004035 إلى SRC-DE7EABE998-L000271
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-F725E90B2A — [tests/test_web_agent.py](../../tests/test_web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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
| [SRC-F725E90B2A-L004294](../../tests/test_web_agent.py#L4294) | 4294 | `")"` | — |
| [SRC-F725E90B2A-L004295](../../tests/test_web_agent.py#L4295) | 4295 | `"def test_model_provider_base_url_allows_https_or_loopback(url):"` | — |
| [SRC-F725E90B2A-L004296](../../tests/test_web_agent.py#L4296) | 4296 | `"    from agents.web_agent import _is_safe_model_base_url"` | — |
| [SRC-F725E90B2A-L004297](../../tests/test_web_agent.py#L4297) | 4297 | `""` | — |
| [SRC-F725E90B2A-L004298](../../tests/test_web_agent.py#L4298) | 4298 | `"    assert _is_safe_model_base_url(url) is True"` | — |
| [SRC-F725E90B2A-L004299](../../tests/test_web_agent.py#L4299) | 4299 | `""` | — |
| [SRC-F725E90B2A-L004300](../../tests/test_web_agent.py#L4300) | 4300 | `""` | — |
| [SRC-F725E90B2A-L004301](../../tests/test_web_agent.py#L4301) | 4301 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L004302](../../tests/test_web_agent.py#L4302) | 4302 | `"    \"url\","` | — |
| [SRC-F725E90B2A-L004303](../../tests/test_web_agent.py#L4303) | 4303 | `"    ["` | — |
| [SRC-F725E90B2A-L004304](../../tests/test_web_agent.py#L4304) | 4304 | `"        \"http://api.example.test/v1\","` | — |
| [SRC-F725E90B2A-L004305](../../tests/test_web_agent.py#L4305) | 4305 | `"        \"ftp://api.example.test/v1\","` | — |
| [SRC-F725E90B2A-L004306](../../tests/test_web_agent.py#L4306) | 4306 | `"        \"https://user:password@api.example.test/v1\","` | — |
| [SRC-F725E90B2A-L004307](../../tests/test_web_agent.py#L4307) | 4307 | `"        \"https://api.example.test/v1?token=secret\","` | — |
| [SRC-F725E90B2A-L004308](../../tests/test_web_agent.py#L4308) | 4308 | `"        \"https://api.example.test/v1#fragment\","` | — |
| [SRC-F725E90B2A-L004309](../../tests/test_web_agent.py#L4309) | 4309 | `"        \"https:///missing-host\","` | — |
| [SRC-F725E90B2A-L004310](../../tests/test_web_agent.py#L4310) | 4310 | `"        \"https://api.example.test:99999/v1\","` | — |
| [SRC-F725E90B2A-L004311](../../tests/test_web_agent.py#L4311) | 4311 | `"    ],"` | — |
| [SRC-F725E90B2A-L004312](../../tests/test_web_agent.py#L4312) | 4312 | `")"` | — |
| [SRC-F725E90B2A-L004313](../../tests/test_web_agent.py#L4313) | 4313 | `"def test_model_provider_base_url_rejects_insecure_or_ambiguous_urls(url):"` | — |
| [SRC-F725E90B2A-L004314](../../tests/test_web_agent.py#L4314) | 4314 | `"    from agents.web_agent import _is_safe_model_base_url"` | — |
| [SRC-F725E90B2A-L004315](../../tests/test_web_agent.py#L4315) | 4315 | `""` | — |
| [SRC-F725E90B2A-L004316](../../tests/test_web_agent.py#L4316) | 4316 | `"    assert _is_safe_model_base_url(url) is False"` | — |
| [SRC-F725E90B2A-L004317](../../tests/test_web_agent.py#L4317) | 4317 | `""` | — |
| [SRC-F725E90B2A-L004318](../../tests/test_web_agent.py#L4318) | 4318 | `""` | — |
| [SRC-F725E90B2A-L004319](../../tests/test_web_agent.py#L4319) | 4319 | `"def test_model_provider_rejects_remote_http_before_sending_bearer_key(monkeypatch):"` | — |
| [SRC-F725E90B2A-L004320](../../tests/test_web_agent.py#L4320) | 4320 | `"    from agents import web_agent"` | — |
| [SRC-F725E90B2A-L004321](../../tests/test_web_agent.py#L4321) | 4321 | `""` | — |
| [SRC-F725E90B2A-L004322](../../tests/test_web_agent.py#L4322) | 4322 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L004323](../../tests/test_web_agent.py#L4323) | 4323 | `"    agent.api_key = \"unit-test-secret\""` | — |
| [SRC-F725E90B2A-L004324](../../tests/test_web_agent.py#L4324) | 4324 | `"    agent.base_url = \"http://provider.example/api/v1\""` | — |
| [SRC-F725E90B2A-L004325](../../tests/test_web_agent.py#L4325) | 4325 | `""` | — |
| [SRC-F725E90B2A-L004326](../../tests/test_web_agent.py#L4326) | 4326 | `"    def unexpected_request(*_args, **_kwargs):"` | — |
| [SRC-F725E90B2A-L004327](../../tests/test_web_agent.py#L4327) | 4327 | `"        pytest.fail(\"bearer credentials must not be sent to a remote HTTP URL\")"` | — |
| [SRC-F725E90B2A-L004328](../../tests/test_web_agent.py#L4328) | 4328 | `""` | — |
| [SRC-F725E90B2A-L004329](../../tests/test_web_agent.py#L4329) | 4329 | `"    monkeypatch.setattr(web_agent, \"_open_model_request\", unexpected_request)"` | — |
| [SRC-F725E90B2A-L004330](../../tests/test_web_agent.py#L4330) | 4330 | `"    with pytest.raises(RuntimeError, match=\"HTTPS\"):"` | — |
| [SRC-F725E90B2A-L004331](../../tests/test_web_agent.py#L4331) | 4331 | `"        agent._request_completion("` | — |
| [SRC-F725E90B2A-L004332](../../tests/test_web_agent.py#L4332) | 4332 | `"            [{\"role\": \"user\", \"content\": \"test\"}],"` | — |
| [SRC-F725E90B2A-L004333](../../tests/test_web_agent.py#L4333) | 4333 | `"            max_tokens=100,"` | — |
| [SRC-F725E90B2A-L004334](../../tests/test_web_agent.py#L4334) | 4334 | `"        )"` | — |
| [SRC-F725E90B2A-L004335](../../tests/test_web_agent.py#L4335) | 4335 | `""` | — |
| [SRC-F725E90B2A-L004336](../../tests/test_web_agent.py#L4336) | 4336 | `"    assert agent.generation_diagnostics[-1][\"status\"] == \"unsafe_provider_url\""` | — |
| [SRC-F725E90B2A-L004337](../../tests/test_web_agent.py#L4337) | 4337 | `"    assert agent.generation_diagnostics[-1][\"request_started\"] is False"` | — |
| [SRC-F725E90B2A-L004338](../../tests/test_web_agent.py#L4338) | 4338 | `""` | — |
| [SRC-F725E90B2A-L004339](../../tests/test_web_agent.py#L4339) | 4339 | `""` | — |
| [SRC-F725E90B2A-L004340](../../tests/test_web_agent.py#L4340) | 4340 | `"def test_health_status_redacts_model_provider_userinfo_path_and_query(monkeypatch):"` | — |
| [SRC-F725E90B2A-L004341](../../tests/test_web_agent.py#L4341) | 4341 | `"    monkeypatch.setenv("` | — |
| [SRC-F725E90B2A-L004342](../../tests/test_web_agent.py#L4342) | 4342 | `"        \"OMARAI_LLM_BASE_URL\","` | — |
| [SRC-F725E90B2A-L004343](../../tests/test_web_agent.py#L4343) | 4343 | `"        \"https://health-user:health-password@provider.example/api/v1?token=health-secret\","` | — |
| [SRC-F725E90B2A-L004344](../../tests/test_web_agent.py#L4344) | 4344 | `"    )"` | — |
| [SRC-F725E90B2A-L004345](../../tests/test_web_agent.py#L4345) | 4345 | `""` | — |
| [SRC-F725E90B2A-L004346](../../tests/test_web_agent.py#L4346) | 4346 | `"    status = WebAgent.status()"` | — |
| [SRC-F725E90B2A-L004347](../../tests/test_web_agent.py#L4347) | 4347 | `"    provider = status[\"language_model_provider\"]"` | — |
| [SRC-F725E90B2A-L004348](../../tests/test_web_agent.py#L4348) | 4348 | `""` | — |
| [SRC-F725E90B2A-L004349](../../tests/test_web_agent.py#L4349) | 4349 | `"    assert provider == \"https://provider.example\""` | — |
| [SRC-F725E90B2A-L004350](../../tests/test_web_agent.py#L4350) | 4350 | `"    assert \"health-user\" not in provider"` | — |
| [SRC-F725E90B2A-L004351](../../tests/test_web_agent.py#L4351) | 4351 | `"    assert \"health-password\" not in provider"` | — |
| [SRC-F725E90B2A-L004352](../../tests/test_web_agent.py#L4352) | 4352 | `"    assert \"health-secret\" not in provider"` | — |
| [SRC-F725E90B2A-L004353](../../tests/test_web_agent.py#L4353) | 4353 | `"    assert \"/api/v1\" not in provider"` | — |
| [SRC-F725E90B2A-L004354](../../tests/test_web_agent.py#L4354) | 4354 | `""` | — |
| [SRC-F725E90B2A-L004355](../../tests/test_web_agent.py#L4355) | 4355 | `""` | — |
| [SRC-F725E90B2A-L004356](../../tests/test_web_agent.py#L4356) | 4356 | `"def test_answer_is_withheld_when_semantic_claim_support_is_not_established(monkeypatch):"` | — |
| [SRC-F725E90B2A-L004357](../../tests/test_web_agent.py#L4357) | 4357 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L004358](../../tests/test_web_agent.py#L4358) | 4358 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L004359](../../tests/test_web_agent.py#L4359) | 4359 | `"    source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L004360](../../tests/test_web_agent.py#L4360) | 4360 | `"    source[\"providers\"] = [\"user_supplied_url\"]"` | — |
| [SRC-F725E90B2A-L004361](../../tests/test_web_agent.py#L4361) | 4361 | `"    source[\"page_fetched\"] = True"` | — |
| [SRC-F725E90B2A-L004362](../../tests/test_web_agent.py#L4362) | 4362 | `"    source[\"page_text\"] = \"النص الكامل المستخرج من الصفحة التي قدمها المستخدم.\""` | — |
| [SRC-F725E90B2A-L004363](../../tests/test_web_agent.py#L4363) | 4363 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L004364](../../tests/test_web_agent.py#L4364) | 4364 | `"        \"queries\": [\"لخص الصفحة\"],"` | — |
| [SRC-F725E90B2A-L004365](../../tests/test_web_agent.py#L4365) | 4365 | `"        \"direct_urls\": [\"https://example.com/research\"],"` | — |
| [SRC-F725E90B2A-L004366](../../tests/test_web_agent.py#L4366) | 4366 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L004367](../../tests/test_web_agent.py#L4367) | 4367 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L004368](../../tests/test_web_agent.py#L4368) | 4368 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L004369](../../tests/test_web_agent.py#L4369) | 4369 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L004370](../../tests/test_web_agent.py#L4370) | 4370 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L004371](../../tests/test_web_agent.py#L4371) | 4371 | `"    }"` | — |
| [SRC-F725E90B2A-L004372](../../tests/test_web_agent.py#L4372) | 4372 | `""` | — |
| [SRC-F725E90B2A-L004373](../../tests/test_web_agent.py#L4373) | 4373 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L004374](../../tests/test_web_agent.py#L4374) | 4374 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L004375](../../tests/test_web_agent.py#L4375) | 4375 | `"        agent,"` | — |
| [SRC-F725E90B2A-L004376](../../tests/test_web_agent.py#L4376) | 4376 | `"        \"_collect_research\","` | — |
| [SRC-F725E90B2A-L004377](../../tests/test_web_agent.py#L4377) | 4377 | `"        lambda research_plan: ("` | — |
| [SRC-F725E90B2A-L004378](../../tests/test_web_agent.py#L4378) | 4378 | `"            [source], [], {"` | — |
| [SRC-F725E90B2A-L004379](../../tests/test_web_agent.py#L4379) | 4379 | `"                \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L004380](../../tests/test_web_agent.py#L4380) | 4380 | `"                \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L004381](../../tests/test_web_agent.py#L4381) | 4381 | `"                \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L004382](../../tests/test_web_agent.py#L4382) | 4382 | `"                \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L004383](../../tests/test_web_agent.py#L4383) | 4383 | `"                \"pages_fetched\": 1,"` | — |
| [SRC-F725E90B2A-L004384](../../tests/test_web_agent.py#L4384) | 4384 | `"                \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L004385](../../tests/test_web_agent.py#L4385) | 4385 | `"                \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L004386](../../tests/test_web_agent.py#L4386) | 4386 | `"                \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L004387](../../tests/test_web_agent.py#L4387) | 4387 | `"                \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L004388](../../tests/test_web_agent.py#L4388) | 4388 | `"                \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L004389](../../tests/test_web_agent.py#L4389) | 4389 | `"            },"` | — |
| [SRC-F725E90B2A-L004390](../../tests/test_web_agent.py#L4390) | 4390 | `"        ),"` | — |
| [SRC-F725E90B2A-L004391](../../tests/test_web_agent.py#L4391) | 4391 | `"    )"` | — |
| [SRC-F725E90B2A-L004392](../../tests/test_web_agent.py#L4392) | 4392 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, item: True)"` | — |
| [SRC-F725E90B2A-L004393](../../tests/test_web_agent.py#L4393) | 4393 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L004394](../../tests/test_web_agent.py#L4394) | 4394 | `"        agent, \"_generate\","` | — |
| [SRC-F725E90B2A-L004395](../../tests/test_web_agent.py#L4395) | 4395 | `"        lambda *args, **kwargs: \"ادعاء واقعي غير مدعوم بما يكفي [المصدر 1].\","` | — |
| [SRC-F725E90B2A-L004396](../../tests/test_web_agent.py#L4396) | 4396 | `"    )"` | — |
| [SRC-F725E90B2A-L004397](../../tests/test_web_agent.py#L4397) | 4397 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L004398](../../tests/test_web_agent.py#L4398) | 4398 | `"        agent, \"_review_answer\","` | — |
| [SRC-F725E90B2A-L004399](../../tests/test_web_agent.py#L4399) | 4399 | `"        lambda question, answer, sources: answer,"` | — |
| [SRC-F725E90B2A-L004400](../../tests/test_web_agent.py#L4400) | 4400 | `"    )"` | — |
| [SRC-F725E90B2A-L004401](../../tests/test_web_agent.py#L4401) | 4401 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L004402](../../tests/test_web_agent.py#L4402) | 4402 | `"        agent, \"_verify_semantic_claims\","` | — |
| [SRC-F725E90B2A-L004403](../../tests/test_web_agent.py#L4403) | 4403 | `"        lambda *args, **kwargs: {"` | — |
| [SRC-F725E90B2A-L004404](../../tests/test_web_agent.py#L4404) | 4404 | `"            \"status\": \"unsupported_claims_detected\","` | — |
| [SRC-F725E90B2A-L004405](../../tests/test_web_agent.py#L4405) | 4405 | `"            \"withhold_answer\": True,"` | — |
| [SRC-F725E90B2A-L004406](../../tests/test_web_agent.py#L4406) | 4406 | `"            \"reason\": \"one_or_more_claims_lack_unconflicted_cited_support\","` | — |
| [SRC-F725E90B2A-L004407](../../tests/test_web_agent.py#L4407) | 4407 | `"        },"` | — |
| [SRC-F725E90B2A-L004408](../../tests/test_web_agent.py#L4408) | 4408 | `"    )"` | — |
| [SRC-F725E90B2A-L004409](../../tests/test_web_agent.py#L4409) | 4409 | `""` | — |
| [SRC-F725E90B2A-L004410](../../tests/test_web_agent.py#L4410) | 4410 | `"    result = agent.answer(\"لخص الصفحة https://example.com/research\")"` | — |
| [SRC-F725E90B2A-L004411](../../tests/test_web_agent.py#L4411) | 4411 | `""` | — |
| [SRC-F725E90B2A-L004412](../../tests/test_web_agent.py#L4412) | 4412 | `"    assert result[\"final_answer_status\"] == \"semantic_verification_failed_with_source_fallback\""` | — |
| [SRC-F725E90B2A-L004413](../../tests/test_web_agent.py#L4413) | 4413 | `"    assert result[\"search_report\"][\"answer_was_withheld\"] is True"` | — |
| [SRC-F725E90B2A-L004414](../../tests/test_web_agent.py#L4414) | 4414 | `"    assert result[\"search_report\"][\"semantic_claim_verification\"][\"status\"] == ("` | — |
| [SRC-F725E90B2A-L004415](../../tests/test_web_agent.py#L4415) | 4415 | `"        \"unsupported_claims_detected\""` | — |
| [SRC-F725E90B2A-L004416](../../tests/test_web_agent.py#L4416) | 4416 | `"    )"` | — |
| [SRC-F725E90B2A-L004417](../../tests/test_web_agent.py#L4417) | 4417 | `"    assert \"ادعاء واقعي غير مدعوم\" not in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L004418](../../tests/test_web_agent.py#L4418) | 4418 | `"    assert \"المقتطفات أدناه مواد مصدرية\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L004419](../../tests/test_web_agent.py#L4419) | 4419 | `"    assert result[\"search_report\"][\"pipeline_completion_status\"] == \"partial\""` | — |
| [SRC-F725E90B2A-L004420](../../tests/test_web_agent.py#L4420) | 4420 | `"    assert result[\"citation_validation\"][\"valid_citation_count\"] == 0"` | — |
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
| [SRC-DE7EABE998-L000045](../../web/agent.html#L45) | 45 | `"<a class=\"ghost\" href=\"/workspace\">مساحة عمل المبيعات ↗</a></header>"` | — |
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
| [SRC-DE7EABE998-L000073](../../web/agent.html#L73) | 73 | `"      <button id=\"saveAccessToken\" type=\"button\" class=\"ghost checkbutton\">تسجيل الدخول</button>"` | — |
| [SRC-DE7EABE998-L000074](../../web/agent.html#L74) | 74 | `"      <button id=\"logoutSession\" type=\"button\" class=\"ghost checkbutton\">تسجيل الخروج</button>"` | — |
| [SRC-DE7EABE998-L000075](../../web/agent.html#L75) | 75 | `"      <p id=\"authStatus\" style=\"font-size:10px;color:var(--muted);line-height:1.8;margin-top:7px\" aria-live=\"polite\">لا يُحفظ رمز الوصول في تخزين JavaScript؛ بعد الدخول يستخدم المتصفح ملف ارتباط HttpOnly محدود المدة.</p>"` | — |
| [SRC-DE7EABE998-L000076](../../web/agent.html#L76) | 76 | `"    </div>"` | — |
| [SRC-DE7EABE998-L000077](../../web/agent.html#L77) | 77 | `"    <div class=\"sideblock\">"` | — |
| [SRC-DE7EABE998-L000078](../../web/agent.html#L78) | 78 | `"      <h3>حالة الاتصال الفعلية</h3>"` | — |
| [SRC-DE7EABE998-L000079](../../web/agent.html#L79) | 79 | `"      <p id=\"setupStatus\">جارٍ فحص إعدادات الخادم. إعداد المحرك لا يعني أن البحث الحي نجح بعد؛ استخدم الاختبار أدناه للتحقق من الاتصال الفعلي.</p>"` | — |
| [SRC-DE7EABE998-L000080](../../web/agent.html#L80) | 80 | `"      <label style=\"display:flex;gap:8px;align-items:flex-start;margin:11px 0;font-size:10px;color:#b9c9dc;line-height:1.7\"><input id=\"diagSocial\" type=\"checkbox\" style=\"margin-top:3px\"> اختبار المصادر الاجتماعية العامة والموصلات المهيأة أيضًا</label>"` | — |
| [SRC-DE7EABE998-L000081](../../web/agent.html#L81) | 81 | `"      <button id=\"runDiagnostics\" type=\"button\" class=\"primary checkbutton\">اختبار حي للإنترنت والنموذج</button>"` | — |
| [SRC-DE7EABE998-L000082](../../web/agent.html#L82) | 82 | `"      <p id=\"diagnosticsResult\" class=\"diag\" aria-live=\"polite\"></p>"` | — |
| [SRC-DE7EABE998-L000083](../../web/agent.html#L83) | 83 | `"    </div>"` | — |
| [SRC-DE7EABE998-L000084](../../web/agent.html#L84) | 84 | `"    <div class=\"sideblock\">"` | — |
| [SRC-DE7EABE998-L000085](../../web/agent.html#L85) | 85 | `"      <h3>مصادر البحث</h3>"` | — |
| [SRC-DE7EABE998-L000086](../../web/agent.html#L86) | 86 | `"      <div class=\"sidefeature\"><div class=\"sideicon\">⌕</div><div><b>محركات الويب</b><span>DuckDuckGo وBing؛ ويمكن إضافة Brave وTavily بمفتاح API اختياري.</span></div></div>"` | — |
| [SRC-DE7EABE998-L000087](../../web/agent.html#L87) | 87 | `"      <div class=\"sidefeature\"><div class=\"sideicon\">▤</div><div><b>الأخبار والمصادر العامة</b><span>Google News عند طلب معلومات حديثة، وقراءة الصفحات التي تسمح بالوصول العام.</span></div></div>"` | — |
| [SRC-DE7EABE998-L000088](../../web/agent.html#L88) | 88 | `"      <div class=\"sidefeature\"><div class=\"sideicon\">◎</div><div><b>الشبكات الاجتماعية</b><span>مصادر عامة موصولة فعليًا أو نتائج مفهرسة؛ ليست تغطية كاملة لكل المنصات أو المنشورات.</span></div></div>"` | — |
| [SRC-DE7EABE998-L000089](../../web/agent.html#L89) | 89 | `"      <div id=\"providerSetup\"></div>"` | — |
| [SRC-DE7EABE998-L000090](../../web/agent.html#L90) | 90 | `"    </div>"` | — |
| [SRC-DE7EABE998-L000091](../../web/agent.html#L91) | 91 | `"    <div class=\"sideblock\">"` | — |
| [SRC-DE7EABE998-L000092](../../web/agent.html#L92) | 92 | `"      <h3>كيف تقرأ النتيجة؟</h3>"` | — |
| [SRC-DE7EABE998-L000093](../../web/agent.html#L93) | 93 | `"      <p>تنوع النطاقات ومحركات البحث والصفحات المقروءة وتواريخ النشر إشارات إلى مدى تغطية البحث، لا دليلًا قاطعًا على صحة الادعاء. افتح المصادر المهمة، وانتبه إلى التضارب والمعلومات غير المؤرخة.</p>"` | — |
| [SRC-DE7EABE998-L000094](../../web/agent.html#L94) | 94 | `"    </div>"` | — |
| [SRC-DE7EABE998-L000095](../../web/agent.html#L95) | 95 | `"  </aside>"` | — |
| [SRC-DE7EABE998-L000096](../../web/agent.html#L96) | 96 | `"</main>"` | — |
| [SRC-DE7EABE998-L000097](../../web/agent.html#L97) | 97 | `"<footer class=\"foot\">Omarai · لا يتجاوز تسجيل الدخول أو الصفحات الخاصة أو الحواجز المدفوعة، ولا يرسل رسائل تلقائية. الإتاحة الفعلية تعتمد على اتصال الإنترنت، وحدود محركات البحث، ومفاتيح الخدمات الاختيارية.</footer>"` | — |
| [SRC-DE7EABE998-L000098](../../web/agent.html#L98) | 98 | `"</div>"` | — |
| [SRC-DE7EABE998-L000099](../../web/agent.html#L99) | 99 | `""` | — |
| [SRC-DE7EABE998-L000100](../../web/agent.html#L100) | 100 | `"<script>"` | — |
| [SRC-DE7EABE998-L000101](../../web/agent.html#L101) | 101 | `"const $=id=>document.getElementById(id);"` | — |
| [SRC-DE7EABE998-L000102](../../web/agent.html#L102) | 102 | `"function apiHeaders(){return {\"Content-Type\":\"application/json\"};}"` | — |
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
| [SRC-DE7EABE998-L000156](../../web/agent.html#L156) | 156 | `" if(s.lead_qualification===\"public_demand_signal\"\|\|s.lead_qualification===\"public_buyer_intent_signal\"){"` | — |
| [SRC-DE7EABE998-L000157](../../web/agent.html#L157) | 157 | `"  const demandType=s.lead_intent_evidence&&s.lead_intent_evidence.signal_type;"` | — |
| [SRC-DE7EABE998-L000158](../../web/agent.html#L158) | 158 | `"  const demandLabels={direct_purchase_request:\"طلب شراء مباشر\",request_for_quotation:\"طلب عرض سعر\",tender_or_procurement:\"مناقصة أو توريد\",stated_need:\"احتياج معلن\",indirect_indicator:\"مؤشر احتياج غير مباشر\"};"` | — |
| [SRC-DE7EABE998-L000159](../../web/agent.html#L159) | 159 | `"  const demandLabel=demandLabels[demandType]\|\|\"إشارة طلب غير مكتملة التصنيف\";"` | — |
| [SRC-DE7EABE998-L000160](../../web/agent.html#L160) | 160 | `"  tags.push('<span class=\"tag read\">'+escapeHtml(demandLabel)+' — ملاءمة المنتج والهوية تحتاج إلى تحقق</span>');"` | — |
| [SRC-DE7EABE998-L000161](../../web/agent.html#L161) | 161 | `" }"` | — |
| [SRC-DE7EABE998-L000162](../../web/agent.html#L162) | 162 | `" const heading=url?'<a href=\"'+escapeHtml(url)+'\" target=\"_blank\" rel=\"noopener noreferrer\">['+(index+1)+'] '+title+' ↗</a>':'<strong>['+(index+1)+'] '+title+'</strong><p class=\"warning\">لم يُعرض الرابط لأنه غير صالح.</p>';"` | — |
| [SRC-DE7EABE998-L000163](../../web/agent.html#L163) | 163 | `" return '<article class=\"source\">'+heading+'<p>'+escapeHtml(s.snippet\|\|\"لا يتوفر مقتطف نصي من هذه النتيجة.\")+'</p><div class=\"source-meta\">'+tags.join(\"\")+'</div></article>';"` | — |
| [SRC-DE7EABE998-L000164](../../web/agent.html#L164) | 164 | `"}"` | — |
| [SRC-DE7EABE998-L000165](../../web/agent.html#L165) | 165 | `"function renderReport(result){"` | — |
| [SRC-DE7EABE998-L000166](../../web/agent.html#L166) | 166 | `" const r=result&&result.search_report&&typeof result.search_report===\"object\"?result.search_report:{};"` | — |
| [SRC-DE7EABE998-L000167](../../web/agent.html#L167) | 167 | `" const completion=r.research_completion&&typeof r.research_completion===\"object\"?r.research_completion:"` | — |
| [SRC-DE7EABE998-L000168](../../web/agent.html#L168) | 168 | `"  (result&&result.research_completion&&typeof result.research_completion===\"object\"?result.research_completion:null);"` | — |
| [SRC-DE7EABE998-L000169](../../web/agent.html#L169) | 169 | `" const completionStatusLabels={"` | — |
| [SRC-DE7EABE998-L000170](../../web/agent.html#L170) | 170 | `"  execution_stopped_budget:\"توقفت العملية عند حد الميزانية\","` | — |
| [SRC-DE7EABE998-L000171](../../web/agent.html#L171) | 171 | `"  no_eligible_sources_after_filtering:\"لم يبقَ مصدر مقبول بعد التصفية\","` | — |
| [SRC-DE7EABE998-L000172](../../web/agent.html#L172) | 172 | `"  search_failed_or_incomplete:\"البحث فشل أو لم يكتمل\","` | — |
| [SRC-DE7EABE998-L000173](../../web/agent.html#L173) | 173 | `"  no_results_returned:\"اكتمل البحث دون نتائج\","` | — |
| [SRC-DE7EABE998-L000174](../../web/agent.html#L174) | 174 | `"  search_not_attempted:\"لم تُنفذ محاولة البحث\","` | — |
| [SRC-DE7EABE998-L000175](../../web/agent.html#L175) | 175 | `"  insufficient_evidence:\"الأدلة غير كافية\","` | — |
| [SRC-DE7EABE998-L000176](../../web/agent.html#L176) | 176 | `"  source_snippets_only_generation_not_completed:\"مقتطفات فقط؛ لم تكتمل صياغة الإجابة\","` | — |
| [SRC-DE7EABE998-L000177](../../web/agent.html#L177) | 177 | `"  evidence_collected_generation_not_completed:\"جُمعت أدلة؛ لم تكتمل صياغة الإجابة\","` | — |
| [SRC-DE7EABE998-L000178](../../web/agent.html#L178) | 178 | `"  answer_generation_or_review_failed:\"تعذر توليد الإجابة أو مراجعتها\","` | — |
| [SRC-DE7EABE998-L000179](../../web/agent.html#L179) | 179 | `"  partial_answer_evidence_gaps_detected:\"إجابة جزئية مع فجوات أدلة محتملة\","` | — |
| [SRC-DE7EABE998-L000180](../../web/agent.html#L180) | 180 | `"  answer_generated_citations_range_checked_semantic_support_unverified:\"وُلّدت الإجابة وفُحصت أرقام الإحالات فقط؛ دعم الادعاءات دلاليًا غير متحقق\","` | — |
| [SRC-DE7EABE998-L000181](../../web/agent.html#L181) | 181 | `"  answer_generated_without_valid_citation_markers:\"وُلّدت الإجابة دون علامات إحالة صالحة\""` | — |
| [SRC-DE7EABE998-L000182](../../web/agent.html#L182) | 182 | `" };"` | — |
| [SRC-DE7EABE998-L000183](../../web/agent.html#L183) | 183 | `" const completionPhaseLabels={"` | — |
| [SRC-DE7EABE998-L000184](../../web/agent.html#L184) | 184 | `"  planning:\"التخطيط\",search:\"البحث\",source_filtering:\"تصفية المصادر\","` | — |
| [SRC-DE7EABE998-L000185](../../web/agent.html#L185) | 185 | `"  page_reading:\"قراءة الصفحات\",answer_generation:\"توليد الإجابة\","` | — |
| [SRC-DE7EABE998-L000186](../../web/agent.html#L186) | 186 | `"  citation_validation:\"فحص الإحالات\",semantic_verification:\"التحقق الدلالي\""` | — |
| [SRC-DE7EABE998-L000187](../../web/agent.html#L187) | 187 | `" };"` | — |
| [SRC-DE7EABE998-L000188](../../web/agent.html#L188) | 188 | `" const completionStateLabels={"` | — |
| [SRC-DE7EABE998-L000189](../../web/agent.html#L189) | 189 | `"  completed:\"مكتمل\",unknown:\"غير معلوم\",not_attempted:\"لم يبدأ\","` | — |
| [SRC-DE7EABE998-L000190](../../web/agent.html#L190) | 190 | `"  failed_or_incomplete:\"فشل أو لم يكتمل\",results_received:\"استُلمت نتائج\","` | — |
| [SRC-DE7EABE998-L000191](../../web/agent.html#L191) | 191 | `"  completed_no_results:\"اكتمل دون نتائج\",attempted_no_usable_sources:\"محاولة دون مصادر صالحة\","` | — |
| [SRC-DE7EABE998-L000192](../../web/agent.html#L192) | 192 | `"  not_applicable_no_eligible_sources:\"لا توجد مصادر نهائية\",all_final_sources_read:\"قُرئت كل الصفحات النهائية\","` | — |
| [SRC-DE7EABE998-L000193](../../web/agent.html#L193) | 193 | `"  some_final_sources_read:\"قُرئ بعض الصفحات\",no_final_source_page_read:\"لم تُقرأ صفحات نهائية\","` | — |
| [SRC-DE7EABE998-L000194](../../web/agent.html#L194) | 194 | `"  not_attempted_or_withheld:\"لم تُولد الإجابة أو حُجبت\",answer_generated:\"وُلّدت الإجابة\","` | — |
| [SRC-DE7EABE998-L000195](../../web/agent.html#L195) | 195 | `"  not_completed:\"لم يكتمل\",failed_or_unavailable:\"فشل أو غير متاح\","` | — |
| [SRC-DE7EABE998-L000196](../../web/agent.html#L196) | 196 | `"  not_run:\"لم يُنفذ\",not_performed:\"لم يُنفذ\",sources_retained:\"احتُفظ بمصادر\","` | — |
| [SRC-DE7EABE998-L000197](../../web/agent.html#L197) | 197 | `"  rejected_all_candidates:\"رُفضت كل المرشحات\",no_eligible_sources:\"لا توجد مصادر مقبولة\","` | — |
| [SRC-DE7EABE998-L000198](../../web/agent.html#L198) | 198 | `"  index_range_check_passed:\"فُحص نطاق أرقام الإحالات فقط\","` | — |
| [SRC-DE7EABE998-L000199](../../web/agent.html#L199) | 199 | `"  invalid_index_references_removed:\"حُذفت إحالات خارج النطاق\","` | — |
| [SRC-DE7EABE998-L000200](../../web/agent.html#L200) | 200 | `"  no_citation_markers_present:\"لا توجد علامات إحالة\",diagnostics_not_computed:\"تعذر احتساب التشخيص\""` | — |
| [SRC-DE7EABE998-L000201](../../web/agent.html#L201) | 201 | `" };"` | — |
| [SRC-DE7EABE998-L000202](../../web/agent.html#L202) | 202 | `" const completionSummary=completion&&completion.status"` | — |
| [SRC-DE7EABE998-L000203](../../web/agent.html#L203) | 203 | `"  ?'<p class=\"'+([\"search_failed_or_incomplete\",\"execution_stopped_budget\",\"answer_generation_or_review_failed\",\"no_eligible_sources_after_filtering\",\"partial_answer_evidence_gaps_detected\"].includes(completion.status)?\"warning\":\"report-note\")+'\"><b>حالة إكمال البحث:</b> '+escapeHtml(completionStatusLabels[completion.status]\|\|completion.status)+'. هذه حالة تشغيلية وليست احتمالًا لصحة الإجابة.</p>'"` | — |
| [SRC-DE7EABE998-L000204](../../web/agent.html#L204) | 204 | `"  :\"\";"` | — |
| [SRC-DE7EABE998-L000205](../../web/agent.html#L205) | 205 | `" const completionPhaseRows=completion&&completion.phases&&typeof completion.phases===\"object\""` | — |
| [SRC-DE7EABE998-L000206](../../web/agent.html#L206) | 206 | `"  ?Object.entries(completion.phases).map(([phase,state])=>'<li>'+escapeHtml(completionPhaseLabels[phase]\|\|phase)+': '+escapeHtml(completionStateLabels[state]\|\|state\|\|\"غير محدد\")+'</li>').join(\"\")"` | — |
| [SRC-DE7EABE998-L000207](../../web/agent.html#L207) | 207 | `"  :\"\";"` | — |
| [SRC-DE7EABE998-L000208](../../web/agent.html#L208) | 208 | `" const completionCounters=completion&&completion.counters&&typeof completion.counters===\"object\"?completion.counters:{};"` | — |
| [SRC-DE7EABE998-L000209](../../web/agent.html#L209) | 209 | `" const completionCounterRows=["` | — |
| [SRC-DE7EABE998-L000210](../../web/agent.html#L210) | 210 | `"  [completionCounters.queries_planned,\"استعلامًا مخططًا\"],"` | — |
| [SRC-DE7EABE998-L000211](../../web/agent.html#L211) | 211 | `"  [completionCounters.queries_attempted,\"استعلامًا تمت محاولته\"],"` | — |
| [SRC-DE7EABE998-L000212](../../web/agent.html#L212) | 212 | `"  [completionCounters.per_query_result_count_sum,\"مجموع أعداد النتائج المسجلة لكل استعلام، قبل إزالة التكرار\"],"` | — |
| [SRC-DE7EABE998-L000213](../../web/agent.html#L213) | 213 | `"  [completionCounters.final_source_list_count,\"مصدرًا في القائمة النهائية\"],"` | — |
| [SRC-DE7EABE998-L000214](../../web/agent.html#L214) | 214 | `"  [completionCounters.unique_normalized_url_count,\"رابطًا فريدًا بعد التطبيع\"],"` | — |
| [SRC-DE7EABE998-L000215](../../web/agent.html#L215) | 215 | `"  [completionCounters.duplicate_normalized_url_count,\"رابطًا مكررًا وفق التطبيع\"],"` | — |
| [SRC-DE7EABE998-L000216](../../web/agent.html#L216) | 216 | `"  [completionCounters.distinct_registrable_domain_count,\"نطاقًا مسجلًا مختلفًا\"],"` | — |
| [SRC-DE7EABE998-L000217](../../web/agent.html#L217) | 217 | `"  [completionCounters.pages_fetched_flag_count,\"صفحة تحمل علامة جلب\"],"` | — |
| [SRC-DE7EABE998-L000218](../../web/agent.html#L218) | 218 | `"  [completionCounters.pages_read_with_text_count,\"صفحة توفر نصها المقروء\"],"` | — |
| [SRC-DE7EABE998-L000219](../../web/agent.html#L219) | 219 | `"  [completionCounters.snippet_only_source_count,\"مصدرًا بمقتطف دون صفحة مقروءة\"],"` | — |
| [SRC-DE7EABE998-L000220](../../web/agent.html#L220) | 220 | `"  [completionCounters.connector_success_count,\"استجابة موصل ناجحة/مكتملة\"],"` | — |
| [SRC-DE7EABE998-L000221](../../web/agent.html#L221) | 221 | `"  [completionCounters.connector_failure_count,\"حالة إخفاق موصل مسجلة\"],"` | — |
| [SRC-DE7EABE998-L000222](../../web/agent.html#L222) | 222 | `"  [completionCounters.guardrail_rejected_candidate_count,\"مرشحًا مرفوضًا بحواجز الأدلة\"]"` | — |
| [SRC-DE7EABE998-L000223](../../web/agent.html#L223) | 223 | `" ];"` | — |
| [SRC-DE7EABE998-L000224](../../web/agent.html#L224) | 224 | `" const completionCounterHtml=completionCounterRows.map(([value,label])=>'<div class=\"metric\"><strong>'+escapeHtml(value===null\|\|value===undefined?\"غير محدد\":value)+'</strong><span>'+escapeHtml(label)+'</span></div>').join(\"\");"` | — |
| [SRC-DE7EABE998-L000225](../../web/agent.html#L225) | 225 | `" const consistency=completion&&completion.counter_consistency&&typeof completion.counter_consistency===\"object\"?completion.counter_consistency:null;"` | — |
| [SRC-DE7EABE998-L000226](../../web/agent.html#L226) | 226 | `" const consistencyLabels={matched:\"العدادات المتاحة متطابقة\",mismatch_detected:\"اختلاف بين بعض العدادات والقائمة النهائية\",not_computable:\"لا توجد عدادات كافية للمقارنة\"};"` | — |
| [SRC-DE7EABE998-L000227](../../web/agent.html#L227) | 227 | `" const consistencyHtml=consistency?'<p class=\"'+(consistency.status===\"mismatch_detected\"?\"warning\":\"report-note\")+'\">اتساق العدادات: '+escapeHtml(consistencyLabels[consistency.status]\|\|consistency.status\|\|\"غير محدد\")+(Array.isArray(consistency.issues)&&consistency.issues.length?' — '+consistency.issues.map(escapeHtml).join(\"، \"):\"\")+'</p>':\"\";"` | — |
| [SRC-DE7EABE998-L000228](../../web/agent.html#L228) | 228 | `" const completionDetailsHtml=completion&&completion.status"` | — |
| [SRC-DE7EABE998-L000229](../../web/agent.html#L229) | 229 | `"  ?'<details class=\"details\"><summary>تفاصيل مراحل إكمال البحث والعدادات</summary>'+(completionPhaseRows?'<p class=\"report-note\">مراحل التنفيذ:</p><ul>'+completionPhaseRows+'</ul>':\"\")+'<div class=\"metrics\">'+completionCounterHtml+'</div>'+consistencyHtml+'<p class=\"warning\">التحقق الدلالي من أن كل ادعاء مسنود فعلًا بالمصدر لم يُنفذ في هذا التشخيص. صلاحية رقم الإحالة أو قراءة الصفحة لا تثبت صحة الادعاء.</p></details>'"` | — |
| [SRC-DE7EABE998-L000230](../../web/agent.html#L230) | 230 | `"  :\"\";"` | — |
| [SRC-DE7EABE998-L000231](../../web/agent.html#L231) | 231 | `" const e=r.evidence_signals&&typeof r.evidence_signals===\"object\"?r.evidence_signals:{};"` | — |
| [SRC-DE7EABE998-L000232](../../web/agent.html#L232) | 232 | `" const sources=Array.isArray(result.sources)?result.sources:[];"` | — |
| [SRC-DE7EABE998-L000233](../../web/agent.html#L233) | 233 | `" const researchErrorOutcome=[\"attempted_research_error\",\"unknown_after_research_error\"].includes(r.search_outcome);"` | — |
| [SRC-DE7EABE998-L000234](../../web/agent.html#L234) | 234 | `" const lead=r.lead_generation&&typeof r.lead_generation===\"object\"?r.lead_generation:null;"` | — |
| [SRC-DE7EABE998-L000235](../../web/agent.html#L235) | 235 | `" const leadResearchIncomplete=!!lead&&lead.status===\"research_incomplete\";"` | — |
| [SRC-DE7EABE998-L000236](../../web/agent.html#L236) | 236 | `" const leadSignalCount=lead&&lead.candidate_signal_count!==null&&lead.candidate_signal_count!==undefined&&Number.isFinite(Number(lead.candidate_signal_count))?Number(lead.candidate_signal_count):null;"` | — |
| [SRC-DE7EABE998-L000237](../../web/agent.html#L237) | 237 | `" const noQualifiedLeads=!!lead&&!leadResearchIncomplete&&leadSignalCount===0;"` | — |
| [SRC-DE7EABE998-L000238](../../web/agent.html#L238) | 238 | `" const scoreLabel=lead?(leadResearchIncomplete?\"تعذر حسم البحث عن العملاء\":noQualifiedLeads?\"لم يُثبت وجود عميل محتمل\":\"إشارات نية شراء مرشحة\"):(researchErrorOutcome?\"تعذر تحديد التغطية\":(e.coverage_level\|\|\"تغطية محدودة\"));"` | — |
| [SRC-DE7EABE998-L000239](../../web/agent.html#L239) | 239 | `" const metrics=lead?["` | — |
| [SRC-DE7EABE998-L000240](../../web/agent.html#L240) | 240 | `"  [leadSignalCount??\"غير محدد\",\"إشارة نصية مرشحة لنية شراء\"],"` | — |
| [SRC-DE7EABE998-L000241](../../web/agent.html#L241) | 241 | `"  [lead.related_results_reviewed??\"غير محدد\",\"نتيجة تمت مراجعتها\"],"` | — |
| [SRC-DE7EABE998-L000242](../../web/agent.html#L242) | 242 | `"  [r.pages_fetched??(leadResearchIncomplete?\"غير محدد\":0),\"صفحة قُرئت\"],"` | — |
| [SRC-DE7EABE998-L000243](../../web/agent.html#L243) | 243 | `"  [leadResearchIncomplete?\"غير محدد\":(e.providers_count??(Array.isArray(r.providers_used)?r.providers_used.length:0)),\"واجهة أسهمت بمصدر صالح\"]"` | — |
| [SRC-DE7EABE998-L000244](../../web/agent.html#L244) | 244 | `" ]:["` | — |
| [SRC-DE7EABE998-L000245](../../web/agent.html#L245) | 245 | `"  [researchErrorOutcome?(r.unique_sources??\"غير محدد\"):(r.unique_sources??sources.length),\"مصدرًا فريدًا\"],"` | — |
| [SRC-DE7EABE998-L000246](../../web/agent.html#L246) | 246 | `"  [researchErrorOutcome?\"غير محدد\":(e.unique_domains??\"—\"),\"نطاقًا مختلفًا\"],"` | — |
| [SRC-DE7EABE998-L000247](../../web/agent.html#L247) | 247 | `"  [researchErrorOutcome?(r.pages_fetched??\"غير محدد\"):(r.pages_fetched??e.pages_read??0),\"صفحة قُرئت\"],"` | — |
| [SRC-DE7EABE998-L000248](../../web/agent.html#L248) | 248 | `"  [researchErrorOutcome?\"غير محدد\":(e.providers_count??(Array.isArray(r.providers_used)?r.providers_used.length:0)),\"واجهة أسهمت بمصدر صالح\"]"` | — |
| [SRC-DE7EABE998-L000249](../../web/agent.html#L249) | 249 | `" ];"` | — |
| [SRC-DE7EABE998-L000250](../../web/agent.html#L250) | 250 | `" const metricHtml=metrics.map(([v,l])=>'<div class=\"metric\"><strong>'+escapeHtml(v)+'</strong><span>'+escapeHtml(l)+'</span></div>').join(\"\");"` | — |
| [SRC-DE7EABE998-L000251](../../web/agent.html#L251) | 251 | `" const operationalMetrics=["` | — |
| [SRC-DE7EABE998-L000252](../../web/agent.html#L252) | 252 | `"  [r.provider_candidates_received??\"غير محدد\",\"مرشح أعاده محرك البحث قبل التصفية (قد يتكرر)\"],"` | — |
| [SRC-DE7EABE998-L000253](../../web/agent.html#L253) | 253 | `"  [r.provider_candidates_accepted??\"غير محدد\",\"مرشح اجتاز فحص الموصل قبل الدمج\"],"` | — |
| [SRC-DE7EABE998-L000254](../../web/agent.html#L254) | 254 | `"  [r.provider_candidates_rejected??\"غير محدد\",\"مرشح رُفض بفحص الرابط أو الصلة\"],"` | — |
| [SRC-DE7EABE998-L000255](../../web/agent.html#L255) | 255 | `"  [r.raw_results??\"غير محدد\",\"نتيجة جُمعت قبل دمج التكرارات\"],"` | — |
| [SRC-DE7EABE998-L000256](../../web/agent.html#L256) | 256 | `"  [r.unique_urls??r.unique_sources??sources.length,\"رابط فريد بعد الدمج\"],"` | — |
| [SRC-DE7EABE998-L000257](../../web/agent.html#L257) | 257 | `"  [r.pages_fetch_attempted??\"غير محدد\",\"محاولة جلب صفحة\"],"` | — |
| [SRC-DE7EABE998-L000258](../../web/agent.html#L258) | 258 | `"  [r.pages_content_extracted??r.pages_fetched??\"غير محدد\",\"صفحة استُخرج منها نص\"],"` | — |
| [SRC-DE7EABE998-L000259](../../web/agent.html#L259) | 259 | `"  [r.pages_partial_extracted??\"غير محدد\",\"صفحة استُخرج جزء من نصها\"],"` | — |
| [SRC-DE7EABE998-L000260](../../web/agent.html#L260) | 260 | `"  [r.pages_extract_failed??\"غير محدد\",\"صفحة فشل استخراج نصها\"]"` | — |
| [SRC-DE7EABE998-L000261](../../web/agent.html#L261) | 261 | `" ];"` | — |
| [SRC-DE7EABE998-L000262](../../web/agent.html#L262) | 262 | `" const operationalHtml='<div class=\"metrics\">'+operationalMetrics.map(([v,l])=>'<div class=\"metric\"><strong>'+escapeHtml(v)+'</strong><span>'+escapeHtml(l)+'</span></div>').join(\"\")+'</div>';"` | — |
| [SRC-DE7EABE998-L000263](../../web/agent.html#L263) | 263 | `" const connectors=r.connector_summary&&Array.isArray(r.connector_summary.connectors)?r.connector_summary.connectors:[];"` | — |
| [SRC-DE7EABE998-L000264](../../web/agent.html#L264) | 264 | `" const connectorDetails=connectors.length?'<details class=\"details\"><summary>تشخيص الموصلات في هذا الطلب ('+connectors.length+')</summary><div>'+connectors.map(c=>'<article class=\"source\"><strong>'+escapeHtml(c.name\|\|\"موصل\")+' · '+escapeHtml(c.status\|\|\"unknown\")+'</strong><p>الإعداد: '+escapeHtml(c.configuration_status\|\|\"unknown\")+' · تمت المحاولة: '+escapeHtml(c.attempted===true?\"نعم\":c.attempted===false?\"لا\":\"غير محسوم\")+' · متاح في هذا الطلب: '+escapeHtml(c.available_for_this_request===true?\"نعم\":c.available_for_this_request===false?\"لا\":\"غير محسوم\")+' · استجابة المعالجة مؤكدة: '+escapeHtml(c.verified_for_this_request===true?\"نعم\":c.verified_for_this_request===false?\"لا\":\"غير مختبر/غير محسوم\")+' · إخفاق ملاحظ: '+escapeHtml(c.failure_observed===true?\"نعم\":\"لا\")+' · مرشحون أوليون من الموصل: '+escapeHtml(c.result_count??\"غير محدد\")+' · اجتازوا فحص الموصل: '+escapeHtml(c.accepted_count??\"غير محدد\")+' · مصادر نهائية منسوبة إليه: '+escapeHtml(c.useful_result_count??\"غير محدد\")+' · مرفوض: '+escapeHtml(c.rejected_count??\"غير محدد\")+' · توزيع الرفض: '+escapeHtml(c.rejection_counts_observed===true&&c.rejection_counts?('مرشح مشوّه '+(c.rejection_counts.malformed_candidate??0)+'؛ رابط غير صالح/هدف غير آمن '+(c.rejection_counts.invalid_url_or_unsafe_target??0)+'؛ نطاق محظور '+(c.rejection_counts.blocked_domain??0)+'؛ صلة ضعيفة '+(c.rejection_counts.relevance_below_threshold??0)):'غير مسجل في هذه الجولة')+' · كل المرشحين رُفضوا: '+escapeHtml(c.candidate_rejection_observed===true?\"نعم\":c.candidate_rejection_observed===false?\"لا\":\"غير محسوم\")+'</p>'+((Array.isArray(c.queries)&&c.queries.length)?'<p>استعلامات: '+c.queries.map(escapeHtml).join(\" · \")+'</p>':\"\")+((Array.isArray(c.errors)&&c.errors.length)?'<p class=\"warning\">أخطاء: '+c.errors.map(escapeHtml).join(\" · \")+'</p>':\"\")+'</article>').join(\"\")+'</div></details>':\"\";"` | — |
| [SRC-DE7EABE998-L000265](../../web/agent.html#L265) | 265 | `" const integrity=r.answer_integrity&&typeof r.answer_integrity===\"object\"?r.answer_integrity:null;"` | — |
| [SRC-DE7EABE998-L000266](../../web/agent.html#L266) | 266 | `" const integrityNumbers=integrity&&Array.isArray(integrity.potentially_unsupported_numeric_literals)?integrity.potentially_unsupported_numeric_literals:[];"` | — |
| [SRC-DE7EABE998-L000267](../../web/agent.html#L267) | 267 | `" const integrityTargets=integrity&&Array.isArray(integrity.target_coverage)?integrity.target_coverage:[];"` | — |
| [SRC-DE7EABE998-L000268](../../web/agent.html#L268) | 268 | `" const requirementEvidence=integrity&&Array.isArray(integrity.requirement_evidence)?integrity.requirement_evidence:[];"` | — |
| [SRC-DE7EABE998-L000269](../../web/agent.html#L269) | 269 | `" const requirementEvidenceHtml=requirementEvidence.length?'<p class=\"report-note\">سجل الأدلة لكل محور — إشارات لفظية وربط استعلامات، وليست إثباتًا لصحة الادعاءات:</p><ul>'+requirementEvidence.map(item=>{const statusText=({candidate_evidence_found_not_verified:\"وُجد نص مرشح مطابق لفظيًا؛ لم تُتحقق دلالته.\",query_returned_candidates_no_lexical_signal:\"عاد الاستعلام بمصادر، لكن لم يظهر تطابق لفظي كافٍ داخل النص.\",no_candidate_evidence_found:\"لم تُسجل أدلة مرشحة لهذا المحور في النتائج المتاحة.\",query_result_linkage_unavailable:\"تعذر ربط النتائج بالاستعلام المخصص لهذا المحور.\",query_not_available:\"لا يوجد استعلام مخصص مسجل لهذا المحور.\"})[item.status]\|\|\"الحالة غير محسومة.\";const ids=Array.isArray(item.candidate_source_indexes)?item.candidate_source_indexes:[];const qids=Array.isArray(item.query_result_source_indexes)?item.query_result_source_indexes:[];return '<li><strong>'+escapeHtml(item.target\|\|\"محور\")+':</strong> '+escapeHtml(statusText)+(ids.length?' — مرشحو الدليل: '+ids.map(n=>\"المصدر \"+escapeHtml(n)).join(\"، \"):\"\")+(qids.length?' — نتائج الاستعلام: '+qids.map(n=>\"المصدر \"+escapeHtml(n)).join(\"، \"):\"\")+'</li>';}).join(\"\")+'</ul>':\"\";"` | — |
| [SRC-DE7EABE998-L000270](../../web/agent.html#L270) | 270 | `" const citationNumericSupport=integrity&&Array.isArray(integrity.citation_numeric_support)?integrity.citation_numeric_support:[];"` | — |
| [SRC-DE7EABE998-L000271](../../web/agent.html#L271) | 271 | `" const citedNumberIssues=citationNumericSupport.filter(item=>item&&Array.isArray(item.potentially_unsupported_numeric_literals)&&item.potentially_unsupported_numeric_literals.length);"` | — |
