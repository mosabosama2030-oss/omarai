"""Regression tests ensuring follow-up lead-in symbols are defined only once.

Duplicate definitions of _FOLLOWUP_LEAD_IN_RE, _FOLLOWUP_ASPECT_FRAGMENTS,
and _strip_followup_leadin previously survived incomplete merges on main.
This test prevents their reintroduction.
"""
from __future__ import annotations

import ast
from pathlib import Path

import pytest


def test_no_duplicate_followup_leadin_symbols():
    """Follow-up lead-in symbols must be defined exactly once in intent_router.py."""
    src_path = Path("agents/intent_router.py")
    assert src_path.is_file(), "agents/intent_router.py missing"
    src = src_path.read_text(encoding="utf-8")
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

    assert len(strip_defs) == 1, f"Expected exactly 1 _strip_followup_leadin definition, found {len(strip_defs)}"
    assert len(lead_assigns) == 1, f"Expected exactly 1 _FOLLOWUP_LEAD_IN_RE assignment, found {len(lead_assigns)}"
    assert len(aspect_assigns) == 1, f"Expected exactly 1 _FOLLOWUP_ASPECT_FRAGMENTS assignment, found {len(aspect_assigns)}"


def test_strip_followup_leadin_still_works():
    """Smoke test that the (now unique) strip helper still functions."""
    from agents.intent_router import _strip_followup_leadin
    assert _strip_followup_leadin("طيب كام سعرها") == "كام سعرها"
    assert _strip_followup_leadin("well what about the price") == "what about the price"
    assert _strip_followup_leadin("كام سعرها") == "كام سعرها"
