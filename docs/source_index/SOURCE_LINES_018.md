# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **018**
- سجلات الأسطر: **800**
- النطاق: SRC-EEF2E6447C-L000019 إلى SRC-EEF2E6447C-L000818
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## واجهات API

### FILE-EEF2E6447C — [api/omarai.py](../../api/omarai.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-EEF2E6447C-L000019](../../api/omarai.py#L19) | 19 | `""` | — |
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
| [SRC-EEF2E6447C-L000208](../../api/omarai.py#L208) | 208 | `"DEFAULT_HTTP_CONNECTION_LIMIT = 32"` | — |
| [SRC-EEF2E6447C-L000209](../../api/omarai.py#L209) | 209 | `"MAX_HTTP_CONNECTION_LIMIT = 128"` | — |
| [SRC-EEF2E6447C-L000210](../../api/omarai.py#L210) | 210 | `""` | — |
| [SRC-EEF2E6447C-L000211](../../api/omarai.py#L211) | 211 | `""` | — |
| [SRC-EEF2E6447C-L000212](../../api/omarai.py#L212) | 212 | `"def _configured_http_connection_limit() -> int:"` | — |
| [SRC-EEF2E6447C-L000213](../../api/omarai.py#L213) | 213 | `"    \"\"\"Return the bounded number of live HTTP handler threads for this process.\"\"\""` | — |
| [SRC-EEF2E6447C-L000214](../../api/omarai.py#L214) | 214 | `"    try:"` | — |
| [SRC-EEF2E6447C-L000215](../../api/omarai.py#L215) | 215 | `"        configured = int(os.getenv(\"OMARAI_MAX_CONCURRENT_HTTP_CONNECTIONS\", \"32\").strip())"` | — |
| [SRC-EEF2E6447C-L000216](../../api/omarai.py#L216) | 216 | `"    except ValueError:"` | — |
| [SRC-EEF2E6447C-L000217](../../api/omarai.py#L217) | 217 | `"        configured = DEFAULT_HTTP_CONNECTION_LIMIT"` | — |
| [SRC-EEF2E6447C-L000218](../../api/omarai.py#L218) | 218 | `"    return max(1, min(configured, MAX_HTTP_CONNECTION_LIMIT))"` | — |
| [SRC-EEF2E6447C-L000219](../../api/omarai.py#L219) | 219 | `""` | — |
| [SRC-EEF2E6447C-L000220](../../api/omarai.py#L220) | 220 | `""` | — |
| [SRC-EEF2E6447C-L000221](../../api/omarai.py#L221) | 221 | `"BUILD_SHA_FILE = Path(__file__).resolve().parents[1] / \"BUILD_SHA\""` | — |
| [SRC-EEF2E6447C-L000222](../../api/omarai.py#L222) | 222 | `"_PLATFORM_BUILD_SHA_ENVIRONMENTS = ("` | — |
| [SRC-EEF2E6447C-L000223](../../api/omarai.py#L223) | 223 | `"    (\"RAILWAY_GIT_COMMIT_SHA\", \"platform:railway\"),"` | — |
| [SRC-EEF2E6447C-L000224](../../api/omarai.py#L224) | 224 | `"    (\"RENDER_GIT_COMMIT\", \"platform:render\"),"` | — |
| [SRC-EEF2E6447C-L000225](../../api/omarai.py#L225) | 225 | `")"` | — |
| [SRC-EEF2E6447C-L000226](../../api/omarai.py#L226) | 226 | `""` | — |
| [SRC-EEF2E6447C-L000227](../../api/omarai.py#L227) | 227 | `""` | — |
| [SRC-EEF2E6447C-L000228](../../api/omarai.py#L228) | 228 | `"def _valid_build_sha(value: str) -> bool:"` | — |
| [SRC-EEF2E6447C-L000229](../../api/omarai.py#L229) | 229 | `"    candidate = value.strip().lower()"` | — |
| [SRC-EEF2E6447C-L000230](../../api/omarai.py#L230) | 230 | `"    return len(candidate) == 40 and all(char in \"0123456789abcdef\" for char in candidate)"` | — |
| [SRC-EEF2E6447C-L000231](../../api/omarai.py#L231) | 231 | `""` | — |
| [SRC-EEF2E6447C-L000232](../../api/omarai.py#L232) | 232 | `""` | — |
| [SRC-EEF2E6447C-L000233](../../api/omarai.py#L233) | 233 | `"def _build_identity() -> tuple[str, str]:"` | — |
| [SRC-EEF2E6447C-L000234](../../api/omarai.py#L234) | 234 | `"    \"\"\"Prefer immutable image metadata, then documented hosting-provided Git SHAs.\"\"\""` | — |
| [SRC-EEF2E6447C-L000235](../../api/omarai.py#L235) | 235 | `"    try:"` | — |
| [SRC-EEF2E6447C-L000236](../../api/omarai.py#L236) | 236 | `"        baked = BUILD_SHA_FILE.read_text(encoding=\"ascii\").strip().lower()"` | — |
| [SRC-EEF2E6447C-L000237](../../api/omarai.py#L237) | 237 | `"    except (OSError, UnicodeError):"` | — |
| [SRC-EEF2E6447C-L000238](../../api/omarai.py#L238) | 238 | `"        baked = \"\""` | — |
| [SRC-EEF2E6447C-L000239](../../api/omarai.py#L239) | 239 | `"    if _valid_build_sha(baked):"` | — |
| [SRC-EEF2E6447C-L000240](../../api/omarai.py#L240) | 240 | `"        return baked, \"image_baked\""` | — |
| [SRC-EEF2E6447C-L000241](../../api/omarai.py#L241) | 241 | `""` | — |
| [SRC-EEF2E6447C-L000242](../../api/omarai.py#L242) | 242 | `"    for environment_name, source in _PLATFORM_BUILD_SHA_ENVIRONMENTS:"` | — |
| [SRC-EEF2E6447C-L000243](../../api/omarai.py#L243) | 243 | `"        candidate = os.getenv(environment_name, \"\").strip().lower()"` | — |
| [SRC-EEF2E6447C-L000244](../../api/omarai.py#L244) | 244 | `"        if _valid_build_sha(candidate):"` | — |
| [SRC-EEF2E6447C-L000245](../../api/omarai.py#L245) | 245 | `"            return candidate, source"` | — |
| [SRC-EEF2E6447C-L000246](../../api/omarai.py#L246) | 246 | `"    return \"unknown\", \"unknown\""` | — |
| [SRC-EEF2E6447C-L000247](../../api/omarai.py#L247) | 247 | `""` | — |
| [SRC-EEF2E6447C-L000248](../../api/omarai.py#L248) | 248 | `""` | — |
| [SRC-EEF2E6447C-L000249](../../api/omarai.py#L249) | 249 | `"def _build_sha() -> str:"` | — |
| [SRC-EEF2E6447C-L000250](../../api/omarai.py#L250) | 250 | `"    \"\"\"Return a validated source SHA, or 'unknown' when no trusted build evidence exists.\"\"\""` | — |
| [SRC-EEF2E6447C-L000251](../../api/omarai.py#L251) | 251 | `"    return _build_identity()[0]"` | — |
| [SRC-EEF2E6447C-L000252](../../api/omarai.py#L252) | 252 | `""` | — |
| [SRC-EEF2E6447C-L000253](../../api/omarai.py#L253) | 253 | `""` | — |
| [SRC-EEF2E6447C-L000254](../../api/omarai.py#L254) | 254 | `"class Handler(BaseHTTPRequestHandler):"` | — |
| [SRC-EEF2E6447C-L000255](../../api/omarai.py#L255) | 255 | `"    def setup(self):"` | — |
| [SRC-EEF2E6447C-L000256](../../api/omarai.py#L256) | 256 | `"        \"\"\"Install a reader with a strict deadline for the request line and headers.\"\"\""` | — |
| [SRC-EEF2E6447C-L000257](../../api/omarai.py#L257) | 257 | `"        self.connection = self.request"` | — |
| [SRC-EEF2E6447C-L000258](../../api/omarai.py#L258) | 258 | `"        if self.timeout is not None:"` | — |
| [SRC-EEF2E6447C-L000259](../../api/omarai.py#L259) | 259 | `"            self.connection.settimeout(self.timeout)"` | — |
| [SRC-EEF2E6447C-L000260](../../api/omarai.py#L260) | 260 | `"        self._request_header_deadline = None"` | — |
| [SRC-EEF2E6447C-L000261](../../api/omarai.py#L261) | 261 | `"        self.rfile = _DeadlineRequestReader(self.connection, self)"` | — |
| [SRC-EEF2E6447C-L000262](../../api/omarai.py#L262) | 262 | `"        self.wfile = self.connection.makefile(\"wb\", self.wbufsize)"` | — |
| [SRC-EEF2E6447C-L000263](../../api/omarai.py#L263) | 263 | `""` | — |
| [SRC-EEF2E6447C-L000264](../../api/omarai.py#L264) | 264 | `"    def handle_one_request(self):"` | — |
| [SRC-EEF2E6447C-L000265](../../api/omarai.py#L265) | 265 | `"        timeout = max("` | — |
| [SRC-EEF2E6447C-L000266](../../api/omarai.py#L266) | 266 | `"            0.1,"` | — |
| [SRC-EEF2E6447C-L000267](../../api/omarai.py#L267) | 267 | `"            min("` | — |
| [SRC-EEF2E6447C-L000268](../../api/omarai.py#L268) | 268 | `"                float(REQUEST_HEADER_READ_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000269](../../api/omarai.py#L269) | 269 | `"                MAX_REQUEST_HEADER_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000270](../../api/omarai.py#L270) | 270 | `"            ),"` | — |
| [SRC-EEF2E6447C-L000271](../../api/omarai.py#L271) | 271 | `"        )"` | — |
| [SRC-EEF2E6447C-L000272](../../api/omarai.py#L272) | 272 | `"        self._request_header_deadline = time.monotonic() + timeout"` | — |
| [SRC-EEF2E6447C-L000273](../../api/omarai.py#L273) | 273 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000274](../../api/omarai.py#L274) | 274 | `"            super().handle_one_request()"` | — |
| [SRC-EEF2E6447C-L000275](../../api/omarai.py#L275) | 275 | `"        except TimeoutError:"` | — |
| [SRC-EEF2E6447C-L000276](../../api/omarai.py#L276) | 276 | `"            # Incomplete request line/headers are untrusted protocol input;"` | — |
| [SRC-EEF2E6447C-L000277](../../api/omarai.py#L277) | 277 | `"            # close the socket without trying to parse or answer a partial request."` | — |
| [SRC-EEF2E6447C-L000278](../../api/omarai.py#L278) | 278 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000279](../../api/omarai.py#L279) | 279 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000280](../../api/omarai.py#L280) | 280 | `"            self._request_header_deadline = None"` | — |
| [SRC-EEF2E6447C-L000281](../../api/omarai.py#L281) | 281 | `""` | — |
| [SRC-EEF2E6447C-L000282](../../api/omarai.py#L282) | 282 | `"    store = _lead_store_from_environment()"` | — |
| [SRC-EEF2E6447C-L000283](../../api/omarai.py#L283) | 283 | `"    _rate_lock = threading.Lock()"` | — |
| [SRC-EEF2E6447C-L000284](../../api/omarai.py#L284) | 284 | `"    _request_times: ClassVar[dict[str, deque[float]]] = defaultdict(deque)"` | — |
| [SRC-EEF2E6447C-L000285](../../api/omarai.py#L285) | 285 | `"    _rate_last_cleanup: ClassVar[float] = 0.0"` | — |
| [SRC-EEF2E6447C-L000286](../../api/omarai.py#L286) | 286 | `"    RATE_LIMIT_REQUESTS = 20"` | — |
| [SRC-EEF2E6447C-L000287](../../api/omarai.py#L287) | 287 | `"    RATE_LIMIT_WINDOW_SECONDS = 60"` | — |
| [SRC-EEF2E6447C-L000288](../../api/omarai.py#L288) | 288 | `"    RATE_LIMIT_CLEANUP_INTERVAL_SECONDS = 60"` | — |
| [SRC-EEF2E6447C-L000289](../../api/omarai.py#L289) | 289 | `"    # Reserve the final bucket for clients beyond the per-process tracking ceiling."` | — |
| [SRC-EEF2E6447C-L000290](../../api/omarai.py#L290) | 290 | `"    MAX_RATE_LIMIT_CLIENT_BUCKETS = 4096"` | — |
| [SRC-EEF2E6447C-L000291](../../api/omarai.py#L291) | 291 | `"    RATE_LIMIT_OVERFLOW_KEY = \"__omarai_overflow__\""` | — |
| [SRC-EEF2E6447C-L000292](../../api/omarai.py#L292) | 292 | `"    AGENT_CONCURRENCY_LIMIT = _configured_agent_concurrency_limit()"` | — |
| [SRC-EEF2E6447C-L000293](../../api/omarai.py#L293) | 293 | `"    _agent_semaphore = threading.BoundedSemaphore(AGENT_CONCURRENCY_LIMIT)"` | — |
| [SRC-EEF2E6447C-L000294](../../api/omarai.py#L294) | 294 | `""` | — |
| [SRC-EEF2E6447C-L000295](../../api/omarai.py#L295) | 295 | `"    def _run_bounded_agent_operation(self, operation):"` | — |
| [SRC-EEF2E6447C-L000296](../../api/omarai.py#L296) | 296 | `"        \"\"\"Run an expensive operation only when a process-local slot is available.\"\"\""` | — |
| [SRC-EEF2E6447C-L000297](../../api/omarai.py#L297) | 297 | `"        cls = type(self)"` | — |
| [SRC-EEF2E6447C-L000298](../../api/omarai.py#L298) | 298 | `"        if not cls._agent_semaphore.acquire(blocking=False):"` | — |
| [SRC-EEF2E6447C-L000299](../../api/omarai.py#L299) | 299 | `"            return self.respond("` | — |
| [SRC-EEF2E6447C-L000300](../../api/omarai.py#L300) | 300 | `"                503,"` | — |
| [SRC-EEF2E6447C-L000301](../../api/omarai.py#L301) | 301 | `"                {"` | — |
| [SRC-EEF2E6447C-L000302](../../api/omarai.py#L302) | 302 | `"                    \"error\": \"خدمة البحث مشغولة حاليًا؛ أعد المحاولة بعد قليل.\","` | — |
| [SRC-EEF2E6447C-L000303](../../api/omarai.py#L303) | 303 | `"                    \"retry_after_seconds\": 5,"` | — |
| [SRC-EEF2E6447C-L000304](../../api/omarai.py#L304) | 304 | `"                    \"process_concurrency_limit\": cls.AGENT_CONCURRENCY_LIMIT,"` | — |
| [SRC-EEF2E6447C-L000305](../../api/omarai.py#L305) | 305 | `"                },"` | — |
| [SRC-EEF2E6447C-L000306](../../api/omarai.py#L306) | 306 | `"            )"` | — |
| [SRC-EEF2E6447C-L000307](../../api/omarai.py#L307) | 307 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000308](../../api/omarai.py#L308) | 308 | `"            return self.respond(200, operation())"` | — |
| [SRC-EEF2E6447C-L000309](../../api/omarai.py#L309) | 309 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000310](../../api/omarai.py#L310) | 310 | `"            cls._agent_semaphore.release()"` | — |
| [SRC-EEF2E6447C-L000311](../../api/omarai.py#L311) | 311 | `""` | — |
| [SRC-EEF2E6447C-L000312](../../api/omarai.py#L312) | 312 | `"    def _authorized(self):"` | — |
| [SRC-EEF2E6447C-L000313](../../api/omarai.py#L313) | 313 | `"        \"\"\"Resolve the request identity from a verified token or loopback dev mode."` | — |
| [SRC-EEF2E6447C-L000314](../../api/omarai.py#L314) | 314 | `""` | — |
| [SRC-EEF2E6447C-L000315](../../api/omarai.py#L315) | 315 | `"        Request-body tenant IDs are never used to establish tenant context."` | — |
| [SRC-EEF2E6447C-L000316](../../api/omarai.py#L316) | 316 | `"        Public deployments always require a valid bearer credential."` | — |
| [SRC-EEF2E6447C-L000317](../../api/omarai.py#L317) | 317 | `"        \"\"\""` | — |
| [SRC-EEF2E6447C-L000318](../../api/omarai.py#L318) | 318 | `"        self._authenticated_principal = None"` | — |
| [SRC-EEF2E6447C-L000319](../../api/omarai.py#L319) | 319 | `"        supplied = self.headers.get(\"Authorization\", \"\")"` | — |
| [SRC-EEF2E6447C-L000320](../../api/omarai.py#L320) | 320 | `"        expected = os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000321](../../api/omarai.py#L321) | 321 | `"        if supplied.startswith(\"Bearer \"):"` | — |
| [SRC-EEF2E6447C-L000322](../../api/omarai.py#L322) | 322 | `"            token = supplied[7:].strip()"` | — |
| [SRC-EEF2E6447C-L000323](../../api/omarai.py#L323) | 323 | `"            if expected and hmac.compare_digest(token, expected):"` | — |
| [SRC-EEF2E6447C-L000324](../../api/omarai.py#L324) | 324 | `"                self._authenticated_principal = self.store.default_principal()"` | — |
| [SRC-EEF2E6447C-L000325](../../api/omarai.py#L325) | 325 | `"            else:"` | — |
| [SRC-EEF2E6447C-L000326](../../api/omarai.py#L326) | 326 | `"                self._authenticated_principal = self.store.resolve_api_token(token)"` | — |
| [SRC-EEF2E6447C-L000327](../../api/omarai.py#L327) | 327 | `"            return bool(self._authenticated_principal)"` | — |
| [SRC-EEF2E6447C-L000328](../../api/omarai.py#L328) | 328 | `""` | — |
| [SRC-EEF2E6447C-L000329](../../api/omarai.py#L329) | 329 | `"        if os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() != \"1\":"` | — |
| [SRC-EEF2E6447C-L000330](../../api/omarai.py#L330) | 330 | `"            try:"` | — |
| [SRC-EEF2E6447C-L000331](../../api/omarai.py#L331) | 331 | `"                if ipaddress.ip_address(self.client_address[0]).is_loopback:"` | — |
| [SRC-EEF2E6447C-L000332](../../api/omarai.py#L332) | 332 | `"                    self._authenticated_principal = self.store.default_principal()"` | — |
| [SRC-EEF2E6447C-L000333](../../api/omarai.py#L333) | 333 | `"                    return bool(self._authenticated_principal)"` | — |
| [SRC-EEF2E6447C-L000334](../../api/omarai.py#L334) | 334 | `"            except ValueError:"` | — |
| [SRC-EEF2E6447C-L000335](../../api/omarai.py#L335) | 335 | `"                pass"` | — |
| [SRC-EEF2E6447C-L000336](../../api/omarai.py#L336) | 336 | `"        return False"` | — |
| [SRC-EEF2E6447C-L000337](../../api/omarai.py#L337) | 337 | `""` | — |
| [SRC-EEF2E6447C-L000338](../../api/omarai.py#L338) | 338 | `"    def _allowed_origins(self):"` | — |
| [SRC-EEF2E6447C-L000339](../../api/omarai.py#L339) | 339 | `"        \"\"\"Return configured browser origins plus this service’s own origin."` | — |
| [SRC-EEF2E6447C-L000340](../../api/omarai.py#L340) | 340 | `""` | — |
| [SRC-EEF2E6447C-L000341](../../api/omarai.py#L341) | 341 | `"        OMARAI_ALLOWED_ORIGINS is a comma-separated list of trusted origins"` | — |
| [SRC-EEF2E6447C-L000342](../../api/omarai.py#L342) | 342 | `"        (scheme + host + optional port; no path and no wildcard)."` | — |
| [SRC-EEF2E6447C-L000343](../../api/omarai.py#L343) | 343 | `"        \"\"\""` | — |
| [SRC-EEF2E6447C-L000344](../../api/omarai.py#L344) | 344 | `"        configured = os.getenv(\"OMARAI_ALLOWED_ORIGINS\", \"\")"` | — |
| [SRC-EEF2E6447C-L000345](../../api/omarai.py#L345) | 345 | `"        origins = {"` | — |
| [SRC-EEF2E6447C-L000346](../../api/omarai.py#L346) | 346 | `"            item.strip().rstrip(\"/\")"` | — |
| [SRC-EEF2E6447C-L000347](../../api/omarai.py#L347) | 347 | `"            for item in configured.split(\",\")"` | — |
| [SRC-EEF2E6447C-L000348](../../api/omarai.py#L348) | 348 | `"            if item.strip()"` | — |
| [SRC-EEF2E6447C-L000349](../../api/omarai.py#L349) | 349 | `"        }"` | — |
| [SRC-EEF2E6447C-L000350](../../api/omarai.py#L350) | 350 | `"        if os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() == \"1\":"` | — |
| [SRC-EEF2E6447C-L000351](../../api/omarai.py#L351) | 351 | `"            # Host identifies the requested service origin. Do not derive allowed"` | — |
| [SRC-EEF2E6447C-L000352](../../api/omarai.py#L352) | 352 | `"            # origins from X-Forwarded-Host: direct clients can spoof that header"` | — |
| [SRC-EEF2E6447C-L000353](../../api/omarai.py#L353) | 353 | `"            # unless the reverse proxy is separately configured to overwrite it."` | — |
| [SRC-EEF2E6447C-L000354](../../api/omarai.py#L354) | 354 | `"            scheme = self.headers.get(\"X-Forwarded-Proto\", \"https\").split(\",\", 1)[0].strip().lower()"` | — |
| [SRC-EEF2E6447C-L000355](../../api/omarai.py#L355) | 355 | `"            host = self.headers.get(\"Host\", \"\").split(\",\", 1)[0].strip()"` | — |
| [SRC-EEF2E6447C-L000356](../../api/omarai.py#L356) | 356 | `"            if host:"` | — |
| [SRC-EEF2E6447C-L000357](../../api/omarai.py#L357) | 357 | `"                origins.add(f\"https://{host}\".rstrip(\"/\"))"` | — |
| [SRC-EEF2E6447C-L000358](../../api/omarai.py#L358) | 358 | `"                origins.add(f\"{scheme}://{host}\".rstrip(\"/\"))"` | — |
| [SRC-EEF2E6447C-L000359](../../api/omarai.py#L359) | 359 | `"        else:"` | — |
| [SRC-EEF2E6447C-L000360](../../api/omarai.py#L360) | 360 | `"            port = self.server.server_port"` | — |
| [SRC-EEF2E6447C-L000361](../../api/omarai.py#L361) | 361 | `"            origins.update("` | — |
| [SRC-EEF2E6447C-L000362](../../api/omarai.py#L362) | 362 | `"                {"` | — |
| [SRC-EEF2E6447C-L000363](../../api/omarai.py#L363) | 363 | `"                    f\"http://127.0.0.1:{port}\","` | — |
| [SRC-EEF2E6447C-L000364](../../api/omarai.py#L364) | 364 | `"                    f\"http://localhost:{port}\","` | — |
| [SRC-EEF2E6447C-L000365](../../api/omarai.py#L365) | 365 | `"                    f\"http://[::1]:{port}\","` | — |
| [SRC-EEF2E6447C-L000366](../../api/omarai.py#L366) | 366 | `"                }"` | — |
| [SRC-EEF2E6447C-L000367](../../api/omarai.py#L367) | 367 | `"            )"` | — |
| [SRC-EEF2E6447C-L000368](../../api/omarai.py#L368) | 368 | `"        return origins"` | — |
| [SRC-EEF2E6447C-L000369](../../api/omarai.py#L369) | 369 | `""` | — |
| [SRC-EEF2E6447C-L000370](../../api/omarai.py#L370) | 370 | `"    def _origin_allowed(self, origin):"` | — |
| [SRC-EEF2E6447C-L000371](../../api/omarai.py#L371) | 371 | `"        return bool(origin) and origin.rstrip(\"/\") in self._allowed_origins()"` | — |
| [SRC-EEF2E6447C-L000372](../../api/omarai.py#L372) | 372 | `""` | — |
| [SRC-EEF2E6447C-L000373](../../api/omarai.py#L373) | 373 | `"    def _rate_limit_client_key(self):"` | — |
| [SRC-EEF2E6447C-L000374](../../api/omarai.py#L374) | 374 | `"        \"\"\"Choose a rate-limit identity without trusting spoofable proxy headers by default."` | — |
| [SRC-EEF2E6447C-L000375](../../api/omarai.py#L375) | 375 | `""` | — |
| [SRC-EEF2E6447C-L000376](../../api/omarai.py#L376) | 376 | `"        Set OMARAI_TRUST_PROXY_HEADERS=1 only when the deployment's trusted reverse"` | — |
| [SRC-EEF2E6447C-L000377](../../api/omarai.py#L377) | 377 | `"        proxy appends the actual client IP as the rightmost X-Forwarded-For value."` | — |
| [SRC-EEF2E6447C-L000378](../../api/omarai.py#L378) | 378 | `"        \"\"\""` | — |
| [SRC-EEF2E6447C-L000379](../../api/omarai.py#L379) | 379 | `"        direct_ip = self.client_address[0]"` | — |
| [SRC-EEF2E6447C-L000380](../../api/omarai.py#L380) | 380 | `"        if os.getenv(\"OMARAI_TRUST_PROXY_HEADERS\", \"\").strip() != \"1\":"` | — |
| [SRC-EEF2E6447C-L000381](../../api/omarai.py#L381) | 381 | `"            return direct_ip"` | — |
| [SRC-EEF2E6447C-L000382](../../api/omarai.py#L382) | 382 | `"        forwarded = self.headers.get(\"X-Forwarded-For\", \"\")"` | — |
| [SRC-EEF2E6447C-L000383](../../api/omarai.py#L383) | 383 | `"        candidate = forwarded.rsplit(\",\", 1)[-1].strip() if forwarded else \"\""` | — |
| [SRC-EEF2E6447C-L000384](../../api/omarai.py#L384) | 384 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000385](../../api/omarai.py#L385) | 385 | `"            return str(ipaddress.ip_address(candidate))"` | — |
| [SRC-EEF2E6447C-L000386](../../api/omarai.py#L386) | 386 | `"        except ValueError:"` | — |
| [SRC-EEF2E6447C-L000387](../../api/omarai.py#L387) | 387 | `"            return direct_ip"` | — |
| [SRC-EEF2E6447C-L000388](../../api/omarai.py#L388) | 388 | `""` | — |
| [SRC-EEF2E6447C-L000389](../../api/omarai.py#L389) | 389 | `"    def _rate_limit_ok(self):"` | — |
| [SRC-EEF2E6447C-L000390](../../api/omarai.py#L390) | 390 | `"        client_ip = self._rate_limit_client_key()"` | — |
| [SRC-EEF2E6447C-L000391](../../api/omarai.py#L391) | 391 | `"        now = time.monotonic()"` | — |
| [SRC-EEF2E6447C-L000392](../../api/omarai.py#L392) | 392 | `"        cls = type(self)"` | — |
| [SRC-EEF2E6447C-L000393](../../api/omarai.py#L393) | 393 | `"        with self._rate_lock:"` | — |
| [SRC-EEF2E6447C-L000394](../../api/omarai.py#L394) | 394 | `"            # Periodically remove IP buckets whose entire sliding window has expired."` | — |
| [SRC-EEF2E6447C-L000395](../../api/omarai.py#L395) | 395 | `"            # Without this sweep, a public endpoint could retain one empty deque per"` | — |
| [SRC-EEF2E6447C-L000396](../../api/omarai.py#L396) | 396 | `"            # distinct client IP forever, even though the rate-limit window is 60 sec."` | — |
| [SRC-EEF2E6447C-L000397](../../api/omarai.py#L397) | 397 | `"            if now - cls._rate_last_cleanup >= cls.RATE_LIMIT_CLEANUP_INTERVAL_SECONDS:"` | — |
| [SRC-EEF2E6447C-L000398](../../api/omarai.py#L398) | 398 | `"                cutoff = now - cls.RATE_LIMIT_WINDOW_SECONDS"` | — |
| [SRC-EEF2E6447C-L000399](../../api/omarai.py#L399) | 399 | `"                for key, timestamps in list(cls._request_times.items()):"` | — |
| [SRC-EEF2E6447C-L000400](../../api/omarai.py#L400) | 400 | `"                    while timestamps and timestamps[0] <= cutoff:"` | — |
| [SRC-EEF2E6447C-L000401](../../api/omarai.py#L401) | 401 | `"                        timestamps.popleft()"` | — |
| [SRC-EEF2E6447C-L000402](../../api/omarai.py#L402) | 402 | `"                    if not timestamps:"` | — |
| [SRC-EEF2E6447C-L000403](../../api/omarai.py#L403) | 403 | `"                        cls._request_times.pop(key, None)"` | — |
| [SRC-EEF2E6447C-L000404](../../api/omarai.py#L404) | 404 | `"                cls._rate_last_cleanup = now"` | — |
| [SRC-EEF2E6447C-L000405](../../api/omarai.py#L405) | 405 | `""` | — |
| [SRC-EEF2E6447C-L000406](../../api/omarai.py#L406) | 406 | `"            if ("` | — |
| [SRC-EEF2E6447C-L000407](../../api/omarai.py#L407) | 407 | `"                client_ip not in cls._request_times"` | — |
| [SRC-EEF2E6447C-L000408](../../api/omarai.py#L408) | 408 | `"                and len(cls._request_times) >= max(1, cls.MAX_RATE_LIMIT_CLIENT_BUCKETS) - 1"` | — |
| [SRC-EEF2E6447C-L000409](../../api/omarai.py#L409) | 409 | `"            ):"` | — |
| [SRC-EEF2E6447C-L000410](../../api/omarai.py#L410) | 410 | `"                # Bound attacker-controlled cardinality. Excess identities share a"` | — |
| [SRC-EEF2E6447C-L000411](../../api/omarai.py#L411) | 411 | `"                # conservative overflow bucket instead of allocating one deque per IP."` | — |
| [SRC-EEF2E6447C-L000412](../../api/omarai.py#L412) | 412 | `"                client_ip = cls.RATE_LIMIT_OVERFLOW_KEY"` | — |
| [SRC-EEF2E6447C-L000413](../../api/omarai.py#L413) | 413 | `"            events = cls._request_times[client_ip]"` | — |
| [SRC-EEF2E6447C-L000414](../../api/omarai.py#L414) | 414 | `"            while events and now - events[0] >= cls.RATE_LIMIT_WINDOW_SECONDS:"` | — |
| [SRC-EEF2E6447C-L000415](../../api/omarai.py#L415) | 415 | `"                events.popleft()"` | — |
| [SRC-EEF2E6447C-L000416](../../api/omarai.py#L416) | 416 | `"            if len(events) >= cls.RATE_LIMIT_REQUESTS:"` | — |
| [SRC-EEF2E6447C-L000417](../../api/omarai.py#L417) | 417 | `"                return False"` | — |
| [SRC-EEF2E6447C-L000418](../../api/omarai.py#L418) | 418 | `"            events.append(now)"` | — |
| [SRC-EEF2E6447C-L000419](../../api/omarai.py#L419) | 419 | `"            return True"` | — |
| [SRC-EEF2E6447C-L000420](../../api/omarai.py#L420) | 420 | `""` | — |
| [SRC-EEF2E6447C-L000421](../../api/omarai.py#L421) | 421 | `"    def _read_request_body(self) -> bytes \| None:"` | — |
| [SRC-EEF2E6447C-L000422](../../api/omarai.py#L422) | 422 | `"        \"\"\"Read a bounded body with both idle and absolute wall-clock deadlines.\"\"\""` | — |
| [SRC-EEF2E6447C-L000423](../../api/omarai.py#L423) | 423 | `"        raw_size = self.headers.get(\"Content-Length\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000424](../../api/omarai.py#L424) | 424 | `"        if not raw_size or not raw_size.isascii() or not raw_size.isdecimal():"` | — |
| [SRC-EEF2E6447C-L000425](../../api/omarai.py#L425) | 425 | `"            self.respond(400, {\"error\": \"valid Content-Length is required\"})"` | — |
| [SRC-EEF2E6447C-L000426](../../api/omarai.py#L426) | 426 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000427](../../api/omarai.py#L427) | 427 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000428](../../api/omarai.py#L428) | 428 | `"            size = int(raw_size)"` | — |
| [SRC-EEF2E6447C-L000429](../../api/omarai.py#L429) | 429 | `"        except ValueError:"` | — |
| [SRC-EEF2E6447C-L000430](../../api/omarai.py#L430) | 430 | `"            self.respond(400, {\"error\": \"valid Content-Length is required\"})"` | — |
| [SRC-EEF2E6447C-L000431](../../api/omarai.py#L431) | 431 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000432](../../api/omarai.py#L432) | 432 | `"        if size <= 0:"` | — |
| [SRC-EEF2E6447C-L000433](../../api/omarai.py#L433) | 433 | `"            self.respond(400, {\"error\": \"request body is required\"})"` | — |
| [SRC-EEF2E6447C-L000434](../../api/omarai.py#L434) | 434 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000435](../../api/omarai.py#L435) | 435 | `"        if size > MAX_REQUEST_BODY_BYTES:"` | — |
| [SRC-EEF2E6447C-L000436](../../api/omarai.py#L436) | 436 | `"            self.respond(413, {\"error\": \"request too large\"})"` | — |
| [SRC-EEF2E6447C-L000437](../../api/omarai.py#L437) | 437 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000438](../../api/omarai.py#L438) | 438 | `""` | — |
| [SRC-EEF2E6447C-L000439](../../api/omarai.py#L439) | 439 | `"        total_timeout = max("` | — |
| [SRC-EEF2E6447C-L000440](../../api/omarai.py#L440) | 440 | `"            0.1,"` | — |
| [SRC-EEF2E6447C-L000441](../../api/omarai.py#L441) | 441 | `"            min("` | — |
| [SRC-EEF2E6447C-L000442](../../api/omarai.py#L442) | 442 | `"                float(REQUEST_BODY_READ_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000443](../../api/omarai.py#L443) | 443 | `"                MAX_REQUEST_BODY_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000444](../../api/omarai.py#L444) | 444 | `"            ),"` | — |
| [SRC-EEF2E6447C-L000445](../../api/omarai.py#L445) | 445 | `"        )"` | — |
| [SRC-EEF2E6447C-L000446](../../api/omarai.py#L446) | 446 | `"        idle_timeout = max("` | — |
| [SRC-EEF2E6447C-L000447](../../api/omarai.py#L447) | 447 | `"            0.1,"` | — |
| [SRC-EEF2E6447C-L000448](../../api/omarai.py#L448) | 448 | `"            min("` | — |
| [SRC-EEF2E6447C-L000449](../../api/omarai.py#L449) | 449 | `"                float(REQUEST_BODY_IDLE_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000450](../../api/omarai.py#L450) | 450 | `"                MAX_REQUEST_BODY_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000451](../../api/omarai.py#L451) | 451 | `"            ),"` | — |
| [SRC-EEF2E6447C-L000452](../../api/omarai.py#L452) | 452 | `"        )"` | — |
| [SRC-EEF2E6447C-L000453](../../api/omarai.py#L453) | 453 | `"        deadline = time.monotonic() + total_timeout"` | — |
| [SRC-EEF2E6447C-L000454](../../api/omarai.py#L454) | 454 | `"        previous_timeout = self.connection.gettimeout()"` | — |
| [SRC-EEF2E6447C-L000455](../../api/omarai.py#L455) | 455 | `"        body = bytearray()"` | — |
| [SRC-EEF2E6447C-L000456](../../api/omarai.py#L456) | 456 | `"        timed_out = False"` | — |
| [SRC-EEF2E6447C-L000457](../../api/omarai.py#L457) | 457 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000458](../../api/omarai.py#L458) | 458 | `"            while len(body) < size:"` | — |
| [SRC-EEF2E6447C-L000459](../../api/omarai.py#L459) | 459 | `"                remaining = deadline - time.monotonic()"` | — |
| [SRC-EEF2E6447C-L000460](../../api/omarai.py#L460) | 460 | `"                if remaining <= 0:"` | — |
| [SRC-EEF2E6447C-L000461](../../api/omarai.py#L461) | 461 | `"                    timed_out = True"` | — |
| [SRC-EEF2E6447C-L000462](../../api/omarai.py#L462) | 462 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000463](../../api/omarai.py#L463) | 463 | `"                self.connection.settimeout(min(idle_timeout, remaining))"` | — |
| [SRC-EEF2E6447C-L000464](../../api/omarai.py#L464) | 464 | `"                try:"` | — |
| [SRC-EEF2E6447C-L000465](../../api/omarai.py#L465) | 465 | `"                    # read1 performs at most one underlying read, letting us re-check"` | — |
| [SRC-EEF2E6447C-L000466](../../api/omarai.py#L466) | 466 | `"                    # the absolute deadline between body fragments."` | — |
| [SRC-EEF2E6447C-L000467](../../api/omarai.py#L467) | 467 | `"                    chunk = self.rfile.read1("` | — |
| [SRC-EEF2E6447C-L000468](../../api/omarai.py#L468) | 468 | `"                        min(size - len(body), REQUEST_BODY_READ_CHUNK_BYTES)"` | — |
| [SRC-EEF2E6447C-L000469](../../api/omarai.py#L469) | 469 | `"                    )"` | — |
| [SRC-EEF2E6447C-L000470](../../api/omarai.py#L470) | 470 | `"                except TimeoutError:"` | — |
| [SRC-EEF2E6447C-L000471](../../api/omarai.py#L471) | 471 | `"                    timed_out = True"` | — |
| [SRC-EEF2E6447C-L000472](../../api/omarai.py#L472) | 472 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000473](../../api/omarai.py#L473) | 473 | `"                if not chunk:"` | — |
| [SRC-EEF2E6447C-L000474](../../api/omarai.py#L474) | 474 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000475](../../api/omarai.py#L475) | 475 | `"                body.extend(chunk)"` | — |
| [SRC-EEF2E6447C-L000476](../../api/omarai.py#L476) | 476 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000477](../../api/omarai.py#L477) | 477 | `"            try:"` | — |
| [SRC-EEF2E6447C-L000478](../../api/omarai.py#L478) | 478 | `"                self.connection.settimeout(previous_timeout)"` | — |
| [SRC-EEF2E6447C-L000479](../../api/omarai.py#L479) | 479 | `"            except OSError:"` | — |
| [SRC-EEF2E6447C-L000480](../../api/omarai.py#L480) | 480 | `"                pass"` | — |
| [SRC-EEF2E6447C-L000481](../../api/omarai.py#L481) | 481 | `""` | — |
| [SRC-EEF2E6447C-L000482](../../api/omarai.py#L482) | 482 | `"        if timed_out:"` | — |
| [SRC-EEF2E6447C-L000483](../../api/omarai.py#L483) | 483 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000484](../../api/omarai.py#L484) | 484 | `"            self.respond(408, {\"error\": \"request body read timed out\"})"` | — |
| [SRC-EEF2E6447C-L000485](../../api/omarai.py#L485) | 485 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000486](../../api/omarai.py#L486) | 486 | `"        if len(body) != size:"` | — |
| [SRC-EEF2E6447C-L000487](../../api/omarai.py#L487) | 487 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000488](../../api/omarai.py#L488) | 488 | `"            self.respond(400, {\"error\": \"incomplete request body\"})"` | — |
| [SRC-EEF2E6447C-L000489](../../api/omarai.py#L489) | 489 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000490](../../api/omarai.py#L490) | 490 | `"        return bytes(body)"` | — |
| [SRC-EEF2E6447C-L000491](../../api/omarai.py#L491) | 491 | `""` | — |
| [SRC-EEF2E6447C-L000492](../../api/omarai.py#L492) | 492 | `"    def end_headers(self):"` | — |
| [SRC-EEF2E6447C-L000493](../../api/omarai.py#L493) | 493 | `"        \"\"\"Apply defensive browser headers to successful and error responses alike.\"\"\""` | — |
| [SRC-EEF2E6447C-L000494](../../api/omarai.py#L494) | 494 | `"        self.send_header(\"X-Content-Type-Options\", \"nosniff\")"` | — |
| [SRC-EEF2E6447C-L000495](../../api/omarai.py#L495) | 495 | `"        self.send_header(\"X-Frame-Options\", \"DENY\")"` | — |
| [SRC-EEF2E6447C-L000496](../../api/omarai.py#L496) | 496 | `"        self.send_header(\"Referrer-Policy\", \"strict-origin-when-cross-origin\")"` | — |
| [SRC-EEF2E6447C-L000497](../../api/omarai.py#L497) | 497 | `"        self.send_header(\"Permissions-Policy\", \"camera=(), microphone=(), geolocation=()\")"` | — |
| [SRC-EEF2E6447C-L000498](../../api/omarai.py#L498) | 498 | `"        self.send_header(\"Content-Security-Policy\", _content_security_policy())"` | — |
| [SRC-EEF2E6447C-L000499](../../api/omarai.py#L499) | 499 | `"        super().end_headers()"` | — |
| [SRC-EEF2E6447C-L000500](../../api/omarai.py#L500) | 500 | `""` | — |
| [SRC-EEF2E6447C-L000501](../../api/omarai.py#L501) | 501 | `"    def respond(self, status, payload, content_type=\"application/json; charset=utf-8\"):"` | — |
| [SRC-EEF2E6447C-L000502](../../api/omarai.py#L502) | 502 | `"        body = payload.encode() if isinstance(payload, str) else json.dumps(payload, ensure_ascii=False).encode()"` | — |
| [SRC-EEF2E6447C-L000503](../../api/omarai.py#L503) | 503 | `"        self.send_response(status)"` | — |
| [SRC-EEF2E6447C-L000504](../../api/omarai.py#L504) | 504 | `"        self.send_header(\"Content-Type\", content_type)"` | — |
| [SRC-EEF2E6447C-L000505](../../api/omarai.py#L505) | 505 | `"        self.send_header(\"Content-Length\", str(len(body)))"` | — |
| [SRC-EEF2E6447C-L000506](../../api/omarai.py#L506) | 506 | `"        self.send_header(\"Cache-Control\", \"no-store\")"` | — |
| [SRC-EEF2E6447C-L000507](../../api/omarai.py#L507) | 507 | `"        origin = self.headers.get(\"Origin\")"` | — |
| [SRC-EEF2E6447C-L000508](../../api/omarai.py#L508) | 508 | `"        if origin and self._origin_allowed(origin):"` | — |
| [SRC-EEF2E6447C-L000509](../../api/omarai.py#L509) | 509 | `"            self.send_header(\"Access-Control-Allow-Origin\", origin)"` | — |
| [SRC-EEF2E6447C-L000510](../../api/omarai.py#L510) | 510 | `"            self.send_header(\"Vary\", \"Origin\")"` | — |
| [SRC-EEF2E6447C-L000511](../../api/omarai.py#L511) | 511 | `"        self.end_headers()"` | — |
| [SRC-EEF2E6447C-L000512](../../api/omarai.py#L512) | 512 | `"        self.wfile.write(body)"` | — |
| [SRC-EEF2E6447C-L000513](../../api/omarai.py#L513) | 513 | `""` | — |
| [SRC-EEF2E6447C-L000514](../../api/omarai.py#L514) | 514 | `"    def do_GET(self):"` | — |
| [SRC-EEF2E6447C-L000515](../../api/omarai.py#L515) | 515 | `"        parsed = urlparse(self.path)"` | — |
| [SRC-EEF2E6447C-L000516](../../api/omarai.py#L516) | 516 | `"        if parsed.path in {\"/\", \"/agent\"}:"` | — |
| [SRC-EEF2E6447C-L000517](../../api/omarai.py#L517) | 517 | `"            if not AGENT_DASHBOARD.exists():"` | — |
| [SRC-EEF2E6447C-L000518](../../api/omarai.py#L518) | 518 | `"                return self.respond(404, {\"error\": \"agent dashboard missing\"})"` | — |
| [SRC-EEF2E6447C-L000519](../../api/omarai.py#L519) | 519 | `"            return self.respond(200, AGENT_DASHBOARD.read_text(encoding=\"utf-8\"), \"text/html; charset=utf-8\")"` | — |
| [SRC-EEF2E6447C-L000520](../../api/omarai.py#L520) | 520 | `"        if parsed.path == \"/leads\":"` | — |
| [SRC-EEF2E6447C-L000521](../../api/omarai.py#L521) | 521 | `"            if not LEADS_DASHBOARD.exists():"` | — |
| [SRC-EEF2E6447C-L000522](../../api/omarai.py#L522) | 522 | `"                return self.respond(404, {\"error\": \"leads dashboard missing\"})"` | — |
| [SRC-EEF2E6447C-L000523](../../api/omarai.py#L523) | 523 | `"            return self.respond(200, LEADS_DASHBOARD.read_text(encoding=\"utf-8\"), \"text/html; charset=utf-8\")"` | — |
| [SRC-EEF2E6447C-L000524](../../api/omarai.py#L524) | 524 | `"        if parsed.path == \"/api/health\":"` | — |
| [SRC-EEF2E6447C-L000525](../../api/omarai.py#L525) | 525 | `"            return self.respond("` | — |
| [SRC-EEF2E6447C-L000526](../../api/omarai.py#L526) | 526 | `"                200,"` | — |
| [SRC-EEF2E6447C-L000527](../../api/omarai.py#L527) | 527 | `"                {"` | — |
| [SRC-EEF2E6447C-L000528](../../api/omarai.py#L528) | 528 | `"                    \"ok\": True,"` | — |
| [SRC-EEF2E6447C-L000529](../../api/omarai.py#L529) | 529 | `"                    \"app\": \"Omarai\","` | — |
| [SRC-EEF2E6447C-L000530](../../api/omarai.py#L530) | 530 | `"                    \"mode\": \"web-research\","` | — |
| [SRC-EEF2E6447C-L000531](../../api/omarai.py#L531) | 531 | `"                    \"agent\": WebAgent.status(),"` | — |
| [SRC-EEF2E6447C-L000532](../../api/omarai.py#L532) | 532 | `"                    \"build\": {"` | — |
| [SRC-EEF2E6447C-L000533](../../api/omarai.py#L533) | 533 | `"                        \"sha\": _build_identity()[0],"` | — |
| [SRC-EEF2E6447C-L000534](../../api/omarai.py#L534) | 534 | `"                        \"sha_status\": ("` | — |
| [SRC-EEF2E6447C-L000535](../../api/omarai.py#L535) | 535 | `"                            \"available\" if _build_identity()[0] != \"unknown\" else \"unknown\""` | — |
| [SRC-EEF2E6447C-L000536](../../api/omarai.py#L536) | 536 | `"                        ),"` | — |
| [SRC-EEF2E6447C-L000537](../../api/omarai.py#L537) | 537 | `"                        \"sha_source\": _build_identity()[1],"` | — |
| [SRC-EEF2E6447C-L000538](../../api/omarai.py#L538) | 538 | `"                    },"` | — |
| [SRC-EEF2E6447C-L000539](../../api/omarai.py#L539) | 539 | `"                },"` | — |
| [SRC-EEF2E6447C-L000540](../../api/omarai.py#L540) | 540 | `"            )"` | — |
| [SRC-EEF2E6447C-L000541](../../api/omarai.py#L541) | 541 | `"        if parsed.path == \"/api/leads\":"` | — |
| [SRC-EEF2E6447C-L000542](../../api/omarai.py#L542) | 542 | `"            if not self._rate_limit_ok():"` | — |
| [SRC-EEF2E6447C-L000543](../../api/omarai.py#L543) | 543 | `"                return self.respond(429, {\"error\": \"تجاوزت حد الطلبات المؤقت؛ حاول بعد دقيقة.\"})"` | — |
| [SRC-EEF2E6447C-L000544](../../api/omarai.py#L544) | 544 | `"            if not self._authorized():"` | — |
| [SRC-EEF2E6447C-L000545](../../api/omarai.py#L545) | 545 | `"                return self.respond(401, {\"error\": \"يلزم رمز الوصول الخاص بالتطبيق.\"})"` | — |
| [SRC-EEF2E6447C-L000546](../../api/omarai.py#L546) | 546 | `"            q = parse_qs(parsed.query)"` | — |
| [SRC-EEF2E6447C-L000547](../../api/omarai.py#L547) | 547 | `"            try:"` | — |
| [SRC-EEF2E6447C-L000548](../../api/omarai.py#L548) | 548 | `"                limit = max(1, min(int(q.get(\"limit\", [\"100\"])[0]), 500))"` | — |
| [SRC-EEF2E6447C-L000549](../../api/omarai.py#L549) | 549 | `"                leads = self.store.list(q.get(\"status\", [None])[0], limit, tenant_id=self._authenticated_principal[\"tenant_id\"])"` | — |
| [SRC-EEF2E6447C-L000550](../../api/omarai.py#L550) | 550 | `"            except (ValueError, TypeError):"` | — |
| [SRC-EEF2E6447C-L000551](../../api/omarai.py#L551) | 551 | `"                return self.respond(400, {\"error\": \"invalid status or limit\"})"` | — |
| [SRC-EEF2E6447C-L000552](../../api/omarai.py#L552) | 552 | `"            return self.respond(200, {\"leads\": leads, \"count\": len(leads)})"` | — |
| [SRC-EEF2E6447C-L000553](../../api/omarai.py#L553) | 553 | `"        return self.respond(404, {\"error\": \"not found\"})"` | — |
| [SRC-EEF2E6447C-L000554](../../api/omarai.py#L554) | 554 | `""` | — |
| [SRC-EEF2E6447C-L000555](../../api/omarai.py#L555) | 555 | `"    def do_POST(self):"` | — |
| [SRC-EEF2E6447C-L000556](../../api/omarai.py#L556) | 556 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000557](../../api/omarai.py#L557) | 557 | `"            # Count API attempts before origin/content-type/body validation so invalid"` | — |
| [SRC-EEF2E6447C-L000558](../../api/omarai.py#L558) | 558 | `"            # credentials and malformed requests cannot bypass per-client throttling."` | — |
| [SRC-EEF2E6447C-L000559](../../api/omarai.py#L559) | 559 | `"            path = urlparse(self.path).path"` | — |
| [SRC-EEF2E6447C-L000560](../../api/omarai.py#L560) | 560 | `"            if path.startswith(\"/api/\") and not self._rate_limit_ok():"` | — |
| [SRC-EEF2E6447C-L000561](../../api/omarai.py#L561) | 561 | `"                return self.respond(429, {\"error\": \"تجاوزت حد الطلبات المؤقت؛ حاول بعد دقيقة.\"})"` | — |
| [SRC-EEF2E6447C-L000562](../../api/omarai.py#L562) | 562 | `"            if path.startswith(\"/api/\") and not self._authorized():"` | — |
| [SRC-EEF2E6447C-L000563](../../api/omarai.py#L563) | 563 | `"                return self.respond(401, {\"error\": \"يلزم رمز الوصول الخاص بالتطبيق.\"})"` | — |
| [SRC-EEF2E6447C-L000564](../../api/omarai.py#L564) | 564 | `""` | — |
| [SRC-EEF2E6447C-L000565](../../api/omarai.py#L565) | 565 | `"            content_type = self.headers.get(\"Content-Type\", \"\").split(\";\", 1)[0].strip().lower()"` | — |
| [SRC-EEF2E6447C-L000566](../../api/omarai.py#L566) | 566 | `"            if content_type != \"application/json\":"` | — |
| [SRC-EEF2E6447C-L000567](../../api/omarai.py#L567) | 567 | `"                return self.respond(415, {\"error\": \"Content-Type must be application/json\"})"` | — |
| [SRC-EEF2E6447C-L000568](../../api/omarai.py#L568) | 568 | `"            origin = self.headers.get(\"Origin\")"` | — |
| [SRC-EEF2E6447C-L000569](../../api/omarai.py#L569) | 569 | `"            if origin and not self._origin_allowed(origin):"` | — |
| [SRC-EEF2E6447C-L000570](../../api/omarai.py#L570) | 570 | `"                return self.respond(403, {\"error\": \"cross-origin requests are not allowed\"})"` | — |
| [SRC-EEF2E6447C-L000571](../../api/omarai.py#L571) | 571 | `""` | — |
| [SRC-EEF2E6447C-L000572](../../api/omarai.py#L572) | 572 | `"            raw_body = self._read_request_body()"` | — |
| [SRC-EEF2E6447C-L000573](../../api/omarai.py#L573) | 573 | `"            if raw_body is None:"` | — |
| [SRC-EEF2E6447C-L000574](../../api/omarai.py#L574) | 574 | `"                return"` | — |
| [SRC-EEF2E6447C-L000575](../../api/omarai.py#L575) | 575 | `"            data = json.loads(raw_body)"` | — |
| [SRC-EEF2E6447C-L000576](../../api/omarai.py#L576) | 576 | `"            if not isinstance(data, dict):"` | — |
| [SRC-EEF2E6447C-L000577](../../api/omarai.py#L577) | 577 | `"                return self.respond(400, {\"error\": \"request body must be a JSON object\"})"` | — |
| [SRC-EEF2E6447C-L000578](../../api/omarai.py#L578) | 578 | `"            if path == \"/api/tokens/revoke\":"` | — |
| [SRC-EEF2E6447C-L000579](../../api/omarai.py#L579) | 579 | `"                supplied = self.headers.get(\"Authorization\", \"\")"` | — |
| [SRC-EEF2E6447C-L000580](../../api/omarai.py#L580) | 580 | `"                token = supplied[7:].strip() if supplied.startswith(\"Bearer \") else \"\""` | — |
| [SRC-EEF2E6447C-L000581](../../api/omarai.py#L581) | 581 | `"                shared_token = os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000582](../../api/omarai.py#L582) | 582 | `"                if shared_token and hmac.compare_digest(token, shared_token):"` | — |
| [SRC-EEF2E6447C-L000583](../../api/omarai.py#L583) | 583 | `"                    return self.respond("` | — |
| [SRC-EEF2E6447C-L000584](../../api/omarai.py#L584) | 584 | `"                        409,"` | — |
| [SRC-EEF2E6447C-L000585](../../api/omarai.py#L585) | 585 | `"                        {"` | — |
| [SRC-EEF2E6447C-L000586](../../api/omarai.py#L586) | 586 | `"                            \"error\": ("` | — |
| [SRC-EEF2E6447C-L000587](../../api/omarai.py#L587) | 587 | `"                                \"shared application token must be rotated by the operator \""` | — |
| [SRC-EEF2E6447C-L000588](../../api/omarai.py#L588) | 588 | `"                                \"through the deployment configuration\""` | — |
| [SRC-EEF2E6447C-L000589](../../api/omarai.py#L589) | 589 | `"                            )"` | — |
| [SRC-EEF2E6447C-L000590](../../api/omarai.py#L590) | 590 | `"                        },"` | — |
| [SRC-EEF2E6447C-L000591](../../api/omarai.py#L591) | 591 | `"                    )"` | — |
| [SRC-EEF2E6447C-L000592](../../api/omarai.py#L592) | 592 | `"                revoked = self.store.revoke_api_token("` | — |
| [SRC-EEF2E6447C-L000593](../../api/omarai.py#L593) | 593 | `"                    token,"` | — |
| [SRC-EEF2E6447C-L000594](../../api/omarai.py#L594) | 594 | `"                    tenant_id=self._authenticated_principal[\"tenant_id\"],"` | — |
| [SRC-EEF2E6447C-L000595](../../api/omarai.py#L595) | 595 | `"                    user_id=self._authenticated_principal[\"user_id\"],"` | — |
| [SRC-EEF2E6447C-L000596](../../api/omarai.py#L596) | 596 | `"                )"` | — |
| [SRC-EEF2E6447C-L000597](../../api/omarai.py#L597) | 597 | `"                if not revoked:"` | — |
| [SRC-EEF2E6447C-L000598](../../api/omarai.py#L598) | 598 | `"                    return self.respond(404, {\"error\": \"token not found\"})"` | — |
| [SRC-EEF2E6447C-L000599](../../api/omarai.py#L599) | 599 | `"                return self.respond(200, {\"revoked\": True})"` | — |
| [SRC-EEF2E6447C-L000600](../../api/omarai.py#L600) | 600 | `""` | — |
| [SRC-EEF2E6447C-L000601](../../api/omarai.py#L601) | 601 | `"            if path == \"/api/diagnostics\":"` | — |
| [SRC-EEF2E6447C-L000602](../../api/omarai.py#L602) | 602 | `"                test_model = data.get(\"test_model\", False)"` | — |
| [SRC-EEF2E6447C-L000603](../../api/omarai.py#L603) | 603 | `"                test_social = data.get(\"test_social\", False)"` | — |
| [SRC-EEF2E6447C-L000604](../../api/omarai.py#L604) | 604 | `"                allow_provider_usage = data.get(\"allow_provider_usage\", False)"` | — |
| [SRC-EEF2E6447C-L000605](../../api/omarai.py#L605) | 605 | `"                if ("` | — |
| [SRC-EEF2E6447C-L000606](../../api/omarai.py#L606) | 606 | `"                    not isinstance(test_model, bool)"` | — |
| [SRC-EEF2E6447C-L000607](../../api/omarai.py#L607) | 607 | `"                    or not isinstance(test_social, bool)"` | — |
| [SRC-EEF2E6447C-L000608](../../api/omarai.py#L608) | 608 | `"                    or not isinstance(allow_provider_usage, bool)"` | — |
| [SRC-EEF2E6447C-L000609](../../api/omarai.py#L609) | 609 | `"                ):"` | — |
| [SRC-EEF2E6447C-L000610](../../api/omarai.py#L610) | 610 | `"                    return self.respond("` | — |
| [SRC-EEF2E6447C-L000611](../../api/omarai.py#L611) | 611 | `"                        400,"` | — |
| [SRC-EEF2E6447C-L000612](../../api/omarai.py#L612) | 612 | `"                        {"` | — |
| [SRC-EEF2E6447C-L000613](../../api/omarai.py#L613) | 613 | `"                            \"error\": ("` | — |
| [SRC-EEF2E6447C-L000614](../../api/omarai.py#L614) | 614 | `"                                \"test_model, test_social, and allow_provider_usage \""` | — |
| [SRC-EEF2E6447C-L000615](../../api/omarai.py#L615) | 615 | `"                                \"must be booleans\""` | — |
| [SRC-EEF2E6447C-L000616](../../api/omarai.py#L616) | 616 | `"                            )"` | — |
| [SRC-EEF2E6447C-L000617](../../api/omarai.py#L617) | 617 | `"                        },"` | — |
| [SRC-EEF2E6447C-L000618](../../api/omarai.py#L618) | 618 | `"                    )"` | — |
| [SRC-EEF2E6447C-L000619](../../api/omarai.py#L619) | 619 | `"                if not allow_provider_usage:"` | — |
| [SRC-EEF2E6447C-L000620](../../api/omarai.py#L620) | 620 | `"                    return self.respond("` | — |
| [SRC-EEF2E6447C-L000621](../../api/omarai.py#L621) | 621 | `"                        403,"` | — |
| [SRC-EEF2E6447C-L000622](../../api/omarai.py#L622) | 622 | `"                        {"` | — |
| [SRC-EEF2E6447C-L000623](../../api/omarai.py#L623) | 623 | `"                            \"error\": ("` | — |
| [SRC-EEF2E6447C-L000624](../../api/omarai.py#L624) | 624 | `"                                \"live diagnostics perform outbound search and may consume \""` | — |
| [SRC-EEF2E6447C-L000625](../../api/omarai.py#L625) | 625 | `"                                \"provider quota or incur charges; explicit owner approval is required\""` | — |
| [SRC-EEF2E6447C-L000626](../../api/omarai.py#L626) | 626 | `"                            )"` | — |
| [SRC-EEF2E6447C-L000627](../../api/omarai.py#L627) | 627 | `"                        },"` | — |
| [SRC-EEF2E6447C-L000628](../../api/omarai.py#L628) | 628 | `"                    )"` | — |
| [SRC-EEF2E6447C-L000629](../../api/omarai.py#L629) | 629 | `"                if self._authenticated_principal.get(\"role\") != \"owner\":"` | — |
| [SRC-EEF2E6447C-L000630](../../api/omarai.py#L630) | 630 | `"                    return self.respond("` | — |
| [SRC-EEF2E6447C-L000631](../../api/omarai.py#L631) | 631 | `"                        403,"` | — |
| [SRC-EEF2E6447C-L000632](../../api/omarai.py#L632) | 632 | `"                        {\"error\": \"فحص الموصلات الحي واستهلاك الحصص متاح لمالك مساحة العمل فقط.\"},"` | — |
| [SRC-EEF2E6447C-L000633](../../api/omarai.py#L633) | 633 | `"                    )"` | — |
| [SRC-EEF2E6447C-L000634](../../api/omarai.py#L634) | 634 | `"                return self._run_bounded_agent_operation("` | — |
| [SRC-EEF2E6447C-L000635](../../api/omarai.py#L635) | 635 | `"                    lambda: WebAgent().diagnostics("` | — |
| [SRC-EEF2E6447C-L000636](../../api/omarai.py#L636) | 636 | `"                        test_model=test_model,"` | — |
| [SRC-EEF2E6447C-L000637](../../api/omarai.py#L637) | 637 | `"                        test_social=test_social,"` | — |
| [SRC-EEF2E6447C-L000638](../../api/omarai.py#L638) | 638 | `"                    )"` | — |
| [SRC-EEF2E6447C-L000639](../../api/omarai.py#L639) | 639 | `"                )"` | — |
| [SRC-EEF2E6447C-L000640](../../api/omarai.py#L640) | 640 | `""` | — |
| [SRC-EEF2E6447C-L000641](../../api/omarai.py#L641) | 641 | `"            if path == \"/api/agent\":"` | — |
| [SRC-EEF2E6447C-L000642](../../api/omarai.py#L642) | 642 | `"                question = data.get(\"question\", \"\")"` | — |
| [SRC-EEF2E6447C-L000643](../../api/omarai.py#L643) | 643 | `"                if not isinstance(question, str) or not question.strip():"` | — |
| [SRC-EEF2E6447C-L000644](../../api/omarai.py#L644) | 644 | `"                    return self.respond(400, {\"error\": \"question must be a non-empty string\"})"` | — |
| [SRC-EEF2E6447C-L000645](../../api/omarai.py#L645) | 645 | `"                agent = WebAgent()"` | — |
| [SRC-EEF2E6447C-L000646](../../api/omarai.py#L646) | 646 | `"                history = data.get(\"history\", [])"` | — |
| [SRC-EEF2E6447C-L000647](../../api/omarai.py#L647) | 647 | `"                if \"mode\" not in data:"` | — |
| [SRC-EEF2E6447C-L000648](../../api/omarai.py#L648) | 648 | `"                    return self._run_bounded_agent_operation("` | — |
| [SRC-EEF2E6447C-L000649](../../api/omarai.py#L649) | 649 | `"                        lambda: agent.answer(question, history)"` | — |
| [SRC-EEF2E6447C-L000650](../../api/omarai.py#L650) | 650 | `"                    )"` | — |
| [SRC-EEF2E6447C-L000651](../../api/omarai.py#L651) | 651 | `"                return self._run_bounded_agent_operation("` | — |
| [SRC-EEF2E6447C-L000652](../../api/omarai.py#L652) | 652 | `"                    lambda: agent.answer(question, history, data.get(\"mode\"))"` | — |
| [SRC-EEF2E6447C-L000653](../../api/omarai.py#L653) | 653 | `"                )"` | — |
| [SRC-EEF2E6447C-L000654](../../api/omarai.py#L654) | 654 | `""` | — |
| [SRC-EEF2E6447C-L000655](../../api/omarai.py#L655) | 655 | `"            if path == \"/api/ask\":"` | — |
| [SRC-EEF2E6447C-L000656](../../api/omarai.py#L656) | 656 | `"                question = data.get(\"question\", \"\")"` | — |
| [SRC-EEF2E6447C-L000657](../../api/omarai.py#L657) | 657 | `"                if not isinstance(question, str) or not question.strip():"` | — |
| [SRC-EEF2E6447C-L000658](../../api/omarai.py#L658) | 658 | `"                    return self.respond(400, {\"error\": \"question must be a non-empty string\"})"` | — |
| [SRC-EEF2E6447C-L000659](../../api/omarai.py#L659) | 659 | `"                if len(question) > 1000:"` | — |
| [SRC-EEF2E6447C-L000660](../../api/omarai.py#L660) | 660 | `"                    return self.respond(400, {\"error\": \"question must be at most 1000 characters\"})"` | — |
| [SRC-EEF2E6447C-L000661](../../api/omarai.py#L661) | 661 | `"                return self.respond(200, answer_question(question, self.store, tenant_id=self._authenticated_principal[\"tenant_id\"]))"` | — |
| [SRC-EEF2E6447C-L000662](../../api/omarai.py#L662) | 662 | `"            if path == \"/api/analyze\":"` | — |
| [SRC-EEF2E6447C-L000663](../../api/omarai.py#L663) | 663 | `"                return self.respond("` | — |
| [SRC-EEF2E6447C-L000664](../../api/omarai.py#L664) | 664 | `"                    200,"` | — |
| [SRC-EEF2E6447C-L000665](../../api/omarai.py#L665) | 665 | `"                    analyze("` | — |
| [SRC-EEF2E6447C-L000666](../../api/omarai.py#L666) | 666 | `"                        data.get(\"text\", \"\"),"` | — |
| [SRC-EEF2E6447C-L000667](../../api/omarai.py#L667) | 667 | `"                        data.get(\"product_terms\", []),"` | — |
| [SRC-EEF2E6447C-L000668](../../api/omarai.py#L668) | 668 | `"                        data.get(\"location_terms\", []),"` | — |
| [SRC-EEF2E6447C-L000669](../../api/omarai.py#L669) | 669 | `"                    ),"` | — |
| [SRC-EEF2E6447C-L000670](../../api/omarai.py#L670) | 670 | `"                )"` | — |
| [SRC-EEF2E6447C-L000671](../../api/omarai.py#L671) | 671 | `"            if path == \"/api/leads\":"` | — |
| [SRC-EEF2E6447C-L000672](../../api/omarai.py#L672) | 672 | `"                if self._authenticated_principal[\"role\"] == \"viewer\":"` | — |
| [SRC-EEF2E6447C-L000673](../../api/omarai.py#L673) | 673 | `"                    return self.respond(403, {\"error\": \"هذه العضوية للقراءة فقط.\"})"` | — |
| [SRC-EEF2E6447C-L000674](../../api/omarai.py#L674) | 674 | `"                lead, created = self.store.add("` | — |
| [SRC-EEF2E6447C-L000675](../../api/omarai.py#L675) | 675 | `"                    data.get(\"text\", \"\"),"` | — |
| [SRC-EEF2E6447C-L000676](../../api/omarai.py#L676) | 676 | `"                    data.get(\"source_url\", \"\"),"` | — |
| [SRC-EEF2E6447C-L000677](../../api/omarai.py#L677) | 677 | `"                    data.get(\"platform\", \"manual\"),"` | — |
| [SRC-EEF2E6447C-L000678](../../api/omarai.py#L678) | 678 | `"                    data.get(\"observed_at\"),"` | — |
| [SRC-EEF2E6447C-L000679](../../api/omarai.py#L679) | 679 | `"                    data.get(\"note\", \"\"),"` | — |
| [SRC-EEF2E6447C-L000680](../../api/omarai.py#L680) | 680 | `"                    data.get(\"product_terms\", []),"` | — |
| [SRC-EEF2E6447C-L000681](../../api/omarai.py#L681) | 681 | `"                    data.get(\"location_terms\", []),"` | — |
| [SRC-EEF2E6447C-L000682](../../api/omarai.py#L682) | 682 | `"                    tenant_id=self._authenticated_principal[\"tenant_id\"],"` | — |
| [SRC-EEF2E6447C-L000683](../../api/omarai.py#L683) | 683 | `"                )"` | — |
| [SRC-EEF2E6447C-L000684](../../api/omarai.py#L684) | 684 | `"                return self.respond(201 if created else 200, {\"lead\": lead, \"created\": created})"` | — |
| [SRC-EEF2E6447C-L000685](../../api/omarai.py#L685) | 685 | `"            route = path.split(\"/\")"` | — |
| [SRC-EEF2E6447C-L000686](../../api/omarai.py#L686) | 686 | `"            if len(route) == 5 and route[1:3] == [\"api\", \"leads\"] and route[4] == \"status\":"` | — |
| [SRC-EEF2E6447C-L000687](../../api/omarai.py#L687) | 687 | `"                if self._authenticated_principal[\"role\"] == \"viewer\":"` | — |
| [SRC-EEF2E6447C-L000688](../../api/omarai.py#L688) | 688 | `"                    return self.respond(403, {\"error\": \"هذه العضوية للقراءة فقط.\"})"` | — |
| [SRC-EEF2E6447C-L000689](../../api/omarai.py#L689) | 689 | `"                lead = self.store.update_status(route[3], data.get(\"status\", \"new\"), tenant_id=self._authenticated_principal[\"tenant_id\"])"` | — |
| [SRC-EEF2E6447C-L000690](../../api/omarai.py#L690) | 690 | `"                return self.respond(200, {\"lead\": lead}) if lead else self.respond(404, {\"error\": \"lead not found\"})"` | — |
| [SRC-EEF2E6447C-L000691](../../api/omarai.py#L691) | 691 | `"            return self.respond(404, {\"error\": \"not found\"})"` | — |
| [SRC-EEF2E6447C-L000692](../../api/omarai.py#L692) | 692 | `"        except (ValueError, TypeError, json.JSONDecodeError) as exc:"` | — |
| [SRC-EEF2E6447C-L000693](../../api/omarai.py#L693) | 693 | `"            return self.respond(400, {\"error\": str(exc)})"` | — |
| [SRC-EEF2E6447C-L000694](../../api/omarai.py#L694) | 694 | `"        except Exception:  # noqa: BLE001 — keep unexpected details out of API responses"` | — |
| [SRC-EEF2E6447C-L000695](../../api/omarai.py#L695) | 695 | `"            return self.respond(500, {\"error\": \"internal server error\"})"` | — |
| [SRC-EEF2E6447C-L000696](../../api/omarai.py#L696) | 696 | `""` | — |
| [SRC-EEF2E6447C-L000697](../../api/omarai.py#L697) | 697 | `"    def do_OPTIONS(self):"` | — |
| [SRC-EEF2E6447C-L000698](../../api/omarai.py#L698) | 698 | `"        origin = self.headers.get(\"Origin\")"` | — |
| [SRC-EEF2E6447C-L000699](../../api/omarai.py#L699) | 699 | `"        if not origin or not self._origin_allowed(origin):"` | — |
| [SRC-EEF2E6447C-L000700](../../api/omarai.py#L700) | 700 | `"            return self.respond(403, {\"error\": \"cross-origin requests are not allowed\"})"` | — |
| [SRC-EEF2E6447C-L000701](../../api/omarai.py#L701) | 701 | `"        self.send_response(204)"` | — |
| [SRC-EEF2E6447C-L000702](../../api/omarai.py#L702) | 702 | `"        self.send_header(\"Access-Control-Allow-Origin\", origin)"` | — |
| [SRC-EEF2E6447C-L000703](../../api/omarai.py#L703) | 703 | `"        self.send_header(\"Vary\", \"Origin\")"` | — |
| [SRC-EEF2E6447C-L000704](../../api/omarai.py#L704) | 704 | `"        self.send_header(\"Access-Control-Allow-Methods\", \"GET, POST, OPTIONS\")"` | — |
| [SRC-EEF2E6447C-L000705](../../api/omarai.py#L705) | 705 | `"        self.send_header(\"Access-Control-Allow-Headers\", \"Authorization, Content-Type\")"` | — |
| [SRC-EEF2E6447C-L000706](../../api/omarai.py#L706) | 706 | `"        self.send_header(\"Access-Control-Max-Age\", \"600\")"` | — |
| [SRC-EEF2E6447C-L000707](../../api/omarai.py#L707) | 707 | `"        self.send_header(\"Content-Length\", \"0\")"` | — |
| [SRC-EEF2E6447C-L000708](../../api/omarai.py#L708) | 708 | `"        self.end_headers()"` | — |
| [SRC-EEF2E6447C-L000709](../../api/omarai.py#L709) | 709 | `""` | — |
| [SRC-EEF2E6447C-L000710](../../api/omarai.py#L710) | 710 | `"    def log_message(self, *args):"` | — |
| [SRC-EEF2E6447C-L000711](../../api/omarai.py#L711) | 711 | `"        pass"` | — |
| [SRC-EEF2E6447C-L000712](../../api/omarai.py#L712) | 712 | `""` | — |
| [SRC-EEF2E6447C-L000713](../../api/omarai.py#L713) | 713 | `""` | — |
| [SRC-EEF2E6447C-L000714](../../api/omarai.py#L714) | 714 | `"def answer_question(question, store, *, tenant_id=None):"` | — |
| [SRC-EEF2E6447C-L000715](../../api/omarai.py#L715) | 715 | `"    \"\"\"Answer common operational questions from local records using explicit rules.\"\"\""` | — |
| [SRC-EEF2E6447C-L000716](../../api/omarai.py#L716) | 716 | `"    normalized = normalize(question)"` | — |
| [SRC-EEF2E6447C-L000717](../../api/omarai.py#L717) | 717 | `"    leads = store.list(limit=500, tenant_id=tenant_id)"` | — |
| [SRC-EEF2E6447C-L000718](../../api/omarai.py#L718) | 718 | `"    active = [lead for lead in leads if lead[\"status\"] not in {\"rejected\", \"converted\"}]"` | — |
| [SRC-EEF2E6447C-L000719](../../api/omarai.py#L719) | 719 | `"    if any(term in normalized for term in (\"افضل عميل\", \"احسن عميل\", \"افضل اشارة\", \"احسن اشارة\", \"اشارة اراجعها\", \"مين افضل\", \"مين اتابع\", \"اتابع مين\", \"اهم عميل\")):"` | — |
| [SRC-EEF2E6447C-L000720](../../api/omarai.py#L720) | 720 | `"        if not active:"` | — |
| [SRC-EEF2E6447C-L000721](../../api/omarai.py#L721) | 721 | `"            return {\"answer\": \"لا توجد إشارة نشطة محفوظة بعد. حلّل نصًا من مصدر مسموح واحفظه أولًا، ثم اسألني مرة أخرى.\", \"kind\": \"no_data\", \"lead_id\": None}"` | — |
| [SRC-EEF2E6447C-L000722](../../api/omarai.py#L722) | 722 | `"        lead = max(active, key=lambda item: (item[\"assessment\"][\"score\"], item[\"updated_at\"]))"` | — |
| [SRC-EEF2E6447C-L000723](../../api/omarai.py#L723) | 723 | `"        assessment = lead[\"assessment\"]"` | — |
| [SRC-EEF2E6447C-L000724](../../api/omarai.py#L724) | 724 | `"        answer = \"الأولوية المقترحة للمراجعة هي الإشارة \" + lead[\"id\"][:8] + \" بدرجة قواعد \" + str(assessment[\"score\"]) + \"/100. السبب: \" + assessment[\"summary\"] + \" المصدر: \" + lead[\"source_url\"] + \". هذه أولوية مراجعة وليست تأكيدًا أن صاحبه سيشتري.\""` | — |
| [SRC-EEF2E6447C-L000725](../../api/omarai.py#L725) | 725 | `"        return {\"answer\": answer, \"kind\": \"lead_recommendation\", \"lead_id\": lead[\"id\"]}"` | — |
| [SRC-EEF2E6447C-L000726](../../api/omarai.py#L726) | 726 | `"    if any(term in normalized for term in (\"كام عميل\", \"كم عميل\", \"عدد العملاء\", \"عدد الاشارات\", \"الاحصائيات\", \"احصائيات\")):"` | — |
| [SRC-EEF2E6447C-L000727](../../api/omarai.py#L727) | 727 | `"        keys = (\"new\", \"qualified\", \"contacted\", \"converted\", \"needs_review\", \"rejected\")"` | — |
| [SRC-EEF2E6447C-L000728](../../api/omarai.py#L728) | 728 | `"        by_status = {key: sum(lead[\"status\"] == key for lead in leads) for key in keys}"` | — |
| [SRC-EEF2E6447C-L000729](../../api/omarai.py#L729) | 729 | `"        high = sum(lead[\"assessment\"][\"label\"] == \"high_intent\" for lead in leads)"` | — |
| [SRC-EEF2E6447C-L000730](../../api/omarai.py#L730) | 730 | `"        answer = \"في السجل المحلي \" + str(len(leads)) + \" إشارة، منها \" + str(high) + \" بإشارة قوية نسبيًا وفق القواعد. الحالات: جديد \" + str(by_status[\"new\"]) + \"، مؤهل \" + str(by_status[\"qualified\"]) + \"، تم التواصل \" + str(by_status[\"contacted\"]) + \"، تم البيع \" + str(by_status[\"converted\"]) + \"، تحتاج مراجعة \" + str(by_status[\"needs_review\"]) + \"، مرفوض \" + str(by_status[\"rejected\"]) + \".\""` | — |
| [SRC-EEF2E6447C-L000731](../../api/omarai.py#L731) | 731 | `"        return {\"answer\": answer, \"kind\": \"local_statistics\", \"lead_id\": None}"` | — |
| [SRC-EEF2E6447C-L000732](../../api/omarai.py#L732) | 732 | `"    if any(term in normalized for term in (\"ليه الدرجه\", \"سبب الدرجه\", \"طريقة التقييم\", \"بتقيم ازاي\", \"معيار التقييم\")):"` | — |
| [SRC-EEF2E6447C-L000733](../../api/omarai.py#L733) | 733 | `"        latest = max(leads, key=lambda item: item[\"updated_at\"], default=None)"` | — |
| [SRC-EEF2E6447C-L000734](../../api/omarai.py#L734) | 734 | `"        if latest:"` | — |
| [SRC-EEF2E6447C-L000735](../../api/omarai.py#L735) | 735 | `"            signals = \"، \".join(signal[\"phrase\"] for signal in latest[\"assessment\"][\"matched_signals\"]) or \"لم تُطابق عبارات معروفة\""` | — |
| [SRC-EEF2E6447C-L000736](../../api/omarai.py#L736) | 736 | `"            answer = \"الإشارة الأحدث درجتها \" + str(latest[\"assessment\"][\"score\"]) + \"/100 لأن القواعد طابقت: \" + signals + \". الدرجة ليست احتمالًا إحصائيًا ولا تثبت نية الكاتب.\""` | — |
| [SRC-EEF2E6447C-L000737](../../api/omarai.py#L737) | 737 | `"        else:"` | — |
| [SRC-EEF2E6447C-L000738](../../api/omarai.py#L738) | 738 | `"            answer = \"أحسب الدرجة بقواعد واضحة: تعبير الشراء، خطوة تجارية تالية، السعر أو الميزانية، وسياق المنتج والمكان. كل فئة تحتسب مرة واحدة فقط.\""` | — |
| [SRC-EEF2E6447C-L000739](../../api/omarai.py#L739) | 739 | `"        return {\"answer\": answer, \"kind\": \"scoring_explanation\", \"lead_id\": latest[\"id\"] if latest else None}"` | — |
| [SRC-EEF2E6447C-L000740](../../api/omarai.py#L740) | 740 | `"    if any(term in normalized for term in (\"اكتب رساله\", \"اكتب رسالة\", \"رساله تواصل\", \"رسالة تواصل\", \"ابعتله\", \"اتواصل ازاي\")):"` | — |
| [SRC-EEF2E6447C-L000741](../../api/omarai.py#L741) | 741 | `"        if not active:"` | — |
| [SRC-EEF2E6447C-L000742](../../api/omarai.py#L742) | 742 | `"            answer = \"لا توجد إشارة محفوظة أخصص مسودة لها بعد. أدخل نصًا ومصدرًا أولًا.\""` | — |
| [SRC-EEF2E6447C-L000743](../../api/omarai.py#L743) | 743 | `"        else:"` | — |
| [SRC-EEF2E6447C-L000744](../../api/omarai.py#L744) | 744 | `"            lead = max(active, key=lambda item: (item[\"assessment\"][\"score\"], item[\"updated_at\"]))"` | — |
| [SRC-EEF2E6447C-L000745](../../api/omarai.py#L745) | 745 | `"            answer = \"مسودة للمراجعة البشرية فقط: «أهلًا، لاحظت سؤالك المنشور عن العقار/الوحدة. لو ما زلت مهتمًا، هل تحب الاطلاع على التفاصيل المتاحة وخيارات المعاينة؟» مرتبطة بالإشارة \" + lead[\"id\"][:8] + \". لم يتم إرسال أي رسالة.\""` | — |
| [SRC-EEF2E6447C-L000746](../../api/omarai.py#L746) | 746 | `"        return {\"answer\": answer, \"kind\": \"message_draft\", \"lead_id\": active[0][\"id\"] if active else None}"` | — |
| [SRC-EEF2E6447C-L000747](../../api/omarai.py#L747) | 747 | `"    return {\"answer\": \"أنا المساعد المحلي الخاص بسجل العملاء. استخدم وكيل البحث العام من الصفحة الرئيسية لطرح أسئلة مفتوحة والبحث في الويب.\", \"kind\": \"help\", \"lead_id\": None}"` | — |
| [SRC-EEF2E6447C-L000748](../../api/omarai.py#L748) | 748 | `""` | — |
| [SRC-EEF2E6447C-L000749](../../api/omarai.py#L749) | 749 | `""` | — |
| [SRC-EEF2E6447C-L000750](../../api/omarai.py#L750) | 750 | `"class BoundedThreadingHTTPServer(ThreadingHTTPServer):"` | — |
| [SRC-EEF2E6447C-L000751](../../api/omarai.py#L751) | 751 | `"    \"\"\"Threaded HTTP server with a hard process-local ceiling on handler threads.\"\"\""` | — |
| [SRC-EEF2E6447C-L000752](../../api/omarai.py#L752) | 752 | `""` | — |
| [SRC-EEF2E6447C-L000753](../../api/omarai.py#L753) | 753 | `"    daemon_threads = True"` | — |
| [SRC-EEF2E6447C-L000754](../../api/omarai.py#L754) | 754 | `"    overload_response = ("` | — |
| [SRC-EEF2E6447C-L000755](../../api/omarai.py#L755) | 755 | `"        b\"HTTP/1.1 503 Service Unavailable\\r\\n\""` | — |
| [SRC-EEF2E6447C-L000756](../../api/omarai.py#L756) | 756 | `"        b\"Connection: close\\r\\n\""` | — |
| [SRC-EEF2E6447C-L000757](../../api/omarai.py#L757) | 757 | `"        b\"Retry-After: 5\\r\\n\""` | — |
| [SRC-EEF2E6447C-L000758](../../api/omarai.py#L758) | 758 | `"        b\"Content-Length: 0\\r\\n\\r\\n\""` | — |
| [SRC-EEF2E6447C-L000759](../../api/omarai.py#L759) | 759 | `"    )"` | — |
| [SRC-EEF2E6447C-L000760](../../api/omarai.py#L760) | 760 | `""` | — |
| [SRC-EEF2E6447C-L000761](../../api/omarai.py#L761) | 761 | `"    def __init__("` | — |
| [SRC-EEF2E6447C-L000762](../../api/omarai.py#L762) | 762 | `"        self,"` | — |
| [SRC-EEF2E6447C-L000763](../../api/omarai.py#L763) | 763 | `"        server_address,"` | — |
| [SRC-EEF2E6447C-L000764](../../api/omarai.py#L764) | 764 | `"        request_handler_class,"` | — |
| [SRC-EEF2E6447C-L000765](../../api/omarai.py#L765) | 765 | `"        bind_and_activate: bool = True,"` | — |
| [SRC-EEF2E6447C-L000766](../../api/omarai.py#L766) | 766 | `"        *,"` | — |
| [SRC-EEF2E6447C-L000767](../../api/omarai.py#L767) | 767 | `"        max_concurrent_connections: int \| None = None,"` | — |
| [SRC-EEF2E6447C-L000768](../../api/omarai.py#L768) | 768 | `"    ):"` | — |
| [SRC-EEF2E6447C-L000769](../../api/omarai.py#L769) | 769 | `"        super().__init__(server_address, request_handler_class, bind_and_activate)"` | — |
| [SRC-EEF2E6447C-L000770](../../api/omarai.py#L770) | 770 | `"        configured = ("` | — |
| [SRC-EEF2E6447C-L000771](../../api/omarai.py#L771) | 771 | `"            _configured_http_connection_limit()"` | — |
| [SRC-EEF2E6447C-L000772](../../api/omarai.py#L772) | 772 | `"            if max_concurrent_connections is None"` | — |
| [SRC-EEF2E6447C-L000773](../../api/omarai.py#L773) | 773 | `"            else int(max_concurrent_connections)"` | — |
| [SRC-EEF2E6447C-L000774](../../api/omarai.py#L774) | 774 | `"        )"` | — |
| [SRC-EEF2E6447C-L000775](../../api/omarai.py#L775) | 775 | `"        limit = max(1, min(configured, MAX_HTTP_CONNECTION_LIMIT))"` | — |
| [SRC-EEF2E6447C-L000776](../../api/omarai.py#L776) | 776 | `"        self.max_concurrent_connections = limit"` | — |
| [SRC-EEF2E6447C-L000777](../../api/omarai.py#L777) | 777 | `"        self._connection_slots = threading.BoundedSemaphore(limit)"` | — |
| [SRC-EEF2E6447C-L000778](../../api/omarai.py#L778) | 778 | `""` | — |
| [SRC-EEF2E6447C-L000779](../../api/omarai.py#L779) | 779 | `"    def process_request(self, request, client_address):"` | — |
| [SRC-EEF2E6447C-L000780](../../api/omarai.py#L780) | 780 | `"        \"\"\"Reject excess accepted sockets before creating another handler thread.\"\"\""` | — |
| [SRC-EEF2E6447C-L000781](../../api/omarai.py#L781) | 781 | `"        if not self._connection_slots.acquire(blocking=False):"` | — |
| [SRC-EEF2E6447C-L000782](../../api/omarai.py#L782) | 782 | `"            try:"` | — |
| [SRC-EEF2E6447C-L000783](../../api/omarai.py#L783) | 783 | `"                request.sendall(self.overload_response)"` | — |
| [SRC-EEF2E6447C-L000784](../../api/omarai.py#L784) | 784 | `"            except OSError:"` | — |
| [SRC-EEF2E6447C-L000785](../../api/omarai.py#L785) | 785 | `"                pass"` | — |
| [SRC-EEF2E6447C-L000786](../../api/omarai.py#L786) | 786 | `"            finally:"` | — |
| [SRC-EEF2E6447C-L000787](../../api/omarai.py#L787) | 787 | `"                self.shutdown_request(request)"` | — |
| [SRC-EEF2E6447C-L000788](../../api/omarai.py#L788) | 788 | `"            return"` | — |
| [SRC-EEF2E6447C-L000789](../../api/omarai.py#L789) | 789 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000790](../../api/omarai.py#L790) | 790 | `"            super().process_request(request, client_address)"` | — |
| [SRC-EEF2E6447C-L000791](../../api/omarai.py#L791) | 791 | `"        except BaseException:"` | — |
| [SRC-EEF2E6447C-L000792](../../api/omarai.py#L792) | 792 | `"            # Thread creation can fail before a worker owns the reserved slot."` | — |
| [SRC-EEF2E6447C-L000793](../../api/omarai.py#L793) | 793 | `"            self._connection_slots.release()"` | — |
| [SRC-EEF2E6447C-L000794](../../api/omarai.py#L794) | 794 | `"            raise"` | — |
| [SRC-EEF2E6447C-L000795](../../api/omarai.py#L795) | 795 | `""` | — |
| [SRC-EEF2E6447C-L000796](../../api/omarai.py#L796) | 796 | `"    def process_request_thread(self, request, client_address):"` | — |
| [SRC-EEF2E6447C-L000797](../../api/omarai.py#L797) | 797 | `"        \"\"\"Return a slot after the handler has shut down the accepted socket.\"\"\""` | — |
| [SRC-EEF2E6447C-L000798](../../api/omarai.py#L798) | 798 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000799](../../api/omarai.py#L799) | 799 | `"            super().process_request_thread(request, client_address)"` | — |
| [SRC-EEF2E6447C-L000800](../../api/omarai.py#L800) | 800 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000801](../../api/omarai.py#L801) | 801 | `"            self._connection_slots.release()"` | — |
| [SRC-EEF2E6447C-L000802](../../api/omarai.py#L802) | 802 | `""` | — |
| [SRC-EEF2E6447C-L000803](../../api/omarai.py#L803) | 803 | `""` | — |
| [SRC-EEF2E6447C-L000804](../../api/omarai.py#L804) | 804 | `"def serve(host=\"127.0.0.1\", port=8765):"` | — |
| [SRC-EEF2E6447C-L000805](../../api/omarai.py#L805) | 805 | `"    public_deployment = os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() == \"1\""` | — |
| [SRC-EEF2E6447C-L000806](../../api/omarai.py#L806) | 806 | `"    access_token = os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000807](../../api/omarai.py#L807) | 807 | `"    if host not in (\"127.0.0.1\", \"localhost\", \"::1\") and ("` | — |
| [SRC-EEF2E6447C-L000808](../../api/omarai.py#L808) | 808 | `"        not public_deployment or len(access_token) < 32"` | — |
| [SRC-EEF2E6447C-L000809](../../api/omarai.py#L809) | 809 | `"    ):"` | — |
| [SRC-EEF2E6447C-L000810](../../api/omarai.py#L810) | 810 | `"        raise ValueError("` | — |
| [SRC-EEF2E6447C-L000811](../../api/omarai.py#L811) | 811 | `"                \"Public binding requires OMARAI_PUBLIC_DEPLOYMENT=1 and \""` | — |
| [SRC-EEF2E6447C-L000812](../../api/omarai.py#L812) | 812 | `"                \"a private OMARAI_ACCESS_TOKEN of at least 32 characters.\""` | — |
| [SRC-EEF2E6447C-L000813](../../api/omarai.py#L813) | 813 | `"            )"` | — |
| [SRC-EEF2E6447C-L000814](../../api/omarai.py#L814) | 814 | `"    server = BoundedThreadingHTTPServer((host, port), Handler)"` | — |
| [SRC-EEF2E6447C-L000815](../../api/omarai.py#L815) | 815 | `"    print(f\"Omarai running at http://{host}:{port} — Ctrl+C to stop\")"` | — |
| [SRC-EEF2E6447C-L000816](../../api/omarai.py#L816) | 816 | `"    print(\"Web research agent: /   \|   Lead workspace: /leads\")"` | — |
| [SRC-EEF2E6447C-L000817](../../api/omarai.py#L817) | 817 | `"    try:"` | — |
| [SRC-EEF2E6447C-L000818](../../api/omarai.py#L818) | 818 | `"        server.serve_forever()"` | — |
