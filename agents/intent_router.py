"""Small deterministic intent routing for Omarai's answer engine.

This module chooses a strategy; it does not search, call a model, or claim that
an answer is factually verified. Keep the rules explicit and unit-testable.
"""
from __future__ import annotations

import re
import unicodedata
from typing import Any

ROUTES = frozenset({
    "LOCAL", "MODEL_ONLY", "CLARIFY", "WEB_SIMPLE", "WEB_DEEP",
})

_ARABIC_DIACRITICS = re.compile(r"[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED]")
_PUNCTUATION = re.compile(r"[؟?!.،,؛;:()\[\]{}\"'«»]+")
_SPACE = re.compile(r"\s+")

_SMALLTALK = frozenset({
    "hi", "hello", "hey", "hello there", "hi there",
    "thanks", "thank you", "thanks that helps", "thank you that helps",
    "got it", "okay thanks", "ok thanks", "how are you", "how are you doing",
  "hello how are you", "hi how are you",
    "ازيك", "ازيك عامل ايه", "ازيك عامل ايه النهارده", "عامل ايه", "عامله ايه", "اهلا", "مرحبا",
    "السلام عليكم", "السلام عليكم ورحمه الله وبركاته",
    "صباح الخير", "مساء الخير", "شكرا", "شكرا لك", "متشكر", "متشكره",
    "تمام شكرا", "تمام", "حسنا", "العفو",
})

# Elliptical questions whose subject normally must be recovered from dialogue.
_AMBIGUOUS_ARABIC = frozenset({
    "كام سعرها", "كم سعرها", "بكام سعرها", "سعرها كام", "سعرها بكام",
    "كام تمنها", "كم تمنها", "بكام دي", "بكام ده", "سعره كام", "كام سعره",
    "كم سعره", "قارنهم", "قارنهملي", "قارن بينهم", "قارن بينهما",
    "ما رايك فيها", "ايه رايك فيها", "هل هي كويسه", "هل هو كويس",
    "هل دي كويسه", "هل ده كويس", "هل هو جيد", "هل هي جيده",
    "اشتريها ولا لا", "اشتريه ولا لا",
})
_AMBIGUOUS_ENGLISH = frozenset({
    "how much is it", "how much does it cost", "what is its price",
    "what about it", "what about this", "is it good", "is this good",
    "does it work", "compare them", "compare these", "compare the two",
    "what do you think of it", "should i buy it", "is it worth it",
})
_DEEP_TERMS = (
    "بحث عميق", "بحث معمق", "بحث مكثف", "بحث شامل", "بالتفصيل",
    "قارن", "مقارنه", "حلل بعمق", "مزايا وعيوب", "الايجابيات والسلبيات",
    "كل الجوانب", "دراسه مقارنه", "compare", "comparison", "deep research",
    "in-depth", "comprehensive", "pros and cons", "trade-offs",
)
_MULTIPART_MARKERS = (
    "بالاضافه الى", "مع مراعاه", "من حيث", "وكذلك", "و ايضا", "والفرق",
    "على ان تشمل", "and also", "as well as", "taking into account",
    "in terms of", "along with",
)


def _normalize(value: str) -> str:
    value = unicodedata.normalize("NFKC", value or "").casefold()
    value = _ARABIC_DIACRITICS.sub("", value)
    value = value.translate(str.maketrans({
        "أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا", "ى": "ي", "ة": "ه", "ـ": "",
    }))
    value = _PUNCTUATION.sub(" ", value)
    return _SPACE.sub(" ", value).strip()


def _is_smalltalk(question: str) -> bool:
    normalized = _normalize(question)
    if normalized in _SMALLTALK:
        return True
    # Keep these patterns narrow: an opening greeting followed by a real question
    # is not itself a greeting-only request.
    if normalized.startswith("السلام عليكم ") and normalized[14:].strip() in _SMALLTALK:
        return True
    return False


