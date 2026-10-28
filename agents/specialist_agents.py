"""Specialist agents inside Omarai agentic RAG pipeline.

- QueryReformulator: natural language → effective search queries + aspects
- IterativeRetriever: multi-hop retrieval tool use
- HallucinationGuard: claim vs evidence verification
- FinalComposer: fluent answer with mandatory citations / abstention
"""
from __future__ import annotations

import re
from typing import Any, Callable

from agents.memory_bank import MemoryBank, split_answer_into_claim_sentences
from agents.retrieval_tool import RetrievalTool

RetrieveFn = Callable[[str], list[dict[str, Any]]]

try:
    from agents.aspect_planning import extract_aspects, build_aspect_queries
except Exception:  # pragma: no cover
    def extract_aspects(question: str) -> list[str]:
        return []

    def build_aspect_queries(topic: str, aspects: list[str], *, limit: int = 8) -> list[str]:
        out = [topic] if topic else []
        for a in aspects:
            out.append(f"{topic} {a}".strip())
        return out[:limit]


class QueryReformulator:
    def reformulate(self, question: str, *, topic_hint: str = "") -> dict[str, Any]:
        q = re.sub(r"\s+", " ", (question or "").strip())
        aspects = extract_aspects(q)
        topic = topic_hint.strip() or q[:240]
        queries = build_aspect_queries(topic, aspects, limit=6)
        if not queries and q:
            queries = [q[:240]]
        probes = []
        if q and "مقارنة" not in q and "قارن" not in q:
            probes.append(f"{topic} حقائق مصادر")
        return {
            "original": q,
            "topic": topic,
            "aspects": aspects,
            "queries": list(dict.fromkeys([x for x in queries + probes if x]))[:8],
            "needs_retrieval": bool(queries),
            "agent": "QueryReformulator",
        }


class IterativeRetriever:
    def __init__(self, retrieve_fn: RetrieveFn, *, max_hops: int = 3) -> None:
        self.tool = RetrievalTool(retrieve_fn, max_hops=max_hops)

    def retrieve(self, queries: list[str], *, aspect: str = "") -> dict[str, Any]:
        seed = queries[0] if queries else ""
        extra = queries[1:] if len(queries) > 1 else []
        state = self.tool.run_until_sufficient(seed, aspect=aspect, extra_queries=extra)
        return {
            "results": state.all_results,
            "hop_count": state.hop_count,
            "final_sufficiency": state.to_dict()["final_sufficiency"],
            "hops": state.to_dict()["hops"],
            "agent": "IterativeRetriever",
        }


class HallucinationGuard:
    def __init__(self, *, min_support: float = 0.25) -> None:
        self.min_support = min_support

    def verify_answer(
        self,
        answer: str,
        bank: MemoryBank,
        *,
        aspects: list[str] | None = None,
    ) -> dict[str, Any]:
        claims_text = split_answer_into_claim_sentences(answer)
        bound = [bank.bind_claim(c, min_score=self.min_support) for c in claims_text]
        unsupported = [c for c in bound if c.status == "unsupported"]
        weak = [c for c in bound if c.status == "weak"]
        missing_aspects = []
        blob = (answer or "").casefold()
        for a in aspects or []:
            if a and a.casefold() not in blob:
                ev_blob = " ".join(e.snippet.casefold() for e in bank.evidence.values())
                if a.casefold() not in ev_blob:
                    missing_aspects.append(a)
        return {
            "agent": "HallucinationGuard",
            "claim_count": len(bound),
            "unsupported_count": len(unsupported),
            "weak_count": len(weak),
            "unsupported_samples": [c.text[:160] for c in unsupported[:5]],
            "missing_aspects": missing_aspects,
            "should_abstain": bool(unsupported) and len(unsupported) >= max(1, len(bound) // 2),
            "support_ratio": bank.stats().get("support_ratio", 0.0),
            "honesty_note": (
                "الدعم لفظي/معجمي وليس إثباتًا دلاليًا لصدق الادعاء."
            ),
        }


class FinalComposer:
    def compose(
        self,
        draft: str,
        bank: MemoryBank,
        guard_report: dict[str, Any],
        *,
        language: str = "ar",
    ) -> dict[str, Any]:
        if guard_report.get("should_abstain") and not bank.evidence:
            answer = (
                "لا تتوفر أدلة كافية في المصادر المسترجعة للإجابة بثقة. "
                "يُفضَّل إعادة صياغة السؤال أو توسيع نطاق البحث."
            )
            return {
                "agent": "FinalComposer",
                "answer": answer,
                "abstained": True,
                "citations": bank.citation_map(),
                "memory": bank.to_dict(),
            }

        sentences = split_answer_into_claim_sentences(draft)
        cited_lines: list[str] = []
        for s in sentences:
            claim = bank.bind_claim(s)
            if claim.status == "unsupported":
                continue
            cited_lines.append(bank.format_claim_with_citations(claim))
        if not cited_lines:
            body = draft.strip()
            note = "\n\nتنبيه: تعذّر ربط جمل الإجابة بأدلة كافية؛ راجع المصادر."
            answer = body + note
            abstained = True
        else:
            answer = "\n".join(cited_lines)
            if guard_report.get("missing_aspects"):
                answer += (
                    "\n\nمحاور بلا دعم كافٍ في النتائج: "
                    + "، ".join(guard_report["missing_aspects"][:6])
                )
            abstained = False
        return {
            "agent": "FinalComposer",
            "answer": answer,
            "abstained": abstained,
            "citations": bank.citation_map(),
            "memory": bank.to_dict(),
        }
