"""Compound-question aspect extraction and per-aspect search planning for Omarai."""
from __future__ import annotations

import re
from typing import Any

MAX_PLAN_QUERIES = 8
MAX_ASPECTS = 8

_ASPECT_MARKER_RE = re.compile(
    r"(?:من\s+حيث|من\s+ناحية|من\s+الناحية|فيما\s+يتعلق\s+ب|فيما\s+يخص|"
    r"من\s+منظور|in\s+terms\s+of|with\s+respect\s+to|"
    r"from\s+the\s+perspective\s+of|based\s+on\s+the\s+following\s+criteria)"
    r"\s*(.+?)(?=[؟?!.؛;\n]|$)",
    flags=re.IGNORECASE,
)
_COMPARE_RE = re.compile(
    r"(?:قارن(?:ي|وا)?|مقارنة|compare|versus|\bvs\.?\b|الفرق\s+بين)",
    flags=re.IGNORECASE,
)
_DIMENSION_GROUPS = (
    ("العاصمة", ("العاصمة", "عاصمة", "العاصمه", "capital city", "capital of", "capital")),
    ("عدد السكان", ("عدد السكان", "عدد سكان", "السكان", "تعداد السكان", "التعداد السكاني", "population", "population count", "population size")),
    ("السعر", ("السعر", "سعر", "الأسعار", "الاسعار", "التكلفة", "التكلفه", "price", "cost", "pricing")),
    ("البطارية", ("البطارية", "البطاريه", "البطاريات", "battery", "batteries")),
    ("الشحن", ("الشحن", "charging", "charge time")),
    ("الضمان", ("الضمان", "ضمان", "warranty")),
    ("الصيانة", ("الصيانة", "الصيانه", "الإصلاح", "الاصلاح", "maintenance", "repair")),
    ("الأمان", ("الأمان", "الامان", "safety", "security")),
    ("الكاميرا", ("الكاميرا", "كاميرا", "camera")),
    ("الأداء", ("الأداء", "الاداء", "performance")),
    ("المميزات", ("المميزات", "المزايا", "features", "pros")),
    ("العيوب", ("العيوب", "drawbacks", "cons")),
    ("المراجعات", ("المراجعات", "الآراء", "الاراء", "reviews", "opinions")),
    ("الخصوصية", ("الخصوصية", "privacy")),
    ("الاعتمادية", ("الاعتمادية", "الموثوقية", "reliability")),
    ("الدعم", ("الدعم", "support")),
    ("السرعة", ("السرعة", "speed")),
    ("الجودة", ("الجودة", "الجوده", "quality")),
    ("التوفر", ("التوفر", "التوافر", "availability")),
    ("المدى", ("المدى", "range")),
)
_COMPOUND_CONNECTOR_RE = re.compile(
    r"(?:بالإضافة\s+إلى|بالاضافة\s+الى|إلى\s+جانب|الى\s+جانب|"
    r"فضلًا\s+عن|فضلا\s+عن|بجانب|as\s+well\s+as|in\s+addition\s+to|"
    r"along\s+with|however|whereas)",
    flags=re.IGNORECASE,
)


def _normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "")).strip()


def _normalize_key(value: str) -> str:
    text = _normalize_space(value).casefold()
    text = text.translate(str.maketrans({"أ": "ا", "إ": "ا", "آ": "ا", "ة": "ه", "ى": "ي"}))
    return text


