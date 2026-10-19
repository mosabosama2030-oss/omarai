"""Per-request connector summary and split research counters for Omarai.

These helpers turn provider diagnostics and source rows into honest, separable
metrics for search_report and the UI. They never invent retrieval success.
"""
from __future__ import annotations

import os
import urllib.parse
from typing import Any

from agents.research import registrable_domain

# Mirror web_agent attempt statuses that confirm a completed connector call.
_SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES = frozenset({"ok", "no_results", "filtered_all"})


def _clean_text(value: Any, limit: int) -> str:
    if not isinstance(value, str):
        return ""
    return " ".join(value.replace("\x00", " ").split())[:limit]


def connector_catalog() -> list[dict[str, Any]]:
    """Static catalog of search connectors known to the agent (code presence)."""
    return [
        {
            "name": "duckduckgo_html",
            "in_code": True,
            "requires_key": False,
            "configured": True,
        },
        {
            "name": "bing_rss",
            "in_code": True,
            "requires_key": False,
            "configured": True,
        },
        {
            "name": "google_news_rss",
            "in_code": True,
            "requires_key": False,
            "configured": True,
        },
        {
            "name": "brave_search_api",
            "in_code": True,
            "requires_key": True,
            "configured": bool(os.getenv("BRAVE_SEARCH_API_KEY", "").strip()),
        },
        {
            "name": "tavily_search_api",
            "in_code": True,
            "requires_key": True,
            "configured": bool(os.getenv("TAVILY_API_KEY", "").strip()),
        },
        {
            "name": "deepseek_search_api",
            "in_code": True,
            "requires_key": True,
            "configured": bool(
                os.getenv("DEEPSEEK_API_KEY", "").strip()
                or os.getenv("OMARAI_DEEPSEEK_API_KEY", "").strip()
            ),
        },
    ]


def summarize_connector_diagnostics(
    diagnostics: list[dict[str, Any]] | None,
) -> list[dict[str, Any]]:
    """Collapse per-query provider diagnostics into one row per connector."""
    catalog = {item["name"]: dict(item) for item in connector_catalog()}
    by_name: dict[str, dict[str, Any]] = {}
    for item in catalog.values():
        by_name[item["name"]] = {
            **item,
            "attempted": False,
            "statuses": [],
            "result_count": 0,
            "rejected_count": 0,
            "useful_result_count": 0,
            "errors": [],
            "queries_attempted": 0,
        }

    for record in diagnostics or []:
        name = str(record.get("provider") or "").strip()
        if not name:
            continue
        if name not in by_name:
            by_name[name] = {
                "name": name,
                "in_code": True,
                "requires_key": False,
                "configured": True,
                "attempted": False,
                "statuses": [],
                "result_count": 0,
                "rejected_count": 0,
                "useful_result_count": 0,
                "errors": [],
                "queries_attempted": 0,
            }
        row = by_name[name]
        status = str(record.get("status") or "")
        if status and status != "not_configured":
            row["attempted"] = True
            row["queries_attempted"] = int(row["queries_attempted"]) + 1
        if status:
            row["statuses"].append(status)
        result_count = int(record.get("result_count") or 0)
        rejected = int(record.get("rejected_count") or 0)
        row["result_count"] = int(row["result_count"]) + result_count
        row["rejected_count"] = int(row["rejected_count"]) + rejected
        if status == "ok" and result_count > 0:
            row["useful_result_count"] = int(row["useful_result_count"]) + result_count
        error = record.get("error")
        if error:
            cleaned = _clean_text(str(error), 160)
            if cleaned and cleaned not in row["errors"]:
                row["errors"].append(cleaned)

    summary: list[dict[str, Any]] = []
    for name, row in sorted(by_name.items(), key=lambda item: item[0]):
        statuses = list(row["statuses"])
        if not statuses and not row["attempted"]:
            rollup = (
                "not_configured"
                if (row.get("requires_key") and not row.get("configured"))
                else "not_attempted"
            )
        elif "ok" in statuses and int(row["result_count"]) > 0:
            rollup = "returned_results"
        elif "ok" in statuses or "no_results" in statuses or "filtered_all" in statuses:
            rollup = "empty_or_filtered"
        elif "not_configured" in statuses and not row["attempted"]:
            rollup = "not_configured"
        elif any(status in {"failed", "timeout", "budget_exhausted"} for status in statuses):
            rollup = "failed"
        elif row["attempted"]:
            rollup = "attempted"
        else:
            rollup = "not_attempted"
        summary.append({
            "name": name,
            "in_code": bool(row.get("in_code", True)),
            "requires_key": bool(row.get("requires_key", False)),
            "configured": bool(row.get("configured", True)),
            "attempted": bool(row["attempted"]),
            "status": rollup,
            "queries_attempted": int(row["queries_attempted"]),
            "result_count": int(row["result_count"]),
            "rejected_count": int(row["rejected_count"]),
            "useful_result_count": int(row["useful_result_count"]),
            "errors": list(row["errors"])[:5],
        })
    return summary


def enrich_search_report_counters(
    report: dict[str, Any],
    sources: list[dict[str, Any]] | None,
    diagnostics: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Attach split counters and connector summary without inventing success."""
    sources = sources or []
    diagnostics = (
        diagnostics
        if diagnostics is not None
        else list(report.get("provider_diagnostics") or [])
    )
    raw_hits = 0
    for record in diagnostics:
        status = str(record.get("status") or "")
        if status in _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES or status == "ok":
            raw_hits += int(record.get("result_count") or 0)

    unique_urls = len(sources)
    domains = {
        registrable_domain(
            source.get("domain")
            or urllib.parse.urlparse(str(source.get("url") or "")).hostname
            or ""
        )
        for source in sources
    }
    domains.discard("")
    pages_attempted = sum(
        1
        for source in sources
        if source.get("page_fetch_attempted") or source.get("page_fetched")
    )
    extracted_via_status = sum(
        1
        for source in sources
        if source.get("content_extraction_status") in {"extracted", "partial"}
    )
    pages_extracted = extracted_via_status or sum(
        1
        for source in sources
        if source.get("page_fetched")
        and str(source.get("page_text") or source.get("snippet") or "").strip()
    )
    pages_failed = sum(
        1
        for source in sources
        if source.get("page_fetch_attempted") and not source.get("page_fetched")
    )

    report["raw_search_hits"] = int(raw_hits)
    report["unique_urls"] = unique_urls
    report["unique_sources"] = unique_urls
    report["unique_domains"] = len(domains)
    report["pages_fetch_attempted"] = pages_attempted
    report["pages_content_extracted"] = pages_extracted
    report["pages_extraction_failed"] = pages_failed
    report["pages_fetched"] = pages_extracted
    report["connector_summary"] = summarize_connector_diagnostics(diagnostics)
    report["counter_semantics"] = {
        "raw_search_hits": "sum_of_connector_result_counts_before_dedup",
        "unique_urls": "deduplicated_sources_after_merge",
        "unique_domains": "distinct_registrable_domains_not_editorial_independence",
        "pages_fetch_attempted": "sources_selected_for_page_fetch",
        "pages_content_extracted": "pages_with_usable_extracted_text",
        "pages_fetched": "legacy_alias_for_pages_content_extracted",
    }
    return report
