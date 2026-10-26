# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **027**
- سجلات الأسطر: **800**
- النطاق: SRC-FA4E1423C3-L000475 إلى SRC-AAA21D04E8-L000183
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-FA4E1423C3 — [tests/test_generate_index.py](../../tests/test_generate_index.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-FA4E1423C3-L000475](../../tests/test_generate_index.py#L475) | 475 | `"    assert not any(\"sample should be ignored\" in desc for _, _, desc in summarized)"` | — |
## اختبارات

### FILE-829A979985 — [tests/test_generation_acceptance_matrix.py](../../tests/test_generation_acceptance_matrix.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-829A979985-L000001](../../tests/test_generation_acceptance_matrix.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-829A979985-L000002](../../tests/test_generation_acceptance_matrix.py#L2) | 2 | `""` | — |
| [SRC-829A979985-L000003](../../tests/test_generation_acceptance_matrix.py#L3) | 3 | `"import json"` | — |
| [SRC-829A979985-L000004](../../tests/test_generation_acceptance_matrix.py#L4) | 4 | `""` | — |
| [SRC-829A979985-L000005](../../tests/test_generation_acceptance_matrix.py#L5) | 5 | `"import pytest"` | — |
| [SRC-829A979985-L000006](../../tests/test_generation_acceptance_matrix.py#L6) | 6 | `""` | — |
| [SRC-829A979985-L000007](../../tests/test_generation_acceptance_matrix.py#L7) | 7 | `"from agents.request_budget import RequestBudget, RequestBudgetExceeded"` | — |
| [SRC-829A979985-L000008](../../tests/test_generation_acceptance_matrix.py#L8) | 8 | `"from agents.web_agent import WebAgent"` | — |
| [SRC-829A979985-L000009](../../tests/test_generation_acceptance_matrix.py#L9) | 9 | `""` | — |
| [SRC-829A979985-L000010](../../tests/test_generation_acceptance_matrix.py#L10) | 10 | `""` | — |
| [SRC-829A979985-L000011](../../tests/test_generation_acceptance_matrix.py#L11) | 11 | `"class FakeCompletionResponse:"` | — |
| [SRC-829A979985-L000012](../../tests/test_generation_acceptance_matrix.py#L12) | 12 | `"    def __init__("` | — |
| [SRC-829A979985-L000013](../../tests/test_generation_acceptance_matrix.py#L13) | 13 | `"        self,"` | — |
| [SRC-829A979985-L000014](../../tests/test_generation_acceptance_matrix.py#L14) | 14 | `"        content: str,"` | — |
| [SRC-829A979985-L000015](../../tests/test_generation_acceptance_matrix.py#L15) | 15 | `"        finish_reason: str \| None,"` | — |
| [SRC-829A979985-L000016](../../tests/test_generation_acceptance_matrix.py#L16) | 16 | `"        *,"` | — |
| [SRC-829A979985-L000017](../../tests/test_generation_acceptance_matrix.py#L17) | 17 | `"        include_reason: bool = True,"` | — |
| [SRC-829A979985-L000018](../../tests/test_generation_acceptance_matrix.py#L18) | 18 | `"    ) -> None:"` | — |
| [SRC-829A979985-L000019](../../tests/test_generation_acceptance_matrix.py#L19) | 19 | `"        choice = {\"message\": {\"content\": content}}"` | — |
| [SRC-829A979985-L000020](../../tests/test_generation_acceptance_matrix.py#L20) | 20 | `"        if include_reason:"` | — |
| [SRC-829A979985-L000021](../../tests/test_generation_acceptance_matrix.py#L21) | 21 | `"            choice[\"finish_reason\"] = finish_reason"` | — |
| [SRC-829A979985-L000022](../../tests/test_generation_acceptance_matrix.py#L22) | 22 | `"        self.body = json.dumps({\"choices\": [choice]}).encode(\"utf-8\")"` | — |
| [SRC-829A979985-L000023](../../tests/test_generation_acceptance_matrix.py#L23) | 23 | `""` | — |
| [SRC-829A979985-L000024](../../tests/test_generation_acceptance_matrix.py#L24) | 24 | `"    def __enter__(self):"` | — |
| [SRC-829A979985-L000025](../../tests/test_generation_acceptance_matrix.py#L25) | 25 | `"        return self"` | — |
| [SRC-829A979985-L000026](../../tests/test_generation_acceptance_matrix.py#L26) | 26 | `""` | — |
| [SRC-829A979985-L000027](../../tests/test_generation_acceptance_matrix.py#L27) | 27 | `"    def __exit__(self, exc_type, exc, traceback):"` | — |
| [SRC-829A979985-L000028](../../tests/test_generation_acceptance_matrix.py#L28) | 28 | `"        return False"` | — |
| [SRC-829A979985-L000029](../../tests/test_generation_acceptance_matrix.py#L29) | 29 | `""` | — |
| [SRC-829A979985-L000030](../../tests/test_generation_acceptance_matrix.py#L30) | 30 | `"    def read(self, limit: int) -> bytes:"` | — |
| [SRC-829A979985-L000031](../../tests/test_generation_acceptance_matrix.py#L31) | 31 | `"        return self.body[:limit]"` | — |
| [SRC-829A979985-L000032](../../tests/test_generation_acceptance_matrix.py#L32) | 32 | `""` | — |
| [SRC-829A979985-L000033](../../tests/test_generation_acceptance_matrix.py#L33) | 33 | `""` | — |
| [SRC-829A979985-L000034](../../tests/test_generation_acceptance_matrix.py#L34) | 34 | `"def source("` | — |
| [SRC-829A979985-L000035](../../tests/test_generation_acceptance_matrix.py#L35) | 35 | `"    url: str,"` | — |
| [SRC-829A979985-L000036](../../tests/test_generation_acceptance_matrix.py#L36) | 36 | `"    domain: str,"` | — |
| [SRC-829A979985-L000037](../../tests/test_generation_acceptance_matrix.py#L37) | 37 | `"    *,"` | — |
| [SRC-829A979985-L000038](../../tests/test_generation_acceptance_matrix.py#L38) | 38 | `"    page_fetched: bool,"` | — |
| [SRC-829A979985-L000039](../../tests/test_generation_acceptance_matrix.py#L39) | 39 | `"    page_text: str = \"\","` | — |
| [SRC-829A979985-L000040](../../tests/test_generation_acceptance_matrix.py#L40) | 40 | `"    snippet: str = \"\","` | — |
| [SRC-829A979985-L000041](../../tests/test_generation_acceptance_matrix.py#L41) | 41 | `"    provider: str = \"test_provider\","` | — |
| [SRC-829A979985-L000042](../../tests/test_generation_acceptance_matrix.py#L42) | 42 | `") -> dict:"` | — |
| [SRC-829A979985-L000043](../../tests/test_generation_acceptance_matrix.py#L43) | 43 | `"    return {"` | — |
| [SRC-829A979985-L000044](../../tests/test_generation_acceptance_matrix.py#L44) | 44 | `"        \"title\": f\"نتيجة عن {domain}\","` | — |
| [SRC-829A979985-L000045](../../tests/test_generation_acceptance_matrix.py#L45) | 45 | `"        \"url\": url,"` | — |
| [SRC-829A979985-L000046](../../tests/test_generation_acceptance_matrix.py#L46) | 46 | `"        \"snippet\": snippet or page_text[:200],"` | — |
| [SRC-829A979985-L000047](../../tests/test_generation_acceptance_matrix.py#L47) | 47 | `"        \"page_text\": page_text,"` | — |
| [SRC-829A979985-L000048](../../tests/test_generation_acceptance_matrix.py#L48) | 48 | `"        \"page_fetched\": page_fetched,"` | — |
| [SRC-829A979985-L000049](../../tests/test_generation_acceptance_matrix.py#L49) | 49 | `"        \"providers\": [provider],"` | — |
| [SRC-829A979985-L000050](../../tests/test_generation_acceptance_matrix.py#L50) | 50 | `"        \"queries\": [\"قارن بين سعر المنتج ومساحته\"],"` | — |
| [SRC-829A979985-L000051](../../tests/test_generation_acceptance_matrix.py#L51) | 51 | `"        \"domain\": domain,"` | — |
| [SRC-829A979985-L000052](../../tests/test_generation_acceptance_matrix.py#L52) | 52 | `"        \"source_class\": \"general\","` | — |
| [SRC-829A979985-L000053](../../tests/test_generation_acceptance_matrix.py#L53) | 53 | `"        \"platform\": \"web\","` | — |
| [SRC-829A979985-L000054](../../tests/test_generation_acceptance_matrix.py#L54) | 54 | `"        \"published_at\": \"\","` | — |
| [SRC-829A979985-L000055](../../tests/test_generation_acceptance_matrix.py#L55) | 55 | `"        \"rank_score\": 0.8,"` | — |
| [SRC-829A979985-L000056](../../tests/test_generation_acceptance_matrix.py#L56) | 56 | `"    }"` | — |
| [SRC-829A979985-L000057](../../tests/test_generation_acceptance_matrix.py#L57) | 57 | `""` | — |
| [SRC-829A979985-L000058](../../tests/test_generation_acceptance_matrix.py#L58) | 58 | `""` | — |
| [SRC-829A979985-L000059](../../tests/test_generation_acceptance_matrix.py#L59) | 59 | `"@pytest.mark.parametrize("` | — |
| [SRC-829A979985-L000060](../../tests/test_generation_acceptance_matrix.py#L60) | 60 | `"    \"finish_reason\","` | — |
| [SRC-829A979985-L000061](../../tests/test_generation_acceptance_matrix.py#L61) | 61 | `"    [\"tool_calls\", \"function_call\", \"error\", \"abort\", \"cancelled\", \"vendor_specific_done\"],"` | — |
| [SRC-829A979985-L000062](../../tests/test_generation_acceptance_matrix.py#L62) | 62 | `")"` | — |
| [SRC-829A979985-L000063](../../tests/test_generation_acceptance_matrix.py#L63) | 63 | `"def test_only_normal_stop_is_accepted_as_a_complete_text_answer("` | — |
| [SRC-829A979985-L000064](../../tests/test_generation_acceptance_matrix.py#L64) | 64 | `"    monkeypatch, finish_reason"` | — |
| [SRC-829A979985-L000065](../../tests/test_generation_acceptance_matrix.py#L65) | 65 | `"):"` | — |
| [SRC-829A979985-L000066](../../tests/test_generation_acceptance_matrix.py#L66) | 66 | `"    agent = WebAgent()"` | — |
| [SRC-829A979985-L000067](../../tests/test_generation_acceptance_matrix.py#L67) | 67 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-829A979985-L000068](../../tests/test_generation_acceptance_matrix.py#L68) | 68 | `"    agent.fallback_model = \"\""` | — |
| [SRC-829A979985-L000069](../../tests/test_generation_acceptance_matrix.py#L69) | 69 | `"    partial_text = \"نص لا يجب قبوله كإجابة نهائية\""` | — |
| [SRC-829A979985-L000070](../../tests/test_generation_acceptance_matrix.py#L70) | 70 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000071](../../tests/test_generation_acceptance_matrix.py#L71) | 71 | `"        \"agents.web_agent.urllib.request.urlopen\","` | — |
| [SRC-829A979985-L000072](../../tests/test_generation_acceptance_matrix.py#L72) | 72 | `"        lambda request, timeout: FakeCompletionResponse(partial_text, finish_reason),"` | — |
| [SRC-829A979985-L000073](../../tests/test_generation_acceptance_matrix.py#L73) | 73 | `"    )"` | — |
| [SRC-829A979985-L000074](../../tests/test_generation_acceptance_matrix.py#L74) | 74 | `""` | — |
| [SRC-829A979985-L000075](../../tests/test_generation_acceptance_matrix.py#L75) | 75 | `"    with pytest.raises(RuntimeError):"` | — |
| [SRC-829A979985-L000076](../../tests/test_generation_acceptance_matrix.py#L76) | 76 | `"        agent._request_completion("` | — |
| [SRC-829A979985-L000077](../../tests/test_generation_acceptance_matrix.py#L77) | 77 | `"            [{\"role\": \"user\", \"content\": \"اختبار\"}],"` | — |
| [SRC-829A979985-L000078](../../tests/test_generation_acceptance_matrix.py#L78) | 78 | `"            model=\"primary/model\","` | — |
| [SRC-829A979985-L000079](../../tests/test_generation_acceptance_matrix.py#L79) | 79 | `"        )"` | — |
| [SRC-829A979985-L000080](../../tests/test_generation_acceptance_matrix.py#L80) | 80 | `""` | — |
| [SRC-829A979985-L000081](../../tests/test_generation_acceptance_matrix.py#L81) | 81 | `"    assert agent.model_usage == []"` | — |
| [SRC-829A979985-L000082](../../tests/test_generation_acceptance_matrix.py#L82) | 82 | `"    assert agent.generation_diagnostics == ["` | — |
| [SRC-829A979985-L000083](../../tests/test_generation_acceptance_matrix.py#L83) | 83 | `"        {"` | — |
| [SRC-829A979985-L000084](../../tests/test_generation_acceptance_matrix.py#L84) | 84 | `"            \"attempt_number\": 1,"` | — |
| [SRC-829A979985-L000085](../../tests/test_generation_acceptance_matrix.py#L85) | 85 | `"            \"requested_model\": \"primary/model\","` | — |
| [SRC-829A979985-L000086](../../tests/test_generation_acceptance_matrix.py#L86) | 86 | `"            \"attempted_model\": \"primary/model\","` | — |
| [SRC-829A979985-L000087](../../tests/test_generation_acceptance_matrix.py#L87) | 87 | `"            \"fallback_used\": False,"` | — |
| [SRC-829A979985-L000088](../../tests/test_generation_acceptance_matrix.py#L88) | 88 | `"            \"request_started\": True,"` | — |
| [SRC-829A979985-L000089](../../tests/test_generation_acceptance_matrix.py#L89) | 89 | `"            \"remote_response_received\": True,"` | — |
| [SRC-829A979985-L000090](../../tests/test_generation_acceptance_matrix.py#L90) | 90 | `"            \"status\": \"finish_reason_not_accepted\","` | — |
| [SRC-829A979985-L000091](../../tests/test_generation_acceptance_matrix.py#L91) | 91 | `"            \"finish_reason\": finish_reason,"` | — |
| [SRC-829A979985-L000092](../../tests/test_generation_acceptance_matrix.py#L92) | 92 | `"        }"` | — |
| [SRC-829A979985-L000093](../../tests/test_generation_acceptance_matrix.py#L93) | 93 | `"    ]"` | — |
| [SRC-829A979985-L000094](../../tests/test_generation_acceptance_matrix.py#L94) | 94 | `""` | — |
| [SRC-829A979985-L000095](../../tests/test_generation_acceptance_matrix.py#L95) | 95 | `""` | — |
| [SRC-829A979985-L000096](../../tests/test_generation_acceptance_matrix.py#L96) | 96 | `"def test_both_models_truncated_fail_without_returning_either_partial_answer(monkeypatch):"` | — |
| [SRC-829A979985-L000097](../../tests/test_generation_acceptance_matrix.py#L97) | 97 | `"    agent = WebAgent()"` | — |
| [SRC-829A979985-L000098](../../tests/test_generation_acceptance_matrix.py#L98) | 98 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-829A979985-L000099](../../tests/test_generation_acceptance_matrix.py#L99) | 99 | `"    agent.fallback_model = \"fallback/model\""` | — |
| [SRC-829A979985-L000100](../../tests/test_generation_acceptance_matrix.py#L100) | 100 | `"    calls: list[str] = []"` | — |
| [SRC-829A979985-L000101](../../tests/test_generation_acceptance_matrix.py#L101) | 101 | `""` | — |
| [SRC-829A979985-L000102](../../tests/test_generation_acceptance_matrix.py#L102) | 102 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-829A979985-L000103](../../tests/test_generation_acceptance_matrix.py#L103) | 103 | `"        model = json.loads(request.data.decode(\"utf-8\"))[\"model\"]"` | — |
| [SRC-829A979985-L000104](../../tests/test_generation_acceptance_matrix.py#L104) | 104 | `"        calls.append(model)"` | — |
| [SRC-829A979985-L000105](../../tests/test_generation_acceptance_matrix.py#L105) | 105 | `"        return FakeCompletionResponse(f\"نص مبتور من {model}\", \"length\")"` | — |
| [SRC-829A979985-L000106](../../tests/test_generation_acceptance_matrix.py#L106) | 106 | `""` | — |
| [SRC-829A979985-L000107](../../tests/test_generation_acceptance_matrix.py#L107) | 107 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-829A979985-L000108](../../tests/test_generation_acceptance_matrix.py#L108) | 108 | `""` | — |
| [SRC-829A979985-L000109](../../tests/test_generation_acceptance_matrix.py#L109) | 109 | `"    with pytest.raises(RuntimeError, match=\"مبتورة\"):"` | — |
| [SRC-829A979985-L000110](../../tests/test_generation_acceptance_matrix.py#L110) | 110 | `"        agent._request_completion("` | — |
| [SRC-829A979985-L000111](../../tests/test_generation_acceptance_matrix.py#L111) | 111 | `"            [{\"role\": \"user\", \"content\": \"اختبار\"}],"` | — |
| [SRC-829A979985-L000112](../../tests/test_generation_acceptance_matrix.py#L112) | 112 | `"            model=\"primary/model\","` | — |
| [SRC-829A979985-L000113](../../tests/test_generation_acceptance_matrix.py#L113) | 113 | `"        )"` | — |
| [SRC-829A979985-L000114](../../tests/test_generation_acceptance_matrix.py#L114) | 114 | `""` | — |
| [SRC-829A979985-L000115](../../tests/test_generation_acceptance_matrix.py#L115) | 115 | `"    assert calls == [\"primary/model\", \"fallback/model\"]"` | — |
| [SRC-829A979985-L000116](../../tests/test_generation_acceptance_matrix.py#L116) | 116 | `"    assert agent.model_usage == []"` | — |
| [SRC-829A979985-L000117](../../tests/test_generation_acceptance_matrix.py#L117) | 117 | `"    assert [item[\"status\"] for item in agent.generation_diagnostics] == ["` | — |
| [SRC-829A979985-L000118](../../tests/test_generation_acceptance_matrix.py#L118) | 118 | `"        \"truncated\","` | — |
| [SRC-829A979985-L000119](../../tests/test_generation_acceptance_matrix.py#L119) | 119 | `"        \"truncated\","` | — |
| [SRC-829A979985-L000120](../../tests/test_generation_acceptance_matrix.py#L120) | 120 | `"    ]"` | — |
| [SRC-829A979985-L000121](../../tests/test_generation_acceptance_matrix.py#L121) | 121 | `"    assert all(\"مبتور\" not in str(item) for item in agent.generation_diagnostics)"` | — |
| [SRC-829A979985-L000122](../../tests/test_generation_acceptance_matrix.py#L122) | 122 | `""` | — |
| [SRC-829A979985-L000123](../../tests/test_generation_acceptance_matrix.py#L123) | 123 | `""` | — |
| [SRC-829A979985-L000124](../../tests/test_generation_acceptance_matrix.py#L124) | 124 | `"def test_model_fallback_cannot_exceed_request_model_call_budget(monkeypatch):"` | — |
| [SRC-829A979985-L000125](../../tests/test_generation_acceptance_matrix.py#L125) | 125 | `"    agent = WebAgent()"` | — |
| [SRC-829A979985-L000126](../../tests/test_generation_acceptance_matrix.py#L126) | 126 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-829A979985-L000127](../../tests/test_generation_acceptance_matrix.py#L127) | 127 | `"    agent.fallback_model = \"fallback/model\""` | — |
| [SRC-829A979985-L000128](../../tests/test_generation_acceptance_matrix.py#L128) | 128 | `"    budget = RequestBudget(timeout_seconds=60, limits={\"model_calls\": 1})"` | — |
| [SRC-829A979985-L000129](../../tests/test_generation_acceptance_matrix.py#L129) | 129 | `"    agent._request_budget = budget"` | — |
| [SRC-829A979985-L000130](../../tests/test_generation_acceptance_matrix.py#L130) | 130 | `"    calls: list[str] = []"` | — |
| [SRC-829A979985-L000131](../../tests/test_generation_acceptance_matrix.py#L131) | 131 | `""` | — |
| [SRC-829A979985-L000132](../../tests/test_generation_acceptance_matrix.py#L132) | 132 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-829A979985-L000133](../../tests/test_generation_acceptance_matrix.py#L133) | 133 | `"        model = json.loads(request.data.decode(\"utf-8\"))[\"model\"]"` | — |
| [SRC-829A979985-L000134](../../tests/test_generation_acceptance_matrix.py#L134) | 134 | `"        calls.append(model)"` | — |
| [SRC-829A979985-L000135](../../tests/test_generation_acceptance_matrix.py#L135) | 135 | `"        return FakeCompletionResponse(\"محتوى مبتور\", \"length\")"` | — |
| [SRC-829A979985-L000136](../../tests/test_generation_acceptance_matrix.py#L136) | 136 | `""` | — |
| [SRC-829A979985-L000137](../../tests/test_generation_acceptance_matrix.py#L137) | 137 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-829A979985-L000138](../../tests/test_generation_acceptance_matrix.py#L138) | 138 | `""` | — |
| [SRC-829A979985-L000139](../../tests/test_generation_acceptance_matrix.py#L139) | 139 | `"    with pytest.raises(RequestBudgetExceeded):"` | — |
| [SRC-829A979985-L000140](../../tests/test_generation_acceptance_matrix.py#L140) | 140 | `"        agent._request_completion("` | — |
| [SRC-829A979985-L000141](../../tests/test_generation_acceptance_matrix.py#L141) | 141 | `"            [{\"role\": \"user\", \"content\": \"اختبار\"}],"` | — |
| [SRC-829A979985-L000142](../../tests/test_generation_acceptance_matrix.py#L142) | 142 | `"            model=\"primary/model\","` | — |
| [SRC-829A979985-L000143](../../tests/test_generation_acceptance_matrix.py#L143) | 143 | `"        )"` | — |
| [SRC-829A979985-L000144](../../tests/test_generation_acceptance_matrix.py#L144) | 144 | `""` | — |
| [SRC-829A979985-L000145](../../tests/test_generation_acceptance_matrix.py#L145) | 145 | `"    assert calls == [\"primary/model\"]"` | — |
| [SRC-829A979985-L000146](../../tests/test_generation_acceptance_matrix.py#L146) | 146 | `"    assert budget.snapshot()[\"counts\"][\"model_calls\"] == 1"` | — |
| [SRC-829A979985-L000147](../../tests/test_generation_acceptance_matrix.py#L147) | 147 | `"    assert [item[\"status\"] for item in agent.generation_diagnostics] == ["` | — |
| [SRC-829A979985-L000148](../../tests/test_generation_acceptance_matrix.py#L148) | 148 | `"        \"truncated\","` | — |
| [SRC-829A979985-L000149](../../tests/test_generation_acceptance_matrix.py#L149) | 149 | `"        \"budget_exhausted\","` | — |
| [SRC-829A979985-L000150](../../tests/test_generation_acceptance_matrix.py#L150) | 150 | `"    ]"` | — |
| [SRC-829A979985-L000151](../../tests/test_generation_acceptance_matrix.py#L151) | 151 | `"    assert agent.generation_diagnostics[1][\"request_started\"] is False"` | — |
| [SRC-829A979985-L000152](../../tests/test_generation_acceptance_matrix.py#L152) | 152 | `"    assert agent.generation_diagnostics[1][\"remote_response_received\"] is False"` | — |
| [SRC-829A979985-L000153](../../tests/test_generation_acceptance_matrix.py#L153) | 153 | `"    assert agent.model_usage == []"` | — |
| [SRC-829A979985-L000154](../../tests/test_generation_acceptance_matrix.py#L154) | 154 | `""` | — |
| [SRC-829A979985-L000155](../../tests/test_generation_acceptance_matrix.py#L155) | 155 | `""` | — |
| [SRC-829A979985-L000156](../../tests/test_generation_acceptance_matrix.py#L156) | 156 | `"def test_capability_snapshot_separates_configuration_from_live_health(monkeypatch):"` | — |
| [SRC-829A979985-L000157](../../tests/test_generation_acceptance_matrix.py#L157) | 157 | `"    agent = WebAgent()"` | — |
| [SRC-829A979985-L000158](../../tests/test_generation_acceptance_matrix.py#L158) | 158 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000159](../../tests/test_generation_acceptance_matrix.py#L159) | 159 | `"        agent,"` | — |
| [SRC-829A979985-L000160](../../tests/test_generation_acceptance_matrix.py#L160) | 160 | `"        \"status\","` | — |
| [SRC-829A979985-L000161](../../tests/test_generation_acceptance_matrix.py#L161) | 161 | `"        lambda: {"` | — |
| [SRC-829A979985-L000162](../../tests/test_generation_acceptance_matrix.py#L162) | 162 | `"            \"web_search_ready\": True,"` | — |
| [SRC-829A979985-L000163](../../tests/test_generation_acceptance_matrix.py#L163) | 163 | `"            \"language_model_configured\": True,"` | — |
| [SRC-829A979985-L000164](../../tests/test_generation_acceptance_matrix.py#L164) | 164 | `"            \"deepseek_search_api_configured\": True,"` | — |
| [SRC-829A979985-L000165](../../tests/test_generation_acceptance_matrix.py#L165) | 165 | `"            \"brave_search_api_configured\": True,"` | — |
| [SRC-829A979985-L000166](../../tests/test_generation_acceptance_matrix.py#L166) | 166 | `"            \"tavily_search_api_configured\": False,"` | — |
| [SRC-829A979985-L000167](../../tests/test_generation_acceptance_matrix.py#L167) | 167 | `"            \"openrouter_web_search_enabled\": False,"` | — |
| [SRC-829A979985-L000168](../../tests/test_generation_acceptance_matrix.py#L168) | 168 | `"        },"` | — |
| [SRC-829A979985-L000169](../../tests/test_generation_acceptance_matrix.py#L169) | 169 | `"    )"` | — |
| [SRC-829A979985-L000170](../../tests/test_generation_acceptance_matrix.py#L170) | 170 | `""` | — |
| [SRC-829A979985-L000171](../../tests/test_generation_acceptance_matrix.py#L171) | 171 | `"    snapshot = agent._capability_status_snapshot()"` | — |
| [SRC-829A979985-L000172](../../tests/test_generation_acceptance_matrix.py#L172) | 172 | `"    providers = {item[\"name\"]: item for item in snapshot[\"web_search\"][\"providers\"]}"` | — |
| [SRC-829A979985-L000173](../../tests/test_generation_acceptance_matrix.py#L173) | 173 | `""` | — |
| [SRC-829A979985-L000174](../../tests/test_generation_acceptance_matrix.py#L174) | 174 | `"    assert snapshot[\"web_search\"][\"implemented\"] is True"` | — |
| [SRC-829A979985-L000175](../../tests/test_generation_acceptance_matrix.py#L175) | 175 | `"    assert snapshot[\"web_search\"][\"local_dependencies_ready\"] is True"` | — |
| [SRC-829A979985-L000176](../../tests/test_generation_acceptance_matrix.py#L176) | 176 | `"    assert snapshot[\"web_search\"][\"runtime_status\"] == \"not_tested_in_this_response\""` | — |
| [SRC-829A979985-L000177](../../tests/test_generation_acceptance_matrix.py#L177) | 177 | `"    assert providers[\"duckduckgo_html\"][\"configuration_status\"] == \"built_in_no_api_key\""` | — |
| [SRC-829A979985-L000178](../../tests/test_generation_acceptance_matrix.py#L178) | 178 | `"    assert providers[\"duckduckgo_html\"][\"runtime_status\"] == \"not_tested_in_this_response\""` | — |
| [SRC-829A979985-L000179](../../tests/test_generation_acceptance_matrix.py#L179) | 179 | `"    assert providers[\"deepseek_search_api\"][\"configuration_status\"] == \"configured\""` | — |
| [SRC-829A979985-L000180](../../tests/test_generation_acceptance_matrix.py#L180) | 180 | `"    assert providers[\"deepseek_search_api\"][\"runtime_status\"] == \"not_tested_in_this_response\""` | — |
| [SRC-829A979985-L000181](../../tests/test_generation_acceptance_matrix.py#L181) | 181 | `"    assert providers[\"brave_search_api\"][\"configuration_status\"] == \"configured\""` | — |
| [SRC-829A979985-L000182](../../tests/test_generation_acceptance_matrix.py#L182) | 182 | `"    assert providers[\"brave_search_api\"][\"runtime_status\"] == \"not_tested_in_this_response\""` | — |
| [SRC-829A979985-L000183](../../tests/test_generation_acceptance_matrix.py#L183) | 183 | `"    assert providers[\"tavily_search_api\"][\"configuration_status\"] == \"not_configured\""` | — |
| [SRC-829A979985-L000184](../../tests/test_generation_acceptance_matrix.py#L184) | 184 | `"    assert providers[\"tavily_search_api\"][\"runtime_status\"] == \"not_configured\""` | — |
| [SRC-829A979985-L000185](../../tests/test_generation_acceptance_matrix.py#L185) | 185 | `"    assert providers[\"openrouter_web_search\"][\"configuration_status\"] == \"disabled\""` | — |
| [SRC-829A979985-L000186](../../tests/test_generation_acceptance_matrix.py#L186) | 186 | `"    assert providers[\"openrouter_web_search\"][\"runtime_status\"] == \"disabled\""` | — |
| [SRC-829A979985-L000187](../../tests/test_generation_acceptance_matrix.py#L187) | 187 | `""` | — |
| [SRC-829A979985-L000188](../../tests/test_generation_acceptance_matrix.py#L188) | 188 | `""` | — |
| [SRC-829A979985-L000189](../../tests/test_generation_acceptance_matrix.py#L189) | 189 | `"def test_capability_answer_discloses_optional_deepseek_search_status(monkeypatch):"` | — |
| [SRC-829A979985-L000190](../../tests/test_generation_acceptance_matrix.py#L190) | 190 | `"    agent = WebAgent()"` | — |
| [SRC-829A979985-L000191](../../tests/test_generation_acceptance_matrix.py#L191) | 191 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000192](../../tests/test_generation_acceptance_matrix.py#L192) | 192 | `"        agent,"` | — |
| [SRC-829A979985-L000193](../../tests/test_generation_acceptance_matrix.py#L193) | 193 | `"        \"status\","` | — |
| [SRC-829A979985-L000194](../../tests/test_generation_acceptance_matrix.py#L194) | 194 | `"        lambda: {"` | — |
| [SRC-829A979985-L000195](../../tests/test_generation_acceptance_matrix.py#L195) | 195 | `"            \"web_search_ready\": True,"` | — |
| [SRC-829A979985-L000196](../../tests/test_generation_acceptance_matrix.py#L196) | 196 | `"            \"language_model_configured\": True,"` | — |
| [SRC-829A979985-L000197](../../tests/test_generation_acceptance_matrix.py#L197) | 197 | `"            \"deepseek_search_api_configured\": True,"` | — |
| [SRC-829A979985-L000198](../../tests/test_generation_acceptance_matrix.py#L198) | 198 | `"            \"brave_search_api_configured\": False,"` | — |
| [SRC-829A979985-L000199](../../tests/test_generation_acceptance_matrix.py#L199) | 199 | `"            \"tavily_search_api_configured\": False,"` | — |
| [SRC-829A979985-L000200](../../tests/test_generation_acceptance_matrix.py#L200) | 200 | `"            \"openrouter_web_search_enabled\": False,"` | — |
| [SRC-829A979985-L000201](../../tests/test_generation_acceptance_matrix.py#L201) | 201 | `"        },"` | — |
| [SRC-829A979985-L000202](../../tests/test_generation_acceptance_matrix.py#L202) | 202 | `"    )"` | — |
| [SRC-829A979985-L000203](../../tests/test_generation_acceptance_matrix.py#L203) | 203 | `""` | — |
| [SRC-829A979985-L000204](../../tests/test_generation_acceptance_matrix.py#L204) | 204 | `"    result = agent.answer(\"ما محركات البحث التي تستخدمها؟\")"` | — |
| [SRC-829A979985-L000205](../../tests/test_generation_acceptance_matrix.py#L205) | 205 | `""` | — |
| [SRC-829A979985-L000206](../../tests/test_generation_acceptance_matrix.py#L206) | 206 | `"    assert result[\"kind\"] == \"capability_answer\""` | — |
| [SRC-829A979985-L000207](../../tests/test_generation_acceptance_matrix.py#L207) | 207 | `"    assert \"DeepSeek Search API\" in result[\"answer\"]"` | — |
| [SRC-829A979985-L000208](../../tests/test_generation_acceptance_matrix.py#L208) | 208 | `"    assert \"غير مختبر في هذه الإجابة\" in result[\"answer\"]"` | — |
| [SRC-829A979985-L000209](../../tests/test_generation_acceptance_matrix.py#L209) | 209 | `"    assert \"قد يستهلك استخدامًا مدفوعًا\" in result[\"answer\"]"` | — |
| [SRC-829A979985-L000210](../../tests/test_generation_acceptance_matrix.py#L210) | 210 | `"    provider = next("` | — |
| [SRC-829A979985-L000211](../../tests/test_generation_acceptance_matrix.py#L211) | 211 | `"        item for item in result[\"capability_status\"][\"web_search\"][\"providers\"]"` | — |
| [SRC-829A979985-L000212](../../tests/test_generation_acceptance_matrix.py#L212) | 212 | `"        if item[\"name\"] == \"deepseek_search_api\""` | — |
| [SRC-829A979985-L000213](../../tests/test_generation_acceptance_matrix.py#L213) | 213 | `"    )"` | — |
| [SRC-829A979985-L000214](../../tests/test_generation_acceptance_matrix.py#L214) | 214 | `"    assert provider[\"configuration_status\"] == \"configured\""` | — |
| [SRC-829A979985-L000215](../../tests/test_generation_acceptance_matrix.py#L215) | 215 | `"    assert provider[\"runtime_status\"] == \"not_tested_in_this_response\""` | — |
| [SRC-829A979985-L000216](../../tests/test_generation_acceptance_matrix.py#L216) | 216 | `""` | — |
| [SRC-829A979985-L000217](../../tests/test_generation_acceptance_matrix.py#L217) | 217 | `""` | — |
| [SRC-829A979985-L000218](../../tests/test_generation_acceptance_matrix.py#L218) | 218 | `"def test_operational_truth_overrides_a_model_claim_about_this_request(monkeypatch):"` | — |
| [SRC-829A979985-L000219](../../tests/test_generation_acceptance_matrix.py#L219) | 219 | `"    agent = WebAgent()"` | — |
| [SRC-829A979985-L000220](../../tests/test_generation_acceptance_matrix.py#L220) | 220 | `"    model_calls: list[str] = []"` | — |
| [SRC-829A979985-L000221](../../tests/test_generation_acceptance_matrix.py#L221) | 221 | `""` | — |
| [SRC-829A979985-L000222](../../tests/test_generation_acceptance_matrix.py#L222) | 222 | `"    def dishonest_model(*args, **kwargs):"` | — |
| [SRC-829A979985-L000223](../../tests/test_generation_acceptance_matrix.py#L223) | 223 | `"        model_calls.append(\"called\")"` | — |
| [SRC-829A979985-L000224](../../tests/test_generation_acceptance_matrix.py#L224) | 224 | `"        return \"نعم، بحثت في الإنترنت وتحققت من المصادر.\""` | — |
| [SRC-829A979985-L000225](../../tests/test_generation_acceptance_matrix.py#L225) | 225 | `""` | — |
| [SRC-829A979985-L000226](../../tests/test_generation_acceptance_matrix.py#L226) | 226 | `"    monkeypatch.setattr(agent, \"_request_completion\", dishonest_model)"` | — |
| [SRC-829A979985-L000227](../../tests/test_generation_acceptance_matrix.py#L227) | 227 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000228](../../tests/test_generation_acceptance_matrix.py#L228) | 228 | `"        agent,"` | — |
| [SRC-829A979985-L000229](../../tests/test_generation_acceptance_matrix.py#L229) | 229 | `"        \"_collect_research\","` | — |
| [SRC-829A979985-L000230](../../tests/test_generation_acceptance_matrix.py#L230) | 230 | `"        lambda plan: pytest.fail(\"A current-search status question must stay local\"),"` | — |
| [SRC-829A979985-L000231](../../tests/test_generation_acceptance_matrix.py#L231) | 231 | `"    )"` | — |
| [SRC-829A979985-L000232](../../tests/test_generation_acceptance_matrix.py#L232) | 232 | `""` | — |
| [SRC-829A979985-L000233](../../tests/test_generation_acceptance_matrix.py#L233) | 233 | `"    result = agent.answer(\"هل بحثت في الانترنت للاجابة الحالية؟\", mode=\"deep\")"` | — |
| [SRC-829A979985-L000234](../../tests/test_generation_acceptance_matrix.py#L234) | 234 | `""` | — |
| [SRC-829A979985-L000235](../../tests/test_generation_acceptance_matrix.py#L235) | 235 | `"    assert model_calls == []"` | — |
| [SRC-829A979985-L000236](../../tests/test_generation_acceptance_matrix.py#L236) | 236 | `"    assert result[\"search_attempted\"] is False"` | — |
| [SRC-829A979985-L000237](../../tests/test_generation_acceptance_matrix.py#L237) | 237 | `"    assert result[\"used_web_search\"] is False"` | — |
| [SRC-829A979985-L000238](../../tests/test_generation_acceptance_matrix.py#L238) | 238 | `"    assert result[\"request_execution_status\"][\"search_outcome\"] == \"not_attempted\""` | — |
| [SRC-829A979985-L000239](../../tests/test_generation_acceptance_matrix.py#L239) | 239 | `"    assert \"لم أنفّذ بحثًا حيًا للإجابة عن هذا السؤال تحديدًا\" in result[\"answer\"]"` | — |
| [SRC-829A979985-L000240](../../tests/test_generation_acceptance_matrix.py#L240) | 240 | `"    assert \"تحققت من المصادر\" not in result[\"answer\"]"` | — |
| [SRC-829A979985-L000241](../../tests/test_generation_acceptance_matrix.py#L241) | 241 | `""` | — |
| [SRC-829A979985-L000242](../../tests/test_generation_acceptance_matrix.py#L242) | 242 | `""` | — |
| [SRC-829A979985-L000243](../../tests/test_generation_acceptance_matrix.py#L243) | 243 | `"def test_generation_budget_exhaustion_preserves_partial_sources(monkeypatch):"` | — |
| [SRC-829A979985-L000244](../../tests/test_generation_acceptance_matrix.py#L244) | 244 | `"    agent = WebAgent()"` | — |
| [SRC-829A979985-L000245](../../tests/test_generation_acceptance_matrix.py#L245) | 245 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-829A979985-L000246](../../tests/test_generation_acceptance_matrix.py#L246) | 246 | `"    question = \"ابحث عن أحدث معلومات حول الطاقة المتجددة\""` | — |
| [SRC-829A979985-L000247](../../tests/test_generation_acceptance_matrix.py#L247) | 247 | `"    monkeypatch.setenv(\"OMARAI_REQUEST_MAX_MODEL_CALLS\", \"1\")"` | — |
| [SRC-829A979985-L000248](../../tests/test_generation_acceptance_matrix.py#L248) | 248 | `"    sources = ["` | — |
| [SRC-829A979985-L000249](../../tests/test_generation_acceptance_matrix.py#L249) | 249 | `"        source("` | — |
| [SRC-829A979985-L000250](../../tests/test_generation_acceptance_matrix.py#L250) | 250 | `"            \"https://one.example/energy\","` | — |
| [SRC-829A979985-L000251](../../tests/test_generation_acceptance_matrix.py#L251) | 251 | `"            \"one.example\","` | — |
| [SRC-829A979985-L000252](../../tests/test_generation_acceptance_matrix.py#L252) | 252 | `"            page_fetched=True,"` | — |
| [SRC-829A979985-L000253](../../tests/test_generation_acceptance_matrix.py#L253) | 253 | `"            page_text=\"معلومة مستخرجة من المصدر الأول عن الطاقة المتجددة.\","` | — |
| [SRC-829A979985-L000254](../../tests/test_generation_acceptance_matrix.py#L254) | 254 | `"            provider=\"duckduckgo_html\","` | — |
| [SRC-829A979985-L000255](../../tests/test_generation_acceptance_matrix.py#L255) | 255 | `"        ),"` | — |
| [SRC-829A979985-L000256](../../tests/test_generation_acceptance_matrix.py#L256) | 256 | `"        source("` | — |
| [SRC-829A979985-L000257](../../tests/test_generation_acceptance_matrix.py#L257) | 257 | `"            \"https://two.example/energy\","` | — |
| [SRC-829A979985-L000258](../../tests/test_generation_acceptance_matrix.py#L258) | 258 | `"            \"two.example\","` | — |
| [SRC-829A979985-L000259](../../tests/test_generation_acceptance_matrix.py#L259) | 259 | `"            page_fetched=False,"` | — |
| [SRC-829A979985-L000260](../../tests/test_generation_acceptance_matrix.py#L260) | 260 | `"            snippet=\"مقتطف المصدر الثاني عن الطاقة المتجددة.\","` | — |
| [SRC-829A979985-L000261](../../tests/test_generation_acceptance_matrix.py#L261) | 261 | `"            provider=\"bing_rss\","` | — |
| [SRC-829A979985-L000262](../../tests/test_generation_acceptance_matrix.py#L262) | 262 | `"        ),"` | — |
| [SRC-829A979985-L000263](../../tests/test_generation_acceptance_matrix.py#L263) | 263 | `"    ]"` | — |
| [SRC-829A979985-L000264](../../tests/test_generation_acceptance_matrix.py#L264) | 264 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000265](../../tests/test_generation_acceptance_matrix.py#L265) | 265 | `"        agent,"` | — |
| [SRC-829A979985-L000266](../../tests/test_generation_acceptance_matrix.py#L266) | 266 | `"        \"_plan_search\","` | — |
| [SRC-829A979985-L000267](../../tests/test_generation_acceptance_matrix.py#L267) | 267 | `"        lambda question, history: {"` | — |
| [SRC-829A979985-L000268](../../tests/test_generation_acceptance_matrix.py#L268) | 268 | `"            \"queries\": [question],"` | — |
| [SRC-829A979985-L000269](../../tests/test_generation_acceptance_matrix.py#L269) | 269 | `"            \"direct_urls\": [],"` | — |
| [SRC-829A979985-L000270](../../tests/test_generation_acceptance_matrix.py#L270) | 270 | `"            \"social_focus\": False,"` | — |
| [SRC-829A979985-L000271](../../tests/test_generation_acceptance_matrix.py#L271) | 271 | `"            \"freshness\": \"current\","` | — |
| [SRC-829A979985-L000272](../../tests/test_generation_acceptance_matrix.py#L272) | 272 | `"            \"depth\": \"standard\","` | — |
| [SRC-829A979985-L000273](../../tests/test_generation_acceptance_matrix.py#L273) | 273 | `"            \"platforms\": [],"` | — |
| [SRC-829A979985-L000274](../../tests/test_generation_acceptance_matrix.py#L274) | 274 | `"            \"planning_method\": \"test\","` | — |
| [SRC-829A979985-L000275](../../tests/test_generation_acceptance_matrix.py#L275) | 275 | `"        },"` | — |
| [SRC-829A979985-L000276](../../tests/test_generation_acceptance_matrix.py#L276) | 276 | `"    )"` | — |
| [SRC-829A979985-L000277](../../tests/test_generation_acceptance_matrix.py#L277) | 277 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000278](../../tests/test_generation_acceptance_matrix.py#L278) | 278 | `"        agent,"` | — |
| [SRC-829A979985-L000279](../../tests/test_generation_acceptance_matrix.py#L279) | 279 | `"        \"_collect_research\","` | — |
| [SRC-829A979985-L000280](../../tests/test_generation_acceptance_matrix.py#L280) | 280 | `"        lambda plan: ("` | — |
| [SRC-829A979985-L000281](../../tests/test_generation_acceptance_matrix.py#L281) | 281 | `"            sources,"` | — |
| [SRC-829A979985-L000282](../../tests/test_generation_acceptance_matrix.py#L282) | 282 | `"            [],"` | — |
| [SRC-829A979985-L000283](../../tests/test_generation_acceptance_matrix.py#L283) | 283 | `"            {"` | — |
| [SRC-829A979985-L000284](../../tests/test_generation_acceptance_matrix.py#L284) | 284 | `"                \"queries_planned\": 1,"` | — |
| [SRC-829A979985-L000285](../../tests/test_generation_acceptance_matrix.py#L285) | 285 | `"                \"queries_attempted\": 1,"` | — |
| [SRC-829A979985-L000286](../../tests/test_generation_acceptance_matrix.py#L286) | 286 | `"                \"search_attempted\": True,"` | — |
| [SRC-829A979985-L000287](../../tests/test_generation_acceptance_matrix.py#L287) | 287 | `"                \"search_outcome\": \"attempted_with_usable_sources\","` | — |
| [SRC-829A979985-L000288](../../tests/test_generation_acceptance_matrix.py#L288) | 288 | `"                \"unique_sources\": 2,"` | — |
| [SRC-829A979985-L000289](../../tests/test_generation_acceptance_matrix.py#L289) | 289 | `"                \"pages_fetched\": 1,"` | — |
| [SRC-829A979985-L000290](../../tests/test_generation_acceptance_matrix.py#L290) | 290 | `"                \"providers_used\": [\"duckduckgo_html\", \"bing_rss\"],"` | — |
| [SRC-829A979985-L000291](../../tests/test_generation_acceptance_matrix.py#L291) | 291 | `"                \"provider_counts\": {\"duckduckgo_html\": 1, \"bing_rss\": 1},"` | — |
| [SRC-829A979985-L000292](../../tests/test_generation_acceptance_matrix.py#L292) | 292 | `"                \"platform_counts\": {\"web\": 2},"` | — |
| [SRC-829A979985-L000293](../../tests/test_generation_acceptance_matrix.py#L293) | 293 | `"                \"social_direct_results\": 0,"` | — |
| [SRC-829A979985-L000294](../../tests/test_generation_acceptance_matrix.py#L294) | 294 | `"                \"provider_diagnostics\": [],"` | — |
| [SRC-829A979985-L000295](../../tests/test_generation_acceptance_matrix.py#L295) | 295 | `"                \"evidence_signals\": {},"` | — |
| [SRC-829A979985-L000296](../../tests/test_generation_acceptance_matrix.py#L296) | 296 | `"            },"` | — |
| [SRC-829A979985-L000297](../../tests/test_generation_acceptance_matrix.py#L297) | 297 | `"        ),"` | — |
| [SRC-829A979985-L000298](../../tests/test_generation_acceptance_matrix.py#L298) | 298 | `"    )"` | — |
| [SRC-829A979985-L000299](../../tests/test_generation_acceptance_matrix.py#L299) | 299 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, item: True)"` | — |
| [SRC-829A979985-L000300](../../tests/test_generation_acceptance_matrix.py#L300) | 300 | `"    calls: list[str] = []"` | — |
| [SRC-829A979985-L000301](../../tests/test_generation_acceptance_matrix.py#L301) | 301 | `""` | — |
| [SRC-829A979985-L000302](../../tests/test_generation_acceptance_matrix.py#L302) | 302 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-829A979985-L000303](../../tests/test_generation_acceptance_matrix.py#L303) | 303 | `"        model = json.loads(request.data.decode(\"utf-8\"))[\"model\"]"` | — |
| [SRC-829A979985-L000304](../../tests/test_generation_acceptance_matrix.py#L304) | 304 | `"        calls.append(model)"` | — |
| [SRC-829A979985-L000305](../../tests/test_generation_acceptance_matrix.py#L305) | 305 | `"        return FakeCompletionResponse(\"إجابة مبتورة لا يجوز عرضها\", \"length\")"` | — |
| [SRC-829A979985-L000306](../../tests/test_generation_acceptance_matrix.py#L306) | 306 | `""` | — |
| [SRC-829A979985-L000307](../../tests/test_generation_acceptance_matrix.py#L307) | 307 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-829A979985-L000308](../../tests/test_generation_acceptance_matrix.py#L308) | 308 | `""` | — |
| [SRC-829A979985-L000309](../../tests/test_generation_acceptance_matrix.py#L309) | 309 | `"    result = agent.answer(question)"` | — |
| [SRC-829A979985-L000310](../../tests/test_generation_acceptance_matrix.py#L310) | 310 | `""` | — |
| [SRC-829A979985-L000311](../../tests/test_generation_acceptance_matrix.py#L311) | 311 | `"    assert len(calls) == 1"` | — |
| [SRC-829A979985-L000312](../../tests/test_generation_acceptance_matrix.py#L312) | 312 | `"    assert result[\"request_budget\"][\"counts\"][\"model_calls\"] == 1"` | — |
| [SRC-829A979985-L000313](../../tests/test_generation_acceptance_matrix.py#L313) | 313 | `"    assert \"model_calls\" in result[\"request_budget\"][\"exhausted_reasons\"]"` | — |
| [SRC-829A979985-L000314](../../tests/test_generation_acceptance_matrix.py#L314) | 314 | `"    assert result[\"final_answer_status\"] == \"budget_exhausted_with_source_fallback\""` | — |
| [SRC-829A979985-L000315](../../tests/test_generation_acceptance_matrix.py#L315) | 315 | `"    assert result[\"used_language_model\"] is False"` | — |
| [SRC-829A979985-L000316](../../tests/test_generation_acceptance_matrix.py#L316) | 316 | `"    assert result[\"search_attempted\"] is True"` | — |
| [SRC-829A979985-L000317](../../tests/test_generation_acceptance_matrix.py#L317) | 317 | `"    assert len(result[\"sources\"]) == 2"` | — |
| [SRC-829A979985-L000318](../../tests/test_generation_acceptance_matrix.py#L318) | 318 | `"    assert \"إجابة مبتورة لا يجوز عرضها\" not in result[\"answer\"]"` | — |
| [SRC-829A979985-L000319](../../tests/test_generation_acceptance_matrix.py#L319) | 319 | `"    assert \"مقتطف المصدر الثاني عن الطاقة المتجددة\" in result[\"answer\"]"` | — |
| [SRC-829A979985-L000320](../../tests/test_generation_acceptance_matrix.py#L320) | 320 | `"    assert result[\"generation_diagnostics\"][0][\"status\"] == \"truncated\""` | — |
| [SRC-829A979985-L000321](../../tests/test_generation_acceptance_matrix.py#L321) | 321 | `""` | — |
| [SRC-829A979985-L000322](../../tests/test_generation_acceptance_matrix.py#L322) | 322 | `""` | — |
| [SRC-829A979985-L000323](../../tests/test_generation_acceptance_matrix.py#L323) | 323 | `"def test_review_budget_exhaustion_discards_draft_and_preserves_sources(monkeypatch):"` | — |
| [SRC-829A979985-L000324](../../tests/test_generation_acceptance_matrix.py#L324) | 324 | `"    agent = WebAgent()"` | — |
| [SRC-829A979985-L000325](../../tests/test_generation_acceptance_matrix.py#L325) | 325 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-829A979985-L000326](../../tests/test_generation_acceptance_matrix.py#L326) | 326 | `"    question = \"قارن بين الخيارات من حيث السعر، المساحة، والبيانات الناقصة\""` | — |
| [SRC-829A979985-L000327](../../tests/test_generation_acceptance_matrix.py#L327) | 327 | `"    monkeypatch.setenv(\"OMARAI_REQUEST_MAX_MODEL_CALLS\", \"1\")"` | — |
| [SRC-829A979985-L000328](../../tests/test_generation_acceptance_matrix.py#L328) | 328 | `"    sources = ["` | — |
| [SRC-829A979985-L000329](../../tests/test_generation_acceptance_matrix.py#L329) | 329 | `"        source("` | — |
| [SRC-829A979985-L000330](../../tests/test_generation_acceptance_matrix.py#L330) | 330 | `"            \"https://one.example/product\","` | — |
| [SRC-829A979985-L000331](../../tests/test_generation_acceptance_matrix.py#L331) | 331 | `"            \"one.example\","` | — |
| [SRC-829A979985-L000332](../../tests/test_generation_acceptance_matrix.py#L332) | 332 | `"            page_fetched=True,"` | — |
| [SRC-829A979985-L000333](../../tests/test_generation_acceptance_matrix.py#L333) | 333 | `"            page_text=\"السعر الإجمالي 100000 جنيه والمساحة 100 متر.\","` | — |
| [SRC-829A979985-L000334](../../tests/test_generation_acceptance_matrix.py#L334) | 334 | `"            provider=\"duckduckgo_html\","` | — |
| [SRC-829A979985-L000335](../../tests/test_generation_acceptance_matrix.py#L335) | 335 | `"        ),"` | — |
| [SRC-829A979985-L000336](../../tests/test_generation_acceptance_matrix.py#L336) | 336 | `"        source("` | — |
| [SRC-829A979985-L000337](../../tests/test_generation_acceptance_matrix.py#L337) | 337 | `"            \"https://two.example/product\","` | — |
| [SRC-829A979985-L000338](../../tests/test_generation_acceptance_matrix.py#L338) | 338 | `"            \"two.example\","` | — |
| [SRC-829A979985-L000339](../../tests/test_generation_acceptance_matrix.py#L339) | 339 | `"            page_fetched=False,"` | — |
| [SRC-829A979985-L000340](../../tests/test_generation_acceptance_matrix.py#L340) | 340 | `"            snippet=\"إعلان يذكر سعرًا دون بيان المساحة.\","` | — |
| [SRC-829A979985-L000341](../../tests/test_generation_acceptance_matrix.py#L341) | 341 | `"            provider=\"bing_rss\","` | — |
| [SRC-829A979985-L000342](../../tests/test_generation_acceptance_matrix.py#L342) | 342 | `"        ),"` | — |
| [SRC-829A979985-L000343](../../tests/test_generation_acceptance_matrix.py#L343) | 343 | `"    ]"` | — |
| [SRC-829A979985-L000344](../../tests/test_generation_acceptance_matrix.py#L344) | 344 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000345](../../tests/test_generation_acceptance_matrix.py#L345) | 345 | `"        agent,"` | — |
| [SRC-829A979985-L000346](../../tests/test_generation_acceptance_matrix.py#L346) | 346 | `"        \"_plan_search\","` | — |
| [SRC-829A979985-L000347](../../tests/test_generation_acceptance_matrix.py#L347) | 347 | `"        lambda question, history: {"` | — |
| [SRC-829A979985-L000348](../../tests/test_generation_acceptance_matrix.py#L348) | 348 | `"            \"queries\": [question],"` | — |
| [SRC-829A979985-L000349](../../tests/test_generation_acceptance_matrix.py#L349) | 349 | `"            \"direct_urls\": [],"` | — |
| [SRC-829A979985-L000350](../../tests/test_generation_acceptance_matrix.py#L350) | 350 | `"            \"social_focus\": False,"` | — |
| [SRC-829A979985-L000351](../../tests/test_generation_acceptance_matrix.py#L351) | 351 | `"            \"freshness\": \"any\","` | — |
| [SRC-829A979985-L000352](../../tests/test_generation_acceptance_matrix.py#L352) | 352 | `"            \"depth\": \"deep\","` | — |
| [SRC-829A979985-L000353](../../tests/test_generation_acceptance_matrix.py#L353) | 353 | `"            \"platforms\": [],"` | — |
| [SRC-829A979985-L000354](../../tests/test_generation_acceptance_matrix.py#L354) | 354 | `"            \"planning_method\": \"test\","` | — |
| [SRC-829A979985-L000355](../../tests/test_generation_acceptance_matrix.py#L355) | 355 | `"        },"` | — |
| [SRC-829A979985-L000356](../../tests/test_generation_acceptance_matrix.py#L356) | 356 | `"    )"` | — |
| [SRC-829A979985-L000357](../../tests/test_generation_acceptance_matrix.py#L357) | 357 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000358](../../tests/test_generation_acceptance_matrix.py#L358) | 358 | `"        agent,"` | — |
| [SRC-829A979985-L000359](../../tests/test_generation_acceptance_matrix.py#L359) | 359 | `"        \"_collect_research\","` | — |
| [SRC-829A979985-L000360](../../tests/test_generation_acceptance_matrix.py#L360) | 360 | `"        lambda plan: ("` | — |
| [SRC-829A979985-L000361](../../tests/test_generation_acceptance_matrix.py#L361) | 361 | `"            sources,"` | — |
| [SRC-829A979985-L000362](../../tests/test_generation_acceptance_matrix.py#L362) | 362 | `"            [],"` | — |
| [SRC-829A979985-L000363](../../tests/test_generation_acceptance_matrix.py#L363) | 363 | `"            {"` | — |
| [SRC-829A979985-L000364](../../tests/test_generation_acceptance_matrix.py#L364) | 364 | `"                \"queries_planned\": 1,"` | — |
| [SRC-829A979985-L000365](../../tests/test_generation_acceptance_matrix.py#L365) | 365 | `"                \"queries_attempted\": 1,"` | — |
| [SRC-829A979985-L000366](../../tests/test_generation_acceptance_matrix.py#L366) | 366 | `"                \"search_attempted\": True,"` | — |
| [SRC-829A979985-L000367](../../tests/test_generation_acceptance_matrix.py#L367) | 367 | `"                \"search_outcome\": \"attempted_with_usable_sources\","` | — |
| [SRC-829A979985-L000368](../../tests/test_generation_acceptance_matrix.py#L368) | 368 | `"                \"unique_sources\": 2,"` | — |
| [SRC-829A979985-L000369](../../tests/test_generation_acceptance_matrix.py#L369) | 369 | `"                \"pages_fetched\": 1,"` | — |
| [SRC-829A979985-L000370](../../tests/test_generation_acceptance_matrix.py#L370) | 370 | `"                \"providers_used\": [\"duckduckgo_html\", \"bing_rss\"],"` | — |
| [SRC-829A979985-L000371](../../tests/test_generation_acceptance_matrix.py#L371) | 371 | `"                \"provider_counts\": {\"duckduckgo_html\": 1, \"bing_rss\": 1},"` | — |
| [SRC-829A979985-L000372](../../tests/test_generation_acceptance_matrix.py#L372) | 372 | `"                \"platform_counts\": {\"web\": 2},"` | — |
| [SRC-829A979985-L000373](../../tests/test_generation_acceptance_matrix.py#L373) | 373 | `"                \"social_direct_results\": 0,"` | — |
| [SRC-829A979985-L000374](../../tests/test_generation_acceptance_matrix.py#L374) | 374 | `"                \"provider_diagnostics\": [],"` | — |
| [SRC-829A979985-L000375](../../tests/test_generation_acceptance_matrix.py#L375) | 375 | `"                \"evidence_signals\": {},"` | — |
| [SRC-829A979985-L000376](../../tests/test_generation_acceptance_matrix.py#L376) | 376 | `"            },"` | — |
| [SRC-829A979985-L000377](../../tests/test_generation_acceptance_matrix.py#L377) | 377 | `"        ),"` | — |
| [SRC-829A979985-L000378](../../tests/test_generation_acceptance_matrix.py#L378) | 378 | `"    )"` | — |
| [SRC-829A979985-L000379](../../tests/test_generation_acceptance_matrix.py#L379) | 379 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, item: True)"` | — |
| [SRC-829A979985-L000380](../../tests/test_generation_acceptance_matrix.py#L380) | 380 | `"    calls: list[str] = []"` | — |
| [SRC-829A979985-L000381](../../tests/test_generation_acceptance_matrix.py#L381) | 381 | `""` | — |
| [SRC-829A979985-L000382](../../tests/test_generation_acceptance_matrix.py#L382) | 382 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-829A979985-L000383](../../tests/test_generation_acceptance_matrix.py#L383) | 383 | `"        calls.append(json.loads(request.data.decode(\"utf-8\"))[\"model\"])"` | — |
| [SRC-829A979985-L000384](../../tests/test_generation_acceptance_matrix.py#L384) | 384 | `"        return FakeCompletionResponse("` | — |
| [SRC-829A979985-L000385](../../tests/test_generation_acceptance_matrix.py#L385) | 385 | `"            \"مسودة تحليل مولدة لكنها لم تخضع للتدقيق النهائي [المصدر 1].\","` | — |
| [SRC-829A979985-L000386](../../tests/test_generation_acceptance_matrix.py#L386) | 386 | `"            \"stop\","` | — |
| [SRC-829A979985-L000387](../../tests/test_generation_acceptance_matrix.py#L387) | 387 | `"        )"` | — |
| [SRC-829A979985-L000388](../../tests/test_generation_acceptance_matrix.py#L388) | 388 | `""` | — |
| [SRC-829A979985-L000389](../../tests/test_generation_acceptance_matrix.py#L389) | 389 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-829A979985-L000390](../../tests/test_generation_acceptance_matrix.py#L390) | 390 | `""` | — |
| [SRC-829A979985-L000391](../../tests/test_generation_acceptance_matrix.py#L391) | 391 | `"    result = agent.answer(question)"` | — |
| [SRC-829A979985-L000392](../../tests/test_generation_acceptance_matrix.py#L392) | 392 | `""` | — |
| [SRC-829A979985-L000393](../../tests/test_generation_acceptance_matrix.py#L393) | 393 | `"    assert len(calls) == 1"` | — |
| [SRC-829A979985-L000394](../../tests/test_generation_acceptance_matrix.py#L394) | 394 | `"    assert result[\"request_budget\"][\"counts\"][\"model_calls\"] == 1"` | — |
| [SRC-829A979985-L000395](../../tests/test_generation_acceptance_matrix.py#L395) | 395 | `"    assert \"model_calls\" in result[\"request_budget\"][\"exhausted_reasons\"]"` | — |
| [SRC-829A979985-L000396](../../tests/test_generation_acceptance_matrix.py#L396) | 396 | `"    assert result[\"final_answer_status\"] == \"budget_exhausted_with_source_fallback\""` | — |
| [SRC-829A979985-L000397](../../tests/test_generation_acceptance_matrix.py#L397) | 397 | `"    assert result[\"search_report\"][\"second_pass_review\"] == \"model_claim_audit_unavailable\""` | — |
| [SRC-829A979985-L000398](../../tests/test_generation_acceptance_matrix.py#L398) | 398 | `"    assert len(result[\"sources\"]) == 2"` | — |
| [SRC-829A979985-L000399](../../tests/test_generation_acceptance_matrix.py#L399) | 399 | `"    assert \"مسودة تحليل مولدة لكنها لم تخضع للتدقيق النهائي\" not in result[\"answer\"]"` | — |
| [SRC-829A979985-L000400](../../tests/test_generation_acceptance_matrix.py#L400) | 400 | `"    assert \"السعر الإجمالي 100000 جنيه والمساحة 100 متر.\" in result[\"answer\"]"` | — |
| [SRC-829A979985-L000401](../../tests/test_generation_acceptance_matrix.py#L401) | 401 | `""` | — |
| [SRC-829A979985-L000402](../../tests/test_generation_acceptance_matrix.py#L402) | 402 | `""` | — |
| [SRC-829A979985-L000403](../../tests/test_generation_acceptance_matrix.py#L403) | 403 | `"def test_search_failure_is_not_reported_as_no_attempt_or_completed_answer(monkeypatch):"` | — |
| [SRC-829A979985-L000404](../../tests/test_generation_acceptance_matrix.py#L404) | 404 | `"    agent = WebAgent()"` | — |
| [SRC-829A979985-L000405](../../tests/test_generation_acceptance_matrix.py#L405) | 405 | `"    question = \"ابحث عن أحدث معلومات حول الطاقة المتجددة\""` | — |
| [SRC-829A979985-L000406](../../tests/test_generation_acceptance_matrix.py#L406) | 406 | `""` | — |
| [SRC-829A979985-L000407](../../tests/test_generation_acceptance_matrix.py#L407) | 407 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000408](../../tests/test_generation_acceptance_matrix.py#L408) | 408 | `"        agent,"` | — |
| [SRC-829A979985-L000409](../../tests/test_generation_acceptance_matrix.py#L409) | 409 | `"        \"_plan_search\","` | — |
| [SRC-829A979985-L000410](../../tests/test_generation_acceptance_matrix.py#L410) | 410 | `"        lambda question, history: {"` | — |
| [SRC-829A979985-L000411](../../tests/test_generation_acceptance_matrix.py#L411) | 411 | `"            \"queries\": [question],"` | — |
| [SRC-829A979985-L000412](../../tests/test_generation_acceptance_matrix.py#L412) | 412 | `"            \"direct_urls\": [],"` | — |
| [SRC-829A979985-L000413](../../tests/test_generation_acceptance_matrix.py#L413) | 413 | `"            \"social_focus\": False,"` | — |
| [SRC-829A979985-L000414](../../tests/test_generation_acceptance_matrix.py#L414) | 414 | `"            \"freshness\": \"current\","` | — |
| [SRC-829A979985-L000415](../../tests/test_generation_acceptance_matrix.py#L415) | 415 | `"            \"depth\": \"standard\","` | — |
| [SRC-829A979985-L000416](../../tests/test_generation_acceptance_matrix.py#L416) | 416 | `"            \"platforms\": [],"` | — |
| [SRC-829A979985-L000417](../../tests/test_generation_acceptance_matrix.py#L417) | 417 | `"            \"planning_method\": \"test\","` | — |
| [SRC-829A979985-L000418](../../tests/test_generation_acceptance_matrix.py#L418) | 418 | `"        },"` | — |
| [SRC-829A979985-L000419](../../tests/test_generation_acceptance_matrix.py#L419) | 419 | `"    )"` | — |
| [SRC-829A979985-L000420](../../tests/test_generation_acceptance_matrix.py#L420) | 420 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000421](../../tests/test_generation_acceptance_matrix.py#L421) | 421 | `"        agent,"` | — |
| [SRC-829A979985-L000422](../../tests/test_generation_acceptance_matrix.py#L422) | 422 | `"        \"_collect_research\","` | — |
| [SRC-829A979985-L000423](../../tests/test_generation_acceptance_matrix.py#L423) | 423 | `"        lambda plan: ("` | — |
| [SRC-829A979985-L000424](../../tests/test_generation_acceptance_matrix.py#L424) | 424 | `"            [],"` | — |
| [SRC-829A979985-L000425](../../tests/test_generation_acceptance_matrix.py#L425) | 425 | `"            [\"تعذر الاتصال بموصلات البحث\"],"` | — |
| [SRC-829A979985-L000426](../../tests/test_generation_acceptance_matrix.py#L426) | 426 | `"            {"` | — |
| [SRC-829A979985-L000427](../../tests/test_generation_acceptance_matrix.py#L427) | 427 | `"                \"queries_planned\": 1,"` | — |
| [SRC-829A979985-L000428](../../tests/test_generation_acceptance_matrix.py#L428) | 428 | `"                \"queries_attempted\": 1,"` | — |
| [SRC-829A979985-L000429](../../tests/test_generation_acceptance_matrix.py#L429) | 429 | `"                \"search_attempted\": True,"` | — |
| [SRC-829A979985-L000430](../../tests/test_generation_acceptance_matrix.py#L430) | 430 | `"                \"search_outcome\": \"attempted_no_usable_sources\","` | — |
| [SRC-829A979985-L000431](../../tests/test_generation_acceptance_matrix.py#L431) | 431 | `"                \"unique_sources\": 0,"` | — |
| [SRC-829A979985-L000432](../../tests/test_generation_acceptance_matrix.py#L432) | 432 | `"                \"pages_fetched\": 0,"` | — |
| [SRC-829A979985-L000433](../../tests/test_generation_acceptance_matrix.py#L433) | 433 | `"                \"providers_used\": [],"` | — |
| [SRC-829A979985-L000434](../../tests/test_generation_acceptance_matrix.py#L434) | 434 | `"                \"provider_diagnostics\": ["` | — |
| [SRC-829A979985-L000435](../../tests/test_generation_acceptance_matrix.py#L435) | 435 | `"                    {\"provider\": \"duckduckgo_html\", \"status\": \"failed\"},"` | — |
| [SRC-829A979985-L000436](../../tests/test_generation_acceptance_matrix.py#L436) | 436 | `"                    {\"provider\": \"bing_rss\", \"status\": \"timeout\"},"` | — |
| [SRC-829A979985-L000437](../../tests/test_generation_acceptance_matrix.py#L437) | 437 | `"                ],"` | — |
| [SRC-829A979985-L000438](../../tests/test_generation_acceptance_matrix.py#L438) | 438 | `"                \"evidence_signals\": {},"` | — |
| [SRC-829A979985-L000439](../../tests/test_generation_acceptance_matrix.py#L439) | 439 | `"            },"` | — |
| [SRC-829A979985-L000440](../../tests/test_generation_acceptance_matrix.py#L440) | 440 | `"        ),"` | — |
| [SRC-829A979985-L000441](../../tests/test_generation_acceptance_matrix.py#L441) | 441 | `"    )"` | — |
| [SRC-829A979985-L000442](../../tests/test_generation_acceptance_matrix.py#L442) | 442 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000443](../../tests/test_generation_acceptance_matrix.py#L443) | 443 | `"        agent,"` | — |
| [SRC-829A979985-L000444](../../tests/test_generation_acceptance_matrix.py#L444) | 444 | `"        \"_generate\","` | — |
| [SRC-829A979985-L000445](../../tests/test_generation_acceptance_matrix.py#L445) | 445 | `"        lambda *args, **kwargs: pytest.fail(\"No final synthesis without usable sources\"),"` | — |
| [SRC-829A979985-L000446](../../tests/test_generation_acceptance_matrix.py#L446) | 446 | `"    )"` | — |
| [SRC-829A979985-L000447](../../tests/test_generation_acceptance_matrix.py#L447) | 447 | `""` | — |
| [SRC-829A979985-L000448](../../tests/test_generation_acceptance_matrix.py#L448) | 448 | `"    result = agent.answer(question)"` | — |
| [SRC-829A979985-L000449](../../tests/test_generation_acceptance_matrix.py#L449) | 449 | `""` | — |
| [SRC-829A979985-L000450](../../tests/test_generation_acceptance_matrix.py#L450) | 450 | `"    assert result[\"search_attempted\"] is True"` | — |
| [SRC-829A979985-L000451](../../tests/test_generation_acceptance_matrix.py#L451) | 451 | `"    assert result[\"used_web_search\"] is False"` | — |
| [SRC-829A979985-L000452](../../tests/test_generation_acceptance_matrix.py#L452) | 452 | `"    assert result[\"search_report\"][\"search_outcome\"] == \"attempted_no_usable_sources\""` | — |
| [SRC-829A979985-L000453](../../tests/test_generation_acceptance_matrix.py#L453) | 453 | `"    assert result[\"final_answer_status\"] == \"insufficient_evidence_no_generation\""` | — |
| [SRC-829A979985-L000454](../../tests/test_generation_acceptance_matrix.py#L454) | 454 | `"    assert result[\"used_language_model\"] is False"` | — |
| [SRC-829A979985-L000455](../../tests/test_generation_acceptance_matrix.py#L455) | 455 | `"    assert result[\"research_quality\"] == \"failed\""` | — |
| [SRC-829A979985-L000456](../../tests/test_generation_acceptance_matrix.py#L456) | 456 | `"    assert result[\"answer_integrity\"][\"method\"] == \"deterministic_lexical_screen_only\""` | — |
| [SRC-829A979985-L000457](../../tests/test_generation_acceptance_matrix.py#L457) | 457 | `"    assert result[\"answer_integrity\"][\"independent_fact_check\"] is False"` | — |
| [SRC-829A979985-L000458](../../tests/test_generation_acceptance_matrix.py#L458) | 458 | `"    assert result[\"search_report\"][\"answer_integrity\"] == result[\"answer_integrity\"]"` | — |
| [SRC-829A979985-L000459](../../tests/test_generation_acceptance_matrix.py#L459) | 459 | `""` | — |
| [SRC-829A979985-L000460](../../tests/test_generation_acceptance_matrix.py#L460) | 460 | `""` | — |
| [SRC-829A979985-L000461](../../tests/test_generation_acceptance_matrix.py#L461) | 461 | `"def test_research_exception_does_not_claim_no_results_or_no_search(monkeypatch):"` | — |
| [SRC-829A979985-L000462](../../tests/test_generation_acceptance_matrix.py#L462) | 462 | `"    agent = WebAgent()"` | — |
| [SRC-829A979985-L000463](../../tests/test_generation_acceptance_matrix.py#L463) | 463 | `"    question = \"ابحث عن أحدث معلومات حول الطاقة المتجددة\""` | — |
| [SRC-829A979985-L000464](../../tests/test_generation_acceptance_matrix.py#L464) | 464 | `""` | — |
| [SRC-829A979985-L000465](../../tests/test_generation_acceptance_matrix.py#L465) | 465 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000466](../../tests/test_generation_acceptance_matrix.py#L466) | 466 | `"        agent,"` | — |
| [SRC-829A979985-L000467](../../tests/test_generation_acceptance_matrix.py#L467) | 467 | `"        \"_plan_search\","` | — |
| [SRC-829A979985-L000468](../../tests/test_generation_acceptance_matrix.py#L468) | 468 | `"        lambda question, history: {"` | — |
| [SRC-829A979985-L000469](../../tests/test_generation_acceptance_matrix.py#L469) | 469 | `"            \"queries\": [question],"` | — |
| [SRC-829A979985-L000470](../../tests/test_generation_acceptance_matrix.py#L470) | 470 | `"            \"direct_urls\": [],"` | — |
| [SRC-829A979985-L000471](../../tests/test_generation_acceptance_matrix.py#L471) | 471 | `"            \"social_focus\": False,"` | — |
| [SRC-829A979985-L000472](../../tests/test_generation_acceptance_matrix.py#L472) | 472 | `"            \"freshness\": \"current\","` | — |
| [SRC-829A979985-L000473](../../tests/test_generation_acceptance_matrix.py#L473) | 473 | `"            \"depth\": \"standard\","` | — |
| [SRC-829A979985-L000474](../../tests/test_generation_acceptance_matrix.py#L474) | 474 | `"            \"platforms\": [],"` | — |
| [SRC-829A979985-L000475](../../tests/test_generation_acceptance_matrix.py#L475) | 475 | `"            \"planning_method\": \"test\","` | — |
| [SRC-829A979985-L000476](../../tests/test_generation_acceptance_matrix.py#L476) | 476 | `"        },"` | — |
| [SRC-829A979985-L000477](../../tests/test_generation_acceptance_matrix.py#L477) | 477 | `"    )"` | — |
| [SRC-829A979985-L000478](../../tests/test_generation_acceptance_matrix.py#L478) | 478 | `""` | — |
| [SRC-829A979985-L000479](../../tests/test_generation_acceptance_matrix.py#L479) | 479 | `"    def collect_fails_before_diagnostics(plan):"` | — |
| [SRC-829A979985-L000480](../../tests/test_generation_acceptance_matrix.py#L480) | 480 | `"        raise RuntimeError(\"collector failed before the attempt status was known\")"` | — |
| [SRC-829A979985-L000481](../../tests/test_generation_acceptance_matrix.py#L481) | 481 | `""` | — |
| [SRC-829A979985-L000482](../../tests/test_generation_acceptance_matrix.py#L482) | 482 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect_fails_before_diagnostics)"` | — |
| [SRC-829A979985-L000483](../../tests/test_generation_acceptance_matrix.py#L483) | 483 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000484](../../tests/test_generation_acceptance_matrix.py#L484) | 484 | `"        agent,"` | — |
| [SRC-829A979985-L000485](../../tests/test_generation_acceptance_matrix.py#L485) | 485 | `"        \"_generate\","` | — |
| [SRC-829A979985-L000486](../../tests/test_generation_acceptance_matrix.py#L486) | 486 | `"        lambda *args, **kwargs: pytest.fail(\"No synthesis when the research state is unknown\"),"` | — |
| [SRC-829A979985-L000487](../../tests/test_generation_acceptance_matrix.py#L487) | 487 | `"    )"` | — |
| [SRC-829A979985-L000488](../../tests/test_generation_acceptance_matrix.py#L488) | 488 | `""` | — |
| [SRC-829A979985-L000489](../../tests/test_generation_acceptance_matrix.py#L489) | 489 | `"    result = agent.answer(question)"` | — |
| [SRC-829A979985-L000490](../../tests/test_generation_acceptance_matrix.py#L490) | 490 | `""` | — |
| [SRC-829A979985-L000491](../../tests/test_generation_acceptance_matrix.py#L491) | 491 | `"    assert result[\"search_report\"][\"search_outcome\"] == \"unknown_after_research_error\""` | — |
| [SRC-829A979985-L000492](../../tests/test_generation_acceptance_matrix.py#L492) | 492 | `"    assert result[\"search_report\"][\"unique_sources\"] is None"` | — |
| [SRC-829A979985-L000493](../../tests/test_generation_acceptance_matrix.py#L493) | 493 | `"    assert result[\"search_report\"][\"pages_fetched\"] is None"` | — |
| [SRC-829A979985-L000494](../../tests/test_generation_acceptance_matrix.py#L494) | 494 | `"    assert result[\"search_attempted\"] is None"` | — |
| [SRC-829A979985-L000495](../../tests/test_generation_acceptance_matrix.py#L495) | 495 | `"    assert result[\"final_answer_status\"] == \"insufficient_evidence_no_generation\""` | — |
| [SRC-829A979985-L000496](../../tests/test_generation_acceptance_matrix.py#L496) | 496 | `"    assert \"لا أستطيع الجزم\" in result[\"answer\"]"` | — |
| [SRC-829A979985-L000497](../../tests/test_generation_acceptance_matrix.py#L497) | 497 | `"    assert \"لم أجد معلومات موثوقة كافية\" not in result[\"answer\"]"` | — |
| [SRC-829A979985-L000498](../../tests/test_generation_acceptance_matrix.py#L498) | 498 | `""` | — |
| [SRC-829A979985-L000499](../../tests/test_generation_acceptance_matrix.py#L499) | 499 | `""` | — |
| [SRC-829A979985-L000500](../../tests/test_generation_acceptance_matrix.py#L500) | 500 | `"def test_search_extraction_generation_and_task_review_remain_distinct(monkeypatch):"` | — |
| [SRC-829A979985-L000501](../../tests/test_generation_acceptance_matrix.py#L501) | 501 | `"    agent = WebAgent()"` | — |
| [SRC-829A979985-L000502](../../tests/test_generation_acceptance_matrix.py#L502) | 502 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-829A979985-L000503](../../tests/test_generation_acceptance_matrix.py#L503) | 503 | `"    question = \"قارن بين الخيارات من حيث السعر، المساحة، والبيانات الناقصة\""` | — |
| [SRC-829A979985-L000504](../../tests/test_generation_acceptance_matrix.py#L504) | 504 | `"    sources = ["` | — |
| [SRC-829A979985-L000505](../../tests/test_generation_acceptance_matrix.py#L505) | 505 | `"        source("` | — |
| [SRC-829A979985-L000506](../../tests/test_generation_acceptance_matrix.py#L506) | 506 | `"            \"https://one.example/product\","` | — |
| [SRC-829A979985-L000507](../../tests/test_generation_acceptance_matrix.py#L507) | 507 | `"            \"one.example\","` | — |
| [SRC-829A979985-L000508](../../tests/test_generation_acceptance_matrix.py#L508) | 508 | `"            page_fetched=True,"` | — |
| [SRC-829A979985-L000509](../../tests/test_generation_acceptance_matrix.py#L509) | 509 | `"            page_text=\"السعر الإجمالي 100000 جنيه والمساحة 100 متر.\","` | — |
| [SRC-829A979985-L000510](../../tests/test_generation_acceptance_matrix.py#L510) | 510 | `"            provider=\"duckduckgo_html\","` | — |
| [SRC-829A979985-L000511](../../tests/test_generation_acceptance_matrix.py#L511) | 511 | `"        ),"` | — |
| [SRC-829A979985-L000512](../../tests/test_generation_acceptance_matrix.py#L512) | 512 | `"        source("` | — |
| [SRC-829A979985-L000513](../../tests/test_generation_acceptance_matrix.py#L513) | 513 | `"            \"https://two.example/product\","` | — |
| [SRC-829A979985-L000514](../../tests/test_generation_acceptance_matrix.py#L514) | 514 | `"            \"two.example\","` | — |
| [SRC-829A979985-L000515](../../tests/test_generation_acceptance_matrix.py#L515) | 515 | `"            page_fetched=False,"` | — |
| [SRC-829A979985-L000516](../../tests/test_generation_acceptance_matrix.py#L516) | 516 | `"            snippet=\"إعلان يذكر سعرًا دون بيان المساحة.\","` | — |
| [SRC-829A979985-L000517](../../tests/test_generation_acceptance_matrix.py#L517) | 517 | `"            provider=\"bing_rss\","` | — |
| [SRC-829A979985-L000518](../../tests/test_generation_acceptance_matrix.py#L518) | 518 | `"        ),"` | — |
| [SRC-829A979985-L000519](../../tests/test_generation_acceptance_matrix.py#L519) | 519 | `"    ]"` | — |
| [SRC-829A979985-L000520](../../tests/test_generation_acceptance_matrix.py#L520) | 520 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000521](../../tests/test_generation_acceptance_matrix.py#L521) | 521 | `"        agent,"` | — |
| [SRC-829A979985-L000522](../../tests/test_generation_acceptance_matrix.py#L522) | 522 | `"        \"_plan_search\","` | — |
| [SRC-829A979985-L000523](../../tests/test_generation_acceptance_matrix.py#L523) | 523 | `"        lambda question, history: {"` | — |
| [SRC-829A979985-L000524](../../tests/test_generation_acceptance_matrix.py#L524) | 524 | `"            \"queries\": [question],"` | — |
| [SRC-829A979985-L000525](../../tests/test_generation_acceptance_matrix.py#L525) | 525 | `"            \"direct_urls\": [],"` | — |
| [SRC-829A979985-L000526](../../tests/test_generation_acceptance_matrix.py#L526) | 526 | `"            \"social_focus\": False,"` | — |
| [SRC-829A979985-L000527](../../tests/test_generation_acceptance_matrix.py#L527) | 527 | `"            \"freshness\": \"any\","` | — |
| [SRC-829A979985-L000528](../../tests/test_generation_acceptance_matrix.py#L528) | 528 | `"            \"depth\": \"deep\","` | — |
| [SRC-829A979985-L000529](../../tests/test_generation_acceptance_matrix.py#L529) | 529 | `"            \"platforms\": [],"` | — |
| [SRC-829A979985-L000530](../../tests/test_generation_acceptance_matrix.py#L530) | 530 | `"            \"planning_method\": \"test\","` | — |
| [SRC-829A979985-L000531](../../tests/test_generation_acceptance_matrix.py#L531) | 531 | `"        },"` | — |
| [SRC-829A979985-L000532](../../tests/test_generation_acceptance_matrix.py#L532) | 532 | `"    )"` | — |
| [SRC-829A979985-L000533](../../tests/test_generation_acceptance_matrix.py#L533) | 533 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000534](../../tests/test_generation_acceptance_matrix.py#L534) | 534 | `"        agent,"` | — |
| [SRC-829A979985-L000535](../../tests/test_generation_acceptance_matrix.py#L535) | 535 | `"        \"_collect_research\","` | — |
| [SRC-829A979985-L000536](../../tests/test_generation_acceptance_matrix.py#L536) | 536 | `"        lambda plan: ("` | — |
| [SRC-829A979985-L000537](../../tests/test_generation_acceptance_matrix.py#L537) | 537 | `"            sources,"` | — |
| [SRC-829A979985-L000538](../../tests/test_generation_acceptance_matrix.py#L538) | 538 | `"            [],"` | — |
| [SRC-829A979985-L000539](../../tests/test_generation_acceptance_matrix.py#L539) | 539 | `"            {"` | — |
| [SRC-829A979985-L000540](../../tests/test_generation_acceptance_matrix.py#L540) | 540 | `"                \"queries_planned\": 1,"` | — |
| [SRC-829A979985-L000541](../../tests/test_generation_acceptance_matrix.py#L541) | 541 | `"                \"queries_attempted\": 1,"` | — |
| [SRC-829A979985-L000542](../../tests/test_generation_acceptance_matrix.py#L542) | 542 | `"                \"search_attempted\": True,"` | — |
| [SRC-829A979985-L000543](../../tests/test_generation_acceptance_matrix.py#L543) | 543 | `"                \"search_outcome\": \"attempted_with_usable_sources\","` | — |
| [SRC-829A979985-L000544](../../tests/test_generation_acceptance_matrix.py#L544) | 544 | `"                \"unique_sources\": 2,"` | — |
| [SRC-829A979985-L000545](../../tests/test_generation_acceptance_matrix.py#L545) | 545 | `"                \"pages_fetched\": 1,"` | — |
| [SRC-829A979985-L000546](../../tests/test_generation_acceptance_matrix.py#L546) | 546 | `"                \"providers_used\": [\"duckduckgo_html\", \"bing_rss\"],"` | — |
| [SRC-829A979985-L000547](../../tests/test_generation_acceptance_matrix.py#L547) | 547 | `"                \"provider_counts\": {\"duckduckgo_html\": 1, \"bing_rss\": 1},"` | — |
| [SRC-829A979985-L000548](../../tests/test_generation_acceptance_matrix.py#L548) | 548 | `"                \"platform_counts\": {\"web\": 2},"` | — |
| [SRC-829A979985-L000549](../../tests/test_generation_acceptance_matrix.py#L549) | 549 | `"                \"social_direct_results\": 0,"` | — |
| [SRC-829A979985-L000550](../../tests/test_generation_acceptance_matrix.py#L550) | 550 | `"                \"provider_diagnostics\": [],"` | — |
| [SRC-829A979985-L000551](../../tests/test_generation_acceptance_matrix.py#L551) | 551 | `"                \"evidence_signals\": {},"` | — |
| [SRC-829A979985-L000552](../../tests/test_generation_acceptance_matrix.py#L552) | 552 | `"            },"` | — |
| [SRC-829A979985-L000553](../../tests/test_generation_acceptance_matrix.py#L553) | 553 | `"        ),"` | — |
| [SRC-829A979985-L000554](../../tests/test_generation_acceptance_matrix.py#L554) | 554 | `"    )"` | — |
| [SRC-829A979985-L000555](../../tests/test_generation_acceptance_matrix.py#L555) | 555 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, item: True)"` | — |
| [SRC-829A979985-L000556](../../tests/test_generation_acceptance_matrix.py#L556) | 556 | `"    final_draft = \"الخلاصة: يوجد اختلاف في اكتمال البيانات، ولا يمكن حسم المقارنة من المقتطف وحده [المصدر 1].\""` | — |
| [SRC-829A979985-L000557](../../tests/test_generation_acceptance_matrix.py#L557) | 557 | `"    repaired_answer = ("` | — |
| [SRC-829A979985-L000558](../../tests/test_generation_acceptance_matrix.py#L558) | 558 | `"        \"السعر الإجمالي 100000 جنيه والمساحة 100 متر في المصدر الأول [المصدر 1]. \""` | — |
| [SRC-829A979985-L000559](../../tests/test_generation_acceptance_matrix.py#L559) | 559 | `"        \"الإعلان الثاني يذكر سعرًا دون بيان المساحة، وهذه هي البيانات الناقصة [المصدر 2].\""` | — |
| [SRC-829A979985-L000560](../../tests/test_generation_acceptance_matrix.py#L560) | 560 | `"    )"` | — |
| [SRC-829A979985-L000561](../../tests/test_generation_acceptance_matrix.py#L561) | 561 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: final_draft)"` | — |
| [SRC-829A979985-L000562](../../tests/test_generation_acceptance_matrix.py#L562) | 562 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-829A979985-L000563](../../tests/test_generation_acceptance_matrix.py#L563) | 563 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000564](../../tests/test_generation_acceptance_matrix.py#L564) | 564 | `"        agent,"` | — |
| [SRC-829A979985-L000565](../../tests/test_generation_acceptance_matrix.py#L565) | 565 | `"        \"_repair_answer_coverage\","` | — |
| [SRC-829A979985-L000566](../../tests/test_generation_acceptance_matrix.py#L566) | 566 | `"        lambda question, answer, sources, missing_targets: repaired_answer,"` | — |
| [SRC-829A979985-L000567](../../tests/test_generation_acceptance_matrix.py#L567) | 567 | `"    )"` | — |
| [SRC-829A979985-L000568](../../tests/test_generation_acceptance_matrix.py#L568) | 568 | `""` | — |
| [SRC-829A979985-L000569](../../tests/test_generation_acceptance_matrix.py#L569) | 569 | `"    result = agent.answer(question)"` | — |
| [SRC-829A979985-L000570](../../tests/test_generation_acceptance_matrix.py#L570) | 570 | `""` | — |
| [SRC-829A979985-L000571](../../tests/test_generation_acceptance_matrix.py#L571) | 571 | `"    assert result[\"search_attempted\"] is True"` | — |
| [SRC-829A979985-L000572](../../tests/test_generation_acceptance_matrix.py#L572) | 572 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-829A979985-L000573](../../tests/test_generation_acceptance_matrix.py#L573) | 573 | `"    assert len(result[\"sources\"]) == 2"` | — |
| [SRC-829A979985-L000574](../../tests/test_generation_acceptance_matrix.py#L574) | 574 | `"    assert result[\"search_report\"][\"search_outcome\"] == \"attempted_with_usable_sources\""` | — |
| [SRC-829A979985-L000575](../../tests/test_generation_acceptance_matrix.py#L575) | 575 | `"    assert result[\"search_report\"][\"pages_fetched\"] == 1"` | — |
| [SRC-829A979985-L000576](../../tests/test_generation_acceptance_matrix.py#L576) | 576 | `"    assert result[\"final_answer_status\"] == \"model_answer_generated\""` | — |
| [SRC-829A979985-L000577](../../tests/test_generation_acceptance_matrix.py#L577) | 577 | `"    assert result[\"coverage_repair_status\"] == \"revised_and_reaudited\""` | — |
| [SRC-829A979985-L000578](../../tests/test_generation_acceptance_matrix.py#L578) | 578 | `"    assert result[\"search_report\"][\"second_pass_review\"] == \"model_claim_audit_completed\""` | — |
| [SRC-829A979985-L000579](../../tests/test_generation_acceptance_matrix.py#L579) | 579 | `"    assert result[\"answer_coverage\"][\"automatically_graded\"] is False"` | — |
| [SRC-829A979985-L000580](../../tests/test_generation_acceptance_matrix.py#L580) | 580 | `"    assert result[\"answer_coverage\"][\"status\"] == \"model_review_requested_not_machine_verified\""` | — |
| [SRC-829A979985-L000581](../../tests/test_generation_acceptance_matrix.py#L581) | 581 | `"    assert \"السعر الإجمالي\" in result[\"answer\"]"` | — |
| [SRC-829A979985-L000582](../../tests/test_generation_acceptance_matrix.py#L582) | 582 | `"    assert \"البيانات الناقصة\" in result[\"answer\"]"` | — |
| [SRC-829A979985-L000583](../../tests/test_generation_acceptance_matrix.py#L583) | 583 | `"    assert result[\"citation_validation\"][\"method\"] == \"numeric_source_index_range_only\""` | — |
| [SRC-829A979985-L000584](../../tests/test_generation_acceptance_matrix.py#L584) | 584 | `"    assert result[\"answer_integrity\"][\"method\"] == \"deterministic_lexical_screen_only\""` | — |
| [SRC-829A979985-L000585](../../tests/test_generation_acceptance_matrix.py#L585) | 585 | `"    assert result[\"answer_integrity\"][\"semantic_verification\"] is False"` | — |
| [SRC-829A979985-L000586](../../tests/test_generation_acceptance_matrix.py#L586) | 586 | `"    assert result[\"search_report\"][\"answer_integrity\"] == result[\"answer_integrity\"]"` | — |
| [SRC-829A979985-L000587](../../tests/test_generation_acceptance_matrix.py#L587) | 587 | `"    assert result[\"answer_integrity\"][\"pages_with_extracted_text\"] == 1"` | — |
| [SRC-829A979985-L000588](../../tests/test_generation_acceptance_matrix.py#L588) | 588 | `"    assert result[\"answer_integrity\"][\"potentially_missing_target_count\"] >= 0"` | — |
| [SRC-829A979985-L000589](../../tests/test_generation_acceptance_matrix.py#L589) | 589 | `""` | — |
| [SRC-829A979985-L000590](../../tests/test_generation_acceptance_matrix.py#L590) | 590 | `""` | — |
| [SRC-829A979985-L000591](../../tests/test_generation_acceptance_matrix.py#L591) | 591 | `"@pytest.mark.parametrize("` | — |
| [SRC-829A979985-L000592](../../tests/test_generation_acceptance_matrix.py#L592) | 592 | `"    \"malformed_review\","` | — |
| [SRC-829A979985-L000593](../../tests/test_generation_acceptance_matrix.py#L593) | 593 | `"    ["` | — |
| [SRC-829A979985-L000594](../../tests/test_generation_acceptance_matrix.py#L594) | 594 | `"        \"إجابة من دون أي علامات فصل\","` | — |
| [SRC-829A979985-L000595](../../tests/test_generation_acceptance_matrix.py#L595) | 595 | `"        \"<<<OMARAI_FINAL_ANSWER>>>إجابة بلا علامة نهاية\","` | — |
| [SRC-829A979985-L000596](../../tests/test_generation_acceptance_matrix.py#L596) | 596 | `"        \"<<<OMARAI_FINAL_ANSWER>>>إجابة<<<END_OMARAI_FINAL_ANSWER>>> نص زائد خارج الإجابة\","` | — |
| [SRC-829A979985-L000597](../../tests/test_generation_acceptance_matrix.py#L597) | 597 | `"    ],"` | — |
| [SRC-829A979985-L000598](../../tests/test_generation_acceptance_matrix.py#L598) | 598 | `")"` | — |
| [SRC-829A979985-L000599](../../tests/test_generation_acceptance_matrix.py#L599) | 599 | `"def test_reviewer_rejects_missing_or_unbounded_final_answer_delimiters("` | — |
| [SRC-829A979985-L000600](../../tests/test_generation_acceptance_matrix.py#L600) | 600 | `"    monkeypatch, malformed_review"` | — |
| [SRC-829A979985-L000601](../../tests/test_generation_acceptance_matrix.py#L601) | 601 | `"):"` | — |
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
