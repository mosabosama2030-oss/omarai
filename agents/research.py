"""Research planning, domain targeting, and multi-query source ranking.

This module is deterministic by design: the language model may propose a plan,
but all queries, result counts and source records are validated before use.
"""
from __future__ import annotations

import ipaddress
import re
from datetime import UTC, datetime, timedelta
from email.utils import parsedate_to_datetime
from typing import Any
from urllib.parse import urlparse

import tldextract

from agents.intent_router import resolve_followup_query

MAX_PLAN_QUERIES = 8
MAX_QUERY_CHARS = 240
MAX_FUSED_RESULTS = 18


# Use the Public Suffix List snapshot bundled with tldextract; never fetch it at
# runtime. Including private suffixes keeps tenant-hosted sites (e.g. github.io)
# separate, while subdomains belonging to one registrable site share one identity.
_DOMAIN_EXTRACTOR = tldextract.TLDExtract(
    suffix_list_urls=(),
    include_psl_private_domains=True,
)


def registrable_domain(value: Any) -> str:
    """Return a normalized registrable domain (or normalized IP/unknown hostname).

    This is a conservative source-diversity key, not proof that two publishers
    are editorially independent. It prevents sibling subdomains from being
    counted as separate domains in the evidence coverage threshold.
    """
    candidate = str(value or "").strip()
    if not candidate:
        return ""
    parsed = urlparse(candidate if "://" in candidate else "//" + candidate)
    host = (parsed.hostname or "").rstrip(".").lower()
    if not host:
        return ""
    try:
        return str(ipaddress.ip_address(host))
    except ValueError:
        pass
    try:
        host = host.encode("idna").decode("ascii").lower()
    except UnicodeError:
        return host
    extracted = _DOMAIN_EXTRACTOR(host)
    return (extracted.top_domain_under_public_suffix or host).lower()

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


_SEARCH_META_START_RE = re.compile(
    r"^(?:و?استخدم|و?استعمل|و?ميّز|و?ميز|و?اجب|و?أجب|و?لا تعرض|و?لا تقدم|"
    r"please cite|cite|provide links|mention sources|use multiple sources|"
    r"don't present|do not present)\b",
    re.IGNORECASE,
)
# Treat "اذكر" as an action unless its object is clearly citation/format metadata.
# This preserves topic-bearing prompts such as "اذكر أبرز السيارات الكهربائية...".
_SEARCH_CITATION_META_START_RE = re.compile(
    r"^(?:و?اذكر(?:ي|وا)?|mention|cite|provide)\s+"
    r"(?:مصادر?|المصادر|مصدر|روابط?|رابط|تواريخ?|تاريخ|الاخبار|الأخبار|"
    r"the original posts|links|sources|dates)\b",
    re.IGNORECASE,
)
# This is a response-quality instruction, not a topic query.
_SEARCH_UNCERTAINTY_META_START_RE = re.compile(
    r"^و?وضّ?ح\s+اذا\s+كانت\s+النتائج\s+غير\s+كافيه\b"
    r".*(?:لتمثيل|تمثيل).*(?:اراء\s+المستخدمين|المستخدمين)\b",
    re.IGNORECASE,
)
_SEARCH_META_TAIL_RE = re.compile(
    r"\s*[,،؛;]\s*(?:و\s*)?(?:استخدم|استعمل|ميّز|ميز|اجب|أجب|لا تعرض|لا تقدم|"
    r"please cite|cite|provide links|mention sources|use multiple sources|"
    r"don't present|do not present|"
    r"اذكر(?:ي|وا)?\s+(?:مصادر?|المصادر|مصدر|روابط?|رابط|تواريخ?|تاريخ|الاخبار|الأخبار))\b.*$",
    re.IGNORECASE,
)
_SEARCH_LEADING_ACTION_RE = re.compile(
    r"^(?:حلّل|حلل|اجمع|قارن|ناقش|استكشف|استقصِ|اعرض|و?وضح|و?وضّح|و?اذكر(?:ي|وا)?|"
    r"analyze|analyse|compare|investigate|collect|gather|review|summarize|"
    r"(?:ابحث|بحث|دورلي|دور|اعثر)(?:\s+(?:عن|على))?)\s+",
    re.IGNORECASE,
)


