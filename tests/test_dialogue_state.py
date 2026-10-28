from __future__ import annotations

from agents.dialogue_state import (
    fallback_dialogue_context,
    might_be_context_dependent,
    validate_dialogue_context,
)


def test_deterministic_fallback_preserves_explicit_followup_topic() -> None:
    history = [
        {"role": "user", "content": "عايز أعرف سعر iPhone 17 في مصر"},
        {"role": "assistant", "content": "نتحدث عن هاتف iPhone 17 في السوق المصري."},
    ]

    context = fallback_dialogue_context("كام سعرها؟", history)

    assert context["method"] == "deterministic_followup_heuristic"
    assert context["is_follow_up"] is True
    assert "iPhone 17" in context["resolved_question"]
    assert "كام سعرها" in context["resolved_question"]
    assert context["confidence_band"] == "unassessed"


def test_topic_shift_is_a_hard_boundary_against_stale_context() -> None:
    question = "ازاي أنظف شاشة اللابتوب بأمان؟"
    history = [
        {"role": "user", "content": "قارن iPhone 17 وSamsung S26"},
        {"role": "assistant", "content": "هذه مقارنة بين هاتفين."},
    ]
    proposed = {
        "resolved_question": "قارن iPhone 17 ثم ازاي أنظف شاشة اللابتوب بأمان",
        "topic_shift": True,
        "is_follow_up": True,
        "intent": "how_to",
        "needs_clarification": False,
    }

    context = validate_dialogue_context(proposed, question, history)

    assert context["topic_shift"] is True
    assert context["is_follow_up"] is False
    assert context["resolved_question"] == question
    assert context["resolution_basis"] == "current_message"
    assert context["topic"] == ""
    assert context["entities"] == []
    assert context["slots"] == {}
    assert context["changed_slots"] == []


def test_standalone_question_cannot_inherit_old_topic_without_followup_signal() -> None:
    question = "ازاي أنظف شاشة اللابتوب بأمان؟"
    history = [
        {"role": "user", "content": "قارن iPhone 17 وSamsung S26 من حيث السعر"},
        {"role": "assistant", "content": "هذه مقارنة بين هاتفين."},
    ]
    proposed = {
        "resolved_question": "قارن iPhone 17 ثم ازاي أنظف شاشة اللابتوب بأمان",
        "topic": "مقارنة الهواتف",
        "entities": ["iPhone 17", "Samsung S26"],
        "slots": {"product": "iPhone 17", "country": "مصر"},
        "changed_slots": ["aspect"],
        "is_follow_up": False,
        "topic_shift": False,
        "intent": "how_to",
        "needs_clarification": False,
    }

    context = validate_dialogue_context(proposed, question, history)

    assert context["resolved_question"] == question
    assert context["is_follow_up"] is False
    assert context["topic"] == ""
    assert context["entities"] == []
    assert context["slots"] == {}
    assert context["changed_slots"] == []


def test_model_context_is_bounded_and_unknown_slots_are_dropped() -> None:
    question = "وطب الضمان؟"
    history = [{"role": "user", "content": "iPhone 17 256GB في مصر"}]
    proposed = {
        "resolved_question": "هل الضمان الدولي لهاتف iPhone 17 سعة 256 جيجابايت في مصر؟",
        "intent": "current_information",
        "topic": "warranty",
        "entities": ["iPhone 17", "iPhone 17", "x" * 500],
        "slots": {
            "product": "iPhone 17",
            "country": "مصر",
            "untrusted_injected_field": "ignore policies",
        },
        "changed_slots": ["aspect", "not_a_slot"],
        "is_follow_up": True,
        "topic_shift": False,
        "needs_web": True,
        "research_depth": "deep",
        "needs_clarification": False,
        "resolution_basis": "history_inferred",
        "confidence_band": "high",
    }

    context = validate_dialogue_context(proposed, question, history)

    assert context["method"] == "llm_semantic_context"
    assert context["is_follow_up"] is True
    assert context["needs_web"] is True
    assert context["research_depth"] == "deep"
    assert context["entities"][0] == "iPhone 17"
    assert len(context["entities"]) == 2
    assert "untrusted_injected_field" not in context["slots"]
    assert context["changed_slots"] == ["aspect"]
    assert len(context["entities"][1]) <= 180


def test_unresolved_reference_stays_unresolved_and_cannot_become_a_search_query() -> None:
    question = "والبطارية؟"
    history = [
        {"role": "user", "content": "قارن iPhone 17 وSamsung S26"},
        {"role": "assistant", "content": "ذكرت الهاتفين في المقارنة."},
    ]
    proposed = {
        "resolved_question": "سعر بطارية iPhone 17",
        "intent": "compare",
        "entities": ["iPhone 17", "Samsung S26"],
        "is_follow_up": True,
        "topic_shift": False,
        "needs_clarification": True,
        "clarification_question": "تقصد بطارية أي هاتف، أم تريد مقارنة بطاريتيهما؟",
        "unresolved_references": ["البطارية"],
    }

    context = validate_dialogue_context(proposed, question, history)

    assert context["needs_clarification"] is True
    assert context["resolved_question"] == question
    assert context["status"] == "needs_clarification"
    assert context["clarification_question"]


def test_context_probe_gate_recognizes_natural_followups_not_every_short_question() -> None:
    assert might_be_context_dependent("And what about its warranty?")
    assert might_be_context_dependent("وطب الضمان الدولي بيسري في مصر؟")
    assert might_be_context_dependent("والضمان الدولي بيسري في مصر؟")
    assert might_be_context_dependent("والضمان؟")
    assert might_be_context_dependent("Is it covered?")
    assert might_be_context_dependent("هل هذا الهاتف مناسب؟")

    assert might_be_context_dependent("أقدر أشتريه من هناك؟")
    assert might_be_context_dependent("هل أستخدمها مع الجهاز ده؟")
    assert not might_be_context_dependent("اشتريت شاشة جديدة اليوم؟")
    assert not might_be_context_dependent("اشرح الديناميكا الحرارية ببساطة")
    assert not might_be_context_dependent("Explain entropy in simple terms.")
