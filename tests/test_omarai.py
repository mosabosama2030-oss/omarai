import csv
import sqlite3

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


def test_sqlite_backup_and_restore_preserve_lead_data(tmp_path):
    source_store = LeadStore(tmp_path / "source.sqlite3")
    first, _ = source_store.add(
        "بدور على شقة وممكن معاينة",
        "https://example.com/post/backup-1",
        platform="manual",
        note="حالة يجب أن تبقى بعد الاستعادة",
    )
    source_store.update_status(first["id"], "qualified")
    source_store.add(
        "عايز اعرف الاسعار",
        "https://example.com/post/backup-2",
        platform="manual",
    )

    backup_path = tmp_path / "backup.sqlite3"
    source = source_store.connect()
    backup = sqlite3.connect(backup_path)
    try:
        source.backup(backup)
    finally:
        backup.close()
        source.close()

    restore_path = tmp_path / "restored.sqlite3"
    backup = sqlite3.connect(backup_path)
    restored = sqlite3.connect(restore_path)
    try:
        backup.backup(restored)
        integrity = restored.execute("PRAGMA integrity_check").fetchone()[0]
    finally:
        restored.close()
        backup.close()

    restored_store = LeadStore(restore_path)
    assert integrity == "ok"
    assert restored_store.list() == source_store.list()
    assert len(restored_store.list()) == 2
    assert next(
        lead for lead in restored_store.list() if lead["id"] == first["id"]
    )["status"] == "qualified"


def test_sqlite_corrupt_backup_is_not_accepted_as_restored(tmp_path):
    corrupt_backup = tmp_path / "corrupt.sqlite3"
    corrupt_backup.write_bytes(b"this is not a valid SQLite database")

    with sqlite3.connect(corrupt_backup) as connection:
        with pytest.raises(sqlite3.DatabaseError):
            connection.execute("SELECT * FROM sqlite_master").fetchall()
