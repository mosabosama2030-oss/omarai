"""HTTP-level tenant authorization regression tests."""
from __future__ import annotations

import json
import threading
from collections import defaultdict, deque
from http.server import ThreadingHTTPServer
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import pytest

from agents.omarai import LeadStore
from api.omarai import Handler


@pytest.fixture
def tenant_api(tmp_path, monkeypatch):
    monkeypatch.setenv("OMARAI_PUBLIC_DEPLOYMENT", "1")
    monkeypatch.delenv("OMARAI_ACCESS_TOKEN", raising=False)
    previous_store = Handler.store
    previous_request_times = Handler._request_times
    previous_rate_cleanup = Handler._rate_last_cleanup
    Handler._request_times = defaultdict(deque)
    Handler._rate_last_cleanup = 0.0
    Handler.store = LeadStore(tmp_path / "tenant-api.sqlite3")
    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}", Handler.store
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=3)
        Handler.store = previous_store
        Handler._request_times = previous_request_times
        Handler._rate_last_cleanup = previous_rate_cleanup


def request_json(base, path, *, method="GET", payload=None, token=""):
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    headers = {}
    if body is not None:
        headers["Content-Type"] = "application/json"
    if token:
        headers["Authorization"] = "Bearer " + token
    request = Request(base + path, data=body, method=method, headers=headers)
    try:
        with urlopen(request, timeout=3) as response:
            return response.status, json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        return error.code, json.loads(error.read().decode("utf-8"))


def _tenant(store, name, email, token):
    tenant_id = store.create_tenant(name, name.casefold())
    user_id = store.create_user(email, name + " User")
    store.add_membership(tenant_id, user_id, "sales_agent")
    store.create_api_token(token, tenant_id, user_id, label=name)
    return tenant_id


def test_api_ignores_client_tenant_id_and_blocks_cross_tenant_reads_and_updates(tenant_api):
    base, store = tenant_api
    token_a = "tenant-a-token-" + "A" * 32
    token_b = "tenant-b-token-" + "B" * 32
    tenant_a = _tenant(store, "Company A", "api-a@example.test", token_a)
    tenant_b = _tenant(store, "Company B", "api-b@example.test", token_b)

    status, created_a = request_json(
        base,
        "/api/leads",
        method="POST",
        token=token_a,
        payload={
            "tenant_id": tenant_b,
            "text": "Buyer A wants to purchase",
            "source_url": "https://example.test/a",
            "platform": "public",
        },
    )
    assert status == 201
    assert created_a["lead"]["tenant_id"] == tenant_a

    status, created_b = request_json(
        base,
        "/api/leads",
        method="POST",
        token=token_b,
        payload={
            "tenant_id": tenant_a,
            "text": "Buyer B wants to purchase",
            "source_url": "https://example.test/b",
            "platform": "public",
        },
    )
    assert status == 201
    assert created_b["lead"]["tenant_id"] == tenant_b

    status, listing_a = request_json(
        base, f"/api/leads?tenant_id={tenant_b}", token=token_a
    )
    assert status == 200
    assert [lead["id"] for lead in listing_a["leads"]] == [created_a["lead"]["id"]]

    status, listing_b = request_json(base, "/api/leads", token=token_b)
    assert status == 200
    assert [lead["id"] for lead in listing_b["leads"]] == [created_b["lead"]["id"]]

    status, denied = request_json(
        base,
        f"/api/leads/{created_b['lead']['id']}/status",
        method="POST",
        token=token_a,
        payload={"status": "qualified"},
    )
    assert status == 404
    assert denied["error"] == "lead not found"

    status, changed = request_json(
        base,
        f"/api/leads/{created_b['lead']['id']}/status",
        method="POST",
        token=token_b,
        payload={"status": "qualified"},
    )
    assert status == 200
    assert changed["lead"]["status"] == "qualified"


def test_public_api_rejects_unknown_token(tenant_api):
    base, _ = tenant_api
    status, error = request_json(
        base,
        "/api/leads",
        token="unknown-token-" + "X" * 32,
    )
    assert status == 401
    assert "رمز الوصول" in error["error"]


