from __future__ import annotations

from agents.answer_validation import audit_answer_integrity
from agents.web_agent import WebAgent


def test_numeric_screen_accepts_arabic_digits_and_thousands_formatting():
    result = audit_answer_integrity(
        "ما السعر المذكور في 2025؟",
        "السعر ١٠٠٬٠٠٠ جنيه في 2025 [المصدر 1].",
        [{
            "title": "تفاصيل السعر",
            "snippet": "السعر 100,000 جنيه",
            "page_text": "السعر 100,000 جنيه",
            "page_fetched": True,
            "published_at": "",
        }],
        ["السعر"],
    )
    assert result["numeric_check_status"] == "all_checked_numeric_literals_appear_in_source_text"
    assert result["potentially_unsupported_numeric_literals"] == []
    assert result["source_evidence_scope"] == "contains_extracted_page_text_and_or_snippets"
    assert result["citation_marker_count"] == 1
    assert result["semantic_verification"] is False


def test_numeric_screen_flags_number_absent_from_available_evidence():
    result = audit_answer_integrity(
        "ما السعر؟",
        "السعر 500 جنيه [المصدر 1].",
        [{
            "title": "تفاصيل السعر",
            "snippet": "السعر 300 جنيه",
            "page_fetched": False,
            "published_at": "",
        }],
    )
    assert result["numeric_check_status"] == "potentially_unsupported_numeric_literals"
    assert "500" in result["potentially_unsupported_numeric_literals"]
    assert result["citation_entailment"] == "not_checked"


def test_task_coverage_screen_flags_a_potentially_missing_target_without_claiming_failure():
    result = audit_answer_integrity(
        "قارن من حيث السعر والمساحة",
        "من حيث السعر، الخيار الأول أقل تكلفة.",
        [{
            "title": "إعلان",
            "snippet": "السعر والمساحة غير موضحين",
            "page_fetched": False,
        }],
        ["السعر", "المساحة"],
    )
    checks = {item["target"]: item for item in result["target_coverage"]}
    assert checks["السعر"]["status"] == "lexical_signal_found"
    assert checks["المساحة"]["status"] == "possibly_missing"
    assert result["potentially_missing_target_count"] == 1
    assert result["method"] == "deterministic_lexical_screen_only"
    assert result["independent_fact_check"] is False


def test_source_scope_does_not_confuse_snippet_with_fetched_page():
    result = audit_answer_integrity(
        "ما التفاصيل؟",
        "وجدت مقتطفًا.",
        [{"title": "نتيجة", "snippet": "مقتطف قصير", "page_fetched": False}],
    )
    assert result["source_evidence_scope"] == "search_snippets_only"
    assert result["pages_with_extracted_text"] == 0
    assert result["sources_with_snippets_only"] == 1


def test_review_prompt_explicitly_requires_number_and_conflict_audit(monkeypatch):
    agent = WebAgent()
    captured = {}

    def fake_completion(messages, **kwargs):
        captured["messages"] = messages
        return "<<<OMARAI_FINAL_ANSWER>>>لا تكفي الأدلة.<<<END_OMARAI_FINAL_ANSWER>>>"

    monkeypatch.setattr(agent, "_request_completion", fake_completion)
    answer = agent._review_answer(
        "قارن السعر والمدة",
        "السعر 100 جنيه [المصدر 1].",
        [{
            "title": "مصدر",
            "url": "https://example.com/item",
            "page_text": "السعر 90 جنيه، والمدة 5 أيام.",
            "snippet": "السعر 90 جنيه",
            "page_fetched": True,
        }],
    )
    prompt = captured["messages"][0]["content"]
    assert answer == "لا تكفي الأدلة."
    assert "المبالغ والأسعار والنسب والتواريخ والمدد والقياسات" in prompt
    assert "قيمًا متعارضة" in prompt


def test_citation_alignment_uses_fetched_page_text_and_flags_weak_overlap():
    page_source = {
        "title": "Report",
        "snippet": "completely unrelated snippet about fruit",
        "page_text": "Renewable energy storage costs decreased during the reporting period.",
        "page_fetched": True,
        "published_at": "",
    }
    good = audit_answer_integrity(
        "What changed?",
        "Renewable energy storage costs decreased [source 1].",
        [page_source],
    )
    assert good["citation_lexical_alignment_method"] == "content_word_overlap_heuristic_not_entailment"
    assert good["citation_lexical_alignment"][0]["status"] == "lexical_overlap_signal_found"
    assert good["citation_lexical_alignment"][0]["citations"][0]["evidence_basis"] == "extracted_page_text"
    assert good["citation_entailment"] == "not_checked"

    weak = audit_answer_integrity(
        "What happened?",
        "Mango harvest volume rose sharply [source 1].",
        [page_source],
    )
    assert weak["citation_lexical_alignment"][0]["status"] == "weak_lexical_overlap"
    assert weak["weak_citation_alignment_count"] == 1
    assert weak["independent_fact_check"] is False


def test_snippet_only_citation_alignment_is_labeled_as_snippet_evidence():
    result = audit_answer_integrity(
        "What was reported?",
        "The reported costs changed [المصدر 1].",
        [{
            "title": "Costs report",
            "snippet": "Reported costs changed in the new report.",
            "page_fetched": False,
        }],
    )
    assert result["citation_lexical_alignment"][0]["citations"][0]["evidence_basis"] == "search_snippet"
    assert result["citation_entailment"] == "not_checked"
