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


def test_no_duplicate_followup_leadin_symbols():
    """Regression: followup lead-in symbols must be defined exactly once.

    Duplicate definitions previously survived incomplete merges and could
    shadow or confuse maintenance. This guards against reintroduction.
    """
    import ast
    from pathlib import Path

    src = Path("agents/intent_router.py").read_text(encoding="utf-8")
    tree = ast.parse(src)
    strip_defs = [
        n for n in ast.walk(tree)
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
        and n.name == "_strip_followup_leadin"
    ]
    lead_assigns = [
        n for n in ast.walk(tree)
        if isinstance(n, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == "_FOLLOWUP_LEAD_IN_RE" for t in n.targets)
    ]
    aspect_assigns = [
        n for n in ast.walk(tree)
        if isinstance(n, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == "_FOLLOWUP_ASPECT_FRAGMENTS" for t in n.targets)
    ]
    assert len(strip_defs) == 1, "Duplicate _strip_followup_leadin definition"
    assert len(lead_assigns) == 1, "Duplicate _FOLLOWUP_LEAD_IN_RE assignment"
    assert len(aspect_assigns) == 1, "Duplicate _FOLLOWUP_ASPECT_FRAGMENTS assignment"
