"""PostgreSQL integration tests for the Neon-backed LeadStore.

These tests run only when OMARAI_TEST_DATABASE_URL points at an isolated test database.
The CI workflow supplies an ephemeral PostgreSQL service; production credentials are never used.
"""
from __future__ import annotations

import os
import uuid

import pytest

from agents.omarai import LeadStore, _PostgresConnection, _qmark_to_psycopg


@pytest.fixture
def postgres_store():
    database_url = os.getenv("OMARAI_TEST_DATABASE_URL", "").strip()
    if not database_url:
        pytest.skip("OMARAI_TEST_DATABASE_URL is not configured")
    return LeadStore(database_url=database_url)


def _tenant_user(store: LeadStore, marker: str) -> tuple[str, str]:
    tenant_id = store.create_tenant(f"PostgreSQL test {marker}", f"pg-{marker}")
    user_id = store.create_user(f"{marker}@example.invalid", f"PostgreSQL {marker}")
    store.add_membership(tenant_id, user_id, "owner")
    return tenant_id, user_id


def test_postgres_leads_preserve_tenant_scoping_and_duplicate_semantics(postgres_store):
    marker = uuid.uuid4().hex
    tenant_a, _ = _tenant_user(postgres_store, f"a-{marker}")
    tenant_b, _ = _tenant_user(postgres_store, f"b-{marker}")
    text = f"نبحث عن مورد لتجهيزات اختبار PostgreSQL {marker}"
    source_url = f"https://example.com/postgres/{marker}"

    lead_a, created_a = postgres_store.add(text, source_url, tenant_id=tenant_a)
    lead_b, created_b = postgres_store.add(text, source_url, tenant_id=tenant_b)

    assert created_a is True
    assert created_b is True
    assert lead_a["id"] != lead_b["id"]
    assert [row["id"] for row in postgres_store.list(tenant_id=tenant_a)] == [lead_a["id"]]
    assert [row["id"] for row in postgres_store.list(tenant_id=tenant_b)] == [lead_b["id"]]

    duplicate, created_again = postgres_store.add(
        text, source_url, tenant_id=tenant_a
    )
    assert created_again is False
    assert duplicate["id"] == lead_a["id"]

    assert postgres_store.update_status(
        lead_a["id"], "qualified", tenant_id=tenant_b
    ) is None
    updated = postgres_store.update_status(
        lead_a["id"], "qualified", tenant_id=tenant_a
    )
    assert updated["status"] == "qualified"
    assert postgres_store.list("qualified", tenant_id=tenant_a)[0]["id"] == lead_a["id"]
    assert postgres_store.list(tenant_id=tenant_b)[0]["status"] == "new"


def test_postgres_tokens_sessions_and_reusable_workspace_records(postgres_store):
    marker = uuid.uuid4().hex
    tenant_id, user_id = _tenant_user(postgres_store, marker)
    token = f"postgres-test-{marker}-" + ("T" * 40)

    postgres_store.create_api_token(token, tenant_id, user_id, label="integration")
    principal = postgres_store.resolve_api_token(token)
    assert principal == {"tenant_id": tenant_id, "user_id": user_id, "role": "owner"}

    created_session = postgres_store.create_web_session(token)
    assert created_session is not None
    session_id, session_principal = created_session
    assert session_principal == principal
    assert postgres_store.resolve_web_session(session_id) == principal
    assert postgres_store.revoke_web_session(session_id) is True
    assert postgres_store.resolve_web_session(session_id) is None

    profile_input = {
        "product": {"name": f"PostgreSQL Widget {marker}", "aliases": ["Widget"]},
        "market": {"locations": ["Cairo"], "industries": ["Testing"]},
    }
    profile = postgres_store.save_product_profile(profile_input, tenant_id=tenant_id)
    assert profile["name"] == profile_input["product"]["name"]
    assert postgres_store.get_product_profile(
        profile["id"], tenant_id=tenant_id
    )["profile"] == profile_input
    assert postgres_store.list_product_profiles(tenant_id=tenant_id)[0]["id"] == profile["id"]

    run = postgres_store.save_discovery_run(
        profile["id"],
        {
            "answer": "تم العثور على طلب توريد معلن.",
            "kind": "lead_discovery",
            "search_queries": ["نبحث عن مورد"],
            "sources": [{
                "title": "طلب مورد تجريبي",
                "url": f"https://example.com/demand/{marker}",
                "snippet": "نبحث عن مورد لتوريد المنتج",
                "platform": "web",
                "lead_qualification": "public_demand_signal",
                "lead_intent_evidence": {
                    "phrase": "نبحث عن مورد",
                    "basis": "source_text",
                    "signal_type": "direct_purchase_request",
                    "product_fit": "unassessed",
                },
            }],
            "search_report": {"search_outcome": "results_found"},
        },
        tenant_id=tenant_id,
    )
    assert run["tenant_id"] == tenant_id
    assert run["sources"][0]["lead_qualification"] == "public_demand_signal"
    assert postgres_store.get_discovery_run(
        run["id"], tenant_id=tenant_id
    )["id"] == run["id"]
    assert postgres_store.list_discovery_runs(tenant_id=tenant_id)[0]["id"] == run["id"]

    saved_signal, created = postgres_store.save_discovery_signal(
        run["id"], 0, tenant_id=tenant_id
    )
    assert created is True
    assert saved_signal["tenant_id"] == tenant_id
    assert postgres_store.revoke_api_token(
        token, tenant_id=tenant_id, user_id=user_id
    ) is True
    assert postgres_store.resolve_api_token(token) is None


