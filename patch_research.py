#!/usr/bin/env python3
import re
from pathlib import Path

path = Path.home() / "omarai" / "agents" / "research.py"
src = path.read_text(encoding="utf-8")
backup = path.with_suffix(".py.bak2")
backup.write_text(src, encoding="utf-8")
print("Backup saved:", backup)

# 1) Replace _contains_any using exact string match (no regex)
old_contains = (
    "def _contains_any(text: str, terms: tuple[str, ...]) -> bool:\n"
    "    haystack = text.casefold()\n"
    "    return any(term.casefold() in haystack for term in terms)\n"
)

new_contains = (
    '_ARABIC_RE = re.compile(r"[\u0600-\u06FF]")\n'
    "\n"
    "\n"
    "def _normalize_arabic(text: str) -> str:\n"
    '    if not text:\n'
    '        return ""\n'
    '    return (text.replace("\\u0623", "\\u0627")\n'
    '                .replace("\\u0625", "\\u0627")\n'
    '                .replace("\\u0622", "\\u0627")\n'
    '                .replace("\\u0629", "\\u0647")\n'
    '                .replace("\\u0649", "\\u064a"))\n'
    "\n"
    "\n"
    "def _contains_any(text: str, terms: tuple) -> bool:\n"
    "    if not text:\n"
    "        return False\n"
    "    haystack = _normalize_arabic(text.casefold())\n"
    "    for term in terms:\n"
    "        if not term:\n"
    "            continue\n"
    "        t = _normalize_arabic(term.casefold())\n"
    "        if _ARABIC_RE.search(t):\n"
    "            if t in haystack:\n"
    "                return True\n"
    "        else:\n"
    '            pat = r"(?<![a-zA-Z0-9])" + re.escape(t) + r"(?![a-zA-Z0-9])"\n'
    "            if re.search(pat, haystack):\n"
    "                return True\n"
    "    return False\n"
)

if old_contains not in src:
    print("ERROR: original _contains_any not found")
    raise SystemExit(1)

src = src.replace(old_contains, new_contains, 1)
print("OK: replaced _contains_any")

# 2) Append new helper functions if missing
if "def source_relevance_score" in src:
    print("Note: helpers already present")
else:
    helper = '''


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
    tokens = re.findall(r"\\w+", norm, flags=re.UNICODE)
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

    score = int(title_ratio * 15 + snippet_ratio * 15 + page_ratio * 5)

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
'''
    src = src.rstrip() + "\n" + helper
    print("OK: appended helper functions")

path.write_text(src, encoding="utf-8")
print("SUCCESS:", path)