def test_viewer_membership_is_read_only(tenant_api):
    base, store = tenant_api
    tenant_id = store.create_tenant("Viewer Org", "viewer-org")
    user_id = store.create_user("viewer@example.test", "Viewer")
    store.add_membership(tenant_id, user_id, "viewer")
    token = "viewer-token-" + "V" * 32
    store.create_api_token(token, tenant_id, user_id, label="viewer")

    status, listing = request_json(base, "/api/leads", token=token)
    assert status == 200

    status, denied = request_json(
        base,
        "/api/leads",
        method="POST",
        token=token,
        payload={
            "text": "Should fail",
            "source_url": "https://example.test/viewer",
            "platform": "public",
        },
    )
    assert status == 403


def test_api_revokes_only_the_authenticated_api_token(tenant_api):
    base, store = tenant_api
    tenant_id = store.create_tenant("Revocable", "revocable")
    user_id = store.create_user("revocable@example.test", "Owner")
    store.add_membership(tenant_id, user_id, "owner")
    token = "revocable-token-" + "R" * 32
    store.create_api_token(token, tenant_id, user_id)

    status, result = request_json(
        base, "/api/tokens/revoke", method="POST", token=token, payload={}
    )
    assert status == 200
    assert result == {"revoked": True}

    status, denied = request_json(base, "/api/leads", token=token)
    assert status == 401
    assert "رمز الوصول" in denied["error"]


def test_api_does_not_claim_to_revoke_shared_environment_token(
    tenant_api, monkeypatch
):
    base, _ = tenant_api
    shared_token = "shared-application-token-" + "S" * 32
    monkeypatch.setenv("OMARAI_ACCESS_TOKEN", shared_token)

    status, result = request_json(
        base,
        "/api/tokens/revoke",
        method="POST",
        token=shared_token,
        payload={},
    )
    assert status == 409
    assert "rotated by the operator" in result["error"]


def test_live_diagnostics_requires_explicit_approval_before_any_provider_call(
    tenant_api, monkeypatch
):
    from api.omarai import WebAgent

    base, store = tenant_api
    tenant_id = store.create_tenant("Diagnostics Owner", "diagnostics-owner")
    user_id = store.create_user("diagnostics-owner@example.test", "Owner")
    store.add_membership(tenant_id, user_id, "owner")
    token = "diagnostics-owner-token-" + "O" * 32

    def unexpected_diagnostics(*_args, **_kwargs):
        pytest.fail("diagnostics must not run without explicit provider-use approval")

    store.create_api_token(token, tenant_id, user_id)
    monkeypatch.setattr(WebAgent, "diagnostics", unexpected_diagnostics)

    status, result = request_json(
        base,
        "/api/diagnostics",
        method="POST",
        token=token,
        payload={"test_model": True, "test_social": True},
    )
    assert status == 403
    assert "explicit owner approval" in result["error"]


def test_live_diagnostics_is_owner_only_even_with_explicit_approval(
    tenant_api, monkeypatch
):
    from api.omarai import WebAgent

    base, store = tenant_api
    tenant_id = store.create_tenant("Sales Member Diagnostics", "sales-member-diagnostics")
    user_id = store.create_user("sales-member@example.test", "Sales Member")
    store.add_membership(tenant_id, user_id, "sales_agent")
    token = "sales-member-diagnostics-token-" + "S" * 32

    def unexpected_diagnostics(*_args, **_kwargs):
        pytest.fail("non-owner diagnostics must be rejected before provider calls")

    store.create_api_token(token, tenant_id, user_id)
    monkeypatch.setattr(WebAgent, "diagnostics", unexpected_diagnostics)

    status, result = request_json(
        base,
        "/api/diagnostics",
        method="POST",
        token=token,
        payload={
            "test_model": True,
            "test_social": False,
            "allow_provider_usage": True,
        },
    )
    assert status == 403


