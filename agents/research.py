"""Research planning, domain targeting, and multi-query source ranking.

This module is deterministic by design: the language model may propose a plan,
but all queries, result counts and source records are validated before use.
"""
from __future__ import annotations

import re
from typing import Any
from urllib.parse import urlparse

MAX_PLAN_QUERIES = 5
MAX_QUERY_CHARS = 240
MAX_FUSED_RESULTS = 12

SOCIAL_DOMAINS = {
    "reddit": "reddit.com",
    "youtube": "youtube.com",
    "facebook": "facebook.com",
    "instagram": "instagram.com",
    "x": "x.com",
    "twitter": "twitter.com",
    "tiktok": "tiktok.com",
    "linkedin": "linkedin.com",
    "threads": "threads.net",
    "bluesky": "bsky.app",
}

_SOCIAL_TERMS = (
    "social media", "social network", "social posts", "social pages", "public social", "public posts",
    "facebook", "instagram", "reddit", "youtube", "twitter", "x.com",
    "tiktok", "linkedin", "threads", "bluesky",
    "سوشيال", "التواصل الاجتماعي", "مواقع التواصل", "صفحات التواصل",
    "منشورات", "تعليقات الناس", "آراء الناس", "تجارب المستخدمين",
    "تجارب العملاء", "اراء العملاء", "آراء العملاء", "رأي الناس",
    "كلام الناس", "الناس بتقول", "مراجعات العملاء", "تعليقات العملاء",
    "بوستات", "فيدوهات", "فيديوهات", "ريلز", "تويتر", "فيسبوك",
    "انستجرام", "إنستجرام", "تيك توك", "لينكدان", "لينكدإن",
    "مصادر العملاء", "عملاء محتملين", "العملاء المحتملين",
)

_FRESH_TERMS = (
    "latest", "current", "today", "this week", "recent", "breaking", "news",
    "now", "2026", "latest price", "market price", "updated",
    "آخر", "اخر", "احدث", "أحدث", "حاليا", "حالياً", "الآن", "دلوقتي", "النهارده", "مؤخرًا", "مؤخرا", "اليوم", "هذا الاسبوع",
    "هذا الأسبوع", "آخر الأخبار", "اخر الاخبار", "مستجدات", "حديث",
    "سعر اليوم", "الاسعار الحالية", "الأسعار الحالية", "جديد",
)

_DEEP_TERMS = (
    "deep research", "in-depth", "comprehensive", "exhaustive", "compare",
    "comparison", "pros and cons", "investigate", "evidence", "sources",
    "بحث عميق", "بحث معمق", "بحث مكثف", "بحث شامل", "بالتفصيل", "قارن",
    "مقارنة", "استقصاء", "تحقق", "تأكد", "مصادر", "أدلة", "ادلة",
    "كل الجوانب", "بحث واسع", "متكامل",
)


def extract_urls(text: str) -> list[str]:
    """Extract explicit HTTP(S) URLs without trying to interpret their content as instructions."""
    candidates = re.findall(r"https?://[^\s<>()]+", text or "", flags=re.IGNORECASE)
    cleaned: list[str] = []
    for value in candidates:
        url = value.rstrip(".,;!?،؛:)\"'»")
        if url and url not in cleaned:
            cleaned.append(url[:2048])
        if len(cleaned) >= 5:
            break
    return cleaned


def _compact(value: Any, limit: int = MAX_QUERY_CHARS) -> str:
    if not isinstance(value, str):
        return ""
    return re.sub(r"\s+", " ", value).strip()[:limit]


def _contains_any(text: str, terms: tuple[str, ...]) -> bool:
    haystack = text.casefold()
    return any(term.casefold() in haystack for term in terms)


def detect_social_focus(question: str, history: list[dict[str, str]] | None = None) -> bool:
    context = question + " " + " ".join(
        item.get("content", "") for item in (history or [])[-4:]
    )
    return _contains_any(context, _SOCIAL_TERMS)


def detect_freshness(question: str) -> bool:
    return _contains_any(question, _FRESH_TERMS)


def detect_depth(question: str) -> str:
    return "deep" if _contains_any(question, _DEEP_TERMS) else "standard"


def mentioned_social_platforms(text: str) -> list[str]:
    rules = (
        ("reddit", ("reddit", "ريديت")),
        ("youtube", ("youtube", "يوتيوب")),
        ("facebook", ("facebook", "فيسبوك", "فيس بوك")),
        ("instagram", ("instagram", "انستجرام", "إنستجرام")),
        ("x", ("x.com", "twitter", "تويتر", "اكس", "إكس")),
        ("tiktok", ("tiktok", "تيك توك")),
        ("linkedin", ("linkedin", "لينكدان", "لينكدإن")),
        ("threads", ("threads", "ثريدز")),
        ("bluesky", ("bluesky", "بلو سكاي")),
    )
    low = text.casefold()
    return [name for name, aliases in rules if any(alias.casefold() in low for alias in aliases)]


