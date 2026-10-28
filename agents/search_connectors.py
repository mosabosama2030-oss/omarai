"""Free academic search connectors for Omarai (M1)."""
from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Callable

MAX_CONNECTOR_RESULTS = 6
DEFAULT_TIMEOUT_SECONDS = 5
USER_AGENT = "OmaraiResearchBot/1.0 (mailto:ops@example.com)"
ConnectorFn = Callable[[str, int], list[dict[str, Any]]]


def _clean_text(value: Any, limit: int = 1600) -> str:
    if not isinstance(value, str):
        return ""
    return re.sub(r"\s+", " ", value).strip()[:limit]


def _http_get_json(url: str, headers: dict[str, str] | None = None, timeout: int = DEFAULT_TIMEOUT_SECONDS) -> Any:
    req_headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    if headers:
        req_headers.update(headers)
    request = urllib.request.Request(url, headers=req_headers, method="GET")
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8", errors="replace"))


def _http_get_text(url: str, timeout: int = DEFAULT_TIMEOUT_SECONDS) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT}, method="GET")
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def _result(*, title: str, url: str, snippet: str, provider: str, rank: int, query: str, published_at: str = "", source_class: str = "web") -> dict[str, Any]:
    return {
        "title": _clean_text(title, 300),
        "url": (url or "").strip(),
        "snippet": _clean_text(snippet, 1600),
        "page_fetched": False,
        "provider": provider,
        "provider_rank": rank,
        "search_query": query,
        "published_at": published_at or "",
        "source_class": source_class,
    }


def search_openalex(query: str, limit: int = MAX_CONNECTOR_RESULTS) -> list[dict[str, Any]]:
    if not isinstance(query, str) or not query.strip():
        return []
    params = urllib.parse.urlencode({"search": query.strip()[:240], "per_page": max(1, min(int(limit), MAX_CONNECTOR_RESULTS)), "mailto": os.getenv("OPENALEX_MAILTO", "ops@example.com")})
    data = _http_get_json(f"https://api.openalex.org/works?{params}")
    rows: list[dict[str, Any]] = []
    for item in data.get("results", [])[:limit]:
        if not isinstance(item, dict):
            continue
        title = item.get("display_name") or ""
        url = ""
        primary = item.get("primary_location") or {}
        if isinstance(primary, dict) and primary.get("landing_page_url"):
            url = str(primary.get("landing_page_url"))
        elif item.get("id"):
            url = str(item.get("id"))
        concepts = ", ".join(str(c.get("display_name", "")) for c in (item.get("concepts") or [])[:5] if isinstance(c, dict))
        snippet = f"{title}. {concepts}".strip(". ")
        if title and url:
            rows.append(_result(title=title, url=url, snippet=snippet or title, provider="openalex", rank=len(rows) + 1, query=query, published_at=str(item.get("publication_date") or ""), source_class="academic"))
    return rows


def search_arxiv(query: str, limit: int = MAX_CONNECTOR_RESULTS) -> list[dict[str, Any]]:
    if not isinstance(query, str) or not query.strip():
        return []
    params = urllib.parse.urlencode({"search_query": f"all:{query.strip()[:200]}", "start": 0, "max_results": max(1, min(int(limit), MAX_CONNECTOR_RESULTS))})
    xml_text = _http_get_text(f"https://export.arxiv.org/api/query?{params}")
    entries = re.findall(r"<entry>(.*?)</entry>", xml_text, flags=re.S)
    rows: list[dict[str, Any]] = []
    for entry in entries[:limit]:
        title_m = re.search(r"<title>(.*?)</title>", entry, re.S)
        link_m = re.search(r"<id>(https?://arxiv\.org/abs/[^<]+)</id>", entry)
        summary_m = re.search(r"<summary>(.*?)</summary>", entry, re.S)
        published_m = re.search(r"<published>([^<]+)</published>", entry)
        title = _clean_text(title_m.group(1) if title_m else "")
        link = link_m.group(1) if link_m else ""
        summary = _clean_text(summary_m.group(1) if summary_m else "", 1600)
        published = published_m.group(1) if published_m else ""
        if title and link:
            rows.append(_result(title=title, url=link, snippet=summary or title, provider="arxiv", rank=len(rows) + 1, query=query, published_at=published, source_class="academic"))
    return rows


