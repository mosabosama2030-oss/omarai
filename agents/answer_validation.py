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
_CITATION = re.compile(r"\[(?:المصدر|source)\s+(\d+)\]", re.IGNORECASE)
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


def _criterion_tokens(value: Any) -> list[str]:
    """Return criterion terms without discarding their original surface forms."""
    tokens = _tokens(value, drop_stopwords=True)
    return tokens or _tokens(value)


_CRITERION_ALIASES = {
    "سعر": ("price", "cost", "pricing", "fee", "amount"),
    "تكلفه": ("price", "cost", "expense", "fee"),
    "بطاريه": ("battery", "capacity", "duration", "battery life"),
    "كاميرا": ("camera", "photography", "image quality", "photo"),
    "خصوصيه": ("privacy", "confidentiality", "data protection"),
    "اعتماديه": ("reliability", "uptime", "dependability"),
    "دعم": ("support", "service", "helpdesk", "customer service"),
    "مساحه": ("area", "size", "space", "sqm"),
    "اداء": ("performance", "speed", "throughput"),
    "امان": ("safety", "security", "protection"),
    "جوده": ("quality", "build quality"),
    "صيانه": ("maintenance", "repair", "servicing"),
    "مميزات": ("features", "benefits", "advantages"),
    "عيوب": ("drawbacks", "disadvantages", "limitations", "cons"),
    "ضمان": ("warranty", "guarantee"),
    "توفر": ("availability", "in stock"),
    "سرعه": ("speed", "latency"),
    "ذاكره": ("memory", "ram", "storage"),
}


def _criterion_token_variants(token: str) -> set[str]:
    """Return conservative Arabic article and common cross-language criterion variants."""
    variants = {token}
    is_arabic = bool(token) and all("ء" <= char <= "ي" for char in token)
    base = token[2:] if is_arabic and token.startswith("ال") and len(token) > 4 else token
    if is_arabic:
        variants.add(base)
        if len(base) >= 3:
            variants.add("ال" + base)
        for alias in _CRITERION_ALIASES.get(base, ()):
            variants.update(_tokens(alias, drop_stopwords=True))
    return variants


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



_VALUE_CUES = {
    "price_or_cost": re.compile(
        r"(?:السعر|سعر|تكلفه|تكلفة|التكاليف|المبلغ|الثمن|price|cost|fee|amount|"
        r"جنيه|دولار|ريال|يورو|egp|usd|eur|\$|€|£)",
        re.IGNORECASE,
    ),
    "area_or_size": re.compile(
        r"(?:المساحه|المساحة|مساحه|مساحة|متر مربع|متر|sqm|square\s+met(?:er|re)s?|area|size)",
        re.IGNORECASE,
    ),
    "duration": re.compile(
        r"(?:المده|المدة|الوقت|مده|مدة|فتره|فترة|duration|elapsed|days?|weeks?|months?|years?|"
        r"يوم|أيام|اسبوع|أسبوع|شهر|أشهر|سنه|سنة|سنوات|عام|أعوام|ساعة|ساعات|دقيقة|دقائق)",
        re.IGNORECASE,
    ),
    "percentage_or_rate": re.compile(
        r"(?:النسبه|النسبة|نسبة|مئويه|مئوية|percent(?:age)?|rate|٪|%)",
        re.IGNORECASE,
    ),
    "date_or_year": re.compile(
        r"(?:التاريخ|تاريخ|الموعد|موعد|صدر|نشر|بتاريخ|date|published|year|deadline|"
        r"يناير|فبراير|مارس|ابريل|أبريل|مايو|يونيو|يوليو|أغسطس|سبتمبر|أكتوبر|نوفمبر|ديسمبر)",
        re.IGNORECASE,
    ),
}


