# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **006**
- سجلات الأسطر: **800**
- النطاق: SRC-3AA6165B18-L000149 إلى SRC-686F71AA50-L000253
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-3AA6165B18 — [agents/research_guardrails.py](../../agents/research_guardrails.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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
| [SRC-60066C6786-L000187](../../agents/research_pipeline.py#L187) | 187 | `"        )"` | — |
| [SRC-60066C6786-L000188](../../agents/research_pipeline.py#L188) | 188 | `"        queries = [item[\"query\"] for item in strategy_matrix]"` | — |
| [SRC-60066C6786-L000189](../../agents/research_pipeline.py#L189) | 189 | `"        query_status = \"completed\""` | — |
| [SRC-60066C6786-L000190](../../agents/research_pipeline.py#L190) | 190 | `""` | — |
| [SRC-60066C6786-L000191](../../agents/research_pipeline.py#L191) | 191 | `"    evidence = evaluate_research_evidence("` | — |
| [SRC-60066C6786-L000192](../../agents/research_pipeline.py#L192) | 192 | `"        aspects, sources, semantic_matcher=semantic_matcher"` | — |
| [SRC-60066C6786-L000193](../../agents/research_pipeline.py#L193) | 193 | `"    )"` | — |
| [SRC-60066C6786-L000194](../../agents/research_pipeline.py#L194) | 194 | `"    return {"` | — |
| [SRC-60066C6786-L000195](../../agents/research_pipeline.py#L195) | 195 | `"        \"contextual_question\": contextual_question,"` | — |
| [SRC-60066C6786-L000196](../../agents/research_pipeline.py#L196) | 196 | `"        \"intent\": intent,"` | — |
| [SRC-60066C6786-L000197](../../agents/research_pipeline.py#L197) | 197 | `"        \"task_spec\": task_spec,"` | — |
| [SRC-60066C6786-L000198](../../agents/research_pipeline.py#L198) | 198 | `"        \"aspects\": aspects,"` | — |
| [SRC-60066C6786-L000199](../../agents/research_pipeline.py#L199) | 199 | `"        \"query_strategy_matrix\": strategy_matrix,"` | — |
| [SRC-60066C6786-L000200](../../agents/research_pipeline.py#L200) | 200 | `"        \"queries\": queries,"` | — |
| [SRC-60066C6786-L000201](../../agents/research_pipeline.py#L201) | 201 | `"        \"evidence\": evidence,"` | — |
| [SRC-60066C6786-L000202](../../agents/research_pipeline.py#L202) | 202 | `"        \"evidence_ledger\": evidence[\"lexical_ledger\"],"` | — |
| [SRC-60066C6786-L000203](../../agents/research_pipeline.py#L203) | 203 | `"        \"stages\": {"` | — |
| [SRC-60066C6786-L000204](../../agents/research_pipeline.py#L204) | 204 | `"            \"context_resolution\": ("` | — |
| [SRC-60066C6786-L000205](../../agents/research_pipeline.py#L205) | 205 | `"                \"completed\""` | — |
| [SRC-60066C6786-L000206](../../agents/research_pipeline.py#L206) | 206 | `"                if history or _has_resolved_dialogue_context(dialogue_context)"` | — |
| [SRC-60066C6786-L000207](../../agents/research_pipeline.py#L207) | 207 | `"                else \"not_needed\""` | — |
| [SRC-60066C6786-L000208](../../agents/research_pipeline.py#L208) | 208 | `"            ),"` | — |
| [SRC-60066C6786-L000209](../../agents/research_pipeline.py#L209) | 209 | `"            \"intent_routing\": \"completed\","` | — |
| [SRC-60066C6786-L000210](../../agents/research_pipeline.py#L210) | 210 | `"            \"task_understanding\": \"completed\","` | — |
| [SRC-60066C6786-L000211](../../agents/research_pipeline.py#L211) | 211 | `"            \"aspect_extraction\": \"completed\","` | — |
| [SRC-60066C6786-L000212](../../agents/research_pipeline.py#L212) | 212 | `"            \"query_planning\": query_status,"` | — |
| [SRC-60066C6786-L000213](../../agents/research_pipeline.py#L213) | 213 | `"            \"lexical_matching\": evidence[\"lexical_matching_status\"],"` | — |
| [SRC-60066C6786-L000214](../../agents/research_pipeline.py#L214) | 214 | `"            \"semantic_matching\": evidence[\"semantic_matching\"][\"status\"],"` | — |
| [SRC-60066C6786-L000215](../../agents/research_pipeline.py#L215) | 215 | `"            \"claim_verification\": evidence[\"claim_verification\"],"` | — |
| [SRC-60066C6786-L000216](../../agents/research_pipeline.py#L216) | 216 | `"        },"` | — |
| [SRC-60066C6786-L000217](../../agents/research_pipeline.py#L217) | 217 | `"    }"` | — |
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

### FILE-686F71AA50 — [agents/task_understanding.py](../../agents/task_understanding.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-686F71AA50-L000001](../../agents/task_understanding.py#L1) | 1 | `"\"\"\"Deterministic, auditable natural-language task interpretation for Omarai."` | — |
| [SRC-686F71AA50-L000002](../../agents/task_understanding.py#L2) | 2 | `""` | — |
| [SRC-686F71AA50-L000003](../../agents/task_understanding.py#L3) | 3 | `"This module produces a bounded TaskSpec and a query-strategy matrix. It does not"` | — |
| [SRC-686F71AA50-L000004](../../agents/task_understanding.py#L4) | 4 | `"claim semantic certainty, generate facts, or execute tools. Signals and hypotheses"` | — |
| [SRC-686F71AA50-L000005](../../agents/task_understanding.py#L5) | 5 | `"are diagnostics, never probabilities. Search plans remain subject to budgets,"` | — |
| [SRC-686F71AA50-L000006](../../agents/task_understanding.py#L6) | 6 | `"source guardrails, and the final evidence checks."` | — |
| [SRC-686F71AA50-L000007](../../agents/task_understanding.py#L7) | 7 | `"\"\"\""` | — |
| [SRC-686F71AA50-L000008](../../agents/task_understanding.py#L8) | 8 | `"from __future__ import annotations"` | — |
| [SRC-686F71AA50-L000009](../../agents/task_understanding.py#L9) | 9 | `""` | — |
| [SRC-686F71AA50-L000010](../../agents/task_understanding.py#L10) | 10 | `"import re"` | — |
| [SRC-686F71AA50-L000011](../../agents/task_understanding.py#L11) | 11 | `"import unicodedata"` | — |
| [SRC-686F71AA50-L000012](../../agents/task_understanding.py#L12) | 12 | `"from typing import Any"` | — |
| [SRC-686F71AA50-L000013](../../agents/task_understanding.py#L13) | 13 | `""` | — |
| [SRC-686F71AA50-L000014](../../agents/task_understanding.py#L14) | 14 | `"MAX_TASK_CHARS = 4000"` | — |
| [SRC-686F71AA50-L000015](../../agents/task_understanding.py#L15) | 15 | `"MAX_TASK_ASPECTS = 8"` | — |
| [SRC-686F71AA50-L000016](../../agents/task_understanding.py#L16) | 16 | `"MAX_STRATEGY_QUERIES = 8"` | — |
| [SRC-686F71AA50-L000017](../../agents/task_understanding.py#L17) | 17 | `"SUPPORTED_MODES = frozenset({\"auto\", \"deep\", \"latest\", \"social\"})"` | — |
| [SRC-686F71AA50-L000018](../../agents/task_understanding.py#L18) | 18 | `""` | — |
| [SRC-686F71AA50-L000019](../../agents/task_understanding.py#L19) | 19 | `"# Closed, code-owned playbooks. The model receives concise task guidance derived"` | — |
| [SRC-686F71AA50-L000020](../../agents/task_understanding.py#L20) | 20 | `"# from these IDs; arbitrary planner/source text cannot add executable instructions."` | — |
| [SRC-686F71AA50-L000021](../../agents/task_understanding.py#L21) | 21 | `"_REASONING_GUIDANCE = {"` | — |
| [SRC-686F71AA50-L000022](../../agents/task_understanding.py#L22) | 22 | `"    \"preserve_goal_and_constraints\": \"حافظ على مقصد المستخدم والكيانات والبلد والسنة والميزانية والتواريخ والصيغة التي ذكرها صراحة؛ لا تخترع قيودًا مفقودة.\","` | — |
| [SRC-686F71AA50-L000023](../../agents/task_understanding.py#L23) | 23 | `"    \"separate_facts_inferences_hypotheses\": \"افصل ما يقوله المصدر مباشرة عن الاستنتاج والفرضية والمعلومة المجهولة؛ لا ترفع الفرضية إلى حقيقة دون دليل.\","` | — |
| [SRC-686F71AA50-L000024](../../agents/task_understanding.py#L24) | 24 | `"    \"ground_material_claims\": \"اربط كل ادعاء واقعي جوهري بدليل مناسب من المصدر؛ الاستشهاد أو تشابه الكلمات وحده لا يثبت صحة الادعاء.\","` | — |
| [SRC-686F71AA50-L000025](../../agents/task_understanding.py#L25) | 25 | `"    \"bounded_stop_rule\": \"استخدم المحاولات والوقت المسموحين فقط؛ عند نقص الدليل، أجب جزئيًا أو امتنع بوضوح بدل التخمين.\","` | — |
| [SRC-686F71AA50-L000026](../../agents/task_understanding.py#L26) | 26 | `"    \"clarify_required_input\": \"إذا غاب مدخل إلزامي يغيّر معنى المهمة، اطلبه قبل تشغيل أداة أو اختراع هدف.\","` | — |
| [SRC-686F71AA50-L000027](../../agents/task_understanding.py#L27) | 27 | `"    \"resolve_followup_slots\": \"في المتابعة، احتفظ فقط بالسياق الذي له مرجع واضح، وطبّق التغييرات التي ذكرها المستخدم، ولا ترث موضوعًا قديمًا بعد تغيير الموضوع.\","` | — |
| [SRC-686F71AA50-L000028](../../agents/task_understanding.py#L28) | 28 | `"    \"verify_official_destination\": \"طابق اسم الجهة والبلد أولًا؛ فضّل نطاق الجهة أو رابطًا صادرًا عن بوابة رسمية موثوقة، ولا تعتبر امتداد النطاق وحده إثباتًا للملكية.\","` | — |
| [SRC-686F71AA50-L000029](../../agents/task_understanding.py#L29) | 29 | `"    \"separate_event_and_publication_dates\": \"ميّز تاريخ وقوع الحدث عن تاريخ النشر وآخر تحديث وتاريخ الوصول؛ لا تستخدم خبرًا قديمًا لإثبات حالة متغيرة الآن.\","` | — |
| [SRC-686F71AA50-L000030](../../agents/task_understanding.py#L30) | 30 | `"    \"reject_stale_current_claims\": \"للمعلومة الحالية، افحص حداثة المصدر وقابلية قراءة الصفحة وارتباطها بالحالة الحالية؛ اعرض عدم التأكد إذا غاب دليل حديث مؤهل.\","` | — |
| [SRC-686F71AA50-L000031](../../agents/task_understanding.py#L31) | 31 | `"    \"decompose_explicit_criteria\": \"قسّم المقارنة إلى كل معيار صريح، وابحث عن دليل لكل معيار، وسجّل المحاور التي لا تزال بلا دليل بدل إسقاطها.\","` | — |
| [SRC-686F71AA50-L000032](../../agents/task_understanding.py#L32) | 32 | `"    \"normalize_comparison_conditions\": \"قبل المقارنة، وحّد العملة والوحدات والفترة وظروف الاستخدام؛ لا تقارن قيمًا غير قابلة للمقارنة دون شرح الفرق.\","` | — |
| [SRC-686F71AA50-L000033](../../agents/task_understanding.py#L33) | 33 | `"    \"separate_specs_and_experiences\": \"افصل المواصفات الرسمية عن الاختبارات الصحفية وتجارب الأفراد والإعلانات؛ لكل نوع منها ما يستطيع إثباته وحدوده.\","` | — |
| [SRC-686F71AA50-L000034](../../agents/task_understanding.py#L34) | 34 | `"    \"balance_social_evidence\": \"ميّز التجربة الشخصية المحتملة عن السؤال والترويج والمحتوى الصحفي؛ اعرض عينة المنشورات وتواريخها والاختلافات ولا تعمم على الجميع.\","` | — |
| [SRC-686F71AA50-L000035](../../agents/task_understanding.py#L35) | 35 | `"    \"record_observed_symptoms\": \"احفظ رسالة الخطأ والبيئة والإصدار والخطوات التي يمكن تكرارها؛ ميّز الملاحظة المرصودة عن تفسير السبب.\","` | — |
| [SRC-686F71AA50-L000036](../../agents/task_understanding.py#L36) | 36 | `"    \"rank_testable_hypotheses\": \"أنشئ عدة فرضيات للسبب، ورتّبها وفق الأدلة المتاحة وقابلية الاختبار، ولا تدّعِ إثبات السبب قبل تجربة تفصل بين الفرضيات.\","` | — |
| [SRC-686F71AA50-L000037](../../agents/task_understanding.py#L37) | 37 | `"    \"verify_primary_technical_docs\": \"تحقق من دليل المنتج أو مرجع الواجهة أو سجل التغيير الأصلي، واستخدم اختبارًا يعيد إنتاج المشكلة للتحقق من الإصلاح.\","` | — |
| [SRC-686F71AA50-L000038](../../agents/task_understanding.py#L38) | 38 | `"    \"prefer_low_risk_steps\": \"ابدأ بخطوات تشخيص قابلة للعكس ومنخفضة المخاطر، واذكر شروط التوقف؛ لا تقترح إجراءً خطيرًا لمجرد أنه احتمال.\","` | — |
| [SRC-686F71AA50-L000039](../../agents/task_understanding.py#L39) | 39 | `"    \"ordered_safe_procedure\": \"اذكر المتطلبات المسبقة والتحذيرات ثم الخطوات بالترتيب، وأضف طريقة للتحقق من النتيجة ولا تساوِ بين إكمال الخطوات ونجاحها.\","` | — |
| [SRC-686F71AA50-L000040](../../agents/task_understanding.py#L40) | 40 | `"    \"check_health_scope_and_urgency\": \"افصل التثقيف الصحي العام عن التشخيص الشخصي، وقدّم مصادر صحية موثوقة وحدود المعلومات، ووجّه الحالات الطارئة إلى الرعاية المناسبة.\","` | — |
| [SRC-686F71AA50-L000041](../../agents/task_understanding.py#L41) | 41 | `"    \"check_legal_jurisdiction_and_effective_date\": \"حدّد الدولة أو الاختصاص القانوني وتاريخ النفاذ، وقدّم النص الأصلي الرسمي عند توفره، ولا تعرض المعلومات العامة بوصفها استشارة قانونية خاصة.\","` | — |
| [SRC-686F71AA50-L000042](../../agents/task_understanding.py#L42) | 42 | `"    \"validate_data_before_interpreting\": \"تحقق من تعريف المقياس ووحدة التحليل والفترة والبيانات الناقصة والتكرارات والقيم الشاذة قبل تفسير النتائج؛ الارتباط لا يثبت السببية.\","` | — |
| [SRC-686F71AA50-L000043](../../agents/task_understanding.py#L43) | 43 | `"    \"validate_units_and_arithmetic\": \"تحقق من الوحدات والمدخلات والافتراضات، واعرض المعادلة أو خطوات الحساب القابلة للفحص، وأجرِ تحققًا حسابيًا مستقلًا عندما يلزم.\","` | — |
| [SRC-686F71AA50-L000044](../../agents/task_understanding.py#L44) | 44 | `"    \"preserve_translation_meaning\": \"حافظ على المعنى والنبرة والأسماء والمصطلحات وصيغة الهدف؛ أظهر الالتباس الحقيقي بدل اختراع معنى للنص.\","` | — |
| [SRC-686F71AA50-L000045](../../agents/task_understanding.py#L45) | 45 | `"    \"preserve_user_facts_in_writing\": \"التزم بالجمهور والنبرة والشكل المطلوب، ولا تضف حقائق غير مقدمة أو موثقة، وافصل إعادة الصياغة عن التحقق الواقعي.\","` | — |
| [SRC-686F71AA50-L000046](../../agents/task_understanding.py#L46) | 46 | `"    \"plan_dependencies_and_fallbacks\": \"رتّب العمل حسب التبعيات والموارد والموعد والمخاطر، وبيّن الافتراضات والبدائل، ولا تصف خطوة مقترحة بأنها نُفذت.\","` | — |
| [SRC-686F71AA50-L000047](../../agents/task_understanding.py#L47) | 47 | `"    \"compare_recommendation_tradeoffs\": \"وازن البدائل وفق احتياج المستخدم وقيوده، وبيّن المفاضلات والمعلومات الناقصة، ولا تعلن فائزًا عامًا دون أساس مقارنة واضح.\","` | — |
| [SRC-686F71AA50-L000048](../../agents/task_understanding.py#L48) | 48 | `"    \"summarize_only_available_content\": \"لخّص النص المقدم أو الصفحة التي قُرئت فعلًا فقط؛ لا تستنتج محتوى غير مقروء من عنوان أو رابط.\","` | — |
| [SRC-686F71AA50-L000049](../../agents/task_understanding.py#L49) | 49 | `"    \"qualify_buyer_intent\": \"ميّز إشارة نية شراء صريحة عن إعلان بيع أو صفحة تجارية؛ لا تعتبر الإعلان عميلًا ولا تزعم التحقق من الهوية.\","` | — |
| [SRC-686F71AA50-L000050](../../agents/task_understanding.py#L50) | 50 | `"    \"prefer_lowest_sufficient_tool\": \"اختر أقل مسار أدوات كافٍ للمهمة؛ لا تبحث في الويب عندما تكفي المادة المقدمة أو الحساب المحلي، ولا تشغّل أداة غير مهيأة أو غير مسموح بها.\","` | — |
| [SRC-686F71AA50-L000051](../../agents/task_understanding.py#L51) | 51 | `"}"` | — |
| [SRC-686F71AA50-L000052](../../agents/task_understanding.py#L52) | 52 | `"_REASONING_FAMILY_IDS = {"` | — |
| [SRC-686F71AA50-L000053](../../agents/task_understanding.py#L53) | 53 | `"    \"official_site_lookup\": (\"verify_official_destination\",),"` | — |
| [SRC-686F71AA50-L000054](../../agents/task_understanding.py#L54) | 54 | `"    \"social_opinions\": (\"balance_social_evidence\", \"separate_specs_and_experiences\"),"` | — |
| [SRC-686F71AA50-L000055](../../agents/task_understanding.py#L55) | 55 | `"    \"summarize\": (\"summarize_only_available_content\",),"` | — |
| [SRC-686F71AA50-L000056](../../agents/task_understanding.py#L56) | 56 | `"    \"troubleshoot\": (\"record_observed_symptoms\", \"rank_testable_hypotheses\", \"verify_primary_technical_docs\", \"prefer_low_risk_steps\"),"` | — |
| [SRC-686F71AA50-L000057](../../agents/task_understanding.py#L57) | 57 | `"    \"compare\": (\"decompose_explicit_criteria\", \"normalize_comparison_conditions\", \"separate_specs_and_experiences\"),"` | — |
| [SRC-686F71AA50-L000058](../../agents/task_understanding.py#L58) | 58 | `"    \"how_to\": (\"ordered_safe_procedure\",),"` | — |
| [SRC-686F71AA50-L000059](../../agents/task_understanding.py#L59) | 59 | `"    \"lead_generation\": (\"qualify_buyer_intent\",),"` | — |
| [SRC-686F71AA50-L000060](../../agents/task_understanding.py#L60) | 60 | `"    \"recommendation\": (\"compare_recommendation_tradeoffs\",),"` | — |
| [SRC-686F71AA50-L000061](../../agents/task_understanding.py#L61) | 61 | `"    \"medical_information\": (\"check_health_scope_and_urgency\",),"` | — |
| [SRC-686F71AA50-L000062](../../agents/task_understanding.py#L62) | 62 | `"    \"legal_information\": (\"check_legal_jurisdiction_and_effective_date\",),"` | — |
| [SRC-686F71AA50-L000063](../../agents/task_understanding.py#L63) | 63 | `"    \"coding_or_technical_design\": (\"record_observed_symptoms\", \"rank_testable_hypotheses\", \"verify_primary_technical_docs\"),"` | — |
| [SRC-686F71AA50-L000064](../../agents/task_understanding.py#L64) | 64 | `"    \"data_analysis\": (\"validate_data_before_interpreting\",),"` | — |
| [SRC-686F71AA50-L000065](../../agents/task_understanding.py#L65) | 65 | `"    \"calculation\": (\"validate_units_and_arithmetic\",),"` | — |
| [SRC-686F71AA50-L000066](../../agents/task_understanding.py#L66) | 66 | `"    \"translation\": (\"preserve_translation_meaning\",),"` | — |
| [SRC-686F71AA50-L000067](../../agents/task_understanding.py#L67) | 67 | `"    \"writing_or_editing\": (\"preserve_user_facts_in_writing\",),"` | — |
| [SRC-686F71AA50-L000068](../../agents/task_understanding.py#L68) | 68 | `"    \"planning\": (\"plan_dependencies_and_fallbacks\",),"` | — |
| [SRC-686F71AA50-L000069](../../agents/task_understanding.py#L69) | 69 | `"    \"creative_generation\": (\"preserve_user_facts_in_writing\",),"` | — |
| [SRC-686F71AA50-L000070](../../agents/task_understanding.py#L70) | 70 | `"}"` | — |
| [SRC-686F71AA50-L000071](../../agents/task_understanding.py#L71) | 71 | `"_DECISION_MATRIX = ("` | — |
| [SRC-686F71AA50-L000072](../../agents/task_understanding.py#L72) | 72 | `"    {\"stage\": \"interpret\", \"check\": \"goal_context_required_inputs\", \"pass_action\": \"preserve_explicit_constraints\", \"fail_action\": \"clarify_missing_required_input\"},"` | — |
| [SRC-686F71AA50-L000073](../../agents/task_understanding.py#L73) | 73 | `"    {\"stage\": \"route\", \"check\": \"tool_permission_and_readiness\", \"pass_action\": \"use_only_allowed_configured_tools\", \"fail_action\": \"report_not_configured_or_blocked\"},"` | — |
| [SRC-686F71AA50-L000074](../../agents/task_understanding.py#L74) | 74 | `"    {\"stage\": \"plan\", \"check\": \"distinct_relevant_queries_and_budget\", \"pass_action\": \"execute_bounded_deduplicated_plan\", \"fail_action\": \"stop_and_report_limit\"},"` | — |
| [SRC-686F71AA50-L000075](../../agents/task_understanding.py#L75) | 75 | `"    {\"stage\": \"evidence\", \"check\": \"relevance_identity_freshness_readability\", \"pass_action\": \"retain_task_eligible_evidence\", \"fail_action\": \"exclude_and_record_reason\"},"` | — |
| [SRC-686F71AA50-L000076](../../agents/task_understanding.py#L76) | 76 | `"    {\"stage\": \"synthesize\", \"check\": \"claim_support_and_scope\", \"pass_action\": \"cite_supported_claims_and_qualify_inference\", \"fail_action\": \"answer_partially_or_abstain\"},"` | — |
| [SRC-686F71AA50-L000077](../../agents/task_understanding.py#L77) | 77 | `"    {\"stage\": \"terminate\", \"check\": \"actual_stage_outcomes\", \"pass_action\": \"report_observed_completion_state\", \"fail_action\": \"mark_partial_failed_or_not_run\"},"` | — |
| [SRC-686F71AA50-L000078](../../agents/task_understanding.py#L78) | 78 | `")"` | — |
| [SRC-686F71AA50-L000079](../../agents/task_understanding.py#L79) | 79 | `"_DECISION_STAGES = {row[\"stage\"] for row in _DECISION_MATRIX}"` | — |
| [SRC-686F71AA50-L000080](../../agents/task_understanding.py#L80) | 80 | `"_DECISION_IDS = {"` | — |
| [SRC-686F71AA50-L000081](../../agents/task_understanding.py#L81) | 81 | `"    field: {row[field] for row in _DECISION_MATRIX}"` | — |
| [SRC-686F71AA50-L000082](../../agents/task_understanding.py#L82) | 82 | `"    for field in (\"check\", \"pass_action\", \"fail_action\")"` | — |
| [SRC-686F71AA50-L000083](../../agents/task_understanding.py#L83) | 83 | `"}"` | — |
| [SRC-686F71AA50-L000084](../../agents/task_understanding.py#L84) | 84 | `""` | — |
| [SRC-686F71AA50-L000085](../../agents/task_understanding.py#L85) | 85 | `""` | — |
| [SRC-686F71AA50-L000086](../../agents/task_understanding.py#L86) | 86 | `"def _reasoning_strategy_ids("` | — |
| [SRC-686F71AA50-L000087](../../agents/task_understanding.py#L87) | 87 | `"    family: str,"` | — |
| [SRC-686F71AA50-L000088](../../agents/task_understanding.py#L88) | 88 | `"    constraints: dict[str, Any],"` | — |
| [SRC-686F71AA50-L000089](../../agents/task_understanding.py#L89) | 89 | `"    context_resolution: dict[str, Any],"` | — |
| [SRC-686F71AA50-L000090](../../agents/task_understanding.py#L90) | 90 | `"    missing_required_inputs: list[str],"` | — |
| [SRC-686F71AA50-L000091](../../agents/task_understanding.py#L91) | 91 | `") -> list[str]:"` | — |
| [SRC-686F71AA50-L000092](../../agents/task_understanding.py#L92) | 92 | `"    selected = ["` | — |
| [SRC-686F71AA50-L000093](../../agents/task_understanding.py#L93) | 93 | `"        \"preserve_goal_and_constraints\","` | — |
| [SRC-686F71AA50-L000094](../../agents/task_understanding.py#L94) | 94 | `"        \"separate_facts_inferences_hypotheses\","` | — |
| [SRC-686F71AA50-L000095](../../agents/task_understanding.py#L95) | 95 | `"        \"ground_material_claims\","` | — |
| [SRC-686F71AA50-L000096](../../agents/task_understanding.py#L96) | 96 | `"        \"bounded_stop_rule\","` | — |
| [SRC-686F71AA50-L000097](../../agents/task_understanding.py#L97) | 97 | `"        \"prefer_lowest_sufficient_tool\","` | — |
| [SRC-686F71AA50-L000098](../../agents/task_understanding.py#L98) | 98 | `"    ]"` | — |
| [SRC-686F71AA50-L000099](../../agents/task_understanding.py#L99) | 99 | `"    selected.extend(_REASONING_FAMILY_IDS.get(family, ()))"` | — |
| [SRC-686F71AA50-L000100](../../agents/task_understanding.py#L100) | 100 | `"    if missing_required_inputs or context_resolution.get(\"needs_clarification\"):"` | — |
| [SRC-686F71AA50-L000101](../../agents/task_understanding.py#L101) | 101 | `"        selected.append(\"clarify_required_input\")"` | — |
| [SRC-686F71AA50-L000102](../../agents/task_understanding.py#L102) | 102 | `"    if context_resolution.get(\"is_follow_up\"):"` | — |
| [SRC-686F71AA50-L000103](../../agents/task_understanding.py#L103) | 103 | `"        selected.append(\"resolve_followup_slots\")"` | — |
| [SRC-686F71AA50-L000104](../../agents/task_understanding.py#L104) | 104 | `"    if constraints.get(\"time_sensitive_request\"):"` | — |
| [SRC-686F71AA50-L000105](../../agents/task_understanding.py#L105) | 105 | `"        selected.extend((\"separate_event_and_publication_dates\", \"reject_stale_current_claims\"))"` | — |
| [SRC-686F71AA50-L000106](../../agents/task_understanding.py#L106) | 106 | `"    if constraints.get(\"official_destination_required\"):"` | — |
| [SRC-686F71AA50-L000107](../../agents/task_understanding.py#L107) | 107 | `"        selected.append(\"verify_official_destination\")"` | — |
| [SRC-686F71AA50-L000108](../../agents/task_understanding.py#L108) | 108 | `"    if constraints.get(\"social_evidence_requested\"):"` | — |
| [SRC-686F71AA50-L000109](../../agents/task_understanding.py#L109) | 109 | `"        selected.append(\"balance_social_evidence\")"` | — |
| [SRC-686F71AA50-L000110](../../agents/task_understanding.py#L110) | 110 | `"    if len(constraints.get(\"explicit_aspects\") or []) > 1:"` | — |
| [SRC-686F71AA50-L000111](../../agents/task_understanding.py#L111) | 111 | `"        selected.append(\"decompose_explicit_criteria\")"` | — |
| [SRC-686F71AA50-L000112](../../agents/task_understanding.py#L112) | 112 | `"    if constraints.get(\"explicit_budgets\"):"` | — |
| [SRC-686F71AA50-L000113](../../agents/task_understanding.py#L113) | 113 | `"        selected.append(\"preserve_goal_and_constraints\")"` | — |
| [SRC-686F71AA50-L000114](../../agents/task_understanding.py#L114) | 114 | `"    return list(dict.fromkeys(item for item in selected if item in _REASONING_GUIDANCE))[:12]"` | — |
| [SRC-686F71AA50-L000115](../../agents/task_understanding.py#L115) | 115 | `""` | — |
| [SRC-686F71AA50-L000116](../../agents/task_understanding.py#L116) | 116 | `""` | — |
| [SRC-686F71AA50-L000117](../../agents/task_understanding.py#L117) | 117 | `"def reasoning_guidance_for_task_spec(task_spec: dict[str, Any]) -> list[str]:"` | — |
| [SRC-686F71AA50-L000118](../../agents/task_understanding.py#L118) | 118 | `"    \"\"\"Expand allowlisted reasoning IDs into fixed, non-executable guidance text.\"\"\""` | — |
| [SRC-686F71AA50-L000119](../../agents/task_understanding.py#L119) | 119 | `"    ids = task_spec.get(\"reasoning_strategy_ids\") if isinstance(task_spec, dict) else []"` | — |
| [SRC-686F71AA50-L000120](../../agents/task_understanding.py#L120) | 120 | `"    if not isinstance(ids, list):"` | — |
| [SRC-686F71AA50-L000121](../../agents/task_understanding.py#L121) | 121 | `"        return []"` | — |
| [SRC-686F71AA50-L000122](../../agents/task_understanding.py#L122) | 122 | `"    return [_REASONING_GUIDANCE[item] for item in ids if isinstance(item, str) and item in _REASONING_GUIDANCE][:12]"` | — |
| [SRC-686F71AA50-L000123](../../agents/task_understanding.py#L123) | 123 | `""` | — |
| [SRC-686F71AA50-L000124](../../agents/task_understanding.py#L124) | 124 | `"_ARABIC_DIACRITICS = re.compile(r\"[\\u0610-\\u061A\\u064B-\\u065F\\u0670\\u06D6-\\u06ED]\")"` | — |
| [SRC-686F71AA50-L000125](../../agents/task_understanding.py#L125) | 125 | `"_PUNCTUATION = re.compile(r\"[؟?!.،,؛;:(){}\\[\\]\\\"'«»]+\")"` | — |
| [SRC-686F71AA50-L000126](../../agents/task_understanding.py#L126) | 126 | `"_SPACE = re.compile(r\"\\s+\")"` | — |
| [SRC-686F71AA50-L000127](../../agents/task_understanding.py#L127) | 127 | `"_TOKEN_RE = re.compile(r\"[a-z0-9]+\|[\\u0600-\\u06FF]+\", re.IGNORECASE)"` | — |
| [SRC-686F71AA50-L000128](../../agents/task_understanding.py#L128) | 128 | `""` | — |
| [SRC-686F71AA50-L000129](../../agents/task_understanding.py#L129) | 129 | `"_PATTERNS: dict[str, tuple[str, ...]] = {"` | — |
| [SRC-686F71AA50-L000130](../../agents/task_understanding.py#L130) | 130 | `"    \"official_site_lookup\": ("` | — |
| [SRC-686F71AA50-L000131](../../agents/task_understanding.py#L131) | 131 | `"        \"الموقع الرسمي\", \"موقع رسمي\", \"رابط الموقع الرسمي\", \"الصفحه الرسميه\","` | — |
| [SRC-686F71AA50-L000132](../../agents/task_understanding.py#L132) | 132 | `"        \"الموقع الحكومي\", \"official website\", \"official site\", \"official homepage\","` | — |
| [SRC-686F71AA50-L000133](../../agents/task_understanding.py#L133) | 133 | `"    ),"` | — |
| [SRC-686F71AA50-L000134](../../agents/task_understanding.py#L134) | 134 | `"    \"social_opinions\": ("` | — |
| [SRC-686F71AA50-L000135](../../agents/task_understanding.py#L135) | 135 | `"        \"اراء الناس\", \"اراء المستخدمين\", \"تجارب الناس\", \"تجارب المستخدمين\","` | — |
| [SRC-686F71AA50-L000136](../../agents/task_understanding.py#L136) | 136 | `"        \"تجارب الملاك\", \"تجارب ملاك\", \"تجربة مالك\", \"مراجعات المستخدمين\", \"الناس بتقول ايه\","` | — |
| [SRC-686F71AA50-L000137](../../agents/task_understanding.py#L137) | 137 | `"        \"real user reviews\", \"owner experience\", \"customer opinions\", \"people's opinions\","` | — |
| [SRC-686F71AA50-L000138](../../agents/task_understanding.py#L138) | 138 | `"        \"user experiences\", \"what do owners say\","` | — |
| [SRC-686F71AA50-L000139](../../agents/task_understanding.py#L139) | 139 | `"    ),"` | — |
| [SRC-686F71AA50-L000140](../../agents/task_understanding.py#L140) | 140 | `"    \"summarize\": ("` | — |
| [SRC-686F71AA50-L000141](../../agents/task_understanding.py#L141) | 141 | `"        \"لخص\", \"تلخيص\", \"ملخص\", \"summarize\", \"summarise\", \"summary of\","` | — |
| [SRC-686F71AA50-L000142](../../agents/task_understanding.py#L142) | 142 | `"    ),"` | — |
| [SRC-686F71AA50-L000143](../../agents/task_understanding.py#L143) | 143 | `"    \"troubleshoot\": ("` | — |
| [SRC-686F71AA50-L000144](../../agents/task_understanding.py#L144) | 144 | `"        \"حل مشكلة\", \"عطل\", \"اعطال\", \"مش بيشتغل\", \"لا يعمل\", \"خطأ\", \"رساله خطأ\","` | — |
| [SRC-686F71AA50-L000145](../../agents/task_understanding.py#L145) | 145 | `"        \"اصلح\", \"استكشاف الاعطال\", \"troubleshoot\", \"debug\", \"does not work\","` | — |
| [SRC-686F71AA50-L000146](../../agents/task_understanding.py#L146) | 146 | `"        \"not working\", \"error message\", \"fix the problem\", \"common failures\","` | — |
| [SRC-686F71AA50-L000147](../../agents/task_understanding.py#L147) | 147 | `"    ),"` | — |
| [SRC-686F71AA50-L000148](../../agents/task_understanding.py#L148) | 148 | `"    \"how_to\": ("` | — |
| [SRC-686F71AA50-L000149](../../agents/task_understanding.py#L149) | 149 | `"        \"ازاي\", \"كيف\", \"طريقة\", \"خطوات\", \"اشرح لي كيف\", \"علمني\", \"كيفية\","` | — |
| [SRC-686F71AA50-L000150](../../agents/task_understanding.py#L150) | 150 | `"        \"how to\", \"steps to\", \"walk me through\", \"teach me\","` | — |
| [SRC-686F71AA50-L000151](../../agents/task_understanding.py#L151) | 151 | `"    ),"` | — |
| [SRC-686F71AA50-L000152](../../agents/task_understanding.py#L152) | 152 | `"    \"compare\": ("` | — |
| [SRC-686F71AA50-L000153](../../agents/task_understanding.py#L153) | 153 | `"        \"قارن\", \"مقارنه\", \"الفرق بين\", \"ايهما افضل\", \"مميزات وعيوب\","` | — |
| [SRC-686F71AA50-L000154](../../agents/task_understanding.py#L154) | 154 | `"        \"الايجابيات والسلبيات\", \"مفاضله\", \"compare\", \"comparison\", \"versus\","` | — |
| [SRC-686F71AA50-L000155](../../agents/task_understanding.py#L155) | 155 | `"        \"trade-offs\", \"pros and cons\", \"which is better\","` | — |
| [SRC-686F71AA50-L000156](../../agents/task_understanding.py#L156) | 156 | `"    ),"` | — |
| [SRC-686F71AA50-L000157](../../agents/task_understanding.py#L157) | 157 | `"    \"current_information\": ("` | — |
| [SRC-686F71AA50-L000158](../../agents/task_understanding.py#L158) | 158 | `"        \"اليوم\", \"النهارده\", \"النهاردة\", \"دلوقتي\", \"الان\", \"حاليا\", \"احدث\","` | — |
| [SRC-686F71AA50-L000159](../../agents/task_understanding.py#L159) | 159 | `"        \"اخر الاخبار\", \"الاسعار الحاليه\", \"المواعيد الحاليه\", \"في الوقت الحالي\","` | — |
| [SRC-686F71AA50-L000160](../../agents/task_understanding.py#L160) | 160 | `"        \"today\", \"right now\", \"currently\", \"latest\", \"breaking news\", \"current price\","` | — |
| [SRC-686F71AA50-L000161](../../agents/task_understanding.py#L161) | 161 | `"        \"current hours\", \"this week\", \"this month\","` | — |
| [SRC-686F71AA50-L000162](../../agents/task_understanding.py#L162) | 162 | `"    ),"` | — |
| [SRC-686F71AA50-L000163](../../agents/task_understanding.py#L163) | 163 | `"    \"lead_generation\": ("` | — |
| [SRC-686F71AA50-L000164](../../agents/task_understanding.py#L164) | 164 | `"        \"عميل محتمل\", \"عملاء محتملين\", \"ابحث عن مشترين\", \"ابحث عن عميل\","` | — |
| [SRC-686F71AA50-L000165](../../agents/task_understanding.py#L165) | 165 | `"        \"دور على عملاء\", \"buyers looking to buy\", \"find prospects\", \"lead generation\","` | — |
| [SRC-686F71AA50-L000166](../../agents/task_understanding.py#L166) | 166 | `"        \"prospective customers\","` | — |
| [SRC-686F71AA50-L000167](../../agents/task_understanding.py#L167) | 167 | `"    ),"` | — |
| [SRC-686F71AA50-L000168](../../agents/task_understanding.py#L168) | 168 | `"    \"recommendation\": ("` | — |
| [SRC-686F71AA50-L000169](../../agents/task_understanding.py#L169) | 169 | `"        \"رشح\", \"ترشيح\", \"تنصحني\", \"هل اشتري\", \"اختار ايه\", \"افضل خيار\","` | — |
| [SRC-686F71AA50-L000170](../../agents/task_understanding.py#L170) | 170 | `"        \"recommend\", \"recommendation\", \"should i buy\", \"best option\", \"what should i choose\","` | — |
| [SRC-686F71AA50-L000171](../../agents/task_understanding.py#L171) | 171 | `"    ),"` | — |
| [SRC-686F71AA50-L000172](../../agents/task_understanding.py#L172) | 172 | `"    \"find_or_discover\": ("` | — |
| [SRC-686F71AA50-L000173](../../agents/task_understanding.py#L173) | 173 | `"        \"ابحث عن\", \"دور على\", \"دورلي على\", \"اعثر على\", \"هات رابط\", \"هاتلي\","` | — |
| [SRC-686F71AA50-L000174](../../agents/task_understanding.py#L174) | 174 | `"        \"فين الاقي\", \"اماكن بيع\", \"ابحث لي عن\", \"find\", \"search for\", \"look up\","` | — |
| [SRC-686F71AA50-L000175](../../agents/task_understanding.py#L175) | 175 | `"        \"where can i find\", \"list of\","` | — |
| [SRC-686F71AA50-L000176](../../agents/task_understanding.py#L176) | 176 | `"    ),"` | — |
| [SRC-686F71AA50-L000177](../../agents/task_understanding.py#L177) | 177 | `"    \"medical_information\": ("` | — |
| [SRC-686F71AA50-L000178](../../agents/task_understanding.py#L178) | 178 | `"        \"اعراض\", \"أعراض\", \"جرعة\", \"جرعات\", \"دواء\", \"ادوية\", \"علاج\", \"تشخيص\","` | — |
| [SRC-686F71AA50-L000179](../../agents/task_understanding.py#L179) | 179 | `"        \"medical symptoms\", \"dosage\", \"medicine\", \"medication\", \"treatment\", \"diagnosis\","` | — |
| [SRC-686F71AA50-L000180](../../agents/task_understanding.py#L180) | 180 | `"    ),"` | — |
| [SRC-686F71AA50-L000181](../../agents/task_understanding.py#L181) | 181 | `"    \"legal_information\": ("` | — |
| [SRC-686F71AA50-L000182](../../agents/task_understanding.py#L182) | 182 | `"        \"قانون\", \"قانوني\", \"نص قانوني\", \"عقد\", \"دعوى\", \"لائحة\", \"تشريع\","` | — |
| [SRC-686F71AA50-L000183](../../agents/task_understanding.py#L183) | 183 | `"        \"legal advice\", \"law\", \"contract\", \"lawsuit\", \"regulation\", \"legislation\","` | — |
| [SRC-686F71AA50-L000184](../../agents/task_understanding.py#L184) | 184 | `"    ),"` | — |
| [SRC-686F71AA50-L000185](../../agents/task_understanding.py#L185) | 185 | `"    \"coding_or_technical_design\": ("` | — |
| [SRC-686F71AA50-L000186](../../agents/task_understanding.py#L186) | 186 | `"        \"اكتب كود\", \"برمج\", \"كود بايثون\", \"اشرح الكود\", \"راجع الكود\","` | — |
| [SRC-686F71AA50-L000187](../../agents/task_understanding.py#L187) | 187 | `"        \"الكود التالي\", \"تصميم api\", \"اكتب سكربت\", \"code\", \"programming\","` | — |
| [SRC-686F71AA50-L000188](../../agents/task_understanding.py#L188) | 188 | `"        \"python code\", \"javascript\", \"api design\", \"stack trace\", \"unit test\","` | — |
| [SRC-686F71AA50-L000189](../../agents/task_understanding.py#L189) | 189 | `"        \"refactor\", \"debug this code\","` | — |
| [SRC-686F71AA50-L000190](../../agents/task_understanding.py#L190) | 190 | `"    ),"` | — |
| [SRC-686F71AA50-L000191](../../agents/task_understanding.py#L191) | 191 | `"    \"data_analysis\": ("` | — |
| [SRC-686F71AA50-L000192](../../agents/task_understanding.py#L192) | 192 | `"        \"حلل البيانات\", \"تحليل البيانات\", \"ملف csv\", \"تحليل جدول\", \"احسب المتوسط\","` | — |
| [SRC-686F71AA50-L000193](../../agents/task_understanding.py#L193) | 193 | `"        \"data analysis\", \"analyze data\", \"analyse data\", \"dataset\", \"spreadsheet\","` | — |
| [SRC-686F71AA50-L000194](../../agents/task_understanding.py#L194) | 194 | `"        \"csv file\", \"trend analysis\", \"calculate average\", \"pivot table\","` | — |
| [SRC-686F71AA50-L000195](../../agents/task_understanding.py#L195) | 195 | `"    ),"` | — |
| [SRC-686F71AA50-L000196](../../agents/task_understanding.py#L196) | 196 | `"    \"calculation\": ("` | — |
| [SRC-686F71AA50-L000197](../../agents/task_understanding.py#L197) | 197 | `"        \"احسب\", \"كم يساوي\", \"ما ناتج\", \"حساب النسبة\", \"احسب الفرق\","` | — |
| [SRC-686F71AA50-L000198](../../agents/task_understanding.py#L198) | 198 | `"        \"calculate\", \"compute\", \"what is the result\", \"percentage calculation\","` | — |
| [SRC-686F71AA50-L000199](../../agents/task_understanding.py#L199) | 199 | `"        \"how many\", \"how much is\","` | — |
| [SRC-686F71AA50-L000200](../../agents/task_understanding.py#L200) | 200 | `"    ),"` | — |
| [SRC-686F71AA50-L000201](../../agents/task_understanding.py#L201) | 201 | `"    \"translation\": ("` | — |
| [SRC-686F71AA50-L000202](../../agents/task_understanding.py#L202) | 202 | `"        \"ترجم\", \"ترجمة\", \"ترجم إلى\", \"ترجم للانجليزية\", \"ترجم للعربية\","` | — |
| [SRC-686F71AA50-L000203](../../agents/task_understanding.py#L203) | 203 | `"        \"translate\", \"translation\", \"translate into\", \"localize this\","` | — |
| [SRC-686F71AA50-L000204](../../agents/task_understanding.py#L204) | 204 | `"    ),"` | — |
| [SRC-686F71AA50-L000205](../../agents/task_understanding.py#L205) | 205 | `"    \"writing_or_editing\": ("` | — |
| [SRC-686F71AA50-L000206](../../agents/task_understanding.py#L206) | 206 | `"        \"اكتب\", \"اكتب رسالة\", \"اكتب بريد\", \"اعد صياغة\", \"أعد صياغة\","` | — |
| [SRC-686F71AA50-L000207](../../agents/task_understanding.py#L207) | 207 | `"        \"صحح لغويا\", \"راجع النص\", \"حسن الصياغة\", \"draft\", \"write\", \"rewrite\","` | — |
| [SRC-686F71AA50-L000208](../../agents/task_understanding.py#L208) | 208 | `"        \"proofread\", \"edit this\", \"polish this\", \"compose an email\","` | — |
| [SRC-686F71AA50-L000209](../../agents/task_understanding.py#L209) | 209 | `"    ),"` | — |
| [SRC-686F71AA50-L000210](../../agents/task_understanding.py#L210) | 210 | `"    \"planning\": ("` | — |
| [SRC-686F71AA50-L000211](../../agents/task_understanding.py#L211) | 211 | `"        \"ضع خطة\", \"خطة عمل\", \"خطة زمنية\", \"جدول زمني\", \"خطوات تنفيذ\","` | — |
| [SRC-686F71AA50-L000212](../../agents/task_understanding.py#L212) | 212 | `"        \"نظم لي\", \"رتب لي\", \"plan\", \"planning\", \"roadmap\", \"itinerary\","` | — |
| [SRC-686F71AA50-L000213](../../agents/task_understanding.py#L213) | 213 | `"        \"project schedule\", \"timeline\", \"project plan\","` | — |
| [SRC-686F71AA50-L000214](../../agents/task_understanding.py#L214) | 214 | `"    ),"` | — |
| [SRC-686F71AA50-L000215](../../agents/task_understanding.py#L215) | 215 | `"    \"creative_generation\": ("` | — |
| [SRC-686F71AA50-L000216](../../agents/task_understanding.py#L216) | 216 | `"        \"اكتب قصة\", \"قصة قصيرة\", \"قصيدة\", \"سيناريو\", \"اقترح افكار\","` | — |
| [SRC-686F71AA50-L000217](../../agents/task_understanding.py#L217) | 217 | `"        \"اقترح أفكار\", \"عصف ذهني\", \"brainstorm\", \"creative writing\","` | — |
| [SRC-686F71AA50-L000218](../../agents/task_understanding.py#L218) | 218 | `"        \"write a story\", \"poem\", \"generate ideas\","` | — |
| [SRC-686F71AA50-L000219](../../agents/task_understanding.py#L219) | 219 | `"    ),"` | — |
| [SRC-686F71AA50-L000220](../../agents/task_understanding.py#L220) | 220 | `"    \"explain_or_define\": ("` | — |
| [SRC-686F71AA50-L000221](../../agents/task_understanding.py#L221) | 221 | `"        \"ما معنى\", \"يعني ايه\", \"ما هو\", \"ما هي\", \"اشرح\", \"وضح مفهوم\","` | — |
| [SRC-686F71AA50-L000222](../../agents/task_understanding.py#L222) | 222 | `"        \"what is\", \"what does\", \"explain\", \"define\","` | — |
| [SRC-686F71AA50-L000223](../../agents/task_understanding.py#L223) | 223 | `"    ),"` | — |
| [SRC-686F71AA50-L000224](../../agents/task_understanding.py#L224) | 224 | `"    \"general_research\": ("` | — |
| [SRC-686F71AA50-L000225](../../agents/task_understanding.py#L225) | 225 | `"        \"بحث عميق\", \"بحث شامل\", \"بحث معمق\", \"تحقق من\", \"مصادر موثوقه\","` | — |
| [SRC-686F71AA50-L000226](../../agents/task_understanding.py#L226) | 226 | `"        \"اذكر المصادر\", \"مع مصادر\", \"بالمصادر\", \"deep research\", \"research\","` | — |
| [SRC-686F71AA50-L000227](../../agents/task_understanding.py#L227) | 227 | `"        \"verify\", \"fact check\", \"with sources\", \"cite sources\","` | — |
| [SRC-686F71AA50-L000228](../../agents/task_understanding.py#L228) | 228 | `"    ),"` | — |
| [SRC-686F71AA50-L000229](../../agents/task_understanding.py#L229) | 229 | `"    \"output_concise\": ("` | — |
| [SRC-686F71AA50-L000230](../../agents/task_understanding.py#L230) | 230 | `"        \"باختصار\", \"بإيجاز\", \"مختصر\", \"من غير إطالة\", \"بدون إطالة\","` | — |
| [SRC-686F71AA50-L000231](../../agents/task_understanding.py#L231) | 231 | `"        \"briefly\", \"in brief\", \"concise\", \"short answer\", \"keep it short\","` | — |
| [SRC-686F71AA50-L000232](../../agents/task_understanding.py#L232) | 232 | `"    ),"` | — |
| [SRC-686F71AA50-L000233](../../agents/task_understanding.py#L233) | 233 | `"    \"output_detailed\": ("` | — |
| [SRC-686F71AA50-L000234](../../agents/task_understanding.py#L234) | 234 | `"        \"بالتفصيل\", \"شرح وافي\", \"اشرح بالتفصيل\", \"خطوة بخطوة\","` | — |
| [SRC-686F71AA50-L000235](../../agents/task_understanding.py#L235) | 235 | `"        \"in detail\", \"step by step\", \"comprehensive explanation\", \"walkthrough\","` | — |
| [SRC-686F71AA50-L000236](../../agents/task_understanding.py#L236) | 236 | `"    ),"` | — |
| [SRC-686F71AA50-L000237](../../agents/task_understanding.py#L237) | 237 | `"    \"output_examples\": ("` | — |
| [SRC-686F71AA50-L000238](../../agents/task_understanding.py#L238) | 238 | `"        \"مع مثال\", \"امثلة\", \"مثال عملي\", \"بأمثلة\", \"for example\","` | — |
| [SRC-686F71AA50-L000239](../../agents/task_understanding.py#L239) | 239 | `"        \"give examples\", \"practical example\", \"worked example\","` | — |
| [SRC-686F71AA50-L000240](../../agents/task_understanding.py#L240) | 240 | `"    ),"` | — |
| [SRC-686F71AA50-L000241](../../agents/task_understanding.py#L241) | 241 | `"    \"output_table\": ("` | — |
| [SRC-686F71AA50-L000242](../../agents/task_understanding.py#L242) | 242 | `"        \"في جدول\", \"اعمل جدول\", \"جدول مقارنة\", \"as a table\", \"in a table\","` | — |
| [SRC-686F71AA50-L000243](../../agents/task_understanding.py#L243) | 243 | `"        \"comparison table\", \"tabulate\","` | — |
| [SRC-686F71AA50-L000244](../../agents/task_understanding.py#L244) | 244 | `"    ),"` | — |
| [SRC-686F71AA50-L000245](../../agents/task_understanding.py#L245) | 245 | `"    \"output_bullets\": ("` | — |
| [SRC-686F71AA50-L000246](../../agents/task_understanding.py#L246) | 246 | `"        \"نقاط\", \"على شكل نقاط\", \"قائمة\", \"bullet points\", \"as a list\","` | — |
| [SRC-686F71AA50-L000247](../../agents/task_understanding.py#L247) | 247 | `"        \"in bullets\", \"checklist\","` | — |
| [SRC-686F71AA50-L000248](../../agents/task_understanding.py#L248) | 248 | `"    ),"` | — |
| [SRC-686F71AA50-L000249](../../agents/task_understanding.py#L249) | 249 | `"    \"output_beginner_friendly\": ("` | — |
| [SRC-686F71AA50-L000250](../../agents/task_understanding.py#L250) | 250 | `"        \"ببساطة\", \"بشرح بسيط\", \"للمبتدئين\", \"من الصفر\", \"بلغة سهلة\","` | — |
| [SRC-686F71AA50-L000251](../../agents/task_understanding.py#L251) | 251 | `"        \"simple language\", \"beginner friendly\", \"beginner-friendly\","` | — |
| [SRC-686F71AA50-L000252](../../agents/task_understanding.py#L252) | 252 | `"        \"explain like i'm five\", \"eli5\","` | — |
| [SRC-686F71AA50-L000253](../../agents/task_understanding.py#L253) | 253 | `"    ),"` | — |
