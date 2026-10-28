"""Phase C — answer payload transparency for aspect coverage and search honesty."""
from __future__ import annotations

from typing import Any


def build_aspect_answer_preamble(
    aspects: list[str],
    ledger: dict[str, Any] | None,
) -> str:
    if not aspects:
        return ""
    lines = [
        "محاور السؤال التي يُفترض تغطيتها:",
        *[f"- {aspect}" for aspect in aspects[:8]],
    ]
    if ledger:
        missing = ledger.get("missing") or []
        if missing:
            lines.append(
                "تنبيه قبل القراءة: لم يُعثر على مرشح نصي كافٍ لهذه المحاور في النتائج الحالية: "
                + "، ".join(str(m) for m in missing)
                + "."
            )
        lines.append(
            "ملاحظة: تطابق الكلمات مع مصدر لا يعني أن المصدر يثبت صحة الادعاء."
        )
    return "\n".join(lines)


def enrich_answer_payload(
    payload: dict[str, Any],
    *,
    aspects: list[str] | None = None,
    evidence_ledger: dict[str, Any] | None = None,
    diagnostics_ar: list[str] | None = None,
    search_queries: list[str] | None = None,
    repair_sources_added: int = 0,
) -> dict[str, Any]:
    out = dict(payload or {})
    if aspects is not None:
        out["aspects"] = list(aspects)
    if evidence_ledger is not None:
        out["evidence_ledger"] = evidence_ledger
    if diagnostics_ar is not None:
        out["aspect_diagnostics_ar"] = list(diagnostics_ar)
    if search_queries is not None:
        out["search_queries"] = list(search_queries)
    if repair_sources_added:
        out["aspect_repair_sources_added"] = int(repair_sources_added)
    missing = (evidence_ledger or {}).get("missing") or []
    out["aspect_coverage_complete"] = not bool(missing) if aspects else None
    out["aspect_coverage_is_not_truth_score"] = True
    return out


def format_ui_diagnostics_block(
    diagnostics_ar: list[str] | None,
    search_queries: list[str] | None = None,
) -> str:
    parts: list[str] = []
    if search_queries:
        parts.append("الاستعلامات المستخدمة:")
        parts.extend(f"• {q}" for q in search_queries[:8] if q)
    if diagnostics_ar:
        if parts:
            parts.append("")
        parts.append("تغطية المحاور (لفظية، غير تحقّق دلالي):")
        parts.extend(f"• {line}" for line in diagnostics_ar)
    return "\n".join(parts)
