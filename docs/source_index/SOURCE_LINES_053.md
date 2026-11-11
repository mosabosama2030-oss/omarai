# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **053**
- سجلات الأسطر: **800**
- النطاق: SRC-1521F490CA-L000133 إلى SRC-44CDA52D01-L000142
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-1521F490CA — [tests/test_multitenant.py](../../tests/test_multitenant.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1521F490CA-L000133](../../tests/test_multitenant.py#L133) | 133 | `"        unique_indexes = ["` | — |
| [SRC-1521F490CA-L000134](../../tests/test_multitenant.py#L134) | 134 | `"            row[\"name\"] for row in db.execute(\"PRAGMA index_list(leads)\")"` | — |
| [SRC-1521F490CA-L000135](../../tests/test_multitenant.py#L135) | 135 | `"            if row[\"unique\"]"` | — |
| [SRC-1521F490CA-L000136](../../tests/test_multitenant.py#L136) | 136 | `"        ]"` | — |
| [SRC-1521F490CA-L000137](../../tests/test_multitenant.py#L137) | 137 | `"        unique_columns = ["` | — |
| [SRC-1521F490CA-L000138](../../tests/test_multitenant.py#L138) | 138 | `"            ["` | — |
| [SRC-1521F490CA-L000139](../../tests/test_multitenant.py#L139) | 139 | `"                item[\"name\"]"` | — |
| [SRC-1521F490CA-L000140](../../tests/test_multitenant.py#L140) | 140 | `"                for item in db.execute(f\"PRAGMA index_info('{index_name}')\")"` | — |
| [SRC-1521F490CA-L000141](../../tests/test_multitenant.py#L141) | 141 | `"            ]"` | — |
| [SRC-1521F490CA-L000142](../../tests/test_multitenant.py#L142) | 142 | `"            for index_name in unique_indexes"` | — |
| [SRC-1521F490CA-L000143](../../tests/test_multitenant.py#L143) | 143 | `"        ]"` | — |
| [SRC-1521F490CA-L000144](../../tests/test_multitenant.py#L144) | 144 | `"    assert \"tenant_id\" in columns"` | — |
| [SRC-1521F490CA-L000145](../../tests/test_multitenant.py#L145) | 145 | `"    assert [\"fingerprint\"] not in unique_columns"` | — |
| [SRC-1521F490CA-L000146](../../tests/test_multitenant.py#L146) | 146 | `"    assert [\"tenant_id\", \"fingerprint\"] in unique_columns"` | — |
| [SRC-1521F490CA-L000147](../../tests/test_multitenant.py#L147) | 147 | `""` | — |
| [SRC-1521F490CA-L000148](../../tests/test_multitenant.py#L148) | 148 | `""` | — |
| [SRC-1521F490CA-L000149](../../tests/test_multitenant.py#L149) | 149 | `""` | — |
| [SRC-1521F490CA-L000150](../../tests/test_multitenant.py#L150) | 150 | `"def test_legacy_migration_rolls_back_and_keeps_original_table_on_copy_error(tmp_path):"` | — |
| [SRC-1521F490CA-L000151](../../tests/test_multitenant.py#L151) | 151 | `"    path = tmp_path / \"incomplete-legacy.sqlite3\""` | — |
| [SRC-1521F490CA-L000152](../../tests/test_multitenant.py#L152) | 152 | `"    with sqlite3.connect(path) as db:"` | — |
| [SRC-1521F490CA-L000153](../../tests/test_multitenant.py#L153) | 153 | `"        db.execute("` | — |
| [SRC-1521F490CA-L000154](../../tests/test_multitenant.py#L154) | 154 | `"            \"CREATE TABLE leads (id TEXT PRIMARY KEY, fingerprint TEXT UNIQUE NOT NULL, text TEXT NOT NULL)\""` | — |
| [SRC-1521F490CA-L000155](../../tests/test_multitenant.py#L155) | 155 | `"        )"` | — |
| [SRC-1521F490CA-L000156](../../tests/test_multitenant.py#L156) | 156 | `"        db.execute("` | — |
| [SRC-1521F490CA-L000157](../../tests/test_multitenant.py#L157) | 157 | `"            \"INSERT INTO leads (id, fingerprint, text) VALUES (?, ?, ?)\","` | — |
| [SRC-1521F490CA-L000158](../../tests/test_multitenant.py#L158) | 158 | `"            (\"legacy-1\", \"fingerprint-1\", \"preserve me\"),"` | — |
| [SRC-1521F490CA-L000159](../../tests/test_multitenant.py#L159) | 159 | `"        )"` | — |
| [SRC-1521F490CA-L000160](../../tests/test_multitenant.py#L160) | 160 | `""` | — |
| [SRC-1521F490CA-L000161](../../tests/test_multitenant.py#L161) | 161 | `"    import pytest"` | — |
| [SRC-1521F490CA-L000162](../../tests/test_multitenant.py#L162) | 162 | `""` | — |
| [SRC-1521F490CA-L000163](../../tests/test_multitenant.py#L163) | 163 | `"    with pytest.raises(sqlite3.OperationalError):"` | — |
| [SRC-1521F490CA-L000164](../../tests/test_multitenant.py#L164) | 164 | `"        LeadStore(path)"` | — |
| [SRC-1521F490CA-L000165](../../tests/test_multitenant.py#L165) | 165 | `""` | — |
| [SRC-1521F490CA-L000166](../../tests/test_multitenant.py#L166) | 166 | `"    with sqlite3.connect(path) as db:"` | — |
| [SRC-1521F490CA-L000167](../../tests/test_multitenant.py#L167) | 167 | `"        tables = {"` | — |
| [SRC-1521F490CA-L000168](../../tests/test_multitenant.py#L168) | 168 | `"            row[0]"` | — |
| [SRC-1521F490CA-L000169](../../tests/test_multitenant.py#L169) | 169 | `"            for row in db.execute("` | — |
| [SRC-1521F490CA-L000170](../../tests/test_multitenant.py#L170) | 170 | `"                \"SELECT name FROM sqlite_master WHERE type='table'\""` | — |
| [SRC-1521F490CA-L000171](../../tests/test_multitenant.py#L171) | 171 | `"            )"` | — |
| [SRC-1521F490CA-L000172](../../tests/test_multitenant.py#L172) | 172 | `"        }"` | — |
| [SRC-1521F490CA-L000173](../../tests/test_multitenant.py#L173) | 173 | `"        original = db.execute("` | — |
| [SRC-1521F490CA-L000174](../../tests/test_multitenant.py#L174) | 174 | `"            \"SELECT id, fingerprint, text FROM leads\""` | — |
| [SRC-1521F490CA-L000175](../../tests/test_multitenant.py#L175) | 175 | `"        ).fetchone()"` | — |
| [SRC-1521F490CA-L000176](../../tests/test_multitenant.py#L176) | 176 | `"    assert \"leads\" in tables"` | — |
| [SRC-1521F490CA-L000177](../../tests/test_multitenant.py#L177) | 177 | `"    assert \"leads_legacy_migration\" not in tables"` | — |
| [SRC-1521F490CA-L000178](../../tests/test_multitenant.py#L178) | 178 | `"    assert original == (\"legacy-1\", \"fingerprint-1\", \"preserve me\")"` | — |
| [SRC-1521F490CA-L000179](../../tests/test_multitenant.py#L179) | 179 | `""` | — |
| [SRC-1521F490CA-L000180](../../tests/test_multitenant.py#L180) | 180 | `""` | — |
| [SRC-1521F490CA-L000181](../../tests/test_multitenant.py#L181) | 181 | `"def test_api_token_expiry_is_normalized_to_utc(tmp_path):"` | — |
| [SRC-1521F490CA-L000182](../../tests/test_multitenant.py#L182) | 182 | `"    store = LeadStore(tmp_path / \"token-expiry.sqlite3\")"` | — |
| [SRC-1521F490CA-L000183](../../tests/test_multitenant.py#L183) | 183 | `"    tenant_id, user_id = _tenant_member("` | — |
| [SRC-1521F490CA-L000184](../../tests/test_multitenant.py#L184) | 184 | `"        store, \"Expiry Company\", \"expiry@example.test\", \"E\" * 40"` | — |
| [SRC-1521F490CA-L000185](../../tests/test_multitenant.py#L185) | 185 | `"    )"` | — |
| [SRC-1521F490CA-L000186](../../tests/test_multitenant.py#L186) | 186 | `"    token = \"F\" * 40"` | — |
| [SRC-1521F490CA-L000187](../../tests/test_multitenant.py#L187) | 187 | `"    store.create_api_token("` | — |
| [SRC-1521F490CA-L000188](../../tests/test_multitenant.py#L188) | 188 | `"        token,"` | — |
| [SRC-1521F490CA-L000189](../../tests/test_multitenant.py#L189) | 189 | `"        tenant_id,"` | — |
| [SRC-1521F490CA-L000190](../../tests/test_multitenant.py#L190) | 190 | `"        user_id,"` | — |
| [SRC-1521F490CA-L000191](../../tests/test_multitenant.py#L191) | 191 | `"        expires_at=\"2099-01-01T03:00:00+03:00\","` | — |
| [SRC-1521F490CA-L000192](../../tests/test_multitenant.py#L192) | 192 | `"    )"` | — |
| [SRC-1521F490CA-L000193](../../tests/test_multitenant.py#L193) | 193 | `"    with store.connect() as db:"` | — |
| [SRC-1521F490CA-L000194](../../tests/test_multitenant.py#L194) | 194 | `"        row = db.execute("` | — |
| [SRC-1521F490CA-L000195](../../tests/test_multitenant.py#L195) | 195 | `"            \"SELECT expires_at FROM api_tokens WHERE token_hash=?\","` | — |
| [SRC-1521F490CA-L000196](../../tests/test_multitenant.py#L196) | 196 | `"            (store._token_hash(token),),"` | — |
| [SRC-1521F490CA-L000197](../../tests/test_multitenant.py#L197) | 197 | `"        ).fetchone()"` | — |
| [SRC-1521F490CA-L000198](../../tests/test_multitenant.py#L198) | 198 | `"    assert row[\"expires_at\"] == \"2099-01-01T00:00:00Z\""` | — |
| [SRC-1521F490CA-L000199](../../tests/test_multitenant.py#L199) | 199 | `"    assert store.resolve_api_token(token) is not None"` | — |
| [SRC-1521F490CA-L000200](../../tests/test_multitenant.py#L200) | 200 | `""` | — |
| [SRC-1521F490CA-L000201](../../tests/test_multitenant.py#L201) | 201 | `"    # Expired tokens must stop resolving even when their membership stays active."` | — |
| [SRC-1521F490CA-L000202](../../tests/test_multitenant.py#L202) | 202 | `"    with store.connect() as db:"` | — |
| [SRC-1521F490CA-L000203](../../tests/test_multitenant.py#L203) | 203 | `"        db.execute("` | — |
| [SRC-1521F490CA-L000204](../../tests/test_multitenant.py#L204) | 204 | `"            \"UPDATE api_tokens SET expires_at=? WHERE token_hash=?\","` | — |
| [SRC-1521F490CA-L000205](../../tests/test_multitenant.py#L205) | 205 | `"            (\"2000-01-01T00:00:00Z\", store._token_hash(token)),"` | — |
| [SRC-1521F490CA-L000206](../../tests/test_multitenant.py#L206) | 206 | `"        )"` | — |
| [SRC-1521F490CA-L000207](../../tests/test_multitenant.py#L207) | 207 | `"    assert store.resolve_api_token(token) is None"` | — |
| [SRC-1521F490CA-L000208](../../tests/test_multitenant.py#L208) | 208 | `""` | — |
| [SRC-1521F490CA-L000209](../../tests/test_multitenant.py#L209) | 209 | `"    utc_token = \"J\" * 40"` | — |
| [SRC-1521F490CA-L000210](../../tests/test_multitenant.py#L210) | 210 | `"    store.create_api_token("` | — |
| [SRC-1521F490CA-L000211](../../tests/test_multitenant.py#L211) | 211 | `"        utc_token, tenant_id, user_id, expires_at=\"2099-01-01T00:00:00Z\""` | — |
| [SRC-1521F490CA-L000212](../../tests/test_multitenant.py#L212) | 212 | `"    )"` | — |
| [SRC-1521F490CA-L000213](../../tests/test_multitenant.py#L213) | 213 | `"    assert store.resolve_api_token(utc_token) is not None"` | — |
| [SRC-1521F490CA-L000214](../../tests/test_multitenant.py#L214) | 214 | `""` | — |
| [SRC-1521F490CA-L000215](../../tests/test_multitenant.py#L215) | 215 | `""` | — |
| [SRC-1521F490CA-L000216](../../tests/test_multitenant.py#L216) | 216 | `"def test_api_token_expiry_rejects_naive_malformed_and_past_values(tmp_path):"` | — |
| [SRC-1521F490CA-L000217](../../tests/test_multitenant.py#L217) | 217 | `"    store = LeadStore(tmp_path / \"invalid-token-expiry.sqlite3\")"` | — |
| [SRC-1521F490CA-L000218](../../tests/test_multitenant.py#L218) | 218 | `"    tenant_id, user_id = _tenant_member("` | — |
| [SRC-1521F490CA-L000219](../../tests/test_multitenant.py#L219) | 219 | `"        store, \"Expiry Validation Company\", \"expiry-validation@example.test\", \"G\" * 40"` | — |
| [SRC-1521F490CA-L000220](../../tests/test_multitenant.py#L220) | 220 | `"    )"` | — |
| [SRC-1521F490CA-L000221](../../tests/test_multitenant.py#L221) | 221 | `"    invalid_values = ("` | — |
| [SRC-1521F490CA-L000222](../../tests/test_multitenant.py#L222) | 222 | `"        \"2099-01-01T00:00:00\","` | — |
| [SRC-1521F490CA-L000223](../../tests/test_multitenant.py#L223) | 223 | `"        \"not-a-timestamp\","` | — |
| [SRC-1521F490CA-L000224](../../tests/test_multitenant.py#L224) | 224 | `"        \"2000-01-01T00:00:00Z\","` | — |
| [SRC-1521F490CA-L000225](../../tests/test_multitenant.py#L225) | 225 | `"        \"\","` | — |
| [SRC-1521F490CA-L000226](../../tests/test_multitenant.py#L226) | 226 | `"    )"` | — |
| [SRC-1521F490CA-L000227](../../tests/test_multitenant.py#L227) | 227 | `"    for index, expiry in enumerate(invalid_values):"` | — |
| [SRC-1521F490CA-L000228](../../tests/test_multitenant.py#L228) | 228 | `"        with pytest.raises(ValueError, match=\"expires_at\"):"` | — |
| [SRC-1521F490CA-L000229](../../tests/test_multitenant.py#L229) | 229 | `"            store.create_api_token("` | — |
| [SRC-1521F490CA-L000230](../../tests/test_multitenant.py#L230) | 230 | `"                (\"H\" * 39) + str(index),"` | — |
| [SRC-1521F490CA-L000231](../../tests/test_multitenant.py#L231) | 231 | `"                tenant_id,"` | — |
| [SRC-1521F490CA-L000232](../../tests/test_multitenant.py#L232) | 232 | `"                user_id,"` | — |
| [SRC-1521F490CA-L000233](../../tests/test_multitenant.py#L233) | 233 | `"                expires_at=expiry,"` | — |
| [SRC-1521F490CA-L000234](../../tests/test_multitenant.py#L234) | 234 | `"            )"` | — |
| [SRC-1521F490CA-L000235](../../tests/test_multitenant.py#L235) | 235 | `""` | — |
| [SRC-1521F490CA-L000236](../../tests/test_multitenant.py#L236) | 236 | `""` | — |
| [SRC-1521F490CA-L000237](../../tests/test_multitenant.py#L237) | 237 | `""` | — |
| [SRC-1521F490CA-L000238](../../tests/test_multitenant.py#L238) | 238 | `"def test_api_token_revocation_is_scoped_to_the_owning_user_and_tenant(tmp_path):"` | — |
| [SRC-1521F490CA-L000239](../../tests/test_multitenant.py#L239) | 239 | `"    store = LeadStore(tmp_path / \"revoke-token.sqlite3\")"` | — |
| [SRC-1521F490CA-L000240](../../tests/test_multitenant.py#L240) | 240 | `"    tenant_id, user_id = _tenant_member("` | — |
| [SRC-1521F490CA-L000241](../../tests/test_multitenant.py#L241) | 241 | `"        store, \"Revocation Company\", \"owner@example.test\", \"K\" * 40"` | — |
| [SRC-1521F490CA-L000242](../../tests/test_multitenant.py#L242) | 242 | `"    )"` | — |
| [SRC-1521F490CA-L000243](../../tests/test_multitenant.py#L243) | 243 | `"    other_tenant_id, other_user_id = _tenant_member("` | — |
| [SRC-1521F490CA-L000244](../../tests/test_multitenant.py#L244) | 244 | `"        store, \"Other Revocation Company\", \"other@example.test\", \"L\" * 40"` | — |
| [SRC-1521F490CA-L000245](../../tests/test_multitenant.py#L245) | 245 | `"    )"` | — |
| [SRC-1521F490CA-L000246](../../tests/test_multitenant.py#L246) | 246 | `"    token = \"M\" * 40"` | — |
| [SRC-1521F490CA-L000247](../../tests/test_multitenant.py#L247) | 247 | `"    store.create_api_token(token, tenant_id, user_id)"` | — |
| [SRC-1521F490CA-L000248](../../tests/test_multitenant.py#L248) | 248 | `""` | — |
| [SRC-1521F490CA-L000249](../../tests/test_multitenant.py#L249) | 249 | `"    assert store.resolve_api_token(token)[\"tenant_id\"] == tenant_id"` | — |
| [SRC-1521F490CA-L000250](../../tests/test_multitenant.py#L250) | 250 | `"    assert store.revoke_api_token("` | — |
| [SRC-1521F490CA-L000251](../../tests/test_multitenant.py#L251) | 251 | `"        token, tenant_id=other_tenant_id, user_id=other_user_id"` | — |
| [SRC-1521F490CA-L000252](../../tests/test_multitenant.py#L252) | 252 | `"    ) is False"` | — |
| [SRC-1521F490CA-L000253](../../tests/test_multitenant.py#L253) | 253 | `"    assert store.resolve_api_token(token)[\"tenant_id\"] == tenant_id"` | — |
| [SRC-1521F490CA-L000254](../../tests/test_multitenant.py#L254) | 254 | `"    assert store.revoke_api_token("` | — |
| [SRC-1521F490CA-L000255](../../tests/test_multitenant.py#L255) | 255 | `"        token, tenant_id=tenant_id, user_id=other_user_id"` | — |
| [SRC-1521F490CA-L000256](../../tests/test_multitenant.py#L256) | 256 | `"    ) is False"` | — |
| [SRC-1521F490CA-L000257](../../tests/test_multitenant.py#L257) | 257 | `"    assert store.resolve_api_token(token)[\"tenant_id\"] == tenant_id"` | — |
| [SRC-1521F490CA-L000258](../../tests/test_multitenant.py#L258) | 258 | `""` | — |
| [SRC-1521F490CA-L000259](../../tests/test_multitenant.py#L259) | 259 | `"    assert store.revoke_api_token("` | — |
| [SRC-1521F490CA-L000260](../../tests/test_multitenant.py#L260) | 260 | `"        token, tenant_id=tenant_id, user_id=user_id"` | — |
| [SRC-1521F490CA-L000261](../../tests/test_multitenant.py#L261) | 261 | `"    ) is True"` | — |
| [SRC-1521F490CA-L000262](../../tests/test_multitenant.py#L262) | 262 | `"    assert store.resolve_api_token(token) is None"` | — |
| [SRC-1521F490CA-L000263](../../tests/test_multitenant.py#L263) | 263 | `"    assert store.revoke_api_token("` | — |
| [SRC-1521F490CA-L000264](../../tests/test_multitenant.py#L264) | 264 | `"        token, tenant_id=tenant_id, user_id=user_id"` | — |
| [SRC-1521F490CA-L000265](../../tests/test_multitenant.py#L265) | 265 | `"    ) is False"` | — |
| [SRC-1521F490CA-L000266](../../tests/test_multitenant.py#L266) | 266 | `""` | — |
| [SRC-1521F490CA-L000267](../../tests/test_multitenant.py#L267) | 267 | `"def test_store_connections_are_closed_after_success_and_rollback(tmp_path, monkeypatch):"` | — |
| [SRC-1521F490CA-L000268](../../tests/test_multitenant.py#L268) | 268 | `"    store = LeadStore(tmp_path / \"connection-lifecycle.sqlite3\")"` | — |
| [SRC-1521F490CA-L000269](../../tests/test_multitenant.py#L269) | 269 | `"    real_connect = sqlite3.connect"` | — |
| [SRC-1521F490CA-L000270](../../tests/test_multitenant.py#L270) | 270 | `"    opened = []"` | — |
| [SRC-1521F490CA-L000271](../../tests/test_multitenant.py#L271) | 271 | `""` | — |
| [SRC-1521F490CA-L000272](../../tests/test_multitenant.py#L272) | 272 | `"    def tracked_connect(*args, **kwargs):"` | — |
| [SRC-1521F490CA-L000273](../../tests/test_multitenant.py#L273) | 273 | `"        connection = real_connect(*args, **kwargs)"` | — |
| [SRC-1521F490CA-L000274](../../tests/test_multitenant.py#L274) | 274 | `"        opened.append(connection)"` | — |
| [SRC-1521F490CA-L000275](../../tests/test_multitenant.py#L275) | 275 | `"        return connection"` | — |
| [SRC-1521F490CA-L000276](../../tests/test_multitenant.py#L276) | 276 | `""` | — |
| [SRC-1521F490CA-L000277](../../tests/test_multitenant.py#L277) | 277 | `"    monkeypatch.setattr(sqlite3, \"connect\", tracked_connect)"` | — |
| [SRC-1521F490CA-L000278](../../tests/test_multitenant.py#L278) | 278 | `""` | — |
| [SRC-1521F490CA-L000279](../../tests/test_multitenant.py#L279) | 279 | `"    assert store.list(tenant_id=DEFAULT_TENANT_ID) == []"` | — |
| [SRC-1521F490CA-L000280](../../tests/test_multitenant.py#L280) | 280 | `"    assert len(opened) == 1"` | — |
| [SRC-1521F490CA-L000281](../../tests/test_multitenant.py#L281) | 281 | `"    with pytest.raises(sqlite3.ProgrammingError, match=\"closed\"):"` | — |
| [SRC-1521F490CA-L000282](../../tests/test_multitenant.py#L282) | 282 | `"        opened[0].execute(\"SELECT 1\")"` | — |
| [SRC-1521F490CA-L000283](../../tests/test_multitenant.py#L283) | 283 | `""` | — |
| [SRC-1521F490CA-L000284](../../tests/test_multitenant.py#L284) | 284 | `"    with pytest.raises(RuntimeError, match=\"force rollback\"), store.connect() as db:"` | — |
| [SRC-1521F490CA-L000285](../../tests/test_multitenant.py#L285) | 285 | `"        db.execute("` | — |
| [SRC-1521F490CA-L000286](../../tests/test_multitenant.py#L286) | 286 | `"            \"INSERT INTO tenants (id, name, slug, active, created_at) \""` | — |
| [SRC-1521F490CA-L000287](../../tests/test_multitenant.py#L287) | 287 | `"            \"VALUES (?, ?, ?, 1, ?)\","` | — |
| [SRC-1521F490CA-L000288](../../tests/test_multitenant.py#L288) | 288 | `"            (\"tenant_rollback_test\", \"Rollback\", \"rollback-test\", \"2026-11-01T00:00:00Z\"),"` | — |
| [SRC-1521F490CA-L000289](../../tests/test_multitenant.py#L289) | 289 | `"        )"` | — |
| [SRC-1521F490CA-L000290](../../tests/test_multitenant.py#L290) | 290 | `"        raise RuntimeError(\"force rollback\")"` | — |
| [SRC-1521F490CA-L000291](../../tests/test_multitenant.py#L291) | 291 | `""` | — |
| [SRC-1521F490CA-L000292](../../tests/test_multitenant.py#L292) | 292 | `"    assert len(opened) == 2"` | — |
| [SRC-1521F490CA-L000293](../../tests/test_multitenant.py#L293) | 293 | `"    with pytest.raises(sqlite3.ProgrammingError, match=\"closed\"):"` | — |
| [SRC-1521F490CA-L000294](../../tests/test_multitenant.py#L294) | 294 | `"        opened[1].execute(\"SELECT 1\")"` | — |
| [SRC-1521F490CA-L000295](../../tests/test_multitenant.py#L295) | 295 | `""` | — |
| [SRC-1521F490CA-L000296](../../tests/test_multitenant.py#L296) | 296 | `"    with store.connect() as db:"` | — |
| [SRC-1521F490CA-L000297](../../tests/test_multitenant.py#L297) | 297 | `"        assert db.execute("` | — |
| [SRC-1521F490CA-L000298](../../tests/test_multitenant.py#L298) | 298 | `"            \"SELECT 1 FROM tenants WHERE id=?\","` | — |
| [SRC-1521F490CA-L000299](../../tests/test_multitenant.py#L299) | 299 | `"            (\"tenant_rollback_test\",),"` | — |
| [SRC-1521F490CA-L000300](../../tests/test_multitenant.py#L300) | 300 | `"        ).fetchone() is None"` | — |
| [SRC-1521F490CA-L000301](../../tests/test_multitenant.py#L301) | 301 | `""` | — |
| [SRC-1521F490CA-L000302](../../tests/test_multitenant.py#L302) | 302 | `"def test_browser_sessions_are_opaque_expiring_and_bound_to_api_token(tmp_path):"` | — |
| [SRC-1521F490CA-L000303](../../tests/test_multitenant.py#L303) | 303 | `"    store = LeadStore(tmp_path / \"browser-session.sqlite3\")"` | — |
| [SRC-1521F490CA-L000304](../../tests/test_multitenant.py#L304) | 304 | `"    tenant_id = store.create_tenant(\"Session Company\", \"session-company\")"` | — |
| [SRC-1521F490CA-L000305](../../tests/test_multitenant.py#L305) | 305 | `"    user_id = store.create_user(\"session@example.test\", \"Session User\")"` | — |
| [SRC-1521F490CA-L000306](../../tests/test_multitenant.py#L306) | 306 | `"    store.add_membership(tenant_id, user_id, \"sales_agent\")"` | — |
| [SRC-1521F490CA-L000307](../../tests/test_multitenant.py#L307) | 307 | `"    api_token = \"session-api-token-\" + \"S\" * 40"` | — |
| [SRC-1521F490CA-L000308](../../tests/test_multitenant.py#L308) | 308 | `"    store.create_api_token(api_token, tenant_id, user_id, label=\"browser\")"` | — |
| [SRC-1521F490CA-L000309](../../tests/test_multitenant.py#L309) | 309 | `"    created = store.create_web_session(api_token)"` | — |
| [SRC-1521F490CA-L000310](../../tests/test_multitenant.py#L310) | 310 | `"    assert created is not None"` | — |
| [SRC-1521F490CA-L000311](../../tests/test_multitenant.py#L311) | 311 | `"    session_id, principal = created"` | — |
| [SRC-1521F490CA-L000312](../../tests/test_multitenant.py#L312) | 312 | `""` | — |
| [SRC-1521F490CA-L000313](../../tests/test_multitenant.py#L313) | 313 | `"    assert session_id != api_token"` | — |
| [SRC-1521F490CA-L000314](../../tests/test_multitenant.py#L314) | 314 | `"    assert principal == {"` | — |
| [SRC-1521F490CA-L000315](../../tests/test_multitenant.py#L315) | 315 | `"        \"tenant_id\": tenant_id,"` | — |
| [SRC-1521F490CA-L000316](../../tests/test_multitenant.py#L316) | 316 | `"        \"user_id\": user_id,"` | — |
| [SRC-1521F490CA-L000317](../../tests/test_multitenant.py#L317) | 317 | `"        \"role\": \"sales_agent\","` | — |
| [SRC-1521F490CA-L000318](../../tests/test_multitenant.py#L318) | 318 | `"    }"` | — |
| [SRC-1521F490CA-L000319](../../tests/test_multitenant.py#L319) | 319 | `"    assert store.resolve_web_session(session_id) == principal"` | — |
| [SRC-1521F490CA-L000320](../../tests/test_multitenant.py#L320) | 320 | `""` | — |
| [SRC-1521F490CA-L000321](../../tests/test_multitenant.py#L321) | 321 | `"    with store.connect() as db:"` | — |
| [SRC-1521F490CA-L000322](../../tests/test_multitenant.py#L322) | 322 | `"        stored = db.execute("` | — |
| [SRC-1521F490CA-L000323](../../tests/test_multitenant.py#L323) | 323 | `"            \"SELECT session_hash, credential_hash FROM web_sessions\""` | — |
| [SRC-1521F490CA-L000324](../../tests/test_multitenant.py#L324) | 324 | `"        ).fetchone()"` | — |
| [SRC-1521F490CA-L000325](../../tests/test_multitenant.py#L325) | 325 | `"    assert stored[\"session_hash\"] == store._token_hash(session_id)"` | — |
| [SRC-1521F490CA-L000326](../../tests/test_multitenant.py#L326) | 326 | `"    assert stored[\"credential_hash\"] == store._token_hash(api_token)"` | — |
| [SRC-1521F490CA-L000327](../../tests/test_multitenant.py#L327) | 327 | `"    assert session_id not in stored[\"session_hash\"]"` | — |
| [SRC-1521F490CA-L000328](../../tests/test_multitenant.py#L328) | 328 | `"    assert api_token not in stored[\"credential_hash\"]"` | — |
| [SRC-1521F490CA-L000329](../../tests/test_multitenant.py#L329) | 329 | `""` | — |
| [SRC-1521F490CA-L000330](../../tests/test_multitenant.py#L330) | 330 | `"    assert store.revoke_api_token("` | — |
| [SRC-1521F490CA-L000331](../../tests/test_multitenant.py#L331) | 331 | `"        api_token, tenant_id=tenant_id, user_id=user_id"` | — |
| [SRC-1521F490CA-L000332](../../tests/test_multitenant.py#L332) | 332 | `"    ) is True"` | — |
| [SRC-1521F490CA-L000333](../../tests/test_multitenant.py#L333) | 333 | `"    assert store.resolve_web_session(session_id) is None"` | — |
| [SRC-1521F490CA-L000334](../../tests/test_multitenant.py#L334) | 334 | `""` | — |
| [SRC-1521F490CA-L000335](../../tests/test_multitenant.py#L335) | 335 | `""` | — |
| [SRC-1521F490CA-L000336](../../tests/test_multitenant.py#L336) | 336 | `"def test_browser_session_expiry_and_explicit_logout_are_enforced(tmp_path):"` | — |
| [SRC-1521F490CA-L000337](../../tests/test_multitenant.py#L337) | 337 | `"    store = LeadStore(tmp_path / \"browser-session-expiry.sqlite3\")"` | — |
| [SRC-1521F490CA-L000338](../../tests/test_multitenant.py#L338) | 338 | `"    shared_token = \"shared-browser-session-token-\" + \"X\" * 32"` | — |
| [SRC-1521F490CA-L000339](../../tests/test_multitenant.py#L339) | 339 | `"    session = store.create_web_session(shared_token, shared_token=shared_token)"` | — |
| [SRC-1521F490CA-L000340](../../tests/test_multitenant.py#L340) | 340 | `"    assert session is not None"` | — |
| [SRC-1521F490CA-L000341](../../tests/test_multitenant.py#L341) | 341 | `"    session_id, principal = session"` | — |
| [SRC-1521F490CA-L000342](../../tests/test_multitenant.py#L342) | 342 | `"    assert principal[\"role\"] == \"owner\""` | — |
| [SRC-1521F490CA-L000343](../../tests/test_multitenant.py#L343) | 343 | `"    assert store.resolve_web_session(session_id, shared_token=shared_token) == principal"` | — |
| [SRC-1521F490CA-L000344](../../tests/test_multitenant.py#L344) | 344 | `""` | — |
| [SRC-1521F490CA-L000345](../../tests/test_multitenant.py#L345) | 345 | `"    with store.connect() as db:"` | — |
| [SRC-1521F490CA-L000346](../../tests/test_multitenant.py#L346) | 346 | `"        db.execute("` | — |
| [SRC-1521F490CA-L000347](../../tests/test_multitenant.py#L347) | 347 | `"            \"UPDATE web_sessions SET expires_at=? WHERE session_hash=?\","` | — |
| [SRC-1521F490CA-L000348](../../tests/test_multitenant.py#L348) | 348 | `"            (\"2000-01-01T00:00:00Z\", store._token_hash(session_id)),"` | — |
| [SRC-1521F490CA-L000349](../../tests/test_multitenant.py#L349) | 349 | `"        )"` | — |
| [SRC-1521F490CA-L000350](../../tests/test_multitenant.py#L350) | 350 | `"    assert store.resolve_web_session(session_id, shared_token=shared_token) is None"` | — |
| [SRC-1521F490CA-L000351](../../tests/test_multitenant.py#L351) | 351 | `""` | — |
| [SRC-1521F490CA-L000352](../../tests/test_multitenant.py#L352) | 352 | `"    fresh = store.create_web_session(shared_token, shared_token=shared_token)"` | — |
| [SRC-1521F490CA-L000353](../../tests/test_multitenant.py#L353) | 353 | `"    assert fresh is not None"` | — |
| [SRC-1521F490CA-L000354](../../tests/test_multitenant.py#L354) | 354 | `"    fresh_id, fresh_principal = fresh"` | — |
| [SRC-1521F490CA-L000355](../../tests/test_multitenant.py#L355) | 355 | `"    assert store.revoke_web_session(fresh_id) is True"` | — |
| [SRC-1521F490CA-L000356](../../tests/test_multitenant.py#L356) | 356 | `"    assert store.resolve_web_session(fresh_id, shared_token=shared_token) is None"` | — |
| [SRC-1521F490CA-L000357](../../tests/test_multitenant.py#L357) | 357 | `"    assert fresh_principal[\"role\"] == \"owner\""` | — |
| [SRC-1521F490CA-L000358](../../tests/test_multitenant.py#L358) | 358 | `""` | — |
| [SRC-1521F490CA-L000359](../../tests/test_multitenant.py#L359) | 359 | `""` | — |
| [SRC-1521F490CA-L000360](../../tests/test_multitenant.py#L360) | 360 | `"def test_browser_session_invalidates_when_shared_access_token_rotates(tmp_path):"` | — |
| [SRC-1521F490CA-L000361](../../tests/test_multitenant.py#L361) | 361 | `"    store = LeadStore(tmp_path / \"browser-session-rotation.sqlite3\")"` | — |
| [SRC-1521F490CA-L000362](../../tests/test_multitenant.py#L362) | 362 | `"    original = \"original-shared-token-\" + \"O\" * 32"` | — |
| [SRC-1521F490CA-L000363](../../tests/test_multitenant.py#L363) | 363 | `"    replacement = \"replacement-shared-token-\" + \"R\" * 32"` | — |
| [SRC-1521F490CA-L000364](../../tests/test_multitenant.py#L364) | 364 | `"    session = store.create_web_session(original, shared_token=original)"` | — |
| [SRC-1521F490CA-L000365](../../tests/test_multitenant.py#L365) | 365 | `"    assert session is not None"` | — |
| [SRC-1521F490CA-L000366](../../tests/test_multitenant.py#L366) | 366 | `"    session_id, _principal = session"` | — |
| [SRC-1521F490CA-L000367](../../tests/test_multitenant.py#L367) | 367 | `""` | — |
| [SRC-1521F490CA-L000368](../../tests/test_multitenant.py#L368) | 368 | `"    assert store.resolve_web_session(session_id, shared_token=original) is not None"` | — |
| [SRC-1521F490CA-L000369](../../tests/test_multitenant.py#L369) | 369 | `"    assert store.resolve_web_session(session_id, shared_token=replacement) is None"` | — |
| [SRC-1521F490CA-L000370](../../tests/test_multitenant.py#L370) | 370 | `""` | — |
| [SRC-1521F490CA-L000371](../../tests/test_multitenant.py#L371) | 371 | `"def test_new_browser_session_prunes_expired_and_revoked_session_rows(tmp_path):"` | — |
| [SRC-1521F490CA-L000372](../../tests/test_multitenant.py#L372) | 372 | `"    store = LeadStore(tmp_path / \"session-cleanup.sqlite3\")"` | — |
| [SRC-1521F490CA-L000373](../../tests/test_multitenant.py#L373) | 373 | `"    token = \"session-cleanup-test-token-123456789012345\""` | — |
| [SRC-1521F490CA-L000374](../../tests/test_multitenant.py#L374) | 374 | `"    expired_session, _ = store.create_web_session(token, shared_token=token)"` | — |
| [SRC-1521F490CA-L000375](../../tests/test_multitenant.py#L375) | 375 | `"    revoked_session, _ = store.create_web_session(token, shared_token=token)"` | — |
| [SRC-1521F490CA-L000376](../../tests/test_multitenant.py#L376) | 376 | `"    assert store.revoke_web_session(revoked_session)"` | — |
| [SRC-1521F490CA-L000377](../../tests/test_multitenant.py#L377) | 377 | `""` | — |
| [SRC-1521F490CA-L000378](../../tests/test_multitenant.py#L378) | 378 | `"    expired_hash = store._token_hash(expired_session)"` | — |
| [SRC-1521F490CA-L000379](../../tests/test_multitenant.py#L379) | 379 | `"    revoked_hash = store._token_hash(revoked_session)"` | — |
| [SRC-1521F490CA-L000380](../../tests/test_multitenant.py#L380) | 380 | `"    with store.connect() as db:"` | — |
| [SRC-1521F490CA-L000381](../../tests/test_multitenant.py#L381) | 381 | `"        db.execute("` | — |
| [SRC-1521F490CA-L000382](../../tests/test_multitenant.py#L382) | 382 | `"            \"UPDATE web_sessions SET expires_at=? WHERE session_hash=?\","` | — |
| [SRC-1521F490CA-L000383](../../tests/test_multitenant.py#L383) | 383 | `"            (\"2000-01-01T00:00:00Z\", expired_hash),"` | — |
| [SRC-1521F490CA-L000384](../../tests/test_multitenant.py#L384) | 384 | `"        )"` | — |
| [SRC-1521F490CA-L000385](../../tests/test_multitenant.py#L385) | 385 | `""` | — |
| [SRC-1521F490CA-L000386](../../tests/test_multitenant.py#L386) | 386 | `"    active_session, _ = store.create_web_session(token, shared_token=token)"` | — |
| [SRC-1521F490CA-L000387](../../tests/test_multitenant.py#L387) | 387 | `"    active_hash = store._token_hash(active_session)"` | — |
| [SRC-1521F490CA-L000388](../../tests/test_multitenant.py#L388) | 388 | `"    with store.connect() as db:"` | — |
| [SRC-1521F490CA-L000389](../../tests/test_multitenant.py#L389) | 389 | `"        retained_hashes = {"` | — |
| [SRC-1521F490CA-L000390](../../tests/test_multitenant.py#L390) | 390 | `"            row[\"session_hash\"]"` | — |
| [SRC-1521F490CA-L000391](../../tests/test_multitenant.py#L391) | 391 | `"            for row in db.execute(\"SELECT session_hash FROM web_sessions\")"` | — |
| [SRC-1521F490CA-L000392](../../tests/test_multitenant.py#L392) | 392 | `"        }"` | — |
| [SRC-1521F490CA-L000393](../../tests/test_multitenant.py#L393) | 393 | `""` | — |
| [SRC-1521F490CA-L000394](../../tests/test_multitenant.py#L394) | 394 | `"    assert expired_hash not in retained_hashes"` | — |
| [SRC-1521F490CA-L000395](../../tests/test_multitenant.py#L395) | 395 | `"    assert revoked_hash not in retained_hashes"` | — |
| [SRC-1521F490CA-L000396](../../tests/test_multitenant.py#L396) | 396 | `"    assert active_hash in retained_hashes"` | — |
| [SRC-1521F490CA-L000397](../../tests/test_multitenant.py#L397) | 397 | `""` | — |
## اختبارات

### FILE-4405E7912C — [tests/test_multitenant_api.py](../../tests/test_multitenant_api.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-4405E7912C-L000001](../../tests/test_multitenant_api.py#L1) | 1 | `"\"\"\"HTTP-level tenant authorization regression tests.\"\"\""` | — |
| [SRC-4405E7912C-L000002](../../tests/test_multitenant_api.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-4405E7912C-L000003](../../tests/test_multitenant_api.py#L3) | 3 | `""` | — |
| [SRC-4405E7912C-L000004](../../tests/test_multitenant_api.py#L4) | 4 | `"import json"` | — |
| [SRC-4405E7912C-L000005](../../tests/test_multitenant_api.py#L5) | 5 | `"import threading"` | — |
| [SRC-4405E7912C-L000006](../../tests/test_multitenant_api.py#L6) | 6 | `"from collections import defaultdict, deque"` | — |
| [SRC-4405E7912C-L000007](../../tests/test_multitenant_api.py#L7) | 7 | `"from http.server import ThreadingHTTPServer"` | — |
| [SRC-4405E7912C-L000008](../../tests/test_multitenant_api.py#L8) | 8 | `"from urllib.error import HTTPError"` | — |
| [SRC-4405E7912C-L000009](../../tests/test_multitenant_api.py#L9) | 9 | `"from urllib.request import Request, urlopen"` | — |
| [SRC-4405E7912C-L000010](../../tests/test_multitenant_api.py#L10) | 10 | `""` | — |
| [SRC-4405E7912C-L000011](../../tests/test_multitenant_api.py#L11) | 11 | `"import pytest"` | — |
| [SRC-4405E7912C-L000012](../../tests/test_multitenant_api.py#L12) | 12 | `""` | — |
| [SRC-4405E7912C-L000013](../../tests/test_multitenant_api.py#L13) | 13 | `"from agents.omarai import LeadStore"` | — |
| [SRC-4405E7912C-L000014](../../tests/test_multitenant_api.py#L14) | 14 | `"from api.omarai import Handler"` | — |
| [SRC-4405E7912C-L000015](../../tests/test_multitenant_api.py#L15) | 15 | `""` | — |
| [SRC-4405E7912C-L000016](../../tests/test_multitenant_api.py#L16) | 16 | `""` | — |
| [SRC-4405E7912C-L000017](../../tests/test_multitenant_api.py#L17) | 17 | `"@pytest.fixture"` | — |
| [SRC-4405E7912C-L000018](../../tests/test_multitenant_api.py#L18) | 18 | `"def tenant_api(tmp_path, monkeypatch):"` | — |
| [SRC-4405E7912C-L000019](../../tests/test_multitenant_api.py#L19) | 19 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-4405E7912C-L000020](../../tests/test_multitenant_api.py#L20) | 20 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-4405E7912C-L000021](../../tests/test_multitenant_api.py#L21) | 21 | `"    previous_store = Handler.store"` | — |
| [SRC-4405E7912C-L000022](../../tests/test_multitenant_api.py#L22) | 22 | `"    previous_request_times = Handler._request_times"` | — |
| [SRC-4405E7912C-L000023](../../tests/test_multitenant_api.py#L23) | 23 | `"    previous_rate_cleanup = Handler._rate_last_cleanup"` | — |
| [SRC-4405E7912C-L000024](../../tests/test_multitenant_api.py#L24) | 24 | `"    Handler._request_times = defaultdict(deque)"` | — |
| [SRC-4405E7912C-L000025](../../tests/test_multitenant_api.py#L25) | 25 | `"    Handler._rate_last_cleanup = 0.0"` | — |
| [SRC-4405E7912C-L000026](../../tests/test_multitenant_api.py#L26) | 26 | `"    Handler.store = LeadStore(tmp_path / \"tenant-api.sqlite3\")"` | — |
| [SRC-4405E7912C-L000027](../../tests/test_multitenant_api.py#L27) | 27 | `"    server = ThreadingHTTPServer((\"127.0.0.1\", 0), Handler)"` | — |
| [SRC-4405E7912C-L000028](../../tests/test_multitenant_api.py#L28) | 28 | `"    thread = threading.Thread(target=server.serve_forever, daemon=True)"` | — |
| [SRC-4405E7912C-L000029](../../tests/test_multitenant_api.py#L29) | 29 | `"    thread.start()"` | — |
| [SRC-4405E7912C-L000030](../../tests/test_multitenant_api.py#L30) | 30 | `"    try:"` | — |
| [SRC-4405E7912C-L000031](../../tests/test_multitenant_api.py#L31) | 31 | `"        yield f\"http://127.0.0.1:{server.server_port}\", Handler.store"` | — |
| [SRC-4405E7912C-L000032](../../tests/test_multitenant_api.py#L32) | 32 | `"    finally:"` | — |
| [SRC-4405E7912C-L000033](../../tests/test_multitenant_api.py#L33) | 33 | `"        server.shutdown()"` | — |
| [SRC-4405E7912C-L000034](../../tests/test_multitenant_api.py#L34) | 34 | `"        server.server_close()"` | — |
| [SRC-4405E7912C-L000035](../../tests/test_multitenant_api.py#L35) | 35 | `"        thread.join(timeout=3)"` | — |
| [SRC-4405E7912C-L000036](../../tests/test_multitenant_api.py#L36) | 36 | `"        Handler.store = previous_store"` | — |
| [SRC-4405E7912C-L000037](../../tests/test_multitenant_api.py#L37) | 37 | `"        Handler._request_times = previous_request_times"` | — |
| [SRC-4405E7912C-L000038](../../tests/test_multitenant_api.py#L38) | 38 | `"        Handler._rate_last_cleanup = previous_rate_cleanup"` | — |
| [SRC-4405E7912C-L000039](../../tests/test_multitenant_api.py#L39) | 39 | `""` | — |
| [SRC-4405E7912C-L000040](../../tests/test_multitenant_api.py#L40) | 40 | `""` | — |
| [SRC-4405E7912C-L000041](../../tests/test_multitenant_api.py#L41) | 41 | `"def request_json(base, path, *, method=\"GET\", payload=None, token=\"\"):"` | — |
| [SRC-4405E7912C-L000042](../../tests/test_multitenant_api.py#L42) | 42 | `"    body = None if payload is None else json.dumps(payload).encode(\"utf-8\")"` | — |
| [SRC-4405E7912C-L000043](../../tests/test_multitenant_api.py#L43) | 43 | `"    headers = {}"` | — |
| [SRC-4405E7912C-L000044](../../tests/test_multitenant_api.py#L44) | 44 | `"    if body is not None:"` | — |
| [SRC-4405E7912C-L000045](../../tests/test_multitenant_api.py#L45) | 45 | `"        headers[\"Content-Type\"] = \"application/json\""` | — |
| [SRC-4405E7912C-L000046](../../tests/test_multitenant_api.py#L46) | 46 | `"    if token:"` | — |
| [SRC-4405E7912C-L000047](../../tests/test_multitenant_api.py#L47) | 47 | `"        headers[\"Authorization\"] = \"Bearer \" + token"` | — |
| [SRC-4405E7912C-L000048](../../tests/test_multitenant_api.py#L48) | 48 | `"    request = Request(base + path, data=body, method=method, headers=headers)"` | — |
| [SRC-4405E7912C-L000049](../../tests/test_multitenant_api.py#L49) | 49 | `"    try:"` | — |
| [SRC-4405E7912C-L000050](../../tests/test_multitenant_api.py#L50) | 50 | `"        with urlopen(request, timeout=3) as response:"` | — |
| [SRC-4405E7912C-L000051](../../tests/test_multitenant_api.py#L51) | 51 | `"            return response.status, json.loads(response.read().decode(\"utf-8\"))"` | — |
| [SRC-4405E7912C-L000052](../../tests/test_multitenant_api.py#L52) | 52 | `"    except HTTPError as error:"` | — |
| [SRC-4405E7912C-L000053](../../tests/test_multitenant_api.py#L53) | 53 | `"        return error.code, json.loads(error.read().decode(\"utf-8\"))"` | — |
| [SRC-4405E7912C-L000054](../../tests/test_multitenant_api.py#L54) | 54 | `""` | — |
| [SRC-4405E7912C-L000055](../../tests/test_multitenant_api.py#L55) | 55 | `""` | — |
| [SRC-4405E7912C-L000056](../../tests/test_multitenant_api.py#L56) | 56 | `"def _tenant(store, name, email, token):"` | — |
| [SRC-4405E7912C-L000057](../../tests/test_multitenant_api.py#L57) | 57 | `"    tenant_id = store.create_tenant(name, name.casefold())"` | — |
| [SRC-4405E7912C-L000058](../../tests/test_multitenant_api.py#L58) | 58 | `"    user_id = store.create_user(email, name + \" User\")"` | — |
| [SRC-4405E7912C-L000059](../../tests/test_multitenant_api.py#L59) | 59 | `"    store.add_membership(tenant_id, user_id, \"sales_agent\")"` | — |
| [SRC-4405E7912C-L000060](../../tests/test_multitenant_api.py#L60) | 60 | `"    store.create_api_token(token, tenant_id, user_id, label=name)"` | — |
| [SRC-4405E7912C-L000061](../../tests/test_multitenant_api.py#L61) | 61 | `"    return tenant_id"` | — |
| [SRC-4405E7912C-L000062](../../tests/test_multitenant_api.py#L62) | 62 | `""` | — |
| [SRC-4405E7912C-L000063](../../tests/test_multitenant_api.py#L63) | 63 | `""` | — |
| [SRC-4405E7912C-L000064](../../tests/test_multitenant_api.py#L64) | 64 | `"def test_api_ignores_client_tenant_id_and_blocks_cross_tenant_reads_and_updates(tenant_api):"` | — |
| [SRC-4405E7912C-L000065](../../tests/test_multitenant_api.py#L65) | 65 | `"    base, store = tenant_api"` | — |
| [SRC-4405E7912C-L000066](../../tests/test_multitenant_api.py#L66) | 66 | `"    token_a = \"tenant-a-token-\" + \"A\" * 32"` | — |
| [SRC-4405E7912C-L000067](../../tests/test_multitenant_api.py#L67) | 67 | `"    token_b = \"tenant-b-token-\" + \"B\" * 32"` | — |
| [SRC-4405E7912C-L000068](../../tests/test_multitenant_api.py#L68) | 68 | `"    tenant_a = _tenant(store, \"Company A\", \"api-a@example.test\", token_a)"` | — |
| [SRC-4405E7912C-L000069](../../tests/test_multitenant_api.py#L69) | 69 | `"    tenant_b = _tenant(store, \"Company B\", \"api-b@example.test\", token_b)"` | — |
| [SRC-4405E7912C-L000070](../../tests/test_multitenant_api.py#L70) | 70 | `""` | — |
| [SRC-4405E7912C-L000071](../../tests/test_multitenant_api.py#L71) | 71 | `"    status, created_a = request_json("` | — |
| [SRC-4405E7912C-L000072](../../tests/test_multitenant_api.py#L72) | 72 | `"        base,"` | — |
| [SRC-4405E7912C-L000073](../../tests/test_multitenant_api.py#L73) | 73 | `"        \"/api/leads\","` | — |
| [SRC-4405E7912C-L000074](../../tests/test_multitenant_api.py#L74) | 74 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000075](../../tests/test_multitenant_api.py#L75) | 75 | `"        token=token_a,"` | — |
| [SRC-4405E7912C-L000076](../../tests/test_multitenant_api.py#L76) | 76 | `"        payload={"` | — |
| [SRC-4405E7912C-L000077](../../tests/test_multitenant_api.py#L77) | 77 | `"            \"tenant_id\": tenant_b,"` | — |
| [SRC-4405E7912C-L000078](../../tests/test_multitenant_api.py#L78) | 78 | `"            \"text\": \"Buyer A wants to purchase\","` | — |
| [SRC-4405E7912C-L000079](../../tests/test_multitenant_api.py#L79) | 79 | `"            \"source_url\": \"https://example.test/a\","` | — |
| [SRC-4405E7912C-L000080](../../tests/test_multitenant_api.py#L80) | 80 | `"            \"platform\": \"public\","` | — |
| [SRC-4405E7912C-L000081](../../tests/test_multitenant_api.py#L81) | 81 | `"        },"` | — |
| [SRC-4405E7912C-L000082](../../tests/test_multitenant_api.py#L82) | 82 | `"    )"` | — |
| [SRC-4405E7912C-L000083](../../tests/test_multitenant_api.py#L83) | 83 | `"    assert status == 201"` | — |
| [SRC-4405E7912C-L000084](../../tests/test_multitenant_api.py#L84) | 84 | `"    assert created_a[\"lead\"][\"tenant_id\"] == tenant_a"` | — |
| [SRC-4405E7912C-L000085](../../tests/test_multitenant_api.py#L85) | 85 | `""` | — |
| [SRC-4405E7912C-L000086](../../tests/test_multitenant_api.py#L86) | 86 | `"    status, created_b = request_json("` | — |
| [SRC-4405E7912C-L000087](../../tests/test_multitenant_api.py#L87) | 87 | `"        base,"` | — |
| [SRC-4405E7912C-L000088](../../tests/test_multitenant_api.py#L88) | 88 | `"        \"/api/leads\","` | — |
| [SRC-4405E7912C-L000089](../../tests/test_multitenant_api.py#L89) | 89 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000090](../../tests/test_multitenant_api.py#L90) | 90 | `"        token=token_b,"` | — |
| [SRC-4405E7912C-L000091](../../tests/test_multitenant_api.py#L91) | 91 | `"        payload={"` | — |
| [SRC-4405E7912C-L000092](../../tests/test_multitenant_api.py#L92) | 92 | `"            \"tenant_id\": tenant_a,"` | — |
| [SRC-4405E7912C-L000093](../../tests/test_multitenant_api.py#L93) | 93 | `"            \"text\": \"Buyer B wants to purchase\","` | — |
| [SRC-4405E7912C-L000094](../../tests/test_multitenant_api.py#L94) | 94 | `"            \"source_url\": \"https://example.test/b\","` | — |
| [SRC-4405E7912C-L000095](../../tests/test_multitenant_api.py#L95) | 95 | `"            \"platform\": \"public\","` | — |
| [SRC-4405E7912C-L000096](../../tests/test_multitenant_api.py#L96) | 96 | `"        },"` | — |
| [SRC-4405E7912C-L000097](../../tests/test_multitenant_api.py#L97) | 97 | `"    )"` | — |
| [SRC-4405E7912C-L000098](../../tests/test_multitenant_api.py#L98) | 98 | `"    assert status == 201"` | — |
| [SRC-4405E7912C-L000099](../../tests/test_multitenant_api.py#L99) | 99 | `"    assert created_b[\"lead\"][\"tenant_id\"] == tenant_b"` | — |
| [SRC-4405E7912C-L000100](../../tests/test_multitenant_api.py#L100) | 100 | `""` | — |
| [SRC-4405E7912C-L000101](../../tests/test_multitenant_api.py#L101) | 101 | `"    status, listing_a = request_json("` | — |
| [SRC-4405E7912C-L000102](../../tests/test_multitenant_api.py#L102) | 102 | `"        base, f\"/api/leads?tenant_id={tenant_b}\", token=token_a"` | — |
| [SRC-4405E7912C-L000103](../../tests/test_multitenant_api.py#L103) | 103 | `"    )"` | — |
| [SRC-4405E7912C-L000104](../../tests/test_multitenant_api.py#L104) | 104 | `"    assert status == 200"` | — |
| [SRC-4405E7912C-L000105](../../tests/test_multitenant_api.py#L105) | 105 | `"    assert [lead[\"id\"] for lead in listing_a[\"leads\"]] == [created_a[\"lead\"][\"id\"]]"` | — |
| [SRC-4405E7912C-L000106](../../tests/test_multitenant_api.py#L106) | 106 | `""` | — |
| [SRC-4405E7912C-L000107](../../tests/test_multitenant_api.py#L107) | 107 | `"    status, listing_b = request_json(base, \"/api/leads\", token=token_b)"` | — |
| [SRC-4405E7912C-L000108](../../tests/test_multitenant_api.py#L108) | 108 | `"    assert status == 200"` | — |
| [SRC-4405E7912C-L000109](../../tests/test_multitenant_api.py#L109) | 109 | `"    assert [lead[\"id\"] for lead in listing_b[\"leads\"]] == [created_b[\"lead\"][\"id\"]]"` | — |
| [SRC-4405E7912C-L000110](../../tests/test_multitenant_api.py#L110) | 110 | `""` | — |
| [SRC-4405E7912C-L000111](../../tests/test_multitenant_api.py#L111) | 111 | `"    status, denied = request_json("` | — |
| [SRC-4405E7912C-L000112](../../tests/test_multitenant_api.py#L112) | 112 | `"        base,"` | — |
| [SRC-4405E7912C-L000113](../../tests/test_multitenant_api.py#L113) | 113 | `"        f\"/api/leads/{created_b['lead']['id']}/status\","` | — |
| [SRC-4405E7912C-L000114](../../tests/test_multitenant_api.py#L114) | 114 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000115](../../tests/test_multitenant_api.py#L115) | 115 | `"        token=token_a,"` | — |
| [SRC-4405E7912C-L000116](../../tests/test_multitenant_api.py#L116) | 116 | `"        payload={\"status\": \"qualified\"},"` | — |
| [SRC-4405E7912C-L000117](../../tests/test_multitenant_api.py#L117) | 117 | `"    )"` | — |
| [SRC-4405E7912C-L000118](../../tests/test_multitenant_api.py#L118) | 118 | `"    assert status == 404"` | — |
| [SRC-4405E7912C-L000119](../../tests/test_multitenant_api.py#L119) | 119 | `"    assert denied[\"error\"] == \"lead not found\""` | — |
| [SRC-4405E7912C-L000120](../../tests/test_multitenant_api.py#L120) | 120 | `""` | — |
| [SRC-4405E7912C-L000121](../../tests/test_multitenant_api.py#L121) | 121 | `"    status, changed = request_json("` | — |
| [SRC-4405E7912C-L000122](../../tests/test_multitenant_api.py#L122) | 122 | `"        base,"` | — |
| [SRC-4405E7912C-L000123](../../tests/test_multitenant_api.py#L123) | 123 | `"        f\"/api/leads/{created_b['lead']['id']}/status\","` | — |
| [SRC-4405E7912C-L000124](../../tests/test_multitenant_api.py#L124) | 124 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000125](../../tests/test_multitenant_api.py#L125) | 125 | `"        token=token_b,"` | — |
| [SRC-4405E7912C-L000126](../../tests/test_multitenant_api.py#L126) | 126 | `"        payload={\"status\": \"qualified\"},"` | — |
| [SRC-4405E7912C-L000127](../../tests/test_multitenant_api.py#L127) | 127 | `"    )"` | — |
| [SRC-4405E7912C-L000128](../../tests/test_multitenant_api.py#L128) | 128 | `"    assert status == 200"` | — |
| [SRC-4405E7912C-L000129](../../tests/test_multitenant_api.py#L129) | 129 | `"    assert changed[\"lead\"][\"status\"] == \"qualified\""` | — |
| [SRC-4405E7912C-L000130](../../tests/test_multitenant_api.py#L130) | 130 | `""` | — |
| [SRC-4405E7912C-L000131](../../tests/test_multitenant_api.py#L131) | 131 | `""` | — |
| [SRC-4405E7912C-L000132](../../tests/test_multitenant_api.py#L132) | 132 | `"def test_public_api_rejects_unknown_token(tenant_api):"` | — |
| [SRC-4405E7912C-L000133](../../tests/test_multitenant_api.py#L133) | 133 | `"    base, _ = tenant_api"` | — |
| [SRC-4405E7912C-L000134](../../tests/test_multitenant_api.py#L134) | 134 | `"    status, error = request_json("` | — |
| [SRC-4405E7912C-L000135](../../tests/test_multitenant_api.py#L135) | 135 | `"        base,"` | — |
| [SRC-4405E7912C-L000136](../../tests/test_multitenant_api.py#L136) | 136 | `"        \"/api/leads\","` | — |
| [SRC-4405E7912C-L000137](../../tests/test_multitenant_api.py#L137) | 137 | `"        token=\"unknown-token-\" + \"X\" * 32,"` | — |
| [SRC-4405E7912C-L000138](../../tests/test_multitenant_api.py#L138) | 138 | `"    )"` | — |
| [SRC-4405E7912C-L000139](../../tests/test_multitenant_api.py#L139) | 139 | `"    assert status == 401"` | — |
| [SRC-4405E7912C-L000140](../../tests/test_multitenant_api.py#L140) | 140 | `"    assert \"رمز الوصول\" in error[\"error\"]"` | — |
| [SRC-4405E7912C-L000141](../../tests/test_multitenant_api.py#L141) | 141 | `""` | — |
| [SRC-4405E7912C-L000142](../../tests/test_multitenant_api.py#L142) | 142 | `""` | — |
| [SRC-4405E7912C-L000143](../../tests/test_multitenant_api.py#L143) | 143 | `"def test_viewer_membership_is_read_only(tenant_api):"` | — |
| [SRC-4405E7912C-L000144](../../tests/test_multitenant_api.py#L144) | 144 | `"    base, store = tenant_api"` | — |
| [SRC-4405E7912C-L000145](../../tests/test_multitenant_api.py#L145) | 145 | `"    tenant_id = store.create_tenant(\"Read Only Company\", \"read-only-company\")"` | — |
| [SRC-4405E7912C-L000146](../../tests/test_multitenant_api.py#L146) | 146 | `"    user_id = store.create_user(\"viewer@example.test\", \"Viewer\")"` | — |
| [SRC-4405E7912C-L000147](../../tests/test_multitenant_api.py#L147) | 147 | `"    store.add_membership(tenant_id, user_id, \"viewer\")"` | — |
| [SRC-4405E7912C-L000148](../../tests/test_multitenant_api.py#L148) | 148 | `"    token = \"viewer-token-\" + \"V\" * 32"` | — |
| [SRC-4405E7912C-L000149](../../tests/test_multitenant_api.py#L149) | 149 | `"    store.create_api_token(token, tenant_id, user_id, label=\"viewer\")"` | — |
| [SRC-4405E7912C-L000150](../../tests/test_multitenant_api.py#L150) | 150 | `""` | — |
| [SRC-4405E7912C-L000151](../../tests/test_multitenant_api.py#L151) | 151 | `"    status, listing = request_json(base, \"/api/leads\", token=token)"` | — |
| [SRC-4405E7912C-L000152](../../tests/test_multitenant_api.py#L152) | 152 | `"    assert status == 200"` | — |
| [SRC-4405E7912C-L000153](../../tests/test_multitenant_api.py#L153) | 153 | `"    assert listing[\"count\"] == 0"` | — |
| [SRC-4405E7912C-L000154](../../tests/test_multitenant_api.py#L154) | 154 | `""` | — |
| [SRC-4405E7912C-L000155](../../tests/test_multitenant_api.py#L155) | 155 | `"    status, error = request_json("` | — |
| [SRC-4405E7912C-L000156](../../tests/test_multitenant_api.py#L156) | 156 | `"        base,"` | — |
| [SRC-4405E7912C-L000157](../../tests/test_multitenant_api.py#L157) | 157 | `"        \"/api/leads\","` | — |
| [SRC-4405E7912C-L000158](../../tests/test_multitenant_api.py#L158) | 158 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000159](../../tests/test_multitenant_api.py#L159) | 159 | `"        token=token,"` | — |
| [SRC-4405E7912C-L000160](../../tests/test_multitenant_api.py#L160) | 160 | `"        payload={"` | — |
| [SRC-4405E7912C-L000161](../../tests/test_multitenant_api.py#L161) | 161 | `"            \"text\": \"Viewer must not write\","` | — |
| [SRC-4405E7912C-L000162](../../tests/test_multitenant_api.py#L162) | 162 | `"            \"source_url\": \"https://example.test/viewer\","` | — |
| [SRC-4405E7912C-L000163](../../tests/test_multitenant_api.py#L163) | 163 | `"        },"` | — |
| [SRC-4405E7912C-L000164](../../tests/test_multitenant_api.py#L164) | 164 | `"    )"` | — |
| [SRC-4405E7912C-L000165](../../tests/test_multitenant_api.py#L165) | 165 | `"    assert status == 403"` | — |
| [SRC-4405E7912C-L000166](../../tests/test_multitenant_api.py#L166) | 166 | `"    assert \"للقراءة فقط\" in error[\"error\"]"` | — |
| [SRC-4405E7912C-L000167](../../tests/test_multitenant_api.py#L167) | 167 | `""` | — |
| [SRC-4405E7912C-L000168](../../tests/test_multitenant_api.py#L168) | 168 | `""` | — |
| [SRC-4405E7912C-L000169](../../tests/test_multitenant_api.py#L169) | 169 | `""` | — |
| [SRC-4405E7912C-L000170](../../tests/test_multitenant_api.py#L170) | 170 | `"def test_api_revokes_only_the_authenticated_api_token(tenant_api):"` | — |
| [SRC-4405E7912C-L000171](../../tests/test_multitenant_api.py#L171) | 171 | `"    base, store = tenant_api"` | — |
| [SRC-4405E7912C-L000172](../../tests/test_multitenant_api.py#L172) | 172 | `"    tenant_id = store.create_tenant(\"Revocable Company\", \"revocable-company\")"` | — |
| [SRC-4405E7912C-L000173](../../tests/test_multitenant_api.py#L173) | 173 | `"    user_id = store.create_user(\"revoker@example.test\", \"Token Owner\")"` | — |
| [SRC-4405E7912C-L000174](../../tests/test_multitenant_api.py#L174) | 174 | `"    store.add_membership(tenant_id, user_id, \"owner\")"` | — |
| [SRC-4405E7912C-L000175](../../tests/test_multitenant_api.py#L175) | 175 | `"    token = \"revocable-token-\" + \"R\" * 32"` | — |
| [SRC-4405E7912C-L000176](../../tests/test_multitenant_api.py#L176) | 176 | `"    store.create_api_token(token, tenant_id, user_id)"` | — |
| [SRC-4405E7912C-L000177](../../tests/test_multitenant_api.py#L177) | 177 | `""` | — |
| [SRC-4405E7912C-L000178](../../tests/test_multitenant_api.py#L178) | 178 | `"    status, result = request_json("` | — |
| [SRC-4405E7912C-L000179](../../tests/test_multitenant_api.py#L179) | 179 | `"        base, \"/api/tokens/revoke\", method=\"POST\", token=token, payload={}"` | — |
| [SRC-4405E7912C-L000180](../../tests/test_multitenant_api.py#L180) | 180 | `"    )"` | — |
| [SRC-4405E7912C-L000181](../../tests/test_multitenant_api.py#L181) | 181 | `"    assert status == 200"` | — |
| [SRC-4405E7912C-L000182](../../tests/test_multitenant_api.py#L182) | 182 | `"    assert result == {\"revoked\": True}"` | — |
| [SRC-4405E7912C-L000183](../../tests/test_multitenant_api.py#L183) | 183 | `""` | — |
| [SRC-4405E7912C-L000184](../../tests/test_multitenant_api.py#L184) | 184 | `"    status, denied = request_json(base, \"/api/leads\", token=token)"` | — |
| [SRC-4405E7912C-L000185](../../tests/test_multitenant_api.py#L185) | 185 | `"    assert status == 401"` | — |
| [SRC-4405E7912C-L000186](../../tests/test_multitenant_api.py#L186) | 186 | `"    assert \"رمز الوصول\" in denied[\"error\"]"` | — |
| [SRC-4405E7912C-L000187](../../tests/test_multitenant_api.py#L187) | 187 | `""` | — |
| [SRC-4405E7912C-L000188](../../tests/test_multitenant_api.py#L188) | 188 | `""` | — |
| [SRC-4405E7912C-L000189](../../tests/test_multitenant_api.py#L189) | 189 | `"def test_api_does_not_claim_to_revoke_shared_environment_token("` | — |
| [SRC-4405E7912C-L000190](../../tests/test_multitenant_api.py#L190) | 190 | `"    tenant_api, monkeypatch"` | — |
| [SRC-4405E7912C-L000191](../../tests/test_multitenant_api.py#L191) | 191 | `"):"` | — |
| [SRC-4405E7912C-L000192](../../tests/test_multitenant_api.py#L192) | 192 | `"    base, _ = tenant_api"` | — |
| [SRC-4405E7912C-L000193](../../tests/test_multitenant_api.py#L193) | 193 | `"    shared_token = \"shared-application-token-\" + \"S\" * 32"` | — |
| [SRC-4405E7912C-L000194](../../tests/test_multitenant_api.py#L194) | 194 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", shared_token)"` | — |
| [SRC-4405E7912C-L000195](../../tests/test_multitenant_api.py#L195) | 195 | `""` | — |
| [SRC-4405E7912C-L000196](../../tests/test_multitenant_api.py#L196) | 196 | `"    status, result = request_json("` | — |
| [SRC-4405E7912C-L000197](../../tests/test_multitenant_api.py#L197) | 197 | `"        base,"` | — |
| [SRC-4405E7912C-L000198](../../tests/test_multitenant_api.py#L198) | 198 | `"        \"/api/tokens/revoke\","` | — |
| [SRC-4405E7912C-L000199](../../tests/test_multitenant_api.py#L199) | 199 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000200](../../tests/test_multitenant_api.py#L200) | 200 | `"        token=shared_token,"` | — |
| [SRC-4405E7912C-L000201](../../tests/test_multitenant_api.py#L201) | 201 | `"        payload={},"` | — |
| [SRC-4405E7912C-L000202](../../tests/test_multitenant_api.py#L202) | 202 | `"    )"` | — |
| [SRC-4405E7912C-L000203](../../tests/test_multitenant_api.py#L203) | 203 | `"    assert status == 409"` | — |
| [SRC-4405E7912C-L000204](../../tests/test_multitenant_api.py#L204) | 204 | `"    assert \"rotated by the operator\" in result[\"error\"]"` | — |
| [SRC-4405E7912C-L000205](../../tests/test_multitenant_api.py#L205) | 205 | `""` | — |
| [SRC-4405E7912C-L000206](../../tests/test_multitenant_api.py#L206) | 206 | `""` | — |
| [SRC-4405E7912C-L000207](../../tests/test_multitenant_api.py#L207) | 207 | `""` | — |
| [SRC-4405E7912C-L000208](../../tests/test_multitenant_api.py#L208) | 208 | `"def test_live_diagnostics_requires_explicit_approval_before_any_provider_call("` | — |
| [SRC-4405E7912C-L000209](../../tests/test_multitenant_api.py#L209) | 209 | `"    tenant_api, monkeypatch"` | — |
| [SRC-4405E7912C-L000210](../../tests/test_multitenant_api.py#L210) | 210 | `"):"` | — |
| [SRC-4405E7912C-L000211](../../tests/test_multitenant_api.py#L211) | 211 | `"    from api.omarai import WebAgent"` | — |
| [SRC-4405E7912C-L000212](../../tests/test_multitenant_api.py#L212) | 212 | `""` | — |
| [SRC-4405E7912C-L000213](../../tests/test_multitenant_api.py#L213) | 213 | `"    base, store = tenant_api"` | — |
| [SRC-4405E7912C-L000214](../../tests/test_multitenant_api.py#L214) | 214 | `"    tenant_id = store.create_tenant(\"Diagnostics Owner\", \"diagnostics-owner\")"` | — |
| [SRC-4405E7912C-L000215](../../tests/test_multitenant_api.py#L215) | 215 | `"    user_id = store.create_user(\"diagnostics-owner@example.test\", \"Owner\")"` | — |
| [SRC-4405E7912C-L000216](../../tests/test_multitenant_api.py#L216) | 216 | `"    store.add_membership(tenant_id, user_id, \"owner\")"` | — |
| [SRC-4405E7912C-L000217](../../tests/test_multitenant_api.py#L217) | 217 | `"    token = \"diagnostics-owner-token-\" + \"O\" * 32"` | — |
| [SRC-4405E7912C-L000218](../../tests/test_multitenant_api.py#L218) | 218 | `""` | — |
| [SRC-4405E7912C-L000219](../../tests/test_multitenant_api.py#L219) | 219 | `"    def unexpected_diagnostics(*_args, **_kwargs):"` | — |
| [SRC-4405E7912C-L000220](../../tests/test_multitenant_api.py#L220) | 220 | `"        pytest.fail(\"diagnostics must not run without explicit provider-use approval\")"` | — |
| [SRC-4405E7912C-L000221](../../tests/test_multitenant_api.py#L221) | 221 | `""` | — |
| [SRC-4405E7912C-L000222](../../tests/test_multitenant_api.py#L222) | 222 | `"    store.create_api_token(token, tenant_id, user_id)"` | — |
| [SRC-4405E7912C-L000223](../../tests/test_multitenant_api.py#L223) | 223 | `"    monkeypatch.setattr(WebAgent, \"diagnostics\", unexpected_diagnostics)"` | — |
| [SRC-4405E7912C-L000224](../../tests/test_multitenant_api.py#L224) | 224 | `""` | — |
| [SRC-4405E7912C-L000225](../../tests/test_multitenant_api.py#L225) | 225 | `"    status, result = request_json("` | — |
| [SRC-4405E7912C-L000226](../../tests/test_multitenant_api.py#L226) | 226 | `"        base,"` | — |
| [SRC-4405E7912C-L000227](../../tests/test_multitenant_api.py#L227) | 227 | `"        \"/api/diagnostics\","` | — |
| [SRC-4405E7912C-L000228](../../tests/test_multitenant_api.py#L228) | 228 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000229](../../tests/test_multitenant_api.py#L229) | 229 | `"        token=token,"` | — |
| [SRC-4405E7912C-L000230](../../tests/test_multitenant_api.py#L230) | 230 | `"        payload={\"test_model\": True, \"test_social\": True},"` | — |
| [SRC-4405E7912C-L000231](../../tests/test_multitenant_api.py#L231) | 231 | `"    )"` | — |
| [SRC-4405E7912C-L000232](../../tests/test_multitenant_api.py#L232) | 232 | `"    assert status == 403"` | — |
| [SRC-4405E7912C-L000233](../../tests/test_multitenant_api.py#L233) | 233 | `"    assert \"explicit owner approval\" in result[\"error\"]"` | — |
| [SRC-4405E7912C-L000234](../../tests/test_multitenant_api.py#L234) | 234 | `""` | — |
| [SRC-4405E7912C-L000235](../../tests/test_multitenant_api.py#L235) | 235 | `""` | — |
| [SRC-4405E7912C-L000236](../../tests/test_multitenant_api.py#L236) | 236 | `"def test_live_diagnostics_is_owner_only_even_with_explicit_approval("` | — |
| [SRC-4405E7912C-L000237](../../tests/test_multitenant_api.py#L237) | 237 | `"    tenant_api, monkeypatch"` | — |
| [SRC-4405E7912C-L000238](../../tests/test_multitenant_api.py#L238) | 238 | `"):"` | — |
| [SRC-4405E7912C-L000239](../../tests/test_multitenant_api.py#L239) | 239 | `"    from api.omarai import WebAgent"` | — |
| [SRC-4405E7912C-L000240](../../tests/test_multitenant_api.py#L240) | 240 | `""` | — |
| [SRC-4405E7912C-L000241](../../tests/test_multitenant_api.py#L241) | 241 | `"    base, store = tenant_api"` | — |
| [SRC-4405E7912C-L000242](../../tests/test_multitenant_api.py#L242) | 242 | `"    tenant_id = store.create_tenant(\"Sales Member Diagnostics\", \"sales-member-diagnostics\")"` | — |
| [SRC-4405E7912C-L000243](../../tests/test_multitenant_api.py#L243) | 243 | `"    user_id = store.create_user(\"sales-member@example.test\", \"Sales Member\")"` | — |
| [SRC-4405E7912C-L000244](../../tests/test_multitenant_api.py#L244) | 244 | `"    store.add_membership(tenant_id, user_id, \"sales_agent\")"` | — |
| [SRC-4405E7912C-L000245](../../tests/test_multitenant_api.py#L245) | 245 | `"    token = \"sales-member-diagnostics-token-\" + \"S\" * 32"` | — |
| [SRC-4405E7912C-L000246](../../tests/test_multitenant_api.py#L246) | 246 | `""` | — |
| [SRC-4405E7912C-L000247](../../tests/test_multitenant_api.py#L247) | 247 | `"    def unexpected_diagnostics(*_args, **_kwargs):"` | — |
| [SRC-4405E7912C-L000248](../../tests/test_multitenant_api.py#L248) | 248 | `"        pytest.fail(\"non-owner diagnostics must be rejected before provider calls\")"` | — |
| [SRC-4405E7912C-L000249](../../tests/test_multitenant_api.py#L249) | 249 | `""` | — |
| [SRC-4405E7912C-L000250](../../tests/test_multitenant_api.py#L250) | 250 | `"    store.create_api_token(token, tenant_id, user_id)"` | — |
| [SRC-4405E7912C-L000251](../../tests/test_multitenant_api.py#L251) | 251 | `"    monkeypatch.setattr(WebAgent, \"diagnostics\", unexpected_diagnostics)"` | — |
| [SRC-4405E7912C-L000252](../../tests/test_multitenant_api.py#L252) | 252 | `""` | — |
| [SRC-4405E7912C-L000253](../../tests/test_multitenant_api.py#L253) | 253 | `"    status, result = request_json("` | — |
| [SRC-4405E7912C-L000254](../../tests/test_multitenant_api.py#L254) | 254 | `"        base,"` | — |
| [SRC-4405E7912C-L000255](../../tests/test_multitenant_api.py#L255) | 255 | `"        \"/api/diagnostics\","` | — |
| [SRC-4405E7912C-L000256](../../tests/test_multitenant_api.py#L256) | 256 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000257](../../tests/test_multitenant_api.py#L257) | 257 | `"        token=token,"` | — |
| [SRC-4405E7912C-L000258](../../tests/test_multitenant_api.py#L258) | 258 | `"        payload={"` | — |
| [SRC-4405E7912C-L000259](../../tests/test_multitenant_api.py#L259) | 259 | `"            \"test_model\": True,"` | — |
| [SRC-4405E7912C-L000260](../../tests/test_multitenant_api.py#L260) | 260 | `"            \"test_social\": True,"` | — |
| [SRC-4405E7912C-L000261](../../tests/test_multitenant_api.py#L261) | 261 | `"            \"allow_provider_usage\": True,"` | — |
| [SRC-4405E7912C-L000262](../../tests/test_multitenant_api.py#L262) | 262 | `"        },"` | — |
| [SRC-4405E7912C-L000263](../../tests/test_multitenant_api.py#L263) | 263 | `"    )"` | — |
| [SRC-4405E7912C-L000264](../../tests/test_multitenant_api.py#L264) | 264 | `"    assert status == 403"` | — |
| [SRC-4405E7912C-L000265](../../tests/test_multitenant_api.py#L265) | 265 | `"    assert \"مالك مساحة العمل\" in result[\"error\"]"` | — |
| [SRC-4405E7912C-L000266](../../tests/test_multitenant_api.py#L266) | 266 | `""` | — |
| [SRC-4405E7912C-L000267](../../tests/test_multitenant_api.py#L267) | 267 | `""` | — |
| [SRC-4405E7912C-L000268](../../tests/test_multitenant_api.py#L268) | 268 | `"def test_owner_can_run_diagnostics_only_after_explicit_approval("` | — |
| [SRC-4405E7912C-L000269](../../tests/test_multitenant_api.py#L269) | 269 | `"    tenant_api, monkeypatch"` | — |
| [SRC-4405E7912C-L000270](../../tests/test_multitenant_api.py#L270) | 270 | `"):"` | — |
| [SRC-4405E7912C-L000271](../../tests/test_multitenant_api.py#L271) | 271 | `"    from api.omarai import WebAgent"` | — |
| [SRC-4405E7912C-L000272](../../tests/test_multitenant_api.py#L272) | 272 | `""` | — |
| [SRC-4405E7912C-L000273](../../tests/test_multitenant_api.py#L273) | 273 | `"    base, store = tenant_api"` | — |
| [SRC-4405E7912C-L000274](../../tests/test_multitenant_api.py#L274) | 274 | `"    tenant_id = store.create_tenant(\"Approved Diagnostics\", \"approved-diagnostics\")"` | — |
| [SRC-4405E7912C-L000275](../../tests/test_multitenant_api.py#L275) | 275 | `"    user_id = store.create_user(\"approved-owner@example.test\", \"Owner\")"` | — |
| [SRC-4405E7912C-L000276](../../tests/test_multitenant_api.py#L276) | 276 | `"    store.add_membership(tenant_id, user_id, \"owner\")"` | — |
| [SRC-4405E7912C-L000277](../../tests/test_multitenant_api.py#L277) | 277 | `"    token = \"approved-diagnostics-token-\" + \"A\" * 32"` | — |
| [SRC-4405E7912C-L000278](../../tests/test_multitenant_api.py#L278) | 278 | `"    store.create_api_token(token, tenant_id, user_id)"` | — |
| [SRC-4405E7912C-L000279](../../tests/test_multitenant_api.py#L279) | 279 | `"    observed = {}"` | — |
| [SRC-4405E7912C-L000280](../../tests/test_multitenant_api.py#L280) | 280 | `""` | — |
| [SRC-4405E7912C-L000281](../../tests/test_multitenant_api.py#L281) | 281 | `"    def fake_diagnostics(self, *, test_model, test_social):"` | — |
| [SRC-4405E7912C-L000282](../../tests/test_multitenant_api.py#L282) | 282 | `"        observed[\"test_model\"] = test_model"` | — |
| [SRC-4405E7912C-L000283](../../tests/test_multitenant_api.py#L283) | 283 | `"        observed[\"test_social\"] = test_social"` | — |
| [SRC-4405E7912C-L000284](../../tests/test_multitenant_api.py#L284) | 284 | `"        return {\"overall_status\": \"passed\", \"model_usage\": []}"` | — |
| [SRC-4405E7912C-L000285](../../tests/test_multitenant_api.py#L285) | 285 | `""` | — |
| [SRC-4405E7912C-L000286](../../tests/test_multitenant_api.py#L286) | 286 | `"    monkeypatch.setattr(WebAgent, \"diagnostics\", fake_diagnostics)"` | — |
| [SRC-4405E7912C-L000287](../../tests/test_multitenant_api.py#L287) | 287 | `"    status, result = request_json("` | — |
| [SRC-4405E7912C-L000288](../../tests/test_multitenant_api.py#L288) | 288 | `"        base,"` | — |
| [SRC-4405E7912C-L000289](../../tests/test_multitenant_api.py#L289) | 289 | `"        \"/api/diagnostics\","` | — |
| [SRC-4405E7912C-L000290](../../tests/test_multitenant_api.py#L290) | 290 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000291](../../tests/test_multitenant_api.py#L291) | 291 | `"        token=token,"` | — |
| [SRC-4405E7912C-L000292](../../tests/test_multitenant_api.py#L292) | 292 | `"        payload={"` | — |
| [SRC-4405E7912C-L000293](../../tests/test_multitenant_api.py#L293) | 293 | `"            \"test_model\": True,"` | — |
| [SRC-4405E7912C-L000294](../../tests/test_multitenant_api.py#L294) | 294 | `"            \"test_social\": False,"` | — |
| [SRC-4405E7912C-L000295](../../tests/test_multitenant_api.py#L295) | 295 | `"            \"allow_provider_usage\": True,"` | — |
| [SRC-4405E7912C-L000296](../../tests/test_multitenant_api.py#L296) | 296 | `"        },"` | — |
| [SRC-4405E7912C-L000297](../../tests/test_multitenant_api.py#L297) | 297 | `"    )"` | — |
| [SRC-4405E7912C-L000298](../../tests/test_multitenant_api.py#L298) | 298 | `"    assert status == 200"` | — |
| [SRC-4405E7912C-L000299](../../tests/test_multitenant_api.py#L299) | 299 | `"    assert result[\"overall_status\"] == \"passed\""` | — |
| [SRC-4405E7912C-L000300](../../tests/test_multitenant_api.py#L300) | 300 | `"    assert observed == {\"test_model\": True, \"test_social\": False}"` | — |
| [SRC-4405E7912C-L000301](../../tests/test_multitenant_api.py#L301) | 301 | `""` | — |
| [SRC-4405E7912C-L000302](../../tests/test_multitenant_api.py#L302) | 302 | `""` | — |
| [SRC-4405E7912C-L000303](../../tests/test_multitenant_api.py#L303) | 303 | `""` | — |
| [SRC-4405E7912C-L000304](../../tests/test_multitenant_api.py#L304) | 304 | `"def test_viewer_cannot_invoke_agent_research_or_model_calls(tenant_api, monkeypatch):"` | — |
| [SRC-4405E7912C-L000305](../../tests/test_multitenant_api.py#L305) | 305 | `"    from api.omarai import WebAgent"` | — |
| [SRC-4405E7912C-L000306](../../tests/test_multitenant_api.py#L306) | 306 | `""` | — |
| [SRC-4405E7912C-L000307](../../tests/test_multitenant_api.py#L307) | 307 | `"    base, store = tenant_api"` | — |
| [SRC-4405E7912C-L000308](../../tests/test_multitenant_api.py#L308) | 308 | `"    monkeypatch.setattr(Handler, \"_rate_limit_ok\", lambda self: True)"` | — |
| [SRC-4405E7912C-L000309](../../tests/test_multitenant_api.py#L309) | 309 | `"    tenant_id = store.create_tenant(\"Viewer Agent Block\", \"viewer-agent-block\")"` | — |
| [SRC-4405E7912C-L000310](../../tests/test_multitenant_api.py#L310) | 310 | `"    user_id = store.create_user(\"viewer-agent@example.test\", \"Viewer\")"` | — |
| [SRC-4405E7912C-L000311](../../tests/test_multitenant_api.py#L311) | 311 | `"    store.add_membership(tenant_id, user_id, \"viewer\")"` | — |
| [SRC-4405E7912C-L000312](../../tests/test_multitenant_api.py#L312) | 312 | `"    token = \"viewer-agent-token-\" + \"W\" * 32"` | — |
| [SRC-4405E7912C-L000313](../../tests/test_multitenant_api.py#L313) | 313 | `"    store.create_api_token(token, tenant_id, user_id)"` | — |
| [SRC-4405E7912C-L000314](../../tests/test_multitenant_api.py#L314) | 314 | `""` | — |
| [SRC-4405E7912C-L000315](../../tests/test_multitenant_api.py#L315) | 315 | `"    def unexpected_answer(*_args, **_kwargs):"` | — |
| [SRC-4405E7912C-L000316](../../tests/test_multitenant_api.py#L316) | 316 | `"        pytest.fail(\"viewer must be denied before agent/model execution\")"` | — |
| [SRC-4405E7912C-L000317](../../tests/test_multitenant_api.py#L317) | 317 | `""` | — |
| [SRC-4405E7912C-L000318](../../tests/test_multitenant_api.py#L318) | 318 | `"    monkeypatch.setattr(WebAgent, \"answer\", unexpected_answer)"` | — |
| [SRC-4405E7912C-L000319](../../tests/test_multitenant_api.py#L319) | 319 | `"    status, result = request_json("` | — |
| [SRC-4405E7912C-L000320](../../tests/test_multitenant_api.py#L320) | 320 | `"        base,"` | — |
| [SRC-4405E7912C-L000321](../../tests/test_multitenant_api.py#L321) | 321 | `"        \"/api/agent\","` | — |
| [SRC-4405E7912C-L000322](../../tests/test_multitenant_api.py#L322) | 322 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000323](../../tests/test_multitenant_api.py#L323) | 323 | `"        token=token,"` | — |
| [SRC-4405E7912C-L000324](../../tests/test_multitenant_api.py#L324) | 324 | `"        payload={\"question\": \"نفّذ بحثًا جديدًا\"},"` | — |
| [SRC-4405E7912C-L000325](../../tests/test_multitenant_api.py#L325) | 325 | `"    )"` | — |
| [SRC-4405E7912C-L000326](../../tests/test_multitenant_api.py#L326) | 326 | `"    assert status == 403"` | — |
| [SRC-4405E7912C-L000327](../../tests/test_multitenant_api.py#L327) | 327 | `"    assert \"viewer\" in result[\"error\"]"` | — |
| [SRC-4405E7912C-L000328](../../tests/test_multitenant_api.py#L328) | 328 | `""` | — |
| [SRC-4405E7912C-L000329](../../tests/test_multitenant_api.py#L329) | 329 | `""` | — |
| [SRC-4405E7912C-L000330](../../tests/test_multitenant_api.py#L330) | 330 | `"def test_agent_api_allowlists_and_forwards_the_hosted_smoke_budget_profile("` | — |
| [SRC-4405E7912C-L000331](../../tests/test_multitenant_api.py#L331) | 331 | `"    tenant_api, monkeypatch"` | — |
| [SRC-4405E7912C-L000332](../../tests/test_multitenant_api.py#L332) | 332 | `"):"` | — |
| [SRC-4405E7912C-L000333](../../tests/test_multitenant_api.py#L333) | 333 | `"    from api.omarai import WebAgent"` | — |
| [SRC-4405E7912C-L000334](../../tests/test_multitenant_api.py#L334) | 334 | `""` | — |
| [SRC-4405E7912C-L000335](../../tests/test_multitenant_api.py#L335) | 335 | `"    base, store = tenant_api"` | — |
| [SRC-4405E7912C-L000336](../../tests/test_multitenant_api.py#L336) | 336 | `"    tenant_id = store.create_tenant(\"Smoke Profile Owner\", \"smoke-profile-owner\")"` | — |
| [SRC-4405E7912C-L000337](../../tests/test_multitenant_api.py#L337) | 337 | `"    user_id = store.create_user(\"smoke-profile@example.test\", \"Smoke Profile Owner\")"` | — |
| [SRC-4405E7912C-L000338](../../tests/test_multitenant_api.py#L338) | 338 | `"    store.add_membership(tenant_id, user_id, \"sales_agent\")"` | — |
| [SRC-4405E7912C-L000339](../../tests/test_multitenant_api.py#L339) | 339 | `"    token = \"smoke-profile-token-\" + \"P\" * 32"` | — |
| [SRC-4405E7912C-L000340](../../tests/test_multitenant_api.py#L340) | 340 | `"    store.create_api_token(token, tenant_id, user_id)"` | — |
| [SRC-4405E7912C-L000341](../../tests/test_multitenant_api.py#L341) | 341 | `"    observed = {}"` | — |
| [SRC-4405E7912C-L000342](../../tests/test_multitenant_api.py#L342) | 342 | `""` | — |
| [SRC-4405E7912C-L000343](../../tests/test_multitenant_api.py#L343) | 343 | `"    def fake_answer(self, question, history=None, mode=\"auto\", *, budget_profile=\"default\"):"` | — |
| [SRC-4405E7912C-L000344](../../tests/test_multitenant_api.py#L344) | 344 | `"        observed.update({"` | — |
| [SRC-4405E7912C-L000345](../../tests/test_multitenant_api.py#L345) | 345 | `"            \"question\": question,"` | — |
| [SRC-4405E7912C-L000346](../../tests/test_multitenant_api.py#L346) | 346 | `"            \"history\": history,"` | — |
| [SRC-4405E7912C-L000347](../../tests/test_multitenant_api.py#L347) | 347 | `"            \"mode\": mode,"` | — |
| [SRC-4405E7912C-L000348](../../tests/test_multitenant_api.py#L348) | 348 | `"            \"budget_profile\": budget_profile,"` | — |
| [SRC-4405E7912C-L000349](../../tests/test_multitenant_api.py#L349) | 349 | `"        })"` | — |
| [SRC-4405E7912C-L000350](../../tests/test_multitenant_api.py#L350) | 350 | `"        return {\"answer\": \"test answer\"}"` | — |
| [SRC-4405E7912C-L000351](../../tests/test_multitenant_api.py#L351) | 351 | `""` | — |
| [SRC-4405E7912C-L000352](../../tests/test_multitenant_api.py#L352) | 352 | `"    monkeypatch.setattr(WebAgent, \"answer\", fake_answer)"` | — |
| [SRC-4405E7912C-L000353](../../tests/test_multitenant_api.py#L353) | 353 | `"    status, result = request_json("` | — |
| [SRC-4405E7912C-L000354](../../tests/test_multitenant_api.py#L354) | 354 | `"        base,"` | — |
| [SRC-4405E7912C-L000355](../../tests/test_multitenant_api.py#L355) | 355 | `"        \"/api/agent\","` | — |
| [SRC-4405E7912C-L000356](../../tests/test_multitenant_api.py#L356) | 356 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000357](../../tests/test_multitenant_api.py#L357) | 357 | `"        token=token,"` | — |
| [SRC-4405E7912C-L000358](../../tests/test_multitenant_api.py#L358) | 358 | `"        payload={"` | — |
| [SRC-4405E7912C-L000359](../../tests/test_multitenant_api.py#L359) | 359 | `"            \"question\": \"اختبار ميزانية القبول\","` | — |
| [SRC-4405E7912C-L000360](../../tests/test_multitenant_api.py#L360) | 360 | `"            \"mode\": \"auto\","` | — |
| [SRC-4405E7912C-L000361](../../tests/test_multitenant_api.py#L361) | 361 | `"            \"request_profile\": \"hosted_smoke\","` | — |
| [SRC-4405E7912C-L000362](../../tests/test_multitenant_api.py#L362) | 362 | `"        },"` | — |
| [SRC-4405E7912C-L000363](../../tests/test_multitenant_api.py#L363) | 363 | `"    )"` | — |
| [SRC-4405E7912C-L000364](../../tests/test_multitenant_api.py#L364) | 364 | `"    assert status == 200"` | — |
| [SRC-4405E7912C-L000365](../../tests/test_multitenant_api.py#L365) | 365 | `"    assert result[\"answer\"] == \"test answer\""` | — |
| [SRC-4405E7912C-L000366](../../tests/test_multitenant_api.py#L366) | 366 | `"    assert observed == {"` | — |
| [SRC-4405E7912C-L000367](../../tests/test_multitenant_api.py#L367) | 367 | `"        \"question\": \"اختبار ميزانية القبول\","` | — |
| [SRC-4405E7912C-L000368](../../tests/test_multitenant_api.py#L368) | 368 | `"        \"history\": [],"` | — |
| [SRC-4405E7912C-L000369](../../tests/test_multitenant_api.py#L369) | 369 | `"        \"mode\": \"auto\","` | — |
| [SRC-4405E7912C-L000370](../../tests/test_multitenant_api.py#L370) | 370 | `"        \"budget_profile\": \"hosted_smoke\","` | — |
| [SRC-4405E7912C-L000371](../../tests/test_multitenant_api.py#L371) | 371 | `"    }"` | — |
| [SRC-4405E7912C-L000372](../../tests/test_multitenant_api.py#L372) | 372 | `""` | — |
| [SRC-4405E7912C-L000373](../../tests/test_multitenant_api.py#L373) | 373 | `"    status, error = request_json("` | — |
| [SRC-4405E7912C-L000374](../../tests/test_multitenant_api.py#L374) | 374 | `"        base,"` | — |
| [SRC-4405E7912C-L000375](../../tests/test_multitenant_api.py#L375) | 375 | `"        \"/api/agent\","` | — |
| [SRC-4405E7912C-L000376](../../tests/test_multitenant_api.py#L376) | 376 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000377](../../tests/test_multitenant_api.py#L377) | 377 | `"        token=token,"` | — |
| [SRC-4405E7912C-L000378](../../tests/test_multitenant_api.py#L378) | 378 | `"        payload={\"question\": \"اختبار ملف غير مسموح\", \"request_profile\": \"unbounded\"},"` | — |
| [SRC-4405E7912C-L000379](../../tests/test_multitenant_api.py#L379) | 379 | `"    )"` | — |
| [SRC-4405E7912C-L000380](../../tests/test_multitenant_api.py#L380) | 380 | `"    assert status == 400"` | — |
| [SRC-4405E7912C-L000381](../../tests/test_multitenant_api.py#L381) | 381 | `"    assert \"request_profile\" in error[\"error\"]"` | — |
| [SRC-4405E7912C-L000382](../../tests/test_multitenant_api.py#L382) | 382 | `"    assert observed[\"budget_profile\"] == \"hosted_smoke\""` | — |
| [SRC-4405E7912C-L000383](../../tests/test_multitenant_api.py#L383) | 383 | `""` | — |
| [SRC-4405E7912C-L000384](../../tests/test_multitenant_api.py#L384) | 384 | `"    status, result = request_json("` | — |
| [SRC-4405E7912C-L000385](../../tests/test_multitenant_api.py#L385) | 385 | `"        base,"` | — |
| [SRC-4405E7912C-L000386](../../tests/test_multitenant_api.py#L386) | 386 | `"        \"/api/agent\","` | — |
| [SRC-4405E7912C-L000387](../../tests/test_multitenant_api.py#L387) | 387 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000388](../../tests/test_multitenant_api.py#L388) | 388 | `"        token=token,"` | — |
| [SRC-4405E7912C-L000389](../../tests/test_multitenant_api.py#L389) | 389 | `"        payload={\"question\": \"اختبار التوافق مع الملف الافتراضي\"},"` | — |
| [SRC-4405E7912C-L000390](../../tests/test_multitenant_api.py#L390) | 390 | `"    )"` | — |
| [SRC-4405E7912C-L000391](../../tests/test_multitenant_api.py#L391) | 391 | `"    assert status == 200"` | — |
| [SRC-4405E7912C-L000392](../../tests/test_multitenant_api.py#L392) | 392 | `"    assert result[\"answer\"] == \"test answer\""` | — |
| [SRC-4405E7912C-L000393](../../tests/test_multitenant_api.py#L393) | 393 | `"    assert observed[\"budget_profile\"] == \"default\""` | — |
## اختبارات

### FILE-44CDA52D01 — [tests/test_omarai.py](../../tests/test_omarai.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-44CDA52D01-L000001](../../tests/test_omarai.py#L1) | 1 | `"import csv"` | — |
| [SRC-44CDA52D01-L000002](../../tests/test_omarai.py#L2) | 2 | `""` | — |
| [SRC-44CDA52D01-L000003](../../tests/test_omarai.py#L3) | 3 | `"import pytest"` | — |
| [SRC-44CDA52D01-L000004](../../tests/test_omarai.py#L4) | 4 | `""` | — |
| [SRC-44CDA52D01-L000005](../../tests/test_omarai.py#L5) | 5 | `"from agents.omarai import LeadStore, analyze, normalize"` | — |
| [SRC-44CDA52D01-L000006](../../tests/test_omarai.py#L6) | 6 | `""` | — |
| [SRC-44CDA52D01-L000007](../../tests/test_omarai.py#L7) | 7 | `""` | — |
| [SRC-44CDA52D01-L000008](../../tests/test_omarai.py#L8) | 8 | `"def test_arabic_normalization():"` | — |
| [SRC-44CDA52D01-L000009](../../tests/test_omarai.py#L9) | 9 | `"    assert normalize(\"إيجارٌ ـ شقة\") == normalize(\"ايجار شقة\")"` | — |
| [SRC-44CDA52D01-L000010](../../tests/test_omarai.py#L10) | 10 | `""` | — |
| [SRC-44CDA52D01-L000011](../../tests/test_omarai.py#L11) | 11 | `"def test_high_intent_with_next_step():"` | — |
| [SRC-44CDA52D01-L000012](../../tests/test_omarai.py#L12) | 12 | `"    result=analyze(\"بدور على شقة وممكن معاينة\")"` | — |
| [SRC-44CDA52D01-L000013](../../tests/test_omarai.py#L13) | 13 | `"    assert result[\"label\"]==\"high_intent\""` | — |
| [SRC-44CDA52D01-L000014](../../tests/test_omarai.py#L14) | 14 | `"    assert result[\"score\"]>=55"` | — |
| [SRC-44CDA52D01-L000015](../../tests/test_omarai.py#L15) | 15 | `""` | — |
| [SRC-44CDA52D01-L000016](../../tests/test_omarai.py#L16) | 16 | `"def test_non_buyer_override():"` | — |
| [SRC-44CDA52D01-L000017](../../tests/test_omarai.py#L17) | 17 | `"    result=analyze(\"مش عايز اشتري، عايز ابيع شقة\")"` | — |
| [SRC-44CDA52D01-L000018](../../tests/test_omarai.py#L18) | 18 | `"    assert result[\"label\"]==\"not_buyer_signal\""` | — |
| [SRC-44CDA52D01-L000019](../../tests/test_omarai.py#L19) | 19 | `"    assert result[\"score\"]==0"` | — |
| [SRC-44CDA52D01-L000020](../../tests/test_omarai.py#L20) | 20 | `""` | — |
| [SRC-44CDA52D01-L000021](../../tests/test_omarai.py#L21) | 21 | `"def test_empty_text_rejected():"` | — |
| [SRC-44CDA52D01-L000022](../../tests/test_omarai.py#L22) | 22 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-44CDA52D01-L000023](../../tests/test_omarai.py#L23) | 23 | `"        analyze(\" \")"` | — |
| [SRC-44CDA52D01-L000024](../../tests/test_omarai.py#L24) | 24 | `""` | — |
| [SRC-44CDA52D01-L000025](../../tests/test_omarai.py#L25) | 25 | `"def test_url_required_and_validated(tmp_path):"` | — |
| [SRC-44CDA52D01-L000026](../../tests/test_omarai.py#L26) | 26 | `"    store=LeadStore(tmp_path/\"db.sqlite3\")"` | — |
| [SRC-44CDA52D01-L000027](../../tests/test_omarai.py#L27) | 27 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-44CDA52D01-L000028](../../tests/test_omarai.py#L28) | 28 | `"        store.add(\"بدور على شقة\",\"\",\"manual\")"` | — |
| [SRC-44CDA52D01-L000029](../../tests/test_omarai.py#L29) | 29 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-44CDA52D01-L000030](../../tests/test_omarai.py#L30) | 30 | `"        store.add(\"بدور على شقة\",\"file:///tmp/private\",\"manual\")"` | — |
| [SRC-44CDA52D01-L000031](../../tests/test_omarai.py#L31) | 31 | `""` | — |
| [SRC-44CDA52D01-L000032](../../tests/test_omarai.py#L32) | 32 | `"def test_duplicate_is_idempotent(tmp_path):"` | — |
| [SRC-44CDA52D01-L000033](../../tests/test_omarai.py#L33) | 33 | `"    store=LeadStore(tmp_path/\"db.sqlite3\")"` | — |
| [SRC-44CDA52D01-L000034](../../tests/test_omarai.py#L34) | 34 | `"    one,created1=store.add(\"بدور على شقة\",\"https://example.com/post/1\",\"facebook\")"` | — |
| [SRC-44CDA52D01-L000035](../../tests/test_omarai.py#L35) | 35 | `"    two,created2=store.add(\"بدور على شقة\",\"https://example.com/post/1\",\"facebook\")"` | — |
| [SRC-44CDA52D01-L000036](../../tests/test_omarai.py#L36) | 36 | `"    assert created1 is True and created2 is False"` | — |
| [SRC-44CDA52D01-L000037](../../tests/test_omarai.py#L37) | 37 | `"    assert one[\"id\"]==two[\"id\"]"` | — |
| [SRC-44CDA52D01-L000038](../../tests/test_omarai.py#L38) | 38 | `"    assert len(store.list())==1"` | — |
| [SRC-44CDA52D01-L000039](../../tests/test_omarai.py#L39) | 39 | `""` | — |
| [SRC-44CDA52D01-L000040](../../tests/test_omarai.py#L40) | 40 | `"def test_status_updates_are_explicit(tmp_path):"` | — |
| [SRC-44CDA52D01-L000041](../../tests/test_omarai.py#L41) | 41 | `"    store=LeadStore(tmp_path/\"db.sqlite3\")"` | — |
| [SRC-44CDA52D01-L000042](../../tests/test_omarai.py#L42) | 42 | `"    lead,_=store.add(\"بدور على شقة\",\"https://example.com/p\",\"manual\")"` | — |
| [SRC-44CDA52D01-L000043](../../tests/test_omarai.py#L43) | 43 | `"    updated=store.update_status(lead[\"id\"],\"qualified\")"` | — |
| [SRC-44CDA52D01-L000044](../../tests/test_omarai.py#L44) | 44 | `"    assert updated[\"status\"]==\"qualified\""` | — |
| [SRC-44CDA52D01-L000045](../../tests/test_omarai.py#L45) | 45 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-44CDA52D01-L000046](../../tests/test_omarai.py#L46) | 46 | `"        store.update_status(lead[\"id\"],\"magic\")"` | — |
| [SRC-44CDA52D01-L000047](../../tests/test_omarai.py#L47) | 47 | `""` | — |
| [SRC-44CDA52D01-L000048](../../tests/test_omarai.py#L48) | 48 | `"def test_csv_requires_columns(tmp_path):"` | — |
| [SRC-44CDA52D01-L000049](../../tests/test_omarai.py#L49) | 49 | `"    bad=tmp_path/\"bad.csv\""` | — |
| [SRC-44CDA52D01-L000050](../../tests/test_omarai.py#L50) | 50 | `"    bad.write_text(\"foo,bar\\na,b\\n\",encoding=\"utf-8\")"` | — |
| [SRC-44CDA52D01-L000051](../../tests/test_omarai.py#L51) | 51 | `"    store=LeadStore(tmp_path/\"db.sqlite3\")"` | — |
| [SRC-44CDA52D01-L000052](../../tests/test_omarai.py#L52) | 52 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-44CDA52D01-L000053](../../tests/test_omarai.py#L53) | 53 | `"        store.import_csv(bad)"` | — |
| [SRC-44CDA52D01-L000054](../../tests/test_omarai.py#L54) | 54 | `""` | — |
| [SRC-44CDA52D01-L000055](../../tests/test_omarai.py#L55) | 55 | `"def test_csv_export_neutralizes_spreadsheet_formula_injection(tmp_path):"` | — |
| [SRC-44CDA52D01-L000056](../../tests/test_omarai.py#L56) | 56 | `"    store = LeadStore(tmp_path / \"db.sqlite3\")"` | — |
| [SRC-44CDA52D01-L000057](../../tests/test_omarai.py#L57) | 57 | `"    store.add("` | — |
| [SRC-44CDA52D01-L000058](../../tests/test_omarai.py#L58) | 58 | `"        '=HYPERLINK(\"https://evil.example\",\"click\")',"` | — |
| [SRC-44CDA52D01-L000059](../../tests/test_omarai.py#L59) | 59 | `"        \"https://example.com/post/1\","` | — |
| [SRC-44CDA52D01-L000060](../../tests/test_omarai.py#L60) | 60 | `"        platform=\"manual\","` | — |
| [SRC-44CDA52D01-L000061](../../tests/test_omarai.py#L61) | 61 | `"        note=\"  +SUM(1,1)\","` | — |
| [SRC-44CDA52D01-L000062](../../tests/test_omarai.py#L62) | 62 | `"    )"` | — |
| [SRC-44CDA52D01-L000063](../../tests/test_omarai.py#L63) | 63 | `"    store.add("` | — |
| [SRC-44CDA52D01-L000064](../../tests/test_omarai.py#L64) | 64 | `"        \"\\u00a0\\ufeff=1+1\","` | — |
| [SRC-44CDA52D01-L000065](../../tests/test_omarai.py#L65) | 65 | `"        \"https://example.com/post/2\","` | — |
| [SRC-44CDA52D01-L000066](../../tests/test_omarai.py#L66) | 66 | `"        platform=\"manual\","` | — |
| [SRC-44CDA52D01-L000067](../../tests/test_omarai.py#L67) | 67 | `"        note=\"\\u00a0\\ufeff=SUM(1,1)\","` | — |
| [SRC-44CDA52D01-L000068](../../tests/test_omarai.py#L68) | 68 | `"    )"` | — |
| [SRC-44CDA52D01-L000069](../../tests/test_omarai.py#L69) | 69 | `"    destination = tmp_path / \"export.csv\""` | — |
| [SRC-44CDA52D01-L000070](../../tests/test_omarai.py#L70) | 70 | `"    assert store.export_csv(destination) == 2"` | — |
| [SRC-44CDA52D01-L000071](../../tests/test_omarai.py#L71) | 71 | `"    raw_csv = destination.read_text(encoding=\"utf-8-sig\")"` | — |
| [SRC-44CDA52D01-L000072](../../tests/test_omarai.py#L72) | 72 | `"    assert '\"\\t=HYPERLINK(' in raw_csv"` | — |
| [SRC-44CDA52D01-L000073](../../tests/test_omarai.py#L73) | 73 | `"    assert '\"\\t  +SUM' in raw_csv"` | — |
| [SRC-44CDA52D01-L000074](../../tests/test_omarai.py#L74) | 74 | `""` | — |
| [SRC-44CDA52D01-L000075](../../tests/test_omarai.py#L75) | 75 | `"    with destination.open(newline=\"\", encoding=\"utf-8-sig\") as stream:"` | — |
| [SRC-44CDA52D01-L000076](../../tests/test_omarai.py#L76) | 76 | `"        rows = list(csv.DictReader(stream))"` | — |
| [SRC-44CDA52D01-L000077](../../tests/test_omarai.py#L77) | 77 | `""` | — |
| [SRC-44CDA52D01-L000078](../../tests/test_omarai.py#L78) | 78 | `"    row1 = next(row for row in rows if row[\"source_url\"] == \"https://example.com/post/1\")"` | — |
| [SRC-44CDA52D01-L000079](../../tests/test_omarai.py#L79) | 79 | `"    row2 = next(row for row in rows if row[\"source_url\"] == \"https://example.com/post/2\")"` | — |
| [SRC-44CDA52D01-L000080](../../tests/test_omarai.py#L80) | 80 | `"    assert row1[\"text\"].startswith(\"\\t=\")"` | — |
| [SRC-44CDA52D01-L000081](../../tests/test_omarai.py#L81) | 81 | `"    assert row1[\"note\"].startswith(\"\\t  +\")"` | — |
| [SRC-44CDA52D01-L000082](../../tests/test_omarai.py#L82) | 82 | `"    assert row2[\"text\"].startswith(\"\\t\\ufeff=\")"` | — |
| [SRC-44CDA52D01-L000083](../../tests/test_omarai.py#L83) | 83 | `"    assert row2[\"note\"].startswith(\"\\t\\u00a0\\ufeff=\")"` | — |
| [SRC-44CDA52D01-L000084](../../tests/test_omarai.py#L84) | 84 | `""` | — |
| [SRC-44CDA52D01-L000085](../../tests/test_omarai.py#L85) | 85 | `""` | — |
| [SRC-44CDA52D01-L000086](../../tests/test_omarai.py#L86) | 86 | `""` | — |
| [SRC-44CDA52D01-L000087](../../tests/test_omarai.py#L87) | 87 | `"def test_generic_fire_alarm_and_supplier_requests_are_sector_neutral():"` | — |
| [SRC-44CDA52D01-L000088](../../tests/test_omarai.py#L88) | 88 | `"    fire_alarm = analyze(\"نحتاج نظام إنذار حريق للمصنع\")"` | — |
| [SRC-44CDA52D01-L000089](../../tests/test_omarai.py#L89) | 89 | `"    supplier = analyze(\"نبحث عن مورد لافتات لمشروع جديد\")"` | — |
| [SRC-44CDA52D01-L000090](../../tests/test_omarai.py#L90) | 90 | `"    assert fire_alarm[\"label\"] == \"high_intent\""` | — |
| [SRC-44CDA52D01-L000091](../../tests/test_omarai.py#L91) | 91 | `"    assert supplier[\"label\"] == \"high_intent\""` | — |
| [SRC-44CDA52D01-L000092](../../tests/test_omarai.py#L92) | 92 | `"    assert fire_alarm[\"score\"] >= 55"` | — |
| [SRC-44CDA52D01-L000093](../../tests/test_omarai.py#L93) | 93 | `"    assert supplier[\"score\"] >= 55"` | — |
| [SRC-44CDA52D01-L000094](../../tests/test_omarai.py#L94) | 94 | `""` | — |
| [SRC-44CDA52D01-L000095](../../tests/test_omarai.py#L95) | 95 | `""` | — |
| [SRC-44CDA52D01-L000096](../../tests/test_omarai.py#L96) | 96 | `"def test_product_mention_alone_does_not_create_a_demand_signal():"` | — |
| [SRC-44CDA52D01-L000097](../../tests/test_omarai.py#L97) | 97 | `"    result = analyze(\"نظام إنذار حريق\")"` | — |
| [SRC-44CDA52D01-L000098](../../tests/test_omarai.py#L98) | 98 | `"    assert result[\"label\"] == \"unclear\""` | — |
| [SRC-44CDA52D01-L000099](../../tests/test_omarai.py#L99) | 99 | `"    assert result[\"score\"] == 0"` | — |
| [SRC-44CDA52D01-L000100](../../tests/test_omarai.py#L100) | 100 | `""` | — |
| [SRC-44CDA52D01-L000101](../../tests/test_omarai.py#L101) | 101 | `""` | — |
| [SRC-44CDA52D01-L000102](../../tests/test_omarai.py#L102) | 102 | `"@pytest.mark.parametrize("` | — |
| [SRC-44CDA52D01-L000103](../../tests/test_omarai.py#L103) | 103 | `"    \"text\","` | — |
| [SRC-44CDA52D01-L000104](../../tests/test_omarai.py#L104) | 104 | `"    ["` | — |
| [SRC-44CDA52D01-L000105](../../tests/test_omarai.py#L105) | 105 | `"        \"مش بدور على شقة\","` | — |
| [SRC-44CDA52D01-L000106](../../tests/test_omarai.py#L106) | 106 | `"        \"مش محتاج نظام إنذار حريق\","` | — |
| [SRC-44CDA52D01-L000107](../../tests/test_omarai.py#L107) | 107 | `"        \"لا نحتاج مورد لافتات\","` | — |
| [SRC-44CDA52D01-L000108](../../tests/test_omarai.py#L108) | 108 | `"        \"not looking for a supplier\","` | — |
| [SRC-44CDA52D01-L000109](../../tests/test_omarai.py#L109) | 109 | `"        \"we do not need a fire alarm system\","` | — |
| [SRC-44CDA52D01-L000110](../../tests/test_omarai.py#L110) | 110 | `"    ],"` | — |
| [SRC-44CDA52D01-L000111](../../tests/test_omarai.py#L111) | 111 | `")"` | — |
| [SRC-44CDA52D01-L000112](../../tests/test_omarai.py#L112) | 112 | `"def test_explicit_negation_never_scores_as_buyer_intent(text):"` | — |
| [SRC-44CDA52D01-L000113](../../tests/test_omarai.py#L113) | 113 | `"    result = analyze(text)"` | — |
| [SRC-44CDA52D01-L000114](../../tests/test_omarai.py#L114) | 114 | `"    assert result[\"label\"] == \"not_buyer_signal\""` | — |
| [SRC-44CDA52D01-L000115](../../tests/test_omarai.py#L115) | 115 | `"    assert result[\"score\"] == 0"` | — |
| [SRC-44CDA52D01-L000116](../../tests/test_omarai.py#L116) | 116 | `""` | — |
| [SRC-44CDA52D01-L000117](../../tests/test_omarai.py#L117) | 117 | `""` | — |
| [SRC-44CDA52D01-L000118](../../tests/test_omarai.py#L118) | 118 | `"@pytest.mark.parametrize("` | — |
| [SRC-44CDA52D01-L000119](../../tests/test_omarai.py#L119) | 119 | `"    \"text\","` | — |
| [SRC-44CDA52D01-L000120](../../tests/test_omarai.py#L120) | 120 | `"    ["` | — |
| [SRC-44CDA52D01-L000121](../../tests/test_omarai.py#L121) | 121 | `"        \"تم الشراء بالفعل\","` | — |
| [SRC-44CDA52D01-L000122](../../tests/test_omarai.py#L122) | 122 | `"        \"وجدنا مورد وتم التعاقد\","` | — |
| [SRC-44CDA52D01-L000123](../../tests/test_omarai.py#L123) | 123 | `"        \"already purchased the equipment\","` | — |
| [SRC-44CDA52D01-L000124](../../tests/test_omarai.py#L124) | 124 | `"        \"supplier selected\","` | — |
| [SRC-44CDA52D01-L000125](../../tests/test_omarai.py#L125) | 125 | `"        \"كنت بدور على شقة\","` | — |
| [SRC-44CDA52D01-L000126](../../tests/test_omarai.py#L126) | 126 | `"    ],"` | — |
| [SRC-44CDA52D01-L000127](../../tests/test_omarai.py#L127) | 127 | `")"` | — |
| [SRC-44CDA52D01-L000128](../../tests/test_omarai.py#L128) | 128 | `"def test_completed_or_past_need_is_not_active_demand(text):"` | — |
| [SRC-44CDA52D01-L000129](../../tests/test_omarai.py#L129) | 129 | `"    result = analyze(text)"` | — |
| [SRC-44CDA52D01-L000130](../../tests/test_omarai.py#L130) | 130 | `"    assert result[\"label\"] == \"closed_or_stale_signal\""` | — |
| [SRC-44CDA52D01-L000131](../../tests/test_omarai.py#L131) | 131 | `"    assert result[\"score\"] == 0"` | — |
| [SRC-44CDA52D01-L000132](../../tests/test_omarai.py#L132) | 132 | `""` | — |
| [SRC-44CDA52D01-L000133](../../tests/test_omarai.py#L133) | 133 | `""` | — |
| [SRC-44CDA52D01-L000134](../../tests/test_omarai.py#L134) | 134 | `"def test_product_and_location_context_do_not_inflate_demand_score():"` | — |
| [SRC-44CDA52D01-L000135](../../tests/test_omarai.py#L135) | 135 | `"    result = analyze("` | — |
| [SRC-44CDA52D01-L000136](../../tests/test_omarai.py#L136) | 136 | `"        \"نظام إنذار حريق في القاهرة\","` | — |
| [SRC-44CDA52D01-L000137](../../tests/test_omarai.py#L137) | 137 | `"        product_terms=[\"نظام إنذار حريق\"],"` | — |
| [SRC-44CDA52D01-L000138](../../tests/test_omarai.py#L138) | 138 | `"        location_terms=[\"القاهرة\"],"` | — |
| [SRC-44CDA52D01-L000139](../../tests/test_omarai.py#L139) | 139 | `"    )"` | — |
| [SRC-44CDA52D01-L000140](../../tests/test_omarai.py#L140) | 140 | `"    assert result[\"score\"] == 0"` | — |
| [SRC-44CDA52D01-L000141](../../tests/test_omarai.py#L141) | 141 | `"    assert result[\"label\"] == \"unclear\""` | — |
| [SRC-44CDA52D01-L000142](../../tests/test_omarai.py#L142) | 142 | `"    assert {item[\"category\"] for item in result[\"matched_signals\"]} == {"` | — |
