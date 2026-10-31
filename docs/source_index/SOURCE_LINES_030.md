# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **030**
- سجلات الأسطر: **800**
- النطاق: SRC-70795F4B61-L000021 إلى SRC-A8360B1B03-L000289
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## ملفات أخرى

### FILE-70795F4B61 — [scripts/compare_answer_quality_runs.py](../../scripts/compare_answer_quality_runs.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-70795F4B61-L000021](../../scripts/compare_answer_quality_runs.py#L21) | 21 | `""` | — |
| [SRC-70795F4B61-L000022](../../scripts/compare_answer_quality_runs.py#L22) | 22 | `""` | — |
| [SRC-70795F4B61-L000023](../../scripts/compare_answer_quality_runs.py#L23) | 23 | `"def load_json_object(path: Path) -> dict[str, Any]:"` | — |
| [SRC-70795F4B61-L000024](../../scripts/compare_answer_quality_runs.py#L24) | 24 | `"    if not path.is_file():"` | — |
| [SRC-70795F4B61-L000025](../../scripts/compare_answer_quality_runs.py#L25) | 25 | `"        raise FileNotFoundError(\"Input file not found: \" + str(path))"` | — |
| [SRC-70795F4B61-L000026](../../scripts/compare_answer_quality_runs.py#L26) | 26 | `"    data = json.loads(path.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-70795F4B61-L000027](../../scripts/compare_answer_quality_runs.py#L27) | 27 | `"    if not isinstance(data, dict):"` | — |
| [SRC-70795F4B61-L000028](../../scripts/compare_answer_quality_runs.py#L28) | 28 | `"        raise TypeError(\"JSON root must be an object: \" + str(path))"` | — |
| [SRC-70795F4B61-L000029](../../scripts/compare_answer_quality_runs.py#L29) | 29 | `"    return data"` | — |
| [SRC-70795F4B61-L000030](../../scripts/compare_answer_quality_runs.py#L30) | 30 | `""` | — |
| [SRC-70795F4B61-L000031](../../scripts/compare_answer_quality_runs.py#L31) | 31 | `""` | — |
| [SRC-70795F4B61-L000032](../../scripts/compare_answer_quality_runs.py#L32) | 32 | `"def _finite_nonnegative(value: Any) -> float \| None:"` | — |
| [SRC-70795F4B61-L000033](../../scripts/compare_answer_quality_runs.py#L33) | 33 | `"    if isinstance(value, bool) or not isinstance(value, (int, float)):"` | — |
| [SRC-70795F4B61-L000034](../../scripts/compare_answer_quality_runs.py#L34) | 34 | `"        return None"` | — |
| [SRC-70795F4B61-L000035](../../scripts/compare_answer_quality_runs.py#L35) | 35 | `"    number = float(value)"` | — |
| [SRC-70795F4B61-L000036](../../scripts/compare_answer_quality_runs.py#L36) | 36 | `"    if not math.isfinite(number) or number < 0:"` | — |
| [SRC-70795F4B61-L000037](../../scripts/compare_answer_quality_runs.py#L37) | 37 | `"        return None"` | — |
| [SRC-70795F4B61-L000038](../../scripts/compare_answer_quality_runs.py#L38) | 38 | `"    return number"` | — |
| [SRC-70795F4B61-L000039](../../scripts/compare_answer_quality_runs.py#L39) | 39 | `""` | — |
| [SRC-70795F4B61-L000040](../../scripts/compare_answer_quality_runs.py#L40) | 40 | `""` | — |
| [SRC-70795F4B61-L000041](../../scripts/compare_answer_quality_runs.py#L41) | 41 | `"def validate_run(run: dict[str, Any], label: str) -> list[str]:"` | — |
| [SRC-70795F4B61-L000042](../../scripts/compare_answer_quality_runs.py#L42) | 42 | `"    problems: list[str] = []"` | — |
| [SRC-70795F4B61-L000043](../../scripts/compare_answer_quality_runs.py#L43) | 43 | `"    missing = REQUIRED_RUN_FIELDS - set(run)"` | — |
| [SRC-70795F4B61-L000044](../../scripts/compare_answer_quality_runs.py#L44) | 44 | `"    if missing:"` | — |
| [SRC-70795F4B61-L000045](../../scripts/compare_answer_quality_runs.py#L45) | 45 | `"        problems.append(f\"{label}: missing run fields {sorted(missing)}\")"` | — |
| [SRC-70795F4B61-L000046](../../scripts/compare_answer_quality_runs.py#L46) | 46 | `"    results = run.get(\"results\")"` | — |
| [SRC-70795F4B61-L000047](../../scripts/compare_answer_quality_runs.py#L47) | 47 | `"    if not isinstance(results, list) or not results:"` | — |
| [SRC-70795F4B61-L000048](../../scripts/compare_answer_quality_runs.py#L48) | 48 | `"        problems.append(f\"{label}: results must be a non-empty array\")"` | — |
| [SRC-70795F4B61-L000049](../../scripts/compare_answer_quality_runs.py#L49) | 49 | `"        return problems"` | — |
| [SRC-70795F4B61-L000050](../../scripts/compare_answer_quality_runs.py#L50) | 50 | `"    seen: set[str] = set()"` | — |
| [SRC-70795F4B61-L000051](../../scripts/compare_answer_quality_runs.py#L51) | 51 | `"    for index, record in enumerate(results):"` | — |
| [SRC-70795F4B61-L000052](../../scripts/compare_answer_quality_runs.py#L52) | 52 | `"        if not isinstance(record, dict):"` | — |
| [SRC-70795F4B61-L000053](../../scripts/compare_answer_quality_runs.py#L53) | 53 | `"            problems.append(f\"{label}: results[{index}] must be an object\")"` | — |
| [SRC-70795F4B61-L000054](../../scripts/compare_answer_quality_runs.py#L54) | 54 | `"            continue"` | — |
| [SRC-70795F4B61-L000055](../../scripts/compare_answer_quality_runs.py#L55) | 55 | `"        case_id = record.get(\"case_id\")"` | — |
| [SRC-70795F4B61-L000056](../../scripts/compare_answer_quality_runs.py#L56) | 56 | `"        if not isinstance(case_id, str) or not case_id.strip():"` | — |
| [SRC-70795F4B61-L000057](../../scripts/compare_answer_quality_runs.py#L57) | 57 | `"            problems.append(f\"{label}: results[{index}] has no case_id\")"` | — |
| [SRC-70795F4B61-L000058](../../scripts/compare_answer_quality_runs.py#L58) | 58 | `"            continue"` | — |
| [SRC-70795F4B61-L000059](../../scripts/compare_answer_quality_runs.py#L59) | 59 | `"        prompt = record.get(\"prompt\")"` | — |
| [SRC-70795F4B61-L000060](../../scripts/compare_answer_quality_runs.py#L60) | 60 | `"        if not isinstance(prompt, str) or not prompt.strip():"` | — |
| [SRC-70795F4B61-L000061](../../scripts/compare_answer_quality_runs.py#L61) | 61 | `"            problems.append(f\"{label}/{case_id}: prompt must be a non-empty string\")"` | — |
| [SRC-70795F4B61-L000062](../../scripts/compare_answer_quality_runs.py#L62) | 62 | `"        if case_id in seen:"` | — |
| [SRC-70795F4B61-L000063](../../scripts/compare_answer_quality_runs.py#L63) | 63 | `"            problems.append(f\"{label}: duplicate case_id {case_id}\")"` | — |
| [SRC-70795F4B61-L000064](../../scripts/compare_answer_quality_runs.py#L64) | 64 | `"        seen.add(case_id)"` | — |
| [SRC-70795F4B61-L000065](../../scripts/compare_answer_quality_runs.py#L65) | 65 | `"        if \"elapsed_ms\" in record and _finite_nonnegative(record[\"elapsed_ms\"]) is None:"` | — |
| [SRC-70795F4B61-L000066](../../scripts/compare_answer_quality_runs.py#L66) | 66 | `"            problems.append(f\"{label}/{case_id}: elapsed_ms must be finite and non-negative\")"` | — |
| [SRC-70795F4B61-L000067](../../scripts/compare_answer_quality_runs.py#L67) | 67 | `"    return problems"` | — |
| [SRC-70795F4B61-L000068](../../scripts/compare_answer_quality_runs.py#L68) | 68 | `""` | — |
| [SRC-70795F4B61-L000069](../../scripts/compare_answer_quality_runs.py#L69) | 69 | `""` | — |
| [SRC-70795F4B61-L000070](../../scripts/compare_answer_quality_runs.py#L70) | 70 | `"def _percentile_nearest_rank(values: list[float], percentile: float) -> float \| None:"` | — |
| [SRC-70795F4B61-L000071](../../scripts/compare_answer_quality_runs.py#L71) | 71 | `"    if not values:"` | — |
| [SRC-70795F4B61-L000072](../../scripts/compare_answer_quality_runs.py#L72) | 72 | `"        return None"` | — |
| [SRC-70795F4B61-L000073](../../scripts/compare_answer_quality_runs.py#L73) | 73 | `"    ordered = sorted(values)"` | — |
| [SRC-70795F4B61-L000074](../../scripts/compare_answer_quality_runs.py#L74) | 74 | `"    index = max(0, math.ceil(percentile * len(ordered)) - 1)"` | — |
| [SRC-70795F4B61-L000075](../../scripts/compare_answer_quality_runs.py#L75) | 75 | `"    return round(ordered[index], 2)"` | — |
| [SRC-70795F4B61-L000076](../../scripts/compare_answer_quality_runs.py#L76) | 76 | `""` | — |
| [SRC-70795F4B61-L000077](../../scripts/compare_answer_quality_runs.py#L77) | 77 | `""` | — |
| [SRC-70795F4B61-L000078](../../scripts/compare_answer_quality_runs.py#L78) | 78 | `"def _rate(numerator: int, denominator: int) -> dict[str, Any]:"` | — |
| [SRC-70795F4B61-L000079](../../scripts/compare_answer_quality_runs.py#L79) | 79 | `"    return {"` | — |
| [SRC-70795F4B61-L000080](../../scripts/compare_answer_quality_runs.py#L80) | 80 | `"        \"score\": round(numerator / denominator, 4) if denominator else None,"` | — |
| [SRC-70795F4B61-L000081](../../scripts/compare_answer_quality_runs.py#L81) | 81 | `"        \"numerator\": numerator,"` | — |
| [SRC-70795F4B61-L000082](../../scripts/compare_answer_quality_runs.py#L82) | 82 | `"        \"denominator\": denominator,"` | — |
| [SRC-70795F4B61-L000083](../../scripts/compare_answer_quality_runs.py#L83) | 83 | `"        \"status\": \"SCORED\" if denominator else \"NOT_SCORABLE_NO_DENOMINATOR\","` | — |
| [SRC-70795F4B61-L000084](../../scripts/compare_answer_quality_runs.py#L84) | 84 | `"    }"` | — |
| [SRC-70795F4B61-L000085](../../scripts/compare_answer_quality_runs.py#L85) | 85 | `""` | — |
| [SRC-70795F4B61-L000086](../../scripts/compare_answer_quality_runs.py#L86) | 86 | `""` | — |
| [SRC-70795F4B61-L000087](../../scripts/compare_answer_quality_runs.py#L87) | 87 | `"def run_metrics(run: dict[str, Any]) -> dict[str, Any]:"` | — |
| [SRC-70795F4B61-L000088](../../scripts/compare_answer_quality_runs.py#L88) | 88 | `"    results = run[\"results\"]"` | — |
| [SRC-70795F4B61-L000089](../../scripts/compare_answer_quality_runs.py#L89) | 89 | `"    transport_ok = [r for r in results if r.get(\"transport_ok\") is True]"` | — |
| [SRC-70795F4B61-L000090](../../scripts/compare_answer_quality_runs.py#L90) | 90 | `"    elapsed = ["` | — |
| [SRC-70795F4B61-L000091](../../scripts/compare_answer_quality_runs.py#L91) | 91 | `"        float(value)"` | — |
| [SRC-70795F4B61-L000092](../../scripts/compare_answer_quality_runs.py#L92) | 92 | `"        for record in results"` | — |
| [SRC-70795F4B61-L000093](../../scripts/compare_answer_quality_runs.py#L93) | 93 | `"        if (value := _finite_nonnegative(record.get(\"elapsed_ms\"))) is not None"` | — |
| [SRC-70795F4B61-L000094](../../scripts/compare_answer_quality_runs.py#L94) | 94 | `"    ]"` | — |
| [SRC-70795F4B61-L000095](../../scripts/compare_answer_quality_runs.py#L95) | 95 | `"    search_cases = [r for r in results if r.get(\"expected_strategy\") == \"web_search\"]"` | — |
| [SRC-70795F4B61-L000096](../../scripts/compare_answer_quality_runs.py#L96) | 96 | `"    search_attempted = ["` | — |
| [SRC-70795F4B61-L000097](../../scripts/compare_answer_quality_runs.py#L97) | 97 | `"        r for r in search_cases"` | — |
| [SRC-70795F4B61-L000098](../../scripts/compare_answer_quality_runs.py#L98) | 98 | `"        if r.get(\"search_outcome\") not in (None, \"\", \"unknown\", \"not_attempted\")"` | — |
| [SRC-70795F4B61-L000099](../../scripts/compare_answer_quality_runs.py#L99) | 99 | `"    ]"` | — |
| [SRC-70795F4B61-L000100](../../scripts/compare_answer_quality_runs.py#L100) | 100 | `"    usable = [r for r in search_cases if r.get(\"tool_status\") == \"SUCCESS_WITH_USABLE_RESULTS\"]"` | — |
| [SRC-70795F4B61-L000101](../../scripts/compare_answer_quality_runs.py#L101) | 101 | `"    tool_failed = [r for r in search_cases if r.get(\"tool_status\") == \"TOOL_FAILED\"]"` | — |
| [SRC-70795F4B61-L000102](../../scripts/compare_answer_quality_runs.py#L102) | 102 | `"    no_usable = [r for r in search_cases if r.get(\"tool_status\") == \"ATTEMPTED_NO_USABLE_RESULTS\"]"` | — |
| [SRC-70795F4B61-L000103](../../scripts/compare_answer_quality_runs.py#L103) | 103 | `"    costs = ["` | — |
| [SRC-70795F4B61-L000104](../../scripts/compare_answer_quality_runs.py#L104) | 104 | `"        float(value)"` | — |
| [SRC-70795F4B61-L000105](../../scripts/compare_answer_quality_runs.py#L105) | 105 | `"        for record in results"` | — |
| [SRC-70795F4B61-L000106](../../scripts/compare_answer_quality_runs.py#L106) | 106 | `"        if (value := _finite_nonnegative(record.get(\"provider_reported_model_cost_usd\"))) is not None"` | — |
| [SRC-70795F4B61-L000107](../../scripts/compare_answer_quality_runs.py#L107) | 107 | `"    ]"` | — |
| [SRC-70795F4B61-L000108](../../scripts/compare_answer_quality_runs.py#L108) | 108 | `"    required_tool_rows = ["` | — |
| [SRC-70795F4B61-L000109](../../scripts/compare_answer_quality_runs.py#L109) | 109 | `"        row"` | — |
| [SRC-70795F4B61-L000110](../../scripts/compare_answer_quality_runs.py#L110) | 110 | `"        for record in results"` | — |
| [SRC-70795F4B61-L000111](../../scripts/compare_answer_quality_runs.py#L111) | 111 | `"        for row in record.get(\"required_tool_statuses\", [])"` | — |
| [SRC-70795F4B61-L000112](../../scripts/compare_answer_quality_runs.py#L112) | 112 | `"        if isinstance(row, dict) and isinstance(row.get(\"successful_completion\"), bool)"` | — |
| [SRC-70795F4B61-L000113](../../scripts/compare_answer_quality_runs.py#L113) | 113 | `"    ]"` | — |
| [SRC-70795F4B61-L000114](../../scripts/compare_answer_quality_runs.py#L114) | 114 | `"    required_tool_successes = sum("` | — |
| [SRC-70795F4B61-L000115](../../scripts/compare_answer_quality_runs.py#L115) | 115 | `"        1 for row in required_tool_rows if row[\"successful_completion\"] is True"` | — |
| [SRC-70795F4B61-L000116](../../scripts/compare_answer_quality_runs.py#L116) | 116 | `"    )"` | — |
| [SRC-70795F4B61-L000117](../../scripts/compare_answer_quality_runs.py#L117) | 117 | `"    tool_status_counts: dict[str, int] = {}"` | — |
| [SRC-70795F4B61-L000118](../../scripts/compare_answer_quality_runs.py#L118) | 118 | `"    for row in required_tool_rows:"` | — |
| [SRC-70795F4B61-L000119](../../scripts/compare_answer_quality_runs.py#L119) | 119 | `"        status = row.get(\"status\")"` | — |
| [SRC-70795F4B61-L000120](../../scripts/compare_answer_quality_runs.py#L120) | 120 | `"        if isinstance(status, str):"` | — |
| [SRC-70795F4B61-L000121](../../scripts/compare_answer_quality_runs.py#L121) | 121 | `"            tool_status_counts[status] = tool_status_counts.get(status, 0) + 1"` | — |
| [SRC-70795F4B61-L000122](../../scripts/compare_answer_quality_runs.py#L122) | 122 | `"    required_tool_matrix_telemetry_known = all("` | — |
| [SRC-70795F4B61-L000123](../../scripts/compare_answer_quality_runs.py#L123) | 123 | `"        isinstance(record.get(\"required_tool_matrix_complete\"), bool)"` | — |
| [SRC-70795F4B61-L000124](../../scripts/compare_answer_quality_runs.py#L124) | 124 | `"        for record in results"` | — |
| [SRC-70795F4B61-L000125](../../scripts/compare_answer_quality_runs.py#L125) | 125 | `"    )"` | — |
| [SRC-70795F4B61-L000126](../../scripts/compare_answer_quality_runs.py#L126) | 126 | `"    required_tool_matrix_complete_count = sum("` | — |
| [SRC-70795F4B61-L000127](../../scripts/compare_answer_quality_runs.py#L127) | 127 | `"        1 for record in results if record.get(\"required_tool_matrix_complete\") is True"` | — |
| [SRC-70795F4B61-L000128](../../scripts/compare_answer_quality_runs.py#L128) | 128 | `"    )"` | — |
| [SRC-70795F4B61-L000129](../../scripts/compare_answer_quality_runs.py#L129) | 129 | `"    required_tool_matrix_incomplete_case_ids = ["` | — |
| [SRC-70795F4B61-L000130](../../scripts/compare_answer_quality_runs.py#L130) | 130 | `"        record.get(\"case_id\", \"unknown\")"` | — |
| [SRC-70795F4B61-L000131](../../scripts/compare_answer_quality_runs.py#L131) | 131 | `"        for record in results"` | — |
| [SRC-70795F4B61-L000132](../../scripts/compare_answer_quality_runs.py#L132) | 132 | `"        if record.get(\"required_tool_matrix_complete\") is not True"` | — |
| [SRC-70795F4B61-L000133](../../scripts/compare_answer_quality_runs.py#L133) | 133 | `"    ]"` | — |
| [SRC-70795F4B61-L000134](../../scripts/compare_answer_quality_runs.py#L134) | 134 | `"    complete_cost_cases = sum("` | — |
| [SRC-70795F4B61-L000135](../../scripts/compare_answer_quality_runs.py#L135) | 135 | `"        1 for r in results"` | — |
| [SRC-70795F4B61-L000136](../../scripts/compare_answer_quality_runs.py#L136) | 136 | `"        if r.get(\"provider_reported_model_cost_status\") == \"COMPLETE_FOR_RETURNED_MODEL_CALLS\""` | — |
| [SRC-70795F4B61-L000137](../../scripts/compare_answer_quality_runs.py#L137) | 137 | `"    )"` | — |
| [SRC-70795F4B61-L000138](../../scripts/compare_answer_quality_runs.py#L138) | 138 | `"    reconciled_request_costs = ["` | — |
| [SRC-70795F4B61-L000139](../../scripts/compare_answer_quality_runs.py#L139) | 139 | `"        float(value)"` | — |
| [SRC-70795F4B61-L000140](../../scripts/compare_answer_quality_runs.py#L140) | 140 | `"        for record in results"` | — |
| [SRC-70795F4B61-L000141](../../scripts/compare_answer_quality_runs.py#L141) | 141 | `"        if record.get(\"request_cost_status\") == \"RECONCILED_COMPLETE_REQUEST_COST\""` | — |
| [SRC-70795F4B61-L000142](../../scripts/compare_answer_quality_runs.py#L142) | 142 | `"        and (value := _finite_nonnegative(record.get(\"request_cost_usd\"))) is not None"` | — |
| [SRC-70795F4B61-L000143](../../scripts/compare_answer_quality_runs.py#L143) | 143 | `"    ]"` | — |
| [SRC-70795F4B61-L000144](../../scripts/compare_answer_quality_runs.py#L144) | 144 | `"    complete_request_cost_count = len(reconciled_request_costs)"` | — |
| [SRC-70795F4B61-L000145](../../scripts/compare_answer_quality_runs.py#L145) | 145 | `"    request_cost_complete = complete_request_cost_count == len(results)"` | — |
| [SRC-70795F4B61-L000146](../../scripts/compare_answer_quality_runs.py#L146) | 146 | `"    return {"` | — |
| [SRC-70795F4B61-L000147](../../scripts/compare_answer_quality_runs.py#L147) | 147 | `"        \"case_count\": len(results),"` | — |
| [SRC-70795F4B61-L000148](../../scripts/compare_answer_quality_runs.py#L148) | 148 | `"        \"transport_success_rate\": _rate(len(transport_ok), len(results)),"` | — |
| [SRC-70795F4B61-L000149](../../scripts/compare_answer_quality_runs.py#L149) | 149 | `"        \"latency_ms\": {"` | — |
| [SRC-70795F4B61-L000150](../../scripts/compare_answer_quality_runs.py#L150) | 150 | `"            \"sample_count\": len(elapsed),"` | — |
| [SRC-70795F4B61-L000151](../../scripts/compare_answer_quality_runs.py#L151) | 151 | `"            \"mean\": round(sum(elapsed) / len(elapsed), 2) if elapsed else None,"` | — |
| [SRC-70795F4B61-L000152](../../scripts/compare_answer_quality_runs.py#L152) | 152 | `"            \"p50\": _percentile_nearest_rank(elapsed, 0.50),"` | — |
| [SRC-70795F4B61-L000153](../../scripts/compare_answer_quality_runs.py#L153) | 153 | `"            \"p95\": _percentile_nearest_rank(elapsed, 0.95),"` | — |
| [SRC-70795F4B61-L000154](../../scripts/compare_answer_quality_runs.py#L154) | 154 | `"            \"max\": round(max(elapsed), 2) if elapsed else None,"` | — |
| [SRC-70795F4B61-L000155](../../scripts/compare_answer_quality_runs.py#L155) | 155 | `"            \"status\": \"SCORED\" if elapsed else \"NOT_MEASURED\","` | — |
| [SRC-70795F4B61-L000156](../../scripts/compare_answer_quality_runs.py#L156) | 156 | `"            \"semantics\": \"Sequential end-to-end HTTP request time; not a concurrency/load test.\","` | — |
| [SRC-70795F4B61-L000157](../../scripts/compare_answer_quality_runs.py#L157) | 157 | `"        },"` | — |
| [SRC-70795F4B61-L000158](../../scripts/compare_answer_quality_runs.py#L158) | 158 | `"        \"tool_usage\": {"` | — |
| [SRC-70795F4B61-L000159](../../scripts/compare_answer_quality_runs.py#L159) | 159 | `"            \"web_search_case_count\": len(search_cases),"` | — |
| [SRC-70795F4B61-L000160](../../scripts/compare_answer_quality_runs.py#L160) | 160 | `"            \"search_attempt_rate\": _rate(len(search_attempted), len(search_cases)),"` | — |
| [SRC-70795F4B61-L000161](../../scripts/compare_answer_quality_runs.py#L161) | 161 | `"            \"usable_result_rate\": _rate(len(usable), len(search_cases)),"` | — |
| [SRC-70795F4B61-L000162](../../scripts/compare_answer_quality_runs.py#L162) | 162 | `"            \"tool_error_rate_among_search_cases\": _rate(len(tool_failed), len(search_cases)),"` | — |
| [SRC-70795F4B61-L000163](../../scripts/compare_answer_quality_runs.py#L163) | 163 | `"            \"attempted_without_usable_results\": len(no_usable),"` | — |
| [SRC-70795F4B61-L000164](../../scripts/compare_answer_quality_runs.py#L164) | 164 | `"            \"unknown_tool_outcome_count\": sum("` | — |
| [SRC-70795F4B61-L000165](../../scripts/compare_answer_quality_runs.py#L165) | 165 | `"                1 for r in search_cases"` | — |
| [SRC-70795F4B61-L000166](../../scripts/compare_answer_quality_runs.py#L166) | 166 | `"                if r.get(\"tool_status\") in (None, \"\", \"UNKNOWN\")"` | — |
| [SRC-70795F4B61-L000167](../../scripts/compare_answer_quality_runs.py#L167) | 167 | `"            ),"` | — |
| [SRC-70795F4B61-L000168](../../scripts/compare_answer_quality_runs.py#L168) | 168 | `"            \"required_tool_observation_count\": len(required_tool_rows),"` | — |
| [SRC-70795F4B61-L000169](../../scripts/compare_answer_quality_runs.py#L169) | 169 | `"            \"required_tool_success_count\": required_tool_successes,"` | — |
| [SRC-70795F4B61-L000170](../../scripts/compare_answer_quality_runs.py#L170) | 170 | `"            \"required_tool_success_rate\": _rate(required_tool_successes, len(required_tool_rows)),"` | — |
| [SRC-70795F4B61-L000171](../../scripts/compare_answer_quality_runs.py#L171) | 171 | `"            \"required_tool_status_counts\": tool_status_counts,"` | — |
| [SRC-70795F4B61-L000172](../../scripts/compare_answer_quality_runs.py#L172) | 172 | `"            \"required_tool_status_case_count\": sum("` | — |
| [SRC-70795F4B61-L000173](../../scripts/compare_answer_quality_runs.py#L173) | 173 | `"                1 for r in results"` | — |
| [SRC-70795F4B61-L000174](../../scripts/compare_answer_quality_runs.py#L174) | 174 | `"                if isinstance(r.get(\"required_tool_statuses\"), list)"` | — |
| [SRC-70795F4B61-L000175](../../scripts/compare_answer_quality_runs.py#L175) | 175 | `"                and r.get(\"required_tool_statuses\")"` | — |
| [SRC-70795F4B61-L000176](../../scripts/compare_answer_quality_runs.py#L176) | 176 | `"            ),"` | — |
| [SRC-70795F4B61-L000177](../../scripts/compare_answer_quality_runs.py#L177) | 177 | `"            \"required_tool_matrix_coverage\": {"` | — |
| [SRC-70795F4B61-L000178](../../scripts/compare_answer_quality_runs.py#L178) | 178 | `"                \"score\": ("` | — |
| [SRC-70795F4B61-L000179](../../scripts/compare_answer_quality_runs.py#L179) | 179 | `"                    round(required_tool_matrix_complete_count / len(results), 4)"` | — |
| [SRC-70795F4B61-L000180](../../scripts/compare_answer_quality_runs.py#L180) | 180 | `"                    if results and required_tool_matrix_telemetry_known"` | — |
| [SRC-70795F4B61-L000181](../../scripts/compare_answer_quality_runs.py#L181) | 181 | `"                    else None"` | — |
| [SRC-70795F4B61-L000182](../../scripts/compare_answer_quality_runs.py#L182) | 182 | `"                ),"` | — |
| [SRC-70795F4B61-L000183](../../scripts/compare_answer_quality_runs.py#L183) | 183 | `"                \"complete_case_count\": required_tool_matrix_complete_count,"` | — |
| [SRC-70795F4B61-L000184](../../scripts/compare_answer_quality_runs.py#L184) | 184 | `"                \"case_count\": len(results),"` | — |
| [SRC-70795F4B61-L000185](../../scripts/compare_answer_quality_runs.py#L185) | 185 | `"                \"incomplete_case_ids\": required_tool_matrix_incomplete_case_ids,"` | — |
| [SRC-70795F4B61-L000186](../../scripts/compare_answer_quality_runs.py#L186) | 186 | `"                \"status\": ("` | — |
| [SRC-70795F4B61-L000187](../../scripts/compare_answer_quality_runs.py#L187) | 187 | `"                    \"SCORED_FROM_EXPLICIT_TOOL_MATRIX\""` | — |
| [SRC-70795F4B61-L000188](../../scripts/compare_answer_quality_runs.py#L188) | 188 | `"                    if required_tool_matrix_telemetry_known"` | — |
| [SRC-70795F4B61-L000189](../../scripts/compare_answer_quality_runs.py#L189) | 189 | `"                    else \"NOT_MEASURED_REQUIRED_TOOL_MATRIX_TELEMETRY_MISSING\""` | — |
| [SRC-70795F4B61-L000190](../../scripts/compare_answer_quality_runs.py#L190) | 190 | `"                ),"` | — |
| [SRC-70795F4B61-L000191](../../scripts/compare_answer_quality_runs.py#L191) | 191 | `"            },"` | — |
| [SRC-70795F4B61-L000192](../../scripts/compare_answer_quality_runs.py#L192) | 192 | `"            \"required_tool_success_semantics\": ("` | — |
| [SRC-70795F4B61-L000193](../../scripts/compare_answer_quality_runs.py#L193) | 193 | `"                \"Only tool-specific completed-with-usable-output states count as success; \""` | — |
| [SRC-70795F4B61-L000194](../../scripts/compare_answer_quality_runs.py#L194) | 194 | `"                \"HTTP success and no-result attempts do not.\""` | — |
| [SRC-70795F4B61-L000195](../../scripts/compare_answer_quality_runs.py#L195) | 195 | `"            ),"` | — |
| [SRC-70795F4B61-L000196](../../scripts/compare_answer_quality_runs.py#L196) | 196 | `"        },"` | — |
| [SRC-70795F4B61-L000197](../../scripts/compare_answer_quality_runs.py#L197) | 197 | `"        \"provider_reported_model_cost\": {"` | — |
| [SRC-70795F4B61-L000198](../../scripts/compare_answer_quality_runs.py#L198) | 198 | `"            \"reported_sum_usd\": round(sum(costs), 10) if costs else None,"` | — |
| [SRC-70795F4B61-L000199](../../scripts/compare_answer_quality_runs.py#L199) | 199 | `"            \"cases_with_any_reported_cost\": len(costs),"` | — |
| [SRC-70795F4B61-L000200](../../scripts/compare_answer_quality_runs.py#L200) | 200 | `"            \"cases_complete_for_returned_model_calls\": complete_cost_cases,"` | — |
| [SRC-70795F4B61-L000201](../../scripts/compare_answer_quality_runs.py#L201) | 201 | `"            \"status\": ("` | — |
| [SRC-70795F4B61-L000202](../../scripts/compare_answer_quality_runs.py#L202) | 202 | `"                \"PARTIAL_OR_PROVIDER_REPORTED_ONLY\""` | — |
| [SRC-70795F4B61-L000203](../../scripts/compare_answer_quality_runs.py#L203) | 203 | `"                if costs"` | — |
| [SRC-70795F4B61-L000204](../../scripts/compare_answer_quality_runs.py#L204) | 204 | `"                else \"NOT_MEASURED_NO_PROVIDER_COST_REPORTED\""` | — |
| [SRC-70795F4B61-L000205](../../scripts/compare_answer_quality_runs.py#L205) | 205 | `"            ),"` | — |
| [SRC-70795F4B61-L000206](../../scripts/compare_answer_quality_runs.py#L206) | 206 | `"            \"complete_request_cost_usd\": ("` | — |
| [SRC-70795F4B61-L000207](../../scripts/compare_answer_quality_runs.py#L207) | 207 | `"                round(sum(reconciled_request_costs), 10) if request_cost_complete else None"` | — |
| [SRC-70795F4B61-L000208](../../scripts/compare_answer_quality_runs.py#L208) | 208 | `"            ),"` | — |
| [SRC-70795F4B61-L000209](../../scripts/compare_answer_quality_runs.py#L209) | 209 | `"            \"complete_request_cost_status\": ("` | — |
| [SRC-70795F4B61-L000210](../../scripts/compare_answer_quality_runs.py#L210) | 210 | `"                \"RECONCILED_COMPLETE_REQUEST_COST\""` | — |
| [SRC-70795F4B61-L000211](../../scripts/compare_answer_quality_runs.py#L211) | 211 | `"                if request_cost_complete"` | — |
| [SRC-70795F4B61-L000212](../../scripts/compare_answer_quality_runs.py#L212) | 212 | `"                else ("` | — |
| [SRC-70795F4B61-L000213](../../scripts/compare_answer_quality_runs.py#L213) | 213 | `"                    \"PARTIAL_EXTERNAL_COST_RECONCILIATION\""` | — |
| [SRC-70795F4B61-L000214](../../scripts/compare_answer_quality_runs.py#L214) | 214 | `"                    if complete_request_cost_count"` | — |
| [SRC-70795F4B61-L000215](../../scripts/compare_answer_quality_runs.py#L215) | 215 | `"                    else \"NOT_MEASURED_TOTAL_CONNECTOR_COSTS_NOT_EXPOSED\""` | — |
| [SRC-70795F4B61-L000216](../../scripts/compare_answer_quality_runs.py#L216) | 216 | `"                )"` | — |
| [SRC-70795F4B61-L000217](../../scripts/compare_answer_quality_runs.py#L217) | 217 | `"            ),"` | — |
| [SRC-70795F4B61-L000218](../../scripts/compare_answer_quality_runs.py#L218) | 218 | `"            \"complete_request_cost_case_count\": complete_request_cost_count,"` | — |
| [SRC-70795F4B61-L000219](../../scripts/compare_answer_quality_runs.py#L219) | 219 | `"        },"` | — |
| [SRC-70795F4B61-L000220](../../scripts/compare_answer_quality_runs.py#L220) | 220 | `"    }"` | — |
| [SRC-70795F4B61-L000221](../../scripts/compare_answer_quality_runs.py#L221) | 221 | `""` | — |
| [SRC-70795F4B61-L000222](../../scripts/compare_answer_quality_runs.py#L222) | 222 | `""` | — |
| [SRC-70795F4B61-L000223](../../scripts/compare_answer_quality_runs.py#L223) | 223 | `"def _load_review_scorer():"` | — |
| [SRC-70795F4B61-L000224](../../scripts/compare_answer_quality_runs.py#L224) | 224 | `"    path = ROOT / \"scripts\" / \"score_answer_quality_reviews.py\""` | — |
| [SRC-70795F4B61-L000225](../../scripts/compare_answer_quality_runs.py#L225) | 225 | `"    spec = importlib.util.spec_from_file_location(\"omarai_review_scorecard\", path)"` | — |
| [SRC-70795F4B61-L000226](../../scripts/compare_answer_quality_runs.py#L226) | 226 | `"    if spec is None or spec.loader is None:"` | — |
| [SRC-70795F4B61-L000227](../../scripts/compare_answer_quality_runs.py#L227) | 227 | `"        raise RuntimeError(\"Unable to load existing review scorecard: \" + str(path))"` | — |
| [SRC-70795F4B61-L000228](../../scripts/compare_answer_quality_runs.py#L228) | 228 | `"    module = importlib.util.module_from_spec(spec)"` | — |
| [SRC-70795F4B61-L000229](../../scripts/compare_answer_quality_runs.py#L229) | 229 | `"    spec.loader.exec_module(module)"` | — |
| [SRC-70795F4B61-L000230](../../scripts/compare_answer_quality_runs.py#L230) | 230 | `"    return module"` | — |
| [SRC-70795F4B61-L000231](../../scripts/compare_answer_quality_runs.py#L231) | 231 | `""` | — |
| [SRC-70795F4B61-L000232](../../scripts/compare_answer_quality_runs.py#L232) | 232 | `""` | — |
| [SRC-70795F4B61-L000233](../../scripts/compare_answer_quality_runs.py#L233) | 233 | `"def _reviewed_case_ids(review_data: dict[str, Any]) -> set[str]:"` | — |
| [SRC-70795F4B61-L000234](../../scripts/compare_answer_quality_runs.py#L234) | 234 | `"    reviews = review_data.get(\"reviews\")"` | — |
| [SRC-70795F4B61-L000235](../../scripts/compare_answer_quality_runs.py#L235) | 235 | `"    if not isinstance(reviews, list):"` | — |
| [SRC-70795F4B61-L000236](../../scripts/compare_answer_quality_runs.py#L236) | 236 | `"        raise ValueError(\"review file must contain a reviews array\")"` | — |
| [SRC-70795F4B61-L000237](../../scripts/compare_answer_quality_runs.py#L237) | 237 | `"    return {"` | — |
| [SRC-70795F4B61-L000238](../../scripts/compare_answer_quality_runs.py#L238) | 238 | `"        item[\"case_id\"]"` | — |
| [SRC-70795F4B61-L000239](../../scripts/compare_answer_quality_runs.py#L239) | 239 | `"        for item in reviews"` | — |
| [SRC-70795F4B61-L000240](../../scripts/compare_answer_quality_runs.py#L240) | 240 | `"        if isinstance(item, dict) and item.get(\"status\") == \"REVIEWED\""` | — |
| [SRC-70795F4B61-L000241](../../scripts/compare_answer_quality_runs.py#L241) | 241 | `"        and isinstance(item.get(\"case_id\"), str)"` | — |
| [SRC-70795F4B61-L000242](../../scripts/compare_answer_quality_runs.py#L242) | 242 | `"    }"` | — |
| [SRC-70795F4B61-L000243](../../scripts/compare_answer_quality_runs.py#L243) | 243 | `""` | — |
| [SRC-70795F4B61-L000244](../../scripts/compare_answer_quality_runs.py#L244) | 244 | `""` | — |
| [SRC-70795F4B61-L000245](../../scripts/compare_answer_quality_runs.py#L245) | 245 | `"def review_comparison("` | — |
| [SRC-70795F4B61-L000246](../../scripts/compare_answer_quality_runs.py#L246) | 246 | `"    baseline_reviews: dict[str, Any],"` | — |
| [SRC-70795F4B61-L000247](../../scripts/compare_answer_quality_runs.py#L247) | 247 | `"    candidate_reviews: dict[str, Any],"` | — |
| [SRC-70795F4B61-L000248](../../scripts/compare_answer_quality_runs.py#L248) | 248 | `"    corpus: dict[str, Any],"` | — |
| [SRC-70795F4B61-L000249](../../scripts/compare_answer_quality_runs.py#L249) | 249 | `") -> dict[str, Any]:"` | — |
| [SRC-70795F4B61-L000250](../../scripts/compare_answer_quality_runs.py#L250) | 250 | `"    baseline_ids = _reviewed_case_ids(baseline_reviews)"` | — |
| [SRC-70795F4B61-L000251](../../scripts/compare_answer_quality_runs.py#L251) | 251 | `"    candidate_ids = _reviewed_case_ids(candidate_reviews)"` | — |
| [SRC-70795F4B61-L000252](../../scripts/compare_answer_quality_runs.py#L252) | 252 | `"    if not baseline_ids or not candidate_ids:"` | — |
| [SRC-70795F4B61-L000253](../../scripts/compare_answer_quality_runs.py#L253) | 253 | `"        raise ValueError(\"both review files need explicitly REVIEWED cases\")"` | — |
| [SRC-70795F4B61-L000254](../../scripts/compare_answer_quality_runs.py#L254) | 254 | `"    corpus_cases = corpus.get(\"cases\")"` | — |
| [SRC-70795F4B61-L000255](../../scripts/compare_answer_quality_runs.py#L255) | 255 | `"    if not isinstance(corpus_cases, list) or not corpus_cases:"` | — |
| [SRC-70795F4B61-L000256](../../scripts/compare_answer_quality_runs.py#L256) | 256 | `"        raise ValueError(\"corpus must contain a non-empty cases array for full-coverage acceptance\")"` | — |
| [SRC-70795F4B61-L000257](../../scripts/compare_answer_quality_runs.py#L257) | 257 | `"    corpus_ids = {"` | — |
| [SRC-70795F4B61-L000258](../../scripts/compare_answer_quality_runs.py#L258) | 258 | `"        item.get(\"case_id\")"` | — |
| [SRC-70795F4B61-L000259](../../scripts/compare_answer_quality_runs.py#L259) | 259 | `"        for item in corpus_cases"` | — |
| [SRC-70795F4B61-L000260](../../scripts/compare_answer_quality_runs.py#L260) | 260 | `"        if isinstance(item, dict) and isinstance(item.get(\"case_id\"), str)"` | — |
| [SRC-70795F4B61-L000261](../../scripts/compare_answer_quality_runs.py#L261) | 261 | `"    }"` | — |
| [SRC-70795F4B61-L000262](../../scripts/compare_answer_quality_runs.py#L262) | 262 | `"    for label, reviewed_ids in ("` | — |
| [SRC-70795F4B61-L000263](../../scripts/compare_answer_quality_runs.py#L263) | 263 | `"        (\"baseline\", baseline_ids),"` | — |
| [SRC-70795F4B61-L000264](../../scripts/compare_answer_quality_runs.py#L264) | 264 | `"        (\"candidate\", candidate_ids),"` | — |
| [SRC-70795F4B61-L000265](../../scripts/compare_answer_quality_runs.py#L265) | 265 | `"    ):"` | — |
| [SRC-70795F4B61-L000266](../../scripts/compare_answer_quality_runs.py#L266) | 266 | `"        if reviewed_ids != corpus_ids:"` | — |
| [SRC-70795F4B61-L000267](../../scripts/compare_answer_quality_runs.py#L267) | 267 | `"            missing = sorted(corpus_ids - reviewed_ids)"` | — |
| [SRC-70795F4B61-L000268](../../scripts/compare_answer_quality_runs.py#L268) | 268 | `"            extra = sorted(reviewed_ids - corpus_ids)"` | — |
| [SRC-70795F4B61-L000269](../../scripts/compare_answer_quality_runs.py#L269) | 269 | `"            raise ValueError("` | — |
| [SRC-70795F4B61-L000270](../../scripts/compare_answer_quality_runs.py#L270) | 270 | `"                f\"incomplete human review coverage for {label}: \""` | — |
| [SRC-70795F4B61-L000271](../../scripts/compare_answer_quality_runs.py#L271) | 271 | `"                f\"missing={missing}; unknown={extra}\""` | — |
| [SRC-70795F4B61-L000272](../../scripts/compare_answer_quality_runs.py#L272) | 272 | `"            )"` | — |
| [SRC-70795F4B61-L000273](../../scripts/compare_answer_quality_runs.py#L273) | 273 | `"    if baseline_ids != candidate_ids:"` | — |
| [SRC-70795F4B61-L000274](../../scripts/compare_answer_quality_runs.py#L274) | 274 | `"        raise ValueError("` | — |
| [SRC-70795F4B61-L000275](../../scripts/compare_answer_quality_runs.py#L275) | 275 | `"            \"incomparable review coverage: REVIEWED case IDs differ between baseline and candidate\""` | — |
| [SRC-70795F4B61-L000276](../../scripts/compare_answer_quality_runs.py#L276) | 276 | `"        )"` | — |
| [SRC-70795F4B61-L000277](../../scripts/compare_answer_quality_runs.py#L277) | 277 | `"    scorer = _load_review_scorer()"` | — |
| [SRC-70795F4B61-L000278](../../scripts/compare_answer_quality_runs.py#L278) | 278 | `"    baseline = scorer.summarize_reviews(baseline_reviews, corpus)"` | — |
| [SRC-70795F4B61-L000279](../../scripts/compare_answer_quality_runs.py#L279) | 279 | `"    candidate = scorer.summarize_reviews(candidate_reviews, corpus)"` | — |
| [SRC-70795F4B61-L000280](../../scripts/compare_answer_quality_runs.py#L280) | 280 | `"    aliases = {"` | — |
| [SRC-70795F4B61-L000281](../../scripts/compare_answer_quality_runs.py#L281) | 281 | `"        \"retrieval_precision\": \"retrieval_precision\","` | — |
| [SRC-70795F4B61-L000282](../../scripts/compare_answer_quality_runs.py#L282) | 282 | `"        \"retrieval_recall\": \"retrieval_recall\","` | — |
| [SRC-70795F4B61-L000283](../../scripts/compare_answer_quality_runs.py#L283) | 283 | `"        \"factual_accuracy\": \"correctness\","` | — |
| [SRC-70795F4B61-L000284](../../scripts/compare_answer_quality_runs.py#L284) | 284 | `"        \"faithfulness\": \"faithfulness\","` | — |
| [SRC-70795F4B61-L000285](../../scripts/compare_answer_quality_runs.py#L285) | 285 | `"        \"citation_support\": \"citation_support\","` | — |
| [SRC-70795F4B61-L000286](../../scripts/compare_answer_quality_runs.py#L286) | 286 | `"        \"writing_quality_1_to_5\": \"writing_quality_1_to_5\","` | — |
| [SRC-70795F4B61-L000287](../../scripts/compare_answer_quality_runs.py#L287) | 287 | `"    }"` | — |
| [SRC-70795F4B61-L000288](../../scripts/compare_answer_quality_runs.py#L288) | 288 | `"    metrics: dict[str, Any] = {}"` | — |
| [SRC-70795F4B61-L000289](../../scripts/compare_answer_quality_runs.py#L289) | 289 | `"    for output_name, score_name in aliases.items():"` | — |
| [SRC-70795F4B61-L000290](../../scripts/compare_answer_quality_runs.py#L290) | 290 | `"        before = baseline[\"metrics\"][score_name][\"score\"]"` | — |
| [SRC-70795F4B61-L000291](../../scripts/compare_answer_quality_runs.py#L291) | 291 | `"        after = candidate[\"metrics\"][score_name][\"score\"]"` | — |
| [SRC-70795F4B61-L000292](../../scripts/compare_answer_quality_runs.py#L292) | 292 | `"        metrics[output_name] = {"` | — |
| [SRC-70795F4B61-L000293](../../scripts/compare_answer_quality_runs.py#L293) | 293 | `"            \"baseline\": before,"` | — |
| [SRC-70795F4B61-L000294](../../scripts/compare_answer_quality_runs.py#L294) | 294 | `"            \"candidate\": after,"` | — |
| [SRC-70795F4B61-L000295](../../scripts/compare_answer_quality_runs.py#L295) | 295 | `"            \"delta\": round(after - before, 4) if before is not None and after is not None else None,"` | — |
| [SRC-70795F4B61-L000296](../../scripts/compare_answer_quality_runs.py#L296) | 296 | `"            \"status\": ("` | — |
| [SRC-70795F4B61-L000297](../../scripts/compare_answer_quality_runs.py#L297) | 297 | `"                \"COMPARED\" if before is not None and after is not None"` | — |
| [SRC-70795F4B61-L000298](../../scripts/compare_answer_quality_runs.py#L298) | 298 | `"                else \"NOT_SCORABLE_MISSING_ANNOTATED_DENOMINATOR\""` | — |
| [SRC-70795F4B61-L000299](../../scripts/compare_answer_quality_runs.py#L299) | 299 | `"            ),"` | — |
| [SRC-70795F4B61-L000300](../../scripts/compare_answer_quality_runs.py#L300) | 300 | `"            \"source\": \"explicit_human_review\","` | — |
| [SRC-70795F4B61-L000301](../../scripts/compare_answer_quality_runs.py#L301) | 301 | `"        }"` | — |
| [SRC-70795F4B61-L000302](../../scripts/compare_answer_quality_runs.py#L302) | 302 | `"    return {"` | — |
| [SRC-70795F4B61-L000303](../../scripts/compare_answer_quality_runs.py#L303) | 303 | `"        \"reviewed_case_count\": len(baseline_ids),"` | — |
| [SRC-70795F4B61-L000304](../../scripts/compare_answer_quality_runs.py#L304) | 304 | `"        \"baseline_review_coverage\": baseline[\"reviewed_case_coverage\"],"` | — |
| [SRC-70795F4B61-L000305](../../scripts/compare_answer_quality_runs.py#L305) | 305 | `"        \"candidate_review_coverage\": candidate[\"reviewed_case_coverage\"],"` | — |
| [SRC-70795F4B61-L000306](../../scripts/compare_answer_quality_runs.py#L306) | 306 | `"        \"metrics\": metrics,"` | — |
| [SRC-70795F4B61-L000307](../../scripts/compare_answer_quality_runs.py#L307) | 307 | `"        \"automatic_answer_grading\": False,"` | — |
| [SRC-70795F4B61-L000308](../../scripts/compare_answer_quality_runs.py#L308) | 308 | `"        \"limitations\": ["` | — |
| [SRC-70795F4B61-L000309](../../scripts/compare_answer_quality_runs.py#L309) | 309 | `"            \"Scores reflect explicit human annotations, not automatic model grading.\","` | — |
| [SRC-70795F4B61-L000310](../../scripts/compare_answer_quality_runs.py#L310) | 310 | `"            \"Retrieval precision/recall require comparable candidate pools and relevance judgments.\","` | — |
| [SRC-70795F4B61-L000311](../../scripts/compare_answer_quality_runs.py#L311) | 311 | `"            \"Citation support measures reviewer-labelled citations that support the associated claims; URL presence alone is not evidence of support.\","` | — |
| [SRC-70795F4B61-L000312](../../scripts/compare_answer_quality_runs.py#L312) | 312 | `"        ],"` | — |
| [SRC-70795F4B61-L000313](../../scripts/compare_answer_quality_runs.py#L313) | 313 | `"    }"` | — |
| [SRC-70795F4B61-L000314](../../scripts/compare_answer_quality_runs.py#L314) | 314 | `""` | — |
| [SRC-70795F4B61-L000315](../../scripts/compare_answer_quality_runs.py#L315) | 315 | `""` | — |
| [SRC-70795F4B61-L000316](../../scripts/compare_answer_quality_runs.py#L316) | 316 | `"def compare_runs("` | — |
| [SRC-70795F4B61-L000317](../../scripts/compare_answer_quality_runs.py#L317) | 317 | `"    baseline: dict[str, Any],"` | — |
| [SRC-70795F4B61-L000318](../../scripts/compare_answer_quality_runs.py#L318) | 318 | `"    candidate: dict[str, Any],"` | — |
| [SRC-70795F4B61-L000319](../../scripts/compare_answer_quality_runs.py#L319) | 319 | `"    *,"` | — |
| [SRC-70795F4B61-L000320](../../scripts/compare_answer_quality_runs.py#L320) | 320 | `"    corpus: dict[str, Any] \| None = None,"` | — |
| [SRC-70795F4B61-L000321](../../scripts/compare_answer_quality_runs.py#L321) | 321 | `"    baseline_reviews: dict[str, Any] \| None = None,"` | — |
| [SRC-70795F4B61-L000322](../../scripts/compare_answer_quality_runs.py#L322) | 322 | `"    candidate_reviews: dict[str, Any] \| None = None,"` | — |
| [SRC-70795F4B61-L000323](../../scripts/compare_answer_quality_runs.py#L323) | 323 | `") -> dict[str, Any]:"` | — |
| [SRC-70795F4B61-L000324](../../scripts/compare_answer_quality_runs.py#L324) | 324 | `"    problems = validate_run(baseline, \"baseline\") + validate_run(candidate, \"candidate\")"` | — |
| [SRC-70795F4B61-L000325](../../scripts/compare_answer_quality_runs.py#L325) | 325 | `"    if problems:"` | — |
| [SRC-70795F4B61-L000326](../../scripts/compare_answer_quality_runs.py#L326) | 326 | `"        raise ValueError(\"; \".join(problems))"` | — |
| [SRC-70795F4B61-L000327](../../scripts/compare_answer_quality_runs.py#L327) | 327 | `"    if baseline.get(\"benchmark_id\") != candidate.get(\"benchmark_id\"):"` | — |
| [SRC-70795F4B61-L000328](../../scripts/compare_answer_quality_runs.py#L328) | 328 | `"        raise ValueError(\"baseline/candidate benchmark_id differs\")"` | — |
| [SRC-70795F4B61-L000329](../../scripts/compare_answer_quality_runs.py#L329) | 329 | `"    if baseline.get(\"benchmark_version\") != candidate.get(\"benchmark_version\"):"` | — |
| [SRC-70795F4B61-L000330](../../scripts/compare_answer_quality_runs.py#L330) | 330 | `"        raise ValueError(\"baseline/candidate benchmark_version differs\")"` | — |
| [SRC-70795F4B61-L000331](../../scripts/compare_answer_quality_runs.py#L331) | 331 | `"    if corpus is not None:"` | — |
| [SRC-70795F4B61-L000332](../../scripts/compare_answer_quality_runs.py#L332) | 332 | `"        if corpus.get(\"benchmark_id\") != baseline.get(\"benchmark_id\"):"` | — |
| [SRC-70795F4B61-L000333](../../scripts/compare_answer_quality_runs.py#L333) | 333 | `"            raise ValueError(\"runs do not match the supplied corpus benchmark_id\")"` | — |
| [SRC-70795F4B61-L000334](../../scripts/compare_answer_quality_runs.py#L334) | 334 | `"        if corpus.get(\"version\") != baseline.get(\"benchmark_version\"):"` | — |
| [SRC-70795F4B61-L000335](../../scripts/compare_answer_quality_runs.py#L335) | 335 | `"            raise ValueError(\"runs do not match the supplied corpus benchmark_version\")"` | — |
| [SRC-70795F4B61-L000336](../../scripts/compare_answer_quality_runs.py#L336) | 336 | `"    baseline_by_id = {row[\"case_id\"]: row for row in baseline[\"results\"]}"` | — |
| [SRC-70795F4B61-L000337](../../scripts/compare_answer_quality_runs.py#L337) | 337 | `"    candidate_by_id = {row[\"case_id\"]: row for row in candidate[\"results\"]}"` | — |
| [SRC-70795F4B61-L000338](../../scripts/compare_answer_quality_runs.py#L338) | 338 | `"    if set(baseline_by_id) != set(candidate_by_id):"` | — |
| [SRC-70795F4B61-L000339](../../scripts/compare_answer_quality_runs.py#L339) | 339 | `"        missing_candidate = sorted(set(baseline_by_id) - set(candidate_by_id))"` | — |
| [SRC-70795F4B61-L000340](../../scripts/compare_answer_quality_runs.py#L340) | 340 | `"        missing_baseline = sorted(set(candidate_by_id) - set(baseline_by_id))"` | — |
| [SRC-70795F4B61-L000341](../../scripts/compare_answer_quality_runs.py#L341) | 341 | `"        raise ValueError("` | — |
| [SRC-70795F4B61-L000342](../../scripts/compare_answer_quality_runs.py#L342) | 342 | `"            f\"incomparable case sets; missing in candidate={missing_candidate}; \""` | — |
| [SRC-70795F4B61-L000343](../../scripts/compare_answer_quality_runs.py#L343) | 343 | `"            f\"missing in baseline={missing_baseline}\""` | — |
| [SRC-70795F4B61-L000344](../../scripts/compare_answer_quality_runs.py#L344) | 344 | `"        )"` | — |
| [SRC-70795F4B61-L000345](../../scripts/compare_answer_quality_runs.py#L345) | 345 | `"    corpus_by_id = {"` | — |
| [SRC-70795F4B61-L000346](../../scripts/compare_answer_quality_runs.py#L346) | 346 | `"        case[\"case_id\"]: case"` | — |
| [SRC-70795F4B61-L000347](../../scripts/compare_answer_quality_runs.py#L347) | 347 | `"        for case in (corpus.get(\"cases\", []) if corpus is not None else [])"` | — |
| [SRC-70795F4B61-L000348](../../scripts/compare_answer_quality_runs.py#L348) | 348 | `"        if isinstance(case, dict) and isinstance(case.get(\"case_id\"), str)"` | — |
| [SRC-70795F4B61-L000349](../../scripts/compare_answer_quality_runs.py#L349) | 349 | `"    }"` | — |
| [SRC-70795F4B61-L000350](../../scripts/compare_answer_quality_runs.py#L350) | 350 | `"    for case_id in baseline_by_id:"` | — |
| [SRC-70795F4B61-L000351](../../scripts/compare_answer_quality_runs.py#L351) | 351 | `"        before_row = baseline_by_id[case_id]"` | — |
| [SRC-70795F4B61-L000352](../../scripts/compare_answer_quality_runs.py#L352) | 352 | `"        after_row = candidate_by_id[case_id]"` | — |
| [SRC-70795F4B61-L000353](../../scripts/compare_answer_quality_runs.py#L353) | 353 | `"        if before_row.get(\"prompt\") != after_row.get(\"prompt\"):"` | — |
| [SRC-70795F4B61-L000354](../../scripts/compare_answer_quality_runs.py#L354) | 354 | `"            raise ValueError(f\"incomparable question text for {case_id}\")"` | — |
| [SRC-70795F4B61-L000355](../../scripts/compare_answer_quality_runs.py#L355) | 355 | `"        if corpus is not None:"` | — |
| [SRC-70795F4B61-L000356](../../scripts/compare_answer_quality_runs.py#L356) | 356 | `"            corpus_case = corpus_by_id.get(case_id)"` | — |
| [SRC-70795F4B61-L000357](../../scripts/compare_answer_quality_runs.py#L357) | 357 | `"            if not isinstance(corpus_case, dict):"` | — |
| [SRC-70795F4B61-L000358](../../scripts/compare_answer_quality_runs.py#L358) | 358 | `"                raise ValueError(f\"{case_id}: case_id is not present in the supplied corpus\")"` | — |
| [SRC-70795F4B61-L000359](../../scripts/compare_answer_quality_runs.py#L359) | 359 | `"            if before_row.get(\"prompt\") != corpus_case.get(\"question\"):"` | — |
| [SRC-70795F4B61-L000360](../../scripts/compare_answer_quality_runs.py#L360) | 360 | `"                raise ValueError(f\"{case_id}: recorded prompt differs from the canonical corpus question\")"` | — |
| [SRC-70795F4B61-L000361](../../scripts/compare_answer_quality_runs.py#L361) | 361 | `"            if before_row.get(\"expected_strategy\") != corpus_case.get(\"expected_strategy\"):"` | — |
| [SRC-70795F4B61-L000362](../../scripts/compare_answer_quality_runs.py#L362) | 362 | `"                raise ValueError(f\"{case_id}: expected_strategy differs from the canonical corpus\")"` | — |
| [SRC-70795F4B61-L000363](../../scripts/compare_answer_quality_runs.py#L363) | 363 | `""` | — |
| [SRC-70795F4B61-L000364](../../scripts/compare_answer_quality_runs.py#L364) | 364 | `"    before_runtime = run_metrics(baseline)"` | — |
| [SRC-70795F4B61-L000365](../../scripts/compare_answer_quality_runs.py#L365) | 365 | `"    after_runtime = run_metrics(candidate)"` | — |
| [SRC-70795F4B61-L000366](../../scripts/compare_answer_quality_runs.py#L366) | 366 | `"    time_metrics = {}"` | — |
| [SRC-70795F4B61-L000367](../../scripts/compare_answer_quality_runs.py#L367) | 367 | `"    for key in (\"mean\", \"p50\", \"p95\", \"max\"):"` | — |
| [SRC-70795F4B61-L000368](../../scripts/compare_answer_quality_runs.py#L368) | 368 | `"        before = before_runtime[\"latency_ms\"][key]"` | — |
| [SRC-70795F4B61-L000369](../../scripts/compare_answer_quality_runs.py#L369) | 369 | `"        after = after_runtime[\"latency_ms\"][key]"` | — |
| [SRC-70795F4B61-L000370](../../scripts/compare_answer_quality_runs.py#L370) | 370 | `"        time_metrics[key] = {"` | — |
| [SRC-70795F4B61-L000371](../../scripts/compare_answer_quality_runs.py#L371) | 371 | `"            \"baseline_ms\": before,"` | — |
| [SRC-70795F4B61-L000372](../../scripts/compare_answer_quality_runs.py#L372) | 372 | `"            \"candidate_ms\": after,"` | — |
| [SRC-70795F4B61-L000373](../../scripts/compare_answer_quality_runs.py#L373) | 373 | `"            \"delta_ms\": round(after - before, 2) if before is not None and after is not None else None,"` | — |
| [SRC-70795F4B61-L000374](../../scripts/compare_answer_quality_runs.py#L374) | 374 | `"            \"status\": \"COMPARED\" if before is not None and after is not None else \"NOT_MEASURED\","` | — |
| [SRC-70795F4B61-L000375](../../scripts/compare_answer_quality_runs.py#L375) | 375 | `"        }"` | — |
| [SRC-70795F4B61-L000376](../../scripts/compare_answer_quality_runs.py#L376) | 376 | `""` | — |
| [SRC-70795F4B61-L000377](../../scripts/compare_answer_quality_runs.py#L377) | 377 | `"    cost_before = before_runtime[\"provider_reported_model_cost\"][\"reported_sum_usd\"]"` | — |
| [SRC-70795F4B61-L000378](../../scripts/compare_answer_quality_runs.py#L378) | 378 | `"    cost_after = after_runtime[\"provider_reported_model_cost\"][\"reported_sum_usd\"]"` | — |
| [SRC-70795F4B61-L000379](../../scripts/compare_answer_quality_runs.py#L379) | 379 | `"    cost_delta = round(cost_after - cost_before, 10) if cost_before is not None and cost_after is not None else None"` | — |
| [SRC-70795F4B61-L000380](../../scripts/compare_answer_quality_runs.py#L380) | 380 | `"    request_cost_before = before_runtime[\"provider_reported_model_cost\"][\"complete_request_cost_usd\"]"` | — |
| [SRC-70795F4B61-L000381](../../scripts/compare_answer_quality_runs.py#L381) | 381 | `"    request_cost_after = after_runtime[\"provider_reported_model_cost\"][\"complete_request_cost_usd\"]"` | — |
| [SRC-70795F4B61-L000382](../../scripts/compare_answer_quality_runs.py#L382) | 382 | `"    request_cost_delta = ("` | — |
| [SRC-70795F4B61-L000383](../../scripts/compare_answer_quality_runs.py#L383) | 383 | `"        round(request_cost_after - request_cost_before, 10)"` | — |
| [SRC-70795F4B61-L000384](../../scripts/compare_answer_quality_runs.py#L384) | 384 | `"        if request_cost_before is not None and request_cost_after is not None"` | — |
| [SRC-70795F4B61-L000385](../../scripts/compare_answer_quality_runs.py#L385) | 385 | `"        else None"` | — |
| [SRC-70795F4B61-L000386](../../scripts/compare_answer_quality_runs.py#L386) | 386 | `"    )"` | — |
| [SRC-70795F4B61-L000387](../../scripts/compare_answer_quality_runs.py#L387) | 387 | `"    runtime_deltas = {"` | — |
| [SRC-70795F4B61-L000388](../../scripts/compare_answer_quality_runs.py#L388) | 388 | `"        \"complete_request_cost_usd\": {"` | — |
| [SRC-70795F4B61-L000389](../../scripts/compare_answer_quality_runs.py#L389) | 389 | `"            \"baseline\": request_cost_before,"` | — |
| [SRC-70795F4B61-L000390](../../scripts/compare_answer_quality_runs.py#L390) | 390 | `"            \"candidate\": request_cost_after,"` | — |
| [SRC-70795F4B61-L000391](../../scripts/compare_answer_quality_runs.py#L391) | 391 | `"            \"delta\": request_cost_delta,"` | — |
| [SRC-70795F4B61-L000392](../../scripts/compare_answer_quality_runs.py#L392) | 392 | `"            \"status\": ("` | — |
| [SRC-70795F4B61-L000393](../../scripts/compare_answer_quality_runs.py#L393) | 393 | `"                \"COMPARED\""` | — |
| [SRC-70795F4B61-L000394](../../scripts/compare_answer_quality_runs.py#L394) | 394 | `"                if request_cost_before is not None and request_cost_after is not None"` | — |
| [SRC-70795F4B61-L000395](../../scripts/compare_answer_quality_runs.py#L395) | 395 | `"                else \"NOT_MEASURED_OR_INCOMPLETE_RECONCILIATION\""` | — |
| [SRC-70795F4B61-L000396](../../scripts/compare_answer_quality_runs.py#L396) | 396 | `"            ),"` | — |
| [SRC-70795F4B61-L000397](../../scripts/compare_answer_quality_runs.py#L397) | 397 | `"        },"` | — |
| [SRC-70795F4B61-L000398](../../scripts/compare_answer_quality_runs.py#L398) | 398 | `"        \"transport_success_rate\": {"` | — |
| [SRC-70795F4B61-L000399](../../scripts/compare_answer_quality_runs.py#L399) | 399 | `"            \"baseline\": before_runtime[\"transport_success_rate\"][\"score\"],"` | — |
| [SRC-70795F4B61-L000400](../../scripts/compare_answer_quality_runs.py#L400) | 400 | `"            \"candidate\": after_runtime[\"transport_success_rate\"][\"score\"],"` | — |
| [SRC-70795F4B61-L000401](../../scripts/compare_answer_quality_runs.py#L401) | 401 | `"        },"` | — |
| [SRC-70795F4B61-L000402](../../scripts/compare_answer_quality_runs.py#L402) | 402 | `"        \"usable_result_rate\": {"` | — |
| [SRC-70795F4B61-L000403](../../scripts/compare_answer_quality_runs.py#L403) | 403 | `"            \"baseline\": before_runtime[\"tool_usage\"][\"usable_result_rate\"][\"score\"],"` | — |
| [SRC-70795F4B61-L000404](../../scripts/compare_answer_quality_runs.py#L404) | 404 | `"            \"candidate\": after_runtime[\"tool_usage\"][\"usable_result_rate\"][\"score\"],"` | — |
| [SRC-70795F4B61-L000405](../../scripts/compare_answer_quality_runs.py#L405) | 405 | `"        },"` | — |
| [SRC-70795F4B61-L000406](../../scripts/compare_answer_quality_runs.py#L406) | 406 | `"        \"required_tool_success_rate\": {"` | — |
| [SRC-70795F4B61-L000407](../../scripts/compare_answer_quality_runs.py#L407) | 407 | `"            \"baseline\": before_runtime[\"tool_usage\"][\"required_tool_success_rate\"][\"score\"],"` | — |
| [SRC-70795F4B61-L000408](../../scripts/compare_answer_quality_runs.py#L408) | 408 | `"            \"candidate\": after_runtime[\"tool_usage\"][\"required_tool_success_rate\"][\"score\"],"` | — |
| [SRC-70795F4B61-L000409](../../scripts/compare_answer_quality_runs.py#L409) | 409 | `"        },"` | — |
| [SRC-70795F4B61-L000410](../../scripts/compare_answer_quality_runs.py#L410) | 410 | `"        \"provider_reported_model_cost_usd\": {"` | — |
| [SRC-70795F4B61-L000411](../../scripts/compare_answer_quality_runs.py#L411) | 411 | `"            \"baseline\": cost_before,"` | — |
| [SRC-70795F4B61-L000412](../../scripts/compare_answer_quality_runs.py#L412) | 412 | `"            \"candidate\": cost_after,"` | — |
| [SRC-70795F4B61-L000413](../../scripts/compare_answer_quality_runs.py#L413) | 413 | `"            \"delta\": cost_delta,"` | — |
| [SRC-70795F4B61-L000414](../../scripts/compare_answer_quality_runs.py#L414) | 414 | `"            \"status\": ("` | — |
| [SRC-70795F4B61-L000415](../../scripts/compare_answer_quality_runs.py#L415) | 415 | `"                \"PARTIAL_OR_PROVIDER_REPORTED_ONLY\""` | — |
| [SRC-70795F4B61-L000416](../../scripts/compare_answer_quality_runs.py#L416) | 416 | `"                if cost_before is not None and cost_after is not None"` | — |
| [SRC-70795F4B61-L000417](../../scripts/compare_answer_quality_runs.py#L417) | 417 | `"                else \"NOT_MEASURED\""` | — |
| [SRC-70795F4B61-L000418](../../scripts/compare_answer_quality_runs.py#L418) | 418 | `"            ),"` | — |
| [SRC-70795F4B61-L000419](../../scripts/compare_answer_quality_runs.py#L419) | 419 | `"        },"` | — |
| [SRC-70795F4B61-L000420](../../scripts/compare_answer_quality_runs.py#L420) | 420 | `"    }"` | — |
| [SRC-70795F4B61-L000421](../../scripts/compare_answer_quality_runs.py#L421) | 421 | `"    for key in (\"transport_success_rate\", \"usable_result_rate\", \"required_tool_success_rate\"):"` | — |
| [SRC-70795F4B61-L000422](../../scripts/compare_answer_quality_runs.py#L422) | 422 | `"        before = runtime_deltas[key][\"baseline\"]"` | — |
| [SRC-70795F4B61-L000423](../../scripts/compare_answer_quality_runs.py#L423) | 423 | `"        after = runtime_deltas[key][\"candidate\"]"` | — |
| [SRC-70795F4B61-L000424](../../scripts/compare_answer_quality_runs.py#L424) | 424 | `"        runtime_deltas[key][\"delta\"] = round(after - before, 4) if before is not None and after is not None else None"` | — |
| [SRC-70795F4B61-L000425](../../scripts/compare_answer_quality_runs.py#L425) | 425 | `"    comparison: dict[str, Any] = {"` | — |
| [SRC-70795F4B61-L000426](../../scripts/compare_answer_quality_runs.py#L426) | 426 | `"        \"schema_version\": \"1.0\","` | — |
| [SRC-70795F4B61-L000427](../../scripts/compare_answer_quality_runs.py#L427) | 427 | `"        \"benchmark_id\": baseline[\"benchmark_id\"],"` | — |
| [SRC-70795F4B61-L000428](../../scripts/compare_answer_quality_runs.py#L428) | 428 | `"        \"benchmark_version\": baseline[\"benchmark_version\"],"` | — |
| [SRC-70795F4B61-L000429](../../scripts/compare_answer_quality_runs.py#L429) | 429 | `"        \"case_count\": len(baseline_by_id),"` | — |
| [SRC-70795F4B61-L000430](../../scripts/compare_answer_quality_runs.py#L430) | 430 | `"        \"baseline\": {"` | — |
| [SRC-70795F4B61-L000431](../../scripts/compare_answer_quality_runs.py#L431) | 431 | `"            \"build_sha\": baseline.get(\"build_sha\", \"unknown\"),"` | — |
| [SRC-70795F4B61-L000432](../../scripts/compare_answer_quality_runs.py#L432) | 432 | `"            \"executed_at_utc\": baseline.get(\"executed_at_utc\"),"` | — |
| [SRC-70795F4B61-L000433](../../scripts/compare_answer_quality_runs.py#L433) | 433 | `"            \"metrics\": before_runtime,"` | — |
| [SRC-70795F4B61-L000434](../../scripts/compare_answer_quality_runs.py#L434) | 434 | `"        },"` | — |
| [SRC-70795F4B61-L000435](../../scripts/compare_answer_quality_runs.py#L435) | 435 | `"        \"candidate\": {"` | — |
| [SRC-70795F4B61-L000436](../../scripts/compare_answer_quality_runs.py#L436) | 436 | `"            \"build_sha\": candidate.get(\"build_sha\", \"unknown\"),"` | — |
| [SRC-70795F4B61-L000437](../../scripts/compare_answer_quality_runs.py#L437) | 437 | `"            \"executed_at_utc\": candidate.get(\"executed_at_utc\"),"` | — |
| [SRC-70795F4B61-L000438](../../scripts/compare_answer_quality_runs.py#L438) | 438 | `"            \"metrics\": after_runtime,"` | — |
| [SRC-70795F4B61-L000439](../../scripts/compare_answer_quality_runs.py#L439) | 439 | `"        },"` | — |
| [SRC-70795F4B61-L000440](../../scripts/compare_answer_quality_runs.py#L440) | 440 | `"        \"runtime_deltas\": runtime_deltas,"` | — |
| [SRC-70795F4B61-L000441](../../scripts/compare_answer_quality_runs.py#L441) | 441 | `"        \"latency_comparison\": time_metrics,"` | — |
| [SRC-70795F4B61-L000442](../../scripts/compare_answer_quality_runs.py#L442) | 442 | `"        \"quality_comparison\": None,"` | — |
| [SRC-70795F4B61-L000443](../../scripts/compare_answer_quality_runs.py#L443) | 443 | `"        \"acceptance_status\": \"PARTIAL\","` | — |
| [SRC-70795F4B61-L000444](../../scripts/compare_answer_quality_runs.py#L444) | 444 | `"        \"acceptance_blockers\": [],"` | — |
| [SRC-70795F4B61-L000445](../../scripts/compare_answer_quality_runs.py#L445) | 445 | `"        \"interpretation\": ["` | — |
| [SRC-70795F4B61-L000446](../../scripts/compare_answer_quality_runs.py#L446) | 446 | `"            \"The same benchmark version, case IDs, and exact question text were compared.\","` | — |
| [SRC-70795F4B61-L000447](../../scripts/compare_answer_quality_runs.py#L447) | 447 | `"            \"HTTP transport success is not semantic correctness, and a successful search request is not proof that the answer is correct.\","` | — |
| [SRC-70795F4B61-L000448](../../scripts/compare_answer_quality_runs.py#L448) | 448 | `"            \"Required-tool success is scored only from complete tool-status matrices; missing required rows count as failures and block complete acceptance.\","` | — |
| [SRC-70795F4B61-L000449](../../scripts/compare_answer_quality_runs.py#L449) | 449 | `"            \"Complete request cost is intentionally null because search connector costs are not consistently exposed; only explicit provider-reported model cost is summarized.\","` | — |
| [SRC-70795F4B61-L000450](../../scripts/compare_answer_quality_runs.py#L450) | 450 | `"        ],"` | — |
| [SRC-70795F4B61-L000451](../../scripts/compare_answer_quality_runs.py#L451) | 451 | `"    }"` | — |
| [SRC-70795F4B61-L000452](../../scripts/compare_answer_quality_runs.py#L452) | 452 | `"    for label, metrics in ((\"baseline\", before_runtime), (\"candidate\", after_runtime)):"` | — |
| [SRC-70795F4B61-L000453](../../scripts/compare_answer_quality_runs.py#L453) | 453 | `"        matrix_coverage = metrics[\"tool_usage\"][\"required_tool_matrix_coverage\"]"` | — |
| [SRC-70795F4B61-L000454](../../scripts/compare_answer_quality_runs.py#L454) | 454 | `"        if ("` | — |
| [SRC-70795F4B61-L000455](../../scripts/compare_answer_quality_runs.py#L455) | 455 | `"            matrix_coverage[\"status\"] != \"SCORED_FROM_EXPLICIT_TOOL_MATRIX\""` | — |
| [SRC-70795F4B61-L000456](../../scripts/compare_answer_quality_runs.py#L456) | 456 | `"            or matrix_coverage[\"score\"] != 1.0"` | — |
| [SRC-70795F4B61-L000457](../../scripts/compare_answer_quality_runs.py#L457) | 457 | `"        ):"` | — |
| [SRC-70795F4B61-L000458](../../scripts/compare_answer_quality_runs.py#L458) | 458 | `"            comparison[\"acceptance_blockers\"].append("` | — |
| [SRC-70795F4B61-L000459](../../scripts/compare_answer_quality_runs.py#L459) | 459 | `"                f\"{label}_required_tool_matrix_incomplete\""` | — |
| [SRC-70795F4B61-L000460](../../scripts/compare_answer_quality_runs.py#L460) | 460 | `"            )"` | — |
| [SRC-70795F4B61-L000461](../../scripts/compare_answer_quality_runs.py#L461) | 461 | `"    sha_re = re.compile(r\"^[0-9a-fA-F]{40}$\")"` | — |
| [SRC-70795F4B61-L000462](../../scripts/compare_answer_quality_runs.py#L462) | 462 | `"    for label, run in ((\"baseline\", baseline), (\"candidate\", candidate)):"` | — |
| [SRC-70795F4B61-L000463](../../scripts/compare_answer_quality_runs.py#L463) | 463 | `"        if not isinstance(run.get(\"build_sha\"), str) or not sha_re.fullmatch(run[\"build_sha\"]):"` | — |
| [SRC-70795F4B61-L000464](../../scripts/compare_answer_quality_runs.py#L464) | 464 | `"            comparison[\"acceptance_blockers\"].append(f\"{label}_build_sha_missing_or_invalid\")"` | — |
| [SRC-70795F4B61-L000465](../../scripts/compare_answer_quality_runs.py#L465) | 465 | `"    for label, metrics in ((\"baseline\", before_runtime), (\"candidate\", after_runtime)):"` | — |
| [SRC-70795F4B61-L000466](../../scripts/compare_answer_quality_runs.py#L466) | 466 | `"        if metrics[\"provider_reported_model_cost\"][\"complete_request_cost_status\"] != \"RECONCILED_COMPLETE_REQUEST_COST\":"` | — |
| [SRC-70795F4B61-L000467](../../scripts/compare_answer_quality_runs.py#L467) | 467 | `"            comparison[\"acceptance_blockers\"].append(f\"{label}_complete_request_cost_missing_or_partial\")"` | — |
| [SRC-70795F4B61-L000468](../../scripts/compare_answer_quality_runs.py#L468) | 468 | `"    if baseline_reviews is None and candidate_reviews is None:"` | — |
| [SRC-70795F4B61-L000469](../../scripts/compare_answer_quality_runs.py#L469) | 469 | `"        comparison[\"acceptance_blockers\"].append(\"human_review_files_missing\")"` | — |
| [SRC-70795F4B61-L000470](../../scripts/compare_answer_quality_runs.py#L470) | 470 | `"    elif baseline_reviews is None or candidate_reviews is None or corpus is None:"` | — |
| [SRC-70795F4B61-L000471](../../scripts/compare_answer_quality_runs.py#L471) | 471 | `"        comparison[\"acceptance_blockers\"].append(\"both_review_files_and_corpus_are_required\")"` | — |
| [SRC-70795F4B61-L000472](../../scripts/compare_answer_quality_runs.py#L472) | 472 | `"    else:"` | — |
| [SRC-70795F4B61-L000473](../../scripts/compare_answer_quality_runs.py#L473) | 473 | `"        corpus_ids = {"` | — |
| [SRC-70795F4B61-L000474](../../scripts/compare_answer_quality_runs.py#L474) | 474 | `"            case.get(\"case_id\")"` | — |
| [SRC-70795F4B61-L000475](../../scripts/compare_answer_quality_runs.py#L475) | 475 | `"            for case in corpus.get(\"cases\", [])"` | — |
| [SRC-70795F4B61-L000476](../../scripts/compare_answer_quality_runs.py#L476) | 476 | `"            if isinstance(case, dict) and isinstance(case.get(\"case_id\"), str)"` | — |
| [SRC-70795F4B61-L000477](../../scripts/compare_answer_quality_runs.py#L477) | 477 | `"        }"` | — |
| [SRC-70795F4B61-L000478](../../scripts/compare_answer_quality_runs.py#L478) | 478 | `"        if set(baseline_by_id) != corpus_ids:"` | — |
| [SRC-70795F4B61-L000479](../../scripts/compare_answer_quality_runs.py#L479) | 479 | `"            comparison[\"acceptance_blockers\"].append(\"benchmark_run_does_not_cover_entire_corpus\")"` | — |
| [SRC-70795F4B61-L000480](../../scripts/compare_answer_quality_runs.py#L480) | 480 | `"        comparison[\"quality_comparison\"] = review_comparison("` | — |
| [SRC-70795F4B61-L000481](../../scripts/compare_answer_quality_runs.py#L481) | 481 | `"            baseline_reviews, candidate_reviews, corpus"` | — |
| [SRC-70795F4B61-L000482](../../scripts/compare_answer_quality_runs.py#L482) | 482 | `"        )"` | — |
| [SRC-70795F4B61-L000483](../../scripts/compare_answer_quality_runs.py#L483) | 483 | `"        unscored_quality = ["` | — |
| [SRC-70795F4B61-L000484](../../scripts/compare_answer_quality_runs.py#L484) | 484 | `"            name for name, metric in comparison[\"quality_comparison\"][\"metrics\"].items()"` | — |
| [SRC-70795F4B61-L000485](../../scripts/compare_answer_quality_runs.py#L485) | 485 | `"            if metric[\"status\"] != \"COMPARED\""` | — |
| [SRC-70795F4B61-L000486](../../scripts/compare_answer_quality_runs.py#L486) | 486 | `"        ]"` | — |
| [SRC-70795F4B61-L000487](../../scripts/compare_answer_quality_runs.py#L487) | 487 | `"        if unscored_quality:"` | — |
| [SRC-70795F4B61-L000488](../../scripts/compare_answer_quality_runs.py#L488) | 488 | `"            comparison[\"acceptance_blockers\"].append("` | — |
| [SRC-70795F4B61-L000489](../../scripts/compare_answer_quality_runs.py#L489) | 489 | `"                \"required_quality_metrics_unscored:\" + \",\".join(unscored_quality)"` | — |
| [SRC-70795F4B61-L000490](../../scripts/compare_answer_quality_runs.py#L490) | 490 | `"            )"` | — |
| [SRC-70795F4B61-L000491](../../scripts/compare_answer_quality_runs.py#L491) | 491 | `"    if not comparison[\"acceptance_blockers\"]:"` | — |
| [SRC-70795F4B61-L000492](../../scripts/compare_answer_quality_runs.py#L492) | 492 | `"        comparison[\"acceptance_status\"] = \"COMPARABLE_WITH_REVIEWED_QUALITY_AND_BUILD_IDENTITIES\""` | — |
| [SRC-70795F4B61-L000493](../../scripts/compare_answer_quality_runs.py#L493) | 493 | `"    else:"` | — |
| [SRC-70795F4B61-L000494](../../scripts/compare_answer_quality_runs.py#L494) | 494 | `"        comparison[\"acceptance_status\"] = \"INCOMPLETE\""` | — |
| [SRC-70795F4B61-L000495](../../scripts/compare_answer_quality_runs.py#L495) | 495 | `"    return comparison"` | — |
| [SRC-70795F4B61-L000496](../../scripts/compare_answer_quality_runs.py#L496) | 496 | `""` | — |
| [SRC-70795F4B61-L000497](../../scripts/compare_answer_quality_runs.py#L497) | 497 | `""` | — |
| [SRC-70795F4B61-L000498](../../scripts/compare_answer_quality_runs.py#L498) | 498 | `"def main(argv: list[str] \| None = None) -> int:"` | — |
| [SRC-70795F4B61-L000499](../../scripts/compare_answer_quality_runs.py#L499) | 499 | `"    parser = argparse.ArgumentParser(description=__doc__)"` | — |
| [SRC-70795F4B61-L000500](../../scripts/compare_answer_quality_runs.py#L500) | 500 | `"    parser.add_argument(\"--baseline-run\", type=Path, required=True)"` | — |
| [SRC-70795F4B61-L000501](../../scripts/compare_answer_quality_runs.py#L501) | 501 | `"    parser.add_argument(\"--candidate-run\", type=Path, required=True)"` | — |
| [SRC-70795F4B61-L000502](../../scripts/compare_answer_quality_runs.py#L502) | 502 | `"    parser.add_argument(\"--baseline-reviews\", type=Path)"` | — |
| [SRC-70795F4B61-L000503](../../scripts/compare_answer_quality_runs.py#L503) | 503 | `"    parser.add_argument(\"--candidate-reviews\", type=Path)"` | — |
| [SRC-70795F4B61-L000504](../../scripts/compare_answer_quality_runs.py#L504) | 504 | `"    parser.add_argument(\"--corpus\", type=Path, default=DEFAULT_CORPUS)"` | — |
| [SRC-70795F4B61-L000505](../../scripts/compare_answer_quality_runs.py#L505) | 505 | `"    parser.add_argument(\"--out\", type=Path)"` | — |
| [SRC-70795F4B61-L000506](../../scripts/compare_answer_quality_runs.py#L506) | 506 | `"    args = parser.parse_args(argv)"` | — |
| [SRC-70795F4B61-L000507](../../scripts/compare_answer_quality_runs.py#L507) | 507 | `"    if bool(args.baseline_reviews) != bool(args.candidate_reviews):"` | — |
| [SRC-70795F4B61-L000508](../../scripts/compare_answer_quality_runs.py#L508) | 508 | `"        parser.error(\"provide both --baseline-reviews and --candidate-reviews, or neither\")"` | — |
| [SRC-70795F4B61-L000509](../../scripts/compare_answer_quality_runs.py#L509) | 509 | `"    try:"` | — |
| [SRC-70795F4B61-L000510](../../scripts/compare_answer_quality_runs.py#L510) | 510 | `"        baseline = load_json_object(args.baseline_run)"` | — |
| [SRC-70795F4B61-L000511](../../scripts/compare_answer_quality_runs.py#L511) | 511 | `"        candidate = load_json_object(args.candidate_run)"` | — |
| [SRC-70795F4B61-L000512](../../scripts/compare_answer_quality_runs.py#L512) | 512 | `"        corpus = load_json_object(args.corpus) if args.baseline_reviews else None"` | — |
| [SRC-70795F4B61-L000513](../../scripts/compare_answer_quality_runs.py#L513) | 513 | `"        before_reviews = load_json_object(args.baseline_reviews) if args.baseline_reviews else None"` | — |
| [SRC-70795F4B61-L000514](../../scripts/compare_answer_quality_runs.py#L514) | 514 | `"        after_reviews = load_json_object(args.candidate_reviews) if args.candidate_reviews else None"` | — |
| [SRC-70795F4B61-L000515](../../scripts/compare_answer_quality_runs.py#L515) | 515 | `"        result = compare_runs("` | — |
| [SRC-70795F4B61-L000516](../../scripts/compare_answer_quality_runs.py#L516) | 516 | `"            baseline, candidate, corpus=corpus,"` | — |
| [SRC-70795F4B61-L000517](../../scripts/compare_answer_quality_runs.py#L517) | 517 | `"            baseline_reviews=before_reviews, candidate_reviews=after_reviews,"` | — |
| [SRC-70795F4B61-L000518](../../scripts/compare_answer_quality_runs.py#L518) | 518 | `"        )"` | — |
| [SRC-70795F4B61-L000519](../../scripts/compare_answer_quality_runs.py#L519) | 519 | `"    except (OSError, ValueError, TypeError, json.JSONDecodeError, KeyError) as exc:"` | — |
| [SRC-70795F4B61-L000520](../../scripts/compare_answer_quality_runs.py#L520) | 520 | `"        print(\"COMPARISON INVALID: \" + str(exc), file=sys.stderr)"` | — |
| [SRC-70795F4B61-L000521](../../scripts/compare_answer_quality_runs.py#L521) | 521 | `"        return 2"` | — |
| [SRC-70795F4B61-L000522](../../scripts/compare_answer_quality_runs.py#L522) | 522 | `"    output = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True)"` | — |
| [SRC-70795F4B61-L000523](../../scripts/compare_answer_quality_runs.py#L523) | 523 | `"    if args.out:"` | — |
| [SRC-70795F4B61-L000524](../../scripts/compare_answer_quality_runs.py#L524) | 524 | `"        args.out.write_text(output + \"\\n\", encoding=\"utf-8\")"` | — |
| [SRC-70795F4B61-L000525](../../scripts/compare_answer_quality_runs.py#L525) | 525 | `"        print(\"Wrote \" + str(args.out))"` | — |
| [SRC-70795F4B61-L000526](../../scripts/compare_answer_quality_runs.py#L526) | 526 | `"    print(output)"` | — |
| [SRC-70795F4B61-L000527](../../scripts/compare_answer_quality_runs.py#L527) | 527 | `"    return 0 if result[\"acceptance_status\"] == \"COMPARABLE_WITH_REVIEWED_QUALITY_AND_BUILD_IDENTITIES\" else 2"` | — |
| [SRC-70795F4B61-L000528](../../scripts/compare_answer_quality_runs.py#L528) | 528 | `""` | — |
| [SRC-70795F4B61-L000529](../../scripts/compare_answer_quality_runs.py#L529) | 529 | `""` | — |
| [SRC-70795F4B61-L000530](../../scripts/compare_answer_quality_runs.py#L530) | 530 | `"if __name__ == \"__main__\":"` | — |
| [SRC-70795F4B61-L000531](../../scripts/compare_answer_quality_runs.py#L531) | 531 | `"    raise SystemExit(main())"` | — |
## ملفات أخرى

### FILE-A8360B1B03 — [scripts/hosted_smoke_test.py](../../scripts/hosted_smoke_test.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-A8360B1B03-L000001](../../scripts/hosted_smoke_test.py#L1) | 1 | `"#!/usr/bin/env python3"` | — |
| [SRC-A8360B1B03-L000002](../../scripts/hosted_smoke_test.py#L2) | 2 | `"\"\"\"End-to-end smoke test for a deployed Omarai instance; uses only stdlib.\"\"\""` | — |
| [SRC-A8360B1B03-L000003](../../scripts/hosted_smoke_test.py#L3) | 3 | `"from __future__ import annotations"` | — |
| [SRC-A8360B1B03-L000004](../../scripts/hosted_smoke_test.py#L4) | 4 | `""` | — |
| [SRC-A8360B1B03-L000005](../../scripts/hosted_smoke_test.py#L5) | 5 | `"import argparse"` | — |
| [SRC-A8360B1B03-L000006](../../scripts/hosted_smoke_test.py#L6) | 6 | `"import json"` | — |
| [SRC-A8360B1B03-L000007](../../scripts/hosted_smoke_test.py#L7) | 7 | `"import os"` | — |
| [SRC-A8360B1B03-L000008](../../scripts/hosted_smoke_test.py#L8) | 8 | `"import re"` | — |
| [SRC-A8360B1B03-L000009](../../scripts/hosted_smoke_test.py#L9) | 9 | `"from pathlib import Path"` | — |
| [SRC-A8360B1B03-L000010](../../scripts/hosted_smoke_test.py#L10) | 10 | `"import sys"` | — |
| [SRC-A8360B1B03-L000011](../../scripts/hosted_smoke_test.py#L11) | 11 | `"import urllib.error"` | — |
| [SRC-A8360B1B03-L000012](../../scripts/hosted_smoke_test.py#L12) | 12 | `"import urllib.parse"` | — |
| [SRC-A8360B1B03-L000013](../../scripts/hosted_smoke_test.py#L13) | 13 | `"import urllib.request"` | — |
| [SRC-A8360B1B03-L000014](../../scripts/hosted_smoke_test.py#L14) | 14 | `"from typing import Any"` | — |
| [SRC-A8360B1B03-L000015](../../scripts/hosted_smoke_test.py#L15) | 15 | `""` | — |
| [SRC-A8360B1B03-L000016](../../scripts/hosted_smoke_test.py#L16) | 16 | `""` | — |
| [SRC-A8360B1B03-L000017](../../scripts/hosted_smoke_test.py#L17) | 17 | `"LIVE_TEST_QUESTION = ("` | — |
| [SRC-A8360B1B03-L000018](../../scripts/hosted_smoke_test.py#L18) | 18 | `"    \"اختبار اكتساب عملاء: ابحث عن طلبات شراء أو مناقصات منشورة وحديثة في مصر تخص \""` | — |
| [SRC-A8360B1B03-L000019](../../scripts/hosted_smoke_test.py#L19) | 19 | `"    \"أنظمة إنذار الحريق. لا تعتبر شركة عميلاً محتملاً إلا إذا وجدت إشارة شراء صريحة \""` | — |
| [SRC-A8360B1B03-L000020](../../scripts/hosted_smoke_test.py#L20) | 20 | `"    \"أو طلب عرض سعر منشورًا. اعرض لكل إشارة المصدر والرابط والتاريخ ومقتطف الدليل، \""` | — |
| [SRC-A8360B1B03-L000021](../../scripts/hosted_smoke_test.py#L21) | 21 | `"    \"وصرّح بوضوح إذا لم تجد طلبًا مؤكدًا.\""` | — |
| [SRC-A8360B1B03-L000022](../../scripts/hosted_smoke_test.py#L22) | 22 | `")"` | — |
| [SRC-A8360B1B03-L000023](../../scripts/hosted_smoke_test.py#L23) | 23 | `""` | — |
| [SRC-A8360B1B03-L000024](../../scripts/hosted_smoke_test.py#L24) | 24 | `""` | — |
| [SRC-A8360B1B03-L000025](../../scripts/hosted_smoke_test.py#L25) | 25 | `"class SmokeError(RuntimeError):"` | — |
| [SRC-A8360B1B03-L000026](../../scripts/hosted_smoke_test.py#L26) | 26 | `"    \"\"\"A live acceptance check failed, optionally carrying a safe partial report.\"\"\""` | — |
| [SRC-A8360B1B03-L000027](../../scripts/hosted_smoke_test.py#L27) | 27 | `""` | — |
| [SRC-A8360B1B03-L000028](../../scripts/hosted_smoke_test.py#L28) | 28 | `"    def __init__(self, message: str, report: dict[str, Any] \| None = None):"` | — |
| [SRC-A8360B1B03-L000029](../../scripts/hosted_smoke_test.py#L29) | 29 | `"        super().__init__(message)"` | — |
| [SRC-A8360B1B03-L000030](../../scripts/hosted_smoke_test.py#L30) | 30 | `"        self.report = report or {}"` | — |
| [SRC-A8360B1B03-L000031](../../scripts/hosted_smoke_test.py#L31) | 31 | `""` | — |
| [SRC-A8360B1B03-L000032](../../scripts/hosted_smoke_test.py#L32) | 32 | `""` | — |
| [SRC-A8360B1B03-L000033](../../scripts/hosted_smoke_test.py#L33) | 33 | `"class _SameOriginRedirectHandler(urllib.request.HTTPRedirectHandler):"` | — |
| [SRC-A8360B1B03-L000034](../../scripts/hosted_smoke_test.py#L34) | 34 | `"    \"\"\"Never forward a bearer token to a different origin during an HTTP redirect.\"\"\""` | — |
| [SRC-A8360B1B03-L000035](../../scripts/hosted_smoke_test.py#L35) | 35 | `""` | — |
| [SRC-A8360B1B03-L000036](../../scripts/hosted_smoke_test.py#L36) | 36 | `"    @staticmethod"` | — |
| [SRC-A8360B1B03-L000037](../../scripts/hosted_smoke_test.py#L37) | 37 | `"    def _origin(url: str) -> tuple[str, str, int \| None]:"` | — |
| [SRC-A8360B1B03-L000038](../../scripts/hosted_smoke_test.py#L38) | 38 | `"        parsed = urllib.parse.urlsplit(url)"` | — |
| [SRC-A8360B1B03-L000039](../../scripts/hosted_smoke_test.py#L39) | 39 | `"        try:"` | — |
| [SRC-A8360B1B03-L000040](../../scripts/hosted_smoke_test.py#L40) | 40 | `"            port = parsed.port"` | — |
| [SRC-A8360B1B03-L000041](../../scripts/hosted_smoke_test.py#L41) | 41 | `"        except ValueError:"` | — |
| [SRC-A8360B1B03-L000042](../../scripts/hosted_smoke_test.py#L42) | 42 | `"            return \"\", \"\", None"` | — |
| [SRC-A8360B1B03-L000043](../../scripts/hosted_smoke_test.py#L43) | 43 | `"        if port is None:"` | — |
| [SRC-A8360B1B03-L000044](../../scripts/hosted_smoke_test.py#L44) | 44 | `"            port = 443 if parsed.scheme.lower() == \"https\" else 80 if parsed.scheme.lower() == \"http\" else None"` | — |
| [SRC-A8360B1B03-L000045](../../scripts/hosted_smoke_test.py#L45) | 45 | `"        return parsed.scheme.lower(), (parsed.hostname or \"\").lower(), port"` | — |
| [SRC-A8360B1B03-L000046](../../scripts/hosted_smoke_test.py#L46) | 46 | `""` | — |
| [SRC-A8360B1B03-L000047](../../scripts/hosted_smoke_test.py#L47) | 47 | `"    def redirect_request(self, req, fp, code, msg, headers, newurl):"` | — |
| [SRC-A8360B1B03-L000048](../../scripts/hosted_smoke_test.py#L48) | 48 | `"        target_url = urllib.parse.urljoin(req.full_url, newurl)"` | — |
| [SRC-A8360B1B03-L000049](../../scripts/hosted_smoke_test.py#L49) | 49 | `"        target = urllib.parse.urlsplit(target_url)"` | — |
| [SRC-A8360B1B03-L000050](../../scripts/hosted_smoke_test.py#L50) | 50 | `"        if ("` | — |
| [SRC-A8360B1B03-L000051](../../scripts/hosted_smoke_test.py#L51) | 51 | `"            self._origin(req.full_url) != self._origin(target_url)"` | — |
| [SRC-A8360B1B03-L000052](../../scripts/hosted_smoke_test.py#L52) | 52 | `"            or target.scheme.lower() not in {\"http\", \"https\"}"` | — |
| [SRC-A8360B1B03-L000053](../../scripts/hosted_smoke_test.py#L53) | 53 | `"            or target.username"` | — |
| [SRC-A8360B1B03-L000054](../../scripts/hosted_smoke_test.py#L54) | 54 | `"            or target.password"` | — |
| [SRC-A8360B1B03-L000055](../../scripts/hosted_smoke_test.py#L55) | 55 | `"        ):"` | — |
| [SRC-A8360B1B03-L000056](../../scripts/hosted_smoke_test.py#L56) | 56 | `"            raise urllib.error.HTTPError("` | — |
| [SRC-A8360B1B03-L000057](../../scripts/hosted_smoke_test.py#L57) | 57 | `"                req.full_url, code, \"Cross-origin redirect blocked\", headers, fp"` | — |
| [SRC-A8360B1B03-L000058](../../scripts/hosted_smoke_test.py#L58) | 58 | `"            )"` | — |
| [SRC-A8360B1B03-L000059](../../scripts/hosted_smoke_test.py#L59) | 59 | `"        return super().redirect_request(req, fp, code, msg, headers, target_url)"` | — |
| [SRC-A8360B1B03-L000060](../../scripts/hosted_smoke_test.py#L60) | 60 | `""` | — |
| [SRC-A8360B1B03-L000061](../../scripts/hosted_smoke_test.py#L61) | 61 | `""` | — |
| [SRC-A8360B1B03-L000062](../../scripts/hosted_smoke_test.py#L62) | 62 | `"def normalize_origin(value: str, allow_http: bool = False) -> str:"` | — |
| [SRC-A8360B1B03-L000063](../../scripts/hosted_smoke_test.py#L63) | 63 | `"    parsed = urllib.parse.urlsplit((value or \"\").strip())"` | — |
| [SRC-A8360B1B03-L000064](../../scripts/hosted_smoke_test.py#L64) | 64 | `"    if parsed.scheme not in {\"https\", \"http\"} or not parsed.hostname:"` | — |
| [SRC-A8360B1B03-L000065](../../scripts/hosted_smoke_test.py#L65) | 65 | `"        raise SmokeError(\"Provide an absolute HTTPS origin, for example https://your-app.example.com.\")"` | — |
| [SRC-A8360B1B03-L000066](../../scripts/hosted_smoke_test.py#L66) | 66 | `"    if parsed.username or parsed.password or parsed.query or parsed.fragment:"` | — |
| [SRC-A8360B1B03-L000067](../../scripts/hosted_smoke_test.py#L67) | 67 | `"        raise SmokeError(\"The base URL must not contain credentials, a query, or a fragment.\")"` | — |
| [SRC-A8360B1B03-L000068](../../scripts/hosted_smoke_test.py#L68) | 68 | `"    if parsed.path not in {\"\", \"/\"}:"` | — |
| [SRC-A8360B1B03-L000069](../../scripts/hosted_smoke_test.py#L69) | 69 | `"        raise SmokeError(\"The base URL must be an origin only; do not add /api or another path.\")"` | — |
| [SRC-A8360B1B03-L000070](../../scripts/hosted_smoke_test.py#L70) | 70 | `"    if parsed.scheme != \"https\" and not ("` | — |
| [SRC-A8360B1B03-L000071](../../scripts/hosted_smoke_test.py#L71) | 71 | `"        allow_http and parsed.hostname.lower() in {\"localhost\", \"127.0.0.1\", \"::1\"}"` | — |
| [SRC-A8360B1B03-L000072](../../scripts/hosted_smoke_test.py#L72) | 72 | `"    ):"` | — |
| [SRC-A8360B1B03-L000073](../../scripts/hosted_smoke_test.py#L73) | 73 | `"        raise SmokeError(\"Hosted tests require HTTPS; plain HTTP is allowed only for local tests.\")"` | — |
| [SRC-A8360B1B03-L000074](../../scripts/hosted_smoke_test.py#L74) | 74 | `"    try:"` | — |
| [SRC-A8360B1B03-L000075](../../scripts/hosted_smoke_test.py#L75) | 75 | `"        port = parsed.port"` | — |
| [SRC-A8360B1B03-L000076](../../scripts/hosted_smoke_test.py#L76) | 76 | `"    except ValueError as exc:"` | — |
| [SRC-A8360B1B03-L000077](../../scripts/hosted_smoke_test.py#L77) | 77 | `"        raise SmokeError(\"Invalid port in base URL.\") from exc"` | — |
| [SRC-A8360B1B03-L000078](../../scripts/hosted_smoke_test.py#L78) | 78 | `"    host = parsed.hostname"` | — |
| [SRC-A8360B1B03-L000079](../../scripts/hosted_smoke_test.py#L79) | 79 | `"    if \":\" in host and not host.startswith(\"[\"):"` | — |
| [SRC-A8360B1B03-L000080](../../scripts/hosted_smoke_test.py#L80) | 80 | `"        host = f\"[{host}]\""` | — |
| [SRC-A8360B1B03-L000081](../../scripts/hosted_smoke_test.py#L81) | 81 | `"    if port:"` | — |
| [SRC-A8360B1B03-L000082](../../scripts/hosted_smoke_test.py#L82) | 82 | `"        host += f\":{port}\""` | — |
| [SRC-A8360B1B03-L000083](../../scripts/hosted_smoke_test.py#L83) | 83 | `"    return f\"{parsed.scheme}://{host}\""` | — |
| [SRC-A8360B1B03-L000084](../../scripts/hosted_smoke_test.py#L84) | 84 | `""` | — |
| [SRC-A8360B1B03-L000085](../../scripts/hosted_smoke_test.py#L85) | 85 | `""` | — |
| [SRC-A8360B1B03-L000086](../../scripts/hosted_smoke_test.py#L86) | 86 | `"def request_json(url: str, *, token: str = \"\", payload: dict[str, Any] \| None = None,"` | — |
| [SRC-A8360B1B03-L000087](../../scripts/hosted_smoke_test.py#L87) | 87 | `"                 timeout: float = 90) -> tuple[int, dict[str, Any] \| None]:"` | — |
| [SRC-A8360B1B03-L000088](../../scripts/hosted_smoke_test.py#L88) | 88 | `"    headers = {\"Accept\": \"application/json\"}"` | — |
| [SRC-A8360B1B03-L000089](../../scripts/hosted_smoke_test.py#L89) | 89 | `"    data = None"` | — |
| [SRC-A8360B1B03-L000090](../../scripts/hosted_smoke_test.py#L90) | 90 | `"    if payload is not None:"` | — |
| [SRC-A8360B1B03-L000091](../../scripts/hosted_smoke_test.py#L91) | 91 | `"        headers[\"Content-Type\"] = \"application/json\""` | — |
| [SRC-A8360B1B03-L000092](../../scripts/hosted_smoke_test.py#L92) | 92 | `"        data = json.dumps(payload, ensure_ascii=False).encode()"` | — |
| [SRC-A8360B1B03-L000093](../../scripts/hosted_smoke_test.py#L93) | 93 | `"    if token:"` | — |
| [SRC-A8360B1B03-L000094](../../scripts/hosted_smoke_test.py#L94) | 94 | `"        headers[\"Authorization\"] = \"Bearer \" + token"` | — |
| [SRC-A8360B1B03-L000095](../../scripts/hosted_smoke_test.py#L95) | 95 | `"    request = urllib.request.Request(url, data=data, headers=headers)"` | — |
| [SRC-A8360B1B03-L000096](../../scripts/hosted_smoke_test.py#L96) | 96 | `"    try:"` | — |
| [SRC-A8360B1B03-L000097](../../scripts/hosted_smoke_test.py#L97) | 97 | `"        opener = urllib.request.build_opener(_SameOriginRedirectHandler())"` | — |
| [SRC-A8360B1B03-L000098](../../scripts/hosted_smoke_test.py#L98) | 98 | `"        with opener.open(request, timeout=timeout) as response:"` | — |
| [SRC-A8360B1B03-L000099](../../scripts/hosted_smoke_test.py#L99) | 99 | `"            status, body = response.status, response.read(1_000_000)"` | — |
| [SRC-A8360B1B03-L000100](../../scripts/hosted_smoke_test.py#L100) | 100 | `"    except urllib.error.HTTPError as exc:"` | — |
| [SRC-A8360B1B03-L000101](../../scripts/hosted_smoke_test.py#L101) | 101 | `"        status = exc.code"` | — |
| [SRC-A8360B1B03-L000102](../../scripts/hosted_smoke_test.py#L102) | 102 | `"        body = exc.read(100_000)"` | — |
| [SRC-A8360B1B03-L000103](../../scripts/hosted_smoke_test.py#L103) | 103 | `"    except (urllib.error.URLError, TimeoutError, OSError) as exc:"` | — |
| [SRC-A8360B1B03-L000104](../../scripts/hosted_smoke_test.py#L104) | 104 | `"        path = urllib.parse.urlsplit(url).path"` | — |
| [SRC-A8360B1B03-L000105](../../scripts/hosted_smoke_test.py#L105) | 105 | `"        raise SmokeError(f\"Network request failed at {path}; check the service and network.\") from exc"` | — |
| [SRC-A8360B1B03-L000106](../../scripts/hosted_smoke_test.py#L106) | 106 | `"    try:"` | — |
| [SRC-A8360B1B03-L000107](../../scripts/hosted_smoke_test.py#L107) | 107 | `"        result = json.loads(body.decode(\"utf-8\"))"` | — |
| [SRC-A8360B1B03-L000108](../../scripts/hosted_smoke_test.py#L108) | 108 | `"    except (UnicodeDecodeError, json.JSONDecodeError):"` | — |
| [SRC-A8360B1B03-L000109](../../scripts/hosted_smoke_test.py#L109) | 109 | `"        result = None"` | — |
| [SRC-A8360B1B03-L000110](../../scripts/hosted_smoke_test.py#L110) | 110 | `"    return status, result if isinstance(result, dict) else None"` | — |
| [SRC-A8360B1B03-L000111](../../scripts/hosted_smoke_test.py#L111) | 111 | `""` | — |
| [SRC-A8360B1B03-L000112](../../scripts/hosted_smoke_test.py#L112) | 112 | `""` | — |
| [SRC-A8360B1B03-L000113](../../scripts/hosted_smoke_test.py#L113) | 113 | `"def run_smoke("` | — |
| [SRC-A8360B1B03-L000114](../../scripts/hosted_smoke_test.py#L114) | 114 | `"    origin: str,"` | — |
| [SRC-A8360B1B03-L000115](../../scripts/hosted_smoke_test.py#L115) | 115 | `"    token: str,"` | — |
| [SRC-A8360B1B03-L000116](../../scripts/hosted_smoke_test.py#L116) | 116 | `"    *,"` | — |
| [SRC-A8360B1B03-L000117](../../scripts/hosted_smoke_test.py#L117) | 117 | `"    timeout: float = 90,"` | — |
| [SRC-A8360B1B03-L000118](../../scripts/hosted_smoke_test.py#L118) | 118 | `"    allow_http: bool = False,"` | — |
| [SRC-A8360B1B03-L000119](../../scripts/hosted_smoke_test.py#L119) | 119 | `"    expected_sha: str \| None = None,"` | — |
| [SRC-A8360B1B03-L000120](../../scripts/hosted_smoke_test.py#L120) | 120 | `"    local_dev_no_token: bool = False,"` | — |
| [SRC-A8360B1B03-L000121](../../scripts/hosted_smoke_test.py#L121) | 121 | `") -> dict[str, Any]:"` | — |
| [SRC-A8360B1B03-L000122](../../scripts/hosted_smoke_test.py#L122) | 122 | `"    origin = normalize_origin(origin, allow_http or local_dev_no_token)"` | — |
| [SRC-A8360B1B03-L000123](../../scripts/hosted_smoke_test.py#L123) | 123 | `"    target_host = urllib.parse.urlsplit(origin).hostname or \"\""` | — |
| [SRC-A8360B1B03-L000124](../../scripts/hosted_smoke_test.py#L124) | 124 | `"    loopback_host = target_host.lower() in {\"localhost\", \"127.0.0.1\", \"::1\"}"` | — |
| [SRC-A8360B1B03-L000125](../../scripts/hosted_smoke_test.py#L125) | 125 | `"    if expected_sha is not None and not re.fullmatch(r\"[0-9a-fA-F]{40}\", expected_sha.strip()):"` | — |
| [SRC-A8360B1B03-L000126](../../scripts/hosted_smoke_test.py#L126) | 126 | `"        raise SmokeError(\"The expected source revision must be a full 40-character Git SHA.\")"` | — |
| [SRC-A8360B1B03-L000127](../../scripts/hosted_smoke_test.py#L127) | 127 | `"    if token.strip():"` | — |
| [SRC-A8360B1B03-L000128](../../scripts/hosted_smoke_test.py#L128) | 128 | `"        if len(token.strip()) < 32:"` | — |
| [SRC-A8360B1B03-L000129](../../scripts/hosted_smoke_test.py#L129) | 129 | `"            raise SmokeError(\"OMARAI_ACCESS_TOKEN is shorter than 32 characters.\")"` | — |
| [SRC-A8360B1B03-L000130](../../scripts/hosted_smoke_test.py#L130) | 130 | `"    elif not (local_dev_no_token and loopback_host):"` | — |
| [SRC-A8360B1B03-L000131](../../scripts/hosted_smoke_test.py#L131) | 131 | `"        raise SmokeError("` | — |
| [SRC-A8360B1B03-L000132](../../scripts/hosted_smoke_test.py#L132) | 132 | `"            \"OMARAI_ACCESS_TOKEN is required for hosted targets. No-token mode is restricted to localhost/loopback.\""` | — |
| [SRC-A8360B1B03-L000133](../../scripts/hosted_smoke_test.py#L133) | 133 | `"        )"` | — |
| [SRC-A8360B1B03-L000134](../../scripts/hosted_smoke_test.py#L134) | 134 | `""` | — |
| [SRC-A8360B1B03-L000135](../../scripts/hosted_smoke_test.py#L135) | 135 | `"    auth_mode = \"bearer_token\" if token.strip() else \"local_loopback_dev_bypass\""` | — |
| [SRC-A8360B1B03-L000136](../../scripts/hosted_smoke_test.py#L136) | 136 | `"    checks: dict[str, Any] = {}"` | — |
| [SRC-A8360B1B03-L000137](../../scripts/hosted_smoke_test.py#L137) | 137 | `"    partial_report: dict[str, Any] = {"` | — |
| [SRC-A8360B1B03-L000138](../../scripts/hosted_smoke_test.py#L138) | 138 | `"        \"result\": \"running\","` | — |
| [SRC-A8360B1B03-L000139](../../scripts/hosted_smoke_test.py#L139) | 139 | `"        \"target_host\": target_host,"` | — |
| [SRC-A8360B1B03-L000140](../../scripts/hosted_smoke_test.py#L140) | 140 | `"        \"auth_mode\": auth_mode,"` | — |
| [SRC-A8360B1B03-L000141](../../scripts/hosted_smoke_test.py#L141) | 141 | `"        \"checks\": checks,"` | — |
| [SRC-A8360B1B03-L000142](../../scripts/hosted_smoke_test.py#L142) | 142 | `"        \"transcript\": [],"` | — |
| [SRC-A8360B1B03-L000143](../../scripts/hosted_smoke_test.py#L143) | 143 | `"    }"` | — |
| [SRC-A8360B1B03-L000144](../../scripts/hosted_smoke_test.py#L144) | 144 | `"    status, health = request_json(f\"{origin}/api/health\", timeout=min(timeout, 20))"` | — |
| [SRC-A8360B1B03-L000145](../../scripts/hosted_smoke_test.py#L145) | 145 | `"    if status != 200 or not health or health.get(\"ok\") is not True:"` | — |
| [SRC-A8360B1B03-L000146](../../scripts/hosted_smoke_test.py#L146) | 146 | `"        raise SmokeError(f\"Health check failed (HTTP {status}).\", partial_report)"` | — |
| [SRC-A8360B1B03-L000147](../../scripts/hosted_smoke_test.py#L147) | 147 | `"    checks[\"health\"] = \"passed\""` | — |
| [SRC-A8360B1B03-L000148](../../scripts/hosted_smoke_test.py#L148) | 148 | `""` | — |
| [SRC-A8360B1B03-L000149](../../scripts/hosted_smoke_test.py#L149) | 149 | `"    build = health.get(\"build\")"` | — |
| [SRC-A8360B1B03-L000150](../../scripts/hosted_smoke_test.py#L150) | 150 | `"    reported_sha = build.get(\"sha\") if isinstance(build, dict) else None"` | — |
| [SRC-A8360B1B03-L000151](../../scripts/hosted_smoke_test.py#L151) | 151 | `"    if expected_sha is not None:"` | — |
| [SRC-A8360B1B03-L000152](../../scripts/hosted_smoke_test.py#L152) | 152 | `"        expected = expected_sha.strip().lower()"` | — |
| [SRC-A8360B1B03-L000153](../../scripts/hosted_smoke_test.py#L153) | 153 | `"        if not isinstance(reported_sha, str) or reported_sha.lower() != expected:"` | — |
| [SRC-A8360B1B03-L000154](../../scripts/hosted_smoke_test.py#L154) | 154 | `"            raise SmokeError("` | — |
| [SRC-A8360B1B03-L000155](../../scripts/hosted_smoke_test.py#L155) | 155 | `"                \"The deployed service SHA does not match the expected Git commit. \""` | — |
| [SRC-A8360B1B03-L000156](../../scripts/hosted_smoke_test.py#L156) | 156 | `"                \"Pass OMARAI_BUILD_SHA as a Docker build argument for the deployed revision, \""` | — |
| [SRC-A8360B1B03-L000157](../../scripts/hosted_smoke_test.py#L157) | 157 | `"                \"then rebuild and redeploy.\","` | — |
| [SRC-A8360B1B03-L000158](../../scripts/hosted_smoke_test.py#L158) | 158 | `"                partial_report,"` | — |
| [SRC-A8360B1B03-L000159](../../scripts/hosted_smoke_test.py#L159) | 159 | `"            )"` | — |
| [SRC-A8360B1B03-L000160](../../scripts/hosted_smoke_test.py#L160) | 160 | `"        checks[\"build_identity\"] = {"` | — |
| [SRC-A8360B1B03-L000161](../../scripts/hosted_smoke_test.py#L161) | 161 | `"            \"status\": \"passed\","` | — |
| [SRC-A8360B1B03-L000162](../../scripts/hosted_smoke_test.py#L162) | 162 | `"            \"expected_sha\": expected,"` | — |
| [SRC-A8360B1B03-L000163](../../scripts/hosted_smoke_test.py#L163) | 163 | `"            \"reported_sha\": reported_sha.lower(),"` | — |
| [SRC-A8360B1B03-L000164](../../scripts/hosted_smoke_test.py#L164) | 164 | `"        }"` | — |
| [SRC-A8360B1B03-L000165](../../scripts/hosted_smoke_test.py#L165) | 165 | `"    else:"` | — |
| [SRC-A8360B1B03-L000166](../../scripts/hosted_smoke_test.py#L166) | 166 | `"        checks[\"build_identity\"] = {"` | — |
| [SRC-A8360B1B03-L000167](../../scripts/hosted_smoke_test.py#L167) | 167 | `"            \"status\": \"not_checked\","` | — |
| [SRC-A8360B1B03-L000168](../../scripts/hosted_smoke_test.py#L168) | 168 | `"            \"reported_sha\": reported_sha if isinstance(reported_sha, str) else \"unknown\","` | — |
| [SRC-A8360B1B03-L000169](../../scripts/hosted_smoke_test.py#L169) | 169 | `"        }"` | — |
| [SRC-A8360B1B03-L000170](../../scripts/hosted_smoke_test.py#L170) | 170 | `""` | — |
| [SRC-A8360B1B03-L000171](../../scripts/hosted_smoke_test.py#L171) | 171 | `"    if token.strip():"` | — |
| [SRC-A8360B1B03-L000172](../../scripts/hosted_smoke_test.py#L172) | 172 | `"        status, _ = request_json("` | — |
| [SRC-A8360B1B03-L000173](../../scripts/hosted_smoke_test.py#L173) | 173 | `"            f\"{origin}/api/agent\", payload={\"question\": \"اختبار رفض الوصول غير المصرح به\"},"` | — |
| [SRC-A8360B1B03-L000174](../../scripts/hosted_smoke_test.py#L174) | 174 | `"            timeout=min(timeout, 20),"` | — |
| [SRC-A8360B1B03-L000175](../../scripts/hosted_smoke_test.py#L175) | 175 | `"        )"` | — |
| [SRC-A8360B1B03-L000176](../../scripts/hosted_smoke_test.py#L176) | 176 | `"        if status != 401:"` | — |
| [SRC-A8360B1B03-L000177](../../scripts/hosted_smoke_test.py#L177) | 177 | `"            raise SmokeError("` | — |
| [SRC-A8360B1B03-L000178](../../scripts/hosted_smoke_test.py#L178) | 178 | `"                f\"Unauthenticated POST /api/agent should return 401, received {status}.\","` | — |
| [SRC-A8360B1B03-L000179](../../scripts/hosted_smoke_test.py#L179) | 179 | `"                partial_report,"` | — |
| [SRC-A8360B1B03-L000180](../../scripts/hosted_smoke_test.py#L180) | 180 | `"            )"` | — |
| [SRC-A8360B1B03-L000181](../../scripts/hosted_smoke_test.py#L181) | 181 | `"        checks[\"authentication\"] = \"passed\""` | — |
| [SRC-A8360B1B03-L000182](../../scripts/hosted_smoke_test.py#L182) | 182 | `"    else:"` | — |
| [SRC-A8360B1B03-L000183](../../scripts/hosted_smoke_test.py#L183) | 183 | `"        checks[\"authentication\"] = \"local_loopback_dev_bypass\""` | — |
| [SRC-A8360B1B03-L000184](../../scripts/hosted_smoke_test.py#L184) | 184 | `""` | — |
| [SRC-A8360B1B03-L000185](../../scripts/hosted_smoke_test.py#L185) | 185 | `"    # These are real network/provider calls and may incur model/search usage."` | — |
| [SRC-A8360B1B03-L000186](../../scripts/hosted_smoke_test.py#L186) | 186 | `"    status, diagnostics = request_json("` | — |
| [SRC-A8360B1B03-L000187](../../scripts/hosted_smoke_test.py#L187) | 187 | `"        f\"{origin}/api/diagnostics\", token=token,"` | — |
| [SRC-A8360B1B03-L000188](../../scripts/hosted_smoke_test.py#L188) | 188 | `"        payload={\"test_model\": False, \"test_social\": False}, timeout=timeout,"` | — |
| [SRC-A8360B1B03-L000189](../../scripts/hosted_smoke_test.py#L189) | 189 | `"    )"` | — |
| [SRC-A8360B1B03-L000190](../../scripts/hosted_smoke_test.py#L190) | 190 | `"    if status != 200 or not diagnostics:"` | — |
| [SRC-A8360B1B03-L000191](../../scripts/hosted_smoke_test.py#L191) | 191 | `"        raise SmokeError(f\"Authenticated diagnostics failed (HTTP {status}).\", partial_report)"` | — |
| [SRC-A8360B1B03-L000192](../../scripts/hosted_smoke_test.py#L192) | 192 | `"    parts = diagnostics.get(\"checks\", {})"` | — |
| [SRC-A8360B1B03-L000193](../../scripts/hosted_smoke_test.py#L193) | 193 | `"    web = parts.get(\"web_search\", {}) if isinstance(parts, dict) else {}"` | — |
| [SRC-A8360B1B03-L000194](../../scripts/hosted_smoke_test.py#L194) | 194 | `"    if not isinstance(web, dict) or web.get(\"status\") != \"passed\":"` | — |
| [SRC-A8360B1B03-L000195](../../scripts/hosted_smoke_test.py#L195) | 195 | `"        raise SmokeError(\"The real web-search connectivity test did not pass.\", partial_report)"` | — |
| [SRC-A8360B1B03-L000196](../../scripts/hosted_smoke_test.py#L196) | 196 | `"    checks[\"live_search\"] = {"` | — |
| [SRC-A8360B1B03-L000197](../../scripts/hosted_smoke_test.py#L197) | 197 | `"        \"status\": \"passed\", \"result_count\": web.get(\"result_count\", 0),"` | — |
| [SRC-A8360B1B03-L000198](../../scripts/hosted_smoke_test.py#L198) | 198 | `"        \"provider_counts\": web.get(\"provider_counts\", {}),"` | — |
| [SRC-A8360B1B03-L000199](../../scripts/hosted_smoke_test.py#L199) | 199 | `"    }"` | — |
| [SRC-A8360B1B03-L000200](../../scripts/hosted_smoke_test.py#L200) | 200 | `"    status, answer = request_json("` | — |
| [SRC-A8360B1B03-L000201](../../scripts/hosted_smoke_test.py#L201) | 201 | `"        f\"{origin}/api/agent\", token=token, timeout=timeout,"` | — |
| [SRC-A8360B1B03-L000202](../../scripts/hosted_smoke_test.py#L202) | 202 | `"        payload={"` | — |
| [SRC-A8360B1B03-L000203](../../scripts/hosted_smoke_test.py#L203) | 203 | `"            \"question\": LIVE_TEST_QUESTION,"` | — |
| [SRC-A8360B1B03-L000204](../../scripts/hosted_smoke_test.py#L204) | 204 | `"            \"history\": [], \"mode\": \"auto\","` | — |
| [SRC-A8360B1B03-L000205](../../scripts/hosted_smoke_test.py#L205) | 205 | `"        },"` | — |
| [SRC-A8360B1B03-L000206](../../scripts/hosted_smoke_test.py#L206) | 206 | `"    )"` | — |
| [SRC-A8360B1B03-L000207](../../scripts/hosted_smoke_test.py#L207) | 207 | `"    if status != 200 or not answer:"` | — |
| [SRC-A8360B1B03-L000208](../../scripts/hosted_smoke_test.py#L208) | 208 | `"        raise SmokeError(f\"Authenticated agent request failed (HTTP {status}).\", partial_report)"` | — |
| [SRC-A8360B1B03-L000209](../../scripts/hosted_smoke_test.py#L209) | 209 | `"    sources = answer.get(\"sources\")"` | — |
| [SRC-A8360B1B03-L000210](../../scripts/hosted_smoke_test.py#L210) | 210 | `"    usable = ["` | — |
| [SRC-A8360B1B03-L000211](../../scripts/hosted_smoke_test.py#L211) | 211 | `"        item for item in sources if isinstance(item, dict)"` | — |
| [SRC-A8360B1B03-L000212](../../scripts/hosted_smoke_test.py#L212) | 212 | `"        and isinstance(item.get(\"url\"), str)"` | — |
| [SRC-A8360B1B03-L000213](../../scripts/hosted_smoke_test.py#L213) | 213 | `"        and urllib.parse.urlsplit(item[\"url\"]).scheme in {\"http\", \"https\"}"` | — |
| [SRC-A8360B1B03-L000214](../../scripts/hosted_smoke_test.py#L214) | 214 | `"        and urllib.parse.urlsplit(item[\"url\"]).hostname"` | — |
| [SRC-A8360B1B03-L000215](../../scripts/hosted_smoke_test.py#L215) | 215 | `"    ] if isinstance(sources, list) else []"` | — |
| [SRC-A8360B1B03-L000216](../../scripts/hosted_smoke_test.py#L216) | 216 | `"    search_report = answer.get(\"search_report\")"` | — |
| [SRC-A8360B1B03-L000217](../../scripts/hosted_smoke_test.py#L217) | 217 | `"    answer_text = str(answer.get(\"answer\", \"\")).strip()"` | — |
| [SRC-A8360B1B03-L000218](../../scripts/hosted_smoke_test.py#L218) | 218 | `"    source_records = ["` | — |
| [SRC-A8360B1B03-L000219](../../scripts/hosted_smoke_test.py#L219) | 219 | `"        {"` | — |
| [SRC-A8360B1B03-L000220](../../scripts/hosted_smoke_test.py#L220) | 220 | `"            \"title\": str(item.get(\"title\") or \"\")[:300],"` | — |
| [SRC-A8360B1B03-L000221](../../scripts/hosted_smoke_test.py#L221) | 221 | `"            \"url\": str(item.get(\"url\") or \"\")[:2048],"` | — |
| [SRC-A8360B1B03-L000222](../../scripts/hosted_smoke_test.py#L222) | 222 | `"            \"provider\": str(item.get(\"provider\") or \"\")[:80],"` | — |
| [SRC-A8360B1B03-L000223](../../scripts/hosted_smoke_test.py#L223) | 223 | `"            \"snippet\": str(item.get(\"snippet\") or \"\")[:1200],"` | — |
| [SRC-A8360B1B03-L000224](../../scripts/hosted_smoke_test.py#L224) | 224 | `"            \"published_at\": str(item.get(\"published_at\") or \"\")[:100],"` | — |
| [SRC-A8360B1B03-L000225](../../scripts/hosted_smoke_test.py#L225) | 225 | `"        }"` | — |
| [SRC-A8360B1B03-L000226](../../scripts/hosted_smoke_test.py#L226) | 226 | `"        for item in usable"` | — |
| [SRC-A8360B1B03-L000227](../../scripts/hosted_smoke_test.py#L227) | 227 | `"    ]"` | — |
| [SRC-A8360B1B03-L000228](../../scripts/hosted_smoke_test.py#L228) | 228 | `"    transcript = {"` | — |
| [SRC-A8360B1B03-L000229](../../scripts/hosted_smoke_test.py#L229) | 229 | `"        \"case_id\": \"sales_intent_fire_alarm_egypt\","` | — |
| [SRC-A8360B1B03-L000230](../../scripts/hosted_smoke_test.py#L230) | 230 | `"        \"question\": LIVE_TEST_QUESTION,"` | — |
| [SRC-A8360B1B03-L000231](../../scripts/hosted_smoke_test.py#L231) | 231 | `"        \"answer\": answer_text,"` | — |
| [SRC-A8360B1B03-L000232](../../scripts/hosted_smoke_test.py#L232) | 232 | `"        \"used_web_search\": answer.get(\"used_web_search\") is True,"` | — |
| [SRC-A8360B1B03-L000233](../../scripts/hosted_smoke_test.py#L233) | 233 | `"        \"used_language_model\": answer.get(\"used_language_model\") is True,"` | — |
| [SRC-A8360B1B03-L000234](../../scripts/hosted_smoke_test.py#L234) | 234 | `"        \"sources\": source_records,"` | — |
| [SRC-A8360B1B03-L000235](../../scripts/hosted_smoke_test.py#L235) | 235 | `"        \"pipeline_completion_status\": ("` | — |
| [SRC-A8360B1B03-L000236](../../scripts/hosted_smoke_test.py#L236) | 236 | `"            search_report.get(\"pipeline_completion_status\")"` | — |
| [SRC-A8360B1B03-L000237](../../scripts/hosted_smoke_test.py#L237) | 237 | `"            if isinstance(search_report, dict) else None"` | — |
| [SRC-A8360B1B03-L000238](../../scripts/hosted_smoke_test.py#L238) | 238 | `"        ),"` | — |
| [SRC-A8360B1B03-L000239](../../scripts/hosted_smoke_test.py#L239) | 239 | `"        \"answer_evidence_status\": answer.get(\"answer_evidence_status\"),"` | — |
| [SRC-A8360B1B03-L000240](../../scripts/hosted_smoke_test.py#L240) | 240 | `"    }"` | — |
| [SRC-A8360B1B03-L000241](../../scripts/hosted_smoke_test.py#L241) | 241 | `"    partial_report[\"transcript\"] = [transcript]"` | — |
| [SRC-A8360B1B03-L000242](../../scripts/hosted_smoke_test.py#L242) | 242 | `"    if answer.get(\"used_web_search\") is not True or not usable:"` | — |
| [SRC-A8360B1B03-L000243](../../scripts/hosted_smoke_test.py#L243) | 243 | `"        raise SmokeError("` | — |
| [SRC-A8360B1B03-L000244](../../scripts/hosted_smoke_test.py#L244) | 244 | `"            \"Agent request did not return a live web search with usable source URLs.\","` | — |
| [SRC-A8360B1B03-L000245](../../scripts/hosted_smoke_test.py#L245) | 245 | `"            partial_report,"` | — |
| [SRC-A8360B1B03-L000246](../../scripts/hosted_smoke_test.py#L246) | 246 | `"        )"` | — |
| [SRC-A8360B1B03-L000247](../../scripts/hosted_smoke_test.py#L247) | 247 | `"    if answer.get(\"used_language_model\") is not True:"` | — |
| [SRC-A8360B1B03-L000248](../../scripts/hosted_smoke_test.py#L248) | 248 | `"        raise SmokeError("` | — |
| [SRC-A8360B1B03-L000249](../../scripts/hosted_smoke_test.py#L249) | 249 | `"            \"Agent request did not confirm that a language model was used.\","` | — |
| [SRC-A8360B1B03-L000250](../../scripts/hosted_smoke_test.py#L250) | 250 | `"            partial_report,"` | — |
| [SRC-A8360B1B03-L000251](../../scripts/hosted_smoke_test.py#L251) | 251 | `"        )"` | — |
| [SRC-A8360B1B03-L000252](../../scripts/hosted_smoke_test.py#L252) | 252 | `"    checks[\"language_model\"] = {"` | — |
| [SRC-A8360B1B03-L000253](../../scripts/hosted_smoke_test.py#L253) | 253 | `"        \"status\": \"passed\","` | — |
| [SRC-A8360B1B03-L000254](../../scripts/hosted_smoke_test.py#L254) | 254 | `"        \"response_received\": bool(answer_text),"` | — |
| [SRC-A8360B1B03-L000255](../../scripts/hosted_smoke_test.py#L255) | 255 | `"        \"verified_by\": \"agent_request\","` | — |
| [SRC-A8360B1B03-L000256](../../scripts/hosted_smoke_test.py#L256) | 256 | `"    }"` | — |
| [SRC-A8360B1B03-L000257](../../scripts/hosted_smoke_test.py#L257) | 257 | `"    checks[\"agent_request\"] = {"` | — |
| [SRC-A8360B1B03-L000258](../../scripts/hosted_smoke_test.py#L258) | 258 | `"        \"status\": \"passed\", \"source_count\": len(usable),"` | — |
| [SRC-A8360B1B03-L000259](../../scripts/hosted_smoke_test.py#L259) | 259 | `"        \"direct_pages_read\": search_report.get(\"pages_fetched\") if isinstance(search_report, dict) else None,"` | — |
| [SRC-A8360B1B03-L000260](../../scripts/hosted_smoke_test.py#L260) | 260 | `"        \"providers_reported\": search_report.get(\"providers_used\", []) if isinstance(search_report, dict) else [],"` | — |
| [SRC-A8360B1B03-L000261](../../scripts/hosted_smoke_test.py#L261) | 261 | `"        \"answer_received\": bool(answer_text),"` | — |
| [SRC-A8360B1B03-L000262](../../scripts/hosted_smoke_test.py#L262) | 262 | `"        \"pipeline_completion_status\": ("` | — |
| [SRC-A8360B1B03-L000263](../../scripts/hosted_smoke_test.py#L263) | 263 | `"            search_report.get(\"pipeline_completion_status\") if isinstance(search_report, dict) else None"` | — |
| [SRC-A8360B1B03-L000264](../../scripts/hosted_smoke_test.py#L264) | 264 | `"        ),"` | — |
| [SRC-A8360B1B03-L000265](../../scripts/hosted_smoke_test.py#L265) | 265 | `"        \"answer_evidence_status\": answer.get(\"answer_evidence_status\"),"` | — |
| [SRC-A8360B1B03-L000266](../../scripts/hosted_smoke_test.py#L266) | 266 | `"    }"` | — |
| [SRC-A8360B1B03-L000267](../../scripts/hosted_smoke_test.py#L267) | 267 | `"    partial_report.update({"` | — |
| [SRC-A8360B1B03-L000268](../../scripts/hosted_smoke_test.py#L268) | 268 | `"        \"result\": \"passed\","` | — |
| [SRC-A8360B1B03-L000269](../../scripts/hosted_smoke_test.py#L269) | 269 | `"        \"checks\": checks,"` | — |
| [SRC-A8360B1B03-L000270](../../scripts/hosted_smoke_test.py#L270) | 270 | `"        \"provider_diagnostics\": diagnostics.get(\"provider_diagnostics\", []),"` | — |
| [SRC-A8360B1B03-L000271](../../scripts/hosted_smoke_test.py#L271) | 271 | `"        \"diagnostic_warnings\": diagnostics.get(\"warnings\", []),"` | — |
| [SRC-A8360B1B03-L000272](../../scripts/hosted_smoke_test.py#L272) | 272 | `"        \"note\": \"Transcript contains the exact fixed test question, answer, and returned source metadata. This proves the request path worked at test time, not continuous uptime. One model completion is made by the agent request; provider usage may incur charges.\","` | — |
| [SRC-A8360B1B03-L000273](../../scripts/hosted_smoke_test.py#L273) | 273 | `"    })"` | — |
| [SRC-A8360B1B03-L000274](../../scripts/hosted_smoke_test.py#L274) | 274 | `"    return partial_report"` | — |
| [SRC-A8360B1B03-L000275](../../scripts/hosted_smoke_test.py#L275) | 275 | `""` | — |
| [SRC-A8360B1B03-L000276](../../scripts/hosted_smoke_test.py#L276) | 276 | `""` | — |
| [SRC-A8360B1B03-L000277](../../scripts/hosted_smoke_test.py#L277) | 277 | `"def main() -> int:"` | — |
| [SRC-A8360B1B03-L000278](../../scripts/hosted_smoke_test.py#L278) | 278 | `"    parser = argparse.ArgumentParser(description=\"Run live acceptance checks against hosted Omarai.\")"` | — |
| [SRC-A8360B1B03-L000279](../../scripts/hosted_smoke_test.py#L279) | 279 | `"    parser.add_argument(\"--base-url\", default=os.getenv(\"OMARAI_BASE_URL\", \"\"))"` | — |
| [SRC-A8360B1B03-L000280](../../scripts/hosted_smoke_test.py#L280) | 280 | `"    parser.add_argument(\"--timeout\", type=float, default=90)"` | — |
| [SRC-A8360B1B03-L000281](../../scripts/hosted_smoke_test.py#L281) | 281 | `"    parser.add_argument("` | — |
| [SRC-A8360B1B03-L000282](../../scripts/hosted_smoke_test.py#L282) | 282 | `"        \"--expected-sha\","` | — |
| [SRC-A8360B1B03-L000283](../../scripts/hosted_smoke_test.py#L283) | 283 | `"        default=os.getenv(\"OMARAI_EXPECTED_BUILD_SHA\", \"\"),"` | — |
| [SRC-A8360B1B03-L000284](../../scripts/hosted_smoke_test.py#L284) | 284 | `"        help=\"Require the deployed image to report this full 40-character source Git SHA.\","` | — |
| [SRC-A8360B1B03-L000285](../../scripts/hosted_smoke_test.py#L285) | 285 | `"    )"` | — |
| [SRC-A8360B1B03-L000286](../../scripts/hosted_smoke_test.py#L286) | 286 | `"    parser.add_argument(\"--allow-http\", action=\"store_true\","` | — |
| [SRC-A8360B1B03-L000287](../../scripts/hosted_smoke_test.py#L287) | 287 | `"                        help=\"Allow HTTP only for localhost/127.0.0.1/::1 testing.\")"` | — |
| [SRC-A8360B1B03-L000288](../../scripts/hosted_smoke_test.py#L288) | 288 | `"    parser.add_argument("` | — |
| [SRC-A8360B1B03-L000289](../../scripts/hosted_smoke_test.py#L289) | 289 | `"        \"--local-dev-no-token\","` | — |
