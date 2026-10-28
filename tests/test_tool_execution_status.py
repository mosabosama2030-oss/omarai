from __future__ import annotations

from agents.tool_execution_status import build_tool_execution_matrix


TOOLS = {
    "web_search",
    "page_fetch",
    "public_social_search_if_configured",
    "language_model_generation_if_configured",
    "claim_review_if_configured",
}


def _statuses(rows):
    return {row["tool"]: row["status"] for row in rows}


def test_tool_matrix_distinguishes_no_usable_results_from_page_read_failure():
    spec = {"tool_requirements": sorted(TOOLS)}
    result = {
        "search_attempted": True,
        "used_language_model": False,
        "final_answer_status": "model_not_configured_fallback",
        "sources": [],
    }
    report = {
        "search_outcome": "attempted_no_usable_sources",
        "usable_sources_after_filtering": 0,
        "pages_fetch_attempted": 3,
        "pages_fetched": 0,
        "social_direct_results": 0,
        "claim_audit": "not_run",
    }

    rows = build_tool_execution_matrix(spec, result, report)
    statuses = _statuses(rows)

    assert set(statuses) == TOOLS
    assert statuses["web_search"] == "completed_no_usable_results"
    assert statuses["page_fetch"] == "attempted_no_readable_pages"
    assert statuses["public_social_search_if_configured"] == "completed_no_usable_results"
    assert statuses["language_model_generation_if_configured"] == "not_configured"
    assert statuses["claim_review_if_configured"] == "not_attempted_no_evidence"
    assert all("لا تثبت صحة المحتوى" in row["semantics"] for row in rows)


def test_tool_matrix_reports_observed_success_without_claiming_fact_verification():
    spec = {"tool_requirements": sorted(TOOLS)}
    result = {
        "search_attempted": True,
        "used_language_model": True,
        "final_answer_status": "model_answer_generated",
        "sources": [
            {
                "url": "https://www.reddit.com/r/example/comments/1",
                "platform": "reddit",
                "source_class": "social",
                "page_fetched": True,
            }
        ],
    }
    report = {
        "search_outcome": "attempted_with_usable_sources",
        "usable_sources_after_filtering": 1,
        "pages_fetch_attempted": 1,
        "pages_fetched": 1,
        "social_direct_results": 2,
        "claim_audit": "model_claim_audit_completed",
    }

    statuses = _statuses(build_tool_execution_matrix(spec, result, report))

    assert statuses["web_search"] == "completed_with_results"
    assert statuses["page_fetch"] == "completed_with_read_pages"
    assert statuses["public_social_search_if_configured"] == "completed_with_results"
    assert statuses["language_model_generation_if_configured"] == "completed"
    assert statuses["claim_review_if_configured"] == "completed_model_assisted_review"


def test_tool_matrix_marks_unrequired_tools_not_required_and_unknowns_unknown():
    rows = build_tool_execution_matrix(
        {"tool_requirements": []},
        {"sources": []},
        {},
    )

    assert all(row["required_by_task_spec"] is False for row in rows)
    assert all(row["status"] == "not_required" for row in rows)

    unknown = _statuses(build_tool_execution_matrix(
        {"tool_requirements": ["web_search"]},
        {},
        {},
    ))
    assert unknown["web_search"] == "unknown"
