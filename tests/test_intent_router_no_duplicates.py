from __future__ import annotations

import inspect
from pathlib import Path

import agents.intent_router as intent_router


def test_no_duplicate_followup_symbol_definitions() -> None:
    """Ensure follow-up lead-in symbols are defined only once.

    Duplicate definitions previously appeared after merge conflicts and could
    silently override earlier constants. This test fails if they reappear.
    """
    source = inspect.getsource(intent_router)
    assert source.count("_FOLLOWUP_LEAD_IN_RE = re.compile") == 1
    assert source.count("_FOLLOWUP_ASPECT_FRAGMENTS = frozenset") == 1
    assert source.count("def _strip_followup_leadin") == 1

    # Sanity: the strip function is usable
    assert intent_router._strip_followup_leadin("طيب السعر") == "السعر"
