"""Truthful task-tool execution status, separate from task planning and evidence quality."""
from __future__ import annotations

from typing import Any

_TOOL_LABELS = {
    "web_search": "البحث على الويب",
    "page_fetch": "فتح الصفحات وقراءة النص",
    "public_social_search_if_configured": "البحث في المحتوى الاجتماعي العام",
    "language_model_generation_if_configured": "توليد الإجابة بالنموذج",
    "claim_review_if_configured": "مراجعة الإجابة بمساعدة النموذج",
}
_ERROR_OUTCOMES = {
    "attempted_research_error",
    "unknown_after_research_error",
    "unknown_after_budget_exhaustion",
}
_SOCIAL_PLATFORMS = {
    "reddit", "youtube", "facebook", "instagram", "x", "twitter",
    "tiktok", "linkedin", "threads", "bluesky",
}


def _nonnegative_int(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return max(0, value)
    if isinstance(value, float) and value.is_integer():
        return max(0, int(value))
    return None


def _status_row(
    tool: str,
    required: bool,
    status: str,
    basis: dict[str, Any],
) -> dict[str, Any]:
    return {
        "tool": tool,
        "label_ar": _TOOL_LABELS[tool],
        "required_by_task_spec": required,
        "status": status,
        "basis": basis,
        "semantics": (
            "حالة مسار التنفيذ المرصودة فقط؛ لا تثبت صحة المحتوى أو كفاية الدليل."
        ),
    }


def build_tool_execution_matrix(
    task_spec: dict[str, Any] | None,
    result: dict[str, Any] | None,
    report: dict[str, Any] | None,
) -> list[dict[str, Any]]:
    """Map planned tool requirements to observed outcomes without inferring success."""
    spec = task_spec if isinstance(task_spec, dict) else {}
    output = result if isinstance(result, dict) else {}
    search_report = report if isinstance(report, dict) else {}
    requirements = spec.get("tool_requirements")
    required = {
        item for item in requirements
        if isinstance(item, str) and item in _TOOL_LABELS
    } if isinstance(requirements, list) else set()

    outcome = str(search_report.get("search_outcome") or "unknown")
    attempted = output.get("search_attempted", search_report.get("search_attempted"))
    reported_accepted_sources = _nonnegative_int(
        search_report.get("usable_sources_after_filtering")
    )
    reported_pages_read = _nonnegative_int(search_report.get("pages_fetched"))
    pages_attempted = _nonnegative_int(search_report.get("pages_fetch_attempted"))
    raw_source_rows = output.get("sources")
    returned_sources_known = isinstance(raw_source_rows, list)
    source_rows = raw_source_rows if returned_sources_known else []
    readable_page_rows = sum(
        1 for source in source_rows
        if isinstance(source, dict)
        and source.get("page_fetched") is True
    )
    # The public return value is the final accepted source set. Prefer it when
    # present; preserve report counters separately so disagreements stay visible.
    returned_source_count = len(source_rows) if returned_sources_known else None
    accepted_sources = (
        returned_source_count if returned_sources_known else reported_accepted_sources
    )
    pages_read = reported_pages_read if reported_pages_read is not None else readable_page_rows
    source_count_mismatch = (
        returned_sources_known
        and reported_accepted_sources is not None
        and reported_accepted_sources != returned_source_count
    )
    page_count_mismatch = (
        returned_sources_known
        and reported_pages_read is not None
        and reported_pages_read != readable_page_rows
    )

    rows: list[dict[str, Any]] = []

    # Search completion and evidence acceptance are distinct: zero accepted sources
    # means this retrieval attempt supplied no eligible evidence, not that the fact
    # or source does not exist.
    tool = "web_search"
    if tool not in required:
        status = "not_required"
    elif outcome == "attempted_research_error":
        status = "failed"
    elif outcome in {"unknown_after_research_error", "unknown_after_budget_exhaustion"}:
        status = "unknown"
    elif outcome == "not_attempted" or attempted is False:
        status = "not_attempted"
    elif source_count_mismatch:
        status = "counter_mismatch"
    elif attempted is True:
        if accepted_sources is not None:
            status = "completed_with_results" if accepted_sources > 0 else "completed_no_usable_results"
        elif outcome == "attempted_with_usable_sources":
            status = "completed_with_results"
        elif outcome == "attempted_no_usable_sources":
            status = "completed_no_usable_results"
        else:
            status = "unknown"
    else:
        status = "unknown"
    rows.append(_status_row(tool, tool in required, status, {
        "search_outcome": outcome,
        "search_attempted": attempted if isinstance(attempted, bool) else None,
        "accepted_source_count": accepted_sources,
        "reported_accepted_source_count": reported_accepted_sources,
        "counter_consistency": (
            "mismatch" if source_count_mismatch else "consistent"
            if returned_sources_known and reported_accepted_sources is not None
            else "not_comparable"
        ),
    }))

    tool = "page_fetch"
    if tool not in required:
        status = "not_required"
    elif page_count_mismatch:
        status = "counter_mismatch"
    elif pages_read > 0:
        status = "completed_with_read_pages"
    elif pages_attempted is not None and pages_attempted > 0:
        status = "attempted_no_readable_pages"
    elif pages_attempted is None:
        status = "unknown"
    elif outcome in _ERROR_OUTCOMES:
        status = "not_attempted_after_search_error"
    elif attempted is True:
        status = "not_attempted_no_fetchable_candidates"
    elif attempted is False:
        status = "not_attempted"
    else:
        status = "unknown"
    rows.append(_status_row(tool, tool in required, status, {
        "pages_fetch_attempted": pages_attempted,
        "pages_read": pages_read,
        "reported_pages_fetched": reported_pages_read,
        "pages_read_from_returned_sources": readable_page_rows,
        "counter_consistency": (
            "mismatch" if page_count_mismatch else "consistent"
            if returned_sources_known and reported_pages_read is not None
            else "not_comparable"
        ),
    }))

    tool = "public_social_search_if_configured"
    raw_social_results = _nonnegative_int(search_report.get("social_direct_results"))
    social_results = raw_social_results or 0
    social_sources = sum(
        1 for source in source_rows
        if isinstance(source, dict)
        and (
            str(source.get("platform") or "").lower() in _SOCIAL_PLATFORMS
            or str(source.get("source_class") or "").lower() == "social"
        )
    )
    connector_summary = search_report.get("connector_summary")
    connector_summary = connector_summary if isinstance(connector_summary, dict) else {}
    connector_rows = connector_summary.get("connectors")
    connector_rows = connector_rows if isinstance(connector_rows, list) else []
    social_connector_names = {
        "reddit_public_rss", "bluesky_public_search", "reddit_oauth_api",
        "facebook_pages_api", "instagram_graph_api", "x_official_api",
        "youtube_data_api",
    }
    social_connector_states = [
        row for row in connector_rows
        if isinstance(row, dict) and row.get("name") in social_connector_names
    ]
    attempted_social_connectors = [
        row for row in social_connector_states if row.get("attempted") is True
    ]
    social_connector_errors = [
        row for row in social_connector_states
        if row.get("status") in {
            "failed", "error", "timeout", "http_error", "unauthorized",
            "rate_limited", "budget_exhausted",
        }
    ]
    social_configured_connectors = [
        row for row in social_connector_states
        if row.get("configured") is True
    ]
    social_not_configured_connectors = [
        row for row in social_connector_states
        if row.get("configured") is False
    ]
    if tool not in required:
        status = "not_required"
    elif social_results > 0 or social_sources > 0:
        status = "completed_with_results"
    elif outcome in _ERROR_OUTCOMES and outcome == "attempted_research_error":
        status = "failed"
    elif outcome in _ERROR_OUTCOMES:
        status = "unknown"
    elif attempted_social_connectors:
        status = "failed" if social_connector_errors else "completed_no_usable_results"
    elif social_configured_connectors and all(
        row.get("attempted") is False for row in social_configured_connectors
    ):
        status = "not_attempted"
    elif social_not_configured_connectors and (
        not social_configured_connectors or not attempted_social_connectors
    ):
        status = "not_configured"
    elif raw_social_results is None and not social_connector_states:
        status = "unknown"
    elif attempted is False:
        status = "not_attempted"
    else:
        # A general web search attempt is not proof that social connectors ran.
        status = "unknown"
    rows.append(_status_row(tool, tool in required, status, {
        "social_direct_results": social_results,
        "social_result_count_known": raw_social_results is not None,
        "accepted_social_sources": social_sources,
        "social_connectors_observed": [
            {
                "name": row.get("name"),
                "configured": row.get("configured"),
                "attempted": row.get("attempted"),
                "status": row.get("status"),
            }
            for row in social_connector_states[:8]
        ],
        "search_outcome": outcome,
        "interpretation": (
            "A general web search attempt does not prove that a social connector was attempted."
        ),
    }))

    tool = "language_model_generation_if_configured"
    final_status = str(output.get("final_answer_status") or "")
    used_model = output.get("used_language_model") is True
    if tool not in required:
        status = "not_required"
    elif used_model:
        status = "completed"
    elif final_status in {
        "model_not_configured_fallback", "model_not_configured",
    }:
        status = "not_configured"
    elif final_status in {
        "generation_failed", "generation_failed_with_source_fallback",
        "budget_exhausted", "budget_exhausted_with_source_fallback",
    }:
        status = "failed"
    elif final_status in {
        "clarification_required", "insufficient_evidence_no_generation",
        "not_attempted", "local_response_no_generation",
    }:
        status = "not_attempted"
    elif output.get("kind") == "insufficient_evidence":
        status = "not_attempted_no_evidence"
    else:
        status = "unknown"
    rows.append(_status_row(tool, tool in required, status, {
        "used_language_model": used_model,
        "final_answer_status": final_status or "unknown",
    }))

    tool = "claim_review_if_configured"
    review_status = str(
        search_report.get("claim_audit")
        or search_report.get("second_pass_review")
        or "unknown"
    )
    if tool not in required:
        status = "not_required"
    elif review_status == "model_claim_audit_completed":
        status = "completed_model_assisted_review"
    elif review_status in {
        "model_claim_audit_unavailable", "review_failed_with_source_fallback",
    }:
        status = "failed"
    elif review_status in {"not_run", "not_assessed", "not_verified"}:
        status = (
            "not_attempted_no_evidence"
            if not source_rows else "not_attempted"
        )
    else:
        status = "unknown"
    rows.append(_status_row(tool, tool in required, status, {
        "review_status": review_status,
        "independent_fact_check": False,
    }))
    return rows
