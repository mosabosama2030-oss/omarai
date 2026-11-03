"""Regression coverage for the Arabic-first workspace UI and route wiring."""
from __future__ import annotations

import threading
from http.server import ThreadingHTTPServer
from pathlib import Path
from urllib.request import urlopen

from agents.omarai import LeadStore
from api.omarai import Handler


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT / "web" / "workspace.html"


def test_workspace_routes_preserve_existing_agent_and_lead_pages(tmp_path, monkeypatch):
    previous_store = Handler.store
    Handler.store = LeadStore(tmp_path / "workspace-route.sqlite3")
    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_port}"
    try:
        with urlopen(base + "/", timeout=3) as response:
            home = response.read().decode("utf-8")
            assert response.status == 200
            assert "Omarai — مساحة استخبارات المبيعات" in home
            assert 'id="screen-overview"' in home

        with urlopen(base + "/workspace", timeout=3) as response:
            workspace = response.read().decode("utf-8")
            assert response.status == 200
            assert workspace == home

        with urlopen(base + "/agent", timeout=3) as response:
            agent = response.read().decode("utf-8")
            assert response.status == 200
            assert "وكيل البحث والتحليل" in agent

        with urlopen(base + "/leads", timeout=3) as response:
            leads = response.read().decode("utf-8")
            assert response.status == 200
            assert "مساعد اكتشاف العملاء" in leads
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=3)
        Handler.store = previous_store


def test_workspace_contains_sixteen_rtl_modules_and_marks_unimplemented_ones():
    html = WORKSPACE.read_text(encoding="utf-8")
    assert '<html lang="ar" dir="rtl">' in html
    assert html.count('data-view="') == 16
    for marker in (
        "ذكاء المنتج والعرض",
        "حملات الاكتشاف",
        "اكتشاف الطلب",
        "مراقبة التشغيل",
        "صندوق إشارات الطلب",
        "ملف الشركة",
        "مسار التأهيل",
        "استخبارات السوق",
        "المصادر والموصلات",
        "مركز الأدلة",
        "التدقيق",
        "المهام والتنبيهات",
        "الإعدادات والأمان",
        "حالة النظام",
        "غير متاح في API الحالي",
        "غير موصول بعد",
    ):
        assert marker in html


def test_workspace_uses_http_only_session_and_does_not_store_access_tokens():
    html = WORKSPACE.read_text(encoding="utf-8")
    assert 'fetch("/api/session"' in html
    assert 'credentials:"same-origin"' in html
    assert "localStorage" not in html
    assert "sessionStorage" not in html
    assert 'headers.Authorization="Bearer "+token' not in html
    assert 'fetch("/api/diagnostics"' not in html
    assert "same-origin" in html


def test_workspace_uses_safe_source_links_and_dom_text_insertion():
    html = WORKSPACE.read_text(encoding="utf-8")
    assert '["http:","https:"]' in html
    assert 'a.rel="noopener noreferrer"' in html
    assert "n.textContent=String(text)" in html
    assert "innerHTML" not in html


def test_workspace_integrates_only_existing_interactive_api_routes():
    html = WORKSPACE.read_text(encoding="utf-8")
    for route in (
        "/api/health",
        "/api/session",
        "/api/session/logout",
        "/api/leads?limit=500",
        "/api/analyze",
        "/api/leads",
        "/api/agent",
    ):
        assert route in html
    assert "/api/campaigns" not in html
    assert "/api/companies" not in html
    assert "/api/audit" not in html