def compact_search_query(value: Any, limit: int = MAX_QUERY_CHARS) -> str:
    """Reduce a full request to the topic-bearing query; preserve safety checks elsewhere."""
    if not isinstance(value, str):
        return ""
    cleaned = re.sub(r"https?://[^\s<>()]+", " ", value, flags=re.IGNORECASE)
    # Split question/sentence boundaries without splitting operators such as site:reddit.com.
    segments = re.split(
        r"(?<=[!?؟؛;])\s+|(?<=\.)\s+(?=[A-Z\u0600-\u06FF])",
        cleaned,
    )
    useful: list[str] = []
    for segment in segments:
        segment = segment.strip()
        if not segment:
            continue
        normalized_segment = _normalize_arabic(segment).casefold()
        if (
            _SEARCH_META_START_RE.search(normalized_segment)
            or _SEARCH_CITATION_META_START_RE.search(normalized_segment)
            or _SEARCH_UNCERTAINTY_META_START_RE.search(normalized_segment)
        ):
            continue
        segment = _SEARCH_META_TAIL_RE.sub("", segment).strip()
        segment = _SEARCH_LEADING_ACTION_RE.sub("", segment).strip()
        if segment:
            useful.append(segment)
    result = re.sub(r"\s+", " ", " ".join(useful)).strip(" \t\r\n,،;؛")
    if not result:
        return ""
    try:
        max_chars = max(2, min(int(limit), MAX_QUERY_CHARS))
    except (TypeError, ValueError, OverflowError):
        max_chars = MAX_QUERY_CHARS
    if len(result) > max_chars:
        shortened = result[:max_chars]
        result = shortened.rsplit(" ", 1)[0] if " " in shortened else shortened
    return result


_ARABIC_RE = re.compile(r"[؀-ۿ]")


def _normalize_arabic(text: str) -> str:
    if not text:
        return ""
    return (text.replace("\u0623", "\u0627")
                .replace("\u0625", "\u0627")
                .replace("\u0622", "\u0627")
                .replace("\u0629", "\u0647")
                .replace("\u0649", "\u064a"))


def _contains_any(text: str, terms: tuple) -> bool:
    if not text:
        return False
    haystack = _normalize_arabic(text.casefold())
    for term in terms:
        if not term:
            continue
        t = _normalize_arabic(term.casefold())
        if _ARABIC_RE.search(t):
            if t in haystack:
                return True
        else:
            pat = r"(?<![a-zA-Z0-9])" + re.escape(t) + r"(?![a-zA-Z0-9])"
            if re.search(pat, haystack):
                return True
    return False


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


