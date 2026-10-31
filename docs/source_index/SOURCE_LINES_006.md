# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **006**
- سجلات الأسطر: **800**
- النطاق: SRC-1E32639872-L000014 إلى SRC-60066C6786-L000186
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1E32639872 — [agents/research_completion.py](../../agents/research_completion.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1E32639872-L000014](../../agents/research_completion.py#L14) | 14 | `"    \"attempted_research_error\", \"unknown_after_research_error\","` | — |
| [SRC-1E32639872-L000015](../../agents/research_completion.py#L15) | 15 | `"    \"unknown_after_budget_exhaustion\","` | — |
| [SRC-1E32639872-L000016](../../agents/research_completion.py#L16) | 16 | `"})"` | — |
| [SRC-1E32639872-L000017](../../agents/research_completion.py#L17) | 17 | `"_CONNECTOR_OK = frozenset({\"ok\", \"no_results\", \"filtered_all\", \"passed\"})"` | — |
| [SRC-1E32639872-L000018](../../agents/research_completion.py#L18) | 18 | `"_CONNECTOR_ERRORS = frozenset({"` | — |
| [SRC-1E32639872-L000019](../../agents/research_completion.py#L19) | 19 | `"    \"failed\", \"timeout\", \"error\", \"not_configured\", \"disabled\","` | — |
| [SRC-1E32639872-L000020](../../agents/research_completion.py#L20) | 20 | `"    \"rate_limited\", \"blocked\","` | — |
| [SRC-1E32639872-L000021](../../agents/research_completion.py#L21) | 21 | `"})"` | — |
| [SRC-1E32639872-L000022](../../agents/research_completion.py#L22) | 22 | `"_TRACKING_KEYS = frozenset({\"fbclid\", \"gclid\", \"mc_cid\", \"mc_eid\"})"` | — |
| [SRC-1E32639872-L000023](../../agents/research_completion.py#L23) | 23 | `""` | — |
| [SRC-1E32639872-L000024](../../agents/research_completion.py#L24) | 24 | `""` | — |
| [SRC-1E32639872-L000025](../../agents/research_completion.py#L25) | 25 | `"def _dict(value: Any) -> dict[str, Any]:"` | — |
| [SRC-1E32639872-L000026](../../agents/research_completion.py#L26) | 26 | `"    return value if isinstance(value, dict) else {}"` | — |
| [SRC-1E32639872-L000027](../../agents/research_completion.py#L27) | 27 | `""` | — |
| [SRC-1E32639872-L000028](../../agents/research_completion.py#L28) | 28 | `""` | — |
| [SRC-1E32639872-L000029](../../agents/research_completion.py#L29) | 29 | `"def _list(value: Any) -> list[Any]:"` | — |
| [SRC-1E32639872-L000030](../../agents/research_completion.py#L30) | 30 | `"    return value if isinstance(value, list) else []"` | — |
| [SRC-1E32639872-L000031](../../agents/research_completion.py#L31) | 31 | `""` | — |
| [SRC-1E32639872-L000032](../../agents/research_completion.py#L32) | 32 | `""` | — |
| [SRC-1E32639872-L000033](../../agents/research_completion.py#L33) | 33 | `"def _int(value: Any) -> int \| None:"` | — |
| [SRC-1E32639872-L000034](../../agents/research_completion.py#L34) | 34 | `"    if isinstance(value, bool):"` | — |
| [SRC-1E32639872-L000035](../../agents/research_completion.py#L35) | 35 | `"        return None"` | — |
| [SRC-1E32639872-L000036](../../agents/research_completion.py#L36) | 36 | `"    try:"` | — |
| [SRC-1E32639872-L000037](../../agents/research_completion.py#L37) | 37 | `"        return max(0, int(value))"` | — |
| [SRC-1E32639872-L000038](../../agents/research_completion.py#L38) | 38 | `"    except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-1E32639872-L000039](../../agents/research_completion.py#L39) | 39 | `"        return None"` | — |
| [SRC-1E32639872-L000040](../../agents/research_completion.py#L40) | 40 | `""` | — |
| [SRC-1E32639872-L000041](../../agents/research_completion.py#L41) | 41 | `""` | — |
| [SRC-1E32639872-L000042](../../agents/research_completion.py#L42) | 42 | `"def _readable(source: dict[str, Any]) -> bool:"` | — |
| [SRC-1E32639872-L000043](../../agents/research_completion.py#L43) | 43 | `"    return bool(source.get(\"page_fetched\")) and ("` | — |
| [SRC-1E32639872-L000044](../../agents/research_completion.py#L44) | 44 | `"        bool(str(source.get(\"page_text\") or \"\").strip())"` | — |
| [SRC-1E32639872-L000045](../../agents/research_completion.py#L45) | 45 | `"        or source.get(\"readable_page_text_available\") is True"` | — |
| [SRC-1E32639872-L000046](../../agents/research_completion.py#L46) | 46 | `"    )"` | — |
| [SRC-1E32639872-L000047](../../agents/research_completion.py#L47) | 47 | `""` | — |
| [SRC-1E32639872-L000048](../../agents/research_completion.py#L48) | 48 | `""` | — |
| [SRC-1E32639872-L000049](../../agents/research_completion.py#L49) | 49 | `"def _url_key(value: Any) -> str:"` | — |
| [SRC-1E32639872-L000050](../../agents/research_completion.py#L50) | 50 | `"    try:"` | — |
| [SRC-1E32639872-L000051](../../agents/research_completion.py#L51) | 51 | `"        parts = urlsplit(str(value or \"\").strip())"` | — |
| [SRC-1E32639872-L000052](../../agents/research_completion.py#L52) | 52 | `"        scheme = parts.scheme.lower()"` | — |
| [SRC-1E32639872-L000053](../../agents/research_completion.py#L53) | 53 | `"        if scheme not in {\"http\", \"https\"} or not parts.hostname:"` | — |
| [SRC-1E32639872-L000054](../../agents/research_completion.py#L54) | 54 | `"            return \"\""` | — |
| [SRC-1E32639872-L000055](../../agents/research_completion.py#L55) | 55 | `"        host = parts.hostname.lower().rstrip(\".\")"` | — |
| [SRC-1E32639872-L000056](../../agents/research_completion.py#L56) | 56 | `"        port = parts.port"` | — |
| [SRC-1E32639872-L000057](../../agents/research_completion.py#L57) | 57 | `"        netloc = host if port is None or (scheme, port) in {"` | — |
| [SRC-1E32639872-L000058](../../agents/research_completion.py#L58) | 58 | `"            (\"http\", 80), (\"https\", 443)"` | — |
| [SRC-1E32639872-L000059](../../agents/research_completion.py#L59) | 59 | `"        } else f\"{host}:{port}\""` | — |
| [SRC-1E32639872-L000060](../../agents/research_completion.py#L60) | 60 | `"        query = ["` | — |
| [SRC-1E32639872-L000061](../../agents/research_completion.py#L61) | 61 | `"            (key, val) for key, val in parse_qsl(parts.query, keep_blank_values=True)"` | — |
| [SRC-1E32639872-L000062](../../agents/research_completion.py#L62) | 62 | `"            if key.casefold() not in _TRACKING_KEYS"` | — |
| [SRC-1E32639872-L000063](../../agents/research_completion.py#L63) | 63 | `"            and not key.casefold().startswith(\"utm_\")"` | — |
| [SRC-1E32639872-L000064](../../agents/research_completion.py#L64) | 64 | `"        ]"` | — |
| [SRC-1E32639872-L000065](../../agents/research_completion.py#L65) | 65 | `"        path = parts.path.rstrip(\"/\") or \"/\""` | — |
| [SRC-1E32639872-L000066](../../agents/research_completion.py#L66) | 66 | `"        return urlunsplit((scheme, netloc, path, urlencode(sorted(query)), \"\"))"` | — |
| [SRC-1E32639872-L000067](../../agents/research_completion.py#L67) | 67 | `"    except (TypeError, ValueError):"` | — |
| [SRC-1E32639872-L000068](../../agents/research_completion.py#L68) | 68 | `"        return \"\""` | — |
| [SRC-1E32639872-L000069](../../agents/research_completion.py#L69) | 69 | `""` | — |
| [SRC-1E32639872-L000070](../../agents/research_completion.py#L70) | 70 | `""` | — |
| [SRC-1E32639872-L000071](../../agents/research_completion.py#L71) | 71 | `"def build_research_completion(result: dict[str, Any]) -> dict[str, Any]:"` | — |
| [SRC-1E32639872-L000072](../../agents/research_completion.py#L72) | 72 | `"    \"\"\"Compute phase states and final counters without claiming semantic verification.\"\"\""` | — |
| [SRC-1E32639872-L000073](../../agents/research_completion.py#L73) | 73 | `"    result = _dict(result)"` | — |
| [SRC-1E32639872-L000074](../../agents/research_completion.py#L74) | 74 | `"    report = _dict(result.get(\"search_report\"))"` | — |
| [SRC-1E32639872-L000075](../../agents/research_completion.py#L75) | 75 | `"    raw_sources = _list(result.get(\"sources\"))"` | — |
| [SRC-1E32639872-L000076](../../agents/research_completion.py#L76) | 76 | `"    sources = [item for item in raw_sources if isinstance(item, dict)]"` | — |
| [SRC-1E32639872-L000077](../../agents/research_completion.py#L77) | 77 | `"    kind = str(result.get(\"kind\") or \"\")"` | — |
| [SRC-1E32639872-L000078](../../agents/research_completion.py#L78) | 78 | `"    if kind not in _RESEARCH_KINDS and not report:"` | — |
| [SRC-1E32639872-L000079](../../agents/research_completion.py#L79) | 79 | `"        return {"` | — |
| [SRC-1E32639872-L000080](../../agents/research_completion.py#L80) | 80 | `"            \"status\": \"not_applicable\" if kind in {"` | — |
| [SRC-1E32639872-L000081](../../agents/research_completion.py#L81) | 81 | `"                \"capability_answer\", \"local_conversation\", \"clarification\""` | — |
| [SRC-1E32639872-L000082](../../agents/research_completion.py#L82) | 82 | `"            } else \"not_run\","` | — |
| [SRC-1E32639872-L000083](../../agents/research_completion.py#L83) | 83 | `"            \"semantic_verification\": \"not_performed\","` | — |
| [SRC-1E32639872-L000084](../../agents/research_completion.py#L84) | 84 | `"        }"` | — |
| [SRC-1E32639872-L000085](../../agents/research_completion.py#L85) | 85 | `""` | — |
| [SRC-1E32639872-L000086](../../agents/research_completion.py#L86) | 86 | `"    budget = _dict(result.get(\"request_budget\") or report.get(\"request_budget\"))"` | — |
| [SRC-1E32639872-L000087](../../agents/research_completion.py#L87) | 87 | `"    exhausted = bool(budget.get(\"budget_exhausted\")) or bool("` | — |
| [SRC-1E32639872-L000088](../../agents/research_completion.py#L88) | 88 | `"        budget.get(\"deadline_exceeded\")"` | — |
| [SRC-1E32639872-L000089](../../agents/research_completion.py#L89) | 89 | `"    )"` | — |
| [SRC-1E32639872-L000090](../../agents/research_completion.py#L90) | 90 | `"    guardrails = _dict(report.get(\"source_guardrails\"))"` | — |
| [SRC-1E32639872-L000091](../../agents/research_completion.py#L91) | 91 | `"    final_guards = _dict(guardrails.get(\"final\") or guardrails.get(\"initial\"))"` | — |
| [SRC-1E32639872-L000092](../../agents/research_completion.py#L92) | 92 | `"    rejection_counts = _dict(final_guards.get(\"rejection_counts\"))"` | — |
| [SRC-1E32639872-L000093](../../agents/research_completion.py#L93) | 93 | `"    rejected = sum("` | — |
| [SRC-1E32639872-L000094](../../agents/research_completion.py#L94) | 94 | `"        count for count in (_int(value) for value in rejection_counts.values())"` | — |
| [SRC-1E32639872-L000095](../../agents/research_completion.py#L95) | 95 | `"        if count is not None"` | — |
| [SRC-1E32639872-L000096](../../agents/research_completion.py#L96) | 96 | `"    )"` | — |
| [SRC-1E32639872-L000097](../../agents/research_completion.py#L97) | 97 | `"    attempted_value = result.get(\"search_attempted\")"` | — |
| [SRC-1E32639872-L000098](../../agents/research_completion.py#L98) | 98 | `"    if attempted_value is None:"` | — |
| [SRC-1E32639872-L000099](../../agents/research_completion.py#L99) | 99 | `"        attempted_value = report.get(\"search_attempted\")"` | — |
| [SRC-1E32639872-L000100](../../agents/research_completion.py#L100) | 100 | `"    attempted = attempted_value if isinstance(attempted_value, bool) else None"` | — |
| [SRC-1E32639872-L000101](../../agents/research_completion.py#L101) | 101 | `""` | — |
| [SRC-1E32639872-L000102](../../agents/research_completion.py#L102) | 102 | `"    fetched = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1E32639872-L000103](../../agents/research_completion.py#L103) | 103 | `"    read = sum(_readable(source) for source in sources)"` | — |
| [SRC-1E32639872-L000104](../../agents/research_completion.py#L104) | 104 | `"    snippet_only = sum("` | — |
| [SRC-1E32639872-L000105](../../agents/research_completion.py#L105) | 105 | `"        bool(str(source.get(\"snippet\") or \"\").strip()) and not _readable(source)"` | — |
| [SRC-1E32639872-L000106](../../agents/research_completion.py#L106) | 106 | `"        for source in sources"` | — |
| [SRC-1E32639872-L000107](../../agents/research_completion.py#L107) | 107 | `"    )"` | — |
| [SRC-1E32639872-L000108](../../agents/research_completion.py#L108) | 108 | `"    unflagged_text = sum("` | — |
| [SRC-1E32639872-L000109](../../agents/research_completion.py#L109) | 109 | `"        ("` | — |
| [SRC-1E32639872-L000110](../../agents/research_completion.py#L110) | 110 | `"            bool(str(source.get(\"page_text\") or \"\").strip())"` | — |
| [SRC-1E32639872-L000111](../../agents/research_completion.py#L111) | 111 | `"            and not bool(source.get(\"page_fetched\"))"` | — |
| [SRC-1E32639872-L000112](../../agents/research_completion.py#L112) | 112 | `"        )"` | — |
| [SRC-1E32639872-L000113](../../agents/research_completion.py#L113) | 113 | `"        or source.get(\"page_text_present_without_fetch_flag\") is True"` | — |
| [SRC-1E32639872-L000114](../../agents/research_completion.py#L114) | 114 | `"        for source in sources"` | — |
| [SRC-1E32639872-L000115](../../agents/research_completion.py#L115) | 115 | `"    )"` | — |
| [SRC-1E32639872-L000116](../../agents/research_completion.py#L116) | 116 | `"    url_keys = [_url_key(source.get(\"url\")) for source in sources]"` | — |
| [SRC-1E32639872-L000117](../../agents/research_completion.py#L117) | 117 | `"    url_keys = [key for key in url_keys if key]"` | — |
| [SRC-1E32639872-L000118](../../agents/research_completion.py#L118) | 118 | `"    unique_urls = set(url_keys)"` | — |
| [SRC-1E32639872-L000119](../../agents/research_completion.py#L119) | 119 | `"    domains = set()"` | — |
| [SRC-1E32639872-L000120](../../agents/research_completion.py#L120) | 120 | `"    for source in sources:"` | — |
| [SRC-1E32639872-L000121](../../agents/research_completion.py#L121) | 121 | `"        key = _url_key(source.get(\"url\"))"` | — |
| [SRC-1E32639872-L000122](../../agents/research_completion.py#L122) | 122 | `"        if not key:"` | — |
| [SRC-1E32639872-L000123](../../agents/research_completion.py#L123) | 123 | `"            continue"` | — |
| [SRC-1E32639872-L000124](../../agents/research_completion.py#L124) | 124 | `"        host = source.get(\"domain\") or urlsplit(key).hostname or \"\""` | — |
| [SRC-1E32639872-L000125](../../agents/research_completion.py#L125) | 125 | `"        domains.add(registrable_domain(str(host)))"` | — |
| [SRC-1E32639872-L000126](../../agents/research_completion.py#L126) | 126 | `"    domains.discard(\"\")"` | — |
| [SRC-1E32639872-L000127](../../agents/research_completion.py#L127) | 127 | `""` | — |
| [SRC-1E32639872-L000128](../../agents/research_completion.py#L128) | 128 | `"    query_rows = _list(report.get(\"query_results\"))"` | — |
| [SRC-1E32639872-L000129](../../agents/research_completion.py#L129) | 129 | `"    query_total = None"` | — |
| [SRC-1E32639872-L000130](../../agents/research_completion.py#L130) | 130 | `"    if query_rows and all("` | — |
| [SRC-1E32639872-L000131](../../agents/research_completion.py#L131) | 131 | `"        isinstance(row, dict) and _int(row.get(\"results\")) is not None"` | — |
| [SRC-1E32639872-L000132](../../agents/research_completion.py#L132) | 132 | `"        for row in query_rows"` | — |
| [SRC-1E32639872-L000133](../../agents/research_completion.py#L133) | 133 | `"    ):"` | — |
| [SRC-1E32639872-L000134](../../agents/research_completion.py#L134) | 134 | `"        query_total = sum(_int(row.get(\"results\")) or 0 for row in query_rows)"` | — |
| [SRC-1E32639872-L000135](../../agents/research_completion.py#L135) | 135 | `"    zero_results = bool(query_rows) and all("` | — |
| [SRC-1E32639872-L000136](../../agents/research_completion.py#L136) | 136 | `"        isinstance(row, dict) and _int(row.get(\"results\")) == 0"` | — |
| [SRC-1E32639872-L000137](../../agents/research_completion.py#L137) | 137 | `"        for row in query_rows"` | — |
| [SRC-1E32639872-L000138](../../agents/research_completion.py#L138) | 138 | `"    )"` | — |
| [SRC-1E32639872-L000139](../../agents/research_completion.py#L139) | 139 | `""` | — |
| [SRC-1E32639872-L000140](../../agents/research_completion.py#L140) | 140 | `"    connector_counts: dict[str, int] = {}"` | — |
| [SRC-1E32639872-L000141](../../agents/research_completion.py#L141) | 141 | `"    for item in _list(report.get(\"provider_diagnostics\")):"` | — |
| [SRC-1E32639872-L000142](../../agents/research_completion.py#L142) | 142 | `"        if not isinstance(item, dict):"` | — |
| [SRC-1E32639872-L000143](../../agents/research_completion.py#L143) | 143 | `"            continue"` | — |
| [SRC-1E32639872-L000144](../../agents/research_completion.py#L144) | 144 | `"        status_value = str(item.get(\"status\") or \"unknown\").strip().lower()"` | — |
| [SRC-1E32639872-L000145](../../agents/research_completion.py#L145) | 145 | `"        connector_counts[status_value] = connector_counts.get(status_value, 0) + 1"` | — |
| [SRC-1E32639872-L000146](../../agents/research_completion.py#L146) | 146 | `"    connector_ok = sum("` | — |
| [SRC-1E32639872-L000147](../../agents/research_completion.py#L147) | 147 | `"        count for status_value, count in connector_counts.items()"` | — |
| [SRC-1E32639872-L000148](../../agents/research_completion.py#L148) | 148 | `"        if status_value in _CONNECTOR_OK"` | — |
| [SRC-1E32639872-L000149](../../agents/research_completion.py#L149) | 149 | `"    )"` | — |
| [SRC-1E32639872-L000150](../../agents/research_completion.py#L150) | 150 | `"    connector_errors = sum("` | — |
| [SRC-1E32639872-L000151](../../agents/research_completion.py#L151) | 151 | `"        count for status_value, count in connector_counts.items()"` | — |
| [SRC-1E32639872-L000152](../../agents/research_completion.py#L152) | 152 | `"        if status_value in _CONNECTOR_ERRORS"` | — |
| [SRC-1E32639872-L000153](../../agents/research_completion.py#L153) | 153 | `"    )"` | — |
| [SRC-1E32639872-L000154](../../agents/research_completion.py#L154) | 154 | `""` | — |
| [SRC-1E32639872-L000155](../../agents/research_completion.py#L155) | 155 | `"    reported_sources = _int(report.get(\"unique_sources\"))"` | — |
| [SRC-1E32639872-L000156](../../agents/research_completion.py#L156) | 156 | `"    reported_fetched = _int(report.get(\"pages_fetched\"))"` | — |
| [SRC-1E32639872-L000157](../../agents/research_completion.py#L157) | 157 | `"    counter_issues = []"` | — |
| [SRC-1E32639872-L000158](../../agents/research_completion.py#L158) | 158 | `"    if reported_sources is not None and reported_sources != len(sources):"` | — |
| [SRC-1E32639872-L000159](../../agents/research_completion.py#L159) | 159 | `"        counter_issues.append(\"reported_unique_sources_differs_from_final_source_list\")"` | — |
| [SRC-1E32639872-L000160](../../agents/research_completion.py#L160) | 160 | `"    if reported_fetched is not None and reported_fetched != fetched:"` | — |
| [SRC-1E32639872-L000161](../../agents/research_completion.py#L161) | 161 | `"        counter_issues.append(\"reported_pages_fetched_differs_from_final_source_list\")"` | — |
| [SRC-1E32639872-L000162](../../agents/research_completion.py#L162) | 162 | `""` | — |
| [SRC-1E32639872-L000163](../../agents/research_completion.py#L163) | 163 | `"    model_used = result.get(\"used_language_model\") is True"` | — |
| [SRC-1E32639872-L000164](../../agents/research_completion.py#L164) | 164 | `"    final_status = str(result.get(\"final_answer_status\") or \"\")"` | — |
| [SRC-1E32639872-L000165](../../agents/research_completion.py#L165) | 165 | `"    integrity = _dict(result.get(\"answer_integrity\"))"` | — |
| [SRC-1E32639872-L000166](../../agents/research_completion.py#L166) | 166 | `"    gap_count = sum("` | — |
| [SRC-1E32639872-L000167](../../agents/research_completion.py#L167) | 167 | `"        _int(integrity.get(key)) or 0"` | — |
| [SRC-1E32639872-L000168](../../agents/research_completion.py#L168) | 168 | `"        for key in (\"potentially_missing_target_count\", \"source_evidence_gap_count\")"` | — |
| [SRC-1E32639872-L000169](../../agents/research_completion.py#L169) | 169 | `"    )"` | — |
| [SRC-1E32639872-L000170](../../agents/research_completion.py#L170) | 170 | `"    unsupported_numeric_count = _int("` | — |
| [SRC-1E32639872-L000171](../../agents/research_completion.py#L171) | 171 | `"        integrity.get(\"potentially_unsupported_numeric_count\")"` | — |
| [SRC-1E32639872-L000172](../../agents/research_completion.py#L172) | 172 | `"    ) or 0"` | — |
| [SRC-1E32639872-L000173](../../agents/research_completion.py#L173) | 173 | `"    unsupported_numeric_by_citation_count = _int("` | — |
| [SRC-1E32639872-L000174](../../agents/research_completion.py#L174) | 174 | `"        integrity.get(\"potentially_unsupported_numeric_by_citation_count\")"` | — |
| [SRC-1E32639872-L000175](../../agents/research_completion.py#L175) | 175 | `"    ) or 0"` | — |
| [SRC-1E32639872-L000176](../../agents/research_completion.py#L176) | 176 | `"    weak_citation_alignment_count = _int("` | — |
| [SRC-1E32639872-L000177](../../agents/research_completion.py#L177) | 177 | `"        integrity.get(\"weak_citation_alignment_count\")"` | — |
| [SRC-1E32639872-L000178](../../agents/research_completion.py#L178) | 178 | `"    ) or 0"` | — |
| [SRC-1E32639872-L000179](../../agents/research_completion.py#L179) | 179 | `"    # The cited-source numeric count can overlap with the general unsupported-number"` | — |
| [SRC-1E32639872-L000180](../../agents/research_completion.py#L180) | 180 | `"    # count. Use the larger count, then add weakly aligned cited segments."` | — |
| [SRC-1E32639872-L000181](../../agents/research_completion.py#L181) | 181 | `"    citation_support_warning_count = ("` | — |
| [SRC-1E32639872-L000182](../../agents/research_completion.py#L182) | 182 | `"        max(unsupported_numeric_count, unsupported_numeric_by_citation_count)"` | — |
| [SRC-1E32639872-L000183](../../agents/research_completion.py#L183) | 183 | `"        + weak_citation_alignment_count"` | — |
| [SRC-1E32639872-L000184](../../agents/research_completion.py#L184) | 184 | `"    )"` | — |
| [SRC-1E32639872-L000185](../../agents/research_completion.py#L185) | 185 | `"    fulfillment = str("` | — |
| [SRC-1E32639872-L000186](../../agents/research_completion.py#L186) | 186 | `"        result.get(\"task_fulfillment_status\") or report.get(\"task_fulfillment_status\") or \"\""` | — |
| [SRC-1E32639872-L000187](../../agents/research_completion.py#L187) | 187 | `"    )"` | — |
| [SRC-1E32639872-L000188](../../agents/research_completion.py#L188) | 188 | `"    citations = _dict(result.get(\"citation_validation\") or result.get(\"citation_check\"))"` | — |
| [SRC-1E32639872-L000189](../../agents/research_completion.py#L189) | 189 | `"    citation_count = _int(citations.get(\"valid_citation_count\")) or 0"` | — |
| [SRC-1E32639872-L000190](../../agents/research_completion.py#L190) | 190 | `"    generation_failed = any("` | — |
| [SRC-1E32639872-L000191](../../agents/research_completion.py#L191) | 191 | `"        token in final_status for token in (\"failed\", \"unavailable\", \"budget_exhausted\")"` | — |
| [SRC-1E32639872-L000192](../../agents/research_completion.py#L192) | 192 | `"    )"` | — |
| [SRC-1E32639872-L000193](../../agents/research_completion.py#L193) | 193 | `""` | — |
| [SRC-1E32639872-L000194](../../agents/research_completion.py#L194) | 194 | `"    if exhausted:"` | — |
| [SRC-1E32639872-L000195](../../agents/research_completion.py#L195) | 195 | `"        status = \"execution_stopped_budget\""` | — |
| [SRC-1E32639872-L000196](../../agents/research_completion.py#L196) | 196 | `"    elif not sources:"` | — |
| [SRC-1E32639872-L000197](../../agents/research_completion.py#L197) | 197 | `"        if rejected:"` | — |
| [SRC-1E32639872-L000198](../../agents/research_completion.py#L198) | 198 | `"            status = \"no_eligible_sources_after_filtering\""` | — |
| [SRC-1E32639872-L000199](../../agents/research_completion.py#L199) | 199 | `"        elif str(report.get(\"search_outcome\") or \"\") in _RESEARCH_ERRORS or ("` | — |
| [SRC-1E32639872-L000200](../../agents/research_completion.py#L200) | 200 | `"            connector_errors and not connector_ok"` | — |
| [SRC-1E32639872-L000201](../../agents/research_completion.py#L201) | 201 | `"        ):"` | — |
| [SRC-1E32639872-L000202](../../agents/research_completion.py#L202) | 202 | `"            status = \"search_failed_or_incomplete\""` | — |
| [SRC-1E32639872-L000203](../../agents/research_completion.py#L203) | 203 | `"        elif zero_results:"` | — |
| [SRC-1E32639872-L000204](../../agents/research_completion.py#L204) | 204 | `"            status = \"no_results_returned\""` | — |
| [SRC-1E32639872-L000205](../../agents/research_completion.py#L205) | 205 | `"        elif attempted is False:"` | — |
| [SRC-1E32639872-L000206](../../agents/research_completion.py#L206) | 206 | `"            status = \"search_not_attempted\""` | — |
| [SRC-1E32639872-L000207](../../agents/research_completion.py#L207) | 207 | `"        else:"` | — |
| [SRC-1E32639872-L000208](../../agents/research_completion.py#L208) | 208 | `"            status = \"insufficient_evidence\""` | — |
| [SRC-1E32639872-L000209](../../agents/research_completion.py#L209) | 209 | `"    elif not model_used:"` | — |
| [SRC-1E32639872-L000210](../../agents/research_completion.py#L210) | 210 | `"        status = ("` | — |
| [SRC-1E32639872-L000211](../../agents/research_completion.py#L211) | 211 | `"            \"source_snippets_only_generation_not_completed\""` | — |
| [SRC-1E32639872-L000212](../../agents/research_completion.py#L212) | 212 | `"            if read == 0 else \"evidence_collected_generation_not_completed\""` | — |
| [SRC-1E32639872-L000213](../../agents/research_completion.py#L213) | 213 | `"        )"` | — |
| [SRC-1E32639872-L000214](../../agents/research_completion.py#L214) | 214 | `"    elif generation_failed:"` | — |
| [SRC-1E32639872-L000215](../../agents/research_completion.py#L215) | 215 | `"        status = \"answer_generation_or_review_failed\""` | — |
| [SRC-1E32639872-L000216](../../agents/research_completion.py#L216) | 216 | `"    elif gap_count or citation_support_warning_count or fulfillment in {"` | — |
| [SRC-1E32639872-L000217](../../agents/research_completion.py#L217) | 217 | `"        \"possible_gap_detected\", \"source_evidence_gap_unresolved\","` | — |
| [SRC-1E32639872-L000218](../../agents/research_completion.py#L218) | 218 | `"        \"not_assessed_insufficient_evidence\","` | — |
| [SRC-1E32639872-L000219](../../agents/research_completion.py#L219) | 219 | `"    }:"` | — |
| [SRC-1E32639872-L000220](../../agents/research_completion.py#L220) | 220 | `"        status = \"partial_answer_evidence_gaps_detected\""` | — |
| [SRC-1E32639872-L000221](../../agents/research_completion.py#L221) | 221 | `"    elif citation_count:"` | — |
| [SRC-1E32639872-L000222](../../agents/research_completion.py#L222) | 222 | `"        status = \"answer_generated_citations_range_checked_semantic_support_unverified\""` | — |
| [SRC-1E32639872-L000223](../../agents/research_completion.py#L223) | 223 | `"    else:"` | — |
| [SRC-1E32639872-L000224](../../agents/research_completion.py#L224) | 224 | `"        status = \"answer_generated_without_valid_citation_markers\""` | — |
| [SRC-1E32639872-L000225](../../agents/research_completion.py#L225) | 225 | `""` | — |
| [SRC-1E32639872-L000226](../../agents/research_completion.py#L226) | 226 | `"    if attempted is False:"` | — |
| [SRC-1E32639872-L000227](../../agents/research_completion.py#L227) | 227 | `"        search_phase = \"not_attempted\""` | — |
| [SRC-1E32639872-L000228](../../agents/research_completion.py#L228) | 228 | `"    elif attempted is None:"` | — |
| [SRC-1E32639872-L000229](../../agents/research_completion.py#L229) | 229 | `"        search_phase = \"unknown\""` | — |
| [SRC-1E32639872-L000230](../../agents/research_completion.py#L230) | 230 | `"    elif connector_errors and not connector_ok and not sources:"` | — |
| [SRC-1E32639872-L000231](../../agents/research_completion.py#L231) | 231 | `"        search_phase = \"failed_or_incomplete\""` | — |
| [SRC-1E32639872-L000232](../../agents/research_completion.py#L232) | 232 | `"    elif sources:"` | — |
| [SRC-1E32639872-L000233](../../agents/research_completion.py#L233) | 233 | `"        search_phase = \"results_received\""` | — |
| [SRC-1E32639872-L000234](../../agents/research_completion.py#L234) | 234 | `"    elif zero_results:"` | — |
| [SRC-1E32639872-L000235](../../agents/research_completion.py#L235) | 235 | `"        search_phase = \"completed_no_results\""` | — |
| [SRC-1E32639872-L000236](../../agents/research_completion.py#L236) | 236 | `"    else:"` | — |
| [SRC-1E32639872-L000237](../../agents/research_completion.py#L237) | 237 | `"        search_phase = \"attempted_no_usable_sources\""` | — |
| [SRC-1E32639872-L000238](../../agents/research_completion.py#L238) | 238 | `""` | — |
| [SRC-1E32639872-L000239](../../agents/research_completion.py#L239) | 239 | `"    if not sources:"` | — |
| [SRC-1E32639872-L000240](../../agents/research_completion.py#L240) | 240 | `"        read_phase = \"not_applicable_no_eligible_sources\""` | — |
| [SRC-1E32639872-L000241](../../agents/research_completion.py#L241) | 241 | `"    elif read == len(sources):"` | — |
| [SRC-1E32639872-L000242](../../agents/research_completion.py#L242) | 242 | `"        read_phase = \"all_final_sources_read\""` | — |
| [SRC-1E32639872-L000243](../../agents/research_completion.py#L243) | 243 | `"    elif read:"` | — |
| [SRC-1E32639872-L000244](../../agents/research_completion.py#L244) | 244 | `"        read_phase = \"some_final_sources_read\""` | — |
| [SRC-1E32639872-L000245](../../agents/research_completion.py#L245) | 245 | `"    else:"` | — |
| [SRC-1E32639872-L000246](../../agents/research_completion.py#L246) | 246 | `"        read_phase = \"no_final_source_page_read\""` | — |
| [SRC-1E32639872-L000247](../../agents/research_completion.py#L247) | 247 | `""` | — |
| [SRC-1E32639872-L000248](../../agents/research_completion.py#L248) | 248 | `"    if kind == \"insufficient_evidence\" or not sources:"` | — |
| [SRC-1E32639872-L000249](../../agents/research_completion.py#L249) | 249 | `"        generation_phase = \"not_attempted_or_withheld\""` | — |
| [SRC-1E32639872-L000250](../../agents/research_completion.py#L250) | 250 | `"    elif model_used and not generation_failed:"` | — |
| [SRC-1E32639872-L000251](../../agents/research_completion.py#L251) | 251 | `"        generation_phase = \"answer_generated\""` | — |
| [SRC-1E32639872-L000252](../../agents/research_completion.py#L252) | 252 | `"    elif model_used:"` | — |
| [SRC-1E32639872-L000253](../../agents/research_completion.py#L253) | 253 | `"        generation_phase = \"failed_or_unavailable\""` | — |
| [SRC-1E32639872-L000254](../../agents/research_completion.py#L254) | 254 | `"    else:"` | — |
| [SRC-1E32639872-L000255](../../agents/research_completion.py#L255) | 255 | `"        generation_phase = \"not_completed\""` | — |
| [SRC-1E32639872-L000256](../../agents/research_completion.py#L256) | 256 | `""` | — |
| [SRC-1E32639872-L000257](../../agents/research_completion.py#L257) | 257 | `"    return {"` | — |
| [SRC-1E32639872-L000258](../../agents/research_completion.py#L258) | 258 | `"        \"status\": status,"` | — |
| [SRC-1E32639872-L000259](../../agents/research_completion.py#L259) | 259 | `"        \"status_semantics\": \"pipeline_state_not_probability_of_factual_correctness\","` | — |
| [SRC-1E32639872-L000260](../../agents/research_completion.py#L260) | 260 | `"        \"phases\": {"` | — |
| [SRC-1E32639872-L000261](../../agents/research_completion.py#L261) | 261 | `"            \"planning\": \"completed\" if isinstance(result.get(\"research_plan\"), dict) else \"unknown\","` | — |
| [SRC-1E32639872-L000262](../../agents/research_completion.py#L262) | 262 | `"            \"search\": search_phase,"` | — |
| [SRC-1E32639872-L000263](../../agents/research_completion.py#L263) | 263 | `"            \"source_filtering\": ("` | — |
| [SRC-1E32639872-L000264](../../agents/research_completion.py#L264) | 264 | `"                \"sources_retained\" if sources else"` | — |
| [SRC-1E32639872-L000265](../../agents/research_completion.py#L265) | 265 | `"                \"rejected_all_candidates\" if rejected else \"no_eligible_sources\""` | — |
| [SRC-1E32639872-L000266](../../agents/research_completion.py#L266) | 266 | `"            ),"` | — |
| [SRC-1E32639872-L000267](../../agents/research_completion.py#L267) | 267 | `"            \"page_reading\": read_phase,"` | — |
| [SRC-1E32639872-L000268](../../agents/research_completion.py#L268) | 268 | `"            \"answer_generation\": generation_phase,"` | — |
| [SRC-1E32639872-L000269](../../agents/research_completion.py#L269) | 269 | `"            \"citation_validation\": str(citations.get(\"status\") or \"not_run\"),"` | — |
| [SRC-1E32639872-L000270](../../agents/research_completion.py#L270) | 270 | `"            \"citation_support_screen\": ("` | — |
| [SRC-1E32639872-L000271](../../agents/research_completion.py#L271) | 271 | `"                \"warning_signals_detected\""` | — |
| [SRC-1E32639872-L000272](../../agents/research_completion.py#L272) | 272 | `"                if citation_support_warning_count"` | — |
| [SRC-1E32639872-L000273](../../agents/research_completion.py#L273) | 273 | `"                else \"no_lexical_warning_signals_detected_not_verified\""` | — |
| [SRC-1E32639872-L000274](../../agents/research_completion.py#L274) | 274 | `"                if any(key in integrity for key in ("` | — |
| [SRC-1E32639872-L000275](../../agents/research_completion.py#L275) | 275 | `"                    \"potentially_unsupported_numeric_count\","` | — |
| [SRC-1E32639872-L000276](../../agents/research_completion.py#L276) | 276 | `"                    \"potentially_unsupported_numeric_by_citation_count\","` | — |
| [SRC-1E32639872-L000277](../../agents/research_completion.py#L277) | 277 | `"                    \"weak_citation_alignment_count\","` | — |
| [SRC-1E32639872-L000278](../../agents/research_completion.py#L278) | 278 | `"                ))"` | — |
| [SRC-1E32639872-L000279](../../agents/research_completion.py#L279) | 279 | `"                else \"not_assessed\""` | — |
| [SRC-1E32639872-L000280](../../agents/research_completion.py#L280) | 280 | `"            ),"` | — |
| [SRC-1E32639872-L000281](../../agents/research_completion.py#L281) | 281 | `"            \"semantic_verification\": \"not_performed\","` | — |
| [SRC-1E32639872-L000282](../../agents/research_completion.py#L282) | 282 | `"        },"` | — |
| [SRC-1E32639872-L000283](../../agents/research_completion.py#L283) | 283 | `"        \"counters\": {"` | — |
| [SRC-1E32639872-L000284](../../agents/research_completion.py#L284) | 284 | `"            \"queries_planned\": _int(report.get(\"queries_planned\")),"` | — |
| [SRC-1E32639872-L000285](../../agents/research_completion.py#L285) | 285 | `"            \"queries_attempted\": _int(report.get(\"queries_attempted\")),"` | — |
| [SRC-1E32639872-L000286](../../agents/research_completion.py#L286) | 286 | `"            \"per_query_result_count_sum\": query_total,"` | — |
| [SRC-1E32639872-L000287](../../agents/research_completion.py#L287) | 287 | `"            \"per_query_result_count_sum_semantics\": \"sum_of_reported_per_query_counts_not_deduplicated_sources\","` | — |
| [SRC-1E32639872-L000288](../../agents/research_completion.py#L288) | 288 | `"            \"query_result_row_count\": len(query_rows),"` | — |
| [SRC-1E32639872-L000289](../../agents/research_completion.py#L289) | 289 | `"            \"query_result_rows_with_counts\": sum("` | — |
| [SRC-1E32639872-L000290](../../agents/research_completion.py#L290) | 290 | `"                isinstance(row, dict) and _int(row.get(\"results\")) is not None"` | — |
| [SRC-1E32639872-L000291](../../agents/research_completion.py#L291) | 291 | `"                for row in query_rows"` | — |
| [SRC-1E32639872-L000292](../../agents/research_completion.py#L292) | 292 | `"            ),"` | — |
| [SRC-1E32639872-L000293](../../agents/research_completion.py#L293) | 293 | `"            \"final_source_list_count\": len(sources),"` | — |
| [SRC-1E32639872-L000294](../../agents/research_completion.py#L294) | 294 | `"            \"unique_normalized_url_count\": len(unique_urls),"` | — |
| [SRC-1E32639872-L000295](../../agents/research_completion.py#L295) | 295 | `"            \"duplicate_normalized_url_count\": max(0, len(url_keys) - len(unique_urls)),"` | — |
| [SRC-1E32639872-L000296](../../agents/research_completion.py#L296) | 296 | `"            \"distinct_registrable_domain_count\": len(domains),"` | — |
| [SRC-1E32639872-L000297](../../agents/research_completion.py#L297) | 297 | `"            \"pages_fetched_flag_count\": fetched,"` | — |
| [SRC-1E32639872-L000298](../../agents/research_completion.py#L298) | 298 | `"            \"pages_read_with_text_count\": read,"` | — |
| [SRC-1E32639872-L000299](../../agents/research_completion.py#L299) | 299 | `"            \"snippet_only_source_count\": snippet_only,"` | — |
| [SRC-1E32639872-L000300](../../agents/research_completion.py#L300) | 300 | `"            \"page_text_without_fetched_flag_count\": unflagged_text,"` | — |
| [SRC-1E32639872-L000301](../../agents/research_completion.py#L301) | 301 | `"            \"connector_status_counts\": connector_counts,"` | — |
| [SRC-1E32639872-L000302](../../agents/research_completion.py#L302) | 302 | `"            \"connector_failure_count\": connector_errors,"` | — |
| [SRC-1E32639872-L000303](../../agents/research_completion.py#L303) | 303 | `"            \"connector_success_count\": connector_ok,"` | — |
| [SRC-1E32639872-L000304](../../agents/research_completion.py#L304) | 304 | `"            \"guardrail_rejected_candidate_count\": rejected,"` | — |
| [SRC-1E32639872-L000305](../../agents/research_completion.py#L305) | 305 | `"            \"potentially_unsupported_numeric_count\": unsupported_numeric_count,"` | — |
| [SRC-1E32639872-L000306](../../agents/research_completion.py#L306) | 306 | `"            \"potentially_unsupported_numeric_by_citation_count\": unsupported_numeric_by_citation_count,"` | — |
| [SRC-1E32639872-L000307](../../agents/research_completion.py#L307) | 307 | `"            \"weak_citation_alignment_count\": weak_citation_alignment_count,"` | — |
| [SRC-1E32639872-L000308](../../agents/research_completion.py#L308) | 308 | `"            \"citation_support_warning_count\": citation_support_warning_count,"` | — |
| [SRC-1E32639872-L000309](../../agents/research_completion.py#L309) | 309 | `"        },"` | — |
| [SRC-1E32639872-L000310](../../agents/research_completion.py#L310) | 310 | `"        \"counter_consistency\": {"` | — |
| [SRC-1E32639872-L000311](../../agents/research_completion.py#L311) | 311 | `"            \"status\": \"mismatch_detected\" if counter_issues else ("` | — |
| [SRC-1E32639872-L000312](../../agents/research_completion.py#L312) | 312 | `"                \"matched\" if reported_sources is not None or reported_fetched is not None"` | — |
| [SRC-1E32639872-L000313](../../agents/research_completion.py#L313) | 313 | `"                else \"not_computable\""` | — |
| [SRC-1E32639872-L000314](../../agents/research_completion.py#L314) | 314 | `"            ),"` | — |
| [SRC-1E32639872-L000315](../../agents/research_completion.py#L315) | 315 | `"            \"reported_unique_sources\": reported_sources,"` | — |
| [SRC-1E32639872-L000316](../../agents/research_completion.py#L316) | 316 | `"            \"recomputed_final_source_count\": len(sources),"` | — |
| [SRC-1E32639872-L000317](../../agents/research_completion.py#L317) | 317 | `"            \"reported_pages_fetched\": reported_fetched,"` | — |
| [SRC-1E32639872-L000318](../../agents/research_completion.py#L318) | 318 | `"            \"recomputed_pages_fetched_flag_count\": fetched,"` | — |
| [SRC-1E32639872-L000319](../../agents/research_completion.py#L319) | 319 | `"            \"issues\": counter_issues,"` | — |
| [SRC-1E32639872-L000320](../../agents/research_completion.py#L320) | 320 | `"        },"` | — |
| [SRC-1E32639872-L000321](../../agents/research_completion.py#L321) | 321 | `"        \"semantic_verification\": \"not_performed\","` | — |
| [SRC-1E32639872-L000322](../../agents/research_completion.py#L322) | 322 | `"        \"warning\": ("` | — |
| [SRC-1E32639872-L000323](../../agents/research_completion.py#L323) | 323 | `"            \"Readable pages and valid citation indexes do not prove semantic support \""` | — |
| [SRC-1E32639872-L000324](../../agents/research_completion.py#L324) | 324 | `"            \"for each claim in the answer.\""` | — |
| [SRC-1E32639872-L000325](../../agents/research_completion.py#L325) | 325 | `"        ),"` | — |
| [SRC-1E32639872-L000326](../../agents/research_completion.py#L326) | 326 | `"    }"` | — |
## الوكيل والمنطق

### FILE-3AA6165B18 — [agents/research_guardrails.py](../../agents/research_guardrails.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-3AA6165B18-L000001](../../agents/research_guardrails.py#L1) | 1 | `"\"\"\"Task-specific guardrails for search evidence."` | — |
| [SRC-3AA6165B18-L000002](../../agents/research_guardrails.py#L2) | 2 | `""` | — |
| [SRC-3AA6165B18-L000003](../../agents/research_guardrails.py#L3) | 3 | `"These checks are conservative retrieval filters, not proof of factual correctness."` | — |
| [SRC-3AA6165B18-L000004](../../agents/research_guardrails.py#L4) | 4 | `"\"\"\""` | — |
| [SRC-3AA6165B18-L000005](../../agents/research_guardrails.py#L5) | 5 | `"from __future__ import annotations"` | — |
| [SRC-3AA6165B18-L000006](../../agents/research_guardrails.py#L6) | 6 | `""` | — |
| [SRC-3AA6165B18-L000007](../../agents/research_guardrails.py#L7) | 7 | `"import re"` | — |
| [SRC-3AA6165B18-L000008](../../agents/research_guardrails.py#L8) | 8 | `"from datetime import UTC, datetime, timedelta"` | — |
| [SRC-3AA6165B18-L000009](../../agents/research_guardrails.py#L9) | 9 | `"from typing import Any"` | — |
| [SRC-3AA6165B18-L000010](../../agents/research_guardrails.py#L10) | 10 | `"from urllib.parse import urlsplit"` | — |
| [SRC-3AA6165B18-L000011](../../agents/research_guardrails.py#L11) | 11 | `""` | — |
| [SRC-3AA6165B18-L000012](../../agents/research_guardrails.py#L12) | 12 | `"from agents.research import ("` | — |
| [SRC-3AA6165B18-L000013](../../agents/research_guardrails.py#L13) | 13 | `"    SOCIAL_DOMAINS,"` | — |
| [SRC-3AA6165B18-L000014](../../agents/research_guardrails.py#L14) | 14 | `"    _parse_publication_date,"` | — |
| [SRC-3AA6165B18-L000015](../../agents/research_guardrails.py#L15) | 15 | `"    detect_freshness,"` | — |
| [SRC-3AA6165B18-L000016](../../agents/research_guardrails.py#L16) | 16 | `")"` | — |
| [SRC-3AA6165B18-L000017](../../agents/research_guardrails.py#L17) | 17 | `""` | — |
| [SRC-3AA6165B18-L000018](../../agents/research_guardrails.py#L18) | 18 | `"_CURRENT_EVIDENCE_MAX_AGE_DAYS = 7"` | — |
| [SRC-3AA6165B18-L000019](../../agents/research_guardrails.py#L19) | 19 | `"_GOVERNMENT_SUFFIXES = ("` | — |
| [SRC-3AA6165B18-L000020](../../agents/research_guardrails.py#L20) | 20 | `"    \".gov\", \".gov.eg\", \".gov.uk\", \".gov.sa\", \".gov.ae\", \".gov.au\","` | — |
| [SRC-3AA6165B18-L000021](../../agents/research_guardrails.py#L21) | 21 | `"    \".gov.in\", \".gov.cn\", \".gov.br\", \".gob.mx\", \".go.jp\", \".gc.ca\","` | — |
| [SRC-3AA6165B18-L000022](../../agents/research_guardrails.py#L22) | 22 | `"    \".govt.nz\", \".gouv.fr\","` | — |
| [SRC-3AA6165B18-L000023](../../agents/research_guardrails.py#L23) | 23 | `")"` | — |
| [SRC-3AA6165B18-L000024](../../agents/research_guardrails.py#L24) | 24 | `"_CURRENT_GOVERNMENT_SERVICE_TERMS = ("` | — |
| [SRC-3AA6165B18-L000025](../../agents/research_guardrails.py#L25) | 25 | `"    \"الجوازات\", \"مكتب الجوازات\", \"مصلحة الجوازات\", \"السجل المدني\","` | — |
| [SRC-3AA6165B18-L000026](../../agents/research_guardrails.py#L26) | 26 | `"    \"الشهر العقاري\", \"مكتب المرور\", \"إدارة المرور\", \"مكتب حكومي\","` | — |
| [SRC-3AA6165B18-L000027](../../agents/research_guardrails.py#L27) | 27 | `"    \"خدمة حكومية\", \"مصلحة حكومية\", \"وزارة\", \"هيئة حكومية\","` | — |
| [SRC-3AA6165B18-L000028](../../agents/research_guardrails.py#L28) | 28 | `"    \"passport office\", \"civil registry\", \"traffic office\","` | — |
| [SRC-3AA6165B18-L000029](../../agents/research_guardrails.py#L29) | 29 | `"    \"government office\", \"government service\","` | — |
| [SRC-3AA6165B18-L000030](../../agents/research_guardrails.py#L30) | 30 | `")"` | — |
| [SRC-3AA6165B18-L000031](../../agents/research_guardrails.py#L31) | 31 | `"_GOVERNMENT_HOURS_TERMS = ("` | — |
| [SRC-3AA6165B18-L000032](../../agents/research_guardrails.py#L32) | 32 | `"    \"مواعيد\", \"مواعيد العمل\", \"ساعات العمل\", \"يفتح\", \"مفتوح\","` | — |
| [SRC-3AA6165B18-L000033](../../agents/research_guardrails.py#L33) | 33 | `"    \"يغلق\", \"مواعيد الدوام\", \"working hours\", \"opening hours\","` | — |
| [SRC-3AA6165B18-L000034](../../agents/research_guardrails.py#L34) | 34 | `"    \"office hours\", \"open today\", \"closes today\","` | — |
| [SRC-3AA6165B18-L000035](../../agents/research_guardrails.py#L35) | 35 | `")"` | — |
| [SRC-3AA6165B18-L000036](../../agents/research_guardrails.py#L36) | 36 | `"_OFFICIAL_WORDS = ("` | — |
| [SRC-3AA6165B18-L000037](../../agents/research_guardrails.py#L37) | 37 | `"    \"الموقع الرسمي\", \"موقع رسمي\", \"الصفحة الرسمية\", \"الموقع الحكومي\","` | — |
| [SRC-3AA6165B18-L000038](../../agents/research_guardrails.py#L38) | 38 | `"    \"official website\", \"official site\", \"official homepage\","` | — |
| [SRC-3AA6165B18-L000039](../../agents/research_guardrails.py#L39) | 39 | `")"` | — |
| [SRC-3AA6165B18-L000040](../../agents/research_guardrails.py#L40) | 40 | `"_GOVERNMENT_ENTITY_WORDS = ("` | — |
| [SRC-3AA6165B18-L000041](../../agents/research_guardrails.py#L41) | 41 | `"    \"وزارة\", \"الوزارة\", \"وزاره\", \"هيئة حكومية\", \"جهة حكومية\", \"مصلحة حكومية\","` | — |
| [SRC-3AA6165B18-L000042](../../agents/research_guardrails.py#L42) | 42 | `"    \"ministry\", \"government agency\", \"government ministry\", \"department of\","` | — |
| [SRC-3AA6165B18-L000043](../../agents/research_guardrails.py#L43) | 43 | `")"` | — |
| [SRC-3AA6165B18-L000044](../../agents/research_guardrails.py#L44) | 44 | `"_TODAY_WORDS = ("` | — |
| [SRC-3AA6165B18-L000045](../../agents/research_guardrails.py#L45) | 45 | `"    \"اليوم\", \"النهارده\", \"النهاردة\", \"دلوقتي\", \"الآن\", \"حاليا\","` | — |
| [SRC-3AA6165B18-L000046](../../agents/research_guardrails.py#L46) | 46 | `"    \"today\", \"right now\", \"currently\", \"current hours\","` | — |
| [SRC-3AA6165B18-L000047](../../agents/research_guardrails.py#L47) | 47 | `")"` | — |
| [SRC-3AA6165B18-L000048](../../agents/research_guardrails.py#L48) | 48 | `"_PROMOTION_TERMS = ("` | — |
| [SRC-3AA6165B18-L000049](../../agents/research_guardrails.py#L49) | 49 | `"    \"للبيع\", \"للايجار\", \"للإيجار\", \"تواصل معنا\", \"اتصل الآن\", \"واتساب\","` | — |
| [SRC-3AA6165B18-L000050](../../agents/research_guardrails.py#L50) | 50 | `"    \"للحجز\", \"اشتر الآن\", \"اطلب الآن\", \"خصم\", \"عرض خاص\", \"السعر يبدأ\","` | — |
| [SRC-3AA6165B18-L000051](../../agents/research_guardrails.py#L51) | 51 | `"    \"for sale\", \"contact us\", \"call now\", \"whatsapp\", \"buy now\", \"shop now\","` | — |
| [SRC-3AA6165B18-L000052](../../agents/research_guardrails.py#L52) | 52 | `"    \"special offer\", \"discount\", \"sponsored\", \"affiliate\","` | — |
| [SRC-3AA6165B18-L000053](../../agents/research_guardrails.py#L53) | 53 | `")"` | — |
| [SRC-3AA6165B18-L000054](../../agents/research_guardrails.py#L54) | 54 | `"_PERSONAL_EXPERIENCE_TERMS = ("` | — |
| [SRC-3AA6165B18-L000055](../../agents/research_guardrails.py#L55) | 55 | `"    \"أنا امتلك\", \"انا امتلك\", \"أنا أملك\", \"انا املك\", \"عندي\", \"معايا\","` | — |
| [SRC-3AA6165B18-L000056](../../agents/research_guardrails.py#L56) | 56 | `"    \"جربت\", \"استخدمت\", \"اشتريت\", \"امتلكت\", \"تجربتي\", \"عن تجربتي\","` | — |
| [SRC-3AA6165B18-L000057](../../agents/research_guardrails.py#L57) | 57 | `"    \"بقالى\", \"بقالي\", \"I own\", \"I bought\", \"I have owned\", \"my experience\","` | — |
| [SRC-3AA6165B18-L000058](../../agents/research_guardrails.py#L58) | 58 | `"    \"I've had\", \"i have had\", \"I use\", \"I drove\", \"in my experience\","` | — |
| [SRC-3AA6165B18-L000059](../../agents/research_guardrails.py#L59) | 59 | `")"` | — |
| [SRC-3AA6165B18-L000060](../../agents/research_guardrails.py#L60) | 60 | `"_DISCUSSION_TERMS = ("` | — |
| [SRC-3AA6165B18-L000061](../../agents/research_guardrails.py#L61) | 61 | `"    \"حد جرب\", \"هل جرب\", \"مين جرب\", \"ما رأيكم\", \"ايه رأيكم\", \"ماذا تظنون\","` | — |
| [SRC-3AA6165B18-L000062](../../agents/research_guardrails.py#L62) | 62 | `"    \"anyone tried\", \"has anyone\", \"what do you think\", \"looking for opinions\","` | — |
| [SRC-3AA6165B18-L000063](../../agents/research_guardrails.py#L63) | 63 | `")"` | — |
| [SRC-3AA6165B18-L000064](../../agents/research_guardrails.py#L64) | 64 | `""` | — |
| [SRC-3AA6165B18-L000065](../../agents/research_guardrails.py#L65) | 65 | `""` | — |
| [SRC-3AA6165B18-L000066](../../agents/research_guardrails.py#L66) | 66 | `"def _normalized(value: Any) -> str:"` | — |
| [SRC-3AA6165B18-L000067](../../agents/research_guardrails.py#L67) | 67 | `"    return re.sub(r\"\\s+\", \" \", str(value or \"\")).strip().casefold()"` | — |
| [SRC-3AA6165B18-L000068](../../agents/research_guardrails.py#L68) | 68 | `""` | — |
| [SRC-3AA6165B18-L000069](../../agents/research_guardrails.py#L69) | 69 | `""` | — |
| [SRC-3AA6165B18-L000070](../../agents/research_guardrails.py#L70) | 70 | `"def _host(value: Any) -> str:"` | — |
| [SRC-3AA6165B18-L000071](../../agents/research_guardrails.py#L71) | 71 | `"    try:"` | — |
| [SRC-3AA6165B18-L000072](../../agents/research_guardrails.py#L72) | 72 | `"        return (urlsplit(str(value or \"\").strip()).hostname or \"\").rstrip(\".\").lower()"` | — |
| [SRC-3AA6165B18-L000073](../../agents/research_guardrails.py#L73) | 73 | `"    except (TypeError, ValueError):"` | — |
| [SRC-3AA6165B18-L000074](../../agents/research_guardrails.py#L74) | 74 | `"        return \"\""` | — |
| [SRC-3AA6165B18-L000075](../../agents/research_guardrails.py#L75) | 75 | `""` | — |
| [SRC-3AA6165B18-L000076](../../agents/research_guardrails.py#L76) | 76 | `""` | — |
| [SRC-3AA6165B18-L000077](../../agents/research_guardrails.py#L77) | 77 | `"def is_social_platform_url(url: Any) -> bool:"` | — |
| [SRC-3AA6165B18-L000078](../../agents/research_guardrails.py#L78) | 78 | `"    \"\"\"Return whether a URL belongs to a recognized public social platform.\"\"\""` | — |
| [SRC-3AA6165B18-L000079](../../agents/research_guardrails.py#L79) | 79 | `"    host = _host(url)"` | — |
| [SRC-3AA6165B18-L000080](../../agents/research_guardrails.py#L80) | 80 | `"    if not host:"` | — |
| [SRC-3AA6165B18-L000081](../../agents/research_guardrails.py#L81) | 81 | `"        return False"` | — |
| [SRC-3AA6165B18-L000082](../../agents/research_guardrails.py#L82) | 82 | `"    return any(host == domain or host.endswith(\".\" + domain)"` | — |
| [SRC-3AA6165B18-L000083](../../agents/research_guardrails.py#L83) | 83 | `"               for domain in SOCIAL_DOMAINS.values())"` | — |
| [SRC-3AA6165B18-L000084](../../agents/research_guardrails.py#L84) | 84 | `""` | — |
| [SRC-3AA6165B18-L000085](../../agents/research_guardrails.py#L85) | 85 | `""` | — |
| [SRC-3AA6165B18-L000086](../../agents/research_guardrails.py#L86) | 86 | `"def _is_navigation_request(question: str) -> bool:"` | — |
| [SRC-3AA6165B18-L000087](../../agents/research_guardrails.py#L87) | 87 | `"    value = _normalized(question)"` | — |
| [SRC-3AA6165B18-L000088](../../agents/research_guardrails.py#L88) | 88 | `"    return any(term in value for term in ("` | — |
| [SRC-3AA6165B18-L000089](../../agents/research_guardrails.py#L89) | 89 | `"        \"موقع\", \"رابط\", \"لينك\", \"homepage\", \"website\", \"official site\","` | — |
| [SRC-3AA6165B18-L000090](../../agents/research_guardrails.py#L90) | 90 | `"        \"official website\", \"link to\","` | — |
| [SRC-3AA6165B18-L000091](../../agents/research_guardrails.py#L91) | 91 | `"    ))"` | — |
| [SRC-3AA6165B18-L000092](../../agents/research_guardrails.py#L92) | 92 | `""` | — |
| [SRC-3AA6165B18-L000093](../../agents/research_guardrails.py#L93) | 93 | `""` | — |
| [SRC-3AA6165B18-L000094](../../agents/research_guardrails.py#L94) | 94 | `"def requires_official_government_domain(question: str) -> bool:"` | — |
| [SRC-3AA6165B18-L000095](../../agents/research_guardrails.py#L95) | 95 | `"    \"\"\"Detect explicit requests for a government's official site, not articles about it.\"\"\""` | — |
| [SRC-3AA6165B18-L000096](../../agents/research_guardrails.py#L96) | 96 | `"    value = _normalized(question)"` | — |
| [SRC-3AA6165B18-L000097](../../agents/research_guardrails.py#L97) | 97 | `"    return ("` | — |
| [SRC-3AA6165B18-L000098](../../agents/research_guardrails.py#L98) | 98 | `"        any(term in value for term in _OFFICIAL_WORDS)"` | — |
| [SRC-3AA6165B18-L000099](../../agents/research_guardrails.py#L99) | 99 | `"        and any(term in value for term in _GOVERNMENT_ENTITY_WORDS)"` | — |
| [SRC-3AA6165B18-L000100](../../agents/research_guardrails.py#L100) | 100 | `"    )"` | — |
| [SRC-3AA6165B18-L000101](../../agents/research_guardrails.py#L101) | 101 | `""` | — |
| [SRC-3AA6165B18-L000102](../../agents/research_guardrails.py#L102) | 102 | `""` | — |
| [SRC-3AA6165B18-L000103](../../agents/research_guardrails.py#L103) | 103 | `"def _is_government_domain(url: Any) -> bool:"` | — |
| [SRC-3AA6165B18-L000104](../../agents/research_guardrails.py#L104) | 104 | `"    host = _host(url)"` | — |
| [SRC-3AA6165B18-L000105](../../agents/research_guardrails.py#L105) | 105 | `"    if not host:"` | — |
| [SRC-3AA6165B18-L000106](../../agents/research_guardrails.py#L106) | 106 | `"        return False"` | — |
| [SRC-3AA6165B18-L000107](../../agents/research_guardrails.py#L107) | 107 | `"    return any(host == suffix.lstrip(\".\") or host.endswith(suffix)"` | — |
| [SRC-3AA6165B18-L000108](../../agents/research_guardrails.py#L108) | 108 | `"               for suffix in _GOVERNMENT_SUFFIXES)"` | — |
| [SRC-3AA6165B18-L000109](../../agents/research_guardrails.py#L109) | 109 | `""` | — |
| [SRC-3AA6165B18-L000110](../../agents/research_guardrails.py#L110) | 110 | `""` | — |
| [SRC-3AA6165B18-L000111](../../agents/research_guardrails.py#L111) | 111 | `"def requires_official_current_government_source(question: str) -> bool:"` | — |
| [SRC-3AA6165B18-L000112](../../agents/research_guardrails.py#L112) | 112 | `"    \"\"\"Require an official-domain candidate for current government service hours.\"\"\""` | — |
| [SRC-3AA6165B18-L000113](../../agents/research_guardrails.py#L113) | 113 | `"    value = _normalized(question)"` | — |
| [SRC-3AA6165B18-L000114](../../agents/research_guardrails.py#L114) | 114 | `"    has_service = any("` | — |
| [SRC-3AA6165B18-L000115](../../agents/research_guardrails.py#L115) | 115 | `"        _normalized(term) in value for term in _CURRENT_GOVERNMENT_SERVICE_TERMS"` | — |
| [SRC-3AA6165B18-L000116](../../agents/research_guardrails.py#L116) | 116 | `"    )"` | — |
| [SRC-3AA6165B18-L000117](../../agents/research_guardrails.py#L117) | 117 | `"    has_hours = any("` | — |
| [SRC-3AA6165B18-L000118](../../agents/research_guardrails.py#L118) | 118 | `"        _normalized(term) in value for term in _GOVERNMENT_HOURS_TERMS"` | — |
| [SRC-3AA6165B18-L000119](../../agents/research_guardrails.py#L119) | 119 | `"    )"` | — |
| [SRC-3AA6165B18-L000120](../../agents/research_guardrails.py#L120) | 120 | `"    return detect_freshness(question) and has_service and has_hours"` | — |
| [SRC-3AA6165B18-L000121](../../agents/research_guardrails.py#L121) | 121 | `""` | — |
| [SRC-3AA6165B18-L000122](../../agents/research_guardrails.py#L122) | 122 | `""` | — |
| [SRC-3AA6165B18-L000123](../../agents/research_guardrails.py#L123) | 123 | `"def assess_current_source("` | — |
| [SRC-3AA6165B18-L000124](../../agents/research_guardrails.py#L124) | 124 | `"    source: dict[str, Any],"` | — |
| [SRC-3AA6165B18-L000125](../../agents/research_guardrails.py#L125) | 125 | `"    *,"` | — |
| [SRC-3AA6165B18-L000126](../../agents/research_guardrails.py#L126) | 126 | `"    now: datetime \| None = None,"` | — |
| [SRC-3AA6165B18-L000127](../../agents/research_guardrails.py#L127) | 127 | `"    max_age_days: int = _CURRENT_EVIDENCE_MAX_AGE_DAYS,"` | — |
| [SRC-3AA6165B18-L000128](../../agents/research_guardrails.py#L128) | 128 | `") -> dict[str, Any]:"` | — |
| [SRC-3AA6165B18-L000129](../../agents/research_guardrails.py#L129) | 129 | `"    \"\"\"Assess whether a read page can support a current-state claim.\"\"\""` | — |
| [SRC-3AA6165B18-L000130](../../agents/research_guardrails.py#L130) | 130 | `"    current = now or datetime.now(UTC)"` | — |
| [SRC-3AA6165B18-L000131](../../agents/research_guardrails.py#L131) | 131 | `"    if current.tzinfo is None:"` | — |
| [SRC-3AA6165B18-L000132](../../agents/research_guardrails.py#L132) | 132 | `"        current = current.replace(tzinfo=UTC)"` | — |
| [SRC-3AA6165B18-L000133](../../agents/research_guardrails.py#L133) | 133 | `"    published = _parse_publication_date(source.get(\"published_at\"), current)"` | — |
| [SRC-3AA6165B18-L000134](../../agents/research_guardrails.py#L134) | 134 | `"    if published is None:"` | — |
| [SRC-3AA6165B18-L000135](../../agents/research_guardrails.py#L135) | 135 | `"        return {\"eligible\": False, \"status\": \"date_unavailable\", \"age_days\": None}"` | — |
| [SRC-3AA6165B18-L000136](../../agents/research_guardrails.py#L136) | 136 | `"    if published > current + timedelta(days=1):"` | — |
| [SRC-3AA6165B18-L000137](../../agents/research_guardrails.py#L137) | 137 | `"        return {\"eligible\": False, \"status\": \"future_date\", \"age_days\": None}"` | — |
| [SRC-3AA6165B18-L000138](../../agents/research_guardrails.py#L138) | 138 | `"    age_days = max(0, (current - published).total_seconds() / 86400)"` | — |
| [SRC-3AA6165B18-L000139](../../agents/research_guardrails.py#L139) | 139 | `"    if age_days > max_age_days:"` | — |
| [SRC-3AA6165B18-L000140](../../agents/research_guardrails.py#L140) | 140 | `"        return {"` | — |
| [SRC-3AA6165B18-L000141](../../agents/research_guardrails.py#L141) | 141 | `"            \"eligible\": False,"` | — |
| [SRC-3AA6165B18-L000142](../../agents/research_guardrails.py#L142) | 142 | `"            \"status\": \"stale\","` | — |
| [SRC-3AA6165B18-L000143](../../agents/research_guardrails.py#L143) | 143 | `"            \"age_days\": round(age_days, 2),"` | — |
| [SRC-3AA6165B18-L000144](../../agents/research_guardrails.py#L144) | 144 | `"            \"max_age_days\": max_age_days,"` | — |
| [SRC-3AA6165B18-L000145](../../agents/research_guardrails.py#L145) | 145 | `"        }"` | — |
| [SRC-3AA6165B18-L000146](../../agents/research_guardrails.py#L146) | 146 | `"    if not bool(source.get(\"page_fetched\")) or not str(source.get(\"page_text\") or \"\").strip():"` | — |
| [SRC-3AA6165B18-L000147](../../agents/research_guardrails.py#L147) | 147 | `"        return {"` | — |
| [SRC-3AA6165B18-L000148](../../agents/research_guardrails.py#L148) | 148 | `"            \"eligible\": False,"` | — |
| [SRC-3AA6165B18-L000149](../../agents/research_guardrails.py#L149) | 149 | `"            \"status\": \"page_not_read\","` | — |
| [SRC-3AA6165B18-L000150](../../agents/research_guardrails.py#L150) | 150 | `"            \"age_days\": round(age_days, 2),"` | — |
| [SRC-3AA6165B18-L000151](../../agents/research_guardrails.py#L151) | 151 | `"            \"max_age_days\": max_age_days,"` | — |
| [SRC-3AA6165B18-L000152](../../agents/research_guardrails.py#L152) | 152 | `"        }"` | — |
| [SRC-3AA6165B18-L000153](../../agents/research_guardrails.py#L153) | 153 | `"    return {"` | — |
| [SRC-3AA6165B18-L000154](../../agents/research_guardrails.py#L154) | 154 | `"        \"eligible\": True,"` | — |
| [SRC-3AA6165B18-L000155](../../agents/research_guardrails.py#L155) | 155 | `"        \"status\": \"recent_page_read\","` | — |
| [SRC-3AA6165B18-L000156](../../agents/research_guardrails.py#L156) | 156 | `"        \"age_days\": round(age_days, 2),"` | — |
| [SRC-3AA6165B18-L000157](../../agents/research_guardrails.py#L157) | 157 | `"        \"max_age_days\": max_age_days,"` | — |
| [SRC-3AA6165B18-L000158](../../agents/research_guardrails.py#L158) | 158 | `"    }"` | — |
| [SRC-3AA6165B18-L000159](../../agents/research_guardrails.py#L159) | 159 | `""` | — |
| [SRC-3AA6165B18-L000160](../../agents/research_guardrails.py#L160) | 160 | `""` | — |
| [SRC-3AA6165B18-L000161](../../agents/research_guardrails.py#L161) | 161 | `"def classify_social_source(source: dict[str, Any]) -> dict[str, str]:"` | — |
| [SRC-3AA6165B18-L000162](../../agents/research_guardrails.py#L162) | 162 | `"    \"\"\"Apply a transparent, non-authoritative label to public social content.\"\"\""` | — |
| [SRC-3AA6165B18-L000163](../../agents/research_guardrails.py#L163) | 163 | `"    url = source.get(\"url\", \"\")"` | — |
| [SRC-3AA6165B18-L000164](../../agents/research_guardrails.py#L164) | 164 | `"    host = _host(url)"` | — |
| [SRC-3AA6165B18-L000165](../../agents/research_guardrails.py#L165) | 165 | `"    platform = next(("` | — |
| [SRC-3AA6165B18-L000166](../../agents/research_guardrails.py#L166) | 166 | `"        name for name, domain in SOCIAL_DOMAINS.items()"` | — |
| [SRC-3AA6165B18-L000167](../../agents/research_guardrails.py#L167) | 167 | `"        if host == domain or host.endswith(\".\" + domain)"` | — |
| [SRC-3AA6165B18-L000168](../../agents/research_guardrails.py#L168) | 168 | `"    ), \"\")"` | — |
| [SRC-3AA6165B18-L000169](../../agents/research_guardrails.py#L169) | 169 | `"    if not platform:"` | — |
| [SRC-3AA6165B18-L000170](../../agents/research_guardrails.py#L170) | 170 | `"        return {"` | — |
| [SRC-3AA6165B18-L000171](../../agents/research_guardrails.py#L171) | 171 | `"            \"opinion_source_classification\": \"not_a_social_post\","` | — |
| [SRC-3AA6165B18-L000172](../../agents/research_guardrails.py#L172) | 172 | `"            \"opinion_classification_basis\": \"URL host is not a recognized social platform\","` | — |
| [SRC-3AA6165B18-L000173](../../agents/research_guardrails.py#L173) | 173 | `"            \"opinion_classification_method\": \"heuristic_only\","` | — |
| [SRC-3AA6165B18-L000174](../../agents/research_guardrails.py#L174) | 174 | `"        }"` | — |
| [SRC-3AA6165B18-L000175](../../agents/research_guardrails.py#L175) | 175 | `""` | — |
| [SRC-3AA6165B18-L000176](../../agents/research_guardrails.py#L176) | 176 | `"    text = _normalized(\" \".join("` | — |
| [SRC-3AA6165B18-L000177](../../agents/research_guardrails.py#L177) | 177 | `"        str(source.get(field) or \"\")"` | — |
| [SRC-3AA6165B18-L000178](../../agents/research_guardrails.py#L178) | 178 | `"        for field in (\"title\", \"snippet\", \"page_text\")"` | — |
| [SRC-3AA6165B18-L000179](../../agents/research_guardrails.py#L179) | 179 | `"    ))"` | — |
| [SRC-3AA6165B18-L000180](../../agents/research_guardrails.py#L180) | 180 | `"    # Normalize the vocabulary as well as the source text so English phrases"` | — |
| [SRC-3AA6165B18-L000181](../../agents/research_guardrails.py#L181) | 181 | `"    # remain case-insensitive (for example, \"I own\" versus \"i own\")."` | — |
| [SRC-3AA6165B18-L000182](../../agents/research_guardrails.py#L182) | 182 | `"    def has_term(terms: tuple[str, ...]) -> bool:"` | — |
| [SRC-3AA6165B18-L000183](../../agents/research_guardrails.py#L183) | 183 | `"        return any(_normalized(term) in text for term in terms)"` | — |
| [SRC-3AA6165B18-L000184](../../agents/research_guardrails.py#L184) | 184 | `"    if has_term(_PROMOTION_TERMS):"` | — |
| [SRC-3AA6165B18-L000185](../../agents/research_guardrails.py#L185) | 185 | `"        label = \"promotional_or_commercial\""` | — |
| [SRC-3AA6165B18-L000186](../../agents/research_guardrails.py#L186) | 186 | `"        basis = \"commercial language detected\""` | — |
| [SRC-3AA6165B18-L000187](../../agents/research_guardrails.py#L187) | 187 | `"    elif has_term(_PERSONAL_EXPERIENCE_TERMS):"` | — |
| [SRC-3AA6165B18-L000188](../../agents/research_guardrails.py#L188) | 188 | `"        label = \"personal_experience_candidate\""` | — |
| [SRC-3AA6165B18-L000189](../../agents/research_guardrails.py#L189) | 189 | `"        basis = \"first-person experience language detected\""` | — |
| [SRC-3AA6165B18-L000190](../../agents/research_guardrails.py#L190) | 190 | `"    elif has_term(_DISCUSSION_TERMS):"` | — |
| [SRC-3AA6165B18-L000191](../../agents/research_guardrails.py#L191) | 191 | `"        label = \"discussion_or_question\""` | — |
| [SRC-3AA6165B18-L000192](../../agents/research_guardrails.py#L192) | 192 | `"        basis = \"question or discussion language detected\""` | — |
| [SRC-3AA6165B18-L000193](../../agents/research_guardrails.py#L193) | 193 | `"    else:"` | — |
| [SRC-3AA6165B18-L000194](../../agents/research_guardrails.py#L194) | 194 | `"        label = \"social_post_unclassified\""` | — |
| [SRC-3AA6165B18-L000195](../../agents/research_guardrails.py#L195) | 195 | `"        basis = \"no clear experience/discussion signal; manual review needed\""` | — |
| [SRC-3AA6165B18-L000196](../../agents/research_guardrails.py#L196) | 196 | `"    return {"` | — |
| [SRC-3AA6165B18-L000197](../../agents/research_guardrails.py#L197) | 197 | `"        \"opinion_source_classification\": label,"` | — |
| [SRC-3AA6165B18-L000198](../../agents/research_guardrails.py#L198) | 198 | `"        \"opinion_classification_basis\": basis,"` | — |
| [SRC-3AA6165B18-L000199](../../agents/research_guardrails.py#L199) | 199 | `"        \"opinion_classification_method\": \"heuristic_only\","` | — |
| [SRC-3AA6165B18-L000200](../../agents/research_guardrails.py#L200) | 200 | `"    }"` | — |
| [SRC-3AA6165B18-L000201](../../agents/research_guardrails.py#L201) | 201 | `""` | — |
| [SRC-3AA6165B18-L000202](../../agents/research_guardrails.py#L202) | 202 | `""` | — |
| [SRC-3AA6165B18-L000203](../../agents/research_guardrails.py#L203) | 203 | `"def apply_source_guardrails("` | — |
| [SRC-3AA6165B18-L000204](../../agents/research_guardrails.py#L204) | 204 | `"    question: str,"` | — |
| [SRC-3AA6165B18-L000205](../../agents/research_guardrails.py#L205) | 205 | `"    mode: str,"` | — |
| [SRC-3AA6165B18-L000206](../../agents/research_guardrails.py#L206) | 206 | `"    plan: dict[str, Any],"` | — |
| [SRC-3AA6165B18-L000207](../../agents/research_guardrails.py#L207) | 207 | `"    sources: list[dict[str, Any]],"` | — |
| [SRC-3AA6165B18-L000208](../../agents/research_guardrails.py#L208) | 208 | `"    *,"` | — |
| [SRC-3AA6165B18-L000209](../../agents/research_guardrails.py#L209) | 209 | `"    now: datetime \| None = None,"` | — |
| [SRC-3AA6165B18-L000210](../../agents/research_guardrails.py#L210) | 210 | `") -> tuple[list[dict[str, Any]], dict[str, Any]]:"` | — |
| [SRC-3AA6165B18-L000211](../../agents/research_guardrails.py#L211) | 211 | `"    \"\"\"Apply official-domain, current-evidence, and explicit social-mode guards."` | — |
| [SRC-3AA6165B18-L000212](../../agents/research_guardrails.py#L212) | 212 | `""` | — |
| [SRC-3AA6165B18-L000213](../../agents/research_guardrails.py#L213) | 213 | `"    Rejection counters describe this filter stage only. They are not search-engine"` | — |
| [SRC-3AA6165B18-L000214](../../agents/research_guardrails.py#L214) | 214 | `"    totals, and passing them is not a semantic fact check."` | — |
| [SRC-3AA6165B18-L000215](../../agents/research_guardrails.py#L215) | 215 | `"    \"\"\""` | — |
| [SRC-3AA6165B18-L000216](../../agents/research_guardrails.py#L216) | 216 | `"    clean_mode = str(mode or \"auto\").strip().lower()"` | — |
| [SRC-3AA6165B18-L000217](../../agents/research_guardrails.py#L217) | 217 | `"    explicit_official_site_request = requires_official_government_domain(question)"` | — |
| [SRC-3AA6165B18-L000218](../../agents/research_guardrails.py#L218) | 218 | `"    current_government_hours_request = requires_official_current_government_source(question)"` | — |
| [SRC-3AA6165B18-L000219](../../agents/research_guardrails.py#L219) | 219 | `"    official_required = explicit_official_site_request or current_government_hours_request"` | — |
| [SRC-3AA6165B18-L000220](../../agents/research_guardrails.py#L220) | 220 | `"    # Latest mode always requires a recent read page. Auto mode also does so for"` | — |
| [SRC-3AA6165B18-L000221](../../agents/research_guardrails.py#L221) | 221 | `"    # explicitly current questions when the planner recognizes freshness, plus"` | — |
| [SRC-3AA6165B18-L000222](../../agents/research_guardrails.py#L222) | 222 | `"    # current government-service hours even if the planner misses that signal."` | — |
| [SRC-3AA6165B18-L000223](../../agents/research_guardrails.py#L223) | 223 | `"    explicit_current_request = detect_freshness(question)"` | — |
| [SRC-3AA6165B18-L000224](../../agents/research_guardrails.py#L224) | 224 | `"    freshness_required = ("` | — |
| [SRC-3AA6165B18-L000225](../../agents/research_guardrails.py#L225) | 225 | `"        ("` | — |
| [SRC-3AA6165B18-L000226](../../agents/research_guardrails.py#L226) | 226 | `"            clean_mode == \"latest\""` | — |
| [SRC-3AA6165B18-L000227](../../agents/research_guardrails.py#L227) | 227 | `"            or ("` | — |
| [SRC-3AA6165B18-L000228](../../agents/research_guardrails.py#L228) | 228 | `"                plan.get(\"freshness\") == \"current\""` | — |
| [SRC-3AA6165B18-L000229](../../agents/research_guardrails.py#L229) | 229 | `"                and explicit_current_request"` | — |
| [SRC-3AA6165B18-L000230](../../agents/research_guardrails.py#L230) | 230 | `"            )"` | — |
| [SRC-3AA6165B18-L000231](../../agents/research_guardrails.py#L231) | 231 | `"            or current_government_hours_request"` | — |
| [SRC-3AA6165B18-L000232](../../agents/research_guardrails.py#L232) | 232 | `"        )"` | — |
| [SRC-3AA6165B18-L000233](../../agents/research_guardrails.py#L233) | 233 | `"        and not _is_navigation_request(question)"` | — |
| [SRC-3AA6165B18-L000234](../../agents/research_guardrails.py#L234) | 234 | `"    )"` | — |
| [SRC-3AA6165B18-L000235](../../agents/research_guardrails.py#L235) | 235 | `"    social_required = clean_mode == \"social\""` | — |
| [SRC-3AA6165B18-L000236](../../agents/research_guardrails.py#L236) | 236 | `"    retained: list[dict[str, Any]] = []"` | — |
| [SRC-3AA6165B18-L000237](../../agents/research_guardrails.py#L237) | 237 | `"    rejected: dict[str, int] = {}"` | — |
| [SRC-3AA6165B18-L000238](../../agents/research_guardrails.py#L238) | 238 | `"    reasons: list[dict[str, str]] = []"` | — |
| [SRC-3AA6165B18-L000239](../../agents/research_guardrails.py#L239) | 239 | `""` | — |
| [SRC-3AA6165B18-L000240](../../agents/research_guardrails.py#L240) | 240 | `"    def reject(reason: str, source: dict[str, Any]) -> None:"` | — |
| [SRC-3AA6165B18-L000241](../../agents/research_guardrails.py#L241) | 241 | `"        rejected[reason] = rejected.get(reason, 0) + 1"` | — |
| [SRC-3AA6165B18-L000242](../../agents/research_guardrails.py#L242) | 242 | `"        reasons.append({"` | — |
| [SRC-3AA6165B18-L000243](../../agents/research_guardrails.py#L243) | 243 | `"            \"reason\": reason,"` | — |
| [SRC-3AA6165B18-L000244](../../agents/research_guardrails.py#L244) | 244 | `"            \"url\": str(source.get(\"url\") or \"\")[:2048],"` | — |
| [SRC-3AA6165B18-L000245](../../agents/research_guardrails.py#L245) | 245 | `"        })"` | — |
| [SRC-3AA6165B18-L000246](../../agents/research_guardrails.py#L246) | 246 | `""` | — |
| [SRC-3AA6165B18-L000247](../../agents/research_guardrails.py#L247) | 247 | `"    for candidate in (sources if isinstance(sources, list) else []):"` | — |
| [SRC-3AA6165B18-L000248](../../agents/research_guardrails.py#L248) | 248 | `"        if not isinstance(candidate, dict):"` | — |
| [SRC-3AA6165B18-L000249](../../agents/research_guardrails.py#L249) | 249 | `"            rejected[\"malformed_candidate\"] = rejected.get(\"malformed_candidate\", 0) + 1"` | — |
| [SRC-3AA6165B18-L000250](../../agents/research_guardrails.py#L250) | 250 | `"            reasons.append({\"reason\": \"malformed_candidate\", \"url\": \"\"})"` | — |
| [SRC-3AA6165B18-L000251](../../agents/research_guardrails.py#L251) | 251 | `"            continue"` | — |
| [SRC-3AA6165B18-L000252](../../agents/research_guardrails.py#L252) | 252 | `"        source = dict(candidate)"` | — |
| [SRC-3AA6165B18-L000253](../../agents/research_guardrails.py#L253) | 253 | `"        if official_required and not _is_government_domain(source.get(\"url\")):"` | — |
| [SRC-3AA6165B18-L000254](../../agents/research_guardrails.py#L254) | 254 | `"            reject(\"not_an_official_government_domain\", source)"` | — |
| [SRC-3AA6165B18-L000255](../../agents/research_guardrails.py#L255) | 255 | `"            continue"` | — |
| [SRC-3AA6165B18-L000256](../../agents/research_guardrails.py#L256) | 256 | `"        if social_required and not is_social_platform_url(source.get(\"url\")):"` | — |
| [SRC-3AA6165B18-L000257](../../agents/research_guardrails.py#L257) | 257 | `"            reject(\"not_a_social_platform_source\", source)"` | — |
| [SRC-3AA6165B18-L000258](../../agents/research_guardrails.py#L258) | 258 | `"            continue"` | — |
| [SRC-3AA6165B18-L000259](../../agents/research_guardrails.py#L259) | 259 | `"        if freshness_required:"` | — |
| [SRC-3AA6165B18-L000260](../../agents/research_guardrails.py#L260) | 260 | `"            freshness = assess_current_source(source, now=now)"` | — |
| [SRC-3AA6165B18-L000261](../../agents/research_guardrails.py#L261) | 261 | `"            source[\"current_evidence_assessment\"] = freshness"` | — |
| [SRC-3AA6165B18-L000262](../../agents/research_guardrails.py#L262) | 262 | `"            if not freshness[\"eligible\"]:"` | — |
| [SRC-3AA6165B18-L000263](../../agents/research_guardrails.py#L263) | 263 | `"                reject(str(freshness[\"status\"]), source)"` | — |
| [SRC-3AA6165B18-L000264](../../agents/research_guardrails.py#L264) | 264 | `"                continue"` | — |
| [SRC-3AA6165B18-L000265](../../agents/research_guardrails.py#L265) | 265 | `"        if social_required or bool(plan.get(\"social_focus\")):"` | — |
| [SRC-3AA6165B18-L000266](../../agents/research_guardrails.py#L266) | 266 | `"            source.update(classify_social_source(source))"` | — |
| [SRC-3AA6165B18-L000267](../../agents/research_guardrails.py#L267) | 267 | `"        retained.append(source)"` | — |
| [SRC-3AA6165B18-L000268](../../agents/research_guardrails.py#L268) | 268 | `""` | — |
| [SRC-3AA6165B18-L000269](../../agents/research_guardrails.py#L269) | 269 | `"    status = \"passed\" if not rejected else \"filtered\""` | — |
| [SRC-3AA6165B18-L000270](../../agents/research_guardrails.py#L270) | 270 | `"    if freshness_required and retained:"` | — |
| [SRC-3AA6165B18-L000271](../../agents/research_guardrails.py#L271) | 271 | `"        current_status = \"eligible_recent_read_pages_only\""` | — |
| [SRC-3AA6165B18-L000272](../../agents/research_guardrails.py#L272) | 272 | `"    elif freshness_required:"` | — |
| [SRC-3AA6165B18-L000273](../../agents/research_guardrails.py#L273) | 273 | `"        current_status = \"no_current_eligible_evidence\""` | — |
| [SRC-3AA6165B18-L000274](../../agents/research_guardrails.py#L274) | 274 | `"    else:"` | — |
| [SRC-3AA6165B18-L000275](../../agents/research_guardrails.py#L275) | 275 | `"        current_status = \"not_required\""` | — |
| [SRC-3AA6165B18-L000276](../../agents/research_guardrails.py#L276) | 276 | `"    summary = {"` | — |
| [SRC-3AA6165B18-L000277](../../agents/research_guardrails.py#L277) | 277 | `"        \"status\": status,"` | — |
| [SRC-3AA6165B18-L000278](../../agents/research_guardrails.py#L278) | 278 | `"        \"input_sources\": len(sources) if isinstance(sources, list) else 0,"` | — |
| [SRC-3AA6165B18-L000279](../../agents/research_guardrails.py#L279) | 279 | `"        \"accepted_sources\": len(retained),"` | — |
| [SRC-3AA6165B18-L000280](../../agents/research_guardrails.py#L280) | 280 | `"        \"rejected_sources\": sum(rejected.values()),"` | — |
| [SRC-3AA6165B18-L000281](../../agents/research_guardrails.py#L281) | 281 | `"        \"rejection_counts\": rejected,"` | — |
| [SRC-3AA6165B18-L000282](../../agents/research_guardrails.py#L282) | 282 | `"        \"rejection_details\": reasons[:20],"` | — |
| [SRC-3AA6165B18-L000283](../../agents/research_guardrails.py#L283) | 283 | `"        \"official_government_domain_required\": official_required,"` | — |
| [SRC-3AA6165B18-L000284](../../agents/research_guardrails.py#L284) | 284 | `"        \"official_government_domain_reason\": ("` | — |
| [SRC-3AA6165B18-L000285](../../agents/research_guardrails.py#L285) | 285 | `"            \"explicit_official_site_request\""` | — |
| [SRC-3AA6165B18-L000286](../../agents/research_guardrails.py#L286) | 286 | `"            if explicit_official_site_request"` | — |
| [SRC-3AA6165B18-L000287](../../agents/research_guardrails.py#L287) | 287 | `"            else \"current_government_service_hours\""` | — |
| [SRC-3AA6165B18-L000288](../../agents/research_guardrails.py#L288) | 288 | `"            if current_government_hours_request"` | — |
| [SRC-3AA6165B18-L000289](../../agents/research_guardrails.py#L289) | 289 | `"            else \"not_required\""` | — |
| [SRC-3AA6165B18-L000290](../../agents/research_guardrails.py#L290) | 290 | `"        ),"` | — |
| [SRC-3AA6165B18-L000291](../../agents/research_guardrails.py#L291) | 291 | `"        \"official_domain_policy\": ("` | — |
| [SRC-3AA6165B18-L000292](../../agents/research_guardrails.py#L292) | 292 | `"            \"government-domain candidate only; organization ownership is not independently verified\""` | — |
| [SRC-3AA6165B18-L000293](../../agents/research_guardrails.py#L293) | 293 | `"            if official_required else \"not_required\""` | — |
| [SRC-3AA6165B18-L000294](../../agents/research_guardrails.py#L294) | 294 | `"        ),"` | — |
| [SRC-3AA6165B18-L000295](../../agents/research_guardrails.py#L295) | 295 | `"        \"current_evidence_required\": freshness_required,"` | — |
| [SRC-3AA6165B18-L000296](../../agents/research_guardrails.py#L296) | 296 | `"        \"current_evidence_status\": current_status,"` | — |
| [SRC-3AA6165B18-L000297](../../agents/research_guardrails.py#L297) | 297 | `"        \"current_evidence_max_age_days\": _CURRENT_EVIDENCE_MAX_AGE_DAYS if freshness_required else None,"` | — |
| [SRC-3AA6165B18-L000298](../../agents/research_guardrails.py#L298) | 298 | `"        \"social_platform_only\": social_required,"` | — |
| [SRC-3AA6165B18-L000299](../../agents/research_guardrails.py#L299) | 299 | `"        \"interpretation\": \"retrieval guardrail only; passing is not proof of claim correctness\","` | — |
| [SRC-3AA6165B18-L000300](../../agents/research_guardrails.py#L300) | 300 | `"    }"` | — |
| [SRC-3AA6165B18-L000301](../../agents/research_guardrails.py#L301) | 301 | `"    return retained, summary"` | — |
## الوكيل والمنطق

### FILE-60066C6786 — [agents/research_pipeline.py](../../agents/research_pipeline.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-60066C6786-L000001](../../agents/research_pipeline.py#L1) | 1 | `"\"\"\"One bounded orchestration path for Omarai's hybrid research pipeline."` | — |
| [SRC-60066C6786-L000002](../../agents/research_pipeline.py#L2) | 2 | `""` | — |
| [SRC-60066C6786-L000003](../../agents/research_pipeline.py#L3) | 3 | `"The coordinator composes existing deterministic interpreters and the existing"` | — |
| [SRC-60066C6786-L000004](../../agents/research_pipeline.py#L4) | 4 | `"language-model planner output. Lexical evidence matching remains a candidate"` | — |
| [SRC-60066C6786-L000005](../../agents/research_pipeline.py#L5) | 5 | `"signal; semantic matching is explicitly unassessed unless a scorer is injected."` | — |
| [SRC-60066C6786-L000006](../../agents/research_pipeline.py#L6) | 6 | `"\"\"\""` | — |
| [SRC-60066C6786-L000007](../../agents/research_pipeline.py#L7) | 7 | `"from __future__ import annotations"` | — |
| [SRC-60066C6786-L000008](../../agents/research_pipeline.py#L8) | 8 | `""` | — |
| [SRC-60066C6786-L000009](../../agents/research_pipeline.py#L9) | 9 | `"from collections.abc import Callable"` | — |
| [SRC-60066C6786-L000010](../../agents/research_pipeline.py#L10) | 10 | `"import math"` | — |
| [SRC-60066C6786-L000011](../../agents/research_pipeline.py#L11) | 11 | `"from typing import Any"` | — |
| [SRC-60066C6786-L000012](../../agents/research_pipeline.py#L12) | 12 | `""` | — |
| [SRC-60066C6786-L000013](../../agents/research_pipeline.py#L13) | 13 | `"from agents.aspect_planning import build_evidence_ledger, extract_aspects"` | — |
| [SRC-60066C6786-L000014](../../agents/research_pipeline.py#L14) | 14 | `"from agents.intent_router import ROUTES, resolve_followup_query, route_intent"` | — |
| [SRC-60066C6786-L000015](../../agents/research_pipeline.py#L15) | 15 | `"from agents.task_understanding import ("` | — |
| [SRC-60066C6786-L000016](../../agents/research_pipeline.py#L16) | 16 | `"    MAX_TASK_ASPECTS,"` | — |
| [SRC-60066C6786-L000017](../../agents/research_pipeline.py#L17) | 17 | `"    build_query_strategy_matrix,"` | — |
| [SRC-60066C6786-L000018](../../agents/research_pipeline.py#L18) | 18 | `"    build_task_spec,"` | — |
| [SRC-60066C6786-L000019](../../agents/research_pipeline.py#L19) | 19 | `")"` | — |
| [SRC-60066C6786-L000020](../../agents/research_pipeline.py#L20) | 20 | `""` | — |
| [SRC-60066C6786-L000021](../../agents/research_pipeline.py#L21) | 21 | `"MAX_PIPELINE_QUESTION_CHARS = 4000"` | — |
| [SRC-60066C6786-L000022](../../agents/research_pipeline.py#L22) | 22 | `"MAX_PIPELINE_SOURCES = 18"` | — |
| [SRC-60066C6786-L000023](../../agents/research_pipeline.py#L23) | 23 | `""` | — |
| [SRC-60066C6786-L000024](../../agents/research_pipeline.py#L24) | 24 | `""` | — |
| [SRC-60066C6786-L000025](../../agents/research_pipeline.py#L25) | 25 | `"def _clean_aspects(task_spec: dict[str, Any], question: str) -> list[str]:"` | — |
| [SRC-60066C6786-L000026](../../agents/research_pipeline.py#L26) | 26 | `"    constraints = task_spec.get(\"constraints\")"` | — |
| [SRC-60066C6786-L000027](../../agents/research_pipeline.py#L27) | 27 | `"    declared = constraints.get(\"explicit_aspects\", []) if isinstance(constraints, dict) else []"` | — |
| [SRC-60066C6786-L000028](../../agents/research_pipeline.py#L28) | 28 | `"    extracted = extract_aspects(question)"` | — |
| [SRC-60066C6786-L000029](../../agents/research_pipeline.py#L29) | 29 | `"    aspects: list[str] = []"` | — |
| [SRC-60066C6786-L000030](../../agents/research_pipeline.py#L30) | 30 | `"    seen: set[str] = set()"` | — |
| [SRC-60066C6786-L000031](../../agents/research_pipeline.py#L31) | 31 | `"    for value in [*(declared if isinstance(declared, list) else []), *extracted]:"` | — |
| [SRC-60066C6786-L000032](../../agents/research_pipeline.py#L32) | 32 | `"        if not isinstance(value, str):"` | — |
| [SRC-60066C6786-L000033](../../agents/research_pipeline.py#L33) | 33 | `"            continue"` | — |
| [SRC-60066C6786-L000034](../../agents/research_pipeline.py#L34) | 34 | `"        item = \" \".join(value.split())[:120]"` | — |
| [SRC-60066C6786-L000035](../../agents/research_pipeline.py#L35) | 35 | `"        key = item.casefold()"` | — |
| [SRC-60066C6786-L000036](../../agents/research_pipeline.py#L36) | 36 | `"        if item and key not in seen:"` | — |
| [SRC-60066C6786-L000037](../../agents/research_pipeline.py#L37) | 37 | `"            seen.add(key)"` | — |
| [SRC-60066C6786-L000038](../../agents/research_pipeline.py#L38) | 38 | `"            aspects.append(item)"` | — |
| [SRC-60066C6786-L000039](../../agents/research_pipeline.py#L39) | 39 | `"        if len(aspects) >= MAX_TASK_ASPECTS:"` | — |
| [SRC-60066C6786-L000040](../../agents/research_pipeline.py#L40) | 40 | `"            break"` | — |
| [SRC-60066C6786-L000041](../../agents/research_pipeline.py#L41) | 41 | `"    return aspects"` | — |
| [SRC-60066C6786-L000042](../../agents/research_pipeline.py#L42) | 42 | `""` | — |
| [SRC-60066C6786-L000043](../../agents/research_pipeline.py#L43) | 43 | `""` | — |
| [SRC-60066C6786-L000044](../../agents/research_pipeline.py#L44) | 44 | `""` | — |
| [SRC-60066C6786-L000045](../../agents/research_pipeline.py#L45) | 45 | `"def _has_resolved_dialogue_context(dialogue_context: dict[str, Any] \| None) -> bool:"` | — |
| [SRC-60066C6786-L000046](../../agents/research_pipeline.py#L46) | 46 | `"    if not isinstance(dialogue_context, dict):"` | — |
| [SRC-60066C6786-L000047](../../agents/research_pipeline.py#L47) | 47 | `"        return False"` | — |
| [SRC-60066C6786-L000048](../../agents/research_pipeline.py#L48) | 48 | `"    resolved_question = dialogue_context.get(\"resolved_question\")"` | — |
| [SRC-60066C6786-L000049](../../agents/research_pipeline.py#L49) | 49 | `"    return bool("` | — |
| [SRC-60066C6786-L000050](../../agents/research_pipeline.py#L50) | 50 | `"        isinstance(resolved_question, str) and resolved_question.strip()"` | — |
| [SRC-60066C6786-L000051](../../agents/research_pipeline.py#L51) | 51 | `"    ) or dialogue_context.get(\"topic_shift\") is True or dialogue_context.get("` | — |
| [SRC-60066C6786-L000052](../../agents/research_pipeline.py#L52) | 52 | `"        \"needs_clarification\""` | — |
| [SRC-60066C6786-L000053](../../agents/research_pipeline.py#L53) | 53 | `"    ) is True"` | — |
| [SRC-60066C6786-L000054](../../agents/research_pipeline.py#L54) | 54 | `""` | — |
| [SRC-60066C6786-L000055](../../agents/research_pipeline.py#L55) | 55 | `""` | — |
| [SRC-60066C6786-L000056](../../agents/research_pipeline.py#L56) | 56 | `"def evaluate_research_evidence("` | — |
| [SRC-60066C6786-L000057](../../agents/research_pipeline.py#L57) | 57 | `"    aspects: list[str],"` | — |
| [SRC-60066C6786-L000058](../../agents/research_pipeline.py#L58) | 58 | `"    sources: list[dict[str, Any]] \| None,"` | — |
| [SRC-60066C6786-L000059](../../agents/research_pipeline.py#L59) | 59 | `"    *,"` | — |
| [SRC-60066C6786-L000060](../../agents/research_pipeline.py#L60) | 60 | `"    semantic_matcher: Callable[[str, dict[str, Any]], Any] \| None = None,"` | — |
| [SRC-60066C6786-L000061](../../agents/research_pipeline.py#L61) | 61 | `") -> dict[str, Any]:"` | — |
| [SRC-60066C6786-L000062](../../agents/research_pipeline.py#L62) | 62 | `"    \"\"\"Evaluate per-aspect candidates without equating relevance with claim truth.\"\"\""` | — |
| [SRC-60066C6786-L000063](../../agents/research_pipeline.py#L63) | 63 | `"    raw_aspects = aspects if isinstance(aspects, list) else []"` | — |
| [SRC-60066C6786-L000064](../../agents/research_pipeline.py#L64) | 64 | `"    safe_aspects = ["` | — |
| [SRC-60066C6786-L000065](../../agents/research_pipeline.py#L65) | 65 | `"        item[:120] for item in raw_aspects[:MAX_TASK_ASPECTS]"` | — |
| [SRC-60066C6786-L000066](../../agents/research_pipeline.py#L66) | 66 | `"        if isinstance(item, str) and item.strip()"` | — |
| [SRC-60066C6786-L000067](../../agents/research_pipeline.py#L67) | 67 | `"    ]"` | — |
| [SRC-60066C6786-L000068](../../agents/research_pipeline.py#L68) | 68 | `"    safe_sources = ["` | — |
| [SRC-60066C6786-L000069](../../agents/research_pipeline.py#L69) | 69 | `"        item for item in (sources or [])[:MAX_PIPELINE_SOURCES]"` | — |
| [SRC-60066C6786-L000070](../../agents/research_pipeline.py#L70) | 70 | `"        if isinstance(item, dict)"` | — |
| [SRC-60066C6786-L000071](../../agents/research_pipeline.py#L71) | 71 | `"    ]"` | — |
| [SRC-60066C6786-L000072](../../agents/research_pipeline.py#L72) | 72 | `"    lexical_ledger = build_evidence_ledger(safe_aspects, safe_sources)"` | — |
| [SRC-60066C6786-L000073](../../agents/research_pipeline.py#L73) | 73 | `"    lexical_matching_status = ("` | — |
| [SRC-60066C6786-L000074](../../agents/research_pipeline.py#L74) | 74 | `"        \"evaluated\""` | — |
| [SRC-60066C6786-L000075](../../agents/research_pipeline.py#L75) | 75 | `"        if safe_aspects"` | — |
| [SRC-60066C6786-L000076](../../agents/research_pipeline.py#L76) | 76 | `"        and any("` | — |
| [SRC-60066C6786-L000077](../../agents/research_pipeline.py#L77) | 77 | `"            any(str(source.get(field) or \"\").strip() for field in (\"title\", \"snippet\", \"page_text\"))"` | — |
| [SRC-60066C6786-L000078](../../agents/research_pipeline.py#L78) | 78 | `"            for source in safe_sources"` | — |
| [SRC-60066C6786-L000079](../../agents/research_pipeline.py#L79) | 79 | `"        )"` | — |
| [SRC-60066C6786-L000080](../../agents/research_pipeline.py#L80) | 80 | `"        else \"not_assessed\""` | — |
| [SRC-60066C6786-L000081](../../agents/research_pipeline.py#L81) | 81 | `"    )"` | — |
| [SRC-60066C6786-L000082](../../agents/research_pipeline.py#L82) | 82 | `"    semantic_status = \"not_configured\""` | — |
| [SRC-60066C6786-L000083](../../agents/research_pipeline.py#L83) | 83 | `"    semantic_candidates: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-60066C6786-L000084](../../agents/research_pipeline.py#L84) | 84 | `"    semantic_errors = 0"` | — |
| [SRC-60066C6786-L000085](../../agents/research_pipeline.py#L85) | 85 | `""` | — |
| [SRC-60066C6786-L000086](../../agents/research_pipeline.py#L86) | 86 | `"    if callable(semantic_matcher) and safe_aspects and safe_sources:"` | — |
| [SRC-60066C6786-L000087](../../agents/research_pipeline.py#L87) | 87 | `"        semantic_status = \"evaluated\""` | — |
| [SRC-60066C6786-L000088](../../agents/research_pipeline.py#L88) | 88 | `"        for aspect in safe_aspects:"` | — |
| [SRC-60066C6786-L000089](../../agents/research_pipeline.py#L89) | 89 | `"            ranked: list[dict[str, Any]] = []"` | — |
| [SRC-60066C6786-L000090](../../agents/research_pipeline.py#L90) | 90 | `"            for source_index, source in enumerate(safe_sources):"` | — |
| [SRC-60066C6786-L000091](../../agents/research_pipeline.py#L91) | 91 | `"                try:"` | — |
| [SRC-60066C6786-L000092](../../agents/research_pipeline.py#L92) | 92 | `"                    raw_score = semantic_matcher(aspect, source)"` | — |
| [SRC-60066C6786-L000093](../../agents/research_pipeline.py#L93) | 93 | `"                    if isinstance(raw_score, bool):"` | — |
| [SRC-60066C6786-L000094](../../agents/research_pipeline.py#L94) | 94 | `"                        continue"` | — |
| [SRC-60066C6786-L000095](../../agents/research_pipeline.py#L95) | 95 | `"                    score = float(raw_score)"` | — |
| [SRC-60066C6786-L000096](../../agents/research_pipeline.py#L96) | 96 | `"                except Exception:"` | — |
| [SRC-60066C6786-L000097](../../agents/research_pipeline.py#L97) | 97 | `"                    semantic_errors += 1"` | — |
| [SRC-60066C6786-L000098](../../agents/research_pipeline.py#L98) | 98 | `"                    continue"` | — |
| [SRC-60066C6786-L000099](../../agents/research_pipeline.py#L99) | 99 | `"                if not math.isfinite(score) or not 0.0 <= score <= 1.0:"` | — |
| [SRC-60066C6786-L000100](../../agents/research_pipeline.py#L100) | 100 | `"                    continue"` | — |
| [SRC-60066C6786-L000101](../../agents/research_pipeline.py#L101) | 101 | `"                ranked.append({"` | — |
| [SRC-60066C6786-L000102](../../agents/research_pipeline.py#L102) | 102 | `"                    \"source_index\": source_index,"` | — |
| [SRC-60066C6786-L000103](../../agents/research_pipeline.py#L103) | 103 | `"                    \"score\": round(score, 4),"` | — |
| [SRC-60066C6786-L000104](../../agents/research_pipeline.py#L104) | 104 | `"                })"` | — |
| [SRC-60066C6786-L000105](../../agents/research_pipeline.py#L105) | 105 | `"            semantic_candidates[aspect] = sorted("` | — |
| [SRC-60066C6786-L000106](../../agents/research_pipeline.py#L106) | 106 | `"                ranked, key=lambda item: item[\"score\"], reverse=True"` | — |
| [SRC-60066C6786-L000107](../../agents/research_pipeline.py#L107) | 107 | `"            )[:5]"` | — |
| [SRC-60066C6786-L000108](../../agents/research_pipeline.py#L108) | 108 | `""` | — |
| [SRC-60066C6786-L000109](../../agents/research_pipeline.py#L109) | 109 | `"    return {"` | — |
| [SRC-60066C6786-L000110](../../agents/research_pipeline.py#L110) | 110 | `"        \"lexical_ledger\": lexical_ledger,"` | — |
| [SRC-60066C6786-L000111](../../agents/research_pipeline.py#L111) | 111 | `"        \"lexical_matching_status\": lexical_matching_status,"` | — |
| [SRC-60066C6786-L000112](../../agents/research_pipeline.py#L112) | 112 | `"        \"semantic_matching\": {"` | — |
| [SRC-60066C6786-L000113](../../agents/research_pipeline.py#L113) | 113 | `"            \"status\": \"degraded\" if semantic_errors else semantic_status,"` | — |
| [SRC-60066C6786-L000114](../../agents/research_pipeline.py#L114) | 114 | `"            \"errors\": semantic_errors,"` | — |
| [SRC-60066C6786-L000115](../../agents/research_pipeline.py#L115) | 115 | `"            \"candidates\": semantic_candidates,"` | — |
| [SRC-60066C6786-L000116](../../agents/research_pipeline.py#L116) | 116 | `"            \"meaning\": ("` | — |
| [SRC-60066C6786-L000117](../../agents/research_pipeline.py#L117) | 117 | `"                \"ترتيب مرشحات الصلة فقط؛ لا يثبت صحة الادعاءات أو كفاية الاستشهاد.\""` | — |
| [SRC-60066C6786-L000118](../../agents/research_pipeline.py#L118) | 118 | `"            ),"` | — |
| [SRC-60066C6786-L000119](../../agents/research_pipeline.py#L119) | 119 | `"        },"` | — |
| [SRC-60066C6786-L000120](../../agents/research_pipeline.py#L120) | 120 | `"        \"claim_verification\": \"delegated_to_existing_validator\","` | — |
| [SRC-60066C6786-L000121](../../agents/research_pipeline.py#L121) | 121 | `"    }"` | — |
| [SRC-60066C6786-L000122](../../agents/research_pipeline.py#L122) | 122 | `""` | — |
| [SRC-60066C6786-L000123](../../agents/research_pipeline.py#L123) | 123 | `""` | — |
| [SRC-60066C6786-L000124](../../agents/research_pipeline.py#L124) | 124 | `"def build_research_pipeline("` | — |
| [SRC-60066C6786-L000125](../../agents/research_pipeline.py#L125) | 125 | `"    question: str,"` | — |
| [SRC-60066C6786-L000126](../../agents/research_pipeline.py#L126) | 126 | `"    plan: dict[str, Any] \| None = None,"` | — |
| [SRC-60066C6786-L000127](../../agents/research_pipeline.py#L127) | 127 | `"    *,"` | — |
| [SRC-60066C6786-L000128](../../agents/research_pipeline.py#L128) | 128 | `"    history: list[dict[str, str]] \| None = None,"` | — |
| [SRC-60066C6786-L000129](../../agents/research_pipeline.py#L129) | 129 | `"    mode: str = \"auto\","` | — |
| [SRC-60066C6786-L000130](../../agents/research_pipeline.py#L130) | 130 | `"    intent_route: str = \"\","` | — |
| [SRC-60066C6786-L000131](../../agents/research_pipeline.py#L131) | 131 | `"    dialogue_context: dict[str, Any] \| None = None,"` | — |
| [SRC-60066C6786-L000132](../../agents/research_pipeline.py#L132) | 132 | `"    sources: list[dict[str, Any]] \| None = None,"` | — |
| [SRC-60066C6786-L000133](../../agents/research_pipeline.py#L133) | 133 | `"    compact_fn: Callable[[str], str] \| None = None,"` | — |
| [SRC-60066C6786-L000134](../../agents/research_pipeline.py#L134) | 134 | `"    semantic_matcher: Callable[[str, dict[str, Any]], Any] \| None = None,"` | — |
| [SRC-60066C6786-L000135](../../agents/research_pipeline.py#L135) | 135 | `") -> dict[str, Any]:"` | — |
| [SRC-60066C6786-L000136](../../agents/research_pipeline.py#L136) | 136 | `"    \"\"\"Run context→intent→task→aspects→queries→evidence as one auditable pipeline.\"\"\""` | — |
| [SRC-60066C6786-L000137](../../agents/research_pipeline.py#L137) | 137 | `"    raw_question = question[:MAX_PIPELINE_QUESTION_CHARS] if isinstance(question, str) else \"\""` | — |
| [SRC-60066C6786-L000138](../../agents/research_pipeline.py#L138) | 138 | `"    supplied_context = dialogue_context if isinstance(dialogue_context, dict) else {}"` | — |
| [SRC-60066C6786-L000139](../../agents/research_pipeline.py#L139) | 139 | `"    resolved_question = supplied_context.get(\"resolved_question\")"` | — |
| [SRC-60066C6786-L000140](../../agents/research_pipeline.py#L140) | 140 | `"    contextual_question = ("` | — |
| [SRC-60066C6786-L000141](../../agents/research_pipeline.py#L141) | 141 | `"        raw_question"` | — |
| [SRC-60066C6786-L000142](../../agents/research_pipeline.py#L142) | 142 | `"        if supplied_context.get(\"topic_shift\") is True"` | — |
| [SRC-60066C6786-L000143](../../agents/research_pipeline.py#L143) | 143 | `"        else str(resolved_question)[:MAX_PIPELINE_QUESTION_CHARS].strip()"` | — |
| [SRC-60066C6786-L000144](../../agents/research_pipeline.py#L144) | 144 | `"        if isinstance(resolved_question, str) and resolved_question.strip()"` | — |
| [SRC-60066C6786-L000145](../../agents/research_pipeline.py#L145) | 145 | `"        else resolve_followup_query(raw_question, history)"` | — |
| [SRC-60066C6786-L000146](../../agents/research_pipeline.py#L146) | 146 | `"        if history and raw_question.strip()"` | — |
| [SRC-60066C6786-L000147](../../agents/research_pipeline.py#L147) | 147 | `"        else raw_question"` | — |
| [SRC-60066C6786-L000148](../../agents/research_pipeline.py#L148) | 148 | `"    )"` | — |
| [SRC-60066C6786-L000149](../../agents/research_pipeline.py#L149) | 149 | `"    supplied_route = intent_route if isinstance(intent_route, str) else \"\""` | — |
| [SRC-60066C6786-L000150](../../agents/research_pipeline.py#L150) | 150 | `"    intent = ("` | — |
| [SRC-60066C6786-L000151](../../agents/research_pipeline.py#L151) | 151 | `"        {"` | — |
| [SRC-60066C6786-L000152](../../agents/research_pipeline.py#L152) | 152 | `"            \"route\": supplied_route,"` | — |
| [SRC-60066C6786-L000153](../../agents/research_pipeline.py#L153) | 153 | `"            \"reason\": \"upstream_route\","` | — |
| [SRC-60066C6786-L000154](../../agents/research_pipeline.py#L154) | 154 | `"            \"context_available\": bool(history) or _has_resolved_dialogue_context(dialogue_context),"` | — |
| [SRC-60066C6786-L000155](../../agents/research_pipeline.py#L155) | 155 | `"            \"needs_clarification\": supplied_route == \"CLARIFY\","` | — |
| [SRC-60066C6786-L000156](../../agents/research_pipeline.py#L156) | 156 | `"        }"` | — |
| [SRC-60066C6786-L000157](../../agents/research_pipeline.py#L157) | 157 | `"        if supplied_route in ROUTES"` | — |
| [SRC-60066C6786-L000158](../../agents/research_pipeline.py#L158) | 158 | `"        else route_intent(contextual_question, history, mode=mode)"` | — |
| [SRC-60066C6786-L000159](../../agents/research_pipeline.py#L159) | 159 | `"    )"` | — |
| [SRC-60066C6786-L000160](../../agents/research_pipeline.py#L160) | 160 | `"    route = intent.get(\"route\", \"CLARIFY\")"` | — |
| [SRC-60066C6786-L000161](../../agents/research_pipeline.py#L161) | 161 | `"    safe_plan = dict(plan) if isinstance(plan, dict) else {}"` | — |
| [SRC-60066C6786-L000162](../../agents/research_pipeline.py#L162) | 162 | `"    task_spec = build_task_spec("` | — |
| [SRC-60066C6786-L000163](../../agents/research_pipeline.py#L163) | 163 | `"        contextual_question,"` | — |
| [SRC-60066C6786-L000164](../../agents/research_pipeline.py#L164) | 164 | `"        mode=mode,"` | — |
| [SRC-60066C6786-L000165](../../agents/research_pipeline.py#L165) | 165 | `"        intent_route=route,"` | — |
| [SRC-60066C6786-L000166](../../agents/research_pipeline.py#L166) | 166 | `"        plan=safe_plan,"` | — |
| [SRC-60066C6786-L000167](../../agents/research_pipeline.py#L167) | 167 | `"        dialogue_context=dialogue_context if isinstance(dialogue_context, dict) else None,"` | — |
| [SRC-60066C6786-L000168](../../agents/research_pipeline.py#L168) | 168 | `"    )"` | — |
| [SRC-60066C6786-L000169](../../agents/research_pipeline.py#L169) | 169 | `"    aspects = _clean_aspects(task_spec, contextual_question)"` | — |
| [SRC-60066C6786-L000170](../../agents/research_pipeline.py#L170) | 170 | `"    task_requires_clarification = bool(task_spec.get(\"requires_clarification\"))"` | — |
| [SRC-60066C6786-L000171](../../agents/research_pipeline.py#L171) | 171 | `"    if task_requires_clarification and not intent.get(\"needs_clarification\"):"` | — |
| [SRC-60066C6786-L000172](../../agents/research_pipeline.py#L172) | 172 | `"        intent = dict(intent)"` | — |
| [SRC-60066C6786-L000173](../../agents/research_pipeline.py#L173) | 173 | `"        intent[\"needs_clarification\"] = True"` | — |
| [SRC-60066C6786-L000174](../../agents/research_pipeline.py#L174) | 174 | `"        intent[\"reason\"] = \"task_spec_missing_required_input\""` | — |
| [SRC-60066C6786-L000175](../../agents/research_pipeline.py#L175) | 175 | `""` | — |
| [SRC-60066C6786-L000176](../../agents/research_pipeline.py#L176) | 176 | `"    if route == \"CLARIFY\" or intent.get(\"needs_clarification\") or task_requires_clarification:"` | — |
| [SRC-60066C6786-L000177](../../agents/research_pipeline.py#L177) | 177 | `"        strategy_matrix: list[dict[str, str]] = []"` | — |
| [SRC-60066C6786-L000178](../../agents/research_pipeline.py#L178) | 178 | `"        queries: list[str] = []"` | — |
| [SRC-60066C6786-L000179](../../agents/research_pipeline.py#L179) | 179 | `"        query_status = \"blocked_pending_clarification\""` | — |
| [SRC-60066C6786-L000180](../../agents/research_pipeline.py#L180) | 180 | `"    else:"` | — |
| [SRC-60066C6786-L000181](../../agents/research_pipeline.py#L181) | 181 | `"        strategy_matrix = build_query_strategy_matrix("` | — |
| [SRC-60066C6786-L000182](../../agents/research_pipeline.py#L182) | 182 | `"            contextual_question,"` | — |
| [SRC-60066C6786-L000183](../../agents/research_pipeline.py#L183) | 183 | `"            task_spec,"` | — |
| [SRC-60066C6786-L000184](../../agents/research_pipeline.py#L184) | 184 | `"            safe_plan.get(\"queries\", []),"` | — |
| [SRC-60066C6786-L000185](../../agents/research_pipeline.py#L185) | 185 | `"            limit=8,"` | — |
| [SRC-60066C6786-L000186](../../agents/research_pipeline.py#L186) | 186 | `"            compact_fn=compact_fn,"` | — |