def search_crossref(query: str, limit: int = MAX_CONNECTOR_RESULTS) -> list[dict[str, Any]]:
    if not isinstance(query, str) or not query.strip():
        return []
    params = urllib.parse.urlencode({"query": query.strip()[:240], "rows": max(1, min(int(limit), MAX_CONNECTOR_RESULTS)), "mailto": os.getenv("CROSSREF_MAILTO", "ops@example.com")})
    data = _http_get_json(f"https://api.crossref.org/works?{params}", headers={"User-Agent": USER_AGENT})
    items = ((data.get("message") or {}).get("items") or [])[:limit]
    rows: list[dict[str, Any]] = []
    for item in items:
        if not isinstance(item, dict):
            continue
        title_list = item.get("title") or []
        title = title_list[0] if isinstance(title_list, list) and title_list else ""
        url = str(item.get("URL") or "")
        container_list = item.get("container-title") or []
        container = container_list[0] if isinstance(container_list, list) and container_list else ""
        year = ""
        issued = item.get("issued") or {}
        if isinstance(issued, dict) and issued.get("date-parts"):
            try:
                year = str(issued["date-parts"][0][0])
            except (IndexError, TypeError, KeyError):
                year = ""
        snippet = _clean_text(f"{title}. {container} {year}".strip())
        if title and url:
            rows.append(_result(title=title, url=url, snippet=snippet, provider="crossref", rank=len(rows) + 1, query=query, published_at=year, source_class="academic"))
    return rows


def search_semantic_scholar(query: str, limit: int = MAX_CONNECTOR_RESULTS) -> list[dict[str, Any]]:
    if not isinstance(query, str) or not query.strip():
        return []
    key = os.getenv("SEMANTIC_SCHOLAR_API_KEY", "").strip()
    params = urllib.parse.urlencode({"query": query.strip()[:240], "limit": max(1, min(int(limit), MAX_CONNECTOR_RESULTS)), "fields": "title,url,abstract,year,externalIds"})
    headers = {"User-Agent": USER_AGENT}
    if key:
        headers["x-api-key"] = key
    data = _http_get_json(f"https://api.semanticscholar.org/graph/v1/paper/search?{params}", headers=headers)
    rows: list[dict[str, Any]] = []
    for item in (data.get("data") or [])[:limit]:
        if not isinstance(item, dict):
            continue
        title = item.get("title") or ""
        url = item.get("url") or ""
        if not url and isinstance(item.get("externalIds"), dict):
            doi = item["externalIds"].get("DOI")
            if doi:
                url = f"https://doi.org/{doi}"
        snippet = item.get("abstract") or title
        year = str(item.get("year") or "")
        if title and url:
            rows.append(_result(title=title, url=url, snippet=snippet, provider="semantic_scholar", rank=len(rows) + 1, query=query, published_at=year, source_class="academic"))
    return rows


CONNECTOR_REGISTRY: dict[str, dict[str, Any]] = {
    "openalex": {"fn": search_openalex, "source_class": "academic", "requires_key": False},
    "arxiv": {"fn": search_arxiv, "source_class": "academic", "requires_key": False},
    "crossref": {"fn": search_crossref, "source_class": "academic", "requires_key": False},
    "semantic_scholar": {"fn": search_semantic_scholar, "source_class": "academic", "requires_key": False},
}


def run_connector(name: str, query: str, limit: int = MAX_CONNECTOR_RESULTS) -> list[dict[str, Any]]:
    meta = CONNECTOR_REGISTRY.get(name)
    if not meta or meta.get("fn") is None:
        return []
    if not isinstance(query, str) or not query.strip():
        return []
    try:
        rows = meta["fn"](query, limit=limit) or []
        return [row for row in rows if isinstance(row, dict) and row.get("url") and row.get("title")]
    except (TimeoutError, urllib.error.URLError, urllib.error.HTTPError, ValueError, KeyError, TypeError, json.JSONDecodeError, OSError):
        return []


def run_free_academic_connectors(query: str, limit_per: int = 4) -> list[dict[str, Any]]:
    combined: list[dict[str, Any]] = []
    for name in ("openalex", "arxiv", "crossref"):
        combined.extend(run_connector(name, query, limit=limit_per))
    return combined
