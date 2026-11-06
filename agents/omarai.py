"""Explainable Arabic lead-intent analysis and local SQLite storage."""
from __future__ import annotations

import csv
import hashlib
import hmac
import ipaddress
import json
import re
import secrets
import sqlite3
import unicodedata
from contextlib import contextmanager
from collections.abc import Iterator
from datetime import UTC, datetime, timedelta
from pathlib import Path
import uuid
from urllib.parse import urlparse

from agents.sales_domain import (
    ContactabilityStatus,
    DemandEvidence,
    DemandSignal,
    DemandSignalType,
    EvidenceBasis,
    FreshnessStatus,
    IdentityStatus,
    LeadQualification,
    ProductFit,
    SourceQuality,
)

MAX_TEXT = 12000
DEFAULT_TENANT_ID = "tenant_default"
DEFAULT_USER_ID = "user_local_admin"
_TRANSLATION = str.maketrans({"أ":"ا","إ":"ا","آ":"ا","ٱ":"ا","ى":"ي","ئ":"ي","ؤ":"و","ـ":""})
SIGNALS = {
    # Direct demand language is sector-neutral. A product mention alone is never
    # sufficient to establish buying intent.
    "high": (35, (
        "عايز اشتري", "عاوز اشتري", "محتاج اشتري",
        # Retain established property-language compatibility while allowing any sector.
        "بدور على شقة", "بدور على عقار", "مطلوب شقة", "عايز وحدة",
    )),
    "direct_demand": (55, (
        "نحتاج شراء", "نبحث عن مورد", "مطلوب مورد", "مطلوب توريد",
        "نحتاج توريد", "محتاجين توريد", "نحتاج نظام", "محتاجين نظام",
        "نحتاج خدمة", "نحتاج عرض سعر", "مطلوب شراء", "طلب شراء", "طلب عرض سعر",
        "طلب عروض اسعار", "مناقصة توريد", "نبحث عن شركة", "نحتاج شركة",
        "looking to buy", "need to purchase", "seeking a supplier",
        "need a supplier", "request for quotation", "purchase request",
        "procurement request", "rfq", "request a quote",
    )),
    "next_step": (20, (
        "ممكن معاينة", "عايز اعاين", "عاوز اعاين", "ابعت التفاصيل",
        "ابعت اللوكيشن", "ميعاد للمعاينة", "ابعت عرض سعر", "ارسل عرض سعر",
        "نحتاج عرض سعر", "يرجى تقديم عرض", "send a quotation",
        "send quote", "contact for quote",
    )),
    "budget": (15, (
        "السعر كام", "مقدم كام", "ميزانيتي", "معايا مقدم", "تقسيط",
        "على اقساط", "في حدود", "ما هي التكلفة", "what is the price",
        "what does it cost", "budget is",
    )),
    "explore": (10, (
        "بدور على", "فيه شقق", "ايه المتاح", "عايز اعرف الاسعار",
        "ابحث عن", "نبحث عن", "looking for", "seeking information",
    )),
}
NOT_BUYER = (
    "مش عايز اشتري", "مش عاوز اشتري", "مش بدور على", "مش محتاج",
    "مش محتاجين", "لا نحتاج", "لا نبحث عن", "لسنا بحاجة",
    "ما عنديش نية", "مش ناوي", "مش مهتم", "مش هشتري",
    "not interested", "not looking for", "do not need", "don't need", "not seeking",
    "عايز ابيع", "عاوز ابيع", "عندي شقة للبيع", "انا وسيط", "انا سمسار",
    "عايز ايجار", "للايجار", "not looking for", "do not need",
    "don't need", "not seeking",
)
CLOSED_OR_STALE = (
    "تم الغاء الطلب", "الغيت الطلب", "لغيت الطلب",
    "تم الشراء", "اشترينا", "اشتريت بالفعل", "تم التعاقد", "تعاقدنا",
    "وجدنا مورد", "تم اختيار المورد", "تم التوريد", "اكتمل التوريد",
    "تم حل المشكلة", "لم نعد بحاجة", "already purchased", "we purchased",
    "contract awarded", "supplier selected", "need fulfilled",
    "no longer needed", "كنت بدور على", "كنت محتاج", "كنت ابحث عن",
    "was looking for", "previously needed",
)

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

