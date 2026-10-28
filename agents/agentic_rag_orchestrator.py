"""Agentic RAG orchestrator (ReAct-style) for Omarai.

Loop: Plan (reformulate) → Act (retrieve tool) → Observe → Decide → Verify → Compose.

The orchestrator does not replace WebAgent network/SSRF policy. It accepts an
injected retrieve_fn that already enforces those controls.
"""
from __future__ import annotations

from typing import Any, Callable

from agents.memory_bank import MemoryBank
from agents.specialist_agents import (
    FinalComposer,
    HallucinationGuard,
    IterativeRetriever,
    QueryReformulator,
)

RetrieveFn = Callable[[str], list[dict[str, Any]]]
DraftFn = Callable[[str, list[dict[str, Any]], dict[str, Any]], str]


def _default_draft(question: str, sources: list[dict[str, Any]], meta: dict[str, Any]) -> str:
    aspects = meta.get("aspects") or []
    lines = [f"ملخص مستند إلى المصادر المتاحة حول: {question.strip()[:200]}"]
    if aspects:
        lines.append("المحاور المطلوبة: " + "، ".join(map(str, aspects[:8])) + ".")
    for src in sources[:8]:
        title = str(src.get("title") or "").strip()
        snip = str(src.get("snippet") or "").strip()[:220]
        if title or snip:
            lines.append(f"{title}: {snip}")
    if len(sources) < 2:
        lines.append("عدد المصادر محدود وقد تكون التغطية جزئية.")
    return "\n".join(lines)


class AgenticRagOrchestrator:
    """Reasoning engine that treats retrieval as a tool inside a ReAct loop."""

    def __init__(
        self,
        retrieve_fn: RetrieveFn,
        *,
        draft_fn: DraftFn | None = None,
        max_hops: int = 3,
        min_support: float = 0.25,
    ) -> None:
        self.reformulator = QueryReformulator()
        self.retriever = IterativeRetriever(retrieve_fn, max_hops=max_hops)
        self.guard = HallucinationGuard(min_support=min_support)
        self.composer = FinalComposer()
        self.draft_fn = draft_fn or _default_draft
        self.max_hops = max_hops

    def run(
        self,
        question: str,
        *,
        history: list[dict[str, str]] | None = None,
        topic_hint: str = "",
        session_id: str = "",
    ) -> dict[str, Any]:
        trace_steps: list[dict[str, Any]] = []

        plan = self.reformulator.reformulate(question, topic_hint=topic_hint)
        trace_steps.append({"phase": "plan", "agent": "QueryReformulator", "plan": {
            "aspects": plan.get("aspects"),
            "queries": plan.get("queries"),
            "needs_retrieval": plan.get("needs_retrieval"),
        }})

        aspect0 = (plan.get("aspects") or [""])[0] if plan.get("aspects") else ""
        retrieval = self.retriever.retrieve(list(plan.get("queries") or []), aspect=str(aspect0))
        trace_steps.append({
            "phase": "act_observe",
            "agent": "IterativeRetriever",
            "hop_count": retrieval.get("hop_count"),
            "sufficiency": retrieval.get("final_sufficiency"),
            "result_count": len(retrieval.get("results") or []),
        })

        sufficiency = str(retrieval.get("final_sufficiency") or "none")
        decide = {
            "proceed_to_answer": sufficiency in {"adequate", "rich", "thin"},
            "reason": (
                "adequate_evidence"
                if sufficiency in {"adequate", "rich"}
                else "thin_or_empty_evidence"
            ),
        }
        trace_steps.append({"phase": "decide", "decision": decide})

        bank = MemoryBank(session_id=session_id or "session")
        bank.ingest_sources(retrieval.get("results") or [])
        bank.notes.append(f"retrieval_hops={retrieval.get('hop_count')}")
        bank.notes.append(f"sufficiency={sufficiency}")

        meta = {
            "aspects": plan.get("aspects") or [],
            "queries": plan.get("queries") or [],
            "retrieval": {
                "hop_count": retrieval.get("hop_count"),
                "final_sufficiency": sufficiency,
            },
            "history_turns": len(history or []),
        }

        draft = self.draft_fn(question, retrieval.get("results") or [], meta)
        trace_steps.append({"phase": "draft", "draft_chars": len(draft or "")})

        guard_report = self.guard.verify_answer(
            draft, bank, aspects=list(plan.get("aspects") or [])
        )
        trace_steps.append({
            "phase": "verify",
            "agent": "HallucinationGuard",
            "unsupported_count": guard_report.get("unsupported_count"),
            "should_abstain": guard_report.get("should_abstain"),
        })

        composed = self.composer.compose(draft, bank, guard_report, language="ar")
        trace_steps.append({
            "phase": "compose",
            "agent": "FinalComposer",
            "abstained": composed.get("abstained"),
            "citation_count": len(composed.get("citations") or []),
        })

        return {
            "question": question,
            "plan": plan,
            "retrieval": {
                "hop_count": retrieval.get("hop_count"),
                "final_sufficiency": retrieval.get("final_sufficiency"),
                "hops": retrieval.get("hops"),
                "result_count": len(retrieval.get("results") or []),
                "results": retrieval.get("results") or [],
            },
            "answer": composed.get("answer"),
            "abstained": composed.get("abstained"),
            "citations": composed.get("citations"),
            "guard": guard_report,
            "memory_stats": (composed.get("memory") or {}).get("stats"),
            "memory": composed.get("memory"),
            "trace": {
                "method": "agentic_rag_react",
                "steps": trace_steps,
                "pipeline": [
                    "reformulate",
                    "retrieve_until_sufficient",
                    "decide",
                    "ingest_memory_bank",
                    "draft",
                    "verify_claims",
                    "compose_with_citations",
                ],
            },
        }
