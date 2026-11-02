# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **046**
- سجلات الأسطر: **800**
- النطاق: SRC-1A176AD4F0-L000147 إلى SRC-EA6EC52573-L000293
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-1A176AD4F0 — [tests/test_hosted_smoke.py](../../tests/test_hosted_smoke.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1A176AD4F0-L000147](../../tests/test_hosted_smoke.py#L147) | 147 | `"    )"` | — |
| [SRC-1A176AD4F0-L000148](../../tests/test_hosted_smoke.py#L148) | 148 | `"    destination_thread.start()"` | — |
| [SRC-1A176AD4F0-L000149](../../tests/test_hosted_smoke.py#L149) | 149 | `"    source_thread.start()"` | — |
| [SRC-1A176AD4F0-L000150](../../tests/test_hosted_smoke.py#L150) | 150 | `"    try:"` | — |
| [SRC-1A176AD4F0-L000151](../../tests/test_hosted_smoke.py#L151) | 151 | `"        status, payload = hosted_smoke_test.request_json("` | — |
| [SRC-1A176AD4F0-L000152](../../tests/test_hosted_smoke.py#L152) | 152 | `"            f\"http://127.0.0.1:{source.server_port}/redirect\","` | — |
| [SRC-1A176AD4F0-L000153](../../tests/test_hosted_smoke.py#L153) | 153 | `"            token=TOKEN,"` | — |
| [SRC-1A176AD4F0-L000154](../../tests/test_hosted_smoke.py#L154) | 154 | `"            timeout=3,"` | — |
| [SRC-1A176AD4F0-L000155](../../tests/test_hosted_smoke.py#L155) | 155 | `"        )"` | — |
| [SRC-1A176AD4F0-L000156](../../tests/test_hosted_smoke.py#L156) | 156 | `"        assert status == 302"` | — |
| [SRC-1A176AD4F0-L000157](../../tests/test_hosted_smoke.py#L157) | 157 | `"        assert payload is None"` | — |
| [SRC-1A176AD4F0-L000158](../../tests/test_hosted_smoke.py#L158) | 158 | `"        assert received_authorizations == []"` | — |
| [SRC-1A176AD4F0-L000159](../../tests/test_hosted_smoke.py#L159) | 159 | `"    finally:"` | — |
| [SRC-1A176AD4F0-L000160](../../tests/test_hosted_smoke.py#L160) | 160 | `"        source.shutdown()"` | — |
| [SRC-1A176AD4F0-L000161](../../tests/test_hosted_smoke.py#L161) | 161 | `"        destination.shutdown()"` | — |
| [SRC-1A176AD4F0-L000162](../../tests/test_hosted_smoke.py#L162) | 162 | `"        source.server_close()"` | — |
| [SRC-1A176AD4F0-L000163](../../tests/test_hosted_smoke.py#L163) | 163 | `"        destination.server_close()"` | — |
| [SRC-1A176AD4F0-L000164](../../tests/test_hosted_smoke.py#L164) | 164 | `"        source_thread.join(timeout=2)"` | — |
| [SRC-1A176AD4F0-L000165](../../tests/test_hosted_smoke.py#L165) | 165 | `"        destination_thread.join(timeout=2)"` | — |
| [SRC-1A176AD4F0-L000166](../../tests/test_hosted_smoke.py#L166) | 166 | `""` | — |
| [SRC-1A176AD4F0-L000167](../../tests/test_hosted_smoke.py#L167) | 167 | `""` | — |
| [SRC-1A176AD4F0-L000168](../../tests/test_hosted_smoke.py#L168) | 168 | `"def test_smoke_refuses_missing_or_short_access_token(hosted_server):"` | — |
| [SRC-1A176AD4F0-L000169](../../tests/test_hosted_smoke.py#L169) | 169 | `"    with pytest.raises(SmokeError, match=\"OMARAI_ACCESS_TOKEN\"):"` | — |
| [SRC-1A176AD4F0-L000170](../../tests/test_hosted_smoke.py#L170) | 170 | `"        run_smoke(hosted_server, \"\", allow_http=True, allow_provider_usage=True, timeout=5)"` | — |
| [SRC-1A176AD4F0-L000171](../../tests/test_hosted_smoke.py#L171) | 171 | `""` | — |
| [SRC-1A176AD4F0-L000172](../../tests/test_hosted_smoke.py#L172) | 172 | `""` | — |
| [SRC-1A176AD4F0-L000173](../../tests/test_hosted_smoke.py#L173) | 173 | `"def test_smoke_fails_when_agent_returns_no_live_source(hosted_server, monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000174](../../tests/test_hosted_smoke.py#L174) | 174 | `"    original = hosted_smoke_test.request_json"` | — |
| [SRC-1A176AD4F0-L000175](../../tests/test_hosted_smoke.py#L175) | 175 | `""` | — |
| [SRC-1A176AD4F0-L000176](../../tests/test_hosted_smoke.py#L176) | 176 | `"    def without_sources(url: str, **kwargs):"` | — |
| [SRC-1A176AD4F0-L000177](../../tests/test_hosted_smoke.py#L177) | 177 | `"        if urlsplit(url).path == \"/api/agent\" and kwargs.get(\"token\") == TOKEN:"` | — |
| [SRC-1A176AD4F0-L000178](../../tests/test_hosted_smoke.py#L178) | 178 | `"            return 200, {"` | — |
| [SRC-1A176AD4F0-L000179](../../tests/test_hosted_smoke.py#L179) | 179 | `"                \"answer\": \"إجابة بلا مصادر\", \"used_web_search\": False,"` | — |
| [SRC-1A176AD4F0-L000180](../../tests/test_hosted_smoke.py#L180) | 180 | `"                \"used_language_model\": True, \"sources\": [],"` | — |
| [SRC-1A176AD4F0-L000181](../../tests/test_hosted_smoke.py#L181) | 181 | `"            }"` | — |
| [SRC-1A176AD4F0-L000182](../../tests/test_hosted_smoke.py#L182) | 182 | `"        return original(url, **kwargs)"` | — |
| [SRC-1A176AD4F0-L000183](../../tests/test_hosted_smoke.py#L183) | 183 | `""` | — |
| [SRC-1A176AD4F0-L000184](../../tests/test_hosted_smoke.py#L184) | 184 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", without_sources)"` | — |
| [SRC-1A176AD4F0-L000185](../../tests/test_hosted_smoke.py#L185) | 185 | `"    with pytest.raises(SmokeError, match=\"usable source URLs\") as failure:"` | — |
| [SRC-1A176AD4F0-L000186](../../tests/test_hosted_smoke.py#L186) | 186 | `"        run_smoke(hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5)"` | — |
| [SRC-1A176AD4F0-L000187](../../tests/test_hosted_smoke.py#L187) | 187 | `"    assert failure.value.report[\"transcript\"][0][\"question\"] == ("` | — |
| [SRC-1A176AD4F0-L000188](../../tests/test_hosted_smoke.py#L188) | 188 | `"        hosted_smoke_test.LIVE_TEST_QUESTION"` | — |
| [SRC-1A176AD4F0-L000189](../../tests/test_hosted_smoke.py#L189) | 189 | `"    )"` | — |
| [SRC-1A176AD4F0-L000190](../../tests/test_hosted_smoke.py#L190) | 190 | `"    assert failure.value.report[\"transcript\"][0][\"answer\"] == \"إجابة بلا مصادر\""` | — |
| [SRC-1A176AD4F0-L000191](../../tests/test_hosted_smoke.py#L191) | 191 | `""` | — |
| [SRC-1A176AD4F0-L000192](../../tests/test_hosted_smoke.py#L192) | 192 | `""` | — |
| [SRC-1A176AD4F0-L000193](../../tests/test_hosted_smoke.py#L193) | 193 | `"def test_smoke_rejects_invalid_expected_source_sha(hosted_server):"` | — |
| [SRC-1A176AD4F0-L000194](../../tests/test_hosted_smoke.py#L194) | 194 | `"    with pytest.raises(SmokeError, match=\"40-character Git SHA\"):"` | — |
| [SRC-1A176AD4F0-L000195](../../tests/test_hosted_smoke.py#L195) | 195 | `"        run_smoke("` | — |
| [SRC-1A176AD4F0-L000196](../../tests/test_hosted_smoke.py#L196) | 196 | `"            hosted_server, TOKEN, allow_http=True, timeout=5, expected_sha=\"main\""` | — |
| [SRC-1A176AD4F0-L000197](../../tests/test_hosted_smoke.py#L197) | 197 | `"        )"` | — |
| [SRC-1A176AD4F0-L000198](../../tests/test_hosted_smoke.py#L198) | 198 | `""` | — |
| [SRC-1A176AD4F0-L000199](../../tests/test_hosted_smoke.py#L199) | 199 | `""` | — |
| [SRC-1A176AD4F0-L000200](../../tests/test_hosted_smoke.py#L200) | 200 | `"def test_smoke_rejects_deployed_build_sha_mismatch(hosted_server):"` | — |
| [SRC-1A176AD4F0-L000201](../../tests/test_hosted_smoke.py#L201) | 201 | `"    with pytest.raises(SmokeError, match=\"does not match the expected Git commit\"):"` | — |
| [SRC-1A176AD4F0-L000202](../../tests/test_hosted_smoke.py#L202) | 202 | `"        run_smoke("` | — |
| [SRC-1A176AD4F0-L000203](../../tests/test_hosted_smoke.py#L203) | 203 | `"            hosted_server,"` | — |
| [SRC-1A176AD4F0-L000204](../../tests/test_hosted_smoke.py#L204) | 204 | `"            TOKEN,"` | — |
| [SRC-1A176AD4F0-L000205](../../tests/test_hosted_smoke.py#L205) | 205 | `"            allow_http=True,"` | — |
| [SRC-1A176AD4F0-L000206](../../tests/test_hosted_smoke.py#L206) | 206 | `"            allow_provider_usage=True,"` | — |
| [SRC-1A176AD4F0-L000207](../../tests/test_hosted_smoke.py#L207) | 207 | `"            timeout=5,"` | — |
| [SRC-1A176AD4F0-L000208](../../tests/test_hosted_smoke.py#L208) | 208 | `"            expected_sha=\"a\" * 40,"` | — |
| [SRC-1A176AD4F0-L000209](../../tests/test_hosted_smoke.py#L209) | 209 | `"        )"` | — |
| [SRC-1A176AD4F0-L000210](../../tests/test_hosted_smoke.py#L210) | 210 | `""` | — |
| [SRC-1A176AD4F0-L000211](../../tests/test_hosted_smoke.py#L211) | 211 | `""` | — |
| [SRC-1A176AD4F0-L000212](../../tests/test_hosted_smoke.py#L212) | 212 | `""` | — |
| [SRC-1A176AD4F0-L000213](../../tests/test_hosted_smoke.py#L213) | 213 | `"def test_http_403_report_contains_only_safe_response_metadata():"` | — |
| [SRC-1A176AD4F0-L000214](../../tests/test_hosted_smoke.py#L214) | 214 | `"    class ForbiddenHandler(BaseHTTPRequestHandler):"` | — |
| [SRC-1A176AD4F0-L000215](../../tests/test_hosted_smoke.py#L215) | 215 | `"        def log_message(self, format: str, *args: object) -> None:"` | — |
| [SRC-1A176AD4F0-L000216](../../tests/test_hosted_smoke.py#L216) | 216 | `"            return"` | — |
| [SRC-1A176AD4F0-L000217](../../tests/test_hosted_smoke.py#L217) | 217 | `""` | — |
| [SRC-1A176AD4F0-L000218](../../tests/test_hosted_smoke.py#L218) | 218 | `"        def do_GET(self) -> None:"` | — |
| [SRC-1A176AD4F0-L000219](../../tests/test_hosted_smoke.py#L219) | 219 | `"            body = b\"<html>blocked</html>\""` | — |
| [SRC-1A176AD4F0-L000220](../../tests/test_hosted_smoke.py#L220) | 220 | `"            self.send_response(403)"` | — |
| [SRC-1A176AD4F0-L000221](../../tests/test_hosted_smoke.py#L221) | 221 | `"            self.send_header(\"Content-Type\", \"text/html\")"` | — |
| [SRC-1A176AD4F0-L000222](../../tests/test_hosted_smoke.py#L222) | 222 | `"            self.send_header(\"X-Request-ID\", \"request-123\")"` | — |
| [SRC-1A176AD4F0-L000223](../../tests/test_hosted_smoke.py#L223) | 223 | `"            self.send_header(\"CF-Ray\", \"ray-456\")"` | — |
| [SRC-1A176AD4F0-L000224](../../tests/test_hosted_smoke.py#L224) | 224 | `"            self.send_header(\"Content-Length\", str(len(body)))"` | — |
| [SRC-1A176AD4F0-L000225](../../tests/test_hosted_smoke.py#L225) | 225 | `"            self.end_headers()"` | — |
| [SRC-1A176AD4F0-L000226](../../tests/test_hosted_smoke.py#L226) | 226 | `"            self.wfile.write(body)"` | — |
| [SRC-1A176AD4F0-L000227](../../tests/test_hosted_smoke.py#L227) | 227 | `""` | — |
| [SRC-1A176AD4F0-L000228](../../tests/test_hosted_smoke.py#L228) | 228 | `"    server = ThreadingHTTPServer((\"127.0.0.1\", 0), ForbiddenHandler)"` | — |
| [SRC-1A176AD4F0-L000229](../../tests/test_hosted_smoke.py#L229) | 229 | `"    thread = threading.Thread(target=server.serve_forever, daemon=True)"` | — |
| [SRC-1A176AD4F0-L000230](../../tests/test_hosted_smoke.py#L230) | 230 | `"    thread.start()"` | — |
| [SRC-1A176AD4F0-L000231](../../tests/test_hosted_smoke.py#L231) | 231 | `"    try:"` | — |
| [SRC-1A176AD4F0-L000232](../../tests/test_hosted_smoke.py#L232) | 232 | `"        status, payload = hosted_smoke_test.request_json("` | — |
| [SRC-1A176AD4F0-L000233](../../tests/test_hosted_smoke.py#L233) | 233 | `"            f\"http://127.0.0.1:{server.server_port}/api/health\","` | — |
| [SRC-1A176AD4F0-L000234](../../tests/test_hosted_smoke.py#L234) | 234 | `"            token=TOKEN,"` | — |
| [SRC-1A176AD4F0-L000235](../../tests/test_hosted_smoke.py#L235) | 235 | `"            timeout=3,"` | — |
| [SRC-1A176AD4F0-L000236](../../tests/test_hosted_smoke.py#L236) | 236 | `"        )"` | — |
| [SRC-1A176AD4F0-L000237](../../tests/test_hosted_smoke.py#L237) | 237 | `"        assert status == 403"` | — |
| [SRC-1A176AD4F0-L000238](../../tests/test_hosted_smoke.py#L238) | 238 | `"        assert payload[\"_smoke_http\"][\"status\"] == 403"` | — |
| [SRC-1A176AD4F0-L000239](../../tests/test_hosted_smoke.py#L239) | 239 | `"        assert payload[\"_smoke_http\"][\"request_id\"] == \"request-123\""` | — |
| [SRC-1A176AD4F0-L000240](../../tests/test_hosted_smoke.py#L240) | 240 | `"        assert payload[\"_smoke_http\"][\"cf_ray\"] == \"ray-456\""` | — |
| [SRC-1A176AD4F0-L000241](../../tests/test_hosted_smoke.py#L241) | 241 | `"        assert payload[\"_smoke_http\"][\"body_bytes_sampled\"] == len(b\"<html>blocked</html>\")"` | — |
| [SRC-1A176AD4F0-L000242](../../tests/test_hosted_smoke.py#L242) | 242 | `"        assert \"body_sha256\" in payload[\"_smoke_http\"]"` | — |
| [SRC-1A176AD4F0-L000243](../../tests/test_hosted_smoke.py#L243) | 243 | `"        assert \"blocked\" not in str(payload)"` | — |
| [SRC-1A176AD4F0-L000244](../../tests/test_hosted_smoke.py#L244) | 244 | `"        assert TOKEN not in str(payload)"` | — |
| [SRC-1A176AD4F0-L000245](../../tests/test_hosted_smoke.py#L245) | 245 | `"    finally:"` | — |
| [SRC-1A176AD4F0-L000246](../../tests/test_hosted_smoke.py#L246) | 246 | `"        server.shutdown()"` | — |
| [SRC-1A176AD4F0-L000247](../../tests/test_hosted_smoke.py#L247) | 247 | `"        server.server_close()"` | — |
| [SRC-1A176AD4F0-L000248](../../tests/test_hosted_smoke.py#L248) | 248 | `"        thread.join(timeout=2)"` | — |
| [SRC-1A176AD4F0-L000249](../../tests/test_hosted_smoke.py#L249) | 249 | `""` | — |
| [SRC-1A176AD4F0-L000250](../../tests/test_hosted_smoke.py#L250) | 250 | `""` | — |
| [SRC-1A176AD4F0-L000251](../../tests/test_hosted_smoke.py#L251) | 251 | `""` | — |
| [SRC-1A176AD4F0-L000252](../../tests/test_hosted_smoke.py#L252) | 252 | `"def test_health_403_metadata_is_preserved_in_failure_report(monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000253](../../tests/test_hosted_smoke.py#L253) | 253 | `"    metadata = {"` | — |
| [SRC-1A176AD4F0-L000254](../../tests/test_hosted_smoke.py#L254) | 254 | `"        \"status\": 403,"` | — |
| [SRC-1A176AD4F0-L000255](../../tests/test_hosted_smoke.py#L255) | 255 | `"        \"content_type\": \"text/html\","` | — |
| [SRC-1A176AD4F0-L000256](../../tests/test_hosted_smoke.py#L256) | 256 | `"        \"server\": \"edge-gateway\","` | — |
| [SRC-1A176AD4F0-L000257](../../tests/test_hosted_smoke.py#L257) | 257 | `"        \"request_id\": \"request-403\","` | — |
| [SRC-1A176AD4F0-L000258](../../tests/test_hosted_smoke.py#L258) | 258 | `"        \"correlation_id\": \"\","` | — |
| [SRC-1A176AD4F0-L000259](../../tests/test_hosted_smoke.py#L259) | 259 | `"        \"cf_ray\": \"ray-403\","` | — |
| [SRC-1A176AD4F0-L000260](../../tests/test_hosted_smoke.py#L260) | 260 | `"        \"via\": \"\","` | — |
| [SRC-1A176AD4F0-L000261](../../tests/test_hosted_smoke.py#L261) | 261 | `"        \"body_bytes_sampled\": 19,"` | — |
| [SRC-1A176AD4F0-L000262](../../tests/test_hosted_smoke.py#L262) | 262 | `"        \"body_sha256\": \"a\" * 64,"` | — |
| [SRC-1A176AD4F0-L000263](../../tests/test_hosted_smoke.py#L263) | 263 | `"    }"` | — |
| [SRC-1A176AD4F0-L000264](../../tests/test_hosted_smoke.py#L264) | 264 | `""` | — |
| [SRC-1A176AD4F0-L000265](../../tests/test_hosted_smoke.py#L265) | 265 | `"    def forbidden_health(url: str, **kwargs):"` | — |
| [SRC-1A176AD4F0-L000266](../../tests/test_hosted_smoke.py#L266) | 266 | `"        return 403, {\"_smoke_http\": metadata}"` | — |
| [SRC-1A176AD4F0-L000267](../../tests/test_hosted_smoke.py#L267) | 267 | `""` | — |
| [SRC-1A176AD4F0-L000268](../../tests/test_hosted_smoke.py#L268) | 268 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", forbidden_health)"` | — |
| [SRC-1A176AD4F0-L000269](../../tests/test_hosted_smoke.py#L269) | 269 | `"    with pytest.raises(SmokeError, match=\"Health check failed\") as failure:"` | — |
| [SRC-1A176AD4F0-L000270](../../tests/test_hosted_smoke.py#L270) | 270 | `"        run_smoke(\"https://omarai.example.test\", TOKEN, allow_provider_usage=False)"` | — |
| [SRC-1A176AD4F0-L000271](../../tests/test_hosted_smoke.py#L271) | 271 | `"    assert failure.value.report[\"http_response\"] == metadata"` | — |
| [SRC-1A176AD4F0-L000272](../../tests/test_hosted_smoke.py#L272) | 272 | `"    assert \"blocked\" not in str(failure.value.report)"` | — |
| [SRC-1A176AD4F0-L000273](../../tests/test_hosted_smoke.py#L273) | 273 | `""` | — |
| [SRC-1A176AD4F0-L000274](../../tests/test_hosted_smoke.py#L274) | 274 | `""` | — |
| [SRC-1A176AD4F0-L000275](../../tests/test_hosted_smoke.py#L275) | 275 | `""` | — |
| [SRC-1A176AD4F0-L000276](../../tests/test_hosted_smoke.py#L276) | 276 | `"def test_hosted_preflight_allows_remote_no_token_and_still_checks_auth_rejection(monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000277](../../tests/test_hosted_smoke.py#L277) | 277 | `"    calls = []"` | — |
| [SRC-1A176AD4F0-L000278](../../tests/test_hosted_smoke.py#L278) | 278 | `""` | — |
| [SRC-1A176AD4F0-L000279](../../tests/test_hosted_smoke.py#L279) | 279 | `"    def fake_request(url: str, *, token=\"\", payload=None, timeout=90):"` | — |
| [SRC-1A176AD4F0-L000280](../../tests/test_hosted_smoke.py#L280) | 280 | `"        path = urlsplit(url).path"` | — |
| [SRC-1A176AD4F0-L000281](../../tests/test_hosted_smoke.py#L281) | 281 | `"        calls.append((path, token))"` | — |
| [SRC-1A176AD4F0-L000282](../../tests/test_hosted_smoke.py#L282) | 282 | `"        if path == \"/api/health\":"` | — |
| [SRC-1A176AD4F0-L000283](../../tests/test_hosted_smoke.py#L283) | 283 | `"            return 200, {\"ok\": True}"` | — |
| [SRC-1A176AD4F0-L000284](../../tests/test_hosted_smoke.py#L284) | 284 | `"        if path == \"/api/agent\" and not token:"` | — |
| [SRC-1A176AD4F0-L000285](../../tests/test_hosted_smoke.py#L285) | 285 | `"            assert payload == {\"question\": \"\"}"` | — |
| [SRC-1A176AD4F0-L000286](../../tests/test_hosted_smoke.py#L286) | 286 | `"            return 401, None"` | — |
| [SRC-1A176AD4F0-L000287](../../tests/test_hosted_smoke.py#L287) | 287 | `"        raise AssertionError(\"preflight must not call authenticated agent/search/model paths\")"` | — |
| [SRC-1A176AD4F0-L000288](../../tests/test_hosted_smoke.py#L288) | 288 | `""` | — |
| [SRC-1A176AD4F0-L000289](../../tests/test_hosted_smoke.py#L289) | 289 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", fake_request)"` | — |
| [SRC-1A176AD4F0-L000290](../../tests/test_hosted_smoke.py#L290) | 290 | `"    result = run_smoke("` | — |
| [SRC-1A176AD4F0-L000291](../../tests/test_hosted_smoke.py#L291) | 291 | `"        \"https://omarai.example.test\","` | — |
| [SRC-1A176AD4F0-L000292](../../tests/test_hosted_smoke.py#L292) | 292 | `"        \"\","` | — |
| [SRC-1A176AD4F0-L000293](../../tests/test_hosted_smoke.py#L293) | 293 | `"        preflight_only=True,"` | — |
| [SRC-1A176AD4F0-L000294](../../tests/test_hosted_smoke.py#L294) | 294 | `"        allow_provider_usage=False,"` | — |
| [SRC-1A176AD4F0-L000295](../../tests/test_hosted_smoke.py#L295) | 295 | `"    )"` | — |
| [SRC-1A176AD4F0-L000296](../../tests/test_hosted_smoke.py#L296) | 296 | `"    assert result[\"result\"] == \"preflight_passed\""` | — |
| [SRC-1A176AD4F0-L000297](../../tests/test_hosted_smoke.py#L297) | 297 | `"    assert result[\"auth_mode\"] == \"preflight_no_token\""` | — |
| [SRC-1A176AD4F0-L000298](../../tests/test_hosted_smoke.py#L298) | 298 | `"    assert result[\"checks\"][\"authentication\"] == \"passed\""` | — |
| [SRC-1A176AD4F0-L000299](../../tests/test_hosted_smoke.py#L299) | 299 | `"    assert calls == [(\"/api/health\", \"\"), (\"/api/agent\", \"\")]"` | — |
| [SRC-1A176AD4F0-L000300](../../tests/test_hosted_smoke.py#L300) | 300 | `""` | — |
| [SRC-1A176AD4F0-L000301](../../tests/test_hosted_smoke.py#L301) | 301 | `""` | — |
| [SRC-1A176AD4F0-L000302](../../tests/test_hosted_smoke.py#L302) | 302 | `""` | — |
| [SRC-1A176AD4F0-L000303](../../tests/test_hosted_smoke.py#L303) | 303 | `""` | — |
| [SRC-1A176AD4F0-L000304](../../tests/test_hosted_smoke.py#L304) | 304 | `"def test_preflight_fails_closed_if_unauthenticated_agent_probe_reaches_validation(monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000305](../../tests/test_hosted_smoke.py#L305) | 305 | `"    calls = []"` | — |
| [SRC-1A176AD4F0-L000306](../../tests/test_hosted_smoke.py#L306) | 306 | `""` | — |
| [SRC-1A176AD4F0-L000307](../../tests/test_hosted_smoke.py#L307) | 307 | `"    def auth_bypass(url: str, *, token=\"\", payload=None, timeout=90):"` | — |
| [SRC-1A176AD4F0-L000308](../../tests/test_hosted_smoke.py#L308) | 308 | `"        path = urlsplit(url).path"` | — |
| [SRC-1A176AD4F0-L000309](../../tests/test_hosted_smoke.py#L309) | 309 | `"        calls.append((path, token, payload))"` | — |
| [SRC-1A176AD4F0-L000310](../../tests/test_hosted_smoke.py#L310) | 310 | `"        if path == \"/api/health\":"` | — |
| [SRC-1A176AD4F0-L000311](../../tests/test_hosted_smoke.py#L311) | 311 | `"            return 200, {\"ok\": True}"` | — |
| [SRC-1A176AD4F0-L000312](../../tests/test_hosted_smoke.py#L312) | 312 | `"        if path == \"/api/agent\" and not token:"` | — |
| [SRC-1A176AD4F0-L000313](../../tests/test_hosted_smoke.py#L313) | 313 | `"            assert payload == {\"question\": \"\"}"` | — |
| [SRC-1A176AD4F0-L000314](../../tests/test_hosted_smoke.py#L314) | 314 | `"            # The API reached question validation, so its auth gate did not reject first."` | — |
| [SRC-1A176AD4F0-L000315](../../tests/test_hosted_smoke.py#L315) | 315 | `"            return 400, {\"error\": \"question must be a non-empty string\"}"` | — |
| [SRC-1A176AD4F0-L000316](../../tests/test_hosted_smoke.py#L316) | 316 | `"        raise AssertionError(\"no authenticated agent request is allowed in preflight\")"` | — |
| [SRC-1A176AD4F0-L000317](../../tests/test_hosted_smoke.py#L317) | 317 | `""` | — |
| [SRC-1A176AD4F0-L000318](../../tests/test_hosted_smoke.py#L318) | 318 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", auth_bypass)"` | — |
| [SRC-1A176AD4F0-L000319](../../tests/test_hosted_smoke.py#L319) | 319 | `"    with pytest.raises(SmokeError, match=\"should return 401\"):"` | — |
| [SRC-1A176AD4F0-L000320](../../tests/test_hosted_smoke.py#L320) | 320 | `"        run_smoke(\"https://omarai.example.test\", \"\", preflight_only=True)"` | — |
| [SRC-1A176AD4F0-L000321](../../tests/test_hosted_smoke.py#L321) | 321 | `"    assert calls == [(\"/api/health\", \"\", None), (\"/api/agent\", \"\", {\"question\": \"\"})]"` | — |
| [SRC-1A176AD4F0-L000322](../../tests/test_hosted_smoke.py#L322) | 322 | `""` | — |
| [SRC-1A176AD4F0-L000323](../../tests/test_hosted_smoke.py#L323) | 323 | `""` | — |
| [SRC-1A176AD4F0-L000324](../../tests/test_hosted_smoke.py#L324) | 324 | `""` | — |
| [SRC-1A176AD4F0-L000325](../../tests/test_hosted_smoke.py#L325) | 325 | `"def test_smoke_preflight_runs_without_provider_usage_or_model_calls(hosted_server):"` | — |
| [SRC-1A176AD4F0-L000326](../../tests/test_hosted_smoke.py#L326) | 326 | `"    result = run_smoke("` | — |
| [SRC-1A176AD4F0-L000327](../../tests/test_hosted_smoke.py#L327) | 327 | `"        hosted_server, TOKEN, allow_http=True, preflight_only=True, allow_provider_usage=False, timeout=5"` | — |
| [SRC-1A176AD4F0-L000328](../../tests/test_hosted_smoke.py#L328) | 328 | `"    )"` | — |
| [SRC-1A176AD4F0-L000329](../../tests/test_hosted_smoke.py#L329) | 329 | `"    assert result[\"result\"] == \"preflight_passed\""` | — |
| [SRC-1A176AD4F0-L000330](../../tests/test_hosted_smoke.py#L330) | 330 | `"    assert result[\"checks\"][\"health\"] == \"passed\""` | — |
| [SRC-1A176AD4F0-L000331](../../tests/test_hosted_smoke.py#L331) | 331 | `"    assert result[\"checks\"][\"authentication\"] == \"passed\""` | — |
| [SRC-1A176AD4F0-L000332](../../tests/test_hosted_smoke.py#L332) | 332 | `"    assert result[\"checks\"][\"provider_usage\"][\"status\"] == \"skipped_not_approved\""` | — |
| [SRC-1A176AD4F0-L000333](../../tests/test_hosted_smoke.py#L333) | 333 | `"    assert result[\"transcript\"] == []"` | — |
| [SRC-1A176AD4F0-L000334](../../tests/test_hosted_smoke.py#L334) | 334 | `""` | — |
| [SRC-1A176AD4F0-L000335](../../tests/test_hosted_smoke.py#L335) | 335 | `""` | — |
| [SRC-1A176AD4F0-L000336](../../tests/test_hosted_smoke.py#L336) | 336 | `"def test_smoke_requires_provider_approval_after_no_cost_preflight(monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000337](../../tests/test_hosted_smoke.py#L337) | 337 | `"    calls = []"` | — |
| [SRC-1A176AD4F0-L000338](../../tests/test_hosted_smoke.py#L338) | 338 | `""` | — |
| [SRC-1A176AD4F0-L000339](../../tests/test_hosted_smoke.py#L339) | 339 | `"    def fake_request(url, *, token=\"\", payload=None, timeout=90):"` | — |
| [SRC-1A176AD4F0-L000340](../../tests/test_hosted_smoke.py#L340) | 340 | `"        calls.append((urlsplit(url).path, token, payload))"` | — |
| [SRC-1A176AD4F0-L000341](../../tests/test_hosted_smoke.py#L341) | 341 | `"        if url.endswith(\"/api/health\"):"` | — |
| [SRC-1A176AD4F0-L000342](../../tests/test_hosted_smoke.py#L342) | 342 | `"            return 200, {\"ok\": True}"` | — |
| [SRC-1A176AD4F0-L000343](../../tests/test_hosted_smoke.py#L343) | 343 | `"        if url.endswith(\"/api/agent\") and not token:"` | — |
| [SRC-1A176AD4F0-L000344](../../tests/test_hosted_smoke.py#L344) | 344 | `"            assert payload == {\"question\": \"\"}"` | — |
| [SRC-1A176AD4F0-L000345](../../tests/test_hosted_smoke.py#L345) | 345 | `"            return 401, None"` | — |
| [SRC-1A176AD4F0-L000346](../../tests/test_hosted_smoke.py#L346) | 346 | `"        raise AssertionError(\"provider-dependent request must not run without approval\")"` | — |
| [SRC-1A176AD4F0-L000347](../../tests/test_hosted_smoke.py#L347) | 347 | `""` | — |
| [SRC-1A176AD4F0-L000348](../../tests/test_hosted_smoke.py#L348) | 348 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", fake_request)"` | — |
| [SRC-1A176AD4F0-L000349](../../tests/test_hosted_smoke.py#L349) | 349 | `"    with pytest.raises(SmokeError, match=\"explicit human approval\") as failure:"` | — |
| [SRC-1A176AD4F0-L000350](../../tests/test_hosted_smoke.py#L350) | 350 | `"        run_smoke(\"https://omarai.example.test\", TOKEN, allow_provider_usage=False)"` | — |
| [SRC-1A176AD4F0-L000351](../../tests/test_hosted_smoke.py#L351) | 351 | `"    assert calls == [(\"/api/health\", \"\", None), (\"/api/agent\", \"\", {\"question\": \"\"})]"` | — |
| [SRC-1A176AD4F0-L000352](../../tests/test_hosted_smoke.py#L352) | 352 | `"    assert failure.value.report[\"checks\"][\"authentication\"] == \"passed\""` | — |
| [SRC-1A176AD4F0-L000353](../../tests/test_hosted_smoke.py#L353) | 353 | `"    assert failure.value.report[\"checks\"][\"provider_usage\"][\"status\"] == \"blocked_not_approved\""` | — |
| [SRC-1A176AD4F0-L000354](../../tests/test_hosted_smoke.py#L354) | 354 | `""` | — |
| [SRC-1A176AD4F0-L000355](../../tests/test_hosted_smoke.py#L355) | 355 | `""` | — |
| [SRC-1A176AD4F0-L000356](../../tests/test_hosted_smoke.py#L356) | 356 | `"def test_smoke_rejects_empty_agent_answer(hosted_server, monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000357](../../tests/test_hosted_smoke.py#L357) | 357 | `"    original = hosted_smoke_test.request_json"` | — |
| [SRC-1A176AD4F0-L000358](../../tests/test_hosted_smoke.py#L358) | 358 | `""` | — |
| [SRC-1A176AD4F0-L000359](../../tests/test_hosted_smoke.py#L359) | 359 | `"    def empty_answer(url: str, **kwargs):"` | — |
| [SRC-1A176AD4F0-L000360](../../tests/test_hosted_smoke.py#L360) | 360 | `"        if urlsplit(url).path == \"/api/agent\" and kwargs.get(\"token\") == TOKEN:"` | — |
| [SRC-1A176AD4F0-L000361](../../tests/test_hosted_smoke.py#L361) | 361 | `"            return 200, {"` | — |
| [SRC-1A176AD4F0-L000362](../../tests/test_hosted_smoke.py#L362) | 362 | `"                \"answer\": \"  \", \"used_web_search\": True, \"used_language_model\": True,"` | — |
| [SRC-1A176AD4F0-L000363](../../tests/test_hosted_smoke.py#L363) | 363 | `"                \"answer_evidence_status\": \"citation_indices_validated_only\","` | — |
| [SRC-1A176AD4F0-L000364](../../tests/test_hosted_smoke.py#L364) | 364 | `"                \"sources\": [{\"url\": \"https://example.com/source\"}],"` | — |
| [SRC-1A176AD4F0-L000365](../../tests/test_hosted_smoke.py#L365) | 365 | `"                \"search_report\": {"` | — |
| [SRC-1A176AD4F0-L000366](../../tests/test_hosted_smoke.py#L366) | 366 | `"                    \"pipeline_completion_status\": \"completed\","` | — |
| [SRC-1A176AD4F0-L000367](../../tests/test_hosted_smoke.py#L367) | 367 | `"                    \"semantic_claim_verification\": {\"status\": \"completed_all_claims_supported\"},"` | — |
| [SRC-1A176AD4F0-L000368](../../tests/test_hosted_smoke.py#L368) | 368 | `"                    \"insufficient_evidence\": False,"` | — |
| [SRC-1A176AD4F0-L000369](../../tests/test_hosted_smoke.py#L369) | 369 | `"                    \"claim_audit_semantics\": \"distinct_model_assessed_source_support_not_ground_truth\","` | — |
| [SRC-1A176AD4F0-L000370](../../tests/test_hosted_smoke.py#L370) | 370 | `"                },"` | — |
| [SRC-1A176AD4F0-L000371](../../tests/test_hosted_smoke.py#L371) | 371 | `"            }"` | — |
| [SRC-1A176AD4F0-L000372](../../tests/test_hosted_smoke.py#L372) | 372 | `"        return original(url, **kwargs)"` | — |
| [SRC-1A176AD4F0-L000373](../../tests/test_hosted_smoke.py#L373) | 373 | `""` | — |
| [SRC-1A176AD4F0-L000374](../../tests/test_hosted_smoke.py#L374) | 374 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", empty_answer)"` | — |
| [SRC-1A176AD4F0-L000375](../../tests/test_hosted_smoke.py#L375) | 375 | `"    with pytest.raises(SmokeError, match=\"empty or whitespace-only answer\"):"` | — |
| [SRC-1A176AD4F0-L000376](../../tests/test_hosted_smoke.py#L376) | 376 | `"        run_smoke(hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5)"` | — |
| [SRC-1A176AD4F0-L000377](../../tests/test_hosted_smoke.py#L377) | 377 | `""` | — |
| [SRC-1A176AD4F0-L000378](../../tests/test_hosted_smoke.py#L378) | 378 | `""` | — |
| [SRC-1A176AD4F0-L000379](../../tests/test_hosted_smoke.py#L379) | 379 | `""` | — |
| [SRC-1A176AD4F0-L000380](../../tests/test_hosted_smoke.py#L380) | 380 | `"def test_smoke_rejects_non_string_agent_answer(hosted_server, monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000381](../../tests/test_hosted_smoke.py#L381) | 381 | `"    original = hosted_smoke_test.request_json"` | — |
| [SRC-1A176AD4F0-L000382](../../tests/test_hosted_smoke.py#L382) | 382 | `""` | — |
| [SRC-1A176AD4F0-L000383](../../tests/test_hosted_smoke.py#L383) | 383 | `"    def non_string_answer(url: str, **kwargs):"` | — |
| [SRC-1A176AD4F0-L000384](../../tests/test_hosted_smoke.py#L384) | 384 | `"        if urlsplit(url).path == \"/api/agent\" and kwargs.get(\"token\") == TOKEN:"` | — |
| [SRC-1A176AD4F0-L000385](../../tests/test_hosted_smoke.py#L385) | 385 | `"            return 200, {"` | — |
| [SRC-1A176AD4F0-L000386](../../tests/test_hosted_smoke.py#L386) | 386 | `"                \"answer\": None, \"used_web_search\": True, \"used_language_model\": True,"` | — |
| [SRC-1A176AD4F0-L000387](../../tests/test_hosted_smoke.py#L387) | 387 | `"                \"answer_evidence_status\": \"citation_indices_validated_only\","` | — |
| [SRC-1A176AD4F0-L000388](../../tests/test_hosted_smoke.py#L388) | 388 | `"                \"sources\": [{\"url\": \"https://example.com/source\"}],"` | — |
| [SRC-1A176AD4F0-L000389](../../tests/test_hosted_smoke.py#L389) | 389 | `"                \"search_report\": {"` | — |
| [SRC-1A176AD4F0-L000390](../../tests/test_hosted_smoke.py#L390) | 390 | `"                    \"pipeline_completion_status\": \"completed\","` | — |
| [SRC-1A176AD4F0-L000391](../../tests/test_hosted_smoke.py#L391) | 391 | `"                    \"semantic_claim_verification\": {\"status\": \"completed_all_claims_supported\"},"` | — |
| [SRC-1A176AD4F0-L000392](../../tests/test_hosted_smoke.py#L392) | 392 | `"                    \"insufficient_evidence\": False,"` | — |
| [SRC-1A176AD4F0-L000393](../../tests/test_hosted_smoke.py#L393) | 393 | `"                    \"claim_audit_semantics\": \"distinct_model_assessed_source_support_not_ground_truth\","` | — |
| [SRC-1A176AD4F0-L000394](../../tests/test_hosted_smoke.py#L394) | 394 | `"                },"` | — |
| [SRC-1A176AD4F0-L000395](../../tests/test_hosted_smoke.py#L395) | 395 | `"            }"` | — |
| [SRC-1A176AD4F0-L000396](../../tests/test_hosted_smoke.py#L396) | 396 | `"        return original(url, **kwargs)"` | — |
| [SRC-1A176AD4F0-L000397](../../tests/test_hosted_smoke.py#L397) | 397 | `""` | — |
| [SRC-1A176AD4F0-L000398](../../tests/test_hosted_smoke.py#L398) | 398 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", non_string_answer)"` | — |
| [SRC-1A176AD4F0-L000399](../../tests/test_hosted_smoke.py#L399) | 399 | `"    with pytest.raises(SmokeError, match=\"empty or whitespace-only answer\"):"` | — |
| [SRC-1A176AD4F0-L000400](../../tests/test_hosted_smoke.py#L400) | 400 | `"        run_smoke(hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5)"` | — |
| [SRC-1A176AD4F0-L000401](../../tests/test_hosted_smoke.py#L401) | 401 | `""` | — |
| [SRC-1A176AD4F0-L000402](../../tests/test_hosted_smoke.py#L402) | 402 | `""` | — |
| [SRC-1A176AD4F0-L000403](../../tests/test_hosted_smoke.py#L403) | 403 | `"def test_smoke_rejects_partial_pipeline_even_with_sources(hosted_server, monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000404](../../tests/test_hosted_smoke.py#L404) | 404 | `"    original = hosted_smoke_test.request_json"` | — |
| [SRC-1A176AD4F0-L000405](../../tests/test_hosted_smoke.py#L405) | 405 | `""` | — |
| [SRC-1A176AD4F0-L000406](../../tests/test_hosted_smoke.py#L406) | 406 | `"    def partial_pipeline(url: str, **kwargs):"` | — |
| [SRC-1A176AD4F0-L000407](../../tests/test_hosted_smoke.py#L407) | 407 | `"        if urlsplit(url).path == \"/api/agent\" and kwargs.get(\"token\") == TOKEN:"` | — |
| [SRC-1A176AD4F0-L000408](../../tests/test_hosted_smoke.py#L408) | 408 | `"            return 200, {"` | — |
| [SRC-1A176AD4F0-L000409](../../tests/test_hosted_smoke.py#L409) | 409 | `"                \"answer\": \"إجابة جزئية [المصدر 1]\", \"used_web_search\": True,"` | — |
| [SRC-1A176AD4F0-L000410](../../tests/test_hosted_smoke.py#L410) | 410 | `"                \"used_language_model\": True,"` | — |
| [SRC-1A176AD4F0-L000411](../../tests/test_hosted_smoke.py#L411) | 411 | `"                \"answer_evidence_status\": \"citation_indices_validated_only\","` | — |
| [SRC-1A176AD4F0-L000412](../../tests/test_hosted_smoke.py#L412) | 412 | `"                \"sources\": [{\"url\": \"https://example.com/source\"}],"` | — |
| [SRC-1A176AD4F0-L000413](../../tests/test_hosted_smoke.py#L413) | 413 | `"                \"request_budget\": {\"profile\": \"hosted_smoke\", \"timeout_seconds\": 75, \"budget_exhausted\": False, \"deadline_exceeded\": False, \"limits\": {\"search_queries\": 3, \"search_calls\": 12, \"model_calls\": 6, \"page_fetches\": 4, \"tool_calls\": 0}, \"counts\": {\"search_queries\": 2, \"search_calls\": 4, \"model_calls\": 4, \"page_fetches\": 1, \"tool_calls\": 0}},"` | — |
| [SRC-1A176AD4F0-L000414](../../tests/test_hosted_smoke.py#L414) | 414 | `"                \"search_report\": {"` | — |
| [SRC-1A176AD4F0-L000415](../../tests/test_hosted_smoke.py#L415) | 415 | `"                    \"pipeline_completion_status\": \"partial\","` | — |
| [SRC-1A176AD4F0-L000416](../../tests/test_hosted_smoke.py#L416) | 416 | `"                    \"semantic_claim_verification\": {\"status\": \"completed_all_claims_supported\"},"` | — |
| [SRC-1A176AD4F0-L000417](../../tests/test_hosted_smoke.py#L417) | 417 | `"                    \"insufficient_evidence\": False,"` | — |
| [SRC-1A176AD4F0-L000418](../../tests/test_hosted_smoke.py#L418) | 418 | `"                    \"claim_audit_semantics\": \"distinct_model_assessed_source_support_not_ground_truth\","` | — |
| [SRC-1A176AD4F0-L000419](../../tests/test_hosted_smoke.py#L419) | 419 | `"                },"` | — |
| [SRC-1A176AD4F0-L000420](../../tests/test_hosted_smoke.py#L420) | 420 | `"            }"` | — |
| [SRC-1A176AD4F0-L000421](../../tests/test_hosted_smoke.py#L421) | 421 | `"        return original(url, **kwargs)"` | — |
| [SRC-1A176AD4F0-L000422](../../tests/test_hosted_smoke.py#L422) | 422 | `""` | — |
| [SRC-1A176AD4F0-L000423](../../tests/test_hosted_smoke.py#L423) | 423 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", partial_pipeline)"` | — |
| [SRC-1A176AD4F0-L000424](../../tests/test_hosted_smoke.py#L424) | 424 | `"    with pytest.raises(SmokeError, match=\"pipeline did not complete\"):"` | — |
| [SRC-1A176AD4F0-L000425](../../tests/test_hosted_smoke.py#L425) | 425 | `"        run_smoke(hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5)"` | — |
| [SRC-1A176AD4F0-L000426](../../tests/test_hosted_smoke.py#L426) | 426 | `""` | — |
| [SRC-1A176AD4F0-L000427](../../tests/test_hosted_smoke.py#L427) | 427 | `""` | — |
| [SRC-1A176AD4F0-L000428](../../tests/test_hosted_smoke.py#L428) | 428 | `"def test_smoke_rejects_unvalidated_answer_evidence(hosted_server, monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000429](../../tests/test_hosted_smoke.py#L429) | 429 | `"    original = hosted_smoke_test.request_json"` | — |
| [SRC-1A176AD4F0-L000430](../../tests/test_hosted_smoke.py#L430) | 430 | `""` | — |
| [SRC-1A176AD4F0-L000431](../../tests/test_hosted_smoke.py#L431) | 431 | `"    def invalid_evidence(url: str, **kwargs):"` | — |
| [SRC-1A176AD4F0-L000432](../../tests/test_hosted_smoke.py#L432) | 432 | `"        if urlsplit(url).path == \"/api/agent\" and kwargs.get(\"token\") == TOKEN:"` | — |
| [SRC-1A176AD4F0-L000433](../../tests/test_hosted_smoke.py#L433) | 433 | `"            return 200, {"` | — |
| [SRC-1A176AD4F0-L000434](../../tests/test_hosted_smoke.py#L434) | 434 | `"                \"answer\": \"إجابة بلا إحالات صالحة\", \"used_web_search\": True,"` | — |
| [SRC-1A176AD4F0-L000435](../../tests/test_hosted_smoke.py#L435) | 435 | `"                \"used_language_model\": True, \"answer_evidence_status\": \"not_assessed\","` | — |
| [SRC-1A176AD4F0-L000436](../../tests/test_hosted_smoke.py#L436) | 436 | `"                \"sources\": [{\"url\": \"https://example.com/source\"}],"` | — |
| [SRC-1A176AD4F0-L000437](../../tests/test_hosted_smoke.py#L437) | 437 | `"                \"request_budget\": {\"profile\": \"hosted_smoke\", \"timeout_seconds\": 75, \"budget_exhausted\": False, \"deadline_exceeded\": False, \"limits\": {\"search_queries\": 3, \"search_calls\": 12, \"model_calls\": 6, \"page_fetches\": 4, \"tool_calls\": 0}, \"counts\": {\"search_queries\": 2, \"search_calls\": 4, \"model_calls\": 4, \"page_fetches\": 1, \"tool_calls\": 0}},"` | — |
| [SRC-1A176AD4F0-L000438](../../tests/test_hosted_smoke.py#L438) | 438 | `"                \"search_report\": {"` | — |
| [SRC-1A176AD4F0-L000439](../../tests/test_hosted_smoke.py#L439) | 439 | `"                    \"pipeline_completion_status\": \"completed\","` | — |
| [SRC-1A176AD4F0-L000440](../../tests/test_hosted_smoke.py#L440) | 440 | `"                    \"semantic_claim_verification\": {\"status\": \"completed_all_claims_supported\"},"` | — |
| [SRC-1A176AD4F0-L000441](../../tests/test_hosted_smoke.py#L441) | 441 | `"                    \"insufficient_evidence\": False,"` | — |
| [SRC-1A176AD4F0-L000442](../../tests/test_hosted_smoke.py#L442) | 442 | `"                    \"claim_audit_semantics\": \"distinct_model_assessed_source_support_not_ground_truth\","` | — |
| [SRC-1A176AD4F0-L000443](../../tests/test_hosted_smoke.py#L443) | 443 | `"                },"` | — |
| [SRC-1A176AD4F0-L000444](../../tests/test_hosted_smoke.py#L444) | 444 | `"            }"` | — |
| [SRC-1A176AD4F0-L000445](../../tests/test_hosted_smoke.py#L445) | 445 | `"        return original(url, **kwargs)"` | — |
| [SRC-1A176AD4F0-L000446](../../tests/test_hosted_smoke.py#L446) | 446 | `""` | — |
| [SRC-1A176AD4F0-L000447](../../tests/test_hosted_smoke.py#L447) | 447 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", invalid_evidence)"` | — |
| [SRC-1A176AD4F0-L000448](../../tests/test_hosted_smoke.py#L448) | 448 | `"    with pytest.raises(SmokeError, match=\"evidence status\"):"` | — |
| [SRC-1A176AD4F0-L000449](../../tests/test_hosted_smoke.py#L449) | 449 | `"        run_smoke(hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5)"` | — |
| [SRC-1A176AD4F0-L000450](../../tests/test_hosted_smoke.py#L450) | 450 | `""` | — |
| [SRC-1A176AD4F0-L000451](../../tests/test_hosted_smoke.py#L451) | 451 | `""` | — |
| [SRC-1A176AD4F0-L000452](../../tests/test_hosted_smoke.py#L452) | 452 | `""` | — |
| [SRC-1A176AD4F0-L000453](../../tests/test_hosted_smoke.py#L453) | 453 | `""` | — |
| [SRC-1A176AD4F0-L000454](../../tests/test_hosted_smoke.py#L454) | 454 | `"def test_smoke_rejects_missing_or_exceeded_server_budget_profile(hosted_server, monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000455](../../tests/test_hosted_smoke.py#L455) | 455 | `"    original = hosted_smoke_test.request_json"` | — |
| [SRC-1A176AD4F0-L000456](../../tests/test_hosted_smoke.py#L456) | 456 | `""` | — |
| [SRC-1A176AD4F0-L000457](../../tests/test_hosted_smoke.py#L457) | 457 | `"    def unbounded_budget(url: str, **kwargs):"` | — |
| [SRC-1A176AD4F0-L000458](../../tests/test_hosted_smoke.py#L458) | 458 | `"        if urlsplit(url).path == \"/api/agent\" and kwargs.get(\"token\") == TOKEN:"` | — |
| [SRC-1A176AD4F0-L000459](../../tests/test_hosted_smoke.py#L459) | 459 | `"            status, payload = original(url, **kwargs)"` | — |
| [SRC-1A176AD4F0-L000460](../../tests/test_hosted_smoke.py#L460) | 460 | `"            payload[\"request_budget\"] = {"` | — |
| [SRC-1A176AD4F0-L000461](../../tests/test_hosted_smoke.py#L461) | 461 | `"                \"profile\": \"default\","` | — |
| [SRC-1A176AD4F0-L000462](../../tests/test_hosted_smoke.py#L462) | 462 | `"                \"budget_exhausted\": False,"` | — |
| [SRC-1A176AD4F0-L000463](../../tests/test_hosted_smoke.py#L463) | 463 | `"                \"deadline_exceeded\": False,"` | — |
| [SRC-1A176AD4F0-L000464](../../tests/test_hosted_smoke.py#L464) | 464 | `"                \"limits\": {\"search_queries\": 8, \"search_calls\": 32, \"model_calls\": 8, \"page_fetches\": 8, \"tool_calls\": 3},"` | — |
| [SRC-1A176AD4F0-L000465](../../tests/test_hosted_smoke.py#L465) | 465 | `"                \"counts\": {\"search_queries\": 1, \"search_calls\": 2, \"model_calls\": 2, \"page_fetches\": 1, \"tool_calls\": 0},"` | — |
| [SRC-1A176AD4F0-L000466](../../tests/test_hosted_smoke.py#L466) | 466 | `"            }"` | — |
| [SRC-1A176AD4F0-L000467](../../tests/test_hosted_smoke.py#L467) | 467 | `"            return status, payload"` | — |
| [SRC-1A176AD4F0-L000468](../../tests/test_hosted_smoke.py#L468) | 468 | `"        return original(url, **kwargs)"` | — |
| [SRC-1A176AD4F0-L000469](../../tests/test_hosted_smoke.py#L469) | 469 | `""` | — |
| [SRC-1A176AD4F0-L000470](../../tests/test_hosted_smoke.py#L470) | 470 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", unbounded_budget)"` | — |
| [SRC-1A176AD4F0-L000471](../../tests/test_hosted_smoke.py#L471) | 471 | `"    with pytest.raises(SmokeError, match=\"hosted_smoke request budget\"):"` | — |
| [SRC-1A176AD4F0-L000472](../../tests/test_hosted_smoke.py#L472) | 472 | `"        run_smoke(hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5)"` | — |
| [SRC-1A176AD4F0-L000473](../../tests/test_hosted_smoke.py#L473) | 473 | `""` | — |
| [SRC-1A176AD4F0-L000474](../../tests/test_hosted_smoke.py#L474) | 474 | `""` | — |
| [SRC-1A176AD4F0-L000475](../../tests/test_hosted_smoke.py#L475) | 475 | `""` | — |
| [SRC-1A176AD4F0-L000476](../../tests/test_hosted_smoke.py#L476) | 476 | `"def test_smoke_rejects_pipeline_complete_without_semantic_claim_support(hosted_server, monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000477](../../tests/test_hosted_smoke.py#L477) | 477 | `"    original = hosted_smoke_test.request_json"` | — |
| [SRC-1A176AD4F0-L000478](../../tests/test_hosted_smoke.py#L478) | 478 | `""` | — |
| [SRC-1A176AD4F0-L000479](../../tests/test_hosted_smoke.py#L479) | 479 | `"    def unverified_claims(url: str, **kwargs):"` | — |
| [SRC-1A176AD4F0-L000480](../../tests/test_hosted_smoke.py#L480) | 480 | `"        if urlsplit(url).path == \"/api/agent\" and kwargs.get(\"token\") == TOKEN:"` | — |
| [SRC-1A176AD4F0-L000481](../../tests/test_hosted_smoke.py#L481) | 481 | `"            return 200, {"` | — |
| [SRC-1A176AD4F0-L000482](../../tests/test_hosted_smoke.py#L482) | 482 | `"                \"answer\": \"ادعاء غير متحقق [المصدر 1]\", \"used_web_search\": True,"` | — |
| [SRC-1A176AD4F0-L000483](../../tests/test_hosted_smoke.py#L483) | 483 | `"                \"used_language_model\": True,"` | — |
| [SRC-1A176AD4F0-L000484](../../tests/test_hosted_smoke.py#L484) | 484 | `"                \"answer_evidence_status\": \"citation_indices_validated_only\","` | — |
| [SRC-1A176AD4F0-L000485](../../tests/test_hosted_smoke.py#L485) | 485 | `"                \"sources\": [{\"url\": \"https://example.com/source\"}],"` | — |
| [SRC-1A176AD4F0-L000486](../../tests/test_hosted_smoke.py#L486) | 486 | `"                \"request_budget\": {\"profile\": \"hosted_smoke\", \"timeout_seconds\": 75, \"budget_exhausted\": False, \"deadline_exceeded\": False, \"limits\": {\"search_queries\": 3, \"search_calls\": 12, \"model_calls\": 6, \"page_fetches\": 4, \"tool_calls\": 0}, \"counts\": {\"search_queries\": 2, \"search_calls\": 4, \"model_calls\": 4, \"page_fetches\": 1, \"tool_calls\": 0}},"` | — |
| [SRC-1A176AD4F0-L000487](../../tests/test_hosted_smoke.py#L487) | 487 | `"                \"search_report\": {"` | — |
| [SRC-1A176AD4F0-L000488](../../tests/test_hosted_smoke.py#L488) | 488 | `"                    \"pipeline_completion_status\": \"completed\","` | — |
| [SRC-1A176AD4F0-L000489](../../tests/test_hosted_smoke.py#L489) | 489 | `"                    \"semantic_claim_verification\": {\"status\": \"not_performed\"},"` | — |
| [SRC-1A176AD4F0-L000490](../../tests/test_hosted_smoke.py#L490) | 490 | `"                    \"insufficient_evidence\": False,"` | — |
| [SRC-1A176AD4F0-L000491](../../tests/test_hosted_smoke.py#L491) | 491 | `"                    \"claim_audit_semantics\": \"distinct_model_assessed_source_support_not_ground_truth\","` | — |
| [SRC-1A176AD4F0-L000492](../../tests/test_hosted_smoke.py#L492) | 492 | `"                },"` | — |
| [SRC-1A176AD4F0-L000493](../../tests/test_hosted_smoke.py#L493) | 493 | `"            }"` | — |
| [SRC-1A176AD4F0-L000494](../../tests/test_hosted_smoke.py#L494) | 494 | `"        return original(url, **kwargs)"` | — |
| [SRC-1A176AD4F0-L000495](../../tests/test_hosted_smoke.py#L495) | 495 | `""` | — |
| [SRC-1A176AD4F0-L000496](../../tests/test_hosted_smoke.py#L496) | 496 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", unverified_claims)"` | — |
| [SRC-1A176AD4F0-L000497](../../tests/test_hosted_smoke.py#L497) | 497 | `"    with pytest.raises(SmokeError, match=\"semantic claim-support review\"):"` | — |
| [SRC-1A176AD4F0-L000498](../../tests/test_hosted_smoke.py#L498) | 498 | `"        run_smoke(hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5)"` | — |
| [SRC-1A176AD4F0-L000499](../../tests/test_hosted_smoke.py#L499) | 499 | `""` | — |
| [SRC-1A176AD4F0-L000500](../../tests/test_hosted_smoke.py#L500) | 500 | `""` | — |
| [SRC-1A176AD4F0-L000501](../../tests/test_hosted_smoke.py#L501) | 501 | `"def test_hosted_smoke_workflow_scopes_secrets_to_the_execution_step():"` | — |
| [SRC-1A176AD4F0-L000502](../../tests/test_hosted_smoke.py#L502) | 502 | `"    workflow = Path(\".github/workflows/hosted-smoke.yml\").read_text(encoding=\"utf-8\")"` | — |
| [SRC-1A176AD4F0-L000503](../../tests/test_hosted_smoke.py#L503) | 503 | `"    job = workflow.split(\"jobs:\", 1)[1].split(\"steps:\", 1)[0]"` | — |
| [SRC-1A176AD4F0-L000504](../../tests/test_hosted_smoke.py#L504) | 504 | `"    assert \"OMARAI_ACCESS_TOKEN\" not in job"` | — |
| [SRC-1A176AD4F0-L000505](../../tests/test_hosted_smoke.py#L505) | 505 | `"    assert \"OMARAI_BASE_URL\" not in job"` | — |
| [SRC-1A176AD4F0-L000506](../../tests/test_hosted_smoke.py#L506) | 506 | `"    assert \"OMARAI_ACCESS_TOKEN:\" in workflow"` | — |
| [SRC-1A176AD4F0-L000507](../../tests/test_hosted_smoke.py#L507) | 507 | `"    assert \"OMARAI_BASE_URL:\" in workflow"` | — |
| [SRC-1A176AD4F0-L000508](../../tests/test_hosted_smoke.py#L508) | 508 | `"    preflight_step = workflow.split(\"- name: Run no-cost hosted preflight\", 1)[1].split("` | — |
| [SRC-1A176AD4F0-L000509](../../tests/test_hosted_smoke.py#L509) | 509 | `"        \"- name: Run live hosted acceptance\", 1"` | — |
| [SRC-1A176AD4F0-L000510](../../tests/test_hosted_smoke.py#L510) | 510 | `"    )[0]"` | — |
| [SRC-1A176AD4F0-L000511](../../tests/test_hosted_smoke.py#L511) | 511 | `"    live_step = workflow.split(\"- name: Run live hosted acceptance\", 1)[1].split("` | — |
| [SRC-1A176AD4F0-L000512](../../tests/test_hosted_smoke.py#L512) | 512 | `"        \"- name: Upload hosted question-and-answer transcript\", 1"` | — |
| [SRC-1A176AD4F0-L000513](../../tests/test_hosted_smoke.py#L513) | 513 | `"    )[0]"` | — |
| [SRC-1A176AD4F0-L000514](../../tests/test_hosted_smoke.py#L514) | 514 | `"    assert \"OMARAI_ACCESS_TOKEN\" not in preflight_step"` | — |
| [SRC-1A176AD4F0-L000515](../../tests/test_hosted_smoke.py#L515) | 515 | `"    assert \"OMARAI_ACCESS_TOKEN:\" in live_step"` | — |
| [SRC-1A176AD4F0-L000516](../../tests/test_hosted_smoke.py#L516) | 516 | `"    assert \"preflight-only\" in workflow"` | — |
| [SRC-1A176AD4F0-L000517](../../tests/test_hosted_smoke.py#L517) | 517 | `"    assert \"default: false\" in workflow"` | — |
| [SRC-1A176AD4F0-L000518](../../tests/test_hosted_smoke.py#L518) | 518 | `""` | — |
| [SRC-1A176AD4F0-L000519](../../tests/test_hosted_smoke.py#L519) | 519 | `""` | — |
| [SRC-1A176AD4F0-L000520](../../tests/test_hosted_smoke.py#L520) | 520 | `"def test_hosted_smoke_workflow_is_manual_and_cost_gated():"` | — |
| [SRC-1A176AD4F0-L000521](../../tests/test_hosted_smoke.py#L521) | 521 | `"    workflow = Path(\".github/workflows/hosted-smoke.yml\").read_text(encoding=\"utf-8\")"` | — |
| [SRC-1A176AD4F0-L000522](../../tests/test_hosted_smoke.py#L522) | 522 | `"    assert \"schedule:\" not in workflow"` | — |
| [SRC-1A176AD4F0-L000523](../../tests/test_hosted_smoke.py#L523) | 523 | `"    assert \"allow_provider_usage:\" in workflow"` | — |
| [SRC-1A176AD4F0-L000524](../../tests/test_hosted_smoke.py#L524) | 524 | `"    assert \"default: false\" in workflow"` | — |
| [SRC-1A176AD4F0-L000525](../../tests/test_hosted_smoke.py#L525) | 525 | `"    assert \"--allow-provider-usage\" in workflow"` | — |
| [SRC-1A176AD4F0-L000526](../../tests/test_hosted_smoke.py#L526) | 526 | `""` | — |
| [SRC-1A176AD4F0-L000527](../../tests/test_hosted_smoke.py#L527) | 527 | `""` | — |
| [SRC-1A176AD4F0-L000528](../../tests/test_hosted_smoke.py#L528) | 528 | `"def test_hosted_smoke_budget_caps_match_server_enforced_profile():"` | — |
| [SRC-1A176AD4F0-L000529](../../tests/test_hosted_smoke.py#L529) | 529 | `"    from agents.request_budget import HOSTED_SMOKE_BUDGET_LIMITS"` | — |
| [SRC-1A176AD4F0-L000530](../../tests/test_hosted_smoke.py#L530) | 530 | `""` | — |
| [SRC-1A176AD4F0-L000531](../../tests/test_hosted_smoke.py#L531) | 531 | `"    assert hosted_smoke_test.HOSTED_SMOKE_BUDGET_MAX == HOSTED_SMOKE_BUDGET_LIMITS"` | — |
## اختبارات

### FILE-1BB2FDD5B7 — [tests/test_hosted_smoke_transcript.py](../../tests/test_hosted_smoke_transcript.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1BB2FDD5B7-L000001](../../tests/test_hosted_smoke_transcript.py#L1) | 1 | `"\"\"\"Tests for the hosted acceptance transcript contract.\"\"\""` | — |
| [SRC-1BB2FDD5B7-L000002](../../tests/test_hosted_smoke_transcript.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-1BB2FDD5B7-L000003](../../tests/test_hosted_smoke_transcript.py#L3) | 3 | `""` | — |
| [SRC-1BB2FDD5B7-L000004](../../tests/test_hosted_smoke_transcript.py#L4) | 4 | `"from scripts import hosted_smoke_test"` | — |
| [SRC-1BB2FDD5B7-L000005](../../tests/test_hosted_smoke_transcript.py#L5) | 5 | `""` | — |
| [SRC-1BB2FDD5B7-L000006](../../tests/test_hosted_smoke_transcript.py#L6) | 6 | `""` | — |
| [SRC-1BB2FDD5B7-L000007](../../tests/test_hosted_smoke_transcript.py#L7) | 7 | `"def test_hosted_smoke_returns_exact_question_answer_and_sources(monkeypatch):"` | — |
| [SRC-1BB2FDD5B7-L000008](../../tests/test_hosted_smoke_transcript.py#L8) | 8 | `"    calls = []"` | — |
| [SRC-1BB2FDD5B7-L000009](../../tests/test_hosted_smoke_transcript.py#L9) | 9 | `""` | — |
| [SRC-1BB2FDD5B7-L000010](../../tests/test_hosted_smoke_transcript.py#L10) | 10 | `"    def fake_request_json(url, *, token=\"\", payload=None, timeout=90):"` | — |
| [SRC-1BB2FDD5B7-L000011](../../tests/test_hosted_smoke_transcript.py#L11) | 11 | `"        calls.append((url, token, payload))"` | — |
| [SRC-1BB2FDD5B7-L000012](../../tests/test_hosted_smoke_transcript.py#L12) | 12 | `"        if url.endswith(\"/api/health\"):"` | — |
| [SRC-1BB2FDD5B7-L000013](../../tests/test_hosted_smoke_transcript.py#L13) | 13 | `"            return 200, {\"ok\": True, \"build\": {\"sha\": \"a\" * 40}}"` | — |
| [SRC-1BB2FDD5B7-L000014](../../tests/test_hosted_smoke_transcript.py#L14) | 14 | `"        if url.endswith(\"/api/agent\") and not token:"` | — |
| [SRC-1BB2FDD5B7-L000015](../../tests/test_hosted_smoke_transcript.py#L15) | 15 | `"            return 401, None"` | — |
| [SRC-1BB2FDD5B7-L000016](../../tests/test_hosted_smoke_transcript.py#L16) | 16 | `"        if url.endswith(\"/api/diagnostics\"):"` | — |
| [SRC-1BB2FDD5B7-L000017](../../tests/test_hosted_smoke_transcript.py#L17) | 17 | `"            return 200, {"` | — |
| [SRC-1BB2FDD5B7-L000018](../../tests/test_hosted_smoke_transcript.py#L18) | 18 | `"                \"checks\": {"` | — |
| [SRC-1BB2FDD5B7-L000019](../../tests/test_hosted_smoke_transcript.py#L19) | 19 | `"                    \"web_search\": {"` | — |
| [SRC-1BB2FDD5B7-L000020](../../tests/test_hosted_smoke_transcript.py#L20) | 20 | `"                        \"status\": \"passed\","` | — |
| [SRC-1BB2FDD5B7-L000021](../../tests/test_hosted_smoke_transcript.py#L21) | 21 | `"                        \"result_count\": 2,"` | — |
| [SRC-1BB2FDD5B7-L000022](../../tests/test_hosted_smoke_transcript.py#L22) | 22 | `"                        \"provider_counts\": {\"bing_rss\": 2},"` | — |
| [SRC-1BB2FDD5B7-L000023](../../tests/test_hosted_smoke_transcript.py#L23) | 23 | `"                    },"` | — |
| [SRC-1BB2FDD5B7-L000024](../../tests/test_hosted_smoke_transcript.py#L24) | 24 | `"                    \"language_model\": {\"status\": \"passed\"},"` | — |
| [SRC-1BB2FDD5B7-L000025](../../tests/test_hosted_smoke_transcript.py#L25) | 25 | `"                },"` | — |
| [SRC-1BB2FDD5B7-L000026](../../tests/test_hosted_smoke_transcript.py#L26) | 26 | `"                \"provider_diagnostics\": ["` | — |
| [SRC-1BB2FDD5B7-L000027](../../tests/test_hosted_smoke_transcript.py#L27) | 27 | `"                    {\"provider\": \"bing_rss\", \"status\": \"ok\", \"accepted_count\": 2}"` | — |
| [SRC-1BB2FDD5B7-L000028](../../tests/test_hosted_smoke_transcript.py#L28) | 28 | `"                ],"` | — |
| [SRC-1BB2FDD5B7-L000029](../../tests/test_hosted_smoke_transcript.py#L29) | 29 | `"                \"configuration\": {"` | — |
| [SRC-1BB2FDD5B7-L000030](../../tests/test_hosted_smoke_transcript.py#L30) | 30 | `"                    \"brave_search_api_configured\": False,"` | — |
| [SRC-1BB2FDD5B7-L000031](../../tests/test_hosted_smoke_transcript.py#L31) | 31 | `"                    \"tavily_search_api_configured\": False,"` | — |
| [SRC-1BB2FDD5B7-L000032](../../tests/test_hosted_smoke_transcript.py#L32) | 32 | `"                    \"deepseek_search_api_configured\": False,"` | — |
| [SRC-1BB2FDD5B7-L000033](../../tests/test_hosted_smoke_transcript.py#L33) | 33 | `"                },"` | — |
| [SRC-1BB2FDD5B7-L000034](../../tests/test_hosted_smoke_transcript.py#L34) | 34 | `"                \"warnings\": [],"` | — |
| [SRC-1BB2FDD5B7-L000035](../../tests/test_hosted_smoke_transcript.py#L35) | 35 | `"            }"` | — |
| [SRC-1BB2FDD5B7-L000036](../../tests/test_hosted_smoke_transcript.py#L36) | 36 | `"        if url.endswith(\"/api/agent\") and token:"` | — |
| [SRC-1BB2FDD5B7-L000037](../../tests/test_hosted_smoke_transcript.py#L37) | 37 | `"            return 200, {"` | — |
| [SRC-1BB2FDD5B7-L000038](../../tests/test_hosted_smoke_transcript.py#L38) | 38 | `"                \"answer\": \"وجدت إشارة منشورة تطلب عرض سعر لنظام إنذار الحريق.\","` | — |
| [SRC-1BB2FDD5B7-L000039](../../tests/test_hosted_smoke_transcript.py#L39) | 39 | `"                \"used_web_search\": True,"` | — |
| [SRC-1BB2FDD5B7-L000040](../../tests/test_hosted_smoke_transcript.py#L40) | 40 | `"                \"used_language_model\": True,"` | — |
| [SRC-1BB2FDD5B7-L000041](../../tests/test_hosted_smoke_transcript.py#L41) | 41 | `"                \"answer_evidence_status\": \"citation_indices_validated_only\","` | — |
| [SRC-1BB2FDD5B7-L000042](../../tests/test_hosted_smoke_transcript.py#L42) | 42 | `"                \"sources\": ["` | — |
| [SRC-1BB2FDD5B7-L000043](../../tests/test_hosted_smoke_transcript.py#L43) | 43 | `"                    {"` | — |
| [SRC-1BB2FDD5B7-L000044](../../tests/test_hosted_smoke_transcript.py#L44) | 44 | `"                        \"title\": \"Fire alarm tender notice\","` | — |
| [SRC-1BB2FDD5B7-L000045](../../tests/test_hosted_smoke_transcript.py#L45) | 45 | `"                        \"url\": \"https://example.test/fire-alarm-tender\","` | — |
| [SRC-1BB2FDD5B7-L000046](../../tests/test_hosted_smoke_transcript.py#L46) | 46 | `"                        \"provider\": \"bing_rss\","` | — |
| [SRC-1BB2FDD5B7-L000047](../../tests/test_hosted_smoke_transcript.py#L47) | 47 | `"                        \"snippet\": \"طلب عرض سعر لنظام إنذار الحريق.\","` | — |
| [SRC-1BB2FDD5B7-L000048](../../tests/test_hosted_smoke_transcript.py#L48) | 48 | `"                        \"published_at\": \"\","` | — |
| [SRC-1BB2FDD5B7-L000049](../../tests/test_hosted_smoke_transcript.py#L49) | 49 | `"                    }"` | — |
| [SRC-1BB2FDD5B7-L000050](../../tests/test_hosted_smoke_transcript.py#L50) | 50 | `"                ],"` | — |
| [SRC-1BB2FDD5B7-L000051](../../tests/test_hosted_smoke_transcript.py#L51) | 51 | `"                \"request_budget\": {\"profile\": \"hosted_smoke\", \"timeout_seconds\": 75, \"budget_exhausted\": False, \"deadline_exceeded\": False, \"limits\": {\"search_queries\": 3, \"search_calls\": 12, \"model_calls\": 6, \"page_fetches\": 4, \"tool_calls\": 0}, \"counts\": {\"search_queries\": 2, \"search_calls\": 4, \"model_calls\": 4, \"page_fetches\": 1, \"tool_calls\": 0}},"` | — |
| [SRC-1BB2FDD5B7-L000052](../../tests/test_hosted_smoke_transcript.py#L52) | 52 | `"                \"search_report\": {"` | — |
| [SRC-1BB2FDD5B7-L000053](../../tests/test_hosted_smoke_transcript.py#L53) | 53 | `"                    \"pages_fetched\": 1,"` | — |
| [SRC-1BB2FDD5B7-L000054](../../tests/test_hosted_smoke_transcript.py#L54) | 54 | `"                    \"providers_used\": [\"bing_rss\"],"` | — |
| [SRC-1BB2FDD5B7-L000055](../../tests/test_hosted_smoke_transcript.py#L55) | 55 | `"                    \"pipeline_completion_status\": \"completed\","` | — |
| [SRC-1BB2FDD5B7-L000056](../../tests/test_hosted_smoke_transcript.py#L56) | 56 | `"                    \"semantic_claim_verification\": {\"status\": \"completed_all_claims_supported\"},"` | — |
| [SRC-1BB2FDD5B7-L000057](../../tests/test_hosted_smoke_transcript.py#L57) | 57 | `"                    \"insufficient_evidence\": False,"` | — |
| [SRC-1BB2FDD5B7-L000058](../../tests/test_hosted_smoke_transcript.py#L58) | 58 | `"                    \"claim_audit_semantics\": \"distinct_model_assessed_source_support_not_ground_truth\","` | — |
| [SRC-1BB2FDD5B7-L000059](../../tests/test_hosted_smoke_transcript.py#L59) | 59 | `"                },"` | — |
| [SRC-1BB2FDD5B7-L000060](../../tests/test_hosted_smoke_transcript.py#L60) | 60 | `"            }"` | — |
| [SRC-1BB2FDD5B7-L000061](../../tests/test_hosted_smoke_transcript.py#L61) | 61 | `"        raise AssertionError(f\"unexpected request: {url}\")"` | — |
| [SRC-1BB2FDD5B7-L000062](../../tests/test_hosted_smoke_transcript.py#L62) | 62 | `""` | — |
| [SRC-1BB2FDD5B7-L000063](../../tests/test_hosted_smoke_transcript.py#L63) | 63 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", fake_request_json)"` | — |
| [SRC-1BB2FDD5B7-L000064](../../tests/test_hosted_smoke_transcript.py#L64) | 64 | `"    report = hosted_smoke_test.run_smoke("` | — |
| [SRC-1BB2FDD5B7-L000065](../../tests/test_hosted_smoke_transcript.py#L65) | 65 | `"        \"https://omarai.example\", \"T\" * 40, expected_sha=\"a\" * 40,"` | — |
| [SRC-1BB2FDD5B7-L000066](../../tests/test_hosted_smoke_transcript.py#L66) | 66 | `"        allow_provider_usage=True,"` | — |
| [SRC-1BB2FDD5B7-L000067](../../tests/test_hosted_smoke_transcript.py#L67) | 67 | `"    )"` | — |
| [SRC-1BB2FDD5B7-L000068](../../tests/test_hosted_smoke_transcript.py#L68) | 68 | `""` | — |
| [SRC-1BB2FDD5B7-L000069](../../tests/test_hosted_smoke_transcript.py#L69) | 69 | `"    transcript = report[\"transcript\"][0]"` | — |
| [SRC-1BB2FDD5B7-L000070](../../tests/test_hosted_smoke_transcript.py#L70) | 70 | `"    assert transcript[\"question\"] == hosted_smoke_test.LIVE_TEST_QUESTION"` | — |
| [SRC-1BB2FDD5B7-L000071](../../tests/test_hosted_smoke_transcript.py#L71) | 71 | `"    assert transcript[\"answer\"] == \"وجدت إشارة منشورة تطلب عرض سعر لنظام إنذار الحريق.\""` | — |
| [SRC-1BB2FDD5B7-L000072](../../tests/test_hosted_smoke_transcript.py#L72) | 72 | `"    assert transcript[\"sources\"][0][\"url\"] == \"https://example.test/fire-alarm-tender\""` | — |
| [SRC-1BB2FDD5B7-L000073](../../tests/test_hosted_smoke_transcript.py#L73) | 73 | `"    assert transcript[\"pipeline_completion_status\"] == \"completed\""` | — |
| [SRC-1BB2FDD5B7-L000074](../../tests/test_hosted_smoke_transcript.py#L74) | 74 | `"    assert transcript[\"request_budget\"][\"profile\"] == \"hosted_smoke\""` | — |
| [SRC-1BB2FDD5B7-L000075](../../tests/test_hosted_smoke_transcript.py#L75) | 75 | `"    assert report[\"checks\"][\"request_budget\"][\"limits\"][\"search_calls\"] <= 12"` | — |
| [SRC-1BB2FDD5B7-L000076](../../tests/test_hosted_smoke_transcript.py#L76) | 76 | `"    assert report[\"checks\"][\"search\"][\"providers_reported\"] == [\"bing_rss\"]"` | — |
| [SRC-1BB2FDD5B7-L000077](../../tests/test_hosted_smoke_transcript.py#L77) | 77 | `"    assert all(\"T\" * 40 not in str(item) for item in report.values())"` | — |
| [SRC-1BB2FDD5B7-L000078](../../tests/test_hosted_smoke_transcript.py#L78) | 78 | `"    assert len(calls) == 3"` | — |
| [SRC-1BB2FDD5B7-L000079](../../tests/test_hosted_smoke_transcript.py#L79) | 79 | `"    assert not any(call[0].endswith(\"/api/diagnostics\") for call in calls)"` | — |
| [SRC-1BB2FDD5B7-L000080](../../tests/test_hosted_smoke_transcript.py#L80) | 80 | `""` | — |
| [SRC-1BB2FDD5B7-L000081](../../tests/test_hosted_smoke_transcript.py#L81) | 81 | `""` | — |
| [SRC-1BB2FDD5B7-L000082](../../tests/test_hosted_smoke_transcript.py#L82) | 82 | `"def test_hosted_smoke_allows_no_token_only_for_loopback_dev(monkeypatch):"` | — |
| [SRC-1BB2FDD5B7-L000083](../../tests/test_hosted_smoke_transcript.py#L83) | 83 | `"    def fake_request_json(url, *, token=\"\", payload=None, timeout=90):"` | — |
| [SRC-1BB2FDD5B7-L000084](../../tests/test_hosted_smoke_transcript.py#L84) | 84 | `"        if url.endswith(\"/api/health\"):"` | — |
| [SRC-1BB2FDD5B7-L000085](../../tests/test_hosted_smoke_transcript.py#L85) | 85 | `"            return 200, {\"ok\": True, \"build\": {\"sha\": \"unknown\"}}"` | — |
| [SRC-1BB2FDD5B7-L000086](../../tests/test_hosted_smoke_transcript.py#L86) | 86 | `"        if url.endswith(\"/api/agent\"):"` | — |
| [SRC-1BB2FDD5B7-L000087](../../tests/test_hosted_smoke_transcript.py#L87) | 87 | `"            return 200, {"` | — |
| [SRC-1BB2FDD5B7-L000088](../../tests/test_hosted_smoke_transcript.py#L88) | 88 | `"                \"answer\": \"لا توجد إشارة شراء مؤكدة في المصادر التي تم فحصها.\","` | — |
| [SRC-1BB2FDD5B7-L000089](../../tests/test_hosted_smoke_transcript.py#L89) | 89 | `"                \"used_web_search\": True,"` | — |
| [SRC-1BB2FDD5B7-L000090](../../tests/test_hosted_smoke_transcript.py#L90) | 90 | `"                \"used_language_model\": True,"` | — |
| [SRC-1BB2FDD5B7-L000091](../../tests/test_hosted_smoke_transcript.py#L91) | 91 | `"                \"answer_evidence_status\": \"citation_indices_validated_only\","` | — |
| [SRC-1BB2FDD5B7-L000092](../../tests/test_hosted_smoke_transcript.py#L92) | 92 | `"                \"sources\": [{\"url\": \"https://example.test/egypt\"}],"` | — |
| [SRC-1BB2FDD5B7-L000093](../../tests/test_hosted_smoke_transcript.py#L93) | 93 | `"                \"request_budget\": {\"profile\": \"hosted_smoke\", \"timeout_seconds\": 75, \"budget_exhausted\": False, \"deadline_exceeded\": False, \"limits\": {\"search_queries\": 3, \"search_calls\": 12, \"model_calls\": 6, \"page_fetches\": 4, \"tool_calls\": 0}, \"counts\": {\"search_queries\": 1, \"search_calls\": 2, \"model_calls\": 3, \"page_fetches\": 1, \"tool_calls\": 0}},"` | — |
| [SRC-1BB2FDD5B7-L000094](../../tests/test_hosted_smoke_transcript.py#L94) | 94 | `"                \"search_report\": {"` | — |
| [SRC-1BB2FDD5B7-L000095](../../tests/test_hosted_smoke_transcript.py#L95) | 95 | `"                    \"pipeline_completion_status\": \"completed\","` | — |
| [SRC-1BB2FDD5B7-L000096](../../tests/test_hosted_smoke_transcript.py#L96) | 96 | `"                    \"semantic_claim_verification\": {\"status\": \"completed_no_factual_claims\"},"` | — |
| [SRC-1BB2FDD5B7-L000097](../../tests/test_hosted_smoke_transcript.py#L97) | 97 | `"                    \"insufficient_evidence\": False,"` | — |
| [SRC-1BB2FDD5B7-L000098](../../tests/test_hosted_smoke_transcript.py#L98) | 98 | `"                    \"claim_audit_semantics\": \"distinct_model_assessed_source_support_not_ground_truth\","` | — |
| [SRC-1BB2FDD5B7-L000099](../../tests/test_hosted_smoke_transcript.py#L99) | 99 | `"                },"` | — |
| [SRC-1BB2FDD5B7-L000100](../../tests/test_hosted_smoke_transcript.py#L100) | 100 | `"            }"` | — |
| [SRC-1BB2FDD5B7-L000101](../../tests/test_hosted_smoke_transcript.py#L101) | 101 | `"        raise AssertionError(url)"` | — |
| [SRC-1BB2FDD5B7-L000102](../../tests/test_hosted_smoke_transcript.py#L102) | 102 | `""` | — |
| [SRC-1BB2FDD5B7-L000103](../../tests/test_hosted_smoke_transcript.py#L103) | 103 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", fake_request_json)"` | — |
| [SRC-1BB2FDD5B7-L000104](../../tests/test_hosted_smoke_transcript.py#L104) | 104 | `"    report = hosted_smoke_test.run_smoke("` | — |
| [SRC-1BB2FDD5B7-L000105](../../tests/test_hosted_smoke_transcript.py#L105) | 105 | `"        \"http://127.0.0.1:8000\","` | — |
| [SRC-1BB2FDD5B7-L000106](../../tests/test_hosted_smoke_transcript.py#L106) | 106 | `"        \"\","` | — |
| [SRC-1BB2FDD5B7-L000107](../../tests/test_hosted_smoke_transcript.py#L107) | 107 | `"        local_dev_no_token=True,"` | — |
| [SRC-1BB2FDD5B7-L000108](../../tests/test_hosted_smoke_transcript.py#L108) | 108 | `"        allow_provider_usage=True,"` | — |
| [SRC-1BB2FDD5B7-L000109](../../tests/test_hosted_smoke_transcript.py#L109) | 109 | `"    )"` | — |
| [SRC-1BB2FDD5B7-L000110](../../tests/test_hosted_smoke_transcript.py#L110) | 110 | `"    assert report[\"auth_mode\"] == \"local_loopback_dev_bypass\""` | — |
| [SRC-1BB2FDD5B7-L000111](../../tests/test_hosted_smoke_transcript.py#L111) | 111 | `"    assert report[\"transcript\"][0][\"answer\"] == \"لا توجد إشارة شراء مؤكدة في المصادر التي تم فحصها.\""` | — |
| [SRC-1BB2FDD5B7-L000112](../../tests/test_hosted_smoke_transcript.py#L112) | 112 | `""` | — |
| [SRC-1BB2FDD5B7-L000113](../../tests/test_hosted_smoke_transcript.py#L113) | 113 | `""` | — |
| [SRC-1BB2FDD5B7-L000114](../../tests/test_hosted_smoke_transcript.py#L114) | 114 | `"def test_hosted_smoke_rejects_no_token_for_remote_host():"` | — |
| [SRC-1BB2FDD5B7-L000115](../../tests/test_hosted_smoke_transcript.py#L115) | 115 | `"    import pytest"` | — |
| [SRC-1BB2FDD5B7-L000116](../../tests/test_hosted_smoke_transcript.py#L116) | 116 | `""` | — |
| [SRC-1BB2FDD5B7-L000117](../../tests/test_hosted_smoke_transcript.py#L117) | 117 | `"    with pytest.raises(hosted_smoke_test.SmokeError, match=\"localhost/loopback\"):"` | — |
| [SRC-1BB2FDD5B7-L000118](../../tests/test_hosted_smoke_transcript.py#L118) | 118 | `"        hosted_smoke_test.run_smoke("` | — |
| [SRC-1BB2FDD5B7-L000119](../../tests/test_hosted_smoke_transcript.py#L119) | 119 | `"            \"https://omarai.example\","` | — |
| [SRC-1BB2FDD5B7-L000120](../../tests/test_hosted_smoke_transcript.py#L120) | 120 | `"            \"\","` | — |
| [SRC-1BB2FDD5B7-L000121](../../tests/test_hosted_smoke_transcript.py#L121) | 121 | `"            local_dev_no_token=True,"` | — |
| [SRC-1BB2FDD5B7-L000122](../../tests/test_hosted_smoke_transcript.py#L122) | 122 | `"        )"` | — |
## اختبارات

### FILE-EA6EC52573 — [tests/test_intent_router.py](../../tests/test_intent_router.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-EA6EC52573-L000001](../../tests/test_intent_router.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-EA6EC52573-L000002](../../tests/test_intent_router.py#L2) | 2 | `""` | — |
| [SRC-EA6EC52573-L000003](../../tests/test_intent_router.py#L3) | 3 | `"import pytest"` | — |
| [SRC-EA6EC52573-L000004](../../tests/test_intent_router.py#L4) | 4 | `""` | — |
| [SRC-EA6EC52573-L000005](../../tests/test_intent_router.py#L5) | 5 | `"from agents.intent_router import resolve_followup_query, route_intent"` | — |
| [SRC-EA6EC52573-L000006](../../tests/test_intent_router.py#L6) | 6 | `""` | — |
| [SRC-EA6EC52573-L000007](../../tests/test_intent_router.py#L7) | 7 | `""` | — |
| [SRC-EA6EC52573-L000008](../../tests/test_intent_router.py#L8) | 8 | `"@pytest.mark.parametrize("` | — |
| [SRC-EA6EC52573-L000009](../../tests/test_intent_router.py#L9) | 9 | `"    (\"question\", \"expected\"),"` | — |
| [SRC-EA6EC52573-L000010](../../tests/test_intent_router.py#L10) | 10 | `"    ["` | — |
| [SRC-EA6EC52573-L000011](../../tests/test_intent_router.py#L11) | 11 | `"        (\"ازيك؟ عامل ايه النهاردة؟\", \"LOCAL\"),"` | — |
| [SRC-EA6EC52573-L000012](../../tests/test_intent_router.py#L12) | 12 | `"        (\"Thanks, that helps.\", \"LOCAL\"),"` | — |
| [SRC-EA6EC52573-L000013](../../tests/test_intent_router.py#L13) | 13 | `"        (\"ما عاصمة مصر؟\", \"MODEL_ONLY\"),"` | — |
| [SRC-EA6EC52573-L000014](../../tests/test_intent_router.py#L14) | 14 | `"        (\"كام سعرها؟\", \"CLARIFY\"),"` | — |
| [SRC-EA6EC52573-L000015](../../tests/test_intent_router.py#L15) | 15 | `"        (\"قارنهم\", \"CLARIFY\"),"` | — |
| [SRC-EA6EC52573-L000016](../../tests/test_intent_router.py#L16) | 16 | `"        (\"ما سعر الهاتف اليوم في مصر؟\", \"WEB_SIMPLE\"),"` | — |
| [SRC-EA6EC52573-L000017](../../tests/test_intent_router.py#L17) | 17 | `"        ("` | — |
| [SRC-EA6EC52573-L000018](../../tests/test_intent_router.py#L18) | 18 | `"            \"قارن بين iPhone 17 وSamsung S26 من حيث السعر والبطارية والكاميرا\","` | — |
| [SRC-EA6EC52573-L000019](../../tests/test_intent_router.py#L19) | 19 | `"            \"WEB_DEEP\","` | — |
| [SRC-EA6EC52573-L000020](../../tests/test_intent_router.py#L20) | 20 | `"        ),"` | — |
| [SRC-EA6EC52573-L000021](../../tests/test_intent_router.py#L21) | 21 | `"    ],"` | — |
| [SRC-EA6EC52573-L000022](../../tests/test_intent_router.py#L22) | 22 | `")"` | — |
| [SRC-EA6EC52573-L000023](../../tests/test_intent_router.py#L23) | 23 | `"def test_deterministic_intent_routes(question: str, expected: str) -> None:"` | — |
| [SRC-EA6EC52573-L000024](../../tests/test_intent_router.py#L24) | 24 | `"    decision = route_intent(question)"` | — |
| [SRC-EA6EC52573-L000025](../../tests/test_intent_router.py#L25) | 25 | `"    assert decision[\"route\"] == expected"` | — |
| [SRC-EA6EC52573-L000026](../../tests/test_intent_router.py#L26) | 26 | `"    assert decision[\"reason\"]"` | — |
| [SRC-EA6EC52573-L000027](../../tests/test_intent_router.py#L27) | 27 | `""` | — |
| [SRC-EA6EC52573-L000028](../../tests/test_intent_router.py#L28) | 28 | `""` | — |
| [SRC-EA6EC52573-L000029](../../tests/test_intent_router.py#L29) | 29 | `"@pytest.mark.parametrize("` | — |
| [SRC-EA6EC52573-L000030](../../tests/test_intent_router.py#L30) | 30 | `"    (\"question\", \"expected\"),"` | — |
| [SRC-EA6EC52573-L000031](../../tests/test_intent_router.py#L31) | 31 | `"    ["` | — |
| [SRC-EA6EC52573-L000032](../../tests/test_intent_router.py#L32) | 32 | `"        (\"ابحث عن عميل يريد شراء شقة في العاصمة الإدارية بمصر\", \"LEAD_GENERATION\"),"` | — |
| [SRC-EA6EC52573-L000033](../../tests/test_intent_router.py#L33) | 33 | `"        (\"ابحث عن عميل يطلب او يريد شقة في التجمع الخامس\", \"LEAD_GENERATION\"),"` | — |
| [SRC-EA6EC52573-L000034](../../tests/test_intent_router.py#L34) | 34 | `"        (\"ابحث عن ١٠ عملاش يريدون شرا شقة في التجمع الخامس\", \"LEAD_GENERATION\"),"` | — |
| [SRC-EA6EC52573-L000035](../../tests/test_intent_router.py#L35) | 35 | `"        (\"ابحث عن شقق للبيع في العاصمة الإدارية\", \"WEB_SIMPLE\"),"` | — |
| [SRC-EA6EC52573-L000036](../../tests/test_intent_router.py#L36) | 36 | `"        (\"Find buyers looking to buy apartments in New Capital\", \"LEAD_GENERATION\"),"` | — |
| [SRC-EA6EC52573-L000037](../../tests/test_intent_router.py#L37) | 37 | `"        (\"لخص الصفحة https://example.com/article\", \"WEB_SIMPLE\"),"` | — |
| [SRC-EA6EC52573-L000038](../../tests/test_intent_router.py#L38) | 38 | `"        (\"Summarize this page https://example.com/article\", \"WEB_SIMPLE\"),"` | — |
| [SRC-EA6EC52573-L000039](../../tests/test_intent_router.py#L39) | 39 | `"        (\"لخص النص التالي: هذا نص تجريبي\", \"MODEL_ONLY\"),"` | — |
| [SRC-EA6EC52573-L000040](../../tests/test_intent_router.py#L40) | 40 | `"    ],"` | — |
| [SRC-EA6EC52573-L000041](../../tests/test_intent_router.py#L41) | 41 | `")"` | — |
| [SRC-EA6EC52573-L000042](../../tests/test_intent_router.py#L42) | 42 | `"def test_lead_generation_and_summarization_routes(question: str, expected: str) -> None:"` | — |
| [SRC-EA6EC52573-L000043](../../tests/test_intent_router.py#L43) | 43 | `"    decision = route_intent(question)"` | — |
| [SRC-EA6EC52573-L000044](../../tests/test_intent_router.py#L44) | 44 | `"    assert decision[\"route\"] == expected"` | — |
| [SRC-EA6EC52573-L000045](../../tests/test_intent_router.py#L45) | 45 | `"    assert decision[\"reason\"]"` | — |
| [SRC-EA6EC52573-L000046](../../tests/test_intent_router.py#L46) | 46 | `""` | — |
| [SRC-EA6EC52573-L000047](../../tests/test_intent_router.py#L47) | 47 | `""` | — |
| [SRC-EA6EC52573-L000048](../../tests/test_intent_router.py#L48) | 48 | `"def test_generic_explanation_of_lead_generation_is_not_a_lead_search() -> None:"` | — |
| [SRC-EA6EC52573-L000049](../../tests/test_intent_router.py#L49) | 49 | `"    assert route_intent(\"What is lead generation?\")[\"route\"] == \"MODEL_ONLY\""` | — |
| [SRC-EA6EC52573-L000050](../../tests/test_intent_router.py#L50) | 50 | `"    assert route_intent(\"Create a prospect list for apartment buyers\")[\"route\"] == \"LEAD_GENERATION\""` | — |
| [SRC-EA6EC52573-L000051](../../tests/test_intent_router.py#L51) | 51 | `""` | — |
| [SRC-EA6EC52573-L000052](../../tests/test_intent_router.py#L52) | 52 | `""` | — |
| [SRC-EA6EC52573-L000053](../../tests/test_intent_router.py#L53) | 53 | `""` | — |
| [SRC-EA6EC52573-L000054](../../tests/test_intent_router.py#L54) | 54 | `"def test_capability_question_is_local() -> None:"` | — |
| [SRC-EA6EC52573-L000055](../../tests/test_intent_router.py#L55) | 55 | `"    decision = route_intent("` | — |
| [SRC-EA6EC52573-L000056](../../tests/test_intent_router.py#L56) | 56 | `"        \"كيف تستطيع مساعدتي؟\","` | — |
| [SRC-EA6EC52573-L000057](../../tests/test_intent_router.py#L57) | 57 | `"        capability_question=True,"` | — |
| [SRC-EA6EC52573-L000058](../../tests/test_intent_router.py#L58) | 58 | `"        requires_web=False,"` | — |
| [SRC-EA6EC52573-L000059](../../tests/test_intent_router.py#L59) | 59 | `"    )"` | — |
| [SRC-EA6EC52573-L000060](../../tests/test_intent_router.py#L60) | 60 | `"    assert decision[\"route\"] == \"LOCAL\""` | — |
| [SRC-EA6EC52573-L000061](../../tests/test_intent_router.py#L61) | 61 | `"    assert decision[\"reason\"] == \"capability_question\""` | — |
| [SRC-EA6EC52573-L000062](../../tests/test_intent_router.py#L62) | 62 | `""` | — |
| [SRC-EA6EC52573-L000063](../../tests/test_intent_router.py#L63) | 63 | `""` | — |
| [SRC-EA6EC52573-L000064](../../tests/test_intent_router.py#L64) | 64 | `"def test_ambiguous_followup_uses_existing_conversation_context() -> None:"` | — |
| [SRC-EA6EC52573-L000065](../../tests/test_intent_router.py#L65) | 65 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000066](../../tests/test_intent_router.py#L66) | 66 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر iPhone 17 في مصر\"},"` | — |
| [SRC-EA6EC52573-L000067](../../tests/test_intent_router.py#L67) | 67 | `"        {\"role\": \"assistant\", \"content\": \"نتحدث عن هاتف iPhone 17 في السوق المصري.\"},"` | — |
| [SRC-EA6EC52573-L000068](../../tests/test_intent_router.py#L68) | 68 | `"    ]"` | — |
| [SRC-EA6EC52573-L000069](../../tests/test_intent_router.py#L69) | 69 | `"    decision = route_intent(\"كام سعرها؟\", history, requires_web=True)"` | — |
| [SRC-EA6EC52573-L000070](../../tests/test_intent_router.py#L70) | 70 | `"    assert decision[\"route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-EA6EC52573-L000071](../../tests/test_intent_router.py#L71) | 71 | `"    assert decision[\"context_available\"] is True"` | — |
| [SRC-EA6EC52573-L000072](../../tests/test_intent_router.py#L72) | 72 | `"    assert decision[\"needs_clarification\"] is False"` | — |
| [SRC-EA6EC52573-L000073](../../tests/test_intent_router.py#L73) | 73 | `""` | — |
| [SRC-EA6EC52573-L000074](../../tests/test_intent_router.py#L74) | 74 | `""` | — |
| [SRC-EA6EC52573-L000075](../../tests/test_intent_router.py#L75) | 75 | `"def test_comparison_followup_requires_context_before_deep_search() -> None:"` | — |
| [SRC-EA6EC52573-L000076](../../tests/test_intent_router.py#L76) | 76 | `"    assert route_intent(\"قارنهم\")[\"route\"] == \"CLARIFY\""` | — |
| [SRC-EA6EC52573-L000077](../../tests/test_intent_router.py#L77) | 77 | `"    history = [{\"role\": \"user\", \"content\": \"قارن iPhone 17 وSamsung S26\"}]"` | — |
| [SRC-EA6EC52573-L000078](../../tests/test_intent_router.py#L78) | 78 | `"    decision = route_intent(\"قارنهم\", history)"` | — |
| [SRC-EA6EC52573-L000079](../../tests/test_intent_router.py#L79) | 79 | `"    assert decision[\"route\"] == \"WEB_DEEP\""` | — |
| [SRC-EA6EC52573-L000080](../../tests/test_intent_router.py#L80) | 80 | `"    assert decision[\"context_available\"] is True"` | — |
| [SRC-EA6EC52573-L000081](../../tests/test_intent_router.py#L81) | 81 | `""` | — |
| [SRC-EA6EC52573-L000082](../../tests/test_intent_router.py#L82) | 82 | `""` | — |
| [SRC-EA6EC52573-L000083](../../tests/test_intent_router.py#L83) | 83 | `"def test_ambiguous_followup_does_not_reuse_stale_topic_after_acknowledgment() -> None:"` | — |
| [SRC-EA6EC52573-L000084](../../tests/test_intent_router.py#L84) | 84 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000085](../../tests/test_intent_router.py#L85) | 85 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر iPhone 17 في مصر\"},"` | — |
| [SRC-EA6EC52573-L000086](../../tests/test_intent_router.py#L86) | 86 | `"        {\"role\": \"assistant\", \"content\": \"سأساعدك في العثور على أسعار حديثة.\"},"` | — |
| [SRC-EA6EC52573-L000087](../../tests/test_intent_router.py#L87) | 87 | `"        {\"role\": \"user\", \"content\": \"شكرا\"},"` | — |
| [SRC-EA6EC52573-L000088](../../tests/test_intent_router.py#L88) | 88 | `"        {\"role\": \"assistant\", \"content\": \"العفو.\"},"` | — |
| [SRC-EA6EC52573-L000089](../../tests/test_intent_router.py#L89) | 89 | `"    ]"` | — |
| [SRC-EA6EC52573-L000090](../../tests/test_intent_router.py#L90) | 90 | `"    decision = route_intent(\"كام سعرها؟\", history, requires_web=True)"` | — |
| [SRC-EA6EC52573-L000091](../../tests/test_intent_router.py#L91) | 91 | `"    assert decision[\"route\"] == \"CLARIFY\""` | — |
| [SRC-EA6EC52573-L000092](../../tests/test_intent_router.py#L92) | 92 | `"    assert decision[\"context_available\"] is False"` | — |
| [SRC-EA6EC52573-L000093](../../tests/test_intent_router.py#L93) | 93 | `""` | — |
| [SRC-EA6EC52573-L000094](../../tests/test_intent_router.py#L94) | 94 | `""` | — |
| [SRC-EA6EC52573-L000095](../../tests/test_intent_router.py#L95) | 95 | `"def test_explicit_mode_overrides_conversational_shortcuts() -> None:"` | — |
| [SRC-EA6EC52573-L000096](../../tests/test_intent_router.py#L96) | 96 | `"    assert route_intent(\"ازيك؟\", mode=\"deep\")[\"route\"] == \"WEB_DEEP\""` | — |
| [SRC-EA6EC52573-L000097](../../tests/test_intent_router.py#L97) | 97 | `"    assert route_intent(\"ما سعر الهاتف؟\", mode=\"latest\")[\"route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-EA6EC52573-L000098](../../tests/test_intent_router.py#L98) | 98 | `""` | — |
| [SRC-EA6EC52573-L000099](../../tests/test_intent_router.py#L99) | 99 | `""` | — |
| [SRC-EA6EC52573-L000100](../../tests/test_intent_router.py#L100) | 100 | `"@pytest.mark.parametrize("` | — |
| [SRC-EA6EC52573-L000101](../../tests/test_intent_router.py#L101) | 101 | `"    (\"question\", \"expected_route\", \"expected_reason\"),"` | — |
| [SRC-EA6EC52573-L000102](../../tests/test_intent_router.py#L102) | 102 | `"    ["` | — |
| [SRC-EA6EC52573-L000103](../../tests/test_intent_router.py#L103) | 103 | `"        ("` | — |
| [SRC-EA6EC52573-L000104](../../tests/test_intent_router.py#L104) | 104 | `"            \"لخص الصفحة https://example.com/article\","` | — |
| [SRC-EA6EC52573-L000105](../../tests/test_intent_router.py#L105) | 105 | `"            \"WEB_SIMPLE\","` | — |
| [SRC-EA6EC52573-L000106](../../tests/test_intent_router.py#L106) | 106 | `"            \"summarization_request\","` | — |
| [SRC-EA6EC52573-L000107](../../tests/test_intent_router.py#L107) | 107 | `"        ),"` | — |
| [SRC-EA6EC52573-L000108](../../tests/test_intent_router.py#L108) | 108 | `"        ("` | — |
| [SRC-EA6EC52573-L000109](../../tests/test_intent_router.py#L109) | 109 | `"            \"Summarize this page https://example.com/article\","` | — |
| [SRC-EA6EC52573-L000110](../../tests/test_intent_router.py#L110) | 110 | `"            \"WEB_SIMPLE\","` | — |
| [SRC-EA6EC52573-L000111](../../tests/test_intent_router.py#L111) | 111 | `"            \"summarization_request\","` | — |
| [SRC-EA6EC52573-L000112](../../tests/test_intent_router.py#L112) | 112 | `"        ),"` | — |
| [SRC-EA6EC52573-L000113](../../tests/test_intent_router.py#L113) | 113 | `"        (\"لخص الصفحة\", \"CLARIFY\", \"missing_summarization_input\"),"` | — |
| [SRC-EA6EC52573-L000114](../../tests/test_intent_router.py#L114) | 114 | `"        (\"لخص لي هذا الرابط\", \"CLARIFY\", \"missing_summarization_input\"),"` | — |
| [SRC-EA6EC52573-L000115](../../tests/test_intent_router.py#L115) | 115 | `"        (\"summarize the page\", \"CLARIFY\", \"missing_summarization_input\"),"` | — |
| [SRC-EA6EC52573-L000116](../../tests/test_intent_router.py#L116) | 116 | `"        (\"تلخيص المقال\", \"CLARIFY\", \"missing_summarization_input\"),"` | — |
| [SRC-EA6EC52573-L000117](../../tests/test_intent_router.py#L117) | 117 | `"        (\"لخص النص التالي: هذا نص تجريبي\", \"MODEL_ONLY\", \"stable_knowledge_or_conversation\"),"` | — |
| [SRC-EA6EC52573-L000118](../../tests/test_intent_router.py#L118) | 118 | `"        (\"Summarize this text: the test content is here\", \"MODEL_ONLY\", \"stable_knowledge_or_conversation\"),"` | — |
| [SRC-EA6EC52573-L000119](../../tests/test_intent_router.py#L119) | 119 | `"    ],"` | — |
| [SRC-EA6EC52573-L000120](../../tests/test_intent_router.py#L120) | 120 | `")"` | — |
| [SRC-EA6EC52573-L000121](../../tests/test_intent_router.py#L121) | 121 | `"def test_summarization_routing_respects_page_text_and_missing_input("` | — |
| [SRC-EA6EC52573-L000122](../../tests/test_intent_router.py#L122) | 122 | `"    question: str, expected_route: str, expected_reason: str"` | — |
| [SRC-EA6EC52573-L000123](../../tests/test_intent_router.py#L123) | 123 | `") -> None:"` | — |
| [SRC-EA6EC52573-L000124](../../tests/test_intent_router.py#L124) | 124 | `"    decision = route_intent(question, [])"` | — |
| [SRC-EA6EC52573-L000125](../../tests/test_intent_router.py#L125) | 125 | `"    assert decision[\"route\"] == expected_route"` | — |
| [SRC-EA6EC52573-L000126](../../tests/test_intent_router.py#L126) | 126 | `"    assert decision[\"reason\"] == expected_reason"` | — |
| [SRC-EA6EC52573-L000127](../../tests/test_intent_router.py#L127) | 127 | `""` | — |
| [SRC-EA6EC52573-L000128](../../tests/test_intent_router.py#L128) | 128 | `""` | — |
| [SRC-EA6EC52573-L000129](../../tests/test_intent_router.py#L129) | 129 | `"@pytest.mark.parametrize("` | — |
| [SRC-EA6EC52573-L000130](../../tests/test_intent_router.py#L130) | 130 | `"    \"question\","` | — |
| [SRC-EA6EC52573-L000131](../../tests/test_intent_router.py#L131) | 131 | `"    ["` | — |
| [SRC-EA6EC52573-L000132](../../tests/test_intent_router.py#L132) | 132 | `"        \"فين؟\","` | — |
| [SRC-EA6EC52573-L000133](../../tests/test_intent_router.py#L133) | 133 | `"        \"فين هي؟\","` | — |
| [SRC-EA6EC52573-L000134](../../tests/test_intent_router.py#L134) | 134 | `"        \"مكانها فين؟\","` | — |
| [SRC-EA6EC52573-L000135](../../tests/test_intent_router.py#L135) | 135 | `"        \"هل فيه ضمان؟\","` | — |
| [SRC-EA6EC52573-L000136](../../tests/test_intent_router.py#L136) | 136 | `"        \"هل لها ضمان؟\","` | — |
| [SRC-EA6EC52573-L000137](../../tests/test_intent_router.py#L137) | 137 | `"        \"ضمانها إيه؟\","` | — |
| [SRC-EA6EC52573-L000138](../../tests/test_intent_router.py#L138) | 138 | `"        \"Where is it?\","` | — |
| [SRC-EA6EC52573-L000139](../../tests/test_intent_router.py#L139) | 139 | `"        \"Does it have a warranty?\","` | — |
| [SRC-EA6EC52573-L000140](../../tests/test_intent_router.py#L140) | 140 | `"    ],"` | — |
| [SRC-EA6EC52573-L000141](../../tests/test_intent_router.py#L141) | 141 | `")"` | — |
| [SRC-EA6EC52573-L000142](../../tests/test_intent_router.py#L142) | 142 | `"def test_missing_referent_questions_clarify_without_context(question: str) -> None:"` | — |
| [SRC-EA6EC52573-L000143](../../tests/test_intent_router.py#L143) | 143 | `"    decision = route_intent(question, history=None, mode=\"auto\", requires_web=True)"` | — |
| [SRC-EA6EC52573-L000144](../../tests/test_intent_router.py#L144) | 144 | `"    assert decision[\"route\"] == \"CLARIFY\""` | — |
| [SRC-EA6EC52573-L000145](../../tests/test_intent_router.py#L145) | 145 | `"    assert decision[\"needs_clarification\"] is True"` | — |
| [SRC-EA6EC52573-L000146](../../tests/test_intent_router.py#L146) | 146 | `"    assert decision[\"context_available\"] is False"` | — |
| [SRC-EA6EC52573-L000147](../../tests/test_intent_router.py#L147) | 147 | `""` | — |
| [SRC-EA6EC52573-L000148](../../tests/test_intent_router.py#L148) | 148 | `""` | — |
| [SRC-EA6EC52573-L000149](../../tests/test_intent_router.py#L149) | 149 | `"@pytest.mark.parametrize(\"question\", [\"فين؟\", \"هل فيه ضمان؟\", \"كام سعرها؟\"])"` | — |
| [SRC-EA6EC52573-L000150](../../tests/test_intent_router.py#L150) | 150 | `"def test_missing_referent_still_clarifies_in_explicit_search_mode(question: str) -> None:"` | — |
| [SRC-EA6EC52573-L000151](../../tests/test_intent_router.py#L151) | 151 | `"    decision = route_intent(question, history=None, mode=\"deep\")"` | — |
| [SRC-EA6EC52573-L000152](../../tests/test_intent_router.py#L152) | 152 | `"    assert decision[\"route\"] == \"CLARIFY\""` | — |
| [SRC-EA6EC52573-L000153](../../tests/test_intent_router.py#L153) | 153 | `"    assert decision[\"needs_clarification\"] is True"` | — |
| [SRC-EA6EC52573-L000154](../../tests/test_intent_router.py#L154) | 154 | `""` | — |
| [SRC-EA6EC52573-L000155](../../tests/test_intent_router.py#L155) | 155 | `""` | — |
| [SRC-EA6EC52573-L000156](../../tests/test_intent_router.py#L156) | 156 | `"def test_followup_resolver_uses_topic_from_latest_user_turn() -> None:"` | — |
| [SRC-EA6EC52573-L000157](../../tests/test_intent_router.py#L157) | 157 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000158](../../tests/test_intent_router.py#L158) | 158 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر آيفون 16 في مصر\"},"` | — |
| [SRC-EA6EC52573-L000159](../../tests/test_intent_router.py#L159) | 159 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن معلومات موثوقة.\"},"` | — |
| [SRC-EA6EC52573-L000160](../../tests/test_intent_router.py#L160) | 160 | `"    ]"` | — |
| [SRC-EA6EC52573-L000161](../../tests/test_intent_router.py#L161) | 161 | `"    resolved = resolve_followup_query(\"هل فيه ضمان؟\", history)"` | — |
| [SRC-EA6EC52573-L000162](../../tests/test_intent_router.py#L162) | 162 | `"    assert \"آيفون 16\" in resolved"` | — |
| [SRC-EA6EC52573-L000163](../../tests/test_intent_router.py#L163) | 163 | `"    assert \"ضمان\" in resolved"` | — |
| [SRC-EA6EC52573-L000164](../../tests/test_intent_router.py#L164) | 164 | `""` | — |
| [SRC-EA6EC52573-L000165](../../tests/test_intent_router.py#L165) | 165 | `""` | — |
| [SRC-EA6EC52573-L000166](../../tests/test_intent_router.py#L166) | 166 | `"def test_followup_resolver_does_not_resurrect_topic_after_acknowledgment() -> None:"` | — |
| [SRC-EA6EC52573-L000167](../../tests/test_intent_router.py#L167) | 167 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000168](../../tests/test_intent_router.py#L168) | 168 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر آيفون 16 في مصر\"},"` | — |
| [SRC-EA6EC52573-L000169](../../tests/test_intent_router.py#L169) | 169 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن معلومات موثوقة.\"},"` | — |
| [SRC-EA6EC52573-L000170](../../tests/test_intent_router.py#L170) | 170 | `"        {\"role\": \"user\", \"content\": \"شكرًا\"},"` | — |
| [SRC-EA6EC52573-L000171](../../tests/test_intent_router.py#L171) | 171 | `"        {\"role\": \"assistant\", \"content\": \"العفو.\"},"` | — |
| [SRC-EA6EC52573-L000172](../../tests/test_intent_router.py#L172) | 172 | `"    ]"` | — |
| [SRC-EA6EC52573-L000173](../../tests/test_intent_router.py#L173) | 173 | `"    assert resolve_followup_query(\"فين؟\", history) == \"فين؟\""` | — |
| [SRC-EA6EC52573-L000174](../../tests/test_intent_router.py#L174) | 174 | `""` | — |
| [SRC-EA6EC52573-L000175](../../tests/test_intent_router.py#L175) | 175 | `""` | — |
| [SRC-EA6EC52573-L000176](../../tests/test_intent_router.py#L176) | 176 | `"def test_followup_resolver_bounds_output_and_handles_malformed_history() -> None:"` | — |
| [SRC-EA6EC52573-L000177](../../tests/test_intent_router.py#L177) | 177 | `"    history = [{\"role\": \"user\", \"content\": \"س\" * 4000}]"` | — |
| [SRC-EA6EC52573-L000178](../../tests/test_intent_router.py#L178) | 178 | `"    assert len(resolve_followup_query(\"والسعر؟\", history)) <= 500"` | — |
| [SRC-EA6EC52573-L000179](../../tests/test_intent_router.py#L179) | 179 | `"    assert resolve_followup_query(\"فين؟\", {\"role\": \"user\", \"content\": \"topic\"}) == \"فين؟\""` | — |
| [SRC-EA6EC52573-L000180](../../tests/test_intent_router.py#L180) | 180 | `""` | — |
| [SRC-EA6EC52573-L000181](../../tests/test_intent_router.py#L181) | 181 | `"def test_prefixed_elliptical_followup_is_clarified_without_topic():"` | — |
| [SRC-EA6EC52573-L000182](../../tests/test_intent_router.py#L182) | 182 | `"    for question in (\"طب هل فيه ضمان؟\", \"طيب كام سعرها؟\", \"والضمان؟\", \"والسعر؟\"):"` | — |
| [SRC-EA6EC52573-L000183](../../tests/test_intent_router.py#L183) | 183 | `"        decision = route_intent(question)"` | — |
| [SRC-EA6EC52573-L000184](../../tests/test_intent_router.py#L184) | 184 | `"        assert decision[\"route\"] == \"CLARIFY\", question"` | — |
| [SRC-EA6EC52573-L000185](../../tests/test_intent_router.py#L185) | 185 | `""` | — |
| [SRC-EA6EC52573-L000186](../../tests/test_intent_router.py#L186) | 186 | `"def test_prefixed_elliptical_followup_uses_topic_when_available():"` | — |
| [SRC-EA6EC52573-L000187](../../tests/test_intent_router.py#L187) | 187 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000188](../../tests/test_intent_router.py#L188) | 188 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر iPhone 16 في مصر\"},"` | — |
| [SRC-EA6EC52573-L000189](../../tests/test_intent_router.py#L189) | 189 | `"        {\"role\": \"assistant\", \"content\": \"نتحدث عن iPhone 16 في مصر.\"},"` | — |
| [SRC-EA6EC52573-L000190](../../tests/test_intent_router.py#L190) | 190 | `"    ]"` | — |
| [SRC-EA6EC52573-L000191](../../tests/test_intent_router.py#L191) | 191 | `"    for question in (\"طب هل فيه ضمان؟\", \"طيب كام سعرها؟\", \"والضمان؟\"):"` | — |
| [SRC-EA6EC52573-L000192](../../tests/test_intent_router.py#L192) | 192 | `"        decision = route_intent(question, history, requires_web=True)"` | — |
| [SRC-EA6EC52573-L000193](../../tests/test_intent_router.py#L193) | 193 | `"        assert decision[\"route\"] == \"WEB_SIMPLE\", question"` | — |
| [SRC-EA6EC52573-L000194](../../tests/test_intent_router.py#L194) | 194 | `"        resolved = resolve_followup_query(question, history)"` | — |
| [SRC-EA6EC52573-L000195](../../tests/test_intent_router.py#L195) | 195 | `"        assert \"iPhone 16\" in resolved"` | — |
| [SRC-EA6EC52573-L000196](../../tests/test_intent_router.py#L196) | 196 | `"        assert \"مصر\" in resolved"` | — |
| [SRC-EA6EC52573-L000197](../../tests/test_intent_router.py#L197) | 197 | `""` | — |
| [SRC-EA6EC52573-L000198](../../tests/test_intent_router.py#L198) | 198 | `"def test_long_arabic_warranty_followup_resolves_with_context():"` | — |
| [SRC-EA6EC52573-L000199](../../tests/test_intent_router.py#L199) | 199 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000200](../../tests/test_intent_router.py#L200) | 200 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر iPhone 17 نسخة 256 جيجابايت في مصر\"},"` | — |
| [SRC-EA6EC52573-L000201](../../tests/test_intent_router.py#L201) | 201 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن السعر.\"},"` | — |
| [SRC-EA6EC52573-L000202](../../tests/test_intent_router.py#L202) | 202 | `"    ]"` | — |
| [SRC-EA6EC52573-L000203](../../tests/test_intent_router.py#L203) | 203 | `"    question = \"وطب الضمان الدولي بيسري في مصر؟\""` | — |
| [SRC-EA6EC52573-L000204](../../tests/test_intent_router.py#L204) | 204 | `"    resolved = resolve_followup_query(question, history)"` | — |
| [SRC-EA6EC52573-L000205](../../tests/test_intent_router.py#L205) | 205 | `"    assert \"iPhone 17\" in resolved"` | — |
| [SRC-EA6EC52573-L000206](../../tests/test_intent_router.py#L206) | 206 | `"    assert question in resolved"` | — |
| [SRC-EA6EC52573-L000207](../../tests/test_intent_router.py#L207) | 207 | `""` | — |
| [SRC-EA6EC52573-L000208](../../tests/test_intent_router.py#L208) | 208 | `"def test_long_arabic_warranty_followup_without_context_clarifies():"` | — |
| [SRC-EA6EC52573-L000209](../../tests/test_intent_router.py#L209) | 209 | `"    question = \"وطب الضمان الدولي بيسري في مصر؟\""` | — |
| [SRC-EA6EC52573-L000210](../../tests/test_intent_router.py#L210) | 210 | `"    decision = route_intent(question)"` | — |
| [SRC-EA6EC52573-L000211](../../tests/test_intent_router.py#L211) | 211 | `"    assert decision[\"route\"] == \"CLARIFY\""` | — |
| [SRC-EA6EC52573-L000212](../../tests/test_intent_router.py#L212) | 212 | `"    assert decision[\"needs_clarification\"] is True"` | — |
| [SRC-EA6EC52573-L000213](../../tests/test_intent_router.py#L213) | 213 | `""` | — |
| [SRC-EA6EC52573-L000214](../../tests/test_intent_router.py#L214) | 214 | `"def test_new_question_starting_with_tayyib_does_not_inherit_old_topic():"` | — |
| [SRC-EA6EC52573-L000215](../../tests/test_intent_router.py#L215) | 215 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000216](../../tests/test_intent_router.py#L216) | 216 | `"        {\"role\": \"user\", \"content\": \"ما سعر iPhone 16 في مصر؟\"},"` | — |
| [SRC-EA6EC52573-L000217](../../tests/test_intent_router.py#L217) | 217 | `"        {\"role\": \"assistant\", \"content\": \"هذه بعض معلومات السعر.\"},"` | — |
| [SRC-EA6EC52573-L000218](../../tests/test_intent_router.py#L218) | 218 | `"    ]"` | — |
| [SRC-EA6EC52573-L000219](../../tests/test_intent_router.py#L219) | 219 | `"    question = \"طيب اشرح الذكاء الاصطناعي في المدارس\""` | — |
| [SRC-EA6EC52573-L000220](../../tests/test_intent_router.py#L220) | 220 | `"    assert resolve_followup_query(question, history) == question"` | — |
| [SRC-EA6EC52573-L000221](../../tests/test_intent_router.py#L221) | 221 | `"    decision = route_intent(question, history)"` | — |
| [SRC-EA6EC52573-L000222](../../tests/test_intent_router.py#L222) | 222 | `"    assert decision[\"route\"] == \"MODEL_ONLY\""` | — |
| [SRC-EA6EC52573-L000223](../../tests/test_intent_router.py#L223) | 223 | `""` | — |
| [SRC-EA6EC52573-L000224](../../tests/test_intent_router.py#L224) | 224 | `"def test_chained_followups_keep_the_last_substantive_topic():"` | — |
| [SRC-EA6EC52573-L000225](../../tests/test_intent_router.py#L225) | 225 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000226](../../tests/test_intent_router.py#L226) | 226 | `"        {\"role\": \"user\", \"content\": \"ما سعر iPhone 16 في مصر؟\"},"` | — |
| [SRC-EA6EC52573-L000227](../../tests/test_intent_router.py#L227) | 227 | `"        {\"role\": \"assistant\", \"content\": \"السعر يختلف حسب المتجر.\"},"` | — |
| [SRC-EA6EC52573-L000228](../../tests/test_intent_router.py#L228) | 228 | `"        {\"role\": \"user\", \"content\": \"والضمان؟\"},"` | — |
| [SRC-EA6EC52573-L000229](../../tests/test_intent_router.py#L229) | 229 | `"        {\"role\": \"assistant\", \"content\": \"سأوضح الضمان.\"},"` | — |
| [SRC-EA6EC52573-L000230](../../tests/test_intent_router.py#L230) | 230 | `"    ]"` | — |
| [SRC-EA6EC52573-L000231](../../tests/test_intent_router.py#L231) | 231 | `"    resolved = resolve_followup_query(\"والبطارية؟\", history)"` | — |
| [SRC-EA6EC52573-L000232](../../tests/test_intent_router.py#L232) | 232 | `"    assert \"iPhone 16\" in resolved"` | — |
| [SRC-EA6EC52573-L000233](../../tests/test_intent_router.py#L233) | 233 | `"    assert \"البطارية\" in resolved"` | — |
| [SRC-EA6EC52573-L000234](../../tests/test_intent_router.py#L234) | 234 | `""` | — |
| [SRC-EA6EC52573-L000235](../../tests/test_intent_router.py#L235) | 235 | `"def test_answer_to_clarification_restores_original_intent():"` | — |
| [SRC-EA6EC52573-L000236](../../tests/test_intent_router.py#L236) | 236 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000237](../../tests/test_intent_router.py#L237) | 237 | `"        {\"role\": \"user\", \"content\": \"كام سعرها؟\"},"` | — |
| [SRC-EA6EC52573-L000238](../../tests/test_intent_router.py#L238) | 238 | `"        {"` | — |
| [SRC-EA6EC52573-L000239](../../tests/test_intent_router.py#L239) | 239 | `"            \"role\": \"assistant\","` | — |
| [SRC-EA6EC52573-L000240](../../tests/test_intent_router.py#L240) | 240 | `"            \"content\": \"تقصد إيه تحديدًا؟ اكتب اسم الشيء أو المنتج المقصود، أو ابعت الرابط، وأكمل معاك من غير ما أخمّن.\","` | — |
| [SRC-EA6EC52573-L000241](../../tests/test_intent_router.py#L241) | 241 | `"        },"` | — |
| [SRC-EA6EC52573-L000242](../../tests/test_intent_router.py#L242) | 242 | `"    ]"` | — |
| [SRC-EA6EC52573-L000243](../../tests/test_intent_router.py#L243) | 243 | `"    decision = route_intent(\"iPhone 16\", history)"` | — |
| [SRC-EA6EC52573-L000244](../../tests/test_intent_router.py#L244) | 244 | `"    assert decision[\"route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-EA6EC52573-L000245](../../tests/test_intent_router.py#L245) | 245 | `"    assert decision[\"reason\"] == \"answer_to_pending_clarification\""` | — |
| [SRC-EA6EC52573-L000246](../../tests/test_intent_router.py#L246) | 246 | `"    resolved = resolve_followup_query(\"iPhone 16\", history)"` | — |
| [SRC-EA6EC52573-L000247](../../tests/test_intent_router.py#L247) | 247 | `"    assert \"سعرها\" in resolved"` | — |
| [SRC-EA6EC52573-L000248](../../tests/test_intent_router.py#L248) | 248 | `"    assert \"iPhone 16\" in resolved"` | — |
| [SRC-EA6EC52573-L000249](../../tests/test_intent_router.py#L249) | 249 | `""` | — |
| [SRC-EA6EC52573-L000250](../../tests/test_intent_router.py#L250) | 250 | `"def test_topic_detection_does_not_inherit_old_social_or_depth_intent():"` | — |
| [SRC-EA6EC52573-L000251](../../tests/test_intent_router.py#L251) | 251 | `"    from agents.research import fallback_plan"` | — |
| [SRC-EA6EC52573-L000252](../../tests/test_intent_router.py#L252) | 252 | `""` | — |
| [SRC-EA6EC52573-L000253](../../tests/test_intent_router.py#L253) | 253 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000254](../../tests/test_intent_router.py#L254) | 254 | `"        {\"role\": \"user\", \"content\": \"اجمع آراء مستخدمي السيارات الكهربائية على Reddit\"},"` | — |
| [SRC-EA6EC52573-L000255](../../tests/test_intent_router.py#L255) | 255 | `"        {\"role\": \"assistant\", \"content\": \"هذه النتائج.\"},"` | — |
| [SRC-EA6EC52573-L000256](../../tests/test_intent_router.py#L256) | 256 | `"    ]"` | — |
| [SRC-EA6EC52573-L000257](../../tests/test_intent_router.py#L257) | 257 | `"    plan = fallback_plan(\"اشرح طريقة عمل المحرك الكهربائي\", history)"` | — |
| [SRC-EA6EC52573-L000258](../../tests/test_intent_router.py#L258) | 258 | `"    assert plan[\"social_focus\"] is False"` | — |
| [SRC-EA6EC52573-L000259](../../tests/test_intent_router.py#L259) | 259 | `"    assert plan[\"platforms\"] == []"` | — |
| [SRC-EA6EC52573-L000260](../../tests/test_intent_router.py#L260) | 260 | `"    assert plan[\"depth\"] == \"standard\""` | — |
| [SRC-EA6EC52573-L000261](../../tests/test_intent_router.py#L261) | 261 | `""` | — |
| [SRC-EA6EC52573-L000262](../../tests/test_intent_router.py#L262) | 262 | `"def test_explicit_request_for_reliable_sources_uses_web_search_in_auto_mode():"` | — |
| [SRC-EA6EC52573-L000263](../../tests/test_intent_router.py#L263) | 263 | `"    question = ("` | — |
| [SRC-EA6EC52573-L000264](../../tests/test_intent_router.py#L264) | 264 | `"        \"ما أهم استخدامات الذكاء الاصطناعي في الشركات الصغيرة؟ \""` | — |
| [SRC-EA6EC52573-L000265](../../tests/test_intent_router.py#L265) | 265 | `"        \"اذكر أمثلة ومصادر موثوقة.\""` | — |
| [SRC-EA6EC52573-L000266](../../tests/test_intent_router.py#L266) | 266 | `"    )"` | — |
| [SRC-EA6EC52573-L000267](../../tests/test_intent_router.py#L267) | 267 | `"    decision = route_intent(question, mode=\"auto\")"` | — |
| [SRC-EA6EC52573-L000268](../../tests/test_intent_router.py#L268) | 268 | `"    assert decision[\"route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-EA6EC52573-L000269](../../tests/test_intent_router.py#L269) | 269 | `"    assert decision[\"reason\"] == \"explicit_evidence_request\""` | — |
| [SRC-EA6EC52573-L000270](../../tests/test_intent_router.py#L270) | 270 | `""` | — |
| [SRC-EA6EC52573-L000271](../../tests/test_intent_router.py#L271) | 271 | `"def test_stable_question_without_source_request_remains_model_only():"` | — |
| [SRC-EA6EC52573-L000272](../../tests/test_intent_router.py#L272) | 272 | `"    decision = route_intent(\"اشرح الفرق بين التعلم الخاضع للإشراف وغير الخاضع للإشراف\")"` | — |
| [SRC-EA6EC52573-L000273](../../tests/test_intent_router.py#L273) | 273 | `"    assert decision[\"route\"] == \"MODEL_ONLY\""` | — |
| [SRC-EA6EC52573-L000274](../../tests/test_intent_router.py#L274) | 274 | `""` | — |
| [SRC-EA6EC52573-L000275](../../tests/test_intent_router.py#L275) | 275 | `"def test_attached_arabic_object_pronoun_resolves_against_previous_subject() -> None:"` | — |
| [SRC-EA6EC52573-L000276](../../tests/test_intent_router.py#L276) | 276 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000277](../../tests/test_intent_router.py#L277) | 277 | `"        {\"role\": \"user\", \"content\": \"بفكر أشتري Lenovo ThinkPad E14 في مصر\"},"` | — |
| [SRC-EA6EC52573-L000278](../../tests/test_intent_router.py#L278) | 278 | `"        {\"role\": \"assistant\", \"content\": \"نتحدث عن Lenovo ThinkPad E14 في السوق المصري.\"},"` | — |
| [SRC-EA6EC52573-L000279](../../tests/test_intent_router.py#L279) | 279 | `"    ]"` | — |
| [SRC-EA6EC52573-L000280](../../tests/test_intent_router.py#L280) | 280 | `""` | — |
| [SRC-EA6EC52573-L000281](../../tests/test_intent_router.py#L281) | 281 | `"    resolved = resolve_followup_query(\"أقدر أشتريه منين؟\", history)"` | — |
| [SRC-EA6EC52573-L000282](../../tests/test_intent_router.py#L282) | 282 | `""` | — |
| [SRC-EA6EC52573-L000283](../../tests/test_intent_router.py#L283) | 283 | `"    assert \"Lenovo ThinkPad E14\" in resolved"` | — |
| [SRC-EA6EC52573-L000284](../../tests/test_intent_router.py#L284) | 284 | `"    assert \"أقدر أشتريه منين\" in resolved"` | — |
| [SRC-EA6EC52573-L000285](../../tests/test_intent_router.py#L285) | 285 | `""` | — |
| [SRC-EA6EC52573-L000286](../../tests/test_intent_router.py#L286) | 286 | `"def test_no_duplicate_followup_leadin_symbols():"` | — |
| [SRC-EA6EC52573-L000287](../../tests/test_intent_router.py#L287) | 287 | `"    \"\"\"Follow-up normalization symbols must have one authoritative definition.\"\"\""` | — |
| [SRC-EA6EC52573-L000288](../../tests/test_intent_router.py#L288) | 288 | `"    import inspect"` | — |
| [SRC-EA6EC52573-L000289](../../tests/test_intent_router.py#L289) | 289 | `"    from agents import intent_router"` | — |
| [SRC-EA6EC52573-L000290](../../tests/test_intent_router.py#L290) | 290 | `""` | — |
| [SRC-EA6EC52573-L000291](../../tests/test_intent_router.py#L291) | 291 | `"    module_source = inspect.getsource(intent_router)"` | — |
| [SRC-EA6EC52573-L000292](../../tests/test_intent_router.py#L292) | 292 | `"    assert module_source.count(\"_FOLLOWUP_LEAD_IN_RE = re.compile\") == 1"` | — |
| [SRC-EA6EC52573-L000293](../../tests/test_intent_router.py#L293) | 293 | `"    assert module_source.count(\"_FOLLOWUP_ASPECT_FRAGMENTS = frozenset\") == 1"` | — |
