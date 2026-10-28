"""Validated dialogue-context records for Omarai.

The language model may propose semantic context, but all returned state is bounded,
normalized, and explicitly marked as model-derived or deterministic fallback. This
module never performs I/O and never stores cross-request user state.
"""
from __future__ import annotations

import re
import unicodedata
from typing import Any

from agents.intent_router import resolve_followup_query

MAX_RESOLVED_QUESTION_CHARS = 500
MAX_CONTEXT_TEXT_CHARS = 180
MAX_ENTITIES = 8
MAX_SLOT_VALUES = 16

_ALLOWED_INTENTS = frozenset({
    "answer_general",
    "compare",
    "current_information",
    "explain",
    "find_official_site",
    "find_product",
    "how_to",
    "lead_generation",
    "recommend",
    "social_opinions",
    "summarize",
    "troubleshoot",
    "unknown",
})
_ALLOWED_SLOT_KEYS = frozenset({
    "aspect", "audience", "budget", "capacity", "country", "currency",
    "entity", "goal", "language", "location", "model", "platform", "product",
    "time_range", "variant", "version",
})
_ALLOWED_CHANGED_SLOTS = _ALLOWED_SLOT_KEYS | frozenset({"topic", "intent"})
_ALLOWED_RESOLUTION_BASES = frozenset({
    "current_message", "explicit_confirmation", "history_inferred",
    "insufficient_evidence", "deterministic_fallback",
})
_ALLOWED_CONFIDENCE_BANDS = frozenset({"low", "medium", "high", "unassessed"})
_WHITESPACE = re.compile(r"\s+")


def _clean_text(value: Any, limit: int) -> str:
    if not isinstance(value, str):
        return ""
    value = unicodedata.normalize("NFKC", value)
    value = value.replace("\x00", " ")
    value = _WHITESPACE.sub(" ", value).strip()
    return value[:limit]


def _clean_string_list(value: Any, *, max_items: int, max_chars: int) -> list[str]:
    if not isinstance(value, list):
        return []
    result: list[str] = []
    seen: set[str] = set()
    for item in value[:max_items * 2]:
        clean = _clean_text(item, max_chars)
        key = clean.casefold()
        if clean and key not in seen:
            result.append(clean)
            seen.add(key)
        if len(result) >= max_items:
            break
    return result


def fallback_dialogue_context(question: str, history: Any = None) -> dict[str, Any]:
    """Build a conservative context record from the deterministic follow-up resolver."""
    current = _clean_text(question, MAX_RESOLVED_QUESTION_CHARS)
    resolved = _clean_text(
        resolve_followup_query(current, history) or current,
        MAX_RESOLVED_QUESTION_CHARS,
    )
    is_follow_up = bool(resolved and current and resolved.casefold() != current.casefold())
    return {
        "status": "fallback",
        "method": "deterministic_followup_heuristic",
        "resolved_question": resolved or current,
        "intent": "unknown",
        "topic": "",
        "entities": [],
        "slots": {},
        "changed_slots": [],
        "is_follow_up": is_follow_up,
        "topic_shift": False,
        "needs_web": False,
        "research_depth": "standard",
        "needs_clarification": False,
        "clarification_question": "",
        "unresolved_references": [],
        "resolution_basis": "deterministic_fallback",
        "confidence_band": "unassessed",
    }


