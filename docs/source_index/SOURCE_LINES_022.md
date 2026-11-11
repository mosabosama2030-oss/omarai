# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **022**
- سجلات الأسطر: **800**
- النطاق: SRC-EEF2E6447C-L000098 إلى SRC-EEF2E6447C-L000897
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## واجهات API

### FILE-EEF2E6447C — [api/omarai.py](../../api/omarai.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-EEF2E6447C-L000098](../../api/omarai.py#L98) | 98 | `"        \"default-src 'self'; base-uri 'self'; object-src 'none'; frame-ancestors 'none'; \""` | — |
| [SRC-EEF2E6447C-L000099](../../api/omarai.py#L99) | 99 | `"        \"form-action 'self'; connect-src 'self'; img-src 'self' data:; \""` | — |
| [SRC-EEF2E6447C-L000100](../../api/omarai.py#L100) | 100 | `"        f\"script-src {' '.join(script_sources)}; \""` | — |
| [SRC-EEF2E6447C-L000101](../../api/omarai.py#L101) | 101 | `"        f\"style-src {' '.join(style_sources)}; font-src 'self' data:\""` | — |
| [SRC-EEF2E6447C-L000102](../../api/omarai.py#L102) | 102 | `"    )"` | — |
| [SRC-EEF2E6447C-L000103](../../api/omarai.py#L103) | 103 | `"# Bound request-line + header parsing before application code or body processing."` | — |
| [SRC-EEF2E6447C-L000104](../../api/omarai.py#L104) | 104 | `"REQUEST_HEADER_READ_TIMEOUT_SECONDS = 8.0"` | — |
| [SRC-EEF2E6447C-L000105](../../api/omarai.py#L105) | 105 | `"REQUEST_HEADER_IDLE_TIMEOUT_SECONDS = 2.0"` | — |
| [SRC-EEF2E6447C-L000106](../../api/omarai.py#L106) | 106 | `"MAX_REQUEST_HEADER_READ_TIMEOUT_SECONDS = 15.0"` | — |
| [SRC-EEF2E6447C-L000107](../../api/omarai.py#L107) | 107 | `"# Absolute deadline for reading the entire body, not merely a per-read idle timeout."` | — |
| [SRC-EEF2E6447C-L000108](../../api/omarai.py#L108) | 108 | `"REQUEST_BODY_READ_TIMEOUT_SECONDS = 10.0"` | — |
| [SRC-EEF2E6447C-L000109](../../api/omarai.py#L109) | 109 | `"REQUEST_BODY_IDLE_TIMEOUT_SECONDS = 2.0"` | — |
| [SRC-EEF2E6447C-L000110](../../api/omarai.py#L110) | 110 | `"MAX_REQUEST_BODY_READ_TIMEOUT_SECONDS = 30.0"` | — |
| [SRC-EEF2E6447C-L000111](../../api/omarai.py#L111) | 111 | `"REQUEST_BODY_READ_CHUNK_BYTES = 8_192"` | — |
| [SRC-EEF2E6447C-L000112](../../api/omarai.py#L112) | 112 | `""` | — |
| [SRC-EEF2E6447C-L000113](../../api/omarai.py#L113) | 113 | `""` | — |
| [SRC-EEF2E6447C-L000114](../../api/omarai.py#L114) | 114 | `""` | — |
| [SRC-EEF2E6447C-L000115](../../api/omarai.py#L115) | 115 | `"def _lead_store_from_environment() -> LeadStore:"` | — |
| [SRC-EEF2E6447C-L000116](../../api/omarai.py#L116) | 116 | `"    \"\"\"Select managed PostgreSQL when configured; otherwise retain local SQLite.\"\"\""` | — |
| [SRC-EEF2E6447C-L000117](../../api/omarai.py#L117) | 117 | `"    database_url = ("` | — |
| [SRC-EEF2E6447C-L000118](../../api/omarai.py#L118) | 118 | `"        os.getenv(\"OMARAI_DATABASE_URL\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000119](../../api/omarai.py#L119) | 119 | `"        or os.getenv(\"DATABASE_URL\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000120](../../api/omarai.py#L120) | 120 | `"    )"` | — |
| [SRC-EEF2E6447C-L000121](../../api/omarai.py#L121) | 121 | `"    configured_path = os.getenv(\"OMARAI_DB_PATH\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000122](../../api/omarai.py#L122) | 122 | `"    if database_url and configured_path:"` | — |
| [SRC-EEF2E6447C-L000123](../../api/omarai.py#L123) | 123 | `"        raise ValueError("` | — |
| [SRC-EEF2E6447C-L000124](../../api/omarai.py#L124) | 124 | `"            \"configure either OMARAI_DATABASE_URL/DATABASE_URL or OMARAI_DB_PATH, not both\""` | — |
| [SRC-EEF2E6447C-L000125](../../api/omarai.py#L125) | 125 | `"        )"` | — |
| [SRC-EEF2E6447C-L000126](../../api/omarai.py#L126) | 126 | `"    return LeadStore(configured_path or None, database_url=database_url or None)"` | — |
| [SRC-EEF2E6447C-L000127](../../api/omarai.py#L127) | 127 | `""` | — |
| [SRC-EEF2E6447C-L000128](../../api/omarai.py#L128) | 128 | `""` | — |
| [SRC-EEF2E6447C-L000129](../../api/omarai.py#L129) | 129 | `"def _profile_terms(value, field_name: str) -> tuple[str, ...]:"` | — |
| [SRC-EEF2E6447C-L000130](../../api/omarai.py#L130) | 130 | `"    \"\"\"Validate bounded ProductProfile/MarketProfile string arrays.\"\"\""` | — |
| [SRC-EEF2E6447C-L000131](../../api/omarai.py#L131) | 131 | `"    if value is None:"` | — |
| [SRC-EEF2E6447C-L000132](../../api/omarai.py#L132) | 132 | `"        return ()"` | — |
| [SRC-EEF2E6447C-L000133](../../api/omarai.py#L133) | 133 | `"    if not isinstance(value, list) or len(value) > 40:"` | — |
| [SRC-EEF2E6447C-L000134](../../api/omarai.py#L134) | 134 | `"        raise ValueError(f\"{field_name} must be a list of at most 40 strings\")"` | — |
| [SRC-EEF2E6447C-L000135](../../api/omarai.py#L135) | 135 | `"    if any(not isinstance(item, str) or len(item) > 240 for item in value):"` | — |
| [SRC-EEF2E6447C-L000136](../../api/omarai.py#L136) | 136 | `"        raise ValueError(f\"{field_name} items must be strings of at most 240 characters\")"` | — |
| [SRC-EEF2E6447C-L000137](../../api/omarai.py#L137) | 137 | `"    return tuple(value)"` | — |
| [SRC-EEF2E6447C-L000138](../../api/omarai.py#L138) | 138 | `""` | — |
| [SRC-EEF2E6447C-L000139](../../api/omarai.py#L139) | 139 | `""` | — |
| [SRC-EEF2E6447C-L000140](../../api/omarai.py#L140) | 140 | `"def _product_market_from_payload(data: dict):"` | — |
| [SRC-EEF2E6447C-L000141](../../api/omarai.py#L141) | 141 | `"    product_data = data.get(\"product\")"` | — |
| [SRC-EEF2E6447C-L000142](../../api/omarai.py#L142) | 142 | `"    market_data = data.get(\"market\")"` | — |
| [SRC-EEF2E6447C-L000143](../../api/omarai.py#L143) | 143 | `"    if not isinstance(product_data, dict) or not isinstance(market_data, dict):"` | — |
| [SRC-EEF2E6447C-L000144](../../api/omarai.py#L144) | 144 | `"        raise TypeError(\"product and market objects are required\")"` | — |
| [SRC-EEF2E6447C-L000145](../../api/omarai.py#L145) | 145 | `"    product = ProductProfile("` | — |
| [SRC-EEF2E6447C-L000146](../../api/omarai.py#L146) | 146 | `"        name=product_data.get(\"name\", \"\"),"` | — |
| [SRC-EEF2E6447C-L000147](../../api/omarai.py#L147) | 147 | `"        aliases=_profile_terms(product_data.get(\"aliases\"), \"aliases\"),"` | — |
| [SRC-EEF2E6447C-L000148](../../api/omarai.py#L148) | 148 | `"        category_path=_profile_terms(product_data.get(\"category_path\"), \"category_path\"),"` | — |
| [SRC-EEF2E6447C-L000149](../../api/omarai.py#L149) | 149 | `"        use_cases=_profile_terms(product_data.get(\"use_cases\"), \"use_cases\"),"` | — |
| [SRC-EEF2E6447C-L000150](../../api/omarai.py#L150) | 150 | `"        problems_solved=_profile_terms(product_data.get(\"problems_solved\"), \"problems_solved\"),"` | — |
| [SRC-EEF2E6447C-L000151](../../api/omarai.py#L151) | 151 | `"    )"` | — |
| [SRC-EEF2E6447C-L000152](../../api/omarai.py#L152) | 152 | `"    market = MarketProfile("` | — |
| [SRC-EEF2E6447C-L000153](../../api/omarai.py#L153) | 153 | `"        locations=_profile_terms(market_data.get(\"locations\"), \"locations\"),"` | — |
| [SRC-EEF2E6447C-L000154](../../api/omarai.py#L154) | 154 | `"        industries=_profile_terms(market_data.get(\"industries\"), \"industries\"),"` | — |
| [SRC-EEF2E6447C-L000155](../../api/omarai.py#L155) | 155 | `"        customer_types=_profile_terms(market_data.get(\"customer_types\"), \"customer_types\"),"` | — |
| [SRC-EEF2E6447C-L000156](../../api/omarai.py#L156) | 156 | `"        decision_roles=_profile_terms(market_data.get(\"decision_roles\"), \"decision_roles\"),"` | — |
| [SRC-EEF2E6447C-L000157](../../api/omarai.py#L157) | 157 | `"        exclusions=_profile_terms(market_data.get(\"exclusions\"), \"exclusions\"),"` | — |
| [SRC-EEF2E6447C-L000158](../../api/omarai.py#L158) | 158 | `"    )"` | — |
| [SRC-EEF2E6447C-L000159](../../api/omarai.py#L159) | 159 | `"    locale = data.get(\"locale\", \"auto\")"` | — |
| [SRC-EEF2E6447C-L000160](../../api/omarai.py#L160) | 160 | `"    if not isinstance(locale, str) or locale not in {\"auto\", \"ar\", \"en\", \"mixed\"}:"` | — |
| [SRC-EEF2E6447C-L000161](../../api/omarai.py#L161) | 161 | `"        raise ValueError(\"locale must be auto, ar, en, or mixed\")"` | — |
| [SRC-EEF2E6447C-L000162](../../api/omarai.py#L162) | 162 | `"    return product, market, locale"` | — |
| [SRC-EEF2E6447C-L000163](../../api/omarai.py#L163) | 163 | `""` | — |
| [SRC-EEF2E6447C-L000164](../../api/omarai.py#L164) | 164 | `""` | — |
| [SRC-EEF2E6447C-L000165](../../api/omarai.py#L165) | 165 | `"class _DeadlineRequestReader:"` | — |
| [SRC-EEF2E6447C-L000166](../../api/omarai.py#L166) | 166 | `"    \"\"\"Read HTTP header lines with one absolute deadline across all fragments."` | — |
| [SRC-EEF2E6447C-L000167](../../api/omarai.py#L167) | 167 | `""` | — |
| [SRC-EEF2E6447C-L000168](../../api/omarai.py#L168) | 168 | `"    The standard buffered readline can wait indefinitely for a newline if a"` | — |
| [SRC-EEF2E6447C-L000169](../../api/omarai.py#L169) | 169 | `"    client keeps trickling bytes. This reader checks the same deadline before"` | — |
| [SRC-EEF2E6447C-L000170](../../api/omarai.py#L170) | 170 | `"    every socket read and buffers only bounded look-ahead so request body bytes"` | — |
| [SRC-EEF2E6447C-L000171](../../api/omarai.py#L171) | 171 | `"    received with the headers are preserved for read1()."` | — |
| [SRC-EEF2E6447C-L000172](../../api/omarai.py#L172) | 172 | `"    \"\"\""` | — |
| [SRC-EEF2E6447C-L000173](../../api/omarai.py#L173) | 173 | `""` | — |
| [SRC-EEF2E6447C-L000174](../../api/omarai.py#L174) | 174 | `"    def __init__(self, connection, handler):"` | — |
| [SRC-EEF2E6447C-L000175](../../api/omarai.py#L175) | 175 | `"        self.connection = connection"` | — |
| [SRC-EEF2E6447C-L000176](../../api/omarai.py#L176) | 176 | `"        self.handler = handler"` | — |
| [SRC-EEF2E6447C-L000177](../../api/omarai.py#L177) | 177 | `"        self._buffer = bytearray()"` | — |
| [SRC-EEF2E6447C-L000178](../../api/omarai.py#L178) | 178 | `""` | — |
| [SRC-EEF2E6447C-L000179](../../api/omarai.py#L179) | 179 | `"    def readline(self, limit=-1):"` | — |
| [SRC-EEF2E6447C-L000180](../../api/omarai.py#L180) | 180 | `"        if limit == 0:"` | — |
| [SRC-EEF2E6447C-L000181](../../api/omarai.py#L181) | 181 | `"            return b\"\""` | — |
| [SRC-EEF2E6447C-L000182](../../api/omarai.py#L182) | 182 | `"        max_bytes = int(limit) if limit is not None and limit > 0 else 65_537"` | — |
| [SRC-EEF2E6447C-L000183](../../api/omarai.py#L183) | 183 | `"        previous_timeout = self.connection.gettimeout()"` | — |
| [SRC-EEF2E6447C-L000184](../../api/omarai.py#L184) | 184 | `"        line = bytearray()"` | — |
| [SRC-EEF2E6447C-L000185](../../api/omarai.py#L185) | 185 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000186](../../api/omarai.py#L186) | 186 | `"            while len(line) < max_bytes:"` | — |
| [SRC-EEF2E6447C-L000187](../../api/omarai.py#L187) | 187 | `"                deadline = getattr(self.handler, \"_request_header_deadline\", None)"` | — |
| [SRC-EEF2E6447C-L000188](../../api/omarai.py#L188) | 188 | `"                if deadline is None:"` | — |
| [SRC-EEF2E6447C-L000189](../../api/omarai.py#L189) | 189 | `"                    raise TimeoutError(\"request-header deadline is not active\")"` | — |
| [SRC-EEF2E6447C-L000190](../../api/omarai.py#L190) | 190 | `"                remaining = deadline - time.monotonic()"` | — |
| [SRC-EEF2E6447C-L000191](../../api/omarai.py#L191) | 191 | `"                if remaining <= 0:"` | — |
| [SRC-EEF2E6447C-L000192](../../api/omarai.py#L192) | 192 | `"                    raise TimeoutError(\"absolute request-header deadline exceeded\")"` | — |
| [SRC-EEF2E6447C-L000193](../../api/omarai.py#L193) | 193 | `""` | — |
| [SRC-EEF2E6447C-L000194](../../api/omarai.py#L194) | 194 | `"                newline_index = self._buffer.find(b\"\\n\")"` | — |
| [SRC-EEF2E6447C-L000195](../../api/omarai.py#L195) | 195 | `"                if newline_index >= 0:"` | — |
| [SRC-EEF2E6447C-L000196](../../api/omarai.py#L196) | 196 | `"                    take = min(newline_index + 1, max_bytes - len(line))"` | — |
| [SRC-EEF2E6447C-L000197](../../api/omarai.py#L197) | 197 | `"                    line.extend(self._buffer[:take])"` | — |
| [SRC-EEF2E6447C-L000198](../../api/omarai.py#L198) | 198 | `"                    del self._buffer[:take]"` | — |
| [SRC-EEF2E6447C-L000199](../../api/omarai.py#L199) | 199 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000200](../../api/omarai.py#L200) | 200 | `""` | — |
| [SRC-EEF2E6447C-L000201](../../api/omarai.py#L201) | 201 | `"                if self._buffer:"` | — |
| [SRC-EEF2E6447C-L000202](../../api/omarai.py#L202) | 202 | `"                    take = min(len(self._buffer), max_bytes - len(line))"` | — |
| [SRC-EEF2E6447C-L000203](../../api/omarai.py#L203) | 203 | `"                    line.extend(self._buffer[:take])"` | — |
| [SRC-EEF2E6447C-L000204](../../api/omarai.py#L204) | 204 | `"                    del self._buffer[:take]"` | — |
| [SRC-EEF2E6447C-L000205](../../api/omarai.py#L205) | 205 | `"                    if len(line) >= max_bytes:"` | — |
| [SRC-EEF2E6447C-L000206](../../api/omarai.py#L206) | 206 | `"                        break"` | — |
| [SRC-EEF2E6447C-L000207](../../api/omarai.py#L207) | 207 | `""` | — |
| [SRC-EEF2E6447C-L000208](../../api/omarai.py#L208) | 208 | `"                remaining = deadline - time.monotonic()"` | — |
| [SRC-EEF2E6447C-L000209](../../api/omarai.py#L209) | 209 | `"                if remaining <= 0:"` | — |
| [SRC-EEF2E6447C-L000210](../../api/omarai.py#L210) | 210 | `"                    raise TimeoutError(\"absolute request-header deadline exceeded\")"` | — |
| [SRC-EEF2E6447C-L000211](../../api/omarai.py#L211) | 211 | `"                idle_timeout = max("` | — |
| [SRC-EEF2E6447C-L000212](../../api/omarai.py#L212) | 212 | `"                    0.1,"` | — |
| [SRC-EEF2E6447C-L000213](../../api/omarai.py#L213) | 213 | `"                    min("` | — |
| [SRC-EEF2E6447C-L000214](../../api/omarai.py#L214) | 214 | `"                        float(REQUEST_HEADER_IDLE_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000215](../../api/omarai.py#L215) | 215 | `"                        MAX_REQUEST_HEADER_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000216](../../api/omarai.py#L216) | 216 | `"                    ),"` | — |
| [SRC-EEF2E6447C-L000217](../../api/omarai.py#L217) | 217 | `"                )"` | — |
| [SRC-EEF2E6447C-L000218](../../api/omarai.py#L218) | 218 | `"                self.connection.settimeout(min(idle_timeout, remaining))"` | — |
| [SRC-EEF2E6447C-L000219](../../api/omarai.py#L219) | 219 | `"                chunk = self.connection.recv(min(4_096, max_bytes - len(line)))"` | — |
| [SRC-EEF2E6447C-L000220](../../api/omarai.py#L220) | 220 | `"                if not chunk:"` | — |
| [SRC-EEF2E6447C-L000221](../../api/omarai.py#L221) | 221 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000222](../../api/omarai.py#L222) | 222 | `"                self._buffer.extend(chunk)"` | — |
| [SRC-EEF2E6447C-L000223](../../api/omarai.py#L223) | 223 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000224](../../api/omarai.py#L224) | 224 | `"            try:"` | — |
| [SRC-EEF2E6447C-L000225](../../api/omarai.py#L225) | 225 | `"                self.connection.settimeout(previous_timeout)"` | — |
| [SRC-EEF2E6447C-L000226](../../api/omarai.py#L226) | 226 | `"            except OSError:"` | — |
| [SRC-EEF2E6447C-L000227](../../api/omarai.py#L227) | 227 | `"                pass"` | — |
| [SRC-EEF2E6447C-L000228](../../api/omarai.py#L228) | 228 | `"        return bytes(line)"` | — |
| [SRC-EEF2E6447C-L000229](../../api/omarai.py#L229) | 229 | `""` | — |
| [SRC-EEF2E6447C-L000230](../../api/omarai.py#L230) | 230 | `"    def read1(self, size=-1):"` | — |
| [SRC-EEF2E6447C-L000231](../../api/omarai.py#L231) | 231 | `"        \"\"\"Read one chunk; body code applies its own idle and absolute deadlines.\"\"\""` | — |
| [SRC-EEF2E6447C-L000232](../../api/omarai.py#L232) | 232 | `"        if size == 0:"` | — |
| [SRC-EEF2E6447C-L000233](../../api/omarai.py#L233) | 233 | `"            return b\"\""` | — |
| [SRC-EEF2E6447C-L000234](../../api/omarai.py#L234) | 234 | `"        if size is None or size < 0:"` | — |
| [SRC-EEF2E6447C-L000235](../../api/omarai.py#L235) | 235 | `"            size = 8_192"` | — |
| [SRC-EEF2E6447C-L000236](../../api/omarai.py#L236) | 236 | `"        if self._buffer:"` | — |
| [SRC-EEF2E6447C-L000237](../../api/omarai.py#L237) | 237 | `"            take = min(len(self._buffer), size)"` | — |
| [SRC-EEF2E6447C-L000238](../../api/omarai.py#L238) | 238 | `"            data = bytes(self._buffer[:take])"` | — |
| [SRC-EEF2E6447C-L000239](../../api/omarai.py#L239) | 239 | `"            del self._buffer[:take]"` | — |
| [SRC-EEF2E6447C-L000240](../../api/omarai.py#L240) | 240 | `"            return data"` | — |
| [SRC-EEF2E6447C-L000241](../../api/omarai.py#L241) | 241 | `"        return self.connection.recv(size)"` | — |
| [SRC-EEF2E6447C-L000242](../../api/omarai.py#L242) | 242 | `""` | — |
| [SRC-EEF2E6447C-L000243](../../api/omarai.py#L243) | 243 | `"    def close(self):"` | — |
| [SRC-EEF2E6447C-L000244](../../api/omarai.py#L244) | 244 | `"        # The request handler owns the socket and closes its output stream."` | — |
| [SRC-EEF2E6447C-L000245](../../api/omarai.py#L245) | 245 | `"        return None"` | — |
| [SRC-EEF2E6447C-L000246](../../api/omarai.py#L246) | 246 | `""` | — |
| [SRC-EEF2E6447C-L000247](../../api/omarai.py#L247) | 247 | `""` | — |
| [SRC-EEF2E6447C-L000248](../../api/omarai.py#L248) | 248 | `"def _configured_agent_concurrency_limit() -> int:"` | — |
| [SRC-EEF2E6447C-L000249](../../api/omarai.py#L249) | 249 | `"    \"\"\"Return a process-local cap for expensive research and diagnostics operations.\"\"\""` | — |
| [SRC-EEF2E6447C-L000250](../../api/omarai.py#L250) | 250 | `"    try:"` | — |
| [SRC-EEF2E6447C-L000251](../../api/omarai.py#L251) | 251 | `"        configured = int(os.getenv(\"OMARAI_MAX_CONCURRENT_AGENT_REQUESTS\", \"4\").strip())"` | — |
| [SRC-EEF2E6447C-L000252](../../api/omarai.py#L252) | 252 | `"    except ValueError:"` | — |
| [SRC-EEF2E6447C-L000253](../../api/omarai.py#L253) | 253 | `"        configured = 4"` | — |
| [SRC-EEF2E6447C-L000254](../../api/omarai.py#L254) | 254 | `"    return max(1, min(configured, 8))"` | — |
| [SRC-EEF2E6447C-L000255](../../api/omarai.py#L255) | 255 | `""` | — |
| [SRC-EEF2E6447C-L000256](../../api/omarai.py#L256) | 256 | `""` | — |
| [SRC-EEF2E6447C-L000257](../../api/omarai.py#L257) | 257 | `"DEFAULT_HTTP_CONNECTION_LIMIT = 32"` | — |
| [SRC-EEF2E6447C-L000258](../../api/omarai.py#L258) | 258 | `"MAX_HTTP_CONNECTION_LIMIT = 128"` | — |
| [SRC-EEF2E6447C-L000259](../../api/omarai.py#L259) | 259 | `""` | — |
| [SRC-EEF2E6447C-L000260](../../api/omarai.py#L260) | 260 | `""` | — |
| [SRC-EEF2E6447C-L000261](../../api/omarai.py#L261) | 261 | `"def _configured_http_connection_limit() -> int:"` | — |
| [SRC-EEF2E6447C-L000262](../../api/omarai.py#L262) | 262 | `"    \"\"\"Return the bounded number of live HTTP handler threads for this process.\"\"\""` | — |
| [SRC-EEF2E6447C-L000263](../../api/omarai.py#L263) | 263 | `"    try:"` | — |
| [SRC-EEF2E6447C-L000264](../../api/omarai.py#L264) | 264 | `"        configured = int(os.getenv(\"OMARAI_MAX_CONCURRENT_HTTP_CONNECTIONS\", \"32\").strip())"` | — |
| [SRC-EEF2E6447C-L000265](../../api/omarai.py#L265) | 265 | `"    except ValueError:"` | — |
| [SRC-EEF2E6447C-L000266](../../api/omarai.py#L266) | 266 | `"        configured = DEFAULT_HTTP_CONNECTION_LIMIT"` | — |
| [SRC-EEF2E6447C-L000267](../../api/omarai.py#L267) | 267 | `"    return max(1, min(configured, MAX_HTTP_CONNECTION_LIMIT))"` | — |
| [SRC-EEF2E6447C-L000268](../../api/omarai.py#L268) | 268 | `""` | — |
| [SRC-EEF2E6447C-L000269](../../api/omarai.py#L269) | 269 | `""` | — |
| [SRC-EEF2E6447C-L000270](../../api/omarai.py#L270) | 270 | `"BUILD_SHA_FILE = Path(__file__).resolve().parents[1] / \"BUILD_SHA\""` | — |
| [SRC-EEF2E6447C-L000271](../../api/omarai.py#L271) | 271 | `"_PLATFORM_BUILD_SHA_ENVIRONMENTS = ("` | — |
| [SRC-EEF2E6447C-L000272](../../api/omarai.py#L272) | 272 | `"    (\"RAILWAY_GIT_COMMIT_SHA\", \"platform:railway\"),"` | — |
| [SRC-EEF2E6447C-L000273](../../api/omarai.py#L273) | 273 | `"    (\"RENDER_GIT_COMMIT\", \"platform:render\"),"` | — |
| [SRC-EEF2E6447C-L000274](../../api/omarai.py#L274) | 274 | `")"` | — |
| [SRC-EEF2E6447C-L000275](../../api/omarai.py#L275) | 275 | `""` | — |
| [SRC-EEF2E6447C-L000276](../../api/omarai.py#L276) | 276 | `""` | — |
| [SRC-EEF2E6447C-L000277](../../api/omarai.py#L277) | 277 | `"def _valid_build_sha(value: str) -> bool:"` | — |
| [SRC-EEF2E6447C-L000278](../../api/omarai.py#L278) | 278 | `"    candidate = value.strip().lower()"` | — |
| [SRC-EEF2E6447C-L000279](../../api/omarai.py#L279) | 279 | `"    return len(candidate) == 40 and all(char in \"0123456789abcdef\" for char in candidate)"` | — |
| [SRC-EEF2E6447C-L000280](../../api/omarai.py#L280) | 280 | `""` | — |
| [SRC-EEF2E6447C-L000281](../../api/omarai.py#L281) | 281 | `""` | — |
| [SRC-EEF2E6447C-L000282](../../api/omarai.py#L282) | 282 | `"def _build_identity() -> tuple[str, str]:"` | — |
| [SRC-EEF2E6447C-L000283](../../api/omarai.py#L283) | 283 | `"    \"\"\"Prefer immutable image metadata, then documented hosting-provided Git SHAs.\"\"\""` | — |
| [SRC-EEF2E6447C-L000284](../../api/omarai.py#L284) | 284 | `"    try:"` | — |
| [SRC-EEF2E6447C-L000285](../../api/omarai.py#L285) | 285 | `"        baked = BUILD_SHA_FILE.read_text(encoding=\"ascii\").strip().lower()"` | — |
| [SRC-EEF2E6447C-L000286](../../api/omarai.py#L286) | 286 | `"    except (OSError, UnicodeError):"` | — |
| [SRC-EEF2E6447C-L000287](../../api/omarai.py#L287) | 287 | `"        baked = \"\""` | — |
| [SRC-EEF2E6447C-L000288](../../api/omarai.py#L288) | 288 | `"    if _valid_build_sha(baked):"` | — |
| [SRC-EEF2E6447C-L000289](../../api/omarai.py#L289) | 289 | `"        return baked, \"image_baked\""` | — |
| [SRC-EEF2E6447C-L000290](../../api/omarai.py#L290) | 290 | `""` | — |
| [SRC-EEF2E6447C-L000291](../../api/omarai.py#L291) | 291 | `"    for environment_name, source in _PLATFORM_BUILD_SHA_ENVIRONMENTS:"` | — |
| [SRC-EEF2E6447C-L000292](../../api/omarai.py#L292) | 292 | `"        candidate = os.getenv(environment_name, \"\").strip().lower()"` | — |
| [SRC-EEF2E6447C-L000293](../../api/omarai.py#L293) | 293 | `"        if _valid_build_sha(candidate):"` | — |
| [SRC-EEF2E6447C-L000294](../../api/omarai.py#L294) | 294 | `"            return candidate, source"` | — |
| [SRC-EEF2E6447C-L000295](../../api/omarai.py#L295) | 295 | `"    return \"unknown\", \"unknown\""` | — |
| [SRC-EEF2E6447C-L000296](../../api/omarai.py#L296) | 296 | `""` | — |
| [SRC-EEF2E6447C-L000297](../../api/omarai.py#L297) | 297 | `""` | — |
| [SRC-EEF2E6447C-L000298](../../api/omarai.py#L298) | 298 | `"def _build_sha() -> str:"` | — |
| [SRC-EEF2E6447C-L000299](../../api/omarai.py#L299) | 299 | `"    \"\"\"Return a validated source SHA, or 'unknown' when no trusted build evidence exists.\"\"\""` | — |
| [SRC-EEF2E6447C-L000300](../../api/omarai.py#L300) | 300 | `"    return _build_identity()[0]"` | — |
| [SRC-EEF2E6447C-L000301](../../api/omarai.py#L301) | 301 | `""` | — |
| [SRC-EEF2E6447C-L000302](../../api/omarai.py#L302) | 302 | `""` | — |
| [SRC-EEF2E6447C-L000303](../../api/omarai.py#L303) | 303 | `"class Handler(BaseHTTPRequestHandler):"` | — |
| [SRC-EEF2E6447C-L000304](../../api/omarai.py#L304) | 304 | `"    def setup(self):"` | — |
| [SRC-EEF2E6447C-L000305](../../api/omarai.py#L305) | 305 | `"        \"\"\"Install a reader with a strict deadline for the request line and headers.\"\"\""` | — |
| [SRC-EEF2E6447C-L000306](../../api/omarai.py#L306) | 306 | `"        self.connection = self.request"` | — |
| [SRC-EEF2E6447C-L000307](../../api/omarai.py#L307) | 307 | `"        if self.timeout is not None:"` | — |
| [SRC-EEF2E6447C-L000308](../../api/omarai.py#L308) | 308 | `"            self.connection.settimeout(self.timeout)"` | — |
| [SRC-EEF2E6447C-L000309](../../api/omarai.py#L309) | 309 | `"        self._request_header_deadline = None"` | — |
| [SRC-EEF2E6447C-L000310](../../api/omarai.py#L310) | 310 | `"        self.rfile = _DeadlineRequestReader(self.connection, self)"` | — |
| [SRC-EEF2E6447C-L000311](../../api/omarai.py#L311) | 311 | `"        self.wfile = self.connection.makefile(\"wb\", self.wbufsize)"` | — |
| [SRC-EEF2E6447C-L000312](../../api/omarai.py#L312) | 312 | `""` | — |
| [SRC-EEF2E6447C-L000313](../../api/omarai.py#L313) | 313 | `"    def handle_one_request(self):"` | — |
| [SRC-EEF2E6447C-L000314](../../api/omarai.py#L314) | 314 | `"        timeout = max("` | — |
| [SRC-EEF2E6447C-L000315](../../api/omarai.py#L315) | 315 | `"            0.1,"` | — |
| [SRC-EEF2E6447C-L000316](../../api/omarai.py#L316) | 316 | `"            min("` | — |
| [SRC-EEF2E6447C-L000317](../../api/omarai.py#L317) | 317 | `"                float(REQUEST_HEADER_READ_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000318](../../api/omarai.py#L318) | 318 | `"                MAX_REQUEST_HEADER_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000319](../../api/omarai.py#L319) | 319 | `"            ),"` | — |
| [SRC-EEF2E6447C-L000320](../../api/omarai.py#L320) | 320 | `"        )"` | — |
| [SRC-EEF2E6447C-L000321](../../api/omarai.py#L321) | 321 | `"        self._request_header_deadline = time.monotonic() + timeout"` | — |
| [SRC-EEF2E6447C-L000322](../../api/omarai.py#L322) | 322 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000323](../../api/omarai.py#L323) | 323 | `"            super().handle_one_request()"` | — |
| [SRC-EEF2E6447C-L000324](../../api/omarai.py#L324) | 324 | `"        except TimeoutError:"` | — |
| [SRC-EEF2E6447C-L000325](../../api/omarai.py#L325) | 325 | `"            # Incomplete request line/headers are untrusted protocol input;"` | — |
| [SRC-EEF2E6447C-L000326](../../api/omarai.py#L326) | 326 | `"            # close the socket without trying to parse or answer a partial request."` | — |
| [SRC-EEF2E6447C-L000327](../../api/omarai.py#L327) | 327 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000328](../../api/omarai.py#L328) | 328 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000329](../../api/omarai.py#L329) | 329 | `"            self._request_header_deadline = None"` | — |
| [SRC-EEF2E6447C-L000330](../../api/omarai.py#L330) | 330 | `""` | — |
| [SRC-EEF2E6447C-L000331](../../api/omarai.py#L331) | 331 | `"    def parse_request(self):"` | — |
| [SRC-EEF2E6447C-L000332](../../api/omarai.py#L332) | 332 | `"        \"\"\"Reject ambiguous HTTP message framing before dispatching any handler.\"\"\""` | — |
| [SRC-EEF2E6447C-L000333](../../api/omarai.py#L333) | 333 | `"        if not super().parse_request():"` | — |
| [SRC-EEF2E6447C-L000334](../../api/omarai.py#L334) | 334 | `"            return False"` | — |
| [SRC-EEF2E6447C-L000335](../../api/omarai.py#L335) | 335 | `""` | — |
| [SRC-EEF2E6447C-L000336](../../api/omarai.py#L336) | 336 | `"        transfer_encodings = self.headers.get_all(\"Transfer-Encoding\", [])"` | — |
| [SRC-EEF2E6447C-L000337](../../api/omarai.py#L337) | 337 | `"        if transfer_encodings:"` | — |
| [SRC-EEF2E6447C-L000338](../../api/omarai.py#L338) | 338 | `"            # This API does not implement chunked request decoding. Never let a"` | — |
| [SRC-EEF2E6447C-L000339](../../api/omarai.py#L339) | 339 | `"            # proxy/backend disagree about where the request body ends."` | — |
| [SRC-EEF2E6447C-L000340](../../api/omarai.py#L340) | 340 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000341](../../api/omarai.py#L341) | 341 | `"            self.send_error(400, \"Transfer-Encoding is not supported\")"` | — |
| [SRC-EEF2E6447C-L000342](../../api/omarai.py#L342) | 342 | `"            return False"` | — |
| [SRC-EEF2E6447C-L000343](../../api/omarai.py#L343) | 343 | `""` | — |
| [SRC-EEF2E6447C-L000344](../../api/omarai.py#L344) | 344 | `"        content_lengths = self.headers.get_all(\"Content-Length\", [])"` | — |
| [SRC-EEF2E6447C-L000345](../../api/omarai.py#L345) | 345 | `"        if len(content_lengths) > 1:"` | — |
| [SRC-EEF2E6447C-L000346](../../api/omarai.py#L346) | 346 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000347](../../api/omarai.py#L347) | 347 | `"            self.send_error(400, \"Multiple Content-Length headers are not supported\")"` | — |
| [SRC-EEF2E6447C-L000348](../../api/omarai.py#L348) | 348 | `"            return False"` | — |
| [SRC-EEF2E6447C-L000349](../../api/omarai.py#L349) | 349 | `""` | — |
| [SRC-EEF2E6447C-L000350](../../api/omarai.py#L350) | 350 | `"        if content_lengths:"` | — |
| [SRC-EEF2E6447C-L000351](../../api/omarai.py#L351) | 351 | `"            raw_size = content_lengths[0].strip()"` | — |
| [SRC-EEF2E6447C-L000352](../../api/omarai.py#L352) | 352 | `"            if not raw_size or not raw_size.isascii() or not raw_size.isdecimal():"` | — |
| [SRC-EEF2E6447C-L000353](../../api/omarai.py#L353) | 353 | `"                self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000354](../../api/omarai.py#L354) | 354 | `"                self.send_error(400, \"valid Content-Length is required\")"` | — |
| [SRC-EEF2E6447C-L000355](../../api/omarai.py#L355) | 355 | `"                return False"` | — |
| [SRC-EEF2E6447C-L000356](../../api/omarai.py#L356) | 356 | `"            if self.command != \"POST\" and raw_size.lstrip(\"0\"):"` | — |
| [SRC-EEF2E6447C-L000357](../../api/omarai.py#L357) | 357 | `"                # GET/HEAD/other methods are not allowed to leave unread bytes"` | — |
| [SRC-EEF2E6447C-L000358](../../api/omarai.py#L358) | 358 | `"                # on a persistent connection."` | — |
| [SRC-EEF2E6447C-L000359](../../api/omarai.py#L359) | 359 | `"                self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000360](../../api/omarai.py#L360) | 360 | `"                self.send_error(400, \"Content-Length body is not supported for this method\")"` | — |
| [SRC-EEF2E6447C-L000361](../../api/omarai.py#L361) | 361 | `"                return False"` | — |
| [SRC-EEF2E6447C-L000362](../../api/omarai.py#L362) | 362 | `""` | — |
| [SRC-EEF2E6447C-L000363](../../api/omarai.py#L363) | 363 | `"        return True"` | — |
| [SRC-EEF2E6447C-L000364](../../api/omarai.py#L364) | 364 | `""` | — |
| [SRC-EEF2E6447C-L000365](../../api/omarai.py#L365) | 365 | `"    store = _lead_store_from_environment()"` | — |
| [SRC-EEF2E6447C-L000366](../../api/omarai.py#L366) | 366 | `"    _rate_lock = threading.Lock()"` | — |
| [SRC-EEF2E6447C-L000367](../../api/omarai.py#L367) | 367 | `"    _request_times: ClassVar[dict[str, deque[float]]] = defaultdict(deque)"` | — |
| [SRC-EEF2E6447C-L000368](../../api/omarai.py#L368) | 368 | `"    _rate_last_cleanup: ClassVar[float] = 0.0"` | — |
| [SRC-EEF2E6447C-L000369](../../api/omarai.py#L369) | 369 | `"    RATE_LIMIT_REQUESTS = 20"` | — |
| [SRC-EEF2E6447C-L000370](../../api/omarai.py#L370) | 370 | `"    RATE_LIMIT_WINDOW_SECONDS = 60"` | — |
| [SRC-EEF2E6447C-L000371](../../api/omarai.py#L371) | 371 | `"    RATE_LIMIT_CLEANUP_INTERVAL_SECONDS = 60"` | — |
| [SRC-EEF2E6447C-L000372](../../api/omarai.py#L372) | 372 | `"    # Reserve the final bucket for clients beyond the per-process tracking ceiling."` | — |
| [SRC-EEF2E6447C-L000373](../../api/omarai.py#L373) | 373 | `"    MAX_RATE_LIMIT_CLIENT_BUCKETS = 4096"` | — |
| [SRC-EEF2E6447C-L000374](../../api/omarai.py#L374) | 374 | `"    RATE_LIMIT_OVERFLOW_KEY = \"__omarai_overflow__\""` | — |
| [SRC-EEF2E6447C-L000375](../../api/omarai.py#L375) | 375 | `"    AGENT_CONCURRENCY_LIMIT = _configured_agent_concurrency_limit()"` | — |
| [SRC-EEF2E6447C-L000376](../../api/omarai.py#L376) | 376 | `"    _agent_semaphore = threading.BoundedSemaphore(AGENT_CONCURRENCY_LIMIT)"` | — |
| [SRC-EEF2E6447C-L000377](../../api/omarai.py#L377) | 377 | `""` | — |
| [SRC-EEF2E6447C-L000378](../../api/omarai.py#L378) | 378 | `"    def _run_bounded_agent_operation(self, operation):"` | — |
| [SRC-EEF2E6447C-L000379](../../api/omarai.py#L379) | 379 | `"        \"\"\"Run an expensive operation only when a process-local slot is available.\"\"\""` | — |
| [SRC-EEF2E6447C-L000380](../../api/omarai.py#L380) | 380 | `"        cls = type(self)"` | — |
| [SRC-EEF2E6447C-L000381](../../api/omarai.py#L381) | 381 | `"        if not cls._agent_semaphore.acquire(blocking=False):"` | — |
| [SRC-EEF2E6447C-L000382](../../api/omarai.py#L382) | 382 | `"            return self.respond("` | — |
| [SRC-EEF2E6447C-L000383](../../api/omarai.py#L383) | 383 | `"                503,"` | — |
| [SRC-EEF2E6447C-L000384](../../api/omarai.py#L384) | 384 | `"                {"` | — |
| [SRC-EEF2E6447C-L000385](../../api/omarai.py#L385) | 385 | `"                    \"error\": \"خدمة البحث مشغولة حاليًا؛ أعد المحاولة بعد قليل.\","` | — |
| [SRC-EEF2E6447C-L000386](../../api/omarai.py#L386) | 386 | `"                    \"retry_after_seconds\": 5,"` | — |
| [SRC-EEF2E6447C-L000387](../../api/omarai.py#L387) | 387 | `"                    \"process_concurrency_limit\": cls.AGENT_CONCURRENCY_LIMIT,"` | — |
| [SRC-EEF2E6447C-L000388](../../api/omarai.py#L388) | 388 | `"                },"` | — |
| [SRC-EEF2E6447C-L000389](../../api/omarai.py#L389) | 389 | `"            )"` | — |
| [SRC-EEF2E6447C-L000390](../../api/omarai.py#L390) | 390 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000391](../../api/omarai.py#L391) | 391 | `"            return self.respond(200, operation())"` | — |
| [SRC-EEF2E6447C-L000392](../../api/omarai.py#L392) | 392 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000393](../../api/omarai.py#L393) | 393 | `"            cls._agent_semaphore.release()"` | — |
| [SRC-EEF2E6447C-L000394](../../api/omarai.py#L394) | 394 | `""` | — |
| [SRC-EEF2E6447C-L000395](../../api/omarai.py#L395) | 395 | `"    def _session_cookie_name(self):"` | — |
| [SRC-EEF2E6447C-L000396](../../api/omarai.py#L396) | 396 | `"        \"\"\"Use the __Host- prefix on HTTPS public deployments.\"\"\""` | — |
| [SRC-EEF2E6447C-L000397](../../api/omarai.py#L397) | 397 | `"        if os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() == \"1\":"` | — |
| [SRC-EEF2E6447C-L000398](../../api/omarai.py#L398) | 398 | `"            return \"__Host-omarai_session\""` | — |
| [SRC-EEF2E6447C-L000399](../../api/omarai.py#L399) | 399 | `"        return \"omarai_session\""` | — |
| [SRC-EEF2E6447C-L000400](../../api/omarai.py#L400) | 400 | `""` | — |
| [SRC-EEF2E6447C-L000401](../../api/omarai.py#L401) | 401 | `"    def _session_cookie_header(self, token: str) -> str:"` | — |
| [SRC-EEF2E6447C-L000402](../../api/omarai.py#L402) | 402 | `"        if not BROWSER_SESSION_ID_RE.fullmatch(token):"` | — |
| [SRC-EEF2E6447C-L000403](../../api/omarai.py#L403) | 403 | `"            raise ValueError(\"browser access token has an unsupported format\")"` | — |
| [SRC-EEF2E6447C-L000404](../../api/omarai.py#L404) | 404 | `"        parts = ["` | — |
| [SRC-EEF2E6447C-L000405](../../api/omarai.py#L405) | 405 | `"            f\"{self._session_cookie_name()}={token}\","` | — |
| [SRC-EEF2E6447C-L000406](../../api/omarai.py#L406) | 406 | `"            \"Path=/\","` | — |
| [SRC-EEF2E6447C-L000407](../../api/omarai.py#L407) | 407 | `"            \"HttpOnly\","` | — |
| [SRC-EEF2E6447C-L000408](../../api/omarai.py#L408) | 408 | `"            \"SameSite=Strict\","` | — |
| [SRC-EEF2E6447C-L000409](../../api/omarai.py#L409) | 409 | `"            f\"Max-Age={BROWSER_SESSION_COOKIE_MAX_AGE}\","` | — |
| [SRC-EEF2E6447C-L000410](../../api/omarai.py#L410) | 410 | `"        ]"` | — |
| [SRC-EEF2E6447C-L000411](../../api/omarai.py#L411) | 411 | `"        if os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() == \"1\":"` | — |
| [SRC-EEF2E6447C-L000412](../../api/omarai.py#L412) | 412 | `"            parts.insert(2, \"Secure\")"` | — |
| [SRC-EEF2E6447C-L000413](../../api/omarai.py#L413) | 413 | `"        return \"; \".join(parts)"` | — |
| [SRC-EEF2E6447C-L000414](../../api/omarai.py#L414) | 414 | `""` | — |
| [SRC-EEF2E6447C-L000415](../../api/omarai.py#L415) | 415 | `"    def _clear_session_cookie_header(self) -> str:"` | — |
| [SRC-EEF2E6447C-L000416](../../api/omarai.py#L416) | 416 | `"        parts = ["` | — |
| [SRC-EEF2E6447C-L000417](../../api/omarai.py#L417) | 417 | `"            f\"{self._session_cookie_name()}=\","` | — |
| [SRC-EEF2E6447C-L000418](../../api/omarai.py#L418) | 418 | `"            \"Path=/\","` | — |
| [SRC-EEF2E6447C-L000419](../../api/omarai.py#L419) | 419 | `"            \"HttpOnly\","` | — |
| [SRC-EEF2E6447C-L000420](../../api/omarai.py#L420) | 420 | `"            \"SameSite=Strict\","` | — |
| [SRC-EEF2E6447C-L000421](../../api/omarai.py#L421) | 421 | `"            \"Max-Age=0\","` | — |
| [SRC-EEF2E6447C-L000422](../../api/omarai.py#L422) | 422 | `"        ]"` | — |
| [SRC-EEF2E6447C-L000423](../../api/omarai.py#L423) | 423 | `"        if os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() == \"1\":"` | — |
| [SRC-EEF2E6447C-L000424](../../api/omarai.py#L424) | 424 | `"            parts.insert(2, \"Secure\")"` | — |
| [SRC-EEF2E6447C-L000425](../../api/omarai.py#L425) | 425 | `"        return \"; \".join(parts)"` | — |
| [SRC-EEF2E6447C-L000426](../../api/omarai.py#L426) | 426 | `""` | — |
| [SRC-EEF2E6447C-L000427](../../api/omarai.py#L427) | 427 | `"    def _principal_for_access_token(self, token: str):"` | — |
| [SRC-EEF2E6447C-L000428](../../api/omarai.py#L428) | 428 | `"        expected = os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000429](../../api/omarai.py#L429) | 429 | `"        if expected and hmac.compare_digest(token, expected):"` | — |
| [SRC-EEF2E6447C-L000430](../../api/omarai.py#L430) | 430 | `"            return self.store.default_principal()"` | — |
| [SRC-EEF2E6447C-L000431](../../api/omarai.py#L431) | 431 | `"        return self.store.resolve_api_token(token)"` | — |
| [SRC-EEF2E6447C-L000432](../../api/omarai.py#L432) | 432 | `""` | — |
| [SRC-EEF2E6447C-L000433](../../api/omarai.py#L433) | 433 | `"    _FORWARDING_HEADERS = ("` | — |
| [SRC-EEF2E6447C-L000434](../../api/omarai.py#L434) | 434 | `"        \"X-Forwarded-For\", \"X-Forwarded-Host\", \"X-Forwarded-Proto\","` | — |
| [SRC-EEF2E6447C-L000435](../../api/omarai.py#L435) | 435 | `"        \"X-Real-IP\", \"Forwarded\", \"CF-Connecting-IP\", \"True-Client-IP\","` | — |
| [SRC-EEF2E6447C-L000436](../../api/omarai.py#L436) | 436 | `"    )"` | — |
| [SRC-EEF2E6447C-L000437](../../api/omarai.py#L437) | 437 | `""` | — |
| [SRC-EEF2E6447C-L000438](../../api/omarai.py#L438) | 438 | `"    def _has_forwarding_headers(self) -> bool:"` | — |
| [SRC-EEF2E6447C-L000439](../../api/omarai.py#L439) | 439 | `"        return any(self.headers.get(name) for name in self._FORWARDING_HEADERS)"` | — |
| [SRC-EEF2E6447C-L000440](../../api/omarai.py#L440) | 440 | `""` | — |
| [SRC-EEF2E6447C-L000441](../../api/omarai.py#L441) | 441 | `"    def _authorized(self):"` | — |
| [SRC-EEF2E6447C-L000442](../../api/omarai.py#L442) | 442 | `"        \"\"\"Resolve a verified bearer token or HttpOnly browser cookie."` | — |
| [SRC-EEF2E6447C-L000443](../../api/omarai.py#L443) | 443 | `""` | — |
| [SRC-EEF2E6447C-L000444](../../api/omarai.py#L444) | 444 | `"        Browser cookies are accepted only with same-origin POST requests. Request-body"` | — |
| [SRC-EEF2E6447C-L000445](../../api/omarai.py#L445) | 445 | `"        tenant IDs are never used to establish tenant context."` | — |
| [SRC-EEF2E6447C-L000446](../../api/omarai.py#L446) | 446 | `"        \"\"\""` | — |
| [SRC-EEF2E6447C-L000447](../../api/omarai.py#L447) | 447 | `"        self._authenticated_principal = None"` | — |
| [SRC-EEF2E6447C-L000448](../../api/omarai.py#L448) | 448 | `"        self._cookie_authenticated = False"` | — |
| [SRC-EEF2E6447C-L000449](../../api/omarai.py#L449) | 449 | `"        self._browser_session_id = \"\""` | — |
| [SRC-EEF2E6447C-L000450](../../api/omarai.py#L450) | 450 | `"        supplied = self.headers.get(\"Authorization\", \"\")"` | — |
| [SRC-EEF2E6447C-L000451](../../api/omarai.py#L451) | 451 | `"        if supplied.startswith(\"Bearer \"):"` | — |
| [SRC-EEF2E6447C-L000452](../../api/omarai.py#L452) | 452 | `"            token = supplied[7:].strip()"` | — |
| [SRC-EEF2E6447C-L000453](../../api/omarai.py#L453) | 453 | `"            self._authenticated_principal = self._principal_for_access_token(token)"` | — |
| [SRC-EEF2E6447C-L000454](../../api/omarai.py#L454) | 454 | `"            return bool(self._authenticated_principal)"` | — |
| [SRC-EEF2E6447C-L000455](../../api/omarai.py#L455) | 455 | `""` | — |
| [SRC-EEF2E6447C-L000456](../../api/omarai.py#L456) | 456 | `"        cookie = SimpleCookie()"` | — |
| [SRC-EEF2E6447C-L000457](../../api/omarai.py#L457) | 457 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000458](../../api/omarai.py#L458) | 458 | `"            cookie.load(self.headers.get(\"Cookie\", \"\"))"` | — |
| [SRC-EEF2E6447C-L000459](../../api/omarai.py#L459) | 459 | `"        except Exception:"` | — |
| [SRC-EEF2E6447C-L000460](../../api/omarai.py#L460) | 460 | `"            cookie = SimpleCookie()"` | — |
| [SRC-EEF2E6447C-L000461](../../api/omarai.py#L461) | 461 | `"        morsel = cookie.get(self._session_cookie_name())"` | — |
| [SRC-EEF2E6447C-L000462](../../api/omarai.py#L462) | 462 | `"        if morsel is not None:"` | — |
| [SRC-EEF2E6447C-L000463](../../api/omarai.py#L463) | 463 | `"            token = morsel.value"` | — |
| [SRC-EEF2E6447C-L000464](../../api/omarai.py#L464) | 464 | `"            if BROWSER_SESSION_ID_RE.fullmatch(token):"` | — |
| [SRC-EEF2E6447C-L000465](../../api/omarai.py#L465) | 465 | `"                self._authenticated_principal = self.store.resolve_web_session("` | — |
| [SRC-EEF2E6447C-L000466](../../api/omarai.py#L466) | 466 | `"                    token,"` | — |
| [SRC-EEF2E6447C-L000467](../../api/omarai.py#L467) | 467 | `"                    shared_token=os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip(),"` | — |
| [SRC-EEF2E6447C-L000468](../../api/omarai.py#L468) | 468 | `"                )"` | — |
| [SRC-EEF2E6447C-L000469](../../api/omarai.py#L469) | 469 | `"                self._cookie_authenticated = bool(self._authenticated_principal)"` | — |
| [SRC-EEF2E6447C-L000470](../../api/omarai.py#L470) | 470 | `"                if self._cookie_authenticated:"` | — |
| [SRC-EEF2E6447C-L000471](../../api/omarai.py#L471) | 471 | `"                    self._browser_session_id = token"` | — |
| [SRC-EEF2E6447C-L000472](../../api/omarai.py#L472) | 472 | `"                return self._cookie_authenticated"` | — |
| [SRC-EEF2E6447C-L000473](../../api/omarai.py#L473) | 473 | `""` | — |
| [SRC-EEF2E6447C-L000474](../../api/omarai.py#L474) | 474 | `"        # Loopback is not proof of a human identity: reverse proxies and tunnels"` | — |
| [SRC-EEF2E6447C-L000475](../../api/omarai.py#L475) | 475 | `"        # may connect from 127.0.0.1 while forwarding untrusted remote requests."` | — |
| [SRC-EEF2E6447C-L000476](../../api/omarai.py#L476) | 476 | `"        # Local development must opt in explicitly; public deployments never do."` | — |
| [SRC-EEF2E6447C-L000477](../../api/omarai.py#L477) | 477 | `"        if ("` | — |
| [SRC-EEF2E6447C-L000478](../../api/omarai.py#L478) | 478 | `"            os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() != \"1\""` | — |
| [SRC-EEF2E6447C-L000479](../../api/omarai.py#L479) | 479 | `"            and os.getenv(\"OMARAI_ALLOW_LOOPBACK_AUTH\", \"\").strip() == \"1\""` | — |
| [SRC-EEF2E6447C-L000480](../../api/omarai.py#L480) | 480 | `"            and not self._has_forwarding_headers()"` | — |
| [SRC-EEF2E6447C-L000481](../../api/omarai.py#L481) | 481 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000482](../../api/omarai.py#L482) | 482 | `"            try:"` | — |
| [SRC-EEF2E6447C-L000483](../../api/omarai.py#L483) | 483 | `"                if ipaddress.ip_address(self.client_address[0]).is_loopback:"` | — |
| [SRC-EEF2E6447C-L000484](../../api/omarai.py#L484) | 484 | `"                    self._authenticated_principal = self.store.default_principal()"` | — |
| [SRC-EEF2E6447C-L000485](../../api/omarai.py#L485) | 485 | `"                    return bool(self._authenticated_principal)"` | — |
| [SRC-EEF2E6447C-L000486](../../api/omarai.py#L486) | 486 | `"            except ValueError:"` | — |
| [SRC-EEF2E6447C-L000487](../../api/omarai.py#L487) | 487 | `"                pass"` | — |
| [SRC-EEF2E6447C-L000488](../../api/omarai.py#L488) | 488 | `"        return False"` | — |
| [SRC-EEF2E6447C-L000489](../../api/omarai.py#L489) | 489 | `""` | — |
| [SRC-EEF2E6447C-L000490](../../api/omarai.py#L490) | 490 | `"    def _allowed_origins(self):"` | — |
| [SRC-EEF2E6447C-L000491](../../api/omarai.py#L491) | 491 | `"        \"\"\"Return configured browser origins plus this service’s own origin."` | — |
| [SRC-EEF2E6447C-L000492](../../api/omarai.py#L492) | 492 | `""` | — |
| [SRC-EEF2E6447C-L000493](../../api/omarai.py#L493) | 493 | `"        OMARAI_ALLOWED_ORIGINS is a comma-separated list of trusted origins"` | — |
| [SRC-EEF2E6447C-L000494](../../api/omarai.py#L494) | 494 | `"        (scheme + host + optional port; no path and no wildcard)."` | — |
| [SRC-EEF2E6447C-L000495](../../api/omarai.py#L495) | 495 | `"        \"\"\""` | — |
| [SRC-EEF2E6447C-L000496](../../api/omarai.py#L496) | 496 | `"        configured = os.getenv(\"OMARAI_ALLOWED_ORIGINS\", \"\")"` | — |
| [SRC-EEF2E6447C-L000497](../../api/omarai.py#L497) | 497 | `"        origins = {"` | — |
| [SRC-EEF2E6447C-L000498](../../api/omarai.py#L498) | 498 | `"            item.strip().rstrip(\"/\")"` | — |
| [SRC-EEF2E6447C-L000499](../../api/omarai.py#L499) | 499 | `"            for item in configured.split(\",\")"` | — |
| [SRC-EEF2E6447C-L000500](../../api/omarai.py#L500) | 500 | `"            if item.strip()"` | — |
| [SRC-EEF2E6447C-L000501](../../api/omarai.py#L501) | 501 | `"        }"` | — |
| [SRC-EEF2E6447C-L000502](../../api/omarai.py#L502) | 502 | `"        if os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() == \"1\":"` | — |
| [SRC-EEF2E6447C-L000503](../../api/omarai.py#L503) | 503 | `"            # Host identifies the requested service origin. Do not derive allowed"` | — |
| [SRC-EEF2E6447C-L000504](../../api/omarai.py#L504) | 504 | `"            # origins from X-Forwarded-Host: direct clients can spoof that header"` | — |
| [SRC-EEF2E6447C-L000505](../../api/omarai.py#L505) | 505 | `"            # unless the reverse proxy is separately configured to overwrite it."` | — |
| [SRC-EEF2E6447C-L000506](../../api/omarai.py#L506) | 506 | `"            scheme = self.headers.get(\"X-Forwarded-Proto\", \"https\").split(\",\", 1)[0].strip().lower()"` | — |
| [SRC-EEF2E6447C-L000507](../../api/omarai.py#L507) | 507 | `"            host = self.headers.get(\"Host\", \"\").split(\",\", 1)[0].strip()"` | — |
| [SRC-EEF2E6447C-L000508](../../api/omarai.py#L508) | 508 | `"            if host:"` | — |
| [SRC-EEF2E6447C-L000509](../../api/omarai.py#L509) | 509 | `"                origins.add(f\"https://{host}\".rstrip(\"/\"))"` | — |
| [SRC-EEF2E6447C-L000510](../../api/omarai.py#L510) | 510 | `"                origins.add(f\"{scheme}://{host}\".rstrip(\"/\"))"` | — |
| [SRC-EEF2E6447C-L000511](../../api/omarai.py#L511) | 511 | `"        else:"` | — |
| [SRC-EEF2E6447C-L000512](../../api/omarai.py#L512) | 512 | `"            port = self.server.server_port"` | — |
| [SRC-EEF2E6447C-L000513](../../api/omarai.py#L513) | 513 | `"            origins.update("` | — |
| [SRC-EEF2E6447C-L000514](../../api/omarai.py#L514) | 514 | `"                {"` | — |
| [SRC-EEF2E6447C-L000515](../../api/omarai.py#L515) | 515 | `"                    f\"http://127.0.0.1:{port}\","` | — |
| [SRC-EEF2E6447C-L000516](../../api/omarai.py#L516) | 516 | `"                    f\"http://localhost:{port}\","` | — |
| [SRC-EEF2E6447C-L000517](../../api/omarai.py#L517) | 517 | `"                    f\"http://[::1]:{port}\","` | — |
| [SRC-EEF2E6447C-L000518](../../api/omarai.py#L518) | 518 | `"                }"` | — |
| [SRC-EEF2E6447C-L000519](../../api/omarai.py#L519) | 519 | `"            )"` | — |
| [SRC-EEF2E6447C-L000520](../../api/omarai.py#L520) | 520 | `"        return origins"` | — |
| [SRC-EEF2E6447C-L000521](../../api/omarai.py#L521) | 521 | `""` | — |
| [SRC-EEF2E6447C-L000522](../../api/omarai.py#L522) | 522 | `"    def _origin_allowed(self, origin):"` | — |
| [SRC-EEF2E6447C-L000523](../../api/omarai.py#L523) | 523 | `"        return bool(origin) and origin.rstrip(\"/\") in self._allowed_origins()"` | — |
| [SRC-EEF2E6447C-L000524](../../api/omarai.py#L524) | 524 | `""` | — |
| [SRC-EEF2E6447C-L000525](../../api/omarai.py#L525) | 525 | `"    def _rate_limit_client_key(self):"` | — |
| [SRC-EEF2E6447C-L000526](../../api/omarai.py#L526) | 526 | `"        \"\"\"Choose a rate-limit identity without trusting spoofable proxy headers by default."` | — |
| [SRC-EEF2E6447C-L000527](../../api/omarai.py#L527) | 527 | `""` | — |
| [SRC-EEF2E6447C-L000528](../../api/omarai.py#L528) | 528 | `"        Set OMARAI_TRUST_PROXY_HEADERS=1 only when the deployment's trusted reverse"` | — |
| [SRC-EEF2E6447C-L000529](../../api/omarai.py#L529) | 529 | `"        proxy appends the actual client IP as the rightmost X-Forwarded-For value."` | — |
| [SRC-EEF2E6447C-L000530](../../api/omarai.py#L530) | 530 | `"        \"\"\""` | — |
| [SRC-EEF2E6447C-L000531](../../api/omarai.py#L531) | 531 | `"        direct_ip = self.client_address[0]"` | — |
| [SRC-EEF2E6447C-L000532](../../api/omarai.py#L532) | 532 | `"        if os.getenv(\"OMARAI_TRUST_PROXY_HEADERS\", \"\").strip() != \"1\":"` | — |
| [SRC-EEF2E6447C-L000533](../../api/omarai.py#L533) | 533 | `"            return direct_ip"` | — |
| [SRC-EEF2E6447C-L000534](../../api/omarai.py#L534) | 534 | `"        forwarded = self.headers.get(\"X-Forwarded-For\", \"\")"` | — |
| [SRC-EEF2E6447C-L000535](../../api/omarai.py#L535) | 535 | `"        candidate = forwarded.rsplit(\",\", 1)[-1].strip() if forwarded else \"\""` | — |
| [SRC-EEF2E6447C-L000536](../../api/omarai.py#L536) | 536 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000537](../../api/omarai.py#L537) | 537 | `"            return str(ipaddress.ip_address(candidate))"` | — |
| [SRC-EEF2E6447C-L000538](../../api/omarai.py#L538) | 538 | `"        except ValueError:"` | — |
| [SRC-EEF2E6447C-L000539](../../api/omarai.py#L539) | 539 | `"            return direct_ip"` | — |
| [SRC-EEF2E6447C-L000540](../../api/omarai.py#L540) | 540 | `""` | — |
| [SRC-EEF2E6447C-L000541](../../api/omarai.py#L541) | 541 | `"    def _rate_limit_ok(self):"` | — |
| [SRC-EEF2E6447C-L000542](../../api/omarai.py#L542) | 542 | `"        client_ip = self._rate_limit_client_key()"` | — |
| [SRC-EEF2E6447C-L000543](../../api/omarai.py#L543) | 543 | `"        now = time.monotonic()"` | — |
| [SRC-EEF2E6447C-L000544](../../api/omarai.py#L544) | 544 | `"        cls = type(self)"` | — |
| [SRC-EEF2E6447C-L000545](../../api/omarai.py#L545) | 545 | `"        with self._rate_lock:"` | — |
| [SRC-EEF2E6447C-L000546](../../api/omarai.py#L546) | 546 | `"            # Periodically remove IP buckets whose entire sliding window has expired."` | — |
| [SRC-EEF2E6447C-L000547](../../api/omarai.py#L547) | 547 | `"            # Without this sweep, a public endpoint could retain one empty deque per"` | — |
| [SRC-EEF2E6447C-L000548](../../api/omarai.py#L548) | 548 | `"            # distinct client IP forever, even though the rate-limit window is 60 sec."` | — |
| [SRC-EEF2E6447C-L000549](../../api/omarai.py#L549) | 549 | `"            if now - cls._rate_last_cleanup >= cls.RATE_LIMIT_CLEANUP_INTERVAL_SECONDS:"` | — |
| [SRC-EEF2E6447C-L000550](../../api/omarai.py#L550) | 550 | `"                cutoff = now - cls.RATE_LIMIT_WINDOW_SECONDS"` | — |
| [SRC-EEF2E6447C-L000551](../../api/omarai.py#L551) | 551 | `"                for key, timestamps in list(cls._request_times.items()):"` | — |
| [SRC-EEF2E6447C-L000552](../../api/omarai.py#L552) | 552 | `"                    while timestamps and timestamps[0] <= cutoff:"` | — |
| [SRC-EEF2E6447C-L000553](../../api/omarai.py#L553) | 553 | `"                        timestamps.popleft()"` | — |
| [SRC-EEF2E6447C-L000554](../../api/omarai.py#L554) | 554 | `"                    if not timestamps:"` | — |
| [SRC-EEF2E6447C-L000555](../../api/omarai.py#L555) | 555 | `"                        cls._request_times.pop(key, None)"` | — |
| [SRC-EEF2E6447C-L000556](../../api/omarai.py#L556) | 556 | `"                cls._rate_last_cleanup = now"` | — |
| [SRC-EEF2E6447C-L000557](../../api/omarai.py#L557) | 557 | `""` | — |
| [SRC-EEF2E6447C-L000558](../../api/omarai.py#L558) | 558 | `"            if ("` | — |
| [SRC-EEF2E6447C-L000559](../../api/omarai.py#L559) | 559 | `"                client_ip not in cls._request_times"` | — |
| [SRC-EEF2E6447C-L000560](../../api/omarai.py#L560) | 560 | `"                and len(cls._request_times) >= max(1, cls.MAX_RATE_LIMIT_CLIENT_BUCKETS) - 1"` | — |
| [SRC-EEF2E6447C-L000561](../../api/omarai.py#L561) | 561 | `"            ):"` | — |
| [SRC-EEF2E6447C-L000562](../../api/omarai.py#L562) | 562 | `"                # Bound attacker-controlled cardinality. Excess identities share a"` | — |
| [SRC-EEF2E6447C-L000563](../../api/omarai.py#L563) | 563 | `"                # conservative overflow bucket instead of allocating one deque per IP."` | — |
| [SRC-EEF2E6447C-L000564](../../api/omarai.py#L564) | 564 | `"                client_ip = cls.RATE_LIMIT_OVERFLOW_KEY"` | — |
| [SRC-EEF2E6447C-L000565](../../api/omarai.py#L565) | 565 | `"            events = cls._request_times[client_ip]"` | — |
| [SRC-EEF2E6447C-L000566](../../api/omarai.py#L566) | 566 | `"            while events and now - events[0] >= cls.RATE_LIMIT_WINDOW_SECONDS:"` | — |
| [SRC-EEF2E6447C-L000567](../../api/omarai.py#L567) | 567 | `"                events.popleft()"` | — |
| [SRC-EEF2E6447C-L000568](../../api/omarai.py#L568) | 568 | `"            if len(events) >= cls.RATE_LIMIT_REQUESTS:"` | — |
| [SRC-EEF2E6447C-L000569](../../api/omarai.py#L569) | 569 | `"                return False"` | — |
| [SRC-EEF2E6447C-L000570](../../api/omarai.py#L570) | 570 | `"            events.append(now)"` | — |
| [SRC-EEF2E6447C-L000571](../../api/omarai.py#L571) | 571 | `"            return True"` | — |
| [SRC-EEF2E6447C-L000572](../../api/omarai.py#L572) | 572 | `""` | — |
| [SRC-EEF2E6447C-L000573](../../api/omarai.py#L573) | 573 | `"    def _read_request_body(self) -> bytes \| None:"` | — |
| [SRC-EEF2E6447C-L000574](../../api/omarai.py#L574) | 574 | `"        \"\"\"Read a bounded body with both idle and absolute wall-clock deadlines.\"\"\""` | — |
| [SRC-EEF2E6447C-L000575](../../api/omarai.py#L575) | 575 | `"        raw_size = self.headers.get(\"Content-Length\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000576](../../api/omarai.py#L576) | 576 | `"        if not raw_size or not raw_size.isascii() or not raw_size.isdecimal():"` | — |
| [SRC-EEF2E6447C-L000577](../../api/omarai.py#L577) | 577 | `"            self.respond(400, {\"error\": \"valid Content-Length is required\"})"` | — |
| [SRC-EEF2E6447C-L000578](../../api/omarai.py#L578) | 578 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000579](../../api/omarai.py#L579) | 579 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000580](../../api/omarai.py#L580) | 580 | `"            size = int(raw_size)"` | — |
| [SRC-EEF2E6447C-L000581](../../api/omarai.py#L581) | 581 | `"        except ValueError:"` | — |
| [SRC-EEF2E6447C-L000582](../../api/omarai.py#L582) | 582 | `"            self.respond(400, {\"error\": \"valid Content-Length is required\"})"` | — |
| [SRC-EEF2E6447C-L000583](../../api/omarai.py#L583) | 583 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000584](../../api/omarai.py#L584) | 584 | `"        if size <= 0:"` | — |
| [SRC-EEF2E6447C-L000585](../../api/omarai.py#L585) | 585 | `"            self.respond(400, {\"error\": \"request body is required\"})"` | — |
| [SRC-EEF2E6447C-L000586](../../api/omarai.py#L586) | 586 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000587](../../api/omarai.py#L587) | 587 | `"        if size > MAX_REQUEST_BODY_BYTES:"` | — |
| [SRC-EEF2E6447C-L000588](../../api/omarai.py#L588) | 588 | `"            # The declared body remains unread; do not reuse this connection."` | — |
| [SRC-EEF2E6447C-L000589](../../api/omarai.py#L589) | 589 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000590](../../api/omarai.py#L590) | 590 | `"            self.respond(413, {\"error\": \"request too large\"})"` | — |
| [SRC-EEF2E6447C-L000591](../../api/omarai.py#L591) | 591 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000592](../../api/omarai.py#L592) | 592 | `""` | — |
| [SRC-EEF2E6447C-L000593](../../api/omarai.py#L593) | 593 | `"        total_timeout = max("` | — |
| [SRC-EEF2E6447C-L000594](../../api/omarai.py#L594) | 594 | `"            0.1,"` | — |
| [SRC-EEF2E6447C-L000595](../../api/omarai.py#L595) | 595 | `"            min("` | — |
| [SRC-EEF2E6447C-L000596](../../api/omarai.py#L596) | 596 | `"                float(REQUEST_BODY_READ_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000597](../../api/omarai.py#L597) | 597 | `"                MAX_REQUEST_BODY_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000598](../../api/omarai.py#L598) | 598 | `"            ),"` | — |
| [SRC-EEF2E6447C-L000599](../../api/omarai.py#L599) | 599 | `"        )"` | — |
| [SRC-EEF2E6447C-L000600](../../api/omarai.py#L600) | 600 | `"        idle_timeout = max("` | — |
| [SRC-EEF2E6447C-L000601](../../api/omarai.py#L601) | 601 | `"            0.1,"` | — |
| [SRC-EEF2E6447C-L000602](../../api/omarai.py#L602) | 602 | `"            min("` | — |
| [SRC-EEF2E6447C-L000603](../../api/omarai.py#L603) | 603 | `"                float(REQUEST_BODY_IDLE_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000604](../../api/omarai.py#L604) | 604 | `"                MAX_REQUEST_BODY_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000605](../../api/omarai.py#L605) | 605 | `"            ),"` | — |
| [SRC-EEF2E6447C-L000606](../../api/omarai.py#L606) | 606 | `"        )"` | — |
| [SRC-EEF2E6447C-L000607](../../api/omarai.py#L607) | 607 | `"        deadline = time.monotonic() + total_timeout"` | — |
| [SRC-EEF2E6447C-L000608](../../api/omarai.py#L608) | 608 | `"        previous_timeout = self.connection.gettimeout()"` | — |
| [SRC-EEF2E6447C-L000609](../../api/omarai.py#L609) | 609 | `"        body = bytearray()"` | — |
| [SRC-EEF2E6447C-L000610](../../api/omarai.py#L610) | 610 | `"        timed_out = False"` | — |
| [SRC-EEF2E6447C-L000611](../../api/omarai.py#L611) | 611 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000612](../../api/omarai.py#L612) | 612 | `"            while len(body) < size:"` | — |
| [SRC-EEF2E6447C-L000613](../../api/omarai.py#L613) | 613 | `"                remaining = deadline - time.monotonic()"` | — |
| [SRC-EEF2E6447C-L000614](../../api/omarai.py#L614) | 614 | `"                if remaining <= 0:"` | — |
| [SRC-EEF2E6447C-L000615](../../api/omarai.py#L615) | 615 | `"                    timed_out = True"` | — |
| [SRC-EEF2E6447C-L000616](../../api/omarai.py#L616) | 616 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000617](../../api/omarai.py#L617) | 617 | `"                self.connection.settimeout(min(idle_timeout, remaining))"` | — |
| [SRC-EEF2E6447C-L000618](../../api/omarai.py#L618) | 618 | `"                try:"` | — |
| [SRC-EEF2E6447C-L000619](../../api/omarai.py#L619) | 619 | `"                    # read1 performs at most one underlying read, letting us re-check"` | — |
| [SRC-EEF2E6447C-L000620](../../api/omarai.py#L620) | 620 | `"                    # the absolute deadline between body fragments."` | — |
| [SRC-EEF2E6447C-L000621](../../api/omarai.py#L621) | 621 | `"                    chunk = self.rfile.read1("` | — |
| [SRC-EEF2E6447C-L000622](../../api/omarai.py#L622) | 622 | `"                        min(size - len(body), REQUEST_BODY_READ_CHUNK_BYTES)"` | — |
| [SRC-EEF2E6447C-L000623](../../api/omarai.py#L623) | 623 | `"                    )"` | — |
| [SRC-EEF2E6447C-L000624](../../api/omarai.py#L624) | 624 | `"                except TimeoutError:"` | — |
| [SRC-EEF2E6447C-L000625](../../api/omarai.py#L625) | 625 | `"                    timed_out = True"` | — |
| [SRC-EEF2E6447C-L000626](../../api/omarai.py#L626) | 626 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000627](../../api/omarai.py#L627) | 627 | `"                if not chunk:"` | — |
| [SRC-EEF2E6447C-L000628](../../api/omarai.py#L628) | 628 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000629](../../api/omarai.py#L629) | 629 | `"                body.extend(chunk)"` | — |
| [SRC-EEF2E6447C-L000630](../../api/omarai.py#L630) | 630 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000631](../../api/omarai.py#L631) | 631 | `"            try:"` | — |
| [SRC-EEF2E6447C-L000632](../../api/omarai.py#L632) | 632 | `"                self.connection.settimeout(previous_timeout)"` | — |
| [SRC-EEF2E6447C-L000633](../../api/omarai.py#L633) | 633 | `"            except OSError:"` | — |
| [SRC-EEF2E6447C-L000634](../../api/omarai.py#L634) | 634 | `"                pass"` | — |
| [SRC-EEF2E6447C-L000635](../../api/omarai.py#L635) | 635 | `""` | — |
| [SRC-EEF2E6447C-L000636](../../api/omarai.py#L636) | 636 | `"        if timed_out:"` | — |
| [SRC-EEF2E6447C-L000637](../../api/omarai.py#L637) | 637 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000638](../../api/omarai.py#L638) | 638 | `"            self.respond(408, {\"error\": \"request body read timed out\"})"` | — |
| [SRC-EEF2E6447C-L000639](../../api/omarai.py#L639) | 639 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000640](../../api/omarai.py#L640) | 640 | `"        if len(body) != size:"` | — |
| [SRC-EEF2E6447C-L000641](../../api/omarai.py#L641) | 641 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000642](../../api/omarai.py#L642) | 642 | `"            self.respond(400, {\"error\": \"incomplete request body\"})"` | — |
| [SRC-EEF2E6447C-L000643](../../api/omarai.py#L643) | 643 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000644](../../api/omarai.py#L644) | 644 | `"        return bytes(body)"` | — |
| [SRC-EEF2E6447C-L000645](../../api/omarai.py#L645) | 645 | `""` | — |
| [SRC-EEF2E6447C-L000646](../../api/omarai.py#L646) | 646 | `"    def end_headers(self):"` | — |
| [SRC-EEF2E6447C-L000647](../../api/omarai.py#L647) | 647 | `"        \"\"\"Apply defensive browser headers to successful and error responses alike.\"\"\""` | — |
| [SRC-EEF2E6447C-L000648](../../api/omarai.py#L648) | 648 | `"        self.send_header(\"X-Content-Type-Options\", \"nosniff\")"` | — |
| [SRC-EEF2E6447C-L000649](../../api/omarai.py#L649) | 649 | `"        self.send_header(\"X-Frame-Options\", \"DENY\")"` | — |
| [SRC-EEF2E6447C-L000650](../../api/omarai.py#L650) | 650 | `"        self.send_header(\"Referrer-Policy\", \"strict-origin-when-cross-origin\")"` | — |
| [SRC-EEF2E6447C-L000651](../../api/omarai.py#L651) | 651 | `"        self.send_header(\"Permissions-Policy\", \"camera=(), microphone=(), geolocation=()\")"` | — |
| [SRC-EEF2E6447C-L000652](../../api/omarai.py#L652) | 652 | `"        self.send_header(\"Content-Security-Policy\", _content_security_policy())"` | — |
| [SRC-EEF2E6447C-L000653](../../api/omarai.py#L653) | 653 | `"        super().end_headers()"` | — |
| [SRC-EEF2E6447C-L000654](../../api/omarai.py#L654) | 654 | `""` | — |
| [SRC-EEF2E6447C-L000655](../../api/omarai.py#L655) | 655 | `"    def respond("` | — |
| [SRC-EEF2E6447C-L000656](../../api/omarai.py#L656) | 656 | `"        self,"` | — |
| [SRC-EEF2E6447C-L000657](../../api/omarai.py#L657) | 657 | `"        status,"` | — |
| [SRC-EEF2E6447C-L000658](../../api/omarai.py#L658) | 658 | `"        payload,"` | — |
| [SRC-EEF2E6447C-L000659](../../api/omarai.py#L659) | 659 | `"        content_type=\"application/json; charset=utf-8\","` | — |
| [SRC-EEF2E6447C-L000660](../../api/omarai.py#L660) | 660 | `"        extra_headers: list[tuple[str, str]] \| None = None,"` | — |
| [SRC-EEF2E6447C-L000661](../../api/omarai.py#L661) | 661 | `"    ):"` | — |
| [SRC-EEF2E6447C-L000662](../../api/omarai.py#L662) | 662 | `"        body = payload.encode() if isinstance(payload, str) else json.dumps(payload, ensure_ascii=False).encode()"` | — |
| [SRC-EEF2E6447C-L000663](../../api/omarai.py#L663) | 663 | `"        self.send_response(status)"` | — |
| [SRC-EEF2E6447C-L000664](../../api/omarai.py#L664) | 664 | `"        self.send_header(\"Content-Type\", content_type)"` | — |
| [SRC-EEF2E6447C-L000665](../../api/omarai.py#L665) | 665 | `"        self.send_header(\"Content-Length\", str(len(body)))"` | — |
| [SRC-EEF2E6447C-L000666](../../api/omarai.py#L666) | 666 | `"        self.send_header(\"Cache-Control\", \"no-store\")"` | — |
| [SRC-EEF2E6447C-L000667](../../api/omarai.py#L667) | 667 | `"        origin = self.headers.get(\"Origin\")"` | — |
| [SRC-EEF2E6447C-L000668](../../api/omarai.py#L668) | 668 | `"        if origin and self._origin_allowed(origin):"` | — |
| [SRC-EEF2E6447C-L000669](../../api/omarai.py#L669) | 669 | `"            self.send_header(\"Access-Control-Allow-Origin\", origin)"` | — |
| [SRC-EEF2E6447C-L000670](../../api/omarai.py#L670) | 670 | `"            self.send_header(\"Vary\", \"Origin\")"` | — |
| [SRC-EEF2E6447C-L000671](../../api/omarai.py#L671) | 671 | `"        for name, value in extra_headers or []:"` | — |
| [SRC-EEF2E6447C-L000672](../../api/omarai.py#L672) | 672 | `"            self.send_header(name, value)"` | — |
| [SRC-EEF2E6447C-L000673](../../api/omarai.py#L673) | 673 | `"        self.end_headers()"` | — |
| [SRC-EEF2E6447C-L000674](../../api/omarai.py#L674) | 674 | `"        self.wfile.write(body)"` | — |
| [SRC-EEF2E6447C-L000675](../../api/omarai.py#L675) | 675 | `""` | — |
| [SRC-EEF2E6447C-L000676](../../api/omarai.py#L676) | 676 | `"    def do_GET(self):"` | — |
| [SRC-EEF2E6447C-L000677](../../api/omarai.py#L677) | 677 | `"        parsed = urlparse(self.path)"` | — |
| [SRC-EEF2E6447C-L000678](../../api/omarai.py#L678) | 678 | `"        if parsed.path == \"/agent\":"` | — |
| [SRC-EEF2E6447C-L000679](../../api/omarai.py#L679) | 679 | `"            if not AGENT_DASHBOARD.exists():"` | — |
| [SRC-EEF2E6447C-L000680](../../api/omarai.py#L680) | 680 | `"                return self.respond(404, {\"error\": \"agent dashboard missing\"})"` | — |
| [SRC-EEF2E6447C-L000681](../../api/omarai.py#L681) | 681 | `"            return self.respond(200, AGENT_DASHBOARD.read_text(encoding=\"utf-8\"), \"text/html; charset=utf-8\")"` | — |
| [SRC-EEF2E6447C-L000682](../../api/omarai.py#L682) | 682 | `"        if parsed.path in {\"/\", \"/workspace\"}:"` | — |
| [SRC-EEF2E6447C-L000683](../../api/omarai.py#L683) | 683 | `"            if not WORKSPACE_DASHBOARD.exists():"` | — |
| [SRC-EEF2E6447C-L000684](../../api/omarai.py#L684) | 684 | `"                return self.respond(404, {\"error\": \"workspace dashboard missing\"})"` | — |
| [SRC-EEF2E6447C-L000685](../../api/omarai.py#L685) | 685 | `"            return self.respond(200, WORKSPACE_DASHBOARD.read_text(encoding=\"utf-8\"), \"text/html; charset=utf-8\")"` | — |
| [SRC-EEF2E6447C-L000686](../../api/omarai.py#L686) | 686 | `"        if parsed.path == \"/leads\":"` | — |
| [SRC-EEF2E6447C-L000687](../../api/omarai.py#L687) | 687 | `"            if not LEADS_DASHBOARD.exists():"` | — |
| [SRC-EEF2E6447C-L000688](../../api/omarai.py#L688) | 688 | `"                return self.respond(404, {\"error\": \"leads dashboard missing\"})"` | — |
| [SRC-EEF2E6447C-L000689](../../api/omarai.py#L689) | 689 | `"            return self.respond(200, LEADS_DASHBOARD.read_text(encoding=\"utf-8\"), \"text/html; charset=utf-8\")"` | — |
| [SRC-EEF2E6447C-L000690](../../api/omarai.py#L690) | 690 | `"        if parsed.path == \"/api/health\":"` | — |
| [SRC-EEF2E6447C-L000691](../../api/omarai.py#L691) | 691 | `"            return self.respond("` | — |
| [SRC-EEF2E6447C-L000692](../../api/omarai.py#L692) | 692 | `"                200,"` | — |
| [SRC-EEF2E6447C-L000693](../../api/omarai.py#L693) | 693 | `"                {"` | — |
| [SRC-EEF2E6447C-L000694](../../api/omarai.py#L694) | 694 | `"                    \"ok\": True,"` | — |
| [SRC-EEF2E6447C-L000695](../../api/omarai.py#L695) | 695 | `"                    \"app\": \"Omarai\","` | — |
| [SRC-EEF2E6447C-L000696](../../api/omarai.py#L696) | 696 | `"                    \"mode\": \"web-research\","` | — |
| [SRC-EEF2E6447C-L000697](../../api/omarai.py#L697) | 697 | `"                    \"agent\": WebAgent.status(),"` | — |
| [SRC-EEF2E6447C-L000698](../../api/omarai.py#L698) | 698 | `"                    \"storage\": {"` | — |
| [SRC-EEF2E6447C-L000699](../../api/omarai.py#L699) | 699 | `"                        \"backend\": getattr(self.store, \"backend\", \"unknown\"),"` | — |
| [SRC-EEF2E6447C-L000700](../../api/omarai.py#L700) | 700 | `"                        \"database_url_configured\": bool("` | — |
| [SRC-EEF2E6447C-L000701](../../api/omarai.py#L701) | 701 | `"                            os.getenv(\"OMARAI_DATABASE_URL\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000702](../../api/omarai.py#L702) | 702 | `"                            or os.getenv(\"DATABASE_URL\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000703](../../api/omarai.py#L703) | 703 | `"                        ),"` | — |
| [SRC-EEF2E6447C-L000704](../../api/omarai.py#L704) | 704 | `"                        \"database_path_override_configured\": bool("` | — |
| [SRC-EEF2E6447C-L000705](../../api/omarai.py#L705) | 705 | `"                            os.getenv(\"OMARAI_DB_PATH\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000706](../../api/omarai.py#L706) | 706 | `"                        ),"` | — |
| [SRC-EEF2E6447C-L000707](../../api/omarai.py#L707) | 707 | `"                        # This is an operator assertion, not automatic mount detection."` | — |
| [SRC-EEF2E6447C-L000708](../../api/omarai.py#L708) | 708 | `"                        \"persistent_volume_operator_asserted\": ("` | — |
| [SRC-EEF2E6447C-L000709](../../api/omarai.py#L709) | 709 | `"                            os.getenv(\"OMARAI_DB_PERSISTENT\", \"\").strip() == \"1\""` | — |
| [SRC-EEF2E6447C-L000710](../../api/omarai.py#L710) | 710 | `"                        ),"` | — |
| [SRC-EEF2E6447C-L000711](../../api/omarai.py#L711) | 711 | `"                        \"durability_status\": ("` | — |
| [SRC-EEF2E6447C-L000712](../../api/omarai.py#L712) | 712 | `"                            \"external_database_configured\""` | — |
| [SRC-EEF2E6447C-L000713](../../api/omarai.py#L713) | 713 | `"                            if getattr(self.store, \"backend\", \"unknown\") == \"postgresql\""` | — |
| [SRC-EEF2E6447C-L000714](../../api/omarai.py#L714) | 714 | `"                            else \"operator_asserted\""` | — |
| [SRC-EEF2E6447C-L000715](../../api/omarai.py#L715) | 715 | `"                            if os.getenv(\"OMARAI_DB_PERSISTENT\", \"\").strip() == \"1\""` | — |
| [SRC-EEF2E6447C-L000716](../../api/omarai.py#L716) | 716 | `"                            else \"not_guaranteed\""` | — |
| [SRC-EEF2E6447C-L000717](../../api/omarai.py#L717) | 717 | `"                        ),"` | — |
| [SRC-EEF2E6447C-L000718](../../api/omarai.py#L718) | 718 | `"                        \"warning\": ("` | — |
| [SRC-EEF2E6447C-L000719](../../api/omarai.py#L719) | 719 | `"                            \"PostgreSQL is selected; provider durability and backups are outside this health check.\""` | — |
| [SRC-EEF2E6447C-L000720](../../api/omarai.py#L720) | 720 | `"                            if getattr(self.store, \"backend\", \"unknown\") == \"postgresql\""` | — |
| [SRC-EEF2E6447C-L000721](../../api/omarai.py#L721) | 721 | `"                            else None"` | — |
| [SRC-EEF2E6447C-L000722](../../api/omarai.py#L722) | 722 | `"                            if os.getenv(\"OMARAI_DB_PERSISTENT\", \"\").strip() == \"1\""` | — |
| [SRC-EEF2E6447C-L000723](../../api/omarai.py#L723) | 723 | `"                            else \"SQLite records may be lost when the host replaces its ephemeral filesystem.\""` | — |
| [SRC-EEF2E6447C-L000724](../../api/omarai.py#L724) | 724 | `"                        ),"` | — |
| [SRC-EEF2E6447C-L000725](../../api/omarai.py#L725) | 725 | `"                    },"` | — |
| [SRC-EEF2E6447C-L000726](../../api/omarai.py#L726) | 726 | `"                    \"build\": {"` | — |
| [SRC-EEF2E6447C-L000727](../../api/omarai.py#L727) | 727 | `"                        \"sha\": _build_identity()[0],"` | — |
| [SRC-EEF2E6447C-L000728](../../api/omarai.py#L728) | 728 | `"                        \"sha_status\": ("` | — |
| [SRC-EEF2E6447C-L000729](../../api/omarai.py#L729) | 729 | `"                            \"available\" if _build_identity()[0] != \"unknown\" else \"unknown\""` | — |
| [SRC-EEF2E6447C-L000730](../../api/omarai.py#L730) | 730 | `"                        ),"` | — |
| [SRC-EEF2E6447C-L000731](../../api/omarai.py#L731) | 731 | `"                        \"sha_source\": _build_identity()[1],"` | — |
| [SRC-EEF2E6447C-L000732](../../api/omarai.py#L732) | 732 | `"                    },"` | — |
| [SRC-EEF2E6447C-L000733](../../api/omarai.py#L733) | 733 | `"                },"` | — |
| [SRC-EEF2E6447C-L000734](../../api/omarai.py#L734) | 734 | `"            )"` | — |
| [SRC-EEF2E6447C-L000735](../../api/omarai.py#L735) | 735 | `"        if parsed.path == \"/api/product-profiles\":"` | — |
| [SRC-EEF2E6447C-L000736](../../api/omarai.py#L736) | 736 | `"            if not self._rate_limit_ok():"` | — |
| [SRC-EEF2E6447C-L000737](../../api/omarai.py#L737) | 737 | `"                return self.respond(429, {\"error\": \"تجاوزت حد الطلبات المؤقت؛ حاول بعد دقيقة.\"})"` | — |
| [SRC-EEF2E6447C-L000738](../../api/omarai.py#L738) | 738 | `"            if not self._authorized():"` | — |
| [SRC-EEF2E6447C-L000739](../../api/omarai.py#L739) | 739 | `"                return self.respond(401, {\"error\": \"يلزم تسجيل الدخول لقراءة ملفات المنتجات.\"})"` | — |
| [SRC-EEF2E6447C-L000740](../../api/omarai.py#L740) | 740 | `"            profiles = self.store.list_product_profiles("` | — |
| [SRC-EEF2E6447C-L000741](../../api/omarai.py#L741) | 741 | `"                tenant_id=self._authenticated_principal[\"tenant_id\"]"` | — |
| [SRC-EEF2E6447C-L000742](../../api/omarai.py#L742) | 742 | `"            )"` | — |
| [SRC-EEF2E6447C-L000743](../../api/omarai.py#L743) | 743 | `"            return self.respond(200, {\"profiles\": profiles, \"count\": len(profiles)})"` | — |
| [SRC-EEF2E6447C-L000744](../../api/omarai.py#L744) | 744 | `"        if parsed.path == \"/api/discoveries\":"` | — |
| [SRC-EEF2E6447C-L000745](../../api/omarai.py#L745) | 745 | `"            if not self._rate_limit_ok():"` | — |
| [SRC-EEF2E6447C-L000746](../../api/omarai.py#L746) | 746 | `"                return self.respond(429, {\"error\": \"تجاوزت حد الطلبات المؤقت؛ حاول بعد دقيقة.\"})"` | — |
| [SRC-EEF2E6447C-L000747](../../api/omarai.py#L747) | 747 | `"            if not self._authorized():"` | — |
| [SRC-EEF2E6447C-L000748](../../api/omarai.py#L748) | 748 | `"                return self.respond(401, {\"error\": \"يلزم تسجيل الدخول لقراءة سجل الاكتشاف.\"})"` | — |
| [SRC-EEF2E6447C-L000749](../../api/omarai.py#L749) | 749 | `"            runs = self.store.list_discovery_runs("` | — |
| [SRC-EEF2E6447C-L000750](../../api/omarai.py#L750) | 750 | `"                tenant_id=self._authenticated_principal[\"tenant_id\"]"` | — |
| [SRC-EEF2E6447C-L000751](../../api/omarai.py#L751) | 751 | `"            )"` | — |
| [SRC-EEF2E6447C-L000752](../../api/omarai.py#L752) | 752 | `"            return self.respond(200, {\"runs\": runs, \"count\": len(runs)})"` | — |
| [SRC-EEF2E6447C-L000753](../../api/omarai.py#L753) | 753 | `"        discovery_route = parsed.path.split(\"/\")"` | — |
| [SRC-EEF2E6447C-L000754](../../api/omarai.py#L754) | 754 | `"        if ("` | — |
| [SRC-EEF2E6447C-L000755](../../api/omarai.py#L755) | 755 | `"            len(discovery_route) == 4"` | — |
| [SRC-EEF2E6447C-L000756](../../api/omarai.py#L756) | 756 | `"            and discovery_route[1:3] == [\"api\", \"discoveries\"]"` | — |
| [SRC-EEF2E6447C-L000757](../../api/omarai.py#L757) | 757 | `"            and discovery_route[3]"` | — |
| [SRC-EEF2E6447C-L000758](../../api/omarai.py#L758) | 758 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000759](../../api/omarai.py#L759) | 759 | `"            if not self._rate_limit_ok():"` | — |
| [SRC-EEF2E6447C-L000760](../../api/omarai.py#L760) | 760 | `"                return self.respond(429, {\"error\": \"تجاوزت حد الطلبات المؤقت؛ حاول بعد دقيقة.\"})"` | — |
| [SRC-EEF2E6447C-L000761](../../api/omarai.py#L761) | 761 | `"            if not self._authorized():"` | — |
| [SRC-EEF2E6447C-L000762](../../api/omarai.py#L762) | 762 | `"                return self.respond(401, {\"error\": \"يلزم تسجيل الدخول لقراءة عملية الاكتشاف.\"})"` | — |
| [SRC-EEF2E6447C-L000763](../../api/omarai.py#L763) | 763 | `"            run = self.store.get_discovery_run("` | — |
| [SRC-EEF2E6447C-L000764](../../api/omarai.py#L764) | 764 | `"                discovery_route[3],"` | — |
| [SRC-EEF2E6447C-L000765](../../api/omarai.py#L765) | 765 | `"                tenant_id=self._authenticated_principal[\"tenant_id\"],"` | — |
| [SRC-EEF2E6447C-L000766](../../api/omarai.py#L766) | 766 | `"            )"` | — |
| [SRC-EEF2E6447C-L000767](../../api/omarai.py#L767) | 767 | `"            return self.respond(200, run) if run else self.respond(404, {\"error\": \"discovery run not found\"})"` | — |
| [SRC-EEF2E6447C-L000768](../../api/omarai.py#L768) | 768 | `"        if parsed.path == \"/api/session\":"` | — |
| [SRC-EEF2E6447C-L000769](../../api/omarai.py#L769) | 769 | `"            if not self._rate_limit_ok():"` | — |
| [SRC-EEF2E6447C-L000770](../../api/omarai.py#L770) | 770 | `"                return self.respond(429, {\"error\": \"تجاوزت حد الطلبات المؤقت؛ حاول بعد دقيقة.\"})"` | — |
| [SRC-EEF2E6447C-L000771](../../api/omarai.py#L771) | 771 | `"            if not self._authorized():"` | — |
| [SRC-EEF2E6447C-L000772](../../api/omarai.py#L772) | 772 | `"                return self.respond(401, {\"error\": \"لا توجد جلسة صالحة؛ سجّل الدخول مجددًا.\"})"` | — |
| [SRC-EEF2E6447C-L000773](../../api/omarai.py#L773) | 773 | `"            return self.respond("` | — |
| [SRC-EEF2E6447C-L000774](../../api/omarai.py#L774) | 774 | `"                200,"` | — |
| [SRC-EEF2E6447C-L000775](../../api/omarai.py#L775) | 775 | `"                {"` | — |
| [SRC-EEF2E6447C-L000776](../../api/omarai.py#L776) | 776 | `"                    \"authenticated\": True,"` | — |
| [SRC-EEF2E6447C-L000777](../../api/omarai.py#L777) | 777 | `"                    \"role\": self._authenticated_principal[\"role\"],"` | — |
| [SRC-EEF2E6447C-L000778](../../api/omarai.py#L778) | 778 | `"                },"` | — |
| [SRC-EEF2E6447C-L000779](../../api/omarai.py#L779) | 779 | `"            )"` | — |
| [SRC-EEF2E6447C-L000780](../../api/omarai.py#L780) | 780 | `"        if parsed.path == \"/api/leads\":"` | — |
| [SRC-EEF2E6447C-L000781](../../api/omarai.py#L781) | 781 | `"            if not self._rate_limit_ok():"` | — |
| [SRC-EEF2E6447C-L000782](../../api/omarai.py#L782) | 782 | `"                return self.respond(429, {\"error\": \"تجاوزت حد الطلبات المؤقت؛ حاول بعد دقيقة.\"})"` | — |
| [SRC-EEF2E6447C-L000783](../../api/omarai.py#L783) | 783 | `"            if not self._authorized():"` | — |
| [SRC-EEF2E6447C-L000784](../../api/omarai.py#L784) | 784 | `"                return self.respond(401, {\"error\": \"يلزم رمز الوصول الخاص بالتطبيق.\"})"` | — |
| [SRC-EEF2E6447C-L000785](../../api/omarai.py#L785) | 785 | `"            q = parse_qs(parsed.query)"` | — |
| [SRC-EEF2E6447C-L000786](../../api/omarai.py#L786) | 786 | `"            try:"` | — |
| [SRC-EEF2E6447C-L000787](../../api/omarai.py#L787) | 787 | `"                limit = max(1, min(int(q.get(\"limit\", [\"100\"])[0]), 500))"` | — |
| [SRC-EEF2E6447C-L000788](../../api/omarai.py#L788) | 788 | `"                leads = self.store.list(q.get(\"status\", [None])[0], limit, tenant_id=self._authenticated_principal[\"tenant_id\"])"` | — |
| [SRC-EEF2E6447C-L000789](../../api/omarai.py#L789) | 789 | `"            except (ValueError, TypeError):"` | — |
| [SRC-EEF2E6447C-L000790](../../api/omarai.py#L790) | 790 | `"                return self.respond(400, {\"error\": \"invalid status or limit\"})"` | — |
| [SRC-EEF2E6447C-L000791](../../api/omarai.py#L791) | 791 | `"            return self.respond(200, {\"leads\": leads, \"count\": len(leads)})"` | — |
| [SRC-EEF2E6447C-L000792](../../api/omarai.py#L792) | 792 | `"        return self.respond(404, {\"error\": \"not found\"})"` | — |
| [SRC-EEF2E6447C-L000793](../../api/omarai.py#L793) | 793 | `""` | — |
| [SRC-EEF2E6447C-L000794](../../api/omarai.py#L794) | 794 | `"    def do_POST(self):"` | — |
| [SRC-EEF2E6447C-L000795](../../api/omarai.py#L795) | 795 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000796](../../api/omarai.py#L796) | 796 | `"            # Count API attempts before origin/content-type/body validation so invalid"` | — |
| [SRC-EEF2E6447C-L000797](../../api/omarai.py#L797) | 797 | `"            # credentials and malformed requests cannot bypass per-client throttling."` | — |
| [SRC-EEF2E6447C-L000798](../../api/omarai.py#L798) | 798 | `"            path = urlparse(self.path).path"` | — |
| [SRC-EEF2E6447C-L000799](../../api/omarai.py#L799) | 799 | `"            if path.startswith(\"/api/\") and not self._rate_limit_ok():"` | — |
| [SRC-EEF2E6447C-L000800](../../api/omarai.py#L800) | 800 | `"                return self.respond(429, {\"error\": \"تجاوزت حد الطلبات المؤقت؛ حاول بعد دقيقة.\"})"` | — |
| [SRC-EEF2E6447C-L000801](../../api/omarai.py#L801) | 801 | `"            session_login = path == \"/api/session\""` | — |
| [SRC-EEF2E6447C-L000802](../../api/omarai.py#L802) | 802 | `"            session_logout = path == \"/api/session/logout\""` | — |
| [SRC-EEF2E6447C-L000803](../../api/omarai.py#L803) | 803 | `"            if session_logout:"` | — |
| [SRC-EEF2E6447C-L000804](../../api/omarai.py#L804) | 804 | `"                # Logout is idempotent: an expired/revoked session must still be"` | — |
| [SRC-EEF2E6447C-L000805](../../api/omarai.py#L805) | 805 | `"                # able to clear the browser cookie. Resolve it opportunistically"` | — |
| [SRC-EEF2E6447C-L000806](../../api/omarai.py#L806) | 806 | `"                # so a live session is revoked, but do not require it to be valid."` | — |
| [SRC-EEF2E6447C-L000807](../../api/omarai.py#L807) | 807 | `"                self._authorized()"` | — |
| [SRC-EEF2E6447C-L000808](../../api/omarai.py#L808) | 808 | `"            elif path.startswith(\"/api/\") and not session_login and not self._authorized():"` | — |
| [SRC-EEF2E6447C-L000809](../../api/omarai.py#L809) | 809 | `"                return self.respond(401, {\"error\": \"يلزم رمز الوصول الخاص بالتطبيق.\"})"` | — |
| [SRC-EEF2E6447C-L000810](../../api/omarai.py#L810) | 810 | `""` | — |
| [SRC-EEF2E6447C-L000811](../../api/omarai.py#L811) | 811 | `"            content_type = self.headers.get(\"Content-Type\", \"\").split(\";\", 1)[0].strip().lower()"` | — |
| [SRC-EEF2E6447C-L000812](../../api/omarai.py#L812) | 812 | `"            if content_type != \"application/json\":"` | — |
| [SRC-EEF2E6447C-L000813](../../api/omarai.py#L813) | 813 | `"                return self.respond(415, {\"error\": \"Content-Type must be application/json\"})"` | — |
| [SRC-EEF2E6447C-L000814](../../api/omarai.py#L814) | 814 | `"            origin = self.headers.get(\"Origin\")"` | — |
| [SRC-EEF2E6447C-L000815](../../api/omarai.py#L815) | 815 | `"            if session_login and (not origin or not self._origin_allowed(origin)):"` | — |
| [SRC-EEF2E6447C-L000816](../../api/omarai.py#L816) | 816 | `"                return self.respond(403, {\"error\": \"browser session login requires a trusted same-origin request\"})"` | — |
| [SRC-EEF2E6447C-L000817](../../api/omarai.py#L817) | 817 | `"            if ("` | — |
| [SRC-EEF2E6447C-L000818](../../api/omarai.py#L818) | 818 | `"                session_logout"` | — |
| [SRC-EEF2E6447C-L000819](../../api/omarai.py#L819) | 819 | `"                and os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() == \"1\""` | — |
| [SRC-EEF2E6447C-L000820](../../api/omarai.py#L820) | 820 | `"                and (not origin or not self._origin_allowed(origin))"` | — |
| [SRC-EEF2E6447C-L000821](../../api/omarai.py#L821) | 821 | `"            ):"` | — |
| [SRC-EEF2E6447C-L000822](../../api/omarai.py#L822) | 822 | `"                return self.respond(403, {\"error\": \"browser session logout requires a trusted same-origin request\"})"` | — |
| [SRC-EEF2E6447C-L000823](../../api/omarai.py#L823) | 823 | `"            if origin and not self._origin_allowed(origin):"` | — |
| [SRC-EEF2E6447C-L000824](../../api/omarai.py#L824) | 824 | `"                return self.respond(403, {\"error\": \"cross-origin requests are not allowed\"})"` | — |
| [SRC-EEF2E6447C-L000825](../../api/omarai.py#L825) | 825 | `"            if getattr(self, \"_cookie_authenticated\", False) and ("` | — |
| [SRC-EEF2E6447C-L000826](../../api/omarai.py#L826) | 826 | `"                not origin or not self._origin_allowed(origin)"` | — |
| [SRC-EEF2E6447C-L000827](../../api/omarai.py#L827) | 827 | `"            ):"` | — |
| [SRC-EEF2E6447C-L000828](../../api/omarai.py#L828) | 828 | `"                return self.respond(403, {\"error\": \"cookie-authenticated requests require a trusted Origin\"})"` | — |
| [SRC-EEF2E6447C-L000829](../../api/omarai.py#L829) | 829 | `""` | — |
| [SRC-EEF2E6447C-L000830](../../api/omarai.py#L830) | 830 | `"            raw_body = self._read_request_body()"` | — |
| [SRC-EEF2E6447C-L000831](../../api/omarai.py#L831) | 831 | `"            if raw_body is None:"` | — |
| [SRC-EEF2E6447C-L000832](../../api/omarai.py#L832) | 832 | `"                return"` | — |
| [SRC-EEF2E6447C-L000833](../../api/omarai.py#L833) | 833 | `"            data = json.loads(raw_body)"` | — |
| [SRC-EEF2E6447C-L000834](../../api/omarai.py#L834) | 834 | `"            if not isinstance(data, dict):"` | — |
| [SRC-EEF2E6447C-L000835](../../api/omarai.py#L835) | 835 | `"                return self.respond(400, {\"error\": \"request body must be a JSON object\"})"` | — |
| [SRC-EEF2E6447C-L000836](../../api/omarai.py#L836) | 836 | `"            if path == \"/api/session\":"` | — |
| [SRC-EEF2E6447C-L000837](../../api/omarai.py#L837) | 837 | `"                token = data.get(\"access_token\", \"\")"` | — |
| [SRC-EEF2E6447C-L000838](../../api/omarai.py#L838) | 838 | `"                if not isinstance(token, str) or len(token.strip()) < 32:"` | — |
| [SRC-EEF2E6447C-L000839](../../api/omarai.py#L839) | 839 | `"                    return self.respond(401, {\"error\": \"رمز الوصول غير صالح.\"})"` | — |
| [SRC-EEF2E6447C-L000840](../../api/omarai.py#L840) | 840 | `"                session = self.store.create_web_session("` | — |
| [SRC-EEF2E6447C-L000841](../../api/omarai.py#L841) | 841 | `"                    token.strip(),"` | — |
| [SRC-EEF2E6447C-L000842](../../api/omarai.py#L842) | 842 | `"                    shared_token=os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip(),"` | — |
| [SRC-EEF2E6447C-L000843](../../api/omarai.py#L843) | 843 | `"                    max_age_seconds=BROWSER_SESSION_COOKIE_MAX_AGE,"` | — |
| [SRC-EEF2E6447C-L000844](../../api/omarai.py#L844) | 844 | `"                )"` | — |
| [SRC-EEF2E6447C-L000845](../../api/omarai.py#L845) | 845 | `"                if not session:"` | — |
| [SRC-EEF2E6447C-L000846](../../api/omarai.py#L846) | 846 | `"                    return self.respond(401, {\"error\": \"رمز الوصول غير صحيح أو منتهي الصلاحية.\"})"` | — |
| [SRC-EEF2E6447C-L000847](../../api/omarai.py#L847) | 847 | `"                session_id, principal = session"` | — |
| [SRC-EEF2E6447C-L000848](../../api/omarai.py#L848) | 848 | `"                self._authenticated_principal = principal"` | — |
| [SRC-EEF2E6447C-L000849](../../api/omarai.py#L849) | 849 | `"                return self.respond("` | — |
| [SRC-EEF2E6447C-L000850](../../api/omarai.py#L850) | 850 | `"                    200,"` | — |
| [SRC-EEF2E6447C-L000851](../../api/omarai.py#L851) | 851 | `"                    {\"authenticated\": True, \"role\": principal[\"role\"]},"` | — |
| [SRC-EEF2E6447C-L000852](../../api/omarai.py#L852) | 852 | `"                    extra_headers=[(\"Set-Cookie\", self._session_cookie_header(session_id))],"` | — |
| [SRC-EEF2E6447C-L000853](../../api/omarai.py#L853) | 853 | `"                )"` | — |
| [SRC-EEF2E6447C-L000854](../../api/omarai.py#L854) | 854 | `""` | — |
| [SRC-EEF2E6447C-L000855](../../api/omarai.py#L855) | 855 | `"            if path == \"/api/session/logout\":"` | — |
| [SRC-EEF2E6447C-L000856](../../api/omarai.py#L856) | 856 | `"                session_id = getattr(self, \"_browser_session_id\", \"\")"` | — |
| [SRC-EEF2E6447C-L000857](../../api/omarai.py#L857) | 857 | `"                if session_id:"` | — |
| [SRC-EEF2E6447C-L000858](../../api/omarai.py#L858) | 858 | `"                    self.store.revoke_web_session(session_id)"` | — |
| [SRC-EEF2E6447C-L000859](../../api/omarai.py#L859) | 859 | `"                return self.respond("` | — |
| [SRC-EEF2E6447C-L000860](../../api/omarai.py#L860) | 860 | `"                    200,"` | — |
| [SRC-EEF2E6447C-L000861](../../api/omarai.py#L861) | 861 | `"                    {\"logged_out\": True},"` | — |
| [SRC-EEF2E6447C-L000862](../../api/omarai.py#L862) | 862 | `"                    extra_headers=[(\"Set-Cookie\", self._clear_session_cookie_header())],"` | — |
| [SRC-EEF2E6447C-L000863](../../api/omarai.py#L863) | 863 | `"                )"` | — |
| [SRC-EEF2E6447C-L000864](../../api/omarai.py#L864) | 864 | `""` | — |
| [SRC-EEF2E6447C-L000865](../../api/omarai.py#L865) | 865 | `"            if path == \"/api/product-profiles\":"` | — |
| [SRC-EEF2E6447C-L000866](../../api/omarai.py#L866) | 866 | `"                principal = self._authenticated_principal"` | — |
| [SRC-EEF2E6447C-L000867](../../api/omarai.py#L867) | 867 | `"                if principal.get(\"role\") == \"viewer\":"` | — |
| [SRC-EEF2E6447C-L000868](../../api/omarai.py#L868) | 868 | `"                    return self.respond(403, {\"error\": \"هذه العضوية للقراءة فقط.\"})"` | — |
| [SRC-EEF2E6447C-L000869](../../api/omarai.py#L869) | 869 | `"                product, market, locale = _product_market_from_payload(data)"` | — |
| [SRC-EEF2E6447C-L000870](../../api/omarai.py#L870) | 870 | `"                saved = self.store.save_product_profile("` | — |
| [SRC-EEF2E6447C-L000871](../../api/omarai.py#L871) | 871 | `"                    {"` | — |
| [SRC-EEF2E6447C-L000872](../../api/omarai.py#L872) | 872 | `"                        \"product\": product.to_dict(),"` | — |
| [SRC-EEF2E6447C-L000873](../../api/omarai.py#L873) | 873 | `"                        \"market\": market.to_dict(),"` | — |
| [SRC-EEF2E6447C-L000874](../../api/omarai.py#L874) | 874 | `"                        \"locale\": locale,"` | — |
| [SRC-EEF2E6447C-L000875](../../api/omarai.py#L875) | 875 | `"                    },"` | — |
| [SRC-EEF2E6447C-L000876](../../api/omarai.py#L876) | 876 | `"                    tenant_id=principal[\"tenant_id\"],"` | — |
| [SRC-EEF2E6447C-L000877](../../api/omarai.py#L877) | 877 | `"                )"` | — |
| [SRC-EEF2E6447C-L000878](../../api/omarai.py#L878) | 878 | `"                return self.respond(201, saved)"` | — |
| [SRC-EEF2E6447C-L000879](../../api/omarai.py#L879) | 879 | `""` | — |
| [SRC-EEF2E6447C-L000880](../../api/omarai.py#L880) | 880 | `"            if path == \"/api/discoveries\":"` | — |
| [SRC-EEF2E6447C-L000881](../../api/omarai.py#L881) | 881 | `"                principal = self._authenticated_principal"` | — |
| [SRC-EEF2E6447C-L000882](../../api/omarai.py#L882) | 882 | `"                if principal.get(\"role\") == \"viewer\":"` | — |
| [SRC-EEF2E6447C-L000883](../../api/omarai.py#L883) | 883 | `"                    return self.respond(403, {\"error\": \"هذه العضوية للقراءة فقط؛ لا يمكنها تشغيل الاكتشاف.\"})"` | — |
| [SRC-EEF2E6447C-L000884](../../api/omarai.py#L884) | 884 | `"                profile_id = data.get(\"profile_id\")"` | — |
| [SRC-EEF2E6447C-L000885](../../api/omarai.py#L885) | 885 | `"                if not isinstance(profile_id, str) or not profile_id.strip():"` | — |
| [SRC-EEF2E6447C-L000886](../../api/omarai.py#L886) | 886 | `"                    return self.respond(400, {\"error\": \"profile_id is required\"})"` | — |
| [SRC-EEF2E6447C-L000887](../../api/omarai.py#L887) | 887 | `"                allow_optional = data.get(\"allow_optional_providers\", False)"` | — |
| [SRC-EEF2E6447C-L000888](../../api/omarai.py#L888) | 888 | `"                if not isinstance(allow_optional, bool):"` | — |
| [SRC-EEF2E6447C-L000889](../../api/omarai.py#L889) | 889 | `"                    return self.respond(400, {\"error\": \"allow_optional_providers must be a boolean\"})"` | — |
| [SRC-EEF2E6447C-L000890](../../api/omarai.py#L890) | 890 | `"                if allow_optional and principal.get(\"role\") != \"owner\":"` | — |
| [SRC-EEF2E6447C-L000891](../../api/omarai.py#L891) | 891 | `"                    return self.respond("` | — |
| [SRC-EEF2E6447C-L000892](../../api/omarai.py#L892) | 892 | `"                        403,"` | — |
| [SRC-EEF2E6447C-L000893](../../api/omarai.py#L893) | 893 | `"                        {\"error\": \"تفعيل موصلات البحث الاختيارية ذات الحصص متاح لمالك مساحة العمل فقط.\"},"` | — |
| [SRC-EEF2E6447C-L000894](../../api/omarai.py#L894) | 894 | `"                    )"` | — |
| [SRC-EEF2E6447C-L000895](../../api/omarai.py#L895) | 895 | `"                profile = self.store.get_product_profile("` | — |
| [SRC-EEF2E6447C-L000896](../../api/omarai.py#L896) | 896 | `"                    profile_id, tenant_id=principal[\"tenant_id\"]"` | — |
| [SRC-EEF2E6447C-L000897](../../api/omarai.py#L897) | 897 | `"                )"` | — |
