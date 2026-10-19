"""Conservative, deterministic screening for answer evidence and task coverage.

These checks are lexical guardrails. They cannot establish that a statement is true,
that a citation entails a claim, or that a task was semantically completed.
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
_NUMBER = re.compile(r"(?<![\w])\d+(?:[.,٬٫]\d+)*(?![\w])")
_CITATION = re.compile(r"\[(?:المصدر|source)\s+\d+\]", re.IGNORECASE)
_STOPWORDS = {
    "من", "في", "على", "عن", "الى", "و", "او", "هل", "ما", "ماذا", "كيف",
    "مع", "بين", "هذا", "هذه", "ذلك", "تلك", "الذي", "التي", "هو", "هي",
    "the", "a", "an", "and", "or", "in", "on", "of", "to", "for", "with",
    "from", "is", "are", "what", "which", "who", "how", "why", "when",
    "where", "compare", "comparison", "based", "terms", "respect",
}
_UNIT_OR_VALUE_CONTEXT = re.compile(
    r"(?:جنيه|ج\.م|دولار|ريال|يورو|درهم|egp|usd|eur|\$|€|£|%|٪|"
    r"متر|مربع|كيلومتر|كلم|كم|كيلو|كجم|kg|km|gb|mb|tb|"
    r"سنة|سنوات|عام|أعوام|شهر|أشهر|يوم|أيام|ساعة|ساعات|دقيقة|دقائق|"
    r"مليون|مليار|ألف|الف|فدان|درجة|شخص|أشخاص)",
    re.IGNORECASE,
)


def _normalize(value: Any) -> str:
    text = unicodedata.normalize("NFKC", str(value or "")).casefold().translate(_DIGITS)
    text = _DIACRITICS.sub("", text).translate(_ARABIC_NORMALIZATION)
    return text


def _tokens(value: Any, *, drop_stopwords: bool = False) -> list[str]:
    tokens = _TOKEN.findall(_normalize(value))
    if drop_stopwords:
        tokens = [token for token in tokens if token not in _STOPWORDS]
    return tokens


def _numeric_literals(value: Any, *, question: str = "") -> set[str]:
    """Extract explicit numeric literals, ignoring citation indices and unqualified single digits."""
    text = _normalize(_CITATION.sub(" ", str(value or "")))
    question_literals = {
        _canonical_number(match.group(0))
        for match in _NUMBER.finditer(_normalize(question))
    }
    result: set[str] = set()
    for match in _NUMBER.finditer(text):
        raw = match.group(0)
        context = text[max(0, match.start() - 24):min(len(text), match.end() + 24)]
        canonical = _canonical_number(raw)
        digit_count = sum(char.isdigit() for char in canonical)
        is_year = len(canonical) == 4 and canonical.startswith(("19", "20"))
        if digit_count < 2 and not is_year and not _UNIT_OR_VALUE_CONTEXT.search(context):
            continue
        if canonical and canonical not in question_literals:
            result.add(canonical)
    return result


def _canonical_number(value: str) -> str:
    text = _normalize(value).replace("٬", ",").replace("٫", ".")
    # Treat conventional comma thousands separators as formatting, not a value change.
    text = re.sub(r"(?<=\d),(?=\d{3}(?:\D|$))", "", text)
    return text.replace(",", "")


def audit_answer_integrity(
    question: str,
    answer: str,
    sources: list[dict[str, Any]] | None,
    coverage_targets: list[str] | None = None,
) -> dict[str, Any]:
    """Return bounded lexical checks; never label them as semantic fact verification."""
    safe_sources = [item for item in (sources or []) if isinstance(item, dict)]
    source_texts: list[str] = []
    extracted_page_count = 0
    snippet_count = 0
    source_number_literals: set[str] = set()

    for source in safe_sources[:40]:
        page_text = str(source.get("page_text") or "")
        snippet = str(source.get("snippet") or "")
        title = str(source.get("title") or "")
        published_at = str(source.get("published_at") or "")
        if page_text.strip() and bool(source.get("page_fetched")):
            extracted_page_count += 1
        elif snippet.strip():
            snippet_count += 1
        source_text = " ".join(part for part in (title, snippet, page_text, published_at) if part)
        if source_text.strip():
            source_texts.append(source_text[:16000])
            source_number_literals.update(_numeric_literals(source_text))

    answer_text = str(answer or "")[:24000]
    answer_number_literals = _numeric_literals(answer_text, question=question)
    unsupported_numbers = sorted(answer_number_literals - source_number_literals)
    answer_tokens = set(_tokens(_CITATION.sub(" ", answer_text), drop_stopwords=True))
    target_checks: list[dict[str, Any]] = []
    for target in (coverage_targets or [])[:8]:
        target_tokens = list(dict.fromkeys(_tokens(target, drop_stopwords=True)))
        if not target_tokens:
            target_tokens = list(dict.fromkeys(_tokens(target)))
        overlap = [token for token in target_tokens if token in answer_tokens]
        ratio = len(overlap) / len(target_tokens) if target_tokens else 0.0
        likely_covered = bool(overlap) and (
            ratio >= 0.5 if len(target_tokens) > 1 else True
        )
        target_checks.append({
            "target": str(target)[:120],
            "status": "lexical_signal_found" if likely_covered else "possibly_missing",
            "matched_terms": overlap[:12],
            "missing_terms": [token for token in target_tokens if token not in answer_tokens][:12],
            "token_overlap_ratio": round(ratio, 3),
        })

    citation_count = len(re.findall(r"\[(?:المصدر|source)\s+\d+\]", answer_text, re.IGNORECASE))
    if extracted_page_count:
        source_scope = "contains_extracted_page_text_and_or_snippets"
    elif snippet_count:
        source_scope = "search_snippets_only"
    else:
        source_scope = "no_readable_source_text"

    if not source_texts:
        numeric_status = "not_assessable_no_readable_source_text"
    elif unsupported_numbers:
        numeric_status = "potentially_unsupported_numeric_literals"
    elif answer_number_literals:
        numeric_status = "all_checked_numeric_literals_appear_in_source_text"
    else:
        numeric_status = "no_specific_numeric_literals_checked"

    return {
        "method": "deterministic_lexical_screen_only",
        "semantic_verification": False,
        "independent_fact_check": False,
        "answer_nonempty": bool(answer_text.strip()),
        "source_count": len(safe_sources),
        "source_evidence_scope": source_scope,
        "pages_with_extracted_text": extracted_page_count,
        "sources_with_snippets_only": snippet_count,
        "citation_marker_count": citation_count,
        "citation_entailment": "not_checked",
        "numeric_check_status": numeric_status,
        "checked_numeric_literals": sorted(answer_number_literals)[:40],
        "potentially_unsupported_numeric_literals": unsupported_numbers[:40],
        "potentially_unsupported_numeric_count": len(unsupported_numbers),
        "target_coverage": target_checks,
        "potentially_missing_target_count": sum(
            item["status"] == "possibly_missing" for item in target_checks
        ),
        "limitations": [
            "Token overlap does not prove that an answer fulfills the intended task.",
            "A number appearing in any source does not prove that the source supports the claim.",
            "Contradictory sources and citation-to-claim entailment require claim-level review.",
            "Search snippets may be partial; extracted page text is still not independent verification.",
        ],
    }
