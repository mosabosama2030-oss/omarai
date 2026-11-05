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
    assert 'href="/agent">وكيل البحث</a>' in html

def test_workspace_write_controls_match_supported_membership_roles():
    workspace = Path(__file__).resolve().parents[1] / "web" / "workspace.html"
    html = workspace.read_text(encoding="utf-8")

    match = re.search(r"const WRITE_ROLES = (\[[^\]]*\]);", html)
    assert match is not None
    assert set(json.loads(match.group(1))) == set(LeadStore.ALLOWED_ROLES - {"viewer"})

def test_workspace_does_not_clear_local_session_state_when_server_logout_fails():
    workspace = Path(__file__).resolve().parents[1] / "web" / "workspace.html"
    html = workspace.read_text(encoding="utf-8")
    start = html.index('$("logoutButton").addEventListener("click"')
    end = html.index('$("addSignalTop").addEventListener', start)
    handler = html[start:end]

    assert "catch(e)" in handler
    assert "alert(" in handler
    assert "catch(_e){}" not in handler
    assert handler.index("await api(\"/api/session/logout\"") < handler.index("state.role=null")
    assert "return" in handler.split("catch(e)", 1)[1].split("state.role=null", 1)[0]

def test_workspace_navigation_matches_the_sixteen_screen_design_and_enabled_routes():
    workspace = Path(__file__).resolve().parents[1] / "web" / "workspace.html"
    html = workspace.read_text(encoding="utf-8")
    match = re.search(r"const menu=\[(.*?)\n\];", html, re.DOTALL)
    assert match is not None
    entries = re.findall(
        r'\{id:"([^"]+)",label:"([^"]+)",icon:"[^"]+",enabled:(true|false)\}',
        match.group(1),
    )
    assert len(entries) == 16
    roles = {entry_id: (label, enabled == "true") for entry_id, label, enabled in entries}
    assert "evidence" in roles
    assert "audit" in roles
    assert roles["opportunities"][1] is False


def test_workspace_uses_safe_http_source_urls_and_text_only_dom_rendering():
    workspace = Path(__file__).resolve().parents[1] / "web" / "workspace.html"
    html = workspace.read_text(encoding="utf-8")

    assert "function safeHttp(value)" in html
    assert 'u.protocol!=="http:"&&u.protocol!=="https:"' in html
    assert "u.username||u.password" in html
    assert "node.textContent=String(text)" in html
    assert "innerHTML" not in html
