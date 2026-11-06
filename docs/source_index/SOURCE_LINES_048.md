# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **048**
- سجلات الأسطر: **800**
- النطاق: SRC-829A979985-L000471 إلى SRC-1A176AD4F0-L000271
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-829A979985 — [tests/test_generation_acceptance_matrix.py](../../tests/test_generation_acceptance_matrix.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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
| [SRC-829A979985-L000563](../../tests/test_generation_acceptance_matrix.py#L563) | 563 | `"    monkeypatch.setattr(agent, \"_verify_semantic_claims\", lambda *args, **kwargs: {"` | — |
| [SRC-829A979985-L000564](../../tests/test_generation_acceptance_matrix.py#L564) | 564 | `"        \"status\": \"completed_all_claims_supported\","` | — |
| [SRC-829A979985-L000565](../../tests/test_generation_acceptance_matrix.py#L565) | 565 | `"        \"withhold_answer\": False,"` | — |
| [SRC-829A979985-L000566](../../tests/test_generation_acceptance_matrix.py#L566) | 566 | `"        \"semantic_verification\": \"model_assessed_source_support\","` | — |
| [SRC-829A979985-L000567](../../tests/test_generation_acceptance_matrix.py#L567) | 567 | `"        \"fact_correctness\": \"not_verified\","` | — |
| [SRC-829A979985-L000568](../../tests/test_generation_acceptance_matrix.py#L568) | 568 | `"    })"` | — |
| [SRC-829A979985-L000569](../../tests/test_generation_acceptance_matrix.py#L569) | 569 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000570](../../tests/test_generation_acceptance_matrix.py#L570) | 570 | `"        agent,"` | — |
| [SRC-829A979985-L000571](../../tests/test_generation_acceptance_matrix.py#L571) | 571 | `"        \"_repair_answer_coverage\","` | — |
| [SRC-829A979985-L000572](../../tests/test_generation_acceptance_matrix.py#L572) | 572 | `"        lambda question, answer, sources, missing_targets: repaired_answer,"` | — |
| [SRC-829A979985-L000573](../../tests/test_generation_acceptance_matrix.py#L573) | 573 | `"    )"` | — |
| [SRC-829A979985-L000574](../../tests/test_generation_acceptance_matrix.py#L574) | 574 | `""` | — |
| [SRC-829A979985-L000575](../../tests/test_generation_acceptance_matrix.py#L575) | 575 | `"    result = agent.answer(question)"` | — |
| [SRC-829A979985-L000576](../../tests/test_generation_acceptance_matrix.py#L576) | 576 | `""` | — |
| [SRC-829A979985-L000577](../../tests/test_generation_acceptance_matrix.py#L577) | 577 | `"    assert result[\"search_attempted\"] is True"` | — |
| [SRC-829A979985-L000578](../../tests/test_generation_acceptance_matrix.py#L578) | 578 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-829A979985-L000579](../../tests/test_generation_acceptance_matrix.py#L579) | 579 | `"    assert len(result[\"sources\"]) == 2"` | — |
| [SRC-829A979985-L000580](../../tests/test_generation_acceptance_matrix.py#L580) | 580 | `"    assert result[\"search_report\"][\"search_outcome\"] == \"attempted_with_usable_sources\""` | — |
| [SRC-829A979985-L000581](../../tests/test_generation_acceptance_matrix.py#L581) | 581 | `"    assert result[\"search_report\"][\"pages_fetched\"] == 1"` | — |
| [SRC-829A979985-L000582](../../tests/test_generation_acceptance_matrix.py#L582) | 582 | `"    assert result[\"final_answer_status\"] == \"model_answer_generated\""` | — |
| [SRC-829A979985-L000583](../../tests/test_generation_acceptance_matrix.py#L583) | 583 | `"    assert result[\"coverage_repair_status\"] == \"revised_and_reaudited\""` | — |
| [SRC-829A979985-L000584](../../tests/test_generation_acceptance_matrix.py#L584) | 584 | `"    assert result[\"search_report\"][\"second_pass_review\"] == \"model_claim_audit_completed\""` | — |
| [SRC-829A979985-L000585](../../tests/test_generation_acceptance_matrix.py#L585) | 585 | `"    assert result[\"answer_coverage\"][\"automatically_graded\"] is False"` | — |
| [SRC-829A979985-L000586](../../tests/test_generation_acceptance_matrix.py#L586) | 586 | `"    assert result[\"answer_coverage\"][\"status\"] == \"model_review_requested_not_machine_verified\""` | — |
| [SRC-829A979985-L000587](../../tests/test_generation_acceptance_matrix.py#L587) | 587 | `"    assert \"السعر الإجمالي\" in result[\"answer\"]"` | — |
| [SRC-829A979985-L000588](../../tests/test_generation_acceptance_matrix.py#L588) | 588 | `"    assert \"البيانات الناقصة\" in result[\"answer\"]"` | — |
| [SRC-829A979985-L000589](../../tests/test_generation_acceptance_matrix.py#L589) | 589 | `"    assert result[\"citation_validation\"][\"method\"] == \"numeric_source_index_range_only\""` | — |
| [SRC-829A979985-L000590](../../tests/test_generation_acceptance_matrix.py#L590) | 590 | `"    assert result[\"answer_integrity\"][\"method\"] == \"deterministic_lexical_screen_only\""` | — |
| [SRC-829A979985-L000591](../../tests/test_generation_acceptance_matrix.py#L591) | 591 | `"    assert result[\"answer_integrity\"][\"semantic_verification\"] is False"` | — |
| [SRC-829A979985-L000592](../../tests/test_generation_acceptance_matrix.py#L592) | 592 | `"    assert result[\"search_report\"][\"answer_integrity\"] == result[\"answer_integrity\"]"` | — |
| [SRC-829A979985-L000593](../../tests/test_generation_acceptance_matrix.py#L593) | 593 | `"    assert result[\"answer_integrity\"][\"pages_with_extracted_text\"] == 1"` | — |
| [SRC-829A979985-L000594](../../tests/test_generation_acceptance_matrix.py#L594) | 594 | `"    assert result[\"answer_integrity\"][\"potentially_missing_target_count\"] >= 0"` | — |
| [SRC-829A979985-L000595](../../tests/test_generation_acceptance_matrix.py#L595) | 595 | `""` | — |
| [SRC-829A979985-L000596](../../tests/test_generation_acceptance_matrix.py#L596) | 596 | `""` | — |
| [SRC-829A979985-L000597](../../tests/test_generation_acceptance_matrix.py#L597) | 597 | `"@pytest.mark.parametrize("` | — |
| [SRC-829A979985-L000598](../../tests/test_generation_acceptance_matrix.py#L598) | 598 | `"    \"malformed_review\","` | — |
| [SRC-829A979985-L000599](../../tests/test_generation_acceptance_matrix.py#L599) | 599 | `"    ["` | — |
| [SRC-829A979985-L000600](../../tests/test_generation_acceptance_matrix.py#L600) | 600 | `"        \"إجابة من دون أي علامات فصل\","` | — |
| [SRC-829A979985-L000601](../../tests/test_generation_acceptance_matrix.py#L601) | 601 | `"        \"<<<OMARAI_FINAL_ANSWER>>>إجابة بلا علامة نهاية\","` | — |
| [SRC-829A979985-L000602](../../tests/test_generation_acceptance_matrix.py#L602) | 602 | `"        \"<<<OMARAI_FINAL_ANSWER>>>إجابة<<<END_OMARAI_FINAL_ANSWER>>> نص زائد خارج الإجابة\","` | — |
| [SRC-829A979985-L000603](../../tests/test_generation_acceptance_matrix.py#L603) | 603 | `"    ],"` | — |
| [SRC-829A979985-L000604](../../tests/test_generation_acceptance_matrix.py#L604) | 604 | `")"` | — |
| [SRC-829A979985-L000605](../../tests/test_generation_acceptance_matrix.py#L605) | 605 | `"def test_reviewer_rejects_missing_or_unbounded_final_answer_delimiters("` | — |
| [SRC-829A979985-L000606](../../tests/test_generation_acceptance_matrix.py#L606) | 606 | `"    monkeypatch, malformed_review"` | — |
| [SRC-829A979985-L000607](../../tests/test_generation_acceptance_matrix.py#L607) | 607 | `"):"` | — |
| [SRC-829A979985-L000608](../../tests/test_generation_acceptance_matrix.py#L608) | 608 | `"    agent = WebAgent()"` | — |
| [SRC-829A979985-L000609](../../tests/test_generation_acceptance_matrix.py#L609) | 609 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000610](../../tests/test_generation_acceptance_matrix.py#L610) | 610 | `"        agent,"` | — |
| [SRC-829A979985-L000611](../../tests/test_generation_acceptance_matrix.py#L611) | 611 | `"        \"_request_completion\","` | — |
| [SRC-829A979985-L000612](../../tests/test_generation_acceptance_matrix.py#L612) | 612 | `"        lambda *args, **kwargs: malformed_review,"` | — |
| [SRC-829A979985-L000613](../../tests/test_generation_acceptance_matrix.py#L613) | 613 | `"    )"` | — |
| [SRC-829A979985-L000614](../../tests/test_generation_acceptance_matrix.py#L614) | 614 | `"    test_source = source("` | — |
| [SRC-829A979985-L000615](../../tests/test_generation_acceptance_matrix.py#L615) | 615 | `"        \"https://one.example/page\","` | — |
| [SRC-829A979985-L000616](../../tests/test_generation_acceptance_matrix.py#L616) | 616 | `"        \"one.example\","` | — |
| [SRC-829A979985-L000617](../../tests/test_generation_acceptance_matrix.py#L617) | 617 | `"        page_fetched=True,"` | — |
| [SRC-829A979985-L000618](../../tests/test_generation_acceptance_matrix.py#L618) | 618 | `"        page_text=\"نص الصفحة\","` | — |
| [SRC-829A979985-L000619](../../tests/test_generation_acceptance_matrix.py#L619) | 619 | `"    )"` | — |
| [SRC-829A979985-L000620](../../tests/test_generation_acceptance_matrix.py#L620) | 620 | `""` | — |
| [SRC-829A979985-L000621](../../tests/test_generation_acceptance_matrix.py#L621) | 621 | `"    with pytest.raises(RuntimeError, match=\"فصل الإجابة النهائية\"):"` | — |
| [SRC-829A979985-L000622](../../tests/test_generation_acceptance_matrix.py#L622) | 622 | `"        agent._review_answer(\"ما مضمون الصفحة؟\", \"مسودة\", [test_source])"` | — |
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
| [SRC-AAA21D04E8-L000040](../../tests/test_generation_capabilities.py#L40) | 40 | `"    monkeypatch.setattr(\"agents.web_agent._open_model_request\", fake_urlopen)"` | — |
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
| [SRC-AAA21D04E8-L000074](../../tests/test_generation_capabilities.py#L74) | 74 | `"    monkeypatch.setattr(\"agents.web_agent._open_model_request\", fake_urlopen)"` | — |
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
| [SRC-AAA21D04E8-L000097](../../tests/test_generation_capabilities.py#L97) | 97 | `"    monkeypatch.setattr(\"agents.web_agent._open_model_request\", fake_urlopen)"` | — |
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
| [SRC-AAA21D04E8-L000290](../../tests/test_generation_capabilities.py#L290) | 290 | `""` | — |
| [SRC-AAA21D04E8-L000291](../../tests/test_generation_capabilities.py#L291) | 291 | `"def test_model_http_429_is_classified_and_bounded_fallback_can_recover(monkeypatch):"` | — |
| [SRC-AAA21D04E8-L000292](../../tests/test_generation_capabilities.py#L292) | 292 | `"    from urllib.error import HTTPError"` | — |
| [SRC-AAA21D04E8-L000293](../../tests/test_generation_capabilities.py#L293) | 293 | `""` | — |
| [SRC-AAA21D04E8-L000294](../../tests/test_generation_capabilities.py#L294) | 294 | `"    agent = WebAgent()"` | — |
| [SRC-AAA21D04E8-L000295](../../tests/test_generation_capabilities.py#L295) | 295 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-AAA21D04E8-L000296](../../tests/test_generation_capabilities.py#L296) | 296 | `"    agent.fallback_model = \"backup/model\""` | — |
| [SRC-AAA21D04E8-L000297](../../tests/test_generation_capabilities.py#L297) | 297 | `"    calls: list[str] = []"` | — |
| [SRC-AAA21D04E8-L000298](../../tests/test_generation_capabilities.py#L298) | 298 | `""` | — |
| [SRC-AAA21D04E8-L000299](../../tests/test_generation_capabilities.py#L299) | 299 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-AAA21D04E8-L000300](../../tests/test_generation_capabilities.py#L300) | 300 | `"        model = json.loads(request.data.decode(\"utf-8\"))[\"model\"]"` | — |
| [SRC-AAA21D04E8-L000301](../../tests/test_generation_capabilities.py#L301) | 301 | `"        calls.append(model)"` | — |
| [SRC-AAA21D04E8-L000302](../../tests/test_generation_capabilities.py#L302) | 302 | `"        if model == \"primary/model\":"` | — |
| [SRC-AAA21D04E8-L000303](../../tests/test_generation_capabilities.py#L303) | 303 | `"            raise HTTPError(request.full_url, 429, \"Too Many Requests\", None, None)"` | — |
| [SRC-AAA21D04E8-L000304](../../tests/test_generation_capabilities.py#L304) | 304 | `"        return FakeResponse(\"إجابة مكتملة من النموذج الاحتياطي\", \"stop\")"` | — |
| [SRC-AAA21D04E8-L000305](../../tests/test_generation_capabilities.py#L305) | 305 | `""` | — |
| [SRC-AAA21D04E8-L000306](../../tests/test_generation_capabilities.py#L306) | 306 | `"    monkeypatch.setattr(\"agents.web_agent._open_model_request\", fake_urlopen)"` | — |
| [SRC-AAA21D04E8-L000307](../../tests/test_generation_capabilities.py#L307) | 307 | `"    answer = agent._request_completion("` | — |
| [SRC-AAA21D04E8-L000308](../../tests/test_generation_capabilities.py#L308) | 308 | `"        [{\"role\": \"user\", \"content\": \"اختبار\"}], model=\"primary/model\""` | — |
| [SRC-AAA21D04E8-L000309](../../tests/test_generation_capabilities.py#L309) | 309 | `"    )"` | — |
| [SRC-AAA21D04E8-L000310](../../tests/test_generation_capabilities.py#L310) | 310 | `""` | — |
| [SRC-AAA21D04E8-L000311](../../tests/test_generation_capabilities.py#L311) | 311 | `"    assert answer == \"إجابة مكتملة من النموذج الاحتياطي\""` | — |
| [SRC-AAA21D04E8-L000312](../../tests/test_generation_capabilities.py#L312) | 312 | `"    assert calls == [\"primary/model\", \"backup/model\"]"` | — |
| [SRC-AAA21D04E8-L000313](../../tests/test_generation_capabilities.py#L313) | 313 | `"    assert agent.generation_diagnostics[0][\"status\"] == \"rate_limited\""` | — |
| [SRC-AAA21D04E8-L000314](../../tests/test_generation_capabilities.py#L314) | 314 | `"    assert agent.generation_diagnostics[0][\"http_status_code\"] == 429"` | — |
| [SRC-AAA21D04E8-L000315](../../tests/test_generation_capabilities.py#L315) | 315 | `"    assert agent.generation_diagnostics[0][\"fallback_used\"] is False"` | — |
| [SRC-AAA21D04E8-L000316](../../tests/test_generation_capabilities.py#L316) | 316 | `"    assert agent.generation_diagnostics[1][\"status\"] == \"accepted\""` | — |
| [SRC-AAA21D04E8-L000317](../../tests/test_generation_capabilities.py#L317) | 317 | `"    assert agent.generation_diagnostics[1][\"fallback_used\"] is True"` | — |
| [SRC-AAA21D04E8-L000318](../../tests/test_generation_capabilities.py#L318) | 318 | `""` | — |
| [SRC-AAA21D04E8-L000319](../../tests/test_generation_capabilities.py#L319) | 319 | `""` | — |
| [SRC-AAA21D04E8-L000320](../../tests/test_generation_capabilities.py#L320) | 320 | `"def test_model_http_429_from_all_models_is_bounded_and_redacted(monkeypatch):"` | — |
| [SRC-AAA21D04E8-L000321](../../tests/test_generation_capabilities.py#L321) | 321 | `"    from urllib.error import HTTPError"` | — |
| [SRC-AAA21D04E8-L000322](../../tests/test_generation_capabilities.py#L322) | 322 | `""` | — |
| [SRC-AAA21D04E8-L000323](../../tests/test_generation_capabilities.py#L323) | 323 | `"    agent = WebAgent()"` | — |
| [SRC-AAA21D04E8-L000324](../../tests/test_generation_capabilities.py#L324) | 324 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-AAA21D04E8-L000325](../../tests/test_generation_capabilities.py#L325) | 325 | `"    agent.fallback_model = \"backup/model\""` | — |
| [SRC-AAA21D04E8-L000326](../../tests/test_generation_capabilities.py#L326) | 326 | `"    calls: list[str] = []"` | — |
| [SRC-AAA21D04E8-L000327](../../tests/test_generation_capabilities.py#L327) | 327 | `""` | — |
| [SRC-AAA21D04E8-L000328](../../tests/test_generation_capabilities.py#L328) | 328 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-AAA21D04E8-L000329](../../tests/test_generation_capabilities.py#L329) | 329 | `"        model = json.loads(request.data.decode(\"utf-8\"))[\"model\"]"` | — |
| [SRC-AAA21D04E8-L000330](../../tests/test_generation_capabilities.py#L330) | 330 | `"        calls.append(model)"` | — |
| [SRC-AAA21D04E8-L000331](../../tests/test_generation_capabilities.py#L331) | 331 | `"        raise HTTPError(request.full_url, 429, \"private provider detail\", None, None)"` | — |
| [SRC-AAA21D04E8-L000332](../../tests/test_generation_capabilities.py#L332) | 332 | `""` | — |
| [SRC-AAA21D04E8-L000333](../../tests/test_generation_capabilities.py#L333) | 333 | `"    monkeypatch.setattr(\"agents.web_agent._open_model_request\", fake_urlopen)"` | — |
| [SRC-AAA21D04E8-L000334](../../tests/test_generation_capabilities.py#L334) | 334 | `"    with pytest.raises(RuntimeError, match=\"HTTP 429\"):"` | — |
| [SRC-AAA21D04E8-L000335](../../tests/test_generation_capabilities.py#L335) | 335 | `"        agent._request_completion("` | — |
| [SRC-AAA21D04E8-L000336](../../tests/test_generation_capabilities.py#L336) | 336 | `"            [{\"role\": \"user\", \"content\": \"اختبار\"}], model=\"primary/model\""` | — |
| [SRC-AAA21D04E8-L000337](../../tests/test_generation_capabilities.py#L337) | 337 | `"        )"` | — |
| [SRC-AAA21D04E8-L000338](../../tests/test_generation_capabilities.py#L338) | 338 | `""` | — |
| [SRC-AAA21D04E8-L000339](../../tests/test_generation_capabilities.py#L339) | 339 | `"    assert calls == [\"primary/model\", \"backup/model\"]"` | — |
| [SRC-AAA21D04E8-L000340](../../tests/test_generation_capabilities.py#L340) | 340 | `"    assert [row[\"status\"] for row in agent.generation_diagnostics] == ["` | — |
| [SRC-AAA21D04E8-L000341](../../tests/test_generation_capabilities.py#L341) | 341 | `"        \"rate_limited\", \"rate_limited\""` | — |
| [SRC-AAA21D04E8-L000342](../../tests/test_generation_capabilities.py#L342) | 342 | `"    ]"` | — |
| [SRC-AAA21D04E8-L000343](../../tests/test_generation_capabilities.py#L343) | 343 | `"    assert [row[\"http_status_code\"] for row in agent.generation_diagnostics] == [429, 429]"` | — |
| [SRC-AAA21D04E8-L000344](../../tests/test_generation_capabilities.py#L344) | 344 | `"    assert \"private provider detail\" not in repr(agent.generation_diagnostics)"` | — |
| [SRC-AAA21D04E8-L000345](../../tests/test_generation_capabilities.py#L345) | 345 | `""` | — |
| [SRC-AAA21D04E8-L000346](../../tests/test_generation_capabilities.py#L346) | 346 | `""` | — |
| [SRC-AAA21D04E8-L000347](../../tests/test_generation_capabilities.py#L347) | 347 | `"@pytest.mark.parametrize(\"status_code\", [401, 403])"` | — |
| [SRC-AAA21D04E8-L000348](../../tests/test_generation_capabilities.py#L348) | 348 | `"def test_model_auth_http_errors_are_classified_and_fallback_is_bounded("` | — |
| [SRC-AAA21D04E8-L000349](../../tests/test_generation_capabilities.py#L349) | 349 | `"    monkeypatch, status_code"` | — |
| [SRC-AAA21D04E8-L000350](../../tests/test_generation_capabilities.py#L350) | 350 | `"):"` | — |
| [SRC-AAA21D04E8-L000351](../../tests/test_generation_capabilities.py#L351) | 351 | `"    from urllib.error import HTTPError"` | — |
| [SRC-AAA21D04E8-L000352](../../tests/test_generation_capabilities.py#L352) | 352 | `""` | — |
| [SRC-AAA21D04E8-L000353](../../tests/test_generation_capabilities.py#L353) | 353 | `"    agent = WebAgent()"` | — |
| [SRC-AAA21D04E8-L000354](../../tests/test_generation_capabilities.py#L354) | 354 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-AAA21D04E8-L000355](../../tests/test_generation_capabilities.py#L355) | 355 | `"    agent.fallback_model = \"backup/model\""` | — |
| [SRC-AAA21D04E8-L000356](../../tests/test_generation_capabilities.py#L356) | 356 | `"    calls: list[str] = []"` | — |
| [SRC-AAA21D04E8-L000357](../../tests/test_generation_capabilities.py#L357) | 357 | `""` | — |
| [SRC-AAA21D04E8-L000358](../../tests/test_generation_capabilities.py#L358) | 358 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-AAA21D04E8-L000359](../../tests/test_generation_capabilities.py#L359) | 359 | `"        model = json.loads(request.data.decode(\"utf-8\"))[\"model\"]"` | — |
| [SRC-AAA21D04E8-L000360](../../tests/test_generation_capabilities.py#L360) | 360 | `"        calls.append(model)"` | — |
| [SRC-AAA21D04E8-L000361](../../tests/test_generation_capabilities.py#L361) | 361 | `"        raise HTTPError(request.full_url, status_code, \"private auth detail\", None, None)"` | — |
| [SRC-AAA21D04E8-L000362](../../tests/test_generation_capabilities.py#L362) | 362 | `""` | — |
| [SRC-AAA21D04E8-L000363](../../tests/test_generation_capabilities.py#L363) | 363 | `"    monkeypatch.setattr(\"agents.web_agent._open_model_request\", fake_urlopen)"` | — |
| [SRC-AAA21D04E8-L000364](../../tests/test_generation_capabilities.py#L364) | 364 | `"    with pytest.raises(RuntimeError, match=f\"HTTP {status_code}\"):"` | — |
| [SRC-AAA21D04E8-L000365](../../tests/test_generation_capabilities.py#L365) | 365 | `"        agent._request_completion("` | — |
| [SRC-AAA21D04E8-L000366](../../tests/test_generation_capabilities.py#L366) | 366 | `"            [{\"role\": \"user\", \"content\": \"اختبار\"}], model=\"primary/model\""` | — |
| [SRC-AAA21D04E8-L000367](../../tests/test_generation_capabilities.py#L367) | 367 | `"        )"` | — |
| [SRC-AAA21D04E8-L000368](../../tests/test_generation_capabilities.py#L368) | 368 | `""` | — |
| [SRC-AAA21D04E8-L000369](../../tests/test_generation_capabilities.py#L369) | 369 | `"    assert calls == [\"primary/model\", \"backup/model\"]"` | — |
| [SRC-AAA21D04E8-L000370](../../tests/test_generation_capabilities.py#L370) | 370 | `"    assert [row[\"status\"] for row in agent.generation_diagnostics] == ["` | — |
| [SRC-AAA21D04E8-L000371](../../tests/test_generation_capabilities.py#L371) | 371 | `"        \"unauthorized\", \"unauthorized\""` | — |
| [SRC-AAA21D04E8-L000372](../../tests/test_generation_capabilities.py#L372) | 372 | `"    ]"` | — |
| [SRC-AAA21D04E8-L000373](../../tests/test_generation_capabilities.py#L373) | 373 | `"    assert [row[\"http_status_code\"] for row in agent.generation_diagnostics] == ["` | — |
| [SRC-AAA21D04E8-L000374](../../tests/test_generation_capabilities.py#L374) | 374 | `"        status_code, status_code"` | — |
| [SRC-AAA21D04E8-L000375](../../tests/test_generation_capabilities.py#L375) | 375 | `"    ]"` | — |
| [SRC-AAA21D04E8-L000376](../../tests/test_generation_capabilities.py#L376) | 376 | `"    assert \"private auth detail\" not in repr(agent.generation_diagnostics)"` | — |
| [SRC-AAA21D04E8-L000377](../../tests/test_generation_capabilities.py#L377) | 377 | `""` | — |
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
| [SRC-1A176AD4F0-L000030](../../tests/test_hosted_smoke.py#L30) | 30 | `"        if self.path == \"/\":"` | — |
| [SRC-1A176AD4F0-L000031](../../tests/test_hosted_smoke.py#L31) | 31 | `"            self.respond(200, {\"page\": \"dashboard\"})"` | — |
| [SRC-1A176AD4F0-L000032](../../tests/test_hosted_smoke.py#L32) | 32 | `"        elif self.path == \"/api/health\":"` | — |
| [SRC-1A176AD4F0-L000033](../../tests/test_hosted_smoke.py#L33) | 33 | `"            self.respond(200, {\"ok\": True, \"app\": \"Omarai\", \"agent\": {}})"` | — |
| [SRC-1A176AD4F0-L000034](../../tests/test_hosted_smoke.py#L34) | 34 | `"        else:"` | — |
| [SRC-1A176AD4F0-L000035](../../tests/test_hosted_smoke.py#L35) | 35 | `"            self.respond(404, {\"error\": \"not found\"})"` | — |
| [SRC-1A176AD4F0-L000036](../../tests/test_hosted_smoke.py#L36) | 36 | `""` | — |
| [SRC-1A176AD4F0-L000037](../../tests/test_hosted_smoke.py#L37) | 37 | `"    def do_POST(self) -> None:"` | — |
| [SRC-1A176AD4F0-L000038](../../tests/test_hosted_smoke.py#L38) | 38 | `"        if self.headers.get(\"Authorization\") != f\"Bearer {TOKEN}\":"` | — |
| [SRC-1A176AD4F0-L000039](../../tests/test_hosted_smoke.py#L39) | 39 | `"            self.respond(401, {\"error\": \"unauthorized\"})"` | — |
| [SRC-1A176AD4F0-L000040](../../tests/test_hosted_smoke.py#L40) | 40 | `"            return"` | — |
| [SRC-1A176AD4F0-L000041](../../tests/test_hosted_smoke.py#L41) | 41 | `"        length = int(self.headers.get(\"Content-Length\", \"0\"))"` | — |
| [SRC-1A176AD4F0-L000042](../../tests/test_hosted_smoke.py#L42) | 42 | `"        self.rfile.read(length)"` | — |
| [SRC-1A176AD4F0-L000043](../../tests/test_hosted_smoke.py#L43) | 43 | `"        if self.path == \"/api/diagnostics\":"` | — |
| [SRC-1A176AD4F0-L000044](../../tests/test_hosted_smoke.py#L44) | 44 | `"            self.respond(200, {"` | — |
| [SRC-1A176AD4F0-L000045](../../tests/test_hosted_smoke.py#L45) | 45 | `"                \"overall_status\": \"passed\","` | — |
| [SRC-1A176AD4F0-L000046](../../tests/test_hosted_smoke.py#L46) | 46 | `"                \"checks\": {"` | — |
| [SRC-1A176AD4F0-L000047](../../tests/test_hosted_smoke.py#L47) | 47 | `"                    \"web_search\": {"` | — |
| [SRC-1A176AD4F0-L000048](../../tests/test_hosted_smoke.py#L48) | 48 | `"                        \"status\": \"passed\", \"result_count\": 2,"` | — |
| [SRC-1A176AD4F0-L000049](../../tests/test_hosted_smoke.py#L49) | 49 | `"                        \"provider_counts\": {\"bing_rss\": 1, \"duckduckgo_html\": 1},"` | — |
| [SRC-1A176AD4F0-L000050](../../tests/test_hosted_smoke.py#L50) | 50 | `"                    },"` | — |
| [SRC-1A176AD4F0-L000051](../../tests/test_hosted_smoke.py#L51) | 51 | `"                    \"language_model\": {\"status\": \"passed\", \"response_received\": True},"` | — |
| [SRC-1A176AD4F0-L000052](../../tests/test_hosted_smoke.py#L52) | 52 | `"                    \"social_search\": {\"status\": \"skipped\"},"` | — |
| [SRC-1A176AD4F0-L000053](../../tests/test_hosted_smoke.py#L53) | 53 | `"                },"` | — |
| [SRC-1A176AD4F0-L000054](../../tests/test_hosted_smoke.py#L54) | 54 | `"            })"` | — |
| [SRC-1A176AD4F0-L000055](../../tests/test_hosted_smoke.py#L55) | 55 | `"        elif self.path == \"/api/agent\":"` | — |
| [SRC-1A176AD4F0-L000056](../../tests/test_hosted_smoke.py#L56) | 56 | `"            self.respond(200, {"` | — |
| [SRC-1A176AD4F0-L000057](../../tests/test_hosted_smoke.py#L57) | 57 | `"                \"answer\": \"القاهرة هي عاصمة مصر. [المصدر 1]\","` | — |
| [SRC-1A176AD4F0-L000058](../../tests/test_hosted_smoke.py#L58) | 58 | `"                \"used_web_search\": True,"` | — |
| [SRC-1A176AD4F0-L000059](../../tests/test_hosted_smoke.py#L59) | 59 | `"                \"used_language_model\": True,"` | — |
| [SRC-1A176AD4F0-L000060](../../tests/test_hosted_smoke.py#L60) | 60 | `"                \"sources\": [{\"title\": \"مصدر اختبار\", \"url\": \"https://example.com/source\"}],"` | — |
| [SRC-1A176AD4F0-L000061](../../tests/test_hosted_smoke.py#L61) | 61 | `"                \"answer_evidence_status\": \"citation_indices_validated_only\","` | — |
| [SRC-1A176AD4F0-L000062](../../tests/test_hosted_smoke.py#L62) | 62 | `"                \"request_budget\": {\"profile\": \"hosted_smoke\", \"timeout_seconds\": 75, \"budget_exhausted\": False, \"deadline_exceeded\": False, \"limits\": {\"search_queries\": 3, \"search_calls\": 12, \"model_calls\": 6, \"page_fetches\": 4, \"tool_calls\": 0}, \"counts\": {\"search_queries\": 2, \"search_calls\": 4, \"model_calls\": 4, \"page_fetches\": 1, \"tool_calls\": 0}},"` | — |
| [SRC-1A176AD4F0-L000063](../../tests/test_hosted_smoke.py#L63) | 63 | `"                \"search_report\": {"` | — |
| [SRC-1A176AD4F0-L000064](../../tests/test_hosted_smoke.py#L64) | 64 | `"                    \"providers_used\": [\"bing_rss\"], \"pages_fetched\": 1,"` | — |
| [SRC-1A176AD4F0-L000065](../../tests/test_hosted_smoke.py#L65) | 65 | `"                    \"pipeline_completion_status\": \"completed\","` | — |
| [SRC-1A176AD4F0-L000066](../../tests/test_hosted_smoke.py#L66) | 66 | `"                    \"semantic_claim_verification\": {\"status\": \"completed_all_claims_supported\"},"` | — |
| [SRC-1A176AD4F0-L000067](../../tests/test_hosted_smoke.py#L67) | 67 | `"                    \"insufficient_evidence\": False,"` | — |
| [SRC-1A176AD4F0-L000068](../../tests/test_hosted_smoke.py#L68) | 68 | `"                    \"claim_audit_semantics\": \"distinct_model_assessed_source_support_not_ground_truth\","` | — |
| [SRC-1A176AD4F0-L000069](../../tests/test_hosted_smoke.py#L69) | 69 | `"                },"` | — |
| [SRC-1A176AD4F0-L000070](../../tests/test_hosted_smoke.py#L70) | 70 | `"            })"` | — |
| [SRC-1A176AD4F0-L000071](../../tests/test_hosted_smoke.py#L71) | 71 | `"        else:"` | — |
| [SRC-1A176AD4F0-L000072](../../tests/test_hosted_smoke.py#L72) | 72 | `"            self.respond(404, {\"error\": \"not found\"})"` | — |
| [SRC-1A176AD4F0-L000073](../../tests/test_hosted_smoke.py#L73) | 73 | `""` | — |
| [SRC-1A176AD4F0-L000074](../../tests/test_hosted_smoke.py#L74) | 74 | `""` | — |
| [SRC-1A176AD4F0-L000075](../../tests/test_hosted_smoke.py#L75) | 75 | `"@pytest.fixture"` | — |
| [SRC-1A176AD4F0-L000076](../../tests/test_hosted_smoke.py#L76) | 76 | `"def hosted_server():"` | — |
| [SRC-1A176AD4F0-L000077](../../tests/test_hosted_smoke.py#L77) | 77 | `"    server = ThreadingHTTPServer((\"127.0.0.1\", 0), Handler)"` | — |
| [SRC-1A176AD4F0-L000078](../../tests/test_hosted_smoke.py#L78) | 78 | `"    thread = threading.Thread(target=server.serve_forever, daemon=True)"` | — |
| [SRC-1A176AD4F0-L000079](../../tests/test_hosted_smoke.py#L79) | 79 | `"    thread.start()"` | — |
| [SRC-1A176AD4F0-L000080](../../tests/test_hosted_smoke.py#L80) | 80 | `"    try:"` | — |
| [SRC-1A176AD4F0-L000081](../../tests/test_hosted_smoke.py#L81) | 81 | `"        yield f\"http://127.0.0.1:{server.server_port}\""` | — |
| [SRC-1A176AD4F0-L000082](../../tests/test_hosted_smoke.py#L82) | 82 | `"    finally:"` | — |
| [SRC-1A176AD4F0-L000083](../../tests/test_hosted_smoke.py#L83) | 83 | `"        server.shutdown()"` | — |
| [SRC-1A176AD4F0-L000084](../../tests/test_hosted_smoke.py#L84) | 84 | `"        server.server_close()"` | — |
| [SRC-1A176AD4F0-L000085](../../tests/test_hosted_smoke.py#L85) | 85 | `"        thread.join(timeout=2)"` | — |
| [SRC-1A176AD4F0-L000086](../../tests/test_hosted_smoke.py#L86) | 86 | `""` | — |
| [SRC-1A176AD4F0-L000087](../../tests/test_hosted_smoke.py#L87) | 87 | `""` | — |
| [SRC-1A176AD4F0-L000088](../../tests/test_hosted_smoke.py#L88) | 88 | `"def test_normalize_origin_requires_https_and_rejects_credentials_or_paths():"` | — |
| [SRC-1A176AD4F0-L000089](../../tests/test_hosted_smoke.py#L89) | 89 | `"    assert normalize_origin(\"https://example.com/\") == \"https://example.com\""` | — |
| [SRC-1A176AD4F0-L000090](../../tests/test_hosted_smoke.py#L90) | 90 | `"    for invalid in ("` | — |
| [SRC-1A176AD4F0-L000091](../../tests/test_hosted_smoke.py#L91) | 91 | `"        \"http://example.com\","` | — |
| [SRC-1A176AD4F0-L000092](../../tests/test_hosted_smoke.py#L92) | 92 | `"        \"https://user:password@example.com\","` | — |
| [SRC-1A176AD4F0-L000093](../../tests/test_hosted_smoke.py#L93) | 93 | `"        \"https://example.com/path\","` | — |
| [SRC-1A176AD4F0-L000094](../../tests/test_hosted_smoke.py#L94) | 94 | `"        \"https://example.com/?token=secret\","` | — |
| [SRC-1A176AD4F0-L000095](../../tests/test_hosted_smoke.py#L95) | 95 | `"    ):"` | — |
| [SRC-1A176AD4F0-L000096](../../tests/test_hosted_smoke.py#L96) | 96 | `"        with pytest.raises(SmokeError):"` | — |
| [SRC-1A176AD4F0-L000097](../../tests/test_hosted_smoke.py#L97) | 97 | `"            normalize_origin(invalid)"` | — |
| [SRC-1A176AD4F0-L000098](../../tests/test_hosted_smoke.py#L98) | 98 | `""` | — |
| [SRC-1A176AD4F0-L000099](../../tests/test_hosted_smoke.py#L99) | 99 | `""` | — |
| [SRC-1A176AD4F0-L000100](../../tests/test_hosted_smoke.py#L100) | 100 | `"def test_normalize_origin_allows_plain_http_only_for_local_test():"` | — |
| [SRC-1A176AD4F0-L000101](../../tests/test_hosted_smoke.py#L101) | 101 | `"    assert normalize_origin(\"http://127.0.0.1:8765\", allow_http=True) == ("` | — |
| [SRC-1A176AD4F0-L000102](../../tests/test_hosted_smoke.py#L102) | 102 | `"        \"http://127.0.0.1:8765\""` | — |
| [SRC-1A176AD4F0-L000103](../../tests/test_hosted_smoke.py#L103) | 103 | `"    )"` | — |
| [SRC-1A176AD4F0-L000104](../../tests/test_hosted_smoke.py#L104) | 104 | `"    with pytest.raises(SmokeError):"` | — |
| [SRC-1A176AD4F0-L000105](../../tests/test_hosted_smoke.py#L105) | 105 | `"        normalize_origin(\"http://example.com\", allow_http=True)"` | — |
| [SRC-1A176AD4F0-L000106](../../tests/test_hosted_smoke.py#L106) | 106 | `""` | — |
| [SRC-1A176AD4F0-L000107](../../tests/test_hosted_smoke.py#L107) | 107 | `""` | — |
| [SRC-1A176AD4F0-L000108](../../tests/test_hosted_smoke.py#L108) | 108 | `"def test_smoke_checks_health_auth_and_single_agent_search(hosted_server):"` | — |
| [SRC-1A176AD4F0-L000109](../../tests/test_hosted_smoke.py#L109) | 109 | `"    result = run_smoke("` | — |
| [SRC-1A176AD4F0-L000110](../../tests/test_hosted_smoke.py#L110) | 110 | `"        hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5"` | — |
| [SRC-1A176AD4F0-L000111](../../tests/test_hosted_smoke.py#L111) | 111 | `"    )"` | — |
| [SRC-1A176AD4F0-L000112](../../tests/test_hosted_smoke.py#L112) | 112 | `"    assert result[\"result\"] == \"passed\""` | — |
| [SRC-1A176AD4F0-L000113](../../tests/test_hosted_smoke.py#L113) | 113 | `"    assert result[\"checks\"][\"health\"] == \"passed\""` | — |
| [SRC-1A176AD4F0-L000114](../../tests/test_hosted_smoke.py#L114) | 114 | `"    assert result[\"checks\"][\"authentication\"] == \"passed\""` | — |
| [SRC-1A176AD4F0-L000115](../../tests/test_hosted_smoke.py#L115) | 115 | `"    assert result[\"checks\"][\"search\"][\"providers_reported\"] == [\"bing_rss\"]"` | — |
| [SRC-1A176AD4F0-L000116](../../tests/test_hosted_smoke.py#L116) | 116 | `"    assert result[\"checks\"][\"agent_request\"][\"source_count\"] == 1"` | — |
| [SRC-1A176AD4F0-L000117](../../tests/test_hosted_smoke.py#L117) | 117 | `"    assert result[\"checks\"][\"agent_request\"][\"pipeline_completion_status\"] == \"completed\""` | — |
| [SRC-1A176AD4F0-L000118](../../tests/test_hosted_smoke.py#L118) | 118 | `""` | — |
| [SRC-1A176AD4F0-L000119](../../tests/test_hosted_smoke.py#L119) | 119 | `""` | — |
| [SRC-1A176AD4F0-L000120](../../tests/test_hosted_smoke.py#L120) | 120 | `"def test_smoke_never_forwards_bearer_to_cross_origin_redirect():"` | — |
| [SRC-1A176AD4F0-L000121](../../tests/test_hosted_smoke.py#L121) | 121 | `"    received_authorizations = []"` | — |
| [SRC-1A176AD4F0-L000122](../../tests/test_hosted_smoke.py#L122) | 122 | `""` | — |
| [SRC-1A176AD4F0-L000123](../../tests/test_hosted_smoke.py#L123) | 123 | `"    class RedirectHandler(BaseHTTPRequestHandler):"` | — |
| [SRC-1A176AD4F0-L000124](../../tests/test_hosted_smoke.py#L124) | 124 | `"        def log_message(self, format: str, *args: object) -> None:"` | — |
| [SRC-1A176AD4F0-L000125](../../tests/test_hosted_smoke.py#L125) | 125 | `"            return"` | — |
| [SRC-1A176AD4F0-L000126](../../tests/test_hosted_smoke.py#L126) | 126 | `""` | — |
| [SRC-1A176AD4F0-L000127](../../tests/test_hosted_smoke.py#L127) | 127 | `"        def do_GET(self) -> None:"` | — |
| [SRC-1A176AD4F0-L000128](../../tests/test_hosted_smoke.py#L128) | 128 | `"            self.send_response(302)"` | — |
| [SRC-1A176AD4F0-L000129](../../tests/test_hosted_smoke.py#L129) | 129 | `"            self.send_header(\"Location\", self.server.redirect_destination)"` | — |
| [SRC-1A176AD4F0-L000130](../../tests/test_hosted_smoke.py#L130) | 130 | `"            self.send_header(\"Content-Length\", \"0\")"` | — |
| [SRC-1A176AD4F0-L000131](../../tests/test_hosted_smoke.py#L131) | 131 | `"            self.end_headers()"` | — |
| [SRC-1A176AD4F0-L000132](../../tests/test_hosted_smoke.py#L132) | 132 | `""` | — |
| [SRC-1A176AD4F0-L000133](../../tests/test_hosted_smoke.py#L133) | 133 | `"    class DestinationHandler(BaseHTTPRequestHandler):"` | — |
| [SRC-1A176AD4F0-L000134](../../tests/test_hosted_smoke.py#L134) | 134 | `"        def log_message(self, format: str, *args: object) -> None:"` | — |
| [SRC-1A176AD4F0-L000135](../../tests/test_hosted_smoke.py#L135) | 135 | `"            return"` | — |
| [SRC-1A176AD4F0-L000136](../../tests/test_hosted_smoke.py#L136) | 136 | `""` | — |
| [SRC-1A176AD4F0-L000137](../../tests/test_hosted_smoke.py#L137) | 137 | `"        def do_GET(self) -> None:"` | — |
| [SRC-1A176AD4F0-L000138](../../tests/test_hosted_smoke.py#L138) | 138 | `"            received_authorizations.append(self.headers.get(\"Authorization\"))"` | — |
| [SRC-1A176AD4F0-L000139](../../tests/test_hosted_smoke.py#L139) | 139 | `"            self.send_response(200)"` | — |
| [SRC-1A176AD4F0-L000140](../../tests/test_hosted_smoke.py#L140) | 140 | `"            self.send_header(\"Content-Length\", \"0\")"` | — |
| [SRC-1A176AD4F0-L000141](../../tests/test_hosted_smoke.py#L141) | 141 | `"            self.end_headers()"` | — |
| [SRC-1A176AD4F0-L000142](../../tests/test_hosted_smoke.py#L142) | 142 | `""` | — |
| [SRC-1A176AD4F0-L000143](../../tests/test_hosted_smoke.py#L143) | 143 | `"    destination = ThreadingHTTPServer((\"127.0.0.1\", 0), DestinationHandler)"` | — |
| [SRC-1A176AD4F0-L000144](../../tests/test_hosted_smoke.py#L144) | 144 | `"    source = ThreadingHTTPServer((\"127.0.0.1\", 0), RedirectHandler)"` | — |
| [SRC-1A176AD4F0-L000145](../../tests/test_hosted_smoke.py#L145) | 145 | `"    destination_thread = threading.Thread(target=destination.serve_forever, daemon=True)"` | — |
| [SRC-1A176AD4F0-L000146](../../tests/test_hosted_smoke.py#L146) | 146 | `"    source_thread = threading.Thread(target=source.serve_forever, daemon=True)"` | — |
| [SRC-1A176AD4F0-L000147](../../tests/test_hosted_smoke.py#L147) | 147 | `"    source.redirect_destination = ("` | — |
| [SRC-1A176AD4F0-L000148](../../tests/test_hosted_smoke.py#L148) | 148 | `"        f\"http://127.0.0.1:{destination.server_port}/capture\""` | — |
| [SRC-1A176AD4F0-L000149](../../tests/test_hosted_smoke.py#L149) | 149 | `"    )"` | — |
| [SRC-1A176AD4F0-L000150](../../tests/test_hosted_smoke.py#L150) | 150 | `"    destination_thread.start()"` | — |
| [SRC-1A176AD4F0-L000151](../../tests/test_hosted_smoke.py#L151) | 151 | `"    source_thread.start()"` | — |
| [SRC-1A176AD4F0-L000152](../../tests/test_hosted_smoke.py#L152) | 152 | `"    try:"` | — |
| [SRC-1A176AD4F0-L000153](../../tests/test_hosted_smoke.py#L153) | 153 | `"        status, payload = hosted_smoke_test.request_json("` | — |
| [SRC-1A176AD4F0-L000154](../../tests/test_hosted_smoke.py#L154) | 154 | `"            f\"http://127.0.0.1:{source.server_port}/redirect\","` | — |
| [SRC-1A176AD4F0-L000155](../../tests/test_hosted_smoke.py#L155) | 155 | `"            token=TOKEN,"` | — |
| [SRC-1A176AD4F0-L000156](../../tests/test_hosted_smoke.py#L156) | 156 | `"            timeout=3,"` | — |
| [SRC-1A176AD4F0-L000157](../../tests/test_hosted_smoke.py#L157) | 157 | `"        )"` | — |
| [SRC-1A176AD4F0-L000158](../../tests/test_hosted_smoke.py#L158) | 158 | `"        assert status == 302"` | — |
| [SRC-1A176AD4F0-L000159](../../tests/test_hosted_smoke.py#L159) | 159 | `"        assert payload is None"` | — |
| [SRC-1A176AD4F0-L000160](../../tests/test_hosted_smoke.py#L160) | 160 | `"        assert received_authorizations == []"` | — |
| [SRC-1A176AD4F0-L000161](../../tests/test_hosted_smoke.py#L161) | 161 | `"    finally:"` | — |
| [SRC-1A176AD4F0-L000162](../../tests/test_hosted_smoke.py#L162) | 162 | `"        source.shutdown()"` | — |
| [SRC-1A176AD4F0-L000163](../../tests/test_hosted_smoke.py#L163) | 163 | `"        destination.shutdown()"` | — |
| [SRC-1A176AD4F0-L000164](../../tests/test_hosted_smoke.py#L164) | 164 | `"        source.server_close()"` | — |
| [SRC-1A176AD4F0-L000165](../../tests/test_hosted_smoke.py#L165) | 165 | `"        destination.server_close()"` | — |
| [SRC-1A176AD4F0-L000166](../../tests/test_hosted_smoke.py#L166) | 166 | `"        source_thread.join(timeout=2)"` | — |
| [SRC-1A176AD4F0-L000167](../../tests/test_hosted_smoke.py#L167) | 167 | `"        destination_thread.join(timeout=2)"` | — |
| [SRC-1A176AD4F0-L000168](../../tests/test_hosted_smoke.py#L168) | 168 | `""` | — |
| [SRC-1A176AD4F0-L000169](../../tests/test_hosted_smoke.py#L169) | 169 | `""` | — |
| [SRC-1A176AD4F0-L000170](../../tests/test_hosted_smoke.py#L170) | 170 | `"def test_smoke_refuses_missing_or_short_access_token(hosted_server):"` | — |
| [SRC-1A176AD4F0-L000171](../../tests/test_hosted_smoke.py#L171) | 171 | `"    with pytest.raises(SmokeError, match=\"OMARAI_ACCESS_TOKEN\"):"` | — |
| [SRC-1A176AD4F0-L000172](../../tests/test_hosted_smoke.py#L172) | 172 | `"        run_smoke(hosted_server, \"\", allow_http=True, allow_provider_usage=True, timeout=5)"` | — |
| [SRC-1A176AD4F0-L000173](../../tests/test_hosted_smoke.py#L173) | 173 | `""` | — |
| [SRC-1A176AD4F0-L000174](../../tests/test_hosted_smoke.py#L174) | 174 | `""` | — |
| [SRC-1A176AD4F0-L000175](../../tests/test_hosted_smoke.py#L175) | 175 | `"def test_smoke_fails_when_agent_returns_no_live_source(hosted_server, monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000176](../../tests/test_hosted_smoke.py#L176) | 176 | `"    original = hosted_smoke_test.request_json"` | — |
| [SRC-1A176AD4F0-L000177](../../tests/test_hosted_smoke.py#L177) | 177 | `""` | — |
| [SRC-1A176AD4F0-L000178](../../tests/test_hosted_smoke.py#L178) | 178 | `"    def without_sources(url: str, **kwargs):"` | — |
| [SRC-1A176AD4F0-L000179](../../tests/test_hosted_smoke.py#L179) | 179 | `"        if urlsplit(url).path == \"/api/agent\" and kwargs.get(\"token\") == TOKEN:"` | — |
| [SRC-1A176AD4F0-L000180](../../tests/test_hosted_smoke.py#L180) | 180 | `"            return 200, {"` | — |
| [SRC-1A176AD4F0-L000181](../../tests/test_hosted_smoke.py#L181) | 181 | `"                \"answer\": \"إجابة بلا مصادر\", \"used_web_search\": False,"` | — |
| [SRC-1A176AD4F0-L000182](../../tests/test_hosted_smoke.py#L182) | 182 | `"                \"used_language_model\": True, \"sources\": [],"` | — |
| [SRC-1A176AD4F0-L000183](../../tests/test_hosted_smoke.py#L183) | 183 | `"            }"` | — |
| [SRC-1A176AD4F0-L000184](../../tests/test_hosted_smoke.py#L184) | 184 | `"        return original(url, **kwargs)"` | — |
| [SRC-1A176AD4F0-L000185](../../tests/test_hosted_smoke.py#L185) | 185 | `""` | — |
| [SRC-1A176AD4F0-L000186](../../tests/test_hosted_smoke.py#L186) | 186 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", without_sources)"` | — |
| [SRC-1A176AD4F0-L000187](../../tests/test_hosted_smoke.py#L187) | 187 | `"    with pytest.raises(SmokeError, match=\"usable source URLs\") as failure:"` | — |
| [SRC-1A176AD4F0-L000188](../../tests/test_hosted_smoke.py#L188) | 188 | `"        run_smoke(hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5)"` | — |
| [SRC-1A176AD4F0-L000189](../../tests/test_hosted_smoke.py#L189) | 189 | `"    assert failure.value.report[\"transcript\"][0][\"question\"] == ("` | — |
| [SRC-1A176AD4F0-L000190](../../tests/test_hosted_smoke.py#L190) | 190 | `"        hosted_smoke_test.LIVE_TEST_QUESTION"` | — |
| [SRC-1A176AD4F0-L000191](../../tests/test_hosted_smoke.py#L191) | 191 | `"    )"` | — |
| [SRC-1A176AD4F0-L000192](../../tests/test_hosted_smoke.py#L192) | 192 | `"    assert failure.value.report[\"transcript\"][0][\"answer\"] == \"إجابة بلا مصادر\""` | — |
| [SRC-1A176AD4F0-L000193](../../tests/test_hosted_smoke.py#L193) | 193 | `""` | — |
| [SRC-1A176AD4F0-L000194](../../tests/test_hosted_smoke.py#L194) | 194 | `""` | — |
| [SRC-1A176AD4F0-L000195](../../tests/test_hosted_smoke.py#L195) | 195 | `"def test_smoke_rejects_invalid_expected_source_sha(hosted_server):"` | — |
| [SRC-1A176AD4F0-L000196](../../tests/test_hosted_smoke.py#L196) | 196 | `"    with pytest.raises(SmokeError, match=\"40-character Git SHA\"):"` | — |
| [SRC-1A176AD4F0-L000197](../../tests/test_hosted_smoke.py#L197) | 197 | `"        run_smoke("` | — |
| [SRC-1A176AD4F0-L000198](../../tests/test_hosted_smoke.py#L198) | 198 | `"            hosted_server, TOKEN, allow_http=True, timeout=5, expected_sha=\"main\""` | — |
| [SRC-1A176AD4F0-L000199](../../tests/test_hosted_smoke.py#L199) | 199 | `"        )"` | — |
| [SRC-1A176AD4F0-L000200](../../tests/test_hosted_smoke.py#L200) | 200 | `""` | — |
| [SRC-1A176AD4F0-L000201](../../tests/test_hosted_smoke.py#L201) | 201 | `""` | — |
| [SRC-1A176AD4F0-L000202](../../tests/test_hosted_smoke.py#L202) | 202 | `"def test_smoke_rejects_deployed_build_sha_mismatch(hosted_server):"` | — |
| [SRC-1A176AD4F0-L000203](../../tests/test_hosted_smoke.py#L203) | 203 | `"    with pytest.raises(SmokeError, match=\"does not match the expected Git commit\"):"` | — |
| [SRC-1A176AD4F0-L000204](../../tests/test_hosted_smoke.py#L204) | 204 | `"        run_smoke("` | — |
| [SRC-1A176AD4F0-L000205](../../tests/test_hosted_smoke.py#L205) | 205 | `"            hosted_server,"` | — |
| [SRC-1A176AD4F0-L000206](../../tests/test_hosted_smoke.py#L206) | 206 | `"            TOKEN,"` | — |
| [SRC-1A176AD4F0-L000207](../../tests/test_hosted_smoke.py#L207) | 207 | `"            allow_http=True,"` | — |
| [SRC-1A176AD4F0-L000208](../../tests/test_hosted_smoke.py#L208) | 208 | `"            allow_provider_usage=True,"` | — |
| [SRC-1A176AD4F0-L000209](../../tests/test_hosted_smoke.py#L209) | 209 | `"            timeout=5,"` | — |
| [SRC-1A176AD4F0-L000210](../../tests/test_hosted_smoke.py#L210) | 210 | `"            expected_sha=\"a\" * 40,"` | — |
| [SRC-1A176AD4F0-L000211](../../tests/test_hosted_smoke.py#L211) | 211 | `"        )"` | — |
| [SRC-1A176AD4F0-L000212](../../tests/test_hosted_smoke.py#L212) | 212 | `""` | — |
| [SRC-1A176AD4F0-L000213](../../tests/test_hosted_smoke.py#L213) | 213 | `""` | — |
| [SRC-1A176AD4F0-L000214](../../tests/test_hosted_smoke.py#L214) | 214 | `""` | — |
| [SRC-1A176AD4F0-L000215](../../tests/test_hosted_smoke.py#L215) | 215 | `"def test_http_403_report_contains_only_safe_response_metadata():"` | — |
| [SRC-1A176AD4F0-L000216](../../tests/test_hosted_smoke.py#L216) | 216 | `"    class ForbiddenHandler(BaseHTTPRequestHandler):"` | — |
| [SRC-1A176AD4F0-L000217](../../tests/test_hosted_smoke.py#L217) | 217 | `"        def log_message(self, format: str, *args: object) -> None:"` | — |
| [SRC-1A176AD4F0-L000218](../../tests/test_hosted_smoke.py#L218) | 218 | `"            return"` | — |
| [SRC-1A176AD4F0-L000219](../../tests/test_hosted_smoke.py#L219) | 219 | `""` | — |
| [SRC-1A176AD4F0-L000220](../../tests/test_hosted_smoke.py#L220) | 220 | `"        def do_GET(self) -> None:"` | — |
| [SRC-1A176AD4F0-L000221](../../tests/test_hosted_smoke.py#L221) | 221 | `"            body = b\"<html>blocked</html>\""` | — |
| [SRC-1A176AD4F0-L000222](../../tests/test_hosted_smoke.py#L222) | 222 | `"            self.send_response(403)"` | — |
| [SRC-1A176AD4F0-L000223](../../tests/test_hosted_smoke.py#L223) | 223 | `"            self.send_header(\"Content-Type\", \"text/html\")"` | — |
| [SRC-1A176AD4F0-L000224](../../tests/test_hosted_smoke.py#L224) | 224 | `"            self.send_header(\"X-Request-ID\", \"request-123\")"` | — |
| [SRC-1A176AD4F0-L000225](../../tests/test_hosted_smoke.py#L225) | 225 | `"            self.send_header(\"CF-Ray\", \"ray-456\")"` | — |
| [SRC-1A176AD4F0-L000226](../../tests/test_hosted_smoke.py#L226) | 226 | `"            self.send_header(\"Content-Length\", str(len(body)))"` | — |
| [SRC-1A176AD4F0-L000227](../../tests/test_hosted_smoke.py#L227) | 227 | `"            self.end_headers()"` | — |
| [SRC-1A176AD4F0-L000228](../../tests/test_hosted_smoke.py#L228) | 228 | `"            self.wfile.write(body)"` | — |
| [SRC-1A176AD4F0-L000229](../../tests/test_hosted_smoke.py#L229) | 229 | `""` | — |
| [SRC-1A176AD4F0-L000230](../../tests/test_hosted_smoke.py#L230) | 230 | `"    server = ThreadingHTTPServer((\"127.0.0.1\", 0), ForbiddenHandler)"` | — |
| [SRC-1A176AD4F0-L000231](../../tests/test_hosted_smoke.py#L231) | 231 | `"    thread = threading.Thread(target=server.serve_forever, daemon=True)"` | — |
| [SRC-1A176AD4F0-L000232](../../tests/test_hosted_smoke.py#L232) | 232 | `"    thread.start()"` | — |
| [SRC-1A176AD4F0-L000233](../../tests/test_hosted_smoke.py#L233) | 233 | `"    try:"` | — |
| [SRC-1A176AD4F0-L000234](../../tests/test_hosted_smoke.py#L234) | 234 | `"        status, payload = hosted_smoke_test.request_json("` | — |
| [SRC-1A176AD4F0-L000235](../../tests/test_hosted_smoke.py#L235) | 235 | `"            f\"http://127.0.0.1:{server.server_port}/api/health\","` | — |
| [SRC-1A176AD4F0-L000236](../../tests/test_hosted_smoke.py#L236) | 236 | `"            token=TOKEN,"` | — |
| [SRC-1A176AD4F0-L000237](../../tests/test_hosted_smoke.py#L237) | 237 | `"            timeout=3,"` | — |
| [SRC-1A176AD4F0-L000238](../../tests/test_hosted_smoke.py#L238) | 238 | `"        )"` | — |
| [SRC-1A176AD4F0-L000239](../../tests/test_hosted_smoke.py#L239) | 239 | `"        assert status == 403"` | — |
| [SRC-1A176AD4F0-L000240](../../tests/test_hosted_smoke.py#L240) | 240 | `"        assert payload[\"_smoke_http\"][\"status\"] == 403"` | — |
| [SRC-1A176AD4F0-L000241](../../tests/test_hosted_smoke.py#L241) | 241 | `"        assert payload[\"_smoke_http\"][\"request_id\"] == \"request-123\""` | — |
| [SRC-1A176AD4F0-L000242](../../tests/test_hosted_smoke.py#L242) | 242 | `"        assert payload[\"_smoke_http\"][\"cf_ray\"] == \"ray-456\""` | — |
| [SRC-1A176AD4F0-L000243](../../tests/test_hosted_smoke.py#L243) | 243 | `"        assert payload[\"_smoke_http\"][\"body_bytes_sampled\"] == len(b\"<html>blocked</html>\")"` | — |
| [SRC-1A176AD4F0-L000244](../../tests/test_hosted_smoke.py#L244) | 244 | `"        assert \"body_sha256\" in payload[\"_smoke_http\"]"` | — |
| [SRC-1A176AD4F0-L000245](../../tests/test_hosted_smoke.py#L245) | 245 | `"        assert \"blocked\" not in str(payload)"` | — |
| [SRC-1A176AD4F0-L000246](../../tests/test_hosted_smoke.py#L246) | 246 | `"        assert TOKEN not in str(payload)"` | — |
| [SRC-1A176AD4F0-L000247](../../tests/test_hosted_smoke.py#L247) | 247 | `"    finally:"` | — |
| [SRC-1A176AD4F0-L000248](../../tests/test_hosted_smoke.py#L248) | 248 | `"        server.shutdown()"` | — |
| [SRC-1A176AD4F0-L000249](../../tests/test_hosted_smoke.py#L249) | 249 | `"        server.server_close()"` | — |
| [SRC-1A176AD4F0-L000250](../../tests/test_hosted_smoke.py#L250) | 250 | `"        thread.join(timeout=2)"` | — |
| [SRC-1A176AD4F0-L000251](../../tests/test_hosted_smoke.py#L251) | 251 | `""` | — |
| [SRC-1A176AD4F0-L000252](../../tests/test_hosted_smoke.py#L252) | 252 | `""` | — |
| [SRC-1A176AD4F0-L000253](../../tests/test_hosted_smoke.py#L253) | 253 | `""` | — |
| [SRC-1A176AD4F0-L000254](../../tests/test_hosted_smoke.py#L254) | 254 | `"def test_health_403_metadata_is_preserved_in_failure_report(monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000255](../../tests/test_hosted_smoke.py#L255) | 255 | `"    metadata = {"` | — |
| [SRC-1A176AD4F0-L000256](../../tests/test_hosted_smoke.py#L256) | 256 | `"        \"status\": 403,"` | — |
| [SRC-1A176AD4F0-L000257](../../tests/test_hosted_smoke.py#L257) | 257 | `"        \"content_type\": \"text/html\","` | — |
| [SRC-1A176AD4F0-L000258](../../tests/test_hosted_smoke.py#L258) | 258 | `"        \"server\": \"edge-gateway\","` | — |
| [SRC-1A176AD4F0-L000259](../../tests/test_hosted_smoke.py#L259) | 259 | `"        \"request_id\": \"request-403\","` | — |
| [SRC-1A176AD4F0-L000260](../../tests/test_hosted_smoke.py#L260) | 260 | `"        \"correlation_id\": \"\","` | — |
| [SRC-1A176AD4F0-L000261](../../tests/test_hosted_smoke.py#L261) | 261 | `"        \"cf_ray\": \"ray-403\","` | — |
| [SRC-1A176AD4F0-L000262](../../tests/test_hosted_smoke.py#L262) | 262 | `"        \"via\": \"\","` | — |
| [SRC-1A176AD4F0-L000263](../../tests/test_hosted_smoke.py#L263) | 263 | `"        \"body_bytes_sampled\": 19,"` | — |
| [SRC-1A176AD4F0-L000264](../../tests/test_hosted_smoke.py#L264) | 264 | `"        \"body_sha256\": \"a\" * 64,"` | — |
| [SRC-1A176AD4F0-L000265](../../tests/test_hosted_smoke.py#L265) | 265 | `"    }"` | — |
| [SRC-1A176AD4F0-L000266](../../tests/test_hosted_smoke.py#L266) | 266 | `""` | — |
| [SRC-1A176AD4F0-L000267](../../tests/test_hosted_smoke.py#L267) | 267 | `"    def forbidden_health(url: str, **kwargs):"` | — |
| [SRC-1A176AD4F0-L000268](../../tests/test_hosted_smoke.py#L268) | 268 | `"        return 403, {\"_smoke_http\": metadata}"` | — |
| [SRC-1A176AD4F0-L000269](../../tests/test_hosted_smoke.py#L269) | 269 | `""` | — |
| [SRC-1A176AD4F0-L000270](../../tests/test_hosted_smoke.py#L270) | 270 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", forbidden_health)"` | — |
| [SRC-1A176AD4F0-L000271](../../tests/test_hosted_smoke.py#L271) | 271 | `"    with pytest.raises(SmokeError, match=\"Health check failed\") as failure:"` | — |
