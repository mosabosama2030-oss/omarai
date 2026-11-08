"""Shared search-query meta-tail patterns for compact_search_query."""
from __future__ import annotations

import re

# Citation/format tails may appear after punctuation OR after a plain conjunction
# space (e.g. "السيارات ... واذكر مصادر") without a preceding comma.
SEARCH_META_TAIL_RE = re.compile(
    r"(?:\s*[,،؛;]\s*|\s+)(?:(?:و\s*)|(?:and\s+))?(?:"
    r"استخدم\s+مصادر|استعمل\s+مصادر|ميّز\s+بين\s+الحقائق|ميز\s+بين\s+الحقائق|"
    r"اجب\b|أجب\b|لا تعرض|لا تقدم|"
    r"please cite|cite\b|provide links|mention sources|use multiple sources|"
    r"don't present|do not present|"
    r"اذكر(?:ي|وا)?\s+(?:مصادر?|المصادر|مصدر|روابط?|رابط|تواريخ?|تاريخ|الاخبار|الأخبار)"
    r")\b.*$",
    re.IGNORECASE,
)


def strip_trailing_conjunctions(text: str) -> str:
    """Drop trailing Arabic/English conjunctions left after meta-tail removal."""
    return re.sub(r"(?:\s+(?:و|and))+\s*$", "", text, flags=re.IGNORECASE).strip()