def extract_aspects(question: str) -> list[str]:
    if not isinstance(question, str) or not question.strip():
        return []
    text = question.strip()[:4000]
    match = _ASPECT_MARKER_RE.search(text)
    pieces: list[str] = []
    if match:
        raw = match.group(1)
        raw = re.split(
            r"(?:،|,|؛|;)\s*(?:و?اذكر|و?وضح|بيّن|اشرح|and\s+(?:explain|note|discuss))\b",
            raw, maxsplit=1, flags=re.IGNORECASE,
        )[0]
        pieces = re.split(
            r"\s*(?:،|,|؛|;|/)\s*|\s+\band\b\s+|\s+\bas well as\b\s+|"
            r"\s+و(?=ال|[ء-ي])|\s+(?:بالإضافة\s+إلى|بالاضافة\s+الى|"
            r"إلى\s+جانب|الى\s+جانب|فضلًا\s+عن|فضلا\s+عن|بجانب|"
            r"in\s+addition\s+to|along\s+with)\s+",
            raw, flags=re.IGNORECASE,
        )
    else:
        question_parts = [
            part.strip(" \t\r\n-•")
            for part in re.split(r"[؟?]+", text)
            if len(part.strip(" \t\r\n-•")) >= 4
        ]
        if len(question_parts) > 1:
            pieces = question_parts
        else:
            normalized_text = _normalize_key(text)
            found_facets = [
                canonical
                for canonical, aliases in _DIMENSION_GROUPS
                if any(_normalize_key(alias) in normalized_text for alias in aliases)
            ]
            # Joined facet nouns (e.g. "price and warranty") are compound
            # requirements even when the user omits a formal comparison phrase.
            if (
                len(found_facets) >= 2
                or _COMPARE_RE.search(text)
                or _COMPOUND_CONNECTOR_RE.search(text)
            ):
                pieces = found_facets[:MAX_ASPECTS]
    targets: list[str] = []
    seen: set[str] = set()
    for piece in pieces:
        target = re.sub(r"^[\s:،,؛;/.!?\-–—]+|[\s:،,؛;/.!?\-–—]+$", "", piece).strip()
        target = re.sub(r"^(?:و\s*)", "", target).strip()
        if len(target) < 2:
            continue
        if len(target) > 120:
            target = target[:120].rsplit(" ", 1)[0].strip()
        key = _normalize_key(target)
        if key and key not in seen:
            seen.add(key)
            targets.append(target)
        if len(targets) >= MAX_ASPECTS:
            break
    return targets


def build_aspect_queries(topic_query: str, aspects: list[str], *, limit: int = MAX_PLAN_QUERIES) -> list[str]:
    queries: list[str] = []
    seen: set[str] = set()
    topic = _normalize_space(topic_query)
    if topic:
        queries.append(topic)
        seen.add(_normalize_key(topic))
    for aspect in aspects:
        aspect_clean = _normalize_space(str(aspect))
        if not aspect_clean:
            continue
        candidate = _normalize_space(f"{topic} {aspect_clean}" if topic else aspect_clean)[:240]
        key = _normalize_key(candidate)
        if key and key not in seen:
            seen.add(key)
            queries.append(candidate)
        if len(queries) >= max(1, min(int(limit), MAX_PLAN_QUERIES)):
            break
    return queries


def augment_plan_with_aspects(
    plan: dict[str, Any], question: str, topic_query: str, *, compact_fn: Any = None,
) -> dict[str, Any]:
    out = dict(plan or {})
    aspects = extract_aspects(question)
    out["aspects"] = aspects
    base_queries = [str(q).strip() for q in (out.get("queries") or []) if isinstance(q, str) and q.strip()]
    topic = topic_query or (base_queries[0] if base_queries else "")
    if compact_fn is not None:
        try:
            topic = compact_fn(topic) or topic
        except (TypeError, ValueError):
            pass
    aspect_queries = build_aspect_queries(topic, aspects)
    if compact_fn is not None:
        compacted: list[str] = []
        seen: set[str] = set()
        for q in aspect_queries + base_queries:
            try:
                cq = compact_fn(q)
            except (TypeError, ValueError):
                cq = q
            if not cq:
                continue
            key = _normalize_key(cq)
            if key not in seen:
                seen.add(key)
                compacted.append(cq)
            if len(compacted) >= MAX_PLAN_QUERIES:
                break
        out["queries"] = compacted
    else:
        merged: list[str] = []
        seen_m: set[str] = set()
        for q in aspect_queries + base_queries:
            key = _normalize_key(q)
            if key and key not in seen_m:
                seen_m.add(key)
                merged.append(q)
            if len(merged) >= MAX_PLAN_QUERIES:
                break
        out["queries"] = merged
    out["aspect_queries"] = list(out.get("queries") or [])
    return out


