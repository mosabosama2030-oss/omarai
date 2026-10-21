# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **026**
- سجلات الأسطر: **800**
- النطاق: SRC-829A979985-L000473 إلى SRC-4397BC2CD2-L000062
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-829A979985 — [tests/test_generation_acceptance_matrix.py](../../tests/test_generation_acceptance_matrix.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-829A979985-L000473](../../tests/test_generation_acceptance_matrix.py#L473) | 473 | `"        \"_generate\","` | — |
| [SRC-829A979985-L000474](../../tests/test_generation_acceptance_matrix.py#L474) | 474 | `"        lambda *args, **kwargs: pytest.fail(\"No synthesis when the research state is unknown\"),"` | — |
| [SRC-829A979985-L000475](../../tests/test_generation_acceptance_matrix.py#L475) | 475 | `"    )"` | — |
| [SRC-829A979985-L000476](../../tests/test_generation_acceptance_matrix.py#L476) | 476 | `""` | — |
| [SRC-829A979985-L000477](../../tests/test_generation_acceptance_matrix.py#L477) | 477 | `"    result = agent.answer(question)"` | — |
| [SRC-829A979985-L000478](../../tests/test_generation_acceptance_matrix.py#L478) | 478 | `""` | — |
| [SRC-829A979985-L000479](../../tests/test_generation_acceptance_matrix.py#L479) | 479 | `"    assert result[\"search_report\"][\"search_outcome\"] == \"unknown_after_research_error\""` | — |
| [SRC-829A979985-L000480](../../tests/test_generation_acceptance_matrix.py#L480) | 480 | `"    assert result[\"search_report\"][\"unique_sources\"] is None"` | — |
| [SRC-829A979985-L000481](../../tests/test_generation_acceptance_matrix.py#L481) | 481 | `"    assert result[\"search_report\"][\"pages_fetched\"] is None"` | — |
| [SRC-829A979985-L000482](../../tests/test_generation_acceptance_matrix.py#L482) | 482 | `"    assert result[\"search_attempted\"] is None"` | — |
| [SRC-829A979985-L000483](../../tests/test_generation_acceptance_matrix.py#L483) | 483 | `"    assert result[\"final_answer_status\"] == \"insufficient_evidence_no_generation\""` | — |
| [SRC-829A979985-L000484](../../tests/test_generation_acceptance_matrix.py#L484) | 484 | `"    assert \"لا أستطيع الجزم\" in result[\"answer\"]"` | — |
| [SRC-829A979985-L000485](../../tests/test_generation_acceptance_matrix.py#L485) | 485 | `"    assert \"لم أجد معلومات موثوقة كافية\" not in result[\"answer\"]"` | — |
| [SRC-829A979985-L000486](../../tests/test_generation_acceptance_matrix.py#L486) | 486 | `""` | — |
| [SRC-829A979985-L000487](../../tests/test_generation_acceptance_matrix.py#L487) | 487 | `""` | — |
| [SRC-829A979985-L000488](../../tests/test_generation_acceptance_matrix.py#L488) | 488 | `"def test_search_extraction_generation_and_task_review_remain_distinct(monkeypatch):"` | — |
| [SRC-829A979985-L000489](../../tests/test_generation_acceptance_matrix.py#L489) | 489 | `"    agent = WebAgent()"` | — |
| [SRC-829A979985-L000490](../../tests/test_generation_acceptance_matrix.py#L490) | 490 | `"    question = \"قارن بين الخيارات من حيث السعر، المساحة، والبيانات الناقصة\""` | — |
| [SRC-829A979985-L000491](../../tests/test_generation_acceptance_matrix.py#L491) | 491 | `"    sources = ["` | — |
| [SRC-829A979985-L000492](../../tests/test_generation_acceptance_matrix.py#L492) | 492 | `"        source("` | — |
| [SRC-829A979985-L000493](../../tests/test_generation_acceptance_matrix.py#L493) | 493 | `"            \"https://one.example/product\","` | — |
| [SRC-829A979985-L000494](../../tests/test_generation_acceptance_matrix.py#L494) | 494 | `"            \"one.example\","` | — |
| [SRC-829A979985-L000495](../../tests/test_generation_acceptance_matrix.py#L495) | 495 | `"            page_fetched=True,"` | — |
| [SRC-829A979985-L000496](../../tests/test_generation_acceptance_matrix.py#L496) | 496 | `"            page_text=\"السعر الإجمالي 100000 جنيه والمساحة 100 متر.\","` | — |
| [SRC-829A979985-L000497](../../tests/test_generation_acceptance_matrix.py#L497) | 497 | `"            provider=\"duckduckgo_html\","` | — |
| [SRC-829A979985-L000498](../../tests/test_generation_acceptance_matrix.py#L498) | 498 | `"        ),"` | — |
| [SRC-829A979985-L000499](../../tests/test_generation_acceptance_matrix.py#L499) | 499 | `"        source("` | — |
| [SRC-829A979985-L000500](../../tests/test_generation_acceptance_matrix.py#L500) | 500 | `"            \"https://two.example/product\","` | — |
| [SRC-829A979985-L000501](../../tests/test_generation_acceptance_matrix.py#L501) | 501 | `"            \"two.example\","` | — |
| [SRC-829A979985-L000502](../../tests/test_generation_acceptance_matrix.py#L502) | 502 | `"            page_fetched=False,"` | — |
| [SRC-829A979985-L000503](../../tests/test_generation_acceptance_matrix.py#L503) | 503 | `"            snippet=\"إعلان يذكر سعرًا دون بيان المساحة.\","` | — |
| [SRC-829A979985-L000504](../../tests/test_generation_acceptance_matrix.py#L504) | 504 | `"            provider=\"bing_rss\","` | — |
| [SRC-829A979985-L000505](../../tests/test_generation_acceptance_matrix.py#L505) | 505 | `"        ),"` | — |
| [SRC-829A979985-L000506](../../tests/test_generation_acceptance_matrix.py#L506) | 506 | `"    ]"` | — |
| [SRC-829A979985-L000507](../../tests/test_generation_acceptance_matrix.py#L507) | 507 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000508](../../tests/test_generation_acceptance_matrix.py#L508) | 508 | `"        agent,"` | — |
| [SRC-829A979985-L000509](../../tests/test_generation_acceptance_matrix.py#L509) | 509 | `"        \"_plan_search\","` | — |
| [SRC-829A979985-L000510](../../tests/test_generation_acceptance_matrix.py#L510) | 510 | `"        lambda question, history: {"` | — |
| [SRC-829A979985-L000511](../../tests/test_generation_acceptance_matrix.py#L511) | 511 | `"            \"queries\": [question],"` | — |
| [SRC-829A979985-L000512](../../tests/test_generation_acceptance_matrix.py#L512) | 512 | `"            \"direct_urls\": [],"` | — |
| [SRC-829A979985-L000513](../../tests/test_generation_acceptance_matrix.py#L513) | 513 | `"            \"social_focus\": False,"` | — |
| [SRC-829A979985-L000514](../../tests/test_generation_acceptance_matrix.py#L514) | 514 | `"            \"freshness\": \"any\","` | — |
| [SRC-829A979985-L000515](../../tests/test_generation_acceptance_matrix.py#L515) | 515 | `"            \"depth\": \"deep\","` | — |
| [SRC-829A979985-L000516](../../tests/test_generation_acceptance_matrix.py#L516) | 516 | `"            \"platforms\": [],"` | — |
| [SRC-829A979985-L000517](../../tests/test_generation_acceptance_matrix.py#L517) | 517 | `"            \"planning_method\": \"test\","` | — |
| [SRC-829A979985-L000518](../../tests/test_generation_acceptance_matrix.py#L518) | 518 | `"        },"` | — |
| [SRC-829A979985-L000519](../../tests/test_generation_acceptance_matrix.py#L519) | 519 | `"    )"` | — |
| [SRC-829A979985-L000520](../../tests/test_generation_acceptance_matrix.py#L520) | 520 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000521](../../tests/test_generation_acceptance_matrix.py#L521) | 521 | `"        agent,"` | — |
| [SRC-829A979985-L000522](../../tests/test_generation_acceptance_matrix.py#L522) | 522 | `"        \"_collect_research\","` | — |
| [SRC-829A979985-L000523](../../tests/test_generation_acceptance_matrix.py#L523) | 523 | `"        lambda plan: ("` | — |
| [SRC-829A979985-L000524](../../tests/test_generation_acceptance_matrix.py#L524) | 524 | `"            sources,"` | — |
| [SRC-829A979985-L000525](../../tests/test_generation_acceptance_matrix.py#L525) | 525 | `"            [],"` | — |
| [SRC-829A979985-L000526](../../tests/test_generation_acceptance_matrix.py#L526) | 526 | `"            {"` | — |
| [SRC-829A979985-L000527](../../tests/test_generation_acceptance_matrix.py#L527) | 527 | `"                \"queries_planned\": 1,"` | — |
| [SRC-829A979985-L000528](../../tests/test_generation_acceptance_matrix.py#L528) | 528 | `"                \"queries_attempted\": 1,"` | — |
| [SRC-829A979985-L000529](../../tests/test_generation_acceptance_matrix.py#L529) | 529 | `"                \"search_attempted\": True,"` | — |
| [SRC-829A979985-L000530](../../tests/test_generation_acceptance_matrix.py#L530) | 530 | `"                \"search_outcome\": \"attempted_with_usable_sources\","` | — |
| [SRC-829A979985-L000531](../../tests/test_generation_acceptance_matrix.py#L531) | 531 | `"                \"unique_sources\": 2,"` | — |
| [SRC-829A979985-L000532](../../tests/test_generation_acceptance_matrix.py#L532) | 532 | `"                \"pages_fetched\": 1,"` | — |
| [SRC-829A979985-L000533](../../tests/test_generation_acceptance_matrix.py#L533) | 533 | `"                \"providers_used\": [\"duckduckgo_html\", \"bing_rss\"],"` | — |
| [SRC-829A979985-L000534](../../tests/test_generation_acceptance_matrix.py#L534) | 534 | `"                \"provider_counts\": {\"duckduckgo_html\": 1, \"bing_rss\": 1},"` | — |
| [SRC-829A979985-L000535](../../tests/test_generation_acceptance_matrix.py#L535) | 535 | `"                \"platform_counts\": {\"web\": 2},"` | — |
| [SRC-829A979985-L000536](../../tests/test_generation_acceptance_matrix.py#L536) | 536 | `"                \"social_direct_results\": 0,"` | — |
| [SRC-829A979985-L000537](../../tests/test_generation_acceptance_matrix.py#L537) | 537 | `"                \"provider_diagnostics\": [],"` | — |
| [SRC-829A979985-L000538](../../tests/test_generation_acceptance_matrix.py#L538) | 538 | `"                \"evidence_signals\": {},"` | — |
| [SRC-829A979985-L000539](../../tests/test_generation_acceptance_matrix.py#L539) | 539 | `"            },"` | — |
| [SRC-829A979985-L000540](../../tests/test_generation_acceptance_matrix.py#L540) | 540 | `"        ),"` | — |
| [SRC-829A979985-L000541](../../tests/test_generation_acceptance_matrix.py#L541) | 541 | `"    )"` | — |
| [SRC-829A979985-L000542](../../tests/test_generation_acceptance_matrix.py#L542) | 542 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, item: True)"` | — |
| [SRC-829A979985-L000543](../../tests/test_generation_acceptance_matrix.py#L543) | 543 | `"    final_draft = \"الخلاصة: يوجد اختلاف في اكتمال البيانات، ولا يمكن حسم المقارنة من المقتطف وحده [المصدر 1].\""` | — |
| [SRC-829A979985-L000544](../../tests/test_generation_acceptance_matrix.py#L544) | 544 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: final_draft)"` | — |
| [SRC-829A979985-L000545](../../tests/test_generation_acceptance_matrix.py#L545) | 545 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-829A979985-L000546](../../tests/test_generation_acceptance_matrix.py#L546) | 546 | `""` | — |
| [SRC-829A979985-L000547](../../tests/test_generation_acceptance_matrix.py#L547) | 547 | `"    result = agent.answer(question)"` | — |
| [SRC-829A979985-L000548](../../tests/test_generation_acceptance_matrix.py#L548) | 548 | `""` | — |
| [SRC-829A979985-L000549](../../tests/test_generation_acceptance_matrix.py#L549) | 549 | `"    assert result[\"search_attempted\"] is True"` | — |
| [SRC-829A979985-L000550](../../tests/test_generation_acceptance_matrix.py#L550) | 550 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-829A979985-L000551](../../tests/test_generation_acceptance_matrix.py#L551) | 551 | `"    assert len(result[\"sources\"]) == 2"` | — |
| [SRC-829A979985-L000552](../../tests/test_generation_acceptance_matrix.py#L552) | 552 | `"    assert result[\"search_report\"][\"search_outcome\"] == \"attempted_with_usable_sources\""` | — |
| [SRC-829A979985-L000553](../../tests/test_generation_acceptance_matrix.py#L553) | 553 | `"    assert result[\"search_report\"][\"pages_fetched\"] == 1"` | — |
| [SRC-829A979985-L000554](../../tests/test_generation_acceptance_matrix.py#L554) | 554 | `"    assert result[\"final_answer_status\"] == \"model_answer_generated\""` | — |
| [SRC-829A979985-L000555](../../tests/test_generation_acceptance_matrix.py#L555) | 555 | `"    assert result[\"search_report\"][\"second_pass_review\"] == \"model_claim_audit_completed\""` | — |
| [SRC-829A979985-L000556](../../tests/test_generation_acceptance_matrix.py#L556) | 556 | `"    assert result[\"answer_coverage\"][\"automatically_graded\"] is False"` | — |
| [SRC-829A979985-L000557](../../tests/test_generation_acceptance_matrix.py#L557) | 557 | `"    assert result[\"answer_coverage\"][\"status\"] == \"model_review_requested_not_machine_verified\""` | — |
| [SRC-829A979985-L000558](../../tests/test_generation_acceptance_matrix.py#L558) | 558 | `"    assert result[\"citation_validation\"][\"method\"] == \"numeric_source_index_range_only\""` | — |
| [SRC-829A979985-L000559](../../tests/test_generation_acceptance_matrix.py#L559) | 559 | `""` | — |
| [SRC-829A979985-L000560](../../tests/test_generation_acceptance_matrix.py#L560) | 560 | `""` | — |
| [SRC-829A979985-L000561](../../tests/test_generation_acceptance_matrix.py#L561) | 561 | `"@pytest.mark.parametrize("` | — |
| [SRC-829A979985-L000562](../../tests/test_generation_acceptance_matrix.py#L562) | 562 | `"    \"malformed_review\","` | — |
| [SRC-829A979985-L000563](../../tests/test_generation_acceptance_matrix.py#L563) | 563 | `"    ["` | — |
| [SRC-829A979985-L000564](../../tests/test_generation_acceptance_matrix.py#L564) | 564 | `"        \"إجابة من دون أي علامات فصل\","` | — |
| [SRC-829A979985-L000565](../../tests/test_generation_acceptance_matrix.py#L565) | 565 | `"        \"<<<OMARAI_FINAL_ANSWER>>>إجابة بلا علامة نهاية\","` | — |
| [SRC-829A979985-L000566](../../tests/test_generation_acceptance_matrix.py#L566) | 566 | `"        \"<<<OMARAI_FINAL_ANSWER>>>إجابة<<<END_OMARAI_FINAL_ANSWER>>> نص زائد خارج الإجابة\","` | — |
| [SRC-829A979985-L000567](../../tests/test_generation_acceptance_matrix.py#L567) | 567 | `"    ],"` | — |
| [SRC-829A979985-L000568](../../tests/test_generation_acceptance_matrix.py#L568) | 568 | `")"` | — |
| [SRC-829A979985-L000569](../../tests/test_generation_acceptance_matrix.py#L569) | 569 | `"def test_reviewer_rejects_missing_or_unbounded_final_answer_delimiters("` | — |
| [SRC-829A979985-L000570](../../tests/test_generation_acceptance_matrix.py#L570) | 570 | `"    monkeypatch, malformed_review"` | — |
| [SRC-829A979985-L000571](../../tests/test_generation_acceptance_matrix.py#L571) | 571 | `"):"` | — |
| [SRC-829A979985-L000572](../../tests/test_generation_acceptance_matrix.py#L572) | 572 | `"    agent = WebAgent()"` | — |
| [SRC-829A979985-L000573](../../tests/test_generation_acceptance_matrix.py#L573) | 573 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000574](../../tests/test_generation_acceptance_matrix.py#L574) | 574 | `"        agent,"` | — |
| [SRC-829A979985-L000575](../../tests/test_generation_acceptance_matrix.py#L575) | 575 | `"        \"_request_completion\","` | — |
| [SRC-829A979985-L000576](../../tests/test_generation_acceptance_matrix.py#L576) | 576 | `"        lambda *args, **kwargs: malformed_review,"` | — |
| [SRC-829A979985-L000577](../../tests/test_generation_acceptance_matrix.py#L577) | 577 | `"    )"` | — |
| [SRC-829A979985-L000578](../../tests/test_generation_acceptance_matrix.py#L578) | 578 | `"    test_source = source("` | — |
| [SRC-829A979985-L000579](../../tests/test_generation_acceptance_matrix.py#L579) | 579 | `"        \"https://one.example/page\","` | — |
| [SRC-829A979985-L000580](../../tests/test_generation_acceptance_matrix.py#L580) | 580 | `"        \"one.example\","` | — |
| [SRC-829A979985-L000581](../../tests/test_generation_acceptance_matrix.py#L581) | 581 | `"        page_fetched=True,"` | — |
| [SRC-829A979985-L000582](../../tests/test_generation_acceptance_matrix.py#L582) | 582 | `"        page_text=\"نص الصفحة\","` | — |
| [SRC-829A979985-L000583](../../tests/test_generation_acceptance_matrix.py#L583) | 583 | `"    )"` | — |
| [SRC-829A979985-L000584](../../tests/test_generation_acceptance_matrix.py#L584) | 584 | `""` | — |
| [SRC-829A979985-L000585](../../tests/test_generation_acceptance_matrix.py#L585) | 585 | `"    with pytest.raises(RuntimeError, match=\"فصل الإجابة النهائية\"):"` | — |
| [SRC-829A979985-L000586](../../tests/test_generation_acceptance_matrix.py#L586) | 586 | `"        agent._review_answer(\"ما مضمون الصفحة؟\", \"مسودة\", [test_source])"` | — |
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
| [SRC-AAA21D04E8-L000055](../../tests/test_generation_capabilities.py#L55) | 55 | `""` | — |
| [SRC-AAA21D04E8-L000056](../../tests/test_generation_capabilities.py#L56) | 56 | `""` | — |
| [SRC-AAA21D04E8-L000057](../../tests/test_generation_capabilities.py#L57) | 57 | `"def test_unknown_finish_reason_is_rejected_and_fallback_is_used(monkeypatch):"` | — |
| [SRC-AAA21D04E8-L000058](../../tests/test_generation_capabilities.py#L58) | 58 | `"    agent = WebAgent()"` | — |
| [SRC-AAA21D04E8-L000059](../../tests/test_generation_capabilities.py#L59) | 59 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-AAA21D04E8-L000060](../../tests/test_generation_capabilities.py#L60) | 60 | `"    agent.fallback_model = \"backup/model\""` | — |
| [SRC-AAA21D04E8-L000061](../../tests/test_generation_capabilities.py#L61) | 61 | `"    calls: list[str] = []"` | — |
| [SRC-AAA21D04E8-L000062](../../tests/test_generation_capabilities.py#L62) | 62 | `""` | — |
| [SRC-AAA21D04E8-L000063](../../tests/test_generation_capabilities.py#L63) | 63 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-AAA21D04E8-L000064](../../tests/test_generation_capabilities.py#L64) | 64 | `"        model = json.loads(request.data.decode(\"utf-8\"))[\"model\"]"` | — |
| [SRC-AAA21D04E8-L000065](../../tests/test_generation_capabilities.py#L65) | 65 | `"        calls.append(model)"` | — |
| [SRC-AAA21D04E8-L000066](../../tests/test_generation_capabilities.py#L66) | 66 | `"        if model == \"primary/model\":"` | — |
| [SRC-AAA21D04E8-L000067](../../tests/test_generation_capabilities.py#L67) | 67 | `"            return FakeResponse(\"response with unrecognized termination\", \"vendor_specific_done\")"` | — |
| [SRC-AAA21D04E8-L000068](../../tests/test_generation_capabilities.py#L68) | 68 | `"        return FakeResponse(\"إجابة مكتملة\", \"stop\")"` | — |
| [SRC-AAA21D04E8-L000069](../../tests/test_generation_capabilities.py#L69) | 69 | `""` | — |
| [SRC-AAA21D04E8-L000070](../../tests/test_generation_capabilities.py#L70) | 70 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-AAA21D04E8-L000071](../../tests/test_generation_capabilities.py#L71) | 71 | `""` | — |
| [SRC-AAA21D04E8-L000072](../../tests/test_generation_capabilities.py#L72) | 72 | `"    answer = agent._request_completion("` | — |
| [SRC-AAA21D04E8-L000073](../../tests/test_generation_capabilities.py#L73) | 73 | `"        [{\"role\": \"user\", \"content\": \"اختبار\"}],"` | — |
| [SRC-AAA21D04E8-L000074](../../tests/test_generation_capabilities.py#L74) | 74 | `"        model=\"primary/model\","` | — |
| [SRC-AAA21D04E8-L000075](../../tests/test_generation_capabilities.py#L75) | 75 | `"    )"` | — |
| [SRC-AAA21D04E8-L000076](../../tests/test_generation_capabilities.py#L76) | 76 | `""` | — |
| [SRC-AAA21D04E8-L000077](../../tests/test_generation_capabilities.py#L77) | 77 | `"    assert answer == \"إجابة مكتملة\""` | — |
| [SRC-AAA21D04E8-L000078](../../tests/test_generation_capabilities.py#L78) | 78 | `"    assert calls == [\"primary/model\", \"backup/model\"]"` | — |
| [SRC-AAA21D04E8-L000079](../../tests/test_generation_capabilities.py#L79) | 79 | `"    assert agent.generation_diagnostics[0][\"status\"] == \"finish_reason_not_accepted\""` | — |
| [SRC-AAA21D04E8-L000080](../../tests/test_generation_capabilities.py#L80) | 80 | `"    assert agent.generation_diagnostics[0][\"finish_reason\"] == \"vendor_specific_done\""` | — |
| [SRC-AAA21D04E8-L000081](../../tests/test_generation_capabilities.py#L81) | 81 | `""` | — |
| [SRC-AAA21D04E8-L000082](../../tests/test_generation_capabilities.py#L82) | 82 | `""` | — |
| [SRC-AAA21D04E8-L000083](../../tests/test_generation_capabilities.py#L83) | 83 | `"def test_missing_finish_reason_from_all_models_fails_closed(monkeypatch):"` | — |
| [SRC-AAA21D04E8-L000084](../../tests/test_generation_capabilities.py#L84) | 84 | `"    agent = WebAgent()"` | — |
| [SRC-AAA21D04E8-L000085](../../tests/test_generation_capabilities.py#L85) | 85 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-AAA21D04E8-L000086](../../tests/test_generation_capabilities.py#L86) | 86 | `"    agent.fallback_model = \"\""` | — |
| [SRC-AAA21D04E8-L000087](../../tests/test_generation_capabilities.py#L87) | 87 | `"    calls: list[str] = []"` | — |
| [SRC-AAA21D04E8-L000088](../../tests/test_generation_capabilities.py#L88) | 88 | `""` | — |
| [SRC-AAA21D04E8-L000089](../../tests/test_generation_capabilities.py#L89) | 89 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-AAA21D04E8-L000090](../../tests/test_generation_capabilities.py#L90) | 90 | `"        calls.append(json.loads(request.data.decode(\"utf-8\"))[\"model\"])"` | — |
| [SRC-AAA21D04E8-L000091](../../tests/test_generation_capabilities.py#L91) | 91 | `"        return FakeResponse(\"may be incomplete\", include_reason=False)"` | — |
| [SRC-AAA21D04E8-L000092](../../tests/test_generation_capabilities.py#L92) | 92 | `""` | — |
| [SRC-AAA21D04E8-L000093](../../tests/test_generation_capabilities.py#L93) | 93 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-AAA21D04E8-L000094](../../tests/test_generation_capabilities.py#L94) | 94 | `""` | — |
| [SRC-AAA21D04E8-L000095](../../tests/test_generation_capabilities.py#L95) | 95 | `"    with pytest.raises(RuntimeError, match=\"سبب انتهاء واضحًا\"):"` | — |
| [SRC-AAA21D04E8-L000096](../../tests/test_generation_capabilities.py#L96) | 96 | `"        agent._request_completion("` | — |
| [SRC-AAA21D04E8-L000097](../../tests/test_generation_capabilities.py#L97) | 97 | `"            [{\"role\": \"user\", \"content\": \"اختبار\"}],"` | — |
| [SRC-AAA21D04E8-L000098](../../tests/test_generation_capabilities.py#L98) | 98 | `"            model=\"primary/model\","` | — |
| [SRC-AAA21D04E8-L000099](../../tests/test_generation_capabilities.py#L99) | 99 | `"        )"` | — |
| [SRC-AAA21D04E8-L000100](../../tests/test_generation_capabilities.py#L100) | 100 | `""` | — |
| [SRC-AAA21D04E8-L000101](../../tests/test_generation_capabilities.py#L101) | 101 | `"    assert calls == [\"primary/model\"]"` | — |
| [SRC-AAA21D04E8-L000102](../../tests/test_generation_capabilities.py#L102) | 102 | `"    assert agent.model_usage == []"` | — |
| [SRC-AAA21D04E8-L000103](../../tests/test_generation_capabilities.py#L103) | 103 | `"    assert agent.generation_diagnostics == [{"` | — |
| [SRC-AAA21D04E8-L000104](../../tests/test_generation_capabilities.py#L104) | 104 | `"        \"requested_model\": \"primary/model\","` | — |
| [SRC-AAA21D04E8-L000105](../../tests/test_generation_capabilities.py#L105) | 105 | `"        \"attempted_model\": \"primary/model\","` | — |
| [SRC-AAA21D04E8-L000106](../../tests/test_generation_capabilities.py#L106) | 106 | `"        \"status\": \"finish_reason_missing\","` | — |
| [SRC-AAA21D04E8-L000107](../../tests/test_generation_capabilities.py#L107) | 107 | `"    }]"` | — |
| [SRC-AAA21D04E8-L000108](../../tests/test_generation_capabilities.py#L108) | 108 | `""` | — |
| [SRC-AAA21D04E8-L000109](../../tests/test_generation_capabilities.py#L109) | 109 | `""` | — |
| [SRC-AAA21D04E8-L000110](../../tests/test_generation_capabilities.py#L110) | 110 | `"def test_capability_question_distinguishes_configuration_from_live_health(monkeypatch):"` | — |
| [SRC-AAA21D04E8-L000111](../../tests/test_generation_capabilities.py#L111) | 111 | `"    agent = WebAgent()"` | — |
| [SRC-AAA21D04E8-L000112](../../tests/test_generation_capabilities.py#L112) | 112 | `""` | — |
| [SRC-AAA21D04E8-L000113](../../tests/test_generation_capabilities.py#L113) | 113 | `"    monkeypatch.setattr("` | — |
| [SRC-AAA21D04E8-L000114](../../tests/test_generation_capabilities.py#L114) | 114 | `"        agent,"` | — |
| [SRC-AAA21D04E8-L000115](../../tests/test_generation_capabilities.py#L115) | 115 | `"        \"_collect_research\","` | — |
| [SRC-AAA21D04E8-L000116](../../tests/test_generation_capabilities.py#L116) | 116 | `"        lambda plan: pytest.fail(\"Capability questions must not run live search\"),"` | — |
| [SRC-AAA21D04E8-L000117](../../tests/test_generation_capabilities.py#L117) | 117 | `"    )"` | — |
| [SRC-AAA21D04E8-L000118](../../tests/test_generation_capabilities.py#L118) | 118 | `""` | — |
| [SRC-AAA21D04E8-L000119](../../tests/test_generation_capabilities.py#L119) | 119 | `"    result = agent.answer(\"هل تستطيع البحث على الانترنت؟\")"` | — |
| [SRC-AAA21D04E8-L000120](../../tests/test_generation_capabilities.py#L120) | 120 | `""` | — |
| [SRC-AAA21D04E8-L000121](../../tests/test_generation_capabilities.py#L121) | 121 | `"    assert result[\"kind\"] == \"capability_answer\""` | — |
| [SRC-AAA21D04E8-L000122](../../tests/test_generation_capabilities.py#L122) | 122 | `"    assert result[\"final_answer_status\"] == \"local_response_no_generation\""` | — |
| [SRC-AAA21D04E8-L000123](../../tests/test_generation_capabilities.py#L123) | 123 | `"    assert result[\"search_attempted\"] is False"` | — |
| [SRC-AAA21D04E8-L000124](../../tests/test_generation_capabilities.py#L124) | 124 | `"    assert result[\"used_web_search\"] is False"` | — |
| [SRC-AAA21D04E8-L000125](../../tests/test_generation_capabilities.py#L125) | 125 | `"    capability = result[\"capability_status\"][\"web_search\"]"` | — |
| [SRC-AAA21D04E8-L000126](../../tests/test_generation_capabilities.py#L126) | 126 | `"    assert capability[\"implemented\"] is True"` | — |
| [SRC-AAA21D04E8-L000127](../../tests/test_generation_capabilities.py#L127) | 127 | `"    assert capability[\"runtime_status\"] == \"not_tested_in_this_response\""` | — |
| [SRC-AAA21D04E8-L000128](../../tests/test_generation_capabilities.py#L128) | 128 | `"    assert capability[\"local_dependencies_ready\"] is True"` | — |
| [SRC-AAA21D04E8-L000129](../../tests/test_generation_capabilities.py#L129) | 129 | `"    assert \"لم أنفّذ اختبار اتصال حي\" in result[\"answer\"]"` | — |
| [SRC-AAA21D04E8-L000130](../../tests/test_generation_capabilities.py#L130) | 130 | `"    assert \"DuckDuckGo HTML\" in result[\"answer\"]"` | — |
| [SRC-AAA21D04E8-L000131](../../tests/test_generation_capabilities.py#L131) | 131 | `""` | — |
| [SRC-AAA21D04E8-L000132](../../tests/test_generation_capabilities.py#L132) | 132 | `""` | — |
| [SRC-AAA21D04E8-L000133](../../tests/test_generation_capabilities.py#L133) | 133 | `"@pytest.mark.parametrize(\"mode\", [\"auto\", \"deep\", \"latest\", \"social\"])"` | — |
| [SRC-AAA21D04E8-L000134](../../tests/test_generation_capabilities.py#L134) | 134 | `"def test_current_request_search_status_is_not_confused_with_capability(monkeypatch, mode):"` | — |
| [SRC-AAA21D04E8-L000135](../../tests/test_generation_capabilities.py#L135) | 135 | `"    agent = WebAgent()"` | — |
| [SRC-AAA21D04E8-L000136](../../tests/test_generation_capabilities.py#L136) | 136 | `"    monkeypatch.setattr("` | — |
| [SRC-AAA21D04E8-L000137](../../tests/test_generation_capabilities.py#L137) | 137 | `"        agent,"` | — |
| [SRC-AAA21D04E8-L000138](../../tests/test_generation_capabilities.py#L138) | 138 | `"        \"_collect_research\","` | — |
| [SRC-AAA21D04E8-L000139](../../tests/test_generation_capabilities.py#L139) | 139 | `"        lambda plan: pytest.fail(\"This asks about the current response, not a web lookup\"),"` | — |
| [SRC-AAA21D04E8-L000140](../../tests/test_generation_capabilities.py#L140) | 140 | `"    )"` | — |
| [SRC-AAA21D04E8-L000141](../../tests/test_generation_capabilities.py#L141) | 141 | `""` | — |
| [SRC-AAA21D04E8-L000142](../../tests/test_generation_capabilities.py#L142) | 142 | `"    result = agent.answer(\"هل بحثت في الانترنت للاجابة الحالية؟\", mode=mode)"` | — |
| [SRC-AAA21D04E8-L000143](../../tests/test_generation_capabilities.py#L143) | 143 | `""` | — |
| [SRC-AAA21D04E8-L000144](../../tests/test_generation_capabilities.py#L144) | 144 | `"    assert result[\"kind\"] == \"capability_answer\""` | — |
| [SRC-AAA21D04E8-L000145](../../tests/test_generation_capabilities.py#L145) | 145 | `"    assert result[\"request_execution_status\"] == {"` | — |
| [SRC-AAA21D04E8-L000146](../../tests/test_generation_capabilities.py#L146) | 146 | `"        \"search_attempted\": False,"` | — |
| [SRC-AAA21D04E8-L000147](../../tests/test_generation_capabilities.py#L147) | 147 | `"        \"search_outcome\": \"not_attempted\","` | — |
| [SRC-AAA21D04E8-L000148](../../tests/test_generation_capabilities.py#L148) | 148 | `"        \"semantics\": \"status_of_this_request_only\","` | — |
| [SRC-AAA21D04E8-L000149](../../tests/test_generation_capabilities.py#L149) | 149 | `"    }"` | — |
| [SRC-AAA21D04E8-L000150](../../tests/test_generation_capabilities.py#L150) | 150 | `"    assert \"لم أنفّذ بحثًا حيًا للإجابة عن هذا السؤال تحديدًا\" in result[\"answer\"]"` | — |
| [SRC-AAA21D04E8-L000151](../../tests/test_generation_capabilities.py#L151) | 151 | `"    assert result[\"capability_status\"][\"web_search\"][\"runtime_status\"] == ("` | — |
| [SRC-AAA21D04E8-L000152](../../tests/test_generation_capabilities.py#L152) | 152 | `"        \"not_tested_in_this_response\""` | — |
| [SRC-AAA21D04E8-L000153](../../tests/test_generation_capabilities.py#L153) | 153 | `"    )"` | — |
| [SRC-AAA21D04E8-L000154](../../tests/test_generation_capabilities.py#L154) | 154 | `"    assert result[\"search_attempted\"] is False"` | — |
| [SRC-AAA21D04E8-L000155](../../tests/test_generation_capabilities.py#L155) | 155 | `""` | — |
| [SRC-AAA21D04E8-L000156](../../tests/test_generation_capabilities.py#L156) | 156 | `""` | — |
| [SRC-AAA21D04E8-L000157](../../tests/test_generation_capabilities.py#L157) | 157 | `"def test_generation_failure_returns_partial_sources_and_diagnostics(monkeypatch):"` | — |
| [SRC-AAA21D04E8-L000158](../../tests/test_generation_capabilities.py#L158) | 158 | `"    agent = WebAgent()"` | — |
| [SRC-AAA21D04E8-L000159](../../tests/test_generation_capabilities.py#L159) | 159 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-AAA21D04E8-L000160](../../tests/test_generation_capabilities.py#L160) | 160 | `"    question = \"ابحث عن أحدث تقرير عن الذكاء الاصطناعي\""` | — |
| [SRC-AAA21D04E8-L000161](../../tests/test_generation_capabilities.py#L161) | 161 | `""` | — |
| [SRC-AAA21D04E8-L000162](../../tests/test_generation_capabilities.py#L162) | 162 | `"    sources = ["` | — |
| [SRC-AAA21D04E8-L000163](../../tests/test_generation_capabilities.py#L163) | 163 | `"        {"` | — |
| [SRC-AAA21D04E8-L000164](../../tests/test_generation_capabilities.py#L164) | 164 | `"            \"title\": \"تقرير ذكاء اصطناعي\","` | — |
| [SRC-AAA21D04E8-L000165](../../tests/test_generation_capabilities.py#L165) | 165 | `"            \"url\": \"https://example.com/report\","` | — |
| [SRC-AAA21D04E8-L000166](../../tests/test_generation_capabilities.py#L166) | 166 | `"            \"snippet\": \"مقتطف تجريبي من المصدر الأول\","` | — |
| [SRC-AAA21D04E8-L000167](../../tests/test_generation_capabilities.py#L167) | 167 | `"            \"page_fetched\": False,"` | — |
| [SRC-AAA21D04E8-L000168](../../tests/test_generation_capabilities.py#L168) | 168 | `"            \"providers\": [\"duckduckgo_html\"],"` | — |
| [SRC-AAA21D04E8-L000169](../../tests/test_generation_capabilities.py#L169) | 169 | `"            \"queries\": [question],"` | — |
| [SRC-AAA21D04E8-L000170](../../tests/test_generation_capabilities.py#L170) | 170 | `"            \"domain\": \"example.com\","` | — |
| [SRC-AAA21D04E8-L000171](../../tests/test_generation_capabilities.py#L171) | 171 | `"            \"source_class\": \"general\","` | — |
| [SRC-AAA21D04E8-L000172](../../tests/test_generation_capabilities.py#L172) | 172 | `"            \"platform\": \"web\","` | — |
| [SRC-AAA21D04E8-L000173](../../tests/test_generation_capabilities.py#L173) | 173 | `"            \"published_at\": \"\","` | — |
| [SRC-AAA21D04E8-L000174](../../tests/test_generation_capabilities.py#L174) | 174 | `"            \"rank_score\": 0.9,"` | — |
| [SRC-AAA21D04E8-L000175](../../tests/test_generation_capabilities.py#L175) | 175 | `"        },"` | — |
| [SRC-AAA21D04E8-L000176](../../tests/test_generation_capabilities.py#L176) | 176 | `"        {"` | — |
| [SRC-AAA21D04E8-L000177](../../tests/test_generation_capabilities.py#L177) | 177 | `"            \"title\": \"مصدر ثان\","` | — |
| [SRC-AAA21D04E8-L000178](../../tests/test_generation_capabilities.py#L178) | 178 | `"            \"url\": \"https://example.net/report\","` | — |
| [SRC-AAA21D04E8-L000179](../../tests/test_generation_capabilities.py#L179) | 179 | `"            \"snippet\": \"مقتطف تجريبي من المصدر الثاني\","` | — |
| [SRC-AAA21D04E8-L000180](../../tests/test_generation_capabilities.py#L180) | 180 | `"            \"page_fetched\": False,"` | — |
| [SRC-AAA21D04E8-L000181](../../tests/test_generation_capabilities.py#L181) | 181 | `"            \"providers\": [\"bing_rss\"],"` | — |
| [SRC-AAA21D04E8-L000182](../../tests/test_generation_capabilities.py#L182) | 182 | `"            \"queries\": [question],"` | — |
| [SRC-AAA21D04E8-L000183](../../tests/test_generation_capabilities.py#L183) | 183 | `"            \"domain\": \"example.net\","` | — |
| [SRC-AAA21D04E8-L000184](../../tests/test_generation_capabilities.py#L184) | 184 | `"            \"source_class\": \"general\","` | — |
| [SRC-AAA21D04E8-L000185](../../tests/test_generation_capabilities.py#L185) | 185 | `"            \"platform\": \"web\","` | — |
| [SRC-AAA21D04E8-L000186](../../tests/test_generation_capabilities.py#L186) | 186 | `"            \"published_at\": \"\","` | — |
| [SRC-AAA21D04E8-L000187](../../tests/test_generation_capabilities.py#L187) | 187 | `"            \"rank_score\": 0.8,"` | — |
| [SRC-AAA21D04E8-L000188](../../tests/test_generation_capabilities.py#L188) | 188 | `"        },"` | — |
| [SRC-AAA21D04E8-L000189](../../tests/test_generation_capabilities.py#L189) | 189 | `"    ]"` | — |
| [SRC-AAA21D04E8-L000190](../../tests/test_generation_capabilities.py#L190) | 190 | `""` | — |
| [SRC-AAA21D04E8-L000191](../../tests/test_generation_capabilities.py#L191) | 191 | `"    monkeypatch.setattr("` | — |
| [SRC-AAA21D04E8-L000192](../../tests/test_generation_capabilities.py#L192) | 192 | `"        agent,"` | — |
| [SRC-AAA21D04E8-L000193](../../tests/test_generation_capabilities.py#L193) | 193 | `"        \"_plan_search\","` | — |
| [SRC-AAA21D04E8-L000194](../../tests/test_generation_capabilities.py#L194) | 194 | `"        lambda question, history: {"` | — |
| [SRC-AAA21D04E8-L000195](../../tests/test_generation_capabilities.py#L195) | 195 | `"            \"queries\": [question],"` | — |
| [SRC-AAA21D04E8-L000196](../../tests/test_generation_capabilities.py#L196) | 196 | `"            \"depth\": \"standard\","` | — |
| [SRC-AAA21D04E8-L000197](../../tests/test_generation_capabilities.py#L197) | 197 | `"            \"freshness\": \"any\","` | — |
| [SRC-AAA21D04E8-L000198](../../tests/test_generation_capabilities.py#L198) | 198 | `"            \"social_focus\": False,"` | — |
| [SRC-AAA21D04E8-L000199](../../tests/test_generation_capabilities.py#L199) | 199 | `"            \"platforms\": [],"` | — |
| [SRC-AAA21D04E8-L000200](../../tests/test_generation_capabilities.py#L200) | 200 | `"            \"planning_method\": \"test_fixture\","` | — |
| [SRC-AAA21D04E8-L000201](../../tests/test_generation_capabilities.py#L201) | 201 | `"            \"direct_urls\": [],"` | — |
| [SRC-AAA21D04E8-L000202](../../tests/test_generation_capabilities.py#L202) | 202 | `"        },"` | — |
| [SRC-AAA21D04E8-L000203](../../tests/test_generation_capabilities.py#L203) | 203 | `"    )"` | — |
| [SRC-AAA21D04E8-L000204](../../tests/test_generation_capabilities.py#L204) | 204 | `"    monkeypatch.setattr("` | — |
| [SRC-AAA21D04E8-L000205](../../tests/test_generation_capabilities.py#L205) | 205 | `"        agent,"` | — |
| [SRC-AAA21D04E8-L000206](../../tests/test_generation_capabilities.py#L206) | 206 | `"        \"_collect_research\","` | — |
| [SRC-AAA21D04E8-L000207](../../tests/test_generation_capabilities.py#L207) | 207 | `"        lambda plan: ("` | — |
| [SRC-AAA21D04E8-L000208](../../tests/test_generation_capabilities.py#L208) | 208 | `"            sources,"` | — |
| [SRC-AAA21D04E8-L000209](../../tests/test_generation_capabilities.py#L209) | 209 | `"            [],"` | — |
| [SRC-AAA21D04E8-L000210](../../tests/test_generation_capabilities.py#L210) | 210 | `"            {"` | — |
| [SRC-AAA21D04E8-L000211](../../tests/test_generation_capabilities.py#L211) | 211 | `"                \"queries_planned\": 1,"` | — |
| [SRC-AAA21D04E8-L000212](../../tests/test_generation_capabilities.py#L212) | 212 | `"                \"queries_attempted\": 1,"` | — |
| [SRC-AAA21D04E8-L000213](../../tests/test_generation_capabilities.py#L213) | 213 | `"                \"queries_attempted_known\": True,"` | — |
| [SRC-AAA21D04E8-L000214](../../tests/test_generation_capabilities.py#L214) | 214 | `"                \"search_attempted\": True,"` | — |
| [SRC-AAA21D04E8-L000215](../../tests/test_generation_capabilities.py#L215) | 215 | `"                \"search_outcome\": \"attempted_with_usable_sources\","` | — |
| [SRC-AAA21D04E8-L000216](../../tests/test_generation_capabilities.py#L216) | 216 | `"                \"unique_sources\": 2,"` | — |
| [SRC-AAA21D04E8-L000217](../../tests/test_generation_capabilities.py#L217) | 217 | `"                \"pages_fetched\": 0,"` | — |
| [SRC-AAA21D04E8-L000218](../../tests/test_generation_capabilities.py#L218) | 218 | `"                \"providers_used\": [\"duckduckgo_html\", \"bing_rss\"],"` | — |
| [SRC-AAA21D04E8-L000219](../../tests/test_generation_capabilities.py#L219) | 219 | `"                \"provider_counts\": {\"duckduckgo_html\": 1, \"bing_rss\": 1},"` | — |
| [SRC-AAA21D04E8-L000220](../../tests/test_generation_capabilities.py#L220) | 220 | `"                \"platform_counts\": {\"web\": 2},"` | — |
| [SRC-AAA21D04E8-L000221](../../tests/test_generation_capabilities.py#L221) | 221 | `"                \"evidence_signals\": {},"` | — |
| [SRC-AAA21D04E8-L000222](../../tests/test_generation_capabilities.py#L222) | 222 | `"            },"` | — |
| [SRC-AAA21D04E8-L000223](../../tests/test_generation_capabilities.py#L223) | 223 | `"        ),"` | — |
| [SRC-AAA21D04E8-L000224](../../tests/test_generation_capabilities.py#L224) | 224 | `"    )"` | — |
| [SRC-AAA21D04E8-L000225](../../tests/test_generation_capabilities.py#L225) | 225 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-AAA21D04E8-L000226](../../tests/test_generation_capabilities.py#L226) | 226 | `""` | — |
| [SRC-AAA21D04E8-L000227](../../tests/test_generation_capabilities.py#L227) | 227 | `"    def failed_generate(*args, **kwargs):"` | — |
| [SRC-AAA21D04E8-L000228](../../tests/test_generation_capabilities.py#L228) | 228 | `"        agent._record_generation_diagnostic("` | — |
| [SRC-AAA21D04E8-L000229](../../tests/test_generation_capabilities.py#L229) | 229 | `"            requested_model=\"primary/model\","` | — |
| [SRC-AAA21D04E8-L000230](../../tests/test_generation_capabilities.py#L230) | 230 | `"            attempted_model=\"fallback/model\","` | — |
| [SRC-AAA21D04E8-L000231](../../tests/test_generation_capabilities.py#L231) | 231 | `"            status=\"truncated\","` | — |
| [SRC-AAA21D04E8-L000232](../../tests/test_generation_capabilities.py#L232) | 232 | `"            finish_reason=\"length\","` | — |
| [SRC-AAA21D04E8-L000233](../../tests/test_generation_capabilities.py#L233) | 233 | `"        )"` | — |
| [SRC-AAA21D04E8-L000234](../../tests/test_generation_capabilities.py#L234) | 234 | `"        raise RuntimeError(\"اختبار: فشل التوليد بعد انتهاء حد الرموز\")"` | — |
| [SRC-AAA21D04E8-L000235](../../tests/test_generation_capabilities.py#L235) | 235 | `""` | — |
| [SRC-AAA21D04E8-L000236](../../tests/test_generation_capabilities.py#L236) | 236 | `"    monkeypatch.setattr(agent, \"_generate\", failed_generate)"` | — |
| [SRC-AAA21D04E8-L000237](../../tests/test_generation_capabilities.py#L237) | 237 | `""` | — |
| [SRC-AAA21D04E8-L000238](../../tests/test_generation_capabilities.py#L238) | 238 | `"    result = agent.answer(question)"` | — |
| [SRC-AAA21D04E8-L000239](../../tests/test_generation_capabilities.py#L239) | 239 | `""` | — |
| [SRC-AAA21D04E8-L000240](../../tests/test_generation_capabilities.py#L240) | 240 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-AAA21D04E8-L000241](../../tests/test_generation_capabilities.py#L241) | 241 | `"    assert result[\"used_language_model\"] is False"` | — |
| [SRC-AAA21D04E8-L000242](../../tests/test_generation_capabilities.py#L242) | 242 | `"    assert result[\"final_answer_status\"] == \"generation_failed_with_source_fallback\""` | — |
| [SRC-AAA21D04E8-L000243](../../tests/test_generation_capabilities.py#L243) | 243 | `"    assert len(result[\"sources\"]) == 2"` | — |
| [SRC-AAA21D04E8-L000244](../../tests/test_generation_capabilities.py#L244) | 244 | `"    assert \"تعذر توليد إجابة تحليلية\" in result[\"answer\"]"` | — |
| [SRC-AAA21D04E8-L000245](../../tests/test_generation_capabilities.py#L245) | 245 | `"    assert \"مقتطف تجريبي من المصدر الأول\" in result[\"answer\"]"` | — |
| [SRC-AAA21D04E8-L000246](../../tests/test_generation_capabilities.py#L246) | 246 | `"    assert result[\"generation_diagnostics\"] == ["` | — |
| [SRC-AAA21D04E8-L000247](../../tests/test_generation_capabilities.py#L247) | 247 | `"        {"` | — |
| [SRC-AAA21D04E8-L000248](../../tests/test_generation_capabilities.py#L248) | 248 | `"            \"requested_model\": \"primary/model\","` | — |
| [SRC-AAA21D04E8-L000249](../../tests/test_generation_capabilities.py#L249) | 249 | `"            \"attempted_model\": \"fallback/model\","` | — |
| [SRC-AAA21D04E8-L000250](../../tests/test_generation_capabilities.py#L250) | 250 | `"            \"status\": \"truncated\","` | — |
| [SRC-AAA21D04E8-L000251](../../tests/test_generation_capabilities.py#L251) | 251 | `"            \"finish_reason\": \"length\","` | — |
| [SRC-AAA21D04E8-L000252](../../tests/test_generation_capabilities.py#L252) | 252 | `"        }"` | — |
| [SRC-AAA21D04E8-L000253](../../tests/test_generation_capabilities.py#L253) | 253 | `"    ]"` | — |
| [SRC-AAA21D04E8-L000254](../../tests/test_generation_capabilities.py#L254) | 254 | `"    assert result[\"search_report\"][\"research_quality\"] == \"partial\""` | — |
| [SRC-AAA21D04E8-L000255](../../tests/test_generation_capabilities.py#L255) | 255 | `"    assert result[\"citation_validation\"][\"status\"] != \"validated_as_fact\""` | — |
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
| [SRC-1A176AD4F0-L000005](../../tests/test_hosted_smoke.py#L5) | 5 | `"from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer"` | — |
| [SRC-1A176AD4F0-L000006](../../tests/test_hosted_smoke.py#L6) | 6 | `"from urllib.parse import urlsplit"` | — |
| [SRC-1A176AD4F0-L000007](../../tests/test_hosted_smoke.py#L7) | 7 | `""` | — |
| [SRC-1A176AD4F0-L000008](../../tests/test_hosted_smoke.py#L8) | 8 | `"import pytest"` | — |
| [SRC-1A176AD4F0-L000009](../../tests/test_hosted_smoke.py#L9) | 9 | `""` | — |
| [SRC-1A176AD4F0-L000010](../../tests/test_hosted_smoke.py#L10) | 10 | `"from scripts import hosted_smoke_test"` | — |
| [SRC-1A176AD4F0-L000011](../../tests/test_hosted_smoke.py#L11) | 11 | `"from scripts.hosted_smoke_test import SmokeError, normalize_origin, run_smoke"` | — |
| [SRC-1A176AD4F0-L000012](../../tests/test_hosted_smoke.py#L12) | 12 | `""` | — |
| [SRC-1A176AD4F0-L000013](../../tests/test_hosted_smoke.py#L13) | 13 | `"TOKEN = \"local-test-token-long-enough-for-the-32-character-rule\""` | — |
| [SRC-1A176AD4F0-L000014](../../tests/test_hosted_smoke.py#L14) | 14 | `""` | — |
| [SRC-1A176AD4F0-L000015](../../tests/test_hosted_smoke.py#L15) | 15 | `""` | — |
| [SRC-1A176AD4F0-L000016](../../tests/test_hosted_smoke.py#L16) | 16 | `"class Handler(BaseHTTPRequestHandler):"` | — |
| [SRC-1A176AD4F0-L000017](../../tests/test_hosted_smoke.py#L17) | 17 | `"    def log_message(self, format: str, *args: object) -> None:"` | — |
| [SRC-1A176AD4F0-L000018](../../tests/test_hosted_smoke.py#L18) | 18 | `"        return"` | — |
| [SRC-1A176AD4F0-L000019](../../tests/test_hosted_smoke.py#L19) | 19 | `""` | — |
| [SRC-1A176AD4F0-L000020](../../tests/test_hosted_smoke.py#L20) | 20 | `"    def respond(self, status: int, payload: dict[str, object]) -> None:"` | — |
| [SRC-1A176AD4F0-L000021](../../tests/test_hosted_smoke.py#L21) | 21 | `"        body = json.dumps(payload).encode()"` | — |
| [SRC-1A176AD4F0-L000022](../../tests/test_hosted_smoke.py#L22) | 22 | `"        self.send_response(status)"` | — |
| [SRC-1A176AD4F0-L000023](../../tests/test_hosted_smoke.py#L23) | 23 | `"        self.send_header(\"Content-Type\", \"application/json\")"` | — |
| [SRC-1A176AD4F0-L000024](../../tests/test_hosted_smoke.py#L24) | 24 | `"        self.send_header(\"Content-Length\", str(len(body)))"` | — |
| [SRC-1A176AD4F0-L000025](../../tests/test_hosted_smoke.py#L25) | 25 | `"        self.end_headers()"` | — |
| [SRC-1A176AD4F0-L000026](../../tests/test_hosted_smoke.py#L26) | 26 | `"        self.wfile.write(body)"` | — |
| [SRC-1A176AD4F0-L000027](../../tests/test_hosted_smoke.py#L27) | 27 | `""` | — |
| [SRC-1A176AD4F0-L000028](../../tests/test_hosted_smoke.py#L28) | 28 | `"    def do_GET(self) -> None:"` | — |
| [SRC-1A176AD4F0-L000029](../../tests/test_hosted_smoke.py#L29) | 29 | `"        if self.path == \"/api/health\":"` | — |
| [SRC-1A176AD4F0-L000030](../../tests/test_hosted_smoke.py#L30) | 30 | `"            self.respond(200, {\"ok\": True, \"app\": \"Omarai\", \"agent\": {}})"` | — |
| [SRC-1A176AD4F0-L000031](../../tests/test_hosted_smoke.py#L31) | 31 | `"        else:"` | — |
| [SRC-1A176AD4F0-L000032](../../tests/test_hosted_smoke.py#L32) | 32 | `"            self.respond(404, {\"error\": \"not found\"})"` | — |
| [SRC-1A176AD4F0-L000033](../../tests/test_hosted_smoke.py#L33) | 33 | `""` | — |
| [SRC-1A176AD4F0-L000034](../../tests/test_hosted_smoke.py#L34) | 34 | `"    def do_POST(self) -> None:"` | — |
| [SRC-1A176AD4F0-L000035](../../tests/test_hosted_smoke.py#L35) | 35 | `"        if self.headers.get(\"Authorization\") != f\"Bearer {TOKEN}\":"` | — |
| [SRC-1A176AD4F0-L000036](../../tests/test_hosted_smoke.py#L36) | 36 | `"            self.respond(401, {\"error\": \"unauthorized\"})"` | — |
| [SRC-1A176AD4F0-L000037](../../tests/test_hosted_smoke.py#L37) | 37 | `"            return"` | — |
| [SRC-1A176AD4F0-L000038](../../tests/test_hosted_smoke.py#L38) | 38 | `"        length = int(self.headers.get(\"Content-Length\", \"0\"))"` | — |
| [SRC-1A176AD4F0-L000039](../../tests/test_hosted_smoke.py#L39) | 39 | `"        self.rfile.read(length)"` | — |
| [SRC-1A176AD4F0-L000040](../../tests/test_hosted_smoke.py#L40) | 40 | `"        if self.path == \"/api/diagnostics\":"` | — |
| [SRC-1A176AD4F0-L000041](../../tests/test_hosted_smoke.py#L41) | 41 | `"            self.respond(200, {"` | — |
| [SRC-1A176AD4F0-L000042](../../tests/test_hosted_smoke.py#L42) | 42 | `"                \"overall_status\": \"passed\","` | — |
| [SRC-1A176AD4F0-L000043](../../tests/test_hosted_smoke.py#L43) | 43 | `"                \"checks\": {"` | — |
| [SRC-1A176AD4F0-L000044](../../tests/test_hosted_smoke.py#L44) | 44 | `"                    \"web_search\": {"` | — |
| [SRC-1A176AD4F0-L000045](../../tests/test_hosted_smoke.py#L45) | 45 | `"                        \"status\": \"passed\", \"result_count\": 2,"` | — |
| [SRC-1A176AD4F0-L000046](../../tests/test_hosted_smoke.py#L46) | 46 | `"                        \"provider_counts\": {\"bing_rss\": 1, \"duckduckgo_html\": 1},"` | — |
| [SRC-1A176AD4F0-L000047](../../tests/test_hosted_smoke.py#L47) | 47 | `"                    },"` | — |
| [SRC-1A176AD4F0-L000048](../../tests/test_hosted_smoke.py#L48) | 48 | `"                    \"language_model\": {\"status\": \"passed\", \"response_received\": True},"` | — |
| [SRC-1A176AD4F0-L000049](../../tests/test_hosted_smoke.py#L49) | 49 | `"                    \"social_search\": {\"status\": \"skipped\"},"` | — |
| [SRC-1A176AD4F0-L000050](../../tests/test_hosted_smoke.py#L50) | 50 | `"                },"` | — |
| [SRC-1A176AD4F0-L000051](../../tests/test_hosted_smoke.py#L51) | 51 | `"            })"` | — |
| [SRC-1A176AD4F0-L000052](../../tests/test_hosted_smoke.py#L52) | 52 | `"        elif self.path == \"/api/agent\":"` | — |
| [SRC-1A176AD4F0-L000053](../../tests/test_hosted_smoke.py#L53) | 53 | `"            self.respond(200, {"` | — |
| [SRC-1A176AD4F0-L000054](../../tests/test_hosted_smoke.py#L54) | 54 | `"                \"answer\": \"القاهرة هي عاصمة مصر. [المصدر 1]\","` | — |
| [SRC-1A176AD4F0-L000055](../../tests/test_hosted_smoke.py#L55) | 55 | `"                \"used_web_search\": True,"` | — |
| [SRC-1A176AD4F0-L000056](../../tests/test_hosted_smoke.py#L56) | 56 | `"                \"used_language_model\": True,"` | — |
| [SRC-1A176AD4F0-L000057](../../tests/test_hosted_smoke.py#L57) | 57 | `"                \"sources\": [{\"title\": \"مصدر اختبار\", \"url\": \"https://example.com/source\"}],"` | — |
| [SRC-1A176AD4F0-L000058](../../tests/test_hosted_smoke.py#L58) | 58 | `"                \"search_report\": {\"providers_used\": [\"bing_rss\"], \"pages_fetched\": 1},"` | — |
| [SRC-1A176AD4F0-L000059](../../tests/test_hosted_smoke.py#L59) | 59 | `"            })"` | — |
| [SRC-1A176AD4F0-L000060](../../tests/test_hosted_smoke.py#L60) | 60 | `"        else:"` | — |
| [SRC-1A176AD4F0-L000061](../../tests/test_hosted_smoke.py#L61) | 61 | `"            self.respond(404, {\"error\": \"not found\"})"` | — |
| [SRC-1A176AD4F0-L000062](../../tests/test_hosted_smoke.py#L62) | 62 | `""` | — |
| [SRC-1A176AD4F0-L000063](../../tests/test_hosted_smoke.py#L63) | 63 | `""` | — |
| [SRC-1A176AD4F0-L000064](../../tests/test_hosted_smoke.py#L64) | 64 | `"@pytest.fixture"` | — |
| [SRC-1A176AD4F0-L000065](../../tests/test_hosted_smoke.py#L65) | 65 | `"def hosted_server():"` | — |
| [SRC-1A176AD4F0-L000066](../../tests/test_hosted_smoke.py#L66) | 66 | `"    server = ThreadingHTTPServer((\"127.0.0.1\", 0), Handler)"` | — |
| [SRC-1A176AD4F0-L000067](../../tests/test_hosted_smoke.py#L67) | 67 | `"    thread = threading.Thread(target=server.serve_forever, daemon=True)"` | — |
| [SRC-1A176AD4F0-L000068](../../tests/test_hosted_smoke.py#L68) | 68 | `"    thread.start()"` | — |
| [SRC-1A176AD4F0-L000069](../../tests/test_hosted_smoke.py#L69) | 69 | `"    try:"` | — |
| [SRC-1A176AD4F0-L000070](../../tests/test_hosted_smoke.py#L70) | 70 | `"        yield f\"http://127.0.0.1:{server.server_port}\""` | — |
| [SRC-1A176AD4F0-L000071](../../tests/test_hosted_smoke.py#L71) | 71 | `"    finally:"` | — |
| [SRC-1A176AD4F0-L000072](../../tests/test_hosted_smoke.py#L72) | 72 | `"        server.shutdown()"` | — |
| [SRC-1A176AD4F0-L000073](../../tests/test_hosted_smoke.py#L73) | 73 | `"        server.server_close()"` | — |
| [SRC-1A176AD4F0-L000074](../../tests/test_hosted_smoke.py#L74) | 74 | `"        thread.join(timeout=2)"` | — |
| [SRC-1A176AD4F0-L000075](../../tests/test_hosted_smoke.py#L75) | 75 | `""` | — |
| [SRC-1A176AD4F0-L000076](../../tests/test_hosted_smoke.py#L76) | 76 | `""` | — |
| [SRC-1A176AD4F0-L000077](../../tests/test_hosted_smoke.py#L77) | 77 | `"def test_normalize_origin_requires_https_and_rejects_credentials_or_paths():"` | — |
| [SRC-1A176AD4F0-L000078](../../tests/test_hosted_smoke.py#L78) | 78 | `"    assert normalize_origin(\"https://example.com/\") == \"https://example.com\""` | — |
| [SRC-1A176AD4F0-L000079](../../tests/test_hosted_smoke.py#L79) | 79 | `"    for invalid in ("` | — |
| [SRC-1A176AD4F0-L000080](../../tests/test_hosted_smoke.py#L80) | 80 | `"        \"http://example.com\","` | — |
| [SRC-1A176AD4F0-L000081](../../tests/test_hosted_smoke.py#L81) | 81 | `"        \"https://user:password@example.com\","` | — |
| [SRC-1A176AD4F0-L000082](../../tests/test_hosted_smoke.py#L82) | 82 | `"        \"https://example.com/path\","` | — |
| [SRC-1A176AD4F0-L000083](../../tests/test_hosted_smoke.py#L83) | 83 | `"        \"https://example.com/?token=secret\","` | — |
| [SRC-1A176AD4F0-L000084](../../tests/test_hosted_smoke.py#L84) | 84 | `"    ):"` | — |
| [SRC-1A176AD4F0-L000085](../../tests/test_hosted_smoke.py#L85) | 85 | `"        with pytest.raises(SmokeError):"` | — |
| [SRC-1A176AD4F0-L000086](../../tests/test_hosted_smoke.py#L86) | 86 | `"            normalize_origin(invalid)"` | — |
| [SRC-1A176AD4F0-L000087](../../tests/test_hosted_smoke.py#L87) | 87 | `""` | — |
| [SRC-1A176AD4F0-L000088](../../tests/test_hosted_smoke.py#L88) | 88 | `""` | — |
| [SRC-1A176AD4F0-L000089](../../tests/test_hosted_smoke.py#L89) | 89 | `"def test_normalize_origin_allows_plain_http_only_for_local_test():"` | — |
| [SRC-1A176AD4F0-L000090](../../tests/test_hosted_smoke.py#L90) | 90 | `"    assert normalize_origin(\"http://127.0.0.1:8765\", allow_http=True) == ("` | — |
| [SRC-1A176AD4F0-L000091](../../tests/test_hosted_smoke.py#L91) | 91 | `"        \"http://127.0.0.1:8765\""` | — |
| [SRC-1A176AD4F0-L000092](../../tests/test_hosted_smoke.py#L92) | 92 | `"    )"` | — |
| [SRC-1A176AD4F0-L000093](../../tests/test_hosted_smoke.py#L93) | 93 | `"    with pytest.raises(SmokeError):"` | — |
| [SRC-1A176AD4F0-L000094](../../tests/test_hosted_smoke.py#L94) | 94 | `"        normalize_origin(\"http://example.com\", allow_http=True)"` | — |
| [SRC-1A176AD4F0-L000095](../../tests/test_hosted_smoke.py#L95) | 95 | `""` | — |
| [SRC-1A176AD4F0-L000096](../../tests/test_hosted_smoke.py#L96) | 96 | `""` | — |
| [SRC-1A176AD4F0-L000097](../../tests/test_hosted_smoke.py#L97) | 97 | `"def test_smoke_checks_health_auth_live_diagnostics_and_agent(hosted_server):"` | — |
| [SRC-1A176AD4F0-L000098](../../tests/test_hosted_smoke.py#L98) | 98 | `"    result = run_smoke(hosted_server, TOKEN, allow_http=True, timeout=5)"` | — |
| [SRC-1A176AD4F0-L000099](../../tests/test_hosted_smoke.py#L99) | 99 | `"    assert result[\"result\"] == \"passed\""` | — |
| [SRC-1A176AD4F0-L000100](../../tests/test_hosted_smoke.py#L100) | 100 | `"    assert result[\"checks\"][\"health\"] == \"passed\""` | — |
| [SRC-1A176AD4F0-L000101](../../tests/test_hosted_smoke.py#L101) | 101 | `"    assert result[\"checks\"][\"authentication\"] == \"passed\""` | — |
| [SRC-1A176AD4F0-L000102](../../tests/test_hosted_smoke.py#L102) | 102 | `"    assert result[\"checks\"][\"live_search\"][\"result_count\"] == 2"` | — |
| [SRC-1A176AD4F0-L000103](../../tests/test_hosted_smoke.py#L103) | 103 | `"    assert result[\"checks\"][\"agent_request\"][\"source_count\"] == 1"` | — |
| [SRC-1A176AD4F0-L000104](../../tests/test_hosted_smoke.py#L104) | 104 | `""` | — |
| [SRC-1A176AD4F0-L000105](../../tests/test_hosted_smoke.py#L105) | 105 | `""` | — |
| [SRC-1A176AD4F0-L000106](../../tests/test_hosted_smoke.py#L106) | 106 | `"def test_smoke_never_forwards_bearer_to_cross_origin_redirect():"` | — |
| [SRC-1A176AD4F0-L000107](../../tests/test_hosted_smoke.py#L107) | 107 | `"    received_authorizations = []"` | — |
| [SRC-1A176AD4F0-L000108](../../tests/test_hosted_smoke.py#L108) | 108 | `""` | — |
| [SRC-1A176AD4F0-L000109](../../tests/test_hosted_smoke.py#L109) | 109 | `"    class RedirectHandler(BaseHTTPRequestHandler):"` | — |
| [SRC-1A176AD4F0-L000110](../../tests/test_hosted_smoke.py#L110) | 110 | `"        def log_message(self, format: str, *args: object) -> None:"` | — |
| [SRC-1A176AD4F0-L000111](../../tests/test_hosted_smoke.py#L111) | 111 | `"            return"` | — |
| [SRC-1A176AD4F0-L000112](../../tests/test_hosted_smoke.py#L112) | 112 | `""` | — |
| [SRC-1A176AD4F0-L000113](../../tests/test_hosted_smoke.py#L113) | 113 | `"        def do_GET(self) -> None:"` | — |
| [SRC-1A176AD4F0-L000114](../../tests/test_hosted_smoke.py#L114) | 114 | `"            self.send_response(302)"` | — |
| [SRC-1A176AD4F0-L000115](../../tests/test_hosted_smoke.py#L115) | 115 | `"            self.send_header(\"Location\", self.server.redirect_destination)"` | — |
| [SRC-1A176AD4F0-L000116](../../tests/test_hosted_smoke.py#L116) | 116 | `"            self.send_header(\"Content-Length\", \"0\")"` | — |
| [SRC-1A176AD4F0-L000117](../../tests/test_hosted_smoke.py#L117) | 117 | `"            self.end_headers()"` | — |
| [SRC-1A176AD4F0-L000118](../../tests/test_hosted_smoke.py#L118) | 118 | `""` | — |
| [SRC-1A176AD4F0-L000119](../../tests/test_hosted_smoke.py#L119) | 119 | `"    class DestinationHandler(BaseHTTPRequestHandler):"` | — |
| [SRC-1A176AD4F0-L000120](../../tests/test_hosted_smoke.py#L120) | 120 | `"        def log_message(self, format: str, *args: object) -> None:"` | — |
| [SRC-1A176AD4F0-L000121](../../tests/test_hosted_smoke.py#L121) | 121 | `"            return"` | — |
| [SRC-1A176AD4F0-L000122](../../tests/test_hosted_smoke.py#L122) | 122 | `""` | — |
| [SRC-1A176AD4F0-L000123](../../tests/test_hosted_smoke.py#L123) | 123 | `"        def do_GET(self) -> None:"` | — |
| [SRC-1A176AD4F0-L000124](../../tests/test_hosted_smoke.py#L124) | 124 | `"            received_authorizations.append(self.headers.get(\"Authorization\"))"` | — |
| [SRC-1A176AD4F0-L000125](../../tests/test_hosted_smoke.py#L125) | 125 | `"            self.send_response(200)"` | — |
| [SRC-1A176AD4F0-L000126](../../tests/test_hosted_smoke.py#L126) | 126 | `"            self.send_header(\"Content-Length\", \"0\")"` | — |
| [SRC-1A176AD4F0-L000127](../../tests/test_hosted_smoke.py#L127) | 127 | `"            self.end_headers()"` | — |
| [SRC-1A176AD4F0-L000128](../../tests/test_hosted_smoke.py#L128) | 128 | `""` | — |
| [SRC-1A176AD4F0-L000129](../../tests/test_hosted_smoke.py#L129) | 129 | `"    destination = ThreadingHTTPServer((\"127.0.0.1\", 0), DestinationHandler)"` | — |
| [SRC-1A176AD4F0-L000130](../../tests/test_hosted_smoke.py#L130) | 130 | `"    source = ThreadingHTTPServer((\"127.0.0.1\", 0), RedirectHandler)"` | — |
| [SRC-1A176AD4F0-L000131](../../tests/test_hosted_smoke.py#L131) | 131 | `"    destination_thread = threading.Thread(target=destination.serve_forever, daemon=True)"` | — |
| [SRC-1A176AD4F0-L000132](../../tests/test_hosted_smoke.py#L132) | 132 | `"    source_thread = threading.Thread(target=source.serve_forever, daemon=True)"` | — |
| [SRC-1A176AD4F0-L000133](../../tests/test_hosted_smoke.py#L133) | 133 | `"    source.redirect_destination = ("` | — |
| [SRC-1A176AD4F0-L000134](../../tests/test_hosted_smoke.py#L134) | 134 | `"        f\"http://127.0.0.1:{destination.server_port}/capture\""` | — |
| [SRC-1A176AD4F0-L000135](../../tests/test_hosted_smoke.py#L135) | 135 | `"    )"` | — |
| [SRC-1A176AD4F0-L000136](../../tests/test_hosted_smoke.py#L136) | 136 | `"    destination_thread.start()"` | — |
| [SRC-1A176AD4F0-L000137](../../tests/test_hosted_smoke.py#L137) | 137 | `"    source_thread.start()"` | — |
| [SRC-1A176AD4F0-L000138](../../tests/test_hosted_smoke.py#L138) | 138 | `"    try:"` | — |
| [SRC-1A176AD4F0-L000139](../../tests/test_hosted_smoke.py#L139) | 139 | `"        status, payload = hosted_smoke_test.request_json("` | — |
| [SRC-1A176AD4F0-L000140](../../tests/test_hosted_smoke.py#L140) | 140 | `"            f\"http://127.0.0.1:{source.server_port}/redirect\","` | — |
| [SRC-1A176AD4F0-L000141](../../tests/test_hosted_smoke.py#L141) | 141 | `"            token=TOKEN,"` | — |
| [SRC-1A176AD4F0-L000142](../../tests/test_hosted_smoke.py#L142) | 142 | `"            timeout=3,"` | — |
| [SRC-1A176AD4F0-L000143](../../tests/test_hosted_smoke.py#L143) | 143 | `"        )"` | — |
| [SRC-1A176AD4F0-L000144](../../tests/test_hosted_smoke.py#L144) | 144 | `"        assert status == 302"` | — |
| [SRC-1A176AD4F0-L000145](../../tests/test_hosted_smoke.py#L145) | 145 | `"        assert payload is None"` | — |
| [SRC-1A176AD4F0-L000146](../../tests/test_hosted_smoke.py#L146) | 146 | `"        assert received_authorizations == []"` | — |
| [SRC-1A176AD4F0-L000147](../../tests/test_hosted_smoke.py#L147) | 147 | `"    finally:"` | — |
| [SRC-1A176AD4F0-L000148](../../tests/test_hosted_smoke.py#L148) | 148 | `"        source.shutdown()"` | — |
| [SRC-1A176AD4F0-L000149](../../tests/test_hosted_smoke.py#L149) | 149 | `"        destination.shutdown()"` | — |
| [SRC-1A176AD4F0-L000150](../../tests/test_hosted_smoke.py#L150) | 150 | `"        source.server_close()"` | — |
| [SRC-1A176AD4F0-L000151](../../tests/test_hosted_smoke.py#L151) | 151 | `"        destination.server_close()"` | — |
| [SRC-1A176AD4F0-L000152](../../tests/test_hosted_smoke.py#L152) | 152 | `"        source_thread.join(timeout=2)"` | — |
| [SRC-1A176AD4F0-L000153](../../tests/test_hosted_smoke.py#L153) | 153 | `"        destination_thread.join(timeout=2)"` | — |
| [SRC-1A176AD4F0-L000154](../../tests/test_hosted_smoke.py#L154) | 154 | `""` | — |
| [SRC-1A176AD4F0-L000155](../../tests/test_hosted_smoke.py#L155) | 155 | `""` | — |
| [SRC-1A176AD4F0-L000156](../../tests/test_hosted_smoke.py#L156) | 156 | `"def test_smoke_refuses_missing_or_short_access_token(hosted_server):"` | — |
| [SRC-1A176AD4F0-L000157](../../tests/test_hosted_smoke.py#L157) | 157 | `"    with pytest.raises(SmokeError, match=\"OMARAI_ACCESS_TOKEN\"):"` | — |
| [SRC-1A176AD4F0-L000158](../../tests/test_hosted_smoke.py#L158) | 158 | `"        run_smoke(hosted_server, \"\", allow_http=True, timeout=5)"` | — |
| [SRC-1A176AD4F0-L000159](../../tests/test_hosted_smoke.py#L159) | 159 | `""` | — |
| [SRC-1A176AD4F0-L000160](../../tests/test_hosted_smoke.py#L160) | 160 | `""` | — |
| [SRC-1A176AD4F0-L000161](../../tests/test_hosted_smoke.py#L161) | 161 | `"def test_smoke_fails_when_agent_returns_no_live_source(hosted_server, monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000162](../../tests/test_hosted_smoke.py#L162) | 162 | `"    original = hosted_smoke_test.request_json"` | — |
| [SRC-1A176AD4F0-L000163](../../tests/test_hosted_smoke.py#L163) | 163 | `""` | — |
| [SRC-1A176AD4F0-L000164](../../tests/test_hosted_smoke.py#L164) | 164 | `"    def without_sources(url: str, **kwargs):"` | — |
| [SRC-1A176AD4F0-L000165](../../tests/test_hosted_smoke.py#L165) | 165 | `"        if urlsplit(url).path == \"/api/agent\" and kwargs.get(\"token\") == TOKEN:"` | — |
| [SRC-1A176AD4F0-L000166](../../tests/test_hosted_smoke.py#L166) | 166 | `"            return 200, {"` | — |
| [SRC-1A176AD4F0-L000167](../../tests/test_hosted_smoke.py#L167) | 167 | `"                \"answer\": \"إجابة بلا مصادر\", \"used_web_search\": False,"` | — |
| [SRC-1A176AD4F0-L000168](../../tests/test_hosted_smoke.py#L168) | 168 | `"                \"used_language_model\": True, \"sources\": [],"` | — |
| [SRC-1A176AD4F0-L000169](../../tests/test_hosted_smoke.py#L169) | 169 | `"            }"` | — |
| [SRC-1A176AD4F0-L000170](../../tests/test_hosted_smoke.py#L170) | 170 | `"        return original(url, **kwargs)"` | — |
| [SRC-1A176AD4F0-L000171](../../tests/test_hosted_smoke.py#L171) | 171 | `""` | — |
| [SRC-1A176AD4F0-L000172](../../tests/test_hosted_smoke.py#L172) | 172 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", without_sources)"` | — |
| [SRC-1A176AD4F0-L000173](../../tests/test_hosted_smoke.py#L173) | 173 | `"    with pytest.raises(SmokeError, match=\"usable source URLs\"):"` | — |
| [SRC-1A176AD4F0-L000174](../../tests/test_hosted_smoke.py#L174) | 174 | `"        run_smoke(hosted_server, TOKEN, allow_http=True, timeout=5)"` | — |
| [SRC-1A176AD4F0-L000175](../../tests/test_hosted_smoke.py#L175) | 175 | `""` | — |
| [SRC-1A176AD4F0-L000176](../../tests/test_hosted_smoke.py#L176) | 176 | `""` | — |
| [SRC-1A176AD4F0-L000177](../../tests/test_hosted_smoke.py#L177) | 177 | `"def test_smoke_rejects_invalid_expected_source_sha(hosted_server):"` | — |
| [SRC-1A176AD4F0-L000178](../../tests/test_hosted_smoke.py#L178) | 178 | `"    with pytest.raises(SmokeError, match=\"40-character Git SHA\"):"` | — |
| [SRC-1A176AD4F0-L000179](../../tests/test_hosted_smoke.py#L179) | 179 | `"        run_smoke("` | — |
| [SRC-1A176AD4F0-L000180](../../tests/test_hosted_smoke.py#L180) | 180 | `"            hosted_server, TOKEN, allow_http=True, timeout=5, expected_sha=\"main\""` | — |
| [SRC-1A176AD4F0-L000181](../../tests/test_hosted_smoke.py#L181) | 181 | `"        )"` | — |
| [SRC-1A176AD4F0-L000182](../../tests/test_hosted_smoke.py#L182) | 182 | `""` | — |
| [SRC-1A176AD4F0-L000183](../../tests/test_hosted_smoke.py#L183) | 183 | `""` | — |
| [SRC-1A176AD4F0-L000184](../../tests/test_hosted_smoke.py#L184) | 184 | `"def test_smoke_rejects_deployed_build_sha_mismatch(hosted_server):"` | — |
| [SRC-1A176AD4F0-L000185](../../tests/test_hosted_smoke.py#L185) | 185 | `"    with pytest.raises(SmokeError, match=\"does not match the expected Git commit\"):"` | — |
| [SRC-1A176AD4F0-L000186](../../tests/test_hosted_smoke.py#L186) | 186 | `"        run_smoke("` | — |
| [SRC-1A176AD4F0-L000187](../../tests/test_hosted_smoke.py#L187) | 187 | `"            hosted_server,"` | — |
| [SRC-1A176AD4F0-L000188](../../tests/test_hosted_smoke.py#L188) | 188 | `"            TOKEN,"` | — |
| [SRC-1A176AD4F0-L000189](../../tests/test_hosted_smoke.py#L189) | 189 | `"            allow_http=True,"` | — |
| [SRC-1A176AD4F0-L000190](../../tests/test_hosted_smoke.py#L190) | 190 | `"            timeout=5,"` | — |
| [SRC-1A176AD4F0-L000191](../../tests/test_hosted_smoke.py#L191) | 191 | `"            expected_sha=\"a\" * 40,"` | — |
| [SRC-1A176AD4F0-L000192](../../tests/test_hosted_smoke.py#L192) | 192 | `"        )"` | — |
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
| [SRC-EA6EC52573-L000151](../../tests/test_intent_router.py#L151) | 151 | `"    assert decision[\"needs_clarification\"] is True"` | — |
| [SRC-EA6EC52573-L000152](../../tests/test_intent_router.py#L152) | 152 | `""` | — |
| [SRC-EA6EC52573-L000153](../../tests/test_intent_router.py#L153) | 153 | `""` | — |
| [SRC-EA6EC52573-L000154](../../tests/test_intent_router.py#L154) | 154 | `"def test_followup_resolver_uses_topic_from_latest_user_turn() -> None:"` | — |
| [SRC-EA6EC52573-L000155](../../tests/test_intent_router.py#L155) | 155 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000156](../../tests/test_intent_router.py#L156) | 156 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر آيفون 16 في مصر\"},"` | — |
| [SRC-EA6EC52573-L000157](../../tests/test_intent_router.py#L157) | 157 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن معلومات موثوقة.\"},"` | — |
| [SRC-EA6EC52573-L000158](../../tests/test_intent_router.py#L158) | 158 | `"    ]"` | — |
| [SRC-EA6EC52573-L000159](../../tests/test_intent_router.py#L159) | 159 | `"    resolved = resolve_followup_query(\"هل فيه ضمان؟\", history)"` | — |
| [SRC-EA6EC52573-L000160](../../tests/test_intent_router.py#L160) | 160 | `"    assert \"آيفون 16\" in resolved"` | — |
| [SRC-EA6EC52573-L000161](../../tests/test_intent_router.py#L161) | 161 | `"    assert \"ضمان\" in resolved"` | — |
| [SRC-EA6EC52573-L000162](../../tests/test_intent_router.py#L162) | 162 | `""` | — |
| [SRC-EA6EC52573-L000163](../../tests/test_intent_router.py#L163) | 163 | `""` | — |
| [SRC-EA6EC52573-L000164](../../tests/test_intent_router.py#L164) | 164 | `"def test_followup_resolver_does_not_resurrect_topic_after_acknowledgment() -> None:"` | — |
| [SRC-EA6EC52573-L000165](../../tests/test_intent_router.py#L165) | 165 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000166](../../tests/test_intent_router.py#L166) | 166 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر آيفون 16 في مصر\"},"` | — |
| [SRC-EA6EC52573-L000167](../../tests/test_intent_router.py#L167) | 167 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن معلومات موثوقة.\"},"` | — |
| [SRC-EA6EC52573-L000168](../../tests/test_intent_router.py#L168) | 168 | `"        {\"role\": \"user\", \"content\": \"شكرًا\"},"` | — |
| [SRC-EA6EC52573-L000169](../../tests/test_intent_router.py#L169) | 169 | `"        {\"role\": \"assistant\", \"content\": \"العفو.\"},"` | — |
| [SRC-EA6EC52573-L000170](../../tests/test_intent_router.py#L170) | 170 | `"    ]"` | — |
| [SRC-EA6EC52573-L000171](../../tests/test_intent_router.py#L171) | 171 | `"    assert resolve_followup_query(\"فين؟\", history) == \"فين؟\""` | — |
| [SRC-EA6EC52573-L000172](../../tests/test_intent_router.py#L172) | 172 | `""` | — |
| [SRC-EA6EC52573-L000173](../../tests/test_intent_router.py#L173) | 173 | `""` | — |
| [SRC-EA6EC52573-L000174](../../tests/test_intent_router.py#L174) | 174 | `"def test_followup_resolver_bounds_output_and_handles_malformed_history() -> None:"` | — |
| [SRC-EA6EC52573-L000175](../../tests/test_intent_router.py#L175) | 175 | `"    history = [{\"role\": \"user\", \"content\": \"س\" * 4000}]"` | — |
| [SRC-EA6EC52573-L000176](../../tests/test_intent_router.py#L176) | 176 | `"    assert len(resolve_followup_query(\"والسعر؟\", history)) <= 500"` | — |
| [SRC-EA6EC52573-L000177](../../tests/test_intent_router.py#L177) | 177 | `"    assert resolve_followup_query(\"فين؟\", {\"role\": \"user\", \"content\": \"topic\"}) == \"فين؟\""` | — |
## اختبارات

### FILE-4397BC2CD2 — [tests/test_intent_router_integration.py](../../tests/test_intent_router_integration.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-4397BC2CD2-L000001](../../tests/test_intent_router_integration.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-4397BC2CD2-L000002](../../tests/test_intent_router_integration.py#L2) | 2 | `""` | — |
| [SRC-4397BC2CD2-L000003](../../tests/test_intent_router_integration.py#L3) | 3 | `"import pytest"` | — |
| [SRC-4397BC2CD2-L000004](../../tests/test_intent_router_integration.py#L4) | 4 | `""` | — |
| [SRC-4397BC2CD2-L000005](../../tests/test_intent_router_integration.py#L5) | 5 | `"from agents.research import evidence_signal_report"` | — |
| [SRC-4397BC2CD2-L000006](../../tests/test_intent_router_integration.py#L6) | 6 | `"from agents.web_agent import WebAgent"` | — |
| [SRC-4397BC2CD2-L000007](../../tests/test_intent_router_integration.py#L7) | 7 | `""` | — |
| [SRC-4397BC2CD2-L000008](../../tests/test_intent_router_integration.py#L8) | 8 | `""` | — |
| [SRC-4397BC2CD2-L000009](../../tests/test_intent_router_integration.py#L9) | 9 | `"def _evidence(domain: str, queries: list[str]) -> dict:"` | — |
| [SRC-4397BC2CD2-L000010](../../tests/test_intent_router_integration.py#L10) | 10 | `"    return {"` | — |
| [SRC-4397BC2CD2-L000011](../../tests/test_intent_router_integration.py#L11) | 11 | `"        \"title\": \"iPhone 17 price information in Egypt\","` | — |
| [SRC-4397BC2CD2-L000012](../../tests/test_intent_router_integration.py#L12) | 12 | `"        \"url\": f\"https://{domain}/iphone-17-price\","` | — |
| [SRC-4397BC2CD2-L000013](../../tests/test_intent_router_integration.py#L13) | 13 | `"        \"snippet\": \"Published price information for iPhone 17 in Egypt.\","` | — |
| [SRC-4397BC2CD2-L000014](../../tests/test_intent_router_integration.py#L14) | 14 | `"        \"page_text\": \"Price information for iPhone 17 in Egypt.\","` | — |
| [SRC-4397BC2CD2-L000015](../../tests/test_intent_router_integration.py#L15) | 15 | `"        \"page_fetched\": True,"` | — |
| [SRC-4397BC2CD2-L000016](../../tests/test_intent_router_integration.py#L16) | 16 | `"        \"providers\": [\"test_search\"],"` | — |
| [SRC-4397BC2CD2-L000017](../../tests/test_intent_router_integration.py#L17) | 17 | `"        \"queries\": list(queries),"` | — |
| [SRC-4397BC2CD2-L000018](../../tests/test_intent_router_integration.py#L18) | 18 | `"        \"domain\": domain,"` | — |
| [SRC-4397BC2CD2-L000019](../../tests/test_intent_router_integration.py#L19) | 19 | `"        \"source_class\": \"general\","` | — |
| [SRC-4397BC2CD2-L000020](../../tests/test_intent_router_integration.py#L20) | 20 | `"        \"platform\": \"web\","` | — |
| [SRC-4397BC2CD2-L000021](../../tests/test_intent_router_integration.py#L21) | 21 | `"        \"published_at\": \"\","` | — |
| [SRC-4397BC2CD2-L000022](../../tests/test_intent_router_integration.py#L22) | 22 | `"        \"rank_score\": 1.0,"` | — |
| [SRC-4397BC2CD2-L000023](../../tests/test_intent_router_integration.py#L23) | 23 | `"    }"` | — |
| [SRC-4397BC2CD2-L000024](../../tests/test_intent_router_integration.py#L24) | 24 | `""` | — |
| [SRC-4397BC2CD2-L000025](../../tests/test_intent_router_integration.py#L25) | 25 | `""` | — |
| [SRC-4397BC2CD2-L000026](../../tests/test_intent_router_integration.py#L26) | 26 | `"def _report(plan: dict, sources: list[dict]) -> dict:"` | — |
| [SRC-4397BC2CD2-L000027](../../tests/test_intent_router_integration.py#L27) | 27 | `"    return {"` | — |
| [SRC-4397BC2CD2-L000028](../../tests/test_intent_router_integration.py#L28) | 28 | `"        \"queries_planned\": len(plan.get(\"queries\", [])),"` | — |
| [SRC-4397BC2CD2-L000029](../../tests/test_intent_router_integration.py#L29) | 29 | `"        \"queries_attempted\": len(plan.get(\"queries\", [])),"` | — |
| [SRC-4397BC2CD2-L000030](../../tests/test_intent_router_integration.py#L30) | 30 | `"        \"query_results\": [],"` | — |
| [SRC-4397BC2CD2-L000031](../../tests/test_intent_router_integration.py#L31) | 31 | `"        \"unique_sources\": len(sources),"` | — |
| [SRC-4397BC2CD2-L000032](../../tests/test_intent_router_integration.py#L32) | 32 | `"        \"pages_fetched\": len(sources),"` | — |
| [SRC-4397BC2CD2-L000033](../../tests/test_intent_router_integration.py#L33) | 33 | `"        \"providers_used\": [\"test_search\"],"` | — |
| [SRC-4397BC2CD2-L000034](../../tests/test_intent_router_integration.py#L34) | 34 | `"        \"provider_counts\": {\"test_search\": len(sources)},"` | — |
| [SRC-4397BC2CD2-L000035](../../tests/test_intent_router_integration.py#L35) | 35 | `"        \"platform_counts\": {\"web\": len(sources)},"` | — |
| [SRC-4397BC2CD2-L000036](../../tests/test_intent_router_integration.py#L36) | 36 | `"        \"social_direct_results\": 0,"` | — |
| [SRC-4397BC2CD2-L000037](../../tests/test_intent_router_integration.py#L37) | 37 | `"        \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-4397BC2CD2-L000038](../../tests/test_intent_router_integration.py#L38) | 38 | `"        \"planning_method\": plan.get(\"planning_method\", \"test\"),"` | — |
| [SRC-4397BC2CD2-L000039](../../tests/test_intent_router_integration.py#L39) | 39 | `"        \"evidence_signals\": evidence_signal_report(sources),"` | — |
| [SRC-4397BC2CD2-L000040](../../tests/test_intent_router_integration.py#L40) | 40 | `"    }"` | — |
| [SRC-4397BC2CD2-L000041](../../tests/test_intent_router_integration.py#L41) | 41 | `""` | — |
| [SRC-4397BC2CD2-L000042](../../tests/test_intent_router_integration.py#L42) | 42 | `""` | — |
| [SRC-4397BC2CD2-L000043](../../tests/test_intent_router_integration.py#L43) | 43 | `"def test_greeting_is_local_without_model_or_search(monkeypatch) -> None:"` | — |
| [SRC-4397BC2CD2-L000044](../../tests/test_intent_router_integration.py#L44) | 44 | `"    agent = WebAgent()"` | — |
| [SRC-4397BC2CD2-L000045](../../tests/test_intent_router_integration.py#L45) | 45 | `""` | — |
| [SRC-4397BC2CD2-L000046](../../tests/test_intent_router_integration.py#L46) | 46 | `"    def unexpected(*args, **kwargs):"` | — |
| [SRC-4397BC2CD2-L000047](../../tests/test_intent_router_integration.py#L47) | 47 | `"        pytest.fail(\"Greeting must not call the model or search.\")"` | — |
| [SRC-4397BC2CD2-L000048](../../tests/test_intent_router_integration.py#L48) | 48 | `""` | — |
| [SRC-4397BC2CD2-L000049](../../tests/test_intent_router_integration.py#L49) | 49 | `"    monkeypatch.setattr(agent, \"_answer_without_search\", unexpected)"` | — |
| [SRC-4397BC2CD2-L000050](../../tests/test_intent_router_integration.py#L50) | 50 | `"    monkeypatch.setattr(agent, \"_plan_search\", unexpected)"` | — |
| [SRC-4397BC2CD2-L000051](../../tests/test_intent_router_integration.py#L51) | 51 | `""` | — |
| [SRC-4397BC2CD2-L000052](../../tests/test_intent_router_integration.py#L52) | 52 | `"    result = agent.answer(\"ازيك؟ عامل ايه النهاردة؟\")"` | — |
| [SRC-4397BC2CD2-L000053](../../tests/test_intent_router_integration.py#L53) | 53 | `""` | — |
| [SRC-4397BC2CD2-L000054](../../tests/test_intent_router_integration.py#L54) | 54 | `"    assert result[\"kind\"] == \"local_conversation\""` | — |
| [SRC-4397BC2CD2-L000055](../../tests/test_intent_router_integration.py#L55) | 55 | `"    assert result[\"intent_route\"] == \"LOCAL\""` | — |
| [SRC-4397BC2CD2-L000056](../../tests/test_intent_router_integration.py#L56) | 56 | `"    assert result[\"research_plan\"][\"intent_route\"] == \"LOCAL\""` | — |
| [SRC-4397BC2CD2-L000057](../../tests/test_intent_router_integration.py#L57) | 57 | `"    assert result[\"used_web_search\"] is False"` | — |
| [SRC-4397BC2CD2-L000058](../../tests/test_intent_router_integration.py#L58) | 58 | `"    assert result[\"used_language_model\"] is False"` | — |
| [SRC-4397BC2CD2-L000059](../../tests/test_intent_router_integration.py#L59) | 59 | `"    assert result[\"sources\"] == []"` | — |
| [SRC-4397BC2CD2-L000060](../../tests/test_intent_router_integration.py#L60) | 60 | `""` | — |
| [SRC-4397BC2CD2-L000061](../../tests/test_intent_router_integration.py#L61) | 61 | `""` | — |
| [SRC-4397BC2CD2-L000062](../../tests/test_intent_router_integration.py#L62) | 62 | `"def test_ambiguous_question_clarifies_without_model_or_search(monkeypatch) -> None:"` | — |
