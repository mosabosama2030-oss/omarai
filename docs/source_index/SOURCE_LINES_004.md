# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **004**
- سجلات الأسطر: **800**
- النطاق: SRC-C9CF9B54F8-L000057 إلى SRC-59CF4B7DE8-L000119
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-C9CF9B54F8 — [agents/omarai.py](../../agents/omarai.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-C9CF9B54F8-L000057](../../agents/omarai.py#L57) | 57 | `"        raise ValueError(f\"text must be at most {MAX_TEXT} characters\")"` | — |
| [SRC-C9CF9B54F8-L000058](../../agents/omarai.py#L58) | 58 | `"    body = normalize(text)"` | — |
| [SRC-C9CF9B54F8-L000059](../../agents/omarai.py#L59) | 59 | `"    excluded = [p for p in NOT_BUYER if normalize(p) in body]"` | — |
| [SRC-C9CF9B54F8-L000060](../../agents/omarai.py#L60) | 60 | `"    if excluded:"` | — |
| [SRC-C9CF9B54F8-L000061](../../agents/omarai.py#L61) | 61 | `"        return {\"score\": 0, \"label\": \"not_buyer_signal\", \"summary\": \"قد لا تكون إشارة شراء مباشرة؛ راجع النص يدويًا.\", \"matched_signals\": [{\"phrase\": p, \"category\": \"exclusion\", \"points\": 0} for p in excluded], \"warnings\": [\"تصنيف أولي وليس حكمًا نهائيًا.\"]}"` | — |
| [SRC-C9CF9B54F8-L000062](../../agents/omarai.py#L62) | 62 | `"    matches = []"` | — |
| [SRC-C9CF9B54F8-L000063](../../agents/omarai.py#L63) | 63 | `"    for category, (points, phrases) in SIGNALS.items():"` | — |
| [SRC-C9CF9B54F8-L000064](../../agents/omarai.py#L64) | 64 | `"        found = next((p for p in phrases if normalize(p) in body), None)"` | — |
| [SRC-C9CF9B54F8-L000065](../../agents/omarai.py#L65) | 65 | `"        if found:"` | — |
| [SRC-C9CF9B54F8-L000066](../../agents/omarai.py#L66) | 66 | `"            matches.append({\"phrase\": found, \"category\": category, \"points\": points})"` | — |
| [SRC-C9CF9B54F8-L000067](../../agents/omarai.py#L67) | 67 | `"    for category, terms in ((\"product_context\", product_terms), (\"location_context\", location_terms)):"` | — |
| [SRC-C9CF9B54F8-L000068](../../agents/omarai.py#L68) | 68 | `"        found = next((normalize(t) for t in terms if isinstance(t, str) and normalize(t) and normalize(t) in body), None)"` | — |
| [SRC-C9CF9B54F8-L000069](../../agents/omarai.py#L69) | 69 | `"        if found:"` | — |
| [SRC-C9CF9B54F8-L000070](../../agents/omarai.py#L70) | 70 | `"            matches.append({\"phrase\": found, \"category\": category, \"points\": 10})"` | — |
| [SRC-C9CF9B54F8-L000071](../../agents/omarai.py#L71) | 71 | `"    score = min(100, sum(x[\"points\"] for x in matches))"` | — |
| [SRC-C9CF9B54F8-L000072](../../agents/omarai.py#L72) | 72 | `"    label = \"high_intent\" if score >= 55 and any(x[\"category\"] == \"high\" for x in matches) else \"medium_intent\" if score >= 40 else \"early_research\" if score >= 20 else \"unclear\""` | — |
| [SRC-C9CF9B54F8-L000073](../../agents/omarai.py#L73) | 73 | `"    return {\"score\": score, \"label\": label, \"summary\": {\"high_intent\":\"إشارة قوية نسبيًا وفق قواعد بسيطة وتحتاج مراجعة بشرية.\",\"medium_intent\":\"مؤشرات اهتمام تستحق التأهيل والتحقق.\",\"early_research\":\"اهتمام مبكر؛ ليس عميلًا مؤهلًا بعد.\",\"unclear\":\"لا توجد مؤشرات كافية.\"}[label], \"matched_signals\": matches, \"warnings\": [\"الدرجة ليست احتمالًا إحصائيًا للشراء.\", \"لا تثبت هوية الكاتب أو قدرته على الدفع أو نيته.\", \"استخدم مصادر عامة ومسموحًا بمعالجتها فقط.\"]}"` | — |
| [SRC-C9CF9B54F8-L000074](../../agents/omarai.py#L74) | 74 | `""` | — |
| [SRC-C9CF9B54F8-L000075](../../agents/omarai.py#L75) | 75 | `"def validate_url(url: str) -> str:"` | — |
| [SRC-C9CF9B54F8-L000076](../../agents/omarai.py#L76) | 76 | `"    parsed = urlparse(str(url or \"\").strip())"` | — |
| [SRC-C9CF9B54F8-L000077](../../agents/omarai.py#L77) | 77 | `"    if parsed.scheme not in (\"http\", \"https\") or not parsed.netloc or parsed.username or parsed.password:"` | — |
| [SRC-C9CF9B54F8-L000078](../../agents/omarai.py#L78) | 78 | `"        raise ValueError(\"source_url must be an absolute http(s) URL without embedded credentials\")"` | — |
| [SRC-C9CF9B54F8-L000079](../../agents/omarai.py#L79) | 79 | `"    if len(url) > 2048:"` | — |
| [SRC-C9CF9B54F8-L000080](../../agents/omarai.py#L80) | 80 | `"        raise ValueError(\"source_url is too long\")"` | — |
| [SRC-C9CF9B54F8-L000081](../../agents/omarai.py#L81) | 81 | `"    return url.strip()"` | — |
| [SRC-C9CF9B54F8-L000082](../../agents/omarai.py#L82) | 82 | `""` | — |
| [SRC-C9CF9B54F8-L000083](../../agents/omarai.py#L83) | 83 | `"class LeadStore:"` | — |
| [SRC-C9CF9B54F8-L000084](../../agents/omarai.py#L84) | 84 | `"    \"\"\"Tenant-scoped SQLite storage for customer-demand signals.\"\"\""` | — |
| [SRC-C9CF9B54F8-L000085](../../agents/omarai.py#L85) | 85 | `""` | — |
| [SRC-C9CF9B54F8-L000086](../../agents/omarai.py#L86) | 86 | `"    ROLES: ClassVar[frozenset[str]] = frozenset({\"owner\", \"admin\", \"manager\", \"sales_agent\", \"viewer\"})"` | — |
| [SRC-C9CF9B54F8-L000087](../../agents/omarai.py#L87) | 87 | `"    DEFAULT_TENANT_ID = \"default\""` | — |
| [SRC-C9CF9B54F8-L000088](../../agents/omarai.py#L88) | 88 | `""` | — |
| [SRC-C9CF9B54F8-L000089](../../agents/omarai.py#L89) | 89 | `"    def __init__("` | — |
| [SRC-C9CF9B54F8-L000090](../../agents/omarai.py#L90) | 90 | `"        self,"` | — |
| [SRC-C9CF9B54F8-L000091](../../agents/omarai.py#L91) | 91 | `"        path: str \| Path \| None = None,"` | — |
| [SRC-C9CF9B54F8-L000092](../../agents/omarai.py#L92) | 92 | `"        *,"` | — |
| [SRC-C9CF9B54F8-L000093](../../agents/omarai.py#L93) | 93 | `"        default_tenant_id: str = DEFAULT_TENANT_ID,"` | — |
| [SRC-C9CF9B54F8-L000094](../../agents/omarai.py#L94) | 94 | `"        default_tenant_name: str = \"المنشأة الرئيسية\","` | — |
| [SRC-C9CF9B54F8-L000095](../../agents/omarai.py#L95) | 95 | `"    ):"` | — |
| [SRC-C9CF9B54F8-L000096](../../agents/omarai.py#L96) | 96 | `"        self.path = Path(path or Path.home() / \".omarai\" / \"omarai.sqlite3\").expanduser()"` | — |
| [SRC-C9CF9B54F8-L000097](../../agents/omarai.py#L97) | 97 | `"        self.path.parent.mkdir(parents=True, exist_ok=True)"` | — |
| [SRC-C9CF9B54F8-L000098](../../agents/omarai.py#L98) | 98 | `"        self.default_tenant_id = self._required_id(default_tenant_id, \"tenant_id\")"` | — |
| [SRC-C9CF9B54F8-L000099](../../agents/omarai.py#L99) | 99 | `"        default_tenant_name = str(default_tenant_name or \"\").strip()[:200]"` | — |
| [SRC-C9CF9B54F8-L000100](../../agents/omarai.py#L100) | 100 | `"        if not default_tenant_name:"` | — |
| [SRC-C9CF9B54F8-L000101](../../agents/omarai.py#L101) | 101 | `"            raise ValueError(\"company name is required\")"` | — |
| [SRC-C9CF9B54F8-L000102](../../agents/omarai.py#L102) | 102 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000103](../../agents/omarai.py#L103) | 103 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L000104](../../agents/omarai.py#L104) | 104 | `"                \"\"\"CREATE TABLE IF NOT EXISTS companies ("` | — |
| [SRC-C9CF9B54F8-L000105](../../agents/omarai.py#L105) | 105 | `"                    id TEXT PRIMARY KEY,"` | — |
| [SRC-C9CF9B54F8-L000106](../../agents/omarai.py#L106) | 106 | `"                    name TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000107](../../agents/omarai.py#L107) | 107 | `"                    status TEXT NOT NULL DEFAULT 'active'"` | — |
| [SRC-C9CF9B54F8-L000108](../../agents/omarai.py#L108) | 108 | `"                        CHECK(status IN ('active', 'suspended', 'archived')),"` | — |
| [SRC-C9CF9B54F8-L000109](../../agents/omarai.py#L109) | 109 | `"                    created_at TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000110](../../agents/omarai.py#L110) | 110 | `"                    updated_at TEXT NOT NULL"` | — |
| [SRC-C9CF9B54F8-L000111](../../agents/omarai.py#L111) | 111 | `"                )\"\"\""` | — |
| [SRC-C9CF9B54F8-L000112](../../agents/omarai.py#L112) | 112 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000113](../../agents/omarai.py#L113) | 113 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L000114](../../agents/omarai.py#L114) | 114 | `"                \"\"\"CREATE TABLE IF NOT EXISTS users ("` | — |
| [SRC-C9CF9B54F8-L000115](../../agents/omarai.py#L115) | 115 | `"                    id TEXT PRIMARY KEY,"` | — |
| [SRC-C9CF9B54F8-L000116](../../agents/omarai.py#L116) | 116 | `"                    email TEXT UNIQUE,"` | — |
| [SRC-C9CF9B54F8-L000117](../../agents/omarai.py#L117) | 117 | `"                    display_name TEXT NOT NULL DEFAULT '',"` | — |
| [SRC-C9CF9B54F8-L000118](../../agents/omarai.py#L118) | 118 | `"                    status TEXT NOT NULL DEFAULT 'active'"` | — |
| [SRC-C9CF9B54F8-L000119](../../agents/omarai.py#L119) | 119 | `"                        CHECK(status IN ('active', 'disabled')),"` | — |
| [SRC-C9CF9B54F8-L000120](../../agents/omarai.py#L120) | 120 | `"                    created_at TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000121](../../agents/omarai.py#L121) | 121 | `"                    updated_at TEXT NOT NULL"` | — |
| [SRC-C9CF9B54F8-L000122](../../agents/omarai.py#L122) | 122 | `"                )\"\"\""` | — |
| [SRC-C9CF9B54F8-L000123](../../agents/omarai.py#L123) | 123 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000124](../../agents/omarai.py#L124) | 124 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L000125](../../agents/omarai.py#L125) | 125 | `"                \"\"\"CREATE TABLE IF NOT EXISTS tenant_memberships ("` | — |
| [SRC-C9CF9B54F8-L000126](../../agents/omarai.py#L126) | 126 | `"                    tenant_id TEXT NOT NULL REFERENCES companies(id) ON DELETE CASCADE,"` | — |
| [SRC-C9CF9B54F8-L000127](../../agents/omarai.py#L127) | 127 | `"                    user_id TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,"` | — |
| [SRC-C9CF9B54F8-L000128](../../agents/omarai.py#L128) | 128 | `"                    role TEXT NOT NULL CHECK(role IN ("` | — |
| [SRC-C9CF9B54F8-L000129](../../agents/omarai.py#L129) | 129 | `"                        'owner', 'admin', 'manager', 'sales_agent', 'viewer'"` | — |
| [SRC-C9CF9B54F8-L000130](../../agents/omarai.py#L130) | 130 | `"                    )),"` | — |
| [SRC-C9CF9B54F8-L000131](../../agents/omarai.py#L131) | 131 | `"                    status TEXT NOT NULL DEFAULT 'active'"` | — |
| [SRC-C9CF9B54F8-L000132](../../agents/omarai.py#L132) | 132 | `"                        CHECK(status IN ('active', 'suspended', 'revoked')),"` | — |
| [SRC-C9CF9B54F8-L000133](../../agents/omarai.py#L133) | 133 | `"                    created_at TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000134](../../agents/omarai.py#L134) | 134 | `"                    updated_at TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000135](../../agents/omarai.py#L135) | 135 | `"                    PRIMARY KEY (tenant_id, user_id)"` | — |
| [SRC-C9CF9B54F8-L000136](../../agents/omarai.py#L136) | 136 | `"                )\"\"\""` | — |
| [SRC-C9CF9B54F8-L000137](../../agents/omarai.py#L137) | 137 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000138](../../agents/omarai.py#L138) | 138 | `"            now = now_utc()"` | — |
| [SRC-C9CF9B54F8-L000139](../../agents/omarai.py#L139) | 139 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L000140](../../agents/omarai.py#L140) | 140 | `"                \"\"\"INSERT OR IGNORE INTO companies"` | — |
| [SRC-C9CF9B54F8-L000141](../../agents/omarai.py#L141) | 141 | `"                   (id, name, status, created_at, updated_at)"` | — |
| [SRC-C9CF9B54F8-L000142](../../agents/omarai.py#L142) | 142 | `"                   VALUES (?, ?, 'active', ?, ?)\"\"\","` | — |
| [SRC-C9CF9B54F8-L000143](../../agents/omarai.py#L143) | 143 | `"                (self.default_tenant_id, default_tenant_name, now, now),"` | — |
| [SRC-C9CF9B54F8-L000144](../../agents/omarai.py#L144) | 144 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000145](../../agents/omarai.py#L145) | 145 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L000146](../../agents/omarai.py#L146) | 146 | `"                \"\"\"INSERT OR IGNORE INTO users"` | — |
| [SRC-C9CF9B54F8-L000147](../../agents/omarai.py#L147) | 147 | `"                   (id, email, display_name, status, created_at, updated_at)"` | — |
| [SRC-C9CF9B54F8-L000148](../../agents/omarai.py#L148) | 148 | `"                   VALUES ('operator', NULL, 'Local operator', 'active', ?, ?)\"\"\","` | — |
| [SRC-C9CF9B54F8-L000149](../../agents/omarai.py#L149) | 149 | `"                (now, now),"` | — |
| [SRC-C9CF9B54F8-L000150](../../agents/omarai.py#L150) | 150 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000151](../../agents/omarai.py#L151) | 151 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L000152](../../agents/omarai.py#L152) | 152 | `"                \"\"\"INSERT OR IGNORE INTO tenant_memberships"` | — |
| [SRC-C9CF9B54F8-L000153](../../agents/omarai.py#L153) | 153 | `"                   (tenant_id, user_id, role, status, created_at, updated_at)"` | — |
| [SRC-C9CF9B54F8-L000154](../../agents/omarai.py#L154) | 154 | `"                   VALUES (?, 'operator', 'owner', 'active', ?, ?)\"\"\","` | — |
| [SRC-C9CF9B54F8-L000155](../../agents/omarai.py#L155) | 155 | `"                (self.default_tenant_id, now, now),"` | — |
| [SRC-C9CF9B54F8-L000156](../../agents/omarai.py#L156) | 156 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000157](../../agents/omarai.py#L157) | 157 | `"            self._ensure_tenant_scoped_leads_table(db)"` | — |
| [SRC-C9CF9B54F8-L000158](../../agents/omarai.py#L158) | 158 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L000159](../../agents/omarai.py#L159) | 159 | `"                \"\"\"CREATE INDEX IF NOT EXISTS leads_tenant_status_idx"` | — |
| [SRC-C9CF9B54F8-L000160](../../agents/omarai.py#L160) | 160 | `"                   ON leads(tenant_id, status, created_at DESC)\"\"\""` | — |
| [SRC-C9CF9B54F8-L000161](../../agents/omarai.py#L161) | 161 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000162](../../agents/omarai.py#L162) | 162 | `""` | — |
| [SRC-C9CF9B54F8-L000163](../../agents/omarai.py#L163) | 163 | `"    def connect(self):"` | — |
| [SRC-C9CF9B54F8-L000164](../../agents/omarai.py#L164) | 164 | `"        db = sqlite3.connect(self.path, timeout=10)"` | — |
| [SRC-C9CF9B54F8-L000165](../../agents/omarai.py#L165) | 165 | `"        db.row_factory = sqlite3.Row"` | — |
| [SRC-C9CF9B54F8-L000166](../../agents/omarai.py#L166) | 166 | `"        db.execute(\"PRAGMA foreign_keys = ON\")"` | — |
| [SRC-C9CF9B54F8-L000167](../../agents/omarai.py#L167) | 167 | `"        return db"` | — |
| [SRC-C9CF9B54F8-L000168](../../agents/omarai.py#L168) | 168 | `""` | — |
| [SRC-C9CF9B54F8-L000169](../../agents/omarai.py#L169) | 169 | `"    @staticmethod"` | — |
| [SRC-C9CF9B54F8-L000170](../../agents/omarai.py#L170) | 170 | `"    def _required_id(value: object, field: str) -> str:"` | — |
| [SRC-C9CF9B54F8-L000171](../../agents/omarai.py#L171) | 171 | `"        result = str(value or \"\").strip()"` | — |
| [SRC-C9CF9B54F8-L000172](../../agents/omarai.py#L172) | 172 | `"        if not result or len(result) > 128:"` | — |
| [SRC-C9CF9B54F8-L000173](../../agents/omarai.py#L173) | 173 | `"            raise ValueError(f\"{field} must be a non-empty value of at most 128 characters\")"` | — |
| [SRC-C9CF9B54F8-L000174](../../agents/omarai.py#L174) | 174 | `"        return result"` | — |
| [SRC-C9CF9B54F8-L000175](../../agents/omarai.py#L175) | 175 | `""` | — |
| [SRC-C9CF9B54F8-L000176](../../agents/omarai.py#L176) | 176 | `"    @staticmethod"` | — |
| [SRC-C9CF9B54F8-L000177](../../agents/omarai.py#L177) | 177 | `"    def _create_leads_table(db: sqlite3.Connection) -> None:"` | — |
| [SRC-C9CF9B54F8-L000178](../../agents/omarai.py#L178) | 178 | `"        db.execute("` | — |
| [SRC-C9CF9B54F8-L000179](../../agents/omarai.py#L179) | 179 | `"            \"\"\"CREATE TABLE leads ("` | — |
| [SRC-C9CF9B54F8-L000180](../../agents/omarai.py#L180) | 180 | `"                id TEXT PRIMARY KEY,"` | — |
| [SRC-C9CF9B54F8-L000181](../../agents/omarai.py#L181) | 181 | `"                tenant_id TEXT NOT NULL REFERENCES companies(id) ON DELETE CASCADE,"` | — |
| [SRC-C9CF9B54F8-L000182](../../agents/omarai.py#L182) | 182 | `"                fingerprint TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000183](../../agents/omarai.py#L183) | 183 | `"                text TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000184](../../agents/omarai.py#L184) | 184 | `"                source_url TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000185](../../agents/omarai.py#L185) | 185 | `"                platform TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000186](../../agents/omarai.py#L186) | 186 | `"                observed_at TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000187](../../agents/omarai.py#L187) | 187 | `"                assessment TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000188](../../agents/omarai.py#L188) | 188 | `"                status TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000189](../../agents/omarai.py#L189) | 189 | `"                note TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000190](../../agents/omarai.py#L190) | 190 | `"                created_at TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000191](../../agents/omarai.py#L191) | 191 | `"                updated_at TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000192](../../agents/omarai.py#L192) | 192 | `"                UNIQUE (tenant_id, fingerprint)"` | — |
| [SRC-C9CF9B54F8-L000193](../../agents/omarai.py#L193) | 193 | `"            )\"\"\""` | — |
| [SRC-C9CF9B54F8-L000194](../../agents/omarai.py#L194) | 194 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000195](../../agents/omarai.py#L195) | 195 | `""` | — |
| [SRC-C9CF9B54F8-L000196](../../agents/omarai.py#L196) | 196 | `"    def _ensure_tenant_scoped_leads_table(self, db: sqlite3.Connection) -> None:"` | — |
| [SRC-C9CF9B54F8-L000197](../../agents/omarai.py#L197) | 197 | `"        table = db.execute("` | — |
| [SRC-C9CF9B54F8-L000198](../../agents/omarai.py#L198) | 198 | `"            \"SELECT name FROM sqlite_master WHERE type='table' AND name='leads'\""` | — |
| [SRC-C9CF9B54F8-L000199](../../agents/omarai.py#L199) | 199 | `"        ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000200](../../agents/omarai.py#L200) | 200 | `"        if table is None:"` | — |
| [SRC-C9CF9B54F8-L000201](../../agents/omarai.py#L201) | 201 | `"            self._create_leads_table(db)"` | — |
| [SRC-C9CF9B54F8-L000202](../../agents/omarai.py#L202) | 202 | `"            return"` | — |
| [SRC-C9CF9B54F8-L000203](../../agents/omarai.py#L203) | 203 | `""` | — |
| [SRC-C9CF9B54F8-L000204](../../agents/omarai.py#L204) | 204 | `"        columns = {"` | — |
| [SRC-C9CF9B54F8-L000205](../../agents/omarai.py#L205) | 205 | `"            row[\"name\"] for row in db.execute(\"PRAGMA table_info(leads)\").fetchall()"` | — |
| [SRC-C9CF9B54F8-L000206](../../agents/omarai.py#L206) | 206 | `"        }"` | — |
| [SRC-C9CF9B54F8-L000207](../../agents/omarai.py#L207) | 207 | `"        if \"tenant_id\" in columns:"` | — |
| [SRC-C9CF9B54F8-L000208](../../agents/omarai.py#L208) | 208 | `"            required = {"` | — |
| [SRC-C9CF9B54F8-L000209](../../agents/omarai.py#L209) | 209 | `"                \"id\", \"fingerprint\", \"text\", \"source_url\", \"platform\", \"observed_at\","` | — |
| [SRC-C9CF9B54F8-L000210](../../agents/omarai.py#L210) | 210 | `"                \"assessment\", \"status\", \"note\", \"created_at\", \"updated_at\","` | — |
| [SRC-C9CF9B54F8-L000211](../../agents/omarai.py#L211) | 211 | `"            }"` | — |
| [SRC-C9CF9B54F8-L000212](../../agents/omarai.py#L212) | 212 | `"            missing = required - columns"` | — |
| [SRC-C9CF9B54F8-L000213](../../agents/omarai.py#L213) | 213 | `"            if missing:"` | — |
| [SRC-C9CF9B54F8-L000214](../../agents/omarai.py#L214) | 214 | `"                raise RuntimeError("` | — |
| [SRC-C9CF9B54F8-L000215](../../agents/omarai.py#L215) | 215 | `"                    \"Unsupported leads schema; missing columns: \" + \", \".join(sorted(missing))"` | — |
| [SRC-C9CF9B54F8-L000216](../../agents/omarai.py#L216) | 216 | `"                )"` | — |
| [SRC-C9CF9B54F8-L000217](../../agents/omarai.py#L217) | 217 | `"            return"` | — |
| [SRC-C9CF9B54F8-L000218](../../agents/omarai.py#L218) | 218 | `""` | — |
| [SRC-C9CF9B54F8-L000219](../../agents/omarai.py#L219) | 219 | `"        # Preserve every legacy lead under the initial company while replacing the"` | — |
| [SRC-C9CF9B54F8-L000220](../../agents/omarai.py#L220) | 220 | `"        # global UNIQUE(fingerprint) constraint with UNIQUE(tenant_id, fingerprint)."` | — |
| [SRC-C9CF9B54F8-L000221](../../agents/omarai.py#L221) | 221 | `"        db.execute(\"DROP INDEX IF EXISTS leads_status_idx\")"` | — |
| [SRC-C9CF9B54F8-L000222](../../agents/omarai.py#L222) | 222 | `"        db.execute(\"ALTER TABLE leads RENAME TO leads_legacy_migration\")"` | — |
| [SRC-C9CF9B54F8-L000223](../../agents/omarai.py#L223) | 223 | `"        self._create_leads_table(db)"` | — |
| [SRC-C9CF9B54F8-L000224](../../agents/omarai.py#L224) | 224 | `"        db.execute("` | — |
| [SRC-C9CF9B54F8-L000225](../../agents/omarai.py#L225) | 225 | `"            \"\"\"INSERT INTO leads ("` | — |
| [SRC-C9CF9B54F8-L000226](../../agents/omarai.py#L226) | 226 | `"                   id, tenant_id, fingerprint, text, source_url, platform, observed_at,"` | — |
| [SRC-C9CF9B54F8-L000227](../../agents/omarai.py#L227) | 227 | `"                   assessment, status, note, created_at, updated_at"` | — |
| [SRC-C9CF9B54F8-L000228](../../agents/omarai.py#L228) | 228 | `"               )"` | — |
| [SRC-C9CF9B54F8-L000229](../../agents/omarai.py#L229) | 229 | `"               SELECT id, ?, fingerprint, text, source_url, platform, observed_at,"` | — |
| [SRC-C9CF9B54F8-L000230](../../agents/omarai.py#L230) | 230 | `"                      assessment, status, note, created_at, updated_at"` | — |
| [SRC-C9CF9B54F8-L000231](../../agents/omarai.py#L231) | 231 | `"               FROM leads_legacy_migration\"\"\","` | — |
| [SRC-C9CF9B54F8-L000232](../../agents/omarai.py#L232) | 232 | `"            (self.default_tenant_id,),"` | — |
| [SRC-C9CF9B54F8-L000233](../../agents/omarai.py#L233) | 233 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000234](../../agents/omarai.py#L234) | 234 | `"        db.execute(\"DROP TABLE leads_legacy_migration\")"` | — |
| [SRC-C9CF9B54F8-L000235](../../agents/omarai.py#L235) | 235 | `""` | — |
| [SRC-C9CF9B54F8-L000236](../../agents/omarai.py#L236) | 236 | `"    def create_company(self, company_id: str, name: str) -> None:"` | — |
| [SRC-C9CF9B54F8-L000237](../../agents/omarai.py#L237) | 237 | `"        company_id = self._required_id(company_id, \"company_id\")"` | — |
| [SRC-C9CF9B54F8-L000238](../../agents/omarai.py#L238) | 238 | `"        name = str(name or \"\").strip()[:200]"` | — |
| [SRC-C9CF9B54F8-L000239](../../agents/omarai.py#L239) | 239 | `"        if not name:"` | — |
| [SRC-C9CF9B54F8-L000240](../../agents/omarai.py#L240) | 240 | `"            raise ValueError(\"company name is required\")"` | — |
| [SRC-C9CF9B54F8-L000241](../../agents/omarai.py#L241) | 241 | `"        now = now_utc()"` | — |
| [SRC-C9CF9B54F8-L000242](../../agents/omarai.py#L242) | 242 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000243](../../agents/omarai.py#L243) | 243 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L000244](../../agents/omarai.py#L244) | 244 | `"                \"\"\"INSERT INTO companies (id, name, status, created_at, updated_at)"` | — |
| [SRC-C9CF9B54F8-L000245](../../agents/omarai.py#L245) | 245 | `"                   VALUES (?, ?, 'active', ?, ?)\"\"\","` | — |
| [SRC-C9CF9B54F8-L000246](../../agents/omarai.py#L246) | 246 | `"                (company_id, name, now, now),"` | — |
| [SRC-C9CF9B54F8-L000247](../../agents/omarai.py#L247) | 247 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000248](../../agents/omarai.py#L248) | 248 | `""` | — |
| [SRC-C9CF9B54F8-L000249](../../agents/omarai.py#L249) | 249 | `"    def create_user("` | — |
| [SRC-C9CF9B54F8-L000250](../../agents/omarai.py#L250) | 250 | `"        self, user_id: str, *, email: str \| None = None, display_name: str = \"\""` | — |
| [SRC-C9CF9B54F8-L000251](../../agents/omarai.py#L251) | 251 | `"    ) -> None:"` | — |
| [SRC-C9CF9B54F8-L000252](../../agents/omarai.py#L252) | 252 | `"        user_id = self._required_id(user_id, \"user_id\")"` | — |
| [SRC-C9CF9B54F8-L000253](../../agents/omarai.py#L253) | 253 | `"        email = str(email or \"\").strip().lower() or None"` | — |
| [SRC-C9CF9B54F8-L000254](../../agents/omarai.py#L254) | 254 | `"        if email and len(email) > 320:"` | — |
| [SRC-C9CF9B54F8-L000255](../../agents/omarai.py#L255) | 255 | `"            raise ValueError(\"email is too long\")"` | — |
| [SRC-C9CF9B54F8-L000256](../../agents/omarai.py#L256) | 256 | `"        now = now_utc()"` | — |
| [SRC-C9CF9B54F8-L000257](../../agents/omarai.py#L257) | 257 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000258](../../agents/omarai.py#L258) | 258 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L000259](../../agents/omarai.py#L259) | 259 | `"                \"\"\"INSERT INTO users"` | — |
| [SRC-C9CF9B54F8-L000260](../../agents/omarai.py#L260) | 260 | `"                   (id, email, display_name, status, created_at, updated_at)"` | — |
| [SRC-C9CF9B54F8-L000261](../../agents/omarai.py#L261) | 261 | `"                   VALUES (?, ?, ?, 'active', ?, ?)\"\"\","` | — |
| [SRC-C9CF9B54F8-L000262](../../agents/omarai.py#L262) | 262 | `"                (user_id, email, str(display_name or \"\")[:200], now, now),"` | — |
| [SRC-C9CF9B54F8-L000263](../../agents/omarai.py#L263) | 263 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000264](../../agents/omarai.py#L264) | 264 | `""` | — |
| [SRC-C9CF9B54F8-L000265](../../agents/omarai.py#L265) | 265 | `"    def add_membership(self, tenant_id: str, user_id: str, role: str = \"sales_agent\") -> None:"` | — |
| [SRC-C9CF9B54F8-L000266](../../agents/omarai.py#L266) | 266 | `"        tenant_id = self._required_id(tenant_id, \"tenant_id\")"` | — |
| [SRC-C9CF9B54F8-L000267](../../agents/omarai.py#L267) | 267 | `"        user_id = self._required_id(user_id, \"user_id\")"` | — |
| [SRC-C9CF9B54F8-L000268](../../agents/omarai.py#L268) | 268 | `"        if role not in self.ROLES:"` | — |
| [SRC-C9CF9B54F8-L000269](../../agents/omarai.py#L269) | 269 | `"            raise ValueError(\"unsupported membership role\")"` | — |
| [SRC-C9CF9B54F8-L000270](../../agents/omarai.py#L270) | 270 | `"        now = now_utc()"` | — |
| [SRC-C9CF9B54F8-L000271](../../agents/omarai.py#L271) | 271 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000272](../../agents/omarai.py#L272) | 272 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L000273](../../agents/omarai.py#L273) | 273 | `"                \"\"\"INSERT INTO tenant_memberships"` | — |
| [SRC-C9CF9B54F8-L000274](../../agents/omarai.py#L274) | 274 | `"                   (tenant_id, user_id, role, status, created_at, updated_at)"` | — |
| [SRC-C9CF9B54F8-L000275](../../agents/omarai.py#L275) | 275 | `"                   VALUES (?, ?, ?, 'active', ?, ?)"` | — |
| [SRC-C9CF9B54F8-L000276](../../agents/omarai.py#L276) | 276 | `"                   ON CONFLICT(tenant_id, user_id) DO UPDATE SET"` | — |
| [SRC-C9CF9B54F8-L000277](../../agents/omarai.py#L277) | 277 | `"                       role=excluded.role, status='active', updated_at=excluded.updated_at\"\"\","` | — |
| [SRC-C9CF9B54F8-L000278](../../agents/omarai.py#L278) | 278 | `"                (tenant_id, user_id, role, now, now),"` | — |
| [SRC-C9CF9B54F8-L000279](../../agents/omarai.py#L279) | 279 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000280](../../agents/omarai.py#L280) | 280 | `""` | — |
| [SRC-C9CF9B54F8-L000281](../../agents/omarai.py#L281) | 281 | `"    def resolve_membership("` | — |
| [SRC-C9CF9B54F8-L000282](../../agents/omarai.py#L282) | 282 | `"        self, user_id: str, requested_tenant_id: str \| None = None"` | — |
| [SRC-C9CF9B54F8-L000283](../../agents/omarai.py#L283) | 283 | `"    ) -> dict \| None:"` | — |
| [SRC-C9CF9B54F8-L000284](../../agents/omarai.py#L284) | 284 | `"        \"\"\"Resolve an active tenant only through a persisted user membership.\"\"\""` | — |
| [SRC-C9CF9B54F8-L000285](../../agents/omarai.py#L285) | 285 | `"        user_id = self._required_id(user_id, \"user_id\")"` | — |
| [SRC-C9CF9B54F8-L000286](../../agents/omarai.py#L286) | 286 | `"        if requested_tenant_id is not None:"` | — |
| [SRC-C9CF9B54F8-L000287](../../agents/omarai.py#L287) | 287 | `"            requested_tenant_id = self._required_id(requested_tenant_id, \"tenant_id\")"` | — |
| [SRC-C9CF9B54F8-L000288](../../agents/omarai.py#L288) | 288 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000289](../../agents/omarai.py#L289) | 289 | `"            rows = db.execute("` | — |
| [SRC-C9CF9B54F8-L000290](../../agents/omarai.py#L290) | 290 | `"                \"\"\"SELECT m.tenant_id, m.user_id, m.role, c.name AS company_name"` | — |
| [SRC-C9CF9B54F8-L000291](../../agents/omarai.py#L291) | 291 | `"                   FROM tenant_memberships AS m"` | — |
| [SRC-C9CF9B54F8-L000292](../../agents/omarai.py#L292) | 292 | `"                   JOIN users AS u ON u.id = m.user_id"` | — |
| [SRC-C9CF9B54F8-L000293](../../agents/omarai.py#L293) | 293 | `"                   JOIN companies AS c ON c.id = m.tenant_id"` | — |
| [SRC-C9CF9B54F8-L000294](../../agents/omarai.py#L294) | 294 | `"                   WHERE m.user_id = ?"` | — |
| [SRC-C9CF9B54F8-L000295](../../agents/omarai.py#L295) | 295 | `"                     AND m.status = 'active'"` | — |
| [SRC-C9CF9B54F8-L000296](../../agents/omarai.py#L296) | 296 | `"                     AND u.status = 'active'"` | — |
| [SRC-C9CF9B54F8-L000297](../../agents/omarai.py#L297) | 297 | `"                     AND c.status = 'active'"` | — |
| [SRC-C9CF9B54F8-L000298](../../agents/omarai.py#L298) | 298 | `"                   ORDER BY m.tenant_id\"\"\","` | — |
| [SRC-C9CF9B54F8-L000299](../../agents/omarai.py#L299) | 299 | `"                (user_id,),"` | — |
| [SRC-C9CF9B54F8-L000300](../../agents/omarai.py#L300) | 300 | `"            ).fetchall()"` | — |
| [SRC-C9CF9B54F8-L000301](../../agents/omarai.py#L301) | 301 | `"        memberships = [dict(row) for row in rows]"` | — |
| [SRC-C9CF9B54F8-L000302](../../agents/omarai.py#L302) | 302 | `"        if requested_tenant_id is not None:"` | — |
| [SRC-C9CF9B54F8-L000303](../../agents/omarai.py#L303) | 303 | `"            return next("` | — |
| [SRC-C9CF9B54F8-L000304](../../agents/omarai.py#L304) | 304 | `"                (item for item in memberships if item[\"tenant_id\"] == requested_tenant_id),"` | — |
| [SRC-C9CF9B54F8-L000305](../../agents/omarai.py#L305) | 305 | `"                None,"` | — |
| [SRC-C9CF9B54F8-L000306](../../agents/omarai.py#L306) | 306 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000307](../../agents/omarai.py#L307) | 307 | `"        if len(memberships) == 1:"` | — |
| [SRC-C9CF9B54F8-L000308](../../agents/omarai.py#L308) | 308 | `"            return memberships[0]"` | — |
| [SRC-C9CF9B54F8-L000309](../../agents/omarai.py#L309) | 309 | `"        return next("` | — |
| [SRC-C9CF9B54F8-L000310](../../agents/omarai.py#L310) | 310 | `"            (item for item in memberships if item[\"tenant_id\"] == self.default_tenant_id),"` | — |
| [SRC-C9CF9B54F8-L000311](../../agents/omarai.py#L311) | 311 | `"            None,"` | — |
| [SRC-C9CF9B54F8-L000312](../../agents/omarai.py#L312) | 312 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000313](../../agents/omarai.py#L313) | 313 | `""` | — |
| [SRC-C9CF9B54F8-L000314](../../agents/omarai.py#L314) | 314 | `"    def add("` | — |
| [SRC-C9CF9B54F8-L000315](../../agents/omarai.py#L315) | 315 | `"        self,"` | — |
| [SRC-C9CF9B54F8-L000316](../../agents/omarai.py#L316) | 316 | `"        text: str,"` | — |
| [SRC-C9CF9B54F8-L000317](../../agents/omarai.py#L317) | 317 | `"        source_url: str,"` | — |
| [SRC-C9CF9B54F8-L000318](../../agents/omarai.py#L318) | 318 | `"        platform: str = \"manual\","` | — |
| [SRC-C9CF9B54F8-L000319](../../agents/omarai.py#L319) | 319 | `"        observed_at: str \| None = None,"` | — |
| [SRC-C9CF9B54F8-L000320](../../agents/omarai.py#L320) | 320 | `"        note: str = \"\","` | — |
| [SRC-C9CF9B54F8-L000321](../../agents/omarai.py#L321) | 321 | `"        product_terms=(),"` | — |
| [SRC-C9CF9B54F8-L000322](../../agents/omarai.py#L322) | 322 | `"        location_terms=(),"` | — |
| [SRC-C9CF9B54F8-L000323](../../agents/omarai.py#L323) | 323 | `"        *,"` | — |
| [SRC-C9CF9B54F8-L000324](../../agents/omarai.py#L324) | 324 | `"        tenant_id: str = DEFAULT_TENANT_ID,"` | — |
| [SRC-C9CF9B54F8-L000325](../../agents/omarai.py#L325) | 325 | `"    ):"` | — |
| [SRC-C9CF9B54F8-L000326](../../agents/omarai.py#L326) | 326 | `"        tenant_id = self._required_id(tenant_id, \"tenant_id\")"` | — |
| [SRC-C9CF9B54F8-L000327](../../agents/omarai.py#L327) | 327 | `"        if not isinstance(text, str) or not text.strip():"` | — |
| [SRC-C9CF9B54F8-L000328](../../agents/omarai.py#L328) | 328 | `"            raise ValueError(\"text is required\")"` | — |
| [SRC-C9CF9B54F8-L000329](../../agents/omarai.py#L329) | 329 | `"        if len(text) > MAX_TEXT:"` | — |
| [SRC-C9CF9B54F8-L000330](../../agents/omarai.py#L330) | 330 | `"            raise ValueError(\"text is too long\")"` | — |
| [SRC-C9CF9B54F8-L000331](../../agents/omarai.py#L331) | 331 | `"        url = validate_url(source_url)"` | — |
| [SRC-C9CF9B54F8-L000332](../../agents/omarai.py#L332) | 332 | `"        normalized = normalize(text)"` | — |
| [SRC-C9CF9B54F8-L000333](../../agents/omarai.py#L333) | 333 | `"        fingerprint = hashlib.sha256("` | — |
| [SRC-C9CF9B54F8-L000334](../../agents/omarai.py#L334) | 334 | `"            (url.rstrip(\"/\") + \"\\n\" + normalized).encode()"` | — |
| [SRC-C9CF9B54F8-L000335](../../agents/omarai.py#L335) | 335 | `"        ).hexdigest()"` | — |
| [SRC-C9CF9B54F8-L000336](../../agents/omarai.py#L336) | 336 | `"        lead_id = hashlib.sha256("` | — |
| [SRC-C9CF9B54F8-L000337](../../agents/omarai.py#L337) | 337 | `"            (tenant_id + \"\\n\" + fingerprint).encode()"` | — |
| [SRC-C9CF9B54F8-L000338](../../agents/omarai.py#L338) | 338 | `"        ).hexdigest()[:24]"` | — |
| [SRC-C9CF9B54F8-L000339](../../agents/omarai.py#L339) | 339 | `"        timestamp = observed_at or now_utc()"` | — |
| [SRC-C9CF9B54F8-L000340](../../agents/omarai.py#L340) | 340 | `"        assessment = analyze(text, product_terms=product_terms, location_terms=location_terms)"` | — |
| [SRC-C9CF9B54F8-L000341](../../agents/omarai.py#L341) | 341 | `"        now = now_utc()"` | — |
| [SRC-C9CF9B54F8-L000342](../../agents/omarai.py#L342) | 342 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000343](../../agents/omarai.py#L343) | 343 | `"            company = db.execute("` | — |
| [SRC-C9CF9B54F8-L000344](../../agents/omarai.py#L344) | 344 | `"                \"SELECT 1 FROM companies WHERE id=? AND status='active'\", (tenant_id,)"` | — |
| [SRC-C9CF9B54F8-L000345](../../agents/omarai.py#L345) | 345 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000346](../../agents/omarai.py#L346) | 346 | `"            if not company:"` | — |
| [SRC-C9CF9B54F8-L000347](../../agents/omarai.py#L347) | 347 | `"                raise ValueError(\"unknown or inactive company\")"` | — |
| [SRC-C9CF9B54F8-L000348](../../agents/omarai.py#L348) | 348 | `"            cursor = db.execute("` | — |
| [SRC-C9CF9B54F8-L000349](../../agents/omarai.py#L349) | 349 | `"                \"\"\"INSERT OR IGNORE INTO leads"` | — |
| [SRC-C9CF9B54F8-L000350](../../agents/omarai.py#L350) | 350 | `"                   (id, tenant_id, fingerprint, text, source_url, platform, observed_at,"` | — |
| [SRC-C9CF9B54F8-L000351](../../agents/omarai.py#L351) | 351 | `"                    assessment, status, note, created_at, updated_at)"` | — |
| [SRC-C9CF9B54F8-L000352](../../agents/omarai.py#L352) | 352 | `"                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)\"\"\","` | — |
| [SRC-C9CF9B54F8-L000353](../../agents/omarai.py#L353) | 353 | `"                ("` | — |
| [SRC-C9CF9B54F8-L000354](../../agents/omarai.py#L354) | 354 | `"                    lead_id, tenant_id, fingerprint, text.strip(), url, str(platform)[:80],"` | — |
| [SRC-C9CF9B54F8-L000355](../../agents/omarai.py#L355) | 355 | `"                    timestamp, json.dumps(assessment, ensure_ascii=False), \"new\","` | — |
| [SRC-C9CF9B54F8-L000356](../../agents/omarai.py#L356) | 356 | `"                    str(note)[:1000], now, now,"` | — |
| [SRC-C9CF9B54F8-L000357](../../agents/omarai.py#L357) | 357 | `"                ),"` | — |
| [SRC-C9CF9B54F8-L000358](../../agents/omarai.py#L358) | 358 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000359](../../agents/omarai.py#L359) | 359 | `"            row = db.execute("` | — |
| [SRC-C9CF9B54F8-L000360](../../agents/omarai.py#L360) | 360 | `"                \"SELECT * FROM leads WHERE tenant_id=? AND fingerprint=?\","` | — |
| [SRC-C9CF9B54F8-L000361](../../agents/omarai.py#L361) | 361 | `"                (tenant_id, fingerprint),"` | — |
| [SRC-C9CF9B54F8-L000362](../../agents/omarai.py#L362) | 362 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000363](../../agents/omarai.py#L363) | 363 | `"        return self.to_dict(row), cursor.rowcount == 1"` | — |
| [SRC-C9CF9B54F8-L000364](../../agents/omarai.py#L364) | 364 | `""` | — |
| [SRC-C9CF9B54F8-L000365](../../agents/omarai.py#L365) | 365 | `"    @staticmethod"` | — |
| [SRC-C9CF9B54F8-L000366](../../agents/omarai.py#L366) | 366 | `"    def to_dict(row):"` | — |
| [SRC-C9CF9B54F8-L000367](../../agents/omarai.py#L367) | 367 | `"        item = dict(row)"` | — |
| [SRC-C9CF9B54F8-L000368](../../agents/omarai.py#L368) | 368 | `"        item[\"assessment\"] = json.loads(item[\"assessment\"])"` | — |
| [SRC-C9CF9B54F8-L000369](../../agents/omarai.py#L369) | 369 | `"        return item"` | — |
| [SRC-C9CF9B54F8-L000370](../../agents/omarai.py#L370) | 370 | `""` | — |
| [SRC-C9CF9B54F8-L000371](../../agents/omarai.py#L371) | 371 | `"    def list(self, status: str \| None = None, limit: int = 100, *, tenant_id: str = DEFAULT_TENANT_ID):"` | — |
| [SRC-C9CF9B54F8-L000372](../../agents/omarai.py#L372) | 372 | `"        tenant_id = self._required_id(tenant_id, \"tenant_id\")"` | — |
| [SRC-C9CF9B54F8-L000373](../../agents/omarai.py#L373) | 373 | `"        limit = max(1, min(int(limit), 500))"` | — |
| [SRC-C9CF9B54F8-L000374](../../agents/omarai.py#L374) | 374 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000375](../../agents/omarai.py#L375) | 375 | `"            rows = db.execute("` | — |
| [SRC-C9CF9B54F8-L000376](../../agents/omarai.py#L376) | 376 | `"                \"\"\"SELECT * FROM leads"` | — |
| [SRC-C9CF9B54F8-L000377](../../agents/omarai.py#L377) | 377 | `"                   WHERE tenant_id=? AND (? IS NULL OR status=?)"` | — |
| [SRC-C9CF9B54F8-L000378](../../agents/omarai.py#L378) | 378 | `"                   ORDER BY created_at DESC LIMIT ?\"\"\","` | — |
| [SRC-C9CF9B54F8-L000379](../../agents/omarai.py#L379) | 379 | `"                (tenant_id, status, status, limit),"` | — |
| [SRC-C9CF9B54F8-L000380](../../agents/omarai.py#L380) | 380 | `"            ).fetchall()"` | — |
| [SRC-C9CF9B54F8-L000381](../../agents/omarai.py#L381) | 381 | `"        return [self.to_dict(row) for row in rows]"` | — |
| [SRC-C9CF9B54F8-L000382](../../agents/omarai.py#L382) | 382 | `""` | — |
| [SRC-C9CF9B54F8-L000383](../../agents/omarai.py#L383) | 383 | `"    def update_status("` | — |
| [SRC-C9CF9B54F8-L000384](../../agents/omarai.py#L384) | 384 | `"        self, lead_id: str, status: str, *, tenant_id: str = DEFAULT_TENANT_ID"` | — |
| [SRC-C9CF9B54F8-L000385](../../agents/omarai.py#L385) | 385 | `"    ):"` | — |
| [SRC-C9CF9B54F8-L000386](../../agents/omarai.py#L386) | 386 | `"        tenant_id = self._required_id(tenant_id, \"tenant_id\")"` | — |
| [SRC-C9CF9B54F8-L000387](../../agents/omarai.py#L387) | 387 | `"        allowed = {\"new\", \"qualified\", \"contacted\", \"converted\", \"rejected\", \"needs_review\"}"` | — |
| [SRC-C9CF9B54F8-L000388](../../agents/omarai.py#L388) | 388 | `"        if status not in allowed:"` | — |
| [SRC-C9CF9B54F8-L000389](../../agents/omarai.py#L389) | 389 | `"            raise ValueError(\"unsupported status\")"` | — |
| [SRC-C9CF9B54F8-L000390](../../agents/omarai.py#L390) | 390 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000391](../../agents/omarai.py#L391) | 391 | `"            db.execute("` | — |
| [SRC-C9CF9B54F8-L000392](../../agents/omarai.py#L392) | 392 | `"                \"UPDATE leads SET status=?, updated_at=? WHERE id=? AND tenant_id=?\","` | — |
| [SRC-C9CF9B54F8-L000393](../../agents/omarai.py#L393) | 393 | `"                (status, now_utc(), lead_id, tenant_id),"` | — |
| [SRC-C9CF9B54F8-L000394](../../agents/omarai.py#L394) | 394 | `"            )"` | — |
| [SRC-C9CF9B54F8-L000395](../../agents/omarai.py#L395) | 395 | `"            row = db.execute("` | — |
| [SRC-C9CF9B54F8-L000396](../../agents/omarai.py#L396) | 396 | `"                \"SELECT * FROM leads WHERE id=? AND tenant_id=?\", (lead_id, tenant_id)"` | — |
| [SRC-C9CF9B54F8-L000397](../../agents/omarai.py#L397) | 397 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000398](../../agents/omarai.py#L398) | 398 | `"        return self.to_dict(row) if row else None"` | — |
| [SRC-C9CF9B54F8-L000399](../../agents/omarai.py#L399) | 399 | `""` | — |
| [SRC-C9CF9B54F8-L000400](../../agents/omarai.py#L400) | 400 | `"    def import_csv(self, filename: str, *, tenant_id: str = DEFAULT_TENANT_ID):"` | — |
| [SRC-C9CF9B54F8-L000401](../../agents/omarai.py#L401) | 401 | `"        tenant_id = self._required_id(tenant_id, \"tenant_id\")"` | — |
| [SRC-C9CF9B54F8-L000402](../../agents/omarai.py#L402) | 402 | `"        results = {\"created\": 0, \"duplicates\": 0, \"errors\": []}"` | — |
| [SRC-C9CF9B54F8-L000403](../../agents/omarai.py#L403) | 403 | `"        with open(filename, newline=\"\", encoding=\"utf-8-sig\") as stream:"` | — |
| [SRC-C9CF9B54F8-L000404](../../agents/omarai.py#L404) | 404 | `"            reader = csv.DictReader(stream)"` | — |
| [SRC-C9CF9B54F8-L000405](../../agents/omarai.py#L405) | 405 | `"            required = {\"text\", \"source_url\", \"platform\"}"` | — |
| [SRC-C9CF9B54F8-L000406](../../agents/omarai.py#L406) | 406 | `"            if not reader.fieldnames or not required.issubset(reader.fieldnames):"` | — |
| [SRC-C9CF9B54F8-L000407](../../agents/omarai.py#L407) | 407 | `"                raise ValueError(\"CSV must contain text,source_url,platform columns\")"` | — |
| [SRC-C9CF9B54F8-L000408](../../agents/omarai.py#L408) | 408 | `"            for line, row in enumerate(reader, 2):"` | — |
| [SRC-C9CF9B54F8-L000409](../../agents/omarai.py#L409) | 409 | `"                try:"` | — |
| [SRC-C9CF9B54F8-L000410](../../agents/omarai.py#L410) | 410 | `"                    _, created = self.add("` | — |
| [SRC-C9CF9B54F8-L000411](../../agents/omarai.py#L411) | 411 | `"                        row[\"text\"], row[\"source_url\"], row[\"platform\"],"` | — |
| [SRC-C9CF9B54F8-L000412](../../agents/omarai.py#L412) | 412 | `"                        row.get(\"observed_at\") or None, row.get(\"note\") or \"\","` | — |
| [SRC-C9CF9B54F8-L000413](../../agents/omarai.py#L413) | 413 | `"                        tenant_id=tenant_id,"` | — |
| [SRC-C9CF9B54F8-L000414](../../agents/omarai.py#L414) | 414 | `"                    )"` | — |
| [SRC-C9CF9B54F8-L000415](../../agents/omarai.py#L415) | 415 | `"                    results[\"created\" if created else \"duplicates\"] += 1"` | — |
| [SRC-C9CF9B54F8-L000416](../../agents/omarai.py#L416) | 416 | `"                except (ValueError, TypeError) as exc:"` | — |
| [SRC-C9CF9B54F8-L000417](../../agents/omarai.py#L417) | 417 | `"                    results[\"errors\"].append({\"line\": line, \"error\": str(exc)})"` | — |
| [SRC-C9CF9B54F8-L000418](../../agents/omarai.py#L418) | 418 | `"        return results"` | — |
| [SRC-C9CF9B54F8-L000419](../../agents/omarai.py#L419) | 419 | `""` | — |
| [SRC-C9CF9B54F8-L000420](../../agents/omarai.py#L420) | 420 | `"    def _write_csv(self, stream, tenant_id: str) -> int:"` | — |
| [SRC-C9CF9B54F8-L000421](../../agents/omarai.py#L421) | 421 | `"        rows = self.list(limit=500, tenant_id=tenant_id)"` | — |
| [SRC-C9CF9B54F8-L000422](../../agents/omarai.py#L422) | 422 | `"        fields = ["` | — |
| [SRC-C9CF9B54F8-L000423](../../agents/omarai.py#L423) | 423 | `"            \"id\", \"tenant_id\", \"text\", \"source_url\", \"platform\", \"observed_at\","` | — |
| [SRC-C9CF9B54F8-L000424](../../agents/omarai.py#L424) | 424 | `"            \"assessment\", \"status\", \"note\", \"created_at\","` | — |
| [SRC-C9CF9B54F8-L000425](../../agents/omarai.py#L425) | 425 | `"        ]"` | — |
| [SRC-C9CF9B54F8-L000426](../../agents/omarai.py#L426) | 426 | `"        writer = csv.DictWriter(stream, fieldnames=fields, quoting=csv.QUOTE_ALL)"` | — |
| [SRC-C9CF9B54F8-L000427](../../agents/omarai.py#L427) | 427 | `"        writer.writeheader()"` | — |
| [SRC-C9CF9B54F8-L000428](../../agents/omarai.py#L428) | 428 | `"        for row in rows:"` | — |
| [SRC-C9CF9B54F8-L000429](../../agents/omarai.py#L429) | 429 | `"            values = {"` | — |
| [SRC-C9CF9B54F8-L000430](../../agents/omarai.py#L430) | 430 | `"                key: json.dumps(row[key], ensure_ascii=False)"` | — |
| [SRC-C9CF9B54F8-L000431](../../agents/omarai.py#L431) | 431 | `"                if key == \"assessment\""` | — |
| [SRC-C9CF9B54F8-L000432](../../agents/omarai.py#L432) | 432 | `"                else row.get(key, \"\")"` | — |
| [SRC-C9CF9B54F8-L000433](../../agents/omarai.py#L433) | 433 | `"                for key in fields"` | — |
| [SRC-C9CF9B54F8-L000434](../../agents/omarai.py#L434) | 434 | `"            }"` | — |
| [SRC-C9CF9B54F8-L000435](../../agents/omarai.py#L435) | 435 | `"            writer.writerow({key: _csv_safe_cell(value) for key, value in values.items()})"` | — |
| [SRC-C9CF9B54F8-L000436](../../agents/omarai.py#L436) | 436 | `"        return len(rows)"` | — |
| [SRC-C9CF9B54F8-L000437](../../agents/omarai.py#L437) | 437 | `""` | — |
| [SRC-C9CF9B54F8-L000438](../../agents/omarai.py#L438) | 438 | `"    def export_csv(self, filename: str \| Path, *, tenant_id: str = DEFAULT_TENANT_ID):"` | — |
| [SRC-C9CF9B54F8-L000439](../../agents/omarai.py#L439) | 439 | `"        tenant_id = self._required_id(tenant_id, \"tenant_id\")"` | — |
| [SRC-C9CF9B54F8-L000440](../../agents/omarai.py#L440) | 440 | `"        with open(filename, \"w\", newline=\"\", encoding=\"utf-8-sig\") as stream:"` | — |
| [SRC-C9CF9B54F8-L000441](../../agents/omarai.py#L441) | 441 | `"            return self._write_csv(stream, tenant_id)"` | — |
| [SRC-C9CF9B54F8-L000442](../../agents/omarai.py#L442) | 442 | `""` | — |
| [SRC-C9CF9B54F8-L000443](../../agents/omarai.py#L443) | 443 | `"    def export_csv_text(self, *, tenant_id: str = DEFAULT_TENANT_ID) -> str:"` | — |
| [SRC-C9CF9B54F8-L000444](../../agents/omarai.py#L444) | 444 | `"        tenant_id = self._required_id(tenant_id, \"tenant_id\")"` | — |
| [SRC-C9CF9B54F8-L000445](../../agents/omarai.py#L445) | 445 | `"        stream = StringIO(newline=\"\")"` | — |
| [SRC-C9CF9B54F8-L000446](../../agents/omarai.py#L446) | 446 | `"        self._write_csv(stream, tenant_id)"` | — |
| [SRC-C9CF9B54F8-L000447](../../agents/omarai.py#L447) | 447 | `"        return stream.getvalue()"` | — |
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
| [SRC-3D565C3B85-L000127](../../agents/requirement_evidence.py#L127) | 127 | `"            status = \"no_candidate_evidence_found\""` | — |
| [SRC-3D565C3B85-L000128](../../agents/requirement_evidence.py#L128) | 128 | `"        else:"` | — |
| [SRC-3D565C3B85-L000129](../../agents/requirement_evidence.py#L129) | 129 | `"            status = \"query_not_available\""` | — |
| [SRC-3D565C3B85-L000130](../../agents/requirement_evidence.py#L130) | 130 | `""` | — |
| [SRC-3D565C3B85-L000131](../../agents/requirement_evidence.py#L131) | 131 | `"        ledger.append({"` | — |
| [SRC-3D565C3B85-L000132](../../agents/requirement_evidence.py#L132) | 132 | `"            \"target\": target_text,"` | — |
| [SRC-3D565C3B85-L000133](../../agents/requirement_evidence.py#L133) | 133 | `"            \"targeted_query\": targeted_query or None,"` | — |
| [SRC-3D565C3B85-L000134](../../agents/requirement_evidence.py#L134) | 134 | `"            \"targeted_query_status\": ("` | — |
| [SRC-3D565C3B85-L000135](../../agents/requirement_evidence.py#L135) | 135 | `"                \"linked_to_returned_sources\" if query_result_indexes"` | — |
| [SRC-3D565C3B85-L000136](../../agents/requirement_evidence.py#L136) | 136 | `"                else \"no_linked_source_record\""` | — |
| [SRC-3D565C3B85-L000137](../../agents/requirement_evidence.py#L137) | 137 | `"            ),"` | — |
| [SRC-3D565C3B85-L000138](../../agents/requirement_evidence.py#L138) | 138 | `"            \"query_result_source_indexes\": query_result_indexes[:12],"` | — |
| [SRC-3D565C3B85-L000139](../../agents/requirement_evidence.py#L139) | 139 | `"            \"candidate_source_indexes\": ["` | — |
| [SRC-3D565C3B85-L000140](../../agents/requirement_evidence.py#L140) | 140 | `"                item[\"source_index\"] for item in candidate_sources"` | — |
| [SRC-3D565C3B85-L000141](../../agents/requirement_evidence.py#L141) | 141 | `"            ],"` | — |
| [SRC-3D565C3B85-L000142](../../agents/requirement_evidence.py#L142) | 142 | `"            \"candidate_sources\": candidate_sources[:8],"` | — |
| [SRC-3D565C3B85-L000143](../../agents/requirement_evidence.py#L143) | 143 | `"            \"status\": status,"` | — |
| [SRC-3D565C3B85-L000144](../../agents/requirement_evidence.py#L144) | 144 | `"            \"method\": \"targeted_query_provenance_plus_lexical_source_screen\","` | — |
| [SRC-3D565C3B85-L000145](../../agents/requirement_evidence.py#L145) | 145 | `"            \"semantic_verification\": False,"` | — |
| [SRC-3D565C3B85-L000146](../../agents/requirement_evidence.py#L146) | 146 | `"            \"source_entailment_verified\": False,"` | — |
| [SRC-3D565C3B85-L000147](../../agents/requirement_evidence.py#L147) | 147 | `"        })"` | — |
| [SRC-3D565C3B85-L000148](../../agents/requirement_evidence.py#L148) | 148 | `"    return ledger"` | — |
## الوكيل والمنطق

### FILE-59CF4B7DE8 — [agents/research.py](../../agents/research.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-59CF4B7DE8-L000001](../../agents/research.py#L1) | 1 | `"\"\"\"Research planning, domain targeting, and multi-query source ranking."` | — |
| [SRC-59CF4B7DE8-L000002](../../agents/research.py#L2) | 2 | `""` | — |
| [SRC-59CF4B7DE8-L000003](../../agents/research.py#L3) | 3 | `"This module is deterministic by design: the language model may propose a plan,"` | — |
| [SRC-59CF4B7DE8-L000004](../../agents/research.py#L4) | 4 | `"but all queries, result counts and source records are validated before use."` | — |
| [SRC-59CF4B7DE8-L000005](../../agents/research.py#L5) | 5 | `"\"\"\""` | — |
| [SRC-59CF4B7DE8-L000006](../../agents/research.py#L6) | 6 | `"from __future__ import annotations"` | — |
| [SRC-59CF4B7DE8-L000007](../../agents/research.py#L7) | 7 | `""` | — |
| [SRC-59CF4B7DE8-L000008](../../agents/research.py#L8) | 8 | `"import ipaddress"` | — |
| [SRC-59CF4B7DE8-L000009](../../agents/research.py#L9) | 9 | `"import re"` | — |
| [SRC-59CF4B7DE8-L000010](../../agents/research.py#L10) | 10 | `"from datetime import UTC, datetime, timedelta"` | — |
| [SRC-59CF4B7DE8-L000011](../../agents/research.py#L11) | 11 | `"from email.utils import parsedate_to_datetime"` | — |
| [SRC-59CF4B7DE8-L000012](../../agents/research.py#L12) | 12 | `"from typing import Any"` | — |
| [SRC-59CF4B7DE8-L000013](../../agents/research.py#L13) | 13 | `"from urllib.parse import urlparse"` | — |
| [SRC-59CF4B7DE8-L000014](../../agents/research.py#L14) | 14 | `""` | — |
| [SRC-59CF4B7DE8-L000015](../../agents/research.py#L15) | 15 | `"import tldextract"` | — |
| [SRC-59CF4B7DE8-L000016](../../agents/research.py#L16) | 16 | `""` | — |
| [SRC-59CF4B7DE8-L000017](../../agents/research.py#L17) | 17 | `"from agents.aspect_planning import extract_aspects"` | — |
| [SRC-59CF4B7DE8-L000018](../../agents/research.py#L18) | 18 | `"from agents.intent_router import resolve_followup_query"` | — |
| [SRC-59CF4B7DE8-L000019](../../agents/research.py#L19) | 19 | `""` | — |
| [SRC-59CF4B7DE8-L000020](../../agents/research.py#L20) | 20 | `"MAX_PLAN_QUERIES = 8"` | — |
| [SRC-59CF4B7DE8-L000021](../../agents/research.py#L21) | 21 | `"MAX_QUERY_CHARS = 240"` | — |
| [SRC-59CF4B7DE8-L000022](../../agents/research.py#L22) | 22 | `"MAX_FUSED_RESULTS = 18"` | — |
| [SRC-59CF4B7DE8-L000023](../../agents/research.py#L23) | 23 | `""` | — |
| [SRC-59CF4B7DE8-L000024](../../agents/research.py#L24) | 24 | `""` | — |
| [SRC-59CF4B7DE8-L000025](../../agents/research.py#L25) | 25 | `"# Use the Public Suffix List snapshot bundled with tldextract; never fetch it at"` | — |
| [SRC-59CF4B7DE8-L000026](../../agents/research.py#L26) | 26 | `"# runtime. Including private suffixes keeps tenant-hosted sites (e.g. github.io)"` | — |
| [SRC-59CF4B7DE8-L000027](../../agents/research.py#L27) | 27 | `"# separate, while subdomains belonging to one registrable site share one identity."` | — |
| [SRC-59CF4B7DE8-L000028](../../agents/research.py#L28) | 28 | `"_DOMAIN_EXTRACTOR = tldextract.TLDExtract("` | — |
| [SRC-59CF4B7DE8-L000029](../../agents/research.py#L29) | 29 | `"    suffix_list_urls=(),"` | — |
| [SRC-59CF4B7DE8-L000030](../../agents/research.py#L30) | 30 | `"    include_psl_private_domains=True,"` | — |
| [SRC-59CF4B7DE8-L000031](../../agents/research.py#L31) | 31 | `")"` | — |
| [SRC-59CF4B7DE8-L000032](../../agents/research.py#L32) | 32 | `""` | — |
| [SRC-59CF4B7DE8-L000033](../../agents/research.py#L33) | 33 | `""` | — |
| [SRC-59CF4B7DE8-L000034](../../agents/research.py#L34) | 34 | `"def registrable_domain(value: Any) -> str:"` | — |
| [SRC-59CF4B7DE8-L000035](../../agents/research.py#L35) | 35 | `"    \"\"\"Return a normalized registrable domain (or normalized IP/unknown hostname)."` | — |
| [SRC-59CF4B7DE8-L000036](../../agents/research.py#L36) | 36 | `""` | — |
| [SRC-59CF4B7DE8-L000037](../../agents/research.py#L37) | 37 | `"    This is a conservative source-diversity key, not proof that two publishers"` | — |
| [SRC-59CF4B7DE8-L000038](../../agents/research.py#L38) | 38 | `"    are editorially independent. It prevents sibling subdomains from being"` | — |
| [SRC-59CF4B7DE8-L000039](../../agents/research.py#L39) | 39 | `"    counted as separate domains in the evidence coverage threshold."` | — |
| [SRC-59CF4B7DE8-L000040](../../agents/research.py#L40) | 40 | `"    \"\"\""` | — |
| [SRC-59CF4B7DE8-L000041](../../agents/research.py#L41) | 41 | `"    candidate = str(value or \"\").strip()"` | — |
| [SRC-59CF4B7DE8-L000042](../../agents/research.py#L42) | 42 | `"    if not candidate:"` | — |
| [SRC-59CF4B7DE8-L000043](../../agents/research.py#L43) | 43 | `"        return \"\""` | — |
| [SRC-59CF4B7DE8-L000044](../../agents/research.py#L44) | 44 | `"    parsed = urlparse(candidate if \"://\" in candidate else \"//\" + candidate)"` | — |
| [SRC-59CF4B7DE8-L000045](../../agents/research.py#L45) | 45 | `"    host = (parsed.hostname or \"\").rstrip(\".\").lower()"` | — |
| [SRC-59CF4B7DE8-L000046](../../agents/research.py#L46) | 46 | `"    if not host:"` | — |
| [SRC-59CF4B7DE8-L000047](../../agents/research.py#L47) | 47 | `"        return \"\""` | — |
| [SRC-59CF4B7DE8-L000048](../../agents/research.py#L48) | 48 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000049](../../agents/research.py#L49) | 49 | `"        return str(ipaddress.ip_address(host))"` | — |
| [SRC-59CF4B7DE8-L000050](../../agents/research.py#L50) | 50 | `"    except ValueError:"` | — |
| [SRC-59CF4B7DE8-L000051](../../agents/research.py#L51) | 51 | `"        pass"` | — |
| [SRC-59CF4B7DE8-L000052](../../agents/research.py#L52) | 52 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000053](../../agents/research.py#L53) | 53 | `"        host = host.encode(\"idna\").decode(\"ascii\").lower()"` | — |
| [SRC-59CF4B7DE8-L000054](../../agents/research.py#L54) | 54 | `"    except UnicodeError:"` | — |
| [SRC-59CF4B7DE8-L000055](../../agents/research.py#L55) | 55 | `"        return host"` | — |
| [SRC-59CF4B7DE8-L000056](../../agents/research.py#L56) | 56 | `"    extracted = _DOMAIN_EXTRACTOR(host)"` | — |
| [SRC-59CF4B7DE8-L000057](../../agents/research.py#L57) | 57 | `"    return (extracted.top_domain_under_public_suffix or host).lower()"` | — |
| [SRC-59CF4B7DE8-L000058](../../agents/research.py#L58) | 58 | `""` | — |
| [SRC-59CF4B7DE8-L000059](../../agents/research.py#L59) | 59 | `"SOCIAL_DOMAINS = {"` | — |
| [SRC-59CF4B7DE8-L000060](../../agents/research.py#L60) | 60 | `"    \"reddit\": \"reddit.com\","` | — |
| [SRC-59CF4B7DE8-L000061](../../agents/research.py#L61) | 61 | `"    \"youtube\": \"youtube.com\","` | — |
| [SRC-59CF4B7DE8-L000062](../../agents/research.py#L62) | 62 | `"    \"facebook\": \"facebook.com\","` | — |
| [SRC-59CF4B7DE8-L000063](../../agents/research.py#L63) | 63 | `"    \"instagram\": \"instagram.com\","` | — |
| [SRC-59CF4B7DE8-L000064](../../agents/research.py#L64) | 64 | `"    \"x\": \"x.com\","` | — |
| [SRC-59CF4B7DE8-L000065](../../agents/research.py#L65) | 65 | `"    \"twitter\": \"twitter.com\","` | — |
| [SRC-59CF4B7DE8-L000066](../../agents/research.py#L66) | 66 | `"    \"tiktok\": \"tiktok.com\","` | — |
| [SRC-59CF4B7DE8-L000067](../../agents/research.py#L67) | 67 | `"    \"linkedin\": \"linkedin.com\","` | — |
| [SRC-59CF4B7DE8-L000068](../../agents/research.py#L68) | 68 | `"    \"threads\": \"threads.net\","` | — |
| [SRC-59CF4B7DE8-L000069](../../agents/research.py#L69) | 69 | `"    \"bluesky\": \"bsky.app\","` | — |
| [SRC-59CF4B7DE8-L000070](../../agents/research.py#L70) | 70 | `"}"` | — |
| [SRC-59CF4B7DE8-L000071](../../agents/research.py#L71) | 71 | `""` | — |
| [SRC-59CF4B7DE8-L000072](../../agents/research.py#L72) | 72 | `"_SOCIAL_TERMS = ("` | — |
| [SRC-59CF4B7DE8-L000073](../../agents/research.py#L73) | 73 | `"    \"social media\", \"social network\", \"social posts\", \"social pages\", \"public social\", \"public posts\","` | — |
| [SRC-59CF4B7DE8-L000074](../../agents/research.py#L74) | 74 | `"    \"facebook\", \"instagram\", \"reddit\", \"youtube\", \"twitter\", \"x.com\","` | — |
| [SRC-59CF4B7DE8-L000075](../../agents/research.py#L75) | 75 | `"    \"tiktok\", \"linkedin\", \"threads\", \"bluesky\","` | — |
| [SRC-59CF4B7DE8-L000076](../../agents/research.py#L76) | 76 | `"    \"سوشيال\", \"التواصل الاجتماعي\", \"مواقع التواصل\", \"صفحات التواصل\","` | — |
| [SRC-59CF4B7DE8-L000077](../../agents/research.py#L77) | 77 | `"    \"منشورات\", \"تعليقات الناس\", \"آراء الناس\", \"تجارب المستخدمين\","` | — |
| [SRC-59CF4B7DE8-L000078](../../agents/research.py#L78) | 78 | `"    \"تجارب العملاء\", \"اراء العملاء\", \"آراء العملاء\", \"رأي الناس\","` | — |
| [SRC-59CF4B7DE8-L000079](../../agents/research.py#L79) | 79 | `"    \"كلام الناس\", \"الناس بتقول\", \"مراجعات العملاء\", \"تعليقات العملاء\","` | — |
| [SRC-59CF4B7DE8-L000080](../../agents/research.py#L80) | 80 | `"    \"بوستات\", \"فيدوهات\", \"فيديوهات\", \"ريلز\", \"تويتر\", \"فيسبوك\","` | — |
| [SRC-59CF4B7DE8-L000081](../../agents/research.py#L81) | 81 | `"    \"انستجرام\", \"إنستجرام\", \"تيك توك\", \"لينكدان\", \"لينكدإن\","` | — |
| [SRC-59CF4B7DE8-L000082](../../agents/research.py#L82) | 82 | `"    \"مصادر العملاء\", \"عملاء محتملين\", \"العملاء المحتملين\","` | — |
| [SRC-59CF4B7DE8-L000083](../../agents/research.py#L83) | 83 | `")"` | — |
| [SRC-59CF4B7DE8-L000084](../../agents/research.py#L84) | 84 | `""` | — |
| [SRC-59CF4B7DE8-L000085](../../agents/research.py#L85) | 85 | `"_FRESH_TERMS = ("` | — |
| [SRC-59CF4B7DE8-L000086](../../agents/research.py#L86) | 86 | `"    \"latest\", \"current\", \"today\", \"this week\", \"recent\", \"breaking\", \"news\","` | — |
| [SRC-59CF4B7DE8-L000087](../../agents/research.py#L87) | 87 | `"    \"now\", \"2026\", \"latest price\", \"market price\", \"updated\","` | — |
| [SRC-59CF4B7DE8-L000088](../../agents/research.py#L88) | 88 | `"    \"آخر\", \"اخر\", \"احدث\", \"أحدث\", \"حاليا\", \"حالياً\", \"الآن\", \"دلوقتي\", \"النهارده\", \"مؤخرًا\", \"مؤخرا\", \"اليوم\", \"هذا الاسبوع\","` | — |
| [SRC-59CF4B7DE8-L000089](../../agents/research.py#L89) | 89 | `"    \"هذا الأسبوع\", \"آخر الأخبار\", \"اخر الاخبار\", \"مستجدات\", \"حديث\","` | — |
| [SRC-59CF4B7DE8-L000090](../../agents/research.py#L90) | 90 | `"    \"سعر اليوم\", \"الاسعار الحالية\", \"الأسعار الحالية\", \"جديد\","` | — |
| [SRC-59CF4B7DE8-L000091](../../agents/research.py#L91) | 91 | `")"` | — |
| [SRC-59CF4B7DE8-L000092](../../agents/research.py#L92) | 92 | `""` | — |
| [SRC-59CF4B7DE8-L000093](../../agents/research.py#L93) | 93 | `"_DEEP_TERMS = ("` | — |
| [SRC-59CF4B7DE8-L000094](../../agents/research.py#L94) | 94 | `"    \"deep research\", \"in-depth\", \"comprehensive\", \"exhaustive\", \"compare\","` | — |
| [SRC-59CF4B7DE8-L000095](../../agents/research.py#L95) | 95 | `"    \"comparison\", \"pros and cons\", \"investigate\", \"evidence\", \"sources\","` | — |
| [SRC-59CF4B7DE8-L000096](../../agents/research.py#L96) | 96 | `"    \"بحث عميق\", \"بحث معمق\", \"بحث مكثف\", \"بحث شامل\", \"بالتفصيل\", \"قارن\","` | — |
| [SRC-59CF4B7DE8-L000097](../../agents/research.py#L97) | 97 | `"    \"مقارنة\", \"استقصاء\", \"تحقق\", \"تأكد\", \"مصادر\", \"أدلة\", \"ادلة\","` | — |
| [SRC-59CF4B7DE8-L000098](../../agents/research.py#L98) | 98 | `"    \"كل الجوانب\", \"بحث واسع\", \"متكامل\","` | — |
| [SRC-59CF4B7DE8-L000099](../../agents/research.py#L99) | 99 | `")"` | — |
| [SRC-59CF4B7DE8-L000100](../../agents/research.py#L100) | 100 | `""` | — |
| [SRC-59CF4B7DE8-L000101](../../agents/research.py#L101) | 101 | `""` | — |
| [SRC-59CF4B7DE8-L000102](../../agents/research.py#L102) | 102 | `"def extract_urls(text: str) -> list[str]:"` | — |
| [SRC-59CF4B7DE8-L000103](../../agents/research.py#L103) | 103 | `"    \"\"\"Extract explicit HTTP(S) URLs without trying to interpret their content as instructions.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000104](../../agents/research.py#L104) | 104 | `"    candidates = re.findall(r\"https?://[^\\s<>()]+\", text or \"\", flags=re.IGNORECASE)"` | — |
| [SRC-59CF4B7DE8-L000105](../../agents/research.py#L105) | 105 | `"    cleaned: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000106](../../agents/research.py#L106) | 106 | `"    for value in candidates:"` | — |
| [SRC-59CF4B7DE8-L000107](../../agents/research.py#L107) | 107 | `"        url = value.rstrip(\".,;!?،؛:)\\\"'»\")"` | — |
| [SRC-59CF4B7DE8-L000108](../../agents/research.py#L108) | 108 | `"        if url and url not in cleaned:"` | — |
| [SRC-59CF4B7DE8-L000109](../../agents/research.py#L109) | 109 | `"            cleaned.append(url[:2048])"` | — |
| [SRC-59CF4B7DE8-L000110](../../agents/research.py#L110) | 110 | `"        if len(cleaned) >= 5:"` | — |
| [SRC-59CF4B7DE8-L000111](../../agents/research.py#L111) | 111 | `"            break"` | — |
| [SRC-59CF4B7DE8-L000112](../../agents/research.py#L112) | 112 | `"    return cleaned"` | — |
| [SRC-59CF4B7DE8-L000113](../../agents/research.py#L113) | 113 | `""` | — |
| [SRC-59CF4B7DE8-L000114](../../agents/research.py#L114) | 114 | `""` | — |
| [SRC-59CF4B7DE8-L000115](../../agents/research.py#L115) | 115 | `"def _compact(value: Any, limit: int = MAX_QUERY_CHARS) -> str:"` | — |
| [SRC-59CF4B7DE8-L000116](../../agents/research.py#L116) | 116 | `"    if not isinstance(value, str):"` | — |
| [SRC-59CF4B7DE8-L000117](../../agents/research.py#L117) | 117 | `"        return \"\""` | — |
| [SRC-59CF4B7DE8-L000118](../../agents/research.py#L118) | 118 | `"    return re.sub(r\"\\s+\", \" \", value).strip()[:limit]"` | — |
| [SRC-59CF4B7DE8-L000119](../../agents/research.py#L119) | 119 | `""` | — |
