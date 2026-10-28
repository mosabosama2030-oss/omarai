"""Retrieval-as-a-Tool for Omarai (agentic RAG primitive).

Instead of a fixed search→context→answer pipe, the reasoner calls this tool
when it decides evidence is needed. Supports multi-hop refinement and
dynamic source-class hints (web | academic | mixed).

Does not bypass SSRF/URL/relevance filters — those stay in the caller's path.
"""
from __future__ import annotations

import re
from dataclasses import asdict, dataclass, field
from typing import Any, Callable
from urllib.parse import urlparse

RetrieveFn = Callable[[str], list[dict[str, Any]]]

_TOKEN = re.compile(r"[a-z0-9]+|[\u0600-\u06FF]+", re.I)

ACADEMIC_MARKERS = (
    "دراسة", "بحث", "ورقة", "paper", "arxiv", "doi", "journal", "peer",
    "systematic", "academic", "علمي", "أكاديمي", "منهجية",
)


@dataclass
class RetrievalObservation:
    query: str
    results: list[dict[str, Any]]
    result_count: int
    unique_domains: int
    sufficiency: str  # none | thin | adequate | rich
    source_class_hint: str = "mixed"
    suggested_next_query: str = ""
    reason: str = ""

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["results"] = [
            {
                "title": r.get("title"),
                "url": r.get("url"),
                "provider": r.get("provider"),
                "snippet": str(r.get("snippet") or "")[:240],
            }
            for r in (self.results or [])[:8]
        ]
        return d


@dataclass
class RetrievalToolState:
    hops: list[RetrievalObservation] = field(default_factory=list)
    all_results: list[dict[str, Any]] = field(default_factory=list)

    @property
    def hop_count(self) -> int:
        return len(self.hops)

    def to_dict(self) -> dict[str, Any]:
        return {
            "hop_count": self.hop_count,
            "result_count": len(self.all_results),
            "hops": [h.to_dict() for h in self.hops],
            "final_sufficiency": self.hops[-1].sufficiency if self.hops else "none",
        }


def _domains(results: list[dict[str, Any]]) -> set[str]:
    out: set[str] = set()
    for item in results or []:
        url = str(item.get("url") or "")
        try:
            host = (urlparse(url).hostname or "").lower().removeprefix("www.")
            if host:
                out.add(host)
        except Exception:
            continue
    return out


def score_sufficiency(results: list[dict[str, Any]]) -> str:
    n = len(results or [])
    d = len(_domains(results))
    if n == 0:
        return "none"
    if n < 2 or d < 1:
        return "thin"
    if n >= 5 and d >= 3:
        return "rich"
    return "adequate"


def infer_source_class_hint(query: str) -> str:
    q = (query or "").casefold()
    if any(m in q for m in ACADEMIC_MARKERS):
        return "academic"
    return "web"


def suggest_refined_query(query: str, observation: RetrievalObservation) -> str:
    base = (query or "").strip()
    if not base:
        return ""
    if observation.sufficiency == "none":
        return f"{base} مصادر موثوقة"
    if observation.sufficiency == "thin":
        if observation.source_class_hint == "academic":
            return f"{base} review paper evidence"
        return f"{base} تقرير رسمي إحصاءات"
    return ""


class RetrievalTool:
    """Callable retrieval tool for the ReAct loop."""

    def __init__(self, retrieve_fn: RetrieveFn, *, max_hops: int = 3) -> None:
        self.retrieve_fn = retrieve_fn
        self.max_hops = max(1, min(int(max_hops), 5))

    def once(self, query: str, *, aspect: str = "") -> RetrievalObservation:
        q = (query or "").strip()
        if aspect and aspect not in q:
            q = f"{q} {aspect}".strip()
        hint = infer_source_class_hint(q)
        try:
            results = list(self.retrieve_fn(q) or [])
        except Exception as exc:  # noqa: BLE001
            return RetrievalObservation(
                query=q,
                results=[],
                result_count=0,
                unique_domains=0,
                sufficiency="none",
                source_class_hint=hint,
                reason=f"retrieve_error:{type(exc).__name__}",
            )
        seen: set[str] = set()
        unique: list[dict[str, Any]] = []
        for item in results:
            if not isinstance(item, dict):
                continue
            url = str(item.get("url") or "").split("#", 1)[0].rstrip("/")
            if not url or url in seen:
                continue
            seen.add(url)
            unique.append(item)
        obs = RetrievalObservation(
            query=q,
            results=unique,
            result_count=len(unique),
            unique_domains=len(_domains(unique)),
            sufficiency=score_sufficiency(unique),
            source_class_hint=hint,
            reason="ok",
        )
        obs.suggested_next_query = suggest_refined_query(query, obs)
        return obs

    def run_until_sufficient(
        self,
        seed_query: str,
        *,
        aspect: str = "",
        extra_queries: list[str] | None = None,
    ) -> RetrievalToolState:
        state = RetrievalToolState()
        queue: list[str] = []
        if seed_query.strip():
            queue.append(seed_query.strip())
        for q in extra_queries or []:
            if isinstance(q, str) and q.strip() and q.strip() not in queue:
                queue.append(q.strip())
        seen_q: set[str] = set()
        while queue and state.hop_count < self.max_hops:
            q = queue.pop(0)
            key = q.casefold()
            if key in seen_q:
                continue
            seen_q.add(key)
            obs = self.once(q, aspect=aspect if state.hop_count == 0 else "")
            state.hops.append(obs)
            for item in obs.results:
                url = str(item.get("url") or "")
                if url and not any(str(x.get("url") or "") == url for x in state.all_results):
                    state.all_results.append(item)
            if obs.sufficiency in {"adequate", "rich"} and state.hop_count >= 1:
                if len(_domains(state.all_results)) >= 2 or obs.sufficiency == "rich":
                    break
            if obs.suggested_next_query and obs.suggested_next_query.casefold() not in seen_q:
                queue.append(obs.suggested_next_query)
        return state