def _source_text(source: dict[str, Any]) -> str:
    return " ".join(str(source.get(key) or "") for key in ("title", "snippet", "page_text"))


def build_evidence_ledger(aspects: list[str], sources: list[dict[str, Any]], *, min_term_len: int = 2) -> dict[str, Any]:
    ledger: dict[str, Any] = {"aspects": [], "covered": [], "missing": [], "by_aspect": {}}
    if not aspects:
        ledger["note"] = "no_explicit_aspects"
        return ledger
    for aspect in aspects:
        tokens = [t for t in re.findall(r"[a-z0-9]+|[\u0600-\u06FF]+", _normalize_key(aspect)) if len(t) >= min_term_len]
        matches: list[dict[str, Any]] = []
        for source in sources or []:
            if not isinstance(source, dict):
                continue
            hay = _normalize_key(_source_text(source))
            if not hay:
                continue
            hit = sum(1 for t in tokens if t in hay)
            if tokens and hit >= max(1, (len(tokens) + 1) // 2):
                evidence_type = "page_text" if source.get("page_text") else "snippet" if source.get("snippet") else "title"
                matches.append({
                    "url": source.get("url", ""),
                    "title": source.get("title", ""),
                    "provider": source.get("provider") or (source.get("providers") or ["unknown"])[0],
                    "evidence_type": evidence_type,
                    "lexical_hits": hit,
                    "search_query": source.get("search_query") or ((source.get("queries") or [""])[0] if source.get("queries") else ""),
                })
        entry = {"aspect": aspect, "candidate_count": len(matches), "candidates": matches[:5], "has_lexical_candidate": bool(matches)}
        ledger["by_aspect"][aspect] = entry
        ledger["aspects"].append(aspect)
        if matches:
            ledger["covered"].append(aspect)
        else:
            ledger["missing"].append(aspect)
    ledger["coverage_ratio"] = round(len(ledger["covered"]) / max(1, len(aspects)), 3)
    return ledger


def repair_queries_for_missing_aspects(
    topic_query: str, missing_aspects: list[str], *, limit: int = 3, compact_fn: Any = None,
) -> list[str]:
    topic = _normalize_space(topic_query)
    out: list[str] = []
    seen: set[str] = set()
    for aspect in missing_aspects:
        aspect_clean = _normalize_space(str(aspect))
        if not aspect_clean:
            continue
        raw = f"{topic} {aspect_clean}".strip() if topic else aspect_clean
        if compact_fn is not None:
            try:
                raw = compact_fn(raw) or raw
            except (TypeError, ValueError):
                pass
        raw = _normalize_space(raw)[:240]
        key = _normalize_key(raw)
        if raw and key not in seen:
            seen.add(key)
            out.append(raw)
        if len(out) >= max(1, min(int(limit), 3)):
            break
    return out


def arabic_aspect_diagnostics(ledger: dict[str, Any]) -> list[str]:
    lines: list[str] = []
    if not ledger or ledger.get("note") == "no_explicit_aspects":
        return lines
    covered = ledger.get("covered") or []
    missing = ledger.get("missing") or []
    if covered:
        lines.append("محاور وُجد لها مرشح نصي واحد على الأقل: " + "، ".join(str(x) for x in covered))
    if missing:
        lines.append(
            "محاور بلا مرشح نصي كافٍ في النتائج الحالية: "
            + "، ".join(str(x) for x in missing)
            + ". هذا لا ينفي وجود معلومات خارج النتائج المجلوبة."
        )
    ratio = ledger.get("coverage_ratio")
    if isinstance(ratio, (int, float)):
        lines.append(f"نسبة تغطية المحاور لفظيًا (تقريبية): {int(ratio * 100)}٪.")
    lines.append("تنبيه: وجود مقتطف يطابق كلمات المحور لا يثبت صحة الادعاء.")
    return lines
