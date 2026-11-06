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

def test_workspace_navigation_exposes_six_core_destinations_and_secondary_system_status():
    workspace = Path(__file__).resolve().parents[1] / "web" / "workspace.html"
    html = workspace.read_text(encoding="utf-8")
    match = re.search(r"const menu=\[(.*?)\n\];", html, re.DOTALL)
    assert match is not None
    entries = re.findall(
        r'\{id:"([^"]+)",label:"([^"]+)",icon:"[^"]+",enabled:(true|false)\}',
        match.group(1),
    )
    assert [entry[0] for entry in entries] == [
        "overview", "offer", "campaign", "signals", "pipeline", "indicators"
    ]
    assert all(enabled == "true" for _, _, enabled in entries)
    assert 'id="systemNav"' in html
    assert '$("systemNav").addEventListener("click",()=>navigate("system"))' in html


def test_workspace_overview_uses_three_factual_kpis_and_simple_start_actions():
    workspace = Path(__file__).resolve().parents[1] / "web" / "workspace.html"
    html = workspace.read_text(encoding="utf-8")
    overview = html.split("function renderOverview(){", 1)[1].split("\nfunction emptyState", 1)[0]
    assert 'buildStat("إجمالي الإشارات"' in overview
    assert 'buildStat("تحتاج مراجعة"' in overview
    assert 'buildStat("مؤهلة أو قيد المتابعة"' in overview
    assert "قوية نسبيًا بالقواعد" not in overview
    assert 'action("١. إعداد ملف المنتج"' in overview
    assert 'action("٢. إنشاء حملة اكتشاف"' in overview


def test_workspace_indicators_are_derived_from_loaded_server_data_not_mock_metrics():
    workspace = Path(__file__).resolve().parents[1] / "web" / "workspace.html"
    html = workspace.read_text(encoding="utf-8")
    indicators = html.split("function renderIndicators(){", 1)[1].split("\nfunction renderPlaceholder", 1)[0]
    assert "state.leads.length" in indicators
    assert "state.discoveryRuns.length" in indicators
    assert 'countByStatus(id)' in indicators
    assert "safeHttp(x.source_url)" in indicators
    assert "78%" not in indicators
    assert "12%" not in indicators
    assert "احتمال شراء" in indicators


def test_workspace_indicators_include_responsive_glass_layout_and_semantic_status_colors():
    workspace = Path(__file__).resolve().parents[1] / "web" / "workspace.html"
    html = workspace.read_text(encoding="utf-8")
    assert ".indicator-hero" in html
    assert ".indicator-ring" in html
    assert ".indicator-fill.green" in html
    assert ".indicator-fill.red" in html
    assert "@media(max-width:760px)" in html
    assert "@media(max-width:520px)" in html
    # The ring is created dynamically; verify the DOM attributes are assigned by JS.
    assert 'ring.setAttribute("role","img")' in html
    assert 'ring.setAttribute("aria-label",' in html


def test_workspace_uses_safe_http_source_urls_and_text_only_dom_rendering():
    workspace = Path(__file__).resolve().parents[1] / "web" / "workspace.html"
    html = workspace.read_text(encoding="utf-8")

    assert "function safeHttp(value)" in html
    assert 'u.protocol!=="http:"&&u.protocol!=="https:"' in html
    assert "u.username||u.password" in html
    assert "node.textContent=String(text)" in html
    assert "innerHTML" not in html


def test_workspace_product_profile_and_discovery_screens_are_connected_to_protected_apis():
    workspace = Path(__file__).resolve().parents[1] / "web" / "workspace.html"
    html = workspace.read_text(encoding="utf-8")
    match = re.search(r"const menu=\[(.*?)\n\];", html, re.DOTALL)
    assert match is not None
    entries = re.findall(
        r'\{id:"([^"]+)",label:"([^"]+)",icon:"[^"]+",enabled:(true|false)\}',
        match.group(1),
    )
    roles = {entry_id: enabled == "true" for entry_id, _label, enabled in entries}
    assert roles["offer"] is True
    assert roles["campaign"] is True
    assert 'api("/api/product-profiles")' in html
    assert 'api("/api/product-profiles",{method:"POST",body:payload})' in html
    assert 'api("/api/discoveries",{method:"POST"' in html
    assert 'api("/api/discoveries/"+encodeURIComponent(run.id)+"/signals/"+index+"/save"' in html
    assert 'optional.checked=false' in html
    assert 'optional.disabled=state.role!=="owner"' in html
    assert 'window.location.href="/agent"' in html
    assert "innerHTML" not in html
    assert "Promise.allSettled" in html
    assert "تعذر تحميل بعض البيانات" in html
    assert "النموذج اللغوي المهيأ حاليًا في Omarai" in html
    assert "قد يستهلك حصة أو تكلفة" in html
