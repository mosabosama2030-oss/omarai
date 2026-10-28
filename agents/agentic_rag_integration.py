"""Wire Agentic RAG + MemoryBank into Omarai WebAgent safely.

Does not bypass SSRF/URL/relevance policy. retrieve_fn must already enforce them.
"""
from __future__ import annotations

from typing import Any, Callable

from agents.agentic_rag_orchestrator import AgenticRagOrchestrator
from agents.eval_rag_metrics import evaluate_rag_case
from agents.memory_bank import (
    MemoryBank,
    build_memory_from_sources_and_answer,
)

RetrieveFn = Callable[[str], list[dict[str, Any]]]


def bind_existing_answer_to_sources(
    answer: str,
    sources: list[dict[str, Any]],
    *,
    aspects: list[str] | None = None,
    min_score: float = 0.25,
) -> dict[str, Any]:
    bank = build_memory_from_sources_and_answer(
        sources, answer, aspects=aspects, min_score=min_score
    )
    metrics = evaluate_rag_case(
        question="",
        answer=answer,
        sources=sources,
        aspects=aspects,
    )
    return {
        "memory": bank.to_dict(),
        "ledger": bank.to_claim_evidence_ledger_shape(),
        "claims": [
            {
                "text": c.text,
                "status": c.status,
                "support_score": c.support_score,
                "evidence_ids": c.evidence_ids,
                "aspect": c.aspect,
                "cited": bank.format_claim_with_citations(c),
            }
            for c in bank.claims
        ],
        "supported_answer": bank.render_supported_answer(drop_unsupported=True),
        "metrics": metrics,
        "citation_map": bank.citation_map(),
        "stats": bank.stats(),
    }


def run_agentic_rag(
    question: str,
    retrieve_fn: RetrieveFn,
    *,
    history: list[dict[str, str]] | None = None,
    max_hops: int = 3,
) -> dict[str, Any]:
    orch = AgenticRagOrchestrator(retrieve_fn, max_hops=max_hops)
    result = orch.run(question, history=history)
    sources = list((result.get("retrieval") or {}).get("results") or [])
    result["metrics"] = evaluate_rag_case(
        question=question,
        answer=str(result.get("answer") or ""),
        sources=sources,
        aspects=list((result.get("plan") or {}).get("aspects") or []),
    )
    mem = result.get("memory")
    if isinstance(mem, dict) and mem.get("claims"):
        bank = MemoryBank(session_id=str(mem.get("session_id") or ""))
        bank.ingest_sources(sources)
        bank.bind_answer(str(result.get("answer") or ""))
        result["ledger"] = bank.to_claim_evidence_ledger_shape()
    return result


def run_agentic_rag_over_sources(
    question: str,
    sources: list[dict[str, Any]],
    *,
    retrieve_fn: RetrieveFn | None = None,
    aspects: list[str] | None = None,
    draft_answer: str = "",
) -> dict[str, Any]:
    fixed = list(sources or [])

    def _fixed_retrieve(q: str) -> list[dict[str, Any]]:
        return fixed

    fn = retrieve_fn or _fixed_retrieve
    orch = AgenticRagOrchestrator(fn, max_hops=2)

    def draft_fn(q: str, srcs: list[dict[str, Any]], meta: dict[str, Any]) -> str:
        if draft_answer.strip():
            return draft_answer
        return (
            f"إجابة موجّهة بالأدلة عن: {q}\n"
            + "\n".join(
                f"- {s.get('title')}: {str(s.get('snippet') or '')[:180]}"
                for s in (srcs or fixed)[:8]
            )
        )

    orch.draft_fn = draft_fn
    result = orch.run(question)
    if fixed:
        post = bind_existing_answer_to_sources(
            str(result.get("answer") or draft_answer or ""),
            fixed,
            aspects=aspects,
        )
        result["post_hoc_binding"] = post
        result["metrics"] = post.get("metrics")
        result["ledger"] = post.get("ledger")
    return result


def web_agent_post_answer_hook(
    question: str,
    answer: str,
    sources: list[dict[str, Any]],
    *,
    aspects: list[str] | None = None,
    min_score: float = 0.25,
) -> dict[str, Any]:
    binding = bind_existing_answer_to_sources(
        answer, sources, aspects=aspects, min_score=min_score
    )
    return {
        "agentic_rag": {
            "enabled": True,
            "question": question[:500],
            "claims": binding.get("claims"),
            "metrics": binding.get("metrics"),
            "citation_map": binding.get("citation_map"),
            "memory_stats": binding.get("stats"),
            "ledger": binding.get("ledger"),
            "supported_answer": binding.get("supported_answer"),
            "honesty": (
                "الدعم لفظي عبر MemoryBank؛ لا يُفسَّر كتحقق حقيقة دلالي."
            ),
        }
    }
