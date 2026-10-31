"""Regression: ensure follow-up lead-in symbols are defined only once."""
from pathlib import Path

def test_no_duplicate_followup_leadin_symbols():
    src = Path("agents/intent_router.py").read_text(encoding="utf-8")
    assert src.count("_FOLLOWUP_LEAD_IN_RE = re.compile") == 1
    assert src.count("_FOLLOWUP_ASPECT_FRAGMENTS = frozenset") == 1
    assert src.count("def _strip_followup_leadin") == 1
