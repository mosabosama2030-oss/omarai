"""Tenant isolation, migration, and scoped export regression tests."""
from __future__ import annotations

import csv
import hashlib
import sqlite3

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
