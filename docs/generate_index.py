"""Generate Omarai MASTER_INDEX.md (multi-section code index)."""
from __future__ import annotations
import base64
import sys
import types
import zlib
from pathlib import Path as _Path

_d = _Path(__file__).resolve().parent
_b64 = "".join(
    (_d / ("_index_z%d.b64" % i)).read_text(encoding="ascii").strip()
    for i in range(1, 3 + 1)
)
_code = zlib.decompress(base64.b64decode(_b64)).decode("utf-8")
if __name__ not in sys.modules:
    sys.modules[__name__] = types.ModuleType(__name__)
exec(compile(_code, str(_d / "generate_index.py"), "exec"), globals())
