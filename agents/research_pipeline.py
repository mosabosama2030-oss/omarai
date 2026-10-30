"""One bounded orchestration path for Omarai's hybrid research pipeline.

The coordinator composes existing deterministic interpreters and the existing
language-model planner output. Lexical evidence matching remains a candidate
signal; semantic matching is explicitly unassessed unless a scorer is injected.
"""
from __future__ import annotations

from collections.abc import Callable
from typing import Any

from agents.aspect_planning import build_evidence_ledger, extract_aspects
from agents.intent_router import ROUTES, resolve_followup_query, route_intent
from agents.task_understanding import (
    MAX_TASK_ASPECTS,
    build_query_strategy_matrix,
    build_task_spec,
)

MAX_PIPELINE_QUESTION_CHARS = 4000
MAX_PIPELINE_SOURCES = 18


def _clean_aspects(task_spec: dict[str, Any], question: str) -> list[str]:
    constraints = task_spec.get("constraints")
    declared = constraints.get("explicit_aspects", []) if isinstance(constraints, dict) else []
    extracted = extract_aspects(question)
    aspects: list[str] = []
    seen: set[str] = set()
    for value in [*(declared if isinstance(declared, list) else []), *extracted]:
        if not isinstance(value, str):
            continue
        item = " ".join(value.split())[:120]
        key = item.casefold()
        if item and key not in seen:
            seen.add(key)
            aspects.append(item)
        if len(aspects) >= MAX_TASK_ASPECTS:
            break
    return aspects


def evaluate_research_evidence(
    aspects: list[str],
    sources: list[dict[str, Any]] | None,
    *,
    semantic_matcher: Callable[[str, dict[str, Any]], Any] | None = None,
) -> dict[str, Any]:
    """Evaluate per-aspect candidates without equating relevance with claim truth."""
    safe_aspects = [
        item[:120] for item in aspects[:MAX_TASK_ASPECTS]
        if isinstance(item, str) and item.strip()
    ]
    safe_sources = [
        item for item in (sources or [])[:MAX_PIPELINE_SOURCES]
        if isinstance(item, dict)
    ]
    lexical_ledger = build_evidence_ledger(safe_aspects, safe_sources)
    semantic_status = "not_configured"
    semantic_candidates: dict[str, list[dict[str, Any]]] = {}

    if callable(semantic_matcher) and safe_aspects and safe_sources:
        semantic_status = "evaluated"
        for aspect in safe_aspects:
            ranked: list[dict[str, Any]] = []
            for source_index, source in enumerate(safe_sources):
                try:
                    raw_score = semantic_matcher(aspect, source)
                    score = float(raw_score)
                except (ArithmeticError, TypeError, ValueError):
                    continue
                if not 0.0 <= score <= 1.0:
                    continue
                ranked.append({
                    "source_index": source_index,
                    "score": round(score, 4),
                })
            semantic_candidates[aspect] = sorted(
                ranked, key=lambda item: item["score"], reverse=True
            )[:5]

    return {
        "lexical_ledger": lexical_ledger,
        "semantic_matching": {
            "status": semantic_status,
            "candidates": semantic_candidates,
            "meaning": (
                "ترتيب مرشحات الصلة فقط؛ لا يثبت صحة الادعاءات أو كفاية الاستشهاد."
            ),
        },
        "claim_verification": "delegated_to_existing_validator",
    }


def build_research_pipeline(
    question: str,
    plan: dict[str, Any] | None = None,
    *,
    history: list[dict[str, str]] | None = None,
    mode: str = "auto",
    intent_route: str = "",
    dialogue_context: dict[str, Any] | None = None,
    sources: list[dict[str, Any]] | None = None,
    compact_fn: Callable[[str], str] | None = None,
    semantic_matcher: Callable[[str, dict[str, Any]], Any] | None = None,
) -> dict[str, Any]:
    """Run context→intent→task→aspects→queries→evidence as one auditable pipeline."""
    raw_question = question[:MAX_PIPELINE_QUESTION_CHARS] if isinstance(question, str) else ""
    contextual_question = (
        resolve_followup_query(raw_question, history)
        if history and raw_question.strip()
        else raw_question
    )
    supplied_route = intent_route if isinstance(intent_route, str) else ""
    intent = (
        {"route": supplied_route, "reason": "upstream_route", "context_available": bool(history),
         "needs_clarification": supplied_route == "CLARIFY"}
        if supplied_route in ROUTES
        else route_intent(contextual_question, history, mode=mode)
    )
    route = intent.get("route", "CLARIFY")
    safe_plan = dict(plan) if isinstance(plan, dict) else {}
    task_spec = build_task_spec(
        contextual_question,
        mode=mode,
        intent_route=route,
        plan=safe_plan,
        dialogue_context=dialogue_context if isinstance(dialogue_context, dict) else None,
    )
    aspects = _clean_aspects(task_spec, contextual_question)

    if route == "CLARIFY" or intent.get("needs_clarification"):
        strategy_matrix: list[dict[str, str]] = []
        queries: list[str] = []
        query_status = "blocked_pending_clarification"
    else:
        strategy_matrix = build_query_strategy_matrix(
            contextual_question,
            task_spec,
            safe_plan.get("queries", []),
            limit=8,
            compact_fn=compact_fn,
        )
        queries = [item["query"] for item in strategy_matrix]
        query_status = "completed"

    evidence = evaluate_research_evidence(
        aspects, sources, semantic_matcher=semantic_matcher
    )
    return {
        "contextual_question": contextual_question,
        "intent": intent,
        "task_spec": task_spec,
        "aspects": aspects,
        "query_strategy_matrix": strategy_matrix,
        "queries": queries,
        "evidence": evidence,
        "evidence_ledger": evidence["lexical_ledger"],
        "stages": {
            "context_resolution": "completed" if history else "not_needed",
            "intent_routing": "completed",
            "task_understanding": "completed",
            "aspect_extraction": "completed",
            "query_planning": query_status,
            "lexical_matching": "completed" if aspects and sources else "not_assessed",
            "semantic_matching": evidence["semantic_matching"]["status"],
            "claim_verification": evidence["claim_verification"],
        },
    }
