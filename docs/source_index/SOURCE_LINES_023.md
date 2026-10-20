# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **023**
- سجلات الأسطر: **800**
- النطاق: SRC-B106ADC5EF-L000052 إلى SRC-F725E90B2A-L000270
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-B106ADC5EF — [tests/test_proxy_origin.py](../../tests/test_proxy_origin.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-B106ADC5EF-L000052](../../tests/test_proxy_origin.py#L52) | 52 | `"}"` | — |
| [SRC-B106ADC5EF-L000053](../../tests/test_proxy_origin.py#L53) | 53 | `""` | — |
| [SRC-B106ADC5EF-L000054](../../tests/test_proxy_origin.py#L54) | 54 | `"@pytest.mark.parametrize(\"shape\", ALLOWED_SHAPES)"` | — |
| [SRC-B106ADC5EF-L000055](../../tests/test_proxy_origin.py#L55) | 55 | `"def test_own_origin_is_accepted_behind_a_proxy(port, shape):"` | — |
| [SRC-B106ADC5EF-L000056](../../tests/test_proxy_origin.py#L56) | 56 | `"    headers = {**ALLOWED_SHAPES[shape], \"Origin\": \"https://\" + PUBLIC_NAME}"` | — |
| [SRC-B106ADC5EF-L000057](../../tests/test_proxy_origin.py#L57) | 57 | `"    assert call(port, \"POST\", headers) == 200"` | — |
| [SRC-B106ADC5EF-L000058](../../tests/test_proxy_origin.py#L58) | 58 | `"    assert call(port, \"OPTIONS\", {k: v for k, v in headers.items() if k != \"Authorization\"}) == 204"` | — |
| [SRC-B106ADC5EF-L000059](../../tests/test_proxy_origin.py#L59) | 59 | `""` | — |
| [SRC-B106ADC5EF-L000060](../../tests/test_proxy_origin.py#L60) | 60 | `"@pytest.mark.parametrize(\"shape\", ALLOWED_SHAPES)"` | — |
| [SRC-B106ADC5EF-L000061](../../tests/test_proxy_origin.py#L61) | 61 | `"def test_a_foreign_site_is_still_refused(port, shape):"` | — |
| [SRC-B106ADC5EF-L000062](../../tests/test_proxy_origin.py#L62) | 62 | `"    headers = {**ALLOWED_SHAPES[shape], \"Origin\": \"https://evil.example\"}"` | — |
| [SRC-B106ADC5EF-L000063](../../tests/test_proxy_origin.py#L63) | 63 | `"    assert call(port, \"POST\", headers) == 403"` | — |
| [SRC-B106ADC5EF-L000064](../../tests/test_proxy_origin.py#L64) | 64 | `"    assert call(port, \"OPTIONS\", headers) == 403"` | — |
| [SRC-B106ADC5EF-L000065](../../tests/test_proxy_origin.py#L65) | 65 | `""` | — |
| [SRC-B106ADC5EF-L000066](../../tests/test_proxy_origin.py#L66) | 66 | `"def test_configured_origin_still_works_without_any_proxy_headers(port, monkeypatch):"` | — |
| [SRC-B106ADC5EF-L000067](../../tests/test_proxy_origin.py#L67) | 67 | `"    monkeypatch.setenv(\"OMARAI_ALLOWED_ORIGINS\", \"https://frontend.example\")"` | — |
| [SRC-B106ADC5EF-L000068](../../tests/test_proxy_origin.py#L68) | 68 | `"    headers = {\"Host\": \"127.0.0.1:8000\", \"Origin\": \"https://frontend.example\"}"` | — |
| [SRC-B106ADC5EF-L000069](../../tests/test_proxy_origin.py#L69) | 69 | `"    assert call(port, \"POST\", headers) == 200"` | — |
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
## اختبارات

### FILE-6BF96689A8 — [tests/test_research.py](../../tests/test_research.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6BF96689A8-L000001](../../tests/test_research.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-6BF96689A8-L000002](../../tests/test_research.py#L2) | 2 | `""` | — |
| [SRC-6BF96689A8-L000003](../../tests/test_research.py#L3) | 3 | `"from agents.research import ("` | — |
| [SRC-6BF96689A8-L000004](../../tests/test_research.py#L4) | 4 | `"    evidence_signal_report,"` | — |
| [SRC-6BF96689A8-L000005](../../tests/test_research.py#L5) | 5 | `"    fallback_plan,"` | — |
| [SRC-6BF96689A8-L000006](../../tests/test_research.py#L6) | 6 | `"    fuse_ranked_results,"` | — |
| [SRC-6BF96689A8-L000007](../../tests/test_research.py#L7) | 7 | `"    registrable_domain,"` | — |
| [SRC-6BF96689A8-L000008](../../tests/test_research.py#L8) | 8 | `"    validate_plan,"` | — |
| [SRC-6BF96689A8-L000009](../../tests/test_research.py#L9) | 9 | `")"` | — |
| [SRC-6BF96689A8-L000010](../../tests/test_research.py#L10) | 10 | `""` | — |
| [SRC-6BF96689A8-L000011](../../tests/test_research.py#L11) | 11 | `""` | — |
| [SRC-6BF96689A8-L000012](../../tests/test_research.py#L12) | 12 | `"def test_social_question_gets_platform_targeted_queries():"` | — |
| [SRC-6BF96689A8-L000013](../../tests/test_research.py#L13) | 13 | `"    plan = fallback_plan(\"ابحث في Reddit عن تجارب العملاء مع السيارات الكهربائية\")"` | — |
| [SRC-6BF96689A8-L000014](../../tests/test_research.py#L14) | 14 | `"    assert plan[\"social_focus\"] is True"` | — |
| [SRC-6BF96689A8-L000015](../../tests/test_research.py#L15) | 15 | `"    assert \"reddit\" in plan[\"platforms\"]"` | — |
| [SRC-6BF96689A8-L000016](../../tests/test_research.py#L16) | 16 | `"    assert any(\"site:reddit.com\" in query for query in plan[\"queries\"])"` | — |
| [SRC-6BF96689A8-L000017](../../tests/test_research.py#L17) | 17 | `"    assert len(plan[\"queries\"]) <= 8"` | — |
| [SRC-6BF96689A8-L000018](../../tests/test_research.py#L18) | 18 | `""` | — |
| [SRC-6BF96689A8-L000019](../../tests/test_research.py#L19) | 19 | `""` | — |
| [SRC-6BF96689A8-L000020](../../tests/test_research.py#L20) | 20 | `"def test_follow_up_query_keeps_prior_topic():"` | — |
| [SRC-6BF96689A8-L000021](../../tests/test_research.py#L21) | 21 | `"    history = [{\"role\": \"user\", \"content\": \"قارن سوق السيارات الكهربائية في مصر\"}]"` | — |
| [SRC-6BF96689A8-L000022](../../tests/test_research.py#L22) | 22 | `"    plan = fallback_plan(\"وطب الأسعار الحالية؟\", history)"` | — |
| [SRC-6BF96689A8-L000023](../../tests/test_research.py#L23) | 23 | `"    assert \"السيارات الكهربائية\" in plan[\"queries\"][0]"` | — |
| [SRC-6BF96689A8-L000024](../../tests/test_research.py#L24) | 24 | `"    assert plan[\"freshness\"] == \"current\""` | — |
| [SRC-6BF96689A8-L000025](../../tests/test_research.py#L25) | 25 | `""` | — |
| [SRC-6BF96689A8-L000026](../../tests/test_research.py#L26) | 26 | `""` | — |
| [SRC-6BF96689A8-L000027](../../tests/test_research.py#L27) | 27 | `"def test_plan_validation_caps_queries_and_rejects_non_string_values():"` | — |
| [SRC-6BF96689A8-L000028](../../tests/test_research.py#L28) | 28 | `"    candidate = {"` | — |
| [SRC-6BF96689A8-L000029](../../tests/test_research.py#L29) | 29 | `"        \"queries\": [\"بحث أ\", \"بحث ب\", None, \"بحث ج\", \"بحث د\", \"بحث هـ\", \"بحث سادس\", \"بحث سابع\", \"بحث ثامن\", \"بحث تاسع\"],"` | — |
| [SRC-6BF96689A8-L000030](../../tests/test_research.py#L30) | 30 | `"        \"social_focus\": True,"` | — |
| [SRC-6BF96689A8-L000031](../../tests/test_research.py#L31) | 31 | `"        \"freshness\": \"current\","` | — |
| [SRC-6BF96689A8-L000032](../../tests/test_research.py#L32) | 32 | `"        \"depth\": \"deep\","` | — |
| [SRC-6BF96689A8-L000033](../../tests/test_research.py#L33) | 33 | `"        \"platforms\": [\"reddit\", \"unknown\"],"` | — |
| [SRC-6BF96689A8-L000034](../../tests/test_research.py#L34) | 34 | `"    }"` | — |
| [SRC-6BF96689A8-L000035](../../tests/test_research.py#L35) | 35 | `"    plan = validate_plan(candidate, \"بحث عن منشورات\")"` | — |
| [SRC-6BF96689A8-L000036](../../tests/test_research.py#L36) | 36 | `"    assert len(plan[\"queries\"]) <= 8"` | — |
| [SRC-6BF96689A8-L000037](../../tests/test_research.py#L37) | 37 | `"    assert \"unknown\" not in plan[\"platforms\"]"` | — |
| [SRC-6BF96689A8-L000038](../../tests/test_research.py#L38) | 38 | `"    assert plan[\"social_focus\"] is True"` | — |
| [SRC-6BF96689A8-L000039](../../tests/test_research.py#L39) | 39 | `"    assert plan[\"freshness\"] == \"current\""` | — |
| [SRC-6BF96689A8-L000040](../../tests/test_research.py#L40) | 40 | `""` | — |
| [SRC-6BF96689A8-L000041](../../tests/test_research.py#L41) | 41 | `""` | — |
| [SRC-6BF96689A8-L000042](../../tests/test_research.py#L42) | 42 | `"def test_rank_fusion_promotes_cross_provider_consensus_and_deduplicates():"` | — |
| [SRC-6BF96689A8-L000043](../../tests/test_research.py#L43) | 43 | `"    batches = ["` | — |
| [SRC-6BF96689A8-L000044](../../tests/test_research.py#L44) | 44 | `"        {"` | — |
| [SRC-6BF96689A8-L000045](../../tests/test_research.py#L45) | 45 | `"            \"query\": \"cars Egypt\","` | — |
| [SRC-6BF96689A8-L000046](../../tests/test_research.py#L46) | 46 | `"            \"provider\": \"ddg\","` | — |
| [SRC-6BF96689A8-L000047](../../tests/test_research.py#L47) | 47 | `"            \"results\": ["` | — |
| [SRC-6BF96689A8-L000048](../../tests/test_research.py#L48) | 48 | `"                {\"title\": \"A\", \"url\": \"https://www.example.com/a?utm_source=x\", \"snippet\": \"A\"},"` | — |
| [SRC-6BF96689A8-L000049](../../tests/test_research.py#L49) | 49 | `"                {\"title\": \"B\", \"url\": \"https://example.com/b\", \"snippet\": \"B\"},"` | — |
| [SRC-6BF96689A8-L000050](../../tests/test_research.py#L50) | 50 | `"            ],"` | — |
| [SRC-6BF96689A8-L000051](../../tests/test_research.py#L51) | 51 | `"        },"` | — |
| [SRC-6BF96689A8-L000052](../../tests/test_research.py#L52) | 52 | `"        {"` | — |
| [SRC-6BF96689A8-L000053](../../tests/test_research.py#L53) | 53 | `"            \"query\": \"electric vehicles Egypt\","` | — |
| [SRC-6BF96689A8-L000054](../../tests/test_research.py#L54) | 54 | `"            \"provider\": \"bing\","` | — |
| [SRC-6BF96689A8-L000055](../../tests/test_research.py#L55) | 55 | `"            \"results\": ["` | — |
| [SRC-6BF96689A8-L000056](../../tests/test_research.py#L56) | 56 | `"                {\"title\": \"A better title\", \"url\": \"https://example.com/a\", \"snippet\": \"Longer evidence snippet\"},"` | — |
| [SRC-6BF96689A8-L000057](../../tests/test_research.py#L57) | 57 | `"                {\"title\": \"C\", \"url\": \"https://example.com/c\", \"snippet\": \"C\"},"` | — |
| [SRC-6BF96689A8-L000058](../../tests/test_research.py#L58) | 58 | `"            ],"` | — |
| [SRC-6BF96689A8-L000059](../../tests/test_research.py#L59) | 59 | `"        },"` | — |
| [SRC-6BF96689A8-L000060](../../tests/test_research.py#L60) | 60 | `"    ]"` | — |
| [SRC-6BF96689A8-L000061](../../tests/test_research.py#L61) | 61 | `"    ranked = fuse_ranked_results(batches)"` | — |
| [SRC-6BF96689A8-L000062](../../tests/test_research.py#L62) | 62 | `"    urls = [source[\"url\"] for source in ranked]"` | — |
| [SRC-6BF96689A8-L000063](../../tests/test_research.py#L63) | 63 | `"    assert len(urls) == 3"` | — |
| [SRC-6BF96689A8-L000064](../../tests/test_research.py#L64) | 64 | `"    source_a = next(source for source in ranked if \"example.com/a\" in source[\"url\"])"` | — |
| [SRC-6BF96689A8-L000065](../../tests/test_research.py#L65) | 65 | `"    assert len(source_a[\"providers\"]) == 2"` | — |
| [SRC-6BF96689A8-L000066](../../tests/test_research.py#L66) | 66 | `"    assert len(source_a[\"queries\"]) == 2"` | — |
| [SRC-6BF96689A8-L000067](../../tests/test_research.py#L67) | 67 | `"    assert source_a[\"rank_score\"] > next("` | — |
| [SRC-6BF96689A8-L000068](../../tests/test_research.py#L68) | 68 | `"        source[\"rank_score\"] for source in ranked if \"example.com/c\" in source[\"url\"]"` | — |
| [SRC-6BF96689A8-L000069](../../tests/test_research.py#L69) | 69 | `"    )"` | — |
| [SRC-6BF96689A8-L000070](../../tests/test_research.py#L70) | 70 | `""` | — |
| [SRC-6BF96689A8-L000071](../../tests/test_research.py#L71) | 71 | `""` | — |
| [SRC-6BF96689A8-L000072](../../tests/test_research.py#L72) | 72 | `"def test_source_classification_distinguishes_social_and_government():"` | — |
| [SRC-6BF96689A8-L000073](../../tests/test_research.py#L73) | 73 | `"    from agents.research import classify_source"` | — |
| [SRC-6BF96689A8-L000074](../../tests/test_research.py#L74) | 74 | `""` | — |
| [SRC-6BF96689A8-L000075](../../tests/test_research.py#L75) | 75 | `"    assert classify_source(\"https://www.reddit.com/r/example/comments/1\")[\"platform\"] == \"reddit\""` | — |
| [SRC-6BF96689A8-L000076](../../tests/test_research.py#L76) | 76 | `"    assert classify_source(\"https://example.gov.eg/page\")[\"source_class\"] == \"government\""` | — |
| [SRC-6BF96689A8-L000077](../../tests/test_research.py#L77) | 77 | `""` | — |
| [SRC-6BF96689A8-L000078](../../tests/test_research.py#L78) | 78 | `""` | — |
| [SRC-6BF96689A8-L000079](../../tests/test_research.py#L79) | 79 | `"def test_explicit_page_urls_are_extracted_and_not_left_in_search_terms():"` | — |
| [SRC-6BF96689A8-L000080](../../tests/test_research.py#L80) | 80 | `"    from agents.research import extract_urls"` | — |
| [SRC-6BF96689A8-L000081](../../tests/test_research.py#L81) | 81 | `""` | — |
| [SRC-6BF96689A8-L000082](../../tests/test_research.py#L82) | 82 | `"    question = \"حلل هذه الصفحة بالتفصيل https://example.com/a?utm_source=chat#section.\""` | — |
| [SRC-6BF96689A8-L000083](../../tests/test_research.py#L83) | 83 | `"    plan = fallback_plan(question)"` | — |
| [SRC-6BF96689A8-L000084](../../tests/test_research.py#L84) | 84 | `"    assert extract_urls(question) == [\"https://example.com/a?utm_source=chat#section\"]"` | — |
| [SRC-6BF96689A8-L000085](../../tests/test_research.py#L85) | 85 | `"    assert plan[\"direct_urls\"] == [\"https://example.com/a?utm_source=chat#section\"]"` | — |
| [SRC-6BF96689A8-L000086](../../tests/test_research.py#L86) | 86 | `"    assert \"https://\" not in plan[\"queries\"][0]"` | — |
| [SRC-6BF96689A8-L000087](../../tests/test_research.py#L87) | 87 | `""` | — |
| [SRC-6BF96689A8-L000088](../../tests/test_research.py#L88) | 88 | `"def test_registrable_domain_groups_subdomains_and_respects_public_suffixes():"` | — |
| [SRC-6BF96689A8-L000089](../../tests/test_research.py#L89) | 89 | `"    assert registrable_domain(\"news.example.com\") == \"example.com\""` | — |
| [SRC-6BF96689A8-L000090](../../tests/test_research.py#L90) | 90 | `"    assert registrable_domain(\"offers.example.com\") == \"example.com\""` | — |
| [SRC-6BF96689A8-L000091](../../tests/test_research.py#L91) | 91 | `"    assert registrable_domain(\"news.example.co.uk\") == \"example.co.uk\""` | — |
| [SRC-6BF96689A8-L000092](../../tests/test_research.py#L92) | 92 | `"    assert registrable_domain(\"other.co.uk\") == \"other.co.uk\""` | — |
| [SRC-6BF96689A8-L000093](../../tests/test_research.py#L93) | 93 | `"    assert registrable_domain(\"alice.github.io\") == \"alice.github.io\""` | — |
| [SRC-6BF96689A8-L000094](../../tests/test_research.py#L94) | 94 | `"    assert registrable_domain(\"https://www.example.com/path\") == \"example.com\""` | — |
| [SRC-6BF96689A8-L000095](../../tests/test_research.py#L95) | 95 | `""` | — |
| [SRC-6BF96689A8-L000096](../../tests/test_research.py#L96) | 96 | `""` | — |
| [SRC-6BF96689A8-L000097](../../tests/test_research.py#L97) | 97 | `"def test_evidence_coverage_does_not_count_sibling_subdomains_as_independent():"` | — |
| [SRC-6BF96689A8-L000098](../../tests/test_research.py#L98) | 98 | `"    report = evidence_signal_report(["` | — |
| [SRC-6BF96689A8-L000099](../../tests/test_research.py#L99) | 99 | `"        {"` | — |
| [SRC-6BF96689A8-L000100](../../tests/test_research.py#L100) | 100 | `"            \"url\": \"https://news.example.com/story\","` | — |
| [SRC-6BF96689A8-L000101](../../tests/test_research.py#L101) | 101 | `"            \"domain\": \"news.example.com\","` | — |
| [SRC-6BF96689A8-L000102](../../tests/test_research.py#L102) | 102 | `"            \"providers\": [\"search_a\"],"` | — |
| [SRC-6BF96689A8-L000103](../../tests/test_research.py#L103) | 103 | `"        },"` | — |
| [SRC-6BF96689A8-L000104](../../tests/test_research.py#L104) | 104 | `"        {"` | — |
| [SRC-6BF96689A8-L000105](../../tests/test_research.py#L105) | 105 | `"            \"url\": \"https://offers.example.com/second-story\","` | — |
| [SRC-6BF96689A8-L000106](../../tests/test_research.py#L106) | 106 | `"            \"domain\": \"offers.example.com\","` | — |
| [SRC-6BF96689A8-L000107](../../tests/test_research.py#L107) | 107 | `"            \"providers\": [\"search_b\"],"` | — |
| [SRC-6BF96689A8-L000108](../../tests/test_research.py#L108) | 108 | `"        },"` | — |
| [SRC-6BF96689A8-L000109](../../tests/test_research.py#L109) | 109 | `"    ])"` | — |
| [SRC-6BF96689A8-L000110](../../tests/test_research.py#L110) | 110 | `"    assert report[\"unique_domains\"] == 1"` | — |
| [SRC-6BF96689A8-L000111](../../tests/test_research.py#L111) | 111 | `"    assert report[\"coverage_level\"] == \"محدود\""` | — |
## اختبارات

### FILE-01E35ABC46 — [tests/test_research_guardrails.py](../../tests/test_research_guardrails.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-01E35ABC46-L000001](../../tests/test_research_guardrails.py#L1) | 1 | `"\"\"\"Regression and adversarial tests for depth, freshness, relevance, evidence.\"\"\""` | — |
| [SRC-01E35ABC46-L000002](../../tests/test_research_guardrails.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-01E35ABC46-L000003](../../tests/test_research_guardrails.py#L3) | 3 | `""` | — |
| [SRC-01E35ABC46-L000004](../../tests/test_research_guardrails.py#L4) | 4 | `"from agents.research import ("` | — |
| [SRC-01E35ABC46-L000005](../../tests/test_research_guardrails.py#L5) | 5 | `"    decide_evidence_status,"` | — |
| [SRC-01E35ABC46-L000006](../../tests/test_research_guardrails.py#L6) | 6 | `"    detect_depth,"` | — |
| [SRC-01E35ABC46-L000007](../../tests/test_research_guardrails.py#L7) | 7 | `"    detect_freshness,"` | — |
| [SRC-01E35ABC46-L000008](../../tests/test_research_guardrails.py#L8) | 8 | `"    filter_relevant_sources,"` | — |
| [SRC-01E35ABC46-L000009](../../tests/test_research_guardrails.py#L9) | 9 | `"    source_relevance_score,"` | — |
| [SRC-01E35ABC46-L000010](../../tests/test_research_guardrails.py#L10) | 10 | `")"` | — |
| [SRC-01E35ABC46-L000011](../../tests/test_research_guardrails.py#L11) | 11 | `""` | — |
| [SRC-01E35ABC46-L000012](../../tests/test_research_guardrails.py#L12) | 12 | `""` | — |
| [SRC-01E35ABC46-L000013](../../tests/test_research_guardrails.py#L13) | 13 | `"# --- detect_depth -----------------------------------------------------------"` | — |
| [SRC-01E35ABC46-L000014](../../tests/test_research_guardrails.py#L14) | 14 | `""` | — |
| [SRC-01E35ABC46-L000015](../../tests/test_research_guardrails.py#L15) | 15 | `"def test_depth_deep_english_phrases():"` | — |
| [SRC-01E35ABC46-L000016](../../tests/test_research_guardrails.py#L16) | 16 | `"    assert detect_depth(\"Please do a deep research on climate policy\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000017](../../tests/test_research_guardrails.py#L17) | 17 | `"    assert detect_depth(\"in-depth comparison of EV batteries\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000018](../../tests/test_research_guardrails.py#L18) | 18 | `"    assert detect_depth(\"comprehensive analysis of market risks\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000019](../../tests/test_research_guardrails.py#L19) | 19 | `""` | — |
| [SRC-01E35ABC46-L000020](../../tests/test_research_guardrails.py#L20) | 20 | `""` | — |
| [SRC-01E35ABC46-L000021](../../tests/test_research_guardrails.py#L21) | 21 | `"def test_depth_deep_arabic_phrases():"` | — |
| [SRC-01E35ABC46-L000022](../../tests/test_research_guardrails.py#L22) | 22 | `"    assert detect_depth(\"أريد بحث عميق عن الذكاء الاصطناعي\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000023](../../tests/test_research_guardrails.py#L23) | 23 | `"    assert detect_depth(\"قارن بين السيارات الكهربائية والبنزين\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000024](../../tests/test_research_guardrails.py#L24) | 24 | `"    assert detect_depth(\"بحث شامل بالتفصيل عن الذهب\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000025](../../tests/test_research_guardrails.py#L25) | 25 | `""` | — |
| [SRC-01E35ABC46-L000026](../../tests/test_research_guardrails.py#L26) | 26 | `""` | — |
| [SRC-01E35ABC46-L000027](../../tests/test_research_guardrails.py#L27) | 27 | `"def test_depth_standard_ordinary_questions():"` | — |
| [SRC-01E35ABC46-L000028](../../tests/test_research_guardrails.py#L28) | 28 | `"    assert detect_depth(\"what is the capital of France\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000029](../../tests/test_research_guardrails.py#L29) | 29 | `"    assert detect_depth(\"ما عاصمة مصر\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000030](../../tests/test_research_guardrails.py#L30) | 30 | `"    assert detect_depth(\"I know about electric cars\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000031](../../tests/test_research_guardrails.py#L31) | 31 | `"    assert detect_depth(\"hello\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000032](../../tests/test_research_guardrails.py#L32) | 32 | `"    assert detect_depth(\"\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000033](../../tests/test_research_guardrails.py#L33) | 33 | `""` | — |
| [SRC-01E35ABC46-L000034](../../tests/test_research_guardrails.py#L34) | 34 | `""` | — |
| [SRC-01E35ABC46-L000035](../../tests/test_research_guardrails.py#L35) | 35 | `"def test_depth_does_not_trigger_on_partial_words():"` | — |
| [SRC-01E35ABC46-L000036](../../tests/test_research_guardrails.py#L36) | 36 | `"    # \"sources\" is a deep term; ensure isolated ordinary use still works via whole-word"` | — |
| [SRC-01E35ABC46-L000037](../../tests/test_research_guardrails.py#L37) | 37 | `"    assert detect_depth(\"the river sources of the Nile\") in {\"deep\", \"standard\"}  # may match"` | — |
| [SRC-01E35ABC46-L000038](../../tests/test_research_guardrails.py#L38) | 38 | `"    assert detect_depth(\"tell me a joke\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000039](../../tests/test_research_guardrails.py#L39) | 39 | `""` | — |
| [SRC-01E35ABC46-L000040](../../tests/test_research_guardrails.py#L40) | 40 | `""` | — |
| [SRC-01E35ABC46-L000041](../../tests/test_research_guardrails.py#L41) | 41 | `"# --- detect_freshness -------------------------------------------------------"` | — |
| [SRC-01E35ABC46-L000042](../../tests/test_research_guardrails.py#L42) | 42 | `""` | — |
| [SRC-01E35ABC46-L000043](../../tests/test_research_guardrails.py#L43) | 43 | `"def test_freshness_positive_english():"` | — |
| [SRC-01E35ABC46-L000044](../../tests/test_research_guardrails.py#L44) | 44 | `"    assert detect_freshness(\"what is happening now\") is True"` | — |
| [SRC-01E35ABC46-L000045](../../tests/test_research_guardrails.py#L45) | 45 | `"    assert detect_freshness(\"latest news about Egypt\") is True"` | — |
| [SRC-01E35ABC46-L000046](../../tests/test_research_guardrails.py#L46) | 46 | `"    assert detect_freshness(\"price today of gold\") is True"` | — |
| [SRC-01E35ABC46-L000047](../../tests/test_research_guardrails.py#L47) | 47 | `"    assert detect_freshness(\"breaking news\") is True"` | — |
| [SRC-01E35ABC46-L000048](../../tests/test_research_guardrails.py#L48) | 48 | `""` | — |
| [SRC-01E35ABC46-L000049](../../tests/test_research_guardrails.py#L49) | 49 | `""` | — |
| [SRC-01E35ABC46-L000050](../../tests/test_research_guardrails.py#L50) | 50 | `"def test_freshness_positive_arabic():"` | — |
| [SRC-01E35ABC46-L000051](../../tests/test_research_guardrails.py#L51) | 51 | `"    assert detect_freshness(\"ما هي آخر الأخبار عن الذهب\") is True"` | — |
| [SRC-01E35ABC46-L000052](../../tests/test_research_guardrails.py#L52) | 52 | `"    assert detect_freshness(\"سعر اليوم للدولار\") is True"` | — |
| [SRC-01E35ABC46-L000053](../../tests/test_research_guardrails.py#L53) | 53 | `"    assert detect_freshness(\"مستجدات السوق حاليا\") is True"` | — |
| [SRC-01E35ABC46-L000054](../../tests/test_research_guardrails.py#L54) | 54 | `""` | — |
| [SRC-01E35ABC46-L000055](../../tests/test_research_guardrails.py#L55) | 55 | `""` | — |
| [SRC-01E35ABC46-L000056](../../tests/test_research_guardrails.py#L56) | 56 | `"def test_freshness_negative_know_and_snowden():"` | — |
| [SRC-01E35ABC46-L000057](../../tests/test_research_guardrails.py#L57) | 57 | `"    assert detect_freshness(\"I know about cars\") is False"` | — |
| [SRC-01E35ABC46-L000058](../../tests/test_research_guardrails.py#L58) | 58 | `"    assert detect_freshness(\"Snowden revelations summary\") is False"` | — |
| [SRC-01E35ABC46-L000059](../../tests/test_research_guardrails.py#L59) | 59 | `"    assert detect_freshness(\"knowledge graph basics\") is False"` | — |
| [SRC-01E35ABC46-L000060](../../tests/test_research_guardrails.py#L60) | 60 | `"    assert detect_freshness(\"ما عاصمة فرنسا\") is False"` | — |
| [SRC-01E35ABC46-L000061](../../tests/test_research_guardrails.py#L61) | 61 | `""` | — |
| [SRC-01E35ABC46-L000062](../../tests/test_research_guardrails.py#L62) | 62 | `""` | — |
| [SRC-01E35ABC46-L000063](../../tests/test_research_guardrails.py#L63) | 63 | `"# --- relevance gate ---------------------------------------------------------"` | — |
| [SRC-01E35ABC46-L000064](../../tests/test_research_guardrails.py#L64) | 64 | `""` | — |
| [SRC-01E35ABC46-L000065](../../tests/test_research_guardrails.py#L65) | 65 | `"def test_relevance_keeps_matching_source():"` | — |
| [SRC-01E35ABC46-L000066](../../tests/test_research_guardrails.py#L66) | 66 | `"    src = {"` | — |
| [SRC-01E35ABC46-L000067](../../tests/test_research_guardrails.py#L67) | 67 | `"        \"title\": \"أسعار السيارات الكهربائية في مصر 2026\","` | — |
| [SRC-01E35ABC46-L000068](../../tests/test_research_guardrails.py#L68) | 68 | `"        \"url\": \"https://example.com/ev-egypt\","` | — |
| [SRC-01E35ABC46-L000069](../../tests/test_research_guardrails.py#L69) | 69 | `"        \"snippet\": \"ارتفعت حصة السيارات الكهربائية في السوق المصري هذا العام.\","` | — |
| [SRC-01E35ABC46-L000070](../../tests/test_research_guardrails.py#L70) | 70 | `"        \"domain\": \"example.com\","` | — |
| [SRC-01E35ABC46-L000071](../../tests/test_research_guardrails.py#L71) | 71 | `"        \"source_class\": \"general\","` | — |
| [SRC-01E35ABC46-L000072](../../tests/test_research_guardrails.py#L72) | 72 | `"        \"providers\": [\"ddg\"],"` | — |
| [SRC-01E35ABC46-L000073](../../tests/test_research_guardrails.py#L73) | 73 | `"    }"` | — |
| [SRC-01E35ABC46-L000074](../../tests/test_research_guardrails.py#L74) | 74 | `"    rel = source_relevance_score(src, \"أسعار السيارات الكهربائية في مصر\")"` | — |
| [SRC-01E35ABC46-L000075](../../tests/test_research_guardrails.py#L75) | 75 | `"    assert rel[\"accepted\"] is True"` | — |
| [SRC-01E35ABC46-L000076](../../tests/test_research_guardrails.py#L76) | 76 | `"    assert rel[\"score\"] >= 18"` | — |
| [SRC-01E35ABC46-L000077](../../tests/test_research_guardrails.py#L77) | 77 | `""` | — |
| [SRC-01E35ABC46-L000078](../../tests/test_research_guardrails.py#L78) | 78 | `"    # English-English match"` | — |
| [SRC-01E35ABC46-L000079](../../tests/test_research_guardrails.py#L79) | 79 | `"    src_en = {"` | — |
| [SRC-01E35ABC46-L000080](../../tests/test_research_guardrails.py#L80) | 80 | `"        \"title\": \"Electric vehicles in Egypt 2026\","` | — |
| [SRC-01E35ABC46-L000081](../../tests/test_research_guardrails.py#L81) | 81 | `"        \"url\": \"https://example.com/ev-egypt-en\","` | — |
| [SRC-01E35ABC46-L000082](../../tests/test_research_guardrails.py#L82) | 82 | `"        \"snippet\": \"Market share of electric cars in Egypt rose this year.\","` | — |
| [SRC-01E35ABC46-L000083](../../tests/test_research_guardrails.py#L83) | 83 | `"        \"domain\": \"example.com\","` | — |
| [SRC-01E35ABC46-L000084](../../tests/test_research_guardrails.py#L84) | 84 | `"        \"source_class\": \"general\","` | — |
| [SRC-01E35ABC46-L000085](../../tests/test_research_guardrails.py#L85) | 85 | `"        \"providers\": [\"ddg\"],"` | — |
| [SRC-01E35ABC46-L000086](../../tests/test_research_guardrails.py#L86) | 86 | `"    }"` | — |
| [SRC-01E35ABC46-L000087](../../tests/test_research_guardrails.py#L87) | 87 | `"    rel_en = source_relevance_score(src_en, \"electric vehicles Egypt market share\")"` | — |
| [SRC-01E35ABC46-L000088](../../tests/test_research_guardrails.py#L88) | 88 | `"    assert rel_en[\"accepted\"] is True"` | — |
| [SRC-01E35ABC46-L000089](../../tests/test_research_guardrails.py#L89) | 89 | `""` | — |
| [SRC-01E35ABC46-L000090](../../tests/test_research_guardrails.py#L90) | 90 | `""` | — |
| [SRC-01E35ABC46-L000091](../../tests/test_research_guardrails.py#L91) | 91 | `"def test_relevance_rejects_unrelated():"` | — |
| [SRC-01E35ABC46-L000092](../../tests/test_research_guardrails.py#L92) | 92 | `"    src = {"` | — |
| [SRC-01E35ABC46-L000093](../../tests/test_research_guardrails.py#L93) | 93 | `"        \"title\": \"Best pasta recipes\","` | — |
| [SRC-01E35ABC46-L000094](../../tests/test_research_guardrails.py#L94) | 94 | `"        \"url\": \"https://cooking.example/pasta\","` | — |
| [SRC-01E35ABC46-L000095](../../tests/test_research_guardrails.py#L95) | 95 | `"        \"snippet\": \"How to make carbonara at home with eggs and cheese.\","` | — |
| [SRC-01E35ABC46-L000096](../../tests/test_research_guardrails.py#L96) | 96 | `"        \"domain\": \"cooking.example\","` | — |
| [SRC-01E35ABC46-L000097](../../tests/test_research_guardrails.py#L97) | 97 | `"        \"source_class\": \"general\","` | — |
| [SRC-01E35ABC46-L000098](../../tests/test_research_guardrails.py#L98) | 98 | `"        \"providers\": [\"bing\"],"` | — |
| [SRC-01E35ABC46-L000099](../../tests/test_research_guardrails.py#L99) | 99 | `"    }"` | — |
| [SRC-01E35ABC46-L000100](../../tests/test_research_guardrails.py#L100) | 100 | `"    rel = source_relevance_score(src, \"أسعار السيارات الكهربائية في مصر\")"` | — |
| [SRC-01E35ABC46-L000101](../../tests/test_research_guardrails.py#L101) | 101 | `"    assert rel[\"accepted\"] is False"` | — |
| [SRC-01E35ABC46-L000102](../../tests/test_research_guardrails.py#L102) | 102 | `""` | — |
| [SRC-01E35ABC46-L000103](../../tests/test_research_guardrails.py#L103) | 103 | `""` | — |
| [SRC-01E35ABC46-L000104](../../tests/test_research_guardrails.py#L104) | 104 | `"def test_relevance_keeps_official_despite_wording():"` | — |
| [SRC-01E35ABC46-L000105](../../tests/test_research_guardrails.py#L105) | 105 | `"    src = {"` | — |
| [SRC-01E35ABC46-L000106](../../tests/test_research_guardrails.py#L106) | 106 | `"        \"title\": \"Official statistical bulletin Q1\","` | — |
| [SRC-01E35ABC46-L000107](../../tests/test_research_guardrails.py#L107) | 107 | `"        \"url\": \"https://www.capmas.gov.eg/bulletin\","` | — |
| [SRC-01E35ABC46-L000108](../../tests/test_research_guardrails.py#L108) | 108 | `"        \"snippet\": \"National statistics release.\","` | — |
| [SRC-01E35ABC46-L000109](../../tests/test_research_guardrails.py#L109) | 109 | `"        \"domain\": \"capmas.gov.eg\","` | — |
| [SRC-01E35ABC46-L000110](../../tests/test_research_guardrails.py#L110) | 110 | `"        \"source_class\": \"government\","` | — |
| [SRC-01E35ABC46-L000111](../../tests/test_research_guardrails.py#L111) | 111 | `"        \"providers\": [\"ddg\"],"` | — |
| [SRC-01E35ABC46-L000112](../../tests/test_research_guardrails.py#L112) | 112 | `"    }"` | — |
| [SRC-01E35ABC46-L000113](../../tests/test_research_guardrails.py#L113) | 113 | `"    rel = source_relevance_score(src, \"أسعار السيارات الكهربائية في مصر\")"` | — |
| [SRC-01E35ABC46-L000114](../../tests/test_research_guardrails.py#L114) | 114 | `"    assert rel[\"accepted\"] is True"` | — |
| [SRC-01E35ABC46-L000115](../../tests/test_research_guardrails.py#L115) | 115 | `"    assert rel[\"reason\"] in {\"accepted\", \"kept_official_despite_low_overlap\"}"` | — |
| [SRC-01E35ABC46-L000116](../../tests/test_research_guardrails.py#L116) | 116 | `""` | — |
| [SRC-01E35ABC46-L000117](../../tests/test_research_guardrails.py#L117) | 117 | `""` | — |
| [SRC-01E35ABC46-L000118](../../tests/test_research_guardrails.py#L118) | 118 | `"def test_filter_deduplicates():"` | — |
| [SRC-01E35ABC46-L000119](../../tests/test_research_guardrails.py#L119) | 119 | `"    sources = ["` | — |
| [SRC-01E35ABC46-L000120](../../tests/test_research_guardrails.py#L120) | 120 | `"        {"` | — |
| [SRC-01E35ABC46-L000121](../../tests/test_research_guardrails.py#L121) | 121 | `"            \"title\": \"Same Article Title\","` | — |
| [SRC-01E35ABC46-L000122](../../tests/test_research_guardrails.py#L122) | 122 | `"            \"url\": \"https://a.example/1\","` | — |
| [SRC-01E35ABC46-L000123](../../tests/test_research_guardrails.py#L123) | 123 | `"            \"snippet\": \"electric vehicles Egypt market\","` | — |
| [SRC-01E35ABC46-L000124](../../tests/test_research_guardrails.py#L124) | 124 | `"            \"domain\": \"a.example\","` | — |
| [SRC-01E35ABC46-L000125](../../tests/test_research_guardrails.py#L125) | 125 | `"            \"source_class\": \"general\","` | — |
| [SRC-01E35ABC46-L000126](../../tests/test_research_guardrails.py#L126) | 126 | `"            \"providers\": [\"ddg\"],"` | — |
| [SRC-01E35ABC46-L000127](../../tests/test_research_guardrails.py#L127) | 127 | `"        },"` | — |
| [SRC-01E35ABC46-L000128](../../tests/test_research_guardrails.py#L128) | 128 | `"        {"` | — |
| [SRC-01E35ABC46-L000129](../../tests/test_research_guardrails.py#L129) | 129 | `"            \"title\": \"Same Article Title\","` | — |
| [SRC-01E35ABC46-L000130](../../tests/test_research_guardrails.py#L130) | 130 | `"            \"url\": \"https://a.example/1?utm=x\","` | — |
| [SRC-01E35ABC46-L000131](../../tests/test_research_guardrails.py#L131) | 131 | `"            \"snippet\": \"electric vehicles Egypt market again\","` | — |
| [SRC-01E35ABC46-L000132](../../tests/test_research_guardrails.py#L132) | 132 | `"            \"domain\": \"a.example\","` | — |
| [SRC-01E35ABC46-L000133](../../tests/test_research_guardrails.py#L133) | 133 | `"            \"source_class\": \"general\","` | — |
| [SRC-01E35ABC46-L000134](../../tests/test_research_guardrails.py#L134) | 134 | `"            \"providers\": [\"bing\"],"` | — |
| [SRC-01E35ABC46-L000135](../../tests/test_research_guardrails.py#L135) | 135 | `"        },"` | — |
| [SRC-01E35ABC46-L000136](../../tests/test_research_guardrails.py#L136) | 136 | `"    ]"` | — |
| [SRC-01E35ABC46-L000137](../../tests/test_research_guardrails.py#L137) | 137 | `"    kept, diag = filter_relevant_sources("` | — |
| [SRC-01E35ABC46-L000138](../../tests/test_research_guardrails.py#L138) | 138 | `"        sources, \"electric vehicles Egypt\", [\"electric vehicles Egypt\"]"` | — |
| [SRC-01E35ABC46-L000139](../../tests/test_research_guardrails.py#L139) | 139 | `"    )"` | — |
| [SRC-01E35ABC46-L000140](../../tests/test_research_guardrails.py#L140) | 140 | `"    assert len(kept) == 1"` | — |
| [SRC-01E35ABC46-L000141](../../tests/test_research_guardrails.py#L141) | 141 | `"    assert any(d[\"reason\"] == \"duplicate_title_domain\" for d in diag)"` | — |
| [SRC-01E35ABC46-L000142](../../tests/test_research_guardrails.py#L142) | 142 | `""` | — |
| [SRC-01E35ABC46-L000143](../../tests/test_research_guardrails.py#L143) | 143 | `""` | — |
| [SRC-01E35ABC46-L000144](../../tests/test_research_guardrails.py#L144) | 144 | `"def test_filter_empty_and_failed_extract():"` | — |
| [SRC-01E35ABC46-L000145](../../tests/test_research_guardrails.py#L145) | 145 | `"    kept, diag = filter_relevant_sources([], \"anything\")"` | — |
| [SRC-01E35ABC46-L000146](../../tests/test_research_guardrails.py#L146) | 146 | `"    assert kept == []"` | — |
| [SRC-01E35ABC46-L000147](../../tests/test_research_guardrails.py#L147) | 147 | `"    assert diag == []"` | — |
| [SRC-01E35ABC46-L000148](../../tests/test_research_guardrails.py#L148) | 148 | `"    src = {"` | — |
| [SRC-01E35ABC46-L000149](../../tests/test_research_guardrails.py#L149) | 149 | `"        \"title\": \"\","` | — |
| [SRC-01E35ABC46-L000150](../../tests/test_research_guardrails.py#L150) | 150 | `"        \"url\": \"https://example.com/x\","` | — |
| [SRC-01E35ABC46-L000151](../../tests/test_research_guardrails.py#L151) | 151 | `"        \"snippet\": \"\","` | — |
| [SRC-01E35ABC46-L000152](../../tests/test_research_guardrails.py#L152) | 152 | `"        \"page_text\": \"\","` | — |
| [SRC-01E35ABC46-L000153](../../tests/test_research_guardrails.py#L153) | 153 | `"        \"domain\": \"example.com\","` | — |
| [SRC-01E35ABC46-L000154](../../tests/test_research_guardrails.py#L154) | 154 | `"        \"source_class\": \"general\","` | — |
| [SRC-01E35ABC46-L000155](../../tests/test_research_guardrails.py#L155) | 155 | `"        \"providers\": [\"ddg\"],"` | — |
| [SRC-01E35ABC46-L000156](../../tests/test_research_guardrails.py#L156) | 156 | `"    }"` | — |
| [SRC-01E35ABC46-L000157](../../tests/test_research_guardrails.py#L157) | 157 | `"    _kept2, diag2 = filter_relevant_sources([src], \"unrelated pasta recipes\")"` | — |
| [SRC-01E35ABC46-L000158](../../tests/test_research_guardrails.py#L158) | 158 | `"    # May reject for low overlap"` | — |
| [SRC-01E35ABC46-L000159](../../tests/test_research_guardrails.py#L159) | 159 | `"    assert isinstance(diag2, list)"` | — |
| [SRC-01E35ABC46-L000160](../../tests/test_research_guardrails.py#L160) | 160 | `""` | — |
| [SRC-01E35ABC46-L000161](../../tests/test_research_guardrails.py#L161) | 161 | `""` | — |
| [SRC-01E35ABC46-L000162](../../tests/test_research_guardrails.py#L162) | 162 | `"# --- evidence status --------------------------------------------------------"` | — |
| [SRC-01E35ABC46-L000163](../../tests/test_research_guardrails.py#L163) | 163 | `""` | — |
| [SRC-01E35ABC46-L000164](../../tests/test_research_guardrails.py#L164) | 164 | `"def test_evidence_adequate():"` | — |
| [SRC-01E35ABC46-L000165](../../tests/test_research_guardrails.py#L165) | 165 | `"    sources = ["` | — |
| [SRC-01E35ABC46-L000166](../../tests/test_research_guardrails.py#L166) | 166 | `"        {\"url\": f\"https://a{i}.example/p\", \"domain\": f\"a{i}.example\","` | — |
| [SRC-01E35ABC46-L000167](../../tests/test_research_guardrails.py#L167) | 167 | `"         \"snippet\": \"content\", \"page_fetched\": True, \"source_class\": \"general\"}"` | — |
| [SRC-01E35ABC46-L000168](../../tests/test_research_guardrails.py#L168) | 168 | `"        for i in range(4)"` | — |
| [SRC-01E35ABC46-L000169](../../tests/test_research_guardrails.py#L169) | 169 | `"    ]"` | — |
| [SRC-01E35ABC46-L000170](../../tests/test_research_guardrails.py#L170) | 170 | `"    sources[0][\"source_class\"] = \"government\""` | — |
| [SRC-01E35ABC46-L000171](../../tests/test_research_guardrails.py#L171) | 171 | `"    decision = decide_evidence_status(sources, pages_read=2)"` | — |
| [SRC-01E35ABC46-L000172](../../tests/test_research_guardrails.py#L172) | 172 | `"    assert decision[\"evidence_status\"] == \"adequate\""` | — |
| [SRC-01E35ABC46-L000173](../../tests/test_research_guardrails.py#L173) | 173 | `"    assert decision[\"should_abstain\"] is False"` | — |
| [SRC-01E35ABC46-L000174](../../tests/test_research_guardrails.py#L174) | 174 | `""` | — |
| [SRC-01E35ABC46-L000175](../../tests/test_research_guardrails.py#L175) | 175 | `""` | — |
| [SRC-01E35ABC46-L000176](../../tests/test_research_guardrails.py#L176) | 176 | `"def test_evidence_insufficient_empty():"` | — |
| [SRC-01E35ABC46-L000177](../../tests/test_research_guardrails.py#L177) | 177 | `"    decision = decide_evidence_status([], search_attempted=True)"` | — |
| [SRC-01E35ABC46-L000178](../../tests/test_research_guardrails.py#L178) | 178 | `"    assert decision[\"evidence_status\"] == \"insufficient\""` | — |
| [SRC-01E35ABC46-L000179](../../tests/test_research_guardrails.py#L179) | 179 | `"    assert decision[\"should_abstain\"] is True"` | — |
| [SRC-01E35ABC46-L000180](../../tests/test_research_guardrails.py#L180) | 180 | `""` | — |
| [SRC-01E35ABC46-L000181](../../tests/test_research_guardrails.py#L181) | 181 | `""` | — |
| [SRC-01E35ABC46-L000182](../../tests/test_research_guardrails.py#L182) | 182 | `"def test_evidence_failed_provider():"` | — |
| [SRC-01E35ABC46-L000183](../../tests/test_research_guardrails.py#L183) | 183 | `"    decision = decide_evidence_status([], provider_failures=2, search_attempted=True)"` | — |
| [SRC-01E35ABC46-L000184](../../tests/test_research_guardrails.py#L184) | 184 | `"    assert decision[\"evidence_status\"] == \"failed\""` | — |
| [SRC-01E35ABC46-L000185](../../tests/test_research_guardrails.py#L185) | 185 | `"    assert decision[\"should_abstain\"] is True"` | — |
| [SRC-01E35ABC46-L000186](../../tests/test_research_guardrails.py#L186) | 186 | `""` | — |
| [SRC-01E35ABC46-L000187](../../tests/test_research_guardrails.py#L187) | 187 | `""` | — |
| [SRC-01E35ABC46-L000188](../../tests/test_research_guardrails.py#L188) | 188 | `"def test_evidence_partial_single_source():"` | — |
| [SRC-01E35ABC46-L000189](../../tests/test_research_guardrails.py#L189) | 189 | `"    sources = ["` | — |
| [SRC-01E35ABC46-L000190](../../tests/test_research_guardrails.py#L190) | 190 | `"        {\"url\": \"https://a.example/p\", \"domain\": \"a.example\","` | — |
| [SRC-01E35ABC46-L000191](../../tests/test_research_guardrails.py#L191) | 191 | `"         \"snippet\": \"some text\", \"page_fetched\": True, \"source_class\": \"general\"}"` | — |
| [SRC-01E35ABC46-L000192](../../tests/test_research_guardrails.py#L192) | 192 | `"    ]"` | — |
| [SRC-01E35ABC46-L000193](../../tests/test_research_guardrails.py#L193) | 193 | `"    decision = decide_evidence_status(sources, pages_read=1)"` | — |
| [SRC-01E35ABC46-L000194](../../tests/test_research_guardrails.py#L194) | 194 | `"    assert decision[\"evidence_status\"] == \"partial\""` | — |
| [SRC-01E35ABC46-L000195](../../tests/test_research_guardrails.py#L195) | 195 | `"    assert decision[\"should_abstain\"] is False"` | — |
## اختبارات

### FILE-1C0D3D1206 — [tests/test_sqlite_backup_restore.py](../../tests/test_sqlite_backup_restore.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1C0D3D1206-L000001](../../tests/test_sqlite_backup_restore.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-1C0D3D1206-L000002](../../tests/test_sqlite_backup_restore.py#L2) | 2 | `""` | — |
| [SRC-1C0D3D1206-L000003](../../tests/test_sqlite_backup_restore.py#L3) | 3 | `"import sqlite3"` | — |
| [SRC-1C0D3D1206-L000004](../../tests/test_sqlite_backup_restore.py#L4) | 4 | `""` | — |
| [SRC-1C0D3D1206-L000005](../../tests/test_sqlite_backup_restore.py#L5) | 5 | `"import pytest"` | — |
| [SRC-1C0D3D1206-L000006](../../tests/test_sqlite_backup_restore.py#L6) | 6 | `""` | — |
| [SRC-1C0D3D1206-L000007](../../tests/test_sqlite_backup_restore.py#L7) | 7 | `"from agents.omarai import LeadStore"` | — |
| [SRC-1C0D3D1206-L000008](../../tests/test_sqlite_backup_restore.py#L8) | 8 | `"from scripts.sqlite_backup_restore import BackupError, backup_database, restore_database"` | — |
| [SRC-1C0D3D1206-L000009](../../tests/test_sqlite_backup_restore.py#L9) | 9 | `""` | — |
| [SRC-1C0D3D1206-L000010](../../tests/test_sqlite_backup_restore.py#L10) | 10 | `""` | — |
| [SRC-1C0D3D1206-L000011](../../tests/test_sqlite_backup_restore.py#L11) | 11 | `"def test_backup_and_restore_preserve_omarai_leads(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000012](../../tests/test_sqlite_backup_restore.py#L12) | 12 | `"    source_path = tmp_path / \"live.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000013](../../tests/test_sqlite_backup_restore.py#L13) | 13 | `"    source = LeadStore(source_path)"` | — |
| [SRC-1C0D3D1206-L000014](../../tests/test_sqlite_backup_restore.py#L14) | 14 | `"    first, created_first = source.add("` | — |
| [SRC-1C0D3D1206-L000015](../../tests/test_sqlite_backup_restore.py#L15) | 15 | `"        \"بدور على شقة في التجمع وممكن معاينة\","` | — |
| [SRC-1C0D3D1206-L000016](../../tests/test_sqlite_backup_restore.py#L16) | 16 | `"        \"https://example.com/posts/1\","` | — |
| [SRC-1C0D3D1206-L000017](../../tests/test_sqlite_backup_restore.py#L17) | 17 | `"        platform=\"manual\","` | — |
| [SRC-1C0D3D1206-L000018](../../tests/test_sqlite_backup_restore.py#L18) | 18 | `"        note=\"سجل اختبار أول\","` | — |
| [SRC-1C0D3D1206-L000019](../../tests/test_sqlite_backup_restore.py#L19) | 19 | `"    )"` | — |
| [SRC-1C0D3D1206-L000020](../../tests/test_sqlite_backup_restore.py#L20) | 20 | `"    second, created_second = source.add("` | — |
| [SRC-1C0D3D1206-L000021](../../tests/test_sqlite_backup_restore.py#L21) | 21 | `"        \"محتاج شقة للإيجار الشهر القادم\","` | — |
| [SRC-1C0D3D1206-L000022](../../tests/test_sqlite_backup_restore.py#L22) | 22 | `"        \"https://example.com/posts/2\","` | — |
| [SRC-1C0D3D1206-L000023](../../tests/test_sqlite_backup_restore.py#L23) | 23 | `"        platform=\"manual\","` | — |
| [SRC-1C0D3D1206-L000024](../../tests/test_sqlite_backup_restore.py#L24) | 24 | `"        note=\"سجل اختبار ثان\","` | — |
| [SRC-1C0D3D1206-L000025](../../tests/test_sqlite_backup_restore.py#L25) | 25 | `"    )"` | — |
| [SRC-1C0D3D1206-L000026](../../tests/test_sqlite_backup_restore.py#L26) | 26 | `"    assert created_first and created_second"` | — |
| [SRC-1C0D3D1206-L000027](../../tests/test_sqlite_backup_restore.py#L27) | 27 | `"    source.update_status(first[\"id\"], \"qualified\")"` | — |
| [SRC-1C0D3D1206-L000028](../../tests/test_sqlite_backup_restore.py#L28) | 28 | `""` | — |
| [SRC-1C0D3D1206-L000029](../../tests/test_sqlite_backup_restore.py#L29) | 29 | `"    snapshot_path = tmp_path / \"backups\" / \"snapshot.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000030](../../tests/test_sqlite_backup_restore.py#L30) | 30 | `"    backup_report = backup_database(source_path, snapshot_path)"` | — |
| [SRC-1C0D3D1206-L000031](../../tests/test_sqlite_backup_restore.py#L31) | 31 | `"    assert backup_report[\"result\"] == \"passed\""` | — |
| [SRC-1C0D3D1206-L000032](../../tests/test_sqlite_backup_restore.py#L32) | 32 | `"    assert backup_report[\"integrity_check\"] == \"ok\""` | — |
| [SRC-1C0D3D1206-L000033](../../tests/test_sqlite_backup_restore.py#L33) | 33 | `"    assert backup_report[\"lead_count\"] == 2"` | — |
| [SRC-1C0D3D1206-L000034](../../tests/test_sqlite_backup_restore.py#L34) | 34 | `"    assert backup_report[\"overwrite\"] is False"` | — |
| [SRC-1C0D3D1206-L000035](../../tests/test_sqlite_backup_restore.py#L35) | 35 | `""` | — |
| [SRC-1C0D3D1206-L000036](../../tests/test_sqlite_backup_restore.py#L36) | 36 | `"    restored_path = tmp_path / \"restored\" / \"restored.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000037](../../tests/test_sqlite_backup_restore.py#L37) | 37 | `"    restore_report = restore_database(snapshot_path, restored_path)"` | — |
| [SRC-1C0D3D1206-L000038](../../tests/test_sqlite_backup_restore.py#L38) | 38 | `"    assert restore_report[\"result\"] == \"passed\""` | — |
| [SRC-1C0D3D1206-L000039](../../tests/test_sqlite_backup_restore.py#L39) | 39 | `"    assert restore_report[\"integrity_check\"] == \"ok\""` | — |
| [SRC-1C0D3D1206-L000040](../../tests/test_sqlite_backup_restore.py#L40) | 40 | `"    assert restore_report[\"lead_count\"] == 2"` | — |
| [SRC-1C0D3D1206-L000041](../../tests/test_sqlite_backup_restore.py#L41) | 41 | `""` | — |
| [SRC-1C0D3D1206-L000042](../../tests/test_sqlite_backup_restore.py#L42) | 42 | `"    restored = LeadStore(restored_path)"` | — |
| [SRC-1C0D3D1206-L000043](../../tests/test_sqlite_backup_restore.py#L43) | 43 | `"    original_rows = {row[\"id\"]: row for row in source.list(limit=500)}"` | — |
| [SRC-1C0D3D1206-L000044](../../tests/test_sqlite_backup_restore.py#L44) | 44 | `"    restored_rows = {row[\"id\"]: row for row in restored.list(limit=500)}"` | — |
| [SRC-1C0D3D1206-L000045](../../tests/test_sqlite_backup_restore.py#L45) | 45 | `"    assert restored_rows == original_rows"` | — |
| [SRC-1C0D3D1206-L000046](../../tests/test_sqlite_backup_restore.py#L46) | 46 | `"    assert restored_rows[first[\"id\"]][\"status\"] == \"qualified\""` | — |
| [SRC-1C0D3D1206-L000047](../../tests/test_sqlite_backup_restore.py#L47) | 47 | `"    assert second[\"id\"] in restored_rows"` | — |
| [SRC-1C0D3D1206-L000048](../../tests/test_sqlite_backup_restore.py#L48) | 48 | `""` | — |
| [SRC-1C0D3D1206-L000049](../../tests/test_sqlite_backup_restore.py#L49) | 49 | `""` | — |
| [SRC-1C0D3D1206-L000050](../../tests/test_sqlite_backup_restore.py#L50) | 50 | `"def test_backup_never_overwrites_an_existing_destination(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000051](../../tests/test_sqlite_backup_restore.py#L51) | 51 | `"    source_path = tmp_path / \"source.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000052](../../tests/test_sqlite_backup_restore.py#L52) | 52 | `"    LeadStore(source_path)"` | — |
| [SRC-1C0D3D1206-L000053](../../tests/test_sqlite_backup_restore.py#L53) | 53 | `"    destination = tmp_path / \"keep-me.txt\""` | — |
| [SRC-1C0D3D1206-L000054](../../tests/test_sqlite_backup_restore.py#L54) | 54 | `"    destination.write_text(\"do not overwrite\", encoding=\"utf-8\")"` | — |
| [SRC-1C0D3D1206-L000055](../../tests/test_sqlite_backup_restore.py#L55) | 55 | `""` | — |
| [SRC-1C0D3D1206-L000056](../../tests/test_sqlite_backup_restore.py#L56) | 56 | `"    with pytest.raises(FileExistsError):"` | — |
| [SRC-1C0D3D1206-L000057](../../tests/test_sqlite_backup_restore.py#L57) | 57 | `"        backup_database(source_path, destination)"` | — |
| [SRC-1C0D3D1206-L000058](../../tests/test_sqlite_backup_restore.py#L58) | 58 | `""` | — |
| [SRC-1C0D3D1206-L000059](../../tests/test_sqlite_backup_restore.py#L59) | 59 | `"    assert destination.read_text(encoding=\"utf-8\") == \"do not overwrite\""` | — |
| [SRC-1C0D3D1206-L000060](../../tests/test_sqlite_backup_restore.py#L60) | 60 | `""` | — |
| [SRC-1C0D3D1206-L000061](../../tests/test_sqlite_backup_restore.py#L61) | 61 | `""` | — |
| [SRC-1C0D3D1206-L000062](../../tests/test_sqlite_backup_restore.py#L62) | 62 | `"def test_backup_rejects_non_omarai_sqlite_database_without_leaving_destination(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000063](../../tests/test_sqlite_backup_restore.py#L63) | 63 | `"    source_path = tmp_path / \"unrelated.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000064](../../tests/test_sqlite_backup_restore.py#L64) | 64 | `"    with sqlite3.connect(source_path) as db:"` | — |
| [SRC-1C0D3D1206-L000065](../../tests/test_sqlite_backup_restore.py#L65) | 65 | `"        db.execute(\"CREATE TABLE unrelated (value TEXT)\")"` | — |
| [SRC-1C0D3D1206-L000066](../../tests/test_sqlite_backup_restore.py#L66) | 66 | `""` | — |
| [SRC-1C0D3D1206-L000067](../../tests/test_sqlite_backup_restore.py#L67) | 67 | `"    destination = tmp_path / \"should-not-exist.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000068](../../tests/test_sqlite_backup_restore.py#L68) | 68 | `"    with pytest.raises(BackupError, match=\"not an Omarai leads database\"):"` | — |
| [SRC-1C0D3D1206-L000069](../../tests/test_sqlite_backup_restore.py#L69) | 69 | `"        backup_database(source_path, destination)"` | — |
| [SRC-1C0D3D1206-L000070](../../tests/test_sqlite_backup_restore.py#L70) | 70 | `""` | — |
| [SRC-1C0D3D1206-L000071](../../tests/test_sqlite_backup_restore.py#L71) | 71 | `"    assert not destination.exists()"` | — |
| [SRC-1C0D3D1206-L000072](../../tests/test_sqlite_backup_restore.py#L72) | 72 | `""` | — |
| [SRC-1C0D3D1206-L000073](../../tests/test_sqlite_backup_restore.py#L73) | 73 | `""` | — |
| [SRC-1C0D3D1206-L000074](../../tests/test_sqlite_backup_restore.py#L74) | 74 | `"def test_backup_rejects_same_source_and_destination(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000075](../../tests/test_sqlite_backup_restore.py#L75) | 75 | `"    source_path = tmp_path / \"source.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000076](../../tests/test_sqlite_backup_restore.py#L76) | 76 | `"    LeadStore(source_path)"` | — |
| [SRC-1C0D3D1206-L000077](../../tests/test_sqlite_backup_restore.py#L77) | 77 | `""` | — |
| [SRC-1C0D3D1206-L000078](../../tests/test_sqlite_backup_restore.py#L78) | 78 | `"    with pytest.raises(BackupError, match=\"different paths\"):"` | — |
| [SRC-1C0D3D1206-L000079](../../tests/test_sqlite_backup_restore.py#L79) | 79 | `"        backup_database(source_path, source_path)"` | — |
| [SRC-1C0D3D1206-L000080](../../tests/test_sqlite_backup_restore.py#L80) | 80 | `""` | — |
| [SRC-1C0D3D1206-L000081](../../tests/test_sqlite_backup_restore.py#L81) | 81 | `""` | — |
| [SRC-1C0D3D1206-L000082](../../tests/test_sqlite_backup_restore.py#L82) | 82 | `"def test_restore_rejects_corrupt_backup_without_overwriting_source(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000083](../../tests/test_sqlite_backup_restore.py#L83) | 83 | `"    backup_path = tmp_path / \"corrupt.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000084](../../tests/test_sqlite_backup_restore.py#L84) | 84 | `"    backup_path.write_bytes(b\"not a sqlite database\")"` | — |
| [SRC-1C0D3D1206-L000085](../../tests/test_sqlite_backup_restore.py#L85) | 85 | `"    destination = tmp_path / \"restore.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000086](../../tests/test_sqlite_backup_restore.py#L86) | 86 | `""` | — |
| [SRC-1C0D3D1206-L000087](../../tests/test_sqlite_backup_restore.py#L87) | 87 | `"    with pytest.raises(BackupError):"` | — |
| [SRC-1C0D3D1206-L000088](../../tests/test_sqlite_backup_restore.py#L88) | 88 | `"        restore_database(backup_path, destination)"` | — |
| [SRC-1C0D3D1206-L000089](../../tests/test_sqlite_backup_restore.py#L89) | 89 | `""` | — |
| [SRC-1C0D3D1206-L000090](../../tests/test_sqlite_backup_restore.py#L90) | 90 | `"    assert backup_path.read_bytes() == b\"not a sqlite database\""` | — |
| [SRC-1C0D3D1206-L000091](../../tests/test_sqlite_backup_restore.py#L91) | 91 | `"    assert not destination.exists()"` | — |
| [SRC-1C0D3D1206-L000092](../../tests/test_sqlite_backup_restore.py#L92) | 92 | `""` | — |
| [SRC-1C0D3D1206-L000093](../../tests/test_sqlite_backup_restore.py#L93) | 93 | `"def test_backup_rejects_dangling_symlink_destination(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000094](../../tests/test_sqlite_backup_restore.py#L94) | 94 | `"    source_path = tmp_path / \"source.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000095](../../tests/test_sqlite_backup_restore.py#L95) | 95 | `"    LeadStore(source_path)"` | — |
| [SRC-1C0D3D1206-L000096](../../tests/test_sqlite_backup_restore.py#L96) | 96 | `"    target_path = tmp_path / \"target.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000097](../../tests/test_sqlite_backup_restore.py#L97) | 97 | `"    destination_link = tmp_path / \"backup-link.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000098](../../tests/test_sqlite_backup_restore.py#L98) | 98 | `"    destination_link.symlink_to(target_path)"` | — |
| [SRC-1C0D3D1206-L000099](../../tests/test_sqlite_backup_restore.py#L99) | 99 | `""` | — |
| [SRC-1C0D3D1206-L000100](../../tests/test_sqlite_backup_restore.py#L100) | 100 | `"    with pytest.raises(FileExistsError):"` | — |
| [SRC-1C0D3D1206-L000101](../../tests/test_sqlite_backup_restore.py#L101) | 101 | `"        backup_database(source_path, destination_link)"` | — |
| [SRC-1C0D3D1206-L000102](../../tests/test_sqlite_backup_restore.py#L102) | 102 | `""` | — |
| [SRC-1C0D3D1206-L000103](../../tests/test_sqlite_backup_restore.py#L103) | 103 | `"    assert destination_link.is_symlink()"` | — |
| [SRC-1C0D3D1206-L000104](../../tests/test_sqlite_backup_restore.py#L104) | 104 | `"    assert not target_path.exists()"` | — |
| [SRC-1C0D3D1206-L000105](../../tests/test_sqlite_backup_restore.py#L105) | 105 | `""` | — |
## اختبارات

### FILE-F725E90B2A — [tests/test_web_agent.py](../../tests/test_web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-F725E90B2A-L000001](../../tests/test_web_agent.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-F725E90B2A-L000002](../../tests/test_web_agent.py#L2) | 2 | `""` | — |
| [SRC-F725E90B2A-L000003](../../tests/test_web_agent.py#L3) | 3 | `"from pathlib import Path"` | — |
| [SRC-F725E90B2A-L000004](../../tests/test_web_agent.py#L4) | 4 | `""` | — |
| [SRC-F725E90B2A-L000005](../../tests/test_web_agent.py#L5) | 5 | `"import pytest"` | — |
| [SRC-F725E90B2A-L000006](../../tests/test_web_agent.py#L6) | 6 | `""` | — |
| [SRC-F725E90B2A-L000007](../../tests/test_web_agent.py#L7) | 7 | `"from agents.web_agent import ("` | — |
| [SRC-F725E90B2A-L000008](../../tests/test_web_agent.py#L8) | 8 | `"    WebAgent,"` | — |
| [SRC-F725E90B2A-L000009](../../tests/test_web_agent.py#L9) | 9 | `"    _normalize_search_query,"` | — |
| [SRC-F725E90B2A-L000010](../../tests/test_web_agent.py#L10) | 10 | `"    _public_http_url,"` | — |
| [SRC-F725E90B2A-L000011](../../tests/test_web_agent.py#L11) | 11 | `"    _relevance_ratio,"` | — |
| [SRC-F725E90B2A-L000012](../../tests/test_web_agent.py#L12) | 12 | `")"` | — |
| [SRC-F725E90B2A-L000013](../../tests/test_web_agent.py#L13) | 13 | `""` | — |
| [SRC-F725E90B2A-L000014](../../tests/test_web_agent.py#L14) | 14 | `""` | — |
| [SRC-F725E90B2A-L000015](../../tests/test_web_agent.py#L15) | 15 | `"def sample_source(index=0):"` | — |
| [SRC-F725E90B2A-L000016](../../tests/test_web_agent.py#L16) | 16 | `"    domain = \"example.com\" if index == 0 else \"example.net\""` | — |
| [SRC-F725E90B2A-L000017](../../tests/test_web_agent.py#L17) | 17 | `"    return {"` | — |
| [SRC-F725E90B2A-L000018](../../tests/test_web_agent.py#L18) | 18 | `"        \"title\": \"مقالة عن التقنية\","` | — |
| [SRC-F725E90B2A-L000019](../../tests/test_web_agent.py#L19) | 19 | `"        \"url\": f\"https://{domain}/research\","` | — |
| [SRC-F725E90B2A-L000020](../../tests/test_web_agent.py#L20) | 20 | `"        \"snippet\": \"يشرح هذا المصدر التقنية وسبب المقارنة.\","` | — |
| [SRC-F725E90B2A-L000021](../../tests/test_web_agent.py#L21) | 21 | `"        \"page_text\": \"نص مستخرج من الصفحة يشرح التقنية وأسباب المقارنة.\","` | — |
| [SRC-F725E90B2A-L000022](../../tests/test_web_agent.py#L22) | 22 | `"        \"page_fetched\": True,"` | — |
| [SRC-F725E90B2A-L000023](../../tests/test_web_agent.py#L23) | 23 | `"        \"providers\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L000024](../../tests/test_web_agent.py#L24) | 24 | `"        \"queries\": [\"قارن هذه التقنية\"],"` | — |
| [SRC-F725E90B2A-L000025](../../tests/test_web_agent.py#L25) | 25 | `"        \"domain\": domain,"` | — |
| [SRC-F725E90B2A-L000026](../../tests/test_web_agent.py#L26) | 26 | `"        \"source_class\": \"general\","` | — |
| [SRC-F725E90B2A-L000027](../../tests/test_web_agent.py#L27) | 27 | `"        \"platform\": \"web\","` | — |
| [SRC-F725E90B2A-L000028](../../tests/test_web_agent.py#L28) | 28 | `"    }"` | — |
| [SRC-F725E90B2A-L000029](../../tests/test_web_agent.py#L29) | 29 | `""` | — |
| [SRC-F725E90B2A-L000030](../../tests/test_web_agent.py#L30) | 30 | `""` | — |
| [SRC-F725E90B2A-L000031](../../tests/test_web_agent.py#L31) | 31 | `"def test_agent_synthesizes_with_sources_without_live_network(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000032](../../tests/test_web_agent.py#L32) | 32 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000033](../../tests/test_web_agent.py#L33) | 33 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L000034](../../tests/test_web_agent.py#L34) | 34 | `"    seen = {}"` | — |
| [SRC-F725E90B2A-L000035](../../tests/test_web_agent.py#L35) | 35 | `""` | — |
| [SRC-F725E90B2A-L000036](../../tests/test_web_agent.py#L36) | 36 | `"    def plan(question, history):"` | — |
| [SRC-F725E90B2A-L000037](../../tests/test_web_agent.py#L37) | 37 | `"        return {"` | — |
| [SRC-F725E90B2A-L000038](../../tests/test_web_agent.py#L38) | 38 | `"            \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L000039](../../tests/test_web_agent.py#L39) | 39 | `"            \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L000040](../../tests/test_web_agent.py#L40) | 40 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L000041](../../tests/test_web_agent.py#L41) | 41 | `"            \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L000042](../../tests/test_web_agent.py#L42) | 42 | `"            \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L000043](../../tests/test_web_agent.py#L43) | 43 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L000044](../../tests/test_web_agent.py#L44) | 44 | `"        }"` | — |
| [SRC-F725E90B2A-L000045](../../tests/test_web_agent.py#L45) | 45 | `""` | — |
| [SRC-F725E90B2A-L000046](../../tests/test_web_agent.py#L46) | 46 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L000047](../../tests/test_web_agent.py#L47) | 47 | `"        seen[\"plan\"] = research_plan"` | — |
| [SRC-F725E90B2A-L000048](../../tests/test_web_agent.py#L48) | 48 | `"        return [sample_source(0), sample_source(1)], [], {"` | — |
| [SRC-F725E90B2A-L000049](../../tests/test_web_agent.py#L49) | 49 | `"            \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L000050](../../tests/test_web_agent.py#L50) | 50 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L000051](../../tests/test_web_agent.py#L51) | 51 | `"            \"query_results\": [{\"query\": research_plan[\"queries\"][0], \"results\": 1}],"` | — |
| [SRC-F725E90B2A-L000052](../../tests/test_web_agent.py#L52) | 52 | `"            \"unique_sources\": 2,"` | — |
| [SRC-F725E90B2A-L000053](../../tests/test_web_agent.py#L53) | 53 | `"            \"pages_fetched\": 2,"` | — |
| [SRC-F725E90B2A-L000054](../../tests/test_web_agent.py#L54) | 54 | `"            \"providers_used\": [\"test\"],"` | — |
| [SRC-F725E90B2A-L000055](../../tests/test_web_agent.py#L55) | 55 | `"            \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L000056](../../tests/test_web_agent.py#L56) | 56 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L000057](../../tests/test_web_agent.py#L57) | 57 | `"            \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L000058](../../tests/test_web_agent.py#L58) | 58 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L000059](../../tests/test_web_agent.py#L59) | 59 | `"        }"` | — |
| [SRC-F725E90B2A-L000060](../../tests/test_web_agent.py#L60) | 60 | `""` | — |
| [SRC-F725E90B2A-L000061](../../tests/test_web_agent.py#L61) | 61 | `"    def generate(question, history, sources, search_warning, research_plan=None, search_report=None):"` | — |
| [SRC-F725E90B2A-L000062](../../tests/test_web_agent.py#L62) | 62 | `"        seen[\"question\"] = question"` | — |
| [SRC-F725E90B2A-L000063](../../tests/test_web_agent.py#L63) | 63 | `"        seen[\"history\"] = history"` | — |
| [SRC-F725E90B2A-L000064](../../tests/test_web_agent.py#L64) | 64 | `"        seen[\"sources\"] = sources"` | — |
| [SRC-F725E90B2A-L000065](../../tests/test_web_agent.py#L65) | 65 | `"        seen[\"report\"] = search_report"` | — |
| [SRC-F725E90B2A-L000066](../../tests/test_web_agent.py#L66) | 66 | `"        return \"الإجابة: التقنية مناسبة للأسباب التالية [المصدر 1].\""` | — |
| [SRC-F725E90B2A-L000067](../../tests/test_web_agent.py#L67) | 67 | `""` | — |
| [SRC-F725E90B2A-L000068](../../tests/test_web_agent.py#L68) | 68 | `"    monkeypatch.setattr(agent, \"_plan_search\", plan)"` | — |
| [SRC-F725E90B2A-L000069](../../tests/test_web_agent.py#L69) | 69 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L000070](../../tests/test_web_agent.py#L70) | 70 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L000071](../../tests/test_web_agent.py#L71) | 71 | `"    monkeypatch.setattr(agent, \"_generate\", generate)"` | — |
| [SRC-F725E90B2A-L000072](../../tests/test_web_agent.py#L72) | 72 | `"    result = agent.answer("` | — |
| [SRC-F725E90B2A-L000073](../../tests/test_web_agent.py#L73) | 73 | `"        \"قارن هذه التقنية\","` | — |
| [SRC-F725E90B2A-L000074](../../tests/test_web_agent.py#L74) | 74 | `"        history=[{\"role\": \"user\", \"content\": \"ما هي التقنية؟\"}],"` | — |
| [SRC-F725E90B2A-L000075](../../tests/test_web_agent.py#L75) | 75 | `"    )"` | — |
| [SRC-F725E90B2A-L000076](../../tests/test_web_agent.py#L76) | 76 | `""` | — |
| [SRC-F725E90B2A-L000077](../../tests/test_web_agent.py#L77) | 77 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-F725E90B2A-L000078](../../tests/test_web_agent.py#L78) | 78 | `"    assert result[\"search_attempted\"] is True"` | — |
| [SRC-F725E90B2A-L000079](../../tests/test_web_agent.py#L79) | 79 | `"    assert result[\"search_report\"][\"search_attempted\"] is True"` | — |
| [SRC-F725E90B2A-L000080](../../tests/test_web_agent.py#L80) | 80 | `"    assert result[\"search_report\"][\"search_outcome\"] == \"attempted_with_usable_sources\""` | — |
| [SRC-F725E90B2A-L000081](../../tests/test_web_agent.py#L81) | 81 | `"    assert result[\"search_report\"][\"research_quality_semantics\"] == ("` | — |
| [SRC-F725E90B2A-L000082](../../tests/test_web_agent.py#L82) | 82 | `"        \"process_coverage_not_factual_probability\""` | — |
| [SRC-F725E90B2A-L000083](../../tests/test_web_agent.py#L83) | 83 | `"    )"` | — |
| [SRC-F725E90B2A-L000084](../../tests/test_web_agent.py#L84) | 84 | `"    assert result[\"search_report\"][\"claim_audit_semantics\"] == ("` | — |
| [SRC-F725E90B2A-L000085](../../tests/test_web_agent.py#L85) | 85 | `"        \"model_assisted_not_independent_fact_check\""` | — |
| [SRC-F725E90B2A-L000086](../../tests/test_web_agent.py#L86) | 86 | `"    )"` | — |
| [SRC-F725E90B2A-L000087](../../tests/test_web_agent.py#L87) | 87 | `"    assert result[\"search_report\"][\"distinct_registrable_domains\"] == 2"` | — |
| [SRC-F725E90B2A-L000088](../../tests/test_web_agent.py#L88) | 88 | `"    assert result[\"search_report\"][\"editorial_independence_status\"] == \"not_assessed\""` | — |
| [SRC-F725E90B2A-L000089](../../tests/test_web_agent.py#L89) | 89 | `"    assert result[\"search_report\"][\"independent_sources_field_semantics\"] == ("` | — |
| [SRC-F725E90B2A-L000090](../../tests/test_web_agent.py#L90) | 90 | `"        \"legacy_compatibility_alias_for_distinct_registrable_domain_count\""` | — |
| [SRC-F725E90B2A-L000091](../../tests/test_web_agent.py#L91) | 91 | `"    )"` | — |
| [SRC-F725E90B2A-L000092](../../tests/test_web_agent.py#L92) | 92 | `"    assert any(\"تعدد النطاقات المسجلة لا يثبت الاستقلال التحريري\" in warning"` | — |
| [SRC-F725E90B2A-L000093](../../tests/test_web_agent.py#L93) | 93 | `"               for warning in result[\"warnings\"])"` | — |
| [SRC-F725E90B2A-L000094](../../tests/test_web_agent.py#L94) | 94 | `"    assert result[\"used_language_model\"] is True"` | — |
| [SRC-F725E90B2A-L000095](../../tests/test_web_agent.py#L95) | 95 | `"    assert result[\"sources\"][0][\"url\"] == \"https://example.com/research\""` | — |
| [SRC-F725E90B2A-L000096](../../tests/test_web_agent.py#L96) | 96 | `"    assert \"[المصدر 1]\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L000097](../../tests/test_web_agent.py#L97) | 97 | `"    assert seen[\"question\"] == \"قارن هذه التقنية\""` | — |
| [SRC-F725E90B2A-L000098](../../tests/test_web_agent.py#L98) | 98 | `"    assert seen[\"history\"] == [{\"role\": \"user\", \"content\": \"ما هي التقنية؟\"}]"` | — |
| [SRC-F725E90B2A-L000099](../../tests/test_web_agent.py#L99) | 99 | `""` | — |
| [SRC-F725E90B2A-L000100](../../tests/test_web_agent.py#L100) | 100 | `""` | — |
| [SRC-F725E90B2A-L000101](../../tests/test_web_agent.py#L101) | 101 | `"def test_agent_returns_search_snippets_if_model_not_configured(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000102](../../tests/test_web_agent.py#L102) | 102 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000103](../../tests/test_web_agent.py#L103) | 103 | `"    agent.api_key = \"\""` | — |
| [SRC-F725E90B2A-L000104](../../tests/test_web_agent.py#L104) | 104 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L000105](../../tests/test_web_agent.py#L105) | 105 | `"        agent,"` | — |
| [SRC-F725E90B2A-L000106](../../tests/test_web_agent.py#L106) | 106 | `"        \"_collect_research\","` | — |
| [SRC-F725E90B2A-L000107](../../tests/test_web_agent.py#L107) | 107 | `"        lambda plan: ("` | — |
| [SRC-F725E90B2A-L000108](../../tests/test_web_agent.py#L108) | 108 | `"            [sample_source(0), sample_source(1)],"` | — |
| [SRC-F725E90B2A-L000109](../../tests/test_web_agent.py#L109) | 109 | `"            [],"` | — |
| [SRC-F725E90B2A-L000110](../../tests/test_web_agent.py#L110) | 110 | `"            {"` | — |
| [SRC-F725E90B2A-L000111](../../tests/test_web_agent.py#L111) | 111 | `"                \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L000112](../../tests/test_web_agent.py#L112) | 112 | `"                \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L000113](../../tests/test_web_agent.py#L113) | 113 | `"                \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L000114](../../tests/test_web_agent.py#L114) | 114 | `"                \"unique_sources\": 2,"` | — |
| [SRC-F725E90B2A-L000115](../../tests/test_web_agent.py#L115) | 115 | `"                \"pages_fetched\": 2,"` | — |
| [SRC-F725E90B2A-L000116](../../tests/test_web_agent.py#L116) | 116 | `"                \"providers_used\": [\"test\"],"` | — |
| [SRC-F725E90B2A-L000117](../../tests/test_web_agent.py#L117) | 117 | `"                \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L000118](../../tests/test_web_agent.py#L118) | 118 | `"                \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L000119](../../tests/test_web_agent.py#L119) | 119 | `"                \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L000120](../../tests/test_web_agent.py#L120) | 120 | `"                \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L000121](../../tests/test_web_agent.py#L121) | 121 | `"            },"` | — |
| [SRC-F725E90B2A-L000122](../../tests/test_web_agent.py#L122) | 122 | `"        ),"` | — |
| [SRC-F725E90B2A-L000123](../../tests/test_web_agent.py#L123) | 123 | `"    )"` | — |
| [SRC-F725E90B2A-L000124](../../tests/test_web_agent.py#L124) | 124 | `""` | — |
| [SRC-F725E90B2A-L000125](../../tests/test_web_agent.py#L125) | 125 | `"    result = agent.answer(\"ما الذي يقوله المصدر؟\")"` | — |
| [SRC-F725E90B2A-L000126](../../tests/test_web_agent.py#L126) | 126 | `""` | — |
| [SRC-F725E90B2A-L000127](../../tests/test_web_agent.py#L127) | 127 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-F725E90B2A-L000128](../../tests/test_web_agent.py#L128) | 128 | `"    assert result[\"used_language_model\"] is False"` | — |
| [SRC-F725E90B2A-L000129](../../tests/test_web_agent.py#L129) | 129 | `"    assert \"OPENROUTER_API_KEY\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L000130](../../tests/test_web_agent.py#L130) | 130 | `"    assert result[\"sources\"][0][\"page_fetched\"] is True"` | — |
| [SRC-F725E90B2A-L000131](../../tests/test_web_agent.py#L131) | 131 | `""` | — |
| [SRC-F725E90B2A-L000132](../../tests/test_web_agent.py#L132) | 132 | `""` | — |
| [SRC-F725E90B2A-L000133](../../tests/test_web_agent.py#L133) | 133 | `"def test_agent_rejects_empty_or_oversized_question():"` | — |
| [SRC-F725E90B2A-L000134](../../tests/test_web_agent.py#L134) | 134 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000135](../../tests/test_web_agent.py#L135) | 135 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-F725E90B2A-L000136](../../tests/test_web_agent.py#L136) | 136 | `"        agent.answer(\"   \")"` | — |
| [SRC-F725E90B2A-L000137](../../tests/test_web_agent.py#L137) | 137 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-F725E90B2A-L000138](../../tests/test_web_agent.py#L138) | 138 | `"        agent.answer(\"س\" * 4001)"` | — |
| [SRC-F725E90B2A-L000139](../../tests/test_web_agent.py#L139) | 139 | `""` | — |
| [SRC-F725E90B2A-L000140](../../tests/test_web_agent.py#L140) | 140 | `""` | — |
| [SRC-F725E90B2A-L000141](../../tests/test_web_agent.py#L141) | 141 | `"def test_history_search_query_expands_short_follow_up():"` | — |
| [SRC-F725E90B2A-L000142](../../tests/test_web_agent.py#L142) | 142 | `"    history = [{\"role\": \"user\", \"content\": \"قارن أسعار السيارات الكهربائية في مصر\"}]"` | — |
| [SRC-F725E90B2A-L000143](../../tests/test_web_agent.py#L143) | 143 | `"    query = WebAgent._history_search_query(\"والسعر؟\", history)"` | — |
| [SRC-F725E90B2A-L000144](../../tests/test_web_agent.py#L144) | 144 | `"    assert \"السيارات الكهربائية\" in query"` | — |
| [SRC-F725E90B2A-L000145](../../tests/test_web_agent.py#L145) | 145 | `"    assert \"والسعر؟\" in query"` | — |
| [SRC-F725E90B2A-L000146](../../tests/test_web_agent.py#L146) | 146 | `""` | — |
| [SRC-F725E90B2A-L000147](../../tests/test_web_agent.py#L147) | 147 | `""` | — |
| [SRC-F725E90B2A-L000148](../../tests/test_web_agent.py#L148) | 148 | `"def test_public_url_filter_rejects_local_and_credential_urls():"` | — |
| [SRC-F725E90B2A-L000149](../../tests/test_web_agent.py#L149) | 149 | `"    assert _public_http_url(\"http://127.0.0.1/admin\") is None"` | — |
| [SRC-F725E90B2A-L000150](../../tests/test_web_agent.py#L150) | 150 | `"    assert _public_http_url(\"http://localhost:8000/\") is None"` | — |
| [SRC-F725E90B2A-L000151](../../tests/test_web_agent.py#L151) | 151 | `"    assert _public_http_url(\"https://user:pass@example.com/private\") is None"` | — |
| [SRC-F725E90B2A-L000152](../../tests/test_web_agent.py#L152) | 152 | `"    assert _public_http_url(\"file:///etc/passwd\") is None"` | — |
| [SRC-F725E90B2A-L000153](../../tests/test_web_agent.py#L153) | 153 | `""` | — |
| [SRC-F725E90B2A-L000154](../../tests/test_web_agent.py#L154) | 154 | `""` | — |
| [SRC-F725E90B2A-L000155](../../tests/test_web_agent.py#L155) | 155 | `"def test_public_url_filter_accepts_basic_https_url():"` | — |
| [SRC-F725E90B2A-L000156](../../tests/test_web_agent.py#L156) | 156 | `"    assert _public_http_url(\"https://example.com/path#section\") == \"https://example.com/path\""` | — |
| [SRC-F725E90B2A-L000157](../../tests/test_web_agent.py#L157) | 157 | `""` | — |
| [SRC-F725E90B2A-L000158](../../tests/test_web_agent.py#L158) | 158 | `""` | — |
| [SRC-F725E90B2A-L000159](../../tests/test_web_agent.py#L159) | 159 | `"def test_search_web_parses_duckduckgo_and_bing_without_ddgs(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000160](../../tests/test_web_agent.py#L160) | 160 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L000161](../../tests/test_web_agent.py#L161) | 161 | `""` | — |
| [SRC-F725E90B2A-L000162](../../tests/test_web_agent.py#L162) | 162 | `"    html = \"\"\""` | — |
| [SRC-F725E90B2A-L000163](../../tests/test_web_agent.py#L163) | 163 | `"    <html><body>"` | — |
| [SRC-F725E90B2A-L000164](../../tests/test_web_agent.py#L164) | 164 | `"      <div class=\"result\">"` | — |
| [SRC-F725E90B2A-L000165](../../tests/test_web_agent.py#L165) | 165 | `"        <a class=\"result__a\" href=\"https://example.com/first\">صفحة أولى</a>"` | — |
| [SRC-F725E90B2A-L000166](../../tests/test_web_agent.py#L166) | 166 | `"        <a class=\"result__snippet\">سؤال بحث تجريبي مقتطف أول</a>"` | — |
| [SRC-F725E90B2A-L000167](../../tests/test_web_agent.py#L167) | 167 | `"      </div>"` | — |
| [SRC-F725E90B2A-L000168](../../tests/test_web_agent.py#L168) | 168 | `"    </body></html>"` | — |
| [SRC-F725E90B2A-L000169](../../tests/test_web_agent.py#L169) | 169 | `"    \"\"\""` | — |
| [SRC-F725E90B2A-L000170](../../tests/test_web_agent.py#L170) | 170 | `"    rss = \"\"\""` | — |
| [SRC-F725E90B2A-L000171](../../tests/test_web_agent.py#L171) | 171 | `"    <rss><channel><item>"` | — |
| [SRC-F725E90B2A-L000172](../../tests/test_web_agent.py#L172) | 172 | `"      <title>صفحة ثانية</title>"` | — |
| [SRC-F725E90B2A-L000173](../../tests/test_web_agent.py#L173) | 173 | `"      <link>https://example.net/second</link>"` | — |
| [SRC-F725E90B2A-L000174](../../tests/test_web_agent.py#L174) | 174 | `"      <description>سؤال بحث تجريبي مقتطف ثاني</description>"` | — |
| [SRC-F725E90B2A-L000175](../../tests/test_web_agent.py#L175) | 175 | `"    </item></channel></rss>"` | — |
| [SRC-F725E90B2A-L000176](../../tests/test_web_agent.py#L176) | 176 | `"    \"\"\""` | — |
| [SRC-F725E90B2A-L000177](../../tests/test_web_agent.py#L177) | 177 | `""` | — |
| [SRC-F725E90B2A-L000178](../../tests/test_web_agent.py#L178) | 178 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000179](../../tests/test_web_agent.py#L179) | 179 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L000180](../../tests/test_web_agent.py#L180) | 180 | `""` | — |
| [SRC-F725E90B2A-L000181](../../tests/test_web_agent.py#L181) | 181 | `"        def __init__(self, text):"` | — |
| [SRC-F725E90B2A-L000182](../../tests/test_web_agent.py#L182) | 182 | `"            self.text = text"` | — |
| [SRC-F725E90B2A-L000183](../../tests/test_web_agent.py#L183) | 183 | `"            self.content = text.encode(\"utf-8\")"` | — |
| [SRC-F725E90B2A-L000184](../../tests/test_web_agent.py#L184) | 184 | `""` | — |
| [SRC-F725E90B2A-L000185](../../tests/test_web_agent.py#L185) | 185 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L000186](../../tests/test_web_agent.py#L186) | 186 | `""` | — |
| [SRC-F725E90B2A-L000187](../../tests/test_web_agent.py#L187) | 187 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000188](../../tests/test_web_agent.py#L188) | 188 | `"        calls.append(url)"` | — |
| [SRC-F725E90B2A-L000189](../../tests/test_web_agent.py#L189) | 189 | `"        return FakeResponse(html if \"duckduckgo.com\" in url else rss)"` | — |
| [SRC-F725E90B2A-L000190](../../tests/test_web_agent.py#L190) | 190 | `""` | — |
| [SRC-F725E90B2A-L000191](../../tests/test_web_agent.py#L191) | 191 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L000192](../../tests/test_web_agent.py#L192) | 192 | `"    results = WebAgent()._search_web(\"سؤال بحث تجريبي\")"` | — |
| [SRC-F725E90B2A-L000193](../../tests/test_web_agent.py#L193) | 193 | `""` | — |
| [SRC-F725E90B2A-L000194](../../tests/test_web_agent.py#L194) | 194 | `"    assert len(results) == 2"` | — |
| [SRC-F725E90B2A-L000195](../../tests/test_web_agent.py#L195) | 195 | `"    assert results[0][\"title\"] == \"صفحة أولى\""` | — |
| [SRC-F725E90B2A-L000196](../../tests/test_web_agent.py#L196) | 196 | `"    assert results[0][\"url\"] == \"https://example.com/first\""` | — |
| [SRC-F725E90B2A-L000197](../../tests/test_web_agent.py#L197) | 197 | `"    assert results[1][\"title\"] == \"صفحة ثانية\""` | — |
| [SRC-F725E90B2A-L000198](../../tests/test_web_agent.py#L198) | 198 | `"    assert results[1][\"url\"] == \"https://example.net/second\""` | — |
| [SRC-F725E90B2A-L000199](../../tests/test_web_agent.py#L199) | 199 | `"    assert len(calls) == 2"` | — |
| [SRC-F725E90B2A-L000200](../../tests/test_web_agent.py#L200) | 200 | `""` | — |
| [SRC-F725E90B2A-L000201](../../tests/test_web_agent.py#L201) | 201 | `""` | — |
| [SRC-F725E90B2A-L000202](../../tests/test_web_agent.py#L202) | 202 | `""` | — |
| [SRC-F725E90B2A-L000203](../../tests/test_web_agent.py#L203) | 203 | `"def test_model_planner_preserves_social_intent_and_adds_targeted_query(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000204](../../tests/test_web_agent.py#L204) | 204 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000205](../../tests/test_web_agent.py#L205) | 205 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L000206](../../tests/test_web_agent.py#L206) | 206 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L000207](../../tests/test_web_agent.py#L207) | 207 | `"        agent,"` | — |
| [SRC-F725E90B2A-L000208](../../tests/test_web_agent.py#L208) | 208 | `"        \"_request_completion\","` | — |
| [SRC-F725E90B2A-L000209](../../tests/test_web_agent.py#L209) | 209 | `"        lambda *args, **kwargs: ("` | — |
| [SRC-F725E90B2A-L000210](../../tests/test_web_agent.py#L210) | 210 | `"            '{\"queries\":[\"مراجعات السيارات الكهربائية\"],\"social_focus\":true,'"` | — |
| [SRC-F725E90B2A-L000211](../../tests/test_web_agent.py#L211) | 211 | `"            '\"freshness\":\"any\",\"depth\":\"deep\",\"platforms\":[\"reddit\"]}'"` | — |
| [SRC-F725E90B2A-L000212](../../tests/test_web_agent.py#L212) | 212 | `"        ),"` | — |
| [SRC-F725E90B2A-L000213](../../tests/test_web_agent.py#L213) | 213 | `"    )"` | — |
| [SRC-F725E90B2A-L000214](../../tests/test_web_agent.py#L214) | 214 | `"    plan = agent._plan_search("` | — |
| [SRC-F725E90B2A-L000215](../../tests/test_web_agent.py#L215) | 215 | `"        \"ابحث في Reddit عن تجارب العملاء مع السيارات الكهربائية\","` | — |
| [SRC-F725E90B2A-L000216](../../tests/test_web_agent.py#L216) | 216 | `"        [],"` | — |
| [SRC-F725E90B2A-L000217](../../tests/test_web_agent.py#L217) | 217 | `"    )"` | — |
| [SRC-F725E90B2A-L000218](../../tests/test_web_agent.py#L218) | 218 | `"    assert plan[\"planning_method\"] == \"language_model\""` | — |
| [SRC-F725E90B2A-L000219](../../tests/test_web_agent.py#L219) | 219 | `"    assert plan[\"social_focus\"] is True"` | — |
| [SRC-F725E90B2A-L000220](../../tests/test_web_agent.py#L220) | 220 | `"    assert \"reddit\" in plan[\"platforms\"]"` | — |
| [SRC-F725E90B2A-L000221](../../tests/test_web_agent.py#L221) | 221 | `"    assert any(\"site:reddit.com\" in query for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L000222](../../tests/test_web_agent.py#L222) | 222 | `""` | — |
| [SRC-F725E90B2A-L000223](../../tests/test_web_agent.py#L223) | 223 | `""` | — |
| [SRC-F725E90B2A-L000224](../../tests/test_web_agent.py#L224) | 224 | `"def test_direct_social_search_reads_public_reddit_and_bluesky_results(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000225](../../tests/test_web_agent.py#L225) | 225 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L000226](../../tests/test_web_agent.py#L226) | 226 | `""` | — |
| [SRC-F725E90B2A-L000227](../../tests/test_web_agent.py#L227) | 227 | `"    reddit_xml = \"\"\"<rss><channel><item>"` | — |
| [SRC-F725E90B2A-L000228](../../tests/test_web_agent.py#L228) | 228 | `"      <title>تجربة سيارة كهربائية</title>"` | — |
| [SRC-F725E90B2A-L000229](../../tests/test_web_agent.py#L229) | 229 | `"      <link>https://www.reddit.com/r/cars/comments/abc123/test/</link>"` | — |
| [SRC-F725E90B2A-L000230](../../tests/test_web_agent.py#L230) | 230 | `"      <description>استهلاك البطارية في الحر</description>"` | — |
| [SRC-F725E90B2A-L000231](../../tests/test_web_agent.py#L231) | 231 | `"      <pubDate>Mon, 12 Oct 2026 10:00:00 GMT</pubDate>"` | — |
| [SRC-F725E90B2A-L000232](../../tests/test_web_agent.py#L232) | 232 | `"    </item></channel></rss>\"\"\""` | — |
| [SRC-F725E90B2A-L000233](../../tests/test_web_agent.py#L233) | 233 | `""` | — |
| [SRC-F725E90B2A-L000234](../../tests/test_web_agent.py#L234) | 234 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000235](../../tests/test_web_agent.py#L235) | 235 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L000236](../../tests/test_web_agent.py#L236) | 236 | `""` | — |
| [SRC-F725E90B2A-L000237](../../tests/test_web_agent.py#L237) | 237 | `"        def __init__(self, text=\"\", data=None):"` | — |
| [SRC-F725E90B2A-L000238](../../tests/test_web_agent.py#L238) | 238 | `"            self.text = text"` | — |
| [SRC-F725E90B2A-L000239](../../tests/test_web_agent.py#L239) | 239 | `"            self.content = text.encode(\"utf-8\")"` | — |
| [SRC-F725E90B2A-L000240](../../tests/test_web_agent.py#L240) | 240 | `"            self._data = data or {}"` | — |
| [SRC-F725E90B2A-L000241](../../tests/test_web_agent.py#L241) | 241 | `""` | — |
| [SRC-F725E90B2A-L000242](../../tests/test_web_agent.py#L242) | 242 | `"        def json(self):"` | — |
| [SRC-F725E90B2A-L000243](../../tests/test_web_agent.py#L243) | 243 | `"            return self._data"` | — |
| [SRC-F725E90B2A-L000244](../../tests/test_web_agent.py#L244) | 244 | `""` | — |
| [SRC-F725E90B2A-L000245](../../tests/test_web_agent.py#L245) | 245 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000246](../../tests/test_web_agent.py#L246) | 246 | `"        if \"reddit.com\" in url:"` | — |
| [SRC-F725E90B2A-L000247](../../tests/test_web_agent.py#L247) | 247 | `"            return FakeResponse(reddit_xml)"` | — |
| [SRC-F725E90B2A-L000248](../../tests/test_web_agent.py#L248) | 248 | `"        if \"bsky.app\" in url or \"public.api.bsky.app\" in url:"` | — |
| [SRC-F725E90B2A-L000249](../../tests/test_web_agent.py#L249) | 249 | `"            return FakeResponse(data={"` | — |
| [SRC-F725E90B2A-L000250](../../tests/test_web_agent.py#L250) | 250 | `"                \"posts\": [{"` | — |
| [SRC-F725E90B2A-L000251](../../tests/test_web_agent.py#L251) | 251 | `"                    \"post\": {"` | — |
| [SRC-F725E90B2A-L000252](../../tests/test_web_agent.py#L252) | 252 | `"                        \"uri\": \"at://did:plc:example/app.bsky.feed.post/rkey123\","` | — |
| [SRC-F725E90B2A-L000253](../../tests/test_web_agent.py#L253) | 253 | `"                        \"indexedAt\": \"2026-10-12T10:00:00Z\","` | — |
| [SRC-F725E90B2A-L000254](../../tests/test_web_agent.py#L254) | 254 | `"                        \"record\": {\"text\": \"استخدمت السيارة شهرًا\"},"` | — |
| [SRC-F725E90B2A-L000255](../../tests/test_web_agent.py#L255) | 255 | `"                        \"author\": {\"handle\": \"driver.bsky.social\", \"displayName\": \"Driver\"},"` | — |
| [SRC-F725E90B2A-L000256](../../tests/test_web_agent.py#L256) | 256 | `"                    }"` | — |
| [SRC-F725E90B2A-L000257](../../tests/test_web_agent.py#L257) | 257 | `"                }]"` | — |
| [SRC-F725E90B2A-L000258](../../tests/test_web_agent.py#L258) | 258 | `"            })"` | — |
| [SRC-F725E90B2A-L000259](../../tests/test_web_agent.py#L259) | 259 | `"        raise AssertionError(f\"Unexpected URL: {url}\")"` | — |
| [SRC-F725E90B2A-L000260](../../tests/test_web_agent.py#L260) | 260 | `""` | — |
| [SRC-F725E90B2A-L000261](../../tests/test_web_agent.py#L261) | 261 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L000262](../../tests/test_web_agent.py#L262) | 262 | `"    results, warnings = WebAgent()._search_social("` | — |
| [SRC-F725E90B2A-L000263](../../tests/test_web_agent.py#L263) | 263 | `"        \"سيارة كهربائية\", [\"reddit\", \"bluesky\"]"` | — |
| [SRC-F725E90B2A-L000264](../../tests/test_web_agent.py#L264) | 264 | `"    )"` | — |
| [SRC-F725E90B2A-L000265](../../tests/test_web_agent.py#L265) | 265 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000266](../../tests/test_web_agent.py#L266) | 266 | `"    assert any(item[\"provider\"] == \"reddit_public_rss\" for item in results)"` | — |
| [SRC-F725E90B2A-L000267](../../tests/test_web_agent.py#L267) | 267 | `"    bsky = next(item for item in results if item[\"provider\"] == \"bluesky_public_search\")"` | — |
| [SRC-F725E90B2A-L000268](../../tests/test_web_agent.py#L268) | 268 | `"    assert bsky[\"url\"] == \"https://bsky.app/profile/driver.bsky.social/post/rkey123\""` | — |
| [SRC-F725E90B2A-L000269](../../tests/test_web_agent.py#L269) | 269 | `"    assert bsky[\"snippet\"] == \"استخدمت السيارة شهرًا\""` | — |
| [SRC-F725E90B2A-L000270](../../tests/test_web_agent.py#L270) | 270 | `""` | — |
