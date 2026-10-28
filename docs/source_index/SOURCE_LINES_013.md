# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **013**
- سجلات الأسطر: **800**
- النطاق: SRC-EEF2E6447C-L000020 إلى SRC-792A9A235D-L000036
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## واجهات API

### FILE-EEF2E6447C — [api/omarai.py](../../api/omarai.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-EEF2E6447C-L000020](../../api/omarai.py#L20) | 20 | `"from agents.omarai import LeadStore, analyze, normalize"` | — |
| [SRC-EEF2E6447C-L000021](../../api/omarai.py#L21) | 21 | `"from agents.web_agent import WebAgent"` | — |
| [SRC-EEF2E6447C-L000022](../../api/omarai.py#L22) | 22 | `""` | — |
| [SRC-EEF2E6447C-L000023](../../api/omarai.py#L23) | 23 | `"ROOT = Path(__file__).resolve().parents[1] / \"web\""` | — |
| [SRC-EEF2E6447C-L000024](../../api/omarai.py#L24) | 24 | `"AGENT_DASHBOARD = ROOT / \"agent.html\""` | — |
| [SRC-EEF2E6447C-L000025](../../api/omarai.py#L25) | 25 | `"LEADS_DASHBOARD = ROOT / \"dashboard.html\""` | — |
| [SRC-EEF2E6447C-L000026](../../api/omarai.py#L26) | 26 | `"MAX_REQUEST_BODY_BYTES = 200_000"` | — |
| [SRC-EEF2E6447C-L000027](../../api/omarai.py#L27) | 27 | `""` | — |
| [SRC-EEF2E6447C-L000028](../../api/omarai.py#L28) | 28 | `""` | — |
| [SRC-EEF2E6447C-L000029](../../api/omarai.py#L29) | 29 | `"def _csp_hash_source(value: str) -> str:"` | — |
| [SRC-EEF2E6447C-L000030](../../api/omarai.py#L30) | 30 | `"    digest = base64.b64encode(hashlib.sha256(value.encode(\"utf-8\")).digest()).decode(\"ascii\")"` | — |
| [SRC-EEF2E6447C-L000031](../../api/omarai.py#L31) | 31 | `"    return f\"'sha256-{digest}'\""` | — |
| [SRC-EEF2E6447C-L000032](../../api/omarai.py#L32) | 32 | `""` | — |
| [SRC-EEF2E6447C-L000033](../../api/omarai.py#L33) | 33 | `""` | — |
| [SRC-EEF2E6447C-L000034](../../api/omarai.py#L34) | 34 | `"@lru_cache(maxsize=1)"` | — |
| [SRC-EEF2E6447C-L000035](../../api/omarai.py#L35) | 35 | `"def _content_security_policy() -> str:"` | — |
| [SRC-EEF2E6447C-L000036](../../api/omarai.py#L36) | 36 | `"    \"\"\"Allow only known inline blocks/attributes from the static first-party HTML."` | — |
| [SRC-EEF2E6447C-L000037](../../api/omarai.py#L37) | 37 | `""` | — |
| [SRC-EEF2E6447C-L000038](../../api/omarai.py#L38) | 38 | `"    Hashes deliberately replace unsafe-inline. Updating an inline script/style means its"` | — |
| [SRC-EEF2E6447C-L000039](../../api/omarai.py#L39) | 39 | `"    hash changes automatically with the served source. This is not a sanitizer for"` | — |
| [SRC-EEF2E6447C-L000040](../../api/omarai.py#L40) | 40 | `"    untrusted HTML; callers must never splice untrusted input into these static files."` | — |
| [SRC-EEF2E6447C-L000041](../../api/omarai.py#L41) | 41 | `"    \"\"\""` | — |
| [SRC-EEF2E6447C-L000042](../../api/omarai.py#L42) | 42 | `"    script_hashes: set[str] = set()"` | — |
| [SRC-EEF2E6447C-L000043](../../api/omarai.py#L43) | 43 | `"    style_hashes: set[str] = set()"` | — |
| [SRC-EEF2E6447C-L000044](../../api/omarai.py#L44) | 44 | `"    event_handler_hashes: set[str] = set()"` | — |
| [SRC-EEF2E6447C-L000045](../../api/omarai.py#L45) | 45 | `"    style_attribute_hashes: set[str] = set()"` | — |
| [SRC-EEF2E6447C-L000046](../../api/omarai.py#L46) | 46 | `""` | — |
| [SRC-EEF2E6447C-L000047](../../api/omarai.py#L47) | 47 | `"    for html_path in sorted(ROOT.glob(\"*.html\")):"` | — |
| [SRC-EEF2E6447C-L000048](../../api/omarai.py#L48) | 48 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000049](../../api/omarai.py#L49) | 49 | `"            document = html_path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-EEF2E6447C-L000050](../../api/omarai.py#L50) | 50 | `"        except (OSError, UnicodeError):"` | — |
| [SRC-EEF2E6447C-L000051](../../api/omarai.py#L51) | 51 | `"            continue"` | — |
| [SRC-EEF2E6447C-L000052](../../api/omarai.py#L52) | 52 | `""` | — |
| [SRC-EEF2E6447C-L000053](../../api/omarai.py#L53) | 53 | `"        for match in re.finditer("` | — |
| [SRC-EEF2E6447C-L000054](../../api/omarai.py#L54) | 54 | `"            r\"<script\\b(?P<attrs>[^>]*)>(?P<body>.*?)</script\\s*>\","` | — |
| [SRC-EEF2E6447C-L000055](../../api/omarai.py#L55) | 55 | `"            document,"` | — |
| [SRC-EEF2E6447C-L000056](../../api/omarai.py#L56) | 56 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-EEF2E6447C-L000057](../../api/omarai.py#L57) | 57 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000058](../../api/omarai.py#L58) | 58 | `"            if re.search(r\"\\bsrc\\s*=\", match.group(\"attrs\"), re.IGNORECASE):"` | — |
| [SRC-EEF2E6447C-L000059](../../api/omarai.py#L59) | 59 | `"                continue"` | — |
| [SRC-EEF2E6447C-L000060](../../api/omarai.py#L60) | 60 | `"            script_hashes.add(_csp_hash_source(match.group(\"body\")))"` | — |
| [SRC-EEF2E6447C-L000061](../../api/omarai.py#L61) | 61 | `""` | — |
| [SRC-EEF2E6447C-L000062](../../api/omarai.py#L62) | 62 | `"        for match in re.finditer("` | — |
| [SRC-EEF2E6447C-L000063](../../api/omarai.py#L63) | 63 | `"            r\"<style\\b[^>]*>(?P<body>.*?)</style\\s*>\","` | — |
| [SRC-EEF2E6447C-L000064](../../api/omarai.py#L64) | 64 | `"            document,"` | — |
| [SRC-EEF2E6447C-L000065](../../api/omarai.py#L65) | 65 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-EEF2E6447C-L000066](../../api/omarai.py#L66) | 66 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000067](../../api/omarai.py#L67) | 67 | `"            style_hashes.add(_csp_hash_source(match.group(\"body\")))"` | — |
| [SRC-EEF2E6447C-L000068](../../api/omarai.py#L68) | 68 | `""` | — |
| [SRC-EEF2E6447C-L000069](../../api/omarai.py#L69) | 69 | `"        # This scan intentionally includes style/event attributes embedded in"` | — |
| [SRC-EEF2E6447C-L000070](../../api/omarai.py#L70) | 70 | `"        # trusted first-party HTML templates assembled by inline scripts."` | — |
| [SRC-EEF2E6447C-L000071](../../api/omarai.py#L71) | 71 | `"        for match in re.finditer("` | — |
| [SRC-EEF2E6447C-L000072](../../api/omarai.py#L72) | 72 | `"            r\"\"\"\\bstyle\\s*=\\s*([\"'])(.*?)\\1\"\"\","` | — |
| [SRC-EEF2E6447C-L000073](../../api/omarai.py#L73) | 73 | `"            document,"` | — |
| [SRC-EEF2E6447C-L000074](../../api/omarai.py#L74) | 74 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-EEF2E6447C-L000075](../../api/omarai.py#L75) | 75 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000076](../../api/omarai.py#L76) | 76 | `"            style_attribute_hashes.add(_csp_hash_source(match.group(2).strip()))"` | — |
| [SRC-EEF2E6447C-L000077](../../api/omarai.py#L77) | 77 | `""` | — |
| [SRC-EEF2E6447C-L000078](../../api/omarai.py#L78) | 78 | `"        for match in re.finditer("` | — |
| [SRC-EEF2E6447C-L000079](../../api/omarai.py#L79) | 79 | `"            r\"\"\"\\bon[a-z]+\\s*=\\s*([\"'])(.*?)\\1\"\"\","` | — |
| [SRC-EEF2E6447C-L000080](../../api/omarai.py#L80) | 80 | `"            document,"` | — |
| [SRC-EEF2E6447C-L000081](../../api/omarai.py#L81) | 81 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-EEF2E6447C-L000082](../../api/omarai.py#L82) | 82 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000083](../../api/omarai.py#L83) | 83 | `"            event_handler_hashes.add(_csp_hash_source(match.group(2).strip()))"` | — |
| [SRC-EEF2E6447C-L000084](../../api/omarai.py#L84) | 84 | `""` | — |
| [SRC-EEF2E6447C-L000085](../../api/omarai.py#L85) | 85 | `"    script_sources = [\"'self'\", *sorted(script_hashes)]"` | — |
| [SRC-EEF2E6447C-L000086](../../api/omarai.py#L86) | 86 | `"    style_sources = [\"'self'\", *sorted(style_hashes)]"` | — |
| [SRC-EEF2E6447C-L000087](../../api/omarai.py#L87) | 87 | `"    if event_handler_hashes:"` | — |
| [SRC-EEF2E6447C-L000088](../../api/omarai.py#L88) | 88 | `"        script_sources.extend([\"'unsafe-hashes'\", *sorted(event_handler_hashes)])"` | — |
| [SRC-EEF2E6447C-L000089](../../api/omarai.py#L89) | 89 | `"    if style_attribute_hashes:"` | — |
| [SRC-EEF2E6447C-L000090](../../api/omarai.py#L90) | 90 | `"        style_sources.extend([\"'unsafe-hashes'\", *sorted(style_attribute_hashes)])"` | — |
| [SRC-EEF2E6447C-L000091](../../api/omarai.py#L91) | 91 | `""` | — |
| [SRC-EEF2E6447C-L000092](../../api/omarai.py#L92) | 92 | `"    return ("` | — |
| [SRC-EEF2E6447C-L000093](../../api/omarai.py#L93) | 93 | `"        \"default-src 'self'; base-uri 'self'; object-src 'none'; frame-ancestors 'none'; \""` | — |
| [SRC-EEF2E6447C-L000094](../../api/omarai.py#L94) | 94 | `"        \"form-action 'self'; connect-src 'self'; img-src 'self' data:; \""` | — |
| [SRC-EEF2E6447C-L000095](../../api/omarai.py#L95) | 95 | `"        f\"script-src {' '.join(script_sources)}; \""` | — |
| [SRC-EEF2E6447C-L000096](../../api/omarai.py#L96) | 96 | `"        f\"style-src {' '.join(style_sources)}; font-src 'self' data:\""` | — |
| [SRC-EEF2E6447C-L000097](../../api/omarai.py#L97) | 97 | `"    )"` | — |
| [SRC-EEF2E6447C-L000098](../../api/omarai.py#L98) | 98 | `"# Bound request-line + header parsing before application code or body processing."` | — |
| [SRC-EEF2E6447C-L000099](../../api/omarai.py#L99) | 99 | `"REQUEST_HEADER_READ_TIMEOUT_SECONDS = 8.0"` | — |
| [SRC-EEF2E6447C-L000100](../../api/omarai.py#L100) | 100 | `"REQUEST_HEADER_IDLE_TIMEOUT_SECONDS = 2.0"` | — |
| [SRC-EEF2E6447C-L000101](../../api/omarai.py#L101) | 101 | `"MAX_REQUEST_HEADER_READ_TIMEOUT_SECONDS = 15.0"` | — |
| [SRC-EEF2E6447C-L000102](../../api/omarai.py#L102) | 102 | `"# Absolute deadline for reading the entire body, not merely a per-read idle timeout."` | — |
| [SRC-EEF2E6447C-L000103](../../api/omarai.py#L103) | 103 | `"REQUEST_BODY_READ_TIMEOUT_SECONDS = 10.0"` | — |
| [SRC-EEF2E6447C-L000104](../../api/omarai.py#L104) | 104 | `"REQUEST_BODY_IDLE_TIMEOUT_SECONDS = 2.0"` | — |
| [SRC-EEF2E6447C-L000105](../../api/omarai.py#L105) | 105 | `"MAX_REQUEST_BODY_READ_TIMEOUT_SECONDS = 30.0"` | — |
| [SRC-EEF2E6447C-L000106](../../api/omarai.py#L106) | 106 | `"REQUEST_BODY_READ_CHUNK_BYTES = 8_192"` | — |
| [SRC-EEF2E6447C-L000107](../../api/omarai.py#L107) | 107 | `""` | — |
| [SRC-EEF2E6447C-L000108](../../api/omarai.py#L108) | 108 | `""` | — |
| [SRC-EEF2E6447C-L000109](../../api/omarai.py#L109) | 109 | `""` | — |
| [SRC-EEF2E6447C-L000110](../../api/omarai.py#L110) | 110 | `"def _lead_store_from_environment() -> LeadStore:"` | — |
| [SRC-EEF2E6447C-L000111](../../api/omarai.py#L111) | 111 | `"    \"\"\"Use an operator-configured database path when a persistent volume is available.\"\"\""` | — |
| [SRC-EEF2E6447C-L000112](../../api/omarai.py#L112) | 112 | `"    configured_path = os.getenv(\"OMARAI_DB_PATH\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000113](../../api/omarai.py#L113) | 113 | `"    return LeadStore(configured_path or None)"` | — |
| [SRC-EEF2E6447C-L000114](../../api/omarai.py#L114) | 114 | `""` | — |
| [SRC-EEF2E6447C-L000115](../../api/omarai.py#L115) | 115 | `""` | — |
| [SRC-EEF2E6447C-L000116](../../api/omarai.py#L116) | 116 | `"class _DeadlineRequestReader:"` | — |
| [SRC-EEF2E6447C-L000117](../../api/omarai.py#L117) | 117 | `"    \"\"\"Read HTTP header lines with one absolute deadline across all fragments."` | — |
| [SRC-EEF2E6447C-L000118](../../api/omarai.py#L118) | 118 | `""` | — |
| [SRC-EEF2E6447C-L000119](../../api/omarai.py#L119) | 119 | `"    The standard buffered readline can wait indefinitely for a newline if a"` | — |
| [SRC-EEF2E6447C-L000120](../../api/omarai.py#L120) | 120 | `"    client keeps trickling bytes. This reader checks the same deadline before"` | — |
| [SRC-EEF2E6447C-L000121](../../api/omarai.py#L121) | 121 | `"    every socket read and buffers only bounded look-ahead so request body bytes"` | — |
| [SRC-EEF2E6447C-L000122](../../api/omarai.py#L122) | 122 | `"    received with the headers are preserved for read1()."` | — |
| [SRC-EEF2E6447C-L000123](../../api/omarai.py#L123) | 123 | `"    \"\"\""` | — |
| [SRC-EEF2E6447C-L000124](../../api/omarai.py#L124) | 124 | `""` | — |
| [SRC-EEF2E6447C-L000125](../../api/omarai.py#L125) | 125 | `"    def __init__(self, connection, handler):"` | — |
| [SRC-EEF2E6447C-L000126](../../api/omarai.py#L126) | 126 | `"        self.connection = connection"` | — |
| [SRC-EEF2E6447C-L000127](../../api/omarai.py#L127) | 127 | `"        self.handler = handler"` | — |
| [SRC-EEF2E6447C-L000128](../../api/omarai.py#L128) | 128 | `"        self._buffer = bytearray()"` | — |
| [SRC-EEF2E6447C-L000129](../../api/omarai.py#L129) | 129 | `""` | — |
| [SRC-EEF2E6447C-L000130](../../api/omarai.py#L130) | 130 | `"    def readline(self, limit=-1):"` | — |
| [SRC-EEF2E6447C-L000131](../../api/omarai.py#L131) | 131 | `"        if limit == 0:"` | — |
| [SRC-EEF2E6447C-L000132](../../api/omarai.py#L132) | 132 | `"            return b\"\""` | — |
| [SRC-EEF2E6447C-L000133](../../api/omarai.py#L133) | 133 | `"        max_bytes = int(limit) if limit is not None and limit > 0 else 65_537"` | — |
| [SRC-EEF2E6447C-L000134](../../api/omarai.py#L134) | 134 | `"        previous_timeout = self.connection.gettimeout()"` | — |
| [SRC-EEF2E6447C-L000135](../../api/omarai.py#L135) | 135 | `"        line = bytearray()"` | — |
| [SRC-EEF2E6447C-L000136](../../api/omarai.py#L136) | 136 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000137](../../api/omarai.py#L137) | 137 | `"            while len(line) < max_bytes:"` | — |
| [SRC-EEF2E6447C-L000138](../../api/omarai.py#L138) | 138 | `"                deadline = getattr(self.handler, \"_request_header_deadline\", None)"` | — |
| [SRC-EEF2E6447C-L000139](../../api/omarai.py#L139) | 139 | `"                if deadline is None:"` | — |
| [SRC-EEF2E6447C-L000140](../../api/omarai.py#L140) | 140 | `"                    raise TimeoutError(\"request-header deadline is not active\")"` | — |
| [SRC-EEF2E6447C-L000141](../../api/omarai.py#L141) | 141 | `"                remaining = deadline - time.monotonic()"` | — |
| [SRC-EEF2E6447C-L000142](../../api/omarai.py#L142) | 142 | `"                if remaining <= 0:"` | — |
| [SRC-EEF2E6447C-L000143](../../api/omarai.py#L143) | 143 | `"                    raise TimeoutError(\"absolute request-header deadline exceeded\")"` | — |
| [SRC-EEF2E6447C-L000144](../../api/omarai.py#L144) | 144 | `""` | — |
| [SRC-EEF2E6447C-L000145](../../api/omarai.py#L145) | 145 | `"                newline_index = self._buffer.find(b\"\\n\")"` | — |
| [SRC-EEF2E6447C-L000146](../../api/omarai.py#L146) | 146 | `"                if newline_index >= 0:"` | — |
| [SRC-EEF2E6447C-L000147](../../api/omarai.py#L147) | 147 | `"                    take = min(newline_index + 1, max_bytes - len(line))"` | — |
| [SRC-EEF2E6447C-L000148](../../api/omarai.py#L148) | 148 | `"                    line.extend(self._buffer[:take])"` | — |
| [SRC-EEF2E6447C-L000149](../../api/omarai.py#L149) | 149 | `"                    del self._buffer[:take]"` | — |
| [SRC-EEF2E6447C-L000150](../../api/omarai.py#L150) | 150 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000151](../../api/omarai.py#L151) | 151 | `""` | — |
| [SRC-EEF2E6447C-L000152](../../api/omarai.py#L152) | 152 | `"                if self._buffer:"` | — |
| [SRC-EEF2E6447C-L000153](../../api/omarai.py#L153) | 153 | `"                    take = min(len(self._buffer), max_bytes - len(line))"` | — |
| [SRC-EEF2E6447C-L000154](../../api/omarai.py#L154) | 154 | `"                    line.extend(self._buffer[:take])"` | — |
| [SRC-EEF2E6447C-L000155](../../api/omarai.py#L155) | 155 | `"                    del self._buffer[:take]"` | — |
| [SRC-EEF2E6447C-L000156](../../api/omarai.py#L156) | 156 | `"                    if len(line) >= max_bytes:"` | — |
| [SRC-EEF2E6447C-L000157](../../api/omarai.py#L157) | 157 | `"                        break"` | — |
| [SRC-EEF2E6447C-L000158](../../api/omarai.py#L158) | 158 | `""` | — |
| [SRC-EEF2E6447C-L000159](../../api/omarai.py#L159) | 159 | `"                remaining = deadline - time.monotonic()"` | — |
| [SRC-EEF2E6447C-L000160](../../api/omarai.py#L160) | 160 | `"                if remaining <= 0:"` | — |
| [SRC-EEF2E6447C-L000161](../../api/omarai.py#L161) | 161 | `"                    raise TimeoutError(\"absolute request-header deadline exceeded\")"` | — |
| [SRC-EEF2E6447C-L000162](../../api/omarai.py#L162) | 162 | `"                idle_timeout = max("` | — |
| [SRC-EEF2E6447C-L000163](../../api/omarai.py#L163) | 163 | `"                    0.1,"` | — |
| [SRC-EEF2E6447C-L000164](../../api/omarai.py#L164) | 164 | `"                    min("` | — |
| [SRC-EEF2E6447C-L000165](../../api/omarai.py#L165) | 165 | `"                        float(REQUEST_HEADER_IDLE_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000166](../../api/omarai.py#L166) | 166 | `"                        MAX_REQUEST_HEADER_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000167](../../api/omarai.py#L167) | 167 | `"                    ),"` | — |
| [SRC-EEF2E6447C-L000168](../../api/omarai.py#L168) | 168 | `"                )"` | — |
| [SRC-EEF2E6447C-L000169](../../api/omarai.py#L169) | 169 | `"                self.connection.settimeout(min(idle_timeout, remaining))"` | — |
| [SRC-EEF2E6447C-L000170](../../api/omarai.py#L170) | 170 | `"                chunk = self.connection.recv(min(4_096, max_bytes - len(line)))"` | — |
| [SRC-EEF2E6447C-L000171](../../api/omarai.py#L171) | 171 | `"                if not chunk:"` | — |
| [SRC-EEF2E6447C-L000172](../../api/omarai.py#L172) | 172 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000173](../../api/omarai.py#L173) | 173 | `"                self._buffer.extend(chunk)"` | — |
| [SRC-EEF2E6447C-L000174](../../api/omarai.py#L174) | 174 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000175](../../api/omarai.py#L175) | 175 | `"            try:"` | — |
| [SRC-EEF2E6447C-L000176](../../api/omarai.py#L176) | 176 | `"                self.connection.settimeout(previous_timeout)"` | — |
| [SRC-EEF2E6447C-L000177](../../api/omarai.py#L177) | 177 | `"            except OSError:"` | — |
| [SRC-EEF2E6447C-L000178](../../api/omarai.py#L178) | 178 | `"                pass"` | — |
| [SRC-EEF2E6447C-L000179](../../api/omarai.py#L179) | 179 | `"        return bytes(line)"` | — |
| [SRC-EEF2E6447C-L000180](../../api/omarai.py#L180) | 180 | `""` | — |
| [SRC-EEF2E6447C-L000181](../../api/omarai.py#L181) | 181 | `"    def read1(self, size=-1):"` | — |
| [SRC-EEF2E6447C-L000182](../../api/omarai.py#L182) | 182 | `"        \"\"\"Read one chunk; body code applies its own idle and absolute deadlines.\"\"\""` | — |
| [SRC-EEF2E6447C-L000183](../../api/omarai.py#L183) | 183 | `"        if size == 0:"` | — |
| [SRC-EEF2E6447C-L000184](../../api/omarai.py#L184) | 184 | `"            return b\"\""` | — |
| [SRC-EEF2E6447C-L000185](../../api/omarai.py#L185) | 185 | `"        if size is None or size < 0:"` | — |
| [SRC-EEF2E6447C-L000186](../../api/omarai.py#L186) | 186 | `"            size = 8_192"` | — |
| [SRC-EEF2E6447C-L000187](../../api/omarai.py#L187) | 187 | `"        if self._buffer:"` | — |
| [SRC-EEF2E6447C-L000188](../../api/omarai.py#L188) | 188 | `"            take = min(len(self._buffer), size)"` | — |
| [SRC-EEF2E6447C-L000189](../../api/omarai.py#L189) | 189 | `"            data = bytes(self._buffer[:take])"` | — |
| [SRC-EEF2E6447C-L000190](../../api/omarai.py#L190) | 190 | `"            del self._buffer[:take]"` | — |
| [SRC-EEF2E6447C-L000191](../../api/omarai.py#L191) | 191 | `"            return data"` | — |
| [SRC-EEF2E6447C-L000192](../../api/omarai.py#L192) | 192 | `"        return self.connection.recv(size)"` | — |
| [SRC-EEF2E6447C-L000193](../../api/omarai.py#L193) | 193 | `""` | — |
| [SRC-EEF2E6447C-L000194](../../api/omarai.py#L194) | 194 | `"    def close(self):"` | — |
| [SRC-EEF2E6447C-L000195](../../api/omarai.py#L195) | 195 | `"        # The request handler owns the socket and closes its output stream."` | — |
| [SRC-EEF2E6447C-L000196](../../api/omarai.py#L196) | 196 | `"        return None"` | — |
| [SRC-EEF2E6447C-L000197](../../api/omarai.py#L197) | 197 | `""` | — |
| [SRC-EEF2E6447C-L000198](../../api/omarai.py#L198) | 198 | `""` | — |
| [SRC-EEF2E6447C-L000199](../../api/omarai.py#L199) | 199 | `"def _configured_agent_concurrency_limit() -> int:"` | — |
| [SRC-EEF2E6447C-L000200](../../api/omarai.py#L200) | 200 | `"    \"\"\"Return a process-local cap for expensive research and diagnostics operations.\"\"\""` | — |
| [SRC-EEF2E6447C-L000201](../../api/omarai.py#L201) | 201 | `"    try:"` | — |
| [SRC-EEF2E6447C-L000202](../../api/omarai.py#L202) | 202 | `"        configured = int(os.getenv(\"OMARAI_MAX_CONCURRENT_AGENT_REQUESTS\", \"4\").strip())"` | — |
| [SRC-EEF2E6447C-L000203](../../api/omarai.py#L203) | 203 | `"    except ValueError:"` | — |
| [SRC-EEF2E6447C-L000204](../../api/omarai.py#L204) | 204 | `"        configured = 4"` | — |
| [SRC-EEF2E6447C-L000205](../../api/omarai.py#L205) | 205 | `"    return max(1, min(configured, 8))"` | — |
| [SRC-EEF2E6447C-L000206](../../api/omarai.py#L206) | 206 | `""` | — |
| [SRC-EEF2E6447C-L000207](../../api/omarai.py#L207) | 207 | `""` | — |
| [SRC-EEF2E6447C-L000208](../../api/omarai.py#L208) | 208 | `"BUILD_SHA_FILE = Path(__file__).resolve().parents[1] / \"BUILD_SHA\""` | — |
| [SRC-EEF2E6447C-L000209](../../api/omarai.py#L209) | 209 | `"_PLATFORM_BUILD_SHA_ENVIRONMENTS = ("` | — |
| [SRC-EEF2E6447C-L000210](../../api/omarai.py#L210) | 210 | `"    (\"RAILWAY_GIT_COMMIT_SHA\", \"platform:railway\"),"` | — |
| [SRC-EEF2E6447C-L000211](../../api/omarai.py#L211) | 211 | `"    (\"RENDER_GIT_COMMIT\", \"platform:render\"),"` | — |
| [SRC-EEF2E6447C-L000212](../../api/omarai.py#L212) | 212 | `")"` | — |
| [SRC-EEF2E6447C-L000213](../../api/omarai.py#L213) | 213 | `""` | — |
| [SRC-EEF2E6447C-L000214](../../api/omarai.py#L214) | 214 | `""` | — |
| [SRC-EEF2E6447C-L000215](../../api/omarai.py#L215) | 215 | `"def _valid_build_sha(value: str) -> bool:"` | — |
| [SRC-EEF2E6447C-L000216](../../api/omarai.py#L216) | 216 | `"    candidate = value.strip().lower()"` | — |
| [SRC-EEF2E6447C-L000217](../../api/omarai.py#L217) | 217 | `"    return len(candidate) == 40 and all(char in \"0123456789abcdef\" for char in candidate)"` | — |
| [SRC-EEF2E6447C-L000218](../../api/omarai.py#L218) | 218 | `""` | — |
| [SRC-EEF2E6447C-L000219](../../api/omarai.py#L219) | 219 | `""` | — |
| [SRC-EEF2E6447C-L000220](../../api/omarai.py#L220) | 220 | `"def _build_identity() -> tuple[str, str]:"` | — |
| [SRC-EEF2E6447C-L000221](../../api/omarai.py#L221) | 221 | `"    \"\"\"Prefer immutable image metadata, then documented hosting-provided Git SHAs.\"\"\""` | — |
| [SRC-EEF2E6447C-L000222](../../api/omarai.py#L222) | 222 | `"    try:"` | — |
| [SRC-EEF2E6447C-L000223](../../api/omarai.py#L223) | 223 | `"        baked = BUILD_SHA_FILE.read_text(encoding=\"ascii\").strip().lower()"` | — |
| [SRC-EEF2E6447C-L000224](../../api/omarai.py#L224) | 224 | `"    except (OSError, UnicodeError):"` | — |
| [SRC-EEF2E6447C-L000225](../../api/omarai.py#L225) | 225 | `"        baked = \"\""` | — |
| [SRC-EEF2E6447C-L000226](../../api/omarai.py#L226) | 226 | `"    if _valid_build_sha(baked):"` | — |
| [SRC-EEF2E6447C-L000227](../../api/omarai.py#L227) | 227 | `"        return baked, \"image_baked\""` | — |
| [SRC-EEF2E6447C-L000228](../../api/omarai.py#L228) | 228 | `""` | — |
| [SRC-EEF2E6447C-L000229](../../api/omarai.py#L229) | 229 | `"    for environment_name, source in _PLATFORM_BUILD_SHA_ENVIRONMENTS:"` | — |
| [SRC-EEF2E6447C-L000230](../../api/omarai.py#L230) | 230 | `"        candidate = os.getenv(environment_name, \"\").strip().lower()"` | — |
| [SRC-EEF2E6447C-L000231](../../api/omarai.py#L231) | 231 | `"        if _valid_build_sha(candidate):"` | — |
| [SRC-EEF2E6447C-L000232](../../api/omarai.py#L232) | 232 | `"            return candidate, source"` | — |
| [SRC-EEF2E6447C-L000233](../../api/omarai.py#L233) | 233 | `"    return \"unknown\", \"unknown\""` | — |
| [SRC-EEF2E6447C-L000234](../../api/omarai.py#L234) | 234 | `""` | — |
| [SRC-EEF2E6447C-L000235](../../api/omarai.py#L235) | 235 | `""` | — |
| [SRC-EEF2E6447C-L000236](../../api/omarai.py#L236) | 236 | `"def _build_sha() -> str:"` | — |
| [SRC-EEF2E6447C-L000237](../../api/omarai.py#L237) | 237 | `"    \"\"\"Return a validated source SHA, or 'unknown' when no trusted build evidence exists.\"\"\""` | — |
| [SRC-EEF2E6447C-L000238](../../api/omarai.py#L238) | 238 | `"    return _build_identity()[0]"` | — |
| [SRC-EEF2E6447C-L000239](../../api/omarai.py#L239) | 239 | `""` | — |
| [SRC-EEF2E6447C-L000240](../../api/omarai.py#L240) | 240 | `""` | — |
| [SRC-EEF2E6447C-L000241](../../api/omarai.py#L241) | 241 | `"class Handler(BaseHTTPRequestHandler):"` | — |
| [SRC-EEF2E6447C-L000242](../../api/omarai.py#L242) | 242 | `"    def setup(self):"` | — |
| [SRC-EEF2E6447C-L000243](../../api/omarai.py#L243) | 243 | `"        \"\"\"Install a reader with a strict deadline for the request line and headers.\"\"\""` | — |
| [SRC-EEF2E6447C-L000244](../../api/omarai.py#L244) | 244 | `"        self.connection = self.request"` | — |
| [SRC-EEF2E6447C-L000245](../../api/omarai.py#L245) | 245 | `"        if self.timeout is not None:"` | — |
| [SRC-EEF2E6447C-L000246](../../api/omarai.py#L246) | 246 | `"            self.connection.settimeout(self.timeout)"` | — |
| [SRC-EEF2E6447C-L000247](../../api/omarai.py#L247) | 247 | `"        self._request_header_deadline = None"` | — |
| [SRC-EEF2E6447C-L000248](../../api/omarai.py#L248) | 248 | `"        self.rfile = _DeadlineRequestReader(self.connection, self)"` | — |
| [SRC-EEF2E6447C-L000249](../../api/omarai.py#L249) | 249 | `"        self.wfile = self.connection.makefile(\"wb\", self.wbufsize)"` | — |
| [SRC-EEF2E6447C-L000250](../../api/omarai.py#L250) | 250 | `""` | — |
| [SRC-EEF2E6447C-L000251](../../api/omarai.py#L251) | 251 | `"    def handle_one_request(self):"` | — |
| [SRC-EEF2E6447C-L000252](../../api/omarai.py#L252) | 252 | `"        timeout = max("` | — |
| [SRC-EEF2E6447C-L000253](../../api/omarai.py#L253) | 253 | `"            0.1,"` | — |
| [SRC-EEF2E6447C-L000254](../../api/omarai.py#L254) | 254 | `"            min("` | — |
| [SRC-EEF2E6447C-L000255](../../api/omarai.py#L255) | 255 | `"                float(REQUEST_HEADER_READ_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000256](../../api/omarai.py#L256) | 256 | `"                MAX_REQUEST_HEADER_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000257](../../api/omarai.py#L257) | 257 | `"            ),"` | — |
| [SRC-EEF2E6447C-L000258](../../api/omarai.py#L258) | 258 | `"        )"` | — |
| [SRC-EEF2E6447C-L000259](../../api/omarai.py#L259) | 259 | `"        self._request_header_deadline = time.monotonic() + timeout"` | — |
| [SRC-EEF2E6447C-L000260](../../api/omarai.py#L260) | 260 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000261](../../api/omarai.py#L261) | 261 | `"            super().handle_one_request()"` | — |
| [SRC-EEF2E6447C-L000262](../../api/omarai.py#L262) | 262 | `"        except TimeoutError:"` | — |
| [SRC-EEF2E6447C-L000263](../../api/omarai.py#L263) | 263 | `"            # Incomplete request line/headers are untrusted protocol input;"` | — |
| [SRC-EEF2E6447C-L000264](../../api/omarai.py#L264) | 264 | `"            # close the socket without trying to parse or answer a partial request."` | — |
| [SRC-EEF2E6447C-L000265](../../api/omarai.py#L265) | 265 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000266](../../api/omarai.py#L266) | 266 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000267](../../api/omarai.py#L267) | 267 | `"            self._request_header_deadline = None"` | — |
| [SRC-EEF2E6447C-L000268](../../api/omarai.py#L268) | 268 | `""` | — |
| [SRC-EEF2E6447C-L000269](../../api/omarai.py#L269) | 269 | `"    store = _lead_store_from_environment()"` | — |
| [SRC-EEF2E6447C-L000270](../../api/omarai.py#L270) | 270 | `"    _rate_lock = threading.Lock()"` | — |
| [SRC-EEF2E6447C-L000271](../../api/omarai.py#L271) | 271 | `"    _request_times: ClassVar[dict[str, deque[float]]] = defaultdict(deque)"` | — |
| [SRC-EEF2E6447C-L000272](../../api/omarai.py#L272) | 272 | `"    _rate_last_cleanup: ClassVar[float] = 0.0"` | — |
| [SRC-EEF2E6447C-L000273](../../api/omarai.py#L273) | 273 | `"    RATE_LIMIT_REQUESTS = 20"` | — |
| [SRC-EEF2E6447C-L000274](../../api/omarai.py#L274) | 274 | `"    RATE_LIMIT_WINDOW_SECONDS = 60"` | — |
| [SRC-EEF2E6447C-L000275](../../api/omarai.py#L275) | 275 | `"    RATE_LIMIT_CLEANUP_INTERVAL_SECONDS = 60"` | — |
| [SRC-EEF2E6447C-L000276](../../api/omarai.py#L276) | 276 | `"    AGENT_CONCURRENCY_LIMIT = _configured_agent_concurrency_limit()"` | — |
| [SRC-EEF2E6447C-L000277](../../api/omarai.py#L277) | 277 | `"    _agent_semaphore = threading.BoundedSemaphore(AGENT_CONCURRENCY_LIMIT)"` | — |
| [SRC-EEF2E6447C-L000278](../../api/omarai.py#L278) | 278 | `""` | — |
| [SRC-EEF2E6447C-L000279](../../api/omarai.py#L279) | 279 | `"    def _run_bounded_agent_operation(self, operation):"` | — |
| [SRC-EEF2E6447C-L000280](../../api/omarai.py#L280) | 280 | `"        \"\"\"Run an expensive operation only when a process-local slot is available.\"\"\""` | — |
| [SRC-EEF2E6447C-L000281](../../api/omarai.py#L281) | 281 | `"        cls = type(self)"` | — |
| [SRC-EEF2E6447C-L000282](../../api/omarai.py#L282) | 282 | `"        if not cls._agent_semaphore.acquire(blocking=False):"` | — |
| [SRC-EEF2E6447C-L000283](../../api/omarai.py#L283) | 283 | `"            return self.respond("` | — |
| [SRC-EEF2E6447C-L000284](../../api/omarai.py#L284) | 284 | `"                503,"` | — |
| [SRC-EEF2E6447C-L000285](../../api/omarai.py#L285) | 285 | `"                {"` | — |
| [SRC-EEF2E6447C-L000286](../../api/omarai.py#L286) | 286 | `"                    \"error\": \"خدمة البحث مشغولة حاليًا؛ أعد المحاولة بعد قليل.\","` | — |
| [SRC-EEF2E6447C-L000287](../../api/omarai.py#L287) | 287 | `"                    \"retry_after_seconds\": 5,"` | — |
| [SRC-EEF2E6447C-L000288](../../api/omarai.py#L288) | 288 | `"                    \"process_concurrency_limit\": cls.AGENT_CONCURRENCY_LIMIT,"` | — |
| [SRC-EEF2E6447C-L000289](../../api/omarai.py#L289) | 289 | `"                },"` | — |
| [SRC-EEF2E6447C-L000290](../../api/omarai.py#L290) | 290 | `"            )"` | — |
| [SRC-EEF2E6447C-L000291](../../api/omarai.py#L291) | 291 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000292](../../api/omarai.py#L292) | 292 | `"            return self.respond(200, operation())"` | — |
| [SRC-EEF2E6447C-L000293](../../api/omarai.py#L293) | 293 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000294](../../api/omarai.py#L294) | 294 | `"            cls._agent_semaphore.release()"` | — |
| [SRC-EEF2E6447C-L000295](../../api/omarai.py#L295) | 295 | `""` | — |
| [SRC-EEF2E6447C-L000296](../../api/omarai.py#L296) | 296 | `"    def _authorized(self):"` | — |
| [SRC-EEF2E6447C-L000297](../../api/omarai.py#L297) | 297 | `"        expected = os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000298](../../api/omarai.py#L298) | 298 | `"        if not expected:"` | — |
| [SRC-EEF2E6447C-L000299](../../api/omarai.py#L299) | 299 | `"            return os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() != \"1\""` | — |
| [SRC-EEF2E6447C-L000300](../../api/omarai.py#L300) | 300 | `"        supplied = self.headers.get(\"Authorization\", \"\")"` | — |
| [SRC-EEF2E6447C-L000301](../../api/omarai.py#L301) | 301 | `"        if not supplied.startswith(\"Bearer \"):"` | — |
| [SRC-EEF2E6447C-L000302](../../api/omarai.py#L302) | 302 | `"            return False"` | — |
| [SRC-EEF2E6447C-L000303](../../api/omarai.py#L303) | 303 | `"        return hmac.compare_digest(supplied[7:].strip(), expected)"` | — |
| [SRC-EEF2E6447C-L000304](../../api/omarai.py#L304) | 304 | `""` | — |
| [SRC-EEF2E6447C-L000305](../../api/omarai.py#L305) | 305 | `"    def _allowed_origins(self):"` | — |
| [SRC-EEF2E6447C-L000306](../../api/omarai.py#L306) | 306 | `"        \"\"\"Return configured browser origins plus this service’s own origin."` | — |
| [SRC-EEF2E6447C-L000307](../../api/omarai.py#L307) | 307 | `""` | — |
| [SRC-EEF2E6447C-L000308](../../api/omarai.py#L308) | 308 | `"        OMARAI_ALLOWED_ORIGINS is a comma-separated list of trusted origins"` | — |
| [SRC-EEF2E6447C-L000309](../../api/omarai.py#L309) | 309 | `"        (scheme + host + optional port; no path and no wildcard)."` | — |
| [SRC-EEF2E6447C-L000310](../../api/omarai.py#L310) | 310 | `"        \"\"\""` | — |
| [SRC-EEF2E6447C-L000311](../../api/omarai.py#L311) | 311 | `"        configured = os.getenv(\"OMARAI_ALLOWED_ORIGINS\", \"\")"` | — |
| [SRC-EEF2E6447C-L000312](../../api/omarai.py#L312) | 312 | `"        origins = {"` | — |
| [SRC-EEF2E6447C-L000313](../../api/omarai.py#L313) | 313 | `"            item.strip().rstrip(\"/\")"` | — |
| [SRC-EEF2E6447C-L000314](../../api/omarai.py#L314) | 314 | `"            for item in configured.split(\",\")"` | — |
| [SRC-EEF2E6447C-L000315](../../api/omarai.py#L315) | 315 | `"            if item.strip()"` | — |
| [SRC-EEF2E6447C-L000316](../../api/omarai.py#L316) | 316 | `"        }"` | — |
| [SRC-EEF2E6447C-L000317](../../api/omarai.py#L317) | 317 | `"        if os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() == \"1\":"` | — |
| [SRC-EEF2E6447C-L000318](../../api/omarai.py#L318) | 318 | `"            # Host identifies the requested service origin. Do not derive allowed"` | — |
| [SRC-EEF2E6447C-L000319](../../api/omarai.py#L319) | 319 | `"            # origins from X-Forwarded-Host: direct clients can spoof that header"` | — |
| [SRC-EEF2E6447C-L000320](../../api/omarai.py#L320) | 320 | `"            # unless the reverse proxy is separately configured to overwrite it."` | — |
| [SRC-EEF2E6447C-L000321](../../api/omarai.py#L321) | 321 | `"            scheme = self.headers.get(\"X-Forwarded-Proto\", \"https\").split(\",\", 1)[0].strip().lower()"` | — |
| [SRC-EEF2E6447C-L000322](../../api/omarai.py#L322) | 322 | `"            host = self.headers.get(\"Host\", \"\").split(\",\", 1)[0].strip()"` | — |
| [SRC-EEF2E6447C-L000323](../../api/omarai.py#L323) | 323 | `"            if host:"` | — |
| [SRC-EEF2E6447C-L000324](../../api/omarai.py#L324) | 324 | `"                origins.add(f\"https://{host}\".rstrip(\"/\"))"` | — |
| [SRC-EEF2E6447C-L000325](../../api/omarai.py#L325) | 325 | `"                origins.add(f\"{scheme}://{host}\".rstrip(\"/\"))"` | — |
| [SRC-EEF2E6447C-L000326](../../api/omarai.py#L326) | 326 | `"        else:"` | — |
| [SRC-EEF2E6447C-L000327](../../api/omarai.py#L327) | 327 | `"            port = self.server.server_port"` | — |
| [SRC-EEF2E6447C-L000328](../../api/omarai.py#L328) | 328 | `"            origins.update("` | — |
| [SRC-EEF2E6447C-L000329](../../api/omarai.py#L329) | 329 | `"                {"` | — |
| [SRC-EEF2E6447C-L000330](../../api/omarai.py#L330) | 330 | `"                    f\"http://127.0.0.1:{port}\","` | — |
| [SRC-EEF2E6447C-L000331](../../api/omarai.py#L331) | 331 | `"                    f\"http://localhost:{port}\","` | — |
| [SRC-EEF2E6447C-L000332](../../api/omarai.py#L332) | 332 | `"                    f\"http://[::1]:{port}\","` | — |
| [SRC-EEF2E6447C-L000333](../../api/omarai.py#L333) | 333 | `"                }"` | — |
| [SRC-EEF2E6447C-L000334](../../api/omarai.py#L334) | 334 | `"            )"` | — |
| [SRC-EEF2E6447C-L000335](../../api/omarai.py#L335) | 335 | `"        return origins"` | — |
| [SRC-EEF2E6447C-L000336](../../api/omarai.py#L336) | 336 | `""` | — |
| [SRC-EEF2E6447C-L000337](../../api/omarai.py#L337) | 337 | `"    def _origin_allowed(self, origin):"` | — |
| [SRC-EEF2E6447C-L000338](../../api/omarai.py#L338) | 338 | `"        return bool(origin) and origin.rstrip(\"/\") in self._allowed_origins()"` | — |
| [SRC-EEF2E6447C-L000339](../../api/omarai.py#L339) | 339 | `""` | — |
| [SRC-EEF2E6447C-L000340](../../api/omarai.py#L340) | 340 | `"    def _rate_limit_client_key(self):"` | — |
| [SRC-EEF2E6447C-L000341](../../api/omarai.py#L341) | 341 | `"        \"\"\"Choose a rate-limit identity without trusting spoofable proxy headers by default."` | — |
| [SRC-EEF2E6447C-L000342](../../api/omarai.py#L342) | 342 | `""` | — |
| [SRC-EEF2E6447C-L000343](../../api/omarai.py#L343) | 343 | `"        Set OMARAI_TRUST_PROXY_HEADERS=1 only when the deployment's trusted reverse"` | — |
| [SRC-EEF2E6447C-L000344](../../api/omarai.py#L344) | 344 | `"        proxy appends the actual client IP as the rightmost X-Forwarded-For value."` | — |
| [SRC-EEF2E6447C-L000345](../../api/omarai.py#L345) | 345 | `"        \"\"\""` | — |
| [SRC-EEF2E6447C-L000346](../../api/omarai.py#L346) | 346 | `"        direct_ip = self.client_address[0]"` | — |
| [SRC-EEF2E6447C-L000347](../../api/omarai.py#L347) | 347 | `"        if os.getenv(\"OMARAI_TRUST_PROXY_HEADERS\", \"\").strip() != \"1\":"` | — |
| [SRC-EEF2E6447C-L000348](../../api/omarai.py#L348) | 348 | `"            return direct_ip"` | — |
| [SRC-EEF2E6447C-L000349](../../api/omarai.py#L349) | 349 | `"        forwarded = self.headers.get(\"X-Forwarded-For\", \"\")"` | — |
| [SRC-EEF2E6447C-L000350](../../api/omarai.py#L350) | 350 | `"        candidate = forwarded.rsplit(\",\", 1)[-1].strip() if forwarded else \"\""` | — |
| [SRC-EEF2E6447C-L000351](../../api/omarai.py#L351) | 351 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000352](../../api/omarai.py#L352) | 352 | `"            return str(ipaddress.ip_address(candidate))"` | — |
| [SRC-EEF2E6447C-L000353](../../api/omarai.py#L353) | 353 | `"        except ValueError:"` | — |
| [SRC-EEF2E6447C-L000354](../../api/omarai.py#L354) | 354 | `"            return direct_ip"` | — |
| [SRC-EEF2E6447C-L000355](../../api/omarai.py#L355) | 355 | `""` | — |
| [SRC-EEF2E6447C-L000356](../../api/omarai.py#L356) | 356 | `"    def _rate_limit_ok(self):"` | — |
| [SRC-EEF2E6447C-L000357](../../api/omarai.py#L357) | 357 | `"        client_ip = self._rate_limit_client_key()"` | — |
| [SRC-EEF2E6447C-L000358](../../api/omarai.py#L358) | 358 | `"        now = time.monotonic()"` | — |
| [SRC-EEF2E6447C-L000359](../../api/omarai.py#L359) | 359 | `"        cls = type(self)"` | — |
| [SRC-EEF2E6447C-L000360](../../api/omarai.py#L360) | 360 | `"        with self._rate_lock:"` | — |
| [SRC-EEF2E6447C-L000361](../../api/omarai.py#L361) | 361 | `"            # Periodically remove IP buckets whose entire sliding window has expired."` | — |
| [SRC-EEF2E6447C-L000362](../../api/omarai.py#L362) | 362 | `"            # Without this sweep, a public endpoint could retain one empty deque per"` | — |
| [SRC-EEF2E6447C-L000363](../../api/omarai.py#L363) | 363 | `"            # distinct client IP forever, even though the rate-limit window is 60 sec."` | — |
| [SRC-EEF2E6447C-L000364](../../api/omarai.py#L364) | 364 | `"            if now - cls._rate_last_cleanup >= cls.RATE_LIMIT_CLEANUP_INTERVAL_SECONDS:"` | — |
| [SRC-EEF2E6447C-L000365](../../api/omarai.py#L365) | 365 | `"                cutoff = now - cls.RATE_LIMIT_WINDOW_SECONDS"` | — |
| [SRC-EEF2E6447C-L000366](../../api/omarai.py#L366) | 366 | `"                for key, timestamps in list(cls._request_times.items()):"` | — |
| [SRC-EEF2E6447C-L000367](../../api/omarai.py#L367) | 367 | `"                    while timestamps and timestamps[0] <= cutoff:"` | — |
| [SRC-EEF2E6447C-L000368](../../api/omarai.py#L368) | 368 | `"                        timestamps.popleft()"` | — |
| [SRC-EEF2E6447C-L000369](../../api/omarai.py#L369) | 369 | `"                    if not timestamps:"` | — |
| [SRC-EEF2E6447C-L000370](../../api/omarai.py#L370) | 370 | `"                        cls._request_times.pop(key, None)"` | — |
| [SRC-EEF2E6447C-L000371](../../api/omarai.py#L371) | 371 | `"                cls._rate_last_cleanup = now"` | — |
| [SRC-EEF2E6447C-L000372](../../api/omarai.py#L372) | 372 | `""` | — |
| [SRC-EEF2E6447C-L000373](../../api/omarai.py#L373) | 373 | `"            events = cls._request_times[client_ip]"` | — |
| [SRC-EEF2E6447C-L000374](../../api/omarai.py#L374) | 374 | `"            while events and now - events[0] >= cls.RATE_LIMIT_WINDOW_SECONDS:"` | — |
| [SRC-EEF2E6447C-L000375](../../api/omarai.py#L375) | 375 | `"                events.popleft()"` | — |
| [SRC-EEF2E6447C-L000376](../../api/omarai.py#L376) | 376 | `"            if len(events) >= cls.RATE_LIMIT_REQUESTS:"` | — |
| [SRC-EEF2E6447C-L000377](../../api/omarai.py#L377) | 377 | `"                return False"` | — |
| [SRC-EEF2E6447C-L000378](../../api/omarai.py#L378) | 378 | `"            events.append(now)"` | — |
| [SRC-EEF2E6447C-L000379](../../api/omarai.py#L379) | 379 | `"            return True"` | — |
| [SRC-EEF2E6447C-L000380](../../api/omarai.py#L380) | 380 | `""` | — |
| [SRC-EEF2E6447C-L000381](../../api/omarai.py#L381) | 381 | `"    def _read_request_body(self) -> bytes \| None:"` | — |
| [SRC-EEF2E6447C-L000382](../../api/omarai.py#L382) | 382 | `"        \"\"\"Read a bounded body with both idle and absolute wall-clock deadlines.\"\"\""` | — |
| [SRC-EEF2E6447C-L000383](../../api/omarai.py#L383) | 383 | `"        raw_size = self.headers.get(\"Content-Length\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000384](../../api/omarai.py#L384) | 384 | `"        if not raw_size or not raw_size.isascii() or not raw_size.isdecimal():"` | — |
| [SRC-EEF2E6447C-L000385](../../api/omarai.py#L385) | 385 | `"            self.respond(400, {\"error\": \"valid Content-Length is required\"})"` | — |
| [SRC-EEF2E6447C-L000386](../../api/omarai.py#L386) | 386 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000387](../../api/omarai.py#L387) | 387 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000388](../../api/omarai.py#L388) | 388 | `"            size = int(raw_size)"` | — |
| [SRC-EEF2E6447C-L000389](../../api/omarai.py#L389) | 389 | `"        except ValueError:"` | — |
| [SRC-EEF2E6447C-L000390](../../api/omarai.py#L390) | 390 | `"            self.respond(400, {\"error\": \"valid Content-Length is required\"})"` | — |
| [SRC-EEF2E6447C-L000391](../../api/omarai.py#L391) | 391 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000392](../../api/omarai.py#L392) | 392 | `"        if size <= 0:"` | — |
| [SRC-EEF2E6447C-L000393](../../api/omarai.py#L393) | 393 | `"            self.respond(400, {\"error\": \"request body is required\"})"` | — |
| [SRC-EEF2E6447C-L000394](../../api/omarai.py#L394) | 394 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000395](../../api/omarai.py#L395) | 395 | `"        if size > MAX_REQUEST_BODY_BYTES:"` | — |
| [SRC-EEF2E6447C-L000396](../../api/omarai.py#L396) | 396 | `"            self.respond(413, {\"error\": \"request too large\"})"` | — |
| [SRC-EEF2E6447C-L000397](../../api/omarai.py#L397) | 397 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000398](../../api/omarai.py#L398) | 398 | `""` | — |
| [SRC-EEF2E6447C-L000399](../../api/omarai.py#L399) | 399 | `"        total_timeout = max("` | — |
| [SRC-EEF2E6447C-L000400](../../api/omarai.py#L400) | 400 | `"            0.1,"` | — |
| [SRC-EEF2E6447C-L000401](../../api/omarai.py#L401) | 401 | `"            min("` | — |
| [SRC-EEF2E6447C-L000402](../../api/omarai.py#L402) | 402 | `"                float(REQUEST_BODY_READ_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000403](../../api/omarai.py#L403) | 403 | `"                MAX_REQUEST_BODY_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000404](../../api/omarai.py#L404) | 404 | `"            ),"` | — |
| [SRC-EEF2E6447C-L000405](../../api/omarai.py#L405) | 405 | `"        )"` | — |
| [SRC-EEF2E6447C-L000406](../../api/omarai.py#L406) | 406 | `"        idle_timeout = max("` | — |
| [SRC-EEF2E6447C-L000407](../../api/omarai.py#L407) | 407 | `"            0.1,"` | — |
| [SRC-EEF2E6447C-L000408](../../api/omarai.py#L408) | 408 | `"            min("` | — |
| [SRC-EEF2E6447C-L000409](../../api/omarai.py#L409) | 409 | `"                float(REQUEST_BODY_IDLE_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000410](../../api/omarai.py#L410) | 410 | `"                MAX_REQUEST_BODY_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000411](../../api/omarai.py#L411) | 411 | `"            ),"` | — |
| [SRC-EEF2E6447C-L000412](../../api/omarai.py#L412) | 412 | `"        )"` | — |
| [SRC-EEF2E6447C-L000413](../../api/omarai.py#L413) | 413 | `"        deadline = time.monotonic() + total_timeout"` | — |
| [SRC-EEF2E6447C-L000414](../../api/omarai.py#L414) | 414 | `"        previous_timeout = self.connection.gettimeout()"` | — |
| [SRC-EEF2E6447C-L000415](../../api/omarai.py#L415) | 415 | `"        body = bytearray()"` | — |
| [SRC-EEF2E6447C-L000416](../../api/omarai.py#L416) | 416 | `"        timed_out = False"` | — |
| [SRC-EEF2E6447C-L000417](../../api/omarai.py#L417) | 417 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000418](../../api/omarai.py#L418) | 418 | `"            while len(body) < size:"` | — |
| [SRC-EEF2E6447C-L000419](../../api/omarai.py#L419) | 419 | `"                remaining = deadline - time.monotonic()"` | — |
| [SRC-EEF2E6447C-L000420](../../api/omarai.py#L420) | 420 | `"                if remaining <= 0:"` | — |
| [SRC-EEF2E6447C-L000421](../../api/omarai.py#L421) | 421 | `"                    timed_out = True"` | — |
| [SRC-EEF2E6447C-L000422](../../api/omarai.py#L422) | 422 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000423](../../api/omarai.py#L423) | 423 | `"                self.connection.settimeout(min(idle_timeout, remaining))"` | — |
| [SRC-EEF2E6447C-L000424](../../api/omarai.py#L424) | 424 | `"                try:"` | — |
| [SRC-EEF2E6447C-L000425](../../api/omarai.py#L425) | 425 | `"                    # read1 performs at most one underlying read, letting us re-check"` | — |
| [SRC-EEF2E6447C-L000426](../../api/omarai.py#L426) | 426 | `"                    # the absolute deadline between body fragments."` | — |
| [SRC-EEF2E6447C-L000427](../../api/omarai.py#L427) | 427 | `"                    chunk = self.rfile.read1("` | — |
| [SRC-EEF2E6447C-L000428](../../api/omarai.py#L428) | 428 | `"                        min(size - len(body), REQUEST_BODY_READ_CHUNK_BYTES)"` | — |
| [SRC-EEF2E6447C-L000429](../../api/omarai.py#L429) | 429 | `"                    )"` | — |
| [SRC-EEF2E6447C-L000430](../../api/omarai.py#L430) | 430 | `"                except TimeoutError:"` | — |
| [SRC-EEF2E6447C-L000431](../../api/omarai.py#L431) | 431 | `"                    timed_out = True"` | — |
| [SRC-EEF2E6447C-L000432](../../api/omarai.py#L432) | 432 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000433](../../api/omarai.py#L433) | 433 | `"                if not chunk:"` | — |
| [SRC-EEF2E6447C-L000434](../../api/omarai.py#L434) | 434 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000435](../../api/omarai.py#L435) | 435 | `"                body.extend(chunk)"` | — |
| [SRC-EEF2E6447C-L000436](../../api/omarai.py#L436) | 436 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000437](../../api/omarai.py#L437) | 437 | `"            try:"` | — |
| [SRC-EEF2E6447C-L000438](../../api/omarai.py#L438) | 438 | `"                self.connection.settimeout(previous_timeout)"` | — |
| [SRC-EEF2E6447C-L000439](../../api/omarai.py#L439) | 439 | `"            except OSError:"` | — |
| [SRC-EEF2E6447C-L000440](../../api/omarai.py#L440) | 440 | `"                pass"` | — |
| [SRC-EEF2E6447C-L000441](../../api/omarai.py#L441) | 441 | `""` | — |
| [SRC-EEF2E6447C-L000442](../../api/omarai.py#L442) | 442 | `"        if timed_out:"` | — |
| [SRC-EEF2E6447C-L000443](../../api/omarai.py#L443) | 443 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000444](../../api/omarai.py#L444) | 444 | `"            self.respond(408, {\"error\": \"request body read timed out\"})"` | — |
| [SRC-EEF2E6447C-L000445](../../api/omarai.py#L445) | 445 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000446](../../api/omarai.py#L446) | 446 | `"        if len(body) != size:"` | — |
| [SRC-EEF2E6447C-L000447](../../api/omarai.py#L447) | 447 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000448](../../api/omarai.py#L448) | 448 | `"            self.respond(400, {\"error\": \"incomplete request body\"})"` | — |
| [SRC-EEF2E6447C-L000449](../../api/omarai.py#L449) | 449 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000450](../../api/omarai.py#L450) | 450 | `"        return bytes(body)"` | — |
| [SRC-EEF2E6447C-L000451](../../api/omarai.py#L451) | 451 | `""` | — |
| [SRC-EEF2E6447C-L000452](../../api/omarai.py#L452) | 452 | `"    def end_headers(self):"` | — |
| [SRC-EEF2E6447C-L000453](../../api/omarai.py#L453) | 453 | `"        \"\"\"Apply defensive browser headers to successful and error responses alike.\"\"\""` | — |
| [SRC-EEF2E6447C-L000454](../../api/omarai.py#L454) | 454 | `"        self.send_header(\"X-Content-Type-Options\", \"nosniff\")"` | — |
| [SRC-EEF2E6447C-L000455](../../api/omarai.py#L455) | 455 | `"        self.send_header(\"X-Frame-Options\", \"DENY\")"` | — |
| [SRC-EEF2E6447C-L000456](../../api/omarai.py#L456) | 456 | `"        self.send_header(\"Referrer-Policy\", \"strict-origin-when-cross-origin\")"` | — |
| [SRC-EEF2E6447C-L000457](../../api/omarai.py#L457) | 457 | `"        self.send_header(\"Permissions-Policy\", \"camera=(), microphone=(), geolocation=()\")"` | — |
| [SRC-EEF2E6447C-L000458](../../api/omarai.py#L458) | 458 | `"        self.send_header(\"Content-Security-Policy\", _content_security_policy())"` | — |
| [SRC-EEF2E6447C-L000459](../../api/omarai.py#L459) | 459 | `"        super().end_headers()"` | — |
| [SRC-EEF2E6447C-L000460](../../api/omarai.py#L460) | 460 | `""` | — |
| [SRC-EEF2E6447C-L000461](../../api/omarai.py#L461) | 461 | `"    def respond(self, status, payload, content_type=\"application/json; charset=utf-8\"):"` | — |
| [SRC-EEF2E6447C-L000462](../../api/omarai.py#L462) | 462 | `"        body = payload.encode() if isinstance(payload, str) else json.dumps(payload, ensure_ascii=False).encode()"` | — |
| [SRC-EEF2E6447C-L000463](../../api/omarai.py#L463) | 463 | `"        self.send_response(status)"` | — |
| [SRC-EEF2E6447C-L000464](../../api/omarai.py#L464) | 464 | `"        self.send_header(\"Content-Type\", content_type)"` | — |
| [SRC-EEF2E6447C-L000465](../../api/omarai.py#L465) | 465 | `"        self.send_header(\"Content-Length\", str(len(body)))"` | — |
| [SRC-EEF2E6447C-L000466](../../api/omarai.py#L466) | 466 | `"        self.send_header(\"Cache-Control\", \"no-store\")"` | — |
| [SRC-EEF2E6447C-L000467](../../api/omarai.py#L467) | 467 | `"        origin = self.headers.get(\"Origin\")"` | — |
| [SRC-EEF2E6447C-L000468](../../api/omarai.py#L468) | 468 | `"        if origin and self._origin_allowed(origin):"` | — |
| [SRC-EEF2E6447C-L000469](../../api/omarai.py#L469) | 469 | `"            self.send_header(\"Access-Control-Allow-Origin\", origin)"` | — |
| [SRC-EEF2E6447C-L000470](../../api/omarai.py#L470) | 470 | `"            self.send_header(\"Vary\", \"Origin\")"` | — |
| [SRC-EEF2E6447C-L000471](../../api/omarai.py#L471) | 471 | `"        self.end_headers()"` | — |
| [SRC-EEF2E6447C-L000472](../../api/omarai.py#L472) | 472 | `"        self.wfile.write(body)"` | — |
| [SRC-EEF2E6447C-L000473](../../api/omarai.py#L473) | 473 | `""` | — |
| [SRC-EEF2E6447C-L000474](../../api/omarai.py#L474) | 474 | `"    def do_GET(self):"` | — |
| [SRC-EEF2E6447C-L000475](../../api/omarai.py#L475) | 475 | `"        parsed = urlparse(self.path)"` | — |
| [SRC-EEF2E6447C-L000476](../../api/omarai.py#L476) | 476 | `"        if parsed.path in {\"/\", \"/agent\"}:"` | — |
| [SRC-EEF2E6447C-L000477](../../api/omarai.py#L477) | 477 | `"            if not AGENT_DASHBOARD.exists():"` | — |
| [SRC-EEF2E6447C-L000478](../../api/omarai.py#L478) | 478 | `"                return self.respond(404, {\"error\": \"agent dashboard missing\"})"` | — |
| [SRC-EEF2E6447C-L000479](../../api/omarai.py#L479) | 479 | `"            return self.respond(200, AGENT_DASHBOARD.read_text(encoding=\"utf-8\"), \"text/html; charset=utf-8\")"` | — |
| [SRC-EEF2E6447C-L000480](../../api/omarai.py#L480) | 480 | `"        if parsed.path == \"/leads\":"` | — |
| [SRC-EEF2E6447C-L000481](../../api/omarai.py#L481) | 481 | `"            if not LEADS_DASHBOARD.exists():"` | — |
| [SRC-EEF2E6447C-L000482](../../api/omarai.py#L482) | 482 | `"                return self.respond(404, {\"error\": \"leads dashboard missing\"})"` | — |
| [SRC-EEF2E6447C-L000483](../../api/omarai.py#L483) | 483 | `"            return self.respond(200, LEADS_DASHBOARD.read_text(encoding=\"utf-8\"), \"text/html; charset=utf-8\")"` | — |
| [SRC-EEF2E6447C-L000484](../../api/omarai.py#L484) | 484 | `"        if parsed.path == \"/api/health\":"` | — |
| [SRC-EEF2E6447C-L000485](../../api/omarai.py#L485) | 485 | `"            return self.respond("` | — |
| [SRC-EEF2E6447C-L000486](../../api/omarai.py#L486) | 486 | `"                200,"` | — |
| [SRC-EEF2E6447C-L000487](../../api/omarai.py#L487) | 487 | `"                {"` | — |
| [SRC-EEF2E6447C-L000488](../../api/omarai.py#L488) | 488 | `"                    \"ok\": True,"` | — |
| [SRC-EEF2E6447C-L000489](../../api/omarai.py#L489) | 489 | `"                    \"app\": \"Omarai\","` | — |
| [SRC-EEF2E6447C-L000490](../../api/omarai.py#L490) | 490 | `"                    \"mode\": \"web-research\","` | — |
| [SRC-EEF2E6447C-L000491](../../api/omarai.py#L491) | 491 | `"                    \"agent\": WebAgent.status(),"` | — |
| [SRC-EEF2E6447C-L000492](../../api/omarai.py#L492) | 492 | `"                    \"build\": {"` | — |
| [SRC-EEF2E6447C-L000493](../../api/omarai.py#L493) | 493 | `"                        \"sha\": _build_identity()[0],"` | — |
| [SRC-EEF2E6447C-L000494](../../api/omarai.py#L494) | 494 | `"                        \"sha_status\": ("` | — |
| [SRC-EEF2E6447C-L000495](../../api/omarai.py#L495) | 495 | `"                            \"available\" if _build_identity()[0] != \"unknown\" else \"unknown\""` | — |
| [SRC-EEF2E6447C-L000496](../../api/omarai.py#L496) | 496 | `"                        ),"` | — |
| [SRC-EEF2E6447C-L000497](../../api/omarai.py#L497) | 497 | `"                        \"sha_source\": _build_identity()[1],"` | — |
| [SRC-EEF2E6447C-L000498](../../api/omarai.py#L498) | 498 | `"                    },"` | — |
| [SRC-EEF2E6447C-L000499](../../api/omarai.py#L499) | 499 | `"                },"` | — |
| [SRC-EEF2E6447C-L000500](../../api/omarai.py#L500) | 500 | `"            )"` | — |
| [SRC-EEF2E6447C-L000501](../../api/omarai.py#L501) | 501 | `"        if parsed.path == \"/api/leads\":"` | — |
| [SRC-EEF2E6447C-L000502](../../api/omarai.py#L502) | 502 | `"            if not self._rate_limit_ok():"` | — |
| [SRC-EEF2E6447C-L000503](../../api/omarai.py#L503) | 503 | `"                return self.respond(429, {\"error\": \"تجاوزت حد الطلبات المؤقت؛ حاول بعد دقيقة.\"})"` | — |
| [SRC-EEF2E6447C-L000504](../../api/omarai.py#L504) | 504 | `"            if not self._authorized():"` | — |
| [SRC-EEF2E6447C-L000505](../../api/omarai.py#L505) | 505 | `"                return self.respond(401, {\"error\": \"يلزم رمز الوصول الخاص بالتطبيق.\"})"` | — |
| [SRC-EEF2E6447C-L000506](../../api/omarai.py#L506) | 506 | `"            q = parse_qs(parsed.query)"` | — |
| [SRC-EEF2E6447C-L000507](../../api/omarai.py#L507) | 507 | `"            try:"` | — |
| [SRC-EEF2E6447C-L000508](../../api/omarai.py#L508) | 508 | `"                limit = max(1, min(int(q.get(\"limit\", [\"100\"])[0]), 500))"` | — |
| [SRC-EEF2E6447C-L000509](../../api/omarai.py#L509) | 509 | `"                leads = self.store.list(q.get(\"status\", [None])[0], limit)"` | — |
| [SRC-EEF2E6447C-L000510](../../api/omarai.py#L510) | 510 | `"            except (ValueError, TypeError):"` | — |
| [SRC-EEF2E6447C-L000511](../../api/omarai.py#L511) | 511 | `"                return self.respond(400, {\"error\": \"invalid status or limit\"})"` | — |
| [SRC-EEF2E6447C-L000512](../../api/omarai.py#L512) | 512 | `"            return self.respond(200, {\"leads\": leads, \"count\": len(leads)})"` | — |
| [SRC-EEF2E6447C-L000513](../../api/omarai.py#L513) | 513 | `"        return self.respond(404, {\"error\": \"not found\"})"` | — |
| [SRC-EEF2E6447C-L000514](../../api/omarai.py#L514) | 514 | `""` | — |
| [SRC-EEF2E6447C-L000515](../../api/omarai.py#L515) | 515 | `"    def do_POST(self):"` | — |
| [SRC-EEF2E6447C-L000516](../../api/omarai.py#L516) | 516 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000517](../../api/omarai.py#L517) | 517 | `"            # Count API attempts before origin/content-type/body validation so invalid"` | — |
| [SRC-EEF2E6447C-L000518](../../api/omarai.py#L518) | 518 | `"            # credentials and malformed requests cannot bypass per-client throttling."` | — |
| [SRC-EEF2E6447C-L000519](../../api/omarai.py#L519) | 519 | `"            path = urlparse(self.path).path"` | — |
| [SRC-EEF2E6447C-L000520](../../api/omarai.py#L520) | 520 | `"            if path.startswith(\"/api/\") and not self._rate_limit_ok():"` | — |
| [SRC-EEF2E6447C-L000521](../../api/omarai.py#L521) | 521 | `"                return self.respond(429, {\"error\": \"تجاوزت حد الطلبات المؤقت؛ حاول بعد دقيقة.\"})"` | — |
| [SRC-EEF2E6447C-L000522](../../api/omarai.py#L522) | 522 | `"            if path.startswith(\"/api/\") and not self._authorized():"` | — |
| [SRC-EEF2E6447C-L000523](../../api/omarai.py#L523) | 523 | `"                return self.respond(401, {\"error\": \"يلزم رمز الوصول الخاص بالتطبيق.\"})"` | — |
| [SRC-EEF2E6447C-L000524](../../api/omarai.py#L524) | 524 | `""` | — |
| [SRC-EEF2E6447C-L000525](../../api/omarai.py#L525) | 525 | `"            content_type = self.headers.get(\"Content-Type\", \"\").split(\";\", 1)[0].strip().lower()"` | — |
| [SRC-EEF2E6447C-L000526](../../api/omarai.py#L526) | 526 | `"            if content_type != \"application/json\":"` | — |
| [SRC-EEF2E6447C-L000527](../../api/omarai.py#L527) | 527 | `"                return self.respond(415, {\"error\": \"Content-Type must be application/json\"})"` | — |
| [SRC-EEF2E6447C-L000528](../../api/omarai.py#L528) | 528 | `"            origin = self.headers.get(\"Origin\")"` | — |
| [SRC-EEF2E6447C-L000529](../../api/omarai.py#L529) | 529 | `"            if origin and not self._origin_allowed(origin):"` | — |
| [SRC-EEF2E6447C-L000530](../../api/omarai.py#L530) | 530 | `"                return self.respond(403, {\"error\": \"cross-origin requests are not allowed\"})"` | — |
| [SRC-EEF2E6447C-L000531](../../api/omarai.py#L531) | 531 | `""` | — |
| [SRC-EEF2E6447C-L000532](../../api/omarai.py#L532) | 532 | `"            raw_body = self._read_request_body()"` | — |
| [SRC-EEF2E6447C-L000533](../../api/omarai.py#L533) | 533 | `"            if raw_body is None:"` | — |
| [SRC-EEF2E6447C-L000534](../../api/omarai.py#L534) | 534 | `"                return"` | — |
| [SRC-EEF2E6447C-L000535](../../api/omarai.py#L535) | 535 | `"            data = json.loads(raw_body)"` | — |
| [SRC-EEF2E6447C-L000536](../../api/omarai.py#L536) | 536 | `"            if not isinstance(data, dict):"` | — |
| [SRC-EEF2E6447C-L000537](../../api/omarai.py#L537) | 537 | `"                return self.respond(400, {\"error\": \"request body must be a JSON object\"})"` | — |
| [SRC-EEF2E6447C-L000538](../../api/omarai.py#L538) | 538 | `"            if path == \"/api/diagnostics\":"` | — |
| [SRC-EEF2E6447C-L000539](../../api/omarai.py#L539) | 539 | `"                test_model = data.get(\"test_model\", True)"` | — |
| [SRC-EEF2E6447C-L000540](../../api/omarai.py#L540) | 540 | `"                test_social = data.get(\"test_social\", False)"` | — |
| [SRC-EEF2E6447C-L000541](../../api/omarai.py#L541) | 541 | `"                if not isinstance(test_model, bool) or not isinstance(test_social, bool):"` | — |
| [SRC-EEF2E6447C-L000542](../../api/omarai.py#L542) | 542 | `"                    return self.respond("` | — |
| [SRC-EEF2E6447C-L000543](../../api/omarai.py#L543) | 543 | `"                        400,"` | — |
| [SRC-EEF2E6447C-L000544](../../api/omarai.py#L544) | 544 | `"                        {\"error\": \"test_model and test_social must be booleans\"},"` | — |
| [SRC-EEF2E6447C-L000545](../../api/omarai.py#L545) | 545 | `"                    )"` | — |
| [SRC-EEF2E6447C-L000546](../../api/omarai.py#L546) | 546 | `"                return self._run_bounded_agent_operation("` | — |
| [SRC-EEF2E6447C-L000547](../../api/omarai.py#L547) | 547 | `"                    lambda: WebAgent().diagnostics("` | — |
| [SRC-EEF2E6447C-L000548](../../api/omarai.py#L548) | 548 | `"                        test_model=test_model,"` | — |
| [SRC-EEF2E6447C-L000549](../../api/omarai.py#L549) | 549 | `"                        test_social=test_social,"` | — |
| [SRC-EEF2E6447C-L000550](../../api/omarai.py#L550) | 550 | `"                    )"` | — |
| [SRC-EEF2E6447C-L000551](../../api/omarai.py#L551) | 551 | `"                )"` | — |
| [SRC-EEF2E6447C-L000552](../../api/omarai.py#L552) | 552 | `""` | — |
| [SRC-EEF2E6447C-L000553](../../api/omarai.py#L553) | 553 | `"            if path == \"/api/agent\":"` | — |
| [SRC-EEF2E6447C-L000554](../../api/omarai.py#L554) | 554 | `"                question = data.get(\"question\", \"\")"` | — |
| [SRC-EEF2E6447C-L000555](../../api/omarai.py#L555) | 555 | `"                if not isinstance(question, str) or not question.strip():"` | — |
| [SRC-EEF2E6447C-L000556](../../api/omarai.py#L556) | 556 | `"                    return self.respond(400, {\"error\": \"question must be a non-empty string\"})"` | — |
| [SRC-EEF2E6447C-L000557](../../api/omarai.py#L557) | 557 | `"                agent = WebAgent()"` | — |
| [SRC-EEF2E6447C-L000558](../../api/omarai.py#L558) | 558 | `"                history = data.get(\"history\", [])"` | — |
| [SRC-EEF2E6447C-L000559](../../api/omarai.py#L559) | 559 | `"                if \"mode\" not in data:"` | — |
| [SRC-EEF2E6447C-L000560](../../api/omarai.py#L560) | 560 | `"                    return self._run_bounded_agent_operation("` | — |
| [SRC-EEF2E6447C-L000561](../../api/omarai.py#L561) | 561 | `"                        lambda: agent.answer(question, history)"` | — |
| [SRC-EEF2E6447C-L000562](../../api/omarai.py#L562) | 562 | `"                    )"` | — |
| [SRC-EEF2E6447C-L000563](../../api/omarai.py#L563) | 563 | `"                return self._run_bounded_agent_operation("` | — |
| [SRC-EEF2E6447C-L000564](../../api/omarai.py#L564) | 564 | `"                    lambda: agent.answer(question, history, data.get(\"mode\"))"` | — |
| [SRC-EEF2E6447C-L000565](../../api/omarai.py#L565) | 565 | `"                )"` | — |
| [SRC-EEF2E6447C-L000566](../../api/omarai.py#L566) | 566 | `""` | — |
| [SRC-EEF2E6447C-L000567](../../api/omarai.py#L567) | 567 | `"            if path == \"/api/ask\":"` | — |
| [SRC-EEF2E6447C-L000568](../../api/omarai.py#L568) | 568 | `"                question = data.get(\"question\", \"\")"` | — |
| [SRC-EEF2E6447C-L000569](../../api/omarai.py#L569) | 569 | `"                if not isinstance(question, str) or not question.strip():"` | — |
| [SRC-EEF2E6447C-L000570](../../api/omarai.py#L570) | 570 | `"                    return self.respond(400, {\"error\": \"question must be a non-empty string\"})"` | — |
| [SRC-EEF2E6447C-L000571](../../api/omarai.py#L571) | 571 | `"                if len(question) > 1000:"` | — |
| [SRC-EEF2E6447C-L000572](../../api/omarai.py#L572) | 572 | `"                    return self.respond(400, {\"error\": \"question must be at most 1000 characters\"})"` | — |
| [SRC-EEF2E6447C-L000573](../../api/omarai.py#L573) | 573 | `"                return self.respond(200, answer_question(question, self.store))"` | — |
| [SRC-EEF2E6447C-L000574](../../api/omarai.py#L574) | 574 | `"            if path == \"/api/analyze\":"` | — |
| [SRC-EEF2E6447C-L000575](../../api/omarai.py#L575) | 575 | `"                return self.respond("` | — |
| [SRC-EEF2E6447C-L000576](../../api/omarai.py#L576) | 576 | `"                    200,"` | — |
| [SRC-EEF2E6447C-L000577](../../api/omarai.py#L577) | 577 | `"                    analyze("` | — |
| [SRC-EEF2E6447C-L000578](../../api/omarai.py#L578) | 578 | `"                        data.get(\"text\", \"\"),"` | — |
| [SRC-EEF2E6447C-L000579](../../api/omarai.py#L579) | 579 | `"                        data.get(\"product_terms\", []),"` | — |
| [SRC-EEF2E6447C-L000580](../../api/omarai.py#L580) | 580 | `"                        data.get(\"location_terms\", []),"` | — |
| [SRC-EEF2E6447C-L000581](../../api/omarai.py#L581) | 581 | `"                    ),"` | — |
| [SRC-EEF2E6447C-L000582](../../api/omarai.py#L582) | 582 | `"                )"` | — |
| [SRC-EEF2E6447C-L000583](../../api/omarai.py#L583) | 583 | `"            if path == \"/api/leads\":"` | — |
| [SRC-EEF2E6447C-L000584](../../api/omarai.py#L584) | 584 | `"                lead, created = self.store.add("` | — |
| [SRC-EEF2E6447C-L000585](../../api/omarai.py#L585) | 585 | `"                    data.get(\"text\", \"\"),"` | — |
| [SRC-EEF2E6447C-L000586](../../api/omarai.py#L586) | 586 | `"                    data.get(\"source_url\", \"\"),"` | — |
| [SRC-EEF2E6447C-L000587](../../api/omarai.py#L587) | 587 | `"                    data.get(\"platform\", \"manual\"),"` | — |
| [SRC-EEF2E6447C-L000588](../../api/omarai.py#L588) | 588 | `"                    data.get(\"observed_at\"),"` | — |
| [SRC-EEF2E6447C-L000589](../../api/omarai.py#L589) | 589 | `"                    data.get(\"note\", \"\"),"` | — |
| [SRC-EEF2E6447C-L000590](../../api/omarai.py#L590) | 590 | `"                    data.get(\"product_terms\", []),"` | — |
| [SRC-EEF2E6447C-L000591](../../api/omarai.py#L591) | 591 | `"                    data.get(\"location_terms\", []),"` | — |
| [SRC-EEF2E6447C-L000592](../../api/omarai.py#L592) | 592 | `"                )"` | — |
| [SRC-EEF2E6447C-L000593](../../api/omarai.py#L593) | 593 | `"                return self.respond(201 if created else 200, {\"lead\": lead, \"created\": created})"` | — |
| [SRC-EEF2E6447C-L000594](../../api/omarai.py#L594) | 594 | `"            route = path.split(\"/\")"` | — |
| [SRC-EEF2E6447C-L000595](../../api/omarai.py#L595) | 595 | `"            if len(route) == 5 and route[1:3] == [\"api\", \"leads\"] and route[4] == \"status\":"` | — |
| [SRC-EEF2E6447C-L000596](../../api/omarai.py#L596) | 596 | `"                lead = self.store.update_status(route[3], data.get(\"status\", \"new\"))"` | — |
| [SRC-EEF2E6447C-L000597](../../api/omarai.py#L597) | 597 | `"                return self.respond(200, {\"lead\": lead}) if lead else self.respond(404, {\"error\": \"lead not found\"})"` | — |
| [SRC-EEF2E6447C-L000598](../../api/omarai.py#L598) | 598 | `"            return self.respond(404, {\"error\": \"not found\"})"` | — |
| [SRC-EEF2E6447C-L000599](../../api/omarai.py#L599) | 599 | `"        except (ValueError, TypeError, json.JSONDecodeError) as exc:"` | — |
| [SRC-EEF2E6447C-L000600](../../api/omarai.py#L600) | 600 | `"            return self.respond(400, {\"error\": str(exc)})"` | — |
| [SRC-EEF2E6447C-L000601](../../api/omarai.py#L601) | 601 | `"        except Exception:  # noqa: BLE001 — keep unexpected details out of API responses"` | — |
| [SRC-EEF2E6447C-L000602](../../api/omarai.py#L602) | 602 | `"            return self.respond(500, {\"error\": \"internal server error\"})"` | — |
| [SRC-EEF2E6447C-L000603](../../api/omarai.py#L603) | 603 | `""` | — |
| [SRC-EEF2E6447C-L000604](../../api/omarai.py#L604) | 604 | `"    def do_OPTIONS(self):"` | — |
| [SRC-EEF2E6447C-L000605](../../api/omarai.py#L605) | 605 | `"        origin = self.headers.get(\"Origin\")"` | — |
| [SRC-EEF2E6447C-L000606](../../api/omarai.py#L606) | 606 | `"        if not origin or not self._origin_allowed(origin):"` | — |
| [SRC-EEF2E6447C-L000607](../../api/omarai.py#L607) | 607 | `"            return self.respond(403, {\"error\": \"cross-origin requests are not allowed\"})"` | — |
| [SRC-EEF2E6447C-L000608](../../api/omarai.py#L608) | 608 | `"        self.send_response(204)"` | — |
| [SRC-EEF2E6447C-L000609](../../api/omarai.py#L609) | 609 | `"        self.send_header(\"Access-Control-Allow-Origin\", origin)"` | — |
| [SRC-EEF2E6447C-L000610](../../api/omarai.py#L610) | 610 | `"        self.send_header(\"Vary\", \"Origin\")"` | — |
| [SRC-EEF2E6447C-L000611](../../api/omarai.py#L611) | 611 | `"        self.send_header(\"Access-Control-Allow-Methods\", \"GET, POST, OPTIONS\")"` | — |
| [SRC-EEF2E6447C-L000612](../../api/omarai.py#L612) | 612 | `"        self.send_header(\"Access-Control-Allow-Headers\", \"Authorization, Content-Type\")"` | — |
| [SRC-EEF2E6447C-L000613](../../api/omarai.py#L613) | 613 | `"        self.send_header(\"Access-Control-Max-Age\", \"600\")"` | — |
| [SRC-EEF2E6447C-L000614](../../api/omarai.py#L614) | 614 | `"        self.send_header(\"Content-Length\", \"0\")"` | — |
| [SRC-EEF2E6447C-L000615](../../api/omarai.py#L615) | 615 | `"        self.end_headers()"` | — |
| [SRC-EEF2E6447C-L000616](../../api/omarai.py#L616) | 616 | `""` | — |
| [SRC-EEF2E6447C-L000617](../../api/omarai.py#L617) | 617 | `"    def log_message(self, *args):"` | — |
| [SRC-EEF2E6447C-L000618](../../api/omarai.py#L618) | 618 | `"        pass"` | — |
| [SRC-EEF2E6447C-L000619](../../api/omarai.py#L619) | 619 | `""` | — |
| [SRC-EEF2E6447C-L000620](../../api/omarai.py#L620) | 620 | `""` | — |
| [SRC-EEF2E6447C-L000621](../../api/omarai.py#L621) | 621 | `"def answer_question(question, store):"` | — |
| [SRC-EEF2E6447C-L000622](../../api/omarai.py#L622) | 622 | `"    \"\"\"Answer common operational questions from local records using explicit rules.\"\"\""` | — |
| [SRC-EEF2E6447C-L000623](../../api/omarai.py#L623) | 623 | `"    normalized = normalize(question)"` | — |
| [SRC-EEF2E6447C-L000624](../../api/omarai.py#L624) | 624 | `"    leads = store.list(limit=500)"` | — |
| [SRC-EEF2E6447C-L000625](../../api/omarai.py#L625) | 625 | `"    active = [lead for lead in leads if lead[\"status\"] not in {\"rejected\", \"converted\"}]"` | — |
| [SRC-EEF2E6447C-L000626](../../api/omarai.py#L626) | 626 | `"    if any(term in normalized for term in (\"افضل عميل\", \"احسن عميل\", \"افضل اشارة\", \"احسن اشارة\", \"اشارة اراجعها\", \"مين افضل\", \"مين اتابع\", \"اتابع مين\", \"اهم عميل\")):"` | — |
| [SRC-EEF2E6447C-L000627](../../api/omarai.py#L627) | 627 | `"        if not active:"` | — |
| [SRC-EEF2E6447C-L000628](../../api/omarai.py#L628) | 628 | `"            return {\"answer\": \"لا توجد إشارة نشطة محفوظة بعد. حلّل نصًا من مصدر مسموح واحفظه أولًا، ثم اسألني مرة أخرى.\", \"kind\": \"no_data\", \"lead_id\": None}"` | — |
| [SRC-EEF2E6447C-L000629](../../api/omarai.py#L629) | 629 | `"        lead = max(active, key=lambda item: (item[\"assessment\"][\"score\"], item[\"updated_at\"]))"` | — |
| [SRC-EEF2E6447C-L000630](../../api/omarai.py#L630) | 630 | `"        assessment = lead[\"assessment\"]"` | — |
| [SRC-EEF2E6447C-L000631](../../api/omarai.py#L631) | 631 | `"        answer = \"الأولوية المقترحة للمراجعة هي الإشارة \" + lead[\"id\"][:8] + \" بدرجة قواعد \" + str(assessment[\"score\"]) + \"/100. السبب: \" + assessment[\"summary\"] + \" المصدر: \" + lead[\"source_url\"] + \". هذه أولوية مراجعة وليست تأكيدًا أن صاحبه سيشتري.\""` | — |
| [SRC-EEF2E6447C-L000632](../../api/omarai.py#L632) | 632 | `"        return {\"answer\": answer, \"kind\": \"lead_recommendation\", \"lead_id\": lead[\"id\"]}"` | — |
| [SRC-EEF2E6447C-L000633](../../api/omarai.py#L633) | 633 | `"    if any(term in normalized for term in (\"كام عميل\", \"كم عميل\", \"عدد العملاء\", \"عدد الاشارات\", \"الاحصائيات\", \"احصائيات\")):"` | — |
| [SRC-EEF2E6447C-L000634](../../api/omarai.py#L634) | 634 | `"        keys = (\"new\", \"qualified\", \"contacted\", \"converted\", \"needs_review\", \"rejected\")"` | — |
| [SRC-EEF2E6447C-L000635](../../api/omarai.py#L635) | 635 | `"        by_status = {key: sum(lead[\"status\"] == key for lead in leads) for key in keys}"` | — |
| [SRC-EEF2E6447C-L000636](../../api/omarai.py#L636) | 636 | `"        high = sum(lead[\"assessment\"][\"label\"] == \"high_intent\" for lead in leads)"` | — |
| [SRC-EEF2E6447C-L000637](../../api/omarai.py#L637) | 637 | `"        answer = \"في السجل المحلي \" + str(len(leads)) + \" إشارة، منها \" + str(high) + \" بإشارة قوية نسبيًا وفق القواعد. الحالات: جديد \" + str(by_status[\"new\"]) + \"، مؤهل \" + str(by_status[\"qualified\"]) + \"، تم التواصل \" + str(by_status[\"contacted\"]) + \"، تم البيع \" + str(by_status[\"converted\"]) + \"، تحتاج مراجعة \" + str(by_status[\"needs_review\"]) + \"، مرفوض \" + str(by_status[\"rejected\"]) + \".\""` | — |
| [SRC-EEF2E6447C-L000638](../../api/omarai.py#L638) | 638 | `"        return {\"answer\": answer, \"kind\": \"local_statistics\", \"lead_id\": None}"` | — |
| [SRC-EEF2E6447C-L000639](../../api/omarai.py#L639) | 639 | `"    if any(term in normalized for term in (\"ليه الدرجه\", \"سبب الدرجه\", \"طريقة التقييم\", \"بتقيم ازاي\", \"معيار التقييم\")):"` | — |
| [SRC-EEF2E6447C-L000640](../../api/omarai.py#L640) | 640 | `"        latest = max(leads, key=lambda item: item[\"updated_at\"], default=None)"` | — |
| [SRC-EEF2E6447C-L000641](../../api/omarai.py#L641) | 641 | `"        if latest:"` | — |
| [SRC-EEF2E6447C-L000642](../../api/omarai.py#L642) | 642 | `"            signals = \"، \".join(signal[\"phrase\"] for signal in latest[\"assessment\"][\"matched_signals\"]) or \"لم تُطابق عبارات معروفة\""` | — |
| [SRC-EEF2E6447C-L000643](../../api/omarai.py#L643) | 643 | `"            answer = \"الإشارة الأحدث درجتها \" + str(latest[\"assessment\"][\"score\"]) + \"/100 لأن القواعد طابقت: \" + signals + \". الدرجة ليست احتمالًا إحصائيًا ولا تثبت نية الكاتب.\""` | — |
| [SRC-EEF2E6447C-L000644](../../api/omarai.py#L644) | 644 | `"        else:"` | — |
| [SRC-EEF2E6447C-L000645](../../api/omarai.py#L645) | 645 | `"            answer = \"أحسب الدرجة بقواعد واضحة: تعبير الشراء، خطوة تجارية تالية، السعر أو الميزانية، وسياق المنتج والمكان. كل فئة تحتسب مرة واحدة فقط.\""` | — |
| [SRC-EEF2E6447C-L000646](../../api/omarai.py#L646) | 646 | `"        return {\"answer\": answer, \"kind\": \"scoring_explanation\", \"lead_id\": latest[\"id\"] if latest else None}"` | — |
| [SRC-EEF2E6447C-L000647](../../api/omarai.py#L647) | 647 | `"    if any(term in normalized for term in (\"اكتب رساله\", \"اكتب رسالة\", \"رساله تواصل\", \"رسالة تواصل\", \"ابعتله\", \"اتواصل ازاي\")):"` | — |
| [SRC-EEF2E6447C-L000648](../../api/omarai.py#L648) | 648 | `"        if not active:"` | — |
| [SRC-EEF2E6447C-L000649](../../api/omarai.py#L649) | 649 | `"            answer = \"لا توجد إشارة محفوظة أخصص مسودة لها بعد. أدخل نصًا ومصدرًا أولًا.\""` | — |
| [SRC-EEF2E6447C-L000650](../../api/omarai.py#L650) | 650 | `"        else:"` | — |
| [SRC-EEF2E6447C-L000651](../../api/omarai.py#L651) | 651 | `"            lead = max(active, key=lambda item: (item[\"assessment\"][\"score\"], item[\"updated_at\"]))"` | — |
| [SRC-EEF2E6447C-L000652](../../api/omarai.py#L652) | 652 | `"            answer = \"مسودة للمراجعة البشرية فقط: «أهلًا، لاحظت سؤالك المنشور عن العقار/الوحدة. لو ما زلت مهتمًا، هل تحب الاطلاع على التفاصيل المتاحة وخيارات المعاينة؟» مرتبطة بالإشارة \" + lead[\"id\"][:8] + \". لم يتم إرسال أي رسالة.\""` | — |
| [SRC-EEF2E6447C-L000653](../../api/omarai.py#L653) | 653 | `"        return {\"answer\": answer, \"kind\": \"message_draft\", \"lead_id\": active[0][\"id\"] if active else None}"` | — |
| [SRC-EEF2E6447C-L000654](../../api/omarai.py#L654) | 654 | `"    return {\"answer\": \"أنا المساعد المحلي الخاص بسجل العملاء. استخدم وكيل البحث العام من الصفحة الرئيسية لطرح أسئلة مفتوحة والبحث في الويب.\", \"kind\": \"help\", \"lead_id\": None}"` | — |
| [SRC-EEF2E6447C-L000655](../../api/omarai.py#L655) | 655 | `""` | — |
| [SRC-EEF2E6447C-L000656](../../api/omarai.py#L656) | 656 | `""` | — |
| [SRC-EEF2E6447C-L000657](../../api/omarai.py#L657) | 657 | `"def serve(host=\"127.0.0.1\", port=8765):"` | — |
| [SRC-EEF2E6447C-L000658](../../api/omarai.py#L658) | 658 | `"    public_deployment = os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() == \"1\""` | — |
| [SRC-EEF2E6447C-L000659](../../api/omarai.py#L659) | 659 | `"    access_token = os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000660](../../api/omarai.py#L660) | 660 | `"    if host not in (\"127.0.0.1\", \"localhost\", \"::1\") and ("` | — |
| [SRC-EEF2E6447C-L000661](../../api/omarai.py#L661) | 661 | `"        not public_deployment or len(access_token) < 32"` | — |
| [SRC-EEF2E6447C-L000662](../../api/omarai.py#L662) | 662 | `"    ):"` | — |
| [SRC-EEF2E6447C-L000663](../../api/omarai.py#L663) | 663 | `"        raise ValueError("` | — |
| [SRC-EEF2E6447C-L000664](../../api/omarai.py#L664) | 664 | `"                \"Public binding requires OMARAI_PUBLIC_DEPLOYMENT=1 and \""` | — |
| [SRC-EEF2E6447C-L000665](../../api/omarai.py#L665) | 665 | `"                \"a private OMARAI_ACCESS_TOKEN of at least 32 characters.\""` | — |
| [SRC-EEF2E6447C-L000666](../../api/omarai.py#L666) | 666 | `"            )"` | — |
| [SRC-EEF2E6447C-L000667](../../api/omarai.py#L667) | 667 | `"    server = ThreadingHTTPServer((host, port), Handler)"` | — |
| [SRC-EEF2E6447C-L000668](../../api/omarai.py#L668) | 668 | `"    server.daemon_threads = True"` | — |
| [SRC-EEF2E6447C-L000669](../../api/omarai.py#L669) | 669 | `"    print(f\"Omarai running at http://{host}:{port} — Ctrl+C to stop\")"` | — |
| [SRC-EEF2E6447C-L000670](../../api/omarai.py#L670) | 670 | `"    print(\"Web research agent: /   \|   Lead workspace: /leads\")"` | — |
| [SRC-EEF2E6447C-L000671](../../api/omarai.py#L671) | 671 | `"    try:"` | — |
| [SRC-EEF2E6447C-L000672](../../api/omarai.py#L672) | 672 | `"        server.serve_forever()"` | — |
| [SRC-EEF2E6447C-L000673](../../api/omarai.py#L673) | 673 | `"    except KeyboardInterrupt:"` | — |
| [SRC-EEF2E6447C-L000674](../../api/omarai.py#L674) | 674 | `"        pass"` | — |
| [SRC-EEF2E6447C-L000675](../../api/omarai.py#L675) | 675 | `"    finally:"` | — |
| [SRC-EEF2E6447C-L000676](../../api/omarai.py#L676) | 676 | `"        server.server_close()"` | — |
| [SRC-EEF2E6447C-L000677](../../api/omarai.py#L677) | 677 | `""` | — |
| [SRC-EEF2E6447C-L000678](../../api/omarai.py#L678) | 678 | `""` | — |
| [SRC-EEF2E6447C-L000679](../../api/omarai.py#L679) | 679 | `"if __name__ == \"__main__\":"` | — |
| [SRC-EEF2E6447C-L000680](../../api/omarai.py#L680) | 680 | `"    serve()"` | — |
## وثائق ونصوص

### FILE-65AAF94960 — [artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-65AAF94960-L000001](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L1) | 1 | `"# تقرير قبول الاستضافة — Omarai"` | — |
| [SRC-65AAF94960-L000002](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L2) | 2 | `"**التاريخ:** 27 أكتوبر 2026  "` | — |
| [SRC-65AAF94960-L000003](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L3) | 3 | `"**المضيف:** https://omarai-dec45.containers.snapdeploy.app/  "` | — |
| [SRC-65AAF94960-L000004](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L4) | 4 | `"**جلسة المتصفح:** [TinyFish run af7ebb42-e032-4321-8454-a3628432f53d](https://agent.tinyfish.ai/runs/af7ebb42-e032-4321-8454-a3628432f53d)  "` | — |
| [SRC-65AAF94960-L000005](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L5) | 5 | `"**التصنيف:** PARTIAL / BLOCKED — لا إعلان جاهزية."` | — |
| [SRC-65AAF94960-L000006](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L6) | 6 | `""` | — |
| [SRC-65AAF94960-L000007](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L7) | 7 | `"## الملخص التنفيذي"` | — |
| [SRC-65AAF94960-L000008](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L8) | 8 | `"أُعيد اختبار الواجهة في ملف المتصفح المخصص، دون خزنة أسرار ودون إدخال أو كشف أي رمز. الصفحة حملت، لكن حقل رمز الوصول في **ملف المتصفح الاختباري فارغ**. لذلك فشل سؤال «ما عاصمة مصر؟» قبل تنفيذ البحث. لم تُختبر بعد مصادر البحث الحية ولا البحث الحديث ولا البحث المعمق فعليًا."` | — |
| [SRC-65AAF94960-L000009](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L9) | 9 | `""` | — |
| [SRC-65AAF94960-L000010](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L10) | 10 | `"هذه النتيجة لا تثبت أن الرمز المخزن في متصفح المستخدم غير صحيح؛ إنها تثبت فقط أن رمزًا لم يكن متاحًا في ملف المتصفح الاختباري. التخزين المحلي في المتصفحات/الملفات منفصل."` | — |
| [SRC-65AAF94960-L000011](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L11) | 11 | `""` | — |
| [SRC-65AAF94960-L000012](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L12) | 12 | `"## أدلة القبول"` | — |
| [SRC-65AAF94960-L000013](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L13) | 13 | `"\| الفحص \| النتيجة \| الحالة \|"` | — |
| [SRC-65AAF94960-L000014](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L14) | 14 | `"\|---\|---\|---\|"` | — |
| [SRC-65AAF94960-L000015](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L15) | 15 | `"\| تحميل الصفحة الرئيسية \| ظهرت واجهة Omarai \| VERIFIED \|"` | — |
| [SRC-65AAF94960-L000016](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L16) | 16 | ``"\| وجود رمز وصول في ملف المتصفح الاختباري \| الحقل `accessToken` فارغ ويعرض «أدخل رمز الاستضافة الذي أنشأته» \| VERIFIED \|"`` | — |
| [SRC-65AAF94960-L000017](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L17) | 17 | `"\| سؤال «ما عاصمة مصر؟» في الوضع الافتراضي الظاهر «بحث معمّق» \| فشل قبل استرجاع إجابة أو مصادر \| FAILED / BLOCKED \|"` | — |
| [SRC-65AAF94960-L000018](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L18) | 18 | `"\| نص الخطأ \| «رمز الوصول غير صحيح أو غير محفوظ. راجع رمز التطبيق المستضاف.» \| VERIFIED \|"` | — |
| [SRC-65AAF94960-L000019](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L19) | 19 | `"\| البحث عن الموقع الرسمي لـ OpenAI في «الأحدث الآن» \| لم يُنفذ بسبب حاجز المصادقة \| NOT_RUN \|"` | — |
| [SRC-65AAF94960-L000020](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L20) | 20 | `"\| سؤال بحث معمّق إضافي \| لم يُنفذ بسبب حاجز المصادقة \| NOT_RUN \|"` | — |
| [SRC-65AAF94960-L000021](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L21) | 21 | ``"\| `GET /api/health` \| `ok=true` \| VERIFIED — لكنه لا يثبت صلاحية البحث الحي \|"`` | — |
| [SRC-65AAF94960-L000022](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L22) | 22 | ``"\| هوية البناء \| `build.sha=unknown`, `sha_status=unknown`, `sha_source=unknown` \| BLOCKED / NOT VERIFIED \|"`` | — |
| [SRC-65AAF94960-L000023](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L23) | 23 | ``"\| فحص الشبكة الحي \| `live_network_checks_performed=false` \| NOT_RUN \|"`` | — |
| [SRC-65AAF94960-L000024](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L24) | 24 | `""` | — |
| [SRC-65AAF94960-L000025](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L25) | 25 | `"## تفسير الاستجابة الصحية"` | — |
| [SRC-65AAF94960-L000026](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L26) | 26 | ``"يصرّح رد الصحة بأن `web_search_ready` يعني أن الاعتماديات قابلة للاستيراد، وليس أن مزود البحث متصل؛ وأن `language_model_configured` يعني وجود بيانات اعتماد، وليس نجاح إكمال طلب. ويعرض مصادر منها DuckDuckGo HTML وBing RSS وGoogle News RSS كمدعومة، بينما يعرض DeepSeek/Brave/Tavily على أنها مشروطة الإعداد، ويعرض OpenRouter server-side live web search على أنه معطل. هذه أوصاف إعداد وليست اختبارات اتصال."`` | — |
| [SRC-65AAF94960-L000027](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L27) | 27 | `""` | — |
| [SRC-65AAF94960-L000028](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L28) | 28 | `"## السبب والحالة"` | — |
| [SRC-65AAF94960-L000029](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L29) | 29 | `"- **OMR-LIVE-004 — PARTIAL / BLOCKED:** اختبار الطلبات المحمية يتوقف عند المصادقة. السبب الدقيق وراء عدم وجود الرمز في ملف المتصفح الاختباري هو اختلاف سياق التخزين، لا دليل على فساد الرمز نفسه."` | — |
| [SRC-65AAF94960-L000030](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L30) | 30 | ``"- **OMR-LIVE-005 — CODE/CI FIXED_AND_TESTED; HOST_CONFIGURATION_PENDING:** إصلاح Dockerfile الذي يقرأ `PUBLIC_OMARAI_BUILD_SHA` موجود في #98، لكن المضيف ما زال يعرض SHA مجهولًا. يلزم تعيين متغير الإصدار العام إلى SHA الكامل المعتمد وإعادة البناء/النشر من مالك الاستضافة، ثم التحقق من التطابق. لا تضع أي أسرار في متغير الإصدار."`` | — |
| [SRC-65AAF94960-L000031](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L31) | 31 | ``"- لا يجوز اعتبار نجاح CI أو `ok=true` إثباتًا لصحة البحث أو الإجابات في الإنتاج."`` | — |
| [SRC-65AAF94960-L000032](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L32) | 32 | `""` | — |
| [SRC-65AAF94960-L000033](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L33) | 33 | `"## الخطوات اللازمة للإغلاق"` | — |
| [SRC-65AAF94960-L000034](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L34) | 34 | `"1. افتح جلسة إعداد ملف المتصفح الآمنة من الرابط الذي يوفره ChatGPT، على الموقع المستضاف."` | — |
| [SRC-65AAF94960-L000035](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L35) | 35 | `"2. أدخل رمز الوصول بنفسك في حقل التطبيق، واحفظه داخل ملف المتصفح الاختباري. **لا ترسل الرمز في المحادثة ولا تضعه في سجل GitHub.**"` | — |
| [SRC-65AAF94960-L000036](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L36) | 36 | `"3. أعد اختبار سؤال معرفي بسيط، ثم بحث الموقع الرسمي في وضع «الأحدث الآن»، ثم بحث معمّق؛ سجل حالة الطلب وروابط المصادر الفعلية."` | — |
| [SRC-65AAF94960-L000037](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L37) | 37 | ``"4. راجع إعدادات SnapDeploy لتعيين `PUBLIC_OMARAI_BUILD_SHA` إلى SHA الكامل النهائي المعتمد، ثم أعد البناء/النشر عبر مسار النشر المعتاد، وبعدها تحقق أن `/api/health` يعرض SHA المطابق. هذا التقرير لا يغير إعدادات المضيف ولا ينشر."`` | — |
| [SRC-65AAF94960-L000038](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L38) | 38 | `"5. لا تعلن القبول النهائي حتى تنجح هذه الاختبارات وتوثق مصادر حقيقية قابلة للفتح، أو تسجل كل عائق متبقٍ بوضوح."` | — |
| [SRC-65AAF94960-L000039](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L39) | 39 | `""` | — |
| [SRC-65AAF94960-L000040](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L40) | 40 | `"## حدود العمل"` | — |
| [SRC-65AAF94960-L000041](../../artifacts/OMARAI-HOSTED-ACCEPTANCE-2026-10-27-AR.md#L41) | 41 | `"لم تُقرأ أو تُكشف أسرار، ولم تُغير إعدادات الاستضافة، ولم يُنفذ نشر أو إجراء مدفوع. تم استخدام المتصفح للقراءة والاختبار فقط."` | — |
## واجهة سطر الأوامر

### FILE-14C6359E27 — [cli/__init__.py](../../cli/__init__.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-14C6359E27-L000001](../../cli/__init__.py#L1) | 1 | `"\"\"\"Omarai command-line package.\"\"\""` | — |
## واجهة سطر الأوامر

### FILE-9C97DF51AC — [cli/omarai.py](../../cli/omarai.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-9C97DF51AC-L000001](../../cli/omarai.py#L1) | 1 | `"\"\"\"Command-line interface for Omarai.\"\"\""` | — |
| [SRC-9C97DF51AC-L000002](../../cli/omarai.py#L2) | 2 | `"import argparse"` | — |
| [SRC-9C97DF51AC-L000003](../../cli/omarai.py#L3) | 3 | `"import json"` | — |
| [SRC-9C97DF51AC-L000004](../../cli/omarai.py#L4) | 4 | `""` | — |
| [SRC-9C97DF51AC-L000005](../../cli/omarai.py#L5) | 5 | `"from agents.omarai import LeadStore, analyze"` | — |
| [SRC-9C97DF51AC-L000006](../../cli/omarai.py#L6) | 6 | `"from api.omarai import serve"` | — |
| [SRC-9C97DF51AC-L000007](../../cli/omarai.py#L7) | 7 | `""` | — |
| [SRC-9C97DF51AC-L000008](../../cli/omarai.py#L8) | 8 | `""` | — |
| [SRC-9C97DF51AC-L000009](../../cli/omarai.py#L9) | 9 | `"def main():"` | — |
| [SRC-9C97DF51AC-L000010](../../cli/omarai.py#L10) | 10 | `"    parser=argparse.ArgumentParser(prog=\"omarai\",description=\"Arabic lead-intent helper\")"` | — |
| [SRC-9C97DF51AC-L000011](../../cli/omarai.py#L11) | 11 | `"    sub=parser.add_subparsers(dest=\"command\",required=True)"` | — |
| [SRC-9C97DF51AC-L000012](../../cli/omarai.py#L12) | 12 | `"    p=sub.add_parser(\"analyze\")"` | — |
| [SRC-9C97DF51AC-L000013](../../cli/omarai.py#L13) | 13 | `"    p.add_argument(\"--text\",required=True)"` | — |
| [SRC-9C97DF51AC-L000014](../../cli/omarai.py#L14) | 14 | `"    p.add_argument(\"--product\",default=\"\")"` | — |
| [SRC-9C97DF51AC-L000015](../../cli/omarai.py#L15) | 15 | `"    p.add_argument(\"--location\",default=\"\")"` | — |
| [SRC-9C97DF51AC-L000016](../../cli/omarai.py#L16) | 16 | `"    p=sub.add_parser(\"serve\")"` | — |
| [SRC-9C97DF51AC-L000017](../../cli/omarai.py#L17) | 17 | `"    p.add_argument(\"--host\",default=\"127.0.0.1\")"` | — |
| [SRC-9C97DF51AC-L000018](../../cli/omarai.py#L18) | 18 | `"    p.add_argument(\"--port\",type=int,default=8765)"` | — |
| [SRC-9C97DF51AC-L000019](../../cli/omarai.py#L19) | 19 | `"    p=sub.add_parser(\"import-csv\")"` | — |
| [SRC-9C97DF51AC-L000020](../../cli/omarai.py#L20) | 20 | `"    p.add_argument(\"--file\",required=True)"` | — |
| [SRC-9C97DF51AC-L000021](../../cli/omarai.py#L21) | 21 | `"    p=sub.add_parser(\"list\")"` | — |
| [SRC-9C97DF51AC-L000022](../../cli/omarai.py#L22) | 22 | `"    p.add_argument(\"--limit\",type=int,default=100)"` | — |
| [SRC-9C97DF51AC-L000023](../../cli/omarai.py#L23) | 23 | `"    p.add_argument(\"--status\")"` | — |
| [SRC-9C97DF51AC-L000024](../../cli/omarai.py#L24) | 24 | `"    p=sub.add_parser(\"export-csv\")"` | — |
| [SRC-9C97DF51AC-L000025](../../cli/omarai.py#L25) | 25 | `"    p.add_argument(\"--file\",required=True)"` | — |
| [SRC-9C97DF51AC-L000026](../../cli/omarai.py#L26) | 26 | `"    args=parser.parse_args()"` | — |
| [SRC-9C97DF51AC-L000027](../../cli/omarai.py#L27) | 27 | `"    if args.command==\"analyze\":"` | — |
| [SRC-9C97DF51AC-L000028](../../cli/omarai.py#L28) | 28 | `"        result=analyze(args.text,[x.strip() for x in args.product.split(\",\") if x.strip()],[x.strip() for x in args.location.split(\",\") if x.strip()])"` | — |
| [SRC-9C97DF51AC-L000029](../../cli/omarai.py#L29) | 29 | `"        print(json.dumps(result,ensure_ascii=False,indent=2))"` | — |
| [SRC-9C97DF51AC-L000030](../../cli/omarai.py#L30) | 30 | `"        return"` | — |
| [SRC-9C97DF51AC-L000031](../../cli/omarai.py#L31) | 31 | `"    store=LeadStore()"` | — |
| [SRC-9C97DF51AC-L000032](../../cli/omarai.py#L32) | 32 | `"    if args.command==\"serve\":"` | — |
| [SRC-9C97DF51AC-L000033](../../cli/omarai.py#L33) | 33 | `"        serve(args.host,args.port)"` | — |
| [SRC-9C97DF51AC-L000034](../../cli/omarai.py#L34) | 34 | `"    elif args.command==\"import-csv\":"` | — |
| [SRC-9C97DF51AC-L000035](../../cli/omarai.py#L35) | 35 | `"        print(json.dumps(store.import_csv(args.file),ensure_ascii=False,indent=2))"` | — |
| [SRC-9C97DF51AC-L000036](../../cli/omarai.py#L36) | 36 | `"    elif args.command==\"list\":"` | — |
| [SRC-9C97DF51AC-L000037](../../cli/omarai.py#L37) | 37 | `"        print(json.dumps(store.list(args.status,args.limit),ensure_ascii=False,indent=2))"` | — |
| [SRC-9C97DF51AC-L000038](../../cli/omarai.py#L38) | 38 | `"    elif args.command==\"export-csv\":"` | — |
| [SRC-9C97DF51AC-L000039](../../cli/omarai.py#L39) | 39 | `"        print(f\"Exported {store.export_csv(args.file)} leads to {args.file}\")"` | — |
| [SRC-9C97DF51AC-L000040](../../cli/omarai.py#L40) | 40 | `"if __name__==\"__main__\":"` | — |
| [SRC-9C97DF51AC-L000041](../../cli/omarai.py#L41) | 41 | `"    main()"` | — |
## إعدادات وتشغيل

### FILE-DD2C0EB6EA — [Dockerfile](../../Dockerfile#L1)

- النوع: **Dockerfile**
- نطاق الفهرسة: جرد الملف + أسماء إعدادات عامة إن وجدت

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-DD2C0EB6EA-L000001](../../Dockerfile#L1) | 1 | `"FROM python:3.12-slim"` | — |
| [SRC-DD2C0EB6EA-L000002](../../Dockerfile#L2) | 2 | `""` | — |
| [SRC-DD2C0EB6EA-L000003](../../Dockerfile#L3) | 3 | `"ARG OMARAI_BUILD_SHA=unknown"` | — |
| [SRC-DD2C0EB6EA-L000004](../../Dockerfile#L4) | 4 | `"ARG PUBLIC_OMARAI_BUILD_SHA=unknown"` | — |
| [SRC-DD2C0EB6EA-L000005](../../Dockerfile#L5) | 5 | `"ENV PYTHONDONTWRITEBYTECODE=1 \\"` | — |
| [SRC-DD2C0EB6EA-L000006](../../Dockerfile#L6) | 6 | `"    PYTHONUNBUFFERED=1 \\"` | — |
| [SRC-DD2C0EB6EA-L000007](../../Dockerfile#L7) | 7 | `"    PIP_DISABLE_PIP_VERSION_CHECK=1"` | — |
| [SRC-DD2C0EB6EA-L000008](../../Dockerfile#L8) | 8 | `""` | — |
| [SRC-DD2C0EB6EA-L000009](../../Dockerfile#L9) | 9 | `"WORKDIR /app"` | — |
| [SRC-DD2C0EB6EA-L000010](../../Dockerfile#L10) | 10 | `"COPY pyproject.toml README.md ./"` | — |
| [SRC-DD2C0EB6EA-L000011](../../Dockerfile#L11) | 11 | `"COPY agents ./agents"` | — |
| [SRC-DD2C0EB6EA-L000012](../../Dockerfile#L12) | 12 | `"COPY api ./api"` | — |
| [SRC-DD2C0EB6EA-L000013](../../Dockerfile#L13) | 13 | `"COPY cli ./cli"` | — |
| [SRC-DD2C0EB6EA-L000014](../../Dockerfile#L14) | 14 | `"COPY web ./web"` | — |
| [SRC-DD2C0EB6EA-L000015](../../Dockerfile#L15) | 15 | `""` | — |
| [SRC-DD2C0EB6EA-L000016](../../Dockerfile#L16) | 16 | `"RUN python -m pip install --no-cache-dir ."` | — |
| [SRC-DD2C0EB6EA-L000017](../../Dockerfile#L17) | 17 | `"RUN python -c \"import os; from pathlib import Path; import api.omarai; values=(os.getenv('OMARAI_BUILD_SHA',''), os.getenv('PUBLIC_OMARAI_BUILD_SHA','')); valid=lambda value: len(value.strip())==40 and all(char in '0123456789abcdef' for char in value.strip().lower()); sha=next((value.strip().lower() for value in values if valid(value)), 'unknown'); Path(api.omarai.__file__).resolve().parents[1].joinpath('BUILD_SHA').write_text(sha, encoding='ascii')\""` | — |
| [SRC-DD2C0EB6EA-L000018](../../Dockerfile#L18) | 18 | `""` | — |
| [SRC-DD2C0EB6EA-L000019](../../Dockerfile#L19) | 19 | `"EXPOSE 8000"` | — |
| [SRC-DD2C0EB6EA-L000020](../../Dockerfile#L20) | 20 | `"CMD [\"sh\", \"-c\", \"python -m cli.omarai serve --host 0.0.0.0 --port ${PORT:-8000}\"]"` | — |
## وثائق وفهرسة

### FILE-792A9A235D — [docs/ANSWER_QUALITY_BENCHMARK_AR.md](../ANSWER_QUALITY_BENCHMARK_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-792A9A235D-L000001](../ANSWER_QUALITY_BENCHMARK_AR.md#L1) | 1 | `"# معيار تقييم جودة الإجابة (عدائي / Red-Team)"` | — |
| [SRC-792A9A235D-L000002](../ANSWER_QUALITY_BENCHMARK_AR.md#L2) | 2 | `""` | — |
| [SRC-792A9A235D-L000003](../ANSWER_QUALITY_BENCHMARK_AR.md#L3) | 3 | `"**المعرّف:** OMARAI-REDTEAM-001  "` | — |
| [SRC-792A9A235D-L000004](../ANSWER_QUALITY_BENCHMARK_AR.md#L4) | 4 | `"**الإصدار:** 1.1.0 (تصحيح أمثلة الحالة + بروتوكول المقارنة)  "` | — |
| [SRC-792A9A235D-L000005](../ANSWER_QUALITY_BENCHMARK_AR.md#L5) | 5 | ``"**مرجع الكود عند التصميم:** `ac05f4777f140694b285c5364e6c3875fdecdae6` (main)"`` | — |
| [SRC-792A9A235D-L000006](../ANSWER_QUALITY_BENCHMARK_AR.md#L6) | 6 | `""` | — |
| [SRC-792A9A235D-L000007](../ANSWER_QUALITY_BENCHMARK_AR.md#L7) | 7 | `"هذا المجلد يوفّر **مجموعة تقييم قابلة لإعادة التشغيل** لفحص فهم عمرai، استراتيجية البحث، استخدام الأدلة، التعامل مع عدم اليقين، والأمان."` | — |
| [SRC-792A9A235D-L000008](../ANSWER_QUALITY_BENCHMARK_AR.md#L8) | 8 | `""` | — |
| [SRC-792A9A235D-L000009](../ANSWER_QUALITY_BENCHMARK_AR.md#L9) | 9 | ``"> **مهم:** اختبار `tests/test_answer_quality_corpus.py` يتحقق فقط من **سلامة بنية** ملف الحالات.  "`` | — |
| [SRC-792A9A235D-L000010](../ANSWER_QUALITY_BENCHMARK_AR.md#L10) | 10 | `"> نجاح هذا الاختبار **لا يعني** أن عمرai أجاب بشكل صحيح على أي حالة استدلال."` | — |
| [SRC-792A9A235D-L000011](../ANSWER_QUALITY_BENCHMARK_AR.md#L11) | 11 | `""` | — |
| [SRC-792A9A235D-L000012](../ANSWER_QUALITY_BENCHMARK_AR.md#L12) | 12 | ``"لا يعدّل هذا المعيار ملفات الإنتاج (`agents/`، `api/`، `web/`)."`` | — |
| [SRC-792A9A235D-L000013](../ANSWER_QUALITY_BENCHMARK_AR.md#L13) | 13 | `""` | — |
| [SRC-792A9A235D-L000014](../ANSWER_QUALITY_BENCHMARK_AR.md#L14) | 14 | `"## الملفات"` | — |
| [SRC-792A9A235D-L000015](../ANSWER_QUALITY_BENCHMARK_AR.md#L15) | 15 | `""` | — |
| [SRC-792A9A235D-L000016](../ANSWER_QUALITY_BENCHMARK_AR.md#L16) | 16 | `"\| الملف \| الوظيفة \|"` | — |
| [SRC-792A9A235D-L000017](../ANSWER_QUALITY_BENCHMARK_AR.md#L17) | 17 | `"\|--------\|---------\|"` | — |
| [SRC-792A9A235D-L000018](../ANSWER_QUALITY_BENCHMARK_AR.md#L18) | 18 | ``"\| `tests/fixtures/answer_quality_cases.json` \| ذخيرة الحالات (45) مع تجهيزات أدلة عند الحاجة \|"`` | — |
| [SRC-792A9A235D-L000019](../ANSWER_QUALITY_BENCHMARK_AR.md#L19) | 19 | ``"\| `tests/test_answer_quality_corpus.py` \| تحقق آلي حتمي من البنية (بدون شبكة) \|"`` | — |
| [SRC-792A9A235D-L000020](../ANSWER_QUALITY_BENCHMARK_AR.md#L20) | 20 | ``"\| `scripts/run_answer_quality_benchmark.py` \| تشغيل validate / live اختياري (stdlib) \|"`` | — |
| [SRC-792A9A235D-L000021](../ANSWER_QUALITY_BENCHMARK_AR.md#L21) | 21 | ``"\| `docs/ANSWER_QUALITY_BENCHMARK_AR.md` \| بروتوكول التقييم والتسجيل (هذا الملف) \|"`` | — |
| [SRC-792A9A235D-L000022](../ANSWER_QUALITY_BENCHMARK_AR.md#L22) | 22 | `""` | — |
| [SRC-792A9A235D-L000023](../ANSWER_QUALITY_BENCHMARK_AR.md#L23) | 23 | ``"## الاستراتيجيات المسموحة في الحقل `expected_strategy`"`` | — |
| [SRC-792A9A235D-L000024](../ANSWER_QUALITY_BENCHMARK_AR.md#L24) | 24 | `""` | — |
| [SRC-792A9A235D-L000025](../ANSWER_QUALITY_BENCHMARK_AR.md#L25) | 25 | `"مستمدة من سلوك المستودع الفعلي (موجّه القدرات المحلي، البحث، التوضيح):"` | — |
| [SRC-792A9A235D-L000026](../ANSWER_QUALITY_BENCHMARK_AR.md#L26) | 26 | `""` | — |
| [SRC-792A9A235D-L000027](../ANSWER_QUALITY_BENCHMARK_AR.md#L27) | 27 | `"\| القيمة \| المعنى العملي \|"` | — |
| [SRC-792A9A235D-L000028](../ANSWER_QUALITY_BENCHMARK_AR.md#L28) | 28 | `"\|--------\|----------------\|"` | — |
| [SRC-792A9A235D-L000029](../ANSWER_QUALITY_BENCHMARK_AR.md#L29) | 29 | ``"\| `local` \| إجابة محلية/قواعد (مثل قدرات عمرai أو تسجيل العملاء) دون بحث ويب \|"`` | — |
| [SRC-792A9A235D-L000030](../ANSWER_QUALITY_BENCHMARK_AR.md#L30) | 30 | ``"\| `model_no_search` \| إجابة نموذج بلا بحث ويب (تحية، معرفة عامة مستقرة) \|"`` | — |
| [SRC-792A9A235D-L000031](../ANSWER_QUALITY_BENCHMARK_AR.md#L31) | 31 | ``"\| `web_search` \| يتطلب بحثًا عامًا أو استرجاع صفحات \|"`` | — |
| [SRC-792A9A235D-L000032](../ANSWER_QUALITY_BENCHMARK_AR.md#L32) | 32 | ``"\| `clarify` \| الطلب غامض ويجب طلب توضيح قبل إجابة قطعية \|"`` | — |
| [SRC-792A9A235D-L000033](../ANSWER_QUALITY_BENCHMARK_AR.md#L33) | 33 | `""` | — |
| [SRC-792A9A235D-L000034](../ANSWER_QUALITY_BENCHMARK_AR.md#L34) | 34 | ``"## أوضاع التقييم `evaluation_mode`"`` | — |
| [SRC-792A9A235D-L000035](../ANSWER_QUALITY_BENCHMARK_AR.md#L35) | 35 | `""` | — |
| [SRC-792A9A235D-L000036](../ANSWER_QUALITY_BENCHMARK_AR.md#L36) | 36 | `"\| الوضع \| متى يُستخدم \|"` | — |
