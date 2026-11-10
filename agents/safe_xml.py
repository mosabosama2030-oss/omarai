"""Stdlib-only XML parsing for untrusted feeds (RSS/Atom/arXiv/sitemaps).

Feeds never need a DTD, so any DOCTYPE or ENTITY declaration is rejected before
parsing. This blocks entity-expansion ("billion laughs") and external-entity
tricks without adding a dependency.
"""
from __future__ import annotations

import re
import xml.etree.ElementTree as ET

_DTD_RE = re.compile(rb"<!\s*(?:DOCTYPE|ENTITY)", re.IGNORECASE)
_DTD_TEXT_RE = re.compile(r"<!\s*(?:DOCTYPE|ENTITY)", re.IGNORECASE)

ParseError = ET.ParseError


def fromstring(data: bytes | str) -> ET.Element:
    """Parse untrusted XML, refusing documents that declare a DTD or entities."""
    if isinstance(data, str):
        blocked = _DTD_TEXT_RE.search(data)
    else:
        # UTF-16 feeds interleave NUL bytes; strip them so the check still sees the markup.
        blocked = _DTD_RE.search(data.replace(b"\x00", b""))
    if blocked:
        raise ET.ParseError("XML DOCTYPE/ENTITY declarations are not allowed")
    return ET.fromstring(data)
