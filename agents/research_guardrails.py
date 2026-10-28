"""Task-specific guardrails for search evidence.

These checks are conservative retrieval filters, not proof of factual correctness.
"""
from __future__ import annotations

import re
from datetime import UTC, datetime, timedelta
from typing import Any
from urllib.parse import urlsplit

from agents.research import (
    SOCIAL_DOMAINS,
    _parse_publication_date,
    detect_freshness,
)

_CURRENT_EVIDENCE_MAX_AGE_DAYS = 7
_GOVERNMENT_SUFFIXES = (
    ".gov", ".gov.eg", ".gov.uk", ".gov.sa", ".gov.ae", ".gov.au",
    ".gov.in", ".gov.cn", ".gov.br", ".gob.mx", ".go.jp", ".gc.ca",
    ".govt.nz", ".gouv.fr",
)
_CURRENT_GOVERNMENT_SERVICE_TERMS = (
    "الجوازات", "مكتب الجوازات", "مصلحة الجوازات", "السجل المدني",
    "الشهر العقاري", "مكتب المرور", "إدارة المرور", "مكتب حكومي",
    "خدمة حكومية", "مصلحة حكومية", "وزارة", "هيئة حكومية",
    "passport office", "civil registry", "traffic office",
    "government office", "government service",
)
_GOVERNMENT_HOURS_TERMS = (
    "مواعيد", "مواعيد العمل", "ساعات العمل", "يفتح", "مفتوح",
    "يغلق", "مواعيد الدوام", "working hours", "opening hours",
    "office hours", "open today", "closes today",
)
_OFFICIAL_WORDS = (
    "الموقع الرسمي", "موقع رسمي", "الصفحة الرسمية", "الموقع الحكومي",
    "official website", "official site", "official homepage",
)
_GOVERNMENT_ENTITY_WORDS = (
    "وزارة", "الوزارة", "وزاره", "هيئة حكومية", "جهة حكومية", "مصلحة حكومية",
    "ministry", "government agency", "government ministry", "department of",
)
_TODAY_WORDS = (
    "اليوم", "النهارده", "النهاردة", "دلوقتي", "الآن", "حاليا",
    "today", "right now", "currently", "current hours",
)
_PROMOTION_TERMS = (
    "للبيع", "للايجار", "للإيجار", "تواصل معنا", "اتصل الآن", "واتساب",
    "للحجز", "اشتر الآن", "اطلب الآن", "خصم", "عرض خاص", "السعر يبدأ",
    "for sale", "contact us", "call now", "whatsapp", "buy now", "shop now",
    "special offer", "discount", "sponsored", "affiliate",
)
_PERSONAL_EXPERIENCE_TERMS = (
    "أنا امتلك", "انا امتلك", "أنا أملك", "انا املك", "عندي", "معايا",
    "جربت", "استخدمت", "اشتريت", "امتلكت", "تجربتي", "عن تجربتي",
    "بقالى", "بقالي", "I own", "I bought", "I have owned", "my experience",
    "I've had", "i have had", "I use", "I drove", "in my experience",
)
_DISCUSSION_TERMS = (
    "حد جرب", "هل جرب", "مين جرب", "ما رأيكم", "ايه رأيكم", "ماذا تظنون",
    "anyone tried", "has anyone", "what do you think", "looking for opinions",
)


