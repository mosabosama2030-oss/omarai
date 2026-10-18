from __future__ import annotations

import pytest

from agents.intent_router import route_intent


@pytest.mark.parametrize(
    ("question", "expected"),
    [
        ("ازيك؟ عامل ايه النهاردة؟", "LOCAL"),
        ("Thanks, that helps.", "LOCAL"),
        ("ما عاصمة مصر؟", "MODEL_ONLY"),
        ("كام سعرها؟", "CLARIFY"),
        ("قارنهم", "CLARIFY"),
        ("ما سعر الهاتف اليوم في مصر؟", "WEB_SIMPLE"),
        (
            "قارن بين iPhone 17 وSamsung S26 من حيث السعر والبطارية والكاميرا",
            "WEB_DEEP",
        ),
    ],
)
def test_deterministic_intent_routes(question: str, expected: str) -> None:
    decision = route_intent(question)
    assert decision["route"] == expected
    assert decision["reason"]


@pytest.mark.parametrize(
    ("question", "expected"),
    [
        ("ابحث عن عميل يريد شراء شقة في العاصمة الإدارية بمصر", "LEAD_GENERATION"),
        ("ابحث عن شقق للبيع في العاصمة الإدارية", "WEB_SIMPLE"),
        ("Find buyers looking to buy apartments in New Capital", "LEAD_GENERATION"),
        ("لخص الصفحة https://example.com/article", "WEB_SIMPLE"),
        ("Summarize this page https://example.com/article", "WEB_SIMPLE"),
        ("لخص النص التالي: هذا نص تجريبي", "MODEL_ONLY"),
    ],
)
def test_lead_generation_and_summarization_routes(question: str, expected: str) -> None:
    decision = route_intent(question)
    assert decision["route"] == expected
    assert decision["reason"]


def test_generic_explanation_of_lead_generation_is_not_a_lead_search() -> None:
    assert route_intent("What is lead generation?")["route"] == "MODEL_ONLY"
    assert route_intent("Create a prospect list for apartment buyers")["route"] == "LEAD_GENERATION"



def test_capability_question_is_local() -> None:
    decision = route_intent(
        "كيف تستطيع مساعدتي؟",
        capability_question=True,
        requires_web=False,
    )
    assert decision["route"] == "LOCAL"
    assert decision["reason"] == "capability_question"


def test_ambiguous_followup_uses_existing_conversation_context() -> None:
    history = [
        {"role": "user", "content": "عايز أعرف سعر iPhone 17 في مصر"},
        {"role": "assistant", "content": "نتحدث عن هاتف iPhone 17 في السوق المصري."},
    ]
    decision = route_intent("كام سعرها؟", history, requires_web=True)
    assert decision["route"] == "WEB_SIMPLE"
    assert decision["context_available"] is True
    assert decision["needs_clarification"] is False


def test_comparison_followup_requires_context_before_deep_search() -> None:
    assert route_intent("قارنهم")["route"] == "CLARIFY"
    history = [{"role": "user", "content": "قارن iPhone 17 وSamsung S26"}]
    decision = route_intent("قارنهم", history)
    assert decision["route"] == "WEB_DEEP"
    assert decision["context_available"] is True


def test_ambiguous_followup_does_not_reuse_stale_topic_after_acknowledgment() -> None:
    history = [
        {"role": "user", "content": "عايز أعرف سعر iPhone 17 في مصر"},
        {"role": "assistant", "content": "سأساعدك في العثور على أسعار حديثة."},
        {"role": "user", "content": "شكرا"},
        {"role": "assistant", "content": "العفو."},
    ]
    decision = route_intent("كام سعرها؟", history, requires_web=True)
    assert decision["route"] == "CLARIFY"
    assert decision["context_available"] is False


def test_explicit_mode_overrides_conversational_shortcuts() -> None:
    assert route_intent("ازيك؟", mode="deep")["route"] == "WEB_DEEP"
    assert route_intent("ما سعر الهاتف؟", mode="latest")["route"] == "WEB_SIMPLE"