def _followup_query(question: str, history: list[dict[str, str]] | None) -> str:
    q = _compact(question, 500)
    if not q or len(q) >= 100 or not history:
        return q
    follow_markers = (
        "والسعر", "وسعر", "طب ", "وماذا", "وكمان", "طيب", "المصدر",
        "التكلفة", "والتاريخ", "والمميزات", "والعيوب",
        "and the price", "what about", "how about", "and also", "why",
    )
    if not any(marker in q.casefold() for marker in follow_markers):
        return q
    previous = next(
        (_compact(item.get("content", ""), 300) for item in reversed(history)
         if item.get("role") == "user" and item.get("content")),
        "",
    )
    return _compact(previous + " " + q, 500) if previous else q


def fallback_plan(
    question: str, history: list[dict[str, str]] | None = None
) -> dict[str, Any]:
    """Build a small but varied plan when no model planner is configured or parsing fails."""
    contextual_question = _followup_query(question, history)
    direct_urls = extract_urls(question)
    base = _compact(re.sub(r"https?://[^\s<>()]+", " ", contextual_question), 500)
    if not base:
        base = "اقرأ محتوى الصفحة" if re.search(r"[\u0600-\u06FF]", question) else "read the linked page"
    social_focus = detect_social_focus(question, history)
    fresh = detect_freshness(question)
    deep = detect_depth(question)
    platforms = mentioned_social_platforms(question + " " + " ".join(
        item.get("content", "") for item in (history or [])[-4:]
    ))
    queries: list[str] = [base]

    if fresh and base:
        queries.append(_compact(base + " أحدث مستجدات آخر الأخبار", 500))
    if _contains_any(question, ("قارن", "مقارنة", "compare", "versus", "vs", "الفرق بين")):
        queries.append(_compact(base + " مقارنة مراجعات مميزات عيوب", 500))

    if social_focus:
        selected = platforms or ["facebook", "instagram", "reddit"]
        for platform in selected[:3]:
            domain = SOCIAL_DOMAINS[platform]
            site_query = _compact(f"site:{domain} {base}", 500)
            if site_query not in queries:
                queries.append(site_query)

    if deep and not social_focus and len(queries) < MAX_PLAN_QUERIES:
        queries.append(_compact(base + " مصادر موثوقة تقارير إحصاءات", 500))

    unique: list[str] = []
    seen: set[str] = set()
    for query in queries:
        value = _compact(query, 500)
        key = value.casefold()
        if value and key not in seen:
            unique.append(value)
            seen.add(key)
        if len(unique) >= MAX_PLAN_QUERIES:
            break

    return {
        "queries": unique or [base],
        "direct_urls": direct_urls,
        "social_focus": social_focus,
        "freshness": "current" if fresh else "any",
        "depth": deep,
        "platforms": platforms,
        "planning_method": "deterministic_fallback",
    }


def validate_plan(
    candidate: Any, question: str, history: list[dict[str, str]] | None = None
) -> dict[str, Any]:
    fallback = fallback_plan(question, history)
    if not isinstance(candidate, dict):
        return fallback
    raw_queries = candidate.get("queries", [])
    if not isinstance(raw_queries, list):
        return fallback
    queries: list[str] = []
    seen: set[str] = set()
    for item in raw_queries:
        query = _compact(item, 500)
        # Never accept prompt-like multi-line payloads as search-query instructions.
        query = query.replace("\n", " ").replace("\r", " ")
        if len(query) < 2:
            continue
        if query.casefold() not in seen:
            seen.add(query.casefold())
            queries.append(query)
        if len(queries) >= MAX_PLAN_QUERIES:
            break
    if not queries:
        return fallback
    base = fallback_plan(question, history)
    platforms = candidate.get("platforms")
    if not isinstance(platforms, list):
        platforms = base["platforms"]
    safe_platforms = [p for p in platforms if isinstance(p, str) and p in SOCIAL_DOMAINS]
    return {
        "queries": queries,
        "direct_urls": fallback["direct_urls"],
        "social_focus": bool(candidate.get("social_focus", base["social_focus"])),
        "freshness": "current" if candidate.get("freshness") == "current" else base["freshness"],
        "depth": "deep" if candidate.get("depth") == "deep" else base["depth"],
        "platforms": list(dict.fromkeys(safe_platforms))[:5],
        "planning_method": "language_model",
    }


