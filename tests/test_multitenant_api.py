"""HTTP-level tenant authorization regression tests."""
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
def tenant_api(tmp_path, monkeypatch):
    monkeypatch.setenv("OMARAI_PUBLIC_DEPLOYMENT", "1")
    monkeypatch.delenv("OMARAI_ACCESS_TOKEN", raising=False)
    previous_store = Handler.store
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
    tenant_id = store.create_tenant("Read Only Company", "read-only-company")
    user_id = store.create_user("viewer@example.test", "Viewer")
    store.add_membership(tenant_id, user_id, "viewer")
    token = "viewer-token-" + "V" * 32
    store.create_api_token(token, tenant_id, user_id, label="viewer")

    status, listing = request_json(base, "/api/leads", token=token)
    assert status == 200
    assert listing["count"] == 0

    status, error = request_json(
        base,
        "/api/leads",
        method="POST",
        token=token,
        payload={
            "text": "Viewer must not write",
            "source_url": "https://example.test/viewer",
        },
    )
    assert status == 403
    assert "للقراءة فقط" in error["error"]



def test_api_revokes_only_the_authenticated_api_token(tenant_api):
    base, store = tenant_api
    tenant_id = store.create_tenant("Revocable Company", "revocable-company")
    user_id = store.create_user("revoker@example.test", "Token Owner")
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
