"""Shared public text normalization primitives for Arabic and English matching.

This module owns Unicode/Arabic normalization and token extraction. It has no knowledge
of search, sources, citations, or answer policy.
"""
from __future__ import annotations

import re
import unicodedata
from typing import Any

_DIGITS = str.maketrans("٠١٢٣٤٥٦٧٨٩۰۱۲۳۴۵۶۷۸۹", "01234567890123456789")
_ARABIC_NORMALIZATION = str.maketrans({
    "أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا", "ى": "ي",
    "ؤ": "و", "ئ": "ي", "ة": "ه", "ـ": "",
})
_DIACRITICS = re.compile(r"[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED]")
_TOKEN = re.compile(r"[a-z0-9]+|[\u0621-\u064A\u0660-\u0669]+", re.IGNORECASE)

_STOPWORDS = {
    "من", "في", "على", "عن", "الى", "و", "او", "هل", "ما", "ماذا", "كيف",
    "مع", "بين", "هذا", "هذه", "ذلك", "تلك", "الذي", "التي", "هو", "هي",
    "the", "a", "an", "and", "or", "in", "on", "of", "to", "for", "with",
    "from", "is", "are", "what", "which", "who", "how", "why", "when",
    "where", "compare", "comparison", "based", "terms", "respect",
}

def normalize_text(value: Any) -> str:
    """Normalize Unicode, Arabic letter variants, diacritics, and Arabic-Indic digits."""
    text = unicodedata.normalize("NFKC", str(value or "")).casefold().translate(_DIGITS)
    text = _DIACRITICS.sub("", text).translate(_ARABIC_NORMALIZATION)
    return text


def tokenize_text(value: Any, *, drop_stopwords: bool = False) -> list[str]:
    """Tokenize normalized Arabic/English text with optional stopword removal."""
    tokens = _TOKEN.findall(normalize_text(value))
    if drop_stopwords:
        tokens = [token for token in tokens if token not in _STOPWORDS]
    return tokens