def _normalized(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip().casefold()


def _host(value: Any) -> str:
    try:
        return (urlsplit(str(value or "").strip()).hostname or "").rstrip(".").lower()
    except (TypeError, ValueError):
        return ""


def is_social_platform_url(url: Any) -> bool:
    """Return whether a URL belongs to a recognized public social platform."""
    host = _host(url)
    if not host:
        return False
    return any(host == domain or host.endswith("." + domain)
               for domain in SOCIAL_DOMAINS.values())


def _is_navigation_request(question: str) -> bool:
    value = _normalized(question)
    return any(term in value for term in (
        "موقع", "رابط", "لينك", "homepage", "website", "official site",
        "official website", "link to",
    ))


def requires_official_government_domain(question: str) -> bool:
    """Detect explicit requests for a government's official site, not articles about it."""
    value = _normalized(question)
    return (
        any(term in value for term in _OFFICIAL_WORDS)
        and any(term in value for term in _GOVERNMENT_ENTITY_WORDS)
    )


def _is_government_domain(url: Any) -> bool:
    host = _host(url)
    if not host:
        return False
    return any(host == suffix.lstrip(".") or host.endswith(suffix)
               for suffix in _GOVERNMENT_SUFFIXES)


def requires_official_current_government_source(question: str) -> bool:
    """Require an official-domain candidate for current government service hours."""
    value = _normalized(question)
    has_service = any(
        _normalized(term) in value for term in _CURRENT_GOVERNMENT_SERVICE_TERMS
    )
    has_hours = any(
        _normalized(term) in value for term in _GOVERNMENT_HOURS_TERMS
    )
    return detect_freshness(question) and has_service and has_hours


def assess_current_source(
    source: dict[str, Any],
    *,
    now: datetime | None = None,
    max_age_days: int = _CURRENT_EVIDENCE_MAX_AGE_DAYS,
) -> dict[str, Any]:
    """Assess whether a read page can support a current-state claim."""
    current = now or datetime.now(UTC)
    if current.tzinfo is None:
        current = current.replace(tzinfo=UTC)
    published = _parse_publication_date(source.get("published_at"), current)
    if published is None:
        return {"eligible": False, "status": "date_unavailable", "age_days": None}
    if published > current + timedelta(days=1):
        return {"eligible": False, "status": "future_date", "age_days": None}
    age_days = max(0, (current - published).total_seconds() / 86400)
    if age_days > max_age_days:
        return {
            "eligible": False,
            "status": "stale",
            "age_days": round(age_days, 2),
            "max_age_days": max_age_days,
        }
    if not bool(source.get("page_fetched")) or not str(source.get("page_text") or "").strip():
        return {
            "eligible": False,
            "status": "page_not_read",
            "age_days": round(age_days, 2),
            "max_age_days": max_age_days,
        }
    return {
        "eligible": True,
        "status": "recent_page_read",
        "age_days": round(age_days, 2),
        "max_age_days": max_age_days,
    }


def classify_social_source(source: dict[str, Any]) -> dict[str, str]:
    """Apply a transparent, non-authoritative label to public social content."""
    url = source.get("url", "")
    host = _host(url)
    platform = next((
        name for name, domain in SOCIAL_DOMAINS.items()
        if host == domain or host.endswith("." + domain)
    ), "")
    if not platform:
        return {
            "opinion_source_classification": "not_a_social_post",
            "opinion_classification_basis": "URL host is not a recognized social platform",
            "opinion_classification_method": "heuristic_only",
        }

    text = _normalized(" ".join(
        str(source.get(field) or "")
        for field in ("title", "snippet", "page_text")
    ))
    # Normalize the vocabulary as well as the source text so English phrases
    # remain case-insensitive (for example, "I own" versus "i own").
    def has_term(terms: tuple[str, ...]) -> bool:
        return any(_normalized(term) in text for term in terms)
    if has_term(_PROMOTION_TERMS):
        label = "promotional_or_commercial"
        basis = "commercial language detected"
    elif has_term(_PERSONAL_EXPERIENCE_TERMS):
        label = "personal_experience_candidate"
        basis = "first-person experience language detected"
    elif has_term(_DISCUSSION_TERMS):
        label = "discussion_or_question"
        basis = "question or discussion language detected"
    else:
        label = "social_post_unclassified"
        basis = "no clear experience/discussion signal; manual review needed"
    return {
        "opinion_source_classification": label,
        "opinion_classification_basis": basis,
        "opinion_classification_method": "heuristic_only",
    }


def apply_source_guardrails(
    question: str,
    mode: str,
    plan: dict[str, Any],
    sources: list[dict[str, Any]],
    *,
    now: datetime | None = None,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Apply official-domain, current-evidence, and explicit social-mode guards.

    Rejection counters describe this filter stage only. They are not search-engine
    totals, and passing them is not a semantic fact check.
    """
    clean_mode = str(mode or "auto").strip().lower()
    explicit_official_site_request = requires_official_government_domain(question)
    current_government_hours_request = requires_official_current_government_source(question)
    official_required = explicit_official_site_request or current_government_hours_request
    # Latest mode always requires a recent read page. Auto mode also does so for
    # explicitly current questions when the planner recognizes freshness, plus
    # current government-service hours even if the planner misses that signal.
    explicit_current_request = detect_freshness(question)
    freshness_required = (
        (
            clean_mode == "latest"
            or (
                plan.get("freshness") == "current"
                and explicit_current_request
            )
            or current_government_hours_request
        )
        and not _is_navigation_request(question)
    )
    social_required = clean_mode == "social"
    retained: list[dict[str, Any]] = []
    rejected: dict[str, int] = {}
    reasons: list[dict[str, str]] = []

    def reject(reason: str, source: dict[str, Any]) -> None:
        rejected[reason] = rejected.get(reason, 0) + 1
        reasons.append({
            "reason": reason,
            "url": str(source.get("url") or "")[:2048],
        })

    for candidate in (sources if isinstance(sources, list) else []):
        if not isinstance(candidate, dict):
            rejected["malformed_candidate"] = rejected.get("malformed_candidate", 0) + 1
            reasons.append({"reason": "malformed_candidate", "url": ""})
            continue
        source = dict(candidate)
        if official_required and not _is_government_domain(source.get("url")):
            reject("not_an_official_government_domain", source)
            continue
        if social_required and not is_social_platform_url(source.get("url")):
            reject("not_a_social_platform_source", source)
            continue
        if freshness_required:
            freshness = assess_current_source(source, now=now)
            source["current_evidence_assessment"] = freshness
            if not freshness["eligible"]:
                reject(str(freshness["status"]), source)
                continue
        if social_required or bool(plan.get("social_focus")):
            source.update(classify_social_source(source))
        retained.append(source)

    status = "passed" if not rejected else "filtered"
    if freshness_required and retained:
        current_status = "eligible_recent_read_pages_only"
    elif freshness_required:
        current_status = "no_current_eligible_evidence"
    else:
        current_status = "not_required"
    summary = {
        "status": status,
        "input_sources": len(sources) if isinstance(sources, list) else 0,
        "accepted_sources": len(retained),
        "rejected_sources": sum(rejected.values()),
        "rejection_counts": rejected,
        "rejection_details": reasons[:20],
        "official_government_domain_required": official_required,
        "official_government_domain_reason": (
            "explicit_official_site_request"
            if explicit_official_site_request
            else "current_government_service_hours"
            if current_government_hours_request
            else "not_required"
        ),
        "official_domain_policy": (
            "government-domain candidate only; organization ownership is not independently verified"
            if official_required else "not_required"
        ),
        "current_evidence_required": freshness_required,
        "current_evidence_status": current_status,
        "current_evidence_max_age_days": _CURRENT_EVIDENCE_MAX_AGE_DAYS if freshness_required else None,
        "social_platform_only": social_required,
        "interpretation": "retrieval guardrail only; passing is not proof of claim correctness",
    }
    return retained, summary
