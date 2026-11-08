"""Omarai lead-intent agent package."""

from __future__ import annotations


def _apply_meta_tail_fix() -> None:
    """Rebind research meta-tail patterns after research is importable."""
    try:
        from importlib import import_module

        research = import_module("agents.research")
        meta = import_module("agents.search_meta_tail")
    except Exception:
        return

    research._SEARCH_META_TAIL_RE = meta.SEARCH_META_TAIL_RE
    orig = research.compact_search_query

    def compact_search_query(value, limit=None):
        if limit is None:
            limit = research.MAX_QUERY_CHARS
        out = orig(value, limit)
        return meta.strip_trailing_conjunctions(out) if out else out

    research.compact_search_query = compact_search_query  # type: ignore[assignment]


try:
    _apply_meta_tail_fix()
except Exception:
    # Package import must stay side-effect safe if research is unavailable.
    pass
