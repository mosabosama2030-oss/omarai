"""Static regression checks for sensitive lead-dashboard browser behavior."""
from pathlib import Path

DASHBOARD = Path(__file__).resolve().parents[1] / "web" / "dashboard.html"


def test_hosted_lead_dashboard_exchanges_access_token_for_http_only_session():
    html = DASHBOARD.read_text(encoding="utf-8")
    assert 'fetch("/api/session"' in html
    assert 'JSON.stringify({access_token:token})' in html
    assert 'credentials:"same-origin"' in html
    assert 'headers.Authorization="Bearer "+token' not in html
    assert 'localStorage' not in html
    assert 'sessionStorage' not in html
    assert '$("saveAccessToken").onclick' in html

def test_saved_lead_source_links_reject_non_http_schemes():
    html = DASHBOARD.read_text(encoding="utf-8")
    assert "function safeSourceUrl(value)" in html
    assert '["http:","https:"]' in html
    assert "const sourceUrl=safeSourceUrl(l.source_url)" in html
    assert "const sourceLink=sourceUrl?" in html

def test_lead_status_handler_accepts_sha256_hex_lead_ids():
    html = DASHBOARD.read_text(encoding="utf-8")
    assert 'if(!/^[a-f0-9]{24}$/.test(id||""))return;' in html
    assert 'data-lead-id="' in html

def test_browser_pages_never_store_access_tokens_in_web_storage():
    root = Path(__file__).resolve().parents[1] / "web"
    for name in ("agent.html", "dashboard.html"):
        html = (root / name).read_text(encoding="utf-8")
        assert "localStorage" not in html
        assert "sessionStorage" not in html
        assert "/api/session" in html
        assert "credentials:\"same-origin\"" in html

