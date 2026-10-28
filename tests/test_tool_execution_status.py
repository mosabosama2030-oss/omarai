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
    assert statuses["public_social_search_if_configured"] == "unknown"
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
        {"tool_requirements": ["web_search", "page_fetch"]},
        {},
        {},
    ))
    assert unknown["web_search"] == "unknown"
    assert unknown["page_fetch"] == "unknown"


def test_tool_matrix_surfaces_mismatch_between_report_counters_and_final_sources():
    rows = build_tool_execution_matrix(
        {"tool_requirements": ["web_search", "page_fetch"]},
        {
            "search_attempted": True,
            "sources": [
                {"url": "https://example.org/read", "page_fetched": True, "page_text": "text"}
            ],
        },
        {
            "search_attempted": True,
            "search_outcome": "attempted_no_usable_sources",
            "usable_sources_after_filtering": 0,
            "pages_fetch_attempted": 1,
            "pages_fetched": 0,
        },
    )
    by_tool = {row["tool"]: row for row in rows}

    assert by_tool["web_search"]["status"] == "counter_mismatch"
    assert by_tool["web_search"]["basis"]["counter_consistency"] == "mismatch"
    assert by_tool["web_search"]["basis"]["reported_accepted_source_count"] == 0
    assert by_tool["web_search"]["basis"]["accepted_source_count"] == 1
    assert by_tool["page_fetch"]["status"] == "counter_mismatch"
    assert by_tool["page_fetch"]["basis"]["counter_consistency"] == "mismatch"
    assert by_tool["page_fetch"]["basis"]["pages_read_from_returned_sources"] == 1
    assert by_tool["page_fetch"]["basis"]["reported_pages_fetched"] == 0


def test_social_search_is_only_called_completed_when_connector_attempt_is_observed():
    rows = build_tool_execution_matrix(
        {"tool_requirements": ["public_social_search_if_configured"]},
        {"search_attempted": True, "sources": []},
        {
            "search_outcome": "attempted_no_usable_sources",
            "social_direct_results": 0,
            "connector_summary": {
                "connectors": [
                    {
                        "name": "reddit_public_rss",
                        "configured": True,
                        "attempted": True,
                        "status": "no_results",
                    }
                ]
            },
        },
    )
    social = next(row for row in rows if row["tool"] == "public_social_search_if_configured")
    assert social["status"] == "completed_no_usable_results"
