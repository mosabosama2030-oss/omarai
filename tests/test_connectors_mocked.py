"""Connector unit tests with mocked HTTP (no live network required)."""
from __future__ import annotations

import json

import agents.search_connectors as sc


def test_openalex_parses_mocked_payload(monkeypatch):
    payload = {
        "results": [
            {
                "display_name": "Electric Vehicles in Egypt",
                "id": "https://openalex.org/W123",
                "primary_location": {"landing_page_url": "https://example.org/paper"},
                "concepts": [{"display_name": "Battery"}],
                "publication_date": "2024-01-01",
            }
        ]
    }

    def fake_json(url, headers=None, timeout=12):
        return payload

    monkeypatch.setattr(sc, "_http_get_json", fake_json)
    rows = sc.search_openalex("electric vehicles Egypt", limit=3)
    assert len(rows) == 1
    assert rows[0]["provider"] == "openalex"
    assert rows[0]["url"] == "https://example.org/paper"
    assert rows[0]["page_fetched"] is False


def test_arxiv_parses_atom(monkeypatch):
    xml = """
    <feed>
      <entry>
        <title>Study of EV Batteries</title>
        <id>http://arxiv.org/abs/2401.00001</id>
        <summary>Battery degradation analysis.</summary>
        <published>2024-01-02T00:00:00Z</published>
      </entry>
    </feed>
    """

    monkeypatch.setattr(sc, "_http_get_text", lambda url, timeout=12: xml)
    rows = sc.search_arxiv("battery", limit=2)
    assert len(rows) == 1
    assert rows[0]["provider"] == "arxiv"
    assert "arxiv.org" in rows[0]["url"]


def test_connector_failure_returns_empty(monkeypatch):
    def boom(*args, **kwargs):
        raise sc.urllib.error.URLError("down")

    monkeypatch.setattr(sc, "_http_get_json", boom)
    assert sc.run_connector("openalex", "query") == []


def test_run_free_academic_dedupe_path(monkeypatch):
    def fake_run(name, query, limit=4):
        return [
            {
                "title": f"{name}-title",
                "url": f"https://example.com/{name}",
                "snippet": "x",
                "page_fetched": False,
                "provider": name,
                "provider_rank": 1,
                "search_query": query,
                "published_at": "",
                "source_class": "academic",
            }
        ]

    monkeypatch.setattr(sc, "run_connector", fake_run)
    rows = sc.run_free_academic_connectors("ev egypt", limit_per=1)
    assert len(rows) == 3
    providers = {r["provider"] for r in rows}
    assert providers == {"openalex", "arxiv", "crossref"}
