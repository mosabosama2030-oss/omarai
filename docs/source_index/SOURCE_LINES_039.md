# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **039**
- سجلات الأسطر: **800**
- النطاق: SRC-6BECF5AD00-L000049 إلى SRC-6BCB799CEC-L000305
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-6BECF5AD00 — [tests/test_connectors_mocked.py](../../tests/test_connectors_mocked.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6BECF5AD00-L000049](../../tests/test_connectors_mocked.py#L49) | 49 | `""` | — |
| [SRC-6BECF5AD00-L000050](../../tests/test_connectors_mocked.py#L50) | 50 | `""` | — |
| [SRC-6BECF5AD00-L000051](../../tests/test_connectors_mocked.py#L51) | 51 | `"def test_connector_failure_returns_empty(monkeypatch):"` | — |
| [SRC-6BECF5AD00-L000052](../../tests/test_connectors_mocked.py#L52) | 52 | `"    def boom(*args, **kwargs):"` | — |
| [SRC-6BECF5AD00-L000053](../../tests/test_connectors_mocked.py#L53) | 53 | `"        raise sc.urllib.error.URLError(\"down\")"` | — |
| [SRC-6BECF5AD00-L000054](../../tests/test_connectors_mocked.py#L54) | 54 | `""` | — |
| [SRC-6BECF5AD00-L000055](../../tests/test_connectors_mocked.py#L55) | 55 | `"    monkeypatch.setattr(sc, \"_http_get_json\", boom)"` | — |
| [SRC-6BECF5AD00-L000056](../../tests/test_connectors_mocked.py#L56) | 56 | `"    assert sc.run_connector(\"openalex\", \"query\") == []"` | — |
| [SRC-6BECF5AD00-L000057](../../tests/test_connectors_mocked.py#L57) | 57 | `""` | — |
| [SRC-6BECF5AD00-L000058](../../tests/test_connectors_mocked.py#L58) | 58 | `""` | — |
| [SRC-6BECF5AD00-L000059](../../tests/test_connectors_mocked.py#L59) | 59 | `"def test_run_free_academic_dedupe_path(monkeypatch):"` | — |
| [SRC-6BECF5AD00-L000060](../../tests/test_connectors_mocked.py#L60) | 60 | `"    def fake_run(name, query, limit=4):"` | — |
| [SRC-6BECF5AD00-L000061](../../tests/test_connectors_mocked.py#L61) | 61 | `"        return ["` | — |
| [SRC-6BECF5AD00-L000062](../../tests/test_connectors_mocked.py#L62) | 62 | `"            {"` | — |
| [SRC-6BECF5AD00-L000063](../../tests/test_connectors_mocked.py#L63) | 63 | `"                \"title\": f\"{name}-title\","` | — |
| [SRC-6BECF5AD00-L000064](../../tests/test_connectors_mocked.py#L64) | 64 | `"                \"url\": f\"https://example.com/{name}\","` | — |
| [SRC-6BECF5AD00-L000065](../../tests/test_connectors_mocked.py#L65) | 65 | `"                \"snippet\": \"x\","` | — |
| [SRC-6BECF5AD00-L000066](../../tests/test_connectors_mocked.py#L66) | 66 | `"                \"page_fetched\": False,"` | — |
| [SRC-6BECF5AD00-L000067](../../tests/test_connectors_mocked.py#L67) | 67 | `"                \"provider\": name,"` | — |
| [SRC-6BECF5AD00-L000068](../../tests/test_connectors_mocked.py#L68) | 68 | `"                \"provider_rank\": 1,"` | — |
| [SRC-6BECF5AD00-L000069](../../tests/test_connectors_mocked.py#L69) | 69 | `"                \"search_query\": query,"` | — |
| [SRC-6BECF5AD00-L000070](../../tests/test_connectors_mocked.py#L70) | 70 | `"                \"published_at\": \"\","` | — |
| [SRC-6BECF5AD00-L000071](../../tests/test_connectors_mocked.py#L71) | 71 | `"                \"source_class\": \"academic\","` | — |
| [SRC-6BECF5AD00-L000072](../../tests/test_connectors_mocked.py#L72) | 72 | `"            }"` | — |
| [SRC-6BECF5AD00-L000073](../../tests/test_connectors_mocked.py#L73) | 73 | `"        ]"` | — |
| [SRC-6BECF5AD00-L000074](../../tests/test_connectors_mocked.py#L74) | 74 | `""` | — |
| [SRC-6BECF5AD00-L000075](../../tests/test_connectors_mocked.py#L75) | 75 | `"    monkeypatch.setattr(sc, \"run_connector\", fake_run)"` | — |
| [SRC-6BECF5AD00-L000076](../../tests/test_connectors_mocked.py#L76) | 76 | `"    rows = sc.run_free_academic_connectors(\"ev egypt\", limit_per=1)"` | — |
| [SRC-6BECF5AD00-L000077](../../tests/test_connectors_mocked.py#L77) | 77 | `"    assert len(rows) == 3"` | — |
| [SRC-6BECF5AD00-L000078](../../tests/test_connectors_mocked.py#L78) | 78 | `"    providers = {r[\"provider\"] for r in rows}"` | — |
| [SRC-6BECF5AD00-L000079](../../tests/test_connectors_mocked.py#L79) | 79 | `"    assert providers == {\"openalex\", \"arxiv\", \"crossref\"}"` | — |
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

### FILE-29A9CD43D1 — [tests/test_dialogue_context_pipeline.py](../../tests/test_dialogue_context_pipeline.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-29A9CD43D1-L000001](../../tests/test_dialogue_context_pipeline.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-29A9CD43D1-L000002](../../tests/test_dialogue_context_pipeline.py#L2) | 2 | `""` | — |
| [SRC-29A9CD43D1-L000003](../../tests/test_dialogue_context_pipeline.py#L3) | 3 | `"import json"` | — |
| [SRC-29A9CD43D1-L000004](../../tests/test_dialogue_context_pipeline.py#L4) | 4 | `"from typing import Any"` | — |
| [SRC-29A9CD43D1-L000005](../../tests/test_dialogue_context_pipeline.py#L5) | 5 | `""` | — |
| [SRC-29A9CD43D1-L000006](../../tests/test_dialogue_context_pipeline.py#L6) | 6 | `"import pytest"` | — |
| [SRC-29A9CD43D1-L000007](../../tests/test_dialogue_context_pipeline.py#L7) | 7 | `""` | — |
| [SRC-29A9CD43D1-L000008](../../tests/test_dialogue_context_pipeline.py#L8) | 8 | `"from agents.research import evidence_signal_report"` | — |
| [SRC-29A9CD43D1-L000009](../../tests/test_dialogue_context_pipeline.py#L9) | 9 | `"from agents.dialogue_state import might_be_context_dependent"` | — |
| [SRC-29A9CD43D1-L000010](../../tests/test_dialogue_context_pipeline.py#L10) | 10 | `"from agents.web_agent import WebAgent"` | — |
| [SRC-29A9CD43D1-L000011](../../tests/test_dialogue_context_pipeline.py#L11) | 11 | `""` | — |
| [SRC-29A9CD43D1-L000012](../../tests/test_dialogue_context_pipeline.py#L12) | 12 | `""` | — |
| [SRC-29A9CD43D1-L000013](../../tests/test_dialogue_context_pipeline.py#L13) | 13 | `"def _source(domain: str, queries: list[str]) -> dict[str, Any]:"` | — |
| [SRC-29A9CD43D1-L000014](../../tests/test_dialogue_context_pipeline.py#L14) | 14 | `"    return {"` | — |
| [SRC-29A9CD43D1-L000015](../../tests/test_dialogue_context_pipeline.py#L15) | 15 | `"        \"title\": \"iPhone 17 256GB international warranty coverage in Egypt\","` | — |
| [SRC-29A9CD43D1-L000016](../../tests/test_dialogue_context_pipeline.py#L16) | 16 | `"        \"url\": f\"https://{domain}/iphone-warranty\","` | — |
| [SRC-29A9CD43D1-L000017](../../tests/test_dialogue_context_pipeline.py#L17) | 17 | `"        \"snippet\": \"Warranty coverage and service policy for iPhone 17 in Egypt.\","` | — |
| [SRC-29A9CD43D1-L000018](../../tests/test_dialogue_context_pipeline.py#L18) | 18 | `"        \"page_text\": \"Warranty coverage and service policy for iPhone 17 in Egypt.\","` | — |
| [SRC-29A9CD43D1-L000019](../../tests/test_dialogue_context_pipeline.py#L19) | 19 | `"        \"page_fetched\": True,"` | — |
| [SRC-29A9CD43D1-L000020](../../tests/test_dialogue_context_pipeline.py#L20) | 20 | `"        \"providers\": [\"test_search\"],"` | — |
| [SRC-29A9CD43D1-L000021](../../tests/test_dialogue_context_pipeline.py#L21) | 21 | `"        \"queries\": list(queries),"` | — |
| [SRC-29A9CD43D1-L000022](../../tests/test_dialogue_context_pipeline.py#L22) | 22 | `"        \"domain\": domain,"` | — |
| [SRC-29A9CD43D1-L000023](../../tests/test_dialogue_context_pipeline.py#L23) | 23 | `"        \"source_class\": \"general\","` | — |
| [SRC-29A9CD43D1-L000024](../../tests/test_dialogue_context_pipeline.py#L24) | 24 | `"        \"platform\": \"web\","` | — |
| [SRC-29A9CD43D1-L000025](../../tests/test_dialogue_context_pipeline.py#L25) | 25 | `"        \"published_at\": \"\","` | — |
| [SRC-29A9CD43D1-L000026](../../tests/test_dialogue_context_pipeline.py#L26) | 26 | `"        \"rank_score\": 1.0,"` | — |
| [SRC-29A9CD43D1-L000027](../../tests/test_dialogue_context_pipeline.py#L27) | 27 | `"    }"` | — |
| [SRC-29A9CD43D1-L000028](../../tests/test_dialogue_context_pipeline.py#L28) | 28 | `""` | — |
| [SRC-29A9CD43D1-L000029](../../tests/test_dialogue_context_pipeline.py#L29) | 29 | `""` | — |
| [SRC-29A9CD43D1-L000030](../../tests/test_dialogue_context_pipeline.py#L30) | 30 | `"def _report(plan: dict[str, Any], sources: list[dict[str, Any]]) -> dict[str, Any]:"` | — |
| [SRC-29A9CD43D1-L000031](../../tests/test_dialogue_context_pipeline.py#L31) | 31 | `"    return {"` | — |
| [SRC-29A9CD43D1-L000032](../../tests/test_dialogue_context_pipeline.py#L32) | 32 | `"        \"queries_planned\": len(plan.get(\"queries\", [])),"` | — |
| [SRC-29A9CD43D1-L000033](../../tests/test_dialogue_context_pipeline.py#L33) | 33 | `"        \"queries_attempted\": len(plan.get(\"queries\", [])),"` | — |
| [SRC-29A9CD43D1-L000034](../../tests/test_dialogue_context_pipeline.py#L34) | 34 | `"        \"queries_attempted_known\": True,"` | — |
| [SRC-29A9CD43D1-L000035](../../tests/test_dialogue_context_pipeline.py#L35) | 35 | `"        \"search_attempted\": True,"` | — |
| [SRC-29A9CD43D1-L000036](../../tests/test_dialogue_context_pipeline.py#L36) | 36 | `"        \"search_outcome\": \"attempted_with_usable_sources\","` | — |
| [SRC-29A9CD43D1-L000037](../../tests/test_dialogue_context_pipeline.py#L37) | 37 | `"        \"query_results\": [],"` | — |
| [SRC-29A9CD43D1-L000038](../../tests/test_dialogue_context_pipeline.py#L38) | 38 | `"        \"unique_sources\": len(sources),"` | — |
| [SRC-29A9CD43D1-L000039](../../tests/test_dialogue_context_pipeline.py#L39) | 39 | `"        \"pages_fetched\": len(sources),"` | — |
| [SRC-29A9CD43D1-L000040](../../tests/test_dialogue_context_pipeline.py#L40) | 40 | `"        \"providers_used\": [\"test_search\"],"` | — |
| [SRC-29A9CD43D1-L000041](../../tests/test_dialogue_context_pipeline.py#L41) | 41 | `"        \"provider_counts\": {\"test_search\": len(sources)},"` | — |
| [SRC-29A9CD43D1-L000042](../../tests/test_dialogue_context_pipeline.py#L42) | 42 | `"        \"platform_counts\": {\"web\": len(sources)},"` | — |
| [SRC-29A9CD43D1-L000043](../../tests/test_dialogue_context_pipeline.py#L43) | 43 | `"        \"social_direct_results\": 0,"` | — |
| [SRC-29A9CD43D1-L000044](../../tests/test_dialogue_context_pipeline.py#L44) | 44 | `"        \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-29A9CD43D1-L000045](../../tests/test_dialogue_context_pipeline.py#L45) | 45 | `"        \"planning_method\": plan.get(\"planning_method\", \"test\"),"` | — |
| [SRC-29A9CD43D1-L000046](../../tests/test_dialogue_context_pipeline.py#L46) | 46 | `"        \"evidence_signals\": evidence_signal_report(sources),"` | — |
| [SRC-29A9CD43D1-L000047](../../tests/test_dialogue_context_pipeline.py#L47) | 47 | `"    }"` | — |
| [SRC-29A9CD43D1-L000048](../../tests/test_dialogue_context_pipeline.py#L48) | 48 | `""` | — |
| [SRC-29A9CD43D1-L000049](../../tests/test_dialogue_context_pipeline.py#L49) | 49 | `""` | — |
| [SRC-29A9CD43D1-L000050](../../tests/test_dialogue_context_pipeline.py#L50) | 50 | `"def _semantic_context(*, needs_clarification: bool = False) -> dict[str, Any]:"` | — |
| [SRC-29A9CD43D1-L000051](../../tests/test_dialogue_context_pipeline.py#L51) | 51 | `"    return {"` | — |
| [SRC-29A9CD43D1-L000052](../../tests/test_dialogue_context_pipeline.py#L52) | 52 | `"        \"resolved_question\": ("` | — |
| [SRC-29A9CD43D1-L000053](../../tests/test_dialogue_context_pipeline.py#L53) | 53 | `"            \"هل الضمان الدولي لهاتف iPhone 17 سعة 256 جيجابايت الذي اشتريته \""` | — |
| [SRC-29A9CD43D1-L000054](../../tests/test_dialogue_context_pipeline.py#L54) | 54 | `"            \"في مصر يغطي الصيانة داخل مصر؟\""` | — |
| [SRC-29A9CD43D1-L000055](../../tests/test_dialogue_context_pipeline.py#L55) | 55 | `"        ),"` | — |
| [SRC-29A9CD43D1-L000056](../../tests/test_dialogue_context_pipeline.py#L56) | 56 | `"        \"intent\": \"current_information\","` | — |
| [SRC-29A9CD43D1-L000057](../../tests/test_dialogue_context_pipeline.py#L57) | 57 | `"        \"topic\": \"تغطية الضمان\","` | — |
| [SRC-29A9CD43D1-L000058](../../tests/test_dialogue_context_pipeline.py#L58) | 58 | `"        \"entities\": [\"iPhone 17\"],"` | — |
| [SRC-29A9CD43D1-L000059](../../tests/test_dialogue_context_pipeline.py#L59) | 59 | `"        \"slots\": {"` | — |
| [SRC-29A9CD43D1-L000060](../../tests/test_dialogue_context_pipeline.py#L60) | 60 | `"            \"product\": \"iPhone 17\","` | — |
| [SRC-29A9CD43D1-L000061](../../tests/test_dialogue_context_pipeline.py#L61) | 61 | `"            \"capacity\": \"256 جيجابايت\","` | — |
| [SRC-29A9CD43D1-L000062](../../tests/test_dialogue_context_pipeline.py#L62) | 62 | `"            \"country\": \"مصر\","` | — |
| [SRC-29A9CD43D1-L000063](../../tests/test_dialogue_context_pipeline.py#L63) | 63 | `"            \"aspect\": \"الضمان الدولي والصيانة داخل مصر\","` | — |
| [SRC-29A9CD43D1-L000064](../../tests/test_dialogue_context_pipeline.py#L64) | 64 | `"        },"` | — |
| [SRC-29A9CD43D1-L000065](../../tests/test_dialogue_context_pipeline.py#L65) | 65 | `"        \"changed_slots\": [\"aspect\"],"` | — |
| [SRC-29A9CD43D1-L000066](../../tests/test_dialogue_context_pipeline.py#L66) | 66 | `"        \"is_follow_up\": True,"` | — |
| [SRC-29A9CD43D1-L000067](../../tests/test_dialogue_context_pipeline.py#L67) | 67 | `"        \"topic_shift\": False,"` | — |
| [SRC-29A9CD43D1-L000068](../../tests/test_dialogue_context_pipeline.py#L68) | 68 | `"        \"needs_web\": True,"` | — |
| [SRC-29A9CD43D1-L000069](../../tests/test_dialogue_context_pipeline.py#L69) | 69 | `"        \"research_depth\": \"standard\","` | — |
| [SRC-29A9CD43D1-L000070](../../tests/test_dialogue_context_pipeline.py#L70) | 70 | `"        \"needs_clarification\": needs_clarification,"` | — |
| [SRC-29A9CD43D1-L000071](../../tests/test_dialogue_context_pipeline.py#L71) | 71 | `"        \"clarification_question\": ("` | — |
| [SRC-29A9CD43D1-L000072](../../tests/test_dialogue_context_pipeline.py#L72) | 72 | `"            \"تقصد ضمان أي هاتف تحديدًا، أم تريد مقارنة ضمان الهاتفين؟\""` | — |
| [SRC-29A9CD43D1-L000073](../../tests/test_dialogue_context_pipeline.py#L73) | 73 | `"            if needs_clarification else \"\""` | — |
| [SRC-29A9CD43D1-L000074](../../tests/test_dialogue_context_pipeline.py#L74) | 74 | `"        ),"` | — |
| [SRC-29A9CD43D1-L000075](../../tests/test_dialogue_context_pipeline.py#L75) | 75 | `"        \"unresolved_references\": [\"الضمان\"] if needs_clarification else [],"` | — |
| [SRC-29A9CD43D1-L000076](../../tests/test_dialogue_context_pipeline.py#L76) | 76 | `"        \"resolution_basis\": \"history_inferred\","` | — |
| [SRC-29A9CD43D1-L000077](../../tests/test_dialogue_context_pipeline.py#L77) | 77 | `"        \"confidence_band\": \"medium\","` | — |
| [SRC-29A9CD43D1-L000078](../../tests/test_dialogue_context_pipeline.py#L78) | 78 | `"    }"` | — |
| [SRC-29A9CD43D1-L000079](../../tests/test_dialogue_context_pipeline.py#L79) | 79 | `""` | — |
| [SRC-29A9CD43D1-L000080](../../tests/test_dialogue_context_pipeline.py#L80) | 80 | `""` | — |
| [SRC-29A9CD43D1-L000081](../../tests/test_dialogue_context_pipeline.py#L81) | 81 | `"def test_semantic_context_probe_routes_natural_followup_to_search_and_answer("` | — |
| [SRC-29A9CD43D1-L000082](../../tests/test_dialogue_context_pipeline.py#L82) | 82 | `"    monkeypatch: pytest.MonkeyPatch,"` | — |
| [SRC-29A9CD43D1-L000083](../../tests/test_dialogue_context_pipeline.py#L83) | 83 | `") -> None:"` | — |
| [SRC-29A9CD43D1-L000084](../../tests/test_dialogue_context_pipeline.py#L84) | 84 | `"    agent = WebAgent()"` | — |
| [SRC-29A9CD43D1-L000085](../../tests/test_dialogue_context_pipeline.py#L85) | 85 | `"    agent.api_key = \"test-key\"  # All model responses are mocked; no provider call is made."` | — |
| [SRC-29A9CD43D1-L000086](../../tests/test_dialogue_context_pipeline.py#L86) | 86 | `"    history = ["` | — |
| [SRC-29A9CD43D1-L000087](../../tests/test_dialogue_context_pipeline.py#L87) | 87 | `"        {\"role\": \"user\", \"content\": \"اشتريت iPhone 17 النسخة الأساسية سعة 256 جيجابايت من مصر.\"},"` | — |
| [SRC-29A9CD43D1-L000088](../../tests/test_dialogue_context_pipeline.py#L88) | 88 | `"        {\"role\": \"assistant\", \"content\": \"نتحدث عن نسخة iPhone 17 سعة 256 جيجابايت في مصر.\"},"` | — |
| [SRC-29A9CD43D1-L000089](../../tests/test_dialogue_context_pipeline.py#L89) | 89 | `"    ]"` | — |
| [SRC-29A9CD43D1-L000090](../../tests/test_dialogue_context_pipeline.py#L90) | 90 | `"    context = _semantic_context()"` | — |
| [SRC-29A9CD43D1-L000091](../../tests/test_dialogue_context_pipeline.py#L91) | 91 | `"    seen: dict[str, Any] = {\"model_prompts\": []}"` | — |
| [SRC-29A9CD43D1-L000092](../../tests/test_dialogue_context_pipeline.py#L92) | 92 | `""` | — |
| [SRC-29A9CD43D1-L000093](../../tests/test_dialogue_context_pipeline.py#L93) | 93 | `"    def mocked_completion(messages, **kwargs):"` | — |
| [SRC-29A9CD43D1-L000094](../../tests/test_dialogue_context_pipeline.py#L94) | 94 | `"        system_prompt = messages[0][\"content\"]"` | — |
| [SRC-29A9CD43D1-L000095](../../tests/test_dialogue_context_pipeline.py#L95) | 95 | `"        seen[\"model_prompts\"].append(system_prompt)"` | — |
| [SRC-29A9CD43D1-L000096](../../tests/test_dialogue_context_pipeline.py#L96) | 96 | `"        if \"أنت محلل سياق حواري\" in system_prompt:"` | — |
| [SRC-29A9CD43D1-L000097](../../tests/test_dialogue_context_pipeline.py#L97) | 97 | `"            return json.dumps(context, ensure_ascii=False)"` | — |
| [SRC-29A9CD43D1-L000098](../../tests/test_dialogue_context_pipeline.py#L98) | 98 | `"        if \"أنت مخطط بحث ومحلل دلالي حواري\" in system_prompt:"` | — |
| [SRC-29A9CD43D1-L000099](../../tests/test_dialogue_context_pipeline.py#L99) | 99 | `"            return json.dumps("` | — |
| [SRC-29A9CD43D1-L000100](../../tests/test_dialogue_context_pipeline.py#L100) | 100 | `"                {"` | — |
| [SRC-29A9CD43D1-L000101](../../tests/test_dialogue_context_pipeline.py#L101) | 101 | `"                    \"queries\": ["` | — |
| [SRC-29A9CD43D1-L000102](../../tests/test_dialogue_context_pipeline.py#L102) | 102 | `"                        \"iPhone 17 256GB الضمان الدولي في مصر تغطية الصيانة warranty Egypt\""` | — |
| [SRC-29A9CD43D1-L000103](../../tests/test_dialogue_context_pipeline.py#L103) | 103 | `"                    ],"` | — |
| [SRC-29A9CD43D1-L000104](../../tests/test_dialogue_context_pipeline.py#L104) | 104 | `"                    \"direct_urls\": [],"` | — |
| [SRC-29A9CD43D1-L000105](../../tests/test_dialogue_context_pipeline.py#L105) | 105 | `"                    \"social_focus\": False,"` | — |
| [SRC-29A9CD43D1-L000106](../../tests/test_dialogue_context_pipeline.py#L106) | 106 | `"                    \"freshness\": \"current\","` | — |
| [SRC-29A9CD43D1-L000107](../../tests/test_dialogue_context_pipeline.py#L107) | 107 | `"                    \"depth\": \"standard\","` | — |
| [SRC-29A9CD43D1-L000108](../../tests/test_dialogue_context_pipeline.py#L108) | 108 | `"                    \"platforms\": [],"` | — |
| [SRC-29A9CD43D1-L000109](../../tests/test_dialogue_context_pipeline.py#L109) | 109 | `"                    \"dialogue_context\": context,"` | — |
| [SRC-29A9CD43D1-L000110](../../tests/test_dialogue_context_pipeline.py#L110) | 110 | `"                },"` | — |
| [SRC-29A9CD43D1-L000111](../../tests/test_dialogue_context_pipeline.py#L111) | 111 | `"                ensure_ascii=False,"` | — |
| [SRC-29A9CD43D1-L000112](../../tests/test_dialogue_context_pipeline.py#L112) | 112 | `"            )"` | — |
| [SRC-29A9CD43D1-L000113](../../tests/test_dialogue_context_pipeline.py#L113) | 113 | `"        pytest.fail(\"Unexpected model prompt in mocked offline test\")"` | — |
| [SRC-29A9CD43D1-L000114](../../tests/test_dialogue_context_pipeline.py#L114) | 114 | `""` | — |
| [SRC-29A9CD43D1-L000115](../../tests/test_dialogue_context_pipeline.py#L115) | 115 | `"    monkeypatch.setattr(agent, \"_request_completion\", mocked_completion)"` | — |
| [SRC-29A9CD43D1-L000116](../../tests/test_dialogue_context_pipeline.py#L116) | 116 | `"    seen[\"generated_question\"] = None"` | — |
| [SRC-29A9CD43D1-L000117](../../tests/test_dialogue_context_pipeline.py#L117) | 117 | `"    seen[\"reviewed_question\"] = None"` | — |
| [SRC-29A9CD43D1-L000118](../../tests/test_dialogue_context_pipeline.py#L118) | 118 | `""` | — |
| [SRC-29A9CD43D1-L000119](../../tests/test_dialogue_context_pipeline.py#L119) | 119 | `"    def collect(plan):"` | — |
| [SRC-29A9CD43D1-L000120](../../tests/test_dialogue_context_pipeline.py#L120) | 120 | `"        seen[\"plan\"] = dict(plan)"` | — |
| [SRC-29A9CD43D1-L000121](../../tests/test_dialogue_context_pipeline.py#L121) | 121 | `"        sources = [_source(\"example.com\", plan[\"queries\"]), _source(\"example.net\", plan[\"queries\"])]"` | — |
| [SRC-29A9CD43D1-L000122](../../tests/test_dialogue_context_pipeline.py#L122) | 122 | `"        return sources, [], _report(plan, sources)"` | — |
| [SRC-29A9CD43D1-L000123](../../tests/test_dialogue_context_pipeline.py#L123) | 123 | `""` | — |
| [SRC-29A9CD43D1-L000124](../../tests/test_dialogue_context_pipeline.py#L124) | 124 | `"    def generate(resolved_question, *args, **kwargs):"` | — |
| [SRC-29A9CD43D1-L000125](../../tests/test_dialogue_context_pipeline.py#L125) | 125 | `"        seen[\"generated_question\"] = resolved_question"` | — |
| [SRC-29A9CD43D1-L000126](../../tests/test_dialogue_context_pipeline.py#L126) | 126 | `"        return \"لم أؤكد شروط الضمان من النصوص المتاحة؛ راجع الشروط الرسمية [المصدر 1].\""` | — |
| [SRC-29A9CD43D1-L000127](../../tests/test_dialogue_context_pipeline.py#L127) | 127 | `""` | — |
| [SRC-29A9CD43D1-L000128](../../tests/test_dialogue_context_pipeline.py#L128) | 128 | `"    def review(resolved_question, answer, sources):"` | — |
| [SRC-29A9CD43D1-L000129](../../tests/test_dialogue_context_pipeline.py#L129) | 129 | `"        seen[\"reviewed_question\"] = resolved_question"` | — |
| [SRC-29A9CD43D1-L000130](../../tests/test_dialogue_context_pipeline.py#L130) | 130 | `"        return answer"` | — |
| [SRC-29A9CD43D1-L000131](../../tests/test_dialogue_context_pipeline.py#L131) | 131 | `""` | — |
| [SRC-29A9CD43D1-L000132](../../tests/test_dialogue_context_pipeline.py#L132) | 132 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-29A9CD43D1-L000133](../../tests/test_dialogue_context_pipeline.py#L133) | 133 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda _query, _source: True)"` | — |
| [SRC-29A9CD43D1-L000134](../../tests/test_dialogue_context_pipeline.py#L134) | 134 | `"    monkeypatch.setattr(agent, \"_generate\", generate)"` | — |
| [SRC-29A9CD43D1-L000135](../../tests/test_dialogue_context_pipeline.py#L135) | 135 | `"    monkeypatch.setattr(agent, \"_review_answer\", review)"` | — |
| [SRC-29A9CD43D1-L000136](../../tests/test_dialogue_context_pipeline.py#L136) | 136 | `""` | — |
| [SRC-29A9CD43D1-L000137](../../tests/test_dialogue_context_pipeline.py#L137) | 137 | `"    question = \"وطب الضمان الدولي بيسري في مصر؟\""` | — |
| [SRC-29A9CD43D1-L000138](../../tests/test_dialogue_context_pipeline.py#L138) | 138 | `"    result = agent.answer(question, history=history)"` | — |
| [SRC-29A9CD43D1-L000139](../../tests/test_dialogue_context_pipeline.py#L139) | 139 | `""` | — |
| [SRC-29A9CD43D1-L000140](../../tests/test_dialogue_context_pipeline.py#L140) | 140 | `"    assert result[\"intent_route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-29A9CD43D1-L000141](../../tests/test_dialogue_context_pipeline.py#L141) | 141 | `"    assert result[\"question\"] == question  # Preserve the visible user utterance."` | — |
| [SRC-29A9CD43D1-L000142](../../tests/test_dialogue_context_pipeline.py#L142) | 142 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-29A9CD43D1-L000143](../../tests/test_dialogue_context_pipeline.py#L143) | 143 | `"    assert len(seen[\"model_prompts\"]) == 2  # one context pass + one search-plan pass"` | — |
| [SRC-29A9CD43D1-L000144](../../tests/test_dialogue_context_pipeline.py#L144) | 144 | `"    assert \"iPhone 17\" in seen[\"generated_question\"]"` | — |
| [SRC-29A9CD43D1-L000145](../../tests/test_dialogue_context_pipeline.py#L145) | 145 | `"    assert \"256 جيجابايت\" in seen[\"generated_question\"]"` | — |
| [SRC-29A9CD43D1-L000146](../../tests/test_dialogue_context_pipeline.py#L146) | 146 | `"    assert \"الضمان الدولي\" in seen[\"generated_question\"]"` | — |
| [SRC-29A9CD43D1-L000147](../../tests/test_dialogue_context_pipeline.py#L147) | 147 | `"    assert seen[\"reviewed_question\"] == seen[\"generated_question\"]"` | — |
| [SRC-29A9CD43D1-L000148](../../tests/test_dialogue_context_pipeline.py#L148) | 148 | `"    context_result = result[\"research_plan\"][\"dialogue_context\"]"` | — |
| [SRC-29A9CD43D1-L000149](../../tests/test_dialogue_context_pipeline.py#L149) | 149 | `"    assert context_result[\"method\"] == \"llm_semantic_context\""` | — |
| [SRC-29A9CD43D1-L000150](../../tests/test_dialogue_context_pipeline.py#L150) | 150 | `"    assert context_result[\"slots\"][\"country\"] == \"مصر\""` | — |
| [SRC-29A9CD43D1-L000151](../../tests/test_dialogue_context_pipeline.py#L151) | 151 | `"    assert context_result[\"changed_slots\"] == [\"aspect\"]"` | — |
| [SRC-29A9CD43D1-L000152](../../tests/test_dialogue_context_pipeline.py#L152) | 152 | `"    assert context_result[\"needs_web\"] is True"` | — |
| [SRC-29A9CD43D1-L000153](../../tests/test_dialogue_context_pipeline.py#L153) | 153 | `""` | — |
| [SRC-29A9CD43D1-L000154](../../tests/test_dialogue_context_pipeline.py#L154) | 154 | `""` | — |
| [SRC-29A9CD43D1-L000155](../../tests/test_dialogue_context_pipeline.py#L155) | 155 | `"def test_semantic_context_asks_before_search_when_two_referents_are_plausible("` | — |
| [SRC-29A9CD43D1-L000156](../../tests/test_dialogue_context_pipeline.py#L156) | 156 | `"    monkeypatch: pytest.MonkeyPatch,"` | — |
| [SRC-29A9CD43D1-L000157](../../tests/test_dialogue_context_pipeline.py#L157) | 157 | `") -> None:"` | — |
| [SRC-29A9CD43D1-L000158](../../tests/test_dialogue_context_pipeline.py#L158) | 158 | `"    agent = WebAgent()"` | — |
| [SRC-29A9CD43D1-L000159](../../tests/test_dialogue_context_pipeline.py#L159) | 159 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-29A9CD43D1-L000160](../../tests/test_dialogue_context_pipeline.py#L160) | 160 | `"    history = ["` | — |
| [SRC-29A9CD43D1-L000161](../../tests/test_dialogue_context_pipeline.py#L161) | 161 | `"        {\"role\": \"user\", \"content\": \"قارن بين iPhone 17 وSamsung S26\"},"` | — |
| [SRC-29A9CD43D1-L000162](../../tests/test_dialogue_context_pipeline.py#L162) | 162 | `"        {\"role\": \"assistant\", \"content\": \"ذكرت الهاتفين في المقارنة.\"},"` | — |
| [SRC-29A9CD43D1-L000163](../../tests/test_dialogue_context_pipeline.py#L163) | 163 | `"    ]"` | — |
| [SRC-29A9CD43D1-L000164](../../tests/test_dialogue_context_pipeline.py#L164) | 164 | `"    ambiguous = {"` | — |
| [SRC-29A9CD43D1-L000165](../../tests/test_dialogue_context_pipeline.py#L165) | 165 | `"        \"resolved_question\": \"What about the second one?\","` | — |
| [SRC-29A9CD43D1-L000166](../../tests/test_dialogue_context_pipeline.py#L166) | 166 | `"        \"intent\": \"compare\","` | — |
| [SRC-29A9CD43D1-L000167](../../tests/test_dialogue_context_pipeline.py#L167) | 167 | `"        \"topic\": \"اختيار الهاتف\","` | — |
| [SRC-29A9CD43D1-L000168](../../tests/test_dialogue_context_pipeline.py#L168) | 168 | `"        \"entities\": [\"iPhone 17\", \"Samsung S26\"],"` | — |
| [SRC-29A9CD43D1-L000169](../../tests/test_dialogue_context_pipeline.py#L169) | 169 | `"        \"slots\": {\"aspect\": \"الاختيار\"},"` | — |
| [SRC-29A9CD43D1-L000170](../../tests/test_dialogue_context_pipeline.py#L170) | 170 | `"        \"changed_slots\": [],"` | — |
| [SRC-29A9CD43D1-L000171](../../tests/test_dialogue_context_pipeline.py#L171) | 171 | `"        \"is_follow_up\": True,"` | — |
| [SRC-29A9CD43D1-L000172](../../tests/test_dialogue_context_pipeline.py#L172) | 172 | `"        \"topic_shift\": False,"` | — |
| [SRC-29A9CD43D1-L000173](../../tests/test_dialogue_context_pipeline.py#L173) | 173 | `"        \"needs_web\": False,"` | — |
| [SRC-29A9CD43D1-L000174](../../tests/test_dialogue_context_pipeline.py#L174) | 174 | `"        \"research_depth\": \"standard\","` | — |
| [SRC-29A9CD43D1-L000175](../../tests/test_dialogue_context_pipeline.py#L175) | 175 | `"        \"needs_clarification\": True,"` | — |
| [SRC-29A9CD43D1-L000176](../../tests/test_dialogue_context_pipeline.py#L176) | 176 | `"        \"clarification_question\": \"تقصد أي هاتف تحديدًا: iPhone 17 أم Samsung S26؟\","` | — |
| [SRC-29A9CD43D1-L000177](../../tests/test_dialogue_context_pipeline.py#L177) | 177 | `"        \"unresolved_references\": [\"the second one\"],"` | — |
| [SRC-29A9CD43D1-L000178](../../tests/test_dialogue_context_pipeline.py#L178) | 178 | `"        \"resolution_basis\": \"insufficient_evidence\","` | — |
| [SRC-29A9CD43D1-L000179](../../tests/test_dialogue_context_pipeline.py#L179) | 179 | `"        \"confidence_band\": \"low\","` | — |
| [SRC-29A9CD43D1-L000180](../../tests/test_dialogue_context_pipeline.py#L180) | 180 | `"    }"` | — |
| [SRC-29A9CD43D1-L000181](../../tests/test_dialogue_context_pipeline.py#L181) | 181 | `""` | — |
| [SRC-29A9CD43D1-L000182](../../tests/test_dialogue_context_pipeline.py#L182) | 182 | `"    def mocked_completion(messages, **kwargs):"` | — |
| [SRC-29A9CD43D1-L000183](../../tests/test_dialogue_context_pipeline.py#L183) | 183 | `"        assert \"أنت محلل سياق حواري\" in messages[0][\"content\"]"` | — |
| [SRC-29A9CD43D1-L000184](../../tests/test_dialogue_context_pipeline.py#L184) | 184 | `"        return json.dumps(ambiguous, ensure_ascii=False)"` | — |
| [SRC-29A9CD43D1-L000185](../../tests/test_dialogue_context_pipeline.py#L185) | 185 | `""` | — |
| [SRC-29A9CD43D1-L000186](../../tests/test_dialogue_context_pipeline.py#L186) | 186 | `"    def forbidden_search(*args, **kwargs):"` | — |
| [SRC-29A9CD43D1-L000187](../../tests/test_dialogue_context_pipeline.py#L187) | 187 | `"        pytest.fail(\"An unresolved referent must not start web research.\")"` | — |
| [SRC-29A9CD43D1-L000188](../../tests/test_dialogue_context_pipeline.py#L188) | 188 | `""` | — |
| [SRC-29A9CD43D1-L000189](../../tests/test_dialogue_context_pipeline.py#L189) | 189 | `"    monkeypatch.setattr(agent, \"_request_completion\", mocked_completion)"` | — |
| [SRC-29A9CD43D1-L000190](../../tests/test_dialogue_context_pipeline.py#L190) | 190 | `"    monkeypatch.setattr(agent, \"_collect_research\", forbidden_search)"` | — |
| [SRC-29A9CD43D1-L000191](../../tests/test_dialogue_context_pipeline.py#L191) | 191 | `""` | — |
| [SRC-29A9CD43D1-L000192](../../tests/test_dialogue_context_pipeline.py#L192) | 192 | `"    result = agent.answer(\"What about the second one?\", history=history)"` | — |
| [SRC-29A9CD43D1-L000193](../../tests/test_dialogue_context_pipeline.py#L193) | 193 | `""` | — |
| [SRC-29A9CD43D1-L000194](../../tests/test_dialogue_context_pipeline.py#L194) | 194 | `"    assert result[\"kind\"] == \"clarification_needed\""` | — |
| [SRC-29A9CD43D1-L000195](../../tests/test_dialogue_context_pipeline.py#L195) | 195 | `"    assert result[\"intent_route\"] == \"CLARIFY\""` | — |
| [SRC-29A9CD43D1-L000196](../../tests/test_dialogue_context_pipeline.py#L196) | 196 | `"    assert \"iPhone 17\" in result[\"answer\"]"` | — |
| [SRC-29A9CD43D1-L000197](../../tests/test_dialogue_context_pipeline.py#L197) | 197 | `"    assert \"Samsung S26\" in result[\"answer\"]"` | — |
| [SRC-29A9CD43D1-L000198](../../tests/test_dialogue_context_pipeline.py#L198) | 198 | `"    assert result[\"dialogue_context\"][\"needs_clarification\"] is True"` | — |
| [SRC-29A9CD43D1-L000199](../../tests/test_dialogue_context_pipeline.py#L199) | 199 | `"    assert result[\"used_web_search\"] is False"` | — |
| [SRC-29A9CD43D1-L000200](../../tests/test_dialogue_context_pipeline.py#L200) | 200 | `""` | — |
| [SRC-29A9CD43D1-L000201](../../tests/test_dialogue_context_pipeline.py#L201) | 201 | `"def test_semantic_probe_catches_implicit_context_without_keyword_trigger("` | — |
| [SRC-29A9CD43D1-L000202](../../tests/test_dialogue_context_pipeline.py#L202) | 202 | `"    monkeypatch: pytest.MonkeyPatch,"` | — |
| [SRC-29A9CD43D1-L000203](../../tests/test_dialogue_context_pipeline.py#L203) | 203 | `") -> None:"` | — |
| [SRC-29A9CD43D1-L000204](../../tests/test_dialogue_context_pipeline.py#L204) | 204 | `"    agent = WebAgent()"` | — |
| [SRC-29A9CD43D1-L000205](../../tests/test_dialogue_context_pipeline.py#L205) | 205 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-29A9CD43D1-L000206](../../tests/test_dialogue_context_pipeline.py#L206) | 206 | `"    question = \"في وضعي، أبدأ بإيه؟\""` | — |
| [SRC-29A9CD43D1-L000207](../../tests/test_dialogue_context_pipeline.py#L207) | 207 | `"    history = ["` | — |
| [SRC-29A9CD43D1-L000208](../../tests/test_dialogue_context_pipeline.py#L208) | 208 | `"        {"` | — |
| [SRC-29A9CD43D1-L000209](../../tests/test_dialogue_context_pipeline.py#L209) | 209 | `"            \"role\": \"user\","` | — |
| [SRC-29A9CD43D1-L000210](../../tests/test_dialogue_context_pipeline.py#L210) | 210 | `"            \"content\": ("` | — |
| [SRC-29A9CD43D1-L000211](../../tests/test_dialogue_context_pipeline.py#L211) | 211 | `"                \"عندي امتحان كيمياء بكرة، وفاضلي ساعتين أراجع الاتزان الكيميائي \""` | — |
| [SRC-29A9CD43D1-L000212](../../tests/test_dialogue_context_pipeline.py#L212) | 212 | `"                \"ومش فاهمه كويس.\""` | — |
| [SRC-29A9CD43D1-L000213](../../tests/test_dialogue_context_pipeline.py#L213) | 213 | `"            ),"` | — |
| [SRC-29A9CD43D1-L000214](../../tests/test_dialogue_context_pipeline.py#L214) | 214 | `"        },"` | — |
| [SRC-29A9CD43D1-L000215](../../tests/test_dialogue_context_pipeline.py#L215) | 215 | `"        {"` | — |
| [SRC-29A9CD43D1-L000216](../../tests/test_dialogue_context_pipeline.py#L216) | 216 | `"            \"role\": \"assistant\","` | — |
| [SRC-29A9CD43D1-L000217](../../tests/test_dialogue_context_pipeline.py#L217) | 217 | `"            \"content\": \"نقدر نرتب الساعتين لمراجعة المفاهيم والتدريب على المسائل.\","` | — |
| [SRC-29A9CD43D1-L000218](../../tests/test_dialogue_context_pipeline.py#L218) | 218 | `"        },"` | — |
| [SRC-29A9CD43D1-L000219](../../tests/test_dialogue_context_pipeline.py#L219) | 219 | `"    ]"` | — |
| [SRC-29A9CD43D1-L000220](../../tests/test_dialogue_context_pipeline.py#L220) | 220 | `"    assert not might_be_context_dependent(question)"` | — |
| [SRC-29A9CD43D1-L000221](../../tests/test_dialogue_context_pipeline.py#L221) | 221 | `""` | — |
| [SRC-29A9CD43D1-L000222](../../tests/test_dialogue_context_pipeline.py#L222) | 222 | `"    semantic_context = {"` | — |
| [SRC-29A9CD43D1-L000223](../../tests/test_dialogue_context_pipeline.py#L223) | 223 | `"        \"resolved_question\": ("` | — |
| [SRC-29A9CD43D1-L000224](../../tests/test_dialogue_context_pipeline.py#L224) | 224 | `"            \"في ظل امتحان الكيمياء غدًا ووجود ساعتين لمراجعة الاتزان الكيميائي، \""` | — |
| [SRC-29A9CD43D1-L000225](../../tests/test_dialogue_context_pipeline.py#L225) | 225 | `"            \"بماذا أبدأ؟\""` | — |
| [SRC-29A9CD43D1-L000226](../../tests/test_dialogue_context_pipeline.py#L226) | 226 | `"        ),"` | — |
| [SRC-29A9CD43D1-L000227](../../tests/test_dialogue_context_pipeline.py#L227) | 227 | `"        \"intent\": \"how_to\","` | — |
| [SRC-29A9CD43D1-L000228](../../tests/test_dialogue_context_pipeline.py#L228) | 228 | `"        \"topic\": \"خطة مراجعة الاتزان الكيميائي\","` | — |
| [SRC-29A9CD43D1-L000229](../../tests/test_dialogue_context_pipeline.py#L229) | 229 | `"        \"entities\": [\"امتحان الكيمياء\", \"الاتزان الكيميائي\"],"` | — |
| [SRC-29A9CD43D1-L000230](../../tests/test_dialogue_context_pipeline.py#L230) | 230 | `"        \"slots\": {"` | — |
| [SRC-29A9CD43D1-L000231](../../tests/test_dialogue_context_pipeline.py#L231) | 231 | `"            \"goal\": \"مراجعة امتحان الكيمياء\","` | — |
| [SRC-29A9CD43D1-L000232](../../tests/test_dialogue_context_pipeline.py#L232) | 232 | `"            \"time_range\": \"ساعتان\","` | — |
| [SRC-29A9CD43D1-L000233](../../tests/test_dialogue_context_pipeline.py#L233) | 233 | `"            \"topic\": \"الاتزان الكيميائي\","` | — |
| [SRC-29A9CD43D1-L000234](../../tests/test_dialogue_context_pipeline.py#L234) | 234 | `"        },"` | — |
| [SRC-29A9CD43D1-L000235](../../tests/test_dialogue_context_pipeline.py#L235) | 235 | `"        \"changed_slots\": [\"goal\"],"` | — |
| [SRC-29A9CD43D1-L000236](../../tests/test_dialogue_context_pipeline.py#L236) | 236 | `"        \"is_follow_up\": True,"` | — |
| [SRC-29A9CD43D1-L000237](../../tests/test_dialogue_context_pipeline.py#L237) | 237 | `"        \"topic_shift\": False,"` | — |
| [SRC-29A9CD43D1-L000238](../../tests/test_dialogue_context_pipeline.py#L238) | 238 | `"        \"needs_web\": False,"` | — |
| [SRC-29A9CD43D1-L000239](../../tests/test_dialogue_context_pipeline.py#L239) | 239 | `"        \"research_depth\": \"standard\","` | — |
| [SRC-29A9CD43D1-L000240](../../tests/test_dialogue_context_pipeline.py#L240) | 240 | `"        \"needs_clarification\": False,"` | — |
| [SRC-29A9CD43D1-L000241](../../tests/test_dialogue_context_pipeline.py#L241) | 241 | `"        \"clarification_question\": \"\","` | — |
| [SRC-29A9CD43D1-L000242](../../tests/test_dialogue_context_pipeline.py#L242) | 242 | `"        \"unresolved_references\": [],"` | — |
| [SRC-29A9CD43D1-L000243](../../tests/test_dialogue_context_pipeline.py#L243) | 243 | `"        \"resolution_basis\": \"history_inferred\","` | — |
| [SRC-29A9CD43D1-L000244](../../tests/test_dialogue_context_pipeline.py#L244) | 244 | `"        \"confidence_band\": \"medium\","` | — |
| [SRC-29A9CD43D1-L000245](../../tests/test_dialogue_context_pipeline.py#L245) | 245 | `"    }"` | — |
| [SRC-29A9CD43D1-L000246](../../tests/test_dialogue_context_pipeline.py#L246) | 246 | `"    seen: dict[str, Any] = {\"context_calls\": 0}"` | — |
| [SRC-29A9CD43D1-L000247](../../tests/test_dialogue_context_pipeline.py#L247) | 247 | `""` | — |
| [SRC-29A9CD43D1-L000248](../../tests/test_dialogue_context_pipeline.py#L248) | 248 | `"    def mocked_completion(messages, **kwargs):"` | — |
| [SRC-29A9CD43D1-L000249](../../tests/test_dialogue_context_pipeline.py#L249) | 249 | `"        assert \"أنت محلل سياق حواري\" in messages[0][\"content\"]"` | — |
| [SRC-29A9CD43D1-L000250](../../tests/test_dialogue_context_pipeline.py#L250) | 250 | `"        seen[\"context_calls\"] += 1"` | — |
| [SRC-29A9CD43D1-L000251](../../tests/test_dialogue_context_pipeline.py#L251) | 251 | `"        return json.dumps(semantic_context, ensure_ascii=False)"` | — |
| [SRC-29A9CD43D1-L000252](../../tests/test_dialogue_context_pipeline.py#L252) | 252 | `""` | — |
| [SRC-29A9CD43D1-L000253](../../tests/test_dialogue_context_pipeline.py#L253) | 253 | `"    def answer_without_search(resolved_question, prior_history):"` | — |
| [SRC-29A9CD43D1-L000254](../../tests/test_dialogue_context_pipeline.py#L254) | 254 | `"        seen[\"resolved_question\"] = resolved_question"` | — |
| [SRC-29A9CD43D1-L000255](../../tests/test_dialogue_context_pipeline.py#L255) | 255 | `"        return {"` | — |
| [SRC-29A9CD43D1-L000256](../../tests/test_dialogue_context_pipeline.py#L256) | 256 | `"            \"answer\": \"ابدأ بمراجعة أساسيات الاتزان ثم حل أمثلة قصيرة.\","` | — |
| [SRC-29A9CD43D1-L000257](../../tests/test_dialogue_context_pipeline.py#L257) | 257 | `"            \"question\": resolved_question,"` | — |
| [SRC-29A9CD43D1-L000258](../../tests/test_dialogue_context_pipeline.py#L258) | 258 | `"            \"search_query\": resolved_question,"` | — |
| [SRC-29A9CD43D1-L000259](../../tests/test_dialogue_context_pipeline.py#L259) | 259 | `"            \"search_queries\": [],"` | — |
| [SRC-29A9CD43D1-L000260](../../tests/test_dialogue_context_pipeline.py#L260) | 260 | `"            \"research_plan\": {"` | — |
| [SRC-29A9CD43D1-L000261](../../tests/test_dialogue_context_pipeline.py#L261) | 261 | `"                \"mode\": \"auto\","` | — |
| [SRC-29A9CD43D1-L000262](../../tests/test_dialogue_context_pipeline.py#L262) | 262 | `"                \"planning_method\": \"general_qa_without_web\","` | — |
| [SRC-29A9CD43D1-L000263](../../tests/test_dialogue_context_pipeline.py#L263) | 263 | `"                \"web_search_skipped\": True,"` | — |
| [SRC-29A9CD43D1-L000264](../../tests/test_dialogue_context_pipeline.py#L264) | 264 | `"            },"` | — |
| [SRC-29A9CD43D1-L000265](../../tests/test_dialogue_context_pipeline.py#L265) | 265 | `"            \"sources\": [],"` | — |
| [SRC-29A9CD43D1-L000266](../../tests/test_dialogue_context_pipeline.py#L266) | 266 | `"            \"used_language_model\": True,"` | — |
| [SRC-29A9CD43D1-L000267](../../tests/test_dialogue_context_pipeline.py#L267) | 267 | `"            \"used_web_search\": False,"` | — |
| [SRC-29A9CD43D1-L000268](../../tests/test_dialogue_context_pipeline.py#L268) | 268 | `"            \"search_attempted\": False,"` | — |
| [SRC-29A9CD43D1-L000269](../../tests/test_dialogue_context_pipeline.py#L269) | 269 | `"            \"used_social_search\": False,"` | — |
| [SRC-29A9CD43D1-L000270](../../tests/test_dialogue_context_pipeline.py#L270) | 270 | `"            \"warnings\": [],"` | — |
| [SRC-29A9CD43D1-L000271](../../tests/test_dialogue_context_pipeline.py#L271) | 271 | `"            \"kind\": \"general_answer\","` | — |
| [SRC-29A9CD43D1-L000272](../../tests/test_dialogue_context_pipeline.py#L272) | 272 | `"            \"research_quality\": \"not_applicable\","` | — |
| [SRC-29A9CD43D1-L000273](../../tests/test_dialogue_context_pipeline.py#L273) | 273 | `"            \"model_calls\": [],"` | — |
| [SRC-29A9CD43D1-L000274](../../tests/test_dialogue_context_pipeline.py#L274) | 274 | `"        }"` | — |
| [SRC-29A9CD43D1-L000275](../../tests/test_dialogue_context_pipeline.py#L275) | 275 | `""` | — |
| [SRC-29A9CD43D1-L000276](../../tests/test_dialogue_context_pipeline.py#L276) | 276 | `"    def forbidden_search(*args, **kwargs):"` | — |
| [SRC-29A9CD43D1-L000277](../../tests/test_dialogue_context_pipeline.py#L277) | 277 | `"        pytest.fail(\"This contextual study-plan question must not start web search.\")"` | — |
| [SRC-29A9CD43D1-L000278](../../tests/test_dialogue_context_pipeline.py#L278) | 278 | `""` | — |
| [SRC-29A9CD43D1-L000279](../../tests/test_dialogue_context_pipeline.py#L279) | 279 | `"    monkeypatch.setattr(agent, \"_request_completion\", mocked_completion)"` | — |
| [SRC-29A9CD43D1-L000280](../../tests/test_dialogue_context_pipeline.py#L280) | 280 | `"    monkeypatch.setattr(agent, \"_answer_without_search\", answer_without_search)"` | — |
| [SRC-29A9CD43D1-L000281](../../tests/test_dialogue_context_pipeline.py#L281) | 281 | `"    monkeypatch.setattr(agent, \"_collect_research\", forbidden_search)"` | — |
| [SRC-29A9CD43D1-L000282](../../tests/test_dialogue_context_pipeline.py#L282) | 282 | `""` | — |
| [SRC-29A9CD43D1-L000283](../../tests/test_dialogue_context_pipeline.py#L283) | 283 | `"    result = agent.answer(question, history=history)"` | — |
| [SRC-29A9CD43D1-L000284](../../tests/test_dialogue_context_pipeline.py#L284) | 284 | `""` | — |
| [SRC-29A9CD43D1-L000285](../../tests/test_dialogue_context_pipeline.py#L285) | 285 | `"    assert seen[\"context_calls\"] == 1"` | — |
| [SRC-29A9CD43D1-L000286](../../tests/test_dialogue_context_pipeline.py#L286) | 286 | `"    assert \"الكيمياء\" in seen[\"resolved_question\"]"` | — |
| [SRC-29A9CD43D1-L000287](../../tests/test_dialogue_context_pipeline.py#L287) | 287 | `"    assert \"ساعتين\" in seen[\"resolved_question\"]"` | — |
| [SRC-29A9CD43D1-L000288](../../tests/test_dialogue_context_pipeline.py#L288) | 288 | `"    assert \"الاتزان الكيميائي\" in seen[\"resolved_question\"]"` | — |
| [SRC-29A9CD43D1-L000289](../../tests/test_dialogue_context_pipeline.py#L289) | 289 | `"    assert result[\"question\"] == question"` | — |
| [SRC-29A9CD43D1-L000290](../../tests/test_dialogue_context_pipeline.py#L290) | 290 | `"    assert result[\"dialogue_context\"][\"is_follow_up\"] is True"` | — |
| [SRC-29A9CD43D1-L000291](../../tests/test_dialogue_context_pipeline.py#L291) | 291 | `"    assert result[\"used_web_search\"] is False"` | — |
| [SRC-29A9CD43D1-L000292](../../tests/test_dialogue_context_pipeline.py#L292) | 292 | `"    assert result[\"search_attempted\"] is False"` | — |
| [SRC-29A9CD43D1-L000293](../../tests/test_dialogue_context_pipeline.py#L293) | 293 | `""` | — |
## اختبارات

### FILE-DA139AC9D0 — [tests/test_dialogue_state.py](../../tests/test_dialogue_state.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-DA139AC9D0-L000001](../../tests/test_dialogue_state.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-DA139AC9D0-L000002](../../tests/test_dialogue_state.py#L2) | 2 | `""` | — |
| [SRC-DA139AC9D0-L000003](../../tests/test_dialogue_state.py#L3) | 3 | `"from agents.dialogue_state import ("` | — |
| [SRC-DA139AC9D0-L000004](../../tests/test_dialogue_state.py#L4) | 4 | `"    fallback_dialogue_context,"` | — |
| [SRC-DA139AC9D0-L000005](../../tests/test_dialogue_state.py#L5) | 5 | `"    might_be_context_dependent,"` | — |
| [SRC-DA139AC9D0-L000006](../../tests/test_dialogue_state.py#L6) | 6 | `"    validate_dialogue_context,"` | — |
| [SRC-DA139AC9D0-L000007](../../tests/test_dialogue_state.py#L7) | 7 | `")"` | — |
| [SRC-DA139AC9D0-L000008](../../tests/test_dialogue_state.py#L8) | 8 | `""` | — |
| [SRC-DA139AC9D0-L000009](../../tests/test_dialogue_state.py#L9) | 9 | `""` | — |
| [SRC-DA139AC9D0-L000010](../../tests/test_dialogue_state.py#L10) | 10 | `"def test_deterministic_fallback_preserves_explicit_followup_topic() -> None:"` | — |
| [SRC-DA139AC9D0-L000011](../../tests/test_dialogue_state.py#L11) | 11 | `"    history = ["` | — |
| [SRC-DA139AC9D0-L000012](../../tests/test_dialogue_state.py#L12) | 12 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر iPhone 17 في مصر\"},"` | — |
| [SRC-DA139AC9D0-L000013](../../tests/test_dialogue_state.py#L13) | 13 | `"        {\"role\": \"assistant\", \"content\": \"نتحدث عن هاتف iPhone 17 في السوق المصري.\"},"` | — |
| [SRC-DA139AC9D0-L000014](../../tests/test_dialogue_state.py#L14) | 14 | `"    ]"` | — |
| [SRC-DA139AC9D0-L000015](../../tests/test_dialogue_state.py#L15) | 15 | `""` | — |
| [SRC-DA139AC9D0-L000016](../../tests/test_dialogue_state.py#L16) | 16 | `"    context = fallback_dialogue_context(\"كام سعرها؟\", history)"` | — |
| [SRC-DA139AC9D0-L000017](../../tests/test_dialogue_state.py#L17) | 17 | `""` | — |
| [SRC-DA139AC9D0-L000018](../../tests/test_dialogue_state.py#L18) | 18 | `"    assert context[\"method\"] == \"deterministic_followup_heuristic\""` | — |
| [SRC-DA139AC9D0-L000019](../../tests/test_dialogue_state.py#L19) | 19 | `"    assert context[\"is_follow_up\"] is True"` | — |
| [SRC-DA139AC9D0-L000020](../../tests/test_dialogue_state.py#L20) | 20 | `"    assert \"iPhone 17\" in context[\"resolved_question\"]"` | — |
| [SRC-DA139AC9D0-L000021](../../tests/test_dialogue_state.py#L21) | 21 | `"    assert \"كام سعرها\" in context[\"resolved_question\"]"` | — |
| [SRC-DA139AC9D0-L000022](../../tests/test_dialogue_state.py#L22) | 22 | `"    assert context[\"confidence_band\"] == \"unassessed\""` | — |
| [SRC-DA139AC9D0-L000023](../../tests/test_dialogue_state.py#L23) | 23 | `""` | — |
| [SRC-DA139AC9D0-L000024](../../tests/test_dialogue_state.py#L24) | 24 | `""` | — |
| [SRC-DA139AC9D0-L000025](../../tests/test_dialogue_state.py#L25) | 25 | `"def test_topic_shift_is_a_hard_boundary_against_stale_context() -> None:"` | — |
| [SRC-DA139AC9D0-L000026](../../tests/test_dialogue_state.py#L26) | 26 | `"    question = \"ازاي أنظف شاشة اللابتوب بأمان؟\""` | — |
| [SRC-DA139AC9D0-L000027](../../tests/test_dialogue_state.py#L27) | 27 | `"    history = ["` | — |
| [SRC-DA139AC9D0-L000028](../../tests/test_dialogue_state.py#L28) | 28 | `"        {\"role\": \"user\", \"content\": \"قارن iPhone 17 وSamsung S26\"},"` | — |
| [SRC-DA139AC9D0-L000029](../../tests/test_dialogue_state.py#L29) | 29 | `"        {\"role\": \"assistant\", \"content\": \"هذه مقارنة بين هاتفين.\"},"` | — |
| [SRC-DA139AC9D0-L000030](../../tests/test_dialogue_state.py#L30) | 30 | `"    ]"` | — |
| [SRC-DA139AC9D0-L000031](../../tests/test_dialogue_state.py#L31) | 31 | `"    proposed = {"` | — |
| [SRC-DA139AC9D0-L000032](../../tests/test_dialogue_state.py#L32) | 32 | `"        \"resolved_question\": \"قارن iPhone 17 ثم ازاي أنظف شاشة اللابتوب بأمان\","` | — |
| [SRC-DA139AC9D0-L000033](../../tests/test_dialogue_state.py#L33) | 33 | `"        \"topic_shift\": True,"` | — |
| [SRC-DA139AC9D0-L000034](../../tests/test_dialogue_state.py#L34) | 34 | `"        \"is_follow_up\": True,"` | — |
| [SRC-DA139AC9D0-L000035](../../tests/test_dialogue_state.py#L35) | 35 | `"        \"intent\": \"how_to\","` | — |
| [SRC-DA139AC9D0-L000036](../../tests/test_dialogue_state.py#L36) | 36 | `"        \"needs_clarification\": False,"` | — |
| [SRC-DA139AC9D0-L000037](../../tests/test_dialogue_state.py#L37) | 37 | `"    }"` | — |
| [SRC-DA139AC9D0-L000038](../../tests/test_dialogue_state.py#L38) | 38 | `""` | — |
| [SRC-DA139AC9D0-L000039](../../tests/test_dialogue_state.py#L39) | 39 | `"    context = validate_dialogue_context(proposed, question, history)"` | — |
| [SRC-DA139AC9D0-L000040](../../tests/test_dialogue_state.py#L40) | 40 | `""` | — |
| [SRC-DA139AC9D0-L000041](../../tests/test_dialogue_state.py#L41) | 41 | `"    assert context[\"topic_shift\"] is True"` | — |
| [SRC-DA139AC9D0-L000042](../../tests/test_dialogue_state.py#L42) | 42 | `"    assert context[\"is_follow_up\"] is False"` | — |
| [SRC-DA139AC9D0-L000043](../../tests/test_dialogue_state.py#L43) | 43 | `"    assert context[\"resolved_question\"] == question"` | — |
| [SRC-DA139AC9D0-L000044](../../tests/test_dialogue_state.py#L44) | 44 | `"    assert context[\"resolution_basis\"] == \"current_message\""` | — |
| [SRC-DA139AC9D0-L000045](../../tests/test_dialogue_state.py#L45) | 45 | `"    assert context[\"topic\"] == \"\""` | — |
| [SRC-DA139AC9D0-L000046](../../tests/test_dialogue_state.py#L46) | 46 | `"    assert context[\"entities\"] == []"` | — |
| [SRC-DA139AC9D0-L000047](../../tests/test_dialogue_state.py#L47) | 47 | `"    assert context[\"slots\"] == {}"` | — |
| [SRC-DA139AC9D0-L000048](../../tests/test_dialogue_state.py#L48) | 48 | `"    assert context[\"changed_slots\"] == []"` | — |
| [SRC-DA139AC9D0-L000049](../../tests/test_dialogue_state.py#L49) | 49 | `""` | — |
| [SRC-DA139AC9D0-L000050](../../tests/test_dialogue_state.py#L50) | 50 | `""` | — |
| [SRC-DA139AC9D0-L000051](../../tests/test_dialogue_state.py#L51) | 51 | `"def test_standalone_question_cannot_inherit_old_topic_without_followup_signal() -> None:"` | — |
| [SRC-DA139AC9D0-L000052](../../tests/test_dialogue_state.py#L52) | 52 | `"    question = \"ازاي أنظف شاشة اللابتوب بأمان؟\""` | — |
| [SRC-DA139AC9D0-L000053](../../tests/test_dialogue_state.py#L53) | 53 | `"    history = ["` | — |
| [SRC-DA139AC9D0-L000054](../../tests/test_dialogue_state.py#L54) | 54 | `"        {\"role\": \"user\", \"content\": \"قارن iPhone 17 وSamsung S26 من حيث السعر\"},"` | — |
| [SRC-DA139AC9D0-L000055](../../tests/test_dialogue_state.py#L55) | 55 | `"        {\"role\": \"assistant\", \"content\": \"هذه مقارنة بين هاتفين.\"},"` | — |
| [SRC-DA139AC9D0-L000056](../../tests/test_dialogue_state.py#L56) | 56 | `"    ]"` | — |
| [SRC-DA139AC9D0-L000057](../../tests/test_dialogue_state.py#L57) | 57 | `"    proposed = {"` | — |
| [SRC-DA139AC9D0-L000058](../../tests/test_dialogue_state.py#L58) | 58 | `"        \"resolved_question\": \"قارن iPhone 17 ثم ازاي أنظف شاشة اللابتوب بأمان\","` | — |
| [SRC-DA139AC9D0-L000059](../../tests/test_dialogue_state.py#L59) | 59 | `"        \"topic\": \"مقارنة الهواتف\","` | — |
| [SRC-DA139AC9D0-L000060](../../tests/test_dialogue_state.py#L60) | 60 | `"        \"entities\": [\"iPhone 17\", \"Samsung S26\"],"` | — |
| [SRC-DA139AC9D0-L000061](../../tests/test_dialogue_state.py#L61) | 61 | `"        \"slots\": {\"product\": \"iPhone 17\", \"country\": \"مصر\"},"` | — |
| [SRC-DA139AC9D0-L000062](../../tests/test_dialogue_state.py#L62) | 62 | `"        \"changed_slots\": [\"aspect\"],"` | — |
| [SRC-DA139AC9D0-L000063](../../tests/test_dialogue_state.py#L63) | 63 | `"        \"is_follow_up\": False,"` | — |
| [SRC-DA139AC9D0-L000064](../../tests/test_dialogue_state.py#L64) | 64 | `"        \"topic_shift\": False,"` | — |
| [SRC-DA139AC9D0-L000065](../../tests/test_dialogue_state.py#L65) | 65 | `"        \"intent\": \"how_to\","` | — |
| [SRC-DA139AC9D0-L000066](../../tests/test_dialogue_state.py#L66) | 66 | `"        \"needs_clarification\": False,"` | — |
| [SRC-DA139AC9D0-L000067](../../tests/test_dialogue_state.py#L67) | 67 | `"    }"` | — |
| [SRC-DA139AC9D0-L000068](../../tests/test_dialogue_state.py#L68) | 68 | `""` | — |
| [SRC-DA139AC9D0-L000069](../../tests/test_dialogue_state.py#L69) | 69 | `"    context = validate_dialogue_context(proposed, question, history)"` | — |
| [SRC-DA139AC9D0-L000070](../../tests/test_dialogue_state.py#L70) | 70 | `""` | — |
| [SRC-DA139AC9D0-L000071](../../tests/test_dialogue_state.py#L71) | 71 | `"    assert context[\"resolved_question\"] == question"` | — |
| [SRC-DA139AC9D0-L000072](../../tests/test_dialogue_state.py#L72) | 72 | `"    assert context[\"is_follow_up\"] is False"` | — |
| [SRC-DA139AC9D0-L000073](../../tests/test_dialogue_state.py#L73) | 73 | `"    assert context[\"topic\"] == \"\""` | — |
| [SRC-DA139AC9D0-L000074](../../tests/test_dialogue_state.py#L74) | 74 | `"    assert context[\"entities\"] == []"` | — |
| [SRC-DA139AC9D0-L000075](../../tests/test_dialogue_state.py#L75) | 75 | `"    assert context[\"slots\"] == {}"` | — |
| [SRC-DA139AC9D0-L000076](../../tests/test_dialogue_state.py#L76) | 76 | `"    assert context[\"changed_slots\"] == []"` | — |
| [SRC-DA139AC9D0-L000077](../../tests/test_dialogue_state.py#L77) | 77 | `""` | — |
| [SRC-DA139AC9D0-L000078](../../tests/test_dialogue_state.py#L78) | 78 | `""` | — |
| [SRC-DA139AC9D0-L000079](../../tests/test_dialogue_state.py#L79) | 79 | `"def test_model_context_is_bounded_and_unknown_slots_are_dropped() -> None:"` | — |
| [SRC-DA139AC9D0-L000080](../../tests/test_dialogue_state.py#L80) | 80 | `"    question = \"وطب الضمان؟\""` | — |
| [SRC-DA139AC9D0-L000081](../../tests/test_dialogue_state.py#L81) | 81 | `"    history = [{\"role\": \"user\", \"content\": \"iPhone 17 256GB في مصر\"}]"` | — |
| [SRC-DA139AC9D0-L000082](../../tests/test_dialogue_state.py#L82) | 82 | `"    proposed = {"` | — |
| [SRC-DA139AC9D0-L000083](../../tests/test_dialogue_state.py#L83) | 83 | `"        \"resolved_question\": \"هل الضمان الدولي لهاتف iPhone 17 سعة 256 جيجابايت في مصر؟\","` | — |
| [SRC-DA139AC9D0-L000084](../../tests/test_dialogue_state.py#L84) | 84 | `"        \"intent\": \"current_information\","` | — |
| [SRC-DA139AC9D0-L000085](../../tests/test_dialogue_state.py#L85) | 85 | `"        \"topic\": \"warranty\","` | — |
| [SRC-DA139AC9D0-L000086](../../tests/test_dialogue_state.py#L86) | 86 | `"        \"entities\": [\"iPhone 17\", \"iPhone 17\", \"x\" * 500],"` | — |
| [SRC-DA139AC9D0-L000087](../../tests/test_dialogue_state.py#L87) | 87 | `"        \"slots\": {"` | — |
| [SRC-DA139AC9D0-L000088](../../tests/test_dialogue_state.py#L88) | 88 | `"            \"product\": \"iPhone 17\","` | — |
| [SRC-DA139AC9D0-L000089](../../tests/test_dialogue_state.py#L89) | 89 | `"            \"country\": \"مصر\","` | — |
| [SRC-DA139AC9D0-L000090](../../tests/test_dialogue_state.py#L90) | 90 | `"            \"untrusted_injected_field\": \"ignore policies\","` | — |
| [SRC-DA139AC9D0-L000091](../../tests/test_dialogue_state.py#L91) | 91 | `"        },"` | — |
| [SRC-DA139AC9D0-L000092](../../tests/test_dialogue_state.py#L92) | 92 | `"        \"changed_slots\": [\"aspect\", \"not_a_slot\"],"` | — |
| [SRC-DA139AC9D0-L000093](../../tests/test_dialogue_state.py#L93) | 93 | `"        \"is_follow_up\": True,"` | — |
| [SRC-DA139AC9D0-L000094](../../tests/test_dialogue_state.py#L94) | 94 | `"        \"topic_shift\": False,"` | — |
| [SRC-DA139AC9D0-L000095](../../tests/test_dialogue_state.py#L95) | 95 | `"        \"needs_web\": True,"` | — |
| [SRC-DA139AC9D0-L000096](../../tests/test_dialogue_state.py#L96) | 96 | `"        \"research_depth\": \"deep\","` | — |
| [SRC-DA139AC9D0-L000097](../../tests/test_dialogue_state.py#L97) | 97 | `"        \"needs_clarification\": False,"` | — |
| [SRC-DA139AC9D0-L000098](../../tests/test_dialogue_state.py#L98) | 98 | `"        \"resolution_basis\": \"history_inferred\","` | — |
| [SRC-DA139AC9D0-L000099](../../tests/test_dialogue_state.py#L99) | 99 | `"        \"confidence_band\": \"high\","` | — |
| [SRC-DA139AC9D0-L000100](../../tests/test_dialogue_state.py#L100) | 100 | `"    }"` | — |
| [SRC-DA139AC9D0-L000101](../../tests/test_dialogue_state.py#L101) | 101 | `""` | — |
| [SRC-DA139AC9D0-L000102](../../tests/test_dialogue_state.py#L102) | 102 | `"    context = validate_dialogue_context(proposed, question, history)"` | — |
| [SRC-DA139AC9D0-L000103](../../tests/test_dialogue_state.py#L103) | 103 | `""` | — |
| [SRC-DA139AC9D0-L000104](../../tests/test_dialogue_state.py#L104) | 104 | `"    assert context[\"method\"] == \"llm_semantic_context\""` | — |
| [SRC-DA139AC9D0-L000105](../../tests/test_dialogue_state.py#L105) | 105 | `"    assert context[\"is_follow_up\"] is True"` | — |
| [SRC-DA139AC9D0-L000106](../../tests/test_dialogue_state.py#L106) | 106 | `"    assert context[\"needs_web\"] is True"` | — |
| [SRC-DA139AC9D0-L000107](../../tests/test_dialogue_state.py#L107) | 107 | `"    assert context[\"research_depth\"] == \"deep\""` | — |
| [SRC-DA139AC9D0-L000108](../../tests/test_dialogue_state.py#L108) | 108 | `"    assert context[\"entities\"][0] == \"iPhone 17\""` | — |
| [SRC-DA139AC9D0-L000109](../../tests/test_dialogue_state.py#L109) | 109 | `"    assert len(context[\"entities\"]) == 2"` | — |
| [SRC-DA139AC9D0-L000110](../../tests/test_dialogue_state.py#L110) | 110 | `"    assert \"untrusted_injected_field\" not in context[\"slots\"]"` | — |
| [SRC-DA139AC9D0-L000111](../../tests/test_dialogue_state.py#L111) | 111 | `"    assert context[\"changed_slots\"] == [\"aspect\"]"` | — |
| [SRC-DA139AC9D0-L000112](../../tests/test_dialogue_state.py#L112) | 112 | `"    assert len(context[\"entities\"][1]) <= 180"` | — |
| [SRC-DA139AC9D0-L000113](../../tests/test_dialogue_state.py#L113) | 113 | `""` | — |
| [SRC-DA139AC9D0-L000114](../../tests/test_dialogue_state.py#L114) | 114 | `""` | — |
| [SRC-DA139AC9D0-L000115](../../tests/test_dialogue_state.py#L115) | 115 | `"def test_unresolved_reference_stays_unresolved_and_cannot_become_a_search_query() -> None:"` | — |
| [SRC-DA139AC9D0-L000116](../../tests/test_dialogue_state.py#L116) | 116 | `"    question = \"والبطارية؟\""` | — |
| [SRC-DA139AC9D0-L000117](../../tests/test_dialogue_state.py#L117) | 117 | `"    history = ["` | — |
| [SRC-DA139AC9D0-L000118](../../tests/test_dialogue_state.py#L118) | 118 | `"        {\"role\": \"user\", \"content\": \"قارن iPhone 17 وSamsung S26\"},"` | — |
| [SRC-DA139AC9D0-L000119](../../tests/test_dialogue_state.py#L119) | 119 | `"        {\"role\": \"assistant\", \"content\": \"ذكرت الهاتفين في المقارنة.\"},"` | — |
| [SRC-DA139AC9D0-L000120](../../tests/test_dialogue_state.py#L120) | 120 | `"    ]"` | — |
| [SRC-DA139AC9D0-L000121](../../tests/test_dialogue_state.py#L121) | 121 | `"    proposed = {"` | — |
| [SRC-DA139AC9D0-L000122](../../tests/test_dialogue_state.py#L122) | 122 | `"        \"resolved_question\": \"سعر بطارية iPhone 17\","` | — |
| [SRC-DA139AC9D0-L000123](../../tests/test_dialogue_state.py#L123) | 123 | `"        \"intent\": \"compare\","` | — |
| [SRC-DA139AC9D0-L000124](../../tests/test_dialogue_state.py#L124) | 124 | `"        \"entities\": [\"iPhone 17\", \"Samsung S26\"],"` | — |
| [SRC-DA139AC9D0-L000125](../../tests/test_dialogue_state.py#L125) | 125 | `"        \"is_follow_up\": True,"` | — |
| [SRC-DA139AC9D0-L000126](../../tests/test_dialogue_state.py#L126) | 126 | `"        \"topic_shift\": False,"` | — |
| [SRC-DA139AC9D0-L000127](../../tests/test_dialogue_state.py#L127) | 127 | `"        \"needs_clarification\": True,"` | — |
| [SRC-DA139AC9D0-L000128](../../tests/test_dialogue_state.py#L128) | 128 | `"        \"clarification_question\": \"تقصد بطارية أي هاتف، أم تريد مقارنة بطاريتيهما؟\","` | — |
| [SRC-DA139AC9D0-L000129](../../tests/test_dialogue_state.py#L129) | 129 | `"        \"unresolved_references\": [\"البطارية\"],"` | — |
| [SRC-DA139AC9D0-L000130](../../tests/test_dialogue_state.py#L130) | 130 | `"    }"` | — |
| [SRC-DA139AC9D0-L000131](../../tests/test_dialogue_state.py#L131) | 131 | `""` | — |
| [SRC-DA139AC9D0-L000132](../../tests/test_dialogue_state.py#L132) | 132 | `"    context = validate_dialogue_context(proposed, question, history)"` | — |
| [SRC-DA139AC9D0-L000133](../../tests/test_dialogue_state.py#L133) | 133 | `""` | — |
| [SRC-DA139AC9D0-L000134](../../tests/test_dialogue_state.py#L134) | 134 | `"    assert context[\"needs_clarification\"] is True"` | — |
| [SRC-DA139AC9D0-L000135](../../tests/test_dialogue_state.py#L135) | 135 | `"    assert context[\"resolved_question\"] == question"` | — |
| [SRC-DA139AC9D0-L000136](../../tests/test_dialogue_state.py#L136) | 136 | `"    assert context[\"status\"] == \"needs_clarification\""` | — |
| [SRC-DA139AC9D0-L000137](../../tests/test_dialogue_state.py#L137) | 137 | `"    assert context[\"clarification_question\"]"` | — |
| [SRC-DA139AC9D0-L000138](../../tests/test_dialogue_state.py#L138) | 138 | `""` | — |
| [SRC-DA139AC9D0-L000139](../../tests/test_dialogue_state.py#L139) | 139 | `""` | — |
| [SRC-DA139AC9D0-L000140](../../tests/test_dialogue_state.py#L140) | 140 | `"def test_context_probe_gate_recognizes_natural_followups_not_every_short_question() -> None:"` | — |
| [SRC-DA139AC9D0-L000141](../../tests/test_dialogue_state.py#L141) | 141 | `"    assert might_be_context_dependent(\"And what about its warranty?\")"` | — |
| [SRC-DA139AC9D0-L000142](../../tests/test_dialogue_state.py#L142) | 142 | `"    assert might_be_context_dependent(\"وطب الضمان الدولي بيسري في مصر؟\")"` | — |
| [SRC-DA139AC9D0-L000143](../../tests/test_dialogue_state.py#L143) | 143 | `"    assert might_be_context_dependent(\"والضمان الدولي بيسري في مصر؟\")"` | — |
| [SRC-DA139AC9D0-L000144](../../tests/test_dialogue_state.py#L144) | 144 | `"    assert might_be_context_dependent(\"والضمان؟\")"` | — |
| [SRC-DA139AC9D0-L000145](../../tests/test_dialogue_state.py#L145) | 145 | `"    assert might_be_context_dependent(\"Is it covered?\")"` | — |
| [SRC-DA139AC9D0-L000146](../../tests/test_dialogue_state.py#L146) | 146 | `"    assert might_be_context_dependent(\"هل هذا الهاتف مناسب؟\")"` | — |
| [SRC-DA139AC9D0-L000147](../../tests/test_dialogue_state.py#L147) | 147 | `""` | — |
| [SRC-DA139AC9D0-L000148](../../tests/test_dialogue_state.py#L148) | 148 | `"    assert might_be_context_dependent(\"أقدر أشتريه من هناك؟\")"` | — |
| [SRC-DA139AC9D0-L000149](../../tests/test_dialogue_state.py#L149) | 149 | `"    assert might_be_context_dependent(\"هل أستخدمها مع الجهاز ده؟\")"` | — |
| [SRC-DA139AC9D0-L000150](../../tests/test_dialogue_state.py#L150) | 150 | `"    assert not might_be_context_dependent(\"اشتريت شاشة جديدة اليوم؟\")"` | — |
| [SRC-DA139AC9D0-L000151](../../tests/test_dialogue_state.py#L151) | 151 | `"    assert not might_be_context_dependent(\"اشرح الديناميكا الحرارية ببساطة\")"` | — |
| [SRC-DA139AC9D0-L000152](../../tests/test_dialogue_state.py#L152) | 152 | `"    assert not might_be_context_dependent(\"Explain entropy in simple terms.\")"` | — |
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
| [SRC-6BCB799CEC-L000283](../../tests/test_evidence_provenance.py#L283) | 283 | `"    \"address\","` | — |
| [SRC-6BCB799CEC-L000284](../../tests/test_evidence_provenance.py#L284) | 284 | `"    ["` | — |
| [SRC-6BCB799CEC-L000285](../../tests/test_evidence_provenance.py#L285) | 285 | `"        \"0.0.0.0\",          # unspecified IPv4"` | — |
| [SRC-6BCB799CEC-L000286](../../tests/test_evidence_provenance.py#L286) | 286 | `"        \"127.0.0.1\",        # loopback IPv4"` | — |
| [SRC-6BCB799CEC-L000287](../../tests/test_evidence_provenance.py#L287) | 287 | `"        \"10.0.0.1\",         # private IPv4"` | — |
| [SRC-6BCB799CEC-L000288](../../tests/test_evidence_provenance.py#L288) | 288 | `"        \"172.16.0.1\",       # private IPv4"` | — |
| [SRC-6BCB799CEC-L000289](../../tests/test_evidence_provenance.py#L289) | 289 | `"        \"192.168.1.1\",      # private IPv4"` | — |
| [SRC-6BCB799CEC-L000290](../../tests/test_evidence_provenance.py#L290) | 290 | `"        \"169.254.169.254\",  # link-local / common metadata endpoint"` | — |
| [SRC-6BCB799CEC-L000291](../../tests/test_evidence_provenance.py#L291) | 291 | `"        \"100.64.0.1\",       # shared address space"` | — |
| [SRC-6BCB799CEC-L000292](../../tests/test_evidence_provenance.py#L292) | 292 | `"        \"::\",                # unspecified IPv6"` | — |
| [SRC-6BCB799CEC-L000293](../../tests/test_evidence_provenance.py#L293) | 293 | `"        \"::1\",               # loopback IPv6"` | — |
| [SRC-6BCB799CEC-L000294](../../tests/test_evidence_provenance.py#L294) | 294 | `"        \"fc00::1\",           # unique-local IPv6"` | — |
| [SRC-6BCB799CEC-L000295](../../tests/test_evidence_provenance.py#L295) | 295 | `"        \"fe80::1\",           # link-local IPv6"` | — |
| [SRC-6BCB799CEC-L000296](../../tests/test_evidence_provenance.py#L296) | 296 | `"    ],"` | — |
| [SRC-6BCB799CEC-L000297](../../tests/test_evidence_provenance.py#L297) | 297 | `")"` | — |
| [SRC-6BCB799CEC-L000298](../../tests/test_evidence_provenance.py#L298) | 298 | `"def test_non_global_ipv4_and_ipv6_dns_answers_are_rejected(address, monkeypatch):"` | — |
| [SRC-6BCB799CEC-L000299](../../tests/test_evidence_provenance.py#L299) | 299 | `"    \"\"\"No DNS answer from a non-global range may pass the page-fetch gate.\"\"\""` | — |
| [SRC-6BCB799CEC-L000300](../../tests/test_evidence_provenance.py#L300) | 300 | `"    monkeypatch.setattr("` | — |
| [SRC-6BCB799CEC-L000301](../../tests/test_evidence_provenance.py#L301) | 301 | `"        socket,"` | — |
| [SRC-6BCB799CEC-L000302](../../tests/test_evidence_provenance.py#L302) | 302 | `"        \"getaddrinfo\","` | — |
| [SRC-6BCB799CEC-L000303](../../tests/test_evidence_provenance.py#L303) | 303 | `"        lambda host, port, *args, **kwargs: _addrinfo(address),"` | — |
| [SRC-6BCB799CEC-L000304](../../tests/test_evidence_provenance.py#L304) | 304 | `"    )"` | — |
| [SRC-6BCB799CEC-L000305](../../tests/test_evidence_provenance.py#L305) | 305 | `""` | — |