def validate_dialogue_context(
    candidate: Any,
    question: str,
    history: Any = None,
    *,
    fallback: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Validate bounded context output from a planner without treating it as truth."""
    baseline = dict(fallback or fallback_dialogue_context(question, history))
    if not isinstance(candidate, dict):
        return baseline

    current = _clean_text(question, MAX_RESOLVED_QUESTION_CHARS)
    resolved = _clean_text(candidate.get("resolved_question"), MAX_RESOLVED_QUESTION_CHARS)
    if not resolved:
        return baseline

    has_history = isinstance(history, list) and any(
        isinstance(item, dict)
        and item.get("role") in {"user", "assistant"}
        and isinstance(item.get("content"), str)
        and item.get("content", "").strip()
        for item in history
    )
    topic_shift = candidate.get("topic_shift") is True
    is_follow_up = candidate.get("is_follow_up") is True and has_history and not topic_shift

    # A detected topic shift is a hard boundary: don't allow the old topic to leak
    # into the resolved question, even if the model accidentally included it.
    if topic_shift or not has_history:
        resolved = current
        is_follow_up = False

    needs_clarification = candidate.get("needs_clarification") is True
    if needs_clarification:
        # Never issue a search based on a reference the model itself says is unresolved.
        resolved = current

    intent = candidate.get("intent")
    if not isinstance(intent, str) or intent not in _ALLOWED_INTENTS:
        intent = "unknown"

    raw_slots = candidate.get("slots")
    slots: dict[str, str] = {}
    if isinstance(raw_slots, dict):
        for raw_key, raw_value in list(raw_slots.items())[:MAX_SLOT_VALUES]:
            key = _clean_text(raw_key, 40)
            value = _clean_text(raw_value, MAX_CONTEXT_TEXT_CHARS)
            if key in _ALLOWED_SLOT_KEYS and value:
                slots[key] = value

    changed_slots = [
        item for item in _clean_string_list(
            candidate.get("changed_slots"), max_items=8, max_chars=40
        )
        if item in _ALLOWED_CHANGED_SLOTS
    ]
    resolution_basis = candidate.get("resolution_basis")
    if not isinstance(resolution_basis, str) or resolution_basis not in _ALLOWED_RESOLUTION_BASES:
        resolution_basis = "history_inferred" if is_follow_up else "current_message"
    if topic_shift:
        resolution_basis = "current_message"

    depth = candidate.get("research_depth")
    if depth not in {"standard", "deep"}:
        depth = "standard"

    confidence_band = candidate.get("confidence_band")
    if confidence_band not in _ALLOWED_CONFIDENCE_BANDS:
        confidence_band = "unassessed"

    clarification_question = _clean_text(
        candidate.get("clarification_question"), 400
    ) if needs_clarification else ""

    status = (
        "needs_clarification" if needs_clarification
        else "topic_shift" if topic_shift
        else "resolved"
    )
    return {
        "status": status,
        "method": "llm_semantic_context",
        "resolved_question": resolved,
        "intent": intent,
        "topic": _clean_text(candidate.get("topic"), MAX_CONTEXT_TEXT_CHARS),
        "entities": _clean_string_list(
            candidate.get("entities"), max_items=MAX_ENTITIES, max_chars=MAX_CONTEXT_TEXT_CHARS
        ),
        "slots": slots,
        "changed_slots": changed_slots,
        "is_follow_up": is_follow_up,
        "topic_shift": topic_shift,
        "needs_web": candidate.get("needs_web") is True,
        "research_depth": depth,
        "needs_clarification": needs_clarification,
        "clarification_question": clarification_question,
        "unresolved_references": _clean_string_list(
            candidate.get("unresolved_references"), max_items=8, max_chars=100
        ),
        "resolution_basis": resolution_basis,
        "confidence_band": confidence_band,
    }


def might_be_context_dependent(question: str) -> bool:
    """Cheap trigger only; it does not decide the meaning of a contextual message."""
    current = _clean_text(question, MAX_RESOLVED_QUESTION_CHARS).casefold()
    if not current or len(current) > 220:
        return False
    lead_in = re.search(
        r"^(?:و?طب|و?طيب|و?تمام|ثم|كمان|وبالنسبه|بالنسبه|"
        r"and\s+(?:what|the|how)|what\s+about|how\s+about|"
        r"then\b|also\b|as\s+for\b|and\s+its\b)",
        current,
    )
    reference = re.search(
        r"\b(?:it|its|they|them|their|this|that|these|those|there|"
        r"he|she|هو|هي|ده|دي|دول|عليه|عليها|فيه|فيها|لها|له|"
        r"سعرها|سعره|ضمانها|ضمانه|بطاريتها|كاميرتها)\b",
        current,
    )
    fragment = re.fullmatch(
        r"[؟?\s]*(?:وال?)?(?:السعر|الاسعار|الضمان|البطاريه|الكاميرا|"
        r"المكان|الرابط|المصدر|المميزات|العيوب|warranty|price|battery|"
        r"camera|location|source|pros|cons)[؟?\s]*",
        current,
    )
    return bool(lead_in or reference or fragment)
