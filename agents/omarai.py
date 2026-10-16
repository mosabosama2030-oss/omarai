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
from urllib.parse import urlparse

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
    """Prefix spreadsheet formula-like values so exported data is not executed."""
    text = "" if value is None else str(value)
    if not text:
        return text
    first_non_space = text.lstrip(" \t\r\n")[:1]
    if text[0] in "\t\r\n" or first_non_space in {"=", "+", "-", "@"}:
        return "'" + text
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
    def __init__(self, path: str | Path | None = None):
        self.path = Path(path or Path.home()/".omarai"/"omarai.sqlite3").expanduser()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as db:
            db.execute("""CREATE TABLE IF NOT EXISTS leads (
            id TEXT PRIMARY KEY, fingerprint TEXT UNIQUE NOT NULL, text TEXT NOT NULL,
            source_url TEXT NOT NULL, platform TEXT NOT NULL, observed_at TEXT NOT NULL,
            assessment TEXT NOT NULL, status TEXT NOT NULL, note TEXT NOT NULL,
            created_at TEXT NOT NULL, updated_at TEXT NOT NULL)""")
            db.execute("CREATE INDEX IF NOT EXISTS leads_status_idx ON leads(status, created_at DESC)")
    def connect(self):
        db = sqlite3.connect(self.path, timeout=10)
        db.row_factory = sqlite3.Row
        return db
    def add(self, text: str, source_url: str, platform: str="manual", observed_at: str | None=None, note: str="", product_terms=(), location_terms=()):
        if not isinstance(text, str) or not text.strip():
            raise ValueError("text is required")
        if len(text) > MAX_TEXT:
            raise ValueError("text is too long")
        url = validate_url(source_url)
        normalized = normalize(text)
        fingerprint = hashlib.sha256((url.rstrip("/") + "\n" + normalized).encode()).hexdigest()
        lead_id = fingerprint[:24]
        timestamp = observed_at or now_utc()
        assessment = analyze(text, product_terms=product_terms, location_terms=location_terms)
        now = now_utc()
        with self.connect() as db:
            cursor = db.execute("""INSERT OR IGNORE INTO leads
            (id,fingerprint,text,source_url,platform,observed_at,assessment,status,note,created_at,updated_at)
            VALUES(?,?,?,?,?,?,?,?,?,?,?)""", (lead_id,fingerprint,text.strip(),url,str(platform)[:80],timestamp,json.dumps(assessment,ensure_ascii=False),"new",str(note)[:1000],now,now))
            row = db.execute("SELECT * FROM leads WHERE id=?", (lead_id,)).fetchone()
        return self.to_dict(row), cursor.rowcount == 1
    @staticmethod
    def to_dict(row):
        item = dict(row)
        item["assessment"] = json.loads(item["assessment"])
        return item
    def list(self, status: str | None=None, limit: int=100):
        limit = max(1,min(int(limit),500))
        with self.connect() as db:
            rows = db.execute("SELECT * FROM leads WHERE (? IS NULL OR status=?) ORDER BY created_at DESC LIMIT ?",(status,status,limit)).fetchall()
        return [self.to_dict(r) for r in rows]
    def update_status(self, lead_id: str, status: str):
        allowed={"new","qualified","contacted","converted","rejected","needs_review"}
        if status not in allowed:
            raise ValueError("unsupported status")
        with self.connect() as db:
            db.execute("UPDATE leads SET status=?,updated_at=? WHERE id=?",(status,now_utc(),lead_id))
            row=db.execute("SELECT * FROM leads WHERE id=?",(lead_id,)).fetchone()
        return self.to_dict(row) if row else None
    def import_csv(self, filename: str):
        results={"created":0,"duplicates":0,"errors":[]}
        with open(filename, newline="", encoding="utf-8-sig") as stream:
            reader=csv.DictReader(stream)
            required={"text","source_url","platform"}
            if not reader.fieldnames or not required.issubset(reader.fieldnames):
                raise ValueError("CSV must contain text,source_url,platform columns")
            for line,row in enumerate(reader,2):
                try:
                    _,created=self.add(row["text"],row["source_url"],row["platform"],row.get("observed_at") or None,row.get("note") or "")
                    results["created" if created else "duplicates"] += 1
                except (ValueError, TypeError) as exc:
                    results["errors"].append({"line":line,"error":str(exc)})
        return results
    def export_csv(self, filename: str):
        rows=self.list(limit=500)
        with open(filename,"w",newline="",encoding="utf-8-sig") as stream:
            fields=["id","text","source_url","platform","observed_at","assessment","status","note","created_at"]
            writer=csv.DictWriter(stream,fieldnames=fields)
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
