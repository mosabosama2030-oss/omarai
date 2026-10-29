"""Sentence-level source tracing for Omarai.

This maps citation markers to the exact bounded source list sent to the model.
It does not prove truth, citation entailment, or semantic completeness.
"""
from __future__ import annotations

import re
import unicodedata
from typing import Any
from urllib.parse import urlsplit

_CITATION = re.compile(r"\[(?:المصدر|source)\s+(\d+)\]", re.IGNORECASE)
_SENTENCE_SPLIT = re.compile(r"(?<=[.!?؟])\s+|\n+")


def _evidence_basis(source: dict[str, Any]) -> str:
    if bool(source.get("page_fetched")) and str(source.get("page_text") or "").strip():
        return "extracted_page_text"
    if str(source.get("snippet") or "").strip():
        return "search_snippet"
    if str(source.get("title") or "").strip():
        return "title_only"
    return "no_readable_evidence"



_POPULATION_CLAIM = re.compile(
    r"(?:population|inhabitants|number of people|how many people|people live in|عدد\s+(?:ال)?سكان|(?:ال)?سكان|"
    r"نسمة|القاهره\s+الكبرى|محافظه\s+القاهره|الكثافه\s+السكانيه)",
    re.IGNORECASE,
)
_ARABIC_CLAIM_TRANSLATION = str.maketrans({
    "أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا", "ى": "ي", "ة": "ه",
})


def requires_population_scope(claim_text: str) -> bool:
    """Detect population claims conservatively; this is a routing hint, not NLU verification."""
    normalized = unicodedata.normalize("NFKC", str(claim_text or "")).casefold()
    normalized = normalized.translate(_ARABIC_CLAIM_TRANSLATION)
    return bool(_POPULATION_CLAIM.search(normalized))


def audit_source_metadata(
    source: dict[str, Any], *, claim_text: str = ""
) -> dict[str, Any]:
    """Audit traceability metadata without fetching URLs or asserting claim truth."""
    item = source if isinstance(source, dict) else {}
    raw_url = str(item.get("url") or "").strip()
    try:
        parsed = urlsplit(raw_url)
        # Accessing .port validates malformed ports; URLs are never fetched here.
        _ = parsed.port
        valid_url = (
            parsed.scheme.lower() in {"http", "https"}
            and bool(parsed.hostname)
            and parsed.username is None
            and parsed.password is None
            and not any(char.isspace() for char in raw_url)
        )
    except (TypeError, ValueError):
        valid_url = False

    title = str(item.get("title") or "").strip()
    publisher = str(
        item.get("publisher") or item.get("source_name") or item.get("domain") or ""
    ).strip()

    def first_value(keys: tuple[str, ...]) -> str:
        for key in keys:
            value = item.get(key)
            if value is not None and str(value).strip():
                return str(value).strip()
        return ""

    publication_date = first_value((
        "published_at", "published_date", "publication_date", "date_published",
        "published", "date",
    ))
    data_period = first_value((
        "data_date", "data_reference_date", "reference_date", "data_as_of",
        "data_period", "reference_period", "observation_date", "data_year",
        "reference_year", "period", "year",
    ))
    geographic_scope = str(
        item.get("geographic_scope") or item.get("geography")
        or item.get("scope") or item.get("population_definition") or ""
    ).strip()
    readable = (
        (bool(item.get("page_fetched")) and bool(str(item.get("page_text") or "").strip()))
        or bool(str(item.get("snippet") or "").strip())
    )
    population_required = requires_population_scope(claim_text)

    missing: list[str] = []
    if not valid_url:
        missing.append("valid_http_source_url")
    if not title:
        missing.append("source_title")
    if not publisher:
        missing.append("publisher_identity_or_domain")
    if not publication_date:
        missing.append("publication_date")
    if population_required and not data_period:
        missing.append("data_reference_period_for_population_claim")
    if population_required and not geographic_scope:
        missing.append("geographic_scope_for_population_claim")
    if not readable:
        missing.append("readable_source_evidence")

    return {
        "status": "metadata_complete" if not missing else "metadata_incomplete",
        "valid_http_url": valid_url,
        "has_title": bool(title),
        "has_publisher_identity": bool(publisher),
        "has_publication_date": bool(publication_date),
        "has_data_reference_period": bool(data_period),
        "population_scope_required": population_required,
        "has_geographic_scope": bool(geographic_scope),
        "has_readable_evidence": readable,
        "required_fields_missing": missing,
        "claim_entailment": "not_checked",
        "fact_correctness": "not_checked",
        "semantic_verification": False,
        "limitations": [
            "Metadata presence does not validate source authenticity, date correctness, or claim support.",
            "Publication date and data reference period are separate fields.",
            "Population scope must be explicitly supplied; administrative boundaries are not inferred.",
        ],
    }

