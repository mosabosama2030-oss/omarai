# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **042**
- سجلات الأسطر: **800**
- النطاق: SRC-3D0DE98F65-L000169 إلى SRC-AFFCF23BD4-L000245
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-3D0DE98F65 — [tests/test_question_requirement_loop.py](../../tests/test_question_requirement_loop.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-3D0DE98F65-L000169](../../tests/test_question_requirement_loop.py#L169) | 169 | `"        assert any(item[\"target\"] in source[\"title\"] for source in matched[:2])"` | — |
| [SRC-3D0DE98F65-L000170](../../tests/test_question_requirement_loop.py#L170) | 170 | `"    assert report[\"queries_planned\"] == 4"` | — |
| [SRC-3D0DE98F65-L000171](../../tests/test_question_requirement_loop.py#L171) | 171 | `"    assert report[\"queries_attempted\"] == 4"` | — |
| [SRC-3D0DE98F65-L000172](../../tests/test_question_requirement_loop.py#L172) | 172 | `""` | — |
| [SRC-3D0DE98F65-L000173](../../tests/test_question_requirement_loop.py#L173) | 173 | `""` | — |
| [SRC-3D0DE98F65-L000174](../../tests/test_question_requirement_loop.py#L174) | 174 | `"def test_answer_integrity_exposes_requirement_evidence_separately_from_word_overlap() -> None:"` | — |
| [SRC-3D0DE98F65-L000175](../../tests/test_question_requirement_loop.py#L175) | 175 | `"    plan = fallback_plan(QUESTION)"` | — |
| [SRC-3D0DE98F65-L000176](../../tests/test_question_requirement_loop.py#L176) | 176 | `"    price_query = next(item[\"query\"] for item in plan[\"requirement_queries\"] if item[\"target\"] == \"السعر\")"` | — |
| [SRC-3D0DE98F65-L000177](../../tests/test_question_requirement_loop.py#L177) | 177 | `"    sources = ["` | — |
| [SRC-3D0DE98F65-L000178](../../tests/test_question_requirement_loop.py#L178) | 178 | `"        {"` | — |
| [SRC-3D0DE98F65-L000179](../../tests/test_question_requirement_loop.py#L179) | 179 | `"            \"url\": \"https://example.com/price\","` | — |
| [SRC-3D0DE98F65-L000180](../../tests/test_question_requirement_loop.py#L180) | 180 | `"            \"title\": \"Phone pricing\","` | — |
| [SRC-3D0DE98F65-L000181](../../tests/test_question_requirement_loop.py#L181) | 181 | `"            \"snippet\": \"The price is 100 EGP.\","` | — |
| [SRC-3D0DE98F65-L000182](../../tests/test_question_requirement_loop.py#L182) | 182 | `"            \"page_fetched\": False,"` | — |
| [SRC-3D0DE98F65-L000183](../../tests/test_question_requirement_loop.py#L183) | 183 | `"            \"queries\": [price_query],"` | — |
| [SRC-3D0DE98F65-L000184](../../tests/test_question_requirement_loop.py#L184) | 184 | `"        }"` | — |
| [SRC-3D0DE98F65-L000185](../../tests/test_question_requirement_loop.py#L185) | 185 | `"    ]"` | — |
| [SRC-3D0DE98F65-L000186](../../tests/test_question_requirement_loop.py#L186) | 186 | `""` | — |
| [SRC-3D0DE98F65-L000187](../../tests/test_question_requirement_loop.py#L187) | 187 | `"    result = audit_answer_integrity("` | — |
| [SRC-3D0DE98F65-L000188](../../tests/test_question_requirement_loop.py#L188) | 188 | `"        QUESTION,"` | — |
| [SRC-3D0DE98F65-L000189](../../tests/test_question_requirement_loop.py#L189) | 189 | `"        \"السعر غير محسوم والبطارية غير محسومة والكاميرا غير محسومة.\","` | — |
| [SRC-3D0DE98F65-L000190](../../tests/test_question_requirement_loop.py#L190) | 190 | `"        sources,"` | — |
| [SRC-3D0DE98F65-L000191](../../tests/test_question_requirement_loop.py#L191) | 191 | `"        plan[\"coverage_targets\"],"` | — |
| [SRC-3D0DE98F65-L000192](../../tests/test_question_requirement_loop.py#L192) | 192 | `"        plan[\"requirement_queries\"],"` | — |
| [SRC-3D0DE98F65-L000193](../../tests/test_question_requirement_loop.py#L193) | 193 | `"    )"` | — |
| [SRC-3D0DE98F65-L000194](../../tests/test_question_requirement_loop.py#L194) | 194 | `""` | — |
| [SRC-3D0DE98F65-L000195](../../tests/test_question_requirement_loop.py#L195) | 195 | `"    evidence = {item[\"target\"]: item for item in result[\"requirement_evidence\"]}"` | — |
| [SRC-3D0DE98F65-L000196](../../tests/test_question_requirement_loop.py#L196) | 196 | `"    assert evidence[\"السعر\"][\"status\"] == \"candidate_evidence_found_not_verified\""` | — |
| [SRC-3D0DE98F65-L000197](../../tests/test_question_requirement_loop.py#L197) | 197 | `"    assert evidence[\"البطارية\"][\"status\"] == \"no_candidate_evidence_found\""` | — |
| [SRC-3D0DE98F65-L000198](../../tests/test_question_requirement_loop.py#L198) | 198 | `"    assert result[\"semantic_verification\"] is False"` | — |
| [SRC-3D0DE98F65-L000199](../../tests/test_question_requirement_loop.py#L199) | 199 | `"    assert result[\"requirements_without_candidate_evidence_count\"] == 2"` | — |
| [SRC-3D0DE98F65-L000200](../../tests/test_question_requirement_loop.py#L200) | 200 | `"    assert result[\"target_coverage\"][0][\"evidence\"][\"status\"] == \"candidate_evidence_found_not_verified\""` | — |
| [SRC-3D0DE98F65-L000201](../../tests/test_question_requirement_loop.py#L201) | 201 | `""` | — |
| [SRC-3D0DE98F65-L000202](../../tests/test_question_requirement_loop.py#L202) | 202 | `""` | — |
| [SRC-3D0DE98F65-L000203](../../tests/test_question_requirement_loop.py#L203) | 203 | `"def test_general_compound_factual_question_creates_one_requirement_per_aspect() -> None:"` | — |
| [SRC-3D0DE98F65-L000204](../../tests/test_question_requirement_loop.py#L204) | 204 | `"    question = \"اذكر عاصمة مصر وعدد سكان القاهرة، مع مصدر وتاريخ لكل معلومة\""` | — |
| [SRC-3D0DE98F65-L000205](../../tests/test_question_requirement_loop.py#L205) | 205 | `"    targets = extract_question_coverage_targets(question)"` | — |
| [SRC-3D0DE98F65-L000206](../../tests/test_question_requirement_loop.py#L206) | 206 | `"    assert targets == [\"العاصمة\", \"عدد السكان\"]"` | — |
| [SRC-3D0DE98F65-L000207](../../tests/test_question_requirement_loop.py#L207) | 207 | `""` | — |
| [SRC-3D0DE98F65-L000208](../../tests/test_question_requirement_loop.py#L208) | 208 | `""` | — |
| [SRC-3D0DE98F65-L000209](../../tests/test_question_requirement_loop.py#L209) | 209 | `"def test_general_compound_factual_fallback_plan_keeps_separate_requirement_queries() -> None:"` | — |
| [SRC-3D0DE98F65-L000210](../../tests/test_question_requirement_loop.py#L210) | 210 | `"    question = \"اذكر عاصمة مصر وعدد سكان القاهرة، مع مصدر وتاريخ لكل معلومة\""` | — |
| [SRC-3D0DE98F65-L000211](../../tests/test_question_requirement_loop.py#L211) | 211 | `"    plan = fallback_plan(question)"` | — |
| [SRC-3D0DE98F65-L000212](../../tests/test_question_requirement_loop.py#L212) | 212 | `"    targets = [item[\"target\"] for item in plan[\"requirement_queries\"]]"` | — |
| [SRC-3D0DE98F65-L000213](../../tests/test_question_requirement_loop.py#L213) | 213 | `"    assert targets == [\"العاصمة\", \"عدد السكان\"]"` | — |
| [SRC-3D0DE98F65-L000214](../../tests/test_question_requirement_loop.py#L214) | 214 | `"    assert all(item[\"query\"] in plan[\"queries\"] for item in plan[\"requirement_queries\"])"` | — |
| [SRC-3D0DE98F65-L000215](../../tests/test_question_requirement_loop.py#L215) | 215 | `"    assert len(plan[\"queries\"]) <= MAX_PLAN_QUERIES"` | — |
## اختبارات

### FILE-C353AAAC10 — [tests/test_request_budget.py](../../tests/test_request_budget.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-C353AAAC10-L000001](../../tests/test_request_budget.py#L1) | 1 | `"\"\"\"Unit tests for Omarai's per-request resource budget.\"\"\""` | — |
| [SRC-C353AAAC10-L000002](../../tests/test_request_budget.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-C353AAAC10-L000003](../../tests/test_request_budget.py#L3) | 3 | `""` | — |
| [SRC-C353AAAC10-L000004](../../tests/test_request_budget.py#L4) | 4 | `"import pytest"` | — |
| [SRC-C353AAAC10-L000005](../../tests/test_request_budget.py#L5) | 5 | `""` | — |
| [SRC-C353AAAC10-L000006](../../tests/test_request_budget.py#L6) | 6 | `"from agents.request_budget import RequestBudget, RequestBudgetExceeded"` | — |
| [SRC-C353AAAC10-L000007](../../tests/test_request_budget.py#L7) | 7 | `""` | — |
| [SRC-C353AAAC10-L000008](../../tests/test_request_budget.py#L8) | 8 | `""` | — |
| [SRC-C353AAAC10-L000009](../../tests/test_request_budget.py#L9) | 9 | `"class FakeClock:"` | — |
| [SRC-C353AAAC10-L000010](../../tests/test_request_budget.py#L10) | 10 | `"    def __init__(self, value: float = 100.0) -> None:"` | — |
| [SRC-C353AAAC10-L000011](../../tests/test_request_budget.py#L11) | 11 | `"        self.value = value"` | — |
| [SRC-C353AAAC10-L000012](../../tests/test_request_budget.py#L12) | 12 | `""` | — |
| [SRC-C353AAAC10-L000013](../../tests/test_request_budget.py#L13) | 13 | `"    def __call__(self) -> float:"` | — |
| [SRC-C353AAAC10-L000014](../../tests/test_request_budget.py#L14) | 14 | `"        return self.value"` | — |
| [SRC-C353AAAC10-L000015](../../tests/test_request_budget.py#L15) | 15 | `""` | — |
| [SRC-C353AAAC10-L000016](../../tests/test_request_budget.py#L16) | 16 | `""` | — |
| [SRC-C353AAAC10-L000017](../../tests/test_request_budget.py#L17) | 17 | `"def test_resource_reservations_are_bounded_and_thread_safe_in_snapshot():"` | — |
| [SRC-C353AAAC10-L000018](../../tests/test_request_budget.py#L18) | 18 | `"    clock = FakeClock()"` | — |
| [SRC-C353AAAC10-L000019](../../tests/test_request_budget.py#L19) | 19 | `"    budget = RequestBudget("` | — |
| [SRC-C353AAAC10-L000020](../../tests/test_request_budget.py#L20) | 20 | `"        timeout_seconds=10,"` | — |
| [SRC-C353AAAC10-L000021](../../tests/test_request_budget.py#L21) | 21 | `"        limits={\"search_calls\": 1},"` | — |
| [SRC-C353AAAC10-L000022](../../tests/test_request_budget.py#L22) | 22 | `"        clock=clock,"` | — |
| [SRC-C353AAAC10-L000023](../../tests/test_request_budget.py#L23) | 23 | `"    )"` | — |
| [SRC-C353AAAC10-L000024](../../tests/test_request_budget.py#L24) | 24 | `""` | — |
| [SRC-C353AAAC10-L000025](../../tests/test_request_budget.py#L25) | 25 | `"    budget.reserve(\"search_calls\")"` | — |
| [SRC-C353AAAC10-L000026](../../tests/test_request_budget.py#L26) | 26 | `"    with pytest.raises(RequestBudgetExceeded, match=\"search_calls\"):"` | — |
| [SRC-C353AAAC10-L000027](../../tests/test_request_budget.py#L27) | 27 | `"        budget.reserve(\"search_calls\")"` | — |
| [SRC-C353AAAC10-L000028](../../tests/test_request_budget.py#L28) | 28 | `""` | — |
| [SRC-C353AAAC10-L000029](../../tests/test_request_budget.py#L29) | 29 | `"    snapshot = budget.snapshot()"` | — |
| [SRC-C353AAAC10-L000030](../../tests/test_request_budget.py#L30) | 30 | `"    assert snapshot[\"counts\"][\"search_calls\"] == 1"` | — |
| [SRC-C353AAAC10-L000031](../../tests/test_request_budget.py#L31) | 31 | `"    assert snapshot[\"limits\"][\"search_calls\"] == 1"` | — |
| [SRC-C353AAAC10-L000032](../../tests/test_request_budget.py#L32) | 32 | `"    assert snapshot[\"deadline_exceeded\"] is False"` | — |
| [SRC-C353AAAC10-L000033](../../tests/test_request_budget.py#L33) | 33 | `""` | — |
| [SRC-C353AAAC10-L000034](../../tests/test_request_budget.py#L34) | 34 | `""` | — |
| [SRC-C353AAAC10-L000035](../../tests/test_request_budget.py#L35) | 35 | `"def test_deadline_blocks_new_work_and_caps_outbound_timeout():"` | — |
| [SRC-C353AAAC10-L000036](../../tests/test_request_budget.py#L36) | 36 | `"    clock = FakeClock()"` | — |
| [SRC-C353AAAC10-L000037](../../tests/test_request_budget.py#L37) | 37 | `"    budget = RequestBudget(timeout_seconds=10, clock=clock)"` | — |
| [SRC-C353AAAC10-L000038](../../tests/test_request_budget.py#L38) | 38 | `""` | — |
| [SRC-C353AAAC10-L000039](../../tests/test_request_budget.py#L39) | 39 | `"    clock.value += 7"` | — |
| [SRC-C353AAAC10-L000040](../../tests/test_request_budget.py#L40) | 40 | `"    assert budget.timeout_for(30) == pytest.approx(3)"` | — |
| [SRC-C353AAAC10-L000041](../../tests/test_request_budget.py#L41) | 41 | `"    assert budget.timeout_for(1) == pytest.approx(1)"` | — |
| [SRC-C353AAAC10-L000042](../../tests/test_request_budget.py#L42) | 42 | `""` | — |
| [SRC-C353AAAC10-L000043](../../tests/test_request_budget.py#L43) | 43 | `"    clock.value += 4"` | — |
| [SRC-C353AAAC10-L000044](../../tests/test_request_budget.py#L44) | 44 | `"    assert budget.remaining_seconds() == 0"` | — |
| [SRC-C353AAAC10-L000045](../../tests/test_request_budget.py#L45) | 45 | `"    with pytest.raises(RequestBudgetExceeded, match=\"وقت الطلب\"):"` | — |
| [SRC-C353AAAC10-L000046](../../tests/test_request_budget.py#L46) | 46 | `"        budget.reserve(\"model_calls\")"` | — |
| [SRC-C353AAAC10-L000047](../../tests/test_request_budget.py#L47) | 47 | `"    with pytest.raises(RequestBudgetExceeded, match=\"وقت الطلب\"):"` | — |
| [SRC-C353AAAC10-L000048](../../tests/test_request_budget.py#L48) | 48 | `"        budget.timeout_for(3)"` | — |
| [SRC-C353AAAC10-L000049](../../tests/test_request_budget.py#L49) | 49 | `""` | — |
| [SRC-C353AAAC10-L000050](../../tests/test_request_budget.py#L50) | 50 | `""` | — |
| [SRC-C353AAAC10-L000051](../../tests/test_request_budget.py#L51) | 51 | `"def test_environment_overrides_are_clamped(monkeypatch):"` | — |
| [SRC-C353AAAC10-L000052](../../tests/test_request_budget.py#L52) | 52 | `"    monkeypatch.setenv(\"OMARAI_REQUEST_BUDGET_SECONDS\", \"999\")"` | — |
| [SRC-C353AAAC10-L000053](../../tests/test_request_budget.py#L53) | 53 | `"    monkeypatch.setenv(\"OMARAI_REQUEST_MAX_SEARCH_CALLS\", \"999\")"` | — |
| [SRC-C353AAAC10-L000054](../../tests/test_request_budget.py#L54) | 54 | `"    monkeypatch.setenv(\"OMARAI_REQUEST_MAX_MODEL_CALLS\", \"-1\")"` | — |
| [SRC-C353AAAC10-L000055](../../tests/test_request_budget.py#L55) | 55 | `"    monkeypatch.setenv(\"OMARAI_REQUEST_MAX_TOOL_CALLS\", \"-1\")"` | — |
| [SRC-C353AAAC10-L000056](../../tests/test_request_budget.py#L56) | 56 | `""` | — |
| [SRC-C353AAAC10-L000057](../../tests/test_request_budget.py#L57) | 57 | `"    snapshot = RequestBudget.from_environment().snapshot()"` | — |
| [SRC-C353AAAC10-L000058](../../tests/test_request_budget.py#L58) | 58 | `""` | — |
| [SRC-C353AAAC10-L000059](../../tests/test_request_budget.py#L59) | 59 | `"    assert snapshot[\"timeout_seconds\"] == 120"` | — |
| [SRC-C353AAAC10-L000060](../../tests/test_request_budget.py#L60) | 60 | `"    assert snapshot[\"limits\"][\"search_calls\"] == 40"` | — |
| [SRC-C353AAAC10-L000061](../../tests/test_request_budget.py#L61) | 61 | `"    assert snapshot[\"limits\"][\"model_calls\"] == 1"` | — |
| [SRC-C353AAAC10-L000062](../../tests/test_request_budget.py#L62) | 62 | `"    assert snapshot[\"limits\"][\"tool_calls\"] == 0"` | — |
| [SRC-C353AAAC10-L000063](../../tests/test_request_budget.py#L63) | 63 | `""` | — |
| [SRC-C353AAAC10-L000064](../../tests/test_request_budget.py#L64) | 64 | `""` | — |
| [SRC-C353AAAC10-L000065](../../tests/test_request_budget.py#L65) | 65 | `"def test_web_agent_reserves_search_model_and_page_work_before_io(monkeypatch):"` | — |
| [SRC-C353AAAC10-L000066](../../tests/test_request_budget.py#L66) | 66 | `"    from agents.web_agent import WebAgent"` | — |
| [SRC-C353AAAC10-L000067](../../tests/test_request_budget.py#L67) | 67 | `""` | — |
| [SRC-C353AAAC10-L000068](../../tests/test_request_budget.py#L68) | 68 | `"    agent = WebAgent()"` | — |
| [SRC-C353AAAC10-L000069](../../tests/test_request_budget.py#L69) | 69 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-C353AAAC10-L000070](../../tests/test_request_budget.py#L70) | 70 | `""` | — |
| [SRC-C353AAAC10-L000071](../../tests/test_request_budget.py#L71) | 71 | `"    agent._request_budget = RequestBudget(limits={\"search_queries\": 0})"` | — |
| [SRC-C353AAAC10-L000072](../../tests/test_request_budget.py#L72) | 72 | `"    with pytest.raises(RequestBudgetExceeded, match=\"search_queries\"):"` | — |
| [SRC-C353AAAC10-L000073](../../tests/test_request_budget.py#L73) | 73 | `"        agent._search_web(\"budget test\")"` | — |
| [SRC-C353AAAC10-L000074](../../tests/test_request_budget.py#L74) | 74 | `""` | — |
| [SRC-C353AAAC10-L000075](../../tests/test_request_budget.py#L75) | 75 | `"    agent._request_budget = RequestBudget(limits={\"model_calls\": 0})"` | — |
| [SRC-C353AAAC10-L000076](../../tests/test_request_budget.py#L76) | 76 | `"    monkeypatch.setattr("` | — |
| [SRC-C353AAAC10-L000077](../../tests/test_request_budget.py#L77) | 77 | `"        \"agents.web_agent.urllib.request.urlopen\","` | — |
| [SRC-C353AAAC10-L000078](../../tests/test_request_budget.py#L78) | 78 | `"        lambda *args, **kwargs: pytest.fail(\"model HTTP request must not start\"),"` | — |
| [SRC-C353AAAC10-L000079](../../tests/test_request_budget.py#L79) | 79 | `"    )"` | — |
| [SRC-C353AAAC10-L000080](../../tests/test_request_budget.py#L80) | 80 | `"    with pytest.raises(RequestBudgetExceeded, match=\"model_calls\"):"` | — |
| [SRC-C353AAAC10-L000081](../../tests/test_request_budget.py#L81) | 81 | `"        agent._request_completion([{\"role\": \"user\", \"content\": \"test\"}])"` | — |
| [SRC-C353AAAC10-L000082](../../tests/test_request_budget.py#L82) | 82 | `""` | — |
| [SRC-C353AAAC10-L000083](../../tests/test_request_budget.py#L83) | 83 | `"    agent._request_budget = RequestBudget(limits={\"page_fetches\": 0})"` | — |
| [SRC-C353AAAC10-L000084](../../tests/test_request_budget.py#L84) | 84 | `"    with pytest.raises(RequestBudgetExceeded, match=\"page_fetches\"):"` | — |
| [SRC-C353AAAC10-L000085](../../tests/test_request_budget.py#L85) | 85 | `"        agent._fetch_page(\"https://example.com/\")"` | — |
| [SRC-C353AAAC10-L000086](../../tests/test_request_budget.py#L86) | 86 | `""` | — |
| [SRC-C353AAAC10-L000087](../../tests/test_request_budget.py#L87) | 87 | `""` | — |
| [SRC-C353AAAC10-L000088](../../tests/test_request_budget.py#L88) | 88 | `"def test_social_provider_reserves_budget_before_network_io(monkeypatch):"` | — |
| [SRC-C353AAAC10-L000089](../../tests/test_request_budget.py#L89) | 89 | `"    from agents.web_agent import WebAgent"` | — |
| [SRC-C353AAAC10-L000090](../../tests/test_request_budget.py#L90) | 90 | `""` | — |
| [SRC-C353AAAC10-L000091](../../tests/test_request_budget.py#L91) | 91 | `"    monkeypatch.setenv(\"REDDIT_CLIENT_ID\", \"test-client\")"` | — |
| [SRC-C353AAAC10-L000092](../../tests/test_request_budget.py#L92) | 92 | `"    monkeypatch.setenv(\"REDDIT_CLIENT_SECRET\", \"test-secret\")"` | — |
| [SRC-C353AAAC10-L000093](../../tests/test_request_budget.py#L93) | 93 | `"    agent = WebAgent()"` | — |
| [SRC-C353AAAC10-L000094](../../tests/test_request_budget.py#L94) | 94 | `"    agent._request_budget = RequestBudget(limits={\"search_calls\": 0})"` | — |
| [SRC-C353AAAC10-L000095](../../tests/test_request_budget.py#L95) | 95 | `""` | — |
| [SRC-C353AAAC10-L000096](../../tests/test_request_budget.py#L96) | 96 | `"    monkeypatch.setattr("` | — |
| [SRC-C353AAAC10-L000097](../../tests/test_request_budget.py#L97) | 97 | `"        \"httpx.post\","` | — |
| [SRC-C353AAAC10-L000098](../../tests/test_request_budget.py#L98) | 98 | `"        lambda *args, **kwargs: pytest.fail(\"social HTTP request must not start\"),"` | — |
| [SRC-C353AAAC10-L000099](../../tests/test_request_budget.py#L99) | 99 | `"    )"` | — |
| [SRC-C353AAAC10-L000100](../../tests/test_request_budget.py#L100) | 100 | `"    with pytest.raises(RequestBudgetExceeded, match=\"search_calls\"):"` | — |
| [SRC-C353AAAC10-L000101](../../tests/test_request_budget.py#L101) | 101 | `"        agent._search_social(\"budget test\", [\"reddit\"])"` | — |
| [SRC-C353AAAC10-L000102](../../tests/test_request_budget.py#L102) | 102 | `""` | — |
| [SRC-C353AAAC10-L000103](../../tests/test_request_budget.py#L103) | 103 | `""` | — |
| [SRC-C353AAAC10-L000104](../../tests/test_request_budget.py#L104) | 104 | `"@pytest.mark.parametrize("` | — |
| [SRC-C353AAAC10-L000105](../../tests/test_request_budget.py#L105) | 105 | `"    (\"resource\", \"limit\"),"` | — |
| [SRC-C353AAAC10-L000106](../../tests/test_request_budget.py#L106) | 106 | `"    ["` | — |
| [SRC-C353AAAC10-L000107](../../tests/test_request_budget.py#L107) | 107 | `"        (\"search_queries\", 8),"` | — |
| [SRC-C353AAAC10-L000108](../../tests/test_request_budget.py#L108) | 108 | `"        (\"search_calls\", 32),"` | — |
| [SRC-C353AAAC10-L000109](../../tests/test_request_budget.py#L109) | 109 | `"        (\"model_calls\", 8),"` | — |
| [SRC-C353AAAC10-L000110](../../tests/test_request_budget.py#L110) | 110 | `"        (\"page_fetches\", 8),"` | — |
| [SRC-C353AAAC10-L000111](../../tests/test_request_budget.py#L111) | 111 | `"        (\"tool_calls\", 3),"` | — |
| [SRC-C353AAAC10-L000112](../../tests/test_request_budget.py#L112) | 112 | `"    ],"` | — |
| [SRC-C353AAAC10-L000113](../../tests/test_request_budget.py#L113) | 113 | `")"` | — |
| [SRC-C353AAAC10-L000114](../../tests/test_request_budget.py#L114) | 114 | `"def test_each_resource_counter_stops_at_its_limit(resource, limit):"` | — |
| [SRC-C353AAAC10-L000115](../../tests/test_request_budget.py#L115) | 115 | `"    budget = RequestBudget(timeout_seconds=10, limits={resource: limit})"` | — |
| [SRC-C353AAAC10-L000116](../../tests/test_request_budget.py#L116) | 116 | `""` | — |
| [SRC-C353AAAC10-L000117](../../tests/test_request_budget.py#L117) | 117 | `"    for expected_count in range(1, limit + 1):"` | — |
| [SRC-C353AAAC10-L000118](../../tests/test_request_budget.py#L118) | 118 | `"        budget.reserve(resource)"` | — |
| [SRC-C353AAAC10-L000119](../../tests/test_request_budget.py#L119) | 119 | `"        snapshot = budget.snapshot()"` | — |
| [SRC-C353AAAC10-L000120](../../tests/test_request_budget.py#L120) | 120 | `"        assert snapshot[\"counts\"][resource] == expected_count"` | — |
| [SRC-C353AAAC10-L000121](../../tests/test_request_budget.py#L121) | 121 | `"        assert snapshot[\"counts\"][resource] <= snapshot[\"limits\"][resource]"` | — |
| [SRC-C353AAAC10-L000122](../../tests/test_request_budget.py#L122) | 122 | `""` | — |
| [SRC-C353AAAC10-L000123](../../tests/test_request_budget.py#L123) | 123 | `"    with pytest.raises(RequestBudgetExceeded, match=resource):"` | — |
| [SRC-C353AAAC10-L000124](../../tests/test_request_budget.py#L124) | 124 | `"        budget.reserve(resource)"` | — |
| [SRC-C353AAAC10-L000125](../../tests/test_request_budget.py#L125) | 125 | `""` | — |
| [SRC-C353AAAC10-L000126](../../tests/test_request_budget.py#L126) | 126 | `"    snapshot = budget.snapshot()"` | — |
| [SRC-C353AAAC10-L000127](../../tests/test_request_budget.py#L127) | 127 | `"    assert snapshot[\"counts\"][resource] == limit"` | — |
| [SRC-C353AAAC10-L000128](../../tests/test_request_budget.py#L128) | 128 | `"    assert resource in snapshot[\"exhausted_reasons\"]"` | — |
| [SRC-C353AAAC10-L000129](../../tests/test_request_budget.py#L129) | 129 | `""` | — |
| [SRC-C353AAAC10-L000130](../../tests/test_request_budget.py#L130) | 130 | `""` | — |
| [SRC-C353AAAC10-L000131](../../tests/test_request_budget.py#L131) | 131 | `"@pytest.mark.parametrize("` | — |
| [SRC-C353AAAC10-L000132](../../tests/test_request_budget.py#L132) | 132 | `"    \"resource\","` | — |
| [SRC-C353AAAC10-L000133](../../tests/test_request_budget.py#L133) | 133 | `"    [\"search_queries\", \"search_calls\", \"model_calls\", \"page_fetches\", \"tool_calls\"],"` | — |
| [SRC-C353AAAC10-L000134](../../tests/test_request_budget.py#L134) | 134 | `")"` | — |
| [SRC-C353AAAC10-L000135](../../tests/test_request_budget.py#L135) | 135 | `"def test_disabled_resource_never_starts_work(resource):"` | — |
| [SRC-C353AAAC10-L000136](../../tests/test_request_budget.py#L136) | 136 | `"    budget = RequestBudget(timeout_seconds=10, limits={resource: 0})"` | — |
| [SRC-C353AAAC10-L000137](../../tests/test_request_budget.py#L137) | 137 | `""` | — |
| [SRC-C353AAAC10-L000138](../../tests/test_request_budget.py#L138) | 138 | `"    assert budget.remaining_units(resource) == 0"` | — |
| [SRC-C353AAAC10-L000139](../../tests/test_request_budget.py#L139) | 139 | `"    with pytest.raises(RequestBudgetExceeded, match=resource):"` | — |
| [SRC-C353AAAC10-L000140](../../tests/test_request_budget.py#L140) | 140 | `"        budget.reserve(resource)"` | — |
| [SRC-C353AAAC10-L000141](../../tests/test_request_budget.py#L141) | 141 | `""` | — |
| [SRC-C353AAAC10-L000142](../../tests/test_request_budget.py#L142) | 142 | `"    snapshot = budget.snapshot()"` | — |
| [SRC-C353AAAC10-L000143](../../tests/test_request_budget.py#L143) | 143 | `"    assert snapshot[\"counts\"][resource] == 0"` | — |
| [SRC-C353AAAC10-L000144](../../tests/test_request_budget.py#L144) | 144 | `"    assert snapshot[\"limits\"][resource] == 0"` | — |
| [SRC-C353AAAC10-L000145](../../tests/test_request_budget.py#L145) | 145 | `"    assert resource in snapshot[\"disabled_resources\"]"` | — |
| [SRC-C353AAAC10-L000146](../../tests/test_request_budget.py#L146) | 146 | `"    assert resource in snapshot[\"exhausted_reasons\"]"` | — |
## اختبارات

### FILE-6BF96689A8 — [tests/test_research.py](../../tests/test_research.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6BF96689A8-L000001](../../tests/test_research.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-6BF96689A8-L000002](../../tests/test_research.py#L2) | 2 | `""` | — |
| [SRC-6BF96689A8-L000003](../../tests/test_research.py#L3) | 3 | `"from agents.research import ("` | — |
| [SRC-6BF96689A8-L000004](../../tests/test_research.py#L4) | 4 | `"    classify_source,"` | — |
| [SRC-6BF96689A8-L000005](../../tests/test_research.py#L5) | 5 | `"    compact_search_query,"` | — |
| [SRC-6BF96689A8-L000006](../../tests/test_research.py#L6) | 6 | `"    evidence_signal_report,"` | — |
| [SRC-6BF96689A8-L000007](../../tests/test_research.py#L7) | 7 | `"    fallback_plan,"` | — |
| [SRC-6BF96689A8-L000008](../../tests/test_research.py#L8) | 8 | `"    fuse_ranked_results,"` | — |
| [SRC-6BF96689A8-L000009](../../tests/test_research.py#L9) | 9 | `"    registrable_domain,"` | — |
| [SRC-6BF96689A8-L000010](../../tests/test_research.py#L10) | 10 | `"    validate_plan,"` | — |
| [SRC-6BF96689A8-L000011](../../tests/test_research.py#L11) | 11 | `")"` | — |
| [SRC-6BF96689A8-L000012](../../tests/test_research.py#L12) | 12 | `""` | — |
| [SRC-6BF96689A8-L000013](../../tests/test_research.py#L13) | 13 | `""` | — |
| [SRC-6BF96689A8-L000014](../../tests/test_research.py#L14) | 14 | `"def test_social_question_gets_platform_targeted_queries():"` | — |
| [SRC-6BF96689A8-L000015](../../tests/test_research.py#L15) | 15 | `"    plan = fallback_plan(\"ابحث في Reddit عن تجارب العملاء مع السيارات الكهربائية\")"` | — |
| [SRC-6BF96689A8-L000016](../../tests/test_research.py#L16) | 16 | `"    assert plan[\"social_focus\"] is True"` | — |
| [SRC-6BF96689A8-L000017](../../tests/test_research.py#L17) | 17 | `"    assert \"reddit\" in plan[\"platforms\"]"` | — |
| [SRC-6BF96689A8-L000018](../../tests/test_research.py#L18) | 18 | `"    assert any(\"site:reddit.com\" in query for query in plan[\"queries\"])"` | — |
| [SRC-6BF96689A8-L000019](../../tests/test_research.py#L19) | 19 | `"    assert len(plan[\"queries\"]) <= 8"` | — |
| [SRC-6BF96689A8-L000020](../../tests/test_research.py#L20) | 20 | `""` | — |
| [SRC-6BF96689A8-L000021](../../tests/test_research.py#L21) | 21 | `""` | — |
| [SRC-6BF96689A8-L000022](../../tests/test_research.py#L22) | 22 | `"def test_follow_up_query_keeps_prior_topic():"` | — |
| [SRC-6BF96689A8-L000023](../../tests/test_research.py#L23) | 23 | `"    history = [{\"role\": \"user\", \"content\": \"قارن سوق السيارات الكهربائية في مصر\"}]"` | — |
| [SRC-6BF96689A8-L000024](../../tests/test_research.py#L24) | 24 | `"    plan = fallback_plan(\"وطب الأسعار الحالية؟\", history)"` | — |
| [SRC-6BF96689A8-L000025](../../tests/test_research.py#L25) | 25 | `"    assert \"السيارات الكهربائية\" in plan[\"queries\"][0]"` | — |
| [SRC-6BF96689A8-L000026](../../tests/test_research.py#L26) | 26 | `"    assert plan[\"freshness\"] == \"current\""` | — |
| [SRC-6BF96689A8-L000027](../../tests/test_research.py#L27) | 27 | `""` | — |
| [SRC-6BF96689A8-L000028](../../tests/test_research.py#L28) | 28 | `""` | — |
| [SRC-6BF96689A8-L000029](../../tests/test_research.py#L29) | 29 | `"def test_plan_validation_caps_queries_and_rejects_non_string_values():"` | — |
| [SRC-6BF96689A8-L000030](../../tests/test_research.py#L30) | 30 | `"    candidate = {"` | — |
| [SRC-6BF96689A8-L000031](../../tests/test_research.py#L31) | 31 | `"        \"queries\": [\"بحث أ\", \"بحث ب\", None, \"بحث ج\", \"بحث د\", \"بحث هـ\", \"بحث سادس\", \"بحث سابع\", \"بحث ثامن\", \"بحث تاسع\"],"` | — |
| [SRC-6BF96689A8-L000032](../../tests/test_research.py#L32) | 32 | `"        \"social_focus\": True,"` | — |
| [SRC-6BF96689A8-L000033](../../tests/test_research.py#L33) | 33 | `"        \"freshness\": \"current\","` | — |
| [SRC-6BF96689A8-L000034](../../tests/test_research.py#L34) | 34 | `"        \"depth\": \"deep\","` | — |
| [SRC-6BF96689A8-L000035](../../tests/test_research.py#L35) | 35 | `"        \"platforms\": [\"reddit\", \"unknown\"],"` | — |
| [SRC-6BF96689A8-L000036](../../tests/test_research.py#L36) | 36 | `"    }"` | — |
| [SRC-6BF96689A8-L000037](../../tests/test_research.py#L37) | 37 | `"    plan = validate_plan(candidate, \"بحث عن منشورات\")"` | — |
| [SRC-6BF96689A8-L000038](../../tests/test_research.py#L38) | 38 | `"    assert len(plan[\"queries\"]) <= 8"` | — |
| [SRC-6BF96689A8-L000039](../../tests/test_research.py#L39) | 39 | `"    assert \"unknown\" not in plan[\"platforms\"]"` | — |
| [SRC-6BF96689A8-L000040](../../tests/test_research.py#L40) | 40 | `"    assert plan[\"social_focus\"] is True"` | — |
| [SRC-6BF96689A8-L000041](../../tests/test_research.py#L41) | 41 | `"    assert plan[\"freshness\"] == \"current\""` | — |
| [SRC-6BF96689A8-L000042](../../tests/test_research.py#L42) | 42 | `""` | — |
| [SRC-6BF96689A8-L000043](../../tests/test_research.py#L43) | 43 | `""` | — |
| [SRC-6BF96689A8-L000044](../../tests/test_research.py#L44) | 44 | `"def test_rank_fusion_promotes_cross_provider_consensus_and_deduplicates():"` | — |
| [SRC-6BF96689A8-L000045](../../tests/test_research.py#L45) | 45 | `"    batches = ["` | — |
| [SRC-6BF96689A8-L000046](../../tests/test_research.py#L46) | 46 | `"        {"` | — |
| [SRC-6BF96689A8-L000047](../../tests/test_research.py#L47) | 47 | `"            \"query\": \"cars Egypt\","` | — |
| [SRC-6BF96689A8-L000048](../../tests/test_research.py#L48) | 48 | `"            \"provider\": \"ddg\","` | — |
| [SRC-6BF96689A8-L000049](../../tests/test_research.py#L49) | 49 | `"            \"results\": ["` | — |
| [SRC-6BF96689A8-L000050](../../tests/test_research.py#L50) | 50 | `"                {\"title\": \"A\", \"url\": \"https://www.example.com/a?utm_source=x\", \"snippet\": \"A\"},"` | — |
| [SRC-6BF96689A8-L000051](../../tests/test_research.py#L51) | 51 | `"                {\"title\": \"B\", \"url\": \"https://example.com/b\", \"snippet\": \"B\"},"` | — |
| [SRC-6BF96689A8-L000052](../../tests/test_research.py#L52) | 52 | `"            ],"` | — |
| [SRC-6BF96689A8-L000053](../../tests/test_research.py#L53) | 53 | `"        },"` | — |
| [SRC-6BF96689A8-L000054](../../tests/test_research.py#L54) | 54 | `"        {"` | — |
| [SRC-6BF96689A8-L000055](../../tests/test_research.py#L55) | 55 | `"            \"query\": \"electric vehicles Egypt\","` | — |
| [SRC-6BF96689A8-L000056](../../tests/test_research.py#L56) | 56 | `"            \"provider\": \"bing\","` | — |
| [SRC-6BF96689A8-L000057](../../tests/test_research.py#L57) | 57 | `"            \"results\": ["` | — |
| [SRC-6BF96689A8-L000058](../../tests/test_research.py#L58) | 58 | `"                {\"title\": \"A better title\", \"url\": \"https://example.com/a\", \"snippet\": \"Longer evidence snippet\"},"` | — |
| [SRC-6BF96689A8-L000059](../../tests/test_research.py#L59) | 59 | `"                {\"title\": \"C\", \"url\": \"https://example.com/c\", \"snippet\": \"C\"},"` | — |
| [SRC-6BF96689A8-L000060](../../tests/test_research.py#L60) | 60 | `"            ],"` | — |
| [SRC-6BF96689A8-L000061](../../tests/test_research.py#L61) | 61 | `"        },"` | — |
| [SRC-6BF96689A8-L000062](../../tests/test_research.py#L62) | 62 | `"    ]"` | — |
| [SRC-6BF96689A8-L000063](../../tests/test_research.py#L63) | 63 | `"    ranked = fuse_ranked_results(batches)"` | — |
| [SRC-6BF96689A8-L000064](../../tests/test_research.py#L64) | 64 | `"    urls = [source[\"url\"] for source in ranked]"` | — |
| [SRC-6BF96689A8-L000065](../../tests/test_research.py#L65) | 65 | `"    assert len(urls) == 3"` | — |
| [SRC-6BF96689A8-L000066](../../tests/test_research.py#L66) | 66 | `"    source_a = next(source for source in ranked if \"example.com/a\" in source[\"url\"])"` | — |
| [SRC-6BF96689A8-L000067](../../tests/test_research.py#L67) | 67 | `"    assert len(source_a[\"providers\"]) == 2"` | — |
| [SRC-6BF96689A8-L000068](../../tests/test_research.py#L68) | 68 | `"    assert len(source_a[\"queries\"]) == 2"` | — |
| [SRC-6BF96689A8-L000069](../../tests/test_research.py#L69) | 69 | `"    assert source_a[\"rank_score\"] > next("` | — |
| [SRC-6BF96689A8-L000070](../../tests/test_research.py#L70) | 70 | `"        source[\"rank_score\"] for source in ranked if \"example.com/c\" in source[\"url\"]"` | — |
| [SRC-6BF96689A8-L000071](../../tests/test_research.py#L71) | 71 | `"    )"` | — |
| [SRC-6BF96689A8-L000072](../../tests/test_research.py#L72) | 72 | `""` | — |
| [SRC-6BF96689A8-L000073](../../tests/test_research.py#L73) | 73 | `""` | — |
| [SRC-6BF96689A8-L000074](../../tests/test_research.py#L74) | 74 | `"def test_source_classification_distinguishes_social_and_government():"` | — |
| [SRC-6BF96689A8-L000075](../../tests/test_research.py#L75) | 75 | `"    from agents.research import classify_source"` | — |
| [SRC-6BF96689A8-L000076](../../tests/test_research.py#L76) | 76 | `""` | — |
| [SRC-6BF96689A8-L000077](../../tests/test_research.py#L77) | 77 | `"    assert classify_source(\"https://www.reddit.com/r/example/comments/1\")[\"platform\"] == \"reddit\""` | — |
| [SRC-6BF96689A8-L000078](../../tests/test_research.py#L78) | 78 | `"    assert classify_source(\"https://example.gov.eg/page\")[\"source_class\"] == \"government\""` | — |
| [SRC-6BF96689A8-L000079](../../tests/test_research.py#L79) | 79 | `""` | — |
| [SRC-6BF96689A8-L000080](../../tests/test_research.py#L80) | 80 | `""` | — |
| [SRC-6BF96689A8-L000081](../../tests/test_research.py#L81) | 81 | `"def test_explicit_page_urls_are_extracted_and_not_left_in_search_terms():"` | — |
| [SRC-6BF96689A8-L000082](../../tests/test_research.py#L82) | 82 | `"    from agents.research import extract_urls"` | — |
| [SRC-6BF96689A8-L000083](../../tests/test_research.py#L83) | 83 | `""` | — |
| [SRC-6BF96689A8-L000084](../../tests/test_research.py#L84) | 84 | `"    question = \"حلل هذه الصفحة بالتفصيل https://example.com/a?utm_source=chat#section.\""` | — |
| [SRC-6BF96689A8-L000085](../../tests/test_research.py#L85) | 85 | `"    plan = fallback_plan(question)"` | — |
| [SRC-6BF96689A8-L000086](../../tests/test_research.py#L86) | 86 | `"    assert extract_urls(question) == [\"https://example.com/a?utm_source=chat#section\"]"` | — |
| [SRC-6BF96689A8-L000087](../../tests/test_research.py#L87) | 87 | `"    assert plan[\"direct_urls\"] == [\"https://example.com/a?utm_source=chat#section\"]"` | — |
| [SRC-6BF96689A8-L000088](../../tests/test_research.py#L88) | 88 | `"    assert \"https://\" not in plan[\"queries\"][0]"` | — |
| [SRC-6BF96689A8-L000089](../../tests/test_research.py#L89) | 89 | `""` | — |
| [SRC-6BF96689A8-L000090](../../tests/test_research.py#L90) | 90 | `"def test_registrable_domain_groups_subdomains_and_respects_public_suffixes():"` | — |
| [SRC-6BF96689A8-L000091](../../tests/test_research.py#L91) | 91 | `"    assert registrable_domain(\"news.example.com\") == \"example.com\""` | — |
| [SRC-6BF96689A8-L000092](../../tests/test_research.py#L92) | 92 | `"    assert registrable_domain(\"offers.example.com\") == \"example.com\""` | — |
| [SRC-6BF96689A8-L000093](../../tests/test_research.py#L93) | 93 | `"    assert registrable_domain(\"news.example.co.uk\") == \"example.co.uk\""` | — |
| [SRC-6BF96689A8-L000094](../../tests/test_research.py#L94) | 94 | `"    assert registrable_domain(\"other.co.uk\") == \"other.co.uk\""` | — |
| [SRC-6BF96689A8-L000095](../../tests/test_research.py#L95) | 95 | `"    assert registrable_domain(\"alice.github.io\") == \"alice.github.io\""` | — |
| [SRC-6BF96689A8-L000096](../../tests/test_research.py#L96) | 96 | `"    assert registrable_domain(\"https://www.example.com/path\") == \"example.com\""` | — |
| [SRC-6BF96689A8-L000097](../../tests/test_research.py#L97) | 97 | `""` | — |
| [SRC-6BF96689A8-L000098](../../tests/test_research.py#L98) | 98 | `""` | — |
| [SRC-6BF96689A8-L000099](../../tests/test_research.py#L99) | 99 | `"def test_evidence_coverage_does_not_count_sibling_subdomains_as_independent():"` | — |
| [SRC-6BF96689A8-L000100](../../tests/test_research.py#L100) | 100 | `"    report = evidence_signal_report(["` | — |
| [SRC-6BF96689A8-L000101](../../tests/test_research.py#L101) | 101 | `"        {"` | — |
| [SRC-6BF96689A8-L000102](../../tests/test_research.py#L102) | 102 | `"            \"url\": \"https://news.example.com/story\","` | — |
| [SRC-6BF96689A8-L000103](../../tests/test_research.py#L103) | 103 | `"            \"domain\": \"news.example.com\","` | — |
| [SRC-6BF96689A8-L000104](../../tests/test_research.py#L104) | 104 | `"            \"providers\": [\"search_a\"],"` | — |
| [SRC-6BF96689A8-L000105](../../tests/test_research.py#L105) | 105 | `"        },"` | — |
| [SRC-6BF96689A8-L000106](../../tests/test_research.py#L106) | 106 | `"        {"` | — |
| [SRC-6BF96689A8-L000107](../../tests/test_research.py#L107) | 107 | `"            \"url\": \"https://offers.example.com/second-story\","` | — |
| [SRC-6BF96689A8-L000108](../../tests/test_research.py#L108) | 108 | `"            \"domain\": \"offers.example.com\","` | — |
| [SRC-6BF96689A8-L000109](../../tests/test_research.py#L109) | 109 | `"            \"providers\": [\"search_b\"],"` | — |
| [SRC-6BF96689A8-L000110](../../tests/test_research.py#L110) | 110 | `"        },"` | — |
| [SRC-6BF96689A8-L000111](../../tests/test_research.py#L111) | 111 | `"    ])"` | — |
| [SRC-6BF96689A8-L000112](../../tests/test_research.py#L112) | 112 | `"    assert report[\"unique_domains\"] == 1"` | — |
| [SRC-6BF96689A8-L000113](../../tests/test_research.py#L113) | 113 | `"    assert report[\"coverage_level\"] == \"محدود\""` | — |
| [SRC-6BF96689A8-L000114](../../tests/test_research.py#L114) | 114 | `""` | — |
| [SRC-6BF96689A8-L000115](../../tests/test_research.py#L115) | 115 | `""` | — |
| [SRC-6BF96689A8-L000116](../../tests/test_research.py#L116) | 116 | `""` | — |
| [SRC-6BF96689A8-L000117](../../tests/test_research.py#L117) | 117 | `"def test_standard_fallback_plan_does_not_add_deep_research_query():"` | — |
| [SRC-6BF96689A8-L000118](../../tests/test_research.py#L118) | 118 | `"    plan = fallback_plan(\"اشرح طريقة عمل المحرك الكهربائي\")"` | — |
| [SRC-6BF96689A8-L000119](../../tests/test_research.py#L119) | 119 | `"    assert plan[\"depth\"] == \"standard\""` | — |
| [SRC-6BF96689A8-L000120](../../tests/test_research.py#L120) | 120 | `"    assert not any(\"مصادر موثوقة تقارير إحصاءات\" in query for query in plan[\"queries\"])"` | — |
| [SRC-6BF96689A8-L000121](../../tests/test_research.py#L121) | 121 | `""` | — |
| [SRC-6BF96689A8-L000122](../../tests/test_research.py#L122) | 122 | `""` | — |
| [SRC-6BF96689A8-L000123](../../tests/test_research.py#L123) | 123 | `"def test_deep_fallback_plan_adds_deep_research_query_for_explicit_comparison():"` | — |
| [SRC-6BF96689A8-L000124](../../tests/test_research.py#L124) | 124 | `"    plan = fallback_plan(\"قارن مميزات وعيوب المحرك الكهربائي\")"` | — |
| [SRC-6BF96689A8-L000125](../../tests/test_research.py#L125) | 125 | `"    assert plan[\"depth\"] == \"deep\""` | — |
| [SRC-6BF96689A8-L000126](../../tests/test_research.py#L126) | 126 | `"    assert any(\"مصادر موثوقة تقارير إحصاءات\" in query for query in plan[\"queries\"])"` | — |
| [SRC-6BF96689A8-L000127](../../tests/test_research.py#L127) | 127 | `""` | — |
| [SRC-6BF96689A8-L000128](../../tests/test_research.py#L128) | 128 | `""` | — |
| [SRC-6BF96689A8-L000129](../../tests/test_research.py#L129) | 129 | `"def test_fallback_plan_expands_warranty_followup_with_previous_topic():"` | — |
| [SRC-6BF96689A8-L000130](../../tests/test_research.py#L130) | 130 | `"    history = ["` | — |
| [SRC-6BF96689A8-L000131](../../tests/test_research.py#L131) | 131 | `"        {\"role\": \"user\", \"content\": \"سعر آيفون 16 في مصر\"},"` | — |
| [SRC-6BF96689A8-L000132](../../tests/test_research.py#L132) | 132 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن معلومات حديثة.\"},"` | — |
| [SRC-6BF96689A8-L000133](../../tests/test_research.py#L133) | 133 | `"    ]"` | — |
| [SRC-6BF96689A8-L000134](../../tests/test_research.py#L134) | 134 | `"    plan = fallback_plan(\"هل فيه ضمان؟\", history)"` | — |
| [SRC-6BF96689A8-L000135](../../tests/test_research.py#L135) | 135 | `"    assert \"آيفون 16\" in plan[\"queries\"][0]"` | — |
| [SRC-6BF96689A8-L000136](../../tests/test_research.py#L136) | 136 | `"    assert \"ضمان\" in plan[\"queries\"][0]"` | — |
| [SRC-6BF96689A8-L000137](../../tests/test_research.py#L137) | 137 | `""` | — |
| [SRC-6BF96689A8-L000138](../../tests/test_research.py#L138) | 138 | `""` | — |
| [SRC-6BF96689A8-L000139](../../tests/test_research.py#L139) | 139 | `"def test_fallback_plan_does_not_reuse_topic_after_acknowledgment():"` | — |
| [SRC-6BF96689A8-L000140](../../tests/test_research.py#L140) | 140 | `"    history = ["` | — |
| [SRC-6BF96689A8-L000141](../../tests/test_research.py#L141) | 141 | `"        {\"role\": \"user\", \"content\": \"سعر آيفون 16 في مصر\"},"` | — |
| [SRC-6BF96689A8-L000142](../../tests/test_research.py#L142) | 142 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن معلومات حديثة.\"},"` | — |
| [SRC-6BF96689A8-L000143](../../tests/test_research.py#L143) | 143 | `"        {\"role\": \"user\", \"content\": \"شكرًا\"},"` | — |
| [SRC-6BF96689A8-L000144](../../tests/test_research.py#L144) | 144 | `"        {\"role\": \"assistant\", \"content\": \"العفو.\"},"` | — |
| [SRC-6BF96689A8-L000145](../../tests/test_research.py#L145) | 145 | `"    ]"` | — |
| [SRC-6BF96689A8-L000146](../../tests/test_research.py#L146) | 146 | `"    plan = fallback_plan(\"فين؟\", history)"` | — |
| [SRC-6BF96689A8-L000147](../../tests/test_research.py#L147) | 147 | `"    assert \"آيفون 16\" not in plan[\"queries\"][0]"` | — |
| [SRC-6BF96689A8-L000148](../../tests/test_research.py#L148) | 148 | `""` | — |
| [SRC-6BF96689A8-L000149](../../tests/test_research.py#L149) | 149 | `""` | — |
| [SRC-6BF96689A8-L000150](../../tests/test_research.py#L150) | 150 | `"def test_compact_search_query_keeps_subject_and_removes_answer_format_instructions():"` | — |
| [SRC-6BF96689A8-L000151](../../tests/test_research.py#L151) | 151 | `"    cases = ["` | — |
| [SRC-6BF96689A8-L000152](../../tests/test_research.py#L152) | 152 | `"        ("` | — |
| [SRC-6BF96689A8-L000153](../../tests/test_research.py#L153) | 153 | `"            \"ما عاصمة مصر؟ اذكر مصدرًا موثوقًا مع رابط مباشر، وأجب بالعربية بإيجاز.\","` | — |
| [SRC-6BF96689A8-L000154](../../tests/test_research.py#L154) | 154 | `"            (\"عاصمة مصر\",),"` | — |
| [SRC-6BF96689A8-L000155](../../tests/test_research.py#L155) | 155 | `"            (\"اذكر مصدرًا موثوقًا\", \"رابط مباشر\", \"بالعربية بإيجاز\"),"` | — |
| [SRC-6BF96689A8-L000156](../../tests/test_research.py#L156) | 156 | `"        ),"` | — |
| [SRC-6BF96689A8-L000157](../../tests/test_research.py#L157) | 157 | `"        ("` | — |
| [SRC-6BF96689A8-L000158](../../tests/test_research.py#L158) | 158 | `"            \"حلل أهم التحديات التي تواجه السيارات الكهربائية في مصر، وقارن بين التكلفة والبنية التحتية والشحن. استخدم مصادر متعددة، وميز بين الحقائق والاستنتاجات، واذكر روابط المصادر.\","` | — |
| [SRC-6BF96689A8-L000159](../../tests/test_research.py#L159) | 159 | `"            (\"السيارات الكهربائية\", \"مصر\", \"التكلفة\", \"البنية التحتية\", \"الشحن\"),"` | — |
| [SRC-6BF96689A8-L000160](../../tests/test_research.py#L160) | 160 | `"            (\"استخدم مصادر متعددة\", \"الحقائق والاستنتاجات\", \"روابط المصادر\"),"` | — |
| [SRC-6BF96689A8-L000161](../../tests/test_research.py#L161) | 161 | `"        ),"` | — |
| [SRC-6BF96689A8-L000162](../../tests/test_research.py#L162) | 162 | `"        ("` | — |
| [SRC-6BF96689A8-L000163](../../tests/test_research.py#L163) | 163 | `"            \"ما أحدث التطورات في وكلاء الذكاء الاصطناعي خلال الأيام السبعة الماضية؟ اذكر تواريخ الأخبار وروابط المصادر، ولا تعرض معلومات قديمة باعتبارها جديدة.\","` | — |
| [SRC-6BF96689A8-L000164](../../tests/test_research.py#L164) | 164 | `"            (\"وكلاء الذكاء الاصطناعي\", \"الأيام السبعة الماضية\"),"` | — |
| [SRC-6BF96689A8-L000165](../../tests/test_research.py#L165) | 165 | `"            (\"تواريخ الأخبار\", \"روابط المصادر\", \"معلومات قديمة\"),"` | — |
| [SRC-6BF96689A8-L000166](../../tests/test_research.py#L166) | 166 | `"        ),"` | — |
| [SRC-6BF96689A8-L000167](../../tests/test_research.py#L167) | 167 | `"        ("` | — |
| [SRC-6BF96689A8-L000168](../../tests/test_research.py#L168) | 168 | `"            \"اجمع آراء وتجارب المستخدمين العامة حول السيارات الكهربائية في مصر. اعرض الآراء الإيجابية والسلبية، واذكر روابط المنشورات أو المصادر المتاحة. وضح إذا كانت النتائج غير كافية لتمثيل آراء المستخدمين عمومًا.\","` | — |
| [SRC-6BF96689A8-L000169](../../tests/test_research.py#L169) | 169 | `"            (\"آراء وتجارب المستخدمين\", \"السيارات الكهربائية في مصر\", \"الإيجابية والسلبية\"),"` | — |
| [SRC-6BF96689A8-L000170](../../tests/test_research.py#L170) | 170 | `"            (\"روابط المنشورات\", \"النتائج غير كافية\", \"تمثيل آراء المستخدمين عمومًا\"),"` | — |
| [SRC-6BF96689A8-L000171](../../tests/test_research.py#L171) | 171 | `"        ),"` | — |
| [SRC-6BF96689A8-L000172](../../tests/test_research.py#L172) | 172 | `"    ]"` | — |
| [SRC-6BF96689A8-L000173](../../tests/test_research.py#L173) | 173 | `"    for question, required_terms, removed_terms in cases:"` | — |
| [SRC-6BF96689A8-L000174](../../tests/test_research.py#L174) | 174 | `"        query = compact_search_query(question)"` | — |
| [SRC-6BF96689A8-L000175](../../tests/test_research.py#L175) | 175 | `"        assert 2 <= len(query) <= 240"` | — |
| [SRC-6BF96689A8-L000176](../../tests/test_research.py#L176) | 176 | `"        for term in required_terms:"` | — |
| [SRC-6BF96689A8-L000177](../../tests/test_research.py#L177) | 177 | `"            assert term in query, f\"topic term was lost: {term!r} in {query!r}\""` | — |
| [SRC-6BF96689A8-L000178](../../tests/test_research.py#L178) | 178 | `"        for term in removed_terms:"` | — |
| [SRC-6BF96689A8-L000179](../../tests/test_research.py#L179) | 179 | `"            assert term not in query, f\"format instruction remains: {term!r} in {query!r}\""` | — |
| [SRC-6BF96689A8-L000180](../../tests/test_research.py#L180) | 180 | `""` | — |
| [SRC-6BF96689A8-L000181](../../tests/test_research.py#L181) | 181 | `""` | — |
| [SRC-6BF96689A8-L000182](../../tests/test_research.py#L182) | 182 | `"def test_fallback_plan_compacts_four_representative_arabic_tasks_before_expansion():"` | — |
| [SRC-6BF96689A8-L000183](../../tests/test_research.py#L183) | 183 | `"    questions = ["` | — |
| [SRC-6BF96689A8-L000184](../../tests/test_research.py#L184) | 184 | `"        \"ما عاصمة مصر؟ اذكر مصدرًا موثوقًا مع رابط مباشر، وأجب بالعربية بإيجاز.\","` | — |
| [SRC-6BF96689A8-L000185](../../tests/test_research.py#L185) | 185 | `"        \"حلل أهم التحديات التي تواجه السيارات الكهربائية في مصر، وقارن بين التكلفة والبنية التحتية والشحن. استخدم مصادر متعددة، وميز بين الحقائق والاستنتاجات، واذكر روابط المصادر.\","` | — |
| [SRC-6BF96689A8-L000186](../../tests/test_research.py#L186) | 186 | `"        \"ما أحدث التطورات في وكلاء الذكاء الاصطناعي خلال الأيام السبعة الماضية؟ اذكر تواريخ الأخبار وروابط المصادر، ولا تعرض معلومات قديمة باعتبارها جديدة.\","` | — |
| [SRC-6BF96689A8-L000187](../../tests/test_research.py#L187) | 187 | `"        \"اجمع آراء وتجارب المستخدمين العامة حول السيارات الكهربائية في مصر. اعرض الآراء الإيجابية والسلبية، واذكر روابط المنشورات أو المصادر المتاحة. وضح إذا كانت النتائج غير كافية لتمثيل آراء المستخدمين عمومًا.\","` | — |
| [SRC-6BF96689A8-L000188](../../tests/test_research.py#L188) | 188 | `"    ]"` | — |
| [SRC-6BF96689A8-L000189](../../tests/test_research.py#L189) | 189 | `"    for question in questions:"` | — |
| [SRC-6BF96689A8-L000190](../../tests/test_research.py#L190) | 190 | `"        plan = fallback_plan(question)"` | — |
| [SRC-6BF96689A8-L000191](../../tests/test_research.py#L191) | 191 | `"        assert plan[\"queries\"]"` | — |
| [SRC-6BF96689A8-L000192](../../tests/test_research.py#L192) | 192 | `"        assert all(2 <= len(query) <= 240 for query in plan[\"queries\"])"` | — |
| [SRC-6BF96689A8-L000193](../../tests/test_research.py#L193) | 193 | `""` | — |
| [SRC-6BF96689A8-L000194](../../tests/test_research.py#L194) | 194 | `""` | — |
| [SRC-6BF96689A8-L000195](../../tests/test_research.py#L195) | 195 | `"def test_compact_search_query_preserves_site_operator_and_discards_separate_citation_instruction():"` | — |
| [SRC-6BF96689A8-L000196](../../tests/test_research.py#L196) | 196 | `"    query = compact_search_query("` | — |
| [SRC-6BF96689A8-L000197](../../tests/test_research.py#L197) | 197 | `"        'site:reddit.com electric car reviews Egypt. Cite the original posts and provide links.'"` | — |
| [SRC-6BF96689A8-L000198](../../tests/test_research.py#L198) | 198 | `"    )"` | — |
| [SRC-6BF96689A8-L000199](../../tests/test_research.py#L199) | 199 | `"    assert query.startswith(\"site:reddit.com\")"` | — |
| [SRC-6BF96689A8-L000200](../../tests/test_research.py#L200) | 200 | `"    assert \"electric car reviews Egypt\" in query"` | — |
| [SRC-6BF96689A8-L000201](../../tests/test_research.py#L201) | 201 | `"    assert \"Cite the original posts\" not in query"` | — |
| [SRC-6BF96689A8-L000202](../../tests/test_research.py#L202) | 202 | `"    assert len(query) <= 240"` | — |
| [SRC-6BF96689A8-L000203](../../tests/test_research.py#L203) | 203 | `""` | — |
| [SRC-6BF96689A8-L000204](../../tests/test_research.py#L204) | 204 | `""` | — |
| [SRC-6BF96689A8-L000205](../../tests/test_research.py#L205) | 205 | `"def test_compact_search_query_bounds_length_without_leaving_partial_tail_word():"` | — |
| [SRC-6BF96689A8-L000206](../../tests/test_research.py#L206) | 206 | `"    query = compact_search_query("` | — |
| [SRC-6BF96689A8-L000207](../../tests/test_research.py#L207) | 207 | `"        \"Electric vehicles in Egypt charging infrastructure costs and ownership experiences\","` | — |
| [SRC-6BF96689A8-L000208](../../tests/test_research.py#L208) | 208 | `"        limit=42,"` | — |
| [SRC-6BF96689A8-L000209](../../tests/test_research.py#L209) | 209 | `"    )"` | — |
| [SRC-6BF96689A8-L000210](../../tests/test_research.py#L210) | 210 | `"    assert len(query) <= 42"` | — |
| [SRC-6BF96689A8-L000211](../../tests/test_research.py#L211) | 211 | `"    assert not query.endswith(\"infrastructur\")"` | — |
| [SRC-6BF96689A8-L000212](../../tests/test_research.py#L212) | 212 | `""` | — |
| [SRC-6BF96689A8-L000213](../../tests/test_research.py#L213) | 213 | `""` | — |
| [SRC-6BF96689A8-L000214](../../tests/test_research.py#L214) | 214 | `"def test_compact_search_query_preserves_subject_when_prompt_starts_with_action_verb():"` | — |
| [SRC-6BF96689A8-L000215](../../tests/test_research.py#L215) | 215 | `"    query = compact_search_query("` | — |
| [SRC-6BF96689A8-L000216](../../tests/test_research.py#L216) | 216 | `"        \"وضح أهمية السيارات الكهربائية في مصر. ما تأثير الشحن على المدى الطويل؟ اذكر مصادر موثوقة.\""` | — |
| [SRC-6BF96689A8-L000217](../../tests/test_research.py#L217) | 217 | `"    )"` | — |
| [SRC-6BF96689A8-L000218](../../tests/test_research.py#L218) | 218 | `"    assert \"السيارات الكهربائية في مصر\" in query"` | — |
| [SRC-6BF96689A8-L000219](../../tests/test_research.py#L219) | 219 | `"    assert \"الشحن على المدى الطويل\" in query"` | — |
| [SRC-6BF96689A8-L000220](../../tests/test_research.py#L220) | 220 | `"    assert \"مصادر موثوقة\" not in query"` | — |
| [SRC-6BF96689A8-L000221](../../tests/test_research.py#L221) | 221 | `""` | — |
| [SRC-6BF96689A8-L000222](../../tests/test_research.py#L222) | 222 | `"    query = compact_search_query("` | — |
| [SRC-6BF96689A8-L000223](../../tests/test_research.py#L223) | 223 | `"        \"اذكر أبرز السيارات الكهربائية في مصر. قارن بين أسعارها.\""` | — |
| [SRC-6BF96689A8-L000224](../../tests/test_research.py#L224) | 224 | `"    )"` | — |
| [SRC-6BF96689A8-L000225](../../tests/test_research.py#L225) | 225 | `"    assert \"السيارات الكهربائية في مصر\" in query"` | — |
| [SRC-6BF96689A8-L000226](../../tests/test_research.py#L226) | 226 | `"    assert \"أسعارها\" in query"` | — |
| [SRC-6BF96689A8-L000227](../../tests/test_research.py#L227) | 227 | `"    assert \"اذكر أبرز\" not in query"` | — |
| [SRC-6BF96689A8-L000228](../../tests/test_research.py#L228) | 228 | `""` | — |
| [SRC-6BF96689A8-L000229](../../tests/test_research.py#L229) | 229 | `""` | — |
| [SRC-6BF96689A8-L000230](../../tests/test_research.py#L230) | 230 | `""` | — |
| [SRC-6BF96689A8-L000231](../../tests/test_research.py#L231) | 231 | `"def test_compact_search_query_returns_empty_for_instruction_only_request():"` | — |
| [SRC-6BF96689A8-L000232](../../tests/test_research.py#L232) | 232 | `"    query = compact_search_query(\"اذكر مصادر موثوقة، روابط مباشرة، باختصار\")"` | — |
| [SRC-6BF96689A8-L000233](../../tests/test_research.py#L233) | 233 | `"    assert query == \"\""` | — |
| [SRC-6BF96689A8-L000234](../../tests/test_research.py#L234) | 234 | `""` | — |
| [SRC-6BF96689A8-L000235](../../tests/test_research.py#L235) | 235 | `""` | — |
| [SRC-6BF96689A8-L000236](../../tests/test_research.py#L236) | 236 | `"def test_compact_search_query_removes_diacritic_uncertainty_instruction():"` | — |
| [SRC-6BF96689A8-L000237](../../tests/test_research.py#L237) | 237 | `"    question = ("` | — |
| [SRC-6BF96689A8-L000238](../../tests/test_research.py#L238) | 238 | `"        \"اجمع آراء العملاء عن السيارات الكهربائية. \""` | — |
| [SRC-6BF96689A8-L000239](../../tests/test_research.py#L239) | 239 | `"        \"وَضِّحْ إِذَا كَانَتِ النَّتَائِجُ غَيْرَ كَافِيَةٍ \""` | — |
| [SRC-6BF96689A8-L000240](../../tests/test_research.py#L240) | 240 | `"        \"لِتَمْثِيلِ آراء المستخدمين عمومًا.\""` | — |
| [SRC-6BF96689A8-L000241](../../tests/test_research.py#L241) | 241 | `"    )"` | — |
| [SRC-6BF96689A8-L000242](../../tests/test_research.py#L242) | 242 | `"    query = compact_search_query(question)"` | — |
| [SRC-6BF96689A8-L000243](../../tests/test_research.py#L243) | 243 | `"    assert \"السيارات الكهربائية\" in query"` | — |
| [SRC-6BF96689A8-L000244](../../tests/test_research.py#L244) | 244 | `"    assert \"النتائج\" not in query"` | — |
| [SRC-6BF96689A8-L000245](../../tests/test_research.py#L245) | 245 | `"    assert \"تمثيل آراء المستخدمين\" not in query"` | — |
| [SRC-6BF96689A8-L000246](../../tests/test_research.py#L246) | 246 | `""` | — |
| [SRC-6BF96689A8-L000247](../../tests/test_research.py#L247) | 247 | `""` | — |
| [SRC-6BF96689A8-L000248](../../tests/test_research.py#L248) | 248 | `"def test_compact_search_query_preserves_topic_after_source_quality_lead_in():"` | — |
| [SRC-6BF96689A8-L000249](../../tests/test_research.py#L249) | 249 | `"    cases = ("` | — |
| [SRC-6BF96689A8-L000250](../../tests/test_research.py#L250) | 250 | `"        ("` | — |
| [SRC-6BF96689A8-L000251](../../tests/test_research.py#L251) | 251 | `"            \"استخدم مصادر متعددة للبحث عن السيارات الكهربائية في مصر\","` | — |
| [SRC-6BF96689A8-L000252](../../tests/test_research.py#L252) | 252 | `"            (\"السيارات الكهربائية\", \"مصر\"),"` | — |
| [SRC-6BF96689A8-L000253](../../tests/test_research.py#L253) | 253 | `"        ),"` | — |
| [SRC-6BF96689A8-L000254](../../tests/test_research.py#L254) | 254 | `"        ("` | — |
| [SRC-6BF96689A8-L000255](../../tests/test_research.py#L255) | 255 | `"            \"Use multiple sources to research electric vehicle charging in Egypt\","` | — |
| [SRC-6BF96689A8-L000256](../../tests/test_research.py#L256) | 256 | `"            (\"electric vehicle charging\", \"Egypt\"),"` | — |
| [SRC-6BF96689A8-L000257](../../tests/test_research.py#L257) | 257 | `"        ),"` | — |
| [SRC-6BF96689A8-L000258](../../tests/test_research.py#L258) | 258 | `"    )"` | — |
| [SRC-6BF96689A8-L000259](../../tests/test_research.py#L259) | 259 | `"    for question, required_terms in cases:"` | — |
| [SRC-6BF96689A8-L000260](../../tests/test_research.py#L260) | 260 | `"        query = compact_search_query(question)"` | — |
| [SRC-6BF96689A8-L000261](../../tests/test_research.py#L261) | 261 | `"        assert query"` | — |
| [SRC-6BF96689A8-L000262](../../tests/test_research.py#L262) | 262 | `"        for term in required_terms:"` | — |
| [SRC-6BF96689A8-L000263](../../tests/test_research.py#L263) | 263 | `"            assert term in query, f\"lost topic term {term!r}: {query!r}\""` | — |
| [SRC-6BF96689A8-L000264](../../tests/test_research.py#L264) | 264 | `""` | — |
| [SRC-6BF96689A8-L000265](../../tests/test_research.py#L265) | 265 | `""` | — |
| [SRC-6BF96689A8-L000266](../../tests/test_research.py#L266) | 266 | `"def test_compact_search_query_preserves_topic_after_distinguish_action():"` | — |
| [SRC-6BF96689A8-L000267](../../tests/test_research.py#L267) | 267 | `"    query = compact_search_query(\"ميّز بين السيارات الكهربائية وسيارات البنزين في مصر\")"` | — |
| [SRC-6BF96689A8-L000268](../../tests/test_research.py#L268) | 268 | `"    assert \"السيارات الكهربائية\" in query"` | — |
| [SRC-6BF96689A8-L000269](../../tests/test_research.py#L269) | 269 | `"    assert \"سيارات البنزين\" in query"` | — |
| [SRC-6BF96689A8-L000270](../../tests/test_research.py#L270) | 270 | `"    assert \"مصر\" in query"` | — |
| [SRC-6BF96689A8-L000271](../../tests/test_research.py#L271) | 271 | `""` | — |
| [SRC-6BF96689A8-L000272](../../tests/test_research.py#L272) | 272 | `""` | — |
| [SRC-6BF96689A8-L000273](../../tests/test_research.py#L273) | 273 | `"def test_compact_search_query_discards_standalone_fact_vs_inference_instruction():"` | — |
| [SRC-6BF96689A8-L000274](../../tests/test_research.py#L274) | 274 | `"    assert compact_search_query(\"ميّز بين الحقائق والاستنتاجات.\") == \"\""` | — |
| [SRC-6BF96689A8-L000275](../../tests/test_research.py#L275) | 275 | `""` | — |
| [SRC-6BF96689A8-L000276](../../tests/test_research.py#L276) | 276 | `""` | — |
| [SRC-6BF96689A8-L000277](../../tests/test_research.py#L277) | 277 | `"def test_fallback_plan_does_not_invent_query_for_instruction_only_prompt():"` | — |
| [SRC-6BF96689A8-L000278](../../tests/test_research.py#L278) | 278 | `"    plan = fallback_plan(\"اذكر مصادر موثوقة، روابط مباشرة، باختصار\")"` | — |
| [SRC-6BF96689A8-L000279](../../tests/test_research.py#L279) | 279 | `"    assert plan[\"queries\"] == []"` | — |
| [SRC-6BF96689A8-L000280](../../tests/test_research.py#L280) | 280 | `""` | — |
| [SRC-6BF96689A8-L000281](../../tests/test_research.py#L281) | 281 | `""` | — |
| [SRC-6BF96689A8-L000282](../../tests/test_research.py#L282) | 282 | `"def test_collect_research_compacts_queries_before_provider_calls(monkeypatch):"` | — |
| [SRC-6BF96689A8-L000283](../../tests/test_research.py#L283) | 283 | `"    from agents.web_agent import WebAgent"` | — |
| [SRC-6BF96689A8-L000284](../../tests/test_research.py#L284) | 284 | `""` | — |
| [SRC-6BF96689A8-L000285](../../tests/test_research.py#L285) | 285 | `"    agent = WebAgent()"` | — |
| [SRC-6BF96689A8-L000286](../../tests/test_research.py#L286) | 286 | `"    seen = []"` | — |
| [SRC-6BF96689A8-L000287](../../tests/test_research.py#L287) | 287 | `"    monkeypatch.setattr(agent, \"_search_web\", lambda query: seen.append(query) or [])"` | — |
| [SRC-6BF96689A8-L000288](../../tests/test_research.py#L288) | 288 | `"    sources, _warnings, report = agent._collect_research({"` | — |
| [SRC-6BF96689A8-L000289](../../tests/test_research.py#L289) | 289 | `"        \"queries\": ["` | — |
| [SRC-6BF96689A8-L000290](../../tests/test_research.py#L290) | 290 | `"            \"ما عاصمة مصر؟ اذكر مصدرًا موثوقًا مع رابط مباشر، وأجب بالعربية بإيجاز.\""` | — |
| [SRC-6BF96689A8-L000291](../../tests/test_research.py#L291) | 291 | `"        ],"` | — |
| [SRC-6BF96689A8-L000292](../../tests/test_research.py#L292) | 292 | `"        \"direct_urls\": [],"` | — |
| [SRC-6BF96689A8-L000293](../../tests/test_research.py#L293) | 293 | `"        \"social_focus\": False,"` | — |
| [SRC-6BF96689A8-L000294](../../tests/test_research.py#L294) | 294 | `"        \"freshness\": \"any\","` | — |
| [SRC-6BF96689A8-L000295](../../tests/test_research.py#L295) | 295 | `"        \"depth\": \"standard\","` | — |
| [SRC-6BF96689A8-L000296](../../tests/test_research.py#L296) | 296 | `"        \"platforms\": [],"` | — |
| [SRC-6BF96689A8-L000297](../../tests/test_research.py#L297) | 297 | `"    })"` | — |
| [SRC-6BF96689A8-L000298](../../tests/test_research.py#L298) | 298 | `""` | — |
| [SRC-6BF96689A8-L000299](../../tests/test_research.py#L299) | 299 | `"    assert sources == []"` | — |
| [SRC-6BF96689A8-L000300](../../tests/test_research.py#L300) | 300 | `"    assert seen == [\"ما عاصمة مصر؟\"]"` | — |
| [SRC-6BF96689A8-L000301](../../tests/test_research.py#L301) | 301 | `"    assert report[\"queries_planned\"] == 1"` | — |
| [SRC-6BF96689A8-L000302](../../tests/test_research.py#L302) | 302 | `"    assert report[\"queries_attempted\"] == 1"` | — |
| [SRC-6BF96689A8-L000303](../../tests/test_research.py#L303) | 303 | `""` | — |
| [SRC-6BF96689A8-L000304](../../tests/test_research.py#L304) | 304 | `""` | — |
| [SRC-6BF96689A8-L000305](../../tests/test_research.py#L305) | 305 | `"def test_collect_research_skips_provider_calls_without_topic_or_direct_url(monkeypatch):"` | — |
| [SRC-6BF96689A8-L000306](../../tests/test_research.py#L306) | 306 | `"    from agents.web_agent import WebAgent"` | — |
| [SRC-6BF96689A8-L000307](../../tests/test_research.py#L307) | 307 | `""` | — |
| [SRC-6BF96689A8-L000308](../../tests/test_research.py#L308) | 308 | `"    agent = WebAgent()"` | — |
| [SRC-6BF96689A8-L000309](../../tests/test_research.py#L309) | 309 | `"    seen = []"` | — |
| [SRC-6BF96689A8-L000310](../../tests/test_research.py#L310) | 310 | `"    monkeypatch.setattr(agent, \"_search_web\", lambda query: seen.append(query) or [])"` | — |
| [SRC-6BF96689A8-L000311](../../tests/test_research.py#L311) | 311 | `"    sources, warnings, report = agent._collect_research({"` | — |
| [SRC-6BF96689A8-L000312](../../tests/test_research.py#L312) | 312 | `"        \"queries\": [\"اذكر مصادر موثوقة، روابط مباشرة، باختصار\"],"` | — |
| [SRC-6BF96689A8-L000313](../../tests/test_research.py#L313) | 313 | `"        \"direct_urls\": [],"` | — |
| [SRC-6BF96689A8-L000314](../../tests/test_research.py#L314) | 314 | `"        \"social_focus\": False,"` | — |
| [SRC-6BF96689A8-L000315](../../tests/test_research.py#L315) | 315 | `"        \"freshness\": \"any\","` | — |
| [SRC-6BF96689A8-L000316](../../tests/test_research.py#L316) | 316 | `"        \"depth\": \"standard\","` | — |
| [SRC-6BF96689A8-L000317](../../tests/test_research.py#L317) | 317 | `"        \"platforms\": [],"` | — |
| [SRC-6BF96689A8-L000318](../../tests/test_research.py#L318) | 318 | `"    })"` | — |
| [SRC-6BF96689A8-L000319](../../tests/test_research.py#L319) | 319 | `""` | — |
| [SRC-6BF96689A8-L000320](../../tests/test_research.py#L320) | 320 | `"    assert sources == []"` | — |
| [SRC-6BF96689A8-L000321](../../tests/test_research.py#L321) | 321 | `"    assert report[\"queries_planned\"] == 0"` | — |
| [SRC-6BF96689A8-L000322](../../tests/test_research.py#L322) | 322 | `"    assert report[\"queries_attempted\"] == 0"` | — |
| [SRC-6BF96689A8-L000323](../../tests/test_research.py#L323) | 323 | `"    assert seen == []"` | — |
| [SRC-6BF96689A8-L000324](../../tests/test_research.py#L324) | 324 | `"    assert any(\"لم تُستدعَ محركات البحث\" in warning for warning in warnings)"` | — |
| [SRC-6BF96689A8-L000325](../../tests/test_research.py#L325) | 325 | `""` | — |
| [SRC-6BF96689A8-L000326](../../tests/test_research.py#L326) | 326 | `""` | — |
| [SRC-6BF96689A8-L000327](../../tests/test_research.py#L327) | 327 | `"def test_fallback_plan_keeps_direct_url_without_generic_keyword_query():"` | — |
| [SRC-6BF96689A8-L000328](../../tests/test_research.py#L328) | 328 | `"    plan = fallback_plan(\"https://example.com/research\")"` | — |
| [SRC-6BF96689A8-L000329](../../tests/test_research.py#L329) | 329 | `"    assert plan[\"direct_urls\"] == [\"https://example.com/research\"]"` | — |
| [SRC-6BF96689A8-L000330](../../tests/test_research.py#L330) | 330 | `"    assert plan[\"queries\"] == []"` | — |
| [SRC-6BF96689A8-L000331](../../tests/test_research.py#L331) | 331 | `""` | — |
| [SRC-6BF96689A8-L000332](../../tests/test_research.py#L332) | 332 | `""` | — |
| [SRC-6BF96689A8-L000333](../../tests/test_research.py#L333) | 333 | `""` | — |
| [SRC-6BF96689A8-L000334](../../tests/test_research.py#L334) | 334 | `"def test_followup_plan_keeps_topic_across_chained_turns():"` | — |
| [SRC-6BF96689A8-L000335](../../tests/test_research.py#L335) | 335 | `"    history = ["` | — |
| [SRC-6BF96689A8-L000336](../../tests/test_research.py#L336) | 336 | `"        {\"role\": \"user\", \"content\": \"ما سعر iPhone 16 في مصر؟\"},"` | — |
| [SRC-6BF96689A8-L000337](../../tests/test_research.py#L337) | 337 | `"        {\"role\": \"assistant\", \"content\": \"السعر يختلف حسب المتجر.\"},"` | — |
| [SRC-6BF96689A8-L000338](../../tests/test_research.py#L338) | 338 | `"        {\"role\": \"user\", \"content\": \"والضمان؟\"},"` | — |
| [SRC-6BF96689A8-L000339](../../tests/test_research.py#L339) | 339 | `"        {\"role\": \"assistant\", \"content\": \"سأوضح الضمان.\"},"` | — |
| [SRC-6BF96689A8-L000340](../../tests/test_research.py#L340) | 340 | `"    ]"` | — |
| [SRC-6BF96689A8-L000341](../../tests/test_research.py#L341) | 341 | `"    plan = fallback_plan(\"والبطارية؟\", history)"` | — |
| [SRC-6BF96689A8-L000342](../../tests/test_research.py#L342) | 342 | `"    assert plan[\"queries\"]"` | — |
| [SRC-6BF96689A8-L000343](../../tests/test_research.py#L343) | 343 | `"    assert \"iPhone 16\" in plan[\"queries\"][0]"` | — |
| [SRC-6BF96689A8-L000344](../../tests/test_research.py#L344) | 344 | `"    assert \"البطارية\" in plan[\"queries\"][0]"` | — |
| [SRC-6BF96689A8-L000345](../../tests/test_research.py#L345) | 345 | `""` | — |
| [SRC-6BF96689A8-L000346](../../tests/test_research.py#L346) | 346 | `""` | — |
| [SRC-6BF96689A8-L000347](../../tests/test_research.py#L347) | 347 | `"def test_followup_plan_does_not_inherit_unrelated_social_intent():"` | — |
| [SRC-6BF96689A8-L000348](../../tests/test_research.py#L348) | 348 | `"    history = ["` | — |
| [SRC-6BF96689A8-L000349](../../tests/test_research.py#L349) | 349 | `"        {\"role\": \"user\", \"content\": \"اجمع آراء مستخدمي السيارات الكهربائية على Reddit\"},"` | — |
| [SRC-6BF96689A8-L000350](../../tests/test_research.py#L350) | 350 | `"        {\"role\": \"assistant\", \"content\": \"هذه النتائج.\"},"` | — |
| [SRC-6BF96689A8-L000351](../../tests/test_research.py#L351) | 351 | `"    ]"` | — |
| [SRC-6BF96689A8-L000352](../../tests/test_research.py#L352) | 352 | `"    plan = fallback_plan(\"اشرح طريقة عمل المحرك الكهربائي\", history)"` | — |
| [SRC-6BF96689A8-L000353](../../tests/test_research.py#L353) | 353 | `"    assert plan[\"social_focus\"] is False"` | — |
| [SRC-6BF96689A8-L000354](../../tests/test_research.py#L354) | 354 | `"    assert plan[\"platforms\"] == []"` | — |
| [SRC-6BF96689A8-L000355](../../tests/test_research.py#L355) | 355 | `""` | — |
| [SRC-6BF96689A8-L000356](../../tests/test_research.py#L356) | 356 | `""` | — |
| [SRC-6BF96689A8-L000357](../../tests/test_research.py#L357) | 357 | `""` | — |
| [SRC-6BF96689A8-L000358](../../tests/test_research.py#L358) | 358 | `"def test_source_classification_does_not_trust_lookalike_news_domains():"` | — |
| [SRC-6BF96689A8-L000359](../../tests/test_research.py#L359) | 359 | `"    assert classify_source(\"https://www.reuters.com/world/article\")[\"source_class\"] == \"news\""` | — |
| [SRC-6BF96689A8-L000360](../../tests/test_research.py#L360) | 360 | `"    lookalike = classify_source(\"https://reuters.com.attacker.example/article\")"` | — |
| [SRC-6BF96689A8-L000361](../../tests/test_research.py#L361) | 361 | `"    assert lookalike[\"source_class\"] == \"general\""` | — |
| [SRC-6BF96689A8-L000362](../../tests/test_research.py#L362) | 362 | `"    assert lookalike[\"domain\"] == \"reuters.com.attacker.example\""` | — |
## اختبارات

### FILE-AFFCF23BD4 — [tests/test_research_completion.py](../../tests/test_research_completion.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-AFFCF23BD4-L000001](../../tests/test_research_completion.py#L1) | 1 | `"\"\"\"Tests for truthful research completion states and counter reconciliation.\"\"\""` | — |
| [SRC-AFFCF23BD4-L000002](../../tests/test_research_completion.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-AFFCF23BD4-L000003](../../tests/test_research_completion.py#L3) | 3 | `""` | — |
| [SRC-AFFCF23BD4-L000004](../../tests/test_research_completion.py#L4) | 4 | `"from agents.claim_evidence import build_claim_evidence_ledger"` | — |
| [SRC-AFFCF23BD4-L000005](../../tests/test_research_completion.py#L5) | 5 | `"from agents.research_completion import build_research_completion"` | — |
| [SRC-AFFCF23BD4-L000006](../../tests/test_research_completion.py#L6) | 6 | `""` | — |
| [SRC-AFFCF23BD4-L000007](../../tests/test_research_completion.py#L7) | 7 | `""` | — |
| [SRC-AFFCF23BD4-L000008](../../tests/test_research_completion.py#L8) | 8 | `"def test_non_research_answer_is_not_reported_as_web_research_complete() -> None:"` | — |
| [SRC-AFFCF23BD4-L000009](../../tests/test_research_completion.py#L9) | 9 | `"    result = build_research_completion({\"kind\": \"local_conversation\", \"answer\": \"مرحبا\"})"` | — |
| [SRC-AFFCF23BD4-L000010](../../tests/test_research_completion.py#L10) | 10 | `"    assert result[\"status\"] == \"not_applicable\""` | — |
| [SRC-AFFCF23BD4-L000011](../../tests/test_research_completion.py#L11) | 11 | `"    assert result[\"semantic_verification\"] == \"not_performed\""` | — |
| [SRC-AFFCF23BD4-L000012](../../tests/test_research_completion.py#L12) | 12 | `""` | — |
| [SRC-AFFCF23BD4-L000013](../../tests/test_research_completion.py#L13) | 13 | `""` | — |
| [SRC-AFFCF23BD4-L000014](../../tests/test_research_completion.py#L14) | 14 | `"def test_empty_results_distinguish_zero_results_from_tool_failure() -> None:"` | — |
| [SRC-AFFCF23BD4-L000015](../../tests/test_research_completion.py#L15) | 15 | `"    no_results = build_research_completion({"` | — |
| [SRC-AFFCF23BD4-L000016](../../tests/test_research_completion.py#L16) | 16 | `"        \"kind\": \"insufficient_evidence\","` | — |
| [SRC-AFFCF23BD4-L000017](../../tests/test_research_completion.py#L17) | 17 | `"        \"search_attempted\": True,"` | — |
| [SRC-AFFCF23BD4-L000018](../../tests/test_research_completion.py#L18) | 18 | `"        \"sources\": [],"` | — |
| [SRC-AFFCF23BD4-L000019](../../tests/test_research_completion.py#L19) | 19 | `"        \"search_report\": {"` | — |
| [SRC-AFFCF23BD4-L000020](../../tests/test_research_completion.py#L20) | 20 | `"            \"search_attempted\": True,"` | — |
| [SRC-AFFCF23BD4-L000021](../../tests/test_research_completion.py#L21) | 21 | `"            \"query_results\": [{\"query\": \"topic\", \"results\": 0}],"` | — |
| [SRC-AFFCF23BD4-L000022](../../tests/test_research_completion.py#L22) | 22 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-AFFCF23BD4-L000023](../../tests/test_research_completion.py#L23) | 23 | `"            \"queries_planned\": 1,"` | — |
| [SRC-AFFCF23BD4-L000024](../../tests/test_research_completion.py#L24) | 24 | `"        },"` | — |
| [SRC-AFFCF23BD4-L000025](../../tests/test_research_completion.py#L25) | 25 | `"    })"` | — |
| [SRC-AFFCF23BD4-L000026](../../tests/test_research_completion.py#L26) | 26 | `"    failure = build_research_completion({"` | — |
| [SRC-AFFCF23BD4-L000027](../../tests/test_research_completion.py#L27) | 27 | `"        \"kind\": \"web_fallback\","` | — |
| [SRC-AFFCF23BD4-L000028](../../tests/test_research_completion.py#L28) | 28 | `"        \"search_attempted\": True,"` | — |
| [SRC-AFFCF23BD4-L000029](../../tests/test_research_completion.py#L29) | 29 | `"        \"sources\": [],"` | — |
| [SRC-AFFCF23BD4-L000030](../../tests/test_research_completion.py#L30) | 30 | `"        \"search_report\": {"` | — |
| [SRC-AFFCF23BD4-L000031](../../tests/test_research_completion.py#L31) | 31 | `"            \"search_attempted\": True,"` | — |
| [SRC-AFFCF23BD4-L000032](../../tests/test_research_completion.py#L32) | 32 | `"            \"search_outcome\": \"attempted_research_error\","` | — |
| [SRC-AFFCF23BD4-L000033](../../tests/test_research_completion.py#L33) | 33 | `"            \"provider_diagnostics\": [{\"provider\": \"test\", \"status\": \"timeout\"}],"` | — |
| [SRC-AFFCF23BD4-L000034](../../tests/test_research_completion.py#L34) | 34 | `"        },"` | — |
| [SRC-AFFCF23BD4-L000035](../../tests/test_research_completion.py#L35) | 35 | `"    })"` | — |
| [SRC-AFFCF23BD4-L000036](../../tests/test_research_completion.py#L36) | 36 | `"    assert no_results[\"status\"] == \"no_results_returned\""` | — |
| [SRC-AFFCF23BD4-L000037](../../tests/test_research_completion.py#L37) | 37 | `"    assert no_results[\"phases\"][\"search\"] == \"completed_no_results\""` | — |
| [SRC-AFFCF23BD4-L000038](../../tests/test_research_completion.py#L38) | 38 | `"    assert failure[\"status\"] == \"search_failed_or_incomplete\""` | — |
| [SRC-AFFCF23BD4-L000039](../../tests/test_research_completion.py#L39) | 39 | `"    assert failure[\"counters\"][\"connector_failure_count\"] == 1"` | — |
| [SRC-AFFCF23BD4-L000040](../../tests/test_research_completion.py#L40) | 40 | `""` | — |
| [SRC-AFFCF23BD4-L000041](../../tests/test_research_completion.py#L41) | 41 | `""` | — |
| [SRC-AFFCF23BD4-L000042](../../tests/test_research_completion.py#L42) | 42 | `"def test_all_rejected_sources_are_not_mislabeled_as_no_results() -> None:"` | — |
| [SRC-AFFCF23BD4-L000043](../../tests/test_research_completion.py#L43) | 43 | `"    result = build_research_completion({"` | — |
| [SRC-AFFCF23BD4-L000044](../../tests/test_research_completion.py#L44) | 44 | `"        \"kind\": \"insufficient_evidence\","` | — |
| [SRC-AFFCF23BD4-L000045](../../tests/test_research_completion.py#L45) | 45 | `"        \"search_attempted\": True,"` | — |
| [SRC-AFFCF23BD4-L000046](../../tests/test_research_completion.py#L46) | 46 | `"        \"sources\": [],"` | — |
| [SRC-AFFCF23BD4-L000047](../../tests/test_research_completion.py#L47) | 47 | `"        \"search_report\": {"` | — |
| [SRC-AFFCF23BD4-L000048](../../tests/test_research_completion.py#L48) | 48 | `"            \"search_attempted\": True,"` | — |
| [SRC-AFFCF23BD4-L000049](../../tests/test_research_completion.py#L49) | 49 | `"            \"source_guardrails\": {"` | — |
| [SRC-AFFCF23BD4-L000050](../../tests/test_research_completion.py#L50) | 50 | `"                \"final\": {\"rejection_counts\": {\"stale\": 2, \"date_unavailable\": 1}},"` | — |
| [SRC-AFFCF23BD4-L000051](../../tests/test_research_completion.py#L51) | 51 | `"            },"` | — |
| [SRC-AFFCF23BD4-L000052](../../tests/test_research_completion.py#L52) | 52 | `"        },"` | — |
| [SRC-AFFCF23BD4-L000053](../../tests/test_research_completion.py#L53) | 53 | `"    })"` | — |
| [SRC-AFFCF23BD4-L000054](../../tests/test_research_completion.py#L54) | 54 | `"    assert result[\"status\"] == \"no_eligible_sources_after_filtering\""` | — |
| [SRC-AFFCF23BD4-L000055](../../tests/test_research_completion.py#L55) | 55 | `"    assert result[\"counters\"][\"guardrail_rejected_candidate_count\"] == 3"` | — |
| [SRC-AFFCF23BD4-L000056](../../tests/test_research_completion.py#L56) | 56 | `""` | — |
| [SRC-AFFCF23BD4-L000057](../../tests/test_research_completion.py#L57) | 57 | `""` | — |
| [SRC-AFFCF23BD4-L000058](../../tests/test_research_completion.py#L58) | 58 | `"def test_snippet_only_results_do_not_claim_pages_were_read() -> None:"` | — |
| [SRC-AFFCF23BD4-L000059](../../tests/test_research_completion.py#L59) | 59 | `"    result = build_research_completion({"` | — |
| [SRC-AFFCF23BD4-L000060](../../tests/test_research_completion.py#L60) | 60 | `"        \"kind\": \"web_fallback\","` | — |
| [SRC-AFFCF23BD4-L000061](../../tests/test_research_completion.py#L61) | 61 | `"        \"search_attempted\": True,"` | — |
| [SRC-AFFCF23BD4-L000062](../../tests/test_research_completion.py#L62) | 62 | `"        \"used_language_model\": False,"` | — |
| [SRC-AFFCF23BD4-L000063](../../tests/test_research_completion.py#L63) | 63 | `"        \"sources\": ["` | — |
| [SRC-AFFCF23BD4-L000064](../../tests/test_research_completion.py#L64) | 64 | `"            {\"url\": \"https://example.com/a\", \"snippet\": \"Search snippet\", \"page_fetched\": False}"` | — |
| [SRC-AFFCF23BD4-L000065](../../tests/test_research_completion.py#L65) | 65 | `"        ],"` | — |
| [SRC-AFFCF23BD4-L000066](../../tests/test_research_completion.py#L66) | 66 | `"        \"search_report\": {\"unique_sources\": 1, \"pages_fetched\": 0},"` | — |
| [SRC-AFFCF23BD4-L000067](../../tests/test_research_completion.py#L67) | 67 | `"    })"` | — |
| [SRC-AFFCF23BD4-L000068](../../tests/test_research_completion.py#L68) | 68 | `"    assert result[\"status\"] == \"source_snippets_only_generation_not_completed\""` | — |
| [SRC-AFFCF23BD4-L000069](../../tests/test_research_completion.py#L69) | 69 | `"    assert result[\"phases\"][\"page_reading\"] == \"no_final_source_page_read\""` | — |
| [SRC-AFFCF23BD4-L000070](../../tests/test_research_completion.py#L70) | 70 | `"    assert result[\"counters\"][\"pages_read_with_text_count\"] == 0"` | — |
| [SRC-AFFCF23BD4-L000071](../../tests/test_research_completion.py#L71) | 71 | `""` | — |
| [SRC-AFFCF23BD4-L000072](../../tests/test_research_completion.py#L72) | 72 | `""` | — |
| [SRC-AFFCF23BD4-L000073](../../tests/test_research_completion.py#L73) | 73 | `"def test_answer_with_valid_citation_indices_still_discloses_semantic_gap() -> None:"` | — |
| [SRC-AFFCF23BD4-L000074](../../tests/test_research_completion.py#L74) | 74 | `"    result = build_research_completion({"` | — |
| [SRC-AFFCF23BD4-L000075](../../tests/test_research_completion.py#L75) | 75 | `"        \"kind\": \"web_research\","` | — |
| [SRC-AFFCF23BD4-L000076](../../tests/test_research_completion.py#L76) | 76 | `"        \"search_attempted\": True,"` | — |
| [SRC-AFFCF23BD4-L000077](../../tests/test_research_completion.py#L77) | 77 | `"        \"used_language_model\": True,"` | — |
| [SRC-AFFCF23BD4-L000078](../../tests/test_research_completion.py#L78) | 78 | `"        \"final_answer_status\": \"model_answer_generated\","` | — |
| [SRC-AFFCF23BD4-L000079](../../tests/test_research_completion.py#L79) | 79 | `"        \"citation_validation\": {\"status\": \"index_range_check_passed\", \"valid_citation_count\": 2},"` | — |
| [SRC-AFFCF23BD4-L000080](../../tests/test_research_completion.py#L80) | 80 | `"        \"sources\": ["` | — |
| [SRC-AFFCF23BD4-L000081](../../tests/test_research_completion.py#L81) | 81 | `"            {\"url\": \"https://example.com/a\", \"snippet\": \"text\", \"page_fetched\": True, \"page_text\": \"read\"}"` | — |
| [SRC-AFFCF23BD4-L000082](../../tests/test_research_completion.py#L82) | 82 | `"        ],"` | — |
| [SRC-AFFCF23BD4-L000083](../../tests/test_research_completion.py#L83) | 83 | `"        \"search_report\": {"` | — |
| [SRC-AFFCF23BD4-L000084](../../tests/test_research_completion.py#L84) | 84 | `"            \"unique_sources\": 1, \"pages_fetched\": 1,"` | — |
| [SRC-AFFCF23BD4-L000085](../../tests/test_research_completion.py#L85) | 85 | `"            \"query_results\": [{\"query\": \"topic\", \"results\": 1}],"` | — |
| [SRC-AFFCF23BD4-L000086](../../tests/test_research_completion.py#L86) | 86 | `"        },"` | — |
| [SRC-AFFCF23BD4-L000087](../../tests/test_research_completion.py#L87) | 87 | `"    })"` | — |
| [SRC-AFFCF23BD4-L000088](../../tests/test_research_completion.py#L88) | 88 | `"    assert result[\"status\"] == \"answer_generated_citations_range_checked_semantic_support_unverified\""` | — |
| [SRC-AFFCF23BD4-L000089](../../tests/test_research_completion.py#L89) | 89 | `"    assert result[\"phases\"][\"semantic_verification\"] == \"not_performed\""` | — |
| [SRC-AFFCF23BD4-L000090](../../tests/test_research_completion.py#L90) | 90 | `"    assert result[\"semantic_verification\"] == \"not_performed\""` | — |
| [SRC-AFFCF23BD4-L000091](../../tests/test_research_completion.py#L91) | 91 | `""` | — |
| [SRC-AFFCF23BD4-L000092](../../tests/test_research_completion.py#L92) | 92 | `""` | — |
| [SRC-AFFCF23BD4-L000093](../../tests/test_research_completion.py#L93) | 93 | `"def test_normalized_url_counters_and_mismatched_legacy_counters_are_exposed() -> None:"` | — |
| [SRC-AFFCF23BD4-L000094](../../tests/test_research_completion.py#L94) | 94 | `"    result = build_research_completion({"` | — |
| [SRC-AFFCF23BD4-L000095](../../tests/test_research_completion.py#L95) | 95 | `"        \"kind\": \"web_fallback\","` | — |
| [SRC-AFFCF23BD4-L000096](../../tests/test_research_completion.py#L96) | 96 | `"        \"search_attempted\": True,"` | — |
| [SRC-AFFCF23BD4-L000097](../../tests/test_research_completion.py#L97) | 97 | `"        \"sources\": ["` | — |
| [SRC-AFFCF23BD4-L000098](../../tests/test_research_completion.py#L98) | 98 | `"            {\"url\": \"https://example.com/path?utm_source=abc\", \"snippet\": \"a\"},"` | — |
| [SRC-AFFCF23BD4-L000099](../../tests/test_research_completion.py#L99) | 99 | `"            {\"url\": \"https://example.com/path#section\", \"snippet\": \"b\"},"` | — |
| [SRC-AFFCF23BD4-L000100](../../tests/test_research_completion.py#L100) | 100 | `"        ],"` | — |
| [SRC-AFFCF23BD4-L000101](../../tests/test_research_completion.py#L101) | 101 | `"        \"search_report\": {\"unique_sources\": 5, \"pages_fetched\": 4},"` | — |
| [SRC-AFFCF23BD4-L000102](../../tests/test_research_completion.py#L102) | 102 | `"    })"` | — |
| [SRC-AFFCF23BD4-L000103](../../tests/test_research_completion.py#L103) | 103 | `"    assert result[\"counters\"][\"final_source_list_count\"] == 2"` | — |
| [SRC-AFFCF23BD4-L000104](../../tests/test_research_completion.py#L104) | 104 | `"    assert result[\"counters\"][\"unique_normalized_url_count\"] == 1"` | — |
| [SRC-AFFCF23BD4-L000105](../../tests/test_research_completion.py#L105) | 105 | `"    assert result[\"counters\"][\"duplicate_normalized_url_count\"] == 1"` | — |
| [SRC-AFFCF23BD4-L000106](../../tests/test_research_completion.py#L106) | 106 | `"    assert result[\"counter_consistency\"][\"status\"] == \"mismatch_detected\""` | — |
| [SRC-AFFCF23BD4-L000107](../../tests/test_research_completion.py#L107) | 107 | `"    assert len(result[\"counter_consistency\"][\"issues\"]) == 2"` | — |
| [SRC-AFFCF23BD4-L000108](../../tests/test_research_completion.py#L108) | 108 | `""` | — |
| [SRC-AFFCF23BD4-L000109](../../tests/test_research_completion.py#L109) | 109 | `""` | — |
| [SRC-AFFCF23BD4-L000110](../../tests/test_research_completion.py#L110) | 110 | `"def test_counter_consistency_is_not_claimed_when_legacy_counters_are_missing() -> None:"` | — |
| [SRC-AFFCF23BD4-L000111](../../tests/test_research_completion.py#L111) | 111 | `"    result = build_research_completion({"` | — |
| [SRC-AFFCF23BD4-L000112](../../tests/test_research_completion.py#L112) | 112 | `"        \"kind\": \"web_fallback\", \"search_attempted\": True, \"sources\": [],"` | — |
| [SRC-AFFCF23BD4-L000113](../../tests/test_research_completion.py#L113) | 113 | `"        \"search_report\": {\"query_results\": []},"` | — |
| [SRC-AFFCF23BD4-L000114](../../tests/test_research_completion.py#L114) | 114 | `"    })"` | — |
| [SRC-AFFCF23BD4-L000115](../../tests/test_research_completion.py#L115) | 115 | `"    assert result[\"counter_consistency\"][\"status\"] == \"not_computable\""` | — |
| [SRC-AFFCF23BD4-L000116](../../tests/test_research_completion.py#L116) | 116 | `""` | — |
| [SRC-AFFCF23BD4-L000117](../../tests/test_research_completion.py#L117) | 117 | `""` | — |
| [SRC-AFFCF23BD4-L000118](../../tests/test_research_completion.py#L118) | 118 | `""` | — |
| [SRC-AFFCF23BD4-L000119](../../tests/test_research_completion.py#L119) | 119 | `"def test_public_readability_marker_counts_read_page_without_exposing_text() -> None:"` | — |
| [SRC-AFFCF23BD4-L000120](../../tests/test_research_completion.py#L120) | 120 | `"    result = build_research_completion({"` | — |
| [SRC-AFFCF23BD4-L000121](../../tests/test_research_completion.py#L121) | 121 | `"        \"kind\": \"web_research\","` | — |
| [SRC-AFFCF23BD4-L000122](../../tests/test_research_completion.py#L122) | 122 | `"        \"used_language_model\": True,"` | — |
| [SRC-AFFCF23BD4-L000123](../../tests/test_research_completion.py#L123) | 123 | `"        \"final_answer_status\": \"model_answer_generated\","` | — |
| [SRC-AFFCF23BD4-L000124](../../tests/test_research_completion.py#L124) | 124 | `"        \"sources\": [{"` | — |
| [SRC-AFFCF23BD4-L000125](../../tests/test_research_completion.py#L125) | 125 | `"            \"url\": \"https://example.com/a\","` | — |
| [SRC-AFFCF23BD4-L000126](../../tests/test_research_completion.py#L126) | 126 | `"            \"snippet\": \"summary\","` | — |
| [SRC-AFFCF23BD4-L000127](../../tests/test_research_completion.py#L127) | 127 | `"            \"page_fetched\": True,"` | — |
| [SRC-AFFCF23BD4-L000128](../../tests/test_research_completion.py#L128) | 128 | `"            \"readable_page_text_available\": True,"` | — |
| [SRC-AFFCF23BD4-L000129](../../tests/test_research_completion.py#L129) | 129 | `"        }],"` | — |
| [SRC-AFFCF23BD4-L000130](../../tests/test_research_completion.py#L130) | 130 | `"        \"search_report\": {\"unique_sources\": 1, \"pages_fetched\": 1},"` | — |
| [SRC-AFFCF23BD4-L000131](../../tests/test_research_completion.py#L131) | 131 | `"    })"` | — |
| [SRC-AFFCF23BD4-L000132](../../tests/test_research_completion.py#L132) | 132 | `"    assert result[\"counters\"][\"pages_read_with_text_count\"] == 1"` | — |
| [SRC-AFFCF23BD4-L000133](../../tests/test_research_completion.py#L133) | 133 | `"    assert result[\"phases\"][\"page_reading\"] == \"all_final_sources_read\""` | — |
| [SRC-AFFCF23BD4-L000134](../../tests/test_research_completion.py#L134) | 134 | `""` | — |
| [SRC-AFFCF23BD4-L000135](../../tests/test_research_completion.py#L135) | 135 | `""` | — |
| [SRC-AFFCF23BD4-L000136](../../tests/test_research_completion.py#L136) | 136 | `"def test_ref_query_parameters_are_not_assumed_to_be_tracking_ids() -> None:"` | — |
| [SRC-AFFCF23BD4-L000137](../../tests/test_research_completion.py#L137) | 137 | `"    result = build_research_completion({"` | — |
| [SRC-AFFCF23BD4-L000138](../../tests/test_research_completion.py#L138) | 138 | `"        \"kind\": \"web_fallback\","` | — |
| [SRC-AFFCF23BD4-L000139](../../tests/test_research_completion.py#L139) | 139 | `"        \"sources\": ["` | — |
| [SRC-AFFCF23BD4-L000140](../../tests/test_research_completion.py#L140) | 140 | `"            {\"url\": \"https://example.com/post?ref=one\"},"` | — |
| [SRC-AFFCF23BD4-L000141](../../tests/test_research_completion.py#L141) | 141 | `"            {\"url\": \"https://example.com/post?ref=two\"},"` | — |
| [SRC-AFFCF23BD4-L000142](../../tests/test_research_completion.py#L142) | 142 | `"        ],"` | — |
| [SRC-AFFCF23BD4-L000143](../../tests/test_research_completion.py#L143) | 143 | `"        \"search_report\": {},"` | — |
| [SRC-AFFCF23BD4-L000144](../../tests/test_research_completion.py#L144) | 144 | `"    })"` | — |
| [SRC-AFFCF23BD4-L000145](../../tests/test_research_completion.py#L145) | 145 | `"    assert result[\"counters\"][\"unique_normalized_url_count\"] == 2"` | — |
| [SRC-AFFCF23BD4-L000146](../../tests/test_research_completion.py#L146) | 146 | `"    assert result[\"counters\"][\"duplicate_normalized_url_count\"] == 0"` | — |
| [SRC-AFFCF23BD4-L000147](../../tests/test_research_completion.py#L147) | 147 | `""` | — |
| [SRC-AFFCF23BD4-L000148](../../tests/test_research_completion.py#L148) | 148 | `""` | — |
| [SRC-AFFCF23BD4-L000149](../../tests/test_research_completion.py#L149) | 149 | `""` | — |
| [SRC-AFFCF23BD4-L000150](../../tests/test_research_completion.py#L150) | 150 | `"def test_unflagged_page_text_marker_is_counted_without_exposing_page_text() -> None:"` | — |
| [SRC-AFFCF23BD4-L000151](../../tests/test_research_completion.py#L151) | 151 | `"    result = build_research_completion({"` | — |
| [SRC-AFFCF23BD4-L000152](../../tests/test_research_completion.py#L152) | 152 | `"        \"kind\": \"web_fallback\","` | — |
| [SRC-AFFCF23BD4-L000153](../../tests/test_research_completion.py#L153) | 153 | `"        \"sources\": [{"` | — |
| [SRC-AFFCF23BD4-L000154](../../tests/test_research_completion.py#L154) | 154 | `"            \"url\": \"https://example.com/a\","` | — |
| [SRC-AFFCF23BD4-L000155](../../tests/test_research_completion.py#L155) | 155 | `"            \"snippet\": \"summary\","` | — |
| [SRC-AFFCF23BD4-L000156](../../tests/test_research_completion.py#L156) | 156 | `"            \"page_fetched\": False,"` | — |
| [SRC-AFFCF23BD4-L000157](../../tests/test_research_completion.py#L157) | 157 | `"            \"page_text_present_without_fetch_flag\": True,"` | — |
| [SRC-AFFCF23BD4-L000158](../../tests/test_research_completion.py#L158) | 158 | `"        }],"` | — |
| [SRC-AFFCF23BD4-L000159](../../tests/test_research_completion.py#L159) | 159 | `"        \"search_report\": {},"` | — |
| [SRC-AFFCF23BD4-L000160](../../tests/test_research_completion.py#L160) | 160 | `"    })"` | — |
| [SRC-AFFCF23BD4-L000161](../../tests/test_research_completion.py#L161) | 161 | `"    assert result[\"counters\"][\"page_text_without_fetched_flag_count\"] == 1"` | — |
| [SRC-AFFCF23BD4-L000162](../../tests/test_research_completion.py#L162) | 162 | `""` | — |
| [SRC-AFFCF23BD4-L000163](../../tests/test_research_completion.py#L163) | 163 | `""` | — |
| [SRC-AFFCF23BD4-L000164](../../tests/test_research_completion.py#L164) | 164 | `""` | — |
| [SRC-AFFCF23BD4-L000165](../../tests/test_research_completion.py#L165) | 165 | `"def test_unresolved_citation_support_flags_prevent_completed_research_status() -> None:"` | — |
| [SRC-AFFCF23BD4-L000166](../../tests/test_research_completion.py#L166) | 166 | `"    base = {"` | — |
| [SRC-AFFCF23BD4-L000167](../../tests/test_research_completion.py#L167) | 167 | `"        \"kind\": \"web_research\","` | — |
| [SRC-AFFCF23BD4-L000168](../../tests/test_research_completion.py#L168) | 168 | `"        \"search_attempted\": True,"` | — |
| [SRC-AFFCF23BD4-L000169](../../tests/test_research_completion.py#L169) | 169 | `"        \"used_language_model\": True,"` | — |
| [SRC-AFFCF23BD4-L000170](../../tests/test_research_completion.py#L170) | 170 | `"        \"final_answer_status\": \"model_answer_generated\","` | — |
| [SRC-AFFCF23BD4-L000171](../../tests/test_research_completion.py#L171) | 171 | `"        \"citation_validation\": {"` | — |
| [SRC-AFFCF23BD4-L000172](../../tests/test_research_completion.py#L172) | 172 | `"            \"status\": \"index_range_check_passed\","` | — |
| [SRC-AFFCF23BD4-L000173](../../tests/test_research_completion.py#L173) | 173 | `"            \"valid_citation_count\": 1,"` | — |
| [SRC-AFFCF23BD4-L000174](../../tests/test_research_completion.py#L174) | 174 | `"        },"` | — |
| [SRC-AFFCF23BD4-L000175](../../tests/test_research_completion.py#L175) | 175 | `"        \"sources\": ["` | — |
| [SRC-AFFCF23BD4-L000176](../../tests/test_research_completion.py#L176) | 176 | `"            {"` | — |
| [SRC-AFFCF23BD4-L000177](../../tests/test_research_completion.py#L177) | 177 | `"                \"url\": \"https://example.com/report\","` | — |
| [SRC-AFFCF23BD4-L000178](../../tests/test_research_completion.py#L178) | 178 | `"                \"snippet\": \"A readable report excerpt.\","` | — |
| [SRC-AFFCF23BD4-L000179](../../tests/test_research_completion.py#L179) | 179 | `"                \"page_fetched\": True,"` | — |
| [SRC-AFFCF23BD4-L000180](../../tests/test_research_completion.py#L180) | 180 | `"                \"page_text\": \"A readable report excerpt.\","` | — |
| [SRC-AFFCF23BD4-L000181](../../tests/test_research_completion.py#L181) | 181 | `"            }"` | — |
| [SRC-AFFCF23BD4-L000182](../../tests/test_research_completion.py#L182) | 182 | `"        ],"` | — |
| [SRC-AFFCF23BD4-L000183](../../tests/test_research_completion.py#L183) | 183 | `"        \"search_report\": {\"unique_sources\": 1, \"pages_fetched\": 1},"` | — |
| [SRC-AFFCF23BD4-L000184](../../tests/test_research_completion.py#L184) | 184 | `"    }"` | — |
| [SRC-AFFCF23BD4-L000185](../../tests/test_research_completion.py#L185) | 185 | `""` | — |
| [SRC-AFFCF23BD4-L000186](../../tests/test_research_completion.py#L186) | 186 | `"    unsupported_number = build_research_completion({"` | — |
| [SRC-AFFCF23BD4-L000187](../../tests/test_research_completion.py#L187) | 187 | `"        **base,"` | — |
| [SRC-AFFCF23BD4-L000188](../../tests/test_research_completion.py#L188) | 188 | `"        \"answer_integrity\": {"` | — |
| [SRC-AFFCF23BD4-L000189](../../tests/test_research_completion.py#L189) | 189 | `"            \"potentially_unsupported_numeric_by_citation_count\": 1,"` | — |
| [SRC-AFFCF23BD4-L000190](../../tests/test_research_completion.py#L190) | 190 | `"        },"` | — |
| [SRC-AFFCF23BD4-L000191](../../tests/test_research_completion.py#L191) | 191 | `"    })"` | — |
| [SRC-AFFCF23BD4-L000192](../../tests/test_research_completion.py#L192) | 192 | `"    weak_alignment = build_research_completion({"` | — |
| [SRC-AFFCF23BD4-L000193](../../tests/test_research_completion.py#L193) | 193 | `"        **base,"` | — |
| [SRC-AFFCF23BD4-L000194](../../tests/test_research_completion.py#L194) | 194 | `"        \"answer_integrity\": {\"weak_citation_alignment_count\": 1},"` | — |
| [SRC-AFFCF23BD4-L000195](../../tests/test_research_completion.py#L195) | 195 | `"    })"` | — |
| [SRC-AFFCF23BD4-L000196](../../tests/test_research_completion.py#L196) | 196 | `""` | — |
| [SRC-AFFCF23BD4-L000197](../../tests/test_research_completion.py#L197) | 197 | `"    assert unsupported_number[\"status\"] == \"partial_answer_evidence_gaps_detected\""` | — |
| [SRC-AFFCF23BD4-L000198](../../tests/test_research_completion.py#L198) | 198 | `"    assert weak_alignment[\"status\"] == \"partial_answer_evidence_gaps_detected\""` | — |
| [SRC-AFFCF23BD4-L000199](../../tests/test_research_completion.py#L199) | 199 | `"    assert unsupported_number[\"counters\"][\"citation_support_warning_count\"] == 1"` | — |
| [SRC-AFFCF23BD4-L000200](../../tests/test_research_completion.py#L200) | 200 | `"    assert weak_alignment[\"counters\"][\"citation_support_warning_count\"] == 1"` | — |
| [SRC-AFFCF23BD4-L000201](../../tests/test_research_completion.py#L201) | 201 | `"    assert unsupported_number[\"phases\"][\"semantic_verification\"] == \"not_performed\""` | — |
| [SRC-AFFCF23BD4-L000202](../../tests/test_research_completion.py#L202) | 202 | `"    assert weak_alignment[\"phases\"][\"semantic_verification\"] == \"not_performed\""` | — |
| [SRC-AFFCF23BD4-L000203](../../tests/test_research_completion.py#L203) | 203 | `""` | — |
| [SRC-AFFCF23BD4-L000204](../../tests/test_research_completion.py#L204) | 204 | `""` | — |
| [SRC-AFFCF23BD4-L000205](../../tests/test_research_completion.py#L205) | 205 | `"def test_out_of_range_citation_reference_prevents_completed_research_status() -> None:"` | — |
| [SRC-AFFCF23BD4-L000206](../../tests/test_research_completion.py#L206) | 206 | `"    result = build_research_completion({"` | — |
| [SRC-AFFCF23BD4-L000207](../../tests/test_research_completion.py#L207) | 207 | `"        \"kind\": \"web_research\","` | — |
| [SRC-AFFCF23BD4-L000208](../../tests/test_research_completion.py#L208) | 208 | `"        \"search_attempted\": True,"` | — |
| [SRC-AFFCF23BD4-L000209](../../tests/test_research_completion.py#L209) | 209 | `"        \"used_language_model\": True,"` | — |
| [SRC-AFFCF23BD4-L000210](../../tests/test_research_completion.py#L210) | 210 | `"        \"final_answer_status\": \"model_answer_generated\","` | — |
| [SRC-AFFCF23BD4-L000211](../../tests/test_research_completion.py#L211) | 211 | `"        \"citation_validation\": {"` | — |
| [SRC-AFFCF23BD4-L000212](../../tests/test_research_completion.py#L212) | 212 | `"            \"status\": \"index_range_check_passed\","` | — |
| [SRC-AFFCF23BD4-L000213](../../tests/test_research_completion.py#L213) | 213 | `"            \"valid_citation_count\": 1,"` | — |
| [SRC-AFFCF23BD4-L000214](../../tests/test_research_completion.py#L214) | 214 | `"        },"` | — |
| [SRC-AFFCF23BD4-L000215](../../tests/test_research_completion.py#L215) | 215 | `"        \"claim_evidence_ledger\": {"` | — |
| [SRC-AFFCF23BD4-L000216](../../tests/test_research_completion.py#L216) | 216 | `"            \"status\": \"built\","` | — |
| [SRC-AFFCF23BD4-L000217](../../tests/test_research_completion.py#L217) | 217 | `"            \"summary\": {"` | — |
| [SRC-AFFCF23BD4-L000218](../../tests/test_research_completion.py#L218) | 218 | `"                \"out_of_range_reference_count\": 1,"` | — |
| [SRC-AFFCF23BD4-L000219](../../tests/test_research_completion.py#L219) | 219 | `"            },"` | — |
| [SRC-AFFCF23BD4-L000220](../../tests/test_research_completion.py#L220) | 220 | `"        },"` | — |
| [SRC-AFFCF23BD4-L000221](../../tests/test_research_completion.py#L221) | 221 | `"        \"answer_integrity\": {"` | — |
| [SRC-AFFCF23BD4-L000222](../../tests/test_research_completion.py#L222) | 222 | `"            # One of multiple citations aligned lexically; this must not hide"` | — |
| [SRC-AFFCF23BD4-L000223](../../tests/test_research_completion.py#L223) | 223 | `"            # a separate out-of-range reference in the same answer."` | — |
| [SRC-AFFCF23BD4-L000224](../../tests/test_research_completion.py#L224) | 224 | `"            \"weak_citation_alignment_count\": 0,"` | — |
| [SRC-AFFCF23BD4-L000225](../../tests/test_research_completion.py#L225) | 225 | `"        },"` | — |
| [SRC-AFFCF23BD4-L000226](../../tests/test_research_completion.py#L226) | 226 | `"        \"sources\": [{"` | — |
| [SRC-AFFCF23BD4-L000227](../../tests/test_research_completion.py#L227) | 227 | `"            \"url\": \"https://example.com/report\","` | — |
| [SRC-AFFCF23BD4-L000228](../../tests/test_research_completion.py#L228) | 228 | `"            \"snippet\": \"A readable report excerpt.\","` | — |
| [SRC-AFFCF23BD4-L000229](../../tests/test_research_completion.py#L229) | 229 | `"            \"page_fetched\": True,"` | — |
| [SRC-AFFCF23BD4-L000230](../../tests/test_research_completion.py#L230) | 230 | `"            \"page_text\": \"A readable report excerpt.\","` | — |
| [SRC-AFFCF23BD4-L000231](../../tests/test_research_completion.py#L231) | 231 | `"        }],"` | — |
| [SRC-AFFCF23BD4-L000232](../../tests/test_research_completion.py#L232) | 232 | `"        \"search_report\": {\"unique_sources\": 1, \"pages_fetched\": 1},"` | — |
| [SRC-AFFCF23BD4-L000233](../../tests/test_research_completion.py#L233) | 233 | `"    })"` | — |
| [SRC-AFFCF23BD4-L000234](../../tests/test_research_completion.py#L234) | 234 | `""` | — |
| [SRC-AFFCF23BD4-L000235](../../tests/test_research_completion.py#L235) | 235 | `"    assert result[\"status\"] == \"partial_answer_evidence_gaps_detected\""` | — |
| [SRC-AFFCF23BD4-L000236](../../tests/test_research_completion.py#L236) | 236 | `"    assert result[\"counters\"][\"out_of_range_citation_reference_count\"] == 1"` | — |
| [SRC-AFFCF23BD4-L000237](../../tests/test_research_completion.py#L237) | 237 | `"    assert result[\"counters\"][\"citation_support_warning_count\"] == 1"` | — |
| [SRC-AFFCF23BD4-L000238](../../tests/test_research_completion.py#L238) | 238 | `"    assert result[\"phases\"][\"citation_support_screen\"] == \"warning_signals_detected\""` | — |
| [SRC-AFFCF23BD4-L000239](../../tests/test_research_completion.py#L239) | 239 | `""` | — |
| [SRC-AFFCF23BD4-L000240](../../tests/test_research_completion.py#L240) | 240 | `""` | — |
| [SRC-AFFCF23BD4-L000241](../../tests/test_research_completion.py#L241) | 241 | `"def test_missing_claim_ledger_does_not_create_citation_reference_warning() -> None:"` | — |
| [SRC-AFFCF23BD4-L000242](../../tests/test_research_completion.py#L242) | 242 | `"    result = build_research_completion({"` | — |
| [SRC-AFFCF23BD4-L000243](../../tests/test_research_completion.py#L243) | 243 | `"        \"kind\": \"web_research\","` | — |
| [SRC-AFFCF23BD4-L000244](../../tests/test_research_completion.py#L244) | 244 | `"        \"used_language_model\": True,"` | — |
| [SRC-AFFCF23BD4-L000245](../../tests/test_research_completion.py#L245) | 245 | `"        \"final_answer_status\": \"model_answer_generated\","` | — |
