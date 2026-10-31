"""Regression: ensure followup lead-in symbols are defined only once.

Duplicate module-level definitions of _FOLLOWUP_LEAD_IN_RE,
_FOLLOWUP_ASPECT_FRAGMENTS and _strip_followup_leadin were observed on main
and caused confusion / potential override risk. This test fails if they reappear.
"""
from __future__ import annotations

import pathlib

import pytest


def _count_definitions(source: str) -> dict[str, int]:
    return {
        "lead_in_re": source.count("_FOLLOWUP_LEAD_IN_RE = re.compile"),
        "aspect_fragments": source.count("_FOLLOWUP_ASPECT_FRAGMENTS = frozenset"),
        "strip_fn": source.count("def _strip_followup_leadin"),
    }


def test_intent_router_has_no_duplicate_followup_symbols() -> None:
    path = pathlib.Path(__file__).resolve().parents[1] / "agents" / "intent_router.py"
    source = path.read_text(encoding="utf-8")
    counts = _count_definitions(source)
    assert counts == {
        "lead_in_re": 1,
        "aspect_fragments": 1,
        "strip_fn": 1,
    }, f"Duplicate followup symbols detected: {counts}"


def test_strip_followup_leadin_still_works() -> None:
    from agents.intent_router import _strip_followup_leadin, _normalize

    assert _strip_followup_leadin("\u0637\u064a\u0628 \u0643\u0627\u0645 \u0633\u0639\u0631\u0647\u0627\uff1f") == "\u0643\u0627\u0645 \u0633\u0639\u0631\u0647\u0627\uff1f"
    assert _strip_followup_leadin(_normalize("\u0637\u0628 \u0647\u0644 \u0641\u064a\u0647 \u0636\u0645\u0627\u0646")) == "\u0647\u0644 \u0641\u064a\u0647 \u0636\u0645\u0627\u0646"
    assert _strip_followup_leadin("\u0648\u0627\u0644\u0633\u0639\u0631\uff1f") == "\u0648\u0627\u0644\u0633\u0639\u0631\uff1f"
