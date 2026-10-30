from __future__ import annotations

import re
from pathlib import Path


def test_followup_symbols_are_defined_once() -> None:
    """Prevent the residual duplicate definitions of follow-up helpers from returning."""
    source = Path("agents/intent_router.py").read_text(encoding="utf-8")
    assert len(re.findall(r"^_FOLLOWUP_LEAD_IN_RE = ", source, flags=re.MULTILINE)) == 1
    assert len(re.findall(r"^_FOLLOWUP_ASPECT_FRAGMENTS = ", source, flags=re.MULTILINE)) == 1
    assert len(re.findall(r"^def _strip_followup_leadin\(", source, flags=re.MULTILINE)) == 1
