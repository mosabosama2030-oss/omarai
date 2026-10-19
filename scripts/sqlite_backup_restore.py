#!/usr/bin/env python3
"""Create and restore verified, non-overwriting snapshots of Omarai's SQLite lead DB."""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
from pathlib import Path
from typing import Any


class BackupError(RuntimeError):
    """Raised when a backup/restore operation cannot be proven safe."""


def _open_read_only(path: Path) -> sqlite3.Connection:
    """Open an existing SQLite database without accidentally creating a missing source."""
    try:
        return sqlite3.connect(f"{path.as_uri()}?mode=ro", uri=True, timeout=10)
    except (OSError, sqlite3.Error) as exc:
        raise BackupError(f"cannot open SQLite source: {type(exc).__name__}") from exc


def _validate_omarai_database(db: sqlite3.Connection) -> int:
    """Require a healthy SQLite file containing the Omarai leads table."""
    try:
        integrity_row = db.execute("PRAGMA integrity_check").fetchone()
        if not integrity_row or integrity_row[0] != "ok":
            raise BackupError("SQLite integrity_check did not return ok")
        table_row = db.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name='leads'"
        ).fetchone()
        if not table_row:
            raise BackupError("source is not an Omarai leads database")
        count_row = db.execute("SELECT COUNT(*) FROM leads").fetchone()
        if not count_row:
            raise BackupError("could not count leads in database")
        return int(count_row[0])
    except sqlite3.Error as exc:
        raise BackupError(f"SQLite validation failed: {type(exc).__name__}") from exc


def _create_destination_exclusively(path: Path) -> None:
    """Create a new destination without overwriting an existing file or following its symlink."""
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    os.close(descriptor)
    try:
        path.chmod(0o600)
    except OSError:
        # The exclusive-create mode remains the primary permission setting; do not
        # discard a completed backup solely because chmod is unavailable on a host.
        pass


def _copy_verified_database(source: str | Path, destination: str | Path) -> dict[str, Any]:
    source_path = Path(source).expanduser().resolve(strict=True)
    destination_path = Path(destination).expanduser().resolve(strict=False)

    if not source_path.is_file():
        raise BackupError("source must be an existing regular file")
    if source_path == destination_path:
        raise BackupError("source and destination must be different paths")
    if destination_path.exists():
        raise FileExistsError(f"destination already exists: {destination_path}")

    # Validate the source before creating anything at the destination.
    with _open_read_only(source_path) as source_db:
        source_count = _validate_omarai_database(source_db)
        _create_destination_exclusively(destination_path)
        try:
            with sqlite3.connect(destination_path, timeout=10) as destination_db:
                source_db.backup(destination_db)
                restored_count = _validate_omarai_database(destination_db)
                if restored_count != source_count:
                    raise BackupError(
                        "lead count changed during snapshot: "
                        f"source={source_count}, destination={restored_count}"
                    )
        except Exception:
            # Remove only the destination created by this operation; never touch source.
            try:
                destination_path.unlink(missing_ok=True)
            except OSError:
                pass
            raise

    return {
        "result": "passed",
        "source": str(source_path),
        "destination": str(destination_path),
        "integrity_check": "ok",
        "lead_count": source_count,
        "overwrite": False,
    }


def backup_database(source: str | Path, destination: str | Path) -> dict[str, Any]:
    """Create a consistent SQLite snapshot of a healthy Omarai leads database."""
    return _copy_verified_database(source, destination)


def restore_database(backup: str | Path, destination: str | Path) -> dict[str, Any]:
    """Restore a snapshot into a new destination; existing files are never overwritten."""
    return _copy_verified_database(backup, destination)


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Back up or restore an Omarai SQLite leads database. "
            "The destination must not already exist."
        )
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    backup_parser = subparsers.add_parser("backup", help="create a verified snapshot")
    backup_parser.add_argument("source", help="existing Omarai SQLite database path")
    backup_parser.add_argument("destination", help="new backup path; must not exist")
    restore_parser = subparsers.add_parser("restore", help="restore to a new database file")
    restore_parser.add_argument("source", help="existing verified backup path")
    restore_parser.add_argument("destination", help="new restore path; must not exist")
    args = parser.parse_args()

    try:
        if args.command == "backup":
            result = backup_database(args.source, args.destination)
        else:
            result = restore_database(args.source, args.destination)
    except (BackupError, FileExistsError, OSError, sqlite3.Error, ValueError) as exc:
        print(
            json.dumps(
                {"result": "failed", "error": str(exc)},
                ensure_ascii=False,
                indent=2,
            ),
            file=sys.stderr,
        )
        return 1

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