def _canonical_result_url(url: str) -> str:
    try:
        parsed = urlparse(url)
        host = (parsed.hostname or "").lower().removeprefix("www.")
        # Drop fragments and common tracking query parameters before deduplication.
        parts = []
        for part in parsed.query.split("&"):
            key = part.split("=", 1)[0].lower()
            if key.startswith("utm_") or key in {"fbclid", "gclid", "ref", "ref_src"}:
                continue
            if part:
                parts.append(part)
        query = "&".join(sorted(parts))
        path = parsed.path.rstrip("/") or "/"
        return f"{parsed.scheme.lower()}://{host}{path}" + (f"?{query}" if query else "")
    except (ValueError, TypeError):
        return url


def classify_source(url: str) -> dict[str, str]:
    host = (urlparse(url).hostname or "").lower().removeprefix("www.")
    platform = "web"
    mapping = {
        "reddit.com": "reddit", "old.reddit.com": "reddit",
        "youtube.com": "youtube", "youtu.be": "youtube",
        "facebook.com": "facebook", "instagram.com": "instagram",
        "x.com": "x", "twitter.com": "x", "tiktok.com": "tiktok",
        "linkedin.com": "linkedin", "threads.net": "threads",
        "bsky.app": "bluesky",
    }
    for domain, label in mapping.items():
        if host == domain or host.endswith("." + domain):
            platform = label
            break
    trust = "general"
    if host.endswith((".gov", ".gov.eg", ".gov.uk")):
        trust = "government"
    elif host.endswith((".edu", ".ac.uk", ".edu.eg")):
        trust = "academic"
    elif host == "news.google.com" or any(
        name in host
        for name in (
            "reuters.com", "apnews.com", "bbc.com", "bbc.co.uk",
            "ft.com", "nytimes.com", "theguardian.com",
        )
    ):
        trust = "news"
    elif platform != "web":
        trust = "social"
    return {"domain": host, "platform": platform, "source_class": trust}


def fuse_ranked_results(
    batches: list[dict[str, Any]], limit: int = MAX_FUSED_RESULTS
) -> list[dict[str, Any]]:
    """Reciprocal-rank-fuse result sets across queries/providers and dedupe URLs."""
    accumulated: dict[str, dict[str, Any]] = {}
    for batch in batches:
        query = _compact(batch.get("query", ""), 500)
        provider = _compact(batch.get("provider", "search"), 80)
        results = batch.get("results", [])
        if not isinstance(results, list):
            continue
        for position, source in enumerate(results, 1):
            if not isinstance(source, dict) or not source.get("url"):
                continue
            url = _canonical_result_url(str(source["url"]))
            if not url.startswith(("https://", "http://")):
                continue
            entry = accumulated.get(url)
            if entry is None:
                entry = {
                    "title": _compact(source.get("title") or "نتيجة ويب", 300),
                    "url": str(source["url"]),
                    "snippet": _compact(source.get("snippet") or "", 1800),
                    "page_text": _compact(source.get("page_text") or "", 12_000),
                    "page_fetched": bool(source.get("page_fetched")),
                    "providers": [],
                    "queries": [],
                    "rank_score": 0.0,
                    "best_raw_rank": position,
                    "published_at": _compact(source.get("published_at") or "", 100),
                }
                entry.update(classify_source(str(source["url"])))
                accumulated[url] = entry
            entry["rank_score"] += 1.0 / (60 + position)
            entry["best_raw_rank"] = min(entry["best_raw_rank"], position)
            if provider and provider not in entry["providers"]:
                entry["providers"].append(provider)
            if query and query not in entry["queries"]:
                entry["queries"].append(query)
            if len(str(source.get("snippet") or "")) > len(entry["snippet"]):
                entry["snippet"] = _compact(source.get("snippet"), 1800)
            if source.get("published_at") and not entry.get("published_at"):
                entry["published_at"] = _compact(source["published_at"], 100)
            if source.get("page_text") and not entry["page_text"]:
                entry["page_text"] = _compact(source["page_text"], 12_000)
                entry["page_fetched"] = True
    # A cross-query result gets a modest consensus bonus; official/academic sources
    # get a small prior, never enough to override actual query relevance.
    for entry in accumulated.values():
        entry["rank_score"] += min(len(entry["queries"]), 4) * 0.00015
        if entry["source_class"] in {"government", "academic"}:
            entry["rank_score"] += 0.0001
        if "user_supplied_url" in entry["providers"]:
            entry["rank_score"] += 0.5
    ranked = sorted(accumulated.values(), key=lambda item: item["rank_score"], reverse=True)
    return ranked[:max(1, min(int(limit), MAX_FUSED_RESULTS))]
