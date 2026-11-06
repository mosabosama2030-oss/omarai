# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **049**
- سجلات الأسطر: **800**
- النطاق: SRC-1A176AD4F0-L000533 إلى SRC-62DC597310-L000010
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-1A176AD4F0 — [tests/test_hosted_smoke.py](../../tests/test_hosted_smoke.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1A176AD4F0-L000533](../../tests/test_hosted_smoke.py#L533) | 533 | `"        run_smoke(hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5)"` | — |
| [SRC-1A176AD4F0-L000534](../../tests/test_hosted_smoke.py#L534) | 534 | `""` | — |
| [SRC-1A176AD4F0-L000535](../../tests/test_hosted_smoke.py#L535) | 535 | `""` | — |
| [SRC-1A176AD4F0-L000536](../../tests/test_hosted_smoke.py#L536) | 536 | `"def test_smoke_rejects_unvalidated_answer_evidence(hosted_server, monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000537](../../tests/test_hosted_smoke.py#L537) | 537 | `"    original = hosted_smoke_test.request_json"` | — |
| [SRC-1A176AD4F0-L000538](../../tests/test_hosted_smoke.py#L538) | 538 | `""` | — |
| [SRC-1A176AD4F0-L000539](../../tests/test_hosted_smoke.py#L539) | 539 | `"    def invalid_evidence(url: str, **kwargs):"` | — |
| [SRC-1A176AD4F0-L000540](../../tests/test_hosted_smoke.py#L540) | 540 | `"        if urlsplit(url).path == \"/api/agent\" and kwargs.get(\"token\") == TOKEN:"` | — |
| [SRC-1A176AD4F0-L000541](../../tests/test_hosted_smoke.py#L541) | 541 | `"            return 200, {"` | — |
| [SRC-1A176AD4F0-L000542](../../tests/test_hosted_smoke.py#L542) | 542 | `"                \"answer\": \"إجابة بلا إحالات صالحة\", \"used_web_search\": True,"` | — |
| [SRC-1A176AD4F0-L000543](../../tests/test_hosted_smoke.py#L543) | 543 | `"                \"used_language_model\": True, \"answer_evidence_status\": \"not_assessed\","` | — |
| [SRC-1A176AD4F0-L000544](../../tests/test_hosted_smoke.py#L544) | 544 | `"                \"sources\": [{\"url\": \"https://example.com/source\"}],"` | — |
| [SRC-1A176AD4F0-L000545](../../tests/test_hosted_smoke.py#L545) | 545 | `"                \"request_budget\": {\"profile\": \"hosted_smoke\", \"timeout_seconds\": 75, \"budget_exhausted\": False, \"deadline_exceeded\": False, \"limits\": {\"search_queries\": 3, \"search_calls\": 12, \"model_calls\": 6, \"page_fetches\": 4, \"tool_calls\": 0}, \"counts\": {\"search_queries\": 2, \"search_calls\": 4, \"model_calls\": 4, \"page_fetches\": 1, \"tool_calls\": 0}},"` | — |
| [SRC-1A176AD4F0-L000546](../../tests/test_hosted_smoke.py#L546) | 546 | `"                \"search_report\": {"` | — |
| [SRC-1A176AD4F0-L000547](../../tests/test_hosted_smoke.py#L547) | 547 | `"                    \"pipeline_completion_status\": \"completed\","` | — |
| [SRC-1A176AD4F0-L000548](../../tests/test_hosted_smoke.py#L548) | 548 | `"                    \"semantic_claim_verification\": {\"status\": \"completed_all_claims_supported\"},"` | — |
| [SRC-1A176AD4F0-L000549](../../tests/test_hosted_smoke.py#L549) | 549 | `"                    \"insufficient_evidence\": False,"` | — |
| [SRC-1A176AD4F0-L000550](../../tests/test_hosted_smoke.py#L550) | 550 | `"                    \"claim_audit_semantics\": \"distinct_model_assessed_source_support_not_ground_truth\","` | — |
| [SRC-1A176AD4F0-L000551](../../tests/test_hosted_smoke.py#L551) | 551 | `"                },"` | — |
| [SRC-1A176AD4F0-L000552](../../tests/test_hosted_smoke.py#L552) | 552 | `"            }"` | — |
| [SRC-1A176AD4F0-L000553](../../tests/test_hosted_smoke.py#L553) | 553 | `"        return original(url, **kwargs)"` | — |
| [SRC-1A176AD4F0-L000554](../../tests/test_hosted_smoke.py#L554) | 554 | `""` | — |
| [SRC-1A176AD4F0-L000555](../../tests/test_hosted_smoke.py#L555) | 555 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", invalid_evidence)"` | — |
| [SRC-1A176AD4F0-L000556](../../tests/test_hosted_smoke.py#L556) | 556 | `"    with pytest.raises(SmokeError, match=\"evidence status\"):"` | — |
| [SRC-1A176AD4F0-L000557](../../tests/test_hosted_smoke.py#L557) | 557 | `"        run_smoke(hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5)"` | — |
| [SRC-1A176AD4F0-L000558](../../tests/test_hosted_smoke.py#L558) | 558 | `""` | — |
| [SRC-1A176AD4F0-L000559](../../tests/test_hosted_smoke.py#L559) | 559 | `""` | — |
| [SRC-1A176AD4F0-L000560](../../tests/test_hosted_smoke.py#L560) | 560 | `""` | — |
| [SRC-1A176AD4F0-L000561](../../tests/test_hosted_smoke.py#L561) | 561 | `""` | — |
| [SRC-1A176AD4F0-L000562](../../tests/test_hosted_smoke.py#L562) | 562 | `"def test_smoke_rejects_missing_or_exceeded_server_budget_profile(hosted_server, monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000563](../../tests/test_hosted_smoke.py#L563) | 563 | `"    original = hosted_smoke_test.request_json"` | — |
| [SRC-1A176AD4F0-L000564](../../tests/test_hosted_smoke.py#L564) | 564 | `""` | — |
| [SRC-1A176AD4F0-L000565](../../tests/test_hosted_smoke.py#L565) | 565 | `"    def unbounded_budget(url: str, **kwargs):"` | — |
| [SRC-1A176AD4F0-L000566](../../tests/test_hosted_smoke.py#L566) | 566 | `"        if urlsplit(url).path == \"/api/agent\" and kwargs.get(\"token\") == TOKEN:"` | — |
| [SRC-1A176AD4F0-L000567](../../tests/test_hosted_smoke.py#L567) | 567 | `"            status, payload = original(url, **kwargs)"` | — |
| [SRC-1A176AD4F0-L000568](../../tests/test_hosted_smoke.py#L568) | 568 | `"            payload[\"request_budget\"] = {"` | — |
| [SRC-1A176AD4F0-L000569](../../tests/test_hosted_smoke.py#L569) | 569 | `"                \"profile\": \"default\","` | — |
| [SRC-1A176AD4F0-L000570](../../tests/test_hosted_smoke.py#L570) | 570 | `"                \"budget_exhausted\": False,"` | — |
| [SRC-1A176AD4F0-L000571](../../tests/test_hosted_smoke.py#L571) | 571 | `"                \"deadline_exceeded\": False,"` | — |
| [SRC-1A176AD4F0-L000572](../../tests/test_hosted_smoke.py#L572) | 572 | `"                \"limits\": {\"search_queries\": 8, \"search_calls\": 32, \"model_calls\": 8, \"page_fetches\": 8, \"tool_calls\": 3},"` | — |
| [SRC-1A176AD4F0-L000573](../../tests/test_hosted_smoke.py#L573) | 573 | `"                \"counts\": {\"search_queries\": 1, \"search_calls\": 2, \"model_calls\": 2, \"page_fetches\": 1, \"tool_calls\": 0},"` | — |
| [SRC-1A176AD4F0-L000574](../../tests/test_hosted_smoke.py#L574) | 574 | `"            }"` | — |
| [SRC-1A176AD4F0-L000575](../../tests/test_hosted_smoke.py#L575) | 575 | `"            return status, payload"` | — |
| [SRC-1A176AD4F0-L000576](../../tests/test_hosted_smoke.py#L576) | 576 | `"        return original(url, **kwargs)"` | — |
| [SRC-1A176AD4F0-L000577](../../tests/test_hosted_smoke.py#L577) | 577 | `""` | — |
| [SRC-1A176AD4F0-L000578](../../tests/test_hosted_smoke.py#L578) | 578 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", unbounded_budget)"` | — |
| [SRC-1A176AD4F0-L000579](../../tests/test_hosted_smoke.py#L579) | 579 | `"    with pytest.raises(SmokeError, match=\"hosted_smoke request budget\"):"` | — |
| [SRC-1A176AD4F0-L000580](../../tests/test_hosted_smoke.py#L580) | 580 | `"        run_smoke(hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5)"` | — |
| [SRC-1A176AD4F0-L000581](../../tests/test_hosted_smoke.py#L581) | 581 | `""` | — |
| [SRC-1A176AD4F0-L000582](../../tests/test_hosted_smoke.py#L582) | 582 | `""` | — |
| [SRC-1A176AD4F0-L000583](../../tests/test_hosted_smoke.py#L583) | 583 | `""` | — |
| [SRC-1A176AD4F0-L000584](../../tests/test_hosted_smoke.py#L584) | 584 | `"def test_smoke_rejects_pipeline_complete_without_semantic_claim_support(hosted_server, monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000585](../../tests/test_hosted_smoke.py#L585) | 585 | `"    original = hosted_smoke_test.request_json"` | — |
| [SRC-1A176AD4F0-L000586](../../tests/test_hosted_smoke.py#L586) | 586 | `""` | — |
| [SRC-1A176AD4F0-L000587](../../tests/test_hosted_smoke.py#L587) | 587 | `"    def unverified_claims(url: str, **kwargs):"` | — |
| [SRC-1A176AD4F0-L000588](../../tests/test_hosted_smoke.py#L588) | 588 | `"        if urlsplit(url).path == \"/api/agent\" and kwargs.get(\"token\") == TOKEN:"` | — |
| [SRC-1A176AD4F0-L000589](../../tests/test_hosted_smoke.py#L589) | 589 | `"            return 200, {"` | — |
| [SRC-1A176AD4F0-L000590](../../tests/test_hosted_smoke.py#L590) | 590 | `"                \"answer\": \"ادعاء غير متحقق [المصدر 1]\", \"used_web_search\": True,"` | — |
| [SRC-1A176AD4F0-L000591](../../tests/test_hosted_smoke.py#L591) | 591 | `"                \"used_language_model\": True,"` | — |
| [SRC-1A176AD4F0-L000592](../../tests/test_hosted_smoke.py#L592) | 592 | `"                \"answer_evidence_status\": \"citation_indices_validated_only\","` | — |
| [SRC-1A176AD4F0-L000593](../../tests/test_hosted_smoke.py#L593) | 593 | `"                \"sources\": [{\"url\": \"https://example.com/source\"}],"` | — |
| [SRC-1A176AD4F0-L000594](../../tests/test_hosted_smoke.py#L594) | 594 | `"                \"request_budget\": {\"profile\": \"hosted_smoke\", \"timeout_seconds\": 75, \"budget_exhausted\": False, \"deadline_exceeded\": False, \"limits\": {\"search_queries\": 3, \"search_calls\": 12, \"model_calls\": 6, \"page_fetches\": 4, \"tool_calls\": 0}, \"counts\": {\"search_queries\": 2, \"search_calls\": 4, \"model_calls\": 4, \"page_fetches\": 1, \"tool_calls\": 0}},"` | — |
| [SRC-1A176AD4F0-L000595](../../tests/test_hosted_smoke.py#L595) | 595 | `"                \"search_report\": {"` | — |
| [SRC-1A176AD4F0-L000596](../../tests/test_hosted_smoke.py#L596) | 596 | `"                    \"pipeline_completion_status\": \"completed\","` | — |
| [SRC-1A176AD4F0-L000597](../../tests/test_hosted_smoke.py#L597) | 597 | `"                    \"semantic_claim_verification\": {\"status\": \"not_performed\"},"` | — |
| [SRC-1A176AD4F0-L000598](../../tests/test_hosted_smoke.py#L598) | 598 | `"                    \"insufficient_evidence\": False,"` | — |
| [SRC-1A176AD4F0-L000599](../../tests/test_hosted_smoke.py#L599) | 599 | `"                    \"claim_audit_semantics\": \"distinct_model_assessed_source_support_not_ground_truth\","` | — |
| [SRC-1A176AD4F0-L000600](../../tests/test_hosted_smoke.py#L600) | 600 | `"                },"` | — |
| [SRC-1A176AD4F0-L000601](../../tests/test_hosted_smoke.py#L601) | 601 | `"            }"` | — |
| [SRC-1A176AD4F0-L000602](../../tests/test_hosted_smoke.py#L602) | 602 | `"        return original(url, **kwargs)"` | — |
| [SRC-1A176AD4F0-L000603](../../tests/test_hosted_smoke.py#L603) | 603 | `""` | — |
| [SRC-1A176AD4F0-L000604](../../tests/test_hosted_smoke.py#L604) | 604 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", unverified_claims)"` | — |
| [SRC-1A176AD4F0-L000605](../../tests/test_hosted_smoke.py#L605) | 605 | `"    with pytest.raises(SmokeError, match=\"semantic claim-support review\"):"` | — |
| [SRC-1A176AD4F0-L000606](../../tests/test_hosted_smoke.py#L606) | 606 | `"        run_smoke(hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5)"` | — |
| [SRC-1A176AD4F0-L000607](../../tests/test_hosted_smoke.py#L607) | 607 | `""` | — |
| [SRC-1A176AD4F0-L000608](../../tests/test_hosted_smoke.py#L608) | 608 | `""` | — |
| [SRC-1A176AD4F0-L000609](../../tests/test_hosted_smoke.py#L609) | 609 | `"def test_hosted_smoke_workflow_scopes_secrets_to_the_execution_step():"` | — |
| [SRC-1A176AD4F0-L000610](../../tests/test_hosted_smoke.py#L610) | 610 | `"    workflow = Path(\".github/workflows/hosted-smoke.yml\").read_text(encoding=\"utf-8\")"` | — |
| [SRC-1A176AD4F0-L000611](../../tests/test_hosted_smoke.py#L611) | 611 | `"    job = workflow.split(\"jobs:\", 1)[1].split(\"steps:\", 1)[0]"` | — |
| [SRC-1A176AD4F0-L000612](../../tests/test_hosted_smoke.py#L612) | 612 | `"    assert \"OMARAI_ACCESS_TOKEN\" not in job"` | — |
| [SRC-1A176AD4F0-L000613](../../tests/test_hosted_smoke.py#L613) | 613 | `"    assert \"OMARAI_BASE_URL\" not in job"` | — |
| [SRC-1A176AD4F0-L000614](../../tests/test_hosted_smoke.py#L614) | 614 | `"    assert \"OMARAI_ACCESS_TOKEN:\" in workflow"` | — |
| [SRC-1A176AD4F0-L000615](../../tests/test_hosted_smoke.py#L615) | 615 | `"    assert \"OMARAI_BASE_URL:\" in workflow"` | — |
| [SRC-1A176AD4F0-L000616](../../tests/test_hosted_smoke.py#L616) | 616 | `"    preflight_step = workflow.split(\"- name: Run no-cost hosted preflight\", 1)[1].split("` | — |
| [SRC-1A176AD4F0-L000617](../../tests/test_hosted_smoke.py#L617) | 617 | `"        \"- name: Run live hosted acceptance\", 1"` | — |
| [SRC-1A176AD4F0-L000618](../../tests/test_hosted_smoke.py#L618) | 618 | `"    )[0]"` | — |
| [SRC-1A176AD4F0-L000619](../../tests/test_hosted_smoke.py#L619) | 619 | `"    live_step = workflow.split(\"- name: Run live hosted acceptance\", 1)[1].split("` | — |
| [SRC-1A176AD4F0-L000620](../../tests/test_hosted_smoke.py#L620) | 620 | `"        \"- name: Upload hosted question-and-answer transcript\", 1"` | — |
| [SRC-1A176AD4F0-L000621](../../tests/test_hosted_smoke.py#L621) | 621 | `"    )[0]"` | — |
| [SRC-1A176AD4F0-L000622](../../tests/test_hosted_smoke.py#L622) | 622 | `"    assert \"OMARAI_ACCESS_TOKEN\" not in preflight_step"` | — |
| [SRC-1A176AD4F0-L000623](../../tests/test_hosted_smoke.py#L623) | 623 | `"    assert \"OMARAI_ACCESS_TOKEN:\" in live_step"` | — |
| [SRC-1A176AD4F0-L000624](../../tests/test_hosted_smoke.py#L624) | 624 | `"    assert \"preflight-only\" in workflow"` | — |
| [SRC-1A176AD4F0-L000625](../../tests/test_hosted_smoke.py#L625) | 625 | `"    assert \"default: false\" in workflow"` | — |
| [SRC-1A176AD4F0-L000626](../../tests/test_hosted_smoke.py#L626) | 626 | `""` | — |
| [SRC-1A176AD4F0-L000627](../../tests/test_hosted_smoke.py#L627) | 627 | `""` | — |
| [SRC-1A176AD4F0-L000628](../../tests/test_hosted_smoke.py#L628) | 628 | `"def test_hosted_smoke_workflow_is_manual_and_cost_gated():"` | — |
| [SRC-1A176AD4F0-L000629](../../tests/test_hosted_smoke.py#L629) | 629 | `"    workflow = Path(\".github/workflows/hosted-smoke.yml\").read_text(encoding=\"utf-8\")"` | — |
| [SRC-1A176AD4F0-L000630](../../tests/test_hosted_smoke.py#L630) | 630 | `"    assert \"schedule:\" not in workflow"` | — |
| [SRC-1A176AD4F0-L000631](../../tests/test_hosted_smoke.py#L631) | 631 | `"    assert \"allow_provider_usage:\" in workflow"` | — |
| [SRC-1A176AD4F0-L000632](../../tests/test_hosted_smoke.py#L632) | 632 | `"    assert \"default: false\" in workflow"` | — |
| [SRC-1A176AD4F0-L000633](../../tests/test_hosted_smoke.py#L633) | 633 | `"    assert \"--allow-provider-usage\" in workflow"` | — |
| [SRC-1A176AD4F0-L000634](../../tests/test_hosted_smoke.py#L634) | 634 | `""` | — |
| [SRC-1A176AD4F0-L000635](../../tests/test_hosted_smoke.py#L635) | 635 | `""` | — |
| [SRC-1A176AD4F0-L000636](../../tests/test_hosted_smoke.py#L636) | 636 | `"def test_hosted_smoke_budget_caps_match_server_enforced_profile():"` | — |
| [SRC-1A176AD4F0-L000637](../../tests/test_hosted_smoke.py#L637) | 637 | `"    from agents.request_budget import HOSTED_SMOKE_BUDGET_LIMITS"` | — |
| [SRC-1A176AD4F0-L000638](../../tests/test_hosted_smoke.py#L638) | 638 | `""` | — |
| [SRC-1A176AD4F0-L000639](../../tests/test_hosted_smoke.py#L639) | 639 | `"    assert hosted_smoke_test.HOSTED_SMOKE_BUDGET_MAX == HOSTED_SMOKE_BUDGET_LIMITS"` | — |
| [SRC-1A176AD4F0-L000640](../../tests/test_hosted_smoke.py#L640) | 640 | `""` | — |
| [SRC-1A176AD4F0-L000641](../../tests/test_hosted_smoke.py#L641) | 641 | `""` | — |
| [SRC-1A176AD4F0-L000642](../../tests/test_hosted_smoke.py#L642) | 642 | `"def test_hosted_smoke_requires_successful_no_cost_preflight_before_live_usage():"` | — |
| [SRC-1A176AD4F0-L000643](../../tests/test_hosted_smoke.py#L643) | 643 | `"    workflow = Path(\".github/workflows/hosted-smoke.yml\").read_text(encoding=\"utf-8\")"` | — |
| [SRC-1A176AD4F0-L000644](../../tests/test_hosted_smoke.py#L644) | 644 | `"    preflight_step = workflow.split(\"- name: Run no-cost hosted preflight\", 1)[1].split("` | — |
| [SRC-1A176AD4F0-L000645](../../tests/test_hosted_smoke.py#L645) | 645 | `"        \"- name: Run live hosted acceptance\", 1"` | — |
| [SRC-1A176AD4F0-L000646](../../tests/test_hosted_smoke.py#L646) | 646 | `"    )[0]"` | — |
| [SRC-1A176AD4F0-L000647](../../tests/test_hosted_smoke.py#L647) | 647 | `"    live_step = workflow.split(\"- name: Run live hosted acceptance\", 1)[1].split("` | — |
| [SRC-1A176AD4F0-L000648](../../tests/test_hosted_smoke.py#L648) | 648 | `"        \"- name: Upload hosted question-and-answer transcript\", 1"` | — |
| [SRC-1A176AD4F0-L000649](../../tests/test_hosted_smoke.py#L649) | 649 | `"    )[0]"` | — |
| [SRC-1A176AD4F0-L000650](../../tests/test_hosted_smoke.py#L650) | 650 | `""` | — |
| [SRC-1A176AD4F0-L000651](../../tests/test_hosted_smoke.py#L651) | 651 | `"    assert \"id: preflight\" in preflight_step"` | — |
| [SRC-1A176AD4F0-L000652](../../tests/test_hosted_smoke.py#L652) | 652 | `"    assert \"if:\" not in preflight_step"` | — |
| [SRC-1A176AD4F0-L000653](../../tests/test_hosted_smoke.py#L653) | 653 | `"    assert '--expected-sha \"$(git rev-parse HEAD)\"' in preflight_step"` | — |
| [SRC-1A176AD4F0-L000654](../../tests/test_hosted_smoke.py#L654) | 654 | `"    assert \"steps.preflight.outcome == 'success'\" in live_step"` | — |
| [SRC-1A176AD4F0-L000655](../../tests/test_hosted_smoke.py#L655) | 655 | `"    assert \"allow_provider_usage == true\" in live_step"` | — |
| [SRC-1A176AD4F0-L000656](../../tests/test_hosted_smoke.py#L656) | 656 | `"    assert \"OMARAI_ACCESS_TOKEN\" not in preflight_step"` | — |
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
| [SRC-1BB2FDD5B7-L000041](../../tests/test_hosted_smoke_transcript.py#L41) | 41 | `"                \"answer_evidence_status\": \"citation_indices_validated_only\","` | — |
| [SRC-1BB2FDD5B7-L000042](../../tests/test_hosted_smoke_transcript.py#L42) | 42 | `"                \"sources\": ["` | — |
| [SRC-1BB2FDD5B7-L000043](../../tests/test_hosted_smoke_transcript.py#L43) | 43 | `"                    {"` | — |
| [SRC-1BB2FDD5B7-L000044](../../tests/test_hosted_smoke_transcript.py#L44) | 44 | `"                        \"title\": \"Fire alarm tender notice\","` | — |
| [SRC-1BB2FDD5B7-L000045](../../tests/test_hosted_smoke_transcript.py#L45) | 45 | `"                        \"url\": \"https://example.test/fire-alarm-tender\","` | — |
| [SRC-1BB2FDD5B7-L000046](../../tests/test_hosted_smoke_transcript.py#L46) | 46 | `"                        \"provider\": \"bing_rss\","` | — |
| [SRC-1BB2FDD5B7-L000047](../../tests/test_hosted_smoke_transcript.py#L47) | 47 | `"                        \"snippet\": \"طلب عرض سعر لنظام إنذار الحريق.\","` | — |
| [SRC-1BB2FDD5B7-L000048](../../tests/test_hosted_smoke_transcript.py#L48) | 48 | `"                        \"published_at\": \"\","` | — |
| [SRC-1BB2FDD5B7-L000049](../../tests/test_hosted_smoke_transcript.py#L49) | 49 | `"                    }"` | — |
| [SRC-1BB2FDD5B7-L000050](../../tests/test_hosted_smoke_transcript.py#L50) | 50 | `"                ],"` | — |
| [SRC-1BB2FDD5B7-L000051](../../tests/test_hosted_smoke_transcript.py#L51) | 51 | `"                \"request_budget\": {\"profile\": \"hosted_smoke\", \"timeout_seconds\": 75, \"budget_exhausted\": False, \"deadline_exceeded\": False, \"limits\": {\"search_queries\": 3, \"search_calls\": 12, \"model_calls\": 6, \"page_fetches\": 4, \"tool_calls\": 0}, \"counts\": {\"search_queries\": 2, \"search_calls\": 4, \"model_calls\": 4, \"page_fetches\": 1, \"tool_calls\": 0}},"` | — |
| [SRC-1BB2FDD5B7-L000052](../../tests/test_hosted_smoke_transcript.py#L52) | 52 | `"                \"search_report\": {"` | — |
| [SRC-1BB2FDD5B7-L000053](../../tests/test_hosted_smoke_transcript.py#L53) | 53 | `"                    \"pages_fetched\": 1,"` | — |
| [SRC-1BB2FDD5B7-L000054](../../tests/test_hosted_smoke_transcript.py#L54) | 54 | `"                    \"providers_used\": [\"bing_rss\"],"` | — |
| [SRC-1BB2FDD5B7-L000055](../../tests/test_hosted_smoke_transcript.py#L55) | 55 | `"                    \"pipeline_completion_status\": \"completed\","` | — |
| [SRC-1BB2FDD5B7-L000056](../../tests/test_hosted_smoke_transcript.py#L56) | 56 | `"                    \"semantic_claim_verification\": {\"status\": \"completed_all_claims_supported\"},"` | — |
| [SRC-1BB2FDD5B7-L000057](../../tests/test_hosted_smoke_transcript.py#L57) | 57 | `"                    \"insufficient_evidence\": False,"` | — |
| [SRC-1BB2FDD5B7-L000058](../../tests/test_hosted_smoke_transcript.py#L58) | 58 | `"                    \"claim_audit_semantics\": \"distinct_model_assessed_source_support_not_ground_truth\","` | — |
| [SRC-1BB2FDD5B7-L000059](../../tests/test_hosted_smoke_transcript.py#L59) | 59 | `"                },"` | — |
| [SRC-1BB2FDD5B7-L000060](../../tests/test_hosted_smoke_transcript.py#L60) | 60 | `"            }"` | — |
| [SRC-1BB2FDD5B7-L000061](../../tests/test_hosted_smoke_transcript.py#L61) | 61 | `"        raise AssertionError(f\"unexpected request: {url}\")"` | — |
| [SRC-1BB2FDD5B7-L000062](../../tests/test_hosted_smoke_transcript.py#L62) | 62 | `""` | — |
| [SRC-1BB2FDD5B7-L000063](../../tests/test_hosted_smoke_transcript.py#L63) | 63 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", fake_request_json)"` | — |
| [SRC-1BB2FDD5B7-L000064](../../tests/test_hosted_smoke_transcript.py#L64) | 64 | `"    report = hosted_smoke_test.run_smoke("` | — |
| [SRC-1BB2FDD5B7-L000065](../../tests/test_hosted_smoke_transcript.py#L65) | 65 | `"        \"https://omarai.example\", \"T\" * 40, expected_sha=\"a\" * 40,"` | — |
| [SRC-1BB2FDD5B7-L000066](../../tests/test_hosted_smoke_transcript.py#L66) | 66 | `"        allow_provider_usage=True,"` | — |
| [SRC-1BB2FDD5B7-L000067](../../tests/test_hosted_smoke_transcript.py#L67) | 67 | `"    )"` | — |
| [SRC-1BB2FDD5B7-L000068](../../tests/test_hosted_smoke_transcript.py#L68) | 68 | `""` | — |
| [SRC-1BB2FDD5B7-L000069](../../tests/test_hosted_smoke_transcript.py#L69) | 69 | `"    transcript = report[\"transcript\"][0]"` | — |
| [SRC-1BB2FDD5B7-L000070](../../tests/test_hosted_smoke_transcript.py#L70) | 70 | `"    assert transcript[\"question\"] == hosted_smoke_test.LIVE_TEST_QUESTION"` | — |
| [SRC-1BB2FDD5B7-L000071](../../tests/test_hosted_smoke_transcript.py#L71) | 71 | `"    assert transcript[\"answer\"] == \"وجدت إشارة منشورة تطلب عرض سعر لنظام إنذار الحريق.\""` | — |
| [SRC-1BB2FDD5B7-L000072](../../tests/test_hosted_smoke_transcript.py#L72) | 72 | `"    assert transcript[\"sources\"][0][\"url\"] == \"https://example.test/fire-alarm-tender\""` | — |
| [SRC-1BB2FDD5B7-L000073](../../tests/test_hosted_smoke_transcript.py#L73) | 73 | `"    assert transcript[\"pipeline_completion_status\"] == \"completed\""` | — |
| [SRC-1BB2FDD5B7-L000074](../../tests/test_hosted_smoke_transcript.py#L74) | 74 | `"    assert transcript[\"request_budget\"][\"profile\"] == \"hosted_smoke\""` | — |
| [SRC-1BB2FDD5B7-L000075](../../tests/test_hosted_smoke_transcript.py#L75) | 75 | `"    assert report[\"checks\"][\"request_budget\"][\"limits\"][\"search_calls\"] <= 12"` | — |
| [SRC-1BB2FDD5B7-L000076](../../tests/test_hosted_smoke_transcript.py#L76) | 76 | `"    assert report[\"checks\"][\"search\"][\"providers_reported\"] == [\"bing_rss\"]"` | — |
| [SRC-1BB2FDD5B7-L000077](../../tests/test_hosted_smoke_transcript.py#L77) | 77 | `"    assert all(\"T\" * 40 not in str(item) for item in report.values())"` | — |
| [SRC-1BB2FDD5B7-L000078](../../tests/test_hosted_smoke_transcript.py#L78) | 78 | `"    assert len(calls) == 3"` | — |
| [SRC-1BB2FDD5B7-L000079](../../tests/test_hosted_smoke_transcript.py#L79) | 79 | `"    assert not any(call[0].endswith(\"/api/diagnostics\") for call in calls)"` | — |
| [SRC-1BB2FDD5B7-L000080](../../tests/test_hosted_smoke_transcript.py#L80) | 80 | `""` | — |
| [SRC-1BB2FDD5B7-L000081](../../tests/test_hosted_smoke_transcript.py#L81) | 81 | `""` | — |
| [SRC-1BB2FDD5B7-L000082](../../tests/test_hosted_smoke_transcript.py#L82) | 82 | `"def test_hosted_smoke_allows_no_token_only_for_loopback_dev(monkeypatch):"` | — |
| [SRC-1BB2FDD5B7-L000083](../../tests/test_hosted_smoke_transcript.py#L83) | 83 | `"    def fake_request_json(url, *, token=\"\", payload=None, timeout=90):"` | — |
| [SRC-1BB2FDD5B7-L000084](../../tests/test_hosted_smoke_transcript.py#L84) | 84 | `"        if url.endswith(\"/api/health\"):"` | — |
| [SRC-1BB2FDD5B7-L000085](../../tests/test_hosted_smoke_transcript.py#L85) | 85 | `"            return 200, {\"ok\": True, \"build\": {\"sha\": \"unknown\"}}"` | — |
| [SRC-1BB2FDD5B7-L000086](../../tests/test_hosted_smoke_transcript.py#L86) | 86 | `"        if url.endswith(\"/api/agent\"):"` | — |
| [SRC-1BB2FDD5B7-L000087](../../tests/test_hosted_smoke_transcript.py#L87) | 87 | `"            return 200, {"` | — |
| [SRC-1BB2FDD5B7-L000088](../../tests/test_hosted_smoke_transcript.py#L88) | 88 | `"                \"answer\": \"لا توجد إشارة شراء مؤكدة في المصادر التي تم فحصها.\","` | — |
| [SRC-1BB2FDD5B7-L000089](../../tests/test_hosted_smoke_transcript.py#L89) | 89 | `"                \"used_web_search\": True,"` | — |
| [SRC-1BB2FDD5B7-L000090](../../tests/test_hosted_smoke_transcript.py#L90) | 90 | `"                \"used_language_model\": True,"` | — |
| [SRC-1BB2FDD5B7-L000091](../../tests/test_hosted_smoke_transcript.py#L91) | 91 | `"                \"answer_evidence_status\": \"citation_indices_validated_only\","` | — |
| [SRC-1BB2FDD5B7-L000092](../../tests/test_hosted_smoke_transcript.py#L92) | 92 | `"                \"sources\": [{\"url\": \"https://example.test/egypt\"}],"` | — |
| [SRC-1BB2FDD5B7-L000093](../../tests/test_hosted_smoke_transcript.py#L93) | 93 | `"                \"request_budget\": {\"profile\": \"hosted_smoke\", \"timeout_seconds\": 75, \"budget_exhausted\": False, \"deadline_exceeded\": False, \"limits\": {\"search_queries\": 3, \"search_calls\": 12, \"model_calls\": 6, \"page_fetches\": 4, \"tool_calls\": 0}, \"counts\": {\"search_queries\": 1, \"search_calls\": 2, \"model_calls\": 3, \"page_fetches\": 1, \"tool_calls\": 0}},"` | — |
| [SRC-1BB2FDD5B7-L000094](../../tests/test_hosted_smoke_transcript.py#L94) | 94 | `"                \"search_report\": {"` | — |
| [SRC-1BB2FDD5B7-L000095](../../tests/test_hosted_smoke_transcript.py#L95) | 95 | `"                    \"pipeline_completion_status\": \"completed\","` | — |
| [SRC-1BB2FDD5B7-L000096](../../tests/test_hosted_smoke_transcript.py#L96) | 96 | `"                    \"semantic_claim_verification\": {\"status\": \"completed_no_factual_claims\"},"` | — |
| [SRC-1BB2FDD5B7-L000097](../../tests/test_hosted_smoke_transcript.py#L97) | 97 | `"                    \"insufficient_evidence\": False,"` | — |
| [SRC-1BB2FDD5B7-L000098](../../tests/test_hosted_smoke_transcript.py#L98) | 98 | `"                    \"claim_audit_semantics\": \"distinct_model_assessed_source_support_not_ground_truth\","` | — |
| [SRC-1BB2FDD5B7-L000099](../../tests/test_hosted_smoke_transcript.py#L99) | 99 | `"                },"` | — |
| [SRC-1BB2FDD5B7-L000100](../../tests/test_hosted_smoke_transcript.py#L100) | 100 | `"            }"` | — |
| [SRC-1BB2FDD5B7-L000101](../../tests/test_hosted_smoke_transcript.py#L101) | 101 | `"        raise AssertionError(url)"` | — |
| [SRC-1BB2FDD5B7-L000102](../../tests/test_hosted_smoke_transcript.py#L102) | 102 | `""` | — |
| [SRC-1BB2FDD5B7-L000103](../../tests/test_hosted_smoke_transcript.py#L103) | 103 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", fake_request_json)"` | — |
| [SRC-1BB2FDD5B7-L000104](../../tests/test_hosted_smoke_transcript.py#L104) | 104 | `"    report = hosted_smoke_test.run_smoke("` | — |
| [SRC-1BB2FDD5B7-L000105](../../tests/test_hosted_smoke_transcript.py#L105) | 105 | `"        \"http://127.0.0.1:8000\","` | — |
| [SRC-1BB2FDD5B7-L000106](../../tests/test_hosted_smoke_transcript.py#L106) | 106 | `"        \"\","` | — |
| [SRC-1BB2FDD5B7-L000107](../../tests/test_hosted_smoke_transcript.py#L107) | 107 | `"        local_dev_no_token=True,"` | — |
| [SRC-1BB2FDD5B7-L000108](../../tests/test_hosted_smoke_transcript.py#L108) | 108 | `"        allow_provider_usage=True,"` | — |
| [SRC-1BB2FDD5B7-L000109](../../tests/test_hosted_smoke_transcript.py#L109) | 109 | `"    )"` | — |
| [SRC-1BB2FDD5B7-L000110](../../tests/test_hosted_smoke_transcript.py#L110) | 110 | `"    assert report[\"auth_mode\"] == \"local_loopback_dev_bypass\""` | — |
| [SRC-1BB2FDD5B7-L000111](../../tests/test_hosted_smoke_transcript.py#L111) | 111 | `"    assert report[\"transcript\"][0][\"answer\"] == \"لا توجد إشارة شراء مؤكدة في المصادر التي تم فحصها.\""` | — |
| [SRC-1BB2FDD5B7-L000112](../../tests/test_hosted_smoke_transcript.py#L112) | 112 | `""` | — |
| [SRC-1BB2FDD5B7-L000113](../../tests/test_hosted_smoke_transcript.py#L113) | 113 | `""` | — |
| [SRC-1BB2FDD5B7-L000114](../../tests/test_hosted_smoke_transcript.py#L114) | 114 | `"def test_hosted_smoke_rejects_no_token_for_remote_host():"` | — |
| [SRC-1BB2FDD5B7-L000115](../../tests/test_hosted_smoke_transcript.py#L115) | 115 | `"    import pytest"` | — |
| [SRC-1BB2FDD5B7-L000116](../../tests/test_hosted_smoke_transcript.py#L116) | 116 | `""` | — |
| [SRC-1BB2FDD5B7-L000117](../../tests/test_hosted_smoke_transcript.py#L117) | 117 | `"    with pytest.raises(hosted_smoke_test.SmokeError, match=\"localhost/loopback\"):"` | — |
| [SRC-1BB2FDD5B7-L000118](../../tests/test_hosted_smoke_transcript.py#L118) | 118 | `"        hosted_smoke_test.run_smoke("` | — |
| [SRC-1BB2FDD5B7-L000119](../../tests/test_hosted_smoke_transcript.py#L119) | 119 | `"            \"https://omarai.example\","` | — |
| [SRC-1BB2FDD5B7-L000120](../../tests/test_hosted_smoke_transcript.py#L120) | 120 | `"            \"\","` | — |
| [SRC-1BB2FDD5B7-L000121](../../tests/test_hosted_smoke_transcript.py#L121) | 121 | `"            local_dev_no_token=True,"` | — |
| [SRC-1BB2FDD5B7-L000122](../../tests/test_hosted_smoke_transcript.py#L122) | 122 | `"        )"` | — |
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
| [SRC-EA6EC52573-L000033](../../tests/test_intent_router.py#L33) | 33 | `"        (\"ابحث عن عميل يطلب او يريد شقة في التجمع الخامس\", \"LEAD_GENERATION\"),"` | — |
| [SRC-EA6EC52573-L000034](../../tests/test_intent_router.py#L34) | 34 | `"        (\"ابحث عن ١٠ عملاش يريدون شرا شقة في التجمع الخامس\", \"LEAD_GENERATION\"),"` | — |
| [SRC-EA6EC52573-L000035](../../tests/test_intent_router.py#L35) | 35 | `"        (\"ابحث عن شقق للبيع في العاصمة الإدارية\", \"WEB_SIMPLE\"),"` | — |
| [SRC-EA6EC52573-L000036](../../tests/test_intent_router.py#L36) | 36 | `"        (\"Find buyers looking to buy apartments in New Capital\", \"LEAD_GENERATION\"),"` | — |
| [SRC-EA6EC52573-L000037](../../tests/test_intent_router.py#L37) | 37 | `"        (\"لخص الصفحة https://example.com/article\", \"WEB_SIMPLE\"),"` | — |
| [SRC-EA6EC52573-L000038](../../tests/test_intent_router.py#L38) | 38 | `"        (\"Summarize this page https://example.com/article\", \"WEB_SIMPLE\"),"` | — |
| [SRC-EA6EC52573-L000039](../../tests/test_intent_router.py#L39) | 39 | `"        (\"لخص النص التالي: هذا نص تجريبي\", \"MODEL_ONLY\"),"` | — |
| [SRC-EA6EC52573-L000040](../../tests/test_intent_router.py#L40) | 40 | `"    ],"` | — |
| [SRC-EA6EC52573-L000041](../../tests/test_intent_router.py#L41) | 41 | `")"` | — |
| [SRC-EA6EC52573-L000042](../../tests/test_intent_router.py#L42) | 42 | `"def test_lead_generation_and_summarization_routes(question: str, expected: str) -> None:"` | — |
| [SRC-EA6EC52573-L000043](../../tests/test_intent_router.py#L43) | 43 | `"    decision = route_intent(question)"` | — |
| [SRC-EA6EC52573-L000044](../../tests/test_intent_router.py#L44) | 44 | `"    assert decision[\"route\"] == expected"` | — |
| [SRC-EA6EC52573-L000045](../../tests/test_intent_router.py#L45) | 45 | `"    assert decision[\"reason\"]"` | — |
| [SRC-EA6EC52573-L000046](../../tests/test_intent_router.py#L46) | 46 | `""` | — |
| [SRC-EA6EC52573-L000047](../../tests/test_intent_router.py#L47) | 47 | `""` | — |
| [SRC-EA6EC52573-L000048](../../tests/test_intent_router.py#L48) | 48 | `"def test_generic_explanation_of_lead_generation_is_not_a_lead_search() -> None:"` | — |
| [SRC-EA6EC52573-L000049](../../tests/test_intent_router.py#L49) | 49 | `"    assert route_intent(\"What is lead generation?\")[\"route\"] == \"MODEL_ONLY\""` | — |
| [SRC-EA6EC52573-L000050](../../tests/test_intent_router.py#L50) | 50 | `"    assert route_intent(\"Create a prospect list for apartment buyers\")[\"route\"] == \"LEAD_GENERATION\""` | — |
| [SRC-EA6EC52573-L000051](../../tests/test_intent_router.py#L51) | 51 | `""` | — |
| [SRC-EA6EC52573-L000052](../../tests/test_intent_router.py#L52) | 52 | `""` | — |
| [SRC-EA6EC52573-L000053](../../tests/test_intent_router.py#L53) | 53 | `""` | — |
| [SRC-EA6EC52573-L000054](../../tests/test_intent_router.py#L54) | 54 | `"def test_capability_question_is_local() -> None:"` | — |
| [SRC-EA6EC52573-L000055](../../tests/test_intent_router.py#L55) | 55 | `"    decision = route_intent("` | — |
| [SRC-EA6EC52573-L000056](../../tests/test_intent_router.py#L56) | 56 | `"        \"كيف تستطيع مساعدتي؟\","` | — |
| [SRC-EA6EC52573-L000057](../../tests/test_intent_router.py#L57) | 57 | `"        capability_question=True,"` | — |
| [SRC-EA6EC52573-L000058](../../tests/test_intent_router.py#L58) | 58 | `"        requires_web=False,"` | — |
| [SRC-EA6EC52573-L000059](../../tests/test_intent_router.py#L59) | 59 | `"    )"` | — |
| [SRC-EA6EC52573-L000060](../../tests/test_intent_router.py#L60) | 60 | `"    assert decision[\"route\"] == \"LOCAL\""` | — |
| [SRC-EA6EC52573-L000061](../../tests/test_intent_router.py#L61) | 61 | `"    assert decision[\"reason\"] == \"capability_question\""` | — |
| [SRC-EA6EC52573-L000062](../../tests/test_intent_router.py#L62) | 62 | `""` | — |
| [SRC-EA6EC52573-L000063](../../tests/test_intent_router.py#L63) | 63 | `""` | — |
| [SRC-EA6EC52573-L000064](../../tests/test_intent_router.py#L64) | 64 | `"def test_ambiguous_followup_uses_existing_conversation_context() -> None:"` | — |
| [SRC-EA6EC52573-L000065](../../tests/test_intent_router.py#L65) | 65 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000066](../../tests/test_intent_router.py#L66) | 66 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر iPhone 17 في مصر\"},"` | — |
| [SRC-EA6EC52573-L000067](../../tests/test_intent_router.py#L67) | 67 | `"        {\"role\": \"assistant\", \"content\": \"نتحدث عن هاتف iPhone 17 في السوق المصري.\"},"` | — |
| [SRC-EA6EC52573-L000068](../../tests/test_intent_router.py#L68) | 68 | `"    ]"` | — |
| [SRC-EA6EC52573-L000069](../../tests/test_intent_router.py#L69) | 69 | `"    decision = route_intent(\"كام سعرها؟\", history, requires_web=True)"` | — |
| [SRC-EA6EC52573-L000070](../../tests/test_intent_router.py#L70) | 70 | `"    assert decision[\"route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-EA6EC52573-L000071](../../tests/test_intent_router.py#L71) | 71 | `"    assert decision[\"context_available\"] is True"` | — |
| [SRC-EA6EC52573-L000072](../../tests/test_intent_router.py#L72) | 72 | `"    assert decision[\"needs_clarification\"] is False"` | — |
| [SRC-EA6EC52573-L000073](../../tests/test_intent_router.py#L73) | 73 | `""` | — |
| [SRC-EA6EC52573-L000074](../../tests/test_intent_router.py#L74) | 74 | `""` | — |
| [SRC-EA6EC52573-L000075](../../tests/test_intent_router.py#L75) | 75 | `"def test_comparison_followup_requires_context_before_deep_search() -> None:"` | — |
| [SRC-EA6EC52573-L000076](../../tests/test_intent_router.py#L76) | 76 | `"    assert route_intent(\"قارنهم\")[\"route\"] == \"CLARIFY\""` | — |
| [SRC-EA6EC52573-L000077](../../tests/test_intent_router.py#L77) | 77 | `"    history = [{\"role\": \"user\", \"content\": \"قارن iPhone 17 وSamsung S26\"}]"` | — |
| [SRC-EA6EC52573-L000078](../../tests/test_intent_router.py#L78) | 78 | `"    decision = route_intent(\"قارنهم\", history)"` | — |
| [SRC-EA6EC52573-L000079](../../tests/test_intent_router.py#L79) | 79 | `"    assert decision[\"route\"] == \"WEB_DEEP\""` | — |
| [SRC-EA6EC52573-L000080](../../tests/test_intent_router.py#L80) | 80 | `"    assert decision[\"context_available\"] is True"` | — |
| [SRC-EA6EC52573-L000081](../../tests/test_intent_router.py#L81) | 81 | `""` | — |
| [SRC-EA6EC52573-L000082](../../tests/test_intent_router.py#L82) | 82 | `""` | — |
| [SRC-EA6EC52573-L000083](../../tests/test_intent_router.py#L83) | 83 | `"def test_ambiguous_followup_does_not_reuse_stale_topic_after_acknowledgment() -> None:"` | — |
| [SRC-EA6EC52573-L000084](../../tests/test_intent_router.py#L84) | 84 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000085](../../tests/test_intent_router.py#L85) | 85 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر iPhone 17 في مصر\"},"` | — |
| [SRC-EA6EC52573-L000086](../../tests/test_intent_router.py#L86) | 86 | `"        {\"role\": \"assistant\", \"content\": \"سأساعدك في العثور على أسعار حديثة.\"},"` | — |
| [SRC-EA6EC52573-L000087](../../tests/test_intent_router.py#L87) | 87 | `"        {\"role\": \"user\", \"content\": \"شكرا\"},"` | — |
| [SRC-EA6EC52573-L000088](../../tests/test_intent_router.py#L88) | 88 | `"        {\"role\": \"assistant\", \"content\": \"العفو.\"},"` | — |
| [SRC-EA6EC52573-L000089](../../tests/test_intent_router.py#L89) | 89 | `"    ]"` | — |
| [SRC-EA6EC52573-L000090](../../tests/test_intent_router.py#L90) | 90 | `"    decision = route_intent(\"كام سعرها؟\", history, requires_web=True)"` | — |
| [SRC-EA6EC52573-L000091](../../tests/test_intent_router.py#L91) | 91 | `"    assert decision[\"route\"] == \"CLARIFY\""` | — |
| [SRC-EA6EC52573-L000092](../../tests/test_intent_router.py#L92) | 92 | `"    assert decision[\"context_available\"] is False"` | — |
| [SRC-EA6EC52573-L000093](../../tests/test_intent_router.py#L93) | 93 | `""` | — |
| [SRC-EA6EC52573-L000094](../../tests/test_intent_router.py#L94) | 94 | `""` | — |
| [SRC-EA6EC52573-L000095](../../tests/test_intent_router.py#L95) | 95 | `"def test_explicit_mode_overrides_conversational_shortcuts() -> None:"` | — |
| [SRC-EA6EC52573-L000096](../../tests/test_intent_router.py#L96) | 96 | `"    assert route_intent(\"ازيك؟\", mode=\"deep\")[\"route\"] == \"WEB_DEEP\""` | — |
| [SRC-EA6EC52573-L000097](../../tests/test_intent_router.py#L97) | 97 | `"    assert route_intent(\"ما سعر الهاتف؟\", mode=\"latest\")[\"route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-EA6EC52573-L000098](../../tests/test_intent_router.py#L98) | 98 | `""` | — |
| [SRC-EA6EC52573-L000099](../../tests/test_intent_router.py#L99) | 99 | `""` | — |
| [SRC-EA6EC52573-L000100](../../tests/test_intent_router.py#L100) | 100 | `"@pytest.mark.parametrize("` | — |
| [SRC-EA6EC52573-L000101](../../tests/test_intent_router.py#L101) | 101 | `"    (\"question\", \"expected_route\", \"expected_reason\"),"` | — |
| [SRC-EA6EC52573-L000102](../../tests/test_intent_router.py#L102) | 102 | `"    ["` | — |
| [SRC-EA6EC52573-L000103](../../tests/test_intent_router.py#L103) | 103 | `"        ("` | — |
| [SRC-EA6EC52573-L000104](../../tests/test_intent_router.py#L104) | 104 | `"            \"لخص الصفحة https://example.com/article\","` | — |
| [SRC-EA6EC52573-L000105](../../tests/test_intent_router.py#L105) | 105 | `"            \"WEB_SIMPLE\","` | — |
| [SRC-EA6EC52573-L000106](../../tests/test_intent_router.py#L106) | 106 | `"            \"summarization_request\","` | — |
| [SRC-EA6EC52573-L000107](../../tests/test_intent_router.py#L107) | 107 | `"        ),"` | — |
| [SRC-EA6EC52573-L000108](../../tests/test_intent_router.py#L108) | 108 | `"        ("` | — |
| [SRC-EA6EC52573-L000109](../../tests/test_intent_router.py#L109) | 109 | `"            \"Summarize this page https://example.com/article\","` | — |
| [SRC-EA6EC52573-L000110](../../tests/test_intent_router.py#L110) | 110 | `"            \"WEB_SIMPLE\","` | — |
| [SRC-EA6EC52573-L000111](../../tests/test_intent_router.py#L111) | 111 | `"            \"summarization_request\","` | — |
| [SRC-EA6EC52573-L000112](../../tests/test_intent_router.py#L112) | 112 | `"        ),"` | — |
| [SRC-EA6EC52573-L000113](../../tests/test_intent_router.py#L113) | 113 | `"        (\"لخص الصفحة\", \"CLARIFY\", \"missing_summarization_input\"),"` | — |
| [SRC-EA6EC52573-L000114](../../tests/test_intent_router.py#L114) | 114 | `"        (\"لخص لي هذا الرابط\", \"CLARIFY\", \"missing_summarization_input\"),"` | — |
| [SRC-EA6EC52573-L000115](../../tests/test_intent_router.py#L115) | 115 | `"        (\"summarize the page\", \"CLARIFY\", \"missing_summarization_input\"),"` | — |
| [SRC-EA6EC52573-L000116](../../tests/test_intent_router.py#L116) | 116 | `"        (\"تلخيص المقال\", \"CLARIFY\", \"missing_summarization_input\"),"` | — |
| [SRC-EA6EC52573-L000117](../../tests/test_intent_router.py#L117) | 117 | `"        (\"لخص النص التالي: هذا نص تجريبي\", \"MODEL_ONLY\", \"stable_knowledge_or_conversation\"),"` | — |
| [SRC-EA6EC52573-L000118](../../tests/test_intent_router.py#L118) | 118 | `"        (\"Summarize this text: the test content is here\", \"MODEL_ONLY\", \"stable_knowledge_or_conversation\"),"` | — |
| [SRC-EA6EC52573-L000119](../../tests/test_intent_router.py#L119) | 119 | `"    ],"` | — |
| [SRC-EA6EC52573-L000120](../../tests/test_intent_router.py#L120) | 120 | `")"` | — |
| [SRC-EA6EC52573-L000121](../../tests/test_intent_router.py#L121) | 121 | `"def test_summarization_routing_respects_page_text_and_missing_input("` | — |
| [SRC-EA6EC52573-L000122](../../tests/test_intent_router.py#L122) | 122 | `"    question: str, expected_route: str, expected_reason: str"` | — |
| [SRC-EA6EC52573-L000123](../../tests/test_intent_router.py#L123) | 123 | `") -> None:"` | — |
| [SRC-EA6EC52573-L000124](../../tests/test_intent_router.py#L124) | 124 | `"    decision = route_intent(question, [])"` | — |
| [SRC-EA6EC52573-L000125](../../tests/test_intent_router.py#L125) | 125 | `"    assert decision[\"route\"] == expected_route"` | — |
| [SRC-EA6EC52573-L000126](../../tests/test_intent_router.py#L126) | 126 | `"    assert decision[\"reason\"] == expected_reason"` | — |
| [SRC-EA6EC52573-L000127](../../tests/test_intent_router.py#L127) | 127 | `""` | — |
| [SRC-EA6EC52573-L000128](../../tests/test_intent_router.py#L128) | 128 | `""` | — |
| [SRC-EA6EC52573-L000129](../../tests/test_intent_router.py#L129) | 129 | `"@pytest.mark.parametrize("` | — |
| [SRC-EA6EC52573-L000130](../../tests/test_intent_router.py#L130) | 130 | `"    \"question\","` | — |
| [SRC-EA6EC52573-L000131](../../tests/test_intent_router.py#L131) | 131 | `"    ["` | — |
| [SRC-EA6EC52573-L000132](../../tests/test_intent_router.py#L132) | 132 | `"        \"فين؟\","` | — |
| [SRC-EA6EC52573-L000133](../../tests/test_intent_router.py#L133) | 133 | `"        \"فين هي؟\","` | — |
| [SRC-EA6EC52573-L000134](../../tests/test_intent_router.py#L134) | 134 | `"        \"مكانها فين؟\","` | — |
| [SRC-EA6EC52573-L000135](../../tests/test_intent_router.py#L135) | 135 | `"        \"هل فيه ضمان؟\","` | — |
| [SRC-EA6EC52573-L000136](../../tests/test_intent_router.py#L136) | 136 | `"        \"هل لها ضمان؟\","` | — |
| [SRC-EA6EC52573-L000137](../../tests/test_intent_router.py#L137) | 137 | `"        \"ضمانها إيه؟\","` | — |
| [SRC-EA6EC52573-L000138](../../tests/test_intent_router.py#L138) | 138 | `"        \"Where is it?\","` | — |
| [SRC-EA6EC52573-L000139](../../tests/test_intent_router.py#L139) | 139 | `"        \"Does it have a warranty?\","` | — |
| [SRC-EA6EC52573-L000140](../../tests/test_intent_router.py#L140) | 140 | `"    ],"` | — |
| [SRC-EA6EC52573-L000141](../../tests/test_intent_router.py#L141) | 141 | `")"` | — |
| [SRC-EA6EC52573-L000142](../../tests/test_intent_router.py#L142) | 142 | `"def test_missing_referent_questions_clarify_without_context(question: str) -> None:"` | — |
| [SRC-EA6EC52573-L000143](../../tests/test_intent_router.py#L143) | 143 | `"    decision = route_intent(question, history=None, mode=\"auto\", requires_web=True)"` | — |
| [SRC-EA6EC52573-L000144](../../tests/test_intent_router.py#L144) | 144 | `"    assert decision[\"route\"] == \"CLARIFY\""` | — |
| [SRC-EA6EC52573-L000145](../../tests/test_intent_router.py#L145) | 145 | `"    assert decision[\"needs_clarification\"] is True"` | — |
| [SRC-EA6EC52573-L000146](../../tests/test_intent_router.py#L146) | 146 | `"    assert decision[\"context_available\"] is False"` | — |
| [SRC-EA6EC52573-L000147](../../tests/test_intent_router.py#L147) | 147 | `""` | — |
| [SRC-EA6EC52573-L000148](../../tests/test_intent_router.py#L148) | 148 | `""` | — |
| [SRC-EA6EC52573-L000149](../../tests/test_intent_router.py#L149) | 149 | `"@pytest.mark.parametrize(\"question\", [\"فين؟\", \"هل فيه ضمان؟\", \"كام سعرها؟\"])"` | — |
| [SRC-EA6EC52573-L000150](../../tests/test_intent_router.py#L150) | 150 | `"def test_missing_referent_still_clarifies_in_explicit_search_mode(question: str) -> None:"` | — |
| [SRC-EA6EC52573-L000151](../../tests/test_intent_router.py#L151) | 151 | `"    decision = route_intent(question, history=None, mode=\"deep\")"` | — |
| [SRC-EA6EC52573-L000152](../../tests/test_intent_router.py#L152) | 152 | `"    assert decision[\"route\"] == \"CLARIFY\""` | — |
| [SRC-EA6EC52573-L000153](../../tests/test_intent_router.py#L153) | 153 | `"    assert decision[\"needs_clarification\"] is True"` | — |
| [SRC-EA6EC52573-L000154](../../tests/test_intent_router.py#L154) | 154 | `""` | — |
| [SRC-EA6EC52573-L000155](../../tests/test_intent_router.py#L155) | 155 | `""` | — |
| [SRC-EA6EC52573-L000156](../../tests/test_intent_router.py#L156) | 156 | `"def test_followup_resolver_uses_topic_from_latest_user_turn() -> None:"` | — |
| [SRC-EA6EC52573-L000157](../../tests/test_intent_router.py#L157) | 157 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000158](../../tests/test_intent_router.py#L158) | 158 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر آيفون 16 في مصر\"},"` | — |
| [SRC-EA6EC52573-L000159](../../tests/test_intent_router.py#L159) | 159 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن معلومات موثوقة.\"},"` | — |
| [SRC-EA6EC52573-L000160](../../tests/test_intent_router.py#L160) | 160 | `"    ]"` | — |
| [SRC-EA6EC52573-L000161](../../tests/test_intent_router.py#L161) | 161 | `"    resolved = resolve_followup_query(\"هل فيه ضمان؟\", history)"` | — |
| [SRC-EA6EC52573-L000162](../../tests/test_intent_router.py#L162) | 162 | `"    assert \"آيفون 16\" in resolved"` | — |
| [SRC-EA6EC52573-L000163](../../tests/test_intent_router.py#L163) | 163 | `"    assert \"ضمان\" in resolved"` | — |
| [SRC-EA6EC52573-L000164](../../tests/test_intent_router.py#L164) | 164 | `""` | — |
| [SRC-EA6EC52573-L000165](../../tests/test_intent_router.py#L165) | 165 | `""` | — |
| [SRC-EA6EC52573-L000166](../../tests/test_intent_router.py#L166) | 166 | `"def test_followup_resolver_does_not_resurrect_topic_after_acknowledgment() -> None:"` | — |
| [SRC-EA6EC52573-L000167](../../tests/test_intent_router.py#L167) | 167 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000168](../../tests/test_intent_router.py#L168) | 168 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر آيفون 16 في مصر\"},"` | — |
| [SRC-EA6EC52573-L000169](../../tests/test_intent_router.py#L169) | 169 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن معلومات موثوقة.\"},"` | — |
| [SRC-EA6EC52573-L000170](../../tests/test_intent_router.py#L170) | 170 | `"        {\"role\": \"user\", \"content\": \"شكرًا\"},"` | — |
| [SRC-EA6EC52573-L000171](../../tests/test_intent_router.py#L171) | 171 | `"        {\"role\": \"assistant\", \"content\": \"العفو.\"},"` | — |
| [SRC-EA6EC52573-L000172](../../tests/test_intent_router.py#L172) | 172 | `"    ]"` | — |
| [SRC-EA6EC52573-L000173](../../tests/test_intent_router.py#L173) | 173 | `"    assert resolve_followup_query(\"فين؟\", history) == \"فين؟\""` | — |
| [SRC-EA6EC52573-L000174](../../tests/test_intent_router.py#L174) | 174 | `""` | — |
| [SRC-EA6EC52573-L000175](../../tests/test_intent_router.py#L175) | 175 | `""` | — |
| [SRC-EA6EC52573-L000176](../../tests/test_intent_router.py#L176) | 176 | `"def test_followup_resolver_bounds_output_and_handles_malformed_history() -> None:"` | — |
| [SRC-EA6EC52573-L000177](../../tests/test_intent_router.py#L177) | 177 | `"    history = [{\"role\": \"user\", \"content\": \"س\" * 4000}]"` | — |
| [SRC-EA6EC52573-L000178](../../tests/test_intent_router.py#L178) | 178 | `"    assert len(resolve_followup_query(\"والسعر؟\", history)) <= 500"` | — |
| [SRC-EA6EC52573-L000179](../../tests/test_intent_router.py#L179) | 179 | `"    assert resolve_followup_query(\"فين؟\", {\"role\": \"user\", \"content\": \"topic\"}) == \"فين؟\""` | — |
| [SRC-EA6EC52573-L000180](../../tests/test_intent_router.py#L180) | 180 | `""` | — |
| [SRC-EA6EC52573-L000181](../../tests/test_intent_router.py#L181) | 181 | `"def test_prefixed_elliptical_followup_is_clarified_without_topic():"` | — |
| [SRC-EA6EC52573-L000182](../../tests/test_intent_router.py#L182) | 182 | `"    for question in (\"طب هل فيه ضمان؟\", \"طيب كام سعرها؟\", \"والضمان؟\", \"والسعر؟\"):"` | — |
| [SRC-EA6EC52573-L000183](../../tests/test_intent_router.py#L183) | 183 | `"        decision = route_intent(question)"` | — |
| [SRC-EA6EC52573-L000184](../../tests/test_intent_router.py#L184) | 184 | `"        assert decision[\"route\"] == \"CLARIFY\", question"` | — |
| [SRC-EA6EC52573-L000185](../../tests/test_intent_router.py#L185) | 185 | `""` | — |
| [SRC-EA6EC52573-L000186](../../tests/test_intent_router.py#L186) | 186 | `"def test_prefixed_elliptical_followup_uses_topic_when_available():"` | — |
| [SRC-EA6EC52573-L000187](../../tests/test_intent_router.py#L187) | 187 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000188](../../tests/test_intent_router.py#L188) | 188 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر iPhone 16 في مصر\"},"` | — |
| [SRC-EA6EC52573-L000189](../../tests/test_intent_router.py#L189) | 189 | `"        {\"role\": \"assistant\", \"content\": \"نتحدث عن iPhone 16 في مصر.\"},"` | — |
| [SRC-EA6EC52573-L000190](../../tests/test_intent_router.py#L190) | 190 | `"    ]"` | — |
| [SRC-EA6EC52573-L000191](../../tests/test_intent_router.py#L191) | 191 | `"    for question in (\"طب هل فيه ضمان؟\", \"طيب كام سعرها؟\", \"والضمان؟\"):"` | — |
| [SRC-EA6EC52573-L000192](../../tests/test_intent_router.py#L192) | 192 | `"        decision = route_intent(question, history, requires_web=True)"` | — |
| [SRC-EA6EC52573-L000193](../../tests/test_intent_router.py#L193) | 193 | `"        assert decision[\"route\"] == \"WEB_SIMPLE\", question"` | — |
| [SRC-EA6EC52573-L000194](../../tests/test_intent_router.py#L194) | 194 | `"        resolved = resolve_followup_query(question, history)"` | — |
| [SRC-EA6EC52573-L000195](../../tests/test_intent_router.py#L195) | 195 | `"        assert \"iPhone 16\" in resolved"` | — |
| [SRC-EA6EC52573-L000196](../../tests/test_intent_router.py#L196) | 196 | `"        assert \"مصر\" in resolved"` | — |
| [SRC-EA6EC52573-L000197](../../tests/test_intent_router.py#L197) | 197 | `""` | — |
| [SRC-EA6EC52573-L000198](../../tests/test_intent_router.py#L198) | 198 | `"def test_long_arabic_warranty_followup_resolves_with_context():"` | — |
| [SRC-EA6EC52573-L000199](../../tests/test_intent_router.py#L199) | 199 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000200](../../tests/test_intent_router.py#L200) | 200 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر iPhone 17 نسخة 256 جيجابايت في مصر\"},"` | — |
| [SRC-EA6EC52573-L000201](../../tests/test_intent_router.py#L201) | 201 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن السعر.\"},"` | — |
| [SRC-EA6EC52573-L000202](../../tests/test_intent_router.py#L202) | 202 | `"    ]"` | — |
| [SRC-EA6EC52573-L000203](../../tests/test_intent_router.py#L203) | 203 | `"    question = \"وطب الضمان الدولي بيسري في مصر؟\""` | — |
| [SRC-EA6EC52573-L000204](../../tests/test_intent_router.py#L204) | 204 | `"    resolved = resolve_followup_query(question, history)"` | — |
| [SRC-EA6EC52573-L000205](../../tests/test_intent_router.py#L205) | 205 | `"    assert \"iPhone 17\" in resolved"` | — |
| [SRC-EA6EC52573-L000206](../../tests/test_intent_router.py#L206) | 206 | `"    assert question in resolved"` | — |
| [SRC-EA6EC52573-L000207](../../tests/test_intent_router.py#L207) | 207 | `""` | — |
| [SRC-EA6EC52573-L000208](../../tests/test_intent_router.py#L208) | 208 | `"def test_long_arabic_warranty_followup_without_context_clarifies():"` | — |
| [SRC-EA6EC52573-L000209](../../tests/test_intent_router.py#L209) | 209 | `"    question = \"وطب الضمان الدولي بيسري في مصر؟\""` | — |
| [SRC-EA6EC52573-L000210](../../tests/test_intent_router.py#L210) | 210 | `"    decision = route_intent(question)"` | — |
| [SRC-EA6EC52573-L000211](../../tests/test_intent_router.py#L211) | 211 | `"    assert decision[\"route\"] == \"CLARIFY\""` | — |
| [SRC-EA6EC52573-L000212](../../tests/test_intent_router.py#L212) | 212 | `"    assert decision[\"needs_clarification\"] is True"` | — |
| [SRC-EA6EC52573-L000213](../../tests/test_intent_router.py#L213) | 213 | `""` | — |
| [SRC-EA6EC52573-L000214](../../tests/test_intent_router.py#L214) | 214 | `"def test_new_question_starting_with_tayyib_does_not_inherit_old_topic():"` | — |
| [SRC-EA6EC52573-L000215](../../tests/test_intent_router.py#L215) | 215 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000216](../../tests/test_intent_router.py#L216) | 216 | `"        {\"role\": \"user\", \"content\": \"ما سعر iPhone 16 في مصر؟\"},"` | — |
| [SRC-EA6EC52573-L000217](../../tests/test_intent_router.py#L217) | 217 | `"        {\"role\": \"assistant\", \"content\": \"هذه بعض معلومات السعر.\"},"` | — |
| [SRC-EA6EC52573-L000218](../../tests/test_intent_router.py#L218) | 218 | `"    ]"` | — |
| [SRC-EA6EC52573-L000219](../../tests/test_intent_router.py#L219) | 219 | `"    question = \"طيب اشرح الذكاء الاصطناعي في المدارس\""` | — |
| [SRC-EA6EC52573-L000220](../../tests/test_intent_router.py#L220) | 220 | `"    assert resolve_followup_query(question, history) == question"` | — |
| [SRC-EA6EC52573-L000221](../../tests/test_intent_router.py#L221) | 221 | `"    decision = route_intent(question, history)"` | — |
| [SRC-EA6EC52573-L000222](../../tests/test_intent_router.py#L222) | 222 | `"    assert decision[\"route\"] == \"MODEL_ONLY\""` | — |
| [SRC-EA6EC52573-L000223](../../tests/test_intent_router.py#L223) | 223 | `""` | — |
| [SRC-EA6EC52573-L000224](../../tests/test_intent_router.py#L224) | 224 | `"def test_chained_followups_keep_the_last_substantive_topic():"` | — |
| [SRC-EA6EC52573-L000225](../../tests/test_intent_router.py#L225) | 225 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000226](../../tests/test_intent_router.py#L226) | 226 | `"        {\"role\": \"user\", \"content\": \"ما سعر iPhone 16 في مصر؟\"},"` | — |
| [SRC-EA6EC52573-L000227](../../tests/test_intent_router.py#L227) | 227 | `"        {\"role\": \"assistant\", \"content\": \"السعر يختلف حسب المتجر.\"},"` | — |
| [SRC-EA6EC52573-L000228](../../tests/test_intent_router.py#L228) | 228 | `"        {\"role\": \"user\", \"content\": \"والضمان؟\"},"` | — |
| [SRC-EA6EC52573-L000229](../../tests/test_intent_router.py#L229) | 229 | `"        {\"role\": \"assistant\", \"content\": \"سأوضح الضمان.\"},"` | — |
| [SRC-EA6EC52573-L000230](../../tests/test_intent_router.py#L230) | 230 | `"    ]"` | — |
| [SRC-EA6EC52573-L000231](../../tests/test_intent_router.py#L231) | 231 | `"    resolved = resolve_followup_query(\"والبطارية؟\", history)"` | — |
| [SRC-EA6EC52573-L000232](../../tests/test_intent_router.py#L232) | 232 | `"    assert \"iPhone 16\" in resolved"` | — |
| [SRC-EA6EC52573-L000233](../../tests/test_intent_router.py#L233) | 233 | `"    assert \"البطارية\" in resolved"` | — |
| [SRC-EA6EC52573-L000234](../../tests/test_intent_router.py#L234) | 234 | `""` | — |
| [SRC-EA6EC52573-L000235](../../tests/test_intent_router.py#L235) | 235 | `"def test_answer_to_clarification_restores_original_intent():"` | — |
| [SRC-EA6EC52573-L000236](../../tests/test_intent_router.py#L236) | 236 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000237](../../tests/test_intent_router.py#L237) | 237 | `"        {\"role\": \"user\", \"content\": \"كام سعرها؟\"},"` | — |
| [SRC-EA6EC52573-L000238](../../tests/test_intent_router.py#L238) | 238 | `"        {"` | — |
| [SRC-EA6EC52573-L000239](../../tests/test_intent_router.py#L239) | 239 | `"            \"role\": \"assistant\","` | — |
| [SRC-EA6EC52573-L000240](../../tests/test_intent_router.py#L240) | 240 | `"            \"content\": \"تقصد إيه تحديدًا؟ اكتب اسم الشيء أو المنتج المقصود، أو ابعت الرابط، وأكمل معاك من غير ما أخمّن.\","` | — |
| [SRC-EA6EC52573-L000241](../../tests/test_intent_router.py#L241) | 241 | `"        },"` | — |
| [SRC-EA6EC52573-L000242](../../tests/test_intent_router.py#L242) | 242 | `"    ]"` | — |
| [SRC-EA6EC52573-L000243](../../tests/test_intent_router.py#L243) | 243 | `"    decision = route_intent(\"iPhone 16\", history)"` | — |
| [SRC-EA6EC52573-L000244](../../tests/test_intent_router.py#L244) | 244 | `"    assert decision[\"route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-EA6EC52573-L000245](../../tests/test_intent_router.py#L245) | 245 | `"    assert decision[\"reason\"] == \"answer_to_pending_clarification\""` | — |
| [SRC-EA6EC52573-L000246](../../tests/test_intent_router.py#L246) | 246 | `"    resolved = resolve_followup_query(\"iPhone 16\", history)"` | — |
| [SRC-EA6EC52573-L000247](../../tests/test_intent_router.py#L247) | 247 | `"    assert \"سعرها\" in resolved"` | — |
| [SRC-EA6EC52573-L000248](../../tests/test_intent_router.py#L248) | 248 | `"    assert \"iPhone 16\" in resolved"` | — |
| [SRC-EA6EC52573-L000249](../../tests/test_intent_router.py#L249) | 249 | `""` | — |
| [SRC-EA6EC52573-L000250](../../tests/test_intent_router.py#L250) | 250 | `"def test_topic_detection_does_not_inherit_old_social_or_depth_intent():"` | — |
| [SRC-EA6EC52573-L000251](../../tests/test_intent_router.py#L251) | 251 | `"    from agents.research import fallback_plan"` | — |
| [SRC-EA6EC52573-L000252](../../tests/test_intent_router.py#L252) | 252 | `""` | — |
| [SRC-EA6EC52573-L000253](../../tests/test_intent_router.py#L253) | 253 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000254](../../tests/test_intent_router.py#L254) | 254 | `"        {\"role\": \"user\", \"content\": \"اجمع آراء مستخدمي السيارات الكهربائية على Reddit\"},"` | — |
| [SRC-EA6EC52573-L000255](../../tests/test_intent_router.py#L255) | 255 | `"        {\"role\": \"assistant\", \"content\": \"هذه النتائج.\"},"` | — |
| [SRC-EA6EC52573-L000256](../../tests/test_intent_router.py#L256) | 256 | `"    ]"` | — |
| [SRC-EA6EC52573-L000257](../../tests/test_intent_router.py#L257) | 257 | `"    plan = fallback_plan(\"اشرح طريقة عمل المحرك الكهربائي\", history)"` | — |
| [SRC-EA6EC52573-L000258](../../tests/test_intent_router.py#L258) | 258 | `"    assert plan[\"social_focus\"] is False"` | — |
| [SRC-EA6EC52573-L000259](../../tests/test_intent_router.py#L259) | 259 | `"    assert plan[\"platforms\"] == []"` | — |
| [SRC-EA6EC52573-L000260](../../tests/test_intent_router.py#L260) | 260 | `"    assert plan[\"depth\"] == \"standard\""` | — |
| [SRC-EA6EC52573-L000261](../../tests/test_intent_router.py#L261) | 261 | `""` | — |
| [SRC-EA6EC52573-L000262](../../tests/test_intent_router.py#L262) | 262 | `"def test_explicit_request_for_reliable_sources_uses_web_search_in_auto_mode():"` | — |
| [SRC-EA6EC52573-L000263](../../tests/test_intent_router.py#L263) | 263 | `"    question = ("` | — |
| [SRC-EA6EC52573-L000264](../../tests/test_intent_router.py#L264) | 264 | `"        \"ما أهم استخدامات الذكاء الاصطناعي في الشركات الصغيرة؟ \""` | — |
| [SRC-EA6EC52573-L000265](../../tests/test_intent_router.py#L265) | 265 | `"        \"اذكر أمثلة ومصادر موثوقة.\""` | — |
| [SRC-EA6EC52573-L000266](../../tests/test_intent_router.py#L266) | 266 | `"    )"` | — |
| [SRC-EA6EC52573-L000267](../../tests/test_intent_router.py#L267) | 267 | `"    decision = route_intent(question, mode=\"auto\")"` | — |
| [SRC-EA6EC52573-L000268](../../tests/test_intent_router.py#L268) | 268 | `"    assert decision[\"route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-EA6EC52573-L000269](../../tests/test_intent_router.py#L269) | 269 | `"    assert decision[\"reason\"] == \"explicit_evidence_request\""` | — |
| [SRC-EA6EC52573-L000270](../../tests/test_intent_router.py#L270) | 270 | `""` | — |
| [SRC-EA6EC52573-L000271](../../tests/test_intent_router.py#L271) | 271 | `"def test_stable_question_without_source_request_remains_model_only():"` | — |
| [SRC-EA6EC52573-L000272](../../tests/test_intent_router.py#L272) | 272 | `"    decision = route_intent(\"اشرح الفرق بين التعلم الخاضع للإشراف وغير الخاضع للإشراف\")"` | — |
| [SRC-EA6EC52573-L000273](../../tests/test_intent_router.py#L273) | 273 | `"    assert decision[\"route\"] == \"MODEL_ONLY\""` | — |
| [SRC-EA6EC52573-L000274](../../tests/test_intent_router.py#L274) | 274 | `""` | — |
| [SRC-EA6EC52573-L000275](../../tests/test_intent_router.py#L275) | 275 | `"def test_attached_arabic_object_pronoun_resolves_against_previous_subject() -> None:"` | — |
| [SRC-EA6EC52573-L000276](../../tests/test_intent_router.py#L276) | 276 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000277](../../tests/test_intent_router.py#L277) | 277 | `"        {\"role\": \"user\", \"content\": \"بفكر أشتري Lenovo ThinkPad E14 في مصر\"},"` | — |
| [SRC-EA6EC52573-L000278](../../tests/test_intent_router.py#L278) | 278 | `"        {\"role\": \"assistant\", \"content\": \"نتحدث عن Lenovo ThinkPad E14 في السوق المصري.\"},"` | — |
| [SRC-EA6EC52573-L000279](../../tests/test_intent_router.py#L279) | 279 | `"    ]"` | — |
| [SRC-EA6EC52573-L000280](../../tests/test_intent_router.py#L280) | 280 | `""` | — |
| [SRC-EA6EC52573-L000281](../../tests/test_intent_router.py#L281) | 281 | `"    resolved = resolve_followup_query(\"أقدر أشتريه منين؟\", history)"` | — |
| [SRC-EA6EC52573-L000282](../../tests/test_intent_router.py#L282) | 282 | `""` | — |
| [SRC-EA6EC52573-L000283](../../tests/test_intent_router.py#L283) | 283 | `"    assert \"Lenovo ThinkPad E14\" in resolved"` | — |
| [SRC-EA6EC52573-L000284](../../tests/test_intent_router.py#L284) | 284 | `"    assert \"أقدر أشتريه منين\" in resolved"` | — |
| [SRC-EA6EC52573-L000285](../../tests/test_intent_router.py#L285) | 285 | `""` | — |
| [SRC-EA6EC52573-L000286](../../tests/test_intent_router.py#L286) | 286 | `"def test_no_duplicate_followup_leadin_symbols():"` | — |
| [SRC-EA6EC52573-L000287](../../tests/test_intent_router.py#L287) | 287 | `"    \"\"\"Follow-up normalization symbols must have one authoritative definition.\"\"\""` | — |
| [SRC-EA6EC52573-L000288](../../tests/test_intent_router.py#L288) | 288 | `"    import inspect"` | — |
| [SRC-EA6EC52573-L000289](../../tests/test_intent_router.py#L289) | 289 | `"    from agents import intent_router"` | — |
| [SRC-EA6EC52573-L000290](../../tests/test_intent_router.py#L290) | 290 | `""` | — |
| [SRC-EA6EC52573-L000291](../../tests/test_intent_router.py#L291) | 291 | `"    module_source = inspect.getsource(intent_router)"` | — |
| [SRC-EA6EC52573-L000292](../../tests/test_intent_router.py#L292) | 292 | `"    assert module_source.count(\"_FOLLOWUP_LEAD_IN_RE = re.compile\") == 1"` | — |
| [SRC-EA6EC52573-L000293](../../tests/test_intent_router.py#L293) | 293 | `"    assert module_source.count(\"_FOLLOWUP_ASPECT_FRAGMENTS = frozenset\") == 1"` | — |
| [SRC-EA6EC52573-L000294](../../tests/test_intent_router.py#L294) | 294 | `"    assert module_source.count(\"def _strip_followup_leadin\") == 1"` | — |
| [SRC-EA6EC52573-L000295](../../tests/test_intent_router.py#L295) | 295 | `""` | — |
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
| [SRC-4397BC2CD2-L000063](../../tests/test_intent_router_integration.py#L63) | 63 | `"    agent = WebAgent()"` | — |
| [SRC-4397BC2CD2-L000064](../../tests/test_intent_router_integration.py#L64) | 64 | `""` | — |
| [SRC-4397BC2CD2-L000065](../../tests/test_intent_router_integration.py#L65) | 65 | `"    def unexpected(*args, **kwargs):"` | — |
| [SRC-4397BC2CD2-L000066](../../tests/test_intent_router_integration.py#L66) | 66 | `"        pytest.fail(\"An unresolved referent must be clarified without model/search.\")"` | — |
| [SRC-4397BC2CD2-L000067](../../tests/test_intent_router_integration.py#L67) | 67 | `""` | — |
| [SRC-4397BC2CD2-L000068](../../tests/test_intent_router_integration.py#L68) | 68 | `"    monkeypatch.setattr(agent, \"_answer_without_search\", unexpected)"` | — |
| [SRC-4397BC2CD2-L000069](../../tests/test_intent_router_integration.py#L69) | 69 | `"    monkeypatch.setattr(agent, \"_plan_search\", unexpected)"` | — |
| [SRC-4397BC2CD2-L000070](../../tests/test_intent_router_integration.py#L70) | 70 | `"    monkeypatch.setattr(agent, \"_collect_research\", unexpected)"` | — |
| [SRC-4397BC2CD2-L000071](../../tests/test_intent_router_integration.py#L71) | 71 | `""` | — |
| [SRC-4397BC2CD2-L000072](../../tests/test_intent_router_integration.py#L72) | 72 | `"    result = agent.answer(\"كام سعرها؟\")"` | — |
| [SRC-4397BC2CD2-L000073](../../tests/test_intent_router_integration.py#L73) | 73 | `""` | — |
| [SRC-4397BC2CD2-L000074](../../tests/test_intent_router_integration.py#L74) | 74 | `"    assert result[\"kind\"] == \"clarification_needed\""` | — |
| [SRC-4397BC2CD2-L000075](../../tests/test_intent_router_integration.py#L75) | 75 | `"    assert result[\"intent_route\"] == \"CLARIFY\""` | — |
| [SRC-4397BC2CD2-L000076](../../tests/test_intent_router_integration.py#L76) | 76 | `"    assert result[\"research_plan\"][\"intent_route\"] == \"CLARIFY\""` | — |
| [SRC-4397BC2CD2-L000077](../../tests/test_intent_router_integration.py#L77) | 77 | `"    assert \"تقصد\" in result[\"answer\"]"` | — |
| [SRC-4397BC2CD2-L000078](../../tests/test_intent_router_integration.py#L78) | 78 | `"    assert result[\"used_web_search\"] is False"` | — |
| [SRC-4397BC2CD2-L000079](../../tests/test_intent_router_integration.py#L79) | 79 | `"    assert result[\"used_language_model\"] is False"` | — |
| [SRC-4397BC2CD2-L000080](../../tests/test_intent_router_integration.py#L80) | 80 | `"    assert result[\"sources\"] == []"` | — |
| [SRC-4397BC2CD2-L000081](../../tests/test_intent_router_integration.py#L81) | 81 | `""` | — |
| [SRC-4397BC2CD2-L000082](../../tests/test_intent_router_integration.py#L82) | 82 | `""` | — |
| [SRC-4397BC2CD2-L000083](../../tests/test_intent_router_integration.py#L83) | 83 | `"def test_contextual_price_followup_searches_with_previous_subject(monkeypatch) -> None:"` | — |
| [SRC-4397BC2CD2-L000084](../../tests/test_intent_router_integration.py#L84) | 84 | `"    agent = WebAgent()"` | — |
| [SRC-4397BC2CD2-L000085](../../tests/test_intent_router_integration.py#L85) | 85 | `"    agent.api_key = \"\"  # Keep this acceptance test deterministic and offline."` | — |
| [SRC-4397BC2CD2-L000086](../../tests/test_intent_router_integration.py#L86) | 86 | `"    seen: dict = {}"` | — |
| [SRC-4397BC2CD2-L000087](../../tests/test_intent_router_integration.py#L87) | 87 | `"    history = ["` | — |
| [SRC-4397BC2CD2-L000088](../../tests/test_intent_router_integration.py#L88) | 88 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر iPhone 17 في مصر\"},"` | — |
| [SRC-4397BC2CD2-L000089](../../tests/test_intent_router_integration.py#L89) | 89 | `"        {\"role\": \"assistant\", \"content\": \"نتحدث عن هاتف iPhone 17 في السوق المصري.\"},"` | — |
| [SRC-4397BC2CD2-L000090](../../tests/test_intent_router_integration.py#L90) | 90 | `"    ]"` | — |
| [SRC-4397BC2CD2-L000091](../../tests/test_intent_router_integration.py#L91) | 91 | `""` | — |
| [SRC-4397BC2CD2-L000092](../../tests/test_intent_router_integration.py#L92) | 92 | `"    def collect(plan):"` | — |
| [SRC-4397BC2CD2-L000093](../../tests/test_intent_router_integration.py#L93) | 93 | `"        seen[\"plan\"] = dict(plan)"` | — |
| [SRC-4397BC2CD2-L000094](../../tests/test_intent_router_integration.py#L94) | 94 | `"        sources = ["` | — |
| [SRC-4397BC2CD2-L000095](../../tests/test_intent_router_integration.py#L95) | 95 | `"            _evidence(\"example.com\", plan[\"queries\"]),"` | — |
| [SRC-4397BC2CD2-L000096](../../tests/test_intent_router_integration.py#L96) | 96 | `"            _evidence(\"example.net\", plan[\"queries\"]),"` | — |
| [SRC-4397BC2CD2-L000097](../../tests/test_intent_router_integration.py#L97) | 97 | `"        ]"` | — |
| [SRC-4397BC2CD2-L000098](../../tests/test_intent_router_integration.py#L98) | 98 | `"        return sources, [], _report(plan, sources)"` | — |
| [SRC-4397BC2CD2-L000099](../../tests/test_intent_router_integration.py#L99) | 99 | `""` | — |
| [SRC-4397BC2CD2-L000100](../../tests/test_intent_router_integration.py#L100) | 100 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-4397BC2CD2-L000101](../../tests/test_intent_router_integration.py#L101) | 101 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-4397BC2CD2-L000102](../../tests/test_intent_router_integration.py#L102) | 102 | `"    def generate(resolved_question, *args, **kwargs):"` | — |
| [SRC-4397BC2CD2-L000103](../../tests/test_intent_router_integration.py#L103) | 103 | `"        seen[\"generation_question\"] = resolved_question"` | — |
| [SRC-4397BC2CD2-L000104](../../tests/test_intent_router_integration.py#L104) | 104 | `"        return \"توجد أسعار مختلفة حسب النسخة [المصدر 1].\""` | — |
| [SRC-4397BC2CD2-L000105](../../tests/test_intent_router_integration.py#L105) | 105 | `""` | — |
| [SRC-4397BC2CD2-L000106](../../tests/test_intent_router_integration.py#L106) | 106 | `"    def review(resolved_question, answer, sources):"` | — |
| [SRC-4397BC2CD2-L000107](../../tests/test_intent_router_integration.py#L107) | 107 | `"        seen[\"review_question\"] = resolved_question"` | — |
| [SRC-4397BC2CD2-L000108](../../tests/test_intent_router_integration.py#L108) | 108 | `"        return answer"` | — |
| [SRC-4397BC2CD2-L000109](../../tests/test_intent_router_integration.py#L109) | 109 | `""` | — |
| [SRC-4397BC2CD2-L000110](../../tests/test_intent_router_integration.py#L110) | 110 | `"    monkeypatch.setattr(agent, \"_generate\", generate)"` | — |
| [SRC-4397BC2CD2-L000111](../../tests/test_intent_router_integration.py#L111) | 111 | `"    monkeypatch.setattr(agent, \"_review_answer\", review)"` | — |
| [SRC-4397BC2CD2-L000112](../../tests/test_intent_router_integration.py#L112) | 112 | `""` | — |
| [SRC-4397BC2CD2-L000113](../../tests/test_intent_router_integration.py#L113) | 113 | `"    result = agent.answer(\"كام سعرها؟\", history=history)"` | — |
| [SRC-4397BC2CD2-L000114](../../tests/test_intent_router_integration.py#L114) | 114 | `""` | — |
| [SRC-4397BC2CD2-L000115](../../tests/test_intent_router_integration.py#L115) | 115 | `"    assert result[\"intent_route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-4397BC2CD2-L000116](../../tests/test_intent_router_integration.py#L116) | 116 | `"    assert result[\"research_plan\"][\"intent_route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-4397BC2CD2-L000117](../../tests/test_intent_router_integration.py#L117) | 117 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-4397BC2CD2-L000118](../../tests/test_intent_router_integration.py#L118) | 118 | `"    assert result[\"citation_validation\"][\"method\"] == \"numeric_source_index_range_only\""` | — |
| [SRC-4397BC2CD2-L000119](../../tests/test_intent_router_integration.py#L119) | 119 | `"    assert result[\"search_report\"][\"citation_validation\"] == result[\"citation_validation\"]"` | — |
| [SRC-4397BC2CD2-L000120](../../tests/test_intent_router_integration.py#L120) | 120 | `"    assert any(\"iPhone 17\" in query for query in seen[\"plan\"][\"queries\"])"` | — |
| [SRC-4397BC2CD2-L000121](../../tests/test_intent_router_integration.py#L121) | 121 | `"    # The plan already resolved the follow-up for search, but historically generation"` | — |
| [SRC-4397BC2CD2-L000122](../../tests/test_intent_router_integration.py#L122) | 122 | `"    # still received only \"كام سعرها؟\". All answer stages must receive the same context."` | — |
| [SRC-4397BC2CD2-L000123](../../tests/test_intent_router_integration.py#L123) | 123 | `"    assert \"iPhone 17\" in seen[\"generation_question\"]"` | — |
| [SRC-4397BC2CD2-L000124](../../tests/test_intent_router_integration.py#L124) | 124 | `"    assert \"كام سعرها\" in seen[\"generation_question\"]"` | — |
| [SRC-4397BC2CD2-L000125](../../tests/test_intent_router_integration.py#L125) | 125 | `"    assert seen[\"review_question\"] == seen[\"generation_question\"]"` | — |
| [SRC-4397BC2CD2-L000126](../../tests/test_intent_router_integration.py#L126) | 126 | `""` | — |
| [SRC-4397BC2CD2-L000127](../../tests/test_intent_router_integration.py#L127) | 127 | `""` | — |
| [SRC-4397BC2CD2-L000128](../../tests/test_intent_router_integration.py#L128) | 128 | `"def test_multi_part_comparison_forces_deep_plan_and_multiple_angles(monkeypatch) -> None:"` | — |
| [SRC-4397BC2CD2-L000129](../../tests/test_intent_router_integration.py#L129) | 129 | `"    agent = WebAgent()"` | — |
| [SRC-4397BC2CD2-L000130](../../tests/test_intent_router_integration.py#L130) | 130 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-4397BC2CD2-L000131](../../tests/test_intent_router_integration.py#L131) | 131 | `"    seen: dict = {\"plans\": []}"` | — |
| [SRC-4397BC2CD2-L000132](../../tests/test_intent_router_integration.py#L132) | 132 | `"    history = []"` | — |
| [SRC-4397BC2CD2-L000133](../../tests/test_intent_router_integration.py#L133) | 133 | `""` | — |
| [SRC-4397BC2CD2-L000134](../../tests/test_intent_router_integration.py#L134) | 134 | `"    def plan(question, prior_history):"` | — |
| [SRC-4397BC2CD2-L000135](../../tests/test_intent_router_integration.py#L135) | 135 | `"        return {"` | — |
| [SRC-4397BC2CD2-L000136](../../tests/test_intent_router_integration.py#L136) | 136 | `"            \"queries\": [\"iPhone 17 versus Samsung S26\"],"` | — |
| [SRC-4397BC2CD2-L000137](../../tests/test_intent_router_integration.py#L137) | 137 | `"            \"direct_urls\": [],"` | — |
| [SRC-4397BC2CD2-L000138](../../tests/test_intent_router_integration.py#L138) | 138 | `"            \"social_focus\": False,"` | — |
| [SRC-4397BC2CD2-L000139](../../tests/test_intent_router_integration.py#L139) | 139 | `"            \"freshness\": \"any\","` | — |
| [SRC-4397BC2CD2-L000140](../../tests/test_intent_router_integration.py#L140) | 140 | `"            \"depth\": \"standard\","` | — |
| [SRC-4397BC2CD2-L000141](../../tests/test_intent_router_integration.py#L141) | 141 | `"            \"platforms\": [],"` | — |
| [SRC-4397BC2CD2-L000142](../../tests/test_intent_router_integration.py#L142) | 142 | `"            \"planning_method\": \"test_single_query\","` | — |
| [SRC-4397BC2CD2-L000143](../../tests/test_intent_router_integration.py#L143) | 143 | `"        }"` | — |
| [SRC-4397BC2CD2-L000144](../../tests/test_intent_router_integration.py#L144) | 144 | `""` | — |
| [SRC-4397BC2CD2-L000145](../../tests/test_intent_router_integration.py#L145) | 145 | `"    def collect(research_plan):"` | — |
| [SRC-4397BC2CD2-L000146](../../tests/test_intent_router_integration.py#L146) | 146 | `"        seen[\"plans\"].append(dict(research_plan))"` | — |
| [SRC-4397BC2CD2-L000147](../../tests/test_intent_router_integration.py#L147) | 147 | `"        sources = ["` | — |
| [SRC-4397BC2CD2-L000148](../../tests/test_intent_router_integration.py#L148) | 148 | `"            _evidence(\"example.com\", research_plan[\"queries\"]),"` | — |
| [SRC-4397BC2CD2-L000149](../../tests/test_intent_router_integration.py#L149) | 149 | `"            _evidence(\"example.net\", research_plan[\"queries\"]),"` | — |
| [SRC-4397BC2CD2-L000150](../../tests/test_intent_router_integration.py#L150) | 150 | `"        ]"` | — |
| [SRC-4397BC2CD2-L000151](../../tests/test_intent_router_integration.py#L151) | 151 | `"        return sources, [], _report(research_plan, sources)"` | — |
| [SRC-4397BC2CD2-L000152](../../tests/test_intent_router_integration.py#L152) | 152 | `""` | — |
| [SRC-4397BC2CD2-L000153](../../tests/test_intent_router_integration.py#L153) | 153 | `"    monkeypatch.setattr(agent, \"_plan_search\", plan)"` | — |
| [SRC-4397BC2CD2-L000154](../../tests/test_intent_router_integration.py#L154) | 154 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-4397BC2CD2-L000155](../../tests/test_intent_router_integration.py#L155) | 155 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-4397BC2CD2-L000156](../../tests/test_intent_router_integration.py#L156) | 156 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"مقارنة أولية [المصدر 1].\")"` | — |
| [SRC-4397BC2CD2-L000157](../../tests/test_intent_router_integration.py#L157) | 157 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-4397BC2CD2-L000158](../../tests/test_intent_router_integration.py#L158) | 158 | `"    monkeypatch.setattr(agent, \"_repair_answer_coverage\", lambda _q, answer, _s, _m: answer)"` | — |
| [SRC-4397BC2CD2-L000159](../../tests/test_intent_router_integration.py#L159) | 159 | `"    monkeypatch.setattr(agent, \"_verify_semantic_claims\", lambda *args, **kwargs: {"` | — |
| [SRC-4397BC2CD2-L000160](../../tests/test_intent_router_integration.py#L160) | 160 | `"        \"status\": \"completed_all_claims_supported\","` | — |
| [SRC-4397BC2CD2-L000161](../../tests/test_intent_router_integration.py#L161) | 161 | `"        \"withhold_answer\": False,"` | — |
| [SRC-4397BC2CD2-L000162](../../tests/test_intent_router_integration.py#L162) | 162 | `"        \"semantic_verification\": \"model_assessed_source_support\","` | — |
| [SRC-4397BC2CD2-L000163](../../tests/test_intent_router_integration.py#L163) | 163 | `"        \"fact_correctness\": \"not_verified\","` | — |
| [SRC-4397BC2CD2-L000164](../../tests/test_intent_router_integration.py#L164) | 164 | `"    })"` | — |
| [SRC-4397BC2CD2-L000165](../../tests/test_intent_router_integration.py#L165) | 165 | `""` | — |
| [SRC-4397BC2CD2-L000166](../../tests/test_intent_router_integration.py#L166) | 166 | `"    result = agent.answer("` | — |
| [SRC-4397BC2CD2-L000167](../../tests/test_intent_router_integration.py#L167) | 167 | `"        \"قارن بين iPhone 17 وSamsung S26 من حيث السعر والبطارية والكاميرا\","` | — |
| [SRC-4397BC2CD2-L000168](../../tests/test_intent_router_integration.py#L168) | 168 | `"        history=history,"` | — |
| [SRC-4397BC2CD2-L000169](../../tests/test_intent_router_integration.py#L169) | 169 | `"    )"` | — |
| [SRC-4397BC2CD2-L000170](../../tests/test_intent_router_integration.py#L170) | 170 | `""` | — |
| [SRC-4397BC2CD2-L000171](../../tests/test_intent_router_integration.py#L171) | 171 | `"    assert result[\"intent_route\"] == \"WEB_DEEP\""` | — |
| [SRC-4397BC2CD2-L000172](../../tests/test_intent_router_integration.py#L172) | 172 | `"    assert result[\"research_plan\"][\"intent_route\"] == \"WEB_DEEP\""` | — |
| [SRC-4397BC2CD2-L000173](../../tests/test_intent_router_integration.py#L173) | 173 | `"    assert result[\"research_plan\"][\"depth\"] == \"deep\""` | — |
| [SRC-4397BC2CD2-L000174](../../tests/test_intent_router_integration.py#L174) | 174 | `"    initial_plan = seen[\"plans\"][0]"` | — |
| [SRC-4397BC2CD2-L000175](../../tests/test_intent_router_integration.py#L175) | 175 | `"    assert len(initial_plan[\"queries\"]) > 1"` | — |
| [SRC-4397BC2CD2-L000176](../../tests/test_intent_router_integration.py#L176) | 176 | `"    assert initial_plan[\"coverage_gap_repair_slot_reserved\"] is True"` | — |
| [SRC-4397BC2CD2-L000177](../../tests/test_intent_router_integration.py#L177) | 177 | `"    assert initial_plan[\"query_limit\"] == 7"` | — |
| [SRC-4397BC2CD2-L000178](../../tests/test_intent_router_integration.py#L178) | 178 | `"    # Each requested criterion gets a distinct search angle before generic deep"` | — |
| [SRC-4397BC2CD2-L000179](../../tests/test_intent_router_integration.py#L179) | 179 | `"    # modifiers consume the bounded query budget."` | — |
| [SRC-4397BC2CD2-L000180](../../tests/test_intent_router_integration.py#L180) | 180 | `"    planned_queries = \" \".join(initial_plan[\"queries\"]).casefold()"` | — |
| [SRC-4397BC2CD2-L000181](../../tests/test_intent_router_integration.py#L181) | 181 | `"    assert \"السعر\" in planned_queries"` | — |
| [SRC-4397BC2CD2-L000182](../../tests/test_intent_router_integration.py#L182) | 182 | `"    assert \"البطارية\" in planned_queries"` | — |
| [SRC-4397BC2CD2-L000183](../../tests/test_intent_router_integration.py#L183) | 183 | `"    assert \"الكاميرا\" in planned_queries"` | — |
| [SRC-4397BC2CD2-L000184](../../tests/test_intent_router_integration.py#L184) | 184 | `"    assert len(initial_plan[\"queries\"]) <= 7"` | — |
| [SRC-4397BC2CD2-L000185](../../tests/test_intent_router_integration.py#L185) | 185 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-4397BC2CD2-L000186](../../tests/test_intent_router_integration.py#L186) | 186 | `"    coverage = result[\"answer_coverage\"]"` | — |
| [SRC-4397BC2CD2-L000187](../../tests/test_intent_router_integration.py#L187) | 187 | `"    assert coverage[\"method\"] == \"explicit_criteria_heuristic\""` | — |
| [SRC-4397BC2CD2-L000188](../../tests/test_intent_router_integration.py#L188) | 188 | `"    assert coverage[\"targets\"] == [\"السعر\", \"البطارية\", \"الكاميرا\"]"` | — |
| [SRC-4397BC2CD2-L000189](../../tests/test_intent_router_integration.py#L189) | 189 | `"    assert coverage[\"status\"] == \"model_review_requested_not_machine_verified\""` | — |
| [SRC-4397BC2CD2-L000190](../../tests/test_intent_router_integration.py#L190) | 190 | `"    assert coverage[\"automatically_graded\"] is False"` | — |
| [SRC-4397BC2CD2-L000191](../../tests/test_intent_router_integration.py#L191) | 191 | `"    # The mocked sources do not contain battery/camera evidence. The task must"` | — |
| [SRC-4397BC2CD2-L000192](../../tests/test_intent_router_integration.py#L192) | 192 | `"    # remain visibly incomplete even if the planner generated multiple queries."` | — |
| [SRC-4397BC2CD2-L000193](../../tests/test_intent_router_integration.py#L193) | 193 | `"    assert coverage[\"source_evidence_gap_count\"] == 2"` | — |
| [SRC-4397BC2CD2-L000194](../../tests/test_intent_router_integration.py#L194) | 194 | `"    assert result[\"task_fulfillment_status\"] == \"possible_gap_detected\""` | — |
| [SRC-4397BC2CD2-L000195](../../tests/test_intent_router_integration.py#L195) | 195 | `"    assert len(seen[\"plans\"]) == 2"` | — |
| [SRC-4397BC2CD2-L000196](../../tests/test_intent_router_integration.py#L196) | 196 | `"    assert \"البطارية\" in \" \".join(seen[\"plans\"][1][\"queries\"])"` | — |
| [SRC-4397BC2CD2-L000197](../../tests/test_intent_router_integration.py#L197) | 197 | `"    assert result[\"search_report\"][\"criterion_gap_research\"][\"attempted\"] is True"` | — |
| [SRC-4397BC2CD2-L000198](../../tests/test_intent_router_integration.py#L198) | 198 | `"    assert result[\"search_report\"][\"criterion_gap_research\"][\"status\"] == \"search_completed_no_new_criterion_evidence\""` | — |
| [SRC-4397BC2CD2-L000199](../../tests/test_intent_router_integration.py#L199) | 199 | `""` | — |
| [SRC-4397BC2CD2-L000200](../../tests/test_intent_router_integration.py#L200) | 200 | `"def test_deep_plan_preserves_all_eight_explicit_criteria_within_query_budget(monkeypatch) -> None:"` | — |
| [SRC-4397BC2CD2-L000201](../../tests/test_intent_router_integration.py#L201) | 201 | `"    agent = WebAgent()"` | — |
| [SRC-4397BC2CD2-L000202](../../tests/test_intent_router_integration.py#L202) | 202 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-4397BC2CD2-L000203](../../tests/test_intent_router_integration.py#L203) | 203 | `"    seen: dict = {\"plans\": []}"` | — |
| [SRC-4397BC2CD2-L000204](../../tests/test_intent_router_integration.py#L204) | 204 | `"    question = ("` | — |
| [SRC-4397BC2CD2-L000205](../../tests/test_intent_router_integration.py#L205) | 205 | `"        \"قارن بين خدمات من حيث السعر، الخصوصية، الاعتمادية، الدعم، \""` | — |
| [SRC-4397BC2CD2-L000206](../../tests/test_intent_router_integration.py#L206) | 206 | `"        \"الأمان، السرعة، الجودة، والتوفر\""` | — |
| [SRC-4397BC2CD2-L000207](../../tests/test_intent_router_integration.py#L207) | 207 | `"    )"` | — |
| [SRC-4397BC2CD2-L000208](../../tests/test_intent_router_integration.py#L208) | 208 | `""` | — |
| [SRC-4397BC2CD2-L000209](../../tests/test_intent_router_integration.py#L209) | 209 | `"    def plan(_question, _history):"` | — |
| [SRC-4397BC2CD2-L000210](../../tests/test_intent_router_integration.py#L210) | 210 | `"        return {"` | — |
| [SRC-4397BC2CD2-L000211](../../tests/test_intent_router_integration.py#L211) | 211 | `"            \"queries\": [\"مقارنة الخدمات\"],"` | — |
| [SRC-4397BC2CD2-L000212](../../tests/test_intent_router_integration.py#L212) | 212 | `"            \"direct_urls\": [],"` | — |
| [SRC-4397BC2CD2-L000213](../../tests/test_intent_router_integration.py#L213) | 213 | `"            \"social_focus\": False,"` | — |
| [SRC-4397BC2CD2-L000214](../../tests/test_intent_router_integration.py#L214) | 214 | `"            \"freshness\": \"any\","` | — |
| [SRC-4397BC2CD2-L000215](../../tests/test_intent_router_integration.py#L215) | 215 | `"            \"depth\": \"standard\","` | — |
| [SRC-4397BC2CD2-L000216](../../tests/test_intent_router_integration.py#L216) | 216 | `"            \"platforms\": [],"` | — |
| [SRC-4397BC2CD2-L000217](../../tests/test_intent_router_integration.py#L217) | 217 | `"            \"planning_method\": \"test_single_query\","` | — |
| [SRC-4397BC2CD2-L000218](../../tests/test_intent_router_integration.py#L218) | 218 | `"        }"` | — |
| [SRC-4397BC2CD2-L000219](../../tests/test_intent_router_integration.py#L219) | 219 | `""` | — |
| [SRC-4397BC2CD2-L000220](../../tests/test_intent_router_integration.py#L220) | 220 | `"    def collect(research_plan):"` | — |
| [SRC-4397BC2CD2-L000221](../../tests/test_intent_router_integration.py#L221) | 221 | `"        seen[\"plans\"].append(dict(research_plan))"` | — |
| [SRC-4397BC2CD2-L000222](../../tests/test_intent_router_integration.py#L222) | 222 | `"        sources = ["` | — |
| [SRC-4397BC2CD2-L000223](../../tests/test_intent_router_integration.py#L223) | 223 | `"            _evidence(\"example.com\", research_plan[\"queries\"]),"` | — |
| [SRC-4397BC2CD2-L000224](../../tests/test_intent_router_integration.py#L224) | 224 | `"            _evidence(\"example.net\", research_plan[\"queries\"]),"` | — |
| [SRC-4397BC2CD2-L000225](../../tests/test_intent_router_integration.py#L225) | 225 | `"        ]"` | — |
| [SRC-4397BC2CD2-L000226](../../tests/test_intent_router_integration.py#L226) | 226 | `"        return sources, [], _report(research_plan, sources)"` | — |
| [SRC-4397BC2CD2-L000227](../../tests/test_intent_router_integration.py#L227) | 227 | `""` | — |
| [SRC-4397BC2CD2-L000228](../../tests/test_intent_router_integration.py#L228) | 228 | `"    monkeypatch.setattr(agent, \"_plan_search\", plan)"` | — |
| [SRC-4397BC2CD2-L000229](../../tests/test_intent_router_integration.py#L229) | 229 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-4397BC2CD2-L000230](../../tests/test_intent_router_integration.py#L230) | 230 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda _query, _source: True)"` | — |
| [SRC-4397BC2CD2-L000231](../../tests/test_intent_router_integration.py#L231) | 231 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"مقارنة أولية [المصدر 1].\")"` | — |
| [SRC-4397BC2CD2-L000232](../../tests/test_intent_router_integration.py#L232) | 232 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda _question, answer, _sources: answer)"` | — |
| [SRC-4397BC2CD2-L000233](../../tests/test_intent_router_integration.py#L233) | 233 | `"    monkeypatch.setattr(agent, \"_repair_answer_coverage\", lambda _q, answer, _s, _m: answer)"` | — |
| [SRC-4397BC2CD2-L000234](../../tests/test_intent_router_integration.py#L234) | 234 | `""` | — |
| [SRC-4397BC2CD2-L000235](../../tests/test_intent_router_integration.py#L235) | 235 | `"    agent.answer(question, history=[])"` | — |
| [SRC-4397BC2CD2-L000236](../../tests/test_intent_router_integration.py#L236) | 236 | `""` | — |
| [SRC-4397BC2CD2-L000237](../../tests/test_intent_router_integration.py#L237) | 237 | `"    # All eight explicit criteria consume the bounded initial query allowance;"` | — |
| [SRC-4397BC2CD2-L000238](../../tests/test_intent_router_integration.py#L238) | 238 | `"    # the system must not launch an unbudgeted ninth query for coverage repair."` | — |
| [SRC-4397BC2CD2-L000239](../../tests/test_intent_router_integration.py#L239) | 239 | `"    assert len(seen[\"plans\"]) == 1"` | — |
| [SRC-4397BC2CD2-L000240](../../tests/test_intent_router_integration.py#L240) | 240 | `"    targets = WebAgent._question_coverage_targets(question)"` | — |
| [SRC-4397BC2CD2-L000241](../../tests/test_intent_router_integration.py#L241) | 241 | `"    assert len(targets) == 8"` | — |
| [SRC-4397BC2CD2-L000242](../../tests/test_intent_router_integration.py#L242) | 242 | `"    initial_plan = seen[\"plans\"][0]"` | — |
| [SRC-4397BC2CD2-L000243](../../tests/test_intent_router_integration.py#L243) | 243 | `"    queries = initial_plan[\"queries\"]"` | — |
| [SRC-4397BC2CD2-L000244](../../tests/test_intent_router_integration.py#L244) | 244 | `"    assert initial_plan[\"coverage_gap_repair_slot_reserved\"] is False"` | — |
| [SRC-4397BC2CD2-L000245](../../tests/test_intent_router_integration.py#L245) | 245 | `"    assert initial_plan[\"query_limit\"] == 8"` | — |
| [SRC-4397BC2CD2-L000246](../../tests/test_intent_router_integration.py#L246) | 246 | `"    assert len(queries) == 8"` | — |
| [SRC-4397BC2CD2-L000247](../../tests/test_intent_router_integration.py#L247) | 247 | `"    for target in targets:"` | — |
| [SRC-4397BC2CD2-L000248](../../tests/test_intent_router_integration.py#L248) | 248 | `"        assert any(target in query for query in queries), f\"Missing criterion query for {target!r}\""` | — |
| [SRC-4397BC2CD2-L000249](../../tests/test_intent_router_integration.py#L249) | 249 | `""` | — |
## اختبارات

### FILE-62DC597310 — [tests/test_live_search_connectors.py](../../tests/test_live_search_connectors.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-62DC597310-L000001](../../tests/test_live_search_connectors.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-62DC597310-L000002](../../tests/test_live_search_connectors.py#L2) | 2 | `""` | — |
| [SRC-62DC597310-L000003](../../tests/test_live_search_connectors.py#L3) | 3 | `"import httpx"` | — |
| [SRC-62DC597310-L000004](../../tests/test_live_search_connectors.py#L4) | 4 | `"import pytest"` | — |
| [SRC-62DC597310-L000005](../../tests/test_live_search_connectors.py#L5) | 5 | `""` | — |
| [SRC-62DC597310-L000006](../../tests/test_live_search_connectors.py#L6) | 6 | `"from agents.web_agent import ("` | — |
| [SRC-62DC597310-L000007](../../tests/test_live_search_connectors.py#L7) | 7 | `"    MAX_PROVIDER_RESPONSE_BYTES,"` | — |
| [SRC-62DC597310-L000008](../../tests/test_live_search_connectors.py#L8) | 8 | `"    WebAgent,"` | — |
| [SRC-62DC597310-L000009](../../tests/test_live_search_connectors.py#L9) | 9 | `"    _bounded_http_request,"` | — |
| [SRC-62DC597310-L000010](../../tests/test_live_search_connectors.py#L10) | 10 | `")"` | — |