def _has_context(history: Any) -> bool:
    if not isinstance(history, list):
        return False
    for item in reversed(history[-8:]):
        if not isinstance(item, dict):
            continue
        if item.get("role") not in {"user", "assistant"}:
            continue
        content = item.get("content")
        if not isinstance(content, str):
            continue
        normalized = _normalize(content)
        if not normalized or _is_smalltalk(normalized):
            continue
        # A substantive earlier turn is context; a bare greeting/acknowledgment is not.
        meaningful = re.findall(r"[a-z0-9]+|[\u0600-\u06FF]+", normalized)
        if len(meaningful) >= 2 and len(normalized) >= 8:
            return True
    return False


def _needs_clarification(question: str) -> bool:
    normalized = _normalize(question)
    if normalized in _AMBIGUOUS_ARABIC or normalized in _AMBIGUOUS_ENGLISH:
        return True
    # Common inflected forms missed by exact phrase matching.
    if re.fullmatch(r"(?:كام|كم|بكام)\s+(?:سعر|ثمن)\s*(?:ها|ه|هم)", normalized):
        return True
    if re.fullmatch(r"(?:قارن|قارنلي)\s+(?:بينهم|بينهما|دول|دي|دولتين)", normalized):
        return True
    return False


def _is_deep(question: str) -> bool:
    normalized = _normalize(question)
    if any(_normalize(term) in normalized for term in _DEEP_TERMS):
        return True
    # Explicit multi-dimension comparisons need evidence from more than one angle.
    dimensions = (
        "السعر", "سعر", "بطاريه", "كاميرا", "اداء", "امان", "تكلفه",
        "الصيانه", "الجوده", "المميزات", "العيوب", "الاراء", "المراجعات",
        "price", "battery", "camera", "performance", "safety", "cost",
        "maintenance", "quality", "features", "drawbacks", "reviews",
    )
    matched_dimensions = sum(1 for item in dimensions if _normalize(item) in normalized)
    return matched_dimensions >= 2 and any(
        marker in normalized for marker in _MULTIPART_MARKERS
    )


def route_intent(
    question: str,
    history: Any = None,
    mode: str = "auto",
    *,
    capability_question: bool = False,
    requires_web: bool = False,
) -> dict[str, Any]:
    """Return a deterministic route and auditable reason for a user question."""
    clean_mode = mode.strip().lower() if isinstance(mode, str) else "auto"
    context_available = _has_context(history)

    # An explicitly selected mode is a user control and takes precedence over
    # conversational heuristics; it must not silently convert a requested search.
    if clean_mode != "auto":
        route = "WEB_DEEP" if clean_mode == "deep" else "WEB_SIMPLE"
        return {
            "route": route,
            "reason": "explicit_mode",
            "context_available": context_available,
            "needs_clarification": False,
        }

    if capability_question:
        return {
            "route": "LOCAL",
            "reason": "capability_question",
            "context_available": context_available,
            "needs_clarification": False,
        }

    if _is_smalltalk(question):
        return {
            "route": "LOCAL",
            "reason": "short_conversational_turn",
            "context_available": context_available,
            "needs_clarification": False,
        }

    ambiguous = _needs_clarification(question)
    if ambiguous and not context_available:
        return {
            "route": "CLARIFY",
            "reason": "missing_referent_and_no_conversation_context",
            "context_available": False,
            "needs_clarification": True,
        }

    if _is_deep(question):
        return {
            "route": "WEB_DEEP",
            "reason": "comparison_or_multi_part_research",
            "context_available": context_available,
            "needs_clarification": False,
        }

    if requires_web:
        return {
            "route": "WEB_SIMPLE",
            "reason": "freshness_or_explicit_research_signal",
            "context_available": context_available,
            "needs_clarification": False,
        }

    return {
        "route": "MODEL_ONLY",
        "reason": "stable_knowledge_or_conversation",
        "context_available": context_available,
        "needs_clarification": False,
    }
