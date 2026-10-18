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


def test_summarization_routes_to_web_simple():
    """Summarization requests must route to WEB_SIMPLE, not CLARIFY or MODEL_ONLY."""
    from agents.intent_router import route_intent

    cases = [
        "لخص الصفحة",
        "لخص لي هذا الرابط",
        "تلخيص المقال",
        "summarize the page",
        "summarize this article",
    ]
    for q in cases:
        decision = route_intent(q, [])
        route = decision["route"] if isinstance(decision, dict) else decision[0]
        assert route == "WEB_SIMPLE", f"Failed: {q!r} -> {decision}"
        if isinstance(decision, dict):
            assert decision.get("reason") == "summarization_request"
