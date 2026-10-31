"""Explainable Arabic lead-intent analysis and local SQLite storage."""
from __future__ import annotations

import csv
import hashlib
from io import StringIO
import json
import re
import sqlite3
import unicodedata
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import urlparse
from typing import ClassVar

MAX_TEXT = 12000
_TRANSLATION = str.maketrans({"أ":"ا","إ":"ا","آ":"ا","ٱ":"ا","ى":"ي","ئ":"ي","ؤ":"و","ـ":""})
SIGNALS = {
    "high": (35, ("عايز اشتري", "عاوز اشتري", "بدور على شقة", "بدور على عقار", "مطلوب شقة", "عايز وحدة", "محتاج اشتري")),
    "next_step": (20, ("ممكن معاينة", "عايز اعاين", "عاوز اعاين", "ابعت التفاصيل", "ابعت اللوكيشن", "ميعاد للمعاينة")),
    "budget": (15, ("السعر كام", "مقدم كام", "ميزانيتي", "معايا مقدم", "تقسيط", "على اقساط", "في حدود")),
    "explore": (10, ("بدور على", "فيه شقق", "ايه المتاح", "عايز اعرف الاسعار")),
}
NOT_BUYER = ("مش عايز اشتري", "مش عاوز اشتري", "عايز ابيع", "عاوز ابيع", "عندي شقة للبيع", "انا وسيط", "انا سمسار", "عايز ايجار", "للايجار")

def normalize(text: str) -> str:
    value = unicodedata.normalize("NFKC", str(text)).translate(_TRANSLATION)
    value = "".join(c for c in value if not unicodedata.category(c).startswith("M"))
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", value.casefold())).strip()

def now_utc() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")

def _csv_safe_cell(value: object) -> str:
    """Prefix spreadsheet formulas even when hidden whitespace/control chars precede them."""
    text = "" if value is None else str(value)
    if not text:
        return text
    index = 0
    while index < len(text) and (
        text[index].isspace()
        or unicodedata.category(text[index]) in {"Cc", "Cf"}
    ):
        index += 1
    first_non_format = text[index:index + 1]
    formula_prefixes = {"=", "+", "-", "@", "＝", "＋", "－", "＠"}
    if text[0] in "\t\r\n" or first_non_format in formula_prefixes:
        # OWASP notes that a tab inside the quoted CSV field is more resilient
        # in Excel than an apostrophe, although no CSV mitigation is universal.
        return "\t" + text
    return text

def analyze(text: str, product_terms=(), location_terms=()) -> dict:
    if not isinstance(text, str) or not text.strip():
        raise ValueError("text must not be empty")
    if len(text) > MAX_TEXT:
        raise ValueError(f"text must be at most {MAX_TEXT} characters")
    body = normalize(text)
    excluded = [p for p in NOT_BUYER if normalize(p) in body]
    if excluded:
        return {"score": 0, "label": "not_buyer_signal", "summary": "قد لا تكون إشارة شراء مباشرة؛ راجع النص يدويًا.", "matched_signals": [{"phrase": p, "category": "exclusion", "points": 0} for p in excluded], "warnings": ["تصنيف أولي وليس حكمًا نهائيًا."]}
    matches = []
    for category, (points, phrases) in SIGNALS.items():
        found = next((p for p in phrases if normalize(p) in body), None)
        if found:
            matches.append({"phrase": found, "category": category, "points": points})
    for category, terms in (("product_context", product_terms), ("location_context", location_terms)):
        found = next((normalize(t) for t in terms if isinstance(t, str) and normalize(t) and normalize(t) in body), None)
        if found:
            matches.append({"phrase": found, "category": category, "points": 10})
    score = min(100, sum(x["points"] for x in matches))
    label = "high_intent" if score >= 55 and any(x["category"] == "high" for x in matches) else "medium_intent" if score >= 40 else "early_research" if score >= 20 else "unclear"
    return {"score": score, "label": label, "summary": {"high_intent":"إشارة قوية نسبيًا وفق قواعد بسيطة وتحتاج مراجعة بشرية.","medium_intent":"مؤشرات اهتمام تستحق التأهيل والتحقق.","early_research":"اهتمام مبكر؛ ليس عميلًا مؤهلًا بعد.","unclear":"لا توجد مؤشرات كافية."}[label], "matched_signals": matches, "warnings": ["الدرجة ليست احتمالًا إحصائيًا للشراء.", "لا تثبت هوية الكاتب أو قدرته على الدفع أو نيته.", "استخدم مصادر عامة ومسموحًا بمعالجتها فقط."]}

