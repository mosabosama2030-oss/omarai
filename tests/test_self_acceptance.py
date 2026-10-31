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
