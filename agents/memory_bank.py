"""Structured claim–evidence memory bank for Omarai.

Every generated claim can be bound to one or more evidence snippets with a
stable evidence_id. Generation should be constrained by this graph so fluency
never outruns support.

Lexical support ≠ semantic entailment. Status labels are honest about that.

Compatible conceptually with agents.claim_evidence.build_claim_evidence_ledger
(sentence-level citation index tracing on main).
"""
from __future__ import annotations

import hashlib
import re
import time
from dataclasses import asdict, dataclass, field
from typing import Any

_TOKEN = re.compile(r"[a-z0-9]+|[\u0600-\u06FF]+", re.I)
_SENTENCE_SPLIT = re.compile(r"(?<=[.!?؟])\s+|\n+")
_CITATION_MARK = re.compile(r"\[(?:المصدر|source)\s+(\d+)\]", re.I)
_STOP = {
    "من", "في", "على", "عن", "الى", "و", "او", "هل", "ما", "ال", "the", "a", "an",
    "and", "or", "in", "on", "of", "to", "for", "with", "is", "are", "this", "that",
    "إلى", "أن", "إن", "كان", "يكون", "غير", "بين", "حتى", "قد", "لم", "لن",
}


def _norm(text: str) -> str:
    text = (text or "").casefold()
    text = text.translate(str.maketrans({"أ": "ا", "إ": "ا", "آ": "ا", "ة": "ه", "ى": "ي"}))
    return re.sub(r"\s+", " ", text).strip()


def _tokens(text: str) -> set[str]:
    return {t for t in _TOKEN.findall(_norm(text)) if len(t) >= 2 and t not in _STOP}


def _evidence_id(url: str, snippet: str) -> str:
    raw = f"{url}|{snippet[:160]}".encode("utf-8", errors="replace")
    return "ev_" + hashlib.sha1(raw).hexdigest()[:12]


def _claim_id(text: str) -> str:
    return "cl_" + hashlib.sha1((text or "").encode("utf-8", errors="replace")).hexdigest()[:10]


@dataclass
class Evidence:
    evidence_id: str
    url: str
    title: str
    snippet: str
    provider: str = ""
    source_class: str = "web"
    page_fetched: bool = False
    source_index: int = 0

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @property
    def readable(self) -> bool:
        return bool(self.snippet.strip()) or self.page_fetched


