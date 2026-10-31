"""Build bounded evidence-candidate traces for planned research requirements.

Responsibility: connect up to eight requested coverage targets to up to twelve returned
sources and their query provenance. This is lexical candidate mapping only; it never
claims source entailment, semantic support, or factual correctness.

Public contract: build_requirement_evidence_ledger(targets, sources, requirement_queries)
returns one bounded record per target, with source indexes, evidence basis, and a status.
Dependencies point only to shared text normalization; no network or model calls occur.
"""
from __future__ import annotations

import re
from typing import Any

from agents.text_normalization import normalize_text, tokenize_text

_REQUIREMENT_ALIAS_GROUPS = (
    frozenset({"السعر", "سعر", "تكلفه", "التكلفه", "التكاليف", "الثمن", "price", "cost", "pricing", "fee"}),
    frozenset({"البطاريه", "بطاريه", "battery", "batteries"}),
    frozenset({"الكاميرا", "كاميرا", "camera", "cameras", "تصوير"}),
    frozenset({"ضمان", "الضمان", "warranty", "guarantee"}),
    frozenset({"الخصوصيه", "خصوصيه", "privacy", "الامان", "امان", "security", "safety"}),
    frozenset({"الاعتماديه", "اعتماديه", "reliability", "reliable", "الموثوقيه"}),
    frozenset({"الدعم", "الدعم الفني", "support", "customer service", "خدمه"}),
)


def _alias_token_groups() -> list[set[str]]:
    groups: list[set[str]] = []
    for aliases in _REQUIREMENT_ALIAS_GROUPS:
        tokens: set[str] = set()
        for alias in aliases:
            tokens.update(tokenize_text(alias, drop_stopwords=True))
        groups.append(tokens)
    return groups


def _matched_target_terms(target_tokens: list[str], available_tokens: set[str]) -> list[str]:
    """Match target terms conservatively, with a small explicit Arabic/English alias list."""
    groups = _alias_token_groups()
    matched: list[str] = []
    for token in target_tokens:
        aliases = next((group for group in groups if token in group), {token})
        if aliases.intersection(available_tokens):
            matched.append(token)
    return matched


def build_requirement_evidence_ledger(
    coverage_targets: list[str] | None,
    sources: list[dict[str, Any]] | None,
    requirement_queries: list[dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    """Link requirements to query provenance and lexical source candidates, never to truth."""
    safe_sources = [
        item for item in (sources or [])[:12]
        if isinstance(item, dict)
    ]
    query_rows = [
        item for item in (requirement_queries or [])
        if isinstance(item, dict) and isinstance(item.get("target"), str)
    ]
    query_by_target = {
        normalize_text(item["target"]).strip().casefold(): str(item.get("query") or "").strip()
        for item in query_rows
    }
    any_query_metadata = any(isinstance(item.get("queries"), list) for item in safe_sources)
    ledger: list[dict[str, Any]] = []

    for target in (coverage_targets or [])[:8]:
        target_text = str(target or "")[:120]
        target_tokens = list(dict.fromkeys(tokenize_text(target_text, drop_stopwords=True)))
        if not target_tokens:
            target_tokens = list(dict.fromkeys(tokenize_text(target_text)))
        key = normalize_text(target_text).strip().casefold()
        targeted_query = query_by_target.get(key, "")
        normalized_query = re.sub(r"\s+", " ", targeted_query).strip().casefold()
        query_result_indexes: list[int] = []
        candidate_sources: list[dict[str, Any]] = []

        for source_index, source in enumerate(safe_sources, 1):
            raw_queries = source.get("queries", [])
            source_queries = [
                re.sub(r"\s+", " ", str(value)).strip().casefold()
                for value in raw_queries
            ] if isinstance(raw_queries, list) else []
            if normalized_query and normalized_query in source_queries:
                query_result_indexes.append(source_index)

            page_text = str(source.get("page_text") or "")
            snippet = str(source.get("snippet") or "")
            title = str(source.get("title") or "")
            if bool(source.get("page_fetched")) and page_text.strip():
                candidate_text = page_text
                evidence_basis = "extracted_page_text"
            elif snippet.strip():
                candidate_text = snippet
                evidence_basis = "search_snippet"
            elif title.strip():
                candidate_text = title
                evidence_basis = "title_only"
            else:
                candidate_text = ""
                evidence_basis = "no_readable_text"
            available_tokens = set(tokenize_text(candidate_text, drop_stopwords=True))
            matched_terms = _matched_target_terms(target_tokens, available_tokens)
            ratio = len(matched_terms) / len(target_tokens) if target_tokens else 0.0
            likely_candidate = bool(matched_terms) and (
                ratio >= 0.5 if len(target_tokens) > 1 else True
            )
            if likely_candidate:
                candidate_sources.append({
                    "source_index": source_index,
                    "matched_target_terms": matched_terms[:8],
                    "token_overlap_ratio": round(ratio, 3),
                    "evidence_basis": evidence_basis,
                })

        if candidate_sources:
            status = "candidate_evidence_found_not_verified"
        elif query_result_indexes:
            status = "query_returned_candidates_no_lexical_signal"
        elif targeted_query and not any_query_metadata:
            status = "query_result_linkage_unavailable"
        elif targeted_query:
            status = "no_candidate_evidence_found"
        else:
            status = "query_not_available"

        ledger.append({
            "target": target_text,
            "targeted_query": targeted_query or None,
            "targeted_query_status": (
                "linked_to_returned_sources" if query_result_indexes
                else "no_linked_source_record"
            ),
            "query_result_source_indexes": query_result_indexes[:12],
            "candidate_source_indexes": [
                item["source_index"] for item in candidate_sources
            ],
            "candidate_sources": candidate_sources[:8],
            "status": status,
            "method": "targeted_query_provenance_plus_lexical_source_screen",
            "semantic_verification": False,
            "source_entailment_verified": False,
        })
    return ledger