def test_owner_can_run_diagnostics_only_after_explicit_approval(
    tenant_api, monkeypatch
):
    from api.omarai import WebAgent

    base, store = tenant_api
    tenant_id = store.create_tenant("Approved Diagnostics", "approved-diagnostics")
    user_id = store.create_user("approved-owner@example.test", "Owner")
    store.add_membership(tenant_id, user_id, "owner")
    token = "approved-diagnostics-token-" + "D" * 32
    store.create_api_token(token, tenant_id, user_id)
    observed = {}

    def fake_diagnostics(self, *, test_model=False, test_social=False):
        observed.update({"test_model": test_model, "test_social": test_social})
        return {"overall_status": "passed"}

    monkeypatch.setattr(WebAgent, "diagnostics", fake_diagnostics)
    status, result = request_json(
        base,
        "/api/diagnostics",
        method="POST",
        token=token,
        payload={
            "test_model": True,
            "test_social": False,
            "allow_provider_usage": True,
        },
    )
    assert status == 200
    assert result["overall_status"] == "passed"
    assert observed == {"test_model": True, "test_social": False}


def test_viewer_cannot_invoke_agent_research_or_model_calls(tenant_api, monkeypatch):
    from api.omarai import WebAgent

    base, store = tenant_api
    monkeypatch.setattr(Handler, "_rate_limit_ok", lambda self: True)
    tenant_id = store.create_tenant("Viewer Agent Block", "viewer-agent-block")
    user_id = store.create_user("viewer-agent@example.test", "Viewer")
    store.add_membership(tenant_id, user_id, "viewer")
    token = "viewer-agent-token-" + "W" * 32
    store.create_api_token(token, tenant_id, user_id)

    def unexpected_answer(*_args, **_kwargs):
        pytest.fail("viewer must be denied before agent/model execution")

    monkeypatch.setattr(WebAgent, "answer", unexpected_answer)
    status, result = request_json(
        base,
        "/api/agent",
        method="POST",
        token=token,
        payload={"question": "نفّذ بحثًا جديدًا"},
    )
    assert status == 403
    assert "viewer" in result["error"]


def test_agent_api_allowlists_and_forwards_the_hosted_smoke_budget_profile(
    tenant_api, monkeypatch
):
    from api.omarai import WebAgent

    base, store = tenant_api
    tenant_id = store.create_tenant("Smoke Profile Owner", "smoke-profile-owner")
    user_id = store.create_user("smoke-profile@example.test", "Smoke Profile Owner")
    store.add_membership(tenant_id, user_id, "sales_agent")
    token = "smoke-profile-token-" + "P" * 32
    store.create_api_token(token, tenant_id, user_id)
    observed = {}

    def fake_answer(self, question, history=None, mode="auto", *, budget_profile="default"):
        observed.update({
            "question": question,
            "history": history,
            "mode": mode,
            "budget_profile": budget_profile,
        })
        return {"answer": "test answer"}

    monkeypatch.setattr(WebAgent, "answer", fake_answer)
    status, result = request_json(
        base,
        "/api/agent",
        method="POST",
        token=token,
        payload={
            "question": "اختبار ميزانية القبول",
            "mode": "auto",
            "request_profile": "hosted_smoke",
        },
    )
    assert status == 200
    assert result["answer"] == "test answer"
    assert observed == {
        "question": "اختبار ميزانية القبول",
        "history": [],
        "mode": "auto",
        "budget_profile": "hosted_smoke",
    }

    status, error = request_json(
        base,
        "/api/agent",
        method="POST",
        token=token,
        payload={"question": "اختبار ملف غير مسموح", "request_profile": "unbounded"},
    )
    assert status == 400
    assert "request_profile" in error["error"]
    assert observed["budget_profile"] == "hosted_smoke"

    status, result = request_json(
        base,
        "/api/agent",
        method="POST",
        token=token,
        payload={"question": "اختبار التوافق مع الملف الافتراضي"},
    )
    assert status == 200
    assert result["answer"] == "test answer"
    assert observed["budget_profile"] == "default"


