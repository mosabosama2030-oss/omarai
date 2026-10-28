# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **006**
- سجلات الأسطر: **800**
- النطاق: SRC-3AA6165B18-L000070 إلى SRC-1AE03B9EC3-L000083
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-3AA6165B18 — [agents/research_guardrails.py](../../agents/research_guardrails.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-3AA6165B18-L000070](../../agents/research_guardrails.py#L70) | 70 | `"    return any(host == domain or host.endswith(\".\" + domain)"` | — |
| [SRC-3AA6165B18-L000071](../../agents/research_guardrails.py#L71) | 71 | `"               for domain in SOCIAL_DOMAINS.values())"` | — |
| [SRC-3AA6165B18-L000072](../../agents/research_guardrails.py#L72) | 72 | `""` | — |
| [SRC-3AA6165B18-L000073](../../agents/research_guardrails.py#L73) | 73 | `""` | — |
| [SRC-3AA6165B18-L000074](../../agents/research_guardrails.py#L74) | 74 | `"def _is_navigation_request(question: str) -> bool:"` | — |
| [SRC-3AA6165B18-L000075](../../agents/research_guardrails.py#L75) | 75 | `"    value = _normalized(question)"` | — |
| [SRC-3AA6165B18-L000076](../../agents/research_guardrails.py#L76) | 76 | `"    return any(term in value for term in ("` | — |
| [SRC-3AA6165B18-L000077](../../agents/research_guardrails.py#L77) | 77 | `"        \"موقع\", \"رابط\", \"لينك\", \"homepage\", \"website\", \"official site\","` | — |
| [SRC-3AA6165B18-L000078](../../agents/research_guardrails.py#L78) | 78 | `"        \"official website\", \"link to\","` | — |
| [SRC-3AA6165B18-L000079](../../agents/research_guardrails.py#L79) | 79 | `"    ))"` | — |
| [SRC-3AA6165B18-L000080](../../agents/research_guardrails.py#L80) | 80 | `""` | — |
| [SRC-3AA6165B18-L000081](../../agents/research_guardrails.py#L81) | 81 | `""` | — |
| [SRC-3AA6165B18-L000082](../../agents/research_guardrails.py#L82) | 82 | `"def requires_official_government_domain(question: str) -> bool:"` | — |
| [SRC-3AA6165B18-L000083](../../agents/research_guardrails.py#L83) | 83 | `"    \"\"\"Detect explicit requests for a government's official site, not articles about it.\"\"\""` | — |
| [SRC-3AA6165B18-L000084](../../agents/research_guardrails.py#L84) | 84 | `"    value = _normalized(question)"` | — |
| [SRC-3AA6165B18-L000085](../../agents/research_guardrails.py#L85) | 85 | `"    return ("` | — |
| [SRC-3AA6165B18-L000086](../../agents/research_guardrails.py#L86) | 86 | `"        any(term in value for term in _OFFICIAL_WORDS)"` | — |
| [SRC-3AA6165B18-L000087](../../agents/research_guardrails.py#L87) | 87 | `"        and any(term in value for term in _GOVERNMENT_ENTITY_WORDS)"` | — |
| [SRC-3AA6165B18-L000088](../../agents/research_guardrails.py#L88) | 88 | `"    )"` | — |
| [SRC-3AA6165B18-L000089](../../agents/research_guardrails.py#L89) | 89 | `""` | — |
| [SRC-3AA6165B18-L000090](../../agents/research_guardrails.py#L90) | 90 | `""` | — |
| [SRC-3AA6165B18-L000091](../../agents/research_guardrails.py#L91) | 91 | `"def _is_government_domain(url: Any) -> bool:"` | — |
| [SRC-3AA6165B18-L000092](../../agents/research_guardrails.py#L92) | 92 | `"    host = _host(url)"` | — |
| [SRC-3AA6165B18-L000093](../../agents/research_guardrails.py#L93) | 93 | `"    if not host:"` | — |
| [SRC-3AA6165B18-L000094](../../agents/research_guardrails.py#L94) | 94 | `"        return False"` | — |
| [SRC-3AA6165B18-L000095](../../agents/research_guardrails.py#L95) | 95 | `"    return any(host == suffix.lstrip(\".\") or host.endswith(suffix)"` | — |
| [SRC-3AA6165B18-L000096](../../agents/research_guardrails.py#L96) | 96 | `"               for suffix in _GOVERNMENT_SUFFIXES)"` | — |
| [SRC-3AA6165B18-L000097](../../agents/research_guardrails.py#L97) | 97 | `""` | — |
| [SRC-3AA6165B18-L000098](../../agents/research_guardrails.py#L98) | 98 | `""` | — |
| [SRC-3AA6165B18-L000099](../../agents/research_guardrails.py#L99) | 99 | `"def assess_current_source("` | — |
| [SRC-3AA6165B18-L000100](../../agents/research_guardrails.py#L100) | 100 | `"    source: dict[str, Any],"` | — |
| [SRC-3AA6165B18-L000101](../../agents/research_guardrails.py#L101) | 101 | `"    *,"` | — |
| [SRC-3AA6165B18-L000102](../../agents/research_guardrails.py#L102) | 102 | `"    now: datetime \| None = None,"` | — |
| [SRC-3AA6165B18-L000103](../../agents/research_guardrails.py#L103) | 103 | `"    max_age_days: int = _CURRENT_EVIDENCE_MAX_AGE_DAYS,"` | — |
| [SRC-3AA6165B18-L000104](../../agents/research_guardrails.py#L104) | 104 | `") -> dict[str, Any]:"` | — |
| [SRC-3AA6165B18-L000105](../../agents/research_guardrails.py#L105) | 105 | `"    \"\"\"Assess whether a read page can support a current-state claim.\"\"\""` | — |
| [SRC-3AA6165B18-L000106](../../agents/research_guardrails.py#L106) | 106 | `"    current = now or datetime.now(UTC)"` | — |
| [SRC-3AA6165B18-L000107](../../agents/research_guardrails.py#L107) | 107 | `"    if current.tzinfo is None:"` | — |
| [SRC-3AA6165B18-L000108](../../agents/research_guardrails.py#L108) | 108 | `"        current = current.replace(tzinfo=UTC)"` | — |
| [SRC-3AA6165B18-L000109](../../agents/research_guardrails.py#L109) | 109 | `"    published = _parse_publication_date(source.get(\"published_at\"), current)"` | — |
| [SRC-3AA6165B18-L000110](../../agents/research_guardrails.py#L110) | 110 | `"    if published is None:"` | — |
| [SRC-3AA6165B18-L000111](../../agents/research_guardrails.py#L111) | 111 | `"        return {\"eligible\": False, \"status\": \"date_unavailable\", \"age_days\": None}"` | — |
| [SRC-3AA6165B18-L000112](../../agents/research_guardrails.py#L112) | 112 | `"    if published > current + timedelta(days=1):"` | — |
| [SRC-3AA6165B18-L000113](../../agents/research_guardrails.py#L113) | 113 | `"        return {\"eligible\": False, \"status\": \"future_date\", \"age_days\": None}"` | — |
| [SRC-3AA6165B18-L000114](../../agents/research_guardrails.py#L114) | 114 | `"    age_days = max(0, (current - published).total_seconds() / 86400)"` | — |
| [SRC-3AA6165B18-L000115](../../agents/research_guardrails.py#L115) | 115 | `"    if age_days > max_age_days:"` | — |
| [SRC-3AA6165B18-L000116](../../agents/research_guardrails.py#L116) | 116 | `"        return {"` | — |
| [SRC-3AA6165B18-L000117](../../agents/research_guardrails.py#L117) | 117 | `"            \"eligible\": False,"` | — |
| [SRC-3AA6165B18-L000118](../../agents/research_guardrails.py#L118) | 118 | `"            \"status\": \"stale\","` | — |
| [SRC-3AA6165B18-L000119](../../agents/research_guardrails.py#L119) | 119 | `"            \"age_days\": round(age_days, 2),"` | — |
| [SRC-3AA6165B18-L000120](../../agents/research_guardrails.py#L120) | 120 | `"            \"max_age_days\": max_age_days,"` | — |
| [SRC-3AA6165B18-L000121](../../agents/research_guardrails.py#L121) | 121 | `"        }"` | — |
| [SRC-3AA6165B18-L000122](../../agents/research_guardrails.py#L122) | 122 | `"    if not bool(source.get(\"page_fetched\")) or not str(source.get(\"page_text\") or \"\").strip():"` | — |
| [SRC-3AA6165B18-L000123](../../agents/research_guardrails.py#L123) | 123 | `"        return {"` | — |
| [SRC-3AA6165B18-L000124](../../agents/research_guardrails.py#L124) | 124 | `"            \"eligible\": False,"` | — |
| [SRC-3AA6165B18-L000125](../../agents/research_guardrails.py#L125) | 125 | `"            \"status\": \"page_not_read\","` | — |
| [SRC-3AA6165B18-L000126](../../agents/research_guardrails.py#L126) | 126 | `"            \"age_days\": round(age_days, 2),"` | — |
| [SRC-3AA6165B18-L000127](../../agents/research_guardrails.py#L127) | 127 | `"            \"max_age_days\": max_age_days,"` | — |
| [SRC-3AA6165B18-L000128](../../agents/research_guardrails.py#L128) | 128 | `"        }"` | — |
| [SRC-3AA6165B18-L000129](../../agents/research_guardrails.py#L129) | 129 | `"    return {"` | — |
| [SRC-3AA6165B18-L000130](../../agents/research_guardrails.py#L130) | 130 | `"        \"eligible\": True,"` | — |
| [SRC-3AA6165B18-L000131](../../agents/research_guardrails.py#L131) | 131 | `"        \"status\": \"recent_page_read\","` | — |
| [SRC-3AA6165B18-L000132](../../agents/research_guardrails.py#L132) | 132 | `"        \"age_days\": round(age_days, 2),"` | — |
| [SRC-3AA6165B18-L000133](../../agents/research_guardrails.py#L133) | 133 | `"        \"max_age_days\": max_age_days,"` | — |
| [SRC-3AA6165B18-L000134](../../agents/research_guardrails.py#L134) | 134 | `"    }"` | — |
| [SRC-3AA6165B18-L000135](../../agents/research_guardrails.py#L135) | 135 | `""` | — |
| [SRC-3AA6165B18-L000136](../../agents/research_guardrails.py#L136) | 136 | `""` | — |
| [SRC-3AA6165B18-L000137](../../agents/research_guardrails.py#L137) | 137 | `"def classify_social_source(source: dict[str, Any]) -> dict[str, str]:"` | — |
| [SRC-3AA6165B18-L000138](../../agents/research_guardrails.py#L138) | 138 | `"    \"\"\"Apply a transparent, non-authoritative label to public social content.\"\"\""` | — |
| [SRC-3AA6165B18-L000139](../../agents/research_guardrails.py#L139) | 139 | `"    url = source.get(\"url\", \"\")"` | — |
| [SRC-3AA6165B18-L000140](../../agents/research_guardrails.py#L140) | 140 | `"    host = _host(url)"` | — |
| [SRC-3AA6165B18-L000141](../../agents/research_guardrails.py#L141) | 141 | `"    platform = next(("` | — |
| [SRC-3AA6165B18-L000142](../../agents/research_guardrails.py#L142) | 142 | `"        name for name, domain in SOCIAL_DOMAINS.items()"` | — |
| [SRC-3AA6165B18-L000143](../../agents/research_guardrails.py#L143) | 143 | `"        if host == domain or host.endswith(\".\" + domain)"` | — |
| [SRC-3AA6165B18-L000144](../../agents/research_guardrails.py#L144) | 144 | `"    ), \"\")"` | — |
| [SRC-3AA6165B18-L000145](../../agents/research_guardrails.py#L145) | 145 | `"    if not platform:"` | — |
| [SRC-3AA6165B18-L000146](../../agents/research_guardrails.py#L146) | 146 | `"        return {"` | — |
| [SRC-3AA6165B18-L000147](../../agents/research_guardrails.py#L147) | 147 | `"            \"opinion_source_classification\": \"not_a_social_post\","` | — |
| [SRC-3AA6165B18-L000148](../../agents/research_guardrails.py#L148) | 148 | `"            \"opinion_classification_basis\": \"URL host is not a recognized social platform\","` | — |
| [SRC-3AA6165B18-L000149](../../agents/research_guardrails.py#L149) | 149 | `"            \"opinion_classification_method\": \"heuristic_only\","` | — |
| [SRC-3AA6165B18-L000150](../../agents/research_guardrails.py#L150) | 150 | `"        }"` | — |
| [SRC-3AA6165B18-L000151](../../agents/research_guardrails.py#L151) | 151 | `""` | — |
| [SRC-3AA6165B18-L000152](../../agents/research_guardrails.py#L152) | 152 | `"    text = _normalized(\" \".join("` | — |
| [SRC-3AA6165B18-L000153](../../agents/research_guardrails.py#L153) | 153 | `"        str(source.get(field) or \"\")"` | — |
| [SRC-3AA6165B18-L000154](../../agents/research_guardrails.py#L154) | 154 | `"        for field in (\"title\", \"snippet\", \"page_text\")"` | — |
| [SRC-3AA6165B18-L000155](../../agents/research_guardrails.py#L155) | 155 | `"    ))"` | — |
| [SRC-3AA6165B18-L000156](../../agents/research_guardrails.py#L156) | 156 | `"    # Normalize the vocabulary as well as the source text so English phrases"` | — |
| [SRC-3AA6165B18-L000157](../../agents/research_guardrails.py#L157) | 157 | `"    # remain case-insensitive (for example, \"I own\" versus \"i own\")."` | — |
| [SRC-3AA6165B18-L000158](../../agents/research_guardrails.py#L158) | 158 | `"    def has_term(terms: tuple[str, ...]) -> bool:"` | — |
| [SRC-3AA6165B18-L000159](../../agents/research_guardrails.py#L159) | 159 | `"        return any(_normalized(term) in text for term in terms)"` | — |
| [SRC-3AA6165B18-L000160](../../agents/research_guardrails.py#L160) | 160 | `"    if has_term(_PROMOTION_TERMS):"` | — |
| [SRC-3AA6165B18-L000161](../../agents/research_guardrails.py#L161) | 161 | `"        label = \"promotional_or_commercial\""` | — |
| [SRC-3AA6165B18-L000162](../../agents/research_guardrails.py#L162) | 162 | `"        basis = \"commercial language detected\""` | — |
| [SRC-3AA6165B18-L000163](../../agents/research_guardrails.py#L163) | 163 | `"    elif has_term(_PERSONAL_EXPERIENCE_TERMS):"` | — |
| [SRC-3AA6165B18-L000164](../../agents/research_guardrails.py#L164) | 164 | `"        label = \"personal_experience_candidate\""` | — |
| [SRC-3AA6165B18-L000165](../../agents/research_guardrails.py#L165) | 165 | `"        basis = \"first-person experience language detected\""` | — |
| [SRC-3AA6165B18-L000166](../../agents/research_guardrails.py#L166) | 166 | `"    elif has_term(_DISCUSSION_TERMS):"` | — |
| [SRC-3AA6165B18-L000167](../../agents/research_guardrails.py#L167) | 167 | `"        label = \"discussion_or_question\""` | — |
| [SRC-3AA6165B18-L000168](../../agents/research_guardrails.py#L168) | 168 | `"        basis = \"question or discussion language detected\""` | — |
| [SRC-3AA6165B18-L000169](../../agents/research_guardrails.py#L169) | 169 | `"    else:"` | — |
| [SRC-3AA6165B18-L000170](../../agents/research_guardrails.py#L170) | 170 | `"        label = \"social_post_unclassified\""` | — |
| [SRC-3AA6165B18-L000171](../../agents/research_guardrails.py#L171) | 171 | `"        basis = \"no clear experience/discussion signal; manual review needed\""` | — |
| [SRC-3AA6165B18-L000172](../../agents/research_guardrails.py#L172) | 172 | `"    return {"` | — |
| [SRC-3AA6165B18-L000173](../../agents/research_guardrails.py#L173) | 173 | `"        \"opinion_source_classification\": label,"` | — |
| [SRC-3AA6165B18-L000174](../../agents/research_guardrails.py#L174) | 174 | `"        \"opinion_classification_basis\": basis,"` | — |
| [SRC-3AA6165B18-L000175](../../agents/research_guardrails.py#L175) | 175 | `"        \"opinion_classification_method\": \"heuristic_only\","` | — |
| [SRC-3AA6165B18-L000176](../../agents/research_guardrails.py#L176) | 176 | `"    }"` | — |
| [SRC-3AA6165B18-L000177](../../agents/research_guardrails.py#L177) | 177 | `""` | — |
| [SRC-3AA6165B18-L000178](../../agents/research_guardrails.py#L178) | 178 | `""` | — |
| [SRC-3AA6165B18-L000179](../../agents/research_guardrails.py#L179) | 179 | `"def apply_source_guardrails("` | — |
| [SRC-3AA6165B18-L000180](../../agents/research_guardrails.py#L180) | 180 | `"    question: str,"` | — |
| [SRC-3AA6165B18-L000181](../../agents/research_guardrails.py#L181) | 181 | `"    mode: str,"` | — |
| [SRC-3AA6165B18-L000182](../../agents/research_guardrails.py#L182) | 182 | `"    plan: dict[str, Any],"` | — |
| [SRC-3AA6165B18-L000183](../../agents/research_guardrails.py#L183) | 183 | `"    sources: list[dict[str, Any]],"` | — |
| [SRC-3AA6165B18-L000184](../../agents/research_guardrails.py#L184) | 184 | `"    *,"` | — |
| [SRC-3AA6165B18-L000185](../../agents/research_guardrails.py#L185) | 185 | `"    now: datetime \| None = None,"` | — |
| [SRC-3AA6165B18-L000186](../../agents/research_guardrails.py#L186) | 186 | `") -> tuple[list[dict[str, Any]], dict[str, Any]]:"` | — |
| [SRC-3AA6165B18-L000187](../../agents/research_guardrails.py#L187) | 187 | `"    \"\"\"Apply official-domain, current-evidence, and explicit social-mode guards."` | — |
| [SRC-3AA6165B18-L000188](../../agents/research_guardrails.py#L188) | 188 | `""` | — |
| [SRC-3AA6165B18-L000189](../../agents/research_guardrails.py#L189) | 189 | `"    Rejection counters describe this filter stage only. They are not search-engine"` | — |
| [SRC-3AA6165B18-L000190](../../agents/research_guardrails.py#L190) | 190 | `"    totals, and passing them is not a semantic fact check."` | — |
| [SRC-3AA6165B18-L000191](../../agents/research_guardrails.py#L191) | 191 | `"    \"\"\""` | — |
| [SRC-3AA6165B18-L000192](../../agents/research_guardrails.py#L192) | 192 | `"    clean_mode = str(mode or \"auto\").strip().lower()"` | — |
| [SRC-3AA6165B18-L000193](../../agents/research_guardrails.py#L193) | 193 | `"    official_required = requires_official_government_domain(question)"` | — |
| [SRC-3AA6165B18-L000194](../../agents/research_guardrails.py#L194) | 194 | `"    # An LLM/intent planner can mark broad tasks as freshness-sensitive. In auto"` | — |
| [SRC-3AA6165B18-L000195](../../agents/research_guardrails.py#L195) | 195 | `"    # mode, enforce the strict date gate only when the user's question itself signals"` | — |
| [SRC-3AA6165B18-L000196](../../agents/research_guardrails.py#L196) | 196 | `"    # a time-sensitive fact; the explicit Latest mode always enforces it."` | — |
| [SRC-3AA6165B18-L000197](../../agents/research_guardrails.py#L197) | 197 | `"    explicit_current_request = detect_freshness(question)"` | — |
| [SRC-3AA6165B18-L000198](../../agents/research_guardrails.py#L198) | 198 | `"    freshness_required = ("` | — |
| [SRC-3AA6165B18-L000199](../../agents/research_guardrails.py#L199) | 199 | `"        (clean_mode == \"latest\" or ("` | — |
| [SRC-3AA6165B18-L000200](../../agents/research_guardrails.py#L200) | 200 | `"            plan.get(\"freshness\") == \"current\" and explicit_current_request"` | — |
| [SRC-3AA6165B18-L000201](../../agents/research_guardrails.py#L201) | 201 | `"        ))"` | — |
| [SRC-3AA6165B18-L000202](../../agents/research_guardrails.py#L202) | 202 | `"        and not _is_navigation_request(question)"` | — |
| [SRC-3AA6165B18-L000203](../../agents/research_guardrails.py#L203) | 203 | `"    )"` | — |
| [SRC-3AA6165B18-L000204](../../agents/research_guardrails.py#L204) | 204 | `"    social_required = clean_mode == \"social\""` | — |
| [SRC-3AA6165B18-L000205](../../agents/research_guardrails.py#L205) | 205 | `"    retained: list[dict[str, Any]] = []"` | — |
| [SRC-3AA6165B18-L000206](../../agents/research_guardrails.py#L206) | 206 | `"    rejected: dict[str, int] = {}"` | — |
| [SRC-3AA6165B18-L000207](../../agents/research_guardrails.py#L207) | 207 | `"    reasons: list[dict[str, str]] = []"` | — |
| [SRC-3AA6165B18-L000208](../../agents/research_guardrails.py#L208) | 208 | `""` | — |
| [SRC-3AA6165B18-L000209](../../agents/research_guardrails.py#L209) | 209 | `"    def reject(reason: str, source: dict[str, Any]) -> None:"` | — |
| [SRC-3AA6165B18-L000210](../../agents/research_guardrails.py#L210) | 210 | `"        rejected[reason] = rejected.get(reason, 0) + 1"` | — |
| [SRC-3AA6165B18-L000211](../../agents/research_guardrails.py#L211) | 211 | `"        reasons.append({"` | — |
| [SRC-3AA6165B18-L000212](../../agents/research_guardrails.py#L212) | 212 | `"            \"reason\": reason,"` | — |
| [SRC-3AA6165B18-L000213](../../agents/research_guardrails.py#L213) | 213 | `"            \"url\": str(source.get(\"url\") or \"\")[:2048],"` | — |
| [SRC-3AA6165B18-L000214](../../agents/research_guardrails.py#L214) | 214 | `"        })"` | — |
| [SRC-3AA6165B18-L000215](../../agents/research_guardrails.py#L215) | 215 | `""` | — |
| [SRC-3AA6165B18-L000216](../../agents/research_guardrails.py#L216) | 216 | `"    for candidate in (sources if isinstance(sources, list) else []):"` | — |
| [SRC-3AA6165B18-L000217](../../agents/research_guardrails.py#L217) | 217 | `"        if not isinstance(candidate, dict):"` | — |
| [SRC-3AA6165B18-L000218](../../agents/research_guardrails.py#L218) | 218 | `"            rejected[\"malformed_candidate\"] = rejected.get(\"malformed_candidate\", 0) + 1"` | — |
| [SRC-3AA6165B18-L000219](../../agents/research_guardrails.py#L219) | 219 | `"            reasons.append({\"reason\": \"malformed_candidate\", \"url\": \"\"})"` | — |
| [SRC-3AA6165B18-L000220](../../agents/research_guardrails.py#L220) | 220 | `"            continue"` | — |
| [SRC-3AA6165B18-L000221](../../agents/research_guardrails.py#L221) | 221 | `"        source = dict(candidate)"` | — |
| [SRC-3AA6165B18-L000222](../../agents/research_guardrails.py#L222) | 222 | `"        if official_required and not _is_government_domain(source.get(\"url\")):"` | — |
| [SRC-3AA6165B18-L000223](../../agents/research_guardrails.py#L223) | 223 | `"            reject(\"not_an_official_government_domain\", source)"` | — |
| [SRC-3AA6165B18-L000224](../../agents/research_guardrails.py#L224) | 224 | `"            continue"` | — |
| [SRC-3AA6165B18-L000225](../../agents/research_guardrails.py#L225) | 225 | `"        if social_required and not is_social_platform_url(source.get(\"url\")):"` | — |
| [SRC-3AA6165B18-L000226](../../agents/research_guardrails.py#L226) | 226 | `"            reject(\"not_a_social_platform_source\", source)"` | — |
| [SRC-3AA6165B18-L000227](../../agents/research_guardrails.py#L227) | 227 | `"            continue"` | — |
| [SRC-3AA6165B18-L000228](../../agents/research_guardrails.py#L228) | 228 | `"        if freshness_required:"` | — |
| [SRC-3AA6165B18-L000229](../../agents/research_guardrails.py#L229) | 229 | `"            freshness = assess_current_source(source, now=now)"` | — |
| [SRC-3AA6165B18-L000230](../../agents/research_guardrails.py#L230) | 230 | `"            source[\"current_evidence_assessment\"] = freshness"` | — |
| [SRC-3AA6165B18-L000231](../../agents/research_guardrails.py#L231) | 231 | `"            if not freshness[\"eligible\"]:"` | — |
| [SRC-3AA6165B18-L000232](../../agents/research_guardrails.py#L232) | 232 | `"                reject(str(freshness[\"status\"]), source)"` | — |
| [SRC-3AA6165B18-L000233](../../agents/research_guardrails.py#L233) | 233 | `"                continue"` | — |
| [SRC-3AA6165B18-L000234](../../agents/research_guardrails.py#L234) | 234 | `"        if social_required or bool(plan.get(\"social_focus\")):"` | — |
| [SRC-3AA6165B18-L000235](../../agents/research_guardrails.py#L235) | 235 | `"            source.update(classify_social_source(source))"` | — |
| [SRC-3AA6165B18-L000236](../../agents/research_guardrails.py#L236) | 236 | `"        retained.append(source)"` | — |
| [SRC-3AA6165B18-L000237](../../agents/research_guardrails.py#L237) | 237 | `""` | — |
| [SRC-3AA6165B18-L000238](../../agents/research_guardrails.py#L238) | 238 | `"    status = \"passed\" if not rejected else \"filtered\""` | — |
| [SRC-3AA6165B18-L000239](../../agents/research_guardrails.py#L239) | 239 | `"    if freshness_required and retained:"` | — |
| [SRC-3AA6165B18-L000240](../../agents/research_guardrails.py#L240) | 240 | `"        current_status = \"eligible_recent_read_pages_only\""` | — |
| [SRC-3AA6165B18-L000241](../../agents/research_guardrails.py#L241) | 241 | `"    elif freshness_required:"` | — |
| [SRC-3AA6165B18-L000242](../../agents/research_guardrails.py#L242) | 242 | `"        current_status = \"no_current_eligible_evidence\""` | — |
| [SRC-3AA6165B18-L000243](../../agents/research_guardrails.py#L243) | 243 | `"    else:"` | — |
| [SRC-3AA6165B18-L000244](../../agents/research_guardrails.py#L244) | 244 | `"        current_status = \"not_required\""` | — |
| [SRC-3AA6165B18-L000245](../../agents/research_guardrails.py#L245) | 245 | `"    summary = {"` | — |
| [SRC-3AA6165B18-L000246](../../agents/research_guardrails.py#L246) | 246 | `"        \"status\": status,"` | — |
| [SRC-3AA6165B18-L000247](../../agents/research_guardrails.py#L247) | 247 | `"        \"input_sources\": len(sources) if isinstance(sources, list) else 0,"` | — |
| [SRC-3AA6165B18-L000248](../../agents/research_guardrails.py#L248) | 248 | `"        \"accepted_sources\": len(retained),"` | — |
| [SRC-3AA6165B18-L000249](../../agents/research_guardrails.py#L249) | 249 | `"        \"rejected_sources\": sum(rejected.values()),"` | — |
| [SRC-3AA6165B18-L000250](../../agents/research_guardrails.py#L250) | 250 | `"        \"rejection_counts\": rejected,"` | — |
| [SRC-3AA6165B18-L000251](../../agents/research_guardrails.py#L251) | 251 | `"        \"rejection_details\": reasons[:20],"` | — |
| [SRC-3AA6165B18-L000252](../../agents/research_guardrails.py#L252) | 252 | `"        \"official_government_domain_required\": official_required,"` | — |
| [SRC-3AA6165B18-L000253](../../agents/research_guardrails.py#L253) | 253 | `"        \"official_domain_policy\": ("` | — |
| [SRC-3AA6165B18-L000254](../../agents/research_guardrails.py#L254) | 254 | `"            \"government-domain candidate only; organization ownership is not independently verified\""` | — |
| [SRC-3AA6165B18-L000255](../../agents/research_guardrails.py#L255) | 255 | `"            if official_required else \"not_required\""` | — |
| [SRC-3AA6165B18-L000256](../../agents/research_guardrails.py#L256) | 256 | `"        ),"` | — |
| [SRC-3AA6165B18-L000257](../../agents/research_guardrails.py#L257) | 257 | `"        \"current_evidence_required\": freshness_required,"` | — |
| [SRC-3AA6165B18-L000258](../../agents/research_guardrails.py#L258) | 258 | `"        \"current_evidence_status\": current_status,"` | — |
| [SRC-3AA6165B18-L000259](../../agents/research_guardrails.py#L259) | 259 | `"        \"current_evidence_max_age_days\": _CURRENT_EVIDENCE_MAX_AGE_DAYS if freshness_required else None,"` | — |
| [SRC-3AA6165B18-L000260](../../agents/research_guardrails.py#L260) | 260 | `"        \"social_platform_only\": social_required,"` | — |
| [SRC-3AA6165B18-L000261](../../agents/research_guardrails.py#L261) | 261 | `"        \"interpretation\": \"retrieval guardrail only; passing is not proof of claim correctness\","` | — |
| [SRC-3AA6165B18-L000262](../../agents/research_guardrails.py#L262) | 262 | `"    }"` | — |
| [SRC-3AA6165B18-L000263](../../agents/research_guardrails.py#L263) | 263 | `"    return retained, summary"` | — |
## الوكيل والمنطق

### FILE-1A2E47C5FA — [agents/retrieval_tool.py](../../agents/retrieval_tool.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1A2E47C5FA-L000001](../../agents/retrieval_tool.py#L1) | 1 | `"\"\"\"Retrieval-as-a-Tool for Omarai (agentic RAG primitive)."` | — |
| [SRC-1A2E47C5FA-L000002](../../agents/retrieval_tool.py#L2) | 2 | `""` | — |
| [SRC-1A2E47C5FA-L000003](../../agents/retrieval_tool.py#L3) | 3 | `"Instead of a fixed search→context→answer pipe, the reasoner calls this tool"` | — |
| [SRC-1A2E47C5FA-L000004](../../agents/retrieval_tool.py#L4) | 4 | `"when it decides evidence is needed. Supports multi-hop refinement and"` | — |
| [SRC-1A2E47C5FA-L000005](../../agents/retrieval_tool.py#L5) | 5 | `"dynamic source-class hints (web \| academic \| mixed)."` | — |
| [SRC-1A2E47C5FA-L000006](../../agents/retrieval_tool.py#L6) | 6 | `""` | — |
| [SRC-1A2E47C5FA-L000007](../../agents/retrieval_tool.py#L7) | 7 | `"Does not bypass SSRF/URL/relevance filters — those stay in the caller's path."` | — |
| [SRC-1A2E47C5FA-L000008](../../agents/retrieval_tool.py#L8) | 8 | `"\"\"\""` | — |
| [SRC-1A2E47C5FA-L000009](../../agents/retrieval_tool.py#L9) | 9 | `"from __future__ import annotations"` | — |
| [SRC-1A2E47C5FA-L000010](../../agents/retrieval_tool.py#L10) | 10 | `""` | — |
| [SRC-1A2E47C5FA-L000011](../../agents/retrieval_tool.py#L11) | 11 | `"import re"` | — |
| [SRC-1A2E47C5FA-L000012](../../agents/retrieval_tool.py#L12) | 12 | `"from dataclasses import asdict, dataclass, field"` | — |
| [SRC-1A2E47C5FA-L000013](../../agents/retrieval_tool.py#L13) | 13 | `"from typing import Any, Callable"` | — |
| [SRC-1A2E47C5FA-L000014](../../agents/retrieval_tool.py#L14) | 14 | `"from urllib.parse import urlparse"` | — |
| [SRC-1A2E47C5FA-L000015](../../agents/retrieval_tool.py#L15) | 15 | `""` | — |
| [SRC-1A2E47C5FA-L000016](../../agents/retrieval_tool.py#L16) | 16 | `"RetrieveFn = Callable[[str], list[dict[str, Any]]]"` | — |
| [SRC-1A2E47C5FA-L000017](../../agents/retrieval_tool.py#L17) | 17 | `""` | — |
| [SRC-1A2E47C5FA-L000018](../../agents/retrieval_tool.py#L18) | 18 | `"_TOKEN = re.compile(r\"[a-z0-9]+\|[\\u0600-\\u06FF]+\", re.I)"` | — |
| [SRC-1A2E47C5FA-L000019](../../agents/retrieval_tool.py#L19) | 19 | `""` | — |
| [SRC-1A2E47C5FA-L000020](../../agents/retrieval_tool.py#L20) | 20 | `"ACADEMIC_MARKERS = ("` | — |
| [SRC-1A2E47C5FA-L000021](../../agents/retrieval_tool.py#L21) | 21 | `"    \"دراسة\", \"بحث\", \"ورقة\", \"paper\", \"arxiv\", \"doi\", \"journal\", \"peer\","` | — |
| [SRC-1A2E47C5FA-L000022](../../agents/retrieval_tool.py#L22) | 22 | `"    \"systematic\", \"academic\", \"علمي\", \"أكاديمي\", \"منهجية\","` | — |
| [SRC-1A2E47C5FA-L000023](../../agents/retrieval_tool.py#L23) | 23 | `")"` | — |
| [SRC-1A2E47C5FA-L000024](../../agents/retrieval_tool.py#L24) | 24 | `""` | — |
| [SRC-1A2E47C5FA-L000025](../../agents/retrieval_tool.py#L25) | 25 | `""` | — |
| [SRC-1A2E47C5FA-L000026](../../agents/retrieval_tool.py#L26) | 26 | `"@dataclass"` | — |
| [SRC-1A2E47C5FA-L000027](../../agents/retrieval_tool.py#L27) | 27 | `"class RetrievalObservation:"` | — |
| [SRC-1A2E47C5FA-L000028](../../agents/retrieval_tool.py#L28) | 28 | `"    query: str"` | — |
| [SRC-1A2E47C5FA-L000029](../../agents/retrieval_tool.py#L29) | 29 | `"    results: list[dict[str, Any]]"` | — |
| [SRC-1A2E47C5FA-L000030](../../agents/retrieval_tool.py#L30) | 30 | `"    result_count: int"` | — |
| [SRC-1A2E47C5FA-L000031](../../agents/retrieval_tool.py#L31) | 31 | `"    unique_domains: int"` | — |
| [SRC-1A2E47C5FA-L000032](../../agents/retrieval_tool.py#L32) | 32 | `"    sufficiency: str  # none \| thin \| adequate \| rich"` | — |
| [SRC-1A2E47C5FA-L000033](../../agents/retrieval_tool.py#L33) | 33 | `"    source_class_hint: str = \"mixed\""` | — |
| [SRC-1A2E47C5FA-L000034](../../agents/retrieval_tool.py#L34) | 34 | `"    suggested_next_query: str = \"\""` | — |
| [SRC-1A2E47C5FA-L000035](../../agents/retrieval_tool.py#L35) | 35 | `"    reason: str = \"\""` | — |
| [SRC-1A2E47C5FA-L000036](../../agents/retrieval_tool.py#L36) | 36 | `""` | — |
| [SRC-1A2E47C5FA-L000037](../../agents/retrieval_tool.py#L37) | 37 | `"    def to_dict(self) -> dict[str, Any]:"` | — |
| [SRC-1A2E47C5FA-L000038](../../agents/retrieval_tool.py#L38) | 38 | `"        d = asdict(self)"` | — |
| [SRC-1A2E47C5FA-L000039](../../agents/retrieval_tool.py#L39) | 39 | `"        d[\"results\"] = ["` | — |
| [SRC-1A2E47C5FA-L000040](../../agents/retrieval_tool.py#L40) | 40 | `"            {"` | — |
| [SRC-1A2E47C5FA-L000041](../../agents/retrieval_tool.py#L41) | 41 | `"                \"title\": r.get(\"title\"),"` | — |
| [SRC-1A2E47C5FA-L000042](../../agents/retrieval_tool.py#L42) | 42 | `"                \"url\": r.get(\"url\"),"` | — |
| [SRC-1A2E47C5FA-L000043](../../agents/retrieval_tool.py#L43) | 43 | `"                \"provider\": r.get(\"provider\"),"` | — |
| [SRC-1A2E47C5FA-L000044](../../agents/retrieval_tool.py#L44) | 44 | `"                \"snippet\": str(r.get(\"snippet\") or \"\")[:240],"` | — |
| [SRC-1A2E47C5FA-L000045](../../agents/retrieval_tool.py#L45) | 45 | `"            }"` | — |
| [SRC-1A2E47C5FA-L000046](../../agents/retrieval_tool.py#L46) | 46 | `"            for r in (self.results or [])[:8]"` | — |
| [SRC-1A2E47C5FA-L000047](../../agents/retrieval_tool.py#L47) | 47 | `"        ]"` | — |
| [SRC-1A2E47C5FA-L000048](../../agents/retrieval_tool.py#L48) | 48 | `"        return d"` | — |
| [SRC-1A2E47C5FA-L000049](../../agents/retrieval_tool.py#L49) | 49 | `""` | — |
| [SRC-1A2E47C5FA-L000050](../../agents/retrieval_tool.py#L50) | 50 | `""` | — |
| [SRC-1A2E47C5FA-L000051](../../agents/retrieval_tool.py#L51) | 51 | `"@dataclass"` | — |
| [SRC-1A2E47C5FA-L000052](../../agents/retrieval_tool.py#L52) | 52 | `"class RetrievalToolState:"` | — |
| [SRC-1A2E47C5FA-L000053](../../agents/retrieval_tool.py#L53) | 53 | `"    hops: list[RetrievalObservation] = field(default_factory=list)"` | — |
| [SRC-1A2E47C5FA-L000054](../../agents/retrieval_tool.py#L54) | 54 | `"    all_results: list[dict[str, Any]] = field(default_factory=list)"` | — |
| [SRC-1A2E47C5FA-L000055](../../agents/retrieval_tool.py#L55) | 55 | `""` | — |
| [SRC-1A2E47C5FA-L000056](../../agents/retrieval_tool.py#L56) | 56 | `"    @property"` | — |
| [SRC-1A2E47C5FA-L000057](../../agents/retrieval_tool.py#L57) | 57 | `"    def hop_count(self) -> int:"` | — |
| [SRC-1A2E47C5FA-L000058](../../agents/retrieval_tool.py#L58) | 58 | `"        return len(self.hops)"` | — |
| [SRC-1A2E47C5FA-L000059](../../agents/retrieval_tool.py#L59) | 59 | `""` | — |
| [SRC-1A2E47C5FA-L000060](../../agents/retrieval_tool.py#L60) | 60 | `"    def to_dict(self) -> dict[str, Any]:"` | — |
| [SRC-1A2E47C5FA-L000061](../../agents/retrieval_tool.py#L61) | 61 | `"        return {"` | — |
| [SRC-1A2E47C5FA-L000062](../../agents/retrieval_tool.py#L62) | 62 | `"            \"hop_count\": self.hop_count,"` | — |
| [SRC-1A2E47C5FA-L000063](../../agents/retrieval_tool.py#L63) | 63 | `"            \"result_count\": len(self.all_results),"` | — |
| [SRC-1A2E47C5FA-L000064](../../agents/retrieval_tool.py#L64) | 64 | `"            \"hops\": [h.to_dict() for h in self.hops],"` | — |
| [SRC-1A2E47C5FA-L000065](../../agents/retrieval_tool.py#L65) | 65 | `"            \"final_sufficiency\": self.hops[-1].sufficiency if self.hops else \"none\","` | — |
| [SRC-1A2E47C5FA-L000066](../../agents/retrieval_tool.py#L66) | 66 | `"        }"` | — |
| [SRC-1A2E47C5FA-L000067](../../agents/retrieval_tool.py#L67) | 67 | `""` | — |
| [SRC-1A2E47C5FA-L000068](../../agents/retrieval_tool.py#L68) | 68 | `""` | — |
| [SRC-1A2E47C5FA-L000069](../../agents/retrieval_tool.py#L69) | 69 | `"def _domains(results: list[dict[str, Any]]) -> set[str]:"` | — |
| [SRC-1A2E47C5FA-L000070](../../agents/retrieval_tool.py#L70) | 70 | `"    out: set[str] = set()"` | — |
| [SRC-1A2E47C5FA-L000071](../../agents/retrieval_tool.py#L71) | 71 | `"    for item in results or []:"` | — |
| [SRC-1A2E47C5FA-L000072](../../agents/retrieval_tool.py#L72) | 72 | `"        url = str(item.get(\"url\") or \"\")"` | — |
| [SRC-1A2E47C5FA-L000073](../../agents/retrieval_tool.py#L73) | 73 | `"        try:"` | — |
| [SRC-1A2E47C5FA-L000074](../../agents/retrieval_tool.py#L74) | 74 | `"            host = (urlparse(url).hostname or \"\").lower().removeprefix(\"www.\")"` | — |
| [SRC-1A2E47C5FA-L000075](../../agents/retrieval_tool.py#L75) | 75 | `"            if host:"` | — |
| [SRC-1A2E47C5FA-L000076](../../agents/retrieval_tool.py#L76) | 76 | `"                out.add(host)"` | — |
| [SRC-1A2E47C5FA-L000077](../../agents/retrieval_tool.py#L77) | 77 | `"        except Exception:"` | — |
| [SRC-1A2E47C5FA-L000078](../../agents/retrieval_tool.py#L78) | 78 | `"            continue"` | — |
| [SRC-1A2E47C5FA-L000079](../../agents/retrieval_tool.py#L79) | 79 | `"    return out"` | — |
| [SRC-1A2E47C5FA-L000080](../../agents/retrieval_tool.py#L80) | 80 | `""` | — |
| [SRC-1A2E47C5FA-L000081](../../agents/retrieval_tool.py#L81) | 81 | `""` | — |
| [SRC-1A2E47C5FA-L000082](../../agents/retrieval_tool.py#L82) | 82 | `"def score_sufficiency(results: list[dict[str, Any]]) -> str:"` | — |
| [SRC-1A2E47C5FA-L000083](../../agents/retrieval_tool.py#L83) | 83 | `"    n = len(results or [])"` | — |
| [SRC-1A2E47C5FA-L000084](../../agents/retrieval_tool.py#L84) | 84 | `"    d = len(_domains(results))"` | — |
| [SRC-1A2E47C5FA-L000085](../../agents/retrieval_tool.py#L85) | 85 | `"    if n == 0:"` | — |
| [SRC-1A2E47C5FA-L000086](../../agents/retrieval_tool.py#L86) | 86 | `"        return \"none\""` | — |
| [SRC-1A2E47C5FA-L000087](../../agents/retrieval_tool.py#L87) | 87 | `"    if n < 2 or d < 1:"` | — |
| [SRC-1A2E47C5FA-L000088](../../agents/retrieval_tool.py#L88) | 88 | `"        return \"thin\""` | — |
| [SRC-1A2E47C5FA-L000089](../../agents/retrieval_tool.py#L89) | 89 | `"    if n >= 5 and d >= 3:"` | — |
| [SRC-1A2E47C5FA-L000090](../../agents/retrieval_tool.py#L90) | 90 | `"        return \"rich\""` | — |
| [SRC-1A2E47C5FA-L000091](../../agents/retrieval_tool.py#L91) | 91 | `"    return \"adequate\""` | — |
| [SRC-1A2E47C5FA-L000092](../../agents/retrieval_tool.py#L92) | 92 | `""` | — |
| [SRC-1A2E47C5FA-L000093](../../agents/retrieval_tool.py#L93) | 93 | `""` | — |
| [SRC-1A2E47C5FA-L000094](../../agents/retrieval_tool.py#L94) | 94 | `"def infer_source_class_hint(query: str) -> str:"` | — |
| [SRC-1A2E47C5FA-L000095](../../agents/retrieval_tool.py#L95) | 95 | `"    q = (query or \"\").casefold()"` | — |
| [SRC-1A2E47C5FA-L000096](../../agents/retrieval_tool.py#L96) | 96 | `"    if any(m in q for m in ACADEMIC_MARKERS):"` | — |
| [SRC-1A2E47C5FA-L000097](../../agents/retrieval_tool.py#L97) | 97 | `"        return \"academic\""` | — |
| [SRC-1A2E47C5FA-L000098](../../agents/retrieval_tool.py#L98) | 98 | `"    return \"web\""` | — |
| [SRC-1A2E47C5FA-L000099](../../agents/retrieval_tool.py#L99) | 99 | `""` | — |
| [SRC-1A2E47C5FA-L000100](../../agents/retrieval_tool.py#L100) | 100 | `""` | — |
| [SRC-1A2E47C5FA-L000101](../../agents/retrieval_tool.py#L101) | 101 | `"def suggest_refined_query(query: str, observation: RetrievalObservation) -> str:"` | — |
| [SRC-1A2E47C5FA-L000102](../../agents/retrieval_tool.py#L102) | 102 | `"    base = (query or \"\").strip()"` | — |
| [SRC-1A2E47C5FA-L000103](../../agents/retrieval_tool.py#L103) | 103 | `"    if not base:"` | — |
| [SRC-1A2E47C5FA-L000104](../../agents/retrieval_tool.py#L104) | 104 | `"        return \"\""` | — |
| [SRC-1A2E47C5FA-L000105](../../agents/retrieval_tool.py#L105) | 105 | `"    if observation.sufficiency == \"none\":"` | — |
| [SRC-1A2E47C5FA-L000106](../../agents/retrieval_tool.py#L106) | 106 | `"        return f\"{base} مصادر موثوقة\""` | — |
| [SRC-1A2E47C5FA-L000107](../../agents/retrieval_tool.py#L107) | 107 | `"    if observation.sufficiency == \"thin\":"` | — |
| [SRC-1A2E47C5FA-L000108](../../agents/retrieval_tool.py#L108) | 108 | `"        if observation.source_class_hint == \"academic\":"` | — |
| [SRC-1A2E47C5FA-L000109](../../agents/retrieval_tool.py#L109) | 109 | `"            return f\"{base} review paper evidence\""` | — |
| [SRC-1A2E47C5FA-L000110](../../agents/retrieval_tool.py#L110) | 110 | `"        return f\"{base} تقرير رسمي إحصاءات\""` | — |
| [SRC-1A2E47C5FA-L000111](../../agents/retrieval_tool.py#L111) | 111 | `"    return \"\""` | — |
| [SRC-1A2E47C5FA-L000112](../../agents/retrieval_tool.py#L112) | 112 | `""` | — |
| [SRC-1A2E47C5FA-L000113](../../agents/retrieval_tool.py#L113) | 113 | `""` | — |
| [SRC-1A2E47C5FA-L000114](../../agents/retrieval_tool.py#L114) | 114 | `"class RetrievalTool:"` | — |
| [SRC-1A2E47C5FA-L000115](../../agents/retrieval_tool.py#L115) | 115 | `"    \"\"\"Callable retrieval tool for the ReAct loop.\"\"\""` | — |
| [SRC-1A2E47C5FA-L000116](../../agents/retrieval_tool.py#L116) | 116 | `""` | — |
| [SRC-1A2E47C5FA-L000117](../../agents/retrieval_tool.py#L117) | 117 | `"    def __init__(self, retrieve_fn: RetrieveFn, *, max_hops: int = 3) -> None:"` | — |
| [SRC-1A2E47C5FA-L000118](../../agents/retrieval_tool.py#L118) | 118 | `"        self.retrieve_fn = retrieve_fn"` | — |
| [SRC-1A2E47C5FA-L000119](../../agents/retrieval_tool.py#L119) | 119 | `"        self.max_hops = max(1, min(int(max_hops), 5))"` | — |
| [SRC-1A2E47C5FA-L000120](../../agents/retrieval_tool.py#L120) | 120 | `""` | — |
| [SRC-1A2E47C5FA-L000121](../../agents/retrieval_tool.py#L121) | 121 | `"    def once(self, query: str, *, aspect: str = \"\") -> RetrievalObservation:"` | — |
| [SRC-1A2E47C5FA-L000122](../../agents/retrieval_tool.py#L122) | 122 | `"        q = (query or \"\").strip()"` | — |
| [SRC-1A2E47C5FA-L000123](../../agents/retrieval_tool.py#L123) | 123 | `"        if aspect and aspect not in q:"` | — |
| [SRC-1A2E47C5FA-L000124](../../agents/retrieval_tool.py#L124) | 124 | `"            q = f\"{q} {aspect}\".strip()"` | — |
| [SRC-1A2E47C5FA-L000125](../../agents/retrieval_tool.py#L125) | 125 | `"        hint = infer_source_class_hint(q)"` | — |
| [SRC-1A2E47C5FA-L000126](../../agents/retrieval_tool.py#L126) | 126 | `"        try:"` | — |
| [SRC-1A2E47C5FA-L000127](../../agents/retrieval_tool.py#L127) | 127 | `"            results = list(self.retrieve_fn(q) or [])"` | — |
| [SRC-1A2E47C5FA-L000128](../../agents/retrieval_tool.py#L128) | 128 | `"        except Exception as exc:  # noqa: BLE001"` | — |
| [SRC-1A2E47C5FA-L000129](../../agents/retrieval_tool.py#L129) | 129 | `"            return RetrievalObservation("` | — |
| [SRC-1A2E47C5FA-L000130](../../agents/retrieval_tool.py#L130) | 130 | `"                query=q,"` | — |
| [SRC-1A2E47C5FA-L000131](../../agents/retrieval_tool.py#L131) | 131 | `"                results=[],"` | — |
| [SRC-1A2E47C5FA-L000132](../../agents/retrieval_tool.py#L132) | 132 | `"                result_count=0,"` | — |
| [SRC-1A2E47C5FA-L000133](../../agents/retrieval_tool.py#L133) | 133 | `"                unique_domains=0,"` | — |
| [SRC-1A2E47C5FA-L000134](../../agents/retrieval_tool.py#L134) | 134 | `"                sufficiency=\"none\","` | — |
| [SRC-1A2E47C5FA-L000135](../../agents/retrieval_tool.py#L135) | 135 | `"                source_class_hint=hint,"` | — |
| [SRC-1A2E47C5FA-L000136](../../agents/retrieval_tool.py#L136) | 136 | `"                reason=f\"retrieve_error:{type(exc).__name__}\","` | — |
| [SRC-1A2E47C5FA-L000137](../../agents/retrieval_tool.py#L137) | 137 | `"            )"` | — |
| [SRC-1A2E47C5FA-L000138](../../agents/retrieval_tool.py#L138) | 138 | `"        seen: set[str] = set()"` | — |
| [SRC-1A2E47C5FA-L000139](../../agents/retrieval_tool.py#L139) | 139 | `"        unique: list[dict[str, Any]] = []"` | — |
| [SRC-1A2E47C5FA-L000140](../../agents/retrieval_tool.py#L140) | 140 | `"        for item in results:"` | — |
| [SRC-1A2E47C5FA-L000141](../../agents/retrieval_tool.py#L141) | 141 | `"            if not isinstance(item, dict):"` | — |
| [SRC-1A2E47C5FA-L000142](../../agents/retrieval_tool.py#L142) | 142 | `"                continue"` | — |
| [SRC-1A2E47C5FA-L000143](../../agents/retrieval_tool.py#L143) | 143 | `"            url = str(item.get(\"url\") or \"\").split(\"#\", 1)[0].rstrip(\"/\")"` | — |
| [SRC-1A2E47C5FA-L000144](../../agents/retrieval_tool.py#L144) | 144 | `"            if not url or url in seen:"` | — |
| [SRC-1A2E47C5FA-L000145](../../agents/retrieval_tool.py#L145) | 145 | `"                continue"` | — |
| [SRC-1A2E47C5FA-L000146](../../agents/retrieval_tool.py#L146) | 146 | `"            seen.add(url)"` | — |
| [SRC-1A2E47C5FA-L000147](../../agents/retrieval_tool.py#L147) | 147 | `"            unique.append(item)"` | — |
| [SRC-1A2E47C5FA-L000148](../../agents/retrieval_tool.py#L148) | 148 | `"        obs = RetrievalObservation("` | — |
| [SRC-1A2E47C5FA-L000149](../../agents/retrieval_tool.py#L149) | 149 | `"            query=q,"` | — |
| [SRC-1A2E47C5FA-L000150](../../agents/retrieval_tool.py#L150) | 150 | `"            results=unique,"` | — |
| [SRC-1A2E47C5FA-L000151](../../agents/retrieval_tool.py#L151) | 151 | `"            result_count=len(unique),"` | — |
| [SRC-1A2E47C5FA-L000152](../../agents/retrieval_tool.py#L152) | 152 | `"            unique_domains=len(_domains(unique)),"` | — |
| [SRC-1A2E47C5FA-L000153](../../agents/retrieval_tool.py#L153) | 153 | `"            sufficiency=score_sufficiency(unique),"` | — |
| [SRC-1A2E47C5FA-L000154](../../agents/retrieval_tool.py#L154) | 154 | `"            source_class_hint=hint,"` | — |
| [SRC-1A2E47C5FA-L000155](../../agents/retrieval_tool.py#L155) | 155 | `"            reason=\"ok\","` | — |
| [SRC-1A2E47C5FA-L000156](../../agents/retrieval_tool.py#L156) | 156 | `"        )"` | — |
| [SRC-1A2E47C5FA-L000157](../../agents/retrieval_tool.py#L157) | 157 | `"        obs.suggested_next_query = suggest_refined_query(query, obs)"` | — |
| [SRC-1A2E47C5FA-L000158](../../agents/retrieval_tool.py#L158) | 158 | `"        return obs"` | — |
| [SRC-1A2E47C5FA-L000159](../../agents/retrieval_tool.py#L159) | 159 | `""` | — |
| [SRC-1A2E47C5FA-L000160](../../agents/retrieval_tool.py#L160) | 160 | `"    def run_until_sufficient("` | — |
| [SRC-1A2E47C5FA-L000161](../../agents/retrieval_tool.py#L161) | 161 | `"        self,"` | — |
| [SRC-1A2E47C5FA-L000162](../../agents/retrieval_tool.py#L162) | 162 | `"        seed_query: str,"` | — |
| [SRC-1A2E47C5FA-L000163](../../agents/retrieval_tool.py#L163) | 163 | `"        *,"` | — |
| [SRC-1A2E47C5FA-L000164](../../agents/retrieval_tool.py#L164) | 164 | `"        aspect: str = \"\","` | — |
| [SRC-1A2E47C5FA-L000165](../../agents/retrieval_tool.py#L165) | 165 | `"        extra_queries: list[str] \| None = None,"` | — |
| [SRC-1A2E47C5FA-L000166](../../agents/retrieval_tool.py#L166) | 166 | `"    ) -> RetrievalToolState:"` | — |
| [SRC-1A2E47C5FA-L000167](../../agents/retrieval_tool.py#L167) | 167 | `"        state = RetrievalToolState()"` | — |
| [SRC-1A2E47C5FA-L000168](../../agents/retrieval_tool.py#L168) | 168 | `"        queue: list[str] = []"` | — |
| [SRC-1A2E47C5FA-L000169](../../agents/retrieval_tool.py#L169) | 169 | `"        if seed_query.strip():"` | — |
| [SRC-1A2E47C5FA-L000170](../../agents/retrieval_tool.py#L170) | 170 | `"            queue.append(seed_query.strip())"` | — |
| [SRC-1A2E47C5FA-L000171](../../agents/retrieval_tool.py#L171) | 171 | `"        for q in extra_queries or []:"` | — |
| [SRC-1A2E47C5FA-L000172](../../agents/retrieval_tool.py#L172) | 172 | `"            if isinstance(q, str) and q.strip() and q.strip() not in queue:"` | — |
| [SRC-1A2E47C5FA-L000173](../../agents/retrieval_tool.py#L173) | 173 | `"                queue.append(q.strip())"` | — |
| [SRC-1A2E47C5FA-L000174](../../agents/retrieval_tool.py#L174) | 174 | `"        seen_q: set[str] = set()"` | — |
| [SRC-1A2E47C5FA-L000175](../../agents/retrieval_tool.py#L175) | 175 | `"        while queue and state.hop_count < self.max_hops:"` | — |
| [SRC-1A2E47C5FA-L000176](../../agents/retrieval_tool.py#L176) | 176 | `"            q = queue.pop(0)"` | — |
| [SRC-1A2E47C5FA-L000177](../../agents/retrieval_tool.py#L177) | 177 | `"            key = q.casefold()"` | — |
| [SRC-1A2E47C5FA-L000178](../../agents/retrieval_tool.py#L178) | 178 | `"            if key in seen_q:"` | — |
| [SRC-1A2E47C5FA-L000179](../../agents/retrieval_tool.py#L179) | 179 | `"                continue"` | — |
| [SRC-1A2E47C5FA-L000180](../../agents/retrieval_tool.py#L180) | 180 | `"            seen_q.add(key)"` | — |
| [SRC-1A2E47C5FA-L000181](../../agents/retrieval_tool.py#L181) | 181 | `"            obs = self.once(q, aspect=aspect if state.hop_count == 0 else \"\")"` | — |
| [SRC-1A2E47C5FA-L000182](../../agents/retrieval_tool.py#L182) | 182 | `"            state.hops.append(obs)"` | — |
| [SRC-1A2E47C5FA-L000183](../../agents/retrieval_tool.py#L183) | 183 | `"            for item in obs.results:"` | — |
| [SRC-1A2E47C5FA-L000184](../../agents/retrieval_tool.py#L184) | 184 | `"                url = str(item.get(\"url\") or \"\")"` | — |
| [SRC-1A2E47C5FA-L000185](../../agents/retrieval_tool.py#L185) | 185 | `"                if url and not any(str(x.get(\"url\") or \"\") == url for x in state.all_results):"` | — |
| [SRC-1A2E47C5FA-L000186](../../agents/retrieval_tool.py#L186) | 186 | `"                    state.all_results.append(item)"` | — |
| [SRC-1A2E47C5FA-L000187](../../agents/retrieval_tool.py#L187) | 187 | `"            if obs.sufficiency in {\"adequate\", \"rich\"} and state.hop_count >= 1:"` | — |
| [SRC-1A2E47C5FA-L000188](../../agents/retrieval_tool.py#L188) | 188 | `"                if len(_domains(state.all_results)) >= 2 or obs.sufficiency == \"rich\":"` | — |
| [SRC-1A2E47C5FA-L000189](../../agents/retrieval_tool.py#L189) | 189 | `"                    break"` | — |
| [SRC-1A2E47C5FA-L000190](../../agents/retrieval_tool.py#L190) | 190 | `"            if obs.suggested_next_query and obs.suggested_next_query.casefold() not in seen_q:"` | — |
| [SRC-1A2E47C5FA-L000191](../../agents/retrieval_tool.py#L191) | 191 | `"                queue.append(obs.suggested_next_query)"` | — |
| [SRC-1A2E47C5FA-L000192](../../agents/retrieval_tool.py#L192) | 192 | `"        return state"` | — |
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

### FILE-8A5C31AD7D — [agents/specialist_agents.py](../../agents/specialist_agents.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-8A5C31AD7D-L000001](../../agents/specialist_agents.py#L1) | 1 | `"\"\"\"Specialist agents inside Omarai agentic RAG pipeline."` | — |
| [SRC-8A5C31AD7D-L000002](../../agents/specialist_agents.py#L2) | 2 | `""` | — |
| [SRC-8A5C31AD7D-L000003](../../agents/specialist_agents.py#L3) | 3 | `"- QueryReformulator: natural language → effective search queries + aspects"` | — |
| [SRC-8A5C31AD7D-L000004](../../agents/specialist_agents.py#L4) | 4 | `"- IterativeRetriever: multi-hop retrieval tool use"` | — |
| [SRC-8A5C31AD7D-L000005](../../agents/specialist_agents.py#L5) | 5 | `"- HallucinationGuard: claim vs evidence verification"` | — |
| [SRC-8A5C31AD7D-L000006](../../agents/specialist_agents.py#L6) | 6 | `"- FinalComposer: fluent answer with mandatory citations / abstention"` | — |
| [SRC-8A5C31AD7D-L000007](../../agents/specialist_agents.py#L7) | 7 | `"\"\"\""` | — |
| [SRC-8A5C31AD7D-L000008](../../agents/specialist_agents.py#L8) | 8 | `"from __future__ import annotations"` | — |
| [SRC-8A5C31AD7D-L000009](../../agents/specialist_agents.py#L9) | 9 | `""` | — |
| [SRC-8A5C31AD7D-L000010](../../agents/specialist_agents.py#L10) | 10 | `"import re"` | — |
| [SRC-8A5C31AD7D-L000011](../../agents/specialist_agents.py#L11) | 11 | `"from typing import Any, Callable"` | — |
| [SRC-8A5C31AD7D-L000012](../../agents/specialist_agents.py#L12) | 12 | `""` | — |
| [SRC-8A5C31AD7D-L000013](../../agents/specialist_agents.py#L13) | 13 | `"from agents.memory_bank import MemoryBank, split_answer_into_claim_sentences"` | — |
| [SRC-8A5C31AD7D-L000014](../../agents/specialist_agents.py#L14) | 14 | `"from agents.retrieval_tool import RetrievalTool"` | — |
| [SRC-8A5C31AD7D-L000015](../../agents/specialist_agents.py#L15) | 15 | `""` | — |
| [SRC-8A5C31AD7D-L000016](../../agents/specialist_agents.py#L16) | 16 | `"RetrieveFn = Callable[[str], list[dict[str, Any]]]"` | — |
| [SRC-8A5C31AD7D-L000017](../../agents/specialist_agents.py#L17) | 17 | `""` | — |
| [SRC-8A5C31AD7D-L000018](../../agents/specialist_agents.py#L18) | 18 | `"try:"` | — |
| [SRC-8A5C31AD7D-L000019](../../agents/specialist_agents.py#L19) | 19 | `"    from agents.aspect_planning import extract_aspects, build_aspect_queries"` | — |
| [SRC-8A5C31AD7D-L000020](../../agents/specialist_agents.py#L20) | 20 | `"except Exception:  # pragma: no cover"` | — |
| [SRC-8A5C31AD7D-L000021](../../agents/specialist_agents.py#L21) | 21 | `"    def extract_aspects(question: str) -> list[str]:"` | — |
| [SRC-8A5C31AD7D-L000022](../../agents/specialist_agents.py#L22) | 22 | `"        return []"` | — |
| [SRC-8A5C31AD7D-L000023](../../agents/specialist_agents.py#L23) | 23 | `""` | — |
| [SRC-8A5C31AD7D-L000024](../../agents/specialist_agents.py#L24) | 24 | `"    def build_aspect_queries(topic: str, aspects: list[str], *, limit: int = 8) -> list[str]:"` | — |
| [SRC-8A5C31AD7D-L000025](../../agents/specialist_agents.py#L25) | 25 | `"        out = [topic] if topic else []"` | — |
| [SRC-8A5C31AD7D-L000026](../../agents/specialist_agents.py#L26) | 26 | `"        for a in aspects:"` | — |
| [SRC-8A5C31AD7D-L000027](../../agents/specialist_agents.py#L27) | 27 | `"            out.append(f\"{topic} {a}\".strip())"` | — |
| [SRC-8A5C31AD7D-L000028](../../agents/specialist_agents.py#L28) | 28 | `"        return out[:limit]"` | — |
| [SRC-8A5C31AD7D-L000029](../../agents/specialist_agents.py#L29) | 29 | `""` | — |
| [SRC-8A5C31AD7D-L000030](../../agents/specialist_agents.py#L30) | 30 | `""` | — |
| [SRC-8A5C31AD7D-L000031](../../agents/specialist_agents.py#L31) | 31 | `"class QueryReformulator:"` | — |
| [SRC-8A5C31AD7D-L000032](../../agents/specialist_agents.py#L32) | 32 | `"    def reformulate(self, question: str, *, topic_hint: str = \"\") -> dict[str, Any]:"` | — |
| [SRC-8A5C31AD7D-L000033](../../agents/specialist_agents.py#L33) | 33 | `"        q = re.sub(r\"\\s+\", \" \", (question or \"\").strip())"` | — |
| [SRC-8A5C31AD7D-L000034](../../agents/specialist_agents.py#L34) | 34 | `"        aspects = extract_aspects(q)"` | — |
| [SRC-8A5C31AD7D-L000035](../../agents/specialist_agents.py#L35) | 35 | `"        topic = topic_hint.strip() or q[:240]"` | — |
| [SRC-8A5C31AD7D-L000036](../../agents/specialist_agents.py#L36) | 36 | `"        queries = build_aspect_queries(topic, aspects, limit=6)"` | — |
| [SRC-8A5C31AD7D-L000037](../../agents/specialist_agents.py#L37) | 37 | `"        if not queries and q:"` | — |
| [SRC-8A5C31AD7D-L000038](../../agents/specialist_agents.py#L38) | 38 | `"            queries = [q[:240]]"` | — |
| [SRC-8A5C31AD7D-L000039](../../agents/specialist_agents.py#L39) | 39 | `"        probes = []"` | — |
| [SRC-8A5C31AD7D-L000040](../../agents/specialist_agents.py#L40) | 40 | `"        if q and \"مقارنة\" not in q and \"قارن\" not in q:"` | — |
| [SRC-8A5C31AD7D-L000041](../../agents/specialist_agents.py#L41) | 41 | `"            probes.append(f\"{topic} حقائق مصادر\")"` | — |
| [SRC-8A5C31AD7D-L000042](../../agents/specialist_agents.py#L42) | 42 | `"        return {"` | — |
| [SRC-8A5C31AD7D-L000043](../../agents/specialist_agents.py#L43) | 43 | `"            \"original\": q,"` | — |
| [SRC-8A5C31AD7D-L000044](../../agents/specialist_agents.py#L44) | 44 | `"            \"topic\": topic,"` | — |
| [SRC-8A5C31AD7D-L000045](../../agents/specialist_agents.py#L45) | 45 | `"            \"aspects\": aspects,"` | — |
| [SRC-8A5C31AD7D-L000046](../../agents/specialist_agents.py#L46) | 46 | `"            \"queries\": list(dict.fromkeys([x for x in queries + probes if x]))[:8],"` | — |
| [SRC-8A5C31AD7D-L000047](../../agents/specialist_agents.py#L47) | 47 | `"            \"needs_retrieval\": bool(queries),"` | — |
| [SRC-8A5C31AD7D-L000048](../../agents/specialist_agents.py#L48) | 48 | `"            \"agent\": \"QueryReformulator\","` | — |
| [SRC-8A5C31AD7D-L000049](../../agents/specialist_agents.py#L49) | 49 | `"        }"` | — |
| [SRC-8A5C31AD7D-L000050](../../agents/specialist_agents.py#L50) | 50 | `""` | — |
| [SRC-8A5C31AD7D-L000051](../../agents/specialist_agents.py#L51) | 51 | `""` | — |
| [SRC-8A5C31AD7D-L000052](../../agents/specialist_agents.py#L52) | 52 | `"class IterativeRetriever:"` | — |
| [SRC-8A5C31AD7D-L000053](../../agents/specialist_agents.py#L53) | 53 | `"    def __init__(self, retrieve_fn: RetrieveFn, *, max_hops: int = 3) -> None:"` | — |
| [SRC-8A5C31AD7D-L000054](../../agents/specialist_agents.py#L54) | 54 | `"        self.tool = RetrievalTool(retrieve_fn, max_hops=max_hops)"` | — |
| [SRC-8A5C31AD7D-L000055](../../agents/specialist_agents.py#L55) | 55 | `""` | — |
| [SRC-8A5C31AD7D-L000056](../../agents/specialist_agents.py#L56) | 56 | `"    def retrieve(self, queries: list[str], *, aspect: str = \"\") -> dict[str, Any]:"` | — |
| [SRC-8A5C31AD7D-L000057](../../agents/specialist_agents.py#L57) | 57 | `"        seed = queries[0] if queries else \"\""` | — |
| [SRC-8A5C31AD7D-L000058](../../agents/specialist_agents.py#L58) | 58 | `"        extra = queries[1:] if len(queries) > 1 else []"` | — |
| [SRC-8A5C31AD7D-L000059](../../agents/specialist_agents.py#L59) | 59 | `"        state = self.tool.run_until_sufficient(seed, aspect=aspect, extra_queries=extra)"` | — |
| [SRC-8A5C31AD7D-L000060](../../agents/specialist_agents.py#L60) | 60 | `"        return {"` | — |
| [SRC-8A5C31AD7D-L000061](../../agents/specialist_agents.py#L61) | 61 | `"            \"results\": state.all_results,"` | — |
| [SRC-8A5C31AD7D-L000062](../../agents/specialist_agents.py#L62) | 62 | `"            \"hop_count\": state.hop_count,"` | — |
| [SRC-8A5C31AD7D-L000063](../../agents/specialist_agents.py#L63) | 63 | `"            \"final_sufficiency\": state.to_dict()[\"final_sufficiency\"],"` | — |
| [SRC-8A5C31AD7D-L000064](../../agents/specialist_agents.py#L64) | 64 | `"            \"hops\": state.to_dict()[\"hops\"],"` | — |
| [SRC-8A5C31AD7D-L000065](../../agents/specialist_agents.py#L65) | 65 | `"            \"agent\": \"IterativeRetriever\","` | — |
| [SRC-8A5C31AD7D-L000066](../../agents/specialist_agents.py#L66) | 66 | `"        }"` | — |
| [SRC-8A5C31AD7D-L000067](../../agents/specialist_agents.py#L67) | 67 | `""` | — |
| [SRC-8A5C31AD7D-L000068](../../agents/specialist_agents.py#L68) | 68 | `""` | — |
| [SRC-8A5C31AD7D-L000069](../../agents/specialist_agents.py#L69) | 69 | `"class HallucinationGuard:"` | — |
| [SRC-8A5C31AD7D-L000070](../../agents/specialist_agents.py#L70) | 70 | `"    def __init__(self, *, min_support: float = 0.25) -> None:"` | — |
| [SRC-8A5C31AD7D-L000071](../../agents/specialist_agents.py#L71) | 71 | `"        self.min_support = min_support"` | — |
| [SRC-8A5C31AD7D-L000072](../../agents/specialist_agents.py#L72) | 72 | `""` | — |
| [SRC-8A5C31AD7D-L000073](../../agents/specialist_agents.py#L73) | 73 | `"    def verify_answer("` | — |
| [SRC-8A5C31AD7D-L000074](../../agents/specialist_agents.py#L74) | 74 | `"        self,"` | — |
| [SRC-8A5C31AD7D-L000075](../../agents/specialist_agents.py#L75) | 75 | `"        answer: str,"` | — |
| [SRC-8A5C31AD7D-L000076](../../agents/specialist_agents.py#L76) | 76 | `"        bank: MemoryBank,"` | — |
| [SRC-8A5C31AD7D-L000077](../../agents/specialist_agents.py#L77) | 77 | `"        *,"` | — |
| [SRC-8A5C31AD7D-L000078](../../agents/specialist_agents.py#L78) | 78 | `"        aspects: list[str] \| None = None,"` | — |
| [SRC-8A5C31AD7D-L000079](../../agents/specialist_agents.py#L79) | 79 | `"    ) -> dict[str, Any]:"` | — |
| [SRC-8A5C31AD7D-L000080](../../agents/specialist_agents.py#L80) | 80 | `"        claims_text = split_answer_into_claim_sentences(answer)"` | — |
| [SRC-8A5C31AD7D-L000081](../../agents/specialist_agents.py#L81) | 81 | `"        bound = [bank.bind_claim(c, min_score=self.min_support) for c in claims_text]"` | — |
| [SRC-8A5C31AD7D-L000082](../../agents/specialist_agents.py#L82) | 82 | `"        unsupported = [c for c in bound if c.status == \"unsupported\"]"` | — |
| [SRC-8A5C31AD7D-L000083](../../agents/specialist_agents.py#L83) | 83 | `"        weak = [c for c in bound if c.status == \"weak\"]"` | — |
| [SRC-8A5C31AD7D-L000084](../../agents/specialist_agents.py#L84) | 84 | `"        missing_aspects = []"` | — |
| [SRC-8A5C31AD7D-L000085](../../agents/specialist_agents.py#L85) | 85 | `"        blob = (answer or \"\").casefold()"` | — |
| [SRC-8A5C31AD7D-L000086](../../agents/specialist_agents.py#L86) | 86 | `"        for a in aspects or []:"` | — |
| [SRC-8A5C31AD7D-L000087](../../agents/specialist_agents.py#L87) | 87 | `"            if a and a.casefold() not in blob:"` | — |
| [SRC-8A5C31AD7D-L000088](../../agents/specialist_agents.py#L88) | 88 | `"                ev_blob = \" \".join(e.snippet.casefold() for e in bank.evidence.values())"` | — |
| [SRC-8A5C31AD7D-L000089](../../agents/specialist_agents.py#L89) | 89 | `"                if a.casefold() not in ev_blob:"` | — |
| [SRC-8A5C31AD7D-L000090](../../agents/specialist_agents.py#L90) | 90 | `"                    missing_aspects.append(a)"` | — |
| [SRC-8A5C31AD7D-L000091](../../agents/specialist_agents.py#L91) | 91 | `"        return {"` | — |
| [SRC-8A5C31AD7D-L000092](../../agents/specialist_agents.py#L92) | 92 | `"            \"agent\": \"HallucinationGuard\","` | — |
| [SRC-8A5C31AD7D-L000093](../../agents/specialist_agents.py#L93) | 93 | `"            \"claim_count\": len(bound),"` | — |
| [SRC-8A5C31AD7D-L000094](../../agents/specialist_agents.py#L94) | 94 | `"            \"unsupported_count\": len(unsupported),"` | — |
| [SRC-8A5C31AD7D-L000095](../../agents/specialist_agents.py#L95) | 95 | `"            \"weak_count\": len(weak),"` | — |
| [SRC-8A5C31AD7D-L000096](../../agents/specialist_agents.py#L96) | 96 | `"            \"unsupported_samples\": [c.text[:160] for c in unsupported[:5]],"` | — |
| [SRC-8A5C31AD7D-L000097](../../agents/specialist_agents.py#L97) | 97 | `"            \"missing_aspects\": missing_aspects,"` | — |
| [SRC-8A5C31AD7D-L000098](../../agents/specialist_agents.py#L98) | 98 | `"            \"should_abstain\": bool(unsupported) and len(unsupported) >= max(1, len(bound) // 2),"` | — |
| [SRC-8A5C31AD7D-L000099](../../agents/specialist_agents.py#L99) | 99 | `"            \"support_ratio\": bank.stats().get(\"support_ratio\", 0.0),"` | — |
| [SRC-8A5C31AD7D-L000100](../../agents/specialist_agents.py#L100) | 100 | `"            \"honesty_note\": ("` | — |
| [SRC-8A5C31AD7D-L000101](../../agents/specialist_agents.py#L101) | 101 | `"                \"الدعم لفظي/معجمي وليس إثباتًا دلاليًا لصدق الادعاء.\""` | — |
| [SRC-8A5C31AD7D-L000102](../../agents/specialist_agents.py#L102) | 102 | `"            ),"` | — |
| [SRC-8A5C31AD7D-L000103](../../agents/specialist_agents.py#L103) | 103 | `"        }"` | — |
| [SRC-8A5C31AD7D-L000104](../../agents/specialist_agents.py#L104) | 104 | `""` | — |
| [SRC-8A5C31AD7D-L000105](../../agents/specialist_agents.py#L105) | 105 | `""` | — |
| [SRC-8A5C31AD7D-L000106](../../agents/specialist_agents.py#L106) | 106 | `"class FinalComposer:"` | — |
| [SRC-8A5C31AD7D-L000107](../../agents/specialist_agents.py#L107) | 107 | `"    def compose("` | — |
| [SRC-8A5C31AD7D-L000108](../../agents/specialist_agents.py#L108) | 108 | `"        self,"` | — |
| [SRC-8A5C31AD7D-L000109](../../agents/specialist_agents.py#L109) | 109 | `"        draft: str,"` | — |
| [SRC-8A5C31AD7D-L000110](../../agents/specialist_agents.py#L110) | 110 | `"        bank: MemoryBank,"` | — |
| [SRC-8A5C31AD7D-L000111](../../agents/specialist_agents.py#L111) | 111 | `"        guard_report: dict[str, Any],"` | — |
| [SRC-8A5C31AD7D-L000112](../../agents/specialist_agents.py#L112) | 112 | `"        *,"` | — |
| [SRC-8A5C31AD7D-L000113](../../agents/specialist_agents.py#L113) | 113 | `"        language: str = \"ar\","` | — |
| [SRC-8A5C31AD7D-L000114](../../agents/specialist_agents.py#L114) | 114 | `"    ) -> dict[str, Any]:"` | — |
| [SRC-8A5C31AD7D-L000115](../../agents/specialist_agents.py#L115) | 115 | `"        if guard_report.get(\"should_abstain\") and not bank.evidence:"` | — |
| [SRC-8A5C31AD7D-L000116](../../agents/specialist_agents.py#L116) | 116 | `"            answer = ("` | — |
| [SRC-8A5C31AD7D-L000117](../../agents/specialist_agents.py#L117) | 117 | `"                \"لا تتوفر أدلة كافية في المصادر المسترجعة للإجابة بثقة. \""` | — |
| [SRC-8A5C31AD7D-L000118](../../agents/specialist_agents.py#L118) | 118 | `"                \"يُفضَّل إعادة صياغة السؤال أو توسيع نطاق البحث.\""` | — |
| [SRC-8A5C31AD7D-L000119](../../agents/specialist_agents.py#L119) | 119 | `"            )"` | — |
| [SRC-8A5C31AD7D-L000120](../../agents/specialist_agents.py#L120) | 120 | `"            return {"` | — |
| [SRC-8A5C31AD7D-L000121](../../agents/specialist_agents.py#L121) | 121 | `"                \"agent\": \"FinalComposer\","` | — |
| [SRC-8A5C31AD7D-L000122](../../agents/specialist_agents.py#L122) | 122 | `"                \"answer\": answer,"` | — |
| [SRC-8A5C31AD7D-L000123](../../agents/specialist_agents.py#L123) | 123 | `"                \"abstained\": True,"` | — |
| [SRC-8A5C31AD7D-L000124](../../agents/specialist_agents.py#L124) | 124 | `"                \"citations\": bank.citation_map(),"` | — |
| [SRC-8A5C31AD7D-L000125](../../agents/specialist_agents.py#L125) | 125 | `"                \"memory\": bank.to_dict(),"` | — |
| [SRC-8A5C31AD7D-L000126](../../agents/specialist_agents.py#L126) | 126 | `"            }"` | — |
| [SRC-8A5C31AD7D-L000127](../../agents/specialist_agents.py#L127) | 127 | `""` | — |
| [SRC-8A5C31AD7D-L000128](../../agents/specialist_agents.py#L128) | 128 | `"        sentences = split_answer_into_claim_sentences(draft)"` | — |
| [SRC-8A5C31AD7D-L000129](../../agents/specialist_agents.py#L129) | 129 | `"        cited_lines: list[str] = []"` | — |
| [SRC-8A5C31AD7D-L000130](../../agents/specialist_agents.py#L130) | 130 | `"        for s in sentences:"` | — |
| [SRC-8A5C31AD7D-L000131](../../agents/specialist_agents.py#L131) | 131 | `"            claim = bank.bind_claim(s)"` | — |
| [SRC-8A5C31AD7D-L000132](../../agents/specialist_agents.py#L132) | 132 | `"            if claim.status == \"unsupported\":"` | — |
| [SRC-8A5C31AD7D-L000133](../../agents/specialist_agents.py#L133) | 133 | `"                continue"` | — |
| [SRC-8A5C31AD7D-L000134](../../agents/specialist_agents.py#L134) | 134 | `"            cited_lines.append(bank.format_claim_with_citations(claim))"` | — |
| [SRC-8A5C31AD7D-L000135](../../agents/specialist_agents.py#L135) | 135 | `"        if not cited_lines:"` | — |
| [SRC-8A5C31AD7D-L000136](../../agents/specialist_agents.py#L136) | 136 | `"            body = draft.strip()"` | — |
| [SRC-8A5C31AD7D-L000137](../../agents/specialist_agents.py#L137) | 137 | `"            note = \"\\n\\nتنبيه: تعذّر ربط جمل الإجابة بأدلة كافية؛ راجع المصادر.\""` | — |
| [SRC-8A5C31AD7D-L000138](../../agents/specialist_agents.py#L138) | 138 | `"            answer = body + note"` | — |
| [SRC-8A5C31AD7D-L000139](../../agents/specialist_agents.py#L139) | 139 | `"            abstained = True"` | — |
| [SRC-8A5C31AD7D-L000140](../../agents/specialist_agents.py#L140) | 140 | `"        else:"` | — |
| [SRC-8A5C31AD7D-L000141](../../agents/specialist_agents.py#L141) | 141 | `"            answer = \"\\n\".join(cited_lines)"` | — |
| [SRC-8A5C31AD7D-L000142](../../agents/specialist_agents.py#L142) | 142 | `"            if guard_report.get(\"missing_aspects\"):"` | — |
| [SRC-8A5C31AD7D-L000143](../../agents/specialist_agents.py#L143) | 143 | `"                answer += ("` | — |
| [SRC-8A5C31AD7D-L000144](../../agents/specialist_agents.py#L144) | 144 | `"                    \"\\n\\nمحاور بلا دعم كافٍ في النتائج: \""` | — |
| [SRC-8A5C31AD7D-L000145](../../agents/specialist_agents.py#L145) | 145 | `"                    + \"، \".join(guard_report[\"missing_aspects\"][:6])"` | — |
| [SRC-8A5C31AD7D-L000146](../../agents/specialist_agents.py#L146) | 146 | `"                )"` | — |
| [SRC-8A5C31AD7D-L000147](../../agents/specialist_agents.py#L147) | 147 | `"            abstained = False"` | — |
| [SRC-8A5C31AD7D-L000148](../../agents/specialist_agents.py#L148) | 148 | `"        return {"` | — |
| [SRC-8A5C31AD7D-L000149](../../agents/specialist_agents.py#L149) | 149 | `"            \"agent\": \"FinalComposer\","` | — |
| [SRC-8A5C31AD7D-L000150](../../agents/specialist_agents.py#L150) | 150 | `"            \"answer\": answer,"` | — |
| [SRC-8A5C31AD7D-L000151](../../agents/specialist_agents.py#L151) | 151 | `"            \"abstained\": abstained,"` | — |
| [SRC-8A5C31AD7D-L000152](../../agents/specialist_agents.py#L152) | 152 | `"            \"citations\": bank.citation_map(),"` | — |
| [SRC-8A5C31AD7D-L000153](../../agents/specialist_agents.py#L153) | 153 | `"            \"memory\": bank.to_dict(),"` | — |
| [SRC-8A5C31AD7D-L000154](../../agents/specialist_agents.py#L154) | 154 | `"        }"` | — |
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
| [SRC-1AE03B9EC3-L000028](../../agents/web_agent.py#L28) | 28 | `"    validate_dialogue_context,"` | — |
| [SRC-1AE03B9EC3-L000029](../../agents/web_agent.py#L29) | 29 | `")"` | — |
| [SRC-1AE03B9EC3-L000030](../../agents/web_agent.py#L30) | 30 | `"from agents.answer_validation import audit_answer_integrity"` | — |
| [SRC-1AE03B9EC3-L000031](../../agents/web_agent.py#L31) | 31 | `"from agents.claim_evidence import build_claim_evidence_ledger"` | — |
| [SRC-1AE03B9EC3-L000032](../../agents/web_agent.py#L32) | 32 | `"from agents.request_budget import RequestBudget, RequestBudgetExceeded"` | — |
| [SRC-1AE03B9EC3-L000033](../../agents/web_agent.py#L33) | 33 | `"from agents.aspect_planning import ("` | — |
| [SRC-1AE03B9EC3-L000034](../../agents/web_agent.py#L34) | 34 | `"    arabic_aspect_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L000035](../../agents/web_agent.py#L35) | 35 | `"    build_evidence_ledger,"` | — |
| [SRC-1AE03B9EC3-L000036](../../agents/web_agent.py#L36) | 36 | `"    extract_aspects,"` | — |
| [SRC-1AE03B9EC3-L000037](../../agents/web_agent.py#L37) | 37 | `"    repair_queries_for_missing_aspects,"` | — |
| [SRC-1AE03B9EC3-L000038](../../agents/web_agent.py#L38) | 38 | `")"` | — |
| [SRC-1AE03B9EC3-L000039](../../agents/web_agent.py#L39) | 39 | `"from agents.search_connectors import search_arxiv, search_crossref, search_openalex"` | — |
| [SRC-1AE03B9EC3-L000040](../../agents/web_agent.py#L40) | 40 | `"from agents.research import ("` | — |
| [SRC-1AE03B9EC3-L000041](../../agents/web_agent.py#L41) | 41 | `"    MAX_PLAN_QUERIES,"` | — |
| [SRC-1AE03B9EC3-L000042](../../agents/web_agent.py#L42) | 42 | `"    SOCIAL_DOMAINS,"` | — |
| [SRC-1AE03B9EC3-L000043](../../agents/web_agent.py#L43) | 43 | `"    compact_search_query,"` | — |
| [SRC-1AE03B9EC3-L000044](../../agents/web_agent.py#L44) | 44 | `"    evidence_signal_report,"` | — |
| [SRC-1AE03B9EC3-L000045](../../agents/web_agent.py#L45) | 45 | `"    fallback_plan,"` | — |
| [SRC-1AE03B9EC3-L000046](../../agents/web_agent.py#L46) | 46 | `"    fuse_ranked_results,"` | — |
| [SRC-1AE03B9EC3-L000047](../../agents/web_agent.py#L47) | 47 | `"    registrable_domain,"` | — |
| [SRC-1AE03B9EC3-L000048](../../agents/web_agent.py#L48) | 48 | `"    validate_plan,"` | — |
| [SRC-1AE03B9EC3-L000049](../../agents/web_agent.py#L49) | 49 | `")"` | — |
| [SRC-1AE03B9EC3-L000050](../../agents/web_agent.py#L50) | 50 | `"from agents.research_guardrails import apply_source_guardrails"` | — |
| [SRC-1AE03B9EC3-L000051](../../agents/web_agent.py#L51) | 51 | `""` | — |
| [SRC-1AE03B9EC3-L000052](../../agents/web_agent.py#L52) | 52 | `"MAX_QUESTION_CHARS = 4000"` | — |
| [SRC-1AE03B9EC3-L000053](../../agents/web_agent.py#L53) | 53 | `"MAX_HISTORY_ITEMS = 8"` | — |
| [SRC-1AE03B9EC3-L000054](../../agents/web_agent.py#L54) | 54 | `"MAX_HISTORY_CHARS = 4000"` | — |
| [SRC-1AE03B9EC3-L000055](../../agents/web_agent.py#L55) | 55 | `"MAX_SEARCH_RESULTS = 18"` | — |
| [SRC-1AE03B9EC3-L000056](../../agents/web_agent.py#L56) | 56 | `"MAX_PROVIDER_RESULTS = 6"` | — |
| [SRC-1AE03B9EC3-L000057](../../agents/web_agent.py#L57) | 57 | `"MAX_FETCHED_PAGES = 8"` | — |
| [SRC-1AE03B9EC3-L000058](../../agents/web_agent.py#L58) | 58 | `"MAX_LLM_CITED_SOURCES = 12"` | — |
| [SRC-1AE03B9EC3-L000059](../../agents/web_agent.py#L59) | 59 | `"MAX_RESEARCH_WORKERS = 8"` | — |
| [SRC-1AE03B9EC3-L000060](../../agents/web_agent.py#L60) | 60 | `"MAX_PAGE_BYTES = 1_000_000"` | — |
| [SRC-1AE03B9EC3-L000061](../../agents/web_agent.py#L61) | 61 | `"MAX_PAGE_TEXT_CHARS = 12_000"` | — |
| [SRC-1AE03B9EC3-L000062](../../agents/web_agent.py#L62) | 62 | `"LLM_TIMEOUT_SECONDS = 35"` | — |
| [SRC-1AE03B9EC3-L000063](../../agents/web_agent.py#L63) | 63 | `""` | — |
| [SRC-1AE03B9EC3-L000064](../../agents/web_agent.py#L64) | 64 | `"# Only completed connector result-processing states positively confirm an attempt."` | — |
| [SRC-1AE03B9EC3-L000065](../../agents/web_agent.py#L65) | 65 | `"# A generic \"failed\" or timeout diagnostic may occur before a network request is sent."` | — |
| [SRC-1AE03B9EC3-L000066](../../agents/web_agent.py#L66) | 66 | `"_SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES = frozenset({\"ok\", \"no_results\", \"filtered_all\"})"` | — |
| [SRC-1AE03B9EC3-L000067](../../agents/web_agent.py#L67) | 67 | `"_RESEARCH_ERROR_OUTCOMES = frozenset({\"attempted_research_error\", \"unknown_after_research_error\"})"` | — |
| [SRC-1AE03B9EC3-L000068](../../agents/web_agent.py#L68) | 68 | `"_PROVIDER_REJECTION_REASONS = ("` | — |
| [SRC-1AE03B9EC3-L000069](../../agents/web_agent.py#L69) | 69 | `"    \"malformed_candidate\","` | — |
| [SRC-1AE03B9EC3-L000070](../../agents/web_agent.py#L70) | 70 | `"    \"invalid_url_or_unsafe_target\","` | — |
| [SRC-1AE03B9EC3-L000071](../../agents/web_agent.py#L71) | 71 | `"    \"blocked_domain\","` | — |
| [SRC-1AE03B9EC3-L000072](../../agents/web_agent.py#L72) | 72 | `"    \"relevance_below_threshold\","` | — |
| [SRC-1AE03B9EC3-L000073](../../agents/web_agent.py#L73) | 73 | `")"` | — |
| [SRC-1AE03B9EC3-L000074](../../agents/web_agent.py#L74) | 74 | `""` | — |
| [SRC-1AE03B9EC3-L000075](../../agents/web_agent.py#L75) | 75 | `""` | — |
| [SRC-1AE03B9EC3-L000076](../../agents/web_agent.py#L76) | 76 | `"_ARABIC_SEARCH_TRANSLATION = str.maketrans({"` | — |
| [SRC-1AE03B9EC3-L000077](../../agents/web_agent.py#L77) | 77 | `"    \"أ\": \"ا\", \"إ\": \"ا\", \"آ\": \"ا\", \"ٱ\": \"ا\", \"ى\": \"ي\","` | — |
| [SRC-1AE03B9EC3-L000078](../../agents/web_agent.py#L78) | 78 | `"    \"ؤ\": \"و\", \"ئ\": \"ي\", \"ة\": \"ه\", \"ـ\": \"\","` | — |
| [SRC-1AE03B9EC3-L000079](../../agents/web_agent.py#L79) | 79 | `"})"` | — |
| [SRC-1AE03B9EC3-L000080](../../agents/web_agent.py#L80) | 80 | `"_ARABIC_DIACRITICS_RE = re.compile(r\"[\\u0610-\\u061A\\u064B-\\u065F\\u0670\\u06D6-\\u06ED]\")"` | — |
| [SRC-1AE03B9EC3-L000081](../../agents/web_agent.py#L81) | 81 | `"_SEARCH_STOPWORDS = frozenset({"` | — |
| [SRC-1AE03B9EC3-L000082](../../agents/web_agent.py#L82) | 82 | `"    \"ما\", \"ماذا\", \"من\", \"في\", \"على\", \"عن\", \"الى\", \"إلى\", \"و\", \"او\", \"أو\","` | — |
| [SRC-1AE03B9EC3-L000083](../../agents/web_agent.py#L83) | 83 | `"    \"هل\", \"هو\", \"هي\", \"هذا\", \"هذه\", \"ذلك\", \"تلك\", \"التي\", \"الذي\", \"مع\","` | — |
