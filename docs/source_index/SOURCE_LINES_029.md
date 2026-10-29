# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **029**
- سجلات الأسطر: **800**
- النطاق: SRC-4FFD5AFC54-L000075 إلى SRC-03FF422A16-L000180
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## ملفات أخرى

### FILE-4FFD5AFC54 — [scripts/run_answer_quality_benchmark.py](../../scripts/run_answer_quality_benchmark.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-4FFD5AFC54-L000075](../../scripts/run_answer_quality_benchmark.py#L75) | 75 | `"def _model_calls_from_payload(payload: dict) -> list[dict]:"` | — |
| [SRC-4FFD5AFC54-L000076](../../scripts/run_answer_quality_benchmark.py#L76) | 76 | `"    \"\"\"Read only structured per-request model-call metadata from an API response.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000077](../../scripts/run_answer_quality_benchmark.py#L77) | 77 | `"    report = payload.get(\"search_report\")"` | — |
| [SRC-4FFD5AFC54-L000078](../../scripts/run_answer_quality_benchmark.py#L78) | 78 | `"    understanding = payload.get(\"task_understanding\")"` | — |
| [SRC-4FFD5AFC54-L000079](../../scripts/run_answer_quality_benchmark.py#L79) | 79 | `"    candidates = ["` | — |
| [SRC-4FFD5AFC54-L000080](../../scripts/run_answer_quality_benchmark.py#L80) | 80 | `"        payload.get(\"model_calls\"),"` | — |
| [SRC-4FFD5AFC54-L000081](../../scripts/run_answer_quality_benchmark.py#L81) | 81 | `"        report.get(\"model_calls\") if isinstance(report, dict) else None,"` | — |
| [SRC-4FFD5AFC54-L000082](../../scripts/run_answer_quality_benchmark.py#L82) | 82 | `"        understanding.get(\"model_calls\") if isinstance(understanding, dict) else None,"` | — |
| [SRC-4FFD5AFC54-L000083](../../scripts/run_answer_quality_benchmark.py#L83) | 83 | `"    ]"` | — |
| [SRC-4FFD5AFC54-L000084](../../scripts/run_answer_quality_benchmark.py#L84) | 84 | `"    for candidate in candidates:"` | — |
| [SRC-4FFD5AFC54-L000085](../../scripts/run_answer_quality_benchmark.py#L85) | 85 | `"        if isinstance(candidate, list) and candidate:"` | — |
| [SRC-4FFD5AFC54-L000086](../../scripts/run_answer_quality_benchmark.py#L86) | 86 | `"            return [item for item in candidate if isinstance(item, dict)]"` | — |
| [SRC-4FFD5AFC54-L000087](../../scripts/run_answer_quality_benchmark.py#L87) | 87 | `"    return []"` | — |
| [SRC-4FFD5AFC54-L000088](../../scripts/run_answer_quality_benchmark.py#L88) | 88 | `""` | — |
| [SRC-4FFD5AFC54-L000089](../../scripts/run_answer_quality_benchmark.py#L89) | 89 | `""` | — |
| [SRC-4FFD5AFC54-L000090](../../scripts/run_answer_quality_benchmark.py#L90) | 90 | `"def _finite_nonnegative_number(value) -> float \| None:"` | — |
| [SRC-4FFD5AFC54-L000091](../../scripts/run_answer_quality_benchmark.py#L91) | 91 | `"    if isinstance(value, bool) or not isinstance(value, (int, float)):"` | — |
| [SRC-4FFD5AFC54-L000092](../../scripts/run_answer_quality_benchmark.py#L92) | 92 | `"        return None"` | — |
| [SRC-4FFD5AFC54-L000093](../../scripts/run_answer_quality_benchmark.py#L93) | 93 | `"    number = float(value)"` | — |
| [SRC-4FFD5AFC54-L000094](../../scripts/run_answer_quality_benchmark.py#L94) | 94 | `"    if not math.isfinite(number) or number < 0:"` | — |
| [SRC-4FFD5AFC54-L000095](../../scripts/run_answer_quality_benchmark.py#L95) | 95 | `"        return None"` | — |
| [SRC-4FFD5AFC54-L000096](../../scripts/run_answer_quality_benchmark.py#L96) | 96 | `"    return number"` | — |
| [SRC-4FFD5AFC54-L000097](../../scripts/run_answer_quality_benchmark.py#L97) | 97 | `""` | — |
| [SRC-4FFD5AFC54-L000098](../../scripts/run_answer_quality_benchmark.py#L98) | 98 | `""` | — |
| [SRC-4FFD5AFC54-L000099](../../scripts/run_answer_quality_benchmark.py#L99) | 99 | `"def _response_metrics(payload: dict \| str, expected_strategy: str, transport_ok: bool) -> dict:"` | — |
| [SRC-4FFD5AFC54-L000100](../../scripts/run_answer_quality_benchmark.py#L100) | 100 | `"    \"\"\"Derive conservative telemetry; never infer semantic correctness from HTTP 200.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000101](../../scripts/run_answer_quality_benchmark.py#L101) | 101 | `"    if not isinstance(payload, dict):"` | — |
| [SRC-4FFD5AFC54-L000102](../../scripts/run_answer_quality_benchmark.py#L102) | 102 | `"        payload = {}"` | — |
| [SRC-4FFD5AFC54-L000103](../../scripts/run_answer_quality_benchmark.py#L103) | 103 | `"    report = payload.get(\"search_report\")"` | — |
| [SRC-4FFD5AFC54-L000104](../../scripts/run_answer_quality_benchmark.py#L104) | 104 | `"    report = report if isinstance(report, dict) else {}"` | — |
| [SRC-4FFD5AFC54-L000105](../../scripts/run_answer_quality_benchmark.py#L105) | 105 | `"    outcome = report.get(\"search_outcome\")"` | — |
| [SRC-4FFD5AFC54-L000106](../../scripts/run_answer_quality_benchmark.py#L106) | 106 | `"    pipeline = report.get(\"pipeline_completion_status\")"` | — |
| [SRC-4FFD5AFC54-L000107](../../scripts/run_answer_quality_benchmark.py#L107) | 107 | `"    source_rows = payload.get(\"sources\")"` | — |
| [SRC-4FFD5AFC54-L000108](../../scripts/run_answer_quality_benchmark.py#L108) | 108 | `"    source_rows_known = isinstance(source_rows, list)"` | — |
| [SRC-4FFD5AFC54-L000109](../../scripts/run_answer_quality_benchmark.py#L109) | 109 | `"    source_count = len(source_rows) if source_rows_known else None"` | — |
| [SRC-4FFD5AFC54-L000110](../../scripts/run_answer_quality_benchmark.py#L110) | 110 | `"    if expected_strategy != \"web_search\":"` | — |
| [SRC-4FFD5AFC54-L000111](../../scripts/run_answer_quality_benchmark.py#L111) | 111 | `"        tool_status = \"NOT_APPLICABLE\""` | — |
| [SRC-4FFD5AFC54-L000112](../../scripts/run_answer_quality_benchmark.py#L112) | 112 | `"    elif not transport_ok:"` | — |
| [SRC-4FFD5AFC54-L000113](../../scripts/run_answer_quality_benchmark.py#L113) | 113 | `"        tool_status = \"TRANSPORT_FAILED\""` | — |
| [SRC-4FFD5AFC54-L000114](../../scripts/run_answer_quality_benchmark.py#L114) | 114 | `"    elif outcome == \"attempted_with_usable_sources\":"` | — |
| [SRC-4FFD5AFC54-L000115](../../scripts/run_answer_quality_benchmark.py#L115) | 115 | `"        if source_count is None:"` | — |
| [SRC-4FFD5AFC54-L000116](../../scripts/run_answer_quality_benchmark.py#L116) | 116 | `"            tool_status = \"UNKNOWN_SOURCE_COUNT\""` | — |
| [SRC-4FFD5AFC54-L000117](../../scripts/run_answer_quality_benchmark.py#L117) | 117 | `"        elif source_count == 0:"` | — |
| [SRC-4FFD5AFC54-L000118](../../scripts/run_answer_quality_benchmark.py#L118) | 118 | `"            tool_status = \"INCONSISTENT_SEARCH_OUTCOME_NO_RETURNED_SOURCES\""` | — |
| [SRC-4FFD5AFC54-L000119](../../scripts/run_answer_quality_benchmark.py#L119) | 119 | `"        else:"` | — |
| [SRC-4FFD5AFC54-L000120](../../scripts/run_answer_quality_benchmark.py#L120) | 120 | `"            tool_status = \"SUCCESS_WITH_USABLE_RESULTS\""` | — |
| [SRC-4FFD5AFC54-L000121](../../scripts/run_answer_quality_benchmark.py#L121) | 121 | `"    elif outcome == \"attempted_no_usable_sources\":"` | — |
| [SRC-4FFD5AFC54-L000122](../../scripts/run_answer_quality_benchmark.py#L122) | 122 | `"        if source_count is not None and source_count > 0:"` | — |
| [SRC-4FFD5AFC54-L000123](../../scripts/run_answer_quality_benchmark.py#L123) | 123 | `"            tool_status = \"INCONSISTENT_SEARCH_OUTCOME_WITH_RETURNED_SOURCES\""` | — |
| [SRC-4FFD5AFC54-L000124](../../scripts/run_answer_quality_benchmark.py#L124) | 124 | `"        else:"` | — |
| [SRC-4FFD5AFC54-L000125](../../scripts/run_answer_quality_benchmark.py#L125) | 125 | `"            tool_status = \"ATTEMPTED_NO_USABLE_RESULTS\""` | — |
| [SRC-4FFD5AFC54-L000126](../../scripts/run_answer_quality_benchmark.py#L126) | 126 | `"    elif outcome == \"attempted_research_error\":"` | — |
| [SRC-4FFD5AFC54-L000127](../../scripts/run_answer_quality_benchmark.py#L127) | 127 | `"        tool_status = \"TOOL_FAILED\""` | — |
| [SRC-4FFD5AFC54-L000128](../../scripts/run_answer_quality_benchmark.py#L128) | 128 | `"    elif outcome == \"unknown_after_budget_exhaustion\":"` | — |
| [SRC-4FFD5AFC54-L000129](../../scripts/run_answer_quality_benchmark.py#L129) | 129 | `"        tool_status = \"BUDGET_EXHAUSTED\""` | — |
| [SRC-4FFD5AFC54-L000130](../../scripts/run_answer_quality_benchmark.py#L130) | 130 | `"    elif outcome == \"not_attempted\":"` | — |
| [SRC-4FFD5AFC54-L000131](../../scripts/run_answer_quality_benchmark.py#L131) | 131 | `"        tool_status = \"NOT_ATTEMPTED\""` | — |
| [SRC-4FFD5AFC54-L000132](../../scripts/run_answer_quality_benchmark.py#L132) | 132 | `"    else:"` | — |
| [SRC-4FFD5AFC54-L000133](../../scripts/run_answer_quality_benchmark.py#L133) | 133 | `"        tool_status = \"UNKNOWN\""` | — |
| [SRC-4FFD5AFC54-L000134](../../scripts/run_answer_quality_benchmark.py#L134) | 134 | `""` | — |
| [SRC-4FFD5AFC54-L000135](../../scripts/run_answer_quality_benchmark.py#L135) | 135 | `"    task_understanding = payload.get(\"task_understanding\")"` | — |
| [SRC-4FFD5AFC54-L000136](../../scripts/run_answer_quality_benchmark.py#L136) | 136 | `"    task_understanding = task_understanding if isinstance(task_understanding, dict) else {}"` | — |
| [SRC-4FFD5AFC54-L000137](../../scripts/run_answer_quality_benchmark.py#L137) | 137 | `"    tool_execution = task_understanding.get(\"tool_execution\")"` | — |
| [SRC-4FFD5AFC54-L000138](../../scripts/run_answer_quality_benchmark.py#L138) | 138 | `"    tool_execution = tool_execution if isinstance(tool_execution, dict) else {}"` | — |
| [SRC-4FFD5AFC54-L000139](../../scripts/run_answer_quality_benchmark.py#L139) | 139 | `"    raw_tool_rows = tool_execution.get(\"tool_status_matrix\")"` | — |
| [SRC-4FFD5AFC54-L000140](../../scripts/run_answer_quality_benchmark.py#L140) | 140 | `"    requirements_raw = tool_execution.get(\"required_tools\")"` | — |
| [SRC-4FFD5AFC54-L000141](../../scripts/run_answer_quality_benchmark.py#L141) | 141 | `"    required_tool_matrix_present = ("` | — |
| [SRC-4FFD5AFC54-L000142](../../scripts/run_answer_quality_benchmark.py#L142) | 142 | `"        isinstance(raw_tool_rows, list) and isinstance(requirements_raw, list)"` | — |
| [SRC-4FFD5AFC54-L000143](../../scripts/run_answer_quality_benchmark.py#L143) | 143 | `"    )"` | — |
| [SRC-4FFD5AFC54-L000144](../../scripts/run_answer_quality_benchmark.py#L144) | 144 | `"    matrix_rows = [row for row in raw_tool_rows if isinstance(row, dict)] if isinstance(raw_tool_rows, list) else []"` | — |
| [SRC-4FFD5AFC54-L000145](../../scripts/run_answer_quality_benchmark.py#L145) | 145 | `"    required_tool_names = ["` | — |
| [SRC-4FFD5AFC54-L000146](../../scripts/run_answer_quality_benchmark.py#L146) | 146 | `"        name.strip()"` | — |
| [SRC-4FFD5AFC54-L000147](../../scripts/run_answer_quality_benchmark.py#L147) | 147 | `"        for name in requirements_raw"` | — |
| [SRC-4FFD5AFC54-L000148](../../scripts/run_answer_quality_benchmark.py#L148) | 148 | `"        if isinstance(name, str) and name.strip()"` | — |
| [SRC-4FFD5AFC54-L000149](../../scripts/run_answer_quality_benchmark.py#L149) | 149 | `"    ] if isinstance(requirements_raw, list) else []"` | — |
| [SRC-4FFD5AFC54-L000150](../../scripts/run_answer_quality_benchmark.py#L150) | 150 | `"    successful_statuses = {"` | — |
| [SRC-4FFD5AFC54-L000151](../../scripts/run_answer_quality_benchmark.py#L151) | 151 | `"        \"web_search\": {\"completed_with_results\"},"` | — |
| [SRC-4FFD5AFC54-L000152](../../scripts/run_answer_quality_benchmark.py#L152) | 152 | `"        \"page_fetch\": {\"completed_with_read_pages\"},"` | — |
| [SRC-4FFD5AFC54-L000153](../../scripts/run_answer_quality_benchmark.py#L153) | 153 | `"        \"public_social_search_if_configured\": {\"completed_with_results\"},"` | — |
| [SRC-4FFD5AFC54-L000154](../../scripts/run_answer_quality_benchmark.py#L154) | 154 | `"        \"language_model_generation_if_configured\": {\"completed\"},"` | — |
| [SRC-4FFD5AFC54-L000155](../../scripts/run_answer_quality_benchmark.py#L155) | 155 | `"        \"claim_review_if_configured\": {\"completed_model_assisted_review\"},"` | — |
| [SRC-4FFD5AFC54-L000156](../../scripts/run_answer_quality_benchmark.py#L156) | 156 | `"    }"` | — |
| [SRC-4FFD5AFC54-L000157](../../scripts/run_answer_quality_benchmark.py#L157) | 157 | `"    required_tool_statuses = []"` | — |
| [SRC-4FFD5AFC54-L000158](../../scripts/run_answer_quality_benchmark.py#L158) | 158 | `"    required_name_set = set(required_tool_names)"` | — |
| [SRC-4FFD5AFC54-L000159](../../scripts/run_answer_quality_benchmark.py#L159) | 159 | `"    reported_required_names = {"` | — |
| [SRC-4FFD5AFC54-L000160](../../scripts/run_answer_quality_benchmark.py#L160) | 160 | `"        row.get(\"tool\")"` | — |
| [SRC-4FFD5AFC54-L000161](../../scripts/run_answer_quality_benchmark.py#L161) | 161 | `"        for row in matrix_rows"` | — |
| [SRC-4FFD5AFC54-L000162](../../scripts/run_answer_quality_benchmark.py#L162) | 162 | `"        if row.get(\"required_by_task_spec\") is True and isinstance(row.get(\"tool\"), str)"` | — |
| [SRC-4FFD5AFC54-L000163](../../scripts/run_answer_quality_benchmark.py#L163) | 163 | `"    }"` | — |
| [SRC-4FFD5AFC54-L000164](../../scripts/run_answer_quality_benchmark.py#L164) | 164 | `"    required_tool_matrix_complete = ("` | — |
| [SRC-4FFD5AFC54-L000165](../../scripts/run_answer_quality_benchmark.py#L165) | 165 | `"        required_tool_matrix_present"` | — |
| [SRC-4FFD5AFC54-L000166](../../scripts/run_answer_quality_benchmark.py#L166) | 166 | `"        and len(required_tool_names) == len(required_name_set)"` | — |
| [SRC-4FFD5AFC54-L000167](../../scripts/run_answer_quality_benchmark.py#L167) | 167 | `"        and reported_required_names == required_name_set"` | — |
| [SRC-4FFD5AFC54-L000168](../../scripts/run_answer_quality_benchmark.py#L168) | 168 | `"    )"` | — |
| [SRC-4FFD5AFC54-L000169](../../scripts/run_answer_quality_benchmark.py#L169) | 169 | `"    for tool in dict.fromkeys(required_tool_names):"` | — |
| [SRC-4FFD5AFC54-L000170](../../scripts/run_answer_quality_benchmark.py#L170) | 170 | `"        matches = ["` | — |
| [SRC-4FFD5AFC54-L000171](../../scripts/run_answer_quality_benchmark.py#L171) | 171 | `"            row for row in matrix_rows"` | — |
| [SRC-4FFD5AFC54-L000172](../../scripts/run_answer_quality_benchmark.py#L172) | 172 | `"            if row.get(\"tool\") == tool and row.get(\"required_by_task_spec\") is True"` | — |
| [SRC-4FFD5AFC54-L000173](../../scripts/run_answer_quality_benchmark.py#L173) | 173 | `"        ]"` | — |
| [SRC-4FFD5AFC54-L000174](../../scripts/run_answer_quality_benchmark.py#L174) | 174 | `"        if len(matches) == 0:"` | — |
| [SRC-4FFD5AFC54-L000175](../../scripts/run_answer_quality_benchmark.py#L175) | 175 | `"            status = \"missing_matrix_row\""` | — |
| [SRC-4FFD5AFC54-L000176](../../scripts/run_answer_quality_benchmark.py#L176) | 176 | `"            status_observed = False"` | — |
| [SRC-4FFD5AFC54-L000177](../../scripts/run_answer_quality_benchmark.py#L177) | 177 | `"            successful = False"` | — |
| [SRC-4FFD5AFC54-L000178](../../scripts/run_answer_quality_benchmark.py#L178) | 178 | `"            required_tool_matrix_complete = False"` | — |
| [SRC-4FFD5AFC54-L000179](../../scripts/run_answer_quality_benchmark.py#L179) | 179 | `"        elif len(matches) > 1:"` | — |
| [SRC-4FFD5AFC54-L000180](../../scripts/run_answer_quality_benchmark.py#L180) | 180 | `"            status = \"duplicate_matrix_rows\""` | — |
| [SRC-4FFD5AFC54-L000181](../../scripts/run_answer_quality_benchmark.py#L181) | 181 | `"            status_observed = False"` | — |
| [SRC-4FFD5AFC54-L000182](../../scripts/run_answer_quality_benchmark.py#L182) | 182 | `"            successful = False"` | — |
| [SRC-4FFD5AFC54-L000183](../../scripts/run_answer_quality_benchmark.py#L183) | 183 | `"            required_tool_matrix_complete = False"` | — |
| [SRC-4FFD5AFC54-L000184](../../scripts/run_answer_quality_benchmark.py#L184) | 184 | `"        else:"` | — |
| [SRC-4FFD5AFC54-L000185](../../scripts/run_answer_quality_benchmark.py#L185) | 185 | `"            raw_status = matches[0].get(\"status\")"` | — |
| [SRC-4FFD5AFC54-L000186](../../scripts/run_answer_quality_benchmark.py#L186) | 186 | `"            status_observed = isinstance(raw_status, str) and bool(raw_status.strip())"` | — |
| [SRC-4FFD5AFC54-L000187](../../scripts/run_answer_quality_benchmark.py#L187) | 187 | `"            status = raw_status if status_observed else \"missing_status\""` | — |
| [SRC-4FFD5AFC54-L000188](../../scripts/run_answer_quality_benchmark.py#L188) | 188 | `"            successful = status_observed and status in successful_statuses.get(tool, set())"` | — |
| [SRC-4FFD5AFC54-L000189](../../scripts/run_answer_quality_benchmark.py#L189) | 189 | `"            if not status_observed:"` | — |
| [SRC-4FFD5AFC54-L000190](../../scripts/run_answer_quality_benchmark.py#L190) | 190 | `"                required_tool_matrix_complete = False"` | — |
| [SRC-4FFD5AFC54-L000191](../../scripts/run_answer_quality_benchmark.py#L191) | 191 | `"        required_tool_statuses.append({"` | — |
| [SRC-4FFD5AFC54-L000192](../../scripts/run_answer_quality_benchmark.py#L192) | 192 | `"            \"tool\": tool,"` | — |
| [SRC-4FFD5AFC54-L000193](../../scripts/run_answer_quality_benchmark.py#L193) | 193 | `"            \"status\": status,"` | — |
| [SRC-4FFD5AFC54-L000194](../../scripts/run_answer_quality_benchmark.py#L194) | 194 | `"            \"status_observed\": status_observed,"` | — |
| [SRC-4FFD5AFC54-L000195](../../scripts/run_answer_quality_benchmark.py#L195) | 195 | `"            \"successful_completion\": successful,"` | — |
| [SRC-4FFD5AFC54-L000196](../../scripts/run_answer_quality_benchmark.py#L196) | 196 | `"        })"` | — |
| [SRC-4FFD5AFC54-L000197](../../scripts/run_answer_quality_benchmark.py#L197) | 197 | `"    if expected_strategy == \"web_search\" and \"web_search\" not in required_name_set:"` | — |
| [SRC-4FFD5AFC54-L000198](../../scripts/run_answer_quality_benchmark.py#L198) | 198 | `"        required_tool_matrix_complete = False"` | — |
| [SRC-4FFD5AFC54-L000199](../../scripts/run_answer_quality_benchmark.py#L199) | 199 | `""` | — |
| [SRC-4FFD5AFC54-L000200](../../scripts/run_answer_quality_benchmark.py#L200) | 200 | `"    calls = _model_calls_from_payload(payload)"` | — |
| [SRC-4FFD5AFC54-L000201](../../scripts/run_answer_quality_benchmark.py#L201) | 201 | `"    reported_costs = []"` | — |
| [SRC-4FFD5AFC54-L000202](../../scripts/run_answer_quality_benchmark.py#L202) | 202 | `"    for call in calls:"` | — |
| [SRC-4FFD5AFC54-L000203](../../scripts/run_answer_quality_benchmark.py#L203) | 203 | `"        usage = call.get(\"provider_usage\")"` | — |
| [SRC-4FFD5AFC54-L000204](../../scripts/run_answer_quality_benchmark.py#L204) | 204 | `"        if not isinstance(usage, dict):"` | — |
| [SRC-4FFD5AFC54-L000205](../../scripts/run_answer_quality_benchmark.py#L205) | 205 | `"            continue"` | — |
| [SRC-4FFD5AFC54-L000206](../../scripts/run_answer_quality_benchmark.py#L206) | 206 | `"        cost = _finite_nonnegative_number(usage.get(\"cost_usd\"))"` | — |
| [SRC-4FFD5AFC54-L000207](../../scripts/run_answer_quality_benchmark.py#L207) | 207 | `"        if cost is not None:"` | — |
| [SRC-4FFD5AFC54-L000208](../../scripts/run_answer_quality_benchmark.py#L208) | 208 | `"            reported_costs.append(cost)"` | — |
| [SRC-4FFD5AFC54-L000209](../../scripts/run_answer_quality_benchmark.py#L209) | 209 | `""` | — |
| [SRC-4FFD5AFC54-L000210](../../scripts/run_answer_quality_benchmark.py#L210) | 210 | `"    if not calls:"` | — |
| [SRC-4FFD5AFC54-L000211](../../scripts/run_answer_quality_benchmark.py#L211) | 211 | `"        cost_status = \"NO_MODEL_CALL_METADATA\""` | — |
| [SRC-4FFD5AFC54-L000212](../../scripts/run_answer_quality_benchmark.py#L212) | 212 | `"    elif len(reported_costs) == len(calls):"` | — |
| [SRC-4FFD5AFC54-L000213](../../scripts/run_answer_quality_benchmark.py#L213) | 213 | `"        cost_status = \"COMPLETE_FOR_RETURNED_MODEL_CALLS\""` | — |
| [SRC-4FFD5AFC54-L000214](../../scripts/run_answer_quality_benchmark.py#L214) | 214 | `"    elif reported_costs:"` | — |
| [SRC-4FFD5AFC54-L000215](../../scripts/run_answer_quality_benchmark.py#L215) | 215 | `"        cost_status = \"PARTIAL_PROVIDER_REPORTED_MODEL_COST\""` | — |
| [SRC-4FFD5AFC54-L000216](../../scripts/run_answer_quality_benchmark.py#L216) | 216 | `"    else:"` | — |
| [SRC-4FFD5AFC54-L000217](../../scripts/run_answer_quality_benchmark.py#L217) | 217 | `"        cost_status = \"PROVIDER_COST_NOT_REPORTED\""` | — |
| [SRC-4FFD5AFC54-L000218](../../scripts/run_answer_quality_benchmark.py#L218) | 218 | `""` | — |
| [SRC-4FFD5AFC54-L000219](../../scripts/run_answer_quality_benchmark.py#L219) | 219 | `"    return {"` | — |
| [SRC-4FFD5AFC54-L000220](../../scripts/run_answer_quality_benchmark.py#L220) | 220 | `"        \"search_outcome\": outcome if isinstance(outcome, str) else \"unknown\","` | — |
| [SRC-4FFD5AFC54-L000221](../../scripts/run_answer_quality_benchmark.py#L221) | 221 | `"        \"pipeline_completion_status\": pipeline if isinstance(pipeline, str) else \"unknown\","` | — |
| [SRC-4FFD5AFC54-L000222](../../scripts/run_answer_quality_benchmark.py#L222) | 222 | `"        \"tool_status\": tool_status,"` | — |
| [SRC-4FFD5AFC54-L000223](../../scripts/run_answer_quality_benchmark.py#L223) | 223 | `"        \"required_tool_statuses\": required_tool_statuses,"` | — |
| [SRC-4FFD5AFC54-L000224](../../scripts/run_answer_quality_benchmark.py#L224) | 224 | `"        \"required_tool_success_count\": sum(1 for row in required_tool_statuses if row[\"successful_completion\"]),"` | — |
| [SRC-4FFD5AFC54-L000225](../../scripts/run_answer_quality_benchmark.py#L225) | 225 | `"        \"required_tool_count\": len(required_tool_statuses),"` | — |
| [SRC-4FFD5AFC54-L000226](../../scripts/run_answer_quality_benchmark.py#L226) | 226 | `"        \"required_tool_success_rate\": ("` | — |
| [SRC-4FFD5AFC54-L000227](../../scripts/run_answer_quality_benchmark.py#L227) | 227 | `"            round("` | — |
| [SRC-4FFD5AFC54-L000228](../../scripts/run_answer_quality_benchmark.py#L228) | 228 | `"                sum(1 for row in required_tool_statuses if row[\"successful_completion\"])"` | — |
| [SRC-4FFD5AFC54-L000229](../../scripts/run_answer_quality_benchmark.py#L229) | 229 | `"                / len(required_tool_statuses),"` | — |
| [SRC-4FFD5AFC54-L000230](../../scripts/run_answer_quality_benchmark.py#L230) | 230 | `"                4,"` | — |
| [SRC-4FFD5AFC54-L000231](../../scripts/run_answer_quality_benchmark.py#L231) | 231 | `"            )"` | — |
| [SRC-4FFD5AFC54-L000232](../../scripts/run_answer_quality_benchmark.py#L232) | 232 | `"            if required_tool_statuses"` | — |
| [SRC-4FFD5AFC54-L000233](../../scripts/run_answer_quality_benchmark.py#L233) | 233 | `"            else None"` | — |
| [SRC-4FFD5AFC54-L000234](../../scripts/run_answer_quality_benchmark.py#L234) | 234 | `"        ),"` | — |
| [SRC-4FFD5AFC54-L000235](../../scripts/run_answer_quality_benchmark.py#L235) | 235 | `"        \"required_tool_status_metrics_status\": ("` | — |
| [SRC-4FFD5AFC54-L000236](../../scripts/run_answer_quality_benchmark.py#L236) | 236 | `"            \"NOT_MEASURED_TOOL_REQUIREMENTS_OR_MATRIX_UNKNOWN\""` | — |
| [SRC-4FFD5AFC54-L000237](../../scripts/run_answer_quality_benchmark.py#L237) | 237 | `"            if not required_tool_matrix_present"` | — |
| [SRC-4FFD5AFC54-L000238](../../scripts/run_answer_quality_benchmark.py#L238) | 238 | `"            else \"SCORED_FROM_TOOL_EXECUTION_MATRIX\""` | — |
| [SRC-4FFD5AFC54-L000239](../../scripts/run_answer_quality_benchmark.py#L239) | 239 | `"            if required_tool_matrix_complete"` | — |
| [SRC-4FFD5AFC54-L000240](../../scripts/run_answer_quality_benchmark.py#L240) | 240 | `"            else \"INCOMPLETE_TOOL_STATUS_MATRIX\""` | — |
| [SRC-4FFD5AFC54-L000241](../../scripts/run_answer_quality_benchmark.py#L241) | 241 | `"        ),"` | — |
| [SRC-4FFD5AFC54-L000242](../../scripts/run_answer_quality_benchmark.py#L242) | 242 | `"        \"required_tool_matrix_present\": required_tool_matrix_present,"` | — |
| [SRC-4FFD5AFC54-L000243](../../scripts/run_answer_quality_benchmark.py#L243) | 243 | `"        \"required_tool_matrix_complete\": required_tool_matrix_complete,"` | — |
| [SRC-4FFD5AFC54-L000244](../../scripts/run_answer_quality_benchmark.py#L244) | 244 | `"        \"source_count\": source_count,"` | — |
| [SRC-4FFD5AFC54-L000245](../../scripts/run_answer_quality_benchmark.py#L245) | 245 | `"        \"model_call_count\": len(calls),"` | — |
| [SRC-4FFD5AFC54-L000246](../../scripts/run_answer_quality_benchmark.py#L246) | 246 | `"        \"provider_reported_model_cost_usd\": round(sum(reported_costs), 10) if reported_costs else None,"` | — |
| [SRC-4FFD5AFC54-L000247](../../scripts/run_answer_quality_benchmark.py#L247) | 247 | `"        \"provider_reported_model_cost_call_count\": len(reported_costs),"` | — |
| [SRC-4FFD5AFC54-L000248](../../scripts/run_answer_quality_benchmark.py#L248) | 248 | `"        \"provider_reported_model_cost_status\": cost_status,"` | — |
| [SRC-4FFD5AFC54-L000249](../../scripts/run_answer_quality_benchmark.py#L249) | 249 | `"        \"request_cost_usd\": None,"` | — |
| [SRC-4FFD5AFC54-L000250](../../scripts/run_answer_quality_benchmark.py#L250) | 250 | `"        \"request_cost_status\": \"NOT_MEASURED_TOTAL_CONNECTOR_COSTS_NOT_EXPOSED\","` | — |
| [SRC-4FFD5AFC54-L000251](../../scripts/run_answer_quality_benchmark.py#L251) | 251 | `"    }"` | — |
| [SRC-4FFD5AFC54-L000252](../../scripts/run_answer_quality_benchmark.py#L252) | 252 | `""` | — |
| [SRC-4FFD5AFC54-L000253](../../scripts/run_answer_quality_benchmark.py#L253) | 253 | `""` | — |
| [SRC-4FFD5AFC54-L000254](../../scripts/run_answer_quality_benchmark.py#L254) | 254 | `"def validate_base_url(base_url: str, *, token_present: bool = False) -> str:"` | — |
| [SRC-4FFD5AFC54-L000255](../../scripts/run_answer_quality_benchmark.py#L255) | 255 | `"    \"\"\"Validate and normalize an API origin before any request can carry a token.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000256](../../scripts/run_answer_quality_benchmark.py#L256) | 256 | `"    if not isinstance(base_url, str) or not base_url.strip():"` | — |
| [SRC-4FFD5AFC54-L000257](../../scripts/run_answer_quality_benchmark.py#L257) | 257 | `"        raise ValueError(\"Base URL must be a non-empty HTTP(S) origin.\")"` | — |
| [SRC-4FFD5AFC54-L000258](../../scripts/run_answer_quality_benchmark.py#L258) | 258 | `"    try:"` | — |
| [SRC-4FFD5AFC54-L000259](../../scripts/run_answer_quality_benchmark.py#L259) | 259 | `"        parsed = urllib.parse.urlsplit(base_url.strip())"` | — |
| [SRC-4FFD5AFC54-L000260](../../scripts/run_answer_quality_benchmark.py#L260) | 260 | `"        scheme = parsed.scheme.lower()"` | — |
| [SRC-4FFD5AFC54-L000261](../../scripts/run_answer_quality_benchmark.py#L261) | 261 | `"        host = (parsed.hostname or \"\").lower().rstrip(\".\")"` | — |
| [SRC-4FFD5AFC54-L000262](../../scripts/run_answer_quality_benchmark.py#L262) | 262 | `"        port = parsed.port"` | — |
| [SRC-4FFD5AFC54-L000263](../../scripts/run_answer_quality_benchmark.py#L263) | 263 | `"    except ValueError as exc:"` | — |
| [SRC-4FFD5AFC54-L000264](../../scripts/run_answer_quality_benchmark.py#L264) | 264 | `"        raise ValueError(\"Base URL is malformed.\") from exc"` | — |
| [SRC-4FFD5AFC54-L000265](../../scripts/run_answer_quality_benchmark.py#L265) | 265 | `""` | — |
| [SRC-4FFD5AFC54-L000266](../../scripts/run_answer_quality_benchmark.py#L266) | 266 | `"    if scheme not in {\"http\", \"https\"} or not host:"` | — |
| [SRC-4FFD5AFC54-L000267](../../scripts/run_answer_quality_benchmark.py#L267) | 267 | `"        raise ValueError(\"Base URL must use HTTP or HTTPS and include a hostname.\")"` | — |
| [SRC-4FFD5AFC54-L000268](../../scripts/run_answer_quality_benchmark.py#L268) | 268 | `"    if parsed.username is not None or parsed.password is not None:"` | — |
| [SRC-4FFD5AFC54-L000269](../../scripts/run_answer_quality_benchmark.py#L269) | 269 | `"        raise ValueError(\"Base URL must not include a username or password.\")"` | — |
| [SRC-4FFD5AFC54-L000270](../../scripts/run_answer_quality_benchmark.py#L270) | 270 | `"    if parsed.path not in {\"\", \"/\"} or parsed.query or parsed.fragment:"` | — |
| [SRC-4FFD5AFC54-L000271](../../scripts/run_answer_quality_benchmark.py#L271) | 271 | `"        raise ValueError(\"Base URL must contain only the origin, without path, query, or fragment.\")"` | — |
| [SRC-4FFD5AFC54-L000272](../../scripts/run_answer_quality_benchmark.py#L272) | 272 | `""` | — |
| [SRC-4FFD5AFC54-L000273](../../scripts/run_answer_quality_benchmark.py#L273) | 273 | `"    loopback = host == \"localhost\""` | — |
| [SRC-4FFD5AFC54-L000274](../../scripts/run_answer_quality_benchmark.py#L274) | 274 | `"    try:"` | — |
| [SRC-4FFD5AFC54-L000275](../../scripts/run_answer_quality_benchmark.py#L275) | 275 | `"        loopback = ipaddress.ip_address(host).is_loopback"` | — |
| [SRC-4FFD5AFC54-L000276](../../scripts/run_answer_quality_benchmark.py#L276) | 276 | `"    except ValueError:"` | — |
| [SRC-4FFD5AFC54-L000277](../../scripts/run_answer_quality_benchmark.py#L277) | 277 | `"        pass"` | — |
| [SRC-4FFD5AFC54-L000278](../../scripts/run_answer_quality_benchmark.py#L278) | 278 | `""` | — |
| [SRC-4FFD5AFC54-L000279](../../scripts/run_answer_quality_benchmark.py#L279) | 279 | `"    if scheme == \"http\" and not loopback:"` | — |
| [SRC-4FFD5AFC54-L000280](../../scripts/run_answer_quality_benchmark.py#L280) | 280 | `"        raise ValueError(\"Plain HTTP is allowed only for localhost or a loopback IP.\")"` | — |
| [SRC-4FFD5AFC54-L000281](../../scripts/run_answer_quality_benchmark.py#L281) | 281 | `""` | — |
| [SRC-4FFD5AFC54-L000282](../../scripts/run_answer_quality_benchmark.py#L282) | 282 | `"    if (scheme == \"https\" and port == 443) or (scheme == \"http\" and port == 80):"` | — |
| [SRC-4FFD5AFC54-L000283](../../scripts/run_answer_quality_benchmark.py#L283) | 283 | `"        port = None"` | — |
| [SRC-4FFD5AFC54-L000284](../../scripts/run_answer_quality_benchmark.py#L284) | 284 | `"    host_for_origin = f\"[{host}]\" if \":\" in host else host"` | — |
| [SRC-4FFD5AFC54-L000285](../../scripts/run_answer_quality_benchmark.py#L285) | 285 | `"    origin = f\"{scheme}://{host_for_origin}\" + (f\":{port}\" if port is not None else \"\")"` | — |
| [SRC-4FFD5AFC54-L000286](../../scripts/run_answer_quality_benchmark.py#L286) | 286 | `""` | — |
| [SRC-4FFD5AFC54-L000287](../../scripts/run_answer_quality_benchmark.py#L287) | 287 | `"    if token_present and not loopback:"` | — |
| [SRC-4FFD5AFC54-L000288](../../scripts/run_answer_quality_benchmark.py#L288) | 288 | `"        allowed = os.getenv(\"OMARAI_BENCHMARK_ALLOWED_ORIGIN\", \"\").strip()"` | — |
| [SRC-4FFD5AFC54-L000289](../../scripts/run_answer_quality_benchmark.py#L289) | 289 | `"        if not allowed:"` | — |
| [SRC-4FFD5AFC54-L000290](../../scripts/run_answer_quality_benchmark.py#L290) | 290 | `"            raise ValueError("` | — |
| [SRC-4FFD5AFC54-L000291](../../scripts/run_answer_quality_benchmark.py#L291) | 291 | `"                \"A bearer token requires OMARAI_BENCHMARK_ALLOWED_ORIGIN to match \""` | — |
| [SRC-4FFD5AFC54-L000292](../../scripts/run_answer_quality_benchmark.py#L292) | 292 | `"                \"the exact HTTPS deployment origin.\""` | — |
| [SRC-4FFD5AFC54-L000293](../../scripts/run_answer_quality_benchmark.py#L293) | 293 | `"            )"` | — |
| [SRC-4FFD5AFC54-L000294](../../scripts/run_answer_quality_benchmark.py#L294) | 294 | `"        allowed_origin = validate_base_url(allowed, token_present=False)"` | — |
| [SRC-4FFD5AFC54-L000295](../../scripts/run_answer_quality_benchmark.py#L295) | 295 | `"        if allowed_origin != origin:"` | — |
| [SRC-4FFD5AFC54-L000296](../../scripts/run_answer_quality_benchmark.py#L296) | 296 | `"            raise ValueError("` | — |
| [SRC-4FFD5AFC54-L000297](../../scripts/run_answer_quality_benchmark.py#L297) | 297 | `"                \"Refusing to send the bearer token: base URL does not match \""` | — |
| [SRC-4FFD5AFC54-L000298](../../scripts/run_answer_quality_benchmark.py#L298) | 298 | `"                \"OMARAI_BENCHMARK_ALLOWED_ORIGIN.\""` | — |
| [SRC-4FFD5AFC54-L000299](../../scripts/run_answer_quality_benchmark.py#L299) | 299 | `"            )"` | — |
| [SRC-4FFD5AFC54-L000300](../../scripts/run_answer_quality_benchmark.py#L300) | 300 | `"    return origin"` | — |
| [SRC-4FFD5AFC54-L000301](../../scripts/run_answer_quality_benchmark.py#L301) | 301 | `""` | — |
| [SRC-4FFD5AFC54-L000302](../../scripts/run_answer_quality_benchmark.py#L302) | 302 | `""` | — |
| [SRC-4FFD5AFC54-L000303](../../scripts/run_answer_quality_benchmark.py#L303) | 303 | `"class _NoRedirectHandler(urllib.request.HTTPRedirectHandler):"` | — |
| [SRC-4FFD5AFC54-L000304](../../scripts/run_answer_quality_benchmark.py#L304) | 304 | `"    \"\"\"Do not follow redirects; the bearer token must never move to another origin.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000305](../../scripts/run_answer_quality_benchmark.py#L305) | 305 | `""` | — |
| [SRC-4FFD5AFC54-L000306](../../scripts/run_answer_quality_benchmark.py#L306) | 306 | `"    def redirect_request(self, req, fp, code, msg, headers, newurl):"` | — |
| [SRC-4FFD5AFC54-L000307](../../scripts/run_answer_quality_benchmark.py#L307) | 307 | `"        return None"` | — |
| [SRC-4FFD5AFC54-L000308](../../scripts/run_answer_quality_benchmark.py#L308) | 308 | `""` | — |
| [SRC-4FFD5AFC54-L000309](../../scripts/run_answer_quality_benchmark.py#L309) | 309 | `""` | — |
| [SRC-4FFD5AFC54-L000310](../../scripts/run_answer_quality_benchmark.py#L310) | 310 | `"_NO_REDIRECT_OPENER = urllib.request.build_opener(_NoRedirectHandler())"` | — |
| [SRC-4FFD5AFC54-L000311](../../scripts/run_answer_quality_benchmark.py#L311) | 311 | `""` | — |
| [SRC-4FFD5AFC54-L000312](../../scripts/run_answer_quality_benchmark.py#L312) | 312 | `"REQUIRED_FIELDS = {"` | — |
| [SRC-4FFD5AFC54-L000313](../../scripts/run_answer_quality_benchmark.py#L313) | 313 | `"    \"case_id\","` | — |
| [SRC-4FFD5AFC54-L000314](../../scripts/run_answer_quality_benchmark.py#L314) | 314 | `"    \"category\","` | — |
| [SRC-4FFD5AFC54-L000315](../../scripts/run_answer_quality_benchmark.py#L315) | 315 | `"    \"language\","` | — |
| [SRC-4FFD5AFC54-L000316](../../scripts/run_answer_quality_benchmark.py#L316) | 316 | `"    \"question\","` | — |
| [SRC-4FFD5AFC54-L000317](../../scripts/run_answer_quality_benchmark.py#L317) | 317 | `"    \"expected_strategy\","` | — |
| [SRC-4FFD5AFC54-L000318](../../scripts/run_answer_quality_benchmark.py#L318) | 318 | `"    \"required_behaviors\","` | — |
| [SRC-4FFD5AFC54-L000319](../../scripts/run_answer_quality_benchmark.py#L319) | 319 | `"    \"forbidden_behaviors\","` | — |
| [SRC-4FFD5AFC54-L000320](../../scripts/run_answer_quality_benchmark.py#L320) | 320 | `"    \"evidence_fixture\","` | — |
| [SRC-4FFD5AFC54-L000321](../../scripts/run_answer_quality_benchmark.py#L321) | 321 | `"    \"failure_conditions\","` | — |
| [SRC-4FFD5AFC54-L000322](../../scripts/run_answer_quality_benchmark.py#L322) | 322 | `"    \"evaluation_mode\","` | — |
| [SRC-4FFD5AFC54-L000323](../../scripts/run_answer_quality_benchmark.py#L323) | 323 | `"}"` | — |
| [SRC-4FFD5AFC54-L000324](../../scripts/run_answer_quality_benchmark.py#L324) | 324 | `"ALLOWED_STRATEGIES = {\"local\", \"model_no_search\", \"web_search\", \"clarify\"}"` | — |
| [SRC-4FFD5AFC54-L000325](../../scripts/run_answer_quality_benchmark.py#L325) | 325 | `"ALLOWED_EVAL_MODES = {\"deterministic_structure\", \"fixture_assisted\", \"human_judgment\"}"` | — |
| [SRC-4FFD5AFC54-L000326](../../scripts/run_answer_quality_benchmark.py#L326) | 326 | `""` | — |
| [SRC-4FFD5AFC54-L000327](../../scripts/run_answer_quality_benchmark.py#L327) | 327 | `""` | — |
| [SRC-4FFD5AFC54-L000328](../../scripts/run_answer_quality_benchmark.py#L328) | 328 | `"def _utc_now() -> str:"` | — |
| [SRC-4FFD5AFC54-L000329](../../scripts/run_answer_quality_benchmark.py#L329) | 329 | `"    return datetime.now(UTC).isoformat(timespec=\"seconds\")"` | — |
| [SRC-4FFD5AFC54-L000330](../../scripts/run_answer_quality_benchmark.py#L330) | 330 | `""` | — |
| [SRC-4FFD5AFC54-L000331](../../scripts/run_answer_quality_benchmark.py#L331) | 331 | `""` | — |
| [SRC-4FFD5AFC54-L000332](../../scripts/run_answer_quality_benchmark.py#L332) | 332 | `"def load_corpus(path: Path) -> dict:"` | — |
| [SRC-4FFD5AFC54-L000333](../../scripts/run_answer_quality_benchmark.py#L333) | 333 | `"    if not path.is_file():"` | — |
| [SRC-4FFD5AFC54-L000334](../../scripts/run_answer_quality_benchmark.py#L334) | 334 | `"        raise FileNotFoundError(f\"Corpus not found: {path}\")"` | — |
| [SRC-4FFD5AFC54-L000335](../../scripts/run_answer_quality_benchmark.py#L335) | 335 | `"    data = json.loads(path.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-4FFD5AFC54-L000336](../../scripts/run_answer_quality_benchmark.py#L336) | 336 | `"    if not isinstance(data, dict) or not isinstance(data.get(\"cases\"), list):"` | — |
| [SRC-4FFD5AFC54-L000337](../../scripts/run_answer_quality_benchmark.py#L337) | 337 | `"        raise TypeError(\"Corpus root must be an object with a cases array\")"` | — |
| [SRC-4FFD5AFC54-L000338](../../scripts/run_answer_quality_benchmark.py#L338) | 338 | `"    if data.get(\"parts\"):"` | — |
| [SRC-4FFD5AFC54-L000339](../../scripts/run_answer_quality_benchmark.py#L339) | 339 | `"        raise ValueError(\"Incomplete shard index is not accepted; use merged cases[] corpus\")"` | — |
| [SRC-4FFD5AFC54-L000340](../../scripts/run_answer_quality_benchmark.py#L340) | 340 | `"    return data"` | — |
| [SRC-4FFD5AFC54-L000341](../../scripts/run_answer_quality_benchmark.py#L341) | 341 | `""` | — |
| [SRC-4FFD5AFC54-L000342](../../scripts/run_answer_quality_benchmark.py#L342) | 342 | `""` | — |
| [SRC-4FFD5AFC54-L000343](../../scripts/run_answer_quality_benchmark.py#L343) | 343 | `"def validate_corpus(data: dict) -> list[str]:"` | — |
| [SRC-4FFD5AFC54-L000344](../../scripts/run_answer_quality_benchmark.py#L344) | 344 | `"    \"\"\"Return a list of human-readable problems (empty => OK).\"\"\""` | — |
| [SRC-4FFD5AFC54-L000345](../../scripts/run_answer_quality_benchmark.py#L345) | 345 | `"    problems: list[str] = []"` | — |
| [SRC-4FFD5AFC54-L000346](../../scripts/run_answer_quality_benchmark.py#L346) | 346 | `"    cases = data.get(\"cases\") or []"` | — |
| [SRC-4FFD5AFC54-L000347](../../scripts/run_answer_quality_benchmark.py#L347) | 347 | `"    if data.get(\"case_count\") != len(cases):"` | — |
| [SRC-4FFD5AFC54-L000348](../../scripts/run_answer_quality_benchmark.py#L348) | 348 | `"        problems.append("` | — |
| [SRC-4FFD5AFC54-L000349](../../scripts/run_answer_quality_benchmark.py#L349) | 349 | `"            f\"case_count metadata {data.get('case_count')!r} != len(cases) {len(cases)}\""` | — |
| [SRC-4FFD5AFC54-L000350](../../scripts/run_answer_quality_benchmark.py#L350) | 350 | `"        )"` | — |
| [SRC-4FFD5AFC54-L000351](../../scripts/run_answer_quality_benchmark.py#L351) | 351 | `"    if len(cases) < 40:"` | — |
| [SRC-4FFD5AFC54-L000352](../../scripts/run_answer_quality_benchmark.py#L352) | 352 | `"        problems.append(f\"expected at least 40 cases, found {len(cases)}\")"` | — |
| [SRC-4FFD5AFC54-L000353](../../scripts/run_answer_quality_benchmark.py#L353) | 353 | `"    ids: list[str] = []"` | — |
| [SRC-4FFD5AFC54-L000354](../../scripts/run_answer_quality_benchmark.py#L354) | 354 | `"    for i, case in enumerate(cases):"` | — |
| [SRC-4FFD5AFC54-L000355](../../scripts/run_answer_quality_benchmark.py#L355) | 355 | `"        if not isinstance(case, dict):"` | — |
| [SRC-4FFD5AFC54-L000356](../../scripts/run_answer_quality_benchmark.py#L356) | 356 | `"            problems.append(f\"cases[{i}] is not an object\")"` | — |
| [SRC-4FFD5AFC54-L000357](../../scripts/run_answer_quality_benchmark.py#L357) | 357 | `"            continue"` | — |
| [SRC-4FFD5AFC54-L000358](../../scripts/run_answer_quality_benchmark.py#L358) | 358 | `"        missing = REQUIRED_FIELDS - set(case)"` | — |
| [SRC-4FFD5AFC54-L000359](../../scripts/run_answer_quality_benchmark.py#L359) | 359 | `"        if missing:"` | — |
| [SRC-4FFD5AFC54-L000360](../../scripts/run_answer_quality_benchmark.py#L360) | 360 | `"            problems.append(f\"{case.get('case_id', i)}: missing {sorted(missing)}\")"` | — |
| [SRC-4FFD5AFC54-L000361](../../scripts/run_answer_quality_benchmark.py#L361) | 361 | `"        cid = case.get(\"case_id\")"` | — |
| [SRC-4FFD5AFC54-L000362](../../scripts/run_answer_quality_benchmark.py#L362) | 362 | `"        if isinstance(cid, str):"` | — |
| [SRC-4FFD5AFC54-L000363](../../scripts/run_answer_quality_benchmark.py#L363) | 363 | `"            ids.append(cid)"` | — |
| [SRC-4FFD5AFC54-L000364](../../scripts/run_answer_quality_benchmark.py#L364) | 364 | `"        if case.get(\"expected_strategy\") not in ALLOWED_STRATEGIES:"` | — |
| [SRC-4FFD5AFC54-L000365](../../scripts/run_answer_quality_benchmark.py#L365) | 365 | `"            problems.append(f\"{cid}: bad strategy {case.get('expected_strategy')!r}\")"` | — |
| [SRC-4FFD5AFC54-L000366](../../scripts/run_answer_quality_benchmark.py#L366) | 366 | `"        if case.get(\"evaluation_mode\") not in ALLOWED_EVAL_MODES:"` | — |
| [SRC-4FFD5AFC54-L000367](../../scripts/run_answer_quality_benchmark.py#L367) | 367 | `"            problems.append(f\"{cid}: bad evaluation_mode {case.get('evaluation_mode')!r}\")"` | — |
| [SRC-4FFD5AFC54-L000368](../../scripts/run_answer_quality_benchmark.py#L368) | 368 | `"        q = case.get(\"question\")"` | — |
| [SRC-4FFD5AFC54-L000369](../../scripts/run_answer_quality_benchmark.py#L369) | 369 | `"        if not isinstance(q, str) or len(q.strip()) < 2:"` | — |
| [SRC-4FFD5AFC54-L000370](../../scripts/run_answer_quality_benchmark.py#L370) | 370 | `"            problems.append(f\"{cid}: empty question\")"` | — |
| [SRC-4FFD5AFC54-L000371](../../scripts/run_answer_quality_benchmark.py#L371) | 371 | `"    if len(ids) != len(set(ids)):"` | — |
| [SRC-4FFD5AFC54-L000372](../../scripts/run_answer_quality_benchmark.py#L372) | 372 | `"        problems.append(\"duplicate case_id values\")"` | — |
| [SRC-4FFD5AFC54-L000373](../../scripts/run_answer_quality_benchmark.py#L373) | 373 | `"    return problems"` | — |
| [SRC-4FFD5AFC54-L000374](../../scripts/run_answer_quality_benchmark.py#L374) | 374 | `""` | — |
| [SRC-4FFD5AFC54-L000375](../../scripts/run_answer_quality_benchmark.py#L375) | 375 | `""` | — |
| [SRC-4FFD5AFC54-L000376](../../scripts/run_answer_quality_benchmark.py#L376) | 376 | `"def redact_secrets(text: str) -> str:"` | — |
| [SRC-4FFD5AFC54-L000377](../../scripts/run_answer_quality_benchmark.py#L377) | 377 | `"    \"\"\"Best-effort redaction of common secret patterns from stored outputs.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000378](../../scripts/run_answer_quality_benchmark.py#L378) | 378 | `"    if not text:"` | — |
| [SRC-4FFD5AFC54-L000379](../../scripts/run_answer_quality_benchmark.py#L379) | 379 | `"        return text"` | — |
| [SRC-4FFD5AFC54-L000380](../../scripts/run_answer_quality_benchmark.py#L380) | 380 | `"    out = text"` | — |
| [SRC-4FFD5AFC54-L000381](../../scripts/run_answer_quality_benchmark.py#L381) | 381 | `"    for key in ("` | — |
| [SRC-4FFD5AFC54-L000382](../../scripts/run_answer_quality_benchmark.py#L382) | 382 | `"        \"OPENROUTER_API_KEY\","` | — |
| [SRC-4FFD5AFC54-L000383](../../scripts/run_answer_quality_benchmark.py#L383) | 383 | `"        \"OMARAI_ACCESS_TOKEN\","` | — |
| [SRC-4FFD5AFC54-L000384](../../scripts/run_answer_quality_benchmark.py#L384) | 384 | `"        \"OMARAI_LLM_API_KEY\","` | — |
| [SRC-4FFD5AFC54-L000385](../../scripts/run_answer_quality_benchmark.py#L385) | 385 | `"        \"Authorization\","` | — |
| [SRC-4FFD5AFC54-L000386](../../scripts/run_answer_quality_benchmark.py#L386) | 386 | `"        \"Bearer \","` | — |
| [SRC-4FFD5AFC54-L000387](../../scripts/run_answer_quality_benchmark.py#L387) | 387 | `"    ):"` | — |
| [SRC-4FFD5AFC54-L000388](../../scripts/run_answer_quality_benchmark.py#L388) | 388 | `"        out = out.replace(key, f\"[REDACTED:{key.strip()}]\")"` | — |
| [SRC-4FFD5AFC54-L000389](../../scripts/run_answer_quality_benchmark.py#L389) | 389 | `"    token = os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-4FFD5AFC54-L000390](../../scripts/run_answer_quality_benchmark.py#L390) | 390 | `"    if token and token in out:"` | — |
| [SRC-4FFD5AFC54-L000391](../../scripts/run_answer_quality_benchmark.py#L391) | 391 | `"        out = out.replace(token, \"[REDACTED:OMARAI_ACCESS_TOKEN]\")"` | — |
| [SRC-4FFD5AFC54-L000392](../../scripts/run_answer_quality_benchmark.py#L392) | 392 | `"    for env_name in (\"OPENROUTER_API_KEY\", \"OMARAI_LLM_API_KEY\"):"` | — |
| [SRC-4FFD5AFC54-L000393](../../scripts/run_answer_quality_benchmark.py#L393) | 393 | `"        val = os.getenv(env_name, \"\").strip()"` | — |
| [SRC-4FFD5AFC54-L000394](../../scripts/run_answer_quality_benchmark.py#L394) | 394 | `"        if val and val in out:"` | — |
| [SRC-4FFD5AFC54-L000395](../../scripts/run_answer_quality_benchmark.py#L395) | 395 | `"            out = out.replace(val, f\"[REDACTED:{env_name}]\")"` | — |
| [SRC-4FFD5AFC54-L000396](../../scripts/run_answer_quality_benchmark.py#L396) | 396 | `"    return out"` | — |
| [SRC-4FFD5AFC54-L000397](../../scripts/run_answer_quality_benchmark.py#L397) | 397 | `""` | — |
| [SRC-4FFD5AFC54-L000398](../../scripts/run_answer_quality_benchmark.py#L398) | 398 | `""` | — |
| [SRC-4FFD5AFC54-L000399](../../scripts/run_answer_quality_benchmark.py#L399) | 399 | `"def post_agent("` | — |
| [SRC-4FFD5AFC54-L000400](../../scripts/run_answer_quality_benchmark.py#L400) | 400 | `"    base_url: str,"` | — |
| [SRC-4FFD5AFC54-L000401](../../scripts/run_answer_quality_benchmark.py#L401) | 401 | `"    question: str,"` | — |
| [SRC-4FFD5AFC54-L000402](../../scripts/run_answer_quality_benchmark.py#L402) | 402 | `"    timeout: float,"` | — |
| [SRC-4FFD5AFC54-L000403](../../scripts/run_answer_quality_benchmark.py#L403) | 403 | `"    token: str \| None,"` | — |
| [SRC-4FFD5AFC54-L000404](../../scripts/run_answer_quality_benchmark.py#L404) | 404 | `") -> tuple[int, dict \| str]:"` | — |
| [SRC-4FFD5AFC54-L000405](../../scripts/run_answer_quality_benchmark.py#L405) | 405 | `"    origin = validate_base_url(base_url, token_present=bool(token))"` | — |
| [SRC-4FFD5AFC54-L000406](../../scripts/run_answer_quality_benchmark.py#L406) | 406 | `"    url = origin + \"/api/agent\""` | — |
| [SRC-4FFD5AFC54-L000407](../../scripts/run_answer_quality_benchmark.py#L407) | 407 | `"    body = json.dumps({\"question\": question, \"history\": []}, ensure_ascii=False).encode(\"utf-8\")"` | — |
| [SRC-4FFD5AFC54-L000408](../../scripts/run_answer_quality_benchmark.py#L408) | 408 | `"    headers = {\"Content-Type\": \"application/json\", \"Content-Length\": str(len(body))}"` | — |
| [SRC-4FFD5AFC54-L000409](../../scripts/run_answer_quality_benchmark.py#L409) | 409 | `"    if token:"` | — |
| [SRC-4FFD5AFC54-L000410](../../scripts/run_answer_quality_benchmark.py#L410) | 410 | `"        headers[\"Authorization\"] = \"Bearer \" + token"` | — |
| [SRC-4FFD5AFC54-L000411](../../scripts/run_answer_quality_benchmark.py#L411) | 411 | `"    req = urllib.request.Request(url, data=body, headers=headers, method=\"POST\")"` | — |
| [SRC-4FFD5AFC54-L000412](../../scripts/run_answer_quality_benchmark.py#L412) | 412 | `"    try:"` | — |
| [SRC-4FFD5AFC54-L000413](../../scripts/run_answer_quality_benchmark.py#L413) | 413 | `"        with _NO_REDIRECT_OPENER.open(req, timeout=timeout) as resp:"` | — |
| [SRC-4FFD5AFC54-L000414](../../scripts/run_answer_quality_benchmark.py#L414) | 414 | `"            raw_bytes = resp.read(MAX_RESPONSE_BYTES + 1)"` | — |
| [SRC-4FFD5AFC54-L000415](../../scripts/run_answer_quality_benchmark.py#L415) | 415 | `"            if len(raw_bytes) > MAX_RESPONSE_BYTES:"` | — |
| [SRC-4FFD5AFC54-L000416](../../scripts/run_answer_quality_benchmark.py#L416) | 416 | `"                return 0, {\"error\": \"ResponseTooLarge\", \"detail\": \"Response exceeded the 2 MB limit.\"}"` | — |
| [SRC-4FFD5AFC54-L000417](../../scripts/run_answer_quality_benchmark.py#L417) | 417 | `"            raw = raw_bytes.decode(\"utf-8\", errors=\"replace\")"` | — |
| [SRC-4FFD5AFC54-L000418](../../scripts/run_answer_quality_benchmark.py#L418) | 418 | `"            status = getattr(resp, \"status\", 200)"` | — |
| [SRC-4FFD5AFC54-L000419](../../scripts/run_answer_quality_benchmark.py#L419) | 419 | `"            try:"` | — |
| [SRC-4FFD5AFC54-L000420](../../scripts/run_answer_quality_benchmark.py#L420) | 420 | `"                return status, json.loads(raw)"` | — |
| [SRC-4FFD5AFC54-L000421](../../scripts/run_answer_quality_benchmark.py#L421) | 421 | `"            except json.JSONDecodeError:"` | — |
| [SRC-4FFD5AFC54-L000422](../../scripts/run_answer_quality_benchmark.py#L422) | 422 | `"                return status, raw"` | — |
| [SRC-4FFD5AFC54-L000423](../../scripts/run_answer_quality_benchmark.py#L423) | 423 | `"    except urllib.error.HTTPError as exc:"` | — |
| [SRC-4FFD5AFC54-L000424](../../scripts/run_answer_quality_benchmark.py#L424) | 424 | `"        raw_bytes = exc.read(MAX_RESPONSE_BYTES + 1)"` | — |
| [SRC-4FFD5AFC54-L000425](../../scripts/run_answer_quality_benchmark.py#L425) | 425 | `"        if len(raw_bytes) > MAX_RESPONSE_BYTES:"` | — |
| [SRC-4FFD5AFC54-L000426](../../scripts/run_answer_quality_benchmark.py#L426) | 426 | `"            return exc.code, {\"error\": \"ResponseTooLarge\", \"detail\": \"Response exceeded the 2 MB limit.\"}"` | — |
| [SRC-4FFD5AFC54-L000427](../../scripts/run_answer_quality_benchmark.py#L427) | 427 | `"        raw = raw_bytes.decode(\"utf-8\", errors=\"replace\")"` | — |
| [SRC-4FFD5AFC54-L000428](../../scripts/run_answer_quality_benchmark.py#L428) | 428 | `"        try:"` | — |
| [SRC-4FFD5AFC54-L000429](../../scripts/run_answer_quality_benchmark.py#L429) | 429 | `"            return exc.code, json.loads(raw)"` | — |
| [SRC-4FFD5AFC54-L000430](../../scripts/run_answer_quality_benchmark.py#L430) | 430 | `"        except json.JSONDecodeError:"` | — |
| [SRC-4FFD5AFC54-L000431](../../scripts/run_answer_quality_benchmark.py#L431) | 431 | `"            return exc.code, raw"` | — |
| [SRC-4FFD5AFC54-L000432](../../scripts/run_answer_quality_benchmark.py#L432) | 432 | `"    except ValueError as exc:"` | — |
| [SRC-4FFD5AFC54-L000433](../../scripts/run_answer_quality_benchmark.py#L433) | 433 | `"        return 0, {\"error\": \"UnsafeBaseURL\", \"detail\": str(exc)}"` | — |
| [SRC-4FFD5AFC54-L000434](../../scripts/run_answer_quality_benchmark.py#L434) | 434 | `"    except (urllib.error.URLError, TimeoutError, OSError) as exc:"` | — |
| [SRC-4FFD5AFC54-L000435](../../scripts/run_answer_quality_benchmark.py#L435) | 435 | `"        return 0, {\"error\": type(exc).__name__, \"detail\": str(exc)}"` | — |
| [SRC-4FFD5AFC54-L000436](../../scripts/run_answer_quality_benchmark.py#L436) | 436 | `""` | — |
| [SRC-4FFD5AFC54-L000437](../../scripts/run_answer_quality_benchmark.py#L437) | 437 | `""` | — |
| [SRC-4FFD5AFC54-L000438](../../scripts/run_answer_quality_benchmark.py#L438) | 438 | `"def get_verified_build_sha(base_url: str, timeout: float, token: str \| None = None) -> str:"` | — |
| [SRC-4FFD5AFC54-L000439](../../scripts/run_answer_quality_benchmark.py#L439) | 439 | `"    \"\"\"Read the deployed build identity from /api/health; never trust a caller-only SHA.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000440](../../scripts/run_answer_quality_benchmark.py#L440) | 440 | `"    origin = validate_base_url(base_url, token_present=bool(token))"` | — |
| [SRC-4FFD5AFC54-L000441](../../scripts/run_answer_quality_benchmark.py#L441) | 441 | `"    request = urllib.request.Request("` | — |
| [SRC-4FFD5AFC54-L000442](../../scripts/run_answer_quality_benchmark.py#L442) | 442 | `"        origin + \"/api/health\","` | — |
| [SRC-4FFD5AFC54-L000443](../../scripts/run_answer_quality_benchmark.py#L443) | 443 | `"        headers={\"Accept\": \"application/json\"},"` | — |
| [SRC-4FFD5AFC54-L000444](../../scripts/run_answer_quality_benchmark.py#L444) | 444 | `"        method=\"GET\","` | — |
| [SRC-4FFD5AFC54-L000445](../../scripts/run_answer_quality_benchmark.py#L445) | 445 | `"    )"` | — |
| [SRC-4FFD5AFC54-L000446](../../scripts/run_answer_quality_benchmark.py#L446) | 446 | `"    try:"` | — |
| [SRC-4FFD5AFC54-L000447](../../scripts/run_answer_quality_benchmark.py#L447) | 447 | `"        with _NO_REDIRECT_OPENER.open(request, timeout=timeout) as response:"` | — |
| [SRC-4FFD5AFC54-L000448](../../scripts/run_answer_quality_benchmark.py#L448) | 448 | `"            raw = response.read(64_001)"` | — |
| [SRC-4FFD5AFC54-L000449](../../scripts/run_answer_quality_benchmark.py#L449) | 449 | `"            if len(raw) > 64_000:"` | — |
| [SRC-4FFD5AFC54-L000450](../../scripts/run_answer_quality_benchmark.py#L450) | 450 | `"                raise ValueError(\"/api/health response exceeded the 64 KB limit\")"` | — |
| [SRC-4FFD5AFC54-L000451](../../scripts/run_answer_quality_benchmark.py#L451) | 451 | `"            status = getattr(response, \"status\", 200)"` | — |
| [SRC-4FFD5AFC54-L000452](../../scripts/run_answer_quality_benchmark.py#L452) | 452 | `"            if not 200 <= status < 300:"` | — |
| [SRC-4FFD5AFC54-L000453](../../scripts/run_answer_quality_benchmark.py#L453) | 453 | `"                raise ValueError(f\"/api/health returned HTTP {status}\")"` | — |
| [SRC-4FFD5AFC54-L000454](../../scripts/run_answer_quality_benchmark.py#L454) | 454 | `"    except urllib.error.HTTPError as exc:"` | — |
| [SRC-4FFD5AFC54-L000455](../../scripts/run_answer_quality_benchmark.py#L455) | 455 | `"        raise ValueError(f\"/api/health returned HTTP {exc.code}\") from exc"` | — |
| [SRC-4FFD5AFC54-L000456](../../scripts/run_answer_quality_benchmark.py#L456) | 456 | `"    except (urllib.error.URLError, TimeoutError, OSError) as exc:"` | — |
| [SRC-4FFD5AFC54-L000457](../../scripts/run_answer_quality_benchmark.py#L457) | 457 | `"        raise ValueError(f\"/api/health request failed: {type(exc).__name__}\") from exc"` | — |
| [SRC-4FFD5AFC54-L000458](../../scripts/run_answer_quality_benchmark.py#L458) | 458 | `""` | — |
| [SRC-4FFD5AFC54-L000459](../../scripts/run_answer_quality_benchmark.py#L459) | 459 | `"    try:"` | — |
| [SRC-4FFD5AFC54-L000460](../../scripts/run_answer_quality_benchmark.py#L460) | 460 | `"        payload = json.loads(raw.decode(\"utf-8\"))"` | — |
| [SRC-4FFD5AFC54-L000461](../../scripts/run_answer_quality_benchmark.py#L461) | 461 | `"    except (UnicodeDecodeError, json.JSONDecodeError) as exc:"` | — |
| [SRC-4FFD5AFC54-L000462](../../scripts/run_answer_quality_benchmark.py#L462) | 462 | `"        raise ValueError(\"/api/health did not return valid JSON\") from exc"` | — |
| [SRC-4FFD5AFC54-L000463](../../scripts/run_answer_quality_benchmark.py#L463) | 463 | `"    if not isinstance(payload, dict) or payload.get(\"ok\") is not True:"` | — |
| [SRC-4FFD5AFC54-L000464](../../scripts/run_answer_quality_benchmark.py#L464) | 464 | `"        raise ValueError(\"/api/health did not report ok=true\")"` | — |
| [SRC-4FFD5AFC54-L000465](../../scripts/run_answer_quality_benchmark.py#L465) | 465 | `"    build = payload.get(\"build\")"` | — |
| [SRC-4FFD5AFC54-L000466](../../scripts/run_answer_quality_benchmark.py#L466) | 466 | `"    sha = build.get(\"sha\") if isinstance(build, dict) else None"` | — |
| [SRC-4FFD5AFC54-L000467](../../scripts/run_answer_quality_benchmark.py#L467) | 467 | `"    if not isinstance(sha, str) or not re.fullmatch(r\"[0-9a-fA-F]{40}\", sha):"` | — |
| [SRC-4FFD5AFC54-L000468](../../scripts/run_answer_quality_benchmark.py#L468) | 468 | `"        raise ValueError(\"/api/health build.sha is missing or not a full 40-character SHA\")"` | — |
| [SRC-4FFD5AFC54-L000469](../../scripts/run_answer_quality_benchmark.py#L469) | 469 | `"    return sha.lower()"` | — |
| [SRC-4FFD5AFC54-L000470](../../scripts/run_answer_quality_benchmark.py#L470) | 470 | `""` | — |
| [SRC-4FFD5AFC54-L000471](../../scripts/run_answer_quality_benchmark.py#L471) | 471 | `""` | — |
| [SRC-4FFD5AFC54-L000472](../../scripts/run_answer_quality_benchmark.py#L472) | 472 | `"def run_validate(corpus_path: Path, summary: bool) -> int:"` | — |
| [SRC-4FFD5AFC54-L000473](../../scripts/run_answer_quality_benchmark.py#L473) | 473 | `"    data = load_corpus(corpus_path)"` | — |
| [SRC-4FFD5AFC54-L000474](../../scripts/run_answer_quality_benchmark.py#L474) | 474 | `"    problems = validate_corpus(data)"` | — |
| [SRC-4FFD5AFC54-L000475](../../scripts/run_answer_quality_benchmark.py#L475) | 475 | `"    if problems:"` | — |
| [SRC-4FFD5AFC54-L000476](../../scripts/run_answer_quality_benchmark.py#L476) | 476 | `"        print(\"VALIDATE FAIL\")"` | — |
| [SRC-4FFD5AFC54-L000477](../../scripts/run_answer_quality_benchmark.py#L477) | 477 | `"        for p in problems:"` | — |
| [SRC-4FFD5AFC54-L000478](../../scripts/run_answer_quality_benchmark.py#L478) | 478 | `"            print(\" -\", p)"` | — |
| [SRC-4FFD5AFC54-L000479](../../scripts/run_answer_quality_benchmark.py#L479) | 479 | `"        return 1"` | — |
| [SRC-4FFD5AFC54-L000480](../../scripts/run_answer_quality_benchmark.py#L480) | 480 | `"    cases = data[\"cases\"]"` | — |
| [SRC-4FFD5AFC54-L000481](../../scripts/run_answer_quality_benchmark.py#L481) | 481 | `"    cats = sorted({c[\"category\"] for c in cases})"` | — |
| [SRC-4FFD5AFC54-L000482](../../scripts/run_answer_quality_benchmark.py#L482) | 482 | `"    langs = sorted({c[\"language\"] for c in cases})"` | — |
| [SRC-4FFD5AFC54-L000483](../../scripts/run_answer_quality_benchmark.py#L483) | 483 | `"    print(\"VALIDATE OK\")"` | — |
| [SRC-4FFD5AFC54-L000484](../../scripts/run_answer_quality_benchmark.py#L484) | 484 | `"    print(f\"benchmark_id={data.get('benchmark_id')} version={data.get('version')}\")"` | — |
| [SRC-4FFD5AFC54-L000485](../../scripts/run_answer_quality_benchmark.py#L485) | 485 | `"    print(f\"cases={len(cases)} categories={len(cats)} languages={langs}\")"` | — |
| [SRC-4FFD5AFC54-L000486](../../scripts/run_answer_quality_benchmark.py#L486) | 486 | `"    if summary:"` | — |
| [SRC-4FFD5AFC54-L000487](../../scripts/run_answer_quality_benchmark.py#L487) | 487 | `"        from collections import Counter"` | — |
| [SRC-4FFD5AFC54-L000488](../../scripts/run_answer_quality_benchmark.py#L488) | 488 | `""` | — |
| [SRC-4FFD5AFC54-L000489](../../scripts/run_answer_quality_benchmark.py#L489) | 489 | `"        print(\"strategies:\", dict(Counter(c[\"expected_strategy\"] for c in cases)))"` | — |
| [SRC-4FFD5AFC54-L000490](../../scripts/run_answer_quality_benchmark.py#L490) | 490 | `"        print(\"eval_modes:\", dict(Counter(c[\"evaluation_mode\"] for c in cases)))"` | — |
| [SRC-4FFD5AFC54-L000491](../../scripts/run_answer_quality_benchmark.py#L491) | 491 | `"        print(\"categories:\", \", \".join(cats))"` | — |
| [SRC-4FFD5AFC54-L000492](../../scripts/run_answer_quality_benchmark.py#L492) | 492 | `"    print("` | — |
| [SRC-4FFD5AFC54-L000493](../../scripts/run_answer_quality_benchmark.py#L493) | 493 | `"        \"NOTE: Structural validation is not answer-quality evaluation. \""` | — |
| [SRC-4FFD5AFC54-L000494](../../scripts/run_answer_quality_benchmark.py#L494) | 494 | `"        \"All reasoning cases remain NOT_TESTED until reviewed.\""` | — |
| [SRC-4FFD5AFC54-L000495](../../scripts/run_answer_quality_benchmark.py#L495) | 495 | `"    )"` | — |
| [SRC-4FFD5AFC54-L000496](../../scripts/run_answer_quality_benchmark.py#L496) | 496 | `"    return 0"` | — |
| [SRC-4FFD5AFC54-L000497](../../scripts/run_answer_quality_benchmark.py#L497) | 497 | `""` | — |
| [SRC-4FFD5AFC54-L000498](../../scripts/run_answer_quality_benchmark.py#L498) | 498 | `""` | — |
| [SRC-4FFD5AFC54-L000499](../../scripts/run_answer_quality_benchmark.py#L499) | 499 | `"def run_live("` | — |
| [SRC-4FFD5AFC54-L000500](../../scripts/run_answer_quality_benchmark.py#L500) | 500 | `"    corpus_path: Path,"` | — |
| [SRC-4FFD5AFC54-L000501](../../scripts/run_answer_quality_benchmark.py#L501) | 501 | `"    base_url: str,"` | — |
| [SRC-4FFD5AFC54-L000502](../../scripts/run_answer_quality_benchmark.py#L502) | 502 | `"    case_id: str \| None,"` | — |
| [SRC-4FFD5AFC54-L000503](../../scripts/run_answer_quality_benchmark.py#L503) | 503 | `"    limit: int,"` | — |
| [SRC-4FFD5AFC54-L000504](../../scripts/run_answer_quality_benchmark.py#L504) | 504 | `"    timeout: float,"` | — |
| [SRC-4FFD5AFC54-L000505](../../scripts/run_answer_quality_benchmark.py#L505) | 505 | `"    delay: float,"` | — |
| [SRC-4FFD5AFC54-L000506](../../scripts/run_answer_quality_benchmark.py#L506) | 506 | `"    out_path: Path \| None,"` | — |
| [SRC-4FFD5AFC54-L000507](../../scripts/run_answer_quality_benchmark.py#L507) | 507 | `"    build_sha: str \| None = None,"` | — |
| [SRC-4FFD5AFC54-L000508](../../scripts/run_answer_quality_benchmark.py#L508) | 508 | `"    request_costs_path: Path \| None = None,"` | — |
| [SRC-4FFD5AFC54-L000509](../../scripts/run_answer_quality_benchmark.py#L509) | 509 | `") -> int:"` | — |
| [SRC-4FFD5AFC54-L000510](../../scripts/run_answer_quality_benchmark.py#L510) | 510 | `"    data = load_corpus(corpus_path)"` | — |
| [SRC-4FFD5AFC54-L000511](../../scripts/run_answer_quality_benchmark.py#L511) | 511 | `"    problems = validate_corpus(data)"` | — |
| [SRC-4FFD5AFC54-L000512](../../scripts/run_answer_quality_benchmark.py#L512) | 512 | `"    if problems:"` | — |
| [SRC-4FFD5AFC54-L000513](../../scripts/run_answer_quality_benchmark.py#L513) | 513 | `"        print(\"Corpus invalid; refusing live run:\")"` | — |
| [SRC-4FFD5AFC54-L000514](../../scripts/run_answer_quality_benchmark.py#L514) | 514 | `"        for p in problems:"` | — |
| [SRC-4FFD5AFC54-L000515](../../scripts/run_answer_quality_benchmark.py#L515) | 515 | `"            print(\" -\", p)"` | — |
| [SRC-4FFD5AFC54-L000516](../../scripts/run_answer_quality_benchmark.py#L516) | 516 | `"        return 2"` | — |
| [SRC-4FFD5AFC54-L000517](../../scripts/run_answer_quality_benchmark.py#L517) | 517 | `""` | — |
| [SRC-4FFD5AFC54-L000518](../../scripts/run_answer_quality_benchmark.py#L518) | 518 | `"    try:"` | — |
| [SRC-4FFD5AFC54-L000519](../../scripts/run_answer_quality_benchmark.py#L519) | 519 | `"        full_case_ids = {case.get(\"case_id\") for case in data.get(\"cases\", []) if isinstance(case, dict)}"` | — |
| [SRC-4FFD5AFC54-L000520](../../scripts/run_answer_quality_benchmark.py#L520) | 520 | `"        request_costs, request_cost_source = _load_request_cost_ledger(request_costs_path, full_case_ids)"` | — |
| [SRC-4FFD5AFC54-L000521](../../scripts/run_answer_quality_benchmark.py#L521) | 521 | `"    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:"` | — |
| [SRC-4FFD5AFC54-L000522](../../scripts/run_answer_quality_benchmark.py#L522) | 522 | `"        print(f\"Invalid request-cost ledger; refusing live run: {exc}\", file=sys.stderr)"` | — |
| [SRC-4FFD5AFC54-L000523](../../scripts/run_answer_quality_benchmark.py#L523) | 523 | `"        return 2"` | — |
| [SRC-4FFD5AFC54-L000524](../../scripts/run_answer_quality_benchmark.py#L524) | 524 | `""` | — |
| [SRC-4FFD5AFC54-L000525](../../scripts/run_answer_quality_benchmark.py#L525) | 525 | `"    token = os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip() or None"` | — |
| [SRC-4FFD5AFC54-L000526](../../scripts/run_answer_quality_benchmark.py#L526) | 526 | `"    try:"` | — |
| [SRC-4FFD5AFC54-L000527](../../scripts/run_answer_quality_benchmark.py#L527) | 527 | `"        safe_base_url = validate_base_url(base_url, token_present=bool(token))"` | — |
| [SRC-4FFD5AFC54-L000528](../../scripts/run_answer_quality_benchmark.py#L528) | 528 | `"    except ValueError as exc:"` | — |
| [SRC-4FFD5AFC54-L000529](../../scripts/run_answer_quality_benchmark.py#L529) | 529 | `"        print(f\"Unsafe base URL; refusing live run: {exc}\", file=sys.stderr)"` | — |
| [SRC-4FFD5AFC54-L000530](../../scripts/run_answer_quality_benchmark.py#L530) | 530 | `"        return 2"` | — |
| [SRC-4FFD5AFC54-L000531](../../scripts/run_answer_quality_benchmark.py#L531) | 531 | `"    try:"` | — |
| [SRC-4FFD5AFC54-L000532](../../scripts/run_answer_quality_benchmark.py#L532) | 532 | `"        verified_build_sha = get_verified_build_sha(safe_base_url, timeout, token)"` | — |
| [SRC-4FFD5AFC54-L000533](../../scripts/run_answer_quality_benchmark.py#L533) | 533 | `"    except ValueError as exc:"` | — |
| [SRC-4FFD5AFC54-L000534](../../scripts/run_answer_quality_benchmark.py#L534) | 534 | `"        print(f\"Unverified deployed build; refusing live run: {exc}\", file=sys.stderr)"` | — |
| [SRC-4FFD5AFC54-L000535](../../scripts/run_answer_quality_benchmark.py#L535) | 535 | `"        return 2"` | — |
| [SRC-4FFD5AFC54-L000536](../../scripts/run_answer_quality_benchmark.py#L536) | 536 | `"    expected_build_sha = build_sha.strip().lower() if isinstance(build_sha, str) else \"\""` | — |
| [SRC-4FFD5AFC54-L000537](../../scripts/run_answer_quality_benchmark.py#L537) | 537 | `"    if expected_build_sha and expected_build_sha != verified_build_sha:"` | — |
| [SRC-4FFD5AFC54-L000538](../../scripts/run_answer_quality_benchmark.py#L538) | 538 | `"        print("` | — |
| [SRC-4FFD5AFC54-L000539](../../scripts/run_answer_quality_benchmark.py#L539) | 539 | `"            \"Build SHA mismatch: --build-sha does not match /api/health build.sha; \""` | — |
| [SRC-4FFD5AFC54-L000540](../../scripts/run_answer_quality_benchmark.py#L540) | 540 | `"            \"refusing live requests.\","` | — |
| [SRC-4FFD5AFC54-L000541](../../scripts/run_answer_quality_benchmark.py#L541) | 541 | `"            file=sys.stderr,"` | — |
| [SRC-4FFD5AFC54-L000542](../../scripts/run_answer_quality_benchmark.py#L542) | 542 | `"        )"` | — |
| [SRC-4FFD5AFC54-L000543](../../scripts/run_answer_quality_benchmark.py#L543) | 543 | `"        return 2"` | — |
| [SRC-4FFD5AFC54-L000544](../../scripts/run_answer_quality_benchmark.py#L544) | 544 | `"    cases = data[\"cases\"]"` | — |
| [SRC-4FFD5AFC54-L000545](../../scripts/run_answer_quality_benchmark.py#L545) | 545 | `"    if case_id:"` | — |
| [SRC-4FFD5AFC54-L000546](../../scripts/run_answer_quality_benchmark.py#L546) | 546 | `"        cases = [c for c in cases if c[\"case_id\"] == case_id]"` | — |
| [SRC-4FFD5AFC54-L000547](../../scripts/run_answer_quality_benchmark.py#L547) | 547 | `"        if not cases:"` | — |
| [SRC-4FFD5AFC54-L000548](../../scripts/run_answer_quality_benchmark.py#L548) | 548 | `"            print(f\"Unknown case_id: {case_id}\", file=sys.stderr)"` | — |
| [SRC-4FFD5AFC54-L000549](../../scripts/run_answer_quality_benchmark.py#L549) | 549 | `"            return 2"` | — |
| [SRC-4FFD5AFC54-L000550](../../scripts/run_answer_quality_benchmark.py#L550) | 550 | `"    if limit > 0:"` | — |
| [SRC-4FFD5AFC54-L000551](../../scripts/run_answer_quality_benchmark.py#L551) | 551 | `"        cases = cases[:limit]"` | — |
| [SRC-4FFD5AFC54-L000552](../../scripts/run_answer_quality_benchmark.py#L552) | 552 | `""` | — |
| [SRC-4FFD5AFC54-L000553](../../scripts/run_answer_quality_benchmark.py#L553) | 553 | `"    results = []"` | — |
| [SRC-4FFD5AFC54-L000554](../../scripts/run_answer_quality_benchmark.py#L554) | 554 | `"    print("` | — |
| [SRC-4FFD5AFC54-L000555](../../scripts/run_answer_quality_benchmark.py#L555) | 555 | `"        \"LIVE mode: fixtures are NOT injected into the server. \""` | — |
| [SRC-4FFD5AFC54-L000556](../../scripts/run_answer_quality_benchmark.py#L556) | 556 | `"        \"Answers are recorded as NOT_TESTED (quality) unless transport fails.\""` | — |
| [SRC-4FFD5AFC54-L000557](../../scripts/run_answer_quality_benchmark.py#L557) | 557 | `"    )"` | — |
| [SRC-4FFD5AFC54-L000558](../../scripts/run_answer_quality_benchmark.py#L558) | 558 | `"    for case in cases:"` | — |
| [SRC-4FFD5AFC54-L000559](../../scripts/run_answer_quality_benchmark.py#L559) | 559 | `"        cid = case[\"case_id\"]"` | — |
| [SRC-4FFD5AFC54-L000560](../../scripts/run_answer_quality_benchmark.py#L560) | 560 | `"        prompt = case[\"question\"]"` | — |
| [SRC-4FFD5AFC54-L000561](../../scripts/run_answer_quality_benchmark.py#L561) | 561 | `"        request_started = time.perf_counter()"` | — |
| [SRC-4FFD5AFC54-L000562](../../scripts/run_answer_quality_benchmark.py#L562) | 562 | `"        status_code, payload = post_agent(safe_base_url, prompt, timeout, token)"` | — |
| [SRC-4FFD5AFC54-L000563](../../scripts/run_answer_quality_benchmark.py#L563) | 563 | `"        elapsed_ms = round((time.perf_counter() - request_started) * 1000, 2)"` | — |
| [SRC-4FFD5AFC54-L000564](../../scripts/run_answer_quality_benchmark.py#L564) | 564 | `"        if isinstance(payload, dict):"` | — |
| [SRC-4FFD5AFC54-L000565](../../scripts/run_answer_quality_benchmark.py#L565) | 565 | `"            safe_payload = json.loads(redact_secrets(json.dumps(payload, ensure_ascii=False)))"` | — |
| [SRC-4FFD5AFC54-L000566](../../scripts/run_answer_quality_benchmark.py#L566) | 566 | `"        else:"` | — |
| [SRC-4FFD5AFC54-L000567](../../scripts/run_answer_quality_benchmark.py#L567) | 567 | `"            safe_payload = redact_secrets(str(payload))"` | — |
| [SRC-4FFD5AFC54-L000568](../../scripts/run_answer_quality_benchmark.py#L568) | 568 | `""` | — |
| [SRC-4FFD5AFC54-L000569](../../scripts/run_answer_quality_benchmark.py#L569) | 569 | `"        transport_ok = 200 <= status_code < 300"` | — |
| [SRC-4FFD5AFC54-L000570](../../scripts/run_answer_quality_benchmark.py#L570) | 570 | `"        response_metrics = _response_metrics(safe_payload, case[\"expected_strategy\"], transport_ok)"` | — |
| [SRC-4FFD5AFC54-L000571](../../scripts/run_answer_quality_benchmark.py#L571) | 571 | `"        if request_cost_source is not None:"` | — |
| [SRC-4FFD5AFC54-L000572](../../scripts/run_answer_quality_benchmark.py#L572) | 572 | `"            if cid in request_costs:"` | — |
| [SRC-4FFD5AFC54-L000573](../../scripts/run_answer_quality_benchmark.py#L573) | 573 | `"                response_metrics[\"request_cost_usd\"] = request_costs[cid]"` | — |
| [SRC-4FFD5AFC54-L000574](../../scripts/run_answer_quality_benchmark.py#L574) | 574 | `"                response_metrics[\"request_cost_status\"] = \"RECONCILED_COMPLETE_REQUEST_COST\""` | — |
| [SRC-4FFD5AFC54-L000575](../../scripts/run_answer_quality_benchmark.py#L575) | 575 | `"                response_metrics[\"request_cost_source\"] = request_cost_source"` | — |
| [SRC-4FFD5AFC54-L000576](../../scripts/run_answer_quality_benchmark.py#L576) | 576 | `"            else:"` | — |
| [SRC-4FFD5AFC54-L000577](../../scripts/run_answer_quality_benchmark.py#L577) | 577 | `"                response_metrics[\"request_cost_status\"] = \"PARTIAL_EXTERNAL_COST_RECONCILIATION\""` | — |
| [SRC-4FFD5AFC54-L000578](../../scripts/run_answer_quality_benchmark.py#L578) | 578 | `"                response_metrics[\"request_cost_source\"] = request_cost_source"` | — |
| [SRC-4FFD5AFC54-L000579](../../scripts/run_answer_quality_benchmark.py#L579) | 579 | `"        record = {"` | — |
| [SRC-4FFD5AFC54-L000580](../../scripts/run_answer_quality_benchmark.py#L580) | 580 | `"            \"case_id\": cid,"` | — |
| [SRC-4FFD5AFC54-L000581](../../scripts/run_answer_quality_benchmark.py#L581) | 581 | `"            \"benchmark_version\": data.get(\"version\"),"` | — |
| [SRC-4FFD5AFC54-L000582](../../scripts/run_answer_quality_benchmark.py#L582) | 582 | `"            \"benchmark_id\": data.get(\"benchmark_id\"),"` | — |
| [SRC-4FFD5AFC54-L000583](../../scripts/run_answer_quality_benchmark.py#L583) | 583 | `"            \"executed_at_utc\": _utc_now(),"` | — |
| [SRC-4FFD5AFC54-L000584](../../scripts/run_answer_quality_benchmark.py#L584) | 584 | `"            \"mode\": \"live_api\","` | — |
| [SRC-4FFD5AFC54-L000585](../../scripts/run_answer_quality_benchmark.py#L585) | 585 | `"            \"base_url\": safe_base_url,"` | — |
| [SRC-4FFD5AFC54-L000586](../../scripts/run_answer_quality_benchmark.py#L586) | 586 | `"            \"http_status\": status_code,"` | — |
| [SRC-4FFD5AFC54-L000587](../../scripts/run_answer_quality_benchmark.py#L587) | 587 | `"            \"elapsed_ms\": elapsed_ms,"` | — |
| [SRC-4FFD5AFC54-L000588](../../scripts/run_answer_quality_benchmark.py#L588) | 588 | `"            \"build_sha\": verified_build_sha,"` | — |
| [SRC-4FFD5AFC54-L000589](../../scripts/run_answer_quality_benchmark.py#L589) | 589 | `"            \"build_sha_verification\": \"confirmed_by_api_health\","` | — |
| [SRC-4FFD5AFC54-L000590](../../scripts/run_answer_quality_benchmark.py#L590) | 590 | `"            **response_metrics,"` | — |
| [SRC-4FFD5AFC54-L000591](../../scripts/run_answer_quality_benchmark.py#L591) | 591 | `"            \"prompt\": prompt,"` | — |
| [SRC-4FFD5AFC54-L000592](../../scripts/run_answer_quality_benchmark.py#L592) | 592 | `"            \"expected_strategy\": case[\"expected_strategy\"],"` | — |
| [SRC-4FFD5AFC54-L000593](../../scripts/run_answer_quality_benchmark.py#L593) | 593 | `"            \"category\": case[\"category\"],"` | — |
| [SRC-4FFD5AFC54-L000594](../../scripts/run_answer_quality_benchmark.py#L594) | 594 | `"            \"response\": safe_payload,"` | — |
| [SRC-4FFD5AFC54-L000595](../../scripts/run_answer_quality_benchmark.py#L595) | 595 | `"            \"used_web_search\": ("` | — |
| [SRC-4FFD5AFC54-L000596](../../scripts/run_answer_quality_benchmark.py#L596) | 596 | `"                safe_payload.get(\"used_web_search\") if isinstance(safe_payload, dict) else None"` | — |
| [SRC-4FFD5AFC54-L000597](../../scripts/run_answer_quality_benchmark.py#L597) | 597 | `"            ),"` | — |
| [SRC-4FFD5AFC54-L000598](../../scripts/run_answer_quality_benchmark.py#L598) | 598 | `"            \"used_language_model\": ("` | — |
| [SRC-4FFD5AFC54-L000599](../../scripts/run_answer_quality_benchmark.py#L599) | 599 | `"                safe_payload.get(\"used_language_model\")"` | — |
| [SRC-4FFD5AFC54-L000600](../../scripts/run_answer_quality_benchmark.py#L600) | 600 | `"                if isinstance(safe_payload, dict)"` | — |
| [SRC-4FFD5AFC54-L000601](../../scripts/run_answer_quality_benchmark.py#L601) | 601 | `"                else None"` | — |
| [SRC-4FFD5AFC54-L000602](../../scripts/run_answer_quality_benchmark.py#L602) | 602 | `"            ),"` | — |
| [SRC-4FFD5AFC54-L000603](../../scripts/run_answer_quality_benchmark.py#L603) | 603 | `"            \"sources\": ("` | — |
| [SRC-4FFD5AFC54-L000604](../../scripts/run_answer_quality_benchmark.py#L604) | 604 | `"                safe_payload.get(\"sources\") if isinstance(safe_payload, dict) else None"` | — |
| [SRC-4FFD5AFC54-L000605](../../scripts/run_answer_quality_benchmark.py#L605) | 605 | `"            ),"` | — |
| [SRC-4FFD5AFC54-L000606](../../scripts/run_answer_quality_benchmark.py#L606) | 606 | `"            \"status\": \"NOT_TESTED\","` | — |
| [SRC-4FFD5AFC54-L000607](../../scripts/run_answer_quality_benchmark.py#L607) | 607 | `"            \"transport_ok\": transport_ok,"` | — |
| [SRC-4FFD5AFC54-L000608](../../scripts/run_answer_quality_benchmark.py#L608) | 608 | `"            \"reviewer_notes\": ("` | — |
| [SRC-4FFD5AFC54-L000609](../../scripts/run_answer_quality_benchmark.py#L609) | 609 | `"                \"Response collected; human/fixture review required for PASS/FAIL.\""` | — |
| [SRC-4FFD5AFC54-L000610](../../scripts/run_answer_quality_benchmark.py#L610) | 610 | `"                if transport_ok"` | — |
| [SRC-4FFD5AFC54-L000611](../../scripts/run_answer_quality_benchmark.py#L611) | 611 | `"                else \"Transport or HTTP error; quality not graded.\""` | — |
| [SRC-4FFD5AFC54-L000612](../../scripts/run_answer_quality_benchmark.py#L612) | 612 | `"            ),"` | — |
| [SRC-4FFD5AFC54-L000613](../../scripts/run_answer_quality_benchmark.py#L613) | 613 | `"            \"evidence_fixture_injected\": False,"` | — |
| [SRC-4FFD5AFC54-L000614](../../scripts/run_answer_quality_benchmark.py#L614) | 614 | `"        }"` | — |
| [SRC-4FFD5AFC54-L000615](../../scripts/run_answer_quality_benchmark.py#L615) | 615 | `"        results.append(record)"` | — |
| [SRC-4FFD5AFC54-L000616](../../scripts/run_answer_quality_benchmark.py#L616) | 616 | `"        flag = \"OK\" if transport_ok else \"ERR\""` | — |
| [SRC-4FFD5AFC54-L000617](../../scripts/run_answer_quality_benchmark.py#L617) | 617 | `"        print(f\"[{flag}] {cid} http={status_code}\")"` | — |
| [SRC-4FFD5AFC54-L000618](../../scripts/run_answer_quality_benchmark.py#L618) | 618 | `"        if delay > 0:"` | — |
| [SRC-4FFD5AFC54-L000619](../../scripts/run_answer_quality_benchmark.py#L619) | 619 | `"            time.sleep(delay)"` | — |
| [SRC-4FFD5AFC54-L000620](../../scripts/run_answer_quality_benchmark.py#L620) | 620 | `""` | — |
| [SRC-4FFD5AFC54-L000621](../../scripts/run_answer_quality_benchmark.py#L621) | 621 | `"    envelope = {"` | — |
| [SRC-4FFD5AFC54-L000622](../../scripts/run_answer_quality_benchmark.py#L622) | 622 | `"        \"benchmark_id\": data.get(\"benchmark_id\"),"` | — |
| [SRC-4FFD5AFC54-L000623](../../scripts/run_answer_quality_benchmark.py#L623) | 623 | `"        \"benchmark_version\": data.get(\"version\"),"` | — |
| [SRC-4FFD5AFC54-L000624](../../scripts/run_answer_quality_benchmark.py#L624) | 624 | `"        \"mode\": \"live_api\","` | — |
| [SRC-4FFD5AFC54-L000625](../../scripts/run_answer_quality_benchmark.py#L625) | 625 | `"        \"build_sha\": verified_build_sha,"` | — |
| [SRC-4FFD5AFC54-L000626](../../scripts/run_answer_quality_benchmark.py#L626) | 626 | `"        \"build_sha_verification\": \"confirmed_by_api_health\","` | — |
| [SRC-4FFD5AFC54-L000627](../../scripts/run_answer_quality_benchmark.py#L627) | 627 | `"        \"expected_build_sha\": expected_build_sha or None,"` | — |
| [SRC-4FFD5AFC54-L000628](../../scripts/run_answer_quality_benchmark.py#L628) | 628 | `"        \"executed_at_utc\": _utc_now(),"` | — |
| [SRC-4FFD5AFC54-L000629](../../scripts/run_answer_quality_benchmark.py#L629) | 629 | `"        \"case_count\": len(results),"` | — |
| [SRC-4FFD5AFC54-L000630](../../scripts/run_answer_quality_benchmark.py#L630) | 630 | `"        \"results\": results,"` | — |
| [SRC-4FFD5AFC54-L000631](../../scripts/run_answer_quality_benchmark.py#L631) | 631 | `"        \"disclaimer\": ("` | — |
| [SRC-4FFD5AFC54-L000632](../../scripts/run_answer_quality_benchmark.py#L632) | 632 | `"            \"status=NOT_TESTED means answer quality was not auto-graded. \""` | — |
| [SRC-4FFD5AFC54-L000633](../../scripts/run_answer_quality_benchmark.py#L633) | 633 | `"            \"Fixtures in JSON were not applied to the live server.\""` | — |
| [SRC-4FFD5AFC54-L000634](../../scripts/run_answer_quality_benchmark.py#L634) | 634 | `"        ),"` | — |
| [SRC-4FFD5AFC54-L000635](../../scripts/run_answer_quality_benchmark.py#L635) | 635 | `"    }"` | — |
| [SRC-4FFD5AFC54-L000636](../../scripts/run_answer_quality_benchmark.py#L636) | 636 | `"    text = json.dumps(envelope, ensure_ascii=False, indent=2)"` | — |
| [SRC-4FFD5AFC54-L000637](../../scripts/run_answer_quality_benchmark.py#L637) | 637 | `"    if out_path:"` | — |
| [SRC-4FFD5AFC54-L000638](../../scripts/run_answer_quality_benchmark.py#L638) | 638 | `"        out_path.write_text(text + \"\\n\", encoding=\"utf-8\")"` | — |
| [SRC-4FFD5AFC54-L000639](../../scripts/run_answer_quality_benchmark.py#L639) | 639 | `"        print(f\"Wrote {out_path}\")"` | — |
| [SRC-4FFD5AFC54-L000640](../../scripts/run_answer_quality_benchmark.py#L640) | 640 | `"    else:"` | — |
| [SRC-4FFD5AFC54-L000641](../../scripts/run_answer_quality_benchmark.py#L641) | 641 | `"        print(text)"` | — |
| [SRC-4FFD5AFC54-L000642](../../scripts/run_answer_quality_benchmark.py#L642) | 642 | `"    return 0"` | — |
| [SRC-4FFD5AFC54-L000643](../../scripts/run_answer_quality_benchmark.py#L643) | 643 | `""` | — |
| [SRC-4FFD5AFC54-L000644](../../scripts/run_answer_quality_benchmark.py#L644) | 644 | `""` | — |
| [SRC-4FFD5AFC54-L000645](../../scripts/run_answer_quality_benchmark.py#L645) | 645 | `"def main(argv: list[str] \| None = None) -> int:"` | — |
| [SRC-4FFD5AFC54-L000646](../../scripts/run_answer_quality_benchmark.py#L646) | 646 | `"    parser = argparse.ArgumentParser(description=\"Omarai answer-quality benchmark runner\")"` | — |
| [SRC-4FFD5AFC54-L000647](../../scripts/run_answer_quality_benchmark.py#L647) | 647 | `"    parser.add_argument("` | — |
| [SRC-4FFD5AFC54-L000648](../../scripts/run_answer_quality_benchmark.py#L648) | 648 | `"        \"--mode\","` | — |
| [SRC-4FFD5AFC54-L000649](../../scripts/run_answer_quality_benchmark.py#L649) | 649 | `"        choices=(\"validate\", \"live\"),"` | — |
| [SRC-4FFD5AFC54-L000650](../../scripts/run_answer_quality_benchmark.py#L650) | 650 | `"        default=\"validate\","` | — |
| [SRC-4FFD5AFC54-L000651](../../scripts/run_answer_quality_benchmark.py#L651) | 651 | `"        help=\"validate=offline corpus check (default); live=opt-in API calls\","` | — |
| [SRC-4FFD5AFC54-L000652](../../scripts/run_answer_quality_benchmark.py#L652) | 652 | `"    )"` | — |
| [SRC-4FFD5AFC54-L000653](../../scripts/run_answer_quality_benchmark.py#L653) | 653 | `"    parser.add_argument("` | — |
| [SRC-4FFD5AFC54-L000654](../../scripts/run_answer_quality_benchmark.py#L654) | 654 | `"        \"--corpus\","` | — |
| [SRC-4FFD5AFC54-L000655](../../scripts/run_answer_quality_benchmark.py#L655) | 655 | `"        type=Path,"` | — |
| [SRC-4FFD5AFC54-L000656](../../scripts/run_answer_quality_benchmark.py#L656) | 656 | `"        default=DEFAULT_CORPUS,"` | — |
| [SRC-4FFD5AFC54-L000657](../../scripts/run_answer_quality_benchmark.py#L657) | 657 | `"        help=\"Path to answer_quality_cases.json\","` | — |
| [SRC-4FFD5AFC54-L000658](../../scripts/run_answer_quality_benchmark.py#L658) | 658 | `"    )"` | — |
| [SRC-4FFD5AFC54-L000659](../../scripts/run_answer_quality_benchmark.py#L659) | 659 | `"    parser.add_argument(\"--summary\", action=\"store_true\", help=\"Extra validate summary\")"` | — |
| [SRC-4FFD5AFC54-L000660](../../scripts/run_answer_quality_benchmark.py#L660) | 660 | `"    parser.add_argument(\"--base-url\", default=\"http://127.0.0.1:8765\")"` | — |
| [SRC-4FFD5AFC54-L000661](../../scripts/run_answer_quality_benchmark.py#L661) | 661 | `"    parser.add_argument(\"--case-id\", default=None, help=\"Run a single case (live)\")"` | — |
| [SRC-4FFD5AFC54-L000662](../../scripts/run_answer_quality_benchmark.py#L662) | 662 | `"    parser.add_argument(\"--limit\", type=int, default=0, help=\"Max cases in live mode (0=all selected)\")"` | — |
| [SRC-4FFD5AFC54-L000663](../../scripts/run_answer_quality_benchmark.py#L663) | 663 | `"    parser.add_argument(\"--timeout\", type=float, default=60.0)"` | — |
| [SRC-4FFD5AFC54-L000664](../../scripts/run_answer_quality_benchmark.py#L664) | 664 | `"    parser.add_argument(\"--build-sha\", default=None, help=\"Optional expected deployed SHA; checked against /api/health before any benchmark request\")"` | — |
| [SRC-4FFD5AFC54-L000665](../../scripts/run_answer_quality_benchmark.py#L665) | 665 | `"    parser.add_argument(\"--request-costs\", type=Path, default=None, help=\"Optional externally reconciled per-case full-request costs in USD\")"` | — |
| [SRC-4FFD5AFC54-L000666](../../scripts/run_answer_quality_benchmark.py#L666) | 666 | `"    parser.add_argument(\"--delay\", type=float, default=0.0, help=\"Seconds between live requests\")"` | — |
| [SRC-4FFD5AFC54-L000667](../../scripts/run_answer_quality_benchmark.py#L667) | 667 | `"    parser.add_argument(\"--out\", type=Path, default=None, help=\"Write live results JSON\")"` | — |
| [SRC-4FFD5AFC54-L000668](../../scripts/run_answer_quality_benchmark.py#L668) | 668 | `"    args = parser.parse_args(argv)"` | — |
| [SRC-4FFD5AFC54-L000669](../../scripts/run_answer_quality_benchmark.py#L669) | 669 | `""` | — |
| [SRC-4FFD5AFC54-L000670](../../scripts/run_answer_quality_benchmark.py#L670) | 670 | `"    if args.mode == \"validate\":"` | — |
| [SRC-4FFD5AFC54-L000671](../../scripts/run_answer_quality_benchmark.py#L671) | 671 | `"        return run_validate(args.corpus, args.summary)"` | — |
| [SRC-4FFD5AFC54-L000672](../../scripts/run_answer_quality_benchmark.py#L672) | 672 | `"    if args.mode == \"live\":"` | — |
| [SRC-4FFD5AFC54-L000673](../../scripts/run_answer_quality_benchmark.py#L673) | 673 | `"        if not args.case_id and args.limit <= 0:"` | — |
| [SRC-4FFD5AFC54-L000674](../../scripts/run_answer_quality_benchmark.py#L674) | 674 | `"            print("` | — |
| [SRC-4FFD5AFC54-L000675](../../scripts/run_answer_quality_benchmark.py#L675) | 675 | `"                \"Refusing unbounded live run. Pass --case-id and/or --limit > 0.\","` | — |
| [SRC-4FFD5AFC54-L000676](../../scripts/run_answer_quality_benchmark.py#L676) | 676 | `"                file=sys.stderr,"` | — |
| [SRC-4FFD5AFC54-L000677](../../scripts/run_answer_quality_benchmark.py#L677) | 677 | `"            )"` | — |
| [SRC-4FFD5AFC54-L000678](../../scripts/run_answer_quality_benchmark.py#L678) | 678 | `"            return 2"` | — |
| [SRC-4FFD5AFC54-L000679](../../scripts/run_answer_quality_benchmark.py#L679) | 679 | `"        return run_live("` | — |
| [SRC-4FFD5AFC54-L000680](../../scripts/run_answer_quality_benchmark.py#L680) | 680 | `"            args.corpus,"` | — |
| [SRC-4FFD5AFC54-L000681](../../scripts/run_answer_quality_benchmark.py#L681) | 681 | `"            args.base_url,"` | — |
| [SRC-4FFD5AFC54-L000682](../../scripts/run_answer_quality_benchmark.py#L682) | 682 | `"            args.case_id,"` | — |
| [SRC-4FFD5AFC54-L000683](../../scripts/run_answer_quality_benchmark.py#L683) | 683 | `"            args.limit,"` | — |
| [SRC-4FFD5AFC54-L000684](../../scripts/run_answer_quality_benchmark.py#L684) | 684 | `"            args.timeout,"` | — |
| [SRC-4FFD5AFC54-L000685](../../scripts/run_answer_quality_benchmark.py#L685) | 685 | `"            args.delay,"` | — |
| [SRC-4FFD5AFC54-L000686](../../scripts/run_answer_quality_benchmark.py#L686) | 686 | `"            args.out,"` | — |
| [SRC-4FFD5AFC54-L000687](../../scripts/run_answer_quality_benchmark.py#L687) | 687 | `"            args.build_sha,"` | — |
| [SRC-4FFD5AFC54-L000688](../../scripts/run_answer_quality_benchmark.py#L688) | 688 | `"            args.request_costs,"` | — |
| [SRC-4FFD5AFC54-L000689](../../scripts/run_answer_quality_benchmark.py#L689) | 689 | `"        )"` | — |
| [SRC-4FFD5AFC54-L000690](../../scripts/run_answer_quality_benchmark.py#L690) | 690 | `"    return 2"` | — |
| [SRC-4FFD5AFC54-L000691](../../scripts/run_answer_quality_benchmark.py#L691) | 691 | `""` | — |
| [SRC-4FFD5AFC54-L000692](../../scripts/run_answer_quality_benchmark.py#L692) | 692 | `""` | — |
| [SRC-4FFD5AFC54-L000693](../../scripts/run_answer_quality_benchmark.py#L693) | 693 | `"if __name__ == \"__main__\":"` | — |
| [SRC-4FFD5AFC54-L000694](../../scripts/run_answer_quality_benchmark.py#L694) | 694 | `"    raise SystemExit(main())"` | — |
## ملفات أخرى

### FILE-03FF422A16 — [scripts/score_answer_quality_reviews.py](../../scripts/score_answer_quality_reviews.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-03FF422A16-L000001](../../scripts/score_answer_quality_reviews.py#L1) | 1 | `"\"\"\"Score manually reviewed Omarai answer-quality cases without auto-grading."` | — |
| [SRC-03FF422A16-L000002](../../scripts/score_answer_quality_reviews.py#L2) | 2 | `""` | — |
| [SRC-03FF422A16-L000003](../../scripts/score_answer_quality_reviews.py#L3) | 3 | `"This offline tool calculates aggregate retrieval, faithfulness, correctness, citation,"` | — |
| [SRC-03FF422A16-L000004](../../scripts/score_answer_quality_reviews.py#L4) | 4 | `"and writing-quality metrics only from explicit review annotations. Missing judgments"` | — |
| [SRC-03FF422A16-L000005](../../scripts/score_answer_quality_reviews.py#L5) | 5 | `"remain NOT_TESTED; this script never calls an LLM or treats transport success as PASS."` | — |
| [SRC-03FF422A16-L000006](../../scripts/score_answer_quality_reviews.py#L6) | 6 | `"\"\"\""` | — |
| [SRC-03FF422A16-L000007](../../scripts/score_answer_quality_reviews.py#L7) | 7 | `"from __future__ import annotations"` | — |
| [SRC-03FF422A16-L000008](../../scripts/score_answer_quality_reviews.py#L8) | 8 | `""` | — |
| [SRC-03FF422A16-L000009](../../scripts/score_answer_quality_reviews.py#L9) | 9 | `"import argparse"` | — |
| [SRC-03FF422A16-L000010](../../scripts/score_answer_quality_reviews.py#L10) | 10 | `"import json"` | — |
| [SRC-03FF422A16-L000011](../../scripts/score_answer_quality_reviews.py#L11) | 11 | `"import math"` | — |
| [SRC-03FF422A16-L000012](../../scripts/score_answer_quality_reviews.py#L12) | 12 | `"import sys"` | — |
| [SRC-03FF422A16-L000013](../../scripts/score_answer_quality_reviews.py#L13) | 13 | `"from collections import Counter"` | — |
| [SRC-03FF422A16-L000014](../../scripts/score_answer_quality_reviews.py#L14) | 14 | `"from pathlib import Path"` | — |
| [SRC-03FF422A16-L000015](../../scripts/score_answer_quality_reviews.py#L15) | 15 | `"from typing import Any"` | — |
| [SRC-03FF422A16-L000016](../../scripts/score_answer_quality_reviews.py#L16) | 16 | `""` | — |
| [SRC-03FF422A16-L000017](../../scripts/score_answer_quality_reviews.py#L17) | 17 | `"ROOT = Path(__file__).resolve().parents[1]"` | — |
| [SRC-03FF422A16-L000018](../../scripts/score_answer_quality_reviews.py#L18) | 18 | `"DEFAULT_CORPUS = ROOT / \"tests\" / \"fixtures\" / \"answer_quality_cases.json\""` | — |
| [SRC-03FF422A16-L000019](../../scripts/score_answer_quality_reviews.py#L19) | 19 | `"ALLOWED_STATUSES = {\"REVIEWED\", \"NOT_TESTED\", \"BLOCKED\"}"` | — |
| [SRC-03FF422A16-L000020](../../scripts/score_answer_quality_reviews.py#L20) | 20 | `"COUNT_GROUPS = {"` | — |
| [SRC-03FF422A16-L000021](../../scripts/score_answer_quality_reviews.py#L21) | 21 | `"    \"retrieval\": (\"relevant_retrieved\", \"retrieved_count\", \"relevant_available\"),"` | — |
| [SRC-03FF422A16-L000022](../../scripts/score_answer_quality_reviews.py#L22) | 22 | `"    \"faithfulness\": (\"supported_claims\", \"reviewed_claims\"),"` | — |
| [SRC-03FF422A16-L000023](../../scripts/score_answer_quality_reviews.py#L23) | 23 | `"    \"correctness\": (\"correct_facts\", \"reviewed_facts\"),"` | — |
| [SRC-03FF422A16-L000024](../../scripts/score_answer_quality_reviews.py#L24) | 24 | `"    \"citations\": (\"supported_citations\", \"reviewed_citations\"),"` | — |
| [SRC-03FF422A16-L000025](../../scripts/score_answer_quality_reviews.py#L25) | 25 | `"}"` | — |
| [SRC-03FF422A16-L000026](../../scripts/score_answer_quality_reviews.py#L26) | 26 | `""` | — |
| [SRC-03FF422A16-L000027](../../scripts/score_answer_quality_reviews.py#L27) | 27 | `""` | — |
| [SRC-03FF422A16-L000028](../../scripts/score_answer_quality_reviews.py#L28) | 28 | `"def load_json_object(path: Path) -> dict[str, Any]:"` | — |
| [SRC-03FF422A16-L000029](../../scripts/score_answer_quality_reviews.py#L29) | 29 | `"    if not path.is_file():"` | — |
| [SRC-03FF422A16-L000030](../../scripts/score_answer_quality_reviews.py#L30) | 30 | `"        raise FileNotFoundError(\"Input file not found: \" + str(path))"` | — |
| [SRC-03FF422A16-L000031](../../scripts/score_answer_quality_reviews.py#L31) | 31 | `"    data = json.loads(path.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-03FF422A16-L000032](../../scripts/score_answer_quality_reviews.py#L32) | 32 | `"    if not isinstance(data, dict):"` | — |
| [SRC-03FF422A16-L000033](../../scripts/score_answer_quality_reviews.py#L33) | 33 | `"        raise TypeError(\"JSON root must be an object\")"` | — |
| [SRC-03FF422A16-L000034](../../scripts/score_answer_quality_reviews.py#L34) | 34 | `"    return data"` | — |
| [SRC-03FF422A16-L000035](../../scripts/score_answer_quality_reviews.py#L35) | 35 | `""` | — |
| [SRC-03FF422A16-L000036](../../scripts/score_answer_quality_reviews.py#L36) | 36 | `""` | — |
| [SRC-03FF422A16-L000037](../../scripts/score_answer_quality_reviews.py#L37) | 37 | `"def _is_nonnegative_int(value: Any) -> bool:"` | — |
| [SRC-03FF422A16-L000038](../../scripts/score_answer_quality_reviews.py#L38) | 38 | `"    return isinstance(value, int) and not isinstance(value, bool) and value >= 0"` | — |
| [SRC-03FF422A16-L000039](../../scripts/score_answer_quality_reviews.py#L39) | 39 | `""` | — |
| [SRC-03FF422A16-L000040](../../scripts/score_answer_quality_reviews.py#L40) | 40 | `""` | — |
| [SRC-03FF422A16-L000041](../../scripts/score_answer_quality_reviews.py#L41) | 41 | `"def validate_reviews("` | — |
| [SRC-03FF422A16-L000042](../../scripts/score_answer_quality_reviews.py#L42) | 42 | `"    review_data: dict[str, Any], corpus_data: dict[str, Any]"` | — |
| [SRC-03FF422A16-L000043](../../scripts/score_answer_quality_reviews.py#L43) | 43 | `") -> list[str]:"` | — |
| [SRC-03FF422A16-L000044](../../scripts/score_answer_quality_reviews.py#L44) | 44 | `"    problems: list[str] = []"` | — |
| [SRC-03FF422A16-L000045](../../scripts/score_answer_quality_reviews.py#L45) | 45 | `"    reviews = review_data.get(\"reviews\")"` | — |
| [SRC-03FF422A16-L000046](../../scripts/score_answer_quality_reviews.py#L46) | 46 | `"    corpus_cases = corpus_data.get(\"cases\")"` | — |
| [SRC-03FF422A16-L000047](../../scripts/score_answer_quality_reviews.py#L47) | 47 | `"    if not isinstance(reviews, list):"` | — |
| [SRC-03FF422A16-L000048](../../scripts/score_answer_quality_reviews.py#L48) | 48 | `"        return [\"reviews must be an array\"]"` | — |
| [SRC-03FF422A16-L000049](../../scripts/score_answer_quality_reviews.py#L49) | 49 | `"    if not isinstance(corpus_cases, list):"` | — |
| [SRC-03FF422A16-L000050](../../scripts/score_answer_quality_reviews.py#L50) | 50 | `"        return [\"corpus must contain a cases array\"]"` | — |
| [SRC-03FF422A16-L000051](../../scripts/score_answer_quality_reviews.py#L51) | 51 | `""` | — |
| [SRC-03FF422A16-L000052](../../scripts/score_answer_quality_reviews.py#L52) | 52 | `"    valid_case_ids = {"` | — |
| [SRC-03FF422A16-L000053](../../scripts/score_answer_quality_reviews.py#L53) | 53 | `"        item.get(\"case_id\")"` | — |
| [SRC-03FF422A16-L000054](../../scripts/score_answer_quality_reviews.py#L54) | 54 | `"        for item in corpus_cases"` | — |
| [SRC-03FF422A16-L000055](../../scripts/score_answer_quality_reviews.py#L55) | 55 | `"        if isinstance(item, dict) and isinstance(item.get(\"case_id\"), str)"` | — |
| [SRC-03FF422A16-L000056](../../scripts/score_answer_quality_reviews.py#L56) | 56 | `"    }"` | — |
| [SRC-03FF422A16-L000057](../../scripts/score_answer_quality_reviews.py#L57) | 57 | `"    seen: set[str] = set()"` | — |
| [SRC-03FF422A16-L000058](../../scripts/score_answer_quality_reviews.py#L58) | 58 | `"    for index, item in enumerate(reviews):"` | — |
| [SRC-03FF422A16-L000059](../../scripts/score_answer_quality_reviews.py#L59) | 59 | `"        label = \"reviews[\" + str(index) + \"]\""` | — |
| [SRC-03FF422A16-L000060](../../scripts/score_answer_quality_reviews.py#L60) | 60 | `"        if not isinstance(item, dict):"` | — |
| [SRC-03FF422A16-L000061](../../scripts/score_answer_quality_reviews.py#L61) | 61 | `"            problems.append(label + \" must be an object\")"` | — |
| [SRC-03FF422A16-L000062](../../scripts/score_answer_quality_reviews.py#L62) | 62 | `"            continue"` | — |
| [SRC-03FF422A16-L000063](../../scripts/score_answer_quality_reviews.py#L63) | 63 | `"        case_id = item.get(\"case_id\")"` | — |
| [SRC-03FF422A16-L000064](../../scripts/score_answer_quality_reviews.py#L64) | 64 | `"        if not isinstance(case_id, str) or not case_id.strip():"` | — |
| [SRC-03FF422A16-L000065](../../scripts/score_answer_quality_reviews.py#L65) | 65 | `"            problems.append(label + \": case_id must be a non-empty string\")"` | — |
| [SRC-03FF422A16-L000066](../../scripts/score_answer_quality_reviews.py#L66) | 66 | `"            continue"` | — |
| [SRC-03FF422A16-L000067](../../scripts/score_answer_quality_reviews.py#L67) | 67 | `"        if case_id in seen:"` | — |
| [SRC-03FF422A16-L000068](../../scripts/score_answer_quality_reviews.py#L68) | 68 | `"            problems.append(case_id + \": duplicate review\")"` | — |
| [SRC-03FF422A16-L000069](../../scripts/score_answer_quality_reviews.py#L69) | 69 | `"        seen.add(case_id)"` | — |
| [SRC-03FF422A16-L000070](../../scripts/score_answer_quality_reviews.py#L70) | 70 | `"        if case_id not in valid_case_ids:"` | — |
| [SRC-03FF422A16-L000071](../../scripts/score_answer_quality_reviews.py#L71) | 71 | `"            problems.append(case_id + \": unknown case_id (not in the supplied corpus)\")"` | — |
| [SRC-03FF422A16-L000072](../../scripts/score_answer_quality_reviews.py#L72) | 72 | `"        status = item.get(\"status\")"` | — |
| [SRC-03FF422A16-L000073](../../scripts/score_answer_quality_reviews.py#L73) | 73 | `"        if status not in ALLOWED_STATUSES:"` | — |
| [SRC-03FF422A16-L000074](../../scripts/score_answer_quality_reviews.py#L74) | 74 | `"            problems.append(case_id + \": status must be one of \" + \", \".join(sorted(ALLOWED_STATUSES)))"` | — |
| [SRC-03FF422A16-L000075](../../scripts/score_answer_quality_reviews.py#L75) | 75 | `"            continue"` | — |
| [SRC-03FF422A16-L000076](../../scripts/score_answer_quality_reviews.py#L76) | 76 | `""` | — |
| [SRC-03FF422A16-L000077](../../scripts/score_answer_quality_reviews.py#L77) | 77 | `"        has_score = False"` | — |
| [SRC-03FF422A16-L000078](../../scripts/score_answer_quality_reviews.py#L78) | 78 | `"        for group_name, fields in COUNT_GROUPS.items():"` | — |
| [SRC-03FF422A16-L000079](../../scripts/score_answer_quality_reviews.py#L79) | 79 | `"            group = item.get(group_name)"` | — |
| [SRC-03FF422A16-L000080](../../scripts/score_answer_quality_reviews.py#L80) | 80 | `"            if group is None:"` | — |
| [SRC-03FF422A16-L000081](../../scripts/score_answer_quality_reviews.py#L81) | 81 | `"                continue"` | — |
| [SRC-03FF422A16-L000082](../../scripts/score_answer_quality_reviews.py#L82) | 82 | `"            if not isinstance(group, dict):"` | — |
| [SRC-03FF422A16-L000083](../../scripts/score_answer_quality_reviews.py#L83) | 83 | `"                problems.append(case_id + \": \" + group_name + \" must be an object\")"` | — |
| [SRC-03FF422A16-L000084](../../scripts/score_answer_quality_reviews.py#L84) | 84 | `"                continue"` | — |
| [SRC-03FF422A16-L000085](../../scripts/score_answer_quality_reviews.py#L85) | 85 | `"            has_score = True"` | — |
| [SRC-03FF422A16-L000086](../../scripts/score_answer_quality_reviews.py#L86) | 86 | `"            missing = [field for field in fields if field not in group]"` | — |
| [SRC-03FF422A16-L000087](../../scripts/score_answer_quality_reviews.py#L87) | 87 | `"            if missing:"` | — |
| [SRC-03FF422A16-L000088](../../scripts/score_answer_quality_reviews.py#L88) | 88 | `"                problems.append(case_id + \": \" + group_name + \" missing \" + \", \".join(missing))"` | — |
| [SRC-03FF422A16-L000089](../../scripts/score_answer_quality_reviews.py#L89) | 89 | `"                continue"` | — |
| [SRC-03FF422A16-L000090](../../scripts/score_answer_quality_reviews.py#L90) | 90 | `"            values: dict[str, int] = {}"` | — |
| [SRC-03FF422A16-L000091](../../scripts/score_answer_quality_reviews.py#L91) | 91 | `"            for field in fields:"` | — |
| [SRC-03FF422A16-L000092](../../scripts/score_answer_quality_reviews.py#L92) | 92 | `"                value = group[field]"` | — |
| [SRC-03FF422A16-L000093](../../scripts/score_answer_quality_reviews.py#L93) | 93 | `"                if not _is_nonnegative_int(value):"` | — |
| [SRC-03FF422A16-L000094](../../scripts/score_answer_quality_reviews.py#L94) | 94 | `"                    problems.append(case_id + \": \" + group_name + \".\" + field + \" must be a non-negative integer\")"` | — |
| [SRC-03FF422A16-L000095](../../scripts/score_answer_quality_reviews.py#L95) | 95 | `"                else:"` | — |
| [SRC-03FF422A16-L000096](../../scripts/score_answer_quality_reviews.py#L96) | 96 | `"                    values[field] = value"` | — |
| [SRC-03FF422A16-L000097](../../scripts/score_answer_quality_reviews.py#L97) | 97 | `"            if len(values) != len(fields):"` | — |
| [SRC-03FF422A16-L000098](../../scripts/score_answer_quality_reviews.py#L98) | 98 | `"                continue"` | — |
| [SRC-03FF422A16-L000099](../../scripts/score_answer_quality_reviews.py#L99) | 99 | `"            if group_name == \"retrieval\":"` | — |
| [SRC-03FF422A16-L000100](../../scripts/score_answer_quality_reviews.py#L100) | 100 | `"                if values[\"relevant_retrieved\"] > values[\"retrieved_count\"]:"` | — |
| [SRC-03FF422A16-L000101](../../scripts/score_answer_quality_reviews.py#L101) | 101 | `"                    problems.append(case_id + \": relevant_retrieved cannot exceed retrieved_count\")"` | — |
| [SRC-03FF422A16-L000102](../../scripts/score_answer_quality_reviews.py#L102) | 102 | `"                if values[\"relevant_retrieved\"] > values[\"relevant_available\"]:"` | — |
| [SRC-03FF422A16-L000103](../../scripts/score_answer_quality_reviews.py#L103) | 103 | `"                    problems.append(case_id + \": relevant_retrieved cannot exceed relevant_available\")"` | — |
| [SRC-03FF422A16-L000104](../../scripts/score_answer_quality_reviews.py#L104) | 104 | `"            else:"` | — |
| [SRC-03FF422A16-L000105](../../scripts/score_answer_quality_reviews.py#L105) | 105 | `"                numerator, denominator = fields"` | — |
| [SRC-03FF422A16-L000106](../../scripts/score_answer_quality_reviews.py#L106) | 106 | `"                if values[numerator] > values[denominator]:"` | — |
| [SRC-03FF422A16-L000107](../../scripts/score_answer_quality_reviews.py#L107) | 107 | `"                    problems.append(case_id + \": \" + numerator + \" cannot exceed \" + denominator)"` | — |
| [SRC-03FF422A16-L000108](../../scripts/score_answer_quality_reviews.py#L108) | 108 | `""` | — |
| [SRC-03FF422A16-L000109](../../scripts/score_answer_quality_reviews.py#L109) | 109 | `"        writing = item.get(\"writing_quality\")"` | — |
| [SRC-03FF422A16-L000110](../../scripts/score_answer_quality_reviews.py#L110) | 110 | `"        if writing is not None:"` | — |
| [SRC-03FF422A16-L000111](../../scripts/score_answer_quality_reviews.py#L111) | 111 | `"            has_score = True"` | — |
| [SRC-03FF422A16-L000112](../../scripts/score_answer_quality_reviews.py#L112) | 112 | `"            if ("` | — |
| [SRC-03FF422A16-L000113](../../scripts/score_answer_quality_reviews.py#L113) | 113 | `"                isinstance(writing, bool)"` | — |
| [SRC-03FF422A16-L000114](../../scripts/score_answer_quality_reviews.py#L114) | 114 | `"                or not isinstance(writing, (int, float))"` | — |
| [SRC-03FF422A16-L000115](../../scripts/score_answer_quality_reviews.py#L115) | 115 | `"                or not math.isfinite(float(writing))"` | — |
| [SRC-03FF422A16-L000116](../../scripts/score_answer_quality_reviews.py#L116) | 116 | `"                or float(writing) < 1"` | — |
| [SRC-03FF422A16-L000117](../../scripts/score_answer_quality_reviews.py#L117) | 117 | `"                or float(writing) > 5"` | — |
| [SRC-03FF422A16-L000118](../../scripts/score_answer_quality_reviews.py#L118) | 118 | `"            ):"` | — |
| [SRC-03FF422A16-L000119](../../scripts/score_answer_quality_reviews.py#L119) | 119 | `"                problems.append(case_id + \": writing_quality must be a finite score from 1 to 5\")"` | — |
| [SRC-03FF422A16-L000120](../../scripts/score_answer_quality_reviews.py#L120) | 120 | `""` | — |
| [SRC-03FF422A16-L000121](../../scripts/score_answer_quality_reviews.py#L121) | 121 | `"        if status != \"REVIEWED\" and has_score:"` | — |
| [SRC-03FF422A16-L000122](../../scripts/score_answer_quality_reviews.py#L122) | 122 | `"            problems.append(case_id + \": unreviewed case must not contain metric scores\")"` | — |
| [SRC-03FF422A16-L000123](../../scripts/score_answer_quality_reviews.py#L123) | 123 | `"        if status == \"REVIEWED\" and not has_score:"` | — |
| [SRC-03FF422A16-L000124](../../scripts/score_answer_quality_reviews.py#L124) | 124 | `"            problems.append(case_id + \": REVIEWED case must include at least one scored dimension\")"` | — |
| [SRC-03FF422A16-L000125](../../scripts/score_answer_quality_reviews.py#L125) | 125 | `"    return problems"` | — |
| [SRC-03FF422A16-L000126](../../scripts/score_answer_quality_reviews.py#L126) | 126 | `""` | — |
| [SRC-03FF422A16-L000127](../../scripts/score_answer_quality_reviews.py#L127) | 127 | `""` | — |
| [SRC-03FF422A16-L000128](../../scripts/score_answer_quality_reviews.py#L128) | 128 | `"def _ratio(numerator: int, denominator: int, case_count: int) -> dict[str, Any]:"` | — |
| [SRC-03FF422A16-L000129](../../scripts/score_answer_quality_reviews.py#L129) | 129 | `"    return {"` | — |
| [SRC-03FF422A16-L000130](../../scripts/score_answer_quality_reviews.py#L130) | 130 | `"        \"score\": round(numerator / denominator, 4) if denominator else None,"` | — |
| [SRC-03FF422A16-L000131](../../scripts/score_answer_quality_reviews.py#L131) | 131 | `"        \"numerator\": numerator,"` | — |
| [SRC-03FF422A16-L000132](../../scripts/score_answer_quality_reviews.py#L132) | 132 | `"        \"denominator\": denominator,"` | — |
| [SRC-03FF422A16-L000133](../../scripts/score_answer_quality_reviews.py#L133) | 133 | `"        \"reviewed_case_count\": case_count,"` | — |
| [SRC-03FF422A16-L000134](../../scripts/score_answer_quality_reviews.py#L134) | 134 | `"        \"status\": \"SCORED_FROM_HUMAN_REVIEW\" if denominator else \"NOT_SCORABLE_NO_ANNOTATED_DENOMINATOR\","` | — |
| [SRC-03FF422A16-L000135](../../scripts/score_answer_quality_reviews.py#L135) | 135 | `"    }"` | — |
| [SRC-03FF422A16-L000136](../../scripts/score_answer_quality_reviews.py#L136) | 136 | `""` | — |
| [SRC-03FF422A16-L000137](../../scripts/score_answer_quality_reviews.py#L137) | 137 | `""` | — |
| [SRC-03FF422A16-L000138](../../scripts/score_answer_quality_reviews.py#L138) | 138 | `"def summarize_reviews("` | — |
| [SRC-03FF422A16-L000139](../../scripts/score_answer_quality_reviews.py#L139) | 139 | `"    review_data: dict[str, Any], corpus_data: dict[str, Any]"` | — |
| [SRC-03FF422A16-L000140](../../scripts/score_answer_quality_reviews.py#L140) | 140 | `") -> dict[str, Any]:"` | — |
| [SRC-03FF422A16-L000141](../../scripts/score_answer_quality_reviews.py#L141) | 141 | `"    problems = validate_reviews(review_data, corpus_data)"` | — |
| [SRC-03FF422A16-L000142](../../scripts/score_answer_quality_reviews.py#L142) | 142 | `"    if problems:"` | — |
| [SRC-03FF422A16-L000143](../../scripts/score_answer_quality_reviews.py#L143) | 143 | `"        raise ValueError(\"; \".join(problems))"` | — |
| [SRC-03FF422A16-L000144](../../scripts/score_answer_quality_reviews.py#L144) | 144 | `"    reviews = review_data[\"reviews\"]"` | — |
| [SRC-03FF422A16-L000145](../../scripts/score_answer_quality_reviews.py#L145) | 145 | `"    reviewed = [item for item in reviews if item[\"status\"] == \"REVIEWED\"]"` | — |
| [SRC-03FF422A16-L000146](../../scripts/score_answer_quality_reviews.py#L146) | 146 | `"    status_counts = Counter(item[\"status\"] for item in reviews)"` | — |
| [SRC-03FF422A16-L000147](../../scripts/score_answer_quality_reviews.py#L147) | 147 | `"    corpus_count = len(corpus_data[\"cases\"])"` | — |
| [SRC-03FF422A16-L000148](../../scripts/score_answer_quality_reviews.py#L148) | 148 | `"    reviewed_ids = {item[\"case_id\"] for item in reviewed}"` | — |
| [SRC-03FF422A16-L000149](../../scripts/score_answer_quality_reviews.py#L149) | 149 | `""` | — |
| [SRC-03FF422A16-L000150](../../scripts/score_answer_quality_reviews.py#L150) | 150 | `"    retrieval_rel = retrieval_total = retrieval_available = 0"` | — |
| [SRC-03FF422A16-L000151](../../scripts/score_answer_quality_reviews.py#L151) | 151 | `"    retrieval_cases = set()"` | — |
| [SRC-03FF422A16-L000152](../../scripts/score_answer_quality_reviews.py#L152) | 152 | `"    faithfulness_supported = faithfulness_total = 0"` | — |
| [SRC-03FF422A16-L000153](../../scripts/score_answer_quality_reviews.py#L153) | 153 | `"    faithfulness_cases = set()"` | — |
| [SRC-03FF422A16-L000154](../../scripts/score_answer_quality_reviews.py#L154) | 154 | `"    correctness_correct = correctness_total = 0"` | — |
| [SRC-03FF422A16-L000155](../../scripts/score_answer_quality_reviews.py#L155) | 155 | `"    correctness_cases = set()"` | — |
| [SRC-03FF422A16-L000156](../../scripts/score_answer_quality_reviews.py#L156) | 156 | `"    citation_supported = citation_total = 0"` | — |
| [SRC-03FF422A16-L000157](../../scripts/score_answer_quality_reviews.py#L157) | 157 | `"    citation_cases = set()"` | — |
| [SRC-03FF422A16-L000158](../../scripts/score_answer_quality_reviews.py#L158) | 158 | `"    writing_scores: list[float] = []"` | — |
| [SRC-03FF422A16-L000159](../../scripts/score_answer_quality_reviews.py#L159) | 159 | `""` | — |
| [SRC-03FF422A16-L000160](../../scripts/score_answer_quality_reviews.py#L160) | 160 | `"    for item in reviewed:"` | — |
| [SRC-03FF422A16-L000161](../../scripts/score_answer_quality_reviews.py#L161) | 161 | `"        case_id = item[\"case_id\"]"` | — |
| [SRC-03FF422A16-L000162](../../scripts/score_answer_quality_reviews.py#L162) | 162 | `"        retrieval = item.get(\"retrieval\")"` | — |
| [SRC-03FF422A16-L000163](../../scripts/score_answer_quality_reviews.py#L163) | 163 | `"        if isinstance(retrieval, dict):"` | — |
| [SRC-03FF422A16-L000164](../../scripts/score_answer_quality_reviews.py#L164) | 164 | `"            retrieval_rel += retrieval[\"relevant_retrieved\"]"` | — |
| [SRC-03FF422A16-L000165](../../scripts/score_answer_quality_reviews.py#L165) | 165 | `"            retrieval_total += retrieval[\"retrieved_count\"]"` | — |
| [SRC-03FF422A16-L000166](../../scripts/score_answer_quality_reviews.py#L166) | 166 | `"            retrieval_available += retrieval[\"relevant_available\"]"` | — |
| [SRC-03FF422A16-L000167](../../scripts/score_answer_quality_reviews.py#L167) | 167 | `"            retrieval_cases.add(case_id)"` | — |
| [SRC-03FF422A16-L000168](../../scripts/score_answer_quality_reviews.py#L168) | 168 | `"        faithfulness = item.get(\"faithfulness\")"` | — |
| [SRC-03FF422A16-L000169](../../scripts/score_answer_quality_reviews.py#L169) | 169 | `"        if isinstance(faithfulness, dict):"` | — |
| [SRC-03FF422A16-L000170](../../scripts/score_answer_quality_reviews.py#L170) | 170 | `"            faithfulness_supported += faithfulness[\"supported_claims\"]"` | — |
| [SRC-03FF422A16-L000171](../../scripts/score_answer_quality_reviews.py#L171) | 171 | `"            faithfulness_total += faithfulness[\"reviewed_claims\"]"` | — |
| [SRC-03FF422A16-L000172](../../scripts/score_answer_quality_reviews.py#L172) | 172 | `"            faithfulness_cases.add(case_id)"` | — |
| [SRC-03FF422A16-L000173](../../scripts/score_answer_quality_reviews.py#L173) | 173 | `"        correctness = item.get(\"correctness\")"` | — |
| [SRC-03FF422A16-L000174](../../scripts/score_answer_quality_reviews.py#L174) | 174 | `"        if isinstance(correctness, dict):"` | — |
| [SRC-03FF422A16-L000175](../../scripts/score_answer_quality_reviews.py#L175) | 175 | `"            correctness_correct += correctness[\"correct_facts\"]"` | — |
| [SRC-03FF422A16-L000176](../../scripts/score_answer_quality_reviews.py#L176) | 176 | `"            correctness_total += correctness[\"reviewed_facts\"]"` | — |
| [SRC-03FF422A16-L000177](../../scripts/score_answer_quality_reviews.py#L177) | 177 | `"            correctness_cases.add(case_id)"` | — |
| [SRC-03FF422A16-L000178](../../scripts/score_answer_quality_reviews.py#L178) | 178 | `"        citations = item.get(\"citations\")"` | — |
| [SRC-03FF422A16-L000179](../../scripts/score_answer_quality_reviews.py#L179) | 179 | `"        if isinstance(citations, dict):"` | — |
| [SRC-03FF422A16-L000180](../../scripts/score_answer_quality_reviews.py#L180) | 180 | `"            citation_supported += citations[\"supported_citations\"]"` | — |
