# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **041**
- سجلات الأسطر: **800**
- النطاق: SRC-829A979985-L000602 إلى SRC-EA6EC52573-L000150
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-829A979985 — [tests/test_generation_acceptance_matrix.py](../../tests/test_generation_acceptance_matrix.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-829A979985-L000602](../../tests/test_generation_acceptance_matrix.py#L602) | 602 | `"    agent = WebAgent()"` | — |
| [SRC-829A979985-L000603](../../tests/test_generation_acceptance_matrix.py#L603) | 603 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000604](../../tests/test_generation_acceptance_matrix.py#L604) | 604 | `"        agent,"` | — |
| [SRC-829A979985-L000605](../../tests/test_generation_acceptance_matrix.py#L605) | 605 | `"        \"_request_completion\","` | — |
| [SRC-829A979985-L000606](../../tests/test_generation_acceptance_matrix.py#L606) | 606 | `"        lambda *args, **kwargs: malformed_review,"` | — |
| [SRC-829A979985-L000607](../../tests/test_generation_acceptance_matrix.py#L607) | 607 | `"    )"` | — |
| [SRC-829A979985-L000608](../../tests/test_generation_acceptance_matrix.py#L608) | 608 | `"    test_source = source("` | — |
| [SRC-829A979985-L000609](../../tests/test_generation_acceptance_matrix.py#L609) | 609 | `"        \"https://one.example/page\","` | — |
| [SRC-829A979985-L000610](../../tests/test_generation_acceptance_matrix.py#L610) | 610 | `"        \"one.example\","` | — |
| [SRC-829A979985-L000611](../../tests/test_generation_acceptance_matrix.py#L611) | 611 | `"        page_fetched=True,"` | — |
| [SRC-829A979985-L000612](../../tests/test_generation_acceptance_matrix.py#L612) | 612 | `"        page_text=\"نص الصفحة\","` | — |
| [SRC-829A979985-L000613](../../tests/test_generation_acceptance_matrix.py#L613) | 613 | `"    )"` | — |
| [SRC-829A979985-L000614](../../tests/test_generation_acceptance_matrix.py#L614) | 614 | `""` | — |
| [SRC-829A979985-L000615](../../tests/test_generation_acceptance_matrix.py#L615) | 615 | `"    with pytest.raises(RuntimeError, match=\"فصل الإجابة النهائية\"):"` | — |
| [SRC-829A979985-L000616](../../tests/test_generation_acceptance_matrix.py#L616) | 616 | `"        agent._review_answer(\"ما مضمون الصفحة؟\", \"مسودة\", [test_source])"` | — |
## اختبارات

### FILE-AAA21D04E8 — [tests/test_generation_capabilities.py](../../tests/test_generation_capabilities.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-AAA21D04E8-L000001](../../tests/test_generation_capabilities.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-AAA21D04E8-L000002](../../tests/test_generation_capabilities.py#L2) | 2 | `""` | — |
| [SRC-AAA21D04E8-L000003](../../tests/test_generation_capabilities.py#L3) | 3 | `"import json"` | — |
| [SRC-AAA21D04E8-L000004](../../tests/test_generation_capabilities.py#L4) | 4 | `""` | — |
| [SRC-AAA21D04E8-L000005](../../tests/test_generation_capabilities.py#L5) | 5 | `"import pytest"` | — |
| [SRC-AAA21D04E8-L000006](../../tests/test_generation_capabilities.py#L6) | 6 | `""` | — |
| [SRC-AAA21D04E8-L000007](../../tests/test_generation_capabilities.py#L7) | 7 | `"from agents.web_agent import WebAgent"` | — |
| [SRC-AAA21D04E8-L000008](../../tests/test_generation_capabilities.py#L8) | 8 | `""` | — |
| [SRC-AAA21D04E8-L000009](../../tests/test_generation_capabilities.py#L9) | 9 | `""` | — |
| [SRC-AAA21D04E8-L000010](../../tests/test_generation_capabilities.py#L10) | 10 | `"class FakeResponse:"` | — |
| [SRC-AAA21D04E8-L000011](../../tests/test_generation_capabilities.py#L11) | 11 | `"    def __init__(self, content: str, finish_reason: str \| None = None, *, include_reason: bool = True):"` | — |
| [SRC-AAA21D04E8-L000012](../../tests/test_generation_capabilities.py#L12) | 12 | `"        choice = {\"message\": {\"content\": content}}"` | — |
| [SRC-AAA21D04E8-L000013](../../tests/test_generation_capabilities.py#L13) | 13 | `"        if include_reason:"` | — |
| [SRC-AAA21D04E8-L000014](../../tests/test_generation_capabilities.py#L14) | 14 | `"            choice[\"finish_reason\"] = finish_reason"` | — |
| [SRC-AAA21D04E8-L000015](../../tests/test_generation_capabilities.py#L15) | 15 | `"        self.body = json.dumps({\"choices\": [choice]}).encode(\"utf-8\")"` | — |
| [SRC-AAA21D04E8-L000016](../../tests/test_generation_capabilities.py#L16) | 16 | `""` | — |
| [SRC-AAA21D04E8-L000017](../../tests/test_generation_capabilities.py#L17) | 17 | `"    def __enter__(self):"` | — |
| [SRC-AAA21D04E8-L000018](../../tests/test_generation_capabilities.py#L18) | 18 | `"        return self"` | — |
| [SRC-AAA21D04E8-L000019](../../tests/test_generation_capabilities.py#L19) | 19 | `""` | — |
| [SRC-AAA21D04E8-L000020](../../tests/test_generation_capabilities.py#L20) | 20 | `"    def __exit__(self, exc_type, exc, traceback):"` | — |
| [SRC-AAA21D04E8-L000021](../../tests/test_generation_capabilities.py#L21) | 21 | `"        return False"` | — |
| [SRC-AAA21D04E8-L000022](../../tests/test_generation_capabilities.py#L22) | 22 | `""` | — |
| [SRC-AAA21D04E8-L000023](../../tests/test_generation_capabilities.py#L23) | 23 | `"    def read(self, limit: int) -> bytes:"` | — |
| [SRC-AAA21D04E8-L000024](../../tests/test_generation_capabilities.py#L24) | 24 | `"        return self.body[:limit]"` | — |
| [SRC-AAA21D04E8-L000025](../../tests/test_generation_capabilities.py#L25) | 25 | `""` | — |
| [SRC-AAA21D04E8-L000026](../../tests/test_generation_capabilities.py#L26) | 26 | `""` | — |
| [SRC-AAA21D04E8-L000027](../../tests/test_generation_capabilities.py#L27) | 27 | `"def test_missing_finish_reason_is_rejected_and_bounded_fallback_is_used(monkeypatch):"` | — |
| [SRC-AAA21D04E8-L000028](../../tests/test_generation_capabilities.py#L28) | 28 | `"    agent = WebAgent()"` | — |
| [SRC-AAA21D04E8-L000029](../../tests/test_generation_capabilities.py#L29) | 29 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-AAA21D04E8-L000030](../../tests/test_generation_capabilities.py#L30) | 30 | `"    agent.fallback_model = \"backup/model\""` | — |
| [SRC-AAA21D04E8-L000031](../../tests/test_generation_capabilities.py#L31) | 31 | `"    calls: list[str] = []"` | — |
| [SRC-AAA21D04E8-L000032](../../tests/test_generation_capabilities.py#L32) | 32 | `""` | — |
| [SRC-AAA21D04E8-L000033](../../tests/test_generation_capabilities.py#L33) | 33 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-AAA21D04E8-L000034](../../tests/test_generation_capabilities.py#L34) | 34 | `"        model = json.loads(request.data.decode(\"utf-8\"))[\"model\"]"` | — |
| [SRC-AAA21D04E8-L000035](../../tests/test_generation_capabilities.py#L35) | 35 | `"        calls.append(model)"` | — |
| [SRC-AAA21D04E8-L000036](../../tests/test_generation_capabilities.py#L36) | 36 | `"        if model == \"primary/model\":"` | — |
| [SRC-AAA21D04E8-L000037](../../tests/test_generation_capabilities.py#L37) | 37 | `"            return FakeResponse(\"possibly incomplete response\", include_reason=False)"` | — |
| [SRC-AAA21D04E8-L000038](../../tests/test_generation_capabilities.py#L38) | 38 | `"        return FakeResponse(\"إجابة مكتملة من النموذج الاحتياطي\", \"stop\")"` | — |
| [SRC-AAA21D04E8-L000039](../../tests/test_generation_capabilities.py#L39) | 39 | `""` | — |
| [SRC-AAA21D04E8-L000040](../../tests/test_generation_capabilities.py#L40) | 40 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-AAA21D04E8-L000041](../../tests/test_generation_capabilities.py#L41) | 41 | `""` | — |
| [SRC-AAA21D04E8-L000042](../../tests/test_generation_capabilities.py#L42) | 42 | `"    answer = agent._request_completion("` | — |
| [SRC-AAA21D04E8-L000043](../../tests/test_generation_capabilities.py#L43) | 43 | `"        [{\"role\": \"user\", \"content\": \"اختبار\"}],"` | — |
| [SRC-AAA21D04E8-L000044](../../tests/test_generation_capabilities.py#L44) | 44 | `"        model=\"primary/model\","` | — |
| [SRC-AAA21D04E8-L000045](../../tests/test_generation_capabilities.py#L45) | 45 | `"    )"` | — |
| [SRC-AAA21D04E8-L000046](../../tests/test_generation_capabilities.py#L46) | 46 | `""` | — |
| [SRC-AAA21D04E8-L000047](../../tests/test_generation_capabilities.py#L47) | 47 | `"    assert answer == \"إجابة مكتملة من النموذج الاحتياطي\""` | — |
| [SRC-AAA21D04E8-L000048](../../tests/test_generation_capabilities.py#L48) | 48 | `"    assert calls == [\"primary/model\", \"backup/model\"]"` | — |
| [SRC-AAA21D04E8-L000049](../../tests/test_generation_capabilities.py#L49) | 49 | `"    assert [item[\"status\"] for item in agent.generation_diagnostics] == ["` | — |
| [SRC-AAA21D04E8-L000050](../../tests/test_generation_capabilities.py#L50) | 50 | `"        \"finish_reason_missing\","` | — |
| [SRC-AAA21D04E8-L000051](../../tests/test_generation_capabilities.py#L51) | 51 | `"        \"accepted\","` | — |
| [SRC-AAA21D04E8-L000052](../../tests/test_generation_capabilities.py#L52) | 52 | `"    ]"` | — |
| [SRC-AAA21D04E8-L000053](../../tests/test_generation_capabilities.py#L53) | 53 | `"    assert agent.generation_diagnostics[0][\"attempted_model\"] == \"primary/model\""` | — |
| [SRC-AAA21D04E8-L000054](../../tests/test_generation_capabilities.py#L54) | 54 | `"    assert agent.generation_diagnostics[1][\"attempted_model\"] == \"backup/model\""` | — |
| [SRC-AAA21D04E8-L000055](../../tests/test_generation_capabilities.py#L55) | 55 | `"    assert [item[\"attempt_number\"] for item in agent.generation_diagnostics] == [1, 2]"` | — |
| [SRC-AAA21D04E8-L000056](../../tests/test_generation_capabilities.py#L56) | 56 | `"    assert [item[\"fallback_used\"] for item in agent.generation_diagnostics] == [False, True]"` | — |
| [SRC-AAA21D04E8-L000057](../../tests/test_generation_capabilities.py#L57) | 57 | `"    assert all(item[\"request_started\"] is True for item in agent.generation_diagnostics)"` | — |
| [SRC-AAA21D04E8-L000058](../../tests/test_generation_capabilities.py#L58) | 58 | `"    assert all(item[\"remote_response_received\"] is True for item in agent.generation_diagnostics)"` | — |
| [SRC-AAA21D04E8-L000059](../../tests/test_generation_capabilities.py#L59) | 59 | `""` | — |
| [SRC-AAA21D04E8-L000060](../../tests/test_generation_capabilities.py#L60) | 60 | `""` | — |
| [SRC-AAA21D04E8-L000061](../../tests/test_generation_capabilities.py#L61) | 61 | `"def test_unknown_finish_reason_is_rejected_and_fallback_is_used(monkeypatch):"` | — |
| [SRC-AAA21D04E8-L000062](../../tests/test_generation_capabilities.py#L62) | 62 | `"    agent = WebAgent()"` | — |
| [SRC-AAA21D04E8-L000063](../../tests/test_generation_capabilities.py#L63) | 63 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-AAA21D04E8-L000064](../../tests/test_generation_capabilities.py#L64) | 64 | `"    agent.fallback_model = \"backup/model\""` | — |
| [SRC-AAA21D04E8-L000065](../../tests/test_generation_capabilities.py#L65) | 65 | `"    calls: list[str] = []"` | — |
| [SRC-AAA21D04E8-L000066](../../tests/test_generation_capabilities.py#L66) | 66 | `""` | — |
| [SRC-AAA21D04E8-L000067](../../tests/test_generation_capabilities.py#L67) | 67 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-AAA21D04E8-L000068](../../tests/test_generation_capabilities.py#L68) | 68 | `"        model = json.loads(request.data.decode(\"utf-8\"))[\"model\"]"` | — |
| [SRC-AAA21D04E8-L000069](../../tests/test_generation_capabilities.py#L69) | 69 | `"        calls.append(model)"` | — |
| [SRC-AAA21D04E8-L000070](../../tests/test_generation_capabilities.py#L70) | 70 | `"        if model == \"primary/model\":"` | — |
| [SRC-AAA21D04E8-L000071](../../tests/test_generation_capabilities.py#L71) | 71 | `"            return FakeResponse(\"response with unrecognized termination\", \"vendor_specific_done\")"` | — |
| [SRC-AAA21D04E8-L000072](../../tests/test_generation_capabilities.py#L72) | 72 | `"        return FakeResponse(\"إجابة مكتملة\", \"stop\")"` | — |
| [SRC-AAA21D04E8-L000073](../../tests/test_generation_capabilities.py#L73) | 73 | `""` | — |
| [SRC-AAA21D04E8-L000074](../../tests/test_generation_capabilities.py#L74) | 74 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-AAA21D04E8-L000075](../../tests/test_generation_capabilities.py#L75) | 75 | `""` | — |
| [SRC-AAA21D04E8-L000076](../../tests/test_generation_capabilities.py#L76) | 76 | `"    answer = agent._request_completion("` | — |
| [SRC-AAA21D04E8-L000077](../../tests/test_generation_capabilities.py#L77) | 77 | `"        [{\"role\": \"user\", \"content\": \"اختبار\"}],"` | — |
| [SRC-AAA21D04E8-L000078](../../tests/test_generation_capabilities.py#L78) | 78 | `"        model=\"primary/model\","` | — |
| [SRC-AAA21D04E8-L000079](../../tests/test_generation_capabilities.py#L79) | 79 | `"    )"` | — |
| [SRC-AAA21D04E8-L000080](../../tests/test_generation_capabilities.py#L80) | 80 | `""` | — |
| [SRC-AAA21D04E8-L000081](../../tests/test_generation_capabilities.py#L81) | 81 | `"    assert answer == \"إجابة مكتملة\""` | — |
| [SRC-AAA21D04E8-L000082](../../tests/test_generation_capabilities.py#L82) | 82 | `"    assert calls == [\"primary/model\", \"backup/model\"]"` | — |
| [SRC-AAA21D04E8-L000083](../../tests/test_generation_capabilities.py#L83) | 83 | `"    assert agent.generation_diagnostics[0][\"status\"] == \"finish_reason_not_accepted\""` | — |
| [SRC-AAA21D04E8-L000084](../../tests/test_generation_capabilities.py#L84) | 84 | `"    assert agent.generation_diagnostics[0][\"finish_reason\"] == \"vendor_specific_done\""` | — |
| [SRC-AAA21D04E8-L000085](../../tests/test_generation_capabilities.py#L85) | 85 | `""` | — |
| [SRC-AAA21D04E8-L000086](../../tests/test_generation_capabilities.py#L86) | 86 | `""` | — |
| [SRC-AAA21D04E8-L000087](../../tests/test_generation_capabilities.py#L87) | 87 | `"def test_missing_finish_reason_from_all_models_fails_closed(monkeypatch):"` | — |
| [SRC-AAA21D04E8-L000088](../../tests/test_generation_capabilities.py#L88) | 88 | `"    agent = WebAgent()"` | — |
| [SRC-AAA21D04E8-L000089](../../tests/test_generation_capabilities.py#L89) | 89 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-AAA21D04E8-L000090](../../tests/test_generation_capabilities.py#L90) | 90 | `"    agent.fallback_model = \"\""` | — |
| [SRC-AAA21D04E8-L000091](../../tests/test_generation_capabilities.py#L91) | 91 | `"    calls: list[str] = []"` | — |
| [SRC-AAA21D04E8-L000092](../../tests/test_generation_capabilities.py#L92) | 92 | `""` | — |
| [SRC-AAA21D04E8-L000093](../../tests/test_generation_capabilities.py#L93) | 93 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-AAA21D04E8-L000094](../../tests/test_generation_capabilities.py#L94) | 94 | `"        calls.append(json.loads(request.data.decode(\"utf-8\"))[\"model\"])"` | — |
| [SRC-AAA21D04E8-L000095](../../tests/test_generation_capabilities.py#L95) | 95 | `"        return FakeResponse(\"may be incomplete\", include_reason=False)"` | — |
| [SRC-AAA21D04E8-L000096](../../tests/test_generation_capabilities.py#L96) | 96 | `""` | — |
| [SRC-AAA21D04E8-L000097](../../tests/test_generation_capabilities.py#L97) | 97 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-AAA21D04E8-L000098](../../tests/test_generation_capabilities.py#L98) | 98 | `""` | — |
| [SRC-AAA21D04E8-L000099](../../tests/test_generation_capabilities.py#L99) | 99 | `"    with pytest.raises(RuntimeError, match=\"سبب انتهاء واضحًا\"):"` | — |
| [SRC-AAA21D04E8-L000100](../../tests/test_generation_capabilities.py#L100) | 100 | `"        agent._request_completion("` | — |
| [SRC-AAA21D04E8-L000101](../../tests/test_generation_capabilities.py#L101) | 101 | `"            [{\"role\": \"user\", \"content\": \"اختبار\"}],"` | — |
| [SRC-AAA21D04E8-L000102](../../tests/test_generation_capabilities.py#L102) | 102 | `"            model=\"primary/model\","` | — |
| [SRC-AAA21D04E8-L000103](../../tests/test_generation_capabilities.py#L103) | 103 | `"        )"` | — |
| [SRC-AAA21D04E8-L000104](../../tests/test_generation_capabilities.py#L104) | 104 | `""` | — |
| [SRC-AAA21D04E8-L000105](../../tests/test_generation_capabilities.py#L105) | 105 | `"    assert calls == [\"primary/model\"]"` | — |
| [SRC-AAA21D04E8-L000106](../../tests/test_generation_capabilities.py#L106) | 106 | `"    assert agent.model_usage == []"` | — |
| [SRC-AAA21D04E8-L000107](../../tests/test_generation_capabilities.py#L107) | 107 | `"    assert agent.generation_diagnostics == [{"` | — |
| [SRC-AAA21D04E8-L000108](../../tests/test_generation_capabilities.py#L108) | 108 | `"        \"attempt_number\": 1,"` | — |
| [SRC-AAA21D04E8-L000109](../../tests/test_generation_capabilities.py#L109) | 109 | `"        \"requested_model\": \"primary/model\","` | — |
| [SRC-AAA21D04E8-L000110](../../tests/test_generation_capabilities.py#L110) | 110 | `"        \"attempted_model\": \"primary/model\","` | — |
| [SRC-AAA21D04E8-L000111](../../tests/test_generation_capabilities.py#L111) | 111 | `"        \"fallback_used\": False,"` | — |
| [SRC-AAA21D04E8-L000112](../../tests/test_generation_capabilities.py#L112) | 112 | `"        \"request_started\": True,"` | — |
| [SRC-AAA21D04E8-L000113](../../tests/test_generation_capabilities.py#L113) | 113 | `"        \"remote_response_received\": True,"` | — |
| [SRC-AAA21D04E8-L000114](../../tests/test_generation_capabilities.py#L114) | 114 | `"        \"status\": \"finish_reason_missing\","` | — |
| [SRC-AAA21D04E8-L000115](../../tests/test_generation_capabilities.py#L115) | 115 | `"    }]"` | — |
| [SRC-AAA21D04E8-L000116](../../tests/test_generation_capabilities.py#L116) | 116 | `""` | — |
| [SRC-AAA21D04E8-L000117](../../tests/test_generation_capabilities.py#L117) | 117 | `""` | — |
| [SRC-AAA21D04E8-L000118](../../tests/test_generation_capabilities.py#L118) | 118 | `"def test_capability_question_distinguishes_configuration_from_live_health(monkeypatch):"` | — |
| [SRC-AAA21D04E8-L000119](../../tests/test_generation_capabilities.py#L119) | 119 | `"    agent = WebAgent()"` | — |
| [SRC-AAA21D04E8-L000120](../../tests/test_generation_capabilities.py#L120) | 120 | `""` | — |
| [SRC-AAA21D04E8-L000121](../../tests/test_generation_capabilities.py#L121) | 121 | `"    monkeypatch.setattr("` | — |
| [SRC-AAA21D04E8-L000122](../../tests/test_generation_capabilities.py#L122) | 122 | `"        agent,"` | — |
| [SRC-AAA21D04E8-L000123](../../tests/test_generation_capabilities.py#L123) | 123 | `"        \"_collect_research\","` | — |
| [SRC-AAA21D04E8-L000124](../../tests/test_generation_capabilities.py#L124) | 124 | `"        lambda plan: pytest.fail(\"Capability questions must not run live search\"),"` | — |
| [SRC-AAA21D04E8-L000125](../../tests/test_generation_capabilities.py#L125) | 125 | `"    )"` | — |
| [SRC-AAA21D04E8-L000126](../../tests/test_generation_capabilities.py#L126) | 126 | `""` | — |
| [SRC-AAA21D04E8-L000127](../../tests/test_generation_capabilities.py#L127) | 127 | `"    result = agent.answer(\"هل تستطيع البحث على الانترنت؟\")"` | — |
| [SRC-AAA21D04E8-L000128](../../tests/test_generation_capabilities.py#L128) | 128 | `""` | — |
| [SRC-AAA21D04E8-L000129](../../tests/test_generation_capabilities.py#L129) | 129 | `"    assert result[\"kind\"] == \"capability_answer\""` | — |
| [SRC-AAA21D04E8-L000130](../../tests/test_generation_capabilities.py#L130) | 130 | `"    assert result[\"final_answer_status\"] == \"local_response_no_generation\""` | — |
| [SRC-AAA21D04E8-L000131](../../tests/test_generation_capabilities.py#L131) | 131 | `"    assert result[\"search_attempted\"] is False"` | — |
| [SRC-AAA21D04E8-L000132](../../tests/test_generation_capabilities.py#L132) | 132 | `"    assert result[\"used_web_search\"] is False"` | — |
| [SRC-AAA21D04E8-L000133](../../tests/test_generation_capabilities.py#L133) | 133 | `"    capability = result[\"capability_status\"][\"web_search\"]"` | — |
| [SRC-AAA21D04E8-L000134](../../tests/test_generation_capabilities.py#L134) | 134 | `"    assert capability[\"implemented\"] is True"` | — |
| [SRC-AAA21D04E8-L000135](../../tests/test_generation_capabilities.py#L135) | 135 | `"    assert capability[\"runtime_status\"] == \"not_tested_in_this_response\""` | — |
| [SRC-AAA21D04E8-L000136](../../tests/test_generation_capabilities.py#L136) | 136 | `"    assert capability[\"local_dependencies_ready\"] is True"` | — |
| [SRC-AAA21D04E8-L000137](../../tests/test_generation_capabilities.py#L137) | 137 | `"    assert \"لم أنفّذ اختبار اتصال حي\" in result[\"answer\"]"` | — |
| [SRC-AAA21D04E8-L000138](../../tests/test_generation_capabilities.py#L138) | 138 | `"    assert \"DuckDuckGo HTML\" in result[\"answer\"]"` | — |
| [SRC-AAA21D04E8-L000139](../../tests/test_generation_capabilities.py#L139) | 139 | `""` | — |
| [SRC-AAA21D04E8-L000140](../../tests/test_generation_capabilities.py#L140) | 140 | `""` | — |
| [SRC-AAA21D04E8-L000141](../../tests/test_generation_capabilities.py#L141) | 141 | `"@pytest.mark.parametrize(\"mode\", [\"auto\", \"deep\", \"latest\", \"social\"])"` | — |
| [SRC-AAA21D04E8-L000142](../../tests/test_generation_capabilities.py#L142) | 142 | `"def test_current_request_search_status_is_not_confused_with_capability(monkeypatch, mode):"` | — |
| [SRC-AAA21D04E8-L000143](../../tests/test_generation_capabilities.py#L143) | 143 | `"    agent = WebAgent()"` | — |
| [SRC-AAA21D04E8-L000144](../../tests/test_generation_capabilities.py#L144) | 144 | `"    monkeypatch.setattr("` | — |
| [SRC-AAA21D04E8-L000145](../../tests/test_generation_capabilities.py#L145) | 145 | `"        agent,"` | — |
| [SRC-AAA21D04E8-L000146](../../tests/test_generation_capabilities.py#L146) | 146 | `"        \"_collect_research\","` | — |
| [SRC-AAA21D04E8-L000147](../../tests/test_generation_capabilities.py#L147) | 147 | `"        lambda plan: pytest.fail(\"This asks about the current response, not a web lookup\"),"` | — |
| [SRC-AAA21D04E8-L000148](../../tests/test_generation_capabilities.py#L148) | 148 | `"    )"` | — |
| [SRC-AAA21D04E8-L000149](../../tests/test_generation_capabilities.py#L149) | 149 | `""` | — |
| [SRC-AAA21D04E8-L000150](../../tests/test_generation_capabilities.py#L150) | 150 | `"    result = agent.answer(\"هل بحثت في الانترنت للاجابة الحالية؟\", mode=mode)"` | — |
| [SRC-AAA21D04E8-L000151](../../tests/test_generation_capabilities.py#L151) | 151 | `""` | — |
| [SRC-AAA21D04E8-L000152](../../tests/test_generation_capabilities.py#L152) | 152 | `"    assert result[\"kind\"] == \"capability_answer\""` | — |
| [SRC-AAA21D04E8-L000153](../../tests/test_generation_capabilities.py#L153) | 153 | `"    assert result[\"request_execution_status\"] == {"` | — |
| [SRC-AAA21D04E8-L000154](../../tests/test_generation_capabilities.py#L154) | 154 | `"        \"search_attempted\": False,"` | — |
| [SRC-AAA21D04E8-L000155](../../tests/test_generation_capabilities.py#L155) | 155 | `"        \"search_outcome\": \"not_attempted\","` | — |
| [SRC-AAA21D04E8-L000156](../../tests/test_generation_capabilities.py#L156) | 156 | `"        \"semantics\": \"status_of_this_request_only\","` | — |
| [SRC-AAA21D04E8-L000157](../../tests/test_generation_capabilities.py#L157) | 157 | `"    }"` | — |
| [SRC-AAA21D04E8-L000158](../../tests/test_generation_capabilities.py#L158) | 158 | `"    assert \"لم أنفّذ بحثًا حيًا للإجابة عن هذا السؤال تحديدًا\" in result[\"answer\"]"` | — |
| [SRC-AAA21D04E8-L000159](../../tests/test_generation_capabilities.py#L159) | 159 | `"    assert result[\"capability_status\"][\"web_search\"][\"runtime_status\"] == ("` | — |
| [SRC-AAA21D04E8-L000160](../../tests/test_generation_capabilities.py#L160) | 160 | `"        \"not_tested_in_this_response\""` | — |
| [SRC-AAA21D04E8-L000161](../../tests/test_generation_capabilities.py#L161) | 161 | `"    )"` | — |
| [SRC-AAA21D04E8-L000162](../../tests/test_generation_capabilities.py#L162) | 162 | `"    assert result[\"search_attempted\"] is False"` | — |
| [SRC-AAA21D04E8-L000163](../../tests/test_generation_capabilities.py#L163) | 163 | `""` | — |
| [SRC-AAA21D04E8-L000164](../../tests/test_generation_capabilities.py#L164) | 164 | `""` | — |
| [SRC-AAA21D04E8-L000165](../../tests/test_generation_capabilities.py#L165) | 165 | `"def test_generation_failure_returns_partial_sources_and_diagnostics(monkeypatch):"` | — |
| [SRC-AAA21D04E8-L000166](../../tests/test_generation_capabilities.py#L166) | 166 | `"    agent = WebAgent()"` | — |
| [SRC-AAA21D04E8-L000167](../../tests/test_generation_capabilities.py#L167) | 167 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-AAA21D04E8-L000168](../../tests/test_generation_capabilities.py#L168) | 168 | `"    question = \"ابحث عن أحدث تقرير عن الذكاء الاصطناعي\""` | — |
| [SRC-AAA21D04E8-L000169](../../tests/test_generation_capabilities.py#L169) | 169 | `""` | — |
| [SRC-AAA21D04E8-L000170](../../tests/test_generation_capabilities.py#L170) | 170 | `"    sources = ["` | — |
| [SRC-AAA21D04E8-L000171](../../tests/test_generation_capabilities.py#L171) | 171 | `"        {"` | — |
| [SRC-AAA21D04E8-L000172](../../tests/test_generation_capabilities.py#L172) | 172 | `"            \"title\": \"تقرير ذكاء اصطناعي\","` | — |
| [SRC-AAA21D04E8-L000173](../../tests/test_generation_capabilities.py#L173) | 173 | `"            \"url\": \"https://example.com/report\","` | — |
| [SRC-AAA21D04E8-L000174](../../tests/test_generation_capabilities.py#L174) | 174 | `"            \"snippet\": \"مقتطف تجريبي من المصدر الأول\","` | — |
| [SRC-AAA21D04E8-L000175](../../tests/test_generation_capabilities.py#L175) | 175 | `"            \"page_fetched\": False,"` | — |
| [SRC-AAA21D04E8-L000176](../../tests/test_generation_capabilities.py#L176) | 176 | `"            \"providers\": [\"duckduckgo_html\"],"` | — |
| [SRC-AAA21D04E8-L000177](../../tests/test_generation_capabilities.py#L177) | 177 | `"            \"queries\": [question],"` | — |
| [SRC-AAA21D04E8-L000178](../../tests/test_generation_capabilities.py#L178) | 178 | `"            \"domain\": \"example.com\","` | — |
| [SRC-AAA21D04E8-L000179](../../tests/test_generation_capabilities.py#L179) | 179 | `"            \"source_class\": \"general\","` | — |
| [SRC-AAA21D04E8-L000180](../../tests/test_generation_capabilities.py#L180) | 180 | `"            \"platform\": \"web\","` | — |
| [SRC-AAA21D04E8-L000181](../../tests/test_generation_capabilities.py#L181) | 181 | `"            \"published_at\": \"\","` | — |
| [SRC-AAA21D04E8-L000182](../../tests/test_generation_capabilities.py#L182) | 182 | `"            \"rank_score\": 0.9,"` | — |
| [SRC-AAA21D04E8-L000183](../../tests/test_generation_capabilities.py#L183) | 183 | `"        },"` | — |
| [SRC-AAA21D04E8-L000184](../../tests/test_generation_capabilities.py#L184) | 184 | `"        {"` | — |
| [SRC-AAA21D04E8-L000185](../../tests/test_generation_capabilities.py#L185) | 185 | `"            \"title\": \"مصدر ثان\","` | — |
| [SRC-AAA21D04E8-L000186](../../tests/test_generation_capabilities.py#L186) | 186 | `"            \"url\": \"https://example.net/report\","` | — |
| [SRC-AAA21D04E8-L000187](../../tests/test_generation_capabilities.py#L187) | 187 | `"            \"snippet\": \"مقتطف تجريبي من المصدر الثاني\","` | — |
| [SRC-AAA21D04E8-L000188](../../tests/test_generation_capabilities.py#L188) | 188 | `"            \"page_fetched\": False,"` | — |
| [SRC-AAA21D04E8-L000189](../../tests/test_generation_capabilities.py#L189) | 189 | `"            \"providers\": [\"bing_rss\"],"` | — |
| [SRC-AAA21D04E8-L000190](../../tests/test_generation_capabilities.py#L190) | 190 | `"            \"queries\": [question],"` | — |
| [SRC-AAA21D04E8-L000191](../../tests/test_generation_capabilities.py#L191) | 191 | `"            \"domain\": \"example.net\","` | — |
| [SRC-AAA21D04E8-L000192](../../tests/test_generation_capabilities.py#L192) | 192 | `"            \"source_class\": \"general\","` | — |
| [SRC-AAA21D04E8-L000193](../../tests/test_generation_capabilities.py#L193) | 193 | `"            \"platform\": \"web\","` | — |
| [SRC-AAA21D04E8-L000194](../../tests/test_generation_capabilities.py#L194) | 194 | `"            \"published_at\": \"\","` | — |
| [SRC-AAA21D04E8-L000195](../../tests/test_generation_capabilities.py#L195) | 195 | `"            \"rank_score\": 0.8,"` | — |
| [SRC-AAA21D04E8-L000196](../../tests/test_generation_capabilities.py#L196) | 196 | `"        },"` | — |
| [SRC-AAA21D04E8-L000197](../../tests/test_generation_capabilities.py#L197) | 197 | `"    ]"` | — |
| [SRC-AAA21D04E8-L000198](../../tests/test_generation_capabilities.py#L198) | 198 | `""` | — |
| [SRC-AAA21D04E8-L000199](../../tests/test_generation_capabilities.py#L199) | 199 | `"    monkeypatch.setattr("` | — |
| [SRC-AAA21D04E8-L000200](../../tests/test_generation_capabilities.py#L200) | 200 | `"        agent,"` | — |
| [SRC-AAA21D04E8-L000201](../../tests/test_generation_capabilities.py#L201) | 201 | `"        \"_plan_search\","` | — |
| [SRC-AAA21D04E8-L000202](../../tests/test_generation_capabilities.py#L202) | 202 | `"        lambda question, history: {"` | — |
| [SRC-AAA21D04E8-L000203](../../tests/test_generation_capabilities.py#L203) | 203 | `"            \"queries\": [question],"` | — |
| [SRC-AAA21D04E8-L000204](../../tests/test_generation_capabilities.py#L204) | 204 | `"            \"depth\": \"standard\","` | — |
| [SRC-AAA21D04E8-L000205](../../tests/test_generation_capabilities.py#L205) | 205 | `"            \"freshness\": \"any\","` | — |
| [SRC-AAA21D04E8-L000206](../../tests/test_generation_capabilities.py#L206) | 206 | `"            \"social_focus\": False,"` | — |
| [SRC-AAA21D04E8-L000207](../../tests/test_generation_capabilities.py#L207) | 207 | `"            \"platforms\": [],"` | — |
| [SRC-AAA21D04E8-L000208](../../tests/test_generation_capabilities.py#L208) | 208 | `"            \"planning_method\": \"test_fixture\","` | — |
| [SRC-AAA21D04E8-L000209](../../tests/test_generation_capabilities.py#L209) | 209 | `"            \"direct_urls\": [],"` | — |
| [SRC-AAA21D04E8-L000210](../../tests/test_generation_capabilities.py#L210) | 210 | `"        },"` | — |
| [SRC-AAA21D04E8-L000211](../../tests/test_generation_capabilities.py#L211) | 211 | `"    )"` | — |
| [SRC-AAA21D04E8-L000212](../../tests/test_generation_capabilities.py#L212) | 212 | `"    monkeypatch.setattr("` | — |
| [SRC-AAA21D04E8-L000213](../../tests/test_generation_capabilities.py#L213) | 213 | `"        agent,"` | — |
| [SRC-AAA21D04E8-L000214](../../tests/test_generation_capabilities.py#L214) | 214 | `"        \"_collect_research\","` | — |
| [SRC-AAA21D04E8-L000215](../../tests/test_generation_capabilities.py#L215) | 215 | `"        lambda plan: ("` | — |
| [SRC-AAA21D04E8-L000216](../../tests/test_generation_capabilities.py#L216) | 216 | `"            sources,"` | — |
| [SRC-AAA21D04E8-L000217](../../tests/test_generation_capabilities.py#L217) | 217 | `"            [],"` | — |
| [SRC-AAA21D04E8-L000218](../../tests/test_generation_capabilities.py#L218) | 218 | `"            {"` | — |
| [SRC-AAA21D04E8-L000219](../../tests/test_generation_capabilities.py#L219) | 219 | `"                \"queries_planned\": 1,"` | — |
| [SRC-AAA21D04E8-L000220](../../tests/test_generation_capabilities.py#L220) | 220 | `"                \"queries_attempted\": 1,"` | — |
| [SRC-AAA21D04E8-L000221](../../tests/test_generation_capabilities.py#L221) | 221 | `"                \"queries_attempted_known\": True,"` | — |
| [SRC-AAA21D04E8-L000222](../../tests/test_generation_capabilities.py#L222) | 222 | `"                \"search_attempted\": True,"` | — |
| [SRC-AAA21D04E8-L000223](../../tests/test_generation_capabilities.py#L223) | 223 | `"                \"search_outcome\": \"attempted_with_usable_sources\","` | — |
| [SRC-AAA21D04E8-L000224](../../tests/test_generation_capabilities.py#L224) | 224 | `"                \"unique_sources\": 2,"` | — |
| [SRC-AAA21D04E8-L000225](../../tests/test_generation_capabilities.py#L225) | 225 | `"                \"pages_fetched\": 0,"` | — |
| [SRC-AAA21D04E8-L000226](../../tests/test_generation_capabilities.py#L226) | 226 | `"                \"providers_used\": [\"duckduckgo_html\", \"bing_rss\"],"` | — |
| [SRC-AAA21D04E8-L000227](../../tests/test_generation_capabilities.py#L227) | 227 | `"                \"provider_counts\": {\"duckduckgo_html\": 1, \"bing_rss\": 1},"` | — |
| [SRC-AAA21D04E8-L000228](../../tests/test_generation_capabilities.py#L228) | 228 | `"                \"platform_counts\": {\"web\": 2},"` | — |
| [SRC-AAA21D04E8-L000229](../../tests/test_generation_capabilities.py#L229) | 229 | `"                \"evidence_signals\": {},"` | — |
| [SRC-AAA21D04E8-L000230](../../tests/test_generation_capabilities.py#L230) | 230 | `"            },"` | — |
| [SRC-AAA21D04E8-L000231](../../tests/test_generation_capabilities.py#L231) | 231 | `"        ),"` | — |
| [SRC-AAA21D04E8-L000232](../../tests/test_generation_capabilities.py#L232) | 232 | `"    )"` | — |
| [SRC-AAA21D04E8-L000233](../../tests/test_generation_capabilities.py#L233) | 233 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-AAA21D04E8-L000234](../../tests/test_generation_capabilities.py#L234) | 234 | `""` | — |
| [SRC-AAA21D04E8-L000235](../../tests/test_generation_capabilities.py#L235) | 235 | `"    def failed_generate(*args, **kwargs):"` | — |
| [SRC-AAA21D04E8-L000236](../../tests/test_generation_capabilities.py#L236) | 236 | `"        agent._record_generation_diagnostic("` | — |
| [SRC-AAA21D04E8-L000237](../../tests/test_generation_capabilities.py#L237) | 237 | `"            requested_model=\"primary/model\","` | — |
| [SRC-AAA21D04E8-L000238](../../tests/test_generation_capabilities.py#L238) | 238 | `"            attempted_model=\"fallback/model\","` | — |
| [SRC-AAA21D04E8-L000239](../../tests/test_generation_capabilities.py#L239) | 239 | `"            status=\"truncated\","` | — |
| [SRC-AAA21D04E8-L000240](../../tests/test_generation_capabilities.py#L240) | 240 | `"            finish_reason=\"length\","` | — |
| [SRC-AAA21D04E8-L000241](../../tests/test_generation_capabilities.py#L241) | 241 | `"        )"` | — |
| [SRC-AAA21D04E8-L000242](../../tests/test_generation_capabilities.py#L242) | 242 | `"        raise RuntimeError(\"اختبار: فشل التوليد بعد انتهاء حد الرموز\")"` | — |
| [SRC-AAA21D04E8-L000243](../../tests/test_generation_capabilities.py#L243) | 243 | `""` | — |
| [SRC-AAA21D04E8-L000244](../../tests/test_generation_capabilities.py#L244) | 244 | `"    monkeypatch.setattr(agent, \"_generate\", failed_generate)"` | — |
| [SRC-AAA21D04E8-L000245](../../tests/test_generation_capabilities.py#L245) | 245 | `""` | — |
| [SRC-AAA21D04E8-L000246](../../tests/test_generation_capabilities.py#L246) | 246 | `"    result = agent.answer(question)"` | — |
| [SRC-AAA21D04E8-L000247](../../tests/test_generation_capabilities.py#L247) | 247 | `""` | — |
| [SRC-AAA21D04E8-L000248](../../tests/test_generation_capabilities.py#L248) | 248 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-AAA21D04E8-L000249](../../tests/test_generation_capabilities.py#L249) | 249 | `"    assert result[\"used_language_model\"] is False"` | — |
| [SRC-AAA21D04E8-L000250](../../tests/test_generation_capabilities.py#L250) | 250 | `"    assert result[\"final_answer_status\"] == \"generation_failed_with_source_fallback\""` | — |
| [SRC-AAA21D04E8-L000251](../../tests/test_generation_capabilities.py#L251) | 251 | `"    assert len(result[\"sources\"]) == 2"` | — |
| [SRC-AAA21D04E8-L000252](../../tests/test_generation_capabilities.py#L252) | 252 | `"    assert \"تعذر توليد إجابة تحليلية\" in result[\"answer\"]"` | — |
| [SRC-AAA21D04E8-L000253](../../tests/test_generation_capabilities.py#L253) | 253 | `"    assert \"مقتطف تجريبي من المصدر الأول\" in result[\"answer\"]"` | — |
| [SRC-AAA21D04E8-L000254](../../tests/test_generation_capabilities.py#L254) | 254 | `"    assert result[\"generation_diagnostics\"] == ["` | — |
| [SRC-AAA21D04E8-L000255](../../tests/test_generation_capabilities.py#L255) | 255 | `"        {"` | — |
| [SRC-AAA21D04E8-L000256](../../tests/test_generation_capabilities.py#L256) | 256 | `"            \"attempt_number\": 1,"` | — |
| [SRC-AAA21D04E8-L000257](../../tests/test_generation_capabilities.py#L257) | 257 | `"            \"requested_model\": \"primary/model\","` | — |
| [SRC-AAA21D04E8-L000258](../../tests/test_generation_capabilities.py#L258) | 258 | `"            \"attempted_model\": \"fallback/model\","` | — |
| [SRC-AAA21D04E8-L000259](../../tests/test_generation_capabilities.py#L259) | 259 | `"            \"fallback_used\": True,"` | — |
| [SRC-AAA21D04E8-L000260](../../tests/test_generation_capabilities.py#L260) | 260 | `"            \"request_started\": True,"` | — |
| [SRC-AAA21D04E8-L000261](../../tests/test_generation_capabilities.py#L261) | 261 | `"            \"remote_response_received\": True,"` | — |
| [SRC-AAA21D04E8-L000262](../../tests/test_generation_capabilities.py#L262) | 262 | `"            \"status\": \"truncated\","` | — |
| [SRC-AAA21D04E8-L000263](../../tests/test_generation_capabilities.py#L263) | 263 | `"            \"finish_reason\": \"length\","` | — |
| [SRC-AAA21D04E8-L000264](../../tests/test_generation_capabilities.py#L264) | 264 | `"        }"` | — |
| [SRC-AAA21D04E8-L000265](../../tests/test_generation_capabilities.py#L265) | 265 | `"    ]"` | — |
| [SRC-AAA21D04E8-L000266](../../tests/test_generation_capabilities.py#L266) | 266 | `"    assert result[\"search_report\"][\"research_quality\"] == \"partial\""` | — |
| [SRC-AAA21D04E8-L000267](../../tests/test_generation_capabilities.py#L267) | 267 | `"    assert result[\"citation_validation\"][\"status\"] != \"validated_as_fact\""` | — |
| [SRC-AAA21D04E8-L000268](../../tests/test_generation_capabilities.py#L268) | 268 | `""` | — |
| [SRC-AAA21D04E8-L000269](../../tests/test_generation_capabilities.py#L269) | 269 | `""` | — |
| [SRC-AAA21D04E8-L000270](../../tests/test_generation_capabilities.py#L270) | 270 | `"def test_missing_api_key_is_reported_as_not_configured_not_attempted(monkeypatch):"` | — |
| [SRC-AAA21D04E8-L000271](../../tests/test_generation_capabilities.py#L271) | 271 | `"    agent = WebAgent()"` | — |
| [SRC-AAA21D04E8-L000272](../../tests/test_generation_capabilities.py#L272) | 272 | `"    agent.api_key = \"\""` | — |
| [SRC-AAA21D04E8-L000273](../../tests/test_generation_capabilities.py#L273) | 273 | `"    agent.generation_diagnostics = []"` | — |
| [SRC-AAA21D04E8-L000274](../../tests/test_generation_capabilities.py#L274) | 274 | `"    agent._generation_attempt_sequence = 0"` | — |
| [SRC-AAA21D04E8-L000275](../../tests/test_generation_capabilities.py#L275) | 275 | `"    with pytest.raises(RuntimeError, match=\"لم يتم ضبط مفتاح\"):"` | — |
| [SRC-AAA21D04E8-L000276](../../tests/test_generation_capabilities.py#L276) | 276 | `"        agent._request_completion("` | — |
| [SRC-AAA21D04E8-L000277](../../tests/test_generation_capabilities.py#L277) | 277 | `"            [{\"role\": \"user\", \"content\": \"اختبار\"}],"` | — |
| [SRC-AAA21D04E8-L000278](../../tests/test_generation_capabilities.py#L278) | 278 | `"            model=\"primary/model\","` | — |
| [SRC-AAA21D04E8-L000279](../../tests/test_generation_capabilities.py#L279) | 279 | `"        )"` | — |
| [SRC-AAA21D04E8-L000280](../../tests/test_generation_capabilities.py#L280) | 280 | `"    assert agent.generation_diagnostics == [{"` | — |
| [SRC-AAA21D04E8-L000281](../../tests/test_generation_capabilities.py#L281) | 281 | `"        \"attempt_number\": 1,"` | — |
| [SRC-AAA21D04E8-L000282](../../tests/test_generation_capabilities.py#L282) | 282 | `"        \"requested_model\": \"primary/model\","` | — |
| [SRC-AAA21D04E8-L000283](../../tests/test_generation_capabilities.py#L283) | 283 | `"        \"attempted_model\": \"primary/model\","` | — |
| [SRC-AAA21D04E8-L000284](../../tests/test_generation_capabilities.py#L284) | 284 | `"        \"fallback_used\": False,"` | — |
| [SRC-AAA21D04E8-L000285](../../tests/test_generation_capabilities.py#L285) | 285 | `"        \"request_started\": False,"` | — |
| [SRC-AAA21D04E8-L000286](../../tests/test_generation_capabilities.py#L286) | 286 | `"        \"remote_response_received\": False,"` | — |
| [SRC-AAA21D04E8-L000287](../../tests/test_generation_capabilities.py#L287) | 287 | `"        \"status\": \"not_configured\","` | — |
| [SRC-AAA21D04E8-L000288](../../tests/test_generation_capabilities.py#L288) | 288 | `"        \"error_class\": \"MissingAPIKey\","` | — |
| [SRC-AAA21D04E8-L000289](../../tests/test_generation_capabilities.py#L289) | 289 | `"    }]"` | — |
## اختبارات

### FILE-1A176AD4F0 — [tests/test_hosted_smoke.py](../../tests/test_hosted_smoke.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1A176AD4F0-L000001](../../tests/test_hosted_smoke.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-1A176AD4F0-L000002](../../tests/test_hosted_smoke.py#L2) | 2 | `""` | — |
| [SRC-1A176AD4F0-L000003](../../tests/test_hosted_smoke.py#L3) | 3 | `"import json"` | — |
| [SRC-1A176AD4F0-L000004](../../tests/test_hosted_smoke.py#L4) | 4 | `"import threading"` | — |
| [SRC-1A176AD4F0-L000005](../../tests/test_hosted_smoke.py#L5) | 5 | `"from pathlib import Path"` | — |
| [SRC-1A176AD4F0-L000006](../../tests/test_hosted_smoke.py#L6) | 6 | `"from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer"` | — |
| [SRC-1A176AD4F0-L000007](../../tests/test_hosted_smoke.py#L7) | 7 | `"from urllib.parse import urlsplit"` | — |
| [SRC-1A176AD4F0-L000008](../../tests/test_hosted_smoke.py#L8) | 8 | `""` | — |
| [SRC-1A176AD4F0-L000009](../../tests/test_hosted_smoke.py#L9) | 9 | `"import pytest"` | — |
| [SRC-1A176AD4F0-L000010](../../tests/test_hosted_smoke.py#L10) | 10 | `""` | — |
| [SRC-1A176AD4F0-L000011](../../tests/test_hosted_smoke.py#L11) | 11 | `"from scripts import hosted_smoke_test"` | — |
| [SRC-1A176AD4F0-L000012](../../tests/test_hosted_smoke.py#L12) | 12 | `"from scripts.hosted_smoke_test import SmokeError, normalize_origin, run_smoke"` | — |
| [SRC-1A176AD4F0-L000013](../../tests/test_hosted_smoke.py#L13) | 13 | `""` | — |
| [SRC-1A176AD4F0-L000014](../../tests/test_hosted_smoke.py#L14) | 14 | `"TOKEN = \"local-test-token-long-enough-for-the-32-character-rule\""` | — |
| [SRC-1A176AD4F0-L000015](../../tests/test_hosted_smoke.py#L15) | 15 | `""` | — |
| [SRC-1A176AD4F0-L000016](../../tests/test_hosted_smoke.py#L16) | 16 | `""` | — |
| [SRC-1A176AD4F0-L000017](../../tests/test_hosted_smoke.py#L17) | 17 | `"class Handler(BaseHTTPRequestHandler):"` | — |
| [SRC-1A176AD4F0-L000018](../../tests/test_hosted_smoke.py#L18) | 18 | `"    def log_message(self, format: str, *args: object) -> None:"` | — |
| [SRC-1A176AD4F0-L000019](../../tests/test_hosted_smoke.py#L19) | 19 | `"        return"` | — |
| [SRC-1A176AD4F0-L000020](../../tests/test_hosted_smoke.py#L20) | 20 | `""` | — |
| [SRC-1A176AD4F0-L000021](../../tests/test_hosted_smoke.py#L21) | 21 | `"    def respond(self, status: int, payload: dict[str, object]) -> None:"` | — |
| [SRC-1A176AD4F0-L000022](../../tests/test_hosted_smoke.py#L22) | 22 | `"        body = json.dumps(payload).encode()"` | — |
| [SRC-1A176AD4F0-L000023](../../tests/test_hosted_smoke.py#L23) | 23 | `"        self.send_response(status)"` | — |
| [SRC-1A176AD4F0-L000024](../../tests/test_hosted_smoke.py#L24) | 24 | `"        self.send_header(\"Content-Type\", \"application/json\")"` | — |
| [SRC-1A176AD4F0-L000025](../../tests/test_hosted_smoke.py#L25) | 25 | `"        self.send_header(\"Content-Length\", str(len(body)))"` | — |
| [SRC-1A176AD4F0-L000026](../../tests/test_hosted_smoke.py#L26) | 26 | `"        self.end_headers()"` | — |
| [SRC-1A176AD4F0-L000027](../../tests/test_hosted_smoke.py#L27) | 27 | `"        self.wfile.write(body)"` | — |
| [SRC-1A176AD4F0-L000028](../../tests/test_hosted_smoke.py#L28) | 28 | `""` | — |
| [SRC-1A176AD4F0-L000029](../../tests/test_hosted_smoke.py#L29) | 29 | `"    def do_GET(self) -> None:"` | — |
| [SRC-1A176AD4F0-L000030](../../tests/test_hosted_smoke.py#L30) | 30 | `"        if self.path == \"/api/health\":"` | — |
| [SRC-1A176AD4F0-L000031](../../tests/test_hosted_smoke.py#L31) | 31 | `"            self.respond(200, {\"ok\": True, \"app\": \"Omarai\", \"agent\": {}})"` | — |
| [SRC-1A176AD4F0-L000032](../../tests/test_hosted_smoke.py#L32) | 32 | `"        else:"` | — |
| [SRC-1A176AD4F0-L000033](../../tests/test_hosted_smoke.py#L33) | 33 | `"            self.respond(404, {\"error\": \"not found\"})"` | — |
| [SRC-1A176AD4F0-L000034](../../tests/test_hosted_smoke.py#L34) | 34 | `""` | — |
| [SRC-1A176AD4F0-L000035](../../tests/test_hosted_smoke.py#L35) | 35 | `"    def do_POST(self) -> None:"` | — |
| [SRC-1A176AD4F0-L000036](../../tests/test_hosted_smoke.py#L36) | 36 | `"        if self.headers.get(\"Authorization\") != f\"Bearer {TOKEN}\":"` | — |
| [SRC-1A176AD4F0-L000037](../../tests/test_hosted_smoke.py#L37) | 37 | `"            self.respond(401, {\"error\": \"unauthorized\"})"` | — |
| [SRC-1A176AD4F0-L000038](../../tests/test_hosted_smoke.py#L38) | 38 | `"            return"` | — |
| [SRC-1A176AD4F0-L000039](../../tests/test_hosted_smoke.py#L39) | 39 | `"        length = int(self.headers.get(\"Content-Length\", \"0\"))"` | — |
| [SRC-1A176AD4F0-L000040](../../tests/test_hosted_smoke.py#L40) | 40 | `"        self.rfile.read(length)"` | — |
| [SRC-1A176AD4F0-L000041](../../tests/test_hosted_smoke.py#L41) | 41 | `"        if self.path == \"/api/diagnostics\":"` | — |
| [SRC-1A176AD4F0-L000042](../../tests/test_hosted_smoke.py#L42) | 42 | `"            self.respond(200, {"` | — |
| [SRC-1A176AD4F0-L000043](../../tests/test_hosted_smoke.py#L43) | 43 | `"                \"overall_status\": \"passed\","` | — |
| [SRC-1A176AD4F0-L000044](../../tests/test_hosted_smoke.py#L44) | 44 | `"                \"checks\": {"` | — |
| [SRC-1A176AD4F0-L000045](../../tests/test_hosted_smoke.py#L45) | 45 | `"                    \"web_search\": {"` | — |
| [SRC-1A176AD4F0-L000046](../../tests/test_hosted_smoke.py#L46) | 46 | `"                        \"status\": \"passed\", \"result_count\": 2,"` | — |
| [SRC-1A176AD4F0-L000047](../../tests/test_hosted_smoke.py#L47) | 47 | `"                        \"provider_counts\": {\"bing_rss\": 1, \"duckduckgo_html\": 1},"` | — |
| [SRC-1A176AD4F0-L000048](../../tests/test_hosted_smoke.py#L48) | 48 | `"                    },"` | — |
| [SRC-1A176AD4F0-L000049](../../tests/test_hosted_smoke.py#L49) | 49 | `"                    \"language_model\": {\"status\": \"passed\", \"response_received\": True},"` | — |
| [SRC-1A176AD4F0-L000050](../../tests/test_hosted_smoke.py#L50) | 50 | `"                    \"social_search\": {\"status\": \"skipped\"},"` | — |
| [SRC-1A176AD4F0-L000051](../../tests/test_hosted_smoke.py#L51) | 51 | `"                },"` | — |
| [SRC-1A176AD4F0-L000052](../../tests/test_hosted_smoke.py#L52) | 52 | `"            })"` | — |
| [SRC-1A176AD4F0-L000053](../../tests/test_hosted_smoke.py#L53) | 53 | `"        elif self.path == \"/api/agent\":"` | — |
| [SRC-1A176AD4F0-L000054](../../tests/test_hosted_smoke.py#L54) | 54 | `"            self.respond(200, {"` | — |
| [SRC-1A176AD4F0-L000055](../../tests/test_hosted_smoke.py#L55) | 55 | `"                \"answer\": \"القاهرة هي عاصمة مصر. [المصدر 1]\","` | — |
| [SRC-1A176AD4F0-L000056](../../tests/test_hosted_smoke.py#L56) | 56 | `"                \"used_web_search\": True,"` | — |
| [SRC-1A176AD4F0-L000057](../../tests/test_hosted_smoke.py#L57) | 57 | `"                \"used_language_model\": True,"` | — |
| [SRC-1A176AD4F0-L000058](../../tests/test_hosted_smoke.py#L58) | 58 | `"                \"sources\": [{\"title\": \"مصدر اختبار\", \"url\": \"https://example.com/source\"}],"` | — |
| [SRC-1A176AD4F0-L000059](../../tests/test_hosted_smoke.py#L59) | 59 | `"                \"search_report\": {\"providers_used\": [\"bing_rss\"], \"pages_fetched\": 1},"` | — |
| [SRC-1A176AD4F0-L000060](../../tests/test_hosted_smoke.py#L60) | 60 | `"            })"` | — |
| [SRC-1A176AD4F0-L000061](../../tests/test_hosted_smoke.py#L61) | 61 | `"        else:"` | — |
| [SRC-1A176AD4F0-L000062](../../tests/test_hosted_smoke.py#L62) | 62 | `"            self.respond(404, {\"error\": \"not found\"})"` | — |
| [SRC-1A176AD4F0-L000063](../../tests/test_hosted_smoke.py#L63) | 63 | `""` | — |
| [SRC-1A176AD4F0-L000064](../../tests/test_hosted_smoke.py#L64) | 64 | `""` | — |
| [SRC-1A176AD4F0-L000065](../../tests/test_hosted_smoke.py#L65) | 65 | `"@pytest.fixture"` | — |
| [SRC-1A176AD4F0-L000066](../../tests/test_hosted_smoke.py#L66) | 66 | `"def hosted_server():"` | — |
| [SRC-1A176AD4F0-L000067](../../tests/test_hosted_smoke.py#L67) | 67 | `"    server = ThreadingHTTPServer((\"127.0.0.1\", 0), Handler)"` | — |
| [SRC-1A176AD4F0-L000068](../../tests/test_hosted_smoke.py#L68) | 68 | `"    thread = threading.Thread(target=server.serve_forever, daemon=True)"` | — |
| [SRC-1A176AD4F0-L000069](../../tests/test_hosted_smoke.py#L69) | 69 | `"    thread.start()"` | — |
| [SRC-1A176AD4F0-L000070](../../tests/test_hosted_smoke.py#L70) | 70 | `"    try:"` | — |
| [SRC-1A176AD4F0-L000071](../../tests/test_hosted_smoke.py#L71) | 71 | `"        yield f\"http://127.0.0.1:{server.server_port}\""` | — |
| [SRC-1A176AD4F0-L000072](../../tests/test_hosted_smoke.py#L72) | 72 | `"    finally:"` | — |
| [SRC-1A176AD4F0-L000073](../../tests/test_hosted_smoke.py#L73) | 73 | `"        server.shutdown()"` | — |
| [SRC-1A176AD4F0-L000074](../../tests/test_hosted_smoke.py#L74) | 74 | `"        server.server_close()"` | — |
| [SRC-1A176AD4F0-L000075](../../tests/test_hosted_smoke.py#L75) | 75 | `"        thread.join(timeout=2)"` | — |
| [SRC-1A176AD4F0-L000076](../../tests/test_hosted_smoke.py#L76) | 76 | `""` | — |
| [SRC-1A176AD4F0-L000077](../../tests/test_hosted_smoke.py#L77) | 77 | `""` | — |
| [SRC-1A176AD4F0-L000078](../../tests/test_hosted_smoke.py#L78) | 78 | `"def test_normalize_origin_requires_https_and_rejects_credentials_or_paths():"` | — |
| [SRC-1A176AD4F0-L000079](../../tests/test_hosted_smoke.py#L79) | 79 | `"    assert normalize_origin(\"https://example.com/\") == \"https://example.com\""` | — |
| [SRC-1A176AD4F0-L000080](../../tests/test_hosted_smoke.py#L80) | 80 | `"    for invalid in ("` | — |
| [SRC-1A176AD4F0-L000081](../../tests/test_hosted_smoke.py#L81) | 81 | `"        \"http://example.com\","` | — |
| [SRC-1A176AD4F0-L000082](../../tests/test_hosted_smoke.py#L82) | 82 | `"        \"https://user:password@example.com\","` | — |
| [SRC-1A176AD4F0-L000083](../../tests/test_hosted_smoke.py#L83) | 83 | `"        \"https://example.com/path\","` | — |
| [SRC-1A176AD4F0-L000084](../../tests/test_hosted_smoke.py#L84) | 84 | `"        \"https://example.com/?token=secret\","` | — |
| [SRC-1A176AD4F0-L000085](../../tests/test_hosted_smoke.py#L85) | 85 | `"    ):"` | — |
| [SRC-1A176AD4F0-L000086](../../tests/test_hosted_smoke.py#L86) | 86 | `"        with pytest.raises(SmokeError):"` | — |
| [SRC-1A176AD4F0-L000087](../../tests/test_hosted_smoke.py#L87) | 87 | `"            normalize_origin(invalid)"` | — |
| [SRC-1A176AD4F0-L000088](../../tests/test_hosted_smoke.py#L88) | 88 | `""` | — |
| [SRC-1A176AD4F0-L000089](../../tests/test_hosted_smoke.py#L89) | 89 | `""` | — |
| [SRC-1A176AD4F0-L000090](../../tests/test_hosted_smoke.py#L90) | 90 | `"def test_normalize_origin_allows_plain_http_only_for_local_test():"` | — |
| [SRC-1A176AD4F0-L000091](../../tests/test_hosted_smoke.py#L91) | 91 | `"    assert normalize_origin(\"http://127.0.0.1:8765\", allow_http=True) == ("` | — |
| [SRC-1A176AD4F0-L000092](../../tests/test_hosted_smoke.py#L92) | 92 | `"        \"http://127.0.0.1:8765\""` | — |
| [SRC-1A176AD4F0-L000093](../../tests/test_hosted_smoke.py#L93) | 93 | `"    )"` | — |
| [SRC-1A176AD4F0-L000094](../../tests/test_hosted_smoke.py#L94) | 94 | `"    with pytest.raises(SmokeError):"` | — |
| [SRC-1A176AD4F0-L000095](../../tests/test_hosted_smoke.py#L95) | 95 | `"        normalize_origin(\"http://example.com\", allow_http=True)"` | — |
| [SRC-1A176AD4F0-L000096](../../tests/test_hosted_smoke.py#L96) | 96 | `""` | — |
| [SRC-1A176AD4F0-L000097](../../tests/test_hosted_smoke.py#L97) | 97 | `""` | — |
| [SRC-1A176AD4F0-L000098](../../tests/test_hosted_smoke.py#L98) | 98 | `"def test_smoke_checks_health_auth_live_diagnostics_and_agent(hosted_server):"` | — |
| [SRC-1A176AD4F0-L000099](../../tests/test_hosted_smoke.py#L99) | 99 | `"    result = run_smoke("` | — |
| [SRC-1A176AD4F0-L000100](../../tests/test_hosted_smoke.py#L100) | 100 | `"        hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5"` | — |
| [SRC-1A176AD4F0-L000101](../../tests/test_hosted_smoke.py#L101) | 101 | `"    )"` | — |
| [SRC-1A176AD4F0-L000102](../../tests/test_hosted_smoke.py#L102) | 102 | `"    assert result[\"result\"] == \"passed\""` | — |
| [SRC-1A176AD4F0-L000103](../../tests/test_hosted_smoke.py#L103) | 103 | `"    assert result[\"checks\"][\"health\"] == \"passed\""` | — |
| [SRC-1A176AD4F0-L000104](../../tests/test_hosted_smoke.py#L104) | 104 | `"    assert result[\"checks\"][\"authentication\"] == \"passed\""` | — |
| [SRC-1A176AD4F0-L000105](../../tests/test_hosted_smoke.py#L105) | 105 | `"    assert result[\"checks\"][\"live_search\"][\"result_count\"] == 2"` | — |
| [SRC-1A176AD4F0-L000106](../../tests/test_hosted_smoke.py#L106) | 106 | `"    assert result[\"checks\"][\"agent_request\"][\"source_count\"] == 1"` | — |
| [SRC-1A176AD4F0-L000107](../../tests/test_hosted_smoke.py#L107) | 107 | `""` | — |
| [SRC-1A176AD4F0-L000108](../../tests/test_hosted_smoke.py#L108) | 108 | `""` | — |
| [SRC-1A176AD4F0-L000109](../../tests/test_hosted_smoke.py#L109) | 109 | `"def test_smoke_never_forwards_bearer_to_cross_origin_redirect():"` | — |
| [SRC-1A176AD4F0-L000110](../../tests/test_hosted_smoke.py#L110) | 110 | `"    received_authorizations = []"` | — |
| [SRC-1A176AD4F0-L000111](../../tests/test_hosted_smoke.py#L111) | 111 | `""` | — |
| [SRC-1A176AD4F0-L000112](../../tests/test_hosted_smoke.py#L112) | 112 | `"    class RedirectHandler(BaseHTTPRequestHandler):"` | — |
| [SRC-1A176AD4F0-L000113](../../tests/test_hosted_smoke.py#L113) | 113 | `"        def log_message(self, format: str, *args: object) -> None:"` | — |
| [SRC-1A176AD4F0-L000114](../../tests/test_hosted_smoke.py#L114) | 114 | `"            return"` | — |
| [SRC-1A176AD4F0-L000115](../../tests/test_hosted_smoke.py#L115) | 115 | `""` | — |
| [SRC-1A176AD4F0-L000116](../../tests/test_hosted_smoke.py#L116) | 116 | `"        def do_GET(self) -> None:"` | — |
| [SRC-1A176AD4F0-L000117](../../tests/test_hosted_smoke.py#L117) | 117 | `"            self.send_response(302)"` | — |
| [SRC-1A176AD4F0-L000118](../../tests/test_hosted_smoke.py#L118) | 118 | `"            self.send_header(\"Location\", self.server.redirect_destination)"` | — |
| [SRC-1A176AD4F0-L000119](../../tests/test_hosted_smoke.py#L119) | 119 | `"            self.send_header(\"Content-Length\", \"0\")"` | — |
| [SRC-1A176AD4F0-L000120](../../tests/test_hosted_smoke.py#L120) | 120 | `"            self.end_headers()"` | — |
| [SRC-1A176AD4F0-L000121](../../tests/test_hosted_smoke.py#L121) | 121 | `""` | — |
| [SRC-1A176AD4F0-L000122](../../tests/test_hosted_smoke.py#L122) | 122 | `"    class DestinationHandler(BaseHTTPRequestHandler):"` | — |
| [SRC-1A176AD4F0-L000123](../../tests/test_hosted_smoke.py#L123) | 123 | `"        def log_message(self, format: str, *args: object) -> None:"` | — |
| [SRC-1A176AD4F0-L000124](../../tests/test_hosted_smoke.py#L124) | 124 | `"            return"` | — |
| [SRC-1A176AD4F0-L000125](../../tests/test_hosted_smoke.py#L125) | 125 | `""` | — |
| [SRC-1A176AD4F0-L000126](../../tests/test_hosted_smoke.py#L126) | 126 | `"        def do_GET(self) -> None:"` | — |
| [SRC-1A176AD4F0-L000127](../../tests/test_hosted_smoke.py#L127) | 127 | `"            received_authorizations.append(self.headers.get(\"Authorization\"))"` | — |
| [SRC-1A176AD4F0-L000128](../../tests/test_hosted_smoke.py#L128) | 128 | `"            self.send_response(200)"` | — |
| [SRC-1A176AD4F0-L000129](../../tests/test_hosted_smoke.py#L129) | 129 | `"            self.send_header(\"Content-Length\", \"0\")"` | — |
| [SRC-1A176AD4F0-L000130](../../tests/test_hosted_smoke.py#L130) | 130 | `"            self.end_headers()"` | — |
| [SRC-1A176AD4F0-L000131](../../tests/test_hosted_smoke.py#L131) | 131 | `""` | — |
| [SRC-1A176AD4F0-L000132](../../tests/test_hosted_smoke.py#L132) | 132 | `"    destination = ThreadingHTTPServer((\"127.0.0.1\", 0), DestinationHandler)"` | — |
| [SRC-1A176AD4F0-L000133](../../tests/test_hosted_smoke.py#L133) | 133 | `"    source = ThreadingHTTPServer((\"127.0.0.1\", 0), RedirectHandler)"` | — |
| [SRC-1A176AD4F0-L000134](../../tests/test_hosted_smoke.py#L134) | 134 | `"    destination_thread = threading.Thread(target=destination.serve_forever, daemon=True)"` | — |
| [SRC-1A176AD4F0-L000135](../../tests/test_hosted_smoke.py#L135) | 135 | `"    source_thread = threading.Thread(target=source.serve_forever, daemon=True)"` | — |
| [SRC-1A176AD4F0-L000136](../../tests/test_hosted_smoke.py#L136) | 136 | `"    source.redirect_destination = ("` | — |
| [SRC-1A176AD4F0-L000137](../../tests/test_hosted_smoke.py#L137) | 137 | `"        f\"http://127.0.0.1:{destination.server_port}/capture\""` | — |
| [SRC-1A176AD4F0-L000138](../../tests/test_hosted_smoke.py#L138) | 138 | `"    )"` | — |
| [SRC-1A176AD4F0-L000139](../../tests/test_hosted_smoke.py#L139) | 139 | `"    destination_thread.start()"` | — |
| [SRC-1A176AD4F0-L000140](../../tests/test_hosted_smoke.py#L140) | 140 | `"    source_thread.start()"` | — |
| [SRC-1A176AD4F0-L000141](../../tests/test_hosted_smoke.py#L141) | 141 | `"    try:"` | — |
| [SRC-1A176AD4F0-L000142](../../tests/test_hosted_smoke.py#L142) | 142 | `"        status, payload = hosted_smoke_test.request_json("` | — |
| [SRC-1A176AD4F0-L000143](../../tests/test_hosted_smoke.py#L143) | 143 | `"            f\"http://127.0.0.1:{source.server_port}/redirect\","` | — |
| [SRC-1A176AD4F0-L000144](../../tests/test_hosted_smoke.py#L144) | 144 | `"            token=TOKEN,"` | — |
| [SRC-1A176AD4F0-L000145](../../tests/test_hosted_smoke.py#L145) | 145 | `"            timeout=3,"` | — |
| [SRC-1A176AD4F0-L000146](../../tests/test_hosted_smoke.py#L146) | 146 | `"        )"` | — |
| [SRC-1A176AD4F0-L000147](../../tests/test_hosted_smoke.py#L147) | 147 | `"        assert status == 302"` | — |
| [SRC-1A176AD4F0-L000148](../../tests/test_hosted_smoke.py#L148) | 148 | `"        assert payload is None"` | — |
| [SRC-1A176AD4F0-L000149](../../tests/test_hosted_smoke.py#L149) | 149 | `"        assert received_authorizations == []"` | — |
| [SRC-1A176AD4F0-L000150](../../tests/test_hosted_smoke.py#L150) | 150 | `"    finally:"` | — |
| [SRC-1A176AD4F0-L000151](../../tests/test_hosted_smoke.py#L151) | 151 | `"        source.shutdown()"` | — |
| [SRC-1A176AD4F0-L000152](../../tests/test_hosted_smoke.py#L152) | 152 | `"        destination.shutdown()"` | — |
| [SRC-1A176AD4F0-L000153](../../tests/test_hosted_smoke.py#L153) | 153 | `"        source.server_close()"` | — |
| [SRC-1A176AD4F0-L000154](../../tests/test_hosted_smoke.py#L154) | 154 | `"        destination.server_close()"` | — |
| [SRC-1A176AD4F0-L000155](../../tests/test_hosted_smoke.py#L155) | 155 | `"        source_thread.join(timeout=2)"` | — |
| [SRC-1A176AD4F0-L000156](../../tests/test_hosted_smoke.py#L156) | 156 | `"        destination_thread.join(timeout=2)"` | — |
| [SRC-1A176AD4F0-L000157](../../tests/test_hosted_smoke.py#L157) | 157 | `""` | — |
| [SRC-1A176AD4F0-L000158](../../tests/test_hosted_smoke.py#L158) | 158 | `""` | — |
| [SRC-1A176AD4F0-L000159](../../tests/test_hosted_smoke.py#L159) | 159 | `"def test_smoke_refuses_missing_or_short_access_token(hosted_server):"` | — |
| [SRC-1A176AD4F0-L000160](../../tests/test_hosted_smoke.py#L160) | 160 | `"    with pytest.raises(SmokeError, match=\"OMARAI_ACCESS_TOKEN\"):"` | — |
| [SRC-1A176AD4F0-L000161](../../tests/test_hosted_smoke.py#L161) | 161 | `"        run_smoke(hosted_server, \"\", allow_http=True, allow_provider_usage=True, timeout=5)"` | — |
| [SRC-1A176AD4F0-L000162](../../tests/test_hosted_smoke.py#L162) | 162 | `""` | — |
| [SRC-1A176AD4F0-L000163](../../tests/test_hosted_smoke.py#L163) | 163 | `""` | — |
| [SRC-1A176AD4F0-L000164](../../tests/test_hosted_smoke.py#L164) | 164 | `"def test_smoke_fails_when_agent_returns_no_live_source(hosted_server, monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000165](../../tests/test_hosted_smoke.py#L165) | 165 | `"    original = hosted_smoke_test.request_json"` | — |
| [SRC-1A176AD4F0-L000166](../../tests/test_hosted_smoke.py#L166) | 166 | `""` | — |
| [SRC-1A176AD4F0-L000167](../../tests/test_hosted_smoke.py#L167) | 167 | `"    def without_sources(url: str, **kwargs):"` | — |
| [SRC-1A176AD4F0-L000168](../../tests/test_hosted_smoke.py#L168) | 168 | `"        if urlsplit(url).path == \"/api/agent\" and kwargs.get(\"token\") == TOKEN:"` | — |
| [SRC-1A176AD4F0-L000169](../../tests/test_hosted_smoke.py#L169) | 169 | `"            return 200, {"` | — |
| [SRC-1A176AD4F0-L000170](../../tests/test_hosted_smoke.py#L170) | 170 | `"                \"answer\": \"إجابة بلا مصادر\", \"used_web_search\": False,"` | — |
| [SRC-1A176AD4F0-L000171](../../tests/test_hosted_smoke.py#L171) | 171 | `"                \"used_language_model\": True, \"sources\": [],"` | — |
| [SRC-1A176AD4F0-L000172](../../tests/test_hosted_smoke.py#L172) | 172 | `"            }"` | — |
| [SRC-1A176AD4F0-L000173](../../tests/test_hosted_smoke.py#L173) | 173 | `"        return original(url, **kwargs)"` | — |
| [SRC-1A176AD4F0-L000174](../../tests/test_hosted_smoke.py#L174) | 174 | `""` | — |
| [SRC-1A176AD4F0-L000175](../../tests/test_hosted_smoke.py#L175) | 175 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", without_sources)"` | — |
| [SRC-1A176AD4F0-L000176](../../tests/test_hosted_smoke.py#L176) | 176 | `"    with pytest.raises(SmokeError, match=\"usable source URLs\") as failure:"` | — |
| [SRC-1A176AD4F0-L000177](../../tests/test_hosted_smoke.py#L177) | 177 | `"        run_smoke(hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5)"` | — |
| [SRC-1A176AD4F0-L000178](../../tests/test_hosted_smoke.py#L178) | 178 | `"    assert failure.value.report[\"transcript\"][0][\"question\"] == ("` | — |
| [SRC-1A176AD4F0-L000179](../../tests/test_hosted_smoke.py#L179) | 179 | `"        hosted_smoke_test.LIVE_TEST_QUESTION"` | — |
| [SRC-1A176AD4F0-L000180](../../tests/test_hosted_smoke.py#L180) | 180 | `"    )"` | — |
| [SRC-1A176AD4F0-L000181](../../tests/test_hosted_smoke.py#L181) | 181 | `"    assert failure.value.report[\"transcript\"][0][\"answer\"] == \"إجابة بلا مصادر\""` | — |
| [SRC-1A176AD4F0-L000182](../../tests/test_hosted_smoke.py#L182) | 182 | `""` | — |
| [SRC-1A176AD4F0-L000183](../../tests/test_hosted_smoke.py#L183) | 183 | `""` | — |
| [SRC-1A176AD4F0-L000184](../../tests/test_hosted_smoke.py#L184) | 184 | `"def test_smoke_rejects_invalid_expected_source_sha(hosted_server):"` | — |
| [SRC-1A176AD4F0-L000185](../../tests/test_hosted_smoke.py#L185) | 185 | `"    with pytest.raises(SmokeError, match=\"40-character Git SHA\"):"` | — |
| [SRC-1A176AD4F0-L000186](../../tests/test_hosted_smoke.py#L186) | 186 | `"        run_smoke("` | — |
| [SRC-1A176AD4F0-L000187](../../tests/test_hosted_smoke.py#L187) | 187 | `"            hosted_server, TOKEN, allow_http=True, timeout=5, expected_sha=\"main\""` | — |
| [SRC-1A176AD4F0-L000188](../../tests/test_hosted_smoke.py#L188) | 188 | `"        )"` | — |
| [SRC-1A176AD4F0-L000189](../../tests/test_hosted_smoke.py#L189) | 189 | `""` | — |
| [SRC-1A176AD4F0-L000190](../../tests/test_hosted_smoke.py#L190) | 190 | `""` | — |
| [SRC-1A176AD4F0-L000191](../../tests/test_hosted_smoke.py#L191) | 191 | `"def test_smoke_rejects_deployed_build_sha_mismatch(hosted_server):"` | — |
| [SRC-1A176AD4F0-L000192](../../tests/test_hosted_smoke.py#L192) | 192 | `"    with pytest.raises(SmokeError, match=\"does not match the expected Git commit\"):"` | — |
| [SRC-1A176AD4F0-L000193](../../tests/test_hosted_smoke.py#L193) | 193 | `"        run_smoke("` | — |
| [SRC-1A176AD4F0-L000194](../../tests/test_hosted_smoke.py#L194) | 194 | `"            hosted_server,"` | — |
| [SRC-1A176AD4F0-L000195](../../tests/test_hosted_smoke.py#L195) | 195 | `"            TOKEN,"` | — |
| [SRC-1A176AD4F0-L000196](../../tests/test_hosted_smoke.py#L196) | 196 | `"            allow_http=True,"` | — |
| [SRC-1A176AD4F0-L000197](../../tests/test_hosted_smoke.py#L197) | 197 | `"            allow_provider_usage=True,"` | — |
| [SRC-1A176AD4F0-L000198](../../tests/test_hosted_smoke.py#L198) | 198 | `"            timeout=5,"` | — |
| [SRC-1A176AD4F0-L000199](../../tests/test_hosted_smoke.py#L199) | 199 | `"            expected_sha=\"a\" * 40,"` | — |
| [SRC-1A176AD4F0-L000200](../../tests/test_hosted_smoke.py#L200) | 200 | `"        )"` | — |
| [SRC-1A176AD4F0-L000201](../../tests/test_hosted_smoke.py#L201) | 201 | `""` | — |
| [SRC-1A176AD4F0-L000202](../../tests/test_hosted_smoke.py#L202) | 202 | `""` | — |
| [SRC-1A176AD4F0-L000203](../../tests/test_hosted_smoke.py#L203) | 203 | `"def test_smoke_requires_explicit_provider_usage_approval_before_network(monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000204](../../tests/test_hosted_smoke.py#L204) | 204 | `"    calls = []"` | — |
| [SRC-1A176AD4F0-L000205](../../tests/test_hosted_smoke.py#L205) | 205 | `""` | — |
| [SRC-1A176AD4F0-L000206](../../tests/test_hosted_smoke.py#L206) | 206 | `"    def unexpected_request(*args, **kwargs):"` | — |
| [SRC-1A176AD4F0-L000207](../../tests/test_hosted_smoke.py#L207) | 207 | `"        calls.append((args, kwargs))"` | — |
| [SRC-1A176AD4F0-L000208](../../tests/test_hosted_smoke.py#L208) | 208 | `"        raise AssertionError(\"network must not be called without explicit approval\")"` | — |
| [SRC-1A176AD4F0-L000209](../../tests/test_hosted_smoke.py#L209) | 209 | `""` | — |
| [SRC-1A176AD4F0-L000210](../../tests/test_hosted_smoke.py#L210) | 210 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", unexpected_request)"` | — |
| [SRC-1A176AD4F0-L000211](../../tests/test_hosted_smoke.py#L211) | 211 | `"    with pytest.raises(SmokeError, match=\"explicit human approval\"):"` | — |
| [SRC-1A176AD4F0-L000212](../../tests/test_hosted_smoke.py#L212) | 212 | `"        run_smoke("` | — |
| [SRC-1A176AD4F0-L000213](../../tests/test_hosted_smoke.py#L213) | 213 | `"            \"https://omarai.example.test\","` | — |
| [SRC-1A176AD4F0-L000214](../../tests/test_hosted_smoke.py#L214) | 214 | `"            TOKEN,"` | — |
| [SRC-1A176AD4F0-L000215](../../tests/test_hosted_smoke.py#L215) | 215 | `"            allow_provider_usage=False,"` | — |
| [SRC-1A176AD4F0-L000216](../../tests/test_hosted_smoke.py#L216) | 216 | `"            expected_sha=\"a\" * 40,"` | — |
| [SRC-1A176AD4F0-L000217](../../tests/test_hosted_smoke.py#L217) | 217 | `"        )"` | — |
| [SRC-1A176AD4F0-L000218](../../tests/test_hosted_smoke.py#L218) | 218 | `"    assert calls == []"` | — |
| [SRC-1A176AD4F0-L000219](../../tests/test_hosted_smoke.py#L219) | 219 | `""` | — |
| [SRC-1A176AD4F0-L000220](../../tests/test_hosted_smoke.py#L220) | 220 | `""` | — |
| [SRC-1A176AD4F0-L000221](../../tests/test_hosted_smoke.py#L221) | 221 | `"def test_hosted_smoke_workflow_is_manual_and_cost_gated():"` | — |
| [SRC-1A176AD4F0-L000222](../../tests/test_hosted_smoke.py#L222) | 222 | `"    workflow = Path(\".github/workflows/hosted-smoke.yml\").read_text(encoding=\"utf-8\")"` | — |
| [SRC-1A176AD4F0-L000223](../../tests/test_hosted_smoke.py#L223) | 223 | `"    assert \"schedule:\" not in workflow"` | — |
| [SRC-1A176AD4F0-L000224](../../tests/test_hosted_smoke.py#L224) | 224 | `"    assert \"allow_provider_usage:\" in workflow"` | — |
| [SRC-1A176AD4F0-L000225](../../tests/test_hosted_smoke.py#L225) | 225 | `"    assert \"default: false\" in workflow"` | — |
| [SRC-1A176AD4F0-L000226](../../tests/test_hosted_smoke.py#L226) | 226 | `"    assert \"--allow-provider-usage\" in workflow"` | — |
## اختبارات

### FILE-1BB2FDD5B7 — [tests/test_hosted_smoke_transcript.py](../../tests/test_hosted_smoke_transcript.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1BB2FDD5B7-L000001](../../tests/test_hosted_smoke_transcript.py#L1) | 1 | `"\"\"\"Tests for the hosted acceptance transcript contract.\"\"\""` | — |
| [SRC-1BB2FDD5B7-L000002](../../tests/test_hosted_smoke_transcript.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-1BB2FDD5B7-L000003](../../tests/test_hosted_smoke_transcript.py#L3) | 3 | `""` | — |
| [SRC-1BB2FDD5B7-L000004](../../tests/test_hosted_smoke_transcript.py#L4) | 4 | `"from scripts import hosted_smoke_test"` | — |
| [SRC-1BB2FDD5B7-L000005](../../tests/test_hosted_smoke_transcript.py#L5) | 5 | `""` | — |
| [SRC-1BB2FDD5B7-L000006](../../tests/test_hosted_smoke_transcript.py#L6) | 6 | `""` | — |
| [SRC-1BB2FDD5B7-L000007](../../tests/test_hosted_smoke_transcript.py#L7) | 7 | `"def test_hosted_smoke_returns_exact_question_answer_and_sources(monkeypatch):"` | — |
| [SRC-1BB2FDD5B7-L000008](../../tests/test_hosted_smoke_transcript.py#L8) | 8 | `"    calls = []"` | — |
| [SRC-1BB2FDD5B7-L000009](../../tests/test_hosted_smoke_transcript.py#L9) | 9 | `""` | — |
| [SRC-1BB2FDD5B7-L000010](../../tests/test_hosted_smoke_transcript.py#L10) | 10 | `"    def fake_request_json(url, *, token=\"\", payload=None, timeout=90):"` | — |
| [SRC-1BB2FDD5B7-L000011](../../tests/test_hosted_smoke_transcript.py#L11) | 11 | `"        calls.append((url, token, payload))"` | — |
| [SRC-1BB2FDD5B7-L000012](../../tests/test_hosted_smoke_transcript.py#L12) | 12 | `"        if url.endswith(\"/api/health\"):"` | — |
| [SRC-1BB2FDD5B7-L000013](../../tests/test_hosted_smoke_transcript.py#L13) | 13 | `"            return 200, {\"ok\": True, \"build\": {\"sha\": \"a\" * 40}}"` | — |
| [SRC-1BB2FDD5B7-L000014](../../tests/test_hosted_smoke_transcript.py#L14) | 14 | `"        if url.endswith(\"/api/agent\") and not token:"` | — |
| [SRC-1BB2FDD5B7-L000015](../../tests/test_hosted_smoke_transcript.py#L15) | 15 | `"            return 401, None"` | — |
| [SRC-1BB2FDD5B7-L000016](../../tests/test_hosted_smoke_transcript.py#L16) | 16 | `"        if url.endswith(\"/api/diagnostics\"):"` | — |
| [SRC-1BB2FDD5B7-L000017](../../tests/test_hosted_smoke_transcript.py#L17) | 17 | `"            return 200, {"` | — |
| [SRC-1BB2FDD5B7-L000018](../../tests/test_hosted_smoke_transcript.py#L18) | 18 | `"                \"checks\": {"` | — |
| [SRC-1BB2FDD5B7-L000019](../../tests/test_hosted_smoke_transcript.py#L19) | 19 | `"                    \"web_search\": {"` | — |
| [SRC-1BB2FDD5B7-L000020](../../tests/test_hosted_smoke_transcript.py#L20) | 20 | `"                        \"status\": \"passed\","` | — |
| [SRC-1BB2FDD5B7-L000021](../../tests/test_hosted_smoke_transcript.py#L21) | 21 | `"                        \"result_count\": 2,"` | — |
| [SRC-1BB2FDD5B7-L000022](../../tests/test_hosted_smoke_transcript.py#L22) | 22 | `"                        \"provider_counts\": {\"bing_rss\": 2},"` | — |
| [SRC-1BB2FDD5B7-L000023](../../tests/test_hosted_smoke_transcript.py#L23) | 23 | `"                    },"` | — |
| [SRC-1BB2FDD5B7-L000024](../../tests/test_hosted_smoke_transcript.py#L24) | 24 | `"                    \"language_model\": {\"status\": \"passed\"},"` | — |
| [SRC-1BB2FDD5B7-L000025](../../tests/test_hosted_smoke_transcript.py#L25) | 25 | `"                },"` | — |
| [SRC-1BB2FDD5B7-L000026](../../tests/test_hosted_smoke_transcript.py#L26) | 26 | `"                \"provider_diagnostics\": ["` | — |
| [SRC-1BB2FDD5B7-L000027](../../tests/test_hosted_smoke_transcript.py#L27) | 27 | `"                    {\"provider\": \"bing_rss\", \"status\": \"ok\", \"accepted_count\": 2}"` | — |
| [SRC-1BB2FDD5B7-L000028](../../tests/test_hosted_smoke_transcript.py#L28) | 28 | `"                ],"` | — |
| [SRC-1BB2FDD5B7-L000029](../../tests/test_hosted_smoke_transcript.py#L29) | 29 | `"                \"configuration\": {"` | — |
| [SRC-1BB2FDD5B7-L000030](../../tests/test_hosted_smoke_transcript.py#L30) | 30 | `"                    \"brave_search_api_configured\": False,"` | — |
| [SRC-1BB2FDD5B7-L000031](../../tests/test_hosted_smoke_transcript.py#L31) | 31 | `"                    \"tavily_search_api_configured\": False,"` | — |
| [SRC-1BB2FDD5B7-L000032](../../tests/test_hosted_smoke_transcript.py#L32) | 32 | `"                    \"deepseek_search_api_configured\": False,"` | — |
| [SRC-1BB2FDD5B7-L000033](../../tests/test_hosted_smoke_transcript.py#L33) | 33 | `"                },"` | — |
| [SRC-1BB2FDD5B7-L000034](../../tests/test_hosted_smoke_transcript.py#L34) | 34 | `"                \"warnings\": [],"` | — |
| [SRC-1BB2FDD5B7-L000035](../../tests/test_hosted_smoke_transcript.py#L35) | 35 | `"            }"` | — |
| [SRC-1BB2FDD5B7-L000036](../../tests/test_hosted_smoke_transcript.py#L36) | 36 | `"        if url.endswith(\"/api/agent\") and token:"` | — |
| [SRC-1BB2FDD5B7-L000037](../../tests/test_hosted_smoke_transcript.py#L37) | 37 | `"            return 200, {"` | — |
| [SRC-1BB2FDD5B7-L000038](../../tests/test_hosted_smoke_transcript.py#L38) | 38 | `"                \"answer\": \"وجدت إشارة منشورة تطلب عرض سعر لنظام إنذار الحريق.\","` | — |
| [SRC-1BB2FDD5B7-L000039](../../tests/test_hosted_smoke_transcript.py#L39) | 39 | `"                \"used_web_search\": True,"` | — |
| [SRC-1BB2FDD5B7-L000040](../../tests/test_hosted_smoke_transcript.py#L40) | 40 | `"                \"used_language_model\": True,"` | — |
| [SRC-1BB2FDD5B7-L000041](../../tests/test_hosted_smoke_transcript.py#L41) | 41 | `"                \"answer_evidence_status\": \"sources_present\","` | — |
| [SRC-1BB2FDD5B7-L000042](../../tests/test_hosted_smoke_transcript.py#L42) | 42 | `"                \"sources\": ["` | — |
| [SRC-1BB2FDD5B7-L000043](../../tests/test_hosted_smoke_transcript.py#L43) | 43 | `"                    {"` | — |
| [SRC-1BB2FDD5B7-L000044](../../tests/test_hosted_smoke_transcript.py#L44) | 44 | `"                        \"title\": \"Fire alarm tender notice\","` | — |
| [SRC-1BB2FDD5B7-L000045](../../tests/test_hosted_smoke_transcript.py#L45) | 45 | `"                        \"url\": \"https://example.test/fire-alarm-tender\","` | — |
| [SRC-1BB2FDD5B7-L000046](../../tests/test_hosted_smoke_transcript.py#L46) | 46 | `"                        \"provider\": \"bing_rss\","` | — |
| [SRC-1BB2FDD5B7-L000047](../../tests/test_hosted_smoke_transcript.py#L47) | 47 | `"                        \"snippet\": \"طلب عرض سعر لنظام إنذار الحريق.\","` | — |
| [SRC-1BB2FDD5B7-L000048](../../tests/test_hosted_smoke_transcript.py#L48) | 48 | `"                        \"published_at\": \"\","` | — |
| [SRC-1BB2FDD5B7-L000049](../../tests/test_hosted_smoke_transcript.py#L49) | 49 | `"                    }"` | — |
| [SRC-1BB2FDD5B7-L000050](../../tests/test_hosted_smoke_transcript.py#L50) | 50 | `"                ],"` | — |
| [SRC-1BB2FDD5B7-L000051](../../tests/test_hosted_smoke_transcript.py#L51) | 51 | `"                \"search_report\": {"` | — |
| [SRC-1BB2FDD5B7-L000052](../../tests/test_hosted_smoke_transcript.py#L52) | 52 | `"                    \"pages_fetched\": 1,"` | — |
| [SRC-1BB2FDD5B7-L000053](../../tests/test_hosted_smoke_transcript.py#L53) | 53 | `"                    \"providers_used\": [\"bing_rss\"],"` | — |
| [SRC-1BB2FDD5B7-L000054](../../tests/test_hosted_smoke_transcript.py#L54) | 54 | `"                    \"pipeline_completion_status\": \"completed\","` | — |
| [SRC-1BB2FDD5B7-L000055](../../tests/test_hosted_smoke_transcript.py#L55) | 55 | `"                },"` | — |
| [SRC-1BB2FDD5B7-L000056](../../tests/test_hosted_smoke_transcript.py#L56) | 56 | `"            }"` | — |
| [SRC-1BB2FDD5B7-L000057](../../tests/test_hosted_smoke_transcript.py#L57) | 57 | `"        raise AssertionError(f\"unexpected request: {url}\")"` | — |
| [SRC-1BB2FDD5B7-L000058](../../tests/test_hosted_smoke_transcript.py#L58) | 58 | `""` | — |
| [SRC-1BB2FDD5B7-L000059](../../tests/test_hosted_smoke_transcript.py#L59) | 59 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", fake_request_json)"` | — |
| [SRC-1BB2FDD5B7-L000060](../../tests/test_hosted_smoke_transcript.py#L60) | 60 | `"    report = hosted_smoke_test.run_smoke("` | — |
| [SRC-1BB2FDD5B7-L000061](../../tests/test_hosted_smoke_transcript.py#L61) | 61 | `"        \"https://omarai.example\", \"T\" * 40, expected_sha=\"a\" * 40,"` | — |
| [SRC-1BB2FDD5B7-L000062](../../tests/test_hosted_smoke_transcript.py#L62) | 62 | `"        allow_provider_usage=True,"` | — |
| [SRC-1BB2FDD5B7-L000063](../../tests/test_hosted_smoke_transcript.py#L63) | 63 | `"    )"` | — |
| [SRC-1BB2FDD5B7-L000064](../../tests/test_hosted_smoke_transcript.py#L64) | 64 | `""` | — |
| [SRC-1BB2FDD5B7-L000065](../../tests/test_hosted_smoke_transcript.py#L65) | 65 | `"    transcript = report[\"transcript\"][0]"` | — |
| [SRC-1BB2FDD5B7-L000066](../../tests/test_hosted_smoke_transcript.py#L66) | 66 | `"    assert transcript[\"question\"] == hosted_smoke_test.LIVE_TEST_QUESTION"` | — |
| [SRC-1BB2FDD5B7-L000067](../../tests/test_hosted_smoke_transcript.py#L67) | 67 | `"    assert transcript[\"answer\"] == \"وجدت إشارة منشورة تطلب عرض سعر لنظام إنذار الحريق.\""` | — |
| [SRC-1BB2FDD5B7-L000068](../../tests/test_hosted_smoke_transcript.py#L68) | 68 | `"    assert transcript[\"sources\"][0][\"url\"] == \"https://example.test/fire-alarm-tender\""` | — |
| [SRC-1BB2FDD5B7-L000069](../../tests/test_hosted_smoke_transcript.py#L69) | 69 | `"    assert transcript[\"pipeline_completion_status\"] == \"completed\""` | — |
| [SRC-1BB2FDD5B7-L000070](../../tests/test_hosted_smoke_transcript.py#L70) | 70 | `"    assert report[\"provider_diagnostics\"][0][\"provider\"] == \"bing_rss\""` | — |
| [SRC-1BB2FDD5B7-L000071](../../tests/test_hosted_smoke_transcript.py#L71) | 71 | `"    assert report[\"connector_configuration\"][\"brave_search_api_configured\"] is False"` | — |
| [SRC-1BB2FDD5B7-L000072](../../tests/test_hosted_smoke_transcript.py#L72) | 72 | `"    assert report[\"connector_check\"][\"provider_counts\"] == {\"bing_rss\": 2}"` | — |
| [SRC-1BB2FDD5B7-L000073](../../tests/test_hosted_smoke_transcript.py#L73) | 73 | `"    diagnostics_call = next(call for call in calls if call[0].endswith(\"/api/diagnostics\"))"` | — |
| [SRC-1BB2FDD5B7-L000074](../../tests/test_hosted_smoke_transcript.py#L74) | 74 | `"    assert diagnostics_call[2][\"test_model\"] is False"` | — |
| [SRC-1BB2FDD5B7-L000075](../../tests/test_hosted_smoke_transcript.py#L75) | 75 | `"    assert all(\"T\" * 40 not in str(item) for item in report.values())"` | — |
| [SRC-1BB2FDD5B7-L000076](../../tests/test_hosted_smoke_transcript.py#L76) | 76 | `"    assert len(calls) == 4"` | — |
| [SRC-1BB2FDD5B7-L000077](../../tests/test_hosted_smoke_transcript.py#L77) | 77 | `""` | — |
| [SRC-1BB2FDD5B7-L000078](../../tests/test_hosted_smoke_transcript.py#L78) | 78 | `""` | — |
| [SRC-1BB2FDD5B7-L000079](../../tests/test_hosted_smoke_transcript.py#L79) | 79 | `"def test_hosted_smoke_allows_no_token_only_for_loopback_dev(monkeypatch):"` | — |
| [SRC-1BB2FDD5B7-L000080](../../tests/test_hosted_smoke_transcript.py#L80) | 80 | `"    def fake_request_json(url, *, token=\"\", payload=None, timeout=90):"` | — |
| [SRC-1BB2FDD5B7-L000081](../../tests/test_hosted_smoke_transcript.py#L81) | 81 | `"        if url.endswith(\"/api/health\"):"` | — |
| [SRC-1BB2FDD5B7-L000082](../../tests/test_hosted_smoke_transcript.py#L82) | 82 | `"            return 200, {\"ok\": True, \"build\": {\"sha\": \"unknown\"}}"` | — |
| [SRC-1BB2FDD5B7-L000083](../../tests/test_hosted_smoke_transcript.py#L83) | 83 | `"        if url.endswith(\"/api/diagnostics\"):"` | — |
| [SRC-1BB2FDD5B7-L000084](../../tests/test_hosted_smoke_transcript.py#L84) | 84 | `"            return 200, {"` | — |
| [SRC-1BB2FDD5B7-L000085](../../tests/test_hosted_smoke_transcript.py#L85) | 85 | `"                \"checks\": {"` | — |
| [SRC-1BB2FDD5B7-L000086](../../tests/test_hosted_smoke_transcript.py#L86) | 86 | `"                    \"web_search\": {\"status\": \"passed\", \"result_count\": 1},"` | — |
| [SRC-1BB2FDD5B7-L000087](../../tests/test_hosted_smoke_transcript.py#L87) | 87 | `"                    \"language_model\": {\"status\": \"passed\"},"` | — |
| [SRC-1BB2FDD5B7-L000088](../../tests/test_hosted_smoke_transcript.py#L88) | 88 | `"                },"` | — |
| [SRC-1BB2FDD5B7-L000089](../../tests/test_hosted_smoke_transcript.py#L89) | 89 | `"                \"provider_diagnostics\": [],"` | — |
| [SRC-1BB2FDD5B7-L000090](../../tests/test_hosted_smoke_transcript.py#L90) | 90 | `"                \"warnings\": [],"` | — |
| [SRC-1BB2FDD5B7-L000091](../../tests/test_hosted_smoke_transcript.py#L91) | 91 | `"            }"` | — |
| [SRC-1BB2FDD5B7-L000092](../../tests/test_hosted_smoke_transcript.py#L92) | 92 | `"        if url.endswith(\"/api/agent\"):"` | — |
| [SRC-1BB2FDD5B7-L000093](../../tests/test_hosted_smoke_transcript.py#L93) | 93 | `"            return 200, {"` | — |
| [SRC-1BB2FDD5B7-L000094](../../tests/test_hosted_smoke_transcript.py#L94) | 94 | `"                \"answer\": \"لا توجد إشارة شراء مؤكدة في المصادر التي تم فحصها.\","` | — |
| [SRC-1BB2FDD5B7-L000095](../../tests/test_hosted_smoke_transcript.py#L95) | 95 | `"                \"used_web_search\": True,"` | — |
| [SRC-1BB2FDD5B7-L000096](../../tests/test_hosted_smoke_transcript.py#L96) | 96 | `"                \"used_language_model\": True,"` | — |
| [SRC-1BB2FDD5B7-L000097](../../tests/test_hosted_smoke_transcript.py#L97) | 97 | `"                \"sources\": [{\"url\": \"https://example.test/egypt\"}],"` | — |
| [SRC-1BB2FDD5B7-L000098](../../tests/test_hosted_smoke_transcript.py#L98) | 98 | `"            }"` | — |
| [SRC-1BB2FDD5B7-L000099](../../tests/test_hosted_smoke_transcript.py#L99) | 99 | `"        raise AssertionError(url)"` | — |
| [SRC-1BB2FDD5B7-L000100](../../tests/test_hosted_smoke_transcript.py#L100) | 100 | `""` | — |
| [SRC-1BB2FDD5B7-L000101](../../tests/test_hosted_smoke_transcript.py#L101) | 101 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", fake_request_json)"` | — |
| [SRC-1BB2FDD5B7-L000102](../../tests/test_hosted_smoke_transcript.py#L102) | 102 | `"    report = hosted_smoke_test.run_smoke("` | — |
| [SRC-1BB2FDD5B7-L000103](../../tests/test_hosted_smoke_transcript.py#L103) | 103 | `"        \"http://127.0.0.1:8000\","` | — |
| [SRC-1BB2FDD5B7-L000104](../../tests/test_hosted_smoke_transcript.py#L104) | 104 | `"        \"\","` | — |
| [SRC-1BB2FDD5B7-L000105](../../tests/test_hosted_smoke_transcript.py#L105) | 105 | `"        local_dev_no_token=True,"` | — |
| [SRC-1BB2FDD5B7-L000106](../../tests/test_hosted_smoke_transcript.py#L106) | 106 | `"        allow_provider_usage=True,"` | — |
| [SRC-1BB2FDD5B7-L000107](../../tests/test_hosted_smoke_transcript.py#L107) | 107 | `"    )"` | — |
| [SRC-1BB2FDD5B7-L000108](../../tests/test_hosted_smoke_transcript.py#L108) | 108 | `"    assert report[\"auth_mode\"] == \"local_loopback_dev_bypass\""` | — |
| [SRC-1BB2FDD5B7-L000109](../../tests/test_hosted_smoke_transcript.py#L109) | 109 | `"    assert report[\"transcript\"][0][\"answer\"] == \"لا توجد إشارة شراء مؤكدة في المصادر التي تم فحصها.\""` | — |
| [SRC-1BB2FDD5B7-L000110](../../tests/test_hosted_smoke_transcript.py#L110) | 110 | `""` | — |
| [SRC-1BB2FDD5B7-L000111](../../tests/test_hosted_smoke_transcript.py#L111) | 111 | `""` | — |
| [SRC-1BB2FDD5B7-L000112](../../tests/test_hosted_smoke_transcript.py#L112) | 112 | `"def test_hosted_smoke_rejects_no_token_for_remote_host():"` | — |
| [SRC-1BB2FDD5B7-L000113](../../tests/test_hosted_smoke_transcript.py#L113) | 113 | `"    import pytest"` | — |
| [SRC-1BB2FDD5B7-L000114](../../tests/test_hosted_smoke_transcript.py#L114) | 114 | `""` | — |
| [SRC-1BB2FDD5B7-L000115](../../tests/test_hosted_smoke_transcript.py#L115) | 115 | `"    with pytest.raises(hosted_smoke_test.SmokeError, match=\"localhost/loopback\"):"` | — |
| [SRC-1BB2FDD5B7-L000116](../../tests/test_hosted_smoke_transcript.py#L116) | 116 | `"        hosted_smoke_test.run_smoke("` | — |
| [SRC-1BB2FDD5B7-L000117](../../tests/test_hosted_smoke_transcript.py#L117) | 117 | `"            \"https://omarai.example\","` | — |
| [SRC-1BB2FDD5B7-L000118](../../tests/test_hosted_smoke_transcript.py#L118) | 118 | `"            \"\","` | — |
| [SRC-1BB2FDD5B7-L000119](../../tests/test_hosted_smoke_transcript.py#L119) | 119 | `"            local_dev_no_token=True,"` | — |
| [SRC-1BB2FDD5B7-L000120](../../tests/test_hosted_smoke_transcript.py#L120) | 120 | `"        )"` | — |
## اختبارات

### FILE-EA6EC52573 — [tests/test_intent_router.py](../../tests/test_intent_router.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-EA6EC52573-L000001](../../tests/test_intent_router.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-EA6EC52573-L000002](../../tests/test_intent_router.py#L2) | 2 | `""` | — |
| [SRC-EA6EC52573-L000003](../../tests/test_intent_router.py#L3) | 3 | `"import pytest"` | — |
| [SRC-EA6EC52573-L000004](../../tests/test_intent_router.py#L4) | 4 | `""` | — |
| [SRC-EA6EC52573-L000005](../../tests/test_intent_router.py#L5) | 5 | `"from agents.intent_router import resolve_followup_query, route_intent"` | — |
| [SRC-EA6EC52573-L000006](../../tests/test_intent_router.py#L6) | 6 | `""` | — |
| [SRC-EA6EC52573-L000007](../../tests/test_intent_router.py#L7) | 7 | `""` | — |
| [SRC-EA6EC52573-L000008](../../tests/test_intent_router.py#L8) | 8 | `"@pytest.mark.parametrize("` | — |
| [SRC-EA6EC52573-L000009](../../tests/test_intent_router.py#L9) | 9 | `"    (\"question\", \"expected\"),"` | — |
| [SRC-EA6EC52573-L000010](../../tests/test_intent_router.py#L10) | 10 | `"    ["` | — |
| [SRC-EA6EC52573-L000011](../../tests/test_intent_router.py#L11) | 11 | `"        (\"ازيك؟ عامل ايه النهاردة؟\", \"LOCAL\"),"` | — |
| [SRC-EA6EC52573-L000012](../../tests/test_intent_router.py#L12) | 12 | `"        (\"Thanks, that helps.\", \"LOCAL\"),"` | — |
| [SRC-EA6EC52573-L000013](../../tests/test_intent_router.py#L13) | 13 | `"        (\"ما عاصمة مصر؟\", \"MODEL_ONLY\"),"` | — |
| [SRC-EA6EC52573-L000014](../../tests/test_intent_router.py#L14) | 14 | `"        (\"كام سعرها؟\", \"CLARIFY\"),"` | — |
| [SRC-EA6EC52573-L000015](../../tests/test_intent_router.py#L15) | 15 | `"        (\"قارنهم\", \"CLARIFY\"),"` | — |
| [SRC-EA6EC52573-L000016](../../tests/test_intent_router.py#L16) | 16 | `"        (\"ما سعر الهاتف اليوم في مصر؟\", \"WEB_SIMPLE\"),"` | — |
| [SRC-EA6EC52573-L000017](../../tests/test_intent_router.py#L17) | 17 | `"        ("` | — |
| [SRC-EA6EC52573-L000018](../../tests/test_intent_router.py#L18) | 18 | `"            \"قارن بين iPhone 17 وSamsung S26 من حيث السعر والبطارية والكاميرا\","` | — |
| [SRC-EA6EC52573-L000019](../../tests/test_intent_router.py#L19) | 19 | `"            \"WEB_DEEP\","` | — |
| [SRC-EA6EC52573-L000020](../../tests/test_intent_router.py#L20) | 20 | `"        ),"` | — |
| [SRC-EA6EC52573-L000021](../../tests/test_intent_router.py#L21) | 21 | `"    ],"` | — |
| [SRC-EA6EC52573-L000022](../../tests/test_intent_router.py#L22) | 22 | `")"` | — |
| [SRC-EA6EC52573-L000023](../../tests/test_intent_router.py#L23) | 23 | `"def test_deterministic_intent_routes(question: str, expected: str) -> None:"` | — |
| [SRC-EA6EC52573-L000024](../../tests/test_intent_router.py#L24) | 24 | `"    decision = route_intent(question)"` | — |
| [SRC-EA6EC52573-L000025](../../tests/test_intent_router.py#L25) | 25 | `"    assert decision[\"route\"] == expected"` | — |
| [SRC-EA6EC52573-L000026](../../tests/test_intent_router.py#L26) | 26 | `"    assert decision[\"reason\"]"` | — |
| [SRC-EA6EC52573-L000027](../../tests/test_intent_router.py#L27) | 27 | `""` | — |
| [SRC-EA6EC52573-L000028](../../tests/test_intent_router.py#L28) | 28 | `""` | — |
| [SRC-EA6EC52573-L000029](../../tests/test_intent_router.py#L29) | 29 | `"@pytest.mark.parametrize("` | — |
| [SRC-EA6EC52573-L000030](../../tests/test_intent_router.py#L30) | 30 | `"    (\"question\", \"expected\"),"` | — |
| [SRC-EA6EC52573-L000031](../../tests/test_intent_router.py#L31) | 31 | `"    ["` | — |
| [SRC-EA6EC52573-L000032](../../tests/test_intent_router.py#L32) | 32 | `"        (\"ابحث عن عميل يريد شراء شقة في العاصمة الإدارية بمصر\", \"LEAD_GENERATION\"),"` | — |
| [SRC-EA6EC52573-L000033](../../tests/test_intent_router.py#L33) | 33 | `"        (\"ابحث عن شقق للبيع في العاصمة الإدارية\", \"WEB_SIMPLE\"),"` | — |
| [SRC-EA6EC52573-L000034](../../tests/test_intent_router.py#L34) | 34 | `"        (\"Find buyers looking to buy apartments in New Capital\", \"LEAD_GENERATION\"),"` | — |
| [SRC-EA6EC52573-L000035](../../tests/test_intent_router.py#L35) | 35 | `"        (\"لخص الصفحة https://example.com/article\", \"WEB_SIMPLE\"),"` | — |
| [SRC-EA6EC52573-L000036](../../tests/test_intent_router.py#L36) | 36 | `"        (\"Summarize this page https://example.com/article\", \"WEB_SIMPLE\"),"` | — |
| [SRC-EA6EC52573-L000037](../../tests/test_intent_router.py#L37) | 37 | `"        (\"لخص النص التالي: هذا نص تجريبي\", \"MODEL_ONLY\"),"` | — |
| [SRC-EA6EC52573-L000038](../../tests/test_intent_router.py#L38) | 38 | `"    ],"` | — |
| [SRC-EA6EC52573-L000039](../../tests/test_intent_router.py#L39) | 39 | `")"` | — |
| [SRC-EA6EC52573-L000040](../../tests/test_intent_router.py#L40) | 40 | `"def test_lead_generation_and_summarization_routes(question: str, expected: str) -> None:"` | — |
| [SRC-EA6EC52573-L000041](../../tests/test_intent_router.py#L41) | 41 | `"    decision = route_intent(question)"` | — |
| [SRC-EA6EC52573-L000042](../../tests/test_intent_router.py#L42) | 42 | `"    assert decision[\"route\"] == expected"` | — |
| [SRC-EA6EC52573-L000043](../../tests/test_intent_router.py#L43) | 43 | `"    assert decision[\"reason\"]"` | — |
| [SRC-EA6EC52573-L000044](../../tests/test_intent_router.py#L44) | 44 | `""` | — |
| [SRC-EA6EC52573-L000045](../../tests/test_intent_router.py#L45) | 45 | `""` | — |
| [SRC-EA6EC52573-L000046](../../tests/test_intent_router.py#L46) | 46 | `"def test_generic_explanation_of_lead_generation_is_not_a_lead_search() -> None:"` | — |
| [SRC-EA6EC52573-L000047](../../tests/test_intent_router.py#L47) | 47 | `"    assert route_intent(\"What is lead generation?\")[\"route\"] == \"MODEL_ONLY\""` | — |
| [SRC-EA6EC52573-L000048](../../tests/test_intent_router.py#L48) | 48 | `"    assert route_intent(\"Create a prospect list for apartment buyers\")[\"route\"] == \"LEAD_GENERATION\""` | — |
| [SRC-EA6EC52573-L000049](../../tests/test_intent_router.py#L49) | 49 | `""` | — |
| [SRC-EA6EC52573-L000050](../../tests/test_intent_router.py#L50) | 50 | `""` | — |
| [SRC-EA6EC52573-L000051](../../tests/test_intent_router.py#L51) | 51 | `""` | — |
| [SRC-EA6EC52573-L000052](../../tests/test_intent_router.py#L52) | 52 | `"def test_capability_question_is_local() -> None:"` | — |
| [SRC-EA6EC52573-L000053](../../tests/test_intent_router.py#L53) | 53 | `"    decision = route_intent("` | — |
| [SRC-EA6EC52573-L000054](../../tests/test_intent_router.py#L54) | 54 | `"        \"كيف تستطيع مساعدتي؟\","` | — |
| [SRC-EA6EC52573-L000055](../../tests/test_intent_router.py#L55) | 55 | `"        capability_question=True,"` | — |
| [SRC-EA6EC52573-L000056](../../tests/test_intent_router.py#L56) | 56 | `"        requires_web=False,"` | — |
| [SRC-EA6EC52573-L000057](../../tests/test_intent_router.py#L57) | 57 | `"    )"` | — |
| [SRC-EA6EC52573-L000058](../../tests/test_intent_router.py#L58) | 58 | `"    assert decision[\"route\"] == \"LOCAL\""` | — |
| [SRC-EA6EC52573-L000059](../../tests/test_intent_router.py#L59) | 59 | `"    assert decision[\"reason\"] == \"capability_question\""` | — |
| [SRC-EA6EC52573-L000060](../../tests/test_intent_router.py#L60) | 60 | `""` | — |
| [SRC-EA6EC52573-L000061](../../tests/test_intent_router.py#L61) | 61 | `""` | — |
| [SRC-EA6EC52573-L000062](../../tests/test_intent_router.py#L62) | 62 | `"def test_ambiguous_followup_uses_existing_conversation_context() -> None:"` | — |
| [SRC-EA6EC52573-L000063](../../tests/test_intent_router.py#L63) | 63 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000064](../../tests/test_intent_router.py#L64) | 64 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر iPhone 17 في مصر\"},"` | — |
| [SRC-EA6EC52573-L000065](../../tests/test_intent_router.py#L65) | 65 | `"        {\"role\": \"assistant\", \"content\": \"نتحدث عن هاتف iPhone 17 في السوق المصري.\"},"` | — |
| [SRC-EA6EC52573-L000066](../../tests/test_intent_router.py#L66) | 66 | `"    ]"` | — |
| [SRC-EA6EC52573-L000067](../../tests/test_intent_router.py#L67) | 67 | `"    decision = route_intent(\"كام سعرها؟\", history, requires_web=True)"` | — |
| [SRC-EA6EC52573-L000068](../../tests/test_intent_router.py#L68) | 68 | `"    assert decision[\"route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-EA6EC52573-L000069](../../tests/test_intent_router.py#L69) | 69 | `"    assert decision[\"context_available\"] is True"` | — |
| [SRC-EA6EC52573-L000070](../../tests/test_intent_router.py#L70) | 70 | `"    assert decision[\"needs_clarification\"] is False"` | — |
| [SRC-EA6EC52573-L000071](../../tests/test_intent_router.py#L71) | 71 | `""` | — |
| [SRC-EA6EC52573-L000072](../../tests/test_intent_router.py#L72) | 72 | `""` | — |
| [SRC-EA6EC52573-L000073](../../tests/test_intent_router.py#L73) | 73 | `"def test_comparison_followup_requires_context_before_deep_search() -> None:"` | — |
| [SRC-EA6EC52573-L000074](../../tests/test_intent_router.py#L74) | 74 | `"    assert route_intent(\"قارنهم\")[\"route\"] == \"CLARIFY\""` | — |
| [SRC-EA6EC52573-L000075](../../tests/test_intent_router.py#L75) | 75 | `"    history = [{\"role\": \"user\", \"content\": \"قارن iPhone 17 وSamsung S26\"}]"` | — |
| [SRC-EA6EC52573-L000076](../../tests/test_intent_router.py#L76) | 76 | `"    decision = route_intent(\"قارنهم\", history)"` | — |
| [SRC-EA6EC52573-L000077](../../tests/test_intent_router.py#L77) | 77 | `"    assert decision[\"route\"] == \"WEB_DEEP\""` | — |
| [SRC-EA6EC52573-L000078](../../tests/test_intent_router.py#L78) | 78 | `"    assert decision[\"context_available\"] is True"` | — |
| [SRC-EA6EC52573-L000079](../../tests/test_intent_router.py#L79) | 79 | `""` | — |
| [SRC-EA6EC52573-L000080](../../tests/test_intent_router.py#L80) | 80 | `""` | — |
| [SRC-EA6EC52573-L000081](../../tests/test_intent_router.py#L81) | 81 | `"def test_ambiguous_followup_does_not_reuse_stale_topic_after_acknowledgment() -> None:"` | — |
| [SRC-EA6EC52573-L000082](../../tests/test_intent_router.py#L82) | 82 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000083](../../tests/test_intent_router.py#L83) | 83 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر iPhone 17 في مصر\"},"` | — |
| [SRC-EA6EC52573-L000084](../../tests/test_intent_router.py#L84) | 84 | `"        {\"role\": \"assistant\", \"content\": \"سأساعدك في العثور على أسعار حديثة.\"},"` | — |
| [SRC-EA6EC52573-L000085](../../tests/test_intent_router.py#L85) | 85 | `"        {\"role\": \"user\", \"content\": \"شكرا\"},"` | — |
| [SRC-EA6EC52573-L000086](../../tests/test_intent_router.py#L86) | 86 | `"        {\"role\": \"assistant\", \"content\": \"العفو.\"},"` | — |
| [SRC-EA6EC52573-L000087](../../tests/test_intent_router.py#L87) | 87 | `"    ]"` | — |
| [SRC-EA6EC52573-L000088](../../tests/test_intent_router.py#L88) | 88 | `"    decision = route_intent(\"كام سعرها؟\", history, requires_web=True)"` | — |
| [SRC-EA6EC52573-L000089](../../tests/test_intent_router.py#L89) | 89 | `"    assert decision[\"route\"] == \"CLARIFY\""` | — |
| [SRC-EA6EC52573-L000090](../../tests/test_intent_router.py#L90) | 90 | `"    assert decision[\"context_available\"] is False"` | — |
| [SRC-EA6EC52573-L000091](../../tests/test_intent_router.py#L91) | 91 | `""` | — |
| [SRC-EA6EC52573-L000092](../../tests/test_intent_router.py#L92) | 92 | `""` | — |
| [SRC-EA6EC52573-L000093](../../tests/test_intent_router.py#L93) | 93 | `"def test_explicit_mode_overrides_conversational_shortcuts() -> None:"` | — |
| [SRC-EA6EC52573-L000094](../../tests/test_intent_router.py#L94) | 94 | `"    assert route_intent(\"ازيك؟\", mode=\"deep\")[\"route\"] == \"WEB_DEEP\""` | — |
| [SRC-EA6EC52573-L000095](../../tests/test_intent_router.py#L95) | 95 | `"    assert route_intent(\"ما سعر الهاتف؟\", mode=\"latest\")[\"route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-EA6EC52573-L000096](../../tests/test_intent_router.py#L96) | 96 | `""` | — |
| [SRC-EA6EC52573-L000097](../../tests/test_intent_router.py#L97) | 97 | `""` | — |
| [SRC-EA6EC52573-L000098](../../tests/test_intent_router.py#L98) | 98 | `"@pytest.mark.parametrize("` | — |
| [SRC-EA6EC52573-L000099](../../tests/test_intent_router.py#L99) | 99 | `"    (\"question\", \"expected_route\", \"expected_reason\"),"` | — |
| [SRC-EA6EC52573-L000100](../../tests/test_intent_router.py#L100) | 100 | `"    ["` | — |
| [SRC-EA6EC52573-L000101](../../tests/test_intent_router.py#L101) | 101 | `"        ("` | — |
| [SRC-EA6EC52573-L000102](../../tests/test_intent_router.py#L102) | 102 | `"            \"لخص الصفحة https://example.com/article\","` | — |
| [SRC-EA6EC52573-L000103](../../tests/test_intent_router.py#L103) | 103 | `"            \"WEB_SIMPLE\","` | — |
| [SRC-EA6EC52573-L000104](../../tests/test_intent_router.py#L104) | 104 | `"            \"summarization_request\","` | — |
| [SRC-EA6EC52573-L000105](../../tests/test_intent_router.py#L105) | 105 | `"        ),"` | — |
| [SRC-EA6EC52573-L000106](../../tests/test_intent_router.py#L106) | 106 | `"        ("` | — |
| [SRC-EA6EC52573-L000107](../../tests/test_intent_router.py#L107) | 107 | `"            \"Summarize this page https://example.com/article\","` | — |
| [SRC-EA6EC52573-L000108](../../tests/test_intent_router.py#L108) | 108 | `"            \"WEB_SIMPLE\","` | — |
| [SRC-EA6EC52573-L000109](../../tests/test_intent_router.py#L109) | 109 | `"            \"summarization_request\","` | — |
| [SRC-EA6EC52573-L000110](../../tests/test_intent_router.py#L110) | 110 | `"        ),"` | — |
| [SRC-EA6EC52573-L000111](../../tests/test_intent_router.py#L111) | 111 | `"        (\"لخص الصفحة\", \"CLARIFY\", \"missing_summarization_input\"),"` | — |
| [SRC-EA6EC52573-L000112](../../tests/test_intent_router.py#L112) | 112 | `"        (\"لخص لي هذا الرابط\", \"CLARIFY\", \"missing_summarization_input\"),"` | — |
| [SRC-EA6EC52573-L000113](../../tests/test_intent_router.py#L113) | 113 | `"        (\"summarize the page\", \"CLARIFY\", \"missing_summarization_input\"),"` | — |
| [SRC-EA6EC52573-L000114](../../tests/test_intent_router.py#L114) | 114 | `"        (\"تلخيص المقال\", \"CLARIFY\", \"missing_summarization_input\"),"` | — |
| [SRC-EA6EC52573-L000115](../../tests/test_intent_router.py#L115) | 115 | `"        (\"لخص النص التالي: هذا نص تجريبي\", \"MODEL_ONLY\", \"stable_knowledge_or_conversation\"),"` | — |
| [SRC-EA6EC52573-L000116](../../tests/test_intent_router.py#L116) | 116 | `"        (\"Summarize this text: the test content is here\", \"MODEL_ONLY\", \"stable_knowledge_or_conversation\"),"` | — |
| [SRC-EA6EC52573-L000117](../../tests/test_intent_router.py#L117) | 117 | `"    ],"` | — |
| [SRC-EA6EC52573-L000118](../../tests/test_intent_router.py#L118) | 118 | `")"` | — |
| [SRC-EA6EC52573-L000119](../../tests/test_intent_router.py#L119) | 119 | `"def test_summarization_routing_respects_page_text_and_missing_input("` | — |
| [SRC-EA6EC52573-L000120](../../tests/test_intent_router.py#L120) | 120 | `"    question: str, expected_route: str, expected_reason: str"` | — |
| [SRC-EA6EC52573-L000121](../../tests/test_intent_router.py#L121) | 121 | `") -> None:"` | — |
| [SRC-EA6EC52573-L000122](../../tests/test_intent_router.py#L122) | 122 | `"    decision = route_intent(question, [])"` | — |
| [SRC-EA6EC52573-L000123](../../tests/test_intent_router.py#L123) | 123 | `"    assert decision[\"route\"] == expected_route"` | — |
| [SRC-EA6EC52573-L000124](../../tests/test_intent_router.py#L124) | 124 | `"    assert decision[\"reason\"] == expected_reason"` | — |
| [SRC-EA6EC52573-L000125](../../tests/test_intent_router.py#L125) | 125 | `""` | — |
| [SRC-EA6EC52573-L000126](../../tests/test_intent_router.py#L126) | 126 | `""` | — |
| [SRC-EA6EC52573-L000127](../../tests/test_intent_router.py#L127) | 127 | `"@pytest.mark.parametrize("` | — |
| [SRC-EA6EC52573-L000128](../../tests/test_intent_router.py#L128) | 128 | `"    \"question\","` | — |
| [SRC-EA6EC52573-L000129](../../tests/test_intent_router.py#L129) | 129 | `"    ["` | — |
| [SRC-EA6EC52573-L000130](../../tests/test_intent_router.py#L130) | 130 | `"        \"فين؟\","` | — |
| [SRC-EA6EC52573-L000131](../../tests/test_intent_router.py#L131) | 131 | `"        \"فين هي؟\","` | — |
| [SRC-EA6EC52573-L000132](../../tests/test_intent_router.py#L132) | 132 | `"        \"مكانها فين؟\","` | — |
| [SRC-EA6EC52573-L000133](../../tests/test_intent_router.py#L133) | 133 | `"        \"هل فيه ضمان؟\","` | — |
| [SRC-EA6EC52573-L000134](../../tests/test_intent_router.py#L134) | 134 | `"        \"هل لها ضمان؟\","` | — |
| [SRC-EA6EC52573-L000135](../../tests/test_intent_router.py#L135) | 135 | `"        \"ضمانها إيه؟\","` | — |
| [SRC-EA6EC52573-L000136](../../tests/test_intent_router.py#L136) | 136 | `"        \"Where is it?\","` | — |
| [SRC-EA6EC52573-L000137](../../tests/test_intent_router.py#L137) | 137 | `"        \"Does it have a warranty?\","` | — |
| [SRC-EA6EC52573-L000138](../../tests/test_intent_router.py#L138) | 138 | `"    ],"` | — |
| [SRC-EA6EC52573-L000139](../../tests/test_intent_router.py#L139) | 139 | `")"` | — |
| [SRC-EA6EC52573-L000140](../../tests/test_intent_router.py#L140) | 140 | `"def test_missing_referent_questions_clarify_without_context(question: str) -> None:"` | — |
| [SRC-EA6EC52573-L000141](../../tests/test_intent_router.py#L141) | 141 | `"    decision = route_intent(question, history=None, mode=\"auto\", requires_web=True)"` | — |
| [SRC-EA6EC52573-L000142](../../tests/test_intent_router.py#L142) | 142 | `"    assert decision[\"route\"] == \"CLARIFY\""` | — |
| [SRC-EA6EC52573-L000143](../../tests/test_intent_router.py#L143) | 143 | `"    assert decision[\"needs_clarification\"] is True"` | — |
| [SRC-EA6EC52573-L000144](../../tests/test_intent_router.py#L144) | 144 | `"    assert decision[\"context_available\"] is False"` | — |
| [SRC-EA6EC52573-L000145](../../tests/test_intent_router.py#L145) | 145 | `""` | — |
| [SRC-EA6EC52573-L000146](../../tests/test_intent_router.py#L146) | 146 | `""` | — |
| [SRC-EA6EC52573-L000147](../../tests/test_intent_router.py#L147) | 147 | `"@pytest.mark.parametrize(\"question\", [\"فين؟\", \"هل فيه ضمان؟\", \"كام سعرها؟\"])"` | — |
| [SRC-EA6EC52573-L000148](../../tests/test_intent_router.py#L148) | 148 | `"def test_missing_referent_still_clarifies_in_explicit_search_mode(question: str) -> None:"` | — |
| [SRC-EA6EC52573-L000149](../../tests/test_intent_router.py#L149) | 149 | `"    decision = route_intent(question, history=None, mode=\"deep\")"` | — |
| [SRC-EA6EC52573-L000150](../../tests/test_intent_router.py#L150) | 150 | `"    assert decision[\"route\"] == \"CLARIFY\""` | — |
