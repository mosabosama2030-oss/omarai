"""Deterministic P0 intent routing for Omarai (no network, no model calls)."""
from __future__ import annotations

import re
from typing import Any


def is_greeting(question: str, normalize) -> bool:
    value = normalize(question).casefold().strip()
    if not value or len(value) > 48:
        return False
    greetings = (
        "ازيك", "ازيك؟", "عامل ايه", "عامل ايه؟", "اخبارك", "اخبارك؟",
        "صباح الخير", "مساء الخير", "السلام عليكم", "مرحبا", "مرحباً", "اهلا", "أهلا",
        "hi", "hello", "hey", "good morning", "good evening", "thanks", "thank you",
        "شكرا", "شكراً", "ميرسي", "تمام", "ok", "okay",
    )
    if value in greetings:
        return True
    return any(value == g or value.startswith(g + " ") for g in greetings if len(g) >= 3)


def is_multipart_question(question: str, normalize) -> bool:
    value = question.strip()
    if re.search(r"[١٢٣٤٥]|[1-5]\s*[\)\.\-]|اولًا|ثانيًا|ثالثًا|أولا|ثانيا|ثالثا", value):
        return True
    low = normalize(value).casefold()
    multi_markers = (
        "قارن", "مقارنة", "من حيث", "من ناحية", "والبطارية", "والكاميرا",
        "والسعر", "compare", "versus", " vs ", "pros and cons", "المميزات والعيوب",
    )
    if sum(1 for m in multi_markers if m in low) >= 1 and (
        "و" in low or "and" in low or "vs" in low or "من حيث" in low or "من ناحية" in low
    ):
        dimension_hits = sum(
            1
            for d in (
                "سعر", "بطارية", "كاميرا", "خصوصية", "اداء", "أداء", "جودة",
                "price", "battery", "camera", "privacy", "performance",
            )
            if d in low
        )
        if dimension_hits >= 2:
            return True
        if "قارن" in low or "compare" in low or "مقارنة" in low:
            return True
    return False


def looks_ambiguous_referent(question: str, normalize) -> bool:
    value = normalize(question).casefold().strip()
    if not value:
        return True
    ambiguous_exact = (
        "كام سعرها", "كام سعره", "كام السعر", "ايه سعرها", "ايه سعره",
        "سعرها كام", "سعره كام", "is it good", "is it worth it", "compare them",
        "قارنهم", "قارن بينها", "ايه رأيك", "ما رأيك", "and the price", "what about it",
    )
    compact = value.replace("؟", "").replace("?", "").strip()
    if compact in ambiguous_exact:
        return True
    if len(compact) <= 18 and any(
        p in compact for p in ("سعرها", "سعره", "بكم", "كام ", "is it", "what about")
    ):
        stripped = compact
        for noise in (
            "كام", "ايه", "سعرها", "سعره", "السعر", "بكم", "هل",
            "is", "it", "the", "price", "good", "about",
        ):
            stripped = stripped.replace(noise, " ")
        tokens = [t for t in stripped.split() if len(t) >= 3]
        if not tokens:
            return True
    if compact in {"قارن", "compare", "compare them", "them"}:
        return True
    return False


def history_provides_referent(question: str, history: list[dict[str, str]] | None, normalize, clean_text) -> str | None:
    if not history:
        return None
    prior_users = [
        clean_text(item.get("content", ""), 400)
        for item in history
        if item.get("role") == "user" and (item.get("content") or "").strip()
    ]
    if not prior_users:
        return None
    previous = prior_users[-1]
    prev_low = normalize(previous).casefold()
    substantive = [
        t for t in re.findall(r"[\w\u0600-\u06FF]{3,}", prev_low)
        if t not in {
            "ازيك", "عامل", "ايه", "كام", "سعر", "السعر", "عايز", "أريد", "ابحث",
            "دور", "قولي", "يعني", "the", "and", "for", "what", "about", "please",
        }
    ]
    if not substantive:
        return None
    q = clean_text(question, 200)
    return clean_text(f"{previous} — {q}", 500)


def classify_intent_route(
    question: str,
    history: list[dict[str, str]] | None,
    mode: str,
    *,
    normalize,
    clean_text,
    is_self_question,
    requires_web_research,
    detect_depth,
    detect_freshness,
) -> dict[str, Any]:
    """Routes: LOCAL | MODEL_ONLY | CLARIFY | WEB_SIMPLE | WEB_DEEP.

    ABSTAIN is an evidence outcome after search, not a pre-search route.
    """
    clean_mode = mode if mode in {"auto", "deep", "latest", "social"} else "auto"
    resolved = question.strip()
    reason = "default"

    if clean_mode == "deep":
        return {
            "route": "WEB_DEEP",
            "resolved_question": resolved,
            "reason": "explicit_mode_deep",
            "web_search": True,
            "model_allowed": True,
        }
    if clean_mode in {"latest", "social"}:
        return {
            "route": "WEB_SIMPLE",
            "resolved_question": resolved,
            "reason": f"explicit_mode_{clean_mode}",
            "web_search": True,
            "model_allowed": True,
        }

    if is_self_question(resolved):
        return {
            "route": "LOCAL",
            "resolved_question": resolved,
            "reason": "capability_or_self_question",
            "web_search": False,
            "model_allowed": False,
        }
    if is_greeting(resolved, normalize):
        return {
            "route": "LOCAL",
            "resolved_question": resolved,
            "reason": "greeting_or_ack",
            "web_search": False,
            "model_allowed": False,
        }

    if looks_ambiguous_referent(resolved, normalize):
        expanded = history_provides_referent(resolved, history, normalize, clean_text)
        if expanded:
            resolved = expanded
            reason = "ambiguous_resolved_from_history"
        else:
            return {
                "route": "CLARIFY",
                "resolved_question": resolved,
                "reason": "ambiguous_without_referent",
                "web_search": False,
                "model_allowed": False,
            }

    if is_multipart_question(resolved, normalize) or detect_depth(resolved) == "deep":
        return {
            "route": "WEB_DEEP",
            "resolved_question": resolved,
            "reason": reason if reason != "default" else "multipart_or_deep_terms",
            "web_search": True,
            "model_allowed": True,
        }

    if requires_web_research(resolved, "auto") or detect_freshness(resolved):
        return {
            "route": "WEB_SIMPLE",
            "resolved_question": resolved,
            "reason": reason if reason != "default" else "dynamic_or_fresh_terms",
            "web_search": True,
            "model_allowed": True,
        }

    return {
        "route": "MODEL_ONLY",
        "resolved_question": resolved,
        "reason": "stable_general_or_conversational",
        "web_search": False,
        "model_allowed": True,
    }