def test_postgres_placeholder_translation_skips_quoted_question_marks():
    sql = "SELECT ?, '?' AS literal, \"?\" AS identifier, ? AS last_value"
    assert _qmark_to_psycopg(sql) == (
        "SELECT %s, '?' AS literal, \"?\" AS identifier, %s AS last_value"
    )


def test_postgres_connection_adapter_converts_insert_or_ignore():
    class FakeConnection:
        statement = None
        params = None

        def execute(self, statement, params):
            self.statement = statement
            self.params = params
            return "cursor"

    connection = FakeConnection()
    adapter = _PostgresConnection(connection)

    result = adapter.execute(
        "INSERT OR IGNORE INTO leads (id, note) VALUES (?, '?')",
        ("lead-1",),
    )

    assert result == "cursor"
    assert connection.statement == (
        "INSERT INTO leads (id, note) VALUES (%s, '?') ON CONFLICT DO NOTHING"
    )
    assert connection.params == ("lead-1",)


def test_postgres_database_url_rejects_unsupported_scheme():
    with pytest.raises(ValueError, match="PostgreSQL URL scheme"):
        LeadStore(database_url="mysql://user:pass@example.com/db")


def test_postgres_database_url_cannot_be_combined_with_sqlite_path(tmp_path):
    with pytest.raises(ValueError, match="either database_url or a SQLite path"):
        LeadStore(tmp_path / "local.sqlite3", database_url="postgresql://user:pass@example.com/db")

def test_postgres_records_survive_a_new_python_process(postgres_store):
    import json
    import subprocess
    import sys
    from pathlib import Path

    marker = uuid.uuid4().hex
    tenant_id, _user_id = _tenant_user(postgres_store, f"restart-{marker}")
    lead, created = postgres_store.add(
        f"نحتاج موردًا لنظام إنذار حريق {marker}",
        f"https://example.com/postgres/restart/{marker}",
        tenant_id=tenant_id,
    )
    assert created is True
    profile = postgres_store.save_product_profile(
        {
            "product": {"name": f"PostgreSQL restart {marker}", "aliases": ["FACP"]},
            "market": {"locations": ["Cairo"], "industries": ["Manufacturing"]},
        },
        tenant_id=tenant_id,
    )
    run = postgres_store.save_discovery_run(
        profile["id"],
        {
            "answer": "تم حفظ عملية اكتشاف اختبارية.",
            "kind": "lead_discovery",
            "search_queries": ["نحتاج موردًا لنظام إنذار حريق"],
            "sources": [{
                "title": "طلب توريد اختباري",
                "url": f"https://example.com/postgres/source/{marker}",
                "snippet": "نحتاج موردًا لنظام إنذار حريق",
                "lead_qualification": "public_demand_signal",
                "lead_intent_evidence": {
                    "phrase": "نحتاج موردًا",
                    "basis": "source_text",
                    "signal_type": "direct_purchase_request",
                },
            }],
            "search_report": {"search_outcome": "results_found"},
        },
        tenant_id=tenant_id,
    )

    child_code = """
import json
import os
import sys
from agents.omarai import LeadStore
store = LeadStore(database_url=os.environ["OMARAI_TEST_DATABASE_URL"])
tenant_id = sys.argv[1]
print(json.dumps({
    "lead_ids": [row["id"] for row in store.list(tenant_id=tenant_id)],
    "profile_ids": [row["id"] for row in store.list_product_profiles(tenant_id=tenant_id)],
    "run_ids": [row["id"] for row in store.list_discovery_runs(tenant_id=tenant_id)],
}))
"""
    repository_root = Path(__file__).resolve().parents[1]
    completed = subprocess.run(
        [sys.executable, "-c", child_code, tenant_id],
        cwd=repository_root,
        env=os.environ.copy(),
        check=True,
        capture_output=True,
        text=True,
    )
    persisted = json.loads(completed.stdout)

    assert persisted["lead_ids"] == [lead["id"]]
    assert persisted["profile_ids"] == [profile["id"]]
    assert persisted["run_ids"] == [run["id"]]