def _signal_type_for_matches(matches: list[dict]) -> DemandSignalType:
    categories = {item["category"] for item in matches}
    phrases = {normalize(item["phrase"]) for item in matches}
    if "direct_demand" in categories:
        if any(token in phrases for token in {
            normalize("طلب عرض سعر"), normalize("طلب عروض اسعار"),
            normalize("نحتاج عرض سعر"), normalize("request for quotation"), normalize("rfq"),
            normalize("request a quote"),
        }):
            return DemandSignalType.REQUEST_FOR_QUOTATION
        if any(token in phrases for token in {
            normalize("مناقصة توريد"), normalize("procurement request"),
        }):
            return DemandSignalType.TENDER_OR_PROCUREMENT
        return DemandSignalType.DIRECT_PURCHASE_REQUEST
    if "high" in categories:
        return DemandSignalType.STATED_NEED
    if categories.intersection({"next_step", "budget", "explore"}):
        return DemandSignalType.INDIRECT_INDICATOR
    return DemandSignalType.UNKNOWN


def _contains_normalized_phrase(body: str, phrase: str) -> bool:
    """Match a normalized phrase while allowing common attached Arabic clitics."""
    normalized_phrase = normalize(phrase)
    if not normalized_phrase:
        return False
    # Arabic conjunctions/prepositions are commonly attached to the next word
    # (e.g. "وممكن معاينة"); allow one such prefix without partial-word matches.
    pattern = rf"(?<!\w)(?:[وفبكل])?{re.escape(normalized_phrase)}(?!\w)"
    return re.search(pattern, body, flags=re.UNICODE) is not None