@dataclass
class Claim:
    claim_id: str
    text: str
    evidence_ids: list[str] = field(default_factory=list)
    support_score: float = 0.0
    status: str = "unsupported"
    aspect: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class MemoryBank:
    """In-session claim↔evidence graph for agentic RAG."""

    def __init__(self, session_id: str = "") -> None:
        self.session_id = session_id or f"s_{int(time.time())}"
        self.evidence: dict[str, Evidence] = {}
        self.claims: list[Claim] = []
        self.notes: list[str] = []
        self._index_by_id: dict[str, int] = {}

    def ingest_sources(self, sources: list[dict[str, Any]] | None) -> int:
        added = 0
        for src in sources or []:
            if not isinstance(src, dict):
                continue
            url = str(src.get("url") or "").strip()
            title = str(src.get("title") or "").strip()
            snippet = str(
                src.get("snippet") or src.get("page_text") or src.get("content") or ""
            ).strip()
            if not url and not snippet and not title:
                continue
            eid = _evidence_id(url, snippet or title)
            if eid in self.evidence:
                continue
            idx = len(self.evidence) + 1
            self.evidence[eid] = Evidence(
                evidence_id=eid,
                url=url[:2048],
                title=title[:300],
                snippet=(snippet or title)[:1600],
                provider=str(
                    src.get("provider")
                    or (src.get("providers") or [""])[0]
                    or ""
                )[:80],
                source_class=str(src.get("source_class") or "web")[:40],
                page_fetched=bool(src.get("page_fetched")),
                source_index=idx,
            )
            self._index_by_id[eid] = idx
            added += 1
        return added

    def _score_claim_against(self, claim_text: str, ev: Evidence) -> float:
        ct = _tokens(claim_text)
        et = _tokens(f"{ev.title} {ev.snippet}")
        if not ct or not et:
            return 0.0
        return len(ct & et) / max(1, len(ct))

    def bind_claim(
        self,
        text: str,
        *,
        min_score: float = 0.25,
        aspect: str = "",
        top_k: int = 3,
    ) -> Claim:
        text = re.sub(r"\s+", " ", (text or "").strip())
        clean = _CITATION_MARK.sub("", text).strip()
        cid = _claim_id(clean)
        scored: list[tuple[float, str]] = []
        for eid, ev in self.evidence.items():
            s = self._score_claim_against(clean, ev)
            if s >= min_score:
                scored.append((s, eid))
        scored.sort(reverse=True)
        top = scored[: max(1, min(int(top_k), 5))]
        score = top[0][0] if top else 0.0
        if score >= 0.45:
            status = "supported"
        elif score >= min_score:
            status = "weak"
        else:
            status = "unsupported"
        claim = Claim(
            claim_id=cid,
            text=clean[:500],
            evidence_ids=[eid for _, eid in top],
            support_score=round(score, 3),
            status=status,
            aspect=str(aspect or "")[:80],
        )
        self.claims.append(claim)
        return claim

    def bind_answer(
        self,
        answer: str,
        *,
        min_score: float = 0.25,
        aspects: list[str] | None = None,
    ) -> list[Claim]:
        sentences = split_answer_into_claim_sentences(answer)
        bound: list[Claim] = []
        aspect_list = list(aspects or [])
        for i, sentence in enumerate(sentences):
            aspect = aspect_list[i] if i < len(aspect_list) else ""
            if not aspect:
                for a in aspect_list:
                    if a and a.casefold() in sentence.casefold():
                        aspect = a
                        break
            bound.append(self.bind_claim(sentence, min_score=min_score, aspect=aspect))
        return bound

    def format_claim_with_citations(self, claim: Claim) -> str:
        if not claim.evidence_ids:
            return claim.text
        markers: list[str] = []
        for eid in claim.evidence_ids:
            idx = self._index_by_id.get(eid)
            if idx:
                markers.append(f"[المصدر {idx}]")
        if not markers:
            return claim.text
        return f"{claim.text} {' '.join(dict.fromkeys(markers))}"

    def render_supported_answer(self, *, drop_unsupported: bool = True) -> str:
        lines: list[str] = []
        for claim in self.claims:
            if drop_unsupported and claim.status == "unsupported":
                continue
            lines.append(self.format_claim_with_citations(claim))
        return "\n".join(lines)

    def citation_map(self) -> list[dict[str, Any]]:
        rows = []
        for eid, ev in self.evidence.items():
            rows.append({
                "index": ev.source_index or self._index_by_id.get(eid, 0),
                "evidence_id": eid,
                "title": ev.title,
                "url": ev.url,
                "provider": ev.provider,
                "source_class": ev.source_class,
                "readable": ev.readable,
            })
        return sorted(rows, key=lambda r: r["index"])

    def stats(self) -> dict[str, Any]:
        supported = sum(1 for c in self.claims if c.status == "supported")
        weak = sum(1 for c in self.claims if c.status == "weak")
        unsupported = sum(1 for c in self.claims if c.status == "unsupported")
        total = len(self.claims)
        return {
            "session_id": self.session_id,
            "evidence_count": len(self.evidence),
            "claim_count": total,
            "supported": supported,
            "weak": weak,
            "unsupported": unsupported,
            "support_ratio": round(
                (supported + 0.5 * weak) / max(1, total), 3
            ) if total else 0.0,
            "readable_evidence": sum(1 for e in self.evidence.values() if e.readable),
        }

    def graph(self) -> dict[str, Any]:
        edges = []
        for c in self.claims:
            for eid in c.evidence_ids:
                edges.append({
                    "claim_id": c.claim_id,
                    "evidence_id": eid,
                    "status": c.status,
                    "support_score": c.support_score,
                    "aspect": c.aspect,
                })
        return {
            "nodes_claims": [c.to_dict() for c in self.claims],
            "nodes_evidence": [e.to_dict() for e in self.evidence.values()],
            "edges": edges,
        }

    def to_claim_evidence_ledger_shape(self) -> dict[str, Any]:
        segments = []
        for i, c in enumerate(self.claims, start=1):
            refs = []
            for eid in c.evidence_ids:
                ev = self.evidence.get(eid)
                if not ev:
                    continue
                refs.append({
                    "source_index": ev.source_index,
                    "reference_status": (
                        "valid_index_with_readable_evidence"
                        if ev.readable
                        else "valid_index_without_readable_evidence"
                    ),
                    "title": ev.title,
                    "url": ev.url,
                    "evidence_basis": (
                        "extracted_page_text" if ev.page_fetched else "search_snippet"
                    ),
                })
            if c.status == "supported":
                status = "cited_source_attached"
            elif c.status == "weak":
                status = "weak_lexical_overlap"
            else:
                status = "uncited"
            segments.append({
                "sentence_number": i,
                "text": c.text,
                "status": status,
                "support_score": c.support_score,
                "refs": refs,
                "aspect": c.aspect,
            })
        return {
            "method": "memory_bank_lexical_bind",
            "segments": segments,
            "stats": self.stats(),
            "citation_map": self.citation_map(),
            "honesty": (
                "الربط لفظي/معجمي عبر MemoryBank؛ ليس إثباتًا دلاليًا لصدق الادعاء."
            ),
        }

    def to_dict(self) -> dict[str, Any]:
        return {
            "session_id": self.session_id,
            "evidence": [e.to_dict() for e in self.evidence.values()],
            "claims": [c.to_dict() for c in self.claims],
            "notes": list(self.notes),
            "stats": self.stats(),
            "citation_map": self.citation_map(),
            "graph": self.graph(),
        }


def split_answer_into_claim_sentences(answer: str, *, min_len: int = 12) -> list[str]:
    parts = [p.strip() for p in _SENTENCE_SPLIT.split(answer or "") if p and p.strip()]
    return [p for p in parts if len(p) >= min_len][:40]


def build_memory_from_sources_and_answer(
    sources: list[dict[str, Any]] | None,
    answer: str,
    *,
    aspects: list[str] | None = None,
    session_id: str = "",
    min_score: float = 0.25,
) -> MemoryBank:
    bank = MemoryBank(session_id=session_id)
    bank.ingest_sources(sources)
    bank.bind_answer(answer, min_score=min_score, aspects=aspects)
    return bank
