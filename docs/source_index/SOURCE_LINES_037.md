# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **037**
- سجلات الأسطر: **800**
- النطاق: SRC-6CBA87B20C-L000043 إلى SRC-29A9CD43D1-L000243
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-6CBA87B20C — [tests/test_aspect_planning.py](../../tests/test_aspect_planning.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6CBA87B20C-L000043](../../tests/test_aspect_planning.py#L43) | 43 | `"def test_evidence_ledger_marks_missing_and_covered():"` | — |
| [SRC-6CBA87B20C-L000044](../../tests/test_aspect_planning.py#L44) | 44 | `"    aspects = [\"السعر\", \"الضمان\"]"` | — |
| [SRC-6CBA87B20C-L000045](../../tests/test_aspect_planning.py#L45) | 45 | `"    sources = ["` | — |
| [SRC-6CBA87B20C-L000046](../../tests/test_aspect_planning.py#L46) | 46 | `"        {"` | — |
| [SRC-6CBA87B20C-L000047](../../tests/test_aspect_planning.py#L47) | 47 | `"            \"title\": \"أسعار السيارات الكهربائية\","` | — |
| [SRC-6CBA87B20C-L000048](../../tests/test_aspect_planning.py#L48) | 48 | `"            \"url\": \"https://example.com/prices\","` | — |
| [SRC-6CBA87B20C-L000049](../../tests/test_aspect_planning.py#L49) | 49 | `"            \"snippet\": \"متوسط السعر في مصر لعام 2026\","` | — |
| [SRC-6CBA87B20C-L000050](../../tests/test_aspect_planning.py#L50) | 50 | `"            \"page_text\": \"\","` | — |
| [SRC-6CBA87B20C-L000051](../../tests/test_aspect_planning.py#L51) | 51 | `"            \"provider\": \"test\","` | — |
| [SRC-6CBA87B20C-L000052](../../tests/test_aspect_planning.py#L52) | 52 | `"        }"` | — |
| [SRC-6CBA87B20C-L000053](../../tests/test_aspect_planning.py#L53) | 53 | `"    ]"` | — |
| [SRC-6CBA87B20C-L000054](../../tests/test_aspect_planning.py#L54) | 54 | `"    ledger = build_evidence_ledger(aspects, sources)"` | — |
| [SRC-6CBA87B20C-L000055](../../tests/test_aspect_planning.py#L55) | 55 | `"    assert \"السعر\" in ledger[\"covered\"] or any("` | — |
| [SRC-6CBA87B20C-L000056](../../tests/test_aspect_planning.py#L56) | 56 | `"        \"سعر\" in c for c in ledger[\"covered\"]"` | — |
| [SRC-6CBA87B20C-L000057](../../tests/test_aspect_planning.py#L57) | 57 | `"    )"` | — |
| [SRC-6CBA87B20C-L000058](../../tests/test_aspect_planning.py#L58) | 58 | `"    assert \"الضمان\" in ledger[\"missing\"]"` | — |
| [SRC-6CBA87B20C-L000059](../../tests/test_aspect_planning.py#L59) | 59 | `"    assert 0 <= ledger[\"coverage_ratio\"] <= 1"` | — |
| [SRC-6CBA87B20C-L000060](../../tests/test_aspect_planning.py#L60) | 60 | `""` | — |
| [SRC-6CBA87B20C-L000061](../../tests/test_aspect_planning.py#L61) | 61 | `""` | — |
| [SRC-6CBA87B20C-L000062](../../tests/test_aspect_planning.py#L62) | 62 | `"def test_repair_queries_for_missing():"` | — |
| [SRC-6CBA87B20C-L000063](../../tests/test_aspect_planning.py#L63) | 63 | `"    qs = repair_queries_for_missing_aspects("` | — |
| [SRC-6CBA87B20C-L000064](../../tests/test_aspect_planning.py#L64) | 64 | `"        \"السيارات الكهربائية مصر\","` | — |
| [SRC-6CBA87B20C-L000065](../../tests/test_aspect_planning.py#L65) | 65 | `"        [\"الضمان\", \"الصيانة\"],"` | — |
| [SRC-6CBA87B20C-L000066](../../tests/test_aspect_planning.py#L66) | 66 | `"        limit=2,"` | — |
| [SRC-6CBA87B20C-L000067](../../tests/test_aspect_planning.py#L67) | 67 | `"    )"` | — |
| [SRC-6CBA87B20C-L000068](../../tests/test_aspect_planning.py#L68) | 68 | `"    assert len(qs) == 2"` | — |
| [SRC-6CBA87B20C-L000069](../../tests/test_aspect_planning.py#L69) | 69 | `"    assert all(\"السيارات\" in q for q in qs)"` | — |
| [SRC-6CBA87B20C-L000070](../../tests/test_aspect_planning.py#L70) | 70 | `""` | — |
| [SRC-6CBA87B20C-L000071](../../tests/test_aspect_planning.py#L71) | 71 | `""` | — |
| [SRC-6CBA87B20C-L000072](../../tests/test_aspect_planning.py#L72) | 72 | `"def test_arabic_diagnostics_not_truth_claim():"` | — |
| [SRC-6CBA87B20C-L000073](../../tests/test_aspect_planning.py#L73) | 73 | `"    ledger = {"` | — |
| [SRC-6CBA87B20C-L000074](../../tests/test_aspect_planning.py#L74) | 74 | `"        \"covered\": [\"السعر\"],"` | — |
| [SRC-6CBA87B20C-L000075](../../tests/test_aspect_planning.py#L75) | 75 | `"        \"missing\": [\"الضمان\"],"` | — |
| [SRC-6CBA87B20C-L000076](../../tests/test_aspect_planning.py#L76) | 76 | `"        \"coverage_ratio\": 0.5,"` | — |
| [SRC-6CBA87B20C-L000077](../../tests/test_aspect_planning.py#L77) | 77 | `"    }"` | — |
| [SRC-6CBA87B20C-L000078](../../tests/test_aspect_planning.py#L78) | 78 | `"    lines = arabic_aspect_diagnostics(ledger)"` | — |
| [SRC-6CBA87B20C-L000079](../../tests/test_aspect_planning.py#L79) | 79 | `"    assert any(\"ضمان\" in line for line in lines)"` | — |
| [SRC-6CBA87B20C-L000080](../../tests/test_aspect_planning.py#L80) | 80 | `"    assert any(\"لا يثبت\" in line for line in lines)"` | — |
| [SRC-6CBA87B20C-L000081](../../tests/test_aspect_planning.py#L81) | 81 | `""` | — |
| [SRC-6CBA87B20C-L000082](../../tests/test_aspect_planning.py#L82) | 82 | `""` | — |
| [SRC-6CBA87B20C-L000083](../../tests/test_aspect_planning.py#L83) | 83 | `"def test_extract_aspects_understands_compound_connectors_without_marker():"` | — |
| [SRC-6CBA87B20C-L000084](../../tests/test_aspect_planning.py#L84) | 84 | `"    question = ("` | — |
| [SRC-6CBA87B20C-L000085](../../tests/test_aspect_planning.py#L85) | 85 | `"        \"قارن بين الأنظمة: السعر والبطارية، بالإضافة إلى الضمان والصيانة \""` | — |
| [SRC-6CBA87B20C-L000086](../../tests/test_aspect_planning.py#L86) | 86 | `"        \"والخصوصية والاعتمادية والدعم والجودة\""` | — |
| [SRC-6CBA87B20C-L000087](../../tests/test_aspect_planning.py#L87) | 87 | `"    )"` | — |
| [SRC-6CBA87B20C-L000088](../../tests/test_aspect_planning.py#L88) | 88 | `"    aspects = extract_aspects(question)"` | — |
| [SRC-6CBA87B20C-L000089](../../tests/test_aspect_planning.py#L89) | 89 | `"    normalized = \" \".join(aspects)"` | — |
| [SRC-6CBA87B20C-L000090](../../tests/test_aspect_planning.py#L90) | 90 | `"    for expected in (\"السعر\", \"البطارية\", \"الضمان\", \"الصيانة\", \"الخصوصية\", \"الاعتمادية\", \"الدعم\", \"الجودة\"):"` | — |
| [SRC-6CBA87B20C-L000091](../../tests/test_aspect_planning.py#L91) | 91 | `"        assert expected in normalized"` | — |
| [SRC-6CBA87B20C-L000092](../../tests/test_aspect_planning.py#L92) | 92 | `"    assert len(aspects) <= 8"` | — |
| [SRC-6CBA87B20C-L000093](../../tests/test_aspect_planning.py#L93) | 93 | `""` | — |
| [SRC-6CBA87B20C-L000094](../../tests/test_aspect_planning.py#L94) | 94 | `""` | — |
| [SRC-6CBA87B20C-L000095](../../tests/test_aspect_planning.py#L95) | 95 | `"def test_extracts_joined_facets_without_formal_comparison_marker():"` | — |
| [SRC-6CBA87B20C-L000096](../../tests/test_aspect_planning.py#L96) | 96 | `"    aspects = extract_aspects(\"ما سعر الهاتف ومدة الضمان والصيانة؟\")"` | — |
| [SRC-6CBA87B20C-L000097](../../tests/test_aspect_planning.py#L97) | 97 | `"    joined = \" \".join(aspects)"` | — |
| [SRC-6CBA87B20C-L000098](../../tests/test_aspect_planning.py#L98) | 98 | `"    assert \"السعر\" in joined"` | — |
| [SRC-6CBA87B20C-L000099](../../tests/test_aspect_planning.py#L99) | 99 | `"    assert \"الضمان\" in joined"` | — |
| [SRC-6CBA87B20C-L000100](../../tests/test_aspect_planning.py#L100) | 100 | `"    assert \"الصيانة\" in joined"` | — |
| [SRC-6CBA87B20C-L000101](../../tests/test_aspect_planning.py#L101) | 101 | `""` | — |
| [SRC-6CBA87B20C-L000102](../../tests/test_aspect_planning.py#L102) | 102 | `""` | — |
| [SRC-6CBA87B20C-L000103](../../tests/test_aspect_planning.py#L103) | 103 | `"def test_extracts_general_factual_aspects_from_compound_arabic_question():"` | — |
| [SRC-6CBA87B20C-L000104](../../tests/test_aspect_planning.py#L104) | 104 | `"    question = \"اذكر عاصمة مصر وعدد سكان القاهرة، مع مصدر وتاريخ لكل معلومة\""` | — |
| [SRC-6CBA87B20C-L000105](../../tests/test_aspect_planning.py#L105) | 105 | `"    aspects = extract_aspects(question)"` | — |
| [SRC-6CBA87B20C-L000106](../../tests/test_aspect_planning.py#L106) | 106 | `"    joined = \" \".join(aspects)"` | — |
| [SRC-6CBA87B20C-L000107](../../tests/test_aspect_planning.py#L107) | 107 | `"    assert \"العاصمة\" in joined"` | — |
| [SRC-6CBA87B20C-L000108](../../tests/test_aspect_planning.py#L108) | 108 | `"    assert \"عدد السكان\" in joined"` | — |
| [SRC-6CBA87B20C-L000109](../../tests/test_aspect_planning.py#L109) | 109 | `"    assert len(aspects) <= 8"` | — |
| [SRC-6CBA87B20C-L000110](../../tests/test_aspect_planning.py#L110) | 110 | `""` | — |
| [SRC-6CBA87B20C-L000111](../../tests/test_aspect_planning.py#L111) | 111 | `""` | — |
| [SRC-6CBA87B20C-L000112](../../tests/test_aspect_planning.py#L112) | 112 | `"def test_builds_separate_queries_for_capital_and_population_aspects():"` | — |
| [SRC-6CBA87B20C-L000113](../../tests/test_aspect_planning.py#L113) | 113 | `"    question = \"اذكر عاصمة مصر وعدد سكان القاهرة\""` | — |
| [SRC-6CBA87B20C-L000114](../../tests/test_aspect_planning.py#L114) | 114 | `"    aspects = extract_aspects(question)"` | — |
| [SRC-6CBA87B20C-L000115](../../tests/test_aspect_planning.py#L115) | 115 | `"    queries = build_aspect_queries(\"مصر القاهرة\", aspects)"` | — |
| [SRC-6CBA87B20C-L000116](../../tests/test_aspect_planning.py#L116) | 116 | `"    assert any(\"العاصمة\" in query for query in queries)"` | — |
| [SRC-6CBA87B20C-L000117](../../tests/test_aspect_planning.py#L117) | 117 | `"    assert any(\"عدد السكان\" in query for query in queries)"` | — |
## اختبارات

### FILE-6B37B7D6D3 — [tests/test_claim_evidence_metadata.py](../../tests/test_claim_evidence_metadata.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6B37B7D6D3-L000001](../../tests/test_claim_evidence_metadata.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-6B37B7D6D3-L000002](../../tests/test_claim_evidence_metadata.py#L2) | 2 | `""` | — |
| [SRC-6B37B7D6D3-L000003](../../tests/test_claim_evidence_metadata.py#L3) | 3 | `"from agents.claim_evidence import audit_source_metadata, build_claim_evidence_ledger"` | — |
| [SRC-6B37B7D6D3-L000004](../../tests/test_claim_evidence_metadata.py#L4) | 4 | `""` | — |
| [SRC-6B37B7D6D3-L000005](../../tests/test_claim_evidence_metadata.py#L5) | 5 | `""` | — |
| [SRC-6B37B7D6D3-L000006](../../tests/test_claim_evidence_metadata.py#L6) | 6 | `"def test_source_metadata_accepts_complete_population_metadata_without_asserting_truth():"` | — |
| [SRC-6B37B7D6D3-L000007](../../tests/test_claim_evidence_metadata.py#L7) | 7 | `"    result = audit_source_metadata("` | — |
| [SRC-6B37B7D6D3-L000008](../../tests/test_claim_evidence_metadata.py#L8) | 8 | `"        {"` | — |
| [SRC-6B37B7D6D3-L000009](../../tests/test_claim_evidence_metadata.py#L9) | 9 | `"            \"url\": \"https://example.org/census\","` | — |
| [SRC-6B37B7D6D3-L000010](../../tests/test_claim_evidence_metadata.py#L10) | 10 | `"            \"title\": \"Population table\","` | — |
| [SRC-6B37B7D6D3-L000011](../../tests/test_claim_evidence_metadata.py#L11) | 11 | `"            \"publisher\": \"Example Statistics Office\","` | — |
| [SRC-6B37B7D6D3-L000012](../../tests/test_claim_evidence_metadata.py#L12) | 12 | `"            \"published_at\": \"2025-06-01\","` | — |
| [SRC-6B37B7D6D3-L000013](../../tests/test_claim_evidence_metadata.py#L13) | 13 | `"            \"data_reference_period\": \"2025 estimate\","` | — |
| [SRC-6B37B7D6D3-L000014](../../tests/test_claim_evidence_metadata.py#L14) | 14 | `"            \"geographic_scope\": \"Cairo Governorate administrative boundaries\","` | — |
| [SRC-6B37B7D6D3-L000015](../../tests/test_claim_evidence_metadata.py#L15) | 15 | `"            \"snippet\": \"Population estimate for the governorate.\","` | — |
| [SRC-6B37B7D6D3-L000016](../../tests/test_claim_evidence_metadata.py#L16) | 16 | `"        },"` | — |
| [SRC-6B37B7D6D3-L000017](../../tests/test_claim_evidence_metadata.py#L17) | 17 | `"        claim_text=\"عدد سكان محافظة القاهرة\","` | — |
| [SRC-6B37B7D6D3-L000018](../../tests/test_claim_evidence_metadata.py#L18) | 18 | `"    )"` | — |
| [SRC-6B37B7D6D3-L000019](../../tests/test_claim_evidence_metadata.py#L19) | 19 | `""` | — |
| [SRC-6B37B7D6D3-L000020](../../tests/test_claim_evidence_metadata.py#L20) | 20 | `"    assert result[\"status\"] == \"metadata_complete\""` | — |
| [SRC-6B37B7D6D3-L000021](../../tests/test_claim_evidence_metadata.py#L21) | 21 | `"    assert result[\"required_fields_missing\"] == []"` | — |
| [SRC-6B37B7D6D3-L000022](../../tests/test_claim_evidence_metadata.py#L22) | 22 | `"    assert result[\"claim_entailment\"] == \"not_checked\""` | — |
| [SRC-6B37B7D6D3-L000023](../../tests/test_claim_evidence_metadata.py#L23) | 23 | `"    assert result[\"fact_correctness\"] == \"not_checked\""` | — |
| [SRC-6B37B7D6D3-L000024](../../tests/test_claim_evidence_metadata.py#L24) | 24 | `"    assert result[\"semantic_verification\"] is False"` | — |
| [SRC-6B37B7D6D3-L000025](../../tests/test_claim_evidence_metadata.py#L25) | 25 | `""` | — |
| [SRC-6B37B7D6D3-L000026](../../tests/test_claim_evidence_metadata.py#L26) | 26 | `""` | — |
| [SRC-6B37B7D6D3-L000027](../../tests/test_claim_evidence_metadata.py#L27) | 27 | `"def test_source_metadata_flags_missing_publication_date_period_and_population_scope():"` | — |
| [SRC-6B37B7D6D3-L000028](../../tests/test_claim_evidence_metadata.py#L28) | 28 | `"    result = audit_source_metadata("` | — |
| [SRC-6B37B7D6D3-L000029](../../tests/test_claim_evidence_metadata.py#L29) | 29 | `"        {"` | — |
| [SRC-6B37B7D6D3-L000030](../../tests/test_claim_evidence_metadata.py#L30) | 30 | `"            \"url\": \"https://example.org/census\","` | — |
| [SRC-6B37B7D6D3-L000031](../../tests/test_claim_evidence_metadata.py#L31) | 31 | `"            \"title\": \"Population table\","` | — |
| [SRC-6B37B7D6D3-L000032](../../tests/test_claim_evidence_metadata.py#L32) | 32 | `"            \"publisher\": \"Example Statistics Office\","` | — |
| [SRC-6B37B7D6D3-L000033](../../tests/test_claim_evidence_metadata.py#L33) | 33 | `"            \"snippet\": \"Population estimate.\","` | — |
| [SRC-6B37B7D6D3-L000034](../../tests/test_claim_evidence_metadata.py#L34) | 34 | `"        },"` | — |
| [SRC-6B37B7D6D3-L000035](../../tests/test_claim_evidence_metadata.py#L35) | 35 | `"        claim_text=\"عدد سكان القاهرة الكبرى\","` | — |
| [SRC-6B37B7D6D3-L000036](../../tests/test_claim_evidence_metadata.py#L36) | 36 | `"    )"` | — |
| [SRC-6B37B7D6D3-L000037](../../tests/test_claim_evidence_metadata.py#L37) | 37 | `""` | — |
| [SRC-6B37B7D6D3-L000038](../../tests/test_claim_evidence_metadata.py#L38) | 38 | `"    assert result[\"status\"] == \"metadata_incomplete\""` | — |
| [SRC-6B37B7D6D3-L000039](../../tests/test_claim_evidence_metadata.py#L39) | 39 | `"    assert \"publication_date\" in result[\"required_fields_missing\"]"` | — |
| [SRC-6B37B7D6D3-L000040](../../tests/test_claim_evidence_metadata.py#L40) | 40 | `"    assert \"data_reference_period_for_population_claim\" in result[\"required_fields_missing\"]"` | — |
| [SRC-6B37B7D6D3-L000041](../../tests/test_claim_evidence_metadata.py#L41) | 41 | `"    assert \"geographic_scope_for_population_claim\" in result[\"required_fields_missing\"]"` | — |
| [SRC-6B37B7D6D3-L000042](../../tests/test_claim_evidence_metadata.py#L42) | 42 | `""` | — |
| [SRC-6B37B7D6D3-L000043](../../tests/test_claim_evidence_metadata.py#L43) | 43 | `""` | — |
| [SRC-6B37B7D6D3-L000044](../../tests/test_claim_evidence_metadata.py#L44) | 44 | `"def test_source_metadata_rejects_non_http_urls_and_urls_with_credentials():"` | — |
| [SRC-6B37B7D6D3-L000045](../../tests/test_claim_evidence_metadata.py#L45) | 45 | `"    for url in (\"javascript:alert(1)\", \"https://user:password@example.org/data\"):"` | — |
| [SRC-6B37B7D6D3-L000046](../../tests/test_claim_evidence_metadata.py#L46) | 46 | `"        result = audit_source_metadata("` | — |
| [SRC-6B37B7D6D3-L000047](../../tests/test_claim_evidence_metadata.py#L47) | 47 | `"            {"` | — |
| [SRC-6B37B7D6D3-L000048](../../tests/test_claim_evidence_metadata.py#L48) | 48 | `"                \"url\": url,"` | — |
| [SRC-6B37B7D6D3-L000049](../../tests/test_claim_evidence_metadata.py#L49) | 49 | `"                \"title\": \"Research report\","` | — |
| [SRC-6B37B7D6D3-L000050](../../tests/test_claim_evidence_metadata.py#L50) | 50 | `"                \"publisher\": \"Example Statistics Office\","` | — |
| [SRC-6B37B7D6D3-L000051](../../tests/test_claim_evidence_metadata.py#L51) | 51 | `"                \"published_at\": \"2025-06-01\","` | — |
| [SRC-6B37B7D6D3-L000052](../../tests/test_claim_evidence_metadata.py#L52) | 52 | `"                \"snippet\": \"A readable summary.\","` | — |
| [SRC-6B37B7D6D3-L000053](../../tests/test_claim_evidence_metadata.py#L53) | 53 | `"            },"` | — |
| [SRC-6B37B7D6D3-L000054](../../tests/test_claim_evidence_metadata.py#L54) | 54 | `"            claim_text=\"general research\","` | — |
| [SRC-6B37B7D6D3-L000055](../../tests/test_claim_evidence_metadata.py#L55) | 55 | `"        )"` | — |
| [SRC-6B37B7D6D3-L000056](../../tests/test_claim_evidence_metadata.py#L56) | 56 | `""` | — |
| [SRC-6B37B7D6D3-L000057](../../tests/test_claim_evidence_metadata.py#L57) | 57 | `"        assert result[\"valid_http_url\"] is False"` | — |
| [SRC-6B37B7D6D3-L000058](../../tests/test_claim_evidence_metadata.py#L58) | 58 | `"        assert \"valid_http_source_url\" in result[\"required_fields_missing\"]"` | — |
| [SRC-6B37B7D6D3-L000059](../../tests/test_claim_evidence_metadata.py#L59) | 59 | `""` | — |
| [SRC-6B37B7D6D3-L000060](../../tests/test_claim_evidence_metadata.py#L60) | 60 | `""` | — |
| [SRC-6B37B7D6D3-L000061](../../tests/test_claim_evidence_metadata.py#L61) | 61 | `"def test_claim_evidence_ledger_uses_question_context_for_population_metadata():"` | — |
| [SRC-6B37B7D6D3-L000062](../../tests/test_claim_evidence_metadata.py#L62) | 62 | `"    ledger = build_claim_evidence_ledger("` | — |
| [SRC-6B37B7D6D3-L000063](../../tests/test_claim_evidence_metadata.py#L63) | 63 | `"        \"The estimate is 9.7 million [source 1].\","` | — |
| [SRC-6B37B7D6D3-L000064](../../tests/test_claim_evidence_metadata.py#L64) | 64 | `"        ["` | — |
| [SRC-6B37B7D6D3-L000065](../../tests/test_claim_evidence_metadata.py#L65) | 65 | `"            {"` | — |
| [SRC-6B37B7D6D3-L000066](../../tests/test_claim_evidence_metadata.py#L66) | 66 | `"                \"url\": \"https://example.org/census\","` | — |
| [SRC-6B37B7D6D3-L000067](../../tests/test_claim_evidence_metadata.py#L67) | 67 | `"                \"title\": \"Population table\","` | — |
| [SRC-6B37B7D6D3-L000068](../../tests/test_claim_evidence_metadata.py#L68) | 68 | `"                \"publisher\": \"Example Statistics Office\","` | — |
| [SRC-6B37B7D6D3-L000069](../../tests/test_claim_evidence_metadata.py#L69) | 69 | `"                \"published_at\": \"2025-06-01\","` | — |
| [SRC-6B37B7D6D3-L000070](../../tests/test_claim_evidence_metadata.py#L70) | 70 | `"                \"snippet\": \"The estimate is 9.7 million.\","` | — |
| [SRC-6B37B7D6D3-L000071](../../tests/test_claim_evidence_metadata.py#L71) | 71 | `"            }"` | — |
| [SRC-6B37B7D6D3-L000072](../../tests/test_claim_evidence_metadata.py#L72) | 72 | `"        ],"` | — |
| [SRC-6B37B7D6D3-L000073](../../tests/test_claim_evidence_metadata.py#L73) | 73 | `"        question_context=\"How many people live in Cairo?\","` | — |
| [SRC-6B37B7D6D3-L000074](../../tests/test_claim_evidence_metadata.py#L74) | 74 | `"    )"` | — |
| [SRC-6B37B7D6D3-L000075](../../tests/test_claim_evidence_metadata.py#L75) | 75 | `""` | — |
| [SRC-6B37B7D6D3-L000076](../../tests/test_claim_evidence_metadata.py#L76) | 76 | `"    audit = ledger[\"segments\"][0][\"sources\"][0][\"metadata_audit\"]"` | — |
| [SRC-6B37B7D6D3-L000077](../../tests/test_claim_evidence_metadata.py#L77) | 77 | `"    assert audit[\"population_scope_required\"] is True"` | — |
| [SRC-6B37B7D6D3-L000078](../../tests/test_claim_evidence_metadata.py#L78) | 78 | `"    assert \"data_reference_period_for_population_claim\" in audit[\"required_fields_missing\"]"` | — |
| [SRC-6B37B7D6D3-L000079](../../tests/test_claim_evidence_metadata.py#L79) | 79 | `"    assert \"geographic_scope_for_population_claim\" in audit[\"required_fields_missing\"]"` | — |
| [SRC-6B37B7D6D3-L000080](../../tests/test_claim_evidence_metadata.py#L80) | 80 | `"    assert ledger[\"fact_correctness\"] == \"not_checked\""` | — |
## اختبارات

### FILE-DA61479D59 — [tests/test_connector_summary_counters.py](../../tests/test_connector_summary_counters.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-DA61479D59-L000001](../../tests/test_connector_summary_counters.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-DA61479D59-L000002](../../tests/test_connector_summary_counters.py#L2) | 2 | `""` | — |
| [SRC-DA61479D59-L000003](../../tests/test_connector_summary_counters.py#L3) | 3 | `"import json"` | — |
| [SRC-DA61479D59-L000004](../../tests/test_connector_summary_counters.py#L4) | 4 | `""` | — |
| [SRC-DA61479D59-L000005](../../tests/test_connector_summary_counters.py#L5) | 5 | `"from agents.web_agent import PageFetchResult, WebAgent"` | — |
| [SRC-DA61479D59-L000006](../../tests/test_connector_summary_counters.py#L6) | 6 | `""` | — |
| [SRC-DA61479D59-L000007](../../tests/test_connector_summary_counters.py#L7) | 7 | `""` | — |
| [SRC-DA61479D59-L000008](../../tests/test_connector_summary_counters.py#L8) | 8 | `"def test_connector_summary_reports_request_scope_worst_state_and_redacts_secrets(monkeypatch):"` | — |
| [SRC-DA61479D59-L000009](../../tests/test_connector_summary_counters.py#L9) | 9 | `"    agent = WebAgent()"` | — |
| [SRC-DA61479D59-L000010](../../tests/test_connector_summary_counters.py#L10) | 10 | `"    monkeypatch.delenv(\"BRAVE_SEARCH_API_KEY\", raising=False)"` | — |
| [SRC-DA61479D59-L000011](../../tests/test_connector_summary_counters.py#L11) | 11 | `"    diagnostics = ["` | — |
| [SRC-DA61479D59-L000012](../../tests/test_connector_summary_counters.py#L12) | 12 | `"        {"` | — |
| [SRC-DA61479D59-L000013](../../tests/test_connector_summary_counters.py#L13) | 13 | `"            \"provider\": \"duckduckgo_html\","` | — |
| [SRC-DA61479D59-L000014](../../tests/test_connector_summary_counters.py#L14) | 14 | `"            \"query\": \"renewable energy\","` | — |
| [SRC-DA61479D59-L000015](../../tests/test_connector_summary_counters.py#L15) | 15 | `"            \"status\": \"ok\","` | — |
| [SRC-DA61479D59-L000016](../../tests/test_connector_summary_counters.py#L16) | 16 | `"            \"result_count\": 3,"` | — |
| [SRC-DA61479D59-L000017](../../tests/test_connector_summary_counters.py#L17) | 17 | `"            \"rejected_count\": 1,"` | — |
| [SRC-DA61479D59-L000018](../../tests/test_connector_summary_counters.py#L18) | 18 | `"        },"` | — |
| [SRC-DA61479D59-L000019](../../tests/test_connector_summary_counters.py#L19) | 19 | `"        {"` | — |
| [SRC-DA61479D59-L000020](../../tests/test_connector_summary_counters.py#L20) | 20 | `"            \"provider\": \"duckduckgo_html\","` | — |
| [SRC-DA61479D59-L000021](../../tests/test_connector_summary_counters.py#L21) | 21 | `"            \"query\": \"renewable energy\","` | — |
| [SRC-DA61479D59-L000022](../../tests/test_connector_summary_counters.py#L22) | 22 | `"            \"status\": \"failed\","` | — |
| [SRC-DA61479D59-L000023](../../tests/test_connector_summary_counters.py#L23) | 23 | `"            \"result_count\": 0,"` | — |
| [SRC-DA61479D59-L000024](../../tests/test_connector_summary_counters.py#L24) | 24 | `"            \"rejected_count\": 0,"` | — |
| [SRC-DA61479D59-L000025](../../tests/test_connector_summary_counters.py#L25) | 25 | `"            \"error\": \"HTTP 500 token=secret-value\","` | — |
| [SRC-DA61479D59-L000026](../../tests/test_connector_summary_counters.py#L26) | 26 | `"        },"` | — |
| [SRC-DA61479D59-L000027](../../tests/test_connector_summary_counters.py#L27) | 27 | `"    ]"` | — |
| [SRC-DA61479D59-L000028](../../tests/test_connector_summary_counters.py#L28) | 28 | `"    sources = ["` | — |
| [SRC-DA61479D59-L000029](../../tests/test_connector_summary_counters.py#L29) | 29 | `"        {\"url\": \"https://example.com/a\", \"providers\": [\"duckduckgo_html\"]},"` | — |
| [SRC-DA61479D59-L000030](../../tests/test_connector_summary_counters.py#L30) | 30 | `"        {\"url\": \"https://example.org/b\", \"providers\": [\"bing_rss\"]},"` | — |
| [SRC-DA61479D59-L000031](../../tests/test_connector_summary_counters.py#L31) | 31 | `"    ]"` | — |
| [SRC-DA61479D59-L000032](../../tests/test_connector_summary_counters.py#L32) | 32 | `""` | — |
| [SRC-DA61479D59-L000033](../../tests/test_connector_summary_counters.py#L33) | 33 | `"    summary = agent._connector_status_summary(diagnostics, sources)"` | — |
| [SRC-DA61479D59-L000034](../../tests/test_connector_summary_counters.py#L34) | 34 | `""` | — |
| [SRC-DA61479D59-L000035](../../tests/test_connector_summary_counters.py#L35) | 35 | `"    duckduckgo = next(item for item in summary[\"connectors\"] if item[\"name\"] == \"duckduckgo_html\")"` | — |
| [SRC-DA61479D59-L000036](../../tests/test_connector_summary_counters.py#L36) | 36 | `"    brave = next(item for item in summary[\"connectors\"] if item[\"name\"] == \"brave_search_api\")"` | — |
| [SRC-DA61479D59-L000037](../../tests/test_connector_summary_counters.py#L37) | 37 | `"    assert summary[\"scope\"] == \"this_request_only\""` | — |
| [SRC-DA61479D59-L000038](../../tests/test_connector_summary_counters.py#L38) | 38 | `"    assert duckduckgo[\"attempted\"] is True"` | — |
| [SRC-DA61479D59-L000039](../../tests/test_connector_summary_counters.py#L39) | 39 | `"    assert duckduckgo[\"status\"] == \"failed\""` | — |
| [SRC-DA61479D59-L000040](../../tests/test_connector_summary_counters.py#L40) | 40 | `"    assert duckduckgo[\"observed_statuses\"] == [\"ok\", \"failed\"]"` | — |
| [SRC-DA61479D59-L000041](../../tests/test_connector_summary_counters.py#L41) | 41 | `"    assert duckduckgo[\"result_count\"] == 3"` | — |
| [SRC-DA61479D59-L000042](../../tests/test_connector_summary_counters.py#L42) | 42 | `"    assert duckduckgo[\"useful_result_count\"] == 1"` | — |
| [SRC-DA61479D59-L000043](../../tests/test_connector_summary_counters.py#L43) | 43 | `"    assert duckduckgo[\"rejected_count\"] == 1"` | — |
| [SRC-DA61479D59-L000044](../../tests/test_connector_summary_counters.py#L44) | 44 | `"    assert duckduckgo[\"implementation_status\"] == \"implemented_in_code\""` | — |
| [SRC-DA61479D59-L000045](../../tests/test_connector_summary_counters.py#L45) | 45 | `"    assert duckduckgo[\"available_for_this_request\"] is True"` | — |
| [SRC-DA61479D59-L000046](../../tests/test_connector_summary_counters.py#L46) | 46 | `"    assert duckduckgo[\"verified_for_this_request\"] is True"` | — |
| [SRC-DA61479D59-L000047](../../tests/test_connector_summary_counters.py#L47) | 47 | `"    assert duckduckgo[\"failure_observed\"] is True"` | — |
| [SRC-DA61479D59-L000048](../../tests/test_connector_summary_counters.py#L48) | 48 | `"    assert \"secret-value\" not in json.dumps(summary)"` | — |
| [SRC-DA61479D59-L000049](../../tests/test_connector_summary_counters.py#L49) | 49 | `"    assert brave[\"configured\"] is False"` | — |
| [SRC-DA61479D59-L000050](../../tests/test_connector_summary_counters.py#L50) | 50 | `"    assert brave[\"status\"] == \"not_configured\""` | — |
| [SRC-DA61479D59-L000051](../../tests/test_connector_summary_counters.py#L51) | 51 | `"    assert brave[\"available_for_this_request\"] is False"` | — |
| [SRC-DA61479D59-L000052](../../tests/test_connector_summary_counters.py#L52) | 52 | `"    assert brave[\"verified_for_this_request\"] is None"` | — |
| [SRC-DA61479D59-L000053](../../tests/test_connector_summary_counters.py#L53) | 53 | `""` | — |
| [SRC-DA61479D59-L000054](../../tests/test_connector_summary_counters.py#L54) | 54 | `""` | — |
| [SRC-DA61479D59-L000055](../../tests/test_connector_summary_counters.py#L55) | 55 | `"def test_collect_research_distinguishes_raw_rows_unique_urls_and_page_extraction(monkeypatch):"` | — |
| [SRC-DA61479D59-L000056](../../tests/test_connector_summary_counters.py#L56) | 56 | `"    agent = WebAgent()"` | — |
| [SRC-DA61479D59-L000057](../../tests/test_connector_summary_counters.py#L57) | 57 | `"    query = \"renewable energy storage\""` | — |
| [SRC-DA61479D59-L000058](../../tests/test_connector_summary_counters.py#L58) | 58 | `"    results = ["` | — |
| [SRC-DA61479D59-L000059](../../tests/test_connector_summary_counters.py#L59) | 59 | `"        {"` | — |
| [SRC-DA61479D59-L000060](../../tests/test_connector_summary_counters.py#L60) | 60 | `"            \"title\": \"Renewable energy storage report\","` | — |
| [SRC-DA61479D59-L000061](../../tests/test_connector_summary_counters.py#L61) | 61 | `"            \"url\": \"https://example.com/report\","` | — |
| [SRC-DA61479D59-L000062](../../tests/test_connector_summary_counters.py#L62) | 62 | `"            \"snippet\": \"Renewable energy storage data from the report\","` | — |
| [SRC-DA61479D59-L000063](../../tests/test_connector_summary_counters.py#L63) | 63 | `"            \"page_text\": \"\","` | — |
| [SRC-DA61479D59-L000064](../../tests/test_connector_summary_counters.py#L64) | 64 | `"            \"page_fetched\": False,"` | — |
| [SRC-DA61479D59-L000065](../../tests/test_connector_summary_counters.py#L65) | 65 | `"            \"provider\": \"test_search\","` | — |
| [SRC-DA61479D59-L000066](../../tests/test_connector_summary_counters.py#L66) | 66 | `"            \"provider_rank\": 1,"` | — |
| [SRC-DA61479D59-L000067](../../tests/test_connector_summary_counters.py#L67) | 67 | `"            \"search_query\": query,"` | — |
| [SRC-DA61479D59-L000068](../../tests/test_connector_summary_counters.py#L68) | 68 | `"            \"published_at\": \"\","` | — |
| [SRC-DA61479D59-L000069](../../tests/test_connector_summary_counters.py#L69) | 69 | `"        },"` | — |
| [SRC-DA61479D59-L000070](../../tests/test_connector_summary_counters.py#L70) | 70 | `"        {"` | — |
| [SRC-DA61479D59-L000071](../../tests/test_connector_summary_counters.py#L71) | 71 | `"            \"title\": \"Renewable energy storage report (duplicate URL)\","` | — |
| [SRC-DA61479D59-L000072](../../tests/test_connector_summary_counters.py#L72) | 72 | `"            \"url\": \"https://example.com/report?utm_source=test\","` | — |
| [SRC-DA61479D59-L000073](../../tests/test_connector_summary_counters.py#L73) | 73 | `"            \"snippet\": \"Renewable energy storage data from a duplicate result\","` | — |
| [SRC-DA61479D59-L000074](../../tests/test_connector_summary_counters.py#L74) | 74 | `"            \"page_text\": \"\","` | — |
| [SRC-DA61479D59-L000075](../../tests/test_connector_summary_counters.py#L75) | 75 | `"            \"page_fetched\": False,"` | — |
| [SRC-DA61479D59-L000076](../../tests/test_connector_summary_counters.py#L76) | 76 | `"            \"provider\": \"test_search\","` | — |
| [SRC-DA61479D59-L000077](../../tests/test_connector_summary_counters.py#L77) | 77 | `"            \"provider_rank\": 2,"` | — |
| [SRC-DA61479D59-L000078](../../tests/test_connector_summary_counters.py#L78) | 78 | `"            \"search_query\": query,"` | — |
| [SRC-DA61479D59-L000079](../../tests/test_connector_summary_counters.py#L79) | 79 | `"            \"published_at\": \"\","` | — |
| [SRC-DA61479D59-L000080](../../tests/test_connector_summary_counters.py#L80) | 80 | `"        },"` | — |
| [SRC-DA61479D59-L000081](../../tests/test_connector_summary_counters.py#L81) | 81 | `"        {"` | — |
| [SRC-DA61479D59-L000082](../../tests/test_connector_summary_counters.py#L82) | 82 | `"            \"title\": \"Renewable energy storage statistics\","` | — |
| [SRC-DA61479D59-L000083](../../tests/test_connector_summary_counters.py#L83) | 83 | `"            \"url\": \"https://example.org/statistics\","` | — |
| [SRC-DA61479D59-L000084](../../tests/test_connector_summary_counters.py#L84) | 84 | `"            \"snippet\": \"Renewable energy storage statistics\","` | — |
| [SRC-DA61479D59-L000085](../../tests/test_connector_summary_counters.py#L85) | 85 | `"            \"page_text\": \"\","` | — |
| [SRC-DA61479D59-L000086](../../tests/test_connector_summary_counters.py#L86) | 86 | `"            \"page_fetched\": False,"` | — |
| [SRC-DA61479D59-L000087](../../tests/test_connector_summary_counters.py#L87) | 87 | `"            \"provider\": \"test_search\","` | — |
| [SRC-DA61479D59-L000088](../../tests/test_connector_summary_counters.py#L88) | 88 | `"            \"provider_rank\": 3,"` | — |
| [SRC-DA61479D59-L000089](../../tests/test_connector_summary_counters.py#L89) | 89 | `"            \"search_query\": query,"` | — |
| [SRC-DA61479D59-L000090](../../tests/test_connector_summary_counters.py#L90) | 90 | `"            \"published_at\": \"\","` | — |
| [SRC-DA61479D59-L000091](../../tests/test_connector_summary_counters.py#L91) | 91 | `"        },"` | — |
| [SRC-DA61479D59-L000092](../../tests/test_connector_summary_counters.py#L92) | 92 | `"    ]"` | — |
| [SRC-DA61479D59-L000093](../../tests/test_connector_summary_counters.py#L93) | 93 | `""` | — |
| [SRC-DA61479D59-L000094](../../tests/test_connector_summary_counters.py#L94) | 94 | `"    monkeypatch.setattr(agent, \"_search_web\", lambda _query: results)"` | — |
| [SRC-DA61479D59-L000095](../../tests/test_connector_summary_counters.py#L95) | 95 | `"    def fetch(url: str):"` | — |
| [SRC-DA61479D59-L000096](../../tests/test_connector_summary_counters.py#L96) | 96 | `"        if \"example.com\" in url:"` | — |
| [SRC-DA61479D59-L000097](../../tests/test_connector_summary_counters.py#L97) | 97 | `"            return \"Report page\", \"Renewable energy storage page body with extracted text.\""` | — |
| [SRC-DA61479D59-L000098](../../tests/test_connector_summary_counters.py#L98) | 98 | `"        return \"\", \"\""` | — |
| [SRC-DA61479D59-L000099](../../tests/test_connector_summary_counters.py#L99) | 99 | `""` | — |
| [SRC-DA61479D59-L000100](../../tests/test_connector_summary_counters.py#L100) | 100 | `"    monkeypatch.setattr(agent, \"_fetch_page\", fetch)"` | — |
| [SRC-DA61479D59-L000101](../../tests/test_connector_summary_counters.py#L101) | 101 | `"    sources, warnings, report = agent._collect_research({"` | — |
| [SRC-DA61479D59-L000102](../../tests/test_connector_summary_counters.py#L102) | 102 | `"        \"queries\": [query],"` | — |
| [SRC-DA61479D59-L000103](../../tests/test_connector_summary_counters.py#L103) | 103 | `"        \"direct_urls\": [],"` | — |
| [SRC-DA61479D59-L000104](../../tests/test_connector_summary_counters.py#L104) | 104 | `"        \"social_focus\": False,"` | — |
| [SRC-DA61479D59-L000105](../../tests/test_connector_summary_counters.py#L105) | 105 | `"        \"freshness\": \"any\","` | — |
| [SRC-DA61479D59-L000106](../../tests/test_connector_summary_counters.py#L106) | 106 | `"        \"depth\": \"standard\","` | — |
| [SRC-DA61479D59-L000107](../../tests/test_connector_summary_counters.py#L107) | 107 | `"        \"platforms\": [],"` | — |
| [SRC-DA61479D59-L000108](../../tests/test_connector_summary_counters.py#L108) | 108 | `"        \"planning_method\": \"unit_test\","` | — |
| [SRC-DA61479D59-L000109](../../tests/test_connector_summary_counters.py#L109) | 109 | `"    })"` | — |
| [SRC-DA61479D59-L000110](../../tests/test_connector_summary_counters.py#L110) | 110 | `""` | — |
| [SRC-DA61479D59-L000111](../../tests/test_connector_summary_counters.py#L111) | 111 | `"    assert warnings"` | — |
| [SRC-DA61479D59-L000112](../../tests/test_connector_summary_counters.py#L112) | 112 | `"    assert report[\"raw_results\"] == 3"` | — |
| [SRC-DA61479D59-L000113](../../tests/test_connector_summary_counters.py#L113) | 113 | `"    assert report[\"unique_urls\"] == 2"` | — |
| [SRC-DA61479D59-L000114](../../tests/test_connector_summary_counters.py#L114) | 114 | `"    assert report[\"unique_sources\"] == 2"` | — |
| [SRC-DA61479D59-L000115](../../tests/test_connector_summary_counters.py#L115) | 115 | `"    assert report[\"pages_fetch_attempted\"] == 2"` | — |
| [SRC-DA61479D59-L000116](../../tests/test_connector_summary_counters.py#L116) | 116 | `"    assert report[\"pages_content_extracted\"] == 1"` | — |
| [SRC-DA61479D59-L000117](../../tests/test_connector_summary_counters.py#L117) | 117 | `"    assert report[\"pages_extract_failed\"] == 1"` | — |
| [SRC-DA61479D59-L000118](../../tests/test_connector_summary_counters.py#L118) | 118 | `"    assert report[\"page_fetch_status_counts\"][\"content_extracted\"] == 1"` | — |
| [SRC-DA61479D59-L000119](../../tests/test_connector_summary_counters.py#L119) | 119 | `"    assert report[\"page_fetch_status_counts\"][\"no_text_extracted\"] == 1"` | — |
| [SRC-DA61479D59-L000120](../../tests/test_connector_summary_counters.py#L120) | 120 | `"    assert report[\"page_fetch_status_counts\"][\"fetch_failed\"] == 0"` | — |
| [SRC-DA61479D59-L000121](../../tests/test_connector_summary_counters.py#L121) | 121 | `"    assert report[\"page_fetch_status_counts\"][\"partial_extraction\"] == 0"` | — |
| [SRC-DA61479D59-L000122](../../tests/test_connector_summary_counters.py#L122) | 122 | `"    assert report[\"pages_partial_extracted\"] == 0"` | — |
| [SRC-DA61479D59-L000123](../../tests/test_connector_summary_counters.py#L123) | 123 | `"    assert sum(source[\"page_fetch_status\"] == \"content_extracted\" for source in sources) == 1"` | — |
| [SRC-DA61479D59-L000124](../../tests/test_connector_summary_counters.py#L124) | 124 | `"    assert sum(source[\"page_fetch_status\"] == \"no_text_extracted\" for source in sources) == 1"` | — |
| [SRC-DA61479D59-L000125](../../tests/test_connector_summary_counters.py#L125) | 125 | `"    assert report[\"connector_summary\"][\"scope\"] == \"this_request_only\""` | — |
| [SRC-DA61479D59-L000126](../../tests/test_connector_summary_counters.py#L126) | 126 | `""` | — |
| [SRC-DA61479D59-L000127](../../tests/test_connector_summary_counters.py#L127) | 127 | `""` | — |
| [SRC-DA61479D59-L000128](../../tests/test_connector_summary_counters.py#L128) | 128 | `"def test_connector_summary_does_not_claim_timeout_or_budget_exhaustion_was_a_confirmed_attempt(monkeypatch):"` | — |
| [SRC-DA61479D59-L000129](../../tests/test_connector_summary_counters.py#L129) | 129 | `"    agent = WebAgent()"` | — |
| [SRC-DA61479D59-L000130](../../tests/test_connector_summary_counters.py#L130) | 130 | `"    monkeypatch.setenv(\"TAVILY_API_KEY\", \"configured-test-key\")"` | — |
| [SRC-DA61479D59-L000131](../../tests/test_connector_summary_counters.py#L131) | 131 | `"    monkeypatch.setenv(\"DEEPSEEK_SEARCH_API_KEY\", \"configured-test-key\")"` | — |
| [SRC-DA61479D59-L000132](../../tests/test_connector_summary_counters.py#L132) | 132 | `"    timeout = agent._connector_status_summary("` | — |
| [SRC-DA61479D59-L000133](../../tests/test_connector_summary_counters.py#L133) | 133 | `"        [{\"provider\": \"tavily_search_api\", \"query\": \"query\", \"status\": \"timeout\", \"error\": \"request timed out\"}],"` | — |
| [SRC-DA61479D59-L000134](../../tests/test_connector_summary_counters.py#L134) | 134 | `"        [],"` | — |
| [SRC-DA61479D59-L000135](../../tests/test_connector_summary_counters.py#L135) | 135 | `"    )"` | — |
| [SRC-DA61479D59-L000136](../../tests/test_connector_summary_counters.py#L136) | 136 | `"    exhausted = agent._connector_status_summary("` | — |
| [SRC-DA61479D59-L000137](../../tests/test_connector_summary_counters.py#L137) | 137 | `"        [{\"provider\": \"deepseek_search_api\", \"query\": \"query\", \"status\": \"budget_exhausted\"}],"` | — |
| [SRC-DA61479D59-L000138](../../tests/test_connector_summary_counters.py#L138) | 138 | `"        [],"` | — |
| [SRC-DA61479D59-L000139](../../tests/test_connector_summary_counters.py#L139) | 139 | `"    )"` | — |
| [SRC-DA61479D59-L000140](../../tests/test_connector_summary_counters.py#L140) | 140 | `"    tavily = next(item for item in timeout[\"connectors\"] if item[\"name\"] == \"tavily_search_api\")"` | — |
| [SRC-DA61479D59-L000141](../../tests/test_connector_summary_counters.py#L141) | 141 | `"    deepseek = next(item for item in exhausted[\"connectors\"] if item[\"name\"] == \"deepseek_search_api\")"` | — |
| [SRC-DA61479D59-L000142](../../tests/test_connector_summary_counters.py#L142) | 142 | `"    assert tavily[\"configured\"] is True"` | — |
| [SRC-DA61479D59-L000143](../../tests/test_connector_summary_counters.py#L143) | 143 | `"    assert tavily[\"attempted\"] is None"` | — |
| [SRC-DA61479D59-L000144](../../tests/test_connector_summary_counters.py#L144) | 144 | `"    assert tavily[\"status\"] == \"timeout\""` | — |
| [SRC-DA61479D59-L000145](../../tests/test_connector_summary_counters.py#L145) | 145 | `"    assert tavily[\"available_for_this_request\"] is None"` | — |
| [SRC-DA61479D59-L000146](../../tests/test_connector_summary_counters.py#L146) | 146 | `"    assert tavily[\"verified_for_this_request\"] is None"` | — |
| [SRC-DA61479D59-L000147](../../tests/test_connector_summary_counters.py#L147) | 147 | `"    assert tavily[\"failure_observed\"] is True"` | — |
| [SRC-DA61479D59-L000148](../../tests/test_connector_summary_counters.py#L148) | 148 | `"    assert deepseek[\"configured\"] is True"` | — |
| [SRC-DA61479D59-L000149](../../tests/test_connector_summary_counters.py#L149) | 149 | `"    assert deepseek[\"attempted\"] is False"` | — |
| [SRC-DA61479D59-L000150](../../tests/test_connector_summary_counters.py#L150) | 150 | `"    assert deepseek[\"status\"] == \"budget_exhausted\""` | — |
| [SRC-DA61479D59-L000151](../../tests/test_connector_summary_counters.py#L151) | 151 | `"    assert deepseek[\"available_for_this_request\"] is False"` | — |
| [SRC-DA61479D59-L000152](../../tests/test_connector_summary_counters.py#L152) | 152 | `"    assert deepseek[\"verified_for_this_request\"] is None"` | — |
| [SRC-DA61479D59-L000153](../../tests/test_connector_summary_counters.py#L153) | 153 | `""` | — |
| [SRC-DA61479D59-L000154](../../tests/test_connector_summary_counters.py#L154) | 154 | `""` | — |
| [SRC-DA61479D59-L000155](../../tests/test_connector_summary_counters.py#L155) | 155 | `"def test_collect_research_preserves_partial_and_http_failure_page_statuses(monkeypatch):"` | — |
| [SRC-DA61479D59-L000156](../../tests/test_connector_summary_counters.py#L156) | 156 | `"    agent = WebAgent()"` | — |
| [SRC-DA61479D59-L000157](../../tests/test_connector_summary_counters.py#L157) | 157 | `"    query = \"renewable energy storage\""` | — |
| [SRC-DA61479D59-L000158](../../tests/test_connector_summary_counters.py#L158) | 158 | `"    results = ["` | — |
| [SRC-DA61479D59-L000159](../../tests/test_connector_summary_counters.py#L159) | 159 | `"        {"` | — |
| [SRC-DA61479D59-L000160](../../tests/test_connector_summary_counters.py#L160) | 160 | `"            \"title\": \"Renewable energy storage report\","` | — |
| [SRC-DA61479D59-L000161](../../tests/test_connector_summary_counters.py#L161) | 161 | `"            \"url\": \"https://example.com/report\","` | — |
| [SRC-DA61479D59-L000162](../../tests/test_connector_summary_counters.py#L162) | 162 | `"            \"snippet\": \"Renewable energy storage report\","` | — |
| [SRC-DA61479D59-L000163](../../tests/test_connector_summary_counters.py#L163) | 163 | `"            \"page_text\": \"\","` | — |
| [SRC-DA61479D59-L000164](../../tests/test_connector_summary_counters.py#L164) | 164 | `"            \"page_fetched\": False,"` | — |
| [SRC-DA61479D59-L000165](../../tests/test_connector_summary_counters.py#L165) | 165 | `"            \"provider\": \"test_search\","` | — |
| [SRC-DA61479D59-L000166](../../tests/test_connector_summary_counters.py#L166) | 166 | `"            \"provider_rank\": 1,"` | — |
| [SRC-DA61479D59-L000167](../../tests/test_connector_summary_counters.py#L167) | 167 | `"            \"search_query\": query,"` | — |
| [SRC-DA61479D59-L000168](../../tests/test_connector_summary_counters.py#L168) | 168 | `"            \"published_at\": \"\","` | — |
| [SRC-DA61479D59-L000169](../../tests/test_connector_summary_counters.py#L169) | 169 | `"        },"` | — |
| [SRC-DA61479D59-L000170](../../tests/test_connector_summary_counters.py#L170) | 170 | `"        {"` | — |
| [SRC-DA61479D59-L000171](../../tests/test_connector_summary_counters.py#L171) | 171 | `"            \"title\": \"Renewable energy storage statistics\","` | — |
| [SRC-DA61479D59-L000172](../../tests/test_connector_summary_counters.py#L172) | 172 | `"            \"url\": \"https://example.org/statistics\","` | — |
| [SRC-DA61479D59-L000173](../../tests/test_connector_summary_counters.py#L173) | 173 | `"            \"snippet\": \"Renewable energy storage statistics\","` | — |
| [SRC-DA61479D59-L000174](../../tests/test_connector_summary_counters.py#L174) | 174 | `"            \"page_text\": \"\","` | — |
| [SRC-DA61479D59-L000175](../../tests/test_connector_summary_counters.py#L175) | 175 | `"            \"page_fetched\": False,"` | — |
| [SRC-DA61479D59-L000176](../../tests/test_connector_summary_counters.py#L176) | 176 | `"            \"provider\": \"test_search\","` | — |
| [SRC-DA61479D59-L000177](../../tests/test_connector_summary_counters.py#L177) | 177 | `"            \"provider_rank\": 2,"` | — |
| [SRC-DA61479D59-L000178](../../tests/test_connector_summary_counters.py#L178) | 178 | `"            \"search_query\": query,"` | — |
| [SRC-DA61479D59-L000179](../../tests/test_connector_summary_counters.py#L179) | 179 | `"            \"published_at\": \"\","` | — |
| [SRC-DA61479D59-L000180](../../tests/test_connector_summary_counters.py#L180) | 180 | `"        },"` | — |
| [SRC-DA61479D59-L000181](../../tests/test_connector_summary_counters.py#L181) | 181 | `"    ]"` | — |
| [SRC-DA61479D59-L000182](../../tests/test_connector_summary_counters.py#L182) | 182 | `"    monkeypatch.setattr(agent, \"_search_web\", lambda _query: results)"` | — |
| [SRC-DA61479D59-L000183](../../tests/test_connector_summary_counters.py#L183) | 183 | `""` | — |
| [SRC-DA61479D59-L000184](../../tests/test_connector_summary_counters.py#L184) | 184 | `"    def fetch(url: str):"` | — |
| [SRC-DA61479D59-L000185](../../tests/test_connector_summary_counters.py#L185) | 185 | `"        if \"example.com\" in url:"` | — |
| [SRC-DA61479D59-L000186](../../tests/test_connector_summary_counters.py#L186) | 186 | `"            return PageFetchResult("` | — |
| [SRC-DA61479D59-L000187](../../tests/test_connector_summary_counters.py#L187) | 187 | `"                \"Report page\","` | — |
| [SRC-DA61479D59-L000188](../../tests/test_connector_summary_counters.py#L188) | 188 | `"                \"Renewable energy storage body, with an explicit note that extraction was capped.\","` | — |
| [SRC-DA61479D59-L000189](../../tests/test_connector_summary_counters.py#L189) | 189 | `"                \"partial_extraction\","` | — |
| [SRC-DA61479D59-L000190](../../tests/test_connector_summary_counters.py#L190) | 190 | `"            )"` | — |
| [SRC-DA61479D59-L000191](../../tests/test_connector_summary_counters.py#L191) | 191 | `"        return PageFetchResult(\"\", \"\", \"http_error\", \"HTTPStatus\")"` | — |
| [SRC-DA61479D59-L000192](../../tests/test_connector_summary_counters.py#L192) | 192 | `""` | — |
| [SRC-DA61479D59-L000193](../../tests/test_connector_summary_counters.py#L193) | 193 | `"    monkeypatch.setattr(agent, \"_fetch_page\", fetch)"` | — |
| [SRC-DA61479D59-L000194](../../tests/test_connector_summary_counters.py#L194) | 194 | `"    sources, warnings, report = agent._collect_research({"` | — |
| [SRC-DA61479D59-L000195](../../tests/test_connector_summary_counters.py#L195) | 195 | `"        \"queries\": [query],"` | — |
| [SRC-DA61479D59-L000196](../../tests/test_connector_summary_counters.py#L196) | 196 | `"        \"direct_urls\": [],"` | — |
| [SRC-DA61479D59-L000197](../../tests/test_connector_summary_counters.py#L197) | 197 | `"        \"social_focus\": False,"` | — |
| [SRC-DA61479D59-L000198](../../tests/test_connector_summary_counters.py#L198) | 198 | `"        \"freshness\": \"any\","` | — |
| [SRC-DA61479D59-L000199](../../tests/test_connector_summary_counters.py#L199) | 199 | `"        \"depth\": \"standard\","` | — |
| [SRC-DA61479D59-L000200](../../tests/test_connector_summary_counters.py#L200) | 200 | `"        \"platforms\": [],"` | — |
| [SRC-DA61479D59-L000201](../../tests/test_connector_summary_counters.py#L201) | 201 | `"        \"planning_method\": \"unit_test\","` | — |
| [SRC-DA61479D59-L000202](../../tests/test_connector_summary_counters.py#L202) | 202 | `"    })"` | — |
| [SRC-DA61479D59-L000203](../../tests/test_connector_summary_counters.py#L203) | 203 | `""` | — |
| [SRC-DA61479D59-L000204](../../tests/test_connector_summary_counters.py#L204) | 204 | `"    assert warnings"` | — |
| [SRC-DA61479D59-L000205](../../tests/test_connector_summary_counters.py#L205) | 205 | `"    assert report[\"pages_fetch_attempted\"] == 2"` | — |
| [SRC-DA61479D59-L000206](../../tests/test_connector_summary_counters.py#L206) | 206 | `"    assert report[\"pages_content_extracted\"] == 1"` | — |
| [SRC-DA61479D59-L000207](../../tests/test_connector_summary_counters.py#L207) | 207 | `"    assert report[\"pages_partial_extracted\"] == 1"` | — |
| [SRC-DA61479D59-L000208](../../tests/test_connector_summary_counters.py#L208) | 208 | `"    assert report[\"pages_extract_failed\"] == 1"` | — |
| [SRC-DA61479D59-L000209](../../tests/test_connector_summary_counters.py#L209) | 209 | `"    assert report[\"page_fetch_status_counts\"][\"partial_extraction\"] == 1"` | — |
| [SRC-DA61479D59-L000210](../../tests/test_connector_summary_counters.py#L210) | 210 | `"    assert report[\"page_fetch_status_counts\"][\"http_error\"] == 1"` | — |
| [SRC-DA61479D59-L000211](../../tests/test_connector_summary_counters.py#L211) | 211 | `"    assert sum(item[\"page_fetch_status\"] == \"partial_extraction\" for item in sources) == 1"` | — |
| [SRC-DA61479D59-L000212](../../tests/test_connector_summary_counters.py#L212) | 212 | `"    assert sum(item[\"page_fetch_status\"] == \"http_error\" for item in sources) == 1"` | — |
| [SRC-DA61479D59-L000213](../../tests/test_connector_summary_counters.py#L213) | 213 | `"    assert any(\"HTTPStatus\" in str(item.get(\"page_fetch_error_class\")) for item in sources)"` | — |
| [SRC-DA61479D59-L000214](../../tests/test_connector_summary_counters.py#L214) | 214 | `""` | — |
| [SRC-DA61479D59-L000215](../../tests/test_connector_summary_counters.py#L215) | 215 | `""` | — |
| [SRC-DA61479D59-L000216](../../tests/test_connector_summary_counters.py#L216) | 216 | `"def test_raw_provider_diagnostics_redact_credentials_from_queries_and_errors():"` | — |
| [SRC-DA61479D59-L000217](../../tests/test_connector_summary_counters.py#L217) | 217 | `"    agent = WebAgent()"` | — |
| [SRC-DA61479D59-L000218](../../tests/test_connector_summary_counters.py#L218) | 218 | `"    agent._record_provider_diagnostic("` | — |
| [SRC-DA61479D59-L000219](../../tests/test_connector_summary_counters.py#L219) | 219 | `"        provider=\"test_provider\","` | — |
| [SRC-DA61479D59-L000220](../../tests/test_connector_summary_counters.py#L220) | 220 | `"        query=\"research API_KEY=query-secret\","` | — |
| [SRC-DA61479D59-L000221](../../tests/test_connector_summary_counters.py#L221) | 221 | `"        status=\"failed\","` | — |
| [SRC-DA61479D59-L000222](../../tests/test_connector_summary_counters.py#L222) | 222 | `"        error=("` | — |
| [SRC-DA61479D59-L000223](../../tests/test_connector_summary_counters.py#L223) | 223 | `"            \"Authorization: Bearer bearer-secret access_token=access-secret; \""` | — |
| [SRC-DA61479D59-L000224](../../tests/test_connector_summary_counters.py#L224) | 224 | `"            \"URL https://example.test/search?token=url-secret\""` | — |
| [SRC-DA61479D59-L000225](../../tests/test_connector_summary_counters.py#L225) | 225 | `"        ),"` | — |
| [SRC-DA61479D59-L000226](../../tests/test_connector_summary_counters.py#L226) | 226 | `"    )"` | — |
| [SRC-DA61479D59-L000227](../../tests/test_connector_summary_counters.py#L227) | 227 | `""` | — |
| [SRC-DA61479D59-L000228](../../tests/test_connector_summary_counters.py#L228) | 228 | `"    diagnostic_json = json.dumps(agent._provider_diagnostics, ensure_ascii=False)"` | — |
| [SRC-DA61479D59-L000229](../../tests/test_connector_summary_counters.py#L229) | 229 | `"    for secret in (\"query-secret\", \"bearer-secret\", \"access-secret\", \"url-secret\"):"` | — |
| [SRC-DA61479D59-L000230](../../tests/test_connector_summary_counters.py#L230) | 230 | `"        assert secret not in diagnostic_json"` | — |
| [SRC-DA61479D59-L000231](../../tests/test_connector_summary_counters.py#L231) | 231 | `"    assert \"[REDACTED]\" in diagnostic_json"` | — |
| [SRC-DA61479D59-L000232](../../tests/test_connector_summary_counters.py#L232) | 232 | `""` | — |
| [SRC-DA61479D59-L000233](../../tests/test_connector_summary_counters.py#L233) | 233 | `""` | — |
| [SRC-DA61479D59-L000234](../../tests/test_connector_summary_counters.py#L234) | 234 | `"def test_connector_summary_separates_raw_candidates_from_filtered_results():"` | — |
| [SRC-DA61479D59-L000235](../../tests/test_connector_summary_counters.py#L235) | 235 | `"    agent = WebAgent()"` | — |
| [SRC-DA61479D59-L000236](../../tests/test_connector_summary_counters.py#L236) | 236 | `"    summary = agent._connector_status_summary("` | — |
| [SRC-DA61479D59-L000237](../../tests/test_connector_summary_counters.py#L237) | 237 | `"        [{"` | — |
| [SRC-DA61479D59-L000238](../../tests/test_connector_summary_counters.py#L238) | 238 | `"            \"provider\": \"bing_rss\","` | — |
| [SRC-DA61479D59-L000239](../../tests/test_connector_summary_counters.py#L239) | 239 | `"            \"query\": \"Arabic question with source instructions\","` | — |
| [SRC-DA61479D59-L000240](../../tests/test_connector_summary_counters.py#L240) | 240 | `"            \"status\": \"filtered_all\","` | — |
| [SRC-DA61479D59-L000241](../../tests/test_connector_summary_counters.py#L241) | 241 | `"            \"result_count\": 6,"` | — |
| [SRC-DA61479D59-L000242](../../tests/test_connector_summary_counters.py#L242) | 242 | `"            \"accepted_count\": 0,"` | — |
| [SRC-DA61479D59-L000243](../../tests/test_connector_summary_counters.py#L243) | 243 | `"            \"rejected_count\": 6,"` | — |
| [SRC-DA61479D59-L000244](../../tests/test_connector_summary_counters.py#L244) | 244 | `"            \"rejection_counts\": {"` | — |
| [SRC-DA61479D59-L000245](../../tests/test_connector_summary_counters.py#L245) | 245 | `"                \"malformed_candidate\": 0,"` | — |
| [SRC-DA61479D59-L000246](../../tests/test_connector_summary_counters.py#L246) | 246 | `"                \"invalid_url_or_unsafe_target\": 2,"` | — |
| [SRC-DA61479D59-L000247](../../tests/test_connector_summary_counters.py#L247) | 247 | `"                \"blocked_domain\": 1,"` | — |
| [SRC-DA61479D59-L000248](../../tests/test_connector_summary_counters.py#L248) | 248 | `"                \"relevance_below_threshold\": 3,"` | — |
| [SRC-DA61479D59-L000249](../../tests/test_connector_summary_counters.py#L249) | 249 | `"            },"` | — |
| [SRC-DA61479D59-L000250](../../tests/test_connector_summary_counters.py#L250) | 250 | `"            \"error\": \"all candidates rejected; invalid_url_or_unsafe_target=2, blocked_domain=1, relevance_below_threshold=3\","` | — |
| [SRC-DA61479D59-L000251](../../tests/test_connector_summary_counters.py#L251) | 251 | `"        }],"` | — |
| [SRC-DA61479D59-L000252](../../tests/test_connector_summary_counters.py#L252) | 252 | `"        [],"` | — |
| [SRC-DA61479D59-L000253](../../tests/test_connector_summary_counters.py#L253) | 253 | `"    )"` | — |
| [SRC-DA61479D59-L000254](../../tests/test_connector_summary_counters.py#L254) | 254 | `"    bing = next(item for item in summary[\"connectors\"] if item[\"name\"] == \"bing_rss\")"` | — |
| [SRC-DA61479D59-L000255](../../tests/test_connector_summary_counters.py#L255) | 255 | `"    assert bing[\"attempted\"] is True"` | — |
| [SRC-DA61479D59-L000256](../../tests/test_connector_summary_counters.py#L256) | 256 | `"    assert bing[\"result_count\"] == 6"` | — |
| [SRC-DA61479D59-L000257](../../tests/test_connector_summary_counters.py#L257) | 257 | `"    assert bing[\"accepted_count\"] == 0"` | — |
| [SRC-DA61479D59-L000258](../../tests/test_connector_summary_counters.py#L258) | 258 | `"    assert bing[\"rejected_count\"] == 6"` | — |
| [SRC-DA61479D59-L000259](../../tests/test_connector_summary_counters.py#L259) | 259 | `"    assert bing[\"rejection_counts_observed\"] is True"` | — |
| [SRC-DA61479D59-L000260](../../tests/test_connector_summary_counters.py#L260) | 260 | `"    assert bing[\"rejection_counts\"] == {"` | — |
| [SRC-DA61479D59-L000261](../../tests/test_connector_summary_counters.py#L261) | 261 | `"        \"malformed_candidate\": 0,"` | — |
| [SRC-DA61479D59-L000262](../../tests/test_connector_summary_counters.py#L262) | 262 | `"        \"invalid_url_or_unsafe_target\": 2,"` | — |
| [SRC-DA61479D59-L000263](../../tests/test_connector_summary_counters.py#L263) | 263 | `"        \"blocked_domain\": 1,"` | — |
| [SRC-DA61479D59-L000264](../../tests/test_connector_summary_counters.py#L264) | 264 | `"        \"relevance_below_threshold\": 3,"` | — |
| [SRC-DA61479D59-L000265](../../tests/test_connector_summary_counters.py#L265) | 265 | `"    }"` | — |
| [SRC-DA61479D59-L000266](../../tests/test_connector_summary_counters.py#L266) | 266 | `"    assert sum(bing[\"rejection_counts\"].values()) == bing[\"rejected_count\"]"` | — |
| [SRC-DA61479D59-L000267](../../tests/test_connector_summary_counters.py#L267) | 267 | `"    assert bing[\"candidate_rejection_observed\"] is True"` | — |
| [SRC-DA61479D59-L000268](../../tests/test_connector_summary_counters.py#L268) | 268 | `"    assert bing[\"available_for_this_request\"] is True"` | — |
| [SRC-DA61479D59-L000269](../../tests/test_connector_summary_counters.py#L269) | 269 | `"    assert bing[\"verified_for_this_request\"] is True"` | — |
| [SRC-DA61479D59-L000270](../../tests/test_connector_summary_counters.py#L270) | 270 | `""` | — |
| [SRC-DA61479D59-L000271](../../tests/test_connector_summary_counters.py#L271) | 271 | `""` | — |
| [SRC-DA61479D59-L000272](../../tests/test_connector_summary_counters.py#L272) | 272 | `"def test_connector_summary_does_not_present_partial_legacy_rejection_counts_as_complete():"` | — |
| [SRC-DA61479D59-L000273](../../tests/test_connector_summary_counters.py#L273) | 273 | `"    agent = WebAgent()"` | — |
| [SRC-DA61479D59-L000274](../../tests/test_connector_summary_counters.py#L274) | 274 | `"    summary = agent._connector_status_summary("` | — |
| [SRC-DA61479D59-L000275](../../tests/test_connector_summary_counters.py#L275) | 275 | `"        ["` | — |
| [SRC-DA61479D59-L000276](../../tests/test_connector_summary_counters.py#L276) | 276 | `"            {"` | — |
| [SRC-DA61479D59-L000277](../../tests/test_connector_summary_counters.py#L277) | 277 | `"                \"provider\": \"bing_rss\","` | — |
| [SRC-DA61479D59-L000278](../../tests/test_connector_summary_counters.py#L278) | 278 | `"                \"query\": \"first query\","` | — |
| [SRC-DA61479D59-L000279](../../tests/test_connector_summary_counters.py#L279) | 279 | `"                \"status\": \"filtered_all\","` | — |
| [SRC-DA61479D59-L000280](../../tests/test_connector_summary_counters.py#L280) | 280 | `"                \"result_count\": 3,"` | — |
| [SRC-DA61479D59-L000281](../../tests/test_connector_summary_counters.py#L281) | 281 | `"                \"accepted_count\": 0,"` | — |
| [SRC-DA61479D59-L000282](../../tests/test_connector_summary_counters.py#L282) | 282 | `"                \"rejected_count\": 3,"` | — |
| [SRC-DA61479D59-L000283](../../tests/test_connector_summary_counters.py#L283) | 283 | `"            },"` | — |
| [SRC-DA61479D59-L000284](../../tests/test_connector_summary_counters.py#L284) | 284 | `"            {"` | — |
| [SRC-DA61479D59-L000285](../../tests/test_connector_summary_counters.py#L285) | 285 | `"                \"provider\": \"bing_rss\","` | — |
| [SRC-DA61479D59-L000286](../../tests/test_connector_summary_counters.py#L286) | 286 | `"                \"query\": \"second query\","` | — |
| [SRC-DA61479D59-L000287](../../tests/test_connector_summary_counters.py#L287) | 287 | `"                \"status\": \"filtered_all\","` | — |
| [SRC-DA61479D59-L000288](../../tests/test_connector_summary_counters.py#L288) | 288 | `"                \"result_count\": 2,"` | — |
| [SRC-DA61479D59-L000289](../../tests/test_connector_summary_counters.py#L289) | 289 | `"                \"accepted_count\": 0,"` | — |
| [SRC-DA61479D59-L000290](../../tests/test_connector_summary_counters.py#L290) | 290 | `"                \"rejected_count\": 2,"` | — |
| [SRC-DA61479D59-L000291](../../tests/test_connector_summary_counters.py#L291) | 291 | `"                \"rejection_counts\": {"` | — |
| [SRC-DA61479D59-L000292](../../tests/test_connector_summary_counters.py#L292) | 292 | `"                    \"malformed_candidate\": 0,"` | — |
| [SRC-DA61479D59-L000293](../../tests/test_connector_summary_counters.py#L293) | 293 | `"                    \"invalid_url_or_unsafe_target\": 0,"` | — |
| [SRC-DA61479D59-L000294](../../tests/test_connector_summary_counters.py#L294) | 294 | `"                    \"blocked_domain\": 0,"` | — |
| [SRC-DA61479D59-L000295](../../tests/test_connector_summary_counters.py#L295) | 295 | `"                    \"relevance_below_threshold\": 2,"` | — |
| [SRC-DA61479D59-L000296](../../tests/test_connector_summary_counters.py#L296) | 296 | `"                },"` | — |
| [SRC-DA61479D59-L000297](../../tests/test_connector_summary_counters.py#L297) | 297 | `"            },"` | — |
| [SRC-DA61479D59-L000298](../../tests/test_connector_summary_counters.py#L298) | 298 | `"        ],"` | — |
| [SRC-DA61479D59-L000299](../../tests/test_connector_summary_counters.py#L299) | 299 | `"        [],"` | — |
| [SRC-DA61479D59-L000300](../../tests/test_connector_summary_counters.py#L300) | 300 | `"    )"` | — |
| [SRC-DA61479D59-L000301](../../tests/test_connector_summary_counters.py#L301) | 301 | `"    bing = next(item for item in summary[\"connectors\"] if item[\"name\"] == \"bing_rss\")"` | — |
| [SRC-DA61479D59-L000302](../../tests/test_connector_summary_counters.py#L302) | 302 | `"    assert bing[\"rejected_count\"] == 5"` | — |
| [SRC-DA61479D59-L000303](../../tests/test_connector_summary_counters.py#L303) | 303 | `"    assert bing[\"rejection_counts_observed\"] is False"` | — |
| [SRC-DA61479D59-L000304](../../tests/test_connector_summary_counters.py#L304) | 304 | `"    assert bing[\"rejection_counts\"] is None"` | — |
## اختبارات

### FILE-6BECF5AD00 — [tests/test_connectors_mocked.py](../../tests/test_connectors_mocked.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6BECF5AD00-L000001](../../tests/test_connectors_mocked.py#L1) | 1 | `"\"\"\"Connector unit tests with mocked HTTP (no live network required).\"\"\""` | — |
| [SRC-6BECF5AD00-L000002](../../tests/test_connectors_mocked.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-6BECF5AD00-L000003](../../tests/test_connectors_mocked.py#L3) | 3 | `""` | — |
| [SRC-6BECF5AD00-L000004](../../tests/test_connectors_mocked.py#L4) | 4 | `""` | — |
| [SRC-6BECF5AD00-L000005](../../tests/test_connectors_mocked.py#L5) | 5 | `"import agents.search_connectors as sc"` | — |
| [SRC-6BECF5AD00-L000006](../../tests/test_connectors_mocked.py#L6) | 6 | `""` | — |
| [SRC-6BECF5AD00-L000007](../../tests/test_connectors_mocked.py#L7) | 7 | `""` | — |
| [SRC-6BECF5AD00-L000008](../../tests/test_connectors_mocked.py#L8) | 8 | `"def test_openalex_parses_mocked_payload(monkeypatch):"` | — |
| [SRC-6BECF5AD00-L000009](../../tests/test_connectors_mocked.py#L9) | 9 | `"    payload = {"` | — |
| [SRC-6BECF5AD00-L000010](../../tests/test_connectors_mocked.py#L10) | 10 | `"        \"results\": ["` | — |
| [SRC-6BECF5AD00-L000011](../../tests/test_connectors_mocked.py#L11) | 11 | `"            {"` | — |
| [SRC-6BECF5AD00-L000012](../../tests/test_connectors_mocked.py#L12) | 12 | `"                \"display_name\": \"Electric Vehicles in Egypt\","` | — |
| [SRC-6BECF5AD00-L000013](../../tests/test_connectors_mocked.py#L13) | 13 | `"                \"id\": \"https://openalex.org/W123\","` | — |
| [SRC-6BECF5AD00-L000014](../../tests/test_connectors_mocked.py#L14) | 14 | `"                \"primary_location\": {\"landing_page_url\": \"https://example.org/paper\"},"` | — |
| [SRC-6BECF5AD00-L000015](../../tests/test_connectors_mocked.py#L15) | 15 | `"                \"concepts\": [{\"display_name\": \"Battery\"}],"` | — |
| [SRC-6BECF5AD00-L000016](../../tests/test_connectors_mocked.py#L16) | 16 | `"                \"publication_date\": \"2024-01-01\","` | — |
| [SRC-6BECF5AD00-L000017](../../tests/test_connectors_mocked.py#L17) | 17 | `"            }"` | — |
| [SRC-6BECF5AD00-L000018](../../tests/test_connectors_mocked.py#L18) | 18 | `"        ]"` | — |
| [SRC-6BECF5AD00-L000019](../../tests/test_connectors_mocked.py#L19) | 19 | `"    }"` | — |
| [SRC-6BECF5AD00-L000020](../../tests/test_connectors_mocked.py#L20) | 20 | `""` | — |
| [SRC-6BECF5AD00-L000021](../../tests/test_connectors_mocked.py#L21) | 21 | `"    def fake_json(url, headers=None, timeout=12):"` | — |
| [SRC-6BECF5AD00-L000022](../../tests/test_connectors_mocked.py#L22) | 22 | `"        return payload"` | — |
| [SRC-6BECF5AD00-L000023](../../tests/test_connectors_mocked.py#L23) | 23 | `""` | — |
| [SRC-6BECF5AD00-L000024](../../tests/test_connectors_mocked.py#L24) | 24 | `"    monkeypatch.setattr(sc, \"_http_get_json\", fake_json)"` | — |
| [SRC-6BECF5AD00-L000025](../../tests/test_connectors_mocked.py#L25) | 25 | `"    rows = sc.search_openalex(\"electric vehicles Egypt\", limit=3)"` | — |
| [SRC-6BECF5AD00-L000026](../../tests/test_connectors_mocked.py#L26) | 26 | `"    assert len(rows) == 1"` | — |
| [SRC-6BECF5AD00-L000027](../../tests/test_connectors_mocked.py#L27) | 27 | `"    assert rows[0][\"provider\"] == \"openalex\""` | — |
| [SRC-6BECF5AD00-L000028](../../tests/test_connectors_mocked.py#L28) | 28 | `"    assert rows[0][\"url\"] == \"https://example.org/paper\""` | — |
| [SRC-6BECF5AD00-L000029](../../tests/test_connectors_mocked.py#L29) | 29 | `"    assert rows[0][\"page_fetched\"] is False"` | — |
| [SRC-6BECF5AD00-L000030](../../tests/test_connectors_mocked.py#L30) | 30 | `""` | — |
| [SRC-6BECF5AD00-L000031](../../tests/test_connectors_mocked.py#L31) | 31 | `""` | — |
| [SRC-6BECF5AD00-L000032](../../tests/test_connectors_mocked.py#L32) | 32 | `"def test_arxiv_parses_atom(monkeypatch):"` | — |
| [SRC-6BECF5AD00-L000033](../../tests/test_connectors_mocked.py#L33) | 33 | `"    xml = \"\"\""` | — |
| [SRC-6BECF5AD00-L000034](../../tests/test_connectors_mocked.py#L34) | 34 | `"    <feed>"` | — |
| [SRC-6BECF5AD00-L000035](../../tests/test_connectors_mocked.py#L35) | 35 | `"      <entry>"` | — |
| [SRC-6BECF5AD00-L000036](../../tests/test_connectors_mocked.py#L36) | 36 | `"        <title>Study of EV Batteries</title>"` | — |
| [SRC-6BECF5AD00-L000037](../../tests/test_connectors_mocked.py#L37) | 37 | `"        <id>http://arxiv.org/abs/2401.00001</id>"` | — |
| [SRC-6BECF5AD00-L000038](../../tests/test_connectors_mocked.py#L38) | 38 | `"        <summary>Battery degradation analysis.</summary>"` | — |
| [SRC-6BECF5AD00-L000039](../../tests/test_connectors_mocked.py#L39) | 39 | `"        <published>2024-01-02T00:00:00Z</published>"` | — |
| [SRC-6BECF5AD00-L000040](../../tests/test_connectors_mocked.py#L40) | 40 | `"      </entry>"` | — |
| [SRC-6BECF5AD00-L000041](../../tests/test_connectors_mocked.py#L41) | 41 | `"    </feed>"` | — |
| [SRC-6BECF5AD00-L000042](../../tests/test_connectors_mocked.py#L42) | 42 | `"    \"\"\""` | — |
| [SRC-6BECF5AD00-L000043](../../tests/test_connectors_mocked.py#L43) | 43 | `""` | — |
| [SRC-6BECF5AD00-L000044](../../tests/test_connectors_mocked.py#L44) | 44 | `"    monkeypatch.setattr(sc, \"_http_get_text\", lambda url, timeout=12: xml)"` | — |
| [SRC-6BECF5AD00-L000045](../../tests/test_connectors_mocked.py#L45) | 45 | `"    rows = sc.search_arxiv(\"battery\", limit=2)"` | — |
| [SRC-6BECF5AD00-L000046](../../tests/test_connectors_mocked.py#L46) | 46 | `"    assert len(rows) == 1"` | — |
| [SRC-6BECF5AD00-L000047](../../tests/test_connectors_mocked.py#L47) | 47 | `"    assert rows[0][\"provider\"] == \"arxiv\""` | — |
| [SRC-6BECF5AD00-L000048](../../tests/test_connectors_mocked.py#L48) | 48 | `"    assert \"arxiv.org\" in rows[0][\"url\"]"` | — |
| [SRC-6BECF5AD00-L000049](../../tests/test_connectors_mocked.py#L49) | 49 | `""` | — |
| [SRC-6BECF5AD00-L000050](../../tests/test_connectors_mocked.py#L50) | 50 | `""` | — |
| [SRC-6BECF5AD00-L000051](../../tests/test_connectors_mocked.py#L51) | 51 | `"def test_connector_failure_returns_empty(monkeypatch):"` | — |
| [SRC-6BECF5AD00-L000052](../../tests/test_connectors_mocked.py#L52) | 52 | `"    def boom(*args, **kwargs):"` | — |
| [SRC-6BECF5AD00-L000053](../../tests/test_connectors_mocked.py#L53) | 53 | `"        raise sc.urllib.error.URLError(\"down\")"` | — |
| [SRC-6BECF5AD00-L000054](../../tests/test_connectors_mocked.py#L54) | 54 | `""` | — |
| [SRC-6BECF5AD00-L000055](../../tests/test_connectors_mocked.py#L55) | 55 | `"    monkeypatch.setattr(sc, \"_http_get_json\", boom)"` | — |
| [SRC-6BECF5AD00-L000056](../../tests/test_connectors_mocked.py#L56) | 56 | `"    assert sc.run_connector(\"openalex\", \"query\") == []"` | — |
| [SRC-6BECF5AD00-L000057](../../tests/test_connectors_mocked.py#L57) | 57 | `""` | — |
| [SRC-6BECF5AD00-L000058](../../tests/test_connectors_mocked.py#L58) | 58 | `""` | — |
| [SRC-6BECF5AD00-L000059](../../tests/test_connectors_mocked.py#L59) | 59 | `"def test_run_free_academic_dedupe_path(monkeypatch):"` | — |
| [SRC-6BECF5AD00-L000060](../../tests/test_connectors_mocked.py#L60) | 60 | `"    def fake_run(name, query, limit=4):"` | — |
| [SRC-6BECF5AD00-L000061](../../tests/test_connectors_mocked.py#L61) | 61 | `"        return ["` | — |
| [SRC-6BECF5AD00-L000062](../../tests/test_connectors_mocked.py#L62) | 62 | `"            {"` | — |
| [SRC-6BECF5AD00-L000063](../../tests/test_connectors_mocked.py#L63) | 63 | `"                \"title\": f\"{name}-title\","` | — |
| [SRC-6BECF5AD00-L000064](../../tests/test_connectors_mocked.py#L64) | 64 | `"                \"url\": f\"https://example.com/{name}\","` | — |
| [SRC-6BECF5AD00-L000065](../../tests/test_connectors_mocked.py#L65) | 65 | `"                \"snippet\": \"x\","` | — |
| [SRC-6BECF5AD00-L000066](../../tests/test_connectors_mocked.py#L66) | 66 | `"                \"page_fetched\": False,"` | — |
| [SRC-6BECF5AD00-L000067](../../tests/test_connectors_mocked.py#L67) | 67 | `"                \"provider\": name,"` | — |
| [SRC-6BECF5AD00-L000068](../../tests/test_connectors_mocked.py#L68) | 68 | `"                \"provider_rank\": 1,"` | — |
| [SRC-6BECF5AD00-L000069](../../tests/test_connectors_mocked.py#L69) | 69 | `"                \"search_query\": query,"` | — |
| [SRC-6BECF5AD00-L000070](../../tests/test_connectors_mocked.py#L70) | 70 | `"                \"published_at\": \"\","` | — |
| [SRC-6BECF5AD00-L000071](../../tests/test_connectors_mocked.py#L71) | 71 | `"                \"source_class\": \"academic\","` | — |
| [SRC-6BECF5AD00-L000072](../../tests/test_connectors_mocked.py#L72) | 72 | `"            }"` | — |
| [SRC-6BECF5AD00-L000073](../../tests/test_connectors_mocked.py#L73) | 73 | `"        ]"` | — |
| [SRC-6BECF5AD00-L000074](../../tests/test_connectors_mocked.py#L74) | 74 | `""` | — |
| [SRC-6BECF5AD00-L000075](../../tests/test_connectors_mocked.py#L75) | 75 | `"    monkeypatch.setattr(sc, \"run_connector\", fake_run)"` | — |
| [SRC-6BECF5AD00-L000076](../../tests/test_connectors_mocked.py#L76) | 76 | `"    rows = sc.run_free_academic_connectors(\"ev egypt\", limit_per=1)"` | — |
| [SRC-6BECF5AD00-L000077](../../tests/test_connectors_mocked.py#L77) | 77 | `"    assert len(rows) == 3"` | — |
| [SRC-6BECF5AD00-L000078](../../tests/test_connectors_mocked.py#L78) | 78 | `"    providers = {r[\"provider\"] for r in rows}"` | — |
| [SRC-6BECF5AD00-L000079](../../tests/test_connectors_mocked.py#L79) | 79 | `"    assert providers == {\"openalex\", \"arxiv\", \"crossref\"}"` | — |
## اختبارات

### FILE-3D0A619359 — [tests/test_dashboard_security.py](../../tests/test_dashboard_security.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-3D0A619359-L000001](../../tests/test_dashboard_security.py#L1) | 1 | `"\"\"\"Static regression checks for sensitive lead-dashboard browser behavior.\"\"\""` | — |
| [SRC-3D0A619359-L000002](../../tests/test_dashboard_security.py#L2) | 2 | `"from pathlib import Path"` | — |
| [SRC-3D0A619359-L000003](../../tests/test_dashboard_security.py#L3) | 3 | `""` | — |
| [SRC-3D0A619359-L000004](../../tests/test_dashboard_security.py#L4) | 4 | `"DASHBOARD = Path(__file__).resolve().parents[1] / \"web\" / \"dashboard.html\""` | — |
| [SRC-3D0A619359-L000005](../../tests/test_dashboard_security.py#L5) | 5 | `""` | — |
| [SRC-3D0A619359-L000006](../../tests/test_dashboard_security.py#L6) | 6 | `""` | — |
| [SRC-3D0A619359-L000007](../../tests/test_dashboard_security.py#L7) | 7 | `"def test_hosted_lead_dashboard_can_send_the_private_access_token():"` | — |
| [SRC-3D0A619359-L000008](../../tests/test_dashboard_security.py#L8) | 8 | `"    html = DASHBOARD.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000009](../../tests/test_dashboard_security.py#L9) | 9 | `"    assert 'const ACCESS_TOKEN_STORAGE_KEY=\"omarai_access_token\"' in html"` | — |
| [SRC-3D0A619359-L000010](../../tests/test_dashboard_security.py#L10) | 10 | `"    assert 'headers.Authorization=\"Bearer \"+token' in html"` | — |
| [SRC-3D0A619359-L000011](../../tests/test_dashboard_security.py#L11) | 11 | `"    assert '$(\"saveAccessToken\").onclick' in html"` | — |
| [SRC-3D0A619359-L000012](../../tests/test_dashboard_security.py#L12) | 12 | `""` | — |
| [SRC-3D0A619359-L000013](../../tests/test_dashboard_security.py#L13) | 13 | `""` | — |
| [SRC-3D0A619359-L000014](../../tests/test_dashboard_security.py#L14) | 14 | `"def test_saved_lead_source_links_reject_non_http_schemes():"` | — |
| [SRC-3D0A619359-L000015](../../tests/test_dashboard_security.py#L15) | 15 | `"    html = DASHBOARD.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000016](../../tests/test_dashboard_security.py#L16) | 16 | `"    assert \"function safeSourceUrl(value)\" in html"` | — |
| [SRC-3D0A619359-L000017](../../tests/test_dashboard_security.py#L17) | 17 | `"    assert '[\"http:\",\"https:\"]' in html"` | — |
| [SRC-3D0A619359-L000018](../../tests/test_dashboard_security.py#L18) | 18 | `"    assert \"const sourceUrl=safeSourceUrl(l.source_url)\" in html"` | — |
| [SRC-3D0A619359-L000019](../../tests/test_dashboard_security.py#L19) | 19 | `"    assert \"const sourceLink=sourceUrl?\" in html"` | — |
## اختبارات

### FILE-29A9CD43D1 — [tests/test_dialogue_context_pipeline.py](../../tests/test_dialogue_context_pipeline.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-29A9CD43D1-L000001](../../tests/test_dialogue_context_pipeline.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-29A9CD43D1-L000002](../../tests/test_dialogue_context_pipeline.py#L2) | 2 | `""` | — |
| [SRC-29A9CD43D1-L000003](../../tests/test_dialogue_context_pipeline.py#L3) | 3 | `"import json"` | — |
| [SRC-29A9CD43D1-L000004](../../tests/test_dialogue_context_pipeline.py#L4) | 4 | `"from typing import Any"` | — |
| [SRC-29A9CD43D1-L000005](../../tests/test_dialogue_context_pipeline.py#L5) | 5 | `""` | — |
| [SRC-29A9CD43D1-L000006](../../tests/test_dialogue_context_pipeline.py#L6) | 6 | `"import pytest"` | — |
| [SRC-29A9CD43D1-L000007](../../tests/test_dialogue_context_pipeline.py#L7) | 7 | `""` | — |
| [SRC-29A9CD43D1-L000008](../../tests/test_dialogue_context_pipeline.py#L8) | 8 | `"from agents.research import evidence_signal_report"` | — |
| [SRC-29A9CD43D1-L000009](../../tests/test_dialogue_context_pipeline.py#L9) | 9 | `"from agents.dialogue_state import might_be_context_dependent"` | — |
| [SRC-29A9CD43D1-L000010](../../tests/test_dialogue_context_pipeline.py#L10) | 10 | `"from agents.web_agent import WebAgent"` | — |
| [SRC-29A9CD43D1-L000011](../../tests/test_dialogue_context_pipeline.py#L11) | 11 | `""` | — |
| [SRC-29A9CD43D1-L000012](../../tests/test_dialogue_context_pipeline.py#L12) | 12 | `""` | — |
| [SRC-29A9CD43D1-L000013](../../tests/test_dialogue_context_pipeline.py#L13) | 13 | `"def _source(domain: str, queries: list[str]) -> dict[str, Any]:"` | — |
| [SRC-29A9CD43D1-L000014](../../tests/test_dialogue_context_pipeline.py#L14) | 14 | `"    return {"` | — |
| [SRC-29A9CD43D1-L000015](../../tests/test_dialogue_context_pipeline.py#L15) | 15 | `"        \"title\": \"iPhone 17 256GB international warranty coverage in Egypt\","` | — |
| [SRC-29A9CD43D1-L000016](../../tests/test_dialogue_context_pipeline.py#L16) | 16 | `"        \"url\": f\"https://{domain}/iphone-warranty\","` | — |
| [SRC-29A9CD43D1-L000017](../../tests/test_dialogue_context_pipeline.py#L17) | 17 | `"        \"snippet\": \"Warranty coverage and service policy for iPhone 17 in Egypt.\","` | — |
| [SRC-29A9CD43D1-L000018](../../tests/test_dialogue_context_pipeline.py#L18) | 18 | `"        \"page_text\": \"Warranty coverage and service policy for iPhone 17 in Egypt.\","` | — |
| [SRC-29A9CD43D1-L000019](../../tests/test_dialogue_context_pipeline.py#L19) | 19 | `"        \"page_fetched\": True,"` | — |
| [SRC-29A9CD43D1-L000020](../../tests/test_dialogue_context_pipeline.py#L20) | 20 | `"        \"providers\": [\"test_search\"],"` | — |
| [SRC-29A9CD43D1-L000021](../../tests/test_dialogue_context_pipeline.py#L21) | 21 | `"        \"queries\": list(queries),"` | — |
| [SRC-29A9CD43D1-L000022](../../tests/test_dialogue_context_pipeline.py#L22) | 22 | `"        \"domain\": domain,"` | — |
| [SRC-29A9CD43D1-L000023](../../tests/test_dialogue_context_pipeline.py#L23) | 23 | `"        \"source_class\": \"general\","` | — |
| [SRC-29A9CD43D1-L000024](../../tests/test_dialogue_context_pipeline.py#L24) | 24 | `"        \"platform\": \"web\","` | — |
| [SRC-29A9CD43D1-L000025](../../tests/test_dialogue_context_pipeline.py#L25) | 25 | `"        \"published_at\": \"\","` | — |
| [SRC-29A9CD43D1-L000026](../../tests/test_dialogue_context_pipeline.py#L26) | 26 | `"        \"rank_score\": 1.0,"` | — |
| [SRC-29A9CD43D1-L000027](../../tests/test_dialogue_context_pipeline.py#L27) | 27 | `"    }"` | — |
| [SRC-29A9CD43D1-L000028](../../tests/test_dialogue_context_pipeline.py#L28) | 28 | `""` | — |
| [SRC-29A9CD43D1-L000029](../../tests/test_dialogue_context_pipeline.py#L29) | 29 | `""` | — |
| [SRC-29A9CD43D1-L000030](../../tests/test_dialogue_context_pipeline.py#L30) | 30 | `"def _report(plan: dict[str, Any], sources: list[dict[str, Any]]) -> dict[str, Any]:"` | — |
| [SRC-29A9CD43D1-L000031](../../tests/test_dialogue_context_pipeline.py#L31) | 31 | `"    return {"` | — |
| [SRC-29A9CD43D1-L000032](../../tests/test_dialogue_context_pipeline.py#L32) | 32 | `"        \"queries_planned\": len(plan.get(\"queries\", [])),"` | — |
| [SRC-29A9CD43D1-L000033](../../tests/test_dialogue_context_pipeline.py#L33) | 33 | `"        \"queries_attempted\": len(plan.get(\"queries\", [])),"` | — |
| [SRC-29A9CD43D1-L000034](../../tests/test_dialogue_context_pipeline.py#L34) | 34 | `"        \"queries_attempted_known\": True,"` | — |
| [SRC-29A9CD43D1-L000035](../../tests/test_dialogue_context_pipeline.py#L35) | 35 | `"        \"search_attempted\": True,"` | — |
| [SRC-29A9CD43D1-L000036](../../tests/test_dialogue_context_pipeline.py#L36) | 36 | `"        \"search_outcome\": \"attempted_with_usable_sources\","` | — |
| [SRC-29A9CD43D1-L000037](../../tests/test_dialogue_context_pipeline.py#L37) | 37 | `"        \"query_results\": [],"` | — |
| [SRC-29A9CD43D1-L000038](../../tests/test_dialogue_context_pipeline.py#L38) | 38 | `"        \"unique_sources\": len(sources),"` | — |
| [SRC-29A9CD43D1-L000039](../../tests/test_dialogue_context_pipeline.py#L39) | 39 | `"        \"pages_fetched\": len(sources),"` | — |
| [SRC-29A9CD43D1-L000040](../../tests/test_dialogue_context_pipeline.py#L40) | 40 | `"        \"providers_used\": [\"test_search\"],"` | — |
| [SRC-29A9CD43D1-L000041](../../tests/test_dialogue_context_pipeline.py#L41) | 41 | `"        \"provider_counts\": {\"test_search\": len(sources)},"` | — |
| [SRC-29A9CD43D1-L000042](../../tests/test_dialogue_context_pipeline.py#L42) | 42 | `"        \"platform_counts\": {\"web\": len(sources)},"` | — |
| [SRC-29A9CD43D1-L000043](../../tests/test_dialogue_context_pipeline.py#L43) | 43 | `"        \"social_direct_results\": 0,"` | — |
| [SRC-29A9CD43D1-L000044](../../tests/test_dialogue_context_pipeline.py#L44) | 44 | `"        \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-29A9CD43D1-L000045](../../tests/test_dialogue_context_pipeline.py#L45) | 45 | `"        \"planning_method\": plan.get(\"planning_method\", \"test\"),"` | — |
| [SRC-29A9CD43D1-L000046](../../tests/test_dialogue_context_pipeline.py#L46) | 46 | `"        \"evidence_signals\": evidence_signal_report(sources),"` | — |
| [SRC-29A9CD43D1-L000047](../../tests/test_dialogue_context_pipeline.py#L47) | 47 | `"    }"` | — |
| [SRC-29A9CD43D1-L000048](../../tests/test_dialogue_context_pipeline.py#L48) | 48 | `""` | — |
| [SRC-29A9CD43D1-L000049](../../tests/test_dialogue_context_pipeline.py#L49) | 49 | `""` | — |
| [SRC-29A9CD43D1-L000050](../../tests/test_dialogue_context_pipeline.py#L50) | 50 | `"def _semantic_context(*, needs_clarification: bool = False) -> dict[str, Any]:"` | — |
| [SRC-29A9CD43D1-L000051](../../tests/test_dialogue_context_pipeline.py#L51) | 51 | `"    return {"` | — |
| [SRC-29A9CD43D1-L000052](../../tests/test_dialogue_context_pipeline.py#L52) | 52 | `"        \"resolved_question\": ("` | — |
| [SRC-29A9CD43D1-L000053](../../tests/test_dialogue_context_pipeline.py#L53) | 53 | `"            \"هل الضمان الدولي لهاتف iPhone 17 سعة 256 جيجابايت الذي اشتريته \""` | — |
| [SRC-29A9CD43D1-L000054](../../tests/test_dialogue_context_pipeline.py#L54) | 54 | `"            \"في مصر يغطي الصيانة داخل مصر؟\""` | — |
| [SRC-29A9CD43D1-L000055](../../tests/test_dialogue_context_pipeline.py#L55) | 55 | `"        ),"` | — |
| [SRC-29A9CD43D1-L000056](../../tests/test_dialogue_context_pipeline.py#L56) | 56 | `"        \"intent\": \"current_information\","` | — |
| [SRC-29A9CD43D1-L000057](../../tests/test_dialogue_context_pipeline.py#L57) | 57 | `"        \"topic\": \"تغطية الضمان\","` | — |
| [SRC-29A9CD43D1-L000058](../../tests/test_dialogue_context_pipeline.py#L58) | 58 | `"        \"entities\": [\"iPhone 17\"],"` | — |
| [SRC-29A9CD43D1-L000059](../../tests/test_dialogue_context_pipeline.py#L59) | 59 | `"        \"slots\": {"` | — |
| [SRC-29A9CD43D1-L000060](../../tests/test_dialogue_context_pipeline.py#L60) | 60 | `"            \"product\": \"iPhone 17\","` | — |
| [SRC-29A9CD43D1-L000061](../../tests/test_dialogue_context_pipeline.py#L61) | 61 | `"            \"capacity\": \"256 جيجابايت\","` | — |
| [SRC-29A9CD43D1-L000062](../../tests/test_dialogue_context_pipeline.py#L62) | 62 | `"            \"country\": \"مصر\","` | — |
| [SRC-29A9CD43D1-L000063](../../tests/test_dialogue_context_pipeline.py#L63) | 63 | `"            \"aspect\": \"الضمان الدولي والصيانة داخل مصر\","` | — |
| [SRC-29A9CD43D1-L000064](../../tests/test_dialogue_context_pipeline.py#L64) | 64 | `"        },"` | — |
| [SRC-29A9CD43D1-L000065](../../tests/test_dialogue_context_pipeline.py#L65) | 65 | `"        \"changed_slots\": [\"aspect\"],"` | — |
| [SRC-29A9CD43D1-L000066](../../tests/test_dialogue_context_pipeline.py#L66) | 66 | `"        \"is_follow_up\": True,"` | — |
| [SRC-29A9CD43D1-L000067](../../tests/test_dialogue_context_pipeline.py#L67) | 67 | `"        \"topic_shift\": False,"` | — |
| [SRC-29A9CD43D1-L000068](../../tests/test_dialogue_context_pipeline.py#L68) | 68 | `"        \"needs_web\": True,"` | — |
| [SRC-29A9CD43D1-L000069](../../tests/test_dialogue_context_pipeline.py#L69) | 69 | `"        \"research_depth\": \"standard\","` | — |
| [SRC-29A9CD43D1-L000070](../../tests/test_dialogue_context_pipeline.py#L70) | 70 | `"        \"needs_clarification\": needs_clarification,"` | — |
| [SRC-29A9CD43D1-L000071](../../tests/test_dialogue_context_pipeline.py#L71) | 71 | `"        \"clarification_question\": ("` | — |
| [SRC-29A9CD43D1-L000072](../../tests/test_dialogue_context_pipeline.py#L72) | 72 | `"            \"تقصد ضمان أي هاتف تحديدًا، أم تريد مقارنة ضمان الهاتفين؟\""` | — |
| [SRC-29A9CD43D1-L000073](../../tests/test_dialogue_context_pipeline.py#L73) | 73 | `"            if needs_clarification else \"\""` | — |
| [SRC-29A9CD43D1-L000074](../../tests/test_dialogue_context_pipeline.py#L74) | 74 | `"        ),"` | — |
| [SRC-29A9CD43D1-L000075](../../tests/test_dialogue_context_pipeline.py#L75) | 75 | `"        \"unresolved_references\": [\"الضمان\"] if needs_clarification else [],"` | — |
| [SRC-29A9CD43D1-L000076](../../tests/test_dialogue_context_pipeline.py#L76) | 76 | `"        \"resolution_basis\": \"history_inferred\","` | — |
| [SRC-29A9CD43D1-L000077](../../tests/test_dialogue_context_pipeline.py#L77) | 77 | `"        \"confidence_band\": \"medium\","` | — |
| [SRC-29A9CD43D1-L000078](../../tests/test_dialogue_context_pipeline.py#L78) | 78 | `"    }"` | — |
| [SRC-29A9CD43D1-L000079](../../tests/test_dialogue_context_pipeline.py#L79) | 79 | `""` | — |
| [SRC-29A9CD43D1-L000080](../../tests/test_dialogue_context_pipeline.py#L80) | 80 | `""` | — |
| [SRC-29A9CD43D1-L000081](../../tests/test_dialogue_context_pipeline.py#L81) | 81 | `"def test_semantic_context_probe_routes_natural_followup_to_search_and_answer("` | — |
| [SRC-29A9CD43D1-L000082](../../tests/test_dialogue_context_pipeline.py#L82) | 82 | `"    monkeypatch: pytest.MonkeyPatch,"` | — |
| [SRC-29A9CD43D1-L000083](../../tests/test_dialogue_context_pipeline.py#L83) | 83 | `") -> None:"` | — |
| [SRC-29A9CD43D1-L000084](../../tests/test_dialogue_context_pipeline.py#L84) | 84 | `"    agent = WebAgent()"` | — |
| [SRC-29A9CD43D1-L000085](../../tests/test_dialogue_context_pipeline.py#L85) | 85 | `"    agent.api_key = \"test-key\"  # All model responses are mocked; no provider call is made."` | — |
| [SRC-29A9CD43D1-L000086](../../tests/test_dialogue_context_pipeline.py#L86) | 86 | `"    history = ["` | — |
| [SRC-29A9CD43D1-L000087](../../tests/test_dialogue_context_pipeline.py#L87) | 87 | `"        {\"role\": \"user\", \"content\": \"اشتريت iPhone 17 النسخة الأساسية سعة 256 جيجابايت من مصر.\"},"` | — |
| [SRC-29A9CD43D1-L000088](../../tests/test_dialogue_context_pipeline.py#L88) | 88 | `"        {\"role\": \"assistant\", \"content\": \"نتحدث عن نسخة iPhone 17 سعة 256 جيجابايت في مصر.\"},"` | — |
| [SRC-29A9CD43D1-L000089](../../tests/test_dialogue_context_pipeline.py#L89) | 89 | `"    ]"` | — |
| [SRC-29A9CD43D1-L000090](../../tests/test_dialogue_context_pipeline.py#L90) | 90 | `"    context = _semantic_context()"` | — |
| [SRC-29A9CD43D1-L000091](../../tests/test_dialogue_context_pipeline.py#L91) | 91 | `"    seen: dict[str, Any] = {\"model_prompts\": []}"` | — |
| [SRC-29A9CD43D1-L000092](../../tests/test_dialogue_context_pipeline.py#L92) | 92 | `""` | — |
| [SRC-29A9CD43D1-L000093](../../tests/test_dialogue_context_pipeline.py#L93) | 93 | `"    def mocked_completion(messages, **kwargs):"` | — |
| [SRC-29A9CD43D1-L000094](../../tests/test_dialogue_context_pipeline.py#L94) | 94 | `"        system_prompt = messages[0][\"content\"]"` | — |
| [SRC-29A9CD43D1-L000095](../../tests/test_dialogue_context_pipeline.py#L95) | 95 | `"        seen[\"model_prompts\"].append(system_prompt)"` | — |
| [SRC-29A9CD43D1-L000096](../../tests/test_dialogue_context_pipeline.py#L96) | 96 | `"        if \"أنت محلل سياق حواري\" in system_prompt:"` | — |
| [SRC-29A9CD43D1-L000097](../../tests/test_dialogue_context_pipeline.py#L97) | 97 | `"            return json.dumps(context, ensure_ascii=False)"` | — |
| [SRC-29A9CD43D1-L000098](../../tests/test_dialogue_context_pipeline.py#L98) | 98 | `"        if \"أنت مخطط بحث ومحلل دلالي حواري\" in system_prompt:"` | — |
| [SRC-29A9CD43D1-L000099](../../tests/test_dialogue_context_pipeline.py#L99) | 99 | `"            return json.dumps("` | — |
| [SRC-29A9CD43D1-L000100](../../tests/test_dialogue_context_pipeline.py#L100) | 100 | `"                {"` | — |
| [SRC-29A9CD43D1-L000101](../../tests/test_dialogue_context_pipeline.py#L101) | 101 | `"                    \"queries\": ["` | — |
| [SRC-29A9CD43D1-L000102](../../tests/test_dialogue_context_pipeline.py#L102) | 102 | `"                        \"iPhone 17 256GB الضمان الدولي في مصر تغطية الصيانة warranty Egypt\""` | — |
| [SRC-29A9CD43D1-L000103](../../tests/test_dialogue_context_pipeline.py#L103) | 103 | `"                    ],"` | — |
| [SRC-29A9CD43D1-L000104](../../tests/test_dialogue_context_pipeline.py#L104) | 104 | `"                    \"direct_urls\": [],"` | — |
| [SRC-29A9CD43D1-L000105](../../tests/test_dialogue_context_pipeline.py#L105) | 105 | `"                    \"social_focus\": False,"` | — |
| [SRC-29A9CD43D1-L000106](../../tests/test_dialogue_context_pipeline.py#L106) | 106 | `"                    \"freshness\": \"current\","` | — |
| [SRC-29A9CD43D1-L000107](../../tests/test_dialogue_context_pipeline.py#L107) | 107 | `"                    \"depth\": \"standard\","` | — |
| [SRC-29A9CD43D1-L000108](../../tests/test_dialogue_context_pipeline.py#L108) | 108 | `"                    \"platforms\": [],"` | — |
| [SRC-29A9CD43D1-L000109](../../tests/test_dialogue_context_pipeline.py#L109) | 109 | `"                    \"dialogue_context\": context,"` | — |
| [SRC-29A9CD43D1-L000110](../../tests/test_dialogue_context_pipeline.py#L110) | 110 | `"                },"` | — |
| [SRC-29A9CD43D1-L000111](../../tests/test_dialogue_context_pipeline.py#L111) | 111 | `"                ensure_ascii=False,"` | — |
| [SRC-29A9CD43D1-L000112](../../tests/test_dialogue_context_pipeline.py#L112) | 112 | `"            )"` | — |
| [SRC-29A9CD43D1-L000113](../../tests/test_dialogue_context_pipeline.py#L113) | 113 | `"        pytest.fail(\"Unexpected model prompt in mocked offline test\")"` | — |
| [SRC-29A9CD43D1-L000114](../../tests/test_dialogue_context_pipeline.py#L114) | 114 | `""` | — |
| [SRC-29A9CD43D1-L000115](../../tests/test_dialogue_context_pipeline.py#L115) | 115 | `"    monkeypatch.setattr(agent, \"_request_completion\", mocked_completion)"` | — |
| [SRC-29A9CD43D1-L000116](../../tests/test_dialogue_context_pipeline.py#L116) | 116 | `"    seen[\"generated_question\"] = None"` | — |
| [SRC-29A9CD43D1-L000117](../../tests/test_dialogue_context_pipeline.py#L117) | 117 | `"    seen[\"reviewed_question\"] = None"` | — |
| [SRC-29A9CD43D1-L000118](../../tests/test_dialogue_context_pipeline.py#L118) | 118 | `""` | — |
| [SRC-29A9CD43D1-L000119](../../tests/test_dialogue_context_pipeline.py#L119) | 119 | `"    def collect(plan):"` | — |
| [SRC-29A9CD43D1-L000120](../../tests/test_dialogue_context_pipeline.py#L120) | 120 | `"        seen[\"plan\"] = dict(plan)"` | — |
| [SRC-29A9CD43D1-L000121](../../tests/test_dialogue_context_pipeline.py#L121) | 121 | `"        sources = [_source(\"example.com\", plan[\"queries\"]), _source(\"example.net\", plan[\"queries\"])]"` | — |
| [SRC-29A9CD43D1-L000122](../../tests/test_dialogue_context_pipeline.py#L122) | 122 | `"        return sources, [], _report(plan, sources)"` | — |
| [SRC-29A9CD43D1-L000123](../../tests/test_dialogue_context_pipeline.py#L123) | 123 | `""` | — |
| [SRC-29A9CD43D1-L000124](../../tests/test_dialogue_context_pipeline.py#L124) | 124 | `"    def generate(resolved_question, *args, **kwargs):"` | — |
| [SRC-29A9CD43D1-L000125](../../tests/test_dialogue_context_pipeline.py#L125) | 125 | `"        seen[\"generated_question\"] = resolved_question"` | — |
| [SRC-29A9CD43D1-L000126](../../tests/test_dialogue_context_pipeline.py#L126) | 126 | `"        return \"لم أؤكد شروط الضمان من النصوص المتاحة؛ راجع الشروط الرسمية [المصدر 1].\""` | — |
| [SRC-29A9CD43D1-L000127](../../tests/test_dialogue_context_pipeline.py#L127) | 127 | `""` | — |
| [SRC-29A9CD43D1-L000128](../../tests/test_dialogue_context_pipeline.py#L128) | 128 | `"    def review(resolved_question, answer, sources):"` | — |
| [SRC-29A9CD43D1-L000129](../../tests/test_dialogue_context_pipeline.py#L129) | 129 | `"        seen[\"reviewed_question\"] = resolved_question"` | — |
| [SRC-29A9CD43D1-L000130](../../tests/test_dialogue_context_pipeline.py#L130) | 130 | `"        return answer"` | — |
| [SRC-29A9CD43D1-L000131](../../tests/test_dialogue_context_pipeline.py#L131) | 131 | `""` | — |
| [SRC-29A9CD43D1-L000132](../../tests/test_dialogue_context_pipeline.py#L132) | 132 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-29A9CD43D1-L000133](../../tests/test_dialogue_context_pipeline.py#L133) | 133 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda _query, _source: True)"` | — |
| [SRC-29A9CD43D1-L000134](../../tests/test_dialogue_context_pipeline.py#L134) | 134 | `"    monkeypatch.setattr(agent, \"_generate\", generate)"` | — |
| [SRC-29A9CD43D1-L000135](../../tests/test_dialogue_context_pipeline.py#L135) | 135 | `"    monkeypatch.setattr(agent, \"_review_answer\", review)"` | — |
| [SRC-29A9CD43D1-L000136](../../tests/test_dialogue_context_pipeline.py#L136) | 136 | `""` | — |
| [SRC-29A9CD43D1-L000137](../../tests/test_dialogue_context_pipeline.py#L137) | 137 | `"    question = \"وطب الضمان الدولي بيسري في مصر؟\""` | — |
| [SRC-29A9CD43D1-L000138](../../tests/test_dialogue_context_pipeline.py#L138) | 138 | `"    result = agent.answer(question, history=history)"` | — |
| [SRC-29A9CD43D1-L000139](../../tests/test_dialogue_context_pipeline.py#L139) | 139 | `""` | — |
| [SRC-29A9CD43D1-L000140](../../tests/test_dialogue_context_pipeline.py#L140) | 140 | `"    assert result[\"intent_route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-29A9CD43D1-L000141](../../tests/test_dialogue_context_pipeline.py#L141) | 141 | `"    assert result[\"question\"] == question  # Preserve the visible user utterance."` | — |
| [SRC-29A9CD43D1-L000142](../../tests/test_dialogue_context_pipeline.py#L142) | 142 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-29A9CD43D1-L000143](../../tests/test_dialogue_context_pipeline.py#L143) | 143 | `"    assert len(seen[\"model_prompts\"]) == 2  # one context pass + one search-plan pass"` | — |
| [SRC-29A9CD43D1-L000144](../../tests/test_dialogue_context_pipeline.py#L144) | 144 | `"    assert \"iPhone 17\" in seen[\"generated_question\"]"` | — |
| [SRC-29A9CD43D1-L000145](../../tests/test_dialogue_context_pipeline.py#L145) | 145 | `"    assert \"256 جيجابايت\" in seen[\"generated_question\"]"` | — |
| [SRC-29A9CD43D1-L000146](../../tests/test_dialogue_context_pipeline.py#L146) | 146 | `"    assert \"الضمان الدولي\" in seen[\"generated_question\"]"` | — |
| [SRC-29A9CD43D1-L000147](../../tests/test_dialogue_context_pipeline.py#L147) | 147 | `"    assert seen[\"reviewed_question\"] == seen[\"generated_question\"]"` | — |
| [SRC-29A9CD43D1-L000148](../../tests/test_dialogue_context_pipeline.py#L148) | 148 | `"    context_result = result[\"research_plan\"][\"dialogue_context\"]"` | — |
| [SRC-29A9CD43D1-L000149](../../tests/test_dialogue_context_pipeline.py#L149) | 149 | `"    assert context_result[\"method\"] == \"llm_semantic_context\""` | — |
| [SRC-29A9CD43D1-L000150](../../tests/test_dialogue_context_pipeline.py#L150) | 150 | `"    assert context_result[\"slots\"][\"country\"] == \"مصر\""` | — |
| [SRC-29A9CD43D1-L000151](../../tests/test_dialogue_context_pipeline.py#L151) | 151 | `"    assert context_result[\"changed_slots\"] == [\"aspect\"]"` | — |
| [SRC-29A9CD43D1-L000152](../../tests/test_dialogue_context_pipeline.py#L152) | 152 | `"    assert context_result[\"needs_web\"] is True"` | — |
| [SRC-29A9CD43D1-L000153](../../tests/test_dialogue_context_pipeline.py#L153) | 153 | `""` | — |
| [SRC-29A9CD43D1-L000154](../../tests/test_dialogue_context_pipeline.py#L154) | 154 | `""` | — |
| [SRC-29A9CD43D1-L000155](../../tests/test_dialogue_context_pipeline.py#L155) | 155 | `"def test_semantic_context_asks_before_search_when_two_referents_are_plausible("` | — |
| [SRC-29A9CD43D1-L000156](../../tests/test_dialogue_context_pipeline.py#L156) | 156 | `"    monkeypatch: pytest.MonkeyPatch,"` | — |
| [SRC-29A9CD43D1-L000157](../../tests/test_dialogue_context_pipeline.py#L157) | 157 | `") -> None:"` | — |
| [SRC-29A9CD43D1-L000158](../../tests/test_dialogue_context_pipeline.py#L158) | 158 | `"    agent = WebAgent()"` | — |
| [SRC-29A9CD43D1-L000159](../../tests/test_dialogue_context_pipeline.py#L159) | 159 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-29A9CD43D1-L000160](../../tests/test_dialogue_context_pipeline.py#L160) | 160 | `"    history = ["` | — |
| [SRC-29A9CD43D1-L000161](../../tests/test_dialogue_context_pipeline.py#L161) | 161 | `"        {\"role\": \"user\", \"content\": \"قارن بين iPhone 17 وSamsung S26\"},"` | — |
| [SRC-29A9CD43D1-L000162](../../tests/test_dialogue_context_pipeline.py#L162) | 162 | `"        {\"role\": \"assistant\", \"content\": \"ذكرت الهاتفين في المقارنة.\"},"` | — |
| [SRC-29A9CD43D1-L000163](../../tests/test_dialogue_context_pipeline.py#L163) | 163 | `"    ]"` | — |
| [SRC-29A9CD43D1-L000164](../../tests/test_dialogue_context_pipeline.py#L164) | 164 | `"    ambiguous = {"` | — |
| [SRC-29A9CD43D1-L000165](../../tests/test_dialogue_context_pipeline.py#L165) | 165 | `"        \"resolved_question\": \"What about the second one?\","` | — |
| [SRC-29A9CD43D1-L000166](../../tests/test_dialogue_context_pipeline.py#L166) | 166 | `"        \"intent\": \"compare\","` | — |
| [SRC-29A9CD43D1-L000167](../../tests/test_dialogue_context_pipeline.py#L167) | 167 | `"        \"topic\": \"اختيار الهاتف\","` | — |
| [SRC-29A9CD43D1-L000168](../../tests/test_dialogue_context_pipeline.py#L168) | 168 | `"        \"entities\": [\"iPhone 17\", \"Samsung S26\"],"` | — |
| [SRC-29A9CD43D1-L000169](../../tests/test_dialogue_context_pipeline.py#L169) | 169 | `"        \"slots\": {\"aspect\": \"الاختيار\"},"` | — |
| [SRC-29A9CD43D1-L000170](../../tests/test_dialogue_context_pipeline.py#L170) | 170 | `"        \"changed_slots\": [],"` | — |
| [SRC-29A9CD43D1-L000171](../../tests/test_dialogue_context_pipeline.py#L171) | 171 | `"        \"is_follow_up\": True,"` | — |
| [SRC-29A9CD43D1-L000172](../../tests/test_dialogue_context_pipeline.py#L172) | 172 | `"        \"topic_shift\": False,"` | — |
| [SRC-29A9CD43D1-L000173](../../tests/test_dialogue_context_pipeline.py#L173) | 173 | `"        \"needs_web\": False,"` | — |
| [SRC-29A9CD43D1-L000174](../../tests/test_dialogue_context_pipeline.py#L174) | 174 | `"        \"research_depth\": \"standard\","` | — |
| [SRC-29A9CD43D1-L000175](../../tests/test_dialogue_context_pipeline.py#L175) | 175 | `"        \"needs_clarification\": True,"` | — |
| [SRC-29A9CD43D1-L000176](../../tests/test_dialogue_context_pipeline.py#L176) | 176 | `"        \"clarification_question\": \"تقصد أي هاتف تحديدًا: iPhone 17 أم Samsung S26؟\","` | — |
| [SRC-29A9CD43D1-L000177](../../tests/test_dialogue_context_pipeline.py#L177) | 177 | `"        \"unresolved_references\": [\"the second one\"],"` | — |
| [SRC-29A9CD43D1-L000178](../../tests/test_dialogue_context_pipeline.py#L178) | 178 | `"        \"resolution_basis\": \"insufficient_evidence\","` | — |
| [SRC-29A9CD43D1-L000179](../../tests/test_dialogue_context_pipeline.py#L179) | 179 | `"        \"confidence_band\": \"low\","` | — |
| [SRC-29A9CD43D1-L000180](../../tests/test_dialogue_context_pipeline.py#L180) | 180 | `"    }"` | — |
| [SRC-29A9CD43D1-L000181](../../tests/test_dialogue_context_pipeline.py#L181) | 181 | `""` | — |
| [SRC-29A9CD43D1-L000182](../../tests/test_dialogue_context_pipeline.py#L182) | 182 | `"    def mocked_completion(messages, **kwargs):"` | — |
| [SRC-29A9CD43D1-L000183](../../tests/test_dialogue_context_pipeline.py#L183) | 183 | `"        assert \"أنت محلل سياق حواري\" in messages[0][\"content\"]"` | — |
| [SRC-29A9CD43D1-L000184](../../tests/test_dialogue_context_pipeline.py#L184) | 184 | `"        return json.dumps(ambiguous, ensure_ascii=False)"` | — |
| [SRC-29A9CD43D1-L000185](../../tests/test_dialogue_context_pipeline.py#L185) | 185 | `""` | — |
| [SRC-29A9CD43D1-L000186](../../tests/test_dialogue_context_pipeline.py#L186) | 186 | `"    def forbidden_search(*args, **kwargs):"` | — |
| [SRC-29A9CD43D1-L000187](../../tests/test_dialogue_context_pipeline.py#L187) | 187 | `"        pytest.fail(\"An unresolved referent must not start web research.\")"` | — |
| [SRC-29A9CD43D1-L000188](../../tests/test_dialogue_context_pipeline.py#L188) | 188 | `""` | — |
| [SRC-29A9CD43D1-L000189](../../tests/test_dialogue_context_pipeline.py#L189) | 189 | `"    monkeypatch.setattr(agent, \"_request_completion\", mocked_completion)"` | — |
| [SRC-29A9CD43D1-L000190](../../tests/test_dialogue_context_pipeline.py#L190) | 190 | `"    monkeypatch.setattr(agent, \"_collect_research\", forbidden_search)"` | — |
| [SRC-29A9CD43D1-L000191](../../tests/test_dialogue_context_pipeline.py#L191) | 191 | `""` | — |
| [SRC-29A9CD43D1-L000192](../../tests/test_dialogue_context_pipeline.py#L192) | 192 | `"    result = agent.answer(\"What about the second one?\", history=history)"` | — |
| [SRC-29A9CD43D1-L000193](../../tests/test_dialogue_context_pipeline.py#L193) | 193 | `""` | — |
| [SRC-29A9CD43D1-L000194](../../tests/test_dialogue_context_pipeline.py#L194) | 194 | `"    assert result[\"kind\"] == \"clarification_needed\""` | — |
| [SRC-29A9CD43D1-L000195](../../tests/test_dialogue_context_pipeline.py#L195) | 195 | `"    assert result[\"intent_route\"] == \"CLARIFY\""` | — |
| [SRC-29A9CD43D1-L000196](../../tests/test_dialogue_context_pipeline.py#L196) | 196 | `"    assert \"iPhone 17\" in result[\"answer\"]"` | — |
| [SRC-29A9CD43D1-L000197](../../tests/test_dialogue_context_pipeline.py#L197) | 197 | `"    assert \"Samsung S26\" in result[\"answer\"]"` | — |
| [SRC-29A9CD43D1-L000198](../../tests/test_dialogue_context_pipeline.py#L198) | 198 | `"    assert result[\"dialogue_context\"][\"needs_clarification\"] is True"` | — |
| [SRC-29A9CD43D1-L000199](../../tests/test_dialogue_context_pipeline.py#L199) | 199 | `"    assert result[\"used_web_search\"] is False"` | — |
| [SRC-29A9CD43D1-L000200](../../tests/test_dialogue_context_pipeline.py#L200) | 200 | `""` | — |
| [SRC-29A9CD43D1-L000201](../../tests/test_dialogue_context_pipeline.py#L201) | 201 | `"def test_semantic_probe_catches_implicit_context_without_keyword_trigger("` | — |
| [SRC-29A9CD43D1-L000202](../../tests/test_dialogue_context_pipeline.py#L202) | 202 | `"    monkeypatch: pytest.MonkeyPatch,"` | — |
| [SRC-29A9CD43D1-L000203](../../tests/test_dialogue_context_pipeline.py#L203) | 203 | `") -> None:"` | — |
| [SRC-29A9CD43D1-L000204](../../tests/test_dialogue_context_pipeline.py#L204) | 204 | `"    agent = WebAgent()"` | — |
| [SRC-29A9CD43D1-L000205](../../tests/test_dialogue_context_pipeline.py#L205) | 205 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-29A9CD43D1-L000206](../../tests/test_dialogue_context_pipeline.py#L206) | 206 | `"    question = \"في وضعي، أبدأ بإيه؟\""` | — |
| [SRC-29A9CD43D1-L000207](../../tests/test_dialogue_context_pipeline.py#L207) | 207 | `"    history = ["` | — |
| [SRC-29A9CD43D1-L000208](../../tests/test_dialogue_context_pipeline.py#L208) | 208 | `"        {"` | — |
| [SRC-29A9CD43D1-L000209](../../tests/test_dialogue_context_pipeline.py#L209) | 209 | `"            \"role\": \"user\","` | — |
| [SRC-29A9CD43D1-L000210](../../tests/test_dialogue_context_pipeline.py#L210) | 210 | `"            \"content\": ("` | — |
| [SRC-29A9CD43D1-L000211](../../tests/test_dialogue_context_pipeline.py#L211) | 211 | `"                \"عندي امتحان كيمياء بكرة، وفاضلي ساعتين أراجع الاتزان الكيميائي \""` | — |
| [SRC-29A9CD43D1-L000212](../../tests/test_dialogue_context_pipeline.py#L212) | 212 | `"                \"ومش فاهمه كويس.\""` | — |
| [SRC-29A9CD43D1-L000213](../../tests/test_dialogue_context_pipeline.py#L213) | 213 | `"            ),"` | — |
| [SRC-29A9CD43D1-L000214](../../tests/test_dialogue_context_pipeline.py#L214) | 214 | `"        },"` | — |
| [SRC-29A9CD43D1-L000215](../../tests/test_dialogue_context_pipeline.py#L215) | 215 | `"        {"` | — |
| [SRC-29A9CD43D1-L000216](../../tests/test_dialogue_context_pipeline.py#L216) | 216 | `"            \"role\": \"assistant\","` | — |
| [SRC-29A9CD43D1-L000217](../../tests/test_dialogue_context_pipeline.py#L217) | 217 | `"            \"content\": \"نقدر نرتب الساعتين لمراجعة المفاهيم والتدريب على المسائل.\","` | — |
| [SRC-29A9CD43D1-L000218](../../tests/test_dialogue_context_pipeline.py#L218) | 218 | `"        },"` | — |
| [SRC-29A9CD43D1-L000219](../../tests/test_dialogue_context_pipeline.py#L219) | 219 | `"    ]"` | — |
| [SRC-29A9CD43D1-L000220](../../tests/test_dialogue_context_pipeline.py#L220) | 220 | `"    assert not might_be_context_dependent(question)"` | — |
| [SRC-29A9CD43D1-L000221](../../tests/test_dialogue_context_pipeline.py#L221) | 221 | `""` | — |
| [SRC-29A9CD43D1-L000222](../../tests/test_dialogue_context_pipeline.py#L222) | 222 | `"    semantic_context = {"` | — |
| [SRC-29A9CD43D1-L000223](../../tests/test_dialogue_context_pipeline.py#L223) | 223 | `"        \"resolved_question\": ("` | — |
| [SRC-29A9CD43D1-L000224](../../tests/test_dialogue_context_pipeline.py#L224) | 224 | `"            \"في ظل امتحان الكيمياء غدًا ووجود ساعتين لمراجعة الاتزان الكيميائي، \""` | — |
| [SRC-29A9CD43D1-L000225](../../tests/test_dialogue_context_pipeline.py#L225) | 225 | `"            \"بماذا أبدأ؟\""` | — |
| [SRC-29A9CD43D1-L000226](../../tests/test_dialogue_context_pipeline.py#L226) | 226 | `"        ),"` | — |
| [SRC-29A9CD43D1-L000227](../../tests/test_dialogue_context_pipeline.py#L227) | 227 | `"        \"intent\": \"how_to\","` | — |
| [SRC-29A9CD43D1-L000228](../../tests/test_dialogue_context_pipeline.py#L228) | 228 | `"        \"topic\": \"خطة مراجعة الاتزان الكيميائي\","` | — |
| [SRC-29A9CD43D1-L000229](../../tests/test_dialogue_context_pipeline.py#L229) | 229 | `"        \"entities\": [\"امتحان الكيمياء\", \"الاتزان الكيميائي\"],"` | — |
| [SRC-29A9CD43D1-L000230](../../tests/test_dialogue_context_pipeline.py#L230) | 230 | `"        \"slots\": {"` | — |
| [SRC-29A9CD43D1-L000231](../../tests/test_dialogue_context_pipeline.py#L231) | 231 | `"            \"goal\": \"مراجعة امتحان الكيمياء\","` | — |
| [SRC-29A9CD43D1-L000232](../../tests/test_dialogue_context_pipeline.py#L232) | 232 | `"            \"time_range\": \"ساعتان\","` | — |
| [SRC-29A9CD43D1-L000233](../../tests/test_dialogue_context_pipeline.py#L233) | 233 | `"            \"topic\": \"الاتزان الكيميائي\","` | — |
| [SRC-29A9CD43D1-L000234](../../tests/test_dialogue_context_pipeline.py#L234) | 234 | `"        },"` | — |
| [SRC-29A9CD43D1-L000235](../../tests/test_dialogue_context_pipeline.py#L235) | 235 | `"        \"changed_slots\": [\"goal\"],"` | — |
| [SRC-29A9CD43D1-L000236](../../tests/test_dialogue_context_pipeline.py#L236) | 236 | `"        \"is_follow_up\": True,"` | — |
| [SRC-29A9CD43D1-L000237](../../tests/test_dialogue_context_pipeline.py#L237) | 237 | `"        \"topic_shift\": False,"` | — |
| [SRC-29A9CD43D1-L000238](../../tests/test_dialogue_context_pipeline.py#L238) | 238 | `"        \"needs_web\": False,"` | — |
| [SRC-29A9CD43D1-L000239](../../tests/test_dialogue_context_pipeline.py#L239) | 239 | `"        \"research_depth\": \"standard\","` | — |
| [SRC-29A9CD43D1-L000240](../../tests/test_dialogue_context_pipeline.py#L240) | 240 | `"        \"needs_clarification\": False,"` | — |
| [SRC-29A9CD43D1-L000241](../../tests/test_dialogue_context_pipeline.py#L241) | 241 | `"        \"clarification_question\": \"\","` | — |
| [SRC-29A9CD43D1-L000242](../../tests/test_dialogue_context_pipeline.py#L242) | 242 | `"        \"unresolved_references\": [],"` | — |
| [SRC-29A9CD43D1-L000243](../../tests/test_dialogue_context_pipeline.py#L243) | 243 | `"        \"resolution_basis\": \"history_inferred\","` | — |