def _numeric_values_with_cues(value: Any) -> list[tuple[str, str]]:
    """Extract number/dimension pairs as review signals, not as semantic claims."""
    text = _normalize(value)
    found: list[tuple[str, str]] = []
    for match in _NUMBER.finditer(text):
        number = _canonical_number(match.group(0))
        context = text[max(0, match.start() - 55):min(len(text), match.end() + 55)]
        for dimension, pattern in _VALUE_CUES.items():
            if pattern.search(context):
                found.append((dimension, number))
    return found


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
    source_text_by_index: dict[int, str] = {}

    for source_index, source in enumerate(safe_sources[:40], 1):
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
            bounded_source_text = source_text[:16000]
            source_texts.append(bounded_source_text)
            source_text_by_index[source_index] = bounded_source_text
            source_number_literals.update(_numeric_literals(bounded_source_text))

    answer_text = str(answer or "")[:24000]
    answer_number_literals = _numeric_literals(answer_text, question=question)
    unsupported_numbers = sorted(answer_number_literals - source_number_literals)
    answer_tokens = set(_criterion_tokens(_CITATION.sub(" ", answer_text)))

    # Align citation-bearing sentences only by lexical overlap with the exact cited
    # source index. This is an audit hint, not an entailment or truth check.
    citable_sources = safe_sources[:12]
    source_token_sets: list[set[str]] = []
    source_bases: list[str] = []
    for source in citable_sources:
        page_text = str(source.get("page_text") or "")
        snippet = str(source.get("snippet") or "")
        title = str(source.get("title") or "")
        if bool(source.get("page_fetched")) and page_text.strip():
            selected_text = page_text
            basis = "extracted_page_text"
        elif snippet.strip():
            selected_text = snippet
            basis = "search_snippet"
        elif title.strip():
            selected_text = title
            basis = "title_only"
        else:
            selected_text = ""
            basis = "no_readable_text"
        source_token_sets.append(set(_tokens(selected_text, drop_stopwords=True)))
        source_bases.append(basis)

    citation_alignment: list[dict[str, Any]] = []
    sentence_parts = [
        part.strip()
        for part in re.split(r"(?<=[.!?؟])\s+|\n+", answer_text)
        if part.strip()
    ]
    for sentence_number, sentence in enumerate(sentence_parts[:40], 1):
        cited_indices = [
            int(match.group(1))
            for match in _CITATION.finditer(sentence)
        ]
        if not cited_indices:
            continue
        claim_tokens = list(dict.fromkeys(_tokens(_CITATION.sub(" ", sentence), drop_stopwords=True)))
        cited_checks: list[dict[str, Any]] = []
        for source_index in list(dict.fromkeys(cited_indices))[:8]:
            if source_index < 1 or source_index > len(source_token_sets):
                cited_checks.append({
                    "source_index": source_index,
                    "status": "source_index_out_of_scope",
                    "evidence_basis": "unavailable",
                    "matched_terms": [],
                    "overlap_ratio": 0.0,
                })
                continue
            available_tokens = source_token_sets[source_index - 1]
            overlap = [token for token in claim_tokens if token in available_tokens]
            ratio = len(overlap) / len(claim_tokens) if claim_tokens else 0.0
            # A lexical match is only a weak proxy for relevance, not entailment.
            # Require both relative coverage and at least two content-token matches.
            enough_overlap = len(overlap) >= 2 and ratio >= 0.5
            cited_checks.append({
                "source_index": source_index,
                "status": "lexical_overlap_signal_found" if enough_overlap else "weak_lexical_overlap",
                "evidence_basis": source_bases[source_index - 1],
                "matched_terms": overlap[:8],
                "overlap_ratio": round(ratio, 3),
            })
        sentence_status = (
            "lexical_overlap_signal_found"
            if any(item["status"] == "lexical_overlap_signal_found" for item in cited_checks)
            else "weak_lexical_overlap"
        )
        citation_alignment.append({
            "sentence_number": sentence_number,
            "status": sentence_status,
            "claim_terms_checked": claim_tokens[:16],
            "citations": cited_checks,
        })


    # Check numeric literals against the exact source indices cited in each sentence.
    # Values found in some unrelated source do not count as support for this citation.
    source_numbers_by_index = {
        index: _numeric_literals(text)
        for index, text in source_text_by_index.items()
    }
    citation_numeric_support: list[dict[str, Any]] = []
    for sentence_number, sentence in enumerate(sentence_parts[:40], 1):
        cited_indices = list(dict.fromkeys(
            int(match.group(1)) for match in _CITATION.finditer(sentence)
        ))
        if not cited_indices:
            continue
        claim_numbers = sorted(_numeric_literals(sentence, question=question))
        valid_indices = [index for index in cited_indices if 1 <= index <= len(citable_sources)]
        supported_numbers = {
            number
            for number in claim_numbers
            if any(number in source_numbers_by_index.get(index, set()) for index in valid_indices)
        }
        unsupported_for_citation = [
            number for number in claim_numbers if number not in supported_numbers
        ]
        citation_numeric_support.append({
            "sentence_number": sentence_number,
            "cited_source_indexes": cited_indices[:8],
            "claim_numeric_literals": claim_numbers[:30],
            "potentially_unsupported_numeric_literals": unsupported_for_citation[:30],
            "status": (
                "potentially_unsupported_numeric_literals_for_cited_sources"
                if unsupported_for_citation
                else "numeric_literals_seen_in_cited_source_text"
                if claim_numbers and valid_indices
                else "no_numeric_literals_to_check"
                if not claim_numbers
                else "not_assessable_no_readable_cited_source"
            ),
        })

    value_evidence: dict[str, list[dict[str, Any]]] = {}
    for source_index in source_text_by_index:
        source = safe_sources[source_index - 1]
        page_text = str(source.get("page_text") or "")
        snippet = str(source.get("snippet") or "")
        selected_evidence = page_text if bool(source.get("page_fetched")) and page_text.strip() else snippet
        if not selected_evidence.strip():
            selected_evidence = str(source.get("title") or "")
        for dimension, number in _numeric_values_with_cues(selected_evidence):
            value_evidence.setdefault(dimension, []).append({
                "source_index": source_index,
                "value": number,
            })
    potential_value_discrepancies: list[dict[str, Any]] = []
    for dimension, entries in sorted(value_evidence.items()):
        unique_values = list(dict.fromkeys(entry["value"] for entry in entries))
        source_indexes = sorted({entry["source_index"] for entry in entries})
        if len(unique_values) < 2 or len(source_indexes) < 2:
            continue
        by_value = []
        for value in unique_values[:8]:
            supporting_indexes = sorted({
                entry["source_index"] for entry in entries if entry["value"] == value
            })
            by_value.append({"value": value, "source_indexes": supporting_indexes[:8]})
        potential_value_discrepancies.append({
            "dimension": dimension,
            "values": by_value,
            "source_indexes": source_indexes[:12],
            "status": "potential_variation_or_conflict_requires_entity_review",
        })

    weak_citation_alignment_count = sum(
        item["status"] == "weak_lexical_overlap"
        for item in citation_alignment
    )
    target_checks: list[dict[str, Any]] = []
    source_evidence_gap_count = 0
    for target in (coverage_targets or [])[:8]:
        target_tokens = list(dict.fromkeys(_criterion_tokens(target)))
        overlap = [token for token in target_tokens if token in answer_tokens]
        ratio = len(overlap) / len(target_tokens) if target_tokens else 0.0
        likely_covered = bool(overlap) and (
            ratio >= 0.5 if len(target_tokens) > 1 else True
        )

        # Track criterion-level source signals separately from answer wording.
        # A term appearing in a source is not proof that the source supports a claim;
        # this is a bounded retrieval/evidence diagnostic only.
        source_checks: list[dict[str, Any]] = []
        for source_index, source in enumerate(safe_sources[:40], 1):
            page_text = str(source.get("page_text") or "")
            snippet = str(source.get("snippet") or "")
            title = str(source.get("title") or "")
            if bool(source.get("page_fetched")) and page_text.strip():
                selected_text, basis = page_text, "extracted_page_text"
            elif snippet.strip():
                selected_text, basis = snippet, "search_snippet"
            elif title.strip():
                selected_text, basis = title, "title_only"
            else:
                continue
            source_tokens = set(_criterion_tokens(selected_text[:16000]))
            source_match_tokens = set().union(*(
                _criterion_token_variants(token) for token in source_tokens
            )) if source_tokens else set()
            source_overlap = [
                token for token in target_tokens
                if _criterion_token_variants(token) & source_match_tokens
            ]
            source_ratio = len(source_overlap) / len(target_tokens) if target_tokens else 0.0
            source_signal = bool(source_overlap) and (
                source_ratio >= 0.5 if len(target_tokens) > 1 else True
            )
            if source_signal:
                source_checks.append({
                    "source_index": source_index,
                    "status": "lexical_signal_found",
                    "evidence_basis": basis,
                    "matched_terms": source_overlap[:8],
                    "token_overlap_ratio": round(source_ratio, 3),
                })
        if not source_checks:
            source_evidence_gap_count += 1
        target_checks.append({
            "target": str(target)[:120],
            "status": "lexical_signal_found" if likely_covered else "possibly_missing",
            "matched_terms": overlap[:12],
            "missing_terms": [token for token in target_tokens if token not in answer_tokens][:12],
            "token_overlap_ratio": round(ratio, 3),
            "source_evidence_status": (
                "source_lexical_signal_found" if source_checks else "no_source_lexical_signal"
            ),
            "source_evidence_checks": source_checks[:12],
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
        "citation_lexical_alignment_method": "content_word_overlap_heuristic_not_entailment",
        "citation_lexical_alignment": citation_alignment[:30],
        "weak_citation_alignment_count": weak_citation_alignment_count,
        "citation_numeric_support": citation_numeric_support[:30],
        "potentially_unsupported_numeric_by_citation_count": sum(
            len(item["potentially_unsupported_numeric_literals"])
            for item in citation_numeric_support
        ),
        "potential_value_discrepancies": potential_value_discrepancies[:8],
        "potential_value_discrepancy_count": len(potential_value_discrepancies),
        "numeric_check_status": numeric_status,
        "checked_numeric_literals": sorted(answer_number_literals)[:40],
        "potentially_unsupported_numeric_literals": unsupported_numbers[:40],
        "potentially_unsupported_numeric_count": len(unsupported_numbers),
        "target_coverage": target_checks,
        "potentially_missing_target_count": sum(
            item["status"] == "possibly_missing" for item in target_checks
        ),
        "source_evidence_gap_count": source_evidence_gap_count,
        "source_evidence_assessment": "criterion_level_lexical_signals_not_claim_support_or_entailment",
        "limitations": [
            "Token overlap does not prove that an answer fulfills the intended task.",
            "A number appearing in any source does not prove that the source supports the claim.",
            "Citation token overlap can be coincidental and does not establish that the source entails the claim.",
            "Value-discrepancy flags may reflect different products, periods, or units; they are not automatic contradiction findings.",
            "Contradictory sources and citation-to-claim entailment require claim-level review.",
            "Search snippets may be partial; extracted page text is still not independent verification.",
        ],
    }
