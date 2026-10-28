"""Truthful research completion diagnostics, separate from factual correctness."""
from __future__ import annotations

from typing import Any
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from agents.research import registrable_domain

_RESEARCH_KINDS = frozenset({
    "web_research", "web_fallback", "insufficient_evidence",
    "lead_discovery_no_qualified_candidates",
})
_RESEARCH_ERRORS = frozenset({
    "attempted_research_error", "unknown_after_research_error",
    "unknown_after_budget_exhaustion",
})
_CONNECTOR_OK = frozenset({"ok", "no_results", "filtered_all", "passed"})
_CONNECTOR_ERRORS = frozenset({
    "failed", "timeout", "error", "not_configured", "disabled",
    "rate_limited", "blocked",
})
_TRACKING_KEYS = frozenset({"fbclid", "gclid", "mc_cid", "mc_eid", "ref", "source"})


def _dict(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _int(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    try:
        return max(0, int(value))
    except (TypeError, ValueError, OverflowError):
        return None


def _readable(source: dict[str, Any]) -> bool:
    return bool(source.get("page_fetched")) and bool(
        str(source.get("page_text") or "").strip()
    )


def _url_key(value: Any) -> str:
    try:
        parts = urlsplit(str(value or "").strip())
        scheme = parts.scheme.lower()
        if scheme not in {"http", "https"} or not parts.hostname:
            return ""
        host = parts.hostname.lower().rstrip(".")
        port = parts.port
        netloc = host if port is None or (scheme, port) in {
            ("http", 80), ("https", 443)
        } else f"{host}:{port}"
        query = [
            (key, val) for key, val in parse_qsl(parts.query, keep_blank_values=True)
            if key.casefold() not in _TRACKING_KEYS
            and not key.casefold().startswith("utm_")
        ]
        path = parts.path.rstrip("/") or "/"
        return urlunsplit((scheme, netloc, path, urlencode(sorted(query)), ""))
    except (TypeError, ValueError):
        return ""


def build_research_completion(result: dict[str, Any]) -> dict[str, Any]:
    """Compute phase states and final counters without claiming semantic verification."""
    result = _dict(result)
    report = _dict(result.get("search_report"))
    raw_sources = _list(result.get("sources"))
    sources = [item for item in raw_sources if isinstance(item, dict)]
    kind = str(result.get("kind") or "")
    if kind not in _RESEARCH_KINDS and not report:
        return {
            "status": "not_applicable" if kind in {
                "capability_answer", "local_conversation", "clarification"
            } else "not_run",
            "semantic_verification": "not_performed",
        }

    budget = _dict(result.get("request_budget") or report.get("request_budget"))
    exhausted = bool(budget.get("budget_exhausted")) or bool(
        budget.get("deadline_exceeded")
    )
    guardrails = _dict(report.get("source_guardrails"))
    final_guards = _dict(guardrails.get("final") or guardrails.get("initial"))
    rejection_counts = _dict(final_guards.get("rejection_counts"))
    rejected = sum(
        count for count in (_int(value) for value in rejection_counts.values())
        if count is not None
    )
    attempted_value = result.get("search_attempted")
    if attempted_value is None:
        attempted_value = report.get("search_attempted")
    attempted = attempted_value if isinstance(attempted_value, bool) else None

    fetched = sum(bool(source.get("page_fetched")) for source in sources)
    read = sum(_readable(source) for source in sources)
    snippet_only = sum(
        bool(str(source.get("snippet") or "").strip()) and not _readable(source)
        for source in sources
    )
    unflagged_text = sum(
        bool(str(source.get("page_text") or "").strip())
        and not bool(source.get("page_fetched"))
        for source in sources
    )
    url_keys = [_url_key(source.get("url")) for source in sources]
    url_keys = [key for key in url_keys if key]
    unique_urls = set(url_keys)
    domains = set()
    for source in sources:
        key = _url_key(source.get("url"))
        if not key:
            continue
        host = source.get("domain") or urlsplit(key).hostname or ""
        domains.add(registrable_domain(str(host)))
    domains.discard("")

    query_rows = _list(report.get("query_results"))
    query_total = None
    if query_rows and all(
        isinstance(row, dict) and _int(row.get("results")) is not None
        for row in query_rows
    ):
        query_total = sum(_int(row.get("results")) or 0 for row in query_rows)
    zero_results = bool(query_rows) and all(
        isinstance(row, dict) and _int(row.get("results")) == 0
        for row in query_rows
    )

    connector_counts: dict[str, int] = {}
    for item in _list(report.get("provider_diagnostics")):
        if not isinstance(item, dict):
            continue
        status_value = str(item.get("status") or "unknown").strip().lower()
        connector_counts[status_value] = connector_counts.get(status_value, 0) + 1
    connector_ok = sum(
        count for status_value, count in connector_counts.items()
        if status_value in _CONNECTOR_OK
    )
    connector_errors = sum(
        count for status_value, count in connector_counts.items()
        if status_value in _CONNECTOR_ERRORS
    )

    reported_sources = _int(report.get("unique_sources"))
    reported_fetched = _int(report.get("pages_fetched"))
    counter_issues = []
    if reported_sources is not None and reported_sources != len(sources):
        counter_issues.append("reported_unique_sources_differs_from_final_source_list")
    if reported_fetched is not None and reported_fetched != fetched:
        counter_issues.append("reported_pages_fetched_differs_from_final_source_list")

    model_used = result.get("used_language_model") is True
    final_status = str(result.get("final_answer_status") or "")
    integrity = _dict(result.get("answer_integrity"))
    gap_count = sum(
        _int(integrity.get(key)) or 0
        for key in ("potentially_missing_target_count", "source_evidence_gap_count")
    )
    fulfillment = str(
        result.get("task_fulfillment_status") or report.get("task_fulfillment_status") or ""
    )
    citations = _dict(result.get("citation_validation") or result.get("citation_check"))
    citation_count = _int(citations.get("valid_citation_count")) or 0
    generation_failed = any(
        token in final_status for token in ("failed", "unavailable", "budget_exhausted")
    )

    if exhausted:
        status = "execution_stopped_budget"
    elif not sources:
        if rejected:
            status = "no_eligible_sources_after_filtering"
        elif str(report.get("search_outcome") or "") in _RESEARCH_ERRORS or (
            connector_errors and not connector_ok
        ):
            status = "search_failed_or_incomplete"
        elif zero_results:
            status = "no_results_returned"
        elif attempted is False:
            status = "search_not_attempted"
        else:
            status = "insufficient_evidence"
    elif not model_used:
        status = (
            "source_snippets_only_generation_not_completed"
            if read == 0 else "evidence_collected_generation_not_completed"
        )
    elif generation_failed:
        status = "answer_generation_or_review_failed"
    elif gap_count or fulfillment in {
        "possible_gap_detected", "source_evidence_gap_unresolved",
        "not_assessed_insufficient_evidence",
    }:
        status = "partial_answer_evidence_gaps_detected"
    elif citation_count:
        status = "answer_generated_citations_range_checked_semantic_support_unverified"
    else:
        status = "answer_generated_without_valid_citation_markers"

    if attempted is False:
        search_phase = "not_attempted"
    elif attempted is None:
        search_phase = "unknown"
    elif connector_errors and not connector_ok and not sources:
        search_phase = "failed_or_incomplete"
    elif sources:
        search_phase = "results_received"
    elif zero_results:
        search_phase = "completed_no_results"
    else:
        search_phase = "attempted_no_usable_sources"

    if not sources:
        read_phase = "not_applicable_no_eligible_sources"
    elif read == len(sources):
        read_phase = "all_final_sources_read"
    elif read:
        read_phase = "some_final_sources_read"
    else:
        read_phase = "no_final_source_page_read"

    if kind == "insufficient_evidence" or not sources:
        generation_phase = "not_attempted_or_withheld"
    elif model_used and not generation_failed:
        generation_phase = "answer_generated"
    elif model_used:
        generation_phase = "failed_or_unavailable"
    else:
        generation_phase = "not_completed"

    return {
        "status": status,
        "status_semantics": "pipeline_state_not_probability_of_factual_correctness",
        "phases": {
            "planning": "completed" if isinstance(result.get("research_plan"), dict) else "unknown",
            "search": search_phase,
            "source_filtering": (
                "sources_retained" if sources else
                "rejected_all_candidates" if rejected else "no_eligible_sources"
            ),
            "page_reading": read_phase,
            "answer_generation": generation_phase,
            "citation_validation": str(citations.get("status") or "not_run"),
            "semantic_verification": "not_performed",
        },
        "counters": {
            "queries_planned": _int(report.get("queries_planned")),
            "queries_attempted": _int(report.get("queries_attempted")),
            "search_result_count_observed": query_total,
            "query_result_rows_with_counts": len(query_rows) if query_rows else 0,
            "final_source_list_count": len(sources),
            "unique_normalized_url_count": len(unique_urls),
            "duplicate_normalized_url_count": max(0, len(url_keys) - len(unique_urls)),
            "distinct_registrable_domain_count": len(domains),
            "pages_fetched_flag_count": fetched,
            "pages_read_with_text_count": read,
            "snippet_only_source_count": snippet_only,
            "page_text_without_fetched_flag_count": unflagged_text,
            "connector_status_counts": connector_counts,
            "connector_failure_count": connector_errors,
            "connector_success_count": connector_ok,
            "guardrail_rejected_candidate_count": rejected,
        },
        "counter_consistency": {
            "status": "mismatch_detected" if counter_issues else (
                "matched" if reported_sources is not None or reported_fetched is not None
                else "not_computable"
            ),
            "reported_unique_sources": reported_sources,
            "recomputed_final_source_count": len(sources),
            "reported_pages_fetched": reported_fetched,
            "recomputed_pages_fetched_flag_count": fetched,
            "issues": counter_issues,
        },
        "semantic_verification": "not_performed",
        "warning": (
            "Readable pages and valid citation indexes do not prove semantic support "
            "for each claim in the answer."
        ),
    }
