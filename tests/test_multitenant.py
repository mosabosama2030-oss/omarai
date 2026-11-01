"""Tenant isolation, migration, and scoped export regression tests."""
from __future__ import annotations

import csv
import hashlib
import sqlite3

import pytest

from agents.omarai import DEFAULT_TENANT_ID, LeadStore, normalize


def _tenant_member(store: LeadStore, name: str, email: str, token: str):
    tenant_id = store.create_tenant(name, name.casefold())
    user_id = store.create_user(email, name + " User")
    store.add_membership(tenant_id, user_id, "sales_agent")
    store.create_api_token(token, tenant_id, user_id, label=name)
    return tenant_id, user_id


def test_tenant_scoped_fingerprints_reads_updates_and_exports(tmp_path):
    store = LeadStore(tmp_path / "multi.sqlite3")
    tenant_a, _, = _tenant_member(
        store, "Company A", "a@example.test", "A" * 40
    )
    tenant_b, _, = _tenant_member(
        store, "Company B", "b@example.test", "B" * 40
    )

    payload = ("Buyer asks to purchase a product", "https://example.test/post/1")
    lead_a, created_a = store.add(
        *payload, tenant_id=tenant_a
    )
    lead_b, created_b = store.add(
        *payload, tenant_id=tenant_b
    )

    assert created_a is True
    assert created_b is True
    assert lead_a["id"] != lead_b["id"]
    assert lead_a["tenant_id"] == tenant_a
    assert lead_b["tenant_id"] == tenant_b
    assert [row["id"] for row in store.list(tenant_id=tenant_a)] == [lead_a["id"]]
    assert [row["id"] for row in store.list(tenant_id=tenant_b)] == [lead_b["id"]]

    assert store.update_status(
        lead_b["id"], "qualified", tenant_id=tenant_a
    ) is None
    updated_b = store.update_status(
        lead_b["id"], "qualified", tenant_id=tenant_b
    )
    assert updated_b is not None
    assert updated_b["status"] == "qualified"

    export_path = tmp_path / "company-a.csv"
    assert store.export_csv(export_path, tenant_id=tenant_a) == 1
    with export_path.open(newline="", encoding="utf-8-sig") as stream:
        rows = list(csv.DictReader(stream))
    assert len(rows) == 1
    assert rows[0]["tenant_id"] == tenant_a
    assert rows[0]["id"] == lead_a["id"]


def test_api_tokens_resolve_only_active_tenant_memberships(tmp_path):
    store = LeadStore(tmp_path / "tokens.sqlite3")
    tenant_id, user_id = _tenant_member(
        store, "Company", "owner@example.test", "C" * 40
    )

    principal = store.resolve_api_token("C" * 40)
    assert principal == {
        "tenant_id": tenant_id,
        "user_id": user_id,
        "role": "sales_agent",
    }
    assert store.resolve_api_token("X" * 40) is None

    with store.connect() as db:
        db.execute(
            "UPDATE tenant_memberships SET active=0 WHERE tenant_id=? AND user_id=?",
            (tenant_id, user_id),
        )
    assert store.resolve_api_token("C" * 40) is None