def analyze(text: str, product_terms=(), location_terms=()) -> dict:
    """Score explicit demand language without treating product fit as purchase intent."""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("text must not be empty")
    if len(text) > MAX_TEXT:
        raise ValueError(f"text must be at most {MAX_TEXT} characters")

    body = normalize(text)
    closed = [phrase for phrase in CLOSED_OR_STALE if _contains_normalized_phrase(body, phrase)]
    if closed:
        return {
            "score": 0,
            "label": "closed_or_stale_signal",
            "signal_type": (
                DemandSignalType.CANCELLED.value
                if any(normalize(phrase) in {normalize("تم الغاء الطلب"), normalize("الغيت الطلب"), normalize("لغيت الطلب")} for phrase in closed)
                else DemandSignalType.EXPIRED.value
            ),
            "summary": "الإشارة قديمة أو تم تلبية الاحتياج؛ لا تُعامل كطلب شراء نشط.",
            "matched_signals": [
                {"phrase": phrase, "category": "closed_or_stale", "points": 0}
                for phrase in closed
            ],
            "warnings": ["تحقق من التاريخ والسياق قبل أي متابعة."],
        }

    excluded = [phrase for phrase in NOT_BUYER if _contains_normalized_phrase(body, phrase)]
    if excluded:
        return {
            "score": 0,
            "label": "not_buyer_signal",
            "signal_type": DemandSignalType.NEGATED.value,
            "summary": "النص ينفي الاحتياج أو لا يمثل طلب شراء نشطًا؛ راجعه يدويًا.",
            "matched_signals": [
                {"phrase": phrase, "category": "exclusion", "points": 0}
                for phrase in excluded
            ],
            "warnings": ["لا تُصنّف النفي كإشارة شراء."],
        }

    matches = []
    for category, (points, phrases) in SIGNALS.items():
        found = next(
            (phrase for phrase in phrases if _contains_normalized_phrase(body, phrase)),
            None,
        )
        if found:
            matches.append({"phrase": found, "category": category, "points": points})

    # Product and location matches are contextual dimensions only. They must
    # never inflate the demand score or turn a catalogue mention into a lead.
    for category, terms in (("product_context", product_terms), ("location_context", location_terms)):
        found = next(
            (
                normalize(term)
                for term in terms
                if isinstance(term, str)
                and normalize(term)
                and _contains_normalized_phrase(body, term)
            ),
            None,
        )
        if found:
            matches.append({"phrase": found, "category": category, "points": 0})

    signal_type = _signal_type_for_matches(matches)
    score = min(100, sum(item["points"] for item in matches))
    label = (
        "high_intent"
        if score >= 55 and any(
            item["category"] in {"high", "direct_demand"} for item in matches
        )
        else "medium_intent"
        if score >= 40
        else "early_research"
        if score >= 20
        else "unclear"
    )
    return {
        "score": score,
        "label": label,
        "signal_type": signal_type.value,
        "summary": {
            "high_intent": "إشارة طلب مباشرة نسبيًا؛ يلزم التحقق من المصدر والحداثة.",
            "medium_intent": "مؤشرات اهتمام تستحق التأهيل والتحقق.",
            "early_research": "اهتمام مبكر؛ ليس طلب شراء مؤكدًا.",
            "unclear": "لا توجد لغة طلب كافية؛ ذكر المنتج وحده لا يكفي.",
        }[label],
        "matched_signals": matches,
        "warnings": [
            "الدرجة ترتيبية وليست احتمالًا إحصائيًا للشراء.",
            "لا تثبت هوية الكاتب أو قدرته على الدفع أو نيته.",
            "ملاءمة المنتج والموقع سياق منفصل ولا يرفعان درجة الطلب.",
            "استخدم مصادر عامة ومسموحًا بمعالجتها فقط.",
        ],
    }

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

    @contextmanager
    def connect(self) -> Iterator[sqlite3.Connection]:
        """Yield one transaction-scoped connection and always close it.

        sqlite3.Connection's built-in context manager commits or rolls back;
        it does not close the connection. This wrapper provides both guarantees.
        """
        db = sqlite3.connect(self.path, timeout=10)
        try:
            db.row_factory = sqlite3.Row
            db.execute("PRAGMA foreign_keys = ON")
            with db:
                yield db
        finally:
            db.close()

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
        db.execute(
            """CREATE TABLE IF NOT EXISTS web_sessions (
                session_hash TEXT PRIMARY KEY,
                credential_hash TEXT NOT NULL,
                is_shared_token INTEGER NOT NULL DEFAULT 0,
                tenant_id TEXT NOT NULL,
                user_id TEXT NOT NULL,
                created_at TEXT NOT NULL,
                expires_at TEXT NOT NULL,
                revoked_at TEXT,
                FOREIGN KEY (tenant_id, user_id)
                    REFERENCES tenant_memberships(tenant_id, user_id)
            )"""
        )
        db.execute(
            "CREATE INDEX IF NOT EXISTS idx_web_sessions_expiry "
            "ON web_sessions(expires_at, revoked_at)"
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
                if tenant_expression == "?":
                    db.execute(
                        """INSERT OR IGNORE INTO leads
                            (id, tenant_id, fingerprint, text, source_url, platform,
                             observed_at, assessment, status, note, created_at, updated_at)
                            SELECT id, ?, fingerprint, text, source_url, platform,
                                   observed_at, assessment, status, note, created_at, updated_at
                            FROM leads_legacy_migration""",
                        (DEFAULT_TENANT_ID,),
                    )
                else:
                    db.execute(
                        """INSERT OR IGNORE INTO leads
                            (id, tenant_id, fingerprint, text, source_url, platform,
                             observed_at, assessment, status, note, created_at, updated_at)
                            SELECT id, tenant_id, fingerprint, text, source_url, platform,
                                   observed_at, assessment, status, note, created_at, updated_at
                            FROM leads_legacy_migration"""
                    )
                legacy_count = db.execute(
                    "SELECT COUNT(*) FROM leads_legacy_migration"
                ).fetchone()[0]
                migrated_count = db.execute(
                    "SELECT COUNT(*) FROM leads"
                ).fetchone()[0]
                missing_rows = db.execute(
                    """SELECT COUNT(*)
                       FROM leads_legacy_migration legacy
                       LEFT JOIN leads migrated
                         ON migrated.id=legacy.id
                        AND migrated.fingerprint=legacy.fingerprint
                       WHERE migrated.id IS NULL"""
                ).fetchone()[0]
                foreign_key_errors = db.execute(
                    "PRAGMA foreign_key_check(leads)"
                ).fetchall()
                if (
                    migrated_count != legacy_count
                    or missing_rows
                    or foreign_key_errors
                ):
                    raise RuntimeError(
                        "lead migration verification failed; legacy data was retained"
                    )
                # Drop the old table only after count, identity, and FK checks pass.
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

        db.execute(
            """CREATE TABLE IF NOT EXISTS product_profiles (
                id TEXT PRIMARY KEY,
                tenant_id TEXT NOT NULL REFERENCES tenants(id),
                normalized_name TEXT NOT NULL,
                name TEXT NOT NULL,
                profile_json TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                UNIQUE (id, tenant_id),
                UNIQUE (tenant_id, normalized_name)
            )"""
        )
        db.execute(
            """CREATE TABLE IF NOT EXISTS discovery_runs (
                id TEXT PRIMARY KEY,
                tenant_id TEXT NOT NULL,
                profile_id TEXT NOT NULL,
                answer TEXT NOT NULL,
                kind TEXT NOT NULL,
                search_queries_json TEXT NOT NULL,
                search_report_json TEXT NOT NULL,
                sources_json TEXT NOT NULL,
                created_at TEXT NOT NULL,
                FOREIGN KEY (profile_id, tenant_id)
                    REFERENCES product_profiles(id, tenant_id)
            )"""
        )
        db.execute(
            "CREATE INDEX IF NOT EXISTS product_profiles_tenant_updated_idx "
            "ON product_profiles(tenant_id, updated_at DESC)"
        )
        db.execute(
            "CREATE INDEX IF NOT EXISTS discovery_runs_tenant_created_idx "
            "ON discovery_runs(tenant_id, created_at DESC)"
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
                """SELECT 1 FROM tenants t
                   JOIN users u ON u.id=?
                   WHERE t.id=? AND t.active=1 AND u.active=1""",
                (user_id, tenant),
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

    @staticmethod
    def _normalize_token_expiry(expires_at: str | None) -> str | None:
        """Store token expiries as validated UTC timestamps for safe comparisons."""
        if expires_at is None:
            return None
        if not isinstance(expires_at, str) or not expires_at.strip():
            raise ValueError("expires_at must be an ISO-8601 timestamp with a timezone")
        value = expires_at.strip()
        if value.endswith("Z"):
            value = value[:-1] + "+00:00"
        try:
            parsed = datetime.fromisoformat(value)
        except ValueError as exc:
            raise ValueError(
                "expires_at must be an ISO-8601 timestamp with a timezone"
            ) from exc
        if parsed.tzinfo is None or parsed.utcoffset() is None:
            raise ValueError("expires_at must include an explicit timezone")
        normalized = parsed.astimezone(UTC)
        if normalized <= datetime.now(UTC):
            raise ValueError("expires_at must be in the future")
        return normalized.isoformat(timespec="seconds").replace("+00:00", "Z")

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
        expires_at = self._normalize_token_expiry(expires_at)
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

    def create_web_session(
        self,
        access_token: str,
        *,
        shared_token: str = "",
        max_age_seconds: int = 8 * 60 * 60,
    ) -> tuple[str, dict] | None:
        """Exchange a valid API credential for a short-lived opaque browser session."""
        if not isinstance(access_token, str) or len(access_token.strip()) < 32:
            return None
        token = access_token.strip()
        is_shared = bool(shared_token and hmac.compare_digest(token, shared_token))
        principal = self.default_principal() if is_shared else self.resolve_api_token(token)
        if not principal:
            return None
        if (
            not isinstance(max_age_seconds, int)
            or isinstance(max_age_seconds, bool)
            or not 60 <= max_age_seconds <= 24 * 60 * 60
        ):
            raise ValueError("browser session lifetime must be between 60 seconds and 24 hours")

        session_id = secrets.token_urlsafe(32)
        created_at = now_utc()
        expires_at = (
            datetime.now(UTC) + timedelta(seconds=max_age_seconds)
        ).isoformat(timespec="seconds").replace("+00:00", "Z")
        with self.connect() as db:
            # Browser sessions are short-lived credentials, not an audit log.
            # Prune expired and revoked rows opportunistically before inserting
            # a new session so abandoned rows cannot grow without bound.
            db.execute(
                """DELETE FROM web_sessions
                   WHERE revoked_at IS NOT NULL OR expires_at <= ?""",
                (created_at,),
            )
            db.execute(
                """INSERT INTO web_sessions
                   (session_hash, credential_hash, is_shared_token, tenant_id,
                    user_id, created_at, expires_at, revoked_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, NULL)""",
                (
                    self._token_hash(session_id),
                    self._token_hash(token),
                    1 if is_shared else 0,
                    principal["tenant_id"],
                    principal["user_id"],
                    created_at,
                    expires_at,
                ),
            )
        return session_id, principal

    def resolve_web_session(
        self,
        session_id: str,
        *,
        shared_token: str = "",
    ) -> dict | None:
        """Resolve an opaque browser session and re-check its backing credential."""
        if not isinstance(session_id, str) or not re.fullmatch(
            r"[A-Za-z0-9_-]{32,128}", session_id
        ):
            return None
        with self.connect() as db:
            session = db.execute(
                """SELECT credential_hash, is_shared_token, tenant_id, user_id
                   FROM web_sessions
                   WHERE session_hash=? AND revoked_at IS NULL AND expires_at > ?""",
                (self._token_hash(session_id), now_utc()),
            ).fetchone()
            if not session:
                return None
            if session["is_shared_token"]:
                if (
                    not shared_token
                    or not hmac.compare_digest(
                        session["credential_hash"], self._token_hash(shared_token)
                    )
                ):
                    return None
                principal = db.execute(
                    """SELECT m.tenant_id, m.user_id, m.role
                       FROM tenant_memberships m
                       JOIN tenants t ON t.id=m.tenant_id AND t.active=1
                       JOIN users u ON u.id=m.user_id AND u.active=1
                       WHERE m.tenant_id=? AND m.user_id=? AND m.active=1""",
                    (session["tenant_id"], session["user_id"]),
                ).fetchone()
                return dict(principal) if principal else None

            principal = db.execute(
                """SELECT m.tenant_id, m.user_id, m.role
                   FROM api_tokens a
                   JOIN tenant_memberships m
                     ON m.tenant_id=a.tenant_id AND m.user_id=a.user_id
                   JOIN tenants t ON t.id=m.tenant_id AND t.active=1
                   JOIN users u ON u.id=m.user_id AND u.active=1
                   WHERE a.token_hash=? AND a.tenant_id=? AND a.user_id=?
                     AND a.active=1 AND m.active=1
                     AND (a.expires_at IS NULL OR a.expires_at > ?)""",
                (
                    session["credential_hash"],
                    session["tenant_id"],
                    session["user_id"],
                    now_utc(),
                ),
            ).fetchone()
        return dict(principal) if principal else None

    def revoke_web_session(self, session_id: str) -> bool:
        """Revoke one opaque browser session without revoking its backing API token."""
        if not isinstance(session_id, str) or not re.fullmatch(
            r"[A-Za-z0-9_-]{32,128}", session_id
        ):
            return False
        with self.connect() as db:
            cursor = db.execute(
                """UPDATE web_sessions SET revoked_at=?
                   WHERE session_hash=? AND revoked_at IS NULL""",
                (now_utc(), self._token_hash(session_id)),
            )
        return cursor.rowcount == 1

    def revoke_api_token(
        self,
        token: str,
        *,
        tenant_id: str,
        user_id: str,
    ) -> bool:
        """Revoke only a token owned by the authenticated user in the active tenant."""
        if not isinstance(token, str) or len(token.strip()) < 32:
            return False
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
                return False
            cursor = db.execute(
                """UPDATE api_tokens SET active=0
                   WHERE token_hash=? AND tenant_id=? AND user_id=? AND active=1""",
                (self._token_hash(token.strip()), tenant, user_id),
            )
        return cursor.rowcount == 1

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
            (url.rstrip("/") + "\n" + normalized).encode()
        ).hexdigest()
        lead_id = hashlib.sha256(
            (tenant + "\n" + fingerprint).encode()
        ).hexdigest()[:24]
        timestamp = observed_at or now_utc()
        assessment = analyze(text, product_terms=product_terms, location_terms=location_terms)
        domain_observed_at = timestamp
        try:
            parsed_observed_at = datetime.fromisoformat(str(timestamp).replace("Z", "+00:00"))
            if parsed_observed_at.tzinfo is None:
                domain_observed_at = None
        except (TypeError, ValueError):
            domain_observed_at = None
        evidence = DemandEvidence(
            source_id=lead_id,
            source_url=url,
            excerpt=text.strip()[:2_000],
            content_basis=EvidenceBasis.USER_PROVIDED,
            observed_at=domain_observed_at,
            page_read=False,
        )
        domain_signal = DemandSignal(
            signal_id=lead_id,
            signal_type=DemandSignalType(assessment["signal_type"]),
            evidence=evidence,
            product_fit=ProductFit.UNASSESSED,
            identity_status=IdentityStatus.UNKNOWN,
            classification_reason=assessment["summary"],
        )
        qualification = LeadQualification(
            signal_id=lead_id,
            product_fit=ProductFit.UNASSESSED,
            source_quality=SourceQuality.UNKNOWN,
            freshness=FreshnessStatus.UNKNOWN,
            identity_status=IdentityStatus.UNKNOWN,
            contactability=ContactabilityStatus.NOT_ASSESSED,
            missing_information=(
                "product_fit", "source_quality", "freshness",
                "identity", "contactability",
            ),
        )
        assessment["domain_signal"] = domain_signal.to_dict()
        assessment["qualification"] = qualification.to_dict()
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

    @staticmethod
    def _product_profile_row(row):
        if row is None:
            return None
        return {
            "id": row["id"],
            "name": row["name"],
            "profile": json.loads(row["profile_json"]),
            "created_at": row["created_at"],
            "updated_at": row["updated_at"],
        }

    def save_product_profile(self, profile: dict, *, tenant_id: str):
        if not isinstance(profile, dict):
            raise TypeError("profile must be an object")
        product = profile.get("product")
        if not isinstance(product, dict):
            raise TypeError("product profile is required")
        name = str(product.get("name") or "").strip()
        if not name or len(name) > 240:
            raise ValueError("product name is required and must be at most 240 characters")
        normalized_name = normalize(name)
        if not normalized_name:
            raise ValueError("product name is invalid")
        encoded = json.dumps(profile, ensure_ascii=False, separators=(",", ":"))
        if len(encoded) > 30000:
            raise ValueError("product profile is too large")
        tenant = self._tenant(tenant_id)
        now = now_utc()
        profile_id = "profile_" + uuid.uuid4().hex
        with self.connect() as db:
            active_tenant = db.execute(
                "SELECT 1 FROM tenants WHERE id=? AND active=1", (tenant,)
            ).fetchone()
            if not active_tenant:
                raise ValueError("active tenant is required")
            db.execute(
                """INSERT INTO product_profiles
                   (id, tenant_id, normalized_name, name, profile_json, created_at, updated_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?)
                   ON CONFLICT(tenant_id, normalized_name)
                   DO UPDATE SET name=excluded.name,
                                 profile_json=excluded.profile_json,
                                 updated_at=excluded.updated_at""",
                (profile_id, tenant, normalized_name, name, encoded, now, now),
            )
            row = db.execute(
                """SELECT id, name, profile_json, created_at, updated_at
                   FROM product_profiles
                   WHERE tenant_id=? AND normalized_name=?""",
                (tenant, normalized_name),
            ).fetchone()
        return self._product_profile_row(row)

    def list_product_profiles(self, *, tenant_id: str):
        tenant = self._tenant(tenant_id)
        with self.connect() as db:
            rows = db.execute(
                """SELECT id, name, profile_json, created_at, updated_at
                   FROM product_profiles WHERE tenant_id=?
                   ORDER BY updated_at DESC, id LIMIT 100""",
                (tenant,),
            ).fetchall()
        return [self._product_profile_row(row) for row in rows]

    def get_product_profile(self, profile_id: str, *, tenant_id: str):
        if not isinstance(profile_id, str) or not profile_id.strip():
            return None
        tenant = self._tenant(tenant_id)
        with self.connect() as db:
            row = db.execute(
                """SELECT id, name, profile_json, created_at, updated_at
                   FROM product_profiles WHERE id=? AND tenant_id=?""",
                (profile_id.strip(), tenant),
            ).fetchone()
        return self._product_profile_row(row)

    @staticmethod
    def _safe_discovery_source(source: dict):
        from urllib.parse import urlparse

        title = str(source.get("title") or "")[:300].strip()
        snippet = str(source.get("snippet") or "")[:1600].strip()
        source_url = validate_url(source.get("url", ""))
        parsed = urlparse(source_url)
        hostname = (parsed.hostname or "").lower().rstrip(".")
        if hostname == "localhost" or hostname.endswith((".localhost", ".local")):
            raise ValueError("discovery source URL is not public")
        try:
            address = ipaddress.ip_address(hostname)
        except ValueError:
            address = None
        if address is not None and not address.is_global:
            raise ValueError("discovery source URL is not public")
        evidence = source.get("lead_intent_evidence")
        safe_evidence = None
        if isinstance(evidence, dict):
            safe_evidence = {
                "phrase": str(evidence.get("phrase") or "")[:500],
                "basis": str(evidence.get("basis") or "")[:40],
                "signal_type": str(evidence.get("signal_type") or "")[:80],
                "product_fit": str(evidence.get("product_fit") or "unassessed")[:40],
            }
        providers = source.get("providers")
        queries = source.get("queries")
        return {
            "title": title,
            "url": source_url,
            "snippet": snippet,
            "platform": str(source.get("platform") or "web")[:80],
            "domain": str(source.get("domain") or "")[:253],
            "published_at": (
                str(source.get("published_at"))[:120]
                if source.get("published_at") is not None else None
            ),
            "page_fetched": source.get("page_fetched") is True,
            "readable_page_text_available": source.get("readable_page_text_available") is True,
            "providers": [
                str(value)[:80] for value in providers[:8] if isinstance(value, str)
            ] if isinstance(providers, list) else [],
            "queries": [
                str(value)[:500] for value in queries[:8] if isinstance(value, str)
            ] if isinstance(queries, list) else [],
            "lead_qualification": (
                "public_demand_signal"
                if source.get("lead_qualification") == "public_demand_signal"
                else "related_result_not_lead"
            ),
            "lead_intent_evidence": safe_evidence,
        }

    def save_discovery_run(self, profile_id: str, run: dict, *, tenant_id: str):
        if not isinstance(run, dict):
            raise TypeError("discovery run must be an object")
        tenant = self._tenant(tenant_id)
        profile = self.get_product_profile(profile_id, tenant_id=tenant)
        if profile is None:
            return None
        raw_sources = run.get("sources")
        raw_sources = raw_sources if isinstance(raw_sources, list) else []
        sources = [
            self._safe_discovery_source(item)
            for item in raw_sources[:30] if isinstance(item, dict)
        ]
        raw_queries = run.get("search_queries")
        if not isinstance(raw_queries, list):
            raw_queries = []
        queries = [str(item)[:500] for item in raw_queries[:8] if isinstance(item, str)]
        raw_report = run.get("search_report")
        raw_report = raw_report if isinstance(raw_report, dict) else {}
        lead_report = raw_report.get("lead_generation")
        report = {
            "lead_generation": lead_report if isinstance(lead_report, dict) else {},
            "pipeline_completion_status": str(
                raw_report.get("pipeline_completion_status")
                or run.get("pipeline_completion_status")
                or "unknown"
            )[:80],
            "search_outcome": str(raw_report.get("search_outcome") or "unknown")[:80],
            "search_attempted": raw_report.get("search_attempted"),
            "used_web_search": run.get("used_web_search") is True,
            "used_social_search": run.get("used_social_search") is True,
        }
        report_json = json.dumps(report, ensure_ascii=False, separators=(",", ":"))
        queries_json = json.dumps(queries, ensure_ascii=False, separators=(",", ":"))
        sources_json = json.dumps(sources, ensure_ascii=False, separators=(",", ":"))
        if sum(map(len, (report_json, queries_json, sources_json))) > 120000:
            raise ValueError("discovery result exceeds the storage limit")
        run_id = "discovery_" + uuid.uuid4().hex
        now = now_utc()
        answer = str(run.get("answer") or "")[:5000]
        kind = str(run.get("kind") or "lead_discovery")[:100]
        with self.connect() as db:
            db.execute(
                """INSERT INTO discovery_runs
                   (id, tenant_id, profile_id, answer, kind, search_queries_json,
                    search_report_json, sources_json, created_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    run_id, tenant, profile_id, answer, kind, queries_json,
                    report_json, sources_json, now,
                ),
            )
            row = db.execute(
                """SELECT r.id, r.tenant_id, r.profile_id, p.name AS profile_name,
                          r.answer, r.kind, r.search_queries_json, r.search_report_json,
                          r.sources_json, r.created_at
                   FROM discovery_runs r
                   JOIN product_profiles p
                     ON p.id=r.profile_id AND p.tenant_id=r.tenant_id
                   WHERE r.id=? AND r.tenant_id=?""",
                (run_id, tenant),
            ).fetchone()
        return self._discovery_run_row(row)

    @staticmethod
    def _discovery_run_row(row):
        if row is None:
            return None
        item = dict(row)
        item["search_queries"] = json.loads(item.pop("search_queries_json"))
        item["search_report"] = json.loads(item.pop("search_report_json"))
        item["sources"] = json.loads(item.pop("sources_json"))
        return item

    def list_discovery_runs(self, *, tenant_id: str, limit: int = 50):
        tenant = self._tenant(tenant_id)
        limit = max(1, min(int(limit), 100))
        with self.connect() as db:
            rows = db.execute(
                """SELECT r.id, r.tenant_id, r.profile_id, p.name AS profile_name,
                          r.answer, r.kind, r.search_queries_json, r.search_report_json,
                          r.sources_json, r.created_at
                   FROM discovery_runs r
                   JOIN product_profiles p
                     ON p.id=r.profile_id AND p.tenant_id=r.tenant_id
                   WHERE r.tenant_id=?
                   ORDER BY r.created_at DESC, r.id LIMIT ?""",
                (tenant, limit),
            ).fetchall()
        results = []
        for row in rows:
            item = self._discovery_run_row(row)
            results.append({
                "id": item["id"],
                "profile_id": item["profile_id"],
                "profile_name": item["profile_name"],
                "answer": item["answer"],
                "kind": item["kind"],
                "created_at": item["created_at"],
                "source_count": len(item["sources"]),
                "qualified_signal_count": sum(
                    source.get("lead_qualification") == "public_demand_signal"
                    for source in item["sources"]
                ),
                "pipeline_completion_status": item["search_report"].get(
                    "pipeline_completion_status", "unknown"
                ),
            })
        return results

    def get_discovery_run(self, run_id: str, *, tenant_id: str):
        if not isinstance(run_id, str) or not run_id.strip():
            return None
        tenant = self._tenant(tenant_id)
        with self.connect() as db:
            row = db.execute(
                """SELECT r.id, r.tenant_id, r.profile_id, p.name AS profile_name,
                          r.answer, r.kind, r.search_queries_json, r.search_report_json,
                          r.sources_json, r.created_at
                   FROM discovery_runs r
                   JOIN product_profiles p
                     ON p.id=r.profile_id AND p.tenant_id=r.tenant_id
                   WHERE r.id=? AND r.tenant_id=?""",
                (run_id.strip(), tenant),
            ).fetchone()
        return self._discovery_run_row(row)

    def save_discovery_signal(
        self, run_id: str, source_index: int, *, tenant_id: str
    ):
        if not isinstance(source_index, int) or isinstance(source_index, bool):
            return None
        run = self.get_discovery_run(run_id, tenant_id=tenant_id)
        if run is None or not 0 <= source_index < len(run["sources"]):
            return None
        source = run["sources"][source_index]
        if source.get("lead_qualification") != "public_demand_signal":
            return None
        evidence = source.get("lead_intent_evidence")
        if not isinstance(evidence, dict) or not str(evidence.get("phrase") or "").strip():
            return None
        profile = self.get_product_profile(run["profile_id"], tenant_id=tenant_id)
        if profile is None:
            return None
        product = profile["profile"].get("product", {})
        market = profile["profile"].get("market", {})
        product_terms = [
            str(item) for item in [product.get("name"), *(product.get("aliases") or [])]
            if isinstance(item, str) and item.strip()
        ]
        location_terms = [
            str(item) for item in (market.get("locations") or [])
            if isinstance(item, str) and item.strip()
        ]
        source_text = str(source.get("snippet") or source.get("title") or "").strip()
        if not source_text:
            return None
        note = (
            "Omarai public demand evidence | "
            + "phrase=" + str(evidence.get("phrase") or "")[:240]
            + " | basis=" + str(evidence.get("basis") or "unknown")[:40]
            + " | signal_type=" + str(evidence.get("signal_type") or "unknown")[:80]
            + " | profile=" + str(profile.get("name") or "")[:160]
            + " | run=" + run["id"]
        )
        return self.add(
            source_text[:MAX_TEXT],
            source["url"],
            str(source.get("platform") or "web")[:80],
            observed_at=now_utc(),
            note=note[:1000],
            product_terms=product_terms,
            location_terms=location_terms,
            tenant_id=tenant_id,
        )

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
