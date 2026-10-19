from __future__ import annotations

import sqlite3

import pytest

from agents.omarai import LeadStore
from scripts.sqlite_backup_restore import BackupError, backup_database, restore_database


def test_backup_and_restore_preserve_omarai_leads(tmp_path):
    source_path = tmp_path / "live.sqlite3"
    source = LeadStore(source_path)
    first, created_first = source.add(
        "بدور على شقة في التجمع وممكن معاينة",
        "https://example.com/posts/1",
        platform="manual",
        note="سجل اختبار أول",
    )
    second, created_second = source.add(
        "محتاج شقة للإيجار الشهر القادم",
        "https://example.com/posts/2",
        platform="manual",
        note="سجل اختبار ثان",
    )
    assert created_first and created_second
    source.update_status(first["id"], "qualified")

    snapshot_path = tmp_path / "backups" / "snapshot.sqlite3"
    backup_report = backup_database(source_path, snapshot_path)
    assert backup_report["result"] == "passed"
    assert backup_report["integrity_check"] == "ok"
    assert backup_report["lead_count"] == 2
    assert backup_report["overwrite"] is False

    restored_path = tmp_path / "restored" / "restored.sqlite3"
    restore_report = restore_database(snapshot_path, restored_path)
    assert restore_report["result"] == "passed"
    assert restore_report["integrity_check"] == "ok"
    assert restore_report["lead_count"] == 2

    restored = LeadStore(restored_path)
    original_rows = {row["id"]: row for row in source.list(limit=500)}
    restored_rows = {row["id"]: row for row in restored.list(limit=500)}
    assert restored_rows == original_rows
    assert restored_rows[first["id"]]["status"] == "qualified"
    assert second["id"] in restored_rows


def test_backup_never_overwrites_an_existing_destination(tmp_path):
    source_path = tmp_path / "source.sqlite3"
    LeadStore(source_path)
    destination = tmp_path / "keep-me.txt"
    destination.write_text("do not overwrite", encoding="utf-8")

    with pytest.raises(FileExistsError):
        backup_database(source_path, destination)

    assert destination.read_text(encoding="utf-8") == "do not overwrite"


def test_backup_rejects_non_omarai_sqlite_database_without_leaving_destination(tmp_path):
    source_path = tmp_path / "unrelated.sqlite3"
    with sqlite3.connect(source_path) as db:
        db.execute("CREATE TABLE unrelated (value TEXT)")

    destination = tmp_path / "should-not-exist.sqlite3"
    with pytest.raises(BackupError, match="not an Omarai leads database"):
        backup_database(source_path, destination)

    assert not destination.exists()


def test_backup_rejects_same_source_and_destination(tmp_path):
    source_path = tmp_path / "source.sqlite3"
    LeadStore(source_path)

    with pytest.raises(BackupError, match="different paths"):
        backup_database(source_path, source_path)


def test_restore_rejects_corrupt_backup_without_overwriting_source(tmp_path):
    backup_path = tmp_path / "corrupt.sqlite3"
    backup_path.write_bytes(b"not a sqlite database")
    destination = tmp_path / "restore.sqlite3"

    with pytest.raises(BackupError):
        restore_database(backup_path, destination)

    assert backup_path.read_bytes() == b"not a sqlite database"
    assert not destination.exists()
