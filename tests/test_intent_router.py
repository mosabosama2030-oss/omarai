from __future__ import annotations

import pytest

from agents.intent_router import resolve_followup_query, route_intent


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
        (
            "ابحث عن ١٠ عملاش يريدون شراء شقة في التجمع الخامس",
            "LEAD_GENERATION",
        ),
        (
            "ابحث عن ٥ عملاء يطلبون شقة في التجمع الخامس",
            "LEAD_GENERATION",
        ),
        (
            "ابحث عن ١٠ عملاش يريدون شرا سيارة في القاهرة",
            "LEAD_GENERATION",
        ),
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


@pytest.mark.parametrize(
    ("question", "expected_route", "expected_reason"),
    [
        (
            "لخص الصفحة https://example.com/article",
            "WEB_SIMPLE",
            "summarization_request",
        ),
        (
            "Summarize this page https://example.com/article",
            "WEB_SIMPLE",
            "summarization_request",
        ),
        ("لخص الصفحة", "CLARIFY", "missing_summarization_input"),
        ("لخص لي هذا الرابط", "CLARIFY", "missing_summarization_input"),
        ("summarize the page", "CLARIFY", "missing_summarization_input"),
        ("تلخيص المقال", "CLARIFY", "missing_summarization_input"),
        ("لخص النص التالي: هذا نص تجريبي", "MODEL_ONLY", "stable_knowledge_or_conversation"),
        ("Summarize this text: the test content is here", "MODEL_ONLY", "stable_knowledge_or_conversation"),
    ],
)
def test_summarization_routing_respects_page_text_and_missing_input(
    question: str, expected_route: str, expected_reason: str
) -> None:
    decision = route_intent(question, [])
    assert decision["route"] == expected_route
    assert decision["reason"] == expected_reason


@pytest.mark.parametrize(
    "question",
    [
        "فين؟",
        "فين هي؟",
        "مكانها فين؟",
        "هل فيه ضمان؟",
        "هل لها ضمان؟",
        "ضمانها إيه؟",
        "Where is it?",
        "Does it have a warranty?",
    ],
)
def test_missing_referent_questions_clarify_without_context(question: str) -> None:
    decision = route_intent(question, history=None, mode="auto", requires_web=True)
    assert decision["route"] == "CLARIFY"
    assert decision["needs_clarification"] is True
    assert decision["context_available"] is False


@pytest.mark.parametrize("question", ["فين؟", "هل فيه ضمان؟", "كام سعرها؟"])
def test_missing_referent_still_clarifies_in_explicit_search_mode(question: str) -> None:
    decision = route_intent(question, history=None, mode="deep")
    assert decision["route"] == "CLARIFY"
    assert decision["needs_clarification"] is True


def test_followup_resolver_uses_topic_from_latest_user_turn() -> None:
    history = [
        {"role": "user", "content": "عايز أعرف سعر آيفون 16 في مصر"},
        {"role": "assistant", "content": "سأبحث عن معلومات موثوقة."},
    ]
    resolved = resolve_followup_query("هل فيه ضمان؟", history)
    assert "آيفون 16" in resolved
    assert "ضمان" in resolved


def test_followup_resolver_does_not_resurrect_topic_after_acknowledgment() -> None:
    history = [
        {"role": "user", "content": "عايز أعرف سعر آيفون 16 في مصر"},
        {"role": "assistant", "content": "سأبحث عن معلومات موثوقة."},
        {"role": "user", "content": "شكرًا"},
        {"role": "assistant", "content": "العفو."},
    ]
    assert resolve_followup_query("فين؟", history) == "فين؟"


def test_followup_resolver_bounds_output_and_handles_malformed_history() -> None:
    history = [{"role": "user", "content": "س" * 4000}]
    assert len(resolve_followup_query("والسعر؟", history)) <= 500
    assert resolve_followup_query("فين؟", {"role": "user", "content": "topic"}) == "فين؟"

def test_prefixed_elliptical_followup_is_clarified_without_topic():
    for question in ("طب هل فيه ضمان؟", "طيب كام سعرها؟", "والضمان؟", "والسعر؟"):
        decision = route_intent(question)
        assert decision["route"] == "CLARIFY", question

