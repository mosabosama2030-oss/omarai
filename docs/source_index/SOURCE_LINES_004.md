# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **004**
- سجلات الأسطر: **800**
- النطاق: SRC-C9CF9B54F8-L000032 إلى SRC-3D565C3B85-L000126
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-C9CF9B54F8 — [agents/omarai.py](../../agents/omarai.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-C9CF9B54F8-L000032](../../agents/omarai.py#L32) | 32 | `"def now_utc() -> str:"` | — |
| [SRC-C9CF9B54F8-L000033](../../agents/omarai.py#L33) | 33 | `"    return datetime.now(UTC).isoformat(timespec=\"seconds\").replace(\"+00:00\", \"Z\")"` | — |
| [SRC-C9CF9B54F8-L000034](../../agents/omarai.py#L34) | 34 | `""` | — |
| [SRC-C9CF9B54F8-L000035](../../agents/omarai.py#L35) | 35 | `"def _csv_safe_cell(value: object) -> str:"` | — |
| [SRC-C9CF9B54F8-L000036](../../agents/omarai.py#L36) | 36 | `"    \"\"\"Prefix spreadsheet formulas even when hidden whitespace/control chars precede them.\"\"\""` | — |
| [SRC-C9CF9B54F8-L000037](../../agents/omarai.py#L37) | 37 | `"    text = \"\" if value is None else str(value)"` | — |
| [SRC-C9CF9B54F8-L000038](../../agents/omarai.py#L38) | 38 | `"    if not text:"` | — |
| [SRC-C9CF9B54F8-L000039](../../agents/omarai.py#L39) | 39 | `"        return text"` | — |
| [SRC-C9CF9B54F8-L000040](../../agents/omarai.py#L40) | 40 | `"    index = 0"` | — |
| [SRC-C9CF9B54F8-L000041](../../agents/omarai.py#L41) | 41 | `"    while index < len(text) and ("` | — |
| [SRC-C9CF9B54F8-L000042](../../agents/omarai.py#L42) | 42 | `"        text[index].isspace()"` | — |
| [SRC-C9CF9B54F8-L000043](../../agents/omarai.py#L43) | 43 | `"        or unicodedata.category(text[index]) in {\"Cc\", \"Cf\"}"` | — |
| [SRC-C9CF9B54F8-L000044](../../agents/omarai.py#L44) | 44 | `"    ):"` | — |
| [SRC-C9CF9B54F8-L000045](../../agents/omarai.py#L45) | 45 | `"        index += 1"` | — |
| [SRC-C9CF9B54F8-L000046](../../agents/omarai.py#L46) | 46 | `"    first_non_format = text[index:index + 1]"` | — |
| [SRC-C9CF9B54F8-L000047](../../agents/omarai.py#L47) | 47 | `"    formula_prefixes = {\"=\", \"+\", \"-\", \"@\", \"＝\", \"＋\", \"－\", \"＠\"}"` | — |
| [SRC-C9CF9B54F8-L000048](../../agents/omarai.py#L48) | 48 | `"    if text[0] in \"\\t\\r\\n\" or first_non_format in formula_prefixes:"` | — |
| [SRC-C9CF9B54F8-L000049](../../agents/omarai.py#L49) | 49 | `"        # OWASP notes that a tab inside the quoted CSV field is more resilient"` | — |
| [SRC-C9CF9B54F8-L000050](../../agents/omarai.py#L50) | 50 | `"        # in Excel than an apostrophe, although no CSV mitigation is universal."` | — |
| [SRC-C9CF9B54F8-L000051](../../agents/omarai.py#L51) | 51 | `"        return \"\\t\" + text"` | — |
| [SRC-C9CF9B54F8-L000052](../../agents/omarai.py#L52) | 52 | `"    return text"` | — |
| [SRC-C9CF9B54F8-L000053](../../agents/omarai.py#L53) | 53 | `""` | — |
| [SRC-C9CF9B54F8-L000054](../../agents/omarai.py#L54) | 54 | `"def analyze(text: str, product_terms=(), location_terms=()) -> dict:"` | — |
| [SRC-C9CF9B54F8-L000055](../../agents/omarai.py#L55) | 55 | `"    if not isinstance(text, str) or not text.strip():"` | — |
| [SRC-C9CF9B54F8-L000056](../../agents/omarai.py#L56) | 56 | `"        raise ValueError(\"text must not be empty\")"` | — |
| [SRC-C9CF9B54F8-L000057](../../agents/omarai.py#L57) | 57 | `"    if len(text) > MAX_TEXT:"` | — |
| [SRC-C9CF9B54F8-L000058](../../agents/omarai.py#L58) | 58 | `"        raise ValueError(f\"text must be at most {MAX_TEXT} characters\")"` | — |
| [SRC-C9CF9B54F8-L000059](../../agents/omarai.py#L59) | 59 | `"    body = normalize(text)"` | — |
| [SRC-C9CF9B54F8-L000060](../../agents/omarai.py#L60) | 60 | `"    excluded = [p for p in NOT_BUYER if normalize(p) in body]"` | — |
| [SRC-C9CF9B54F8-L000061](../../agents/omarai.py#L61) | 61 | `"    if excluded:"` | — |
| [SRC-C9CF9B54F8-L000062](../../agents/omarai.py#L62) | 62 | `"        return {\"score\": 0, \"label\": \"not_buyer_signal\", \"summary\": \"قد لا تكون إشارة شراء مباشرة؛ راجع النص يدويًا.\", \"matched_signals\": [{\"phrase\": p, \"category\": \"exclusion\", \"points\": 0} for p in excluded], \"warnings\": [\"تصنيف أولي وليس حكمًا نهائيًا.\"]}"` | — |
| [SRC-C9CF9B54F8-L000063](../../agents/omarai.py#L63) | 63 | `"    matches = []"` | — |
| [SRC-C9CF9B54F8-L000064](../../agents/omarai.py#L64) | 64 | `"    for category, (points, phrases) in SIGNALS.items():"` | — |
| [SRC-C9CF9B54F8-L000065](../../agents/omarai.py#L65) | 65 | `"        found = next((p for p in phrases if normalize(p) in body), None)"` | — |
| [SRC-C9CF9B54F8-L000066](../../agents/omarai.py#L66) | 66 | `"        if found:"` | — |
| [SRC-C9CF9B54F8-L000067](../../agents/omarai.py#L67) | 67 | `"            matches.append({\"phrase\": found, \"category\": category, \"points\": points})"` | — |
| [SRC-C9CF9B54F8-L000068](../../agents/omarai.py#L68) | 68 | `"    for category, terms in ((\"product_context\", product_terms), (\"location_context\", location_terms)):"` | — |
| [SRC-C9CF9B54F8-L000069](../../agents/omarai.py#L69) | 69 | `"        found = next((normalize(t) for t in terms if isinstance(t, str) and normalize(t) and normalize(t) in body), None)"` | — |
| [SRC-C9CF9B54F8-L000070](../../agents/omarai.py#L70) | 70 | `"        if found:"` | — |
| [SRC-C9CF9B54F8-L000071](../../agents/omarai.py#L71) | 71 | `"            matches.append({\"phrase\": found, \"category\": category, \"points\": 10})"` | — |
| [SRC-C9CF9B54F8-L000072](../../agents/omarai.py#L72) | 72 | `"    score = min(100, sum(x[\"points\"] for x in matches))"` | — |
| [SRC-C9CF9B54F8-L000073](../../agents/omarai.py#L73) | 73 | `"    label = \"high_intent\" if score >= 55 and any(x[\"category\"] == \"high\" for x in matches) else \"medium_intent\" if score >= 40 else \"early_research\" if score >= 20 else \"unclear\""` | — |
| [SRC-C9CF9B54F8-L000074](../../agents/omarai.py#L74) | 74 | `"    return {\"score\": score, \"label\": label, \"summary\": {\"high_intent\":\"إشارة قوية نسبيًا وفق قواعد بسيطة وتحتاج مراجعة بشرية.\",\"medium_intent\":\"مؤشرات اهتمام تستحق التأهيل والتحقق.\",\"early_research\":\"اهتمام مبكر؛ ليس عميلًا مؤهلًا بعد.\",\"unclear\":\"لا توجد مؤشرات كافية.\"}[label], \"matched_signals\": matches, \"warnings\": [\"الدرجة ليست احتمالًا إحصائيًا للشراء.\", \"لا تثبت هوية الكاتب أو قدرته على الدفع أو نيته.\", \"استخدم مصادر عامة ومسموحًا بمعالجتها فقط.\"]}"` | — |
| [SRC-C9CF9B54F8-L000075](../../agents/omarai.py#L75) | 75 | `""` | — |
| [SRC-C9CF9B54F8-L000076](../../agents/omarai.py#L76) | 76 | `"def validate_url(url: str) -> str:"` | — |
| [SRC-C9CF9B54F8-L000077](../../agents/omarai.py#L77) | 77 | `"    parsed = urlparse(str(url or \"\").strip())"` | — |
| [SRC-C9CF9B54F8-L000078](../../agents/omarai.py#L78) | 78 | `"    if parsed.scheme not in (\"http\", \"https\") or not parsed.netloc or parsed.username or parsed.password:"` | — |
| [SRC-C9CF9B54F8-L000079](../../agents/omarai.py#L79) | 79 | `"        raise ValueError(\"source_url must be an absolute http(s) URL without embedded credentials\")"` | — |
| [SRC-C9CF9B54F8-L000080](../../agents/omarai.py#L80) | 80 | `"    if len(url) > 2048:"` | — |
| [SRC-C9CF9B54F8-L000081](../../agents/omarai.py#L81) | 81 | `"        raise ValueError(\"source_url is too long\")"` | — |
| [SRC-C9CF9B54F8-L000082](../../agents/omarai.py#L82) | 82 | `"    return url.strip()"` | — |
| [SRC-C9CF9B54F8-L000083](../../agents/omarai.py#L83) | 83 | `""` | — |
| [SRC-C9CF9B54F8-L000084](../../agents/omarai.py#L84) | 84 | `"class LeadStore:"` | — |
| [SRC-C9CF9B54F8-L000085](../../agents/omarai.py#L85) | 85 | `"    \"\"\"Tenant-scoped SQLite lead storage with a safe single-company bootstrap.\"\"\""` | — |
| [SRC-C9CF9B54F8-L000086](../../agents/omarai.py#L86) | 86 | `""` | — |
| [SRC-C9CF9B54F8-L000087](../../agents/omarai.py#L87) | 87 | `"    ALLOWED_STATUSES = frozenset({"` | — |
| [SRC-C9CF9B54F8-L000088](../../agents/omarai.py#L88) | 88 | `"        \"new\", \"qualified\", \"contacted\", \"converted\", \"rejected\", \"needs_review\""` | — |
| [SRC-C9CF9B54F8-L000089](../../agents/omarai.py#L89) | 89 | `"    })"` | — |
| [SRC-C9CF9B54F8-L000090](../../agents/omarai.py#L90) | 90 | `"    ALLOWED_ROLES = frozenset({\"owner\", \"admin\", \"manager\", \"sales_agent\", \"viewer\"})"` | — |
| [SRC-C9CF9B54F8-L000091](../../agents/omarai.py#L91) | 91 | `""` | — |
| [SRC-C9CF9B54F8-L000092](../../agents/omarai.py#L92) | 92 | `"    def __init__(self, path: str \| Path \| None = None):"` | — |
| [SRC-C9CF9B54F8-L000093](../../agents/omarai.py#L93) | 93 | `"        self.path = Path(path or Path.home() / \".omarai\" / \"omarai.sqlite3\").expanduser()"` | — |
| [SRC-C9CF9B54F8-L000094](../../agents/omarai.py#L94) | 94 | `"        self.path.parent.mkdir(parents=True, exist_ok=True)"` | — |
| [SRC-C9CF9B54F8-L000095](../../agents/omarai.py#L95) | 95 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000096](../../agents/omarai.py#L96) | 96 | `"            self._initialize_schema(db)"` | — |
| [SRC-C9CF9B54F8-L000097](../../agents/omarai.py#L97) | 97 | `""` | — |
| [SRC-C9CF9B54F8-L000098](../../agents/omarai.py#L98) | 98 | `"    def connect(self):"` | — |
| [SRC-C9CF9B54F8-L000099](../../agents/omarai.py#L99) | 99 | `"        db = sqlite3.connect(self.path, timeout=10)"` | — |
| [SRC-C9CF9B54F8-L000100](../../agents/omarai.py#L100) | 100 | `"        db.row_factory = sqlite3.Row"` | — |
| [SRC-C9CF9B54F8-L000101](../../agents/omarai.py#L101) | 101 | `"        db.execute(\"PRAGMA foreign_keys = ON\")"` | — |
| [SRC-C9CF9B54F8-L000102](../../agents/omarai.py#L102) | 102 | `"        return db"` | — |
| [SRC-C9CF9B54F8-L000103](../../agents/omarai.py#L103) | 103 | `""` | — |
| [SRC-C9CF9B54F8-L000104](../../agents/omarai.py#L104) | 104 | `"    @staticmethod"` | — |
| [SRC-C9CF9B54F8-L000105](../../agents/omarai.py#L105) | 105 | `"    def _create_leads_table(db):"` | — |
| [SRC-C9CF9B54F8-L000106](../../agents/omarai.py#L106) | 106 | `"        db.execute("` | — |
| [SRC-C9CF9B54F8-L000107](../../agents/omarai.py#L107) | 107 | `"            \"\"\"CREATE TABLE IF NOT EXISTS leads ("` | — |
| [SRC-C9CF9B54F8-L000108](../../agents/omarai.py#L108) | 108 | `"                id TEXT PRIMARY KEY,"` | — |
| [SRC-C9CF9B54F8-L000109](../../agents/omarai.py#L109) | 109 | `"                tenant_id TEXT NOT NULL REFERENCES tenants(id),"` | — |
| [SRC-C9CF9B54F8-L000110](../../agents/omarai.py#L110) | 110 | `"                fingerprint TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000111](../../agents/omarai.py#L111) | 111 | `"                text TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000112](../../agents/omarai.py#L112) | 112 | `"                source_url TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000113](../../agents/omarai.py#L113) | 113 | `"                platform TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000114](../../agents/omarai.py#L114) | 114 | `"                observed_at TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000115](../../agents/omarai.py#L115) | 115 | `"                assessment TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000116](../../agents/omarai.py#L116) | 116 | `"                status TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000117](../../agents/omarai.py#L117) | 117 | `"                note TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000118](../../agents/omarai.py#L118) | 118 | `"                created_at TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000119](../../agents/omarai.py#L119) | 119 | `"                updated_at TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000120](../../agents/omarai.py#L120) | 120 | `"                UNIQUE (tenant_id, fingerprint)"` | — |
| [SRC-C9CF9B54F8-L000121](../../agents/omarai.py#L121) | 121 | `"            )\"\"\""` | — |
| [SRC-C9CF9B54F8-L000122](../../agents/omarai.py#L122) | 122 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000123](../../agents/omarai.py#L123) | 123 | `""` | — |
| [SRC-C9CF9B54F8-L000124](../../agents/omarai.py#L124) | 124 | `"    def _initialize_schema(self, db):"` | — |
| [SRC-C9CF9B54F8-L000125](../../agents/omarai.py#L125) | 125 | `"        db.execute("` | — |
| [SRC-C9CF9B54F8-L000126](../../agents/omarai.py#L126) | 126 | `"            \"\"\"CREATE TABLE IF NOT EXISTS tenants ("` | — |
| [SRC-C9CF9B54F8-L000127](../../agents/omarai.py#L127) | 127 | `"                id TEXT PRIMARY KEY,"` | — |
| [SRC-C9CF9B54F8-L000128](../../agents/omarai.py#L128) | 128 | `"                name TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000129](../../agents/omarai.py#L129) | 129 | `"                slug TEXT NOT NULL UNIQUE,"` | — |
| [SRC-C9CF9B54F8-L000130](../../agents/omarai.py#L130) | 130 | `"                active INTEGER NOT NULL DEFAULT 1,"` | — |
| [SRC-C9CF9B54F8-L000131](../../agents/omarai.py#L131) | 131 | `"                created_at TEXT NOT NULL"` | — |
| [SRC-C9CF9B54F8-L000132](../../agents/omarai.py#L132) | 132 | `"            )\"\"\""` | — |
| [SRC-C9CF9B54F8-L000133](../../agents/omarai.py#L133) | 133 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000134](../../agents/omarai.py#L134) | 134 | `"        db.execute("` | — |
| [SRC-C9CF9B54F8-L000135](../../agents/omarai.py#L135) | 135 | `"            \"\"\"CREATE TABLE IF NOT EXISTS users ("` | — |
| [SRC-C9CF9B54F8-L000136](../../agents/omarai.py#L136) | 136 | `"                id TEXT PRIMARY KEY,"` | — |
| [SRC-C9CF9B54F8-L000137](../../agents/omarai.py#L137) | 137 | `"                email TEXT NOT NULL UNIQUE COLLATE NOCASE,"` | — |
| [SRC-C9CF9B54F8-L000138](../../agents/omarai.py#L138) | 138 | `"                display_name TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000139](../../agents/omarai.py#L139) | 139 | `"                active INTEGER NOT NULL DEFAULT 1,"` | — |
| [SRC-C9CF9B54F8-L000140](../../agents/omarai.py#L140) | 140 | `"                created_at TEXT NOT NULL"` | — |
| [SRC-C9CF9B54F8-L000141](../../agents/omarai.py#L141) | 141 | `"            )\"\"\""` | — |
| [SRC-C9CF9B54F8-L000142](../../agents/omarai.py#L142) | 142 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000143](../../agents/omarai.py#L143) | 143 | `"        db.execute("` | — |
| [SRC-C9CF9B54F8-L000144](../../agents/omarai.py#L144) | 144 | `"            \"\"\"CREATE TABLE IF NOT EXISTS tenant_memberships ("` | — |
| [SRC-C9CF9B54F8-L000145](../../agents/omarai.py#L145) | 145 | `"                tenant_id TEXT NOT NULL REFERENCES tenants(id),"` | — |
| [SRC-C9CF9B54F8-L000146](../../agents/omarai.py#L146) | 146 | `"                user_id TEXT NOT NULL REFERENCES users(id),"` | — |
| [SRC-C9CF9B54F8-L000147](../../agents/omarai.py#L147) | 147 | `"                role TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000148](../../agents/omarai.py#L148) | 148 | `"                active INTEGER NOT NULL DEFAULT 1,"` | — |
| [SRC-C9CF9B54F8-L000149](../../agents/omarai.py#L149) | 149 | `"                created_at TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000150](../../agents/omarai.py#L150) | 150 | `"                PRIMARY KEY (tenant_id, user_id)"` | — |
| [SRC-C9CF9B54F8-L000151](../../agents/omarai.py#L151) | 151 | `"            )\"\"\""` | — |
| [SRC-C9CF9B54F8-L000152](../../agents/omarai.py#L152) | 152 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000153](../../agents/omarai.py#L153) | 153 | `"        db.execute("` | — |
| [SRC-C9CF9B54F8-L000154](../../agents/omarai.py#L154) | 154 | `"            \"\"\"CREATE TABLE IF NOT EXISTS api_tokens ("` | — |
| [SRC-C9CF9B54F8-L000155](../../agents/omarai.py#L155) | 155 | `"                token_hash TEXT PRIMARY KEY,"` | — |
| [SRC-C9CF9B54F8-L000156](../../agents/omarai.py#L156) | 156 | `"                tenant_id TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000157](../../agents/omarai.py#L157) | 157 | `"                user_id TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000158](../../agents/omarai.py#L158) | 158 | `"                label TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000159](../../agents/omarai.py#L159) | 159 | `"                active INTEGER NOT NULL DEFAULT 1,"` | — |
| [SRC-C9CF9B54F8-L000160](../../agents/omarai.py#L160) | 160 | `"                created_at TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000161](../../agents/omarai.py#L161) | 161 | `"                expires_at TEXT,"` | — |
| [SRC-C9CF9B54F8-L000162](../../agents/omarai.py#L162) | 162 | `"                FOREIGN KEY (tenant_id, user_id)"` | — |
| [SRC-C9CF9B54F8-L000163](../../agents/omarai.py#L163) | 163 | `"                    REFERENCES tenant_memberships(tenant_id, user_id)"` | — |
| [SRC-C9CF9B54F8-L000164](../../agents/omarai.py#L164) | 164 | `"            )\"\"\""` | — |
| [SRC-C9CF9B54F8-L000165](../../agents/omarai.py#L165) | 165 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000166](../../agents/omarai.py#L166) | 166 | `""` | — |
| [SRC-C9CF9B54F8-L000167](../../agents/omarai.py#L167) | 167 | `"        now = now_utc()"` | — |
| [SRC-C9CF9B54F8-L000168](../../agents/omarai.py#L168) | 168 | `"        db.execute("` | — |
| [SRC-C9CF9B54F8-L000169](../../agents/omarai.py#L169) | 169 | `"            \"\"\"INSERT OR IGNORE INTO tenants (id, name, slug, active, created_at)"` | — |
| [SRC-C9CF9B54F8-L000170](../../agents/omarai.py#L170) | 170 | `"               VALUES (?, ?, ?, 1, ?)\"\"\","` | — |
| [SRC-C9CF9B54F8-L000171](../../agents/omarai.py#L171) | 171 | `"            (DEFAULT_TENANT_ID, \"Omarai Workspace\", \"omarai-default\", now),"` | — |
| [SRC-C9CF9B54F8-L000172](../../agents/omarai.py#L172) | 172 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000173](../../agents/omarai.py#L173) | 173 | `"        db.execute("` | — |
| [SRC-C9CF9B54F8-L000174](../../agents/omarai.py#L174) | 174 | `"            \"\"\"INSERT OR IGNORE INTO users"` | — |
| [SRC-C9CF9B54F8-L000175](../../agents/omarai.py#L175) | 175 | `"               (id, email, display_name, active, created_at)"` | — |
| [SRC-C9CF9B54F8-L000176](../../agents/omarai.py#L176) | 176 | `"               VALUES (?, ?, ?, 1, ?)\"\"\","` | — |
| [SRC-C9CF9B54F8-L000177](../../agents/omarai.py#L177) | 177 | `"            (DEFAULT_USER_ID, \"local-admin@omarai.invalid\", \"Omarai Local Admin\", now),"` | — |
| [SRC-C9CF9B54F8-L000178](../../agents/omarai.py#L178) | 178 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000179](../../agents/omarai.py#L179) | 179 | `"        db.execute("` | — |
| [SRC-C9CF9B54F8-L000180](../../agents/omarai.py#L180) | 180 | `"            \"\"\"INSERT OR IGNORE INTO tenant_memberships"` | — |
| [SRC-C9CF9B54F8-L000181](../../agents/omarai.py#L181) | 181 | `"               (tenant_id, user_id, role, active, created_at)"` | — |
| [SRC-C9CF9B54F8-L000182](../../agents/omarai.py#L182) | 182 | `"               VALUES (?, ?, 'owner', 1, ?)\"\"\","` | — |
| [SRC-C9CF9B54F8-L000183](../../agents/omarai.py#L183) | 183 | `"            (DEFAULT_TENANT_ID, DEFAULT_USER_ID, now),"` | — |
| [SRC-C9CF9B54F8-L000184](../../agents/omarai.py#L184) | 184 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000185](../../agents/omarai.py#L185) | 185 | `""` | — |
| [SRC-C9CF9B54F8-L000186](../../agents/omarai.py#L186) | 186 | `"        table = db.execute("` | — |
| [SRC-C9CF9B54F8-L000187](../../agents/omarai.py#L187) | 187 | `"            \"SELECT 1 FROM sqlite_master WHERE type='table' AND name='leads'\""` | — |
| [SRC-C9CF9B54F8-L000188](../../agents/omarai.py#L188) | 188 | `"        ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000189](../../agents/omarai.py#L189) | 189 | `"        if table:"` | — |
| [SRC-C9CF9B54F8-L000190](../../agents/omarai.py#L190) | 190 | `"            columns = {"` | — |
| [SRC-C9CF9B54F8-L000191](../../agents/omarai.py#L191) | 191 | `"                row[\"name\"] for row in db.execute(\"PRAGMA table_info(leads)\").fetchall()"` | — |
| [SRC-C9CF9B54F8-L000192](../../agents/omarai.py#L192) | 192 | `"            }"` | — |
| [SRC-C9CF9B54F8-L000193](../../agents/omarai.py#L193) | 193 | `"            unique_fingerprint = False"` | — |
| [SRC-C9CF9B54F8-L000194](../../agents/omarai.py#L194) | 194 | `"            for index in db.execute(\"PRAGMA index_list(leads)\").fetchall():"` | — |
| [SRC-C9CF9B54F8-L000195](../../agents/omarai.py#L195) | 195 | `"                if not index[\"unique\"]:"` | — |
| [SRC-C9CF9B54F8-L000196](../../agents/omarai.py#L196) | 196 | `"                    continue"` | — |
| [SRC-C9CF9B54F8-L000197](../../agents/omarai.py#L197) | 197 | `"                index_columns = ["` | — |
| [SRC-C9CF9B54F8-L000198](../../agents/omarai.py#L198) | 198 | `"                    row[\"name\"]"` | — |
| [SRC-C9CF9B54F8-L000199](../../agents/omarai.py#L199) | 199 | `"                    for row in db.execute("` | — |
| [SRC-C9CF9B54F8-L000200](../../agents/omarai.py#L200) | 200 | `"                        f\"PRAGMA index_info('{index['name']}')\""` | — |
| [SRC-C9CF9B54F8-L000201](../../agents/omarai.py#L201) | 201 | `"                    ).fetchall()"` | — |
| [SRC-C9CF9B54F8-L000202](../../agents/omarai.py#L202) | 202 | `"                ]"` | — |
| [SRC-C9CF9B54F8-L000203](../../agents/omarai.py#L203) | 203 | `"                if index_columns == [\"fingerprint\"]:"` | — |
| [SRC-C9CF9B54F8-L000204](../../agents/omarai.py#L204) | 204 | `"                    unique_fingerprint = True"` | — |
| [SRC-C9CF9B54F8-L000205](../../agents/omarai.py#L205) | 205 | `"                    break"` | — |
| [SRC-C9CF9B54F8-L000206](../../agents/omarai.py#L206) | 206 | `"            if \"tenant_id\" not in columns or unique_fingerprint:"` | — |
| [SRC-C9CF9B54F8-L000207](../../agents/omarai.py#L207) | 207 | `"                db.execute(\"ALTER TABLE leads RENAME TO leads_legacy_migration\")"` | — |
| [SRC-C9CF9B54F8-L000208](../../agents/omarai.py#L208) | 208 | `"                self._create_leads_table(db)"` | — |
| [SRC-C9CF9B54F8-L000209](../../agents/omarai.py#L209) | 209 | `"                legacy_columns = {"` | — |
| [SRC-C9CF9B54F8-L000210](../../agents/omarai.py#L210) | 210 | `"                    row[\"name\"]"` | — |
| [SRC-C9CF9B54F8-L000211](../../agents/omarai.py#L211) | 211 | `"                    for row in db.execute("` | — |
| [SRC-C9CF9B54F8-L000212](../../agents/omarai.py#L212) | 212 | `"                        \"PRAGMA table_info(leads_legacy_migration)\""` | — |
| [SRC-C9CF9B54F8-L000213](../../agents/omarai.py#L213) | 213 | `"                    ).fetchall()"` | — |
| [SRC-C9CF9B54F8-L000214](../../agents/omarai.py#L214) | 214 | `"                }"` | — |
| [SRC-C9CF9B54F8-L000215](../../agents/omarai.py#L215) | 215 | `"                tenant_expression = ("` | — |
| [SRC-C9CF9B54F8-L000216](../../agents/omarai.py#L216) | 216 | `"                    \"tenant_id\" if \"tenant_id\" in legacy_columns else \"?\""` | — |
| [SRC-C9CF9B54F8-L000217](../../agents/omarai.py#L217) | 217 | `"                )"` | — |
| [SRC-C9CF9B54F8-L000218](../../agents/omarai.py#L218) | 218 | `"                if tenant_expression == \"?\":"` | — |
| [SRC-C9CF9B54F8-L000219](../../agents/omarai.py#L219) | 219 | `"                    db.execute("` | — |
| [SRC-C9CF9B54F8-L000220](../../agents/omarai.py#L220) | 220 | `"                        \"\"\"INSERT OR IGNORE INTO leads"` | — |
| [SRC-C9CF9B54F8-L000221](../../agents/omarai.py#L221) | 221 | `"                            (id, tenant_id, fingerprint, text, source_url, platform,"` | — |
| [SRC-C9CF9B54F8-L000222](../../agents/omarai.py#L222) | 222 | `"                             observed_at, assessment, status, note, created_at, updated_at)"` | — |
| [SRC-C9CF9B54F8-L000223](../../agents/omarai.py#L223) | 223 | `"                            SELECT id, ?, fingerprint, text, source_url, platform,"` | — |
| [SRC-C9CF9B54F8-L000224](../../agents/omarai.py#L224) | 224 | `"                                   observed_at, assessment, status, note, created_at, updated_at"` | — |
| [SRC-C9CF9B54F8-L000225](../../agents/omarai.py#L225) | 225 | `"                            FROM leads_legacy_migration\"\"\","` | — |
| [SRC-C9CF9B54F8-L000226](../../agents/omarai.py#L226) | 226 | `"                        (DEFAULT_TENANT_ID,),"` | — |
| [SRC-C9CF9B54F8-L000227](../../agents/omarai.py#L227) | 227 | `"                    )"` | — |
| [SRC-C9CF9B54F8-L000228](../../agents/omarai.py#L228) | 228 | `"                else:"` | — |
| [SRC-C9CF9B54F8-L000229](../../agents/omarai.py#L229) | 229 | `"                    db.execute("` | — |
| [SRC-C9CF9B54F8-L000230](../../agents/omarai.py#L230) | 230 | `"                        \"\"\"INSERT OR IGNORE INTO leads"` | — |
| [SRC-C9CF9B54F8-L000231](../../agents/omarai.py#L231) | 231 | `"                            (id, tenant_id, fingerprint, text, source_url, platform,"` | — |
| [SRC-C9CF9B54F8-L000232](../../agents/omarai.py#L232) | 232 | `"                             observed_at, assessment, status, note, created_at, updated_at)"` | — |
| [SRC-C9CF9B54F8-L000233](../../agents/omarai.py#L233) | 233 | `"                            SELECT id, tenant_id, fingerprint, text, source_url, platform,"` | — |
| [SRC-C9CF9B54F8-L000234](../../agents/omarai.py#L234) | 234 | `"                                   observed_at, assessment, status, note, created_at, updated_at"` | — |
| [SRC-C9CF9B54F8-L000235](../../agents/omarai.py#L235) | 235 | `"                            FROM leads_legacy_migration\"\"\""` | — |
| [SRC-C9CF9B54F8-L000236](../../agents/omarai.py#L236) | 236 | `"                    )"` | — |
| [SRC-C9CF9B54F8-L000237](../../agents/omarai.py#L237) | 237 | `"                legacy_count = db.execute("` | — |
| [SRC-C9CF9B54F8-L000238](../../agents/omarai.py#L238) | 238 | `"                    \"SELECT COUNT(*) FROM leads_legacy_migration\""` | — |
| [SRC-C9CF9B54F8-L000239](../../agents/omarai.py#L239) | 239 | `"                ).fetchone()[0]"` | — |
| [SRC-C9CF9B54F8-L000240](../../agents/omarai.py#L240) | 240 | `"                migrated_count = db.execute("` | — |
| [SRC-C9CF9B54F8-L000241](../../agents/omarai.py#L241) | 241 | `"                    \"SELECT COUNT(*) FROM leads\""` | — |
| [SRC-C9CF9B54F8-L000242](../../agents/omarai.py#L242) | 242 | `"                ).fetchone()[0]"` | — |
| [SRC-C9CF9B54F8-L000243](../../agents/omarai.py#L243) | 243 | `"                missing_rows = db.execute("` | — |
| [SRC-C9CF9B54F8-L000244](../../agents/omarai.py#L244) | 244 | `"                    \"\"\"SELECT COUNT(*)"` | — |
| [SRC-C9CF9B54F8-L000245](../../agents/omarai.py#L245) | 245 | `"                       FROM leads_legacy_migration legacy"` | — |
| [SRC-C9CF9B54F8-L000246](../../agents/omarai.py#L246) | 246 | `"                       LEFT JOIN leads migrated"` | — |
| [SRC-C9CF9B54F8-L000247](../../agents/omarai.py#L247) | 247 | `"                         ON migrated.id=legacy.id"` | — |
| [SRC-C9CF9B54F8-L000248](../../agents/omarai.py#L248) | 248 | `"                        AND migrated.fingerprint=legacy.fingerprint"` | — |
| [SRC-C9CF9B54F8-L000249](../../agents/omarai.py#L249) | 249 | `"                       WHERE migrated.id IS NULL\"\"\""` | — |
| [SRC-C9CF9B54F8-L000250](../../agents/omarai.py#L250) | 250 | `"                ).fetchone()[0]"` | — |
| [SRC-C9CF9B54F8-L000251](../../agents/omarai.py#L251) | 251 | `"                foreign_key_errors = db.execute("` | — |
| [SRC-C9CF9B54F8-L000252](../../agents/omarai.py#L252) | 252 | `"                    \"PRAGMA foreign_key_check(leads)\""` | — |
| [SRC-C9CF9B54F8-L000253](../../agents/omarai.py#L253) | 253 | `"                ).fetchall()"` | — |
| [SRC-C9CF9B54F8-L000254](../../agents/omarai.py#L254) | 254 | `"                if ("` | — |
| [SRC-C9CF9B54F8-L000255](../../agents/omarai.py#L255) | 255 | `"                    migrated_count != legacy_count"` | — |
| [SRC-C9CF9B54F8-L000256](../../agents/omarai.py#L256) | 256 | `"                    or missing_rows"` | — |
| [SRC-C9CF9B54F8-L000257](../../agents/omarai.py#L257) | 257 | `"                    or foreign_key_errors"` | — |
| [SRC-C9CF9B54F8-L000258](../../agents/omarai.py#L258) | 258 | `"                ):"` | — |
| [SRC-C9CF9B54F8-L000259](../../agents/omarai.py#L259) | 259 | `"                    raise RuntimeError("` | — |
| [SRC-C9CF9B54F8-L000260](../../agents/omarai.py#L260) | 260 | `"                        \"lead migration verification failed; legacy data was retained\""` | — |
| [SRC-C9CF9B54F8-L000261](../../agents/omarai.py#L261) | 261 | `"                    )"` | — |
| [SRC-C9CF9B54F8-L000262](../../agents/omarai.py#L262) | 262 | `"                # Drop the old table only after count, identity, and FK checks pass."` | — |
| [SRC-C9CF9B54F8-L000263](../../agents/omarai.py#L263) | 263 | `"                db.execute(\"DROP TABLE leads_legacy_migration\")"` | — |
| [SRC-C9CF9B54F8-L000264](../../agents/omarai.py#L264) | 264 | `"        else:"` | — |
| [SRC-C9CF9B54F8-L000265](../../agents/omarai.py#L265) | 265 | `"            self._create_leads_table(db)"` | — |
| [SRC-C9CF9B54F8-L000266](../../agents/omarai.py#L266) | 266 | `""` | — |
| [SRC-C9CF9B54F8-L000267](../../agents/omarai.py#L267) | 267 | `"        db.execute(\"DROP INDEX IF EXISTS leads_status_idx\")"` | — |
| [SRC-C9CF9B54F8-L000268](../../agents/omarai.py#L268) | 268 | `"        db.execute("` | — |
| [SRC-C9CF9B54F8-L000269](../../agents/omarai.py#L269) | 269 | `"            \"CREATE INDEX IF NOT EXISTS leads_tenant_status_idx \""` | — |
| [SRC-C9CF9B54F8-L000270](../../agents/omarai.py#L270) | 270 | `"            \"ON leads(tenant_id, status, created_at DESC)\""` | — |
| [SRC-C9CF9B54F8-L000271](../../agents/omarai.py#L271) | 271 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000272](../../agents/omarai.py#L272) | 272 | `"        db.execute("` | — |
| [SRC-C9CF9B54F8-L000273](../../agents/omarai.py#L273) | 273 | `"            \"CREATE INDEX IF NOT EXISTS memberships_user_active_idx \""` | — |
| [SRC-C9CF9B54F8-L000274](../../agents/omarai.py#L274) | 274 | `"            \"ON tenant_memberships(user_id, active, tenant_id)\""` | — |
| [SRC-C9CF9B54F8-L000275](../../agents/omarai.py#L275) | 275 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000276](../../agents/omarai.py#L276) | 276 | `""` | — |
| [SRC-C9CF9B54F8-L000277](../../agents/omarai.py#L277) | 277 | `"    @staticmethod"` | — |
| [SRC-C9CF9B54F8-L000278](../../agents/omarai.py#L278) | 278 | `"    def _tenant(tenant_id: str \| None) -> str:"` | — |
| [SRC-C9CF9B54F8-L000279](../../agents/omarai.py#L279) | 279 | `"        value = DEFAULT_TENANT_ID if tenant_id is None else str(tenant_id).strip()"` | — |
| [SRC-C9CF9B54F8-L000280](../../agents/omarai.py#L280) | 280 | `"        if not value or len(value) > 128:"` | — |
| [SRC-C9CF9B54F8-L000281](../../agents/omarai.py#L281) | 281 | `"            raise ValueError(\"tenant_id is invalid\")"` | — |
| [SRC-C9CF9B54F8-L000282](../../agents/omarai.py#L282) | 282 | `"        return value"` | — |
| [SRC-C9CF9B54F8-L000283](../../agents/omarai.py#L283) | 283 | `""` | — |
| [SRC-C9CF9B54F8-L000284](../../agents/omarai.py#L284) | 284 | `"    def default_principal(self) -> dict:"` | — |
| [SRC-C9CF9B54F8-L000285](../../agents/omarai.py#L285) | 285 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000286](../../agents/omarai.py#L286) | 286 | `"            row = db.execute("` | — |
| [SRC-C9CF9B54F8-L000287](../../agents/omarai.py#L287) | 287 | `"                \"\"\"SELECT m.tenant_id, m.user_id, m.role"` | — |
| [SRC-C9CF9B54F8-L000288](../../agents/omarai.py#L288) | 288 | `"                   FROM tenant_memberships m"` | — |
| [SRC-C9CF9B54F8-L000289](../../agents/omarai.py#L289) | 289 | `"                   JOIN tenants t ON t.id=m.tenant_id AND t.active=1"` | — |
| [SRC-C9CF9B54F8-L000290](../../agents/omarai.py#L290) | 290 | `"                   JOIN users u ON u.id=m.user_id AND u.active=1"` | — |
| [SRC-C9CF9B54F8-L000291](../../agents/omarai.py#L291) | 291 | `"                   WHERE m.tenant_id=? AND m.user_id=? AND m.active=1\"\"\","` | — |
| [SRC-C9CF9B54F8-L000292](../../agents/omarai.py#L292) | 292 | `"                (DEFAULT_TENANT_ID, DEFAULT_USER_ID),"` | — |
| [SRC-C9CF9B54F8-L000293](../../agents/omarai.py#L293) | 293 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000294](../../agents/omarai.py#L294) | 294 | `"        return dict(row) if row else {}"` | — |
| [SRC-C9CF9B54F8-L000295](../../agents/omarai.py#L295) | 295 | `""` | — |
| [SRC-C9CF9B54F8-L000296](../../agents/omarai.py#L296) | 296 | `"    def create_tenant(self, name: str, slug: str \| None = None) -> str:"` | — |
| [SRC-C9CF9B54F8-L000297](../../agents/omarai.py#L297) | 297 | `"        clean_name = str(name or \"\").strip()[:160]"` | — |
| [SRC-C9CF9B54F8-L000298](../../agents/omarai.py#L298) | 298 | `"        if not clean_name:"` | — |
| [SRC-C9CF9B54F8-L000299](../../agents/omarai.py#L299) | 299 | `"            raise ValueError(\"tenant name is required\")"` | — |
| [SRC-C9CF9B54F8-L000300](../../agents/omarai.py#L300) | 300 | `"        clean_slug = re.sub("` | — |
| [SRC-C9CF9B54F8-L000301](../../agents/omarai.py#L301) | 301 | `"            r\"[^a-z0-9-]+\", \"-\", str(slug or clean_name.casefold())"` | — |
| [SRC-C9CF9B54F8-L000302](../../agents/omarai.py#L302) | 302 | `"        ).strip(\"-\")[:80]"` | — |
| [SRC-C9CF9B54F8-L000303](../../agents/omarai.py#L303) | 303 | `"        if not clean_slug:"` | — |
| [SRC-C9CF9B54F8-L000304](../../agents/omarai.py#L304) | 304 | `"            raise ValueError(\"tenant slug is invalid\")"` | — |
| [SRC-C9CF9B54F8-L000305](../../agents/omarai.py#L305) | 305 | `"        tenant_id = \"tenant_\" + uuid.uuid4().hex"` | — |
| [SRC-C9CF9B54F8-L000306](../../agents/omarai.py#L306) | 306 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000307](../../agents/omarai.py#L307) | 307 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L000308](../../agents/omarai.py#L308) | 308 | `"                \"INSERT INTO tenants (id, name, slug, active, created_at) VALUES (?, ?, ?, 1, ?)\","` | — |
| [SRC-C9CF9B54F8-L000309](../../agents/omarai.py#L309) | 309 | `"                (tenant_id, clean_name, clean_slug, now_utc()),"` | — |
| [SRC-C9CF9B54F8-L000310](../../agents/omarai.py#L310) | 310 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000311](../../agents/omarai.py#L311) | 311 | `"        return tenant_id"` | — |
| [SRC-C9CF9B54F8-L000312](../../agents/omarai.py#L312) | 312 | `""` | — |
| [SRC-C9CF9B54F8-L000313](../../agents/omarai.py#L313) | 313 | `"    def create_user(self, email: str, display_name: str, user_id: str \| None = None) -> str:"` | — |
| [SRC-C9CF9B54F8-L000314](../../agents/omarai.py#L314) | 314 | `"        clean_email = str(email or \"\").strip().lower()[:254]"` | — |
| [SRC-C9CF9B54F8-L000315](../../agents/omarai.py#L315) | 315 | `"        clean_name = str(display_name or \"\").strip()[:160]"` | — |
| [SRC-C9CF9B54F8-L000316](../../agents/omarai.py#L316) | 316 | `"        if not clean_email or \"@\" not in clean_email or not clean_name:"` | — |
| [SRC-C9CF9B54F8-L000317](../../agents/omarai.py#L317) | 317 | `"            raise ValueError(\"valid email and display name are required\")"` | — |
| [SRC-C9CF9B54F8-L000318](../../agents/omarai.py#L318) | 318 | `"        identity = str(user_id or (\"user_\" + uuid.uuid4().hex))"` | — |
| [SRC-C9CF9B54F8-L000319](../../agents/omarai.py#L319) | 319 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000320](../../agents/omarai.py#L320) | 320 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L000321](../../agents/omarai.py#L321) | 321 | `"                \"\"\"INSERT INTO users (id, email, display_name, active, created_at)"` | — |
| [SRC-C9CF9B54F8-L000322](../../agents/omarai.py#L322) | 322 | `"                   VALUES (?, ?, ?, 1, ?)\"\"\","` | — |
| [SRC-C9CF9B54F8-L000323](../../agents/omarai.py#L323) | 323 | `"                (identity, clean_email, clean_name, now_utc()),"` | — |
| [SRC-C9CF9B54F8-L000324](../../agents/omarai.py#L324) | 324 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000325](../../agents/omarai.py#L325) | 325 | `"        return identity"` | — |
| [SRC-C9CF9B54F8-L000326](../../agents/omarai.py#L326) | 326 | `""` | — |
| [SRC-C9CF9B54F8-L000327](../../agents/omarai.py#L327) | 327 | `"    def add_membership(self, tenant_id: str, user_id: str, role: str = \"sales_agent\"):"` | — |
| [SRC-C9CF9B54F8-L000328](../../agents/omarai.py#L328) | 328 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L000329](../../agents/omarai.py#L329) | 329 | `"        if role not in self.ALLOWED_ROLES:"` | — |
| [SRC-C9CF9B54F8-L000330](../../agents/omarai.py#L330) | 330 | `"            raise ValueError(\"unsupported membership role\")"` | — |
| [SRC-C9CF9B54F8-L000331](../../agents/omarai.py#L331) | 331 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000332](../../agents/omarai.py#L332) | 332 | `"            exists = db.execute("` | — |
| [SRC-C9CF9B54F8-L000333](../../agents/omarai.py#L333) | 333 | `"                \"\"\"SELECT 1 FROM tenants t"` | — |
| [SRC-C9CF9B54F8-L000334](../../agents/omarai.py#L334) | 334 | `"                   JOIN users u ON u.id=?"` | — |
| [SRC-C9CF9B54F8-L000335](../../agents/omarai.py#L335) | 335 | `"                   WHERE t.id=? AND t.active=1 AND u.active=1\"\"\","` | — |
| [SRC-C9CF9B54F8-L000336](../../agents/omarai.py#L336) | 336 | `"                (user_id, tenant),"` | — |
| [SRC-C9CF9B54F8-L000337](../../agents/omarai.py#L337) | 337 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000338](../../agents/omarai.py#L338) | 338 | `"            if not exists:"` | — |
| [SRC-C9CF9B54F8-L000339](../../agents/omarai.py#L339) | 339 | `"                raise ValueError(\"active tenant and user are required\")"` | — |
| [SRC-C9CF9B54F8-L000340](../../agents/omarai.py#L340) | 340 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L000341](../../agents/omarai.py#L341) | 341 | `"                \"\"\"INSERT INTO tenant_memberships"` | — |
| [SRC-C9CF9B54F8-L000342](../../agents/omarai.py#L342) | 342 | `"                   (tenant_id, user_id, role, active, created_at)"` | — |
| [SRC-C9CF9B54F8-L000343](../../agents/omarai.py#L343) | 343 | `"                   VALUES (?, ?, ?, 1, ?)"` | — |
| [SRC-C9CF9B54F8-L000344](../../agents/omarai.py#L344) | 344 | `"                   ON CONFLICT(tenant_id, user_id)"` | — |
| [SRC-C9CF9B54F8-L000345](../../agents/omarai.py#L345) | 345 | `"                   DO UPDATE SET role=excluded.role, active=1\"\"\","` | — |
| [SRC-C9CF9B54F8-L000346](../../agents/omarai.py#L346) | 346 | `"                (tenant, user_id, role, now_utc()),"` | — |
| [SRC-C9CF9B54F8-L000347](../../agents/omarai.py#L347) | 347 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000348](../../agents/omarai.py#L348) | 348 | `""` | — |
| [SRC-C9CF9B54F8-L000349](../../agents/omarai.py#L349) | 349 | `"    @staticmethod"` | — |
| [SRC-C9CF9B54F8-L000350](../../agents/omarai.py#L350) | 350 | `"    def _token_hash(token: str) -> str:"` | — |
| [SRC-C9CF9B54F8-L000351](../../agents/omarai.py#L351) | 351 | `"        return hashlib.sha256(token.encode(\"utf-8\")).hexdigest()"` | — |
| [SRC-C9CF9B54F8-L000352](../../agents/omarai.py#L352) | 352 | `""` | — |
| [SRC-C9CF9B54F8-L000353](../../agents/omarai.py#L353) | 353 | `"    @staticmethod"` | — |
| [SRC-C9CF9B54F8-L000354](../../agents/omarai.py#L354) | 354 | `"    def _normalize_token_expiry(expires_at: str \| None) -> str \| None:"` | — |
| [SRC-C9CF9B54F8-L000355](../../agents/omarai.py#L355) | 355 | `"        \"\"\"Store token expiries as validated UTC timestamps for safe comparisons.\"\"\""` | — |
| [SRC-C9CF9B54F8-L000356](../../agents/omarai.py#L356) | 356 | `"        if expires_at is None:"` | — |
| [SRC-C9CF9B54F8-L000357](../../agents/omarai.py#L357) | 357 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L000358](../../agents/omarai.py#L358) | 358 | `"        if not isinstance(expires_at, str) or not expires_at.strip():"` | — |
| [SRC-C9CF9B54F8-L000359](../../agents/omarai.py#L359) | 359 | `"            raise ValueError(\"expires_at must be an ISO-8601 timestamp with a timezone\")"` | — |
| [SRC-C9CF9B54F8-L000360](../../agents/omarai.py#L360) | 360 | `"        value = expires_at.strip()"` | — |
| [SRC-C9CF9B54F8-L000361](../../agents/omarai.py#L361) | 361 | `"        if value.endswith(\"Z\"):"` | — |
| [SRC-C9CF9B54F8-L000362](../../agents/omarai.py#L362) | 362 | `"            value = value[:-1] + \"+00:00\""` | — |
| [SRC-C9CF9B54F8-L000363](../../agents/omarai.py#L363) | 363 | `"        try:"` | — |
| [SRC-C9CF9B54F8-L000364](../../agents/omarai.py#L364) | 364 | `"            parsed = datetime.fromisoformat(value)"` | — |
| [SRC-C9CF9B54F8-L000365](../../agents/omarai.py#L365) | 365 | `"        except ValueError as exc:"` | — |
| [SRC-C9CF9B54F8-L000366](../../agents/omarai.py#L366) | 366 | `"            raise ValueError("` | — |
| [SRC-C9CF9B54F8-L000367](../../agents/omarai.py#L367) | 367 | `"                \"expires_at must be an ISO-8601 timestamp with a timezone\""` | — |
| [SRC-C9CF9B54F8-L000368](../../agents/omarai.py#L368) | 368 | `"            ) from exc"` | — |
| [SRC-C9CF9B54F8-L000369](../../agents/omarai.py#L369) | 369 | `"        if parsed.tzinfo is None or parsed.utcoffset() is None:"` | — |
| [SRC-C9CF9B54F8-L000370](../../agents/omarai.py#L370) | 370 | `"            raise ValueError(\"expires_at must include an explicit timezone\")"` | — |
| [SRC-C9CF9B54F8-L000371](../../agents/omarai.py#L371) | 371 | `"        normalized = parsed.astimezone(UTC)"` | — |
| [SRC-C9CF9B54F8-L000372](../../agents/omarai.py#L372) | 372 | `"        if normalized <= datetime.now(UTC):"` | — |
| [SRC-C9CF9B54F8-L000373](../../agents/omarai.py#L373) | 373 | `"            raise ValueError(\"expires_at must be in the future\")"` | — |
| [SRC-C9CF9B54F8-L000374](../../agents/omarai.py#L374) | 374 | `"        return normalized.isoformat(timespec=\"seconds\").replace(\"+00:00\", \"Z\")"` | — |
| [SRC-C9CF9B54F8-L000375](../../agents/omarai.py#L375) | 375 | `""` | — |
| [SRC-C9CF9B54F8-L000376](../../agents/omarai.py#L376) | 376 | `"    def create_api_token("` | — |
| [SRC-C9CF9B54F8-L000377](../../agents/omarai.py#L377) | 377 | `"        self,"` | — |
| [SRC-C9CF9B54F8-L000378](../../agents/omarai.py#L378) | 378 | `"        token: str,"` | — |
| [SRC-C9CF9B54F8-L000379](../../agents/omarai.py#L379) | 379 | `"        tenant_id: str,"` | — |
| [SRC-C9CF9B54F8-L000380](../../agents/omarai.py#L380) | 380 | `"        user_id: str,"` | — |
| [SRC-C9CF9B54F8-L000381](../../agents/omarai.py#L381) | 381 | `"        label: str = \"api\","` | — |
| [SRC-C9CF9B54F8-L000382](../../agents/omarai.py#L382) | 382 | `"        expires_at: str \| None = None,"` | — |
| [SRC-C9CF9B54F8-L000383](../../agents/omarai.py#L383) | 383 | `"    ):"` | — |
| [SRC-C9CF9B54F8-L000384](../../agents/omarai.py#L384) | 384 | `"        if not isinstance(token, str) or len(token.strip()) < 32:"` | — |
| [SRC-C9CF9B54F8-L000385](../../agents/omarai.py#L385) | 385 | `"            raise ValueError(\"API token must contain at least 32 characters\")"` | — |
| [SRC-C9CF9B54F8-L000386](../../agents/omarai.py#L386) | 386 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L000387](../../agents/omarai.py#L387) | 387 | `"        expires_at = self._normalize_token_expiry(expires_at)"` | — |
| [SRC-C9CF9B54F8-L000388](../../agents/omarai.py#L388) | 388 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000389](../../agents/omarai.py#L389) | 389 | `"            membership = db.execute("` | — |
| [SRC-C9CF9B54F8-L000390](../../agents/omarai.py#L390) | 390 | `"                \"\"\"SELECT 1 FROM tenant_memberships m"` | — |
| [SRC-C9CF9B54F8-L000391](../../agents/omarai.py#L391) | 391 | `"                   JOIN tenants t ON t.id=m.tenant_id AND t.active=1"` | — |
| [SRC-C9CF9B54F8-L000392](../../agents/omarai.py#L392) | 392 | `"                   JOIN users u ON u.id=m.user_id AND u.active=1"` | — |
| [SRC-C9CF9B54F8-L000393](../../agents/omarai.py#L393) | 393 | `"                   WHERE m.tenant_id=? AND m.user_id=? AND m.active=1\"\"\","` | — |
| [SRC-C9CF9B54F8-L000394](../../agents/omarai.py#L394) | 394 | `"                (tenant, user_id),"` | — |
| [SRC-C9CF9B54F8-L000395](../../agents/omarai.py#L395) | 395 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000396](../../agents/omarai.py#L396) | 396 | `"            if not membership:"` | — |
| [SRC-C9CF9B54F8-L000397](../../agents/omarai.py#L397) | 397 | `"                raise ValueError(\"active tenant membership is required\")"` | — |
| [SRC-C9CF9B54F8-L000398](../../agents/omarai.py#L398) | 398 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L000399](../../agents/omarai.py#L399) | 399 | `"                \"\"\"INSERT INTO api_tokens"` | — |
| [SRC-C9CF9B54F8-L000400](../../agents/omarai.py#L400) | 400 | `"                   (token_hash, tenant_id, user_id, label, active, created_at, expires_at)"` | — |
| [SRC-C9CF9B54F8-L000401](../../agents/omarai.py#L401) | 401 | `"                   VALUES (?, ?, ?, ?, 1, ?, ?)\"\"\","` | — |
| [SRC-C9CF9B54F8-L000402](../../agents/omarai.py#L402) | 402 | `"                ("` | — |
| [SRC-C9CF9B54F8-L000403](../../agents/omarai.py#L403) | 403 | `"                    self._token_hash(token.strip()),"` | — |
| [SRC-C9CF9B54F8-L000404](../../agents/omarai.py#L404) | 404 | `"                    tenant,"` | — |
| [SRC-C9CF9B54F8-L000405](../../agents/omarai.py#L405) | 405 | `"                    user_id,"` | — |
| [SRC-C9CF9B54F8-L000406](../../agents/omarai.py#L406) | 406 | `"                    str(label or \"api\")[:80],"` | — |
| [SRC-C9CF9B54F8-L000407](../../agents/omarai.py#L407) | 407 | `"                    now_utc(),"` | — |
| [SRC-C9CF9B54F8-L000408](../../agents/omarai.py#L408) | 408 | `"                    expires_at,"` | — |
| [SRC-C9CF9B54F8-L000409](../../agents/omarai.py#L409) | 409 | `"                ),"` | — |
| [SRC-C9CF9B54F8-L000410](../../agents/omarai.py#L410) | 410 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000411](../../agents/omarai.py#L411) | 411 | `""` | — |
| [SRC-C9CF9B54F8-L000412](../../agents/omarai.py#L412) | 412 | `"    def resolve_api_token(self, token: str) -> dict \| None:"` | — |
| [SRC-C9CF9B54F8-L000413](../../agents/omarai.py#L413) | 413 | `"        if not isinstance(token, str) or len(token.strip()) < 32:"` | — |
| [SRC-C9CF9B54F8-L000414](../../agents/omarai.py#L414) | 414 | `"            return None"` | — |
| [SRC-C9CF9B54F8-L000415](../../agents/omarai.py#L415) | 415 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000416](../../agents/omarai.py#L416) | 416 | `"            row = db.execute("` | — |
| [SRC-C9CF9B54F8-L000417](../../agents/omarai.py#L417) | 417 | `"                \"\"\"SELECT m.tenant_id, m.user_id, m.role"` | — |
| [SRC-C9CF9B54F8-L000418](../../agents/omarai.py#L418) | 418 | `"                   FROM api_tokens a"` | — |
| [SRC-C9CF9B54F8-L000419](../../agents/omarai.py#L419) | 419 | `"                   JOIN tenant_memberships m"` | — |
| [SRC-C9CF9B54F8-L000420](../../agents/omarai.py#L420) | 420 | `"                     ON m.tenant_id=a.tenant_id AND m.user_id=a.user_id"` | — |
| [SRC-C9CF9B54F8-L000421](../../agents/omarai.py#L421) | 421 | `"                   JOIN tenants t ON t.id=m.tenant_id AND t.active=1"` | — |
| [SRC-C9CF9B54F8-L000422](../../agents/omarai.py#L422) | 422 | `"                   JOIN users u ON u.id=m.user_id AND u.active=1"` | — |
| [SRC-C9CF9B54F8-L000423](../../agents/omarai.py#L423) | 423 | `"                   WHERE a.token_hash=? AND a.active=1 AND m.active=1"` | — |
| [SRC-C9CF9B54F8-L000424](../../agents/omarai.py#L424) | 424 | `"                     AND (a.expires_at IS NULL OR a.expires_at > ?)\"\"\","` | — |
| [SRC-C9CF9B54F8-L000425](../../agents/omarai.py#L425) | 425 | `"                (self._token_hash(token.strip()), now_utc()),"` | — |
| [SRC-C9CF9B54F8-L000426](../../agents/omarai.py#L426) | 426 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000427](../../agents/omarai.py#L427) | 427 | `"        return dict(row) if row else None"` | — |
| [SRC-C9CF9B54F8-L000428](../../agents/omarai.py#L428) | 428 | `""` | — |
| [SRC-C9CF9B54F8-L000429](../../agents/omarai.py#L429) | 429 | `"    def add("` | — |
| [SRC-C9CF9B54F8-L000430](../../agents/omarai.py#L430) | 430 | `"        self,"` | — |
| [SRC-C9CF9B54F8-L000431](../../agents/omarai.py#L431) | 431 | `"        text: str,"` | — |
| [SRC-C9CF9B54F8-L000432](../../agents/omarai.py#L432) | 432 | `"        source_url: str,"` | — |
| [SRC-C9CF9B54F8-L000433](../../agents/omarai.py#L433) | 433 | `"        platform: str = \"manual\","` | — |
| [SRC-C9CF9B54F8-L000434](../../agents/omarai.py#L434) | 434 | `"        observed_at: str \| None = None,"` | — |
| [SRC-C9CF9B54F8-L000435](../../agents/omarai.py#L435) | 435 | `"        note: str = \"\","` | — |
| [SRC-C9CF9B54F8-L000436](../../agents/omarai.py#L436) | 436 | `"        product_terms=(),"` | — |
| [SRC-C9CF9B54F8-L000437](../../agents/omarai.py#L437) | 437 | `"        location_terms=(),"` | — |
| [SRC-C9CF9B54F8-L000438](../../agents/omarai.py#L438) | 438 | `"        *,"` | — |
| [SRC-C9CF9B54F8-L000439](../../agents/omarai.py#L439) | 439 | `"        tenant_id: str \| None = None,"` | — |
| [SRC-C9CF9B54F8-L000440](../../agents/omarai.py#L440) | 440 | `"    ):"` | — |
| [SRC-C9CF9B54F8-L000441](../../agents/omarai.py#L441) | 441 | `"        if not isinstance(text, str) or not text.strip():"` | — |
| [SRC-C9CF9B54F8-L000442](../../agents/omarai.py#L442) | 442 | `"            raise ValueError(\"text is required\")"` | — |
| [SRC-C9CF9B54F8-L000443](../../agents/omarai.py#L443) | 443 | `"        if len(text) > MAX_TEXT:"` | — |
| [SRC-C9CF9B54F8-L000444](../../agents/omarai.py#L444) | 444 | `"            raise ValueError(\"text is too long\")"` | — |
| [SRC-C9CF9B54F8-L000445](../../agents/omarai.py#L445) | 445 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L000446](../../agents/omarai.py#L446) | 446 | `"        url = validate_url(source_url)"` | — |
| [SRC-C9CF9B54F8-L000447](../../agents/omarai.py#L447) | 447 | `"        normalized = normalize(text)"` | — |
| [SRC-C9CF9B54F8-L000448](../../agents/omarai.py#L448) | 448 | `"        fingerprint = hashlib.sha256("` | — |
| [SRC-C9CF9B54F8-L000449](../../agents/omarai.py#L449) | 449 | `"            (url.rstrip(\"/\") + \"\\n\" + normalized).encode()"` | — |
| [SRC-C9CF9B54F8-L000450](../../agents/omarai.py#L450) | 450 | `"        ).hexdigest()"` | — |
| [SRC-C9CF9B54F8-L000451](../../agents/omarai.py#L451) | 451 | `"        lead_id = hashlib.sha256("` | — |
| [SRC-C9CF9B54F8-L000452](../../agents/omarai.py#L452) | 452 | `"            (tenant + \"\\n\" + fingerprint).encode()"` | — |
| [SRC-C9CF9B54F8-L000453](../../agents/omarai.py#L453) | 453 | `"        ).hexdigest()[:24]"` | — |
| [SRC-C9CF9B54F8-L000454](../../agents/omarai.py#L454) | 454 | `"        timestamp = observed_at or now_utc()"` | — |
| [SRC-C9CF9B54F8-L000455](../../agents/omarai.py#L455) | 455 | `"        assessment = analyze(text, product_terms=product_terms, location_terms=location_terms)"` | — |
| [SRC-C9CF9B54F8-L000456](../../agents/omarai.py#L456) | 456 | `"        now = now_utc()"` | — |
| [SRC-C9CF9B54F8-L000457](../../agents/omarai.py#L457) | 457 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000458](../../agents/omarai.py#L458) | 458 | `"            active_tenant = db.execute("` | — |
| [SRC-C9CF9B54F8-L000459](../../agents/omarai.py#L459) | 459 | `"                \"SELECT 1 FROM tenants WHERE id=? AND active=1\", (tenant,)"` | — |
| [SRC-C9CF9B54F8-L000460](../../agents/omarai.py#L460) | 460 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000461](../../agents/omarai.py#L461) | 461 | `"            if not active_tenant:"` | — |
| [SRC-C9CF9B54F8-L000462](../../agents/omarai.py#L462) | 462 | `"                raise ValueError(\"active tenant is required\")"` | — |
| [SRC-C9CF9B54F8-L000463](../../agents/omarai.py#L463) | 463 | `"            cursor = db.execute("` | — |
| [SRC-C9CF9B54F8-L000464](../../agents/omarai.py#L464) | 464 | `"                \"\"\"INSERT OR IGNORE INTO leads"` | — |
| [SRC-C9CF9B54F8-L000465](../../agents/omarai.py#L465) | 465 | `"                   (id, tenant_id, fingerprint, text, source_url, platform, observed_at,"` | — |
| [SRC-C9CF9B54F8-L000466](../../agents/omarai.py#L466) | 466 | `"                    assessment, status, note, created_at, updated_at)"` | — |
| [SRC-C9CF9B54F8-L000467](../../agents/omarai.py#L467) | 467 | `"                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)\"\"\","` | — |
| [SRC-C9CF9B54F8-L000468](../../agents/omarai.py#L468) | 468 | `"                ("` | — |
| [SRC-C9CF9B54F8-L000469](../../agents/omarai.py#L469) | 469 | `"                    lead_id, tenant, fingerprint, text.strip(), url,"` | — |
| [SRC-C9CF9B54F8-L000470](../../agents/omarai.py#L470) | 470 | `"                    str(platform)[:80], timestamp,"` | — |
| [SRC-C9CF9B54F8-L000471](../../agents/omarai.py#L471) | 471 | `"                    json.dumps(assessment, ensure_ascii=False), \"new\","` | — |
| [SRC-C9CF9B54F8-L000472](../../agents/omarai.py#L472) | 472 | `"                    str(note)[:1000], now, now,"` | — |
| [SRC-C9CF9B54F8-L000473](../../agents/omarai.py#L473) | 473 | `"                ),"` | — |
| [SRC-C9CF9B54F8-L000474](../../agents/omarai.py#L474) | 474 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000475](../../agents/omarai.py#L475) | 475 | `"            row = db.execute("` | — |
| [SRC-C9CF9B54F8-L000476](../../agents/omarai.py#L476) | 476 | `"                \"SELECT * FROM leads WHERE tenant_id=? AND fingerprint=?\","` | — |
| [SRC-C9CF9B54F8-L000477](../../agents/omarai.py#L477) | 477 | `"                (tenant, fingerprint),"` | — |
| [SRC-C9CF9B54F8-L000478](../../agents/omarai.py#L478) | 478 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000479](../../agents/omarai.py#L479) | 479 | `"        return self.to_dict(row), cursor.rowcount == 1"` | — |
| [SRC-C9CF9B54F8-L000480](../../agents/omarai.py#L480) | 480 | `""` | — |
| [SRC-C9CF9B54F8-L000481](../../agents/omarai.py#L481) | 481 | `"    @staticmethod"` | — |
| [SRC-C9CF9B54F8-L000482](../../agents/omarai.py#L482) | 482 | `"    def to_dict(row):"` | — |
| [SRC-C9CF9B54F8-L000483](../../agents/omarai.py#L483) | 483 | `"        item = dict(row)"` | — |
| [SRC-C9CF9B54F8-L000484](../../agents/omarai.py#L484) | 484 | `"        item[\"assessment\"] = json.loads(item[\"assessment\"])"` | — |
| [SRC-C9CF9B54F8-L000485](../../agents/omarai.py#L485) | 485 | `"        return item"` | — |
| [SRC-C9CF9B54F8-L000486](../../agents/omarai.py#L486) | 486 | `""` | — |
| [SRC-C9CF9B54F8-L000487](../../agents/omarai.py#L487) | 487 | `"    def list("` | — |
| [SRC-C9CF9B54F8-L000488](../../agents/omarai.py#L488) | 488 | `"        self,"` | — |
| [SRC-C9CF9B54F8-L000489](../../agents/omarai.py#L489) | 489 | `"        status: str \| None = None,"` | — |
| [SRC-C9CF9B54F8-L000490](../../agents/omarai.py#L490) | 490 | `"        limit: int = 100,"` | — |
| [SRC-C9CF9B54F8-L000491](../../agents/omarai.py#L491) | 491 | `"        *,"` | — |
| [SRC-C9CF9B54F8-L000492](../../agents/omarai.py#L492) | 492 | `"        tenant_id: str \| None = None,"` | — |
| [SRC-C9CF9B54F8-L000493](../../agents/omarai.py#L493) | 493 | `"    ):"` | — |
| [SRC-C9CF9B54F8-L000494](../../agents/omarai.py#L494) | 494 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L000495](../../agents/omarai.py#L495) | 495 | `"        limit = max(1, min(int(limit), 500))"` | — |
| [SRC-C9CF9B54F8-L000496](../../agents/omarai.py#L496) | 496 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000497](../../agents/omarai.py#L497) | 497 | `"            rows = db.execute("` | — |
| [SRC-C9CF9B54F8-L000498](../../agents/omarai.py#L498) | 498 | `"                \"\"\"SELECT * FROM leads"` | — |
| [SRC-C9CF9B54F8-L000499](../../agents/omarai.py#L499) | 499 | `"                   WHERE tenant_id=? AND (? IS NULL OR status=?)"` | — |
| [SRC-C9CF9B54F8-L000500](../../agents/omarai.py#L500) | 500 | `"                   ORDER BY created_at DESC LIMIT ?\"\"\","` | — |
| [SRC-C9CF9B54F8-L000501](../../agents/omarai.py#L501) | 501 | `"                (tenant, status, status, limit),"` | — |
| [SRC-C9CF9B54F8-L000502](../../agents/omarai.py#L502) | 502 | `"            ).fetchall()"` | — |
| [SRC-C9CF9B54F8-L000503](../../agents/omarai.py#L503) | 503 | `"        return [self.to_dict(row) for row in rows]"` | — |
| [SRC-C9CF9B54F8-L000504](../../agents/omarai.py#L504) | 504 | `""` | — |
| [SRC-C9CF9B54F8-L000505](../../agents/omarai.py#L505) | 505 | `"    def update_status("` | — |
| [SRC-C9CF9B54F8-L000506](../../agents/omarai.py#L506) | 506 | `"        self,"` | — |
| [SRC-C9CF9B54F8-L000507](../../agents/omarai.py#L507) | 507 | `"        lead_id: str,"` | — |
| [SRC-C9CF9B54F8-L000508](../../agents/omarai.py#L508) | 508 | `"        status: str,"` | — |
| [SRC-C9CF9B54F8-L000509](../../agents/omarai.py#L509) | 509 | `"        *,"` | — |
| [SRC-C9CF9B54F8-L000510](../../agents/omarai.py#L510) | 510 | `"        tenant_id: str \| None = None,"` | — |
| [SRC-C9CF9B54F8-L000511](../../agents/omarai.py#L511) | 511 | `"    ):"` | — |
| [SRC-C9CF9B54F8-L000512](../../agents/omarai.py#L512) | 512 | `"        if status not in self.ALLOWED_STATUSES:"` | — |
| [SRC-C9CF9B54F8-L000513](../../agents/omarai.py#L513) | 513 | `"            raise ValueError(\"unsupported status\")"` | — |
| [SRC-C9CF9B54F8-L000514](../../agents/omarai.py#L514) | 514 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L000515](../../agents/omarai.py#L515) | 515 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000516](../../agents/omarai.py#L516) | 516 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L000517](../../agents/omarai.py#L517) | 517 | `"                \"UPDATE leads SET status=?, updated_at=? WHERE id=? AND tenant_id=?\","` | — |
| [SRC-C9CF9B54F8-L000518](../../agents/omarai.py#L518) | 518 | `"                (status, now_utc(), lead_id, tenant),"` | — |
| [SRC-C9CF9B54F8-L000519](../../agents/omarai.py#L519) | 519 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000520](../../agents/omarai.py#L520) | 520 | `"            row = db.execute("` | — |
| [SRC-C9CF9B54F8-L000521](../../agents/omarai.py#L521) | 521 | `"                \"SELECT * FROM leads WHERE id=? AND tenant_id=?\","` | — |
| [SRC-C9CF9B54F8-L000522](../../agents/omarai.py#L522) | 522 | `"                (lead_id, tenant),"` | — |
| [SRC-C9CF9B54F8-L000523](../../agents/omarai.py#L523) | 523 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000524](../../agents/omarai.py#L524) | 524 | `"        return self.to_dict(row) if row else None"` | — |
| [SRC-C9CF9B54F8-L000525](../../agents/omarai.py#L525) | 525 | `""` | — |
| [SRC-C9CF9B54F8-L000526](../../agents/omarai.py#L526) | 526 | `"    def import_csv(self, filename: str, *, tenant_id: str \| None = None):"` | — |
| [SRC-C9CF9B54F8-L000527](../../agents/omarai.py#L527) | 527 | `"        tenant = self._tenant(tenant_id)"` | — |
| [SRC-C9CF9B54F8-L000528](../../agents/omarai.py#L528) | 528 | `"        results = {\"created\": 0, \"duplicates\": 0, \"errors\": []}"` | — |
| [SRC-C9CF9B54F8-L000529](../../agents/omarai.py#L529) | 529 | `"        with open(filename, newline=\"\", encoding=\"utf-8-sig\") as stream:"` | — |
| [SRC-C9CF9B54F8-L000530](../../agents/omarai.py#L530) | 530 | `"            reader = csv.DictReader(stream)"` | — |
| [SRC-C9CF9B54F8-L000531](../../agents/omarai.py#L531) | 531 | `"            required = {\"text\", \"source_url\", \"platform\"}"` | — |
| [SRC-C9CF9B54F8-L000532](../../agents/omarai.py#L532) | 532 | `"            if not reader.fieldnames or not required.issubset(reader.fieldnames):"` | — |
| [SRC-C9CF9B54F8-L000533](../../agents/omarai.py#L533) | 533 | `"                raise ValueError(\"CSV must contain text,source_url,platform columns\")"` | — |
| [SRC-C9CF9B54F8-L000534](../../agents/omarai.py#L534) | 534 | `"            for line, row in enumerate(reader, 2):"` | — |
| [SRC-C9CF9B54F8-L000535](../../agents/omarai.py#L535) | 535 | `"                try:"` | — |
| [SRC-C9CF9B54F8-L000536](../../agents/omarai.py#L536) | 536 | `"                    _, created = self.add("` | — |
| [SRC-C9CF9B54F8-L000537](../../agents/omarai.py#L537) | 537 | `"                        row[\"text\"], row[\"source_url\"], row[\"platform\"],"` | — |
| [SRC-C9CF9B54F8-L000538](../../agents/omarai.py#L538) | 538 | `"                        row.get(\"observed_at\") or None, row.get(\"note\") or \"\","` | — |
| [SRC-C9CF9B54F8-L000539](../../agents/omarai.py#L539) | 539 | `"                        tenant_id=tenant,"` | — |
| [SRC-C9CF9B54F8-L000540](../../agents/omarai.py#L540) | 540 | `"                    )"` | — |
| [SRC-C9CF9B54F8-L000541](../../agents/omarai.py#L541) | 541 | `"                    results[\"created\" if created else \"duplicates\"] += 1"` | — |
| [SRC-C9CF9B54F8-L000542](../../agents/omarai.py#L542) | 542 | `"                except (ValueError, TypeError) as exc:"` | — |
| [SRC-C9CF9B54F8-L000543](../../agents/omarai.py#L543) | 543 | `"                    results[\"errors\"].append({\"line\": line, \"error\": str(exc)})"` | — |
| [SRC-C9CF9B54F8-L000544](../../agents/omarai.py#L544) | 544 | `"        return results"` | — |
| [SRC-C9CF9B54F8-L000545](../../agents/omarai.py#L545) | 545 | `""` | — |
| [SRC-C9CF9B54F8-L000546](../../agents/omarai.py#L546) | 546 | `"    def export_csv(self, filename: str, *, tenant_id: str \| None = None):"` | — |
| [SRC-C9CF9B54F8-L000547](../../agents/omarai.py#L547) | 547 | `"        rows = self.list(limit=500, tenant_id=tenant_id)"` | — |
| [SRC-C9CF9B54F8-L000548](../../agents/omarai.py#L548) | 548 | `"        with open(filename, \"w\", newline=\"\", encoding=\"utf-8-sig\") as stream:"` | — |
| [SRC-C9CF9B54F8-L000549](../../agents/omarai.py#L549) | 549 | `"            fields = ["` | — |
| [SRC-C9CF9B54F8-L000550](../../agents/omarai.py#L550) | 550 | `"                \"id\", \"tenant_id\", \"text\", \"source_url\", \"platform\", \"observed_at\","` | — |
| [SRC-C9CF9B54F8-L000551](../../agents/omarai.py#L551) | 551 | `"                \"assessment\", \"status\", \"note\", \"created_at\","` | — |
| [SRC-C9CF9B54F8-L000552](../../agents/omarai.py#L552) | 552 | `"            ]"` | — |
| [SRC-C9CF9B54F8-L000553](../../agents/omarai.py#L553) | 553 | `"            writer = csv.DictWriter(stream, fieldnames=fields, quoting=csv.QUOTE_ALL)"` | — |
| [SRC-C9CF9B54F8-L000554](../../agents/omarai.py#L554) | 554 | `"            writer.writeheader()"` | — |
| [SRC-C9CF9B54F8-L000555](../../agents/omarai.py#L555) | 555 | `"            for row in rows:"` | — |
| [SRC-C9CF9B54F8-L000556](../../agents/omarai.py#L556) | 556 | `"                values = {"` | — |
| [SRC-C9CF9B54F8-L000557](../../agents/omarai.py#L557) | 557 | `"                    key: json.dumps(row[key], ensure_ascii=False)"` | — |
| [SRC-C9CF9B54F8-L000558](../../agents/omarai.py#L558) | 558 | `"                    if key == \"assessment\""` | — |
| [SRC-C9CF9B54F8-L000559](../../agents/omarai.py#L559) | 559 | `"                    else row.get(key, \"\")"` | — |
| [SRC-C9CF9B54F8-L000560](../../agents/omarai.py#L560) | 560 | `"                    for key in fields"` | — |
| [SRC-C9CF9B54F8-L000561](../../agents/omarai.py#L561) | 561 | `"                }"` | — |
| [SRC-C9CF9B54F8-L000562](../../agents/omarai.py#L562) | 562 | `"                writer.writerow({key: _csv_safe_cell(value) for key, value in values.items()})"` | — |
| [SRC-C9CF9B54F8-L000563](../../agents/omarai.py#L563) | 563 | `"        return len(rows)"` | — |
## الوكيل والمنطق

### FILE-FDEEAFDFCA — [agents/request_budget.py](../../agents/request_budget.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-FDEEAFDFCA-L000001](../../agents/request_budget.py#L1) | 1 | `"\"\"\"Cooperative per-request resource budgets for Omarai's web-research pipeline."` | — |
| [SRC-FDEEAFDFCA-L000002](../../agents/request_budget.py#L2) | 2 | `""` | — |
| [SRC-FDEEAFDFCA-L000003](../../agents/request_budget.py#L3) | 3 | `"The budget limits work that has not started yet and caps the timeout supplied to"` | — |
| [SRC-FDEEAFDFCA-L000004](../../agents/request_budget.py#L4) | 4 | `"each outbound operation by the remaining request window. Socket libraries may"` | — |
| [SRC-FDEEAFDFCA-L000005](../../agents/request_budget.py#L5) | 5 | `"still overrun a cooperative deadline slightly while unwinding an in-flight call;"` | — |
| [SRC-FDEEAFDFCA-L000006](../../agents/request_budget.py#L6) | 6 | `"this is not a hard real-time cancellation primitive."` | — |
| [SRC-FDEEAFDFCA-L000007](../../agents/request_budget.py#L7) | 7 | `"\"\"\""` | — |
| [SRC-FDEEAFDFCA-L000008](../../agents/request_budget.py#L8) | 8 | `"from __future__ import annotations"` | — |
| [SRC-FDEEAFDFCA-L000009](../../agents/request_budget.py#L9) | 9 | `""` | — |
| [SRC-FDEEAFDFCA-L000010](../../agents/request_budget.py#L10) | 10 | `"import os"` | — |
| [SRC-FDEEAFDFCA-L000011](../../agents/request_budget.py#L11) | 11 | `"import threading"` | — |
| [SRC-FDEEAFDFCA-L000012](../../agents/request_budget.py#L12) | 12 | `"import time"` | — |
| [SRC-FDEEAFDFCA-L000013](../../agents/request_budget.py#L13) | 13 | `"from collections.abc import Callable, Mapping"` | — |
| [SRC-FDEEAFDFCA-L000014](../../agents/request_budget.py#L14) | 14 | `"from typing import Any"` | — |
| [SRC-FDEEAFDFCA-L000015](../../agents/request_budget.py#L15) | 15 | `""` | — |
| [SRC-FDEEAFDFCA-L000016](../../agents/request_budget.py#L16) | 16 | `""` | — |
| [SRC-FDEEAFDFCA-L000017](../../agents/request_budget.py#L17) | 17 | `"class RequestBudgetExceeded(Exception):"` | — |
| [SRC-FDEEAFDFCA-L000018](../../agents/request_budget.py#L18) | 18 | `"    \"\"\"Raised when a request cannot start more work within its resource budget.\"\"\""` | — |
| [SRC-FDEEAFDFCA-L000019](../../agents/request_budget.py#L19) | 19 | `""` | — |
| [SRC-FDEEAFDFCA-L000020](../../agents/request_budget.py#L20) | 20 | `""` | — |
| [SRC-FDEEAFDFCA-L000021](../../agents/request_budget.py#L21) | 21 | `"DEFAULT_TIMEOUT_SECONDS = 90"` | — |
| [SRC-FDEEAFDFCA-L000022](../../agents/request_budget.py#L22) | 22 | `"MAX_TIMEOUT_SECONDS = 120"` | — |
| [SRC-FDEEAFDFCA-L000023](../../agents/request_budget.py#L23) | 23 | `"RESOURCE_LIMITS = {"` | — |
| [SRC-FDEEAFDFCA-L000024](../../agents/request_budget.py#L24) | 24 | `"    \"search_queries\": (8, 8),"` | — |
| [SRC-FDEEAFDFCA-L000025](../../agents/request_budget.py#L25) | 25 | `"    \"search_calls\": (32, 40),"` | — |
| [SRC-FDEEAFDFCA-L000026](../../agents/request_budget.py#L26) | 26 | `"    \"model_calls\": (8, 12),"` | — |
| [SRC-FDEEAFDFCA-L000027](../../agents/request_budget.py#L27) | 27 | `"    \"page_fetches\": (8, 8),"` | — |
| [SRC-FDEEAFDFCA-L000028](../../agents/request_budget.py#L28) | 28 | `"    \"tool_calls\": (3, 3),"` | — |
| [SRC-FDEEAFDFCA-L000029](../../agents/request_budget.py#L29) | 29 | `"}"` | — |
| [SRC-FDEEAFDFCA-L000030](../../agents/request_budget.py#L30) | 30 | `""` | — |
| [SRC-FDEEAFDFCA-L000031](../../agents/request_budget.py#L31) | 31 | `""` | — |
| [SRC-FDEEAFDFCA-L000032](../../agents/request_budget.py#L32) | 32 | `"def _bounded_env_int(name: str, default: int, minimum: int, maximum: int) -> int:"` | — |
| [SRC-FDEEAFDFCA-L000033](../../agents/request_budget.py#L33) | 33 | `"    raw = os.getenv(name, \"\").strip()"` | — |
| [SRC-FDEEAFDFCA-L000034](../../agents/request_budget.py#L34) | 34 | `"    try:"` | — |
| [SRC-FDEEAFDFCA-L000035](../../agents/request_budget.py#L35) | 35 | `"        value = int(raw) if raw else default"` | — |
| [SRC-FDEEAFDFCA-L000036](../../agents/request_budget.py#L36) | 36 | `"    except (TypeError, ValueError):"` | — |
| [SRC-FDEEAFDFCA-L000037](../../agents/request_budget.py#L37) | 37 | `"        value = default"` | — |
| [SRC-FDEEAFDFCA-L000038](../../agents/request_budget.py#L38) | 38 | `"    return max(minimum, min(value, maximum))"` | — |
| [SRC-FDEEAFDFCA-L000039](../../agents/request_budget.py#L39) | 39 | `""` | — |
| [SRC-FDEEAFDFCA-L000040](../../agents/request_budget.py#L40) | 40 | `""` | — |
| [SRC-FDEEAFDFCA-L000041](../../agents/request_budget.py#L41) | 41 | `"class RequestBudget:"` | — |
| [SRC-FDEEAFDFCA-L000042](../../agents/request_budget.py#L42) | 42 | `"    \"\"\"Thread-safe counters and a cooperative monotonic deadline for one answer.\"\"\""` | — |
| [SRC-FDEEAFDFCA-L000043](../../agents/request_budget.py#L43) | 43 | `""` | — |
| [SRC-FDEEAFDFCA-L000044](../../agents/request_budget.py#L44) | 44 | `"    def __init__("` | — |
| [SRC-FDEEAFDFCA-L000045](../../agents/request_budget.py#L45) | 45 | `"        self,"` | — |
| [SRC-FDEEAFDFCA-L000046](../../agents/request_budget.py#L46) | 46 | `"        timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,"` | — |
| [SRC-FDEEAFDFCA-L000047](../../agents/request_budget.py#L47) | 47 | `"        limits: Mapping[str, int] \| None = None,"` | — |
| [SRC-FDEEAFDFCA-L000048](../../agents/request_budget.py#L48) | 48 | `"        clock: Callable[[], float] = time.monotonic,"` | — |
| [SRC-FDEEAFDFCA-L000049](../../agents/request_budget.py#L49) | 49 | `"    ) -> None:"` | — |
| [SRC-FDEEAFDFCA-L000050](../../agents/request_budget.py#L50) | 50 | `"        self._clock = clock"` | — |
| [SRC-FDEEAFDFCA-L000051](../../agents/request_budget.py#L51) | 51 | `"        bounded_timeout = max(10, min(int(timeout_seconds), MAX_TIMEOUT_SECONDS))"` | — |
| [SRC-FDEEAFDFCA-L000052](../../agents/request_budget.py#L52) | 52 | `"        self.started_at = clock()"` | — |
| [SRC-FDEEAFDFCA-L000053](../../agents/request_budget.py#L53) | 53 | `"        self.deadline = self.started_at + bounded_timeout"` | — |
| [SRC-FDEEAFDFCA-L000054](../../agents/request_budget.py#L54) | 54 | `"        self._limits = {"` | — |
| [SRC-FDEEAFDFCA-L000055](../../agents/request_budget.py#L55) | 55 | `"            key: max(0, min(int(value), RESOURCE_LIMITS[key][1]))"` | — |
| [SRC-FDEEAFDFCA-L000056](../../agents/request_budget.py#L56) | 56 | `"            for key, (default, _maximum) in RESOURCE_LIMITS.items()"` | — |
| [SRC-FDEEAFDFCA-L000057](../../agents/request_budget.py#L57) | 57 | `"            for value in [limits[key] if limits and key in limits else default]"` | — |
| [SRC-FDEEAFDFCA-L000058](../../agents/request_budget.py#L58) | 58 | `"        }"` | — |
| [SRC-FDEEAFDFCA-L000059](../../agents/request_budget.py#L59) | 59 | `"        self._counts = {key: 0 for key in self._limits}"` | — |
| [SRC-FDEEAFDFCA-L000060](../../agents/request_budget.py#L60) | 60 | `"        self._exhausted_reasons: set[str] = set()"` | — |
| [SRC-FDEEAFDFCA-L000061](../../agents/request_budget.py#L61) | 61 | `"        self._lock = threading.Lock()"` | — |
| [SRC-FDEEAFDFCA-L000062](../../agents/request_budget.py#L62) | 62 | `""` | — |
| [SRC-FDEEAFDFCA-L000063](../../agents/request_budget.py#L63) | 63 | `"    @classmethod"` | — |
| [SRC-FDEEAFDFCA-L000064](../../agents/request_budget.py#L64) | 64 | `"    def from_environment(cls) -> RequestBudget:"` | — |
| [SRC-FDEEAFDFCA-L000065](../../agents/request_budget.py#L65) | 65 | `"        timeout = _bounded_env_int("` | — |
| [SRC-FDEEAFDFCA-L000066](../../agents/request_budget.py#L66) | 66 | `"            \"OMARAI_REQUEST_BUDGET_SECONDS\","` | — |
| [SRC-FDEEAFDFCA-L000067](../../agents/request_budget.py#L67) | 67 | `"            DEFAULT_TIMEOUT_SECONDS,"` | — |
| [SRC-FDEEAFDFCA-L000068](../../agents/request_budget.py#L68) | 68 | `"            10,"` | — |
| [SRC-FDEEAFDFCA-L000069](../../agents/request_budget.py#L69) | 69 | `"            MAX_TIMEOUT_SECONDS,"` | — |
| [SRC-FDEEAFDFCA-L000070](../../agents/request_budget.py#L70) | 70 | `"        )"` | — |
| [SRC-FDEEAFDFCA-L000071](../../agents/request_budget.py#L71) | 71 | `"        limits = {"` | — |
| [SRC-FDEEAFDFCA-L000072](../../agents/request_budget.py#L72) | 72 | `"            key: _bounded_env_int("` | — |
| [SRC-FDEEAFDFCA-L000073](../../agents/request_budget.py#L73) | 73 | `"                f\"OMARAI_REQUEST_MAX_{key.upper()}\","` | — |
| [SRC-FDEEAFDFCA-L000074](../../agents/request_budget.py#L74) | 74 | `"                defaults[0],"` | — |
| [SRC-FDEEAFDFCA-L000075](../../agents/request_budget.py#L75) | 75 | `"                0 if key == \"tool_calls\" else 1,"` | — |
| [SRC-FDEEAFDFCA-L000076](../../agents/request_budget.py#L76) | 76 | `"                defaults[1],"` | — |
| [SRC-FDEEAFDFCA-L000077](../../agents/request_budget.py#L77) | 77 | `"            )"` | — |
| [SRC-FDEEAFDFCA-L000078](../../agents/request_budget.py#L78) | 78 | `"            for key, defaults in RESOURCE_LIMITS.items()"` | — |
| [SRC-FDEEAFDFCA-L000079](../../agents/request_budget.py#L79) | 79 | `"        }"` | — |
| [SRC-FDEEAFDFCA-L000080](../../agents/request_budget.py#L80) | 80 | `"        return cls(timeout_seconds=timeout, limits=limits)"` | — |
| [SRC-FDEEAFDFCA-L000081](../../agents/request_budget.py#L81) | 81 | `""` | — |
| [SRC-FDEEAFDFCA-L000082](../../agents/request_budget.py#L82) | 82 | `"    def remaining_seconds(self) -> float:"` | — |
| [SRC-FDEEAFDFCA-L000083](../../agents/request_budget.py#L83) | 83 | `"        return max(0.0, self.deadline - self._clock())"` | — |
| [SRC-FDEEAFDFCA-L000084](../../agents/request_budget.py#L84) | 84 | `""` | — |
| [SRC-FDEEAFDFCA-L000085](../../agents/request_budget.py#L85) | 85 | `"    def timeout_for(self, configured_seconds: float) -> float:"` | — |
| [SRC-FDEEAFDFCA-L000086](../../agents/request_budget.py#L86) | 86 | `"        \"\"\"Cap one outbound timeout to time remaining; raise instead of starting at zero.\"\"\""` | — |
| [SRC-FDEEAFDFCA-L000087](../../agents/request_budget.py#L87) | 87 | `"        remaining = self.remaining_seconds()"` | — |
| [SRC-FDEEAFDFCA-L000088](../../agents/request_budget.py#L88) | 88 | `"        if remaining <= 0:"` | — |
| [SRC-FDEEAFDFCA-L000089](../../agents/request_budget.py#L89) | 89 | `"            with self._lock:"` | — |
| [SRC-FDEEAFDFCA-L000090](../../agents/request_budget.py#L90) | 90 | `"                self._exhausted_reasons.add(\"deadline\")"` | — |
| [SRC-FDEEAFDFCA-L000091](../../agents/request_budget.py#L91) | 91 | `"            raise RequestBudgetExceeded(\"انتهت ميزانية وقت الطلب.\")"` | — |
| [SRC-FDEEAFDFCA-L000092](../../agents/request_budget.py#L92) | 92 | `"        return min(float(configured_seconds), remaining)"` | — |
| [SRC-FDEEAFDFCA-L000093](../../agents/request_budget.py#L93) | 93 | `""` | — |
| [SRC-FDEEAFDFCA-L000094](../../agents/request_budget.py#L94) | 94 | `"    def remaining_units(self, resource: str) -> int:"` | — |
| [SRC-FDEEAFDFCA-L000095](../../agents/request_budget.py#L95) | 95 | `"        \"\"\"Return unused units for a resource; zero means disabled, exhausted, or expired.\"\"\""` | — |
| [SRC-FDEEAFDFCA-L000096](../../agents/request_budget.py#L96) | 96 | `"        if resource not in self._limits:"` | — |
| [SRC-FDEEAFDFCA-L000097](../../agents/request_budget.py#L97) | 97 | `"            raise ValueError(f\"unknown request-budget resource: {resource}\")"` | — |
| [SRC-FDEEAFDFCA-L000098](../../agents/request_budget.py#L98) | 98 | `"        if self.remaining_seconds() <= 0:"` | — |
| [SRC-FDEEAFDFCA-L000099](../../agents/request_budget.py#L99) | 99 | `"            return 0"` | — |
| [SRC-FDEEAFDFCA-L000100](../../agents/request_budget.py#L100) | 100 | `"        with self._lock:"` | — |
| [SRC-FDEEAFDFCA-L000101](../../agents/request_budget.py#L101) | 101 | `"            return max(0, self._limits[resource] - self._counts[resource])"` | — |
| [SRC-FDEEAFDFCA-L000102](../../agents/request_budget.py#L102) | 102 | `""` | — |
| [SRC-FDEEAFDFCA-L000103](../../agents/request_budget.py#L103) | 103 | `"    def reserve(self, resource: str, amount: int = 1) -> None:"` | — |
| [SRC-FDEEAFDFCA-L000104](../../agents/request_budget.py#L104) | 104 | `"        \"\"\"Atomically reserve resource units before initiating external work.\"\"\""` | — |
| [SRC-FDEEAFDFCA-L000105](../../agents/request_budget.py#L105) | 105 | `"        if resource not in self._limits:"` | — |
| [SRC-FDEEAFDFCA-L000106](../../agents/request_budget.py#L106) | 106 | `"            raise ValueError(f\"unknown request-budget resource: {resource}\")"` | — |
| [SRC-FDEEAFDFCA-L000107](../../agents/request_budget.py#L107) | 107 | `"        if amount < 1:"` | — |
| [SRC-FDEEAFDFCA-L000108](../../agents/request_budget.py#L108) | 108 | `"            raise ValueError(\"reservation amount must be positive\")"` | — |
| [SRC-FDEEAFDFCA-L000109](../../agents/request_budget.py#L109) | 109 | `"        with self._lock:"` | — |
| [SRC-FDEEAFDFCA-L000110](../../agents/request_budget.py#L110) | 110 | `"            if self.remaining_seconds() <= 0:"` | — |
| [SRC-FDEEAFDFCA-L000111](../../agents/request_budget.py#L111) | 111 | `"                self._exhausted_reasons.add(\"deadline\")"` | — |
| [SRC-FDEEAFDFCA-L000112](../../agents/request_budget.py#L112) | 112 | `"                raise RequestBudgetExceeded(\"انتهت ميزانية وقت الطلب.\")"` | — |
| [SRC-FDEEAFDFCA-L000113](../../agents/request_budget.py#L113) | 113 | `"            limit = self._limits[resource]"` | — |
| [SRC-FDEEAFDFCA-L000114](../../agents/request_budget.py#L114) | 114 | `"            if self._counts[resource] + amount > limit:"` | — |
| [SRC-FDEEAFDFCA-L000115](../../agents/request_budget.py#L115) | 115 | `"                self._exhausted_reasons.add(resource)"` | — |
| [SRC-FDEEAFDFCA-L000116](../../agents/request_budget.py#L116) | 116 | `"                raise RequestBudgetExceeded("` | — |
| [SRC-FDEEAFDFCA-L000117](../../agents/request_budget.py#L117) | 117 | `"                    f\"تم بلوغ حد موارد الطلب: {resource}.\""` | — |
| [SRC-FDEEAFDFCA-L000118](../../agents/request_budget.py#L118) | 118 | `"                )"` | — |
| [SRC-FDEEAFDFCA-L000119](../../agents/request_budget.py#L119) | 119 | `"            self._counts[resource] += amount"` | — |
| [SRC-FDEEAFDFCA-L000120](../../agents/request_budget.py#L120) | 120 | `""` | — |
| [SRC-FDEEAFDFCA-L000121](../../agents/request_budget.py#L121) | 121 | `"    def snapshot(self) -> dict[str, Any]:"` | — |
| [SRC-FDEEAFDFCA-L000122](../../agents/request_budget.py#L122) | 122 | `"        with self._lock:"` | — |
| [SRC-FDEEAFDFCA-L000123](../../agents/request_budget.py#L123) | 123 | `"            counts = dict(self._counts)"` | — |
| [SRC-FDEEAFDFCA-L000124](../../agents/request_budget.py#L124) | 124 | `"            limits = dict(self._limits)"` | — |
| [SRC-FDEEAFDFCA-L000125](../../agents/request_budget.py#L125) | 125 | `"            exhausted_reasons = sorted(self._exhausted_reasons)"` | — |
| [SRC-FDEEAFDFCA-L000126](../../agents/request_budget.py#L126) | 126 | `"        remaining = self.remaining_seconds()"` | — |
| [SRC-FDEEAFDFCA-L000127](../../agents/request_budget.py#L127) | 127 | `"        return {"` | — |
| [SRC-FDEEAFDFCA-L000128](../../agents/request_budget.py#L128) | 128 | `"            \"policy\": \"cooperative_per_request_budget\","` | — |
| [SRC-FDEEAFDFCA-L000129](../../agents/request_budget.py#L129) | 129 | `"            \"timeout_seconds\": round(self.deadline - self.started_at, 3),"` | — |
| [SRC-FDEEAFDFCA-L000130](../../agents/request_budget.py#L130) | 130 | `"            \"elapsed_seconds\": round(max(0.0, self._clock() - self.started_at), 3),"` | — |
| [SRC-FDEEAFDFCA-L000131](../../agents/request_budget.py#L131) | 131 | `"            \"remaining_seconds\": round(remaining, 3),"` | — |
| [SRC-FDEEAFDFCA-L000132](../../agents/request_budget.py#L132) | 132 | `"            \"deadline_exceeded\": remaining <= 0,"` | — |
| [SRC-FDEEAFDFCA-L000133](../../agents/request_budget.py#L133) | 133 | `"            \"budget_exhausted\": bool(exhausted_reasons) or remaining <= 0,"` | — |
| [SRC-FDEEAFDFCA-L000134](../../agents/request_budget.py#L134) | 134 | `"            \"exhausted_reasons\": exhausted_reasons,"` | — |
| [SRC-FDEEAFDFCA-L000135](../../agents/request_budget.py#L135) | 135 | `"            \"counts\": counts,"` | — |
| [SRC-FDEEAFDFCA-L000136](../../agents/request_budget.py#L136) | 136 | `"            \"limits\": limits,"` | — |
| [SRC-FDEEAFDFCA-L000137](../../agents/request_budget.py#L137) | 137 | `"            \"resources_at_limit\": ["` | — |
| [SRC-FDEEAFDFCA-L000138](../../agents/request_budget.py#L138) | 138 | `"                key for key, limit in limits.items() if limit > 0 and counts[key] >= limit"` | — |
| [SRC-FDEEAFDFCA-L000139](../../agents/request_budget.py#L139) | 139 | `"            ],"` | — |
| [SRC-FDEEAFDFCA-L000140](../../agents/request_budget.py#L140) | 140 | `"            \"disabled_resources\": [key for key, limit in limits.items() if limit == 0],"` | — |
| [SRC-FDEEAFDFCA-L000141](../../agents/request_budget.py#L141) | 141 | `"            \"hard_cancellation_guaranteed\": False,"` | — |
| [SRC-FDEEAFDFCA-L000142](../../agents/request_budget.py#L142) | 142 | `"        }"` | — |
## الوكيل والمنطق

### FILE-3D565C3B85 — [agents/requirement_evidence.py](../../agents/requirement_evidence.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-3D565C3B85-L000001](../../agents/requirement_evidence.py#L1) | 1 | `"\"\"\"Build bounded evidence-candidate traces for planned research requirements."` | — |
| [SRC-3D565C3B85-L000002](../../agents/requirement_evidence.py#L2) | 2 | `""` | — |
| [SRC-3D565C3B85-L000003](../../agents/requirement_evidence.py#L3) | 3 | `"Responsibility: connect up to eight requested coverage targets to up to twelve returned"` | — |
| [SRC-3D565C3B85-L000004](../../agents/requirement_evidence.py#L4) | 4 | `"sources and their query provenance. This is lexical candidate mapping only; it never"` | — |
| [SRC-3D565C3B85-L000005](../../agents/requirement_evidence.py#L5) | 5 | `"claims source entailment, semantic support, or factual correctness."` | — |
| [SRC-3D565C3B85-L000006](../../agents/requirement_evidence.py#L6) | 6 | `""` | — |
| [SRC-3D565C3B85-L000007](../../agents/requirement_evidence.py#L7) | 7 | `"Public contract: build_requirement_evidence_ledger(targets, sources, requirement_queries)"` | — |
| [SRC-3D565C3B85-L000008](../../agents/requirement_evidence.py#L8) | 8 | `"returns one bounded record per target, with source indexes, evidence basis, and a status."` | — |
| [SRC-3D565C3B85-L000009](../../agents/requirement_evidence.py#L9) | 9 | `"Dependencies point only to shared text normalization; no network or model calls occur."` | — |
| [SRC-3D565C3B85-L000010](../../agents/requirement_evidence.py#L10) | 10 | `"\"\"\""` | — |
| [SRC-3D565C3B85-L000011](../../agents/requirement_evidence.py#L11) | 11 | `"from __future__ import annotations"` | — |
| [SRC-3D565C3B85-L000012](../../agents/requirement_evidence.py#L12) | 12 | `""` | — |
| [SRC-3D565C3B85-L000013](../../agents/requirement_evidence.py#L13) | 13 | `"import re"` | — |
| [SRC-3D565C3B85-L000014](../../agents/requirement_evidence.py#L14) | 14 | `"from typing import Any"` | — |
| [SRC-3D565C3B85-L000015](../../agents/requirement_evidence.py#L15) | 15 | `""` | — |
| [SRC-3D565C3B85-L000016](../../agents/requirement_evidence.py#L16) | 16 | `"from agents.text_normalization import normalize_text, tokenize_text"` | — |
| [SRC-3D565C3B85-L000017](../../agents/requirement_evidence.py#L17) | 17 | `""` | — |
| [SRC-3D565C3B85-L000018](../../agents/requirement_evidence.py#L18) | 18 | `"_REQUIREMENT_ALIAS_GROUPS = ("` | — |
| [SRC-3D565C3B85-L000019](../../agents/requirement_evidence.py#L19) | 19 | `"    frozenset({\"السعر\", \"سعر\", \"تكلفه\", \"التكلفه\", \"التكاليف\", \"الثمن\", \"price\", \"cost\", \"pricing\", \"fee\"}),"` | — |
| [SRC-3D565C3B85-L000020](../../agents/requirement_evidence.py#L20) | 20 | `"    frozenset({\"البطاريه\", \"بطاريه\", \"battery\", \"batteries\"}),"` | — |
| [SRC-3D565C3B85-L000021](../../agents/requirement_evidence.py#L21) | 21 | `"    frozenset({\"الكاميرا\", \"كاميرا\", \"camera\", \"cameras\", \"تصوير\"}),"` | — |
| [SRC-3D565C3B85-L000022](../../agents/requirement_evidence.py#L22) | 22 | `"    frozenset({\"ضمان\", \"الضمان\", \"warranty\", \"guarantee\"}),"` | — |
| [SRC-3D565C3B85-L000023](../../agents/requirement_evidence.py#L23) | 23 | `"    frozenset({\"الخصوصيه\", \"خصوصيه\", \"privacy\", \"الامان\", \"امان\", \"security\", \"safety\"}),"` | — |
| [SRC-3D565C3B85-L000024](../../agents/requirement_evidence.py#L24) | 24 | `"    frozenset({\"الاعتماديه\", \"اعتماديه\", \"reliability\", \"reliable\", \"الموثوقيه\"}),"` | — |
| [SRC-3D565C3B85-L000025](../../agents/requirement_evidence.py#L25) | 25 | `"    frozenset({\"الدعم\", \"الدعم الفني\", \"support\", \"customer service\", \"خدمه\"}),"` | — |
| [SRC-3D565C3B85-L000026](../../agents/requirement_evidence.py#L26) | 26 | `")"` | — |
| [SRC-3D565C3B85-L000027](../../agents/requirement_evidence.py#L27) | 27 | `""` | — |
| [SRC-3D565C3B85-L000028](../../agents/requirement_evidence.py#L28) | 28 | `""` | — |
| [SRC-3D565C3B85-L000029](../../agents/requirement_evidence.py#L29) | 29 | `"def _alias_token_groups() -> list[set[str]]:"` | — |
| [SRC-3D565C3B85-L000030](../../agents/requirement_evidence.py#L30) | 30 | `"    groups: list[set[str]] = []"` | — |
| [SRC-3D565C3B85-L000031](../../agents/requirement_evidence.py#L31) | 31 | `"    for aliases in _REQUIREMENT_ALIAS_GROUPS:"` | — |
| [SRC-3D565C3B85-L000032](../../agents/requirement_evidence.py#L32) | 32 | `"        tokens: set[str] = set()"` | — |
| [SRC-3D565C3B85-L000033](../../agents/requirement_evidence.py#L33) | 33 | `"        for alias in aliases:"` | — |
| [SRC-3D565C3B85-L000034](../../agents/requirement_evidence.py#L34) | 34 | `"            tokens.update(tokenize_text(alias, drop_stopwords=True))"` | — |
| [SRC-3D565C3B85-L000035](../../agents/requirement_evidence.py#L35) | 35 | `"        groups.append(tokens)"` | — |
| [SRC-3D565C3B85-L000036](../../agents/requirement_evidence.py#L36) | 36 | `"    return groups"` | — |
| [SRC-3D565C3B85-L000037](../../agents/requirement_evidence.py#L37) | 37 | `""` | — |
| [SRC-3D565C3B85-L000038](../../agents/requirement_evidence.py#L38) | 38 | `""` | — |
| [SRC-3D565C3B85-L000039](../../agents/requirement_evidence.py#L39) | 39 | `"def _matched_target_terms(target_tokens: list[str], available_tokens: set[str]) -> list[str]:"` | — |
| [SRC-3D565C3B85-L000040](../../agents/requirement_evidence.py#L40) | 40 | `"    \"\"\"Match target terms conservatively, with a small explicit Arabic/English alias list.\"\"\""` | — |
| [SRC-3D565C3B85-L000041](../../agents/requirement_evidence.py#L41) | 41 | `"    groups = _alias_token_groups()"` | — |
| [SRC-3D565C3B85-L000042](../../agents/requirement_evidence.py#L42) | 42 | `"    matched: list[str] = []"` | — |
| [SRC-3D565C3B85-L000043](../../agents/requirement_evidence.py#L43) | 43 | `"    for token in target_tokens:"` | — |
| [SRC-3D565C3B85-L000044](../../agents/requirement_evidence.py#L44) | 44 | `"        aliases = next((group for group in groups if token in group), {token})"` | — |
| [SRC-3D565C3B85-L000045](../../agents/requirement_evidence.py#L45) | 45 | `"        if aliases.intersection(available_tokens):"` | — |
| [SRC-3D565C3B85-L000046](../../agents/requirement_evidence.py#L46) | 46 | `"            matched.append(token)"` | — |
| [SRC-3D565C3B85-L000047](../../agents/requirement_evidence.py#L47) | 47 | `"    return matched"` | — |
| [SRC-3D565C3B85-L000048](../../agents/requirement_evidence.py#L48) | 48 | `""` | — |
| [SRC-3D565C3B85-L000049](../../agents/requirement_evidence.py#L49) | 49 | `""` | — |
| [SRC-3D565C3B85-L000050](../../agents/requirement_evidence.py#L50) | 50 | `"def build_requirement_evidence_ledger("` | — |
| [SRC-3D565C3B85-L000051](../../agents/requirement_evidence.py#L51) | 51 | `"    coverage_targets: list[str] \| None,"` | — |
| [SRC-3D565C3B85-L000052](../../agents/requirement_evidence.py#L52) | 52 | `"    sources: list[dict[str, Any]] \| None,"` | — |
| [SRC-3D565C3B85-L000053](../../agents/requirement_evidence.py#L53) | 53 | `"    requirement_queries: list[dict[str, Any]] \| None = None,"` | — |
| [SRC-3D565C3B85-L000054](../../agents/requirement_evidence.py#L54) | 54 | `") -> list[dict[str, Any]]:"` | — |
| [SRC-3D565C3B85-L000055](../../agents/requirement_evidence.py#L55) | 55 | `"    \"\"\"Link requirements to query provenance and lexical source candidates, never to truth.\"\"\""` | — |
| [SRC-3D565C3B85-L000056](../../agents/requirement_evidence.py#L56) | 56 | `"    safe_sources = ["` | — |
| [SRC-3D565C3B85-L000057](../../agents/requirement_evidence.py#L57) | 57 | `"        item for item in (sources or [])[:12]"` | — |
| [SRC-3D565C3B85-L000058](../../agents/requirement_evidence.py#L58) | 58 | `"        if isinstance(item, dict)"` | — |
| [SRC-3D565C3B85-L000059](../../agents/requirement_evidence.py#L59) | 59 | `"    ]"` | — |
| [SRC-3D565C3B85-L000060](../../agents/requirement_evidence.py#L60) | 60 | `"    query_rows = ["` | — |
| [SRC-3D565C3B85-L000061](../../agents/requirement_evidence.py#L61) | 61 | `"        item for item in (requirement_queries or [])"` | — |
| [SRC-3D565C3B85-L000062](../../agents/requirement_evidence.py#L62) | 62 | `"        if isinstance(item, dict) and isinstance(item.get(\"target\"), str)"` | — |
| [SRC-3D565C3B85-L000063](../../agents/requirement_evidence.py#L63) | 63 | `"    ]"` | — |
| [SRC-3D565C3B85-L000064](../../agents/requirement_evidence.py#L64) | 64 | `"    query_by_target = {"` | — |
| [SRC-3D565C3B85-L000065](../../agents/requirement_evidence.py#L65) | 65 | `"        normalize_text(item[\"target\"]).strip().casefold(): str(item.get(\"query\") or \"\").strip()"` | — |
| [SRC-3D565C3B85-L000066](../../agents/requirement_evidence.py#L66) | 66 | `"        for item in query_rows"` | — |
| [SRC-3D565C3B85-L000067](../../agents/requirement_evidence.py#L67) | 67 | `"    }"` | — |
| [SRC-3D565C3B85-L000068](../../agents/requirement_evidence.py#L68) | 68 | `"    any_query_metadata = any(isinstance(item.get(\"queries\"), list) for item in safe_sources)"` | — |
| [SRC-3D565C3B85-L000069](../../agents/requirement_evidence.py#L69) | 69 | `"    ledger: list[dict[str, Any]] = []"` | — |
| [SRC-3D565C3B85-L000070](../../agents/requirement_evidence.py#L70) | 70 | `""` | — |
| [SRC-3D565C3B85-L000071](../../agents/requirement_evidence.py#L71) | 71 | `"    for target in (coverage_targets or [])[:8]:"` | — |
| [SRC-3D565C3B85-L000072](../../agents/requirement_evidence.py#L72) | 72 | `"        target_text = str(target or \"\")[:120]"` | — |
| [SRC-3D565C3B85-L000073](../../agents/requirement_evidence.py#L73) | 73 | `"        target_tokens = list(dict.fromkeys(tokenize_text(target_text, drop_stopwords=True)))"` | — |
| [SRC-3D565C3B85-L000074](../../agents/requirement_evidence.py#L74) | 74 | `"        if not target_tokens:"` | — |
| [SRC-3D565C3B85-L000075](../../agents/requirement_evidence.py#L75) | 75 | `"            target_tokens = list(dict.fromkeys(tokenize_text(target_text)))"` | — |
| [SRC-3D565C3B85-L000076](../../agents/requirement_evidence.py#L76) | 76 | `"        key = normalize_text(target_text).strip().casefold()"` | — |
| [SRC-3D565C3B85-L000077](../../agents/requirement_evidence.py#L77) | 77 | `"        targeted_query = query_by_target.get(key, \"\")"` | — |
| [SRC-3D565C3B85-L000078](../../agents/requirement_evidence.py#L78) | 78 | `"        normalized_query = re.sub(r\"\\s+\", \" \", targeted_query).strip().casefold()"` | — |
| [SRC-3D565C3B85-L000079](../../agents/requirement_evidence.py#L79) | 79 | `"        query_result_indexes: list[int] = []"` | — |
| [SRC-3D565C3B85-L000080](../../agents/requirement_evidence.py#L80) | 80 | `"        candidate_sources: list[dict[str, Any]] = []"` | — |
| [SRC-3D565C3B85-L000081](../../agents/requirement_evidence.py#L81) | 81 | `""` | — |
| [SRC-3D565C3B85-L000082](../../agents/requirement_evidence.py#L82) | 82 | `"        for source_index, source in enumerate(safe_sources, 1):"` | — |
| [SRC-3D565C3B85-L000083](../../agents/requirement_evidence.py#L83) | 83 | `"            raw_queries = source.get(\"queries\", [])"` | — |
| [SRC-3D565C3B85-L000084](../../agents/requirement_evidence.py#L84) | 84 | `"            source_queries = ["` | — |
| [SRC-3D565C3B85-L000085](../../agents/requirement_evidence.py#L85) | 85 | `"                re.sub(r\"\\s+\", \" \", str(value)).strip().casefold()"` | — |
| [SRC-3D565C3B85-L000086](../../agents/requirement_evidence.py#L86) | 86 | `"                for value in raw_queries"` | — |
| [SRC-3D565C3B85-L000087](../../agents/requirement_evidence.py#L87) | 87 | `"            ] if isinstance(raw_queries, list) else []"` | — |
| [SRC-3D565C3B85-L000088](../../agents/requirement_evidence.py#L88) | 88 | `"            if normalized_query and normalized_query in source_queries:"` | — |
| [SRC-3D565C3B85-L000089](../../agents/requirement_evidence.py#L89) | 89 | `"                query_result_indexes.append(source_index)"` | — |
| [SRC-3D565C3B85-L000090](../../agents/requirement_evidence.py#L90) | 90 | `""` | — |
| [SRC-3D565C3B85-L000091](../../agents/requirement_evidence.py#L91) | 91 | `"            page_text = str(source.get(\"page_text\") or \"\")"` | — |
| [SRC-3D565C3B85-L000092](../../agents/requirement_evidence.py#L92) | 92 | `"            snippet = str(source.get(\"snippet\") or \"\")"` | — |
| [SRC-3D565C3B85-L000093](../../agents/requirement_evidence.py#L93) | 93 | `"            title = str(source.get(\"title\") or \"\")"` | — |
| [SRC-3D565C3B85-L000094](../../agents/requirement_evidence.py#L94) | 94 | `"            if bool(source.get(\"page_fetched\")) and page_text.strip():"` | — |
| [SRC-3D565C3B85-L000095](../../agents/requirement_evidence.py#L95) | 95 | `"                candidate_text = page_text"` | — |
| [SRC-3D565C3B85-L000096](../../agents/requirement_evidence.py#L96) | 96 | `"                evidence_basis = \"extracted_page_text\""` | — |
| [SRC-3D565C3B85-L000097](../../agents/requirement_evidence.py#L97) | 97 | `"            elif snippet.strip():"` | — |
| [SRC-3D565C3B85-L000098](../../agents/requirement_evidence.py#L98) | 98 | `"                candidate_text = snippet"` | — |
| [SRC-3D565C3B85-L000099](../../agents/requirement_evidence.py#L99) | 99 | `"                evidence_basis = \"search_snippet\""` | — |
| [SRC-3D565C3B85-L000100](../../agents/requirement_evidence.py#L100) | 100 | `"            elif title.strip():"` | — |
| [SRC-3D565C3B85-L000101](../../agents/requirement_evidence.py#L101) | 101 | `"                candidate_text = title"` | — |
| [SRC-3D565C3B85-L000102](../../agents/requirement_evidence.py#L102) | 102 | `"                evidence_basis = \"title_only\""` | — |
| [SRC-3D565C3B85-L000103](../../agents/requirement_evidence.py#L103) | 103 | `"            else:"` | — |
| [SRC-3D565C3B85-L000104](../../agents/requirement_evidence.py#L104) | 104 | `"                candidate_text = \"\""` | — |
| [SRC-3D565C3B85-L000105](../../agents/requirement_evidence.py#L105) | 105 | `"                evidence_basis = \"no_readable_text\""` | — |
| [SRC-3D565C3B85-L000106](../../agents/requirement_evidence.py#L106) | 106 | `"            available_tokens = set(tokenize_text(candidate_text, drop_stopwords=True))"` | — |
| [SRC-3D565C3B85-L000107](../../agents/requirement_evidence.py#L107) | 107 | `"            matched_terms = _matched_target_terms(target_tokens, available_tokens)"` | — |
| [SRC-3D565C3B85-L000108](../../agents/requirement_evidence.py#L108) | 108 | `"            ratio = len(matched_terms) / len(target_tokens) if target_tokens else 0.0"` | — |
| [SRC-3D565C3B85-L000109](../../agents/requirement_evidence.py#L109) | 109 | `"            likely_candidate = bool(matched_terms) and ("` | — |
| [SRC-3D565C3B85-L000110](../../agents/requirement_evidence.py#L110) | 110 | `"                ratio >= 0.5 if len(target_tokens) > 1 else True"` | — |
| [SRC-3D565C3B85-L000111](../../agents/requirement_evidence.py#L111) | 111 | `"            )"` | — |
| [SRC-3D565C3B85-L000112](../../agents/requirement_evidence.py#L112) | 112 | `"            if likely_candidate:"` | — |
| [SRC-3D565C3B85-L000113](../../agents/requirement_evidence.py#L113) | 113 | `"                candidate_sources.append({"` | — |
| [SRC-3D565C3B85-L000114](../../agents/requirement_evidence.py#L114) | 114 | `"                    \"source_index\": source_index,"` | — |
| [SRC-3D565C3B85-L000115](../../agents/requirement_evidence.py#L115) | 115 | `"                    \"matched_target_terms\": matched_terms[:8],"` | — |
| [SRC-3D565C3B85-L000116](../../agents/requirement_evidence.py#L116) | 116 | `"                    \"token_overlap_ratio\": round(ratio, 3),"` | — |
| [SRC-3D565C3B85-L000117](../../agents/requirement_evidence.py#L117) | 117 | `"                    \"evidence_basis\": evidence_basis,"` | — |
| [SRC-3D565C3B85-L000118](../../agents/requirement_evidence.py#L118) | 118 | `"                })"` | — |
| [SRC-3D565C3B85-L000119](../../agents/requirement_evidence.py#L119) | 119 | `""` | — |
| [SRC-3D565C3B85-L000120](../../agents/requirement_evidence.py#L120) | 120 | `"        if candidate_sources:"` | — |
| [SRC-3D565C3B85-L000121](../../agents/requirement_evidence.py#L121) | 121 | `"            status = \"candidate_evidence_found_not_verified\""` | — |
| [SRC-3D565C3B85-L000122](../../agents/requirement_evidence.py#L122) | 122 | `"        elif query_result_indexes:"` | — |
| [SRC-3D565C3B85-L000123](../../agents/requirement_evidence.py#L123) | 123 | `"            status = \"query_returned_candidates_no_lexical_signal\""` | — |
| [SRC-3D565C3B85-L000124](../../agents/requirement_evidence.py#L124) | 124 | `"        elif targeted_query and not any_query_metadata:"` | — |
| [SRC-3D565C3B85-L000125](../../agents/requirement_evidence.py#L125) | 125 | `"            status = \"query_result_linkage_unavailable\""` | — |
| [SRC-3D565C3B85-L000126](../../agents/requirement_evidence.py#L126) | 126 | `"        elif targeted_query:"` | — |