def test_legacy_single_company_database_migrates_without_losing_leads(tmp_path):
    path = tmp_path / "legacy.sqlite3"
    legacy_text = "Old lead"
    legacy_url = "https://example.test/legacy"
    legacy_fingerprint = hashlib.sha256(
        (legacy_url.rstrip("/") + "\n" + normalize(legacy_text)).encode()
    ).hexdigest()
    with sqlite3.connect(path) as db:
        db.execute(
            """CREATE TABLE leads (
                id TEXT PRIMARY KEY,
                fingerprint TEXT UNIQUE NOT NULL,
                text TEXT NOT NULL,
                source_url TEXT NOT NULL,
                platform TEXT NOT NULL,
                observed_at TEXT NOT NULL,
                assessment TEXT NOT NULL,
                status TEXT NOT NULL,
                note TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )"""
        )
        db.execute(
            """INSERT INTO leads VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                "legacy-lead", legacy_fingerprint, legacy_text,
                legacy_url, "manual", "2026-10-30T00:00:00Z",
                '{"score": 0}', "new", "", "2026-10-30T00:00:00Z",
                "2026-10-30T00:00:00Z",
            ),
        )

    store = LeadStore(path)
    leads = store.list(tenant_id=DEFAULT_TENANT_ID)
    assert len(leads) == 1
    assert leads[0]["id"] == "legacy-lead"
    assert leads[0]["tenant_id"] == DEFAULT_TENANT_ID

    duplicate, created = store.add(
        "Old lead", "https://example.test/legacy", tenant_id=DEFAULT_TENANT_ID
    )
    assert created is False
    assert duplicate["id"] == "legacy-lead"

    with store.connect() as db:
        columns = {row["name"] for row in db.execute("PRAGMA table_info(leads)")}
        unique_indexes = [
            row["name"] for row in db.execute("PRAGMA index_list(leads)")
            if row["unique"]
        ]
        unique_columns = [
            [
                item["name"]
                for item in db.execute(f"PRAGMA index_info('{index_name}')")
            ]
            for index_name in unique_indexes
        ]
    assert "tenant_id" in columns
    assert ["fingerprint"] not in unique_columns
    assert ["tenant_id", "fingerprint"] in unique_columns



def test_legacy_migration_rolls_back_and_keeps_original_table_on_copy_error(tmp_path):
    path = tmp_path / "incomplete-legacy.sqlite3"
    with sqlite3.connect(path) as db:
        db.execute(
            "CREATE TABLE leads (id TEXT PRIMARY KEY, fingerprint TEXT UNIQUE NOT NULL, text TEXT NOT NULL)"
        )
        db.execute(
            "INSERT INTO leads (id, fingerprint, text) VALUES (?, ?, ?)",
            ("legacy-1", "fingerprint-1", "preserve me"),
        )

    import pytest

    with pytest.raises(sqlite3.OperationalError):
        LeadStore(path)

    with sqlite3.connect(path) as db:
        tables = {
            row[0]
            for row in db.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            )
        }
        original = db.execute(
            "SELECT id, fingerprint, text FROM leads"
        ).fetchone()
    assert "leads" in tables
    assert "leads_legacy_migration" not in tables
    assert original == ("legacy-1", "fingerprint-1", "preserve me")


def test_api_token_expiry_is_normalized_to_utc(tmp_path):
    store = LeadStore(tmp_path / "token-expiry.sqlite3")
    tenant_id, user_id = _tenant_member(
        store, "Expiry Company", "expiry@example.test", "E" * 40
    )
    token = "F" * 40
    store.create_api_token(
        token,
        tenant_id,
        user_id,
        expires_at="2099-01-01T03:00:00+03:00",
    )
    with store.connect() as db:
        row = db.execute(
            "SELECT expires_at FROM api_tokens WHERE token_hash=?",
            (store._token_hash(token),),
        ).fetchone()
    assert row["expires_at"] == "2099-01-01T00:00:00Z"
    assert store.resolve_api_token(token) is not None

    # Expired tokens must stop resolving even when their membership stays active.
    with store.connect() as db:
        db.execute(
            "UPDATE api_tokens SET expires_at=? WHERE token_hash=?",
            ("2000-01-01T00:00:00Z", store._token_hash(token)),
        )
    assert store.resolve_api_token(token) is None

    utc_token = "J" * 40
    store.create_api_token(
        utc_token, tenant_id, user_id, expires_at="2099-01-01T00:00:00Z"
    )
    assert store.resolve_api_token(utc_token) is not None


def test_api_token_expiry_rejects_naive_malformed_and_past_values(tmp_path):
    store = LeadStore(tmp_path / "invalid-token-expiry.sqlite3")
    tenant_id, user_id = _tenant_member(
        store, "Expiry Validation Company", "expiry-validation@example.test", "G" * 40
    )
    invalid_values = (
        "2099-01-01T00:00:00",
        "not-a-timestamp",
        "2000-01-01T00:00:00Z",
        "",
    )
    for index, expiry in enumerate(invalid_values):
        with pytest.raises(ValueError, match="expires_at"):
            store.create_api_token(
                ("H" * 39) + str(index),
                tenant_id,
                user_id,
                expires_at=expiry,
            )



def test_api_token_revocation_is_scoped_to_the_owning_user_and_tenant(tmp_path):
    store = LeadStore(tmp_path / "revoke-token.sqlite3")
    tenant_id, user_id = _tenant_member(
        store, "Revocation Company", "owner@example.test", "K" * 40
    )
    other_tenant_id, other_user_id = _tenant_member(
        store, "Other Revocation Company", "other@example.test", "L" * 40
    )
    token = "M" * 40
    store.create_api_token(token, tenant_id, user_id)

    assert store.resolve_api_token(token)["tenant_id"] == tenant_id
    assert store.revoke_api_token(
        token, tenant_id=other_tenant_id, user_id=other_user_id
    ) is False
    assert store.resolve_api_token(token)["tenant_id"] == tenant_id
    assert store.revoke_api_token(
        token, tenant_id=tenant_id, user_id=other_user_id
    ) is False
    assert store.resolve_api_token(token)["tenant_id"] == tenant_id

    assert store.revoke_api_token(
        token, tenant_id=tenant_id, user_id=user_id
    ) is True
    assert store.resolve_api_token(token) is None
    assert store.revoke_api_token(
        token, tenant_id=tenant_id, user_id=user_id
    ) is False

def test_store_connections_are_closed_after_success_and_rollback(tmp_path, monkeypatch):
    store = LeadStore(tmp_path / "connection-lifecycle.sqlite3")
    real_connect = sqlite3.connect
    opened = []

    def tracked_connect(*args, **kwargs):
        connection = real_connect(*args, **kwargs)
        opened.append(connection)
        return connection

    monkeypatch.setattr(sqlite3, "connect", tracked_connect)

    assert store.list(tenant_id=DEFAULT_TENANT_ID) == []
    assert len(opened) == 1
    with pytest.raises(sqlite3.ProgrammingError, match="closed"):
        opened[0].execute("SELECT 1")

    with pytest.raises(RuntimeError, match="force rollback"), store.connect() as db:
        db.execute(
            "INSERT INTO tenants (id, name, slug, active, created_at) "
            "VALUES (?, ?, ?, 1, ?)",
            ("tenant_rollback_test", "Rollback", "rollback-test", "2026-11-01T00:00:00Z"),
        )
        raise RuntimeError("force rollback")

    assert len(opened) == 2
    with pytest.raises(sqlite3.ProgrammingError, match="closed"):
        opened[1].execute("SELECT 1")

    with store.connect() as db:
        assert db.execute(
            "SELECT 1 FROM tenants WHERE id=?",
            ("tenant_rollback_test",),
        ).fetchone() is None

def test_browser_sessions_are_opaque_expiring_and_bound_to_api_token(tmp_path):
    store = LeadStore(tmp_path / "browser-session.sqlite3")
    tenant_id = store.create_tenant("Session Company", "session-company")
    user_id = store.create_user("session@example.test", "Session User")
    store.add_membership(tenant_id, user_id, "sales_agent")
    api_token = "session-api-token-" + "S" * 40
    store.create_api_token(api_token, tenant_id, user_id, label="browser")
    created = store.create_web_session(api_token)
    assert created is not None
    session_id, principal = created

    assert session_id != api_token
    assert principal == {
        "tenant_id": tenant_id,
        "user_id": user_id,
        "role": "sales_agent",
    }
    assert store.resolve_web_session(session_id) == principal

    with store.connect() as db:
        stored = db.execute(
            "SELECT session_hash, credential_hash FROM web_sessions"
        ).fetchone()
    assert stored["session_hash"] == store._token_hash(session_id)
    assert stored["credential_hash"] == store._token_hash(api_token)
    assert session_id not in stored["session_hash"]
    assert api_token not in stored["credential_hash"]

    assert store.revoke_api_token(
        api_token, tenant_id=tenant_id, user_id=user_id
    ) is True
    assert store.resolve_web_session(session_id) is None


def test_browser_session_expiry_and_explicit_logout_are_enforced(tmp_path):
    store = LeadStore(tmp_path / "browser-session-expiry.sqlite3")
    shared_token = "shared-browser-session-token-" + "X" * 32
    session = store.create_web_session(shared_token, shared_token=shared_token)
    assert session is not None
    session_id, principal = session
    assert principal["role"] == "owner"
    assert store.resolve_web_session(session_id, shared_token=shared_token) == principal

    with store.connect() as db:
        db.execute(
            "UPDATE web_sessions SET expires_at=? WHERE session_hash=?",
            ("2000-01-01T00:00:00Z", store._token_hash(session_id)),
        )
    assert store.resolve_web_session(session_id, shared_token=shared_token) is None

    fresh = store.create_web_session(shared_token, shared_token=shared_token)
    assert fresh is not None
    fresh_id, fresh_principal = fresh
    assert store.revoke_web_session(fresh_id) is True
    assert store.resolve_web_session(fresh_id, shared_token=shared_token) is None
    assert fresh_principal["role"] == "owner"


def test_browser_session_invalidates_when_shared_access_token_rotates(tmp_path):
    store = LeadStore(tmp_path / "browser-session-rotation.sqlite3")
    original = "original-shared-token-" + "O" * 32
    replacement = "replacement-shared-token-" + "R" * 32
    session = store.create_web_session(original, shared_token=original)
    assert session is not None
    session_id, _principal = session

    assert store.resolve_web_session(session_id, shared_token=original) is not None
    assert store.resolve_web_session(session_id, shared_token=replacement) is None

def test_new_browser_session_prunes_expired_and_revoked_session_rows(tmp_path):
    store = LeadStore(tmp_path / "session-cleanup.sqlite3")
    token = "session-cleanup-test-token-123456789012345"
    expired_session, _ = store.create_web_session(token, shared_token=token)
    revoked_session, _ = store.create_web_session(token, shared_token=token)
    assert store.revoke_web_session(revoked_session)

    expired_hash = store._token_hash(expired_session)
    revoked_hash = store._token_hash(revoked_session)
    with store.connect() as db:
        db.execute(
            "UPDATE web_sessions SET expires_at=? WHERE session_hash=?",
            ("2000-01-01T00:00:00Z", expired_hash),
        )

    active_session, _ = store.create_web_session(token, shared_token=token)
    active_hash = store._token_hash(active_session)
    with store.connect() as db:
        retained_hashes = {
            row["session_hash"]
            for row in db.execute("SELECT session_hash FROM web_sessions")
        }

    assert expired_hash not in retained_hashes
    assert revoked_hash not in retained_hashes
    assert active_hash in retained_hashes