def fallback_plan(
    question: str, history: list[dict[str, str]] | None = None
) -> dict[str, Any]:
    """Build a small but varied plan when no model planner is configured or parsing fails."""
    contextual_question = resolve_followup_query(question, history)
    direct_urls = extract_urls(question)
    base = compact_search_query(contextual_question)
    if not base:
        base = "اقرأ محتوى الصفحة" if re.search(r"[\u0600-\u06FF]", question) else "read the linked page"
    social_focus = detect_social_focus(question, history)
    fresh = detect_freshness(question)
    detected_depth = detect_depth(question)
    deep = detected_depth == "deep"
    platforms = mentioned_social_platforms(question + " " + " ".join(
        item.get("content", "") for item in (history or [])[-4:]
    ))
    queries: list[str] = [base]

    if fresh and base:
        queries.append(compact_search_query(base + " أحدث مستجدات آخر الأخبار"))
    if _contains_any(question, ("قارن", "مقارنة", "compare", "versus", "vs", "الفرق بين")):
        queries.append(compact_search_query(base + " مقارنة مراجعات مميزات عيوب"))

    if social_focus:
        selected = platforms or ["facebook", "instagram", "reddit"]
        for platform in selected[:3]:
            domain = SOCIAL_DOMAINS[platform]
            site_query = compact_search_query(f"site:{domain} {base}")
            if site_query not in queries:
                queries.append(site_query)

    if deep and not social_focus and len(queries) < MAX_PLAN_QUERIES:
        queries.append(compact_search_query(base + " مصادر موثوقة تقارير إحصاءات"))

    unique: list[str] = []
    seen: set[str] = set()
    for query in queries:
        value = compact_search_query(query)
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
        "depth": detected_depth,
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
        query = compact_search_query(item)
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
                publisher_url = _compact(source.get("publisher_url") or "", 2048)
                source_identity_url = publisher_url or str(source["url"])
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
                    "publisher_name": _compact(source.get("publisher_name") or "", 200),
                    "publisher_url": publisher_url,
                    "publisher_domain": _compact(source.get("publisher_domain") or "", 300),
                }
                entry.update(classify_source(source_identity_url))
                accumulated[url] = entry
            elif source.get("publisher_url") and not entry.get("publisher_url"):
                entry["publisher_url"] = _compact(source.get("publisher_url"), 2048)
                entry["publisher_name"] = _compact(source.get("publisher_name") or "", 200)
                entry["publisher_domain"] = _compact(source.get("publisher_domain") or "", 300)
                entry.update(classify_source(entry["publisher_url"]))
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



def _parse_publication_date(value: Any, now: datetime | None = None) -> datetime | None:
    """Parse common search/RSS publication dates without guessing missing dates."""
    if not isinstance(value, str) or not value.strip():
        return None
    raw = value.strip()
    current = now or datetime.now(UTC)
    try:
        parsed = parsedate_to_datetime(raw)
        if parsed:
            return parsed.replace(tzinfo=parsed.tzinfo or UTC).astimezone(UTC)
    except (TypeError, ValueError, OverflowError):
        pass
    iso_value = raw.replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(iso_value)
        return parsed.replace(tzinfo=parsed.tzinfo or UTC).astimezone(UTC)
    except (TypeError, ValueError, OverflowError):
        pass
    for date_format in ("%b %d, %Y", "%B %d, %Y", "%Y/%m/%d", "%d %b %Y"):
        try:
            return datetime.strptime(raw, date_format).replace(tzinfo=UTC)
        except ValueError:
            continue
    match = re.search(r"(\d+)\s+(hour|day|week|month|year)s?\s+ago", raw, re.IGNORECASE)
    if match:
        amount = int(match.group(1))
        unit = match.group(2).lower()
        durations = {
            "hour": timedelta(hours=amount),
            "day": timedelta(days=amount),
            "week": timedelta(days=7 * amount),
            "month": timedelta(days=30 * amount),
            "year": timedelta(days=365 * amount),
        }
        return current - durations[unit]
    if raw.lower() in {"today", "just now", "now"}:
        return current
    if raw.lower() == "yesterday":
        return current - timedelta(days=1)
    return None


