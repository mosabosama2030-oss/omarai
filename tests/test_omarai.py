import csv

import pytest

from agents.omarai import LeadStore, analyze, normalize


def test_arabic_normalization():
    assert normalize("إيجارٌ ـ شقة") == normalize("ايجار شقة")

def test_high_intent_with_next_step():
    result=analyze("بدور على شقة وممكن معاينة")
    assert result["label"]=="high_intent"
    assert result["score"]>=55

def test_non_buyer_override():
    result=analyze("مش عايز اشتري، عايز ابيع شقة")
    assert result["label"]=="not_buyer_signal"
    assert result["score"]==0

def test_empty_text_rejected():
    with pytest.raises(ValueError):
        analyze(" ")

def test_url_required_and_validated(tmp_path):
    store=LeadStore(tmp_path/"db.sqlite3")
    with pytest.raises(ValueError):
        store.add("بدور على شقة","","manual")
    with pytest.raises(ValueError):
        store.add("بدور على شقة","file:///tmp/private","manual")

def test_duplicate_is_idempotent(tmp_path):
    store=LeadStore(tmp_path/"db.sqlite3")
    one,created1=store.add("بدور على شقة","https://example.com/post/1","facebook")
    two,created2=store.add("بدور على شقة","https://example.com/post/1","facebook")
    assert created1 is True and created2 is False
    assert one["id"]==two["id"]
    assert len(store.list())==1

def test_status_updates_are_explicit(tmp_path):
    store=LeadStore(tmp_path/"db.sqlite3")
    lead,_=store.add("بدور على شقة","https://example.com/p","manual")
    updated=store.update_status(lead["id"],"qualified")
    assert updated["status"]=="qualified"
    with pytest.raises(ValueError):
        store.update_status(lead["id"],"magic")

def test_csv_requires_columns(tmp_path):
    bad=tmp_path/"bad.csv"
    bad.write_text("foo,bar\na,b\n",encoding="utf-8")
    store=LeadStore(tmp_path/"db.sqlite3")
    with pytest.raises(ValueError):
        store.import_csv(bad)

def test_csv_export_neutralizes_spreadsheet_formula_injection(tmp_path):
    store = LeadStore(tmp_path / "db.sqlite3")
    store.add(
        '=HYPERLINK("https://evil.example","click")',
        "https://example.com/post/1",
        platform="manual",
        note="  +SUM(1,1)",
    )
    store.add(
        "\u00a0\ufeff=1+1",
        "https://example.com/post/2",
        platform="manual",
        note="\u00a0\ufeff=SUM(1,1)",
    )
    destination = tmp_path / "export.csv"
    assert store.export_csv(destination) == 2
    raw_csv = destination.read_text(encoding="utf-8-sig")
    assert '"\t=HYPERLINK(' in raw_csv
    assert '"\t  +SUM' in raw_csv

    with destination.open(newline="", encoding="utf-8-sig") as stream:
        rows = list(csv.DictReader(stream))

    row1 = next(row for row in rows if row["source_url"] == "https://example.com/post/1")
    row2 = next(row for row in rows if row["source_url"] == "https://example.com/post/2")
    assert row1["text"].startswith("\t=")
    assert row1["note"].startswith("\t  +")
    assert row2["text"].startswith("\t\ufeff=")
    assert row2["note"].startswith("\t\u00a0\ufeff=")

def test_legacy_leads_migrate_into_the_initial_company_without_data_loss(tmp_path):
    import hashlib
    import json
    import sqlite3

    database = tmp_path / "legacy.sqlite3"
    now = "2026-10-31T00:00:00Z"
    with sqlite3.connect(database) as db:
        db.execute(
            """CREATE TABLE leads (
                id TEXT PRIMARY KEY, fingerprint TEXT UNIQUE NOT NULL, text TEXT NOT NULL,
                source_url TEXT NOT NULL, platform TEXT NOT NULL, observed_at TEXT NOT NULL,
                assessment TEXT NOT NULL, status TEXT NOT NULL, note TEXT NOT NULL,
                created_at TEXT NOT NULL, updated_at TEXT NOT NULL
            )"""
        )
        db.execute(
            "CREATE INDEX leads_status_idx ON leads(status, created_at DESC)"
        )
        db.execute(
            """INSERT INTO leads VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                "legacy-id", hashlib.sha256((
                    "https://example.com/legacy\n" + normalize("بدور على شقة")
                ).encode()).hexdigest(), "بدور على شقة",
                "https://example.com/legacy", "manual", now,
                json.dumps({"score": 1}), "new", "", now, now,
            ),
        )

    store = LeadStore(database)
    rows = store.list()
    assert len(rows) == 1
    assert rows[0]["id"] == "legacy-id"
    assert rows[0]["tenant_id"] == "default"
    assert rows[0]["source_url"] == "https://example.com/legacy"

    store.create_company("company-b", "شركة ب")
    duplicate_in_other_company, created = store.add(
        "بدور على شقة",
        "https://example.com/legacy",
        tenant_id="company-b",
    )
    assert created is True
    assert duplicate_in_other_company["tenant_id"] == "company-b"
    assert duplicate_in_other_company["id"] != "legacy-id"

    duplicate_in_default, created_again = store.add(
        "بدور على شقة",
        "https://example.com/legacy",
        tenant_id="default",
    )
    assert created_again is False
    assert duplicate_in_default["id"] == "legacy-id"


def test_lead_store_reads_updates_and_exports_are_company_scoped(tmp_path):
    store = LeadStore(tmp_path / "tenant-scoped.sqlite3")
    store.create_company("company-b", "شركة ب")
    lead_a, created_a = store.add(
        "مطلوب شراء جهاز", "https://example.com/request",
        tenant_id="default",
    )
    lead_b, created_b = store.add(
        "مطلوب شراء جهاز", "https://example.com/request",
        tenant_id="company-b",
    )
    assert created_a is True and created_b is True
    assert lead_a["id"] != lead_b["id"]
    assert [row["id"] for row in store.list(tenant_id="default")] == [lead_a["id"]]
    assert [row["id"] for row in store.list(tenant_id="company-b")] == [lead_b["id"]]

    assert store.update_status(
        lead_b["id"], "qualified", tenant_id="default"
    ) is None
    updated = store.update_status(
        lead_b["id"], "qualified", tenant_id="company-b"
    )
    assert updated is not None and updated["status"] == "qualified"

    exported = tmp_path / "company-a.csv"
    assert store.export_csv(exported, tenant_id="default") == 1
    csv_text = exported.read_text(encoding="utf-8-sig")
    assert "company-b" not in csv_text
    assert lead_a["id"] in csv_text
    assert lead_b["id"] not in csv_text

    export_text_b = store.export_csv_text(tenant_id="company-b")
    assert lead_b["id"] in export_text_b
    assert lead_a["id"] not in export_text_b


def test_membership_resolution_requires_active_company_user_and_membership(tmp_path):
    store = LeadStore(tmp_path / "memberships.sqlite3")
    store.create_company("company-b", "شركة ب")
    store.create_user("user-b", email="user-b@example.test", display_name="موظف ب")
    store.add_membership("company-b", "user-b", role="sales_agent")

    assert store.resolve_membership("user-b", "company-b")["role"] == "sales_agent"
    assert store.resolve_membership("user-b", "default") is None
    assert store.resolve_membership("operator", "company-b") is None
    assert store.resolve_membership("unknown-user", "company-b") is None
