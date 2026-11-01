"""Static regression checks for sensitive lead-dashboard browser behavior."""
from pathlib import Path

DASHBOARD = Path(__file__).resolve().parents[1] / "web" / "dashboard.html"


def test_hosted_lead_dashboard_can_send_the_private_access_token():
    html = DASHBOARD.read_text(encoding="utf-8")
    assert 'const ACCESS_TOKEN_STORAGE_KEY="omarai_access_token"' in html
    assert 'headers.Authorization="Bearer "+token' in html
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