def validate_url(url: str) -> str:
    parsed = urlparse(str(url or "").strip())
    if parsed.scheme not in ("http", "https") or not parsed.netloc or parsed.username or parsed.password:
        raise ValueError("source_url must be an absolute http(s) URL without embedded credentials")
    if len(url) > 2048:
        raise ValueError("source_url is too long")
    return url.strip()

class LeadStore:
    """Tenant-scoped SQLite storage for customer-demand signals."""

    ROLES: ClassVar[frozenset[str]] = frozenset({"owner", "admin", "manager", "sales_agent", "viewer"})
    DEFAULT_TENANT_ID = "default"

    def __init__(
        self,
        path: str | Path | None = None,
        *,
        default_tenant_id: str = DEFAULT_TENANT_ID,
        default_tenant_name: str = "المنشأة الرئيسية",
    ):
        self.path = Path(path or Path.home() / ".omarai" / "omarai.sqlite3").expanduser()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.default_tenant_id = self._required_id(default_tenant_id, "tenant_id")
        default_tenant_name = str(default_tenant_name or "").strip()[:200]
        if not default_tenant_name:
            raise ValueError("company name is required")
        with self.connect() as db:
            db.execute(
                """CREATE TABLE IF NOT EXISTS companies (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    status TEXT NOT NULL DEFAULT 'active'
                        CHECK(status IN ('active', 'suspended', 'archived')),
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )"""
            )
            db.execute(
                """CREATE TABLE IF NOT EXISTS users (
                    id TEXT PRIMARY KEY,
                    email TEXT UNIQUE,
                    display_name TEXT NOT NULL DEFAULT '',
                    status TEXT NOT NULL DEFAULT 'active'
                        CHECK(status IN ('active', 'disabled')),
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )"""
            )
            db.execute(
                """CREATE TABLE IF NOT EXISTS tenant_memberships (
                    tenant_id TEXT NOT NULL REFERENCES companies(id) ON DELETE CASCADE,
                    user_id TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
                    role TEXT NOT NULL CHECK(role IN (
                        'owner', 'admin', 'manager', 'sales_agent', 'viewer'
                    )),
                    status TEXT NOT NULL DEFAULT 'active'
                        CHECK(status IN ('active', 'suspended', 'revoked')),
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL,
                    PRIMARY KEY (tenant_id, user_id)
                )"""
            )
            now = now_utc()
            db.execute(
                """INSERT OR IGNORE INTO companies
                   (id, name, status, created_at, updated_at)
                   VALUES (?, ?, 'active', ?, ?)""",
                (self.default_tenant_id, default_tenant_name, now, now),
            )
            db.execute(
                """INSERT OR IGNORE INTO users
                   (id, email, display_name, status, created_at, updated_at)
                   VALUES ('operator', NULL, 'Local operator', 'active', ?, ?)""",
                (now, now),
            )
            db.execute(
                """INSERT OR IGNORE INTO tenant_memberships
                   (tenant_id, user_id, role, status, created_at, updated_at)
                   VALUES (?, 'operator', 'owner', 'active', ?, ?)""",
                (self.default_tenant_id, now, now),
            )
            self._ensure_tenant_scoped_leads_table(db)
            db.execute(
                """CREATE INDEX IF NOT EXISTS leads_tenant_status_idx
                   ON leads(tenant_id, status, created_at DESC)"""
            )

    def connect(self):
        db = sqlite3.connect(self.path, timeout=10)
        db.row_factory = sqlite3.Row
        db.execute("PRAGMA foreign_keys = ON")
        return db

    @staticmethod
    def _required_id(value: object, field: str) -> str:
        result = str(value or "").strip()
        if not result or len(result) > 128:
            raise ValueError(f"{field} must be a non-empty value of at most 128 characters")
        return result

    @staticmethod
    def _create_leads_table(db: sqlite3.Connection) -> None:
        db.execute(
            """CREATE TABLE leads (
                id TEXT PRIMARY KEY,
                tenant_id TEXT NOT NULL REFERENCES companies(id) ON DELETE CASCADE,
                fingerprint TEXT NOT NULL,
                text TEXT NOT NULL,
                source_url TEXT NOT NULL,
                platform TEXT NOT NULL,
                observed_at TEXT NOT NULL,
                assessment TEXT NOT NULL,
                status TEXT NOT NULL,
                note TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                UNIQUE (tenant_id, fingerprint)
            )"""
        )

    def _ensure_tenant_scoped_leads_table(self, db: sqlite3.Connection) -> None:
        table = db.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='leads'"
        ).fetchone()
        if table is None:
            self._create_leads_table(db)
            return

        columns = {
            row["name"] for row in db.execute("PRAGMA table_info(leads)").fetchall()
        }
        if "tenant_id" in columns:
            required = {
                "id", "fingerprint", "text", "source_url", "platform", "observed_at",
                "assessment", "status", "note", "created_at", "updated_at",
            }
            missing = required - columns
            if missing:
                raise RuntimeError(
                    "Unsupported leads schema; missing columns: " + ", ".join(sorted(missing))
                )
            return

        # Preserve every legacy lead under the initial company while replacing the
        # global UNIQUE(fingerprint) constraint with UNIQUE(tenant_id, fingerprint).
        db.execute("DROP INDEX IF EXISTS leads_status_idx")
        db.execute("ALTER TABLE leads RENAME TO leads_legacy_migration")
        self._create_leads_table(db)
        db.execute(
            """INSERT INTO leads (
                   id, tenant_id, fingerprint, text, source_url, platform, observed_at,
                   assessment, status, note, created_at, updated_at
               )
               SELECT id, ?, fingerprint, text, source_url, platform, observed_at,
                      assessment, status, note, created_at, updated_at
               FROM leads_legacy_migration""",
            (self.default_tenant_id,),
        )
        db.execute("DROP TABLE leads_legacy_migration")

    def create_company(self, company_id: str, name: str) -> None:
        company_id = self._required_id(company_id, "company_id")
        name = str(name or "").strip()[:200]
        if not name:
            raise ValueError("company name is required")
        now = now_utc()
        with self.connect() as db:
            db.execute(
                """INSERT INTO companies (id, name, status, created_at, updated_at)
                   VALUES (?, ?, 'active', ?, ?)""",
                (company_id, name, now, now),
            )

    def create_user(
        self, user_id: str, *, email: str | None = None, display_name: str = ""
    ) -> None:
        user_id = self._required_id(user_id, "user_id")
        email = str(email or "").strip().lower() or None
        if email and len(email) > 320:
            raise ValueError("email is too long")
        now = now_utc()
        with self.connect() as db:
            db.execute(
                """INSERT INTO users
                   (id, email, display_name, status, created_at, updated_at)
                   VALUES (?, ?, ?, 'active', ?, ?)""",
                (user_id, email, str(display_name or "")[:200], now, now),
            )

    def add_membership(self, tenant_id: str, user_id: str, role: str = "sales_agent") -> None:
        tenant_id = self._required_id(tenant_id, "tenant_id")
        user_id = self._required_id(user_id, "user_id")
        if role not in self.ROLES:
            raise ValueError("unsupported membership role")
        now = now_utc()
        with self.connect() as db:
            db.execute(
                """INSERT INTO tenant_memberships
                   (tenant_id, user_id, role, status, created_at, updated_at)
                   VALUES (?, ?, ?, 'active', ?, ?)
                   ON CONFLICT(tenant_id, user_id) DO UPDATE SET
                       role=excluded.role, status='active', updated_at=excluded.updated_at""",
                (tenant_id, user_id, role, now, now),
            )

    def resolve_membership(
        self, user_id: str, requested_tenant_id: str | None = None
    ) -> dict | None:
        """Resolve an active tenant only through a persisted user membership."""
        user_id = self._required_id(user_id, "user_id")
        if requested_tenant_id is not None:
            requested_tenant_id = self._required_id(requested_tenant_id, "tenant_id")
        with self.connect() as db:
            rows = db.execute(
                """SELECT m.tenant_id, m.user_id, m.role, c.name AS company_name
                   FROM tenant_memberships AS m
                   JOIN users AS u ON u.id = m.user_id
                   JOIN companies AS c ON c.id = m.tenant_id
                   WHERE m.user_id = ?
                     AND m.status = 'active'
                     AND u.status = 'active'
                     AND c.status = 'active'
                   ORDER BY m.tenant_id""",
                (user_id,),
            ).fetchall()
        memberships = [dict(row) for row in rows]
        if requested_tenant_id is not None:
            return next(
                (item for item in memberships if item["tenant_id"] == requested_tenant_id),
                None,
            )
        if len(memberships) == 1:
            return memberships[0]
        return next(
            (item for item in memberships if item["tenant_id"] == self.default_tenant_id),
            None,
        )

    def add(
        self,
        text: str,
        source_url: str,
        platform: str = "manual",
        observed_at: str | None = None,
        note: str = "",
        product_terms=(),
        location_terms=(),
        *,
        tenant_id: str = DEFAULT_TENANT_ID,
    ):
        tenant_id = self._required_id(tenant_id, "tenant_id")
        if not isinstance(text, str) or not text.strip():
            raise ValueError("text is required")
        if len(text) > MAX_TEXT:
            raise ValueError("text is too long")
        url = validate_url(source_url)
        normalized = normalize(text)
        fingerprint = hashlib.sha256(
            (url.rstrip("/") + "\n" + normalized).encode()
        ).hexdigest()
        lead_id = hashlib.sha256(
            (tenant_id + "\n" + fingerprint).encode()
        ).hexdigest()[:24]
        timestamp = observed_at or now_utc()
        assessment = analyze(text, product_terms=product_terms, location_terms=location_terms)
        now = now_utc()
        with self.connect() as db:
            company = db.execute(
                "SELECT 1 FROM companies WHERE id=? AND status='active'", (tenant_id,)
            ).fetchone()
            if not company:
                raise ValueError("unknown or inactive company")
            cursor = db.execute(
                """INSERT OR IGNORE INTO leads
                   (id, tenant_id, fingerprint, text, source_url, platform, observed_at,
                    assessment, status, note, created_at, updated_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    lead_id, tenant_id, fingerprint, text.strip(), url, str(platform)[:80],
                    timestamp, json.dumps(assessment, ensure_ascii=False), "new",
                    str(note)[:1000], now, now,
                ),
            )
            row = db.execute(
                "SELECT * FROM leads WHERE tenant_id=? AND fingerprint=?",
                (tenant_id, fingerprint),
            ).fetchone()
        return self.to_dict(row), cursor.rowcount == 1

    @staticmethod
    def to_dict(row):
        item = dict(row)
        item["assessment"] = json.loads(item["assessment"])
        return item

    def list(self, status: str | None = None, limit: int = 100, *, tenant_id: str = DEFAULT_TENANT_ID):
        tenant_id = self._required_id(tenant_id, "tenant_id")
        limit = max(1, min(int(limit), 500))
        with self.connect() as db:
            rows = db.execute(
                """SELECT * FROM leads
                   WHERE tenant_id=? AND (? IS NULL OR status=?)
                   ORDER BY created_at DESC LIMIT ?""",
                (tenant_id, status, status, limit),
            ).fetchall()
        return [self.to_dict(row) for row in rows]

    def update_status(
        self, lead_id: str, status: str, *, tenant_id: str = DEFAULT_TENANT_ID
    ):
        tenant_id = self._required_id(tenant_id, "tenant_id")
        allowed = {"new", "qualified", "contacted", "converted", "rejected", "needs_review"}
        if status not in allowed:
            raise ValueError("unsupported status")
        with self.connect() as db:
            db.execute(
                "UPDATE leads SET status=?, updated_at=? WHERE id=? AND tenant_id=?",
                (status, now_utc(), lead_id, tenant_id),
            )
            row = db.execute(
                "SELECT * FROM leads WHERE id=? AND tenant_id=?", (lead_id, tenant_id)
            ).fetchone()
        return self.to_dict(row) if row else None

    def import_csv(self, filename: str, *, tenant_id: str = DEFAULT_TENANT_ID):
        tenant_id = self._required_id(tenant_id, "tenant_id")
        results = {"created": 0, "duplicates": 0, "errors": []}
        with open(filename, newline="", encoding="utf-8-sig") as stream:
            reader = csv.DictReader(stream)
            required = {"text", "source_url", "platform"}
            if not reader.fieldnames or not required.issubset(reader.fieldnames):
                raise ValueError("CSV must contain text,source_url,platform columns")
            for line, row in enumerate(reader, 2):
                try:
                    _, created = self.add(
                        row["text"], row["source_url"], row["platform"],
                        row.get("observed_at") or None, row.get("note") or "",
                        tenant_id=tenant_id,
                    )
                    results["created" if created else "duplicates"] += 1
                except (ValueError, TypeError) as exc:
                    results["errors"].append({"line": line, "error": str(exc)})
        return results

    def _write_csv(self, stream, tenant_id: str) -> int:
        rows = self.list(limit=500, tenant_id=tenant_id)
        fields = [
            "id", "tenant_id", "text", "source_url", "platform", "observed_at",
            "assessment", "status", "note", "created_at",
        ]
        writer = csv.DictWriter(stream, fieldnames=fields, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for row in rows:
            values = {
                key: json.dumps(row[key], ensure_ascii=False)
                if key == "assessment"
                else row.get(key, "")
                for key in fields
            }
            writer.writerow({key: _csv_safe_cell(value) for key, value in values.items()})
        return len(rows)

    def export_csv(self, filename: str | Path, *, tenant_id: str = DEFAULT_TENANT_ID):
        tenant_id = self._required_id(tenant_id, "tenant_id")
        with open(filename, "w", newline="", encoding="utf-8-sig") as stream:
            return self._write_csv(stream, tenant_id)

    def export_csv_text(self, *, tenant_id: str = DEFAULT_TENANT_ID) -> str:
        tenant_id = self._required_id(tenant_id, "tenant_id")
        stream = StringIO(newline="")
        self._write_csv(stream, tenant_id)
        return stream.getvalue()
