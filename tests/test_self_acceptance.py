from scripts.self_acceptance_test import build_live_questions, summarize_response


def test_self_acceptance_questions_cover_research_followup_and_optional_buyer_intent():
    questions = build_live_questions("أنظمة إنذار الحريق")
    assert [item["id"] for item in questions] == [
        "web-research-smoke",
        "context-followup",
        "buyer-intent-smoke",
    ]
    assert questions[0]["mode"] == "deep"
    assert questions[1]["history_from_previous"] is True
    assert "أنظمة إنذار الحريق" in questions[2]["question"]
    assert "إشارات شراء" in questions[2]["question"]


def test_custom_self_acceptance_questions_are_preserved_without_rewriting():
    questions = build_live_questions(
        custom_questions=["سؤال أول", "سؤال ثان"]
    )
    assert [item["question"] for item in questions] == ["سؤال أول", "سؤال ثان"]
    assert all(item["mode"] == "deep" for item in questions)


def test_live_response_summary_keeps_quality_gaps_visible():
    result = summarize_response(200, {
        "answer": "إجابة اختبار",
        "used_web_search": False,
        "used_language_model": True,
        "sources": [],
        "research_completion": {
            "status": "partial_answer_evidence_gaps_detected",
            "counters": {
                "invalid_citation_references_removed_count": 1,
                "citation_support_warning_count": 1,
            },
        },
    })
    assert result["http_status"] == 200
    assert result["answer_present"] is True
    assert result["source_count"] == 0
    assert result["used_web_search"] is False
    assert result["research_completion_status"] == "partial_answer_evidence_gaps_detected"
    assert result["invalid_citation_references_removed_count"] == 1
    assert result["citation_support_warning_count"] == 1

def test_tokenless_local_self_acceptance_executes_real_health_and_analyze_routes(
    tmp_path, monkeypatch
):
    import json

    from scripts.self_acceptance_test import run_acceptance

    monkeypatch.delenv("OMARAI_SELF_TEST_ALLOW_EXTERNAL_CALLS", raising=False)
    output = tmp_path / "self-acceptance.json"
    report = run_acceptance(output_path=output, live=False)

    assert report["environment"] == "local_loopback_isolated_database"
    assert report["authentication"]["access_token_required"] is False
    assert report["authentication"]["bind_host"] == "127.0.0.1"
    assert report["external_calls_enabled"] is False
    assert report["checks"]["health"]["status"] == "passed"
    assert report["checks"]["local_analyze"]["status"] == "passed"
    assert report["questions"] == []
    saved = json.loads(output.read_text(encoding="utf-8"))
    assert saved["authentication"]["test_mode"] is True