def build_claim_evidence_ledger(
    answer: str,
    sources: list[dict[str, Any]] | None,
    answer_integrity: dict[str, Any] | None = None,
    *,
    max_segments: int = 40,
    max_citable_sources: int = 12,
    question_context: str = "",
) -> dict[str, Any]:
    """Return bounded sentence candidates with validated source-index traceability."""
    safe_answer = str(answer or "")[:24000]
    safe_sources = [
        source for source in (sources or []) if isinstance(source, dict)
    ][:max(0, min(int(max_citable_sources), 40))]
    segments = [
        part.strip()
        for part in _SENTENCE_SPLIT.split(safe_answer)
        if part and part.strip()
    ]
    truncated = len(segments) > max_segments
    segments = segments[:max(0, min(int(max_segments), 100))]
    integrity = answer_integrity if isinstance(answer_integrity, dict) else {}
    alignments = integrity.get("citation_lexical_alignment")
    alignment_by_sentence = {
        int(item["sentence_number"]): item
        for item in alignments
        if isinstance(item, dict) and isinstance(item.get("sentence_number"), int)
    } if isinstance(alignments, list) else {}

    rows: list[dict[str, Any]] = []
    valid_refs = invalid_refs = cited = uncited = readable_cited = 0
    lexical_signals = weak_signals = 0

    for number, segment in enumerate(segments, 1):
        indexes = list(dict.fromkeys(int(m.group(1)) for m in _CITATION.finditer(segment)))[:8]
        refs: list[dict[str, Any]] = []
        has_readable = False
        for index in indexes:
            if index < 1 or index > len(safe_sources):
                invalid_refs += 1
                refs.append({
                    "source_index": index, "reference_status": "index_out_of_citable_range",
                    "title": "", "url": "", "evidence_basis": "unavailable",
                })
                continue
            source = safe_sources[index - 1]
            basis = _evidence_basis(source)
            valid_refs += 1
            # Titles are useful metadata, but not readable source text for checking entailment.
            has_readable = has_readable or basis in {"extracted_page_text", "search_snippet"}
            refs.append({
                "source_index": index,
                "reference_status": (
                    "valid_index_with_readable_evidence"
                    if basis in {"extracted_page_text", "search_snippet"}
                    else "valid_index_without_readable_evidence"
                ),
                "title": str(source.get("title") or "")[:240],
                "url": str(source.get("url") or "")[:2048],
                "provider": str(source.get("provider") or "")[:80],
                "evidence_basis": basis,
                "metadata_audit": audit_source_metadata(source, claim_text=f"{question_context} {segment}"),
            })

        cited += bool(indexes)
        uncited += not bool(indexes)
        readable_cited += bool(indexes) and has_readable
        alignment = alignment_by_sentence.get(number, {})
        lexical_status = str(alignment.get("status") or "not_assessed_no_citation_alignment")
        lexical_signals += lexical_status == "lexical_overlap_signal_found"
        weak_signals += lexical_status == "weak_lexical_overlap"
        if any(ref["reference_status"] == "index_out_of_citable_range" for ref in refs):
            status = "citation_index_out_of_range"
        elif indexes and not has_readable:
            status = "valid_index_without_readable_evidence"
        elif indexes:
            status = "cited_source_attached"
        else:
            status = "no_citation_marker"

        rows.append({
            "segment_id": f"S{number:03d}",
            "segment_number": number,
            "unit_kind": "sentence_candidate_not_semantically_classified",
            "text": segment[:1200],
            "citation_indexes": indexes,
            "citation_status": status,
            "lexical_audit_status": lexical_status,
            "sources": refs,
        })

    total = len(rows)
    return {
        "schema_version": "1.0",
        "status": "built",
        "method": "bounded_sentence_level_citation_trace",
        "semantic_verification": False,
        "claim_entailment": "not_checked",
        "fact_correctness": "not_checked",
        "max_segments": max_segments,
        "max_citable_sources": len(safe_sources),
        "truncated": truncated,
        "summary": {
            "segment_candidate_count": total,
            "segments_with_citations": cited,
            "segments_without_citation_markers": uncited,
            "valid_source_reference_count": valid_refs,
            "out_of_range_reference_count": invalid_refs,
            "cited_segments_with_readable_source_evidence": readable_cited,
            "citation_lexical_signal_count": lexical_signals,
            "weak_citation_lexical_signal_count": weak_signals,
            "citation_coverage_ratio": round(cited / total, 3) if total else 0.0,
        },
        "segments": rows,
        "limitations": [
            "Sentence candidates are not independently classified into semantic claims.",
            "An in-range index proves only that the source was in the bounded list.",
            "Readable text and lexical overlap do not prove that a source entails a claim.",
            "Correctness, source independence, contradiction resolution, and semantic faithfulness were not verified.",
        ],
    }
