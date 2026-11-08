"""Omarai lead-intent agent package."""

# Bind the expanded citation/format meta-tail regex into research at import time.
# This avoids shipping a full rewrite of agents/research.py for a one-pattern fix.
try:
    from agents import research as _research
    from agents.search_meta_tail import SEARCH_META_TAIL_RE as _SEARCH_META_TAIL_RE

    _research._SEARCH_META_TAIL_RE = _SEARCH_META_TAIL_RE
except Exception:
    # Keep package import resilient if research is unavailable in partial environments.
    pass