def test_product_profiles_and_discoveries_are_isolated_across_tenants(tenant_api, monkeypatch):
    """P0 regression: product profiles and discovery runs must never cross tenants.

    Client-supplied tenant_id must be ignored. Tenant A must not list, read, or
    start discovery against Tenant B's profile, even when the profile UUID is known.
    """
    from api.omarai import WebAgent

    base, store = tenant_api
    token_a = "profile-tenant-a-token-" + "A" * 24
    token_b = "profile-tenant-b-token-" + "B" * 24
    tenant_a = _tenant(store, "Profile Company A", "profiles-a@example.test", token_a)
    tenant_b = _tenant(store, "Profile Company B", "profiles-b@example.test", token_b)

    status, profile_a = request_json(
        base,
        "/api/product-profiles",
        method="POST",
        token=token_a,
        payload={
            "tenant_id": tenant_b,
            "product": {
                "name": "لوحة إنذار حريق A",
                "aliases": ["FACP-A"],
                "use_cases": ["حماية مباني"],
                "problems_solved": [],
            },
            "market": {
                "locations": ["Cairo"],
                "industries": [],
                "customer_types": [],
                "decision_roles": [],
                "exclusions": [],
            },
            "locale": "ar",
        },
    )
    assert status == 201
    assert profile_a["tenant_id"] == tenant_a
    assert profile_a["id"]

    status, profile_b = request_json(
        base,
        "/api/product-profiles",
        method="POST",
        token=token_b,
        payload={
            "tenant_id": tenant_a,
            "product": {
                "name": "لوحة إنذار حريق B",
                "aliases": ["FACP-B"],
                "use_cases": [],
                "problems_solved": [],
            },
            "market": {
                "locations": ["Riyadh"],
                "industries": [],
                "customer_types": [],
                "decision_roles": [],
                "exclusions": [],
            },
            "locale": "ar",
        },
    )
    assert status == 201
    assert profile_b["tenant_id"] == tenant_b

    status, listing_a = request_json(base, "/api/product-profiles", token=token_a)
    assert status == 200
    listed_ids_a = [row["id"] for row in listing_a["profiles"]]
    assert listed_ids_a == [profile_a["id"]]
    assert profile_b["id"] not in listed_ids_a

    status, listing_b = request_json(base, "/api/product-profiles", token=token_b)
    assert status == 200
    listed_ids_b = [row["id"] for row in listing_b["profiles"]]
    assert listed_ids_b == [profile_b["id"]]
    assert profile_a["id"] not in listed_ids_b

    def unexpected_answer(*_args, **_kwargs):
        pytest.fail("cross-tenant discovery must be rejected before agent execution")

    monkeypatch.setattr(WebAgent, "answer", unexpected_answer)

    # Tenant A must not start discovery using Tenant B's profile id.
    status, denied = request_json(
        base,
        "/api/discoveries",
        method="POST",
        token=token_a,
        payload={"profile_id": profile_b["id"]},
    )
    assert status in {403, 404}
    assert "error" in denied

    def fake_answer(
        self, question, history=None, mode="auto", *, budget_profile="default", buyer_queries=None
    ):
        return {
            "answer": "no qualified signals",
            "search_queries": buyer_queries or [],
            "search_report": {"lead_generation": {"status": "no_candidate_signals"}},
            "sources": [],
        }

    monkeypatch.setattr(WebAgent, "answer", fake_answer)
    status, run_b = request_json(
        base,
        "/api/discoveries",
        method="POST",
        token=token_b,
        payload={"profile_id": profile_b["id"]},
    )
    assert status == 201
    assert run_b["tenant_id"] == tenant_b
    assert run_b["profile_id"] == profile_b["id"]

    status, runs_a = request_json(base, "/api/discoveries", token=token_a)
    assert status == 200
    run_ids_a = [row["id"] for row in runs_a["runs"]]
    assert run_b["id"] not in run_ids_a

    status, foreign = request_json(
        base, f"/api/discoveries/{run_b['id']}", token=token_a
    )
    assert status == 404
