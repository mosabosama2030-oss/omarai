"""Static regression checks for sensitive lead-dashboard browser behavior."""
import json
import re
from pathlib import Path

from agents.omarai import LeadStore

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



def test_sales_workspace_uses_http_only_session_and_never_persists_access_token():
    workspace = Path(__file__).resolve().parents[1] / "web" / "workspace.html"
    html = workspace.read_text(encoding="utf-8")

    assert 'api("/api/session")' in html
    assert 'credentials:"same-origin"' in html
    assert 'JSON.stringify({access_token:token})' not in html
    assert "localStorage" not in html
    assert "sessionStorage" not in html
    assert 'api("/api/leads?limit=500")' in html
    assert 'api("/api/health")' in html
    assert 'state.activeView==="system"' in html
    assert 'if(canWrite())panel.append(createSignalForm())' in html
    assert 'if(canWrite())' in html


def test_workspace_uses_approved_neon_command_theme_and_responsive_accessibility():
    workspace = Path(__file__).resolve().parents[1] / "web" / "workspace.html"
    html = workspace.read_text(encoding="utf-8")

    assert "Approved direction: Neon Command" in html
    assert "--bg:#070d16" in html
    assert "rgba(74,216,255,.17)" in html
    assert "@media(max-width:1100px)" in html
    assert "@media(max-width:760px)" in html
    assert "@media(max-width:420px)" in html
    assert "prefers-reduced-motion:reduce" in html
    assert "forced-colors:active" in html
    assert "min-height:42px" in html

def test_workspace_write_controls_match_supported_membership_roles():
    workspace = Path(__file__).resolve().parents[1] / "web" / "workspace.html"
    html = workspace.read_text(encoding="utf-8")

    match = re.search(r"const WRITE_ROLES = (\\[[^\\]]*\\]);", html)
    assert match is not None
    assert set(json.loads(match.group(1))) == set(LeadStore.ALLOWED_ROLES - {"viewer"})
