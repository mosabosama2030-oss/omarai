# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **042**
- سجلات الأسطر: **800**
- النطاق: SRC-1C0D3D1206-L000044 إلى SRC-F725E90B2A-L000198
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-1C0D3D1206 — [tests/test_sqlite_backup_restore.py](../../tests/test_sqlite_backup_restore.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1C0D3D1206-L000044](../../tests/test_sqlite_backup_restore.py#L44) | 44 | `"    restored_rows = {row[\"id\"]: row for row in restored.list(limit=500)}"` | — |
| [SRC-1C0D3D1206-L000045](../../tests/test_sqlite_backup_restore.py#L45) | 45 | `"    assert restored_rows == original_rows"` | — |
| [SRC-1C0D3D1206-L000046](../../tests/test_sqlite_backup_restore.py#L46) | 46 | `"    assert restored_rows[first[\"id\"]][\"status\"] == \"qualified\""` | — |
| [SRC-1C0D3D1206-L000047](../../tests/test_sqlite_backup_restore.py#L47) | 47 | `"    assert second[\"id\"] in restored_rows"` | — |
| [SRC-1C0D3D1206-L000048](../../tests/test_sqlite_backup_restore.py#L48) | 48 | `""` | — |
| [SRC-1C0D3D1206-L000049](../../tests/test_sqlite_backup_restore.py#L49) | 49 | `""` | — |
| [SRC-1C0D3D1206-L000050](../../tests/test_sqlite_backup_restore.py#L50) | 50 | `"def test_backup_never_overwrites_an_existing_destination(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000051](../../tests/test_sqlite_backup_restore.py#L51) | 51 | `"    source_path = tmp_path / \"source.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000052](../../tests/test_sqlite_backup_restore.py#L52) | 52 | `"    LeadStore(source_path)"` | — |
| [SRC-1C0D3D1206-L000053](../../tests/test_sqlite_backup_restore.py#L53) | 53 | `"    destination = tmp_path / \"keep-me.txt\""` | — |
| [SRC-1C0D3D1206-L000054](../../tests/test_sqlite_backup_restore.py#L54) | 54 | `"    destination.write_text(\"do not overwrite\", encoding=\"utf-8\")"` | — |
| [SRC-1C0D3D1206-L000055](../../tests/test_sqlite_backup_restore.py#L55) | 55 | `""` | — |
| [SRC-1C0D3D1206-L000056](../../tests/test_sqlite_backup_restore.py#L56) | 56 | `"    with pytest.raises(FileExistsError):"` | — |
| [SRC-1C0D3D1206-L000057](../../tests/test_sqlite_backup_restore.py#L57) | 57 | `"        backup_database(source_path, destination)"` | — |
| [SRC-1C0D3D1206-L000058](../../tests/test_sqlite_backup_restore.py#L58) | 58 | `""` | — |
| [SRC-1C0D3D1206-L000059](../../tests/test_sqlite_backup_restore.py#L59) | 59 | `"    assert destination.read_text(encoding=\"utf-8\") == \"do not overwrite\""` | — |
| [SRC-1C0D3D1206-L000060](../../tests/test_sqlite_backup_restore.py#L60) | 60 | `""` | — |
| [SRC-1C0D3D1206-L000061](../../tests/test_sqlite_backup_restore.py#L61) | 61 | `""` | — |
| [SRC-1C0D3D1206-L000062](../../tests/test_sqlite_backup_restore.py#L62) | 62 | `"def test_backup_rejects_non_omarai_sqlite_database_without_leaving_destination(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000063](../../tests/test_sqlite_backup_restore.py#L63) | 63 | `"    source_path = tmp_path / \"unrelated.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000064](../../tests/test_sqlite_backup_restore.py#L64) | 64 | `"    with sqlite3.connect(source_path) as db:"` | — |
| [SRC-1C0D3D1206-L000065](../../tests/test_sqlite_backup_restore.py#L65) | 65 | `"        db.execute(\"CREATE TABLE unrelated (value TEXT)\")"` | — |
| [SRC-1C0D3D1206-L000066](../../tests/test_sqlite_backup_restore.py#L66) | 66 | `""` | — |
| [SRC-1C0D3D1206-L000067](../../tests/test_sqlite_backup_restore.py#L67) | 67 | `"    destination = tmp_path / \"should-not-exist.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000068](../../tests/test_sqlite_backup_restore.py#L68) | 68 | `"    with pytest.raises(BackupError, match=\"not an Omarai leads database\"):"` | — |
| [SRC-1C0D3D1206-L000069](../../tests/test_sqlite_backup_restore.py#L69) | 69 | `"        backup_database(source_path, destination)"` | — |
| [SRC-1C0D3D1206-L000070](../../tests/test_sqlite_backup_restore.py#L70) | 70 | `""` | — |
| [SRC-1C0D3D1206-L000071](../../tests/test_sqlite_backup_restore.py#L71) | 71 | `"    assert not destination.exists()"` | — |
| [SRC-1C0D3D1206-L000072](../../tests/test_sqlite_backup_restore.py#L72) | 72 | `""` | — |
| [SRC-1C0D3D1206-L000073](../../tests/test_sqlite_backup_restore.py#L73) | 73 | `""` | — |
| [SRC-1C0D3D1206-L000074](../../tests/test_sqlite_backup_restore.py#L74) | 74 | `"def test_backup_rejects_same_source_and_destination(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000075](../../tests/test_sqlite_backup_restore.py#L75) | 75 | `"    source_path = tmp_path / \"source.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000076](../../tests/test_sqlite_backup_restore.py#L76) | 76 | `"    LeadStore(source_path)"` | — |
| [SRC-1C0D3D1206-L000077](../../tests/test_sqlite_backup_restore.py#L77) | 77 | `""` | — |
| [SRC-1C0D3D1206-L000078](../../tests/test_sqlite_backup_restore.py#L78) | 78 | `"    with pytest.raises(BackupError, match=\"different paths\"):"` | — |
| [SRC-1C0D3D1206-L000079](../../tests/test_sqlite_backup_restore.py#L79) | 79 | `"        backup_database(source_path, source_path)"` | — |
| [SRC-1C0D3D1206-L000080](../../tests/test_sqlite_backup_restore.py#L80) | 80 | `""` | — |
| [SRC-1C0D3D1206-L000081](../../tests/test_sqlite_backup_restore.py#L81) | 81 | `""` | — |
| [SRC-1C0D3D1206-L000082](../../tests/test_sqlite_backup_restore.py#L82) | 82 | `"def test_restore_rejects_corrupt_backup_without_overwriting_source(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000083](../../tests/test_sqlite_backup_restore.py#L83) | 83 | `"    backup_path = tmp_path / \"corrupt.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000084](../../tests/test_sqlite_backup_restore.py#L84) | 84 | `"    backup_path.write_bytes(b\"not a sqlite database\")"` | — |
| [SRC-1C0D3D1206-L000085](../../tests/test_sqlite_backup_restore.py#L85) | 85 | `"    destination = tmp_path / \"restore.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000086](../../tests/test_sqlite_backup_restore.py#L86) | 86 | `""` | — |
| [SRC-1C0D3D1206-L000087](../../tests/test_sqlite_backup_restore.py#L87) | 87 | `"    with pytest.raises(BackupError):"` | — |
| [SRC-1C0D3D1206-L000088](../../tests/test_sqlite_backup_restore.py#L88) | 88 | `"        restore_database(backup_path, destination)"` | — |
| [SRC-1C0D3D1206-L000089](../../tests/test_sqlite_backup_restore.py#L89) | 89 | `""` | — |
| [SRC-1C0D3D1206-L000090](../../tests/test_sqlite_backup_restore.py#L90) | 90 | `"    assert backup_path.read_bytes() == b\"not a sqlite database\""` | — |
| [SRC-1C0D3D1206-L000091](../../tests/test_sqlite_backup_restore.py#L91) | 91 | `"    assert not destination.exists()"` | — |
| [SRC-1C0D3D1206-L000092](../../tests/test_sqlite_backup_restore.py#L92) | 92 | `""` | — |
| [SRC-1C0D3D1206-L000093](../../tests/test_sqlite_backup_restore.py#L93) | 93 | `"def test_backup_rejects_dangling_symlink_destination(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000094](../../tests/test_sqlite_backup_restore.py#L94) | 94 | `"    source_path = tmp_path / \"source.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000095](../../tests/test_sqlite_backup_restore.py#L95) | 95 | `"    LeadStore(source_path)"` | — |
| [SRC-1C0D3D1206-L000096](../../tests/test_sqlite_backup_restore.py#L96) | 96 | `"    target_path = tmp_path / \"target.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000097](../../tests/test_sqlite_backup_restore.py#L97) | 97 | `"    destination_link = tmp_path / \"backup-link.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000098](../../tests/test_sqlite_backup_restore.py#L98) | 98 | `"    destination_link.symlink_to(target_path)"` | — |
| [SRC-1C0D3D1206-L000099](../../tests/test_sqlite_backup_restore.py#L99) | 99 | `""` | — |
| [SRC-1C0D3D1206-L000100](../../tests/test_sqlite_backup_restore.py#L100) | 100 | `"    with pytest.raises(FileExistsError):"` | — |
| [SRC-1C0D3D1206-L000101](../../tests/test_sqlite_backup_restore.py#L101) | 101 | `"        backup_database(source_path, destination_link)"` | — |
| [SRC-1C0D3D1206-L000102](../../tests/test_sqlite_backup_restore.py#L102) | 102 | `""` | — |
| [SRC-1C0D3D1206-L000103](../../tests/test_sqlite_backup_restore.py#L103) | 103 | `"    assert destination_link.is_symlink()"` | — |
| [SRC-1C0D3D1206-L000104](../../tests/test_sqlite_backup_restore.py#L104) | 104 | `"    assert not target_path.exists()"` | — |
| [SRC-1C0D3D1206-L000105](../../tests/test_sqlite_backup_restore.py#L105) | 105 | `""` | — |
## اختبارات

### FILE-AFEDC2645A — [tests/test_task_understanding.py](../../tests/test_task_understanding.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-AFEDC2645A-L000001](../../tests/test_task_understanding.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-AFEDC2645A-L000002](../../tests/test_task_understanding.py#L2) | 2 | `""` | — |
| [SRC-AFEDC2645A-L000003](../../tests/test_task_understanding.py#L3) | 3 | `"import pytest"` | — |
| [SRC-AFEDC2645A-L000004](../../tests/test_task_understanding.py#L4) | 4 | `""` | — |
| [SRC-AFEDC2645A-L000005](../../tests/test_task_understanding.py#L5) | 5 | `"from agents.task_understanding import build_query_strategy_matrix, build_task_spec"` | — |
| [SRC-AFEDC2645A-L000006](../../tests/test_task_understanding.py#L6) | 6 | `""` | — |
| [SRC-AFEDC2645A-L000007](../../tests/test_task_understanding.py#L7) | 7 | `""` | — |
| [SRC-AFEDC2645A-L000008](../../tests/test_task_understanding.py#L8) | 8 | `"@pytest.mark.parametrize("` | — |
| [SRC-AFEDC2645A-L000009](../../tests/test_task_understanding.py#L9) | 9 | `"    (\"question\", \"family\"),"` | — |
| [SRC-AFEDC2645A-L000010](../../tests/test_task_understanding.py#L10) | 10 | `"    ["` | — |
| [SRC-AFEDC2645A-L000011](../../tests/test_task_understanding.py#L11) | 11 | `"        (\"ابحث عن الموقع الرسمي لوزارة الاتصالات في مصر\", \"official_site_lookup\"),"` | — |
| [SRC-AFEDC2645A-L000012](../../tests/test_task_understanding.py#L12) | 12 | `"        (\"مواعيد عمل مكتب الجوازات اليوم في العباسية\", \"current_information\"),"` | — |
| [SRC-AFEDC2645A-L000013](../../tests/test_task_understanding.py#L13) | 13 | `"        (\"قارن نيسان صني 2022 وهيونداي أكسنت من حيث السعر والصيانة\", \"compare\"),"` | — |
| [SRC-AFEDC2645A-L000014](../../tests/test_task_understanding.py#L14) | 14 | `"        (\"عايز تجارب ملاك BYD Dolphin في مصر\", \"social_opinions\"),"` | — |
| [SRC-AFEDC2645A-L000015](../../tests/test_task_understanding.py#L15) | 15 | `"        (\"ازاي أصلح خطأ الشبكة في لوحة إنذار الحريق؟\", \"troubleshoot\"),"` | — |
| [SRC-AFEDC2645A-L000016](../../tests/test_task_understanding.py#L16) | 16 | `"        (\"اشرح خطوات صيانة حساس الدخان\", \"how_to\"),"` | — |
| [SRC-AFEDC2645A-L000017](../../tests/test_task_understanding.py#L17) | 17 | `"        (\"لخص الصفحة https://example.com/article\", \"summarize\"),"` | — |
| [SRC-AFEDC2645A-L000018](../../tests/test_task_understanding.py#L18) | 18 | `"        (\"ابحث عن مشترين يريدون شراء شقة في القاهرة\", \"lead_generation\"),"` | — |
| [SRC-AFEDC2645A-L000019](../../tests/test_task_understanding.py#L19) | 19 | `"        (\"رشح لي أفضل سيارة بميزانية أقل من 500000 جنيه\", \"recommendation\"),"` | — |
| [SRC-AFEDC2645A-L000020](../../tests/test_task_understanding.py#L20) | 20 | `"        (\"ما معنى نظام الإنذار المعنون؟\", \"explain_or_define\"),"` | — |
| [SRC-AFEDC2645A-L000021](../../tests/test_task_understanding.py#L21) | 21 | `"    ],"` | — |
| [SRC-AFEDC2645A-L000022](../../tests/test_task_understanding.py#L22) | 22 | `")"` | — |
| [SRC-AFEDC2645A-L000023](../../tests/test_task_understanding.py#L23) | 23 | `"def test_task_family_covers_diverse_natural_language_patterns(question, family):"` | — |
| [SRC-AFEDC2645A-L000024](../../tests/test_task_understanding.py#L24) | 24 | `"    spec = build_task_spec(question, mode=\"auto\", intent_route=\"WEB_SIMPLE\")"` | — |
| [SRC-AFEDC2645A-L000025](../../tests/test_task_understanding.py#L25) | 25 | `"    assert spec[\"task_family\"] == family"` | — |
| [SRC-AFEDC2645A-L000026](../../tests/test_task_understanding.py#L26) | 26 | `"    assert spec[\"classification_is_probability\"] is False"` | — |
| [SRC-AFEDC2645A-L000027](../../tests/test_task_understanding.py#L27) | 27 | `"    assert spec[\"decision_checks\"]"` | — |
| [SRC-AFEDC2645A-L000028](../../tests/test_task_understanding.py#L28) | 28 | `""` | — |
| [SRC-AFEDC2645A-L000029](../../tests/test_task_understanding.py#L29) | 29 | `""` | — |
| [SRC-AFEDC2645A-L000030](../../tests/test_task_understanding.py#L30) | 30 | `"def test_task_spec_preserves_only_explicit_constraints():"` | — |
| [SRC-AFEDC2645A-L000031](../../tests/test_task_understanding.py#L31) | 31 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000032](../../tests/test_task_understanding.py#L32) | 32 | `"        \"قارن نيسان صني 2022 مع BYD Dolphin في مصر، بميزانية أقل من 400 ألف جنيه\","` | — |
| [SRC-AFEDC2645A-L000033](../../tests/test_task_understanding.py#L33) | 33 | `"        mode=\"deep\","` | — |
| [SRC-AFEDC2645A-L000034](../../tests/test_task_understanding.py#L34) | 34 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000035](../../tests/test_task_understanding.py#L35) | 35 | `"    )"` | — |
| [SRC-AFEDC2645A-L000036](../../tests/test_task_understanding.py#L36) | 36 | `"    constraints = spec[\"constraints\"]"` | — |
| [SRC-AFEDC2645A-L000037](../../tests/test_task_understanding.py#L37) | 37 | `"    assert \"2022\" in constraints[\"explicit_years\"]"` | — |
| [SRC-AFEDC2645A-L000038](../../tests/test_task_understanding.py#L38) | 38 | `"    assert \"مصر\" in constraints[\"explicit_locations\"]"` | — |
| [SRC-AFEDC2645A-L000039](../../tests/test_task_understanding.py#L39) | 39 | `"    assert constraints[\"explicit_budgets\"]"` | — |
| [SRC-AFEDC2645A-L000040](../../tests/test_task_understanding.py#L40) | 40 | `"    assert constraints[\"language_profile\"] in {\"ar\", \"mixed\"}"` | — |
| [SRC-AFEDC2645A-L000041](../../tests/test_task_understanding.py#L41) | 41 | `""` | — |
| [SRC-AFEDC2645A-L000042](../../tests/test_task_understanding.py#L42) | 42 | `""` | — |
| [SRC-AFEDC2645A-L000043](../../tests/test_task_understanding.py#L43) | 43 | `"def test_latest_mode_requires_current_evidence_for_stateful_facts():"` | — |
| [SRC-AFEDC2645A-L000044](../../tests/test_task_understanding.py#L44) | 44 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000045](../../tests/test_task_understanding.py#L45) | 45 | `"        \"مواعيد عمل مكتب الجوازات اليوم\","` | — |
| [SRC-AFEDC2645A-L000046](../../tests/test_task_understanding.py#L46) | 46 | `"        mode=\"latest\","` | — |
| [SRC-AFEDC2645A-L000047](../../tests/test_task_understanding.py#L47) | 47 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-AFEDC2645A-L000048](../../tests/test_task_understanding.py#L48) | 48 | `"    )"` | — |
| [SRC-AFEDC2645A-L000049](../../tests/test_task_understanding.py#L49) | 49 | `"    assert spec[\"constraints\"][\"time_sensitive_request\"] is True"` | — |
| [SRC-AFEDC2645A-L000050](../../tests/test_task_understanding.py#L50) | 50 | `"    assert \"page_text_successfully_read\" in spec[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000051](../../tests/test_task_understanding.py#L51) | 51 | `"    assert \"date_check\" in spec[\"query_strategies\"]"` | — |
| [SRC-AFEDC2645A-L000052](../../tests/test_task_understanding.py#L52) | 52 | `""` | — |
| [SRC-AFEDC2645A-L000053](../../tests/test_task_understanding.py#L53) | 53 | `""` | — |
| [SRC-AFEDC2645A-L000054](../../tests/test_task_understanding.py#L54) | 54 | `"def test_official_site_navigation_is_not_misclassified_as_current_news():"` | — |
| [SRC-AFEDC2645A-L000055](../../tests/test_task_understanding.py#L55) | 55 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000056](../../tests/test_task_understanding.py#L56) | 56 | `"        \"ابحث عن الموقع الرسمي لوزارة الاتصالات في مصر\","` | — |
| [SRC-AFEDC2645A-L000057](../../tests/test_task_understanding.py#L57) | 57 | `"        mode=\"latest\","` | — |
| [SRC-AFEDC2645A-L000058](../../tests/test_task_understanding.py#L58) | 58 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-AFEDC2645A-L000059](../../tests/test_task_understanding.py#L59) | 59 | `"    )"` | — |
| [SRC-AFEDC2645A-L000060](../../tests/test_task_understanding.py#L60) | 60 | `"    assert spec[\"task_family\"] == \"official_site_lookup\""` | — |
| [SRC-AFEDC2645A-L000061](../../tests/test_task_understanding.py#L61) | 61 | `"    assert spec[\"constraints\"][\"official_site_required\"] is True"` | — |
| [SRC-AFEDC2645A-L000062](../../tests/test_task_understanding.py#L62) | 62 | `"    assert spec[\"constraints\"][\"time_sensitive_request\"] is False"` | — |
| [SRC-AFEDC2645A-L000063](../../tests/test_task_understanding.py#L63) | 63 | `""` | — |
| [SRC-AFEDC2645A-L000064](../../tests/test_task_understanding.py#L64) | 64 | `""` | — |
| [SRC-AFEDC2645A-L000065](../../tests/test_task_understanding.py#L65) | 65 | `"def test_social_request_separates_experience_from_truth_verification():"` | — |
| [SRC-AFEDC2645A-L000066](../../tests/test_task_understanding.py#L66) | 66 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000067](../../tests/test_task_understanding.py#L67) | 67 | `"        \"أريد آراء وتجارب ملاك نيسان صني 2022 في مصر\","` | — |
| [SRC-AFEDC2645A-L000068](../../tests/test_task_understanding.py#L68) | 68 | `"        mode=\"social\","` | — |
| [SRC-AFEDC2645A-L000069](../../tests/test_task_understanding.py#L69) | 69 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000070](../../tests/test_task_understanding.py#L70) | 70 | `"    )"` | — |
| [SRC-AFEDC2645A-L000071](../../tests/test_task_understanding.py#L71) | 71 | `"    assert spec[\"constraints\"][\"social_evidence_requested\"] is True"` | — |
| [SRC-AFEDC2645A-L000072](../../tests/test_task_understanding.py#L72) | 72 | `"    assert \"heuristic_classification_is_not_identity_or_truth_verification\" in spec[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000073](../../tests/test_task_understanding.py#L73) | 73 | `"    assert \"personal_experience\" in spec[\"query_strategies\"]"` | — |
| [SRC-AFEDC2645A-L000074](../../tests/test_task_understanding.py#L74) | 74 | `""` | — |
| [SRC-AFEDC2645A-L000075](../../tests/test_task_understanding.py#L75) | 75 | `""` | — |
| [SRC-AFEDC2645A-L000076](../../tests/test_task_understanding.py#L76) | 76 | `"def test_ambiguous_followup_is_not_reported_as_a_confident_interpretation():"` | — |
| [SRC-AFEDC2645A-L000077](../../tests/test_task_understanding.py#L77) | 77 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000078](../../tests/test_task_understanding.py#L78) | 78 | `"        \"كام سعرها؟\","` | — |
| [SRC-AFEDC2645A-L000079](../../tests/test_task_understanding.py#L79) | 79 | `"        mode=\"auto\","` | — |
| [SRC-AFEDC2645A-L000080](../../tests/test_task_understanding.py#L80) | 80 | `"        intent_route=\"CLARIFY\","` | — |
| [SRC-AFEDC2645A-L000081](../../tests/test_task_understanding.py#L81) | 81 | `"        dialogue_context={\"needs_clarification\": True},"` | — |
| [SRC-AFEDC2645A-L000082](../../tests/test_task_understanding.py#L82) | 82 | `"    )"` | — |
| [SRC-AFEDC2645A-L000083](../../tests/test_task_understanding.py#L83) | 83 | `"    assert spec[\"task_family\"] == \"ambiguous_or_incomplete\""` | — |
| [SRC-AFEDC2645A-L000084](../../tests/test_task_understanding.py#L84) | 84 | `"    assert spec[\"ambiguity_status\"] == \"needs_clarification\""` | — |
| [SRC-AFEDC2645A-L000085](../../tests/test_task_understanding.py#L85) | 85 | `""` | — |
| [SRC-AFEDC2645A-L000086](../../tests/test_task_understanding.py#L86) | 86 | `""` | — |
| [SRC-AFEDC2645A-L000087](../../tests/test_task_understanding.py#L87) | 87 | `"def test_query_strategy_matrix_is_bounded_deduplicated_and_topic_anchored():"` | — |
| [SRC-AFEDC2645A-L000088](../../tests/test_task_understanding.py#L88) | 88 | `"    question = \"قارن السيارات الكهربائية في مصر من حيث السعر والضمان\""` | — |
| [SRC-AFEDC2645A-L000089](../../tests/test_task_understanding.py#L89) | 89 | `"    spec = build_task_spec(question, mode=\"deep\", intent_route=\"WEB_DEEP\")"` | — |
| [SRC-AFEDC2645A-L000090](../../tests/test_task_understanding.py#L90) | 90 | `"    existing = [\"السيارات الكهربائية في مصر\"] + ["` | — |
| [SRC-AFEDC2645A-L000091](../../tests/test_task_understanding.py#L91) | 91 | `"        f\"السيارات الكهربائية في مصر بديل عام {i}\" for i in range(1, 9)"` | — |
| [SRC-AFEDC2645A-L000092](../../tests/test_task_understanding.py#L92) | 92 | `"    ]"` | — |
| [SRC-AFEDC2645A-L000093](../../tests/test_task_understanding.py#L93) | 93 | `"    rows = build_query_strategy_matrix(question, spec, existing, limit=6)"` | — |
| [SRC-AFEDC2645A-L000094](../../tests/test_task_understanding.py#L94) | 94 | `"    queries = [row[\"query\"] for row in rows]"` | — |
| [SRC-AFEDC2645A-L000095](../../tests/test_task_understanding.py#L95) | 95 | `"    assert 1 <= len(queries) <= 6"` | — |
| [SRC-AFEDC2645A-L000096](../../tests/test_task_understanding.py#L96) | 96 | `"    assert len({query.casefold() for query in queries}) == len(queries)"` | — |
| [SRC-AFEDC2645A-L000097](../../tests/test_task_understanding.py#L97) | 97 | `"    assert all(\"السيارات\" in query for query in queries)"` | — |
| [SRC-AFEDC2645A-L000098](../../tests/test_task_understanding.py#L98) | 98 | `"    assert any(row[\"strategy\"] == \"explicit_criterion\" for row in rows)"` | — |
| [SRC-AFEDC2645A-L000099](../../tests/test_task_understanding.py#L99) | 99 | `"    assert any(row[\"strategy\"] == \"primary_specification\" for row in rows)"` | — |
| [SRC-AFEDC2645A-L000100](../../tests/test_task_understanding.py#L100) | 100 | `"    assert sum(row[\"strategy\"] == \"planner_alternative\" for row in rows) <= 1"` | — |
| [SRC-AFEDC2645A-L000101](../../tests/test_task_understanding.py#L101) | 101 | `"    assert all(row[\"rationale\"] for row in rows)"` | — |
| [SRC-AFEDC2645A-L000102](../../tests/test_task_understanding.py#L102) | 102 | `""` | — |
| [SRC-AFEDC2645A-L000103](../../tests/test_task_understanding.py#L103) | 103 | `"def test_strategy_matrix_does_not_create_generic_queries_without_topic():"` | — |
| [SRC-AFEDC2645A-L000104](../../tests/test_task_understanding.py#L104) | 104 | `"    spec = build_task_spec(\"قارنهم\", mode=\"deep\", intent_route=\"CLARIFY\")"` | — |
| [SRC-AFEDC2645A-L000105](../../tests/test_task_understanding.py#L105) | 105 | `"    rows = build_query_strategy_matrix(\"قارنهم\", spec, [], limit=8)"` | — |
| [SRC-AFEDC2645A-L000106](../../tests/test_task_understanding.py#L106) | 106 | `"    assert rows == []"` | — |
| [SRC-AFEDC2645A-L000107](../../tests/test_task_understanding.py#L107) | 107 | `""` | — |
| [SRC-AFEDC2645A-L000108](../../tests/test_task_understanding.py#L108) | 108 | `""` | — |
| [SRC-AFEDC2645A-L000109](../../tests/test_task_understanding.py#L109) | 109 | `"def test_mixed_language_is_supported_and_urls_are_explicit_constraints():"` | — |
| [SRC-AFEDC2645A-L000110](../../tests/test_task_understanding.py#L110) | 110 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000111](../../tests/test_task_understanding.py#L111) | 111 | `"        \"Compare Nissan Sunny 2022 with BYD Dolphin في مصر https://example.com/specs\","` | — |
| [SRC-AFEDC2645A-L000112](../../tests/test_task_understanding.py#L112) | 112 | `"        mode=\"auto\","` | — |
| [SRC-AFEDC2645A-L000113](../../tests/test_task_understanding.py#L113) | 113 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000114](../../tests/test_task_understanding.py#L114) | 114 | `"    )"` | — |
| [SRC-AFEDC2645A-L000115](../../tests/test_task_understanding.py#L115) | 115 | `"    assert spec[\"constraints\"][\"language_profile\"] == \"mixed\""` | — |
| [SRC-AFEDC2645A-L000116](../../tests/test_task_understanding.py#L116) | 116 | `"    assert spec[\"constraints\"][\"explicit_urls\"] == [\"https://example.com/specs\"]"` | — |
| [SRC-AFEDC2645A-L000117](../../tests/test_task_understanding.py#L117) | 117 | `"    assert \"2022\" in spec[\"constraints\"][\"explicit_years\"]"` | — |
| [SRC-AFEDC2645A-L000118](../../tests/test_task_understanding.py#L118) | 118 | `""` | — |
| [SRC-AFEDC2645A-L000119](../../tests/test_task_understanding.py#L119) | 119 | `""` | — |
| [SRC-AFEDC2645A-L000120](../../tests/test_task_understanding.py#L120) | 120 | `"def test_task_spec_validator_does_not_accept_untrusted_arbitrary_objects():"` | — |
| [SRC-AFEDC2645A-L000121](../../tests/test_task_understanding.py#L121) | 121 | `"    from agents.task_understanding import validate_task_spec"` | — |
| [SRC-AFEDC2645A-L000122](../../tests/test_task_understanding.py#L122) | 122 | `""` | — |
| [SRC-AFEDC2645A-L000123](../../tests/test_task_understanding.py#L123) | 123 | `"    invalid = validate_task_spec({\"schema\": \"wrong\", \"tool_requirements\": [\"delete files\"]})"` | — |
| [SRC-AFEDC2645A-L000124](../../tests/test_task_understanding.py#L124) | 124 | `"    assert invalid[\"status\"] == \"not_available\""` | — |
| [SRC-AFEDC2645A-L000125](../../tests/test_task_understanding.py#L125) | 125 | `""` | — |
| [SRC-AFEDC2645A-L000126](../../tests/test_task_understanding.py#L126) | 126 | `""` | — |
| [SRC-AFEDC2645A-L000127](../../tests/test_task_understanding.py#L127) | 127 | `"def test_compound_task_keeps_current_social_and_comparison_requirements_together():"` | — |
| [SRC-AFEDC2645A-L000128](../../tests/test_task_understanding.py#L128) | 128 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000129](../../tests/test_task_understanding.py#L129) | 129 | `"        \"قارن تجارب ملاك نيسان صني 2022 في مصر اليوم من حيث السعر والأعطال\","` | — |
| [SRC-AFEDC2645A-L000130](../../tests/test_task_understanding.py#L130) | 130 | `"        mode=\"social\","` | — |
| [SRC-AFEDC2645A-L000131](../../tests/test_task_understanding.py#L131) | 131 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000132](../../tests/test_task_understanding.py#L132) | 132 | `"    )"` | — |
| [SRC-AFEDC2645A-L000133](../../tests/test_task_understanding.py#L133) | 133 | `"    assert spec[\"task_family\"] in {\"social_opinions\", \"compare\"}"` | — |
| [SRC-AFEDC2645A-L000134](../../tests/test_task_understanding.py#L134) | 134 | `"    assert spec[\"constraints\"][\"time_sensitive_request\"] is True"` | — |
| [SRC-AFEDC2645A-L000135](../../tests/test_task_understanding.py#L135) | 135 | `"    assert spec[\"constraints\"][\"social_evidence_requested\"] is True"` | — |
| [SRC-AFEDC2645A-L000136](../../tests/test_task_understanding.py#L136) | 136 | `"    assert \"publication_or_update_date\" in spec[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000137](../../tests/test_task_understanding.py#L137) | 137 | `"    assert \"preserve_explicit_comparison_criteria\" in spec[\"evidence_requirements\"] or \"preserve_each_explicit_comparison_criterion\" in spec[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000138](../../tests/test_task_understanding.py#L138) | 138 | `"    assert \"personal_experience\" in spec[\"query_strategies\"]"` | — |
| [SRC-AFEDC2645A-L000139](../../tests/test_task_understanding.py#L139) | 139 | `"    assert \"date_check\" in spec[\"query_strategies\"]"` | — |
| [SRC-AFEDC2645A-L000140](../../tests/test_task_understanding.py#L140) | 140 | `""` | — |
| [SRC-AFEDC2645A-L000141](../../tests/test_task_understanding.py#L141) | 141 | `""` | — |
| [SRC-AFEDC2645A-L000142](../../tests/test_task_understanding.py#L142) | 142 | `"def test_alarm_word_does_not_trigger_current_information_pattern():"` | — |
| [SRC-AFEDC2645A-L000143](../../tests/test_task_understanding.py#L143) | 143 | `"    spec = build_task_spec(\"ما معنى نظام الإنذار المعنون؟\", mode=\"auto\", intent_route=\"MODEL_ONLY\")"` | — |
| [SRC-AFEDC2645A-L000144](../../tests/test_task_understanding.py#L144) | 144 | `"    assert spec[\"constraints\"][\"time_sensitive_request\"] is False"` | — |
| [SRC-AFEDC2645A-L000145](../../tests/test_task_understanding.py#L145) | 145 | `"    assert spec[\"task_family\"] == \"explain_or_define\""` | — |
| [SRC-AFEDC2645A-L000146](../../tests/test_task_understanding.py#L146) | 146 | `""` | — |
| [SRC-AFEDC2645A-L000147](../../tests/test_task_understanding.py#L147) | 147 | `""` | — |
| [SRC-AFEDC2645A-L000148](../../tests/test_task_understanding.py#L148) | 148 | `"def test_clarification_route_does_not_claim_search_or_generation_tools():"` | — |
| [SRC-AFEDC2645A-L000149](../../tests/test_task_understanding.py#L149) | 149 | `"    spec = build_task_spec(\"كام سعرها؟\", mode=\"deep\", intent_route=\"CLARIFY\")"` | — |
| [SRC-AFEDC2645A-L000150](../../tests/test_task_understanding.py#L150) | 150 | `"    assert spec[\"ambiguity_status\"] == \"needs_clarification\""` | — |
| [SRC-AFEDC2645A-L000151](../../tests/test_task_understanding.py#L151) | 151 | `"    assert \"web_search\" not in spec[\"tool_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000152](../../tests/test_task_understanding.py#L152) | 152 | `"    assert \"page_fetch\" not in spec[\"tool_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000153](../../tests/test_task_understanding.py#L153) | 153 | `"    assert \"language_model_generation_if_configured\" not in spec[\"tool_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000154](../../tests/test_task_understanding.py#L154) | 154 | `""` | — |
| [SRC-AFEDC2645A-L000155](../../tests/test_task_understanding.py#L155) | 155 | `""` | — |
| [SRC-AFEDC2645A-L000156](../../tests/test_task_understanding.py#L156) | 156 | `"def test_summary_text_and_page_link_require_different_tools():"` | — |
| [SRC-AFEDC2645A-L000157](../../tests/test_task_understanding.py#L157) | 157 | `"    pasted = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000158](../../tests/test_task_understanding.py#L158) | 158 | `"        \"لخص النص التالي: يتناول النص صيانة أجهزة الإنذار وإجراء الاختبار الدوري.\","` | — |
| [SRC-AFEDC2645A-L000159](../../tests/test_task_understanding.py#L159) | 159 | `"        mode=\"auto\","` | — |
| [SRC-AFEDC2645A-L000160](../../tests/test_task_understanding.py#L160) | 160 | `"        intent_route=\"MODEL_ONLY\","` | — |
| [SRC-AFEDC2645A-L000161](../../tests/test_task_understanding.py#L161) | 161 | `"    )"` | — |
| [SRC-AFEDC2645A-L000162](../../tests/test_task_understanding.py#L162) | 162 | `"    assert pasted[\"constraints\"][\"inline_text_supplied_for_summary\"] is True"` | — |
| [SRC-AFEDC2645A-L000163](../../tests/test_task_understanding.py#L163) | 163 | `"    assert \"page_fetch\" not in pasted[\"tool_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000164](../../tests/test_task_understanding.py#L164) | 164 | `"    assert \"web_search\" not in pasted[\"tool_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000165](../../tests/test_task_understanding.py#L165) | 165 | `"    linked = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000166](../../tests/test_task_understanding.py#L166) | 166 | `"        \"لخص الصفحة https://example.com/manual\","` | — |
| [SRC-AFEDC2645A-L000167](../../tests/test_task_understanding.py#L167) | 167 | `"        mode=\"auto\","` | — |
| [SRC-AFEDC2645A-L000168](../../tests/test_task_understanding.py#L168) | 168 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-AFEDC2645A-L000169](../../tests/test_task_understanding.py#L169) | 169 | `"    )"` | — |
| [SRC-AFEDC2645A-L000170](../../tests/test_task_understanding.py#L170) | 170 | `"    assert \"page_fetch\" in linked[\"tool_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000171](../../tests/test_task_understanding.py#L171) | 171 | `"    assert \"web_search\" in linked[\"tool_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000172](../../tests/test_task_understanding.py#L172) | 172 | `""` | — |
| [SRC-AFEDC2645A-L000173](../../tests/test_task_understanding.py#L173) | 173 | `""` | — |
| [SRC-AFEDC2645A-L000174](../../tests/test_task_understanding.py#L174) | 174 | `"def test_output_format_preferences_are_preserved_separately_from_intent():"` | — |
| [SRC-AFEDC2645A-L000175](../../tests/test_task_understanding.py#L175) | 175 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000176](../../tests/test_task_understanding.py#L176) | 176 | `"        \"قارن الخيارين في جدول مع أمثلة وبالتفصيل وعلى شكل نقاط\","` | — |
| [SRC-AFEDC2645A-L000177](../../tests/test_task_understanding.py#L177) | 177 | `"        mode=\"deep\","` | — |
| [SRC-AFEDC2645A-L000178](../../tests/test_task_understanding.py#L178) | 178 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000179](../../tests/test_task_understanding.py#L179) | 179 | `"    )"` | — |
| [SRC-AFEDC2645A-L000180](../../tests/test_task_understanding.py#L180) | 180 | `"    preferences = spec[\"output_preferences\"]"` | — |
| [SRC-AFEDC2645A-L000181](../../tests/test_task_understanding.py#L181) | 181 | `"    assert preferences[\"table_requested\"] is True"` | — |
| [SRC-AFEDC2645A-L000182](../../tests/test_task_understanding.py#L182) | 182 | `"    assert preferences[\"examples_requested\"] is True"` | — |
| [SRC-AFEDC2645A-L000183](../../tests/test_task_understanding.py#L183) | 183 | `"    assert preferences[\"detailed\"] is True"` | — |
| [SRC-AFEDC2645A-L000184](../../tests/test_task_understanding.py#L184) | 184 | `"    assert preferences[\"bullets_or_checklist_requested\"] is True"` | — |
| [SRC-AFEDC2645A-L000185](../../tests/test_task_understanding.py#L185) | 185 | `""` | — |
| [SRC-AFEDC2645A-L000186](../../tests/test_task_understanding.py#L186) | 186 | `""` | — |
| [SRC-AFEDC2645A-L000187](../../tests/test_task_understanding.py#L187) | 187 | `"def test_location_matching_avoids_partial_english_word_collision():"` | — |
| [SRC-AFEDC2645A-L000188](../../tests/test_task_understanding.py#L188) | 188 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000189](../../tests/test_task_understanding.py#L189) | 189 | `"        \"Explain Egyptology as an academic field\","` | — |
| [SRC-AFEDC2645A-L000190](../../tests/test_task_understanding.py#L190) | 190 | `"        mode=\"auto\","` | — |
| [SRC-AFEDC2645A-L000191](../../tests/test_task_understanding.py#L191) | 191 | `"        intent_route=\"MODEL_ONLY\","` | — |
| [SRC-AFEDC2645A-L000192](../../tests/test_task_understanding.py#L192) | 192 | `"    )"` | — |
| [SRC-AFEDC2645A-L000193](../../tests/test_task_understanding.py#L193) | 193 | `"    assert \"مصر\" not in spec[\"constraints\"][\"explicit_locations\"]"` | — |
| [SRC-AFEDC2645A-L000194](../../tests/test_task_understanding.py#L194) | 194 | `""` | — |
| [SRC-AFEDC2645A-L000195](../../tests/test_task_understanding.py#L195) | 195 | `""` | — |
| [SRC-AFEDC2645A-L000196](../../tests/test_task_understanding.py#L196) | 196 | `"def test_source_policies_keep_orthogonal_research_constraints():"` | — |
| [SRC-AFEDC2645A-L000197](../../tests/test_task_understanding.py#L197) | 197 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000198](../../tests/test_task_understanding.py#L198) | 198 | `"        \"قارن تجارب ملاك السيارات الكهربائية في مصر اليوم من حيث السعر والاعتمادية\","` | — |
| [SRC-AFEDC2645A-L000199](../../tests/test_task_understanding.py#L199) | 199 | `"        mode=\"social\","` | — |
| [SRC-AFEDC2645A-L000200](../../tests/test_task_understanding.py#L200) | 200 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000201](../../tests/test_task_understanding.py#L201) | 201 | `"    )"` | — |
| [SRC-AFEDC2645A-L000202](../../tests/test_task_understanding.py#L202) | 202 | `"    policies = spec[\"constraints\"][\"source_policies\"]"` | — |
| [SRC-AFEDC2645A-L000203](../../tests/test_task_understanding.py#L203) | 203 | `"    assert \"current_read_page\" in policies"` | — |
| [SRC-AFEDC2645A-L000204](../../tests/test_task_understanding.py#L204) | 204 | `"    assert \"public_social_content\" in policies"` | — |
| [SRC-AFEDC2645A-L000205](../../tests/test_task_understanding.py#L205) | 205 | `"    assert spec[\"constraints\"][\"time_sensitive_request\"] is True"` | — |
| [SRC-AFEDC2645A-L000206](../../tests/test_task_understanding.py#L206) | 206 | `"    assert spec[\"constraints\"][\"social_evidence_requested\"] is True"` | — |
| [SRC-AFEDC2645A-L000207](../../tests/test_task_understanding.py#L207) | 207 | `"    assert \"publication_or_update_date\" in spec[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000208](../../tests/test_task_understanding.py#L208) | 208 | `"    assert \"heuristic_classification_is_not_identity_or_truth_verification\" in spec[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000209](../../tests/test_task_understanding.py#L209) | 209 | `""` | — |
| [SRC-AFEDC2645A-L000210](../../tests/test_task_understanding.py#L210) | 210 | `""` | — |
| [SRC-AFEDC2645A-L000211](../../tests/test_task_understanding.py#L211) | 211 | `"def test_official_site_request_without_a_target_marks_required_input():"` | — |
| [SRC-AFEDC2645A-L000212](../../tests/test_task_understanding.py#L212) | 212 | `"    spec = build_task_spec(\"هات الموقع الرسمي\", mode=\"auto\", intent_route=\"WEB_SIMPLE\")"` | — |
| [SRC-AFEDC2645A-L000213](../../tests/test_task_understanding.py#L213) | 213 | `"    assert spec[\"task_family\"] == \"official_site_lookup\""` | — |
| [SRC-AFEDC2645A-L000214](../../tests/test_task_understanding.py#L214) | 214 | `"    assert \"official_destination_target_entity\" in spec[\"missing_required_inputs\"]"` | — |
| [SRC-AFEDC2645A-L000215](../../tests/test_task_understanding.py#L215) | 215 | `"    assert spec[\"requires_clarification\"] is True"` | — |
| [SRC-AFEDC2645A-L000216](../../tests/test_task_understanding.py#L216) | 216 | `""` | — |
| [SRC-AFEDC2645A-L000217](../../tests/test_task_understanding.py#L217) | 217 | `""` | — |
| [SRC-AFEDC2645A-L000218](../../tests/test_task_understanding.py#L218) | 218 | `"def test_official_site_request_with_a_named_target_does_not_require_subject_clarification():"` | — |
| [SRC-AFEDC2645A-L000219](../../tests/test_task_understanding.py#L219) | 219 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000220](../../tests/test_task_understanding.py#L220) | 220 | `"        \"هات الموقع الرسمي لوزارة الاتصالات في مصر\","` | — |
| [SRC-AFEDC2645A-L000221](../../tests/test_task_understanding.py#L221) | 221 | `"        mode=\"auto\","` | — |
| [SRC-AFEDC2645A-L000222](../../tests/test_task_understanding.py#L222) | 222 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-AFEDC2645A-L000223](../../tests/test_task_understanding.py#L223) | 223 | `"    )"` | — |
| [SRC-AFEDC2645A-L000224](../../tests/test_task_understanding.py#L224) | 224 | `"    assert \"official_destination_target_entity\" not in spec[\"missing_required_inputs\"]"` | — |
| [SRC-AFEDC2645A-L000225](../../tests/test_task_understanding.py#L225) | 225 | `"    assert spec[\"constraints\"][\"official_destination_required\"] is True"` | — |
| [SRC-AFEDC2645A-L000226](../../tests/test_task_understanding.py#L226) | 226 | `""` | — |
| [SRC-AFEDC2645A-L000227](../../tests/test_task_understanding.py#L227) | 227 | `""` | — |
| [SRC-AFEDC2645A-L000228](../../tests/test_task_understanding.py#L228) | 228 | `"def test_summary_without_url_or_text_marks_required_input():"` | — |
| [SRC-AFEDC2645A-L000229](../../tests/test_task_understanding.py#L229) | 229 | `"    spec = build_task_spec(\"لخص\", mode=\"auto\", intent_route=\"MODEL_ONLY\")"` | — |
| [SRC-AFEDC2645A-L000230](../../tests/test_task_understanding.py#L230) | 230 | `"    assert \"summary_source_url_or_pasted_text\" in spec[\"missing_required_inputs\"]"` | — |
| [SRC-AFEDC2645A-L000231](../../tests/test_task_understanding.py#L231) | 231 | `"    assert spec[\"requires_clarification\"] is True"` | — |
| [SRC-AFEDC2645A-L000232](../../tests/test_task_understanding.py#L232) | 232 | `""` | — |
| [SRC-AFEDC2645A-L000233](../../tests/test_task_understanding.py#L233) | 233 | `""` | — |
| [SRC-AFEDC2645A-L000234](../../tests/test_task_understanding.py#L234) | 234 | `"def test_output_preferences_do_not_count_as_competing_intent_hypotheses():"` | — |
| [SRC-AFEDC2645A-L000235](../../tests/test_task_understanding.py#L235) | 235 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000236](../../tests/test_task_understanding.py#L236) | 236 | `"        \"قارن الخيارين في جدول مع أمثلة وبالتفصيل\","` | — |
| [SRC-AFEDC2645A-L000237](../../tests/test_task_understanding.py#L237) | 237 | `"        mode=\"deep\","` | — |
| [SRC-AFEDC2645A-L000238](../../tests/test_task_understanding.py#L238) | 238 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000239](../../tests/test_task_understanding.py#L239) | 239 | `"    )"` | — |
| [SRC-AFEDC2645A-L000240](../../tests/test_task_understanding.py#L240) | 240 | `"    families = {row[\"family\"] for row in spec[\"hypothesis_interpretations\"]}"` | — |
| [SRC-AFEDC2645A-L000241](../../tests/test_task_understanding.py#L241) | 241 | `"    assert \"compare\" in families"` | — |
| [SRC-AFEDC2645A-L000242](../../tests/test_task_understanding.py#L242) | 242 | `"    assert not any(family.startswith(\"output_\") for family in families)"` | — |
| [SRC-AFEDC2645A-L000243](../../tests/test_task_understanding.py#L243) | 243 | `"    assert spec[\"ambiguity_status\"] == \"no_strong_lexical_conflict_detected\""` | — |
| [SRC-AFEDC2645A-L000244](../../tests/test_task_understanding.py#L244) | 244 | `""` | — |
| [SRC-AFEDC2645A-L000245](../../tests/test_task_understanding.py#L245) | 245 | `""` | — |
| [SRC-AFEDC2645A-L000246](../../tests/test_task_understanding.py#L246) | 246 | `"@pytest.mark.parametrize("` | — |
| [SRC-AFEDC2645A-L000247](../../tests/test_task_understanding.py#L247) | 247 | `"    (\"question\", \"family\"),"` | — |
| [SRC-AFEDC2645A-L000248](../../tests/test_task_understanding.py#L248) | 248 | `"    ["` | — |
| [SRC-AFEDC2645A-L000249](../../tests/test_task_understanding.py#L249) | 249 | `"        (\"ترجم هذا النص إلى الإنجليزية: Hello world\", \"translation\"),"` | — |
| [SRC-AFEDC2645A-L000250](../../tests/test_task_understanding.py#L250) | 250 | `"        (\"اكتب بريد إلكتروني للعميل بنبرة مهنية\", \"writing_or_editing\"),"` | — |
| [SRC-AFEDC2645A-L000251](../../tests/test_task_understanding.py#L251) | 251 | `"        (\"احسب 17 بالمئة من 500\", \"calculation\"),"` | — |
| [SRC-AFEDC2645A-L000252](../../tests/test_task_understanding.py#L252) | 252 | `"        (\"حلل البيانات في ملف CSV وحدد القيم الناقصة\", \"data_analysis\"),"` | — |
| [SRC-AFEDC2645A-L000253](../../tests/test_task_understanding.py#L253) | 253 | `"        (\"راجع كود Python الذي يعرض stack trace\", \"coding_or_technical_design\"),"` | — |
| [SRC-AFEDC2645A-L000254](../../tests/test_task_understanding.py#L254) | 254 | `"        (\"ضع خطة عمل لافتتاح متجر خلال شهر\", \"planning\"),"` | — |
| [SRC-AFEDC2645A-L000255](../../tests/test_task_understanding.py#L255) | 255 | `"        (\"ما أعراض الإنفلونزا؟\", \"medical_information\"),"` | — |
| [SRC-AFEDC2645A-L000256](../../tests/test_task_understanding.py#L256) | 256 | `"        (\"ما شروط العقد وفق القانون المصري؟\", \"legal_information\"),"` | — |
| [SRC-AFEDC2645A-L000257](../../tests/test_task_understanding.py#L257) | 257 | `"        (\"اكتب قصة قصيرة عن رحلة خيالية\", \"creative_generation\"),"` | — |
| [SRC-AFEDC2645A-L000258](../../tests/test_task_understanding.py#L258) | 258 | `"    ],"` | — |
| [SRC-AFEDC2645A-L000259](../../tests/test_task_understanding.py#L259) | 259 | `")"` | — |
| [SRC-AFEDC2645A-L000260](../../tests/test_task_understanding.py#L260) | 260 | `"def test_extended_task_families_cover_non_search_and_specialized_requests(question, family):"` | — |
| [SRC-AFEDC2645A-L000261](../../tests/test_task_understanding.py#L261) | 261 | `"    spec = build_task_spec(question, mode=\"auto\", intent_route=\"MODEL_ONLY\")"` | — |
| [SRC-AFEDC2645A-L000262](../../tests/test_task_understanding.py#L262) | 262 | `"    assert spec[\"task_family\"] == family"` | — |
| [SRC-AFEDC2645A-L000263](../../tests/test_task_understanding.py#L263) | 263 | `"    assert spec[\"classification_is_probability\"] is False"` | — |
| [SRC-AFEDC2645A-L000264](../../tests/test_task_understanding.py#L264) | 264 | `"    assert spec[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000265](../../tests/test_task_understanding.py#L265) | 265 | `"    assert spec[\"query_strategies\"]"` | — |
| [SRC-AFEDC2645A-L000266](../../tests/test_task_understanding.py#L266) | 266 | `""` | — |
| [SRC-AFEDC2645A-L000267](../../tests/test_task_understanding.py#L267) | 267 | `""` | — |
| [SRC-AFEDC2645A-L000268](../../tests/test_task_understanding.py#L268) | 268 | `"def test_health_and_legal_tasks_attach_domain_specific_caution():"` | — |
| [SRC-AFEDC2645A-L000269](../../tests/test_task_understanding.py#L269) | 269 | `"    health = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000270](../../tests/test_task_understanding.py#L270) | 270 | `"        \"ما أعراض الإنفلونزا اليوم؟\","` | — |
| [SRC-AFEDC2645A-L000271](../../tests/test_task_understanding.py#L271) | 271 | `"        mode=\"latest\","` | — |
| [SRC-AFEDC2645A-L000272](../../tests/test_task_understanding.py#L272) | 272 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-AFEDC2645A-L000273](../../tests/test_task_understanding.py#L273) | 273 | `"    )"` | — |
| [SRC-AFEDC2645A-L000274](../../tests/test_task_understanding.py#L274) | 274 | `"    assert \"authoritative_health_content\" in health[\"constraints\"][\"source_policies\"]"` | — |
| [SRC-AFEDC2645A-L000275](../../tests/test_task_understanding.py#L275) | 275 | `"    assert \"distinguish_general_health_information_from_personal_diagnosis\" in health[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000276](../../tests/test_task_understanding.py#L276) | 276 | `"    assert \"page_text_successfully_read\" in health[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000277](../../tests/test_task_understanding.py#L277) | 277 | `""` | — |
| [SRC-AFEDC2645A-L000278](../../tests/test_task_understanding.py#L278) | 278 | `"    legal = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000279](../../tests/test_task_understanding.py#L279) | 279 | `"        \"ما نص القانون الحالي المنظم للإيجار في مصر؟\","` | — |
| [SRC-AFEDC2645A-L000280](../../tests/test_task_understanding.py#L280) | 280 | `"        mode=\"latest\","` | — |
| [SRC-AFEDC2645A-L000281](../../tests/test_task_understanding.py#L281) | 281 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-AFEDC2645A-L000282](../../tests/test_task_understanding.py#L282) | 282 | `"    )"` | — |
| [SRC-AFEDC2645A-L000283](../../tests/test_task_understanding.py#L283) | 283 | `"    assert \"official_legal_text\" in legal[\"constraints\"][\"source_policies\"]"` | — |
| [SRC-AFEDC2645A-L000284](../../tests/test_task_understanding.py#L284) | 284 | `"    assert \"identify_jurisdiction_and_effective_date_if_relevant\" in legal[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000285](../../tests/test_task_understanding.py#L285) | 285 | `""` | — |
| [SRC-AFEDC2645A-L000286](../../tests/test_task_understanding.py#L286) | 286 | `""` | — |
| [SRC-AFEDC2645A-L000287](../../tests/test_task_understanding.py#L287) | 287 | `"def test_output_audience_and_delivery_preferences_are_distinct_fields():"` | — |
| [SRC-AFEDC2645A-L000288](../../tests/test_task_understanding.py#L288) | 288 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000289](../../tests/test_task_understanding.py#L289) | 289 | `"        \"اشرح الموضوع ببساطة مع مصادر وروابط مباشرة وبصيغة JSON\","` | — |
| [SRC-AFEDC2645A-L000290](../../tests/test_task_understanding.py#L290) | 290 | `"        mode=\"auto\","` | — |
| [SRC-AFEDC2645A-L000291](../../tests/test_task_understanding.py#L291) | 291 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-AFEDC2645A-L000292](../../tests/test_task_understanding.py#L292) | 292 | `"    )"` | — |
| [SRC-AFEDC2645A-L000293](../../tests/test_task_understanding.py#L293) | 293 | `"    preferences = spec[\"output_preferences\"]"` | — |
| [SRC-AFEDC2645A-L000294](../../tests/test_task_understanding.py#L294) | 294 | `"    assert preferences[\"beginner_friendly_requested\"] is True"` | — |
| [SRC-AFEDC2645A-L000295](../../tests/test_task_understanding.py#L295) | 295 | `"    assert preferences[\"citations_requested\"] is True"` | — |
| [SRC-AFEDC2645A-L000296](../../tests/test_task_understanding.py#L296) | 296 | `"    assert preferences[\"links_requested\"] is True"` | — |
| [SRC-AFEDC2645A-L000297](../../tests/test_task_understanding.py#L297) | 297 | `"    assert preferences[\"json_requested\"] is True"` | — |
| [SRC-AFEDC2645A-L000298](../../tests/test_task_understanding.py#L298) | 298 | `""` | — |
| [SRC-AFEDC2645A-L000299](../../tests/test_task_understanding.py#L299) | 299 | `""` | — |
| [SRC-AFEDC2645A-L000300](../../tests/test_task_understanding.py#L300) | 300 | `"def test_task_spec_validator_allowlists_tools_policies_and_context_slots():"` | — |
| [SRC-AFEDC2645A-L000301](../../tests/test_task_understanding.py#L301) | 301 | `"    from agents.task_understanding import validate_task_spec"` | — |
| [SRC-AFEDC2645A-L000302](../../tests/test_task_understanding.py#L302) | 302 | `""` | — |
| [SRC-AFEDC2645A-L000303](../../tests/test_task_understanding.py#L303) | 303 | `"    candidate = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000304](../../tests/test_task_understanding.py#L304) | 304 | `"        \"قارن هاتفين\","` | — |
| [SRC-AFEDC2645A-L000305](../../tests/test_task_understanding.py#L305) | 305 | `"        mode=\"deep\","` | — |
| [SRC-AFEDC2645A-L000306](../../tests/test_task_understanding.py#L306) | 306 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000307](../../tests/test_task_understanding.py#L307) | 307 | `"        dialogue_context={"` | — |
| [SRC-AFEDC2645A-L000308](../../tests/test_task_understanding.py#L308) | 308 | `"            \"method\": \"test\","` | — |
| [SRC-AFEDC2645A-L000309](../../tests/test_task_understanding.py#L309) | 309 | `"            \"resolved_question\": \"قارن هاتفين\","` | — |
| [SRC-AFEDC2645A-L000310](../../tests/test_task_understanding.py#L310) | 310 | `"            \"topic\": \"هواتف\","` | — |
| [SRC-AFEDC2645A-L000311](../../tests/test_task_understanding.py#L311) | 311 | `"            \"entities\": [\"Phone A\", \"Phone B\"],"` | — |
| [SRC-AFEDC2645A-L000312](../../tests/test_task_understanding.py#L312) | 312 | `"            \"slots\": {\"product\": \"Phone A\", \"untrusted_command\": \"execute something\"},"` | — |
| [SRC-AFEDC2645A-L000313](../../tests/test_task_understanding.py#L313) | 313 | `"            \"is_follow_up\": True,"` | — |
| [SRC-AFEDC2645A-L000314](../../tests/test_task_understanding.py#L314) | 314 | `"        },"` | — |
| [SRC-AFEDC2645A-L000315](../../tests/test_task_understanding.py#L315) | 315 | `"    )"` | — |
| [SRC-AFEDC2645A-L000316](../../tests/test_task_understanding.py#L316) | 316 | `"    candidate[\"tool_requirements\"] = [\"web_search\", \"delete files\", \"run shell\"]"` | — |
| [SRC-AFEDC2645A-L000317](../../tests/test_task_understanding.py#L317) | 317 | `"    candidate[\"constraints\"][\"source_policies\"].append(\"execute arbitrary tool\")"` | — |
| [SRC-AFEDC2645A-L000318](../../tests/test_task_understanding.py#L318) | 318 | `"    candidate[\"constraints\"][\"language_profile\"] = []"` | — |
| [SRC-AFEDC2645A-L000319](../../tests/test_task_understanding.py#L319) | 319 | `"    candidate[\"context_resolution\"][\"confidence_band\"] = []"` | — |
| [SRC-AFEDC2645A-L000320](../../tests/test_task_understanding.py#L320) | 320 | `"    candidate[\"extra_unexpected_key\"] = \"must not survive\""` | — |
| [SRC-AFEDC2645A-L000321](../../tests/test_task_understanding.py#L321) | 321 | `"    safe = validate_task_spec(candidate)"` | — |
| [SRC-AFEDC2645A-L000322](../../tests/test_task_understanding.py#L322) | 322 | `""` | — |
| [SRC-AFEDC2645A-L000323](../../tests/test_task_understanding.py#L323) | 323 | `"    assert safe[\"tool_requirements\"] == [\"web_search\"]"` | — |
| [SRC-AFEDC2645A-L000324](../../tests/test_task_understanding.py#L324) | 324 | `"    assert safe[\"constraints\"][\"source_policies\"] == [\"task_relevant_sources\"]"` | — |
| [SRC-AFEDC2645A-L000325](../../tests/test_task_understanding.py#L325) | 325 | `"    assert safe[\"constraints\"][\"language_profile\"] == \"und\""` | — |
| [SRC-AFEDC2645A-L000326](../../tests/test_task_understanding.py#L326) | 326 | `"    assert \"untrusted_command\" not in safe[\"context_resolution\"][\"slots\"]"` | — |
| [SRC-AFEDC2645A-L000327](../../tests/test_task_understanding.py#L327) | 327 | `"    assert safe[\"context_resolution\"][\"confidence_band\"] == \"unassessed\""` | — |
| [SRC-AFEDC2645A-L000328](../../tests/test_task_understanding.py#L328) | 328 | `"    assert \"extra_unexpected_key\" not in safe"` | — |
| [SRC-AFEDC2645A-L000329](../../tests/test_task_understanding.py#L329) | 329 | `""` | — |
| [SRC-AFEDC2645A-L000330](../../tests/test_task_understanding.py#L330) | 330 | `""` | — |
| [SRC-AFEDC2645A-L000331](../../tests/test_task_understanding.py#L331) | 331 | `"def test_reasoning_playbook_combines_primary_task_and_orthogonal_constraints():"` | — |
| [SRC-AFEDC2645A-L000332](../../tests/test_task_understanding.py#L332) | 332 | `"    from agents.task_understanding import reasoning_guidance_for_task_spec"` | — |
| [SRC-AFEDC2645A-L000333](../../tests/test_task_understanding.py#L333) | 333 | `""` | — |
| [SRC-AFEDC2645A-L000334](../../tests/test_task_understanding.py#L334) | 334 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000335](../../tests/test_task_understanding.py#L335) | 335 | `"        \"قارن تجارب ملاك السيارات الكهربائية في مصر اليوم من حيث السعر والأمان والتوفر\","` | — |
| [SRC-AFEDC2645A-L000336](../../tests/test_task_understanding.py#L336) | 336 | `"        mode=\"latest\","` | — |
| [SRC-AFEDC2645A-L000337](../../tests/test_task_understanding.py#L337) | 337 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000338](../../tests/test_task_understanding.py#L338) | 338 | `"        dialogue_context={"` | — |
| [SRC-AFEDC2645A-L000339](../../tests/test_task_understanding.py#L339) | 339 | `"            \"is_follow_up\": True,"` | — |
| [SRC-AFEDC2645A-L000340](../../tests/test_task_understanding.py#L340) | 340 | `"            \"topic_shift\": False,"` | — |
| [SRC-AFEDC2645A-L000341](../../tests/test_task_understanding.py#L341) | 341 | `"            \"resolved_question\": \"قارن تجارب ملاك السيارات الكهربائية في مصر اليوم من حيث السعر والأمان والتوفر\","` | — |
| [SRC-AFEDC2645A-L000342](../../tests/test_task_understanding.py#L342) | 342 | `"            \"method\": \"test_context\","` | — |
| [SRC-AFEDC2645A-L000343](../../tests/test_task_understanding.py#L343) | 343 | `"        },"` | — |
| [SRC-AFEDC2645A-L000344](../../tests/test_task_understanding.py#L344) | 344 | `"    )"` | — |
| [SRC-AFEDC2645A-L000345](../../tests/test_task_understanding.py#L345) | 345 | `""` | — |
| [SRC-AFEDC2645A-L000346](../../tests/test_task_understanding.py#L346) | 346 | `"    ids = set(spec[\"reasoning_strategy_ids\"])"` | — |
| [SRC-AFEDC2645A-L000347](../../tests/test_task_understanding.py#L347) | 347 | `"    assert spec[\"task_family\"] in {\"social_opinions\", \"compare\"}"` | — |
| [SRC-AFEDC2645A-L000348](../../tests/test_task_understanding.py#L348) | 348 | `"    assert \"separate_facts_inferences_hypotheses\" in ids"` | — |
| [SRC-AFEDC2645A-L000349](../../tests/test_task_understanding.py#L349) | 349 | `"    assert \"bounded_stop_rule\" in ids"` | — |
| [SRC-AFEDC2645A-L000350](../../tests/test_task_understanding.py#L350) | 350 | `"    assert \"separate_event_and_publication_dates\" in ids"` | — |
| [SRC-AFEDC2645A-L000351](../../tests/test_task_understanding.py#L351) | 351 | `"    assert \"reject_stale_current_claims\" in ids"` | — |
| [SRC-AFEDC2645A-L000352](../../tests/test_task_understanding.py#L352) | 352 | `"    assert \"balance_social_evidence\" in ids"` | — |
| [SRC-AFEDC2645A-L000353](../../tests/test_task_understanding.py#L353) | 353 | `"    assert \"resolve_followup_slots\" in ids"` | — |
| [SRC-AFEDC2645A-L000354](../../tests/test_task_understanding.py#L354) | 354 | `"    assert \"decompose_explicit_criteria\" in ids"` | — |
| [SRC-AFEDC2645A-L000355](../../tests/test_task_understanding.py#L355) | 355 | `"    assert len(spec[\"decision_matrix\"]) == 6"` | — |
| [SRC-AFEDC2645A-L000356](../../tests/test_task_understanding.py#L356) | 356 | `""` | — |
| [SRC-AFEDC2645A-L000357](../../tests/test_task_understanding.py#L357) | 357 | `"    guidance = reasoning_guidance_for_task_spec(spec)"` | — |
| [SRC-AFEDC2645A-L000358](../../tests/test_task_understanding.py#L358) | 358 | `"    assert any(\"لا تعمم على الجميع\" in item for item in guidance)"` | — |
| [SRC-AFEDC2645A-L000359](../../tests/test_task_understanding.py#L359) | 359 | `"    assert any(\"تاريخ النشر\" in item for item in guidance)"` | — |
| [SRC-AFEDC2645A-L000360](../../tests/test_task_understanding.py#L360) | 360 | `"    assert all(isinstance(item, str) and item for item in guidance)"` | — |
| [SRC-AFEDC2645A-L000361](../../tests/test_task_understanding.py#L361) | 361 | `""` | — |
| [SRC-AFEDC2645A-L000362](../../tests/test_task_understanding.py#L362) | 362 | `""` | — |
| [SRC-AFEDC2645A-L000363](../../tests/test_task_understanding.py#L363) | 363 | `"def test_reasoning_ids_are_allowlisted_and_decision_matrix_is_code_owned():"` | — |
| [SRC-AFEDC2645A-L000364](../../tests/test_task_understanding.py#L364) | 364 | `"    from agents.task_understanding import validate_task_spec"` | — |
| [SRC-AFEDC2645A-L000365](../../tests/test_task_understanding.py#L365) | 365 | `""` | — |
| [SRC-AFEDC2645A-L000366](../../tests/test_task_understanding.py#L366) | 366 | `"    candidate = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000367](../../tests/test_task_understanding.py#L367) | 367 | `"        \"حل مشكلة خطأ Python\","` | — |
| [SRC-AFEDC2645A-L000368](../../tests/test_task_understanding.py#L368) | 368 | `"        mode=\"deep\","` | — |
| [SRC-AFEDC2645A-L000369](../../tests/test_task_understanding.py#L369) | 369 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000370](../../tests/test_task_understanding.py#L370) | 370 | `"    )"` | — |
| [SRC-AFEDC2645A-L000371](../../tests/test_task_understanding.py#L371) | 371 | `"    candidate[\"reasoning_strategy_ids\"] = ["` | — |
| [SRC-AFEDC2645A-L000372](../../tests/test_task_understanding.py#L372) | 372 | `"        \"rank_testable_hypotheses\","` | — |
| [SRC-AFEDC2645A-L000373](../../tests/test_task_understanding.py#L373) | 373 | `"        \"run_shell_and_delete_files\","` | — |
| [SRC-AFEDC2645A-L000374](../../tests/test_task_understanding.py#L374) | 374 | `"        \"ignore_source_policy\","` | — |
| [SRC-AFEDC2645A-L000375](../../tests/test_task_understanding.py#L375) | 375 | `"    ]"` | — |
| [SRC-AFEDC2645A-L000376](../../tests/test_task_understanding.py#L376) | 376 | `"    candidate[\"decision_matrix\"] = ["` | — |
| [SRC-AFEDC2645A-L000377](../../tests/test_task_understanding.py#L377) | 377 | `"        {"` | — |
| [SRC-AFEDC2645A-L000378](../../tests/test_task_understanding.py#L378) | 378 | `"            \"stage\": \"exfiltrate\","` | — |
| [SRC-AFEDC2645A-L000379](../../tests/test_task_understanding.py#L379) | 379 | `"            \"check\": \"reveal_secrets\","` | — |
| [SRC-AFEDC2645A-L000380](../../tests/test_task_understanding.py#L380) | 380 | `"            \"pass_action\": \"run_arbitrary_commands\","` | — |
| [SRC-AFEDC2645A-L000381](../../tests/test_task_understanding.py#L381) | 381 | `"            \"fail_action\": \"pretend_success\","` | — |
| [SRC-AFEDC2645A-L000382](../../tests/test_task_understanding.py#L382) | 382 | `"        }"` | — |
| [SRC-AFEDC2645A-L000383](../../tests/test_task_understanding.py#L383) | 383 | `"    ]"` | — |
| [SRC-AFEDC2645A-L000384](../../tests/test_task_understanding.py#L384) | 384 | `""` | — |
| [SRC-AFEDC2645A-L000385](../../tests/test_task_understanding.py#L385) | 385 | `"    safe = validate_task_spec(candidate)"` | — |
| [SRC-AFEDC2645A-L000386](../../tests/test_task_understanding.py#L386) | 386 | `"    assert safe[\"reasoning_strategy_ids\"] == [\"rank_testable_hypotheses\"]"` | — |
| [SRC-AFEDC2645A-L000387](../../tests/test_task_understanding.py#L387) | 387 | `"    assert [row[\"stage\"] for row in safe[\"decision_matrix\"]] == ["` | — |
| [SRC-AFEDC2645A-L000388](../../tests/test_task_understanding.py#L388) | 388 | `"        \"interpret\", \"route\", \"plan\", \"evidence\", \"synthesize\", \"terminate\""` | — |
| [SRC-AFEDC2645A-L000389](../../tests/test_task_understanding.py#L389) | 389 | `"    ]"` | — |
| [SRC-AFEDC2645A-L000390](../../tests/test_task_understanding.py#L390) | 390 | `"    assert not any(row.get(\"stage\") == \"exfiltrate\" for row in safe[\"decision_matrix\"])"` | — |
| [SRC-AFEDC2645A-L000391](../../tests/test_task_understanding.py#L391) | 391 | `"    assert \"reasoning_guidance\" not in safe"` | — |
## اختبارات

### FILE-FBDC61DA0B — [tests/test_tool_execution_status.py](../../tests/test_tool_execution_status.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-FBDC61DA0B-L000001](../../tests/test_tool_execution_status.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-FBDC61DA0B-L000002](../../tests/test_tool_execution_status.py#L2) | 2 | `""` | — |
| [SRC-FBDC61DA0B-L000003](../../tests/test_tool_execution_status.py#L3) | 3 | `"from agents.tool_execution_status import build_tool_execution_matrix"` | — |
| [SRC-FBDC61DA0B-L000004](../../tests/test_tool_execution_status.py#L4) | 4 | `""` | — |
| [SRC-FBDC61DA0B-L000005](../../tests/test_tool_execution_status.py#L5) | 5 | `""` | — |
| [SRC-FBDC61DA0B-L000006](../../tests/test_tool_execution_status.py#L6) | 6 | `"TOOLS = {"` | — |
| [SRC-FBDC61DA0B-L000007](../../tests/test_tool_execution_status.py#L7) | 7 | `"    \"web_search\","` | — |
| [SRC-FBDC61DA0B-L000008](../../tests/test_tool_execution_status.py#L8) | 8 | `"    \"page_fetch\","` | — |
| [SRC-FBDC61DA0B-L000009](../../tests/test_tool_execution_status.py#L9) | 9 | `"    \"public_social_search_if_configured\","` | — |
| [SRC-FBDC61DA0B-L000010](../../tests/test_tool_execution_status.py#L10) | 10 | `"    \"language_model_generation_if_configured\","` | — |
| [SRC-FBDC61DA0B-L000011](../../tests/test_tool_execution_status.py#L11) | 11 | `"    \"claim_review_if_configured\","` | — |
| [SRC-FBDC61DA0B-L000012](../../tests/test_tool_execution_status.py#L12) | 12 | `"}"` | — |
| [SRC-FBDC61DA0B-L000013](../../tests/test_tool_execution_status.py#L13) | 13 | `""` | — |
| [SRC-FBDC61DA0B-L000014](../../tests/test_tool_execution_status.py#L14) | 14 | `""` | — |
| [SRC-FBDC61DA0B-L000015](../../tests/test_tool_execution_status.py#L15) | 15 | `"def _statuses(rows):"` | — |
| [SRC-FBDC61DA0B-L000016](../../tests/test_tool_execution_status.py#L16) | 16 | `"    return {row[\"tool\"]: row[\"status\"] for row in rows}"` | — |
| [SRC-FBDC61DA0B-L000017](../../tests/test_tool_execution_status.py#L17) | 17 | `""` | — |
| [SRC-FBDC61DA0B-L000018](../../tests/test_tool_execution_status.py#L18) | 18 | `""` | — |
| [SRC-FBDC61DA0B-L000019](../../tests/test_tool_execution_status.py#L19) | 19 | `"def test_tool_matrix_distinguishes_no_usable_results_from_page_read_failure():"` | — |
| [SRC-FBDC61DA0B-L000020](../../tests/test_tool_execution_status.py#L20) | 20 | `"    spec = {\"tool_requirements\": sorted(TOOLS)}"` | — |
| [SRC-FBDC61DA0B-L000021](../../tests/test_tool_execution_status.py#L21) | 21 | `"    result = {"` | — |
| [SRC-FBDC61DA0B-L000022](../../tests/test_tool_execution_status.py#L22) | 22 | `"        \"search_attempted\": True,"` | — |
| [SRC-FBDC61DA0B-L000023](../../tests/test_tool_execution_status.py#L23) | 23 | `"        \"used_language_model\": False,"` | — |
| [SRC-FBDC61DA0B-L000024](../../tests/test_tool_execution_status.py#L24) | 24 | `"        \"final_answer_status\": \"model_not_configured_fallback\","` | — |
| [SRC-FBDC61DA0B-L000025](../../tests/test_tool_execution_status.py#L25) | 25 | `"        \"sources\": [],"` | — |
| [SRC-FBDC61DA0B-L000026](../../tests/test_tool_execution_status.py#L26) | 26 | `"    }"` | — |
| [SRC-FBDC61DA0B-L000027](../../tests/test_tool_execution_status.py#L27) | 27 | `"    report = {"` | — |
| [SRC-FBDC61DA0B-L000028](../../tests/test_tool_execution_status.py#L28) | 28 | `"        \"search_outcome\": \"attempted_no_usable_sources\","` | — |
| [SRC-FBDC61DA0B-L000029](../../tests/test_tool_execution_status.py#L29) | 29 | `"        \"usable_sources_after_filtering\": 0,"` | — |
| [SRC-FBDC61DA0B-L000030](../../tests/test_tool_execution_status.py#L30) | 30 | `"        \"pages_fetch_attempted\": 3,"` | — |
| [SRC-FBDC61DA0B-L000031](../../tests/test_tool_execution_status.py#L31) | 31 | `"        \"pages_fetched\": 0,"` | — |
| [SRC-FBDC61DA0B-L000032](../../tests/test_tool_execution_status.py#L32) | 32 | `"        \"social_direct_results\": 0,"` | — |
| [SRC-FBDC61DA0B-L000033](../../tests/test_tool_execution_status.py#L33) | 33 | `"        \"claim_audit\": \"not_run\","` | — |
| [SRC-FBDC61DA0B-L000034](../../tests/test_tool_execution_status.py#L34) | 34 | `"    }"` | — |
| [SRC-FBDC61DA0B-L000035](../../tests/test_tool_execution_status.py#L35) | 35 | `""` | — |
| [SRC-FBDC61DA0B-L000036](../../tests/test_tool_execution_status.py#L36) | 36 | `"    rows = build_tool_execution_matrix(spec, result, report)"` | — |
| [SRC-FBDC61DA0B-L000037](../../tests/test_tool_execution_status.py#L37) | 37 | `"    statuses = _statuses(rows)"` | — |
| [SRC-FBDC61DA0B-L000038](../../tests/test_tool_execution_status.py#L38) | 38 | `""` | — |
| [SRC-FBDC61DA0B-L000039](../../tests/test_tool_execution_status.py#L39) | 39 | `"    assert set(statuses) == TOOLS"` | — |
| [SRC-FBDC61DA0B-L000040](../../tests/test_tool_execution_status.py#L40) | 40 | `"    assert statuses[\"web_search\"] == \"completed_no_usable_results\""` | — |
| [SRC-FBDC61DA0B-L000041](../../tests/test_tool_execution_status.py#L41) | 41 | `"    assert statuses[\"page_fetch\"] == \"attempted_no_readable_pages\""` | — |
| [SRC-FBDC61DA0B-L000042](../../tests/test_tool_execution_status.py#L42) | 42 | `"    assert statuses[\"public_social_search_if_configured\"] == \"unknown\""` | — |
| [SRC-FBDC61DA0B-L000043](../../tests/test_tool_execution_status.py#L43) | 43 | `"    assert statuses[\"language_model_generation_if_configured\"] == \"not_configured\""` | — |
| [SRC-FBDC61DA0B-L000044](../../tests/test_tool_execution_status.py#L44) | 44 | `"    assert statuses[\"claim_review_if_configured\"] == \"not_attempted_no_evidence\""` | — |
| [SRC-FBDC61DA0B-L000045](../../tests/test_tool_execution_status.py#L45) | 45 | `"    assert all(\"لا تثبت صحة المحتوى\" in row[\"semantics\"] for row in rows)"` | — |
| [SRC-FBDC61DA0B-L000046](../../tests/test_tool_execution_status.py#L46) | 46 | `""` | — |
| [SRC-FBDC61DA0B-L000047](../../tests/test_tool_execution_status.py#L47) | 47 | `""` | — |
| [SRC-FBDC61DA0B-L000048](../../tests/test_tool_execution_status.py#L48) | 48 | `"def test_tool_matrix_reports_observed_success_without_claiming_fact_verification():"` | — |
| [SRC-FBDC61DA0B-L000049](../../tests/test_tool_execution_status.py#L49) | 49 | `"    spec = {\"tool_requirements\": sorted(TOOLS)}"` | — |
| [SRC-FBDC61DA0B-L000050](../../tests/test_tool_execution_status.py#L50) | 50 | `"    result = {"` | — |
| [SRC-FBDC61DA0B-L000051](../../tests/test_tool_execution_status.py#L51) | 51 | `"        \"search_attempted\": True,"` | — |
| [SRC-FBDC61DA0B-L000052](../../tests/test_tool_execution_status.py#L52) | 52 | `"        \"used_language_model\": True,"` | — |
| [SRC-FBDC61DA0B-L000053](../../tests/test_tool_execution_status.py#L53) | 53 | `"        \"final_answer_status\": \"model_answer_generated\","` | — |
| [SRC-FBDC61DA0B-L000054](../../tests/test_tool_execution_status.py#L54) | 54 | `"        \"sources\": ["` | — |
| [SRC-FBDC61DA0B-L000055](../../tests/test_tool_execution_status.py#L55) | 55 | `"            {"` | — |
| [SRC-FBDC61DA0B-L000056](../../tests/test_tool_execution_status.py#L56) | 56 | `"                \"url\": \"https://www.reddit.com/r/example/comments/1\","` | — |
| [SRC-FBDC61DA0B-L000057](../../tests/test_tool_execution_status.py#L57) | 57 | `"                \"platform\": \"reddit\","` | — |
| [SRC-FBDC61DA0B-L000058](../../tests/test_tool_execution_status.py#L58) | 58 | `"                \"source_class\": \"social\","` | — |
| [SRC-FBDC61DA0B-L000059](../../tests/test_tool_execution_status.py#L59) | 59 | `"                \"page_fetched\": True,"` | — |
| [SRC-FBDC61DA0B-L000060](../../tests/test_tool_execution_status.py#L60) | 60 | `"            }"` | — |
| [SRC-FBDC61DA0B-L000061](../../tests/test_tool_execution_status.py#L61) | 61 | `"        ],"` | — |
| [SRC-FBDC61DA0B-L000062](../../tests/test_tool_execution_status.py#L62) | 62 | `"    }"` | — |
| [SRC-FBDC61DA0B-L000063](../../tests/test_tool_execution_status.py#L63) | 63 | `"    report = {"` | — |
| [SRC-FBDC61DA0B-L000064](../../tests/test_tool_execution_status.py#L64) | 64 | `"        \"search_outcome\": \"attempted_with_usable_sources\","` | — |
| [SRC-FBDC61DA0B-L000065](../../tests/test_tool_execution_status.py#L65) | 65 | `"        \"usable_sources_after_filtering\": 1,"` | — |
| [SRC-FBDC61DA0B-L000066](../../tests/test_tool_execution_status.py#L66) | 66 | `"        \"pages_fetch_attempted\": 1,"` | — |
| [SRC-FBDC61DA0B-L000067](../../tests/test_tool_execution_status.py#L67) | 67 | `"        \"pages_fetched\": 1,"` | — |
| [SRC-FBDC61DA0B-L000068](../../tests/test_tool_execution_status.py#L68) | 68 | `"        \"social_direct_results\": 2,"` | — |
| [SRC-FBDC61DA0B-L000069](../../tests/test_tool_execution_status.py#L69) | 69 | `"        \"claim_audit\": \"model_claim_audit_completed\","` | — |
| [SRC-FBDC61DA0B-L000070](../../tests/test_tool_execution_status.py#L70) | 70 | `"    }"` | — |
| [SRC-FBDC61DA0B-L000071](../../tests/test_tool_execution_status.py#L71) | 71 | `""` | — |
| [SRC-FBDC61DA0B-L000072](../../tests/test_tool_execution_status.py#L72) | 72 | `"    statuses = _statuses(build_tool_execution_matrix(spec, result, report))"` | — |
| [SRC-FBDC61DA0B-L000073](../../tests/test_tool_execution_status.py#L73) | 73 | `""` | — |
| [SRC-FBDC61DA0B-L000074](../../tests/test_tool_execution_status.py#L74) | 74 | `"    assert statuses[\"web_search\"] == \"completed_with_results\""` | — |
| [SRC-FBDC61DA0B-L000075](../../tests/test_tool_execution_status.py#L75) | 75 | `"    assert statuses[\"page_fetch\"] == \"completed_with_read_pages\""` | — |
| [SRC-FBDC61DA0B-L000076](../../tests/test_tool_execution_status.py#L76) | 76 | `"    assert statuses[\"public_social_search_if_configured\"] == \"completed_with_results\""` | — |
| [SRC-FBDC61DA0B-L000077](../../tests/test_tool_execution_status.py#L77) | 77 | `"    assert statuses[\"language_model_generation_if_configured\"] == \"completed\""` | — |
| [SRC-FBDC61DA0B-L000078](../../tests/test_tool_execution_status.py#L78) | 78 | `"    assert statuses[\"claim_review_if_configured\"] == \"completed_model_assisted_review\""` | — |
| [SRC-FBDC61DA0B-L000079](../../tests/test_tool_execution_status.py#L79) | 79 | `""` | — |
| [SRC-FBDC61DA0B-L000080](../../tests/test_tool_execution_status.py#L80) | 80 | `""` | — |
| [SRC-FBDC61DA0B-L000081](../../tests/test_tool_execution_status.py#L81) | 81 | `"def test_tool_matrix_marks_unrequired_tools_not_required_and_unknowns_unknown():"` | — |
| [SRC-FBDC61DA0B-L000082](../../tests/test_tool_execution_status.py#L82) | 82 | `"    rows = build_tool_execution_matrix("` | — |
| [SRC-FBDC61DA0B-L000083](../../tests/test_tool_execution_status.py#L83) | 83 | `"        {\"tool_requirements\": []},"` | — |
| [SRC-FBDC61DA0B-L000084](../../tests/test_tool_execution_status.py#L84) | 84 | `"        {\"sources\": []},"` | — |
| [SRC-FBDC61DA0B-L000085](../../tests/test_tool_execution_status.py#L85) | 85 | `"        {},"` | — |
| [SRC-FBDC61DA0B-L000086](../../tests/test_tool_execution_status.py#L86) | 86 | `"    )"` | — |
| [SRC-FBDC61DA0B-L000087](../../tests/test_tool_execution_status.py#L87) | 87 | `""` | — |
| [SRC-FBDC61DA0B-L000088](../../tests/test_tool_execution_status.py#L88) | 88 | `"    assert all(row[\"required_by_task_spec\"] is False for row in rows)"` | — |
| [SRC-FBDC61DA0B-L000089](../../tests/test_tool_execution_status.py#L89) | 89 | `"    assert all(row[\"status\"] == \"not_required\" for row in rows)"` | — |
| [SRC-FBDC61DA0B-L000090](../../tests/test_tool_execution_status.py#L90) | 90 | `""` | — |
| [SRC-FBDC61DA0B-L000091](../../tests/test_tool_execution_status.py#L91) | 91 | `"    unknown = _statuses(build_tool_execution_matrix("` | — |
| [SRC-FBDC61DA0B-L000092](../../tests/test_tool_execution_status.py#L92) | 92 | `"        {\"tool_requirements\": [\"web_search\", \"page_fetch\"]},"` | — |
| [SRC-FBDC61DA0B-L000093](../../tests/test_tool_execution_status.py#L93) | 93 | `"        {},"` | — |
| [SRC-FBDC61DA0B-L000094](../../tests/test_tool_execution_status.py#L94) | 94 | `"        {},"` | — |
| [SRC-FBDC61DA0B-L000095](../../tests/test_tool_execution_status.py#L95) | 95 | `"    ))"` | — |
| [SRC-FBDC61DA0B-L000096](../../tests/test_tool_execution_status.py#L96) | 96 | `"    assert unknown[\"web_search\"] == \"unknown\""` | — |
| [SRC-FBDC61DA0B-L000097](../../tests/test_tool_execution_status.py#L97) | 97 | `"    assert unknown[\"page_fetch\"] == \"unknown\""` | — |
| [SRC-FBDC61DA0B-L000098](../../tests/test_tool_execution_status.py#L98) | 98 | `""` | — |
| [SRC-FBDC61DA0B-L000099](../../tests/test_tool_execution_status.py#L99) | 99 | `""` | — |
| [SRC-FBDC61DA0B-L000100](../../tests/test_tool_execution_status.py#L100) | 100 | `"def test_tool_matrix_surfaces_mismatch_between_report_counters_and_final_sources():"` | — |
| [SRC-FBDC61DA0B-L000101](../../tests/test_tool_execution_status.py#L101) | 101 | `"    rows = build_tool_execution_matrix("` | — |
| [SRC-FBDC61DA0B-L000102](../../tests/test_tool_execution_status.py#L102) | 102 | `"        {\"tool_requirements\": [\"web_search\", \"page_fetch\"]},"` | — |
| [SRC-FBDC61DA0B-L000103](../../tests/test_tool_execution_status.py#L103) | 103 | `"        {"` | — |
| [SRC-FBDC61DA0B-L000104](../../tests/test_tool_execution_status.py#L104) | 104 | `"            \"search_attempted\": True,"` | — |
| [SRC-FBDC61DA0B-L000105](../../tests/test_tool_execution_status.py#L105) | 105 | `"            \"sources\": ["` | — |
| [SRC-FBDC61DA0B-L000106](../../tests/test_tool_execution_status.py#L106) | 106 | `"                {\"url\": \"https://example.org/read\", \"page_fetched\": True, \"page_text\": \"text\"}"` | — |
| [SRC-FBDC61DA0B-L000107](../../tests/test_tool_execution_status.py#L107) | 107 | `"            ],"` | — |
| [SRC-FBDC61DA0B-L000108](../../tests/test_tool_execution_status.py#L108) | 108 | `"        },"` | — |
| [SRC-FBDC61DA0B-L000109](../../tests/test_tool_execution_status.py#L109) | 109 | `"        {"` | — |
| [SRC-FBDC61DA0B-L000110](../../tests/test_tool_execution_status.py#L110) | 110 | `"            \"search_attempted\": True,"` | — |
| [SRC-FBDC61DA0B-L000111](../../tests/test_tool_execution_status.py#L111) | 111 | `"            \"search_outcome\": \"attempted_no_usable_sources\","` | — |
| [SRC-FBDC61DA0B-L000112](../../tests/test_tool_execution_status.py#L112) | 112 | `"            \"usable_sources_after_filtering\": 0,"` | — |
| [SRC-FBDC61DA0B-L000113](../../tests/test_tool_execution_status.py#L113) | 113 | `"            \"pages_fetch_attempted\": 1,"` | — |
| [SRC-FBDC61DA0B-L000114](../../tests/test_tool_execution_status.py#L114) | 114 | `"            \"pages_fetched\": 0,"` | — |
| [SRC-FBDC61DA0B-L000115](../../tests/test_tool_execution_status.py#L115) | 115 | `"        },"` | — |
| [SRC-FBDC61DA0B-L000116](../../tests/test_tool_execution_status.py#L116) | 116 | `"    )"` | — |
| [SRC-FBDC61DA0B-L000117](../../tests/test_tool_execution_status.py#L117) | 117 | `"    by_tool = {row[\"tool\"]: row for row in rows}"` | — |
| [SRC-FBDC61DA0B-L000118](../../tests/test_tool_execution_status.py#L118) | 118 | `""` | — |
| [SRC-FBDC61DA0B-L000119](../../tests/test_tool_execution_status.py#L119) | 119 | `"    assert by_tool[\"web_search\"][\"status\"] == \"counter_mismatch\""` | — |
| [SRC-FBDC61DA0B-L000120](../../tests/test_tool_execution_status.py#L120) | 120 | `"    assert by_tool[\"web_search\"][\"basis\"][\"counter_consistency\"] == \"mismatch\""` | — |
| [SRC-FBDC61DA0B-L000121](../../tests/test_tool_execution_status.py#L121) | 121 | `"    assert by_tool[\"web_search\"][\"basis\"][\"reported_accepted_source_count\"] == 0"` | — |
| [SRC-FBDC61DA0B-L000122](../../tests/test_tool_execution_status.py#L122) | 122 | `"    assert by_tool[\"web_search\"][\"basis\"][\"accepted_source_count\"] == 1"` | — |
| [SRC-FBDC61DA0B-L000123](../../tests/test_tool_execution_status.py#L123) | 123 | `"    assert by_tool[\"page_fetch\"][\"status\"] == \"counter_mismatch\""` | — |
| [SRC-FBDC61DA0B-L000124](../../tests/test_tool_execution_status.py#L124) | 124 | `"    assert by_tool[\"page_fetch\"][\"basis\"][\"counter_consistency\"] == \"mismatch\""` | — |
| [SRC-FBDC61DA0B-L000125](../../tests/test_tool_execution_status.py#L125) | 125 | `"    assert by_tool[\"page_fetch\"][\"basis\"][\"pages_read_from_returned_sources\"] == 1"` | — |
| [SRC-FBDC61DA0B-L000126](../../tests/test_tool_execution_status.py#L126) | 126 | `"    assert by_tool[\"page_fetch\"][\"basis\"][\"reported_pages_fetched\"] == 0"` | — |
| [SRC-FBDC61DA0B-L000127](../../tests/test_tool_execution_status.py#L127) | 127 | `""` | — |
| [SRC-FBDC61DA0B-L000128](../../tests/test_tool_execution_status.py#L128) | 128 | `""` | — |
| [SRC-FBDC61DA0B-L000129](../../tests/test_tool_execution_status.py#L129) | 129 | `"def test_social_search_is_only_called_completed_when_connector_attempt_is_observed():"` | — |
| [SRC-FBDC61DA0B-L000130](../../tests/test_tool_execution_status.py#L130) | 130 | `"    rows = build_tool_execution_matrix("` | — |
| [SRC-FBDC61DA0B-L000131](../../tests/test_tool_execution_status.py#L131) | 131 | `"        {\"tool_requirements\": [\"public_social_search_if_configured\"]},"` | — |
| [SRC-FBDC61DA0B-L000132](../../tests/test_tool_execution_status.py#L132) | 132 | `"        {\"search_attempted\": True, \"sources\": []},"` | — |
| [SRC-FBDC61DA0B-L000133](../../tests/test_tool_execution_status.py#L133) | 133 | `"        {"` | — |
| [SRC-FBDC61DA0B-L000134](../../tests/test_tool_execution_status.py#L134) | 134 | `"            \"search_outcome\": \"attempted_no_usable_sources\","` | — |
| [SRC-FBDC61DA0B-L000135](../../tests/test_tool_execution_status.py#L135) | 135 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-FBDC61DA0B-L000136](../../tests/test_tool_execution_status.py#L136) | 136 | `"            \"connector_summary\": {"` | — |
| [SRC-FBDC61DA0B-L000137](../../tests/test_tool_execution_status.py#L137) | 137 | `"                \"connectors\": ["` | — |
| [SRC-FBDC61DA0B-L000138](../../tests/test_tool_execution_status.py#L138) | 138 | `"                    {"` | — |
| [SRC-FBDC61DA0B-L000139](../../tests/test_tool_execution_status.py#L139) | 139 | `"                        \"name\": \"reddit_public_rss\","` | — |
| [SRC-FBDC61DA0B-L000140](../../tests/test_tool_execution_status.py#L140) | 140 | `"                        \"configured\": True,"` | — |
| [SRC-FBDC61DA0B-L000141](../../tests/test_tool_execution_status.py#L141) | 141 | `"                        \"attempted\": True,"` | — |
| [SRC-FBDC61DA0B-L000142](../../tests/test_tool_execution_status.py#L142) | 142 | `"                        \"status\": \"no_results\","` | — |
| [SRC-FBDC61DA0B-L000143](../../tests/test_tool_execution_status.py#L143) | 143 | `"                    }"` | — |
| [SRC-FBDC61DA0B-L000144](../../tests/test_tool_execution_status.py#L144) | 144 | `"                ]"` | — |
| [SRC-FBDC61DA0B-L000145](../../tests/test_tool_execution_status.py#L145) | 145 | `"            },"` | — |
| [SRC-FBDC61DA0B-L000146](../../tests/test_tool_execution_status.py#L146) | 146 | `"        },"` | — |
| [SRC-FBDC61DA0B-L000147](../../tests/test_tool_execution_status.py#L147) | 147 | `"    )"` | — |
| [SRC-FBDC61DA0B-L000148](../../tests/test_tool_execution_status.py#L148) | 148 | `"    social = next(row for row in rows if row[\"tool\"] == \"public_social_search_if_configured\")"` | — |
| [SRC-FBDC61DA0B-L000149](../../tests/test_tool_execution_status.py#L149) | 149 | `"    assert social[\"status\"] == \"completed_no_usable_results\""` | — |
## اختبارات

### FILE-F725E90B2A — [tests/test_web_agent.py](../../tests/test_web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-F725E90B2A-L000001](../../tests/test_web_agent.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-F725E90B2A-L000002](../../tests/test_web_agent.py#L2) | 2 | `""` | — |
| [SRC-F725E90B2A-L000003](../../tests/test_web_agent.py#L3) | 3 | `"from pathlib import Path"` | — |
| [SRC-F725E90B2A-L000004](../../tests/test_web_agent.py#L4) | 4 | `""` | — |
| [SRC-F725E90B2A-L000005](../../tests/test_web_agent.py#L5) | 5 | `"import pytest"` | — |
| [SRC-F725E90B2A-L000006](../../tests/test_web_agent.py#L6) | 6 | `""` | — |
| [SRC-F725E90B2A-L000007](../../tests/test_web_agent.py#L7) | 7 | `"from agents.research import compact_search_query"` | — |
| [SRC-F725E90B2A-L000008](../../tests/test_web_agent.py#L8) | 8 | `"from agents.request_budget import RequestBudgetExceeded"` | — |
| [SRC-F725E90B2A-L000009](../../tests/test_web_agent.py#L9) | 9 | `"from agents.web_agent import ("` | — |
| [SRC-F725E90B2A-L000010](../../tests/test_web_agent.py#L10) | 10 | `"    WebAgent,"` | — |
| [SRC-F725E90B2A-L000011](../../tests/test_web_agent.py#L11) | 11 | `"    _minimum_relevance_ratio,"` | — |
| [SRC-F725E90B2A-L000012](../../tests/test_web_agent.py#L12) | 12 | `"    _normalize_search_query,"` | — |
| [SRC-F725E90B2A-L000013](../../tests/test_web_agent.py#L13) | 13 | `"    _public_http_url,"` | — |
| [SRC-F725E90B2A-L000014](../../tests/test_web_agent.py#L14) | 14 | `"    _relevance_query_tokens,"` | — |
| [SRC-F725E90B2A-L000015](../../tests/test_web_agent.py#L15) | 15 | `"    _relevance_ratio,"` | — |
| [SRC-F725E90B2A-L000016](../../tests/test_web_agent.py#L16) | 16 | `")"` | — |
| [SRC-F725E90B2A-L000017](../../tests/test_web_agent.py#L17) | 17 | `""` | — |
| [SRC-F725E90B2A-L000018](../../tests/test_web_agent.py#L18) | 18 | `""` | — |
| [SRC-F725E90B2A-L000019](../../tests/test_web_agent.py#L19) | 19 | `"def sample_source(index=0):"` | — |
| [SRC-F725E90B2A-L000020](../../tests/test_web_agent.py#L20) | 20 | `"    domain = \"example.com\" if index == 0 else \"example.net\""` | — |
| [SRC-F725E90B2A-L000021](../../tests/test_web_agent.py#L21) | 21 | `"    return {"` | — |
| [SRC-F725E90B2A-L000022](../../tests/test_web_agent.py#L22) | 22 | `"        \"title\": \"مقالة عن التقنية\","` | — |
| [SRC-F725E90B2A-L000023](../../tests/test_web_agent.py#L23) | 23 | `"        \"url\": f\"https://{domain}/research\","` | — |
| [SRC-F725E90B2A-L000024](../../tests/test_web_agent.py#L24) | 24 | `"        \"snippet\": \"يشرح هذا المصدر التقنية وسبب المقارنة.\","` | — |
| [SRC-F725E90B2A-L000025](../../tests/test_web_agent.py#L25) | 25 | `"        \"page_text\": \"نص مستخرج من الصفحة يشرح التقنية وأسباب المقارنة.\","` | — |
| [SRC-F725E90B2A-L000026](../../tests/test_web_agent.py#L26) | 26 | `"        \"page_fetched\": True,"` | — |
| [SRC-F725E90B2A-L000027](../../tests/test_web_agent.py#L27) | 27 | `"        \"providers\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L000028](../../tests/test_web_agent.py#L28) | 28 | `"        \"queries\": [\"قارن هذه التقنية\"],"` | — |
| [SRC-F725E90B2A-L000029](../../tests/test_web_agent.py#L29) | 29 | `"        \"domain\": domain,"` | — |
| [SRC-F725E90B2A-L000030](../../tests/test_web_agent.py#L30) | 30 | `"        \"source_class\": \"general\","` | — |
| [SRC-F725E90B2A-L000031](../../tests/test_web_agent.py#L31) | 31 | `"        \"platform\": \"web\","` | — |
| [SRC-F725E90B2A-L000032](../../tests/test_web_agent.py#L32) | 32 | `"    }"` | — |
| [SRC-F725E90B2A-L000033](../../tests/test_web_agent.py#L33) | 33 | `""` | — |
| [SRC-F725E90B2A-L000034](../../tests/test_web_agent.py#L34) | 34 | `""` | — |
| [SRC-F725E90B2A-L000035](../../tests/test_web_agent.py#L35) | 35 | `"def test_agent_synthesizes_with_sources_without_live_network(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000036](../../tests/test_web_agent.py#L36) | 36 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000037](../../tests/test_web_agent.py#L37) | 37 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L000038](../../tests/test_web_agent.py#L38) | 38 | `"    seen = {}"` | — |
| [SRC-F725E90B2A-L000039](../../tests/test_web_agent.py#L39) | 39 | `""` | — |
| [SRC-F725E90B2A-L000040](../../tests/test_web_agent.py#L40) | 40 | `"    def plan(question, history):"` | — |
| [SRC-F725E90B2A-L000041](../../tests/test_web_agent.py#L41) | 41 | `"        return {"` | — |
| [SRC-F725E90B2A-L000042](../../tests/test_web_agent.py#L42) | 42 | `"            \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L000043](../../tests/test_web_agent.py#L43) | 43 | `"            \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L000044](../../tests/test_web_agent.py#L44) | 44 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L000045](../../tests/test_web_agent.py#L45) | 45 | `"            \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L000046](../../tests/test_web_agent.py#L46) | 46 | `"            \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L000047](../../tests/test_web_agent.py#L47) | 47 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L000048](../../tests/test_web_agent.py#L48) | 48 | `"        }"` | — |
| [SRC-F725E90B2A-L000049](../../tests/test_web_agent.py#L49) | 49 | `""` | — |
| [SRC-F725E90B2A-L000050](../../tests/test_web_agent.py#L50) | 50 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L000051](../../tests/test_web_agent.py#L51) | 51 | `"        seen[\"plan\"] = research_plan"` | — |
| [SRC-F725E90B2A-L000052](../../tests/test_web_agent.py#L52) | 52 | `"        return [sample_source(0), sample_source(1)], [], {"` | — |
| [SRC-F725E90B2A-L000053](../../tests/test_web_agent.py#L53) | 53 | `"            \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L000054](../../tests/test_web_agent.py#L54) | 54 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L000055](../../tests/test_web_agent.py#L55) | 55 | `"            \"query_results\": [{\"query\": research_plan[\"queries\"][0], \"results\": 1}],"` | — |
| [SRC-F725E90B2A-L000056](../../tests/test_web_agent.py#L56) | 56 | `"            \"unique_sources\": 2,"` | — |
| [SRC-F725E90B2A-L000057](../../tests/test_web_agent.py#L57) | 57 | `"            \"pages_fetched\": 2,"` | — |
| [SRC-F725E90B2A-L000058](../../tests/test_web_agent.py#L58) | 58 | `"            \"providers_used\": [\"test\"],"` | — |
| [SRC-F725E90B2A-L000059](../../tests/test_web_agent.py#L59) | 59 | `"            \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L000060](../../tests/test_web_agent.py#L60) | 60 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L000061](../../tests/test_web_agent.py#L61) | 61 | `"            \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L000062](../../tests/test_web_agent.py#L62) | 62 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L000063](../../tests/test_web_agent.py#L63) | 63 | `"        }"` | — |
| [SRC-F725E90B2A-L000064](../../tests/test_web_agent.py#L64) | 64 | `""` | — |
| [SRC-F725E90B2A-L000065](../../tests/test_web_agent.py#L65) | 65 | `"    def generate(question, history, sources, search_warning, research_plan=None, search_report=None):"` | — |
| [SRC-F725E90B2A-L000066](../../tests/test_web_agent.py#L66) | 66 | `"        seen[\"question\"] = question"` | — |
| [SRC-F725E90B2A-L000067](../../tests/test_web_agent.py#L67) | 67 | `"        seen[\"history\"] = history"` | — |
| [SRC-F725E90B2A-L000068](../../tests/test_web_agent.py#L68) | 68 | `"        seen[\"sources\"] = sources"` | — |
| [SRC-F725E90B2A-L000069](../../tests/test_web_agent.py#L69) | 69 | `"        seen[\"report\"] = search_report"` | — |
| [SRC-F725E90B2A-L000070](../../tests/test_web_agent.py#L70) | 70 | `"        return \"الإجابة: التقنية مناسبة للأسباب التالية [المصدر 1].\""` | — |
| [SRC-F725E90B2A-L000071](../../tests/test_web_agent.py#L71) | 71 | `""` | — |
| [SRC-F725E90B2A-L000072](../../tests/test_web_agent.py#L72) | 72 | `"    monkeypatch.setattr(agent, \"_plan_search\", plan)"` | — |
| [SRC-F725E90B2A-L000073](../../tests/test_web_agent.py#L73) | 73 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L000074](../../tests/test_web_agent.py#L74) | 74 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L000075](../../tests/test_web_agent.py#L75) | 75 | `"    monkeypatch.setattr(agent, \"_generate\", generate)"` | — |
| [SRC-F725E90B2A-L000076](../../tests/test_web_agent.py#L76) | 76 | `"    result = agent.answer("` | — |
| [SRC-F725E90B2A-L000077](../../tests/test_web_agent.py#L77) | 77 | `"        \"قارن هذه التقنية\","` | — |
| [SRC-F725E90B2A-L000078](../../tests/test_web_agent.py#L78) | 78 | `"        history=[{\"role\": \"user\", \"content\": \"ما هي التقنية؟\"}],"` | — |
| [SRC-F725E90B2A-L000079](../../tests/test_web_agent.py#L79) | 79 | `"    )"` | — |
| [SRC-F725E90B2A-L000080](../../tests/test_web_agent.py#L80) | 80 | `""` | — |
| [SRC-F725E90B2A-L000081](../../tests/test_web_agent.py#L81) | 81 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-F725E90B2A-L000082](../../tests/test_web_agent.py#L82) | 82 | `"    assert result[\"search_attempted\"] is True"` | — |
| [SRC-F725E90B2A-L000083](../../tests/test_web_agent.py#L83) | 83 | `"    assert result[\"search_report\"][\"search_attempted\"] is True"` | — |
| [SRC-F725E90B2A-L000084](../../tests/test_web_agent.py#L84) | 84 | `"    assert result[\"search_report\"][\"search_outcome\"] == \"attempted_with_usable_sources\""` | — |
| [SRC-F725E90B2A-L000085](../../tests/test_web_agent.py#L85) | 85 | `"    assert result[\"search_report\"][\"pipeline_completion_status\"] == \"completed\""` | — |
| [SRC-F725E90B2A-L000086](../../tests/test_web_agent.py#L86) | 86 | `"    assert result[\"search_report\"][\"completion_stages\"][\"semantic_fact_check\"] == \"not_performed\""` | — |
| [SRC-F725E90B2A-L000087](../../tests/test_web_agent.py#L87) | 87 | `"    assert result[\"search_report\"][\"research_quality_semantics\"] == ("` | — |
| [SRC-F725E90B2A-L000088](../../tests/test_web_agent.py#L88) | 88 | `"        \"process_coverage_not_factual_probability\""` | — |
| [SRC-F725E90B2A-L000089](../../tests/test_web_agent.py#L89) | 89 | `"    )"` | — |
| [SRC-F725E90B2A-L000090](../../tests/test_web_agent.py#L90) | 90 | `"    assert result[\"search_report\"][\"claim_audit_semantics\"] == ("` | — |
| [SRC-F725E90B2A-L000091](../../tests/test_web_agent.py#L91) | 91 | `"        \"model_assisted_not_independent_fact_check\""` | — |
| [SRC-F725E90B2A-L000092](../../tests/test_web_agent.py#L92) | 92 | `"    )"` | — |
| [SRC-F725E90B2A-L000093](../../tests/test_web_agent.py#L93) | 93 | `"    assert result[\"search_report\"][\"distinct_registrable_domains\"] == 2"` | — |
| [SRC-F725E90B2A-L000094](../../tests/test_web_agent.py#L94) | 94 | `"    assert result[\"search_report\"][\"editorial_independence_status\"] == \"not_assessed\""` | — |
| [SRC-F725E90B2A-L000095](../../tests/test_web_agent.py#L95) | 95 | `"    assert result[\"search_report\"][\"independent_sources_field_semantics\"] == ("` | — |
| [SRC-F725E90B2A-L000096](../../tests/test_web_agent.py#L96) | 96 | `"        \"legacy_compatibility_alias_for_distinct_registrable_domain_count\""` | — |
| [SRC-F725E90B2A-L000097](../../tests/test_web_agent.py#L97) | 97 | `"    )"` | — |
| [SRC-F725E90B2A-L000098](../../tests/test_web_agent.py#L98) | 98 | `"    assert any(\"تعدد النطاقات المسجلة لا يثبت الاستقلال التحريري\" in warning"` | — |
| [SRC-F725E90B2A-L000099](../../tests/test_web_agent.py#L99) | 99 | `"               for warning in result[\"warnings\"])"` | — |
| [SRC-F725E90B2A-L000100](../../tests/test_web_agent.py#L100) | 100 | `"    assert result[\"used_language_model\"] is True"` | — |
| [SRC-F725E90B2A-L000101](../../tests/test_web_agent.py#L101) | 101 | `"    task_understanding = result[\"task_understanding\"]"` | — |
| [SRC-F725E90B2A-L000102](../../tests/test_web_agent.py#L102) | 102 | `"    assert task_understanding[\"task_spec\"][\"schema\"] == \"omarai.task_spec.v1\""` | — |
| [SRC-F725E90B2A-L000103](../../tests/test_web_agent.py#L103) | 103 | `"    assert task_understanding[\"task_spec\"][\"task_family\"] == \"compare\""` | — |
| [SRC-F725E90B2A-L000104](../../tests/test_web_agent.py#L104) | 104 | `"    assert task_understanding[\"task_spec\"][\"classification_is_probability\"] is False"` | — |
| [SRC-F725E90B2A-L000105](../../tests/test_web_agent.py#L105) | 105 | `"    assert task_understanding[\"tool_execution\"][\"search_outcome\"] == \"attempted_with_usable_sources\""` | — |
| [SRC-F725E90B2A-L000106](../../tests/test_web_agent.py#L106) | 106 | `"    assert task_understanding[\"tool_execution\"][\"accepted_source_count\"] == 2"` | — |
| [SRC-F725E90B2A-L000107](../../tests/test_web_agent.py#L107) | 107 | `"    assert task_understanding[\"query_strategy_matrix\"]"` | — |
| [SRC-F725E90B2A-L000108](../../tests/test_web_agent.py#L108) | 108 | `"    assert task_understanding[\"actual_queries\"] == result[\"search_queries\"]"` | — |
| [SRC-F725E90B2A-L000109](../../tests/test_web_agent.py#L109) | 109 | `"    assert result[\"search_report\"][\"task_understanding\"][\"task_spec\"][\"schema\"] == \"omarai.task_spec.v1\""` | — |
| [SRC-F725E90B2A-L000110](../../tests/test_web_agent.py#L110) | 110 | `"    assert result[\"sources\"][0][\"url\"] == \"https://example.com/research\""` | — |
| [SRC-F725E90B2A-L000111](../../tests/test_web_agent.py#L111) | 111 | `"    assert \"[المصدر 1]\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L000112](../../tests/test_web_agent.py#L112) | 112 | `"    assert seen[\"question\"] == \"قارن هذه التقنية\""` | — |
| [SRC-F725E90B2A-L000113](../../tests/test_web_agent.py#L113) | 113 | `"    assert seen[\"history\"] == [{\"role\": \"user\", \"content\": \"ما هي التقنية؟\"}]"` | — |
| [SRC-F725E90B2A-L000114](../../tests/test_web_agent.py#L114) | 114 | `""` | — |
| [SRC-F725E90B2A-L000115](../../tests/test_web_agent.py#L115) | 115 | `""` | — |
| [SRC-F725E90B2A-L000116](../../tests/test_web_agent.py#L116) | 116 | `"def test_agent_returns_search_snippets_if_model_not_configured(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000117](../../tests/test_web_agent.py#L117) | 117 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000118](../../tests/test_web_agent.py#L118) | 118 | `"    agent.api_key = \"\""` | — |
| [SRC-F725E90B2A-L000119](../../tests/test_web_agent.py#L119) | 119 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L000120](../../tests/test_web_agent.py#L120) | 120 | `"        agent,"` | — |
| [SRC-F725E90B2A-L000121](../../tests/test_web_agent.py#L121) | 121 | `"        \"_collect_research\","` | — |
| [SRC-F725E90B2A-L000122](../../tests/test_web_agent.py#L122) | 122 | `"        lambda plan: ("` | — |
| [SRC-F725E90B2A-L000123](../../tests/test_web_agent.py#L123) | 123 | `"            [sample_source(0), sample_source(1)],"` | — |
| [SRC-F725E90B2A-L000124](../../tests/test_web_agent.py#L124) | 124 | `"            [],"` | — |
| [SRC-F725E90B2A-L000125](../../tests/test_web_agent.py#L125) | 125 | `"            {"` | — |
| [SRC-F725E90B2A-L000126](../../tests/test_web_agent.py#L126) | 126 | `"                \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L000127](../../tests/test_web_agent.py#L127) | 127 | `"                \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L000128](../../tests/test_web_agent.py#L128) | 128 | `"                \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L000129](../../tests/test_web_agent.py#L129) | 129 | `"                \"unique_sources\": 2,"` | — |
| [SRC-F725E90B2A-L000130](../../tests/test_web_agent.py#L130) | 130 | `"                \"pages_fetched\": 2,"` | — |
| [SRC-F725E90B2A-L000131](../../tests/test_web_agent.py#L131) | 131 | `"                \"providers_used\": [\"test\"],"` | — |
| [SRC-F725E90B2A-L000132](../../tests/test_web_agent.py#L132) | 132 | `"                \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L000133](../../tests/test_web_agent.py#L133) | 133 | `"                \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L000134](../../tests/test_web_agent.py#L134) | 134 | `"                \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L000135](../../tests/test_web_agent.py#L135) | 135 | `"                \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L000136](../../tests/test_web_agent.py#L136) | 136 | `"            },"` | — |
| [SRC-F725E90B2A-L000137](../../tests/test_web_agent.py#L137) | 137 | `"        ),"` | — |
| [SRC-F725E90B2A-L000138](../../tests/test_web_agent.py#L138) | 138 | `"    )"` | — |
| [SRC-F725E90B2A-L000139](../../tests/test_web_agent.py#L139) | 139 | `""` | — |
| [SRC-F725E90B2A-L000140](../../tests/test_web_agent.py#L140) | 140 | `"    result = agent.answer(\"ما الذي يقوله المصدر؟\")"` | — |
| [SRC-F725E90B2A-L000141](../../tests/test_web_agent.py#L141) | 141 | `""` | — |
| [SRC-F725E90B2A-L000142](../../tests/test_web_agent.py#L142) | 142 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-F725E90B2A-L000143](../../tests/test_web_agent.py#L143) | 143 | `"    assert result[\"used_language_model\"] is False"` | — |
| [SRC-F725E90B2A-L000144](../../tests/test_web_agent.py#L144) | 144 | `"    assert result[\"search_report\"][\"pipeline_completion_status\"] == \"partial\""` | — |
| [SRC-F725E90B2A-L000145](../../tests/test_web_agent.py#L145) | 145 | `"    assert result[\"search_report\"][\"completion_stages\"][\"claim_review\"] == \"not_run\""` | — |
| [SRC-F725E90B2A-L000146](../../tests/test_web_agent.py#L146) | 146 | `"    assert \"OPENROUTER_API_KEY\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L000147](../../tests/test_web_agent.py#L147) | 147 | `"    assert result[\"sources\"][0][\"page_fetched\"] is True"` | — |
| [SRC-F725E90B2A-L000148](../../tests/test_web_agent.py#L148) | 148 | `""` | — |
| [SRC-F725E90B2A-L000149](../../tests/test_web_agent.py#L149) | 149 | `""` | — |
| [SRC-F725E90B2A-L000150](../../tests/test_web_agent.py#L150) | 150 | `"def test_agent_rejects_empty_or_oversized_question():"` | — |
| [SRC-F725E90B2A-L000151](../../tests/test_web_agent.py#L151) | 151 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000152](../../tests/test_web_agent.py#L152) | 152 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-F725E90B2A-L000153](../../tests/test_web_agent.py#L153) | 153 | `"        agent.answer(\"   \")"` | — |
| [SRC-F725E90B2A-L000154](../../tests/test_web_agent.py#L154) | 154 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-F725E90B2A-L000155](../../tests/test_web_agent.py#L155) | 155 | `"        agent.answer(\"س\" * 4001)"` | — |
| [SRC-F725E90B2A-L000156](../../tests/test_web_agent.py#L156) | 156 | `""` | — |
| [SRC-F725E90B2A-L000157](../../tests/test_web_agent.py#L157) | 157 | `""` | — |
| [SRC-F725E90B2A-L000158](../../tests/test_web_agent.py#L158) | 158 | `"def test_history_search_query_expands_short_follow_up():"` | — |
| [SRC-F725E90B2A-L000159](../../tests/test_web_agent.py#L159) | 159 | `"    history = [{\"role\": \"user\", \"content\": \"قارن أسعار السيارات الكهربائية في مصر\"}]"` | — |
| [SRC-F725E90B2A-L000160](../../tests/test_web_agent.py#L160) | 160 | `"    query = WebAgent._history_search_query(\"والسعر؟\", history)"` | — |
| [SRC-F725E90B2A-L000161](../../tests/test_web_agent.py#L161) | 161 | `"    assert \"السيارات الكهربائية\" in query"` | — |
| [SRC-F725E90B2A-L000162](../../tests/test_web_agent.py#L162) | 162 | `"    assert \"والسعر؟\" in query"` | — |
| [SRC-F725E90B2A-L000163](../../tests/test_web_agent.py#L163) | 163 | `""` | — |
| [SRC-F725E90B2A-L000164](../../tests/test_web_agent.py#L164) | 164 | `""` | — |
| [SRC-F725E90B2A-L000165](../../tests/test_web_agent.py#L165) | 165 | `"def test_public_url_filter_rejects_local_and_credential_urls():"` | — |
| [SRC-F725E90B2A-L000166](../../tests/test_web_agent.py#L166) | 166 | `"    assert _public_http_url(\"http://127.0.0.1/admin\") is None"` | — |
| [SRC-F725E90B2A-L000167](../../tests/test_web_agent.py#L167) | 167 | `"    assert _public_http_url(\"http://localhost:8000/\") is None"` | — |
| [SRC-F725E90B2A-L000168](../../tests/test_web_agent.py#L168) | 168 | `"    assert _public_http_url(\"https://user:pass@example.com/private\") is None"` | — |
| [SRC-F725E90B2A-L000169](../../tests/test_web_agent.py#L169) | 169 | `"    assert _public_http_url(\"file:///etc/passwd\") is None"` | — |
| [SRC-F725E90B2A-L000170](../../tests/test_web_agent.py#L170) | 170 | `""` | — |
| [SRC-F725E90B2A-L000171](../../tests/test_web_agent.py#L171) | 171 | `""` | — |
| [SRC-F725E90B2A-L000172](../../tests/test_web_agent.py#L172) | 172 | `"def test_public_url_filter_accepts_basic_https_url():"` | — |
| [SRC-F725E90B2A-L000173](../../tests/test_web_agent.py#L173) | 173 | `"    assert _public_http_url(\"https://example.com/path#section\") == \"https://example.com/path\""` | — |
| [SRC-F725E90B2A-L000174](../../tests/test_web_agent.py#L174) | 174 | `""` | — |
| [SRC-F725E90B2A-L000175](../../tests/test_web_agent.py#L175) | 175 | `""` | — |
| [SRC-F725E90B2A-L000176](../../tests/test_web_agent.py#L176) | 176 | `"def test_search_web_parses_duckduckgo_and_bing_without_ddgs(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000177](../../tests/test_web_agent.py#L177) | 177 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L000178](../../tests/test_web_agent.py#L178) | 178 | `""` | — |
| [SRC-F725E90B2A-L000179](../../tests/test_web_agent.py#L179) | 179 | `"    html = \"\"\""` | — |
| [SRC-F725E90B2A-L000180](../../tests/test_web_agent.py#L180) | 180 | `"    <html><body>"` | — |
| [SRC-F725E90B2A-L000181](../../tests/test_web_agent.py#L181) | 181 | `"      <div class=\"result\">"` | — |
| [SRC-F725E90B2A-L000182](../../tests/test_web_agent.py#L182) | 182 | `"        <a class=\"result__a\" href=\"https://example.com/first\">صفحة أولى</a>"` | — |
| [SRC-F725E90B2A-L000183](../../tests/test_web_agent.py#L183) | 183 | `"        <a class=\"result__snippet\">سؤال بحث تجريبي مقتطف أول</a>"` | — |
| [SRC-F725E90B2A-L000184](../../tests/test_web_agent.py#L184) | 184 | `"      </div>"` | — |
| [SRC-F725E90B2A-L000185](../../tests/test_web_agent.py#L185) | 185 | `"    </body></html>"` | — |
| [SRC-F725E90B2A-L000186](../../tests/test_web_agent.py#L186) | 186 | `"    \"\"\""` | — |
| [SRC-F725E90B2A-L000187](../../tests/test_web_agent.py#L187) | 187 | `"    rss = \"\"\""` | — |
| [SRC-F725E90B2A-L000188](../../tests/test_web_agent.py#L188) | 188 | `"    <rss><channel><item>"` | — |
| [SRC-F725E90B2A-L000189](../../tests/test_web_agent.py#L189) | 189 | `"      <title>صفحة ثانية</title>"` | — |
| [SRC-F725E90B2A-L000190](../../tests/test_web_agent.py#L190) | 190 | `"      <link>https://example.net/second</link>"` | — |
| [SRC-F725E90B2A-L000191](../../tests/test_web_agent.py#L191) | 191 | `"      <description>سؤال بحث تجريبي مقتطف ثاني</description>"` | — |
| [SRC-F725E90B2A-L000192](../../tests/test_web_agent.py#L192) | 192 | `"    </item></channel></rss>"` | — |
| [SRC-F725E90B2A-L000193](../../tests/test_web_agent.py#L193) | 193 | `"    \"\"\""` | — |
| [SRC-F725E90B2A-L000194](../../tests/test_web_agent.py#L194) | 194 | `""` | — |
| [SRC-F725E90B2A-L000195](../../tests/test_web_agent.py#L195) | 195 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000196](../../tests/test_web_agent.py#L196) | 196 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L000197](../../tests/test_web_agent.py#L197) | 197 | `""` | — |
| [SRC-F725E90B2A-L000198](../../tests/test_web_agent.py#L198) | 198 | `"        def __init__(self, text):"` | — |
