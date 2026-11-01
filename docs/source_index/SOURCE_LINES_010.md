# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **010**
- سجلات الأسطر: **800**
- النطاق: SRC-FC84E5B115-L000039 إلى SRC-1AE03B9EC3-L000486
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-FC84E5B115 — [agents/text_normalization.py](../../agents/text_normalization.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-FC84E5B115-L000039](../../agents/text_normalization.py#L39) | 39 | `"    if drop_stopwords:"` | — |
| [SRC-FC84E5B115-L000040](../../agents/text_normalization.py#L40) | 40 | `"        tokens = [token for token in tokens if token not in _STOPWORDS]"` | — |
| [SRC-FC84E5B115-L000041](../../agents/text_normalization.py#L41) | 41 | `"    return tokens"` | — |
## الوكيل والمنطق

### FILE-0799EEEB02 — [agents/tool_execution_status.py](../../agents/tool_execution_status.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-0799EEEB02-L000001](../../agents/tool_execution_status.py#L1) | 1 | `"\"\"\"Truthful task-tool execution status, separate from task planning and evidence quality.\"\"\""` | — |
| [SRC-0799EEEB02-L000002](../../agents/tool_execution_status.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-0799EEEB02-L000003](../../agents/tool_execution_status.py#L3) | 3 | `""` | — |
| [SRC-0799EEEB02-L000004](../../agents/tool_execution_status.py#L4) | 4 | `"from typing import Any"` | — |
| [SRC-0799EEEB02-L000005](../../agents/tool_execution_status.py#L5) | 5 | `""` | — |
| [SRC-0799EEEB02-L000006](../../agents/tool_execution_status.py#L6) | 6 | `"_TOOL_LABELS = {"` | — |
| [SRC-0799EEEB02-L000007](../../agents/tool_execution_status.py#L7) | 7 | `"    \"web_search\": \"البحث على الويب\","` | — |
| [SRC-0799EEEB02-L000008](../../agents/tool_execution_status.py#L8) | 8 | `"    \"page_fetch\": \"فتح الصفحات وقراءة النص\","` | — |
| [SRC-0799EEEB02-L000009](../../agents/tool_execution_status.py#L9) | 9 | `"    \"public_social_search_if_configured\": \"البحث في المحتوى الاجتماعي العام\","` | — |
| [SRC-0799EEEB02-L000010](../../agents/tool_execution_status.py#L10) | 10 | `"    \"language_model_generation_if_configured\": \"توليد الإجابة بالنموذج\","` | — |
| [SRC-0799EEEB02-L000011](../../agents/tool_execution_status.py#L11) | 11 | `"    \"claim_review_if_configured\": \"مراجعة الإجابة بمساعدة النموذج\","` | — |
| [SRC-0799EEEB02-L000012](../../agents/tool_execution_status.py#L12) | 12 | `"}"` | — |
| [SRC-0799EEEB02-L000013](../../agents/tool_execution_status.py#L13) | 13 | `"_ERROR_OUTCOMES = {"` | — |
| [SRC-0799EEEB02-L000014](../../agents/tool_execution_status.py#L14) | 14 | `"    \"attempted_research_error\","` | — |
| [SRC-0799EEEB02-L000015](../../agents/tool_execution_status.py#L15) | 15 | `"    \"unknown_after_research_error\","` | — |
| [SRC-0799EEEB02-L000016](../../agents/tool_execution_status.py#L16) | 16 | `"    \"unknown_after_budget_exhaustion\","` | — |
| [SRC-0799EEEB02-L000017](../../agents/tool_execution_status.py#L17) | 17 | `"}"` | — |
| [SRC-0799EEEB02-L000018](../../agents/tool_execution_status.py#L18) | 18 | `"_SOCIAL_PLATFORMS = {"` | — |
| [SRC-0799EEEB02-L000019](../../agents/tool_execution_status.py#L19) | 19 | `"    \"reddit\", \"youtube\", \"facebook\", \"instagram\", \"x\", \"twitter\","` | — |
| [SRC-0799EEEB02-L000020](../../agents/tool_execution_status.py#L20) | 20 | `"    \"tiktok\", \"linkedin\", \"threads\", \"bluesky\","` | — |
| [SRC-0799EEEB02-L000021](../../agents/tool_execution_status.py#L21) | 21 | `"}"` | — |
| [SRC-0799EEEB02-L000022](../../agents/tool_execution_status.py#L22) | 22 | `""` | — |
| [SRC-0799EEEB02-L000023](../../agents/tool_execution_status.py#L23) | 23 | `""` | — |
| [SRC-0799EEEB02-L000024](../../agents/tool_execution_status.py#L24) | 24 | `"def _nonnegative_int(value: Any) -> int \| None:"` | — |
| [SRC-0799EEEB02-L000025](../../agents/tool_execution_status.py#L25) | 25 | `"    if isinstance(value, bool):"` | — |
| [SRC-0799EEEB02-L000026](../../agents/tool_execution_status.py#L26) | 26 | `"        return None"` | — |
| [SRC-0799EEEB02-L000027](../../agents/tool_execution_status.py#L27) | 27 | `"    if isinstance(value, int):"` | — |
| [SRC-0799EEEB02-L000028](../../agents/tool_execution_status.py#L28) | 28 | `"        return max(0, value)"` | — |
| [SRC-0799EEEB02-L000029](../../agents/tool_execution_status.py#L29) | 29 | `"    if isinstance(value, float) and value.is_integer():"` | — |
| [SRC-0799EEEB02-L000030](../../agents/tool_execution_status.py#L30) | 30 | `"        return max(0, int(value))"` | — |
| [SRC-0799EEEB02-L000031](../../agents/tool_execution_status.py#L31) | 31 | `"    return None"` | — |
| [SRC-0799EEEB02-L000032](../../agents/tool_execution_status.py#L32) | 32 | `""` | — |
| [SRC-0799EEEB02-L000033](../../agents/tool_execution_status.py#L33) | 33 | `""` | — |
| [SRC-0799EEEB02-L000034](../../agents/tool_execution_status.py#L34) | 34 | `"def _status_row("` | — |
| [SRC-0799EEEB02-L000035](../../agents/tool_execution_status.py#L35) | 35 | `"    tool: str,"` | — |
| [SRC-0799EEEB02-L000036](../../agents/tool_execution_status.py#L36) | 36 | `"    required: bool,"` | — |
| [SRC-0799EEEB02-L000037](../../agents/tool_execution_status.py#L37) | 37 | `"    status: str,"` | — |
| [SRC-0799EEEB02-L000038](../../agents/tool_execution_status.py#L38) | 38 | `"    basis: dict[str, Any],"` | — |
| [SRC-0799EEEB02-L000039](../../agents/tool_execution_status.py#L39) | 39 | `") -> dict[str, Any]:"` | — |
| [SRC-0799EEEB02-L000040](../../agents/tool_execution_status.py#L40) | 40 | `"    return {"` | — |
| [SRC-0799EEEB02-L000041](../../agents/tool_execution_status.py#L41) | 41 | `"        \"tool\": tool,"` | — |
| [SRC-0799EEEB02-L000042](../../agents/tool_execution_status.py#L42) | 42 | `"        \"label_ar\": _TOOL_LABELS[tool],"` | — |
| [SRC-0799EEEB02-L000043](../../agents/tool_execution_status.py#L43) | 43 | `"        \"required_by_task_spec\": required,"` | — |
| [SRC-0799EEEB02-L000044](../../agents/tool_execution_status.py#L44) | 44 | `"        \"status\": status,"` | — |
| [SRC-0799EEEB02-L000045](../../agents/tool_execution_status.py#L45) | 45 | `"        \"basis\": basis,"` | — |
| [SRC-0799EEEB02-L000046](../../agents/tool_execution_status.py#L46) | 46 | `"        \"semantics\": ("` | — |
| [SRC-0799EEEB02-L000047](../../agents/tool_execution_status.py#L47) | 47 | `"            \"حالة مسار التنفيذ المرصودة فقط؛ لا تثبت صحة المحتوى أو كفاية الدليل.\""` | — |
| [SRC-0799EEEB02-L000048](../../agents/tool_execution_status.py#L48) | 48 | `"        ),"` | — |
| [SRC-0799EEEB02-L000049](../../agents/tool_execution_status.py#L49) | 49 | `"    }"` | — |
| [SRC-0799EEEB02-L000050](../../agents/tool_execution_status.py#L50) | 50 | `""` | — |
| [SRC-0799EEEB02-L000051](../../agents/tool_execution_status.py#L51) | 51 | `""` | — |
| [SRC-0799EEEB02-L000052](../../agents/tool_execution_status.py#L52) | 52 | `"def build_tool_execution_matrix("` | — |
| [SRC-0799EEEB02-L000053](../../agents/tool_execution_status.py#L53) | 53 | `"    task_spec: dict[str, Any] \| None,"` | — |
| [SRC-0799EEEB02-L000054](../../agents/tool_execution_status.py#L54) | 54 | `"    result: dict[str, Any] \| None,"` | — |
| [SRC-0799EEEB02-L000055](../../agents/tool_execution_status.py#L55) | 55 | `"    report: dict[str, Any] \| None,"` | — |
| [SRC-0799EEEB02-L000056](../../agents/tool_execution_status.py#L56) | 56 | `") -> list[dict[str, Any]]:"` | — |
| [SRC-0799EEEB02-L000057](../../agents/tool_execution_status.py#L57) | 57 | `"    \"\"\"Map planned tool requirements to observed outcomes without inferring success.\"\"\""` | — |
| [SRC-0799EEEB02-L000058](../../agents/tool_execution_status.py#L58) | 58 | `"    spec = task_spec if isinstance(task_spec, dict) else {}"` | — |
| [SRC-0799EEEB02-L000059](../../agents/tool_execution_status.py#L59) | 59 | `"    output = result if isinstance(result, dict) else {}"` | — |
| [SRC-0799EEEB02-L000060](../../agents/tool_execution_status.py#L60) | 60 | `"    search_report = report if isinstance(report, dict) else {}"` | — |
| [SRC-0799EEEB02-L000061](../../agents/tool_execution_status.py#L61) | 61 | `"    requirements = spec.get(\"tool_requirements\")"` | — |
| [SRC-0799EEEB02-L000062](../../agents/tool_execution_status.py#L62) | 62 | `"    required = {"` | — |
| [SRC-0799EEEB02-L000063](../../agents/tool_execution_status.py#L63) | 63 | `"        item for item in requirements"` | — |
| [SRC-0799EEEB02-L000064](../../agents/tool_execution_status.py#L64) | 64 | `"        if isinstance(item, str) and item in _TOOL_LABELS"` | — |
| [SRC-0799EEEB02-L000065](../../agents/tool_execution_status.py#L65) | 65 | `"    } if isinstance(requirements, list) else set()"` | — |
| [SRC-0799EEEB02-L000066](../../agents/tool_execution_status.py#L66) | 66 | `""` | — |
| [SRC-0799EEEB02-L000067](../../agents/tool_execution_status.py#L67) | 67 | `"    outcome = str(search_report.get(\"search_outcome\") or \"unknown\")"` | — |
| [SRC-0799EEEB02-L000068](../../agents/tool_execution_status.py#L68) | 68 | `"    attempted = output.get(\"search_attempted\", search_report.get(\"search_attempted\"))"` | — |
| [SRC-0799EEEB02-L000069](../../agents/tool_execution_status.py#L69) | 69 | `"    reported_accepted_sources = _nonnegative_int("` | — |
| [SRC-0799EEEB02-L000070](../../agents/tool_execution_status.py#L70) | 70 | `"        search_report.get(\"usable_sources_after_filtering\")"` | — |
| [SRC-0799EEEB02-L000071](../../agents/tool_execution_status.py#L71) | 71 | `"    )"` | — |
| [SRC-0799EEEB02-L000072](../../agents/tool_execution_status.py#L72) | 72 | `"    reported_pages_read = _nonnegative_int(search_report.get(\"pages_fetched\"))"` | — |
| [SRC-0799EEEB02-L000073](../../agents/tool_execution_status.py#L73) | 73 | `"    pages_attempted = _nonnegative_int(search_report.get(\"pages_fetch_attempted\"))"` | — |
| [SRC-0799EEEB02-L000074](../../agents/tool_execution_status.py#L74) | 74 | `"    raw_source_rows = output.get(\"sources\")"` | — |
| [SRC-0799EEEB02-L000075](../../agents/tool_execution_status.py#L75) | 75 | `"    returned_sources_known = isinstance(raw_source_rows, list)"` | — |
| [SRC-0799EEEB02-L000076](../../agents/tool_execution_status.py#L76) | 76 | `"    source_rows = raw_source_rows if returned_sources_known else []"` | — |
| [SRC-0799EEEB02-L000077](../../agents/tool_execution_status.py#L77) | 77 | `"    readable_page_rows = sum("` | — |
| [SRC-0799EEEB02-L000078](../../agents/tool_execution_status.py#L78) | 78 | `"        1 for source in source_rows"` | — |
| [SRC-0799EEEB02-L000079](../../agents/tool_execution_status.py#L79) | 79 | `"        if isinstance(source, dict)"` | — |
| [SRC-0799EEEB02-L000080](../../agents/tool_execution_status.py#L80) | 80 | `"        and source.get(\"page_fetched\") is True"` | — |
| [SRC-0799EEEB02-L000081](../../agents/tool_execution_status.py#L81) | 81 | `"    )"` | — |
| [SRC-0799EEEB02-L000082](../../agents/tool_execution_status.py#L82) | 82 | `"    # The public return value is the final accepted source set. Prefer it when"` | — |
| [SRC-0799EEEB02-L000083](../../agents/tool_execution_status.py#L83) | 83 | `"    # present; preserve report counters separately so disagreements stay visible."` | — |
| [SRC-0799EEEB02-L000084](../../agents/tool_execution_status.py#L84) | 84 | `"    returned_source_count = len(source_rows) if returned_sources_known else None"` | — |
| [SRC-0799EEEB02-L000085](../../agents/tool_execution_status.py#L85) | 85 | `"    accepted_sources = ("` | — |
| [SRC-0799EEEB02-L000086](../../agents/tool_execution_status.py#L86) | 86 | `"        returned_source_count if returned_sources_known else reported_accepted_sources"` | — |
| [SRC-0799EEEB02-L000087](../../agents/tool_execution_status.py#L87) | 87 | `"    )"` | — |
| [SRC-0799EEEB02-L000088](../../agents/tool_execution_status.py#L88) | 88 | `"    pages_read = reported_pages_read if reported_pages_read is not None else readable_page_rows"` | — |
| [SRC-0799EEEB02-L000089](../../agents/tool_execution_status.py#L89) | 89 | `"    source_count_mismatch = ("` | — |
| [SRC-0799EEEB02-L000090](../../agents/tool_execution_status.py#L90) | 90 | `"        returned_sources_known"` | — |
| [SRC-0799EEEB02-L000091](../../agents/tool_execution_status.py#L91) | 91 | `"        and reported_accepted_sources is not None"` | — |
| [SRC-0799EEEB02-L000092](../../agents/tool_execution_status.py#L92) | 92 | `"        and reported_accepted_sources != returned_source_count"` | — |
| [SRC-0799EEEB02-L000093](../../agents/tool_execution_status.py#L93) | 93 | `"    )"` | — |
| [SRC-0799EEEB02-L000094](../../agents/tool_execution_status.py#L94) | 94 | `"    page_count_mismatch = ("` | — |
| [SRC-0799EEEB02-L000095](../../agents/tool_execution_status.py#L95) | 95 | `"        returned_sources_known"` | — |
| [SRC-0799EEEB02-L000096](../../agents/tool_execution_status.py#L96) | 96 | `"        and reported_pages_read is not None"` | — |
| [SRC-0799EEEB02-L000097](../../agents/tool_execution_status.py#L97) | 97 | `"        and reported_pages_read != readable_page_rows"` | — |
| [SRC-0799EEEB02-L000098](../../agents/tool_execution_status.py#L98) | 98 | `"    )"` | — |
| [SRC-0799EEEB02-L000099](../../agents/tool_execution_status.py#L99) | 99 | `""` | — |
| [SRC-0799EEEB02-L000100](../../agents/tool_execution_status.py#L100) | 100 | `"    rows: list[dict[str, Any]] = []"` | — |
| [SRC-0799EEEB02-L000101](../../agents/tool_execution_status.py#L101) | 101 | `""` | — |
| [SRC-0799EEEB02-L000102](../../agents/tool_execution_status.py#L102) | 102 | `"    # Search completion and evidence acceptance are distinct: zero accepted sources"` | — |
| [SRC-0799EEEB02-L000103](../../agents/tool_execution_status.py#L103) | 103 | `"    # means this retrieval attempt supplied no eligible evidence, not that the fact"` | — |
| [SRC-0799EEEB02-L000104](../../agents/tool_execution_status.py#L104) | 104 | `"    # or source does not exist."` | — |
| [SRC-0799EEEB02-L000105](../../agents/tool_execution_status.py#L105) | 105 | `"    tool = \"web_search\""` | — |
| [SRC-0799EEEB02-L000106](../../agents/tool_execution_status.py#L106) | 106 | `"    if tool not in required:"` | — |
| [SRC-0799EEEB02-L000107](../../agents/tool_execution_status.py#L107) | 107 | `"        status = \"not_required\""` | — |
| [SRC-0799EEEB02-L000108](../../agents/tool_execution_status.py#L108) | 108 | `"    elif outcome == \"attempted_research_error\":"` | — |
| [SRC-0799EEEB02-L000109](../../agents/tool_execution_status.py#L109) | 109 | `"        status = \"failed\""` | — |
| [SRC-0799EEEB02-L000110](../../agents/tool_execution_status.py#L110) | 110 | `"    elif outcome in {\"unknown_after_research_error\", \"unknown_after_budget_exhaustion\"}:"` | — |
| [SRC-0799EEEB02-L000111](../../agents/tool_execution_status.py#L111) | 111 | `"        status = \"unknown\""` | — |
| [SRC-0799EEEB02-L000112](../../agents/tool_execution_status.py#L112) | 112 | `"    elif outcome == \"not_attempted\" or attempted is False:"` | — |
| [SRC-0799EEEB02-L000113](../../agents/tool_execution_status.py#L113) | 113 | `"        status = \"not_attempted\""` | — |
| [SRC-0799EEEB02-L000114](../../agents/tool_execution_status.py#L114) | 114 | `"    elif source_count_mismatch:"` | — |
| [SRC-0799EEEB02-L000115](../../agents/tool_execution_status.py#L115) | 115 | `"        status = \"counter_mismatch\""` | — |
| [SRC-0799EEEB02-L000116](../../agents/tool_execution_status.py#L116) | 116 | `"    elif attempted is True:"` | — |
| [SRC-0799EEEB02-L000117](../../agents/tool_execution_status.py#L117) | 117 | `"        if accepted_sources is not None:"` | — |
| [SRC-0799EEEB02-L000118](../../agents/tool_execution_status.py#L118) | 118 | `"            status = \"completed_with_results\" if accepted_sources > 0 else \"completed_no_usable_results\""` | — |
| [SRC-0799EEEB02-L000119](../../agents/tool_execution_status.py#L119) | 119 | `"        elif outcome == \"attempted_with_usable_sources\":"` | — |
| [SRC-0799EEEB02-L000120](../../agents/tool_execution_status.py#L120) | 120 | `"            status = \"completed_with_results\""` | — |
| [SRC-0799EEEB02-L000121](../../agents/tool_execution_status.py#L121) | 121 | `"        elif outcome == \"attempted_no_usable_sources\":"` | — |
| [SRC-0799EEEB02-L000122](../../agents/tool_execution_status.py#L122) | 122 | `"            status = \"completed_no_usable_results\""` | — |
| [SRC-0799EEEB02-L000123](../../agents/tool_execution_status.py#L123) | 123 | `"        else:"` | — |
| [SRC-0799EEEB02-L000124](../../agents/tool_execution_status.py#L124) | 124 | `"            status = \"unknown\""` | — |
| [SRC-0799EEEB02-L000125](../../agents/tool_execution_status.py#L125) | 125 | `"    else:"` | — |
| [SRC-0799EEEB02-L000126](../../agents/tool_execution_status.py#L126) | 126 | `"        status = \"unknown\""` | — |
| [SRC-0799EEEB02-L000127](../../agents/tool_execution_status.py#L127) | 127 | `"    rows.append(_status_row(tool, tool in required, status, {"` | — |
| [SRC-0799EEEB02-L000128](../../agents/tool_execution_status.py#L128) | 128 | `"        \"search_outcome\": outcome,"` | — |
| [SRC-0799EEEB02-L000129](../../agents/tool_execution_status.py#L129) | 129 | `"        \"search_attempted\": attempted if isinstance(attempted, bool) else None,"` | — |
| [SRC-0799EEEB02-L000130](../../agents/tool_execution_status.py#L130) | 130 | `"        \"accepted_source_count\": accepted_sources,"` | — |
| [SRC-0799EEEB02-L000131](../../agents/tool_execution_status.py#L131) | 131 | `"        \"reported_accepted_source_count\": reported_accepted_sources,"` | — |
| [SRC-0799EEEB02-L000132](../../agents/tool_execution_status.py#L132) | 132 | `"        \"counter_consistency\": ("` | — |
| [SRC-0799EEEB02-L000133](../../agents/tool_execution_status.py#L133) | 133 | `"            \"mismatch\" if source_count_mismatch else \"consistent\""` | — |
| [SRC-0799EEEB02-L000134](../../agents/tool_execution_status.py#L134) | 134 | `"            if returned_sources_known and reported_accepted_sources is not None"` | — |
| [SRC-0799EEEB02-L000135](../../agents/tool_execution_status.py#L135) | 135 | `"            else \"not_comparable\""` | — |
| [SRC-0799EEEB02-L000136](../../agents/tool_execution_status.py#L136) | 136 | `"        ),"` | — |
| [SRC-0799EEEB02-L000137](../../agents/tool_execution_status.py#L137) | 137 | `"    }))"` | — |
| [SRC-0799EEEB02-L000138](../../agents/tool_execution_status.py#L138) | 138 | `""` | — |
| [SRC-0799EEEB02-L000139](../../agents/tool_execution_status.py#L139) | 139 | `"    tool = \"page_fetch\""` | — |
| [SRC-0799EEEB02-L000140](../../agents/tool_execution_status.py#L140) | 140 | `"    if tool not in required:"` | — |
| [SRC-0799EEEB02-L000141](../../agents/tool_execution_status.py#L141) | 141 | `"        status = \"not_required\""` | — |
| [SRC-0799EEEB02-L000142](../../agents/tool_execution_status.py#L142) | 142 | `"    elif page_count_mismatch:"` | — |
| [SRC-0799EEEB02-L000143](../../agents/tool_execution_status.py#L143) | 143 | `"        status = \"counter_mismatch\""` | — |
| [SRC-0799EEEB02-L000144](../../agents/tool_execution_status.py#L144) | 144 | `"    elif pages_read > 0:"` | — |
| [SRC-0799EEEB02-L000145](../../agents/tool_execution_status.py#L145) | 145 | `"        status = \"completed_with_read_pages\""` | — |
| [SRC-0799EEEB02-L000146](../../agents/tool_execution_status.py#L146) | 146 | `"    elif pages_attempted is not None and pages_attempted > 0:"` | — |
| [SRC-0799EEEB02-L000147](../../agents/tool_execution_status.py#L147) | 147 | `"        status = \"attempted_no_readable_pages\""` | — |
| [SRC-0799EEEB02-L000148](../../agents/tool_execution_status.py#L148) | 148 | `"    elif pages_attempted is None:"` | — |
| [SRC-0799EEEB02-L000149](../../agents/tool_execution_status.py#L149) | 149 | `"        status = \"unknown\""` | — |
| [SRC-0799EEEB02-L000150](../../agents/tool_execution_status.py#L150) | 150 | `"    elif outcome in _ERROR_OUTCOMES:"` | — |
| [SRC-0799EEEB02-L000151](../../agents/tool_execution_status.py#L151) | 151 | `"        status = \"not_attempted_after_search_error\""` | — |
| [SRC-0799EEEB02-L000152](../../agents/tool_execution_status.py#L152) | 152 | `"    elif attempted is True:"` | — |
| [SRC-0799EEEB02-L000153](../../agents/tool_execution_status.py#L153) | 153 | `"        status = \"not_attempted_no_fetchable_candidates\""` | — |
| [SRC-0799EEEB02-L000154](../../agents/tool_execution_status.py#L154) | 154 | `"    elif attempted is False:"` | — |
| [SRC-0799EEEB02-L000155](../../agents/tool_execution_status.py#L155) | 155 | `"        status = \"not_attempted\""` | — |
| [SRC-0799EEEB02-L000156](../../agents/tool_execution_status.py#L156) | 156 | `"    else:"` | — |
| [SRC-0799EEEB02-L000157](../../agents/tool_execution_status.py#L157) | 157 | `"        status = \"unknown\""` | — |
| [SRC-0799EEEB02-L000158](../../agents/tool_execution_status.py#L158) | 158 | `"    rows.append(_status_row(tool, tool in required, status, {"` | — |
| [SRC-0799EEEB02-L000159](../../agents/tool_execution_status.py#L159) | 159 | `"        \"pages_fetch_attempted\": pages_attempted,"` | — |
| [SRC-0799EEEB02-L000160](../../agents/tool_execution_status.py#L160) | 160 | `"        \"pages_read\": pages_read,"` | — |
| [SRC-0799EEEB02-L000161](../../agents/tool_execution_status.py#L161) | 161 | `"        \"reported_pages_fetched\": reported_pages_read,"` | — |
| [SRC-0799EEEB02-L000162](../../agents/tool_execution_status.py#L162) | 162 | `"        \"pages_read_from_returned_sources\": readable_page_rows,"` | — |
| [SRC-0799EEEB02-L000163](../../agents/tool_execution_status.py#L163) | 163 | `"        \"counter_consistency\": ("` | — |
| [SRC-0799EEEB02-L000164](../../agents/tool_execution_status.py#L164) | 164 | `"            \"mismatch\" if page_count_mismatch else \"consistent\""` | — |
| [SRC-0799EEEB02-L000165](../../agents/tool_execution_status.py#L165) | 165 | `"            if returned_sources_known and reported_pages_read is not None"` | — |
| [SRC-0799EEEB02-L000166](../../agents/tool_execution_status.py#L166) | 166 | `"            else \"not_comparable\""` | — |
| [SRC-0799EEEB02-L000167](../../agents/tool_execution_status.py#L167) | 167 | `"        ),"` | — |
| [SRC-0799EEEB02-L000168](../../agents/tool_execution_status.py#L168) | 168 | `"    }))"` | — |
| [SRC-0799EEEB02-L000169](../../agents/tool_execution_status.py#L169) | 169 | `""` | — |
| [SRC-0799EEEB02-L000170](../../agents/tool_execution_status.py#L170) | 170 | `"    tool = \"public_social_search_if_configured\""` | — |
| [SRC-0799EEEB02-L000171](../../agents/tool_execution_status.py#L171) | 171 | `"    raw_social_results = _nonnegative_int(search_report.get(\"social_direct_results\"))"` | — |
| [SRC-0799EEEB02-L000172](../../agents/tool_execution_status.py#L172) | 172 | `"    social_results = raw_social_results or 0"` | — |
| [SRC-0799EEEB02-L000173](../../agents/tool_execution_status.py#L173) | 173 | `"    social_sources = sum("` | — |
| [SRC-0799EEEB02-L000174](../../agents/tool_execution_status.py#L174) | 174 | `"        1 for source in source_rows"` | — |
| [SRC-0799EEEB02-L000175](../../agents/tool_execution_status.py#L175) | 175 | `"        if isinstance(source, dict)"` | — |
| [SRC-0799EEEB02-L000176](../../agents/tool_execution_status.py#L176) | 176 | `"        and ("` | — |
| [SRC-0799EEEB02-L000177](../../agents/tool_execution_status.py#L177) | 177 | `"            str(source.get(\"platform\") or \"\").lower() in _SOCIAL_PLATFORMS"` | — |
| [SRC-0799EEEB02-L000178](../../agents/tool_execution_status.py#L178) | 178 | `"            or str(source.get(\"source_class\") or \"\").lower() == \"social\""` | — |
| [SRC-0799EEEB02-L000179](../../agents/tool_execution_status.py#L179) | 179 | `"        )"` | — |
| [SRC-0799EEEB02-L000180](../../agents/tool_execution_status.py#L180) | 180 | `"    )"` | — |
| [SRC-0799EEEB02-L000181](../../agents/tool_execution_status.py#L181) | 181 | `"    connector_summary = search_report.get(\"connector_summary\")"` | — |
| [SRC-0799EEEB02-L000182](../../agents/tool_execution_status.py#L182) | 182 | `"    connector_summary = connector_summary if isinstance(connector_summary, dict) else {}"` | — |
| [SRC-0799EEEB02-L000183](../../agents/tool_execution_status.py#L183) | 183 | `"    connector_rows = connector_summary.get(\"connectors\")"` | — |
| [SRC-0799EEEB02-L000184](../../agents/tool_execution_status.py#L184) | 184 | `"    connector_rows = connector_rows if isinstance(connector_rows, list) else []"` | — |
| [SRC-0799EEEB02-L000185](../../agents/tool_execution_status.py#L185) | 185 | `"    social_connector_names = {"` | — |
| [SRC-0799EEEB02-L000186](../../agents/tool_execution_status.py#L186) | 186 | `"        \"reddit_public_rss\", \"bluesky_public_search\", \"reddit_oauth_api\","` | — |
| [SRC-0799EEEB02-L000187](../../agents/tool_execution_status.py#L187) | 187 | `"        \"facebook_pages_api\", \"instagram_graph_api\", \"x_official_api\","` | — |
| [SRC-0799EEEB02-L000188](../../agents/tool_execution_status.py#L188) | 188 | `"        \"youtube_data_api\","` | — |
| [SRC-0799EEEB02-L000189](../../agents/tool_execution_status.py#L189) | 189 | `"    }"` | — |
| [SRC-0799EEEB02-L000190](../../agents/tool_execution_status.py#L190) | 190 | `"    social_connector_states = ["` | — |
| [SRC-0799EEEB02-L000191](../../agents/tool_execution_status.py#L191) | 191 | `"        row for row in connector_rows"` | — |
| [SRC-0799EEEB02-L000192](../../agents/tool_execution_status.py#L192) | 192 | `"        if isinstance(row, dict) and row.get(\"name\") in social_connector_names"` | — |
| [SRC-0799EEEB02-L000193](../../agents/tool_execution_status.py#L193) | 193 | `"    ]"` | — |
| [SRC-0799EEEB02-L000194](../../agents/tool_execution_status.py#L194) | 194 | `"    attempted_social_connectors = ["` | — |
| [SRC-0799EEEB02-L000195](../../agents/tool_execution_status.py#L195) | 195 | `"        row for row in social_connector_states if row.get(\"attempted\") is True"` | — |
| [SRC-0799EEEB02-L000196](../../agents/tool_execution_status.py#L196) | 196 | `"    ]"` | — |
| [SRC-0799EEEB02-L000197](../../agents/tool_execution_status.py#L197) | 197 | `"    social_connector_errors = ["` | — |
| [SRC-0799EEEB02-L000198](../../agents/tool_execution_status.py#L198) | 198 | `"        row for row in social_connector_states"` | — |
| [SRC-0799EEEB02-L000199](../../agents/tool_execution_status.py#L199) | 199 | `"        if row.get(\"status\") in {"` | — |
| [SRC-0799EEEB02-L000200](../../agents/tool_execution_status.py#L200) | 200 | `"            \"failed\", \"error\", \"timeout\", \"http_error\", \"unauthorized\","` | — |
| [SRC-0799EEEB02-L000201](../../agents/tool_execution_status.py#L201) | 201 | `"            \"rate_limited\", \"budget_exhausted\","` | — |
| [SRC-0799EEEB02-L000202](../../agents/tool_execution_status.py#L202) | 202 | `"        }"` | — |
| [SRC-0799EEEB02-L000203](../../agents/tool_execution_status.py#L203) | 203 | `"    ]"` | — |
| [SRC-0799EEEB02-L000204](../../agents/tool_execution_status.py#L204) | 204 | `"    social_configured_connectors = ["` | — |
| [SRC-0799EEEB02-L000205](../../agents/tool_execution_status.py#L205) | 205 | `"        row for row in social_connector_states"` | — |
| [SRC-0799EEEB02-L000206](../../agents/tool_execution_status.py#L206) | 206 | `"        if row.get(\"configured\") is True"` | — |
| [SRC-0799EEEB02-L000207](../../agents/tool_execution_status.py#L207) | 207 | `"    ]"` | — |
| [SRC-0799EEEB02-L000208](../../agents/tool_execution_status.py#L208) | 208 | `"    social_not_configured_connectors = ["` | — |
| [SRC-0799EEEB02-L000209](../../agents/tool_execution_status.py#L209) | 209 | `"        row for row in social_connector_states"` | — |
| [SRC-0799EEEB02-L000210](../../agents/tool_execution_status.py#L210) | 210 | `"        if row.get(\"configured\") is False"` | — |
| [SRC-0799EEEB02-L000211](../../agents/tool_execution_status.py#L211) | 211 | `"    ]"` | — |
| [SRC-0799EEEB02-L000212](../../agents/tool_execution_status.py#L212) | 212 | `"    if tool not in required:"` | — |
| [SRC-0799EEEB02-L000213](../../agents/tool_execution_status.py#L213) | 213 | `"        status = \"not_required\""` | — |
| [SRC-0799EEEB02-L000214](../../agents/tool_execution_status.py#L214) | 214 | `"    elif social_results > 0 or social_sources > 0:"` | — |
| [SRC-0799EEEB02-L000215](../../agents/tool_execution_status.py#L215) | 215 | `"        status = \"completed_with_results\""` | — |
| [SRC-0799EEEB02-L000216](../../agents/tool_execution_status.py#L216) | 216 | `"    elif outcome in _ERROR_OUTCOMES and outcome == \"attempted_research_error\":"` | — |
| [SRC-0799EEEB02-L000217](../../agents/tool_execution_status.py#L217) | 217 | `"        status = \"failed\""` | — |
| [SRC-0799EEEB02-L000218](../../agents/tool_execution_status.py#L218) | 218 | `"    elif outcome in _ERROR_OUTCOMES:"` | — |
| [SRC-0799EEEB02-L000219](../../agents/tool_execution_status.py#L219) | 219 | `"        status = \"unknown\""` | — |
| [SRC-0799EEEB02-L000220](../../agents/tool_execution_status.py#L220) | 220 | `"    elif attempted_social_connectors:"` | — |
| [SRC-0799EEEB02-L000221](../../agents/tool_execution_status.py#L221) | 221 | `"        status = \"failed\" if social_connector_errors else \"completed_no_usable_results\""` | — |
| [SRC-0799EEEB02-L000222](../../agents/tool_execution_status.py#L222) | 222 | `"    elif social_configured_connectors and all("` | — |
| [SRC-0799EEEB02-L000223](../../agents/tool_execution_status.py#L223) | 223 | `"        row.get(\"attempted\") is False for row in social_configured_connectors"` | — |
| [SRC-0799EEEB02-L000224](../../agents/tool_execution_status.py#L224) | 224 | `"    ):"` | — |
| [SRC-0799EEEB02-L000225](../../agents/tool_execution_status.py#L225) | 225 | `"        status = \"not_attempted\""` | — |
| [SRC-0799EEEB02-L000226](../../agents/tool_execution_status.py#L226) | 226 | `"    elif social_not_configured_connectors and ("` | — |
| [SRC-0799EEEB02-L000227](../../agents/tool_execution_status.py#L227) | 227 | `"        not social_configured_connectors or not attempted_social_connectors"` | — |
| [SRC-0799EEEB02-L000228](../../agents/tool_execution_status.py#L228) | 228 | `"    ):"` | — |
| [SRC-0799EEEB02-L000229](../../agents/tool_execution_status.py#L229) | 229 | `"        status = \"not_configured\""` | — |
| [SRC-0799EEEB02-L000230](../../agents/tool_execution_status.py#L230) | 230 | `"    elif raw_social_results is None and not social_connector_states:"` | — |
| [SRC-0799EEEB02-L000231](../../agents/tool_execution_status.py#L231) | 231 | `"        status = \"unknown\""` | — |
| [SRC-0799EEEB02-L000232](../../agents/tool_execution_status.py#L232) | 232 | `"    elif attempted is False:"` | — |
| [SRC-0799EEEB02-L000233](../../agents/tool_execution_status.py#L233) | 233 | `"        status = \"not_attempted\""` | — |
| [SRC-0799EEEB02-L000234](../../agents/tool_execution_status.py#L234) | 234 | `"    else:"` | — |
| [SRC-0799EEEB02-L000235](../../agents/tool_execution_status.py#L235) | 235 | `"        # A general web search attempt is not proof that social connectors ran."` | — |
| [SRC-0799EEEB02-L000236](../../agents/tool_execution_status.py#L236) | 236 | `"        status = \"unknown\""` | — |
| [SRC-0799EEEB02-L000237](../../agents/tool_execution_status.py#L237) | 237 | `"    rows.append(_status_row(tool, tool in required, status, {"` | — |
| [SRC-0799EEEB02-L000238](../../agents/tool_execution_status.py#L238) | 238 | `"        \"social_direct_results\": social_results,"` | — |
| [SRC-0799EEEB02-L000239](../../agents/tool_execution_status.py#L239) | 239 | `"        \"social_result_count_known\": raw_social_results is not None,"` | — |
| [SRC-0799EEEB02-L000240](../../agents/tool_execution_status.py#L240) | 240 | `"        \"accepted_social_sources\": social_sources,"` | — |
| [SRC-0799EEEB02-L000241](../../agents/tool_execution_status.py#L241) | 241 | `"        \"social_connectors_observed\": ["` | — |
| [SRC-0799EEEB02-L000242](../../agents/tool_execution_status.py#L242) | 242 | `"            {"` | — |
| [SRC-0799EEEB02-L000243](../../agents/tool_execution_status.py#L243) | 243 | `"                \"name\": row.get(\"name\"),"` | — |
| [SRC-0799EEEB02-L000244](../../agents/tool_execution_status.py#L244) | 244 | `"                \"configured\": row.get(\"configured\"),"` | — |
| [SRC-0799EEEB02-L000245](../../agents/tool_execution_status.py#L245) | 245 | `"                \"attempted\": row.get(\"attempted\"),"` | — |
| [SRC-0799EEEB02-L000246](../../agents/tool_execution_status.py#L246) | 246 | `"                \"status\": row.get(\"status\"),"` | — |
| [SRC-0799EEEB02-L000247](../../agents/tool_execution_status.py#L247) | 247 | `"            }"` | — |
| [SRC-0799EEEB02-L000248](../../agents/tool_execution_status.py#L248) | 248 | `"            for row in social_connector_states[:8]"` | — |
| [SRC-0799EEEB02-L000249](../../agents/tool_execution_status.py#L249) | 249 | `"        ],"` | — |
| [SRC-0799EEEB02-L000250](../../agents/tool_execution_status.py#L250) | 250 | `"        \"search_outcome\": outcome,"` | — |
| [SRC-0799EEEB02-L000251](../../agents/tool_execution_status.py#L251) | 251 | `"        \"interpretation\": ("` | — |
| [SRC-0799EEEB02-L000252](../../agents/tool_execution_status.py#L252) | 252 | `"            \"A general web search attempt does not prove that a social connector was attempted.\""` | — |
| [SRC-0799EEEB02-L000253](../../agents/tool_execution_status.py#L253) | 253 | `"        ),"` | — |
| [SRC-0799EEEB02-L000254](../../agents/tool_execution_status.py#L254) | 254 | `"    }))"` | — |
| [SRC-0799EEEB02-L000255](../../agents/tool_execution_status.py#L255) | 255 | `""` | — |
| [SRC-0799EEEB02-L000256](../../agents/tool_execution_status.py#L256) | 256 | `"    tool = \"language_model_generation_if_configured\""` | — |
| [SRC-0799EEEB02-L000257](../../agents/tool_execution_status.py#L257) | 257 | `"    final_status = str(output.get(\"final_answer_status\") or \"\")"` | — |
| [SRC-0799EEEB02-L000258](../../agents/tool_execution_status.py#L258) | 258 | `"    used_model = output.get(\"used_language_model\") is True"` | — |
| [SRC-0799EEEB02-L000259](../../agents/tool_execution_status.py#L259) | 259 | `"    if tool not in required:"` | — |
| [SRC-0799EEEB02-L000260](../../agents/tool_execution_status.py#L260) | 260 | `"        status = \"not_required\""` | — |
| [SRC-0799EEEB02-L000261](../../agents/tool_execution_status.py#L261) | 261 | `"    elif used_model:"` | — |
| [SRC-0799EEEB02-L000262](../../agents/tool_execution_status.py#L262) | 262 | `"        status = \"completed\""` | — |
| [SRC-0799EEEB02-L000263](../../agents/tool_execution_status.py#L263) | 263 | `"    elif final_status in {"` | — |
| [SRC-0799EEEB02-L000264](../../agents/tool_execution_status.py#L264) | 264 | `"        \"model_not_configured_fallback\", \"model_not_configured\","` | — |
| [SRC-0799EEEB02-L000265](../../agents/tool_execution_status.py#L265) | 265 | `"    }:"` | — |
| [SRC-0799EEEB02-L000266](../../agents/tool_execution_status.py#L266) | 266 | `"        status = \"not_configured\""` | — |
| [SRC-0799EEEB02-L000267](../../agents/tool_execution_status.py#L267) | 267 | `"    elif final_status in {"` | — |
| [SRC-0799EEEB02-L000268](../../agents/tool_execution_status.py#L268) | 268 | `"        \"generation_failed\", \"generation_failed_with_source_fallback\","` | — |
| [SRC-0799EEEB02-L000269](../../agents/tool_execution_status.py#L269) | 269 | `"        \"budget_exhausted\", \"budget_exhausted_with_source_fallback\","` | — |
| [SRC-0799EEEB02-L000270](../../agents/tool_execution_status.py#L270) | 270 | `"    }:"` | — |
| [SRC-0799EEEB02-L000271](../../agents/tool_execution_status.py#L271) | 271 | `"        status = \"failed\""` | — |
| [SRC-0799EEEB02-L000272](../../agents/tool_execution_status.py#L272) | 272 | `"    elif final_status in {"` | — |
| [SRC-0799EEEB02-L000273](../../agents/tool_execution_status.py#L273) | 273 | `"        \"clarification_required\", \"insufficient_evidence_no_generation\","` | — |
| [SRC-0799EEEB02-L000274](../../agents/tool_execution_status.py#L274) | 274 | `"        \"not_attempted\", \"local_response_no_generation\","` | — |
| [SRC-0799EEEB02-L000275](../../agents/tool_execution_status.py#L275) | 275 | `"    }:"` | — |
| [SRC-0799EEEB02-L000276](../../agents/tool_execution_status.py#L276) | 276 | `"        status = \"not_attempted\""` | — |
| [SRC-0799EEEB02-L000277](../../agents/tool_execution_status.py#L277) | 277 | `"    elif output.get(\"kind\") == \"insufficient_evidence\":"` | — |
| [SRC-0799EEEB02-L000278](../../agents/tool_execution_status.py#L278) | 278 | `"        status = \"not_attempted_no_evidence\""` | — |
| [SRC-0799EEEB02-L000279](../../agents/tool_execution_status.py#L279) | 279 | `"    else:"` | — |
| [SRC-0799EEEB02-L000280](../../agents/tool_execution_status.py#L280) | 280 | `"        status = \"unknown\""` | — |
| [SRC-0799EEEB02-L000281](../../agents/tool_execution_status.py#L281) | 281 | `"    rows.append(_status_row(tool, tool in required, status, {"` | — |
| [SRC-0799EEEB02-L000282](../../agents/tool_execution_status.py#L282) | 282 | `"        \"used_language_model\": used_model,"` | — |
| [SRC-0799EEEB02-L000283](../../agents/tool_execution_status.py#L283) | 283 | `"        \"final_answer_status\": final_status or \"unknown\","` | — |
| [SRC-0799EEEB02-L000284](../../agents/tool_execution_status.py#L284) | 284 | `"    }))"` | — |
| [SRC-0799EEEB02-L000285](../../agents/tool_execution_status.py#L285) | 285 | `""` | — |
| [SRC-0799EEEB02-L000286](../../agents/tool_execution_status.py#L286) | 286 | `"    tool = \"claim_review_if_configured\""` | — |
| [SRC-0799EEEB02-L000287](../../agents/tool_execution_status.py#L287) | 287 | `"    review_status = str("` | — |
| [SRC-0799EEEB02-L000288](../../agents/tool_execution_status.py#L288) | 288 | `"        search_report.get(\"claim_audit\")"` | — |
| [SRC-0799EEEB02-L000289](../../agents/tool_execution_status.py#L289) | 289 | `"        or search_report.get(\"second_pass_review\")"` | — |
| [SRC-0799EEEB02-L000290](../../agents/tool_execution_status.py#L290) | 290 | `"        or \"unknown\""` | — |
| [SRC-0799EEEB02-L000291](../../agents/tool_execution_status.py#L291) | 291 | `"    )"` | — |
| [SRC-0799EEEB02-L000292](../../agents/tool_execution_status.py#L292) | 292 | `"    if tool not in required:"` | — |
| [SRC-0799EEEB02-L000293](../../agents/tool_execution_status.py#L293) | 293 | `"        status = \"not_required\""` | — |
| [SRC-0799EEEB02-L000294](../../agents/tool_execution_status.py#L294) | 294 | `"    elif review_status == \"model_claim_audit_completed\":"` | — |
| [SRC-0799EEEB02-L000295](../../agents/tool_execution_status.py#L295) | 295 | `"        status = \"completed_model_assisted_review\""` | — |
| [SRC-0799EEEB02-L000296](../../agents/tool_execution_status.py#L296) | 296 | `"    elif review_status in {"` | — |
| [SRC-0799EEEB02-L000297](../../agents/tool_execution_status.py#L297) | 297 | `"        \"model_claim_audit_unavailable\", \"review_failed_with_source_fallback\","` | — |
| [SRC-0799EEEB02-L000298](../../agents/tool_execution_status.py#L298) | 298 | `"    }:"` | — |
| [SRC-0799EEEB02-L000299](../../agents/tool_execution_status.py#L299) | 299 | `"        status = \"failed\""` | — |
| [SRC-0799EEEB02-L000300](../../agents/tool_execution_status.py#L300) | 300 | `"    elif review_status in {\"not_run\", \"not_assessed\", \"not_verified\"}:"` | — |
| [SRC-0799EEEB02-L000301](../../agents/tool_execution_status.py#L301) | 301 | `"        status = ("` | — |
| [SRC-0799EEEB02-L000302](../../agents/tool_execution_status.py#L302) | 302 | `"            \"not_attempted_no_evidence\""` | — |
| [SRC-0799EEEB02-L000303](../../agents/tool_execution_status.py#L303) | 303 | `"            if not source_rows else \"not_attempted\""` | — |
| [SRC-0799EEEB02-L000304](../../agents/tool_execution_status.py#L304) | 304 | `"        )"` | — |
| [SRC-0799EEEB02-L000305](../../agents/tool_execution_status.py#L305) | 305 | `"    else:"` | — |
| [SRC-0799EEEB02-L000306](../../agents/tool_execution_status.py#L306) | 306 | `"        status = \"unknown\""` | — |
| [SRC-0799EEEB02-L000307](../../agents/tool_execution_status.py#L307) | 307 | `"    rows.append(_status_row(tool, tool in required, status, {"` | — |
| [SRC-0799EEEB02-L000308](../../agents/tool_execution_status.py#L308) | 308 | `"        \"review_status\": review_status,"` | — |
| [SRC-0799EEEB02-L000309](../../agents/tool_execution_status.py#L309) | 309 | `"        \"independent_fact_check\": False,"` | — |
| [SRC-0799EEEB02-L000310](../../agents/tool_execution_status.py#L310) | 310 | `"    }))"` | — |
| [SRC-0799EEEB02-L000311](../../agents/tool_execution_status.py#L311) | 311 | `"    return rows"` | — |
## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L000001](../../agents/web_agent.py#L1) | 1 | `"\"\"\"Grounded natural-language web research for Omarai."` | — |
| [SRC-1AE03B9EC3-L000002](../../agents/web_agent.py#L2) | 2 | `""` | — |
| [SRC-1AE03B9EC3-L000003](../../agents/web_agent.py#L3) | 3 | `"Searches public web results, extracts a small amount of page text, then asks an"` | — |
| [SRC-1AE03B9EC3-L000004](../../agents/web_agent.py#L4) | 4 | `"OpenAI-compatible language model to answer in the user's language with sources."` | — |
| [SRC-1AE03B9EC3-L000005](../../agents/web_agent.py#L5) | 5 | `"API credentials are read only from environment variables and are never returned."` | — |
| [SRC-1AE03B9EC3-L000006](../../agents/web_agent.py#L6) | 6 | `"\"\"\""` | — |
| [SRC-1AE03B9EC3-L000007](../../agents/web_agent.py#L7) | 7 | `"from __future__ import annotations"` | — |
| [SRC-1AE03B9EC3-L000008](../../agents/web_agent.py#L8) | 8 | `""` | — |
| [SRC-1AE03B9EC3-L000009](../../agents/web_agent.py#L9) | 9 | `"import asyncio"` | — |
| [SRC-1AE03B9EC3-L000010](../../agents/web_agent.py#L10) | 10 | `"import datetime as dt"` | — |
| [SRC-1AE03B9EC3-L000011](../../agents/web_agent.py#L11) | 11 | `"import ipaddress"` | — |
| [SRC-1AE03B9EC3-L000012](../../agents/web_agent.py#L12) | 12 | `"import json"` | — |
| [SRC-1AE03B9EC3-L000013](../../agents/web_agent.py#L13) | 13 | `"import math"` | — |
| [SRC-1AE03B9EC3-L000014](../../agents/web_agent.py#L14) | 14 | `"import os"` | — |
| [SRC-1AE03B9EC3-L000015](../../agents/web_agent.py#L15) | 15 | `"import re"` | — |
| [SRC-1AE03B9EC3-L000016](../../agents/web_agent.py#L16) | 16 | `"import socket"` | — |
| [SRC-1AE03B9EC3-L000017](../../agents/web_agent.py#L17) | 17 | `"import threading"` | — |
| [SRC-1AE03B9EC3-L000018](../../agents/web_agent.py#L18) | 18 | `"import time"` | — |
| [SRC-1AE03B9EC3-L000019](../../agents/web_agent.py#L19) | 19 | `"import unicodedata"` | — |
| [SRC-1AE03B9EC3-L000020](../../agents/web_agent.py#L20) | 20 | `"import urllib.error"` | — |
| [SRC-1AE03B9EC3-L000021](../../agents/web_agent.py#L21) | 21 | `"import urllib.parse"` | — |
| [SRC-1AE03B9EC3-L000022](../../agents/web_agent.py#L22) | 22 | `"import urllib.request"` | — |
| [SRC-1AE03B9EC3-L000023](../../agents/web_agent.py#L23) | 23 | `"from concurrent.futures import ThreadPoolExecutor, as_completed"` | — |
| [SRC-1AE03B9EC3-L000024](../../agents/web_agent.py#L24) | 24 | `"from typing import Any"` | — |
| [SRC-1AE03B9EC3-L000025](../../agents/web_agent.py#L25) | 25 | `""` | — |
| [SRC-1AE03B9EC3-L000026](../../agents/web_agent.py#L26) | 26 | `"from agents.intent_router import resolve_followup_query, route_intent"` | — |
| [SRC-1AE03B9EC3-L000027](../../agents/web_agent.py#L27) | 27 | `"from agents.sales_domain import ProductProfile, build_buyer_queries"` | — |
| [SRC-1AE03B9EC3-L000028](../../agents/web_agent.py#L28) | 28 | `"from agents.dialogue_state import ("` | — |
| [SRC-1AE03B9EC3-L000029](../../agents/web_agent.py#L29) | 29 | `"    fallback_dialogue_context,"` | — |
| [SRC-1AE03B9EC3-L000030](../../agents/web_agent.py#L30) | 30 | `"    might_be_context_dependent,"` | — |
| [SRC-1AE03B9EC3-L000031](../../agents/web_agent.py#L31) | 31 | `"    validate_dialogue_context,"` | — |
| [SRC-1AE03B9EC3-L000032](../../agents/web_agent.py#L32) | 32 | `")"` | — |
| [SRC-1AE03B9EC3-L000033](../../agents/web_agent.py#L33) | 33 | `"from agents.answer_validation import audit_answer_integrity"` | — |
| [SRC-1AE03B9EC3-L000034](../../agents/web_agent.py#L34) | 34 | `"from agents.requirement_evidence import build_requirement_evidence_ledger"` | — |
| [SRC-1AE03B9EC3-L000035](../../agents/web_agent.py#L35) | 35 | `"from agents.claim_evidence import build_claim_evidence_ledger"` | — |
| [SRC-1AE03B9EC3-L000036](../../agents/web_agent.py#L36) | 36 | `"from agents.semantic_claim_verifier import ("` | — |
| [SRC-1AE03B9EC3-L000037](../../agents/web_agent.py#L37) | 37 | `"    build_semantic_verification_request,"` | — |
| [SRC-1AE03B9EC3-L000038](../../agents/web_agent.py#L38) | 38 | `"    parse_semantic_verification_response,"` | — |
| [SRC-1AE03B9EC3-L000039](../../agents/web_agent.py#L39) | 39 | `")"` | — |
| [SRC-1AE03B9EC3-L000040](../../agents/web_agent.py#L40) | 40 | `"from agents.request_budget import RequestBudget, RequestBudgetExceeded"` | — |
| [SRC-1AE03B9EC3-L000041](../../agents/web_agent.py#L41) | 41 | `"from agents.aspect_planning import ("` | — |
| [SRC-1AE03B9EC3-L000042](../../agents/web_agent.py#L42) | 42 | `"    arabic_aspect_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L000043](../../agents/web_agent.py#L43) | 43 | `"    build_evidence_ledger,"` | — |
| [SRC-1AE03B9EC3-L000044](../../agents/web_agent.py#L44) | 44 | `"    extract_aspects,"` | — |
| [SRC-1AE03B9EC3-L000045](../../agents/web_agent.py#L45) | 45 | `"    repair_queries_for_missing_aspects,"` | — |
| [SRC-1AE03B9EC3-L000046](../../agents/web_agent.py#L46) | 46 | `")"` | — |
| [SRC-1AE03B9EC3-L000047](../../agents/web_agent.py#L47) | 47 | `"from agents.search_connectors import search_arxiv, search_crossref, search_openalex"` | — |
| [SRC-1AE03B9EC3-L000048](../../agents/web_agent.py#L48) | 48 | `"from agents.research import ("` | — |
| [SRC-1AE03B9EC3-L000049](../../agents/web_agent.py#L49) | 49 | `"    MAX_PLAN_QUERIES,"` | — |
| [SRC-1AE03B9EC3-L000050](../../agents/web_agent.py#L50) | 50 | `"    SOCIAL_DOMAINS,"` | — |
| [SRC-1AE03B9EC3-L000051](../../agents/web_agent.py#L51) | 51 | `"    compact_search_query,"` | — |
| [SRC-1AE03B9EC3-L000052](../../agents/web_agent.py#L52) | 52 | `"    evidence_signal_report,"` | — |
| [SRC-1AE03B9EC3-L000053](../../agents/web_agent.py#L53) | 53 | `"    fallback_plan,"` | — |
| [SRC-1AE03B9EC3-L000054](../../agents/web_agent.py#L54) | 54 | `"    fuse_ranked_results,"` | — |
| [SRC-1AE03B9EC3-L000055](../../agents/web_agent.py#L55) | 55 | `"    registrable_domain,"` | — |
| [SRC-1AE03B9EC3-L000056](../../agents/web_agent.py#L56) | 56 | `"    extract_question_coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L000057](../../agents/web_agent.py#L57) | 57 | `"    validate_plan,"` | — |
| [SRC-1AE03B9EC3-L000058](../../agents/web_agent.py#L58) | 58 | `")"` | — |
| [SRC-1AE03B9EC3-L000059](../../agents/web_agent.py#L59) | 59 | `"from agents.research_guardrails import apply_source_guardrails"` | — |
| [SRC-1AE03B9EC3-L000060](../../agents/web_agent.py#L60) | 60 | `"from agents.research_completion import build_research_completion"` | — |
| [SRC-1AE03B9EC3-L000061](../../agents/web_agent.py#L61) | 61 | `"from agents.tool_execution_status import build_tool_execution_matrix"` | — |
| [SRC-1AE03B9EC3-L000062](../../agents/web_agent.py#L62) | 62 | `"from agents.task_understanding import ("` | — |
| [SRC-1AE03B9EC3-L000063](../../agents/web_agent.py#L63) | 63 | `"    reasoning_guidance_for_task_spec,"` | — |
| [SRC-1AE03B9EC3-L000064](../../agents/web_agent.py#L64) | 64 | `"    validate_task_spec,"` | — |
| [SRC-1AE03B9EC3-L000065](../../agents/web_agent.py#L65) | 65 | `")"` | — |
| [SRC-1AE03B9EC3-L000066](../../agents/web_agent.py#L66) | 66 | `"from agents.task_understanding import build_query_strategy_matrix, build_task_spec"` | — |
| [SRC-1AE03B9EC3-L000067](../../agents/web_agent.py#L67) | 67 | `"from agents.research_pipeline import build_research_pipeline, evaluate_research_evidence"` | — |
| [SRC-1AE03B9EC3-L000068](../../agents/web_agent.py#L68) | 68 | `""` | — |
| [SRC-1AE03B9EC3-L000069](../../agents/web_agent.py#L69) | 69 | `"MAX_QUESTION_CHARS = 4000"` | — |
| [SRC-1AE03B9EC3-L000070](../../agents/web_agent.py#L70) | 70 | `"MAX_HISTORY_ITEMS = 8"` | — |
| [SRC-1AE03B9EC3-L000071](../../agents/web_agent.py#L71) | 71 | `"MAX_HISTORY_CHARS = 4000"` | — |
| [SRC-1AE03B9EC3-L000072](../../agents/web_agent.py#L72) | 72 | `"MAX_SEARCH_RESULTS = 18"` | — |
| [SRC-1AE03B9EC3-L000073](../../agents/web_agent.py#L73) | 73 | `"MAX_PROVIDER_RESULTS = 6"` | — |
| [SRC-1AE03B9EC3-L000074](../../agents/web_agent.py#L74) | 74 | `"MAX_PROVIDER_RESPONSE_BYTES = 2_000_000"` | — |
| [SRC-1AE03B9EC3-L000075](../../agents/web_agent.py#L75) | 75 | `""` | — |
| [SRC-1AE03B9EC3-L000076](../../agents/web_agent.py#L76) | 76 | `"def _bounded_http_request(method: str, url: str, **kwargs):"` | — |
| [SRC-1AE03B9EC3-L000077](../../agents/web_agent.py#L77) | 77 | `"    \"\"\"Perform one no-redirect provider request with a strict decoded-body byte cap.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000078](../../agents/web_agent.py#L78) | 78 | `"    import httpx"` | — |
| [SRC-1AE03B9EC3-L000079](../../agents/web_agent.py#L79) | 79 | `""` | — |
| [SRC-1AE03B9EC3-L000080](../../agents/web_agent.py#L80) | 80 | `"    timeout = kwargs.pop(\"timeout\", 9.0)"` | — |
| [SRC-1AE03B9EC3-L000081](../../agents/web_agent.py#L81) | 81 | `"    total_timeout = kwargs.pop(\"total_timeout\", timeout)"` | — |
| [SRC-1AE03B9EC3-L000082](../../agents/web_agent.py#L82) | 82 | `"    try:"` | — |
| [SRC-1AE03B9EC3-L000083](../../agents/web_agent.py#L83) | 83 | `"        total_timeout = float(total_timeout)"` | — |
| [SRC-1AE03B9EC3-L000084](../../agents/web_agent.py#L84) | 84 | `"    except (TypeError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L000085](../../agents/web_agent.py#L85) | 85 | `"        raise ValueError(\"total_timeout must be a positive number\") from exc"` | — |
| [SRC-1AE03B9EC3-L000086](../../agents/web_agent.py#L86) | 86 | `"    if not math.isfinite(total_timeout) or total_timeout <= 0:"` | — |
| [SRC-1AE03B9EC3-L000087](../../agents/web_agent.py#L87) | 87 | `"        raise ValueError(\"total_timeout must be a positive number\")"` | — |
| [SRC-1AE03B9EC3-L000088](../../agents/web_agent.py#L88) | 88 | `"    deadline = time.monotonic() + total_timeout"` | — |
| [SRC-1AE03B9EC3-L000089](../../agents/web_agent.py#L89) | 89 | `"    # Redirects are never followed for search/social APIs, including credentialed calls."` | — |
| [SRC-1AE03B9EC3-L000090](../../agents/web_agent.py#L90) | 90 | `"    kwargs.pop(\"follow_redirects\", None)"` | — |
| [SRC-1AE03B9EC3-L000091](../../agents/web_agent.py#L91) | 91 | `"    with httpx.Client("` | — |
| [SRC-1AE03B9EC3-L000092](../../agents/web_agent.py#L92) | 92 | `"        timeout=timeout,"` | — |
| [SRC-1AE03B9EC3-L000093](../../agents/web_agent.py#L93) | 93 | `"        follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L000094](../../agents/web_agent.py#L94) | 94 | `"        trust_env=False,"` | — |
| [SRC-1AE03B9EC3-L000095](../../agents/web_agent.py#L95) | 95 | `"    ) as client, client.stream(method, url, **kwargs) as response:"` | — |
| [SRC-1AE03B9EC3-L000096](../../agents/web_agent.py#L96) | 96 | `"        declared_length = response.headers.get(\"content-length\")"` | — |
| [SRC-1AE03B9EC3-L000097](../../agents/web_agent.py#L97) | 97 | `"        if declared_length:"` | — |
| [SRC-1AE03B9EC3-L000098](../../agents/web_agent.py#L98) | 98 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L000099](../../agents/web_agent.py#L99) | 99 | `"                declared_bytes = int(declared_length)"` | — |
| [SRC-1AE03B9EC3-L000100](../../agents/web_agent.py#L100) | 100 | `"            except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L000101](../../agents/web_agent.py#L101) | 101 | `"                declared_bytes = None"` | — |
| [SRC-1AE03B9EC3-L000102](../../agents/web_agent.py#L102) | 102 | `"            if ("` | — |
| [SRC-1AE03B9EC3-L000103](../../agents/web_agent.py#L103) | 103 | `"                declared_bytes is not None"` | — |
| [SRC-1AE03B9EC3-L000104](../../agents/web_agent.py#L104) | 104 | `"                and declared_bytes > MAX_PROVIDER_RESPONSE_BYTES"` | — |
| [SRC-1AE03B9EC3-L000105](../../agents/web_agent.py#L105) | 105 | `"            ):"` | — |
| [SRC-1AE03B9EC3-L000106](../../agents/web_agent.py#L106) | 106 | `"                raise ValueError("` | — |
| [SRC-1AE03B9EC3-L000107](../../agents/web_agent.py#L107) | 107 | `"                    \"search provider response exceeds the configured size limit\""` | — |
| [SRC-1AE03B9EC3-L000108](../../agents/web_agent.py#L108) | 108 | `"                )"` | — |
| [SRC-1AE03B9EC3-L000109](../../agents/web_agent.py#L109) | 109 | `"        body = bytearray()"` | — |
| [SRC-1AE03B9EC3-L000110](../../agents/web_agent.py#L110) | 110 | `"        chunks = iter(response.iter_bytes())"` | — |
| [SRC-1AE03B9EC3-L000111](../../agents/web_agent.py#L111) | 111 | `"        while True:"` | — |
| [SRC-1AE03B9EC3-L000112](../../agents/web_agent.py#L112) | 112 | `"            # timeout limits idle waits; this deadline also limits a slow trickle"` | — |
| [SRC-1AE03B9EC3-L000113](../../agents/web_agent.py#L113) | 113 | `"            # where each chunk arrives just before the per-read timeout."` | — |
| [SRC-1AE03B9EC3-L000114](../../agents/web_agent.py#L114) | 114 | `"            if time.monotonic() >= deadline:"` | — |
| [SRC-1AE03B9EC3-L000115](../../agents/web_agent.py#L115) | 115 | `"                raise TimeoutError(\"search provider exceeded the total request deadline\")"` | — |
| [SRC-1AE03B9EC3-L000116](../../agents/web_agent.py#L116) | 116 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L000117](../../agents/web_agent.py#L117) | 117 | `"                chunk = next(chunks)"` | — |
| [SRC-1AE03B9EC3-L000118](../../agents/web_agent.py#L118) | 118 | `"            except StopIteration:"` | — |
| [SRC-1AE03B9EC3-L000119](../../agents/web_agent.py#L119) | 119 | `"                break"` | — |
| [SRC-1AE03B9EC3-L000120](../../agents/web_agent.py#L120) | 120 | `"            if len(body) + len(chunk) > MAX_PROVIDER_RESPONSE_BYTES:"` | — |
| [SRC-1AE03B9EC3-L000121](../../agents/web_agent.py#L121) | 121 | `"                raise ValueError("` | — |
| [SRC-1AE03B9EC3-L000122](../../agents/web_agent.py#L122) | 122 | `"                    \"search provider response exceeds the configured size limit\""` | — |
| [SRC-1AE03B9EC3-L000123](../../agents/web_agent.py#L123) | 123 | `"                )"` | — |
| [SRC-1AE03B9EC3-L000124](../../agents/web_agent.py#L124) | 124 | `"            body.extend(chunk)"` | — |
| [SRC-1AE03B9EC3-L000125](../../agents/web_agent.py#L125) | 125 | `"        return httpx.Response("` | — |
| [SRC-1AE03B9EC3-L000126](../../agents/web_agent.py#L126) | 126 | `"            status_code=response.status_code,"` | — |
| [SRC-1AE03B9EC3-L000127](../../agents/web_agent.py#L127) | 127 | `"            headers=response.headers,"` | — |
| [SRC-1AE03B9EC3-L000128](../../agents/web_agent.py#L128) | 128 | `"            content=bytes(body),"` | — |
| [SRC-1AE03B9EC3-L000129](../../agents/web_agent.py#L129) | 129 | `"            request=response.request,"` | — |
| [SRC-1AE03B9EC3-L000130](../../agents/web_agent.py#L130) | 130 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000131](../../agents/web_agent.py#L131) | 131 | `"MAX_FETCHED_PAGES = 8"` | — |
| [SRC-1AE03B9EC3-L000132](../../agents/web_agent.py#L132) | 132 | `"MAX_LLM_CITED_SOURCES = 12"` | — |
| [SRC-1AE03B9EC3-L000133](../../agents/web_agent.py#L133) | 133 | `"MAX_RESEARCH_WORKERS = 8"` | — |
| [SRC-1AE03B9EC3-L000134](../../agents/web_agent.py#L134) | 134 | `"MAX_PAGE_BYTES = 1_000_000"` | — |
| [SRC-1AE03B9EC3-L000135](../../agents/web_agent.py#L135) | 135 | `"MAX_PAGE_TEXT_CHARS = 12_000"` | — |
| [SRC-1AE03B9EC3-L000136](../../agents/web_agent.py#L136) | 136 | `"LLM_TIMEOUT_SECONDS = 35"` | — |
| [SRC-1AE03B9EC3-L000137](../../agents/web_agent.py#L137) | 137 | `""` | — |
| [SRC-1AE03B9EC3-L000138](../../agents/web_agent.py#L138) | 138 | `"# Only completed connector result-processing states positively confirm an attempt."` | — |
| [SRC-1AE03B9EC3-L000139](../../agents/web_agent.py#L139) | 139 | `"# A generic \"failed\" or timeout diagnostic may occur before a network request is sent."` | — |
| [SRC-1AE03B9EC3-L000140](../../agents/web_agent.py#L140) | 140 | `"_SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES = frozenset({\"ok\", \"no_results\", \"filtered_all\"})"` | — |
| [SRC-1AE03B9EC3-L000141](../../agents/web_agent.py#L141) | 141 | `"_RESEARCH_ERROR_OUTCOMES = frozenset({\"attempted_research_error\", \"unknown_after_research_error\"})"` | — |
| [SRC-1AE03B9EC3-L000142](../../agents/web_agent.py#L142) | 142 | `"_PROVIDER_REJECTION_REASONS = ("` | — |
| [SRC-1AE03B9EC3-L000143](../../agents/web_agent.py#L143) | 143 | `"    \"malformed_candidate\","` | — |
| [SRC-1AE03B9EC3-L000144](../../agents/web_agent.py#L144) | 144 | `"    \"invalid_url_or_unsafe_target\","` | — |
| [SRC-1AE03B9EC3-L000145](../../agents/web_agent.py#L145) | 145 | `"    \"blocked_domain\","` | — |
| [SRC-1AE03B9EC3-L000146](../../agents/web_agent.py#L146) | 146 | `"    \"relevance_below_threshold\","` | — |
| [SRC-1AE03B9EC3-L000147](../../agents/web_agent.py#L147) | 147 | `")"` | — |
| [SRC-1AE03B9EC3-L000148](../../agents/web_agent.py#L148) | 148 | `""` | — |
| [SRC-1AE03B9EC3-L000149](../../agents/web_agent.py#L149) | 149 | `"_ARABIC_SEARCH_TRANSLATION = str.maketrans({"` | — |
| [SRC-1AE03B9EC3-L000150](../../agents/web_agent.py#L150) | 150 | `"    \"أ\": \"ا\", \"إ\": \"ا\", \"آ\": \"ا\", \"ٱ\": \"ا\", \"ى\": \"ي\","` | — |
| [SRC-1AE03B9EC3-L000151](../../agents/web_agent.py#L151) | 151 | `"    \"ؤ\": \"و\", \"ئ\": \"ي\", \"ة\": \"ه\", \"ـ\": \"\","` | — |
| [SRC-1AE03B9EC3-L000152](../../agents/web_agent.py#L152) | 152 | `"})"` | — |
| [SRC-1AE03B9EC3-L000153](../../agents/web_agent.py#L153) | 153 | `"_ARABIC_DIACRITICS_RE = re.compile(r\"[\\u0610-\\u061A\\u064B-\\u065F\\u0670\\u06D6-\\u06ED]\")"` | — |
| [SRC-1AE03B9EC3-L000154](../../agents/web_agent.py#L154) | 154 | `"_SEARCH_STOPWORDS = frozenset({"` | — |
| [SRC-1AE03B9EC3-L000155](../../agents/web_agent.py#L155) | 155 | `"    \"ما\", \"ماذا\", \"من\", \"في\", \"على\", \"عن\", \"الى\", \"إلى\", \"و\", \"او\", \"أو\","` | — |
| [SRC-1AE03B9EC3-L000156](../../agents/web_agent.py#L156) | 156 | `"    \"هل\", \"هو\", \"هي\", \"هذا\", \"هذه\", \"ذلك\", \"تلك\", \"التي\", \"الذي\", \"مع\","` | — |
| [SRC-1AE03B9EC3-L000157](../../agents/web_agent.py#L157) | 157 | `"    \"بين\", \"كيف\", \"لماذا\", \"كم\", \"كان\", \"كانت\", \"يكون\", \"تكون\", \"لي\","` | — |
| [SRC-1AE03B9EC3-L000158](../../agents/web_agent.py#L158) | 158 | `"    \"the\", \"a\", \"an\", \"and\", \"or\", \"in\", \"on\", \"of\", \"to\", \"for\", \"with\","` | — |
| [SRC-1AE03B9EC3-L000159](../../agents/web_agent.py#L159) | 159 | `"    \"is\", \"are\", \"was\", \"were\", \"what\", \"which\", \"who\", \"how\", \"why\", \"when\","` | — |
| [SRC-1AE03B9EC3-L000160](../../agents/web_agent.py#L160) | 160 | `"    \"where\", \"compare\", \"comparison\", \"please\", \"show\", \"find\", \"latest\","` | — |
| [SRC-1AE03B9EC3-L000161](../../agents/web_agent.py#L161) | 161 | `"    \"news\", \"official\", \"sources\", \"source\", \"reports\", \"report\", \"analysis\","` | — |
| [SRC-1AE03B9EC3-L000162](../../agents/web_agent.py#L162) | 162 | `"    \"site\", \"com\", \"org\", \"net\", \"www\","` | — |
| [SRC-1AE03B9EC3-L000163](../../agents/web_agent.py#L163) | 163 | `"    # Arabic request/format words are not useful topic concepts for matching search snippets."` | — |
| [SRC-1AE03B9EC3-L000164](../../agents/web_agent.py#L164) | 164 | `"    \"اذكر\", \"مصدر\", \"مصادر\", \"موثوق\", \"موثوقة\", \"رابط\", \"روابط\", \"مباشر\","` | — |
| [SRC-1AE03B9EC3-L000165](../../agents/web_agent.py#L165) | 165 | `"    \"مباشرة\", \"اجب\", \"بالعربية\", \"العربية\", \"بايجاز\", \"بالايجاز\", \"ايجاز\","` | — |
| [SRC-1AE03B9EC3-L000166](../../agents/web_agent.py#L166) | 166 | `"    \"باختصار\", \"اختصار\", \"استخدم\", \"اعرض\", \"وضح\", \"حلل\", \"قارن\", \"متعددة\","` | — |
| [SRC-1AE03B9EC3-L000167](../../agents/web_agent.py#L167) | 167 | `"    \"اهم\", \"الحقائق\", \"حقائق\", \"استنتاج\", \"استنتاجات\", \"الاستنتاجات\","` | — |
| [SRC-1AE03B9EC3-L000168](../../agents/web_agent.py#L168) | 168 | `"    \"تواريخ\", \"تاريخ\", \"الاخبار\", \"اخبار\", \"المصادر\", \"معلومات\", \"قديمة\","` | — |
| [SRC-1AE03B9EC3-L000169](../../agents/web_agent.py#L169) | 169 | `"    \"قديمه\", \"جديدة\", \"جديده\", \"خلال\", \"الايام\", \"ايام\", \"السبعة\", \"سبعة\","` | — |
| [SRC-1AE03B9EC3-L000170](../../agents/web_agent.py#L170) | 170 | `"    \"الماضية\", \"ماضية\", \"الاسبوع\", \"حاليا\", \"الان\", \"احدث\", \"ولا\","` | — |
| [SRC-1AE03B9EC3-L000171](../../agents/web_agent.py#L171) | 171 | `"    \"تعرض\", \"باعتبارها\","` | — |
| [SRC-1AE03B9EC3-L000172](../../agents/web_agent.py#L172) | 172 | `"})"` | — |
| [SRC-1AE03B9EC3-L000173](../../agents/web_agent.py#L173) | 173 | `"# Search-expansion modifiers are useful after a real topic, but must not stand in"` | — |
| [SRC-1AE03B9EC3-L000174](../../agents/web_agent.py#L174) | 174 | `"# for a topic if a future planner/expansion path loses its subject."` | — |
| [SRC-1AE03B9EC3-L000175](../../agents/web_agent.py#L175) | 175 | `"_GENERIC_QUERY_MODIFIER_TOKENS = frozenset({"` | — |
| [SRC-1AE03B9EC3-L000176](../../agents/web_agent.py#L176) | 176 | `"    \"risk\", \"risks\", \"limitation\", \"limitations\", \"alternative\", \"alternatives\","` | — |
| [SRC-1AE03B9EC3-L000177](../../agents/web_agent.py#L177) | 177 | `"    \"recent\", \"data\", \"review\", \"reviews\", \"comparison\", \"compare\", \"official\","` | — |
| [SRC-1AE03B9EC3-L000178](../../agents/web_agent.py#L178) | 178 | `"    \"primary\", \"source\", \"sources\", \"evidence\", \"report\", \"reports\", \"case\", \"cases\","` | — |
| [SRC-1AE03B9EC3-L000179](../../agents/web_agent.py#L179) | 179 | `"    \"study\", \"studies\", \"analysis\", \"latest\", \"news\", \"update\", \"updates\","` | — |
| [SRC-1AE03B9EC3-L000180](../../agents/web_agent.py#L180) | 180 | `"    \"announcement\", \"announcements\", \"comprehensive\", \"research\", \"statistic\","` | — |
| [SRC-1AE03B9EC3-L000181](../../agents/web_agent.py#L181) | 181 | `"    \"statistics\", \"trend\", \"trends\","` | — |
| [SRC-1AE03B9EC3-L000182](../../agents/web_agent.py#L182) | 182 | `"})"` | — |
| [SRC-1AE03B9EC3-L000183](../../agents/web_agent.py#L183) | 183 | `"_SEARCH_SYNONYMS = {"` | — |
| [SRC-1AE03B9EC3-L000184](../../agents/web_agent.py#L184) | 184 | `"    \"استراليا\": {\"australia\"}, \"عاصمة\": {\"capital\"}, \"مصر\": {\"egypt\"},"` | — |
| [SRC-1AE03B9EC3-L000185](../../agents/web_agent.py#L185) | 185 | `"    \"المصري\": {\"egyptian\", \"egypt\"}, \"مركزي\": {\"central\"},"` | — |
| [SRC-1AE03B9EC3-L000186](../../agents/web_agent.py#L186) | 186 | `"    \"المركزي\": {\"central\"}, \"بنك\": {\"bank\"}, \"البنك\": {\"bank\"},"` | — |
| [SRC-1AE03B9EC3-L000187](../../agents/web_agent.py#L187) | 187 | `"    \"قرار\": {\"decision\"}, \"قرارات\": {\"decision\", \"decisions\"},"` | — |
| [SRC-1AE03B9EC3-L000188](../../agents/web_agent.py#L188) | 188 | `"    \"سعر\": {\"price\"}, \"اسعار\": {\"prices\"}, \"استضافة\": {\"hosting\"},"` | — |
| [SRC-1AE03B9EC3-L000189](../../agents/web_agent.py#L189) | 189 | `"    \"شركة\": {\"company\"}, \"شركه\": {\"company\"}, \"ناشئة\": {\"startup\"},"` | — |
| [SRC-1AE03B9EC3-L000190](../../agents/web_agent.py#L190) | 190 | `"    \"صعيد\": {\"upper\"}, \"مقارنة\": {\"compare\", \"comparison\"},"` | — |
| [SRC-1AE03B9EC3-L000191](../../agents/web_agent.py#L191) | 191 | `"    \"تقنية\": {\"technology\"}, \"تقنيات\": {\"technology\"},"` | — |
| [SRC-1AE03B9EC3-L000192](../../agents/web_agent.py#L192) | 192 | `"    \"ميكروسوفت\": {\"microsoft\"}, \"مايكروسوفت\": {\"microsoft\"},"` | — |
| [SRC-1AE03B9EC3-L000193](../../agents/web_agent.py#L193) | 193 | `"    \"microsoft\": {\"ميكروسوفت\", \"مايكروسوفت\"},"` | — |
| [SRC-1AE03B9EC3-L000194](../../agents/web_agent.py#L194) | 194 | `"    \"جمهورية\": {\"republic\"}, \"republic\": {\"جمهورية\"},"` | — |
| [SRC-1AE03B9EC3-L000195](../../agents/web_agent.py#L195) | 195 | `"    \"الرقمية\": {\"digital\"}, \"رقمية\": {\"digital\"},"` | — |
| [SRC-1AE03B9EC3-L000196](../../agents/web_agent.py#L196) | 196 | `"    \"الرقميه\": {\"digital\"}, \"رقميه\": {\"digital\"},"` | — |
| [SRC-1AE03B9EC3-L000197](../../agents/web_agent.py#L197) | 197 | `"    \"موقع\": {\"website\", \"portal\"}, \"مواقع\": {\"websites\", \"portals\"},"` | — |
| [SRC-1AE03B9EC3-L000198](../../agents/web_agent.py#L198) | 198 | `"    \"التجمع\": {\"settlement\"}, \"تجمع\": {\"settlement\"},"` | — |
| [SRC-1AE03B9EC3-L000199](../../agents/web_agent.py#L199) | 199 | `"    \"الخامس\": {\"fifth\", \"5th\"}, \"خامس\": {\"fifth\", \"5th\"},"` | — |
| [SRC-1AE03B9EC3-L000200](../../agents/web_agent.py#L200) | 200 | `"    \"شقة\": {\"apartment\", \"flat\"}, \"شقق\": {\"apartments\", \"flats\"},"` | — |
| [SRC-1AE03B9EC3-L000201](../../agents/web_agent.py#L201) | 201 | `"    \"عميل\": {\"customer\", \"buyer\"}, \"عملاء\": {\"customers\", \"buyers\"},"` | — |
| [SRC-1AE03B9EC3-L000202](../../agents/web_agent.py#L202) | 202 | `"    \"شراء\": {\"buy\", \"purchase\"}, \"مشتري\": {\"buyer\"},"` | — |
| [SRC-1AE03B9EC3-L000203](../../agents/web_agent.py#L203) | 203 | `"    # Small, explicit Arabic-English topic vocabulary; this helps Arabic prompts"` | — |
| [SRC-1AE03B9EC3-L000204](../../agents/web_agent.py#L204) | 204 | `"    # match English-indexed results without relaxing URL or destination safety."` | — |
| [SRC-1AE03B9EC3-L000205](../../agents/web_agent.py#L205) | 205 | `"    \"سيارة\": {\"car\", \"vehicle\"}, \"السيارة\": {\"car\", \"vehicle\"},"` | — |
| [SRC-1AE03B9EC3-L000206](../../agents/web_agent.py#L206) | 206 | `"    \"سيارات\": {\"cars\", \"vehicles\"}, \"السيارات\": {\"cars\", \"vehicles\"},"` | — |
| [SRC-1AE03B9EC3-L000207](../../agents/web_agent.py#L207) | 207 | `"    \"كهربائي\": {\"electric\"}, \"كهربائية\": {\"electric\"},"` | — |
| [SRC-1AE03B9EC3-L000208](../../agents/web_agent.py#L208) | 208 | `"    \"الكهربائي\": {\"electric\"}, \"الكهربائية\": {\"electric\"},"` | — |
| [SRC-1AE03B9EC3-L000209](../../agents/web_agent.py#L209) | 209 | `"    \"شحن\": {\"charging\", \"charge\"}, \"الشحن\": {\"charging\", \"charge\"},"` | — |
| [SRC-1AE03B9EC3-L000210](../../agents/web_agent.py#L210) | 210 | `"    \"شاحن\": {\"charger\"}, \"بطارية\": {\"battery\"}, \"بطاريات\": {\"batteries\"},"` | — |
| [SRC-1AE03B9EC3-L000211](../../agents/web_agent.py#L211) | 211 | `"    \"تكلفة\": {\"cost\", \"costs\"}, \"التكلفة\": {\"cost\", \"costs\"},"` | — |
| [SRC-1AE03B9EC3-L000212](../../agents/web_agent.py#L212) | 212 | `"    \"البنية\": {\"infrastructure\"}, \"التحتية\": {\"infrastructure\"},"` | — |
| [SRC-1AE03B9EC3-L000213](../../agents/web_agent.py#L213) | 213 | `"    \"تحدي\": {\"challenge\"}, \"تحديات\": {\"challenges\"}, \"التحديات\": {\"challenges\"},"` | — |
| [SRC-1AE03B9EC3-L000214](../../agents/web_agent.py#L214) | 214 | `"    \"وكيل\": {\"agent\"}, \"الوكيل\": {\"agent\"},"` | — |
| [SRC-1AE03B9EC3-L000215](../../agents/web_agent.py#L215) | 215 | `"    \"وكلاء\": {\"agents\"}, \"الوكلاء\": {\"agents\"},"` | — |
| [SRC-1AE03B9EC3-L000216](../../agents/web_agent.py#L216) | 216 | `"    # Bilingual vocabulary for AI use-case searches. Keep the relevance floor"` | — |
| [SRC-1AE03B9EC3-L000217](../../agents/web_agent.py#L217) | 217 | `"    # unchanged; expand only concepts that commonly appear in Arabic news titles."` | — |
| [SRC-1AE03B9EC3-L000218](../../agents/web_agent.py#L218) | 218 | `"    \"استخدام\": {\"use\", \"usage\", \"application\", \"applications\"},"` | — |
| [SRC-1AE03B9EC3-L000219](../../agents/web_agent.py#L219) | 219 | `"    \"استخدامات\": {\"use\", \"usage\", \"application\", \"applications\"},"` | — |
| [SRC-1AE03B9EC3-L000220](../../agents/web_agent.py#L220) | 220 | `"    \"استعمال\": {\"use\", \"usage\", \"application\"},"` | — |
| [SRC-1AE03B9EC3-L000221](../../agents/web_agent.py#L221) | 221 | `"    \"استعمالات\": {\"use\", \"usage\", \"applications\"},"` | — |
| [SRC-1AE03B9EC3-L000222](../../agents/web_agent.py#L222) | 222 | `"    \"حالة\": {\"case\"}, \"حالات\": {\"cases\", \"case\"},"` | — |
| [SRC-1AE03B9EC3-L000223](../../agents/web_agent.py#L223) | 223 | `"    \"اعمال\": {\"business\", \"businesses\", \"work\"},"` | — |
| [SRC-1AE03B9EC3-L000224](../../agents/web_agent.py#L224) | 224 | `"    \"الاعمال\": {\"business\", \"businesses\", \"work\"},"` | — |
| [SRC-1AE03B9EC3-L000225](../../agents/web_agent.py#L225) | 225 | `"    \"للاعمال\": {\"business\", \"businesses\", \"work\"},"` | — |
| [SRC-1AE03B9EC3-L000226](../../agents/web_agent.py#L226) | 226 | `"    \"شركات\": {\"company\", \"companies\", \"business\", \"businesses\"},"` | — |
| [SRC-1AE03B9EC3-L000227](../../agents/web_agent.py#L227) | 227 | `"    \"الشركات\": {\"company\", \"companies\", \"business\", \"businesses\"},"` | — |
| [SRC-1AE03B9EC3-L000228](../../agents/web_agent.py#L228) | 228 | `"    \"صغير\": {\"small\"}, \"صغيرة\": {\"small\"}, \"الصغير\": {\"small\"}, \"الصغيرة\": {\"small\"},"` | — |
| [SRC-1AE03B9EC3-L000229](../../agents/web_agent.py#L229) | 229 | `"    \"ذكاء\": {\"intelligence\", \"ai\"}, \"الذكاء\": {\"intelligence\", \"ai\"},"` | — |
| [SRC-1AE03B9EC3-L000230](../../agents/web_agent.py#L230) | 230 | `"    \"اصطناعي\": {\"artificial\", \"ai\"}, \"الاصطناعي\": {\"artificial\", \"ai\"},"` | — |
| [SRC-1AE03B9EC3-L000231](../../agents/web_agent.py#L231) | 231 | `"    \"تطور\": {\"development\", \"advance\"}, \"تطورات\": {\"developments\", \"advances\", \"updates\", \"latest\"},"` | — |
| [SRC-1AE03B9EC3-L000232](../../agents/web_agent.py#L232) | 232 | `"    \"التطورات\": {\"developments\", \"advances\", \"updates\", \"latest\"},"` | — |
| [SRC-1AE03B9EC3-L000233](../../agents/web_agent.py#L233) | 233 | `"    \"اراء\": {\"opinions\", \"views\"}, \"تجربة\": {\"experience\"}, \"تجارب\": {\"experiences\", \"reviews\"},"` | — |
| [SRC-1AE03B9EC3-L000234](../../agents/web_agent.py#L234) | 234 | `"    \"مستخدم\": {\"user\"}, \"المستخدم\": {\"user\"}, \"مستخدمين\": {\"users\"},"` | — |
| [SRC-1AE03B9EC3-L000235](../../agents/web_agent.py#L235) | 235 | `"    \"المستخدمين\": {\"users\"}, \"مالكون\": {\"owners\"}, \"المالكون\": {\"owners\"},"` | — |
| [SRC-1AE03B9EC3-L000236](../../agents/web_agent.py#L236) | 236 | `"}"` | — |
| [SRC-1AE03B9EC3-L000237](../../agents/web_agent.py#L237) | 237 | `"_CALENDAR_MONTHS = ("` | — |
| [SRC-1AE03B9EC3-L000238](../../agents/web_agent.py#L238) | 238 | `"    \"يناير\", \"فبراير\", \"مارس\", \"ابريل\", \"أبريل\", \"مايو\", \"يونيو\","` | — |
| [SRC-1AE03B9EC3-L000239](../../agents/web_agent.py#L239) | 239 | `"    \"يوليو\", \"اغسطس\", \"أغسطس\", \"سبتمبر\", \"اكتوبر\", \"أكتوبر\","` | — |
| [SRC-1AE03B9EC3-L000240](../../agents/web_agent.py#L240) | 240 | `"    \"نوفمبر\", \"ديسمبر\", \"january\", \"february\", \"march\", \"april\","` | — |
| [SRC-1AE03B9EC3-L000241](../../agents/web_agent.py#L241) | 241 | `"    \"may\", \"june\", \"july\", \"august\", \"september\", \"october\","` | — |
| [SRC-1AE03B9EC3-L000242](../../agents/web_agent.py#L242) | 242 | `"    \"november\", \"december\","` | — |
| [SRC-1AE03B9EC3-L000243](../../agents/web_agent.py#L243) | 243 | `")"` | — |
| [SRC-1AE03B9EC3-L000244](../../agents/web_agent.py#L244) | 244 | `"_BLOCKED_SOURCE_DOMAINS = frozenset({"` | — |
| [SRC-1AE03B9EC3-L000245](../../agents/web_agent.py#L245) | 245 | `"    \"translate.google.com\", \"translate.googleusercontent.com\","` | — |
| [SRC-1AE03B9EC3-L000246](../../agents/web_agent.py#L246) | 246 | `"})"` | — |
| [SRC-1AE03B9EC3-L000247](../../agents/web_agent.py#L247) | 247 | `""` | — |
| [SRC-1AE03B9EC3-L000248](../../agents/web_agent.py#L248) | 248 | `"def _normalize_search_query(value: str) -> str:"` | — |
| [SRC-1AE03B9EC3-L000249](../../agents/web_agent.py#L249) | 249 | `"    \"\"\"Normalize Arabic letters/diacritics while preserving search operators and dates.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000250](../../agents/web_agent.py#L250) | 250 | `"    value = unicodedata.normalize(\"NFKC\", value or \"\")"` | — |
| [SRC-1AE03B9EC3-L000251](../../agents/web_agent.py#L251) | 251 | `"    value = _ARABIC_DIACRITICS_RE.sub(\"\", value).translate(_ARABIC_SEARCH_TRANSLATION)"` | — |
| [SRC-1AE03B9EC3-L000252](../../agents/web_agent.py#L252) | 252 | `"    return re.sub(r\"\\s+\", \" \", value).strip()"` | — |
| [SRC-1AE03B9EC3-L000253](../../agents/web_agent.py#L253) | 253 | `""` | — |
| [SRC-1AE03B9EC3-L000254](../../agents/web_agent.py#L254) | 254 | `"# Normalize stop words too: otherwise Arabic letter normalization (e.g. ة→ه, أ→ا)"` | — |
| [SRC-1AE03B9EC3-L000255](../../agents/web_agent.py#L255) | 255 | `"# can leave request-format wording in the token set and distort relevance scores."` | — |
| [SRC-1AE03B9EC3-L000256](../../agents/web_agent.py#L256) | 256 | `"_NORMALIZED_SEARCH_STOPWORDS = frozenset("` | — |
| [SRC-1AE03B9EC3-L000257](../../agents/web_agent.py#L257) | 257 | `"    _normalize_search_query(word).casefold() for word in _SEARCH_STOPWORDS"` | — |
| [SRC-1AE03B9EC3-L000258](../../agents/web_agent.py#L258) | 258 | `")"` | — |
| [SRC-1AE03B9EC3-L000259](../../agents/web_agent.py#L259) | 259 | `""` | — |
| [SRC-1AE03B9EC3-L000260](../../agents/web_agent.py#L260) | 260 | `"# Normalize synonym keys and values by the same rules as search text. This avoids"` | — |
| [SRC-1AE03B9EC3-L000261](../../agents/web_agent.py#L261) | 261 | `"# Arabic ta-marbuta/alif variants silently disabling Arabic-to-English matching."` | — |
| [SRC-1AE03B9EC3-L000262](../../agents/web_agent.py#L262) | 262 | `"_NORMALIZED_SEARCH_SYNONYMS: dict[str, set[str]] = {}"` | — |
| [SRC-1AE03B9EC3-L000263](../../agents/web_agent.py#L263) | 263 | `"for _synonym_key, _synonym_values in _SEARCH_SYNONYMS.items():"` | — |
| [SRC-1AE03B9EC3-L000264](../../agents/web_agent.py#L264) | 264 | `"    _normalized_key = _normalize_search_query(_synonym_key).casefold()"` | — |
| [SRC-1AE03B9EC3-L000265](../../agents/web_agent.py#L265) | 265 | `"    _NORMALIZED_SEARCH_SYNONYMS.setdefault(_normalized_key, set()).update("` | — |
| [SRC-1AE03B9EC3-L000266](../../agents/web_agent.py#L266) | 266 | `"        _normalize_search_query(value).casefold() for value in _synonym_values"` | — |
| [SRC-1AE03B9EC3-L000267](../../agents/web_agent.py#L267) | 267 | `"    )"` | — |
| [SRC-1AE03B9EC3-L000268](../../agents/web_agent.py#L268) | 268 | `""` | — |
| [SRC-1AE03B9EC3-L000269](../../agents/web_agent.py#L269) | 269 | `"def _search_tokens(value: str) -> set[str]:"` | — |
| [SRC-1AE03B9EC3-L000270](../../agents/web_agent.py#L270) | 270 | `"    \"\"\"Tokenize Arabic/English text and expand a small bilingual vocabulary.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000271](../../agents/web_agent.py#L271) | 271 | `"    value = _normalize_search_query(value).casefold()"` | — |
| [SRC-1AE03B9EC3-L000272](../../agents/web_agent.py#L272) | 272 | `"    value = re.sub(r\"(?i)\\bsite\\s*:\\s*\\S+\", \" \", value)"` | — |
| [SRC-1AE03B9EC3-L000273](../../agents/web_agent.py#L273) | 273 | `"    tokens = re.findall(r\"[a-z0-9]+\|[\\u0620-\\u064A\\u066E-\\u06D3]+\", value)"` | — |
| [SRC-1AE03B9EC3-L000274](../../agents/web_agent.py#L274) | 274 | `"    result: set[str] = set()"` | — |
| [SRC-1AE03B9EC3-L000275](../../agents/web_agent.py#L275) | 275 | `"    for token in tokens:"` | — |
| [SRC-1AE03B9EC3-L000276](../../agents/web_agent.py#L276) | 276 | `"        if token in _NORMALIZED_SEARCH_STOPWORDS or len(token) < 2:"` | — |
| [SRC-1AE03B9EC3-L000277](../../agents/web_agent.py#L277) | 277 | `"            continue"` | — |
| [SRC-1AE03B9EC3-L000278](../../agents/web_agent.py#L278) | 278 | `"        forms = _arabic_query_token_forms(token)"` | — |
| [SRC-1AE03B9EC3-L000279](../../agents/web_agent.py#L279) | 279 | `"        raw_forms = set(forms)"` | — |
| [SRC-1AE03B9EC3-L000280](../../agents/web_agent.py#L280) | 280 | `"        for form in raw_forms:"` | — |
| [SRC-1AE03B9EC3-L000281](../../agents/web_agent.py#L281) | 281 | `"            forms.update(_NORMALIZED_SEARCH_SYNONYMS.get(form, set()))"` | — |
| [SRC-1AE03B9EC3-L000282](../../agents/web_agent.py#L282) | 282 | `"        # Reverse-map common English equivalents so Arabic and English results can match."` | — |
| [SRC-1AE03B9EC3-L000283](../../agents/web_agent.py#L283) | 283 | `"        for arabic, english in _NORMALIZED_SEARCH_SYNONYMS.items():"` | — |
| [SRC-1AE03B9EC3-L000284](../../agents/web_agent.py#L284) | 284 | `"            if raw_forms.intersection(english):"` | — |
| [SRC-1AE03B9EC3-L000285](../../agents/web_agent.py#L285) | 285 | `"                forms.add(arabic)"` | — |
| [SRC-1AE03B9EC3-L000286](../../agents/web_agent.py#L286) | 286 | `"                forms.update(english)"` | — |
| [SRC-1AE03B9EC3-L000287](../../agents/web_agent.py#L287) | 287 | `"                if arabic.startswith(\"ال\") and len(arabic) > 4:"` | — |
| [SRC-1AE03B9EC3-L000288](../../agents/web_agent.py#L288) | 288 | `"                    forms.add(arabic[2:])"` | — |
| [SRC-1AE03B9EC3-L000289](../../agents/web_agent.py#L289) | 289 | `"        result.update(forms)"` | — |
| [SRC-1AE03B9EC3-L000290](../../agents/web_agent.py#L290) | 290 | `"    return result"` | — |
| [SRC-1AE03B9EC3-L000291](../../agents/web_agent.py#L291) | 291 | `""` | — |
| [SRC-1AE03B9EC3-L000292](../../agents/web_agent.py#L292) | 292 | `"def _relevance_query_tokens(query: str) -> set[str]:"` | — |
| [SRC-1AE03B9EC3-L000293](../../agents/web_agent.py#L293) | 293 | `"    \"\"\"Return topic concepts after removing answer-format and query-expansion wording.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000294](../../agents/web_agent.py#L294) | 294 | `"    query = compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L000295](../../agents/web_agent.py#L295) | 295 | `"    if not query:"` | — |
| [SRC-1AE03B9EC3-L000296](../../agents/web_agent.py#L296) | 296 | `"        return set()"` | — |
| [SRC-1AE03B9EC3-L000297](../../agents/web_agent.py#L297) | 297 | `"    query_text = _normalize_search_query(query).casefold()"` | — |
| [SRC-1AE03B9EC3-L000298](../../agents/web_agent.py#L298) | 298 | `"    query_text = re.sub(r\"(?i)\\bsite\\s*:\\s*\\S+\", \" \", query_text)"` | — |
| [SRC-1AE03B9EC3-L000299](../../agents/web_agent.py#L299) | 299 | `"    # Treat the Arabic multiword phrase \"الذكاء الاصطناعي\" as one concept;"` | — |
| [SRC-1AE03B9EC3-L000300](../../agents/web_agent.py#L300) | 300 | `"    # otherwise the single English token \"AI\" can falsely satisfy both words."` | — |
| [SRC-1AE03B9EC3-L000301](../../agents/web_agent.py#L301) | 301 | `"    query_text = re.sub("` | — |
| [SRC-1AE03B9EC3-L000302](../../agents/web_agent.py#L302) | 302 | `"        r\"(?<![a-z0-9\\u0620-\\u06D3])(?:ال)?ذكاء\\s+(?:ال)?اصطناعي(?![a-z0-9\\u0620-\\u06D3])\","` | — |
| [SRC-1AE03B9EC3-L000303](../../agents/web_agent.py#L303) | 303 | `"        \" ai \","` | — |
| [SRC-1AE03B9EC3-L000304](../../agents/web_agent.py#L304) | 304 | `"        query_text,"` | — |
| [SRC-1AE03B9EC3-L000305](../../agents/web_agent.py#L305) | 305 | `"    )"` | — |
| [SRC-1AE03B9EC3-L000306](../../agents/web_agent.py#L306) | 306 | `"    query_text = re.sub(r\"(?i)\\bartificial\\s+intelligence\\b\", \" ai \", query_text)"` | — |
| [SRC-1AE03B9EC3-L000307](../../agents/web_agent.py#L307) | 307 | `"    return {"` | — |
| [SRC-1AE03B9EC3-L000308](../../agents/web_agent.py#L308) | 308 | `"        token for token in re.findall(r\"[a-z0-9]+\|[\\u0620-\\u064A\\u066E-\\u06D3]+\", query_text)"` | — |
| [SRC-1AE03B9EC3-L000309](../../agents/web_agent.py#L309) | 309 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L000310](../../agents/web_agent.py#L310) | 310 | `"            token not in _NORMALIZED_SEARCH_STOPWORDS"` | — |
| [SRC-1AE03B9EC3-L000311](../../agents/web_agent.py#L311) | 311 | `"            and token not in _GENERIC_QUERY_MODIFIER_TOKENS"` | — |
| [SRC-1AE03B9EC3-L000312](../../agents/web_agent.py#L312) | 312 | `"            and len(token) >= 2"` | — |
| [SRC-1AE03B9EC3-L000313](../../agents/web_agent.py#L313) | 313 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000314](../../agents/web_agent.py#L314) | 314 | `"    }"` | — |
| [SRC-1AE03B9EC3-L000315](../../agents/web_agent.py#L315) | 315 | `""` | — |
| [SRC-1AE03B9EC3-L000316](../../agents/web_agent.py#L316) | 316 | `"def _arabic_query_token_forms(token: str) -> set[str]:"` | — |
| [SRC-1AE03B9EC3-L000317](../../agents/web_agent.py#L317) | 317 | `"    \"\"\"Return conservative Arabic clitic/article variants for matching search evidence."` | — |
| [SRC-1AE03B9EC3-L000318](../../agents/web_agent.py#L318) | 318 | `""` | — |
| [SRC-1AE03B9EC3-L000319](../../agents/web_agent.py#L319) | 319 | `"    This is a matching aid only; it never changes the submitted query or URL policy."` | — |
| [SRC-1AE03B9EC3-L000320](../../agents/web_agent.py#L320) | 320 | `"    It handles common attached forms such as للشركات/والشركات/بالشركات without"` | — |
| [SRC-1AE03B9EC3-L000321](../../agents/web_agent.py#L321) | 321 | `"    applying broad stemming that could make unrelated Arabic words match."` | — |
| [SRC-1AE03B9EC3-L000322](../../agents/web_agent.py#L322) | 322 | `"    \"\"\""` | — |
| [SRC-1AE03B9EC3-L000323](../../agents/web_agent.py#L323) | 323 | `"    if not re.search(r\"[\\u0620-\\u06D3]\", token):"` | — |
| [SRC-1AE03B9EC3-L000324](../../agents/web_agent.py#L324) | 324 | `"        return {token}"` | — |
| [SRC-1AE03B9EC3-L000325](../../agents/web_agent.py#L325) | 325 | `"    forms = {token}"` | — |
| [SRC-1AE03B9EC3-L000326](../../agents/web_agent.py#L326) | 326 | `"    compound_prefixes = (\"وال\", \"بال\", \"كال\", \"فال\", \"ولل\", \"وبال\", \"فبال\", \"لل\")"` | — |
| [SRC-1AE03B9EC3-L000327](../../agents/web_agent.py#L327) | 327 | `"    for prefix in compound_prefixes:"` | — |
| [SRC-1AE03B9EC3-L000328](../../agents/web_agent.py#L328) | 328 | `"        if token.startswith(prefix) and len(token) - len(prefix) >= 3:"` | — |
| [SRC-1AE03B9EC3-L000329](../../agents/web_agent.py#L329) | 329 | `"            stem = token[len(prefix):]"` | — |
| [SRC-1AE03B9EC3-L000330](../../agents/web_agent.py#L330) | 330 | `"            forms.add(stem)"` | — |
| [SRC-1AE03B9EC3-L000331](../../agents/web_agent.py#L331) | 331 | `"            if stem.startswith(\"ال\") and len(stem) > 4:"` | — |
| [SRC-1AE03B9EC3-L000332](../../agents/web_agent.py#L332) | 332 | `"                forms.add(stem[2:])"` | — |
| [SRC-1AE03B9EC3-L000333](../../agents/web_agent.py#L333) | 333 | `"    if token.startswith(\"ال\") and len(token) > 4:"` | — |
| [SRC-1AE03B9EC3-L000334](../../agents/web_agent.py#L334) | 334 | `"        forms.add(token[2:])"` | — |
| [SRC-1AE03B9EC3-L000335](../../agents/web_agent.py#L335) | 335 | `"    for prefix in (\"و\", \"ف\", \"ب\", \"ك\", \"ل\"):"` | — |
| [SRC-1AE03B9EC3-L000336](../../agents/web_agent.py#L336) | 336 | `"        if token.startswith(prefix) and len(token) - len(prefix) >= 4:"` | — |
| [SRC-1AE03B9EC3-L000337](../../agents/web_agent.py#L337) | 337 | `"            stem = token[1:]"` | — |
| [SRC-1AE03B9EC3-L000338](../../agents/web_agent.py#L338) | 338 | `"            forms.add(stem)"` | — |
| [SRC-1AE03B9EC3-L000339](../../agents/web_agent.py#L339) | 339 | `"            if stem.startswith(\"ال\") and len(stem) > 4:"` | — |
| [SRC-1AE03B9EC3-L000340](../../agents/web_agent.py#L340) | 340 | `"                forms.add(stem[2:])"` | — |
| [SRC-1AE03B9EC3-L000341](../../agents/web_agent.py#L341) | 341 | `"            break"` | — |
| [SRC-1AE03B9EC3-L000342](../../agents/web_agent.py#L342) | 342 | `"    return forms"` | — |
| [SRC-1AE03B9EC3-L000343](../../agents/web_agent.py#L343) | 343 | `""` | — |
| [SRC-1AE03B9EC3-L000344](../../agents/web_agent.py#L344) | 344 | `"def _minimum_relevance_ratio(_query: str) -> float:"` | — |
| [SRC-1AE03B9EC3-L000345](../../agents/web_agent.py#L345) | 345 | `"    \"\"\"Keep the established 20% relevance floor after query normalization and token cleanup.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000346](../../agents/web_agent.py#L346) | 346 | `"    return 0.20"` | — |
| [SRC-1AE03B9EC3-L000347](../../agents/web_agent.py#L347) | 347 | `""` | — |
| [SRC-1AE03B9EC3-L000348](../../agents/web_agent.py#L348) | 348 | `"def _relevance_ratio(query: str, evidence: str) -> float:"` | — |
| [SRC-1AE03B9EC3-L000349](../../agents/web_agent.py#L349) | 349 | `"    \"\"\"Fraction of meaningful query concepts present in a candidate's title/snippet.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000350](../../agents/web_agent.py#L350) | 350 | `"    query_tokens = _relevance_query_tokens(query)"` | — |
| [SRC-1AE03B9EC3-L000351](../../agents/web_agent.py#L351) | 351 | `"    if not query_tokens:"` | — |
| [SRC-1AE03B9EC3-L000352](../../agents/web_agent.py#L352) | 352 | `"        # Relevance cannot be established from an instruction-only query."` | — |
| [SRC-1AE03B9EC3-L000353](../../agents/web_agent.py#L353) | 353 | `"        return 0.0"` | — |
| [SRC-1AE03B9EC3-L000354](../../agents/web_agent.py#L354) | 354 | `"    expanded_evidence = _search_tokens(evidence)"` | — |
| [SRC-1AE03B9EC3-L000355](../../agents/web_agent.py#L355) | 355 | `""` | — |
| [SRC-1AE03B9EC3-L000356](../../agents/web_agent.py#L356) | 356 | `"    def concept_found(token: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000357](../../agents/web_agent.py#L357) | 357 | `"        for form in _arabic_query_token_forms(token):"` | — |
| [SRC-1AE03B9EC3-L000358](../../agents/web_agent.py#L358) | 358 | `"            if ("` | — |
| [SRC-1AE03B9EC3-L000359](../../agents/web_agent.py#L359) | 359 | `"                form in expanded_evidence"` | — |
| [SRC-1AE03B9EC3-L000360](../../agents/web_agent.py#L360) | 360 | `"                or (form.startswith(\"ال\") and form[2:] in expanded_evidence)"` | — |
| [SRC-1AE03B9EC3-L000361](../../agents/web_agent.py#L361) | 361 | `"                or bool(_NORMALIZED_SEARCH_SYNONYMS.get(form, set()) & expanded_evidence)"` | — |
| [SRC-1AE03B9EC3-L000362](../../agents/web_agent.py#L362) | 362 | `"            ):"` | — |
| [SRC-1AE03B9EC3-L000363](../../agents/web_agent.py#L363) | 363 | `"                return True"` | — |
| [SRC-1AE03B9EC3-L000364](../../agents/web_agent.py#L364) | 364 | `"            # Also match an English query term through the Arabic concept that"` | — |
| [SRC-1AE03B9EC3-L000365](../../agents/web_agent.py#L365) | 365 | `"            # expands the evidence token. Synonym vocabulary is directional in its"` | — |
| [SRC-1AE03B9EC3-L000366](../../agents/web_agent.py#L366) | 366 | `"            # storage, but evidence matching must work in both language directions."` | — |
| [SRC-1AE03B9EC3-L000367](../../agents/web_agent.py#L367) | 367 | `"            if any("` | — |
| [SRC-1AE03B9EC3-L000368](../../agents/web_agent.py#L368) | 368 | `"                form in aliases"` | — |
| [SRC-1AE03B9EC3-L000369](../../agents/web_agent.py#L369) | 369 | `"                and ("` | — |
| [SRC-1AE03B9EC3-L000370](../../agents/web_agent.py#L370) | 370 | `"                    arabic in expanded_evidence"` | — |
| [SRC-1AE03B9EC3-L000371](../../agents/web_agent.py#L371) | 371 | `"                    or (arabic.startswith(\"ال\") and arabic[2:] in expanded_evidence)"` | — |
| [SRC-1AE03B9EC3-L000372](../../agents/web_agent.py#L372) | 372 | `"                )"` | — |
| [SRC-1AE03B9EC3-L000373](../../agents/web_agent.py#L373) | 373 | `"                for arabic, aliases in _NORMALIZED_SEARCH_SYNONYMS.items()"` | — |
| [SRC-1AE03B9EC3-L000374](../../agents/web_agent.py#L374) | 374 | `"            ):"` | — |
| [SRC-1AE03B9EC3-L000375](../../agents/web_agent.py#L375) | 375 | `"                return True"` | — |
| [SRC-1AE03B9EC3-L000376](../../agents/web_agent.py#L376) | 376 | `"        return False"` | — |
| [SRC-1AE03B9EC3-L000377](../../agents/web_agent.py#L377) | 377 | `""` | — |
| [SRC-1AE03B9EC3-L000378](../../agents/web_agent.py#L378) | 378 | `"    matched = sum(1 for token in query_tokens if concept_found(token))"` | — |
| [SRC-1AE03B9EC3-L000379](../../agents/web_agent.py#L379) | 379 | `"    ratio = matched / len(query_tokens)"` | — |
| [SRC-1AE03B9EC3-L000380](../../agents/web_agent.py#L380) | 380 | `"    # On longer questions, two matching topic concepts are required; request wording"` | — |
| [SRC-1AE03B9EC3-L000381](../../agents/web_agent.py#L381) | 381 | `"    # should not silently raise that floor to three or four concepts."` | — |
| [SRC-1AE03B9EC3-L000382](../../agents/web_agent.py#L382) | 382 | `"    if len(query_tokens) >= 4 and matched < 2:"` | — |
| [SRC-1AE03B9EC3-L000383](../../agents/web_agent.py#L383) | 383 | `"        return 0.0"` | — |
| [SRC-1AE03B9EC3-L000384](../../agents/web_agent.py#L384) | 384 | `"    return ratio"` | — |
| [SRC-1AE03B9EC3-L000385](../../agents/web_agent.py#L385) | 385 | `""` | — |
| [SRC-1AE03B9EC3-L000386](../../agents/web_agent.py#L386) | 386 | `"def _blocked_source_url(url: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000387](../../agents/web_agent.py#L387) | 387 | `"    try:"` | — |
| [SRC-1AE03B9EC3-L000388](../../agents/web_agent.py#L388) | 388 | `"        host = (urllib.parse.urlparse(url).hostname or \"\").lower().rstrip(\".\")"` | — |
| [SRC-1AE03B9EC3-L000389](../../agents/web_agent.py#L389) | 389 | `"        return any(host == domain or host.endswith(\".\" + domain) for domain in _BLOCKED_SOURCE_DOMAINS)"` | — |
| [SRC-1AE03B9EC3-L000390](../../agents/web_agent.py#L390) | 390 | `"    except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L000391](../../agents/web_agent.py#L391) | 391 | `"        return True"` | — |
| [SRC-1AE03B9EC3-L000392](../../agents/web_agent.py#L392) | 392 | `""` | — |
| [SRC-1AE03B9EC3-L000393](../../agents/web_agent.py#L393) | 393 | `"class AgentDependencyError(RuntimeError):"` | — |
| [SRC-1AE03B9EC3-L000394](../../agents/web_agent.py#L394) | 394 | `"    \"\"\"A required optional runtime dependency is unavailable.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000395](../../agents/web_agent.py#L395) | 395 | `""` | — |
| [SRC-1AE03B9EC3-L000396](../../agents/web_agent.py#L396) | 396 | `"class _NoRedirectHandler(urllib.request.HTTPRedirectHandler):"` | — |
| [SRC-1AE03B9EC3-L000397](../../agents/web_agent.py#L397) | 397 | `"    \"\"\"Fail closed on provider redirects so bearer credentials stay on the configured origin.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000398](../../agents/web_agent.py#L398) | 398 | `""` | — |
| [SRC-1AE03B9EC3-L000399](../../agents/web_agent.py#L399) | 399 | `"    def redirect_request(self, req, fp, code, msg, headers, newurl):"` | — |
| [SRC-1AE03B9EC3-L000400](../../agents/web_agent.py#L400) | 400 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000401](../../agents/web_agent.py#L401) | 401 | `""` | — |
| [SRC-1AE03B9EC3-L000402](../../agents/web_agent.py#L402) | 402 | `"def _open_model_request(request: urllib.request.Request, timeout: float):"` | — |
| [SRC-1AE03B9EC3-L000403](../../agents/web_agent.py#L403) | 403 | `"    \"\"\"Open one model-provider request without following any HTTP redirect.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000404](../../agents/web_agent.py#L404) | 404 | `"    opener = urllib.request.build_opener(_NoRedirectHandler)"` | — |
| [SRC-1AE03B9EC3-L000405](../../agents/web_agent.py#L405) | 405 | `"    return opener.open(request, timeout=timeout)"` | — |
| [SRC-1AE03B9EC3-L000406](../../agents/web_agent.py#L406) | 406 | `""` | — |
| [SRC-1AE03B9EC3-L000407](../../agents/web_agent.py#L407) | 407 | `""` | — |
| [SRC-1AE03B9EC3-L000408](../../agents/web_agent.py#L408) | 408 | `"def _is_safe_model_base_url(value: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000409](../../agents/web_agent.py#L409) | 409 | `"    \"\"\"Require HTTPS for remote model providers; permit HTTP only on loopback.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000410](../../agents/web_agent.py#L410) | 410 | `"    if not isinstance(value, str) or not value or any(ord(char) < 32 for char in value):"` | — |
| [SRC-1AE03B9EC3-L000411](../../agents/web_agent.py#L411) | 411 | `"        return False"` | — |
| [SRC-1AE03B9EC3-L000412](../../agents/web_agent.py#L412) | 412 | `"    try:"` | — |
| [SRC-1AE03B9EC3-L000413](../../agents/web_agent.py#L413) | 413 | `"        parsed = urllib.parse.urlsplit(value)"` | — |
| [SRC-1AE03B9EC3-L000414](../../agents/web_agent.py#L414) | 414 | `"        hostname = parsed.hostname"` | — |
| [SRC-1AE03B9EC3-L000415](../../agents/web_agent.py#L415) | 415 | `"        _ = parsed.port"` | — |
| [SRC-1AE03B9EC3-L000416](../../agents/web_agent.py#L416) | 416 | `"    except ValueError:"` | — |
| [SRC-1AE03B9EC3-L000417](../../agents/web_agent.py#L417) | 417 | `"        return False"` | — |
| [SRC-1AE03B9EC3-L000418](../../agents/web_agent.py#L418) | 418 | `"    if ("` | — |
| [SRC-1AE03B9EC3-L000419](../../agents/web_agent.py#L419) | 419 | `"        not hostname"` | — |
| [SRC-1AE03B9EC3-L000420](../../agents/web_agent.py#L420) | 420 | `"        or parsed.username is not None"` | — |
| [SRC-1AE03B9EC3-L000421](../../agents/web_agent.py#L421) | 421 | `"        or parsed.password is not None"` | — |
| [SRC-1AE03B9EC3-L000422](../../agents/web_agent.py#L422) | 422 | `"        or parsed.query"` | — |
| [SRC-1AE03B9EC3-L000423](../../agents/web_agent.py#L423) | 423 | `"        or parsed.fragment"` | — |
| [SRC-1AE03B9EC3-L000424](../../agents/web_agent.py#L424) | 424 | `"    ):"` | — |
| [SRC-1AE03B9EC3-L000425](../../agents/web_agent.py#L425) | 425 | `"        return False"` | — |
| [SRC-1AE03B9EC3-L000426](../../agents/web_agent.py#L426) | 426 | `"    if parsed.scheme == \"https\":"` | — |
| [SRC-1AE03B9EC3-L000427](../../agents/web_agent.py#L427) | 427 | `"        return True"` | — |
| [SRC-1AE03B9EC3-L000428](../../agents/web_agent.py#L428) | 428 | `"    if parsed.scheme != \"http\":"` | — |
| [SRC-1AE03B9EC3-L000429](../../agents/web_agent.py#L429) | 429 | `"        return False"` | — |
| [SRC-1AE03B9EC3-L000430](../../agents/web_agent.py#L430) | 430 | `"    if hostname.casefold() == \"localhost\":"` | — |
| [SRC-1AE03B9EC3-L000431](../../agents/web_agent.py#L431) | 431 | `"        return True"` | — |
| [SRC-1AE03B9EC3-L000432](../../agents/web_agent.py#L432) | 432 | `"    try:"` | — |
| [SRC-1AE03B9EC3-L000433](../../agents/web_agent.py#L433) | 433 | `"        return ipaddress.ip_address(hostname).is_loopback"` | — |
| [SRC-1AE03B9EC3-L000434](../../agents/web_agent.py#L434) | 434 | `"    except ValueError:"` | — |
| [SRC-1AE03B9EC3-L000435](../../agents/web_agent.py#L435) | 435 | `"        return False"` | — |
| [SRC-1AE03B9EC3-L000436](../../agents/web_agent.py#L436) | 436 | `""` | — |
| [SRC-1AE03B9EC3-L000437](../../agents/web_agent.py#L437) | 437 | `""` | — |
| [SRC-1AE03B9EC3-L000438](../../agents/web_agent.py#L438) | 438 | `"def _safe_model_provider_label(value: str) -> str:"` | — |
| [SRC-1AE03B9EC3-L000439](../../agents/web_agent.py#L439) | 439 | `"    \"\"\"Expose only scheme/host/port in health output; never URL credentials or paths.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000440](../../agents/web_agent.py#L440) | 440 | `"    try:"` | — |
| [SRC-1AE03B9EC3-L000441](../../agents/web_agent.py#L441) | 441 | `"        parsed = urllib.parse.urlsplit(value)"` | — |
| [SRC-1AE03B9EC3-L000442](../../agents/web_agent.py#L442) | 442 | `"        hostname = parsed.hostname"` | — |
| [SRC-1AE03B9EC3-L000443](../../agents/web_agent.py#L443) | 443 | `"        if not parsed.scheme or not hostname:"` | — |
| [SRC-1AE03B9EC3-L000444](../../agents/web_agent.py#L444) | 444 | `"            return \"invalid_provider_url\""` | — |
| [SRC-1AE03B9EC3-L000445](../../agents/web_agent.py#L445) | 445 | `"        port = parsed.port"` | — |
| [SRC-1AE03B9EC3-L000446](../../agents/web_agent.py#L446) | 446 | `"    except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L000447](../../agents/web_agent.py#L447) | 447 | `"        return \"invalid_provider_url\""` | — |
| [SRC-1AE03B9EC3-L000448](../../agents/web_agent.py#L448) | 448 | `"    display_host = f\"[{hostname}]\" if \":\" in hostname else hostname"` | — |
| [SRC-1AE03B9EC3-L000449](../../agents/web_agent.py#L449) | 449 | `"    display_port = f\":{port}\" if port is not None else \"\""` | — |
| [SRC-1AE03B9EC3-L000450](../../agents/web_agent.py#L450) | 450 | `"    return f\"{parsed.scheme}://{display_host}{display_port}\""` | — |
| [SRC-1AE03B9EC3-L000451](../../agents/web_agent.py#L451) | 451 | `""` | — |
| [SRC-1AE03B9EC3-L000452](../../agents/web_agent.py#L452) | 452 | `"def _clean_text(value: Any, limit: int) -> str:"` | — |
| [SRC-1AE03B9EC3-L000453](../../agents/web_agent.py#L453) | 453 | `"    if not isinstance(value, str):"` | — |
| [SRC-1AE03B9EC3-L000454](../../agents/web_agent.py#L454) | 454 | `"        return \"\""` | — |
| [SRC-1AE03B9EC3-L000455](../../agents/web_agent.py#L455) | 455 | `"    return \" \".join(value.replace(\"\\x00\", \" \").split())[:limit]"` | — |
| [SRC-1AE03B9EC3-L000456](../../agents/web_agent.py#L456) | 456 | `""` | — |
| [SRC-1AE03B9EC3-L000457](../../agents/web_agent.py#L457) | 457 | `"def _public_http_url(value: Any) -> str \| None:"` | — |
| [SRC-1AE03B9EC3-L000458](../../agents/web_agent.py#L458) | 458 | `"    \"\"\"Lexically validate an HTTP URL before using it as a search source.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000459](../../agents/web_agent.py#L459) | 459 | `"    if not isinstance(value, str) or len(value) > 2048:"` | — |
| [SRC-1AE03B9EC3-L000460](../../agents/web_agent.py#L460) | 460 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000461](../../agents/web_agent.py#L461) | 461 | `"    try:"` | — |
| [SRC-1AE03B9EC3-L000462](../../agents/web_agent.py#L462) | 462 | `"        parsed = urllib.parse.urlparse(value.strip())"` | — |
| [SRC-1AE03B9EC3-L000463](../../agents/web_agent.py#L463) | 463 | `"        if parsed.scheme not in {\"http\", \"https\"}:"` | — |
| [SRC-1AE03B9EC3-L000464](../../agents/web_agent.py#L464) | 464 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000465](../../agents/web_agent.py#L465) | 465 | `"        if not parsed.hostname or parsed.username is not None or parsed.password is not None:"` | — |
| [SRC-1AE03B9EC3-L000466](../../agents/web_agent.py#L466) | 466 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000467](../../agents/web_agent.py#L467) | 467 | `"        if parsed.port not in (None, 80, 443):"` | — |
| [SRC-1AE03B9EC3-L000468](../../agents/web_agent.py#L468) | 468 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000469](../../agents/web_agent.py#L469) | 469 | `"        host = parsed.hostname.rstrip(\".\").lower()"` | — |
| [SRC-1AE03B9EC3-L000470](../../agents/web_agent.py#L470) | 470 | `"        if not host or host in {\"localhost\"} or host.endswith((\".local\", \".internal\", \".localhost\")):"` | — |
| [SRC-1AE03B9EC3-L000471](../../agents/web_agent.py#L471) | 471 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000472](../../agents/web_agent.py#L472) | 472 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000473](../../agents/web_agent.py#L473) | 473 | `"            ip = ipaddress.ip_address(host)"` | — |
| [SRC-1AE03B9EC3-L000474](../../agents/web_agent.py#L474) | 474 | `"        except ValueError:"` | — |
| [SRC-1AE03B9EC3-L000475](../../agents/web_agent.py#L475) | 475 | `"            pass"` | — |
| [SRC-1AE03B9EC3-L000476](../../agents/web_agent.py#L476) | 476 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L000477](../../agents/web_agent.py#L477) | 477 | `"            if not ip.is_global:"` | — |
| [SRC-1AE03B9EC3-L000478](../../agents/web_agent.py#L478) | 478 | `"                return None"` | — |
| [SRC-1AE03B9EC3-L000479](../../agents/web_agent.py#L479) | 479 | `"        return urllib.parse.urlunparse(parsed._replace(fragment=\"\"))"` | — |
| [SRC-1AE03B9EC3-L000480](../../agents/web_agent.py#L480) | 480 | `"    except (ValueError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L000481](../../agents/web_agent.py#L481) | 481 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000482](../../agents/web_agent.py#L482) | 482 | `""` | — |
| [SRC-1AE03B9EC3-L000483](../../agents/web_agent.py#L483) | 483 | `"def _public_ip_literals(host: str) -> list[str] \| None:"` | — |
| [SRC-1AE03B9EC3-L000484](../../agents/web_agent.py#L484) | 484 | `"    \"\"\"Resolve host and return its public addresses."` | — |
| [SRC-1AE03B9EC3-L000485](../../agents/web_agent.py#L485) | 485 | `""` | — |
| [SRC-1AE03B9EC3-L000486](../../agents/web_agent.py#L486) | 486 | `"    Returns None when resolution fails or any answer is not a global address."` | — |
