"""Omarai lead-intent agent package."""

# Load search_meta_tail early so it can rebind research._SEARCH_META_TAIL_RE
# once agents.research is available (cycle-safe).
from . import search_meta_tail as _search_meta_tail  # noqa: F401
