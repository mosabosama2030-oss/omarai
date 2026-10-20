"""Generate Omarai MASTER_INDEX.md (multi-section code index)."""
from __future__ import annotations
import sys
import types
from pathlib import Path as _Path

_d = _Path(__file__).resolve().parent
_code = (_d / "_index_part1.txt").read_text(encoding="utf-8") + (_d / "_index_part2.txt").read_text(encoding="utf-8")
if __name__ not in sys.modules:
    sys.modules[__name__] = types.ModuleType(__name__)
else:
    # Keep the real module object used by importlib
    pass
exec(compile(_code, str(_d / "generate_index.py"), "exec"), globals())
