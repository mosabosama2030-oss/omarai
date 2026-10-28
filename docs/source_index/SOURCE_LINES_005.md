# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **005**
- سجلات الأسطر: **800**
- النطاق: SRC-1E32639872-L000002 إلى SRC-1AE03B9EC3-L000027
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1E32639872 — [agents/research_completion.py](../../agents/research_completion.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1E32639872-L000002](../../agents/research_completion.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-1E32639872-L000003](../../agents/research_completion.py#L3) | 3 | `""` | — |
| [SRC-1E32639872-L000004](../../agents/research_completion.py#L4) | 4 | `"from typing import Any"` | — |
| [SRC-1E32639872-L000005](../../agents/research_completion.py#L5) | 5 | `"from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit"` | — |
| [SRC-1E32639872-L000006](../../agents/research_completion.py#L6) | 6 | `""` | — |
| [SRC-1E32639872-L000007](../../agents/research_completion.py#L7) | 7 | `"from agents.research import registrable_domain"` | — |
| [SRC-1E32639872-L000008](../../agents/research_completion.py#L8) | 8 | `""` | — |
| [SRC-1E32639872-L000009](../../agents/research_completion.py#L9) | 9 | `"_RESEARCH_KINDS = frozenset({"` | — |
| [SRC-1E32639872-L000010](../../agents/research_completion.py#L10) | 10 | `"    \"web_research\", \"web_fallback\", \"insufficient_evidence\","` | — |
| [SRC-1E32639872-L000011](../../agents/research_completion.py#L11) | 11 | `"    \"lead_discovery_no_qualified_candidates\","` | — |
| [SRC-1E32639872-L000012](../../agents/research_completion.py#L12) | 12 | `"})"` | — |
| [SRC-1E32639872-L000013](../../agents/research_completion.py#L13) | 13 | `"_RESEARCH_ERRORS = frozenset({"` | — |
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
| [SRC-1E32639872-L000170](../../agents/research_completion.py#L170) | 170 | `"    fulfillment = str("` | — |
| [SRC-1E32639872-L000171](../../agents/research_completion.py#L171) | 171 | `"        result.get(\"task_fulfillment_status\") or report.get(\"task_fulfillment_status\") or \"\""` | — |
| [SRC-1E32639872-L000172](../../agents/research_completion.py#L172) | 172 | `"    )"` | — |
| [SRC-1E32639872-L000173](../../agents/research_completion.py#L173) | 173 | `"    citations = _dict(result.get(\"citation_validation\") or result.get(\"citation_check\"))"` | — |
| [SRC-1E32639872-L000174](../../agents/research_completion.py#L174) | 174 | `"    citation_count = _int(citations.get(\"valid_citation_count\")) or 0"` | — |
| [SRC-1E32639872-L000175](../../agents/research_completion.py#L175) | 175 | `"    generation_failed = any("` | — |
| [SRC-1E32639872-L000176](../../agents/research_completion.py#L176) | 176 | `"        token in final_status for token in (\"failed\", \"unavailable\", \"budget_exhausted\")"` | — |
| [SRC-1E32639872-L000177](../../agents/research_completion.py#L177) | 177 | `"    )"` | — |
| [SRC-1E32639872-L000178](../../agents/research_completion.py#L178) | 178 | `""` | — |
| [SRC-1E32639872-L000179](../../agents/research_completion.py#L179) | 179 | `"    if exhausted:"` | — |
| [SRC-1E32639872-L000180](../../agents/research_completion.py#L180) | 180 | `"        status = \"execution_stopped_budget\""` | — |
| [SRC-1E32639872-L000181](../../agents/research_completion.py#L181) | 181 | `"    elif not sources:"` | — |
| [SRC-1E32639872-L000182](../../agents/research_completion.py#L182) | 182 | `"        if rejected:"` | — |
| [SRC-1E32639872-L000183](../../agents/research_completion.py#L183) | 183 | `"            status = \"no_eligible_sources_after_filtering\""` | — |
| [SRC-1E32639872-L000184](../../agents/research_completion.py#L184) | 184 | `"        elif str(report.get(\"search_outcome\") or \"\") in _RESEARCH_ERRORS or ("` | — |
| [SRC-1E32639872-L000185](../../agents/research_completion.py#L185) | 185 | `"            connector_errors and not connector_ok"` | — |
| [SRC-1E32639872-L000186](../../agents/research_completion.py#L186) | 186 | `"        ):"` | — |
| [SRC-1E32639872-L000187](../../agents/research_completion.py#L187) | 187 | `"            status = \"search_failed_or_incomplete\""` | — |
| [SRC-1E32639872-L000188](../../agents/research_completion.py#L188) | 188 | `"        elif zero_results:"` | — |
| [SRC-1E32639872-L000189](../../agents/research_completion.py#L189) | 189 | `"            status = \"no_results_returned\""` | — |
| [SRC-1E32639872-L000190](../../agents/research_completion.py#L190) | 190 | `"        elif attempted is False:"` | — |
| [SRC-1E32639872-L000191](../../agents/research_completion.py#L191) | 191 | `"            status = \"search_not_attempted\""` | — |
| [SRC-1E32639872-L000192](../../agents/research_completion.py#L192) | 192 | `"        else:"` | — |
| [SRC-1E32639872-L000193](../../agents/research_completion.py#L193) | 193 | `"            status = \"insufficient_evidence\""` | — |
| [SRC-1E32639872-L000194](../../agents/research_completion.py#L194) | 194 | `"    elif not model_used:"` | — |
| [SRC-1E32639872-L000195](../../agents/research_completion.py#L195) | 195 | `"        status = ("` | — |
| [SRC-1E32639872-L000196](../../agents/research_completion.py#L196) | 196 | `"            \"source_snippets_only_generation_not_completed\""` | — |
| [SRC-1E32639872-L000197](../../agents/research_completion.py#L197) | 197 | `"            if read == 0 else \"evidence_collected_generation_not_completed\""` | — |
| [SRC-1E32639872-L000198](../../agents/research_completion.py#L198) | 198 | `"        )"` | — |
| [SRC-1E32639872-L000199](../../agents/research_completion.py#L199) | 199 | `"    elif generation_failed:"` | — |
| [SRC-1E32639872-L000200](../../agents/research_completion.py#L200) | 200 | `"        status = \"answer_generation_or_review_failed\""` | — |
| [SRC-1E32639872-L000201](../../agents/research_completion.py#L201) | 201 | `"    elif gap_count or fulfillment in {"` | — |
| [SRC-1E32639872-L000202](../../agents/research_completion.py#L202) | 202 | `"        \"possible_gap_detected\", \"source_evidence_gap_unresolved\","` | — |
| [SRC-1E32639872-L000203](../../agents/research_completion.py#L203) | 203 | `"        \"not_assessed_insufficient_evidence\","` | — |
| [SRC-1E32639872-L000204](../../agents/research_completion.py#L204) | 204 | `"    }:"` | — |
| [SRC-1E32639872-L000205](../../agents/research_completion.py#L205) | 205 | `"        status = \"partial_answer_evidence_gaps_detected\""` | — |
| [SRC-1E32639872-L000206](../../agents/research_completion.py#L206) | 206 | `"    elif citation_count:"` | — |
| [SRC-1E32639872-L000207](../../agents/research_completion.py#L207) | 207 | `"        status = \"answer_generated_citations_range_checked_semantic_support_unverified\""` | — |
| [SRC-1E32639872-L000208](../../agents/research_completion.py#L208) | 208 | `"    else:"` | — |
| [SRC-1E32639872-L000209](../../agents/research_completion.py#L209) | 209 | `"        status = \"answer_generated_without_valid_citation_markers\""` | — |
| [SRC-1E32639872-L000210](../../agents/research_completion.py#L210) | 210 | `""` | — |
| [SRC-1E32639872-L000211](../../agents/research_completion.py#L211) | 211 | `"    if attempted is False:"` | — |
| [SRC-1E32639872-L000212](../../agents/research_completion.py#L212) | 212 | `"        search_phase = \"not_attempted\""` | — |
| [SRC-1E32639872-L000213](../../agents/research_completion.py#L213) | 213 | `"    elif attempted is None:"` | — |
| [SRC-1E32639872-L000214](../../agents/research_completion.py#L214) | 214 | `"        search_phase = \"unknown\""` | — |
| [SRC-1E32639872-L000215](../../agents/research_completion.py#L215) | 215 | `"    elif connector_errors and not connector_ok and not sources:"` | — |
| [SRC-1E32639872-L000216](../../agents/research_completion.py#L216) | 216 | `"        search_phase = \"failed_or_incomplete\""` | — |
| [SRC-1E32639872-L000217](../../agents/research_completion.py#L217) | 217 | `"    elif sources:"` | — |
| [SRC-1E32639872-L000218](../../agents/research_completion.py#L218) | 218 | `"        search_phase = \"results_received\""` | — |
| [SRC-1E32639872-L000219](../../agents/research_completion.py#L219) | 219 | `"    elif zero_results:"` | — |
| [SRC-1E32639872-L000220](../../agents/research_completion.py#L220) | 220 | `"        search_phase = \"completed_no_results\""` | — |
| [SRC-1E32639872-L000221](../../agents/research_completion.py#L221) | 221 | `"    else:"` | — |
| [SRC-1E32639872-L000222](../../agents/research_completion.py#L222) | 222 | `"        search_phase = \"attempted_no_usable_sources\""` | — |
| [SRC-1E32639872-L000223](../../agents/research_completion.py#L223) | 223 | `""` | — |
| [SRC-1E32639872-L000224](../../agents/research_completion.py#L224) | 224 | `"    if not sources:"` | — |
| [SRC-1E32639872-L000225](../../agents/research_completion.py#L225) | 225 | `"        read_phase = \"not_applicable_no_eligible_sources\""` | — |
| [SRC-1E32639872-L000226](../../agents/research_completion.py#L226) | 226 | `"    elif read == len(sources):"` | — |
| [SRC-1E32639872-L000227](../../agents/research_completion.py#L227) | 227 | `"        read_phase = \"all_final_sources_read\""` | — |
| [SRC-1E32639872-L000228](../../agents/research_completion.py#L228) | 228 | `"    elif read:"` | — |
| [SRC-1E32639872-L000229](../../agents/research_completion.py#L229) | 229 | `"        read_phase = \"some_final_sources_read\""` | — |
| [SRC-1E32639872-L000230](../../agents/research_completion.py#L230) | 230 | `"    else:"` | — |
| [SRC-1E32639872-L000231](../../agents/research_completion.py#L231) | 231 | `"        read_phase = \"no_final_source_page_read\""` | — |
| [SRC-1E32639872-L000232](../../agents/research_completion.py#L232) | 232 | `""` | — |
| [SRC-1E32639872-L000233](../../agents/research_completion.py#L233) | 233 | `"    if kind == \"insufficient_evidence\" or not sources:"` | — |
| [SRC-1E32639872-L000234](../../agents/research_completion.py#L234) | 234 | `"        generation_phase = \"not_attempted_or_withheld\""` | — |
| [SRC-1E32639872-L000235](../../agents/research_completion.py#L235) | 235 | `"    elif model_used and not generation_failed:"` | — |
| [SRC-1E32639872-L000236](../../agents/research_completion.py#L236) | 236 | `"        generation_phase = \"answer_generated\""` | — |
| [SRC-1E32639872-L000237](../../agents/research_completion.py#L237) | 237 | `"    elif model_used:"` | — |
| [SRC-1E32639872-L000238](../../agents/research_completion.py#L238) | 238 | `"        generation_phase = \"failed_or_unavailable\""` | — |
| [SRC-1E32639872-L000239](../../agents/research_completion.py#L239) | 239 | `"    else:"` | — |
| [SRC-1E32639872-L000240](../../agents/research_completion.py#L240) | 240 | `"        generation_phase = \"not_completed\""` | — |
| [SRC-1E32639872-L000241](../../agents/research_completion.py#L241) | 241 | `""` | — |
| [SRC-1E32639872-L000242](../../agents/research_completion.py#L242) | 242 | `"    return {"` | — |
| [SRC-1E32639872-L000243](../../agents/research_completion.py#L243) | 243 | `"        \"status\": status,"` | — |
| [SRC-1E32639872-L000244](../../agents/research_completion.py#L244) | 244 | `"        \"status_semantics\": \"pipeline_state_not_probability_of_factual_correctness\","` | — |
| [SRC-1E32639872-L000245](../../agents/research_completion.py#L245) | 245 | `"        \"phases\": {"` | — |
| [SRC-1E32639872-L000246](../../agents/research_completion.py#L246) | 246 | `"            \"planning\": \"completed\" if isinstance(result.get(\"research_plan\"), dict) else \"unknown\","` | — |
| [SRC-1E32639872-L000247](../../agents/research_completion.py#L247) | 247 | `"            \"search\": search_phase,"` | — |
| [SRC-1E32639872-L000248](../../agents/research_completion.py#L248) | 248 | `"            \"source_filtering\": ("` | — |
| [SRC-1E32639872-L000249](../../agents/research_completion.py#L249) | 249 | `"                \"sources_retained\" if sources else"` | — |
| [SRC-1E32639872-L000250](../../agents/research_completion.py#L250) | 250 | `"                \"rejected_all_candidates\" if rejected else \"no_eligible_sources\""` | — |
| [SRC-1E32639872-L000251](../../agents/research_completion.py#L251) | 251 | `"            ),"` | — |
| [SRC-1E32639872-L000252](../../agents/research_completion.py#L252) | 252 | `"            \"page_reading\": read_phase,"` | — |
| [SRC-1E32639872-L000253](../../agents/research_completion.py#L253) | 253 | `"            \"answer_generation\": generation_phase,"` | — |
| [SRC-1E32639872-L000254](../../agents/research_completion.py#L254) | 254 | `"            \"citation_validation\": str(citations.get(\"status\") or \"not_run\"),"` | — |
| [SRC-1E32639872-L000255](../../agents/research_completion.py#L255) | 255 | `"            \"semantic_verification\": \"not_performed\","` | — |
| [SRC-1E32639872-L000256](../../agents/research_completion.py#L256) | 256 | `"        },"` | — |
| [SRC-1E32639872-L000257](../../agents/research_completion.py#L257) | 257 | `"        \"counters\": {"` | — |
| [SRC-1E32639872-L000258](../../agents/research_completion.py#L258) | 258 | `"            \"queries_planned\": _int(report.get(\"queries_planned\")),"` | — |
| [SRC-1E32639872-L000259](../../agents/research_completion.py#L259) | 259 | `"            \"queries_attempted\": _int(report.get(\"queries_attempted\")),"` | — |
| [SRC-1E32639872-L000260](../../agents/research_completion.py#L260) | 260 | `"            \"per_query_result_count_sum\": query_total,"` | — |
| [SRC-1E32639872-L000261](../../agents/research_completion.py#L261) | 261 | `"            \"per_query_result_count_sum_semantics\": \"sum_of_reported_per_query_counts_not_deduplicated_sources\","` | — |
| [SRC-1E32639872-L000262](../../agents/research_completion.py#L262) | 262 | `"            \"query_result_row_count\": len(query_rows),"` | — |
| [SRC-1E32639872-L000263](../../agents/research_completion.py#L263) | 263 | `"            \"query_result_rows_with_counts\": sum("` | — |
| [SRC-1E32639872-L000264](../../agents/research_completion.py#L264) | 264 | `"                isinstance(row, dict) and _int(row.get(\"results\")) is not None"` | — |
| [SRC-1E32639872-L000265](../../agents/research_completion.py#L265) | 265 | `"                for row in query_rows"` | — |
| [SRC-1E32639872-L000266](../../agents/research_completion.py#L266) | 266 | `"            ),"` | — |
| [SRC-1E32639872-L000267](../../agents/research_completion.py#L267) | 267 | `"            \"final_source_list_count\": len(sources),"` | — |
| [SRC-1E32639872-L000268](../../agents/research_completion.py#L268) | 268 | `"            \"unique_normalized_url_count\": len(unique_urls),"` | — |
| [SRC-1E32639872-L000269](../../agents/research_completion.py#L269) | 269 | `"            \"duplicate_normalized_url_count\": max(0, len(url_keys) - len(unique_urls)),"` | — |
| [SRC-1E32639872-L000270](../../agents/research_completion.py#L270) | 270 | `"            \"distinct_registrable_domain_count\": len(domains),"` | — |
| [SRC-1E32639872-L000271](../../agents/research_completion.py#L271) | 271 | `"            \"pages_fetched_flag_count\": fetched,"` | — |
| [SRC-1E32639872-L000272](../../agents/research_completion.py#L272) | 272 | `"            \"pages_read_with_text_count\": read,"` | — |
| [SRC-1E32639872-L000273](../../agents/research_completion.py#L273) | 273 | `"            \"snippet_only_source_count\": snippet_only,"` | — |
| [SRC-1E32639872-L000274](../../agents/research_completion.py#L274) | 274 | `"            \"page_text_without_fetched_flag_count\": unflagged_text,"` | — |
| [SRC-1E32639872-L000275](../../agents/research_completion.py#L275) | 275 | `"            \"connector_status_counts\": connector_counts,"` | — |
| [SRC-1E32639872-L000276](../../agents/research_completion.py#L276) | 276 | `"            \"connector_failure_count\": connector_errors,"` | — |
| [SRC-1E32639872-L000277](../../agents/research_completion.py#L277) | 277 | `"            \"connector_success_count\": connector_ok,"` | — |
| [SRC-1E32639872-L000278](../../agents/research_completion.py#L278) | 278 | `"            \"guardrail_rejected_candidate_count\": rejected,"` | — |
| [SRC-1E32639872-L000279](../../agents/research_completion.py#L279) | 279 | `"        },"` | — |
| [SRC-1E32639872-L000280](../../agents/research_completion.py#L280) | 280 | `"        \"counter_consistency\": {"` | — |
| [SRC-1E32639872-L000281](../../agents/research_completion.py#L281) | 281 | `"            \"status\": \"mismatch_detected\" if counter_issues else ("` | — |
| [SRC-1E32639872-L000282](../../agents/research_completion.py#L282) | 282 | `"                \"matched\" if reported_sources is not None or reported_fetched is not None"` | — |
| [SRC-1E32639872-L000283](../../agents/research_completion.py#L283) | 283 | `"                else \"not_computable\""` | — |
| [SRC-1E32639872-L000284](../../agents/research_completion.py#L284) | 284 | `"            ),"` | — |
| [SRC-1E32639872-L000285](../../agents/research_completion.py#L285) | 285 | `"            \"reported_unique_sources\": reported_sources,"` | — |
| [SRC-1E32639872-L000286](../../agents/research_completion.py#L286) | 286 | `"            \"recomputed_final_source_count\": len(sources),"` | — |
| [SRC-1E32639872-L000287](../../agents/research_completion.py#L287) | 287 | `"            \"reported_pages_fetched\": reported_fetched,"` | — |
| [SRC-1E32639872-L000288](../../agents/research_completion.py#L288) | 288 | `"            \"recomputed_pages_fetched_flag_count\": fetched,"` | — |
| [SRC-1E32639872-L000289](../../agents/research_completion.py#L289) | 289 | `"            \"issues\": counter_issues,"` | — |
| [SRC-1E32639872-L000290](../../agents/research_completion.py#L290) | 290 | `"        },"` | — |
| [SRC-1E32639872-L000291](../../agents/research_completion.py#L291) | 291 | `"        \"semantic_verification\": \"not_performed\","` | — |
| [SRC-1E32639872-L000292](../../agents/research_completion.py#L292) | 292 | `"        \"warning\": ("` | — |
| [SRC-1E32639872-L000293](../../agents/research_completion.py#L293) | 293 | `"            \"Readable pages and valid citation indexes do not prove semantic support \""` | — |
| [SRC-1E32639872-L000294](../../agents/research_completion.py#L294) | 294 | `"            \"for each claim in the answer.\""` | — |
| [SRC-1E32639872-L000295](../../agents/research_completion.py#L295) | 295 | `"        ),"` | — |
| [SRC-1E32639872-L000296](../../agents/research_completion.py#L296) | 296 | `"    }"` | — |
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

### FILE-6E58A660BC — [agents/search_connectors.py](../../agents/search_connectors.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6E58A660BC-L000001](../../agents/search_connectors.py#L1) | 1 | `"\"\"\"Free academic search connectors for Omarai (M1).\"\"\""` | — |
| [SRC-6E58A660BC-L000002](../../agents/search_connectors.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-6E58A660BC-L000003](../../agents/search_connectors.py#L3) | 3 | `""` | — |
| [SRC-6E58A660BC-L000004](../../agents/search_connectors.py#L4) | 4 | `"import json"` | — |
| [SRC-6E58A660BC-L000005](../../agents/search_connectors.py#L5) | 5 | `"import os"` | — |
| [SRC-6E58A660BC-L000006](../../agents/search_connectors.py#L6) | 6 | `"import re"` | — |
| [SRC-6E58A660BC-L000007](../../agents/search_connectors.py#L7) | 7 | `"import urllib.error"` | — |
| [SRC-6E58A660BC-L000008](../../agents/search_connectors.py#L8) | 8 | `"import urllib.parse"` | — |
| [SRC-6E58A660BC-L000009](../../agents/search_connectors.py#L9) | 9 | `"import urllib.request"` | — |
| [SRC-6E58A660BC-L000010](../../agents/search_connectors.py#L10) | 10 | `"from collections.abc import Callable"` | — |
| [SRC-6E58A660BC-L000011](../../agents/search_connectors.py#L11) | 11 | `"from typing import Any"` | — |
| [SRC-6E58A660BC-L000012](../../agents/search_connectors.py#L12) | 12 | `""` | — |
| [SRC-6E58A660BC-L000013](../../agents/search_connectors.py#L13) | 13 | `"MAX_CONNECTOR_RESULTS = 6"` | — |
| [SRC-6E58A660BC-L000014](../../agents/search_connectors.py#L14) | 14 | `"DEFAULT_TIMEOUT_SECONDS = 5"` | — |
| [SRC-6E58A660BC-L000015](../../agents/search_connectors.py#L15) | 15 | `"USER_AGENT = \"OmaraiResearchBot/1.0 (mailto:ops@example.com)\""` | — |
| [SRC-6E58A660BC-L000016](../../agents/search_connectors.py#L16) | 16 | `"ConnectorFn = Callable[[str, int], list[dict[str, Any]]]"` | — |
| [SRC-6E58A660BC-L000017](../../agents/search_connectors.py#L17) | 17 | `""` | — |
| [SRC-6E58A660BC-L000018](../../agents/search_connectors.py#L18) | 18 | `""` | — |
| [SRC-6E58A660BC-L000019](../../agents/search_connectors.py#L19) | 19 | `"def _clean_text(value: Any, limit: int = 1600) -> str:"` | — |
| [SRC-6E58A660BC-L000020](../../agents/search_connectors.py#L20) | 20 | `"    if not isinstance(value, str):"` | — |
| [SRC-6E58A660BC-L000021](../../agents/search_connectors.py#L21) | 21 | `"        return \"\""` | — |
| [SRC-6E58A660BC-L000022](../../agents/search_connectors.py#L22) | 22 | `"    return re.sub(r\"\\s+\", \" \", value).strip()[:limit]"` | — |
| [SRC-6E58A660BC-L000023](../../agents/search_connectors.py#L23) | 23 | `""` | — |
| [SRC-6E58A660BC-L000024](../../agents/search_connectors.py#L24) | 24 | `""` | — |
| [SRC-6E58A660BC-L000025](../../agents/search_connectors.py#L25) | 25 | `"def _http_get_json(url: str, headers: dict[str, str] \| None = None, timeout: int = DEFAULT_TIMEOUT_SECONDS) -> Any:"` | — |
| [SRC-6E58A660BC-L000026](../../agents/search_connectors.py#L26) | 26 | `"    req_headers = {\"User-Agent\": USER_AGENT, \"Accept\": \"application/json\"}"` | — |
| [SRC-6E58A660BC-L000027](../../agents/search_connectors.py#L27) | 27 | `"    if headers:"` | — |
| [SRC-6E58A660BC-L000028](../../agents/search_connectors.py#L28) | 28 | `"        req_headers.update(headers)"` | — |
| [SRC-6E58A660BC-L000029](../../agents/search_connectors.py#L29) | 29 | `"    request = urllib.request.Request(url, headers=req_headers, method=\"GET\")"` | — |
| [SRC-6E58A660BC-L000030](../../agents/search_connectors.py#L30) | 30 | `"    with urllib.request.urlopen(request, timeout=timeout) as response:"` | — |
| [SRC-6E58A660BC-L000031](../../agents/search_connectors.py#L31) | 31 | `"        return json.loads(response.read().decode(\"utf-8\", errors=\"replace\"))"` | — |
| [SRC-6E58A660BC-L000032](../../agents/search_connectors.py#L32) | 32 | `""` | — |
| [SRC-6E58A660BC-L000033](../../agents/search_connectors.py#L33) | 33 | `""` | — |
| [SRC-6E58A660BC-L000034](../../agents/search_connectors.py#L34) | 34 | `"def _http_get_text(url: str, timeout: int = DEFAULT_TIMEOUT_SECONDS) -> str:"` | — |
| [SRC-6E58A660BC-L000035](../../agents/search_connectors.py#L35) | 35 | `"    request = urllib.request.Request(url, headers={\"User-Agent\": USER_AGENT}, method=\"GET\")"` | — |
| [SRC-6E58A660BC-L000036](../../agents/search_connectors.py#L36) | 36 | `"    with urllib.request.urlopen(request, timeout=timeout) as response:"` | — |
| [SRC-6E58A660BC-L000037](../../agents/search_connectors.py#L37) | 37 | `"        return response.read().decode(\"utf-8\", errors=\"replace\")"` | — |
| [SRC-6E58A660BC-L000038](../../agents/search_connectors.py#L38) | 38 | `""` | — |
| [SRC-6E58A660BC-L000039](../../agents/search_connectors.py#L39) | 39 | `""` | — |
| [SRC-6E58A660BC-L000040](../../agents/search_connectors.py#L40) | 40 | `"def _result(*, title: str, url: str, snippet: str, provider: str, rank: int, query: str, published_at: str = \"\", source_class: str = \"web\") -> dict[str, Any]:"` | — |
| [SRC-6E58A660BC-L000041](../../agents/search_connectors.py#L41) | 41 | `"    return {"` | — |
| [SRC-6E58A660BC-L000042](../../agents/search_connectors.py#L42) | 42 | `"        \"title\": _clean_text(title, 300),"` | — |
| [SRC-6E58A660BC-L000043](../../agents/search_connectors.py#L43) | 43 | `"        \"url\": (url or \"\").strip(),"` | — |
| [SRC-6E58A660BC-L000044](../../agents/search_connectors.py#L44) | 44 | `"        \"snippet\": _clean_text(snippet, 1600),"` | — |
| [SRC-6E58A660BC-L000045](../../agents/search_connectors.py#L45) | 45 | `"        \"page_fetched\": False,"` | — |
| [SRC-6E58A660BC-L000046](../../agents/search_connectors.py#L46) | 46 | `"        \"provider\": provider,"` | — |
| [SRC-6E58A660BC-L000047](../../agents/search_connectors.py#L47) | 47 | `"        \"provider_rank\": rank,"` | — |
| [SRC-6E58A660BC-L000048](../../agents/search_connectors.py#L48) | 48 | `"        \"search_query\": query,"` | — |
| [SRC-6E58A660BC-L000049](../../agents/search_connectors.py#L49) | 49 | `"        \"published_at\": published_at or \"\","` | — |
| [SRC-6E58A660BC-L000050](../../agents/search_connectors.py#L50) | 50 | `"        \"source_class\": source_class,"` | — |
| [SRC-6E58A660BC-L000051](../../agents/search_connectors.py#L51) | 51 | `"    }"` | — |
| [SRC-6E58A660BC-L000052](../../agents/search_connectors.py#L52) | 52 | `""` | — |
| [SRC-6E58A660BC-L000053](../../agents/search_connectors.py#L53) | 53 | `""` | — |
| [SRC-6E58A660BC-L000054](../../agents/search_connectors.py#L54) | 54 | `"def search_openalex(query: str, limit: int = MAX_CONNECTOR_RESULTS) -> list[dict[str, Any]]:"` | — |
| [SRC-6E58A660BC-L000055](../../agents/search_connectors.py#L55) | 55 | `"    if not isinstance(query, str) or not query.strip():"` | — |
| [SRC-6E58A660BC-L000056](../../agents/search_connectors.py#L56) | 56 | `"        return []"` | — |
| [SRC-6E58A660BC-L000057](../../agents/search_connectors.py#L57) | 57 | `"    params = urllib.parse.urlencode({\"search\": query.strip()[:240], \"per_page\": max(1, min(int(limit), MAX_CONNECTOR_RESULTS)), \"mailto\": os.getenv(\"OPENALEX_MAILTO\", \"ops@example.com\")})"` | — |
| [SRC-6E58A660BC-L000058](../../agents/search_connectors.py#L58) | 58 | `"    data = _http_get_json(f\"https://api.openalex.org/works?{params}\")"` | — |
| [SRC-6E58A660BC-L000059](../../agents/search_connectors.py#L59) | 59 | `"    rows: list[dict[str, Any]] = []"` | — |
| [SRC-6E58A660BC-L000060](../../agents/search_connectors.py#L60) | 60 | `"    for item in data.get(\"results\", [])[:limit]:"` | — |
| [SRC-6E58A660BC-L000061](../../agents/search_connectors.py#L61) | 61 | `"        if not isinstance(item, dict):"` | — |
| [SRC-6E58A660BC-L000062](../../agents/search_connectors.py#L62) | 62 | `"            continue"` | — |
| [SRC-6E58A660BC-L000063](../../agents/search_connectors.py#L63) | 63 | `"        title = item.get(\"display_name\") or \"\""` | — |
| [SRC-6E58A660BC-L000064](../../agents/search_connectors.py#L64) | 64 | `"        url = \"\""` | — |
| [SRC-6E58A660BC-L000065](../../agents/search_connectors.py#L65) | 65 | `"        primary = item.get(\"primary_location\") or {}"` | — |
| [SRC-6E58A660BC-L000066](../../agents/search_connectors.py#L66) | 66 | `"        if isinstance(primary, dict) and primary.get(\"landing_page_url\"):"` | — |
| [SRC-6E58A660BC-L000067](../../agents/search_connectors.py#L67) | 67 | `"            url = str(primary.get(\"landing_page_url\"))"` | — |
| [SRC-6E58A660BC-L000068](../../agents/search_connectors.py#L68) | 68 | `"        elif item.get(\"id\"):"` | — |
| [SRC-6E58A660BC-L000069](../../agents/search_connectors.py#L69) | 69 | `"            url = str(item.get(\"id\"))"` | — |
| [SRC-6E58A660BC-L000070](../../agents/search_connectors.py#L70) | 70 | `"        concepts = \", \".join(str(c.get(\"display_name\", \"\")) for c in (item.get(\"concepts\") or [])[:5] if isinstance(c, dict))"` | — |
| [SRC-6E58A660BC-L000071](../../agents/search_connectors.py#L71) | 71 | `"        snippet = f\"{title}. {concepts}\".strip(\". \")"` | — |
| [SRC-6E58A660BC-L000072](../../agents/search_connectors.py#L72) | 72 | `"        if title and url:"` | — |
| [SRC-6E58A660BC-L000073](../../agents/search_connectors.py#L73) | 73 | `"            rows.append(_result(title=title, url=url, snippet=snippet or title, provider=\"openalex\", rank=len(rows) + 1, query=query, published_at=str(item.get(\"publication_date\") or \"\"), source_class=\"academic\"))"` | — |
| [SRC-6E58A660BC-L000074](../../agents/search_connectors.py#L74) | 74 | `"    return rows"` | — |
| [SRC-6E58A660BC-L000075](../../agents/search_connectors.py#L75) | 75 | `""` | — |
| [SRC-6E58A660BC-L000076](../../agents/search_connectors.py#L76) | 76 | `""` | — |
| [SRC-6E58A660BC-L000077](../../agents/search_connectors.py#L77) | 77 | `"def search_arxiv(query: str, limit: int = MAX_CONNECTOR_RESULTS) -> list[dict[str, Any]]:"` | — |
| [SRC-6E58A660BC-L000078](../../agents/search_connectors.py#L78) | 78 | `"    if not isinstance(query, str) or not query.strip():"` | — |
| [SRC-6E58A660BC-L000079](../../agents/search_connectors.py#L79) | 79 | `"        return []"` | — |
| [SRC-6E58A660BC-L000080](../../agents/search_connectors.py#L80) | 80 | `"    params = urllib.parse.urlencode({\"search_query\": f\"all:{query.strip()[:200]}\", \"start\": 0, \"max_results\": max(1, min(int(limit), MAX_CONNECTOR_RESULTS))})"` | — |
| [SRC-6E58A660BC-L000081](../../agents/search_connectors.py#L81) | 81 | `"    xml_text = _http_get_text(f\"https://export.arxiv.org/api/query?{params}\")"` | — |
| [SRC-6E58A660BC-L000082](../../agents/search_connectors.py#L82) | 82 | `"    entries = re.findall(r\"<entry>(.*?)</entry>\", xml_text, flags=re.DOTALL)"` | — |
| [SRC-6E58A660BC-L000083](../../agents/search_connectors.py#L83) | 83 | `"    rows: list[dict[str, Any]] = []"` | — |
| [SRC-6E58A660BC-L000084](../../agents/search_connectors.py#L84) | 84 | `"    for entry in entries[:limit]:"` | — |
| [SRC-6E58A660BC-L000085](../../agents/search_connectors.py#L85) | 85 | `"        title_m = re.search(r\"<title>(.*?)</title>\", entry, re.DOTALL)"` | — |
| [SRC-6E58A660BC-L000086](../../agents/search_connectors.py#L86) | 86 | `"        link_m = re.search(r\"<id>(https?://arxiv\\.org/abs/[^<]+)</id>\", entry)"` | — |
| [SRC-6E58A660BC-L000087](../../agents/search_connectors.py#L87) | 87 | `"        summary_m = re.search(r\"<summary>(.*?)</summary>\", entry, re.DOTALL)"` | — |
| [SRC-6E58A660BC-L000088](../../agents/search_connectors.py#L88) | 88 | `"        published_m = re.search(r\"<published>([^<]+)</published>\", entry)"` | — |
| [SRC-6E58A660BC-L000089](../../agents/search_connectors.py#L89) | 89 | `"        title = _clean_text(title_m.group(1) if title_m else \"\")"` | — |
| [SRC-6E58A660BC-L000090](../../agents/search_connectors.py#L90) | 90 | `"        link = link_m.group(1) if link_m else \"\""` | — |
| [SRC-6E58A660BC-L000091](../../agents/search_connectors.py#L91) | 91 | `"        summary = _clean_text(summary_m.group(1) if summary_m else \"\", 1600)"` | — |
| [SRC-6E58A660BC-L000092](../../agents/search_connectors.py#L92) | 92 | `"        published = published_m.group(1) if published_m else \"\""` | — |
| [SRC-6E58A660BC-L000093](../../agents/search_connectors.py#L93) | 93 | `"        if title and link:"` | — |
| [SRC-6E58A660BC-L000094](../../agents/search_connectors.py#L94) | 94 | `"            rows.append(_result(title=title, url=link, snippet=summary or title, provider=\"arxiv\", rank=len(rows) + 1, query=query, published_at=published, source_class=\"academic\"))"` | — |
| [SRC-6E58A660BC-L000095](../../agents/search_connectors.py#L95) | 95 | `"    return rows"` | — |
| [SRC-6E58A660BC-L000096](../../agents/search_connectors.py#L96) | 96 | `""` | — |
| [SRC-6E58A660BC-L000097](../../agents/search_connectors.py#L97) | 97 | `""` | — |
| [SRC-6E58A660BC-L000098](../../agents/search_connectors.py#L98) | 98 | `"def search_crossref(query: str, limit: int = MAX_CONNECTOR_RESULTS) -> list[dict[str, Any]]:"` | — |
| [SRC-6E58A660BC-L000099](../../agents/search_connectors.py#L99) | 99 | `"    if not isinstance(query, str) or not query.strip():"` | — |
| [SRC-6E58A660BC-L000100](../../agents/search_connectors.py#L100) | 100 | `"        return []"` | — |
| [SRC-6E58A660BC-L000101](../../agents/search_connectors.py#L101) | 101 | `"    params = urllib.parse.urlencode({\"query\": query.strip()[:240], \"rows\": max(1, min(int(limit), MAX_CONNECTOR_RESULTS)), \"mailto\": os.getenv(\"CROSSREF_MAILTO\", \"ops@example.com\")})"` | — |
| [SRC-6E58A660BC-L000102](../../agents/search_connectors.py#L102) | 102 | `"    data = _http_get_json(f\"https://api.crossref.org/works?{params}\", headers={\"User-Agent\": USER_AGENT})"` | — |
| [SRC-6E58A660BC-L000103](../../agents/search_connectors.py#L103) | 103 | `"    items = ((data.get(\"message\") or {}).get(\"items\") or [])[:limit]"` | — |
| [SRC-6E58A660BC-L000104](../../agents/search_connectors.py#L104) | 104 | `"    rows: list[dict[str, Any]] = []"` | — |
| [SRC-6E58A660BC-L000105](../../agents/search_connectors.py#L105) | 105 | `"    for item in items:"` | — |
| [SRC-6E58A660BC-L000106](../../agents/search_connectors.py#L106) | 106 | `"        if not isinstance(item, dict):"` | — |
| [SRC-6E58A660BC-L000107](../../agents/search_connectors.py#L107) | 107 | `"            continue"` | — |
| [SRC-6E58A660BC-L000108](../../agents/search_connectors.py#L108) | 108 | `"        title_list = item.get(\"title\") or []"` | — |
| [SRC-6E58A660BC-L000109](../../agents/search_connectors.py#L109) | 109 | `"        title = title_list[0] if isinstance(title_list, list) and title_list else \"\""` | — |
| [SRC-6E58A660BC-L000110](../../agents/search_connectors.py#L110) | 110 | `"        url = str(item.get(\"URL\") or \"\")"` | — |
| [SRC-6E58A660BC-L000111](../../agents/search_connectors.py#L111) | 111 | `"        container_list = item.get(\"container-title\") or []"` | — |
| [SRC-6E58A660BC-L000112](../../agents/search_connectors.py#L112) | 112 | `"        container = container_list[0] if isinstance(container_list, list) and container_list else \"\""` | — |
| [SRC-6E58A660BC-L000113](../../agents/search_connectors.py#L113) | 113 | `"        year = \"\""` | — |
| [SRC-6E58A660BC-L000114](../../agents/search_connectors.py#L114) | 114 | `"        issued = item.get(\"issued\") or {}"` | — |
| [SRC-6E58A660BC-L000115](../../agents/search_connectors.py#L115) | 115 | `"        if isinstance(issued, dict) and issued.get(\"date-parts\"):"` | — |
| [SRC-6E58A660BC-L000116](../../agents/search_connectors.py#L116) | 116 | `"            try:"` | — |
| [SRC-6E58A660BC-L000117](../../agents/search_connectors.py#L117) | 117 | `"                year = str(issued[\"date-parts\"][0][0])"` | — |
| [SRC-6E58A660BC-L000118](../../agents/search_connectors.py#L118) | 118 | `"            except (IndexError, TypeError, KeyError):"` | — |
| [SRC-6E58A660BC-L000119](../../agents/search_connectors.py#L119) | 119 | `"                year = \"\""` | — |
| [SRC-6E58A660BC-L000120](../../agents/search_connectors.py#L120) | 120 | `"        snippet = _clean_text(f\"{title}. {container} {year}\".strip())"` | — |
| [SRC-6E58A660BC-L000121](../../agents/search_connectors.py#L121) | 121 | `"        if title and url:"` | — |
| [SRC-6E58A660BC-L000122](../../agents/search_connectors.py#L122) | 122 | `"            rows.append(_result(title=title, url=url, snippet=snippet, provider=\"crossref\", rank=len(rows) + 1, query=query, published_at=year, source_class=\"academic\"))"` | — |
| [SRC-6E58A660BC-L000123](../../agents/search_connectors.py#L123) | 123 | `"    return rows"` | — |
| [SRC-6E58A660BC-L000124](../../agents/search_connectors.py#L124) | 124 | `""` | — |
| [SRC-6E58A660BC-L000125](../../agents/search_connectors.py#L125) | 125 | `""` | — |
| [SRC-6E58A660BC-L000126](../../agents/search_connectors.py#L126) | 126 | `"def search_semantic_scholar(query: str, limit: int = MAX_CONNECTOR_RESULTS) -> list[dict[str, Any]]:"` | — |
| [SRC-6E58A660BC-L000127](../../agents/search_connectors.py#L127) | 127 | `"    if not isinstance(query, str) or not query.strip():"` | — |
| [SRC-6E58A660BC-L000128](../../agents/search_connectors.py#L128) | 128 | `"        return []"` | — |
| [SRC-6E58A660BC-L000129](../../agents/search_connectors.py#L129) | 129 | `"    key = os.getenv(\"SEMANTIC_SCHOLAR_API_KEY\", \"\").strip()"` | — |
| [SRC-6E58A660BC-L000130](../../agents/search_connectors.py#L130) | 130 | `"    params = urllib.parse.urlencode({\"query\": query.strip()[:240], \"limit\": max(1, min(int(limit), MAX_CONNECTOR_RESULTS)), \"fields\": \"title,url,abstract,year,externalIds\"})"` | — |
| [SRC-6E58A660BC-L000131](../../agents/search_connectors.py#L131) | 131 | `"    headers = {\"User-Agent\": USER_AGENT}"` | — |
| [SRC-6E58A660BC-L000132](../../agents/search_connectors.py#L132) | 132 | `"    if key:"` | — |
| [SRC-6E58A660BC-L000133](../../agents/search_connectors.py#L133) | 133 | `"        headers[\"x-api-key\"] = key"` | — |
| [SRC-6E58A660BC-L000134](../../agents/search_connectors.py#L134) | 134 | `"    data = _http_get_json(f\"https://api.semanticscholar.org/graph/v1/paper/search?{params}\", headers=headers)"` | — |
| [SRC-6E58A660BC-L000135](../../agents/search_connectors.py#L135) | 135 | `"    rows: list[dict[str, Any]] = []"` | — |
| [SRC-6E58A660BC-L000136](../../agents/search_connectors.py#L136) | 136 | `"    for item in (data.get(\"data\") or [])[:limit]:"` | — |
| [SRC-6E58A660BC-L000137](../../agents/search_connectors.py#L137) | 137 | `"        if not isinstance(item, dict):"` | — |
| [SRC-6E58A660BC-L000138](../../agents/search_connectors.py#L138) | 138 | `"            continue"` | — |
| [SRC-6E58A660BC-L000139](../../agents/search_connectors.py#L139) | 139 | `"        title = item.get(\"title\") or \"\""` | — |
| [SRC-6E58A660BC-L000140](../../agents/search_connectors.py#L140) | 140 | `"        url = item.get(\"url\") or \"\""` | — |
| [SRC-6E58A660BC-L000141](../../agents/search_connectors.py#L141) | 141 | `"        if not url and isinstance(item.get(\"externalIds\"), dict):"` | — |
| [SRC-6E58A660BC-L000142](../../agents/search_connectors.py#L142) | 142 | `"            doi = item[\"externalIds\"].get(\"DOI\")"` | — |
| [SRC-6E58A660BC-L000143](../../agents/search_connectors.py#L143) | 143 | `"            if doi:"` | — |
| [SRC-6E58A660BC-L000144](../../agents/search_connectors.py#L144) | 144 | `"                url = f\"https://doi.org/{doi}\""` | — |
| [SRC-6E58A660BC-L000145](../../agents/search_connectors.py#L145) | 145 | `"        snippet = item.get(\"abstract\") or title"` | — |
| [SRC-6E58A660BC-L000146](../../agents/search_connectors.py#L146) | 146 | `"        year = str(item.get(\"year\") or \"\")"` | — |
| [SRC-6E58A660BC-L000147](../../agents/search_connectors.py#L147) | 147 | `"        if title and url:"` | — |
| [SRC-6E58A660BC-L000148](../../agents/search_connectors.py#L148) | 148 | `"            rows.append(_result(title=title, url=url, snippet=snippet, provider=\"semantic_scholar\", rank=len(rows) + 1, query=query, published_at=year, source_class=\"academic\"))"` | — |
| [SRC-6E58A660BC-L000149](../../agents/search_connectors.py#L149) | 149 | `"    return rows"` | — |
| [SRC-6E58A660BC-L000150](../../agents/search_connectors.py#L150) | 150 | `""` | — |
| [SRC-6E58A660BC-L000151](../../agents/search_connectors.py#L151) | 151 | `""` | — |
| [SRC-6E58A660BC-L000152](../../agents/search_connectors.py#L152) | 152 | `"CONNECTOR_REGISTRY: dict[str, dict[str, Any]] = {"` | — |
| [SRC-6E58A660BC-L000153](../../agents/search_connectors.py#L153) | 153 | `"    \"openalex\": {\"fn\": search_openalex, \"source_class\": \"academic\", \"requires_key\": False},"` | — |
| [SRC-6E58A660BC-L000154](../../agents/search_connectors.py#L154) | 154 | `"    \"arxiv\": {\"fn\": search_arxiv, \"source_class\": \"academic\", \"requires_key\": False},"` | — |
| [SRC-6E58A660BC-L000155](../../agents/search_connectors.py#L155) | 155 | `"    \"crossref\": {\"fn\": search_crossref, \"source_class\": \"academic\", \"requires_key\": False},"` | — |
| [SRC-6E58A660BC-L000156](../../agents/search_connectors.py#L156) | 156 | `"    \"semantic_scholar\": {\"fn\": search_semantic_scholar, \"source_class\": \"academic\", \"requires_key\": False},"` | — |
| [SRC-6E58A660BC-L000157](../../agents/search_connectors.py#L157) | 157 | `"}"` | — |
| [SRC-6E58A660BC-L000158](../../agents/search_connectors.py#L158) | 158 | `""` | — |
| [SRC-6E58A660BC-L000159](../../agents/search_connectors.py#L159) | 159 | `""` | — |
| [SRC-6E58A660BC-L000160](../../agents/search_connectors.py#L160) | 160 | `"def run_connector(name: str, query: str, limit: int = MAX_CONNECTOR_RESULTS) -> list[dict[str, Any]]:"` | — |
| [SRC-6E58A660BC-L000161](../../agents/search_connectors.py#L161) | 161 | `"    meta = CONNECTOR_REGISTRY.get(name)"` | — |
| [SRC-6E58A660BC-L000162](../../agents/search_connectors.py#L162) | 162 | `"    if not meta or meta.get(\"fn\") is None:"` | — |
| [SRC-6E58A660BC-L000163](../../agents/search_connectors.py#L163) | 163 | `"        return []"` | — |
| [SRC-6E58A660BC-L000164](../../agents/search_connectors.py#L164) | 164 | `"    if not isinstance(query, str) or not query.strip():"` | — |
| [SRC-6E58A660BC-L000165](../../agents/search_connectors.py#L165) | 165 | `"        return []"` | — |
| [SRC-6E58A660BC-L000166](../../agents/search_connectors.py#L166) | 166 | `"    try:"` | — |
| [SRC-6E58A660BC-L000167](../../agents/search_connectors.py#L167) | 167 | `"        rows = meta[\"fn\"](query, limit=limit) or []"` | — |
| [SRC-6E58A660BC-L000168](../../agents/search_connectors.py#L168) | 168 | `"        return [row for row in rows if isinstance(row, dict) and row.get(\"url\") and row.get(\"title\")]"` | — |
| [SRC-6E58A660BC-L000169](../../agents/search_connectors.py#L169) | 169 | `"    except (TimeoutError, urllib.error.URLError, urllib.error.HTTPError, ValueError, KeyError, TypeError, json.JSONDecodeError, OSError):"` | — |
| [SRC-6E58A660BC-L000170](../../agents/search_connectors.py#L170) | 170 | `"        return []"` | — |
| [SRC-6E58A660BC-L000171](../../agents/search_connectors.py#L171) | 171 | `""` | — |
| [SRC-6E58A660BC-L000172](../../agents/search_connectors.py#L172) | 172 | `""` | — |
| [SRC-6E58A660BC-L000173](../../agents/search_connectors.py#L173) | 173 | `"def run_free_academic_connectors(query: str, limit_per: int = 4) -> list[dict[str, Any]]:"` | — |
| [SRC-6E58A660BC-L000174](../../agents/search_connectors.py#L174) | 174 | `"    combined: list[dict[str, Any]] = []"` | — |
| [SRC-6E58A660BC-L000175](../../agents/search_connectors.py#L175) | 175 | `"    for name in (\"openalex\", \"arxiv\", \"crossref\"):"` | — |
| [SRC-6E58A660BC-L000176](../../agents/search_connectors.py#L176) | 176 | `"        combined.extend(run_connector(name, query, limit=limit_per))"` | — |
| [SRC-6E58A660BC-L000177](../../agents/search_connectors.py#L177) | 177 | `"    return combined"` | — |
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
| [SRC-1AE03B9EC3-L000013](../../agents/web_agent.py#L13) | 13 | `"import os"` | — |
| [SRC-1AE03B9EC3-L000014](../../agents/web_agent.py#L14) | 14 | `"import re"` | — |
| [SRC-1AE03B9EC3-L000015](../../agents/web_agent.py#L15) | 15 | `"import socket"` | — |
| [SRC-1AE03B9EC3-L000016](../../agents/web_agent.py#L16) | 16 | `"import threading"` | — |
| [SRC-1AE03B9EC3-L000017](../../agents/web_agent.py#L17) | 17 | `"import unicodedata"` | — |
| [SRC-1AE03B9EC3-L000018](../../agents/web_agent.py#L18) | 18 | `"import urllib.error"` | — |
| [SRC-1AE03B9EC3-L000019](../../agents/web_agent.py#L19) | 19 | `"import urllib.parse"` | — |
| [SRC-1AE03B9EC3-L000020](../../agents/web_agent.py#L20) | 20 | `"import urllib.request"` | — |
| [SRC-1AE03B9EC3-L000021](../../agents/web_agent.py#L21) | 21 | `"from concurrent.futures import ThreadPoolExecutor, as_completed"` | — |
| [SRC-1AE03B9EC3-L000022](../../agents/web_agent.py#L22) | 22 | `"from typing import Any"` | — |
| [SRC-1AE03B9EC3-L000023](../../agents/web_agent.py#L23) | 23 | `""` | — |
| [SRC-1AE03B9EC3-L000024](../../agents/web_agent.py#L24) | 24 | `"from agents.intent_router import resolve_followup_query, route_intent"` | — |
| [SRC-1AE03B9EC3-L000025](../../agents/web_agent.py#L25) | 25 | `"from agents.dialogue_state import ("` | — |
| [SRC-1AE03B9EC3-L000026](../../agents/web_agent.py#L26) | 26 | `"    fallback_dialogue_context,"` | — |
| [SRC-1AE03B9EC3-L000027](../../agents/web_agent.py#L27) | 27 | `"    might_be_context_dependent,"` | — |
