"""Regression tests ensuring no duplicate follow-up symbol definitions in intent_router."""

import inspect
import re

from agents import intent_router


def test_no_duplicate_followup_leadin_symbols():
    """Ensure exactly one definition of each follow-up helper symbol.

    Residual duplicate assignments of _FOLLOWUP_LEAD_IN_RE, _FOLLOWUP_ASPECT_FRAGMENTS,
    and _strip_followup_leadin risked silent override of the canonical Arabic/English
    follow-up stripping and aspect detection logic.
    """
    source = inspect.getsource(intent_router)
    lead_count = len(re.findall(r"^_FOLLOWUP_LEAD_IN_RE\s*=", source, re.MULTILINE))
    aspect_count = len(re.findall(r"^_FOLLOWUP_ASPECT_FRAGMENTS\s*=", source, re.MULTILINE))
    strip_count = len(re.findall(r"^def _strip_followup_leadin\b", source, re.MULTILINE))
    assert lead_count == 1, f"Expected 1 _FOLLOWUP_LEAD_IN_RE, found {lead_count}"
    assert aspect_count == 1, f"Expected 1 _FOLLOWUP_ASPECT_FRAGMENTS, found {aspect_count}"
    assert strip_count == 1, f"Expected 1 _strip_followup_leadin, found {strip_count}"


def test_strip_followup_leadin_works():
    """Smoke test that the single canonical stripper still functions."""
    assert intent_router._strip_followup_leadin("\u0637\u064a\u0628 \u0627\u0644\u0633\u0639\u0631 \u0643\u0627\u0645") == "\u0627\u0644\u0633\u0639\u0631 \u0643\u0627\u0645"
    assert intent_router._strip_followup_leadin("okay what about the price") == "what about the price"
    assert intent_router._strip_followup_leadin("\u0627\u0644\u0633\u0639\u0631") == "\u0627\u0644\u0633\u0639\u0631"
