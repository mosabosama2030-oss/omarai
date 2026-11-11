# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **055**
- سجلات الأسطر: **800**
- النطاق: SRC-44CDA52D01-L000186 إلى SRC-6BF96689A8-L000056
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-44CDA52D01 — [tests/test_omarai.py](../../tests/test_omarai.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-44CDA52D01-L000186](../../tests/test_omarai.py#L186) | 186 | `"    assert result[\"label\"] == \"high_intent\""` | — |
| [SRC-44CDA52D01-L000187](../../tests/test_omarai.py#L187) | 187 | `"    assert result[\"signal_type\"] == \"direct_purchase_request\""` | — |
| [SRC-44CDA52D01-L000188](../../tests/test_omarai.py#L188) | 188 | `""` | — |
| [SRC-44CDA52D01-L000189](../../tests/test_omarai.py#L189) | 189 | `""` | — |
| [SRC-44CDA52D01-L000190](../../tests/test_omarai.py#L190) | 190 | `"@pytest.mark.parametrize("` | — |
| [SRC-44CDA52D01-L000191](../../tests/test_omarai.py#L191) | 191 | `"    \"text\","` | — |
| [SRC-44CDA52D01-L000192](../../tests/test_omarai.py#L192) | 192 | `"    ["` | — |
| [SRC-44CDA52D01-L000193](../../tests/test_omarai.py#L193) | 193 | `"        \"نظام انذار حريق شركتنا تبيعه\","` | — |
| [SRC-44CDA52D01-L000194](../../tests/test_omarai.py#L194) | 194 | `"        \"مطلوب مهندس مبيعات\","` | — |
| [SRC-44CDA52D01-L000195](../../tests/test_omarai.py#L195) | 195 | `"        \"ما هي افضل انظمة الانذار\","` | — |
| [SRC-44CDA52D01-L000196](../../tests/test_omarai.py#L196) | 196 | `"    ],"` | — |
| [SRC-44CDA52D01-L000197](../../tests/test_omarai.py#L197) | 197 | `")"` | — |
| [SRC-44CDA52D01-L000198](../../tests/test_omarai.py#L198) | 198 | `"def test_product_mention_or_job_ad_is_not_a_buying_signal(text):"` | — |
| [SRC-44CDA52D01-L000199](../../tests/test_omarai.py#L199) | 199 | `"    result = analyze(text)"` | — |
| [SRC-44CDA52D01-L000200](../../tests/test_omarai.py#L200) | 200 | `"    assert result[\"score\"] == 0"` | — |
| [SRC-44CDA52D01-L000201](../../tests/test_omarai.py#L201) | 201 | `"    assert result[\"label\"] == \"unclear\""` | — |
| [SRC-44CDA52D01-L000202](../../tests/test_omarai.py#L202) | 202 | `""` | — |
| [SRC-44CDA52D01-L000203](../../tests/test_omarai.py#L203) | 203 | `""` | — |
| [SRC-44CDA52D01-L000204](../../tests/test_omarai.py#L204) | 204 | `"def test_procurement_phrase_with_negation_or_closure_is_not_live():"` | — |
| [SRC-44CDA52D01-L000205](../../tests/test_omarai.py#L205) | 205 | `"    assert analyze(\"مش محتاج نظام انذار\")[\"label\"] == \"not_buyer_signal\""` | — |
| [SRC-44CDA52D01-L000206](../../tests/test_omarai.py#L206) | 206 | `"    assert analyze(\"تم التعاقد على نظام انذار حريق\")[\"label\"] == \"closed_or_stale_signal\""` | — |
## اختبارات

### FILE-851E7A87D6 — [tests/test_postgres_store.py](../../tests/test_postgres_store.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-851E7A87D6-L000001](../../tests/test_postgres_store.py#L1) | 1 | `"\"\"\"PostgreSQL integration tests for the Neon-backed LeadStore."` | — |
| [SRC-851E7A87D6-L000002](../../tests/test_postgres_store.py#L2) | 2 | `""` | — |
| [SRC-851E7A87D6-L000003](../../tests/test_postgres_store.py#L3) | 3 | `"These tests run only when OMARAI_TEST_DATABASE_URL points at an isolated test database."` | — |
| [SRC-851E7A87D6-L000004](../../tests/test_postgres_store.py#L4) | 4 | `"The CI workflow supplies an ephemeral PostgreSQL service; production credentials are never used."` | — |
| [SRC-851E7A87D6-L000005](../../tests/test_postgres_store.py#L5) | 5 | `"\"\"\""` | — |
| [SRC-851E7A87D6-L000006](../../tests/test_postgres_store.py#L6) | 6 | `"from __future__ import annotations"` | — |
| [SRC-851E7A87D6-L000007](../../tests/test_postgres_store.py#L7) | 7 | `""` | — |
| [SRC-851E7A87D6-L000008](../../tests/test_postgres_store.py#L8) | 8 | `"import os"` | — |
| [SRC-851E7A87D6-L000009](../../tests/test_postgres_store.py#L9) | 9 | `"import uuid"` | — |
| [SRC-851E7A87D6-L000010](../../tests/test_postgres_store.py#L10) | 10 | `""` | — |
| [SRC-851E7A87D6-L000011](../../tests/test_postgres_store.py#L11) | 11 | `"import pytest"` | — |
| [SRC-851E7A87D6-L000012](../../tests/test_postgres_store.py#L12) | 12 | `""` | — |
| [SRC-851E7A87D6-L000013](../../tests/test_postgres_store.py#L13) | 13 | `"from agents.omarai import LeadStore, _PostgresConnection, _qmark_to_psycopg"` | — |
| [SRC-851E7A87D6-L000014](../../tests/test_postgres_store.py#L14) | 14 | `""` | — |
| [SRC-851E7A87D6-L000015](../../tests/test_postgres_store.py#L15) | 15 | `""` | — |
| [SRC-851E7A87D6-L000016](../../tests/test_postgres_store.py#L16) | 16 | `"@pytest.fixture"` | — |
| [SRC-851E7A87D6-L000017](../../tests/test_postgres_store.py#L17) | 17 | `"def postgres_store():"` | — |
| [SRC-851E7A87D6-L000018](../../tests/test_postgres_store.py#L18) | 18 | `"    database_url = os.getenv(\"OMARAI_TEST_DATABASE_URL\", \"\").strip()"` | — |
| [SRC-851E7A87D6-L000019](../../tests/test_postgres_store.py#L19) | 19 | `"    if not database_url:"` | — |
| [SRC-851E7A87D6-L000020](../../tests/test_postgres_store.py#L20) | 20 | `"        pytest.skip(\"OMARAI_TEST_DATABASE_URL is not configured\")"` | — |
| [SRC-851E7A87D6-L000021](../../tests/test_postgres_store.py#L21) | 21 | `"    return LeadStore(database_url=database_url)"` | — |
| [SRC-851E7A87D6-L000022](../../tests/test_postgres_store.py#L22) | 22 | `""` | — |
| [SRC-851E7A87D6-L000023](../../tests/test_postgres_store.py#L23) | 23 | `""` | — |
| [SRC-851E7A87D6-L000024](../../tests/test_postgres_store.py#L24) | 24 | `"def _tenant_user(store: LeadStore, marker: str) -> tuple[str, str]:"` | — |
| [SRC-851E7A87D6-L000025](../../tests/test_postgres_store.py#L25) | 25 | `"    tenant_id = store.create_tenant(f\"PostgreSQL test {marker}\", f\"pg-{marker}\")"` | — |
| [SRC-851E7A87D6-L000026](../../tests/test_postgres_store.py#L26) | 26 | `"    user_id = store.create_user(f\"{marker}@example.invalid\", f\"PostgreSQL {marker}\")"` | — |
| [SRC-851E7A87D6-L000027](../../tests/test_postgres_store.py#L27) | 27 | `"    store.add_membership(tenant_id, user_id, \"owner\")"` | — |
| [SRC-851E7A87D6-L000028](../../tests/test_postgres_store.py#L28) | 28 | `"    return tenant_id, user_id"` | — |
| [SRC-851E7A87D6-L000029](../../tests/test_postgres_store.py#L29) | 29 | `""` | — |
| [SRC-851E7A87D6-L000030](../../tests/test_postgres_store.py#L30) | 30 | `""` | — |
| [SRC-851E7A87D6-L000031](../../tests/test_postgres_store.py#L31) | 31 | `"def test_postgres_leads_preserve_tenant_scoping_and_duplicate_semantics(postgres_store):"` | — |
| [SRC-851E7A87D6-L000032](../../tests/test_postgres_store.py#L32) | 32 | `"    marker = uuid.uuid4().hex"` | — |
| [SRC-851E7A87D6-L000033](../../tests/test_postgres_store.py#L33) | 33 | `"    tenant_a, _ = _tenant_user(postgres_store, f\"a-{marker}\")"` | — |
| [SRC-851E7A87D6-L000034](../../tests/test_postgres_store.py#L34) | 34 | `"    tenant_b, _ = _tenant_user(postgres_store, f\"b-{marker}\")"` | — |
| [SRC-851E7A87D6-L000035](../../tests/test_postgres_store.py#L35) | 35 | `"    text = f\"نبحث عن مورد لتجهيزات اختبار PostgreSQL {marker}\""` | — |
| [SRC-851E7A87D6-L000036](../../tests/test_postgres_store.py#L36) | 36 | `"    source_url = f\"https://example.com/postgres/{marker}\""` | — |
| [SRC-851E7A87D6-L000037](../../tests/test_postgres_store.py#L37) | 37 | `""` | — |
| [SRC-851E7A87D6-L000038](../../tests/test_postgres_store.py#L38) | 38 | `"    lead_a, created_a = postgres_store.add(text, source_url, tenant_id=tenant_a)"` | — |
| [SRC-851E7A87D6-L000039](../../tests/test_postgres_store.py#L39) | 39 | `"    lead_b, created_b = postgres_store.add(text, source_url, tenant_id=tenant_b)"` | — |
| [SRC-851E7A87D6-L000040](../../tests/test_postgres_store.py#L40) | 40 | `""` | — |
| [SRC-851E7A87D6-L000041](../../tests/test_postgres_store.py#L41) | 41 | `"    assert created_a is True"` | — |
| [SRC-851E7A87D6-L000042](../../tests/test_postgres_store.py#L42) | 42 | `"    assert created_b is True"` | — |
| [SRC-851E7A87D6-L000043](../../tests/test_postgres_store.py#L43) | 43 | `"    assert lead_a[\"id\"] != lead_b[\"id\"]"` | — |
| [SRC-851E7A87D6-L000044](../../tests/test_postgres_store.py#L44) | 44 | `"    assert [row[\"id\"] for row in postgres_store.list(tenant_id=tenant_a)] == [lead_a[\"id\"]]"` | — |
| [SRC-851E7A87D6-L000045](../../tests/test_postgres_store.py#L45) | 45 | `"    assert [row[\"id\"] for row in postgres_store.list(tenant_id=tenant_b)] == [lead_b[\"id\"]]"` | — |
| [SRC-851E7A87D6-L000046](../../tests/test_postgres_store.py#L46) | 46 | `""` | — |
| [SRC-851E7A87D6-L000047](../../tests/test_postgres_store.py#L47) | 47 | `"    duplicate, created_again = postgres_store.add("` | — |
| [SRC-851E7A87D6-L000048](../../tests/test_postgres_store.py#L48) | 48 | `"        text, source_url, tenant_id=tenant_a"` | — |
| [SRC-851E7A87D6-L000049](../../tests/test_postgres_store.py#L49) | 49 | `"    )"` | — |
| [SRC-851E7A87D6-L000050](../../tests/test_postgres_store.py#L50) | 50 | `"    assert created_again is False"` | — |
| [SRC-851E7A87D6-L000051](../../tests/test_postgres_store.py#L51) | 51 | `"    assert duplicate[\"id\"] == lead_a[\"id\"]"` | — |
| [SRC-851E7A87D6-L000052](../../tests/test_postgres_store.py#L52) | 52 | `""` | — |
| [SRC-851E7A87D6-L000053](../../tests/test_postgres_store.py#L53) | 53 | `"    assert postgres_store.update_status("` | — |
| [SRC-851E7A87D6-L000054](../../tests/test_postgres_store.py#L54) | 54 | `"        lead_a[\"id\"], \"qualified\", tenant_id=tenant_b"` | — |
| [SRC-851E7A87D6-L000055](../../tests/test_postgres_store.py#L55) | 55 | `"    ) is None"` | — |
| [SRC-851E7A87D6-L000056](../../tests/test_postgres_store.py#L56) | 56 | `"    updated = postgres_store.update_status("` | — |
| [SRC-851E7A87D6-L000057](../../tests/test_postgres_store.py#L57) | 57 | `"        lead_a[\"id\"], \"qualified\", tenant_id=tenant_a"` | — |
| [SRC-851E7A87D6-L000058](../../tests/test_postgres_store.py#L58) | 58 | `"    )"` | — |
| [SRC-851E7A87D6-L000059](../../tests/test_postgres_store.py#L59) | 59 | `"    assert updated[\"status\"] == \"qualified\""` | — |
| [SRC-851E7A87D6-L000060](../../tests/test_postgres_store.py#L60) | 60 | `"    assert postgres_store.list(\"qualified\", tenant_id=tenant_a)[0][\"id\"] == lead_a[\"id\"]"` | — |
| [SRC-851E7A87D6-L000061](../../tests/test_postgres_store.py#L61) | 61 | `"    assert postgres_store.list(tenant_id=tenant_b)[0][\"status\"] == \"new\""` | — |
| [SRC-851E7A87D6-L000062](../../tests/test_postgres_store.py#L62) | 62 | `""` | — |
| [SRC-851E7A87D6-L000063](../../tests/test_postgres_store.py#L63) | 63 | `""` | — |
| [SRC-851E7A87D6-L000064](../../tests/test_postgres_store.py#L64) | 64 | `"def test_postgres_tokens_sessions_and_reusable_workspace_records(postgres_store):"` | — |
| [SRC-851E7A87D6-L000065](../../tests/test_postgres_store.py#L65) | 65 | `"    marker = uuid.uuid4().hex"` | — |
| [SRC-851E7A87D6-L000066](../../tests/test_postgres_store.py#L66) | 66 | `"    tenant_id, user_id = _tenant_user(postgres_store, marker)"` | — |
| [SRC-851E7A87D6-L000067](../../tests/test_postgres_store.py#L67) | 67 | `"    token = f\"postgres-test-{marker}-\" + (\"T\" * 40)"` | — |
| [SRC-851E7A87D6-L000068](../../tests/test_postgres_store.py#L68) | 68 | `""` | — |
| [SRC-851E7A87D6-L000069](../../tests/test_postgres_store.py#L69) | 69 | `"    postgres_store.create_api_token(token, tenant_id, user_id, label=\"integration\")"` | — |
| [SRC-851E7A87D6-L000070](../../tests/test_postgres_store.py#L70) | 70 | `"    principal = postgres_store.resolve_api_token(token)"` | — |
| [SRC-851E7A87D6-L000071](../../tests/test_postgres_store.py#L71) | 71 | `"    assert principal == {\"tenant_id\": tenant_id, \"user_id\": user_id, \"role\": \"owner\"}"` | — |
| [SRC-851E7A87D6-L000072](../../tests/test_postgres_store.py#L72) | 72 | `""` | — |
| [SRC-851E7A87D6-L000073](../../tests/test_postgres_store.py#L73) | 73 | `"    created_session = postgres_store.create_web_session(token)"` | — |
| [SRC-851E7A87D6-L000074](../../tests/test_postgres_store.py#L74) | 74 | `"    assert created_session is not None"` | — |
| [SRC-851E7A87D6-L000075](../../tests/test_postgres_store.py#L75) | 75 | `"    session_id, session_principal = created_session"` | — |
| [SRC-851E7A87D6-L000076](../../tests/test_postgres_store.py#L76) | 76 | `"    assert session_principal == principal"` | — |
| [SRC-851E7A87D6-L000077](../../tests/test_postgres_store.py#L77) | 77 | `"    assert postgres_store.resolve_web_session(session_id) == principal"` | — |
| [SRC-851E7A87D6-L000078](../../tests/test_postgres_store.py#L78) | 78 | `"    assert postgres_store.revoke_web_session(session_id) is True"` | — |
| [SRC-851E7A87D6-L000079](../../tests/test_postgres_store.py#L79) | 79 | `"    assert postgres_store.resolve_web_session(session_id) is None"` | — |
| [SRC-851E7A87D6-L000080](../../tests/test_postgres_store.py#L80) | 80 | `""` | — |
| [SRC-851E7A87D6-L000081](../../tests/test_postgres_store.py#L81) | 81 | `"    profile_input = {"` | — |
| [SRC-851E7A87D6-L000082](../../tests/test_postgres_store.py#L82) | 82 | `"        \"product\": {\"name\": f\"PostgreSQL Widget {marker}\", \"aliases\": [\"Widget\"]},"` | — |
| [SRC-851E7A87D6-L000083](../../tests/test_postgres_store.py#L83) | 83 | `"        \"market\": {\"locations\": [\"Cairo\"], \"industries\": [\"Testing\"]},"` | — |
| [SRC-851E7A87D6-L000084](../../tests/test_postgres_store.py#L84) | 84 | `"    }"` | — |
| [SRC-851E7A87D6-L000085](../../tests/test_postgres_store.py#L85) | 85 | `"    profile = postgres_store.save_product_profile(profile_input, tenant_id=tenant_id)"` | — |
| [SRC-851E7A87D6-L000086](../../tests/test_postgres_store.py#L86) | 86 | `"    assert profile[\"name\"] == profile_input[\"product\"][\"name\"]"` | — |
| [SRC-851E7A87D6-L000087](../../tests/test_postgres_store.py#L87) | 87 | `"    assert postgres_store.get_product_profile("` | — |
| [SRC-851E7A87D6-L000088](../../tests/test_postgres_store.py#L88) | 88 | `"        profile[\"id\"], tenant_id=tenant_id"` | — |
| [SRC-851E7A87D6-L000089](../../tests/test_postgres_store.py#L89) | 89 | `"    )[\"profile\"] == profile_input"` | — |
| [SRC-851E7A87D6-L000090](../../tests/test_postgres_store.py#L90) | 90 | `"    assert postgres_store.list_product_profiles(tenant_id=tenant_id)[0][\"id\"] == profile[\"id\"]"` | — |
| [SRC-851E7A87D6-L000091](../../tests/test_postgres_store.py#L91) | 91 | `""` | — |
| [SRC-851E7A87D6-L000092](../../tests/test_postgres_store.py#L92) | 92 | `"    run = postgres_store.save_discovery_run("` | — |
| [SRC-851E7A87D6-L000093](../../tests/test_postgres_store.py#L93) | 93 | `"        profile[\"id\"],"` | — |
| [SRC-851E7A87D6-L000094](../../tests/test_postgres_store.py#L94) | 94 | `"        {"` | — |
| [SRC-851E7A87D6-L000095](../../tests/test_postgres_store.py#L95) | 95 | `"            \"answer\": \"تم العثور على طلب توريد معلن.\","` | — |
| [SRC-851E7A87D6-L000096](../../tests/test_postgres_store.py#L96) | 96 | `"            \"kind\": \"lead_discovery\","` | — |
| [SRC-851E7A87D6-L000097](../../tests/test_postgres_store.py#L97) | 97 | `"            \"search_queries\": [\"نبحث عن مورد\"],"` | — |
| [SRC-851E7A87D6-L000098](../../tests/test_postgres_store.py#L98) | 98 | `"            \"sources\": [{"` | — |
| [SRC-851E7A87D6-L000099](../../tests/test_postgres_store.py#L99) | 99 | `"                \"title\": \"طلب مورد تجريبي\","` | — |
| [SRC-851E7A87D6-L000100](../../tests/test_postgres_store.py#L100) | 100 | `"                \"url\": f\"https://example.com/demand/{marker}\","` | — |
| [SRC-851E7A87D6-L000101](../../tests/test_postgres_store.py#L101) | 101 | `"                \"snippet\": \"نبحث عن مورد لتوريد المنتج\","` | — |
| [SRC-851E7A87D6-L000102](../../tests/test_postgres_store.py#L102) | 102 | `"                \"platform\": \"web\","` | — |
| [SRC-851E7A87D6-L000103](../../tests/test_postgres_store.py#L103) | 103 | `"                \"lead_qualification\": \"public_demand_signal\","` | — |
| [SRC-851E7A87D6-L000104](../../tests/test_postgres_store.py#L104) | 104 | `"                \"lead_intent_evidence\": {"` | — |
| [SRC-851E7A87D6-L000105](../../tests/test_postgres_store.py#L105) | 105 | `"                    \"phrase\": \"نبحث عن مورد\","` | — |
| [SRC-851E7A87D6-L000106](../../tests/test_postgres_store.py#L106) | 106 | `"                    \"basis\": \"source_text\","` | — |
| [SRC-851E7A87D6-L000107](../../tests/test_postgres_store.py#L107) | 107 | `"                    \"signal_type\": \"direct_purchase_request\","` | — |
| [SRC-851E7A87D6-L000108](../../tests/test_postgres_store.py#L108) | 108 | `"                    \"product_fit\": \"unassessed\","` | — |
| [SRC-851E7A87D6-L000109](../../tests/test_postgres_store.py#L109) | 109 | `"                },"` | — |
| [SRC-851E7A87D6-L000110](../../tests/test_postgres_store.py#L110) | 110 | `"            }],"` | — |
| [SRC-851E7A87D6-L000111](../../tests/test_postgres_store.py#L111) | 111 | `"            \"search_report\": {\"search_outcome\": \"results_found\"},"` | — |
| [SRC-851E7A87D6-L000112](../../tests/test_postgres_store.py#L112) | 112 | `"        },"` | — |
| [SRC-851E7A87D6-L000113](../../tests/test_postgres_store.py#L113) | 113 | `"        tenant_id=tenant_id,"` | — |
| [SRC-851E7A87D6-L000114](../../tests/test_postgres_store.py#L114) | 114 | `"    )"` | — |
| [SRC-851E7A87D6-L000115](../../tests/test_postgres_store.py#L115) | 115 | `"    assert run[\"tenant_id\"] == tenant_id"` | — |
| [SRC-851E7A87D6-L000116](../../tests/test_postgres_store.py#L116) | 116 | `"    assert run[\"sources\"][0][\"lead_qualification\"] == \"public_demand_signal\""` | — |
| [SRC-851E7A87D6-L000117](../../tests/test_postgres_store.py#L117) | 117 | `"    assert postgres_store.get_discovery_run("` | — |
| [SRC-851E7A87D6-L000118](../../tests/test_postgres_store.py#L118) | 118 | `"        run[\"id\"], tenant_id=tenant_id"` | — |
| [SRC-851E7A87D6-L000119](../../tests/test_postgres_store.py#L119) | 119 | `"    )[\"id\"] == run[\"id\"]"` | — |
| [SRC-851E7A87D6-L000120](../../tests/test_postgres_store.py#L120) | 120 | `"    assert postgres_store.list_discovery_runs(tenant_id=tenant_id)[0][\"id\"] == run[\"id\"]"` | — |
| [SRC-851E7A87D6-L000121](../../tests/test_postgres_store.py#L121) | 121 | `""` | — |
| [SRC-851E7A87D6-L000122](../../tests/test_postgres_store.py#L122) | 122 | `"    saved_signal, created = postgres_store.save_discovery_signal("` | — |
| [SRC-851E7A87D6-L000123](../../tests/test_postgres_store.py#L123) | 123 | `"        run[\"id\"], 0, tenant_id=tenant_id"` | — |
| [SRC-851E7A87D6-L000124](../../tests/test_postgres_store.py#L124) | 124 | `"    )"` | — |
| [SRC-851E7A87D6-L000125](../../tests/test_postgres_store.py#L125) | 125 | `"    assert created is True"` | — |
| [SRC-851E7A87D6-L000126](../../tests/test_postgres_store.py#L126) | 126 | `"    assert saved_signal[\"tenant_id\"] == tenant_id"` | — |
| [SRC-851E7A87D6-L000127](../../tests/test_postgres_store.py#L127) | 127 | `"    assert postgres_store.revoke_api_token("` | — |
| [SRC-851E7A87D6-L000128](../../tests/test_postgres_store.py#L128) | 128 | `"        token, tenant_id=tenant_id, user_id=user_id"` | — |
| [SRC-851E7A87D6-L000129](../../tests/test_postgres_store.py#L129) | 129 | `"    ) is True"` | — |
| [SRC-851E7A87D6-L000130](../../tests/test_postgres_store.py#L130) | 130 | `"    assert postgres_store.resolve_api_token(token) is None"` | — |
| [SRC-851E7A87D6-L000131](../../tests/test_postgres_store.py#L131) | 131 | `""` | — |
| [SRC-851E7A87D6-L000132](../../tests/test_postgres_store.py#L132) | 132 | `""` | — |
| [SRC-851E7A87D6-L000133](../../tests/test_postgres_store.py#L133) | 133 | `"def test_postgres_placeholder_translation_skips_quoted_question_marks():"` | — |
| [SRC-851E7A87D6-L000134](../../tests/test_postgres_store.py#L134) | 134 | `"    sql = \"SELECT ?, '?' AS literal, \\\"?\\\" AS identifier, ? AS last_value\""` | — |
| [SRC-851E7A87D6-L000135](../../tests/test_postgres_store.py#L135) | 135 | `"    assert _qmark_to_psycopg(sql) == ("` | — |
| [SRC-851E7A87D6-L000136](../../tests/test_postgres_store.py#L136) | 136 | `"        \"SELECT %s, '?' AS literal, \\\"?\\\" AS identifier, %s AS last_value\""` | — |
| [SRC-851E7A87D6-L000137](../../tests/test_postgres_store.py#L137) | 137 | `"    )"` | — |
| [SRC-851E7A87D6-L000138](../../tests/test_postgres_store.py#L138) | 138 | `""` | — |
| [SRC-851E7A87D6-L000139](../../tests/test_postgres_store.py#L139) | 139 | `""` | — |
| [SRC-851E7A87D6-L000140](../../tests/test_postgres_store.py#L140) | 140 | `"def test_postgres_connection_adapter_converts_insert_or_ignore():"` | — |
| [SRC-851E7A87D6-L000141](../../tests/test_postgres_store.py#L141) | 141 | `"    class FakeConnection:"` | — |
| [SRC-851E7A87D6-L000142](../../tests/test_postgres_store.py#L142) | 142 | `"        statement = None"` | — |
| [SRC-851E7A87D6-L000143](../../tests/test_postgres_store.py#L143) | 143 | `"        params = None"` | — |
| [SRC-851E7A87D6-L000144](../../tests/test_postgres_store.py#L144) | 144 | `""` | — |
| [SRC-851E7A87D6-L000145](../../tests/test_postgres_store.py#L145) | 145 | `"        def execute(self, statement, params):"` | — |
| [SRC-851E7A87D6-L000146](../../tests/test_postgres_store.py#L146) | 146 | `"            self.statement = statement"` | — |
| [SRC-851E7A87D6-L000147](../../tests/test_postgres_store.py#L147) | 147 | `"            self.params = params"` | — |
| [SRC-851E7A87D6-L000148](../../tests/test_postgres_store.py#L148) | 148 | `"            return \"cursor\""` | — |
| [SRC-851E7A87D6-L000149](../../tests/test_postgres_store.py#L149) | 149 | `""` | — |
| [SRC-851E7A87D6-L000150](../../tests/test_postgres_store.py#L150) | 150 | `"    connection = FakeConnection()"` | — |
| [SRC-851E7A87D6-L000151](../../tests/test_postgres_store.py#L151) | 151 | `"    adapter = _PostgresConnection(connection)"` | — |
| [SRC-851E7A87D6-L000152](../../tests/test_postgres_store.py#L152) | 152 | `""` | — |
| [SRC-851E7A87D6-L000153](../../tests/test_postgres_store.py#L153) | 153 | `"    result = adapter.execute("` | — |
| [SRC-851E7A87D6-L000154](../../tests/test_postgres_store.py#L154) | 154 | `"        \"INSERT OR IGNORE INTO leads (id, note) VALUES (?, '?')\","` | — |
| [SRC-851E7A87D6-L000155](../../tests/test_postgres_store.py#L155) | 155 | `"        (\"lead-1\",),"` | — |
| [SRC-851E7A87D6-L000156](../../tests/test_postgres_store.py#L156) | 156 | `"    )"` | — |
| [SRC-851E7A87D6-L000157](../../tests/test_postgres_store.py#L157) | 157 | `""` | — |
| [SRC-851E7A87D6-L000158](../../tests/test_postgres_store.py#L158) | 158 | `"    assert result == \"cursor\""` | — |
| [SRC-851E7A87D6-L000159](../../tests/test_postgres_store.py#L159) | 159 | `"    assert connection.statement == ("` | — |
| [SRC-851E7A87D6-L000160](../../tests/test_postgres_store.py#L160) | 160 | `"        \"INSERT INTO leads (id, note) VALUES (%s, '?') ON CONFLICT DO NOTHING\""` | — |
| [SRC-851E7A87D6-L000161](../../tests/test_postgres_store.py#L161) | 161 | `"    )"` | — |
| [SRC-851E7A87D6-L000162](../../tests/test_postgres_store.py#L162) | 162 | `"    assert connection.params == (\"lead-1\",)"` | — |
| [SRC-851E7A87D6-L000163](../../tests/test_postgres_store.py#L163) | 163 | `""` | — |
| [SRC-851E7A87D6-L000164](../../tests/test_postgres_store.py#L164) | 164 | `""` | — |
| [SRC-851E7A87D6-L000165](../../tests/test_postgres_store.py#L165) | 165 | `"def test_postgres_database_url_rejects_unsupported_scheme():"` | — |
| [SRC-851E7A87D6-L000166](../../tests/test_postgres_store.py#L166) | 166 | `"    with pytest.raises(ValueError, match=\"PostgreSQL URL scheme\"):"` | — |
| [SRC-851E7A87D6-L000167](../../tests/test_postgres_store.py#L167) | 167 | `"        LeadStore(database_url=\"mysql://user:pass@example.com/db\")"` | — |
| [SRC-851E7A87D6-L000168](../../tests/test_postgres_store.py#L168) | 168 | `""` | — |
| [SRC-851E7A87D6-L000169](../../tests/test_postgres_store.py#L169) | 169 | `""` | — |
| [SRC-851E7A87D6-L000170](../../tests/test_postgres_store.py#L170) | 170 | `"def test_postgres_database_url_cannot_be_combined_with_sqlite_path(tmp_path):"` | — |
| [SRC-851E7A87D6-L000171](../../tests/test_postgres_store.py#L171) | 171 | `"    with pytest.raises(ValueError, match=\"either database_url or a SQLite path\"):"` | — |
| [SRC-851E7A87D6-L000172](../../tests/test_postgres_store.py#L172) | 172 | `"        LeadStore(tmp_path / \"local.sqlite3\", database_url=\"postgresql://user:pass@example.com/db\")"` | — |
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
| [SRC-C353AAAC10-L000077](../../tests/test_request_budget.py#L77) | 77 | `"        \"agents.web_agent._open_model_request\","` | — |
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
| [SRC-C353AAAC10-L000121](../../tests/test_request_budget.py#L121) | 121 | `"        assert snapshot[\"counts\"][resource] <= snapshot[\"limits\"][resource]"` | — |
| [SRC-C353AAAC10-L000122](../../tests/test_request_budget.py#L122) | 122 | `""` | — |
| [SRC-C353AAAC10-L000123](../../tests/test_request_budget.py#L123) | 123 | `"    with pytest.raises(RequestBudgetExceeded, match=resource):"` | — |
| [SRC-C353AAAC10-L000124](../../tests/test_request_budget.py#L124) | 124 | `"        budget.reserve(resource)"` | — |
| [SRC-C353AAAC10-L000125](../../tests/test_request_budget.py#L125) | 125 | `""` | — |
| [SRC-C353AAAC10-L000126](../../tests/test_request_budget.py#L126) | 126 | `"    snapshot = budget.snapshot()"` | — |
| [SRC-C353AAAC10-L000127](../../tests/test_request_budget.py#L127) | 127 | `"    assert snapshot[\"counts\"][resource] == limit"` | — |
| [SRC-C353AAAC10-L000128](../../tests/test_request_budget.py#L128) | 128 | `"    assert resource in snapshot[\"exhausted_reasons\"]"` | — |
| [SRC-C353AAAC10-L000129](../../tests/test_request_budget.py#L129) | 129 | `""` | — |
| [SRC-C353AAAC10-L000130](../../tests/test_request_budget.py#L130) | 130 | `""` | — |
| [SRC-C353AAAC10-L000131](../../tests/test_request_budget.py#L131) | 131 | `"@pytest.mark.parametrize("` | — |
| [SRC-C353AAAC10-L000132](../../tests/test_request_budget.py#L132) | 132 | `"    \"resource\","` | — |
| [SRC-C353AAAC10-L000133](../../tests/test_request_budget.py#L133) | 133 | `"    [\"search_queries\", \"search_calls\", \"model_calls\", \"page_fetches\", \"tool_calls\"],"` | — |
| [SRC-C353AAAC10-L000134](../../tests/test_request_budget.py#L134) | 134 | `")"` | — |
| [SRC-C353AAAC10-L000135](../../tests/test_request_budget.py#L135) | 135 | `"def test_disabled_resource_never_starts_work(resource):"` | — |
| [SRC-C353AAAC10-L000136](../../tests/test_request_budget.py#L136) | 136 | `"    budget = RequestBudget(timeout_seconds=10, limits={resource: 0})"` | — |
| [SRC-C353AAAC10-L000137](../../tests/test_request_budget.py#L137) | 137 | `""` | — |
| [SRC-C353AAAC10-L000138](../../tests/test_request_budget.py#L138) | 138 | `"    assert budget.remaining_units(resource) == 0"` | — |
| [SRC-C353AAAC10-L000139](../../tests/test_request_budget.py#L139) | 139 | `"    with pytest.raises(RequestBudgetExceeded, match=resource):"` | — |
| [SRC-C353AAAC10-L000140](../../tests/test_request_budget.py#L140) | 140 | `"        budget.reserve(resource)"` | — |
| [SRC-C353AAAC10-L000141](../../tests/test_request_budget.py#L141) | 141 | `""` | — |
| [SRC-C353AAAC10-L000142](../../tests/test_request_budget.py#L142) | 142 | `"    snapshot = budget.snapshot()"` | — |
| [SRC-C353AAAC10-L000143](../../tests/test_request_budget.py#L143) | 143 | `"    assert snapshot[\"counts\"][resource] == 0"` | — |
| [SRC-C353AAAC10-L000144](../../tests/test_request_budget.py#L144) | 144 | `"    assert snapshot[\"limits\"][resource] == 0"` | — |
| [SRC-C353AAAC10-L000145](../../tests/test_request_budget.py#L145) | 145 | `"    assert resource in snapshot[\"disabled_resources\"]"` | — |
| [SRC-C353AAAC10-L000146](../../tests/test_request_budget.py#L146) | 146 | `"    assert resource in snapshot[\"exhausted_reasons\"]"` | — |
| [SRC-C353AAAC10-L000147](../../tests/test_request_budget.py#L147) | 147 | `""` | — |
| [SRC-C353AAAC10-L000148](../../tests/test_request_budget.py#L148) | 148 | `""` | — |
| [SRC-C353AAAC10-L000149](../../tests/test_request_budget.py#L149) | 149 | `"def test_hosted_smoke_budget_profile_applies_strict_per_request_caps(monkeypatch):"` | — |
| [SRC-C353AAAC10-L000150](../../tests/test_request_budget.py#L150) | 150 | `"    from agents.request_budget import HOSTED_SMOKE_BUDGET_LIMITS"` | — |
| [SRC-C353AAAC10-L000151](../../tests/test_request_budget.py#L151) | 151 | `""` | — |
| [SRC-C353AAAC10-L000152](../../tests/test_request_budget.py#L152) | 152 | `"    monkeypatch.setenv(\"OMARAI_REQUEST_BUDGET_SECONDS\", \"110\")"` | — |
| [SRC-C353AAAC10-L000153](../../tests/test_request_budget.py#L153) | 153 | `"    monkeypatch.setenv(\"OMARAI_REQUEST_MAX_SEARCH_CALLS\", \"2\")"` | — |
| [SRC-C353AAAC10-L000154](../../tests/test_request_budget.py#L154) | 154 | `"    monkeypatch.setenv(\"OMARAI_REQUEST_MAX_MODEL_CALLS\", \"10\")"` | — |
| [SRC-C353AAAC10-L000155](../../tests/test_request_budget.py#L155) | 155 | `""` | — |
| [SRC-C353AAAC10-L000156](../../tests/test_request_budget.py#L156) | 156 | `"    snapshot = RequestBudget.from_environment(profile=\"hosted_smoke\").snapshot()"` | — |
| [SRC-C353AAAC10-L000157](../../tests/test_request_budget.py#L157) | 157 | `""` | — |
| [SRC-C353AAAC10-L000158](../../tests/test_request_budget.py#L158) | 158 | `"    assert snapshot[\"profile\"] == \"hosted_smoke\""` | — |
| [SRC-C353AAAC10-L000159](../../tests/test_request_budget.py#L159) | 159 | `"    assert snapshot[\"timeout_seconds\"] == 75"` | — |
| [SRC-C353AAAC10-L000160](../../tests/test_request_budget.py#L160) | 160 | `"    assert snapshot[\"limits\"] == {"` | — |
| [SRC-C353AAAC10-L000161](../../tests/test_request_budget.py#L161) | 161 | `"        **HOSTED_SMOKE_BUDGET_LIMITS,"` | — |
| [SRC-C353AAAC10-L000162](../../tests/test_request_budget.py#L162) | 162 | `"        \"search_calls\": 2,"` | — |
| [SRC-C353AAAC10-L000163](../../tests/test_request_budget.py#L163) | 163 | `"        \"model_calls\": min(10, HOSTED_SMOKE_BUDGET_LIMITS[\"model_calls\"]),"` | — |
| [SRC-C353AAAC10-L000164](../../tests/test_request_budget.py#L164) | 164 | `"    }"` | — |
| [SRC-C353AAAC10-L000165](../../tests/test_request_budget.py#L165) | 165 | `"    assert snapshot[\"limits\"][\"search_queries\"] <= 3"` | — |
| [SRC-C353AAAC10-L000166](../../tests/test_request_budget.py#L166) | 166 | `"    assert snapshot[\"limits\"][\"search_calls\"] <= 12"` | — |
| [SRC-C353AAAC10-L000167](../../tests/test_request_budget.py#L167) | 167 | `"    assert snapshot[\"limits\"][\"model_calls\"] <= 6"` | — |
| [SRC-C353AAAC10-L000168](../../tests/test_request_budget.py#L168) | 168 | `"    assert snapshot[\"limits\"][\"page_fetches\"] <= 4"` | — |
| [SRC-C353AAAC10-L000169](../../tests/test_request_budget.py#L169) | 169 | `"    assert snapshot[\"limits\"][\"tool_calls\"] == 0"` | — |
| [SRC-C353AAAC10-L000170](../../tests/test_request_budget.py#L170) | 170 | `""` | — |
| [SRC-C353AAAC10-L000171](../../tests/test_request_budget.py#L171) | 171 | `""` | — |
| [SRC-C353AAAC10-L000172](../../tests/test_request_budget.py#L172) | 172 | `"def test_request_budget_rejects_unknown_profile():"` | — |
| [SRC-C353AAAC10-L000173](../../tests/test_request_budget.py#L173) | 173 | `"    with pytest.raises(ValueError, match=\"unknown request-budget profile\"):"` | — |
| [SRC-C353AAAC10-L000174](../../tests/test_request_budget.py#L174) | 174 | `"        RequestBudget.from_environment(profile=\"untrusted\")"` | — |
| [SRC-C353AAAC10-L000175](../../tests/test_request_budget.py#L175) | 175 | `""` | — |
| [SRC-C353AAAC10-L000176](../../tests/test_request_budget.py#L176) | 176 | `""` | — |
| [SRC-C353AAAC10-L000177](../../tests/test_request_budget.py#L177) | 177 | `"def test_web_agent_answer_uses_the_selected_budget_profile(monkeypatch):"` | — |
| [SRC-C353AAAC10-L000178](../../tests/test_request_budget.py#L178) | 178 | `"    from agents.web_agent import WebAgent"` | — |
| [SRC-C353AAAC10-L000179](../../tests/test_request_budget.py#L179) | 179 | `""` | — |
| [SRC-C353AAAC10-L000180](../../tests/test_request_budget.py#L180) | 180 | `"    agent = WebAgent()"` | — |
| [SRC-C353AAAC10-L000181](../../tests/test_request_budget.py#L181) | 181 | `"    monkeypatch.setattr("` | — |
| [SRC-C353AAAC10-L000182](../../tests/test_request_budget.py#L182) | 182 | `"        agent,"` | — |
| [SRC-C353AAAC10-L000183](../../tests/test_request_budget.py#L183) | 183 | `"        \"_answer_with_budget\","` | — |
| [SRC-C353AAAC10-L000184](../../tests/test_request_budget.py#L184) | 184 | `"        lambda question, history, mode: {\"answer\": \"test\", \"kind\": \"test\"},"` | — |
| [SRC-C353AAAC10-L000185](../../tests/test_request_budget.py#L185) | 185 | `"    )"` | — |
| [SRC-C353AAAC10-L000186](../../tests/test_request_budget.py#L186) | 186 | `""` | — |
| [SRC-C353AAAC10-L000187](../../tests/test_request_budget.py#L187) | 187 | `"    result = agent.answer(\"budget profile test\", budget_profile=\"hosted_smoke\")"` | — |
| [SRC-C353AAAC10-L000188](../../tests/test_request_budget.py#L188) | 188 | `""` | — |
| [SRC-C353AAAC10-L000189](../../tests/test_request_budget.py#L189) | 189 | `"    assert result[\"request_budget\"][\"profile\"] == \"hosted_smoke\""` | — |
| [SRC-C353AAAC10-L000190](../../tests/test_request_budget.py#L190) | 190 | `"    assert result[\"request_budget\"][\"limits\"][\"search_calls\"] <= 12"` | — |
| [SRC-C353AAAC10-L000191](../../tests/test_request_budget.py#L191) | 191 | `"    assert result[\"request_budget\"][\"limits\"][\"model_calls\"] <= 6"` | — |
## اختبارات

### FILE-50E7F53B84 — [tests/test_requirement_evidence.py](../../tests/test_requirement_evidence.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-50E7F53B84-L000001](../../tests/test_requirement_evidence.py#L1) | 1 | `"\"\"\"Focused contract tests for the dedicated requirement-evidence module.\"\"\""` | — |
| [SRC-50E7F53B84-L000002](../../tests/test_requirement_evidence.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-50E7F53B84-L000003](../../tests/test_requirement_evidence.py#L3) | 3 | `""` | — |
| [SRC-50E7F53B84-L000004](../../tests/test_requirement_evidence.py#L4) | 4 | `"from agents.answer_validation import build_requirement_evidence_ledger as legacy_builder"` | — |
| [SRC-50E7F53B84-L000005](../../tests/test_requirement_evidence.py#L5) | 5 | `"from agents.requirement_evidence import build_requirement_evidence_ledger"` | — |
| [SRC-50E7F53B84-L000006](../../tests/test_requirement_evidence.py#L6) | 6 | `"from agents.text_normalization import normalize_text, tokenize_text"` | — |
| [SRC-50E7F53B84-L000007](../../tests/test_requirement_evidence.py#L7) | 7 | `""` | — |
| [SRC-50E7F53B84-L000008](../../tests/test_requirement_evidence.py#L8) | 8 | `""` | — |
| [SRC-50E7F53B84-L000009](../../tests/test_requirement_evidence.py#L9) | 9 | `"def test_legacy_import_path_reexports_the_dedicated_builder() -> None:"` | — |
| [SRC-50E7F53B84-L000010](../../tests/test_requirement_evidence.py#L10) | 10 | `"    assert legacy_builder is build_requirement_evidence_ledger"` | — |
| [SRC-50E7F53B84-L000011](../../tests/test_requirement_evidence.py#L11) | 11 | `""` | — |
| [SRC-50E7F53B84-L000012](../../tests/test_requirement_evidence.py#L12) | 12 | `""` | — |
| [SRC-50E7F53B84-L000013](../../tests/test_requirement_evidence.py#L13) | 13 | `"def test_shared_normalizer_handles_arabic_diacritics_and_digits() -> None:"` | — |
| [SRC-50E7F53B84-L000014](../../tests/test_requirement_evidence.py#L14) | 14 | `"    assert normalize_text(\"أَهْلًا ١٢٣\") == \"اهلا 123\""` | — |
| [SRC-50E7F53B84-L000015](../../tests/test_requirement_evidence.py#L15) | 15 | `"    assert tokenize_text(\"The phone السعر ١٢\", drop_stopwords=True) == [\"phone\", \"السعر\", \"12\"]"` | — |
| [SRC-50E7F53B84-L000016](../../tests/test_requirement_evidence.py#L16) | 16 | `""` | — |
| [SRC-50E7F53B84-L000017](../../tests/test_requirement_evidence.py#L17) | 17 | `""` | — |
| [SRC-50E7F53B84-L000018](../../tests/test_requirement_evidence.py#L18) | 18 | `"def test_requirement_ledger_links_query_provenance_and_lexical_candidates() -> None:"` | — |
| [SRC-50E7F53B84-L000019](../../tests/test_requirement_evidence.py#L19) | 19 | `"    targets = [\"السعر\", \"البطارية\"]"` | — |
| [SRC-50E7F53B84-L000020](../../tests/test_requirement_evidence.py#L20) | 20 | `"    queries = ["` | — |
| [SRC-50E7F53B84-L000021](../../tests/test_requirement_evidence.py#L21) | 21 | `"        {\"target\": \"السعر\", \"query\": \"سعر الهاتف\"},"` | — |
| [SRC-50E7F53B84-L000022](../../tests/test_requirement_evidence.py#L22) | 22 | `"        {\"target\": \"البطارية\", \"query\": \"بطارية الهاتف\"},"` | — |
| [SRC-50E7F53B84-L000023](../../tests/test_requirement_evidence.py#L23) | 23 | `"    ]"` | — |
| [SRC-50E7F53B84-L000024](../../tests/test_requirement_evidence.py#L24) | 24 | `"    sources = ["` | — |
| [SRC-50E7F53B84-L000025](../../tests/test_requirement_evidence.py#L25) | 25 | `"        {"` | — |
| [SRC-50E7F53B84-L000026](../../tests/test_requirement_evidence.py#L26) | 26 | `"            \"title\": \"Phone price guide\","` | — |
| [SRC-50E7F53B84-L000027](../../tests/test_requirement_evidence.py#L27) | 27 | `"            \"snippet\": \"The price and cost are listed for the phone.\","` | — |
| [SRC-50E7F53B84-L000028](../../tests/test_requirement_evidence.py#L28) | 28 | `"            \"page_fetched\": False,"` | — |
| [SRC-50E7F53B84-L000029](../../tests/test_requirement_evidence.py#L29) | 29 | `"            \"queries\": [\"سعر الهاتف\"],"` | — |
| [SRC-50E7F53B84-L000030](../../tests/test_requirement_evidence.py#L30) | 30 | `"        },"` | — |
| [SRC-50E7F53B84-L000031](../../tests/test_requirement_evidence.py#L31) | 31 | `"    ]"` | — |
| [SRC-50E7F53B84-L000032](../../tests/test_requirement_evidence.py#L32) | 32 | `""` | — |
| [SRC-50E7F53B84-L000033](../../tests/test_requirement_evidence.py#L33) | 33 | `"    ledger = build_requirement_evidence_ledger(targets, sources, queries)"` | — |
| [SRC-50E7F53B84-L000034](../../tests/test_requirement_evidence.py#L34) | 34 | `"    by_target = {item[\"target\"]: item for item in ledger}"` | — |
| [SRC-50E7F53B84-L000035](../../tests/test_requirement_evidence.py#L35) | 35 | `""` | — |
| [SRC-50E7F53B84-L000036](../../tests/test_requirement_evidence.py#L36) | 36 | `"    price = by_target[\"السعر\"]"` | — |
| [SRC-50E7F53B84-L000037](../../tests/test_requirement_evidence.py#L37) | 37 | `"    assert price[\"status\"] == \"candidate_evidence_found_not_verified\""` | — |
| [SRC-50E7F53B84-L000038](../../tests/test_requirement_evidence.py#L38) | 38 | `"    assert price[\"query_result_source_indexes\"] == [1]"` | — |
| [SRC-50E7F53B84-L000039](../../tests/test_requirement_evidence.py#L39) | 39 | `"    assert price[\"candidate_source_indexes\"] == [1]"` | — |
| [SRC-50E7F53B84-L000040](../../tests/test_requirement_evidence.py#L40) | 40 | `"    assert price[\"candidate_sources\"][0][\"evidence_basis\"] == \"search_snippet\""` | — |
| [SRC-50E7F53B84-L000041](../../tests/test_requirement_evidence.py#L41) | 41 | `"    assert price[\"semantic_verification\"] is False"` | — |
| [SRC-50E7F53B84-L000042](../../tests/test_requirement_evidence.py#L42) | 42 | `"    assert price[\"source_entailment_verified\"] is False"` | — |
| [SRC-50E7F53B84-L000043](../../tests/test_requirement_evidence.py#L43) | 43 | `""` | — |
| [SRC-50E7F53B84-L000044](../../tests/test_requirement_evidence.py#L44) | 44 | `"    battery = by_target[\"البطارية\"]"` | — |
| [SRC-50E7F53B84-L000045](../../tests/test_requirement_evidence.py#L45) | 45 | `"    assert battery[\"status\"] == \"no_candidate_evidence_found\""` | — |
| [SRC-50E7F53B84-L000046](../../tests/test_requirement_evidence.py#L46) | 46 | `"    assert battery[\"candidate_source_indexes\"] == []"` | — |
| [SRC-50E7F53B84-L000047](../../tests/test_requirement_evidence.py#L47) | 47 | `"    assert battery[\"semantic_verification\"] is False"` | — |
| [SRC-50E7F53B84-L000048](../../tests/test_requirement_evidence.py#L48) | 48 | `""` | — |
| [SRC-50E7F53B84-L000049](../../tests/test_requirement_evidence.py#L49) | 49 | `""` | — |
| [SRC-50E7F53B84-L000050](../../tests/test_requirement_evidence.py#L50) | 50 | `"def test_title_only_match_remains_a_candidate_not_verified_evidence() -> None:"` | — |
| [SRC-50E7F53B84-L000051](../../tests/test_requirement_evidence.py#L51) | 51 | `"    ledger = build_requirement_evidence_ledger("` | — |
| [SRC-50E7F53B84-L000052](../../tests/test_requirement_evidence.py#L52) | 52 | `"        [\"battery\"],"` | — |
| [SRC-50E7F53B84-L000053](../../tests/test_requirement_evidence.py#L53) | 53 | `"        [{\"title\": \"Battery overview\", \"page_fetched\": False}],"` | — |
| [SRC-50E7F53B84-L000054](../../tests/test_requirement_evidence.py#L54) | 54 | `"    )"` | — |
| [SRC-50E7F53B84-L000055](../../tests/test_requirement_evidence.py#L55) | 55 | `""` | — |
| [SRC-50E7F53B84-L000056](../../tests/test_requirement_evidence.py#L56) | 56 | `"    assert ledger[0][\"status\"] == \"candidate_evidence_found_not_verified\""` | — |
| [SRC-50E7F53B84-L000057](../../tests/test_requirement_evidence.py#L57) | 57 | `"    assert ledger[0][\"candidate_sources\"][0][\"evidence_basis\"] == \"title_only\""` | — |
| [SRC-50E7F53B84-L000058](../../tests/test_requirement_evidence.py#L58) | 58 | `"    assert ledger[0][\"semantic_verification\"] is False"` | — |
| [SRC-50E7F53B84-L000059](../../tests/test_requirement_evidence.py#L59) | 59 | `"    assert ledger[0][\"source_entailment_verified\"] is False"` | — |
## اختبارات

### FILE-6BF96689A8 — [tests/test_research.py](../../tests/test_research.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6BF96689A8-L000001](../../tests/test_research.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-6BF96689A8-L000002](../../tests/test_research.py#L2) | 2 | `""` | — |
| [SRC-6BF96689A8-L000003](../../tests/test_research.py#L3) | 3 | `"from agents.research import ("` | — |
| [SRC-6BF96689A8-L000004](../../tests/test_research.py#L4) | 4 | `"    classify_source,"` | — |
| [SRC-6BF96689A8-L000005](../../tests/test_research.py#L5) | 5 | `"    compact_search_query,"` | — |
| [SRC-6BF96689A8-L000006](../../tests/test_research.py#L6) | 6 | `"    evidence_signal_report,"` | — |
| [SRC-6BF96689A8-L000007](../../tests/test_research.py#L7) | 7 | `"    fallback_plan,"` | — |
| [SRC-6BF96689A8-L000008](../../tests/test_research.py#L8) | 8 | `"    fuse_ranked_results,"` | — |
| [SRC-6BF96689A8-L000009](../../tests/test_research.py#L9) | 9 | `"    registrable_domain,"` | — |
| [SRC-6BF96689A8-L000010](../../tests/test_research.py#L10) | 10 | `"    validate_plan,"` | — |
| [SRC-6BF96689A8-L000011](../../tests/test_research.py#L11) | 11 | `")"` | — |
| [SRC-6BF96689A8-L000012](../../tests/test_research.py#L12) | 12 | `""` | — |
| [SRC-6BF96689A8-L000013](../../tests/test_research.py#L13) | 13 | `""` | — |
| [SRC-6BF96689A8-L000014](../../tests/test_research.py#L14) | 14 | `"def test_social_question_gets_platform_targeted_queries():"` | — |
| [SRC-6BF96689A8-L000015](../../tests/test_research.py#L15) | 15 | `"    plan = fallback_plan(\"ابحث في Reddit عن تجارب العملاء مع السيارات الكهربائية\")"` | — |
| [SRC-6BF96689A8-L000016](../../tests/test_research.py#L16) | 16 | `"    assert plan[\"social_focus\"] is True"` | — |
| [SRC-6BF96689A8-L000017](../../tests/test_research.py#L17) | 17 | `"    assert \"reddit\" in plan[\"platforms\"]"` | — |
| [SRC-6BF96689A8-L000018](../../tests/test_research.py#L18) | 18 | `"    assert any(\"site:reddit.com\" in query for query in plan[\"queries\"])"` | — |
| [SRC-6BF96689A8-L000019](../../tests/test_research.py#L19) | 19 | `"    assert len(plan[\"queries\"]) <= 8"` | — |
| [SRC-6BF96689A8-L000020](../../tests/test_research.py#L20) | 20 | `""` | — |
| [SRC-6BF96689A8-L000021](../../tests/test_research.py#L21) | 21 | `""` | — |
| [SRC-6BF96689A8-L000022](../../tests/test_research.py#L22) | 22 | `"def test_follow_up_query_keeps_prior_topic():"` | — |
| [SRC-6BF96689A8-L000023](../../tests/test_research.py#L23) | 23 | `"    history = [{\"role\": \"user\", \"content\": \"قارن سوق السيارات الكهربائية في مصر\"}]"` | — |
| [SRC-6BF96689A8-L000024](../../tests/test_research.py#L24) | 24 | `"    plan = fallback_plan(\"وطب الأسعار الحالية؟\", history)"` | — |
| [SRC-6BF96689A8-L000025](../../tests/test_research.py#L25) | 25 | `"    assert \"السيارات الكهربائية\" in plan[\"queries\"][0]"` | — |
| [SRC-6BF96689A8-L000026](../../tests/test_research.py#L26) | 26 | `"    assert plan[\"freshness\"] == \"current\""` | — |
| [SRC-6BF96689A8-L000027](../../tests/test_research.py#L27) | 27 | `""` | — |
| [SRC-6BF96689A8-L000028](../../tests/test_research.py#L28) | 28 | `""` | — |
| [SRC-6BF96689A8-L000029](../../tests/test_research.py#L29) | 29 | `"def test_plan_validation_caps_queries_and_rejects_non_string_values():"` | — |
| [SRC-6BF96689A8-L000030](../../tests/test_research.py#L30) | 30 | `"    candidate = {"` | — |
| [SRC-6BF96689A8-L000031](../../tests/test_research.py#L31) | 31 | `"        \"queries\": [\"بحث أ\", \"بحث ب\", None, \"بحث ج\", \"بحث د\", \"بحث هـ\", \"بحث سادس\", \"بحث سابع\", \"بحث ثامن\", \"بحث تاسع\"],"` | — |
| [SRC-6BF96689A8-L000032](../../tests/test_research.py#L32) | 32 | `"        \"social_focus\": True,"` | — |
| [SRC-6BF96689A8-L000033](../../tests/test_research.py#L33) | 33 | `"        \"freshness\": \"current\","` | — |
| [SRC-6BF96689A8-L000034](../../tests/test_research.py#L34) | 34 | `"        \"depth\": \"deep\","` | — |
| [SRC-6BF96689A8-L000035](../../tests/test_research.py#L35) | 35 | `"        \"platforms\": [\"reddit\", \"unknown\"],"` | — |
| [SRC-6BF96689A8-L000036](../../tests/test_research.py#L36) | 36 | `"    }"` | — |
| [SRC-6BF96689A8-L000037](../../tests/test_research.py#L37) | 37 | `"    plan = validate_plan(candidate, \"بحث عن منشورات\")"` | — |
| [SRC-6BF96689A8-L000038](../../tests/test_research.py#L38) | 38 | `"    assert len(plan[\"queries\"]) <= 8"` | — |
| [SRC-6BF96689A8-L000039](../../tests/test_research.py#L39) | 39 | `"    assert \"unknown\" not in plan[\"platforms\"]"` | — |
| [SRC-6BF96689A8-L000040](../../tests/test_research.py#L40) | 40 | `"    assert plan[\"social_focus\"] is True"` | — |
| [SRC-6BF96689A8-L000041](../../tests/test_research.py#L41) | 41 | `"    assert plan[\"freshness\"] == \"current\""` | — |
| [SRC-6BF96689A8-L000042](../../tests/test_research.py#L42) | 42 | `""` | — |
| [SRC-6BF96689A8-L000043](../../tests/test_research.py#L43) | 43 | `""` | — |
| [SRC-6BF96689A8-L000044](../../tests/test_research.py#L44) | 44 | `"def test_rank_fusion_promotes_cross_provider_consensus_and_deduplicates():"` | — |
| [SRC-6BF96689A8-L000045](../../tests/test_research.py#L45) | 45 | `"    batches = ["` | — |
| [SRC-6BF96689A8-L000046](../../tests/test_research.py#L46) | 46 | `"        {"` | — |
| [SRC-6BF96689A8-L000047](../../tests/test_research.py#L47) | 47 | `"            \"query\": \"cars Egypt\","` | — |
| [SRC-6BF96689A8-L000048](../../tests/test_research.py#L48) | 48 | `"            \"provider\": \"ddg\","` | — |
| [SRC-6BF96689A8-L000049](../../tests/test_research.py#L49) | 49 | `"            \"results\": ["` | — |
| [SRC-6BF96689A8-L000050](../../tests/test_research.py#L50) | 50 | `"                {\"title\": \"A\", \"url\": \"https://www.example.com/a?utm_source=x\", \"snippet\": \"A\"},"` | — |
| [SRC-6BF96689A8-L000051](../../tests/test_research.py#L51) | 51 | `"                {\"title\": \"B\", \"url\": \"https://example.com/b\", \"snippet\": \"B\"},"` | — |
| [SRC-6BF96689A8-L000052](../../tests/test_research.py#L52) | 52 | `"            ],"` | — |
| [SRC-6BF96689A8-L000053](../../tests/test_research.py#L53) | 53 | `"        },"` | — |
| [SRC-6BF96689A8-L000054](../../tests/test_research.py#L54) | 54 | `"        {"` | — |
| [SRC-6BF96689A8-L000055](../../tests/test_research.py#L55) | 55 | `"            \"query\": \"electric vehicles Egypt\","` | — |
| [SRC-6BF96689A8-L000056](../../tests/test_research.py#L56) | 56 | `"            \"provider\": \"bing\","` | — |
