"""Explainable Arabic lead-intent analysis and local SQLite storage."""
from __future__ import annotations

import csv
import hashlib
import json
import re
import sqlite3
import unicodedata
from datetime import UTC, datetime
from pathlib import Path
import uuid
from urllib.parse import urlparse

MAX_TEXT = 12000
DEFAULT_TENANT_ID = "tenant_default"
DEFAULT_USER_ID = "user_local_admin"
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
    """Tenant-scoped SQLite lead storage with a safe single-company bootstrap."""

    ALLOWED_STATUSES = frozenset({
        "new", "qualified", "contacted", "converted", "rejected", "needs_review"
    })
    ALLOWED_ROLES = frozenset({"owner", "admin", "manager", "sales_agent", "viewer"})

    def __init__(self, path: str | Path | None = None):
        self.path = Path(path or Path.home() / ".omarai" / "omarai.sqlite3").expanduser()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as db:
            self._initialize_schema(db)

    def connect(self):
        db = sqlite3.connect(self.path, timeout=10)
        db.row_factory = sqlite3.Row
        db.execute("PRAGMA foreign_keys = ON")
        return db

    @staticmethod
    def _create_leads_table(db):
        db.execute(
            """CREATE TABLE IF NOT EXISTS leads (
                id TEXT PRIMARY KEY,
                tenant_id TEXT NOT NULL REFERENCES tenants(id),
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

    def _initialize_schema(self, db):
        db.execute(
            """CREATE TABLE IF NOT EXISTS tenants (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                slug TEXT NOT NULL UNIQUE,
                active INTEGER NOT NULL DEFAULT 1,
                created_at TEXT NOT NULL
            )"""
        )
        db.execute(
            """CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                email TEXT NOT NULL UNIQUE COLLATE NOCASE,
                display_name TEXT NOT NULL,
                active INTEGER NOT NULL DEFAULT 1,
                created_at TEXT NOT NULL
            )"""
        )
        db.execute(
            """CREATE TABLE IF NOT EXISTS tenant_memberships (
                tenant_id TEXT NOT NULL REFERENCES tenants(id),
                user_id TEXT NOT NULL REFERENCES users(id),
                role TEXT NOT NULL,
                active INTEGER NOT NULL DEFAULT 1,
                created_at TEXT NOT NULL,
                PRIMARY KEY (tenant_id, user_id)
            )"""
        )
        db.execute(
            """CREATE TABLE IF NOT EXISTS api_tokens (
                token_hash TEXT PRIMARY KEY,
                tenant_id TEXT NOT NULL,
                user_id TEXT NOT NULL,
                label TEXT NOT NULL,
                active INTEGER NOT NULL DEFAULT 1,
                created_at TEXT NOT NULL,
                expires_at TEXT,
                FOREIGN KEY (tenant_id, user_id)
                    REFERENCES tenant_memberships(tenant_id, user_id)
            )"""
        )

        now = now_utc()
        db.execute(
            """INSERT OR IGNORE INTO tenants (id, name, slug, active, created_at)
               VALUES (?, ?, ?, 1, ?)""",
            (DEFAULT_TENANT_ID, "Omarai Workspace", "omarai-default", now),
        )
        db.execute(
            """INSERT OR IGNORE INTO users
               (id, email, display_name, active, created_at)
               VALUES (?, ?, ?, 1, ?)""",
            (DEFAULT_USER_ID, "local-admin@omarai.invalid", "Omarai Local Admin", now),
        )
        db.execute(
            """INSERT OR IGNORE INTO tenant_memberships
               (tenant_id, user_id, role, active, created_at)
               VALUES (?, ?, 'owner', 1, ?)""",
            (DEFAULT_TENANT_ID, DEFAULT_USER_ID, now),
        )

        table = db.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name='leads'"
        ).fetchone()
        if table:
            columns = {
                row["name"] for row in db.execute("PRAGMA table_info(leads)").fetchall()
            }
            unique_fingerprint = False
            for index in db.execute("PRAGMA index_list(leads)").fetchall():
                if not index["unique"]:
                    continue
                index_columns = [
                    row["name"]
                    for row in db.execute(
                        f"PRAGMA index_info('{index['name']}')"
                    ).fetchall()
                ]
                if index_columns == ["fingerprint"]:
                    unique_fingerprint = True
                    break
            if "tenant_id" not in columns or unique_fingerprint:
                db.execute("ALTER TABLE leads RENAME TO leads_legacy_migration")
                self._create_leads_table(db)
                legacy_columns = {
                    row["name"]
                    for row in db.execute(
                        "PRAGMA table_info(leads_legacy_migration)"
                    ).fetchall()
                }
                tenant_expression = (
                    "tenant_id" if "tenant_id" in legacy_columns else "?"
                )
                fields = (
                    "id, fingerprint, text, source_url, platform, observed_at, "
                    "assessment, status, note, created_at, updated_at"
                )
                if tenant_expression == "?":
                    db.execute(
                        f"""INSERT OR IGNORE INTO leads
                            (id, tenant_id, fingerprint, text, source_url, platform,
                             observed_at, assessment, status, note, created_at, updated_at)
                            SELECT id, ?, fingerprint, text, source_url, platform,
                                   observed_at, assessment, status, note, created_at, updated_at
                            FROM leads_legacy_migration""",
                        (DEFAULT_TENANT_ID,),
                    )
                else:
                    db.execute(
                        f"""INSERT OR IGNORE INTO leads
                            (id, tenant_id, fingerprint, text, source_url, platform,
                             observed_at, assessment, status, note, created_at, updated_at)
                            SELECT id, tenant_id, fingerprint, text, source_url, platform,
                                   observed_at, assessment, status, note, created_at, updated_at
                            FROM leads_legacy_migration"""
                    )
                db.execute("DROP TABLE leads_legacy_migration")
        else:
            self._create_leads_table(db)

        db.execute("DROP INDEX IF EXISTS leads_status_idx")
        db.execute(
            "CREATE INDEX IF NOT EXISTS leads_tenant_status_idx "
            "ON leads(tenant_id, status, created_at DESC)"
        )
        db.execute(
            "CREATE INDEX IF NOT EXISTS memberships_user_active_idx "
            "ON tenant_memberships(user_id, active, tenant_id)"
        )

    @staticmethod
    def _tenant(tenant_id: str | None) -> str:
        value = DEFAULT_TENANT_ID if tenant_id is None else str(tenant_id).strip()
        if not value or len(value) > 128:
            raise ValueError("tenant_id is invalid")
        return value

    def default_principal(self) -> dict:
        with self.connect() as db:
            row = db.execute(
                """SELECT m.tenant_id, m.user_id, m.role
                   FROM tenant_memberships m
                   JOIN tenants t ON t.id=m.tenant_id AND t.active=1
                   JOIN users u ON u.id=m.user_id AND u.active=1
                   WHERE m.tenant_id=? AND m.user_id=? AND m.active=1""",
                (DEFAULT_TENANT_ID, DEFAULT_USER_ID),
            ).fetchone()
        return dict(row) if row else {}

    def create_tenant(self, name: str, slug: str | None = None) -> str:
        clean_name = str(name or "").strip()[:160]
        if not clean_name:
            raise ValueError("tenant name is required")
        clean_slug = re.sub(
            r"[^a-z0-9-]+", "-", str(slug or clean_name.casefold())
        ).strip("-")[:80]
        if not clean_slug:
            raise ValueError("tenant slug is invalid")
        tenant_id = "tenant_" + uuid.uuid4().hex
        with self.connect() as db:
            db.execute(
                "INSERT INTO tenants (id, name, slug, active, created_at) VALUES (?, ?, ?, 1, ?)",
                (tenant_id, clean_name, clean_slug, now_utc()),
            )
        return tenant_id

    def create_user(self, email: str, display_name: str, user_id: str | None = None) -> str:
        clean_email = str(email or "").strip().lower()[:254]
        clean_name = str(display_name or "").strip()[:160]
        if not clean_email or "@" not in clean_email or not clean_name:
            raise ValueError("valid email and display name are required")
        identity = str(user_id or ("user_" + uuid.uuid4().hex))
        with self.connect() as db:
            db.execute(
                """INSERT INTO users (id, email, display_name, active, created_at)
                   VALUES (?, ?, ?, 1, ?)""",
                (identity, clean_email, clean_name, now_utc()),
            )
        return identity

    def add_membership(self, tenant_id: str, user_id: str, role: str = "sales_agent"):
        tenant = self._tenant(tenant_id)
        if role not in self.ALLOWED_ROLES:
            raise ValueError("unsupported membership role")
        with self.connect() as db:
            exists = db.execute(
                """SELECT 1 FROM tenants t JOIN users u
                   WHERE t.id=? AND t.active=1 AND u.id=? AND u.active=1""",
                (tenant, user_id),
            ).fetchone()
            if not exists:
                raise ValueError("active tenant and user are required")
            db.execute(
                """INSERT INTO tenant_memberships
                   (tenant_id, user_id, role, active, created_at)
                   VALUES (?, ?, ?, 1, ?)
                   ON CONFLICT(tenant_id, user_id)
                   DO UPDATE SET role=excluded.role, active=1""",
                (tenant, user_id, role, now_utc()),
            )

    @staticmethod
    def _token_hash(token: str) -> str:
        return hashlib.sha256(token.encode("utf-8")).hexdigest()

    def create_api_token(
        self,
        token: str,
        tenant_id: str,
        user_id: str,
        label: str = "api",
        expires_at: str | None = None,
    ):
        if not isinstance(token, str) or len(token.strip()) < 32:
            raise ValueError("API token must contain at least 32 characters")
        tenant = self._tenant(tenant_id)
        with self.connect() as db:
            membership = db.execute(
                """SELECT 1 FROM tenant_memberships m
                   JOIN tenants t ON t.id=m.tenant_id AND t.active=1
                   JOIN users u ON u.id=m.user_id AND u.active=1
                   WHERE m.tenant_id=? AND m.user_id=? AND m.active=1""",
                (tenant, user_id),
            ).fetchone()
            if not membership:
                raise ValueError("active tenant membership is required")
            db.execute(
                """INSERT INTO api_tokens
                   (token_hash, tenant_id, user_id, label, active, created_at, expires_at)
                   VALUES (?, ?, ?, ?, 1, ?, ?)""",
                (
                    self._token_hash(token.strip()),
                    tenant,
                    user_id,
                    str(label or "api")[:80],
                    now_utc(),
                    expires_at,
                ),
            )

    def resolve_api_token(self, token: str) -> dict | None:
        if not isinstance(token, str) or len(token.strip()) < 32:
            return None
        with self.connect() as db:
            row = db.execute(
                """SELECT m.tenant_id, m.user_id, m.role
                   FROM api_tokens a
                   JOIN tenant_memberships m
                     ON m.tenant_id=a.tenant_id AND m.user_id=a.user_id
                   JOIN tenants t ON t.id=m.tenant_id AND t.active=1
                   JOIN users u ON u.id=m.user_id AND u.active=1
                   WHERE a.token_hash=? AND a.active=1 AND m.active=1
                     AND (a.expires_at IS NULL OR a.expires_at > ?)""",
                (self._token_hash(token.strip()), now_utc()),
            ).fetchone()
        return dict(row) if row else None

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
        tenant_id: str | None = None,
    ):
        if not isinstance(text, str) or not text.strip():
            raise ValueError("text is required")
        if len(text) > MAX_TEXT:
            raise ValueError("text is too long")
        tenant = self._tenant(tenant_id)
        url = validate_url(source_url)
        normalized = normalize(text)
        fingerprint = hashlib.sha256(
            (tenant + "\\n" + url.rstrip("/") + "\\n" + normalized).encode()
        ).hexdigest()
        lead_id = fingerprint[:24]
        timestamp = observed_at or now_utc()
        assessment = analyze(text, product_terms=product_terms, location_terms=location_terms)
        now = now_utc()
        with self.connect() as db:
            active_tenant = db.execute(
                "SELECT 1 FROM tenants WHERE id=? AND active=1", (tenant,)
            ).fetchone()
            if not active_tenant:
                raise ValueError("active tenant is required")
            cursor = db.execute(
                """INSERT OR IGNORE INTO leads
                   (id, tenant_id, fingerprint, text, source_url, platform, observed_at,
                    assessment, status, note, created_at, updated_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    lead_id, tenant, fingerprint, text.strip(), url,
                    str(platform)[:80], timestamp,
                    json.dumps(assessment, ensure_ascii=False), "new",
                    str(note)[:1000], now, now,
                ),
            )
            row = db.execute(
                "SELECT * FROM leads WHERE tenant_id=? AND fingerprint=?",
                (tenant, fingerprint),
            ).fetchone()
        return self.to_dict(row), cursor.rowcount == 1

    @staticmethod
    def to_dict(row):
        item = dict(row)
        item["assessment"] = json.loads(item["assessment"])
        return item

    def list(
        self,
        status: str | None = None,
        limit: int = 100,
        *,
        tenant_id: str | None = None,
    ):
        tenant = self._tenant(tenant_id)
        limit = max(1, min(int(limit), 500))
        with self.connect() as db:
            rows = db.execute(
                """SELECT * FROM leads
                   WHERE tenant_id=? AND (? IS NULL OR status=?)
                   ORDER BY created_at DESC LIMIT ?""",
                (tenant, status, status, limit),
            ).fetchall()
        return [self.to_dict(row) for row in rows]

    def update_status(
        self,
        lead_id: str,
        status: str,
        *,
        tenant_id: str | None = None,
    ):
        if status not in self.ALLOWED_STATUSES:
            raise ValueError("unsupported status")
        tenant = self._tenant(tenant_id)
        with self.connect() as db:
            db.execute(
                "UPDATE leads SET status=?, updated_at=? WHERE id=? AND tenant_id=?",
                (status, now_utc(), lead_id, tenant),
            )
            row = db.execute(
                "SELECT * FROM leads WHERE id=? AND tenant_id=?",
                (lead_id, tenant),
            ).fetchone()
        return self.to_dict(row) if row else None

    def import_csv(self, filename: str, *, tenant_id: str | None = None):
        tenant = self._tenant(tenant_id)
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
                        tenant_id=tenant,
                    )
                    results["created" if created else "duplicates"] += 1
                except (ValueError, TypeError) as exc:
                    results["errors"].append({"line": line, "error": str(exc)})
        return results

    def export_csv(self, filename: str, *, tenant_id: str | None = None):
        rows = self.list(limit=500, tenant_id=tenant_id)
        with open(filename, "w", newline="", encoding="utf-8-sig") as stream:
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