def evidence_signal_report(
    sources: list[dict[str, Any]],
    freshness: str = "any",
    now: datetime | None = None,
) -> dict[str, Any]:
    """Summarize research coverage; signals describe evidence coverage, not factual truth."""
    current = now or datetime.now(UTC)
    valid_sources = [source for source in sources if isinstance(source, dict) and source.get("url")]
    domains = {
        registrable_domain(
            source.get("domain") or urlparse(str(source.get("url") or "")).hostname or ""
        )
        for source in valid_sources
        if source.get("domain") or source.get("url")
    }
    domains.discard("")
    providers: set[str] = set()
    for source in valid_sources:
        candidate_providers = source.get("providers", [])
        if isinstance(candidate_providers, list):
            providers.update(str(item) for item in candidate_providers if item)
        elif source.get("provider"):
            providers.add(str(source["provider"]))
    classes = [str(source.get("source_class") or "general") for source in valid_sources]
    primary_count = sum(item in {"government", "academic", "official"} for item in classes)
    news_count = sum(item == "news" for item in classes)
    social_count = sum(item == "social" for item in classes)
    pages_read = sum(bool(source.get("page_fetched")) for source in valid_sources)
    dates = [
        parsed
        for source in valid_sources
        if (parsed := _parse_publication_date(source.get("published_at"), current)) is not None
    ]
    recent_days = 7 if freshness == "current" else 30
    recent_count = sum((current - parsed).total_seconds() >= 0 and
                       (current - parsed) <= timedelta(days=recent_days) for parsed in dates)
    future_dates = sum(parsed > current + timedelta(days=1) for parsed in dates)
    unique_sources = len(valid_sources)
    # Evidence coverage uses several independent dimensions and is deliberately not a
    # probability that any factual claim is true.
    coverage_points = 0
    coverage_points += min(unique_sources, 10) * 3
    coverage_points += min(len(domains), 8) * 4
    coverage_points += min(len(providers), 4) * 5
    coverage_points += min(pages_read, 8) * 3
    coverage_points += min(primary_count, 4) * 4
    coverage_points += min(len(dates), 8) * 2
    coverage_score = min(100, coverage_points)
    if unique_sources >= 8 and len(domains) >= 5 and len(providers) >= 2 and pages_read >= 3:
        coverage_level = "متعدد المصادر"
    elif unique_sources >= 4 and len(domains) >= 3 and len(providers) >= 1:
        coverage_level = "متوسط"
    else:
        coverage_level = "محدود"

    warnings: list[str] = []
    if unique_sources == 0:
        warnings.append("لا توجد مصادر قابلة للاستشهاد؛ لا تستنتج حقائق من عدم وجود نتائج.")
    if len(domains) < 3:
        warnings.append("تنوع النطاقات محدود؛ لا تعتبر تكرار النتيجة تأكيدًا مستقلًا.")
    if pages_read < 2 and unique_sources:
        warnings.append("تمت قراءة أقل من صفحتين مباشرة؛ بعض الأدلة مقتطفات من محركات البحث فقط.")
    if freshness == "current":
        if not dates:
            warnings.append("لا تتوفر تواريخ نشر قابلة للتحليل؛ حداثة النتائج غير مؤكدة.")
        elif recent_count == 0:
            warnings.append(f"لم يُعثر على مصدر مؤرخ خلال آخر {recent_days} يومًا ضمن التواريخ القابلة للتحليل.")
    if future_dates:
        warnings.append("توجد تواريخ مستقبلية غير متوقعة؛ يجب مراجعتها يدويًا.")
    if social_count and primary_count == 0:
        warnings.append("المصادر اجتماعية فقط دون مصدر رسمي/أكاديمي؛ تعامل معها كآراء أو إشارات لا كحقائق مثبتة.")
    return {
        "unique_sources": unique_sources,
        "unique_domains": len(domains),
        "providers_count": len(providers),
        "providers": sorted(providers),
        "pages_read": pages_read,
        "primary_sources": primary_count,
        "news_sources": news_count,
        "social_sources": social_count,
        "dated_sources": len(dates),
        "recent_sources": recent_count,
        "undated_sources": max(0, unique_sources - len(dates)),
        "date_coverage_percent": round(100 * len(dates) / unique_sources) if unique_sources else 0,
        "coverage_score": coverage_score,
        "coverage_level": coverage_level,
        "score_meaning": "مؤشر تغطية وتنوع الأدلة، وليس احتمال صحة الإجابة.",
        "warnings": warnings,
    }



# ---------------------------------------------------------------------------
# Evidence-aware helpers
# ---------------------------------------------------------------------------

_RELEVANCE_STOPWORDS = {
    "the", "a", "an", "of", "in", "on", "at", "to", "for",
    "is", "are", "was", "were", "be", "been", "being",
    "and", "or", "but", "not", "with", "without",
    "this", "that", "these", "those", "it", "its",
}

_OFFICIAL_CLASSES = {"government", "education", "official"}


