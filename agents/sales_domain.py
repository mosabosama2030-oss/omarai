"""Provider-independent domain contracts for Omarai sales intelligence.

These models describe evidence and assessments; they do not discover buyers,
infer identity, calculate purchase probability, or execute external actions.
Storage and API integration are deliberately kept separate from this module.
"""
from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from collections.abc import Iterable
from datetime import date, datetime
from enum import Enum
from urllib.parse import urlsplit


MAX_NAME_LENGTH = 240
MAX_TEXT_LENGTH = 2_000
MAX_TERM_COUNT = 64
_MAX_CATEGORY_DEPTH = 8

_ARABIC_MARKS = re.compile(r"[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED]")
_PUNCTUATION = re.compile(r"[\s\t\r\n.,،؛;:!?؟()\[\]{}<>\"'«»]+")
_SPACE = re.compile(r"\s+")

# NOTE: full file content continues in subsequent push if needed - this is incomplete marker
