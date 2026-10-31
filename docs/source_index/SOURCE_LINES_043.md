# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **043**
- سجلات الأسطر: **800**
- النطاق: SRC-4405E7912C-L000025 إلى SRC-C353AAAC10-L000120
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-4405E7912C — [tests/test_multitenant_api.py](../../tests/test_multitenant_api.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-4405E7912C-L000025](../../tests/test_multitenant_api.py#L25) | 25 | `"    try:"` | — |
| [SRC-4405E7912C-L000026](../../tests/test_multitenant_api.py#L26) | 26 | `"        yield f\"http://127.0.0.1:{server.server_port}\", Handler.store"` | — |
| [SRC-4405E7912C-L000027](../../tests/test_multitenant_api.py#L27) | 27 | `"    finally:"` | — |
| [SRC-4405E7912C-L000028](../../tests/test_multitenant_api.py#L28) | 28 | `"        server.shutdown()"` | — |
| [SRC-4405E7912C-L000029](../../tests/test_multitenant_api.py#L29) | 29 | `"        server.server_close()"` | — |
| [SRC-4405E7912C-L000030](../../tests/test_multitenant_api.py#L30) | 30 | `"        thread.join(timeout=3)"` | — |
| [SRC-4405E7912C-L000031](../../tests/test_multitenant_api.py#L31) | 31 | `"        Handler.store = previous_store"` | — |
| [SRC-4405E7912C-L000032](../../tests/test_multitenant_api.py#L32) | 32 | `""` | — |
| [SRC-4405E7912C-L000033](../../tests/test_multitenant_api.py#L33) | 33 | `""` | — |
| [SRC-4405E7912C-L000034](../../tests/test_multitenant_api.py#L34) | 34 | `"def request_json(base, path, *, method=\"GET\", payload=None, token=\"\"):"` | — |
| [SRC-4405E7912C-L000035](../../tests/test_multitenant_api.py#L35) | 35 | `"    body = None if payload is None else json.dumps(payload).encode(\"utf-8\")"` | — |
| [SRC-4405E7912C-L000036](../../tests/test_multitenant_api.py#L36) | 36 | `"    headers = {}"` | — |
| [SRC-4405E7912C-L000037](../../tests/test_multitenant_api.py#L37) | 37 | `"    if body is not None:"` | — |
| [SRC-4405E7912C-L000038](../../tests/test_multitenant_api.py#L38) | 38 | `"        headers[\"Content-Type\"] = \"application/json\""` | — |
| [SRC-4405E7912C-L000039](../../tests/test_multitenant_api.py#L39) | 39 | `"    if token:"` | — |
| [SRC-4405E7912C-L000040](../../tests/test_multitenant_api.py#L40) | 40 | `"        headers[\"Authorization\"] = \"Bearer \" + token"` | — |
| [SRC-4405E7912C-L000041](../../tests/test_multitenant_api.py#L41) | 41 | `"    request = Request(base + path, data=body, method=method, headers=headers)"` | — |
| [SRC-4405E7912C-L000042](../../tests/test_multitenant_api.py#L42) | 42 | `"    try:"` | — |
| [SRC-4405E7912C-L000043](../../tests/test_multitenant_api.py#L43) | 43 | `"        with urlopen(request, timeout=3) as response:"` | — |
| [SRC-4405E7912C-L000044](../../tests/test_multitenant_api.py#L44) | 44 | `"            return response.status, json.loads(response.read().decode(\"utf-8\"))"` | — |
| [SRC-4405E7912C-L000045](../../tests/test_multitenant_api.py#L45) | 45 | `"    except HTTPError as error:"` | — |
| [SRC-4405E7912C-L000046](../../tests/test_multitenant_api.py#L46) | 46 | `"        return error.code, json.loads(error.read().decode(\"utf-8\"))"` | — |
| [SRC-4405E7912C-L000047](../../tests/test_multitenant_api.py#L47) | 47 | `""` | — |
| [SRC-4405E7912C-L000048](../../tests/test_multitenant_api.py#L48) | 48 | `""` | — |
| [SRC-4405E7912C-L000049](../../tests/test_multitenant_api.py#L49) | 49 | `"def _tenant(store, name, email, token):"` | — |
| [SRC-4405E7912C-L000050](../../tests/test_multitenant_api.py#L50) | 50 | `"    tenant_id = store.create_tenant(name, name.casefold())"` | — |
| [SRC-4405E7912C-L000051](../../tests/test_multitenant_api.py#L51) | 51 | `"    user_id = store.create_user(email, name + \" User\")"` | — |
| [SRC-4405E7912C-L000052](../../tests/test_multitenant_api.py#L52) | 52 | `"    store.add_membership(tenant_id, user_id, \"sales_agent\")"` | — |
| [SRC-4405E7912C-L000053](../../tests/test_multitenant_api.py#L53) | 53 | `"    store.create_api_token(token, tenant_id, user_id, label=name)"` | — |
| [SRC-4405E7912C-L000054](../../tests/test_multitenant_api.py#L54) | 54 | `"    return tenant_id"` | — |
| [SRC-4405E7912C-L000055](../../tests/test_multitenant_api.py#L55) | 55 | `""` | — |
| [SRC-4405E7912C-L000056](../../tests/test_multitenant_api.py#L56) | 56 | `""` | — |
| [SRC-4405E7912C-L000057](../../tests/test_multitenant_api.py#L57) | 57 | `"def test_api_ignores_client_tenant_id_and_blocks_cross_tenant_reads_and_updates(tenant_api):"` | — |
| [SRC-4405E7912C-L000058](../../tests/test_multitenant_api.py#L58) | 58 | `"    base, store = tenant_api"` | — |
| [SRC-4405E7912C-L000059](../../tests/test_multitenant_api.py#L59) | 59 | `"    token_a = \"tenant-a-token-\" + \"A\" * 32"` | — |
| [SRC-4405E7912C-L000060](../../tests/test_multitenant_api.py#L60) | 60 | `"    token_b = \"tenant-b-token-\" + \"B\" * 32"` | — |
| [SRC-4405E7912C-L000061](../../tests/test_multitenant_api.py#L61) | 61 | `"    tenant_a = _tenant(store, \"Company A\", \"api-a@example.test\", token_a)"` | — |
| [SRC-4405E7912C-L000062](../../tests/test_multitenant_api.py#L62) | 62 | `"    tenant_b = _tenant(store, \"Company B\", \"api-b@example.test\", token_b)"` | — |
| [SRC-4405E7912C-L000063](../../tests/test_multitenant_api.py#L63) | 63 | `""` | — |
| [SRC-4405E7912C-L000064](../../tests/test_multitenant_api.py#L64) | 64 | `"    status, created_a = request_json("` | — |
| [SRC-4405E7912C-L000065](../../tests/test_multitenant_api.py#L65) | 65 | `"        base,"` | — |
| [SRC-4405E7912C-L000066](../../tests/test_multitenant_api.py#L66) | 66 | `"        \"/api/leads\","` | — |
| [SRC-4405E7912C-L000067](../../tests/test_multitenant_api.py#L67) | 67 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000068](../../tests/test_multitenant_api.py#L68) | 68 | `"        token=token_a,"` | — |
| [SRC-4405E7912C-L000069](../../tests/test_multitenant_api.py#L69) | 69 | `"        payload={"` | — |
| [SRC-4405E7912C-L000070](../../tests/test_multitenant_api.py#L70) | 70 | `"            \"tenant_id\": tenant_b,"` | — |
| [SRC-4405E7912C-L000071](../../tests/test_multitenant_api.py#L71) | 71 | `"            \"text\": \"Buyer A wants to purchase\","` | — |
| [SRC-4405E7912C-L000072](../../tests/test_multitenant_api.py#L72) | 72 | `"            \"source_url\": \"https://example.test/a\","` | — |
| [SRC-4405E7912C-L000073](../../tests/test_multitenant_api.py#L73) | 73 | `"            \"platform\": \"public\","` | — |
| [SRC-4405E7912C-L000074](../../tests/test_multitenant_api.py#L74) | 74 | `"        },"` | — |
| [SRC-4405E7912C-L000075](../../tests/test_multitenant_api.py#L75) | 75 | `"    )"` | — |
| [SRC-4405E7912C-L000076](../../tests/test_multitenant_api.py#L76) | 76 | `"    assert status == 201"` | — |
| [SRC-4405E7912C-L000077](../../tests/test_multitenant_api.py#L77) | 77 | `"    assert created_a[\"lead\"][\"tenant_id\"] == tenant_a"` | — |
| [SRC-4405E7912C-L000078](../../tests/test_multitenant_api.py#L78) | 78 | `""` | — |
| [SRC-4405E7912C-L000079](../../tests/test_multitenant_api.py#L79) | 79 | `"    status, created_b = request_json("` | — |
| [SRC-4405E7912C-L000080](../../tests/test_multitenant_api.py#L80) | 80 | `"        base,"` | — |
| [SRC-4405E7912C-L000081](../../tests/test_multitenant_api.py#L81) | 81 | `"        \"/api/leads\","` | — |
| [SRC-4405E7912C-L000082](../../tests/test_multitenant_api.py#L82) | 82 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000083](../../tests/test_multitenant_api.py#L83) | 83 | `"        token=token_b,"` | — |
| [SRC-4405E7912C-L000084](../../tests/test_multitenant_api.py#L84) | 84 | `"        payload={"` | — |
| [SRC-4405E7912C-L000085](../../tests/test_multitenant_api.py#L85) | 85 | `"            \"tenant_id\": tenant_a,"` | — |
| [SRC-4405E7912C-L000086](../../tests/test_multitenant_api.py#L86) | 86 | `"            \"text\": \"Buyer B wants to purchase\","` | — |
| [SRC-4405E7912C-L000087](../../tests/test_multitenant_api.py#L87) | 87 | `"            \"source_url\": \"https://example.test/b\","` | — |
| [SRC-4405E7912C-L000088](../../tests/test_multitenant_api.py#L88) | 88 | `"            \"platform\": \"public\","` | — |
| [SRC-4405E7912C-L000089](../../tests/test_multitenant_api.py#L89) | 89 | `"        },"` | — |
| [SRC-4405E7912C-L000090](../../tests/test_multitenant_api.py#L90) | 90 | `"    )"` | — |
| [SRC-4405E7912C-L000091](../../tests/test_multitenant_api.py#L91) | 91 | `"    assert status == 201"` | — |
| [SRC-4405E7912C-L000092](../../tests/test_multitenant_api.py#L92) | 92 | `"    assert created_b[\"lead\"][\"tenant_id\"] == tenant_b"` | — |
| [SRC-4405E7912C-L000093](../../tests/test_multitenant_api.py#L93) | 93 | `""` | — |
| [SRC-4405E7912C-L000094](../../tests/test_multitenant_api.py#L94) | 94 | `"    status, listing_a = request_json("` | — |
| [SRC-4405E7912C-L000095](../../tests/test_multitenant_api.py#L95) | 95 | `"        base, f\"/api/leads?tenant_id={tenant_b}\", token=token_a"` | — |
| [SRC-4405E7912C-L000096](../../tests/test_multitenant_api.py#L96) | 96 | `"    )"` | — |
| [SRC-4405E7912C-L000097](../../tests/test_multitenant_api.py#L97) | 97 | `"    assert status == 200"` | — |
| [SRC-4405E7912C-L000098](../../tests/test_multitenant_api.py#L98) | 98 | `"    assert [lead[\"id\"] for lead in listing_a[\"leads\"]] == [created_a[\"lead\"][\"id\"]]"` | — |
| [SRC-4405E7912C-L000099](../../tests/test_multitenant_api.py#L99) | 99 | `""` | — |
| [SRC-4405E7912C-L000100](../../tests/test_multitenant_api.py#L100) | 100 | `"    status, listing_b = request_json(base, \"/api/leads\", token=token_b)"` | — |
| [SRC-4405E7912C-L000101](../../tests/test_multitenant_api.py#L101) | 101 | `"    assert status == 200"` | — |
| [SRC-4405E7912C-L000102](../../tests/test_multitenant_api.py#L102) | 102 | `"    assert [lead[\"id\"] for lead in listing_b[\"leads\"]] == [created_b[\"lead\"][\"id\"]]"` | — |
| [SRC-4405E7912C-L000103](../../tests/test_multitenant_api.py#L103) | 103 | `""` | — |
| [SRC-4405E7912C-L000104](../../tests/test_multitenant_api.py#L104) | 104 | `"    status, denied = request_json("` | — |
| [SRC-4405E7912C-L000105](../../tests/test_multitenant_api.py#L105) | 105 | `"        base,"` | — |
| [SRC-4405E7912C-L000106](../../tests/test_multitenant_api.py#L106) | 106 | `"        f\"/api/leads/{created_b['lead']['id']}/status\","` | — |
| [SRC-4405E7912C-L000107](../../tests/test_multitenant_api.py#L107) | 107 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000108](../../tests/test_multitenant_api.py#L108) | 108 | `"        token=token_a,"` | — |
| [SRC-4405E7912C-L000109](../../tests/test_multitenant_api.py#L109) | 109 | `"        payload={\"status\": \"qualified\"},"` | — |
| [SRC-4405E7912C-L000110](../../tests/test_multitenant_api.py#L110) | 110 | `"    )"` | — |
| [SRC-4405E7912C-L000111](../../tests/test_multitenant_api.py#L111) | 111 | `"    assert status == 404"` | — |
| [SRC-4405E7912C-L000112](../../tests/test_multitenant_api.py#L112) | 112 | `"    assert denied[\"error\"] == \"lead not found\""` | — |
| [SRC-4405E7912C-L000113](../../tests/test_multitenant_api.py#L113) | 113 | `""` | — |
| [SRC-4405E7912C-L000114](../../tests/test_multitenant_api.py#L114) | 114 | `"    status, changed = request_json("` | — |
| [SRC-4405E7912C-L000115](../../tests/test_multitenant_api.py#L115) | 115 | `"        base,"` | — |
| [SRC-4405E7912C-L000116](../../tests/test_multitenant_api.py#L116) | 116 | `"        f\"/api/leads/{created_b['lead']['id']}/status\","` | — |
| [SRC-4405E7912C-L000117](../../tests/test_multitenant_api.py#L117) | 117 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000118](../../tests/test_multitenant_api.py#L118) | 118 | `"        token=token_b,"` | — |
| [SRC-4405E7912C-L000119](../../tests/test_multitenant_api.py#L119) | 119 | `"        payload={\"status\": \"qualified\"},"` | — |
| [SRC-4405E7912C-L000120](../../tests/test_multitenant_api.py#L120) | 120 | `"    )"` | — |
| [SRC-4405E7912C-L000121](../../tests/test_multitenant_api.py#L121) | 121 | `"    assert status == 200"` | — |
| [SRC-4405E7912C-L000122](../../tests/test_multitenant_api.py#L122) | 122 | `"    assert changed[\"lead\"][\"status\"] == \"qualified\""` | — |
| [SRC-4405E7912C-L000123](../../tests/test_multitenant_api.py#L123) | 123 | `""` | — |
| [SRC-4405E7912C-L000124](../../tests/test_multitenant_api.py#L124) | 124 | `""` | — |
| [SRC-4405E7912C-L000125](../../tests/test_multitenant_api.py#L125) | 125 | `"def test_public_api_rejects_unknown_token(tenant_api):"` | — |
| [SRC-4405E7912C-L000126](../../tests/test_multitenant_api.py#L126) | 126 | `"    base, _ = tenant_api"` | — |
| [SRC-4405E7912C-L000127](../../tests/test_multitenant_api.py#L127) | 127 | `"    status, error = request_json("` | — |
| [SRC-4405E7912C-L000128](../../tests/test_multitenant_api.py#L128) | 128 | `"        base,"` | — |
| [SRC-4405E7912C-L000129](../../tests/test_multitenant_api.py#L129) | 129 | `"        \"/api/leads\","` | — |
| [SRC-4405E7912C-L000130](../../tests/test_multitenant_api.py#L130) | 130 | `"        token=\"unknown-token-\" + \"X\" * 32,"` | — |
| [SRC-4405E7912C-L000131](../../tests/test_multitenant_api.py#L131) | 131 | `"    )"` | — |
| [SRC-4405E7912C-L000132](../../tests/test_multitenant_api.py#L132) | 132 | `"    assert status == 401"` | — |
| [SRC-4405E7912C-L000133](../../tests/test_multitenant_api.py#L133) | 133 | `"    assert \"رمز الوصول\" in error[\"error\"]"` | — |
| [SRC-4405E7912C-L000134](../../tests/test_multitenant_api.py#L134) | 134 | `""` | — |
| [SRC-4405E7912C-L000135](../../tests/test_multitenant_api.py#L135) | 135 | `""` | — |
| [SRC-4405E7912C-L000136](../../tests/test_multitenant_api.py#L136) | 136 | `"def test_viewer_membership_is_read_only(tenant_api):"` | — |
| [SRC-4405E7912C-L000137](../../tests/test_multitenant_api.py#L137) | 137 | `"    base, store = tenant_api"` | — |
| [SRC-4405E7912C-L000138](../../tests/test_multitenant_api.py#L138) | 138 | `"    tenant_id = store.create_tenant(\"Read Only Company\", \"read-only-company\")"` | — |
| [SRC-4405E7912C-L000139](../../tests/test_multitenant_api.py#L139) | 139 | `"    user_id = store.create_user(\"viewer@example.test\", \"Viewer\")"` | — |
| [SRC-4405E7912C-L000140](../../tests/test_multitenant_api.py#L140) | 140 | `"    store.add_membership(tenant_id, user_id, \"viewer\")"` | — |
| [SRC-4405E7912C-L000141](../../tests/test_multitenant_api.py#L141) | 141 | `"    token = \"viewer-token-\" + \"V\" * 32"` | — |
| [SRC-4405E7912C-L000142](../../tests/test_multitenant_api.py#L142) | 142 | `"    store.create_api_token(token, tenant_id, user_id, label=\"viewer\")"` | — |
| [SRC-4405E7912C-L000143](../../tests/test_multitenant_api.py#L143) | 143 | `""` | — |
| [SRC-4405E7912C-L000144](../../tests/test_multitenant_api.py#L144) | 144 | `"    status, listing = request_json(base, \"/api/leads\", token=token)"` | — |
| [SRC-4405E7912C-L000145](../../tests/test_multitenant_api.py#L145) | 145 | `"    assert status == 200"` | — |
| [SRC-4405E7912C-L000146](../../tests/test_multitenant_api.py#L146) | 146 | `"    assert listing[\"count\"] == 0"` | — |
| [SRC-4405E7912C-L000147](../../tests/test_multitenant_api.py#L147) | 147 | `""` | — |
| [SRC-4405E7912C-L000148](../../tests/test_multitenant_api.py#L148) | 148 | `"    status, error = request_json("` | — |
| [SRC-4405E7912C-L000149](../../tests/test_multitenant_api.py#L149) | 149 | `"        base,"` | — |
| [SRC-4405E7912C-L000150](../../tests/test_multitenant_api.py#L150) | 150 | `"        \"/api/leads\","` | — |
| [SRC-4405E7912C-L000151](../../tests/test_multitenant_api.py#L151) | 151 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000152](../../tests/test_multitenant_api.py#L152) | 152 | `"        token=token,"` | — |
| [SRC-4405E7912C-L000153](../../tests/test_multitenant_api.py#L153) | 153 | `"        payload={"` | — |
| [SRC-4405E7912C-L000154](../../tests/test_multitenant_api.py#L154) | 154 | `"            \"text\": \"Viewer must not write\","` | — |
| [SRC-4405E7912C-L000155](../../tests/test_multitenant_api.py#L155) | 155 | `"            \"source_url\": \"https://example.test/viewer\","` | — |
| [SRC-4405E7912C-L000156](../../tests/test_multitenant_api.py#L156) | 156 | `"        },"` | — |
| [SRC-4405E7912C-L000157](../../tests/test_multitenant_api.py#L157) | 157 | `"    )"` | — |
| [SRC-4405E7912C-L000158](../../tests/test_multitenant_api.py#L158) | 158 | `"    assert status == 403"` | — |
| [SRC-4405E7912C-L000159](../../tests/test_multitenant_api.py#L159) | 159 | `"    assert \"للقراءة فقط\" in error[\"error\"]"` | — |
| [SRC-4405E7912C-L000160](../../tests/test_multitenant_api.py#L160) | 160 | `""` | — |
| [SRC-4405E7912C-L000161](../../tests/test_multitenant_api.py#L161) | 161 | `""` | — |
| [SRC-4405E7912C-L000162](../../tests/test_multitenant_api.py#L162) | 162 | `""` | — |
| [SRC-4405E7912C-L000163](../../tests/test_multitenant_api.py#L163) | 163 | `"def test_api_revokes_only_the_authenticated_api_token(tenant_api):"` | — |
| [SRC-4405E7912C-L000164](../../tests/test_multitenant_api.py#L164) | 164 | `"    base, store = tenant_api"` | — |
| [SRC-4405E7912C-L000165](../../tests/test_multitenant_api.py#L165) | 165 | `"    tenant_id = store.create_tenant(\"Revocable Company\", \"revocable-company\")"` | — |
| [SRC-4405E7912C-L000166](../../tests/test_multitenant_api.py#L166) | 166 | `"    user_id = store.create_user(\"revoker@example.test\", \"Token Owner\")"` | — |
| [SRC-4405E7912C-L000167](../../tests/test_multitenant_api.py#L167) | 167 | `"    store.add_membership(tenant_id, user_id, \"owner\")"` | — |
| [SRC-4405E7912C-L000168](../../tests/test_multitenant_api.py#L168) | 168 | `"    token = \"revocable-token-\" + \"R\" * 32"` | — |
| [SRC-4405E7912C-L000169](../../tests/test_multitenant_api.py#L169) | 169 | `"    store.create_api_token(token, tenant_id, user_id)"` | — |
| [SRC-4405E7912C-L000170](../../tests/test_multitenant_api.py#L170) | 170 | `""` | — |
| [SRC-4405E7912C-L000171](../../tests/test_multitenant_api.py#L171) | 171 | `"    status, result = request_json("` | — |
| [SRC-4405E7912C-L000172](../../tests/test_multitenant_api.py#L172) | 172 | `"        base, \"/api/tokens/revoke\", method=\"POST\", token=token, payload={}"` | — |
| [SRC-4405E7912C-L000173](../../tests/test_multitenant_api.py#L173) | 173 | `"    )"` | — |
| [SRC-4405E7912C-L000174](../../tests/test_multitenant_api.py#L174) | 174 | `"    assert status == 200"` | — |
| [SRC-4405E7912C-L000175](../../tests/test_multitenant_api.py#L175) | 175 | `"    assert result == {\"revoked\": True}"` | — |
| [SRC-4405E7912C-L000176](../../tests/test_multitenant_api.py#L176) | 176 | `""` | — |
| [SRC-4405E7912C-L000177](../../tests/test_multitenant_api.py#L177) | 177 | `"    status, denied = request_json(base, \"/api/leads\", token=token)"` | — |
| [SRC-4405E7912C-L000178](../../tests/test_multitenant_api.py#L178) | 178 | `"    assert status == 401"` | — |
| [SRC-4405E7912C-L000179](../../tests/test_multitenant_api.py#L179) | 179 | `"    assert \"رمز الوصول\" in denied[\"error\"]"` | — |
| [SRC-4405E7912C-L000180](../../tests/test_multitenant_api.py#L180) | 180 | `""` | — |
| [SRC-4405E7912C-L000181](../../tests/test_multitenant_api.py#L181) | 181 | `""` | — |
| [SRC-4405E7912C-L000182](../../tests/test_multitenant_api.py#L182) | 182 | `"def test_api_does_not_claim_to_revoke_shared_environment_token("` | — |
| [SRC-4405E7912C-L000183](../../tests/test_multitenant_api.py#L183) | 183 | `"    tenant_api, monkeypatch"` | — |
| [SRC-4405E7912C-L000184](../../tests/test_multitenant_api.py#L184) | 184 | `"):"` | — |
| [SRC-4405E7912C-L000185](../../tests/test_multitenant_api.py#L185) | 185 | `"    base, _ = tenant_api"` | — |
| [SRC-4405E7912C-L000186](../../tests/test_multitenant_api.py#L186) | 186 | `"    shared_token = \"shared-application-token-\" + \"S\" * 32"` | — |
| [SRC-4405E7912C-L000187](../../tests/test_multitenant_api.py#L187) | 187 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", shared_token)"` | — |
| [SRC-4405E7912C-L000188](../../tests/test_multitenant_api.py#L188) | 188 | `""` | — |
| [SRC-4405E7912C-L000189](../../tests/test_multitenant_api.py#L189) | 189 | `"    status, result = request_json("` | — |
| [SRC-4405E7912C-L000190](../../tests/test_multitenant_api.py#L190) | 190 | `"        base,"` | — |
| [SRC-4405E7912C-L000191](../../tests/test_multitenant_api.py#L191) | 191 | `"        \"/api/tokens/revoke\","` | — |
| [SRC-4405E7912C-L000192](../../tests/test_multitenant_api.py#L192) | 192 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000193](../../tests/test_multitenant_api.py#L193) | 193 | `"        token=shared_token,"` | — |
| [SRC-4405E7912C-L000194](../../tests/test_multitenant_api.py#L194) | 194 | `"        payload={},"` | — |
| [SRC-4405E7912C-L000195](../../tests/test_multitenant_api.py#L195) | 195 | `"    )"` | — |
| [SRC-4405E7912C-L000196](../../tests/test_multitenant_api.py#L196) | 196 | `"    assert status == 409"` | — |
| [SRC-4405E7912C-L000197](../../tests/test_multitenant_api.py#L197) | 197 | `"    assert \"rotated by the operator\" in result[\"error\"]"` | — |
| [SRC-4405E7912C-L000198](../../tests/test_multitenant_api.py#L198) | 198 | `""` | — |
| [SRC-4405E7912C-L000199](../../tests/test_multitenant_api.py#L199) | 199 | `""` | — |
| [SRC-4405E7912C-L000200](../../tests/test_multitenant_api.py#L200) | 200 | `""` | — |
| [SRC-4405E7912C-L000201](../../tests/test_multitenant_api.py#L201) | 201 | `"def test_live_diagnostics_requires_explicit_approval_before_any_provider_call("` | — |
| [SRC-4405E7912C-L000202](../../tests/test_multitenant_api.py#L202) | 202 | `"    tenant_api, monkeypatch"` | — |
| [SRC-4405E7912C-L000203](../../tests/test_multitenant_api.py#L203) | 203 | `"):"` | — |
| [SRC-4405E7912C-L000204](../../tests/test_multitenant_api.py#L204) | 204 | `"    from api.omarai import WebAgent"` | — |
| [SRC-4405E7912C-L000205](../../tests/test_multitenant_api.py#L205) | 205 | `""` | — |
| [SRC-4405E7912C-L000206](../../tests/test_multitenant_api.py#L206) | 206 | `"    base, store = tenant_api"` | — |
| [SRC-4405E7912C-L000207](../../tests/test_multitenant_api.py#L207) | 207 | `"    tenant_id = store.create_tenant(\"Diagnostics Owner\", \"diagnostics-owner\")"` | — |
| [SRC-4405E7912C-L000208](../../tests/test_multitenant_api.py#L208) | 208 | `"    user_id = store.create_user(\"diagnostics-owner@example.test\", \"Owner\")"` | — |
| [SRC-4405E7912C-L000209](../../tests/test_multitenant_api.py#L209) | 209 | `"    store.add_membership(tenant_id, user_id, \"owner\")"` | — |
| [SRC-4405E7912C-L000210](../../tests/test_multitenant_api.py#L210) | 210 | `"    token = \"diagnostics-owner-token-\" + \"O\" * 32"` | — |
| [SRC-4405E7912C-L000211](../../tests/test_multitenant_api.py#L211) | 211 | `""` | — |
| [SRC-4405E7912C-L000212](../../tests/test_multitenant_api.py#L212) | 212 | `"    def unexpected_diagnostics(*_args, **_kwargs):"` | — |
| [SRC-4405E7912C-L000213](../../tests/test_multitenant_api.py#L213) | 213 | `"        pytest.fail(\"diagnostics must not run without explicit provider-use approval\")"` | — |
| [SRC-4405E7912C-L000214](../../tests/test_multitenant_api.py#L214) | 214 | `""` | — |
| [SRC-4405E7912C-L000215](../../tests/test_multitenant_api.py#L215) | 215 | `"    store.create_api_token(token, tenant_id, user_id)"` | — |
| [SRC-4405E7912C-L000216](../../tests/test_multitenant_api.py#L216) | 216 | `"    monkeypatch.setattr(WebAgent, \"diagnostics\", unexpected_diagnostics)"` | — |
| [SRC-4405E7912C-L000217](../../tests/test_multitenant_api.py#L217) | 217 | `""` | — |
| [SRC-4405E7912C-L000218](../../tests/test_multitenant_api.py#L218) | 218 | `"    status, result = request_json("` | — |
| [SRC-4405E7912C-L000219](../../tests/test_multitenant_api.py#L219) | 219 | `"        base,"` | — |
| [SRC-4405E7912C-L000220](../../tests/test_multitenant_api.py#L220) | 220 | `"        \"/api/diagnostics\","` | — |
| [SRC-4405E7912C-L000221](../../tests/test_multitenant_api.py#L221) | 221 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000222](../../tests/test_multitenant_api.py#L222) | 222 | `"        token=token,"` | — |
| [SRC-4405E7912C-L000223](../../tests/test_multitenant_api.py#L223) | 223 | `"        payload={\"test_model\": True, \"test_social\": True},"` | — |
| [SRC-4405E7912C-L000224](../../tests/test_multitenant_api.py#L224) | 224 | `"    )"` | — |
| [SRC-4405E7912C-L000225](../../tests/test_multitenant_api.py#L225) | 225 | `"    assert status == 403"` | — |
| [SRC-4405E7912C-L000226](../../tests/test_multitenant_api.py#L226) | 226 | `"    assert \"explicit approval\" in result[\"error\"]"` | — |
| [SRC-4405E7912C-L000227](../../tests/test_multitenant_api.py#L227) | 227 | `""` | — |
| [SRC-4405E7912C-L000228](../../tests/test_multitenant_api.py#L228) | 228 | `""` | — |
| [SRC-4405E7912C-L000229](../../tests/test_multitenant_api.py#L229) | 229 | `"def test_live_diagnostics_is_owner_only_even_with_explicit_approval("` | — |
| [SRC-4405E7912C-L000230](../../tests/test_multitenant_api.py#L230) | 230 | `"    tenant_api, monkeypatch"` | — |
| [SRC-4405E7912C-L000231](../../tests/test_multitenant_api.py#L231) | 231 | `"):"` | — |
| [SRC-4405E7912C-L000232](../../tests/test_multitenant_api.py#L232) | 232 | `"    from api.omarai import WebAgent"` | — |
| [SRC-4405E7912C-L000233](../../tests/test_multitenant_api.py#L233) | 233 | `""` | — |
| [SRC-4405E7912C-L000234](../../tests/test_multitenant_api.py#L234) | 234 | `"    base, store = tenant_api"` | — |
| [SRC-4405E7912C-L000235](../../tests/test_multitenant_api.py#L235) | 235 | `"    tenant_id = store.create_tenant(\"Sales Member Diagnostics\", \"sales-member-diagnostics\")"` | — |
| [SRC-4405E7912C-L000236](../../tests/test_multitenant_api.py#L236) | 236 | `"    user_id = store.create_user(\"sales-member@example.test\", \"Sales Member\")"` | — |
| [SRC-4405E7912C-L000237](../../tests/test_multitenant_api.py#L237) | 237 | `"    store.add_membership(tenant_id, user_id, \"sales_agent\")"` | — |
| [SRC-4405E7912C-L000238](../../tests/test_multitenant_api.py#L238) | 238 | `"    token = \"sales-member-diagnostics-token-\" + \"S\" * 32"` | — |
| [SRC-4405E7912C-L000239](../../tests/test_multitenant_api.py#L239) | 239 | `""` | — |
| [SRC-4405E7912C-L000240](../../tests/test_multitenant_api.py#L240) | 240 | `"    def unexpected_diagnostics(*_args, **_kwargs):"` | — |
| [SRC-4405E7912C-L000241](../../tests/test_multitenant_api.py#L241) | 241 | `"        pytest.fail(\"non-owner diagnostics must be rejected before provider calls\")"` | — |
| [SRC-4405E7912C-L000242](../../tests/test_multitenant_api.py#L242) | 242 | `""` | — |
| [SRC-4405E7912C-L000243](../../tests/test_multitenant_api.py#L243) | 243 | `"    store.create_api_token(token, tenant_id, user_id)"` | — |
| [SRC-4405E7912C-L000244](../../tests/test_multitenant_api.py#L244) | 244 | `"    monkeypatch.setattr(WebAgent, \"diagnostics\", unexpected_diagnostics)"` | — |
| [SRC-4405E7912C-L000245](../../tests/test_multitenant_api.py#L245) | 245 | `""` | — |
| [SRC-4405E7912C-L000246](../../tests/test_multitenant_api.py#L246) | 246 | `"    status, result = request_json("` | — |
| [SRC-4405E7912C-L000247](../../tests/test_multitenant_api.py#L247) | 247 | `"        base,"` | — |
| [SRC-4405E7912C-L000248](../../tests/test_multitenant_api.py#L248) | 248 | `"        \"/api/diagnostics\","` | — |
| [SRC-4405E7912C-L000249](../../tests/test_multitenant_api.py#L249) | 249 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000250](../../tests/test_multitenant_api.py#L250) | 250 | `"        token=token,"` | — |
| [SRC-4405E7912C-L000251](../../tests/test_multitenant_api.py#L251) | 251 | `"        payload={"` | — |
| [SRC-4405E7912C-L000252](../../tests/test_multitenant_api.py#L252) | 252 | `"            \"test_model\": True,"` | — |
| [SRC-4405E7912C-L000253](../../tests/test_multitenant_api.py#L253) | 253 | `"            \"test_social\": True,"` | — |
| [SRC-4405E7912C-L000254](../../tests/test_multitenant_api.py#L254) | 254 | `"            \"allow_provider_usage\": True,"` | — |
| [SRC-4405E7912C-L000255](../../tests/test_multitenant_api.py#L255) | 255 | `"        },"` | — |
| [SRC-4405E7912C-L000256](../../tests/test_multitenant_api.py#L256) | 256 | `"    )"` | — |
| [SRC-4405E7912C-L000257](../../tests/test_multitenant_api.py#L257) | 257 | `"    assert status == 403"` | — |
| [SRC-4405E7912C-L000258](../../tests/test_multitenant_api.py#L258) | 258 | `"    assert \"owner\" in result[\"error\"]"` | — |
| [SRC-4405E7912C-L000259](../../tests/test_multitenant_api.py#L259) | 259 | `""` | — |
| [SRC-4405E7912C-L000260](../../tests/test_multitenant_api.py#L260) | 260 | `""` | — |
| [SRC-4405E7912C-L000261](../../tests/test_multitenant_api.py#L261) | 261 | `"def test_owner_can_run_diagnostics_only_after_explicit_approval("` | — |
| [SRC-4405E7912C-L000262](../../tests/test_multitenant_api.py#L262) | 262 | `"    tenant_api, monkeypatch"` | — |
| [SRC-4405E7912C-L000263](../../tests/test_multitenant_api.py#L263) | 263 | `"):"` | — |
| [SRC-4405E7912C-L000264](../../tests/test_multitenant_api.py#L264) | 264 | `"    from api.omarai import WebAgent"` | — |
| [SRC-4405E7912C-L000265](../../tests/test_multitenant_api.py#L265) | 265 | `""` | — |
| [SRC-4405E7912C-L000266](../../tests/test_multitenant_api.py#L266) | 266 | `"    base, store = tenant_api"` | — |
| [SRC-4405E7912C-L000267](../../tests/test_multitenant_api.py#L267) | 267 | `"    tenant_id = store.create_tenant(\"Approved Diagnostics\", \"approved-diagnostics\")"` | — |
| [SRC-4405E7912C-L000268](../../tests/test_multitenant_api.py#L268) | 268 | `"    user_id = store.create_user(\"approved-owner@example.test\", \"Owner\")"` | — |
| [SRC-4405E7912C-L000269](../../tests/test_multitenant_api.py#L269) | 269 | `"    store.add_membership(tenant_id, user_id, \"owner\")"` | — |
| [SRC-4405E7912C-L000270](../../tests/test_multitenant_api.py#L270) | 270 | `"    token = \"approved-diagnostics-token-\" + \"A\" * 32"` | — |
| [SRC-4405E7912C-L000271](../../tests/test_multitenant_api.py#L271) | 271 | `"    store.create_api_token(token, tenant_id, user_id)"` | — |
| [SRC-4405E7912C-L000272](../../tests/test_multitenant_api.py#L272) | 272 | `"    observed = {}"` | — |
| [SRC-4405E7912C-L000273](../../tests/test_multitenant_api.py#L273) | 273 | `""` | — |
| [SRC-4405E7912C-L000274](../../tests/test_multitenant_api.py#L274) | 274 | `"    def fake_diagnostics(self, *, test_model, test_social):"` | — |
| [SRC-4405E7912C-L000275](../../tests/test_multitenant_api.py#L275) | 275 | `"        observed[\"test_model\"] = test_model"` | — |
| [SRC-4405E7912C-L000276](../../tests/test_multitenant_api.py#L276) | 276 | `"        observed[\"test_social\"] = test_social"` | — |
| [SRC-4405E7912C-L000277](../../tests/test_multitenant_api.py#L277) | 277 | `"        return {\"overall_status\": \"passed\", \"model_usage\": []}"` | — |
| [SRC-4405E7912C-L000278](../../tests/test_multitenant_api.py#L278) | 278 | `""` | — |
| [SRC-4405E7912C-L000279](../../tests/test_multitenant_api.py#L279) | 279 | `"    monkeypatch.setattr(WebAgent, \"diagnostics\", fake_diagnostics)"` | — |
| [SRC-4405E7912C-L000280](../../tests/test_multitenant_api.py#L280) | 280 | `"    status, result = request_json("` | — |
| [SRC-4405E7912C-L000281](../../tests/test_multitenant_api.py#L281) | 281 | `"        base,"` | — |
| [SRC-4405E7912C-L000282](../../tests/test_multitenant_api.py#L282) | 282 | `"        \"/api/diagnostics\","` | — |
| [SRC-4405E7912C-L000283](../../tests/test_multitenant_api.py#L283) | 283 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000284](../../tests/test_multitenant_api.py#L284) | 284 | `"        token=token,"` | — |
| [SRC-4405E7912C-L000285](../../tests/test_multitenant_api.py#L285) | 285 | `"        payload={"` | — |
| [SRC-4405E7912C-L000286](../../tests/test_multitenant_api.py#L286) | 286 | `"            \"test_model\": True,"` | — |
| [SRC-4405E7912C-L000287](../../tests/test_multitenant_api.py#L287) | 287 | `"            \"test_social\": False,"` | — |
| [SRC-4405E7912C-L000288](../../tests/test_multitenant_api.py#L288) | 288 | `"            \"allow_provider_usage\": True,"` | — |
| [SRC-4405E7912C-L000289](../../tests/test_multitenant_api.py#L289) | 289 | `"        },"` | — |
| [SRC-4405E7912C-L000290](../../tests/test_multitenant_api.py#L290) | 290 | `"    )"` | — |
| [SRC-4405E7912C-L000291](../../tests/test_multitenant_api.py#L291) | 291 | `"    assert status == 200"` | — |
| [SRC-4405E7912C-L000292](../../tests/test_multitenant_api.py#L292) | 292 | `"    assert result[\"overall_status\"] == \"passed\""` | — |
| [SRC-4405E7912C-L000293](../../tests/test_multitenant_api.py#L293) | 293 | `"    assert observed == {\"test_model\": True, \"test_social\": False}"` | — |
| [SRC-4405E7912C-L000294](../../tests/test_multitenant_api.py#L294) | 294 | `""` | — |
| [SRC-4405E7912C-L000295](../../tests/test_multitenant_api.py#L295) | 295 | `""` | — |
| [SRC-4405E7912C-L000296](../../tests/test_multitenant_api.py#L296) | 296 | `""` | — |
| [SRC-4405E7912C-L000297](../../tests/test_multitenant_api.py#L297) | 297 | `"def test_viewer_cannot_invoke_agent_research_or_model_calls(tenant_api, monkeypatch):"` | — |
| [SRC-4405E7912C-L000298](../../tests/test_multitenant_api.py#L298) | 298 | `"    from api.omarai import WebAgent"` | — |
| [SRC-4405E7912C-L000299](../../tests/test_multitenant_api.py#L299) | 299 | `""` | — |
| [SRC-4405E7912C-L000300](../../tests/test_multitenant_api.py#L300) | 300 | `"    base, store = tenant_api"` | — |
| [SRC-4405E7912C-L000301](../../tests/test_multitenant_api.py#L301) | 301 | `"    tenant_id = store.create_tenant(\"Viewer Agent Block\", \"viewer-agent-block\")"` | — |
| [SRC-4405E7912C-L000302](../../tests/test_multitenant_api.py#L302) | 302 | `"    user_id = store.create_user(\"viewer-agent@example.test\", \"Viewer\")"` | — |
| [SRC-4405E7912C-L000303](../../tests/test_multitenant_api.py#L303) | 303 | `"    store.add_membership(tenant_id, user_id, \"viewer\")"` | — |
| [SRC-4405E7912C-L000304](../../tests/test_multitenant_api.py#L304) | 304 | `"    token = \"viewer-agent-token-\" + \"W\" * 32"` | — |
| [SRC-4405E7912C-L000305](../../tests/test_multitenant_api.py#L305) | 305 | `"    store.create_api_token(token, tenant_id, user_id)"` | — |
| [SRC-4405E7912C-L000306](../../tests/test_multitenant_api.py#L306) | 306 | `""` | — |
| [SRC-4405E7912C-L000307](../../tests/test_multitenant_api.py#L307) | 307 | `"    def unexpected_answer(*_args, **_kwargs):"` | — |
| [SRC-4405E7912C-L000308](../../tests/test_multitenant_api.py#L308) | 308 | `"        pytest.fail(\"viewer must be denied before agent/model execution\")"` | — |
| [SRC-4405E7912C-L000309](../../tests/test_multitenant_api.py#L309) | 309 | `""` | — |
| [SRC-4405E7912C-L000310](../../tests/test_multitenant_api.py#L310) | 310 | `"    monkeypatch.setattr(WebAgent, \"answer\", unexpected_answer)"` | — |
| [SRC-4405E7912C-L000311](../../tests/test_multitenant_api.py#L311) | 311 | `"    status, result = request_json("` | — |
| [SRC-4405E7912C-L000312](../../tests/test_multitenant_api.py#L312) | 312 | `"        base,"` | — |
| [SRC-4405E7912C-L000313](../../tests/test_multitenant_api.py#L313) | 313 | `"        \"/api/agent\","` | — |
| [SRC-4405E7912C-L000314](../../tests/test_multitenant_api.py#L314) | 314 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000315](../../tests/test_multitenant_api.py#L315) | 315 | `"        token=token,"` | — |
| [SRC-4405E7912C-L000316](../../tests/test_multitenant_api.py#L316) | 316 | `"        payload={\"question\": \"نفّذ بحثًا جديدًا\"},"` | — |
| [SRC-4405E7912C-L000317](../../tests/test_multitenant_api.py#L317) | 317 | `"    )"` | — |
| [SRC-4405E7912C-L000318](../../tests/test_multitenant_api.py#L318) | 318 | `"    assert status == 403"` | — |
| [SRC-4405E7912C-L000319](../../tests/test_multitenant_api.py#L319) | 319 | `"    assert \"viewer\" in result[\"error\"]"` | — |
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
## اختبارات

### FILE-B106ADC5EF — [tests/test_proxy_origin.py](../../tests/test_proxy_origin.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-B106ADC5EF-L000001](../../tests/test_proxy_origin.py#L1) | 1 | `"\"\"\"Regression tests for the proxy-aware Origin check. OMARAI-PROXY-ORIGIN-PATCH\"\"\""` | — |
| [SRC-B106ADC5EF-L000002](../../tests/test_proxy_origin.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-B106ADC5EF-L000003](../../tests/test_proxy_origin.py#L3) | 3 | `"import http.client"` | — |
| [SRC-B106ADC5EF-L000004](../../tests/test_proxy_origin.py#L4) | 4 | `"import threading"` | — |
| [SRC-B106ADC5EF-L000005](../../tests/test_proxy_origin.py#L5) | 5 | `"from http.server import ThreadingHTTPServer"` | — |
| [SRC-B106ADC5EF-L000006](../../tests/test_proxy_origin.py#L6) | 6 | `"import pytest"` | — |
| [SRC-B106ADC5EF-L000007](../../tests/test_proxy_origin.py#L7) | 7 | `"from agents.omarai import LeadStore"` | — |
| [SRC-B106ADC5EF-L000008](../../tests/test_proxy_origin.py#L8) | 8 | `"from api.omarai import Handler"` | — |
| [SRC-B106ADC5EF-L000009](../../tests/test_proxy_origin.py#L9) | 9 | `""` | — |
| [SRC-B106ADC5EF-L000010](../../tests/test_proxy_origin.py#L10) | 10 | `"TOKEN = \"t\" * 40"` | — |
| [SRC-B106ADC5EF-L000011](../../tests/test_proxy_origin.py#L11) | 11 | `"PUBLIC_NAME = \"app-1234.hosting.example\""` | — |
| [SRC-B106ADC5EF-L000012](../../tests/test_proxy_origin.py#L12) | 12 | `""` | — |
| [SRC-B106ADC5EF-L000013](../../tests/test_proxy_origin.py#L13) | 13 | `"@pytest.fixture"` | — |
| [SRC-B106ADC5EF-L000014](../../tests/test_proxy_origin.py#L14) | 14 | `"def port(tmp_path, monkeypatch):"` | — |
| [SRC-B106ADC5EF-L000015](../../tests/test_proxy_origin.py#L15) | 15 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-B106ADC5EF-L000016](../../tests/test_proxy_origin.py#L16) | 16 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", TOKEN)"` | — |
| [SRC-B106ADC5EF-L000017](../../tests/test_proxy_origin.py#L17) | 17 | `"    # The public host is explicitly configured; do not infer it from a client header."` | — |
| [SRC-B106ADC5EF-L000018](../../tests/test_proxy_origin.py#L18) | 18 | `"    monkeypatch.setenv(\"OMARAI_ALLOWED_ORIGINS\", \"https://\" + PUBLIC_NAME)"` | — |
| [SRC-B106ADC5EF-L000019](../../tests/test_proxy_origin.py#L19) | 19 | `"    monkeypatch.setattr(Handler, \"store\", LeadStore(tmp_path / \"origin-test.sqlite3\"))"` | — |
| [SRC-B106ADC5EF-L000020](../../tests/test_proxy_origin.py#L20) | 20 | `"    monkeypatch.setattr(Handler, \"RATE_LIMIT_REQUESTS\", 10_000)"` | — |
| [SRC-B106ADC5EF-L000021](../../tests/test_proxy_origin.py#L21) | 21 | `"    server = ThreadingHTTPServer((\"127.0.0.1\", 0), Handler)"` | — |
| [SRC-B106ADC5EF-L000022](../../tests/test_proxy_origin.py#L22) | 22 | `"    thread = threading.Thread(target=server.serve_forever, daemon=True)"` | — |
| [SRC-B106ADC5EF-L000023](../../tests/test_proxy_origin.py#L23) | 23 | `"    thread.start()"` | — |
| [SRC-B106ADC5EF-L000024](../../tests/test_proxy_origin.py#L24) | 24 | `"    try:"` | — |
| [SRC-B106ADC5EF-L000025](../../tests/test_proxy_origin.py#L25) | 25 | `"        yield server.server_port"` | — |
| [SRC-B106ADC5EF-L000026](../../tests/test_proxy_origin.py#L26) | 26 | `"    finally:"` | — |
| [SRC-B106ADC5EF-L000027](../../tests/test_proxy_origin.py#L27) | 27 | `"        server.shutdown()"` | — |
| [SRC-B106ADC5EF-L000028](../../tests/test_proxy_origin.py#L28) | 28 | `"        server.server_close()"` | — |
| [SRC-B106ADC5EF-L000029](../../tests/test_proxy_origin.py#L29) | 29 | `"        thread.join(timeout=3)"` | — |
| [SRC-B106ADC5EF-L000030](../../tests/test_proxy_origin.py#L30) | 30 | `""` | — |
| [SRC-B106ADC5EF-L000031](../../tests/test_proxy_origin.py#L31) | 31 | `"def call(port, method, extra):"` | — |
| [SRC-B106ADC5EF-L000032](../../tests/test_proxy_origin.py#L32) | 32 | `"    body = b'{\"question\": \"x\"}' if method == \"POST\" else b\"\""` | — |
| [SRC-B106ADC5EF-L000033](../../tests/test_proxy_origin.py#L33) | 33 | `"    headers = {\"Content-Type\": \"application/json\", \"Authorization\": \"Bearer \" + TOKEN, **extra}"` | — |
| [SRC-B106ADC5EF-L000034](../../tests/test_proxy_origin.py#L34) | 34 | `"    connection = http.client.HTTPConnection(\"127.0.0.1\", port, timeout=5)"` | — |
| [SRC-B106ADC5EF-L000035](../../tests/test_proxy_origin.py#L35) | 35 | `"    connection.putrequest(method, \"/api/ask\", skip_host=True)"` | — |
| [SRC-B106ADC5EF-L000036](../../tests/test_proxy_origin.py#L36) | 36 | `"    for name, value in headers.items():"` | — |
| [SRC-B106ADC5EF-L000037](../../tests/test_proxy_origin.py#L37) | 37 | `"        connection.putheader(name, value)"` | — |
| [SRC-B106ADC5EF-L000038](../../tests/test_proxy_origin.py#L38) | 38 | `"    connection.putheader(\"Content-Length\", str(len(body)))"` | — |
| [SRC-B106ADC5EF-L000039](../../tests/test_proxy_origin.py#L39) | 39 | `"    connection.endheaders()"` | — |
| [SRC-B106ADC5EF-L000040](../../tests/test_proxy_origin.py#L40) | 40 | `"    if body:"` | — |
| [SRC-B106ADC5EF-L000041](../../tests/test_proxy_origin.py#L41) | 41 | `"        connection.send(body)"` | — |
| [SRC-B106ADC5EF-L000042](../../tests/test_proxy_origin.py#L42) | 42 | `"    response = connection.getresponse()"` | — |
| [SRC-B106ADC5EF-L000043](../../tests/test_proxy_origin.py#L43) | 43 | `"    response.read()"` | — |
| [SRC-B106ADC5EF-L000044](../../tests/test_proxy_origin.py#L44) | 44 | `"    connection.close()"` | — |
| [SRC-B106ADC5EF-L000045](../../tests/test_proxy_origin.py#L45) | 45 | `"    return response.status"` | — |
| [SRC-B106ADC5EF-L000046](../../tests/test_proxy_origin.py#L46) | 46 | `""` | — |
| [SRC-B106ADC5EF-L000047](../../tests/test_proxy_origin.py#L47) | 47 | `"ALLOWED_SHAPES = {"` | — |
| [SRC-B106ADC5EF-L000048](../../tests/test_proxy_origin.py#L48) | 48 | `"    \"proxy keeps Host, forwards https\": {\"Host\": PUBLIC_NAME, \"X-Forwarded-Proto\": \"https\"},"` | — |
| [SRC-B106ADC5EF-L000049](../../tests/test_proxy_origin.py#L49) | 49 | `"    \"proxy keeps Host, sends no proto header\": {\"Host\": PUBLIC_NAME},"` | — |
| [SRC-B106ADC5EF-L000050](../../tests/test_proxy_origin.py#L50) | 50 | `"    \"proxy forwards plain http\": {\"Host\": PUBLIC_NAME, \"X-Forwarded-Proto\": \"http\"},"` | — |
| [SRC-B106ADC5EF-L000051](../../tests/test_proxy_origin.py#L51) | 51 | `"    \"proxy rewrites Host, public name in X-Forwarded-Host\": {"` | — |
| [SRC-B106ADC5EF-L000052](../../tests/test_proxy_origin.py#L52) | 52 | `"        \"Host\": \"127.0.0.1:8000\", \"X-Forwarded-Host\": PUBLIC_NAME, \"X-Forwarded-Proto\": \"http\"},"` | — |
| [SRC-B106ADC5EF-L000053](../../tests/test_proxy_origin.py#L53) | 53 | `"}"` | — |
| [SRC-B106ADC5EF-L000054](../../tests/test_proxy_origin.py#L54) | 54 | `""` | — |
| [SRC-B106ADC5EF-L000055](../../tests/test_proxy_origin.py#L55) | 55 | `"@pytest.mark.parametrize(\"shape\", ALLOWED_SHAPES)"` | — |
| [SRC-B106ADC5EF-L000056](../../tests/test_proxy_origin.py#L56) | 56 | `"def test_own_origin_is_accepted_behind_a_proxy(port, shape):"` | — |
| [SRC-B106ADC5EF-L000057](../../tests/test_proxy_origin.py#L57) | 57 | `"    headers = {**ALLOWED_SHAPES[shape], \"Origin\": \"https://\" + PUBLIC_NAME}"` | — |
| [SRC-B106ADC5EF-L000058](../../tests/test_proxy_origin.py#L58) | 58 | `"    assert call(port, \"POST\", headers) == 200"` | — |
| [SRC-B106ADC5EF-L000059](../../tests/test_proxy_origin.py#L59) | 59 | `"    assert call(port, \"OPTIONS\", {k: v for k, v in headers.items() if k != \"Authorization\"}) == 204"` | — |
| [SRC-B106ADC5EF-L000060](../../tests/test_proxy_origin.py#L60) | 60 | `""` | — |
| [SRC-B106ADC5EF-L000061](../../tests/test_proxy_origin.py#L61) | 61 | `"@pytest.mark.parametrize(\"shape\", ALLOWED_SHAPES)"` | — |
| [SRC-B106ADC5EF-L000062](../../tests/test_proxy_origin.py#L62) | 62 | `"def test_a_foreign_site_is_still_refused(port, shape):"` | — |
| [SRC-B106ADC5EF-L000063](../../tests/test_proxy_origin.py#L63) | 63 | `"    headers = {**ALLOWED_SHAPES[shape], \"Origin\": \"https://evil.example\"}"` | — |
| [SRC-B106ADC5EF-L000064](../../tests/test_proxy_origin.py#L64) | 64 | `"    assert call(port, \"POST\", headers) == 403"` | — |
| [SRC-B106ADC5EF-L000065](../../tests/test_proxy_origin.py#L65) | 65 | `"    assert call(port, \"OPTIONS\", headers) == 403"` | — |
| [SRC-B106ADC5EF-L000066](../../tests/test_proxy_origin.py#L66) | 66 | `""` | — |
| [SRC-B106ADC5EF-L000067](../../tests/test_proxy_origin.py#L67) | 67 | `"def test_configured_origin_still_works_without_any_proxy_headers(port, monkeypatch):"` | — |
| [SRC-B106ADC5EF-L000068](../../tests/test_proxy_origin.py#L68) | 68 | `"    monkeypatch.setenv(\"OMARAI_ALLOWED_ORIGINS\", \"https://frontend.example\")"` | — |
| [SRC-B106ADC5EF-L000069](../../tests/test_proxy_origin.py#L69) | 69 | `"    headers = {\"Host\": \"127.0.0.1:8000\", \"Origin\": \"https://frontend.example\"}"` | — |
| [SRC-B106ADC5EF-L000070](../../tests/test_proxy_origin.py#L70) | 70 | `"    assert call(port, \"POST\", headers) == 200"` | — |
| [SRC-B106ADC5EF-L000071](../../tests/test_proxy_origin.py#L71) | 71 | `""` | — |
| [SRC-B106ADC5EF-L000072](../../tests/test_proxy_origin.py#L72) | 72 | `"def test_spoofed_forwarded_host_cannot_add_an_unapproved_origin(port):"` | — |
| [SRC-B106ADC5EF-L000073](../../tests/test_proxy_origin.py#L73) | 73 | `"    \"\"\"A client-supplied X-Forwarded-Host must not expand the CORS allowlist.\"\"\""` | — |
| [SRC-B106ADC5EF-L000074](../../tests/test_proxy_origin.py#L74) | 74 | `"    headers = {"` | — |
| [SRC-B106ADC5EF-L000075](../../tests/test_proxy_origin.py#L75) | 75 | `"        \"Host\": \"127.0.0.1:8000\","` | — |
| [SRC-B106ADC5EF-L000076](../../tests/test_proxy_origin.py#L76) | 76 | `"        \"X-Forwarded-Host\": \"evil.example\","` | — |
| [SRC-B106ADC5EF-L000077](../../tests/test_proxy_origin.py#L77) | 77 | `"        \"X-Forwarded-Proto\": \"https\","` | — |
| [SRC-B106ADC5EF-L000078](../../tests/test_proxy_origin.py#L78) | 78 | `"        \"Origin\": \"https://evil.example\","` | — |
| [SRC-B106ADC5EF-L000079](../../tests/test_proxy_origin.py#L79) | 79 | `"    }"` | — |
| [SRC-B106ADC5EF-L000080](../../tests/test_proxy_origin.py#L80) | 80 | `"    assert call(port, \"POST\", headers) == 403"` | — |
| [SRC-B106ADC5EF-L000081](../../tests/test_proxy_origin.py#L81) | 81 | `"    assert call("` | — |
| [SRC-B106ADC5EF-L000082](../../tests/test_proxy_origin.py#L82) | 82 | `"        port,"` | — |
| [SRC-B106ADC5EF-L000083](../../tests/test_proxy_origin.py#L83) | 83 | `"        \"OPTIONS\","` | — |
| [SRC-B106ADC5EF-L000084](../../tests/test_proxy_origin.py#L84) | 84 | `"        {key: value for key, value in headers.items() if key != \"Authorization\"},"` | — |
| [SRC-B106ADC5EF-L000085](../../tests/test_proxy_origin.py#L85) | 85 | `"    ) == 403"` | — |
| [SRC-B106ADC5EF-L000086](../../tests/test_proxy_origin.py#L86) | 86 | `""` | — |
## اختبارات

### FILE-3D0DE98F65 — [tests/test_question_requirement_loop.py](../../tests/test_question_requirement_loop.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-3D0DE98F65-L000001](../../tests/test_question_requirement_loop.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-3D0DE98F65-L000002](../../tests/test_question_requirement_loop.py#L2) | 2 | `""` | — |
| [SRC-3D0DE98F65-L000003](../../tests/test_question_requirement_loop.py#L3) | 3 | `"import json"` | — |
| [SRC-3D0DE98F65-L000004](../../tests/test_question_requirement_loop.py#L4) | 4 | `""` | — |
| [SRC-3D0DE98F65-L000005](../../tests/test_question_requirement_loop.py#L5) | 5 | `"from agents.answer_validation import audit_answer_integrity, build_requirement_evidence_ledger"` | — |
| [SRC-3D0DE98F65-L000006](../../tests/test_question_requirement_loop.py#L6) | 6 | `"from agents.research import ("` | — |
| [SRC-3D0DE98F65-L000007](../../tests/test_question_requirement_loop.py#L7) | 7 | `"    MAX_PLAN_QUERIES,"` | — |
| [SRC-3D0DE98F65-L000008](../../tests/test_question_requirement_loop.py#L8) | 8 | `"    extract_question_coverage_targets,"` | — |
| [SRC-3D0DE98F65-L000009](../../tests/test_question_requirement_loop.py#L9) | 9 | `"    fallback_plan,"` | — |
| [SRC-3D0DE98F65-L000010](../../tests/test_question_requirement_loop.py#L10) | 10 | `"    validate_plan,"` | — |
| [SRC-3D0DE98F65-L000011](../../tests/test_question_requirement_loop.py#L11) | 11 | `")"` | — |
| [SRC-3D0DE98F65-L000012](../../tests/test_question_requirement_loop.py#L12) | 12 | `"from agents.web_agent import WebAgent"` | — |
| [SRC-3D0DE98F65-L000013](../../tests/test_question_requirement_loop.py#L13) | 13 | `""` | — |
| [SRC-3D0DE98F65-L000014](../../tests/test_question_requirement_loop.py#L14) | 14 | `""` | — |
| [SRC-3D0DE98F65-L000015](../../tests/test_question_requirement_loop.py#L15) | 15 | `"QUESTION = \"قارن بين iPhone 17 وSamsung S26 من حيث السعر والبطارية والكاميرا\""` | — |
| [SRC-3D0DE98F65-L000016](../../tests/test_question_requirement_loop.py#L16) | 16 | `""` | — |
| [SRC-3D0DE98F65-L000017](../../tests/test_question_requirement_loop.py#L17) | 17 | `""` | — |
| [SRC-3D0DE98F65-L000018](../../tests/test_question_requirement_loop.py#L18) | 18 | `"def test_compound_question_extracts_each_explicit_criterion() -> None:"` | — |
| [SRC-3D0DE98F65-L000019](../../tests/test_question_requirement_loop.py#L19) | 19 | `"    assert extract_question_coverage_targets(QUESTION) == [\"السعر\", \"البطارية\", \"الكاميرا\"]"` | — |
| [SRC-3D0DE98F65-L000020](../../tests/test_question_requirement_loop.py#L20) | 20 | `""` | — |
| [SRC-3D0DE98F65-L000021](../../tests/test_question_requirement_loop.py#L21) | 21 | `""` | — |
| [SRC-3D0DE98F65-L000022](../../tests/test_question_requirement_loop.py#L22) | 22 | `"def test_fallback_plan_assigns_a_bounded_query_to_every_criterion() -> None:"` | — |
| [SRC-3D0DE98F65-L000023](../../tests/test_question_requirement_loop.py#L23) | 23 | `"    plan = fallback_plan(QUESTION)"` | — |
| [SRC-3D0DE98F65-L000024](../../tests/test_question_requirement_loop.py#L24) | 24 | `"    requirement_queries = plan[\"requirement_queries\"]"` | — |
| [SRC-3D0DE98F65-L000025](../../tests/test_question_requirement_loop.py#L25) | 25 | `"    assert [item[\"target\"] for item in requirement_queries] == [\"السعر\", \"البطارية\", \"الكاميرا\"]"` | — |
| [SRC-3D0DE98F65-L000026](../../tests/test_question_requirement_loop.py#L26) | 26 | `"    assert all(item[\"query\"] in plan[\"queries\"] for item in requirement_queries)"` | — |
| [SRC-3D0DE98F65-L000027](../../tests/test_question_requirement_loop.py#L27) | 27 | `"    assert len(plan[\"queries\"]) <= MAX_PLAN_QUERIES"` | — |
| [SRC-3D0DE98F65-L000028](../../tests/test_question_requirement_loop.py#L28) | 28 | `"    assert all(item[\"target\"] in item[\"query\"] for item in requirement_queries)"` | — |
| [SRC-3D0DE98F65-L000029](../../tests/test_question_requirement_loop.py#L29) | 29 | `""` | — |
| [SRC-3D0DE98F65-L000030](../../tests/test_question_requirement_loop.py#L30) | 30 | `""` | — |
| [SRC-3D0DE98F65-L000031](../../tests/test_question_requirement_loop.py#L31) | 31 | `"def test_validated_model_plan_cannot_drop_mandatory_criterion_queries() -> None:"` | — |
| [SRC-3D0DE98F65-L000032](../../tests/test_question_requirement_loop.py#L32) | 32 | `"    fallback = fallback_plan(QUESTION)"` | — |
| [SRC-3D0DE98F65-L000033](../../tests/test_question_requirement_loop.py#L33) | 33 | `"    candidate = {"` | — |
| [SRC-3D0DE98F65-L000034](../../tests/test_question_requirement_loop.py#L34) | 34 | `"        \"queries\": [\"iPhone 17 Samsung S26 reviews\"],"` | — |
| [SRC-3D0DE98F65-L000035](../../tests/test_question_requirement_loop.py#L35) | 35 | `"        \"social_focus\": False,"` | — |
| [SRC-3D0DE98F65-L000036](../../tests/test_question_requirement_loop.py#L36) | 36 | `"        \"freshness\": \"any\","` | — |
| [SRC-3D0DE98F65-L000037](../../tests/test_question_requirement_loop.py#L37) | 37 | `"        \"depth\": \"deep\","` | — |
| [SRC-3D0DE98F65-L000038](../../tests/test_question_requirement_loop.py#L38) | 38 | `"        \"platforms\": [],"` | — |
| [SRC-3D0DE98F65-L000039](../../tests/test_question_requirement_loop.py#L39) | 39 | `"    }"` | — |
| [SRC-3D0DE98F65-L000040](../../tests/test_question_requirement_loop.py#L40) | 40 | `""` | — |
| [SRC-3D0DE98F65-L000041](../../tests/test_question_requirement_loop.py#L41) | 41 | `"    validated = validate_plan(candidate, QUESTION)"` | — |
| [SRC-3D0DE98F65-L000042](../../tests/test_question_requirement_loop.py#L42) | 42 | `""` | — |
| [SRC-3D0DE98F65-L000043](../../tests/test_question_requirement_loop.py#L43) | 43 | `"    assert validated[\"coverage_targets\"] == fallback[\"coverage_targets\"]"` | — |
| [SRC-3D0DE98F65-L000044](../../tests/test_question_requirement_loop.py#L44) | 44 | `"    assert validated[\"requirement_queries\"] == fallback[\"requirement_queries\"]"` | — |
| [SRC-3D0DE98F65-L000045](../../tests/test_question_requirement_loop.py#L45) | 45 | `"    assert all(item[\"query\"] in validated[\"queries\"] for item in fallback[\"requirement_queries\"])"` | — |
| [SRC-3D0DE98F65-L000046](../../tests/test_question_requirement_loop.py#L46) | 46 | `"    assert len(validated[\"queries\"]) <= MAX_PLAN_QUERIES"` | — |
| [SRC-3D0DE98F65-L000047](../../tests/test_question_requirement_loop.py#L47) | 47 | `""` | — |
| [SRC-3D0DE98F65-L000048](../../tests/test_question_requirement_loop.py#L48) | 48 | `""` | — |
| [SRC-3D0DE98F65-L000049](../../tests/test_question_requirement_loop.py#L49) | 49 | `"def test_model_planner_cannot_replace_every_criterion_with_one_generic_query(monkeypatch) -> None:"` | — |
| [SRC-3D0DE98F65-L000050](../../tests/test_question_requirement_loop.py#L50) | 50 | `"    agent = WebAgent()"` | — |
| [SRC-3D0DE98F65-L000051](../../tests/test_question_requirement_loop.py#L51) | 51 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-3D0DE98F65-L000052](../../tests/test_question_requirement_loop.py#L52) | 52 | `"    monkeypatch.setattr("` | — |
| [SRC-3D0DE98F65-L000053](../../tests/test_question_requirement_loop.py#L53) | 53 | `"        agent,"` | — |
| [SRC-3D0DE98F65-L000054](../../tests/test_question_requirement_loop.py#L54) | 54 | `"        \"_request_completion\","` | — |
| [SRC-3D0DE98F65-L000055](../../tests/test_question_requirement_loop.py#L55) | 55 | `"        lambda *args, **kwargs: json.dumps("` | — |
| [SRC-3D0DE98F65-L000056](../../tests/test_question_requirement_loop.py#L56) | 56 | `"            {"` | — |
| [SRC-3D0DE98F65-L000057](../../tests/test_question_requirement_loop.py#L57) | 57 | `"                \"queries\": [\"iPhone Samsung review\"],"` | — |
| [SRC-3D0DE98F65-L000058](../../tests/test_question_requirement_loop.py#L58) | 58 | `"                \"social_focus\": False,"` | — |
| [SRC-3D0DE98F65-L000059](../../tests/test_question_requirement_loop.py#L59) | 59 | `"                \"freshness\": \"any\","` | — |
| [SRC-3D0DE98F65-L000060](../../tests/test_question_requirement_loop.py#L60) | 60 | `"                \"depth\": \"deep\","` | — |
| [SRC-3D0DE98F65-L000061](../../tests/test_question_requirement_loop.py#L61) | 61 | `"                \"platforms\": [],"` | — |
| [SRC-3D0DE98F65-L000062](../../tests/test_question_requirement_loop.py#L62) | 62 | `"            }"` | — |
| [SRC-3D0DE98F65-L000063](../../tests/test_question_requirement_loop.py#L63) | 63 | `"        ),"` | — |
| [SRC-3D0DE98F65-L000064](../../tests/test_question_requirement_loop.py#L64) | 64 | `"    )"` | — |
| [SRC-3D0DE98F65-L000065](../../tests/test_question_requirement_loop.py#L65) | 65 | `""` | — |
| [SRC-3D0DE98F65-L000066](../../tests/test_question_requirement_loop.py#L66) | 66 | `"    plan = agent._plan_search(QUESTION, [])"` | — |
| [SRC-3D0DE98F65-L000067](../../tests/test_question_requirement_loop.py#L67) | 67 | `""` | — |
| [SRC-3D0DE98F65-L000068](../../tests/test_question_requirement_loop.py#L68) | 68 | `"    assert plan[\"coverage_targets\"] == [\"السعر\", \"البطارية\", \"الكاميرا\"]"` | — |
| [SRC-3D0DE98F65-L000069](../../tests/test_question_requirement_loop.py#L69) | 69 | `"    assert all(item[\"query\"] in plan[\"queries\"] for item in plan[\"requirement_queries\"])"` | — |
| [SRC-3D0DE98F65-L000070](../../tests/test_question_requirement_loop.py#L70) | 70 | `"    assert len(plan[\"queries\"]) <= MAX_PLAN_QUERIES"` | — |
| [SRC-3D0DE98F65-L000071](../../tests/test_question_requirement_loop.py#L71) | 71 | `""` | — |
| [SRC-3D0DE98F65-L000072](../../tests/test_question_requirement_loop.py#L72) | 72 | `""` | — |
| [SRC-3D0DE98F65-L000073](../../tests/test_question_requirement_loop.py#L73) | 73 | `"def test_requirement_evidence_ledger_distinguishes_candidate_from_query_only_result() -> None:"` | — |
| [SRC-3D0DE98F65-L000074](../../tests/test_question_requirement_loop.py#L74) | 74 | `"    plan = fallback_plan(QUESTION)"` | — |
| [SRC-3D0DE98F65-L000075](../../tests/test_question_requirement_loop.py#L75) | 75 | `"    queries = plan[\"requirement_queries\"]"` | — |
| [SRC-3D0DE98F65-L000076](../../tests/test_question_requirement_loop.py#L76) | 76 | `"    price_query = next(item[\"query\"] for item in queries if item[\"target\"] == \"السعر\")"` | — |
| [SRC-3D0DE98F65-L000077](../../tests/test_question_requirement_loop.py#L77) | 77 | `"    battery_query = next(item[\"query\"] for item in queries if item[\"target\"] == \"البطارية\")"` | — |
| [SRC-3D0DE98F65-L000078](../../tests/test_question_requirement_loop.py#L78) | 78 | `"    sources = ["` | — |
| [SRC-3D0DE98F65-L000079](../../tests/test_question_requirement_loop.py#L79) | 79 | `"        {"` | — |
| [SRC-3D0DE98F65-L000080](../../tests/test_question_requirement_loop.py#L80) | 80 | `"            \"url\": \"https://example.com/price\","` | — |
| [SRC-3D0DE98F65-L000081](../../tests/test_question_requirement_loop.py#L81) | 81 | `"            \"title\": \"Phone pricing\","` | — |
| [SRC-3D0DE98F65-L000082](../../tests/test_question_requirement_loop.py#L82) | 82 | `"            \"snippet\": \"The current price is listed for both phone models.\","` | — |
| [SRC-3D0DE98F65-L000083](../../tests/test_question_requirement_loop.py#L83) | 83 | `"            \"page_text\": \"The current price is 100 EGP.\","` | — |
| [SRC-3D0DE98F65-L000084](../../tests/test_question_requirement_loop.py#L84) | 84 | `"            \"page_fetched\": True,"` | — |
| [SRC-3D0DE98F65-L000085](../../tests/test_question_requirement_loop.py#L85) | 85 | `"            \"queries\": [price_query],"` | — |
| [SRC-3D0DE98F65-L000086](../../tests/test_question_requirement_loop.py#L86) | 86 | `"        },"` | — |
| [SRC-3D0DE98F65-L000087](../../tests/test_question_requirement_loop.py#L87) | 87 | `"        {"` | — |
| [SRC-3D0DE98F65-L000088](../../tests/test_question_requirement_loop.py#L88) | 88 | `"            \"url\": \"https://example.net/specs\","` | — |
| [SRC-3D0DE98F65-L000089](../../tests/test_question_requirement_loop.py#L89) | 89 | `"            \"title\": \"General technical specifications\","` | — |
| [SRC-3D0DE98F65-L000090](../../tests/test_question_requirement_loop.py#L90) | 90 | `"            \"snippet\": \"Technical specifications for the two products are listed here.\","` | — |
| [SRC-3D0DE98F65-L000091](../../tests/test_question_requirement_loop.py#L91) | 91 | `"            \"page_fetched\": False,"` | — |
| [SRC-3D0DE98F65-L000092](../../tests/test_question_requirement_loop.py#L92) | 92 | `"            \"queries\": [battery_query],"` | — |
| [SRC-3D0DE98F65-L000093](../../tests/test_question_requirement_loop.py#L93) | 93 | `"        },"` | — |
| [SRC-3D0DE98F65-L000094](../../tests/test_question_requirement_loop.py#L94) | 94 | `"    ]"` | — |
| [SRC-3D0DE98F65-L000095](../../tests/test_question_requirement_loop.py#L95) | 95 | `""` | — |
| [SRC-3D0DE98F65-L000096](../../tests/test_question_requirement_loop.py#L96) | 96 | `"    ledger = build_requirement_evidence_ledger(plan[\"coverage_targets\"], sources, queries)"` | — |
| [SRC-3D0DE98F65-L000097](../../tests/test_question_requirement_loop.py#L97) | 97 | `"    by_target = {item[\"target\"]: item for item in ledger}"` | — |
| [SRC-3D0DE98F65-L000098](../../tests/test_question_requirement_loop.py#L98) | 98 | `""` | — |
| [SRC-3D0DE98F65-L000099](../../tests/test_question_requirement_loop.py#L99) | 99 | `"    assert by_target[\"السعر\"][\"status\"] == \"candidate_evidence_found_not_verified\""` | — |
| [SRC-3D0DE98F65-L000100](../../tests/test_question_requirement_loop.py#L100) | 100 | `"    assert by_target[\"السعر\"][\"candidate_source_indexes\"] == [1]"` | — |
| [SRC-3D0DE98F65-L000101](../../tests/test_question_requirement_loop.py#L101) | 101 | `"    assert by_target[\"البطارية\"][\"status\"] == \"query_returned_candidates_no_lexical_signal\""` | — |
| [SRC-3D0DE98F65-L000102](../../tests/test_question_requirement_loop.py#L102) | 102 | `"    assert by_target[\"البطارية\"][\"query_result_source_indexes\"] == [2]"` | — |
| [SRC-3D0DE98F65-L000103](../../tests/test_question_requirement_loop.py#L103) | 103 | `"    assert by_target[\"الكاميرا\"][\"status\"] == \"no_candidate_evidence_found\""` | — |
| [SRC-3D0DE98F65-L000104](../../tests/test_question_requirement_loop.py#L104) | 104 | `"    assert all(item[\"semantic_verification\"] is False for item in ledger)"` | — |
| [SRC-3D0DE98F65-L000105](../../tests/test_question_requirement_loop.py#L105) | 105 | `"    assert all(item[\"source_entailment_verified\"] is False for item in ledger)"` | — |
| [SRC-3D0DE98F65-L000106](../../tests/test_question_requirement_loop.py#L106) | 106 | `""` | — |
| [SRC-3D0DE98F65-L000107](../../tests/test_question_requirement_loop.py#L107) | 107 | `""` | — |
| [SRC-3D0DE98F65-L000108](../../tests/test_question_requirement_loop.py#L108) | 108 | `""` | — |
| [SRC-3D0DE98F65-L000109](../../tests/test_question_requirement_loop.py#L109) | 109 | `"def test_research_keeps_a_relevant_source_for_each_criterion_before_page_fetch(monkeypatch) -> None:"` | — |
| [SRC-3D0DE98F65-L000110](../../tests/test_question_requirement_loop.py#L110) | 110 | `"    agent = WebAgent()"` | — |
| [SRC-3D0DE98F65-L000111](../../tests/test_question_requirement_loop.py#L111) | 111 | `"    targets = [\"price\", \"battery\", \"camera\", \"warranty\"]"` | — |
| [SRC-3D0DE98F65-L000112](../../tests/test_question_requirement_loop.py#L112) | 112 | `"    requirement_queries = ["` | — |
| [SRC-3D0DE98F65-L000113](../../tests/test_question_requirement_loop.py#L113) | 113 | `"        {\"target\": target, \"query\": f\"sample product {target}\"}"` | — |
| [SRC-3D0DE98F65-L000114](../../tests/test_question_requirement_loop.py#L114) | 114 | `"        for target in targets"` | — |
| [SRC-3D0DE98F65-L000115](../../tests/test_question_requirement_loop.py#L115) | 115 | `"    ]"` | — |
| [SRC-3D0DE98F65-L000116](../../tests/test_question_requirement_loop.py#L116) | 116 | `"    plan = {"` | — |
| [SRC-3D0DE98F65-L000117](../../tests/test_question_requirement_loop.py#L117) | 117 | `"        \"queries\": [item[\"query\"] for item in requirement_queries],"` | — |
| [SRC-3D0DE98F65-L000118](../../tests/test_question_requirement_loop.py#L118) | 118 | `"        \"coverage_targets\": targets,"` | — |
| [SRC-3D0DE98F65-L000119](../../tests/test_question_requirement_loop.py#L119) | 119 | `"        \"requirement_queries\": requirement_queries,"` | — |
| [SRC-3D0DE98F65-L000120](../../tests/test_question_requirement_loop.py#L120) | 120 | `"        \"direct_urls\": [],"` | — |
| [SRC-3D0DE98F65-L000121](../../tests/test_question_requirement_loop.py#L121) | 121 | `"        \"social_focus\": False,"` | — |
| [SRC-3D0DE98F65-L000122](../../tests/test_question_requirement_loop.py#L122) | 122 | `"        \"freshness\": \"any\","` | — |
| [SRC-3D0DE98F65-L000123](../../tests/test_question_requirement_loop.py#L123) | 123 | `"        \"depth\": \"standard\","` | — |
| [SRC-3D0DE98F65-L000124](../../tests/test_question_requirement_loop.py#L124) | 124 | `"        \"platforms\": [],"` | — |
| [SRC-3D0DE98F65-L000125](../../tests/test_question_requirement_loop.py#L125) | 125 | `"        \"planning_method\": \"test\","` | — |
| [SRC-3D0DE98F65-L000126](../../tests/test_question_requirement_loop.py#L126) | 126 | `"    }"` | — |
| [SRC-3D0DE98F65-L000127](../../tests/test_question_requirement_loop.py#L127) | 127 | `"    query_index = {"` | — |
| [SRC-3D0DE98F65-L000128](../../tests/test_question_requirement_loop.py#L128) | 128 | `"        item[\"query\"].casefold(): index"` | — |
| [SRC-3D0DE98F65-L000129](../../tests/test_question_requirement_loop.py#L129) | 129 | `"        for index, item in enumerate(requirement_queries)"` | — |
| [SRC-3D0DE98F65-L000130](../../tests/test_question_requirement_loop.py#L130) | 130 | `"    }"` | — |
| [SRC-3D0DE98F65-L000131](../../tests/test_question_requirement_loop.py#L131) | 131 | `""` | — |
| [SRC-3D0DE98F65-L000132](../../tests/test_question_requirement_loop.py#L132) | 132 | `"    def fake_search(query: str):"` | — |
| [SRC-3D0DE98F65-L000133](../../tests/test_question_requirement_loop.py#L133) | 133 | `"        index = query_index[query.casefold()]"` | — |
| [SRC-3D0DE98F65-L000134](../../tests/test_question_requirement_loop.py#L134) | 134 | `"        rows = []"` | — |
| [SRC-3D0DE98F65-L000135](../../tests/test_question_requirement_loop.py#L135) | 135 | `"        for rank in range(1, 7):"` | — |
| [SRC-3D0DE98F65-L000136](../../tests/test_question_requirement_loop.py#L136) | 136 | `"            title = ("` | — |
| [SRC-3D0DE98F65-L000137](../../tests/test_question_requirement_loop.py#L137) | 137 | `"                f\"{targets[index]} detailed evidence\""` | — |
| [SRC-3D0DE98F65-L000138](../../tests/test_question_requirement_loop.py#L138) | 138 | `"                if rank == 6"` | — |
| [SRC-3D0DE98F65-L000139](../../tests/test_question_requirement_loop.py#L139) | 139 | `"                else f\"Generic product listing {index}-{rank}\""` | — |
| [SRC-3D0DE98F65-L000140](../../tests/test_question_requirement_loop.py#L140) | 140 | `"            )"` | — |
| [SRC-3D0DE98F65-L000141](../../tests/test_question_requirement_loop.py#L141) | 141 | `"            rows.append({"` | — |
| [SRC-3D0DE98F65-L000142](../../tests/test_question_requirement_loop.py#L142) | 142 | `"                \"title\": title,"` | — |
| [SRC-3D0DE98F65-L000143](../../tests/test_question_requirement_loop.py#L143) | 143 | `"                \"url\": f\"https://s{index}-r{rank}.example.com/item\","` | — |
| [SRC-3D0DE98F65-L000144](../../tests/test_question_requirement_loop.py#L144) | 144 | `"                \"snippet\": title if rank == 6 else \"General product listing with no criterion detail.\","` | — |
| [SRC-3D0DE98F65-L000145](../../tests/test_question_requirement_loop.py#L145) | 145 | `"                \"provider\": \"test_search\","` | — |
| [SRC-3D0DE98F65-L000146](../../tests/test_question_requirement_loop.py#L146) | 146 | `"                \"provider_rank\": rank,"` | — |
| [SRC-3D0DE98F65-L000147](../../tests/test_question_requirement_loop.py#L147) | 147 | `"                \"domain\": f\"s{index}-r{rank}.example.com\","` | — |
| [SRC-3D0DE98F65-L000148](../../tests/test_question_requirement_loop.py#L148) | 148 | `"            })"` | — |
| [SRC-3D0DE98F65-L000149](../../tests/test_question_requirement_loop.py#L149) | 149 | `"        return rows"` | — |
| [SRC-3D0DE98F65-L000150](../../tests/test_question_requirement_loop.py#L150) | 150 | `""` | — |
| [SRC-3D0DE98F65-L000151](../../tests/test_question_requirement_loop.py#L151) | 151 | `"    def fake_fetch(url: str):"` | — |
| [SRC-3D0DE98F65-L000152](../../tests/test_question_requirement_loop.py#L152) | 152 | `"        hostname = url.split(\"://\", 1)[1].split(\"/\", 1)[0]"` | — |
| [SRC-3D0DE98F65-L000153](../../tests/test_question_requirement_loop.py#L153) | 153 | `"        index = int(hostname.split(\"-r\", 1)[0][1:])"` | — |
| [SRC-3D0DE98F65-L000154](../../tests/test_question_requirement_loop.py#L154) | 154 | `"        target = targets[index]"` | — |
| [SRC-3D0DE98F65-L000155](../../tests/test_question_requirement_loop.py#L155) | 155 | `"        return f\"{target} page\", f\"{target} evidence and detailed specifications.\""` | — |
| [SRC-3D0DE98F65-L000156](../../tests/test_question_requirement_loop.py#L156) | 156 | `""` | — |
| [SRC-3D0DE98F65-L000157](../../tests/test_question_requirement_loop.py#L157) | 157 | `"    monkeypatch.setattr(agent, \"_search_web\", fake_search)"` | — |
| [SRC-3D0DE98F65-L000158](../../tests/test_question_requirement_loop.py#L158) | 158 | `"    monkeypatch.setattr(agent, \"_fetch_page\", fake_fetch)"` | — |
| [SRC-3D0DE98F65-L000159](../../tests/test_question_requirement_loop.py#L159) | 159 | `""` | — |
| [SRC-3D0DE98F65-L000160](../../tests/test_question_requirement_loop.py#L160) | 160 | `"    sources, _warnings, report = agent._collect_research(plan)"` | — |
| [SRC-3D0DE98F65-L000161](../../tests/test_question_requirement_loop.py#L161) | 161 | `""` | — |
| [SRC-3D0DE98F65-L000162](../../tests/test_question_requirement_loop.py#L162) | 162 | `"    assert len(sources) <= 18"` | — |
| [SRC-3D0DE98F65-L000163](../../tests/test_question_requirement_loop.py#L163) | 163 | `"    for item in requirement_queries:"` | — |
| [SRC-3D0DE98F65-L000164](../../tests/test_question_requirement_loop.py#L164) | 164 | `"        matched = ["` | — |
| [SRC-3D0DE98F65-L000165](../../tests/test_question_requirement_loop.py#L165) | 165 | `"            source for source in sources"` | — |
| [SRC-3D0DE98F65-L000166](../../tests/test_question_requirement_loop.py#L166) | 166 | `"            if item[\"query\"] in source.get(\"queries\", [])"` | — |
| [SRC-3D0DE98F65-L000167](../../tests/test_question_requirement_loop.py#L167) | 167 | `"        ]"` | — |
| [SRC-3D0DE98F65-L000168](../../tests/test_question_requirement_loop.py#L168) | 168 | `"        assert matched, f\"criterion query lost from final source pool: {item['target']}\""` | — |
| [SRC-3D0DE98F65-L000169](../../tests/test_question_requirement_loop.py#L169) | 169 | `"        assert any(item[\"target\"] in source[\"title\"] for source in matched[:2])"` | — |
| [SRC-3D0DE98F65-L000170](../../tests/test_question_requirement_loop.py#L170) | 170 | `"    assert report[\"queries_planned\"] == 4"` | — |
| [SRC-3D0DE98F65-L000171](../../tests/test_question_requirement_loop.py#L171) | 171 | `"    assert report[\"queries_attempted\"] == 4"` | — |
| [SRC-3D0DE98F65-L000172](../../tests/test_question_requirement_loop.py#L172) | 172 | `""` | — |
| [SRC-3D0DE98F65-L000173](../../tests/test_question_requirement_loop.py#L173) | 173 | `""` | — |
| [SRC-3D0DE98F65-L000174](../../tests/test_question_requirement_loop.py#L174) | 174 | `"def test_answer_integrity_exposes_requirement_evidence_separately_from_word_overlap() -> None:"` | — |
| [SRC-3D0DE98F65-L000175](../../tests/test_question_requirement_loop.py#L175) | 175 | `"    plan = fallback_plan(QUESTION)"` | — |
| [SRC-3D0DE98F65-L000176](../../tests/test_question_requirement_loop.py#L176) | 176 | `"    price_query = next(item[\"query\"] for item in plan[\"requirement_queries\"] if item[\"target\"] == \"السعر\")"` | — |
| [SRC-3D0DE98F65-L000177](../../tests/test_question_requirement_loop.py#L177) | 177 | `"    sources = ["` | — |
| [SRC-3D0DE98F65-L000178](../../tests/test_question_requirement_loop.py#L178) | 178 | `"        {"` | — |
| [SRC-3D0DE98F65-L000179](../../tests/test_question_requirement_loop.py#L179) | 179 | `"            \"url\": \"https://example.com/price\","` | — |
| [SRC-3D0DE98F65-L000180](../../tests/test_question_requirement_loop.py#L180) | 180 | `"            \"title\": \"Phone pricing\","` | — |
| [SRC-3D0DE98F65-L000181](../../tests/test_question_requirement_loop.py#L181) | 181 | `"            \"snippet\": \"The price is 100 EGP.\","` | — |
| [SRC-3D0DE98F65-L000182](../../tests/test_question_requirement_loop.py#L182) | 182 | `"            \"page_fetched\": False,"` | — |
| [SRC-3D0DE98F65-L000183](../../tests/test_question_requirement_loop.py#L183) | 183 | `"            \"queries\": [price_query],"` | — |
| [SRC-3D0DE98F65-L000184](../../tests/test_question_requirement_loop.py#L184) | 184 | `"        }"` | — |
| [SRC-3D0DE98F65-L000185](../../tests/test_question_requirement_loop.py#L185) | 185 | `"    ]"` | — |
| [SRC-3D0DE98F65-L000186](../../tests/test_question_requirement_loop.py#L186) | 186 | `""` | — |
| [SRC-3D0DE98F65-L000187](../../tests/test_question_requirement_loop.py#L187) | 187 | `"    result = audit_answer_integrity("` | — |
| [SRC-3D0DE98F65-L000188](../../tests/test_question_requirement_loop.py#L188) | 188 | `"        QUESTION,"` | — |
| [SRC-3D0DE98F65-L000189](../../tests/test_question_requirement_loop.py#L189) | 189 | `"        \"السعر غير محسوم والبطارية غير محسومة والكاميرا غير محسومة.\","` | — |
| [SRC-3D0DE98F65-L000190](../../tests/test_question_requirement_loop.py#L190) | 190 | `"        sources,"` | — |
| [SRC-3D0DE98F65-L000191](../../tests/test_question_requirement_loop.py#L191) | 191 | `"        plan[\"coverage_targets\"],"` | — |
| [SRC-3D0DE98F65-L000192](../../tests/test_question_requirement_loop.py#L192) | 192 | `"        plan[\"requirement_queries\"],"` | — |
| [SRC-3D0DE98F65-L000193](../../tests/test_question_requirement_loop.py#L193) | 193 | `"    )"` | — |
| [SRC-3D0DE98F65-L000194](../../tests/test_question_requirement_loop.py#L194) | 194 | `""` | — |
| [SRC-3D0DE98F65-L000195](../../tests/test_question_requirement_loop.py#L195) | 195 | `"    evidence = {item[\"target\"]: item for item in result[\"requirement_evidence\"]}"` | — |
| [SRC-3D0DE98F65-L000196](../../tests/test_question_requirement_loop.py#L196) | 196 | `"    assert evidence[\"السعر\"][\"status\"] == \"candidate_evidence_found_not_verified\""` | — |
| [SRC-3D0DE98F65-L000197](../../tests/test_question_requirement_loop.py#L197) | 197 | `"    assert evidence[\"البطارية\"][\"status\"] == \"no_candidate_evidence_found\""` | — |
| [SRC-3D0DE98F65-L000198](../../tests/test_question_requirement_loop.py#L198) | 198 | `"    assert result[\"semantic_verification\"] is False"` | — |
| [SRC-3D0DE98F65-L000199](../../tests/test_question_requirement_loop.py#L199) | 199 | `"    assert result[\"requirements_without_candidate_evidence_count\"] == 2"` | — |
| [SRC-3D0DE98F65-L000200](../../tests/test_question_requirement_loop.py#L200) | 200 | `"    assert result[\"target_coverage\"][0][\"evidence\"][\"status\"] == \"candidate_evidence_found_not_verified\""` | — |
| [SRC-3D0DE98F65-L000201](../../tests/test_question_requirement_loop.py#L201) | 201 | `""` | — |
| [SRC-3D0DE98F65-L000202](../../tests/test_question_requirement_loop.py#L202) | 202 | `""` | — |
| [SRC-3D0DE98F65-L000203](../../tests/test_question_requirement_loop.py#L203) | 203 | `"def test_general_compound_factual_question_creates_one_requirement_per_aspect() -> None:"` | — |
| [SRC-3D0DE98F65-L000204](../../tests/test_question_requirement_loop.py#L204) | 204 | `"    question = \"اذكر عاصمة مصر وعدد سكان القاهرة، مع مصدر وتاريخ لكل معلومة\""` | — |
| [SRC-3D0DE98F65-L000205](../../tests/test_question_requirement_loop.py#L205) | 205 | `"    targets = extract_question_coverage_targets(question)"` | — |
| [SRC-3D0DE98F65-L000206](../../tests/test_question_requirement_loop.py#L206) | 206 | `"    assert targets == [\"العاصمة\", \"عدد السكان\"]"` | — |
| [SRC-3D0DE98F65-L000207](../../tests/test_question_requirement_loop.py#L207) | 207 | `""` | — |
| [SRC-3D0DE98F65-L000208](../../tests/test_question_requirement_loop.py#L208) | 208 | `""` | — |
| [SRC-3D0DE98F65-L000209](../../tests/test_question_requirement_loop.py#L209) | 209 | `"def test_general_compound_factual_fallback_plan_keeps_separate_requirement_queries() -> None:"` | — |
| [SRC-3D0DE98F65-L000210](../../tests/test_question_requirement_loop.py#L210) | 210 | `"    question = \"اذكر عاصمة مصر وعدد سكان القاهرة، مع مصدر وتاريخ لكل معلومة\""` | — |
| [SRC-3D0DE98F65-L000211](../../tests/test_question_requirement_loop.py#L211) | 211 | `"    plan = fallback_plan(question)"` | — |
| [SRC-3D0DE98F65-L000212](../../tests/test_question_requirement_loop.py#L212) | 212 | `"    targets = [item[\"target\"] for item in plan[\"requirement_queries\"]]"` | — |
| [SRC-3D0DE98F65-L000213](../../tests/test_question_requirement_loop.py#L213) | 213 | `"    assert targets == [\"العاصمة\", \"عدد السكان\"]"` | — |
| [SRC-3D0DE98F65-L000214](../../tests/test_question_requirement_loop.py#L214) | 214 | `"    assert all(item[\"query\"] in plan[\"queries\"] for item in plan[\"requirement_queries\"])"` | — |
| [SRC-3D0DE98F65-L000215](../../tests/test_question_requirement_loop.py#L215) | 215 | `"    assert len(plan[\"queries\"]) <= MAX_PLAN_QUERIES"` | — |
## اختبارات

### FILE-C353AAAC10 — [tests/test_request_budget.py](../../tests/test_request_budget.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-C353AAAC10-L000001](../../tests/test_request_budget.py#L1) | 1 | `"\"\"\"Unit tests for Omarai's per-request resource budget.\"\"\""` | — |
| [SRC-C353AAAC10-L000002](../../tests/test_request_budget.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-C353AAAC10-L000003](../../tests/test_request_budget.py#L3) | 3 | `""` | — |
| [SRC-C353AAAC10-L000004](../../tests/test_request_budget.py#L4) | 4 | `"import pytest"` | — |
| [SRC-C353AAAC10-L000005](../../tests/test_request_budget.py#L5) | 5 | `""` | — |
| [SRC-C353AAAC10-L000006](../../tests/test_request_budget.py#L6) | 6 | `"from agents.request_budget import RequestBudget, RequestBudgetExceeded"` | — |
| [SRC-C353AAAC10-L000007](../../tests/test_request_budget.py#L7) | 7 | `""` | — |
| [SRC-C353AAAC10-L000008](../../tests/test_request_budget.py#L8) | 8 | `""` | — |
| [SRC-C353AAAC10-L000009](../../tests/test_request_budget.py#L9) | 9 | `"class FakeClock:"` | — |
| [SRC-C353AAAC10-L000010](../../tests/test_request_budget.py#L10) | 10 | `"    def __init__(self, value: float = 100.0) -> None:"` | — |
| [SRC-C353AAAC10-L000011](../../tests/test_request_budget.py#L11) | 11 | `"        self.value = value"` | — |
| [SRC-C353AAAC10-L000012](../../tests/test_request_budget.py#L12) | 12 | `""` | — |
| [SRC-C353AAAC10-L000013](../../tests/test_request_budget.py#L13) | 13 | `"    def __call__(self) -> float:"` | — |
| [SRC-C353AAAC10-L000014](../../tests/test_request_budget.py#L14) | 14 | `"        return self.value"` | — |
| [SRC-C353AAAC10-L000015](../../tests/test_request_budget.py#L15) | 15 | `""` | — |
| [SRC-C353AAAC10-L000016](../../tests/test_request_budget.py#L16) | 16 | `""` | — |
| [SRC-C353AAAC10-L000017](../../tests/test_request_budget.py#L17) | 17 | `"def test_resource_reservations_are_bounded_and_thread_safe_in_snapshot():"` | — |
| [SRC-C353AAAC10-L000018](../../tests/test_request_budget.py#L18) | 18 | `"    clock = FakeClock()"` | — |
| [SRC-C353AAAC10-L000019](../../tests/test_request_budget.py#L19) | 19 | `"    budget = RequestBudget("` | — |
| [SRC-C353AAAC10-L000020](../../tests/test_request_budget.py#L20) | 20 | `"        timeout_seconds=10,"` | — |
| [SRC-C353AAAC10-L000021](../../tests/test_request_budget.py#L21) | 21 | `"        limits={\"search_calls\": 1},"` | — |
| [SRC-C353AAAC10-L000022](../../tests/test_request_budget.py#L22) | 22 | `"        clock=clock,"` | — |
| [SRC-C353AAAC10-L000023](../../tests/test_request_budget.py#L23) | 23 | `"    )"` | — |
| [SRC-C353AAAC10-L000024](../../tests/test_request_budget.py#L24) | 24 | `""` | — |
| [SRC-C353AAAC10-L000025](../../tests/test_request_budget.py#L25) | 25 | `"    budget.reserve(\"search_calls\")"` | — |
| [SRC-C353AAAC10-L000026](../../tests/test_request_budget.py#L26) | 26 | `"    with pytest.raises(RequestBudgetExceeded, match=\"search_calls\"):"` | — |
| [SRC-C353AAAC10-L000027](../../tests/test_request_budget.py#L27) | 27 | `"        budget.reserve(\"search_calls\")"` | — |
| [SRC-C353AAAC10-L000028](../../tests/test_request_budget.py#L28) | 28 | `""` | — |
| [SRC-C353AAAC10-L000029](../../tests/test_request_budget.py#L29) | 29 | `"    snapshot = budget.snapshot()"` | — |
| [SRC-C353AAAC10-L000030](../../tests/test_request_budget.py#L30) | 30 | `"    assert snapshot[\"counts\"][\"search_calls\"] == 1"` | — |
| [SRC-C353AAAC10-L000031](../../tests/test_request_budget.py#L31) | 31 | `"    assert snapshot[\"limits\"][\"search_calls\"] == 1"` | — |
| [SRC-C353AAAC10-L000032](../../tests/test_request_budget.py#L32) | 32 | `"    assert snapshot[\"deadline_exceeded\"] is False"` | — |
| [SRC-C353AAAC10-L000033](../../tests/test_request_budget.py#L33) | 33 | `""` | — |
| [SRC-C353AAAC10-L000034](../../tests/test_request_budget.py#L34) | 34 | `""` | — |
| [SRC-C353AAAC10-L000035](../../tests/test_request_budget.py#L35) | 35 | `"def test_deadline_blocks_new_work_and_caps_outbound_timeout():"` | — |
| [SRC-C353AAAC10-L000036](../../tests/test_request_budget.py#L36) | 36 | `"    clock = FakeClock()"` | — |
| [SRC-C353AAAC10-L000037](../../tests/test_request_budget.py#L37) | 37 | `"    budget = RequestBudget(timeout_seconds=10, clock=clock)"` | — |
| [SRC-C353AAAC10-L000038](../../tests/test_request_budget.py#L38) | 38 | `""` | — |
| [SRC-C353AAAC10-L000039](../../tests/test_request_budget.py#L39) | 39 | `"    clock.value += 7"` | — |
| [SRC-C353AAAC10-L000040](../../tests/test_request_budget.py#L40) | 40 | `"    assert budget.timeout_for(30) == pytest.approx(3)"` | — |
| [SRC-C353AAAC10-L000041](../../tests/test_request_budget.py#L41) | 41 | `"    assert budget.timeout_for(1) == pytest.approx(1)"` | — |
| [SRC-C353AAAC10-L000042](../../tests/test_request_budget.py#L42) | 42 | `""` | — |
| [SRC-C353AAAC10-L000043](../../tests/test_request_budget.py#L43) | 43 | `"    clock.value += 4"` | — |
| [SRC-C353AAAC10-L000044](../../tests/test_request_budget.py#L44) | 44 | `"    assert budget.remaining_seconds() == 0"` | — |
| [SRC-C353AAAC10-L000045](../../tests/test_request_budget.py#L45) | 45 | `"    with pytest.raises(RequestBudgetExceeded, match=\"وقت الطلب\"):"` | — |
| [SRC-C353AAAC10-L000046](../../tests/test_request_budget.py#L46) | 46 | `"        budget.reserve(\"model_calls\")"` | — |
| [SRC-C353AAAC10-L000047](../../tests/test_request_budget.py#L47) | 47 | `"    with pytest.raises(RequestBudgetExceeded, match=\"وقت الطلب\"):"` | — |
| [SRC-C353AAAC10-L000048](../../tests/test_request_budget.py#L48) | 48 | `"        budget.timeout_for(3)"` | — |
| [SRC-C353AAAC10-L000049](../../tests/test_request_budget.py#L49) | 49 | `""` | — |
| [SRC-C353AAAC10-L000050](../../tests/test_request_budget.py#L50) | 50 | `""` | — |
| [SRC-C353AAAC10-L000051](../../tests/test_request_budget.py#L51) | 51 | `"def test_environment_overrides_are_clamped(monkeypatch):"` | — |
| [SRC-C353AAAC10-L000052](../../tests/test_request_budget.py#L52) | 52 | `"    monkeypatch.setenv(\"OMARAI_REQUEST_BUDGET_SECONDS\", \"999\")"` | — |
| [SRC-C353AAAC10-L000053](../../tests/test_request_budget.py#L53) | 53 | `"    monkeypatch.setenv(\"OMARAI_REQUEST_MAX_SEARCH_CALLS\", \"999\")"` | — |
| [SRC-C353AAAC10-L000054](../../tests/test_request_budget.py#L54) | 54 | `"    monkeypatch.setenv(\"OMARAI_REQUEST_MAX_MODEL_CALLS\", \"-1\")"` | — |
| [SRC-C353AAAC10-L000055](../../tests/test_request_budget.py#L55) | 55 | `"    monkeypatch.setenv(\"OMARAI_REQUEST_MAX_TOOL_CALLS\", \"-1\")"` | — |
| [SRC-C353AAAC10-L000056](../../tests/test_request_budget.py#L56) | 56 | `""` | — |
| [SRC-C353AAAC10-L000057](../../tests/test_request_budget.py#L57) | 57 | `"    snapshot = RequestBudget.from_environment().snapshot()"` | — |
| [SRC-C353AAAC10-L000058](../../tests/test_request_budget.py#L58) | 58 | `""` | — |
| [SRC-C353AAAC10-L000059](../../tests/test_request_budget.py#L59) | 59 | `"    assert snapshot[\"timeout_seconds\"] == 120"` | — |
| [SRC-C353AAAC10-L000060](../../tests/test_request_budget.py#L60) | 60 | `"    assert snapshot[\"limits\"][\"search_calls\"] == 40"` | — |
| [SRC-C353AAAC10-L000061](../../tests/test_request_budget.py#L61) | 61 | `"    assert snapshot[\"limits\"][\"model_calls\"] == 1"` | — |
| [SRC-C353AAAC10-L000062](../../tests/test_request_budget.py#L62) | 62 | `"    assert snapshot[\"limits\"][\"tool_calls\"] == 0"` | — |
| [SRC-C353AAAC10-L000063](../../tests/test_request_budget.py#L63) | 63 | `""` | — |
| [SRC-C353AAAC10-L000064](../../tests/test_request_budget.py#L64) | 64 | `""` | — |
| [SRC-C353AAAC10-L000065](../../tests/test_request_budget.py#L65) | 65 | `"def test_web_agent_reserves_search_model_and_page_work_before_io(monkeypatch):"` | — |
| [SRC-C353AAAC10-L000066](../../tests/test_request_budget.py#L66) | 66 | `"    from agents.web_agent import WebAgent"` | — |
| [SRC-C353AAAC10-L000067](../../tests/test_request_budget.py#L67) | 67 | `""` | — |
| [SRC-C353AAAC10-L000068](../../tests/test_request_budget.py#L68) | 68 | `"    agent = WebAgent()"` | — |
| [SRC-C353AAAC10-L000069](../../tests/test_request_budget.py#L69) | 69 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-C353AAAC10-L000070](../../tests/test_request_budget.py#L70) | 70 | `""` | — |
| [SRC-C353AAAC10-L000071](../../tests/test_request_budget.py#L71) | 71 | `"    agent._request_budget = RequestBudget(limits={\"search_queries\": 0})"` | — |
| [SRC-C353AAAC10-L000072](../../tests/test_request_budget.py#L72) | 72 | `"    with pytest.raises(RequestBudgetExceeded, match=\"search_queries\"):"` | — |
| [SRC-C353AAAC10-L000073](../../tests/test_request_budget.py#L73) | 73 | `"        agent._search_web(\"budget test\")"` | — |
| [SRC-C353AAAC10-L000074](../../tests/test_request_budget.py#L74) | 74 | `""` | — |
| [SRC-C353AAAC10-L000075](../../tests/test_request_budget.py#L75) | 75 | `"    agent._request_budget = RequestBudget(limits={\"model_calls\": 0})"` | — |
| [SRC-C353AAAC10-L000076](../../tests/test_request_budget.py#L76) | 76 | `"    monkeypatch.setattr("` | — |
| [SRC-C353AAAC10-L000077](../../tests/test_request_budget.py#L77) | 77 | `"        \"agents.web_agent.urllib.request.urlopen\","` | — |
| [SRC-C353AAAC10-L000078](../../tests/test_request_budget.py#L78) | 78 | `"        lambda *args, **kwargs: pytest.fail(\"model HTTP request must not start\"),"` | — |
| [SRC-C353AAAC10-L000079](../../tests/test_request_budget.py#L79) | 79 | `"    )"` | — |
| [SRC-C353AAAC10-L000080](../../tests/test_request_budget.py#L80) | 80 | `"    with pytest.raises(RequestBudgetExceeded, match=\"model_calls\"):"` | — |
| [SRC-C353AAAC10-L000081](../../tests/test_request_budget.py#L81) | 81 | `"        agent._request_completion([{\"role\": \"user\", \"content\": \"test\"}])"` | — |
| [SRC-C353AAAC10-L000082](../../tests/test_request_budget.py#L82) | 82 | `""` | — |
| [SRC-C353AAAC10-L000083](../../tests/test_request_budget.py#L83) | 83 | `"    agent._request_budget = RequestBudget(limits={\"page_fetches\": 0})"` | — |
| [SRC-C353AAAC10-L000084](../../tests/test_request_budget.py#L84) | 84 | `"    with pytest.raises(RequestBudgetExceeded, match=\"page_fetches\"):"` | — |
| [SRC-C353AAAC10-L000085](../../tests/test_request_budget.py#L85) | 85 | `"        agent._fetch_page(\"https://example.com/\")"` | — |
| [SRC-C353AAAC10-L000086](../../tests/test_request_budget.py#L86) | 86 | `""` | — |
| [SRC-C353AAAC10-L000087](../../tests/test_request_budget.py#L87) | 87 | `""` | — |
| [SRC-C353AAAC10-L000088](../../tests/test_request_budget.py#L88) | 88 | `"def test_social_provider_reserves_budget_before_network_io(monkeypatch):"` | — |
| [SRC-C353AAAC10-L000089](../../tests/test_request_budget.py#L89) | 89 | `"    from agents.web_agent import WebAgent"` | — |
| [SRC-C353AAAC10-L000090](../../tests/test_request_budget.py#L90) | 90 | `""` | — |
| [SRC-C353AAAC10-L000091](../../tests/test_request_budget.py#L91) | 91 | `"    monkeypatch.setenv(\"REDDIT_CLIENT_ID\", \"test-client\")"` | — |
| [SRC-C353AAAC10-L000092](../../tests/test_request_budget.py#L92) | 92 | `"    monkeypatch.setenv(\"REDDIT_CLIENT_SECRET\", \"test-secret\")"` | — |
| [SRC-C353AAAC10-L000093](../../tests/test_request_budget.py#L93) | 93 | `"    agent = WebAgent()"` | — |
| [SRC-C353AAAC10-L000094](../../tests/test_request_budget.py#L94) | 94 | `"    agent._request_budget = RequestBudget(limits={\"search_calls\": 0})"` | — |
| [SRC-C353AAAC10-L000095](../../tests/test_request_budget.py#L95) | 95 | `""` | — |
| [SRC-C353AAAC10-L000096](../../tests/test_request_budget.py#L96) | 96 | `"    monkeypatch.setattr("` | — |
| [SRC-C353AAAC10-L000097](../../tests/test_request_budget.py#L97) | 97 | `"        \"httpx.post\","` | — |
| [SRC-C353AAAC10-L000098](../../tests/test_request_budget.py#L98) | 98 | `"        lambda *args, **kwargs: pytest.fail(\"social HTTP request must not start\"),"` | — |
| [SRC-C353AAAC10-L000099](../../tests/test_request_budget.py#L99) | 99 | `"    )"` | — |
| [SRC-C353AAAC10-L000100](../../tests/test_request_budget.py#L100) | 100 | `"    with pytest.raises(RequestBudgetExceeded, match=\"search_calls\"):"` | — |
| [SRC-C353AAAC10-L000101](../../tests/test_request_budget.py#L101) | 101 | `"        agent._search_social(\"budget test\", [\"reddit\"])"` | — |
| [SRC-C353AAAC10-L000102](../../tests/test_request_budget.py#L102) | 102 | `""` | — |
| [SRC-C353AAAC10-L000103](../../tests/test_request_budget.py#L103) | 103 | `""` | — |
| [SRC-C353AAAC10-L000104](../../tests/test_request_budget.py#L104) | 104 | `"@pytest.mark.parametrize("` | — |
| [SRC-C353AAAC10-L000105](../../tests/test_request_budget.py#L105) | 105 | `"    (\"resource\", \"limit\"),"` | — |
| [SRC-C353AAAC10-L000106](../../tests/test_request_budget.py#L106) | 106 | `"    ["` | — |
| [SRC-C353AAAC10-L000107](../../tests/test_request_budget.py#L107) | 107 | `"        (\"search_queries\", 8),"` | — |
| [SRC-C353AAAC10-L000108](../../tests/test_request_budget.py#L108) | 108 | `"        (\"search_calls\", 32),"` | — |
| [SRC-C353AAAC10-L000109](../../tests/test_request_budget.py#L109) | 109 | `"        (\"model_calls\", 8),"` | — |
| [SRC-C353AAAC10-L000110](../../tests/test_request_budget.py#L110) | 110 | `"        (\"page_fetches\", 8),"` | — |
| [SRC-C353AAAC10-L000111](../../tests/test_request_budget.py#L111) | 111 | `"        (\"tool_calls\", 3),"` | — |
| [SRC-C353AAAC10-L000112](../../tests/test_request_budget.py#L112) | 112 | `"    ],"` | — |
| [SRC-C353AAAC10-L000113](../../tests/test_request_budget.py#L113) | 113 | `")"` | — |
| [SRC-C353AAAC10-L000114](../../tests/test_request_budget.py#L114) | 114 | `"def test_each_resource_counter_stops_at_its_limit(resource, limit):"` | — |
| [SRC-C353AAAC10-L000115](../../tests/test_request_budget.py#L115) | 115 | `"    budget = RequestBudget(timeout_seconds=10, limits={resource: limit})"` | — |
| [SRC-C353AAAC10-L000116](../../tests/test_request_budget.py#L116) | 116 | `""` | — |
| [SRC-C353AAAC10-L000117](../../tests/test_request_budget.py#L117) | 117 | `"    for expected_count in range(1, limit + 1):"` | — |
| [SRC-C353AAAC10-L000118](../../tests/test_request_budget.py#L118) | 118 | `"        budget.reserve(resource)"` | — |
| [SRC-C353AAAC10-L000119](../../tests/test_request_budget.py#L119) | 119 | `"        snapshot = budget.snapshot()"` | — |
| [SRC-C353AAAC10-L000120](../../tests/test_request_budget.py#L120) | 120 | `"        assert snapshot[\"counts\"][resource] == expected_count"` | — |
