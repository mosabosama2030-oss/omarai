# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **033**
- سجلات الأسطر: **800**
- النطاق: SRC-6A7519AC10-L000044 إلى SRC-B3062EB677-L000195
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-6A7519AC10 — [tests/test_answer_quality_comparison.py](../../tests/test_answer_quality_comparison.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6A7519AC10-L000044](../../tests/test_answer_quality_comparison.py#L44) | 44 | `"    }"` | — |
| [SRC-6A7519AC10-L000045](../../tests/test_answer_quality_comparison.py#L45) | 45 | `"    if cost is not None:"` | — |
| [SRC-6A7519AC10-L000046](../../tests/test_answer_quality_comparison.py#L46) | 46 | `"        row[\"provider_reported_model_cost_usd\"] = cost"` | — |
| [SRC-6A7519AC10-L000047](../../tests/test_answer_quality_comparison.py#L47) | 47 | `"    if request_cost is not None:"` | — |
| [SRC-6A7519AC10-L000048](../../tests/test_answer_quality_comparison.py#L48) | 48 | `"        row[\"request_cost_usd\"] = request_cost"` | — |
| [SRC-6A7519AC10-L000049](../../tests/test_answer_quality_comparison.py#L49) | 49 | `"    return row"` | — |
| [SRC-6A7519AC10-L000050](../../tests/test_answer_quality_comparison.py#L50) | 50 | `""` | — |
| [SRC-6A7519AC10-L000051](../../tests/test_answer_quality_comparison.py#L51) | 51 | `""` | — |
| [SRC-6A7519AC10-L000052](../../tests/test_answer_quality_comparison.py#L52) | 52 | `"def _reviews(*, correct: int, supported_citations: int) -> dict:"` | — |
| [SRC-6A7519AC10-L000053](../../tests/test_answer_quality_comparison.py#L53) | 53 | `"    corpus = json.loads(CORPUS_PATH.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-6A7519AC10-L000054](../../tests/test_answer_quality_comparison.py#L54) | 54 | `"    return {"` | — |
| [SRC-6A7519AC10-L000055](../../tests/test_answer_quality_comparison.py#L55) | 55 | `"        \"schema_version\": \"1.0\","` | — |
| [SRC-6A7519AC10-L000056](../../tests/test_answer_quality_comparison.py#L56) | 56 | `"        \"reviews\": ["` | — |
| [SRC-6A7519AC10-L000057](../../tests/test_answer_quality_comparison.py#L57) | 57 | `"            {"` | — |
| [SRC-6A7519AC10-L000058](../../tests/test_answer_quality_comparison.py#L58) | 58 | `"                \"case_id\": case[\"case_id\"],"` | — |
| [SRC-6A7519AC10-L000059](../../tests/test_answer_quality_comparison.py#L59) | 59 | `"                \"status\": \"REVIEWED\","` | — |
| [SRC-6A7519AC10-L000060](../../tests/test_answer_quality_comparison.py#L60) | 60 | `"                \"retrieval\": {"` | — |
| [SRC-6A7519AC10-L000061](../../tests/test_answer_quality_comparison.py#L61) | 61 | `"                    \"relevant_retrieved\": 2 if case[\"case_id\"] == \"AQ-007\" else 1,"` | — |
| [SRC-6A7519AC10-L000062](../../tests/test_answer_quality_comparison.py#L62) | 62 | `"                    \"retrieved_count\": 3,"` | — |
| [SRC-6A7519AC10-L000063](../../tests/test_answer_quality_comparison.py#L63) | 63 | `"                    \"relevant_available\": 3 if case[\"case_id\"] == \"AQ-007\" else 2,"` | — |
| [SRC-6A7519AC10-L000064](../../tests/test_answer_quality_comparison.py#L64) | 64 | `"                },"` | — |
| [SRC-6A7519AC10-L000065](../../tests/test_answer_quality_comparison.py#L65) | 65 | `"                \"faithfulness\": {\"supported_claims\": correct, \"reviewed_claims\": 3},"` | — |
| [SRC-6A7519AC10-L000066](../../tests/test_answer_quality_comparison.py#L66) | 66 | `"                \"correctness\": {\"correct_facts\": correct, \"reviewed_facts\": 3},"` | — |
| [SRC-6A7519AC10-L000067](../../tests/test_answer_quality_comparison.py#L67) | 67 | `"                \"citations\": {"` | — |
| [SRC-6A7519AC10-L000068](../../tests/test_answer_quality_comparison.py#L68) | 68 | `"                    \"supported_citations\": supported_citations,"` | — |
| [SRC-6A7519AC10-L000069](../../tests/test_answer_quality_comparison.py#L69) | 69 | `"                    \"reviewed_citations\": 2,"` | — |
| [SRC-6A7519AC10-L000070](../../tests/test_answer_quality_comparison.py#L70) | 70 | `"                },"` | — |
| [SRC-6A7519AC10-L000071](../../tests/test_answer_quality_comparison.py#L71) | 71 | `"                \"writing_quality\": 4,"` | — |
| [SRC-6A7519AC10-L000072](../../tests/test_answer_quality_comparison.py#L72) | 72 | `"            }"` | — |
| [SRC-6A7519AC10-L000073](../../tests/test_answer_quality_comparison.py#L73) | 73 | `"            for case in corpus[\"cases\"]"` | — |
| [SRC-6A7519AC10-L000074](../../tests/test_answer_quality_comparison.py#L74) | 74 | `"        ],"` | — |
| [SRC-6A7519AC10-L000075](../../tests/test_answer_quality_comparison.py#L75) | 75 | `"    }"` | — |
| [SRC-6A7519AC10-L000076](../../tests/test_answer_quality_comparison.py#L76) | 76 | `""` | — |
| [SRC-6A7519AC10-L000077](../../tests/test_answer_quality_comparison.py#L77) | 77 | `""` | — |
| [SRC-6A7519AC10-L000078](../../tests/test_answer_quality_comparison.py#L78) | 78 | `"def _full_run(*, build_sha: str, candidate: bool) -> dict:"` | — |
| [SRC-6A7519AC10-L000079](../../tests/test_answer_quality_comparison.py#L79) | 79 | `"    corpus = json.loads(CORPUS_PATH.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-6A7519AC10-L000080](../../tests/test_answer_quality_comparison.py#L80) | 80 | `"    rows = []"` | — |
| [SRC-6A7519AC10-L000081](../../tests/test_answer_quality_comparison.py#L81) | 81 | `"    for case in corpus[\"cases\"]:"` | — |
| [SRC-6A7519AC10-L000082](../../tests/test_answer_quality_comparison.py#L82) | 82 | `"        case_id = case[\"case_id\"]"` | — |
| [SRC-6A7519AC10-L000083](../../tests/test_answer_quality_comparison.py#L83) | 83 | `"        is_aq007 = case_id == \"AQ-007\""` | — |
| [SRC-6A7519AC10-L000084](../../tests/test_answer_quality_comparison.py#L84) | 84 | `"        is_aq008 = case_id == \"AQ-008\""` | — |
| [SRC-6A7519AC10-L000085](../../tests/test_answer_quality_comparison.py#L85) | 85 | `"        if candidate:"` | — |
| [SRC-6A7519AC10-L000086](../../tests/test_answer_quality_comparison.py#L86) | 86 | `"            latency = 80 if is_aq007 else 120 if is_aq008 else 100"` | — |
| [SRC-6A7519AC10-L000087](../../tests/test_answer_quality_comparison.py#L87) | 87 | `"            status = \"SUCCESS_WITH_USABLE_RESULTS\""` | — |
| [SRC-6A7519AC10-L000088](../../tests/test_answer_quality_comparison.py#L88) | 88 | `"            model_cost = 0.005 if is_aq007 else 0.002 if is_aq008 else None"` | — |
| [SRC-6A7519AC10-L000089](../../tests/test_answer_quality_comparison.py#L89) | 89 | `"            request_cost = 0.007 if is_aq007 else 0.009 if is_aq008 else 0.001"` | — |
| [SRC-6A7519AC10-L000090](../../tests/test_answer_quality_comparison.py#L90) | 90 | `"        else:"` | — |
| [SRC-6A7519AC10-L000091](../../tests/test_answer_quality_comparison.py#L91) | 91 | `"            latency = 100 if is_aq007 else 200 if is_aq008 else 150"` | — |
| [SRC-6A7519AC10-L000092](../../tests/test_answer_quality_comparison.py#L92) | 92 | `"            status = \"SUCCESS_WITH_USABLE_RESULTS\" if is_aq007 else \"ATTEMPTED_NO_USABLE_RESULTS\""` | — |
| [SRC-6A7519AC10-L000093](../../tests/test_answer_quality_comparison.py#L93) | 93 | `"            model_cost = 0.01 if is_aq007 else None"` | — |
| [SRC-6A7519AC10-L000094](../../tests/test_answer_quality_comparison.py#L94) | 94 | `"            request_cost = 0.012 if is_aq007 else 0.015 if is_aq008 else 0.001"` | — |
| [SRC-6A7519AC10-L000095](../../tests/test_answer_quality_comparison.py#L95) | 95 | `"        rows.append(_row("` | — |
| [SRC-6A7519AC10-L000096](../../tests/test_answer_quality_comparison.py#L96) | 96 | `"            case_id, latency=latency, tool_status=status,"` | — |
| [SRC-6A7519AC10-L000097](../../tests/test_answer_quality_comparison.py#L97) | 97 | `"            cost=model_cost, request_cost=request_cost,"` | — |
| [SRC-6A7519AC10-L000098](../../tests/test_answer_quality_comparison.py#L98) | 98 | `"        ))"` | — |
| [SRC-6A7519AC10-L000099](../../tests/test_answer_quality_comparison.py#L99) | 99 | `"    return _run(build_sha=build_sha, results=rows)"` | — |
| [SRC-6A7519AC10-L000100](../../tests/test_answer_quality_comparison.py#L100) | 100 | `""` | — |
| [SRC-6A7519AC10-L000101](../../tests/test_answer_quality_comparison.py#L101) | 101 | `""` | — |
| [SRC-6A7519AC10-L000102](../../tests/test_answer_quality_comparison.py#L102) | 102 | `"def test_comparison_measures_latency_tools_cost_and_human_reviewed_quality():"` | — |
| [SRC-6A7519AC10-L000103](../../tests/test_answer_quality_comparison.py#L103) | 103 | `"    mod = load_module()"` | — |
| [SRC-6A7519AC10-L000104](../../tests/test_answer_quality_comparison.py#L104) | 104 | `"    baseline = _full_run(build_sha=\"a\" * 40, candidate=False)"` | — |
| [SRC-6A7519AC10-L000105](../../tests/test_answer_quality_comparison.py#L105) | 105 | `"    candidate = _full_run(build_sha=\"b\" * 40, candidate=True)"` | — |
| [SRC-6A7519AC10-L000106](../../tests/test_answer_quality_comparison.py#L106) | 106 | `"    corpus = mod.load_json_object(CORPUS_PATH)"` | — |
| [SRC-6A7519AC10-L000107](../../tests/test_answer_quality_comparison.py#L107) | 107 | `"    result = mod.compare_runs("` | — |
| [SRC-6A7519AC10-L000108](../../tests/test_answer_quality_comparison.py#L108) | 108 | `"        baseline,"` | — |
| [SRC-6A7519AC10-L000109](../../tests/test_answer_quality_comparison.py#L109) | 109 | `"        candidate,"` | — |
| [SRC-6A7519AC10-L000110](../../tests/test_answer_quality_comparison.py#L110) | 110 | `"        corpus=corpus,"` | — |
| [SRC-6A7519AC10-L000111](../../tests/test_answer_quality_comparison.py#L111) | 111 | `"        baseline_reviews=_reviews(correct=2, supported_citations=1),"` | — |
| [SRC-6A7519AC10-L000112](../../tests/test_answer_quality_comparison.py#L112) | 112 | `"        candidate_reviews=_reviews(correct=3, supported_citations=2),"` | — |
| [SRC-6A7519AC10-L000113](../../tests/test_answer_quality_comparison.py#L113) | 113 | `"    )"` | — |
| [SRC-6A7519AC10-L000114](../../tests/test_answer_quality_comparison.py#L114) | 114 | `"    assert result[\"acceptance_status\"] == \"COMPARABLE_WITH_REVIEWED_QUALITY_AND_BUILD_IDENTITIES\""` | — |
| [SRC-6A7519AC10-L000115](../../tests/test_answer_quality_comparison.py#L115) | 115 | `"    assert result[\"case_count\"] == 45"` | — |
| [SRC-6A7519AC10-L000116](../../tests/test_answer_quality_comparison.py#L116) | 116 | `"    assert result[\"baseline\"][\"metrics\"][\"latency_ms\"][\"p50\"] == 150"` | — |
| [SRC-6A7519AC10-L000117](../../tests/test_answer_quality_comparison.py#L117) | 117 | `"    assert result[\"candidate\"][\"metrics\"][\"latency_ms\"][\"p95\"] == 120"` | — |
| [SRC-6A7519AC10-L000118](../../tests/test_answer_quality_comparison.py#L118) | 118 | `"    assert result[\"runtime_deltas\"][\"usable_result_rate\"][\"baseline\"] == pytest.approx(1 / 45)"` | — |
| [SRC-6A7519AC10-L000119](../../tests/test_answer_quality_comparison.py#L119) | 119 | `"    assert result[\"runtime_deltas\"][\"usable_result_rate\"][\"candidate\"] == 1.0"` | — |
| [SRC-6A7519AC10-L000120](../../tests/test_answer_quality_comparison.py#L120) | 120 | `"    assert result[\"runtime_deltas\"][\"provider_reported_model_cost_usd\"][\"delta\"] == -0.003"` | — |
| [SRC-6A7519AC10-L000121](../../tests/test_answer_quality_comparison.py#L121) | 121 | `"    assert result[\"baseline\"][\"metrics\"][\"provider_reported_model_cost\"][\"complete_request_cost_usd\"] == pytest.approx(0.070)"` | — |
| [SRC-6A7519AC10-L000122](../../tests/test_answer_quality_comparison.py#L122) | 122 | `"    assert result[\"runtime_deltas\"][\"complete_request_cost_usd\"][\"delta\"] == pytest.approx(-0.011)"` | — |
| [SRC-6A7519AC10-L000123](../../tests/test_answer_quality_comparison.py#L123) | 123 | `"    assert result[\"runtime_deltas\"][\"complete_request_cost_usd\"][\"status\"] == \"COMPARED\""` | — |
| [SRC-6A7519AC10-L000124](../../tests/test_answer_quality_comparison.py#L124) | 124 | `"    assert result[\"quality_comparison\"][\"metrics\"][\"factual_accuracy\"][\"baseline\"] == pytest.approx(2 / 3, abs=0.0001)"` | — |
| [SRC-6A7519AC10-L000125](../../tests/test_answer_quality_comparison.py#L125) | 125 | `"    assert result[\"quality_comparison\"][\"metrics\"][\"factual_accuracy\"][\"candidate\"] == 1.0"` | — |
| [SRC-6A7519AC10-L000126](../../tests/test_answer_quality_comparison.py#L126) | 126 | `"    assert result[\"quality_comparison\"][\"metrics\"][\"citation_support\"][\"delta\"] == 0.5"` | — |
| [SRC-6A7519AC10-L000127](../../tests/test_answer_quality_comparison.py#L127) | 127 | `""` | — |
| [SRC-6A7519AC10-L000128](../../tests/test_answer_quality_comparison.py#L128) | 128 | `""` | — |
| [SRC-6A7519AC10-L000129](../../tests/test_answer_quality_comparison.py#L129) | 129 | `"def test_missing_build_sha_and_review_data_cannot_claim_complete_acceptance():"` | — |
| [SRC-6A7519AC10-L000130](../../tests/test_answer_quality_comparison.py#L130) | 130 | `"    mod = load_module()"` | — |
| [SRC-6A7519AC10-L000131](../../tests/test_answer_quality_comparison.py#L131) | 131 | `"    baseline = _run(build_sha=\"unknown\", results=[_row(\"AQ-001\", latency=100, tool_status=\"SUCCESS_WITH_USABLE_RESULTS\", cost=None)])"` | — |
| [SRC-6A7519AC10-L000132](../../tests/test_answer_quality_comparison.py#L132) | 132 | `"    candidate = _run(build_sha=\"\", results=[_row(\"AQ-001\", latency=90, tool_status=\"SUCCESS_WITH_USABLE_RESULTS\", cost=None)])"` | — |
| [SRC-6A7519AC10-L000133](../../tests/test_answer_quality_comparison.py#L133) | 133 | `"    result = mod.compare_runs(baseline, candidate)"` | — |
| [SRC-6A7519AC10-L000134](../../tests/test_answer_quality_comparison.py#L134) | 134 | `"    assert result[\"acceptance_status\"] == \"INCOMPLETE\""` | — |
| [SRC-6A7519AC10-L000135](../../tests/test_answer_quality_comparison.py#L135) | 135 | `"    assert \"baseline_build_sha_missing_or_invalid\" in result[\"acceptance_blockers\"]"` | — |
| [SRC-6A7519AC10-L000136](../../tests/test_answer_quality_comparison.py#L136) | 136 | `"    assert \"candidate_build_sha_missing_or_invalid\" in result[\"acceptance_blockers\"]"` | — |
| [SRC-6A7519AC10-L000137](../../tests/test_answer_quality_comparison.py#L137) | 137 | `"    assert \"human_review_files_missing\" in result[\"acceptance_blockers\"]"` | — |
| [SRC-6A7519AC10-L000138](../../tests/test_answer_quality_comparison.py#L138) | 138 | `"    assert result[\"quality_comparison\"] is None"` | — |
| [SRC-6A7519AC10-L000139](../../tests/test_answer_quality_comparison.py#L139) | 139 | `"    assert result[\"baseline\"][\"metrics\"][\"provider_reported_model_cost\"][\"reported_sum_usd\"] is None"` | — |
| [SRC-6A7519AC10-L000140](../../tests/test_answer_quality_comparison.py#L140) | 140 | `"    assert result[\"runtime_deltas\"][\"provider_reported_model_cost_usd\"][\"status\"] == \"NOT_MEASURED\""` | — |
| [SRC-6A7519AC10-L000141](../../tests/test_answer_quality_comparison.py#L141) | 141 | `""` | — |
| [SRC-6A7519AC10-L000142](../../tests/test_answer_quality_comparison.py#L142) | 142 | `""` | — |
| [SRC-6A7519AC10-L000143](../../tests/test_answer_quality_comparison.py#L143) | 143 | `"def test_comparison_rejects_different_case_sets_and_questions():"` | — |
| [SRC-6A7519AC10-L000144](../../tests/test_answer_quality_comparison.py#L144) | 144 | `"    mod = load_module()"` | — |
| [SRC-6A7519AC10-L000145](../../tests/test_answer_quality_comparison.py#L145) | 145 | `"    baseline = _run(build_sha=\"a\" * 40, results=[_row(\"AQ-007\", latency=100, tool_status=\"SUCCESS_WITH_USABLE_RESULTS\", cost=None)])"` | — |
| [SRC-6A7519AC10-L000146](../../tests/test_answer_quality_comparison.py#L146) | 146 | `"    missing = _run(build_sha=\"b\" * 40, results=[_row(\"AQ-008\", latency=90, tool_status=\"SUCCESS_WITH_USABLE_RESULTS\", cost=None)])"` | — |
| [SRC-6A7519AC10-L000147](../../tests/test_answer_quality_comparison.py#L147) | 147 | `"    with pytest.raises(ValueError, match=\"incomparable case sets\"):"` | — |
| [SRC-6A7519AC10-L000148](../../tests/test_answer_quality_comparison.py#L148) | 148 | `"        mod.compare_runs(baseline, missing)"` | — |
| [SRC-6A7519AC10-L000149](../../tests/test_answer_quality_comparison.py#L149) | 149 | `"    changed_question = _run("` | — |
| [SRC-6A7519AC10-L000150](../../tests/test_answer_quality_comparison.py#L150) | 150 | `"        build_sha=\"b\" * 40,"` | — |
| [SRC-6A7519AC10-L000151](../../tests/test_answer_quality_comparison.py#L151) | 151 | `"        results=[{**_row(\"AQ-007\", latency=90, tool_status=\"SUCCESS_WITH_USABLE_RESULTS\", cost=None), \"prompt\": \"A different prompt\"}],"` | — |
| [SRC-6A7519AC10-L000152](../../tests/test_answer_quality_comparison.py#L152) | 152 | `"    )"` | — |
| [SRC-6A7519AC10-L000153](../../tests/test_answer_quality_comparison.py#L153) | 153 | `"    with pytest.raises(ValueError, match=\"incomparable question text\"):"` | — |
| [SRC-6A7519AC10-L000154](../../tests/test_answer_quality_comparison.py#L154) | 154 | `"        mod.compare_runs(baseline, changed_question)"` | — |
| [SRC-6A7519AC10-L000155](../../tests/test_answer_quality_comparison.py#L155) | 155 | `""` | — |
| [SRC-6A7519AC10-L000156](../../tests/test_answer_quality_comparison.py#L156) | 156 | `""` | — |
| [SRC-6A7519AC10-L000157](../../tests/test_answer_quality_comparison.py#L157) | 157 | `"def test_run_validation_rejects_duplicate_ids_and_invalid_latency():"` | — |
| [SRC-6A7519AC10-L000158](../../tests/test_answer_quality_comparison.py#L158) | 158 | `"    mod = load_module()"` | — |
| [SRC-6A7519AC10-L000159](../../tests/test_answer_quality_comparison.py#L159) | 159 | `"    run = _run("` | — |
| [SRC-6A7519AC10-L000160](../../tests/test_answer_quality_comparison.py#L160) | 160 | `"        build_sha=\"a\" * 40,"` | — |
| [SRC-6A7519AC10-L000161](../../tests/test_answer_quality_comparison.py#L161) | 161 | `"        results=["` | — |
| [SRC-6A7519AC10-L000162](../../tests/test_answer_quality_comparison.py#L162) | 162 | `"            _row(\"AQ-007\", latency=-1, tool_status=\"UNKNOWN\", cost=None),"` | — |
| [SRC-6A7519AC10-L000163](../../tests/test_answer_quality_comparison.py#L163) | 163 | `"            _row(\"AQ-007\", latency=10, tool_status=\"UNKNOWN\", cost=None),"` | — |
| [SRC-6A7519AC10-L000164](../../tests/test_answer_quality_comparison.py#L164) | 164 | `"        ],"` | — |
| [SRC-6A7519AC10-L000165](../../tests/test_answer_quality_comparison.py#L165) | 165 | `"    )"` | — |
| [SRC-6A7519AC10-L000166](../../tests/test_answer_quality_comparison.py#L166) | 166 | `"    errors = mod.validate_run(run, \"run\")"` | — |
| [SRC-6A7519AC10-L000167](../../tests/test_answer_quality_comparison.py#L167) | 167 | `"    assert any(\"duplicate case_id\" in error for error in errors)"` | — |
| [SRC-6A7519AC10-L000168](../../tests/test_answer_quality_comparison.py#L168) | 168 | `"    assert any(\"elapsed_ms must be finite and non-negative\" in error for error in errors)"` | — |
| [SRC-6A7519AC10-L000169](../../tests/test_answer_quality_comparison.py#L169) | 169 | `""` | — |
| [SRC-6A7519AC10-L000170](../../tests/test_answer_quality_comparison.py#L170) | 170 | `""` | — |
| [SRC-6A7519AC10-L000171](../../tests/test_answer_quality_comparison.py#L171) | 171 | `"def test_quality_comparison_rejects_incomplete_human_review_coverage():"` | — |
| [SRC-6A7519AC10-L000172](../../tests/test_answer_quality_comparison.py#L172) | 172 | `"    mod = load_module()"` | — |
| [SRC-6A7519AC10-L000173](../../tests/test_answer_quality_comparison.py#L173) | 173 | `"    corpus = mod.load_json_object(CORPUS_PATH)"` | — |
| [SRC-6A7519AC10-L000174](../../tests/test_answer_quality_comparison.py#L174) | 174 | `"    partial = {"` | — |
| [SRC-6A7519AC10-L000175](../../tests/test_answer_quality_comparison.py#L175) | 175 | `"        \"schema_version\": \"1.0\","` | — |
| [SRC-6A7519AC10-L000176](../../tests/test_answer_quality_comparison.py#L176) | 176 | `"        \"reviews\": [{"` | — |
| [SRC-6A7519AC10-L000177](../../tests/test_answer_quality_comparison.py#L177) | 177 | `"            \"case_id\": \"AQ-001\","` | — |
| [SRC-6A7519AC10-L000178](../../tests/test_answer_quality_comparison.py#L178) | 178 | `"            \"status\": \"REVIEWED\","` | — |
| [SRC-6A7519AC10-L000179](../../tests/test_answer_quality_comparison.py#L179) | 179 | `"            \"correctness\": {\"correct_facts\": 1, \"reviewed_facts\": 1},"` | — |
| [SRC-6A7519AC10-L000180](../../tests/test_answer_quality_comparison.py#L180) | 180 | `"        }],"` | — |
| [SRC-6A7519AC10-L000181](../../tests/test_answer_quality_comparison.py#L181) | 181 | `"    }"` | — |
| [SRC-6A7519AC10-L000182](../../tests/test_answer_quality_comparison.py#L182) | 182 | `"    full = _reviews(correct=1, supported_citations=1)"` | — |
| [SRC-6A7519AC10-L000183](../../tests/test_answer_quality_comparison.py#L183) | 183 | `"    with pytest.raises(ValueError, match=\"incomplete human review coverage\"):"` | — |
| [SRC-6A7519AC10-L000184](../../tests/test_answer_quality_comparison.py#L184) | 184 | `"        mod.review_comparison(partial, full, corpus)"` | — |
| [SRC-6A7519AC10-L000185](../../tests/test_answer_quality_comparison.py#L185) | 185 | `""` | — |
| [SRC-6A7519AC10-L000186](../../tests/test_answer_quality_comparison.py#L186) | 186 | `""` | — |
| [SRC-6A7519AC10-L000187](../../tests/test_answer_quality_comparison.py#L187) | 187 | `"def test_comparison_requires_nonempty_recorded_question_text():"` | — |
| [SRC-6A7519AC10-L000188](../../tests/test_answer_quality_comparison.py#L188) | 188 | `"    mod = load_module()"` | — |
| [SRC-6A7519AC10-L000189](../../tests/test_answer_quality_comparison.py#L189) | 189 | `"    baseline = _run(build_sha=\"a\" * 40, results=[{\"case_id\": \"AQ-001\", \"elapsed_ms\": 20}])"` | — |
| [SRC-6A7519AC10-L000190](../../tests/test_answer_quality_comparison.py#L190) | 190 | `"    candidate = _run(build_sha=\"b\" * 40, results=[{\"case_id\": \"AQ-001\", \"elapsed_ms\": 10}])"` | — |
| [SRC-6A7519AC10-L000191](../../tests/test_answer_quality_comparison.py#L191) | 191 | `"    errors = mod.validate_run(baseline, \"baseline\")"` | — |
| [SRC-6A7519AC10-L000192](../../tests/test_answer_quality_comparison.py#L192) | 192 | `"    assert any(\"prompt must be a non-empty string\" in error for error in errors)"` | — |
| [SRC-6A7519AC10-L000193](../../tests/test_answer_quality_comparison.py#L193) | 193 | `"    with pytest.raises(ValueError, match=\"prompt must be a non-empty string\"):"` | — |
| [SRC-6A7519AC10-L000194](../../tests/test_answer_quality_comparison.py#L194) | 194 | `"        mod.compare_runs(baseline, candidate)"` | — |
## اختبارات

### FILE-4CCB1F172B — [tests/test_answer_quality_corpus.py](../../tests/test_answer_quality_corpus.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-4CCB1F172B-L000001](../../tests/test_answer_quality_corpus.py#L1) | 1 | `"\"\"\"Structural validation for the offline answer-quality adversarial corpus."` | — |
| [SRC-4CCB1F172B-L000002](../../tests/test_answer_quality_corpus.py#L2) | 2 | `""` | — |
| [SRC-4CCB1F172B-L000003](../../tests/test_answer_quality_corpus.py#L3) | 3 | `"This module does NOT execute Omarai against the cases and does NOT claim that"` | — |
| [SRC-4CCB1F172B-L000004](../../tests/test_answer_quality_corpus.py#L4) | 4 | `"any reasoning case passed. It only verifies that the benchmark file is complete,"` | — |
| [SRC-4CCB1F172B-L000005](../../tests/test_answer_quality_corpus.py#L5) | 5 | `"internally consistent, and ready for human or fixture-assisted review."` | — |
| [SRC-4CCB1F172B-L000006](../../tests/test_answer_quality_corpus.py#L6) | 6 | `"\"\"\""` | — |
| [SRC-4CCB1F172B-L000007](../../tests/test_answer_quality_corpus.py#L7) | 7 | `"from __future__ import annotations"` | — |
| [SRC-4CCB1F172B-L000008](../../tests/test_answer_quality_corpus.py#L8) | 8 | `""` | — |
| [SRC-4CCB1F172B-L000009](../../tests/test_answer_quality_corpus.py#L9) | 9 | `"import json"` | — |
| [SRC-4CCB1F172B-L000010](../../tests/test_answer_quality_corpus.py#L10) | 10 | `"import re"` | — |
| [SRC-4CCB1F172B-L000011](../../tests/test_answer_quality_corpus.py#L11) | 11 | `"from collections import Counter"` | — |
| [SRC-4CCB1F172B-L000012](../../tests/test_answer_quality_corpus.py#L12) | 12 | `"from pathlib import Path"` | — |
| [SRC-4CCB1F172B-L000013](../../tests/test_answer_quality_corpus.py#L13) | 13 | `""` | — |
| [SRC-4CCB1F172B-L000014](../../tests/test_answer_quality_corpus.py#L14) | 14 | `"CORPUS_PATH = Path(__file__).resolve().parent / \"fixtures\" / \"answer_quality_cases.json\""` | — |
| [SRC-4CCB1F172B-L000015](../../tests/test_answer_quality_corpus.py#L15) | 15 | `"DOCS_PATH = Path(__file__).resolve().parents[1] / \"docs\" / \"ANSWER_QUALITY_BENCHMARK_AR.md\""` | — |
| [SRC-4CCB1F172B-L000016](../../tests/test_answer_quality_corpus.py#L16) | 16 | `""` | — |
| [SRC-4CCB1F172B-L000017](../../tests/test_answer_quality_corpus.py#L17) | 17 | `"REQUIRED_CASE_FIELDS = {"` | — |
| [SRC-4CCB1F172B-L000018](../../tests/test_answer_quality_corpus.py#L18) | 18 | `"    \"case_id\","` | — |
| [SRC-4CCB1F172B-L000019](../../tests/test_answer_quality_corpus.py#L19) | 19 | `"    \"category\","` | — |
| [SRC-4CCB1F172B-L000020](../../tests/test_answer_quality_corpus.py#L20) | 20 | `"    \"language\","` | — |
| [SRC-4CCB1F172B-L000021](../../tests/test_answer_quality_corpus.py#L21) | 21 | `"    \"question\","` | — |
| [SRC-4CCB1F172B-L000022](../../tests/test_answer_quality_corpus.py#L22) | 22 | `"    \"expected_strategy\","` | — |
| [SRC-4CCB1F172B-L000023](../../tests/test_answer_quality_corpus.py#L23) | 23 | `"    \"required_behaviors\","` | — |
| [SRC-4CCB1F172B-L000024](../../tests/test_answer_quality_corpus.py#L24) | 24 | `"    \"forbidden_behaviors\","` | — |
| [SRC-4CCB1F172B-L000025](../../tests/test_answer_quality_corpus.py#L25) | 25 | `"    \"evidence_fixture\","` | — |
| [SRC-4CCB1F172B-L000026](../../tests/test_answer_quality_corpus.py#L26) | 26 | `"    \"failure_conditions\","` | — |
| [SRC-4CCB1F172B-L000027](../../tests/test_answer_quality_corpus.py#L27) | 27 | `"    \"evaluation_mode\","` | — |
| [SRC-4CCB1F172B-L000028](../../tests/test_answer_quality_corpus.py#L28) | 28 | `"}"` | — |
| [SRC-4CCB1F172B-L000029](../../tests/test_answer_quality_corpus.py#L29) | 29 | `""` | — |
| [SRC-4CCB1F172B-L000030](../../tests/test_answer_quality_corpus.py#L30) | 30 | `"ALLOWED_STRATEGIES = {\"local\", \"model_no_search\", \"web_search\", \"clarify\"}"` | — |
| [SRC-4CCB1F172B-L000031](../../tests/test_answer_quality_corpus.py#L31) | 31 | `"ALLOWED_EVAL_MODES = {\"deterministic_structure\", \"fixture_assisted\", \"human_judgment\"}"` | — |
| [SRC-4CCB1F172B-L000032](../../tests/test_answer_quality_corpus.py#L32) | 32 | `""` | — |
| [SRC-4CCB1F172B-L000033](../../tests/test_answer_quality_corpus.py#L33) | 33 | `"REQUIRED_THEME_CATEGORIES = {"` | — |
| [SRC-4CCB1F172B-L000034](../../tests/test_answer_quality_corpus.py#L34) | 34 | `"    \"simple_conversational\","` | — |
| [SRC-4CCB1F172B-L000035](../../tests/test_answer_quality_corpus.py#L35) | 35 | `"    \"general_knowledge\","` | — |
| [SRC-4CCB1F172B-L000036](../../tests/test_answer_quality_corpus.py#L36) | 36 | `"    \"omarai_capabilities\","` | — |
| [SRC-4CCB1F172B-L000037](../../tests/test_answer_quality_corpus.py#L37) | 37 | `"    \"current_information\","` | — |
| [SRC-4CCB1F172B-L000038](../../tests/test_answer_quality_corpus.py#L38) | 38 | `"    \"multi_subquestions\","` | — |
| [SRC-4CCB1F172B-L000039](../../tests/test_answer_quality_corpus.py#L39) | 39 | `"    \"ambiguous_clarify\","` | — |
| [SRC-4CCB1F172B-L000040](../../tests/test_answer_quality_corpus.py#L40) | 40 | `"    \"spelling_variation\","` | — |
| [SRC-4CCB1F172B-L000041](../../tests/test_answer_quality_corpus.py#L41) | 41 | `"    \"irrelevant_results\","` | — |
| [SRC-4CCB1F172B-L000042](../../tests/test_answer_quality_corpus.py#L42) | 42 | `"    \"empty_or_failed_search\","` | — |
| [SRC-4CCB1F172B-L000043](../../tests/test_answer_quality_corpus.py#L43) | 43 | `"    \"conflicting_sources\","` | — |
| [SRC-4CCB1F172B-L000044](../../tests/test_answer_quality_corpus.py#L44) | 44 | `"    \"stale_sources_for_current\","` | — |
| [SRC-4CCB1F172B-L000045](../../tests/test_answer_quality_corpus.py#L45) | 45 | `"    \"false_corroboration\","` | — |
| [SRC-4CCB1F172B-L000046](../../tests/test_answer_quality_corpus.py#L46) | 46 | `"    \"unsupported_claim\","` | — |
| [SRC-4CCB1F172B-L000047](../../tests/test_answer_quality_corpus.py#L47) | 47 | `"    \"invalid_links\","` | — |
| [SRC-4CCB1F172B-L000048](../../tests/test_answer_quality_corpus.py#L48) | 48 | `"    \"prompt_injection_in_content\","` | — |
| [SRC-4CCB1F172B-L000049](../../tests/test_answer_quality_corpus.py#L49) | 49 | `"    \"secret_exfiltration_attempt\","` | — |
| [SRC-4CCB1F172B-L000050](../../tests/test_answer_quality_corpus.py#L50) | 50 | `"    \"missing_model_credentials\","` | — |
| [SRC-4CCB1F172B-L000051](../../tests/test_answer_quality_corpus.py#L51) | 51 | `"    \"overconfidence_insufficient_evidence\","` | — |
| [SRC-4CCB1F172B-L000052](../../tests/test_answer_quality_corpus.py#L52) | 52 | `"    \"incomplete_answer\","` | — |
| [SRC-4CCB1F172B-L000053](../../tests/test_answer_quality_corpus.py#L53) | 53 | `"    \"lead_not_verified\","` | — |
| [SRC-4CCB1F172B-L000054](../../tests/test_answer_quality_corpus.py#L54) | 54 | `"}"` | — |
| [SRC-4CCB1F172B-L000055](../../tests/test_answer_quality_corpus.py#L55) | 55 | `""` | — |
| [SRC-4CCB1F172B-L000056](../../tests/test_answer_quality_corpus.py#L56) | 56 | `"DOC_EXAMPLE_CATEGORY_EXPECTATIONS = {"` | — |
| [SRC-4CCB1F172B-L000057](../../tests/test_answer_quality_corpus.py#L57) | 57 | `"    \"AQ-024\": \"prompt_injection_in_content\","` | — |
| [SRC-4CCB1F172B-L000058](../../tests/test_answer_quality_corpus.py#L58) | 58 | `"    \"AQ-030\": \"prompt_injection_in_content\","` | — |
| [SRC-4CCB1F172B-L000059](../../tests/test_answer_quality_corpus.py#L59) | 59 | `"    \"AQ-025\": \"secret_exfiltration_attempt\","` | — |
| [SRC-4CCB1F172B-L000060](../../tests/test_answer_quality_corpus.py#L60) | 60 | `"    \"AQ-031\": \"secret_exfiltration_attempt\","` | — |
| [SRC-4CCB1F172B-L000061](../../tests/test_answer_quality_corpus.py#L61) | 61 | `"    \"AQ-023\": \"invalid_links\","` | — |
| [SRC-4CCB1F172B-L000062](../../tests/test_answer_quality_corpus.py#L62) | 62 | `"    \"AQ-029\": \"lead_not_verified\","` | — |
| [SRC-4CCB1F172B-L000063](../../tests/test_answer_quality_corpus.py#L63) | 63 | `"    \"AQ-032\": \"lead_not_verified\","` | — |
| [SRC-4CCB1F172B-L000064](../../tests/test_answer_quality_corpus.py#L64) | 64 | `"    \"AQ-033\": \"lead_not_verified\","` | — |
| [SRC-4CCB1F172B-L000065](../../tests/test_answer_quality_corpus.py#L65) | 65 | `"    \"AQ-045\": \"lead_not_verified\","` | — |
| [SRC-4CCB1F172B-L000066](../../tests/test_answer_quality_corpus.py#L66) | 66 | `"    \"AQ-018\": \"conflicting_sources\","` | — |
| [SRC-4CCB1F172B-L000067](../../tests/test_answer_quality_corpus.py#L67) | 67 | `"    \"AQ-019\": \"conflicting_sources\","` | — |
| [SRC-4CCB1F172B-L000068](../../tests/test_answer_quality_corpus.py#L68) | 68 | `"    \"AQ-020\": \"stale_sources_for_current\","` | — |
| [SRC-4CCB1F172B-L000069](../../tests/test_answer_quality_corpus.py#L69) | 69 | `"    \"AQ-034\": \"stale_sources_for_current\","` | — |
| [SRC-4CCB1F172B-L000070](../../tests/test_answer_quality_corpus.py#L70) | 70 | `"    \"AQ-042\": \"stale_sources_for_current\","` | — |
| [SRC-4CCB1F172B-L000071](../../tests/test_answer_quality_corpus.py#L71) | 71 | `"    \"AQ-021\": \"false_corroboration\","` | — |
| [SRC-4CCB1F172B-L000072](../../tests/test_answer_quality_corpus.py#L72) | 72 | `"    \"AQ-035\": \"false_corroboration\","` | — |
| [SRC-4CCB1F172B-L000073](../../tests/test_answer_quality_corpus.py#L73) | 73 | `"}"` | — |
| [SRC-4CCB1F172B-L000074](../../tests/test_answer_quality_corpus.py#L74) | 74 | `""` | — |
| [SRC-4CCB1F172B-L000075](../../tests/test_answer_quality_corpus.py#L75) | 75 | `"CASE_ID_RE = re.compile(r\"^AQ-\\d{3}$\")"` | — |
| [SRC-4CCB1F172B-L000076](../../tests/test_answer_quality_corpus.py#L76) | 76 | `""` | — |
| [SRC-4CCB1F172B-L000077](../../tests/test_answer_quality_corpus.py#L77) | 77 | `""` | — |
| [SRC-4CCB1F172B-L000078](../../tests/test_answer_quality_corpus.py#L78) | 78 | `"def _load_corpus() -> dict:"` | — |
| [SRC-4CCB1F172B-L000079](../../tests/test_answer_quality_corpus.py#L79) | 79 | `"    assert CORPUS_PATH.is_file(), f\"Missing corpus file: {CORPUS_PATH}\""` | — |
| [SRC-4CCB1F172B-L000080](../../tests/test_answer_quality_corpus.py#L80) | 80 | `"    data = json.loads(CORPUS_PATH.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-4CCB1F172B-L000081](../../tests/test_answer_quality_corpus.py#L81) | 81 | `"    assert isinstance(data, dict), \"Corpus root must be an object\""` | — |
| [SRC-4CCB1F172B-L000082](../../tests/test_answer_quality_corpus.py#L82) | 82 | `"    assert \"parts\" not in data or not data.get(\"parts\"), ("` | — |
| [SRC-4CCB1F172B-L000083](../../tests/test_answer_quality_corpus.py#L83) | 83 | `"        \"Authoritative corpus must be a single merged cases[] file, not incomplete shards\""` | — |
| [SRC-4CCB1F172B-L000084](../../tests/test_answer_quality_corpus.py#L84) | 84 | `"    )"` | — |
| [SRC-4CCB1F172B-L000085](../../tests/test_answer_quality_corpus.py#L85) | 85 | `"    return data"` | — |
| [SRC-4CCB1F172B-L000086](../../tests/test_answer_quality_corpus.py#L86) | 86 | `""` | — |
| [SRC-4CCB1F172B-L000087](../../tests/test_answer_quality_corpus.py#L87) | 87 | `""` | — |
| [SRC-4CCB1F172B-L000088](../../tests/test_answer_quality_corpus.py#L88) | 88 | `"def test_corpus_file_loads_as_utf8_json():"` | — |
| [SRC-4CCB1F172B-L000089](../../tests/test_answer_quality_corpus.py#L89) | 89 | `"    data = _load_corpus()"` | — |
| [SRC-4CCB1F172B-L000090](../../tests/test_answer_quality_corpus.py#L90) | 90 | `"    assert data.get(\"benchmark_id\") == \"OMARAI-REDTEAM-001\""` | — |
| [SRC-4CCB1F172B-L000091](../../tests/test_answer_quality_corpus.py#L91) | 91 | `"    assert isinstance(data.get(\"cases\"), list)"` | — |
| [SRC-4CCB1F172B-L000092](../../tests/test_answer_quality_corpus.py#L92) | 92 | `"    assert data[\"case_count\"] == len(data[\"cases\"])"` | — |
| [SRC-4CCB1F172B-L000093](../../tests/test_answer_quality_corpus.py#L93) | 93 | `""` | — |
| [SRC-4CCB1F172B-L000094](../../tests/test_answer_quality_corpus.py#L94) | 94 | `""` | — |
| [SRC-4CCB1F172B-L000095](../../tests/test_answer_quality_corpus.py#L95) | 95 | `"def test_minimum_case_count():"` | — |
| [SRC-4CCB1F172B-L000096](../../tests/test_answer_quality_corpus.py#L96) | 96 | `"    data = _load_corpus()"` | — |
| [SRC-4CCB1F172B-L000097](../../tests/test_answer_quality_corpus.py#L97) | 97 | `"    assert len(data[\"cases\"]) >= 40, f\"Need at least 40 cases, found {len(data['cases'])}\""` | — |
| [SRC-4CCB1F172B-L000098](../../tests/test_answer_quality_corpus.py#L98) | 98 | `"    assert data[\"case_count\"] == 45"` | — |
| [SRC-4CCB1F172B-L000099](../../tests/test_answer_quality_corpus.py#L99) | 99 | `""` | — |
| [SRC-4CCB1F172B-L000100](../../tests/test_answer_quality_corpus.py#L100) | 100 | `""` | — |
| [SRC-4CCB1F172B-L000101](../../tests/test_answer_quality_corpus.py#L101) | 101 | `"def test_case_ids_unique_and_shaped():"` | — |
| [SRC-4CCB1F172B-L000102](../../tests/test_answer_quality_corpus.py#L102) | 102 | `"    data = _load_corpus()"` | — |
| [SRC-4CCB1F172B-L000103](../../tests/test_answer_quality_corpus.py#L103) | 103 | `"    ids = [c[\"case_id\"] for c in data[\"cases\"]]"` | — |
| [SRC-4CCB1F172B-L000104](../../tests/test_answer_quality_corpus.py#L104) | 104 | `"    assert len(ids) == len(set(ids)), \"Duplicate case_id values found\""` | — |
| [SRC-4CCB1F172B-L000105](../../tests/test_answer_quality_corpus.py#L105) | 105 | `"    for case_id in ids:"` | — |
| [SRC-4CCB1F172B-L000106](../../tests/test_answer_quality_corpus.py#L106) | 106 | `"        assert CASE_ID_RE.match(case_id), f\"Bad case_id shape: {case_id}\""` | — |
| [SRC-4CCB1F172B-L000107](../../tests/test_answer_quality_corpus.py#L107) | 107 | `"    assert set(ids) == {f\"AQ-{i:03d}\" for i in range(1, 46)}"` | — |
| [SRC-4CCB1F172B-L000108](../../tests/test_answer_quality_corpus.py#L108) | 108 | `""` | — |
| [SRC-4CCB1F172B-L000109](../../tests/test_answer_quality_corpus.py#L109) | 109 | `""` | — |
| [SRC-4CCB1F172B-L000110](../../tests/test_answer_quality_corpus.py#L110) | 110 | `"def test_required_fields_and_types():"` | — |
| [SRC-4CCB1F172B-L000111](../../tests/test_answer_quality_corpus.py#L111) | 111 | `"    data = _load_corpus()"` | — |
| [SRC-4CCB1F172B-L000112](../../tests/test_answer_quality_corpus.py#L112) | 112 | `"    for case in data[\"cases\"]:"` | — |
| [SRC-4CCB1F172B-L000113](../../tests/test_answer_quality_corpus.py#L113) | 113 | `"        missing = REQUIRED_CASE_FIELDS - set(case)"` | — |
| [SRC-4CCB1F172B-L000114](../../tests/test_answer_quality_corpus.py#L114) | 114 | `"        assert not missing, f\"{case.get('case_id')}: missing {missing}\""` | — |
| [SRC-4CCB1F172B-L000115](../../tests/test_answer_quality_corpus.py#L115) | 115 | `"        assert isinstance(case[\"case_id\"], str) and case[\"case_id\"].strip()"` | — |
| [SRC-4CCB1F172B-L000116](../../tests/test_answer_quality_corpus.py#L116) | 116 | `"        assert isinstance(case[\"category\"], str) and case[\"category\"].strip()"` | — |
| [SRC-4CCB1F172B-L000117](../../tests/test_answer_quality_corpus.py#L117) | 117 | `"        assert isinstance(case[\"language\"], str) and case[\"language\"].strip()"` | — |
| [SRC-4CCB1F172B-L000118](../../tests/test_answer_quality_corpus.py#L118) | 118 | `"        assert isinstance(case[\"question\"], str) and len(case[\"question\"].strip()) >= 2"` | — |
| [SRC-4CCB1F172B-L000119](../../tests/test_answer_quality_corpus.py#L119) | 119 | `"        assert case[\"expected_strategy\"] in ALLOWED_STRATEGIES"` | — |
| [SRC-4CCB1F172B-L000120](../../tests/test_answer_quality_corpus.py#L120) | 120 | `"        assert case[\"evaluation_mode\"] in ALLOWED_EVAL_MODES"` | — |
| [SRC-4CCB1F172B-L000121](../../tests/test_answer_quality_corpus.py#L121) | 121 | `"        assert isinstance(case[\"required_behaviors\"], list) and case[\"required_behaviors\"]"` | — |
| [SRC-4CCB1F172B-L000122](../../tests/test_answer_quality_corpus.py#L122) | 122 | `"        assert isinstance(case[\"forbidden_behaviors\"], list) and case[\"forbidden_behaviors\"]"` | — |
| [SRC-4CCB1F172B-L000123](../../tests/test_answer_quality_corpus.py#L123) | 123 | `"        assert isinstance(case[\"failure_conditions\"], list) and case[\"failure_conditions\"]"` | — |
| [SRC-4CCB1F172B-L000124](../../tests/test_answer_quality_corpus.py#L124) | 124 | `"        assert isinstance(case[\"evidence_fixture\"], dict)"` | — |
| [SRC-4CCB1F172B-L000125](../../tests/test_answer_quality_corpus.py#L125) | 125 | `"        for item in ("` | — |
| [SRC-4CCB1F172B-L000126](../../tests/test_answer_quality_corpus.py#L126) | 126 | `"            case[\"required_behaviors\"]"` | — |
| [SRC-4CCB1F172B-L000127](../../tests/test_answer_quality_corpus.py#L127) | 127 | `"            + case[\"forbidden_behaviors\"]"` | — |
| [SRC-4CCB1F172B-L000128](../../tests/test_answer_quality_corpus.py#L128) | 128 | `"            + case[\"failure_conditions\"]"` | — |
| [SRC-4CCB1F172B-L000129](../../tests/test_answer_quality_corpus.py#L129) | 129 | `"        ):"` | — |
| [SRC-4CCB1F172B-L000130](../../tests/test_answer_quality_corpus.py#L130) | 130 | `"            assert isinstance(item, str) and item.strip(), ("` | — |
| [SRC-4CCB1F172B-L000131](../../tests/test_answer_quality_corpus.py#L131) | 131 | `"                f\"{case['case_id']}: empty behavior/condition\""` | — |
| [SRC-4CCB1F172B-L000132](../../tests/test_answer_quality_corpus.py#L132) | 132 | `"            )"` | — |
| [SRC-4CCB1F172B-L000133](../../tests/test_answer_quality_corpus.py#L133) | 133 | `""` | — |
| [SRC-4CCB1F172B-L000134](../../tests/test_answer_quality_corpus.py#L134) | 134 | `""` | — |
| [SRC-4CCB1F172B-L000135](../../tests/test_answer_quality_corpus.py#L135) | 135 | `"def test_required_theme_categories_represented():"` | — |
| [SRC-4CCB1F172B-L000136](../../tests/test_answer_quality_corpus.py#L136) | 136 | `"    data = _load_corpus()"` | — |
| [SRC-4CCB1F172B-L000137](../../tests/test_answer_quality_corpus.py#L137) | 137 | `"    present = {c[\"category\"] for c in data[\"cases\"]}"` | — |
| [SRC-4CCB1F172B-L000138](../../tests/test_answer_quality_corpus.py#L138) | 138 | `"    missing = REQUIRED_THEME_CATEGORIES - present"` | — |
| [SRC-4CCB1F172B-L000139](../../tests/test_answer_quality_corpus.py#L139) | 139 | `"    assert not missing, f\"Missing required categories: {sorted(missing)}\""` | — |
| [SRC-4CCB1F172B-L000140](../../tests/test_answer_quality_corpus.py#L140) | 140 | `""` | — |
| [SRC-4CCB1F172B-L000141](../../tests/test_answer_quality_corpus.py#L141) | 141 | `""` | — |
| [SRC-4CCB1F172B-L000142](../../tests/test_answer_quality_corpus.py#L142) | 142 | `"def test_no_empty_or_exact_duplicate_questions():"` | — |
| [SRC-4CCB1F172B-L000143](../../tests/test_answer_quality_corpus.py#L143) | 143 | `"    data = _load_corpus()"` | — |
| [SRC-4CCB1F172B-L000144](../../tests/test_answer_quality_corpus.py#L144) | 144 | `"    normalized = []"` | — |
| [SRC-4CCB1F172B-L000145](../../tests/test_answer_quality_corpus.py#L145) | 145 | `"    for case in data[\"cases\"]:"` | — |
| [SRC-4CCB1F172B-L000146](../../tests/test_answer_quality_corpus.py#L146) | 146 | `"        q = \" \".join(case[\"question\"].casefold().split())"` | — |
| [SRC-4CCB1F172B-L000147](../../tests/test_answer_quality_corpus.py#L147) | 147 | `"        assert len(q) >= 3, f\"{case['case_id']}: question too short\""` | — |
| [SRC-4CCB1F172B-L000148](../../tests/test_answer_quality_corpus.py#L148) | 148 | `"        normalized.append((case[\"case_id\"], q))"` | — |
| [SRC-4CCB1F172B-L000149](../../tests/test_answer_quality_corpus.py#L149) | 149 | `"    counts = Counter(q for _, q in normalized)"` | — |
| [SRC-4CCB1F172B-L000150](../../tests/test_answer_quality_corpus.py#L150) | 150 | `"    dupes = [q for q, n in counts.items() if n > 1]"` | — |
| [SRC-4CCB1F172B-L000151](../../tests/test_answer_quality_corpus.py#L151) | 151 | `"    assert not dupes, f\"Duplicate questions: {dupes}\""` | — |
| [SRC-4CCB1F172B-L000152](../../tests/test_answer_quality_corpus.py#L152) | 152 | `""` | — |
| [SRC-4CCB1F172B-L000153](../../tests/test_answer_quality_corpus.py#L153) | 153 | `""` | — |
| [SRC-4CCB1F172B-L000154](../../tests/test_answer_quality_corpus.py#L154) | 154 | `"def test_research_cases_declare_fixture_or_controlled_env():"` | — |
| [SRC-4CCB1F172B-L000155](../../tests/test_answer_quality_corpus.py#L155) | 155 | `"    data = _load_corpus()"` | — |
| [SRC-4CCB1F172B-L000156](../../tests/test_answer_quality_corpus.py#L156) | 156 | `"    for case in data[\"cases\"]:"` | — |
| [SRC-4CCB1F172B-L000157](../../tests/test_answer_quality_corpus.py#L157) | 157 | `"        if case[\"expected_strategy\"] != \"web_search\":"` | — |
| [SRC-4CCB1F172B-L000158](../../tests/test_answer_quality_corpus.py#L158) | 158 | `"            continue"` | — |
| [SRC-4CCB1F172B-L000159](../../tests/test_answer_quality_corpus.py#L159) | 159 | `"        fixture = case[\"evidence_fixture\"]"` | — |
| [SRC-4CCB1F172B-L000160](../../tests/test_answer_quality_corpus.py#L160) | 160 | `"        assert fixture.get(\"type\") in {"` | — |
| [SRC-4CCB1F172B-L000161](../../tests/test_answer_quality_corpus.py#L161) | 161 | `"            \"controlled_search\","` | — |
| [SRC-4CCB1F172B-L000162](../../tests/test_answer_quality_corpus.py#L162) | 162 | `"            \"controlled_page\","` | — |
| [SRC-4CCB1F172B-L000163](../../tests/test_answer_quality_corpus.py#L163) | 163 | `"            \"controlled_fetch_failure\","` | — |
| [SRC-4CCB1F172B-L000164](../../tests/test_answer_quality_corpus.py#L164) | 164 | `"            \"ssrf_blocked\","` | — |
| [SRC-4CCB1F172B-L000165](../../tests/test_answer_quality_corpus.py#L165) | 165 | `"            \"env\","` | — |
| [SRC-4CCB1F172B-L000166](../../tests/test_answer_quality_corpus.py#L166) | 166 | `"            \"none\","` | — |
| [SRC-4CCB1F172B-L000167](../../tests/test_answer_quality_corpus.py#L167) | 167 | `"        } or \"notes\" in fixture, ("` | — |
| [SRC-4CCB1F172B-L000168](../../tests/test_answer_quality_corpus.py#L168) | 168 | `"            f\"{case['case_id']}: research case needs a clear evidence fixture\""` | — |
| [SRC-4CCB1F172B-L000169](../../tests/test_answer_quality_corpus.py#L169) | 169 | `"        )"` | — |
| [SRC-4CCB1F172B-L000170](../../tests/test_answer_quality_corpus.py#L170) | 170 | `""` | — |
| [SRC-4CCB1F172B-L000171](../../tests/test_answer_quality_corpus.py#L171) | 171 | `""` | — |
| [SRC-4CCB1F172B-L000172](../../tests/test_answer_quality_corpus.py#L172) | 172 | `"def test_safety_categories_include_injection_and_secrets():"` | — |
| [SRC-4CCB1F172B-L000173](../../tests/test_answer_quality_corpus.py#L173) | 173 | `"    data = _load_corpus()"` | — |
| [SRC-4CCB1F172B-L000174](../../tests/test_answer_quality_corpus.py#L174) | 174 | `"    cats = {c[\"category\"] for c in data[\"cases\"]}"` | — |
| [SRC-4CCB1F172B-L000175](../../tests/test_answer_quality_corpus.py#L175) | 175 | `"    assert \"prompt_injection_in_content\" in cats"` | — |
| [SRC-4CCB1F172B-L000176](../../tests/test_answer_quality_corpus.py#L176) | 176 | `"    assert \"secret_exfiltration_attempt\" in cats"` | — |
| [SRC-4CCB1F172B-L000177](../../tests/test_answer_quality_corpus.py#L177) | 177 | `"    secret_failures = ["` | — |
| [SRC-4CCB1F172B-L000178](../../tests/test_answer_quality_corpus.py#L178) | 178 | `"        c"` | — |
| [SRC-4CCB1F172B-L000179](../../tests/test_answer_quality_corpus.py#L179) | 179 | `"        for c in data[\"cases\"]"` | — |
| [SRC-4CCB1F172B-L000180](../../tests/test_answer_quality_corpus.py#L180) | 180 | `"        if any("` | — |
| [SRC-4CCB1F172B-L000181](../../tests/test_answer_quality_corpus.py#L181) | 181 | `"            \"token\" in f.casefold() or \"secret\" in f.casefold() or \"key\" in f.casefold()"` | — |
| [SRC-4CCB1F172B-L000182](../../tests/test_answer_quality_corpus.py#L182) | 182 | `"            for f in c[\"failure_conditions\"]"` | — |
| [SRC-4CCB1F172B-L000183](../../tests/test_answer_quality_corpus.py#L183) | 183 | `"        )"` | — |
| [SRC-4CCB1F172B-L000184](../../tests/test_answer_quality_corpus.py#L184) | 184 | `"    ]"` | — |
| [SRC-4CCB1F172B-L000185](../../tests/test_answer_quality_corpus.py#L185) | 185 | `"    assert secret_failures, \"Expected at least one case with secret-related failure conditions\""` | — |
| [SRC-4CCB1F172B-L000186](../../tests/test_answer_quality_corpus.py#L186) | 186 | `""` | — |
| [SRC-4CCB1F172B-L000187](../../tests/test_answer_quality_corpus.py#L187) | 187 | `""` | — |
| [SRC-4CCB1F172B-L000188](../../tests/test_answer_quality_corpus.py#L188) | 188 | `"def test_corpus_does_not_claim_live_execution_results():"` | — |
| [SRC-4CCB1F172B-L000189](../../tests/test_answer_quality_corpus.py#L189) | 189 | `"    data = _load_corpus()"` | — |
| [SRC-4CCB1F172B-L000190](../../tests/test_answer_quality_corpus.py#L190) | 190 | `"    for case in data[\"cases\"]:"` | — |
| [SRC-4CCB1F172B-L000191](../../tests/test_answer_quality_corpus.py#L191) | 191 | `"        assert \"observed_result\" not in case"` | — |
| [SRC-4CCB1F172B-L000192](../../tests/test_answer_quality_corpus.py#L192) | 192 | `"        assert \"score\" not in case"` | — |
| [SRC-4CCB1F172B-L000193](../../tests/test_answer_quality_corpus.py#L193) | 193 | `"        assert case.get(\"status\") not in {\"PASS\", \"FAIL\"}"` | — |
| [SRC-4CCB1F172B-L000194](../../tests/test_answer_quality_corpus.py#L194) | 194 | `""` | — |
| [SRC-4CCB1F172B-L000195](../../tests/test_answer_quality_corpus.py#L195) | 195 | `""` | — |
| [SRC-4CCB1F172B-L000196](../../tests/test_answer_quality_corpus.py#L196) | 196 | `"def test_languages_include_arabic_english_and_mixed():"` | — |
| [SRC-4CCB1F172B-L000197](../../tests/test_answer_quality_corpus.py#L197) | 197 | `"    data = _load_corpus()"` | — |
| [SRC-4CCB1F172B-L000198](../../tests/test_answer_quality_corpus.py#L198) | 198 | `"    langs = {c[\"language\"] for c in data[\"cases\"]}"` | — |
| [SRC-4CCB1F172B-L000199](../../tests/test_answer_quality_corpus.py#L199) | 199 | `"    assert any(x.startswith(\"ar\") for x in langs)"` | — |
| [SRC-4CCB1F172B-L000200](../../tests/test_answer_quality_corpus.py#L200) | 200 | `"    assert \"en\" in langs"` | — |
| [SRC-4CCB1F172B-L000201](../../tests/test_answer_quality_corpus.py#L201) | 201 | `"    assert \"mixed\" in langs"` | — |
| [SRC-4CCB1F172B-L000202](../../tests/test_answer_quality_corpus.py#L202) | 202 | `"    assert \"ar-EG\" in langs"` | — |
| [SRC-4CCB1F172B-L000203](../../tests/test_answer_quality_corpus.py#L203) | 203 | `"    assert \"ar-MSA\" in langs"` | — |
| [SRC-4CCB1F172B-L000204](../../tests/test_answer_quality_corpus.py#L204) | 204 | `""` | — |
| [SRC-4CCB1F172B-L000205](../../tests/test_answer_quality_corpus.py#L205) | 205 | `""` | — |
| [SRC-4CCB1F172B-L000206](../../tests/test_answer_quality_corpus.py#L206) | 206 | `"def test_documented_high_risk_examples_match_json_categories():"` | — |
| [SRC-4CCB1F172B-L000207](../../tests/test_answer_quality_corpus.py#L207) | 207 | `"    data = _load_corpus()"` | — |
| [SRC-4CCB1F172B-L000208](../../tests/test_answer_quality_corpus.py#L208) | 208 | `"    by_id = {c[\"case_id\"]: c for c in data[\"cases\"]}"` | — |
| [SRC-4CCB1F172B-L000209](../../tests/test_answer_quality_corpus.py#L209) | 209 | `"    for case_id, expected_cat in DOC_EXAMPLE_CATEGORY_EXPECTATIONS.items():"` | — |
| [SRC-4CCB1F172B-L000210](../../tests/test_answer_quality_corpus.py#L210) | 210 | `"        assert case_id in by_id, f\"Doc example {case_id} missing from corpus\""` | — |
| [SRC-4CCB1F172B-L000211](../../tests/test_answer_quality_corpus.py#L211) | 211 | `"        actual = by_id[case_id][\"category\"]"` | — |
| [SRC-4CCB1F172B-L000212](../../tests/test_answer_quality_corpus.py#L212) | 212 | `"        assert actual == expected_cat, ("` | — |
| [SRC-4CCB1F172B-L000213](../../tests/test_answer_quality_corpus.py#L213) | 213 | `"            f\"Doc/example mismatch: {case_id} is category={actual!r}, \""` | — |
| [SRC-4CCB1F172B-L000214](../../tests/test_answer_quality_corpus.py#L214) | 214 | `"            f\"expected {expected_cat!r}\""` | — |
| [SRC-4CCB1F172B-L000215](../../tests/test_answer_quality_corpus.py#L215) | 215 | `"        )"` | — |
| [SRC-4CCB1F172B-L000216](../../tests/test_answer_quality_corpus.py#L216) | 216 | `""` | — |
| [SRC-4CCB1F172B-L000217](../../tests/test_answer_quality_corpus.py#L217) | 217 | `""` | — |
| [SRC-4CCB1F172B-L000218](../../tests/test_answer_quality_corpus.py#L218) | 218 | `"def test_docs_mention_corrected_high_risk_ids():"` | — |
| [SRC-4CCB1F172B-L000219](../../tests/test_answer_quality_corpus.py#L219) | 219 | `"    assert DOCS_PATH.is_file()"` | — |
| [SRC-4CCB1F172B-L000220](../../tests/test_answer_quality_corpus.py#L220) | 220 | `"    text = DOCS_PATH.read_text(encoding=\"utf-8\")"` | — |
| [SRC-4CCB1F172B-L000221](../../tests/test_answer_quality_corpus.py#L221) | 221 | `"    for case_id in (\"AQ-024\", \"AQ-030\", \"AQ-025\", \"AQ-031\", \"AQ-023\", \"AQ-018\", \"AQ-021\"):"` | — |
| [SRC-4CCB1F172B-L000222](../../tests/test_answer_quality_corpus.py#L222) | 222 | `"        assert case_id in text, f\"Docs missing corrected example {case_id}\""` | — |
| [SRC-4CCB1F172B-L000223](../../tests/test_answer_quality_corpus.py#L223) | 223 | `""` | — |
| [SRC-4CCB1F172B-L000224](../../tests/test_answer_quality_corpus.py#L224) | 224 | `""` | — |
| [SRC-4CCB1F172B-L000225](../../tests/test_answer_quality_corpus.py#L225) | 225 | `"def test_no_placeholder_corpus_content():"` | — |
| [SRC-4CCB1F172B-L000226](../../tests/test_answer_quality_corpus.py#L226) | 226 | `"    raw = CORPUS_PATH.read_text(encoding=\"utf-8\")"` | — |
| [SRC-4CCB1F172B-L000227](../../tests/test_answer_quality_corpus.py#L227) | 227 | `"    assert \"PLACEHOLDER\" not in raw"` | — |
| [SRC-4CCB1F172B-L000228](../../tests/test_answer_quality_corpus.py#L228) | 228 | `"    assert \"SEE_LOCAL_FILE\" not in raw"` | — |
| [SRC-4CCB1F172B-L000229](../../tests/test_answer_quality_corpus.py#L229) | 229 | `"    data = _load_corpus()"` | — |
| [SRC-4CCB1F172B-L000230](../../tests/test_answer_quality_corpus.py#L230) | 230 | `"    assert len(data[\"cases\"]) == data[\"case_count\"] == 45"` | — |
| [SRC-4CCB1F172B-L000231](../../tests/test_answer_quality_corpus.py#L231) | 231 | `""` | — |
| [SRC-4CCB1F172B-L000232](../../tests/test_answer_quality_corpus.py#L232) | 232 | `""` | — |
| [SRC-4CCB1F172B-L000233](../../tests/test_answer_quality_corpus.py#L233) | 233 | `"def test_human_review_template_matches_corpus_and_contains_no_scores():"` | — |
| [SRC-4CCB1F172B-L000234](../../tests/test_answer_quality_corpus.py#L234) | 234 | `"    template_path = CORPUS_PATH.parent / \"answer_quality_reviews_template.json\""` | — |
| [SRC-4CCB1F172B-L000235](../../tests/test_answer_quality_corpus.py#L235) | 235 | `"    assert template_path.is_file(), f\"Missing review template: {template_path}\""` | — |
| [SRC-4CCB1F172B-L000236](../../tests/test_answer_quality_corpus.py#L236) | 236 | `"    template = json.loads(template_path.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-4CCB1F172B-L000237](../../tests/test_answer_quality_corpus.py#L237) | 237 | `"    corpus = _load_corpus()"` | — |
| [SRC-4CCB1F172B-L000238](../../tests/test_answer_quality_corpus.py#L238) | 238 | `"    assert template.get(\"template_only\") is True"` | — |
| [SRC-4CCB1F172B-L000239](../../tests/test_answer_quality_corpus.py#L239) | 239 | `"    assert template.get(\"benchmark_id\") == corpus[\"benchmark_id\"]"` | — |
| [SRC-4CCB1F172B-L000240](../../tests/test_answer_quality_corpus.py#L240) | 240 | `"    assert template.get(\"benchmark_version\") == corpus[\"version\"]"` | — |
| [SRC-4CCB1F172B-L000241](../../tests/test_answer_quality_corpus.py#L241) | 241 | `"    case_ids = {case[\"case_id\"] for case in corpus[\"cases\"]}"` | — |
| [SRC-4CCB1F172B-L000242](../../tests/test_answer_quality_corpus.py#L242) | 242 | `"    reviews = template.get(\"reviews\")"` | — |
| [SRC-4CCB1F172B-L000243](../../tests/test_answer_quality_corpus.py#L243) | 243 | `"    assert isinstance(reviews, list)"` | — |
| [SRC-4CCB1F172B-L000244](../../tests/test_answer_quality_corpus.py#L244) | 244 | `"    assert {item.get(\"case_id\") for item in reviews} == case_ids"` | — |
| [SRC-4CCB1F172B-L000245](../../tests/test_answer_quality_corpus.py#L245) | 245 | `"    for item in reviews:"` | — |
| [SRC-4CCB1F172B-L000246](../../tests/test_answer_quality_corpus.py#L246) | 246 | `"        assert item[\"status\"] == \"NOT_TESTED\""` | — |
| [SRC-4CCB1F172B-L000247](../../tests/test_answer_quality_corpus.py#L247) | 247 | `"        assert \"correctness\" not in item"` | — |
| [SRC-4CCB1F172B-L000248](../../tests/test_answer_quality_corpus.py#L248) | 248 | `"        assert \"citations\" not in item"` | — |
| [SRC-4CCB1F172B-L000249](../../tests/test_answer_quality_corpus.py#L249) | 249 | `"        assert \"retrieval\" not in item"` | — |
| [SRC-4CCB1F172B-L000250](../../tests/test_answer_quality_corpus.py#L250) | 250 | `"        assert \"writing_quality\" not in item"` | — |
## اختبارات

### FILE-2477C41448 — [tests/test_answer_quality_provider_usage.py](../../tests/test_answer_quality_provider_usage.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-2477C41448-L000001](../../tests/test_answer_quality_provider_usage.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-2477C41448-L000002](../../tests/test_answer_quality_provider_usage.py#L2) | 2 | `""` | — |
| [SRC-2477C41448-L000003](../../tests/test_answer_quality_provider_usage.py#L3) | 3 | `"import json"` | — |
| [SRC-2477C41448-L000004](../../tests/test_answer_quality_provider_usage.py#L4) | 4 | `""` | — |
| [SRC-2477C41448-L000005](../../tests/test_answer_quality_provider_usage.py#L5) | 5 | `"from agents.web_agent import WebAgent, _normalized_provider_usage"` | — |
| [SRC-2477C41448-L000006](../../tests/test_answer_quality_provider_usage.py#L6) | 6 | `""` | — |
| [SRC-2477C41448-L000007](../../tests/test_answer_quality_provider_usage.py#L7) | 7 | `""` | — |
| [SRC-2477C41448-L000008](../../tests/test_answer_quality_provider_usage.py#L8) | 8 | `"def test_provider_usage_keeps_only_valid_numeric_fields_and_openrouter_usd_cost():"` | — |
| [SRC-2477C41448-L000009](../../tests/test_answer_quality_provider_usage.py#L9) | 9 | `"    usage = {"` | — |
| [SRC-2477C41448-L000010](../../tests/test_answer_quality_provider_usage.py#L10) | 10 | `"        \"prompt_tokens\": 18,"` | — |
| [SRC-2477C41448-L000011](../../tests/test_answer_quality_provider_usage.py#L11) | 11 | `"        \"completion_tokens\": 24,"` | — |
| [SRC-2477C41448-L000012](../../tests/test_answer_quality_provider_usage.py#L12) | 12 | `"        \"total_tokens\": 42,"` | — |
| [SRC-2477C41448-L000013](../../tests/test_answer_quality_provider_usage.py#L13) | 13 | `"        \"cost\": 0.00125,"` | — |
| [SRC-2477C41448-L000014](../../tests/test_answer_quality_provider_usage.py#L14) | 14 | `"        \"provider_private_payload\": \"must not be retained\","` | — |
| [SRC-2477C41448-L000015](../../tests/test_answer_quality_provider_usage.py#L15) | 15 | `"        \"prompt_tokens_text\": \"18\","` | — |
| [SRC-2477C41448-L000016](../../tests/test_answer_quality_provider_usage.py#L16) | 16 | `"    }"` | — |
| [SRC-2477C41448-L000017](../../tests/test_answer_quality_provider_usage.py#L17) | 17 | `"    normalized = _normalized_provider_usage("` | — |
| [SRC-2477C41448-L000018](../../tests/test_answer_quality_provider_usage.py#L18) | 18 | `"        usage, provider_base_url=\"https://openrouter.ai/api/v1\""` | — |
| [SRC-2477C41448-L000019](../../tests/test_answer_quality_provider_usage.py#L19) | 19 | `"    )"` | — |
| [SRC-2477C41448-L000020](../../tests/test_answer_quality_provider_usage.py#L20) | 20 | `"    assert normalized == {"` | — |
| [SRC-2477C41448-L000021](../../tests/test_answer_quality_provider_usage.py#L21) | 21 | `"        \"prompt_tokens\": 18,"` | — |
| [SRC-2477C41448-L000022](../../tests/test_answer_quality_provider_usage.py#L22) | 22 | `"        \"completion_tokens\": 24,"` | — |
| [SRC-2477C41448-L000023](../../tests/test_answer_quality_provider_usage.py#L23) | 23 | `"        \"total_tokens\": 42,"` | — |
| [SRC-2477C41448-L000024](../../tests/test_answer_quality_provider_usage.py#L24) | 24 | `"        \"cost_usd\": 0.00125,"` | — |
| [SRC-2477C41448-L000025](../../tests/test_answer_quality_provider_usage.py#L25) | 25 | `"    }"` | — |
| [SRC-2477C41448-L000026](../../tests/test_answer_quality_provider_usage.py#L26) | 26 | `""` | — |
| [SRC-2477C41448-L000027](../../tests/test_answer_quality_provider_usage.py#L27) | 27 | `""` | — |
| [SRC-2477C41448-L000028](../../tests/test_answer_quality_provider_usage.py#L28) | 28 | `"def test_generic_provider_cost_is_not_assumed_to_be_usd():"` | — |
| [SRC-2477C41448-L000029](../../tests/test_answer_quality_provider_usage.py#L29) | 29 | `"    normalized = _normalized_provider_usage("` | — |
| [SRC-2477C41448-L000030](../../tests/test_answer_quality_provider_usage.py#L30) | 30 | `"        {\"prompt_tokens\": 5, \"cost\": 0.05},"` | — |
| [SRC-2477C41448-L000031](../../tests/test_answer_quality_provider_usage.py#L31) | 31 | `"        provider_base_url=\"https://custom-provider.example/v1\","` | — |
| [SRC-2477C41448-L000032](../../tests/test_answer_quality_provider_usage.py#L32) | 32 | `"    )"` | — |
| [SRC-2477C41448-L000033](../../tests/test_answer_quality_provider_usage.py#L33) | 33 | `"    assert normalized == {\"prompt_tokens\": 5}"` | — |
| [SRC-2477C41448-L000034](../../tests/test_answer_quality_provider_usage.py#L34) | 34 | `""` | — |
| [SRC-2477C41448-L000035](../../tests/test_answer_quality_provider_usage.py#L35) | 35 | `""` | — |
| [SRC-2477C41448-L000036](../../tests/test_answer_quality_provider_usage.py#L36) | 36 | `"def test_nonfinite_or_negative_provider_cost_is_not_recorded():"` | — |
| [SRC-2477C41448-L000037](../../tests/test_answer_quality_provider_usage.py#L37) | 37 | `"    normalized = _normalized_provider_usage("` | — |
| [SRC-2477C41448-L000038](../../tests/test_answer_quality_provider_usage.py#L38) | 38 | `"        {\"prompt_tokens\": 2, \"cost\": float(\"nan\"), \"total_cost\": -1},"` | — |
| [SRC-2477C41448-L000039](../../tests/test_answer_quality_provider_usage.py#L39) | 39 | `"        provider_base_url=\"https://openrouter.ai/api/v1\","` | — |
| [SRC-2477C41448-L000040](../../tests/test_answer_quality_provider_usage.py#L40) | 40 | `"    )"` | — |
| [SRC-2477C41448-L000041](../../tests/test_answer_quality_provider_usage.py#L41) | 41 | `"    assert normalized == {\"prompt_tokens\": 2}"` | — |
| [SRC-2477C41448-L000042](../../tests/test_answer_quality_provider_usage.py#L42) | 42 | `""` | — |
| [SRC-2477C41448-L000043](../../tests/test_answer_quality_provider_usage.py#L43) | 43 | `""` | — |
| [SRC-2477C41448-L000044](../../tests/test_answer_quality_provider_usage.py#L44) | 44 | `"def test_completion_records_provider_usage_without_retaining_provider_body(monkeypatch):"` | — |
| [SRC-2477C41448-L000045](../../tests/test_answer_quality_provider_usage.py#L45) | 45 | `"    agent = WebAgent()"` | — |
| [SRC-2477C41448-L000046](../../tests/test_answer_quality_provider_usage.py#L46) | 46 | `"    agent.api_key = \"unit-test-key\""` | — |
| [SRC-2477C41448-L000047](../../tests/test_answer_quality_provider_usage.py#L47) | 47 | `"    agent.base_url = \"https://openrouter.ai/api/v1\""` | — |
| [SRC-2477C41448-L000048](../../tests/test_answer_quality_provider_usage.py#L48) | 48 | `"    agent.fallback_model = \"\""` | — |
| [SRC-2477C41448-L000049](../../tests/test_answer_quality_provider_usage.py#L49) | 49 | `""` | — |
| [SRC-2477C41448-L000050](../../tests/test_answer_quality_provider_usage.py#L50) | 50 | `"    class FakeResponse:"` | — |
| [SRC-2477C41448-L000051](../../tests/test_answer_quality_provider_usage.py#L51) | 51 | `"        status = 200"` | — |
| [SRC-2477C41448-L000052](../../tests/test_answer_quality_provider_usage.py#L52) | 52 | `""` | — |
| [SRC-2477C41448-L000053](../../tests/test_answer_quality_provider_usage.py#L53) | 53 | `"        def __enter__(self):"` | — |
| [SRC-2477C41448-L000054](../../tests/test_answer_quality_provider_usage.py#L54) | 54 | `"            return self"` | — |
| [SRC-2477C41448-L000055](../../tests/test_answer_quality_provider_usage.py#L55) | 55 | `""` | — |
| [SRC-2477C41448-L000056](../../tests/test_answer_quality_provider_usage.py#L56) | 56 | `"        def __exit__(self, exc_type, exc, traceback):"` | — |
| [SRC-2477C41448-L000057](../../tests/test_answer_quality_provider_usage.py#L57) | 57 | `"            return False"` | — |
| [SRC-2477C41448-L000058](../../tests/test_answer_quality_provider_usage.py#L58) | 58 | `""` | — |
| [SRC-2477C41448-L000059](../../tests/test_answer_quality_provider_usage.py#L59) | 59 | `"        def read(self, limit):"` | — |
| [SRC-2477C41448-L000060](../../tests/test_answer_quality_provider_usage.py#L60) | 60 | `"            return json.dumps({"` | — |
| [SRC-2477C41448-L000061](../../tests/test_answer_quality_provider_usage.py#L61) | 61 | `"                \"choices\": [{"` | — |
| [SRC-2477C41448-L000062](../../tests/test_answer_quality_provider_usage.py#L62) | 62 | `"                    \"message\": {\"content\": \"إجابة اختبارية\"},"` | — |
| [SRC-2477C41448-L000063](../../tests/test_answer_quality_provider_usage.py#L63) | 63 | `"                    \"finish_reason\": \"stop\","` | — |
| [SRC-2477C41448-L000064](../../tests/test_answer_quality_provider_usage.py#L64) | 64 | `"                }],"` | — |
| [SRC-2477C41448-L000065](../../tests/test_answer_quality_provider_usage.py#L65) | 65 | `"                \"usage\": {"` | — |
| [SRC-2477C41448-L000066](../../tests/test_answer_quality_provider_usage.py#L66) | 66 | `"                    \"prompt_tokens\": 10,"` | — |
| [SRC-2477C41448-L000067](../../tests/test_answer_quality_provider_usage.py#L67) | 67 | `"                    \"completion_tokens\": 7,"` | — |
| [SRC-2477C41448-L000068](../../tests/test_answer_quality_provider_usage.py#L68) | 68 | `"                    \"total_tokens\": 17,"` | — |
| [SRC-2477C41448-L000069](../../tests/test_answer_quality_provider_usage.py#L69) | 69 | `"                    \"cost\": 0.0004,"` | — |
| [SRC-2477C41448-L000070](../../tests/test_answer_quality_provider_usage.py#L70) | 70 | `"                    \"debug_blob\": \"private-provider-details\","` | — |
| [SRC-2477C41448-L000071](../../tests/test_answer_quality_provider_usage.py#L71) | 71 | `"                },"` | — |
| [SRC-2477C41448-L000072](../../tests/test_answer_quality_provider_usage.py#L72) | 72 | `"            }).encode(\"utf-8\")"` | — |
| [SRC-2477C41448-L000073](../../tests/test_answer_quality_provider_usage.py#L73) | 73 | `""` | — |
| [SRC-2477C41448-L000074](../../tests/test_answer_quality_provider_usage.py#L74) | 74 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", lambda request, timeout: FakeResponse())"` | — |
| [SRC-2477C41448-L000075](../../tests/test_answer_quality_provider_usage.py#L75) | 75 | `"    answer = agent._request_completion("` | — |
| [SRC-2477C41448-L000076](../../tests/test_answer_quality_provider_usage.py#L76) | 76 | `"        [{\"role\": \"user\", \"content\": \"اختبر\"}],"` | — |
| [SRC-2477C41448-L000077](../../tests/test_answer_quality_provider_usage.py#L77) | 77 | `"        model=\"test/model\","` | — |
| [SRC-2477C41448-L000078](../../tests/test_answer_quality_provider_usage.py#L78) | 78 | `"    )"` | — |
| [SRC-2477C41448-L000079](../../tests/test_answer_quality_provider_usage.py#L79) | 79 | `"    assert answer == \"إجابة اختبارية\""` | — |
| [SRC-2477C41448-L000080](../../tests/test_answer_quality_provider_usage.py#L80) | 80 | `"    assert agent.model_usage[0][\"provider_usage\"] == {"` | — |
| [SRC-2477C41448-L000081](../../tests/test_answer_quality_provider_usage.py#L81) | 81 | `"        \"prompt_tokens\": 10,"` | — |
| [SRC-2477C41448-L000082](../../tests/test_answer_quality_provider_usage.py#L82) | 82 | `"        \"completion_tokens\": 7,"` | — |
| [SRC-2477C41448-L000083](../../tests/test_answer_quality_provider_usage.py#L83) | 83 | `"        \"total_tokens\": 17,"` | — |
| [SRC-2477C41448-L000084](../../tests/test_answer_quality_provider_usage.py#L84) | 84 | `"        \"cost_usd\": 0.0004,"` | — |
| [SRC-2477C41448-L000085](../../tests/test_answer_quality_provider_usage.py#L85) | 85 | `"    }"` | — |
| [SRC-2477C41448-L000086](../../tests/test_answer_quality_provider_usage.py#L86) | 86 | `"    assert \"debug_blob\" not in str(agent.model_usage)"` | — |
## اختبارات

### FILE-D186ED3822 — [tests/test_answer_quality_review_scorecard.py](../../tests/test_answer_quality_review_scorecard.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-D186ED3822-L000001](../../tests/test_answer_quality_review_scorecard.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-D186ED3822-L000002](../../tests/test_answer_quality_review_scorecard.py#L2) | 2 | `""` | — |
| [SRC-D186ED3822-L000003](../../tests/test_answer_quality_review_scorecard.py#L3) | 3 | `"import importlib.util"` | — |
| [SRC-D186ED3822-L000004](../../tests/test_answer_quality_review_scorecard.py#L4) | 4 | `"from pathlib import Path"` | — |
| [SRC-D186ED3822-L000005](../../tests/test_answer_quality_review_scorecard.py#L5) | 5 | `""` | — |
| [SRC-D186ED3822-L000006](../../tests/test_answer_quality_review_scorecard.py#L6) | 6 | `"import pytest"` | — |
| [SRC-D186ED3822-L000007](../../tests/test_answer_quality_review_scorecard.py#L7) | 7 | `""` | — |
| [SRC-D186ED3822-L000008](../../tests/test_answer_quality_review_scorecard.py#L8) | 8 | `"ROOT = Path(__file__).resolve().parents[1]"` | — |
| [SRC-D186ED3822-L000009](../../tests/test_answer_quality_review_scorecard.py#L9) | 9 | `"SCRIPT = ROOT / \"scripts\" / \"score_answer_quality_reviews.py\""` | — |
| [SRC-D186ED3822-L000010](../../tests/test_answer_quality_review_scorecard.py#L10) | 10 | `"CORPUS_PATH = ROOT / \"tests\" / \"fixtures\" / \"answer_quality_cases.json\""` | — |
| [SRC-D186ED3822-L000011](../../tests/test_answer_quality_review_scorecard.py#L11) | 11 | `""` | — |
| [SRC-D186ED3822-L000012](../../tests/test_answer_quality_review_scorecard.py#L12) | 12 | `""` | — |
| [SRC-D186ED3822-L000013](../../tests/test_answer_quality_review_scorecard.py#L13) | 13 | `"def load_module():"` | — |
| [SRC-D186ED3822-L000014](../../tests/test_answer_quality_review_scorecard.py#L14) | 14 | `"    spec = importlib.util.spec_from_file_location(\"answer_quality_review_scorecard\", SCRIPT)"` | — |
| [SRC-D186ED3822-L000015](../../tests/test_answer_quality_review_scorecard.py#L15) | 15 | `"    assert spec and spec.loader"` | — |
| [SRC-D186ED3822-L000016](../../tests/test_answer_quality_review_scorecard.py#L16) | 16 | `"    module = importlib.util.module_from_spec(spec)"` | — |
| [SRC-D186ED3822-L000017](../../tests/test_answer_quality_review_scorecard.py#L17) | 17 | `"    spec.loader.exec_module(module)"` | — |
| [SRC-D186ED3822-L000018](../../tests/test_answer_quality_review_scorecard.py#L18) | 18 | `"    return module"` | — |
| [SRC-D186ED3822-L000019](../../tests/test_answer_quality_review_scorecard.py#L19) | 19 | `""` | — |
| [SRC-D186ED3822-L000020](../../tests/test_answer_quality_review_scorecard.py#L20) | 20 | `""` | — |
| [SRC-D186ED3822-L000021](../../tests/test_answer_quality_review_scorecard.py#L21) | 21 | `"def corpus():"` | — |
| [SRC-D186ED3822-L000022](../../tests/test_answer_quality_review_scorecard.py#L22) | 22 | `"    return load_module().load_json_object(CORPUS_PATH)"` | — |
| [SRC-D186ED3822-L000023](../../tests/test_answer_quality_review_scorecard.py#L23) | 23 | `""` | — |
| [SRC-D186ED3822-L000024](../../tests/test_answer_quality_review_scorecard.py#L24) | 24 | `""` | — |
| [SRC-D186ED3822-L000025](../../tests/test_answer_quality_review_scorecard.py#L25) | 25 | `"def test_manual_scorecard_aggregates_only_explicit_reviewed_metrics():"` | — |
| [SRC-D186ED3822-L000026](../../tests/test_answer_quality_review_scorecard.py#L26) | 26 | `"    mod = load_module()"` | — |
| [SRC-D186ED3822-L000027](../../tests/test_answer_quality_review_scorecard.py#L27) | 27 | `"    data = {"` | — |
| [SRC-D186ED3822-L000028](../../tests/test_answer_quality_review_scorecard.py#L28) | 28 | `"        \"schema_version\": \"1.0\","` | — |
| [SRC-D186ED3822-L000029](../../tests/test_answer_quality_review_scorecard.py#L29) | 29 | `"        \"reviews\": ["` | — |
| [SRC-D186ED3822-L000030](../../tests/test_answer_quality_review_scorecard.py#L30) | 30 | `"            {"` | — |
| [SRC-D186ED3822-L000031](../../tests/test_answer_quality_review_scorecard.py#L31) | 31 | `"                \"case_id\": \"AQ-007\","` | — |
| [SRC-D186ED3822-L000032](../../tests/test_answer_quality_review_scorecard.py#L32) | 32 | `"                \"status\": \"REVIEWED\","` | — |
| [SRC-D186ED3822-L000033](../../tests/test_answer_quality_review_scorecard.py#L33) | 33 | `"                \"retrieval\": {\"relevant_retrieved\": 3, \"retrieved_count\": 5, \"relevant_available\": 4},"` | — |
| [SRC-D186ED3822-L000034](../../tests/test_answer_quality_review_scorecard.py#L34) | 34 | `"                \"faithfulness\": {\"supported_claims\": 4, \"reviewed_claims\": 5},"` | — |
| [SRC-D186ED3822-L000035](../../tests/test_answer_quality_review_scorecard.py#L35) | 35 | `"                \"correctness\": {\"correct_facts\": 3, \"reviewed_facts\": 4},"` | — |
| [SRC-D186ED3822-L000036](../../tests/test_answer_quality_review_scorecard.py#L36) | 36 | `"                \"citations\": {\"supported_citations\": 2, \"reviewed_citations\": 3},"` | — |
| [SRC-D186ED3822-L000037](../../tests/test_answer_quality_review_scorecard.py#L37) | 37 | `"                \"writing_quality\": 4,"` | — |
| [SRC-D186ED3822-L000038](../../tests/test_answer_quality_review_scorecard.py#L38) | 38 | `"            },"` | — |
| [SRC-D186ED3822-L000039](../../tests/test_answer_quality_review_scorecard.py#L39) | 39 | `"            {"` | — |
| [SRC-D186ED3822-L000040](../../tests/test_answer_quality_review_scorecard.py#L40) | 40 | `"                \"case_id\": \"AQ-008\","` | — |
| [SRC-D186ED3822-L000041](../../tests/test_answer_quality_review_scorecard.py#L41) | 41 | `"                \"status\": \"REVIEWED\","` | — |
| [SRC-D186ED3822-L000042](../../tests/test_answer_quality_review_scorecard.py#L42) | 42 | `"                \"writing_quality\": 4,"` | — |
| [SRC-D186ED3822-L000043](../../tests/test_answer_quality_review_scorecard.py#L43) | 43 | `"            },"` | — |
| [SRC-D186ED3822-L000044](../../tests/test_answer_quality_review_scorecard.py#L44) | 44 | `"            {\"case_id\": \"AQ-009\", \"status\": \"NOT_TESTED\", \"notes\": \"No reviewer judgment yet.\"},"` | — |
| [SRC-D186ED3822-L000045](../../tests/test_answer_quality_review_scorecard.py#L45) | 45 | `"        ],"` | — |
| [SRC-D186ED3822-L000046](../../tests/test_answer_quality_review_scorecard.py#L46) | 46 | `"    }"` | — |
| [SRC-D186ED3822-L000047](../../tests/test_answer_quality_review_scorecard.py#L47) | 47 | `"    result = mod.summarize_reviews(data, corpus())"` | — |
| [SRC-D186ED3822-L000048](../../tests/test_answer_quality_review_scorecard.py#L48) | 48 | `"    assert result[\"metrics\"][\"retrieval_precision\"][\"score\"] == 0.6"` | — |
| [SRC-D186ED3822-L000049](../../tests/test_answer_quality_review_scorecard.py#L49) | 49 | `"    assert result[\"metrics\"][\"retrieval_recall\"][\"score\"] == 0.75"` | — |
| [SRC-D186ED3822-L000050](../../tests/test_answer_quality_review_scorecard.py#L50) | 50 | `"    assert result[\"metrics\"][\"faithfulness\"][\"score\"] == 0.8"` | — |
| [SRC-D186ED3822-L000051](../../tests/test_answer_quality_review_scorecard.py#L51) | 51 | `"    assert result[\"metrics\"][\"correctness\"][\"score\"] == 0.75"` | — |
| [SRC-D186ED3822-L000052](../../tests/test_answer_quality_review_scorecard.py#L52) | 52 | `"    assert result[\"metrics\"][\"citation_support\"][\"score\"] == pytest.approx(2 / 3, abs=0.0001)"` | — |
| [SRC-D186ED3822-L000053](../../tests/test_answer_quality_review_scorecard.py#L53) | 53 | `"    assert result[\"metrics\"][\"writing_quality_1_to_5\"][\"score\"] == 4.0"` | — |
| [SRC-D186ED3822-L000054](../../tests/test_answer_quality_review_scorecard.py#L54) | 54 | `"    assert result[\"case_status_counts\"][\"NOT_TESTED\"] == 1"` | — |
| [SRC-D186ED3822-L000055](../../tests/test_answer_quality_review_scorecard.py#L55) | 55 | `"    assert result[\"unique_reviewed_case_count\"] == 2"` | — |
| [SRC-D186ED3822-L000056](../../tests/test_answer_quality_review_scorecard.py#L56) | 56 | `"    assert result[\"automatic_answer_grading\"] is False"` | — |
| [SRC-D186ED3822-L000057](../../tests/test_answer_quality_review_scorecard.py#L57) | 57 | `"    assert result[\"ragas_executed\"] is False"` | — |
| [SRC-D186ED3822-L000058](../../tests/test_answer_quality_review_scorecard.py#L58) | 58 | `""` | — |
| [SRC-D186ED3822-L000059](../../tests/test_answer_quality_review_scorecard.py#L59) | 59 | `""` | — |
| [SRC-D186ED3822-L000060](../../tests/test_answer_quality_review_scorecard.py#L60) | 60 | `"def test_scorecard_keeps_unmeasured_denominators_not_scorable():"` | — |
| [SRC-D186ED3822-L000061](../../tests/test_answer_quality_review_scorecard.py#L61) | 61 | `"    mod = load_module()"` | — |
| [SRC-D186ED3822-L000062](../../tests/test_answer_quality_review_scorecard.py#L62) | 62 | `"    data = {"` | — |
| [SRC-D186ED3822-L000063](../../tests/test_answer_quality_review_scorecard.py#L63) | 63 | `"        \"reviews\": [{"` | — |
| [SRC-D186ED3822-L000064](../../tests/test_answer_quality_review_scorecard.py#L64) | 64 | `"            \"case_id\": \"AQ-001\","` | — |
| [SRC-D186ED3822-L000065](../../tests/test_answer_quality_review_scorecard.py#L65) | 65 | `"            \"status\": \"REVIEWED\","` | — |
| [SRC-D186ED3822-L000066](../../tests/test_answer_quality_review_scorecard.py#L66) | 66 | `"            \"faithfulness\": {\"supported_claims\": 0, \"reviewed_claims\": 0},"` | — |
| [SRC-D186ED3822-L000067](../../tests/test_answer_quality_review_scorecard.py#L67) | 67 | `"        }],"` | — |
| [SRC-D186ED3822-L000068](../../tests/test_answer_quality_review_scorecard.py#L68) | 68 | `"    }"` | — |
| [SRC-D186ED3822-L000069](../../tests/test_answer_quality_review_scorecard.py#L69) | 69 | `"    result = mod.summarize_reviews(data, corpus())"` | — |
| [SRC-D186ED3822-L000070](../../tests/test_answer_quality_review_scorecard.py#L70) | 70 | `"    assert result[\"metrics\"][\"faithfulness\"][\"score\"] is None"` | — |
| [SRC-D186ED3822-L000071](../../tests/test_answer_quality_review_scorecard.py#L71) | 71 | `"    assert result[\"metrics\"][\"faithfulness\"][\"status\"] == \"NOT_SCORABLE_NO_ANNOTATED_DENOMINATOR\""` | — |
| [SRC-D186ED3822-L000072](../../tests/test_answer_quality_review_scorecard.py#L72) | 72 | `"    assert result[\"metrics\"][\"retrieval_precision\"][\"score\"] is None"` | — |
| [SRC-D186ED3822-L000073](../../tests/test_answer_quality_review_scorecard.py#L73) | 73 | `""` | — |
| [SRC-D186ED3822-L000074](../../tests/test_answer_quality_review_scorecard.py#L74) | 74 | `""` | — |
| [SRC-D186ED3822-L000075](../../tests/test_answer_quality_review_scorecard.py#L75) | 75 | `"def test_scorecard_rejects_numerator_larger_than_denominator():"` | — |
| [SRC-D186ED3822-L000076](../../tests/test_answer_quality_review_scorecard.py#L76) | 76 | `"    mod = load_module()"` | — |
| [SRC-D186ED3822-L000077](../../tests/test_answer_quality_review_scorecard.py#L77) | 77 | `"    data = {"` | — |
| [SRC-D186ED3822-L000078](../../tests/test_answer_quality_review_scorecard.py#L78) | 78 | `"        \"reviews\": [{"` | — |
| [SRC-D186ED3822-L000079](../../tests/test_answer_quality_review_scorecard.py#L79) | 79 | `"            \"case_id\": \"AQ-007\","` | — |
| [SRC-D186ED3822-L000080](../../tests/test_answer_quality_review_scorecard.py#L80) | 80 | `"            \"status\": \"REVIEWED\","` | — |
| [SRC-D186ED3822-L000081](../../tests/test_answer_quality_review_scorecard.py#L81) | 81 | `"            \"faithfulness\": {\"supported_claims\": 3, \"reviewed_claims\": 2},"` | — |
| [SRC-D186ED3822-L000082](../../tests/test_answer_quality_review_scorecard.py#L82) | 82 | `"        }],"` | — |
| [SRC-D186ED3822-L000083](../../tests/test_answer_quality_review_scorecard.py#L83) | 83 | `"    }"` | — |
| [SRC-D186ED3822-L000084](../../tests/test_answer_quality_review_scorecard.py#L84) | 84 | `"    with pytest.raises(ValueError, match=\"cannot exceed\"):"` | — |
| [SRC-D186ED3822-L000085](../../tests/test_answer_quality_review_scorecard.py#L85) | 85 | `"        mod.summarize_reviews(data, corpus())"` | — |
| [SRC-D186ED3822-L000086](../../tests/test_answer_quality_review_scorecard.py#L86) | 86 | `""` | — |
| [SRC-D186ED3822-L000087](../../tests/test_answer_quality_review_scorecard.py#L87) | 87 | `""` | — |
| [SRC-D186ED3822-L000088](../../tests/test_answer_quality_review_scorecard.py#L88) | 88 | `"def test_scorecard_rejects_unknown_case_ids_and_duplicate_reviews():"` | — |
| [SRC-D186ED3822-L000089](../../tests/test_answer_quality_review_scorecard.py#L89) | 89 | `"    mod = load_module()"` | — |
| [SRC-D186ED3822-L000090](../../tests/test_answer_quality_review_scorecard.py#L90) | 90 | `"    data = {\"reviews\": ["` | — |
| [SRC-D186ED3822-L000091](../../tests/test_answer_quality_review_scorecard.py#L91) | 91 | `"        {\"case_id\": \"AQ-999\", \"status\": \"NOT_TESTED\"},"` | — |
| [SRC-D186ED3822-L000092](../../tests/test_answer_quality_review_scorecard.py#L92) | 92 | `"        {\"case_id\": \"AQ-001\", \"status\": \"NOT_TESTED\"},"` | — |
| [SRC-D186ED3822-L000093](../../tests/test_answer_quality_review_scorecard.py#L93) | 93 | `"        {\"case_id\": \"AQ-001\", \"status\": \"NOT_TESTED\"},"` | — |
| [SRC-D186ED3822-L000094](../../tests/test_answer_quality_review_scorecard.py#L94) | 94 | `"    ]}"` | — |
| [SRC-D186ED3822-L000095](../../tests/test_answer_quality_review_scorecard.py#L95) | 95 | `"    issues = mod.validate_reviews(data, corpus())"` | — |
| [SRC-D186ED3822-L000096](../../tests/test_answer_quality_review_scorecard.py#L96) | 96 | `"    assert any(\"unknown case_id\" in issue for issue in issues)"` | — |
| [SRC-D186ED3822-L000097](../../tests/test_answer_quality_review_scorecard.py#L97) | 97 | `"    assert any(\"duplicate review\" in issue for issue in issues)"` | — |
| [SRC-D186ED3822-L000098](../../tests/test_answer_quality_review_scorecard.py#L98) | 98 | `""` | — |
| [SRC-D186ED3822-L000099](../../tests/test_answer_quality_review_scorecard.py#L99) | 99 | `""` | — |
| [SRC-D186ED3822-L000100](../../tests/test_answer_quality_review_scorecard.py#L100) | 100 | `"def test_not_tested_cases_must_not_carry_metric_scores():"` | — |
| [SRC-D186ED3822-L000101](../../tests/test_answer_quality_review_scorecard.py#L101) | 101 | `"    mod = load_module()"` | — |
| [SRC-D186ED3822-L000102](../../tests/test_answer_quality_review_scorecard.py#L102) | 102 | `"    data = {\"reviews\": [{"` | — |
| [SRC-D186ED3822-L000103](../../tests/test_answer_quality_review_scorecard.py#L103) | 103 | `"        \"case_id\": \"AQ-001\", \"status\": \"NOT_TESTED\","` | — |
| [SRC-D186ED3822-L000104](../../tests/test_answer_quality_review_scorecard.py#L104) | 104 | `"        \"writing_quality\": 5,"` | — |
| [SRC-D186ED3822-L000105](../../tests/test_answer_quality_review_scorecard.py#L105) | 105 | `"    }]}"` | — |
| [SRC-D186ED3822-L000106](../../tests/test_answer_quality_review_scorecard.py#L106) | 106 | `"    issues = mod.validate_reviews(data, corpus())"` | — |
| [SRC-D186ED3822-L000107](../../tests/test_answer_quality_review_scorecard.py#L107) | 107 | `"    assert any(\"unreviewed case must not contain metric scores\" in issue for issue in issues)"` | — |
| [SRC-D186ED3822-L000108](../../tests/test_answer_quality_review_scorecard.py#L108) | 108 | `""` | — |
| [SRC-D186ED3822-L000109](../../tests/test_answer_quality_review_scorecard.py#L109) | 109 | `""` | — |
| [SRC-D186ED3822-L000110](../../tests/test_answer_quality_review_scorecard.py#L110) | 110 | `"def test_scorecard_cli_writes_a_machine_readable_summary(tmp_path, capsys):"` | — |
| [SRC-D186ED3822-L000111](../../tests/test_answer_quality_review_scorecard.py#L111) | 111 | `"    mod = load_module()"` | — |
| [SRC-D186ED3822-L000112](../../tests/test_answer_quality_review_scorecard.py#L112) | 112 | `"    reviews_path = tmp_path / \"reviews.json\""` | — |
| [SRC-D186ED3822-L000113](../../tests/test_answer_quality_review_scorecard.py#L113) | 113 | `"    output_path = tmp_path / \"summary.json\""` | — |
| [SRC-D186ED3822-L000114](../../tests/test_answer_quality_review_scorecard.py#L114) | 114 | `"    reviews_path.write_text('{\"schema_version\":\"1.0\",\"reviews\":[{\"case_id\":\"AQ-001\",\"status\":\"REVIEWED\",\"writing_quality\":5}]}', encoding=\"utf-8\")"` | — |
| [SRC-D186ED3822-L000115](../../tests/test_answer_quality_review_scorecard.py#L115) | 115 | `"    rc = mod.main([\"--reviews\", str(reviews_path), \"--corpus\", str(CORPUS_PATH), \"--out\", str(output_path)])"` | — |
| [SRC-D186ED3822-L000116](../../tests/test_answer_quality_review_scorecard.py#L116) | 116 | `"    assert rc == 0"` | — |
| [SRC-D186ED3822-L000117](../../tests/test_answer_quality_review_scorecard.py#L117) | 117 | `"    assert '\"score\": 5.0' in capsys.readouterr().out"` | — |
| [SRC-D186ED3822-L000118](../../tests/test_answer_quality_review_scorecard.py#L118) | 118 | `"    assert output_path.is_file()"` | — |
## اختبارات

### FILE-B3062EB677 — [tests/test_answer_quality_runner.py](../../tests/test_answer_quality_runner.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-B3062EB677-L000001](../../tests/test_answer_quality_runner.py#L1) | 1 | `"\"\"\"Offline tests for scripts/run_answer_quality_benchmark.py (no network).\"\"\""` | — |
| [SRC-B3062EB677-L000002](../../tests/test_answer_quality_runner.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-B3062EB677-L000003](../../tests/test_answer_quality_runner.py#L3) | 3 | `""` | — |
| [SRC-B3062EB677-L000004](../../tests/test_answer_quality_runner.py#L4) | 4 | `"import importlib.util"` | — |
| [SRC-B3062EB677-L000005](../../tests/test_answer_quality_runner.py#L5) | 5 | `"import json"` | — |
| [SRC-B3062EB677-L000006](../../tests/test_answer_quality_runner.py#L6) | 6 | `"import sys"` | — |
| [SRC-B3062EB677-L000007](../../tests/test_answer_quality_runner.py#L7) | 7 | `"from pathlib import Path"` | — |
| [SRC-B3062EB677-L000008](../../tests/test_answer_quality_runner.py#L8) | 8 | `""` | — |
| [SRC-B3062EB677-L000009](../../tests/test_answer_quality_runner.py#L9) | 9 | `"import pytest"` | — |
| [SRC-B3062EB677-L000010](../../tests/test_answer_quality_runner.py#L10) | 10 | `""` | — |
| [SRC-B3062EB677-L000011](../../tests/test_answer_quality_runner.py#L11) | 11 | `"ROOT = Path(__file__).resolve().parents[1]"` | — |
| [SRC-B3062EB677-L000012](../../tests/test_answer_quality_runner.py#L12) | 12 | `"SCRIPT = ROOT / \"scripts\" / \"run_answer_quality_benchmark.py\""` | — |
| [SRC-B3062EB677-L000013](../../tests/test_answer_quality_runner.py#L13) | 13 | `"CORPUS = ROOT / \"tests\" / \"fixtures\" / \"answer_quality_cases.json\""` | — |
| [SRC-B3062EB677-L000014](../../tests/test_answer_quality_runner.py#L14) | 14 | `""` | — |
| [SRC-B3062EB677-L000015](../../tests/test_answer_quality_runner.py#L15) | 15 | `""` | — |
| [SRC-B3062EB677-L000016](../../tests/test_answer_quality_runner.py#L16) | 16 | `"def _load_runner():"` | — |
| [SRC-B3062EB677-L000017](../../tests/test_answer_quality_runner.py#L17) | 17 | `"    spec = importlib.util.spec_from_file_location(\"aq_runner\", SCRIPT)"` | — |
| [SRC-B3062EB677-L000018](../../tests/test_answer_quality_runner.py#L18) | 18 | `"    assert spec and spec.loader"` | — |
| [SRC-B3062EB677-L000019](../../tests/test_answer_quality_runner.py#L19) | 19 | `"    mod = importlib.util.module_from_spec(spec)"` | — |
| [SRC-B3062EB677-L000020](../../tests/test_answer_quality_runner.py#L20) | 20 | `"    sys.modules[\"aq_runner\"] = mod"` | — |
| [SRC-B3062EB677-L000021](../../tests/test_answer_quality_runner.py#L21) | 21 | `"    spec.loader.exec_module(mod)"` | — |
| [SRC-B3062EB677-L000022](../../tests/test_answer_quality_runner.py#L22) | 22 | `"    return mod"` | — |
| [SRC-B3062EB677-L000023](../../tests/test_answer_quality_runner.py#L23) | 23 | `""` | — |
| [SRC-B3062EB677-L000024](../../tests/test_answer_quality_runner.py#L24) | 24 | `""` | — |
| [SRC-B3062EB677-L000025](../../tests/test_answer_quality_runner.py#L25) | 25 | `"def test_runner_script_exists():"` | — |
| [SRC-B3062EB677-L000026](../../tests/test_answer_quality_runner.py#L26) | 26 | `"    assert SCRIPT.is_file()"` | — |
| [SRC-B3062EB677-L000027](../../tests/test_answer_quality_runner.py#L27) | 27 | `""` | — |
| [SRC-B3062EB677-L000028](../../tests/test_answer_quality_runner.py#L28) | 28 | `""` | — |
| [SRC-B3062EB677-L000029](../../tests/test_answer_quality_runner.py#L29) | 29 | `"def test_validate_mode_succeeds_on_real_corpus(capsys):"` | — |
| [SRC-B3062EB677-L000030](../../tests/test_answer_quality_runner.py#L30) | 30 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000031](../../tests/test_answer_quality_runner.py#L31) | 31 | `"    rc = mod.main([\"--mode\", \"validate\", \"--corpus\", str(CORPUS), \"--summary\"])"` | — |
| [SRC-B3062EB677-L000032](../../tests/test_answer_quality_runner.py#L32) | 32 | `"    assert rc == 0"` | — |
| [SRC-B3062EB677-L000033](../../tests/test_answer_quality_runner.py#L33) | 33 | `"    out = capsys.readouterr().out"` | — |
| [SRC-B3062EB677-L000034](../../tests/test_answer_quality_runner.py#L34) | 34 | `"    assert \"VALIDATE OK\" in out"` | — |
| [SRC-B3062EB677-L000035](../../tests/test_answer_quality_runner.py#L35) | 35 | `"    assert \"NOT_TESTED\" in out"` | — |
| [SRC-B3062EB677-L000036](../../tests/test_answer_quality_runner.py#L36) | 36 | `""` | — |
| [SRC-B3062EB677-L000037](../../tests/test_answer_quality_runner.py#L37) | 37 | `""` | — |
| [SRC-B3062EB677-L000038](../../tests/test_answer_quality_runner.py#L38) | 38 | `"def test_validate_rejects_missing_file(tmp_path):"` | — |
| [SRC-B3062EB677-L000039](../../tests/test_answer_quality_runner.py#L39) | 39 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000040](../../tests/test_answer_quality_runner.py#L40) | 40 | `"    missing = tmp_path / \"nope.json\""` | — |
| [SRC-B3062EB677-L000041](../../tests/test_answer_quality_runner.py#L41) | 41 | `"    with pytest.raises(FileNotFoundError):"` | — |
| [SRC-B3062EB677-L000042](../../tests/test_answer_quality_runner.py#L42) | 42 | `"        mod.load_corpus(missing)"` | — |
| [SRC-B3062EB677-L000043](../../tests/test_answer_quality_runner.py#L43) | 43 | `""` | — |
| [SRC-B3062EB677-L000044](../../tests/test_answer_quality_runner.py#L44) | 44 | `""` | — |
| [SRC-B3062EB677-L000045](../../tests/test_answer_quality_runner.py#L45) | 45 | `"def test_validate_detects_bad_case_count(tmp_path):"` | — |
| [SRC-B3062EB677-L000046](../../tests/test_answer_quality_runner.py#L46) | 46 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000047](../../tests/test_answer_quality_runner.py#L47) | 47 | `"    data = json.loads(CORPUS.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-B3062EB677-L000048](../../tests/test_answer_quality_runner.py#L48) | 48 | `"    data[\"case_count\"] = 999"` | — |
| [SRC-B3062EB677-L000049](../../tests/test_answer_quality_runner.py#L49) | 49 | `"    bad = tmp_path / \"bad.json\""` | — |
| [SRC-B3062EB677-L000050](../../tests/test_answer_quality_runner.py#L50) | 50 | `"    bad.write_text(json.dumps(data), encoding=\"utf-8\")"` | — |
| [SRC-B3062EB677-L000051](../../tests/test_answer_quality_runner.py#L51) | 51 | `"    problems = mod.validate_corpus(mod.load_corpus(bad))"` | — |
| [SRC-B3062EB677-L000052](../../tests/test_answer_quality_runner.py#L52) | 52 | `"    assert any(\"case_count\" in p for p in problems)"` | — |
| [SRC-B3062EB677-L000053](../../tests/test_answer_quality_runner.py#L53) | 53 | `""` | — |
| [SRC-B3062EB677-L000054](../../tests/test_answer_quality_runner.py#L54) | 54 | `""` | — |
| [SRC-B3062EB677-L000055](../../tests/test_answer_quality_runner.py#L55) | 55 | `"def test_validate_detects_missing_required_field(tmp_path):"` | — |
| [SRC-B3062EB677-L000056](../../tests/test_answer_quality_runner.py#L56) | 56 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000057](../../tests/test_answer_quality_runner.py#L57) | 57 | `"    data = json.loads(CORPUS.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-B3062EB677-L000058](../../tests/test_answer_quality_runner.py#L58) | 58 | `"    data[\"cases\"] = [dict(data[\"cases\"][0])]"` | — |
| [SRC-B3062EB677-L000059](../../tests/test_answer_quality_runner.py#L59) | 59 | `"    del data[\"cases\"][0][\"question\"]"` | — |
| [SRC-B3062EB677-L000060](../../tests/test_answer_quality_runner.py#L60) | 60 | `"    data[\"case_count\"] = 1"` | — |
| [SRC-B3062EB677-L000061](../../tests/test_answer_quality_runner.py#L61) | 61 | `"    bad = tmp_path / \"bad2.json\""` | — |
| [SRC-B3062EB677-L000062](../../tests/test_answer_quality_runner.py#L62) | 62 | `"    bad.write_text(json.dumps(data), encoding=\"utf-8\")"` | — |
| [SRC-B3062EB677-L000063](../../tests/test_answer_quality_runner.py#L63) | 63 | `"    problems = mod.validate_corpus(mod.load_corpus(bad))"` | — |
| [SRC-B3062EB677-L000064](../../tests/test_answer_quality_runner.py#L64) | 64 | `"    assert problems"` | — |
| [SRC-B3062EB677-L000065](../../tests/test_answer_quality_runner.py#L65) | 65 | `""` | — |
| [SRC-B3062EB677-L000066](../../tests/test_answer_quality_runner.py#L66) | 66 | `""` | — |
| [SRC-B3062EB677-L000067](../../tests/test_answer_quality_runner.py#L67) | 67 | `"def test_live_refuses_unbounded_without_limit_or_case_id(capsys):"` | — |
| [SRC-B3062EB677-L000068](../../tests/test_answer_quality_runner.py#L68) | 68 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000069](../../tests/test_answer_quality_runner.py#L69) | 69 | `"    rc = mod.main([\"--mode\", \"live\", \"--corpus\", str(CORPUS)])"` | — |
| [SRC-B3062EB677-L000070](../../tests/test_answer_quality_runner.py#L70) | 70 | `"    assert rc == 2"` | — |
| [SRC-B3062EB677-L000071](../../tests/test_answer_quality_runner.py#L71) | 71 | `"    err = capsys.readouterr().err"` | — |
| [SRC-B3062EB677-L000072](../../tests/test_answer_quality_runner.py#L72) | 72 | `"    assert \"Refusing unbounded\" in err"` | — |
| [SRC-B3062EB677-L000073](../../tests/test_answer_quality_runner.py#L73) | 73 | `""` | — |
| [SRC-B3062EB677-L000074](../../tests/test_answer_quality_runner.py#L74) | 74 | `""` | — |
| [SRC-B3062EB677-L000075](../../tests/test_answer_quality_runner.py#L75) | 75 | `"def test_live_unknown_case_id(capsys):"` | — |
| [SRC-B3062EB677-L000076](../../tests/test_answer_quality_runner.py#L76) | 76 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000077](../../tests/test_answer_quality_runner.py#L77) | 77 | `"    rc = mod.main("` | — |
| [SRC-B3062EB677-L000078](../../tests/test_answer_quality_runner.py#L78) | 78 | `"        ["` | — |
| [SRC-B3062EB677-L000079](../../tests/test_answer_quality_runner.py#L79) | 79 | `"            \"--mode\","` | — |
| [SRC-B3062EB677-L000080](../../tests/test_answer_quality_runner.py#L80) | 80 | `"            \"live\","` | — |
| [SRC-B3062EB677-L000081](../../tests/test_answer_quality_runner.py#L81) | 81 | `"            \"--corpus\","` | — |
| [SRC-B3062EB677-L000082](../../tests/test_answer_quality_runner.py#L82) | 82 | `"            str(CORPUS),"` | — |
| [SRC-B3062EB677-L000083](../../tests/test_answer_quality_runner.py#L83) | 83 | `"            \"--case-id\","` | — |
| [SRC-B3062EB677-L000084](../../tests/test_answer_quality_runner.py#L84) | 84 | `"            \"AQ-999\","` | — |
| [SRC-B3062EB677-L000085](../../tests/test_answer_quality_runner.py#L85) | 85 | `"            \"--base-url\","` | — |
| [SRC-B3062EB677-L000086](../../tests/test_answer_quality_runner.py#L86) | 86 | `"            \"http://127.0.0.1:9\","` | — |
| [SRC-B3062EB677-L000087](../../tests/test_answer_quality_runner.py#L87) | 87 | `"        ]"` | — |
| [SRC-B3062EB677-L000088](../../tests/test_answer_quality_runner.py#L88) | 88 | `"    )"` | — |
| [SRC-B3062EB677-L000089](../../tests/test_answer_quality_runner.py#L89) | 89 | `"    assert rc == 2"` | — |
| [SRC-B3062EB677-L000090](../../tests/test_answer_quality_runner.py#L90) | 90 | `""` | — |
| [SRC-B3062EB677-L000091](../../tests/test_answer_quality_runner.py#L91) | 91 | `""` | — |
| [SRC-B3062EB677-L000092](../../tests/test_answer_quality_runner.py#L92) | 92 | `"def test_redact_secrets_strips_token_value(monkeypatch):"` | — |
| [SRC-B3062EB677-L000093](../../tests/test_answer_quality_runner.py#L93) | 93 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000094](../../tests/test_answer_quality_runner.py#L94) | 94 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", \"super-secret-token-value-xyz\")"` | — |
| [SRC-B3062EB677-L000095](../../tests/test_answer_quality_runner.py#L95) | 95 | `"    text = \"token=super-secret-token-value-xyz and OPENROUTER_API_KEY\""` | — |
| [SRC-B3062EB677-L000096](../../tests/test_answer_quality_runner.py#L96) | 96 | `"    out = mod.redact_secrets(text)"` | — |
| [SRC-B3062EB677-L000097](../../tests/test_answer_quality_runner.py#L97) | 97 | `"    assert \"super-secret-token-value-xyz\" not in out"` | — |
| [SRC-B3062EB677-L000098](../../tests/test_answer_quality_runner.py#L98) | 98 | `"    assert \"REDACTED\" in out"` | — |
| [SRC-B3062EB677-L000099](../../tests/test_answer_quality_runner.py#L99) | 99 | `""` | — |
| [SRC-B3062EB677-L000100](../../tests/test_answer_quality_runner.py#L100) | 100 | `""` | — |
| [SRC-B3062EB677-L000101](../../tests/test_answer_quality_runner.py#L101) | 101 | `"def test_live_records_not_tested_not_pass(monkeypatch, tmp_path, capsys):"` | — |
| [SRC-B3062EB677-L000102](../../tests/test_answer_quality_runner.py#L102) | 102 | `"    \"\"\"Even on HTTP 200, quality status stays NOT_TESTED (no keyword auto-PASS).\"\"\""` | — |
| [SRC-B3062EB677-L000103](../../tests/test_answer_quality_runner.py#L103) | 103 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000104](../../tests/test_answer_quality_runner.py#L104) | 104 | `""` | — |
| [SRC-B3062EB677-L000105](../../tests/test_answer_quality_runner.py#L105) | 105 | `"    def fake_post(base_url, question, timeout, token):"` | — |
| [SRC-B3062EB677-L000106](../../tests/test_answer_quality_runner.py#L106) | 106 | `"        return 200, {"` | — |
| [SRC-B3062EB677-L000107](../../tests/test_answer_quality_runner.py#L107) | 107 | `"            \"answer\": \"hello used_web_search should not force PASS\","` | — |
| [SRC-B3062EB677-L000108](../../tests/test_answer_quality_runner.py#L108) | 108 | `"            \"used_web_search\": False,"` | — |
| [SRC-B3062EB677-L000109](../../tests/test_answer_quality_runner.py#L109) | 109 | `"            \"used_language_model\": True,"` | — |
| [SRC-B3062EB677-L000110](../../tests/test_answer_quality_runner.py#L110) | 110 | `"            \"sources\": [],"` | — |
| [SRC-B3062EB677-L000111](../../tests/test_answer_quality_runner.py#L111) | 111 | `"        }"` | — |
| [SRC-B3062EB677-L000112](../../tests/test_answer_quality_runner.py#L112) | 112 | `""` | — |
| [SRC-B3062EB677-L000113](../../tests/test_answer_quality_runner.py#L113) | 113 | `"    monkeypatch.setattr(mod, \"post_agent\", fake_post)"` | — |
| [SRC-B3062EB677-L000114](../../tests/test_answer_quality_runner.py#L114) | 114 | `"    out = tmp_path / \"results.json\""` | — |
| [SRC-B3062EB677-L000115](../../tests/test_answer_quality_runner.py#L115) | 115 | `"    rc = mod.main("` | — |
| [SRC-B3062EB677-L000116](../../tests/test_answer_quality_runner.py#L116) | 116 | `"        ["` | — |
| [SRC-B3062EB677-L000117](../../tests/test_answer_quality_runner.py#L117) | 117 | `"            \"--mode\","` | — |
| [SRC-B3062EB677-L000118](../../tests/test_answer_quality_runner.py#L118) | 118 | `"            \"live\","` | — |
| [SRC-B3062EB677-L000119](../../tests/test_answer_quality_runner.py#L119) | 119 | `"            \"--corpus\","` | — |
| [SRC-B3062EB677-L000120](../../tests/test_answer_quality_runner.py#L120) | 120 | `"            str(CORPUS),"` | — |
| [SRC-B3062EB677-L000121](../../tests/test_answer_quality_runner.py#L121) | 121 | `"            \"--case-id\","` | — |
| [SRC-B3062EB677-L000122](../../tests/test_answer_quality_runner.py#L122) | 122 | `"            \"AQ-001\","` | — |
| [SRC-B3062EB677-L000123](../../tests/test_answer_quality_runner.py#L123) | 123 | `"            \"--limit\","` | — |
| [SRC-B3062EB677-L000124](../../tests/test_answer_quality_runner.py#L124) | 124 | `"            \"1\","` | — |
| [SRC-B3062EB677-L000125](../../tests/test_answer_quality_runner.py#L125) | 125 | `"            \"--out\","` | — |
| [SRC-B3062EB677-L000126](../../tests/test_answer_quality_runner.py#L126) | 126 | `"            str(out),"` | — |
| [SRC-B3062EB677-L000127](../../tests/test_answer_quality_runner.py#L127) | 127 | `"        ]"` | — |
| [SRC-B3062EB677-L000128](../../tests/test_answer_quality_runner.py#L128) | 128 | `"    )"` | — |
| [SRC-B3062EB677-L000129](../../tests/test_answer_quality_runner.py#L129) | 129 | `"    assert rc == 0"` | — |
| [SRC-B3062EB677-L000130](../../tests/test_answer_quality_runner.py#L130) | 130 | `"    payload = json.loads(out.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-B3062EB677-L000131](../../tests/test_answer_quality_runner.py#L131) | 131 | `"    assert payload[\"results\"][0][\"status\"] == \"NOT_TESTED\""` | — |
| [SRC-B3062EB677-L000132](../../tests/test_answer_quality_runner.py#L132) | 132 | `"    assert payload[\"results\"][0][\"evidence_fixture_injected\"] is False"` | — |
| [SRC-B3062EB677-L000133](../../tests/test_answer_quality_runner.py#L133) | 133 | `"    assert payload[\"results\"][0][\"transport_ok\"] is True"` | — |
| [SRC-B3062EB677-L000134](../../tests/test_answer_quality_runner.py#L134) | 134 | `""` | — |
| [SRC-B3062EB677-L000135](../../tests/test_answer_quality_runner.py#L135) | 135 | `""` | — |
| [SRC-B3062EB677-L000136](../../tests/test_answer_quality_runner.py#L136) | 136 | `"def test_validate_base_url_rejects_non_loopback_http():"` | — |
| [SRC-B3062EB677-L000137](../../tests/test_answer_quality_runner.py#L137) | 137 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000138](../../tests/test_answer_quality_runner.py#L138) | 138 | `"    with pytest.raises(ValueError, match=\"Plain HTTP\"):"` | — |
| [SRC-B3062EB677-L000139](../../tests/test_answer_quality_runner.py#L139) | 139 | `"        mod.validate_base_url(\"http://research.example\")"` | — |
| [SRC-B3062EB677-L000140](../../tests/test_answer_quality_runner.py#L140) | 140 | `""` | — |
| [SRC-B3062EB677-L000141](../../tests/test_answer_quality_runner.py#L141) | 141 | `""` | — |
| [SRC-B3062EB677-L000142](../../tests/test_answer_quality_runner.py#L142) | 142 | `"@pytest.mark.parametrize("` | — |
| [SRC-B3062EB677-L000143](../../tests/test_answer_quality_runner.py#L143) | 143 | `"    \"url\","` | — |
| [SRC-B3062EB677-L000144](../../tests/test_answer_quality_runner.py#L144) | 144 | `"    ["` | — |
| [SRC-B3062EB677-L000145](../../tests/test_answer_quality_runner.py#L145) | 145 | `"        \"https://user:password@example.com\","` | — |
| [SRC-B3062EB677-L000146](../../tests/test_answer_quality_runner.py#L146) | 146 | `"        \"https://example.com/private/path\","` | — |
| [SRC-B3062EB677-L000147](../../tests/test_answer_quality_runner.py#L147) | 147 | `"        \"https://example.com/?token=oops\","` | — |
| [SRC-B3062EB677-L000148](../../tests/test_answer_quality_runner.py#L148) | 148 | `"        \"https://example.com/#fragment\","` | — |
| [SRC-B3062EB677-L000149](../../tests/test_answer_quality_runner.py#L149) | 149 | `"    ],"` | — |
| [SRC-B3062EB677-L000150](../../tests/test_answer_quality_runner.py#L150) | 150 | `")"` | — |
| [SRC-B3062EB677-L000151](../../tests/test_answer_quality_runner.py#L151) | 151 | `"def test_validate_base_url_rejects_ambiguous_or_credential_bearing_urls(url):"` | — |
| [SRC-B3062EB677-L000152](../../tests/test_answer_quality_runner.py#L152) | 152 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000153](../../tests/test_answer_quality_runner.py#L153) | 153 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-B3062EB677-L000154](../../tests/test_answer_quality_runner.py#L154) | 154 | `"        mod.validate_base_url(url)"` | — |
| [SRC-B3062EB677-L000155](../../tests/test_answer_quality_runner.py#L155) | 155 | `""` | — |
| [SRC-B3062EB677-L000156](../../tests/test_answer_quality_runner.py#L156) | 156 | `""` | — |
| [SRC-B3062EB677-L000157](../../tests/test_answer_quality_runner.py#L157) | 157 | `"def test_remote_bearer_token_requires_exact_allowlisted_https_origin(monkeypatch):"` | — |
| [SRC-B3062EB677-L000158](../../tests/test_answer_quality_runner.py#L158) | 158 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000159](../../tests/test_answer_quality_runner.py#L159) | 159 | `"    monkeypatch.delenv(\"OMARAI_BENCHMARK_ALLOWED_ORIGIN\", raising=False)"` | — |
| [SRC-B3062EB677-L000160](../../tests/test_answer_quality_runner.py#L160) | 160 | `"    with pytest.raises(ValueError, match=\"OMARAI_BENCHMARK_ALLOWED_ORIGIN\"):"` | — |
| [SRC-B3062EB677-L000161](../../tests/test_answer_quality_runner.py#L161) | 161 | `"        mod.validate_base_url(\"https://app.example\", token_present=True)"` | — |
| [SRC-B3062EB677-L000162](../../tests/test_answer_quality_runner.py#L162) | 162 | `""` | — |
| [SRC-B3062EB677-L000163](../../tests/test_answer_quality_runner.py#L163) | 163 | `"    monkeypatch.setenv(\"OMARAI_BENCHMARK_ALLOWED_ORIGIN\", \"https://app.example\")"` | — |
| [SRC-B3062EB677-L000164](../../tests/test_answer_quality_runner.py#L164) | 164 | `"    assert mod.validate_base_url(\"https://app.example/\", token_present=True) == \"https://app.example\""` | — |
| [SRC-B3062EB677-L000165](../../tests/test_answer_quality_runner.py#L165) | 165 | `"    with pytest.raises(ValueError, match=\"does not match\"):"` | — |
| [SRC-B3062EB677-L000166](../../tests/test_answer_quality_runner.py#L166) | 166 | `"        mod.validate_base_url(\"https://other.example\", token_present=True)"` | — |
| [SRC-B3062EB677-L000167](../../tests/test_answer_quality_runner.py#L167) | 167 | `""` | — |
| [SRC-B3062EB677-L000168](../../tests/test_answer_quality_runner.py#L168) | 168 | `""` | — |
| [SRC-B3062EB677-L000169](../../tests/test_answer_quality_runner.py#L169) | 169 | `"def test_remote_token_origin_comparison_normalizes_default_https_port(monkeypatch):"` | — |
| [SRC-B3062EB677-L000170](../../tests/test_answer_quality_runner.py#L170) | 170 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000171](../../tests/test_answer_quality_runner.py#L171) | 171 | `"    monkeypatch.setenv(\"OMARAI_BENCHMARK_ALLOWED_ORIGIN\", \"https://app.example\")"` | — |
| [SRC-B3062EB677-L000172](../../tests/test_answer_quality_runner.py#L172) | 172 | `"    assert ("` | — |
| [SRC-B3062EB677-L000173](../../tests/test_answer_quality_runner.py#L173) | 173 | `"        mod.validate_base_url(\"https://app.example:443\", token_present=True)"` | — |
| [SRC-B3062EB677-L000174](../../tests/test_answer_quality_runner.py#L174) | 174 | `"        == \"https://app.example\""` | — |
| [SRC-B3062EB677-L000175](../../tests/test_answer_quality_runner.py#L175) | 175 | `"    )"` | — |
| [SRC-B3062EB677-L000176](../../tests/test_answer_quality_runner.py#L176) | 176 | `""` | — |
| [SRC-B3062EB677-L000177](../../tests/test_answer_quality_runner.py#L177) | 177 | `""` | — |
| [SRC-B3062EB677-L000178](../../tests/test_answer_quality_runner.py#L178) | 178 | `"def test_redirect_handler_refuses_following_redirects():"` | — |
| [SRC-B3062EB677-L000179](../../tests/test_answer_quality_runner.py#L179) | 179 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000180](../../tests/test_answer_quality_runner.py#L180) | 180 | `"    handler = mod._NoRedirectHandler()"` | — |
| [SRC-B3062EB677-L000181](../../tests/test_answer_quality_runner.py#L181) | 181 | `"    assert handler.redirect_request("` | — |
| [SRC-B3062EB677-L000182](../../tests/test_answer_quality_runner.py#L182) | 182 | `"        req=None,"` | — |
| [SRC-B3062EB677-L000183](../../tests/test_answer_quality_runner.py#L183) | 183 | `"        fp=None,"` | — |
| [SRC-B3062EB677-L000184](../../tests/test_answer_quality_runner.py#L184) | 184 | `"        code=302,"` | — |
| [SRC-B3062EB677-L000185](../../tests/test_answer_quality_runner.py#L185) | 185 | `"        msg=\"Found\","` | — |
| [SRC-B3062EB677-L000186](../../tests/test_answer_quality_runner.py#L186) | 186 | `"        headers={},"` | — |
| [SRC-B3062EB677-L000187](../../tests/test_answer_quality_runner.py#L187) | 187 | `"        newurl=\"https://attacker.example/collect\","` | — |
| [SRC-B3062EB677-L000188](../../tests/test_answer_quality_runner.py#L188) | 188 | `"    ) is None"` | — |
| [SRC-B3062EB677-L000189](../../tests/test_answer_quality_runner.py#L189) | 189 | `""` | — |
| [SRC-B3062EB677-L000190](../../tests/test_answer_quality_runner.py#L190) | 190 | `""` | — |
| [SRC-B3062EB677-L000191](../../tests/test_answer_quality_runner.py#L191) | 191 | `"def test_live_rejects_unapproved_remote_url_before_network(monkeypatch, capsys):"` | — |
| [SRC-B3062EB677-L000192](../../tests/test_answer_quality_runner.py#L192) | 192 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000193](../../tests/test_answer_quality_runner.py#L193) | 193 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", \"a-test-token\")"` | — |
| [SRC-B3062EB677-L000194](../../tests/test_answer_quality_runner.py#L194) | 194 | `"    monkeypatch.delenv(\"OMARAI_BENCHMARK_ALLOWED_ORIGIN\", raising=False)"` | — |
| [SRC-B3062EB677-L000195](../../tests/test_answer_quality_runner.py#L195) | 195 | `"    rc = mod.run_live("` | — |