def _tokenize(text: str) -> set:
    if not text:
        return set()
    norm = _normalize_arabic(text.casefold())
    tokens = re.findall(r"\w+", norm, flags=re.UNICODE)
    return {t for t in tokens if len(t) >= 3 and t not in _RELEVANCE_STOPWORDS}


def source_relevance_score(src, query: str) -> dict:
    if not isinstance(src, dict):
        return {"accepted": False, "score": 0, "reason": "malformed"}

    title = str(src.get("title") or "")
    snippet = str(src.get("snippet") or "")
    page_text = str(src.get("page_text") or "")
    source_class = str(src.get("source_class") or "general").lower()

    q_tokens = _tokenize(query)
    if not q_tokens:
        return {"accepted": False, "score": 0, "reason": "no_query_tokens"}

    t_tokens = _tokenize(title)
    s_tokens = _tokenize(snippet)
    p_tokens = _tokenize(page_text[:3000])

    title_ratio = len(q_tokens & t_tokens) / max(len(q_tokens), 1)
    snippet_ratio = len(q_tokens & s_tokens) / max(len(q_tokens), 1)
    page_ratio = len(q_tokens & p_tokens) / max(len(q_tokens), 1)

    score = int(title_ratio * 15 + snippet_ratio * 20 + page_ratio * 5)

    if source_class in _OFFICIAL_CLASSES:
        if score >= 5:
            return {"accepted": True, "score": score, "reason": "accepted"}
        return {"accepted": True, "score": score,
                "reason": "kept_official_despite_low_overlap"}

    if score >= 18:
        return {"accepted": True, "score": score, "reason": "accepted"}
    return {"accepted": False, "score": score, "reason": "low_overlap"}


def filter_relevant_sources(sources, query: str, extra_queries=None):
    kept = []
    diag = []
    seen_urls = set()
    seen_titles = set()
    combined = " ".join([query] + list(extra_queries or []))

    for src in sources or []:
        if not isinstance(src, dict):
            diag.append({"reason": "malformed", "url": ""})
            continue
        url = str(src.get("url") or "")
        domain = str(src.get("domain") or "").lower()
        title = str(src.get("title") or "").strip()
        url_key = url.rstrip("/").lower()
        title_key = title.lower() + "|" + domain

        if url_key and url_key in seen_urls:
            diag.append({"reason": "duplicate_url", "url": url})
            continue
        if title and title_key in seen_titles:
            diag.append({"reason": "duplicate_title_domain", "url": url})
            continue

        rel = source_relevance_score(src, combined)
        if not rel["accepted"]:
            diag.append({"reason": rel["reason"], "url": url, "score": rel["score"]})
            continue

        kept.append(src)
        if url_key:
            seen_urls.add(url_key)
        if title:
            seen_titles.add(title_key)
    return kept, diag


def decide_evidence_status(sources, pages_read: int = 0,
                           provider_failures: int = 0,
                           search_attempted: bool = True) -> dict:
    if not search_attempted:
        return {"evidence_status": "failed", "should_abstain": True}

    domains = set()
    has_official = False
    for s in sources or []:
        if not isinstance(s, dict):
            continue
        d = str(s.get("domain") or "").lower()
        if not d:
            url = str(s.get("url") or "")
            if url:
                try:
                    from urllib.parse import urlparse
                    d = urlparse(url).netloc.lower()
                except Exception:
                    d = ""
        if d:
            domains.add(d)
        if str(s.get("source_class") or "").lower() in _OFFICIAL_CLASSES:
            has_official = True

    if not sources:
        if provider_failures > 0:
            return {"evidence_status": "failed", "should_abstain": True}
        return {"evidence_status": "insufficient", "should_abstain": True}

    if len(domains) >= 2 or has_official:
        return {"evidence_status": "adequate", "should_abstain": False}
    if len(domains) >= 1:
        return {"evidence_status": "partial", "should_abstain": False}
    return {"evidence_status": "insufficient", "should_abstain": True}
