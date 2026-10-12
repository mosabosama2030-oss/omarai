"""HTTP integration tests for Omarai local API and assistant endpoints."""
from __future__ import annotations

import json
import threading
from http.server import ThreadingHTTPServer
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import pytest

from agents.omarai import LeadStore
from api.omarai import Handler


@pytest.fixture
def local_api(tmp_path):
    """Run the real handler on an ephemeral loopback port with an isolated database."""
    previous_store = Handler.store
    Handler.store = LeadStore(tmp_path / "api-test.sqlite3")
    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=3)
        Handler.store = previous_store


def request_json(base, path, method="GET", payload=None, headers=None):
    body = None if payload is None else json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request_headers = dict(headers or {})
    if body is not None and "Content-Type" not in request_headers:
        request_headers["Content-Type"] = "application/json"
    request = Request(base + path, data=body, method=method, headers=request_headers)
    try:
        with urlopen(request, timeout=3) as response:
            return response.status, json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        return error.code, json.loads(error.read().decode("utf-8"))


def test_api_health_analyze_save_duplicate_list_and_status(local_api):
    status, health = request_json(local_api, "/api/health")
    assert status == 200
    assert health["app"] == "Omarai"
    assert health["mode"] == "web-research"

    text = "بدور على شقة في التجمع الخامس وممكن معاينة"
    status, assessment = request_json(
        local_api,
        "/api/analyze",
        method="POST",
        payload={"text": text, "product_terms": ["شقة"], "location_terms": ["التجمع الخامس"]},
    )
    assert status == 200
    assert assessment["label"] == "high_intent"
    assert {item["category"] for item in assessment["matched_signals"]} >= {
        "high", "next_step", "product_context", "location_context"
    }

    payload = {
        "text": text,
        "source_url": "https://example.com/posts/123",
        "platform": "Public website",
        "product_terms": ["شقة"],
        "location_terms": ["التجمع الخامس"],
    }
    status, saved = request_json(local_api, "/api/leads", method="POST", payload=payload)
    assert status == 201
    assert saved["created"] is True
    assert saved["lead"]["assessment"]["label"] == "high_intent"
    assert "product_context" in {
        item["category"] for item in saved["lead"]["assessment"]["matched_signals"]
    }
    status, duplicate = request_json(local_api, "/api/leads", method="POST", payload=payload)
    assert status == 200
    assert duplicate["created"] is False

    status, listing = request_json(local_api, "/api/leads?limit=25")
    assert status == 200
    assert listing["count"] == 1
    lead_id = listing["leads"][0]["id"]

    status, changed = request_json(
        local_api,
        f"/api/leads/{lead_id}/status",
        method="POST",
        payload={"status": "qualified"},
    )
    assert status == 200
    assert changed["lead"]["status"] == "qualified"

    status, stats = request_json(
        local_api, "/api/ask", method="POST", payload={"question": "كام عميل عندي؟"}
    )
    assert status == 200
    assert stats["kind"] == "local_statistics"
    assert "1 إشارة" in stats["answer"]

    status, recommendation = request_json(
        local_api,
        "/api/ask",
        method="POST",
        payload={"question": "مين أفضل إشارة أراجعها؟"},
    )
    assert status == 200
    assert recommendation["kind"] == "lead_recommendation"
    assert payload["source_url"] in recommendation["answer"]


def test_api_rejects_invalid_filters_and_request_shapes(local_api):
    status, error = request_json(local_api, "/api/leads?limit=not-a-number")
    assert status == 400
    assert "limit" in error["error"]

    status, error = request_json(
        local_api, "/api/analyze", method="POST", payload=["not", "an", "object"]
    )
    assert status == 400
    assert "object" in error["error"]

    status, error = request_json(
        local_api, "/api/ask", method="POST", payload={"question": ""}
    )
    assert status == 400
    assert "question" in error["error"]

    status, error = request_json(
        local_api, "/api/leads", method="POST", payload={
            "text": "بدور على شقة", "source_url": "file:///private/data", "platform": "manual"
        }
    )
    assert status == 400
    assert "absolute" in error["error"]


def test_api_blocks_non_json_and_cross_origin_posts(local_api):
    status, error = request_json(
        local_api,
        "/api/ask",
        method="POST",
        payload={"question": "كام عميل؟"},
        headers={"Content-Type": "text/plain"},
    )
    assert status == 415
    assert "Content-Type" in error["error"]

    status, error = request_json(
        local_api,
        "/api/ask",
        method="POST",
        payload={"question": "كام عميل؟"},
        headers={"Origin": "https://attacker.example"},
    )
    assert status == 403
    assert "cross-origin" in error["error"]


def test_ask_is_honest_when_database_is_empty(local_api):
    status, answer = request_json(
        local_api, "/api/ask", method="POST", payload={"question": "مين أفضل إشارة أراجعها؟"}
    )
    assert status == 200
    assert answer["kind"] == "no_data"
    assert "لا توجد إشارة" in answer["answer"]



def test_web_agent_endpoint_uses_agent_result(local_api, monkeypatch):
    from api.omarai import WebAgent

    def fake_answer(self, question, history=None):
        return {
            "answer": "إجابة اختبار [المصدر 1]",
            "question": question,
            "search_query": question,
            "sources": [{"title": "مصدر", "url": "https://example.com", "snippet": "نص", "page_fetched": False}],
            "used_language_model": True,
            "used_web_search": True,
            "warnings": [],
            "kind": "web_research",
        }

    monkeypatch.setattr(WebAgent, "answer", fake_answer)
    status, response = request_json(
        local_api,
        "/api/agent",
        method="POST",
        payload={"question": "ابحث عن موضوع", "history": []},
    )
    assert status == 200
    assert response["kind"] == "web_research"
    assert response["sources"][0]["url"] == "https://example.com"



def test_live_diagnostics_endpoint_returns_report_without_secrets(local_api, monkeypatch):
    from api.omarai import WebAgent

    def fake_diagnostics(self, test_model=True, test_social=False):
        return {
            "overall_status": "passed",
            "checks": {
                "web_search": {"status": "passed", "result_count": 4},
                "language_model": {"status": "passed", "response_received": True},
                "social_search": {"status": "skipped"},
            },
            "model_usage": [{
                "requested_model": "google/gemma-4-31b-it:free",
                "used_model": "google/gemma-4-31b-it:free",
                "fallback_used": "false",
            }],
        }

    monkeypatch.setattr(WebAgent, "diagnostics", fake_diagnostics)
    status, report = request_json(
        local_api,
        "/api/diagnostics",
        method="POST",
        payload={"test_model": True, "test_social": False},
    )
    assert status == 200
    assert report["overall_status"] == "passed"
    assert report["checks"]["web_search"]["result_count"] == 4
    assert "api_key" not in report
    assert "secret" not in str(report)


def test_diagnostics_endpoint_requires_boolean_options(local_api):
    status, error = request_json(
        local_api,
        "/api/diagnostics",
        method="POST",
        payload={"test_model": "yes", "test_social": False},
    )
    assert status == 400
    assert "booleans" in error["error"]
