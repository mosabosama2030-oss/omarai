"""Lightweight RAG evaluation metrics for Omarai (RAGAS-inspired, local).

Metrics (deterministic proxies — not full LLM-as-judge):
- retrieval_relevance
- faithfulness
- answer_coverage (aspects)
- writing_quality_proxy
"""
from __future__ import annotations

import re
from typing import Any

from agents.memory_bank import MemoryBank, split_answer_into_claim_sentences

_TOKEN = re.compile(r"[a-z0-9]+|[\u0600-\u06FF]+", re.I)


def _tokens(text: str) -> set[str]:
    return {t for t in _TOKEN.findall((text or "").casefold()) if len(t) >= 2}


def retrieval_relevance(query: str, sources: list[dict[str, Any]]) -> float:
    qt = _tokens(query)
    if not qt or not sources:
        return 0.0
    scores = []
    for src in sources:
        blob = " ".join(str(src.get(k) or "") for k in ("title", "snippet", "page_text"))
        st = _tokens(blob)
        if not st:
            scores.append(0.0)
            continue
        scores.append(len(qt & st) / max(1, len(qt)))
    return round(sum(scores) / max(1, len(scores)), 3)


def faithfulness_score(answer: str, sources: list[dict[str, Any]]) -> float:
    bank = MemoryBank()
    bank.ingest_sources(sources)
    claims = split_answer_into_claim_sentences(answer)
    if not claims:
        return 0.0
    supported = 0
    for c in claims:
        claim = bank.bind_claim(c, min_score=0.25)
        if claim.status in {"supported", "weak"}:
            supported += 1
    return round(supported / len(claims), 3)


def aspect_coverage(aspects: list[str], answer: str, sources: list[dict[str, Any]]) -> float:
    if not aspects:
        return 1.0
    blob = (answer or "") + " " + " ".join(
        str(s.get("snippet") or s.get("title") or "") for s in (sources or [])
    )
    blob_l = blob.casefold()
    hit = sum(1 for a in aspects if a and a.casefold() in blob_l)
    return round(hit / max(1, len(aspects)), 3)


def writing_quality_proxy(answer: str) -> float:
    text = (answer or "").strip()
    if not text:
        return 0.0
    score = 0.0
    if 40 <= len(text) <= 4000:
        score += 0.4
    if any(p in text for p in (".", "。", "؟", "?")):
        score += 0.2
    if "\n" in text or "،" in text or "," in text:
        score += 0.2
    if "[المصدر" in text or "[source" in text.lower():
        score += 0.2
    return round(min(1.0, score), 3)


def evaluate_rag_case(
    *,
    question: str,
    answer: str,
    sources: list[dict[str, Any]],
    aspects: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "retrieval_relevance": retrieval_relevance(question, sources),
        "faithfulness": faithfulness_score(answer, sources),
        "aspect_coverage": aspect_coverage(list(aspects or []), answer, sources),
        "writing_quality_proxy": writing_quality_proxy(answer),
        "notes": [
            "المقاييس تقريبية حتمية وليست حكم LLM.",
            "faithfulness لفظي عبر MemoryBank وليس entailment دلالي.",
        ],
    }