def test_prefixed_elliptical_followup_uses_topic_when_available():
    history = [
        {"role": "user", "content": "عايز أعرف سعر iPhone 16 في مصر"},
        {"role": "assistant", "content": "نتحدث عن iPhone 16 في مصر."},
    ]
    for question in ("طب هل فيه ضمان؟", "طيب كام سعرها؟", "والضمان؟"):
        decision = route_intent(question, history, requires_web=True)
        assert decision["route"] == "WEB_SIMPLE", question
        resolved = resolve_followup_query(question, history)
        assert "iPhone 16" in resolved
        assert "مصر" in resolved

def test_long_arabic_warranty_followup_resolves_with_context():
    history = [
        {"role": "user", "content": "عايز أعرف سعر iPhone 17 نسخة 256 جيجابايت في مصر"},
        {"role": "assistant", "content": "سأبحث عن السعر."},
    ]
    question = "وطب الضمان الدولي بيسري في مصر؟"
    resolved = resolve_followup_query(question, history)
    assert "iPhone 17" in resolved
    assert question in resolved

def test_long_arabic_warranty_followup_without_context_clarifies():
    question = "وطب الضمان الدولي بيسري في مصر؟"
    decision = route_intent(question)
    assert decision["route"] == "CLARIFY"
    assert decision["needs_clarification"] is True

def test_new_question_starting_with_tayyib_does_not_inherit_old_topic():
    history = [
        {"role": "user", "content": "ما سعر iPhone 16 في مصر؟"},
        {"role": "assistant", "content": "هذه بعض معلومات السعر."},
    ]
    question = "طيب اشرح الذكاء الاصطناعي في المدارس"
    assert resolve_followup_query(question, history) == question
    decision = route_intent(question, history)
    assert decision["route"] == "MODEL_ONLY"

def test_chained_followups_keep_the_last_substantive_topic():
    history = [
        {"role": "user", "content": "ما سعر iPhone 16 في مصر؟"},
        {"role": "assistant", "content": "السعر يختلف حسب المتجر."},
        {"role": "user", "content": "والضمان؟"},
        {"role": "assistant", "content": "سأوضح الضمان."},
    ]
    resolved = resolve_followup_query("والبطارية؟", history)
    assert "iPhone 16" in resolved
    assert "البطارية" in resolved

def test_answer_to_clarification_restores_original_intent():
    history = [
        {"role": "user", "content": "كام سعرها؟"},
        {
            "role": "assistant",
            "content": "تقصد إيه تحديدًا؟ اكتب اسم الشيء أو المنتج المقصود، أو ابعت الرابط، وأكمل معاك من غير ما أخمّن.",
        },
    ]
    decision = route_intent("iPhone 16", history)
    assert decision["route"] == "WEB_SIMPLE"
    assert decision["reason"] == "answer_to_pending_clarification"
    resolved = resolve_followup_query("iPhone 16", history)
    assert "سعرها" in resolved
    assert "iPhone 16" in resolved

def test_topic_detection_does_not_inherit_old_social_or_depth_intent():
    from agents.research import fallback_plan

    history = [
        {"role": "user", "content": "اجمع آراء مستخدمي السيارات الكهربائية على Reddit"},
        {"role": "assistant", "content": "هذه النتائج."},
    ]
    plan = fallback_plan("اشرح طريقة عمل المحرك الكهربائي", history)
    assert plan["social_focus"] is False
    assert plan["platforms"] == []
    assert plan["depth"] == "standard"

def test_explicit_request_for_reliable_sources_uses_web_search_in_auto_mode():
    question = (
        "ما أهم استخدامات الذكاء الاصطناعي في الشركات الصغيرة؟ "
        "اذكر أمثلة ومصادر موثوقة."
    )
    decision = route_intent(question, mode="auto")
    assert decision["route"] == "WEB_SIMPLE"
    assert decision["reason"] == "explicit_evidence_request"

def test_stable_question_without_source_request_remains_model_only():
    decision = route_intent("اشرح الفرق بين التعلم الخاضع للإشراف وغير الخاضع للإشراف")
    assert decision["route"] == "MODEL_ONLY"

def test_attached_arabic_object_pronoun_resolves_against_previous_subject() -> None:
    history = [
        {"role": "user", "content": "بفكر أشتري Lenovo ThinkPad E14 في مصر"},
        {"role": "assistant", "content": "نتحدث عن Lenovo ThinkPad E14 في السوق المصري."},
    ]

    resolved = resolve_followup_query("أقدر أشتريه منين؟", history)

    assert "Lenovo ThinkPad E14" in resolved
    assert "أقدر أشتريه منين" in resolved
