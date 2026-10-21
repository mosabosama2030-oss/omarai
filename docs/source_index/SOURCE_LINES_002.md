# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **002**
- سجلات الأسطر: **800**
- النطاق: SRC-C9CF9B54F8-L000035 إلى SRC-59CF4B7DE8-L000532
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-C9CF9B54F8 — [agents/omarai.py](../../agents/omarai.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-C9CF9B54F8-L000035](../../agents/omarai.py#L35) | 35 | `"    if not text:"` | — |
| [SRC-C9CF9B54F8-L000036](../../agents/omarai.py#L36) | 36 | `"        return text"` | — |
| [SRC-C9CF9B54F8-L000037](../../agents/omarai.py#L37) | 37 | `"    index = 0"` | — |
| [SRC-C9CF9B54F8-L000038](../../agents/omarai.py#L38) | 38 | `"    while index < len(text) and ("` | — |
| [SRC-C9CF9B54F8-L000039](../../agents/omarai.py#L39) | 39 | `"        text[index].isspace()"` | — |
| [SRC-C9CF9B54F8-L000040](../../agents/omarai.py#L40) | 40 | `"        or unicodedata.category(text[index]) in {\"Cc\", \"Cf\"}"` | — |
| [SRC-C9CF9B54F8-L000041](../../agents/omarai.py#L41) | 41 | `"    ):"` | — |
| [SRC-C9CF9B54F8-L000042](../../agents/omarai.py#L42) | 42 | `"        index += 1"` | — |
| [SRC-C9CF9B54F8-L000043](../../agents/omarai.py#L43) | 43 | `"    first_non_format = text[index:index + 1]"` | — |
| [SRC-C9CF9B54F8-L000044](../../agents/omarai.py#L44) | 44 | `"    formula_prefixes = {\"=\", \"+\", \"-\", \"@\", \"＝\", \"＋\", \"－\", \"＠\"}"` | — |
| [SRC-C9CF9B54F8-L000045](../../agents/omarai.py#L45) | 45 | `"    if text[0] in \"\\t\\r\\n\" or first_non_format in formula_prefixes:"` | — |
| [SRC-C9CF9B54F8-L000046](../../agents/omarai.py#L46) | 46 | `"        # OWASP notes that a tab inside the quoted CSV field is more resilient"` | — |
| [SRC-C9CF9B54F8-L000047](../../agents/omarai.py#L47) | 47 | `"        # in Excel than an apostrophe, although no CSV mitigation is universal."` | — |
| [SRC-C9CF9B54F8-L000048](../../agents/omarai.py#L48) | 48 | `"        return \"\\t\" + text"` | — |
| [SRC-C9CF9B54F8-L000049](../../agents/omarai.py#L49) | 49 | `"    return text"` | — |
| [SRC-C9CF9B54F8-L000050](../../agents/omarai.py#L50) | 50 | `""` | — |
| [SRC-C9CF9B54F8-L000051](../../agents/omarai.py#L51) | 51 | `"def analyze(text: str, product_terms=(), location_terms=()) -> dict:"` | — |
| [SRC-C9CF9B54F8-L000052](../../agents/omarai.py#L52) | 52 | `"    if not isinstance(text, str) or not text.strip():"` | — |
| [SRC-C9CF9B54F8-L000053](../../agents/omarai.py#L53) | 53 | `"        raise ValueError(\"text must not be empty\")"` | — |
| [SRC-C9CF9B54F8-L000054](../../agents/omarai.py#L54) | 54 | `"    if len(text) > MAX_TEXT:"` | — |
| [SRC-C9CF9B54F8-L000055](../../agents/omarai.py#L55) | 55 | `"        raise ValueError(f\"text must be at most {MAX_TEXT} characters\")"` | — |
| [SRC-C9CF9B54F8-L000056](../../agents/omarai.py#L56) | 56 | `"    body = normalize(text)"` | — |
| [SRC-C9CF9B54F8-L000057](../../agents/omarai.py#L57) | 57 | `"    excluded = [p for p in NOT_BUYER if normalize(p) in body]"` | — |
| [SRC-C9CF9B54F8-L000058](../../agents/omarai.py#L58) | 58 | `"    if excluded:"` | — |
| [SRC-C9CF9B54F8-L000059](../../agents/omarai.py#L59) | 59 | `"        return {\"score\": 0, \"label\": \"not_buyer_signal\", \"summary\": \"قد لا تكون إشارة شراء مباشرة؛ راجع النص يدويًا.\", \"matched_signals\": [{\"phrase\": p, \"category\": \"exclusion\", \"points\": 0} for p in excluded], \"warnings\": [\"تصنيف أولي وليس حكمًا نهائيًا.\"]}"` | — |
| [SRC-C9CF9B54F8-L000060](../../agents/omarai.py#L60) | 60 | `"    matches = []"` | — |
| [SRC-C9CF9B54F8-L000061](../../agents/omarai.py#L61) | 61 | `"    for category, (points, phrases) in SIGNALS.items():"` | — |
| [SRC-C9CF9B54F8-L000062](../../agents/omarai.py#L62) | 62 | `"        found = next((p for p in phrases if normalize(p) in body), None)"` | — |
| [SRC-C9CF9B54F8-L000063](../../agents/omarai.py#L63) | 63 | `"        if found:"` | — |
| [SRC-C9CF9B54F8-L000064](../../agents/omarai.py#L64) | 64 | `"            matches.append({\"phrase\": found, \"category\": category, \"points\": points})"` | — |
| [SRC-C9CF9B54F8-L000065](../../agents/omarai.py#L65) | 65 | `"    for category, terms in ((\"product_context\", product_terms), (\"location_context\", location_terms)):"` | — |
| [SRC-C9CF9B54F8-L000066](../../agents/omarai.py#L66) | 66 | `"        found = next((normalize(t) for t in terms if isinstance(t, str) and normalize(t) and normalize(t) in body), None)"` | — |
| [SRC-C9CF9B54F8-L000067](../../agents/omarai.py#L67) | 67 | `"        if found:"` | — |
| [SRC-C9CF9B54F8-L000068](../../agents/omarai.py#L68) | 68 | `"            matches.append({\"phrase\": found, \"category\": category, \"points\": 10})"` | — |
| [SRC-C9CF9B54F8-L000069](../../agents/omarai.py#L69) | 69 | `"    score = min(100, sum(x[\"points\"] for x in matches))"` | — |
| [SRC-C9CF9B54F8-L000070](../../agents/omarai.py#L70) | 70 | `"    label = \"high_intent\" if score >= 55 and any(x[\"category\"] == \"high\" for x in matches) else \"medium_intent\" if score >= 40 else \"early_research\" if score >= 20 else \"unclear\""` | — |
| [SRC-C9CF9B54F8-L000071](../../agents/omarai.py#L71) | 71 | `"    return {\"score\": score, \"label\": label, \"summary\": {\"high_intent\":\"إشارة قوية نسبيًا وفق قواعد بسيطة وتحتاج مراجعة بشرية.\",\"medium_intent\":\"مؤشرات اهتمام تستحق التأهيل والتحقق.\",\"early_research\":\"اهتمام مبكر؛ ليس عميلًا مؤهلًا بعد.\",\"unclear\":\"لا توجد مؤشرات كافية.\"}[label], \"matched_signals\": matches, \"warnings\": [\"الدرجة ليست احتمالًا إحصائيًا للشراء.\", \"لا تثبت هوية الكاتب أو قدرته على الدفع أو نيته.\", \"استخدم مصادر عامة ومسموحًا بمعالجتها فقط.\"]}"` | — |
| [SRC-C9CF9B54F8-L000072](../../agents/omarai.py#L72) | 72 | `""` | — |
| [SRC-C9CF9B54F8-L000073](../../agents/omarai.py#L73) | 73 | `"def validate_url(url: str) -> str:"` | — |
| [SRC-C9CF9B54F8-L000074](../../agents/omarai.py#L74) | 74 | `"    parsed = urlparse(str(url or \"\").strip())"` | — |
| [SRC-C9CF9B54F8-L000075](../../agents/omarai.py#L75) | 75 | `"    if parsed.scheme not in (\"http\", \"https\") or not parsed.netloc or parsed.username or parsed.password:"` | — |
| [SRC-C9CF9B54F8-L000076](../../agents/omarai.py#L76) | 76 | `"        raise ValueError(\"source_url must be an absolute http(s) URL without embedded credentials\")"` | — |
| [SRC-C9CF9B54F8-L000077](../../agents/omarai.py#L77) | 77 | `"    if len(url) > 2048:"` | — |
| [SRC-C9CF9B54F8-L000078](../../agents/omarai.py#L78) | 78 | `"        raise ValueError(\"source_url is too long\")"` | — |
| [SRC-C9CF9B54F8-L000079](../../agents/omarai.py#L79) | 79 | `"    return url.strip()"` | — |
| [SRC-C9CF9B54F8-L000080](../../agents/omarai.py#L80) | 80 | `""` | — |
| [SRC-C9CF9B54F8-L000081](../../agents/omarai.py#L81) | 81 | `"class LeadStore:"` | — |
| [SRC-C9CF9B54F8-L000082](../../agents/omarai.py#L82) | 82 | `"    def __init__(self, path: str \| Path \| None = None):"` | — |
| [SRC-C9CF9B54F8-L000083](../../agents/omarai.py#L83) | 83 | `"        self.path = Path(path or Path.home()/\".omarai\"/\"omarai.sqlite3\").expanduser()"` | — |
| [SRC-C9CF9B54F8-L000084](../../agents/omarai.py#L84) | 84 | `"        self.path.parent.mkdir(parents=True, exist_ok=True)"` | — |
| [SRC-C9CF9B54F8-L000085](../../agents/omarai.py#L85) | 85 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000086](../../agents/omarai.py#L86) | 86 | `"            db.execute(\"\"\"CREATE TABLE IF NOT EXISTS leads ("` | — |
| [SRC-C9CF9B54F8-L000087](../../agents/omarai.py#L87) | 87 | `"            id TEXT PRIMARY KEY, fingerprint TEXT UNIQUE NOT NULL, text TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000088](../../agents/omarai.py#L88) | 88 | `"            source_url TEXT NOT NULL, platform TEXT NOT NULL, observed_at TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000089](../../agents/omarai.py#L89) | 89 | `"            assessment TEXT NOT NULL, status TEXT NOT NULL, note TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000090](../../agents/omarai.py#L90) | 90 | `"            created_at TEXT NOT NULL, updated_at TEXT NOT NULL)\"\"\")"` | — |
| [SRC-C9CF9B54F8-L000091](../../agents/omarai.py#L91) | 91 | `"            db.execute(\"CREATE INDEX IF NOT EXISTS leads_status_idx ON leads(status, created_at DESC)\")"` | — |
| [SRC-C9CF9B54F8-L000092](../../agents/omarai.py#L92) | 92 | `"    def connect(self):"` | — |
| [SRC-C9CF9B54F8-L000093](../../agents/omarai.py#L93) | 93 | `"        db = sqlite3.connect(self.path, timeout=10)"` | — |
| [SRC-C9CF9B54F8-L000094](../../agents/omarai.py#L94) | 94 | `"        db.row_factory = sqlite3.Row"` | — |
| [SRC-C9CF9B54F8-L000095](../../agents/omarai.py#L95) | 95 | `"        return db"` | — |
| [SRC-C9CF9B54F8-L000096](../../agents/omarai.py#L96) | 96 | `"    def add(self, text: str, source_url: str, platform: str=\"manual\", observed_at: str \| None=None, note: str=\"\", product_terms=(), location_terms=()):"` | — |
| [SRC-C9CF9B54F8-L000097](../../agents/omarai.py#L97) | 97 | `"        if not isinstance(text, str) or not text.strip():"` | — |
| [SRC-C9CF9B54F8-L000098](../../agents/omarai.py#L98) | 98 | `"            raise ValueError(\"text is required\")"` | — |
| [SRC-C9CF9B54F8-L000099](../../agents/omarai.py#L99) | 99 | `"        if len(text) > MAX_TEXT:"` | — |
| [SRC-C9CF9B54F8-L000100](../../agents/omarai.py#L100) | 100 | `"            raise ValueError(\"text is too long\")"` | — |
| [SRC-C9CF9B54F8-L000101](../../agents/omarai.py#L101) | 101 | `"        url = validate_url(source_url)"` | — |
| [SRC-C9CF9B54F8-L000102](../../agents/omarai.py#L102) | 102 | `"        normalized = normalize(text)"` | — |
| [SRC-C9CF9B54F8-L000103](../../agents/omarai.py#L103) | 103 | `"        fingerprint = hashlib.sha256((url.rstrip(\"/\") + \"\\n\" + normalized).encode()).hexdigest()"` | — |
| [SRC-C9CF9B54F8-L000104](../../agents/omarai.py#L104) | 104 | `"        lead_id = fingerprint[:24]"` | — |
| [SRC-C9CF9B54F8-L000105](../../agents/omarai.py#L105) | 105 | `"        timestamp = observed_at or now_utc()"` | — |
| [SRC-C9CF9B54F8-L000106](../../agents/omarai.py#L106) | 106 | `"        assessment = analyze(text, product_terms=product_terms, location_terms=location_terms)"` | — |
| [SRC-C9CF9B54F8-L000107](../../agents/omarai.py#L107) | 107 | `"        now = now_utc()"` | — |
| [SRC-C9CF9B54F8-L000108](../../agents/omarai.py#L108) | 108 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000109](../../agents/omarai.py#L109) | 109 | `"            cursor = db.execute(\"\"\"INSERT OR IGNORE INTO leads"` | — |
| [SRC-C9CF9B54F8-L000110](../../agents/omarai.py#L110) | 110 | `"            (id,fingerprint,text,source_url,platform,observed_at,assessment,status,note,created_at,updated_at)"` | — |
| [SRC-C9CF9B54F8-L000111](../../agents/omarai.py#L111) | 111 | `"            VALUES(?,?,?,?,?,?,?,?,?,?,?)\"\"\", (lead_id,fingerprint,text.strip(),url,str(platform)[:80],timestamp,json.dumps(assessment,ensure_ascii=False),\"new\",str(note)[:1000],now,now))"` | — |
| [SRC-C9CF9B54F8-L000112](../../agents/omarai.py#L112) | 112 | `"            row = db.execute(\"SELECT * FROM leads WHERE id=?\", (lead_id,)).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000113](../../agents/omarai.py#L113) | 113 | `"        return self.to_dict(row), cursor.rowcount == 1"` | — |
| [SRC-C9CF9B54F8-L000114](../../agents/omarai.py#L114) | 114 | `"    @staticmethod"` | — |
| [SRC-C9CF9B54F8-L000115](../../agents/omarai.py#L115) | 115 | `"    def to_dict(row):"` | — |
| [SRC-C9CF9B54F8-L000116](../../agents/omarai.py#L116) | 116 | `"        item = dict(row)"` | — |
| [SRC-C9CF9B54F8-L000117](../../agents/omarai.py#L117) | 117 | `"        item[\"assessment\"] = json.loads(item[\"assessment\"])"` | — |
| [SRC-C9CF9B54F8-L000118](../../agents/omarai.py#L118) | 118 | `"        return item"` | — |
| [SRC-C9CF9B54F8-L000119](../../agents/omarai.py#L119) | 119 | `"    def list(self, status: str \| None=None, limit: int=100):"` | — |
| [SRC-C9CF9B54F8-L000120](../../agents/omarai.py#L120) | 120 | `"        limit = max(1,min(int(limit),500))"` | — |
| [SRC-C9CF9B54F8-L000121](../../agents/omarai.py#L121) | 121 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000122](../../agents/omarai.py#L122) | 122 | `"            rows = db.execute(\"SELECT * FROM leads WHERE (? IS NULL OR status=?) ORDER BY created_at DESC LIMIT ?\",(status,status,limit)).fetchall()"` | — |
| [SRC-C9CF9B54F8-L000123](../../agents/omarai.py#L123) | 123 | `"        return [self.to_dict(r) for r in rows]"` | — |
| [SRC-C9CF9B54F8-L000124](../../agents/omarai.py#L124) | 124 | `"    def update_status(self, lead_id: str, status: str):"` | — |
| [SRC-C9CF9B54F8-L000125](../../agents/omarai.py#L125) | 125 | `"        allowed={\"new\",\"qualified\",\"contacted\",\"converted\",\"rejected\",\"needs_review\"}"` | — |
| [SRC-C9CF9B54F8-L000126](../../agents/omarai.py#L126) | 126 | `"        if status not in allowed:"` | — |
| [SRC-C9CF9B54F8-L000127](../../agents/omarai.py#L127) | 127 | `"            raise ValueError(\"unsupported status\")"` | — |
| [SRC-C9CF9B54F8-L000128](../../agents/omarai.py#L128) | 128 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000129](../../agents/omarai.py#L129) | 129 | `"            db.execute(\"UPDATE leads SET status=?,updated_at=? WHERE id=?\",(status,now_utc(),lead_id))"` | — |
| [SRC-C9CF9B54F8-L000130](../../agents/omarai.py#L130) | 130 | `"            row=db.execute(\"SELECT * FROM leads WHERE id=?\",(lead_id,)).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000131](../../agents/omarai.py#L131) | 131 | `"        return self.to_dict(row) if row else None"` | — |
| [SRC-C9CF9B54F8-L000132](../../agents/omarai.py#L132) | 132 | `"    def import_csv(self, filename: str):"` | — |
| [SRC-C9CF9B54F8-L000133](../../agents/omarai.py#L133) | 133 | `"        results={\"created\":0,\"duplicates\":0,\"errors\":[]}"` | — |
| [SRC-C9CF9B54F8-L000134](../../agents/omarai.py#L134) | 134 | `"        with open(filename, newline=\"\", encoding=\"utf-8-sig\") as stream:"` | — |
| [SRC-C9CF9B54F8-L000135](../../agents/omarai.py#L135) | 135 | `"            reader=csv.DictReader(stream)"` | — |
| [SRC-C9CF9B54F8-L000136](../../agents/omarai.py#L136) | 136 | `"            required={\"text\",\"source_url\",\"platform\"}"` | — |
| [SRC-C9CF9B54F8-L000137](../../agents/omarai.py#L137) | 137 | `"            if not reader.fieldnames or not required.issubset(reader.fieldnames):"` | — |
| [SRC-C9CF9B54F8-L000138](../../agents/omarai.py#L138) | 138 | `"                raise ValueError(\"CSV must contain text,source_url,platform columns\")"` | — |
| [SRC-C9CF9B54F8-L000139](../../agents/omarai.py#L139) | 139 | `"            for line,row in enumerate(reader,2):"` | — |
| [SRC-C9CF9B54F8-L000140](../../agents/omarai.py#L140) | 140 | `"                try:"` | — |
| [SRC-C9CF9B54F8-L000141](../../agents/omarai.py#L141) | 141 | `"                    _,created=self.add(row[\"text\"],row[\"source_url\"],row[\"platform\"],row.get(\"observed_at\") or None,row.get(\"note\") or \"\")"` | — |
| [SRC-C9CF9B54F8-L000142](../../agents/omarai.py#L142) | 142 | `"                    results[\"created\" if created else \"duplicates\"] += 1"` | — |
| [SRC-C9CF9B54F8-L000143](../../agents/omarai.py#L143) | 143 | `"                except (ValueError, TypeError) as exc:"` | — |
| [SRC-C9CF9B54F8-L000144](../../agents/omarai.py#L144) | 144 | `"                    results[\"errors\"].append({\"line\":line,\"error\":str(exc)})"` | — |
| [SRC-C9CF9B54F8-L000145](../../agents/omarai.py#L145) | 145 | `"        return results"` | — |
| [SRC-C9CF9B54F8-L000146](../../agents/omarai.py#L146) | 146 | `"    def export_csv(self, filename: str):"` | — |
| [SRC-C9CF9B54F8-L000147](../../agents/omarai.py#L147) | 147 | `"        rows=self.list(limit=500)"` | — |
| [SRC-C9CF9B54F8-L000148](../../agents/omarai.py#L148) | 148 | `"        with open(filename,\"w\",newline=\"\",encoding=\"utf-8-sig\") as stream:"` | — |
| [SRC-C9CF9B54F8-L000149](../../agents/omarai.py#L149) | 149 | `"            fields=[\"id\",\"text\",\"source_url\",\"platform\",\"observed_at\",\"assessment\",\"status\",\"note\",\"created_at\"]"` | — |
| [SRC-C9CF9B54F8-L000150](../../agents/omarai.py#L150) | 150 | `"            writer=csv.DictWriter(stream, fieldnames=fields, quoting=csv.QUOTE_ALL)"` | — |
| [SRC-C9CF9B54F8-L000151](../../agents/omarai.py#L151) | 151 | `"            writer.writeheader()"` | — |
| [SRC-C9CF9B54F8-L000152](../../agents/omarai.py#L152) | 152 | `"            for row in rows:"` | — |
| [SRC-C9CF9B54F8-L000153](../../agents/omarai.py#L153) | 153 | `"                values = {"` | — |
| [SRC-C9CF9B54F8-L000154](../../agents/omarai.py#L154) | 154 | `"                    key: json.dumps(row[key], ensure_ascii=False)"` | — |
| [SRC-C9CF9B54F8-L000155](../../agents/omarai.py#L155) | 155 | `"                    if key == \"assessment\""` | — |
| [SRC-C9CF9B54F8-L000156](../../agents/omarai.py#L156) | 156 | `"                    else row.get(key, \"\")"` | — |
| [SRC-C9CF9B54F8-L000157](../../agents/omarai.py#L157) | 157 | `"                    for key in fields"` | — |
| [SRC-C9CF9B54F8-L000158](../../agents/omarai.py#L158) | 158 | `"                }"` | — |
| [SRC-C9CF9B54F8-L000159](../../agents/omarai.py#L159) | 159 | `"                writer.writerow({key: _csv_safe_cell(value) for key, value in values.items()})"` | — |
| [SRC-C9CF9B54F8-L000160](../../agents/omarai.py#L160) | 160 | `"        return len(rows)"` | — |
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
| [SRC-59CF4B7DE8-L000017](../../agents/research.py#L17) | 17 | `"from agents.intent_router import resolve_followup_query"` | — |
| [SRC-59CF4B7DE8-L000018](../../agents/research.py#L18) | 18 | `""` | — |
| [SRC-59CF4B7DE8-L000019](../../agents/research.py#L19) | 19 | `"MAX_PLAN_QUERIES = 8"` | — |
| [SRC-59CF4B7DE8-L000020](../../agents/research.py#L20) | 20 | `"MAX_QUERY_CHARS = 240"` | — |
| [SRC-59CF4B7DE8-L000021](../../agents/research.py#L21) | 21 | `"MAX_FUSED_RESULTS = 18"` | — |
| [SRC-59CF4B7DE8-L000022](../../agents/research.py#L22) | 22 | `""` | — |
| [SRC-59CF4B7DE8-L000023](../../agents/research.py#L23) | 23 | `""` | — |
| [SRC-59CF4B7DE8-L000024](../../agents/research.py#L24) | 24 | `"# Use the Public Suffix List snapshot bundled with tldextract; never fetch it at"` | — |
| [SRC-59CF4B7DE8-L000025](../../agents/research.py#L25) | 25 | `"# runtime. Including private suffixes keeps tenant-hosted sites (e.g. github.io)"` | — |
| [SRC-59CF4B7DE8-L000026](../../agents/research.py#L26) | 26 | `"# separate, while subdomains belonging to one registrable site share one identity."` | — |
| [SRC-59CF4B7DE8-L000027](../../agents/research.py#L27) | 27 | `"_DOMAIN_EXTRACTOR = tldextract.TLDExtract("` | — |
| [SRC-59CF4B7DE8-L000028](../../agents/research.py#L28) | 28 | `"    suffix_list_urls=(),"` | — |
| [SRC-59CF4B7DE8-L000029](../../agents/research.py#L29) | 29 | `"    include_psl_private_domains=True,"` | — |
| [SRC-59CF4B7DE8-L000030](../../agents/research.py#L30) | 30 | `")"` | — |
| [SRC-59CF4B7DE8-L000031](../../agents/research.py#L31) | 31 | `""` | — |
| [SRC-59CF4B7DE8-L000032](../../agents/research.py#L32) | 32 | `""` | — |
| [SRC-59CF4B7DE8-L000033](../../agents/research.py#L33) | 33 | `"def registrable_domain(value: Any) -> str:"` | — |
| [SRC-59CF4B7DE8-L000034](../../agents/research.py#L34) | 34 | `"    \"\"\"Return a normalized registrable domain (or normalized IP/unknown hostname)."` | — |
| [SRC-59CF4B7DE8-L000035](../../agents/research.py#L35) | 35 | `""` | — |
| [SRC-59CF4B7DE8-L000036](../../agents/research.py#L36) | 36 | `"    This is a conservative source-diversity key, not proof that two publishers"` | — |
| [SRC-59CF4B7DE8-L000037](../../agents/research.py#L37) | 37 | `"    are editorially independent. It prevents sibling subdomains from being"` | — |
| [SRC-59CF4B7DE8-L000038](../../agents/research.py#L38) | 38 | `"    counted as separate domains in the evidence coverage threshold."` | — |
| [SRC-59CF4B7DE8-L000039](../../agents/research.py#L39) | 39 | `"    \"\"\""` | — |
| [SRC-59CF4B7DE8-L000040](../../agents/research.py#L40) | 40 | `"    candidate = str(value or \"\").strip()"` | — |
| [SRC-59CF4B7DE8-L000041](../../agents/research.py#L41) | 41 | `"    if not candidate:"` | — |
| [SRC-59CF4B7DE8-L000042](../../agents/research.py#L42) | 42 | `"        return \"\""` | — |
| [SRC-59CF4B7DE8-L000043](../../agents/research.py#L43) | 43 | `"    parsed = urlparse(candidate if \"://\" in candidate else \"//\" + candidate)"` | — |
| [SRC-59CF4B7DE8-L000044](../../agents/research.py#L44) | 44 | `"    host = (parsed.hostname or \"\").rstrip(\".\").lower()"` | — |
| [SRC-59CF4B7DE8-L000045](../../agents/research.py#L45) | 45 | `"    if not host:"` | — |
| [SRC-59CF4B7DE8-L000046](../../agents/research.py#L46) | 46 | `"        return \"\""` | — |
| [SRC-59CF4B7DE8-L000047](../../agents/research.py#L47) | 47 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000048](../../agents/research.py#L48) | 48 | `"        return str(ipaddress.ip_address(host))"` | — |
| [SRC-59CF4B7DE8-L000049](../../agents/research.py#L49) | 49 | `"    except ValueError:"` | — |
| [SRC-59CF4B7DE8-L000050](../../agents/research.py#L50) | 50 | `"        pass"` | — |
| [SRC-59CF4B7DE8-L000051](../../agents/research.py#L51) | 51 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000052](../../agents/research.py#L52) | 52 | `"        host = host.encode(\"idna\").decode(\"ascii\").lower()"` | — |
| [SRC-59CF4B7DE8-L000053](../../agents/research.py#L53) | 53 | `"    except UnicodeError:"` | — |
| [SRC-59CF4B7DE8-L000054](../../agents/research.py#L54) | 54 | `"        return host"` | — |
| [SRC-59CF4B7DE8-L000055](../../agents/research.py#L55) | 55 | `"    extracted = _DOMAIN_EXTRACTOR(host)"` | — |
| [SRC-59CF4B7DE8-L000056](../../agents/research.py#L56) | 56 | `"    return (extracted.top_domain_under_public_suffix or host).lower()"` | — |
| [SRC-59CF4B7DE8-L000057](../../agents/research.py#L57) | 57 | `""` | — |
| [SRC-59CF4B7DE8-L000058](../../agents/research.py#L58) | 58 | `"SOCIAL_DOMAINS = {"` | — |
| [SRC-59CF4B7DE8-L000059](../../agents/research.py#L59) | 59 | `"    \"reddit\": \"reddit.com\","` | — |
| [SRC-59CF4B7DE8-L000060](../../agents/research.py#L60) | 60 | `"    \"youtube\": \"youtube.com\","` | — |
| [SRC-59CF4B7DE8-L000061](../../agents/research.py#L61) | 61 | `"    \"facebook\": \"facebook.com\","` | — |
| [SRC-59CF4B7DE8-L000062](../../agents/research.py#L62) | 62 | `"    \"instagram\": \"instagram.com\","` | — |
| [SRC-59CF4B7DE8-L000063](../../agents/research.py#L63) | 63 | `"    \"x\": \"x.com\","` | — |
| [SRC-59CF4B7DE8-L000064](../../agents/research.py#L64) | 64 | `"    \"twitter\": \"twitter.com\","` | — |
| [SRC-59CF4B7DE8-L000065](../../agents/research.py#L65) | 65 | `"    \"tiktok\": \"tiktok.com\","` | — |
| [SRC-59CF4B7DE8-L000066](../../agents/research.py#L66) | 66 | `"    \"linkedin\": \"linkedin.com\","` | — |
| [SRC-59CF4B7DE8-L000067](../../agents/research.py#L67) | 67 | `"    \"threads\": \"threads.net\","` | — |
| [SRC-59CF4B7DE8-L000068](../../agents/research.py#L68) | 68 | `"    \"bluesky\": \"bsky.app\","` | — |
| [SRC-59CF4B7DE8-L000069](../../agents/research.py#L69) | 69 | `"}"` | — |
| [SRC-59CF4B7DE8-L000070](../../agents/research.py#L70) | 70 | `""` | — |
| [SRC-59CF4B7DE8-L000071](../../agents/research.py#L71) | 71 | `"_SOCIAL_TERMS = ("` | — |
| [SRC-59CF4B7DE8-L000072](../../agents/research.py#L72) | 72 | `"    \"social media\", \"social network\", \"social posts\", \"social pages\", \"public social\", \"public posts\","` | — |
| [SRC-59CF4B7DE8-L000073](../../agents/research.py#L73) | 73 | `"    \"facebook\", \"instagram\", \"reddit\", \"youtube\", \"twitter\", \"x.com\","` | — |
| [SRC-59CF4B7DE8-L000074](../../agents/research.py#L74) | 74 | `"    \"tiktok\", \"linkedin\", \"threads\", \"bluesky\","` | — |
| [SRC-59CF4B7DE8-L000075](../../agents/research.py#L75) | 75 | `"    \"سوشيال\", \"التواصل الاجتماعي\", \"مواقع التواصل\", \"صفحات التواصل\","` | — |
| [SRC-59CF4B7DE8-L000076](../../agents/research.py#L76) | 76 | `"    \"منشورات\", \"تعليقات الناس\", \"آراء الناس\", \"تجارب المستخدمين\","` | — |
| [SRC-59CF4B7DE8-L000077](../../agents/research.py#L77) | 77 | `"    \"تجارب العملاء\", \"اراء العملاء\", \"آراء العملاء\", \"رأي الناس\","` | — |
| [SRC-59CF4B7DE8-L000078](../../agents/research.py#L78) | 78 | `"    \"كلام الناس\", \"الناس بتقول\", \"مراجعات العملاء\", \"تعليقات العملاء\","` | — |
| [SRC-59CF4B7DE8-L000079](../../agents/research.py#L79) | 79 | `"    \"بوستات\", \"فيدوهات\", \"فيديوهات\", \"ريلز\", \"تويتر\", \"فيسبوك\","` | — |
| [SRC-59CF4B7DE8-L000080](../../agents/research.py#L80) | 80 | `"    \"انستجرام\", \"إنستجرام\", \"تيك توك\", \"لينكدان\", \"لينكدإن\","` | — |
| [SRC-59CF4B7DE8-L000081](../../agents/research.py#L81) | 81 | `"    \"مصادر العملاء\", \"عملاء محتملين\", \"العملاء المحتملين\","` | — |
| [SRC-59CF4B7DE8-L000082](../../agents/research.py#L82) | 82 | `")"` | — |
| [SRC-59CF4B7DE8-L000083](../../agents/research.py#L83) | 83 | `""` | — |
| [SRC-59CF4B7DE8-L000084](../../agents/research.py#L84) | 84 | `"_FRESH_TERMS = ("` | — |
| [SRC-59CF4B7DE8-L000085](../../agents/research.py#L85) | 85 | `"    \"latest\", \"current\", \"today\", \"this week\", \"recent\", \"breaking\", \"news\","` | — |
| [SRC-59CF4B7DE8-L000086](../../agents/research.py#L86) | 86 | `"    \"now\", \"2026\", \"latest price\", \"market price\", \"updated\","` | — |
| [SRC-59CF4B7DE8-L000087](../../agents/research.py#L87) | 87 | `"    \"آخر\", \"اخر\", \"احدث\", \"أحدث\", \"حاليا\", \"حالياً\", \"الآن\", \"دلوقتي\", \"النهارده\", \"مؤخرًا\", \"مؤخرا\", \"اليوم\", \"هذا الاسبوع\","` | — |
| [SRC-59CF4B7DE8-L000088](../../agents/research.py#L88) | 88 | `"    \"هذا الأسبوع\", \"آخر الأخبار\", \"اخر الاخبار\", \"مستجدات\", \"حديث\","` | — |
| [SRC-59CF4B7DE8-L000089](../../agents/research.py#L89) | 89 | `"    \"سعر اليوم\", \"الاسعار الحالية\", \"الأسعار الحالية\", \"جديد\","` | — |
| [SRC-59CF4B7DE8-L000090](../../agents/research.py#L90) | 90 | `")"` | — |
| [SRC-59CF4B7DE8-L000091](../../agents/research.py#L91) | 91 | `""` | — |
| [SRC-59CF4B7DE8-L000092](../../agents/research.py#L92) | 92 | `"_DEEP_TERMS = ("` | — |
| [SRC-59CF4B7DE8-L000093](../../agents/research.py#L93) | 93 | `"    \"deep research\", \"in-depth\", \"comprehensive\", \"exhaustive\", \"compare\","` | — |
| [SRC-59CF4B7DE8-L000094](../../agents/research.py#L94) | 94 | `"    \"comparison\", \"pros and cons\", \"investigate\", \"evidence\", \"sources\","` | — |
| [SRC-59CF4B7DE8-L000095](../../agents/research.py#L95) | 95 | `"    \"بحث عميق\", \"بحث معمق\", \"بحث مكثف\", \"بحث شامل\", \"بالتفصيل\", \"قارن\","` | — |
| [SRC-59CF4B7DE8-L000096](../../agents/research.py#L96) | 96 | `"    \"مقارنة\", \"استقصاء\", \"تحقق\", \"تأكد\", \"مصادر\", \"أدلة\", \"ادلة\","` | — |
| [SRC-59CF4B7DE8-L000097](../../agents/research.py#L97) | 97 | `"    \"كل الجوانب\", \"بحث واسع\", \"متكامل\","` | — |
| [SRC-59CF4B7DE8-L000098](../../agents/research.py#L98) | 98 | `")"` | — |
| [SRC-59CF4B7DE8-L000099](../../agents/research.py#L99) | 99 | `""` | — |
| [SRC-59CF4B7DE8-L000100](../../agents/research.py#L100) | 100 | `""` | — |
| [SRC-59CF4B7DE8-L000101](../../agents/research.py#L101) | 101 | `"def extract_urls(text: str) -> list[str]:"` | — |
| [SRC-59CF4B7DE8-L000102](../../agents/research.py#L102) | 102 | `"    \"\"\"Extract explicit HTTP(S) URLs without trying to interpret their content as instructions.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000103](../../agents/research.py#L103) | 103 | `"    candidates = re.findall(r\"https?://[^\\s<>()]+\", text or \"\", flags=re.IGNORECASE)"` | — |
| [SRC-59CF4B7DE8-L000104](../../agents/research.py#L104) | 104 | `"    cleaned: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000105](../../agents/research.py#L105) | 105 | `"    for value in candidates:"` | — |
| [SRC-59CF4B7DE8-L000106](../../agents/research.py#L106) | 106 | `"        url = value.rstrip(\".,;!?،؛:)\\\"'»\")"` | — |
| [SRC-59CF4B7DE8-L000107](../../agents/research.py#L107) | 107 | `"        if url and url not in cleaned:"` | — |
| [SRC-59CF4B7DE8-L000108](../../agents/research.py#L108) | 108 | `"            cleaned.append(url[:2048])"` | — |
| [SRC-59CF4B7DE8-L000109](../../agents/research.py#L109) | 109 | `"        if len(cleaned) >= 5:"` | — |
| [SRC-59CF4B7DE8-L000110](../../agents/research.py#L110) | 110 | `"            break"` | — |
| [SRC-59CF4B7DE8-L000111](../../agents/research.py#L111) | 111 | `"    return cleaned"` | — |
| [SRC-59CF4B7DE8-L000112](../../agents/research.py#L112) | 112 | `""` | — |
| [SRC-59CF4B7DE8-L000113](../../agents/research.py#L113) | 113 | `""` | — |
| [SRC-59CF4B7DE8-L000114](../../agents/research.py#L114) | 114 | `"def _compact(value: Any, limit: int = MAX_QUERY_CHARS) -> str:"` | — |
| [SRC-59CF4B7DE8-L000115](../../agents/research.py#L115) | 115 | `"    if not isinstance(value, str):"` | — |
| [SRC-59CF4B7DE8-L000116](../../agents/research.py#L116) | 116 | `"        return \"\""` | — |
| [SRC-59CF4B7DE8-L000117](../../agents/research.py#L117) | 117 | `"    return re.sub(r\"\\s+\", \" \", value).strip()[:limit]"` | — |
| [SRC-59CF4B7DE8-L000118](../../agents/research.py#L118) | 118 | `""` | — |
| [SRC-59CF4B7DE8-L000119](../../agents/research.py#L119) | 119 | `""` | — |
| [SRC-59CF4B7DE8-L000120](../../agents/research.py#L120) | 120 | `"_ARABIC_RE = re.compile(r\"[؀-ۿ]\")"` | — |
| [SRC-59CF4B7DE8-L000121](../../agents/research.py#L121) | 121 | `""` | — |
| [SRC-59CF4B7DE8-L000122](../../agents/research.py#L122) | 122 | `""` | — |
| [SRC-59CF4B7DE8-L000123](../../agents/research.py#L123) | 123 | `"def _normalize_arabic(text: str) -> str:"` | — |
| [SRC-59CF4B7DE8-L000124](../../agents/research.py#L124) | 124 | `"    if not text:"` | — |
| [SRC-59CF4B7DE8-L000125](../../agents/research.py#L125) | 125 | `"        return \"\""` | — |
| [SRC-59CF4B7DE8-L000126](../../agents/research.py#L126) | 126 | `"    return (text.replace(\"\\u0623\", \"\\u0627\")"` | — |
| [SRC-59CF4B7DE8-L000127](../../agents/research.py#L127) | 127 | `"                .replace(\"\\u0625\", \"\\u0627\")"` | — |
| [SRC-59CF4B7DE8-L000128](../../agents/research.py#L128) | 128 | `"                .replace(\"\\u0622\", \"\\u0627\")"` | — |
| [SRC-59CF4B7DE8-L000129](../../agents/research.py#L129) | 129 | `"                .replace(\"\\u0629\", \"\\u0647\")"` | — |
| [SRC-59CF4B7DE8-L000130](../../agents/research.py#L130) | 130 | `"                .replace(\"\\u0649\", \"\\u064a\"))"` | — |
| [SRC-59CF4B7DE8-L000131](../../agents/research.py#L131) | 131 | `""` | — |
| [SRC-59CF4B7DE8-L000132](../../agents/research.py#L132) | 132 | `""` | — |
| [SRC-59CF4B7DE8-L000133](../../agents/research.py#L133) | 133 | `"def _contains_any(text: str, terms: tuple) -> bool:"` | — |
| [SRC-59CF4B7DE8-L000134](../../agents/research.py#L134) | 134 | `"    if not text:"` | — |
| [SRC-59CF4B7DE8-L000135](../../agents/research.py#L135) | 135 | `"        return False"` | — |
| [SRC-59CF4B7DE8-L000136](../../agents/research.py#L136) | 136 | `"    haystack = _normalize_arabic(text.casefold())"` | — |
| [SRC-59CF4B7DE8-L000137](../../agents/research.py#L137) | 137 | `"    for term in terms:"` | — |
| [SRC-59CF4B7DE8-L000138](../../agents/research.py#L138) | 138 | `"        if not term:"` | — |
| [SRC-59CF4B7DE8-L000139](../../agents/research.py#L139) | 139 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000140](../../agents/research.py#L140) | 140 | `"        t = _normalize_arabic(term.casefold())"` | — |
| [SRC-59CF4B7DE8-L000141](../../agents/research.py#L141) | 141 | `"        if _ARABIC_RE.search(t):"` | — |
| [SRC-59CF4B7DE8-L000142](../../agents/research.py#L142) | 142 | `"            if t in haystack:"` | — |
| [SRC-59CF4B7DE8-L000143](../../agents/research.py#L143) | 143 | `"                return True"` | — |
| [SRC-59CF4B7DE8-L000144](../../agents/research.py#L144) | 144 | `"        else:"` | — |
| [SRC-59CF4B7DE8-L000145](../../agents/research.py#L145) | 145 | `"            pat = r\"(?<![a-zA-Z0-9])\" + re.escape(t) + r\"(?![a-zA-Z0-9])\""` | — |
| [SRC-59CF4B7DE8-L000146](../../agents/research.py#L146) | 146 | `"            if re.search(pat, haystack):"` | — |
| [SRC-59CF4B7DE8-L000147](../../agents/research.py#L147) | 147 | `"                return True"` | — |
| [SRC-59CF4B7DE8-L000148](../../agents/research.py#L148) | 148 | `"    return False"` | — |
| [SRC-59CF4B7DE8-L000149](../../agents/research.py#L149) | 149 | `""` | — |
| [SRC-59CF4B7DE8-L000150](../../agents/research.py#L150) | 150 | `""` | — |
| [SRC-59CF4B7DE8-L000151](../../agents/research.py#L151) | 151 | `"def detect_social_focus(question: str, history: list[dict[str, str]] \| None = None) -> bool:"` | — |
| [SRC-59CF4B7DE8-L000152](../../agents/research.py#L152) | 152 | `"    context = question + \" \" + \" \".join("` | — |
| [SRC-59CF4B7DE8-L000153](../../agents/research.py#L153) | 153 | `"        item.get(\"content\", \"\") for item in (history or [])[-4:]"` | — |
| [SRC-59CF4B7DE8-L000154](../../agents/research.py#L154) | 154 | `"    )"` | — |
| [SRC-59CF4B7DE8-L000155](../../agents/research.py#L155) | 155 | `"    return _contains_any(context, _SOCIAL_TERMS)"` | — |
| [SRC-59CF4B7DE8-L000156](../../agents/research.py#L156) | 156 | `""` | — |
| [SRC-59CF4B7DE8-L000157](../../agents/research.py#L157) | 157 | `""` | — |
| [SRC-59CF4B7DE8-L000158](../../agents/research.py#L158) | 158 | `"def detect_freshness(question: str) -> bool:"` | — |
| [SRC-59CF4B7DE8-L000159](../../agents/research.py#L159) | 159 | `"    return _contains_any(question, _FRESH_TERMS)"` | — |
| [SRC-59CF4B7DE8-L000160](../../agents/research.py#L160) | 160 | `""` | — |
| [SRC-59CF4B7DE8-L000161](../../agents/research.py#L161) | 161 | `""` | — |
| [SRC-59CF4B7DE8-L000162](../../agents/research.py#L162) | 162 | `"def detect_depth(question: str) -> str:"` | — |
| [SRC-59CF4B7DE8-L000163](../../agents/research.py#L163) | 163 | `"    return \"deep\" if _contains_any(question, _DEEP_TERMS) else \"standard\""` | — |
| [SRC-59CF4B7DE8-L000164](../../agents/research.py#L164) | 164 | `""` | — |
| [SRC-59CF4B7DE8-L000165](../../agents/research.py#L165) | 165 | `""` | — |
| [SRC-59CF4B7DE8-L000166](../../agents/research.py#L166) | 166 | `"def mentioned_social_platforms(text: str) -> list[str]:"` | — |
| [SRC-59CF4B7DE8-L000167](../../agents/research.py#L167) | 167 | `"    rules = ("` | — |
| [SRC-59CF4B7DE8-L000168](../../agents/research.py#L168) | 168 | `"        (\"reddit\", (\"reddit\", \"ريديت\")),"` | — |
| [SRC-59CF4B7DE8-L000169](../../agents/research.py#L169) | 169 | `"        (\"youtube\", (\"youtube\", \"يوتيوب\")),"` | — |
| [SRC-59CF4B7DE8-L000170](../../agents/research.py#L170) | 170 | `"        (\"facebook\", (\"facebook\", \"فيسبوك\", \"فيس بوك\")),"` | — |
| [SRC-59CF4B7DE8-L000171](../../agents/research.py#L171) | 171 | `"        (\"instagram\", (\"instagram\", \"انستجرام\", \"إنستجرام\")),"` | — |
| [SRC-59CF4B7DE8-L000172](../../agents/research.py#L172) | 172 | `"        (\"x\", (\"x.com\", \"twitter\", \"تويتر\", \"اكس\", \"إكس\")),"` | — |
| [SRC-59CF4B7DE8-L000173](../../agents/research.py#L173) | 173 | `"        (\"tiktok\", (\"tiktok\", \"تيك توك\")),"` | — |
| [SRC-59CF4B7DE8-L000174](../../agents/research.py#L174) | 174 | `"        (\"linkedin\", (\"linkedin\", \"لينكدان\", \"لينكدإن\")),"` | — |
| [SRC-59CF4B7DE8-L000175](../../agents/research.py#L175) | 175 | `"        (\"threads\", (\"threads\", \"ثريدز\")),"` | — |
| [SRC-59CF4B7DE8-L000176](../../agents/research.py#L176) | 176 | `"        (\"bluesky\", (\"bluesky\", \"بلو سكاي\")),"` | — |
| [SRC-59CF4B7DE8-L000177](../../agents/research.py#L177) | 177 | `"    )"` | — |
| [SRC-59CF4B7DE8-L000178](../../agents/research.py#L178) | 178 | `"    low = text.casefold()"` | — |
| [SRC-59CF4B7DE8-L000179](../../agents/research.py#L179) | 179 | `"    return [name for name, aliases in rules if any(alias.casefold() in low for alias in aliases)]"` | — |
| [SRC-59CF4B7DE8-L000180](../../agents/research.py#L180) | 180 | `""` | — |
| [SRC-59CF4B7DE8-L000181](../../agents/research.py#L181) | 181 | `""` | — |
| [SRC-59CF4B7DE8-L000182](../../agents/research.py#L182) | 182 | `"def fallback_plan("` | — |
| [SRC-59CF4B7DE8-L000183](../../agents/research.py#L183) | 183 | `"    question: str, history: list[dict[str, str]] \| None = None"` | — |
| [SRC-59CF4B7DE8-L000184](../../agents/research.py#L184) | 184 | `") -> dict[str, Any]:"` | — |
| [SRC-59CF4B7DE8-L000185](../../agents/research.py#L185) | 185 | `"    \"\"\"Build a small but varied plan when no model planner is configured or parsing fails.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000186](../../agents/research.py#L186) | 186 | `"    contextual_question = resolve_followup_query(question, history)"` | — |
| [SRC-59CF4B7DE8-L000187](../../agents/research.py#L187) | 187 | `"    direct_urls = extract_urls(question)"` | — |
| [SRC-59CF4B7DE8-L000188](../../agents/research.py#L188) | 188 | `"    base = _compact(re.sub(r\"https?://[^\\s<>()]+\", \" \", contextual_question), 500)"` | — |
| [SRC-59CF4B7DE8-L000189](../../agents/research.py#L189) | 189 | `"    if not base:"` | — |
| [SRC-59CF4B7DE8-L000190](../../agents/research.py#L190) | 190 | `"        base = \"اقرأ محتوى الصفحة\" if re.search(r\"[\\u0600-\\u06FF]\", question) else \"read the linked page\""` | — |
| [SRC-59CF4B7DE8-L000191](../../agents/research.py#L191) | 191 | `"    social_focus = detect_social_focus(question, history)"` | — |
| [SRC-59CF4B7DE8-L000192](../../agents/research.py#L192) | 192 | `"    fresh = detect_freshness(question)"` | — |
| [SRC-59CF4B7DE8-L000193](../../agents/research.py#L193) | 193 | `"    detected_depth = detect_depth(question)"` | — |
| [SRC-59CF4B7DE8-L000194](../../agents/research.py#L194) | 194 | `"    deep = detected_depth == \"deep\""` | — |
| [SRC-59CF4B7DE8-L000195](../../agents/research.py#L195) | 195 | `"    platforms = mentioned_social_platforms(question + \" \" + \" \".join("` | — |
| [SRC-59CF4B7DE8-L000196](../../agents/research.py#L196) | 196 | `"        item.get(\"content\", \"\") for item in (history or [])[-4:]"` | — |
| [SRC-59CF4B7DE8-L000197](../../agents/research.py#L197) | 197 | `"    ))"` | — |
| [SRC-59CF4B7DE8-L000198](../../agents/research.py#L198) | 198 | `"    queries: list[str] = [base]"` | — |
| [SRC-59CF4B7DE8-L000199](../../agents/research.py#L199) | 199 | `""` | — |
| [SRC-59CF4B7DE8-L000200](../../agents/research.py#L200) | 200 | `"    if fresh and base:"` | — |
| [SRC-59CF4B7DE8-L000201](../../agents/research.py#L201) | 201 | `"        queries.append(_compact(base + \" أحدث مستجدات آخر الأخبار\", 500))"` | — |
| [SRC-59CF4B7DE8-L000202](../../agents/research.py#L202) | 202 | `"    if _contains_any(question, (\"قارن\", \"مقارنة\", \"compare\", \"versus\", \"vs\", \"الفرق بين\")):"` | — |
| [SRC-59CF4B7DE8-L000203](../../agents/research.py#L203) | 203 | `"        queries.append(_compact(base + \" مقارنة مراجعات مميزات عيوب\", 500))"` | — |
| [SRC-59CF4B7DE8-L000204](../../agents/research.py#L204) | 204 | `""` | — |
| [SRC-59CF4B7DE8-L000205](../../agents/research.py#L205) | 205 | `"    if social_focus:"` | — |
| [SRC-59CF4B7DE8-L000206](../../agents/research.py#L206) | 206 | `"        selected = platforms or [\"facebook\", \"instagram\", \"reddit\"]"` | — |
| [SRC-59CF4B7DE8-L000207](../../agents/research.py#L207) | 207 | `"        for platform in selected[:3]:"` | — |
| [SRC-59CF4B7DE8-L000208](../../agents/research.py#L208) | 208 | `"            domain = SOCIAL_DOMAINS[platform]"` | — |
| [SRC-59CF4B7DE8-L000209](../../agents/research.py#L209) | 209 | `"            site_query = _compact(f\"site:{domain} {base}\", 500)"` | — |
| [SRC-59CF4B7DE8-L000210](../../agents/research.py#L210) | 210 | `"            if site_query not in queries:"` | — |
| [SRC-59CF4B7DE8-L000211](../../agents/research.py#L211) | 211 | `"                queries.append(site_query)"` | — |
| [SRC-59CF4B7DE8-L000212](../../agents/research.py#L212) | 212 | `""` | — |
| [SRC-59CF4B7DE8-L000213](../../agents/research.py#L213) | 213 | `"    if deep and not social_focus and len(queries) < MAX_PLAN_QUERIES:"` | — |
| [SRC-59CF4B7DE8-L000214](../../agents/research.py#L214) | 214 | `"        queries.append(_compact(base + \" مصادر موثوقة تقارير إحصاءات\", 500))"` | — |
| [SRC-59CF4B7DE8-L000215](../../agents/research.py#L215) | 215 | `""` | — |
| [SRC-59CF4B7DE8-L000216](../../agents/research.py#L216) | 216 | `"    unique: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000217](../../agents/research.py#L217) | 217 | `"    seen: set[str] = set()"` | — |
| [SRC-59CF4B7DE8-L000218](../../agents/research.py#L218) | 218 | `"    for query in queries:"` | — |
| [SRC-59CF4B7DE8-L000219](../../agents/research.py#L219) | 219 | `"        value = _compact(query, 500)"` | — |
| [SRC-59CF4B7DE8-L000220](../../agents/research.py#L220) | 220 | `"        key = value.casefold()"` | — |
| [SRC-59CF4B7DE8-L000221](../../agents/research.py#L221) | 221 | `"        if value and key not in seen:"` | — |
| [SRC-59CF4B7DE8-L000222](../../agents/research.py#L222) | 222 | `"            unique.append(value)"` | — |
| [SRC-59CF4B7DE8-L000223](../../agents/research.py#L223) | 223 | `"            seen.add(key)"` | — |
| [SRC-59CF4B7DE8-L000224](../../agents/research.py#L224) | 224 | `"        if len(unique) >= MAX_PLAN_QUERIES:"` | — |
| [SRC-59CF4B7DE8-L000225](../../agents/research.py#L225) | 225 | `"            break"` | — |
| [SRC-59CF4B7DE8-L000226](../../agents/research.py#L226) | 226 | `""` | — |
| [SRC-59CF4B7DE8-L000227](../../agents/research.py#L227) | 227 | `"    return {"` | — |
| [SRC-59CF4B7DE8-L000228](../../agents/research.py#L228) | 228 | `"        \"queries\": unique or [base],"` | — |
| [SRC-59CF4B7DE8-L000229](../../agents/research.py#L229) | 229 | `"        \"direct_urls\": direct_urls,"` | — |
| [SRC-59CF4B7DE8-L000230](../../agents/research.py#L230) | 230 | `"        \"social_focus\": social_focus,"` | — |
| [SRC-59CF4B7DE8-L000231](../../agents/research.py#L231) | 231 | `"        \"freshness\": \"current\" if fresh else \"any\","` | — |
| [SRC-59CF4B7DE8-L000232](../../agents/research.py#L232) | 232 | `"        \"depth\": detected_depth,"` | — |
| [SRC-59CF4B7DE8-L000233](../../agents/research.py#L233) | 233 | `"        \"platforms\": platforms,"` | — |
| [SRC-59CF4B7DE8-L000234](../../agents/research.py#L234) | 234 | `"        \"planning_method\": \"deterministic_fallback\","` | — |
| [SRC-59CF4B7DE8-L000235](../../agents/research.py#L235) | 235 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000236](../../agents/research.py#L236) | 236 | `""` | — |
| [SRC-59CF4B7DE8-L000237](../../agents/research.py#L237) | 237 | `""` | — |
| [SRC-59CF4B7DE8-L000238](../../agents/research.py#L238) | 238 | `"def validate_plan("` | — |
| [SRC-59CF4B7DE8-L000239](../../agents/research.py#L239) | 239 | `"    candidate: Any, question: str, history: list[dict[str, str]] \| None = None"` | — |
| [SRC-59CF4B7DE8-L000240](../../agents/research.py#L240) | 240 | `") -> dict[str, Any]:"` | — |
| [SRC-59CF4B7DE8-L000241](../../agents/research.py#L241) | 241 | `"    fallback = fallback_plan(question, history)"` | — |
| [SRC-59CF4B7DE8-L000242](../../agents/research.py#L242) | 242 | `"    if not isinstance(candidate, dict):"` | — |
| [SRC-59CF4B7DE8-L000243](../../agents/research.py#L243) | 243 | `"        return fallback"` | — |
| [SRC-59CF4B7DE8-L000244](../../agents/research.py#L244) | 244 | `"    raw_queries = candidate.get(\"queries\", [])"` | — |
| [SRC-59CF4B7DE8-L000245](../../agents/research.py#L245) | 245 | `"    if not isinstance(raw_queries, list):"` | — |
| [SRC-59CF4B7DE8-L000246](../../agents/research.py#L246) | 246 | `"        return fallback"` | — |
| [SRC-59CF4B7DE8-L000247](../../agents/research.py#L247) | 247 | `"    queries: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000248](../../agents/research.py#L248) | 248 | `"    seen: set[str] = set()"` | — |
| [SRC-59CF4B7DE8-L000249](../../agents/research.py#L249) | 249 | `"    for item in raw_queries:"` | — |
| [SRC-59CF4B7DE8-L000250](../../agents/research.py#L250) | 250 | `"        query = _compact(item, 500)"` | — |
| [SRC-59CF4B7DE8-L000251](../../agents/research.py#L251) | 251 | `"        # Never accept prompt-like multi-line payloads as search-query instructions."` | — |
| [SRC-59CF4B7DE8-L000252](../../agents/research.py#L252) | 252 | `"        query = query.replace(\"\\n\", \" \").replace(\"\\r\", \" \")"` | — |
| [SRC-59CF4B7DE8-L000253](../../agents/research.py#L253) | 253 | `"        if len(query) < 2:"` | — |
| [SRC-59CF4B7DE8-L000254](../../agents/research.py#L254) | 254 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000255](../../agents/research.py#L255) | 255 | `"        if query.casefold() not in seen:"` | — |
| [SRC-59CF4B7DE8-L000256](../../agents/research.py#L256) | 256 | `"            seen.add(query.casefold())"` | — |
| [SRC-59CF4B7DE8-L000257](../../agents/research.py#L257) | 257 | `"            queries.append(query)"` | — |
| [SRC-59CF4B7DE8-L000258](../../agents/research.py#L258) | 258 | `"        if len(queries) >= MAX_PLAN_QUERIES:"` | — |
| [SRC-59CF4B7DE8-L000259](../../agents/research.py#L259) | 259 | `"            break"` | — |
| [SRC-59CF4B7DE8-L000260](../../agents/research.py#L260) | 260 | `"    if not queries:"` | — |
| [SRC-59CF4B7DE8-L000261](../../agents/research.py#L261) | 261 | `"        return fallback"` | — |
| [SRC-59CF4B7DE8-L000262](../../agents/research.py#L262) | 262 | `"    base = fallback_plan(question, history)"` | — |
| [SRC-59CF4B7DE8-L000263](../../agents/research.py#L263) | 263 | `"    platforms = candidate.get(\"platforms\")"` | — |
| [SRC-59CF4B7DE8-L000264](../../agents/research.py#L264) | 264 | `"    if not isinstance(platforms, list):"` | — |
| [SRC-59CF4B7DE8-L000265](../../agents/research.py#L265) | 265 | `"        platforms = base[\"platforms\"]"` | — |
| [SRC-59CF4B7DE8-L000266](../../agents/research.py#L266) | 266 | `"    safe_platforms = [p for p in platforms if isinstance(p, str) and p in SOCIAL_DOMAINS]"` | — |
| [SRC-59CF4B7DE8-L000267](../../agents/research.py#L267) | 267 | `"    return {"` | — |
| [SRC-59CF4B7DE8-L000268](../../agents/research.py#L268) | 268 | `"        \"queries\": queries,"` | — |
| [SRC-59CF4B7DE8-L000269](../../agents/research.py#L269) | 269 | `"        \"direct_urls\": fallback[\"direct_urls\"],"` | — |
| [SRC-59CF4B7DE8-L000270](../../agents/research.py#L270) | 270 | `"        \"social_focus\": bool(candidate.get(\"social_focus\", base[\"social_focus\"])),"` | — |
| [SRC-59CF4B7DE8-L000271](../../agents/research.py#L271) | 271 | `"        \"freshness\": \"current\" if candidate.get(\"freshness\") == \"current\" else base[\"freshness\"],"` | — |
| [SRC-59CF4B7DE8-L000272](../../agents/research.py#L272) | 272 | `"        \"depth\": \"deep\" if candidate.get(\"depth\") == \"deep\" else base[\"depth\"],"` | — |
| [SRC-59CF4B7DE8-L000273](../../agents/research.py#L273) | 273 | `"        \"platforms\": list(dict.fromkeys(safe_platforms))[:5],"` | — |
| [SRC-59CF4B7DE8-L000274](../../agents/research.py#L274) | 274 | `"        \"planning_method\": \"language_model\","` | — |
| [SRC-59CF4B7DE8-L000275](../../agents/research.py#L275) | 275 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000276](../../agents/research.py#L276) | 276 | `""` | — |
| [SRC-59CF4B7DE8-L000277](../../agents/research.py#L277) | 277 | `""` | — |
| [SRC-59CF4B7DE8-L000278](../../agents/research.py#L278) | 278 | `"def _canonical_result_url(url: str) -> str:"` | — |
| [SRC-59CF4B7DE8-L000279](../../agents/research.py#L279) | 279 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000280](../../agents/research.py#L280) | 280 | `"        parsed = urlparse(url)"` | — |
| [SRC-59CF4B7DE8-L000281](../../agents/research.py#L281) | 281 | `"        host = (parsed.hostname or \"\").lower().removeprefix(\"www.\")"` | — |
| [SRC-59CF4B7DE8-L000282](../../agents/research.py#L282) | 282 | `"        # Drop fragments and common tracking query parameters before deduplication."` | — |
| [SRC-59CF4B7DE8-L000283](../../agents/research.py#L283) | 283 | `"        parts = []"` | — |
| [SRC-59CF4B7DE8-L000284](../../agents/research.py#L284) | 284 | `"        for part in parsed.query.split(\"&\"):"` | — |
| [SRC-59CF4B7DE8-L000285](../../agents/research.py#L285) | 285 | `"            key = part.split(\"=\", 1)[0].lower()"` | — |
| [SRC-59CF4B7DE8-L000286](../../agents/research.py#L286) | 286 | `"            if key.startswith(\"utm_\") or key in {\"fbclid\", \"gclid\", \"ref\", \"ref_src\"}:"` | — |
| [SRC-59CF4B7DE8-L000287](../../agents/research.py#L287) | 287 | `"                continue"` | — |
| [SRC-59CF4B7DE8-L000288](../../agents/research.py#L288) | 288 | `"            if part:"` | — |
| [SRC-59CF4B7DE8-L000289](../../agents/research.py#L289) | 289 | `"                parts.append(part)"` | — |
| [SRC-59CF4B7DE8-L000290](../../agents/research.py#L290) | 290 | `"        query = \"&\".join(sorted(parts))"` | — |
| [SRC-59CF4B7DE8-L000291](../../agents/research.py#L291) | 291 | `"        path = parsed.path.rstrip(\"/\") or \"/\""` | — |
| [SRC-59CF4B7DE8-L000292](../../agents/research.py#L292) | 292 | `"        return f\"{parsed.scheme.lower()}://{host}{path}\" + (f\"?{query}\" if query else \"\")"` | — |
| [SRC-59CF4B7DE8-L000293](../../agents/research.py#L293) | 293 | `"    except (ValueError, TypeError):"` | — |
| [SRC-59CF4B7DE8-L000294](../../agents/research.py#L294) | 294 | `"        return url"` | — |
| [SRC-59CF4B7DE8-L000295](../../agents/research.py#L295) | 295 | `""` | — |
| [SRC-59CF4B7DE8-L000296](../../agents/research.py#L296) | 296 | `""` | — |
| [SRC-59CF4B7DE8-L000297](../../agents/research.py#L297) | 297 | `"def classify_source(url: str) -> dict[str, str]:"` | — |
| [SRC-59CF4B7DE8-L000298](../../agents/research.py#L298) | 298 | `"    host = (urlparse(url).hostname or \"\").lower().removeprefix(\"www.\")"` | — |
| [SRC-59CF4B7DE8-L000299](../../agents/research.py#L299) | 299 | `"    platform = \"web\""` | — |
| [SRC-59CF4B7DE8-L000300](../../agents/research.py#L300) | 300 | `"    mapping = {"` | — |
| [SRC-59CF4B7DE8-L000301](../../agents/research.py#L301) | 301 | `"        \"reddit.com\": \"reddit\", \"old.reddit.com\": \"reddit\","` | — |
| [SRC-59CF4B7DE8-L000302](../../agents/research.py#L302) | 302 | `"        \"youtube.com\": \"youtube\", \"youtu.be\": \"youtube\","` | — |
| [SRC-59CF4B7DE8-L000303](../../agents/research.py#L303) | 303 | `"        \"facebook.com\": \"facebook\", \"instagram.com\": \"instagram\","` | — |
| [SRC-59CF4B7DE8-L000304](../../agents/research.py#L304) | 304 | `"        \"x.com\": \"x\", \"twitter.com\": \"x\", \"tiktok.com\": \"tiktok\","` | — |
| [SRC-59CF4B7DE8-L000305](../../agents/research.py#L305) | 305 | `"        \"linkedin.com\": \"linkedin\", \"threads.net\": \"threads\","` | — |
| [SRC-59CF4B7DE8-L000306](../../agents/research.py#L306) | 306 | `"        \"bsky.app\": \"bluesky\","` | — |
| [SRC-59CF4B7DE8-L000307](../../agents/research.py#L307) | 307 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000308](../../agents/research.py#L308) | 308 | `"    for domain, label in mapping.items():"` | — |
| [SRC-59CF4B7DE8-L000309](../../agents/research.py#L309) | 309 | `"        if host == domain or host.endswith(\".\" + domain):"` | — |
| [SRC-59CF4B7DE8-L000310](../../agents/research.py#L310) | 310 | `"            platform = label"` | — |
| [SRC-59CF4B7DE8-L000311](../../agents/research.py#L311) | 311 | `"            break"` | — |
| [SRC-59CF4B7DE8-L000312](../../agents/research.py#L312) | 312 | `"    trust = \"general\""` | — |
| [SRC-59CF4B7DE8-L000313](../../agents/research.py#L313) | 313 | `"    if host.endswith((\".gov\", \".gov.eg\", \".gov.uk\")):"` | — |
| [SRC-59CF4B7DE8-L000314](../../agents/research.py#L314) | 314 | `"        trust = \"government\""` | — |
| [SRC-59CF4B7DE8-L000315](../../agents/research.py#L315) | 315 | `"    elif host.endswith((\".edu\", \".ac.uk\", \".edu.eg\")):"` | — |
| [SRC-59CF4B7DE8-L000316](../../agents/research.py#L316) | 316 | `"        trust = \"academic\""` | — |
| [SRC-59CF4B7DE8-L000317](../../agents/research.py#L317) | 317 | `"    elif host == \"news.google.com\" or any("` | — |
| [SRC-59CF4B7DE8-L000318](../../agents/research.py#L318) | 318 | `"        name in host"` | — |
| [SRC-59CF4B7DE8-L000319](../../agents/research.py#L319) | 319 | `"        for name in ("` | — |
| [SRC-59CF4B7DE8-L000320](../../agents/research.py#L320) | 320 | `"            \"reuters.com\", \"apnews.com\", \"bbc.com\", \"bbc.co.uk\","` | — |
| [SRC-59CF4B7DE8-L000321](../../agents/research.py#L321) | 321 | `"            \"ft.com\", \"nytimes.com\", \"theguardian.com\","` | — |
| [SRC-59CF4B7DE8-L000322](../../agents/research.py#L322) | 322 | `"        )"` | — |
| [SRC-59CF4B7DE8-L000323](../../agents/research.py#L323) | 323 | `"    ):"` | — |
| [SRC-59CF4B7DE8-L000324](../../agents/research.py#L324) | 324 | `"        trust = \"news\""` | — |
| [SRC-59CF4B7DE8-L000325](../../agents/research.py#L325) | 325 | `"    elif platform != \"web\":"` | — |
| [SRC-59CF4B7DE8-L000326](../../agents/research.py#L326) | 326 | `"        trust = \"social\""` | — |
| [SRC-59CF4B7DE8-L000327](../../agents/research.py#L327) | 327 | `"    return {\"domain\": host, \"platform\": platform, \"source_class\": trust}"` | — |
| [SRC-59CF4B7DE8-L000328](../../agents/research.py#L328) | 328 | `""` | — |
| [SRC-59CF4B7DE8-L000329](../../agents/research.py#L329) | 329 | `""` | — |
| [SRC-59CF4B7DE8-L000330](../../agents/research.py#L330) | 330 | `"def fuse_ranked_results("` | — |
| [SRC-59CF4B7DE8-L000331](../../agents/research.py#L331) | 331 | `"    batches: list[dict[str, Any]], limit: int = MAX_FUSED_RESULTS"` | — |
| [SRC-59CF4B7DE8-L000332](../../agents/research.py#L332) | 332 | `") -> list[dict[str, Any]]:"` | — |
| [SRC-59CF4B7DE8-L000333](../../agents/research.py#L333) | 333 | `"    \"\"\"Reciprocal-rank-fuse result sets across queries/providers and dedupe URLs.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000334](../../agents/research.py#L334) | 334 | `"    accumulated: dict[str, dict[str, Any]] = {}"` | — |
| [SRC-59CF4B7DE8-L000335](../../agents/research.py#L335) | 335 | `"    for batch in batches:"` | — |
| [SRC-59CF4B7DE8-L000336](../../agents/research.py#L336) | 336 | `"        query = _compact(batch.get(\"query\", \"\"), 500)"` | — |
| [SRC-59CF4B7DE8-L000337](../../agents/research.py#L337) | 337 | `"        provider = _compact(batch.get(\"provider\", \"search\"), 80)"` | — |
| [SRC-59CF4B7DE8-L000338](../../agents/research.py#L338) | 338 | `"        results = batch.get(\"results\", [])"` | — |
| [SRC-59CF4B7DE8-L000339](../../agents/research.py#L339) | 339 | `"        if not isinstance(results, list):"` | — |
| [SRC-59CF4B7DE8-L000340](../../agents/research.py#L340) | 340 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000341](../../agents/research.py#L341) | 341 | `"        for position, source in enumerate(results, 1):"` | — |
| [SRC-59CF4B7DE8-L000342](../../agents/research.py#L342) | 342 | `"            if not isinstance(source, dict) or not source.get(\"url\"):"` | — |
| [SRC-59CF4B7DE8-L000343](../../agents/research.py#L343) | 343 | `"                continue"` | — |
| [SRC-59CF4B7DE8-L000344](../../agents/research.py#L344) | 344 | `"            url = _canonical_result_url(str(source[\"url\"]))"` | — |
| [SRC-59CF4B7DE8-L000345](../../agents/research.py#L345) | 345 | `"            if not url.startswith((\"https://\", \"http://\")):"` | — |
| [SRC-59CF4B7DE8-L000346](../../agents/research.py#L346) | 346 | `"                continue"` | — |
| [SRC-59CF4B7DE8-L000347](../../agents/research.py#L347) | 347 | `"            entry = accumulated.get(url)"` | — |
| [SRC-59CF4B7DE8-L000348](../../agents/research.py#L348) | 348 | `"            if entry is None:"` | — |
| [SRC-59CF4B7DE8-L000349](../../agents/research.py#L349) | 349 | `"                publisher_url = _compact(source.get(\"publisher_url\") or \"\", 2048)"` | — |
| [SRC-59CF4B7DE8-L000350](../../agents/research.py#L350) | 350 | `"                source_identity_url = publisher_url or str(source[\"url\"])"` | — |
| [SRC-59CF4B7DE8-L000351](../../agents/research.py#L351) | 351 | `"                entry = {"` | — |
| [SRC-59CF4B7DE8-L000352](../../agents/research.py#L352) | 352 | `"                    \"title\": _compact(source.get(\"title\") or \"نتيجة ويب\", 300),"` | — |
| [SRC-59CF4B7DE8-L000353](../../agents/research.py#L353) | 353 | `"                    \"url\": str(source[\"url\"]),"` | — |
| [SRC-59CF4B7DE8-L000354](../../agents/research.py#L354) | 354 | `"                    \"snippet\": _compact(source.get(\"snippet\") or \"\", 1800),"` | — |
| [SRC-59CF4B7DE8-L000355](../../agents/research.py#L355) | 355 | `"                    \"page_text\": _compact(source.get(\"page_text\") or \"\", 12_000),"` | — |
| [SRC-59CF4B7DE8-L000356](../../agents/research.py#L356) | 356 | `"                    \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-59CF4B7DE8-L000357](../../agents/research.py#L357) | 357 | `"                    \"providers\": [],"` | — |
| [SRC-59CF4B7DE8-L000358](../../agents/research.py#L358) | 358 | `"                    \"queries\": [],"` | — |
| [SRC-59CF4B7DE8-L000359](../../agents/research.py#L359) | 359 | `"                    \"rank_score\": 0.0,"` | — |
| [SRC-59CF4B7DE8-L000360](../../agents/research.py#L360) | 360 | `"                    \"best_raw_rank\": position,"` | — |
| [SRC-59CF4B7DE8-L000361](../../agents/research.py#L361) | 361 | `"                    \"published_at\": _compact(source.get(\"published_at\") or \"\", 100),"` | — |
| [SRC-59CF4B7DE8-L000362](../../agents/research.py#L362) | 362 | `"                    \"publisher_name\": _compact(source.get(\"publisher_name\") or \"\", 200),"` | — |
| [SRC-59CF4B7DE8-L000363](../../agents/research.py#L363) | 363 | `"                    \"publisher_url\": publisher_url,"` | — |
| [SRC-59CF4B7DE8-L000364](../../agents/research.py#L364) | 364 | `"                    \"publisher_domain\": _compact(source.get(\"publisher_domain\") or \"\", 300),"` | — |
| [SRC-59CF4B7DE8-L000365](../../agents/research.py#L365) | 365 | `"                }"` | — |
| [SRC-59CF4B7DE8-L000366](../../agents/research.py#L366) | 366 | `"                entry.update(classify_source(source_identity_url))"` | — |
| [SRC-59CF4B7DE8-L000367](../../agents/research.py#L367) | 367 | `"                accumulated[url] = entry"` | — |
| [SRC-59CF4B7DE8-L000368](../../agents/research.py#L368) | 368 | `"            elif source.get(\"publisher_url\") and not entry.get(\"publisher_url\"):"` | — |
| [SRC-59CF4B7DE8-L000369](../../agents/research.py#L369) | 369 | `"                entry[\"publisher_url\"] = _compact(source.get(\"publisher_url\"), 2048)"` | — |
| [SRC-59CF4B7DE8-L000370](../../agents/research.py#L370) | 370 | `"                entry[\"publisher_name\"] = _compact(source.get(\"publisher_name\") or \"\", 200)"` | — |
| [SRC-59CF4B7DE8-L000371](../../agents/research.py#L371) | 371 | `"                entry[\"publisher_domain\"] = _compact(source.get(\"publisher_domain\") or \"\", 300)"` | — |
| [SRC-59CF4B7DE8-L000372](../../agents/research.py#L372) | 372 | `"                entry.update(classify_source(entry[\"publisher_url\"]))"` | — |
| [SRC-59CF4B7DE8-L000373](../../agents/research.py#L373) | 373 | `"            entry[\"rank_score\"] += 1.0 / (60 + position)"` | — |
| [SRC-59CF4B7DE8-L000374](../../agents/research.py#L374) | 374 | `"            entry[\"best_raw_rank\"] = min(entry[\"best_raw_rank\"], position)"` | — |
| [SRC-59CF4B7DE8-L000375](../../agents/research.py#L375) | 375 | `"            if provider and provider not in entry[\"providers\"]:"` | — |
| [SRC-59CF4B7DE8-L000376](../../agents/research.py#L376) | 376 | `"                entry[\"providers\"].append(provider)"` | — |
| [SRC-59CF4B7DE8-L000377](../../agents/research.py#L377) | 377 | `"            if query and query not in entry[\"queries\"]:"` | — |
| [SRC-59CF4B7DE8-L000378](../../agents/research.py#L378) | 378 | `"                entry[\"queries\"].append(query)"` | — |
| [SRC-59CF4B7DE8-L000379](../../agents/research.py#L379) | 379 | `"            if len(str(source.get(\"snippet\") or \"\")) > len(entry[\"snippet\"]):"` | — |
| [SRC-59CF4B7DE8-L000380](../../agents/research.py#L380) | 380 | `"                entry[\"snippet\"] = _compact(source.get(\"snippet\"), 1800)"` | — |
| [SRC-59CF4B7DE8-L000381](../../agents/research.py#L381) | 381 | `"            if source.get(\"published_at\") and not entry.get(\"published_at\"):"` | — |
| [SRC-59CF4B7DE8-L000382](../../agents/research.py#L382) | 382 | `"                entry[\"published_at\"] = _compact(source[\"published_at\"], 100)"` | — |
| [SRC-59CF4B7DE8-L000383](../../agents/research.py#L383) | 383 | `"            if source.get(\"page_text\") and not entry[\"page_text\"]:"` | — |
| [SRC-59CF4B7DE8-L000384](../../agents/research.py#L384) | 384 | `"                entry[\"page_text\"] = _compact(source[\"page_text\"], 12_000)"` | — |
| [SRC-59CF4B7DE8-L000385](../../agents/research.py#L385) | 385 | `"                entry[\"page_fetched\"] = True"` | — |
| [SRC-59CF4B7DE8-L000386](../../agents/research.py#L386) | 386 | `"    # A cross-query result gets a modest consensus bonus; official/academic sources"` | — |
| [SRC-59CF4B7DE8-L000387](../../agents/research.py#L387) | 387 | `"    # get a small prior, never enough to override actual query relevance."` | — |
| [SRC-59CF4B7DE8-L000388](../../agents/research.py#L388) | 388 | `"    for entry in accumulated.values():"` | — |
| [SRC-59CF4B7DE8-L000389](../../agents/research.py#L389) | 389 | `"        entry[\"rank_score\"] += min(len(entry[\"queries\"]), 4) * 0.00015"` | — |
| [SRC-59CF4B7DE8-L000390](../../agents/research.py#L390) | 390 | `"        if entry[\"source_class\"] in {\"government\", \"academic\"}:"` | — |
| [SRC-59CF4B7DE8-L000391](../../agents/research.py#L391) | 391 | `"            entry[\"rank_score\"] += 0.0001"` | — |
| [SRC-59CF4B7DE8-L000392](../../agents/research.py#L392) | 392 | `"        if \"user_supplied_url\" in entry[\"providers\"]:"` | — |
| [SRC-59CF4B7DE8-L000393](../../agents/research.py#L393) | 393 | `"            entry[\"rank_score\"] += 0.5"` | — |
| [SRC-59CF4B7DE8-L000394](../../agents/research.py#L394) | 394 | `"    ranked = sorted(accumulated.values(), key=lambda item: item[\"rank_score\"], reverse=True)"` | — |
| [SRC-59CF4B7DE8-L000395](../../agents/research.py#L395) | 395 | `"    return ranked[:max(1, min(int(limit), MAX_FUSED_RESULTS))]"` | — |
| [SRC-59CF4B7DE8-L000396](../../agents/research.py#L396) | 396 | `""` | — |
| [SRC-59CF4B7DE8-L000397](../../agents/research.py#L397) | 397 | `""` | — |
| [SRC-59CF4B7DE8-L000398](../../agents/research.py#L398) | 398 | `""` | — |
| [SRC-59CF4B7DE8-L000399](../../agents/research.py#L399) | 399 | `"def _parse_publication_date(value: Any, now: datetime \| None = None) -> datetime \| None:"` | — |
| [SRC-59CF4B7DE8-L000400](../../agents/research.py#L400) | 400 | `"    \"\"\"Parse common search/RSS publication dates without guessing missing dates.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000401](../../agents/research.py#L401) | 401 | `"    if not isinstance(value, str) or not value.strip():"` | — |
| [SRC-59CF4B7DE8-L000402](../../agents/research.py#L402) | 402 | `"        return None"` | — |
| [SRC-59CF4B7DE8-L000403](../../agents/research.py#L403) | 403 | `"    raw = value.strip()"` | — |
| [SRC-59CF4B7DE8-L000404](../../agents/research.py#L404) | 404 | `"    current = now or datetime.now(UTC)"` | — |
| [SRC-59CF4B7DE8-L000405](../../agents/research.py#L405) | 405 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000406](../../agents/research.py#L406) | 406 | `"        parsed = parsedate_to_datetime(raw)"` | — |
| [SRC-59CF4B7DE8-L000407](../../agents/research.py#L407) | 407 | `"        if parsed:"` | — |
| [SRC-59CF4B7DE8-L000408](../../agents/research.py#L408) | 408 | `"            return parsed.replace(tzinfo=parsed.tzinfo or UTC).astimezone(UTC)"` | — |
| [SRC-59CF4B7DE8-L000409](../../agents/research.py#L409) | 409 | `"    except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-59CF4B7DE8-L000410](../../agents/research.py#L410) | 410 | `"        pass"` | — |
| [SRC-59CF4B7DE8-L000411](../../agents/research.py#L411) | 411 | `"    iso_value = raw.replace(\"Z\", \"+00:00\")"` | — |
| [SRC-59CF4B7DE8-L000412](../../agents/research.py#L412) | 412 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000413](../../agents/research.py#L413) | 413 | `"        parsed = datetime.fromisoformat(iso_value)"` | — |
| [SRC-59CF4B7DE8-L000414](../../agents/research.py#L414) | 414 | `"        return parsed.replace(tzinfo=parsed.tzinfo or UTC).astimezone(UTC)"` | — |
| [SRC-59CF4B7DE8-L000415](../../agents/research.py#L415) | 415 | `"    except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-59CF4B7DE8-L000416](../../agents/research.py#L416) | 416 | `"        pass"` | — |
| [SRC-59CF4B7DE8-L000417](../../agents/research.py#L417) | 417 | `"    for date_format in (\"%b %d, %Y\", \"%B %d, %Y\", \"%Y/%m/%d\", \"%d %b %Y\"):"` | — |
| [SRC-59CF4B7DE8-L000418](../../agents/research.py#L418) | 418 | `"        try:"` | — |
| [SRC-59CF4B7DE8-L000419](../../agents/research.py#L419) | 419 | `"            return datetime.strptime(raw, date_format).replace(tzinfo=UTC)"` | — |
| [SRC-59CF4B7DE8-L000420](../../agents/research.py#L420) | 420 | `"        except ValueError:"` | — |
| [SRC-59CF4B7DE8-L000421](../../agents/research.py#L421) | 421 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000422](../../agents/research.py#L422) | 422 | `"    match = re.search(r\"(\\d+)\\s+(hour\|day\|week\|month\|year)s?\\s+ago\", raw, re.IGNORECASE)"` | — |
| [SRC-59CF4B7DE8-L000423](../../agents/research.py#L423) | 423 | `"    if match:"` | — |
| [SRC-59CF4B7DE8-L000424](../../agents/research.py#L424) | 424 | `"        amount = int(match.group(1))"` | — |
| [SRC-59CF4B7DE8-L000425](../../agents/research.py#L425) | 425 | `"        unit = match.group(2).lower()"` | — |
| [SRC-59CF4B7DE8-L000426](../../agents/research.py#L426) | 426 | `"        durations = {"` | — |
| [SRC-59CF4B7DE8-L000427](../../agents/research.py#L427) | 427 | `"            \"hour\": timedelta(hours=amount),"` | — |
| [SRC-59CF4B7DE8-L000428](../../agents/research.py#L428) | 428 | `"            \"day\": timedelta(days=amount),"` | — |
| [SRC-59CF4B7DE8-L000429](../../agents/research.py#L429) | 429 | `"            \"week\": timedelta(days=7 * amount),"` | — |
| [SRC-59CF4B7DE8-L000430](../../agents/research.py#L430) | 430 | `"            \"month\": timedelta(days=30 * amount),"` | — |
| [SRC-59CF4B7DE8-L000431](../../agents/research.py#L431) | 431 | `"            \"year\": timedelta(days=365 * amount),"` | — |
| [SRC-59CF4B7DE8-L000432](../../agents/research.py#L432) | 432 | `"        }"` | — |
| [SRC-59CF4B7DE8-L000433](../../agents/research.py#L433) | 433 | `"        return current - durations[unit]"` | — |
| [SRC-59CF4B7DE8-L000434](../../agents/research.py#L434) | 434 | `"    if raw.lower() in {\"today\", \"just now\", \"now\"}:"` | — |
| [SRC-59CF4B7DE8-L000435](../../agents/research.py#L435) | 435 | `"        return current"` | — |
| [SRC-59CF4B7DE8-L000436](../../agents/research.py#L436) | 436 | `"    if raw.lower() == \"yesterday\":"` | — |
| [SRC-59CF4B7DE8-L000437](../../agents/research.py#L437) | 437 | `"        return current - timedelta(days=1)"` | — |
| [SRC-59CF4B7DE8-L000438](../../agents/research.py#L438) | 438 | `"    return None"` | — |
| [SRC-59CF4B7DE8-L000439](../../agents/research.py#L439) | 439 | `""` | — |
| [SRC-59CF4B7DE8-L000440](../../agents/research.py#L440) | 440 | `""` | — |
| [SRC-59CF4B7DE8-L000441](../../agents/research.py#L441) | 441 | `"def evidence_signal_report("` | — |
| [SRC-59CF4B7DE8-L000442](../../agents/research.py#L442) | 442 | `"    sources: list[dict[str, Any]],"` | — |
| [SRC-59CF4B7DE8-L000443](../../agents/research.py#L443) | 443 | `"    freshness: str = \"any\","` | — |
| [SRC-59CF4B7DE8-L000444](../../agents/research.py#L444) | 444 | `"    now: datetime \| None = None,"` | — |
| [SRC-59CF4B7DE8-L000445](../../agents/research.py#L445) | 445 | `") -> dict[str, Any]:"` | — |
| [SRC-59CF4B7DE8-L000446](../../agents/research.py#L446) | 446 | `"    \"\"\"Summarize research coverage; signals describe evidence coverage, not factual truth.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000447](../../agents/research.py#L447) | 447 | `"    current = now or datetime.now(UTC)"` | — |
| [SRC-59CF4B7DE8-L000448](../../agents/research.py#L448) | 448 | `"    valid_sources = [source for source in sources if isinstance(source, dict) and source.get(\"url\")]"` | — |
| [SRC-59CF4B7DE8-L000449](../../agents/research.py#L449) | 449 | `"    domains = {"` | — |
| [SRC-59CF4B7DE8-L000450](../../agents/research.py#L450) | 450 | `"        registrable_domain("` | — |
| [SRC-59CF4B7DE8-L000451](../../agents/research.py#L451) | 451 | `"            source.get(\"domain\") or urlparse(str(source.get(\"url\") or \"\")).hostname or \"\""` | — |
| [SRC-59CF4B7DE8-L000452](../../agents/research.py#L452) | 452 | `"        )"` | — |
| [SRC-59CF4B7DE8-L000453](../../agents/research.py#L453) | 453 | `"        for source in valid_sources"` | — |
| [SRC-59CF4B7DE8-L000454](../../agents/research.py#L454) | 454 | `"        if source.get(\"domain\") or source.get(\"url\")"` | — |
| [SRC-59CF4B7DE8-L000455](../../agents/research.py#L455) | 455 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000456](../../agents/research.py#L456) | 456 | `"    domains.discard(\"\")"` | — |
| [SRC-59CF4B7DE8-L000457](../../agents/research.py#L457) | 457 | `"    providers: set[str] = set()"` | — |
| [SRC-59CF4B7DE8-L000458](../../agents/research.py#L458) | 458 | `"    for source in valid_sources:"` | — |
| [SRC-59CF4B7DE8-L000459](../../agents/research.py#L459) | 459 | `"        candidate_providers = source.get(\"providers\", [])"` | — |
| [SRC-59CF4B7DE8-L000460](../../agents/research.py#L460) | 460 | `"        if isinstance(candidate_providers, list):"` | — |
| [SRC-59CF4B7DE8-L000461](../../agents/research.py#L461) | 461 | `"            providers.update(str(item) for item in candidate_providers if item)"` | — |
| [SRC-59CF4B7DE8-L000462](../../agents/research.py#L462) | 462 | `"        elif source.get(\"provider\"):"` | — |
| [SRC-59CF4B7DE8-L000463](../../agents/research.py#L463) | 463 | `"            providers.add(str(source[\"provider\"]))"` | — |
| [SRC-59CF4B7DE8-L000464](../../agents/research.py#L464) | 464 | `"    classes = [str(source.get(\"source_class\") or \"general\") for source in valid_sources]"` | — |
| [SRC-59CF4B7DE8-L000465](../../agents/research.py#L465) | 465 | `"    primary_count = sum(item in {\"government\", \"academic\", \"official\"} for item in classes)"` | — |
| [SRC-59CF4B7DE8-L000466](../../agents/research.py#L466) | 466 | `"    news_count = sum(item == \"news\" for item in classes)"` | — |
| [SRC-59CF4B7DE8-L000467](../../agents/research.py#L467) | 467 | `"    social_count = sum(item == \"social\" for item in classes)"` | — |
| [SRC-59CF4B7DE8-L000468](../../agents/research.py#L468) | 468 | `"    pages_read = sum(bool(source.get(\"page_fetched\")) for source in valid_sources)"` | — |
| [SRC-59CF4B7DE8-L000469](../../agents/research.py#L469) | 469 | `"    dates = ["` | — |
| [SRC-59CF4B7DE8-L000470](../../agents/research.py#L470) | 470 | `"        parsed"` | — |
| [SRC-59CF4B7DE8-L000471](../../agents/research.py#L471) | 471 | `"        for source in valid_sources"` | — |
| [SRC-59CF4B7DE8-L000472](../../agents/research.py#L472) | 472 | `"        if (parsed := _parse_publication_date(source.get(\"published_at\"), current)) is not None"` | — |
| [SRC-59CF4B7DE8-L000473](../../agents/research.py#L473) | 473 | `"    ]"` | — |
| [SRC-59CF4B7DE8-L000474](../../agents/research.py#L474) | 474 | `"    recent_days = 7 if freshness == \"current\" else 30"` | — |
| [SRC-59CF4B7DE8-L000475](../../agents/research.py#L475) | 475 | `"    recent_count = sum((current - parsed).total_seconds() >= 0 and"` | — |
| [SRC-59CF4B7DE8-L000476](../../agents/research.py#L476) | 476 | `"                       (current - parsed) <= timedelta(days=recent_days) for parsed in dates)"` | — |
| [SRC-59CF4B7DE8-L000477](../../agents/research.py#L477) | 477 | `"    future_dates = sum(parsed > current + timedelta(days=1) for parsed in dates)"` | — |
| [SRC-59CF4B7DE8-L000478](../../agents/research.py#L478) | 478 | `"    unique_sources = len(valid_sources)"` | — |
| [SRC-59CF4B7DE8-L000479](../../agents/research.py#L479) | 479 | `"    # Evidence coverage uses several independent dimensions and is deliberately not a"` | — |
| [SRC-59CF4B7DE8-L000480](../../agents/research.py#L480) | 480 | `"    # probability that any factual claim is true."` | — |
| [SRC-59CF4B7DE8-L000481](../../agents/research.py#L481) | 481 | `"    coverage_points = 0"` | — |
| [SRC-59CF4B7DE8-L000482](../../agents/research.py#L482) | 482 | `"    coverage_points += min(unique_sources, 10) * 3"` | — |
| [SRC-59CF4B7DE8-L000483](../../agents/research.py#L483) | 483 | `"    coverage_points += min(len(domains), 8) * 4"` | — |
| [SRC-59CF4B7DE8-L000484](../../agents/research.py#L484) | 484 | `"    coverage_points += min(len(providers), 4) * 5"` | — |
| [SRC-59CF4B7DE8-L000485](../../agents/research.py#L485) | 485 | `"    coverage_points += min(pages_read, 8) * 3"` | — |
| [SRC-59CF4B7DE8-L000486](../../agents/research.py#L486) | 486 | `"    coverage_points += min(primary_count, 4) * 4"` | — |
| [SRC-59CF4B7DE8-L000487](../../agents/research.py#L487) | 487 | `"    coverage_points += min(len(dates), 8) * 2"` | — |
| [SRC-59CF4B7DE8-L000488](../../agents/research.py#L488) | 488 | `"    coverage_score = min(100, coverage_points)"` | — |
| [SRC-59CF4B7DE8-L000489](../../agents/research.py#L489) | 489 | `"    if unique_sources >= 8 and len(domains) >= 5 and len(providers) >= 2 and pages_read >= 3:"` | — |
| [SRC-59CF4B7DE8-L000490](../../agents/research.py#L490) | 490 | `"        coverage_level = \"متعدد المصادر\""` | — |
| [SRC-59CF4B7DE8-L000491](../../agents/research.py#L491) | 491 | `"    elif unique_sources >= 4 and len(domains) >= 3 and len(providers) >= 1:"` | — |
| [SRC-59CF4B7DE8-L000492](../../agents/research.py#L492) | 492 | `"        coverage_level = \"متوسط\""` | — |
| [SRC-59CF4B7DE8-L000493](../../agents/research.py#L493) | 493 | `"    else:"` | — |
| [SRC-59CF4B7DE8-L000494](../../agents/research.py#L494) | 494 | `"        coverage_level = \"محدود\""` | — |
| [SRC-59CF4B7DE8-L000495](../../agents/research.py#L495) | 495 | `""` | — |
| [SRC-59CF4B7DE8-L000496](../../agents/research.py#L496) | 496 | `"    warnings: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000497](../../agents/research.py#L497) | 497 | `"    if unique_sources == 0:"` | — |
| [SRC-59CF4B7DE8-L000498](../../agents/research.py#L498) | 498 | `"        warnings.append(\"لا توجد مصادر قابلة للاستشهاد؛ لا تستنتج حقائق من عدم وجود نتائج.\")"` | — |
| [SRC-59CF4B7DE8-L000499](../../agents/research.py#L499) | 499 | `"    if len(domains) < 3:"` | — |
| [SRC-59CF4B7DE8-L000500](../../agents/research.py#L500) | 500 | `"        warnings.append(\"تنوع النطاقات محدود؛ لا تعتبر تكرار النتيجة تأكيدًا مستقلًا.\")"` | — |
| [SRC-59CF4B7DE8-L000501](../../agents/research.py#L501) | 501 | `"    if pages_read < 2 and unique_sources:"` | — |
| [SRC-59CF4B7DE8-L000502](../../agents/research.py#L502) | 502 | `"        warnings.append(\"تمت قراءة أقل من صفحتين مباشرة؛ بعض الأدلة مقتطفات من محركات البحث فقط.\")"` | — |
| [SRC-59CF4B7DE8-L000503](../../agents/research.py#L503) | 503 | `"    if freshness == \"current\":"` | — |
| [SRC-59CF4B7DE8-L000504](../../agents/research.py#L504) | 504 | `"        if not dates:"` | — |
| [SRC-59CF4B7DE8-L000505](../../agents/research.py#L505) | 505 | `"            warnings.append(\"لا تتوفر تواريخ نشر قابلة للتحليل؛ حداثة النتائج غير مؤكدة.\")"` | — |
| [SRC-59CF4B7DE8-L000506](../../agents/research.py#L506) | 506 | `"        elif recent_count == 0:"` | — |
| [SRC-59CF4B7DE8-L000507](../../agents/research.py#L507) | 507 | `"            warnings.append(f\"لم يُعثر على مصدر مؤرخ خلال آخر {recent_days} يومًا ضمن التواريخ القابلة للتحليل.\")"` | — |
| [SRC-59CF4B7DE8-L000508](../../agents/research.py#L508) | 508 | `"    if future_dates:"` | — |
| [SRC-59CF4B7DE8-L000509](../../agents/research.py#L509) | 509 | `"        warnings.append(\"توجد تواريخ مستقبلية غير متوقعة؛ يجب مراجعتها يدويًا.\")"` | — |
| [SRC-59CF4B7DE8-L000510](../../agents/research.py#L510) | 510 | `"    if social_count and primary_count == 0:"` | — |
| [SRC-59CF4B7DE8-L000511](../../agents/research.py#L511) | 511 | `"        warnings.append(\"المصادر اجتماعية فقط دون مصدر رسمي/أكاديمي؛ تعامل معها كآراء أو إشارات لا كحقائق مثبتة.\")"` | — |
| [SRC-59CF4B7DE8-L000512](../../agents/research.py#L512) | 512 | `"    return {"` | — |
| [SRC-59CF4B7DE8-L000513](../../agents/research.py#L513) | 513 | `"        \"unique_sources\": unique_sources,"` | — |
| [SRC-59CF4B7DE8-L000514](../../agents/research.py#L514) | 514 | `"        \"unique_domains\": len(domains),"` | — |
| [SRC-59CF4B7DE8-L000515](../../agents/research.py#L515) | 515 | `"        \"providers_count\": len(providers),"` | — |
| [SRC-59CF4B7DE8-L000516](../../agents/research.py#L516) | 516 | `"        \"providers\": sorted(providers),"` | — |
| [SRC-59CF4B7DE8-L000517](../../agents/research.py#L517) | 517 | `"        \"pages_read\": pages_read,"` | — |
| [SRC-59CF4B7DE8-L000518](../../agents/research.py#L518) | 518 | `"        \"primary_sources\": primary_count,"` | — |
| [SRC-59CF4B7DE8-L000519](../../agents/research.py#L519) | 519 | `"        \"news_sources\": news_count,"` | — |
| [SRC-59CF4B7DE8-L000520](../../agents/research.py#L520) | 520 | `"        \"social_sources\": social_count,"` | — |
| [SRC-59CF4B7DE8-L000521](../../agents/research.py#L521) | 521 | `"        \"dated_sources\": len(dates),"` | — |
| [SRC-59CF4B7DE8-L000522](../../agents/research.py#L522) | 522 | `"        \"recent_sources\": recent_count,"` | — |
| [SRC-59CF4B7DE8-L000523](../../agents/research.py#L523) | 523 | `"        \"undated_sources\": max(0, unique_sources - len(dates)),"` | — |
| [SRC-59CF4B7DE8-L000524](../../agents/research.py#L524) | 524 | `"        \"date_coverage_percent\": round(100 * len(dates) / unique_sources) if unique_sources else 0,"` | — |
| [SRC-59CF4B7DE8-L000525](../../agents/research.py#L525) | 525 | `"        \"coverage_score\": coverage_score,"` | — |
| [SRC-59CF4B7DE8-L000526](../../agents/research.py#L526) | 526 | `"        \"coverage_level\": coverage_level,"` | — |
| [SRC-59CF4B7DE8-L000527](../../agents/research.py#L527) | 527 | `"        \"score_meaning\": \"مؤشر تغطية وتنوع الأدلة، وليس احتمال صحة الإجابة.\","` | — |
| [SRC-59CF4B7DE8-L000528](../../agents/research.py#L528) | 528 | `"        \"warnings\": warnings,"` | — |
| [SRC-59CF4B7DE8-L000529](../../agents/research.py#L529) | 529 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000530](../../agents/research.py#L530) | 530 | `""` | — |
| [SRC-59CF4B7DE8-L000531](../../agents/research.py#L531) | 531 | `""` | — |
| [SRC-59CF4B7DE8-L000532](../../agents/research.py#L532) | 532 | `""` | — |
